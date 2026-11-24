---
name: blender
description: >-
  Implement or plan a Blender scene using approved geometry, materials, cameras and animation specifications.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Blender

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Approved scene spec, installed Blender version, renderer and asset provenance.

## Procedure
1. Inspect Blender availability and version. If unavailable produce a labelled script/spec, not a claimed rendered blend.
2. Set units, fps, resolution, colour management, collections, object origins and stable IDs.
3. Construct geometry and node materials with physically plausible relationships; distinguish Cycles vs Eevee limitations.
4. Set lighting, focal camera, keyframes and interpolation; test at benchmark times with low-cost previews before final.
5. Save source scene and logs if built; render stills and motion, inspect optical depth and regressions.

## Outputs
blend or generation script; render stills/clip if possible; test log. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
Source and actual renders only claimed when created and inspected; no invented Blender execution.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/06_QA/QUALITY_GATES.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/MASTER_SPECIFICATION.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
