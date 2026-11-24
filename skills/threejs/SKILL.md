---
name: threejs
description: >-
  Implement and test an approved web-based Three.js creative scene or animation.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Threejs

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Approved scene spec, repository, available dependencies, browser/render access.

## Procedure
1. Inspect repository and installed Three.js version; use current project conventions and avoid destructive edits.
2. Build modular scene, assets, materials, cameras, lights and deterministic time controller; use explicit geometry thickness and appropriate colour space.
3. Implement responsive UI and interaction separately where appropriate; avoid assuming real transmission/caustics in raster rendering.
4. Add performance budgets, resize, reduced motion, loading and disposal; test actual target viewport and browser console.
5. Render representative timestamps, capture frames and compare against gates. If browser access unavailable, mark visual review untested.

## Outputs
working project; render captures; test log; performance notes. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
Actual build and runtime tested where available; no claiming visual fidelity from code alone.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/06_QA/QUALITY_GATES.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/05_AGENT/TRANSFER_WORKFLOW.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
