# DRAFT for M's review — Q5 pass 6: `OWED-REGISTER-EXPANSIONS.md`. Part A — the six R-rows resolve to seated entries and nothing is owed; Part B — registers 603, 604 and 605 corrected from the seed-cap finding as 1833–1835, every figure re-derived. RULED AND SEATED (W-233).

**M's rulings (4 September 2026): 1 — yes; 2 — yes; 3 — correction if it is just a correction, withdrawal if it is
withdrawing a previous statement; 4 — seat it.** Part A recorded in W-233 with no entry seated. Seated as 1833 and 1834
(corrections) and 1835 (a withdrawal), with `r3-q6-measure.py`, its golden and `covers8.json` (BUILD110 main, BUILD226
compendia). The seated text differs from the draft below by the changes six independent auditors found before seating
(recorded in W-233): the step definition includes the alphabet-minimum steps; the full transfer follows from q's maximum
with q ≤ k, not from q's alphabet alone; the compendium object is cited by its printed title, *The seed's forced set,
corrected*; the 219 of 219 is a biased randomised sample (the return's word); *s→p and p→s fall* reads *are no longer
element-forced*; 1835's headline names properties 1–3 and corner 3's *type*; T2's proviso is *at least two values*; ℓ
for the coordinate; each closing pointer carries every register its body names; Chvátal's forced set is the return's
term; §14.5.14's closing sentence is named superseded. Part A's corrections: the lower bound 5 is also in the
Mathematical Compendium's prior-art note; R-01 adds 467; R-02's *asymmetry survives* clause is stated by no entry after
504 (496 states it on prune-greedy's figures) — a lead for the prose pass; §14.1's correction is at main L3701–L3705; the
absence of citations to 603–605 was measured by a pointer sweep of the Register, not by `register_cites.py`. The draft
below is kept as reviewed.

---

Source: `OWED-REGISTER-EXPANSIONS.md` (mirror, 27,931 B; the prose-pass chat of 2026-08-28, source Chapter 14 → reader
14A), its "Register consequences" block returned from the original-works project (`SEED-CAP-FINDING.md`, 4,714 B, and
`EXPANSION-MC54.md`, 7,919 B, both in the mirror), and the evidence file `covers8.json` (mirror, 4,523,682 B, md5
5bb92ebb6cd122115b8b3a96372868e9). Register 602's correction is already seated (1820, chat 152); 603–605 are not, and no
entry cites them (measured by `register_cites.py`'s sweep at BUILD109).

## A. R-01 … R-06 — measured against the Register: every row is already seated, entry by entry

The document says of its six rows that "the actual register entries are authored when the pass reaches the Register".
Read against the seated Register, each row's proof-of-work is an entry cluster written in the cycles the source chapter
itself cites (§14.5.8 *Registers 493–494*, §14.5.9 *Registers 503–506*, §14.5.11 *Registers 596–601*, §14.6.3
*Register 519*), carrying the row's own figures:

| row | owed content, per the document | seated entries | the row's figures, found in the entries |
|---|---|---|---|
| R-01 | greedy bounds → exact minimum; the seed as MINIMUM SET COVER; prune-greedy overcounts; branch-and-bound gives 7; spread 33 | 503, 505, 506, 511, 551 | 505: seed(Λ₈) = 7 exactly by branch and bound, 976 from seven, 139 to 1, d + c − 1 and d + c − 2 exact; 506: five heuristics 12, 7, 7, 7, 40, *a spread of thirty-three around an exact seven*, 7 × 5 on the regular down-set; 511: 7, 9, 9 against 11, 12, 13; 503: one heuristic for twelve cycles; 551: NP-hard, arXiv:2211.08524. **Not in any entry:** the lower bound 5 — it is in §14.5.9's table and in the restore pack's `mathadd.py` (S.lam) only. |
| R-02 | the withdrawn-and-corrected κ chain: +1 counting / +10 coupling, cost = a + κ, κ = S/4 − 1 at +0.980; refit −0.079 at rms 0.999; the parent-count reading withdrawn; the counting/coupling asymmetry survives | 497, 498, 499, 500, 501, 502; 504 | 497: +1, +2, +2 against +10, +11; 498: a + 4 at p = 2; 499: a + κ(base); 500: κ = 0.2506·S − 0.765 at +0.980; 502: (S, c); 504: *one or two cells, the same as a one-parent axis*, −0.079 at rms 0.999, 497–500 and 502 withdrawn, 501's tight pairs = 2S surviving. |
| R-03 | Carathéodory = breadth; a generating set must reach the breadth; the coefficient in the bibliography, glossed; the two bibliography gaps step 2 found | 468, 493, 494, 495 | 468: the second bibliography gap by step 2 in two runs, Helly cited and Carathéodory not; 494: the breadth of a product of d chains is d, seed = Carathéodory number + alphabet cost; 495: exact on the audit index at seven, within one on three reconstructions; 493: (c−1)·d and d + (c−1), superseded by 511. |
| R-04 | Freuder 1982 ≠ Dechter 1992; the book cited Freuder for Dechter's theorem | 400 | 400: backtrack-free search at strong (w+1)-consistency on width w is Freuder's; the global form is Dechter 1992; *corrected at §14.1* — which §14.1 prints (main L3701–L3703). |
| R-05 | the erasure-code false start withdrawn; nothing forced (0 uniquely covered envelope elements at every cap and at Λ₉); 519 completions from 66 cells, min 3 / med 12 / max 157; a conditional misread as necessity | 596, 597, 598, 600 | 596: zero at every setting from 216 cells to 1,636 and zero at Λ₉, *CONDITIONAL … not necessity*, withdrawn; 597: 87 of 102, 519 triples over 66 cells, 3 to 157, *the core is not unreconstructible*; 600: T1 / T3 / T5, min 3 median 12 max 157; 598: the grounding check at 100 % disclosed. |
| R-06 | the mathematics register's own state: the five-component graph (main 162, modular chain 9, two fragments, B.nuV isolated); what is unfinished and why | 519, 527 | 519: 176 objects, 154 settled, 22 unfinished, 12 % open; five components — 162, nine, two fragments among the bracket's roots, B.nuV isolated; 527: seventeen, 9 % open, eight modular objects on two unread sources. (§14.6.3 prints *six modular objects await two unread sources* against 527's eight — the chapter's own class, not this pass's.) |

**So nothing is owed for R-01 … R-06 and no entry is drafted.** The rows were written against the reader draft, where
the workshop had been cut, and the Register was not consulted; the cut was from the reader prose, never from the record.
Proposed disposition: this table to the Working Register (W-233); DEF-153R's row PO-0087 (κ = S/4 at +0.980, registers
500 and 502) is closed by register 504 — seated long before the retraction audit — and the audit row mislocated its
correction to an owed draft; DEF-153R's row PO-0190 (register 314) points at this document, which does not contain the
string *314* (measured: 0 hits) — the row stays a lead. Both go to DEF-153R's successor note.

## B. Registers 603, 604 and 605 — corrected from the seed-cap finding, as 1833–1835. Every figure re-derived first

**The instrument, written and run before drafting:** `r3-q6-measure.py` (standard library, seated with the pass if
approved; golden banked by running, ~3 min). It follows chat 65's `seedcensus.py`, `seedenum3.py` (numpy) and
`coverscheck.py` definition by definition — the envelope-step census as the law prints it, the duplicate-free branch and
bound over the least-carried uncovered element with the top-r gain bound, the checks on `covers8.json` — with Λ₈ from the
seated `tower-2.py` and witness sets as bit-masks where chat 65 used a numpy matrix. Measured: 25 alphabet slots + 77
envelope steps = 102 elements, no element with a unique carrier (the least-carried has four); **no 6-cover** (45,807
nodes); **24,585 seven-cell covers** (2,821,732 nodes, 70 s), **equal set for set to `covers8.json`** (md5 5bb92ebb…
asserted against `drive/MANIFEST.tsv`; its 24,585 listed covers all of size 7, all in Λ₈, each covering the 102 with no
redundant cell); **corner 3 (2,1,3,3,2,1,3,0) in every cover and the only cell that is**; corner 1 in 58.9 %, corner 2 in
27.8 %, corner 4 (11001100) in 13.7 %; the unit template (3,0,1,1,\*,0,1,1) in 10.0 % — with e = 3 in 1,478 covers, e = 1
in 684 and **e = 2 in 290**, the middle value 604 excluded; the six channel conditions **70.8 / 100 / 100 / 100 / 100 /
100 %**, the five at 100 % each element-forced and s→s forced by nothing; the four core cells' completions **519 triples
over 66 cells, none in all, min 3 / median 12 / max 157**; the cap sweep — (2,2,1,3,1) 328 cells, (3,3,1,3,1) 976,
(4,4,1,3,1) 1,968, **seed 7 at each decided exactly** (no 6-cover, a 7-cover exhibited), s→p, p→s, p→p, q = 0, q = k
and corner 3's type element-forced at all three and s→s at none; (3,3,2,6,2) **7,605 cells**, where s→p, p→s and
corner 3's type are no longer forced and **s→d, d→s, q = 0, q = k are**, a greedy cover of 10 cells exhibited so the
seed is ≤ 10. **Not re-derived here, named:** the seed at the d-shell cap is exactly 10 (no 9-cover) only in
SEED-CAP-FINDING's own run — branch and bound over 7,605 cells does not finish in the instrument's budget; p→p's
"forced at exact minimum only" there likewise. Corner 3's *type* is defined for the sweep as l, k, q, f, g at their
maxima with q = k and 2S at its minimum, n and e free — the finding's "corner-3-type", which it did not define.

**Three entries, one per corrected register, each citing the entry it corrects and 1820; kinds: correction.** (605's
kind could be *a withdrawal* — its premise fails — rather than *a correction*; drafted as a correction, M's call.)

### 1833

**REGISTER 603'S SIX CHANNEL CONDITIONS ARE FIVE OVER THE EXACT COVERS, AND THE FIVE ARE THE ℓ ≤ 1 FACE OF AN ENVELOPE-STEP LAW.** *Register 603 states that every minimum seed of Λ₈ contains an s→s, an s→p, a p→s and a p→p transition, a null transition with q = 0 and a full transfer with q = k, in all 219 covers of the sample register 602 recorded; §14.5.12 prints the six at 100%. Measured over the 24,585 minimum covers enumerated exactly (register 1820): s→p, p→s, p→p, q = 0 and q = k hold in every cover, and each is element-forced — some element of the 102 the seed must witness is carried only by cells of that type, so no cover exists without it; s→s holds in 70.8% and is forced by nothing, having never been a step. The five are instances of the envelope-step law (the original-works return of 2026-08-28, theorem T3): a generating set must contain, for each step of the envelope — the least value t of a coordinate j at which φ̂ᵢⱼ(t) = max{cᵢ : cⱼ ≤ t} rises — a cell with cⱼ ≤ t carrying cᵢ = φ̂ᵢⱼ(t), and covering every step with every alphabet value suffices; the alphabet half (theorem T2, register 1835) forces the null and the full transition from q's alphabet alone. At the caps (2,2,1,3,1), (3,3,1,3,1) and (4,4,1,3,1) — 328, 976 and 1,968 cells, seed 7 at each by branch and bound — the same five are element-forced and s→s is not; at the d-shell cap (3,3,2,6,2), 7,605 cells, s→p and p→s fall and s→d and d→s are element-forced beside q = 0 and q = k, as the law reads at ℓ ≤ 2. The moral of 603 — the constraint is on the channel, not on the cell — survives corrected: five of six at ℓ ≤ 1, and the six generalise to the steps. Returned by the original-works project (SEED-CAP-FINDING.md, EXPANSION-MC54.md); seated under RUL-153 Q5. Re-derived at this build by r3-q6-measure.py, seated with this entry with its golden — a standard-library instrument of R3's following chat 65's seedcensus.py, seedenum3.py and coverscheck.py definition by definition, that enumeration needing numpy (M's ruling, passes 4 and 5): the census of 25 alphabet slots and 77 envelope steps; no 6-cover; 24,585 seven-cell covers, equal set for set to covers8.json, the mirror's copy, every one covering all 102 elements with no redundant cell; the six conditions at 70.8 / 100 / 100 / 100 / 100 / 100%; the forcing at the four caps. Cites register 1820 for the exact count, §14.5.12 as printed, and the Mathematical Compendium's The seed's forced set. Both states preserved.* Registers 603; 1820. (a correction.)

### 1834

**REGISTER 604'S UNIT TEMPLATE IS IN ONE COVER IN TEN, NOT IN EVERY ONE, AND ITS FREE COORDINATE TAKES THE MIDDLE VALUE THE ENTRY EXCLUDED.** *Register 604 states that all 219 covers contain a cell matching (3, 0, 1, 1, \*, 0, 1, 1), e free at 1 or 3, and §14.5.13 prints the fork at 157 covers with e = 3 against 62 with e = 1. Over the 24,585 minimum covers enumerated exactly (register 1820) the template appears in 2,452 — 10.0% — with e = 3 in 1,478, e = 1 in 684 and e = 2 in 290, no cover holding two of the three; the template is not forced, and what the entry read as its function — carrying the alphabet values q = 1, g = 1 and 2S = 1 that the extremal corners miss — is done in every cover by some cell, because every alphabet value of every coordinate is witnessed by every seed (theorem T2, register 1835), and by this cell in one cover in ten. The sample's 219 of 219 was the randomised search's attractor, as the four corners were greedy covering's (register 596). Returned by the original-works project (SEED-CAP-FINDING.md); seated under RUL-153 Q5. Re-derived at this build by r3-q6-measure.py, seated with register 1833 — the template's three cells named, 10.0%, 684 / 290 / 1,478. Cites §14.5.13 as printed and the Mathematical Compendium's The seed's forced set. Both states preserved.* Registers 604; 1820. (a correction.)

### 1835

**REGISTER 605 IS SUPERSEDED: ITS PREMISE FAILS AT Λ₈ ITSELF, ITS FOURTH PROPERTY IS A LAW WITH A PROOF, AND CORNER 3'S UNIVERSALITY IS A PROPERTY OF THE ℓ ≤ 1 CAPS.** *Register 605 read the five cells of the 219-cover sample as binary words — corner 1 and corner 2 exact complements on 3 bits, corner 3 and the unit cell on 3, corner 4 fully specified at 11001100 — with every coordinate spoken both ways, measured at one cap and not yet a law. Over the 24,585 minimum covers enumerated exactly (register 1820) the premise fails: corner 3, (2,1,3,3,2,1,3,0), is in every cover and is the only cell that is; corner 1 is in 58.9%, corner 2 in 27.8%, corner 4 in 13.7%, the unit template in 10.0%. So properties 1 to 3 — the two complement pairings and 11001100 as the static transition of every seed — describe the sample and are refuted at Λ₈, not untested. Property 4 is a law with a proof (theorem T2 of the original-works return): ℛ recovers each coordinate's alphabet from its argument, so any X₀ with ℛ(X₀) = Λ witnesses every value of every coordinate, its minimum and maximum among them, at any cap where the alphabet has two values, and no cap enters the proof. Corner 3's own universality is cap-specific: at the three ℓ ≤ 1 caps (328, 976 and 1,968 cells) cells of its type — l, k, q, f and g at their maxima with q = k and 2S at its minimum — are element-forced, and at the d-shell cap (3,3,2,6,2), 7,605 cells, they are not. The multiplicity has a name: no element of the census has fewer than four carriers, so ℛ(Λ∖{x}) = Λ for every cell x and Λ₈ has no extreme point; ℛ on Λ₈ fails the anti-exchange property maximally (Edelman 1980; Edelman and Jamison 1985: every closed set is the hull of its extreme points if and only if the closure is anti-exchange), which is what permits 24,585 minimum generating sets with one cell common to all (Chvátal's forced set of the derived cover instance). §14.5.14's table and its closing sentence stand as printed, a description of the sample. Returned by the original-works project (SEED-CAP-FINDING.md, EXPANSION-MC54.md); seated under RUL-153 Q5. Re-derived at this build by r3-q6-measure.py, seated with register 1833: the frequencies of the four corners and the template over the enumeration; the forcing of corner 3's type at the four caps; the seed 7, 7, 7 at the ℓ ≤ 1 caps by branch and bound and at most 10 at the d-shell cap, a greedy 10-cover exhibited — that no 9-cover exists there is the return's measurement and is not re-derived here. Cites registers 602, 603, 604 and 605 as they stood, 1820, 1833 and 1834, §14.5.14 as printed, and the Mathematical Compendium's The seed's forced set. Both states preserved.* Registers 602; 603; 604; 605; 1820; 1833; 1834. (a correction.)

## C. What else the document holds, and what this pass does not do

- **`covers8.json` (4.5 MB) is read from the mirror by the instrument's cross-check, not seated.** The enumeration is
  independent of it; the cross-check is the two-route agreement chat 65 also made. If M prefers no instrument to read
  `drive/`, the alternative is to seat the file as a member (4,523,682 B in the compendia bundle) — not recommended.
- **The Request-2 and Request-3 returns** (seed laws vs 14D parallel-only; the 1D↔14D bracket proved down the tower,
  branching 4, 4, 6, 8, 9, register 334's sentence proved stage by stage; `factor.py`, `tower.py`, `tower3.py`) are results
  the document routes to prose (MC-55, the time chapter) and to the Mathematical Compendium, not to the Register; no slip
  is drafted for them and none is drafted here. Named as a lead: the bracket-system theorem has no Register entry and
  334 is cited by no entry — a subject-matter result with a banked instrument, outside Q5's scope (drafted slips only).
- **The Request-4 returns** (discrepancies A and B) were seated at pass 1 as 1821 and 1822.
- **The volumes are untouched:** §14.5.12–§14.5.14 stand as printed with 1820's pointer at §14.5.12; 13j-01 (the section
  heading false as printed) remains the prose pass's. S.bits / S.channel / S.unit and [MC-54] are the Mathematical
  Compendium's own expansion (the return authored it into the compendium at BUILD59 — the live compendium prints *The
  seed's forced set, corrected*, which 1820 cites) and are not edited by this pass.

**Rulings wanted:** (1) Part A — record the resolution in W-233 with no entry seated, and correct DEF-153R's PO-0087
row to register 504; (2) Part B — seat 1833–1835 as drafted, with `r3-q6-measure.py` and its golden; (3) 605's kind,
correction or withdrawal; (4) the cross-check reading `covers8.json` from the mirror, as is or seated.
