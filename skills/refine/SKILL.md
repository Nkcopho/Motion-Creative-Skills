---
name: refine
description: >-
  Execute bounded, evidence-driven creative refinement against a critique report.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Refine

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Actual project/output, review.json, target, maximum rounds, approval constraints.

## Procedure
1. Freeze baseline and record critical defects with evidence. Choose the highest-impact root cause first.
2. Change one coherent variable group at a time; record files changed, rationale and expected effect.
3. Re-render or re-test under matched conditions; compare to baseline and re-score applicable criteria.
4. Reject regressions, preserve approved decisions and log unsuccessful variants.
5. Stop when gates pass and target is evidenced, progress stalls, tools fail or round limit is reached. Report residual issues and seek human approval.

## Outputs
refinement-log.json; revised artifacts; review.json; before/after evidence. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
No repeated score inflation, actual improvement demonstrated, max rounds obeyed.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/06_QA/QUALITY_GATES.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/05_AGENT/TRANSFER_WORKFLOW.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
