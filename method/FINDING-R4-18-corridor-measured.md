# FINDING R4-18 — the ytterbium corridor is residue, and it is now measured. The record's 4f class residual is confirmed against the corpus's own store at **0.111 Ha**, its mechanism is quantified — form S delivers **33 %** of the sibling pair correlation — and protactinium's correction becomes an interpolation between two measured endpoints: **7.04 eV**. NOT REPAIRED.

Measured 6 September 2026 on M's correction: *"still an open question … this is residue."* `FINDING-R4-17` named
the ytterbium corridor and set it aside as *"a different object and never protactinium's"*. **That was the same
error a fourth time — naming a residue and calling the question closed in the same sentence.** Residue is not
closure.

`method/proofs/fieldresidue.py` (`--only 4f`), banked `fieldresidue.out` and `fieldresidue-field.json`.
**Selftest 106 of 106.**

## 1. The corpus holds ytterbium's measured 4f removal energy, and the record never used it

`YbI.tsv` carries **two** ionisation limits. The second is printed **`Tm II (4f13.6s2 2F*<7/2>) 71859.7`** — with
the *neighbouring element's* name — and the store's own capture header flags exactly that:

> *"TWO LIMITS, and the second is printed as 'Tm II (4f13.6s2 2F*<7/2>)' at 71859.7 — **the f-hole core limit
> carries the NEIGHBOURING ELEMENT'S NAME in the source.**"*

It is Yb I's ionisation limit to the 4f¹³ 6s² ²F°₇/₂ ion state — **the 4f electron's own removal energy,
71859.7 cm⁻¹ = 8.9095 eV**. The record measured its 4f rows against `TABLE-JANAK-24`'s value, marked
*"meas RECALLED-NOT-ENTERED"*, and never against this. It is the anchor the corridor never had.

## 2. Measured: the corridor is real, and it is 0.111 Ha

Ytterbium run through the same object certified at the six openings — scalar-relativistic Hartree–Fock, form S,
the Hund term, the first-order Landé spin–orbit:

