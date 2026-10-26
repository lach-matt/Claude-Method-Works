# proof5: the five-dimensional proof, written out in full

M asked that the remaining caveat be closed by proof (D184). The caveat is that the record's route to Theorem 4 rests
on deductions at proof level, read by independent verifiers, and on censuses whose completeness is evidenced by two
methods, not proved. This directory holds the write-out that replaces them. Each section of the companion papers that
the route uses is proved at n = 4 on the record's bundles, self-contained, from statements READ at source that hold in
every dimension. Once a part is written and verified, the census and the deductions that covered it are no longer
needed for it.

Labels as in the record. A part is **written** when its proofs are complete on the page; **verified** when an
independent reader has checked it line by line and every finding is seated; **proved** only then. Theorem 4 stays
*deduced* until every part below is proved.

## The plan

| Part | Source | Content | Status |
|---|---|---|---|
| I.A | [Hin26c] 9.1-9.2 | bounded nonzero frequencies, Theorem 9.5, bundles, uniform in b | **proved** (D197) |
| I.B | [Hin26c] 9.3 | high energies, trapping with (5.9)'s conjugation, Theorem 9.16 | **proved** (D231) |
| I.C | [Hin26c] 9.4-9.6 | zero energy (9.36), tf operator (9.38), low energy (9.41), 9.39, 9.43 | **proved** (D194) |
| II.A | [Hin26c] 2-3 | compactifications, Lie algebras, e3b-calculus, embeddings, tame estimates | **proved** (D197) |
| II.A' | [Hin26c] 3.23-3.24, k = 0 | elliptic and propagation estimates, finite regularity | **proved** (D197) |
| II.B | [Hin26c] 4 | null-bicharacteristic dynamics of the stationary model | verified (D197) |
| II.C | [Hin26c] 5, 6 but 6.3 | operator classes, admissibility, time function, order functions | verified (D200); the D226 remark confirmed (D229) |
| II.C' | [Hin26c] 6.3 | stable and unstable trapped sets of perturbed metrics | verified (D201) |
| II.D | [Hin26c] 7.1 | microlocal regularity: radial sets, the trapped set, the global estimate | verified (D204) |
| II.D' | [Hin26c] 7.2 | b-regularity and estimates tame in it | verified (D206) |
| II.E | [Hin26c] 8 | energy estimates on slabs and in the interior; the global estimate | verified (D207) |
| II.F | [Hin26c] 10 | the normal operator at iota+; forward solutions of P_0 on e3b-spaces | **proved** (D216) |
| II.F' | [Hin26c] 11 | forward solutions of wave-type operators, tame estimates | **proved** (D216) |
| II.G | [Hin26c] 12 | the Nash-Moser theorem, smoothing operators, tame bounds | **proved** (D216) |
| II.G' | [Hin26c] 13 | improving decay: Fourier transforms, resolvent bounds, the radiation field | **proved** (D217) |
| III.A | [Hin26] 2.1-2.3 | technical prerequisites: partial polyhomogeneity, integration along b-fields | proved (D231) |
| III.A' | [Hin26] 2.4 | harmonics on S^3; the Minkowski operators in the null splittings; indicial roots by type | verified (D221) |
| III.B | [Hin26] 3-4 | the Myers-Perry family on M, time functions, boosts, the gauge-fixed Einstein equation | proved (D221) |
| III.D | [Hin26] 6-6.3 | the gauge potential operator: structure, Minkowski model, indicial roots, horizon threshold, trapping, high energies, mode stability away from zero, tf-admissibility | proved (D229) |
| III.D' | [Hin26] 6.4, Lemma 6.13 | the gauge potential operator at zero energy: kernel and cokernel, pairings, mode stability at every frequency, the zero energy inverse | proved (D231) |
| III.D'' | [Hin26] 6.5.1 | zero energy states from the Minkowski symmetries; Lemma 6.14's comparisons | proved (D231) |
| III.D''' | [Hin26] 6.5.2 | generalized zero energy states of the gauge potential operator | **proved** (D235) |
| III.E | [Hin26] 7-7.2 (to Proposition 7.3) | the constraint propagation operator at zero energy: invertibility of its adjoint, indicial roots, the large dual states | **proved** (D235) |
| III.E' | [Hin26] 7.2.1 | the vector type 1 dual states: the deformation tensor of a rotation (exact, by equivariance) and the states' dependence on the bracket with the spin | proved (D231: read in full, no findings) |
| III.F | [Hin26] 8 to 8.1 | the linearised gauge-fixed Einstein operator: structure, the spectrum of the model's endomorphism, the bound at the trapped set | **proved** (D235) |
| III.F' | [Hin26] 8.2-8.3 | the linearised operator's indicial roots, the indicial solutions at 0, tf-admissibility, the inverse of the tf-normal operator on b-spaces | **proved** (D238: the ninety-eighth verifier read the D235 repairs, correct) |
| III.F'' | [Hin26] 8.4 (Proposition 8.8) | mode stability of the linearised operator away from zero frequency; its horizon threshold | **proved** (D238: the D235 repairs read, correct; two nits seated) |
| III.F''' | [Hin26] 8.4 (Propositions 8.9, 8.11, Remark 8.10, Corollary 8.13) | the zero energy kernel and cokernel of the linearised operator; stationary solutions on Tangherlini | **proved** (D238: the D235 repairs read, correct) |
| III.F'''' | [Hin26] 8.4-8.5 (Lemmas 8.12, 8.15, Proposition 8.14) | the zero energy pairings, reduced to infinity; the physical states at -2 | **proved** (D238: the D235 repairs read, correct; two nits seated) |
| III.G | [Hin26] 9.1 (Proposition 9.2) | the spectral family at future timelike infinity: the Fredholm property across the light cone, b-regularity there, invertibility for Re λ < 2, finite meromorphy | **proved** (D240: the ninety-ninth verifier read the D238 repairs, correct) |
| III.G' | [Hin26] 9.1 (Definitions 9.3, 9.6, Proposition 9.4, Remark 9.7) | the ι⁺-normal operator: its inverse, the asymptotics at I⁺ and K⁺, finite regularity, the boundary spectrum | **proved** (D241: the hundredth verifier read the D240 repairs, correct; one nit seated) |
| III.G'' | [Hin26] 9.1.1-9.1.2 (Definitions 9.8, 9.10, Propositions 9.9, 9.11, Corollary 9.12) | formal solutions at K⁺ from the zero energy states, the expansion at K⁺, grafting into spacetime; the window ℓ_K < 3 | proved (D244; verifier 100's repairs read by verifier 101, one nit seated) |
| III.C | [Hin26] 5.1-5.3 | metric perturbations at n = 4; the linearised operator at null infinity: constant lower-triangular matrix, perturbation half an order lower; forward mapping | proved (D245; verifier 101's repairs read by verifier 102, three nits seated) |
| III.G''' | [Hin26] 9.1.3 (Lemmas 9.13-9.14, Propositions 9.15, 9.22, Corollary 9.18, Lemma 9.21) | the iota+-normal operator on partially polyhomogeneous inputs: one exceptional exponent, the least incoming pole 3/2 + (1 - e_Ups) gam_Ups; quasi-homogeneous solutions; resonant states | proved (D247; verified D245 with four minor findings and eleven nits) |
| III.G'''' | [Hin26] 9.2 (Definitions 9.25, 9.29, Lemma 9.26, Propositions 9.30, 9.35) | the tf-normal operator: formal solutions at ztf, the expansion of its inverse at r-hat = 0 over the window (-3, 0], grafting into the low-energy space, conormal sources; Prop 9.35's first step repaired | proved (D249; verified D247 with three minor findings and eight nits) |
| III.H | [Hin26] 10.1 (Lemma 10.4, (10.24), Propositions 10.6-10.7, section 10.1.3) | the augmented low-energy resolvent: cut-off states, the augmented zero energy operator, uniform low-energy estimates with sigma-dependent columns; mode stability near b0 at low frequency | proved (D252; verified D249 with two minor findings and six nits) |
| III.H' | [Hin26] 10.2 (Theorem 10.1, Lemmas 10.9-10.13) | 2-admissibility of L_b: the contour representation, high and low frequencies, the zero energy contributions integrated twice in t_*; sf-loss 0 at n = 4 | proved (D256; verified D252, D254) |
| III.I | [Hin26] 11 opening, 11.1 (Definition 11.3, Lemma 11.5, Propositions 11.6, 11.8, Corollaries 11.9-11.10, Theorem 11.12) | the dynamical linearised operator: perturbation classes, the e3b class, structure in the forward cone, forward mapping, admissibility with p_0 = p~_1 = 0, forward solutions at b0 with sf-loss 0; the orders of II.F' in O_c | proved (D258: verifier 108 read the D256 repairs; verified D254, D256) |
| III.I' | [Hin26] 11.2 (Propositions 11.14, 11.16, Lemma 11.15) | partial polyhomogeneity at null infinity without loss at future timelike infinity; formal solutions at null infinity, one exceptional term | proved (D258: verifier 108 read the D256 repairs; verified D256) |
| III.I'' | [Hin26] 11.3 (Proposition 11.17, Lemmas 11.18-11.19) | almost linear bounds: integration of d_t* with a moment condition, the three frequency ranges, forward solutions improved at K+ with the iota+-weight kept at min(alpha_+, 3/2, min Re E_+) | proved (D259: verifier 109 read the D258 repairs; verified D258) |
| III.I''' | [Hin26] 11.4.1 (Proposition 11.20, Lemma 11.21) | the boost parameter: the forward solution is a cut-off generalised boost state plus a remainder of K+-weight alpha_K - 2; zero energy inverted by the augmented operator, no iota+ step at n = 4 | proved (D261: verifier 110 read the D259 repairs; verified D259) |
| III.I'''' | [Hin26] 11.4.2 (Definitions 11.23, 11.25, Lemmas 11.24, 11.28, Proposition 11.30, (11.95)) | undoing the boost: correction terms, the boost identity (11.78b), the augmented operator, its parameter derivative, the boost parameter map invertible; no logarithms, no splitting of the source, the generalised state re-centred at n = 4 | proved (D263: verifier 111 read the D261 repairs; verified D261) |
| III.I''''' | [Hin26] 11.5 (Proposition 11.32) | almost boundedness: with the boost eliminated, K+-weight alpha_K - 2 for every alpha_K < 2, by rounds of III.I''''s argument with a step at iota+ from 3/2 + (1 - e_Ups) gam_Ups; no Lemma 11.33, no Step 3.2 at n = 4 | proved (D266: verifier 112 read the D263 repairs; verified D263) |
| III.I'''''' | [Hin26] 11.6.1 (Proposition 11.34) | extraction of the parameters: for sources of K+-weight alpha_K in (2, 5/2), u = chi_K g-dot(b-dot) + chi_K h(S^(0)_1) + a remainder decaying at K+; no logarithmic centre-of-mass term at n = 4; the tf-improvement by III.G'''' Proposition 5.1 | proved (D268: verifier 113 read the D266 repairs; verified D266) |
| III.I''''''' | [Hin26] 11.6.2 (Definitions 11.37, 11.40, 11.42, 11.44, Lemmas 11.38, 11.41, 11.43, 11.45, Corollary 11.46) | undoing the parameter changes: corrections, the operator P_2 with parameters (S, b - b_0, S^(0)_1), their elimination; the centre-of-mass shift needs a translated exterior background at n = 4 | proved (D269: verifier 114 read the D268 repairs; verified D268) |
| III.I'''''''' | [Hin26] 11.7 (Definitions 11.47-11.48, Lemma 11.49, Proposition 11.51) | decaying centre-of-mass motions: corrections #3 with generalised gauge 1-forms to order 4; the motions read off from the s1 row of the iota+ step; K+-weight alpha - 2 for alpha < min(a_K, 3), almost t_*^-1 | proved (D271: verifier 115 read the D269 repairs; verified D269) |
| III.I''''''''' | [Hin26] 11.8 to Lemma 11.57 (Definitions 11.55-11.56, Lemma 11.57) | correction terms #4 for six row types (s1, v1, s0, s2 and the class roots c0, c1; gauge towers of length 4, 3, 4, 3, 2, 2), the operator P_4 with every modification parameter, and its exact linearisation f^nu = L m_nu + r^nu with a remainder of iota+-weight above 5 + eps_+ and no index set | verified (D271; no major, two minor findings and seven nits seated, to be read) |
| III.I'''''''''' | [Hin26] Theorem 11.59, Parts 1-3, first half (with Remark 11.62) | the parameter exponents fixed (an exponent set Lambda, log orders growing with the real part, the gap (G)), the towers of III.G'' as delta*-images and the uniqueness of row expansions, forward Fourier tails, and the spacetime phase: the iota+-terms of u-exponent below 2 solved up to the K+-order alpha <= 4 + eps_K under (C5), their K+-terms the rows | written (D272) |
| III.C', III.I'''''''''-III.J | [Hin26] 5.4-5.7, 11.8-12 | exterior stability and partial polyhomogeneity; decay | to do |
| IV | [Hin26a] 5.2, 6; [Hin23a] 3 | constraint damping; the exterior estimates | to do |
| V | [CD03], [HHV21] | gluing; the nonlinear step | to do |
| VI | the record's computed inputs | that the record's operators satisfy each part's hypotheses | to do |
| VII | assembly | Theorem 4 from Parts I-VI | to do |

Each part states its hypotheses for a class of operators. Part VI checks them for the record's operators, using the
record's computed items (for Part I: 10.19, 10.36, 10.60 and 10.79) and turning each into a proof.

## Part I.A

`PART-I-SPECTRAL.md`. [Hin26c] Theorem 9.5 at n = 4, for operators on a trivial bundle of any rank, is proved from
the scattering calculus of [HJS] (Hassell-Jia-Sussman, arXiv:2604.18956, every n, with bundles and variable orders).
It is proved with constants uniform in the operator (Theorem 8.1), via a single regularised positive commutator lemma
(section 3), three radial estimates (section 4), propagation and elliptic estimates (section 5), and estimates at the
artificial boundary at every order, energy method included (section 6). Section 9 lists what the write-out found. One
item is a sign slip in [Hin26c] (9.45), repaired without changing the statement (Lemma 4.8; seated as D184).

The seventy-fourth verifier read Part I.A line by line (D186): two major findings -- Lemma 3.1 paired the commutator with
$u$ where an absorbing term of top order makes the pairing undefined, now paired only with Schwartz approximants; and
variable regularity orders lay outside the calculus READ, so Theorem 7.2 is now stated for a constant regularity order --
and seven minor ones, all seated. Its repairs are read next; Part I.A is labelled proved only then.

