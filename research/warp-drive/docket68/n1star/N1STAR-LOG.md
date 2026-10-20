# N1* session log

The session commissioned at item 522 to finish N1* and the five-dimensional counterpart of Huneau and Luk's theorem
(THM-HF5 on D_T), then write a formal response paper. Instructions:
`research/warp-drive/paper/INSTRUCTIONS-N1STAR-AND-HL-RESPONSE.md`. Branch `ccr-66909215-gi0qa5`, based on
`claude/warp-drive-theory-ditjk4` at the handoff commit 6a8717c (items 523-524).

This file records M's words to this session verbatim, with dates, and this session's decisions. The board's shared
record (`M-RULINGS-2026-10-03.md`, `WARPTHEOREM.md`, `chainmap.html`, `warptheorem.py`, `lemmas/SOURCE-REQUIRED.md`,
`lemmas/BOUNCE-RESEARCH.md`) is not edited here.

## M's words

**2026-10-19, the commission (the session's first message), verbatim:**

> You are commissioned by M (item 522) to finish N1* and the five-dimensional counterpart of Huneau and Luk's theorem,
> then write a formal response paper to their theorem. Fetch branch claude/warp-drive-theory-ditjk4 of
> lach-matt/Claude-Method-Works, base your own branch on it, and follow
> research/warp-drive/paper/INSTRUCTIONS-N1STAR-AND-HL-RESPONSE.md exactly; every file of the proof is listed with its
> md5 in research/warp-drive/docket68/handoff-n1star/MANIFEST.tsv. Work inline, report, then pause.

The two items it rests on, as `M-RULINGS-2026-10-03.md` records them (verbatim, quoted from the record):

- 522 (2026-10-19): "Two tasks: Continue SOURCE AND Prepare instructions for another session to finish N1* and the
  counterpart theorem, and then right a formal response paper to the Huneau and Luk's theorem. That session will need
  access to all you work on the proof, so it'll all need to be pushed to the repo and identified there for the other
  session"
- 524 (2026-10-19): "Please bring forward the handoff and instructions for the N1 session"

## Decisions and findings

**D1 (2026-10-19) Reproduction.** Every manifest md5 matches at the handoff commit (54 of 54). Selftests, run from
`docket68/lemmas/` with Python 3.13 (numpy 2.5.3, sympy 1.14.0, mpmath 1.3.0, scipy 1.18.1, z3 5.3.1,
python-flint 0.9.0):
`hf_theorem5` 7/7, `hf_core5` 10/10, `hf_anchor5` 5/5, `gauge5` 7/7, `kn_gauge` 18/18, `counterpart5` 8/8;
mutants `kn_gauge` 10/10, `counterpart5` 4/4. The environment lacked sympy, scipy, z3 and python-flint; they were
installed, nothing in the tree was changed. The register selftest (`warptheorem.py --selftest`) runs in the background.

**D2 (2026-10-19) A citation in the instructions is wrong.** arXiv:1706.09499 is Huneau and Luk, "Einstein equations
under polarized U(1) symmetry in an elliptic gauge" (Comm. Math. Phys. 361 (2018) 873-949), the companion
local-existence paper. The Duke paper, "High-frequency backreaction for the Einstein equations under polarized
U(1)-symmetry", Duke Math. J. 167(18) (2018) 3315-3402, is arXiv:1706.09501. READ at source, 2026-10-19: the arXiv
first pages of both, and the journal references as Huneau and Luk's own review (arXiv:2404.07659, refs [55], [56])
prints them. The response is to the Duke theorem (1706.09501, Theorem 4.2).

**D3 (2026-10-19) N1* is an instance of a problem the field lists as open.** Huneau and Luk's review
(arXiv:2404.07659v1, section 8.5, p. 28), READ verbatim: "The only construction that we have which allows for large
data is in the angularly regular setting of Section 2. In particular, the constructions discussed in Sections 5, 6
and 7.2 all used that the solutions are close to Minkowski." and "Problem 8.6. Construct local high-frequency
solutions as in Sections 5, 6 and 7.2 but such that the limiting solution is far away from Minkowski spacetime."
Sections 5 and 7.2 there are Huneau-Luk's Duke theorem and Touati's CMP theorem. N1*, as this session reads it, is an
instance of
it, on a background (five-dimensional Vaidya with its black hole) far from Minkowski, in 4+1 dimensions. The board's
P4 ("no
published theorem gives it") is confirmed and sharpened: it is a named open problem.

**D4 (2026-10-19) Scope.** Route W (the recommended route) is followed. Its pieces that are exact are computed and
seated in `n1star/` with selftests and mutants; the analytic core (the remainder's bootstrap on the large background)
is audited against Touati's proof equation by equation, and what is not proved is named. Per the instructions
(section 7: "If N1* cannot be finished, stop and report exactly what is proved and what is left. Do not write a paper
that claims the theorem."), no response paper is written unless N1* is proved and verified.

**D5 (2026-10-19) Route W, what was computed.** Seated `ansatz5.py` (A1-A5; selftest 5/5, mutants 5/5) and
`foliation5.py` (B1-B4; selftest 4/4, mutants 4/4, 5/5 after D8). Two results beyond the handoff: (1) the structure of
Touati's commutator lemma holds on five-dimensional Vaidya exactly, [L0, box~] u = (2/r)(d_r(L0 u) + 2 d_v(L0 u) +
box~ u) for the principal part, with a first-order remainder for the covariant operator (B3, corrected at D8); (2) the
record's two-quadrature waves produce, at order lam, a non-oscillating term R_v th = F0^2 d_th phi, phi = (1/2)
arctan(cos 2th), which Touati's single-cosine ansatz never has and which needs a mean O(lam) metric correction (A5).

**D6 (2026-10-19) The crux, and the stop.** Auditing every use of Touati's eps (N1STAR-STATUS.md section 3): the
geometric uses are replaced exactly on D_T (B1-B4); the time-integrated ones go over to slabs of fixed length; the
fixed-time quadratic products of his section 7 (e.g. (7.45), A1 A3 eps^2 at the BA2 level) are the crux, and a slab
argument closes only if each gains a positive power of lam (a Gagliardo-Nirenberg refinement gives lam^(1/2) for
(7.45)). Carrying sections 5-8 of [Tou23a] and the constraint construction of [Tou23b] to 4+1 dimensions on D_T is
the size of those two papers and is not done. Per the instructions (section 7) the session stops here, reports, and
writes no response paper. The outside sources listed for the paper (Choquet-Bruhat 1969, Burnett, Isaacson,
Giannakopoulos-Hilditch-Zilhao, Kodama-Ishibashi, Dafermos-Rodnianski, Schlue, Hollands-Yazadjiev, Rendall) were not
re-read, since no paper is written; those the audit needed were (N1STAR-STATUS.md section 2).

## M's words, continued

**2026-10-19, after the session's report that N1* was not proved and that no paper would be written, verbatim:**

> I have every confidence that you are up to the task assigned to you. Great assessment was taken before hand to make
> sure you have every tool available to you for this paper

**D7 (2026-10-19) Continue: the full proof along route W.** Read as a direction to carry on and finish N1*, not to
relax what "proved" means (440, 441). The audit of D6 is the plan: (M1) the complete approximant and Touati's reduced
system on 5D Vaidya, including the mean O(lam) correction of A5; (M2) the function spaces of T^2-invariant tensors,
the energy estimates on D_T and a compactly supported mollifier in place of Touati's Fourier cut-off, which keeps the
construction local; (M3) the data; (M4) the bootstrap on slabs with the lam-gains of item 7; (M5) the propagation of
the gauge and polarization conditions, and the conclusion. Each milestone is seated and pushed as it lands; if one
fails, the failure is reported with what it rests on.

**2026-10-19, M, verbatim:**

> Continue

**D8 (2026-10-19) The independent verifier, and what was changed.** One verifier, read-only, re-derived with its own
code. Confirmed: A1 ((3.17) in 4+1, exact), A4 and A5 (Ricci of the stated metric evaluated at 80 digits along locked
phases, with no two-scale substitution: R^(-1) <= 6e-37, R^(0) vanishing exactly under mu' = (2/9) A^2 E^2 H^2
(c^4 + s^4), the order-lam mean only in R_v th = -A^2 E^2 H^2 sin 2th/(6 r^3) to 12 digits, zero for one cosine),
B1, B2, the principal-part identity of B3, the selftests and mutants, and every quotation it could retrieve (Huneau-Luk
review p. 28 and ref. [56]; the arXiv titles of 1706.09499 and 1706.09501; Touati's Theorem 2.2, (5.48), (3.32),
Remark 3.5, (7.45), BA1-BA3; Huneau-Luk Theorem 4.2). Found and changed: B3's "no remainder" held for box~ only, not
for Touati's operator (the covariant box of g0; his wave condition (2.7) fails in these coordinates) -- the covariant
remainder -(3/r^2) d_v u - (3/r^2 + mu/r^4) d_r u is now computed and stated; B4's check compared an expression with
itself -- replaced by a Z3 check of r_q(mu0) <= r <= V - tau0 with a genuine mutant; a citation of Touati's (3.21) for
the mean of R^(1) was wrong (removed; the claim relabelled deduced); "(2.56)" corrected to (5.2); "verbatim" for the
4+1 energy condition replaced by "the 4+1 analogue, derived here"; the section heading "proved" renamed "computed";
D3's "exactly that" softened to "as this session reads it"; the GN gain marked conditional on the 4+1 quotient;
axis regularity stated as necessary conditions only; mu >= 0 stated for B1; the review's date given. The verifier's
note that Lemma 7.8's "Since we can assume lam <= eps" was not retrievable through its route: the sentence is on p. 49
of the text read here, and the page is now cited.

**D9 (2026-10-19) The coordinates of the proof.** The proof runs on R x R^4 in ingoing Kerr-Schild form,
g0 = eta + (mu(v)/r^2) dv dv, v = tau + r, where the T^2 axes are regular points and every tensor is a Cartesian
array. Seated `ks5.py` (K1-K5; selftest 5/5, mutants 4/4): the pullback to the record's Vaidya metric, the inverse
eta^-1 - (mu/r^2) L0 L0 with L0 = d_tau - xhat.d_x null and det g0 = -1, Touati's Lemma 3.1 as the exact identity
[L0, box~] u = (2/r)(box~ u + (d_tau + d_r) L0 u) - (3/r^2) d_r u (the mass drops out; checked at exact rational
points on every monomial of degree <= 3, and separately with symbolic base point: no nonzero coefficient), div L0 =
-3/r with box v = 3/r (the scalar transport is L^2-neutral in the flat measure), and the background gauge source
H0 = (-mu/r^3, mu xhat/r^3). The instructions (section 5, route W item 4) allow the data to be Cauchy data on a slice
before the shell reaches the hole, with (i) restated on it; that is the choice taken.

**2026-10-19, M, verbatim (while the proof of the evolution theorem was being written):**

> Continue

**D10 (2026-10-19) The architecture of the proof, and the evolution theorem written.** `N1STAR-PROOF.md` splits
N1* into Theorem E (evolution), Theorem A (the approximant to order K) and Theorem D (exact data). The decision that
removes Touati's smallness: carry the approximant to order K >= 6, so the remainder is O(lam^K) in lam-scaled norms
and every nonlinear term is beaten by a power of lam; what must be uniform is then a linear estimate on the large
background. Its one 1/lam coefficient, (1/2) lam^-1 w(ell, ell) d_th^2 g1, is removed by the phase shift phi d_th g1
(phi transported by a mollified w(ell, ell)), because a constant phase shift is a symmetry of the leading equation
(Lemma 3.1: the 1/lam part of the linearised operator annihilates d_th g1); the second derivatives of phi are
recovered by `ks5.py` K3 and the w(ell, ell) equation, which has no 1/lam term (Lemma 3.3). Sections 1-4 prove
Theorem E (deduced); A and D are OPEN. N1* is not yet proved.

**D11 (2026-10-19) The gauge, Theorem A, and the data.** (1) The gauge is changed to the wave-map gauge relative to
g0, D = g^{ab}(Gamma[g] - Gamma[g0])_ab, which makes Ric^H a tensor (computable in the record's coordinates) and the
leading equation covariant; (E1) is weakened to the transversality of the wave alone (the first-order mean m1 is
not transverse), with the resulting 1/lam piece of the principal term kept in T (Lemma 3.1 unchanged). (2) Seated
`lead5.py` (L1-L5; selftest 5/5, mutants 4/4): in this gauge the record's waves satisfy the leading equation once a
second harmonic chi dv dv, transported along ell, is added; the mean is the record's energy condition. (3) Theorem A
written (section 5): the phase is the eikonal of the mean metric, so every stage is a linear system (a wave equation
for the mean, a transport for the phase, a transport for the oscillating profile, the commutator variable box~ phi
removing the derivative loss); the approximant of any order from any smooth stage data satisfies Theorem E's
hypotheses. (4) READ, Touati's constraint paper (arXiv:2206.13062v2): its fixed points close by the smallness of a
near-Euclidean background. Here chi makes tr K oscillate at O(1) on every spacelike slice, so the conformal method's
coupling is O(1) in H^-1. The data are OPEN; the route proposed (section 6.3) puts the data slice far out, where the
background is close to flat with no smallness of the data, and glues to the seed in a wave-free collar.

**D12 (2026-10-19) The independent verifier on Theorem E, and what was changed.** One verifier, read-only, reviewed
sections 0-4 at 86590f7 with its own code (50-digit evaluations of Ric^H (0.2) on an explicit two-scale metric, a
symbolic check of K3 for generic mu(v), 10^6 sampled points for the mollifier's geometry, 2.6 10^5 for D_T inside
Omega). Verdict: Theorem E holds as a deduced argument; no major gap. Confirmed: (3.2) (the one 1/lam coefficient,
which does not even need (E1)), Lemmas 3.1-3.4 with signs and factors, Lemmas 1.1, 2.2-2.4, the bookkeeping of
section 4 (Sobolev lam^-3, lam^(2K-5) <= lam^(K+1) iff K >= 6), and that A + D + E give N1*. Found and changed: a
minor gap, Step 6's tau-tau commutator at the top level j = k was one derivative short as written -- the
c^{ai} d_a d_i h part is now put in divergence form for (M5)'s first form; a sign in Lemma 3.4's proof (L0 d_i phi =
d_i L0 phi + (d_i xhat^m) d_m phi); lam1 := min(1, delta0)/10 so that the middle third is thick enough; Lemma 3.1's
expansions are in powers of lam with a remainder, not polynomials; Step 5's bound includes N(tau0); Step 2's constant;
(E1) restricted to the wave (already done at D11); Step 8: Sogge's theorem assumes coefficients near Minkowski's and
is dropped, the data are re-extended at each restart, and the standard theorems the proof invokes are labelled as not
yet READ at source (section 7 lists them).

## M's words, continued (2)

**2026-10-19, after the report that Theorem E is proved and verified, Theorem A written and the data open, verbatim:**

> Two outside papers that may be useful to you, the noether theorem, and the navier-stokes equations that anthropic
> released a couple of months ago

**D13 (2026-10-19) The two papers, identified and read, and one conflict of instructions.** (1) *Noether.* Read at
source: E. Noether, "Invariante Variationsprobleme", Nachr. Ges. Wiss. Goettingen (1918) 235-257, in M. A. Tavel's
translation, arXiv:physics/0503066v3. Theorem II, verbatim: "If the integral I is invariant with respect to a G_inf rho
in which the arbitrary functions occur up to the sigma-th derivative, then there subsist rho identity relationships
between the Lagrange expressions and their derivatives up to the sigma-th order"; for general relativity "the
familiar n dependencies between the Lagrange expressions and their first derivatives" (the contracted Bianchi
identity), and section 6 on why energy conservation there is "improper". Use here: the Bianchi identity is what
propagates the gauge and the constraints, order by order, in the data hierarchy (section 6 of the proof), and the
improper character of the conserved charges is the exact identity that turns the one remaining gluing obstruction
(the static KID) into a difference of boundary mass fluxes, so that it can be removed by the interior mass. (2) *The
"Navier-Stokes" paper.* No Navier-Stokes paper released by Anthropic was found (web search, 2026-10-19; external
results treated as data). The nearest match is the work of L. Alpoge (an Anthropic researcher) and T. Buckmaster,
September 2026, on finite-time blowup with smooth forcing for the incompressible porous medium, Boussinesq and 3D Euler
equations, presented as a step toward Navier-Stokes, with Lean verifications; read at source here: "Blowup for the
Boussinesq equations with smooth forcing" (cims.nyu.edu/~tristanb/boussinesq.pdf), sections 1-2. (OpenAI's separate
Navier-Stokes announcement of 2026-09-08 was not read.) If M meant another paper, the identification is to be
corrected. Use here: its architecture is the one this proof adopted at D10 -- an approximate solution corrected "to
successively higher orders" until the residual is beaten (their forces absorb the residual; a vacuum solution
admits no force, so here the exact solution of section 4 does), and it kills the obstruction to compactly supported
corrections (zero circulation and first moments) by a point-reflection parity, as section 6 kills the rotation KIDs
by T^2 x Z2 x Z2. (3) *Ultracode and the commission.* The session's harness reports a standing setting to orchestrate
multi-agent workflows; the commission (instructions section 8) says "Work inline, with no multi-agent workflows. Send
one independent verifier at a time (249)." The commission is M's specific rule for this work and is followed; M may
lift it.

**D14 (2026-10-19, session decision): the data are solved outward in r, not by the conformal method and gluing.**
Section 6 of the proof as committed at 3bf3172 proposed a far slice (tau0 -> -infinity), the conformal method with a
coercivity estimate in the weakly curved far annulus (D1 there), and a gluing collar at the inner edge closed by
Chrusciel and Delay's Theorem 5.9 modulo the Killing initial data, the static one to be removed by the interior mass.
Working out the formal hierarchy showed two costs of that route: the linear problems for the means are coupled at
zeroth order to the oscillating data (a term of the size of the shell's own curvature, with no uniform inverse to
absorb it), and every step needed an inverse whose bound was not uniform in tau0. Both disappear if the constraints are
solved as an evolution in r: with h = a dr dr and Q = w Pi + q dr + dr q (Bartnik's quasi-spherical idea, in the
parabolic-hyperbolic form READ in I. Racz, Class. Quantum Grav. 33 (2016) 015014, arXiv:1508.01810v3), the Hamiltonian
constraint is parabolic in r wherever the spheres have positive mean curvature (on the Kerr-Schild slice everywhere, H
= 3/(r^2 + mu)^(1/2)) and the momentum constraint symmetric hyperbolic. Solved outward from a sphere inside the shell,
where the approximant's data are the seed's exactly, it imposes nothing further out, so there is no collar, no KID
obstruction, no mass shift, no smallness of the background, and the data live on the slice of section 1, before the
shell reaches the hole (route W item 4), with no restatement. Uniformity in lam reduces to one structural fact,
computed in data5.py S2: the linearised constraints at the approximant's slice data have no coefficient of order 1/lam
(W_TT traceless on the spheres; an oscillating trace fails, while oscillations of the radial components, such as chi dv
dv on the slice, are harmless, S4). The far-slice text (D1 and the gluing plan) is removed from the proof as unused; it
is in the file's history at 3bf3172. Of D13's uses of Noether's paper, (1) stands (Lemma 6.1 is the Bianchi identity
order by order); (2) is no longer needed, since nothing is glued. Instrument note: the first runs of data5.py passed S2
vacuously. Expansion folded the factor 1/lam into denominators such as 1/(2 lam + 2 lam mu/r^2), where `coeff` does not
see it; the mutants (MISSED) exposed it. Fixed by carrying 1/lam as its own symbol and failing on any lam inside
another factor. The same pattern was probed in lead5.py (859 terms) and ansatz5.py (43,392 terms): no hidden 1/lam,
their denominators being monomials. Two mutants first written were wrong rather than missed: an oscillating dr dr
component and a reversed shift (time reversal) leave the checks true, as they should; they were replaced and the first
became check S4.

