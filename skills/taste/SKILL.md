---
name: taste
description: >-
  Develop creative judgment through counterfactual art direction and structured review of approved and rejected work.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Taste

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Reference or actual creative outputs, brief, prior evaluations where available.

## Procedure
1. Identify perceptual problem and observed choice; document why it may work without asserting creator intent.
2. Generate at least two materially different alternatives, including removal or simplification.
3. Compare semantic, spatial, material, perceptual, temporal and emotional consequences; mark hypothetical vs tested.
4. If implementation authorized, test one variable at a time with locked framing/exposure and record before/after and regression.
5. Save versioned taste records with evidence, scope, exceptions and human approval status. Never treat a guessed preference as approved.

## Outputs
taste-records.json; counterfactuals.md. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
At least one plausible alternative per hero decision; claims of causal effect require an actual test.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/CREATIVE_CAUSALITY.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/06_QA/EVIDENCE_AUDIT.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
