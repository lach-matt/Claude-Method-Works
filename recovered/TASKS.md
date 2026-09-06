# TASKS — The Method 1.4, reassessed

Register 582 → 584. Two items moved off the outside list by reassessment, and one claim of
impossibility was withdrawn.

---

# WHAT CHANGED IN THE REASSESSMENT

**A5 is settled and needs nothing.** §2.15.2 prints the derivation — *Γ-free ≠ reorderable* yielding
the upper bound *reorderable ⊊ totally balanced* — and **that inference only follows under the
permutation reading**. So the book means *admits a Γ-free ordering* throughout. Lubiw's thesis is not
needed. Register 555's flag withdrawn at 583.

**A1's impossibility proof was wrong.** 2,370 = 2·3·5·79 shows the cell set is not a **sub-box**, not
that implications cannot cut it. **Λ₈ is the counterexample: 976 = 2⁴·61 with 61 above every rung,
cut from a box of 6,912 by implications.** A1 is a search problem, not an impossibility — but the
search space includes disjunctions (T §8.2 prints one) and I have not characterised it.

---

# NEEDS OUTSIDE — genuinely, after reassessment

## 1 · The violation index's edge list or cells
**Closes `W.core9`, `W.core15`, `W.scale`, and `W.supp`'s failure count — four objects.**

**What.** Implications between axis values, including **disjunctive** ones. Printed instances:
`DNc = 2 → IC = 2` (from the withdrawals) and `NEC ≥ 3 → (IC ∨ U ∨ X)` (§8.2). Ten to forty lines.
**Or, better, the 2,370 cells: nine integers per row.**

**Where.** Transitions Appendix C states the computation scripts and cached datasets accompany the
paper. The list is a literal in whichever script printed the §5.6 threshold table. Grep for `2370`,
`DNc`, `NEC`.

**Acceptance test, stated by the companion itself and which I will run first:** 2,370 cells in a box
of 19,440 · E = 30 as 1 × 30 · core (X=0, U=0, NEC=3) · none of 414 subsets failing · multiplicities
3, 5, 10, 30.

## 2 · `B.hstar` — w(h) and V(h)
**One line. Closes one object.**

The minimisation condition αw′ + βV′ = 0 at h* is **one equation in two unknown functions** — the
mathematics here cannot recover them. I found that w = y″h²/2 with V logarithmic reproduces
√(2β/(αy″)) exactly, but by working backwards from the answer.

**If they are stated in Transitions Part XIII or an appendix, name the section and I will read it.**

## 3 · `T.scheme` — how the LS and jj brackets were derived
**One line. Closes one object.**

Not the looseness convention — register 541 shows it does not explain them. The brackets are 1.56 and
1.52 wide where the two candidate conventions differ by 3.18.

**What is needed:** the bounding argument giving [383,065, 597,325] for LS and [160,380, 244,060]
for jj.

## 4 · The species files
**Closes `B.adm`, Q item P, and replaces §24.8's caveat with a number.**

**Format:** NIST ASD levels output with delimiters intact — `1234.567` optimised from measured lines,
`[1234.567]` interpolated or Ritz-fitted, `(1234.567)` ab initio. **Keep the header block**; it
carries the *Primary data source* note, which classed four species without a cell being counted.

**Fastest route:** `data.nublado.org/nist/asd_v5.12/levels/asd.ZZZCCC` — ZZZ atomic number in three
digits, CCC ionisation stage from 000. **Ne I `asd.010000` · K I `asd.019000` · Al I `asd.013000`.**

**Otherwise:** `physics.nist.gov/PhysRefData/ASD/levels_form.html`, tick *Level Uncertainty* and
*Bibliographic references*, ASCII output.

**If only three, those three** — 330 cells, and with He I and H I already read it passes a third of
the 1,442.

## 5 · The Dunz scan, if it exists
**Would settle a contradiction the book carries.**

§19.5 lists Dunz 1911 as **not retrieved**; the References say **retrieved as a scan, unread**. One
is false. **If you have the scan, this stops being a retrieval problem.**

Four routes are empty — primary, review, citing, deposit — and two signals stand against the
citation: it reads *Dunz, —*, an em-dash where an initial belongs, and it places a series-laws
dissertation at **Leipzig**, outside the Tübingen lineage of every other early dissertation in this
literature. The register that would settle it is the *Jahresverzeichnis der deutschen
Hochschulschriften*, unreachable from here.

---

# MINE — I need nothing to do these

| | task | what it is |
|---|---|---|
| **M1** | Ritz's Œuvres, pp. ~142–150 | **one fetch.** Gallica `ark:/12148/bpt6k33824`, full text. Settles §29.5's question about the *further particulars* footnote |
| **M2** | Q item G, properly | **a search.** G asks whether deciding *reorderability* is in P — not the seed's NP-hardness, which I closed it on wrongly. Probably merges with F |
| **M3** | Q item D, Kreuzer–Skarke | **a fetch.** The Hodge pairs are a published database |
| **M4** | Q item C, nine literatures | **nine searches**, each in the index that literature holds |
| **M5** | Q item H, Sc VI measured? | **one lookup** in the ASD bibliographic database |
| **M6** | Q item R, \|Cl(ℛ)\| for Λ | **a computation**, unbounded — #P-complete in general (Kuznetsov) |
| **M7** | A1's search space | **a calculation.** Characterise the disjunctive candidate space before asking again; a proper search might make item 1 unnecessary |

---

# NEEDS NEITHER OF US

**Q item A** — the Sc VI level, measured. Graded *nonexistent*. A spectrometer or nothing.

**`M.C2`** — half-sided modular inclusion on isolated horizons. **Correctly open, interval named on
both sides**: established for Killing horizons in arbitrary interacting QFT, and in January 2026 for
linearised perturbations of them. Open for non-expanding horizons that are not such perturbations —
and their eq. (1.7b) shows the blocking term carries a factor of the expansion, so it vanishes there.

---

# SUMMARY

| | before | **after reassessment** |
|---|---|---|
| needs outside | 5 | **5** — but one is now conditional (the Dunz scan) and one is a search problem rather than an impossibility |
| mine | 7 | **7**, plus M7 which may remove item 1 |
| needs neither | 3 | **2** — A5 resolved by reading |

**Cheapest real gains: items 2 and 3 — one line each, one object each.**
**Largest: item 1 — four objects.**
**Try M7 before item 1**: if the disjunctive search finds a candidate that passes all five printed
figures, the file is not needed.