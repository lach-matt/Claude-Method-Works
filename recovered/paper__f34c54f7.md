# Cold Fusion Under a Closed Index
## A refusal, a computation, and a reduction — the method of the Lach Cylinder applied outside spectroscopy

**Matthew Lach** — Independent researcher
*Draft v0.1, prepared with the computing collaborator, 31 July 2026*
*Companion to* The Method v1.2 (The Lach Cylinder — an index of transitions: closure, self-reference, and the price of certainty)

---

## Abstract

The question "can a stable cold fusion reaction be identified between two cells of Λ?" is put to the framework of *The Method* and answered by the framework's own machinery. The answer is a refusal, derived on three independent routes (B.2.8): by the law (E(Λ) = 0, §18.6 — a complete index makes exactly zero predictions), by the coordinates (all eight are electronic; the bracket is measurably blind to nuclear charge, Ch. 11), and by the data (ⅅ_phys terminates outside the index, and no reproducible measured levels exist to bracket). The refusal is then treated as P8 requires — as a bound, not a dead end. It identifies the correct index for the question: the nuclide chart on (Z, N), named in §1.2 of the book. Computed on measured particle-stability data rather than as drawn, that chart is **not** closed: E(X) = 9 on the window Z ≤ 9, and the nine cells the structure admits and nature denies are ⁵He, ⁷He, ¹⁰Li, ⁸Be, ¹³Be, ⁹B, ¹⁶B, ¹⁸B, and ²¹C. Eight of the nine have odd N; the pattern the coordinates cannot carry is pairing, and the single even–even exception, ⁸Be, is alpha clustering. The drawn chart is proved to be exactly the ℛ-closure of the measured one (idempotence verified; E(drawn) = 0), which corrects the referent of the book's §1.2 row and converts its E = 0 entry into a statement about a model band. Three of the nine holes — ⁵He, ⁸Be, ⁹B — are the compound systems of the classic two-cell fusion reactions, so the chart's non-closure *is* the reaction mechanism: fusion exit channels and missing cells coincide. Finally, the achievability question is reduced (P3, with its residue stated per B.2.16.3) to a laboratory commensurability protocol: per watt of claimed excess heat, 1.91×10¹² events/s through ³He + n, 1.55×10¹² through t + p, or 2.62×10¹¹ through ⁴He + γ, with heat and nuclear products required to agree through Q along two routes sharing no step. Null results are converted, per B.2.15, into upper bounds on the screened d–d rate enhancement — the claim under test being an enhancement of roughly fifty orders of magnitude over the screened molecular baseline. The reduction makes the question decidable; it does not make the answer yes, and the paper closes with its own register of corrections, declines, and degraded provenance.

---

## Part 0 — The shape of the argument

This paper makes three moves, and each is a chapter of *The Method* run on a question the book did not ask.

**The refusal.** The cold fusion question, posed on Λ, is answered by the book's central theorem before any physics is consulted: the number of predictions an index can make is E(X), and E(Λ) = 0. The refusal is derived three ways, and the three derivations agree (§2).

**The computation.** The refusal, read as a bound (P8), points at the right index — the nuclide chart on (Z, N). The book's §1.2 lists that chart at E = 0. Computed on measured data it is E = 9 on Z ≤ 9 alone, and the excess is physics, not noise (§3). The correction to §1.2 is entered in the register (§9, R1).

**The reduction.** The holes of the computed chart are the exit channels of real fusion. That fixes, per watt of any claimed excess heat, the nuclear product rates that must accompany it — three equalities that any calorimetry laboratory can test, under a protocol that is the book's Appendix B translated bench-ward (§§4–6). The measured record of thirty-seven years, including the ARPA-E program concluding in July 2026, is read against it (§7). What the reduction cannot do is stated in the book's Ch. 13 form (§8), and everything withdrawn, declined, or degraded in the course of this work is registered (§9).

Every number in this paper was computed before the sentence describing it was written (B.2.14), and the two predictions it contains were committed before their computations were run (B.2.13). The code is Appendix A. The machinery borrowed from the book is indexed in Appendix B. The numbers are indexed in Appendix C.

---

## 1. The question and its language

"Is cold fusion achievable?" is posed in the documentary language, and P20 is exact about what that costs: the documentary language has no closure mechanism. No search over Λ, no search over the literature, and no amount of restatement closes a question in that form. Before anything can be tested, the question must be translated into a language with a closure operator — and the translation is not free. It is the substance of this paper.

Two translations are attempted. The first — "identify a stable cold fusion reaction between two cells of Λ" — is well-posed and closes immediately, in the negative, and §2 gives the derivation. The second — "what would decide, in a laboratory, whether fusion proceeds at ambient conditions at a measurable rate?" — is well-posed on a different index, and §§3–6 construct it. The gap between the two translations is where the field has lived since 1989, and B.2.9 names the discipline that keeps this paper out of it: a question is admissible or it is refused; it is never silently defaulted into a different question that happens to have an answer.

---

## 2. The refusal, on three routes

Per B.2.8, a conclusion that matters is derived twice by routes sharing no step. This one is derived three times.

### 2.1 Route one — the law

