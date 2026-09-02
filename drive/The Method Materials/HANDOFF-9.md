# HANDOFF-9 — B-list Batch 2: MC-07/08/09/10 CLOSED / MC-11 OPEN

## SELF-IDENTIFICATION (must agree with the files)
- **This handoff:** HANDOFF-9. Successor to HANDOFF-8 (retire it). Written at chat close, ~90% context, on a closed segment (MC-10), never mid-segment.
- **Chat:** chat 57 (Batch-2 completion pass, MC-10). Next chat is **chat 58**: MC-11, then B3.
- **Build described:** **BUILD58** = BUILD56 main (UNTOUCHED) + BUILD58 compendia (MC-10 authored into `L.voidfrac`).
  - main: 18,446 lines · 1,975,147 B · md5 **5292fce89637c6b495363f76f99a4885** (byte-identical to BUILD56/57)
  - compendia: 32,451 lines · 2,363,687 B · md5 **0832b5a9f3546b36a94e762a0467baca**
- **Register range:** subject Register 1–1786 (genesis seated). Queued for Register 1.1 numbering (append-only, Ruling 27): slips 05–12 · B1-C1/C2/C3 · B2-C1 · **B2-C2 (new this chat)**.

## §0 GATE FOR CHAT 58 (measure from the files; never from memory)
- Source of record: Drive Materials (folder 1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY) — BUILD56 main + BUILD58 compendia. Project knowledge still carried BUILD53 at chat-57 open; measure before trusting it.
- main: lines 18,446 · md5 5292fce89637c6b495363f76f99a4885. Presence (each exactly 1): `order dimension exactly **7**` · `ω(N(x)) ≤ 8, the coordinate count` · `an order of dimension seven` · genesis `### 1`. NO `2S′ ≤ v ≤ g, parity`. IoI tower cells 46,740 / 0.6592 / 127,070 / 0.6381 each = 1.
- compendia: lines 32,451 · md5 0832b5a9f3546b36a94e762a0467baca. Presence (each exactly 1): all HANDOFF-8 compendia checks (`order dimension of Λ₈ is 7` · `Dilworth partition of all 976 cells into 122 chains` · `fifteen coordinate-support patterns` · `riding monotonicity upward` · `### W-090` · `### W-091` · `### \`S.gen\`` · `### \`K.bracket\`` · `## THE PRIOR-ART CHAIN`) and the BUILD57 four (`ω(N(x)) ≤ 8, the coordinate count — proved and tight` · `five equivalent forms, all equal to ∏_i(|x_i−y_i|+1)` · `the maximum local up-degree is 7` · `μ_Λ(x,y) = μ_arith(N(x),N(y)) if and only if the interval`).
- **NEW BUILD58 discriminators (each exactly 1):** `exactly the product of the six edge lifts in tree order` · `1.0000 in every stratum for all five shared-coordinate pairs` · `` `K.decay` `K.markov` `L.voidfrac` ``. (`Chebyshev's sum inequality` = 2 by design; not a discriminator.)
- **Grade check (each exactly 1):** `L.omega` `L.occ` `L.metric` `L.mobius` **`L.voidfrac`** all PROVED.
- Λ₈ rebuild: HANDOFF-8 recipe (`lam8.py` in chat57-instruments.tar.gz); confirm |Λ₈| = 976, |Λ₉| = 1,654.

## WHAT CLOSED IN CHAT 57 (all measured)
1. **MC-10 — §10.2 constraint correlation, authored into `L.voidfrac` (COMPUTED → PROVED).** Structural theorem proved and verified on the rebuilt Λ₈: containment `hi_i ≤ φ(lo_j)` is a narrowness condition; shared-coordinate pairs are two decreasing functions of one width → positive dependence (Chebyshev); conditional independence given the shared interval exact (lift 1.0000, all strata, five pairs); non-adjacent lifts 0.9999–1.0101; factor = product of six edge lifts in tree order = 1.4081 at base cap (475,800 pairs exhaustive; individual 69.95–98.06%, product 20.13%, joint 28.35%). Cap-dependent 1.33–1.66.
   **Fallback form, deliberate:** the book's 776M-pair figures (27.7–30.1%, 30.13/20.19, 1.49) are retained as the measurement at their original population, *which the record does not name* (see OPEN). Grade PROVED is on the law; the statement says in place which numbers are measured where.
