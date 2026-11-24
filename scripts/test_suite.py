"""Deterministic local tests, not agent quality evaluations."""
import copy,json,subprocess,sys,tempfile,pathlib,unittest
import umpha
ROOT=umpha.ROOT
class Suite(unittest.TestCase):
 def test_manifest(self): self.assertEqual(umpha.check_suite()['skills'],20)
 def test_unscored(self):
  r=umpha.score(umpha.load(ROOT/'templates/review.json'));self.assertEqual(r['tested_weight_percent'],0);self.assertIsNone(r['complete_score']);self.assertFalse(r['recorded_ready'])
 def test_score_requires_evidence(self):
  r=umpha.load(ROOT/'templates/review.json');r['criteria'][0].update(status='tested',rating=5)
  with self.assertRaises(AssertionError):umpha.score(r)
 def test_no_untested_rating(self):
  r=umpha.load(ROOT/'templates/review.json');r['criteria'][0]['rating']=5
  with self.assertRaises(AssertionError):umpha.score(r)
 def test_complete_arithmetic_only(self):
  r=umpha.load(ROOT/'templates/review.json');r['human_approved']=True
  for c in r['criteria']:c.update(status='tested',rating=5,evidence=['SYNTHETIC TEST ONLY'])
  for g in r['gates']:g.update(status='pass',evidence=['SYNTHETIC TEST ONLY'])
  self.assertTrue(umpha.score(r)['recorded_ready']);r['gates'][1]['status']='fail';self.assertFalse(umpha.score(r)['recorded_ready'])
 def test_motion_cycles(self):
  c={'id':'a','object_id':'o','property':'x','start_s':0,'end_s':1,'depends_on':['b'],'keyframes':[{'t':0,'value':0}],'evidence':[]};d=copy.deepcopy(c);d.update(id='b',depends_on=['a'])
  with self.assertRaises(AssertionError):umpha.validate('motion',{'duration_s':1,'fps':30,'channels':[c,d]})
 def test_motion_outside(self):
  c={'id':'a','object_id':'o','property':'x','start_s':0,'end_s':2,'depends_on':[],'keyframes':[],'evidence':[]}
  with self.assertRaises(AssertionError):umpha.validate('motion',{'duration_s':1,'fps':30,'channels':[c]})
 def test_gate_dependencies_and_reset(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/'run.json'
   def cmd(*args):return subprocess.run([sys.executable,str(ROOT/'scripts/umpha.py'),*map(str,args)],capture_output=True)
   self.assertEqual(cmd('init',d,'--project','Synthetic','--pipeline','creative-development').returncode,0)
   self.assertNotEqual(cmd('gate',p,'world','pass','--evidence','test').returncode,0)
   self.assertNotEqual(cmd('gate',p,'direction','pass').returncode,0)
   self.assertEqual(cmd('gate',p,'direction','pass','--evidence','test').returncode,0)
   self.assertEqual(cmd('gate',p,'world','pass','--evidence','test').returncode,0)
   self.assertEqual(cmd('gate',p,'direction','fail','--evidence','test').returncode,0)
   self.assertEqual(umpha.load(p)['stages'][1]['status'],'pending')
 def test_measure(self):
  import cv2,numpy as np,csv
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d);video=p/'test.avi';v=cv2.VideoWriter(str(video),cv2.VideoWriter_fourcc(*'MJPG'),10,(64,48));self.assertTrue(v.isOpened())
   for i in range(5):v.write(np.full((48,64,3),i*40,dtype=np.uint8))
   v.release();r=subprocess.run([sys.executable,str(ROOT/'scripts/measure.py'),str(video),str(p/'out'),'--every','2'],capture_output=True);self.assertEqual(r.returncode,0,r.stderr.decode());self.assertEqual(umpha.load(p/'out/metadata.json')['decoded_frames'],5);self.assertEqual(len(list((p/'out/frames').glob('*.png'))),3)
if __name__=='__main__':unittest.main(verbosity=2)
