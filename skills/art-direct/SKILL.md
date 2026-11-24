---
name: art-direct
description: >-
  Set creative direction, emotional tone and aesthetic constraints for a project.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Art Direct

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Brief, audience, brand, references, deliverable constraints.

## Procedure
1. Articulate product meaning, intended perception and anti-goals.
2. Derive visual responsibilities and competing concept directions before picking assets.
3. Define geometric vocabulary, construction grammar, spatial hierarchy, colour/material contrast, typography and detail budget.
4. Define motion and camera personality, functional clarity and examples of prohibited generic treatment.
5. Select direction using reasoned tradeoffs; document unresolved questions and approval state.

## Outputs
direction.md; design-system.md; decision-log.json. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
Direction explains why, not only how it looks; no production-ready claim before appropriate approvals.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/CREATIVE_CAUSALITY.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/05_AGENT/TRANSFER_WORKFLOW.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
