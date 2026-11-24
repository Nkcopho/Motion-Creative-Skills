#!/usr/bin/env python3
"""Local deterministic workflow utilities. No LLM, network or renderer invocation."""
import argparse, json, sys, pathlib, hashlib, re, shutil
ROOT=pathlib.Path(__file__).resolve().parent.parent

def load(p): return json.loads(pathlib.Path(p).read_text(encoding='utf-8'))
def save(p,v):
    p=pathlib.Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
def emit(v): print(json.dumps(v,indent=2))
def validate(kind,data):
    import jsonschema
    jsonschema.Draft202012Validator(load(ROOT/'schemas'/f'{kind}.schema.json')).validate(data)
    def unique(rows,key='id'):
        ids=[r[key] for r in rows]; assert len(ids)==len(set(ids)),f'Duplicate {key}';return set(ids)
    if kind in ('scene','object-registry'):
        ids=unique(data['objects']); parents={o['id']:o.get('parent_id') for o in data['objects']}
        for id,p in parents.items():
            seen={id}
            while p is not None:
                assert p in ids and p not in seen, 'Missing or cyclic parent';seen.add(p);p=parents[p]
        if kind=='scene':
            mids=unique(data['materials']);assert all(o['material'] in mids for o in data['objects']),'Unknown material ID'
    if kind=='motion':
        ids=unique(data['channels']); by={r['id']:r for r in data['channels']}
        for c in data['channels']:
            assert c['start_s']<=c['end_s']<=data['duration_s'],'Channel outside timeline'
            times=[k['t'] for k in c['keyframes']];assert times==sorted(times) and all(c['start_s']<=t<=c['end_s'] for t in times),'Invalid keyframe times'
            for d in c['depends_on']:
                assert d in ids and d!=c['id'],'Unknown/self dependency'
                assert by[d]['start_s']<=c['start_s'],'Dependency starts after dependent'
        def visit(i,stack):
            assert i not in stack,'Cyclic motion dependency'
            for d in by[i]['depends_on']:visit(d,stack|{i})
        for i in ids:visit(i,set())
    if kind=='review':
        rubric=load(ROOT/'evaluations/rubric.json')
        assert unique(data['criteria'])=={r['id'] for r in rubric['criteria']},'Missing/extra criteria'
        assert unique(data['gates'])=={r['id'] for r in rubric['gates']},'Missing/extra gates'
        for r in data['criteria']:
            if r['status']=='tested':assert r['rating'] is not None and r['evidence'],'Tested requires rating and evidence'
            else:assert r['rating'] is None,'Untested cannot be scored'
        for g in data['gates']:
            if g['status'] in ('pass','fail'):assert g['evidence'],'Gate verdict needs evidence'
        assert data['human_approved']==(next(g for g in data['gates'] if g['id']=='G10')['status']=='pass'),'Human approval and G10 disagree'
    return data

def score(data):
    validate('review',data); weights={r['id']:r['weight'] for r in load(ROOT/'evaluations/rubric.json')['criteria']}
    tested=[r for r in data['criteria'] if r['status']=='tested'];coverage=sum(weights[r['id']] for r in tested)
    points=sum(weights[r['id']]*r['rating']/5 for r in tested); blockers=[g['id'] for g in data['gates'] if g['status']!='pass']
    # Structural validation cannot authenticate evidence or human sign-off.
    return {'weighted_points_of_100':round(points,2),'tested_weight_percent':coverage,'score_on_tested_only':round(100*points/coverage,2) if coverage else None,'complete_score':round(points,2) if coverage==100 else None,'blocking_gates':blockers,'recorded_ready':coverage==100 and points>=data['target'] and not blockers and data['human_approved'],'caveat':'Arithmetic and record consistency only; not independent proof of evidence or approval.'}