§18.6 of the book: the number of predictions an index can make is E(X), because a prediction is a proposal about a cell the structure admits and the index does not yet hold. E(Λ) = 0, verified over all 475,800 pairs. A "stable cold fusion reaction between two cells" would be content Λ does not carry, and a complete index proposes exactly zero such content. Extracting a fusion prediction from Λ would not stretch the framework; it would contradict the theorem the framework exists to prove. The refusal here is not caution. It is the theorem, applied.

### 2.2 Route two — the coordinates

Read the eight coordinates of Λ: (n, ℓ, k, q, e, f, g, 2S). Every one is electronic. The transition coordinate q moves *electrons* between configurations; no coordinate of Λ₈, Λ₉, or Λ₁₃ carries Z or A, and fusion is by definition a change in (Z, A).

The book carries measured proof of the consequence, and it is the Chapter 11 episode: a wrong nuclear charge propagated through the work while the bracket held 56 of 56, because Z cancels from containment. Two derived quantities the method never uses flagged it immediately; the bracket itself could not, ever. An index demonstrably blind to Z cannot define a reaction whose entire content is a change in Z.

The energy scales say the same thing a third way. Λ's structure lives at Rydberg scale — electron-volts. The d–d Coulomb barrier and the fusion Q-values live at keV–MeV, six orders of magnitude outside every bound in the object.

### 2.3 Route three — the data

The bracket deduces from measured neighbours, and ⅅ_phys terminates outside the index at reproducible, provenance-carrying measurements — the book's Chapter 17 kind of content, the only kind that no index supplies. For cold fusion there is no such dataset: after thirty-seven years there exists no on-demand, repeatable experiment whose levels could serve as neighbours (the phrase is ARPA-E's own; §7). A bracket with no admissible neighbours returns nothing, and B.2.9 says that nothing is a refusal, never a default.

### 2.4 The grid

Per B.2.16, laid as requirements so the obstacle is visible rather than hunted:

| requirement | status |
|---|---|
| cells carrying (Z, A) | **empty — first empty cell** |
| a reaction operator moving nucleons | empty (q moves electrons) |
| MeV-scale energy coordinate | empty |
| barrier and rate physics | external — ⅅ_phys |
| measured neighbours to bracket | none reproducible |

Everything below the first empty cell is downstream of it.

### 2.5 The P22 warning

P22's demonstration in the book bears exactly on what would happen if a "fusion cell" were forced into Λ anyway. There, a single physically impossible cell (one electron, multiplicity 2) was absorbed by an index whose rule was inferred rather than stated; the index revised its rule, admitted 74 further impossible cells, and remained closed at E = 0 throughout. Closure defends against loss and never against invention. Λ would *accept* a fabricated fusion cell and stay closed while doing it. This question is precisely the case the principle warns about, and the warning is why the refusal must come from the stated rules (§2.1–2.3) rather than from watching whether the object complains. It would not.

### 2.6 The refusal as a bound

Per B.2.15, in the register form:

> *attempted* — identify a stable cold fusion reaction between two cells of Λ.
> *excludes* — any nuclear content in Λ's answer space: by the law (E = 0), by the coordinates (no Z, and measured Z-blindness), by the scale (eV vs MeV), and by the data (no admissible neighbours).
> *kind* — structural.

And a structural exclusion names the right object by ruling out the wrong one. The book's own §1.2 already lists it: the nuclide chart, coordinates (Z, N), with drip lines — entered there at 383 cells, E = 0, self-defining. On *that* index, two-cell fusion reactions are content, not prediction: Q = [m(a) + m(b) − Σm(products)]c², computed from measured masses with stated uncertainties. What §3 shows is that the row's E = 0, when computed rather than assumed, does not survive — and that its failure is the most informative thing in this paper.

---

## 3. The computation — E(X) of the measured nuclide chart

### 3.1 The reconstruction, restated from §1.1 of the book

Given a set of cells X on coordinates (x₁, …, x_d), read off the value sets Âᵢ(X) = { xᵢ : x ∈ X } and the bounds φ̂ᵢⱼ(v) = max{ xᵢ : x ∈ X, xⱼ ≤ v }, and form

    ℛ(X) = { x ∈ ∏ Âᵢ(X) : xᵢ ≤ φ̂ᵢⱼ(xⱼ) for all i ≠ j }

E(X) = |ℛ(X)| − |X| is the external definition cost: cells the structure implies and the index denies. On two coordinates (Z, N) this specialises to the running-maxima form of §23.3: ℛ(X) = {(Z, N) ∈ Â_Z × Â_N : Z ≤ maxZ(N′ ≤ N), N ≤ maxN(Z′ ≤ Z)}, with both maxima cumulative. §23.3 proves that a set is ℛ-closed iff it is exactly such a two-sided running-maxima staircase — which will matter in §3.5.

### 3.2 The dataset, and its provenance

