---
name: fidelity
description: >-
  Validate source-to-render or role-to-deliverable fidelity using matched evidence and explicit tolerances.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Fidelity

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Source and actual output, comparison mode, timestamps, masks/landmarks where available.

## Procedure
1. Declare reconstruction versus creative transfer; match frames, resolution, projection, crop and colour handling for reconstruction.
2. Measure landmark residuals, visible scale, reliable mask IoU, sample colours and timing; report method, uncertainty and missing tests.
3. Review matched optical and focus cues; do not use pixel error alone as a quality measure.
4. For transfer, compare object roles and coherent hierarchies; do not demand source colour or logo resemblance.
5. Report each proposed tolerance separately; never equate 95% research readiness with output fidelity.

## Outputs
fidelity-report.md; review.json; comparison metrics and contact sheets. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
Actual comparison evidence, failed/untested tests explicit; no aggregate fidelity claims without coverage.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/06_QA/QUALITY_GATES.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/06_QA/EVIDENCE_AUDIT.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
