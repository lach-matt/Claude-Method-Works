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
| I.A | [Hin26c] 9.1-9.2 | bounded nonzero frequencies, Theorem 9.5, bundles, uniform in b | written (D185); seated (D186) |
| I.B | [Hin26c] 9.3 | high energies, trapping with (5.9)'s conjugation, Theorem 9.16 | in progress |
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