X = particle-bound ground states (stable against prompt nucleon emission; β-instability does not exclude), window Z = 1 to 9, encoded as follows. Provenance per B.2.11, honestly: the computing environment had no network access to the evaluated files, so the assignments are recalled NUBASE2020 content, with the weakest rows subsequently verified against the published literature by search. Verified rows: the fluorine drip pattern — ³¹F last bound, ²⁸F and ³⁰F unbound by neutron decay, ²⁶F the last bound odd-N fluorine isotope (Ahn et al. 2019/2022; Kahlbow et al. 2024; RIKEN BigRIPS dripline program) — and ²⁴O as the heaviest bound oxygen isotope. Unverified-but-textbook rows: the A = 5 and A = 8 gaps, ⁶Be, ⁸C, ¹⁰,¹¹N, ¹²O. The full encoding is in Appendix A; every hole reported below survives even generous error in the marginal rows, because ⁸Be alone forces E > 0.

| Z | bound N values | excluded (unbound) |
|---|---|---|
| 1 (H) | 0, 1, 2 | ⁴H–⁷H |
| 2 (He) | 1, 2, 4, 6 | ⁵He, ⁷He, ⁹He, ¹⁰He |
| 3 (Li) | 3, 4, 5, 6, 8 | ⁴Li, ⁵Li, ¹⁰Li, ¹²Li |
| 4 (Be) | 3, 5, 6, 7, 8, 10 | ⁶Be, ⁸Be, ¹³Be, ¹⁵Be |
| 5 (B) | 3, 5–10, 12, 14 | ⁷B, ⁹B, ¹⁶B, ¹⁸B |
| 6 (C) | 3–14, 16 | ⁸C, ²¹C |
| 7 (N) | 5–16 | ¹⁰N, ¹¹N |
| 8 (O) | 5–16 | ¹²O, ²⁵O–²⁸O |
| 9 (F) | 8–18, 20, 22 | ¹⁶F, ²⁸F, ³⁰F |

77 cells.

### 3.3 The commitment

Per B.2.13, recorded before the computation was run, verbatim from the working session: *"my prediction is that the real chart, computed from measured particle stability, is not E = 0 — and that the excess cells will include ⁵He, ⁸Be, and ⁹B."* The commitment names three cells and a sign; the computation is entitled to embarrass it.

### 3.4 The result

    |X| = 77    |ℛ(X)| = 86    E(X) = 9    X \ ℛ(X) = ∅

The commitment held, as a lower bound: three committed, nine found, and all three committed cells among the nine. X ⊆ ℛ(X) exactly — no cell of the chart is denied by its own bounds, so the reconstruction is sound and the chart is simply not closed. The nine cells the structure admits and nature denies:

| hole (Z, N) | system | N parity | what its absence is |
|---|---|---|---|
| (2, 3) | ⁵He | odd | the mass-5 gap, neutron side |
| (2, 5) | ⁷He | odd | drip-line staggering in He |
| (3, 7) | ¹⁰Li | odd | the unbound core+n of the ¹¹Li halo |
| (4, 4) | **⁸Be** | **even–even** | the mass-8 gap — the triple-alpha bottleneck |
| (4, 9) | ¹³Be | odd | staggering at the Be drip |
| (5, 4) | ⁹B | even (odd-Z) | mirror of ⁹Be, unbound |
| (5, 11) | ¹⁶B | odd | odd-N staggering at the B drip |
| (5, 13) | ¹⁸B | odd | odd-N staggering at the B drip |
| (6, 15) | ²¹C | odd | odd-N staggering at the C drip |

### 3.5 The drawn chart is the closure of the measured one

The book's §1.2 row — "a nuclide chart with drip lines, 383 cells, E = 0, self-defining" — is true of one object and false of another. A chart whose drip lines are *drawn* as monotone staircases is ℛ-closed automatically, by the §23.3 characterisation: any two-sided running-maxima region has E = 0 by construction. That is the object the row names — a model band.

The relation between the two objects is exact, and it was computed rather than asserted: ℛ is idempotent on this data — ℛ(ℛ(X)) = ℛ(X), verified — so ℛ(X) is itself a closed chart of 86 cells with E = 0, and it equals the measured chart with the nine holes filled. **The drawn chart is precisely the closure of the measured one, and the drawing hides the physics by filling the holes.** The correction to the book is register entry R1 (§9): the §1.2 row should state which chart it computed — the band or the measurement — because the two differ by exactly the nine most structurally interesting cells in the window, and by more beyond it.

P21 gives the right verdict on the discrepancy, and it is the opposite of the P21-instrument case: when a property holds in the model and fails in the measurement, that is not a mistranslation to repair — it is ⅅ_phys doing precisely its job. The model closes; nature does not; the difference is content.

### 3.6 Reading the holes — the rhyme

§1.3 of the book: the calendar's E = 7 is the content of *Thirty days hath September* — the information the coordinates cannot carry, exactly seven cells long. The nuclide chart's E has the same character, and it decomposes:

**Eight of the nine holes have odd N.** The pattern (Z, N) cannot encode is the pairing interaction — the odd–even staggering of binding that makes the drip line ragged where the smooth staircase overshoots. E(X) is, cell by cell, the pairing term of the mass formula made visible as an indexing defect.

