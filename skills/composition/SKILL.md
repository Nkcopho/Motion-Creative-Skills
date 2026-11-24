---
name: composition
description: >-
  Design or audit spatial layout, visual weight, negative space and attention across shots.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Composition

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Scene intent, format, object registry, reference or render.

## Procedure
1. Declare focal point, reading order, safe areas, camera distance and hierarchy per shot.
2. Map object bounds, proximity, local alignment, depth, contact, overlap and frame clipping.
3. Assess strong-edge and colour distribution when evidence permits; use consistent methods and do not equate proxies with gaze.
4. Reserve negative space for information, separation, optics, motion and attention; vary density over time.
5. Check silhouette at thumbnail, normal size and macro; test removal/repositioning of high-weight accents.

## Outputs
composition.md; spatial-layout.json; annotated frames or layouts. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
Focal subject reads without relying on explanatory prose; no accidental tangencies, competing accents or inaccessible UI.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/CREATIVE_CAUSALITY.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/04_MEASUREMENTS/landmarks_light_dark.csv`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/MASTER_SPECIFICATION.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
