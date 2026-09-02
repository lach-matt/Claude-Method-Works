# Owed REGISTER expansions — workshop that is subject-matter proof-of-work

Standing distinction (M, this session): some workshop cut from the reader prose is NOT mere
editorial/process residue for the working record — it is subject-matter proof-of-work on the
mathematics (how a result was reached, what was tried and withdrawn, what the correct method turned
out to be). That material is owed to the **subject-matter Register** (the canonical append-only record),
because the Register exists precisely to show thought-process and proof-of-work for the book's subject.

CRITICAL governance guard (Ruling 27 / project rules):
- The subject-matter Register holds SUBJECT MATTER only, append-only, never edited/relocated/renumbered.
- Reader-perspective audits and EDITORIAL/production findings go to WORKING-REGISTER.md, never here.
- This file tracks the FORMER: subject-matter workshop (seed derivations, method corrections that are
  themselves findings about the mathematics) owed as NEW register entries that CITE, never overwrite.
- A withdrawn result is corrected by a NEW entry citing the old, not by removing anything.
- These are DRAFTED as reader prose cuts now; the actual register entries are authored when the pass
  reaches the Register (M closes with it last). This file is the queue so nothing is lost.

Token series for reader-prose flags: [REG-NN] is NOT placed in reader prose (the reader never sees a
register self-citation — that is the whole point of the cut). Instead each cut is logged here with the
source §, the surviving reader claim it supports, and the subject-matter content owed to the Register.

## Batch from source Chapter 14 "Closure" — subject-matter workshop owed to the Register
| # | source § | reader claim it supports (kept in prose) | subject-matter proof-of-work owed to Register |
|---|---|---|---|
| R-01 | §14.5.1, §14.5.9 | Λ is the closure of seven cells (exact) | The route from greedy upper bounds (12/11/12) to the exact minimum: seed as MINIMUM SET COVER (elements = envelope steps, sets = cells); why prune-greedy overcounts (fits its own failures); branch-and-bound gives 7; the spread across heuristics (prune 12, cover 7, reverse-delete 40, LB 5, exact 7 → spread 33) as the quantity that reports algorithm quality. Cites the superseded greedy figures rather than deleting them. |
| R-02 | §14.5.8, §14.5.9 | a counting axis costs the seed about one cell; a coupling axis costs more (the seed reads the dichotomy) | The full withdrawn-and-corrected chain: the prune-greedy per-axis numbers (+1 counting / +10 coupling / cost=a+κ / κ=S/4−1 at r=0.980) WERE the heuristic's difficulty, not the index's cost; under set cover a two-parent axis costs ~1–2, same as one-parent; refit gives coefficient −0.079 at rms 0.999. The parent-count-drives-cost reading is withdrawn; what SURVIVES is the counting/coupling asymmetry read through the seed. This is the untangling (see reader §14.5.8 treatment). |
| R-03 | §14.5.8 | seed = Carathéodory number + alphabet cost; linear in dimension | The Carathéodory identification: breadth of a product of d chains is d; a generating set must reach the breadth; the coefficient "was in the bibliography, glossed and left"; the two bibliography gaps step 2 of the cycle found (Carathéodory never cited though Helly was). Prior-art provenance as proof-of-work. |
| R-04 | §14.1 | Theorem 14.1: X closed iff X = ℛ(X), with prior owners | The mis-citation correction: Freuder 1982 (backtrack-free search, width w, strong (w+1)-consistency) is a DIFFERENT theorem than Dechter 1992 (local→global at strong (w*+1)-consistency); the book had been citing Freuder for Dechter's result. Correction is itself a subject-matter finding about provenance. |
| R-05 | §14.5.10, §14.5.11 | four corner cells appear in every sampled seed but NONE is forced; the constraint is on the channel | The erasure-code false start ("unreconstructible core") withdrawn; nothing is forced (0 uniquely-covered envelope elements at every cap and at Λ₉); 519 completions from 66 cells, heavy-tailed (min3/med12/max157); the conditional-misread-as-necessity correction. |
| R-06 | §14.6.3 | (not carried to reader — pure register content) | The mathematics register's own state: object counts across builds, the five-component graph (main 162, modular chain 9, two fragments, B.nuV isolated), what is unfinished and why (six modular objects await two unread sources). This is register-about-register; author as the register's self-description where appropriate, NOT reader prose. |

