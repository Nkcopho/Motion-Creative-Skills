---
name: brand-translate
description: >-
  Translate reference design intelligence into an original brand system; avoid superficial reskinning.
metadata:
  author: umpha-digital
  version: "1.0.0"
---

# Brand Translate

## Operating rules
Read `references/workspace.md` to locate the shared suite root. Read `knowledge/OPERATING_CONTRACT.md` there first. Paths below are relative to that root. Load only relevant evidence, not all 197 frames by default. If the shared library is unavailable, report the missing dependency and work only with available evidence; do not invent it.

Use the invocation arguments as agent instructions, not shell flags. Respect `--mode`, `--depth`, `--target`, `--rounds`, `--brand`, `--reference`, `--engine`, `--output` and `--strict` when present. State assumptions and missing inputs. Do not run destructive actions, install dependencies or invoke external paid services without permission. Keep source references read-only. Write new deliverables in the requested project/run directory. Use the relevant schemas and templates; record evidence and uncertainty. If asked only for analysis or direction, do not implement or render.

## Inputs
Brand guidelines, product meaning, audience, reference principles.

## Procedure
1. Separate essential relationship from reference-specific palette, logo, typography, UI and prop identities.
2. Map source roles to target visual responsibilities; propose multiple candidate objects per role.
3. Reject one-to-one swaps lacking functional or emotional meaning. Validate cultural and brand details against supplied evidence.
4. Define target geometry, material palette, type, colour allocation, motion character and originality constraints.
5. Compare role-level equivalence rather than Microsoft pixel similarity; document what is intentionally different.

## Outputs
brand-transfer.md; role-map.json; art-direction tokens. If a file is requested, actually create it; otherwise return the corresponding structured content.

## Acceptance gate
The result belongs to the target brand; no copied reference logos or proprietary assets unless explicitly authorized.

## Read as needed
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/05_AGENT/TRANSFER_WORKFLOW.md`
- `references/microsoft-outlook/Outlook_Forensic_Agent_Pack/01_MASTER/CREATIVE_CAUSALITY.md`
- `knowledge/TRANSFERABLE_PRINCIPLES.md`
- `evaluations/rubric.json` and `schemas/` as applicable.
- `scripts/umpha.py --help` for available local helpers.
