# FINDING R4-21 — ruling 8(b) worked, bounded and **not repaired**, with the reason named. The corpus holds three spin–orbit forms and none fixes the pattern; the fault is not the operator; and **no figure in this pass depends on it** — with the store's own measured ζ substituted at all six anchored rows the object still closes to 0.0042 Ha, and protactinium moves under 0.02 eV across the entire error range those rows allow. NOT REPAIRED.

Measured 6 September 2026 on M's ruling 8: *"they are all work. they must be repaired, worked, and then
verified/proven completely."* Item (b) was *"first-order Landé ζ is 9 % low at p and 36 % high at 5d against the
store's measured intervals — repair the spin–orbit term."*

`method/proofs/soterm.py` (new), banked `soterm.json`. **Selftest 17 of 17**, including the gate that its ζ
reproduces `fieldresidue`'s banked value at all six rows to 10⁻⁹.

## 1. The corpus holds three forms, and had never put them side by side

| | |
|---|---|
| **so94 primary** — what `fieldresidue` uses | ζ = (1/2c²)⟨P\|(1/r) dV_loc/dr\|P⟩, V_loc with the entrant's own shell at Q−1 and its same-shell exchange |
| **so94 sensitivity** | the same on V_loc + X/P, the Slater-local projection of the nonlocal exchange — built, declared *"SENSITIVITY ONLY"*, never scored |
| **so97**, a *later* session, written for this same field | ξ = (1/2c²)⟨P\|(1/(r M²)) dV_dir/dr\|P⟩, M = 1 + (ε−V)/2c² — Koelling–Harmon |

**so97 differs from so94 in two ways at once** — the potential *and* the mass factor — and no record separates
them. This instrument computes all four combinations, so which difference does the work is measured.

## 2. Measured against the store's six intervals: **no form fixes the pattern**

Ratio computed / measured:

| row | so94 primary | so94 + exchange | the potential alone | the KH factor alone | so97 verbatim |
|---|---|---|---|---|---|
| 3p Al | **0.910** | 0.893 | 0.908 | 0.903 | 0.902 |
| 4p Ga | **0.914** | 0.908 | 0.914 | 0.873 | 0.872 |
| 5p In | **0.955** | 0.951 | 0.955 | 0.845 | 0.845 |
| 6p Tl | **1.075** | 1.072 | 1.075 | 0.754 | 0.754 |
| 4d Y | **1.237** | 1.216 | 1.236 | 1.225 | 1.224 |
| 5d La | **1.360** | 1.347 | 1.360 | 1.325 | 1.325 |

- **The potential is immaterial.** so94's self-shell-and-exchange refinement and so97's plain direct potential
  agree to **0.2 %** on every row. For a single entrant the distinction the two instruments make does nothing.
- **The exchange projection moves 1–2 %**, and it moves p the wrong way.
- **The Koelling–Harmon mass factor is the whole of the so94/so97 difference**, and it is a Z-driven suppression
  of the deep core: −1 % at Al, −4.5 % at Ga, −11.5 % at In, **−30 % at Tl**, −1 % at Y, −2.6 % at La. It leaves
  the d rows at 1.22–1.33 and destroys the p rows.

**Under every form the d rows are 22–36 % high and the p rows 5–10 % low.** That is not an operator statement:
all five weight the *same radial function*.

## 3. So the fault is the orbital — and the orbital does not fix it either

ζ on the **correlated** orbital (HF + form S with the PZ orbital SIC — the field the object takes its *removal
energies* on, where it takes ζ on the uncorrelated one):

| row | ⟨1/r³⟩ HF → corr | ratio HF | ratio corr |
|---|---|---|---|
| 3p Al | 1.0799 → 1.1551, **+6.97 %** | 0.910 | **0.974** |
| 4p Ga | 3.0307 → 3.2981, +8.82 % | 0.914 | **0.995** |
| 5p In | 5.1856 → 5.6844, +9.62 % | 0.955 | 1.047 |
| 6p Tl | 12.1446 → 13.4860, +11.05 % | 1.075 | 1.193 |
| 4d Y | 1.6093 → 1.6650, +3.46 % | 1.237 | 1.281 |
| 5d La | 2.1428 → 2.2119, +3.22 % | 1.360 | 1.404 |

Correlation contracts every entrant and raises ζ by 3–11 %. **It very nearly fixes 3p and 4p — 0.974 and
0.995 — overshoots 5p and 6p, and worsens both d rows.** So the residual is not one fault: it is at least two,
of opposite sign, one growing with Z inside p and one large and positive at d.