## OPEN FINDING (not a cut — an epistemic-status flag for later passes)
- §14.5.14 complementary-pairing / "every letter spoken both ways": VERIFIED against the record to be
  genuinely OPEN. The subject Register entry (canonical) states it as measured at one cap setting,
  cap-independence UNTESTED, "describes Λ₈ and is not yet a law." The compendia bundle restates the
  finding WITHOUT any cross-cap law. No downstream section raises it to a structural law.
  → Reader prose keeps the honest status: a described property of Λ₈, not a law. Do NOT overstate.
  → WATCH (like the 14D/void precedents): if a later chapter or a cap-variation run ever closes it,
    flag to M and raise the prose to a law then. Until then it stays a described property.
  → This is a candidate for the reader-audit pass to re-check against any cap-variation evidence.

## =====================================================================
## CORRECTION RETURNED FROM ORIGINAL-WORKS (2026-08-28) — supersedes the open-finding flag above
## =====================================================================
## Source files (Drive, restore-packs folder 1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY):
##   SEED-CAP-FINDING.md (1dS26wtgi6m7Bn1ee9bZQoZNqxqzXaUMa) — the finding, cap sweep, register consequences
##   EXPANSION-MC54.md   (1cRxi76vCe9J_eeF2e6_dmdOU3UZ2AWLn) — full proofs T1/T2/T3, P4, attributions
##   covers8.json        (1sqMDyhkQZykKsr7pHUgcwd9IbhcnfO_0, 4.5MB) — the 24,585-cover enumeration evidence
##   ALSO recovered: archive/transitions/Transitions.md in method16_rp_A_instruments.tar.gz
##                   (18RTwgMdnpN1hNdBDR4TgB7opb4buGedh, 1,005,510 bytes byte-verified) — closes Transitions.md location
##
## THE ANSWER (not the one anticipated): §14.5.14 properties 1–3 are REFUTED at Λ₈ (not untested);
##   property 4 is a LAW with proof; the channel conditions generalize to an envelope-step law.
##
## Register consequences — slip-ready for Register 1.1 (R-numbers theirs to assign):
## - R 602 CORRECTED: "219 covers" was a biased randomized sample; exact count = 24,585 minimum covers;
##     four-corner universality REFUTED; only corner 3 (2,1,3,3,2,1,3,0) common to all, and cap-specific.
## - R 603 CORRECTED: five of six channel conditions exact at Λ₈ (s→s fails, 71%); generalized to the
##     envelope-step law (T3); s→d/d→s element-forced at d-shell cap.
## - R 604 CORRECTED: the unit template is not forced (10% of exact covers).
## - R 605 SUPERSEDED: premise (five universal cells) fails; P4 raised to LAW; P1–P3 refuted; corner 3
##     universal at ℓ≤1 caps only. (New entry cites 602–605; append-only, per Ruling 27.)
## - Compendium objects S.bits, S.channel, S.unit REOPEN; [MC-54] gains the proofs (T1/T2/T3/P4)
##     instead of the described pairing.
##
## PRIOR-ART for [MC-54] (from EXPANSION-MC54.md): NEW load-bearing citation = Edelman (1980) +
##   Edelman–Jamison (1985) — convex geometries / anti-exchange / combinatorial Krein–Milman; Λ₈ has
##   EMPTY extreme-point set (ℛ(Λ∖{x})=Λ for all 976) yet seed 7 = maximal Krein–Milman failure = why
##   24,585 covers coexist. Corner-3 forcedness = Chvátal forced-set (already cited). Dilworth 1940 =
##   uniqueness-under-conditions precursor. Krein–Milman 1940 = classical antecedent. Rest retained in place.
##
## BOUNDS of the run (P8): caps (4,4,2,6,2) and (5,5,3,8,3) NOT run; d-shell "pp tight-universality"
##   recorded unexplained; E computed at 976-cap only. These are named limits, not glossed.

