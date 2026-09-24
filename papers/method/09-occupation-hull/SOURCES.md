# SOURCES.md — provenance map for 09-occupation-hull (not published)

Paper: `PAPER.md`, "The Occupation Law as a Lower Convex Hull". Drafted across three runs (two cut
off by service limits on 2026-09-21; finished 2026-09-24). Every number in the paper is produced by
`check.py` (**113 of 113 obligations**: 89 EXHAUSTIVE, 17 guards, 7 MACHINE-CHECKED; `--selftest`
adds three negative controls, all refuted, 116 of 116) or is CITED. Logs of the final runs:
`scratchpad/checks/09-occupation-hull.log` and `09-occupation-hull-selftest.log`.

Paths are relative to the repository root. Instruments are imported by path, never copied:
`method/members/LW1-ground.py` (the observed ground configurations, NIST ASD 5.12),
`tools/slopeaxis.py` (the seated corridor/hull instrument, the object under test),
`method/proofs/walkresets.py` (the walk with its resets, which itself imports the recovered
`extracted/archives/restore-point-2-13/walk.py`), `method/proofs/candidateset.py` (the two
candidate-set conventions at the f openings), and `research/warp-drive/prover.py` (`require_z3`).
`method/proofs/fdomain.py` and `method/proofs/resetrule.py` were read; their measurements are
reproduced by fresh code in `check.py` rather than imported, because both fix a candidate set
(fdomain: n ≤ 7, ℓ ≤ 3) or a walk frame the paper's convention supersedes.

---

## 1 · How the corridor–hull identity resolved

**It holds, at every step, in both forms, and the earlier failures were bugs in the check.**

The decisive question of the brief was whether the identity between the entrant's corridor and
the interval between its flanking lower-hull edge slopes — which `tools/slopeaxis.py --selftest`
asserts at 106 of 106 in both forms — holds under the paper's stated convention, or fails at named
steps. Resolution:

- `python3 tools/slopeaxis.py --selftest`: SELFTEST OK, 21 fixtures, "corridor set vs lower-hull
  vertices, mismatches 0" in both forms; La's corridor (0.7071068, 1.7071068) equals the slopes of
  hull edges 4f→5d and 5d→6p.