**The ninth hole is the exception that carries its own physics.** ⁸Be is even–even — pairing favours it — and it is unbound anyway, because it is two alpha particles that will not stay together. The one hole the parity pattern fails to explain is explained by alpha clustering, and its existence is why stellar helium burning requires the triple-alpha process: the (4, 4) cell is missing, so the universe routes around it through a resonance.

E(measured chart) is not a defect count. It is the chapter of nuclear structure that the coordinates cannot carry, and it is nine cells long in this window for the same reason the rhyme is seven.

### 3.7 What the operator missed, recorded

Two limitations of ℛ surfaced in the computation and are recorded rather than smoothed over (B.2.6, B.2.15):

**The value-set escape.** ²⁸F (N = 19) and ³⁰F (N = 21) are physically exact analogues of the other odd-N holes — unbound isotopes inside the reach of the staircase — but they do not appear in ℛ(X) \ X, because no bound nuclide in the window has N = 19 or N = 21 at all, so those values vanish from Â_N and ℛ cannot express the cells. A hole in a *value set* is invisible to a reconstruction built on value sets. *Kind: structural — a statement about the operator, not the chart.* The book's ℛ was designed for indices whose coordinate values are dense in their ranges; on sparse value sets it undercounts, and E = 9 is therefore a lower bound on the window's true external-definition cost.

**The window decline.** ¹⁶F (Z = 9, N = 7) is unbound while ¹⁷Ne (Z = 10, N = 7) is bound, so (9, 7) becomes a hole the moment the Z = 10 row enters — but the Z = 10 row's neutron-rich end could not be encoded at the confidence standard of §3.2, so the window was cut at Z = 9 and (9, 7) is declined, not counted. *Cause: data confidence. Recorded per B.2.6.*

Neither limitation threatens the sign of the result. Both sharpen it: the true E of the measured chart, on any honest accounting, is larger than 9.

---

## 4. Holes as exit channels — non-closure as mechanism

Here the two halves of the paper meet, and the meeting was not designed; it fell out of the computation.

The classic light-fusion reactions, with Q from measured masses:

