---
name: material-study
description: >-
  Investigate or specify material, texture, lighting response and optical relationships for reference or original worlds.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Material Study

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Source crops or object registry, material intent, target renderer if known.

## Procedure
1. Classify opaque, satin, glossy, translucent, wire, flexible and patterned surfaces by visible behaviour.
2. Sample rendered RGB distributions across interior, edge, shadow and nearby ground; separate albedo from observed colour.
3. Measure texture repeat, orientation and apparent scale where resolvable; inspect directionality of colour transfer and shadow falloff.
4. Specify proposed material parameters with renderer units, ranges and assumptions; do not label them recovered.
5. Define tests at wide, hero and macro scale; compare opaque/translucent, matte/gloss and texture variants when building is permitted.

## Outputs
materials.json; optical-tests.md; texture and shadow evidence. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
Material hypotheses match observed behaviour or target role; no universal glow or shader values masquerading as source data.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/02_REGISTRIES/materials.csv`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/04_MEASUREMENTS/texture_repeat.csv`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/04_MEASUREMENTS/white_block_shadow.csv`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/MASTER_SPECIFICATION.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