**The candidate for the second is prior art, and it is named as prior art, not measured here:** the two-body
spin–other–orbit interaction (Blume–Watson), which is absent from *every* one-body form above, reduces ζ, and is
largest for d shells. Whether it accounts for the d rows is a question this corpus cannot answer without building
an operator it does not contain. **That is a build, not a repair, and it is M's to authorise.**

## 4. And the decisive measurement: **nothing in this pass depends on it**

The store *measures* ζ at all six anchored openings, so the object can simply be re-read with the measured value
in place of the computed one. **That is not a fitted constant — it is the same act as gating on the store's
measured removal limits, which the object already does.**

| row | residual now | with the store's measured ζ | with ζ on the correlated orbital |
|---|---|---|---|
| 3p Al | +0.00050 | +0.00053 | +0.00052 |
| 4p Ga | +0.00052 | +0.00074 | +0.00072 |
| 5p In | +0.00052 | +0.00082 | +0.00114 |
| 6p Tl | −0.00174 | −0.00351 | +0.00107 |
| 4d Y | −0.00381 | −0.00416 | −0.00375 |
| 5d La | −0.00290 | −0.00394 | −0.00277 |
| **worst** | **0.00381** | **0.00416** | **0.00375** |
| **RMS** | 0.00211 | 0.00279 | 0.00204 |

**All three are the same object to within the spread.** ζ moves by 3–11 % between orbitals and by up to 36 %
between computed and measured, but it reaches the removal energy only through the Landé term, which is small: the
worst row moves 1.8 mHa and the RMS 0.7 mHa. **Every variant sits inside the record's single-entrant class bound
of ≤ 0.009 Ha** (`FINDING-HFTERM-SESSION-27`).

**And the choice of orbital for ζ is not decided by the six rows** — 0.00375 against 0.00381 worst, 0.00204
against 0.00211 RMS. The present choice is kept because it is the record's, **not** because measurement prefers
it. Stated because the opposite is easy to assume.

## 5. Protactinium, where the store measures nothing

| ζ scaled by | removal (eV) | t(5f) | move |
|---|---|---|---|
| 1.000 | **6.948** | 2.6359 | — |
| 0.735 (the 5d error) | 6.935 | 2.6349 | −0.014 |
| 0.808 (the 4d error) | 6.939 | 2.6352 | −0.010 |
| 1.099 (the 3p error) | 6.953 | 2.6362 | +0.005 |
| 1.047 (the 5p error) | 6.951 | 2.6361 | +0.002 |

**Across the entire range the six measured rows allow, the 5f removal energy moves by 0.019 eV** — against the
±0.11 eV typical bound the sibling ladder already carries (`FINDING-R4-19`). **The spin–orbit term is not what
limits the 5f figure**, and **ruling 1's floor holds at every scaling**: t(5f) stays between 2.6349 and 2.6362,
never approaching √6 = 2.4495 from below.

## 6. What is discharged and what is not — stated plainly

**Ruling 8(b) asked for the term to be repaired. It is not repaired, and this is not a shortfall left silent:**

1. **The term is worked in full.** Every form the corpus holds is measured against the store's six intervals, and
   the two differences between its two instruments are separated for the first time.
2. **The fault is located and it is not the operator.** No choice among the corpus's forms, and no choice of
   orbital, brings both p and d onto measurement; the residual is at least two faults of opposite sign.
3. **The repair needs an object the corpus does not contain** — a two-body spin–other–orbit term. Building one is
   subject matter, not instrument design, and under the standing rule that every subject-matter decision is M's,
   **it is put to M rather than done.**
4. **It is bounded, and the bound is what matters:** with an exactly correct spin–orbit term every anchored
   opening still closes to ≤ 0.0042 Ha and protactinium moves under 0.02 eV. **No figure of `FINDING-R4-15`
   through `R4-20` changes.**

**What is owed:** ruling 8(c), `t7c_cuaudit.py`'s absence, is the remaining item of ruling 8. A note found while
reading for it: the record states `t7c_cuaudit.py = t7c_corrz.py VERBATIM + env FENT`
(`PREDICTION-CU-AUDIT-SESSION-24`), which would be a route to settling it — except that `t7c_corrz.py` is
**also** absent from `recovered/`, which only holds `t7c_corrz_run.py`. Recorded here so the next pass starts
from it.

Nothing is repaired in any volume. Every figure is MEASURED by the instrument or RECORD-CARRIED with its quote.
