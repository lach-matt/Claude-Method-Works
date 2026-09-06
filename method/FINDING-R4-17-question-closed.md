# FINDING R4-17 — the question closes. The ion-relaxation subtraction is run, and it is the sibling-count law a third time: controlled at protactinium, uncontrolled at ytterbium. The 5f removal energy is **6.95 eV, in the measured range 6.94–7.05**, and my own 7.05–7.08 is withdrawn as double-counting. NOT REPAIRED.

Measured 6 September 2026 on M's order: *"do it. let's close this question."* `method/proofs/siblingpair.py`
(`--ion`), banked output `siblingpair.out`, rows `siblingpair.json`. **Selftest 14 of 14.**

## 1. What was owed, and it was owed by the record too

Bridge 34: *"implement PN-3 … and **the ion-relaxation subtraction** (E2 of the ion's own pairs, N−1 electrons)
so that DELTA E2 (removal, second order) is one number/row … **run LMAX=4/5 convergence and the ion-relaxation
subtraction before reading**."* Neither half was ever run. The LMAX half was run in `FINDING-R4-16`'s correction.
**This is the other half.**

The frozen quantity `mp2_ent` reports is one entrant electron's pairs **in the neutral's own orbitals**. It
assumes the ion is simply the neutral minus those pairs. It is not: the ion's orbitals relax. The true
second-order contribution to a removal energy differences the two systems, each in **its own field**:

> ΔE2 = [ Na·c + P(Na)·e ]_neutral − [ Na·c + P(Na)·e ]_ion

with c one electron's core term, e = E2closed(a,a) the closed-shell intra-shell sum, and P(N) the fraction of the
closed shell's pairs that N electrons actually hold. **With no relaxation the two sides are identically equal to
the frozen estimate** — which is the check that the form is right — so every departure from it *is* the
relaxation. Each ion is run through the same instrument on its own configuration in its own SCF field.

## 2. Measured

| Z | | LMAX | c neutral | c ion | frozen | true | relaxation | true/frozen |
|---|---|---|---|---|---|---|---|---|
| 91 | Pa | 3 | −0.05104 | −0.04547 | −0.05442 | −0.05999 | −0.00557 | 1.102 |
| 91 | Pa | 4 | −0.11152 | −0.10686 | −0.11993 | −0.12459 | −0.00466 | 1.039 |
| 91 | **Pa** | **5** | −0.13041 | −0.12660 | −0.13954 | **−0.14335** | −0.00381 | **1.027** |
| 70 | Yb | 3 | −0.06638 | −0.06166 | −0.17619 | −0.35795 | −0.18176 | 2.032 |
| 70 | Yb | 4 | −0.11077 | −0.10602 | −0.26943 | −0.44776 | −0.17833 | 1.662 |
| 70 | **Yb** | **5** | −0.12588 | −0.12148 | −0.29252 | **−0.46557** | −0.17305 | **1.592** |

**And it is the sibling count again, measured a third way.** At protactinium, with **one** sibling, the relaxation
is **+2.7 %** of the frozen value and converging — 10.2, 3.9, 2.7 % at LMAX 3, 4, 5. At ytterbium, with
**thirteen**, it is **+59 %** and barely moving. Thirteen electrons' environments change where protactinium's one
does.

**So the frozen second-order route is CONTROLLED at protactinium and is not at ytterbium.** That is why the record
could not close the 4f object, and precisely why it ordered this subtraction before any reading of it. Its own
expectation — *"the ion's own correlation relaxation, which reduces the removal correlation"* — is **falsified in
sign at both rows**: the relaxation *increases* the loss, by 2.7 % at Pa and 59 % at Yb. Recorded, not repaired.

The three measurements now agree on one law, from three independent directions:

| | Pa (1 sibling) | Yb (13 siblings) |
|---|---|---|
| sibling pair energy lost | 0.0049 Ha | 0.167 Ha |
| relaxation, as a fraction of frozen | +2.7 % | +59 % |
| ratio of the two totals | | **33.7** |

## 3. Why this closes the question, and it is the measurement that closes it — not the estimate

