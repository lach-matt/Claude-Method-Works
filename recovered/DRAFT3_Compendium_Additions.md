# DRAFT 3 — Compendium additions for the three-body solution

*For review. Nothing here is written into any existing compendium. Order: Mathematical, Physics, Index of Indices, Spectra, Register last. Figures are attached files referenced inline.*

---

## A. MATHEMATICAL COMPENDIUM — additions

### To I · THE CYCLE — the seed table

No new root. The three-body work derives from `L.c1`–`L.c8` (the tree bounds), `B.brk` (the bracket), and the operators; the seed did not move. That is the cycle's falsifier passing on a new subject.

### To II · THE OPERATORS

| symbol | definition | scope | origin |
|---|---|---|---|
| **π** | the shape map ℂ³ → ℝ³, w = (½(|Z₁|²−|Z₂|²), Re Z₁Z̄₂, Im Z₁Z̄₂) | configurations | Montgomery 2014; Hopf 1931 |
| **N₈** | the norm ∏_{ε∈{±1}³}(U − ε·u) — the minimal polynomial of a sum of three square roots | potentials | Lagrange 1770 |

### To IV · THE OBJECTS — new family **3B. Three bodies — 9 objects**

`3B.shape` — **shape space and shape sphere.** ℝ³ = ℂ³ / (translations × rotations); S² = that / scale. Onto; identifies exactly the oriented-congruent triangles; only triple collision maps to 0; w₃ = signed area up to a mass constant; ‖w‖ = I/2. *Montgomery 2014, Thm 1.* Grade: PROVED (cited).

`3B.metric` — **the shape metric** ds² = |dw|²/(2√‖w‖); every plane through 0 totally geodesic, cone metric dr² + ¼r²dθ². *Montgomery 2014, Thm 3.* PROVED (cited).

`3B.JM` — **the Jacobi–Maupertuis metric** g_E = (E+U)·ds²; trajectories at energy E are its geodesics; dt = ds_E/√(2(E+U)). *Maupertuis 1744; Jacobi 1837.* PROVED (cited). Licence in the index: §12.11.1.3, §12.11.0.2.

`3B.pot` — **the potential on shape space** U(w) = Σ c_ij/d_ij, c_ij = (m_i m_j)^{3/2}/√(m_i+m_j), d_ij² = ‖w‖ − w·b_ij; identity r_ij² = d_ij²/μ_ij. *Montgomery 2014 §11.* MEASURED: 650 triangles, 13 mass cases, error < 10⁻¹⁰. No hyper-radius factor.

`3B.norm` — **the algebraic variety.** With u_ij = c_ij/d_ij, p = Σu², q = Σu_i²u_j², r = ∏u²:
U⁸ − 4pU⁶ + (6p²−8q)U⁴ − 4(p³−4pq+16r)U² + (p²−4q)² = 0; constant term = ∏(u₁±u₂±u₃)². *Lagrange resolvent.* PROVED (symbolic, sympy) and MEASURED at 13 mass cases. An inherited form with U⁴ coefficient "6S₂²−4S₄+8S₁₁" = 2p²+16q was wrong and is withdrawn.

`3B.five` — **the five fixed points.** Three Euler roots (one positive root of the quintic per ordering) and two Lagrange points, for every mass triple. *Euler 1767; Lagrange 1772.* MEASURED 13/13. Seed of the family index in §14.5's sense.

`3B.tri` — **the triangle form on K₃** {|a−b| ≤ c ≤ a+b}: join-closed, meet-broken. Cap 8: 344 cells, 0 join failures, 8,385 meet failures; caps 3–12 meet failures 12·111·477·1,488·3,780·8,385·16,812·31,227·54,555·90,705; two-body chain 0 throughout. Confirms §12.11.2 on a grid the book never ran. MEASURED. ![Fig 2](fig2_closure_defect.png)

`3B.def` — **the deficit.** K₃ has treewidth 2; strong 3-consistency required (Freuder 1982); ℛ reaches 2 (§32.3). Shortfall exactly one level. PROVED (§21.5.1 + Freuder). ![Fig 5](fig5_constraint_graphs.png)