## =====================================================================
## RESPONSE TO REQUEST 2 (seed laws vs 14D) — returned 2026-08-28
## Source: 01-seed-laws-14D-confirmation.md (Drive 1IZ6Pva2OCSm5iZRWfU_Yv42phErAdl0Q); artefact verify2.py
## =====================================================================
## VERDICT: NO load-bearing link between seed laws (T1/T2/T3/P4) and 14D §12.11.0.11.
## Two of four refusals are themselves results (Q2, Q3). 14D prose UNCHANGED. Seed laws stay in Ch14.
##
## Q1 (collapse biconditional): SPLIT. Biconditional derivable from T2 for a rung-1 axis INSIDE a built
##   index (register 547 / A.define). But applying it to 14D is a TYPE ERROR — 14D is absent, not a
##   collapsed column; ℛ cannot name a coordinate (§32.1.4). CRITICAL: the premise "14D always collapses
##   to 1D" is NOT on the record — §12.11.0.11 + register 333 make a FILL claim (bracket [0,0.42%]), not a
##   collapse claim. Only a CONDITIONAL survives to prose: were a 14th coordinate adjoined at rung 1, the
##   seed would not move. → DO NOT write "14D collapses to 1D" as recorded fact anywhere in prose.
##
## Q2 (empty-index E=0 vs P4): PARALLEL ONLY, distinction PROVED. Not one theorem:
##   - register 333 underdetermines WHICH closed object (generic Moore-family fact; measure |J(Λ)|=17, join-generation)
##   - P4 underdetermines WHICH generator of ONE object (property of the pair (ℛ,Λ); measure seed=7, ℛ-generation)
##   Proof: a 5-point interval-hull convex geometry has UNIQUE minimal seed (Krein–Milman holds, P4 fails)
##   yet conv(∅)=∅ still closed with zero content. The two come apart in one operator. PROSE MUST NOT SWAP THEM.
##
## Q3 (does seed decide the [0,0.42%] limit?): PARALLEL ONLY, refusal is a theorem. Seed is O(d+c);
##   at c=2 full box (fill 1.0) seeds at d, maximal chain (fill→0) seeds at d+1 (d=3,4). Fill varies over
##   (0,1] at fixed seed budget → NO function of the seed sequence (incl. recorded 7→10) decides null-vs-positive.
##   Generation view leaves open EXACTLY what the fill view leaves open. Stated result.
##
## Q4 (origin=horizon as seed↔14D?): PARALLEL ONLY, metaphor NOT licensed. No theorem pairs minimum seed
##   with 14D. Licensed: ℛ total over cells (7→976), null over coordinates (never regenerates a coordinate;
##   §32.1.4, Thm 11.1, Thm 10.1). origin=horizon connects ∅ TO THE HORIZON (∅ = unique index that is its
##   own seed, zero bits, closed+complete) — NOT the seed of Λ to the horizon. The seductive bridge is the false one.
##
## GUARDS AVAILABLE TO PROSE (Q2, Q3 distinctions): when 14D or the seed is discussed later, these two
##   distinctions may be stated AS RESULTS to prevent the false bridge. Not required, but available.
##
## REVISIT FLAG (M): question narrowed, not settled — revisit as the prose pass reaches later chapters that
##   touch 14D (§12.11.0.11 is in the TIME chapter, already drafted split C) and §32.1.4 / Thm 10.1 / 11.1.
##   When those are revised, apply the Q1 conditional and the Q2/Q3/Q4 guards.
##
## COUNT-FLAG raised back to us (their Q-flag): §14.5.9-era record = 219 minimum covers; P4 = 24,585.
##   RECONCILIATION (ours to state, one line): the 219 was a biased RANDOMIZED SAMPLE; 24,585 is EXACT
##   enumeration at the Λ₈ cap (SEED-CAP-FINDING.md, R 602 corrected). Same object, superseding recomputation.
##   → This one line goes into the R-602 correction slip so both projects' records agree.

