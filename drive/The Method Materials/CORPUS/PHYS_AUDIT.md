
# Physics Compendium — Phase 2 audit (reader perspective)

| # | finding | status |
|---|---|---|
| P1 | All §-references resolve; no chapter-shift casualties here. | Verified. |
| P2 | The Λ_phys parameter entries were ASCII-only (`--`, `<=`, `n+l`, `Loewdin`, `Schroedinger`, `Lambda_phys`) against a Unicode volume. | **Closed** — normalised outside code spans (Goeppert kept: her spelling). |
| P3 | Λ_phys dependence table still summed to 22 after the merge added five parameters. | **Closed** — rows added (free parameters, exact-by-scaling), c entered under measured constants, total 27. |
| P4 | Two stale Löwdin-challenge claims (aufbau origin; channel-constants coda). | Closed in Phase 1; both prior states kept. |
| P5 | Top-level heading case mixed (two sentence-case among caps). | **Closed.** |
| P6 | "objects rest on it" counts for the five new parameters are the build's estimates. | **Closed — chat 39, with one exception named.** Rule and seeds are printed (register 1740), so the table was rerun as seeds-plus-transitive-dependents against the compendium's own graph: **26 of 27 reproduce to the unit. Subshell capacity does not — printed 66, computed 65.** Drift ruled out: BUILD-12's graph is identical (265 objects, 331 edges) and also returns 65. No seventh seed satisfies the rule. Nothing changed; held for the author's ruling. W-056. |
| P6 (closed, chat 4) | Rule stated in the volume for the five new parameters (statement names it, plus everything depending on it, in the Math Compendium): c 8 (unchanged), masses 3→**5**, E 2, L 2→**1**, G 0. The 22 older counts are not reproducible from the Math Compendium under any single rule (direct mentions: ionisation limit 6 vs printed 25; aufbau 7 vs 19) — generated elsewhere on an unprinted rule; flagged, left as stated. | **Closed**, older rule flagged. |
| P6 — all 27 (closed, chat 5) | Author ruled regenerate all: one printed rule (statement/title names the parameter; closure under dependence), seeds listed per parameter, prior counts kept. Five parameters count 0 on the rule (mass ratio, Cs defect, actinides, R_M, Hund). Top table and its lead sentence rewritten; IOI Λ_phys entry corrected (27 parameters, new top three, prior kept). Register 1740. | **Closed.** |