2. **Slip B2-C2** (L.voidfrac condition "at stated caps" pointed at no statement; population now stated) + **W-B2b** drafted in REGISTER-QUEUE-APPEND-batch2b.md.
3. **Request 5** issued and answered (REQUEST-5-voidfrac-caps.md; reply in chat). Reply's instrument finding confirmed from files (mathreg.json: `L.voidfrac` check=null; mathverify.py has no L.void/L.voidfrac row). Reply's "method_tower.py absent from pack A" **corrected by measurement**: present (4,575 B, 140 lines), it is the builder not the driver.

### GUARD CERTIFICATE (measured substitute; guard.py still has no bank)
diff(BUILD57.compendia, BUILD58.compendia) = exactly 5 hunks: 14835 · 14837 · 14839 · 14841 (the `L.voidfrac` block: statement, condition, grade, prior art) and 16670 (bibliography row 1996 Lauritzen gains `L.voidfrac`). Line count 32,451 → 32,451. All prior discriminators still = 1.

## CHAT 58 OPENS WITH MC-11, THEN B3
- **MC-11 — §10.4 closed-form void count + treeness ⟺ sieve-free.** Home `L.box` (compendia ~line 14523, COMPUTED, depends on `L.tree`); main §10.4 at line 2061–2076 states the factorisation and the two closed-form leaves. Owed: full tree factorisation (sum over n,ℓ,k,q,e,f of the indicator product × #{2S ≤ k} × #{g ≤ min(q,2(2f+1))}); the two leaves `#{2S} = max(0, min(hi₇,k) − lo₇ + 1)`, `#{g} = max(0, min(hi₆,q,2(2f+1)) − lo₆ + 1)`; verify against direct enumeration (book: eight random intervals — reproduce, then exhaust); and the proof that treewidth-1 is exactly the sieve-free condition (a cycle forces an inclusion–exclusion term; a tree's constraint indicators factor by the chain rule — same machinery as MC-10's lift factorisation, cite `L.tree`). Author INTO `L.box`; do not duplicate.
- Then B3..B10 in HANDOFF-6's order. MC-35 stays M-flagged (full representation). MC-52/53 RETIRED. Token resolution ([MC-NN]→citations) is LAST.

## CAUTIONS (carry HANDOFF-8's four, plus)
- **A recorded figure may have no recorded population.** Before verifying any COMPUTED object, read its condition line and check the cited section actually states the caps/sample. If it does not, say so first; do not search cap space blind.
- **Check the instrument bank before requesting.** Pack A (`method16_rp_A_instruments.tar.gz`, id 18RTwgMdnpN1hNdBDR4TgB7opb4buGedh, md5 4dee0909…) has 340 files incl. `method_tower.py`, `mathverify.py`, `mathreg.py`, `cycle*.py`. Pack B (`method16_rp_B_data.tar.gz`, id 12XrDQ3Kkj0P073tnCDzTuTZxZSuKnejN, md5 204b7dfb…) has `mathreg.json`, REGISTER data, TSVs. Both spill to `/mnt/user-data/tool_results/`; decode per the standing pattern. Pack C (figures) NOT yet searched.
- **Original-works replies are reconstructions too.** Request 5's reply was wrong about a file's location; measure before carrying a reply's claim into a handoff.

## OPEN / OUTSTANDING (named, not glossed)
- MC-11 (Batch-2 completion) — authorised set MC-07..11: **4 of 5 done, 1 open.**
- The 776M-pair cap family: unrecovered; lives in `method_tower.py`'s driver, absent from packs A and B; pack C unsearched. Reopen when found; MC-10 then gains its numeric reproduction (a second slip, not a rewrite).
- "seventeenfold" (§10.2, rewrite caption) vs "hundredfold"/"100×" (BUILD56 caption line 2054; audit table line 10253) — needs Figure 10.1's plot data; no slip yet.
- `The_Method_1_6_audits.py` line 381 requires "473,800,776" in main; not present in BUILD56 main — stale audit or missing figure, unexamined.
- guard.py still in NO bank; measured-diff substitute used and declared. Bank owed.
- Slips 05–12 · B1-C1/C2/C3 · B2-C1 · B2-C2 await Register 1.1 numbering.
- OWED-EXPANSIONS-2 rows 7/8/9/10: mark DONE. Row 11 open.
- Register 1741's ~39 production figures — Phase-4, M's ruling.

## FILES — UPLOAD / RETIRE
M UPLOADS to Drive Materials (folder 1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY):
  1. **The_Method_1_6_BUILD58_compendia_papers_audits.md** (md5 0832b5a9f3546b36a94e762a0467baca). Main unchanged — keep BUILD56 main, or re-upload renamed as BUILD58 main for a matched pair.
  2. **REGISTER-QUEUE-APPEND-batch2b.md** (slip B2-C2 + W-B2b). APPEND to OWED-REGISTER-EXPANSIONS.md after the batch2 append.
  3. **REQUEST-5-voidfrac-caps.md** (the request; keep its reply with it).
  4. **chat57-instruments.tar.gz** (lam8.py, mc10.py, mc10b.py, mc10c.py, mc10d.py, caps.py; md5 2741d9e3145ff94f8b435bda6c0c84de).
  5. **HANDOFF-9.md** (this file).
STRONGLY RECOMMENDED: replace the compendia file in project knowledge with BUILD58 and the main with BUILD56 (project knowledge still holds BUILD53).
RETIRE: HANDOFF-8.md.

## DO NOT REOPEN
MC-07/08/09 and their edits · **MC-10's form (M-ruled: close properly, fallback population)** · the dim(Λ₈)=7 finding · A-list (all) · 1D↔14D bracket verdict · genesis seating (Ruling 66) · the BUILD55 merge · everything in HANDOFF-8's DO NOT REOPEN list.

## NEXT-SESSION OPENING PROMPT (paste to start chat 58)
> Continue The Method 1.6. This is the B-list Batch-2 close-out and Batch-3 opening (successor to HANDOFF-9, chat 58). Read HANDOFF-9.md first, then from Drive Materials: OWED-EXPANSIONS-2.md, REGISTER-QUEUE-APPEND-batch2b.md, OWED-REGISTER-EXPANSIONS.md. Source of record is BUILD58 = BUILD56 main (md5 5292fce89637c6b495363f76f99a4885, unchanged) + BUILD58 compendia (md5 0832b5a9f3546b36a94e762a0467baca). Run the §0 gate in HANDOFF-9 — line counts 18,446 / 32,451, both md5s, every presence check INCLUDING the three BUILD58 discriminators and the five PROVED grade checks — before any work. Rebuild Λ₈ from lam8.py in chat57-instruments.tar.gz and confirm 976 / 1,654. Then AUTHOR MC-11: locate `L.box` and read its current state (author into it, do not duplicate); read main §10.4 so the expansion matches the sketch; computationally verify — reproduce the tree factorisation and the two closed-form leaves against direct enumeration, then prove treewidth-1 ⟺ sieve-free — BEFORE writing; write the full expansion in Mathematical Compendium house style with an honest grade line; run the measured-diff guard; present it with its slip for approval. Then open Batch 3 (B3 in HANDOFF-6's order). Zeno segmentation throughout; everything to Drive at close; handoff at 90% context or a closed segment, never mid-segment. Do not reopen anything in HANDOFF-9's DO NOT REOPEN list.
