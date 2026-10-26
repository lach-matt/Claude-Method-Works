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
| I.B | [Hin26c] 9.3 | high energies, trapping with (5.9)'s conjugation, Theorem 9.16 | verified (D226; the repair, Lemma 6.0, to be read) |
| I.C | [Hin26c] 9.4-9.6 | zero energy (9.36), tf operator (9.38), low energy (9.41), 9.39, 9.43 | **proved** (D194) |
| II.A | [Hin26c] 2-3 | compactifications, Lie algebras, e3b-calculus, embeddings, tame estimates | **proved** (D197) |
| II.A' | [Hin26c] 3.23-3.24, k = 0 | elliptic and propagation estimates, finite regularity | **proved** (D197) |
| II.B | [Hin26c] 4 | null-bicharacteristic dynamics of the stationary model | verified (D197) |
| II.C | [Hin26c] 5, 6 but 6.3 | operator classes, admissibility, time function, order functions | verified (D200); D226 correction to be read |
| II.C' | [Hin26c] 6.3 | stable and unstable trapped sets of perturbed metrics | verified (D201) |
| II.D | [Hin26c] 7.1 | microlocal regularity: radial sets, the trapped set, the global estimate | verified (D204) |
| II.D' | [Hin26c] 7.2 | b-regularity and estimates tame in it | verified (D206) |
| II.E | [Hin26c] 8 | energy estimates on slabs and in the interior; the global estimate | verified (D207) |
| II.F | [Hin26c] 10 | the normal operator at iota+; forward solutions of P_0 on e3b-spaces | **proved** (D216) |
| II.F' | [Hin26c] 11 | forward solutions of wave-type operators, tame estimates | **proved** (D216) |
| II.G | [Hin26c] 12 | the Nash-Moser theorem, smoothing operators, tame bounds | **proved** (D216) |
| II.G' | [Hin26c] 13 | improving decay: Fourier transforms, resolvent bounds, the radiation field | **proved** (D217) |
| III.A | [Hin26] 2.1-2.3 | technical prerequisites: partial polyhomogeneity, integration along b-fields | verified (D226) |
| III.A' | [Hin26] 2.4 | harmonics on S^3; the Minkowski operators in the null splittings; indicial roots by type | verified (D221) |
| III.B | [Hin26] 3-4 | the Myers-Perry family on M, time functions, boosts, the gauge-fixed Einstein equation | proved (D221) |
| III.D | [Hin26] 6-6.3 | the gauge potential operator: structure, Minkowski model, indicial roots, horizon threshold, trapping, high energies, mode stability away from zero, tf-admissibility | verified (D226) |
| III.D' | [Hin26] 6.4, Lemma 6.13 | the gauge potential operator at zero energy: kernel and cokernel, pairings, mode stability at every frequency, the zero energy inverse | written (D222) |
| III.D'' | [Hin26] 6.5.1 | zero energy states from the Minkowski symmetries; Lemma 6.14's comparisons | written (D223) |
| III.D''' | [Hin26] 6.5.2 | generalized zero energy states of the gauge potential operator | written (D224) |
| III.E | [Hin26] 7-7.2 (to Proposition 7.3) | the constraint propagation operator at zero energy: invertibility of its adjoint, indicial roots, the large dual states | written (D225) |
| III.C, III.E', III.F-III.J | [Hin26] 5, 7.2.1, 8-12 | exterior stability; constraint and linearised operators; spectral theory; decay | to do |
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
and for the unstable one by forward iteration. Its hypotheses are Part I's (Γ.1)-(Γ.3) and the tangential growth bound of
(K3); the invariant splitting is not used. Section 3 graphs the characteristic set near the trapped set over the
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
minor findings are seated (D209): Step 0 of Theorem 10.1 at the order $\mathsf s+1$; the bounded weight at $\mathscr
I^+$ in Lemma 5.8; the density factor near 0f in Lemma 2.2; the decay $\rho_+^2$ of the metric at $\iota^+$, the $n = 4$
value, now cited to Part II.B ((F11)); the absorption time; finite speed of propagation, now Lemma 1.3, proved from the
uniqueness theorem of Bär, Ginoux and Pfäffle (READ) with explicit monotone functions, wherever it is used; and the five
[0C] statements, re-read at source. Seating them brought out four more, repaired: the slab and the comparison region of
Lemma 6.3, the starting time of the iteration in Proposition 7.4 (2), a modified metric in Lemma 7.3 (b) that was not
close to $g_0$ near $K^+$, and Theorem 10.1 itself, now stated and proved on $\Omega_*$, where the next part uses it
((F13)). Findings (F10)-(F14) are added. The eight nits are seated too. The eighty-eighth verifier read those repairs
and confirmed each (D212); its two further minor findings, a time cut-off in Lemma 6.3 that was not scaled and the strip
$0\le\mathrm{Im}\,\sigma< -\gamma_+$ in Lemma 6.4, and four notes are repaired, and await the next reader.

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
at once; and the order of integration and the boundary weight, which the source leaves implicit. Verified (D226), the
repairs to be read.

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
Lemma 6.0, the source's conjugation (5.9), which Lemma 5.2 now cites with the density it uses; four nits. The repairs
are to be read.

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
asserts a low-energy radius independent of the horizon modification, as written not shown; closed here. Written (D222).

## Part III.D''

`PART-III-D3-SYMSTATES.md`. [Hin26] section 6.5.1 at $n = 4$. Lemma 2.1 (Lemma 6.14): the operators of $g_b$ differ
from Minkowski's by one more power of $\rho$ than in the source ($\rho^3$, $\rho^4$ for $\delta^*$; $\rho^4$, $\rho^5$
for $\Box^\Upsilon$), from III.B (3.5). Lemma 2.2: smooth dependence on $b$ of the zero energy inverse images.
Proposition 3.1 (Proposition 6.15): the stationary solutions of the gauge potential equation with the time translation,
the translations, the boosts and the rotations of Minkowski space as leading terms, and their symmetric gradients, each
correction one order faster; the boost's correction at $\rho^1$, no indicial root, so without the source's logarithm
(6.31) and without its formal solution lemma; the translations' at $\rho^2$, which needs $e_\Upsilon\gamma_\Upsilon^2>0$;
six Killing rotations at zero rotation. Findings (D$''$1)-(D$''$5). Written (D223).

## Part III.D'''