## TIME-CHAPTER CHECK (done now, against the Request-2 response)
- REWRITE-chapter12C-time.md (approved, Drive 1cS7VAKQTIMzRP2ijrtebxPU-sEJwvyE3) was checked for the
  "14D collapses to 1D" error the response warns against. RESULT: no error. The chapter states the
  FILL/BRACKET claim exactly as §12.11.0.11 / register 333 ("bounded without being built," limit in
  [0,0.42%], value does not follow, E=0 necessary-not-sufficient). It carries origin=horizon in the
  LICENSED form ("met here from the inside... exactly as it was met at the beginning as the seed" —
  connecting the seed/∅ to the boundary, not pairing minimum-seed-of-Λ with 14D). §12.11.0.11 → MC-33.
- CONCLUSION: no correction to the time chapter. The "collapses to 1D" phrasing exists only in the
  memory bank, not in any draft. Do not introduce it.
- REMAINING REVISIT (narrowed, not closed): when the prose pass reaches §32.1.4 / Thm 10.1 / Thm 11.1
  (ℛ never produces a coordinate — the type-error basis of Q1) and any later 14D-adjacent section, apply
  the Q1 conditional ("were a 14th coordinate adjoined at rung 1, the seed would not move") and keep the
  Q2/Q3/Q4 distinctions available as guards. The seed↔14D question is settled as PARALLEL-ONLY; what
  remains is only to state the guards if/where a later chapter risks the false bridge.

## =====================================================================
## STANDING OPEN THESIS (M, 2026-08-28) — carry through the ENTIRE remaining prose pass
## =====================================================================
## DISTINCT from the settled seed↔14D question. The seed-laws↔14D link is closed (parallel-only).
## THIS is a different and OPEN claim, which M maintains:
##
##   THESIS: the transitional connection between 1D and 14D is PROVABLE from the books —
##           the two ends of the axis structure (origin axis ↔ horizon axis), not the seed's
##           relation to either. M's expectation: the proof may be expressible ONLY in BINARY.
##
## Why binary is a principled expectation, not a hunch (record support to build on):
##   - the seed work already resolves to bit-words: each coordinate read as at-extreme (1) / not (0).
##   - 14D "lands on" 1D on collapse; 1D is the collapse target. A binary reading keeps ONLY the
##     extreme structure — exactly what would survive a collapse — so binary may be the boundary's
##     native language rather than a limitation.
##   - origin=horizon (licensed form): ∅ is its own seed at ZERO bits; the whole construction seeds
##     from "null is definable." A 1D↔14D proof in bits would sit naturally against that zero-bit origin.
##
## HOW TO CARRY IT (every remaining chapter, not just §32.1.4):
##   - At any section touching 1D, 14D, the collapse, binary/bit encodings, join-irreducibles, or the
##     origin=horizon frame: check whether the material supplies a piece of the 1D↔14D bridge, and
##     whether that piece is naturally binary. Log candidate pieces here as found.
##   - Do NOT assert the connection in prose until it is proved (confirmation discipline). Collect the
##     pieces; when enough accumulate, put a focused request to the original-works project to attempt
##     the proof (likely binary-form), the way the seed-cap and seed↔14D requests were run.
##   - Keep DISTINCT from the parallel-only seed↔14D verdict — do not let that verdict be cited as
##     closing THIS question. They are different claims.
##
## STATUS: open, live for the whole pass. Candidate pieces: (none logged yet — begin at Ch14B onward).