| reaction | compound system | its cell | status | products, Q |
|---|---|---|---|---|
| d + t | ⁵He* | (2, 3) | **hole** | ⁴He + n, 17.59 MeV |
| p + α | ⁵Li* | — | unbound (outside ℛ's reach, §3.7-adjacent) | no bound product |
| α + α | ⁸Be | (4, 4) | **hole** | decays back to 2α; bottleneck |
| d + d | ⁴He* (23.85 MeV excitation) | — | bound g.s., unbound at Q | ³He + n / t + p / ⁴He + γ |

d + t proceeds, and releases its energy as it does, *because* (2, 3) is a hole: there is no bound ⁵He to hold the product together, so the compound system flies apart as ⁴He + n at 17.59 MeV. Helium burning in stars stalls at first *because* (4, 4) is a hole. And d + d, the cold fusion workhorse, forms a compound ⁴He* at 23.85 MeV of excitation — far above every particle threshold — whose only exits are the three channels of §5.

The general statement, in the book's language: **the exit channels of a fusion reaction are the E(X) structure of the nuclide chart in the neighbourhood of the compound cell.** Where the compound cell is a hole, the reaction is fast and its products are dictated; where it is occupied, the energy must leave electromagnetically and the reaction is slow. Fusion output cells and missing cells coincide. The chart's failure to close is not a defect to repair — it is, cell for cell, the mechanism. This is §1.3's lesson at full strength: non-closure as a purchase, here purchasing the existence of exothermic nuclear reactions at all.

---

## 5. The reduction — from "achievable?" to three equalities

### 5.1 The decomposition, by P3

P3: when the path is not found, work backwards from the desired output to an established input. The desired output is a decision on achievability. Backwards:

*Achievability* is a documentary claim (§1) → translate to a **rate claim**: fusion events occur in condensed matter at ambient conditions at rate r > r_detectable → any nonzero rate has **mandatory exit channels**, fixed not by any model but by the hole structure of §3–4 → each channel carries a fixed Q, so a claimed excess power P implies **exact product rates** → equalities between two independently measured quantities, which is the established input: a laboratory test.

Per B.2.16.3, the reduction and its residue in one sentence: the question reduces to three commensurability equalities that any calorimetry laboratory can test, *and the residue is that the reduction makes cold fusion decidable, not likely — the index supplies the bookkeeping and never the rate.*

### 5.2 The equalities, computed

Per watt of claimed excess heat, if the heat is d–d fusion (computed; Appendix A):

| channel | Q (MeV) | mandatory rate per watt |
|---|---|---|
| d + d → ³He + n | 3.269 | 1.91 × 10¹² events/s |
| d + d → t + p | 4.033 | 1.55 × 10¹² events/s |
| d + d → ⁴He + γ | 23.847 | 2.62 × 10¹¹ events/s |

Consequences at laboratory scale, computed:

- **Vacuum branching** (~50:50 n : t, γ branch ~10⁻⁷) predicts **8.55 × 10¹¹ neutrons/s per watt** — a lethal, unmissable, unshieldably characteristic flux. Its absence at claimed watt-level excess heat is not a subtlety; it is a factor of ~10¹² against the vacuum-branching hypothesis.
- **The ⁴He branch** predicts **3.76 × 10⁻⁸ mol of helium per watt-day** — comfortably above mass-spectrometric detection floors — *plus* 23.85 MeV per event that must appear as a gamma or be anomalously converted to lattice heat, either of which is independently detectable.

### 5.3 The residue inside the residue

The historical claims (excess heat, ⁴He roughly commensurate, no neutrons or tritium at commensurate levels) therefore require the d–d branching to shift by ~10⁷ toward the ⁴He channel with the 23.85 MeV gamma suppressed. Stated plainly, as most of the literature did not: **that is itself a nuclear claim, requiring its own two-route evidence.** A reduction that hid it would be progress-looking twice, once for what it explains and once for what it has not been tested on (B.2.16.3). It is on the grid (§6.5) as an explicit row.

### 5.4 Two routes, no shared step

B.2.8, bench form: the heat route (calorimetry, with its calibration chain) and the product route (neutron counting, tritium assay, helium mass spectrometry, gamma spectroscopy — with theirs) must share no instrument, no calibration standard, and no analysis step. Then the equalities of §5.2 are a genuine cross-check: heat without commensurate products is not weak evidence of fusion — it is a *measured disagreement between two routes*, and under B.2.9 a disagreement is a refusal, never a coerced positive. An identity computed along one path is vacuous; the whole content of the test is the independence.

---

## 6. The protocol — Appendix B, translated bench-ward

The book's working protocols map onto the decisive experiment nearly line for line. The mapping is this paper's most directly exportable product.

| protocol | book form | laboratory form |
|---|---|---|
| B.2.2 | admissibility r ≥ 5 | excess power admissible only at ≥ 5× total calorimeter uncertainty, threshold stated in advance |
| B.2.5 | census before search | enumerate testable material/loading conditions from theory and prior record before running |
| B.2.6 | declines recorded | every null run published with its sensitivity; no file drawer |
| B.2.8 | two independent routes | heat chain and product chain share no step (§5.4) |
| B.2.9 | refuse rather than coerce | run admissibility decided by pre-stated criteria; no post-hoc selection of "active" runs; anomalies refused, not defaulted into signals |
| B.2.10 | enumerate, then re-enumerate | the condition grid (§6.5) re-enumerated whenever materials science adds an axis |
| B.2.11 | provenance | every calibration traceable; every datum to instrument, run, and timestamp |
| B.2.12 | withdrawals logged | retracted runs and claims kept in the record with what replaced them |
| B.2.13 | commit before you look | predicted heat *and* product rates written and signed before the cell is powered (§6.2) |
| B.2.14 | compute, then write | rates computed from Q before any interpretive sentence about a run |
| B.2.15 | every failure is a bound | every null converted to an upper bound on the enhancement (§6.4) |
| B.2.16 | the grid | conditions × diagnostics laid as an index; read the empty cells (§6.5) |

### 6.1 Admissibility

The book's r = 2Z²R/(ν³σ) ≥ 5 rule is a signal-to-uncertainty admissibility criterion stated *before* the data are seen, with the domain boundary computed in advance. Its bench translation: excess power P is admissible only when P ≥ 5σ_cal, where σ_cal is the full calorimeter uncertainty including calibration drift, measured on blanks under identical protocol — and the run schedule, including which runs are blanks, is fixed before any run is opened.

### 6.2 The committed-prediction sheet

The B.2.13 document an experimenter signs before powering a cell:

> **Committed before measurement — run [ID], date, signature.**
> 1. Predicted excess power: P = ____ W ± ____ (or: null predicted).
> 2. If P > 0 and the source is d–d fusion, mandatory product rates (from §5.2): neutrons ____/s; tritium ____/s; ⁴He ____ mol/day; 23.85 MeV γ ____/s. Claimed branching, if non-vacuum, stated here with its independent evidence: ____.
> 3. Admissibility threshold: 5σ_cal = ____ W, from blank series [IDs].
> 4. Diagnostics in place, with independent calibration chains: [list]. Routes shared between heat and product chains: **none** (enumerated check).
> 5. Disposal of every outcome, pre-stated: signal above threshold with commensurate products → claim; signal without products → route disagreement, refused as fusion evidence, registered; null → bound entered per §6.4.
>
> *The constraint is visible ≤ committed, of §11.4 form, closed, E = 0: nothing may be read before something is written.*

### 6.3 Declines and the file drawer

B.2.6: a collection reporting only successes cannot be checked. The field's central pathology for thirty-seven years has been exactly this — positive anomalies reported, nulls unpublished or unpublishable, run selection unstated. The protocol's cure is mechanical: the run schedule is the enumeration, every scheduled run appears in the record with its outcome and sensitivity, and a rejected run carries its rejection cause from a pre-stated list, exactly as the book's four decline causes (dilution, depth, scheme change, interleaving) carry theirs.

### 6.4 Nulls as bounds — the 1,061 move

B.2.15 is the book's signature: the bracket's non-failure became 1,061 perturbation bounds because someone insisted that a nothing be defined rather than discarded. Applied here:

The screened molecular-D₂ fusion rate is ~3 × 10⁻⁶⁴ per pair per second (Koonin & Nauenberg 1989; *recalled — provenance degraded, flagged*), i.e. ~10⁻⁴⁰ fusions/s in a full mole of deuterium. Watt-scale excess heat therefore claims an environmental enhancement of **roughly fifty orders of magnitude**. Every calibrated null at stated sensitivity is then an *upper bound on the enhancement* at that material, loading, and temperature:

> *attempted* — condition c, sensitivity s. *excludes* — enhancement η(c) > s/r₀ at condition c. *kind* — upper bound.

A program of such nulls does not fail to find cold fusion. It **measures the enhancement ceiling as a function of conditions** — numbers where there were anecdotes. After thirty-seven years of unbounded silence, a bounded silence would be new, and it is publishable regardless of outcome, which dissolves the funding stalemate ARPA-E itself diagnosed (§7).

### 6.5 The grid

Conditions × diagnostics as an index, per B.2.16, with the current occupancy honestly marked:

| requirement | status |
|---|---|
| one on-demand repeatable positive cell, anywhere in the grid | **empty — first empty cell** |
| enhancement ceiling η(c) mapped over (material × loading × T) | sparse; a few bounded points |
| the 10⁷ branching-shift claim, independently evidenced | empty (§5.3) |
| γ-suppression / lattice-conversion mechanism, independently evidenced | empty |
| commensurability equalities tested with two clean routes | partially — 2019 revisit; ARPA-E teams, reporting 2026 |
| multi-messenger correlated diagnostics standard | in progress (ARPA-E design requirement) |

Every empty cell is downstream of the first. The grid also says what §2 said from the other side: nothing in it is a prediction. It is a map of where the silence is bounded and where it is not.

---

## 7. The measured record — ⅅ_phys

The regress terminates outside, at measurements no index supplied. The record, briefly and with provenance:

**1989 and 2004.** Two DOE reviews, fifteen years apart, each concluding that the evidence did not establish a nuclear origin for the reported anomalies and that no special program was warranted, while allowing well-designed individual proposals. (*Recalled; primary documents public.*)

**2019.** The Google-funded multi-laboratory revisit (Berlinguette et al., *Nature* 570, 45) found no evidence supporting cold fusion claims under the tested conditions, while materially improving calorimetry, materials control, and — notably for §6 — the norm of publishing nulls with sensitivities. (*Recalled; flag.*)

**2021–2026.** ARPA-E's own framing, verbatim in its program documents: despite a large body of reported evidence over 30+ years, *there still does not exist a widely accepted, on-demand, repeatable LENR experiment nor a sound theoretical basis*, producing a stalemate in which lack of rigorous results inhibits funding and lack of funding inhibits rigorous results. Its response — a 2021 workshop, then a 2023 Exploratory Topic funding eight teams at $10M with projects running to **July 2026** — asks for *specific, testable hypotheses that can be supported or retired upon the collection of correlated, multi-messenger nuclear diagnostics*. That is B.2.13 and B.2.8 in an agency's voice, and the program concludes as this paper is written. (*Searched and verified against ARPA-E program pages and the FY2023 annual report.*)

**2025.** One flagged open item: a published report (Dubey et al. 2025) of experimental signatures indicative of a new d–d reaction channel at very low energy. Unreplicated; held as a claim, not a result; entered in Q, not in evidence. (*Searched; secondary citation only.*)

The Q-set of this paper, per P19 — open questions its own contents admit: the Dubey replication status; the ARPA-E final reports (due within months of this draft); the Z = 10 row and the (9, 7) hole (§3.7); the full-chart E(X) over Z ≤ 83 against AME/NUBASE evaluated files, which requires only network access and an afternoon; and the value-set repair of ℛ for sparse coordinates (§3.7), which is a question about the book's operator, not about nuclei.

---

## 8. What this paper does not claim

In the form of the book's Chapter 13 — stated limits, not modesty:

1. **No prediction.** E(Λ) = 0 and E-discipline carries over: nothing here proposes that cold fusion occurs, at any rate, under any condition. The paper's only universally quantified claims are the refusal (§2), the computed E = 9 with its stated dataset conditionality (§3), and arithmetic (§5.2).
2. **No mechanism.** The 10⁷ branching shift and the γ-suppression required by the historical claims are named as *what would need independent evidence*, and nothing here supplies or evaluates a mechanism for them.
3. **No likelihood shift.** The reduction changes the question's decidability, not its probability. Fifty orders of magnitude is the size of the claim after the reduction exactly as before it.
4. **The index supplies bookkeeping only.** Exit channels, Q-values, commensurability — structure. Rates are ⅅ_phys, and only the bench moves them.
5. **The computed E = 9 is a lower bound on a window**, conditional on the encoded dataset (§3.2), with two recorded operator limitations (§3.7). It is not the E of the full chart, which remains open in Q.

---

## 9. The register

Per B.2.12, everything corrected, declined, or degraded in the production of this paper, with what replaced it:

**R1 — correction (to the book).** §1.2's row "nuclide chart with drip lines, 383 cells, E = 0, self-defining" conflates two objects. Computed: the *measured* chart has E = 9 on Z ≤ 9 alone; the *drawn* (monotone-band) chart has E = 0 and is exactly ℛ(measured) — idempotence verified. Replacement: the row should name the band, and the difference between band and measurement should be recorded as content (pairing + clustering). *Caught by: computation.*

**R2 — commitment record.** Committed cells ⁵He, ⁸Be, ⁹B before computing; found nine holes including all three. The commitment held as a lower bound. Not a withdrawal; recorded because B.2.13 requires the outcome to be entered whether or not it embarrasses. *Caught by: n/a — honoured.*

**R3 — operator limitation.** ℛ on sparse value sets undercounts: ²⁸F and ³⁰F, physically exact analogues of the counted holes, escape via Â_N gaps at N = 19, 21. Replacement claim: E = 9 is a lower bound. *Caught by: reading the output against the physics (B.2.14 in reverse — the number was right and the first interpretation too strong).*

**R4 — provenance degradations.** (a) NUBASE2020 stability assignments recalled, not fetched; partially upgraded by literature search (F drip pattern, O drip line — verified; light proton-rich rows — textbook, unfetched). (b) Koonin–Nauenberg 3 × 10⁻⁶⁴ /pair/s recalled, unfetched. (c) 2019 *Nature* revisit and DOE reviews recalled, unfetched. Replacement: each flagged at point of use; none load-bearing for a universally quantified claim. *Caught by: B.2.11 applied at writing time.*

**R5 — decline.** The Z = 10 row, and with it the (9, 7)/¹⁶F hole, declined on data confidence; window cut at Z = 9. *Cause: encoding standard. Recorded per B.2.6.*

Five entries for one short paper. The book's register runs 297 for one long one, and the ratio is about right: the register is not an apology for the method — it is the method, applied to its own production, which is what Chapter 25 requires of any work that claims to comprehend the index.

---

## Appendix A — The computation

All results in §3 and §5 reproduce from the following, run under Python 3; outputs shown are verbatim from the working session.

**A.1 — E(X) of the measured chart, Z ≤ 9.**

```python
# E(X) per Method 1.2 §1.1, coordinates (Z,N), window Z<=9
# X = particle-bound ground states (NUBASE2020, recalled; F/O rows search-verified)
X = {
 1:{0,1,2},                                 # 1H 2H 3H ; 4-7H unbound
 2:{1,2,4,6},                               # 3,4,6,8He ; 5He,7He unbound
 3:{3,4,5,6,8},                             # 6-9Li,11Li ; 4,5,10Li unbound
 4:{3,5,6,7,8,10},                          # 7,9,10,11,12,14Be ; 6,8,13Be unbound
 5:{3,5,6,7,8,9,10,12,14},                  # 8,10-15,17,19B ; 7,9,16,18B unbound
 6:{3,4,5,6,7,8,9,10,11,12,13,14,16},       # 9-20,22C ; 8C,21C unbound
 7:{5,6,7,8,9,10,11,12,13,14,15,16},        # 12-23N ; 10,11N unbound
 8:{5,6,7,8,9,10,11,12,13,14,15,16},        # 13-24O ; 12O, 25-28O unbound
 9:{8,9,10,11,12,13,14,15,16,17,18,20,22},  # 17-27F,29F,31F ; 16,28,30F unbound
}
cells = {(z,n) for z,S in X.items() for n in S}
AZ = sorted({z for z,_ in cells}); AN = sorted({n for _,n in cells})
phiZN = lambda n: max((z for z,m in cells if m<=n), default=-1)  # max Z given N<=n
phiNZ = lambda z: max((m for y,m in cells if y<=z), default=-1)  # max N given Z<=z
R = {(z,n) for z in AZ for n in AN if z<=phiZN(n) and n<=phiNZ(z)}
```

Output: `|X| = 77  |R(X)| = 86  E(X) = 9`; value-set gaps `A_N: [19, 21]`; holes `(2,3) 5He, (2,5) 7He, (3,7) 10Li, (4,4) 8Be, (4,9) 13Be, (5,4) 9B, (5,11) 16B, (5,13) 18B, (6,15) 21C`; `X \ R = []`.

**A.2 — Idempotence and the drawn chart.**

Applying the same closure to ℛ(X): `|R(R(X))| = 86`, `R(R(X)) == R(X): True`, hence `E(drawn) = 0`, and `R(X) == X ∪ {nine holes}: True`.

**A.3 — Commensurability rates.**

```python
eV=1.602176634e-19
Q = {"d+d -> 3He + n":3.269, "d+d -> t + p":4.033, "d+d -> 4He + gamma":23.847}  # MeV
# per watt: rate = 1/(Q*1e6*eV)
```

Output: 1.91×10¹², 1.55×10¹², 2.62×10¹¹ events/s per W respectively; vacuum-branching neutrons 8.55×10¹¹ /s/W; ⁴He 2.26×10¹⁶ atoms/day/W = 3.76×10⁻⁸ mol/day/W; Koonin–Nauenberg baseline × 1 mol D = 9.0×10⁻⁴¹ fusions/s.

---

## Appendix B — The book's machinery used, indexed

Definitions carried over: **ℛ(X), E(X)** (§1.1); the running-maxima characterisation of ℛ-closure (§23.3); **ⅅ_def / ⅅ_phys** (Ch. 11); the E(X)-as-prediction-count identity (§18.6); the seven-index table including the nuclide-chart row (§1.2); the calendar reading of non-closure as purchase (§1.3).

Principles applied: **P3** (work backwards from desired output — §5.1); **P8** (any true answer is a bound — §2.6, §6.4); **P19/P7/P13** (the Q-set of §7); **P20** (the language bounds the question — §1); **P21** (model-vs-measurement verdict — §3.5); **P22** (closure absorbs invention — §2.5).

Protocols applied, with section of use: B.2.2 (§6.1), B.2.5 (§6, census), B.2.6 (§3.7, §6.3, R5), B.2.8 (§2, §5.4), B.2.9 (§1, §5.4), B.2.10 (§6.5), B.2.11 (§3.2, R4), B.2.12 (§9), B.2.13 (§3.3, §6.2), B.2.14 (throughout; every number preceded its sentence), B.2.15 (§2.6, §3.7, §6.4), B.2.16 and B.2.16.3 (§2.4, §5.1, §6.5).

Episodes cited as evidence: the Ch. 11 wrong-Z episode (§2.2); the P22 2S ≤ 2 absorption demonstration (§2.5); the 1,061-bounds-from-silence move (§6.4); the Ch. 25 requirement that a work comprehending the index register its own production (§9).

---

## Appendix C — The numbers, indexed

| number | what it is | origin |
|---|---|---|
| 0 | E(Λ) | book, verified over 475,800 pairs |
| 976 | \|Λ₈\| | book §2 |
| 36 / 7 / 0 | E of classroom table / calendar / Janet | book §1.1.1–1.3 |
| 383, E = 0 | book's §1.2 nuclide-chart row | book; corrected in referent, R1 |
| 77 / 86 / **9** | \|X\| / \|ℛ(X)\| / **E(measured chart, Z ≤ 9)** | this paper, A.1 |
| 86, E = 0 | the drawn chart = ℛ(measured) | this paper, A.2 |
| 8 of 9 | odd-N holes | this paper §3.6 |
| 17.59 / 3.269 / 4.033 / 23.847 MeV | Q-values (d+t; d+d three channels) | evaluated masses (recalled; flag) |
| 1.91×10¹² / 1.55×10¹² / 2.62×10¹¹ /s/W | mandatory event rates per watt | this paper, A.3 |
| 8.55×10¹¹ /s/W | vacuum-branching neutron rate per watt | this paper, A.3 |
| 3.76×10⁻⁸ mol/W·day | ⁴He commensurate with heat | this paper, A.3 |
| ~10⁻⁷ | vacuum γ branch of d+d | literature (recalled; flag) |
| ~10⁷ | branching shift required by historical claims | §5.3, arithmetic on the above |
| 3×10⁻⁶⁴ /pair/s | screened molecular D₂ rate | Koonin–Nauenberg 1989 (recalled; flag) |
| ~50 | orders of magnitude of claimed enhancement | arithmetic on the above |
| 5 | admissibility multiplier | book B.2.2, carried over |
| $10M / 8 teams / July 2026 | ARPA-E LENR Exploratory Topic | ARPA-E program pages, searched |
| 297 / 1,442 / 35 / 1,061 | book's register, cells, systems, bounds | book |
| 5 | this paper's register entries | §9 |

---

## References

1. M. Lach, *The Method* v1.2 — *The Lach Cylinder: an index of transitions — closure, self-reference, and the price of certainty* (companion volume; all §, P, and B.2 citations herein).
2. NUBASE2020 / AME2020 evaluations, Kondev, Wang, Huang, Naimi, Audi et al., *Chinese Physics C* 45 (2021) — stability assignments (recalled; verification per row noted in §3.2).
3. D.S. Ahn et al., first observation of ³¹F at the dripline and RIKEN BigRIPS dripline determinations (2019, 2022); J. Kahlbow et al. on ²⁸,³⁰F unbound (2024) — searched and cited via the surveyed literature.
4. S.E. Koonin, M. Nauenberg, "Calculated fusion rates in isotopic hydrogen molecules," *Nature* 339, 690 (1989) — screened D₂ rate (recalled; flag).
5. C. Berlinguette et al., "Revisiting the cold case of cold fusion," *Nature* 570, 45 (2019) (recalled; flag).
6. U.S. DOE cold fusion reviews, 1989 and 2004 (recalled; public documents).
7. ARPA-E, LENR workshop (2021), Exploratory Topic DE-FOA-0002784 (2022), eight-team award announcement (Feb 2023), FY2023 Annual Report to Congress (2025), project pages (end date July 2026) — searched.
8. Dubey, R., et al. (2025), reported low-energy d–d channel signatures — flagged open, unreplicated; secondary citation.

---

*Every claim in this paper is either computed in Appendix A, cited to the book by section, cited to the record with its provenance state, or entered in the register. The paper contains no prediction, and §18.6 of the book is the reason it cannot: it is offered as an index of a question, complete to the best of five audits, and standing — per P23 — only until the next question arrives.*