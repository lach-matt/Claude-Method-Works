# Evaluating λ1 and δ: methods, the reduction, and the programme

*Status.* Begun D338 (M, 2026-10-30: "deep research this for possible methods of evaluating/calculating/deriving such
numbers, and then prove them"). Section 2's reduction was read by verifier 155 (D338): Proposition 2.1 correct,
Proposition 2.2 incomplete (two major findings, five minor, six nits). It is repaired here (D338) and is to be read
again. Nothing else here is proved. Labels as in the record: computed, deduced, READ.

## 0. Summary

- *What λ1 and δ are.* Theorem 4 (proof5 Part VII Theorem 0.2) holds for λ ≤ λ1 and data within δ. Both are fixed in
  Part VII section 4.

- *What they reduce to.* Section 2 proves that they are explicit functions of a finite list of constants:
  - the tame constants of III.K's map and of its right inverses, and the smoothing constants;
  - the loss d of the right inverses, with k'' and d1 = N + k'';
  - the radius δ_K in U on which the right inverses exist and the constants are uniform;
  - the data thresholds of III.K (A_2d, ε_dat) and of Part VII's G-invariant run (ε_G);
  - the record's threshold λ_1.1 at order J, and the gluing's η_gl and C_R.

- *The Nash–Moser step is already effective.* II.G's threshold is an explicit formula in those constants (Proposition
  2.1 below).

- *Where the numbers are lost.* In the linear theory (through the right inverses, and through III.J's inverse
  operators inside the map), in the gluing, and in the local quasilinear theory; the record's threshold at order J is
  not yet checked. The arguments are of four kinds (section 3), and EFFECTIVE-LEDGER.tsv lists the sites.

- *Methods exist for each kind* (section 4, READ). Turning them into numbers is a programme of the size of a second
  write-out of the linear theory, with certified computation at Tangherlini. Section 5 states it.

- *What a number would look like.* Any number it produces will be extremely small, of the order of θ0^−(8d+2) with θ0
  built from products of the linear constants, and d itself a sum of losses not yet added up. It would answer "how
  small is small enough" in the proof's own terms, not physically.

## 1. Methods found (READ)

1. **Verified inverse-operator norms.**
   - *What it replaces.* The step "injective and Fredholm, hence bounded below".
   - *The idea.* Computer-assisted proofs for PDEs bound ‖L⁻¹‖ by splitting off a finite-dimensional part. That part is
     handled by verified linear algebra, and the rest by explicit projection-error constants.
   - *READ.* Sekine, Nakao and Oishi (arXiv:1910.00759v1) write the inverse as an operator matrix through a Schur
     complement S. Their Theorem 2.1 (p. 5) gives L⁻¹ explicitly once T (finite-dimensional) and S are nonsingular, and
     their Lemma 2.2 (p. 6) bounds ‖S⁻¹‖ ≤ 1/(1 − κ) when κ < 1. They state that "the evaluation of ||L⁻¹|| is the
     major task in the verification procedures" (p. 3).
   - *The literature.* It goes back to Plum (1991) and Nakao–Hashimoto–Watanabe (2005), with the monograph of Nakao,
     Plum and Watanabe (2019) (references [7], [12]-[20] there).
2. **Proof mining.**
   - *What it replaces.* Compactness used through convergent subsequences.
   - *The idea.* Replace sequential compactness by Heine–Borel compactness, which yields computable bounds.
   - *READ.* Ferreira, Leuştean and Pinto (arXiv:1810.01508v4, abstract, p. 1): sequential weak compactness arguments
     "can be replaced by Heine/Borel compactness arguments", which "trivializes under the so-called bounded functional
     interpretation", so that "the proof mining program of extracting computational bounds" applies. They also observe
     that Heine–Borel compactness "can be removed from arguments whose conclusion is a quantitative statement. This is
     emphatically not the case with sequential compactness arguments" (p. 2).
   - *What this means here.* An argument "by contradiction with sequences (σ_j, b_j) → (σ_*, b_*)" is to be rewritten
     as a finite cover of the parameter set with explicit radii.