- `check.py` section 1: under the paper's convention (frame n ≤ 15, ℓ ≤ 4, g admitted, exact
  arithmetic on surds) the three sets {corridor non-empty}, {vertex by the pairwise test},
  {vertex by Andrew's monotone chain with strict turns} coincide at all 106 steps in both forms, and
  every vertex's L, U equal its flanking edge slopes **as exact elements of ℚ(√ℕ)**. The same holds
  on 6,868 point sets of the grid {0..3}².
- `check.py` section 8: the instrument's own hull (floating point, its frame n ≤ 7, ℓ ≤ 4) equals
  the fresh exact pairwise vertex set on that frame at all 106 steps, both forms, and its entrant
  corridor equals the fresh one to 10⁻⁹ at every step. So the instrument and the paper agree step
  by step; there is no step at which the identity fails under either convention.

**What the eight failures of the first run were.** The first agent's log
(`scratchpad/checks/09-occupation-hull.log` as it stood before this run) failed at: `form p/q:
{corridor non-empty} = {vertex, monotone chain}`; `form p/q: every vertex's L, U are its flanking
hull-edge slopes`; `grid {0..3}^2 … three vertex tests agree`; `encoding fidelity: the pairwise
predicate = the chain on 300 random instances` (291 of 1,041 disagreements); `without g (l ≤ 3):
… eleven 5f steps`; and `the recovered walk's frame differs … at Li Na K Rb Ag Cs`. In that same
run the pairwise route already agreed with the corridor at every step. So the object that was wrong
was the check's third route — its monotone-chain implementation disagreed with the pairwise
predicate on 28 % of random instances, which no correct hull can do — together with two wrong
expected lists: the eleven 5f steps are 91–95 and 97–102 (curium, 96, enters 6d and is not one), and
the recovered frame lacks a ceiling at seven steps, francium included, not six. The first agent's
code is not on disk; the second agent's committed version (`6c63350`, 06:21) already carries the
present `hull_chain` (strict turns, exact signs) and the corrected lists, and passes. These were
bugs in the check, not claims of the source that fail to reproduce; nothing about the geometry
changed.

**What the second agent left undone and what this run did.** Its last words were that the
piercing-number obligation could not fail and that three float-based figures were to be made
exact. Both are done in the working copy it left: the piercing number is now certified by a
pairwise-disjoint set (a lower bound) and an exhibited set of rational stabs verified exactly to
pierce all 106 (an upper bound), reported as exact only when the two sizes agree; and the running
intersection, the coverage band and the endpoint separations are decided exactly. This run added
three things to `check.py`: the coverage band kept as surds for `figures.py` (the second agent's
exactness pass had turned it into strings, which broke fig2); an obligation that the Madelung pick
is a hull vertex at every step in both forms (for §8's sentence); an obligation that no tabulated
configuration occupies a g subshell, so 5g is admissible at every step (Theorem 4's proof needs
it); and two columns in `--table` naming the flanking hull vertices (Table 1's u and w). No
existing obligation was changed.

---

## 2 · Where each section draws from

| paper section | source passages |
|---|---|
| Thesis, Abstract, §0 | main volume `The_Method_1_6-2.md` §34.4 (lines 9576–9604, the rule and its status), §34.5 (9606–9616, the corridor, "nineteen distinct surds", the ns/(n−1)d crossing), §34.6 (9618–9650, the walk, eighteen resets, the piercing triple, "the state is necessary", the Madelung parabola), §34.9 (9678–9686, domain, the f paragraph); Mathematical Compendium 3558–3600 ("The corridor — a system of linear inequalities"), 3631–3650 ("The necessity of state" — the hull theorem in prose); `docs/SLOPE-AXIS.md`; `tools/slopeaxis.py` docstring |
| §1 D1–D2 | main volume §34.4 ("the node theorem supplies n − ℓ − 1 and antisymmetry the capacity 2(2ℓ+1)"); §34.8's provenance table (9668–9676) |
| §1 D3 | `method/members/LW1-ground.py` header (NIST ASD 5.12, GSIE, retrieved 2026-08-09, DOI 10.18434/T4W30F); main volume §34.1 (9500–9520, the opening sequence read from the 108 neutrals) |
| §1 D4 (candidate set, g admitted) | `method/members/RULINGS-R4e.md` §1 ("g is in … the law's own admissibility test is q < 2(2ℓ+1) and says nothing about ℓ"); `SETTLED-R4.tsv` rows D-21g, D-21h, D-21i; `method/proofs/candidateset.py` (the two generators and what turns on them); `tools/slopeaxis.py` `Store.LMAX_RULED = 4` |
| §1 D4 (the two forms) | main volume §34.1 (9522–9530, "with the fraction q/2(2ℓ+1) in the radicand"), §34.4 (the formula); `tools/slopeaxis.py` forms "p" and "q"; `method/members/r2-ch16y.py` `radicand()` |
| §1 D5–D6 | main volume §34.4, §34.5; Mathematical Compendium 3560–3570 ("one inequality per rival … whose solution is an interval with endpoints L, U = Δn(√p_g + √p_r)/(p_g − p_r)") |
| §1 D7, §2, §3 | Mathematical Compendium 3640–3648 ("only vertices of the lower convex hull are ever taken. A point set carrying two distinct node counts has at least two such vertices"); `tools/slopeaxis.py` docstring and `Store.hull()`; `docs/SLOPE-AXIS.md` "What it is" |
| §1 D8, §6 | main volume §34.6 (eighteen resets; "it never resets mid-subshell, which is why each subshell fills at constant a"); Register 1328 (line 4993: the handshake and the trajectory), 1403 (5273: placed at an endpoint, Pa at U), 1404 (5277: the four touching pairs); `method/proofs/walkresets.py` (its docstring quotes walk.py's rule "keep a if it still lies in the new bracket; if not, move it the MINIMUM distance to re-enter", and separates real moves from boundary touches); `SETTLED-R4.tsv` D-21a, D-21b, D-21f |
| §1 D9, §7 | main volume §34.6 ("pierced by three values of a, and three are forced: boron, lanthanum and lawrencium"); Register 1401 (5265: the fourteen forced emptyings), 1402 (5269: the count is a property of the placement rule), 1463 (5509: the running intersection empties fourteen times; Helly in one dimension), 1580 (5942: the disjoint/piercing census); `method/proofs/resetrule.py`; `tools/slopeaxis.py` `build()` (empties, coverage) |
| §1 D10, §8 | main volume §34.6 ("M = 2n − p − 1 … the parabola M = 2y − x² − 1, where ν sweeps straight lines"; "the Madelung pick lies inside the corridor at every one of the 106 steps"); Register 1437 (5409: Madelung scores 96 conditionally), 1445 (5437: held out the walk scores 90; "the corridor is non-empty at 106 of 106, which is a result about the FORM"), 1460 (5497: "an empty feasible set refutes the form and a non-empty one does not confirm it"; "the corridor tests a FORM, not a magnitude") |
| §4 Theorem 3 | no source passage: the frame lemma is this paper's. The seated instrument's own comment ("one generator convention is not a count. Sweep (NMAX, LMAX) and say which", `r2-ch16y.py`) and its banked sweep n ≤ 7…9, ℓ ≤ 3…4 are the prompt; the closed proof is new |
| §4 Table 1, Table 2, Proposition 1 | main volume §34.5 (the closed form and its four values); Mathematical Compendium 3572–3580 ("a_cross = (√(n−1) + √(n−4))/3 … the 3 in the denominator is p_g − p_r"); `r2-ch16y.out` fixtures quoted in `candidateset.py` (Ce (−∞, 0.7071068), Pa (−∞, 1.3660254) under ℓ ≤ 3) |
| §4 "How the numbers are decided" | this paper's method; the design is `research/warp-drive/proofs.py`'s exact-arithmetic discipline carried to ℚ(√ℕ) |
| §5 Theorem 4, Corollary 2 | Register 1414 (5317: "the floor is minus infinity exactly when the entering subshell is node-free … 106 of 106"); `RULINGS-R4e.md` §1 (the table of §34.9's three claims at 4f and 5f: p = 0 / 1, L = −∞ / 0, t undefined / t = 1) and §3 (the prose repair at 4f); `method/proofs/fdomain.py` (the three-line derivation: a rival lies below an opening iff its node count is smaller); `method/proofs/candidateset.py` (Pa's floor 0 with g, −∞ without; the eleven 5f exceptions); `SETTLED-R4.tsv` D-21c, D-21d, D-21e, D-21g, D-21h, D-21i, D-21j |
| §6 Proposition 2 (independent implementation) | `method/proofs/walkresets.py` `measure()`: 18 recalibrations, 9 real moves at K Rb Cs Ce Hg Tl Fr Pa Lr, 8 touches at Mo Tc Rh Gd Tb Cm Bk Rf, 5d and 6d not constant, Hg the one move not at an opening; its frame's missing ceilings at Li Na K Rb Ag Cs Fr are measured in `check.py` section 5 |
| References | main volume line 11856 (Löwdin 1969); Index of Indices 1456 and Register 4643, 4683 (Allen & Knight 2002, Demkov & Ostrovsky 1972, Klechkovskii 1962, Janet 1929, Madelung 1936); Mathematical Compendium 656–658 (Carathéodory 1911, read, not used) |

---

## 3 · Interpretation choices, stated

1. **The walk is Z = 3 … 108.** Every instrument (the seated `r2-ch16y.py`, `slopeaxis.py`,
   `walk.py`) runs `range(3, 109)`; the source says "106 steps" without stating why hydrogen and
   helium are excluded. The paper defines the walk as the 106 steps from lithium to hassium and
   does not offer a reason, because the source gives none.
2. **The candidate set admits g** (ℓ ≤ 4), following `RULINGS-R4e.md` §1. Under it Theorem 4 is
   exact; under ℓ ≤ 3 it fails at the eleven 5f steps, and the paper prints that consequence (§5).
   The frame is n ≤ 15 rather than the instruments' n ≤ 7 because Theorem 3 shows the corridors
   are frame-free from n ≥ 12 (finished) / n ≥ 8 (node-only); n ≤ 7 is below the threshold and
   differs at Fr, Ra, Lr.
3. **The corridor is open** (strict least ν), as `slopeaxis.py`'s `lo < hi` and `walk.py`'s strict
   test both have it; the endpoints are ties (Theorem 2(c)).
4. **The endpoint formula's sign.** §34.5 prints L, U = Δn(√p_g + √p_r)/(p_g − p_r); read with
   Δn = n_g − n_r (entrant minus rival) this is exactly the slope of D7. The paper writes the
   slope and its rationalised form and does not reproduce the source's typography.
5. **"Recalibration", "move", "touch".** `walk.py` counts a recalibration whenever the strict test
   fails and nudges a by ε = 10⁻⁶; `walkresets.py` separates real moves (|Δa| ≥ 10⁻⁴) from boundary
   touches. The paper's threshold is 10⁻³; no |Δa| lies between 2 × 10⁻⁶ and 0.07 (the smallest real
   move, Tl 1.0000 → Fr… see Table 3), so any threshold in that range gives the same partition.
6. **"Lies inside the corridor" for the Madelung pick** (§34.6) is read as "is a hull vertex, so
   its corridor is non-empty"; under that reading it holds at 106 of 106 in both forms and the
   paper says so. Other readings (e.g. that the pick's ν at the carried a is inside some interval)
   were not tested.
7. **The instrument's "17 distinct hull-edge slopes"** and **"walk resets 10"** are frame- and
   rule-specific figures: 17 is the endpoint count at n ≤ 7 (the paper's frame-free count is 19,
   and the two extra are the ceilings √6 + √7 and (√5 + √7)/2 that n ≤ 7 lacks), and 10 is the
   instrument's count of value-changing placements without an ε nudge (= the paper's 1 initial
   placement + 9 moves). The paper prints 19 and 18/9/8 with their conventions.
8. **The finished-form endpoint count.** The instrument prints 134 at ℓ ≤ 4 (121 at ℓ ≤ 3) on
   n ≤ 7; the frame-free count is 138 (the finished form differs from the n ≤ 7 and n ≤ 8 frames
   at six steps). The paper prints 138.
9. **MEASURED** is used, as in `04-seaton`, for numbers computed from the cited configurations by a
   procedure with a stated parameter (the walk); the walk's exactness argument (§6) says why the
   floating-point walk equals the exact one.

---

## 4 · Reproduction — what reproduces and what does not

**Reproduced exactly.** All 106 corridors non-empty, both forms. The crossing closed form and its
values at n = 4, 5 (0.5773503, 1.0000000). Register 1414's equivalence (26 no-floor steps = the
node-free entrants) with g admitted, and its failure at exactly the eleven 5f steps without g.
Register 1403's "protactinium's L is degenerate at zero" and "Pa takes U". Register 1401's fourteen
emptyings at 37 42 43 45 55 58 64 65 80 91 96 97 103 104. Register 1463's "eleven" for the finished
form (25 43 58 64 65 87 91 96 97 103 104). Register 1404's four touching pairs Mo/Tc (1), Gd/Tb
(√2/2), Cm/Bk ((1+√3)/2), Lr/Rf ((√3+√5)/2). Register 1580's disjoint triple B / La / Lr and
piercing number 3. Register 1328's eighteen recalibrations and its nine values (0.5774, 1.0000,
1.2168, 0.7071, 0.8090, 1.0000, 1.3938, 1.3660, 1.9841) to 10⁻¹⁵ against `walkresets.py`.
Register 1437's Madelung score 96 of 106 with its ten misses Mo Rh Pd La Gd Au Ac Th Cm Lr.
`slopeaxis.py`'s 86 and 90 best coverage, 14 and 11 emptyings, 17 endpoints on its frame, its
|A| histogram {3: 6, 4: 56, 5: 28, 6: 14, 7: 2} on its frame, its 106/106 vertex identity.
`RULINGS-R4e.md`'s table: at 5f p = 1, L = 0, t = 1; at 4f p = 0, L = −∞, t undefined.

**Not reproduced, recorded; the paper prints the reproduced value or omits the claim.**

- *§34.5 and Mathematical Compendium: "0.5773503, 1.0000000, 1.2168450, 1.3938270 at n = 4 to
  7".* The closed form (√(n−1) + √(n−4))/3 evaluates to **1.2167605** and **1.3938469** at n = 6, 7.
  The source's last two decimals are wrong by 8.5 × 10⁻⁵ and 2.0 × 10⁻⁵ (this is the record's own
  16z-04 / 34re-01, quoted in `walkresets.py`'s fixtures). The paper prints the exact values.
- *§34.5: "Nineteen distinct surds across the whole table."* On the instruments' frame n ≤ 7 the
  count is 17 (`slopeaxis.py` fixture; `r2-ch16y.out` sweep). Under the full candidate set the
  count is **19**, and Table 2 lists them. Whether the source's nineteen are these nineteen cannot
  be checked, because the source does not list them; the agreement in number is not claimed as a
  reproduction of the source's list.
- *§34.6: "It never resets mid-subshell, which is why each subshell fills at constant a."* FALSE
  for 5d (moved at Ce 58, open 57–79) and 6d (moved at Pa 91 and Lr 103) — `SETTLED-R4.tsv` D-21a/b,
  reproduced here (§6 Proposition 2(e)). The paper states the measured result. The first clause is
  read as "every move is at the opening of the *entering* subshell", true at 8 of 9 (Hg the
  exception), and the paper says that.
- *§34.6: "Every reset is a subshell opening (8), an aufbau exception (6), or the return from one
  (4)."* `check.py` does not classify the eighteen this way and `walkresets.py` refuses to rescore
  the partition; the paper classifies by move/touch and by "at the entrant's opening" instead and
  does not print 8 / 6 / 4.
- *§34.6 and Mathematical Compendium: "every step admits more than one self-consistent subshell:
  two to six across the table, and one never."* Measured: **3 to 7** on the instrument's frame
  n ≤ 7 ({3: 6, 4: 56, 5: 28, 6: 14, 7: 2}) and 11 to 15 on n ≤ 15. "Two to six" reproduces under
  no frame tried; "one never" reproduces under all (Corollary 1 proves it). The paper prints the
  measured ranges with their frames.
- *§34.9: "At any f opening p = n − ℓ − 1 = 0 … so no rival lies below and L = −∞."* False at 5f
  (p = 1; L = 0 with g admitted) — `RULINGS-R4e.md` §1 and §3, `SETTLED-R4.tsv` D-21c/d/h/j. The
  paper carries the replacement theorem (Theorem 4, the register-1414 form) and Corollary 2, and
  states the 5f case exactly as the settled record has it.
- *Register 1580 and `RULINGS-R4e.md`: "73 bounded both sides / 7 below-only / 26 above-only";
  "73 of the 106 steps carry a two-sided corridor".* These are figures of `walk.py`'s truncated
  candidate set, which has no subshell to the right of an ns opening and so no ceiling at Li Na K
  Rb Ag Cs Fr. Frame-free (Theorem 3) the figures are **80 two-sided / 0 below-only / 26 no-floor**;
  the paper prints those. The 26 agree.
- *Register 1328: "0 → 0.5774 (K) → 1.0000 (Rb) → 1.2168 (Cs) → 0.7071 (La) → …"* and *Register
  1403: "lanthanum 0.7071 … sits exactly at L".* The value 0.7071 = √2/2 is reached at **cerium**
  (58), as the ceiling of 4f's corridor, not at lanthanum (57), where the carried 1.2168 lies inside
  (√2/2, (2+√2)/2) and no recalibration occurs; La's floor happens to be the same surd. Register
  1328 also omits Tl (1.0000, at L) from its trajectory. `walkresets.py`'s fixtures already have
  "0.7071 from Ce" and "1.0000 from Tl"; the paper follows the measurement (Table 3).
- *Register 1403: "seven sit exactly at L … and the eighth, protactinium, sits exactly at U".*
  Measured on the nine moves: seven at L (K Rb Cs Hg Tl Fr Lr) and **two at U (Ce, Pa)**. The paper
  prints the nine.
- *Register 1445: "held out … 90 of 106".* The paper's own held-out score, for its own placement
  rule (stay, else nearest endpoint + ε), is **88 of 105** node-only and 91 of 105 finished, with
  no ties; the source's 90 was produced by a different scorer (`scorer.py`, higher-n tie-break,
  different frame) and is not reproduced or claimed. Register 1580's "STAY reaches 92" likewise
  belongs to `trajectory.py` and is not claimed.
