# FINDING R4-16 — ruling 4 discharged. The 5f bracket at protactinium was the wrong object; the record had already measured the right one, named its mechanism and built its instrument. The 4f class residual does not transfer to protactinium, on both of the record's own readings, and the figure narrows from 5.849–6.949 eV to **7.04–7.18 eV**. NOT REPAIRED.

Measured 6 September 2026 under `RULINGS-R4f` ruling 4 — *"this is an open question. so we test and test,
nothing is accepted without evidence and verification of complete residue closure"* — and under M's correction of
method: *"there is a reason one of my directives is to read everything before doing anything … most if not
everything can be answered by the contents of the repo."*

`method/proofs/siblingpair.py`, banked output `siblingpair.out`, rows `siblingpair.json`. **Selftest 14 of 14.**

## 1. The bracket R4-15 offered was the wrong object, and the record says so

R4-15 bracketed protactinium's 5f removal at 5.849–6.949 eV, the width being whether the Hund term correction is
applied, and called that term *"the one piece no anchored opening tests."* **Both halves of that are wrong, and
the record had already settled them at sessions 24–27.**

**The term is not the open piece.** `FINDING-HFTERM-SESSION-27`, on the four 4f rows: *"Yb 4f14 → 4f13 (2F) HAS NO
TERM CORRECTION and shows the same +0.093: the 4f residual is not term-average error at all. With the term
resolved, the four 4f rows collapse to ONE number, +0.09..+0.10 Ha too shallow — a systematic 4f under-binding of
exact exchange + first-order local correlation, **term-independent**, that the term correction merely uncovers."*

**And what is open is a class, not a row.** The same finding: *"On single-entrant s/d rows: exact exchange +
first-order chain correlation closes to ≤ 0.009. On compact multi-electron shells, term-resolved exact exchange
and the SAME correlation leaves +0.02..+0.07 (3d) and +0.09..+0.10 (4f) … the two derived objects bracket the
measurement from opposite sides on every compact row; the bracket is a two-sided corridor and per M's ruling does
not close."* And `FINDING-OWNSHELL-JANAK-SESSION-24`: *"the residual is ONE monotone function of the entrant's
compactness — 6s −0.002 · 4d/5d −0.008..−0.012 · 3d −0.019..−0.044 · 4f −0.039..−0.052 — plus Dy at −0.090."*

**So R4-15's six anchored openings were never able to speak for protactinium** — every one of them is a *single*
entrant electron, the class that closes to ≤ 0.009 Ha. What they do establish is a confirmation: their residuals
are **+0.0005, +0.0005, +0.0005, −0.0017, −0.0038, −0.0029 Ha**, all inside the record's own single-entrant bound
and most of them far inside it, on **four openings the record never ran** (3p, 4p, 5p, 6p). That stands.

## 2. The record named the mechanism and built the instrument