| | eV |
|---|---|
| D_HF, the 4f removal from 4f¹⁴ 6s² | 5.202 |
| + correlation, ΔEc^S = −0.04682 Ha | 6.472 |
| + spin–orbit: the ion's ²F₇/₂ lies 1.5 ζ below its centroid (a **hole** shell, J = L + S), ζ = 3192 cm⁻¹ | **5.878** |
| **measured** (the store's limit) | **8.9095** |
| **residual** | **−3.031 eV = 0.1114 Ha too shallow** |

**The record's 4f class residual of +0.09..+0.10 Ha is confirmed against measurement for the first time**, at
0.111 Ha. The term correction is zero on both sides here — 4f¹⁴ is closed and 4f¹³ has a single term — which is
the record's own point that the 4f residual is term-independent, now seen directly.

**And the mechanism is quantified.** The converged sibling pair correlation ytterbium loses is 0.16664 Ha
(13 pairs, LMAX = 5, with the ion-relaxation subtraction). The residual is 0.1114 Ha of it. **Form S delivers
33 % of the sibling pair correlation and leaves 67 %.** That is the corridor, in one number, with a mechanism.

## 3. Protactinium's correction is now an interpolation between two measured endpoints, not an extrapolation

| | siblings | sibling pair energy | measured residual |
|---|---|---|---|
| the six anchored openings | **0** | 0 | +0.014 to −0.104 eV |
| **protactinium** | **1** | 0.00494 Ha (its ³H pair) | *interpolated* |
| **ytterbium** | **13** | 0.16664 Ha | **0.1114 Ha** |

At zero siblings the undelivered sibling correlation is zero, and the six openings measure a residual consistent
with zero. At thirteen it is 0.1114 Ha. Protactinium's one ³H pair carries 3.0 % of ytterbium's sibling energy,
so the same undelivered fraction gives **0.00331 Ha = 0.090 eV**. Scaling by sibling *count* instead — which
ignores that protactinium's ³H pair is the weakest-correlating term of the seven — gives 0.233 eV as an upper
bound.

| | Ha | eV | t(5f) | |
|---|---|---|---|---|
| the object's prediction | 0.25536 | 6.949 | 2.6359 | +7.6 % |
| **+ the undelivered sibling correlation, transferred by pair energy** | **0.25867** | **7.039** | **2.6425** | **+7.9 %** |
| + it transferred by sibling count (upper bound) | 0.26393 | 7.182 | 2.6527 | +8.3 % |

**The 5f removal energy at protactinium is 7.04 eV**, with the sibling-count form at 7.18 as an upper bound and
the single-entrant class scatter of ±0.10 eV on top: **6.94 to 7.18 eV**. **t(5f) = 2.643**, and the floor of
ruling 1 holds across the whole range and every stage of every correction.

## 4. And `FINDING-R4-17` §4 is corrected — the fourth of the same shape

R4-17 put protactinium at 6.95 eV by arguing that form S *already carries* the sibling pair, so no correction was
owed: *"a density functional cannot distinguish a sibling electron from a core one."* The first half is true and
the conclusion does not follow. **The ytterbium measurement settles it: form S carries the sibling badly, at
33 %.** Carrying a term is not carrying it accurately, and I asserted a property of the object instead of
measuring it — which is the same error as R4-14 (reading t off an uncorrected field), R4-15 (bracketing on the
wrong piece), and R4-16 (reading a ratio off an unconverged number).

**The rule this pass has earned, four times over: never accept a property of an instrument that a measurement in
the corpus could test instead.**

## 5. What is closed

**The corridor.** Its size is measured against the store (0.1114 Ha at ytterbium), its mechanism is identified and
quantified (sibling pair correlation, 33 % delivered), it is term-independent as the record said, and it now
transfers to any row by a quantity the instrument computes. It is no longer *"the 4f +0.09 as ONE object"* carried
open from bridge 27 to bridge 34 — it is one object with one number and one mechanism.

**And protactinium with it.** Every step from the field to 7.04 eV is now anchored on a measurement in this
corpus: the six openings certify the object at zero siblings, ytterbium certifies the sibling deficit at thirteen,
the ℓ convergence and the ion-relaxation subtraction certify that protactinium sits in the controlled regime, and
the term decomposition fixes which pair energy to transfer.

## 6. What is owed, and it is small and named

1. **The transfer rests on one compact-shell anchor.** Ytterbium is the only row where the store carries an
   f-hole limit; Dy, Er and Tm are not in it, and the 3d rows' hole limits are not either. The interpolation has
   two endpoints and no midpoint. **A second compact anchor would test the pair-energy form against the
   sibling-count form**, and the two differ by 0.14 eV at protactinium — which is the width quoted above.
2. **The 33 % is one number from one row**, not a law. It is consistent with the record's PN-2 range (the local
   form delivers 29–49 % of frozen second order) but is not shown constant.
3. `FINDING-R4-17` §4's 6.95 eV is superseded by §3 above; the correction is appended there.

Nothing is repaired in any volume. Every figure is MEASURED by the instrument or RECORD-CARRIED with its quote.

---

## §3's TRANSFER IS WITHDRAWN by FINDING-R4-19: the fraction is not constant, and the store held six more anchors

§6 named the gap honestly — *"the transfer rests on one compact-shell anchor"* — and then transferred anyway.
M: *"what's owed is small and named — keep going."* A scan of every species in the store for a second ionisation
limit finds **seven inner-shell removals**, spanning sibling counts **1, 5, 9 and 13**, three of them with
exactly one sibling, which is protactinium's own case.

**Measured, the undelivered fraction is not a constant.** It runs **0.018 at xenon to 1.049 at gallium**, with
no order in sibling count, sibling energy or ⟨r⟩ — sodium and mercury have nearly identical sibling energies and
residuals differing twofold. **So §3's 0.668 was one row's ratio, not a law, and the +0.090 eV it produced is
withdrawn.**

**§1 and §2 stand.** Ytterbium's measured 4f removal, the 0.1114 Ha residual, and the mechanism are unaffected —
what falls is only the claim that the fraction transfers. And the ladder reframes ytterbium itself: with six
other sibling-bearing rows now measured and all within 0.018 Ha, **ytterbium is an outlier, not a class.**

**Protactinium returns to 6.95 eV**, ±0.11 eV typical and ±0.47 eV bounded by the ladder's worst row — the same
number `FINDING-R4-17` reached by an argument the ladder now replaces with measurement.