`3B.index` — **the index Λ₃** = {KAM, per, chaos, erg, coll} on ℳ_{E,L}. E(Λ₃) = 0: exhaustive (Chazy classes), disjoint up to measure zero (Saari 1971/73; Painlevé n=3). By §25.6, predictions = 0. PROVED (cited theorems assembled; the assembly is this work's).

### To V · THE CHAINS — one new chain

`L.c1–8` → tree → §7.1 separation hypothesis → `3B.def` (K₃ breaks it) → `3B.tri` (measured) → `3B.index` closes as envelope → §25.6 → zero predictions ≡ Brudno rate. Nine links, no new root.

### To VI · WHAT IS UNFINISHED — nothing added

The three-body work leaves no open object. The two existing unfinished objects (`M.C2`, `Q.exch`) are untouched.

### To VII · THE BIBLIOGRAPHY — add

Alekseev 1968; Arnold 1963; Brudno 1983; Chenciner–Montgomery 2000; Euler 1767; Fleischer–Knauf 2019; Freuder 1982 (already present — now cited correctly); Hill 1878; Hopf 1931; Hsiang–Straume 2006; Jacobi 1837, 1842; Kol 2021, 2023; Kolmogorov 1954; Lagrange 1770, 1772; Marchal–Bozis 1982; Marchal–Saari 1975; Maupertuis 1744; McGehee 1974; Monaghan 1976a,b; Montgomery 1998, 2002, 2014; Moore 1993; Moser 1962, 1973; Nash–Monaghan 1978; Painlevé 1897; Saari 1971, 1973, 1984; Stone–Leigh 2019; Sundman 1912; Xia 1992; Zvonkin–Levin 1970.

---

## B. PHYSICS COMPENDIUM — additions

### New section: Λ₃ — THE THREE-BODY INDEX

**What it indexes.** Motions of three point masses under Newtonian gravity, at fixed E and L, by asymptotic class: five cells. It is the second index in the compendium built from physics rather than from Λ (the first is Λ_spectra), and the first whose subject is classical.

**The coordinate supply.** The masses enter through exactly six numbers — three c_ij and three unit vectors b_ij — and nowhere else. Everything structural (S², the metric, N₈, K₃) is mass-free. ![Fig 1](fig1_shape_sphere.png)

**Kinematic and stateful.** Λ₃'s cells are configurations; by §12.11.1.3 the index has no time column, and the flow is the geodesic flow of `3B.JM`. Time is a quadrature and carries the transcendental part (Sundman series; Painlevé transcendents on the natural boundary). This is the interface §93 found in the register's own objects, now on a classical subject: *placing* a cell (which stratum) and *valuing* it (the geodesic) are different operations.

**Where the physics is exact and where it is envelope.** Exact: the five fixed points, the zero-velocity surface {E + U ≥ 0} (Hill 1878), Hill stability of a hierarchy (Marchal–Bozis 1982). Envelope: every stratum boundary, by `3B.tri`. ![Fig 4](fig4_equator_potential.png)

**The point of observability.** What Λ₃ delivers for a given state: the stratum, the family within it (torus / braid word / symbolic sequence / distribution P(ε)), and the geodesic as far as the natural boundary. What it never delivers: r_i(t). §25.6 is why.

**Failure modes, measured rather than anticipated.**
1. A factor of the hyper-radius carried into `3B.pot` from an inherited convention: 13/13 failures, uniform, hence in the audit not the object. Corrected.
2. An inherited degree-8 polynomial with two wrong coefficients: caught by the second route (N₈). Withdrawn.
3. Threshold silence: L4/L5 stability at μ < 0.0385209 is a number; the method is silent (§31.1.1). Not a failure, a boundary.

### To Λ_phys — THE INDEX OF PHYSICAL PARAMETERS — add rows

| parameter | enters through | where the work would break first |
|---|---|---|
| m₁, m₂, m₃ | c_ij, b_ij only | nowhere structural; moves the five points |
| E | the conformal factor E + U | zero-velocity surface |
| L | the reduction 6 → 4 | angular-momentum stratum boundary |
| G | set to 1 by scaling | nowhere |

---

## C. THE INDEX OF INDICES — additions

### To V · THE INDEXES BUILT FROM IT — new subsection: Λ₃, the three-body index

| coordinate | values | bound |
|---|---|---|
| stratum | KAM, per, chaos, erg, coll | five, exhaustive |
| E | ℝ | sign fixes bounded/unbounded |
| L | ℝ | — |
| masses | ℝ₊³ | 13 order-types; symmetry order 6, 2, 1 |

E(Λ₃) = 0. Certificate (§18.4.1): the shape map, three dropped coordinates. ![Fig 3](fig3_tower.png)

### To VI · THE INDEXES NAMED AND NOT BUILT — remove one

"The three-body problem" — previously named at §12.11.2 as the maximal excluded case and not built. Now built. Move to V.

### To VIII · WHAT EACH INDEX IS — new row

| index | the one thing only it gives |
|---|---|
| **Λ₃** | a complete index whose completeness *is* the impossibility theorem — E = 0 read as Poincaré |

### To the one-line summary, extended — new row

| **Λ₃** | masses enter through six numbers; structure is mass-free — the three-body factorisation, closed |

---

## D. SPECTRA COMPENDIUM — additions

### To III · THE MECHANISMS — one cross-reference

The bracket `B.brk` (T(n) between T(n−1) and T(n+1)) is the book's one ternary object (§21.5.1). Λ₃ is the ternary object of celestial mechanics. The two share the deficit: both need strong 3-consistency and both get level 2 from ℛ. In spectra the deficit is paid per channel by the envelope cells of §12.11.3; in three bodies it is paid once, by the stratum boundaries. No channel entry changes. One line to add under `B.brk`: *"The same shortfall, on a classical object, is Λ₃ (Index of Indices V)."*

---

## E. THE REGISTER — new entries (numbered provisionally 1701–1712; renumber on insertion)

**1701 · a finding.** The stratification of ℳ_{E,L} into five asymptotic classes is an index with E = 0. Cited by 1702, 1705, 1709.

**1702 · a finding.** E(Λ₃) = 0 and §25.6 together give zero predictions; this is Brudno's theorem on the chaotic stratum. The impossibility and the completeness are one statement.

**1703 · a finding.** The three-body potential exhibits §12.11.2's three excluded forms term by term: sum (superposition), difference (Jacobi vectors), symmetric (N₈ in power sums).

**1704 · a measurement.** Triangle form at cap 8: 344 cells, 0 join failures, 8,385 meet failures; caps 3–12 as in `3B.tri`; two-body chain 0. Confirms §12.11.2's join-closed/meet-broken on a fresh grid.

**1705 · a measurement.** 13 mass order-types × 6 checks = 78/78. Symmetry order 6, 2, 1 by number of coincident masses.

**1706 · a correction.** First audit run: check A failed 13/13. Cause: the shape potential divided by the hyper-radius R, an inherited convention. Montgomery's c_ij/d_ij is already Newton's potential (r_ij² = d_ij²/μ_ij). Uniform failure across cases was the diagnostic. §2.14.

**1707 · a withdrawal.** The degree-8 polynomial "U⁸ − 4S₂U⁶ + (6S₂² − 4S₄ + 8S₁₁)U⁴ − …" is withdrawn: its U⁴ coefficient equals 2p² + 16q where the norm gives 6p² − 8q, and its U² term is likewise wrong. Replaced by N₈. Caught by second route (register 784's mechanism).

**1708 · prior art.** N₈ is the norm over (ℤ/2)³ — Lagrange's resolvent method (1770). Not new mathematics.

**1709 · prior art.** Eight attribution questions formed from residue before deriving (§E.5); seven closed to named owners: Montgomery, Saari, Painlevé, Moore/Chenciner–Montgomery, Maupertuis/Jacobi, Alekseev/Moser, Monaghan/Stone–Leigh/Kol, Brudno, Hill/Marchal–Bozis, Baker–Pixley/Montanari/Dechter/Freuder. "Microcanonical ergodic flux" is Kol's term; K(s) ≈ |s| is Brudno's theorem.

**1710 · a new protocol.** *Uniform failure is a fault in the instrument.* When a check fails identically across every case of a variable the object depends on, the fault is upstream of the object. Earned by 1706.

**1711 · a fault of mine.** Carried a convention from working material into a verified formula without checking its normalisation against the source. 1706 is the instance; 1710 the protocol.

**1712 · an open question, closed.** Whether the three-body problem is "the maximal case of what Chapter 18 forbids" (§12.11.2) or a subject the method could solve. Both: the maximal forbidden case *is* the solved case, because what is forbidden is exactly what Poincaré excludes. Closed by 1702.

---

## Figure manifest

| file | used in | shows |
|---|---|---|
| fig1_shape_sphere.png | Physics; essay | S² with E, L, B points; two mass cases |
| fig2_closure_defect.png | Math `3B.tri`; essay | meet/join failures vs cap; chain at 0 |
| fig3_tower.png | Index of Indices; essay | 12 → 4 → 2 → 1 inputs |
| fig4_equator_potential.png | Physics | U on the collinear circle, three mass cases |
| fig5_constraint_graphs.png | Math `3B.def` | K₂ vs K₃, consistency levels |
