# THE CLIQUE-3 OBSTRUCTION — WHY IT IS NOT AT THREE ELEMENTS

Computed by `clique3.py`, which rebuilds the 106 corridors from `brack.py`'s own
construction — bound = (Δn)/(√p_rival − √p_entrant), node counts only, nothing fitted.
Answers the open item in `CHAPTER-LOWDIN.md` §8: *"why those three and not others
is not explained."*

## 1 · The measurement reproduces, by two routes

106 corridors · 735 edges · density 0.132 · **max clique 3** · 10 isolated vertices ·
minimum stabbing points 3 at 0.7071, 1.7071, 2.4409. Greedy-by-right-endpoint
(maximum disjoint set) and brute-force max clique on the conflict graph agree.
R 1517 and R 1521 are confirmed at source.

## 2 · The generating form

Write **g(p) = 1/(√(p+2) − √p)**. A corridor is CANONICAL when both its binding
rivals sit at Δp = ±2 with Δn = ±1; a canonical corridor is then exactly the band

> **( g(p−2) , g(p) )**

32 of the 106 are canonical, and they take only **four distinct intervals**:

    p=0   (−∞,      0.7071)   26 members   B C N O F Ne Sc Ti V …
    p=2   (0.7071,  1.7071)    2 members   La Gd
    p=3   (1.3660,  1.9841)    3 members   Ac Th Cm
    p=5   (1.9841,  2.4409)    1 member    Lr

g is increasing because √ is concave, so the bands ascend. They tile only when p
advances by 2 — the even sub-chain (0, 2) and the odd (3, 5) interleave, and p=3
overlaps p=2 on (1.3660, 1.7071). **That overlap is why the answer is 3 and not 4.**

## 3 · THE CORRECTION — the obstruction is not located at three elements

R 1517 reads *"forced by three elements — boron, lanthanum and lawrencium."*
**There are 205 maximum cliques, not one.** B/La/Lr is one certificate among them.
Sorted by upper endpoint:

    slot 1   51 distinct elements are interchangeable   (B is one of them)
    slot 2    5 distinct elements: Ac, Th, Cm (51 each) · La, Gd (26 each)
    slot 3    Lr ALONE, in all 205

57 of the 106 vertices appear in some maximum clique. **Only lawrencium is forced.**

## 4 · What this says

The clique number 3 is a property of the corridor FAMILY — how many ascending bands
g(p−2)→g(p) the table realises — and not of three special atoms. Boron is the first
member of a 26-element class and was selected by the greedy scan's ordering, not by
any physics. **Naming B and La as the obstruction is the object-versus-observer
coordinate fault again**: a property of the class attributed to the representative
the search happened to reach first (cf. R 1578, and R 1672's negative-from-scope).

Lawrencium is different in kind. It is the sole member of the p=5 band because it is
the only entrant in the table with p = 5 bracketed at p ± 2 — 7p entering against 6d
below and 8s above. **That is a fact about where the table ENDS, not about lawrencium.**
Consistent with R 1696: Z = 120 is a declared bound, so the top band is bounded by the
declaration and not by the shell system.

## 5 · What remains open

The four canonical intervals are exact surds in g. Whether the 74 NON-canonical
corridors admit a second closed family, and whether any band above p=5 would be
realised by a table extended to Z = 120, are not computed here.
