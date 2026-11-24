---
name: choreography
description: >-
  Design coordinated camera, object and interaction animation with explicit timing dependencies.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Choreography

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Scene ledger, object registry, duration, desired behavior, fps.

## Procedure
1. Set shot clock, units, IDs and semantic state changes.
2. Plan separate channels for camera, rigid props, geometry, typography, lighting and visibility; specify dependencies, holds and triggers.
3. Transfer motion energy between regions; reserve playful overshoot for suitable objects, use restrained functional reflow.
4. Define keyframes and candidate easing; maintain layout constraints and text identity rather than scaling screenshots.
5. Check overlap, occlusion, motion blur, reduced-motion variant and comprehension; mark timing as proposed until rendered.

## Outputs
motion.json; dependency graph; choreography.md. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
No cycles or impossible timing, every primary move has a purpose, stable periods and read windows are explicit.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/02_REGISTRIES/behaviours.csv`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/04_MEASUREMENTS/regional_activity.csv`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/SHOT_ANALYSIS.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
