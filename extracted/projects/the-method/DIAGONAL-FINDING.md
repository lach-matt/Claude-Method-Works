# THE DIAGONAL — WHERE THE FACETS LIVE, AND WHAT IS MEASURED THERE

*Computed by `diag.py`, `diagonal.py`, `diagonal2.py`. Follows `FEASIBILITY-FINDING.md`
(five facets). Data: `COORDINATES-2_13.csv` grade **measured** only, plus Rb I from
R 1258 at source. Grade **computed** was never read as evidence — those values are the
amplitude law's own output (Physics Compendium: three fitted constants, "why nothing in
this work answers Löwdin").*

---

## 0 · A SELF-CORRECTION FIRST

Two turns ago I proposed testing whether δ is concave in p along a series. **R 1457 had
already closed that** (δ bounded in n, a√p divergent) and **R 1458 measured the walk's
entrant inside its channel range at 5 of 114.** I proposed a test the register refutes.
What today's facets change is narrower: R 1457's structural objection targets **√p**;
bounded concave forms are feasible (`p1.py`: 1−e⁻ᵖ, 0 refuted, clique 3). The objection
sinks the function, not the shape. R 1458 stands and is respected below.

## 1 · FOUR OF FIVE FACETS LIE ON A SINGLE MADELUNG DIAGONAL

Generating chords, verified at source (`diag.py`; a filter bug printed extra rows for
Ga–Kr and Lu–Au that are monotonicity chords, not facet chords — `p1f.py`'s provenance
stands):

| facet | generators | chord | n+ℓ |
|---|---|---|---|
| 1 | La, Gd | 4f · **5d** · 6p | 7 7 7 |
| 2 | La, Gd | 4f · **5d** · 7s | 7 7 7 |
| 3 | Tl–Rn | 5f · **6p** · 7s | **8** 7 7 |
| 4 | Ac, Th, Cm | 5f · **6d** · 7p | 8 8 8 |
| 5 | Lr | 6d · **7p** · 8s | 8 8 8 |