- *Mathematical Compendium: "the unfilled set carries two [node counts] below 124 electrons — every
  neutral atom there is".* Not tested (the paper's data end at Z = 108); not claimed.
- *`docs/SLOPE-AXIS.md`: "best coverage … at a = 0.5780" and "at a = 1.0010".* The instrument's
  grid probe. The paper gives the exact band on which the maximum is attained, (√3/3, √2/2) and
  (1, (5√2 + √5)/9), which contain those probes; the point values are not printed.

**Claims of the source outside the paper's scope, not evaluated.** §34.7's entry point
t(ℓ) → √(ℓ(ℓ+1)/2) and its measured 1.028 / 1.785 (the record carries them as 34re-04
unreproducible and `SETTLED-R4.tsv` T-01 as an open definition conflict); §34.10's method
narrative; Register 1402's five policy counts (`resetrule.py` reports POLICY-NOT-DEFINED);
Chapter 35's derivation. None is mentioned in the paper.

---

## 5 · Tolerances that remain, and why

- The walk (D8) uses ε = 10⁻⁶ and floating-point a. §6 argues, and section 5 of `check.py`
  verifies, that the recalibration sites and endpoints are identical for ε = 10⁻⁴ … 10⁻¹⁰ and that
  every touch moves a by exactly 2ε; the endpoint separations are certified above 10⁻⁴ exactly.
- Comparisons with the two floating-point instruments (`slopeaxis.py` section 8, `walkresets.py`
  section 5) are at 10⁻⁹; measured agreement is 8.9 × 10⁻¹⁶ on the nine walk values.
- The held-out prediction (§8) evaluates ν at the carried float a with a 10⁻⁹ tie test; 0 ties.
- Everything else — corridors, hull, endpoints, emptyings, disjointness, piercing, coverage,
  Theorem 3's extremes — is exact: representation equality for zero (Besicovitch 1940), rational
  enclosure for sign; deepest enclosure 24 digits, smallest certified magnitude 4.43 × 10⁻⁸.
