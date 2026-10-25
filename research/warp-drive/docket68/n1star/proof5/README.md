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
| I.A | [Hin26c] 9.1-9.2 | bounded nonzero frequencies, Theorem 9.5, bundles, uniform in b | **proved** (D189) |
| I.B | [Hin26c] 9.3 | high energies, trapping with (5.9)'s conjugation, Theorem 9.16 | seated (D189) |
| I.C | [Hin26c] 9.4-9.6 | zero energy (9.36), tf-normal operators (9.38), low energy (9.41), 9.39, 9.43 | to do |
| II | [Hin26c] 7-8, 10-13 | spacetime estimates, decay at iota+ and K+, the iteration | to do |
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

The seventy-sixth verifier, reading Part I.B, checked both repairs and confirmed them (D189). Part I.A is **proved**:
written, read line by line, every finding seated and every repair read.

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