`FINDING-MP2ENT-SESSION-34`, prediction PN-4, held: *"Yb: sibling term 0.112 of 0.179 (63 %). The 4f +0.09
shortfall's candidate is the same-shell pair correlation the SIC-corrected local form handles as self-correlation
subtraction while the 13-sibling correlation is real: horizon item (3) now has a derivable object and a number to
test against (0.09 vs 0.11 lower-bound frozen second order, before the ion's relaxation is subtracted)."*

The missing quantity is the **second-order pair correlation between the entrant and its siblings in the same
shell**, which a removal destroys and which Hartree–Fock with a local first-order correlation term cannot carry.
`recovered/mp2_ent.py` computes it. This instrument runs that file — not a reimplementation — with one declared
departure: r_min restored from 1e-5/Z to **1e-3/Z**, which is the record's own repair, stated in the finding's
numerics and recorded as F34.4 (*"generalized eigh and tridiagonal select both lose the valence eigenvalues to
conditioning on Z ≥ 55"*); the recovered text predates its own fix.

**Four of four of the record's rows reproduce:**

| | E2_ent here | record | core | record | sibling | record |
|---|---|---|---|---|---|---|
| He 1s², k ≤ 3 | **−0.04903** | −0.0490 | | | | |
| Sc 3d | **−0.06523** | −0.0652 | −0.06523 | | 0 | |
| Cs 6s | **−0.02393** | −0.0240 | −0.02393 | | 0 | |
| Yb 4f | **−0.17619** | −0.1786 | −0.06638 | −0.0667 | **−0.10981** | −0.1119 |

PN-4 reproduced: ytterbium's sibling term is **62 %** of its entrant correlation against the record's 63 %.

## 3. A domain limit of the recovered instrument, first exposed at protactinium

`mp2_ent.py` takes the entrant's sibling share as `sib = (2/Na)·E2closed(a,a)`, where `E2closed` is the
intra-shell pair correlation of the shell treated as **closed**. That is right exactly when `Na` is the *full*
occupancy: a closed shell of N electrons holds N(N−1)/2 pairs, the entrant is in N−1 of them, so its share is
2/N. **Every row the record ran satisfies it** — He 2 of 2, Yb 14 of 14, and Sc, Cs, Y, La, Gd, Lu at Na = 1 where
the term is zero. For a **partly filled** shell the entrant has Na−1 siblings, not N−1, and the share is

> **sib = 2(Na − 1) / (N(N − 1)) · E2closed(a,a)**

which is identically (2/Na)·E2closed when Na = N, and zero when Na = 1. **It agrees with the recovered formula at
every banked row and differs only where the record never went.** Protactinium's 5f² is the first such row, and
there the recovered formula counts **91 pairs where the atom has one** — a factor of exactly 14·13/2, asserted in
the selftest. This is the instrument's domain, stated; it touches none of the record's published numbers.

## 4. Measured: the 4f class residual does not transfer to protactinium

| | Na / N | E2_ent | core | sibling | ⟨r⟩ (a₀) |
|---|---|---|---|---|---|
| Yb 4f | 14 / 14 | −0.1762 | −0.0664 | **−0.1098** | 0.760 |
| Pa 5f | **2 / 14** | −0.0544 | −0.0510 | **−0.00338** | **1.421** |

**By sibling count — the mechanism PN-4 names.** Ytterbium's 4f¹⁴ → 4f¹³ loses thirteen sibling pairs, 0.1098 Ha,
or 0.00845 Ha each. Protactinium's 5f² → 5f¹ loses **one**: 0.00338 Ha on its own orbital, or 0.00845 Ha if a 5f
pair correlated like an Yb 4f pair. Against the class residual of +0.09..+0.10 Ha, that is **smaller by a factor
of twenty to thirty.**

**By compactness — the variable of the Janak class law.** ⟨r⟩ is 0.760 a₀ for ytterbium's 4f and **1.421 a₀** for
protactinium's 5f. Protactinium's entrant is nearly twice as diffuse, and sits with the 5d rows the record
measured at −0.008..−0.012 Ha, not with the 4f rows at −0.039..−0.052.

**The two readings agree, which is what makes this a finding rather than a preference.** The record left "the 4f
+0.09 as ONE object" open from bridge 27 through bridge 34 precisely because compactness and sibling count could
not be separated on its own rows — every compact row it ran was also sibling-rich. **Protactinium separates them:
it is compact and sibling-poor, and both readings put it outside the 4f class.**

## 5. The figure

| | Ha | eV |
|---|---|---|
| R4-15's predicted removal (field + correlation + term + spin–orbit) | +0.25536 | 6.949 |
| missing sibling correlation, own orbital → Yb-like pair | +0.00338 → +0.00845 | +0.092 → +0.230 |
| **corrected 5f removal at protactinium** | **+0.25874 → +0.26381** | **7.041 → 7.179** |

**t(5f) = 2.6426 to 2.6524, which is +7.9 % to +8.3 % above √6.**

The bracket narrows from **1.10 eV wide to 0.14 eV**, and its remaining uncertainty is no longer a guess: it is
the single-entrant class scatter measured at the six anchored openings, +0.014 to −0.104 eV, plus the record's own
two cautions on this object — frozen second order on local orbitals **overestimates** (He ×1.3), and the ion's own
correlation relaxation, which reduces the removal correlation, is **absent**. Both push the same way, so 7.04 eV
is the better-supported end.

**Ruling 1 is untouched and strengthened.** t at 5f is above √(ℓ(ℓ+1)/2) at every reading — 2.442 on the bare
field, 2.636 corrected, 2.643–2.652 with the sibling term. The form is a floor and protactinium does not
approach it from below at any stage of the correction.

## 6. What is still not closed, stated exactly

**The compact-shell corridor itself remains open**, exactly as the record left it. This finding does not close it;
it establishes that protactinium is **not in it**. The record's own next test — *"the 4f +0.09 via Yb: sibling
second-order term (2/14)E2(4f,4f) = 0.112 lower bound at l ≤ 3 … run LMAX=4/5 convergence and the ion-relaxation
subtraction before reading"* (bridge 34) — was never run, and is not run here.

**One reconstruction discrepancy is recorded, not repaired.** The box eigenvalue reproduces the SCF to 2 × 10⁻⁵
at scandium and 1.8 × 10⁻⁴ at caesium, both inside the record's stated ≤ 2 × 10⁻⁴, but to **9.5 × 10⁻⁴ at
ytterbium**, about five times outside it — and the ytterbium E2_ent that rides on it comes out +0.0024 Ha shallow.
Under G0c the finding is about the reconstruction, and its likely seat is the seed repair `fieldentry.py`
declares, which the sealed runtime did not need. It does not reach protactinium's sibling term, which is a ratio
of two quantities from the same run.

## 7. What is owed to M

1. **R4-15 §5's bracket is superseded** by §5 above, and its reasoning — that the term correction is the untested
   piece — is withdrawn. The correction is appended to that file.
2. **The single-entrant class bound now has four p openings in it** that the record never ran. Whether that
   confirmation belongs in a volume is M's, under ruling 5.
3. **The domain limit of `mp2_ent.py`'s sibling formula** is recorded here. It changes none of the record's
   numbers and is not a repair to any seated file.

Nothing is repaired in any volume. Every figure is MEASURED by the instrument or RECORD-CARRIED with its quote.
