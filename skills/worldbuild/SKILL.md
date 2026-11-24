---
name: worldbuild
description: >-
  Design a coherent product-specific 3D world, spatial architecture and asset system before implementation.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Worldbuild

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Product meaning, audience, brand constraints, scene goals, reference principles.

## Procedure
1. Define visual responsibilities before props. Establish emotional direction and three alternative world metaphors.
2. Select a metaphor through semantic fit, originality, spatial extensibility, material contrast and narrative potential.
3. Define world, system, component, object, construction and micro scales; provide ground reference, architecture, focal regions and local grouping.
4. Specify object roles, physically meaningful contact/elevation, cropped peripheral continuation, irregularity budget and optical interactions.
5. Build shot-local arrangements with protected reading space; map persistent identities and planned changes.
6. Test hero choices using taste; hand off to composition, material-study and scene-spec. Do not generate a render unless requested.

## Outputs
world-bible.md; object-registry.json; spatial-layout.json; scene concepts. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
World is not a dashboard with randomly floating props; every hero element earns its position and role.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/MASTER_SPECIFICATION.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/CREATIVE_CAUSALITY.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/05_AGENT/TRANSFER_WORKFLOW.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
