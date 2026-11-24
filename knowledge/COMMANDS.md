# Command conventions
Codex interactive: `$skill-name` followed by natural language or options. Claude Code: `/skill-name` followed by arguments. Shell: `python scripts/umpha.py ...` is a local helper, not a model launcher. Options in agent prompts are conventions, not native CLI parsers.
- --mode=analyse|develop|implement|evaluate|full (default depends on skill/request)
- --depth=quick|detailed|forensic|exhaustive (exhaustive requires measured coverage, not a promise)
- --target=0..100 (evaluation aspiration), --rounds=1..10 (cap)
- --brand, --reference, --engine, --output, --strict, --approval=manual|auto (auto never bypasses host permissions or human approval gate)
- Reconstruction compares matched pixels/landmarks; transfer compares role, meaning, originality, coherence. Default creative mode is transfer.
Examples: `$worldbuild --brand=Cause --mode=develop --reference=outlook` ; `/forensic ./reference.mp4 --depth=forensic` ; `$creative-director --brief=brief.md --mode=full --target=95 --rounds=5` ; `/critique ./renders --target=95`.
