---
name: storyboard
description: >-
  Create conversion-led or explanatory narrative beats, shot lists and storyboards.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Storyboard

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Brief, audience, conversion action, duration, format, approved world.

## Procedure
1. Define viewer starting belief, pain point, promise, proof and CTA; avoid unsupported product claims.
2. Explore at least three opening hooks and select by relevance, comprehension and visual potential.
3. Map beats to shot duration, subject, visual action, camera, information, transition and audio intent.
4. Alternate spectacle with quiet comprehension; estimate reading windows and preserve consistent character/product identity.
5. Specify storyboard panel evidence, transitions and fallback if a shot cannot be implemented; check total duration.

## Outputs
storyboard.md; scene-ledger.json; animatic plan. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
Every shot advances narrative; CTA legible, duration reconciled, no unsupported claims.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/SHOT_ANALYSIS.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/05_AGENT/PRODUCTION_BRIEF_TEMPLATE.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
