---
name: critique
description: >-
  Critique actual creative outputs against an agreed brief and evidence-based quality gates.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Critique

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Deliverable or render, brief, mode, evaluation rubric, prior review.

## Procedure
1. Inspect actual output at relevant scales and timestamps. If unavailable assess plan only, not render fidelity.
2. Evaluate each criterion independently; cite frame/ROI/file evidence, distinguish severity, root cause and symptom.
3. Compare reconstruction using matched-source criteria; creative transfer uses role-based originality and coherence.
4. Record pass/fail/blocked/untested gates and scored criteria; do not hide critical failures behind averages.
5. Prioritise fixes by impact, testability and regressions; provide a specific next-pass plan.

## Outputs
review.json; critique.md; prioritized fixes. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
Score derived from rubric and observed evidence; critical failures block readiness.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/06_QA/QUALITY_GATES.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/06_QA/EVIDENCE_AUDIT.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