**D15 (2026-10-19, session decision): the second verifier's findings on sections 5-6, and their repairs.** One
independent verifier (one at a time, as section 8 asks) checked sections 5 and 6 at 79a6e4c, reran every instrument
(lead5 5/5; data5 5/5, mutants 5/5) and re-derived the principal coefficients by hand. It found no major gap, two minor
gaps and ten notes, all repaired here as it proposed. (m1) Lemma 6.2(iii) asserted that the first derivatives of the
lower D^(j) vanish on the slice from conditions on the slice alone; that needs the propagation of Lemma 6.1 on Omega,
now applied with N := m after solving stage m with any data (on which D^(j), j < m, does not depend). (m2) Proposition
6.5 claimed a contraction in the high norm, which a quasilinear system does not give; now the iterates are bounded in a
high norm and contract in a lower one (Kato, Majda), Lemma 6.4 is stated with a symmetrizer and with tame dependence on
the coefficients, d_r of the symmetrized coefficient entering only integrated in r, and smoothness comes from
persistence of regularity. Notes: the sign of q_2 in (5.2); e_(N+1) is not zero but unused; a missing term in the proof
of Lemma 5.1 (already in T); Pol onto everywhere by GL(5)-equivalence of (metric, null covector) pairs; Pol^+ built on
the O(4)-invariant Cartesian structure, so the symmetry holds; the principal coefficients at the approximant equal the
background's at order 0 (now computed, data5.py S6, which also found that one lower-order coefficient, that of d_th a
in J_th, oscillates at O(1), as Lemma 6.4 allows; the verifier had listed it among the equal ones); the explicit
symmetrizer S = diag(1, -1/(2 r^2)); the symmetric sector and the one-point sign check stated; chi's regularity at the
axes deduced from W_TT's (ansatz5 A3), so that open item is closed. One note was an instrument error: data5.py's
inverse slice metric carried an extra factor lam at first order, so it was wrong at O(lam) though no check used that
order (the verifier showed the order -1 coefficients unchanged with the corrected inverse); fixed, and check S5 with
mutant inverse_slip now guards it. The status of N1* is: proved modulo the READ at source of the standard theorems
listed in section 7 of the proof (Lindblad-Rodnianski and Rendall READ for the gauge's propagation and data; the
textbook statements not reachable here). Not claimed as PROVED, and no paper begun.