The seventy-fifth verifier read those repairs (D187) and confirmed each. It found two minor gaps, both in the variant of
Remark 3.3 that Proposition 5.2 (ii) uses: the limit of the main term was taken without saying why the bound survives it,
now by weak lower semicontinuity of the norm on a bounded sequence; and Step 1 used a commutator with $T_t$ it had not
bounded, now avoided by splitting $\check A_\epsilon P w_t$ into three terms each bounded directly. Six nits were seated
with them. Part I.A is labelled proved once the next reader, who reads Part I.B, has checked these two repairs.

The seventy-sixth verifier, reading Part I.B, checked both repairs and confirmed them (D189). Part I.A was then
**proved**: written, read line by line, every finding seated and every repair read.

The seventy-ninth verifier, reading Part II.A$'$, which copied them, found that the cut-offs of Proposition 5.2 are not
equal to 1 on the curve: $\psi$ is even, so $\psi(-z/\delta)$ vanishes for $z\ge\delta$. They are now one-sided, and the
self-adjointness of the commutant, which the identity (3.4) needs, is stated in Proposition 5.2 (D195). Part I.A returns
to verified until the eightieth verifier has read the repair.

The eightieth verifier read the repair and confirmed it (D196). It found, pre-existing, that the commutant of Proposition
4.9 was not stated to be $h$-symmetrised, as Lemma 3.1 (i) requires; Proposition 4.9 now says so, as section 4.3 does
(D196). The eighty-first verifier confirmed it (D197), and Part I.A is **proved** again.

## Part I.B

`PART-I-B-HIGHENERGY.md`. [Hin26c] Theorem 9.16 at n = 4, for operators on a trivial bundle of any rank and uniformly in
the operator. Section 2 proves the semiclassical scattering calculus with matrix-valued symbols and variable orders, for
which no text could be READ. The estimates follow one positive commutator scheme without regularisation (section 3):
elliptic and propagation estimates with flow boxes depending on $z$ (section 4); one radial lemma for the horizon and for
the incoming and outgoing radial sets, with b-regularity at the outgoing one (section 5); the trapped set, through
matrix-valued defect measures, an entire complex absorption and a three lines lemma (section 6); and an energy estimate
at the artificial boundary for every $\mathrm{Im}\,z\ge0$ (section 7). Section 8 assembles Theorem 1.3 and section 10
lists what the write-out found: three slips of the pen in [Hin26c] section 9.3, the diagonal sign of (9.45) again in
(9.77), and a threshold: [Hin26c]'s $\gamma_-$ divides by the least value of $q$ on the trapped set, which justifies the
interpolation only when $q$ is constant there, so Part I.B defines $\gamma_\pm$ as the exact thresholds the proof uses
and assumes $\gamma_-<0$, which Theorem 9.16 (1) needs at real frequencies.

The seventy-sixth verifier read Part I.B line by line (D189). It found the architecture sound and every computation it
recomputed correct, and confirmed (F1)-(F9). One major finding: the regularity step at the artificial boundary
(Proposition 7.2) left an error term on a larger set than the left side controls, at the same regularity, and used $W\in
H^s$ before proving it; now $W\in H^s$ at each $h$ by uniqueness, and the new Corollary 4.6$'$ lowers all orders in the
iteration, so the error term is $\|W\|_{L^2}$. Nine minor ones, among them (H8), stated with the local trapped sets,
which no flow satisfies, now with the global ones and a no-return clause that keeps the chain of section 8.2 acyclic; and
the auxiliary absorption of Theorem 6.8, whose sign was wrong for $z_0 = -1$. All are seated, with (F10), a range in
[Hin26c] Theorem 9.28 (2). Its repairs are read with Part I.C.

The seventy-seventh verifier, reading Part I.C, read these repairs and confirmed each (D191). It asked for one more
clause, in Proposition 6.4, Step 2: $\delta_1$ is chosen so that $\Gamma(\delta_1)$ lies in $\mathrm{Ell}_h(B_1)$ too, as
the step needs; seated (D191). The seventy-eighth verifier, reading Part II.A, checked that clause and confirmed it
(D194). Part I.B is **proved**. It has since gained Lemma 6.0 (D226), the conjugation that lets the inner product at the
trapped set depend on the covector, which the ninety-fourth verifier confirmed (D229), seating two minor findings
(Proposition 6.4 for the conjugated operator also uses Proposition 4.5, Corollary 4.6 and Theorem 2.4, by Remark 4.7;
the symbol in Proposition 6.1 taken at $z$) and two nits: verified; the ninety-fifth verifier read the repairs (D231),
and Part I.B is **proved**.

## Part I.C

`PART-I-C-LOWENERGY.md`. [Hin26c] sections 9.4-9.6 at n = 4, for operators on a trivial bundle of any rank and uniformly
in the operator: the zero energy operator (Theorem 3.1, [Hin26c] Theorem 9.36), the transition face normal operator
(Theorem 4.3, Theorem 9.38), tf-admissibility and its consequences (Corollary 5.2, Corollary 9.39), the asymptotically
Minkowski case (Proposition 5.3, Proposition 9.40, with the weights $(0,2)$), the uniform low-energy estimates (Theorem
6.4, Theorem 9.41 with Remark 9.42's augmentations) and the index 0 of the zero energy operator (Corollary 6.6, Corollary
9.43). Section 2 proves the b-analysis used at the two conic ends. tf-admissibility is stated on the Fredholm problem of
the transition face (Definition 5.1), which the source's definition implies given its (9.115); the asymptotically
Minkowski case is verified directly, with Hankel functions READ in [DLMF]. The low-energy theorem is proved on a norm
glued from the zero energy and transition face norms (Definition 6.1), from the two model estimates alone, as in the
source, and with an adjoint estimate that the source does not state. Section 8 lists seven findings against the source.
None changes a statement; one (F6) is a gap: the proof of Corollary 9.43 infers the invertibility of an augmented
operator from an estimate that gives only injectivity, and the adjoint estimate of Theorem 6.4 closes it. Weaker than the
source, and said so in Remark 6.7: the smallness in Theorem 6.4 may depend on the b-regularity order, and uniformity in
the weight is not proved. The gap hypothesis is labelled (G), since (H6)-(H8) are Part I.B's.

The seventy-seventh verifier read Part I.C line by line (D191). No major finding. One statement gap: Theorem 4.3 (4) was
not stated uniform in $\theta$, which Corollary 5.2 (b) and Theorem 6.4 use; it is now stated and proved. Nine minor
findings, all seated, among them the Mellin transform at negative orders (now by density), the charts of Lemma 6.2 (a)
(dilations, not an inversion), the a priori regularity behind the adjoint absorption of Theorem 6.4 (2), Lemma 5.4 at
$\theta = \pi$, and the reworded proof of Lemma 2.5, in which no commutator arises. It confirmed (F1)-(F7), recomputing
(F4) and the conjugation of the tf operator at $n = 3,4,5$. The seventy-eighth verifier, reading Part II.A, read all ten
repairs and confirmed each (D194); the notation of Proposition 5.3 (iii) was then aligned with (ii). Part I.C is
**proved**.

## Part II.A

`PART-II-A-SETUP.md`. [Hin26c] sections 2-3 at n = 4: the compactified spacetime and its b-, 3b-, eb- and e3b-structures
with the commutator lemmas behind b-regularity (sections 1-2); the scaled bounded geometry calculus of [SBG] (Hintz,
Commun. AMS 6 (2026), arXiv:2408.06651), READ in eleven statements that hold in every dimension (section 3); the
e3b-calculus, its unit cells on $\mathbb S^3$ and its spaces (section 4); the Fourier transform near $K^+$ and the Mellin
transform at $\iota^+$, with the weights of $n = 4$ (sections 5-6); supported and extendible spaces (section 7);
functions and operators of finite regularity, multiplication and pseudolocality, and Sobolev embedding (section 8); and
the elliptic and real principal type estimates with b-regularity and their tame versions (section 9). The dimension
enters through the density only: the weights $(2(\alpha_I+2),\alpha_++\frac52,\alpha_K+\frac12)$ replace
$(2(\alpha_I+\frac32),\alpha_++2,\alpha_K+\frac12)$, and no regularity threshold changes, as $3>\frac52$. Section 10
lists the findings: two signs and a weight printed without its class (G1)-(G2), the tame estimates stated with an infimum
norm their proofs do not support (G3), now stated per representation, and slips in section 3.4 of the source, among them
$\mathsf s-m$ for $\mathsf s-m+1$ in (3.85) (G4), and the hypotheses of the real principal type estimate, too weak as the
source states them (G6)-(G7).

Two statements are standing inputs of this part: the elliptic and the real principal type estimates without b-regularity,
for coefficients of finite regularity and variable orders ((L3)-(L4), [Hin26c] Propositions 3.23-3.24 at $k = 0$). The
source cites them as standard. No text READ here states them: [SBG] does not treat propagation, [HJS] has constant
differential orders and no sharp Gårding inequality, and Hintz's paper with Sobolev coefficients (arXiv:1311.6859) has
constant orders. They are proved in Part II.A$'$. Part II.A is labelled proved only with it. The two further inputs the
source uses in the same way, multiplication by functions of finite regularity on variable-order spaces and its
pseudolocality, are proved in Part II.A itself (Lemma 8.5), from the calculus and the closed graph theorem.

The seventy-eighth verifier read Part II.A line by line (D194) and confirmed the D191 repairs of Parts I.B and I.C. Two
major findings, both in the propagation chain, are seated. The hypothesis of (L4) on the order, $\mathsf H\mathsf s\le0$
near $\mathrm{WF}'(B)\cap\mathrm{Char}(L)$ within $\mathrm{Char}(L)$ as the source states it, is too weak: $L = D_t$ in
one unit cell, with an order rising along the backward curve away from $\mathrm{WF}'(B)$, is a counterexample. It is the
gap Part II.A$'$ records as (G6), found independently, and (L4) and Propositions 9.2 and 9.9 now ask $\mathsf H\mathsf
s\le0$ on a neighbourhood of the backward segments. And the proof of Proposition 9.9 chose an operator near
$\mathrm{WF}'(B)$ whose wave front set must contain the segments; its operators are now chosen by an openness statement
(O), applied twice. Seven minor findings are seated: the quantifier order of (L3)-(L4), the localization of the operators
near the diagonal, the variable-order Plancherel theorem, READ in [SBG] (4.24a-b) as part of (S9), a false commutator
inclusion in the source's proof of its Lemma 2.11, the uniqueness of integral curves at the boundary faces and the
cut-offs away from $I^0\cup K^-$, a threshold in Lemma 8.5, and parametrices to finite order. So are the nits, among them
the angular term of (2.27). The verifier confirmed (G1)-(G5) and recomputed the metric, the weights of $n = 4$, the
Hankel asymptotics and the thresholds of Propositions 9.6 and 9.9. The wording of (S8) was aligned with [SBG] Definition
4.6 (D195), its reading of the theorem it cites stated (D196), and both confirmed by the eightieth and eighty-first
verifiers. With Part II.A$'$ proved, Part II.A is **proved** (D197).

## Part II.A$'$

`PART-II-A2-STANDARD.md`. The two standing inputs of Part II.A, proved: (L3) as Theorem 3.1 and (L4) as Theorem 5.4,
[Hin26c] Propositions 3.23-3.24 at $k = 0$, for operators whose coefficients have finite regularity, with variable orders
and constants locally uniform in the operator. The smooth calculus is (S1)-(S11) of Part II.A. Its operations are
continuous on Fréchet spaces of symbols, so each is bounded by finitely many seminorms, and the bounds pass to finite
regularity by mollification in the charts of the secondary structure and weak lower semicontinuity (section 2,
Proposition 2.4). The elliptic estimate follows from a parametrix of finite regularity (section 3). The propagation
estimate is a positive commutator argument along the exact Hamilton field of the operator, in flow-box coordinates of
finite regularity, so that every positivity is an exact square and no sharp Gårding inequality is used. The imaginary
part is absorbed by the large constant of the commutant (sections 4-5). Section 6 records (G6), the source's hypothesis
on the order, too weak, and (G7), classical principal symbols and the faces where the Hamilton field is continuous.
Written (D193) and aligned with the D194 repairs of Part II.A.

The seventy-ninth verifier read Part II.A$'$ line by line (D195) and confirmed every D194 repair of Part II.A and
(G6)-(G7) at source. One major finding: the class of symbols of finite regularity was too narrow, and the square-root
lemma false in it, so that the factor $z_\epsilon$ of the commutant and the parametrix of Lemma 4.2 were used with exact
orders that were not proved. The class now counts the logarithmic factor each derivative may carry, inside the class of
[SBG] Definition 4.6, whose operators act without loss. The square-root lemma is restated with one such factor per
derivative, proved by resolvent integrals, and shown sharp. Seven minor findings are seated: the identity (4.1) for a
commutant that is not self-adjoint, one-sided cut-offs, the regularity of the approximants in the pairing, nested sets in
Lemma 4.2, smooth operators in the patching, the injectivity of the perturbed flow box, and the convergence of the
factors in Proposition 2.4. So are the nits, among them the wording of (S8) in Part II.A.

The eightieth verifier read the D195 repairs line by line and confirmed each (D196): the class $C^{(M)}_\nu$ inside
[SBG]'s, the resolvent integrals of Lemma 2.5 and its sharpness, the exact orders of $z_\epsilon$ and of the parametrix,
and the seven minor repairs. No major finding. Two minor findings are seated: the support of $g_j$ in Lemma 4.2, now in
$U'_j\cap U_{j-1}$ with $\bar U_j\subset U'_j\cap U_{j-1}$, and the number $M$ of seminorms in Proposition 2.4, taken at
the orders raised by $2\delta$. So are six nits: the reading of [SBG] Theorem 3.44 as its Theorem 3.51 is stated as a
READ decision, in section 1.1 and in (S8) of Part II.A; Definition 1.3 names its coordinates; Lemma 2.5's counterexample
is given for every $\nu$; $\chi_\infty$ is supported in $\{\rho_\infty<1\}$; Lemma 2.6 is applied with $\delta/2$. The
eighty-first verifier read these repairs and confirmed each (D197); its one nit, on the example after Lemma 2.5, is
seated. Part II.A$'$ is **proved**.

## Part II.B