## REQUEST 3 ISSUED (against the standing thesis) — 1D↔14D connection, binary-form expected
- File: REQUEST-3-to-original-works-1D-14D-connection.md (in outputs, for delivery to the original-works project).
- Asks: is 1D↔14D provable from the books (distinct from the settled seed↔14D parallel-only verdict), and is it binary-only?
- Anchors used: 14D = §12.11.0.11/register 333 (fill bracket [0,0.42%]); 1D = §26.2 rank(log q)=1 ("every Rydberg
  property is ν to a power, the exponent the whole of its identity") + the zero-bit thread (∅ its own seed, zero J).
- Four questions: Q1 bracket→scalar collapse map (is 1D the collapse fixed point, 14D its limit?); Q2 binary-only
  expressibility (theorem in bits, type-error at full resolution?); Q3 does origin=horizon become a TWO-ENDED
  theorem with 1D (not the seed) at the origin?; Q4 if not provable, name the missing lemma.
- STATUS: awaiting response. When it returns, land per the file's rules; update the standing thesis with the verdict.

## =====================================================================
## RESPONSE TO REQUEST 3 (1D↔14D) — RESOLVED. Standing thesis CLOSED. 2026-08-28
## Source files (Drive, restore-packs folder 1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY):
##   02-1D-14D-transitional-connection.md (116ifdY-UPghTuHTcVpqBis6Ww5uZ8zt2) — first pass: two ends of the fill law, lemma named
##   03-1D-lands-inside-14D.md          (1RTAAUwoiJRoVlK9WUiDqg7MkSseVmvZ7) — CLOSING: lemma tested on real tower, connection proved
##   Scripts banked: tower.py, tower2.py, tower3.py, factor.py (travel with the slip per R 1712/R 1726)
## =====================================================================
## VERDICT: M's thesis is RIGHT about the connection, WRONG about its vehicle. Both halves now MEASURED.
##   The 1D↔14D transitional connection is PROVED — but the join is a BRACKET, not a map, and needs NO binary.
##
## PROVED (03, exhaustive on the rebuilt tower Λ₈–Λ₁₃, fingerprint-verified as the book's object):
##   1. STRICT MAP REFUTED: rank-below is not a function of rank-above; branching grows 4,4,6,8,9 with height.
##      "One transition as a map" does not exist — measured, not suspected (factor.py).
##   2. BRACKET PROVED at every stage: r ↦ {ranks below} is a GAP-FREE INTERVAL with BOTH endpoints MONOTONE,
##      no exception across all 199,130 cells. The tower's chains form ONE directed system of monotone brackets
##      χ(Λ₁₃)→…→χ(Λ₈). Composition slack ≤ 2 rank units — §22's outward rule appearing INSIDE the tower.
##   3. 1D LANDS INSIDE 14D: projection from Λ₁₃ covers ALL of χ(Λ₈), ranks 3..20 no gap, two routes agree.
##      The 1D chain is the TERMINAL OBJECT of the bracket system, entirely in the image from the top;
##      14D is the same system's LIMIT. R 334's sentence ("bracket not map") proved stage-by-stage down the tower.
##
## BINARY (M's expectation — answered and CORRECTED):
##   - The proof carries at FULL RESOLUTION; no bit-encoding required. Binary-ONLY refused categorically
##     (any bit-reading is a function of the object → statement about bits IS a statement about the object by
##     pullback; "well-formed only in binary" is impossible as a category — the most available is natural-in-binary).
##   - M's SINGLE at-either-extreme bit is NOT closure-lawful: non-monotone (min→1, mid→0, max→1), image E=1 —
##     it breaks the property the proof lives in. The LAWFUL form is TWO bits (at-top, at-bottom), each a
##     homomorphism (both E=0); M's single bit is their pointwise OR, and the OR is where the law breaks.
##   - The connection's native language is THE BRACKET (the book's house currency), not the bit.
##
## ORIGIN=HORIZON: refused as identity, PROVED as ANTIPODES. Fill = 1 at origin, ≤ 0.0042 at horizon — opposite
##   extremes of ONE law (the fill), not one point. Identity form stays licensed for ∅ alone (Request 2 stands).
##
## LANGUAGE-BOUNDARY GUARD (must not reach prose as a conflation):
##   §26.2's rank(log q)=1 is in the VALUE language (Rydberg quantities along ν); D=1 is in the INDEX language
##   (one coordinate, a chain). They are NOT the same 1D. The proved 1D end is the INDEX-language chain (the
##   bracket system's terminal object), NOT §26.2. Do not fit them together — no bridge on record. §26.2 stays put.
##
## WHERE IT LANDS IN PROSE (new result, carriable once M approves the framing):
##   - §12.11.0.11 (14D, in the approved TIME chapter): gains the two-ended statement — the tower's two ends are
##     joined by a bracket; every rank of the 1D chain reached from Λ₁₃ through monotone gap-free intervals;
##     the map the eye wants does not exist (branching 4→9). This is a NEW claim about the whole axis structure.
##   - Owed reader one-liner (from 03): "The tower's two ends are joined, and joined the only way this book joins
##     anything seen from above — by a bracket: every rank of the first axis is reached from the thirteenth
##     through intervals that never cross, and the map the eye wants does not exist, by a branching of four to nine."
##   - New Math Compendium expansion owed: the bracket-system theorem (directed system of monotone gap-free
##     interval maps down the tower; composition slack ≤ 2; terminal object = 1D chain; limit = 14D). → MC-55.
##   - The TIME chapter is APPROVED and already drafted; adding this is a Rule-6 inclusion (like the tower EM
##     section) — needs M's ruling on placement before editing an approved chapter. FLAG, do not edit silently.
##
## STANDING THESIS (1D↔14D): CLOSED. Resolved to PROVED-as-bracket / NOT-binary-only. Remove from "live open"
##   watch; it is now a delivered result awaiting only prose placement in the time chapter.
##
## TWO DISCREPANCY FLAGS raised by the return (owed to Register 1.1, one line each — NOT repaired by original-works):
##   A. Index of Indices tower table prints Λ₁₂=22,275 / Λ₁₃=64,290 — matches NEITHER the f_max build
##      (70,905/199,130, the §12.11.0.10 figures, reproduced) NOR the cell's-f variant (55,755). Stale table or
##      different capping. One line owed. → affects the Index of Indices volume; check in cross-volume audit.
##   B. §12.11.3.1's "parity" annotation on axis 10 belongs to the EXACT physical set, not the admissible bound:
##      parity builds give 1,841 vs printed 2,535; the bare interval gives 2,535 exactly. The annotation misreads
##      the bound. One line owed. → affects the tower material; flag for the tower chapter / compendium.

## =====================================================================
## SEQUENCE RULING (M, 2026-08-28) — PAUSE PROSE FOR VOLUME REPAIR
## =====================================================================
## Order set by M:
##   1. DONE: MC-55 bracket result folded into approved time chapter (REWRITE-chapter12C-time.md).
##   2. Request 4 issued to original-works: the two discrepancies (Index of Indices tower table 22,275/64,290;
##      §12.11.3.1 axis-10 "parity" annotation). File: REQUEST-4-to-original-works-two-discrepancies.md.
##   3. AWAIT Request-4 answer. THEN pause the prose pass.
##   4. REPAIR the affected volumes to canonical values (Index of Indices; tower material / compendia),
##      under NO-SILENT-CHANGE: each change recorded by a Register entry in the same build; guard.py before
##      any bundle is declared current; append-only Register.
##   5. RESUME prose pass after repair.
## Rationale (M): the prose work relies on the compendia being correct; repair must precede further prose.
##
## PREFACE-REVISION FLAG (M): the preface may need another revision when the prose pass cycles back around.
##   Reason: the preface's "how far the method reaches" claims may reference tower figures (e.g. the 14D
##   bracket, the tower counts) that this session's work has now sharpened (MC-55 result) and that Request 4
##   may correct (70,905/199,130/2,535). When the pass returns to the preface, re-check every figure and
##   reach-claim against the post-repair canonical values and against the MC-55 two-ended-bracket result.
##   → Logged so it is not lost across the pause and the handoff.
##
## OPEN REQUESTS OUTSTANDING: Request 4 (two discrepancies) — awaiting answer before repair begins.

## =====================================================================
## RESPONSE TO REQUEST 4 (two discrepancies) — RESOLVED. Repair scope MINIMAL. 2026-08-28
## Source: 04-two-discrepancies-resolved.md (Drive 1tEMzm64kZM2iInSPwB6uYU0XJlrm33iY); artefact req4.py + tower.py/tower3.py
## HEADLINE: neither discrepancy touches a load-bearing figure. Both are "correct different object, name shared."
##   Every load-bearing figure held: 2,535, 13,585, 70,905, 199,130. Nothing was miscomputed.
## =====================================================================
##
## DISCREPANCY A — RESOLVED. The Index of Indices printed the EXACT-TRIANGLE object in the tower rows.
##   - Triangle build (2K by 2 through |2J_c−2f|≤2K≤2J_c+2f, cell's own f, then |2J−2K|≤1) reproduces
##     22,275 and 64,290 to the cell (req4.py); identity #{2K=0}=2,535=|Λ₁₀| gives 64,290 = 3·22,275 − 2,535.
##   - This object DOES NOT CLOSE: E = 35,570. The Mathematical Compendium ALREADY names+prices it at
##     LINE 1515 ("the tree or the tightness: imposing the exact triangle at axis 12 gives 22,275 cells and
##     E = 35,570"). The Index of Indices printed a non-closing object in a table whose stages are all E=0.
##   - CANONICAL: 70,905 / 199,130 (envelope, 2K ≤ 2J_c + 2f_max), confirmed SIX ways (§12.11.0.10/R315;
##     §12.11.1 densities/R434; §12.11.3.1's "39,375 below cap" reproduced exactly; R334 44-rank chain;
##     R249 E=0 at Λ₁₃; Request-3 five exact counts). By the dichotomy the triangle cannot be a stage.
##   - REPAIR (Index of Indices ONLY):
##       * row Λ₁₂ → | Λ₁₂ | 70,905 | 12 | — | — | 2K ≤ 2J_c + 2f_max |
##       * row Λ₁₃ → | Λ₁₃ | 199,130 | 13 | — | — | |2J − 2K| ≤ 1 |
##       * prose line 321: "runs to 64,290 cells at Λ₁₃" → "...199,130..."
##       * composable counts/fractions in those rows (14,242 / 0.6394, 39,772 / 0.6186) were computed on the
##         TRIANGLE object → OWED RECOMPUTATION on the canonical build during repair (not supplied by orig-works).
##     MC line 1515 is correct as written and is the reconciling entry — do NOT touch it.
##
## DISCREPANCY B — RESOLVED. Label fault only, one-word repair.
##   - 2,535 CANONICAL (bare interval 2S′ ≤ v ≤ g; chains into 13,585→70,905→199,130). Parity build = 1,841,
##     appears in NO printed tower. Load-bearing figures untouched.
##   - Parity is real physics, already housed in the EXACT SET (§12.11.1: terms(f^v) − terms(f^(v−2)) = the
##     step-2 seniority ladder; axis-9 exact set is the same ladder edge-on). Lives in the density numerator
##     (44.7%), never the admissible bound (consonant with §12.11.2 excluding congruences from admissible bounds).
##   - REPAIR (MAIN VOLUME, one annotation): §12.11.3.1 row 10 — strike ", parity" from the bound column,
##     leaving "2S′ ≤ v ≤ g". Optional provenance cell: "seniority, Racah 1943 — parity lives in the exact set,
##     §12.11.1." MC-22/23 carry the count WITHOUT the annotation → no compendium repair.
##
## NAMED-NOT-VERIFIED (carry as open): MC 1515's E = 35,570 for the triangle object was NOT recomputed this
##   session (5.3M-cell box census). The identification rests on two exact counts + the compendium's own naming.
##   → owed: recompute E=35,570 census on the triangle object during repair, OR accept MC 1515 as the standing record.
##
## REPAIR PASS SPEC (when M starts it, per the sequence ruling):
##   1. Index of Indices: 2 table rows + 1 prose line (A3) + recompute 2 composable columns on canonical Λ₁₂/Λ₁₃.
##   2. Main volume §12.11.3.1: strike ", parity" (B3).
##   Both under NO-SILENT-CHANGE: each recorded by a Register entry in the same build; guard.py before bundle current.
##   Slips 01–04 ready for Register 1.1; tower scripts (tower.py, tower3.py, factor.py, req4.py, verify2.py, verify3.py)
##   should reach a bank, not die with the container. tower.json regenerable from banked scripts (seconds, fingerprints incl).
##
## PREFACE FLAG UPDATE: the preface reach-claims are SAFE on figures — canonical tower counts held. The preface
##   revision when the pass cycles back is now only about incorporating the MC-55 two-ended-bracket result if desired,
##   NOT about corrected figures (none of the load-bearing ones moved).