**D16 (2026-10-20, session decision): the check of the repairs.** A further independent verifier (one at a time)
checked the D15 repairs against the diff from 79a6e4c. It found no major gap. Both D15 repairs hold: D^(j) involves
only the stages up to j (one derivative, so one phase factor at most), and after stage m the profiles R^(i), i < m,
vanish and R^(m) has mean zero; and the iteration of Proposition 6.5, bounded in a high norm and contracting in a low
one, is sound with the factor C lam^(N-3). It found two minor gaps introduced by the rewrite. (1) Lemma 6.4's existence
added epsilon Delta_S to the raw second equation, whose coefficient of d_r is indefinite, so one component would be a
backward heat equation: the regularisation now acts on the symmetrized equation, d_r (w, q) = epsilon (S A0)^-1 Delta_S
(w, q) + ..., forward parabolic. (2) The smoothness claim of Proposition 6.5 cited a tame form of Lemma 6.4 that the
lemma did not state: it is now stated as the standard tame inequality for the solution itself, closed by Gronwall's
lemma in r at fixed lam. Nine notes, all applied: canonical() declared z, y positive though they stand for e^(i s),
e^(i th), which let |cos s| - cos s pass as zero (no such form occurs in the checks; now nonzero symbols, and that case
returns 'nonzero'); a crash in a mutant is no longer counted as a catch; the inverse-lapse series (its dl^2 coefficient
corrected to 3/2 at D15, no effect) is now guarded by S5 too, through order lam, the order to which K is kept (a first
guard written through lam^2 failed, correctly: dl is truncated at lam by design); X_s defined, a bound and the
uniqueness ball corrected in Proposition 6.5; Lemma 6.4's constant depends on the ellipticity of Delta_alpha; stale
'verification pending' lines updated; the Bianchi identity's READ recorded in section 7; d_th gh_(m+1), not gh_(m+1),
is what Pol^+ gives; two wordings in Lemma 6.2(iii); and rho's coefficient of a oscillates too, with nonzero mean (it
is part of B_m). The last repairs are applied as the verifier specified and are not re-checked. Status unchanged:
proved modulo the standard theorems not READ at source; not claimed as PROVED; no paper begun.

