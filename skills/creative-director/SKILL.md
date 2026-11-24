---
name: creative-director
description: >-
  Orchestrate end-to-end creative work from brief through research, art direction, production and review. Use for multi-stage projects.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Creative Director

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Brief, product, audience, commercial goal, references, constraints, mode, renderer and target.

## Procedure
1. Read AGENTS.md, knowledge/OPERATING_CONTRACT.md and the selected pipeline. Resolve shared root via references/workspace.md.
2. Choose analyse, develop, implement, evaluate or full; initialise a run ledger and record brief assumptions. For analysis-only do not create scenes.
3. Execute applicable skill procedures in dependency order by reading their SKILL.md files directly. Native subskill calls or parallel agents are optional only if supported.
4. Require artifacts and evidence at each gate. Stop at blocked dependencies; human approval required where specified. Never auto-run production when only direction requested.
5. For implementation review actual renders and motion, invoke critique and refine with capped rounds; independently validate the result where possible.
6. Report completed, failed, blocked and untested stages, files, critical risks and next decisions. A numeric target is not a guarantee.

## Outputs
brief.json; run.json; direction.md; scene specs; review.json; delivery manifest. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
No stage advances past a failed critical gate; no final fidelity claim without actual inspected output.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/05_AGENT/TRANSFER_WORKFLOW.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/05_AGENT/PRODUCTION_BRIEF_TEMPLATE.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/06_QA/QUALITY_GATES.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
