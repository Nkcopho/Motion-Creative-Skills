# Quality assurance and acceptance criteria
## Distinguish two modes
Reference reconstruction: compare source/render at equivalent timestamps, matched projection, resolution, colour handling and crop; compare silhouettes/landmarks and perceptual appearance. Creative transfer: evaluate semantic role, cohesion, clarity and product-specific brand quality. Do not apply Microsoft pixel/colour targets to a different creative world.
## Proposed reconstruction tolerances (not achieved)
| Test | Target | Method / caveat |
|---|---|---|
| Major visible objects | All registered major objects for tested shot | Manually reconcile source masks; clipped/unknown groups separate. |
| Principal landmark position | <=1% frame width (~13.3 px) | Mean and max residual, source vs render, matched camera. |
| Silhouette overlap | IoU >=.90 where segmentation reliable | Mask both, report occlusion and uncertain edges; no false masks. |
| Projected scale | Within 3% | Equivalent visible bounds, independent camera compensation. |
| Colour | Mean CIEDE2000 <3 in matched sample ROIs | Convert consistently, control capture/render colour, report limitations. |
| Motion events | Within 2 captured frames (~67ms) | Annotated start/end, not original production frame. |
| Trajectory error | Mean <1% width | Track stable ID after camera alignment, report missing frames. |
| Typography | Alignment within 2–4 px at 1328×744 | Match baseline/legibility, do not claim exact font. |
| Grid pitch | Within 5% | Multiple locations/angles; perspective matters. |
| Material | Matched qualitative and sampled edge/highlight/shadow profiles | No universal shader numbers. |
| Camera | Align multiple non-moving landmarks across views | World camera not uniquely determined. |
| Continuity | No unexplained ID/geometry changes | Maintain state/visibility ledger. |
## Creative transfer rubric (100 possible points; weights proposed)
Product meaning and narrative 15; spatial hierarchy and composition 15; object role and geometric grammar 12; material/optics 12; microdetail and scale 8; camera/focus 8; semantic interaction/reflow 10; collective choreography 10; emotional tone/visual economy 5; consistency and technical QA 5. Score independently using evidence, not self-praise. A gate fails if core functionality unreadable, brand claims unsupported, world visually flat despite required depth, assets violate user brief, or motion competes with narrative. Require actual render review before any fidelity score. Record untested separately, never assign pass by default. 95 research estimate is not target automatically achieved.
## Review procedure
1. Silhouette and composition contact sheet: compare object positions, negative space, visual weight, geometry at all relevant scales. 2. Material stills: inspect actual highlights, penumbrae, overlap, texture, translucency; compare against role not arbitrary gloss. 3. Motion: scrub frame-by-frame, note exact captured/production fps, state timing and stable landmarks. 4. Information: verify UI content, typography, responsive layout, meaningful feedback and CTA. 5. Full sequence: check spectacle/reading rhythm, no generic idle motion, scene continuity. 6. Counterfactual critique: remove/replace one element, test effect and regressions. 7. Deliver actual comparison screenshots, motion clip, project and change log if requested.