def check_suite():
    import yaml,jsonschema
    idx=load(ROOT/'skills-index.json'); assert len(idx)==20;names=set()
    for row in idx:
        f=ROOT/row['file']; raw=f.read_text(encoding='utf-8'); meta=yaml.safe_load(raw.split('---',2)[1]);n=meta['name'];assert n==f.parent.name and n==row['name'] and re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',n) and len(n)<=64;assert 0<len(meta['description'])<=1024;assert n not in names;names.add(n)
        for ref in re.findall(r'`(references/microsoft-outlook/[^`]+)`',raw): assert (ROOT/ref).is_file(),ref
    for f in (ROOT/'schemas').glob('*.json'):jsonschema.Draft202012Validator.check_schema(load(f))
    for f in (ROOT/'pipelines').glob('*.json'):
        prior=set()
        for s in load(f)['stages']:
            assert s['id'] not in prior and set(s['depends_on'])<=prior and set(s['skills'])<=names;prior.add(s['id'])
    validate('brief',load(ROOT/'templates/brief.json'));validate('review',load(ROOT/'templates/review.json'))
    pack=ROOT/'references/microsoft-outlook/Outlook_Forensic_Agent_Pack'
    files=list(pack.rglob('*'));count=sum(f.is_file() for f in files)
    assert count==281,count
    bad=[];manifest=pack/'MANIFEST.sha256'
    for line in manifest.read_text().splitlines():
        if not line.strip():continue
        h,rel=line.split(maxsplit=1);rel=rel.strip().lstrip('*');p=pack/rel
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=h:bad.append(rel)
    assert not bad,f'Bad source checksums: {bad[:5]}'
    return {'skills':len(names),'pipelines':4,'schemas':len(list((ROOT/'schemas').glob('*.json'))),'reference_files':count,'source_manifest':'pass','template_validation':'pass','native_agent_runtime':'untested'}

def main():
    p=argparse.ArgumentParser(description=__doc__);sp=p.add_subparsers(dest='cmd',required=True)
    sp.add_parser('check-suite');sp.add_parser('list');q=sp.add_parser('plan');q.add_argument('pipeline');q=sp.add_parser('init');q.add_argument('directory');q.add_argument('--project',required=True);q.add_argument('--pipeline',default='creative-development');q=sp.add_parser('validate');q.add_argument('kind');q.add_argument('file');q=sp.add_parser('score');q.add_argument('file');q=sp.add_parser('gate');q.add_argument('run');q.add_argument('stage');q.add_argument('status',choices=['pass','fail','blocked','untested','skipped']);q.add_argument('--evidence',action='append',default=[]);q.add_argument('--human-approved',action='store_true')
    a=p.parse_args()
    def pipeline(n):
        assert n in [f.stem for f in (ROOT/'pipelines').glob('*.json')],'Unknown pipeline';return load(ROOT/'pipelines'/f'{n}.json')
    if a.cmd=='check-suite':emit(check_suite())
    elif a.cmd=='list':emit(load(ROOT/'skills-index.json'))
    elif a.cmd=='plan':emit(pipeline(a.pipeline))
    elif a.cmd=='init':
        path=pathlib.Path(a.directory);assert not (path/'run.json').exists(),'Run already exists';plan=pipeline(a.pipeline);path.mkdir(parents=True,exist_ok=True)
        save(path/'run.json',{'project':a.project,'pipeline':a.pipeline,'stages':[{'id':s['id'],'status':'pending','evidence':[]} for s in plan['stages']]})
        for f in (ROOT/'templates').iterdir():
            if not (path/f.name).exists():shutil.copy2(f,path/f.name)
        brief=load(path/'brief.json');brief['project']=a.project;save(path/'brief.json',brief);emit({'run':str(path/'run.json'),'note':'Fill actual brief before proceeding.'})
    elif a.cmd=='validate':validate(a.kind,load(a.file));emit({'schema':a.kind,'status':'pass'})
    elif a.cmd=='score':emit(score(load(a.file)))
    elif a.cmd=='gate':
        run=validate('run',load(a.run));plan=pipeline(run['pipeline']);by={s['id']:s for s in run['stages']};spec={s['id']:s for s in plan['stages']};assert set(by)==set(spec) and len(by)==len(run['stages']),'Invalid stage ledger';assert a.stage in by,'Unknown stage'
        if a.status=='pass':
            assert all(by[d]['status']=='pass' for d in spec[a.stage]['depends_on']),'Prior dependency has not passed'
            assert a.evidence,'Evidence required'
            if a.stage=='approval':assert a.human_approved,'Actual human approval must be explicitly recorded'
        if a.status=='fail':assert a.evidence,'Failure evidence required'
        by[a.stage].update(status=a.status,evidence=a.evidence)
        # invalidate later passes when upstream changes, including a re-pass
        affected={a.stage}
        for s in plan['stages']:
            if s['id']!=a.stage and affected.intersection(s['depends_on']):
                affected.add(s['id']);by[s['id']].update(status='pending',evidence=[])
        save(a.run,run);emit(run)
if __name__=='__main__':
    try: main()
    except Exception as e: print(f'ERROR: {e}',file=sys.stderr);sys.exit(1)
