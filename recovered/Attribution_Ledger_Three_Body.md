# Attribution Ledger — the three-body derivation

**Protocol.** §E.5: *search before deriving.* Audit 7 ATTRIBUTION. Each residue item was recast as a question, and each question was put to the literature before any computation. Every component of the Gemini framework is now assigned to its owner; the one element that could not be assigned is named as such rather than absorbed.

## The questions and who answered them

| # | Question | Owner | Where | Status |
|---|---|---|---|---|
| 1 | Shape coordinates (w₁,w₂,w₃), shape metric, potential on shape space | **R. Montgomery** | *The three-body problem and the shape sphere*, arXiv:1402.0841 (Amer. Math. Monthly); *Infinitely many syzygies*, ARMA 164 (2002) | closed — second route to the coefficients |
| 1a | Jacobi vectors and the mass metric | **C. G. J. Jacobi** (1842); Hopf map remark: **H. Hopf** (1931) | Montgomery §8, Prop. 3 | closed |
| 1b | Degree-8 algebraic variety P(V₀,w,R)=0 in power sums S_k | **unattributed** | searched: Montgomery, Hsiang–Straume, Lemaître — not found | **open: candidate novel element, or owed one more search** |
| 2 | Collision set has Lebesgue measure zero | **D. G. Saari** | Trans. AMS 162 (1971) 267–271; erratum 168 (1972) 521; II, Trans. AMS 181 (1973) 351–368 | closed; extended by Fleischer–Knauf, ARMA (2019) |
| 2a | Non-collision singularities measure zero | **Painlevé** (1895): none exist for n=3 | Painlevé's theorem; Xia (1992) shows they exist for n≥5 | closed for n=3 only — 𝒩_coll clause must be scoped to three bodies |
| 2b | Collision and total-collapse manifolds | **Saari** (1984), **Saari–Hulkower** (1981), **McGehee** (1974) | J. Diff. Eq. 55, 41; Invent. Math. 27 | closed |
| 3 | Figure-eight and braid classification | **C. Moore** (1993, discovery); **Chenciner–Montgomery** (2000, proof); **Montgomery** (1998, braid group) | PRL 70, 3675; Ann. Math. 152, 881–901; Nonlinearity 11, 363 | closed |
| 4 | Jacobi–Maupertuis metric geodesics on reduced space | **Maupertuis** (1744), **Jacobi** (1837); on shape space **Montgomery** (2002, 2014) | Montgomery Thm 3, eq. 51 | closed |
| 5 | Horseshoe / symbolic dynamics in the three-body problem | **V. M. Alekseev** (1968–69); **J. Moser** (1973) | *Stable and Random Motions*, Princeton | closed |
| 5a | KAM tori | **Kolmogorov** (1954), **Arnold** (1963), **Moser** (1962) | standard | closed |
| 5b | Ergodic ejection statistics, "microcanonical flux" | **J. J. Monaghan** (1976a,b), **Nash–Monaghan** (1978), **Stone–Leigh** (Nature 2019), **B. Kol** (2021, *flux-based statistical prediction*) | MNRAS 176, 63; 177, 583; 184, 119; Nature 576, 406; CMDA 133, 17 | closed — Gemini's phrase is Kol's |
| 6 | Kolmogorov complexity of chaotic orbits grows linearly | **A. A. Brudno** (1974, 1982/83) — complexity rate = KS entropy; conjectured **Zvonkin–Levin** (1970) | Trans. Moscow Math. Soc. 2 (1983) 127–151 | closed — Gemini's K(s) ≈ |s| is Brudno's theorem with h > 0 |
| 7 | Zero-velocity surfaces and Hill stability as bounds | **G. W. Hill** (1878); general 3D case **Marchal–Saari** (1975), **Marchal–Bozis** (1982); hierarchical criterion **Mardling–Aarseth** (2001) | Amer. J. Math. 1; J. Diff. Eq. 20; Celest. Mech. 26, 311 | closed — these are the book's §31.1.1 brackets |
| 8 | Closure ⇔ global consistency; treewidth-2 deficit | **Baker–Pixley** (1975), **Bergman**, **Montanari** (1974), **Dechter** (1992), **Freuder** (1982) | already in book §14.1, register 400 | closed |
| — | Time-eliminated reduction as a "solution" framing | **B. Kol** (2021), *Natural dynamical reduction of the three-body problem*, CMDA | — | closed — nearest published statement of Gemini's thesis |

## What is ours

Three things, after the ledger:

1. **The reading of the stratification as a closed index with E = 0**, and hence the identity between "completely solvable" and "zero predictions" (§25.6). This is the book's theorem applied; the application is new.
2. **The identification of Gemini's three potential forms with §12.11.2's three excluded forms** (sum, difference, symmetric), and hence the proof that the strata are the monotone envelope and cannot be sharpened. New.
3. **Possibly** the degree-8 variety (1b) — held open until one more search closes it either way.

Everything else in the framework belongs to the names above and is to be cited as such in the derivation.

## Next step

Build. The coefficients now have their second route (Montgomery's c_ij, d_ij); the build verifies Gemini's A_ij = √2·c_ij, C_ij, D_ij symbolically against Montgomery's formulae, and tests the degree-8 polynomial by elimination. Then the index computation: K₃ closure, excluded-form meet failures, restricted-problem closure.
