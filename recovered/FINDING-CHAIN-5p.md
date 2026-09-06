# FINDING-CHAIN-5p (s45, item 2) — 6/6 ON THE FIELD, THE ORDERING VARIABLE IS DISCRIMINATED, AND THE 4f CHANNEL IS HYDROGENIC

## 0 · THE ROW

    Z   ent  rec    ok      D_ent    margin   vs    D_4f    nfail  failset
    49   5p   5p   True   -0.18833  0.09460   6s  -0.03127    4   5d 5g 6d 6g
    50   5p   5p   True   -0.23359  0.13256   6s  -0.03129    2   5d 6d
    51   5p   5p   True   -0.27973  0.17235   6s  -0.03129    1   5d
    52   5p   5p   True   -0.32732  0.21423   6s  -0.03128    1   5g
    53   5p   5p   True   -0.37664  0.25831   6s  -0.03128    2   5g 6g
    54   5p   5p   True   -0.42783  0.30462   6s  -0.03128    2   5g 6g

**Chain 47 → 53 steps. CONFIG 39/47 → 45/53. STEP 42/47 → 48/53.**
Margins are against **6s**, named at every step (F44.2).

## 1 · SCORING — 8 HELD, 2 FAILED, 0 SUPPRESSED

**PC5P-1 HELD.** 5p is the entrant at all six. The n+ℓ = 6 tie-break (clause 2, smaller n
first) now holds on a **FOURTH distinct pair**: 4s/3d 10/10, 4p/5s 6/6, 4d/5p 10/10,
**5p/6s 6/6**. **32 steps, four unrelated pairs, no exception.**
**PC5P-2 HELD.** Runner-up is 6s at all six; the identity does not change once.
**PC5P-3 HELD.** 0.09460 → 0.30462, monotone, both endpoints inside the filed bands.
**PC5P-8 HELD.** cfg_ok = True and ok = True at all six; the recalled record configurations
match `ground.py` character for character.
**PC5P-9 HELD EXACTLY.** 45/53 and 48/53, disagreement set unchanged at 11, FIRST CONFIG
DIVERGENCE 24 and FIRST STEP DIVERGENCE 25 both unmoved.
**PC5P-10 HELD — A PREDICTION AGAINST.** Margin second differences run 0.00183, 0.00209,
0.00220, 0.00223: smooth, monotone, **no sign change and no minimum at Sb(51)**. The
half-filled 5p³ shell leaves no signature at the 1e-3 level. s44 found the 4d⁵ signature real
and four orders too small; the p-shell analogue is **not detectable at all**.
**§5 clause HELD.** Failing set {5d, 5g, 6d, 6g} ⊆ the filed set, and **no winning or
runner-up channel failed at any step** — unbroken on every row so far.

## 2 · THE ROW'S PURPOSE, MET

**PC5P-5 HELD. THE 5p ROW DISCRIMINATES n FROM n+ℓ AT ALL SIX STEPS.** The smallest-n open
candidate is **4f (n = 4)** at every step; the winner 5p carries **n = 5**. A plain `argmin n`
rule selects 4f at Z=49..54 and is **wrong at six consecutive elements**, while n+ℓ is right
at six.

**PC5P-6 HELD. THE EVIDENCE FOR n+ℓ OVER n GOES FROM FOUR ELEMENTS TO TEN** — K, Ca, Rb, Sr,
and now In, Sn, Sb, Te, I, Xe — and for the first time it rests on **two mechanisms**: a
tie-break at equal n+ℓ, and an outright loss by the smaller-n channel. s44 §2(9) filed the 4d
row's inability to discriminate as its own negative; this row is the repair.

## 3 · TWO FAILED PREDICTIONS, LOGGED WITH MECHANISM

**PC5P-4 FAILED at the far end.** Filed: D_ent ≈ −0.50 ± 0.06 at Z=54 and 0.05–0.06 per
proton. Measured **−0.42783**, outside the band by 0.012, at 0.045–0.051 per proton — below
the range at five of five steps.
*Mechanism: the band was extrapolated from the 4p row (−0.20007 → −0.48627, 0.057/proton).
**The 5p row deepens ~15% more slowly, and the difference is the intervening 4d¹⁰ shell.**
A band imported across a row that has gained a filled d shell is a band imported across a
change of screening. The failure is the extrapolation's, not the field's.*

**PC5P-7 FAILED on one clause, HELD on the other.** The bound held — |D_4f| < 0.10 and 4f is
less bound than 5p at all six. **The clause "4f deepens with Z" is FALSE.** See §4.

## 4 · THE RESULT NOBODY PREDICTED — 4f IS HYDROGENIC

    Z     D_4f      Zeff = sqrt(-32 D)     Zeff - 1
    39   -0.03137        1.00192           +0.00192
    43   -0.03130        1.00080           +0.00080
    48   -0.03128        1.00048           +0.00048
    54   -0.03128        1.00048           +0.00048

Hydrogenic 4f at unit charge is exactly **−1/32 = −0.03125**.

**ACROSS SIXTEEN ELEMENTS AND SIXTEEN ADDED PROTONS, Z=39 TO Z=54, THE 4f CHANNEL BINDS AT
Zeff = 1.0005 ± 0.0010 — AND THE DEVIATION SHRINKS MONOTONICALLY TOWARD 1 AS Z RISES.**
The channel is flat to 1e-5 across the whole 5p row while the nucleus gains six protons.

**It is inert to nuclear charge because it is perfectly screened.** An electron outside the
whole core sees unit charge no matter how large Z becomes, so its binding cannot move. This
is not fitted, not banded, and takes no input but c: the field puts an uncollapsed 4f
electron on the textbook hydrogen n=4 level and holds it there.

**AND IT IS PART 3's PRECURSOR, MEASURED IN ADVANCE.** 4f must collapse before it can open at
Ce(58). The walk now carries a **quantitative pre-collapse baseline over sixteen elements**,
so the collapse — when it arrives — will be measured as a departure from Zeff = 1 rather than
asserted. `PARTS-OF-THE-LAW.md` §3 named orbital collapse (Goeppert-Mayer 1941;
Griffin–Andrew–Cowan 1969) as the candidate mechanism shared between parts 2 and 3. **This is
the first number that mechanism has to explain, and it was produced by a row that was not
looking for it.**

**Declared: this was found, not predicted.** It is scored as a FINDING, never as a held claim,
and PD-5's 4f trace is extended rather than confirmed. The next session must file
**PREDICTION-4f-COLLAPSE** before Z=55 runs, stating where Zeff is expected to leave 1.

## 5 · UNPREDICTED AND STILL UNEXPLAINED

`nfail` runs 4, 2, 1, 1, 2, 2 — non-monotone, with 5d dropping out after Z=51 and 5g
appearing from Z=52. **The 5g onset at Z=46 was stated and not explained in s44; a second
onset boundary at Z=52 is now stated and not explained either.** Item 3 (`t7g_exc.HFCN`)
remains the instrument for both, and is now owed on two boundaries rather than one.