`PART-II-B-DYNAMICS.md`. [Hin26c] section 4 at $n = 4$: the radial sets, the horizon, the trapped set and the global
null-bicharacteristic dynamics of the stationary model in e3b-phase space. The source computes them from the Kerr metric.
Here the stationary model is any metric satisfying the hypotheses of Part I and (K1)-(K4): the metric is Minkowski to
order $r^{-2}$ outside a compact set (K1), and the trapped set is $r$-normally hyperbolic (K3). Over the interior of the
Kerr face the 3b-phase space is the stationary phase space with $\sigma$ conserved, and the map $\Phi_{z_0}$ carries the
semiclassical phase space of I.B at frequency sign $z_0$, flows included, onto the part of the 3b-cosphere bundle over
$K^+$ where $z_0\sigma\ge0$ (section 2), so that (H3), (H4), (H7) and (H8) of Part I give the dynamics there (Proposition
6.1, the source's 4.21). Near $\iota^+$, $\mathscr I^+$ and the corner the flows are solved in closed form (sections 3
and 7). Section 8 assembles the global dynamics (Proposition 8.1, the source's (4.72)) and the curves over the interior
(Proposition 8.2, the form of the source's Proposition 6.1). Section 9 records four slips of the source, none affecting a
statement: a word in the proof of Lemma 4.6 (2), the conic extension of $\partial W^+_{\mathrm{in}}$ and its vector field
in Lemma 4.6 (4), a constant in (4.18), and a gap in the proof of Lemma 4.20, which is not used here. Written (D196). The
eighty-first verifier read it line by line (D197), recomputed the Minkowski symbols, every closed-form flow, the
linearisations, the map $\Phi_{z_0}$ and the 3b-eb conversion, and confirmed (B1)-(B4) at source. One minor finding: the
statement of Lemma 3.3 (4) printed the source's vector field $r\partial_{t_*}-2r\partial_r$, which its proof corrects to
$2r\partial_{t_*}-r\partial_r$. Four nits: a citation of Lemma 2.1 for the Leibniz rule, $dr$ future (not past) timelike
inside the horizon, "within $\Sigma$" for the characteristic sets, and the two meanings each of $\rho_K$ and $\rho_+$.
All are seated (D197); they await the next reader.

## Part II.C

`PART-II-C-OPERATORS.md`. [Hin26c] section 5 and section 6 except Proposition 6.3, at $n = 4$. The stationary wave-type
operators are exactly the operators whose spectral families satisfy (H1), (H2) and (H6) of Part I (Lemma 1.2), with the
constant $\frac32 = \frac{n-1}2$ in place of the source's 1; for the tensor wave operators $S = 0$ in the coordinate
frame (Lemma 1.3). Lemma 1.4 places $P_0$ in the 3b- and e3b-calculi and gives its normal form at $\mathscr I^+$, with
$3+2S$ for the source's $2(1+S)$. Section 2 defines trapping and tf-admissibility through Part I's hypotheses, the
admissible orders, and $\aleph$-admissibility with the weight $\alpha_{\mathrm{sf}}+2$; the thresholds at $\partial K^+$
are those of Part I written in 3b-terms (Lemmas 2.5-2.6). Section 3 proves the time function $t^\flat_*$ with an explicit
gluing, and states the admissible wave-type operators and their normal form at $\mathscr I^+$. Section 4 proves
Proposition 6.1 for perturbed metrics, including its backward half, which the source states without proof. Section 5
proves Proposition 6.4, the order functions, by writing out the construction of [Hin23c] Appendix C that the source
cites, in this class; one localisation of that construction is not needed here. Findings (C1)-(C3) are slips of the
source: a power $x_I^{-2}\rho_+^{-2}$ for $x_I^2\rho_+^2$, "non-decreasing" for non-increasing in its Definition 5.11
(1), and the sign in its characterisation (6.5) of the future characteristic set. Written (D198). The eighty-second
verifier re-derived every computation and confirmed (C1)-(C3) at source. Its one minor finding: the proof of Lemma 1.3
stated the Minkowski metric in $(t_*,x)$ with $\delta_{ij}$ for $\delta_{ij}-\omega_i\omega_j$, and the argument for
$\omega^\mu\bar\Gamma_{\kappa\mu\nu} = 0$ rested on that form; the claim holds by the symmetry of
$(\partial_\nu\omega^\mu)\bar g_{\kappa\mu}$. Seven nits: the bounds of the smoothed minimum in Lemma 3.2 (it lies below
both functions, not between them), values in $[0,1]$ for the cut-offs of section 5.2, Lemma 4.1 (a) at $d_0 = 1$, the
bound $\epsilon_I^2<\frac1{10}$, Lemma 5.5 (c), the backward exit at $\{r = r_0\}$ in Proposition 4.2, and the region
$\{r\le R\}$ in (K1). All are seated (D200); they await the next reader.

## Part II.C$'$

`PART-II-C2-TRAPPING.md`. [Hin26c] Proposition 6.3 at $n = 4$: for a metric decaying in time to the stationary model,
hypersurfaces close to the stable and unstable manifolds of the trapped set, converging to them, to which the
null-bicharacteristic flow is tangent. The source reads it from [Hin21] Theorem 2.6, which is stated for closed
manifolds, smooth invariant splittings and a fixed perturbation, and takes the uniformity in the perturbation from that
theorem's proof. Here Theorem 1.1 proves what is needed directly and quantitatively (section 2), by the graph transform:
the hypersurfaces have codimension one and the normal dynamics is linear in the defining functions, so each graph
transform is a one-dimensional shooting problem, solved for the stable hypersurface by a contraction in a weighted norm
and for the unstable one by forward iteration. Its hypotheses are Part I's (Γ.1)-(Γ.3) and the tangential growth bound
of (K3); the invariant splitting is not used. Section 3 graphs the characteristic set near the trapped set over the
stationary one, computes the projected field, and proves Proposition 6.3 (Proposition 3.4). Finding (C$'$2) changes the
statement: the stable hypersurface loses one derivative, $\tilde\phi^s\in C^{d_0-2}$, and both are constructed on a
neighbourhood of the trapped set, which is all the trapping estimates use. Written (D199). The eighty-third verifier
re-derived every step and confirmed (C$'$1)-(C$'$3) at source. Its five minor findings: in Lemma 2.1 the Lipschitz bound
$(4C_T)^{-1}$ on the graphs made a term of size $\frac14$ where $O(\delta)$ was claimed (the bound is now $\delta$), and
(S3) needs the bound on $\beta$ itself; $\hat W_0t_* = q_1$ exactly, not $q_1-2G_1$; a citation for the frame
$\partial_{t_*},\partial_x$; and the smallness of $\epsilon_0$ for the unstable hypersurface. Its nits (the derivative
formula in the proof of (S3), the chart constant, $\tau$-derivatives in (T2), a doubled window factor, $q_1\ge\beta_0$
near $\Gamma$, relative compactness of $Y$, $T_0 = 1$, a quotation of [Hin21]) are seated, and one nit on the D200
repairs to Part II.C as well (D201); they await the next reader.

## Part II.D

`PART-II-D-REGULARITY.md`. [Hin26c] section 7.1 at $n = 4$: the global edge-3b regularity estimate (Theorem 1.2, the
source's Proposition 7.1), which loses one derivative at the trapped set. Section 2 adds two tools to the commutator
machinery of Part II.A$'$: a term $JL$ produced by a cut-off to the characteristic set (Lemma 2.1), and bounds of
microlocal norms through symbols (Lemmas 2.4-2.5). Section 3 proves the six radial estimates as computations of symbols
at the radial sets of Part II.B, the weights and fibre inner products entering through the subprincipal symbol of a
conjugated operator (Lemma 1.1); at $\mathscr I^+$ that symbol is the source's (7.22) at $n = 4$ (Lemma 3.4). Section 4
proves the estimate at the trapped set, which the source quotes from [Hin21] Theorem 3.9, from the hypersurfaces of Part
II.C$'$: it is the positive commutator form of the defect-measure proof of Part I.B, with an equation with damping, a
commutator that gains $\sqrt\delta$ near the stable hypersurface, a propagation estimate with the weight
$|\phi^s|^{-\beta}$, $\beta<\frac12$, one regulariser and an induction on the order in half steps (finding (D1)).
Section 5 assembles the estimate. Findings (D2)-(D3): in the source's Proposition 7.9 the time cut-offs are reversed,
its statement (4) fails near the initial time, and the case of a finite final time rests on a sign that fails off the
characteristic set; the proof here does without that case. Two slips by a factor 2 at $\mathscr I^+$ do not affect the
inequalities. Written (D202). The eighty-fourth verifier re-derived every threshold, sign and dynamical claim and
confirmed (D1)-(D4) at source. Its two minor findings: in Step 3 of Proposition 4.2 Lemma 2.5 is needed in its general
form, as the symbol of the propagated operator vanishes where the compared one does; and in Proposition 3.6 the term of
the time cut-off could touch the set where $B$ is elliptic, and is now kept a quarter unit earlier. Its nits (open sets
and the regulariser's parameter in the iteration, where the bracket formula of Lemma 4.1 (d) is used, the sign of
$c_{us}$ over $\partial\Sigma^-$, the extension of $F$ at the horizon, a construction of $\Theta$) are seated (D204);
they await the next reader.

## Part II.D'

`PART-II-D2-BREGULARITY.md`. [Hin26c] section 7.2 at $n = 4$: the global estimate of Part II.D with $k$ degrees of
b-regularity (Theorem 1.1, the source's Proposition 7.11) and its version tame in $k$. Section 2 writes the commuted
system for a family of commutator fields, indexed by words so that fields that do not commute need no reordering, and
proves once that the estimate for the system gives the estimate with b-regularity and its tame version (Lemmas 2.1-2.4),
and that the estimates of Part II.D hold for such systems under a sign condition (Lemma 2.5). Sections 3-6 supply the
families: near $\mathscr I^+$, two dilations and the six rotations of $\mathbb S^3$ (Lemma 3.1, the source's Lemma 7.12
at $n = 4$); at the horizon, where the commutator with $\partial_r$ lowers the threshold (the red shift); over $\partial
K^+$; and at the trapped set, where double commutators join the system. Section 7 proves Theorem 1.1 by the six steps of
Part II.D. Findings (D$'$1)-(D$'$8): two inclusions printed reversed, the weights of the tame estimate, multi-indices
for fields that do not commute, the systems to which the source applies its estimates without stating them for systems,
and the sign at the horizon, from Part II.B's constant $\beta_0$ rather than the Kerr formula. Written (D203). The
eighty-fifth verifier re-derived Lemmas 2.1-2.5, the commutators of sections 3-6 and the assembly, and confirmed
(D$'$1)-(D$'$2) at source. Its major finding: with the words of the system as first written, the coupling at the horizon
is not diagonal and its Hermitian part is indefinite for $k\ge2$, so the sign condition failed; as $\partial_r$ and
$t_*\partial_{t_*}$ commute, the system may be written with the letter replaced in place (2.2$'$), which makes the
coupling diagonal and the threshold that of Part II.D. Its minor findings (the remainder of the double commutator at the
trapped set, the bound used in the tame assembly, and half of (D$'$3), which it found mistaken: the source's expansion
is exact, only the reading of the components is not) and its nits are seated (D206); they await the next reader.

## Part II.E

`PART-II-E-ENERGY.md`. [Hin26c] section 8 at $n = 4$: solvability of forward problems on bounded time slabs, with energy
estimates, on edge-Sobolev spaces with and without b-regularity and tame in it (Propositions 3.4, 4.3, 4.4, the source's
Lemma 8.1 and Propositions 8.3, 8.6, 8.9); the same in the black hole interior, where the radius is the time function
(section 5, the source's Lemma 8.10 and Propositions 8.11-8.13); and the global estimate at high frequencies (Theorem
6.1, the source's Theorem 8.14), which joins them to Part II.D$'$. The energy estimate near $\mathscr I^+$ is computed
at $n = 4$ (Lemma 2.4): the term that carries the threshold is the same as at $n = 3$. Every first-order term is kept as
a quadratic form and absorbed by an exponential weight in time, and zeroth-order terms by a Poincaré inequality, so the
fibre inner product need only make $\mathrm{Re}\,p_1$ large. Solutions are constructed by duality from the energy
estimates for the operator and its adjoint, and their regularity comes from the microlocal estimates on slabs, with
radial estimates at the outgoing radial set over $\mathscr I^+$ localised in time by a function whose derivative along
the flow is a sum of squares (section 3). Findings (E1)-(E13), among them: the source's slab argument rests on the case
of its Proposition 7.9 that Part II.D found to fail, and leaves the estimate for the adjoint to the reader; its Theorem
8.14 applies its slab results at an initial time below their stated range, prints the tame estimate with the wrong
weights on $Pu$, and omits the condition $\alpha_+<\alpha_I-\frac12$ that the estimate it invokes assumes. Written
(D205). The eighty-sixth verifier re-derived Lemma 2.4 at $n = 4$ by machine (and at $n = 3$, reproducing the source's
(8.10)), Lemma 2.5, Propositions 3.2 and 3.4 and sections 4-6, and confirmed (E1)-(E13) at source. No major finding. Its
six minor findings are seated (D207): the admissible order is extended below $t_* = 1$ and over $\{r^\sharp\le r\le
r_0\}$ by its own formula, monotone there by the same computation; the collar flow is applied after a cut-off; the tame
inductions use two nested slabs per step; the support of $E_+$ needs a smaller neighbourhood of $\mathscr I^+$; the
extended $t^\flat$ is defined by its formulae, not by Seeley's extension; and Proposition 3.2 states
$t_--\omega_0\ge\frac12$. Its nine nits are seated too; they await the next reader.

## Part II.F

`PART-II-F-IOTA.md`. [Hin26c] section 10 at $n = 4$: the normal operator of the stationary model at future timelike
infinity and its Mellin-transformed family (sections 1-2); that family's invertibility at high frequencies, without and
with b-regularity, by the positive commutator scheme of Part I.B carried to the semiclassical 0- and cone calculus on
$\iota^+$ (sections 3-4, the source's Proposition 10.6 (2)); its Fredholm property and invertibility at bounded
frequencies (section 5, Proposition 10.6 (1) and Lemmas 10.9-10.10); forward solutions of the normal operator (section
6, Proposition 10.12); the modified operator $P_+$ and its forward solutions (section 7, Definition 10.13 and
Proposition 10.14); and Theorem 10.1 (section 8), forward solutions of the stationary model on e3b-spaces with decay at
$\iota^+$ and the loss $\aleph$ at $K^+$. The dimension enters through $c = \frac32$ and the density shifts; every
threshold is recomputed, and they agree with `iplusnorm5.py`. At bounded frequencies the 0-calculus parametrix is that
of [0C] Theorem 3.4 (with bounds), used only through the Fredholm property, proved here by the Schur test; the reduced
normal operator is inverted with modified Bessel functions; the Fourier transform bound the source quotes is proved.
Strong uniqueness for the normal operator is proved by a Paley-Wiener-Schwartz argument at a constant order (Lemma 6.4),
which the source's comparison argument needs and does not have. Findings (F1)-(F9), among them: the normal operator's
factor $t_*^{-2}$, the high-energy statement's range of parameters, a sign at the outgoing radial set, the Plancherel
factor $|\sigma|^{2j}$, and the source order $\mathsf s-1$ (not $\mathsf s-2$) in Proposition 10.12; and gaps (G1)-(G7)
closed, among them the constancy hypothesis of [0C] Theorem 1.5, the dilation invariance of the orders at which
Proposition 10.12 is applied, and the auxiliary operators needed to use Part II.E's slab estimates near $\mathscr I^+$.
Written (D208). The eighty-seventh verifier re-derived the constants at $n = 4$, the four threshold sums, the symbols
and Hamilton fields, the Bessel reduction, the Schur-test integrals, the Fourier bound and the order and weight
bookkeeping of sections 6-8, by machine where it could, and confirmed (F1)-(F9) at source. No major finding. Its seven
minor findings are seated (D209): Step 0 of Theorem 10.1 at the order $\mathsf s+1$; the bounded weight at
$\mathscr I^+$ in Lemma 5.8; the density factor near 0f in Lemma 2.2; the decay $\rho_+^2$ of the metric at $\iota^+$,
the $n = 4$ value, now cited to Part II.B ((F11)); the absorption time; finite speed of propagation, now Lemma 1.3,
proved from the uniqueness theorem of Bär, Ginoux and Pfäffle (READ) with explicit monotone functions, wherever it is
used; and the five [0C] statements, re-read at source. Seating them brought out four more, repaired: the slab and the
comparison region of Lemma 6.3, the starting time of the iteration in Proposition 7.4 (2), a modified metric in Lemma
7.3 (b) that was not close to $g_0$ near $K^+$, and Theorem 10.1 itself, now stated and proved on $\Omega_*$, where the
next part uses it ((F13)). Findings (F10)-(F14) are added. The eight nits are seated too. The eighty-eighth verifier
read those repairs and confirmed each (D212); its two further minor findings, a time cut-off in Lemma 6.3 that was not
scaled and the strip $0\le\mathrm{Im}\,\sigma< -\gamma_+$ in Lemma 6.4, and four notes are repaired, and await the next
reader.

Amended (D238): Lemma 5.7 is stated for $a>-1$, which is all its proof uses, as III.G Proposition 3.2 needs; to be
read.

## Part II.F'

`PART-II-F2-TAME.md`. [Hin26c] section 11 at $n = 4$: Theorem 11.1, forward solutions of admissible wave-type operators
$P$ on b-Sobolev spaces with decay at $\mathscr I^+$, $\iota^+$ and $K^+$, with estimates tame in the b-regularity, its
form with unweighted b-densities, and Remarks 11.2-11.4. The forward solution is the weak limit of those of operators
$P_\epsilon$ equal to $P$ up to a time of order $\epsilon^{-1}$ and to the stationary model after it; the estimate for
$P_\epsilon$, uniform in $\epsilon$, joins Part II.E's global estimate to Part II.F's Theorem 8.1, the error being small
near $\iota^+\cup K^+$ and controlled at bounded times on slabs. Three points the source passes over are written out:
the order function needs the margin $3+\delta+\aleph$, not $2+\delta+\max(1,\aleph)$; the cut-offs must be functions of
the time function $t^\flat$, whose level sets carry the slabs, not of $t_*$; and the tame bound needs one extension
across $\{r = r_0\}$ that is bounded at every order of b-regularity at once, constructed where the order is a constant
integer (recorded in Part II.E as (E14)). Findings (F'1)-(F'12), among them that the source's statement on $\Omega$, for
operators whose principal part is that of the Kerr wave operator, is not proved here, and that uniformity in $P_0$ stays
open until a later part needs it. Written (D210). Read by the eighty-eighth verifier, which confirmed (F'1)-(F'12) and
the constants by machine; its one major finding, a uniqueness class too large for the smallness assumed, is repaired by
restricting the class to $s'\ge\inf\mathsf s-2$, and one minor finding and two notes are seated (D212). Verified; the
repairs await the next reader.

## Part II.G

`PART-II-G-NASHMOSER.md`. The tools of [Hin26c] section 12 on which the nonlinear step rests, none of them dependent on
the dimension. The Nash-Moser theorem in the form of the source's Theorem 12.4, which the source quotes from Saint
Raymond and from an earlier paper of its author, neither read, is proved here by Saint Raymond's iteration with a
smoothing step at each stage and the supports tracked; it needs the hypotheses' constants up to order $21d+6$ (the
source quotes $16d^2+43d+24$; nothing later depends on the number). Smoothing operators on spaces of supported b-Sobolev
functions (Proposition 12.6) are constructed with charts in which the time function is a coordinate, and checked on the
domain $\Omega_*$ of Part II.F$'$ (Example 12.7); tame bounds for products and nonlinear functions (Lemma 12.8) are
proved from the Gagliardo-Nirenberg inequality. The weights of the source's section 12.1 are recorded at $n = 4$
($0<\epsilon_I<\epsilon_+<1$, decay nearly $r^{-3/2}$ at $\mathscr I^+$); its Theorems 12.2-12.3 and the model problems
12.9-12.12 are not carried, Theorem 12.3 being due in Part III with a loss $\aleph>0$. Findings (H1)-(H9), among them
that (12.7) and Theorems 12.9 and 12.11 reverse the inequality between $\epsilon_+$ and $\epsilon_I$ that Theorem 11.1
needs, and that the smoothing construction's charts and its time function need more care near $\mathscr I^+$ and
$\iota^+$ than the source gives. Written (D211). The eighty-ninth verifier redid the iteration's exponent algebra by
machine and found the three theorems sound; its five minor findings, two of which withdraw (H2) and (H7) as misreadings
of the source, and its nits are seated (D213). Verified; the repairs await the next reader.

## Part II.G'

`PART-II-G2-DECAY.md`. [Hin26c] section 13 at $n = 4$: the tools by which forward solutions are shown to decay faster
than Theorem 11.1 alone gives. The Fourier transform in time on weighted b-Sobolev spaces, on the line and on the
resolved product spaces, is proved from the Gagliardo seminorm and two dyadic Hardy inequalities, in place of the
source's appeal to a textbook and to complex interpolation. Part I's resolvent estimates at bounded nonzero, high and
low frequencies are translated into b-Sobolev spaces with a loss of b-regularity that does not grow with the order; the
high-energy bound, which the source states without proof, is proved from Part I.B through a comparison of b-spaces with
I.B's semiclassical spaces. The radiation field at null infinity is the coefficient of $r^{-3/2}$, extracted by two
ordinary differential equation lemmas proved here in place of those the source cites. At $n = 4$ the density shifts
weights by 2 where the source has $\frac32$, the threshold at the outgoing radial set is $\frac32+\bar S$, and the
indicial root at null infinity is $\frac32$. Findings (J1)-(J13), among them that the source's Lemma 13.4 and Corollary
13.5 fail at $\sigma = \infty$, that its spaces (13.7)-(13.8) as printed carry no Taylor terms, so that Corollary 13.7
as printed fails for $\beta>1$, and that the first step of its Proposition 13.11 (2) needs $\ell'\ge1-\delta$; none
changes what later parts use, in the forms proved here. Uniformity in the operator is reduced to that of Part I's
estimates (section 6.2). Written (D214). Read by the ninetieth verifier: no major finding; two minor findings (a
reversed inequality in a proof, a sign in a symbol order) and eleven nits seated (D216). Verified; the repairs await the
next reader.

## Part III.B

`PART-III-B-FAMILY.md`. [Hin26] sections 3-4 at $n = 4$: the compactified spacetime and its charts with $\mathbb S^3$ at
infinity; the Myers-Perry family $g_b$, $b = (\mu,A)\in\mathbb R\times\mathfrak{so}(4)$, in Kerr-Schild form for every
spin at once, smooth on the compactification with its mass at $|x|^{-2}$ and its spin at $|x|^{-3}$; the time functions;
the linearised metrics (seven parameters); the initial data and their decay; null coordinates near null infinity; the
cut-off Lorentz boosts and the pullback of the family by them; and the gauge-fixed Einstein equation with its
linearisation. Five dimensions simplify the source's section 3: the ingoing and outgoing times differ by a function in
$|x|^{-1}C^\infty$, not by a logarithm, so the Kerr-Schild coordinates are smooth on the compactification, a smooth
change of time puts the family into the source's outgoing form at null infinity, and every causal statement reduces to
one inequality of the Kerr-Schild algebra. The boosted mass term has the exponent 4 and the constant $\frac2{\pi^2}$;
the gauge modifications take the trace weight $\frac23$, which makes them act on trace-reversed tensors exactly as at $D
= 4$. Checked symbolically: the Kerr-Schild identities, the change of time, the boost's action at null infinity, and the
Ricci-flatness of Tangherlini; the Ricci-flatness of the spinning family is READ. One finding (K1): the source's
Definition 3.17 is inconsistent and its Lemma 3.18 claims the boost field vanishes near the black hole at early times,
which the cut-offs do not give; repaired by a radial cut-off, with nothing changed at infinity. Written (D215).

*Proved (D216).* The ninetieth verifier confirmed the D213 repairs of Part II.G, and the eighty-ninth had confirmed the
D212 repairs of Parts II.F and II.F' (D213, recorded there as confirmed but not yet marked): Parts II.F, II.F' and II.G
are proved.

*D217.* The ninety-first verifier read Part III.B: no major finding; two minor findings (a sign in an intermediate line
of Lemma 3.5's proof; Lemma 5.2's hypothesis made exhaustive, with strictly nested cut-offs and small boosts shown to
satisfy it) and ten nits seated. Part III.B is verified. It confirmed the D216 repairs of Part II.G', which is proved.

*D221.* The ninety-second verifier read the D217 repairs and confirmed each. Part III.B is proved.

## Part III.A'

`PART-III-A2-HARMONICS.md`. [Hin26] section 2.4 at $n = 4$: functions, 1-forms and symmetric 2-tensors on $\mathbb S^3$
by type, with the identities between the geometric operators on each type and the special low degrees; the Minkowski
wave operator, symmetric gradient and divergence in the null bundle splittings near infinity (the source's Lemma 2.29);
the types those operators preserve; the indicial roots by type; and the symmetric gradient's indicial families with
their kernels. Everything is proved at general $N$ and read at $N = 3$, $N = 2$ being the source entry by entry: the
commutators on the sphere from the Ricci identity, the spectra on co-closed 1-forms and on trace-free divergence-free
tensors from five ambient identities of the Gauss formula, and Lemma 2.29 by the Cartesian route, so no outside result
on harmonics is used. At $n = 4$ one type is new (tensor type, $l\ge2$), the constants of Lemma 2.29 change (findings
(H1)-(H6)), and the free indicial roots on a degree-$d$ component are $-d$ and $d+2$. `harm5.py` K5 checks Lemma 2.29 at
$N = 2$ and $N = 3$ entry by entry against the Cartesian computation for every type with $l$ symbolic; K6 factors the
determinants. Written (D218).

*D221.* The ninety-second verifier read Part III.A$'$ line by line and harm5.py: no major finding; two minor findings
(the labels claimed that no outside result on harmonics is used, where Lemma 1.4 quotes the classical theory of harmonic
polynomials and the spectral theorem; K2 and K3 asserted only closure) and six nits seated (III.A$'$ section 3.4). Part
III.A$'$ is verified.

## Part III.A

`PART-III-A-PREREQ.md`. [Hin26] sections 2.1-2.3 at $n = 4$: manifolds with corners and blow-ups, b-analysis and partial
polyhomogeneity, the normal form of a b-normal vector field, testing for and integrating partial expansions, the
boundary spectrum and formal solutions (with the Mellin transform written out), the scattering, 3b- and
scattering-b-transition notions on $\mathbb R^{1+4}$ with the Plancherel lemma and the normal operator at sf, the
integration of $x\partial_x$ and of the transport operator $x\partial_x-y\partial_y$, and the Fourier transform with
partial expansions at $\iota$, $K$, $I$ and at tf, zf, scf. Everything is proved; the inputs of the last result are Part
II.G$'$'s Propositions 3.3 and 3.5, which carry [Hin26c] section 13.1 to $n = 4$ in b-densities. Findings (L1)-(L4): the
matching condition (2.29) of the source's Proposition 2.25 takes the wrong log index ($k(E_K,j)$ for $k(E_K,j+1)$), so
that as printed it is meaningless already for $E_K = (1,0)$; a weight misprinted in its proof; the commutator with the
cut-off in $\sigma$, which is harmless; the constant in Cauchy's formula of Lemma 2.15; and (L5)-(L7), from the
ninety-third verifier (D226): the source's Lemma 2.23 needs $\alpha+\mathrm{Re}\,z>\beta$, not $\alpha>\beta$ (a
counterexample shows it is necessary); the proof of its Proposition 2.25 (1), integrating one factor at a time, gives a
larger tf index set than stated, and the stated one follows from a new Lemma 3.3, which solves for each zf coefficient
at once; and the order of integration and the boundary weight, which the source leaves implicit. Verified (D226). The
ninety-fourth verifier (D229) confirmed those repairs and found one minor gap, seated: the direct proof of Lemma 1.3,
integrating one factor at a time, loses derivatives, and the stated order follows by subtracting a particular solution
and reading the homogeneous coefficients off; and two nits (the extension of a coefficient by its ordinary differential
equation in Lemma 3.3, and the same loss absorbed in Proposition 4.2's $l$). The ninety-fifth verifier read them (D231):
proved.

## Part III.D

`PART-III-D-GAUGEPOT.md`. [Hin26] section 6 to Proposition 6.9 at $n = 4$: the gauge potential wave operator
$\Box^\Upsilon_{g_b}$ on 1-forms near the five-dimensional Tangherlini parameter. Its structure near infinity (Lemma
2.1: $S = \bar S$, $Q\in\rho^3\mathrm{Diff}^1_{\mathrm b}$, zero-energy difference in
$\rho^4\mathrm{Diff}^2_{\mathrm b}$), the Minkowski model with $\bar E$, $\bar S$ and $M_E$ at general $N$ (Lemma 3.1),
the indicial roots by type with the gap $(0,\lambda^\Upsilon_{\mathrm s1,2})$ (Lemma 4.1), the horizon threshold
$s>\frac32$ (Lemma 5.1), the trapped set in the open form Part I.B uses, $\gamma_-<0$ (Lemma 5.2), high energies and
bounded frequencies (Propositions 6.1 and 6.3), mode stability away from zero on Tangherlini by ordinary differential
equations in place of [AHW24] (Proposition 6.2), and tf-admissibility (Lemma 7.1). Findings (D1)-(D6): the deviations
gain a power because the mass enters at $|x|^{-2}$; the constants $m = \frac2N$ and $\pm Ne$; the roots pair about four
centres by family, with $z = 4e\gamma^2$; the record's claim that strong trapping admissibility persists because "the
inequalities are open" is not right for the all-$\epsilon$ property and is not needed; [AHW24] replaced; the threshold
exactly $s>\frac32$. `harm5.py` K7 checks the model operator against the Cartesian computation for every type at
$N = 2, 3$; K8 factors its indicial determinants. Verified (D226): the ninety-third verifier's minor finding, that the
trapped set's inner product depends on the covector while I.B section 6 assumed one from the base, is repaired in I.B by
Lemma 6.0, the source's conjugation (5.9), which Lemma 5.2 now cites with the density it uses; four nits. The
ninety-fourth verifier read the repairs (D229): proved.

## Part III.D'

`PART-III-D2-ZEROENERGY.md`. [Hin26] section 6.4 and Lemma 6.13 at $n = 4$. Lemma 2.1 ([Hin26] Lemma 6.10): on
five-dimensional Tangherlini the zero energy kernel of the 1-form wave operator is spanned by
$W^* = r^{-2}dt+r_hr^{-3} f^{-1}dr$ (energy identities for the stationary mode equations, and the continuation inside
the horizon of III.D Proposition 6.2 (d)), and the annihilator of its range by the pairing with $d(H(r-r_h))$ (from
$\Box_0H(r-r_h) = 0$, $\Box d = d\Box_0$ and the index 0 of I.C Corollary 6.6), in place of [AHW24] Theorem 5.1 (2).
Lemma 3.1 (Lemma 6.11): both horizon pairings are exactly $4\pi^2$, by hand and computed. Proposition 4.1 (Proposition
6.12): mode stability at every frequency of the closed upper half plane; Step 1 by a Grushin problem with a fixed
compactly supported augmentation, to which I.C Theorems 6.4 and 7.1 apply as proved, its Schur complement
$-4\pi^2(-i\sigma+\gamma)+o(|\sigma|+\gamma)$; Step 2 by perturbation at low, middle and high frequencies around a base
point where invertibility holds at every frequency. Lemma 5.1 (Lemma 6.13): the zero energy inverse, with
polyhomogeneous inverse images by III.A Lemma 1.4. Findings (D$'$1)-(D$'$5), among them (D$'$4): the source's Step 2
asserts a low-energy radius independent of the horizon modification, as written not shown; closed here. Verified (D229):
read in full by the ninety-fourth verifier, who recomputed both horizon pairings independently ($4\pi^2$, against $4\pi$
in four dimensions); two nits seated and read (D231): proved.

## Part III.D''

`PART-III-D3-SYMSTATES.md`. [Hin26] section 6.5.1 at $n = 4$. Lemma 2.1 (Lemma 6.14): the operators of $g_b$ differ from
Minkowski's by one more power of $\rho$ than in the source ($\rho^3$, $\rho^4$ for $\delta^*$; $\rho^4$, $\rho^5$ for
$\Box^\Upsilon$), from III.B (3.5). Lemma 2.2: smooth dependence on $b$ of the zero energy inverse images. Proposition
3.1 (Proposition 6.15): the stationary solutions of the gauge potential equation with the time translation, the
translations, the boosts and the rotations of Minkowski space as leading terms, and their symmetric gradients, each
correction one order faster; the boost's correction at $\rho^1$, no indicial root, so without the source's logarithm
(6.31) and without its formal solution lemma; the translations' at $\rho^2$, which needs
$e_\Upsilon\gamma_\Upsilon^2>0$; six Killing rotations at zero rotation. Findings (D$''$1)-(D$''$5). Verified (D229):
read in full; one minor finding seated, that at general $b$ the difference of the boost corrections lies in
$\bar H^{\infty,\alpha''}_{\mathrm b}$ for every $\alpha''<2$ rather than being $O(\rho^2)$, which suffices through
$\delta^*$, and one nit, both read (D231): proved.

## Part III.D'''

`PART-III-D4-GENSTATES.md`. [Hin26] section 6.5.2 at $n = 4$. Lemma 2.1: solving the zero energy equation with a
prescribed leading term, by a hand step, the formal solution lemma (III.A Lemma 1.5) and the zero energy inverse
(III.D$'$ Lemma 5.1), the roots needed only on the leading coefficient's type. Proposition 3.1 (Proposition 6.18): the
generalized zero energy states -- polynomials in $t_*$ in the kernel of the gauge potential operator -- on the time
translation (no logarithm), the boosts and the rotations to higher order, and the four classes on the roots below $-1$
with the source's degrees, each stationary correction two orders below its leading term; the leading terms computed on
Minkowski space (`genstates5.py`, `puregauge5.py`). Deferred to the part on [Hin26] section 8: that these leading terms
span the kernels of $\bar L(0)$'s indicial families. Findings (D$'''$1)-(D$'''$6), among them a misprint in the source's
recursion and a normalisation in its (6.39a). Verified (D231): read in full by the ninety-fifth verifier; one minor
finding (in the recursion the corrections are shown only $\epsilon_{\mathrm{ind}}$ below their leading terms, which is
all that is used) and two nits seated; the ninety-seventh verifier read the repairs and confirmed each (D235): proved.

## Part III.E

`PART-III-E-CONSTRAINT.md`. [Hin26] section 7 to Proposition 7.3 at $n = 4$. Theorem 1.1, the source's Theorem 7.1 at
$n = 4$ (the summary of [Hin26a]), is stated as the input and is proved in Part IV. Lemma 2.1 (Lemma 7.2): the adjoint
of the constraint propagation operator at zero energy is invertible on b-weights $\alpha\in(0,C_0+2]$ with $s\le C_0+1$,
its indicial roots $2-\bar\lambda$; inverse images are partially polyhomogeneous and vanish inside the horizon.
Proposition 3.1 (Proposition 7.3): the large zero energy dual states built from the time translation, the four
translations and the six rotations, whose trace-reversed symmetric gradients decay, eleven at zero rotation against the
source's seven. Findings (E1)-(E4): the weights move by one (the Coulomb root is 2, the source's 1); the corrections are
one order faster; the eleven states; the input. Section 7.2.1 is Part III.E$'$. Verified (D231): one minor finding
(consequence (a) of Lemma 2.1 restated at the weight where the inverse applies, with the uniqueness step) and three nits
seated, and Theorem 1.1 (3) amended with the count by type and the conditions (C2)-(C4) of Part III.F$'$; the
ninety-seventh verifier read the repairs and confirmed each, the amended (3) being an obligation of Part IV, as Part
III.F$'$ treats it (D235): proved.

## Part III.E'

`PART-III-E2-V1STATES.md`. [Hin26] section 7.2.1 at $n = 4$. Lemma 2.1: Part III.B's family is $O(4)$-equivariant,
$\varphi_O^*g_{(\mu,OAO^T)} = g_{(\mu,A)}$. Lemma 2.2 (Lemma 7.5): for a rotation $V = V(A_V)$,
$\delta^*_{g_b}V_b = \frac12D_Ag_b([A,A_V])$ exactly, with leading term $\mu\rho^3(dt_*+2\,d|x|)\otimes_s\rho V(W)$ and
no pure gauge term. Lemma 2.3: the Killing rotations are $\ker\mathrm{ad}_A$, of dimension 6, 4 or 2. Proposition 3.1
(Proposition 7.4): $h^*_{b,\mathrm v1}(V) = h^\sharp_{b,\mathrm v1}([A(b),A_V])+h^\flat_{b,\mathrm v1}(V)$, $h^\sharp$
defined on all of $\mathfrak{so}(4)$ and smooth in $b$, its $\rho^3$ leading term with the source's coefficients,
$(\delta^*_{g_b,E_C})^*h^\sharp\in\rho^{\lfloor C_0\rfloor+5}C^\infty$ and $D_{g_b}\mathrm{Ric}(0)^*h^\sharp$ compactly
supported. Findings (E$'$1)-(E$'$5), among them (E$'$4): the source's argument for $D\mathrm{Ric}^*h^\sharp$ uses
$G^2 = \mathrm{Id}$, true only in $3+1$ dimensions; the statement holds by the self-adjointness of $G\,D\mathrm{Ric}$.
`dualv1_5.py` V1-V4; `mp5.py` M1-M5. Proved (D231): read in full by the ninety-fifth verifier, with no findings.

## Part III.F

`PART-III-F-LINEARISED.md`. [Hin26] section 8 to the end of 8.1 at $n = 4$. Lemma 2.1 (Lemma 8.1): $2L_b =
-2\partial_{t_*}\rho(\rho\partial_\rho-\frac32-\bar S)+\widehat{2L_b}(0)+Q\partial_{t_*}-g^{00}\partial_{t_*}^2$ near
infinity, $Q\in\rho^3\mathrm{Diff}^1_{\mathrm b}$,
$\widehat{2L_b}(0)-\widehat{2\bar L}(0)\in\rho^4\mathrm{Diff}^2_{\mathrm b}$. Lemma 3.1 (Lemma 8.2, (8.7)): $\rho\bar S$
factors through 1-forms with one cross term zero, so $\mathrm{spec}\,\bar S$ is that of the constraint propagation and
gauge potential operators' endomorphisms with five zeros, $\min\mathrm{spec}\,\bar S = 0$, by hand. Proposition 4.1
(Proposition 8.3): at the trapped set a grading of the symmetric 2-tensors preserved by the rotation of the
two-dimensional angular plane gives, for every $\epsilon$, an inner product with $\lambda_{\max}(p_1^\Gamma)<\epsilon$,
for every constraint damping 1-form. Findings (F1)-(F5). `sbar5.py` S1-S3, `strap5.py` P1-P3, `lgrade5.py` G1 (new).
Verified (D231): one nit seated (the rotation rate written as $\sigma\kappa$); read and confirmed by the ninety-seventh
verifier (D235): proved.

## Part III.F'

`PART-III-F2-INDICIAL.md`. [Hin26] sections 8.2-8.3 at $n = 4$. Lemma 2.1: the indicial determinants of each type factor
through those of the gauge potential and constraint propagation operators, with the gauge-invariant factor
$(\lambda+l)(\lambda-l-2)$ (computed exactly, `lin5.py` E2). Lemma 2.2: the constraint operator's vector type 1 roots
are $3$ and $-1-2\gamma_Cv_C$, by hand. Proposition 2.3 ([Hin26] Lemma 8.4): the roots by type; none with real part in
$(0,1]$; an even split in every type; $0$ only at scalar types 0 and 2, simple; simplicity and the source's (8.13) under
conditions (C1)-(C4) on the constraint operator's roots, stated in III.E Theorem 1.1 (3) as amended in D231, with
$z = 4e_\Upsilon\gamma_\Upsilon^2$ off a countable set. Lemma 2.4: only finitely many isotypic components carry roots in
a strip, uniformly in a parameter. Lemma 2.5 ([Hin26] Lemma 8.5): the indicial solutions at 0 satisfy the gauge
condition exactly; at scalar type 0 the solution is the constant tensor
$-d\bar t^2+\frac{2-e_\Upsilon}{4e_\Upsilon}dx^2$. Lemma 3.1: the relative index theorem at the zero end of the
transition face, proved on Part I.C's spaces. Proposition 3.3 ([Hin26] Proposition 8.6): tf-admissibility for small
$\gamma_\Upsilon$, the kernel by the Bianchi identity and the constraint operator's tf-admissibility, the cokernel by
deforming to the wave operator with the index fixed. Corollary 3.4 ([Hin26] Corollary 8.7). Findings (F$'$1)-(F$'$6),
among them (F$'$2): the source's claim that all roots are simple, and its (8.13), rest on properties of the constraint
operator's roots, now stated in III.E Theorem 1.1 (3) (D231); and (F$'$3): at $n = 4$ Lemma 8.5 is not needed for
tf-admissibility. `linroots5.py` R1-R3 (new) checks Lemmas 2.2 and 2.5. Written (D230). Verified (D235): read in full by
the ninety-seventh verifier; one minor finding ($C_0 = 100$ of III.F, against $C_0\ge101$ here; the record's certificate
is for 100) and two nits ((C1) needs $\gamma_C$ large against $e_C^{-1}$, and $\epsilon_{\mathrm{ind}}<3\times10^{-6}$
at the record's point; the cancelled root at s1) seated, to be read.

Proved (D238): the ninety-eighth verifier read the D235 repairs (m1, $C_0 = 100$; n1, n2) and found them correct and
complete.

## Part III.F''

`PART-III-F3-MODES.md`. [Hin26] Proposition 8.8 at $n = 4$. Lemma 1.1: the horizon threshold of $L_b$, which III.F did
not state: the horizon matrix has determinant (1.1), $k^5(k-1+x)^3(k-2+2x)(k+(1-e_C)x)(k-y)(k+1-y)^3(k+2-2y)$ with
$x = a_v\gamma_Cr_h$, $y = c_v\gamma_{\Upsilon,H}r_h$, so $s>\frac12+\max(0,2-2x)$ with III.D$'$'s horizon modification,
below the source's $\frac52$, which ignores the damping (computed, `lhor5.py` H1-H2, new). Corollary 1.2: Part I's
hypotheses for $L_b$, Fredholm of index 0, invertible at large $|\sigma|$, uniformly in $b$. Lemma 1.3: a conormal
kernel element lies in $\mathcal X_\sigma$. Theorem 2.2 ([AHW24] Theorem 6.1 (1) on five-dimensional Tangherlini): a
mode solution of $D\mathrm{Ric}(h) = 0$ at $\sigma\ne0$ of one type and degree is $\delta^*$ of a mode 1-form, by the
Kodama-Ishibashi master equations with positive potentials for $l\ge2$ and the three exceptional sectors pure gauge, the
gauge 1-form built by the radial equations of Lemma 2.1 and, at scalar type 1 and real $\sigma$, glued across the sphere
$\sigma^2r^4 = \mu_0$ by analyticity (`gmodes5.py` G1-G5; G3 now also checks that the trace-free angular equation is
[KI03]'s algebraic relation). Lemma 2.3: a solution of a wave-type equation on the exterior continues inside the
horizon. Proposition 3.1: $\widehat{L_{b_0}}(\sigma)$ invertible for every $\sigma\ne0$ of the closed upper half plane,
by the Bianchi identity, III.E Theorem 1.1 (1), Theorem 2.2, Lemma 2.3 and III.D$'$ Proposition 4.1, harmonic by
harmonic, with no estimate in $l$. Proposition 4.1: invertibility for $b$ near $b_0$ and $|\sigma|\ge c_0$. Open
(section 5, (F$''$4)): $b\ne b_0$ with $0<|\sigma|<c_0$, which the source takes from [AHW24] on Kerr and which has no
five-dimensional counterpart. Findings (F$''$1)-(F$''$4). Written (D232). Verified (D235): read in full by the
ninety-seventh verifier; one minor finding (Lemma 2.1 (b)'s bound $A = O(r^{-1})$ is false because of the entry
$i\sigma$; the conclusion holds through the b-system in $(w_r,r^{-1}w_{t_*},r^{-1}w_A)$) and four nits (a sign in Lemma
2.3's correction, the reason $x>0$, the high-frequency constant renamed $C_{\mathrm{hf}}$, a citation) seated, to be
read.

Proved (D238): the D235 repairs read and correct. Two nits seated: the angular row of the b-system in Lemma 2.1
(b), $r\partial_r\tilde W_A = \tilde W_A-\partial_A\tilde W_r+2h_{rA}$; and Lemma 2.3 assumes $w$ smooth on
$\{r\ge r_h\}$, which is all its proof uses.

## Part III.F'''

`PART-III-F4-ZERO.md`. [Hin26] section 8.4 from Proposition 8.9 to Corollary 8.13 at $n = 4$. Lemma 1.1: the linearised
family at $b_0$, $\dot g_{b_0}(1,0) = |x|^{-2}(dt+d|x|)^2$ and
$\dot g_{b_0}(0,\dot A) = 2\mu_0|x|^{-4}(dt+d|x|)\otimes_s(\dot Ax)\cdot dx$, from the Kerr-Schild form. Proposition 2.2
([Hin26] Proposition 8.9): the gauged linearised metrics, without the source's logarithm, the mass correction at
$\rho^1$ and the spin's at $\rho^2$ being off the indicial roots (Lemma 2.1). Remark 2.3 (Remark 8.10): the spin changes
in the image of $\mathrm{ad}_A$ are $2h_{b,\mathrm v1}(V)$, pure gauge with unbounded potentials as $A\to0$. Theorem 3.1
([AHW24] Theorem 6.1 (2) on five-dimensional Tangherlini): a decaying stationary solution of $D\mathrm{Ric}(h) = 0$ of
one type and degree is a linearised Myers-Perry metric plus $\delta^*$ of a stationary 1-form one power larger, by the
Kodama-Ishibashi master equations at zero frequency for $l\ge2$ and explicit gauges at $l = 0,1$ (`static5.py` S1-S6).
Proposition 4.1 ([Hin26] Proposition 8.11): index 0, kernel and cokernel eleven-dimensional, the kernel at $b_0$ by the
Bianchi identity, Theorem 3.1, continuation inside the horizon and mode stability of $\Box^\Upsilon$, near $b_0$ by the
augmented operator's invertibility at $b_0$ and I.C Theorem 7.1; the dual states independent at every $b$ by their
leading terms. Corollary 4.2 ([Hin26] Corollary 8.13): the linear right inverse with eleven augmentations. Findings
(F$'''$1)-(F$'''$6), among them (F$'''$4): the source's Lemma 8.12 pairings are not needed for these, and are left to
the next part; and (F$'''$5): the source's adjoint (8.25) uses $G^2 = \mathrm{Id}$, false in five dimensions. Written
(D233). Verified (D235): read in full by the ninety-seventh verifier, three nits (the two $\epsilon_{\mathrm{ind}}$ told
apart, the energy identities for complex solutions, Lemma 2.3 up to $r = r_0$) seated, to be read.

Proved (D238): the D235 repairs read and correct.

## Part III.F''''

`PART-III-F5-PAIRINGS.md`. [Hin26] Lemmas 8.12, 8.15 and Proposition 8.14 at $n = 4$. Lemma 2.1: $G\circ D\mathrm{Ric}$
self-adjoint with $|dg_b| = |dt_*||dx|$ makes its $t_*$-coefficients symmetric, antisymmetric, symmetric, and
$D\mathrm{Ric}\circ\delta^* = 0$ gives $P_1\delta^*\omega = -P_0(dt_*\otimes_s\omega)$,
$P_2\delta^*\omega = -P_1(dt_*\otimes_s\omega)$. Lemma 2.2: the source's 'applies verbatim' written out, each pairing of
a zero energy state (or a generalized pair) with a dual state equal to a limit at infinity, zero above the critical
weight, a leading-term integral at it, invariant under decaying gauge terms and changes of time function. Lemma 3.1
([Hin26] Lemma 8.12): $3\pi^2\dot\mu$, $2\pi^2\mu\langle\dot A,A'\rangle_F$ and $\frac{3\pi^2}2\mu\,\xi_S\cdot\xi_{S'}$
(`pairing5.py` P2-P5), the $11\times11$ matrix block triangular and invertible. Lemma 4.1 ([Hin26] Lemma 8.15): the s1
pairing an isomorphism; the v1 functional $\lambda^\sharp = \pi^2\mu\langle A_V,\cdot\rangle_F$ on all of
$\mathfrak{so}(4)$, from Remark 8.10 and the spin-independence of its leading terms, the images of $\mathrm{ad}_A$ over
small spins spanning $\mathfrak{so}(4)$. Proposition 5.1 ([Hin26] Proposition 8.14 (1)): the physical states at $-2$ of
types s2, v2 and t2, smooth in $b$, with the source's Step 2 modified to absorb the centre-of-mass pairings against the
rotations, which are not determined away from $b_0$. Findings (F$''''$1)-(F$''''$5); (F$''''$3): the states at $-3$ and
the generalized companions are not constructed, the window being decided in the part on [Hin26] sections 9-11. Written
(D234). Verified (D235): read in full by the ninety-seventh verifier; one minor finding (Step 3 placed $u_b$ in a
conormal space only, so (5.1)'s index set was not reached; now $u_b$ is polyhomogeneous by III.A Lemma 1.4) and two nits
(a weight, the spin-independence at spinning $b$) seated, to be read; the four pairing values the brief named were
recomputed or confirmed.

Proved (D238): the D235 repairs read and correct. Two nits seated: the leading term of $\dot g^\Upsilon_b(0,\dot A)$
is $2\mu\rho^3(dt_*+2\,d|x|)\otimes_s\rho V(\dot A)$, and the index set of $u_b$ carries no subscript $b$.

## Part III.G

`PART-III-G-SPECTRAL.md`. [Hin26] Proposition 9.2 at $n = 4$: the spectral family $N_{\mathrm{sf}}(\lambda)$ of the
model operator at future timelike infinity, on spaces supported at $v = -1$ and taken across the light cone $v = 0$,
with conormal regularity there. Lemma 1.2: the principal symbol $v(v+2)\xi^2+|\eta|^2$; b-ellipticity at
$R = v^{-1} = 0$ with Mellin roots $\lambda-r$;
$N_{\mathrm{sf}}(\lambda) = R^{2+\lambda}N_{\iota^+}(\lambda)R^{-\lambda}$, II.F's $N^0(\sigma)$ at
$\sigma = -i\lambda$; the commutators; the dilation metric, for which $dT$ is spacelike. `sf5.py` S1-S8 (new) checks
these, each with a failing control. Section 2: the light cone is a radial source with $\beta_0 = 2(1+v)$ and threshold
$s<2-\mathrm{Re}\,\lambda$; the slab estimates at $v = -1$; the Fredholm property for admissible $(s,\mu)$ (Proposition
2.4); b-regularity through the Lie derivatives along the rotations and the dilation, whose commuted system keeps the
threshold (Propositions 2.6-2.7). Section 3: injectivity for $\mathrm{Re}\,\lambda<2$ through II.F Lemma 5.8, III.F$'$'s
tf-admissibility on $(0,1]$ and conormality at the light cone (Lemma 3.1). Section 4: the semiclassical estimate in
vertical strips (the source's (9.9)), with the escape function $\tilde\xi = -(v+2)(v\xi+1)$, II.F's estimates at the
cone point for $|\mathrm{Im}\,z|\le Ch$ and I.B's at the light cone and on the slabs (Proposition 4.6). Theorem 5.1:
Proposition 9.2 (1)-(3) at $n = 4$, index 0, invertibility for $\mathrm{Re}\,\lambda<2$ (the source has
$1+\epsilon_{\mathrm{ind}}$ at $n = 3$) and finite meromorphy. Findings (G1)-(G6); (G6): Proposition 9.4 and the rest of
section 9 are the next part. Written (D236). Verified (D238): read in full by the ninety-eighth verifier. One major
finding: Proposition 4.6 used Lemma 4.4's constant-order slab estimate where Lemma 4.2's semiclassical order varied. It
is repaired by a factor $g(v)$, which makes the order the constant $b_{\mathrm{in}}$ over $\{v\le-\frac14\}$ and
non-increasing in the direction of propagation. One minor finding: injectivity stopped at $\mathrm{Re}\,\lambda<\frac32$
by the method only. Lemma 3.1 now holds for every $s\notin\frac12+\mathbb Z$ and II.F Lemma 5.7 for $a>-1$, so the
operator is invertible for $\mathrm{Re}\,\lambda<2$. Four nits are seated, among them the uniqueness of the turning
point by $H_p^2v<0$ (`sf5.py` S11, new). The repairs are to be read. Proved (D240): the ninety-ninth verifier read the
D238 repairs (A1-A6, B1-B3) and found them correct and complete; nothing in III.G still relies on the bound $\frac32$.

## Part III.G'

`PART-III-G2-IOTA.md`. [Hin26] Proposition 9.4 at $n = 4$, with Definitions 9.3, 9.6 and Remark 9.7: the inverse of the
$\iota^+$-normal operator $N_{\iota^+}(\lambda) = R^{-2-\lambda}N_{\mathrm{sf}}(\lambda)R^\lambda$ given by III.G's
inverse. Lemma 1.1: $\bar S$ is semisimple at $n = 4$, with constant eigenvalues and smooth spectral projections, by
$\rho\bar S = UV$ and the block structure of $VU$ (`sbar5.py` S4, new). So the expansion at $\mathscr I^+\cap\iota^+$
has one small exponent $\frac32+s$ per eigencomponent
($s\in\{0,(1-e_\Upsilon)\gamma_\Upsilon,\gamma_\Upsilon,2\gamma_\Upsilon\}$), with the index sets of Definition 1.2.
Lemma 1.3: the index set at $K^+\cap\iota^+$ is generated by the roots of III.F$'$ with real part $\le0$; its only
exponent with real part 0 is $(0,0)$. Lemma 2.1: conormality at the light cone for every Sobolev order
$s\notin\frac12+\mathbb Z$, by integrating in $v$; it replaces the source's (9.5) and (9.21). Theorem 3.1:
polyhomogeneity at $K^+$ and the partial expansion at $\mathscr I^+$ up to $\frac32+\gamma_C(1-e_C)(1-v_C)$. The
source's analytic continuation, which excludes $v^\lambda$-terms and their logarithms, is carried out through a Mellin
recursion. The finite-regularity map (3.3) is finite-meromorphic. Lemmas 4.2-4.3: the boundary spectrum. The source's
Remark 9.7 becomes a lemma: poles of $N_{\mathrm{sf}}^{-1}$ invisible on $\iota^+$ lie in
$\frac52+\mathrm{spec}\,\bar S+\mathbb N_0$ (`sf5.py` S9-S10, new). Findings (G$'$1)-(G$'$8); the source's (9.17) holds
to a finite order. Written (D237). Verified (D240): read in full by the ninety-ninth verifier. One major finding: the
finite-regularity order of $(v\partial_v-\frac32-\bar S)h$ is $\ell_I$, not $\ell_I+1$, as the source prints. Two minor
findings: the smallness $\gamma_\Upsilon<\frac38$ and the non-coincidence choices were not secured; and the holomorphy
in $\lambda$ of the expansion coefficients, now by fixed-circle Mellin integrals. Seven nits are seated; one withdraws
the finding of a misprint in the source's (9.22), which the normalised text cannot show. Proved (D241): the hundredth
verifier read the repairs, correct and complete; its one nit, holomorphy of the remainder in the $\ell_I$-weighted
space, is seated.

## Part III.G''

`PART-III-G3-GRAFT.md`. [Hin26] Definitions 9.8, 9.10, Proposition 9.9, Proposition 9.11 and Corollary 9.12 at $n = 4$.
*The window.* If every $\iota^+$-order grafted at $n = 4$ exceeds $1+\max(\epsilon_K,\epsilon_{\mathrm{ind}})$ (for the
source's direct grafts at $\lambda = 1$, the record's open reading $\alpha_5$), the expansion at $R = 0$ is needed only
below $R^3$: $\ell_K<\ell_K^{\max} = \min(3,2+2\gamma_Cv_C)$. That needs no state at $-3$ and no companion of the
physical states at $-2$. Table 1.1 lists the roots in $(-3,0]$ with their states (III.D$''$, III.D$'''$, III.F$''''$),
the companions constructed and those used ($k_\mu\ge2+\mu$). Lemma 1.2: their leading terms span the indicial kernels,
which closes III.D$'''$'s deferred item for the window. Lemmas 2.1-2.6: towers, the Minkowski and Myers-Perry formal
solutions, their errors (the source's (9.28)-(9.31), (9.37)). Theorem 3.1 (Proposition 9.9): the expansion of
$N_{\iota^+}(\lambda)u = f$ at $R = 0$ is a sum of formal solutions, log-free, by induction on the least exponent;
Corollary 3.2 is the $K^+$ index set of III.G$'$ made precise. Theorem 4.2 (Proposition 9.11): grafting, with $2\bar L$
as the $\iota^+$-normal operator of $2L_b$ by the exact identity (4.1) and $\chi_\iota$ a function of $t_*$; Corollary
4.3 (Corollary 9.12). (C5) $\gamma_Cv_C\ge\frac12$ is an obligation for Part VI. Findings (G$''$1)-(G$''$7). Written
(D239). Verified (D241): the hundredth verifier read it in full. One major finding: the $\iota^+$-normal operator is
that of $2\bar L$, so (4.4) failed by a factor 2, repaired by $u_+ := N_{\iota^+}(\lambda)^{-1}(2f_+)$. Two minor: the
window is conditional on the least grafted order, and Corollary 4.3's hypothesis is now a finite quasi-homogeneous sum.
Seven nits are seated. The repairs are to be read.

## Part III.C

`PART-III-C-EXTERIOR.md`. [Hin26] Definitions 5.1-5.4 and 5.13, Remark 5.5, Proposition 5.11 with (5.40)-(5.41a),
Proposition 5.14 and Corollary 5.15 at $n = 4$. Lemma 1.1: on the exterior region near infinity,
$(\rho_0,\rho_I,\omega)$ are global coordinates, and $\partial_{t_*} = \rho_0(X_0-X_I)$,
$\rho\partial_\rho = X_I+8\mu_0\rho_0^2\rho_I(X_0-X_I)$ exactly. Lemma 2.1: products of partially polyhomogeneous
b-Sobolev functions. Definition 3.1: the index sets at $\mathscr I^+$ start at $\frac32$, with the source's last
condition strengthened to $\mathcal E^{\mathrm{tot}}_I+(\mathcal E^{\mathrm{tot}}_I-1) \subset\mathcal E^C_I$ (needing
$\gamma_\Upsilon<\frac14$); $\pi_{11}h$ carries no radiation field. Lemma 4.1: from III.F Lemma 2.1,
$L_b = -\rho_0^2\rho_I(X_I-\frac32-\bar S)(X_0-X_I)$ modulo $\rho_0^2\rho_I^2\mathrm{Diff}^2_{\mathrm b}$. Lemma 4.2:
$\bar S$ in the splitting is a constant lower-triangular matrix (Schur's lemma, `scri5.py` C1). Proposition 4.4: the
perturbation's part of the operator has coefficients of $\mathscr I^+$-index $\mathcal E^{\mathrm{tot}}_I$, half an
order below the leading part, so the source's $A^h-A_0$ and $B^h$ are error terms at $n = 4$. Proposition 5.2 and
Corollary 5.3: the forward mapping into $\langle\mathcal E^C_I+1\rangle'$, with
$\mathcal F_{I,11} = 1+(\mathcal E^C_I\cup(\frac32+(1-e_\Upsilon)\gamma_\Upsilon,0))$. `ext5.py` E1-E5 (new): the
coordinate identities, the scalar leading part, $\bar A$'s support, Definition 3.1's closure properties and Proposition
5.2's bookkeeping, each with controls. Findings (C1)-(C7). Written (D242). Verified (D244): verifier 101's four minor
findings and six nits seated -- the radiation allowance of $\slashed\pi_0$ stated with obligation (C7), Lemma 4.2 in
$\bar g$'s and $\eta$'s frames, E5's third control (the source's analogue condition fails Proposition 5.2), and the
index condition's relation to the source's. Proved (D245): verifier 102 read the repairs; three nits seated.

## Part III.G'''

`PART-III-G4-RESONANT.md`. [Hin26] section 9.1.3 at $n = 4$: Lemmas 9.13-9.14, Proposition 9.15, Definition 9.16 with
(9.49), Remark 9.17, Corollary 9.18, Definition 9.19, Remark 9.20, Lemma 9.21, (9.54)-(9.55), Proposition 9.22 and
Remarks 9.23-9.24. The sources' class (III.C) has one exceptional exponent in its $(dx^1)^2$-component,
$1+\lambda_\sharp$, $\lambda_\sharp = \frac32+(1-e_\Upsilon)\gamma_\Upsilon$, where the source has two. So the least
incoming pole of $N_{\iota^+}(\lambda)^{-1}$ on partially polyhomogeneous inputs is $\lambda_\sharp$, simple (Corollary
2.6), and every other pole has real part above $\frac32+2\gamma_\Upsilon$. Lemma 1.2: III.G$'$'s eigen-spaces lie in the
slot-wise spaces. Lemma 2.3 and Proposition 2.4: the continuation is identified with III.G$'$'s inverse below
$\lambda_\sharp$ by uniqueness in III.G's admissible spaces, a step the source asserts; at $\lambda_\sharp$ itself the
extension by zero creates $\delta(v)$ at the light cone. Lemma 3.4: the left inverse used in the source's Lemma 9.21.
`ext5.py` E6-E7 (new): the eigenvector supports of $\bar A$ and Lemma 2.2's exponent bookkeeping. Findings
(G$'''$1)-(G$'''$5); (G$'''$1) records that the pole at $\lambda_\sharp<2$ is excited only by a $v^{\lambda_\sharp}$
term of $\Pi_{2\gamma_\Upsilon}h$; the record's 10.38 (d) closes it on its readings, and whether section 12's linear
grafting errors reach it is for Part III.J. Written (D243). Proved (D247): verifier 103 read the D245 repairs.
Verified (D245): verifier 102's four minor findings (the
frames on $\iota^+$, finite regularity on strips, the mechanism and the record's account in (G$'''$1)) and eleven nits
seated.

## Part III.G''''

`PART-III-G5-TF.md`. [Hin26] section 9.2 at $n = 4$: (9.57)-(9.61), Definition 9.25, Lemma 9.26, Remarks 9.27-9.28,
Definition 9.29 with (9.72), Proposition 9.30, Remarks 9.31-9.34 and Proposition 9.35. Lemma 1.1: the tf-normal operator
$N_{\mathrm{tf}} = \hat r^{-2}\mathcal N(-\hat r\partial_{\hat r})\pm i\hat r^{-1}(-\hat r\partial_{\hat r}-\frac32-\bar
S)$ is the spectral family of $\bar L$ rescaled; Lemma 1.2: the Myers-Perry family differs from it by
$\rho_{\mathrm{scf}}^2\rho_{\mathrm{tf}}^4\mathrm{Diff}^2_{\mathrm b}$. Lemma 2.2: the formal solutions at ztf satisfy
$N_{\mathrm{tf}}\bar h^{(\mu),\le k} = (\mp i)^{k+1}\hat r^{k-1-\mu}\psi_k$ exactly. Theorem 3.1 (the source's Lemma
9.26): the inverse on $\rho_{\mathrm{ztf}}^{-\alpha}f_0$ expands at $\hat r = 0$ over every row of III.G$''$ Table 1.1
in the window, each with $c_\mu = 2-\lfloor-\mu\rfloor$ companions and the factor $l_{\beta_\mu}$, holomorphically in
$\alpha$ across coincidences, by a merged-residue Mellin argument (Lemmas 3.2-3.4). Proposition 4.4 (the source's 9.30):
grafting with the Myers-Perry states, tf-error $\alpha_0+\mathcal E_{\mathrm{ind}}$, zf-class kept. Proposition 5.1
(9.35): conormal sources. `tfgraft5.py` T1-T4 (new). Findings (G$''''$1)-(G$''''$6): the source's (9.58) is $2\bar L$'s
and its (9.59) misprints $\rho^{-\lambda-j}$; at $n = 4$ Theorem 3.1 needs the window $w_0<\ell_K^{\max}$, where the
source has $3+\epsilon_{\mathrm{ind}}$ (whether sections 11.5-12 need more of the window is for III.I-III.J); the first
step of the source's proof of Proposition 9.35 fails for conormal coefficients and is repaired by a dilation-invariant
inverse. Written (D246). Verified (D247): verifier 103's three minor findings seated -- the bound
$\ell_{\mathrm{zf}}<3$ of D246's (3.1) is not needed (Lemma 3.3 splits as the source's Case 1), the exceptional s1 term
adds tf-exponents at 4 to (4.3) ((G$''''$7), the source's imprecision too), and $\ell_{\mathrm{zf}}\notin\mathbb N_0$
is now assumed ((G$''''$8)) -- with eight nits.

## Part III.H

`PART-III-H-AUGMENT.md`. [Hin26] section 10.1 at $n = 4$: the states cut off near $I^+$, $\chi_K\dot g$ and
$\chi_K(t_*h_{b,\mathrm s1}+\breve h)$, need no improvement at $\iota^+$ (the source's Lemma 10.3 is not needed): their
source terms are $O(r^{-4})$ in a cone inside $\iota^+$ (Lemma 2.2), with zero-frequency values $[L_b,t_*]\dot g$, resp.
$\frac12[[L_b,t_*],t_*]h+[L_b,t_*]\breve h$, modulo $\widehat{L_b}(0)\mathcal A^1$ (Lemma 2.3), and Fourier transforms
$r^{-3}G(\sigma r,x)$, rapidly decaying at scf (Lemma 2.4). Proposition 3.2 (the source's 10.6): the augmented zero
energy operator is invertible, by III.F$''''$ Lemma 3.1's pairings. Theorem 4.1 extends I.C Theorem 6.4 to columns
depending on $\sigma$; Corollary 4.2 is the source's Proposition 10.7, for every weight with $\alpha+2\in(0,1)$ (the
source's $(0,\epsilon_{\mathrm{ind}})$). Corollaries 4.3-4.4: $\widehat{L_b}(\sigma)$ is invertible for small
$\sigma\ne0$ and $b$ near $b_0$, uniformly, which closes III.F$''$ section 5 (the source's Proposition 8.8 at $n = 4$
near $b_0$). Section 5: the spectral-side augmentation, with no correction and no logarithm. Findings (H1)-(H5), among
them (H2): the source's (10.6b) does not give the injectivity its proof of Proposition 10.6 uses, and under
(10.6a)-(10.6b) alone that proposition is false (an explicit choice of rows has a kernel). Written (D248). Verified
(D249): verifier 104's two minor findings seated -- the uniformity in $b$ loses $\delta$ (the states are continuous in
$b$ only below their weights; Remark 2.6, $\epsilon_0 = \frac14(1-(\alpha+2))$) and the differentiability in $\sigma$ of
the Schur complement is written out (Theorem 4.1 (3)) -- with six nits. Proved (D252): verifier 105 read the
repairs; one citation nit seated.

## Part III.H$'$

`PART-III-H2-ADMISS.md`. [Hin26] Theorem 10.1 at $n = 4$ by the argument of its section 10.2: the forward solution is a
contour integral of $\widehat{L_b}(\sigma)^{-1}$ (Lemma 2.1), split into high frequencies (Lemma 3.1), the regular part
of the augmented low-energy inverse (Lemmas 4.1-4.2) and the contributions of the zero energy states, whose
$t_*$-derivatives have transforms bounded at sf-weights below 0 and 1 with rapid decay at scf (Lemma 5.1), and which are
recovered by integrating twice in $t_*$ (Lemma 6.2, with the translation-invariant parametrix of Lemma 6.1). Theorem
1.3: for $\alpha_{\mathrm{sf}}+2\in(0,1)$, $L_b$ is 2-admissible with margin 1 and sf-loss 0 (the source: $\delta>
\alpha_{\mathrm{sf}}+\frac32$ at $n = 3$), for orders of a class $\mathcal O_c$ (II.C Definition 2.4 with three
conditions that Part I needs), at $b_0$ for every $k$ and on neighbourhoods $\mathcal B_K$ for $k\le K$. Findings
(H$'$1)-(H$'$7), among them (H$'$2): with $\alpha_K = -2$ and margin 1 the incoming threshold is one short of what the
source's Lemmas 10.9-10.10 use; the high frequencies are measured at $\alpha_{\mathrm{sf}}+1$ and the regular part at
regularity $\mathsf s+1$ instead, which the margin allows. Written (D250). Verified (D252): verifier 105's three minor
findings seated -- the bounded frequencies freeze the induced orders on finitely many intervals (I.A's estimates are
uniform only for fixed orders), at a cost $2\epsilon$ in the weight of the high-frequency part; Lemma 6.1 is stated
without b-regularity (for variable orders commutators carry logarithms); and Lemma 6.2 handles the boundary $\{r =
r_0\}$ by a cut-off and an extension in $x$ -- with nine nits. D254: verifier 106 found that a frozen order need not be
admissible at nearby frequencies ((C3) is not quantitative); the bounded frequencies now use the induced orders
themselves, uniform by I.A Theorem 7.2 (1) for continuous families, with the inverse bound by a contradiction argument;
and two nits. Proved (D256): verifier 107 read the D254 repairs and found them correct; one nit.

## Part III.I

`PART-III-I-CONE.md`. [Hin26] section 11's setting and section 11.1 at $n = 4$: the perturbation classes with
$(2,0)\in\mathcal E_+$ at $\iota^+$ (the background differences are of order 2 there), the edge-3b class of
perturbations for $\ell_I\le\frac12$, $\ell_+\le1$ with no $\gamma_\Upsilon$ restriction (Lemma 2.2), the structure of
$L^{g,g_0}$ in the forward cone with the constant matrix $\bar A$ and no $h$-dependent leading part (Propositions
3.3-3.4), the forward mapping (Proposition 4.1), the patched background's curvature at $\rho_+^4$ (Lemma 4.3, Corollary
4.2), admissibility relative to $L_b$ with $p_0 = \tilde p_1 = 0$ (Corollary 5.2), and the forward solutions of [Hin26]
Theorem 11.12 at $b_0$ with sf-loss 0, $\beta_+\in(\frac12,\frac32)$, $\beta_I\in(\beta_+,\frac32)$ (Theorem 5.3). Lemma
5.1 shows II.C's construction of orders gives III.H$'$'s class $\mathcal O_c$, which meets III.H$'$'s obligation
(H$'$7). Open ((I3)): Theorem 11.12 for $b\ne b_0$ needs 2-admissibility for all $k$ near $b_0$ and II.F$'$ uniformly in
the stationary model. Written (D251). Verified (D254): verifier 106's major finding seated -- Proposition 4.1's weights
must stay below $a_I+\frac12$ at $\mathscr I^+$ and $a_++\min\mathrm{Re}\,\mathcal E_+$ at $\iota^+$ (and (4.2) needs
$\ell_+\le\max(a_+,\min\mathrm{Re}\,\mathcal E_+)$), a restriction the source's Proposition 11.8 also needs ((I6)) --
with two minor findings (the inverse metric by a finite Taylor expansion and Moser's estimate under $H^3$-smallness;
Lemma 3.1 away from $K^+$) and eight nits. D256: verifier 107 read the repairs, correct but one reason in Lemma 3.6 (now
III.B Lemma 5.2's second alternative) and two nits.
Proved (D258: verifier 108 read the D256 repairs).

## Part III.I$'$

`PART-III-I2-SCRI.md`. [Hin26] section 11.2 at $n = 4$: the structure of $L^{g,g_0}$ at $\mathscr I^+$ with leading part
$(X_+-X_I)(X_I-\frac32-\bar A)$, the same constant $\bar A$ for the dynamical operator as for $L_b$ (Lemma 1.1); partial
polyhomogeneity at $\mathscr I^+$ without loss at $\iota^+$ for $\ell_+<\ell_I<\ell_I^{\max} =
\frac32+(1-e_C)(1-v_C)\gamma_C$, $\ell_I\notin\frac32+\sigma_\Upsilon$ (Proposition 2.1, Lemma 2.2), with the radiation
field at $\frac32$ in $\slashed\pi_0$ only and no $\frac32$-term in $\pi_{11}u$; and formal solutions of $L_bu = f$ at
$\mathscr I^+$ with one exceptional term $\frac52+(1-e_\Upsilon)\gamma_\Upsilon$ where the source has two (Proposition
3.1). Findings (I$'$1)-(I$'$3): the $h$-dependent radiation coupling is half an order lower at $n = 4$; the upper weight
is $\ell_I^{\max}$ where the source writes $3+\epsilon_I$, and the exclusion of $\frac32+\sigma_\Upsilon$ is stated; the
windows of (3.2) start at $\min\mathrm{Re}\,\mathcal E^C_I$. Written (D253). Verified (D256): verifier 107's three major
findings seated -- Proposition 2.1 reaches only $\ell_I<a_I+\frac12$ and $\ell_+<a_++\min\mathrm{Re}\,\mathcal E_+$ (the
products, as III.I (I6); the source's $3+\epsilon_I$ is this bound, not the $\pi_C$-root bound, so (I$'$2) is
rewritten), Lemma 2.2's $\alpha_+$ below $\min\mathrm{Re}\,\mathcal E_+$, and (3.2) with III.A's extended unions
((I$'$4), the source has the same slip) -- with two minor ($\ell_I>\frac32$; $\ell_+\notin\mathrm{Re}\,\pi_1\mathcal
E^{\mathrm{tot}}_I$) and eight nits.
Proved (D258: verifier 108 read the D256 repairs).

## Part III.I$''$

`PART-III-I3-ALMOST.md`. [Hin26] section 11.3 at $n = 4$: the integration of $\partial_{t_*}$ from $t_* = 1$ and from
$t_* = -Cr$ (Lemma 2.1, the source's Lemma 11.18) and with a moment condition (Lemma 3.1, Lemma 11.19, which also needs
$\beta_K>-1$); the high and bounded frequencies (Lemma 4.1, from II.G$'$ Corollaries 4.2 and 4.5), the low frequencies
of the augmented operator in b-spaces (Lemma 4.2, II.G$'$ Proposition 4.7's proof with III.H's estimates) and the
transforms of the cut-off states (Lemma 4.3: rapid decay at scf, tf-orders $a+2$, $a+3$); and Proposition 5.1 ([Hin26]
Proposition 11.17): for sources of $K^+$-weight $\alpha_K\in[\frac12,1)$ the forward solutions have $K^+$-weight
$\alpha_K-2$ and keep the $\iota^+$-weight $\min(\alpha_+,\frac32,\min\mathrm{Re}\,\mathcal E_+)-\epsilon$, where the
source's falls to $\alpha_K-\epsilon$ ((I$''$1)); the iteration's window is $(0,1)$, III.H (1.1)'s, inside the gap
((I$''$2)), and the
null infinity weight needs $2\le\ell_I<a_I+\frac12$ ((I$''$4)). At $b_0$. Written (D255).
Verified (D258: verifier 108; Lemma 3.1's support now in $[-c_0,c_0]$, $c_0<\frac12$ ((I$''$5), a gap the source
shares), $c$ fixed per order $k$ with $H^\infty$ recovered from the $c$-independence of $u$, and the continuity in
$(S,h)$ locally uniform through III.I$'$ Proposition 2.1's constructive bound; nine nits).
Proved (D259: verifier 109 read the D258 repairs).

## Part III.I$'''$

`PART-III-I4-BOOST.md`. [Hin26] section 11.4.1 at $n = 4$: profiles independent of $\sigma$ on
$X^\pm_{\mathrm{sc}\text-\mathrm b}$ (Lemma 1.1, by Fubini), the augmented operator near zero energy (Lemma 1.2, the
source's Lemma 11.21: $\widehat{L_b}(\sigma)-\widehat{L_b}(0)$ and the columns, these of tf-order $3-\epsilon$), the
cut-off states near zero energy (Lemma 1.3), and Proposition 2.1 ([Hin26] Proposition 11.20): for sources of
$K^+$-weight $\alpha_K\in(1,\min(a_K-1,\frac32))$ the forward solution is $\chi_Kh^{\le1}(\dot S)+\tilde u$, $\dot S =
\hat S_1(0)$, $\tilde u$ of $K^+$-weight $\alpha_K-2$ and $\iota^+$-weight
$\min(\alpha_+,\frac32,\min\mathrm{Re}\,\mathcal E_+)-\epsilon$. Findings: no $\iota^+$ step (the source's Step 2), as
the formal solution's $\iota^+$-index set starts at $\frac32+(1-e_\Upsilon)\gamma_\Upsilon$ ((I$'''$1)); the
$\iota^+$-weight ((I$'''$2)); the window $(0,1)$ ((I$'''$3)); the $K^+$-range ((I$'''$4)). At $b_0$. Written (D257).
Verified (D259: verifier 109; Step 4's a priori weight lowered below $\min\mathrm{Re}\,\mathcal E_+$, the support of
$\mathcal Fv$ in a compact subset of $(-c,c)$, $c$ fixed per order $k$; seven nits).
Proved (D261: verifier 110 read the D259 repairs).

## Part III.I$''''$

`PART-III-I5-UNBOOST.md`. [Hin26] section 11.4.2 at $n = 4$: the re-centred boost state $h^{\le1}_\natural =
h^{\le1}-C'h$ (Lemma 1.2: III.B's boosts are centred at $t = 0$, III.D$''$'s model states at $\bar t = 0$), the
correction terms (Definition 2.1, Lemma 2.2: index set $(2,0)\cup(2+\mathcal E_{\mathrm{ind}})$ at $\iota^+$, no
logarithm), the augmented operator $P_1$ in the form of the source's Remark 11.27 (Definition 2.3, Lemma 2.5: its
linearisation is III.I's operator with a shifted perturbation), the boost identity (Lemma 2.4, the source's (11.78b)),
the derivative of the operator family (Lemma 3.1), the parameter derivative (Lemma 3.2, the source's Lemma 11.28:
$\iota^+$-order 4, no splitting), the continuity of the boost parameter in the operator (Lemma 4.2), Proposition 4.1
(the source's Proposition 11.30: asymptotics, and the boost parameter map invertible) and Corollary 4.3 ((11.95)).
Findings (I$''''$1)-(I$''''$6). At $b_0$. Written (D260).
Verified (D261: verifier 110; the boost identity, the re-centring and the invertibility confirmed; Lemma 4.2 (b) stated
for $\ell_I>2$ or sources vanishing near $\mathscr I^+$, Lemma 3.1's count with the background difference as a
perturbation; nine nits).
Proved (D263: verifier 111 read the D261 repairs).

## Part III.I$'''''$

`PART-III-I6-ALMOSTBDD.md`. [Hin26] section 11.5 at $n = 4$: Proposition 2.1 (the source's Proposition 11.32): if the
boost parameter of the source vanishes, the forward solution has $K^+$-weight $\alpha_K-2$ for every $\alpha_K<2$ and
$\iota^+$-weight $\min(\alpha_+,\frac32,\min\mathrm{Re}\,\mathcal E_+)-\epsilon$; Corollary 2.2 (the solutions of
III.I$''''$ Corollary 4.3). The proof raises the $K^+$-weight in rounds of Part III.I$'''$'s argument, with a step at
$\iota^+$ (III.G$''$ Corollary 4.3, no pole below 2) once the weight passes $\lambda_\sharp =
\frac32+(1-e_\Upsilon)\gamma_\Upsilon$; re-solving at null infinity creates no exponent below $\frac52$, so the rounds
end. Findings (I$'''''$1)-(I$'''''$3). At $b_0$. Written (D262).
Verified (D263: verifier 111; the iteration at $\iota^+$, the re-solving at null infinity and $S_0 = 0$ confirmed; the
$K^+$-order fixed rather than $\ell_K$, as in the source's (11.102), and $\alpha^\sharp_+$ kept off the exponents the
iteration creates; nine nits).
Proved (D266: verifier 112 read the D263 repairs).

## Part III.I$''''''$

`PART-III-I7-PARAMS.md`. [Hin26] section 11.6.1 at $n = 4$: Proposition 2.1 (the source's Proposition 11.34): for real
sources with $\dot S(f) = 0$ and $K^+$-weight $\alpha_K\in(2,\min(a_K,2+\epsilon_{\mathrm{ind}},\frac52))$, the forward
solution is $\chi_K\dot g(\dot b)+\chi_Kh(\dot S^{(0)}_1)$ plus a remainder of $K^+$-weight $\alpha_K-2>0$. Lemmas
1.1-1.4: first-order zf expansions, conormal sections admissible at $\sigma\ne0$, the rows answered by the nullspace,
and the boost-type term $|\sigma|^{\alpha-3}h(S)$ of III.G$''''$ Proposition 5.1 moved into the $\mathcal S_1$-column
exactly. No logarithmic centre-of-mass term ($\iota^+$-exponents begin at $\lambda_\sharp>\frac32$). Findings
(I$''''''$1)-(I$''''''$4). At $b_0$. Written (D264).
Verified (D266: verifier 112; Steps 0-6, the matching and the new Steps 1-2 confirmed; Lemma 1.2 now lowers the order at
$R_{\mathrm{out}}$, the zero section, which is a radial set and not elliptic, with the kernels independent of the order;
reality from the $K^+$-limit of the real solution; $\epsilon$ fixed in (2.2); eight nits).
Proved (D268: verifier 113 read the D266 repairs).

## Part III.I$'''''''$

`PART-III-I8-UNPARAM.md`. [Hin26] section 11.6.2 at $n = 4$: the translated background (Definition 1.2, Lemmas 1.1,
1.3), the correction terms (Definition 2.1, Lemma 2.2, the source's 11.37-11.38), the operator $P_2$ (Definition 2.3,
11.40), the identities (2.3) (the source's (11.78b), (11.134b), (11.135b)), the parameter derivatives (Lemma 3.1,
11.41), and the elimination of the parameters (Lemmas 4.1, 4.3, 4.5, Corollary 4.6, the source's 11.42-11.46): for every
source in the class (11.116) there is a unique $(S',b',S'')$ for which the forward solution decays at $K^+$. The
source's centre-of-mass correction has $\iota^+$-order 1, outside $\mathcal X$ at $n = 4$, so the exterior background is
translated as it is boosted. Findings (I$'''''''$1)-(I$'''''''$4). At $b_0$. Written (D265).
Verified (D268: verifier 113; the order-1 obstruction, the translated background and the identities (2.3) confirmed sign
by sign; the uniformity now also covers III.I$'$ Proposition 2.1 applied to $L$, and Lemma 4.1 counts the order-2 terms
at an admissible $\iota^+$-weight; seven nits).
Proved (D269: verifier 114 read the D268 repairs).

## Part III.I$''''''''$

`PART-III-I9-COMMOTION.md`. [Hin26] section 11.7 at $n = 4$: the motion index set $\mathcal E_{++}$ fixed in advance
((1.1)), the corrections #3 and the operator $P_3$ (Definitions 2.1, 2.3, the source's 11.47-11.48) with the exact
identity of Lemma 2.4, the parameter derivatives (Lemma 2.6, 11.49), the expansion at one level (Lemmas 3.1-3.3: the
motions from the s1 row of III.G$''$ Corollary 4.3, the zero energy analysis with a tf-iteration), and Proposition 4.1
(= 11.51): a unique choice of all parameters gives $K^+$-weight $\alpha-2-\epsilon$ for every admissible
$\alpha<\min(a_K,3)$. No proliferation of logarithms, so no device $u_\Sigma$. Findings (I$''''''''$1)-(I$''''''''$5).
At $b_0$. Written (D267).
Verified (D269: verifier 114; the design claims, Lemmas 2.2, 2.4, 3.2, 3.3 and the induction of Proposition 4.1
confirmed; Lemma 3.1's Step 0 now extracts the iota+-terms of the second source class first, Lemma 2.6 (a) counts the
derivative of delta*_{g_0,E_C} on the motion gauge terms; seven nits).
Proved (D271: verifier 115 read the D269 repairs; one residue, $S\in\mathcal S_{1,\mathbb C}$ in Lemma 2.4, seated).

`PART-III-I10-CORR4.md`. [Hin26] section 11.8 to Lemma 11.57 at $n = 4$: the hypotheses (H1)-(H3) on $\mathcal X$,
the parameter exponents $\mathcal E_{\mathrm{par}}$, the rows $\mathcal N$ of six types and the source classes
$\mathcal Y(\alpha)$, $\alpha\le4+\epsilon_K$ (section 1); the correction terms #4 (Definition 2.1, the source's 11.55)
with their orders (Lemma 2.2), the operator $P_4$ (Definition 2.3, 11.56), the row identity (Lemma 2.4), and the
linearisation (Lemma 2.6, 11.57) in the exact form $f^\nu = L_{h,\vec p}m_\nu+r^\nu$, $r^\nu$ of $\iota^+$-weight
$2\lambda_\sharp+2-\epsilon>5+\epsilon_+$. No exponent 1 at $n = 4$, so no logarithmic reparametrisation; the v1
parameters avoid the Killing rotations. Findings (I$'''''''''$1)-(I$'''''''''$6). At $b_0$. Written (D270).
Verified (D271: verifier 115; the rows, towers, (2.1), Lemmas 2.2, 2.4 and the formula (2.4) for $r^\nu$
confirmed; $\mathcal E_{\mathrm{ind}}$ now also holds the towers' index sets, the strong $K^+$-decay of $h$ is
recorded as needed also for $r^\nu$, and at the non-rotating $b_0$ the v1 coefficient space is 0; seven nits).

`PART-III-I11-SPACETIME.md`. [Hin26] Theorem 11.59, Parts 1-3, first half, at $n = 4$: (C5) and (H4)
$\ell_I>3+\epsilon_+$; the parameter exponents $\mathcal E_{\mathrm{par}}$ fixed (Definition 1.1, an exponent set
$\Lambda$ with log orders growing with the real part; Lemma 1.2, the $n = 4$ form of Remark 11.62), the gap (G) and
the admissible orders; the towers of III.G$''$ as $\delta^*$-images of the 1-form towers and their comparison with
$m_\nu$ (Lemma 2.1), joint injectivity of the states and uniqueness of row expansions (Lemma 2.2, Corollary 2.3),
forward Fourier tails (Lemma 2.4); and the spacetime phase (Proposition 3.1): every $\iota^+$-term of
$u$-exponent below 2 solved up to the $K^+$-order $\alpha\le4+\epsilon_K$, its $K^+$-terms below $\alpha-2$ the
rows $\mathcal N_\iota$. The spectral half and the elimination are III.I$'''''''''''$. Findings
(I$''''''''''$1)-(I$''''''''''$6). At $b_0$. Written (D272).