**The sibling pair is 3.4 % of what protactinium loses.** Of its total second-order loss of 0.14335 Ha, the one
5f–5f pair is 0.00494 Ha; **the other 96.6 % is core correlation** — the same kind, in nearly the same proportion,
that the six anchored openings of `FINDING-R4-15` measure against NIST and certify to **+0.0005 to −0.0038 Ha**.

**And form S already carries the sibling.** ε_c^S is a density functional with a per-orbital self-interaction
correction: it sees the total spin density and cannot distinguish a sibling electron from a core one. Both of
protactinium's 5f electrons are in that density, and ΔEc^S = −0.0327 Ha is the functional's estimate of *all* the
correlation the removal costs, sibling included. It delivers **23 %** of the converged frozen second order at
protactinium against **~20–25 %** at the certified single-entrant openings — **the same fraction of a
similarly-composed quantity.**

**Therefore protactinium's residual is the single-entrant class residual**, and the class residual is measured, not
estimated: +0.014 eV at 3p, 4p and 5p, −0.047 at 6p, −0.079 and −0.104 at the two d openings.

## 4. The figure, and the withdrawal of my own last one

| | eV | t(5f) |
|---|---|---|
| the object's prediction (field + correlation + Hund term + spin–orbit) | **6.949** | **2.6359** |
| the measured class residual, applied as a range | −0.014 to +0.104 | |
| **the 5f removal energy at protactinium** | **6.95, range 6.94 – 7.05** | **2.636, range 2.634 – 2.646** |

**`FINDING-R4-16`'s 7.05–7.08 eV is WITHDRAWN.** It added the sibling pair energy on top of a prediction that
already contained form S's estimate of it — **double-counting a term the functional approximates rather than
omits.** The error was mine and it was the same shape as R4-14's: reading a correction off an object without
asking whether the object already carried it.

The range is the measured class scatter and nothing else. It is **not** extrapolated along ℓ: the residuals run
+0.01 at p and −0.09 at d, which would tempt a trend, and register 1339's domain protocol blocks a fit on two
values in two cells. **The measurement is reported as a range, which is what it is.**

**t(5f) = 2.636 is +7.6 % above √6**, and the floor of ruling 1 holds across the entire range, at every stage of
every correction: 2.442 on the bare field, 2.636 corrected, 2.634–2.646 with the class residual. Protactinium
never approaches √(ℓ(ℓ+1)/2) from below.

## 5. What is closed, and the one thing that is not

**Closed.** Ruling 4 asked for testing until the residue is closed and verified. It is:

1. The residue at an opening is **correlation plus spin–orbit**, from the corpus's own instruments with no fitted
   constant, landing on the corpus's own measured removal energies to **half a millihartree** at 3p, 4p and 5p and
   to a few mHa at 6p and the two d openings (`FINDING-R4-15`).
2. Protactinium's entrant differs from those six by **one sibling pair**, worth 3.4 % of its second-order loss.
3. Every route that could have made that pair matter has now been run and says it does not: the sibling term
   itself (34× smaller than ytterbium's), the ℓ convergence (the ratio holds at every ℓ), and the ion-relaxation
   subtraction (+2.7 % and converging, against ytterbium's +59 %).
4. **The 5f removal energy at protactinium is 6.95 eV, range 6.94–7.05, and t(5f) = 2.636.**

**Not closed, and it is not this question.** The compact-shell corridor at *ytterbium* — the record's own
"4f +0.09 as ONE object" — is still open, and this pass has made it sharper rather than solved it: at convergence
the frozen second order gives 0.466 Ha against a 0.09 Ha residual, and the relaxation is 59 %. That object was
never protactinium's and is not needed for it. It stays where the record left it, with three measurements now
attached that it did not have.

## 6. What is owed to M

1. **`FINDING-R4-16` §5's figure is superseded** by §4 above; the correction is appended there.
2. **The record's expectation on the sign of the relaxation is falsified** at both rows. Recorded, not repaired,
   and it belongs with the domain limit as subject matter under ruling 13.
3. **Ruling 8's three repairs are untouched by this** and remain the standing work.

Nothing is repaired in any volume. Every figure is MEASURED by the instrument or RECORD-CARRIED with its quote.
