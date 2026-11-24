# Umpha Creative Intelligence v1.0.0
20 portable Agent Skills (including the master director), shared forensic research, workflow gates and local tools. This is an instruction-and-evidence system, not a trained model, autonomous renderer or installed PC app.

## Windows quick start
1. Extract the **entire** archive into a permanent private folder, e.g. `C:\Users\you\Documents\Umpha_Creative_Intelligence`. Do not run from inside the ZIP. The original source is third-party reference footage; keep the library private unless you have permission to redistribute it.
2. Open PowerShell in the extracted suite root (the folder containing this README). Review `installers/install.ps1` before running it.
3. Run `powershell -NoProfile -ExecutionPolicy RemoteSigned -File .\installers\install.ps1 -Agent both -Scope user` (or run `./installers/install.ps1 -Agent codex` from PowerShell if scripts are allowed). If Windows blocks a trusted downloaded script, review it and use `Unblock-File` on that script; no machine-wide policy change needed. Use `-Agent claude` for Claude only, `-Scope project -ProjectPath 'C:\path\project'` for project registration. `-Force` updates only owned registrations; existing unrelated skill names cause preflight failure. No admin required. Do not move the extracted suite after install; rerun with `-Force` if you move it.
4. Start a new Codex or Claude Code session in your target project. Use `$creative-director` in Codex or `/creative-director` in Claude Code. If not recognised, verify the relevant skills directory, session working directory and agent version. The installer does not install either agent or launch any model.
5. Example: `$worldbuild --brand=Cause --mode=develop --reference=outlook --target=95` then explain the brief. Claude Code uses `/worldbuild`. Options are natural-language conventions, not guaranteed native flags.

## Local tools (optional)
Install Python 3.10+ dependencies in a virtual environment: `python -m pip install -r requirements.txt`. No API key required. From the suite root:
```
python scripts/umpha.py check-suite
python scripts/umpha.py list
python scripts/umpha.py plan creative-development
python scripts/umpha.py init ./runs/cause --project Cause --pipeline creative-development
python scripts/umpha.py validate brief ./runs/cause/brief.json
python scripts/umpha.py score ./runs/cause/review.json
python scripts/umpha.py gate ./runs/cause/run.json direction pass --evidence path/to/actual-approved-direction.md
python scripts/measure.py path/to/video.mp4 ./runs/metrics --every 30
```
The gate command checks dependencies and presence of recorded evidence, not authenticity; never mark a gate passed without inspecting evidence. Approval gate requires explicit `--human-approved` only after actual human approval. Reopening an upstream stage resets dependent statuses. `score` reports coverage separately and cannot establish that an output looks good. The measurement helper produces frame proxies, not a full segmentation or camera solver. The inherited reference analysis has its own scripts and readme.

## Reading order
`AGENTS.md` → `knowledge/OPERATING_CONTRACT.md` → selected `skills/<name>/SKILL.md` → linked knowledge and evidence → pipeline, schemas, templates and rubric. `knowledge/COMMANDS.md` describes invocation conventions. `skills-index.json` is the full skill catalogue. The director coordinates other skills by reading their instructions; native sub-agent calls are not required or guaranteed.

## Reference and version control
The full 281-file Outlook archive is preserved under `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/`. It includes the original video, 197 decoded frames, 20 crops, 10 contact sheets, object data and the source audit. Keep it read-only. Do not commit private client material or third-party reference video to a public repo. Keep project-specific outputs in a separate run directory, and version taste records with actual approval status. The reference 95% estimate is conceptual, not output fidelity.

## Uninstall
`powershell -NoProfile -ExecutionPolicy RemoteSigned -File .\installers\uninstall.ps1 -Agent both -Scope user -WhatIf` previews removals; omit `-WhatIf` to remove only marked Umpha registrations. Shared files remain. For project scope specify the same project path.

## Compatibility and limitations
Codex `.agents/skills`, Claude Code `.claude/skills`; both use `SKILL.md` front matter. See official docs: https://developers.openai.com/codex/skills ; https://code.claude.com/docs/en/skills ; https://agentskills.io/specification . Installation paths were checked against current documentation. This release is statically validated in Linux; PowerShell execution and agent discovery/invocations on Windows require a local smoke test. No production rendering or agent performance benchmark was run. The original archive's source evidence and uncertainties are preserved. See TEST_REPORT.md for checks actually run.
