---
name: visual-intelligence
description: >-
  Extract transferable spatial, material and semantic design rules from reference research.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Visual Intelligence

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Evidence ledger or source, target problem if available.

## Procedure
1. Identify geometric vocabulary and operations: nest, stack, offset, repeat, sweep, bend, embed, occlude, reflow, assemble.
2. Map world/system/component/object/construction/micro scales and spatial, material, motion, information and focus hierarchies.
3. Measure or describe where visual density, saturation and motion shift across scenes. Test threshold sensitivity if using proxies.
4. Assign each key element a visual responsibility and distinguish recurring literal, geometric and semantic identities.
5. Separate robust patterns from exceptions; express principles as condition/action/rationale/evidence/exception records.

## Outputs
principles.json; visual-system.md; exception-ledger.md. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
Rules are conditional and transferable, not superficial palette/prop copying.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/CREATIVE_CAUSALITY.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/MASTER_SPECIFICATION.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/04_MEASUREMENTS/regional_activity.csv`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
