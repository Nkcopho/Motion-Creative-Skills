---
name: scene-spec
description: >-
  Turn approved art direction into renderer-agnostic, implementable scene and asset specifications.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Scene Spec

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Approved brief, scene IDs, object registry, material/camera/motion plans, renderer.

## Procedure
1. Define units, axes, origin, camera frame, fps, colour management and deliverable format.
2. Map objects to parent/child transforms, geometry construction, LOD, material IDs, visibility, contact and clipping.
3. Define lights, environment, camera and focus, render passes and candidate post effects; note renderer limitations.
4. Specify UI geometry vs texture, fonts and asset provenance; reserve semantic interaction states.
5. Check ID integrity, duration and references; give explicit build order and measurable QA criteria.

## Outputs
scene.json; asset-list.md; implementation-plan.md. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
No dangling IDs, unspecified critical axes/units, unsupported assets or implicit production facts.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/MASTER_SPECIFICATION.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/06_QA/QUALITY_GATES.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
