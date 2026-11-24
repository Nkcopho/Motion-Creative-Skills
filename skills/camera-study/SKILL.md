---
name: camera-study
description: >-
  Analyse or design shot framing, camera movement, focus and projection. Use when spatial readability or camera behaviour is the main task.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Camera Study

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Shot list or footage, landmarks, intended subject and format.

## Procedure
1. Mark information focal region, foreground/midground/background, horizon and reliable grid axes.
2. Estimate screen-space projection using multiple landmarks; report fit error and depth/parallax limits.
3. Separate roll, translation, scale and perspective changes; avoid claiming exact lens or world coordinates without calibration.
4. Measure apparent sharpness on comparable ROIs; distinguish optical focus, motion blur, typography and compression.
5. For design, specify shot purpose, framing, proposed camera settings, transitions, focus targets and hold/readability windows.

## Outputs
camera-plan.json; camera-study.md; landmark measurements. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
Camera choices serve information; inferred focal lengths and original extrinsics remain unknown.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/04_MEASUREMENTS/ribbon_camera.csv`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/04_MEASUREMENTS/landmarks_light_dark.csv`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/04_MEASUREMENTS/focus_proxy.csv`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/SHOT_ANALYSIS.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
