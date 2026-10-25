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
| I.A | [Hin26c] 9.1-9.2 | bounded nonzero frequencies, Theorem 9.5, bundles, uniform in b | verified (D195) |
| I.B | [Hin26c] 9.3 | high energies, trapping with (5.9)'s conjugation, Theorem 9.16 | **proved** (D194) |
| I.C | [Hin26c] 9.4-9.6 | zero energy (9.36), tf operator (9.38), low energy (9.41), 9.39, 9.43 | **proved** (D194) |
| II.A | [Hin26c] 2-3 | compactifications, Lie algebras, e3b-calculus, embeddings, tame estimates | verified (D194) |
| II.A' | [Hin26c] 3.23-3.24, k = 0 | elliptic and propagation estimates, finite regularity | verified (D196) |
| II.B | [Hin26c] 4 | null-bicharacteristic dynamics of the stationary model | written (D196) |
| II.C-F | [Hin26c] 5-8, 10-13 | spacetime estimates, decay at iota+ and K+, the iteration | to do |
| III | [Hin26] | the gauge-fixed linearised Einstein operator at n = 4 | to do |
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
(D196). Part I.A is labelled proved again once the next reader has confirmed it.

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
(D194). Part I.B is **proved**.

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
Hankel asymptotics and the thresholds of Propositions 9.6 and 9.9.

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
repairs await the next reader.

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
in Lemma 4.6 (4), a constant in (4.18), and a gap in the proof of Lemma 4.20, which is not used here. Written (D196); the
eighty-first verifier reads it.
