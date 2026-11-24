---
name: motion-study
description: >-
  Measure object motion, temporal events and deformation in footage. Use for analysis rather than new choreography.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Motion Study

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Source video, object IDs, stable landmarks, time interval.

## Procedure
1. Verify decode cadence; use captured frame times rather than assuming original production fps.
2. Track stable landmarks and fit suitable similarity/affine/projective image transform; report inliers and residuals.
3. Track object position, bounds, visibility, orientation and constituent state against the registered environment.
4. Separate camera-induced changes, translation, deformation, illumination and occlusion; bracket ambiguous events.
5. Calculate finite-difference velocity and acceleration only with reliable timing; fit candidate curves and report errors; do not infer spring constants from sparse data.

## Outputs
motion.json; trajectories.csv; tracking-audit.md. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
Trajectories are tied to IDs, frame indices, units, uncertainty and camera model; gaps are not silently interpolated.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/04_MEASUREMENTS/sphere_tracking.csv`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/04_MEASUREMENTS/ribbon_boundary.csv`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/04_MEASUREMENTS/regional_activity.csv`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/06_QA/EVIDENCE_AUDIT.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