`PART-III-D4-GENSTATES.md`. [Hin26] section 6.5.2 at $n = 4$. Lemma 2.1: solving the zero energy equation with a
prescribed leading term, by a hand step, the formal solution lemma (III.A Lemma 1.5) and the zero energy inverse
(III.D$'$ Lemma 5.1), the roots needed only on the leading coefficient's type. Proposition 3.1 (Proposition 6.18): the
generalized zero energy states -- polynomials in $t_*$ in the kernel of the gauge potential operator -- on the time
translation (no logarithm), the boosts and the rotations to higher order, and the four classes on the roots below $-1$
with the source's degrees, each stationary correction two orders below its leading term; the leading terms computed on
Minkowski space (`genstates5.py`, `puregauge5.py`). Deferred to the part on [Hin26] section 8: that these leading terms
span the kernels of $\bar L(0)$'s indicial families. Findings (D$'''$1)-(D$'''$6), among them a misprint in the
source's recursion and a normalisation in its (6.39a). Written (D224).

## Part III.E

`PART-III-E-CONSTRAINT.md`. [Hin26] section 7 to Proposition 7.3 at $n = 4$. Theorem 1.1, the source's Theorem 7.1 at
$n = 4$ (the summary of [Hin26a]), is stated as the input and is proved in Part IV. Lemma 2.1 (Lemma 7.2): the adjoint
of the constraint propagation operator at zero energy is invertible on b-weights $\alpha\in(0,C_0+2]$ with $s\le C_0+1$,
its indicial roots $2-\bar\lambda$; inverse images are partially polyhomogeneous and vanish inside the horizon.
Proposition 3.1 (Proposition 7.3): the large zero energy dual states built from the time translation, the four
translations and the six rotations, whose trace-reversed symmetric gradients decay, eleven at zero rotation against the
source's seven. Findings (E1)-(E4): the weights move by one (the Coulomb root is 2, the source's 1); the corrections are
one order faster; the eleven states; the input. Section 7.2.1 is Part III.E$'$. Written (D225).