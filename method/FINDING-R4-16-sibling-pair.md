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

---

## §4's COMPACTNESS ARGUMENT IS CORRECTED, and the record's own second-order numbers are found unconverged

M, on this file: *"the domain limit is information that needs to be included in the volumes, but over all, it is
still an open question. we are not finished."* Bridge 34's other instruction — *"run LMAX=4/5 convergence and the
ion-relaxation subtraction before reading"* — was never run by the record. **Half of it is now run**, and it
changes two things.

### The record's banked second-order values are unconverged in ℓ

| LMAX | Pa E2closed(aa) | Yb E2closed(aa) | Yb sibling term |
|---|---|---|---|
| **3** (the record's) | −0.30782 | −0.76866 | **0.10981** |
| 4 | −0.76551 | −1.11060 | 0.15866 |
| **5** | **−0.83041** | **−1.16650** | **0.16664** |

**Ytterbium's sibling term runs 0.110 → 0.159 → 0.167**, and protactinium's closed-shell sum nearly triples. The
record banked LMAX = 3 and read PN-4 off it as *"0.09 vs 0.11 lower-bound frozen second order"*. **At convergence
it is 0.09 against 0.167** — the frozen second-order estimate overshoots the residual it was tested against by
**85 %, not 22 %.** So the record's own two cautions — frozen second order overestimates (He ×1.3) and the ion's
relaxation is absent — must carry about **half** the value rather than a fifth of it. This does not refute PN-4;
it makes its own caveats load-bearing, which is why bridge 34 ordered the convergence before reading.

### §4's compactness half was read off an unconverged number and is withdrawn

The per-pair ratio Pa/Yb runs **0.400 → 0.689 → 0.712**. At convergence protactinium's 5f pair correlates
**within 30 %** of an ytterbium 4f pair, not at two-fifths of it. The ⟨r⟩ measurement (1.421 a₀ against 0.760)
stands as a measurement, but its consequence for the pair energy is far weaker than §4 claimed, and the claim
that Pa "sits with the 5d rows" on the Janak law is not supported by this object.

**What survives is the sibling count, and it survives because it is exact arithmetic rather than a computed
quantity: protactinium loses ONE pair where ytterbium loses THIRTEEN.** The ratio of the two totals is **33.7**
at convergence and was 50.4 at LMAX = 3 — the conclusion is the same at every ℓ and does not depend on the
convergence at all. §4's finding therefore stands on one leg instead of two, and it is the stronger leg.

### And the term decomposition, which is new and makes the average the wrong quantity

The seven allowed terms of f² carry statistical weights summing to **91** — which is exactly the pair count of a
closed f¹⁴ shell — so the closed-shell sum is literally a sum over terms, and the per-pair energy in a term is its
contribution divided by its weight. At Pa, LMAX = 5:

| term | ¹S | ³P | ¹D | ³F | ¹G | **³H** | ¹I |
|---|---|---|---|---|---|---|---|
| per pair / average | 5.00 | 1.86 | 1.74 | 0.89 | 1.02 | **0.54** | 1.14 |

**Protactinium's two 5f electrons sit in ³H** — Pa I's ground is ⁴K11/2 = 5f²(³H) + 6d — which is maximum
multiplicity and maximum L, where Hund's rules hold the two electrons furthest apart, and **it is the
weakest-correlating of the seven terms**, at 0.54 of the average against 5.0 for the ¹S singlet. The same shape
appears at ytterbium (³H at 0.60), so it is a property of the f² term structure and not of the element. **The
closed-shell average is therefore the wrong quantity for protactinium and the term-resolved one is right.**

### Where the figure stands, and it is not closed

Protactinium's actual ³H sibling pair, converged: **0.00494 Ha = 0.135 eV**; with the record's own ×1.3 frozen
overestimate removed, 0.00380 Ha = 0.103 eV.

| | Ha | eV | t(5f) |
|---|---|---|---|
| unrelaxed | 0.26030 | **7.083** | 2.6457 (+8.0 %) |
| ÷1.3 | 0.25916 | **7.052** | 2.6434 (+7.9 %) |

So the figure has settled at **7.05–7.08 eV**, inside but at the bottom of §5's 7.04–7.18, with t(5f) = 2.643–2.646.

**It is not closed, and the reason is named: the ion-relaxation subtraction — the other half of bridge 34's
instruction — is still not run**, here or in the record. It can only move the figure down. Until it is run the
7.05–7.08 eV is a one-sided estimate, and the single-entrant class scatter of ±0.1 eV sits on top of it.