3. **Computer-assisted proofs in general relativity.**
   - *READ.* Goldstein and Jejjala (arXiv:2609.21797v2) prove existence of a non-Schwarzschild black hole in
     Einstein–Weyl gravity. Their tools are a convergent horizon series, a "compact core enclosed by a parameter
     dependent Taylor model with directed rounding", and a tail "treated as a centered stable manifold fixed point
     problem", joined by a Poincaré–Miranda certificate (abstract, p. 1).
   - *Precision.* The core's endpoint derivatives are of order 10¹⁴ and the tail tolerance of order 10⁻³⁰, handled with
     512-bit MPFR intervals (pp. 2, 33).
   - *What this means here.* Separated radial ODEs on a black-hole exterior, with a regular singular horizon and an
     irregular end, are within the reach of validated Taylor models. That is the shape of the Tangherlini mode problems
     here.
4. **Explicit Nash–Moser.**
   - *Here.* The record's II.G proof is explicit: section 2 below extracts the formula.
5. **Large constants are to be expected.**
   - *Where.* When trapping is present, the semiclassical resolvent cut off to a region far from the trapped set can
     still be exponentially large in the inverse semiclassical parameter (Datchev–Jin, "Exponential lower resolvent
     bounds far away from trapped sets", J. Spectral Theory, title and abstract READ through the search index only).
   - *What this means here.* Making the high-energy estimates explicit will not give small constants. That is a
     reason to keep the explicit high-energy work on Tangherlini, where the dynamics are explicit.

## 2. The reduction (proved; repaired D338, to be read)

**Proposition 2.1 (II.G's threshold, explicitly).**

- *Setting.* In II.G Theorem 2.1 (PART-II-G-NASHMOSER.md), write its support parameter η_G and its radius δ_G (there
  η0 and δ). Put α := 8d+2 and N := 21d+6, and define the K's below.

- *Constants.*
  - K1 := C_d(1+δ_G)
  - K2 := C_{N−2d}(C_{N−d} + 1)
  - K3 := C_{3d,d} K1
  - K4 := 2 C_{N,N−2d} K2
  - K5 := 2 C_{3d,N−2d} K2

- *The parameter.*
  - θ0 := max{ 16, 16 η_G⁻², (4K3/δ_G)^{1/(6d+2)}, 1 + K4, C1 K5 + ½ C2 K3² }.
  - II.G takes η_G ≤ 1, so the entry 16 is implied by the second; III.K takes η_G := 1.

- *Conclusion.* ε := θ0^−α satisfies the conclusion of the theorem: if ‖Φ(0)‖_{2d} < ε, there is u ∈ B^∞_{η_G/2}
  with |u|_{3d} < δ_G and Φ(u) = 0.

*Proof.* These are the conditions on θ0 imposed in the theorem's proof (PART-II-G-NASHMOSER.md:101-155), collected.

- (2.6) is used with γ = ½ and γ = 6d+2, which needs θ0^{1/4} ≥ 2, so θ0 ≥ 16. This also gives θ0 ≥ 2, θ_j ≥ 1 (so
  ‖e_j‖_{2d} ≤ 1 and θ_j^β ≥ 1) and θ > 1 for S_θ, which the proof uses without comment.

- *Supports.* These need θ0 ≥ 16 η_G⁻².

- *(a_{j+1}).* This needs 2K3 θ0^{−6d−2} ≤ ½δ_G.

- *(c_{j+1}).* This needs θ0 ≥ 1 + K4.

- *(b_{j+1}).* This needs θ0 ≥ C1 K5 + ½ C2 K3².

- *The K's.* They are the constants of the bounds on v_j and w_j there:
  - |v_j|_d ≤ C_d(1+δ_G)‖e_j‖_{2d};
  - |v_j|_{N−2d} ≤ C_{N−2d}(C_{N−d}(1+|u_j|_N) + |u_j|_N) ≤ K2(1+|u_j|_N);
  - the three smoothing bounds (2.8), with |v_j|_{N−2d} ≤ 2K2 θ_j^β.

- *Nothing else.* The paragraphs on the higher norms and on convergence (PART-II-G-NASHMOSER.md:157-173) put conditions
  on j only. Every condition above is a lower bound on θ0, so the max meets them all.

The proof sets ε := θ0^−α. Verifier 155 checked the identities (2.5), 5d − N + β = −κα − 1, α − 2d = 6d+2 and
3d ≤ N − 2d for d = 1, ..., 7, and (2.6) at θ0 = 16 (D338). □

**Proposition 2.2 (the chain to λ1 and δ).**

- *δ.* Part VII section 4 puts δ := ε/2, where ε is the data threshold of III.K Theorem 4.3 as run there. It is
  ε = ε(ε_m, ε_t): the constants below are those of the spaces at the α chosen in VI.C row w2
  (PART-VII-ASSEMBLY.md:397-402).

- *ε.* Any ε with
  - ε ≤ min{ 1, ε_NM / A_2d, ε_dat, ε_G }
  - is admissible, with these quantities:
    - ε_NM: Proposition 2.1's threshold for III.K's spaces, with η_G := 1 and δ_G := min(δ_K, ε_m).
    - δ_K: the radius in U. It is the least of the smallness of U that III.K takes: the definition of Ψ and Lemma
      2.2 (PART-III-K-NONLINEAR.md:214, 219), Lemma 2.3's ε_0 (273), and Proposition 4.2's (457-458). It is also the
      least of the smallness of |S| that III.K takes, turned into a bound on U by |S| ≤ |U|_{3d}: III.K Lemma 1.1 (d)
      (77, 90), Proposition 1.2's C|S| ≤ ½c_ν and its use of II.C Lemma 3.2 (2) (114, 158), and Lemma 2.3's supports
      paragraph (320).
    - A_2d: III.K Lemma 2.2 (d)'s constant, ‖P5(Ψ(0))‖_{F^{2d}} ≤ A_2d ‖(γ̃, k̃)‖_{H^{2d+k''}}.
    - ε_dat: the least of the smallness of the data that III.K takes: Proposition 1.2 (158, 184-186, the local
      quasilinear theory), Lemma 2.3 (281, the base point small in III.I's class; 305-309, the boost defect e_S
      small enough for the elimination; 320, G_S − g_b0 small), and Proposition 4.2 (457-458, h_{−S} small).
    - ε_G: the threshold of Part VII Proposition 3.2's run of II.G on G-fixed spaces. It is Proposition 2.1 with the
      constants of the G-sup norms, so it carries the constants of their equivalence with the original norms
      (PART-VII-ASSEMBLY.md:369-371, 402-404).
  - III.K Theorem 3.2's smallness paragraph bounds the constants once the data norm is at most 1 (III.K:410-411).
    Lemma 2.3 needs more: the data below its thresholds, which are in ε_dat. That is a looseness of the paragraph's
    wording, not a gap in the theorem, which asks only for some ε; it is why the "1" alone does not suffice.

- *λ1.* The order of choices is k := d1 + 5, then R, then c0 and Ω', then J := k + 5, then λ1
  (PART-VII-ASSEMBLY.md:404-405).
  - Lemma 1.1 at that J gives C_J and a threshold λ_1.1 together (PART-VII-ASSEMBLY.md:106).
  - Corollary 2.3's C_R depends on C_J and R, and is the largest of its three constants (PART-VII-ASSEMBLY.md:258-266).
  - Any λ1 with λ1 ≤ λ_1.1, C_R λ1 ≤ η_gl (the gluing's smallness, Part VII Proposition 2.2) and C_R λ1 < ε/2 is
    admissible; for instance λ1 := min(λ_1.1, η_gl/C_R, ε/(4C_R)). Theorem 0.2 then holds for every 0 < λ ≤ λ1.

*Proof.* This is a reading of Part VII section 4 (PART-VII-ASSEMBLY.md:395-410): "λ1 so small that C_R λ1 < ½ε. Put
δ := ½ε". The thresholds it takes:

- *For ε.* III.K Theorem 4.3's ε as run there. Its smallness conditions are those listed under δ_K and ε_dat, each
  read at the cited line, and Theorem 3.2's: "‖P5(Ψ(0))‖_{F^{2d}_ex} < ε_NM for data small in H^{d1}" through Lemma
  2.2 (d) (III.K:410-413). Part VII section 4 replaces II.G's radius by min(δ_G, ε_m), and in (i) adds the threshold
  of Proposition 3.2's run.

- *For λ1.* Corollary 2.3's "for λ small" is η ≤ η_gl against Proposition 2.2 (PART-VII-ASSEMBLY.md:193-197, 258), and
  Lemma 1.1 has its own threshold. The other conditions in Part VII section 2 are on R and η_gl, not on λ.

Each condition is an upper bound on the data norm, on U or on λ, so the minima meet them all. The list of III.K's
conditions is the result of reading every occurrence of "small", "sufficient" and "below" in PART-III-K-NONLINEAR.md
(D338); the first draft missed three of them (verifier 155's M1). □

**What is not explicit.** In Propositions 2.1-2.2, every quantity is a formula except:

- the loss d, with k'' and d1 = N + k''. III.J''' gives d only as the sum of the losses of the parts it composes
  (PART-III-J3-TAME.md:288-292), and the sum has not been added up; so α = 8d+2 and N = 21d+6 are not yet numbers;

- the tame constants C_k (k ≤ N), C1 and C2 of III.K's map and right inverses, and the smoothing constants C_{s,t};

- the parts of δ_K and of ε_dat, and A_2d;

- the constants of the equivalence of the G-sup norms in ε_G;

- the record's C_J and λ_1.1 at order J;

- the gluing's η_gl and C_R.

The smoothing constants, the Moser parts of the map's estimates and c_ν (III.K:114) are explicit in principle. The rest
are where section 3's arguments enter:

- the map's constants, through III.J's inverse operators N_ι+(z)⁻¹ and S_λ0 (PART-III-J-PARAM.md:95, 225-232) and
  through h_{−S} (the local theory, III.K:184-186);

- the right inverses' constants and δ_K, through the linear theory;

- η_gl and C_R, through [CD03]'s implicit function theorem (E5).

## 3. Where the numbers are lost: four kinds of argument

A text count over proof5's 75 PART files (D338, case-insensitive) finds contradiction 19 times, compactness 44,
Rellich 5, compact inclusion or embedding 5, Fredholm 74 and subsequence 28, in 35 files. (D337's count of 51 and 36 was
not reproducible.) Read in context, the arguments that produce a constant without a number are of four kinds.

- **N1: a compact error removed by injectivity.**
  - *The pattern.* ‖u‖ ≤ C(‖Pu‖ + ‖u‖_weak) with a compact inclusion, and a trivial kernel, gives ‖u‖ ≤ C′‖Pu‖ by
    contradiction.
  - *Examples.* PART-I-C-LOWENERGY.md:494-498 (zero energy), the same in I.A and II.F.
  - *What it hides.* C′ hides a lower bound for P on the complement of a finite-dimensional space.

- **N2: uniformity in parameters by sequences.**
  - *The pattern.* An estimate at each point of a compact parameter set, made uniform by contradiction with
    (σ_j, b_j) → (σ_*, b_*).
  - *Examples.* PART-III-H3-UNIFORM.md:189 (I.A Lemma 3.1 for c/2 ≤ |σ| ≤ C0), PART-I-C-LOWENERGY.md:686 and 1421
    (local constancy of the index; Corollary 5.2 (b)), PART-II-F-IOTA.md:1063 and 1329.
  - *What it hides.* The modulus of continuity in the parameters, and a finite cover.

- **N3: semiclassical absorption at trapping.**
  - *The pattern.* The high-energy estimates near the trapped set close by contradiction against the dynamics.
  - *Examples.* PART-I-B-HIGHENERGY.md:2047-2052 (Propositions 6.4 and 6.7 (a)), made uniform in b by the same device.
  - *What it hides.* The constant of the trapping estimate.

- **N4: finite covers of compact parameter sets.**
  - *The pattern.* "By compactness of 𝓑, finitely many suffice" (PART-I-B-HIGHENERGY.md:2047).
  - *Why it is minor.* It is effective once each local neighbourhood has an explicit radius.

Geometric compactness used only to show that a set is closed or a curve extends (for instance PART-II-F-IOTA.md:259)
produces no constant and needs nothing.

**The ledger (E1, D338).** EFFECTIVE-LEDGER.tsv reads each occurrence in context and classes the site. Its columns are
file, line, class, the statement it serves, the constant it hides, and an excerpt (an ASCII rendering of the LaTeX).

| class | meaning | rows |
|---|---|---|
| N1 | compact error removed by injectivity | 6 |
| N2 | uniformity in parameters by sequences | 15 |
| N3 | semiclassical absorption at trapping | 1 |
| N4 | finite cover of a compact parameter set | 13 |
| F | the Fredholm property used qualitatively (index, meromorphy), no constant | 41 |
| G | geometric or weak compactness, no constant | 37 |
| X | a mention, heading, citation or continuation of a row above | 52 |

- *The 35 N-rows.* They lie mostly in the linear theory's foundations: I.B 7, I.C 5, I.A 5, II.F 3, III.H''' 2, and
  one or two in each of nine other parts.

- *How it was built, and what is checked.* A reading pass by an extraction agent (D338) built it. A script then checked
  that each of the 165 rows names an existing file and has one of the words above within two lines of the cited line;
  all do. The classes are a reading, not checked row by row, and the ledger is not claimed complete.

## 4. The effective replacements

| kind | replacement | where the number comes from | READ |
|---|---|---|---|
| N1 | verified inverse norm: finite-dimensional part by interval linear algebra, remainder by explicit projection errors and a Neumann series | at Tangherlini the operators separate over the harmonics of S³: low harmonics by validated ODE integration (Taylor models), high harmonics by explicit coercivity | Sekine–Nakao–Oishi Thm 2.1, Lemma 2.2; Goldstein–Jejjala |
| N2 | Neumann series about certified base points on an explicit finite grid, with Lipschitz bounds of the operators in (σ, b) | the base bounds of N1 at the grid points, and explicit derivatives of the explicit Myers–Perry metrics | Ferreira–Leuştean–Pinto (Heine–Borel in place of sequences) |
| N3 | an explicit trapping estimate at Tangherlini by physical-space multipliers (separable dynamics, explicit photon sphere), carried to nearby b by N2 | explicit multiplier positivity, of the kind the record already computes in five dimensions (rungs5.py's Sturm count) | Datchev–Jin (expect large constants) |
| N4 | explicit radii from N2 | as N2 | as N2 |

## 5. The programme, and its size

- **E1. The ledger (done, D338).** Every site of N1-N4 in proof5, with the constant it hides (EFFECTIVE-LEDGER.tsv,
  section 3).

- **E1'. The loss d.** Add up III.J''''s losses part by part, with k'' and d1, so that α and N become numbers.

- **E2. Tangherlini, mode by mode.**
  - *The problem.* The operators of III.D, III.F and IV at b0, separated over the harmonics of S³, give radial ODE
    families with a regular singular point at the horizon and an irregular one at infinity, as in Goldstein–Jejjala.
  - *What is needed.* Certified lower bounds at each harmonic up to an explicit cut-off, and explicit coercivity
    beyond it.
  - *What it replaces.* The N1 constants at b0.

- **E3. Near b0.**
  - *What is needed.* Explicit Lipschitz bounds of the Myers–Perry operators in b, and the Neumann series.
  - *What it replaces.* The N2 and N4 constants.

- **E4. High energy.** An explicit trapping estimate at Tangherlini (N3).

- **E5. The data side.**
  - *The record's threshold λ_1.1 and C_J at order J.* Its proof is energy estimates on a compact domain; whether it
    contains arguments of kinds N1-N4 is still to be checked (E1 covered proof5 only).
  - *The gluing's η_gl and C_R.* These come through [CD03]'s implicit function theorem, whose linearised operator's
    invertibility is an N1 step.
  - *ε_dat.* Proposition 1.2's part is the local quasilinear theory on a compact domain (energy estimates and Cauchy
    stability), explicit in principle; Lemma 2.3's and Proposition 4.2's parts go through III.I's class and the right
    inverses (E2-E4).
  - *ε_G.* The norm-equivalence constants of a compact group acting smoothly: explicit once the action's derivatives
    are bounded.

- **E6. Assemble.** Feed the numbers through section 2's formulas.

*Size.* E2-E4 rewrite, with numbers, the parts of the linear theory that the right inverses and III.J's inverse
operators rest on (Parts I, II.F, III.D-III.H'', III.J). That is comparable to the original write-out of those parts,
plus certified computation. It is not one session's work. E1 is done; E1' is bookkeeping; E2 at one operator is the
first real test.

## 6. Sources

- READ:
  - Sekine, Nakao, Oishi, arXiv:1910.00759v1 (abstract; pp. 3, 5-6);
  - Ferreira, Leuştean, Pinto, arXiv:1810.01508v4 (abstract; pp. 1-2);
  - Goldstein, Jejjala, arXiv:2609.21797v2 (abstract; pp. 2, 9-15, 33).

- Through the search index only: Datchev–Jin (title, abstract).

- The proof: PART-II-G-NASHMOSER.md:101-173; PART-III-K-NONLINEAR.md sections 1-4; PART-III-J3-TAME.md:288-292;
  PART-III-J-PARAM.md:95, 225-232; PART-VII-ASSEMBLY.md:104-108, 256-266, 366-371 and 395-410; the sites of section 3
  and EFFECTIVE-LEDGER.tsv.

- Verifier 155 (D338), read of section 2: Proposition 2.1 confirmed; M1 (three smallness thresholds missing), M2 (the
  loss d, ε_G's constants, the map's inverse operators), m1-m5 and n1-n6, all seated in this revision.