A Madelung diagonal is the Demkov–Ostrovsky multiplet, n_r + 2ℓ = M − 1 — the coordinate
R 1450 records the field has used since 1972. **On a diagonal n = (M + p + 1)/2**, so
A = n is linear in p with slope ½, p ≡ M+1 (mod 2) is automatic (R 1456's parity), and

> **ν = const + p/2 − a·v(p) — a function of ONE variable.**

**Rung 3 dissolves on the diagonal.** "Why is B a function of p alone" is not a question
at fixed M: n, ℓ and p determine each other.

**And the six refuting steps are proved, not listed.** With linear v, p/2 − a·v(p) is
linear along the diagonal, so its minimum is at an endpoint, so no interior member can
enter first. La, Gd (5d on M=7), Ac, Th, Cm (6d on M=8), Lr (7p on M=8) are exactly the
six steps whose entrant is interior to its diagonal's live set. *That is the second
Madelung rule and its exceptions, restated as lower-hull geometry.* Facet 3 is the one
cross-diagonal comparison that binds — 6p (M=7) before 5f (M=8) at Tl.

**So the problem splits, and each part has a home:**
- *Which diagonal is live* — the onsets. Closed as exact combinatorics at R 1617; Belokolos
  derives the asymptote and drops the parity term (R 1456). Not a Löwdin gap.
- *Within a diagonal, which member* — every anomaly facet. One variable. Physical name:
  **how the D-O degeneracy is lifted below threshold** (R 1621: exact at E = 0, lifted at
  E < 0). R 1621 tested width-vs-Z and refuted it; it did not test this.
- *One cross-diagonal step* — Tl, alone.

## 2 · WHAT IS MEASURED ON THE DIAGONAL: THE CHANNEL DEFECT IS CONCAVE IN p

At each closed core, read the **measured** channel defect δ(ℓ) and place it on the next
live diagonal by p = n − ℓ − 1. (Along a diagonal p ↔ ℓ bijectively; δ is a per-channel
constant with median series spread 0.013 (R 1457), so its value at the lowest member —
where the walk's entrant sits — is the same shape to that tolerance. This uses δ by ℓ at
a fixed core, never along n; R 1457's objection does not arise.)

    K I    Ar core   n+ℓ=5   3d 0.246 · 4p 1.727 · 5s 2.191    Δ 1.481, 0.464   CONCAVE
    Rb I   Kr core   n+ℓ=6   4d 1.331 · 5p 2.657 · 6s 3.136    Δ 1.326, 0.479   CONCAVE
    Sr II  Kr core   n+ℓ=6   4d 1.458 · 5p 2.350 · 6s 2.711    Δ 0.892, 0.361   CONCAVE
    Cs I   Xe core   n+ℓ=7   4f 0.033 · 5d 2.466 · 6p 3.593 · 7s 4.051
                                                   Δ 2.433, 1.127, 0.458          CONCAVE
    Ba II  Xe core   n+ℓ=7   4f 0.756 · 5d 2.415 · 6p 3.241 · 7s 3.598
                                                   Δ 1.659, 0.826, 0.357          CONCAVE

**Seven of seven second differences negative, five of five cores/charges.** Every case in
the bank with three or more measured members on a diagonal.

**Facets 1 and 2 checked directly at Cs I:** v₀−2v₂+v₄ = −1.308 · 2v₀−3v₂+v₆ = −3.281.
Both satisfied by measurement. **Facets 4 and 5 (M = 8) are NOT tested** — the bank holds no
measured d or f channel for Fr I or Ra II. Stated as a gap, not assumed.

### 2.1 The shape is invariant under charge; the order is not
Kr core: Rb I orders (a = 1) 5p < 4d < 6s, Sr II orders 4d < 5p < 6s. Xe core: Cs I
6p < 5d, Ba II 5d < 6p. **The one-electron ORDER flips with charge — R 1304's measured
reordering, reproduced — while the CONCAVITY does not.** That is the split the work has been
circling: **shape is a one-electron property of the core; where the atom sits on it is
the amplitude, R 1311's many-electron quantity.**

### 2.2 The interior member is reachable, and the atom is not at a = 1
On Cs I's measured δ: 5d enters first iff **0.411 < a < 0.887**; 4f iff a < 0.411; 6p iff
0.887 < a < 2.18. La takes 5d; Ce takes 4f. The corridor for the observed anomaly is
non-empty and interior — which no linear v could give — and it excludes a = 1. **ν is
not n\*** (R 1457's conclusion, kept), and the amplitude that places the atom is not
supplied here (R 1311, unchanged).

### 2.3 What the concavity IS, physically
Increments 2.43 → 1.13 → 0.46 at Cs: **penetration saturates.** f is centrifugally
excluded (δ ≈ 0; R 1255's gate ℓ − ℓ_core ≥ 2), d partly admitted, p and s both fully
penetrating and so differing least. The marginal defect gained per unit of ℓ removed
falls once the electron is already inside — diminishing returns on penetration, in
ℓ at fixed core. Standard quantum-defect physics; the attribution is Seaton's and the
centrifugal barrier's. **What is new is only that this is the shape the facets demand,
and that it holds by measurement wherever the bank can test it.**

## 3 · REOPENS ON RECORDED FACT — FOR M's RULING, NOT MINE
- **R 1458** declared "no route from ν to δ." It tested level-RANGE overlap. The route
  above is v := δ_channel(ℓ) at the closed core, read across ℓ on one diagonal — a
  different object, untested there. Reopen requested, not asserted.
- **R 1457**'s "no physical candidate remains" was reached against √p specifically.
  A measured concave v is a candidate for the SHAPE only. The amplitude remains
  undelivered and R 1457's verdict on ν-as-measure stands.

## 4 · STORE FLAG
Rb I's measured defects (R 1258: 3.1357 · 2.6566 · 1.3307 · 0.0143) are in the register
and **absent from `COORDINATES.tsv` at measured grade** (Z=37, charge 1: eight computed
rows). Same shape as T9. Flagged, not repaired here.

## 5 · WHAT THIS DOES NOT DO
No Schrödinger derivation. It locates every anomaly facet on a D-O multiplet, reduces
rung 3 to one variable there, and shows by measurement that the one-electron shape on
that variable is concave wherever it can be read. **The amplitude `a` — the many-electron
term R 1311 names — is untouched, and Löwdin's challenge stands.**

## 6 · REGISTER OWED
- **R 1707** — the diagonal reading: four facets on single Madelung diagonals; ν one-
  variable at fixed M; the six refuting steps proved as interior-of-diagonal entrants.
- **R 1708** — measured concavity of δ along five diagonals, 7/7; shape charge-invariant,
  order charge-variant; facets 1–2 confirmed at Cs I; facets 4–5 untested.
- **R 1709** — self-correction: proposed a series-concavity test R 1457 had closed.
- **Flag** — Rb I store gap (T9-shaped).
