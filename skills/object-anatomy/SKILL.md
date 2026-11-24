---
name: object-anatomy
description: >-
  Decompose individual objects into geometry, components and physical relationships. Use for detailed asset specifications.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Object Anatomy

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Object IDs, source frames or design brief, intended viewing scales.

## Procedure
1. Identify silhouette and occlusions; separate visible bounds from hidden or inferred shape.
2. Annotate primitive bodies, recesses, inserts, wall thickness, bevels, seams, surfaces, glyphs and fasteners.
3. Record local axes, relative proportions, contact and elevation relationships, edge treatment and intended motion channels.
4. Differentiate physical meshes, embedded textures, functional text and optical effects. Propose mesh construction only as a candidate.
5. Inspect wide and macro views; record unknown rear faces and ambiguous masks.

## Outputs
object-registry.json; anatomy.md; component diagrams or annotated evidence. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
Every hero object has a role, constituent parts, spatial constraints and explicit unknowns.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/02_REGISTRIES/objects.json`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/03_EVIDENCE/crop_index.csv`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/MASTER_SPECIFICATION.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
