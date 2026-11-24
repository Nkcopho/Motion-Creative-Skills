# Validation report — v1.0.0
Local Linux validation, November 24, 2026. Nine deterministic tests passed. Tests are structural and synthetic, not visual or agent performance tests.

- 20 skill manifests: YAML, name/folder match, unique names, description length and referenced source file existence.
- 8 JSON schemas: Draft 2020-12 schema validation and brief/review template validation.
- 4 pipeline definitions: valid skill references and forward-only stage dependencies.
- Original 281-file forensic archive: manifest checksums verified.
- Scoring: missing evidence and untested ratings rejected; zero coverage yields no complete score; critical failed gate blocks recorded readiness.
- Motion: cyclic dependencies and channels outside timeline rejected.
- Run ledger: refuses out-of-order passing stages and passes without evidence; changing upstream stage resets dependent stages.
- Generic video measurement: synthetic five-frame video decoded, expected three extracted frames at step two.

Not tested: Windows PowerShell execution, Codex/Claude discovery and invocation, model adherence to skill instructions, rendering, visual quality, human approval. No automatic claims of fidelity. `scripts/test_suite.py` can reproduce the local tests. Source evidence preserved unchanged; not all inherited measurements independently reproduced in this release.
