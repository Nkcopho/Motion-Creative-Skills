---
name: forensic
description: >-
  Analyse visual or video references with measurable evidence; use for deep reference breakdowns, not new creative production.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Forensic

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Source file, analytical scope, depth, frame rate if known.

## Procedure
1. Verify hashes, decode metadata and distinguish player overlays from authored content. Establish zero-based frames and pixel coordinates.
2. Extract contact sheets, mark scene boundaries and assign persistent shot-local IDs; inventory clipped, overlapping, embedded and repeated objects.
3. Decompose bodies, insets, bevels, layers, glyphs, optical effects and subobjects. Record visible bounds and confidence.
4. Measure selected contours, colour samples, camera-compensated changes and trajectories; record ROI, threshold, method, sample interval, units and error.
5. Separate observable events from possible physical causes; inspect exceptions and alternative explanations. Reconcile conflicting measurements by method, never by averaging.
6. Produce an evidence coverage audit. Distinguish estimated analytical readiness from exhaustive coverage and production fidelity.

## Outputs
object-registry.json; scene-ledger.json; evidence.csv; analysis.md; uncertainty-audit.md. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
Every measured claim links to source, frame and method; incomplete segmentation or inaccessible evidence is explicit.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/MASTER_SPECIFICATION.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/SHOT_ANALYSIS.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/06_QA/EVIDENCE_AUDIT.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/07_REPRODUCIBILITY/README.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