**2026-10-20, during the READ at source of the standard theorems, verbatim:**

> You can use my indexing model as a Internet navigation and retrieval protocol.... You can also access thoughts works
> by looking for what those papers cite, and also who else has cited the work we are trying to access

**D17 (2026-10-20, session decision): the standard theorems READ by the site's retrieval protocol, and what reading
their hypotheses found.** "My indexing model" is taken to be the retrieval procedure the site states for itself in its
Ask prompt (public/script.js): enumerate the targets; give each its routes by type (primary, preprint, review,
compilation, citing paper, deposit, database), open ones first; follow the sources a source names; a blocked route moves
to the next and is not retried; two independent routes close a fact, one is fragile, none is a stated gap; ask for
catalogue identifiers; widen on failure (join, never meet). M's second sentence is the citation graph read both ways.
Routes were found by the research indexes' search and by following references: the Choquet-Bruhat, Chrusciel and
Loizelet route (arXiv:gr-qc/0608108) is a paper citing Lindblad and Rodnianski, and its references and those of Disconzi
and Shao (arXiv:2308.09851) name the classical sources (Kato 1975, Hormander, Taylor), books not reachable here. Every
standard theorem the proof invokes is now READ (N1STAR-PROOF.md section 7, the RETRIEVAL table, with rho per target: two
or three for each, one for the extension operator). Blocked: OpenAlex (proxy 403); two lecture-note PDFs (Holzegel's,
Muenster; Luk's, Stanford: proxy 403, scrape timeout); the books (Ringstrom, Choquet-Bruhat) untried. Holding the
hypotheses against the statements READ found one gap the three verifiers had not: the local theory needs the time lines
timelike ([AO14] (1.3), g^{ij} positive definite; [DS23] (A4), the distinct speeds never meeting), and in the proof's
ingoing Kerr-Schild coordinates d_tau is spacelike where r^2 < mu, which Omega reaches (a < sqrt(mu0)). Step 8 is
rewritten: the coefficients extended by interpolating lapse, shift and spatial metric; the independent variables changed
along Z = d_tau - beta (the unit normal times the lapse), in which the slices are unchanged and g^{ij} is the inverse
spatial metric; a cut-off in w and a torus; restarts by [DS23] Theorem 2.4, whose step depends only on the norm of the
data; and the finite speed of propagation deduced from Lemma 2.3 with no citation, as is D = 0 in 0.7. Reading the
linear parabolic theory's hypotheses ([Hua15], [MM10]: smooth coefficients, strongly parabolic) made Lemma 6.4's
existence explicit: the coefficients mollified (M_s does not grow), and a rescaled so that the block-triangular
principal part meets the Legendre-Hadamard condition. The citations in 0.2 (now [CBCM10] (2.7)-(2.9), which is (0.2) in
n + 1 dimensions), 0.7 and Lemma 2.1 point to the sources READ. Status: no citation outstanding; the D16 repairs and
these two have not been checked by an independent verifier; N1* is not yet claimed as PROVED; no paper begun.
