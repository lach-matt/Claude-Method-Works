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

**2026-10-20, to the report that the paper is written and audited by one verifier, verbatim (the four items were
the report's lines quoted before each answer):**

> What it lists as not proved: - these need to be proved
>
> the title; - should be a statement that answers the question of the theorem proof, with a sub title : The Formal
> Counterpart to Huneau and Luk.
>
> whether and where the paper is released; - will be published to my website (via another session that handles the
> site build, but you are welcome to look at the site and it's materials)
>
> whether to open a pull request (the instructions say not to unless you ask). - yes when the work is finished.

**2026-10-20, M's answers to the session's two questions (multiple choice), verbatim:** to "Which rule governs the new
proofs?" (the commission's inline rule, or multi-agent orchestration, now switched on in the session): "Inline only".
To how to treat late-time settling and the application at 10 l5: "Prove three, attack two (Recommended)" (prove part
(iii) for lam > 0, the mean-mass rate and the data at past null infinity; then attempt late-time settling and a
finite-wavelength statement, reporting exactly how far each gets and never claiming more).

**2026-10-20, to the report of D27-D30 (the session's lines quoted before each answer), verbatim:**

> Data at past null infinity: not proved. I said it looked provable; that was wrong as the method stands. Over an
> infinite past, the phase correction builds up, and with the current estimates that gives a growth no power of λ can
> beat. I found the structure that should close it, but it amounts to a separate theorem about as large as the uniform
> existence proof itself (called N1* in the working notes).  - then we need to build, and include that proof as well
>
> Late-time settling, attacked: it is open in the field. Linear stability is known (Ishibashi–Kodama), and nonlinear
> stability is known only for a smaller symmetry class (Holzegel). Our waves depend on an angle and fall outside that
> class. Settling would follow from small-data stability in our class, but only once the solution is also built
> outside the current domain. - use the copper study from the warp theorem work, it was built and models and measured
> under different constant conditions of varying universes. It may be useful to build from.
>
> Wavelength 10 l5, attacked: no high-frequency theorem can reach it. At that wavelength the waves are as long as the
> curvature length: 10 times it on the boundary, and 2.91 or 0.92 times it at the horizon (for μ0/l5² = 100 and
> 1000). - this is why I recommended the navier-stokes equations.

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

**D18 (2026-10-20, session decision): the fourth verifier's findings on the D16 and D17 repairs, and their repairs.**
One independent verifier (one at a time) checked the D16 repairs and the D17 repairs against the diffs, with the saved
texts of the sources READ. It found no major gap: the spacelike time lines in the coordinates of 0.1 confirmed (g0^{ij}
has a negative eigenvalue at r^2 < mu, and Omega reaches there), Step 8's construction meeting [DS23] (A1)-(A4) and
[AO14] (1.3), Lemma 2.3's uniqueness on Omega and D = 0 in 0.7, the rescaling in Lemma 6.4, and Proposition 6.5 after
D16 all holding; every quote checked in section 7 is verbatim in its source. One minor gap: the linear parabolic theory
cited for Lemma 6.4's existence does not cover it, since [MM10] Theorem 1.1 concerns a scalar equation ("smooth initial
datum u0 : M -> R") and the [Hua15] sentence was from its introduction, its setting being Hoelder. Repaired as it
proposed, by a Faedo-Galerkin argument in spherical harmonics (the projection commutes with the Killing fields, so the
energy identities hold for the approximations unchanged; d_r of the hyperbolic unknowns is bounded by testing the
projected equation in turn, S A0 > 0), with no citation, and the epsilon-regularisation and mollification are gone. Five
notes, repaired: one universal extension operator for every order replaces the per-order one in Step 8 (iv) so that
smooth data extend smoothly ([LY22] Theorem 26, READ, with Seeley's operator restated there), and extends g_app beyond
Omega, where it was not defined (Stein's or Rychkov's operator on the Lipschitz domain Omega, READ as restated in
[SY21]; Seeley's original, on ams.org, could not be fetched); Proposition 6.5's smoothness by induction on the iterates
with a Volterra bound E_(i+1) <= A + B int E_i, needing no smallness; the paraphrase of [CBCM10] (2.7) marked. The
SO(4)-averaging note fell with the mollification. The [LR05] and [CD03] quotes could not be checked from the saved
texts; they were READ 2026-10-19. data5.py --mutants: 6/6. Status: no citation outstanding; the D18 repairs not yet
re-checked; N1* not yet claimed as PROVED; no paper begun.

**D19 (2026-10-20, session decision): the fifth verifier's findings on the D18 repairs, and their repairs.** One
independent verifier (one at a time) checked the D18 repairs against the diff and the saved source texts. No major gap.
Lemma 6.4's Faedo-Galerkin existence holds (the ODE system well posed, S A0 being absolutely continuous in r; the test
functions in the range of the projection; the bound on d_r of the hyperbolic unknowns by induction), Step 8 (i) and (iv)
hold (Omega is a trapezoid in (tau, r) times S^3, so bounded and Lipschitz; [SY21]'s Stein covers W^(k,infinity); [LY22]
Theorem 26 covers every H^m), and every new quote in section 7 is in its source. Two minor gaps, repaired as it
proposed. (1) Proposition 6.5's smoothness: the remainder has a term q_th d_r a in J_th (it computed the coefficient
r^4/(r^2+mu)^2 in the symmetric class), which as a source at U_i puts E_i(r) itself, not its integral, on the right of
the X_(s'') bound, so lam0 would depend on s''. Such terms are now frozen as coefficients (f in (6.4)) multiplying d_r
a_(i+1), and the bound is E_(i+1) <= A + int omega_i E_i with omega_i bounded in L^2 uniformly, giving E_i(r) <= A sum_k
W^k ((r - a)^k / k!)^(1/2) with no smallness; the contraction treats the new frozen coefficient as it treats the others.
(2) [DS23] (A1) asks for bounds uniform in t, and the coordinates of Step 8 (ii) degenerate as |tau| grows (it measured
g^rr in y against x growing to 6.3e8 by tau - tau0 = 40): the coefficients are now clamped in time, theta(tau) = tau on
[tau0 - 1, tau_end + 1] and constant outside a slightly larger interval. Four notes, applied: the projection on the
covector q is the Hodge Laplacian's, with X^I acting by Lie derivatives; Lemma 6.4 asks only that M_s be finite, not
smooth coefficients; the data are extended in x and then composed with Phi; the uniformity in tau of the extension
constants is deduced from [LY22] Lemma 27's proof, not READ. Status: no citation outstanding; the D19 repairs not yet
re-checked; N1* not yet claimed as PROVED; no paper begun.

**D20 (2026-10-20, session decision): the sixth verifier's findings on the D19 repairs, and their repair.** One
independent verifier (one at a time) checked the D19 repairs. No major gap: the time clamp gives [DS23] (A1)-(A4)
uniformly in t and changes nothing on [tau0, tau_end] (Phi has bounded derivatives on the clamped interval, by
Gronwall); the extension in x then composition with Phi, with the uniformity in tau deduced, holds; Lemma 6.4 uses no
smoothness of its coefficients, and the projection on 1-forms commutes with Lie derivatives along Killing fields. One
minor gap, with a repair it checked: the coefficient f of d_r a in the J-equation depends on a as well as on (w, q) (it
computed f = -(B k3 - C k2) C / (A C - B^2)^2 for a general symmetric-class gamma and K, and the a d_r a term of the
remainder as its derivative in A, present wherever f is, as on data5.py's data with chi on the slice), so freezing only
its (w, q)-part left a source a_i d_r a_i putting E_i(r) itself on the right. The whole of f is now frozen at U_i, which
Lemma 6.4 admits (f is algebraic in U_i), and the contraction keeps its factor (the extra source is at most C lam^(N-2)
times the difference in the low norm); the density equation has no such term (its coefficient of d_r a, alpha, is
already frozen). Two notes applied: the smoothness bound is stated as E_(i+1)(r) <= A + W (int_a^r E_i^2)^(1/2), which
gives the same induction by Minkowski's inequality; Lemma 6.4 now states the tame form its proof gives. Status: no
citation outstanding; the D20 repair not yet re-checked; N1* not yet claimed as PROVED; no paper begun.

**D21 (2026-10-20, session decision): the seventh verifier's findings, and N1* claimed as PROVED.** One independent
verifier (one at a time) read Proposition 6.5 whole, with the D20 repair and the statement of Lemma 6.4. It found that
Proposition 6.5 holds: computing rho and J in jets for a general symmetric-class gamma and K at random rational points,
with negative controls, it found no d_r a term left in the source once alpha, S A0, S A^B and the whole of f are frozen
(what remains, d_S a (w, q), d_S a a, (d_S a)^2 and algebraic terms, is bounded at each r by E_i(r), so in L^2 by (int
E_i^2)^(1/2)); the contraction factor C lam^(N-3) unchanged, the extra source using ||d_r a_i||_{L^2 H^(s0)}, part of
X_(s0); the induction exact by Minkowski's inequality, A and W uniform in i. One minor gap: Lemma 6.4's tame clause, as
D20 stated it, gives only E_(i+1)(r) <= A + W E_i(r) when read with M_s's supremum norms, the form D19 rejected; the
lemma's proof gives d_r Z <= omega_0 Z + m_(s'') omega_s, hence the integral form, and the clause is restated so, as it
specified. Three notes applied: the weight list (||d_r (w, q)_(i+1)||_inf in it, ||d_r (S A0)||_inf in Gronwall's
exponent); the rate lam^(N-2) at every index (A is proportional to lam^(N-2), W independent of lam); the headings of 0.4
and 0.6 and the README's ranges, which understated the record. Decision: N1* is claimed as PROVED. Every theorem the
proof rests on is deduced here or READ at source with its hypotheses checked; seven verifiers checked the proof and
every round of repairs, none finding a major gap; the last round found the proposition it read to hold, and the one
clause it restated is the form that verifier derived from a proof it had checked. That restatement and the three notes
are the only text no verifier has read after the edit, and the proof file says so. Next, by the instructions: the formal
response paper to Huneau and Luk's theorem, its title saying "proposed"; not begun; it waits for M, as the commission
asks for a report and a pause, and its release is M's decision.

**2026-10-20, to the report of D21 (N1* claimed as PROVED), verbatim:**

> Excellent work. Yes please, continue with the paper

**D22 (2026-10-20, session decision): the paper.** Begun as the instructions' section 9 asks: Markdown in the paper
folder, with a check script that re-derives its numbers independently of the proof's instruments (`response5.py`: the
exact reduction to 2+1 gravity with two free waves, the background's Ricci and Kretschmann scalars and the quantum
boundary, the domain's contractions, the constraints' principal part, each with a negative control). The outside sources
it answers were re-READ for the page numbers the paper cites (2026-10-20): Huneau and Luk, arXiv:1706.09501v1, Theorem
4.2 (p. 10), (1.3)-(1.4) (p. 3), the elliptic gauge (3.4)-(3.5) (p. 7) and Burnett's formulation (p. 1); their review
arXiv:2404.07659v1, Conjectures 1.1-1.2 (p. 2) and section 8.5, Problem 8.6 (p. 28); Touati, arXiv:2206.12318v4, Theorem
2.2 (p. 12), (2.9)-(2.10) (p. 10), section 3.2.2 (p. 20); Luk and Rodnianski, arXiv:2009.08968v1, Theorems 1.9-1.10 (p.
5). The paper claims only what the proof gives: part (i) of the counterpart on D_T with Cauchy data before the shell
reaches the hole (the instructions' route W item 4), the C^0 rate O(lam), bounded derivatives and weak convergence; part
(iv) and the limit are cited from the board's exact instruments; the O(lam^2) mean-mass rate and part (iii) for lam > 0
are computed numerically at two seeds and are listed as not proved. Item 442's verbatim words name the research tree;
the paper quotes them with that word elided and marked.

**D23 (2026-10-20, session decision): the paper written.** `paper/RESPONSE-HL-5D.md`, title proposed, with
`paper/response5.py` (R1-R6, every check passing and every control rejected, about 20 seconds). It states Huneau and
Luk's Theorem 4.2 verbatim (arXiv:1706.09501v1, p. 10) and answers it with Theorem 1 on D_T cap {tau >= tau0}, Cauchy
data on Sigma_tau0, as D22 set out. Found while writing, and carried into the paper rather than left in the notes:
(1) at equality, mu0 = sqrt(72) l5^2, the boundary x = 1 is the seed's horizon for v <= v_start and is null there:
g0^-1(dPhi, dPhi) = 1 - sqrt(mu/(sqrt(72) l5^2)) - r_q mu'/(2 mu) (R6), so it is spacelike exactly where mu >
sqrt(72) l5^2 or mu' > 0, and for g_lam, lam small, when mu0 > sqrt(72) l5^2 (a uniform margin and the C^0 bound of
Theorem E; deduced). hf_theorem5 F2's "inside the horizon the boundary's normal is timelike" is right; the theorem's
"mu0 >= sqrt(72) l5^2" admits the null case. (2) R1 was first written symbolically and did not finish in seven minutes;
it now works from exact 2-jets at three rational points (one second). (3) Two identifiers the proof cited without them,
READ 2026-10-20: [CD03] is Chrusciel and Delay, arXiv:gr-qc/0301073v2, (2.1) on p. 4; [AG22] is F. Angeles,
arXiv:2204.01179v3, the quoted sentence in its abstract (p. 1) and (9.6) on p. 24. (4) Touati's sections 3.2.2-3.2.3
begin on p. 20 and his Lemma 3.1 is on p. 21. (5) In the paper the angular variable is called zeta and the curvature
ratio x_K, since x is also the Cartesian coordinate. The comparison with Huneau and Luk, Touati, and Luk and
Rodnianski is written point by point; the paper names, as an instance in a five-dimensional class and not as an answer
to it, the large-data problem of Huneau and Luk's review (arXiv:2404.07659v1, Problem 8.6, p. 28).

**D24 (2026-10-20, session decision): the work M set after the paper.** The title becomes a statement answering the
question of the theorem, with the subtitle "The Formal Counterpart to Huneau and Luk". The paper goes to M's website
through the site-build session; a pull request is opened when the work is finished. The four items the paper listed as
not proved are taken in M's order of answer: (1) part (iii) for lam > 0, (2) the mean-mass rate, which is computed
before anything is claimed, since an order-lam mean of the two-scale expansion is already on record (ansatz5 A4,
R^(1)_v theta) and the rate may fail, (3) the data at past null infinity, (4) late-time settling and the application at
10 l5 attacked and reported as far as they get. Inline, one verifier at a time.

**D25 (2026-10-20, session decision): part (iii) for lam > 0 proved.** N1STAR-PROOF.md section 8, Proposition 8.1, with
`horizon5.py` (H1-H3, selftest 3/3, mutants 3/3). The outgoing expansion of the spheres {v, r = const} is a smooth
function of g, linear in dg; for g0 it is (2 r^2/(r^2 + mu)) 3 (1 - mu/r^2)/(2 r), with a simple zero at sqrt(mu). The
reason the weakly converging dg does not spoil it: the leading wave enters at order lam^0 only through the trace of
d_th W on the spheres, which vanishes because W(ell, .) = 0 and tr W = 0 (lead5 L5), and along a column the phase is
constant, so the r-derivative of a profile carries no 1/lam. With the remainder's C^2 bound (Theorem E, Step 1, K >= 6),
each column has at most one zero, exactly one within C lam of sqrt(mu) on the columns that reach across it, for
mu0 > sqrt(72) l5^2; at equality on the columns with mu(v) >= mu0 + delta1. The per-column statement is the one the
record's numerics check (hf_mirror5: "its zero in each column").

**D26 (2026-10-20, session decision): the eighth verifier, on the paper, and its findings seated.** One independent
read-only verifier checked the paper at 49d5898 with its own code (the reduction proved fully symbolically, Vaidya's
Ricci and Kretschmann in Eddington-Finkelstein coordinates with mu(v), the commutator (2.4), the boundary (3.1), the
constraints' principal part by another route, Proposition 6.5's induction) and re-READ the quotations against the saved
sources. No major finding; two minor and 21 notes, all seated as it proposed. (m1) The constants of the approximant
were cited to counterpart5 P1, whose scan is of a different gauge's test-field exponent: relabelled deduced (the
profiles are lam-independent, section 5.4), P1 kept for lam < l5/10. (m2) Lemma 6.4's tame clause was stated with an
inequality that does not give it: the inequality the proof gives, d_r Z + c0 ||a||^2_(H^(s''+2)) <= omega_0 Z + C
||F||^2_(H^s'') + C m_(s'') omega_s Z^(1/2), now stated; the verifier checked that Proposition 6.5's use holds and that
no frozen source term carries d_r a_i. Notes: HL's (1.3) box restored, its p. 2-3 locator, a dropped footnote marker
declared; Touati's Fourier-multiplier sentence p. 21; [CBCM10]'s page removed (unpaginated HTML); Luk and Rodnianski's
reverse statement is their Corollary 1.14, on a domain short in one null direction; the boundary spacelike only for
mu0 > sqrt(72) l5^2; nothing is claimed beyond Omega, not beyond x = 1; the g_lam margin -delta + C lam; Q's linear and
constant parts; k = 6 only; uniqueness among C^2 solutions; R1 made exact (symbolic 2-jets in normal coordinates of g3),
K for mu(v) added to R3, R6's controls run one at a time; z3-solver listed. The retitling M set (D24) is applied.

**D27 (2026-10-20, session decision): the mean-mass rate proved, by a symmetry.** N1STAR-PROOF.md section 8, Lemma 8.2
and Proposition 8.2, with `mass5.py` (M1-M4, selftest 4/4, mutants 5/5). The record's "mean mass" (hf_mirror5:
M_mean, the angular mean of the mass aspect at past null infinity after the shell) has as its counterpart in the domain
the five-dimensional Hawking mass of the spheres S_(v,r), equal to mu(v) for Vaidya (M1). After the shell only the
means remain, so the mass is mu + lam DM[m1] + O(lam^2). m1 need not vanish (ansatz5 A5 computes a nonzero order-lam
mean source in the Bondi-type gauge), but the record's two polarizations a quarter turn apart make the leading wave
odd under sigma (th -> pi/2 - th, phi1 <-> phi2) combined with the phase reflection s -> 3 pi/2 - s (M2; one
quadrature, or two in phase, is not), the two-scale operator is equivariant under that reflection with lam -> -lam
(M3), and sigma is an isometry of g0 fixing each sphere (M4); by the uniqueness of every stage, sigma^* m1 = -m1, and a
natural mass cannot see it: DM[m1] = 0. The identification with the mass aspect at past null infinity itself needs
the construction from there (D28).

**D28 (2026-10-20, session finding): the data at past null infinity, reassessed.** At D24 this item was taken as
provable by the method of Theorem E. It is not, as the method stands. On the past region {tau <= tau0} the domain is
infinite in time; the coefficients of the remainder's equation decay like r^(-3/2) ~ |tau|^(-3/2), which is integrable,
but the decomposition w = h + phi [d_th g1] that removes the 1/lam coefficient has phi accumulating along the ingoing
generators, and the crude norm bounds of section 4 turn the loop phi -> h -> s -> phi into a Gronwall growth like
exp(C |tau|^(1/4)) over the past, which no power of lam beats; without the decomposition the 1/lam coefficient gives
exp(C lam^-1 |tau|^(-1/2)), harmless only for |tau| >= lam^-2. The structure that should close it was found: along the
cone the r-derivative of phi is (1/2) P s exactly, with no accumulation, so the dangerous coupling (d_v d_th g1)(d_r
phi), of size r^(-3/2), acts on s directly; the coefficients multiplying the accumulating parts (phi, d_v phi, the
angular derivatives) decay like r^(-5/2) or faster, and the Psi transport is neutral for r^2 Psi. A weighted Theorem E
on the infinite past, with the decay in r of every coefficient and of every profile of the approximant solved from
past null infinity (the means included), would then be a separate theorem of the size of N1* itself. Not proved here;
the paper says so (section 8) and reports what it needs. M is told before any of it is attempted.

**D29 (2026-10-20, session decision): the two items attacked, as far as they go.** Late-time settling: READ at source
(alphaXiv, 2026-10-20), Ishibashi and Kodama, arXiv:hep-th/0305185v3 (Prog. Theor. Phys. 110 (2003) 901): "higher-
dimensional Schwarzschild black holes are stable with respect to all tensorial types of linear perturbations" (p. 16);
Holzegel, arXiv:0808.3246v1: "the evolution of (SU (2) x U (1))-symmetric vacuum perturbations of initial data for the
five-dimensional Schwarzschild metric finally converges in a suitable sense to a member of the Schwarzschild family"
(abstract, p. 1; Theorem 1.1, pp. 5-6), a cohomogeneity-two subclass of the T^2 class (one field B, 1+1 equations). An
earlier guess at Holzegel's identifier (0808.3605) returned an unrelated paper and was discarded. The waves here depend
on th and are outside that subclass. Deduced: after the shell the solution differs from Tangherlini of the final mass
by lam m1 + O(lam^2) with its first derivatives on Omega, so settling would follow from small-data stability of
Tangherlini in the class, once the solution is also built outside D_T; both are open. The application at 10 l5:
computed (response5.py R7), lam/L with L = K^(-1/4) the curvature length is 10 on x = 1 and 2.913 (mu = 100 l5^2),
0.921 (mu = 1000 l5^2) at the horizon: no separation of scales, so no high-frequency theorem reaches it.

**D30 (2026-10-20, session decision): the ninth verifier, on section 8 and the paper's new text, and its findings
seated.** One independent read-only verifier checked Propositions 8.1 and 8.2 and Lemma 8.2 at ee41dbb with its own
code: the background expansion by the Lie-derivative formula (mu' does not enter), the absence of an O(lam^0)
oscillation for the record's wave itself at the shifted phase with chi and a generic mean m1, the remainder's C^2
bound, the counting, M1-M3 independently, the equivariance of every stage (no choice breaks it; the record's own
Bondi-gauge terms of ansatz5 A4-A5 carry the predicted parities), the supports, and R7. No major finding; one minor and
nine notes, all seated. (Minor) Holzegel's SU(2) x U(1) class is not a subclass of ours, as D29 said: its squashing is
a dphi1 dphi2 term that the reflections exclude, so the two classes meet only in spherical symmetry (the waves are
outside it either way); corrected in the paper, and D29's sentence stands corrected by this entry. Notes: Theorem 1
item 6 holds for lam <= lam1; H2 is a sample profile, so H2b is added (`horizon5.py`, the record's wave at the shifted
phase with chi dv^2 and every T^2-invariant component of m1, symbolic in every function; 4/4, mutants 4/4); k_g carries
a positive normalising factor c(g); the naturality used is diffeomorphism covariance, M[S](phi^* g) = M[phi(S)](g); the
induced action of S on the stage unknowns (m_j, phi_j, gh_j) written out; "apparent horizon" for g_lam replaced by the
zero of the spheres' outgoing expansion; the mean mass of the spheres kept apart from the numerics' mass aspect at past
null infinity; the decay claim in the past-null-infinity assessment labelled as an assessment; the [Hol08] locator
made consistent. Two prose lines of sections 2-6 that began with "- " (and so rendered as list items) were re-flowed;
the words of sections 0-7 are unchanged.

**D31 (2026-10-20, session decision): M's three directions, and how they are read.** (1) The construction from past
null infinity is to be built and included (Theorem P, N1STAR-PROOF.md section 9). The route, from D28's structure: the
seed region {v < v_start} is exactly the seed for the solution (its past-directed causal curves cannot leave it while
the metric there is the seed, so the remainder vanishes there by uniqueness), which removes the near-hole region from
the past estimates; on the rest of the past region r and |tau| are comparable and every coefficient decays; the
loops of the decomposition close with integrable kernels because the dangerous coupling (d_v d_th g1)(d_r phi) acts on
d_r phi = (1/2) P s, which does not accumulate; and the gauge vanishes for the limit solution because D(g_app) decays at
past infinity, so no constraints need solving there. What must be computed first: that the approximant has an expansion
near past null infinity in powers of r^(-1/2) without logarithms (a transport source of order r^(-5/2) would make one;
the leading wave's own transport is what removes it). (2) "The copper study" is read, until M corrects it, as the
SOURCE work carried at copper: seed_escape.py (linear scattering of the shell off the five-dimensional hole through
Kodama and Ishibashi's barrier, computed for the copper README at several seeds) with p2_matter.py (copper's molecules
and solids under the laws of the other positions); the first bears on late-time settling. (3) The Navier-Stokes
recommendation, for the wavelength 10 l5, is read as the computer-assisted method the Alpoge-Buckmaster Boussinesq
paper cites for the regime without a small parameter (Chen and Hou, "II: Rigorous Numerics", arXiv:2305.05660, cited
there as [4]): existence near a computed solution at a fixed wavelength, from a rigorous bound on its residual and on
the linearized operator. Order of work: (1), then (2) and (3).


**D32 (2026-10-20, session decision): Theorem P built (N1STAR-PROOF.md section 9; `past5.py` P1-P7, 7/7, mutants
7/7).** The construction from past null infinity is written out as a theorem: on P = {tau <= tau0, |x| >= a, v +
kappa t^(-1/4) <= V_P} (outer boundary spacelike with a margin decaying like t^(-5/4), P1), the seed region is exactly
the seed (Lemma 9.2); the stages of the approximant are solved with nothing coming in from past null infinity, each
with an explicit leading term in r and a remainder half a power better (classes L_p, O_p; Lemma 9.7, P2-P5), and the
residual is in E_3; the remainder is controlled with rotations as commutators (P6; Sobolev gains t^(-3/2)). The D31
expectation "an expansion in r^(-1/2) without logarithms" holds in this form: every source is r^-3 times a function
plus a better remainder, so no r^(-5/2) source (the logarithm of P4) ever occurs. One obstruction found while writing:
in norms, the auxiliary Psi of section 3.3 is transported with growth r^2 and forced by r^-1 times first derivatives,
so each unit of log t costs a constant factor (the true Psi has a cancellation that norms do not see). It is met in
two ways. For the stages, by subtracting the explicit leading terms first, after which every forcing integral
converges. For the remainder, by splitting the past at t = lam^-2: before it the 1/lam coupling integrates to a
constant and no decomposition is used (Proposition 9.8); after it the decomposition runs over an interval of length
lam^-2 with weights (T/t)^beta0, at a cost lam^(-2 beta0) with beta0 independent of K (Proposition 9.9), absorbed by
taking the approximant to order N = K + 4 + ceil(4 beta0). The limit is vacuum because D(g_app) decays at past null
infinity (D_0 = 0 by transversality and trace, D_j in E_2), so the energy of D tends to zero there and Lemma 9.5 gives
D = 0: no constraints are solved on this route. Its radiation field at past null infinity is lam [W_TT] exactly, the
record's F and G at every lam. The mean mass at past null infinity: P7 computes the sphere mean of the flux density of
that field exactly. **A correction of the session's own expectation:** it was taken to be (2/9) A^2 (env^2 + lam^2
env'^2), and the first form of P7 failed; the computation gives that plus a second harmonic, (2/9) A^2 [-(1/2)(env^2 -
lam^2 env'^2) sin(2v/lam) + lam env env' cos(2v/lam)], so the integrated flux oscillates by O(lam) while the shell
passes and exceeds mu by exactly (2/9) lam^2 A^2 int env'^2 + O(lam^3) after it. Turning that into a statement about
a mass at past null infinity needs a five-dimensional mass law there and an expansion of g_lam beyond the r^-2 the
estimates give; that stays OPEN (section 9.5). Theorem P is not yet read by a verifier.

**D33 (2026-10-20, session decision): the two attacked items built on M's directions (N1STAR-PROOF.md section 10;
`settle5.py` T1-T4, 4/4, mutants 4/4; `paper/response5.py` R7 extended).** Settling, on the copper study (read as
seed_escape.py, the black-hole strand; a locator found no README for the study as a whole and no correction of D31's
reading, so the reading stands until M corrects it): the class carries no vector-type perturbation and no linearised
rotation (T1); the copper study's barrier is exactly the tensor-type potential of Cardoso, Lemos and Yoshida (T2);
evolving it, and the scalar-type potential, in time reproduces their l = 2 continued-fraction frequencies to 1% (T3);
the least-damped mode of the class, scalar-type l = 2, has e-folding time 3.905 r_h, 39-124 l5 at the study's seeds
(T4). READ: Hung, Keller and Wang (arXiv:1809.05144v1) prove tau^-2 energy decay of the master quantities in dimension
six and below, the l < 2 part pure gauge plus linearised Myers-Perry, and leave the metric components open; Schlue
(arXiv:1012.5963v1) the same rate for the scalar wave. So linear settling holds in the class at the level of the
gauge-invariant quantities; nonlinear settling stays open (its reduced problem is 2+1-dimensional, like Klainerman and
Szeftel's polarized axisymmetric case in four dimensions). The wavelength: the Navier-Stokes direction is read at
source as Alpoge and Buckmaster's programme of September 2026 (a locator and an extractor read their Boussinesq paper
and the announcement): layers of exact waves with amplitudes solving ordinary differential equations on locally linear
backgrounds; Chen and Hou's rigorous numerics is cited there and is not part of their proof. **D31's reading (3) is
corrected accordingly.** What the method would change here is the parameter, lam/r in place of lam/L: 1.00, 0.32 at the
horizon and 1.85, 1.04 on x_K = 1 (R7), small nowhere; and its wavelengths are chosen, while 10 l5 is prescribed. The
finite-wavelength question stays open, with the route stated (a certified computed solution); the paper's section 8
items carry both.

**D34 (2026-10-20, session finding): a tenth verifier on Theorem P; one major gap, repaired (N1STAR-PROOF.md Lemma
9.4b, Proposition 9.9; `past5.py` P8).** The verifier read section 9 whole and ran past5.py (7/7, mutants 7/7, P7's
integration by parts re-derived by hand). It found the far region, the decay counting, the gauge argument, the
radiation field, uniqueness and section 9.5 to hold, and one MAJOR gap: in Proposition 9.9 the forcing of Psi's
transport omitted the commutator [box~, P] s, which the mollifier's shift makes of size ||d s|| with no decay in t;
with it the near-region loop grows like exp(c t^(1/4)), which no power of lam absorbs. Its proposed repair was checked
before use: P is the convolution followed by a radial shift, which in (tau, v, xhat) is v -> psi_tau(v) with psi
depending on tau only through Delta(tau), so L0 (= d_tau at fixed v) commutes with it up to O(lam h'); and with box~ =
-(1 + mu/r^2) L0^2 - 2 d_r L0 + (3/r) d_r + r^-2 Deltaring, the commutator is exactly -L0(2 (psi' - 1) C d_v g) plus
terms with factors 1/r, mu/r^2, lam h' (P8, exact for every psi independent of tau; its control, psi depending on tau,
fails). So Psi' := Psi - (1/2) X_s, X_s = 4 lam sigma_v C(d_r M s), is transported with a decaying forcing, and
Proposition 9.9 is rewritten for it. The minor findings are seated: the transports are commuted with lam d_tau, lam
d_r and Omega, which commute with L0 exactly, so their growth rates do not rise with the order (F2); beta0 depends on
the bounds of g0, g1, g2 only, not on N (F3); the smoothness of the limit by tame linear estimates at fixed lam (F4);
the hierarchy of constants in (9.7) and the convergence of the stage solutions with O(1) data for f (F5); Data(w) <= C
lam^-1 N_P (F6); Lemma 9.5's bound on P+ (F7); four wording points (F8). The repair has not been read by a verifier:
Theorem P is not claimed as PROVED, and the supplement's status lines say so. The earlier text was merged with PR #59
as "not yet verified"; nothing there claimed it proved.

**D35 (2026-10-20, session finding): an eleventh verifier on the repair; Theorem P PROVED.** The verifier read section
9 after D34, ran past5.py (8/8, mutants 8/8) and rebuilt the commutator independently with mu = mu(v) and psi =
psi(tau, v). Verdict: the repair closes the gap and Theorem P holds as stated; every step of D34's list and F2-F8 was
re-derived and found sound. Two minor findings and four notes, all seated: the coefficient of the angular derivatives
r^-1 Omega phi is E_(5/2), not E_(3/2), and D1 is taken as (d_tau phi, d_r phi, r^-1 Omega phi) with c0 = 0, 0, 1 so
that its top order closes; Lemma 9.4b's remainder with mu(v) and psi(tau, v) has exactly the four further terms the
verifier listed (mu(psi) - mu(v) and three with psi_t or psi_tt), each with a decaying factor, now stated and checked
in P8 (an exact polynomial identity on e^(a tau + b v), with two controls: the psi_t terms left out, the mu term left
out); the Z commute with the shift only up to bounded operators, which suffices; the data terms at tau_T are added to
every line of (9.9); the rate of p in Theorem A_P's convergence step is corrected; B and C are fixed so that the
constants close. These seated edits are the only text of section 9 no verifier has read after the edit.

**D36 (2026-10-20, M's direction): routes for the three open items.** M: "Still open, and stated as open in the paper: -
do some deep research on the web and suggest a method for closing these." The literature was read (alphaXiv; a search
for nonlinear stability of five-dimensional Tangherlini in a class depending on more than (t, r) found none) and one
method is proposed per item in ROUTES-OPEN.md; nothing is claimed proved. Mass at past null infinity: the five-
dimensional Bondi mass law is published (Tanabe, Tanahashi and Shiromizu, arXiv:0909.0426, (28)); with both reflections
it is the class's ansatz with C = 2P, and time-reversed its density is exactly P7's, (4/3)(p1_v^2 + p1_v p2_v + p2_v^2)
(routes5.py Q2; Q1: five-dimensional Vaidya has R_vv = 3 mu'/(2 r^3)); what remains is g_lam's expansion at I^- to their
order, by Theorem P's transport iterated, the r^-2 term of C vanishing because it is constant in v and zero on the seed.
Ten l5: a posteriori existence, Theorem E with certified numbers (Chernyshenko-Constantin-Robinson-Titi; Morosi-
Pizzocchero's control inequality; Reiterer-Trubowitz in general relativity), on the 2+1 system, decided first by the
growth factor exp int K over D_T. Settling: Hintz's generalized wave map gauge route (arXiv:2606.28253, full subextremal
Kerr, 2026) in the class, whose reflections and T^2 leave the mass as the only final parameter; first milestone, linear
stability in wave gauge within the class.

**D37 (2026-10-20, M's direction, "all 3 please, proceed with them in order"): the mass at past null infinity, Theorem
M.** Step 0 first: the numerical solver's mean-mass offset after the shell fits c lam^2 with c = 0.4568 and 0.4569 at
lam = 0.0125 (mu0 = 100 and 1000 l5^2), against the law's (2/9) int env'^2 = 5 pi^2/108 = 0.45693 for its sin^4 envelope
on [1/2, 7/2]: within 0.05 %, converging as O(lam) from 0.4589 and 0.4577 at lam = 0.05, 0.025 (bondi5.py B4,
response5.py R8). This compares the law with the solver's own integration of it (its mass aspect's rate is fixed by E_vv
= 0 at past null infinity), not with g_lam. Then the theorem, section 11: at fixed lam the far region of Theorem P is a
neighbourhood of past null infinity on which g_lam - g0 has an asymptotic expansion in r^(-1/2) to any order (Lemma 11.2
gains half an order per step by Theorem P's own energy estimate, and the remainders gain a full order under ell because
the wave equation is a transport along the outgoing generators for them, which reach the seed in a bounded parameter
length); Bondi coordinates are built on g_lam as in He and Lindblad's construction at future null infinity (the eikonal
transport has an r^-2 source because the first-order wave is transverse to ell), with the leading angular coefficient
untouched (Proposition 11.2, bondi5.py B2); and the five-dimensional Bondi hierarchy (Tanabe, Tanahashi and Shiromizu
2009, (28)) is recomputed in the class with every coefficient general as truncated Laurent series in s = r^(-1/2) (B1,
about a minute): b3 = b4 = b5 = 0, b6 = -(1/4)(p^2 + pq + q^2), u3 = u4 = 0, u5 and w3 = -(2/3) div u5, d_v a_i = 0, and
R_vv at s^6 the law d_v M = (4/3)(p_v^2 + p_v q_v + q_v^2) + (2/3) div(d_v u6), pointwise once a_i = 0, which the seed
gives. The Hawking mass of the Bondi spheres tends to the mean of M (B3). So the mean mass at past null infinity is
mu(v) + O(lam) in the shell and mu + (2/9) lam^2 A^2 int env'^2 + O(lam^3) after it, for g_lam: the paper's section 8
item closed; Theorem 3 in the paper. One correction of the session's own guess in passing: the areal radius's s^4
coefficient carries the divergence of the angular shift, rho_4 = tr_S G_4/6 - (1/3) div ϑ_4, as B2 found when the
guessed formula failed. Not claimed: uniformity in lam of the expansion beyond its leading term, which the law does not
need. Not yet read by a verifier.

**D38 (2026-10-20, M's direction, the second of the three): the go/no-go at 10 l5, measured.** ROUTES-OPEN.md section 2
asks first for the growth factor exp int K dv of the computed solution over D_T, non-rigorously. growth5.py runs the
solver of hf_mirror5.py on hf_core5's own domain (seed 1, A = 1, the record's envelope, the slice continued to the core
boundary x_K = 1: y = 1.361 for mu0 = 100 l5^2 and 1.815 for 1000 l5^2) at lam = 10 l5, that is lam/sqrt(mu0) = 1.000
and 0.3162, recording at every step two measures of K (the radiation field's own rate, and the sup of the first
derivatives of the five dimensionless departures from the seed in the Bondi chart, fifteen maxima kept apart), the
first v at which the scheme's premise fails (a second zero of the round spheres' outgoing expansion in some column, or
the core boundary untrapped), and, from a second run with A -> A(1 + 10^-3) on the same fixed step, the
finite-difference amplification of the data's difference into the slices. At mu0 = 100 l5^2 the premise fails at
v = 1.4516 (Ny = 20) and 1.4508 (Ny = 28), before the shell's peak at v = 2: the expansion acquires a second zero and
within 0.2 the boundary's W changes sign (its value +19 at v = 1.75 in a first trial), the mean mass aspect runs away
and the slice solve fails at v = 1.69-1.75. The time is the solution's in the scheme's gauge, not the grid's. The wave's
metric amplitude at the core boundary there is lam A r^-3/2 = 2.5, beyond the high-frequency regime hf_mirror5 X9
recorded as ending near 1.2; up to the break, int K_v dv = 0.52 (exp 1.7) and the amplification is 1.00. The record's
own regime, lam = 0.1 at mu0 = 100 l5^2, serves as control: complete, int K_v dv = 1.93 (exp 6.9), amplification 1.71.
The mu0 = 1000 l5^2 pair, and what the whole measurement decides, are D41.

**D39 (2026-10-20, M's direction, the third of the three): the linear milestone in the class.** ROUTES-OPEN.md section
3's first milestone L1 asks for linear stability of five-dimensional Tangherlini within the class with decay of every
metric component. What [HKW18] leave to "a suitable choice of linearized gauge" is, in the class, already written in
Kodama and Ishibashi's master-equation paper (hep-th/0305147, READ): for every scalar mode l >= 2 the gauge f_a = 0 =
H_T exists, and in it the metric components are their (3.14), the master field and its derivatives to order two with
coefficients bounded on r >= r_h uniformly in l; the tensor type is its own master field; the class has no vector type
and no l = 1; the l = 0 part is the mass shift. So every metric component of a perturbation in the class settles, in
that Regge-Wheeler-type gauge, to a change of mass at [HKW18]'s rate tau^-2 in energy with the loss of two derivatives
(Proposition 10.1, deduced from READ, section 10.3). Not L1: the gauge is not the wave-map gauge of the nonlinear
problem, and the pure-gauge passage between them (the zero-frequency analysis) is open, as it was in four dimensions.
The computed companion ROUTES-OPEN.md asked for: settle5.py T5, no growing mode for l = 2..10 in either type (the field
on a fixed region falls by five to fourteen orders within 150 r_h of the launch; the sign-reversed potential grows), and
T6, the late-time tail of the l = 2 master fields, 7.05 (tensor; 7.03 at half the step) and 7.06 (scalar) on [550, 700]
r_h measured from the launch and approaching 7 from above, 11.5 at l = 4: Cardoso, Yoshida, Dias and Lemos's t^-(2l+D-2)
for odd D (hep-th/0307122, READ; their D = 5 numerics 7.1 and 11.4), the flat five-dimensional Green's function's tail
and not the hole's. A first measurement with the time origin at the run's own t = 0 read 2.65 from the same points; the
control keeps that mistake visible. Not yet read by a verifier.

**D40 (2026-10-20): the twelfth verifier, on Theorem M.** One independent verifier read section 11, bondi5.py (ran
`--verbose`, 4/4, and `--mutants`, 5/5) and the paper's Theorem 3: "holds with the gaps listed", no major finding, five
minor, four notes, every attack it tried recorded as held. The five, each repaired in place: (1) Lemma 11.2 claimed the
ell-gain at every order m from a hypothesis without ell-derivatives of the source; the lemma now carries (H_m), and at
J = 3 the gains are proved by induction on m, the case m = 1 needing nothing and supplying ell u_1 in E_3 for the next.
(2) "u_1 in E_2 with all its derivatives" rested on Theorem P, which controls four; Lemma 11.0 gives every order at
fixed lam by commuting on the far region, the data on the null hypersurface {v = v_start} being zero. (3) The
contraction building v_B lost a derivative through eps(dů); v_B is now built by characteristics, the null geodesics of
g_lam asymptotic to the background's generators (an ODE contraction, no loss), and (11.9) is then an identity it
satisfies, from which the expansion follows as before. (4) B1's ansatz started b and U at s^3, so b_2 = 0, which the
chart does not give (e^{-2b} = 1 - (d_v C4/2) s^2 + ...), was assumed; B1 now runs the orders below the waves' first:
R_ss at s^-1, s^0 read -12 b_1, -24 b_2 and R_sth at s^-2, s^-1 read -(7/4) u_1, 3 b_1 u_1 - 3 u_2, so they vanish by
the equations (Proposition 11.3(0)). (5) G_k's coefficient is 2/(k - 3), not 2/(k - 4). The notes: the J = 3 source's
sign and argument; the areal condition's coefficient is 6 rho_k (the d_r r_B factors cancel), so it is algebraic as
stated; R_rr's orders are s^7..s^10; "derivatives in s raise the order" is false as written and is replaced by what
holds (d_r raises the s-order by two, v- and th-derivatives preserve it, and the s^6 equation's content is read off).
The ninth, that the solver's M = -w_y|_{y=0} was not independently checked, is covered by 11.4's own caveat. The
repairs are not themselves verified.

**D41 (2026-10-20): the go/no-go at 10 l5, the second seed and the verdict.** At mu0 = 1000 l5^2 (lam/r_h = 0.316, the
core boundary at r = 0.30 r_h where the wave's metric amplitude is 1.9) the record's scheme fails its premise as it did
at 100 l5^2: the round spheres' expansion acquires a second zero at v = 1.5825 (Ny = 24; the Ny = 28 and 20 runs to v =
1.75 agree, D43), W at the core boundary turns positive at v = 1.680 and the slice solve fails at v = 1.704, before the
shell's peak. To the break, int K_v dv = 0.75 (exp 2.1), int K_all dv = 12.3 (exp 2e5, d_r of W - W_V at the deep
boundary), amplification 1.00; the K referenced to Vaidya at the Isaacson mean mass rather than to the seed, after a
first run let the shell's own mass gradient dominate (int K_all dv = 12.6 at lam = 0.1, 8.8 of it the mass term's d_r;
the control now reads 8.77 with d_v of W's oscillating part the largest). The verdict (section 10.2): no approximant on
D_T at 10 l5 comes from the record's own scheme at either seed -- the core boundary x_K = 1 is not trapped throughout
the passage there, so the record's premise that the exterior is fixed by its own data fails, and step 2 of the route
must be re-posed with an inner boundary that stays outflow; and the sup-norm Groenwall factor is no measure of the
growth (1e3 to 1e5 against an amplification of 1.0 to 1.7), so the certified argument would need the propagator's norm.
growth5.py pins the seven runs (G1-G4) and reads them back; the run files are intermediate and `--merge` keeps one
trimmed data file. Not read by a verifier.

**D42 (2026-10-20, M: "evaluate what is still open, execute more deep research ... then work them to completion"):
the harmonic gauge in the class.** The literature was read again at source: Hung's four-dimensional even part in the
harmonic gauge (arXiv:1909.06733) is the template for L1 -- the Lichnerowicz equation under the gauge, the gauge
vector to the Regge-Wheeler gauge solving the tensorial wave equation with the Zerilli source, the l = 0 sector's
stationary one-form W* and linearly growing gauge-fixed mass change K*, and tau^(-2+) decay for the rest -- and nothing
of it exists in five dimensions. wavegauge5.py computes every explicit object of that structure on five-dimensional
Tangherlini in the class (section 10.4, Proposition 10.2): the Lichnerowicz identity and Gamma[pi_X] = box X (W1); the
tensor type is in harmonic gauge already (W5); the scalar gauge vector's three 1+1 equations per mode with the master
field as source (W4, l = 2 and 4); W* = dt/r^2 + sqrt(mu) dr/(r^3 f), regular at the horizon (W2); and K* = K +
pi_{W**} with A and B explicit, harmonic, linear in t (W3). What L1 still needs is the decay estimate for that system,
Hung's sections 5-8 in five dimensions; it is named and not attempted. Not read by a verifier.


**D43 (2026-10-20): the go/no-go at 10 l5 finished -- the grids, the deeper excisions, the criterion, the re-posing.**
The Ny = 28 and 20 runs at mu0 = 1000 l5^2 agree with Ny = 24 (break 1.5829, 1.5825, 1.5825; D41's forward reference
points here). The breakdown is read by a persistence criterion -- a second zero of the expansion holding over 0.01 in v,
or W >= 0 at the boundary (growth5.breakdown): a single-step excursion of the root count at v = 1.4516 had set the first
seed's figure, and the persistent figure is 1.500 (Ny = 20) and 1.496 (Ny = 28); both are stated in section 10.2. Deeper
excisions do not help and fail earlier: y = 1.6 (r = 0.39 r_h) at the first seed breaks at 1.410, W >= 0 at 1.455, the
solve fails at 1.556; y = 2.0 (r = 0.25 r_h) at 1.353, 1.362, 1.370; y = 2.2 (r = 0.21 r_h, Ny = 16) at the second seed
at 1.524, 1.558, 1.559 against 1.583, 1.680, 1.69 (G5, three runs pinned). The untrapping is of the seed's interior in
the scheme's gauge, from the inside outward, and the exterior of the event horizon is unaffected; D41's causal sentence
("the exterior is no longer fixed by its data") is narrowed in 10.2 to the region between x_K = 1 and the apparent
horizon. The question is re-posed as the characteristic initial value problem in double-null gauge, where Luk's theorem
gives local existence without smallness ([Wu26] Theorem 2.1, READ) and [Wu26]'s Theorem 2.2 is the a posteriori
structure; not built. K_all is now referenced to Vaidya at the Isaacson mean mass and U is carried as r U (the first
K_all was dominated by the seed-referenced mass gradient and mixed dimensions), and the amplification run is paired with
its own base (growth5.partner). One rule slip is recorded: a process was once addressed by `pkill -f` with a pattern
instead of by its PID; it killed the issuing shell and the selftest it named, nothing else, and was not repeated. Read
in part by the thirteenth verifier (D44). [D45 withdraws this entry's causal reading: the stored samples do not give the
direction of the untrapping, the zero of W moves inward, and nothing is said of the event horizon.]

**D44 (2026-10-20): the thirteenth verifier -- D38-D41, the repairs of D40, sections 10.2 and 10.3.** Two major findings.
(1) Lemma 11.0 ran Lemma 9.5's identity on the region between {v = v_start} and Sigma_tau, which is unbounded toward past
null infinity, where the flux of d^gamma u_1 is known to vanish only at the orders Theorem P controls (k = 6): the
twelfth verifier's gap was moved, not closed. Repaired by running the identity for each approximating solution g_n of
Proposition 9.8 on P cap {tau_n <= tau' <= tau}, the region of (9.8)'s own identity, where the data on Sigma_tau_n are
the approximant's residual, explicit, with constants independent of n, and passing the bounds to the limit by
Arzela-Ascoli; the sup-against-L^2 bookkeeping is written (floor((N + 2)/2) <= max(4, N - 3)). The verifier proposed a
finite derivative budget instead; k = 6 is fixed in Theorem P, so that route would re-run section 9 at a higher k, and
the one taken keeps every order. (2) Section 10.2's break time at the first seed, 1.4516 / 1.4508, was a single step of
the root count on both grids, and the amplification 1.00 was sampled before the field had grown: the grid agreement
supported a transient, not a persistent second zero -- as D43's criterion had found the same day. Nine minor findings and
notes, all seated: Proposition 11.2(i)'s nullity argument used the transverse Jacobi field d_{v0} gamma with the false
g0(ell, d_v) = 0 (now gamma' and d_{xhat0} gamma only, with the limits in E_1) and called -(2/r) xi' a Lipschitz
perturbation (it is the unperturbed angular operator); Proposition 11.2(iv) had e^{-2b} = 1 + 2 d_v ů (the factor is 1,
as B2 computes); "an order" is one power of r, two of s, in Theorem M(a) and Proposition 11.3's hypothesis; Proposition
10.1(iii)-(iv) hid a factor H ~ l^2 in Phi~ (the two derivatives lost are orbit-space for F_ab and angular for F) and
left the l = 0 gauge unfixed (h_0 = c K, now stated); the even-l claim for the tensor type is not needed and no longer
made; T5's region r* in [-20, 50] was covered by the computed slice only to tau = 175 at T = 120 (now T = 170, covered to
275, the checks restricted to the covered range, the figures unchanged to two digits), and its verdict is a finite-time
observation (rates above 0.08/r_h excluded); T6's "approaching 7 from above" is origin-dependent at that level (the
origin shifted by the launch radius gives 6.89 and 7.23; that the pair brackets 7 is now checked); 10.2's "ceases to be
trapped" and "ceases to be outflow" are given one meaning each, and the amplification is called the lower bound it is.
Open: the literature identifications ([KI03] (3.13)-(3.14), [HKW18] (169)-(186), [CYDL03] (14)) could not be re-fetched
by the verifier (403) and stand as READ by this session. Attacks that held: Lemma 11.2's coefficient 2/(k - 3) and G_4 =
2 int S_3, the induction at J = 3, Proposition 11.3(0) with its controls, the ODE classes of 11.2(i), 10.3's regularity
at the horizon and the absence of l = 1, settle5 6/6 with mutants 6/6, growth5's fields against hf_mirror5's form and
every figure of 10.2 from the pinned data, no line over 121 characters, no model identifier. The repairs of this entry,
D42's section 10.4 and D43's deeper excisions have not been read by a verifier.

**D45 (2026-10-20): the fourteenth verifier -- D42-D44, the repairs of D44, sections 10.2-10.4.** Verdict: the
mathematics repaired in D44 holds. Lemma 11.0's new argument closes the thirteenth verifier's gap rather than moving it
(the region is bounded, its boundaries Sigma_tau_n, Sigma_tau, B and {r = a} where u vanishes; the data on Sigma_tau_n
are the explicit E_2 part of g_app - g0 - r^(-3/2) G_3 at C t_n^(-1/2) and the residual's derivatives at C t_n^(-3/2);
the bookkeeping inequality is the right one; the pointwise bound is uniform in n and in the point, compactness
extracting convergence only); Proposition 11.2(i)'s classes, Lipschitz constants and nullity argument are right (the
verifier recomputed Gamma[g0]^v_{rb} = 0, Gamma^th_{r th} = 1/r, Gamma^v_{th th} = -r, Gamma^r_{rv} = -mu/r^3 and the
three E_1 limits); e^{-2b} = 1 + d_v ů; every instrument passes and reproduces every pinned figure; the verifier's own
sympy agrees with wavegauge5 (and a second sample tensor at five random rational points gives residual 1e-133 against 69
for the sign mutant); the 21 md5 rows of Appendix D match HEAD. One major finding, in section 10.2's reading of the
data: at v = 1.5 (mu0 = 100 l5^2) the samples carry r_lo = r_hi = nan with nz = 2, which by hf_mirror5.horizon means a
column with no zero of the expansion -- no round sphere trapped there -- so the untrapped region was not enclosed by a
trapped one at the quoted time; in the strongest column W > 0 only for r >= 0.74 r_h (W < 0 on 0.54-0.66), so "r <= 0.9
r_h have W > 0" was false below 0.72; the zero of W moves inward with v (0.86-1.02 at v = 1.0 and 1.25, 0.66-0.74 at
1.5, the boundary at 1.516), the opposite of "from the inside outward"; the direction of the second zero cannot be read
from the data at all (q stored as its maximum, the zeros only when every column has one); and "the exterior of the event
horizon is unaffected" is the conclusion the same paragraph says it cannot make. Repaired: section 10.2, D43 (a
bracketed note), ROUTES item 2 and the paper's section 8 now state what the samples show and withdraw the direction, the
inner MOTS and the event-horizon sentence; `--run` records every zero per column from this commit (growth5.zeros_of),
the pinned runs predating it, the direction OPEN. Minor, all seated: "stays from 1.500" was false -- nz = 2 holds on
[1.500, 1.540] (Ny = 20) and [1.496, 1.545] (Ny = 28), lapses on [1.548, 1.661] and [1.549, 1.717], returns from 1.669
and 1.721; the break time stands (the W clause at 1.516) and the text says "holds and lapses"; a grid-independent nz = 2
on [1.4758, 1.4839] (0.008 in v) is excluded by the hold 0.01 by 0.002, so the hold's sensitivity is stated (1.500 for a
hold in (0.0082, 0.040], 1.476 below); D38, not D41, quotes 1.45; Proposition 10.1(iii) split the derivative count
wrongly -- F_ab carries the factor m through its trace -2 r F, the bracket of (10.1) being traceless (the count is
unchanged); Proposition 10.2(iv)'s "can settle only to c1 K* + c2 pi_{W*}" was Hung's Theorems 1.3-1.4 transposed
without their decay estimate, now conditional; the paper's Appendix D and the README misstated which programs import
from the tree (growth5 the solver, past5 lead5); doubled list markers from the last round's rewrap in the README, the
paper and ROUTES; "section 9.3" for 9.4 and a circular clause in Lemma 11.1's proof. Open: the Hung attributions (arXiv
403 for the verifier), as before. Attacks that held: the 12 pinned runs and every figure of 10.2 to the digits quoted;
settle5 6/6 and 6/6 with the coverage arithmetic and the origin shifts (6.89, 7.23) rerun; the T5 control grows 1.5e7 ->
3e144 on the covered window; wavegauge5 5/5 and 5/5 with W2-W5 recomputed independently (W5: Gamma[h_T]_j = 2H (div T)_j
identically) and W4's coefficients theta-free at seven rational angles.

**D46 (2026-10-20, M: "deep research this and propose a method to approach solving this and closing the nonlinear
settlings"): the decay of the gauge-vector system, and the nonlinear settling -- the route.** The literature READ at
source: [Hun19]'s architecture (seven components with a semi-positive potential matrix, Proposition 4.2; the gauge
vector to the Regge-Wheeler gauge by invertible angular operators; the triangular system (4.21)-(4.25) of scalar wave
equations with potentials, each treated by the vector field method under l_0(l_0 + 1)/r^2 + V >= 0, Appendix A; the l =
0 ODE and red-shift argument, section 8; W* and K*, (8.1), (8.39)); [HKW18]'s tools stated for a general
Regge-Wheeler-type potential (Definition 8, Lemma 13, Proposition 15, Theorems 16 and 18) and the reason the decay stops
at six dimensions (the near-horizon Morawetz positivity, section 9.3.2); [Sch13]'s scalar decay on Schwarzschild of
spatial dimension n >= 3 (Theorems 1-2, the photon sphere, the p-hierarchy on r^((n-1)/2) phi); [KI03b]'s Maxwell master
equation (5.20); [Hin26]'s nonlinear programme -- the generalized wave map gauge with finite-dimensional gauge sources,
the strong constraint damping (1.43) of [Hin26a], the two 1-form black boxes (section 1.4.1), the zero-energy nullspace
of Kerr with its second-order pole from translations and boosts -- and [Hin26c]'s tame estimates, in 3 + 1 for
concreteness (Remark 5.6) with the general-dimension indicial gap (0, n - 2) (Proposition 9.40); the 2+1 reductions
[KS17], [Hun15], [HL17]. One computed input, W6: the gauge-vector system of W4 is triangular -- seven exact identities
at l = 2 and 4: div(box X) = box_l(div X); (box X)_t = box_l X_t + (2 mu/r^3) F_tr; (box X)_r = d_r S - f^-1 d_t F_tr -
(k^2/r^2) Q_r; r (box X)_L = box_l(r X_L) - (2 k f/r) Q_r; the Maxwell t-equation; the equation of F_tr; and box_l(r
F_tr) + (4 mu/r^4) r F_tr = r d(box X)_tr + 2(d_t S - (box X)_t) -- so every rung is a scalar wave equation on
Tangherlini with a potential obeying Hung's (A.3) (zero for S, X_t and r X_L; -4 mu/r^4 for r F_tr, positive against
k^2/r^2 for r^2 >= 4 mu/k^2), X_r algebraic. What the class removes: translations and boosts (no vector is fixed by both
rotations), the vector type and rotations, l = 1; the final state is the mass alone. ROUTES-OPEN.md section 4 proposes
route A -- L1 by Hung's architecture in five dimensions, six steps, the four things that must be done rather than quoted
named (the Morawetz currents for the rungs' potentials, the r^(3/2) weights in the r^p identity, Hung's Proposition 4.2
in the class, the l = 0 argument) -- and route B, the nonlinear settling in a generalized wave map gauge after [Hin26]:
mode stability of the ungauged equation already in hand in every dimension ([IK03], [HKW18]), the 1-form operators with
W* removed perturbatively, a five-dimensional constraint damping as the first genuinely new object, a first-order pole
at zero energy where Kerr has a second-order one (deduced from the structure, not proved), [Hin26c] in 4 + 1; the 2+1
reduction (2+1 gravity with a flat-target wave map, the polarized U(1) analogue with two scalars) recorded and not
recommended; and the first step, W7: Hung's Proposition 4.2 in the class. The ROUTES reference line pointed [Sch10] at
the paper, which has no such entry; [Sch13] replaces it. wavegauge5.py W6 and its control (the sign of 2 mu/r^3 and 4
mu/r^4) pass. Nothing in the route is proved. Not read by a verifier.

**D46, addendum (2026-10-20, after the push of 995929a).** The run under `--l4` finished: all seven identities at
l = 4 pass and the control fails, 72 minutes for l = 2 and 4 with the control. The three places that said the l = 4
run had confirmed the first four and the equation of F_tr (the wavegauge5.py docstring, Prop 10.2(vi), ROUTES-OPEN.md
section 4.1) now state the full result. Not read by a verifier.

**D47 (2026-10-21, M: "The open item: - begin with Route A, if it fails, then we will pursue route B. AND Unread. The D45
repairs, the paper's Theorem 3 text, and the D46 route have not been read by a verifier. - send these to the verifier
please"): the fifteenth verifier, then route A's first step, W7, with its four-dimensional control hung4.py.**

*The fifteenth verifier* (the repairs of D45, the paper's Theorem 3 against section 11, the route of D46; sent before
the route work began, one at a time). Verdict: no blocking finding; the D45 repairs hold with repairs, Theorem 3 holds
(labels and numbers as section 11 earns them, Lemma 11.0 sound as repaired), the route holds as a route. Nine repairs,
seated: (1) a bullet of the paper's section 8 merged into the one before it by a doubled marker mid-line, which D45's
pass over line starts missed; (2) growth5.py's G1 docstring still said the second zero "stays from 1.500" where the
data lapse and return; (3) section 10.2 said W < 0 persists out to 1.61 r_h in the other columns -- the stored samples
put the outermost W < 0 at 1.26 r_h (Ny = 20; 1.22 at Ny = 28), the next grid point 1.61 has W > 0 in every sample;
repaired to the samples, and escalated here as a figure in repaired text the record did not support; (9) bondi5.py's
`--verbose` ran B1 and B2 alone, with no controls, no B3-B4 and no summary, and exited 0 -- a defect of the
instrument, not of the mathematics; it is a modifier of `--selftest` now, listing B1's and B2's sub-checks; (14) ROUTES
4.4(3) called the first-order pole at zero energy deduced: in the harmonic gauge of W1-W6 the t-linear zero-energy
state K* = t pi_{W*} + (stationary) with Gamma[K*] = 0 (W3) is present, the second-order structure, and the first-order
claim rests on 4.4(2)'s unconstructed five-dimensional constraint damping removing W*, not on the symmetry -- OPEN now;
and 4.2(ii) credited Kerr's second-order pole to translations and boosts where 4.1 (READ) gives it to the generalized
boosts; (15) 4.3(2), 4.3(6)(a) and 4.5 carried pre-W6 wording (potentials V_r and V_L, a wave equation for X_r, "finish
W6" as the first step) -- rewritten; (16) the paper's "reduces to known tools rung by rung" against the route's four
things to be done rather than quoted -- aligned; (17) one paper under two labels, [Sch10] in section 10.1 and [Sch13] in
the route -- [Sch13] everywhere; (18) the gauges of Johnson's paper and of Hung, Keller and Wang's were swapped between
the route and section 10.3 -- Hung, Keller and Wang in the Regge-Wheeler gauge, Johnson in the generalized wave gauge,
from the titles, the papers not re-fetched. Seven notes: zeros_of verified (the map r = (y_ex(1 - t0)/2)^-2, the roots
refined in the same column, the two new pins); growth5.py's import of hf_core5.y_core omitted by the README and the
paper (added); the paper's Appendix C listed verifiers to the thirteenth (extended); Lemma 11.0's induction written for
d^gamma only while its statement has Omega^beta (a clause added: Lemma 9.3(a) with the rotation energies, the commutator
absorbed as in 9.8(iii)); Lemma 11.1's mutual induction with 11.0 acceptable; Proposition 10.2 skipped (v) (renumbered);
response5.py line 431 at 126 characters (wrapped) and W6's docstring saying "exact" for three points to forty digits
(reworded). The verifier re-derived W6's identities 1, 2, 6 and 7 with its own Christoffels (to 1e-172) and the master
equation of r^3 P against [KI03b] (5.20) by hand, and ran every fast selftest. Not checkable by it: Hung's (A.3) sign
convention, the two papers' gauges, [Hin26]'s pole attributions (the proxy's 403).

*Route A, first step (M: route A first; route B if it fails).* 4.5 named W7, Hung's Proposition 4.2 in the class.
READ at source (alphaXiv, [Hun19] pp. 17-25, 70-71, 75-79): Proposition 4.2 writes the harmonic-gauge system as
box H = A H + B H + U H in seven components, U along nabla_L in rows 6 and 7 only, A_main + B_main self-adjoint with
r^2 (A_main + B_main + O) semi-positive per mode (Lemma 4.3, eigenvalues (l+a)(l+a+1), a = -2, -1, 0, 0, 0, 1, 2),
and the red-shift needing the nabla_L' coefficient non-negative in the regular variables H6', H7' (p. 23: 4M/r^2 and
2M/r^2); and Appendix C: each row is a combination of the Lichnerowicz components and of the harmonic gauge
condition. The instrument built for it -- the Lichnerowicz operator and the gauge one-form on the class's mode ansatz
with the harmonic kept symbolic, its equation S'' = -2 cot 2th S' - k^2 S applied, the angle evaluated exactly at two
Pythagorean points, every coefficient a rational function cancelled -- found, in this order: (i) in the orthonormal
frame the Lichnerowicz system alone is box v = T d_t v + M v with no d_r term, M symmetric, T the chain coupling
(h_00, h_01) and (h_01, h_11) at sqrt2 f'/f and (h_0th, h_1th) at f'/f; in the null frame this is -f' times the boost
weight as the nabla_L' coefficient of each component (-2f' on h(L, L), -f' on h(L, d_th), 0 on h(L, L') and the
angular part, +f' on h(L', d_th), +2f' on h(L', L')), the Teukolsky-type structure -- so the red-shift coefficient is
negative on the positive weights, and Hung's zero rows 1-5 could not be the Lichnerowicz operator alone; a
four-dimensional run in his components showed the same first-order terms in rows 1 and 6 (a first version of that run
used 2/r for the scalar operator's radial coefficient, 2/r - 2M/r^2, and showed spurious terms in rows 2, 3 and 5;
corrected before anything was recorded); (ii) Appendix C, fetched for the discrepancy, resolves it: the gauge
condition is admixed, and that is what removes them; hung4.py recomputes his seven rows from the Schwarzschild metric
and reproduces the printed A, B and U -- rows 1-5 as printed, row 7 as printed with (HG3) for the printed "(ME3)" of
its combination, row 6 as printed once its combination is read as f (ME3) + (M/r^3)(ME6) + (4M(r - 2M)/r^3)(HG2) for
the printed (ME2), M/r^2, 4M(r - 2M)/r^2 (the printed one leaves second-order terms), "nabla_L . r" read as r nabla_L
in row 7 and as nabla_L(r .) in row 6; two misprints, no finding about the theorem; 2/2, mutants 3/3; (iii) W7 in five
dimensions, wavegauge5.py: in his components with (1 - f)/2 = mu/(2 r^2) where his M/r is the same (1 - f)/2, the
admixtures 2 f f' Gamma_r (rows 1, 6) and k f' Gamma_th/r (rows 4, 7), box_l H = A H + U H with U = (2f'/f) nabla_L
(H6 - H1) and (f'/f) nabla_L (H7 - H4) only; r^2 A_main at k^2 = l(l+2) with the eigenvalues (l+a)(l+a+2), a = -2, -1,
0, 0, 0, 1, 2, the characteristic polynomial factored over Q[l]; A - A_main/r^2 = O(mu/r^4); in the regular variables
every coefficient regular at the horizon, rows 1-5 without first-order terms, rows 6', 7' with 2f' nabla_L' and
f' nabla_L', f' = 2 mu/r^3 > 0, and no nabla_L; l = 0 with eigenvalues 0, 0, 3, 8. Seated as Proposition 10.2(vi),
ROUTES 4.6 and 4.5 (the order now: Hung's Proposition 4.1 in five dimensions on this structure, an estimate; the rungs;
the growing source and l = 0; then route B's constraint damping), the README and the paper. Labels: computed; the
estimate OPEN; nothing proved. Two slips in the check's code, caught by its own failing against the standalone
computation before anything was committed: a positive assumption on the eigenvalue symbol defeats sympy's polynomial
comparison, and the row-6' zeroth-order correction needed its 1/f. Not read by a verifier: W7, hung4.py, the repairs.


**D48 (2026-10-21, M: "Continue with Route A"): Hung's Proposition 4.1 in five dimensions, deduced as Proposition 10.3 on
W7's structure from the identities of W8.**

*What was read.* [Hun19] at source (alphaXiv): section 2 (the ingoing chart (2.1), the wave operator (2.2), the red-shift
cut-off and vector field (2.6)-(2.7), the vector-field sets (2.8), the red-shift identity (2.13), the divergence theorem
(2.14), the norms (2.15)-(2.22)); Lemma 3.2 and Corollaries 3.3-3.5 (the Hardy inequalities); section 4.1 in full
(Proposition 4.1 and (4.1), the components, Proposition 4.2 and (4.3), Lemma 4.3, Lemma 4.4 with the current (4.5) and
its divergence, the J_{H,delta} current (4.6), the regular variables H6', H7' and the red-shift current (4.7) with (4.8),
the proof of Proposition 4.1 with the T-current (4.9), Remark 4.5 on l = 1 and l = 0); Appendix A ((A.1)-(A.11), the
class V(delta, R_null, l_0) and Propositions A.4-A.5). [Sch13]: the radiation field r^((n-1)/2) psi and its potential
((5.11)-(5.12), at n = 4 the weight s^(3/2) and V0 = (3/4 + 9 mu/(4 r^2))/r^2), (2.17)-(2.20), Proposition 3.1,
(5.8)-(5.17).

*What was computed (wavegauge5.py W8).* On the W7 system, in the rescaling Hhat = diag(sqrt2, 1, sqrt2, sqrt2, 2 n_S,
sqrt2, sqrt2) H that makes the leading matrix symmetric: (a) the radiation field Psi = s^(3/2) Hhat obeys d_u d_v Psi =
-f (Ahat + V0) Psi - f Uhat Psi, and V_inf = lim r^2 (Ahat + V0) has the eigenvalues (l+a+1/2)(l+a+3/2) -- at least 3/4
at every l >= 2 and at least (3/32) l(l+2): the zero eigenvalue Hung's leading matrix has at l = 2 is lifted by the 3/4
of the five-dimensional radiation weight, so the far-region estimate needs no Hardy inequality (his Corollary 3.3 at l =
2); (b) Uhat Psi = (2f'/f) nabla_L (Psi6 - Psi1) - (3f'/r)(Psi6 - Psi1) and (f'/f) nabla_L (Psi7 - Psi4) -
(3f'/(2r))(Psi7 - Psi4), the zeroth-order parts from the weight; (c) the p-current's divergence, his (4.5) with every
power of s lowered by one, flux s^(p-5) Psi . V_inf . Psi >= 0 at I^+; (d) the red-shift divergence at r = r_h: his
(2.13) with (1/(2M), 2/M) -> (2/r_h, 6/r_h) and three terms new in five dimensions, (1/r_h)|nabla-slash Q|^2,
(2c/mu^(3/2))|Q|^2 and (2c/mu) Q . Q_R, the first-order term entering as 2 Q_R . beta Q_R with beta = diag(0, 0, 0, 0, 0,
2f', f') >= 0; (e) the J_delta current's divergence, his (4.6); (f) the rough Laplacian of S^3 on the one-form S_th dth
and the traceless tensor S_AB, -(k^2 - 2) and -(k^2 - 6), so K = diag(k^2, k^2, k^2, k^2 - 2, k^2 - 6, k^2, k^2 - 2); (g)
A - K/r^2, its regular form and A - A_main/r^2 are of degree at most one in k and the regular form is finite at r_h, so
one angular derivative bounds them uniformly in l; (h) at l = 0, A0 - A0_main/r^2 = O(mu/r^4) and the rescaling
diag(sqrt2, 1, sqrt2, sqrt2) makes A0_main symmetric, V_inf with eigenvalues 3/4, 3/4, 15/4, 35/4. The three divergence
identities are formal: two components, the matrices symbols, the structure the same at seven. Control: V0's sign reversed
and L-bar for L in J^p. The selftest is 8/8 in about seven and a half minutes, the mutants 8/8 in about six minutes; the
l = 0 matrices are cached from W7, which W8 reuses.

*What was deduced.* Section 10.5: the setting and norms of [Hun19] section 2 with (2M, 9M/4, 5M/2, 10M, M) -> (r_h, 9
r_h/8, 5 r_h/4, 10 r_h, r_h), M^-2 -> mu^-1, the radial weights lowered by one for the measure r^3 dr; Proposition 10.3,
his (4.1) with M^-1, M^-3 -> mu^-1/2, mu^-3/2; the proof in his three steps -- the far region on the p-current plus
epsilon J_delta (Lemma 4.4), the horizon on the red-shift current in the regular variables with sigma > 18/r_h and then
large ((4.8)), the T-current in the regular variables and the sum ((4.9)) -- every identity one of (a)-(h), every
inequality Cauchy-Schwarz or a choice of epsilon, R_H, sigma; the remark on l = 0 (his Remark 4.5), which does not bound
h_{l=0}: K* grows. Constants not tracked. Not a decay statement: the right side carries h on [r_rs,H, R_null + r_h],
where Proposition 10.1's master quantities and the gauge vector enter; the rungs' Morawetz estimates (4.3(2)), the
growing source and l = 0 remain. Seated: N1STAR-PROOF.md 10.5 and the closing paragraph of 10.4; ROUTES-OPEN.md 4.5 (the
order: the rungs next) and 4.7; the README; the paper's settling paragraph, Appendix C and D, the retrieval table,
[Sch13] in its references.

*Slips, each caught before anything was committed.* The seven-component divergences in full exceeded the thirty-minute
background limit (exit 143) -- the identities are formal now, two components with the matrices symbolic, which carries
the structure and loses nothing the proof uses, the bounds on the matrices being (a), (b), (g); the first p-current
template had its cross term with the wrong sign (the residual was exactly twice it); the first horizon template lacked
the (1/r_h)|nabla-slash Q|^2 term; V0 enters the system with a minus sign, read off the radiation identity's residual;
substituting r = r_h before replacing the derivatives by symbols left Subs objects; the k-degree script first ran from
the scratchpad and could not import the instrument; Proposition 10.2(vi)'s text and W7's docstring called the quotient
wave operator box_l, (v)'s symbol with the angular term included -- a notational slip, repaired (A carries K/r^2 on its
diagonal, W8(f)); a first statement of the bound on Uhat used the row constants 4 and 6 where the vector bound needs 9
and 13; and the instrument's lines ran past 121 characters four times before the length was asserted in the edit itself.
The sixteenth verifier was sent on W7, hung4.py, W8 and Proposition 10.3 with the D47 repairs.

*The sixteenth verifier* (W7, hung4.py, the D47 repairs, W8 and Proposition 10.3; Hung's and Schlue's papers were
unreachable to it through the proxy, so every item 'against Hung' was checked against the record's quotations and its own
derivations; it re-derived (a), (c), (d), (e), (f), the spectrum, the bound (10.9) in structure and numerically to l =
60, and the flux signs, and ran every selftest: wavegauge5 8/8 in 7m25s, its control False, mutants 8/8, hung4 2/2 and
3/3, bondi5 --verbose as repaired). Verdict: no blocking and no major finding. Four minor, each seated: (1) Step 1's
J_delta cross term was bounded with Hung's four-dimensional power s^(-3-delta) and absorbed by 's^(-3-delta) <= s^(p-4)',
which is false for p < 1 - delta; the five-dimensional powers are s^(-8-delta) on the gradients and s^(-10-delta) on
|Psi|^2 (from Q = s^-3/2 Psi), absorbed for every p >= delta -- repaired, the conclusion unchanged; (2) (W8h) called the
(2c/mu) Q . Q_R term new in five dimensions and quoted Hung's c sigma/(8M^2): the same current in four dimensions has c
sigma/(4M^2)|Q|^2 and (c/(2M^2)) Q . Q_R (the verifier's derivation, and this session's, now hung4.py C3, 3/3 and mutants
4/4), so the Q . Q_R term is four-dimensional too and his print differs by the normalisation of c -- two new terms,
corrected in the proof, the route, the paper and here, the print recorded as read; (3) the paper's md5 rows for
N1STAR-PROOF.md, N1STAR-LOG.md and README.md were D47's -- refreshed; (4) the paper's Appendix C said D1-D46 -- D48. Four
notes, each seated: |G_eta|^2 is mu^-2 |(sqrt mu d)^{<= 1} H|^2, not mu^-1; the T part of the red-shift current carries
2c/r^2; Hung's 10M is 5 r_h, and the record keeps R_null >= 10 r_h and says so; dvol_3 on Sigma' is r^3 dv domega / 2 in
the ingoing chart's v (a constant, constants not tracked). Sound by its report: the three steps, the flux signs, the
thresholds, the sufficiency of the two-component formal identities for the seven-component system, W7's regular
variables, hung4.py's two misprint claims as internally consistent, the D47 repairs, the records' consistency. Not
checkable by it: Hung's and Schlue's text, hung4.py's transcription of the printed rows, the W6 --l4 run.

**D49 (2026-10-21, M: "Continue please"): the rungs. The Morawetz current for the Maxwell potential, and the estimates of
[Hun19] Appendix A in five dimensions for every rung of the gauge-vector system (Propositions 10.4-10.5; rungs5.py
M1-M5).**

*What was read.* [HKW18] at source (alphaXiv), section 7 in full (pp. 28-48: Definition 8 and the energy-momentum tensor
(88), the decay foliation 7.3, the Poincare inequality (98) with lambda = 2 on scalar potentials, Lemmas 9-10, the
T-energy comparison (111), the red-shift 7.8 with Lemma 11 'for any bounded radial potential', Theorem 12 with its
Gronwall-type proof, Lemma 13, Theorem 14, the Morawetz currents (119)-(123), the r^p current (125), Proposition 15 with
its proof, Theorem 16, Lemma 17, Theorem 18 with its dyadic proof), 9.3.2 (pp. 54-57: the n = 3 and n = 4 choices of f
and beta, the epsilon_0 and epsilon_1 splits, the g-current, the red-shift addition, the boundary terms at the horizon,
the remark that the construction fails for n >= 5), 10.4.2 and 10.5 (pp. 66-67). ROUTES 4.3(2) and 4.3(6)(a) named the
Morawetz multiplier for the Maxwell potential as the one thing to be done rather than quoted.

*What was computed (rungs5.py).* (M1) the Morawetz identity (123) at n = 3 for a scalar with potential and source,
re-derived from the current on the quotient with the measure r^3 (the source enters as G (F d_r* u + omega u/2)); (M2)
with [HKW18]'s n = 3 choice read in mu = 2M -- F = (1 - 2 mu/r^2)(1 - mu/(2 r^2) + mu^2/(5 r^4)), beta = 1/(2 sqrt mu),
their 1/2 being in units M = 1 -- and the angular term borrowed at k^2 = 8, the bulk coefficient W is -(y^3/40) Q(y)
mu^(-3/2), y = sqrt(mu)/r, with Q of degree ten and no root in [0, 1] by Sturm's count, Q(0) = -300: W > 0 on the
exterior, W >= r^-3/4 for the Maxwell rung and r^-3/5 for the free one, W(r_h) = 17/(4 mu^(3/2)) and 141/(20 mu^(3/2)),
F'/f = dF/dr = mu (25 r^4 - 24 mu r^2 + 12 mu^2)/(5 r^7) > 0 on the closed exterior, the angular coefficient (r^2 - 2
mu)^2 (10 r^4 - 5 mu r^2 + 2 mu^2)/(10 r^11); a scan over beta = b0/sqrt mu found the bulk positive for b0 in {0.3, 0.5,
0.707} and negative on part of the exterior for b0 = 0 and b0 >= 1 (the control uses 2); (M3) k^2/r^2 - 4 mu/r^4 >=
k^2/(2 r^2) on the exterior for k^2 >= 8, equality at r_h at k^2 = 8, and |V| <= 4/mu; (M4) V_inf = k^2 + 3/4 and the
remainder -7 mu/(4 r^4) (Maxwell), 9 mu/(4 r^4) (free), the p-current identity (10.7) with the source for one component;
(M5) the g-current identity. Selftest 5/5 in about half a minute, mutants 5/5.

*What was deduced.* Section 10.6. Proposition 10.4, the rung estimate: the N-current, the Morawetz current cut off at
R_null + r_h, and the p-current with epsilon J_delta in one divergence theorem, every bulk positive, no compact-region
term; the source norm (10.16) is the one this proof produces -- mu^1/2 int s^(p+1)|G|^2 in the bulk (the radiation weight
supplies the power, so the s-exponent is Hung's), mu int |G|^2 on the two slices and mu^(3/2) int |nabla_T G|^2 on a
compact region in r, both from an integration by parts in T where the Morawetz bulk degenerates in nabla_T u at the
photon sphere; Hung's degenerate |d G|^2 and |d_r G|^2 terms are not reproduced and the norm is said to be this proof's.
Proposition 10.5, the decay: [HKW18] Theorem 18's dyadic argument with the source weights of Hung's I_source, the samples
at p = 2 - delta-bar and p = 1 with an interpolation of the weights between them, the far part of F from E^0_{L,ang} by
k^2 >= 8 alone (their Lemma 17), the photon-sphere degeneracy lifted by the one-dimensional Poincare inequality in r with
T u and k u (their commutation with T and Omega), and the rate (1 + tau/sqrt mu)^(-2 + p + delta + delta-bar): one delta
more than [Hun19] (A.10), the cost of controlling F between the dyadic samples with (10.17) itself (its right side
carries E^delta, interpolated, hence the loss) rather than with a separate boundedness theorem; said so in the statement.
Two readings of [HKW18] recorded: Proposition 15's hypothesis a_0 > 0 is stronger than its proof uses (a_0 bar = a_0 +
3/4 > 0 at n = 3, which the rungs' a_0 = 0 satisfies -- the 3/4 of Proposition 10.3's V_inf), and their beta = 1/2 is
dimensionful. Seated: N1STAR-PROOF.md 10.6 and the closing paragraph of 10.5; ROUTES-OPEN.md 4.5 (the order: the growing
source, then l = 0) and 4.8, [HKW18] in its references; the README; the paper. Labels: computed, deduced (constants not
tracked), READ; nothing proved. The seventeenth verifier is sent on section 10.6 and rungs5.py; its verdict follows.

*The seventeenth verifier (2026-10-21), and the repairs.* Verdict: three major findings, eight minor, two notes; the
instrument sound (an independent sympy derivation of M1-M5 from scratch reproduced every identity, polynomial and
constant), the arithmetic of 10.6 checked by hand, the records' md5s matching. The majors, each repaired the same day:
(1) the angular term was spent twice at l = 2 -- (M2) borrowed the whole of it into W through k^2 u^2 >= 8 u^2, and (b)
then used it again for the epsilon_1 split, the g-current's absorption and (10.21); at k^2 = 8 the displayed inequality
was false off the photon sphere. Repaired by borrowing half: W := W0 + 4 F (1 - 2 mu/r^2)/r^3 = -(y^3/40) Q(y) mu^(-3/2),
Q of degree ten with no root in [0, 1], Q(0) = -140, W >= r^-3/5 (Maxwell; min r^3 W = 0.240478) and r^-3/7 (free;
0.166665), W(r_h) = 29/(20 mu^(3/2)) and 17/(4 mu^(3/2)), W(r_P) = (11/20 - 51 sqrt 2/160) mu^(-3/2) for both; the other
half stays in the bulk with its coefficient proportional to k^2. Some borrowing is necessary -- r^3 W0 = -27/20 at the
horizon for the Maxwell rung and -> -1/2 at infinity for both -- and the thresholds are 27/112 (Maxwell, set at the
horizon) and 1/16 (free, set at infinity); theta = 1/4 serves both. rungs5.py M2 now certifies the half-borrowed W and
carries a second control, no borrowing at all (six mutants, all caught). (2) The closing paragraph of 10.6 and ROUTES 4.8
claimed that the gauge vector decays at the rate of Proposition 10.5 with the loss of a fixed number of derivatives, each
rung's source norm being the energy norm of the rungs below. Withdrawn: (10.16) asks for mu^1/2 int s^(p+1) |G|^2, a rung
supplies s^(p'-4) |nabla_L Psi|^2 with p' <= 2 - delta, r P's source 2 d_t S would need p' = p + 2, and r X_L's (2 f r/k)
d_r S grows in r -- which is the growing-source problem of 4.3(3), now stated as the next step, with what [Hun19] section
4.3 does read and recorded (tr h as the first rung, homogeneous, decaying at his Proposition A.5's rate with k = 1; P-bar
and W-bar through (4.27)-(4.30); eta_b; the sources G_P, G_0, G_1, G_2 bounded with (1 + tau/M)^2 factors in Lemmas
4.8-4.10 and 5.5). (3) I^(0) omitted the p-weighted data the proof uses: (iv) runs (ii)-(iii) for T u and k u, which
takes (10.17) for T^2 u, k T u and k^2 u and so E^{2-delta}_L for them at tau = 0. Enlarged to every order of T and k;
[Hun19]'s (2.23) at k = 0 carries E^{2-delta}_L for K^{<= 1} only, and the difference is said in the statement. The
minors: the slice term of (10.16) and the support of chi_T (the integration by parts in T is now confined to [r_1, 2 r_h]
around the photon sphere, chi_T supported in [r_0, 5 r_h/2] inside Sigma'', and (10.21) is used directly on [2 r_h, R_1],
where (1 - 2 mu/r^2)^2 >= 1/4); d_r(mu/r^2), not d_r*, in (10.18); the coefficient of |nabla-slash u|^2 is F (1 - 2
mu/r^2)/r; (10.21)'s weight r^-1 s^-2, with the constant depending on R_null, now in the statement of Proposition 10.4;
the source of the radiation variable s^(3/2) G and the second cross term's s^(1-delta); beta^2 F'/f <= 5/(4 r^3) in the
epsilon_0 split, with epsilon_0 <= 3c/(5 + 3c); the F' root count on 12 y^4 - 24 y^2 + 25; the README's W >= r^-3/4 and
"fourteen"; the paper's D1-D48 and the [HKW18] READ scope. The notes: r_0 <= 9 r_h/8 and r_1 >= 5 r_h/4, so that eta_rs
is constant off [r_0, r_1]; one sample time for u, T u, k u, T^2 u, k T u and k^2 u in (ii) and (iii); the cut-off
commutator of (c) paid by epsilon_M K^M; and the one the verifier could not settle -- whether the leaves are t = const
near the photon sphere, which the one-dimensional Poincare inequality in r needs -- settled by reading [Hun19] 2.2 at
source: g = r_* on [5M/2, R_null], so the leaves are t = const on [5 r_h/4, R_null] here, said in the proof. Seated:
N1STAR-PROOF.md 10.6 and the closing paragraph of 10.5; rungs5.py; ROUTES-OPEN.md 4.8; the README; the paper (the
settling paragraph, Appendix A, the [HKW18] and [Hun19] entries, D1-D49, the md5 rows). Labels unchanged: computed,
deduced (constants not tracked), READ; nothing proved. Selftest 5/5, mutants 6/6.

**D50 (2026-10-21, M: "Continue"): the growing source and the l = 0 sector -- [Hun19] sections 4.2 and 8 in five
dimensions (sections 10.7-10.8; growing5.py G1-G5, lzero5.py Z1-Z5).**

*What was read.* [Hun19] at source (alphaXiv): section 4.2 in full (pp. 26-32: (4.10)-(4.20), Proposition 4.7 with
(4.21)-(4.26), the substitution (4.27)-(4.30) with u, (4.31)-(4.34), eta_b and (4.35)-(4.42), Lemmas 4.8-4.10 with their
proofs), section 5 (Propositions 5.1-5.9, Lemma 5.5's proof with its three regions and the loss of a derivative at the
photon sphere, Lemma 5.8's Morawetz function for -2M/r^3), (6.1)-(6.11), section 8 in full (pp. 58-69: (8.1)-(8.33),
Theorem 8.1, Propositions 8.2 and 8.4, Lemma 8.3, the red-shift current (8.34) and the argument for d(tau), c_2(tau),
c_1(oo), Theorem 8.7), Appendix A (A.12)-(A.14) and Proposition A.6, Appendix B. [KI03] at source: sections 2-3 ((2.4)-
(2.8), (2.11)-(2.13), (2.20)-(2.21), (3.1)-(3.7), (3.9)-(3.14)), (6.1), Appendix A (A.1b). The order was ROUTES 4.5's:
the growing source, then l = 0; the l = 0 identities being quick, both were carried in parallel.

*What was computed.* growing5.py: (G1) [KI03]'s (3.7) at n = 3, K = 1, lambda = 0 is Q = 1296 x^3 + (624 m - 144) x^2 +
(36 m^2 - 432 m) x + 16 m^3 + 60 m^2, V_S = f Q/(16 r^2 H^2), and with (3.14) the reconstructed F, F_ab satisfy F^a_a =
-2F and the Einstein equations E_a = 0 modulo the master equation (at three (mu, k) and three radii); at n = 2 the same
transcription is the Zerilli potential. (G2) J = -Gamma[h_RW] in h_RW's components, (10.28); tr h_RW = F^a_a + 6F = 4F.
(G3) the direct system (10.29), Hung's (4.21)-(4.23): d_t X_t eliminated through div X, X_1 := f X_r, the (X_1, X_L) pair
coupled at zeroth order. (G4) in Hung's canonical form (d_r^2 eliminated, u + r carried as an abstract function with
d_t(u + r) = 1, d_r(u + r) = 1 - 1/f) and the normalisation phi = r^(-3/2) Phi_KI (box_l phi = V_phi phi, V_phi = -12 mu
(k^2 + 3)((k^2 - 3) r^2 + 2 mu)/(r^6 H^2)), the sources are exactly G_P = 4 r f d_t d_r phi + c_2 d_t phi + d_t Sigma,
J_t = -2 r f d_t d_r phi + c_t d_t phi, f J_r = -2 r d_t^2 phi + O(mu/r^2) d_r phi - r f V_phi phi, J_L = 0, 4F = 2 r f
d_r phi + c_F phi -- a first pass in the other canonical form (d_t^2 eliminated) showed apparent fourth-order terms with
r^3 weights, which were the artefact of that form; the coefficient functions read at k^2 = 8, 24, 48 and fitted in k, the
fit checked at a fourth mode, k^2 = 80 (added on the eighteenth verifier's note). (G5) the substitutions: r P-bar = r P -
r^2 d_t phi + (u + r)((2 k^2/3) phi + Sigma/2), X_t-bar = X_t + (r^2/2) d_t phi - (u + r) phi, X_1-bar = X_1 + (r^2 f/2)
d_r phi + (m r^4 + 6 mu^2)/(r^3 H) phi, X_L-bar = X_L + (k r/2) phi, each coefficient forced as 10.7 says (a hand
estimate 7 k^2/6 for the (u + r) phi coefficient was wrong; the computation gives 2 k^2/3 at every mode, and with the
coefficient halved to k^2/3 an O(1) d_t phi survives -- the control); the residual sources carry no second-order term,
every coefficient O(r^-2) or better, the (u + r)-weighted ones O(r^-4), and r P-bar's Sigma terms are exact, its phi
terms checked to leading order. Selftest 5/5 (about twelve minutes), mutants 5/5. lzero5.py: (Z1)-(Z5), the l = 0
identities (10.23)-(10.26), selftest 5/5 in a quarter of a minute, mutants 5/5; P = r (dW)_tr - 2 W0 is forced (the
coefficient -2 is the one value making box_s P a multiple of d_t S_W), the W3 equation carries f' L' W3 with f' > 0, the
second homogeneous solution of the W0 ODE is 1 + (mu/r^2) log(r^2/mu - 1), the particular W3 for W0 = c_1/r^2 is -c_1/(r
(r + sqrt mu)), W*'s own, and the l = 0 substitution P + (u + r) S_W/2 has the source -(mu/(r^2 f)) nabla_L S_W - (mu/(2
r^3)) S_W.

*What was deduced.* 10.7: the three-region bounds of his Lemmas 4.8-4.10 on the barred and hatted rungs, with the (1 +
tau/sqrt mu) factor on [b r_h, 2 b r_h] and the weights s^-2 nabla_L Sigma, s^-3 Sigma, s^-2 (sqrt mu d)^{<= 1} phi, (1 +
tau) s^-4 phi beyond; Propositions 10.4-10.5 then apply to r P-hat and X_t-hat, and (X_1-hat, X_L-hat) is a system with
the matrix of (10.29) and a source in (10.16). 10.8: his Theorem 8.1's argument on (10.23)-(10.26). What both leave: (a)
the rapid decay of the first rungs (Sigma, phi; S_W at l = 0) -- the hierarchy past p = 2, his Proposition A.5 with k = 1
and A.6, to be derived in five dimensions, where V_inf = k^2 + 3/4 never vanishes and the potentials' tails are r^-4; (b)
his section 6's coupled estimate for (X_1-hat, X_L-hat). Said in both sections and in ROUTES 4.5 and 4.9.

*Seated.* N1STAR-PROOF.md 10.7-10.8 and the closing paragraphs of 10.5 and 10.6; growing5.py; lzero5.py; ROUTES-OPEN.md
4.5 and 4.9; the README; the paper (the settling paragraph, Appendix A, the settling row, Appendix D, the [KI03] and
[Hun19] entries, D1-D50, the md5 rows). Labels: computed (exact at the sample points), deduced, READ; nothing proved; (a)
and (b) open. The eighteenth verifier is sent on 10.7-10.8, growing5.py and lzero5.py; its verdict follows.

*The eighteenth verifier (the same day; one agent, sent on 10.7-10.8, growing5.py, lzero5.py and the records).* No major
finding; six minor and five notes, all seated. Minor: the far-region bound of 10.7 omitted the (1 + tau/sqrt mu) mu^-1/2
s^-4 |Sigma| term its own (10.33) produces (added); (10.25) stood under "what is computed" and is deduced from (8.12)
with f d_r = d_t along the generator (relabelled, in 10.8 and in lzero5.py's docstring); G5 asserted less of (10.33) than
the text printed on lines 2-4 (G5 now checks line 2's d_r phi, phi and (u + r) phi terms exactly -- the last is -V_phi --
and lines 3-4 as single phi terms with the leading coefficients 2 mu k^2 (k^2 + 1)/((k^2 - 3) r^3) and -6 k mu (k^2 +
1)/((k^2 - 3) r^3), which the verifier had derived; the text prints them); this entry misrecorded the G5 control as 7
k^2/6 (it is the coefficient halved to k^2/3); the README's and the paper's import sentences omitted that growing5.py and
lzero5.py import wavegauge5.py; the paper's settling row cited 10.3-10.6 for instruments of 10.7-10.8. Notes: the fit in
k was checked at the fitting points only (a fourth mode, k^2 = 80, is now in SAMPLES; the verifier had run G4 and G5
there itself, passing); a doubled "(G1)"; the second-order flag tested d_t^2 on phi only (now on Sigma too); Appendix D's
R1-R7 is R1-R8; the branch name M's commission quotes at the head of this log carries a model-family word, left as M's
words. What held under its attack: (10.28), (10.30) and all five closed forms of (10.31) from its own Christoffels and
reconstruction with k symbolic; (10.32)-(10.33)'s forced coefficients and the Sigma line by hand; the l = 0 identities
from its own one-form box, Z2 in the stronger joint form (alpha, c) = (-2, 1); _frac's soundness; the mutants as real
controls; the md5 rows, counts and timings. Its verdict: 10.7-10.8 can be relied on as labelled, computed / deduced /
READ, nothing proved, (a) and (b) open. The repairs are seated in this PR before merge.

**D51 (2026-10-21, M: "Continue with the next step of Route A please"): the first rungs' rapid decay -- [Hun19]
Proposition A.5 with k = 1 in five dimensions, and the l = 0 obstruction (section 10.9; hierarchy5.py H1-H4).**

*The step.* ROUTES 4.5's order after D50: the two estimates 10.7 left, first the rapid decay of the first rungs (a), then
the coupled (X_1, X_L) estimate (b). PR #71 had merged (M, 17:11 UTC); the branch was restarted from main.

*What was read.* [Hun19] at source (alphaXiv): Appendix A in full, pp. 70-73 -- (A.1)-(A.14), the assumptions (A.3)
(T-energy), (A.4) (Morawetz), (A.5) (the r^p bulk), (A.6) (derivatives), the commuted potentials V^(j) := V + 2M/r^3 -
j(j + 1)/r^2 + 6 M j(j + 1)/r^3 with (A.7)-(A.9), Definitions A.1-A.2, Remark A.3 (V = 0 qualifies when l_0 >= k),
Propositions A.4-A.6 with the account of [2] (Angelopoulos-Aretakis-Gajic: r^2 L as commutator, the bad term absorbed by
Poincare, the l = 0 extension to p < 4 when the Newman-Penrose constant vanishes), the rate -2(k + 1) + p + (1 + 2k)
delta and the step E^{2,(j)}_L <~ E^{0,(j+1)}_L by Lemma 3.2; Lemma 5.3 with its proof (V^(1)_Z = V_Z - 2/r^2 + 14 M/r^3,
lim r^2 V^(1) = -2, lim V_Z = -8 M/r^3, the polynomial Q_1 and R_Z); Propositions 5.2 and 5.4, Lemma 5.5 re-read; (2.4)
Phi^(j) := (1 - 2M/r)^-1 M s^2 nabla_L Phi^(j-1), (2.19)-(2.23); Proposition 8.2 and Lemma 8.3.

*What was computed.* hierarchy5.py (H1) the commuted equation of Psi_1 := f^-1 r^2 nabla_L Psi for a symbolic
potential: L Lbar Psi_1 = -(2/r)(1 - 2 mu/r^2) nabla_L Psi_1 - f Vcal_1 Psi_1 + f (9 mu/(2 r^3) - r^2 V' - 2 r V)
Psi, Vcal_1 = Vcal - 2/r^2 + 12 mu/r^4, V^(1)_inf = k^2 - 5/4 = (l - 1/2)(l + 5/2); in four dimensions the same
computation gives Vcal_1 = l(l + 1)/r^2 + V^(1), his V^(1) exactly (his 14 M/r^3 counts the radiation field's 2M/r^3
from V; this entry first compared shifts from different baselines and called them different, repaired on the
nineteenth verifier's finding), with the first-order term -(2/r)(1 - 3M/r), which his remark does not print, and the
Psi term f (2M/r^2 - r^2 V' - 2 r V); the normalisation without f^-1 was tried and leaves a Psi term -2 k^2 mu
f/r^5, not uniform in l (the control). (H2) the p-current identity for Psi_1: the first-order term adds 2(1 - 2
mu/r^2) to the |nabla_L Psi_1|^2 bulk, positive beyond r^2 = (10 + p) mu/(4 + p); the Psi_1 nabla_L Psi_1 term
integrated by parts to the bulk r^(p-6) B_1. (H3) B_1 = ((2 - p)/2)(k^2 - 5/4) + (57/8)(4 - p) mu/r^2 for Sigma,
positive everywhere for l >= 1; for phi, B_1 >= (1/4)(2 - p)(k^2 - 5/4) for r >= R_1 = 8.14 r_h at k^2 = 8 and
everywhere at k^2 = 24, 48, 80 (p in [1/10, 19/10], a grid of 21, the first root in mu/r^2 found numerically to
thirty digits); the base bulk B_0 = ((2 - p)/2)(k^2 + 3/4) + (9/8)(4 - p) mu/r^2 for Sigma and R_0 = 10.56, 4.61,
3.04, 2.29 r_h for phi; (A.9): r^4 |V_phi|/mu <= 12 (k^2 + 3)/(k^2 - 3) = 26.40, 15.43, 13.60, 12.94 and r^3
|d_r(r^2 V_phi)|/mu <= 24 (k^2 + 3)/(k^2 - 3) = 52.80, 30.86, 27.20, 25.87, the suprema at infinity (this entry
first gave grid values over r <= 6.3 r_h, 25.13 and 47.84 at k^2 = 8, repaired on the nineteenth verifier's
finding), with V_phi -> -12 mu/r^4; (A.3): min r^2 (k^2/r^2 + V_phi) = 4/11, 124/9, 628/17, 5692/83, at the horizon,
and -1 at k^2 = 3 (the control). (H4) l = 0: V_inf = 3/4, V^(1)_inf = -5/4; the base bulk (3/8)(2 - p) + (9/8)(4 -
p) mu/r^2 is negative for p > 2 once r^2 > 3(4 - p) mu/(p - 2); in four dimensions the l = 0 bulk is (3 - p) M
r^(p-6), positive to p = 3 (the control asserts the five-dimensional sign of it). Selftest 4/4 (about a minute),
mutants 5/5.

*What was deduced.* Proposition 10.6, the rate (1 + tau/sqrt mu)^(-4+p+3 delta) for Sigma and phi at l >= 2 against
I^(1)[u], by his Proposition A.5's argument on (10.34)-(10.35) and H3: the base hierarchy, the commuted one with the bad
term absorbed into the base bulk at the same p (mu^2 r^(p-8) Psi^2 <= (mu/R_null^2) mu r^(p-6) Psi^2), the Hardy step
E^{2,(0)}_L <= 4 (100/99)^2 E^{0,(1)}_L with his exponents, in 10.5's normalisation Phi^(0) = s^(3/2) u and Phi^(1) =
sqrt(mu) f^-1 s^2 nabla_L Phi^(0) (the constant 4 and the identification of the norm with Psi = r^(3/2) u, first written
here, repaired on the nineteenth verifier's finding), and the dyadic argument twice. With it 10.7's bound closes as his
Lemma 5.5 and (a) is done for l >= 2. At l = 0 his route does not transcribe: Proposition A.6(1) needs V_inf = 0, and in
five dimensions V_inf = 3/4; S_W gets Propositions 10.4-10.5's rate only, and 10.8's conditional stands undischarged --
open, with two routes named (a different commutator at l = 0 in odd dimension; his Appendix B's O_j bounds at the weaker
rate).

*Seated.* N1STAR-PROOF.md 10.9, the closing paragraphs of 10.7 and 10.8; hierarchy5.py; ROUTES-OPEN.md 4.5 and 4.10; the
README; the paper (the settling paragraph, Appendix A, the settling row, Appendix D, the [Hun19] entry, D1-D51, the md5
rows). Labels: computed (exact; the radii and constants at four modes), deduced (Proposition 10.6), READ; nothing proved;
l = 0 and (b) open. The nineteenth verifier is sent on 10.9 and hierarchy5.py; its verdict follows.

*The nineteenth verifier (the same day; one agent, sent on 10.9, hierarchy5.py and the records).* No major finding; five
minor and four notes, all seated. Minor: (1) the four-dimensional comparison -- the record's own computation reproduces
Hung's V^(1) exactly, his V^(j) being counted from V, which already carries the radiation field's 2M/r^3 at j = 0, so his
14 M/r^3 is the 12 M/r^3 by which Vcal_1 exceeds Vcal - 2/r^2; the record had compared shifts from different baselines;
H1 now asserts the agreement, and 10.9, ROUTES 4.10 and this entry say it; (2) the (A.9) constants were grid suprema over
r <= 6.3 r_h; the exact suprema are 12 (k^2 + 3)/(k^2 - 3) and 24 (k^2 + 3)/(k^2 - 3), attained at infinity (26.4 and
52.8 at l = 2), now proved in H3 by Sturm sequences; (3) the Hardy step's constant is 4 (100/99)^2 in 10.5's
normalisation Phi^(0) = s^(3/2) u with Phi^(1) := sqrt(mu) f^-1 s^2 nabla_L Phi^(0) (his M s^2), the record having
written 4 and identified the norm with Psi = r^(3/2) u, off by a power of mu; the exponents were right; (4) l >= 1
against l >= 2 -- Proposition 10.6 is stated for l >= 2, Sigma alone at l >= 1 (for phi at l = 1, (A.3) fails), and 10.7,
10.8 and ROUTES 4.5 now say so; (5) ROUTES 4.9's label line said (a) and (b) open after (a) was done for l >= 2. Notes:
the paper's settling sentence now says every mode but the spherically symmetric one; the p-grid is complete because the
difference is affine in p, now checked; H3 now pins the radii, the (A.9) suprema and the (A.3) minima, the last exact at
the horizon because the function decreases in mu/r^2 (checked); H4's five-dimensional claims had no control -- V^(1)_inf
at l = 0 is now computed from H1's equation, and a second control drops the radiation field's (3/4)/r^2; a first attempt
at that control, V_inf claimed 0 at l = 0, passed and so was vacuous, because the Psi^2 bulk -(1/2) r^(3-p) d_r(r^p Vcal)
does not depend on how V_inf is split off -- V_inf's own role is the sign of the flux at null infinity, which is (A.8).
hierarchy5.py now: selftest 4/4 (about a minute), mutants 6/6. What held under its attack: (10.34) and (10.35) by two
independent routes and in Minkowski; B_0, B_1 and the l = 0 root; the radii to four digits; the absorption of the bad
term into the base bulk at the same p; the three deltas; the obstruction stated as the method's; the md5 rows and counts.
Its verdict: 10.9 can be relied on as labelled once these sentences are repaired; they are, in the PR that seats 10.10.

**D52 (2026-10-21, M: "Continue please"): the coupled estimate -- [Hun19] section 6 in five dimensions (section 10.10;
coupled5.py K1-K6); route A carried through for l >= 2.**

*The step.* ROUTES 4.5's order after D51: the coupled (X_1, X_L) estimate, 10.7's (b). PR #72 had merged (M, 17:45 UTC);
the branch was restarted from main. The nineteenth verifier, sent on 10.9, had not reported when this step began; its
findings are seated beside this entry when it does, and the twentieth is sent on 10.10 after it.

*What was read.* [Hun19] section 6 in full at source (alphaXiv), pp. 38-55: Proposition 6.1 and Decay[W], the assumption
(6.3), the identities (6.8)-(6.11) with F_1, F_2, F_3, the T-current (6.12)-(6.19) with A_W,in, A_W,ex, A_W,aux and his
positivity matrices ("only semi-positive definite with eigenvalues {0, 6}" at l = 1, p. 40), the Morawetz current
(6.22)-(6.27) with A_W,Mor, M_[bM,oo), M_[2M,bM] and the polynomials p_1, p_2, p_3, the f-bar current J_3,2, the r^p
current (6.28)-(6.32) with A_W,main and A_W,sub, section 6.5 with the order of the constants C_1, epsilon_2, epsilon_4,
R_T, b, and the dyadic argument (6.35)-(6.37).

*What was computed.* coupled5.py (K1) at l = 2, for the scalar-type one-form with W6's S, P, Q_t, Q_r: d_r X_1 + (3/r)
X_1 + (k/r) X_L = S + f^-1 d_t X_t, f d_r X_L + (f/r) X_L + (k/r) X_1 = (k f/r) Q_r, d_t X_1 = f (P + d_r X_t), and d_t
X_L = (k/r)(Q_t - X_t), the last not in his list; W6 re-run for Q_r and Q_t in terms of S, P and J. (K2) r^2 V -> [[k^2 +
3, 2k], [2k, k^2 - 1]] with eigenvalues (l + 1)(l + 3), (l - 1)(l + 1); his leading matrix's (l + 1)(l + 2), l(l - 1)
reproduced; the antisymmetric part (k mu/r^4)[[0, -2], [2, 0]]; A_12 = 0 at r^2 = 2 mu with a change of sign. (K3) the
weighted T-current identity for generic C and N; N_in (weight 10) and N_ex >= (k^2/4) r^-2 I for every real k^2 >= 8 on
[0, 1] and [0, 1/2] in mu/r^2, by Sturm sequences on the coefficients in k^2 - 8; with weight 1, N_in indefinite at the
horizon at k^2 = 8 (the control). (K4) the Morawetz identity for a pair with arbitrary V and symmetric M, and the
g-current, both exact with generic functions. (K5) the cross term -(2 k mu F/r^4)(X_L Y_1 - X_1 Y_L) and its completion
at the cost k^2 mu^2 F^2/((dF/dr) r^8); W_rest >= r^-3/40 on the exterior for every real k^2 >= 8, exactly. It was found
by exploring before it was checked: with half the angular term kept, the bulk is negative at l = 2 at infinity (-3/2
r^-3) and slightly negative at l = 4, 6 near 1.25 r_h; with a tenth kept it is positive, its least value 0.0352 r^-3 at l
= 2 at 1.261 r_h; beta = 1/4 and 3/4 were tried and are worse; completing the cross term into half of the radial square
instead (to keep the rest of it) fails at the horizon, so the full square is used and the radial derivative is recovered
from the completed square and the kept angular term. (K6) the radiation equation for the pair, V_inf = [[k^2 + 15/4, 2k],
[2k, k^2 - 1/4]] with eigenvalues (l + 3/2)(l + 5/2), (l - 1/2)(l + 1/2), the remainders O(mu/r^4) and the antisymmetric
part. Selftest 6/6 (about a minute), mutants 6/6.

*What was deduced.* Proposition 10.7, the pair at (1 + tau/sqrt mu)^(-2+p+3 delta) against Decay[X], by his section 6 on
K1-K6: the T-current's inner error through F_3, its outer error absorbed by the r^p bulk; the red-shift step by [HKW18]
Lemma 11 for a bounded matrix potential, deduced without a computation; the Morawetz bulk positive without the
compact-region substitution, which five dimensions does not need because the class starts at l = 2 where the pair is
definite; the photon-sphere degeneracy of the derivatives removed by (10.38) as his (6.8)-(6.9) remove it; the r^p
current with V_inf positive definite; his 6.5 and the dyadic argument. With 10.6, 10.9 and 10.10, every component of the
gauge vector and h = h_RW + pi_X decay in harmonic gauge at every mode l >= 2 of the class: route A carried through for l
>= 2, his Theorem 2.4(1) in five dimensions, deduced, by his section 7: Proposition 10.3 with its compact region bounded
by the master field and the gauge vector there. Open: l = 0 alone (10.9's obstruction), and with it the final state c_1
K* + c_2 pi_{W*} of Proposition 10.2(iv).

*Seated.* N1STAR-PROOF.md 10.10 and the closing paragraphs of 10.7 and 10.9; coupled5.py; ROUTES-OPEN.md 4.5, 4.9's last
bullet, 4.10 (its last bullet, and three more with the nineteenth verifier's repairs) and 4.11 (this list first named
4.10's last bullet alone; corrected on the twentieth verifier's note); the README; the paper (the settling paragraph,
Appendix A, the settling row, Appendix D and its import sentence, the [Hun19] entry, D1-D52, the md5 rows). Labels:
computed (exact; K1 at l = 2, K3 and K5 for every real k^2 >= 8), deduced (Proposition 10.7 and the l >= 2 conclusion),
READ; nothing proved; l = 0 open.

*The twentieth verifier (the same day; one agent, sent on 10.10, coupled5.py, the 10.9 repairs and the records).* No
major finding; six minor and eight notes, all seated in the PR that seats 10.11. Minor: (1) the photon-sphere step of
Proposition 10.7 (iii) bounded the angular term through (10.38) with a constant of order k^2 -- the first identity of
(10.38) carries (k/r) X_L -- so not uniformly in l, while 10.10's "What this gives" sums the modes; repaired by the route
this entry had named: the completed square bounds (dF/dr)|f d_r X|^2, the completion cost is at most 35/13 of the kept
tenth of the angular term (their ratio 50 x (1 - x/2 + x^2/5)/(25 - 24 x + 12 x^2), increasing in x = mu/r^2, now
computed in K5), and the identities then bound the angular term; (10.39) now says its constant is independent of l. (2)
The paper said the coupled estimate's Morawetz step needs none of Hung's compact-region substitutions, while step (iii)
uses (10.38) at the photon sphere and step (i) uses F_3: now "needs none of Hung's substitutions for its positivity". (3)
10.10's opening and coupled5.py's docstring said every current is computed; the red-shift current is deduced, now said.
(4) K3's sub-check of the inner error compared an expression with itself; it now forms C V - N_in and V - N_ex whole. (5)
coupled5.py's docstring called N_ex sym(V); it is [[V_11, V_12], [V_12, V_22]], now said. (6) The README's D1-D49, stale
since D50, now D1-D53. Notes: K5's discriminant branch was never used -- d_1 >= 0 on the exterior, with a double zero at
the photon sphere -- now asserted and the branch removed; the T-current's join adds c_1' f d_r X_1 d_t X_1 on [R_T, 4
R_T], again in F_3 alone, now computed in K3 and said in (i), with b r_h >= 4 R_T; (ii)'s coefficients are bounded per
mode, uniformity in l coming from the red-shift's angular term as in Proposition 10.3's Step 2, now said; the attribution
of C = diag(10, 1) to Hung, which the verifier could not check -- READ at source, pp. 41-42, (6.17)-(6.18): his J_1,1 +
J_1,2 weighs T[W_1] by 10 and T[W_2] by 2, now said in 10.10, coupled5.py and ROUTES 4.11, the five-dimensional (10, 1)
standing on K3; the 10.9 reading of his V^(j), which it could not check either -- READ at source, p. 71: "V^(j)(r) :=
V(r) + 2M/r^3 - j(j + 1)/r^2 + 6Mj(j + 1)/r^3", which carries the radiation field's 2M/r^3 at j = 0, so the repaired
comparison of D51 stands; the paper's Review bullet and Appendix C stopped at the sixteenth verifier, now through the
twentieth, with 10.11 marked unread; this entry's Seated list omitted ROUTES 4.9's last bullet and three bullets of 4.10,
now named; c' in (iii) is a function, now defined. What held under its attack: K4 and K5 rebuilt from scratch (its W_M
equal to the record's w_rest), the factorisation of e and the signs of a_1, a_2, d_0 and d_1, the minimum 0.0352 at 1.261
r_h at l = 2 on a 200,000-point grid, the keep and beta trials, K1 and (10.29) by an independent Christoffel computation
at l = 2, K3's positivity on a grid, every coupled5 mutant failing a substantive sub-check, the 10.9 repairs and the 27
md5 rows. Its verdict: 10.10 can be relied on as labelled once these sentences are repaired; they are. coupled5.py now:
selftest 6/6 (about a minute), mutants 6/6.

**D53 (2026-10-21, M: "Continue"): the l = 0 sector by another route -- the commuted hierarchy at l = 0 with a Hardy
absorption (section 10.11; lzerorate5.py Y1-Y5); route A carried through for every mode of the class.**

*The step.* ROUTES 4.5's order after D52: the l = 0 rapid decay by another route. PR #73 had merged; the branch was
restarted from main at f7a5577. The twentieth verifier, sent on 10.10, reported during this step; its findings are seated
above, beside D52, in the same PR.

*What was read.* At source (alphaXiv): [Hun19] section 8, pp. 58-70, in full, with Proposition A.6 ((A.12)-(A.14)) and
Appendix B, pp. 73-75. The l = 0 theorem's rate (1 + tau/M)^(-2+2 delta) comes from his Lemma 8.5, Err_{l=0} bounded by F
and the integrated B-bar of D^{<= 7} P-hat and S_W; c_1(oo) exists because c_1' is an exact tau-derivative of a quantity
that tends to zero; his Proposition 8.4 rests on Lemma 8.3's middle region, where G_P carries (1 + tau/M) |(M d)^{<= 1}
S_W|, which his Proposition 8.2's rate pays. [Sch13]: Theorem 1, Proposition 4.1 with its proof, Corollary 4.3,
Propositions 4.21-4.22 and (5.8)-(5.22); Proposition 4.1 holds with "no restriction on the spherical harmonic number".
And, for the twentieth verifier's two open questions, [Hun19] p. 71 and pp. 40-42.

*What was computed.* lzerorate5.py: (Y1) at k = 0 the commuted equation (Vcal_1 = -5/(4 r^2) + 57 mu/(4 r^4), C = 9 mu
f/(2 r^3)), the base current's |nabla_L Psi|^2 coefficient p f/2 - mu/r^2, and (10.35) on the outgoing leaf, the f's
cancelling; (Y2) the Hardy identity, its constant checked on w = 1 - R/r, the exact absorption identity (10.42) and the
perfect square for the bad term; (Y3) Q(p, x) and its corners, positive on [1/10, 9/10] at R_null = 10 r_h and on [delta,
1 - delta] at R_null = 3 r_h/delta^(1/2), and the leading-order window V^(1)_inf > -2, open in five dimensions at l = 0
and empty in four; (Y4) B_0 >= (3/8)(2 - p) and the T-energy density at most 12 times the p = 1 bulk on x <= 1/100; (Y5)
the cut-off source of P-hat, its growing terms in S_W and d_r S_W only, and (10.26) re-derived. Selftest 5/5 (about half
a minute), mutants 7/7. Found by exploring before it was checked: 10.10's Morawetz multiplier with M = 0 is of both signs
at l = 0 (r^3 s_0 is 3/4 at infinity and -1/2 at the horizon with beta = 0, and other choices of beta tried change sign
too), so the base Morawetz estimate at l = 0 is taken from [Sch13], READ, not computed; and the window is the
leading-order condition (4 + p)(2 - p) > 5.

*What was deduced.* Proposition 10.8: S_W at (1 + tau/sqrt mu)^(-3+p+3 delta), by the commuted hierarchy on [delta, 1 -
delta], whose bulk's zeroth-order term is the base energy one level up; P-hat at (1 + tau/sqrt mu)^(-1+4 delta), its
source decaying at that rate uniformly in p; W' -> c_1(oo) W* and h_0 -> c K* + c_1(oo) pi_{W*} at (1 + tau/sqrt
mu)^(-1+4 delta), by his section 8 and Appendix B. Proposition 10.2(iv)'s conditional and 10.8's are discharged, and with
10.10 route A is carried through for every mode of the class, deduced; the l = 0 rate is a power below his, and the data
need no Newman-Penrose condition.

*Seated.* N1STAR-PROOF.md 10.11, with pointers to it in 10.8-10.10; lzerorate5.py; ROUTES-OPEN.md 4.5, 4.11 and 4.12; the
README; the paper (the settling paragraph, Appendix A, the Review bullet, the settling and verification rows, Appendix D
with its import sentence and commands, the [Sch13] and [Hun19] entries, D1-D53, the md5 rows). Labels: computed
(lzerorate5.py Y1-Y5, exact), deduced (Proposition 10.8), READ ([Sch13]'s Morawetz estimate at l = 0); nothing proved.
The twenty-first verifier is sent on 10.11, lzerorate5.py and the twentieth's repairs; its verdict follows. Next: route
B's item 2, the five-dimensional constraint damping.

*The twenty-first verifier (the same day; one agent, sent on 10.11, lzerorate5.py and the twentieth's repairs).* No
major finding; two minor and nine notes, all seated in the PR that seats 10.12. Minor: (1) "which needs |V^(1)_inf| < 2"
was false as a general statement -- (4 + p)(2 - p) > -4 V1 holds for every V1 >= 0 -- and is now "V^(1)_inf > -2" in
10.11, lzerorate5.py, ROUTES 4.12 and D53 above; (2) 10.8 said 10.11 supplies its (a) and (b), and 10.9 that 10.11 "does
both" of its two options, where 10.11 supplies weaker forms -- S_W at -3 + p + 3 delta for p <= 2 - delta where Hung's
rate is -4 + p + delta up to 4 - delta, by the same commutator with a Hardy absorption -- and re-runs his Appendix B at
the weaker rate: both now say so. Notes: step (a)'s rate is (10.22)'s -2 + p + 2 delta, which [Sch13] Theorem 1's
boundedness would improve by a delta that (c) does not need, now stated; step (d)'s 4 delta in delta-bar's place leaves
10.5's range delta-bar <= 1/10 once delta > 1/40, and the verifier re-ran 10.5 (i)-(iv) to find only 4 delta < 1 and
-1 + 4 delta < 0 used, now said; the red-shift commutator gives Y^j S_W an inhomogeneous equation, so its Morawetz step
is (d)'s deduced one with a source, now said in (a); the [Sch13] quotation read as if the mechanism it named did nothing
at l = 0, and now rests on "for every solution of box phi = 0", the part of his proof that carries l = 0 not identified;
four gaps in the instruments -- Y3's label asserted the B_1 bound and checked only d_x c (now a sub-check of B_1 +
(5/8)(2 - p) = (57/8)(4 - p) x), the closed form Q(1 - delta, delta/9) = delta (25 - 19 delta + delta^2)/18 was never
asserted (now it is), Y1's leaf sub-check compared c with itself (its label now names its content, the substitution L
Psi_1 = f w' and the measure), and coupled5.py's d_2 - e^2 conjunct was d_2's definition (removed; the label says the
top coefficient is a square); the paper's "the window p < 1 at the null radius", where p < 1 is the leading-order
window, now "[delta, 1 - delta]"; c_1(tau) - c_1(oo) decays at the square root of the energy rate, its contribution to
the energy at the rate, now said, conclusion (iii) unchanged; the finiteness of E^{1-delta,(1)}_L is the condition d_r
Psi_1 = O(r^-2), now said; lzerorate5.py's "about a minute", now half a minute (37 s measured). What held under its
attack: an independent sympy check, importing none of the record's code, of the commuted equation at l = 0 and of the
leaf identity with its flux in (u, r) coordinates; the cut-off and null-infinity terms; (10.42) by hand; the absorption
bound and the C-term's cost; the window's corners, its control and Q(1 - delta, delta/9); the four-dimensional
comparison, (4 + p)(2 - p) > 8, empty; Y4; the rates of (c), (d) and (e), re-run; the l = 0 sign claim for 10.10's
Morawetz multiplier; the 10.10 repairs; every control failing a substantive sub-check; the 28 md5 rows. The proxy
refused it arXiv and alphaXiv, so it judged the READ inputs for internal consistency only. Its verdict: 10.11 holds as
labelled, and so do the twentieth's repairs; the sentences it named are repaired. lzerorate5.py now: selftest 5/5 (about
half a minute), mutants 7/7; coupled5.py 6/6, mutants 6/6.

**D54 (2026-10-21, M: "Continue"): route B's constraint damping in five dimensions -- the indicial roots of the
constraint propagation operator at zero energy (section 10.12; damping5.py U1-U6).**

*The step.* ROUTES 4.5's order after D53: route B's item 2. PR #74 had merged; the branch was restarted from main at
365a0ba. The twenty-first verifier, sent on 10.11, reported during this step; its findings are seated above, beside D53,
in the same PR.

*What was read.* At source (alphaXiv, 2026-10-21): [Hin26a] (P. Hintz, Constraint damping on subextremal Kerr
spacetimes, arXiv:2606.27658v2) pp. 1-3, 5, 7, 25, 29, 33-37 (section 4.3 to Remark 4.12, with Theorem 4.9), 67, 69-74
(Appendix A) and 85; [Hin26] (arXiv:2606.28253v2) pp. 1, 4, 25-26, 29 ((1.43)), 82 (Definition 4.2) and 136 (Theorem
7.1). His damping is C omega = h^-1 (2 c (x)_s omega - (1 - e) g iota_{c#} omega), c = r^-1 (dt - v dr); (1.43) asks the
zero energy operator of box^C for no indicial root with real part in [-C_0, 1); and the indicial roots see only the
Minkowski model at infinity.

*What was computed.* damping5.py: (U1) the indicial families from the definitions on Minkowski^{n+1}, n = 3, 4, the
four-dimensional ones his (4.19), (A.2), p_s0 and (A.13); (U2) the trace weight 2/(D - 2), which alone makes G C his
form; (U3) the five-dimensional polynomials, lam = 2 at l = 0 and 1, the h = 0 sextic 8 v (lam - 2) Q_5; (U4) the
certificate, Proposition 10.9; (U5) his weight 1 failing in five dimensions; (U6) a numerical survey over (e, h).
Selftest 6/6 (about eighty seconds), mutants 6/6. Found by exploring before it was checked: his weight transcribed
literally puts a root in (-1, 1) at l = 0, so the weight is the dimension's; U6's first statement, the upper roots above
2 once h is small against e, failed against lam = 2 at l = 1, a root for every (e, h) -- now set aside and found at all
nine, the others above 2 exactly where h <= e; and the certificate at 19/10 extends to the line 2, the cofactors of
lam - 2 at l = 0 and 1 allowing it: the strip [-100, 2) is clear but for the Coulomb root, simple, and the same at his
weight 1 in four dimensions up to his Coulomb root 1.

*What was deduced.* Nothing: Proposition 10.9 is computed, at one parameter point.

*Seated.* N1STAR-PROOF.md 10.12 with (10.46)-(10.47) and Proposition 10.9, and 10.11's last line pointing to it;
damping5.py; ROUTES-OPEN.md 4.4 item 2, 4.5 and 4.13; the README; the paper (the settling paragraph, Appendix A, the
Review bullet, the settling and verification rows, Appendix D with its import sentence and commands, the [Hin26a] and
[Hin26] entries, D1-D54, the md5 rows). Labels: computed (damping5.py U1-U5 exact, U6 numerical), READ ([Hin26a],
[Hin26]); nothing proved. OPEN: which strip the five-dimensional argument needs; [Hin26] Theorem 7.1 (1), (2) and (4)
for box^C on Tangherlini; the modification E^Upsilon of [Hin26] Proposition 6.12. The twenty-second verifier is sent on
10.12, damping5.py and the twenty-first's repairs; its verdict follows. Next: the rest of route B's item 2.

*The twenty-second verifier (the same day; one agent, sent on 10.12, damping5.py and the twenty-first's repairs).* One
major finding, six minor and seven notes, all seated in the PR that seats 10.13. Major: (1) every record called (v, e,
h) = (1/2, 1/100, 1/1000) "his parameters"; it is not his -- [Hin26a] suggests only v = 1/2 (p. 3), its one numerical
example is at (1/2, 10^-4, 10^-6) (p. 76), and [Hin26] fixes v and C_0 and no e -- and e = 1/100 lies far above the
bound his construction needs, "e_0 < c v^2 for c ~ 0.000152" (p. 33, after Lemma 4.4), so the claim that the strong
damping condition has a five-dimensional construction was unsupported at the stated point. The record's own certificate
passes at admissible points, which it showed; repaired: damping5.py's point is now (1/2, 1/102400, 10^-6), inside the
five-dimensional bound computed in 10.13 (W4: e_0 ~ 0.000069 v^2), the certificate re-run there (U4: [-100, 19/10]
clear, and [-100, 2] but for the Coulomb root), "his parameters" withdrawn wherever it stood, and the first point
recorded as an indicial statement only (10.13 W6). This step had found the same bound independently while the verifier
ran. Minor: (2) "So [Hin26] (1.43) holds in five dimensions" sat in a Proposition labelled computed, where the
computation reaches only the Minkowski model -- now a separate deduced paragraph naming its inputs; (3) Theorem 7.1(3)'s
clause that the roots accumulate only at +-infinity was not covered -- now U3's top-weight check, h^3 (kappa - lam^2)^3
and h (kappa - lam^2); (4) U6's l range was 10^6 over 85 sampled values, not 1.5 10^6 -- now said; (5) the paper's
settling paragraph made the zero-energy condition indicial only and gave the strip without its status -- now with
invertibility, the point inside the range and the transfer deduced; (6) the 10.11 sentence that the commuted J^(alpha)
of [Sch13] vanishes at l = 0, leaving the l = 0 carrier unnamed, was wrong about the proof -- READ at source (pp. 38-39,
43, 47): Step 2 treats pi_{<L} phi, which contains l = 0, by J^(alpha) = J^{X_a,0} + sum J^{X_b,2}(Omega_i .), whose
uncommuted part gives the bulk C(n - 1)/(alpha^2 r^n)(d phi/d r*)^2 ((4.64), (4.71)); now said; (7) "discharges the
conditional" in 10.8 and "10.8's with it" in 10.11 claimed his rate -- now at the weaker rate (-1 + 4 delta). Notes:
U1's closure was read on the t, r, theta components only (its own code asserts every component; the sentence stands);
routh_rhp did not refuse a zero constant term -- now asserted; "his p_v ((A.2))" -- the display of his section A.1, now
said; "no root in [-100, 2) but the Coulomb root" was self-contradictory -- now [-100, 2]; [Hin26] p. 29 ties the
strip's endpoint 1 to the shift lam - 1 under delta*, which does not depend on the dimension, so the literal [-C_0, 1)
may be the five-dimensional strip -- READ at source (p. 29) and now 10.12's account of which strip is needed, the
gauge-fixed operator's gap in five dimensions left OPEN; the weight 2/(D - 2) also preserves the form of l_{g,c,e} his
section 3 uses -- now 10.13 W1, whose control is the weight 1 making B indefinite; lzerorate5.py ran in 43 s -- now
"about forty seconds". What held under its attack: U1-U6 re-derived independently (its own Cartesian derivation with
other harmonics, full closure at three points, its own certificate by resultants and a Sturm count over Fractions),
every count reproduced, Hintz's printed four-dimensional formulas matched term by term, the certificate's logic, every
control failing substantively, every READ claim checked at source ([Hin26a], [Hin26], [Sch13] through alphaXiv), the
twenty-first's repairs but two, the 29 md5 rows. Its verdict: Proposition 10.9 and U1-U6 hold as computations; the
labels and the point are repaired.

**D55 (2026-10-21, M: "Continue"): the semiclassical inputs of the constraint damping in five dimensions (section 10.13;
semiclass5.py W1-W6), and the certificate moved inside the range they admit.**

*The step.* ROUTES 4.5's order after D54: the rest of route B's item 2. PR #75 had merged; the branch was restarted from
main at d481823, and M set FRUGAL_ALLOW_EXPENSIVE for the session so that the verifier could be sent. The twenty-second
verifier, sent on 10.12, reported during this step; its findings are seated above, beside D54, in the same PR.

*What was read.* At source (alphaXiv, 2026-10-21): [Hin26] pp. 17, 29 (the reason for (1.43)'s strip), 120-121 (Lemmas
6.10-6.11, Proposition 6.12), 134-137 (section 7.1, Theorem 7.1 and its proof); [Hin26a] pp. 9-10, 25-33 (section 3 and
section 4.1-4.2), 38-41 (Proposition 5.1), 43, 53, 66-68 (Theorem 6.2 and its proof); [Sch13] pp. 38-39, 43, 47 for the
verifier's finding (6). [Hin26] Theorem 7.1 (1)-(2) are [Hin26a] Theorem 6.2, proved by semiclassical estimates whose
inputs are his section 3 (stated for dim M = 4) and section 4's Minkowski symbol calculations.

*What was computed.* semiclass5.py: (W1) his fibrewise theory at n = 4 and the weight 2/3; (W2) the subprincipal symbol
from its definition, his four-dimensional formulas reproduced but Lemma 4.4's a_01, misprinted by a factor e; (W3) the
thresholds at dK+ and R_v, b_K > b_sf - 1 and b_sf < 1; (W4) the interior saddle, its e = 0 limit his, the admissible e
~ 0.000069 v^2 against ~ 0.000154 v^2; (W5) Lemma 4.3 dimension-free; (W6) the two points. Selftest 6/6 (about a
minute), mutants 6/6. damping5.py moved to (1/2, 1/102400, 10^-6), with U3's accumulation check and routh_rhp's guard:
6/6, mutants 6/6. Found by exploring before it was checked: the first statement of W4 took the limit e -> 0 entry by
entry and met a_01's 1/e^(1/2), which the determinant cancels; W6's first statement claimed h < e/10 for h = 10^-6 and e
= 1/102400, which is false -- now h < e, U6's boundary.

*What was deduced.* Nothing new: 10.12's transfer to Tangherlini is now labelled deduced; his Theorems 5.2 and 6.2 in
five dimensions are not deduced here.

*Seated.* N1STAR-PROOF.md 10.13 with Proposition 10.10, and 10.8, 10.11 and 10.12 repaired; semiclass5.py; damping5.py;
lzerorate5.py's header; ROUTES-OPEN.md 4.4 item 2, 4.5, 4.13 and the new 4.14; the README; the paper (the settling
paragraph, the Review bullet, Appendix A, the settling and verification rows, Appendix D, the [Hin26a], [Hin26] and
[Sch13] entries, D1-D55, the md5 rows). Labels: computed (semiclass5.py W1-W6, exact; W4's e_0 numerical), READ; nothing
proved. OPEN: a five-dimensional c of [Hin26a] Proposition 5.1's kind on Tangherlini, his section 5's 3b-estimates and
Theorem B.1 in five dimensions, E^Upsilon. The twenty-third verifier is sent on 10.13, semiclass5.py and the
twenty-second's repairs; its verdict follows. Next: the five-dimensional c on Tangherlini.

*The twenty-third verifier (the same day; one agent, sent on 10.13, semiclass5.py and the twenty-second's repairs).* No
major finding, six minor and seven notes, all seated in the PR that seats 10.14. Minor: (1) the records called the
certificate's point one "his construction admits" -- shown is only that it lies below Lemma 4.4's five-dimensional
bound; his construction also asks e below the black-hole-side bounds of Proposition 5.1 (e', (5.9)-(5.10)) and h below
Theorem 5.2's h_0(e), which he never makes explicit (his one numerical example, p. 76, is plotted, not certified) --
repaired to "below the five-dimensional bound of his Lemma 4.4, h < e chosen here" wherever it stood, with the
uncertified h_0 said, and the black-hole-side bounds met on Tangherlini in 10.14; (2) semiclass5.py's docstring still
said h < e/10 -- now h < e; (3) the reflow of D55 collapsed ROUTES 4.4's numbered items and 4.13's bullets into run-on
paragraphs -- the list layout of d481823 restored with the new text; (4) "his p_v ((A.2))" was repaired in damping5.py
only, while the log said everywhere -- now the display of his section A.1 in 10.12 and ROUTES 4.13 too; (5) Proposition
10.10(iv) dropped Lemma 4.3's range [r_0/2, 2 r_0], beyond r_0 (1 + 1/v) of which c is not timelike -- now stated, with
e <= w < 1 in the proof; (6) "U6 a numerical measurement around it" -- U6's grid does not contain the point; now a
survey at larger e and h. Notes: (7) 10.13's and ROUTES 4.14's OPEN lists omitted section 6's own five-dimensional steps
(the weights of (6.1) with the density r^3, (6.4), (5.16)) and "with them his Theorem 6.2" overstated -- now listed, the
overstatement removed, and S^C of (4.17), section 6's one Minkowski input, said to carry (its computation, not an
instrument here); (8) Proposition 10.10(ii)'s translation into (5.14) rests on b_sf = a_sf + 1 and the |dg|
normalisation -- now labelled deduced, READ at p. 39 in this step; (9) the thresholds -(n - 2)/2, (n - 2)/2 were checked
at n = 3, 4 only -- now said (it checked n = 2, 5 too); (10) the paper set 0.000069 v^2 against his 0.000152, where the
like-for-like figure is the computed 0.000154, e_0/v^2 being nearly independent of v -- now said; (11) the paper's
settling paragraph omitted Theorem 7.1(4), the tf-admissibility -- now listed; (12) W1's control is the weight 1 at n =
4 but the weight 3/2 at n = 3 -- now said; (13) Lemma 3.9 is correct as printed (a flattened extract had lost its
parentheses) -- nothing to change. What held under its attack: W1-W6 and U1-U6 re-derived independently (its own B, S by
Lemma 3.9 at both points, its own Sturm counts and bisection for e_0, the a_01 misprint confirmed basis-independently),
every control and mutant failing on its stated sub-check, every READ at source, the 30 md5 rows, the line lengths and
the paper's guard. Its scan at the point (mpmath, l <= 3 x 10^6) found no root in [-100, 2) but lam = 2 at l = 0 and 1,
the least other upper real part 2.000003.

**D56 (2026-10-21, M: "Continue"): a constraint damping 1-form on five-dimensional Tangherlini (section 10.14; cform5.py
C1-C7), and the twenty-third verifier's findings seated.**

*The step.* ROUTES 4.5's order after D55: the five-dimensional c of [Hin26a] Proposition 5.1's kind. PR #76 had merged;
the branch is main at 1c45342. The twenty-third verifier, sent on 10.13, reported during this step; its findings are
seated above, beside D55, in the same PR.

*What was read.* At source (alphaXiv, 2026-10-21): [Hin26a] pp. 1-3, 38-41 (Proposition 5.1 and its proof, (5.1)-(5.13),
footnote 14: r_2 >= 81m/e^(1/2) on Schwarzschild), 41 (Theorem 5.2, (5.14)-(5.15)), 43, 53 (Proposition 5.1 (4) and (6)
in use), 67 (Theorem 6.2's proof: alpha_K = 1, alpha_sf = -C_0 - 2) and 93 (Theorem B.4). Re-reading p. 39 showed
condition (6) on sf to rest on a delta'_r fixed by (4), which this step then computed rather than assumed.

*What was computed.* cform5.py, in Kerr-Schild time on Tangherlini (mu = 1): (C1) S from its definition on the
Tangherlini metric, of order zero, angle-free, block diagonal, semiclass5.py's at mu = 0; (C2) condition (1), the inner
piece dt + (v/2) dr past timelike for every r > 0; (C3) condition (6) on [r_h/2, oo) at r_0 = 100; (C4) condition (3) at
r_0 = 100; (C5) (5.8) on sf, failing only within 0.00166 of v; (C6) the smallest integer r_0, 86, by every integer in
[2, 86], and 137 at e/4; (C7) (4)-(5) on sf at e = 1/102400, the thresholds b_sf < b* = 0.99341 and b_K > b_sf - b*, and
positivity on all of sf at the weights (1, -102). Selftest 7/7 (about a minute and a half), mutants 7/7. Found by
exploring before it was checked: C6's first form bisected over [30, 100] and so claimed a smallest r_0 it had not shown
-- now every integer is run, and (3) holds at 86 alone below 87; the first reading of (6) on sf fixed delta = 1/100
without the delta'_r that (4) sets -- now C7; the r_0 bound scales neither as e^(-1/4) nor as his e^(-1/2) at these e --
recorded as two measurements, not a law.

*What was deduced.* (4)-(5) off sf in a neighbourhood of it, delta_r not explicit, and the smoothing of c at r_0/2 and 2
r_0, both by his arguments (pp. 39, 41).

*Seated.* N1STAR-PROOF.md 10.14 with Proposition 10.11, and 10.12-10.13 repaired; cform5.py; semiclass5.py's docstring;
ROUTES-OPEN.md 4.4 (its list restored), 4.5, 4.13 (its bullets restored), 4.14 and the new 4.15; the README; the paper
(the settling paragraph, the Review bullet, Appendix A, Appendix C, Appendix D, D1-D56, the md5 rows). Labels: computed
(cform5.py C1-C7, exact; C6 a measurement), deduced, READ; nothing proved. OPEN: his Theorem 5.2 in five dimensions (the
3b-estimates of his section 5, with h_0), section 6's five-dimensional steps, Theorem B.1, E^Upsilon. The twenty-fourth
verifier is sent on 10.14, cform5.py and the twenty-third's repairs; its verdict follows. Next: route B's item 2
continues at his section 5 in five dimensions.

*The twenty-fourth verifier (the same day; one agent, sent on 10.14, cform5.py and the twenty-third's repairs).* No
major finding, four minor and six notes, all seated in the PR that seats 10.15. Minor: (1) "every bound his Proposition
5.1 places on e -- ... Theorem 4.9's ... is met by computation" claimed Theorem 4.9 for every h below an h_0(e), where
Proposition 10.9 is computed at h = 10^-6 (it ran the certificate at 10^-8 and 10^-12 too, the same counts) -- now
"Theorem 4.9's at h = 10^-6"; (2) "where Kerr needs three" put down to rotation a saving that is the time's: Hintz's
three pieces come from Boyer-Lindquist time, and on four-dimensional Schwarzschild in Kerr-Schild time dt + dr/4 serves
alone (its exact check) -- now said in 10.14, ROUTES 4.15 and cform5.py; (3) semiclass5.py's W3 docstring still carried
the thresholds without "at n = 3 and 4" and the translation into (5.14) as computed -- now as in 10.13(ii); (4) the
paper's settling sentence omitted the smoothing of c from what is deduced -- now added. Notes: (5) "by scaling 86
mu^(1/2)" is a deduction (now labelled), and its threshold analysis finds (3) iff r_0 > 85.521 r_h, (6) iff r_0 > 32.900
r_h, and at e/4 (3) iff r_0 > 136.787 r_h, so every r_0 > 85.52 r_h works -- now in 10.14 and ROUTES 4.15 as its
measurement; (6) footnote 14 reads "roughly r_2 >= 81m/e^(1/2)" -- "roughly" restored; (7) with <c, dr> > 0 it is -c#,
not c, that points into the black hole -- now said; (8) the paper's [Hin26a] entry repeated pp. 38-41, 53 and 67, and
10.14's READ omitted p. 93 -- merged, and added; (9) C6's control mutated the assertion, not the instrument -- now the
scan with the window of (3) widened to 121/100; (10) C7's positivity holds to rho_K < 51.33, beyond the stated 10 -- the
statement stands. What held under its attack: Proposition 10.11 and C1-C7 re-derived with its own code (Cartesian
Kerr-Schild coordinates, a Christoffel-free divergence), validated on Hintz's printed Lemma 4.4 entries and the misprint
10.13 named; Lemma 3.8's translation into f e G(c) + 2 (1 - e) <c, dr>^2 > 0 with the signs of (6); the threshold b* =
27307/27306 - 819205^(1/2)/136530; every control failing for its stated reason; every READ at source; every repair of
the twenty-third but (8)-(9) in semiclass5.py's W3; the 31 md5 rows.

**D57 (2026-10-21, M: "Continue please"): the gauge potential operator in five dimensions -- the inputs of [Hin26]
Proposition 6.12 (section 10.15; gaugepot5.py G1-G7) -- and the twenty-fourth verifier's findings seated.**

*The step.* ROUTES 4.5's order after D56: the rest of item 2. PR #77 had merged; the branch is main at 5886b9b. Of the
rest, the modification E^Upsilon of [Hin26] Proposition 6.12 is the piece whose inputs are computations; the
twenty-fourth verifier, sent on 10.14, reported during this step.

*What was read.* At source (alphaXiv, 2026-10-21): [Hin26] pp. 25-26 (section 1.4.1), 82, 113 (section 6, (6.1)-(6.6)),
117-119 (Lemma 6.6, (6.17), Lemma 6.8), 119-124 (section 6.4: Proposition 6.9, Lemmas 6.10-6.11, Proposition 6.12 and
its proof, (6.20)-(6.28)). His Step 1 needs (6.26), <f, omega*> = 4 pi (-i sigma^ + c_b gamma^) != 0, which holds when
(6.21) and (6.23) are real and of one sign; Lemma 6.10's kernel he takes from [AHW24] on Kerr.

*What was computed.* gaugepot5.py: (G1) the indicial roots of box^Ups on 4+1 Minkowski, his Lemma 6.6 reproduced in four
dimensions, the gap (0, 2) and, for e gam^2 > 0, (0, lam_s1,2) with 2 < lam_s1,2 < lam_s0, at the weight 2/3; (G2) the
stationary mode equations on Tangherlini for symbolic l, the dt and spatial parts decoupled; (G3) the identities behind
the kernel for l >= 1; (G4) the l = 0 kernel, W*; (G5) the cokernel functional delta(r - r_h) dr at every l; (G6) the
pairings, 4 pi^2 against his 4 pi (his reproduced), eta != 0, (6.23) = -12 pi^2 c_v - 8 pi^2 c_r; (G7) the first term of
f at infinity, rho^3 by the dimension. Selftest 7/7 (about a minute and a half), mutants 7/7. Found by exploring before
it was checked: the first pairing used r_h^n for the sphere's area, r_h^(n-1), and gave 4 pi mu against his 4 pi -- the
four-dimensional control caught it; G2's first control (2 delta delta* on the dt part) was vacuous, the divergence of a
stationary dt-form vanishing -- now on the spatial part; with the weight 1 the modification near infinity moves the
Coulomb root down into the gap rather than up.

*What was deduced.* The kernel of box(0) on Tangherlini is W* alone: A(r_h) = 0 and three energy identities with
positive forms for l >= 1, the l = 0 computation; delta(r - r_h) dr spans the cokernel once the index is 0; the
augmented operator of his Step 1 is injective in five dimensions, its f in the target space for alpha + 2 < 1.

*Seated.* N1STAR-PROOF.md 10.15 with Proposition 10.12, and 10.14 repaired; gaugepot5.py; cform5.py and semiclass5.py's
docstrings and C6's control; ROUTES-OPEN.md 4.4, 4.5, 4.15 and the new 4.16; the README; the paper (the settling
paragraph, the Review bullet, Appendices A, C and D, the [Hin26a] and [Hin26] entries, D1-D57, the md5 rows). Labels:
computed (gaugepot5.py G1-G7, exact), deduced, READ; nothing proved. OPEN: [Hin26c]'s low-energy theory in five
dimensions, his Step 2, mode stability of box at nonzero frequencies, his Theorem 5.2, section 6's five-dimensional
steps, Theorem B.1. The twenty-fifth verifier is sent on 10.15, gaugepot5.py and the twenty-fourth's repairs; its
verdict follows. Next: route B's item 2 continues at [Hin26c] and his section 5 in five dimensions.

**D58 (2026-10-22, M: "Continue"): mode stability of the 1-form wave operator at nonzero frequency in five dimensions --
the input of [Hin26] Proposition 6.9 (section 10.16; modes5.py M1-M5) -- and the twenty-fifth verifier's findings
seated.**

*The step.* ROUTES 4.5's order after D57: the rest of item 2. PR #78 had merged; the branch is main at 6d6a368. Of the
rest, the mode stability of the unmodified operator at sigma != 0 is the piece [Hin26] takes from another paper ([AHW24]
on Kerr), and the one a static background reduces to ODEs.

*The twenty-fifth verifier* (on 10.15, gaugepot5.py and the twenty-fourth's repairs): no MAJOR finding. Every computed
claim of Proposition 10.12 reproduced with its own code -- Cartesian coordinates for the indicial roots, the Hodge
Laplacian for the mode equations and pairings, and a search for a kernel element at l = 1, 2, 3 by integrating the
decaying solutions inward, none found -- and its READ claims matched at source. One MINOR: the record gave box^Upsilon
the kernel W*, which is the unmodified operator's (his Lemma 6.10 is on box, and E^Upsilon exists to remove it; it
computed 2 E_inf G delta* W* != 0); repaired in ROUTES 4.4 (twice), 4.16, 10.15 and the paper. Six notes (nine items),
seated: G3's control now mutates the operator (f -> 1 in the A equation) where it tripped a literal; the W3 docstring
has 10.13(ii)'s qualifier; 10.15's and 4.16's OPEN lists name the high-energy side (his Proposition 6.5, Lemma 6.4,
Lemma 6.1) and the regularity behind the kernel; the weight-1 root is (1 + (9 - 8 gam^2 (1 - 3e))^(1/2))/2, in (1, 2)
only for e < 1/3 and 0 < gam^2 (1 - 3e) < 1 (confirmed here from gaugepot5.indicial); the admissible weight is alpha + 2
in (0, 1), his alpha + 2 + eta < 3/2 being a target weight; the trace weight at the horizon is stated, 2/3, (6.23) being
the same at 1 since tr delta* W* = 0; (6.26) can vanish only if (6.23)/(6.21) <= 0; this record's z is 4 e gam^2, his e
gam^2; READ: E^Upsilon is Definition 4.1 on p. 81 (as the verifier read; Definition 4.2 is E^C), gaugepot5.py's pages
and 10.15's agree at 117-118, 10.14's Theorem B.1 is on p. 87, and the paper's [Hin26a] entry is merged. Fifteen older
lines that opened with "+ " or "> " inside a paragraph -- eleven in N1STAR-PROOF.md, two here, two in ROUTES -- are
reflowed locally; a first attempt that moved one word and cascaded left seven lines over 121 characters, was restored
from git, and redone as a local reflow.

*What was read.* From D57's reading (alphaXiv, 2026-10-21), [Hin26] pp. 118-119: Proposition 6.9 takes high energies
from his Proposition 6.5 and bounded |sigma| >= c_0 from the unmodified operator by [Hin26c] Theorem 9.5's uniform
Fredholm estimates. [KI03b] (ROUTES 4.1; 2026-10-22): (4.23), (5.17), (5.19), (5.20) at zero charge -- the vector and
scalar Maxwell master equations, which (iii) and (iv) reproduce.

*What was computed.* modes5.py: (M1) box = 2 delta G delta* = d delta + delta d on five arbitrary functions of all five
coordinates, Schwarzschild reproducing it and f = 1 - mu/r, not Ricci flat, failing; (M2) the scalar wave, V_0 =
(f/r^2)(kappa + 3/4 + 9 mu/(4 r^2)); (M3) the Maxwell vector type, V_1 = (f/r^2)(lam - 1/4 + 5 mu/(4 r^2)), the record's
harmonic co-closed with lam = (l + 1)^2; (M4) the Maxwell scalar type, R[r^3 F_tr] = (r^2 M_t)' + i sigma r^2 M_r, V_2 =
(f/r^2)(kappa + 3/4 - 7 mu/(4 r^2)), F_tr = 0 and M = 0 forcing the field to vanish, l = 0 by M_r = -i sigma F_tr/f, and
the converse; (M5) positivity for r > r_h at l >= 1 (and V_0 at l = 0; V_2 negative near the horizon at l = 0, the
control), the tortoise coordinate, Cartan. Selftest 5/5 (about 40 seconds), mutants 5/5. Found by exploring before it
was checked: the representative harmonic cos^l th cos l p1 of symbolic degree made the scalar-type reductions slow (164
s for the converse, and over 300 s for the Hodge identity at fixed l, stopped); an arbitrary function S of the angles
with Delta S = -kappa S imposed as a substitution rule took about a second and covers every harmonic, and the Hodge
identity on arbitrary functions of all coordinates 13 s; a zero test by simplify spent 149 s on a control's nonzero
expression, where expanding the numerator took one.

*What was deduced.* The unmodified operator has no mode at sigma != 0, Im sigma >= 0, on five-dimensional Tangherlini,
for modes smooth across the future horizon and outgoing at infinity: delta omega by the scalar master equation (an
energy identity for Im sigma > 0, the constant Wronskian for real sigma), then d omega by the Maxwell ones (positive
potentials at l >= 1, the equation itself at l = 0), then omega = (i/sigma) d(omega(T)) by Cartan, a scalar mode again.

*Seated.* N1STAR-PROOF.md 10.16 with Proposition 10.13, and 10.14-10.15 repaired; modes5.py; gaugepot5.py (G3's control
and the docstring) and semiclass5.py's docstring; ROUTES-OPEN.md 4.4, 4.5, 4.16 and the new 4.17; the README; the paper
(the settling paragraph, the Review bullet, Appendices A, C and D, the [Hin26a] entry and a new [KI03b], D1-D58, the md5
rows). Labels: computed (modes5.py M1-M5, exact), deduced, READ; nothing proved. OPEN: that the kernel elements of his
spectral family in five dimensions lie in the class; his Proposition 6.5 and [Hin26c] in five dimensions; the rest of
item 2 as before. The twenty-sixth verifier is sent on 10.16, modes5.py and the twenty-fifth's repairs; its verdict
follows. Next: route B's item 2 continues at [Hin26c] and his section 5 in five dimensions.

**D59 (2026-10-22, M: "Continue please"): strong trapping admissibility of the gauge potential operator in five
dimensions -- the input of [Hin26] Proposition 6.5, his Lemma 6.4 (section 10.17; trap5.py T0-T4).**

*The step.* PR #79 merged; the branch restarts at main a75e91f. Of item 2's rest, 10.15-10.16 named the high-energy side
of his Proposition 6.9 as OPEN: his Proposition 6.5, from [Hin26c] Theorem 9.16 with his Lemma 6.4 as the input at the
trapped set. The lemma's content is a computation on the null geodesic flow; the theorem is [Hin26c]'s microlocal
analysis.

*What was read.* At source (alphaXiv, 2026-10-22; firecrawl timed out twice at 60 s): [Hin26] pp. 113-116 -- section 6's
opening, (6.1) E^Upsilon = 0 near the trapped set, (6.2), Lemma 6.1, Remark 6.2, section 6.1 with (6.12)-(6.16c), Lemma
6.4 and its proof, Proposition 6.5; and [Hin26c] (arXiv:2606.28008v1) pp. 88 (Definition 4.13: Gamma_0 = {xi = H_G xi =
0} in the future characteristic set; Lemma 4.14), 90-91 (Proposition 4.19, r-normal hyperbolicity), 101-103 (Example
5.4, Remark 5.6 -- "we work in 3 + 1 dimensions for concreteness" --, Definition 5.8, Remark 5.9), 265.

*What was computed.* trap5.py: (T0) (6.13) in five dimensions from the full symbol of 2 delta G delta* on half
densities: principal part G Id, subprincipal part i Gam^c_ab d_zeta_b G, so S_sub = -i nabla_{H_G}; (T1) the trapped set
r^2 = 2 mu, xi = 0, with C = 4 mu sigma^2 > 0, the differentials independent, and the normal expansion rate (2
mu)^(-1/2) = 1/r_ph (four dimensions: r = 3 mu/2, 1/(3^(3/2) M)); (T2) H_G C = 0 and his frame's Gram matrix C J on the
characteristic set, its complement the angular covectors orthogonal to eta; (T3) nabla_{H_G} e_0 = 0, e_1 -> -2 sigma
e_0, e_2 -> -2 sigma e_1, nilpotent (four dimensions: the same, e_3 parallel); (T4) the skew part N + N^* of norm
2^(1/2) eta^(1/2) for diag(1, eta^-1, eta^-2). Selftest 5/5 (about 12 seconds), mutants 5/5. Found by exploring before
it was checked: (6.16c) prints +2 sigma where the computation gives -2 sigma in four dimensions as in five -- his
relation is the computed one with e_1 -> -e_1, the convention not identified, harmless since the matrix is nilpotent
either way; with his inner product diag(1, eta^-1, eta^-2, eta^-3) the norm is of size eta^(1/2), not O(eta) as his
proof says -- harmless, as it tends to 0; the first symbol check failed only through |sin th| in sqrt(-det g), removed
by the chart's volume factor; and the first expansion-rate check compared four dimensions with 1/r_ph, which holds in
five only.

*What was deduced.* His Lemma 6.4 in five dimensions: with diag(1, eta^-1, eta^-2) on span{e_0, e_1, e_2}/C^(1/2) and g
on the complement -- invariant and g-skew, nabla being metric -- the skew part of S_sub is below any eps at the photon
sphere, so box, and box^Upsilon with E^Upsilon vanishing there, is strongly trapping admissible; and the trapped set is
r-normally hyperbolic, the flow on it the periodic geodesic flow of the round S^3 at the normal rate 1/r_ph.

*Seated.* N1STAR-PROOF.md 10.17 with Proposition 10.14, and pointers in 10.15-10.16; trap5.py; ROUTES-OPEN.md 4.4, 4.5,
4.16, 4.17 and the new 4.18; the README; the paper (the settling paragraph, Appendices A, C and D, the [Hin26] entry and
a new [Hin26c], D1-D59, the md5 rows). Labels: computed (trap5.py T0-T4, exact), deduced, READ; nothing proved. OPEN:
[Hin26c] Theorem 9.16 in five dimensions, and with it his Proposition 6.5; the rest of item 2 as before. The
twenty-sixth verifier, on 10.16, has not reported; its findings will be seated when it does, and the twenty-seventh sent
on 10.17 after it, one at a time. Next: route B's item 2 continues at [Hin26c] and his section 5 in five dimensions.

**D60 (2026-10-22, M: "Continue"): the structure and threshold quantities of the gauge potential operator in five
dimensions -- [Hin26] Lemma 6.1, (6.11) and footnote 71 (section 10.18; thresh5.py U1-U4).**

*The step.* PR #80 merged; the branch restarts at main f2f7f3b. Of item 2's rest, [Hin26a] Appendix B (Theorem B.1, the
tf-admissibility of box^C) was read first and is a microlocal theorem -- Fredholm analysis and a spacetime solvability
estimate -- whose five-dimensional inputs are threshold quantities; so are [Hin26c]'s. 10.15 named two of them OPEN:
Lemma 6.1's structure and the regularity behind its deduced (a), whose threshold [Hin26] footnote 71 gives as 3/2 in
four dimensions.

*What was read.* At source (alphaXiv, 2026-10-22): [Hin26a] (arXiv:2606.27658v2) pp. 1-2, 11 and Appendix B pp. 85,
87-88, 90-91, 93, 98 (Theorem B.1, Proposition B.2 and its proof, Theorem B.4, section B.4); [Hin26] p. 124 (footnote
71) and pp. 113-115 again; [Hin26c] pp. 101-105 (Definitions 5.10-5.11 -- vartheta_H+ = sup spec (rho^2/(2 (r_+ - m)))
xi^-1 sigma_1((P_0 - P_0^*)/2i) over N^*H+, s > 1/2 + vartheta_H+ --, Lemma 5.12, Definition 5.13), 158 (Definition 9.4,
with (n - 1)/2 in general dimension), 161-163 ((9.16a)-(9.16c), Theorem 9.5 with (9.20)).

*What was computed.* thresh5.py: (U1) box^Upsilon on 4+1 Minkowski in t* = t - r and the Cartesian frame is -2 d_t* rho
(rho d_rho - 3/2 - S-bar) + (stationary), S-bar omega = gam (omega + omega_t dt* + e <dt*, omega> dt), exact on a
stereographic chart; (U2) its spectrum gam (1 - e), 2 gam, gam, his (6.11)'s, the weight 2/(D - 2) making it
dimension-free (at weight 1 in five dimensions, (3/2)(1 - e) gam); (U3) at N^*H+, K/f'(r_h) lower triangular with
diagonal 1 + c_v gam_H r_h, -1 + 2 c_v gam_H r_h, c_v gam_H r_h -- 4D control 1 + 2 c_v gam mu, -1 + 4 c_v gam mu, 2 c_v
gam mu, his 3/2 at gam_H = 0; (U4) g00 in rho^2 C^oo and g - g-bar = O(rho^2) on Tangherlini. Selftest 4/4 (about 8
seconds), mutants 4/4. Found by exploring before it was checked: S-bar came out right at a boundary point but a symbolic
simplify could not clear the sqrt(x^2) forms, nor the d_t*^2 coefficient; the inverse stereographic chart, on which |x|
= R exactly, settles both.

*What was deduced.* The horizon threshold is s > 3/2 in five dimensions, and for 10.15's c_H = -(1/2) chi dr (c_v = 0)
at every gam_H -- equality where his footnote says "close to"; Lemma 6.1's structure holds with rho d_rho - 3/2 and
S-bar his, (6.7) with a power to spare; outgoing kernel elements ~ rho^(3/2 + S-bar), the threshold at R_out -1/2 +
S-bar as in (9.16c).

*Seated.* N1STAR-PROOF.md 10.18 with Proposition 10.15, and a pointer in 10.15; thresh5.py; ROUTES-OPEN.md 4.4, 4.5 and
the new 4.19; the README; the paper (the settling paragraph, the Review bullet, Appendices A, C and D, the [Hin26] and
[Hin26c] entries, D1-D60, the md5 rows). Labels: computed (thresh5.py U1-U4, exact), deduced, READ; nothing proved.
OPEN: [Hin26c]'s estimates themselves in five dimensions, the threshold at R_in, and the rest of item 2. The
twenty-sixth verifier, on 10.16, has still not reported; its findings will be seated when it does, and the
twenty-seventh then sent on 10.17-10.18. Next: route B's item 2 continues at [Hin26c] and his section 5 in five
dimensions.

**D61 (2026-10-22): the twenty-sixth verifier's findings seated.**

*The verdict* (on 10.16, modes5.py and the twenty-fifth's repairs, checked at ff67ac6): no MAJOR finding. Every computed
claim of Proposition 10.13 reproduced with its own code -- the Weitzenboeck identity in Kerr-Schild Cartesian
coordinates at exact rational points, the reductions in a hyperspherical chart from Christoffel symbols on Gegenbauer
harmonics l = 0..4, the vector harmonic l = 1..6 -- the deduced mode stability walked step by step and found to hold,
the READ claims matched at source ([Hin26] pp. 81, 116-119, 124; [KI03b] pp. 13, 17-18), the twenty-fifth's repairs
made, the fifteen reflowed lines changed only in their breaks.

*Three MINOR, repaired.* (1) The unmodified operator was still called "the gauge potential operator" in the titles of
10.16 and 4.17, the README and the paper's Appendix A bullets for modes5.py, D58's title, and the older gaugepot5.py
bullets; each now says the 1-form wave operator or the unmodified operator. (2) "Positive potentials" was stated without
the spherically symmetric exception -- V_2 r^2/f = 3/4 - 7 mu/(4 r^2) at l = 0, -1 at r_h -- in the paper's main text
and Appendix A and twice in 10.16; each now says l >= 1, the l = 0 Maxwell sector settled by its own equation. (3) The
outgoing class read "an expansion in powers of 1/r": with integer powers it holds no nonzero outgoing field, the
five-dimensional ones carrying r^(-3/2), so the theorem would have been near-vacuous; it now reads a conormal function,
powers of r^(-1/2) sufficing, the conditions uniform on the sphere (the argument used only that the class excludes e^(-i
sigma r*)), in 10.16 and modes5.py.

*Six notes (eight items), seated.* V_1's constant is -1/4, now listed beside the 3/4 of V_0 and V_2; M5 now checks r* -
r + mu/r to its r^-3 coefficient, -mu^2/3, where it showed only o(1/r); the OPEN list names [Hin26c] Theorem 9.5(5)
(kernel elements in A^(3/2 - eps), 10.18(b) with S-bar = 0), the index 0 that makes injectivity invertibility (his p.
119), and the interior uniqueness carrying the vanishing inside the horizon; modes5.py's docstring says M3's control is
caught by its second sub-check and that M4 (e) is not used in the deduction; "F_tr = 0 forcing the field to vanish" now
needs M = 0 and kappa != 0 (ROUTES 4.17, D58); D58's "Six notes" counts nine items, now said; the paper's [KI03b] entry
adds the 2026-10-20 reading of (5.20) (D46); and ROUTES 4.1's F_ai = E_a S_i is now KI03b's F_ai = r epsilon_ab E^b S_i
at Q = 0 ((5.10b), p. 17, as the verifier read). D58's title, its count and its F_tr sentence are corrected in place,
this entry recording it.

*Runs.* modes5.py 5/5, mutants 5/5 after the changes. The twenty-seventh verifier is sent on 10.17-10.18 (trap5.py,
thresh5.py) and these repairs.

**D62 (2026-10-22, M: "Continue"): the inputs of [Hin26c]'s high-energy and Fredholm estimates in five dimensions --
[Hin26] Propositions 6.5 and 6.9 deduced (section 10.19; hienergy5.py V1-V4).**

*The step.* PR #81 merged at 93edd5e; its last commit (a10a62c, D61), pushed after the merge, was rebased onto main as
305fd4c and merged as PR #82; the branch restarts at main 6f1b61c. The twenty-seventh verifier, on 10.17-10.18, is still
out. 10.16-10.18 left OPEN the high-energy estimates ([Hin26c] Theorem 9.16, which with his Lemma 6.4 gives [Hin26]
Proposition 6.5), the threshold at R_in, and, for his Proposition 6.9, Theorem 9.5's kernel class, the index 0 and the
interior.

*What was read.* At source (alphaXiv, 2026-10-22): [Hin26c] pp. 81 (Definition 4.5), 98 (Proposition 4.24), 104-105
again (Definition 5.11(5)-(6)), 158-159 (Definition 9.4, on R^n), 161, 163, 167-168 (Proposition 9.10; (9.32),
vartheta_in = sup sigma_1^b(Im P_0-hat(0))(-2 dr/r) - 2 Re S; (9.37), "symmetric with respect to the Euclidean volume
density r^(n-1) |dr dg|"; (9.41) with (n - 1)/2), 174-175 (Theorem 9.16), 178, 180 (Propositions 9.25-9.27), 182
((Gamma.1)-(Gamma.4), (9.79)-(9.81), and the remark that delta_Gamma(0) is arbitrarily small for tensor-valued
equations), 191 (Proposition 9.35, dr future timelike), 193 (the proof of Theorem 9.16); [Hin26] pp. 116 (Lemma 6.4's
proof, diag(1, eta^-1, eta^-2, eta^-3); Proposition 6.5), 119 (Lemma 6.8's proof: vartheta_in = vartheta_out = S-bar = 0
for the unmodified box), 122 (orders r > -1/2 at R_in), 200 (Remark 10.2).

*What was computed.* hienergy5.py: (V1) on 4+1 Minkowski rho (rho d_rho - c) is skew for rho^(-5) d rho iff c = 3/2, and
for box^Upsilon at the weight 2/3 the first-order part at the incoming covector satisfies A_w + S-bar = D S-bar D, D the
radial reflection, exactly over the sphere -- four-dimensional control at the weight 1, the same; (V2) on Tangherlini
the trapped set of G_1 is r^2 = 2 mu, C = 4 mu, with nu = 4 (2 mu)^(-1/2), {phi_u, phi_s} = nu/f, beta_0 = 2, and the
gap nu/(4 beta_0) = (8 mu)^(-1/2), half trap5.py T1's rate -- four-dimensional control r = 3 mu/2, beta_0 = 3,
1/(3^(3/2) mu); (V3) at a point of the trapped set the connection on trap5.py's frame is nilpotent with V_perp
invariant, spec p_1 = 0, +-(2 eta)^(1/2), delta_Gamma(0) = (mu eta)^(1/2); (V4) W = f/r^2 has one maximum, 1/(4 mu) at
r^2 = 2 mu, there is no ergoregion, and g^-1(dr, dr) = f < 0 inside. Selftest 4/4 (about 25 seconds), mutants 6/6. Found
by exploring before it was checked: the first-order part at the incoming covector leaves the spectrum unchanged -- A_w +
S-bar is S-bar conjugated by the radial reflection, in five dimensions and in four -- so the threshold at R_in is the
mirror of R_out's; and the five-dimensional angular chart is singular at theta = pi/2, so V3's point is theta = pi/4.

*What was deduced.* vartheta_in = -2 S-bar, the threshold at R_in -1/2 - S-bar; (Gamma.1)-(Gamma.4) with delta_Gamma(0)
= (mu eta)^(1/2) -> 0; the dynamics and the interior; with 10.18, [Hin26c] Theorems 9.16 and 9.5 in five dimensions on
the reading that section 9, stated for general n, carries over -- so [Hin26] Proposition 6.5, and with 10.16, the index
0 and uniqueness inside the horizon, his Proposition 6.9.

*Seated.* N1STAR-PROOF.md 10.19 with Proposition 10.16, and pointers in 10.16-10.18; hienergy5.py; ROUTES-OPEN.md 4.4,
4.5 and the new 4.20; the README; the paper (the settling paragraph, the Review bullet, Appendices A, C and D, the
[Hin26] and [Hin26c] entries, D1-D62, the md5 rows). Labels: computed (hienergy5.py V1-V4, exact), deduced, READ;
nothing proved. OPEN: section 9's proofs line by line for n = 4; the low-energy theory and [Hin26] Proposition 6.12;
[Hin26a] Theorem 5.2, section 6 and Theorem B.1. The twenty-seventh verifier's findings will be seated when it reports,
and the twenty-eighth then sent on 10.19. Next: [Hin26c]'s low-energy theory in five dimensions.

**D63 (2026-10-22): the twenty-seventh verifier's findings seated.**

*The verdict* (on 10.17-10.18, trap5.py, thresh5.py and the D61 repairs, checked at a10a62c): no MAJOR finding. Every
computed claim of Propositions 10.14 and 10.15 reproduced with its own code -- S_sub(box) = -i nabla_{H_G} in ingoing
coordinates with hyperspherical angles, the trapped set, and nu by integrating null geodesics (0.620177 against (2
mu)^(-1/2) = 0.620174 at mu = 1.3), the frame relations at exact rational points, S-bar's spectrum in the t* frame, K at
N^*H+ -- the deduced Lemma 6.4 and 10.18's (a)-(b) held, the optimisation over fiber inner products was found legitimate
(Definition 5.11(4)-(5), Lemma 5.12), the READ claims matched at source, the D61 repairs were made consistently, and all
35 md5 rows matched.

*One MINOR, repaired.* Deduced results were summarised as computed: 10.15's "Lemma 6.1's structure (computed in 10.18)"
and "its threshold, 3/2, computed in 10.18", ROUTES 4.4's "its horizon threshold is 3/2 ... (computed)", and the paper's
settling paragraph, which also called the thresholds complete where the one at R_in was open, and said "also under the
horizon modification" where that holds for 10.15's c_H (c_v = 0) only, vartheta_H+ being 1 + c_v gam_H r_h in general.
Each now says K and S-bar computed and the threshold 3/2 deduced for 10.15's c_H, the paper "the horizon and outgoing
thresholds"; the README's and Appendix A's thresh5.py bullets likewise.

*Nine notes, seated.* (1) The sign of (6.16c), traced: with his sigma = -<., d_t> and the standard H_p the coefficient
is -2 sigma, and his source, [Hin24a] Proposition 3.21 (p. 60), obtains +2 sigma with Remark 3.22's e_2, printed with
the sign opposite to its (3.34b); recorded in 10.17's Remark (a), as the verifier read. (2) "O(eta)" against eta^(1/2):
Remark (b) stands, and his Proposition 8.3 (p. 149) has the same wording, now noted. (3) "Expansion rate 1/r_ph" is the
rate per unit t, the normalisation of [Hin26c] Proposition 4.19, not the nu of its (4.48)-(4.49): "per unit t" added in
10.17, ROUTES 4.18 and the paper's Appendix A, and in 10.19, 4.20 and hienergy5.py. (4) S-bar named both the
endomorphism and the number inf Re spec S ([Hin26c] (5.2), p. 100, now READ; [Hin26] footnote 60, p. 114, now READ): a
sentence in 10.18, 10.19, ROUTES 4.19, thresh5.py and hienergy5.py says which is which, and "his (9.20): rho^(1 +
S-bar)" now reads (9.21), rho^(1 + S). (5) thresh5.py's U4 docstring: g - g-bar = mu rho^2 dt^2 + (mu rho^2/(1 - mu
rho^2)) dr^2, and its control fails both conjuncts, now said. (6) ROUTES 4.19 now names K as Proposition 10.15(iii)
does, the symbol at N^*H+ being i xi f'(r_h) K; D60 and U3's code call that matrix K/f'(r_h), recorded here. (7)
Records: 10.18's READ now matches D60's (pp. 100, 104-105 with Definition 5.13, 161-163; footnote 60); the paper's
[Hin26a] entry adds D60's 2026-10-22 reading of Appendix B, its [Hin26c] entry p. 100 and pp. 161-163; Appendix C's
verification row adds the twenty-sixth and twenty-seventh. (8) D61's "Six notes" listed eight items, now said in place.
(9) The threshold at R_in is vartheta_in, a property of the operator, which the order functions must clear: 10.18's
wording repaired.

*Runs.* thresh5.py 4/4 and mutants 4/4, hienergy5.py 4/4, response5.py all pass, after the changes. The twenty-eighth
verifier is sent on 10.19 (hienergy5.py, D62) and these repairs.

**D64 (2026-10-22, M: "Continue please"): [Hin26c]'s low-energy theory in five dimensions -- [Hin26] Proposition 6.12
deduced (section 10.20; lowenergy5.py L1-L3).**

*The step.* PR #83 merged at its head 54ad36c (D62-D63); the branch restarts at main 34a8199. The twenty-eighth
verifier, on 10.19 and D63, is still out. 10.15 left OPEN the index 0, tf-admissibility and the estimates of [Hin26]
Proposition 6.12; 10.19 left the low-energy theory.

*What was read.* At source (alphaXiv, 2026-10-22): [Hin26c] pp. 61 (Lemma 3.11 -- the shift alpha + 3/2 from |dx| to a
b-density --, Definition 3.12, (3.47)), 193-195 (Theorem 9.36 and its proof; section 9.5: (9.110) with (n - 1)/2,
Theorem 9.38 with n/2 and -n + 2 + beta), 197-198 (Corollary 9.39; Proposition 9.40, "Suppose the spatial dimension
satisfies n >= 3", tf-admissible with all weights in (0, n - 2), by Hankel functions), 198-200 (Theorem 9.41 and its
proof, Remark 9.42, Corollary 9.43); [Hin26] pp. 117-124 again.

*What was computed.* lowenergy5.py: (L1) on 4+1 Minkowski the 1-form wave operator acts componentwise and, conjugated by
e^(i sigma r), its spectral family is Delta_e - sigma^2, exactly over the sphere; (L2) at n = 4, u = r^-1 w gives
Bessel's equation of order l + 1, with exponents l and -(l + 2), and the Hankel asymptotics at 0, at infinity and on the
imaginary ray (mpmath, l = 0, ..., 4), so the outgoing solution is excluded exactly for weights below 2; (L3) the shift
n/2 = 2, and d_sigma^2 box(0) W* = 2 g00 W* = -4 mu rho^4 dt + O(rho^5), so the augmentation lies in the target iff
alpha + 2 < 1. Four-dimensional controls: n = 3 throughout. Selftest 3/3 (about 7 seconds), mutants 4/4. Found by
exploring before it was checked: the large-argument Hankel check at x = 10^4 missed its tolerance at order 5, the
correction (4 nu^2 - 1)/(8x) being 1.2 x 10^-3 there, so it is made at 10^6; and the exponent equation, solved with a
positive unknown, returned one root.

*What was deduced.* Theorem 9.36 at n = 4; Proposition 9.40 at n = 4 (READ for n >= 3, the inputs of its proof
reproduced); his Lemma 6.8 in five dimensions; Corollary 9.43, index 0, so 10.15's horizon functional spans the cokernel
of box(0); and his Proposition 6.12 -- box^Upsilon with 10.15's modification mode stable on the closed upper half plane
-- on 10.19's reading of [Hin26c] section 9 at n = 4.

*Seated.* N1STAR-PROOF.md 10.20 with Proposition 10.17, and a pointer in 10.15; lowenergy5.py; ROUTES-OPEN.md 4.4, 4.5
and the new 4.21; the README; the paper (the settling paragraph, the Review bullet, Appendices A, C and D, the [Hin26]
and [Hin26c] entries, D1-D64, the md5 rows). Labels: computed (lowenergy5.py L1-L3; exact, L2's asymptotics numerical),
deduced, READ; nothing proved. OPEN: section 9 line by line at n = 4; [Hin26] section 6.5 and Lemma 6.13; his sections 7
and 8 in five dimensions, and [Hin26a] Theorem 5.2, section 6 and Theorem B.1. The twenty-eighth verifier's findings
will be seated when it reports, and the twenty-ninth then sent on 10.20. Next: [Hin26] section 6.5 in five dimensions,
or [Hin26a] Theorem 5.2.

**D65 (2026-10-22): the twenty-eighth verifier's findings on 10.19 (hienergy5.py, D62) and the D63 repairs, seated.**

*The verifier.* The twenty-eighth, on 54ad36c: no MAJOR finding; three MINOR findings and eight notes. Every computed
claim of 10.19 reproduced, by its runs and by computations of its own -- V1's symbol algebra in five dimensions at the
weights 2/3 and 1 and in four; nu by an RK4 integration of the flow at mu = 1.3, 2.480675 against 4 (2 mu)^(-1/2) =
2.480695; the loss at theta = pi/3 with a generic eta -- and every control fails at its stated sub-check. Deductions
(a)-(d) hold on the stated reading; every READ matched at source; the D63 repairs were made; all 36 md5 rows matched.

*Three MINOR, repaired.* (1) The incoming threshold, and "every input", were called computed where they are deduced --
10.19(d) and its last paragraph, 10.18's pointer, ROUTES 4.4 and 4.5, hienergy5.py's V1 and Deduced paragraph, the
paper's settling paragraph -- and two inputs were not addressed: the horizon's radial point structure (9.24) and a
global t* with dt* past timelike (his Definition 9.3). Each site now separates the computed (A_w + S-bar = D S-bar D,
nu, beta_0, the spectrum of p_1 at a point, W, the time orientation) from the deduced (vartheta_in and its threshold,
(Gamma.1)-(Gamma.4)) and names (9.24) and t* as those of a non-degenerate static horizon, stated and not computed; the
README's and Appendix A's hienergy5.py bullets add "(deduced)". (2) [Hin26c] section 9 was described as stated for
general n. It sets up general n for scalar operators only -- "the purely notational modifications required to treat
operators acting on vector bundles are left to the reader" (p. 158) -- and states Theorems 9.5 and 9.16 on the Kerr
model with three-dimensional numbers: (9.20), (9.21), (9.55) in Part (5) of the proof (p. 172), his Proposition 4.24 in
section 9.3.6 (p. 193); read again at source here (alphaXiv, 2026-10-22: pp. 157-159, 163, 165, 172-173, 193). The
reading in 10.19(d) is now (i) the scalar-to-bundle step and (ii) Theorems 9.5 and 9.16 restated for n = 4, with (9.20)
and (9.55) at 3/2 (10.18(b)) and Proposition 4.24 replaced by (c); its OPEN list adds the scalar-to-bundle step, Lemmas
9.20, 9.21 and 9.33, Parts (3) and (5) of section 9.2.3 and section 9.3.6; (a) and the last paragraph no longer say that
the dimension enters only through (n - 1)/2; ROUTES 4.4, 4.5 and 4.20, hienergy5.py and the paper say the same. No
conclusion changes. (3) V4's docstring claimed g^-1(dr) future directed, which its code did not check: it checked
f(r_h/2) < 0 and f'(r_h/2) > 0, the second unrelated to time orientation. V4 now checks f' > 0 for every r > 0 with
f(r_h) = 0, so the signs hold on the intervals and not at one point, and g_vr = 1, g(d_v, -d_r) = -1, g(g^-1 dr, -d_r) =
-1; Proposition 10.16(iv) states it.

*Eight notes, seated.* (1) V1's identity is structural -- S-bar = (1/2) M(dt - dr) and A_w + S-bar = (1/2) M(dt + dr), M
the first-order symbol of 2 E-bar G delta* -- so it holds by reflection covariance at every weight and in every
dimension: recorded in 10.19's proof and in V1. (2) The control "the outgoing covector" is a sign flip of A_w, which
does not enter at R_out: renamed in 10.19 and hienergy5.py. (3) Proposition 10.16(iii) called gamma_+ and delta_Gamma(0)
computed; they are computed at one point, and hold on Gamma by 10.17's p_1 = 0 on V_perp (deduced) and the symmetry,
which the verifier's check at theta = pi/3 agrees with: (iii) now states the point values and (b) the deduction. (4) The
sign in (Gamma.3) is a normalisation, phi_u -> -phi_u preserving (Gamma.2): said in (b). (5) [Hin26c] p. 100 ((5.2)) and
[Hin26] p. 114 (footnote 60), cited in 10.19 and hienergy5.py, are added to their READ lists, and p. 100 to ROUTES
4.19's. (6) The paper's Review bullet gave the twenty-seventh "(D61)" where its convention, the decision of the sections
read, gives D59-D60, and Appendix C gave the twenty-sixth and twenty-seventh the decisions that seated them: now D58 and
D59-D60 in both, and the twenty-eighth added. (7) His Proposition 6.5 asserts its constant uniform over a compact set of
parameters, and Theorem 9.16's loss is delta_Gamma(Im sigma - eps): (d) says both. (8) The paper wrote A_ω where the
supplement writes A_w: now A_w.

*Runs.* hienergy5.py 4/4 and mutants 6/6 after the change to V4. The twenty-ninth verifier will be sent on 10.20
(lowenergy5.py, D64) and 10.21 once 10.21 is seated.

**D66 (2026-10-22, M: "Continue"): [Hin26a] section 6 in five dimensions -- his Theorem 6.2 deduced from his Theorem 5.2
(section 10.21; cpmodes5.py K1-K3).**

*The step.* The next piece of route B item 2 after 10.20: [Hin26a]'s constraint damping, whose section 6 deduces the
mode stability of the constraint propagation operator -- his Theorem 6.2, [Hin26] Theorem 7.1 (1)-(2) -- from his
Theorem 5.2. 10.12-10.14 had computed the indicial roots, the semiclassical inputs and a c on Tangherlini, and left
section 6's own steps OPEN.

*What was read.* At source (alphaXiv, 2026-10-22): [Hin26a] pp. 1-3, 41-42 (Theorem 5.2, (5.14)-(5.16), footnote 15),
66-69 (the end of section 5.2.7, Definition 6.1, Theorem 6.2 and its proof, (6.1)-(6.4), Remarks 6.3-6.4) and 93
(Theorem B.4), with pp. 9-11, 38-43, 47, 51, 54, 64, 87 and 98 read earlier the same day; [Hin26] p. 135 ((7.3)-(7.6)).
His proof fixes alpha_K = 1 and alpha_sf = -C_0 - 2, applies Theorem 5.2 with C_0 + 1 and Theorem 4.9 with C_0 + 4, puts
a mode's outgoing part in A^1 by the regular-singular ODE of (6.4), and gets the index 0 from Theorem B.1 with [Hin26c]
Corollary 9.43, or from the radial ODEs of a static metric.

*What was computed.* cpmodes5.py: (K1) on 4+1 Minkowski at the trace weight 2/3, box^C = -2 d_t* rho (rho d_rho - 3/2 -
S-bar^C) plus a stationary operator -- the d_t* d_r coefficient 2 Id, no d_t* times a tangential derivative, no d_t*^2
-- with spec S-bar^C = h^-1 {2 (1 - v), (1 - e)(1 - v), 1 - v (3x)}; (K2) at the incoming covector A_w + S-bar^C = D
S-bar^C(-v) D, spec h^-1 {2 (1 + v), (1 - e)(1 + v), 1 + v (3x)}; (K3) the weights: the slab's +1/2, a mode's data in
rho^(-2-eps) H-bar_b (r^3), alpha_sf = -C_0 - 5/2, l in [-C_0 - 2, 0). Four-dimensional controls: his (7.5) spectrum
with the shift 1, and his weights. Selftest 3/3 (about 5 seconds), mutants 3/3. Found by running: the first version
checked only the d_t* coefficient, so the form -2 d_t* rho (rho d_rho - ...) rested on the shift; the d_t* d_x
coefficients are now checked too. The twenty-eighth verifier's note on a mislabelled control in hienergy5.py applied
here as well: K2's control is the sign flip of A_w.

*What was deduced.* (6.4) on Tangherlini with 10.14's c; Part (1) and the injectivity of Part (2) from Theorem 5.2 in
five dimensions with alpha_sf = -C_0 - 5/2 and alpha_K = 1 (10.13's five-dimensional (5.14)); the index 0 by the radial
ODEs, c being spherically symmetric, with 10.12's roots and their even split at Proposition 10.9's point, for C_0 <= 96;
(B.13)'s window in five dimensions; so [Hin26a] Theorem 6.2 on five-dimensional Tangherlini, conditional on his Theorem
5.2 there, which stays OPEN.

*Seated.* N1STAR-PROOF.md 10.21 with Proposition 10.18, and pointers in 10.12, 10.13 and 10.20; cpmodes5.py;
ROUTES-OPEN.md 4.4, 4.5 and the new 4.22; the README; the paper (the settling paragraph, Appendices A, C and D, the
[Hin26a] entry and the [Hin26c] entry with D65's readings, D1-D66, the md5 rows, and Appendix D's mpmath sentence, which
said "the three that import" damping5.py where every program importing it needs mpmath). Labels: computed (cpmodes5.py
K1-K3, exact), deduced, READ; nothing proved. OPEN: [Hin26a] Theorem 5.2 and Theorem B.1 in five dimensions; [Hin26]
Theorem 7.1(4), section 6.5, Lemma 6.13 and sections 7-8. The twenty-ninth verifier is sent on 10.20-10.21
(lowenergy5.py, cpmodes5.py; D64, D66). Next: [Hin26a] Theorem 5.2 in five dimensions, or [Hin26] section 6.5.

**D67 (2026-10-22, M: "Continue"): the inputs of [Hin26a] Theorem 5.2 in five dimensions -- the theorem deduced on a
reading (section 10.22; solv5.py Q1-Q4).**

*The step.* 10.21 rested on [Hin26a] Theorem 5.2 in five dimensions, OPEN. [Hin26] section 6.5 was weighed first and set
aside for now: its Proposition 6.18 is organised by the indicial roots of the linearized gauge-fixed Einstein operator
([Hin26] Lemma 8.4), not yet in five dimensions, and only its Proposition 6.15 stands alone.

*What was read.* At source (alphaXiv, 2026-10-22): [Hin26a] pp. 9, 12-16, 25-27, 38, 41-44, 47-48, 51-52, 54, 56, 58-60,
64, 66; [Hin26] pp. 113, 118, 124-125, 128-129, 131-132 and 138 (sections 6.5 and 7.2, to weigh them). Proposition
5.16's energy estimates rest on Lemma 5.14, stated for any time-oriented Lorentzian vector space, and Corollary 5.15,
stated on R^(1+n) and for n-dimensional manifolds of bounded geometry (p. 60); Propositions 5.5-5.6 on Lemmas 3.5 and
3.7 alone ("does not rely on any fine properties of the null-geodesic flow", p. 44); and the weights enter only through
Proposition 5.1 (4)-(5).

*What was computed.* solv5.py Q1-Q4 (Proposition 10.19): Tangherlini in Kerr-Schild time is a 3sc-metric, g^-1 =
eta^-1 - mu r^-2 k# k#, its Christoffel symbols in mu rho^3 C^oo by Gamma(lam x; mu) = lam^-1 Gamma(x; mu lam^-2), two
powers beyond (2.12) (Schwarzschild: rho^2); r^2 G(d tau) = -(1 - tau^2) - mu r^-2 (1 + tau)^2, so d tau is past
timelike for g_3b for every T < 1, uniformly; dr is future timelike on [r_h/2, r_h); and his Proposition 5.1 (4)-(5)
holds at 10.21's weights (1, -C_0 - 5/2) for every C_0 >= 0, and on all of sf with rho_K <= 10 at C_0 = 96. Selftest 4/4
(about 15 seconds), mutants 4/4. Found by running: the first Q1 took r = |x| literally, and its scaling check over 125
components ran past three minutes; it was stopped by PID, and Q1 now treats r as an independent symbol with d_i =
d/dx_i + (x_i/r) d/dr, the scaling being a homogeneity in (x, r) jointly.

*What was deduced.* Lemma 5.3 and Propositions 5.5-5.6, 5.8-5.12 and 5.16 have their inputs in five dimensions; on the
reading that his 3b-analysis (sections 2.3 and 5.2) holds there, his Theorem 5.2 on Tangherlini at (v, e) = (1/2,
1/102400) with 10.14's c, for alpha_sf < b* - 1 and alpha_K > alpha_sf + 1 - b*, h_0 not explicit; with 10.21, his
Theorem 6.2 there for C_0 <= 96, on the same reading.

*Seated.* N1STAR-PROOF.md 10.22 with Proposition 10.19, and pointers in 10.21; solv5.py; ROUTES-OPEN.md 4.4, 4.5 and the
new 4.23; the README; the paper (the settling paragraph, the Review bullet, Appendices A, C and D, the [Hin26a] entry,
D1-D67, the md5 rows). Labels: computed (solv5.py Q1-Q4, exact), deduced, READ; nothing proved. OPEN: the line-by-line
reading of [Hin26a] sections 2.3 and 5.2 at n = 4, and h_0; his Theorem B.1 and [Hin26] Theorem 7.1(4); [Hin26] sections
6.5, 7.2 and 8 in five dimensions. The twenty-ninth verifier is still out on 10.20-10.21; 10.22 goes to the thirtieth.
Next: [Hin26a] Theorem B.1 in five dimensions, or [Hin26] section 7.2.

**D68 (2026-10-22): the twenty-ninth verifier's findings on 10.20-10.21 (lowenergy5.py, cpmodes5.py; D64, D66),
seated.**

*The verifier.* The twenty-ninth, on c5d17a2: no MAJOR finding; four MINOR findings and twelve notes. Every READ it
checked matched at source, all 38 md5 rows matched, every control fails at its stated sub-check, and an independent
symbol computation, S-bar^C = (r/2) B(dt - dr) and A_w + S-bar^C = (r/2) B(dt + dr) with B(zeta) = -2 iota_{zeta#} G C,
reproduces K1's and K2's spectra at both weights and dimensions. It found 10.21(b)'s r_* - r = -mu/r - mu^2/(3 r^3) +
..., the data weight, the weights and the n/2 shift right, and his Theorem 4.9(3) the even split the record uses.

*Four MINOR, repaired.* (1) Theorem 6.2(2) in five dimensions was stated "at that point and for C_0 <= 96, with h below
the h_0 of Theorem 5.2", but the roots are known at h = 10^-6 alone, and whether that lies below h_0(e) is not
certified. 10.21(e) now says (1) and the injectivity of (2) for every h in (0, h_0), the invertibility of (2) at h =
10^-6 provided it lies below h_0; 10.22(e), ROUTES 4.4, 4.22 and 4.23 and the paper ("its zero energy part at one
parameter point") say the same. The direct route needs C_0 <= 100; his C_0 + 4 (p. 67) serves his adjoint route, now
said, and the Theorem 1.1(2) analogue holds for C_0 <= 98; Theorem 5.2 is applied for C_0 + 1, also said. (2) The
Fredholm property of (6.1), on which index 0 gives invertibility, was used and not named: 10.21(d) now names it --
[Hin26c] Theorem 9.36 at n = 4 -- with box^C's threshold at the conormal bundle of the horizon below -C_0 - 1/2, not
computed here and OPEN in five dimensions (his Remark 5.7: the damping pushes it below any fixed number for small h).
(3) 10.20 used a wider reading of [Hin26c] than 10.19(d)'s: Lemma 3.11 and (3.47), Theorems 9.36-9.41 and Corollary 9.43
at n = 4 with alpha + 2, section 9.5 again for scalar operators. 10.20(e), the pointers in 10.15 and 10.16, ROUTES 4.21,
the paper and lowenergy5.py now say so. (4) Proposition 10.17(iii) called d_sigma^2 box(0) W* = 2 g00 W* computed; L3
types g00 (thresh5.py U4) and W*'s leading term (10.15) and computes their product, the identity d_sigma^2 = 2 g00 Id
being his Definition 9.4's: now labelled deduced, in 10.20 and lowenergy5.py.

*Twelve notes, seated.* (1) cpmodes5.py's docstring said D65: now D66. (2) Only (B.13)'s l-window is dimension-free; its
beta-range carries the density's shift ([Hin26] p. 137): "l-window" in 10.21, cpmodes5.py, ROUTES 4.5 and 4.22, the
README and the paper; the beta-range is taken up with Theorem B.1. (3) Checks that compared typed constants: K2's window
is now read off the computed spectra, each least eigenvalue shown below the others; K3's data weights are solved from
the integrability exponent; L2's top is read off the computed exponents; L3's shift is taken from its own computed
threshold; K3's top 2 and L3's rho^3 are typed from damping5.py U3 and 10.15(vi), where they are computed, and now say
so. (4) The lower end 0 of (0, 2) is READ (his Proposition 9.40, the adjoint condition), not computed: L2, the README
and ROUTES 4.21 now say so. (5) 10.20's setting called the augmentation "a functional at the horizon"; (6.24)'s row is
<., f*> with f* compactly supported and <W*, f*> = 1, the horizon functional entering through (6.26): repaired. (6)
10.21 credited 10.13 with the five-dimensional (5.14), which 10.13 deduces: repaired. (7) The constants C_0 + 1, C_0 + 4
and the Theorem 1.1(2) range: see (1). (8) 10.14's all-of-sf positivity was checked at (1, -102); 10.22's Q4 (D67)
checks it at 10.21's weights, at C_0 = 96 on all of sf and for every C_0 at the critical points. (9) ROUTES 4.4 called
[Hin26c]'s low-energy theory OPEN beside its deduction; D67 already replaced it by the line-by-line readings. (10) The
two t* conventions, t - r (L3, 10.18) and t - r_* (10.15(vi)), differ by O(mu/r) and move d_sigma box(0) W* only at
rho^5: said in 10.20 and lowenergy5.py. (11) lowenergy5.py's dead code removed. (12) The paper's [Hin26a] entry adds pp.
1-3 to its section 6 group, and its [Hin26c] entry (3.47) and Remark 9.42.

*Runs.* cpmodes5.py 3/3 and mutants 3/3, lowenergy5.py 3/3 and mutants 4/4, after the changes. The thirtieth verifier is
sent on 10.22 (solv5.py, D67) and these repairs.

**D69 (2026-10-22): [Hin26a] Theorem B.1 and [Hin26] Theorem 7.1(4) in five dimensions (tface5.py F1-F4; section
10.23).**

*The step.* With Theorem 5.2's inputs computed (10.22), the next piece of item 2 was his Appendix B, the transition face
problem on Minkowski space, from which [Hin26] Theorem 7.1(4) takes the tf-admissibility of box^C. READ at source
(alphaXiv): [Hin26a] pp. 85-88, 93-94, 96-98; [Hin26] pp. 136-137.

*Computed.* tface5.py F1-F4: (F1) box^C on 4+1 Minkowski in t* = t - r at the trace weight 2/3 is homogeneous of degree
-2, all 147 terms; (F2) the beta-range at the origin is (0, 2 + C_0], the density's shift n/2 = 2; (F3) at (1/2,
1/102400) the cf threshold alpha_cf > 1 - b*, bracketed at d = 0.9934 and 0.9935 in cform5.py's T, and -(1/2) r^2
l(dr/r) with characteristic polynomial (lam - v)^3 (lam^2 - (3 - e) v lam + (2 - e) v^2 - e) and positive eigenvalues;
(F4) section B.4's (alpha_sf, alpha_cf) = (-5/2, 5/2), the closing integral divergent, l = -1/2 in the l-window, beta =
7/2 for C_0 >= 3/2, (B.33)'s data shifts +1/2 and -1/2 from Omega's one time direction, and beta' = -beta + 2 - eps in
range iff beta in [-C_0, 2). 4/4, mutants 4/4, about 10 seconds; the four-dimensional controls reproduce his numbers.

*Deduced (10.23).* Proposition B.2 on the reading of 10.19-10.20, Theorem B.4 on 10.22's reading in its edge-b version,
Theorem B.1 on 4+1 Minkowski with beta in (0, 2 + C_0], and [Hin26] Theorem 7.1(4) with every beta in [-C_0, 2), at (v,
e) = (1/2, 1/102400), C_0 <= 100, and h = 10^-6 if that is below h_0. Nothing proved.

*Decisions.* (1) Hintz calls -(1/2) r^2 l(dr/r) positive definite with respect to Lemma 3.3's fiber inner product
because its eigenvalues are positive; the record computes the eigenvalues, deduces the rest as he does, and labels F3
so. (2) (B.33)'s data weights are not typed: their +1/2 and -1/2 are computed from the density in (tau, r), and are
dimension-free. (3) The closing integral is computed, not compared. (4) After a first passing run, F1's separate d_t*
sub-check, implied by the homogeneity, was replaced by a count of the d_t* terms, F3's threshold was bracketed directly,
F4's data shifts and closing integral were computed rather than typed, and the page of the Lemma 3.3 quotation corrected
to 96.

*Records.* 10.19-10.22's OPEN lists and ROUTES 4.4, 4.5, 4.22 and 4.23 point to 10.23 and 4.24; ROUTES 4.24; the README
(thirty-two programs); the paper's settling paragraph, review bullet, Appendices A, C and D, its [Hin26a] and [Hin26]
entries and the md5 table (40 rows).

*Next.* The thirtieth verifier's findings on 10.22 and D68 are seated when it reports, and the thirty-first is then sent
on 10.23 and tface5.py. Then [Hin26] sections 6.5, 7.2 and 8 in five dimensions.

**D70 (2026-10-22): the thirtieth verifier's findings on 10.22 and D68 (solv5.py; D67, D68), seated.**

*The verifier.* The thirtieth, on f0c106f: no MAJOR finding; four MINOR findings and thirteen notes. All three
instruments pass their selftests and mutants, every control fails at its stated sub-check, all 39 md5 rows matched; it
confirmed Q1's scaling at a rational point with the true r = |x|, Q4's thresholds to +-10^-3 and its positivity for C_0
in {0, 50, 96, 100, 200} with mpmath, and the D68 split (C_0 <= 100 direct, <= 98 for Theorem 1.1(2), (1) and
injectivity for every h < h_0, invertibility at 10^-6) at source.

*Four MINOR, repaired.* (1) "Every input ... is computed" overstated the labels: (4)-(5) off the critical points and the
smoothing of c (10.14(a)-(b)), Lemmas 3.3-3.8 (10.13(i)) and the uniformity Corollary 5.15 asks (p. 60) are deduced from
computed quantities. 10.22's setting and summary, ROUTES 4.4 and 4.23 and solv5.py's docstring now say "computed or
deduced from computed quantities"; 10.22(d) deduces the uniformity from (i) and c in rho_sf C^oo. The D67 entry's
"(4)-(5) holds ... for every C_0 >= 0" is superseded likewise (positive roots at the critical points for every C_0). (2)
His text was described as stated for general n where only Lemma 5.14 and Corollary 5.15 are (pp. 58-59); the rest of
section 5.2 is written in 3+1 (charts on S^2, p. 60; alpha_sf < -1/2 in Proposition 5.11, p. 54) and is to be read at n
= 4: 10.22's summary now says so. (3) The horizon-threshold caveat of D68 had not reached ROUTES 4.23 or 10.22's OPEN
list: added to both and to 4.23's OPEN line. (4) 10.21(d): the root statement dangled after a lower-case "its"
(repaired); Remark 5.7 concerns the spacetime estimate (5.21), so the threshold argument is now "by the mechanism of his
Remark 5.7, stated there for (5.21)"; his own Fredholm citations for (6.1), [HHV21, Theorem 4.3], [Vas21b, section 6],
[Vas18, Theorem 6.9] (p. 68), are named, with [Hin26c] Theorem 9.36 at n = 4 standing in their place; the condition is
written vartheta_H+ < -C_0 - 1/2, the threshold 1/2 + vartheta_H+ of 10.18's convention below -C_0; p. 44 added to
10.21's READ.

*Thirteen notes, seated.* (1) mu rho^2 runs to 4 at r = m: [0, 4] in 10.22(a) and solv5.py. (2) (10.49) is only
continuous at r_0/2 and 2 r_0; 10.22(a) now cites the smoothing (10.14(b), his p. 41) and r >= 3 r_0, and 10.23(a)
likewise. (3) Propositions 5.5-5.6 also use "only simple causal information" near tau = 0 and r = m (pp. 44-45), which
is 10.22(d): in the setting and (b). (4) delta_sf is not a continuity argument: C5 forces delta_sf > 0.0034, and (5)
holds there because T' at the sink does not depend on rho_K (C7; 10.14(iv)): in (c). (5) Q4's Sturm check now runs at
C_0 = 100, the largest C_0 10.21 uses (it held at 96; the verifier's corner minimum at 100 is 103.5). (6) [Hin23d]
replaced by his [Hin26d] section 3 (p. 19), the source he cites for the 3b-calculus. (7) The dimension also enters
through the trace weight 2/(D - 2); the thresholds are now compared at e = 0 (0 against his -1/2) and at e = 1/102400
separately, in 10.22 and in 10.23's summary. (8) solv5.py's Q1-Q4 labels now say what follows "so" is deduced, and Q2
computes the bound on all of tau in [0, T], r in [m, oo] (bound - G = T^2 (1 - s^2) + mu r^-2 (1 + T s)^2 at tau = T s),
not only its limit; the controls stay as they were, not vacuous, as the verifier found. (9) 10.21(b) now cites the e =
1/102400 thresholds (10.22(c), Q4). (10) h_0 = h_0(e, C_0), depending also on the weights, in 10.21(e), 10.22(e) and
ROUTES 4.23. (11) 10.20(e)'s "widened to (iii)" now reads "widened, for (iii), to". (12) Corollary 5.15 is on p. 59, not
60 as the D67 entry has it. (13) The README's mpmath sentence now covers every program importing those three.

*Runs.* solv5.py 4/4 and mutants 4/4 after the changes; response5.py all pass. Next: the thirty-first verifier on 10.23
(tface5.py, D69) and these repairs; and [Hin26] section 8 in five dimensions, its Lemma 8.4 first.

**D71 (2026-10-23): the thirty-first verifier's findings on 10.23, tface5.py, D69 and D70, seated.**

*The verifier.* The thirty-first, on 1012c7d (identical content at 8ccda3e): no MAJOR finding; eight MINOR findings and
seven notes. It confirmed the beta-range (0, 2 + C_0], the dimension-free +-1/2 shifts of (B.33), the cone-face
threshold as the translation of his (4.5), and, with [Hin26c] Theorem 9.38's general-n statement, F2's range and F4's
decay and threshold; it re-derived T's characteristic polynomial independently (b* = 0.993407313835418), read the D70
repairs at source, and found every md5 row current. Its first run stopped on a usage limit and resumed.

*Eight MINOR, repaired.* (1) "beta' in range for some eps > 0 iff beta in [-C_0, 2)" was false as an iff (beta < -C_0
passes with eps = -C_0 - beta): now "for every sufficiently small eps > 0", in 10.23 (iv) and (e), ROUTES 4.24 and
tface5.py, and F4 now tests the endpoints with symbolic eps and delta instead of typing the brackets. (2)
tf-admissibility has two halves ([Hin26c] Definition 5.10, p. 104; his p. 137); 10.23(e) now carries the adjoint half:
an element of the adjoint kernel, at the ztf weight -n + 2 + beta, is improved at ztf by [Hin26c] Theorem 9.38(5) and at
R_in to the decay 3/2 + S_in - eps, S_in = h^-1 (1 - e)(1 + v) from 10.21 K2, so lies where -l - 1 < -1/2 + S_in, the
l-window's lower end -- computed in F4. (3) The index 0 of Proposition B.2 is his relative index argument (p. 91), not
Theorem 9.38, whose part (3) gives only the independence of the weights; its numbers are now computed in a new F5: the
free 1-form operator's r-roots at the origin in five dimensions, -3, -2 | 0, 1 (l = 0), -l - 3, -l - 2, -l - 1 | l - 1,
l, l + 1 (scalar l >= 1), -l - 2 | l (vector), windows containing (-2, 0), crossing counts 2, 3, 1 equal to 10.12's; the
four-dimensional run reproduces his p. 91. 10.23(b) states the step, and pp. 89-91 are in the READ lists. (4) F3's
four-dimensional control was typed: T is now built from semiclass5.py for any n, and as e -> 0 (e symbolic, B being
singular at e = 0) the four-dimensional eigenvalues are 1 - 2d, 1/2 - d and 3/2 - d (twice), so d < 1/2, his alpha_cf >
1/2 ((4.7)); the five-dimensional are 2 - d (three times), 1 - d and 2 - 2d, so d < 1, 10.13's W3; at e = 1/102400 the
four-dimensional first zero is d = 0.4956, which F4 now uses. (5) Labels: F2-F5's docstrings say what follows "so" is
deduced; the README and the paper's Appendix A say tf-admissibility is deduced and that the sink threshold is 10.22's,
met. (6) Hypotheses: C_0 <= 100, the point and h = 10^-6 if below h_0 are now in the paper (settling sentence and
Appendix A), the README and ROUTES 4.4 and 4.5. (7) D70's supersession of "for every C_0 >= 0" now reaches ROUTES 4.23
("positive roots at the critical points for every C_0 >= 0"), solv5.py's Q4 label and the paper's Appendix A. (8) The
paper's thresholds now say "0 and 0 as e -> 0".

*Seven notes, seated.* (1) The quotation now reads "and is thus positive definite" (10.23, tface5.py). (2) 10.23(c)
cites cform5.py C7 for the half-line d < b*. (3) "The smaller root of q(d, 0)". (4) q(d, 0) is now derived from det T in
F3, not typed. (5) 10.23(a) now cites Proposition 10.9 directly, which is stated on 4+1 Minkowski. (6) Control coverage:
F3 adds the characteristic polynomial with n - 2 copies of v, F4 his top 1 claimed, F5 his window claimed; 7/7 caught.
(7) Small items: the 10.21(d) sentence restructured ("It is Fredholm by ... which stands here in place of his own
citations ..."); "only simple causal information" is attributed to Proposition 5.6's proof in 10.22 and its indentation
repaired; the paper's Appendix C row ends in ";"; verbose output prints decimals where it can. The label (10.23) of an
earlier equation shares its number with the section; it is cited elsewhere and stays.

*Runs.* tface5.py 5/5 and mutants 7/7, about 20 seconds; solv5.py 4/4; response5.py all pass. Next: [Hin26] Lemma 8.4 in
five dimensions (D72), its computations under way; the thirty-second verifier on 10.23's repairs and that section.

**D72 (2026-10-23): the thirty-second verifier's findings seated; [Hin26] Lemma 8.4 in five dimensions (10.24).**

*The verifier.* The thirty-second, on 3868a8e: no MAJOR finding; five MINOR findings and nine notes. It reran tface5.py
(5/5, mutants 7/7), solv5.py and response5.py and found the 40 md5 rows current; it recomputed F3's T and its limits,
F5's free roots by a Kelvin transform, and the adjoint half's S-tilde independently, from box^C's formal adjoint in the
incoming coordinate T = t + r: h^-1 {(1 - e)(1 + v), 2 (1 + v), 1 + v (n - 1 times)}, his p. 137 at n = 3 and 10.21
K2's at n = 4.

*Five MINOR, repaired.* (1) F4's "top 1" mutant was caught only by a typed top == n - 2, its endpoint equalities
carrying an offset that made them identities in the top: the offsets and the typed line are gone, and the mutant fails
at the endpoints, 1 - eps against -eps. (2) The adjoint half's S_in was typed where D71 called it computed: F4 now
computes S-tilde by the verifier's construction (s_tilde), asks the mixed coefficient -2 Id and no d_T^2 term, takes the
bottom of the spectrum, and a third control claims the other bottom h^-1 (1 - e)(1 - v); the dual weight -l - 1 is
labelled READ (his p. 137). (3) The paper's solv5.py bullet said "on all of the spatial face at C_0 = 100" where Q4
checks rho_K <= 10 (the verifier finds positivity lost near rho_K = 51.6): now "on the spatial face for rho_K <= 10 at
C_0 = 100". (4) D71's repair (6) said the proviso "h = 10^-6 if below h_0" was in the paper; it was not: the settling
sentence and Appendix A's tface5.py bullet now carry it. (5) 10.23's heading and Proof said F1-F4: now F1-F5 (D69, D71).

*Nine notes, seated.* (1) 10.23(b)'s hanging indent restored. (2) 10.23(b) says why [Hin26c] Theorem 9.38(3) does not
give the index: it makes the index independent of theta and of the weight, so with Corollary 9.39 it would give index 0
from tf-admissibility at theta = 0, which is what is being proved. (3) 10.23(b) adds the variable order l > -1/2 at R_in
and < -1/2 at R_out ([Hin26a] p. 91), which keeps the operator Fredholm as h^-1 -> 0, where (B.13)'s window empties. (4)
10.23(e) cites Corollary 9.39 (Definition 5.10 for every n) and the parenthetical to (9.115) (p. 195), the same
condition for every n, gives the five-dimensional density rho^-4 (p. 196), and records the verifier's comparison at ztf
(beta < 2 again) as not computed here. (5) "improved first at ztf by that theorem" now names the normal-operator
argument of its proof (p. 196). (6) F3's limit e -> 0 is a substitution, T's entries being polynomial in e: the
docstring and 10.23's Proof say so. (7) F5 now asks every root simple and found (multiplicities 1, as many as the
degree). (8) solv5.py's Q4 label: "every C_0 >= 0". (9) 10.23's Proof gives the 90 terms to the program; the READ lists
of 10.23, tface5.py and ROUTES 4.24 add [Hin26c] Theorem 9.38(3), its proof, Corollary 9.39 and Proposition 9.40; ROUTES
4.24's heading says D69, D71. The paper's hung4.py bullet regained its indentation.

*Lemma 8.4 (10.24; lin5.py E1-E5).* [Hin26] Lemma 8.4 lists the indicial roots of the linearized gauge-fixed Einstein
operator L by harmonic type, through those of box^Ups and box^C, and proves them by determinants computed in
Mathematica; Lemma 8.5 and Proposition 8.6 (tf-admissibility) rest on it. lin5.py builds L on 4+1 Minkowski from its
definitions (Cartesian, r an independent symbol, the harmonics of C^2 = R^4 with z^p a symbol so that l is symbolic) and
reads off the indicial matrices of r^2 L at a point. Computed: the types are preserved and his (8.5) holds at two points
(E1); det N_L = c (lam + l)(lam - l - 2) det N_Ups(lam - 1) det N_C(lam + 1) / D, every parameter symbolic, D = (lam -
1)^2 at s0 and s1, lam (lam - 2) at v1, 1 for l >= 2, and at the tensor type, which four dimensions lacks, det N_L = c
(lam + l)(lam - l - 2) (E2); his (1)-(5) recomputed in four dimensions (E3); the factors are gaugepot5.py's and
damping5.py's, and without damping the roots are integers outside (0, 2), as many on each side (E4); at the point (v,
e_C, gam_C, e_U, gam_U) = (1/2, 1/102400, 10^6, 1/100, 1/100), for l <= 12, the roots are simple, none has real part in
(0, 1], the types split 4 | 4, 6 | 6, 7 | 7, 2 | 2, 3 | 3, 1 | 1, box^C's nonpositive ones lie below -101, the least
positive real part is 1.000003, the greatest negative -3.3333 x 10^-7, the least distance from Z of a non-integer root's
real part (|lam| <= 50) 7.3846 x 10^-8, and 0 is a root at s0 and s2 only, its kernel annihilated by the gauge operator
(E5). Deduced for every l, with 10.12(i)'s box^Ups roots and Proposition 10.9's box^C roots: his Lemma 8.4 in five
dimensions, the gap beginning at 0 -- which 10.12 left "not computed here" -- and containing (0, 1]; Lemma 8.5; and
Proposition 8.6, both halves, on the readings of 10.19-10.23 but for the spectrum of his Lemma 8.2's S-bar_{E^Ups, E^C},
which the domain step of the kernel half needs. His cokernel argument says 3 roots are crossed at scalar type l >= 2
where his own list has 7 on each side, 3 being the 1-form count; the argument needs only that the two counts agree, and
10.24(d) says so.

*Three repairs inside the computation.* The first full run failed E1 at s0: N(lam) at the two points differed by the
ratio of r^2 there (25 against 9), the images carrying r^-2; every indicial matrix is now read off r^2 times the images,
which changes the determinants by constants only, and E1 passes. E5 now also reports the greatest negative real part
(the delta of his Proposition 8.6's proof) and the least distance from Z of a non-integer root's real part (his (8.13)).
The next run failed E4's comparison of det N_C with damping5.py's polynomials: the ratio is a power of gam_C alone,
damping5.py normalizing by powers of h = 1/gam_C, so the comparison now allows that power and nothing else (a helper
test: c gam_C^2 accepted, gam_C + 1 refused).

*Runs.* lin5.py 5/5 (about 50 minutes), mutants 4/4; tface5.py 5/5 (about 25 seconds), mutants 8/8; solv5.py 4/4;
response5.py all pass; md5 rows current. Next: the thirty-third verifier on 10.24, lin5.py and these repairs; then the
spectrum of S-bar_{E^Ups, E^C} (his Lemma 8.2) and (8.7) in five dimensions.

**D73 (2026-10-23): the thirty-third verifier's findings on 10.24, lin5.py and D72, seated.**

*The verifier.* The thirty-third, on 5795bd5: no MAJOR finding; five MINOR findings and seven notes. It reran lin5.py
(5/5; mutants 4/4), tface5.py (5/5; 8/8), solv5.py, response5.py, damping5.py and gaugepot5.py, found the 41 md5 rows
current, and recomputed the factorization by an independent construction -- a true r, other real harmonics, D Ric from
the linearized Christoffel symbols, the indicial matrices solved jointly at other points -- at s0-s3, v1-v3 and t2-t4,
symbolically where it could and at two random parameter points otherwise, with the stated D; the four-dimensional
control; E5's numbers from the full determinant, to every printed digit; and, from the factors, a scan to l <= 60 (no
root in (0, 1], even splits, the (8.13) distance 1.94 x 10^-8 at l = 50). It read every quotation of 10.24 at source,
and his "3" on p. 153 in the example after his Definition 2.30 (p. 67), the 1-form count.

*Five MINOR, repaired.* (1) Lemma 8.5 "for every parameter" overstated it: 0 is a simple root at s0 only if box^C has no
root at 1, which Proposition 10.9 gives at its point; 10.24(b) and its summary now say "for every z > 0 at Proposition
10.9's point". (2) 10.24(a) used, unstated, that box^Ups has no root in (-1, 0); it now says why, for every z > 0 and l
(at s0 (1 - (9 + 4z)^(1/2))/2 < -1; Q's negative roots solve lam (lam - 1) = s > l (l + 1) >= 2; the others are 1 - l
and -l). (3) The paper's Lemma 8.4 sentence dropped "at that point" and the factor at l <= 1: both restored; ROUTES 4.4,
4.5 and 4.25, the README and lin5.py's docstring now say "at the point" too. (4) "Coulomb root" was wrong at v1, where D
removes box^C's root 3 (its v1 roots are 3 and -1 - 2 v gam_C): lin5.py's docstring and the paper's lin5.py bullet now
say "2 (s0, s1) or 3 (v1)". (5) N(r^-1 delta_{E^Ups} G, 0) in 10.24(iv) is N(r delta_{E^Ups} G, 0), his N(rho^-1 ...)
with rho = 1/r; the code was right.

*Seven notes, seated.* (1) 10.24(c) states the five-dimensional improvement, (n - 1)/2 + S-bar - eps = 3/2 + min spec
S-bar - eps by [Hin26c] Theorem 9.38(5), his 1 - eps with (8.7), and (d) records that S-bar enters (8.17)'s Fredholm
setting only through admissible orders along the deformation, which any continuous S-bar allows, so (d) rests on the
readings. (2) Forward pointers: 10.12's "not computed here" and ROUTES 4.13's OPEN bullet now point to 10.24 and 4.25.
(3) The headings of 10.23 and ROUTES 4.24 add D72. (4) 10.23(iii) says the limit e -> 0 is a substitution. (5) The
equation label (10.24) shares its number with the new section, as (10.23) did; it is cited elsewhere and stays. (6)
lin5.py's "two generic points" is now "two points" (x_4 = 0 at one). (7) 10.24(a) names the closest pair at the point,
s1's physical 3 and box^Ups's 3 + z/12, 3.3 x 10^-7 apart; and 10.24(d) gives his "3" its source, p. 67.

*Runs.* lin5.py's changes are to its docstring only (its AST is unchanged, checked), so its 5/5 and 4/4 of D72 stand;
response5.py all pass; md5 rows current. Next: the spectrum of S-bar_{E^Ups, E^C} (his Lemma 8.2) and his (8.7) in
five dimensions, the one input Proposition 8.6 lacks.

**D74 (2026-10-23): [Hin26] Lemma 8.2's S-bar and (8.7) in five dimensions (10.25, sbar5.py).**

*M's words.* "Continue please", after PR #88 (D71-D73) merged; the branch restarted from main (b3ed5d0).

*What and why.* 10.24 left one input of [Hin26] Proposition 8.6 OPEN: the spectrum of S-bar_{E^Ups, E^C}, the
endomorphism by which 2 L-bar's d_t* terms differ from the wave operator's ((8.3b)), and his (8.7), min spec S-bar = 0,
with which his proof improves the decay at sctf to 1 - eps before the outgoing threshold (p. 152). His Lemma 8.2 (p.
146) gives S-bar as 1/2 rho^-1 times the d_t* coefficients of 2 E^C delta G + 2 (delta* + E^C) E^Ups G, with diagonal
2 (1 - v) gam_C, (1 - v) gam_C, (1 - e_C)(1 - v) gam_C, (1 - e_Ups) gam_Ups, gam_Ups, 0, 2 gam_Ups ((8.8)).

*Computed (sbar5.py S1-S3, exact).* On 4+1 Minkowski in t* = t - r: the wave operator is -2 d_t* rho (rho d_rho - 3/2)
plus a stationary operator; 2 L - box is first order with d_t* coefficient 2 rho S-bar, S-bar a constant 15 x 15 matrix
(the same characteristic polynomial at two points). Its spectrum is {0 (x5), gam_Ups (x3), 2 gam_Ups, (1 - e_Ups)
gam_Ups, (1 - v) gam_C (x3), 2 (1 - v) gam_C, (1 - e_C)(1 - v) gam_C}: the union of box^Ups's S-bar (10.18's) and
box^C's (10.21's), computed by the same construction, with five zeros; every eigenvalue >= 0, so min spec S-bar = 0, his
(8.7). The four-dimensional run gives his (8.8)'s seven values with multiplicities 1, 2, 1, 1, 2, 2, 1 in his order. And
the consequences: the improvement to 3/2 - eps (his 1 - eps), rho^(3/2 - eps) in rho^l L^2(r^3 dr) iff l < -1/2 - eps,
and (8.18a) beta_sctf < 3/2 (his 1).

*Deduced (10.25).* His (8.4) on Tangherlini, as 10.18 deduces (6.7); and the step of Proposition 8.6's kernel half that
10.24(c) left OPEN, so that Proposition 8.6 holds at Proposition 10.9's point for small gam_Ups on the readings of
10.19-10.24 alone.

*Two corrections inside the computation.* The first draft of S2 claimed the spectrum independent of the trace weight;
the run refused it: at the weight 1 in five dimensions the two eigenvalues (1 - e) gam become (3/2)(1 - e) gam, as
thresh5.py's control already records for box^Ups, and the minimum stays 0; S2 now checks that. And S2's incoming
control (t* = t + r) was described as giving a negative eigenvalue; it gives none -- its constraint part is gam_C {2 (1
+ v), (1 - e_C)(1 + v), 1 + v}, cpmodes5.py K2's spectrum at R_in -- and it is caught because the union fails; the
docstring and 10.25 say so.

*Runs.* sbar5.py 3/3 (about a minute), mutants 3/3; response5.py all pass; md5 rows current (42). Next: the
thirty-fourth verifier on 10.25, sbar5.py and the D73 repairs.

**D75 (2026-10-23): [Hin26] Proposition 8.3 in five dimensions, strong trapping admissibility of L (10.26, strap5.py).**

*M's words.* "Continue please", after PR #89 (D74) merged; the branch restarted from main (03650e6). The thirty-fourth
verifier, sent on D73-D74, is still reading.

*What and why.* His Proposition 8.3 (pp. 147-149) makes 2 L strongly trapping admissible for fixed modification
parameters (footnote 77: needed for b-regularity with a fixed loss). His proof writes i S_sub(2 L) = H_G + sigma A in the
frame of (6.16b) and the splitting (8.11), prints the 10 x 10 A, triangularizes it in (8.12) with eigenvalues 0 (6x),
-2 (1 - e_C) gam c_2, -2 gam c_2 (2x), -4 gam c_2, all >= 0 because c_2 = -g^-1(c_C, e_0) < 0, and weights (8.12) by
powers of eta. 10.17 had carried the frame to five-dimensional Tangherlini (his Lemma 6.4).

*Computed (strap5.py P1-P3, exact).* On an abstract quasi-orthonormal frame: with his sign the computed A equals his
printed matrix in all 100 entries, triangular in his (8.12) with his diagonal (P1); in five dimensions det(lam - A) =
lam^10 (lam + 2 gam c_2)^3 (lam + 4 gam c_2)(lam + 2 (1 - e_C) gam c_2) -- 3 (1 - e_C) at the trace weight 1 -- and a
constant basis triangularizes A for every c (P2); with c's angular part zero, A commutes with the rotation of the angular
plane, and in rotation-adapted units it is block triangular with scalar blocks, the rotation skew within each unit (P3).

*Deduced (10.26).* His Proposition 8.3 on five-dimensional Tangherlini: 10.14's c = a(r) dt + b(r) dr has no angular
part and is past timelike at the photon sphere, so c_2 < 0 and the blocks are >= 0; the inner product weights the
angular pairs alike, so the rotation of the plane along the flow -- the one point four dimensions lacks -- stays skew.

*Three corrections inside the computation.* The first run of P2 compared characteristic polynomials built on two
symbols named lam with different assumptions (charpoly's generator carries none), so equal polynomials compared
unequal: lam is now plain. The draft claimed the spectrum the same at the trace weight 1; the run refused it -- the
last eigenvalue becomes -3 (1 - e_C) gam c_2, as sbar5.py found for S-bar -- and P2 now checks both. P3's eta-rescaling
was written W A W^-1 where the orthonormal coordinates give W^-1 A W; fixed. And the paper's new sentence counted four
nonzero eigenvalues where there are five.

*Runs.* strap5.py 3/3 (a few seconds), mutants 3/3, each control failing for its stated reason (8 entries differ at
the computed sign; A not triangular with e_1^2 moved; A not commuting with the rotation at c_4 = 1/3); response5.py
all pass; md5 rows current (43). Next: the thirty-fourth verifier's findings on D73-D74 when it reports, then the
thirty-fifth on D75; his sections 8.4-8.5 in five dimensions.

**D76 (2026-10-23): the thirty-fourth verifier's findings on 10.25, sbar5.py, D73 and D74, seated.**

*M's words.* "Continue please", after PR #90 (D75) merged; the branch restarted from main (8d51f67).

*The verifier.* The thirty-fourth, on 49c0f00: no MAJOR finding; four MINOR findings and eight notes. It reran sbar5.py
(3/3; mutants 3/3) and response5.py (all pass), found the 42 md5 rows current, and recomputed S-bar by a route that
shares no code with sbar5.py: by hand from principal symbols, S-bar = rho^-1 [E^C sigma_delta(dt*) G + sigma_delta*(dt*)
E^Ups G], in his null splitting (5.27) at a point -- at n = 3 his (5.28) at h = 0 entry for entry, (8.8) with its
starred entries; at n = 4 lower triangular with sbar5.py's spectrum; at the trace weight 1 only the two (1 - e) entries
scaled by 3/2; and the 1-form S-bars equal to thresh5.py U2, cpmodes5.py K1 and his (7.5). It gave the union its reason:
S-bar = XY with X = [E^C | sigma_delta*] and Y = [rho^-1 sigma_delta G; rho^-1 E^Ups G], and YX is block triangular with
diagonal blocks S-bar^C and S-bar^Ups because sigma_delta G sigma_delta*(xi) = -|xi|^2/2 vanishes at the null dt*,
whence (n + 1)(n + 2)/2 - 2 (n + 1) zeros at every trace weight. It read [Hin26c] Theorem 9.38(2), (5) and Proposition
9.40 at source (arXiv:2606.28008v1, pp. 195, 197), and checked each D73 repair against the thirty-third verifier's list.

*Four MINOR, repaired.* (1) (8.8)'s multiplicities were misstated as 2, 2, 1, 1, 2, 1, 1; in his order they are 1, 2, 1,
1, 2, 2, 1, the ranks of the summands of his splitting (5.27). 10.25, sbar5.py's docstring and D74 above are corrected
in place, and S2 now compares the n = 3 spectrum with his seven values at those ranks in his order, which the
set-and-sorted comparison could not see. (2) ROUTES 4.5's "Next" named sections 8.3-8.5; D75 had already rewritten it to
6.5, 7.2, 8.4 and 8.5, right now that Proposition 8.3 is deduced in 4.27. (3) The paper's S-bar sentence reads "that it
needs", and its label is now "the spectrum computed, the improvement deduced". (4) Proposition 8.6 now carries both
hypotheses, Proposition 10.9's point and small gam_Ups, in the README, the paper's lin5.py and sbar5.py bullets, ROUTES
4.4 and 4.5, and the summaries of 10.24 and 10.25.

*Eight notes.* (1) The hanging indents of 10.24(b) and of ROUTES 4.13's OPEN bullet are restored. (2) The headings of
10.25 and ROUTES 4.26 add D76; those of 10.24 and ROUTES 4.25 would pass 121 characters with D73, D74 and D76, so they
stay and this LOG records the edits. (3) The paper's sbar5.py bullet says "the diagonal of his (8.8)", which is what S2
recomputes. (4) The READ ranges begin at p. 144, where section 8 fixes c_Ups = r^-1 dt and gam_Ups << 1. (5) 10.25(b)
now cites what his proof cites, [Hin26c] Theorem 9.38(5)'s parenthetical, the domain inclusion itself, under part (2)'s
threshold -1/2 + S-bar, here -1/2; (iii) is the cross-check. (6) The operator of that step, with the unmodified
symmetric gradient, has minimum 0 as well: the verifier computed {0 (ten times), gam_Ups (three times), 2 gam_Ups, (1 -
e_Ups) gam_Ups}, and S2 now checks it at gam_C = 0, which 10.25(ii) states. (7) 10.24(d) and its summary no longer read
as OPEN and computed at once. (8) 10.17's "Proposition 8.3 (p. 149)" is p. 147.

*Runs.* sbar5.py 3/3 (about a minute), mutants 3/3, the new checks refusing the misstated ranks; response5.py all pass;
md5 rows current. Next: the thirty-fifth verifier on 10.26, strap5.py, D75 and these repairs; and [Hin26] section 8.4,
his Proposition 8.8, in five dimensions.

**D77 (2026-10-23): the thirty-fifth verifier's findings on 10.26, strap5.py, D75 and D76, seated.**

*The verifier.* The thirty-fifth, on cca4070: no MAJOR finding; three MINOR findings and eight notes, all in the
records. It reran strap5.py (3/3; mutants 3/3), sbar5.py and response5.py, found the 43 md5 rows current, and recomputed
A by a route that shares no code with strap5.py: on concrete static Schwarzschild (r = 3M) and Tangherlini (r^2 = 2 mu),
along an equatorial circular null orbit, nabla_{H_G} from the Christoffel symbols along X = 2 zeta^#, E^C sigma_1(i
delta) G in coordinates with iota_{zeta^#}, in 10.17(iii)'s frame -- the connection matrix -2 sigma, 10.17's sign, in
both dimensions; the characteristic polynomials of P2, with 3 (1 - e) at the weight 1 and -3 m (1 - e) gam c_2 at the
symbolic weight m; P2's basis and P3's units holding with its A, and their controls failing; and, with 10.14's c at r^2
= 2, G(c) = -39/1280000, <c, dt> = -1/100, c_2 = -1/200 < 0. It read [Hin26] pp. 34, 113, 115-116, 144-149 and 152, and
[Hin26c] Definition 5.8 (pp. 102-103), Theorem 9.38 (p. 195) and Lemma 4.14 (p. 88) at source, and checked each D76
repair, patching S2 to the misstated ranks to see it fail.

*Three MINOR, repaired.* (1) ROUTES 4.25 and 4.26 still listed his Proposition 8.3 as OPEN; both now point to 4.27,
where it is deduced. (2) The paper's record of verifiers stopped at the thirty-third: its section 8 paragraph and
Appendix C's verification row now carry the thirty-fourth and thirty-fifth, and Appendix C's range reads D1-D77. (3) The
README's lin5.py bullet now carries "for small gam_Ups" on Proposition 8.6.

*Eight notes, seated.* (a) The sign: 10.17's s = -2 is his +2 read in the frame with e_1 -> -e_1 (and so c_1 -> -c_1);
P1 now checks it -- after that change of frame the computed A equals his printed matrix in all 100 entries -- and
10.26(i), its proof, ROUTES 4.27, the README and the paper say so. (b) P1 now compares the diagonal in his order, not
sorted. (c) P3's control breaks the commutation and the block triangularity both (five entries below the unit blocks,
recounted here); the docstring and 10.26 name both. (d) The paper's "reproduced" now says "with his sign convention".
(e) 10.26(a)'s degree 0 comes from the normalization by C^(1/2), H_G C = 0 keeping the connection matrix unchanged under
it. (f) iota_{e_2} is his notation, the contraction with the vector e^2 of the dual frame; the docstring and 10.26 say
so. (g) gam > 0 has its clause: sigma > 0 on the future characteristic set, d_t being timelike outside the horizon
([Hin26c] Lemma 4.14, (4.41)). (h) 10.26(iii) states the angular pair's normalization: in his 2 e_3 (x)_s e_4 the
rotation acts on (e_3 e_4, e_3^2 - e_4^2) as [[0, 2], [-2, 0]], both members of norm^2 2.

*Runs.* strap5.py 3/3 (a few seconds), mutants 3/3; response5.py all pass; md5 rows current. Next: [Hin26] section 8.4,
his Proposition 8.8 in five dimensions (D78), and a thirty-sixth verifier on these repairs with it.

**D78 (2026-10-23): [Hin26] Proposition 8.8 in five dimensions, mode stability (10.27, gmodes5.py).**

*What and why.* [Hin26] section 8.4 opens with Proposition 8.8, mode stability of L-hat(sigma) at 0 != sigma, Im
sigma >= 0. His proof (pp. 153-154) takes his Theorem 7.1(1), his Proposition 6.12 and [AHW24] Theorem 6.1(1): every
outgoing mode of D Ric is pure gauge, on Kerr through the Teukolsky equation. The first two are in five dimensions
already (10.21(e), 10.20(e)); the third was not. On Tangherlini the Kodama-Ishibashi decomposition [KI03] (read for
10.3, and now at its sections 2, 3 and 5 and Appendices A-B) reduces each harmonic type to one master equation, and
gmodes5.py computes that reduction from D Ric at n = 3.

*Computed (gmodes5.py G1-G5, exact).* A harmonic enters through its Taylor jets at a point of S^3 with rational sines,
every jet free but for its defining equations and their derivatives -- every harmonic of the type at once, the
isometries carrying the point anywhere. (G1) D Ric annihilates delta* omega for arbitrary jets; the tensor type gives
[KI03] (5.3) and V_T = (f/r^2)(l (l + 2) + 3/4 + 9 mu/(4 r^2)), 10.16's scalar wave potential. (G2) The vector type:
delta*(r^2 B V) shifts f_a by (r/2) D_a B and H_T by -k_V B/2; in H_T = 0, E_T = -(k_V/(2 r^3)) D_a(r^2 F^a), and Omega
= r^2 F^r/(i sigma) turns E_a = 0 into the master equation with V_V = (f/r^2)(l (l + 2) + 3/4 - 27 mu/(4 r^2)). (G3) The
scalar type: [KI03]'s gauge 1-form, -2 X_a S dy^a - (2 r^2/k) H_T S_i dz^i, leaves their F, F_ab; the seven reduced
equations; at sigma != 0, E_t, E_r and E_tr give exactly their (2.24a-c) with Z = i sigma Z~ (the other sign fails all
three), the remaining three one constraint that the flow preserves, their Phi (3.1) solving (3.5) with Q of (3.7), and
det[Phi; Phi'; C] = -r^4 (r^2 - mu)^5. (G4) l <= 1 at sigma != 0, pure gauge: scalar l = 0 by the algebraic gauge f_tt =
H_L = 0; vector l = 1 by E_r = r^2 d_t F^(1)/(2 (r^2 - mu)); scalar l = 1 by the algebraic gauge f_tt = f_t = H_L = 0,
determinant (r^2 - mu)(sigma^2 r^4 - mu)/(4 r^6); the eliminations over Q(3^(1/2), i)(r, sigma) at mu = 1 by the
homothety, every pivot's factors free of r powers of sigma. (G5) The potentials positive at l >= 2, Q >= 16 m (m - 3)(m
+ 9) for 3 < m <= 12 and Q >= 16 m^3 + 60 m^2 for m >= 12 (corrected in D79); in ingoing coordinates Gamma^lam_rr = 0,
and the master fields free of 1/f.

*Deduced (10.27).* (a) [AHW24] Theorem 6.1(1) on five-dimensional Tangherlini, in the class of 10.16: each master
equation as in 10.16(a); the gauge 1-forms in the class -- covariant on the orbit space at l >= 2, algebraic at l <= 1
with the sphere sigma^2 r^4 = mu removable, smooth across the horizon by the ingoing r-row ODE. (b) His Proposition 8.8
there, on the readings of 10.19-10.26, at Proposition 10.9's point with gam_Ups small; the kernel elements' class and
the interior uniqueness OPEN, as in 10.16.

*Notes on the computation.* (1) Zero tests by expand left the 1/f fractions uncombined, so D Ric(delta* omega) = 0 and
the vector match failed at first; every comparison now cancels. (2) The l = 1 elimination by rref took sixteen minutes
and divided silently by its pivots; it now runs over a fraction field at mu = 1, in about two minutes, every pivot kept,
and the factors free of r are powers of sigma. (3) The reverse direction of the scalar type -- that [KI03] (3.14)
carries every master solution to a solution -- ran for over half an hour unfinished and is not needed for uniqueness;
what is computed is the direction the argument uses, from the equations to the master equation, with Phi = 0 forcing the
invariants to vanish. (4) The master fields are built from static components, which carry 1/f at the horizon; written in
ingoing components they are free of it (G5), which is what puts them in 10.16's class.

*Runs.* gmodes5.py 5/5 (about five minutes), mutants 5/5; response5.py all pass; md5 rows current (44). Next: the
thirty-sixth verifier on 10.27, gmodes5.py, D77 and D78.

**D79 (2026-10-23): the thirty-sixth verifier's findings on 10.27, gmodes5.py, D77 and D78, seated.**

The thirty-sixth verifier read d47dbd0 read-only, every program run from an archive of it, and recomputed independently:
its own D Ric (equal to d/d eps Ric(g + eps h), annihilating d_mu g and delta* omega, agreeing with the record's dric in
all 25 components at the point), explicit harmonics (a TT tensor from two self-dual Killing forms, k_T^2 = 6; co-closed
vectors at l = 2 and 3; zonal scalars at l = 2 and 3; cos chi and a Killing field at l = 1) and the exceptional ranks at
numeric points, complex sigma among them. Verdict: D78 holds; no major finding; five minor findings and eight notes,
each seated here.

*Minor.* (1) Q >= 16 m (m - 3)(m + 9) is false for m > 12 (l >= 4): at x = 0 Q = 16 m^3 + 60 m^2, below the bound there;
at m = 21 Q's minimum on [0, 1] is 174636 against 181440. Q > 0 held by the code's own case split. Repaired in 10.27(v)
and in gmodes5.py's G5, docstring and check, which now verifies both branches -- Q - 16 m (m - 3)(m + 9) = 1296 x^3 +
(624 m - 144) x^2 + 36 m (12 - m)(1 - x) on 3 < m <= 12, every coefficient of Q(12 + p, x) nonnegative for p >= 0 -- and
records the failure at m = 21; D78's entry corrected in place. (2) The paper's Appendix C range stood at D77: now D79.
(3) ROUTES 4.25-4.27's OPEN lists did not point to 4.28: each now names his Proposition 8.8 deduced there. (4) The paper
stated Proposition 8.8 without its class and open items: it now says smooth across the horizon and outgoing at infinity,
deduced on the same readings, the kernel elements' class and the uniqueness inside the horizon open. (5) The paper's
[KI03] and [Hin26] entries lacked the reads of 2026-10-23: added ([KI03] sections 2, 3 and 5 and Appendices A-B; [Hin26]
pp. 25, 28, 34, 113-117, 135-137, 144-154).

*Notes.* (a) His Proposition 6.12 is a statement on all of X: omega must be continued into the part of X inside the
horizon as a solution of box^Ups(sigma) omega = 0 before it applies; 10.27(b), 10.27's OPEN list and ROUTES 4.28 now say
so, the continuation OPEN. (b) h_0 and the size of gam_Ups added to 10.27's and 4.28's OPEN lists. (c) gmodes5.py's
docstring and a comment had f_tt shifting by 2 (d_t A_t - Gamma^r_tt A_r); the code and the verifier's computation give
no factor 2: corrected. (d) E_T is not printed in [KI03]; their (5.12) implies it: the attribution corrected. (e) G4's
vector l = 1 label claimed f_a = (r/2) D_a B unchecked: the check now runs, on a mode with F^(1) = 0 and B = 2 i
f_t/(sigma r). (f) The determinant's value depends on C's normalization (the verifier's E_rr form gives -r^3):
10.27(iii) and the docstring now name the rows, r^(1/2) Phi, r^(1/2) Phi' and C as G3 normalizes it, a multiple of C by
a function of r rescaling the determinant by that function. (g) At scalar l = 1 the jets stop at order 2 with the
constraints at order 0; S's third jet enters D Ric only through nabla^j (nabla_j nabla_i - nabla_i nabla_j) S = 0, and
the verifier's order-3 jets gave identical reduced equations: said in the docstring and the proof. (h) The alphaXiv
extraction drops minus signs; (2.23)'s Z = i sigma Z~ was settled by (A.1b) through (2.22a), (2.24c), (3.9c) and (3.12c)
and by computation: 10.27's READ says so.

*Not checked by the verifier.* [AHW24] itself, read through Hintz; [KI03]'s minus-sign glyphs; the OPEN items; l >= 4
with explicit harmonics, which the record's general-k jets carry.

*Runs.* gmodes5.py 5/5, mutants 5/5; response5.py all pass; md5 rows current (44). The headings of 10.27 and 4.28 keep
D78 alone, D79 added there exceeding 121 characters. Next: [Hin26] section 6.5.1 and Proposition 8.9 in five dimensions
(D80).

**D80 (2026-10-23): [Hin26] section 6.5.1 and Proposition 8.9 in five dimensions (10.28, zstates5.py).**

M's commission (522) continues: route B item 2 carried to five dimensions step by step. After Proposition 8.8 (D78) the
next step of his section 8.4 is the zero energy theory, which rests on section 6.5.1's states built from the Minkowskian
symmetries and on Proposition 8.9's gauged linearized Kerr metrics. READ at source (alphaXiv, 2026-10-23): [Hin26] pp.
25, 81 (Definition 4.1), 124-128 (Lemma 6.13, section 6.5.1; 124-127 until D82), 154-155 (Propositions 8.8-8.9, Remark
8.10).

*Computed (Proposition 10.25, zstates5.py Z1-Z5).* (Z1) g - gbar in rho^2, Gamma in rho^3, r* without a logarithm. (Z2)
delta*_g dx^1 at rho^3, box dx^1 at rho^4; 2 an s1 root only at z = 0, the root through 2 (1 + (17 + 2z - 2 (z^2 + 4z +
16)^(1/2))^(1/2))/2 > 2 for z > 0. (Z3) The boost's stationary defect K at rho^2; 1 no s1 root. (Z4) R Killing, g
gbar^-1 R = R; V_1 = so(4). (Z5) d_mu g and h_A vacuum, at rho^2 and rho^3; eta_mu at rho^3; delta G h_A = 0 and eta_A =
E^Ups h_A = (2 gam mu/(f r^5)) w at rho^4; 1 no s0 root, 2 no v1 root. Controls: the four-dimensional orders; z = 0;
four-dimensional Schwarzschild's K at rho; f R; four-dimensional d_M g at rho.

*Deduced (10.28).* (a) His Proposition 6.15 in five dimensions, every order raised by one and no logarithm at the
boosts, h_v1 = 0. (b) His Proposition 8.9 there, no logarithm at the mass, g-dot^Ups(mu) at rho^2 and g-dot^Ups(A) at
rho^3, six angular momenta. Both on his Lemma 6.13 in five dimensions, OPEN since 10.20.

*Notes on the computation.* (1) The first draft read orders by simplify and as_leading_term along the ray and ran for
over ten minutes on one Christoffel table; every component along a ray is rational in R, so the order is now a
difference of degrees, exact. (2) A ray along (1, 1, 1, 1)/2, on which x^1 - x^2 vanishes identically, was replaced
before the first full run by the generic (2, 4, 5, 6)/9. (3) The symbolic inverse of the 5 x 5 Cartesian metric did not
finish in ten minutes; the inverse is now written out, delta_ij - mu x_i x_j/r^4, and checked against g. (4) D Ric of
h_A in Cartesian coordinates ran for over twenty minutes unfinished; in polar coordinates it takes under a second, and
Z2 moved there too (from four minutes), the orders read on gbar's orthonormal frame. (5) The draft gave the s1 root
through 2 as (1 + (9 + z)^(1/2))/2: the run refuted it, and the root is now solved exactly. (6) The draft's Z4 control,
the gbar-dual of R, was vacuous -- R is orthogonal to x, so its g- and gbar-duals agree -- and the selftest flagged it;
the control is now f R. (7) The draft's Z3 control was forced to fail; it now computes four-dimensional Schwarzschild's
K, of order rho, against the five-dimensional claim. (8) The rotation's gauge source was first written as an assumption;
it is now computed with 10.15's E^Ups at the trace weight 2/3.

*Also repaired.* D79's reflow doubled the marker ('- - ') of six bullets whose first line it rewrapped: ROUTES-OPEN.md
4.25-4.28's OPEN bullets and the paper's [KI03] and [Hin26] entries. Repaired; the reflow now keeps a bullet's own
marker.

*Runs.* zstates5.py 5/5 (about 15 seconds), mutants 5/5; response5.py all pass; md5 rows current (45). Next: the
thirty-seventh verifier on 10.28, zstates5.py, D79 and D80.

**D81 (2026-10-23): [Hin26] Lemma 6.13 and Proposition 6.18 (1)-(3) in five dimensions (10.29, genstates5.py).**

M asked to continue. 10.28 deduced section 6.5.1 and Proposition 8.9 in five dimensions on his Lemma 6.13 there, OPEN;
the next step of item 2 is that lemma and his section 6.5.2. READ at source (alphaXiv, 2026-10-23): [Hin26] pp. 51-52
(Lemmas 2.13 and 2.15), 64-67 (Definition 2.28, (2.37b), Lemma 2.29, (2.43)-(2.46)), 81, 113, 117-119, 121, 124-125
(Lemma 6.13), 128-134 (Proposition 6.18, Remark 6.19 and the proof; 129-134 until D83).

*Computed (Proposition 10.26, genstates5.py H1-H5).* (H1) Part (1) on Minkowski: W = r(-dt + b dr), b = (2 - e_U)/(4
e_U), h-bar^(0)_s0 = (2 - 5 e_U, -(2 + 3 e_U), 2 - 5 e_U, 4 (2 - e_U))/(16 e_U); on Tangherlini the source at rho^1 and
rho^3, nothing at rho^2 (Schwarzschild: (2M, 2M (2 gam_U + 1)) there). (H2) Part (2): W at rho^-2, (alpha, beta, kappa)
= (4 - 7 e_U, -(4 + 17 e_U), (2/3)(25 e_U - 4))/(24 e_U), h-bar^2_s1 stationary and nonzero. (H3) Part (3): kappa = 1 +
2 gam_U/5, h-bar^1_v1 = (1/4)(1 +- 2 gam_U/5). (H4) His printed (0, -1/4, -1/2, 0), (0, 0, 0, -1, 1/2, 0), kappa = 1 +
gam_U/2 and (6.40) reproduced in four dimensions. (H5) lam_s1,2 = 2 + z/12 + O(z^2) < lam_s0 = 2 + z/3 + O(z^2) for
every z > 0 (0 < z < 4 until D83). Controls: the five-dimensional claim on Schwarzschild; the factor 2 on B dropped; his
kappa in five dimensions; the five-dimensional kappa in four; z = 0.

*Deduced (10.29).* (a) His Lemma 6.13 in five dimensions on 10.20's readings, every correction of 10.28 inside the gap,
so 10.28's deductions no longer rest on an OPEN input. (b) His Proposition 6.18 (1)-(3) there: part (1) without his
logarithm, part (2) with its corrections at rho^-k, part (3) with six states at a = 0.

*Notes on the computation.* (1) The first test of h-bar^2_s1's stationarity compared unsimplified t-derivatives with 0
and reported False; with an exact zero test it holds -- the boost's t-terms cancel, as his Killing argument says. (2)
The coefficients of parts (1) and (2) carry 1/e_U, in four dimensions as in five: at e_U = 0, -1 (s0) and -2 (s1) are
roots of box^Ups(0), the coincidences his e_Ups > 0 removes (p. 81). (3) His splitting (2.37b) was READ before the
controls were written; with it his three printed vectors and (6.40) come out exactly, which fixes the convention the
five-dimensional numbers are stated in.

*Runs.* genstates5.py 5/5 (about a minute), mutants 5/5; response5.py all pass; md5 rows current (46). Next: the
thirty-seventh verifier's report on D79-D80, then one verifier on 10.29.

**D82 (2026-10-23): the thirty-seventh verifier's findings on 10.28, zstates5.py, D79 and D80, seated.**

The thirty-seventh verifier read 6ee0a75 (and 73c552e) read-only, every program run from an archive, and recomputed
independently: the five-dimensional indicial roots of box^Ups(0) in Cartesian coordinates without Christoffel symbols
(his Lemma 6.6 reproduced as the control), Z2-Z5 with symbolic angles (delta* by the Lie derivative, delta by the
density formula, D Ric as d/d eps Ric(g + eps h)), the boost terms of 10.28(a) with his Minkowski model, and the
one-spin Myers-Perry metric. Verdict: D80 holds; no major finding; four minor findings and eight notes, each seated
here.

*Minor.* (1) The READ ranges stopped at p. 127, while 10.28(a) uses p. 128 (the origin of (6.31)'s logarithm, f-breve's
type, h-breve^1, (6.35)), and Lemma 8.12 is on p. 157: 10.28's READ, zstates5.py's docstring, ROUTES 4.29 and D80's
entry (corrected in place) now read 124-128, with p. 157 read and recorded. (2) His section 8.4 numbers 8.10 a Remark,
8.12 a Lemma and 8.13 a Corollary: "Propositions 8.10-8.13" (10.28, 10.29, ROUTES 4.29 and 4.30), "Propositions
8.9-8.11" (10.27, ROUTES 4.28) and "Proposition 8.10 on" (ROUTES 4.5) corrected. (3) zstates5.py's line of 122
characters wrapped. (4) The paper's [Hin26] entry now records the reads of 2026-10-23 for sections 6.5 and 8.4.

*Notes.* (a) The Myers-Perry identification is computed now rather than left unREAD: Z6 types [ER08] (32)-(33) at d = 5,
READ at source, and finds Ric = 0 at three exact points, Tangherlini at a = 0 and d_a g at a = 0 = -h_A; 10.28(vi), (b)
and its OPEN list, ROUTES 4.29 and the paper, with [ER08] added to its references, say so. (b) 10.28(i)'s consequence
for his Lemma 6.14 is labelled deduced; (a)'s first and last boost terms now rest on (iii)'s computed residual, not on
(i). (c) His boost uses t-bar = t* + r: Z3 now computes, in retarded coordinates, K-bar of order rho^2 and the
stationary residual box^Ups_g B-bar - t* box^Ups_g dx^1 of order rho^3 (four dimensions rho, rho^2), B-bar Killing for
gbar. (d) The README and zstates5.py's docstring now cite Lemma 6.13 as deduced in 10.29. (e) Z5's root claims are the
polynomials' values, 2 (2 + z) and 3. (f) Z4 checks all six rotations and computes the ranks 6 and 4. (g) pp. 113 and
117 added to 10.28's and 4.29's READ. (h) Z1-Z3 and Z5 read every order at a second ray or angle as well.

*Notes on the computation.* (1) Z3's Killing test for B-bar first compared unsimplified entries with 0 and failed; they
vanish once sin^2 + cos^2 is reduced. (2) Z4's first rank of S_1 took derivatives at points where x^i/r is degenerate
and returned 0; it is now the rank of the four functions' values at four points.

*Not checked by the verifier.* The index sets; Lemma 6.13 in five dimensions (OPEN at 6ee0a75, deduced in 10.29 since);
pages outside those it read; minus-sign glyphs in the extraction.

*Runs.* zstates5.py 6/6 (about half a minute), mutants 6/6; genstates5.py 5/5; response5.py all pass; md5 rows current
(46). Next: one verifier on 10.29, genstates5.py, D81 and D82.

**D83 (2026-10-23): the thirty-eighth verifier's findings on 10.29, genstates5.py, D81 and D82, seated.**

The thirty-eighth verifier read fb25218 (and 967d52c) read-only, every program run from an archive, and recomputed
independently: parts (1)-(3) on 4+1 and 3+1 Minkowski in Cartesian coordinates without Christoffel symbols, the
coefficients solved at six points; the Tangherlini source by the density formula along two rays, with box_g(t* omega_s0
+ W) starting at rho^3 where four dimensions has a rho^2 term; the indicial polynomials from scratch, his Lemma 6.6 as
the control; Z3 with the Lie derivative; and Z6's Ricci tensor identically in cos theta. Verdict: D81 and D82 hold; no
major finding; five minor findings and notes, each seated here.

*Minor.* (1) "-k is no root for z > 0" held for small z only: the s0 polynomial vanishes at -2, -3 and -4 when z = 4, 10
and 18, the s1 polynomial at -3 and -4 when z = 20/3 and 252/17. 10.29(i), (ii) and (b) and genstates5.py's H1-H2 now
say 0 < z < 4 and 0 < z < 20/3 (-1 at s0 and -2 at s1 for every z > 0), computed exactly as the least positive zero in z
of 10.15(i)'s polynomial at each value, with z = 4 and z = 20/3 as new controls. (2) The five-dimensional Lemma 6.13 was
cited without "on the readings of 10.20" in the paper's settling paragraph, the README's two bullets, ROUTES 4.4, 4.5
and 4.29's OPEN list, and genstates5.py's docstring; each now carries it, and 10.28(a)'s "(OPEN since 10.20)" reads
"(deduced in 10.29 on the readings of 10.20)". (3) 10.29(a) passed from injectivity at the shifted weights in (0, 1)
(10.20(e)) to every weight of the gap without saying how; it now says it -- a kernel element at one weight of the gap is
polyhomogeneous by his Lemma 2.13 with exponents above the gap, so lies in every weighted space of it -- with his "and
thus has trivial nullspace on A^eps(X; T*X) for all eps > 0" (p. 121), READ at source. (4) "omega-breve^(0),1_s0 =
rho^-1 W + ..." in 10.29(b) and genstates5.py's H1 counted W's factor r twice; it reads W + .... (5) 10.29(a)'s "at
rho^2 for the translations and the rotations" now names the rotating metrics, the rotations needing none at a = 0; and
"10.12(i)" there and in genstates5.py, Proposition 10.12(i) of section 10.15, now reads 10.15(i), as zstates5.py and
10.20 write it.

*Notes.* (a) H4 now asserts the four-dimensional b = (2 - e_U)/(3 e_U) and (alpha, beta, kappa) = (2 - 3 e_U, -(2 + 7
e_U), 2 (4 e_U - 1))/(10 e_U) that 10.29(iv) prints. (b) (6.40) is printed on p. 130 and re-derived on p. 134; 10.29(iv)
and H4 cite both. Section 6.5.2 begins on p. 128: 10.29's READ, ROUTES 4.30 and D81's entry (corrected in place) read
128-134. (c) lam_s1,2 < lam_s0 holds for every z > 0, not only 0 < z < 4: 10.29(v), H5 and D81's entry say so. (d) d_a g
= -h_A, so h_A is the derivative with the rotation reversed; 10.28(b) and Z6 say so. (e) The partial controls are
completed: Z6 gains d_a g = +h_A claimed, H5 lam_s1,2's first-order coefficient claimed 1/3. (f) The one word the
identifier check flagged in the paper is a quotation of the author; unchanged. (g) The untracked puregauge5.py the
verifier saw is this record's next program, written meanwhile (D84).

*Not checked by the verifier.* The readings of 10.20 ([Hin26c] Theorem 9.36, Corollary 9.43 and section 9 at n = 4); the
index sets; 10.24's kernel dimension and root simplicity; his Lemma 2.15 in detail; minus-sign glyphs in the extraction.

*Runs.* genstates5.py 5/5 (about a minute), mutants 8/8; zstates5.py 6/6 (about half a minute), mutants 7/7;
response5.py all pass; md5 rows current (46). Next: D84, his Proposition 6.18 (4)-(7) in five dimensions.

**D84 (2026-10-23): [Hin26] Proposition 6.18 (4)-(7) in five dimensions (10.30, puregauge5.py).**

M asked to continue while the thirty-eighth verifier read D81-D82. 10.29 left his Proposition 6.18 (4)-(7) OPEN: the
pure gauge states built on the gauge potential operator's growing roots below -1, whose gauge potentials carry no
symmetry. READ at source (alphaXiv, 2026-10-23): [Hin26] pp. 19, 67 ((2.43)-(2.46c) and the remark after them), 113,
117-118 (Lemma 6.6's matrices, (6.17a)-(6.17b), Remark 6.7), 121, 128-134 (Proposition 6.18 (4)-(7), footnotes 74-76,
the proof), 149-151 (Lemma 8.4), 158 (section 8.5).

*Computed (Proposition 10.27, puregauge5.py J1-J5).* (J1) The indicial families of box^Ups on every harmonic type: in
four dimensions his Lemma 6.6 matrices entry by entry and his p. 134 values; in five dimensions det N0 exactly
10.15(i)'s polynomial, N1 = -2 (lam - 3/2) + 2 S-bar, at vl N1 = -2 (lam - 3/2 - gam_U). (J2) His four classes in five
dimensions, every l: Q(l(l + 1)) = l z and Q((l + 1)(l + 2)) = -(l + 2) z put Q's negative roots just below -l and -l -
1, with first-order coefficients -l/(2 (l + 1)(2l + 1)) and -(l + 2)/(2 (l + 1)(2l + 3)); s0's root is at -1 - z/3; sl's
-l + 1 and vl's -l are roots at every z; nothing else is <= 0 but the Killing roots. (J3) delta-bar* is injective at
every class root; his (2.46a)-(2.46c) come out. (J4) No resonance for 0 < z < 4 (four dimensions 0 < z < 3), the z = 0
coincidences all at sl (and at s0 in four dimensions). (J5) The states are exact on Minkowski at every class's largest
k; at vl kappa_i = prod (2l + 2j + 1 + 2 gam_U)/(j (2l + j + 2)), 10.29's 1 + 2 gam_U/5 at l = 1. Controls: his matrices
in five dimensions; z = -1/100; v1 claimed injective at -1; z = 0; the factor k!/(k - i)! dropped.

*Deduced (10.30).* (a) His Proposition 6.18 (4)-(7) in five dimensions on Tangherlini, on 10.29(a): his classes and
ranges, each stationary correction at rho^(mu + 2) where his is at rho^(mu + 1), no logarithm in the leading terms at e_U
> 0. (b) The tensor types of L-hat(0) carry no pure gauge state; their roots -2 and -3 fall with section 8.5's physical
states. All seven parts of his Proposition 6.18 now have five-dimensional counterparts.

*Notes on the computation.* (1) The vector harmonics of S^3 are P(x^3, x^4)(x^1 dx^2 - x^2 dx^1)/r^(l + 1), P harmonic
of degree l - 1 in (x^3, x^4): tangential, divergence-free and componentwise harmonic; at l = 1 the rotation of
10.28-10.29. (2) The irrational class roots are checked exactly with mu a symbol modulo its polynomial, each recursion
step scaled by det N0(mu - i), which is checked nonzero modulo it, so that the check cannot pass vacuously. (3) Real
roots are compared exactly (sympy's real_roots), never as floats. (4) The window [-3, 0] and the ranges are his, chosen
for the decay he proves; whether five dimensions needs the same window is left OPEN.

*Runs.* puregauge5.py 5/5 (about four minutes), mutants 5/5; response5.py all pass; md5 rows current (47). Next: one
verifier on D83 and D84 (10.28-10.30, genstates5.py, zstates5.py, puregauge5.py).

**D85 (2026-10-23): the thirty-ninth verifier's findings on 10.29-10.30, puregauge5.py, D83 and D84, seated.**

The thirty-ninth verifier read 6f373bd read-only, every program run from an archive, and recomputed independently in
Cartesian coordinates without Christoffel symbols, with generic harmonics other than the program's: N0 and N1 for s0,
s1-s5 and v1-v4 in both dimensions, the classes, the injectivity by the gcd of maximal minors over complex lam, the
states (the irrational roots at (1/5, 1/3), residuals about 1e-46), and D83's ranges by hand. Verdict: D83 and D84 hold;
no major finding; three minor findings and notes, each seated here.

*Minor.* (1) J4 asserted only that its bound was positive, which its least positive zero guarantees: a shift resonant at
z = 7/4 passed. J4 now asserts the bound exactly, 4 (four dimensions 3), the roots at it, and 10.30(iv)'s z = 0
coincidences class by class, with the range claimed 0 < z < 5 as a new control. (2) 10.30(b) said the coincidences "would
put logarithms" into -l + 1's first two steps. Computed at e_U = 0 (J6, new; gam_U = 1/3 and 2/7, both dimensions): -l +
1's first step is solvable, and its second step's obstruction is of degree 1 in the first step's kernel coefficient, so
one choice removes it; mu_l,0's first step is obstructed, so a logarithm is forced there. 10.30 gains (vi), and (b) says
which logarithms are forced, which are not, and which -- the stationary corrections, on Tangherlini's sources at e_U = 0
-- are not computed. (3) The paper's [Hin26] entry did not record D84's reads; it now has "READ 2026-10-23 for
Proposition 6.18 (4)-(7)", pp. 19, 67, 113, 117-118, 121, 128-134, 149-151 and 158.

*Notes.* (a) 10.29(a): injectivity past weight 1 follows by inclusion alone, rho^alpha H_b lying in rho^alpha' H_b for
alpha > alpha'; and a kernel element's exponents lie in the index set the roots above the gap generate, shifted by
integers and possibly with logarithms, not "among the roots". (b) The four-dimensional bound 3 is not sharp: at z = 3 the
s0 partner root 2 meets 0 and is double, the class root -2 nothing; five dimensions' 4 is sharp, the class root -2
meeting 0 under mu + 2. J4 asserts both and 10.30(iv) says so. (c) "No logarithm" holds in the leading terms: in five
dimensions omega-breve^2's first correction sits at rho^mu, the class root itself (four dimensions omega-breve^1's), and
at s0 mu_s0 + 4 = 1 - mu_s0 at z = 7/4, above the gap; his E_ind absorbs them. 10.30(a), its closing paragraph, D84's
entry (in place), ROUTES 4.31 and the paper say "in the leading terms". (d) J5's modular check is not vacuous because
each of its eight moduli is irreducible over Q; J5 now asserts it. (e) "Never at sl or vl for l >= 2" was computed for l
<= 5 and l <= 4; 10.30(iii) says so, and a new 10.30(c) deduces every l: a kernel element gives a stationary Killing
1-form of Minkowski space, and those have l <= 1 (his remark after (2.46c), p. 67). The paper and the README name the
computed range. (f) J1 asserts det N0 equal to 10.15(i)'s polynomial, ratio 1. (g) 10.30(a) cited 10.28(i), which covers
delta* and box(0) only, for the orders of A1 and A2; it now cites his decomposition on p. 132 (A0 in rho^2 Diff^2_b, A1
in rho Diff^1_b, A2 = -g^00 in rho^2 C^oo, from (6.4a)), READ at source, in five dimensions by 10.18(b): Tangherlini's A1
differs from Minkowski's in rho^3 Diff^1_b and A2 is in rho^2 C^oo, each two orders above the leading equation (deduced).
(h) The README bullet names the s2 root -1, and ROUTES 4.29's OPEN list points to 4.30-4.31 for his Proposition 6.18.

*Not checked by the verifier*, and OPEN as before: the readings of 10.20; Tangherlini's sources at e_U = 0, so whether
mu_l,1's stationary correction forces a logarithm; the simplicity of L-hat(0)'s roots beyond 10.24's parameter point; his
Lemmas 2.13 and 2.15 in detail.

*Runs.* puregauge5.py 6/6 (about four minutes), mutants 7/7; response5.py all pass; md5 rows current (47).

**D86 (2026-10-23): [Hin26] section 7.2 in five dimensions (10.31, dual5.py).**

M asked to continue after PR #95 merged. 10.30 left [Hin26] section 7.2 OPEN: the large zero energy states of the adjoint
of the constraint propagation operator, built on the Killing 1-forms of Minkowski space, whose trace-reversed symmetric
gradients span the cokernel of the linearized gauge-fixed Einstein operator in his section 8.4. READ at source (alphaXiv,
2026-10-23): [Hin26] pp. 126 ((6.30)-(6.32), Remarks 6.16-6.17), 134-137 (section 7, Theorem 7.1, (7.1)-(7.8)), 137-139
(Lemma 7.2, (7.9)-(7.15), Proposition 7.3 and its proof), 140-144 (section 7.2.1: (7.16), Proposition 7.4, Lemma 7.5,
(7.17)-(7.35)).

*Computed (Proposition 10.28, dual5.py A1-A3).* (A1) The adjoint 2 (delta + C*) G delta* has det N*(lam) = det N(2 - lam)
for s0, sl and vl (l <= 3), so its roots are 2 - conj(lam) (four dimensions his 1 - conj(lam), (7.10)); at v1 -1 and 3 +
2 v gam_C, and N*_v1(2) = 3 + 6 gam_C v_C where his p. 143 has N*_v1(1) = 2 + 4 gam_C v_C. (A2) On Tangherlini the
translations' source is at rho^4, the unique correction at rho^2, h*_s1 at rho^3 (four dimensions rho^3, rho^1, rho^2).
(A3) On one-spin Myers-Perry at first order in a, delta*_(g_a) V_a = -(mu/r^4) a dt (x)_s V', V' the rotation of the
bracket of V's plane with the spin plane, zero for the planes 12 and 34; for the other four c_0 = -2 mu/(3 (h + 2v)) and
h-sharp's rho^3 leading term carries his (7.18)'s ratios (h + 2v -+ 2)/(h + 2v); on Kerr his (7.20), (7.31) and (7.18)
come out. Controls: the shift 1 in five dimensions; the four-dimensional order rho^2 in five dimensions; his c_0 in five
dimensions.

*Deduced (10.31).* (a) His Lemma 7.2 in five dimensions, on what 10.21(e) rests on: invertible on the weights (0, C_0 +
2], the adjoint's roots 0, of negative real part or beyond C_0 + 2. (b) His Proposition 7.3 on Tangherlini: eleven dual
states against his seven, the time translation's and the six rotations' h* rapidly decaying at a = 0 and the
translations' at rho^3, one order faster than his (7.15). (c) Section 7.2.1 at first order in a: his (7.18) with m ->
mu/2 and rho^2 -> rho^3, depending on V only through V'; two of the six rotations Killing, so the space where (7.16)
holds falls from six to two.

*Notes on the computation.* (1) The adjoint is the formal one, 2 (delta + C*) G delta* with C* the pointwise adjoint of
C, his (7.11). (2) The angular components are read in the orthonormal frame (divided by r), as his splitting (2.37b)
does; read in coordinates they gave spurious orders in a first attempt. (3) A3's first control claimed the ratios, which
agree in both dimensions, so it could not fail; it now claims his c_0 = -2 mu/(h + 2v) in five dimensions, which does.
(4) Only first order in a: Myers-Perry enters through d_a g = -h_A (10.28(vi), Z6), and the higher orders, Lemma 7.5 on
the full metric and (7.19) stay OPEN.

*Runs.* dual5.py 3/3 (about a minute and a half), mutants 3/3; response5.py all pass; md5 rows current (48). Next: the
fortieth verifier on D85 and D86 (10.29-10.31, puregauge5.py, dual5.py).

**D87 (2026-10-23): the fortieth verifier's findings on 10.30-10.31, puregauge5.py, dual5.py, D85 and D86, seated.**

The fortieth verifier read 5df1aee and 925844b read-only, every program run from an archive, and recomputed independently
in Cartesian coordinates without Christoffel symbols, with its own harmonics: the adjoint's indicial families in both
dimensions (shift 2 in five, 1 in four, failing with the wrong shift), the translations' dual state at leading order in
the mass, the rotations' at first order in a on the full Tangherlini and Schwarzschild operators, J6's ranks and
obstructions, J4's bounds; it READ every quotation of 10.31 at source, and p. 132's decomposition and p. 67's Killing
remark. Verdict: D85 and D86 hold; no major finding; three minor findings, one of formatting, and notes, each seated
here.

*Minor.* (1) 10.31's Proof said the families are read "at r = 1 and two angles", but dual5.py's fam() decomposed at one,
A2 solved its correction at one and A3 read at one, so pure type and independence of the angle were never checked. fam()
now reads at two generic angles and asserts that they agree, A2's correction is checked at a second angle, A3's c_0 and
ratios too; the Proof says so. (2) A1 asserted box^C's polynomials 10.12's "up to powers of h" by checking only that the
ratio involved h alone; it now asserts the ratios h^-2 (s0), h^-3 (sl) and h^-1 (vl), and 10.31(i) prints them. (3) The
paper said the four non-Killing rotations carry "his coefficients": c_0 = -2 mu/(3 (h + 2v)) differs from his -2M/(h +
2v) by more than M -> mu/2, through N*_v1(2) = 3 + 6 gam_C v_C; only (7.18)'s ratios are his, and the paper now says so.

*Formatting.* The rewrapping helper of D85-D86 took the wrong continuation indent inside ROUTES 4.4's item 2, in 4.5's
paragraph (which it broke) and in the paper's verifier record; the three are reflowed.

*Notes.* (a) 10.31(i)'s "the adjoint's roots are 2 - conj(lam)" now reads "for these types", the general statement being
(a)'s. (b) A3 checks the lower orders for every non-Killing plane, not only 13. (c) The two Killing rotations are Killing
on the full one-spin metric for every a (its coefficients functions of r and theta, 10.28(vi)), so the space where (7.16)
holds is two-dimensional for small a != 0, not only at first order; 10.31(c) says so. (d) The paper's sentence on the
dual states now carries its condition, the readings 10.21 rests on. (e) The default python3 here is 3.13.16 with sympy
1.14.0 (python3.11 has no sympy in this container); Appendix D now says Python 3 and names them.

*Runs.* dual5.py 3/3 (about a minute and a half), mutants 3/3; response5.py all pass; md5 rows current (48).

**D88 (2026-10-23): [Hin26] Lemma 8.12 and Proposition 8.11 in five dimensions (10.32, pairing5.py).**

M asked to continue after PR #96 merged; the fortieth verifier's findings are D87. 10.31 left his Proposition 8.11, Lemma
8.12 and Corollary 8.13 OPEN: the zero energy kernel and cokernel of L-hat(0) and the pairings that count them. READ at
source (alphaXiv, 2026-10-23): [Hin26] pp. 145 ((8.1)), 154-158 (Proposition 8.9 through Corollary 8.13); [Hin24b]
(arXiv:2408.06715) pp. 13, 33 ((3.1a)), 38-39 (Lemma 3.8), 50-53 (Proposition 3.16, Lemma 3.17 and its proof); [Hin23b]
(arXiv:2306.07409) pp. 101-110 (Theorem 9.6 and its proof), 116-117. His Lemma 8.12 is proved by [Hin24b] Lemma 3.17's
proof, "verbatim", which removes the gauge terms and reduces to [Hin23b] Theorem 9.6, where every pairing is a boundary
pairing at infinity on the leading terms.

*Computed (Proposition 10.29, pairing5.py P1-P5).* The boundary pairings directly, on Minkowski in Cartesian coordinates,
chi a radial cutoff and the sphere integrals exact. (P1) Four dimensions: his table, -8 pi m-dot, -8 pi m (q . a-dot), 4
pi m (q . c). (P2) Five dimensions: mass against dt -3 pi^2 mu-dot, rotations -2 pi^2 mu on their own plane, the other
Kerr-row entries 0. (P3) Centres of mass (3 pi^2/2) mu (q . c), 0 against dt. (P4) The 11 x 11 matrix non-degenerate,
block triangular whatever the entries the leading terms leave undetermined. (P5) Kerr-Schild, a pure gauge tensor and t*
= t - r change nothing. Controls: G dropped; the mass perturbation's dr^2 dropped; h-breve dropped; the first-order
translation pairing, which his Theorem 9.6(6) says vanishes, in place of the centre of mass; a non-gauge term added.

*Deduced (10.32).* (a) The entries are -8 pi M-dot, -8 pi J-dot and 4 pi M (q . c) in both dimensions, M and J the ADM
mass and angular momentum. (b) His Lemma 8.12 in five dimensions at a = 0, and near it by continuity, for his L_b of
(8.1); his printed values, -16 pi m-dot and so on, are [Hin24b]'s, whose L is twice L_b. (c) His Proposition 8.11 with
dim ker = dim coker >= 11; equality rests on [AHW24] Theorem 6.1(2) in five dimensions, OPEN. (d) His Corollary 8.13 with
eleven for seven on (c).

*Notes on the computation.* (1) Three entries per centre of mass -- against the rotations of the planes containing its
direction -- sit above the critical weight: their leading terms vanish over the sphere, and they are not determined by
leading terms. The program returns them as undetermined, never as 0, and P4 shows the determinant free of them; his
argument for Theorem 9.6(5) gives 0 there at a = 0. (2) The first P4 control paired only the [[D Ric, t], chi] piece and
passed vacuously; the control is the Kerr-row formula applied to h_b,c, which is his Theorem 9.6(6), and it fails as it
should. (3) sym() first divided Python integers and produced floats; it is exact.

*Runs.* pairing5.py 5/5 (about two minutes), mutants 5/5; response5.py all pass; md5 rows current (49). Next: the
forty-first verifier on D87 and D88 (10.31-10.32, dual5.py, pairing5.py).

**D89 (2026-10-24): the forty-first verifier's findings on D87 and D88 (10.32, pairing5.py).**

The forty-first verifier read D87 and D88 with programs of its own (an explicit C^3 cutoff and Gauss-Legendre
quadrature, three independent formulas for every pairing, all agreeing to 5e-14): no major finding; every value
reproduces, the determinants, the ADM normalization and every quotation at its page. Five minor findings and two nits,
seated here; READ again at source (alphaXiv, 2026-10-24): [Hin26] pp. 125 ((6.29)), 138 ((7.12)), 156-157 (the kernel
proof, Lemma 8.12); [Hin24b] pp. 44 (Lemma 3.11), 51-53 (Lemma 3.17 and its proof).

*Minor 1 (the s0 sign).* [Hin23b]'s s0 dual 1-form is dt (Definition 9.2); [Hin26]'s omega-bar_s0 = g-bar(d_t*, .) = -dt
((6.29)) and omega*_s0 - chi g_b(d_t*, .) decays ((7.12)), as [Hin24b] Lemma 3.11(2) has omega*_s0 - chi d_t^flat. A
pairing is linear in the dual state, so with his normalization the mass entry is +8 pi m-dot for L_b (+16 pi m-dot for
[Hin24b]'s L = 2 L_b), +3 pi^2 mu-dot in five dimensions; he prints -16 pi m-dot, [Hin23b]'s sign, and uses it so in his
(8.37)(1). 10.32(b), ROUTES 4.33 and pairing5.py's docstring now say the factor and the sign; no non-degeneracy changes.

*Minor 2 (entries above the critical weight).* D88's boundary() skipped an integrand vanishing pointwise before it
looked at the weight, so the mass against all six rotations and each centre of mass against the three rotations of
planes not containing its direction (four dimensions three and one) came back 0, though they lie above the critical
weight, where the leading terms do not determine an entry -- his four-dimensional mass-against-rotation entry, -8 pi (q
. a) m-dot, comes from subleading terms. pairing5.py now reads each entry's weight from the homogeneity of its two
tensors (weight()) before computing it, returns every super-critical entry undetermined, and checks A and B against that
weight; undetermined() lists all of them, P4 takes them all as unknowns, and the determinants are unchanged: 2048 pi^7
mu^6 and -972 pi^22 mu^10 (the mass row's unknowns sit beside a dt column whose only nonzero entry is the mass's). At a
= 0 the mass's are 0 by SO(4) symmetry (the mass state invariant, the rotation duals spanning so(4), which has no
invariant vector), the centres of mass's by his Theorem 9.6(5) argument; 10.32(i)-(iv) and (b) say so.

*Minor 3 (Corollary 8.13).* It needs the (co)kernel exactly 11-dimensional near b_0, which is (c)'s equality, OPEN;
10.32's closing paragraph now carries Lemma 8.12 over and Proposition 8.11 and Corollary 8.13 up to the rigidity, and
the paper says "at zero rotation" and "near five-dimensional Tangherlini (linearised Myers-Perry plus pure gauge)".

*Minor 4 (independence).* The pairings of [L, t*] u with the dual states see b-dot only, h_s1(S) pairing to 0 with each
([Hin23b] Theorem 9.6(6)); S = 0 is his separate argument, h_s1(S) = 0 only if S = 0, d(rS) not being Killing ([Hin26]
p. 156). 10.32(c) now argues so.

*Minor 5 and the nits.* [Hin24b] Proposition 3.16 begins on p. 49: "49-53" in 10.32's READ, ROUTES 4.33, pairing5.py and
the paper's reference entry. ROUTES 4.32's "2 - conj(lam) for each root lam of box^C" now says "of these types", as
10.31(i) has since D87. "Its Minkowski part the boost's Killing form" (pairing5.py, 10.32(iii)) meant that the Minkowski
part vanishes, the boost being Killing, and now says that.

*A finding of D89's own (P5's pure gauge check).* D88's pure gauge tensor delta*(log R dt) has chi times it pure gauge
again (chi delta*(F dt) = delta*(G dt), G' = chi F'), so its cut-off source is identically 0 and the invariance check
tested nothing; the same holds for delta*(f(R) alpha) with alpha any constant 1-form, dchi (x)_s f alpha being delta*(G
alpha). P5 now uses delta*(x_2 R^-(n-2) dx_1), homogeneous as the mass perturbation, asserts that its source is not
zero, and finds 0 at every determined entry (dt and the translations) and the rotations undetermined, as the integration
by parts against D Ric* h* = 0 says. The selftests did not catch it because the check was vacuously true; mutants could
not, the control being elsewhere.

*Notes.* (a) The verifier's formula C gives the centres of mass against the rotations exactly 0 at first order in mu at
a = 0, the rotation duals exact on Tangherlini: the deduced 0, computed by it. (b) Hintz's four-dimensional shortcut "g'
in rho^2, omega* = O(1) => 0" moves to the threshold rho^3 in five dimensions, which is why the mass against dt is
critical there and not 0, as P2 has it. (c) The two Killing rotations are d_phi and d_psi of 10.28(vi)'s metric for
every a, and the rotation bracket is injective on the other four, as 10.31(c) says. (d) [AHW24] Theorem 6.1(2) itself
the verifier did not read; static5.py and 10.33 take it up (D90).

*Runs.* pairing5.py 5/5 (about three and a half minutes, P5 now pairing a source that is not zero), mutants 5/5;
response5.py all pass; md5 rows current (49).

**D90 (2026-10-24): [AHW24] Theorem 6.1(2) in five dimensions at a = 0 (10.33, static5.py).**

M asked to continue after PR #97 merged. 10.32(c) left one input of [Hin26] Proposition 8.11's kernel count OPEN in five
dimensions: [AHW24] Theorem 6.1(2), that every decaying stationary solution of D Ric(h) = 0 smooth across the horizon is
a linearized Kerr metric plus a pure gauge term. READ at source (alphaXiv, 2026-10-23 and 2026-10-24): [AHW24]
(arXiv:2207.12952v1) pp. 1, 35 (Theorem 6.1), 41 (section 6.4, its proof through the Teukolsky scalars and the gauge
invariants); [Hin26] pp. 156-157 (the kernel proof: u in A^(eps_ind - eps), "By [AHW24, Theorem 6.1(2)], with q =
eps_ind - 3/2 - eps ...", omega in A^(-1+eps_ind-eps); Corollary 8.13's proof). On Tangherlini, static, [KI03]'s
decomposition makes it ordinary differential equations in r, harmonic by harmonic.

*Computed (Proposition 10.30, static5.py S1-S6).* gmodes5.py's reduced operators (G1-G4) at coefficients independent of
t. (S1) Tensor, l >= 2: (1/r^3)(r^3 f H')' = l(l + 2) H/r^2, Phi = r^(3/2) H with V_T/f > 0, the energy identity,
exponents l, -(l + 2) at infinity and 0, 0 at r_h. (S2) Vector, l >= 2: E_r = (k_V^2 - 2) F_r/(2 r^2) forces F_r = 0,
E_t gives (r^5 y')' = (k_V^2 - 2) r^3 y/f with F_t = r y, its identity and exponents; h_ri = r (f_r - f_t/f) V_i in
ingoing form. (S3) Scalar, l >= 2: E_tr = k^2 F_tr/(2 r^2); in [KI03]'s X, Y the four even equations are equivalent to a
first-order flow, Y' = f'(X - Y)/(2 f) their (2.24b), the determinant of the solve 18 k mu r^2 (r^2 - mu)^6; Z~ defined
by (2.24a) has Z~' = X; Phi = (3 Z~ - r (X + Y))/(r^(1/2) H) solves the master equation at sigma = 0 with G3's V_S,
det[Phi; Phi'] = r^3/(k^2 mu) up to r^(1/2); X and Y free of 1/f in ingoing form where F_tr = 0. (S4) l = 0: f_tr enters
no stationary equation; the solutions are the time rescaling (f, 0) and the mass (r^-2, r^-2 f^-2), r^-2 dv^2 in ingoing
form. (S5) Vector l = 1: f_t = a r + b r^-3, a r the rigid rotation delta*(2 a t r^2 V), b r^-3 the rotation, regular in
ingoing form. (S6) Scalar l = 1: the stationary gauge f_tt = f_t = H_L = 0 algebraic, determinant -mu (r^2 - mu)/(4
r^6), then rank 3 of 3. Controls: Phi = r^(1/2) H; l = 1 at the vector type; Phi without 1/H; (r^-2, 0) for the mass;
the rotation in Schwarzschild form; f_t left free.

*Deduced (10.33).* (a) [AHW24] Theorem 6.1(2) at a = 0: h stationary, smooth across the horizon, conormal and O(r^-eps),
0 < eps < 1, with D Ric(h) = 0 is a mass and one of so(4)'s six rotations plus delta* omega, omega smooth across the
horizon and O(r^(1 - eps)); (b)-(e) sector by sector, the energy identities with 10.24's potentials, the exponents, the
gauge 1-forms and the horizon's r-row. (f) [Hin26] Proposition 8.11 at Tangherlini, dim ker = dim coker = 11, and
Corollary 8.13 there; near Tangherlini on the reading that (8.22)'s kernel dimension is upper semicontinuous in b, as
his Corollary 8.13's proof uses. (g) Without the decay the time rescaling and the rigid rotations (delta* of 1-forms
linear in t) and the static tidal fields at l >= 2 (not pure gauge) survive.

*Notes on the computation.* (1) At sigma = 0 [KI03]'s Z = i sigma Z~ leaves Z~ undefined, and Z = 0 there (F_tr = 0);
reading (2.24a) as Z~'s definition restores the master variable, and the flow then gives Z~' = X, (2.24c), as an
identity, not an assumption. (2) Phi = O(r^(7/2 - eps)) is a crude bound from X, Y = O(r^(1 - eps)) and the
coefficients' degrees 2 and 4; at l = 2 it is exactly what excludes the exponent 7/2, and it needs eps > 0. (3) At
vector l >= 2 regularity in ingoing form gives y(r_h) = 0 only once E_r has forced F_r = 0; at l = 1 E_r vanishes, F_r
is free, and that is where the rotation lives (S2's control). (4) At scalar l = 1 every stationary solution is delta* of
a stationary 1-form, the gauge determinant -mu (r^2 - mu)/(4 r^6) being nonzero; on Minkowski it vanishes, and there the
uniform field h_tt = 2 g z is pure gauge only through a 1-form quadratic in t; the decay enters this sector through
omega's growth, read from the f_rr, f_t and H_L rows. (5) The function F_t/r is y, not v, the ingoing coordinate being
v. (6) The exponents at infinity are from the limit of r^2 op(r^s)/r^s, the one at r_h from Frobenius' p0 and q0; a
first attempt multiplied by rho^(2-s) where rho^(1-s) was right and got 0.

*Runs.* static5.py 6/6 (about a minute and a quarter), mutants 6/6; response5.py all pass; md5 rows current (50).

**D91 (2026-10-24): [Hin26] section 8.5 in five dimensions, the physical states (10.34, physical5.py).**

M asked to continue, with fewer PRs; this batch carries D91 and the forty-second verifier's findings on D89-D90 in one
PR. READ at source (alphaXiv, 2026-10-24): [Hin26] pp. 25 (section 1.4.1), 140-142 (section 7.2.1), 154-163 (Remark 8.10
and (8.21), section 8.5: Proposition 8.14, Lemma 8.15, their proofs, (8.27)-(8.37)), 176 (Definition 9.10); [DLMF]
(15.8.2), (15.8.8), (15.10.1). His section 8.5 builds large zero energy states at the roots that are not pure gauge, sl
and vl's -l for l >= 2 (his window [-3, 0]: l = 2, 3), smoothly in the rotation by his Lemma 8.15; in five dimensions
10.24's physical roots are -l at every type, the tensor type included.

*Computed (Proposition 10.31, physical5.py Y1-Y4).* (Y1) 10.33's stationary equations are Gauss's hypergeometric
equation in z = r^2/mu: H with (-l/2, 1 + l/2, 1), y = F_t/r with ((1 - l)/2, (l + 3)/2, 3), Y = z^(1/2) (z - 1)^-1 w
with (-l/2, 1 + l/2, 2), l symbolic. (Y2) The solutions smooth at z = 1 -- F(-l/2, 1 + l/2; 1; 1 - z), (1 - z) F((l +
5)/2, (3 - l)/2; 2; 1 - z), z^(1/2) F(2 + l/2, 1 - l/2; 2; 1 - z) -- solve them, exactly where they terminate and at 40
digits for l = 2, ..., 8, and grow like r^l (H, f_t, F) with coefficients Gamma(l + 1)/Gamma(1 + l/2)^2 and two like it,
never 0, matched at z = 10^12. (Y3) From lin5.py's factors at 50 digits: at sl, vl, tl, l = 2, 3, -l simple and -l - 1
no root (his Step 4's condition), the root next to -l at sl box^Ups's class root. (Y4) L_R h_A = h_[A,B] on 4+1
Minkowski; <[A_V, e_12], A_V'> on so(4) of rank 4, kernel e_12 and e_34; in three dimensions his triple product.
Controls: c = 2 at the tensor type (Y1, Y2); -l for -l - 1; h_[B,A] for h_[A,B].

*Deduced (10.34).* (a) At a = 0, for every l >= 2 and the three types, the stationary solution smooth across the horizon
is unique up to scale and pure gauge and grows like r^l with a nonzero coefficient; put into the gauge it is his
Proposition 8.14's state, the tensor types t2, t3 and every higher l included; no obstruction at a = 0, a type-l tensor
pairing to 0 with the s0, s1, v1 dual states by SO(4) covariance. (b) His Lemma 8.15 in five dimensions: (1) minus
10.32's centre-of-mass row; (2) by his Remark 8.10, which holds in five dimensions with so(4)'s bracket, -pi^2 mu <[A_V,
A_b], A_V'>, 0 at a = 0, his Step 2 met by A_V1 = v_b/(pi^2 mu) by ad-invariance. (c) His Proposition 8.14 near a = 0
for l = 2, 3 by his Steps 0-5, on the readings 10.33(f) rests on.

*Notes.* (1) Y ~ r^(l-1) while X ~ r^(l+1)/mu and F ~ r^l: Y = r (f F_rr - 2 F) cancels at leading order; the
exponents (l - 1)/2 and -(l + 3)/2 of Y in z are Y1's (X = Y + r (r^2 - mu) Y'/mu). (2) At sl, -l and box^Ups's class
root mu_l,1 + 1 = -l - (l + 2) z/(2 (l + 1)(2l + 3)) + O(z^2) (10.30(ii)) are 3.81 x 10^-7 (l = 2) and 2.78 x 10^-7 (l
= 3) apart at Proposition 10.9's point, z = 4 e_U gam_U^2 = 4 x 10^-6 -- simple, but close; they meet at z = 0. The
in-progress commit printed 3.3 x 10^-7, section 10.24's s1 pair, in physical5.py and 10.34(iii); Y3 now checks the
first-order term (D92). (3) Lemma 8.15(1)'s zero against the non-Killing rotations at a != 0 is not established here
(10.32(b) has it at a = 0); his Step 2 uses that pairing only through his lambda-sharp functional and on the Killing
rotations, where his Theorem 9.6(5) argument applies, so the construction does not need it. (4) Which l five
dimensions needs is OPEN: his window [-3, 0] is his choice for the decay he proves (10.30).

*Runs.* physical5.py --selftest 4/4 at D91 (Y3 in 713 s, lin5.py's determinants); its mutants and the runs after D92's
change to Y3 are D92's.

**D92 (2026-10-24): the forty-second verifier's findings on D89-D90, seated.**

One independent verifier read D89 (f5d320e) and D90 (1c0fcda) against base 2af8d1a, rederiving Proposition 10.30's S1-S6
with a linearized Ricci tensor of its own (scalar type at general k, vector at general k_V, tensor at l = 2 by an
explicit harmonic, l = 0 and scalar l = 1) and the Minkowski pairings by its own code, and reading [Hin26] pp. 125, 138,
156-157, [Hin23b] Definition 9.2 and Theorem 9.6, [Hin24b] Lemmas 3.11 and 3.17, [AHW24] pp. 1, 35, 41 and [KI03] p. 11
at source. Verdict: no major finding; every computed claim reproduces; 10.33(a)-(g) hold as labelled; D89's s0 sign
confirmed at source. Four minor findings, three nits, notes.

*Minor 1 (P5 could not fail).* D89's pure gauge tensor delta*(x_2 R^-(n-2) dx_1) paired 0 by reflection parity alone:
against dt both sphere integrals vanish separately, the tensor odd under x_1 -> -x_1 and the dual even, and against the
translations a stationary spatial tensor has no tj source; the non-gauge x_1 x_2 R^-n (dt^2 + dR^2) passes the same
check with the same row. Repaired as proposed: delta*(dG), G = R in four dimensions and log R in five, homogeneous as
the mass, its source nonzero and its sphere integrals I_A = I_B = -4 pi and -3 pi^2, so its 0 against dt is -I_A + I_B,
a cancellation; P5 now requires both nonzero. A second control, the non-gauge R^-(n-2) |dx|^2 in its place (pairing -4
pi and -6 pi^2 with dt), is caught; mutants 6/6. pairing5.py's docstring, 10.32(v) and its proof, README and the paper's
appendix row say so.

*Minor 2 (p. 157 misdescribed).* ROUTES 4.34 and the D90 entry said near-Tangherlini rests on upper semicontinuity "as
his Corollary 8.13's proof uses". His proof takes the (co)kernel near b_0 as Proposition 8.11 gives it ("The
requirements on f*_j and f#_j are satisfied also for the (co)kernel ... when b is close to b_0") and cites [Vas13]
section 2.7 and [Hin26c] section 9.2.3 Part (3) for the continuity of the augmented operator's inverse in b; he uses no
semicontinuity. ROUTES 4.34 now has 10.33(f)'s wording (a property of the uniform Fredholm estimates his proof invokes,
not read line by line); the D90 entry stands as written and is corrected here.

*Minor 3 (Corollary 8.13 at Tangherlini).* Corollary 8.13 is a statement for b near b_0; at b_0 alone 11 for 7 gives the
augmented operator's invertibility there and no more. 10.33(f) and its closing paragraph, ROUTES 4.4, 4.5, 4.29 and
4.34, README, static5.py's docstring and the paper's appendix rows now say Proposition 8.11 at Tangherlini and, on a
reading, near it, with Corollary 8.13 on that reading; "at and near" is gone from the five places that had dropped the
qualifier, and from physical5.py's README and paper rows, which had copied it in D91.

*Minor 4 ([KI03] section 4 uncited).* [KI03] p. 11, section 4 "Static perturbations", prints the static system (4.1),
(4.2) and the master variable (4.3), Phi := (Q_Y X - Q_X Y)/(2 k^2 r^(n/2-1) f' H), and says "the same master equation
holds for both non-static and static perturbations" -- READ at source here (alphaXiv, 2026-10-24). static5.py S3 now
checks (4.2a), (4.2b) at n = 3 against the flow and (4.3) against the record's Phi, both identically; 10.33's opening,
10.30(iii) and its READ cite it. The D90 entry's note (1), which presented reading (2.24a) at sigma = 0 as the record's
own way to the master variable, is corrected here: [KI03] had done it.

*Nits.* (1) The energy identities S1 and S2 checked are identities for any f, V and lambda and could not fail; they are
no longer checks, and the sign each needs (V_T/f > 0, k_V^2 - 2 >= 5) is, as before. (2) [AHW24] v1's Theorem 6.1 (p.
35) is one statement for Im sigma >= 0, 0 < a < m, without numbered parts; [Hin26] cites its sigma = 0 case as Theorem
6.1(2), and static5.py's docstring now says so. (3) "10.24" meant two things in 10.33-10.34: Proposition 10.24
(gmodes5.py, section 10.27) and section 10.24 (lin5.py, Proposition 10.21); each use now says which, and 10.34's
"10.24(ii)" is Proposition 10.21(ii).

*Notes, accepted.* Not checked by the verifier: the tensor type at general l by explicit harmonics (l = 2 only); [Vas13]
section 2.7; the sign's use in [Hin26] (8.37)(1); the class and horizon smoothness of (8.22)'s kernel elements, which
the record marks OPEN. Its confirmations: 10.33(f)'s 0 < eps_ind - eps < 1 (Hintz takes eps_ind below d(Re lam, Z) <=
1/2, p. 125); Phi = O(r^(7/2 - eps)) excludes the r^(7/2) branch at l = 2, the logarithmic case included; the X, Y flow
has residues 0 and -1 at r_h; A_r = O(r^(1 - eps)) from the f_rr row; the [AHW24] and [Hin26] quotations and pages.

*D92's own finding.* Checking physical5.py's Y3 output: the root next to -l at sl is box^Ups's class root mu_l,1 + 1 =
-l - (l + 2) z/(2 (l + 1)(2l + 3)) + O(z^2) (10.30(ii)), 3.81 x 10^-7 below -l at l = 2 and 2.78 x 10^-7 at l = 3 (z = 4
x 10^-6), where the in-progress D91 commit printed 3.3 x 10^-7 -- section 10.24's s1 pair, z/12, copied to the wrong
root. The distance falls by ten with e_U (a scratch run at l = 2, e_U/10 and e_U/100). Y3 now requires the root real,
below -l, and its first-order term matched to 10^-3; 10.34(iii) and the docstring are corrected.

*Runs.* pairing5.py --selftest 5/5 (about three and a half minutes), --mutants 6/6; static5.py --selftest 6/6 (about a
minute), --mutants 6/6; physical5.py --selftest 4/4 (Y3 in 1047 s beside other runs, 713 s alone), --mutants 4/4;
paper/response5.py --selftest all pass; Appendix D's md5 rows current (51, physical5.py added).

**D93 (2026-10-24): [Hin26]'s window in five dimensions (10.35, window5.py).**

M asked to continue; the next of item 2's open pieces was 10.34's: which l five dimensions needs. READ at source
(alphaXiv, 2026-10-24): [Hin26] pp. 17-18 ((1.23): a term t*^-alpha at iota+ meets a large root lam at K+ as
t*^(-alpha+lam)), 27-30 (footnote 27: the t*^-1 term at iota+ from the trace-free spherical part's radiation coupling
into the (dt*)^2 component, (5.28)'s (7, 6)-entry), 32 (it "is anticipated to encode the Bondi mass"), 34 (the "2" of
2-admissibility is the order of L-hat_b(sigma)^-1's pole at 0; footnote 35), 85, 92-93 (Definition 5.2, Proposition
5.11, (5.27)-(5.28)), 117, 128 ([-3, 0] captures the pure gauge contributions to t*^-4), 149 (Lemma 8.4), 173-177
(Proposition 9.9, (9.32), Proposition 9.11, (9.39a)-(9.39b), "The smallest lam ... is lam = 1"), 199, 218, 225
(Corollary 11.10), 273 (u needs t*^(-2-eps_K) and the sources t*^(-4-eps_K)), 279, 324.

*Computed (Proposition 10.32, window5.py W1-W3).* (W1) lin5.py's roots in [-3, 0] at its point: in four dimensions
exactly his Lemma 8.4's, (9.32)'s set (s0: c0 e0; s1: c0 c-1 e-1; s2: c-1 c-2 e-2 e0; s3: c-2 e-1 e-3; s4: e-2;
s5: e-3; v1: e-1; v2: e-1 e-2; v3: e-2 e-3; v4: e-3), in five the same and t2: e-2, t3: e-3 -- every root real,
the class roots box^Ups's, none from box^C. (W2) The bookkeeping -- the j-th companion of a root mu at K+ order
alpha - mu + j (s1: alpha - 1 + j, v1: alpha + j), kept to order 4 -- returns (9.32)'s orders at alpha = 1, and
for every alpha in (1, 2] keeps s2, v2, t2 at -2 with no companion and nothing at l >= 3. (W3) box(r^-p a(t - r)
S) = (2p - d + 1) a' r^(-p-1) S + (l + p)(p - d - l + 2) a r^(-p-2) S: the radiative order (d - 1)/2 and the
Coulombic d - 2 coincide at d = 3 and part at d = 4, where the latter carries (d - 3) a' = a'. Controls: the
tensor types dropped (W1), s3 and v3 dropped at alpha = 1 (W2), the radiative order claimed to leave a' (W3).

*Deduced (10.35).* (a) alpha_5 = 2: Theorem M(c)'s mass aspect at r^-2, quadratic in the radiation fields, at the
Coulombic order -- on the reading that nothing at iota+ decays more slowly. (b) The pole order is 2, the
centre-of-mass chains ended by Proposition 10.29(iii)'s pairing, so the sources need t*^(-4-eps_K) as in four
dimensions. (c) The window is [-2, 0]; for any alpha_5 in (1, 2] the physical states needed are s2, v2, t2 at -2
alone: 10.34's l = 3 states and his Step 4 are spare. (d) alpha = 1 returns his [-3, 0] and (9.32).

*Notes.* (1) The four-dimensional control is exact: lin5.py at n = 3 reproduces every root of his Lemma 8.4 in [-3,
0], so the bookkeeping's input in five dimensions is the same computation. (2) The conclusion does not need alpha_5 =
2 exactly: any iota+ order in (1, 2] gives the same physical states; only a t*^-1 term at iota+, which in five
dimensions would need an r^-1 term at future null infinity, slower than radiation, would bring l = 3 back. (3) The
class roots just below 0 enter at order 2 + O(z) and are eliminated unless eps_K lies below their distance. (4) New
proposition numbers collide with section numbers (Proposition 10.32 in section 10.35); references to a proposition's
item now name the proposition (D94 completes this).

*Runs.* window5.py --selftest 3/3 (W1 in about 23 minutes, lin5.py's determinants in four and five dimensions),
--mutants 3/3, on the final file after D94's one-line docstring change (before it also 3/3 and 3/3).

**D94 (2026-10-24): the forty-third verifier's findings on D91-D92, seated.**

One independent verifier read D91 and D92 (627a0d3, e2ea5e5, 1bc4243 against d2735c0), recomputing Proposition 10.31
from [KI03]'s own equations (4.2), (5.3), (5.11)-(5.12) and the class root from its own box^Ups, and reading [Hin26]
pp. 25, 125, 155-163, 176, [KI03] p. 11 and [AHW24] p. 35 at source. Verdict: no major finding; every computed claim
reproduces; D92's repairs sound (the new P5 cannot pass by symmetry: against dt the pairing is (1/2) int (d_i d_j
h_ij - Delta tr h), whose kernel among isotropic tensors of the mass's homogeneity is exactly the pure gauge line).
Four minor findings, nine nits, notes. READ again here at source: [Hin26] pp. 145 ((8.2a)), 157-163.

*Minor 1 (Step 2 and its dependency).* His Step 2 uses Lemma 8.15(1)'s vanishing against every h*_v1 ("By Lemma 8.15,
the left-hand side of (8.34) is independent of the choice of V_1 ... Similarly, the left-hand side of (8.35) is
independent of S_1", p. 161), not only its lambda-sharp form as 10.34(b)(1) and D91's note (3) said; and his Steps 1-2
rest on his Proposition 7.4 and (7.19) ((8.32c)-(8.33), footnote 82), which five dimensions has at first order in one
spin only (10.31(c)). Repaired: 10.34(b) now modifies Step 2 -- under the five-dimensional Proposition 7.4 the
non-Killing pairings P(S_1, V') = <p_b(S_1), [A_b, A_V']> are absorbed into V_1, A_V1 = (v_b + p_b(S_1))/(pi^2 mu) --
and 10.34(c) adds Proposition 7.4, Lemma 7.5 and (7.19) on the full two-spin metric to its conditions; ROUTES 4.4 and
4.35, README, physical5.py's docstring, the paper's settling paragraph and 10.35(c) say so. D91's note (3) is
corrected here.

*Minor 2 (the factor of 2).* 10.34(b)(2) set -pi^2 mu <[A_V, A_b], A_V'> beside his -8 pi m. The record's formula in
four dimensions, with Proposition 10.29(i)'s rotation row -4 pi mu (mu = 2m), gives -4 pi m: his -8 pi m is (1/2)
times Lemma 8.12's printed -16 pi m (p. 159), the [Hin24b] normalization 10.32(b) halves. Now said, with which
operator L-hat(0) is: L_b's zero energy part, where his (8.2a) writes 2 L_b = ... + L-hat_b(0).

*Minor 3 (spanning).* "Every l >= 2 ... spanning ker N(L-bar(0), -l)" needs -l simple, computed for l <= 12 at the
point (section 10.24) and l = 2, 3 in Y3; existence, uniqueness and growth hold for every l. Qualified in 10.34(a),
ROUTES 4.35 and physical5.py.

*Minor 4 (the a-dependent zeros).* 10.34(b)(2)'s "0 against h*_s0 and h*_s1" cited a table that covers a = 0 only;
near it these are the rotation row's a-dependent entries, OPEN beyond continuity (10.32), and his Step 2 solves
(8.34)- (8.35) as a coupled system. Now said.

*Nits.* (1) ROUTES 4.35's "(4.24)" is 4.25 (lin5.py). (2) The paper's decision range and a missing ";" in its verifier
table. (3) An accidental wrap in 10.34's proof ("Controls: in" / "(i) c = 2 ..."). (4) "-l - 1 ... its nearest root at
distance 1": at sl it is the class root, at 1 - 3.81 x 10^-7 (l = 2) and 1 - 2.78 x 10^-7 (l = 3); said. (5) Bare
"10.30(ii)", "10.30(iv)", "10.32(ii)", "10.32(iii)", "10.28(v)", "10.28(vi)" and "10.23(ii)" collided with
Propositions 10.30, 10.32 and 10.28; each now names its proposition (10.27, 10.29, 10.25, 10.20) in 10.33-10.35,
physical5.py, pairing5.py and window5.py, and physical5.py's "10.24 found" is section 10.24's; LOG entries stand as
written. (6) 10.34's quotation "comprising the spaces N_sl(L-bar(0), -l)" was not verbatim: he prints N_s2 and N_v2 at
-2 (p. 158); quoted as printed. (7) ROUTES 4.34's READ list now has [KI03] p. 11. (8) DLMF 15.8.8's coefficient needs
m = b - a >= 1, here l + 1; said in 10.34's proof and the paper's [DLMF] entry. (9) New controls: physical5.py Y3 with
mu_l,0's first-order coefficient for mu_l,1's, static5.py S3 with [KI03]'s Q_X and Q_Y exchanged in (4.3); mutants 5/5
and 7/7.

*Notes, accepted.* His Step 2 prints "-8 pi m a(V_1) = v_b", but (8.35) with (8.33) gives +8 pi m a(V_1) = v_b, and
(8.35) prints lambda_b,s1 for lambda_b,v1; the record's sign is the consistent one, and 10.34(b)(2) now says so. Not
checked by the verifier: [Vas13] section 2.7, [Hin26c] section 9.2.3; his direct (8.30) computation of (8.29) (the
extraction's matrix is ambiguous); the tensor and vector equations from a linearized Ricci tensor of its own;
Proposition 7.4 in five dimensions beyond first order; box^C's roots for l > 12. Its runs: physical5 4/4 and mutants
4/4, pairing5 5/5 and 6/6, static5 6/6 and 6/6, response5 all pass; md5 rows matching at 1bc4243.

*Runs.* physical5.py --selftest 4/4 (Y3 in 718 s), --mutants 5/5; static5.py --selftest 6/6, --mutants 7/7;
pairing5.py --selftest 5/5, --mutants 6/6; window5.py as D93 records; paper/response5.py --selftest all pass; Appendix
D's md5 rows current (52, window5.py added).

**D95 (2026-10-24): the forty-fourth verifier's findings on D93-D94, seated.**

One independent verifier read D93 and D94 (306331c, ab2fdd7 against c219c0f), recomputing W1 from det N_L itself with no
cancellation rule, W2 at other iota+ orders and W3 in Cartesian coordinates, and reading [Hin26] pp. 16-17, 28, 32, 34,
37, 85, 92-93, 117, 128, 145, 149, 157-163, 169, 174, 177, 199, 218, 221, 225, 228, 248, 273, 279 and 324 at source.
Verdict: no major finding; every computed claim reproduces; D94's repairs sound. Two minor findings, nine nits, notes.
READ again here at source: [Hin26] pp. 16 ((1.19)), 17 ((1.23)), 28 (the three kinds of root), 31 (Figure 1.7), 149
(Lemma 8.4), 157 (Lemma 8.12), 169 (Proposition 9.4), 228 (Lemma 11.15's proof), 248 (Proposition 11.32's proof).

*Minor 1 (alpha_5 is a reading).* 10.35 gave alpha_5 = 2 and the window [-2, 0], naming one route only to a slower iota+
term, a radiation field with a nonzero late limit. But his index sets at I+ carry the radiative order: E+ "is the
(extended) union of E_I and an index set determined by the pure resonances" ((1.19), p. 16), E-sharp_+ has "smallest
elements (1, 0) and (1 + (1 - e_Ups) gam_Ups, 0)" (p. 248), and "The coupling of (A_h)_{7,4} with u_01 moreover
contributes the index set (1 + (1 - e_Ups) gam_Ups, 0) at I+" (p. 228); in four dimensions these coincide with the
Coulombic 1, in five the same bookkeeping gives alpha_5 = 3/2 + O(gam). Repaired: 10.35 leads with what holds for every
alpha_5 in (1, 2] -- s2, v2, t2 at -2 alone -- gives the window as [alpha_5 - 4, 0], names both readings, and lists what
3/2 adds; window5.py W2 computes it (s2's and s3's class roots just below -2 at k = 0, the class roots just below 0 at
s0 and s1 at k = 2 and just below -1 at s1 and s2 at k = 1, the physical states and the list of order at most 2
unchanged); ROUTES 4.4 and 4.36, README and the paper say so.

*Minor 2 (a root of box^C in the window).* "None from box^C" was false at four-dimensional s0: there det N_L = (1/16)
det N_Ups(lam - 1) det N_C(lam + 1), the surviving 0 is box^C's root 1 shifted by -1, and window5.py's tag "phys" came
from the order in which the cancelled roots were removed. Hintz lists it as 0, without the superscript C (p. 149), and
counts box^C's roots shifted by -1 as the third kind (p. 28). Repaired: W1 takes the roots of det N_L itself, checks
each class root against det N_Ups(lam - 1), and reports which of them are det N_C(lam + 1)'s -- four-dimensional s0's 0
alone, at s1 the same shifted root cancelling, none in five dimensions -- with D93's claim as a second control;
Proposition 10.32(i) and the docstring say so. The first rerun of W1 failed: it counted det N_C(lam + 1)'s roots in the
window rather than those of det N_L, and so found four-dimensional s1's cancelled 0 too; corrected and rerun.

*Nits.* (1) README and the paper had static5.py's mutants at 6/6 and physical5.py's at 4/4: 7/7 and 5/5. (2)
physical5.py's comment "(10.30(ii); D92)" now names Proposition 10.27(ii). (3) Ten bare references in 10.29-10.32 now
name Propositions 10.25 and 10.21; three older wraps beginning "+ " there (one at the margin) rewrapped. (4) The p. 17
quotation is now verbatim: "very large (i.e., very negative) indicial roots". (5) The "+ 1) a'" wrap in Proposition
10.32(iii). (6) Proposition 10.32(ii)'s s2 list ("its class root just below -1 (0) and its -2 (0)"). (7) Proposition 9.4
is on p. 169: 10.35's READ and window5.py; D93's entry stands. (8) Lemma 8.12's -16 pi m is on p. 157: 10.34; D94's
entry stands. (9) W1's tensor-type roots come from lin5.py's det N_L, no longer written in. (10) D94's "(8.34)- (8.35)"
stands as written.

*Notes, accepted.* His Step 2 as modified is solvable near a = 0 because the a-dependent cross entries vanish there: one
sentence in 10.34(b)(2). In four spatial dimensions the mass state r^-2 lies just outside L^2, where for Schroedinger
operators logarithms enter the low-energy resolvent: 10.35(b) now names this as a second reading in the pole order,
cross-referenced with ROUTES 4.4 item 3. W2 matched (9.32) and (9.39a)-(9.39b) term by term; twice the pole order
matches his Remark 11.4 (p. 221, read by the verifier, not here). Not checked by the verifier: [Hin26c]'s admissibility
at n = 4; a five-dimensional (5.28) and whether a (7, 4)-type coupling exists there, which decides how strong Minor 1
is; Proposition 11.16 in full; logarithms at the pole; Proposition 7.4 beyond first order (D96). Its runs: window5 3/3
and 3/3, physical5 4/4 and 5/5, static5 6/6 and 7/7, pairing5 5/5 and 6/6, response5 all pass; md5 rows 52 of 52 at
ab2fdd7.

*Runs.* window5.py --selftest 3/3 (W1 1398 s, beside its mutants; the first rerun failed W1, Minor 2's note), --mutants
4/4; physical5.py changed in a comment only, not rerun.

**D96 (2026-10-24): [Hin26] section 7.2.1 in five dimensions at every spin (10.36, mp5.py).**

M asked to continue; the open piece was the one 10.34(c) and 10.35 made a condition: his Proposition 7.4, Lemma 7.5 and
(7.19) on the full, two-spin Myers-Perry metric. READ at source (alphaXiv, 2026-10-24): [Hin26] pp. 69 (Definition
2.28), 126 (Remark 6.17), 140-144 (section 7.2.1, Lemma 7.5's proof through the coefficients of (3.17), the proof of
Proposition 7.4), 161 (footnote 82); [ER08] pp. 10, 14 ("the solutions belong in the Kerr-Schild class"), 16
((42)-(44)), 19.

*Computed (Proposition 10.33, mp5.py M1-M5).* The five-dimensional Myers-Perry metric in Kerr-Schild form for every spin
matrix A in so(4) at once: P = r^4 + s r^2 + p^2, M = (r^2 + s) I + A^2 (M/P = (r^2 - A^2)^-1 by Cayley-Hamilton), r the
root of Q = P - x^T M x, k = dt + M (r I + A) x . dx / P, H = mu r^2/(P F). (M1) k null on Q = 0; [ER08]'s Pi, F and
g_tt at block form; Tangherlini at A = 0; Ricci-flat exactly at rational points (two spins rotated out of block form by
a Cayley rotation, equal spins, one spin), the jet of g solved to second order in rational arithmetic; Kerr over so(3)
likewise. (M2) Q, P, x^T A^2 M^2 x invariant and M (r I + A) x covariant under so(4) on (x, A), symbolically for each
basis rotation, so delta* V_b = (1/2) L_R g_b = (1/2) D_A g_b([A_b, A_V]); the full identity at the exact points, r
implicit. (M3) Along a ray, D_A g(W) = (2 mu/r^4)(dt + dr) (x)_s V(W) exactly at A = 0, the same leading term at a
two-spin A, the rest from rho^4. (M4) dim ker ad_A = 6, 4 at a = +-b != 0, 2 otherwise; L_R g = 0 on a kernel basis.
(M5) From the Kerr-Schild leading term, dual5.py A3's correction shifted by the pure gauge mu/3 and the same leading
term of h-sharp. Kerr the control throughout. Controls: the even-dimensional H, the bracket reversed, the remainder at
rho^5, two Killing rotations at equal spins, c_0 unshifted.

*Deduced (10.36).* (a) His Lemma 7.5 at every spin, W = [A_b, A_V] for his S', h~_b : so(4) -> rho^4 C^oo, no pure
gauge term at leading order in Kerr-Schild coordinates, on the reading that route B's g_b is SO(4)-equivariant. (b)
His Proposition 7.4 with h-sharp on all of so(4), smooth in b, its leading term 10.31(iii)'s, and (7.19) at
rho^(floor(C_0) + 3) on 10.31(a)'s readings. (c) The Killing rotations jump 6, 4, 2; footnote 82 holds with
lambda-sharp(W) = <v_b, W>, and 10.34(b)'s modified Step 2 stands at every small spin. (d) 10.34(c)'s and 10.35(c)'s
condition is met on those readings. (e) Kerr returns his structure.

*Notes.* (1) The structural reason is the equivariance of the family, which 10.34(b)(2) already used at first order as
his Remark 8.10; what mp5.py adds is the family itself over all of so(4), checked, and the identity on the full metric.
(2) A first attempt checked the identities as rational functions in seventeen symbols and did not finish in ten minutes;
it was stopped (by PID) and the invariance checked on the polynomial building blocks instead. (3) The sign of the
leading term against his -2m depends on the orientation in which A is read as the angular momentum, which is not fixed
here; nothing deduced depends on it. (4) D93-D95's window and D96 together leave of item 2 in five dimensions sections
9-10 and the readings.

*Runs.* mp5.py --selftest 5/5 (M3 157 s, about three minutes in all), --mutants 5/5.

**D97 (2026-10-24): [Hin26] section 9.1 in five dimensions, the pure iota+ resonances (10.37, iota5.py).**

M asked to continue; the open piece was the second channel of alpha_5 that 10.35 left: a pure resonance of the model at
future timelike infinity with real part at most 2 would decay as slowly as the mass aspect. READ at source (alphaXiv,
2026-10-24; printed pages): [Hin26] pp. 16-17 ((1.16), (1.19), footnote 9, (1.20)-(1.22), Example 1.6), 149 (Lemma 8.4),
164-166 (Proposition 9.2 and its proof), 168 ((9.10)-(9.11), Definition 9.3), 170 (Remark 9.5), 172 (Definition 9.6,
Remark 9.7), 180 (Lemma 9.13), 184-185 (Definition 9.19, Lemma 9.21, Proposition 9.22).

*Computed (Proposition 10.34, iota5.py I1-I5).* (I1) The model by type from lin5.py's operators with t* = t - r: M0(D)
G + s M1(D) G = 0, M0 = (x - lam) L1, L1 affine, M1 lin5.py's N itself, the free transport at gam = 0 (L-bar half of
box there). (I2) A connection determinant through z = s/(s + 2), where the Frobenius series at both ends converge at s
= 2: the free 4+1 wave's 3 + l + k to 10^-25 and his u_3 = z^(3/2) exactly; box^C at s0, gam_C = 1. (I3) On box^C at
gam_C = 10 the argument principle counts 4 zeros in [6/5, 9/2] x [-3, 3], exactly 1 + mu + k for det N's upper roots,
and the resonant state's moment obeys N(lam - 1) m = 0 at 1 + mu and vanishes at 2 + mu. (I4) At the record's point det
N_L's roots in (0, 3/2] are box^C's less 1 (s0 1.0000747438, s1 1.0001201950, none at v1); over l <= 400 box^C has no
root in [-100, 2] but the Coulomb 2 at l = 0, 1, and roots in (2, 5/2) at every scalar l (two for 2 <= l <= 135), the
lowest 2 + 2.93 x 10^-6 at l = 2, none at the vector types; the s0 root decreasing inside (2, 5/2) from gam_C = 10^2 to
10^6. (I5) L-bar's s0 candidate is a pure resonance at gam_C = 10 and 100.

*Deduced (10.37).* (a) Towers lam -> lam + 1. (b) The descent: the moment m = int v^-lam G dv obeys N(lam - 1) m = 0,
or m = 0 and the time integral is a pure resonant state at lam - 1. (c) His Proposition 9.2(2)'s injectivity holds
below 1 + eps_ind in five dimensions as in four, on 10.24-10.25's readings. (d) Hence at the record's point every pure
resonance of L-bar below 5/2 sits at a root of box^C's zero energy operator in (2, 5/2), and none has real part at
most 2. (e) Those states are of the constraint kind; on a reading (the injectivity along gam_C in [100, 10^6]) Hurwitz
carries the s0 zero to 2.0000747 at the record's point. (f) The second channel of alpha_5 is closed on the alpha_5 = 2
reading.

*Notes.* (1) A first attempt bridged the two Frobenius series by ODE integration and located zeros by the smallest
singular value; poles of the unnormalized determinant within 5 x 10^-6 of integer-shifted exponents and ill-conditioned
columns made it unreliable, and the z-variable matching replaced it. (2) The builder first split the powers of T with z
= x1 + i x2 symbolic; sympy's expand moved T into denominators and the transport of the degree-p harmonics was lost. The
free-transport check caught it at s1, and it is I1's control. (3) At the record's point, 260 to 480 terms at 40 to 140
digits gave a smooth nonzero determinant at the s0 candidate; it drifted with the number of terms, and convergence needs
some 5 gam_C terms, so it was a truncation artefact and is not reported as a result. (4) The scoping note had the
five-dimensional injectivity bound at 3/2 + eps_ind; his proof gives 1 + eps_ind in any dimension, the bound coming from
Proposition 8.6's zero energy weight. (5) gam_C = 1000 at s0 and gam_C = 10 at s1 were attempted at 100 digits and are
noise-dominated: not used, and the s1 candidate is OPEN. (6) A "pkill -f" with -P (the shell's own children) was issued
in error; it matched nothing; every other process was stopped by exact PID. (7) The forty-fifth verifier's report on
D95-D96 arrived during this work and is seated as D98.

*Runs.* iota5.py --selftest 5/5 (I1 446 s, I2 35 s, I3 516 s, I4 31 s, I5 258 s), --mutants 6/6. Before these, I2 failed
twice and was repaired (a 1 x 1 eigenvalue call returned a nested list; two box^C zeros within 5 x 10^-6 of poles of the
unnormalized determinant, I2 restated on the other root and its tower), I1 once (L-bar's transport is half of box's, his
(8.5)) and I4 twice (a string comparison; the vector types' kappa, l (l + 2) as in damping5.py, not one less).

**D98 (2026-10-24): the forty-fifth verifier's findings on D95-D96, seated.**

One independent verifier read D95 and D96 (a5d581e, defc4c0, 65d2874, a24ab3f against 158c8b0), with its own checks: the
family's Ricci-flatness by 60-digit finite differences at two generic A in so(4) (|Ric| <= 2.4 x 10^-62 against |Riem|
0.03-0.10; a = -b too), the identification with [ER08] (42) by pulling g_A back to Boyer-Lindquist coordinates ((a_1,
a_2) = (-a, -b) to 5 x 10^-51), Lemma 7.5 at generic A and A_V (2 x 10^-51), the Killing dimensions, M3's remainder at
rho^4 (coefficient 0.30717), the asymptotic angular momentum, and W2's rule by hand. READ at source: [Hin26] pp. 1,
16-17, 28-29, 31, 65, 126, 128, 132, 138, 140-144, 149, 156-161, 168, 170, 228, 248, 253; [ER08] pp. 9-10, 14, 16-20.
Verdict: no major finding; five minor findings, seven nits, notes.

*Minor 1 (the orientation).* g_A at A = a J_12 + b J_34 is [ER08] (42) with (a_1, a_2) = (-a, -b); his p. 10 (16) and
p. 14's footnote 4 fix the sense, so A is minus the spin, and in four dimensions mp5.py's Kerr (A x = a x x) has J = -m
a. So W = [A_b, A_V] = -A_(S') for Hintz's S' = a(b) x a(V), and the leading term is his -2m with its sign. Checked
here independently: the standard Kerr-Schild Kerr has a (y dx - x dy)/(r^2 + a^2) in k for J = +m a, mp5.py's k has +a
(x dy - y dx)/(r^2 + a^2). Repaired: 10.33(ii), 10.36(a), mp5.py's M2 docstring and labels, ROUTES 4.37; D96's note (3)
stands as written and is superseded here.

*Minor 2 (stale OPEN lists).* 10.31, 10.32, 10.33, 10.34 and ROUTES 4.32 now carry "(10.36: Lemma 7.5 at every spin
computed; Proposition 7.4 and (7.19) deduced on readings)". *Minor 3 (a page).* Definition 2.28 is on printed p. 65:
10.36's READ, mp5.py, ROUTES 4.37; D96's entry stands. *Minor 4 (where the index sets live).* E_+ and E-sharp_+ are
index sets at iota+, carrying the I+ exponents: 10.35(a), window5.py, ROUTES 4.36; D95's entry stands; the argument is
stronger for it. *Minor 5 (a reading omitted).* The paper now states Proposition 7.4 on readings, an SO(4)-equivariant
family (supplement 10.31(a)).

*Nits.* (1) 10.36(b): a V' replaced by -V(W). (2) 10.36(a) and ROUTES 4.37: the Kerr-Schild dt is the ingoing time, so
dt + dr carries the spin-independent pure gauge mu rho^3 dr (x)_s rho V(W) against his static dt* + dr: "no
spin-dependent pure gauge term". (3) mp5.py: [ER08]'s (31) the class, (42)-(44) the Boyer-Lindquist form. (4) The paper:
the family's derivative, not half of it. (5) "Equal spins" -> a = +-b != 0 in 10.36(c), ROUTES 4.37 and the paper. (6)
10.29's wrap beginning "- 1)" rewrapped with the quotation kept, 10.28's bare 10.20(iii) now Proposition 10.17(iii), and
D95's nit (3) changed eleven references, not ten (D95 stands). (7) ROUTES 4.36's heading now (D93, D95).

*Notes, accepted.* His (7.26) confirms 10.36(a)'s account of his gauge term (m-independent, from varrho^2 = r^2 +
S(a)^2); 10.36(b)'s adjoint condition is consistent with 10.31(i); M5's shift mu/3 is exact; the Killing dimensions
agree with [ER08] section 4.3; D95's reading of alpha_5 and its caution at the threshold are sound. Not checked by the
verifier: Ricci-flatness symbolically; dual5.py's operators; lin5.py's determinants by another route; (7.19) beyond
leading order; route B's g_b in outgoing coordinates; a five-dimensional (5.28) and Proposition 11.16; [Hin26c]. Its
runs: mp5 5/5 and 5/5, window5 3/3 and 4/4, physical5 4/4, response5 all pass; md5 rows 53 of 53 at a24ab3f.

*Runs.* mp5.py --selftest 5/5 after its label and docstring edits (M3 195 s); window5.py's edit is to its docstring
alone (parsed); paper/response5.py --selftest: all checks pass, md5 rows 54.

**D99 (2026-10-24): the forty-sixth verifier's findings on D97-D98, seated.**

One independent verifier read D97 and D98 (92af9b0 against a24ab3f), with its own checks: the model rebuilt from
explicit functions of (t, x1, ..., x4) with Hintz's operators written directly, reproducing iota5.py's M0 and M1
symbolically at box^C s0 and s1, box^Ups s0 and L-bar s0, and the vector types' kappa = l (l + 2); the zeros reproduced
by double-precision shooting (box^C s0 at gam_C = 10) and by high-precision Taylor stepping (L-bar s0 at gam_C = 10, to
19 digits against box^C's root, and the single sign change at gam_C = 100); the descent and the injectivity line by
line; the constraint kind of 10.37(e)'s states (the gauge 1-form about 3 x 10^-2 at gam_C = 10 and 3 x 10^-7 at 10^6);
box^C's roots over l and along gam_C; the terms and digits the connection needs. READ at source: [Hin26] pp. 16-17, 149,
164-170, 172, 180, 184-185; [ER08] p. 14. Verdict: no major finding; three minor findings, eight nits, notes.

*Minor 1 (the l-range).* "One beyond" had lost 10.34(iv)'s l <= 400 and is false for large l: one root in (2, 5/2) for
136 <= l <= 706 and none from 707 -- recomputed here, and now in I4 to l = 711 and at l = 10^3, 10^4, 10^5. Repaired:
10.34(iv), 10.37(d) ("the lowest candidate over l <= 400") and its "What this gives", iota5.py's docstring and I4.
*Minor 2 (the index 0 half).* 10.37(c) had his proof of Proposition 9.2(2) carry over; it carries the injectivity step
(p. 166), not the index 0 step (pp. 167-168, the semiclassical estimate (9.9)), which in five dimensions is a reading
and on which "kernel element => pole" rests -- 10.34(v)'s and 10.37(e)'s "is a pure resonance". READ here at source, pp.
164-169. Repaired: 10.37(c) states the half carried and the reading; 10.34(v), (e), "What this gives", ROUTES 4.38 and
iota5.py say resonant state, and a resonance on that reading; the OPEN lists carry it. *Minor 3 (the paper's
qualifiers).* "And no pure resonance ... t^-2" now reads "at the parameters used and on readings", and "his injectivity"
the injectivity half of his inversion.

*Nits.* (1) iota5.py: I3's zeros are located to 10^-22, as the check asserts. (2) "Where the method reaches (gam_C <=
100)": at gam_C = 10 and 100. (3) 10.37(e)'s path rested on nine points: I4 now checks 201 points of a logarithmic grid
from gam_C = 10^2 to 10^6 -- box^C's s0 root alone in (2, 5/2) and decreasing, det N_L free of roots in (0, 1], its K
lowest roots those with real part <= 0. (4) 10.37(d)'s G1 parenthetical names the fact used: box^Ups's roots near -1 lie
below -1 for z > 0 (at s0 -1 - z/3 + O(z^2)), so their shifts are negative. (5) 10.36(a): [ER08]'s p. 10 (16) and p.
14's footnote 4, not "his"; LOG D98 stands. (6) LOG D98's nit (6) placed its repairs a section early -- the "- 1)" wrap
was in 10.30, the bare 10.20(iii) in 10.29; the repairs are right and D98 stands. (7) mp5.py's M4 label: a = +-b != 0.
(8) 10.34(v): 260 to 480 terms, as LOG D97 has it.

*Notes, accepted.* A pure resonant state is now defined by his (9.17), L1(D) G vanishing one order beyond the outgoing
exponents (p. 169) -- what 10.37(b) uses, and what covers a lam equal to an outgoing exponent (D100 uses it); 10.37(a)'s
(D - lam) G != 0 now rests on the behaviour at v = oo. iota5.py's connection now asserts at every evaluation that the K
lowest roots of det N are those with real part <= 0, the exact root 0 within 10^(-dps/3). The connection needs of the
order of 3 gam_C terms and digits growing with them (900 terms and 400 digits at gam_C = 300), so 10.34(v) and ROUTES
4.38 say millions of terms, and digits to match; LOG D97's "some 5 gam_C" stands. Not checked by the verifier: the s1
and l >= 2 candidates; his index 0 proof in five dimensions; pp. 180 and 184-185 beyond the citations; his section 12;
iota5.py's I1 at v2 and t2 by its own route. Its runs: iota5 5/5 (I1 430 s, I2 33 s, I3 531 s, I4 32 s, I5 276 s) and
mutants 6/6, mp5 5/5, response5 all pass; md5 rows 54 of 54 at 92af9b0.

*Runs.* iota5.py --selftest 5/5 (I1 454 s, I2 34 s, I3 544 s, I4 149 s, I5 296 s) and --mutants 6/6; mp5.py --selftest
5/5 (its M4 label changed); paper/response5.py --selftest all pass; md5 rows refreshed.

**D100 (2026-10-24): [Hin26] (5.27)-(5.28) and Proposition 5.14 in five dimensions (10.38, scri5.py).**

M asked to continue; 10.35 left alpha_5 between 2 and 3/2 + O(gam) for want of a five-dimensional (5.28), and 10.37 had
closed only the pure resonance channel. READ at source (alphaXiv, 2026-10-24; printed pages): [Hin26] pp. 85 (after
Definition 5.2), 91-93 (Definition 5.4, Lemma 5.6, Proposition 5.11, (5.25)-(5.28)), 96-98 ((5.36)-(5.43), Definition
5.13, Proposition 5.14 and its proof), 164-169 (Proposition 9.2 and its proof, (9.11), Definition 9.3, Proposition 9.4,
(9.17)).

*Computed (Proposition 10.35, scri5.py C1-C3).* (C1) sbar5.py's S-bar written in his splitting (5.27) with S^3 is lower
triangular, the same at two points, with his diagonal, his (5, 2) entry and his (7, 4) entry 2 (1 - e_Ups) gam_Ups, and
three trace couplings changed -- (3, 1), (4, 1), (4, 3), (7, 3); in four dimensions, at the trace weight 1, it is his
printed (5.28) at h = 0, all 49 entries. (C2) iota5.py's det L1 by type is the product of 3/2 + (A_0)_ii - x over the
type's slots: s0 1, 3, 4, 7; v1 2, 5; v2 2, 5, 6; t2 6. (C3) At s0, gam_C = 10 and 100, at pi_01's and pi_11's radiative
exponents, and at t2, lam = 3/2, the connection with the exponent's own column is nonzero and continuous through it.

*Deduced (10.38).* (a) The perturbation's entries of A_h and B_h fall half an order in five dimensions (scaling). (b)
Definition 5.2's rates with 3/2 for 1. (c) The (7, 6) coupling and the iteration's quadratic sources reach the
11-component at the Coulombic 2, the mass aspect's; the (7, 4) entry carries pi_01's radiative exponent into pi_11;
F_I,11 in five dimensions. (d) A radiative term reaches iota+ at its own order only through a resonant state there at
that exponent; 10.37(b) holds at such a lam verbatim under D99's definition, and with 10.37(c)-(d) the least iota+ order
is at least 2. (e) alpha_5 = 2 by both channels, on readings, and the window [-2, 0]. (f) Four dimensions, not examined.

*Notes.* (1) The working notes first had his (7, 4) entry as (1 + v_C) gam_C + e_Ups gam_Ups - 2 d_1(r h_01), which is
his (7, 3); the printed matrix (p. 93) and C1's control have (7, 4) = 2 (1 - e_Ups) gam_Ups, the entry his Lemma 11.15's
proof couples. (2) The wrapping helper, run on iota5.py whole, joined a function's lines into a paragraph; the file was
restored from git, the patches reapplied, and only its docstring rewrapped. (3) I4's fine grid first failed: det N_L's
exact root 0 comes out at +-10^-22 at 30 digits; the checks take a tolerance, as the connection's new guard does. (4) A
symbolic det of iota5.py's 4 x 4 M0 ran for minutes; C2 divides M0 by x - lam entrywise first. (5) C3's continuity check
first asked 10^-12 relative and failed at gam_C = 100, where the determinant's noise is 10^-11 -- its differences at lam
+- 10^-15, 10^-25 and 10^-40 all of that size and of either sign, against 3 x 10^-15 at gam_C = 10 -- so it asks 10^-9.
(6) The forty-sixth verifier's report arrived during this work and is seated as D99; the forty-seventh reads D99-D100.

*Runs.* scri5.py --selftest 3/3 (C1 54 s, C2 250 s, C3 409 s) and --mutants 4/4 (about nine minutes); paper/response5.py
--selftest all pass; md5 rows 55, scri5.py added.

**D101 (2026-10-24): the forty-seventh verifier's findings on D99-D100, seated.**

One independent verifier read D99 and D100 (28fbe64 against ef1ae32), with its own checks: his matrix recomputed from
the linearized gauge-fixed operator built from his Definitions 4.1-4.2 and (4.13), applied in Cartesian components to
e^(k (t - r)) r^-x times explicit frame fields -- all 49 four-dimensional entries against his printed (5.28), the
five-dimensional ones at two points; C2's slots from the pointwise a' term; C3's values at gam_C = 10 by a Frobenius
expansion in s and Taylor stepping, to 15 digits at s0 and identical at t2; the l-range by exact Sturm counts in (2,
5/2]; his pp. 87-96 and 228 for 10.38(a); 10.37(b) at lam equal to an outgoing exponent. READ at source: [Hin26] pp.
81-83, 85, 87, 93, 167-169, 223, 228. Verdict: no major finding; three minor findings, five nits, four notes.

*Minor 1 (four trace couplings).* C1 and 10.38 said "three trace couplings changed" and listed four, (3, 1), (4, 1), (4,
3) and (7, 3); the verifier's own route gives those four as the only entries that differ from his. Repaired: "four" in
scri5.py's docstring, Proposition 10.35(i), 10.38's "What this gives", README, ROUTES 4.39 and the paper (twice); LOG
D100 stands. With its note: which entries differ is slot 3's normalization -- the record takes the coefficient of r^2
g-slash, tr-slash/3, where his pi_C has (1/2) tr-slash (Definition 5.2, p. 85, READ here). In his, row 3 scales by 3/2
and column 3 by 2/3, so (3, 1) and (7, 3) become his and only (4, 1) and (4, 3) differ, by (1 - e_C)(1 + v) gam_C/3 and
(1 - e_C)(1 - v) gam_C/6 -- checked here by hand from C1's entries, and now said in 10.35(i) and ROUTES 4.39. *Minor 2
(page numbers).* 10.38's READ, ROUTES 4.39 and LOG D100 cited printed pp. 91-93 for Definition 5.4, section 5.2's
opening and Lemma 5.6, which are on p. 87 (PDF p. 91); printed p. 91 is Corollary 5.10. READ again here: p. 87 holds
Definition 5.4, Lemma 5.6 and (5.11), pp. 92-93 Proposition 5.11. Repaired in 10.38 and ROUTES 4.39; LOG D100 stands.
*Minor 3 (a reading at K+).* 10.38(d)'s "Its term solves the homogeneous model ... So it is a resonant state" also needs
nothing below order 2 fed into iota+ from K+, so that at v = oo the least term carries E_K's exponents alone; on
10.35(c)'s bookkeeping the zero energy and pure gauge states enter at K+ order alpha_5 or are eliminated as his are, so
the conclusion stands, on that reading. Repaired: (d) names it, (e) lists it among its readings, and 10.38's and ROUTES
4.39's OPEN lists carry it.

*Nits.* (1) iota5.py's I4 asserted "not two" for 136 <= l <= 400 but not "one", which 10.34(iv) states; it now asserts
one root in (2, 5/2) at l = 0, 1 and for 136 <= l <= 400, and the docstring's (ii) says so. (2) 10.35's OPEN list now
points to 10.38(d) for a radiation field's late limit, and 10.35(a)'s "has been written (D95)" to 10.38. (3) 10.38(d)'s
t*^(x0 - 2): up to logarithms. (4) README said "All forty-five" against 47 programs -- off by two since before D99 --
and its log range D1-D75; now forty-eight with aug5.py, and D1-D102. (5) scri5.py's docstring: about nine minutes for
the mutants, as LOG D100 has.

*Notes, accepted.* (1) C3's determinant is about 7 x 10^-12 at s0 because two E_K exponents nearly coincide (0 and
-1.33 x 10^-6, the smallest singular value 1.2 x 10^-6), so the test relative to the grid is the meaningful one;
10.38's proof now says so. (2) His own identification, "A_h = A_0 = S-bar_(E-bar^Ups, E-bar^C) in the notation of Lemma
8.2" (p. 223, Proposition 11.6(1)), and (8.8), p. 146 -- READ here -- are now in 10.38's setting and READ. (3) The
paper's sentence and Appendices A-D matched the record but for minor 1. (4) His (9.17) reads "(v d_v - 1 - S-bar) h in
A^(E^tot_(iota+,I) + 1)" (p. 169, READ here); 10.37's definition is its five-dimensional form, 3/2 for his 1. Not
checked by the verifier: C3 at gam_C = 100 by a second method (one column took 572 s at 130 digits); lin5.py's model
matrices beyond L1; 10.24-10.25's readings; his pp. 27-29, 248 and 273; Proposition 11.16 in five dimensions. Its runs:
scri5 3/3 (C1 55 s, C2 262 s, C3 396 s) and mutants 4/4; iota5 5/5 and mutants 6/6; mp5 5/5; response5 all pass; md5
rows 55 of 55 at 28fbe64.

*Runs.* iota5.py --only 4 (218 s, the new assertion passing) and --mutants 6/6 (about fifteen minutes); scri5.py's
changes are its docstring's; paper/response5.py --selftest all pass; md5 rows refreshed.

**D102 (2026-10-24): [Hin26] section 10.1 in five dimensions, the augmented zero energy operator (10.39, aug5.py).**

M asked to continue; ROUTES 4.4 route B item 2 carries [Hin26] to five dimensions step by step, and section 10 --
2-admissibility -- is the next. READ at source (alphaXiv, 2026-10-24; printed pages): [Hin26] pp. 145 (Lemma 8.1,
(8.2a)-(8.2b), (8.5)), 199-205 (Theorem 10.1, (10.1)-(10.9b), Remark 10.2, footnotes 96-97, Lemma 10.3 and its proof,
Lemma 10.4 and its proof to (10.18)), 207-209 ((10.23), (10.24a)-(10.24c), Lemma 10.5, (10.26), Proposition 10.6 and its
proof, Proposition 10.7 with (10.28)-(10.32)), 211-212 ((10.36)-(10.41), Remark 10.8, Lemma 10.9), 214 ((10.46)-(10.48),
Lemmas 10.10-10.11).

*Computed (Proposition 10.36, aug5.py A1-A3).* (A1) On 4+1 Minkowski with sbar5.py's E^Ups and E^C, the gauged mass
state r^-2 (dt^2 + dr^2) + delta*(r^-1 (a dt + b dr)) and rotation state 2 r^-4 dt (x)_s w + delta*(p r^-3 w), p = -4
gam_Ups/3, in closed form, solve L-bar g-dot = 0 at the symbolic point (X1, 0, X3, 0), every parameter symbolic, with no
logarithm; in four dimensions the mass state's gauge 1-form needs c log r dt, the logarithm of his (8.19). (A2) [L-bar,
T] g-dot is nonzero and of degree -3 and -4 (four dimensions -2 and -3, his (10.9a) and (3, 0)), and [[L-bar, T], T]
g-dot = 0. (A3) L-bar(chi(r/T) g-dot) is of iota+ order 4 and 5 (four dimensions 3, his borderline, and 4, his
(10.24b)).

*Deduced (10.39).* (a) Every five-dimensional entry of (10.5) is in A^3, from 10.28's orders and Lemma 8.1's structure,
g^00 in rho^2 C^oo. (b) Such an entry lies in the target space for alpha_sf + 2 < 1, so on (0, eps_ind); his criterion,
o(r^-2), is the same in both dimensions. (c) His (10.24a) serves every state -- chi_K g-dot and chi_K h^(<=1)_s1, L_b of
them of iota+ order 4 -- and Lemma 10.4 holds with his proof: no improved states. (d) Proposition 10.6 from 10.32's
pairings. (e) Proposition 10.7 and Theorem 10.1, 2-admissibility with alpha_sf + 2 in (0, eps_ind), on readings. (f) No
logarithm in the augmentation; whether the resolvent has one at sigma = 0 is his section 11's question.

*Notes.* (1) The first ansatz for the four-dimensional mass state's gauge 1-form, r^0 (a dt + b dr), has no solution: 0
is an s0 root of box^Ups(0) there (10.28), and the log r dt term his (8.19) carries is needed; in five dimensions the
ansatz with log r admitted returns the log coefficients 0. (2) A1 first checked L-bar g-dot = 0 at three numerical
points, which proves it for the mass state, invariant under SO(4), but not for the rotation state; it now checks at the
symbolic point (X1, 0, X3, 0), which meets every orbit of the rotations of the planes 12 and 34. (3) A first run
substituted the parameters into the states before the operator was applied, which left the operator's own symbolic; they
are substituted after. (4) The forty-seventh verifier's report arrived during this work and is seated as D101; the
section was first numbered D101.

*Runs.* aug5.py --selftest 3/3 (A1 15 s, A2 183 s, A3 301 s with the controls, about eight minutes) and --mutants 4/4
(about four minutes); paper/response5.py --selftest all pass; md5 rows 56, aug5.py added.

**D103 (2026-10-24): the forty-eighth verifier's findings on D101-D102, seated.**

One independent verifier read D101 and D102 (8ab8e22 against 4c144f1), with its own checks: L-bar rebuilt in Cartesian
components from his (8.1), (6.5) and (7.3) without sbar5.py or aug5.py; the gauged states' closed forms (5D mass a, b;
5D and 4D rotation p; the 4D mass's c and b), the log coefficients 0 in five dimensions at r^0 log r and at r^-1 log r,
the residuals of L-bar g-dot zero at eight generic five-dimensional and five four-dimensional points, the degrees of A2
and A3 at two parameter sets, and the leading matrix of [L-bar, T] on r^-k U, whose eigenvalues are (n - 1)/2 - k + spec
S-bar to 2 x 10^-14 in both dimensions; the target space arithmetic; D101's slot 3 arithmetic. READ at source: [Hin26]
pp. 113, 135, 145-146, 149, 154, 164, 169, 199-209, 212-216, 223, 234. Verdict: no major finding; four minor findings,
four nits, notes.

*Minor 1 (the boosts' cut-off order).* 10.39(c) said L_b of chi_K g-dot or chi_K h^(<=1)_s1 is of iota+ order 4 and that
(iii) computes it; (iii) computes the mass state's only -- no boost state is built on the model, where it vanishes --
and 10.39's OPEN list had the boost entry by computation open. Repaired: (c) says the mass state's order is computed and
the boosts' deduced; ROUTES 4.40 likewise. *Minor 2 (the cut-off's place).* The paper's "the states cut off near
timelike infinity" read as inverted: chi_K is 1 near K+ and vanishes near I+ and for t* <= 1 (his p. 203). Repaired:
"cut off to vanish near future null infinity". *Minor 3 (a qualifier).* The paper's "Nor does the zero energy
augmentation need Hintz's improved states" now reads "Nor, on readings, does". *Minor 4 (two readings not named).* His
Theorem 10.1's proof takes the representation (10.4) from the Paley-Wiener argument of [Hin26c] Theorem 12.2's proof (p.
200) and adapts [Hin26c] section 14.1 (pp. 201, 212); both are now among 10.39(e)'s readings, its OPEN list and ROUTES
4.40's.

*Nits.* (1) aug5.py's five-dimensional log ansatz sat at r^0 log r, not at the gauge 1-form's own power r^-1; it is now
r^-(n-3) log r -- r^-1 log r in five dimensions, log r in four, as before -- and A1 passes, the log coefficients 0 (the
verifier checked both powers). (2) 10.39(i): "takes p = -2 gam_Ups and none" now reads "with no logarithm, as in his
(8.20)". (3) A parenthesized (10.28) could be his equation or this record's section: 10.39 now says a bare 10.n is a
section here and a parenthesized (10.n) one of his equations, and writes "section 10.28(a)-(b)" and the like where both
meet. (4) 10.39(b)'s 7.3846 x 10^-8 is the bound 10.24(a) computes for his (8.13) at l <= 12, the record's number, not
his; said so.

*Notes, accepted.* (1) The trace weight 2/(D - 2) of E^C is derived in the record (U2, damping5.py), and the verifier
re-derived it; E^Ups's 2/3 is the record's choice made as E^C's is (10.15), and A1's closed forms depend on it. (2) His
p. 202: "It is via inverting the iota+-normal operator ... that one can both improve the iota+-decay rate and obtain the
correct asymptotics at I+"; the chi_K route does not do this -- 10.39(c) now says so, with whether his section 11 needs
those asymptotics open. (3) His p. 208: "h*_b,s0 has O(r^-2) decay (as do all other dual states in (7.15))". (4) His
(8.8) (p. 146) and Proposition 11.6(1) (p. 223) as D101's note 2 has them. Not checked by the verifier: scri5.py;
dual5.py and pairing5.py; the eleven-state kernel count; the boost states; the naive (10.5) claims; his section 11; his
Definitions 5.2 and 5.4 and (5.28) (D101's p. 85 READ is this session's); the 7.3846 x 10^-8. Its runs: aug5 3/3 (A1 20
s, A2 216 s, A3 313 s) and mutants 4/4; iota5 --only 4 True; response5 all pass; md5 rows 56 of 56 at 8ab8e22.

*Runs.* aug5.py --selftest 3/3 (A1 23 s, A2 316 s, A3 354 s with the controls, about eleven and a half minutes on a
loaded machine) and --mutants 4/4 (about five minutes) after nit (1); paper/response5.py --selftest all pass; md5 rows
refreshed.

**D104 (2026-10-24): [Hin26] section 10.2 in five dimensions, 2-admissibility with no sf-loss (10.40, lowfreq5.py).**

M asked to continue; after section 10.1 (D102) the proof of his Theorem 10.1 itself, his section 10.2, is the next step
of ROUTES 4.4 route B item 2. READ at source (alphaXiv, 2026-10-24; printed pages): [Hin26] pp. 25 (the Fourier
transform convention, Figure 1.5), 54-55 (Definition 2.19, Lemma 2.20), 60 ((2.25a)-(2.26b)), 199-201 (Theorem 10.1,
(10.1)-(10.4), Remark 10.2), 212-217 (Lemma 10.9 and its proof, (10.45), Lemmas 10.10-10.13, (10.46)-(10.64), the end of
the proof of Theorem 10.1), 225 (Corollary 11.10, Theorem 11.12's opening).

*Computed (Proposition 10.37, lowfreq5.py W1-W2).* (W1) For a piecewise cubic chi, 1 on [0, 1/4] and 0 from 1/2, C^1 at
its joints, the zero-frequency integrals at r = 2 of d_T(chi(r/T) g-dot) and of d_T^2(chi(r/T)(T h + h')) are g-dot and
h exactly; aug5.py's mass state is of degree -2 (four dimensions -1), from its components, so the weights of the states
g-dot and h_s1 in r^alpha L^2(r^(n-1) dr) are below 0 and 1 (four dimensions -1/2 and 1/2, his (10.51) and (10.52)).
(W2) Section 10.2's weight arithmetic at 598 rational points of alpha_sf + n/2 in (0, eps_ind): five dimensions
alpha_sf + 1, alpha_sf + 2, the final alpha_sf, loss 0; four dimensions his -1/2 - eps, 1/2 - eps, -3/2 - eps and loss
alpha_sf + 3/2 + eps.

*Deduced (10.40).* (a) His Lemmas 10.9-10.11 lossless as his, on readings. (b) Lemma 10.12 in five dimensions: d_t*
g-dot^aug in A^(oo,3,oo) and d_t*^2 h^aug in A^(oo,4,oo), tf orders 2 and 3, weights 0 and 1 against r^3 dr; the radial
threshold at R_out, with Remark 10.2's margin, binds -- alpha_sf + 1 at s' = s and alpha_sf + 2 at s' = s - 1. (c) Lemma
10.13 twice gives u in H^((s-1;k),(alpha_sf,-2)): (10.3) with no loss, every delta >= 0, or every delta > 0 if [Hin26c]
Definition 5.13 asks it. (d) His (10.52) as printed, at s' = s, would need s < -1 + eps at R_out, where Remark 10.2
gives s < -3/2 - alpha_sf; his proof uses (10.52) only through (10.63), at s - 1, where it holds -- a reading, recorded
and not more. (e) His Corollary 11.10 and Theorem 11.12 carry delta; his section 11 is not examined.

*Notes.* (1) sympy does not integrate the piecewise chi to infinity, nor over (1, 8); W1 integrates the explicit cubic
over the transition [4, 8] at r = 2, where chi(2/T) varies, and checks chi C^1 at its joints, so that the second
derivative carries no delta there. (2) W2's grid is five eps_ind, ten alpha_sf and twelve eps; 598 of its 600 points
have eps below both margins, and the two others are skipped. (3) Section 10.40 first cited 10.39 parenthesized, which
10.39's own convention reads as his equation; it now says "section 10.39".

*Runs.* lowfreq5.py --selftest 2/2 (W1 5 s, W2 under 1 s) and --mutants 3/3 (about 3 s); paper/response5.py --selftest
all pass; md5 rows 57, lowfreq5.py added.

**D105 (2026-10-24): the forty-ninth verifier's findings on D104, seated.**

One independent verifier read D104 (2567ab5 against 2a90dc7) with its own checks: the zero-frequency integrals with a
different step at r = 1/3, 2 and 7 over the whole transition; the chain of weights re-derived from his text with the scf
requirement from (2.25a) in each dimension; the reading of (10.52); md5 rows 57 of 57. READ at source: [Hin26] pp. 21,
34, 53-55, 60, 199-200, 202-205, 209, 212-217, 225-226. Verdict: the conclusion holds on readings, with more room than
stated; one major finding, four minor findings, seven nits.

*Major (the mechanism).* D104 took the requirement at R_out, "s' + alpha' < -1/2", as a condition of Lemma 2.20 and kept
it in five dimensions, so that "the radial threshold binds". It is not Lemma 2.20's -- Plancherel, with no threshold (p.
55) -- but the scf weight of his columns: (2.25a) gives the scf order min(beta_I, beta_iota) - eps (p. 60), his (10.54)
has I+ order 1, and his p. 216 has "the requirement on r here is that r < -1/2 at the zero section R_out" for (10.56)'s
scf order 1 - eps; his p. 206 makes the same link, "r + alpha_sf + 1 < 3/2 - eps" for the scf order 3 - eps. Checked
here at source (pp. 60, 206, 215-217). In five dimensions the augmentation chi_K g-dot has no I+ term, the scf weights
are 1 - eps and 2 - eps against |dx|, the requirements s' + alpha' < 1 and < 2 hold at s' = s, and the columns carry the
states' own weights -eps and 1 - eps; the initial weights (10.61)-(10.62) set the bound, and u_sing is at alpha_sf as
before. Repaired: lowfreq5.py W2 reads both weights from (2.25a) -- a column of iota+ order q and I+ order beta_I has tf
weight q - 1 - n/2 and scf weight min(beta_I, q) - n/2, less eps -- and returns his values in four dimensions, -eps, 1 -
eps (also at s' = s) and alpha_sf in five, and, with I+ terms at the radiative order 3/2, alpha_sf + 1 - eps, alpha_sf +
2 - eps and a loss of eps; a third control holds D104's alpha_sf + 1 and alpha_sf + 2 and is caught. 10.40's setting,
Proposition 10.37(ii), the proof, (b)-(e) and the closing paragraph, ROUTES 4.41, README, and the paper's sentence and
Appendix A are rewritten; "binds" is gone.

*Minor.* (1) "r^alpha L^2(r^(n-1) dr)", read literally, is the opposite convention; the code used his, rho^alpha L^2 =
r^-alpha L^2, and the text and the code's comment now say so. (2) "p. 25" for Figure 1.5 was the PDF page; the printed
page is 21 (its header "KERR 21", read here). (3) Lemma 10.13's independence of the dimension is shown for s = 0; for
variable orders his proof refers to [Hin26c] Lemma 14.6 (p. 217), now in 10.40(c) and its OPEN list. (4) W1's weight for
h_s1 is the mass state's plus 1, h_s1's order 3 being 10.28's and not measured; said so.

*Nits.* (1) "His loss is the r^-1 tail" now names both columns and their I+ order. (2) 10.40(e) carries (c)'s Definition
5.13 hedge. (3) [Hin26c] Theorem 12.2 is back on the OPEN list. (4) The paper's Appendix A bullet now says that the time
derivatives of the columns have the states as zero-frequency values. (5) The paper's Appendix C row for settling read
10.3-10.29 (Propositions 10.1-10.26); now 10.3-10.40 (Propositions 10.1-10.37). (6) 10.39(e)'s sf-loss now points to
10.40. (7) W1 has a negative control: a ramp chi, C^0 only, under which the second integral is -3h'/8, not h.

*Notes.* Not checked by the verifier: [Hin26c] (Definitions 5.11 and 5.13, Lemmas 3.9 and 14.6, (13.30a), Theorems 9.16,
12.2 and 14.2); Lemma 10.9 line by line; printed p. 201; the 10.39 readings; response5.py --full. Its runs: lowfreq5.py
2/2 and mutants 3/3; response5.py all pass; md5 rows 57 of 57 at 2567ab5.

*Runs.* lowfreq5.py --selftest 2/2 (W1 5 s, W2 under 1 s) and --mutants 5/5 (about 3 s); paper/response5.py --selftest
all pass; md5 rows refreshed.

**D106 (2026-10-24): [Hin26c]'s readings behind 10.40, at source (10.41, lowfreq5.py W3).**

M asked to continue. Section 10.40 rested on [Hin26c] at n = 4 for Definition 5.13's delta, (13.30a), Lemmas 14.6 and
3.9, and the Paley-Wiener argument and section 14.1 that [Hin26]'s proof of Theorem 10.1 follows; this step reads them.
READ at source (alphaXiv, 2026-10-24; printed pages): [Hin26c] pp. 8, 20-21, 56-59, 106-107, 233, 235, 252, 255,
262-267. [Hin26c] is written on Kerr in 3 + 1 dimensions, so each is READ at n = 3.

*Read.* Definition 5.13: "Let aleph >= 0 and alpha_sf in R, delta >= 0" -- delta = 0 is admitted, and Remark 5.14's
relaxed version, with margin d and loss s - d, is [Hin26]'s (10.3). (13.30a): "The shift of 3/2 in the decay orders at
rho^-1(0) = scf cup tf is due to the passage from mu to mu_b", with L^2(X, mu) = rho^(3/2) L^2(X, mu_b). Lemma 14.6: at
s = 0 an estimate in t at each fixed r; general s through an elliptic t*-translation-invariant 3b-parametrix. Theorem
12.2's Paley-Wiener argument: in t* alone, on Theorems 9.41, 9.16 and 9.5(6). Theorem 14.2, the template: the loss from
u_0 in rho C^oo through Lemma 14.5's condition (14.16).

*Computed (Proposition 10.38, lowfreq5.py W3).* The density shift n/2 -- 3/2 at n = 3, 2 at n = 4 -- from the thresholds
of r^-a in L^2(r^(n-1) dr) and L^2(r^-1 dr); (13.30a)'s rule reproduces his p. 206 (two instances), p. 216 ((10.56)) and
(10.59), and gives 10.40(b)'s five-dimensional requirements and weights. Controls: the shift 3/2 at n = 4; no shift.

*Deduced (10.41).* (a) 10.40's conclusion holds with sf-loss 0 in Remark 5.14's sense (margin 1), the hedge on delta
removed; 10.40(c) and (e) now say so. (b) (13.30a) at n = 4: the shift computed, the microlocal part of Lemma 13.13 a
reading. (c) Lemmas 14.6 and 10.13 at s = 0 hold at every n; general s rests on the 3b-calculus ([Hin23d], not read).
(d) The Paley-Wiener argument rests on the readings of 10.19-10.20; section 14.1's loss comes from the zero energy
state's decay, as 10.40's does. (e) Still readings at n = 4: Lemma 3.9, Lemma 13.13's microlocal part, the 3b-calculus,
Theorems 9.5, 9.16 and 9.41; 10.40's OPEN list now says so.

*Runs.* lowfreq5.py --selftest 3/3 (W1 5 s, W2 and W3 under 1 s) and --mutants 7/7 (about 4 s); paper/response5.py
--selftest all pass; md5 rows refreshed.

**D107 (2026-10-24): the fiftieth verifier's findings on D106, seated.**

One independent verifier read D106 (5d0a56c against 541e310) with its own checks: every quotation in 10.41's READ
re-read at source in [Hin26c] (pp. 8, 20-21, 45-46, 55-60, 106-107, 158, 172-173, 198, 200-201, 227-228, 233, 235,
247-248, 252-253, 255, 260-267, 277) and [Hin26] (pp. 199-200, 206, 208, 210, 212, 215-217); the density identity at n =
3, 4, 5, the thresholds, the rule's instances and (14.16) at n = 3 and 4 by its own sympy script; md5 rows 57 of 57.
Verdict: D106 stands; no major finding; two minor findings, five nits, notes.

*Minor.* (1) 10.41(c), its OPEN list, ROUTES 4.42 and LOG D106 put Lemma 14.6's general-s step on [Hin23d]
(arXiv:2302.13803); the class Psi-tilde_3b of (3.27) is built on the scaled bounded geometry calculus, "the scaled
bounded geometry perspective introduced by the author in [Hin26c]" (pp. 45-46) -- in [Hin26c]'s own references P. Hintz,
*Pseudodifferential operators on manifolds with scaled bounded geometry*, CAMS 6 (2026) 153-243 (p. 277) -- with
[Hin23d] named only for "the proof of the boundedness of a 3b-ps.d.o. on 3b-Sobolev spaces" with smooth coefficients (p.
46). Checked here at source. Repaired: 10.41's READ (c), (c), closing paragraph and ROUTES 4.42 name the paper and its
key; its section 3.1 is set "on an n-dimensional manifold". (2) Proposition 10.38's first sentence held only near
infinity: on all of R^n no power of r is in either space. Repaired: "near infinity (|x| >= 1)", there and in
lowfreq5.py's docstring.

*Nits.* (1) "three printed instances" now "four printed instances, at three places". (2) (14.16)'s quotation had
"s|_(R_out)" inside the quote marks; it now transliterates his subscript. (3) The rule's r < -1/2 - eps for every eps is
his r < -1/2; said so in Proposition 10.38, and W3's shift() comment says it brackets the threshold. (4) The paper
grouped p. 8 with "the setting"; it is the sf-loss, and 10.41's READ now quotes pp. 8 and 106-107. (5) The shift
alpha_sf + 3/2 -> alpha_sf + 2 is 10.23(ii)'s, as applied in 10.24(d).

*Notes, accepted.* (1) Parts of [Hin26c] are written in general n -- section 3.1 (p. 46), section 13.1's b-spaces (p.
247), Definition 9.4 (p. 158) -- so "written on Kerr in 3 + 1" is its subject, not every section; 10.41's setting now
says so. (2) The Paley-Wiener argument also needs the spectral family invertible for Im sigma >= 0, mode stability
(10.27); 10.41(d) now says so. (3) Theorem 14.2's loss passes through one t*-integration (m = 1); 10.41(d) says so. Not
checked by the verifier: 10.40 and W1-W2 beyond the pointer edits; whether [Hin26]'s section 11 needs delta > 0 for
other reasons; the calculi at n = 4; Theorems 9.5, 9.16 and 9.41 at n = 4; 10.27. Its runs: lowfreq5.py 3/3, mutants
7/7; response5.py all pass.

*Runs.* lowfreq5.py --selftest 3/3 (W1 5 s, W2 and W3 under 1 s) and --mutants 7/7 (about 4 s); paper/response5.py
--selftest all pass; md5 rows refreshed.

**D108 (2026-10-24): [Hin26] section 11.1 in five dimensions, admissibility and forward solutions (10.42, cone5.py).**

M asked to continue; after section 10 (D102-D107) his section 11 is the next step of ROUTES 4.4 route B item 2, and its
section 11.1 makes [Hin26c]'s main result available. READ at source (alphaXiv, 2026-10-24; printed pages): [Hin26] pp.
218-226, 231, 244, 263; [Hin26c] pp. 107, 109, 201, 228.

*Computed (Proposition 10.39, cone5.py C1-C3).* (C1) 1/(t* r^n) = rho_I^n rho_+^(n+1) rho_K for [Hin26c]'s (11.4): the
b-density shifts (n/2, (n+1)/2, 1/2), his (11.5) at n = 3 and (2, 5/2, 1/2) at n = 4; beta_+ in (1/2, 1/2 + eps_ind) at
both; his delta > beta_+ - 1/2 is Theorem 10.1's; the radiation field's I+ order -1/2 against |dt dx| at both, so beta_I
< (n - 1)/2 + S-bar: 1 and 3/2. (C2) Mass, rotation and boost differences of degrees -2, -3, -2 along rays (four
dimensions -1, -2, -1). (C3) Ric of g = eta + M r^-(n-2) (dt + dr)^2 with M = mu_0 + d F(r/t): zero for F constant, the
linear part of degree -n and supported where F varies, the quadratic of degree -(2n - 2), no cubic.

*Deduced (10.42).* (a) E+ from (2, 0), min Re E+ >= 2, with 10.38's alpha_5 = 2. (b) Lemma 11.5's l_+ < 2, Definition
5.15's l_+ <= 1 binding. (c) Proposition 11.6 on 10.38's (5.28) at h = 0; Corollary 11.9's P(g0, g0) in rho_+^4 C^oo.
(d) Corollary 11.10 with l_+ in (0, 1), l_K in (2, 2 + eps_K]. (e) Theorem 11.12 with delta = 0 and beta_I in (beta_+,
3/2): u in H^(k, beta_I, beta_+, -3/2)_b.

*Notes.* (1) C3's first test took the part linear in d, which also carries mu_0 d terms, as one homogeneous piece and
failed; graded by order in the deviation (M = eps(mu_0 + d F)) the pieces are homogeneous of degrees -n and -(2n - 2).
(2) C1's first formula for the top of beta_I added 1/2 twice and failed against his 1; the threshold alpha_I < -1/2
shifted by n/2 gives 1 and 3/2.

*Runs.* cone5.py --selftest 3/3 (C1 under 1 s, C2 2 s, C3 7 s) and --mutants 3/3 (about 6 s); paper/response5.py
--selftest all pass; md5 rows 58, cone5.py added.

**D109 (2026-10-24): the fifty-first verifier's findings on D108, seated.**

One independent verifier read D108 (58655de against 1ca71df) with its own checks: every quotation of 10.42 re-read at
source ([Hin26] pp. 218-226; [Hin26c] pp. 107, 109, 201, 226, 228); the density identity for symbolic n and the
b-density Jacobians at the I+/iota+ corner and in the interior of iota+; the three background differences in
five-dimensional Cartesian coordinates, each uncut term with linearized Ricci zero, and the cut-off terms' linearized
Ricci of degrees -4, -5, -4; chi_K = chi_0(t*) chi_1(r/t*) read at [Hin26] p. 318; md5 rows 58 of 58. Verdict: D108
stands; no major finding; three minor findings, four nits, a note.

*Minor.* (1) Proposition 10.39(i), labelled computed, and cone5.py C1, README, ROUTES 4.43 presented the top of beta_I,
3/2, as computed; only the radiation field's I+ order is, the threshold of [Hin26c] (10.2) at n = 4 is a reading, as
10.42(e) already said. Repaired: 10.39(i) states the reading; C1's docstring, comment and label, README and ROUTES 4.43
likewise. (2) The paper's "every order at timelike infinity one higher than his": the admissibility weight l_+ is
bounded by Definition 5.15 and beta_+'s interval is his. Repaired in the paper: "the background's orders at timelike
infinity one higher than his", in its settling paragraph. (3) The paper's Appendix A, README and ROUTES 4.43 put "the
patched background's curvature of order 4" under cone5.py; C3 computes the cut-off mass interpolation, the rotation and
boost being deduced. Repaired in all three; 10.42(c) now gives the deduction, his own count (g - g-bar in rho_+^2 C^oo,
d in rho_+ V_b, so Ric in rho_+^4 C^oo), which the verifier confirmed with its own linearized computation.

*Nits.* (1) 10.42(d)'s aleph = 2 cited sections 10.28-10.29 only; the 2-admissibility is deduced in 10.39-10.41(a), now
cited beside them. (2) (d)'s l_+ in (0, 1) is a subset of what (b) admits, (0, 1]; harmless, kept. (3) C1's control
swapped one hard-coded tuple and was caught only by comparison with another; repaired: the identity is now checked with
the shifts themselves (exponents twice the shifts), so the control fails at the identity, at n = 4, and downstream. (4)
Timings 3 s and 8 s against the log's 2 s and 7 s; machine variance.

*Note.* [Hin26] Theorem 13.1 has (1, 1) in E+ in four dimensions; 10.42(a) leaves the logarithmic content of E+ in five
dimensions to the later sections, consistent with 10.28's "no logarithm". Not checked by it: [Hin26] pp. 231, 244, 263
and (8.7) at source; 10.38, 10.40 and 10.41's internal derivations; the quadratic curvature of the rotation and boost
cut-offs (order 6 or more by the count).

*Also.* `render_pdf.py` joined a list item's continuation lines only at three spaces of indent, so every wrapped bullet
of a paper indented by two split into a bullet and a stray paragraph; it now joins at two, its selftest carrying the
case, and takes the page title from the paper's first heading. The paper's sections 8-9 were arranged at M's direction
of 2026-10-24 and the arrangement withdrawn the same day at M's next direction (D110); only the repairs above are in the
paper.

*Runs.* cone5.py --selftest 3/3 and --mutants 3/3; render_pdf.py --selftest PASS; paper/response5.py --selftest all
pass; md5 rows refreshed.

## M's words, 2026-10-24

**2026-10-24, after the fiftieth verifier's report and the question how close the counterpart paper is, verbatim:**

> Work the extended work into the paper as support for the commissioned work. Tell me the criteria that separates the
> work from being proven. Tell me the title again, so I may consider it. The paper will be published to my webpage
> later today in another session that handles the webpage build. Yes, render the PDF for my review

**2026-10-24, during that arrangement, verbatim:**

> The nonlinear route is only partly built. It has computed and deduced the inputs of Hintz's method in five
> dimensions through his section 11.1 (sections 10.13–10.42). Many steps there rest on reading his four-dimensional
> arguments as holding in five dimensions. - the warp session, which needs this work, says that we need to finish the
> extended nonlinear works

**2026-10-24, next, verbatim:**

> The work has to be finished first and then fully built into the paper

**D110 (2026-10-24): the arrangement withdrawn; the remaining route planned (ROUTES 4.44).**

The paper's sections 8-9 had been arranged as asked (a supporting section 8 with Table 8.1 and a section 8.5 on what
separates it from a proof, a condensed section 9, the abstract and section 1.3 pointing to them). M's next direction
puts the work before the paper, so the arrangement is withdrawn and not committed; the draft and its PDF are kept
outside the tree, and the paper carries only D109's repairs. The criteria that separate the extended work from a proof,
as they were set out for M: readings of [Hin26], [Hin26a] and [Hin26c] at n = 4; parameter points and finite ranges (one
gauge point, h below an h_0 his proof does not make explicit, l <= 12); steps not carried (section 11.2 on, section 12,
section 13, section 5's exterior theorem); computations on the Minkowski model with the transfer deduced; the linear
route's steps taken in Hung's shape with constants not tracked; and the global step from Theorem 1's domain to a Cauchy
surface of the exterior. ROUTES 4.44 orders the work that removes them, the class reduction first.

No five-dimensional nonlinear stability theorem for Tangherlini exists to shorten the route: a search of the literature
(alphaXiv, 2026-10-24, recency first) returned linear, Riemannian and numerical work only.

**D111 (2026-10-24): A1, the class in [Hin26]'s construction (10.43, class5.py).**

M asked to continue, with as few PRs as possible and in record time; the title is to be reconsidered when the work is
finished. ROUTES 4.44's A1 first: what of Hintz's states, parameters and steps survives in the T^2-mirror class. READ at
source (alphaXiv, 2026-10-24; printed pages): [Hin26] pp. 63, 219, 301-302, 310, 312, 321-322.

*Computed (Proposition 10.40, class5.py C1-C2).* Of the fifteen Killing fields of 4+1 Minkowski only d_t is G-invariant
(T^2 alone: three); the mass change is invariant; one invariant scalar and one invariant TT tensor harmonic at each even
l, none at odd l, no invariant divergence-free 1-form (l <= 8).

*Deduced (10.43(a)-(e)).* Equivariance of P with the radial modifications of 10.14-10.15; b = (m, 0), S = 0, no S_1 or
V_l component; Steps 2 and 5 absent, Step 4 the mass alone; only the mass's kernel state and the time translation's dual
state, the s0 generalized state, the even scalar pure gauge classes, and the s2 and t2 physical states remain; the
iteration on the G-fixed subspaces, on a reading of Theorem 12.8's proof checked at A7.

*Notes.* (1) The tensor count first ran by substituting the polynomial ansatz into the symbolic Laplacian and clearing
denominators through the rational parameterization; it took minutes per degree. It now imposes each equation exactly at
48 rational points of the circle, more than twice its degree as a trigonometric polynomial: seconds. (2) A kill of the
slow run by pattern matched its own shell and ended it; processes are killed by exact PID only. (3) The axis smoothness
conditions change no count, the polynomial ansatz being regular already; the controls that bite are the reflections
dropped (two divergence-free 1-forms appear) and the eigenvalue moved by one.

*Runs.* class5.py --selftest 2/2 (about thirty seconds) and --mutants 3/3.

**D112 (2026-10-24): A2, [Hin26] section 11.2 in five dimensions (10.44, iplus5.py).**

READ at source (alphaXiv, 2026-10-24; printed pages): [Hin26] pp. 47, 49-50, 57-58, 86, 181, 224-230, 235. His b-ODE
lemmas are stated for any compact manifold with corners and any number of parameters, so they hold with S^3.

*Computed (Proposition 10.41, iplus5.py P1-P3).* The I+ normal operator's leading part -(rho_I d - (n - 1)/2)(rho_I d -
rho_+ d), 3/2 at n = 4; the exceptional exponents 2 and 3/2 + (1 - e_Ups) gam_Ups, his reproduced at I0 = 1;
non-resonance for gam_Ups != 1/4; the gap at the point.

*Deduced (10.44(a)-(e)).* (11.26), (11.34) and the I+ index sets in five dimensions; Lemma 11.15, Propositions 11.14 and
11.16; E_+ with min Re 3/2 + (1 - e_Ups) gam_Ups, so that 10.42 (pointer added to its (a)) no longer needs 10.38's
readings for E_+.

*Notes.* (1) P1 first compared the plain wave operator with his L_0 and found a remainder of order rho_I^-1 with a
factor 3 for every n; his L is -box/2 to leading order, and with that normalization the remainder is rho_I R exactly.
(2) lin5.py's point uses its own symbols (v, eC, gC, eU, gU) with no assumptions; they are mapped to sbar5.py's by name.
(3) The first mutants of P2-P3 changed a matrix whose diagonal both dimensions share, and were not caught; the exponents
are now functions of the leading exponent I0, and I0 = 1 is the control.

*Runs.* iplus5.py --selftest 3/3 and --mutants 3/3 (seconds).

**D113 (2026-10-24): A3, [Hin26] sections 11.3-11.6 in the class (10.45).**

READ at source (alphaXiv, 2026-10-24; printed pages): [Hin26] pp. 23, 218-219, 221, 231-262. His Steps 1-4 build the
low-energy part u_reg + g-dot + h_s1 and integrate twice because of the boost's second order pole; in the class the
boosts and translations have no G-fixed element (10.43), so h_s1 = 0 and the four steps are one.

*Deduced (10.45(a)-(e)).* Propositions 11.17 and 11.32 with one integration; Step 2 void; Proposition 11.34 and
Corollary 11.46 with u~ of K+ order alpha_K - 1 on f of K+ order in (1, 1 + eps_K); h needed to K+ order 1 + eps_K + eps;
the iota+ orders 3/2 + (1 - e_Ups) gam_Ups - eps for u~ and 5 + 2 (1 - e_Ups) gam_Ups - eps for f.

*Notes.* Nothing computed: the reduction is the equivariance of 10.43 applied to his proofs. iplus5.py's three lines
over 121 characters are wrapped.

**D114 (2026-10-24): A4, [Hin26] sections 11.7-11.8 in the class (10.46, sharp5.py).**

READ at source (alphaXiv, 2026-10-24; printed pages): [Hin26] pp. 218, 221, 263-266, 274-294, 302. His Step 6 eliminates
the pure gauge terms of K+ order at most 2 (p. 289, "(so <= 2)") and records every term below 4 + eps_K; a root mu fed
by t*^-alpha at iota+ gives K+ order alpha - mu (footnote 124).

*Computed (Proposition 10.42, sharp5.py K1-K4).* The class's types and roots; for every iota+ exponent in [3/2 + (1 -
e_Ups) gam_Ups, 3] the eliminated terms within s0 e0, s0 c0, s2 e0, the recorded within these and s2 c-1, no physical
state; his eight parameters and his physical s2, v2, s3, v3 reproduced at alpha = 1 in four dimensions; his weights in
the five-dimensional gaps.

*Deduced (10.46(a)-(e)).* Proposition 11.51 with the mass alone; Theorem 11.59 with u_exp the mass change and four pure
gauge terms, u~ of K+ order 3 + eps_K; h needing K+ order 3 + eps_K; Corollary 11.66 with q-vec the mass and those four;
10.45's OPEN weight l_I settled as his 3 + eps_I.

*Notes.* (1) The elimination rule is his "(so <= 2)": eps_K lies below every class root's distance (about 10^-6 here),
so a class root at alpha = 2, of order 2 + 10^-6, is recorded rather than eliminated; window5.py's W2 at alpha = 2 lists
s0's and s1's class roots among the eliminated, labelled "at 2 + eps" -- a difference of convention, his p. 289
deciding. (2) K2's run is about eight minutes, nearly all in lin5.py's scalar-type determinant; caching it across l did
not shorten it, and the cache was removed. (3) In the class no physical state is recorded at any iota+ exponent above 1,
so the late-time expansion below K+ order 3 + eps_K is pure gauge apart from the mass.

*Runs.* sharp5.py --selftest 4/4 and --mutants 4/4 (about nine minutes each).

**D115 (2026-10-24): the fifty-second verifier's findings on D111 seated.**

The fifty-second verifier confirmed C1 and C2 by an independent count (ambient polynomials on R^4, exact ranks), the
sampling argument exact (the cleared numerators' trigonometric degree at most 14 at l = 8, against 48 points), and (a),
(b)'s A = 0, (d) and (e)'s labelling at source. Seated:

- Major: 10.43(c) said Steps 2 and 5 are absent; only their modifications vanish. Step 2 now reduces to Proposition
  11.20 with S-dot = 0 and no augmentation #1, Step 5 to Proposition 11.51 with no S_1 shifts and no modifications
  (10.46(a)); 10.45(b), ROUTES 4.45 and 4.47 and the README follow. D111's LOG entry stands as written.
- 10.43(b): b - b0 and b_rem keep their mass component, (u^0_lam, f_lam) and h-tilde their G-fixed parts; the S_l-even
  statement is now about the S_l and V_l components.
- The tensor count's completeness: class5.py C3 (new, stdlib) counts the harmonics a second way, as homogeneous
  polynomials on R^4 with ranks modulo 2^31 - 1, whose nullities bound the counts from above; the totals are SO(4)'s and
  the G-invariant counts meet C2's lower bounds, which are therefore exact.
- T^2 alone is now counted, not exhibited: two divergence-free 1-forms at each odd l, and two TT tensors at every even l
  from 2 on (C3's control, which sees more than one solution); x.H = 0 dropped is a second control.
- 10.43(e): the scheme runs for P o Psi, Psi(U) = (chi_-(t*) h_(-S), 0, 0) + Phi(U), with D_S(h_(-.))(S') in its
  assumption (3): absent in the class, S = S' = 0; h_0's invariance needs (13.5)'s uniqueness (A8); (12.34) and (13.6)
  to be READ at A7.
- Pages: Definition 2.27 spans pp. 63-64; chi_K = chi_0(t*) chi_1(r/t*) is p. 318 (both READ at source today). Nits: Pi
  is a bounded projection, of norm 1 for G-invariant norms; tensors "at each even l >= 2" in ROUTES 4.45 and the README;
  the ansatz degree floor(l/2) + 1; chi_- and chi_+ named in (a).
- Noted, not adopted: the verifier's second route for A7 -- if Phi is G-equivariant on all of D^oo, the G-average of U'
  solves (12.35) with the same estimates -- recorded in 10.43's OPEN line.

*Runs.* class5.py --selftest 3/3 (about forty seconds) and --mutants 5/5.

**D116 (2026-10-24): A7, [Hin26] section 12 in the class (10.47); the route's labels.**

READ at source (alphaXiv, 2026-10-24; printed pages): [Hin26] pp. 182-186, 295-297, 301-302, 304, 310, 312, 315-317,
321.

*Deduced (10.47(a)-(e)).* The class's data space: the mass, the G-fixed iota+ data, the mass remainder and the tail; his
conormal gauge remainders at 3 + eps_+ belong to the tail, the class's K+ threshold being 3 + eps_K. Phi is
O(4)-equivariant on all of D^oo -- every step of his construction is canonical (the inverse of the iota+ normal
operator, Res_iota+ of (9.56), Corollary 9.18's contour integral, the unique expansions at R = 0, the unique
modification parameters, cut-offs in t* and r) -- so Theorem 12.3 holds in the class with K+ order 3 + eps_K, and
Theorem 12.8's read-off, starting from Corollary 11.66's unique solution and using Proposition 9.22's explicit right
inverse, gives a G-invariant U': 10.43(e)'s reading is deduced, and the fifty-second verifier's averaging route is not
needed.

*Notes.* (1) ROUTES 4.44's plan numbers his section 11.3-11.6 as A3-A5, sections 11.7-11.8 as A6 and section 12 as A7;
ROUTES 4.47 and 4.48 had labelled D113 and D114 "A3" and "A4". Their headings now read A3-A5 and A6, and their "Next"
lines follow; D113's and D114's LOG entries stand as written. (2) 10.43(e) now points to 10.47(c)-(e). (3) Nothing
computed here: the five-dimensional inputs are Propositions 10.34 and 10.40-10.42.

**D117 (2026-10-24): A8 and A9, [Hin26] sections 5 and 13 in five dimensions in the class (10.48, 10.49); Phase A
complete.**

READ at source (alphaXiv, 2026-10-24; printed pages): [Hin26] pp. 2-3, 84-110, 318-323. His section 5 builds on [Hin23a]
(p. 84: "The setup, estimates, and arguments are very similar to those in [Hin23a]"; Theorem 5.17's proof "the same ...
as that of [Hin23a, Corollary 3.36]"), a reading ROUTES 4.44 had not listed; it is B10.

*Deduced (10.48(a)-(e)).* In five dimensions every I+ exponent is at least 3/2, so the simplest space of Theorem 5.17
carries no radiation-field term for 1 < l-flat_I < 3/2 ((5.25)'s 2 l-flat_I <= 3 holds); Theorem 5.21 needs min Re E_0 >
3/2 + 2 gam_Ups, which admits the r^-2 mass change exactly when gam_Ups < 1/4; in the class S = 0, h_0 = h, G-invariant
-- closing 10.47(e)'s open item.

*Deduced (10.49).* Theorem 13.1 in five dimensions in the class: G-invariant partially polyhomogeneous data near
Tangherlini of mass m_0 settle to Tangherlini of a nearby mass at t*^(-2-eps_K) in spatially compact sets, on the
readings of 10.13-10.48, [Hin26a], [Hin26c] and [Hin23a]. This completes Phase A of ROUTES 4.44.

*Notes.* (1) 10.48(c) first said that no weak null structure enters in five dimensions and cited 10.38(a) for it;
neither was checked, and the sentence now says only that the radiation fields sit at r^(-3/2) and that nothing uses it.
(2) 10.49(a)'s cross-references are 10.15-10.18 for Proposition 6.12's inputs and 10.24-10.25 for Proposition 8.6's,
checked against the section headings. (3) Nothing computed in D116-D117; the fifty-third verifier, on D112-D115, is
still running.

**D118 (2026-10-24): Phase C deduced (10.50).**

Phase C was taken before Phase B because it decides whether the route connects to the record's own solution at all. It
does, on readings: after the shell, {v > v_end}, every oscillating profile vanishes -- W is proportional to env, env = 0
there (mu' = (2/9) A^2 env^2, mu constant for v >= v_end), Lemma 6.2's oscillating stage data are built from W and
earlier oscillating parts, and Lemma 5.3(c)'s transports run along ell, on which v is constant -- so the approximant
there is Tangherlini(mu_end) plus smooth lam-independent means times powers of lam, and its data on a tau-slice after
the shell are small in every unscaled norm Theorem E controls. Beyond the bounded Omega the data are glued
G-equivariantly to exact Tangherlini; the result is a compactly supported perturbation, Hintz's Theorem 1.1 case, inside
10.49's hypotheses.

*Notes.* (1) Theorem E is stated at k = 6, which is [DS23]'s lower bound k > 4/2 + 1 (section 4); Hintz's iteration
needs H^d smallness for a large d, so Theorem E must be rerun at higher order (C-i). (2) The gluing's obstruction space
is the G-invariant Killing initial data; Proposition 10.40(i) leaves d_t alone, matched by the mass (C-ii). (3) Nothing
computed here.

**D119 (2026-10-24): Phase B begun; C-i discharged (10.51).**

Theorem E at every order: the record's section 4 uses k = 6 only through Lemma 2.1's scaled L^inf bounds, the L^inf/L^2
split of Step 4's commutator terms and [DS23]'s condition k > 4/2 + 1, all of which hold at every k >= 6 with
k-dependent constants; the bootstrap closes when 2K - 5 >= K + 1, whatever k is. The inputs at order k come from Theorem
A (5.4) and from Proposition 6.5, whose bound sup_r ||d_r^j U||_{H^s} <= C_(j,s) lam^(N-2-j) holds at every order with
lam0 independent of it. So 10.50(d)'s H^d smallness holds once k >= d and K >= d + 1.

*Notes.* (1) [Hin26c] states (Remark 5.6, printed p. 101) that it works in 3 + 1 dimensions for concreteness and refers
to [Hin23c] section 3.1.2 for general dimension; some of its results (Corollary 9.39, Proposition 9.40) are stated for
general n. Its audit, and one of [Hin26a] and [Hin23a], are running as background reads; their reports are claims to be
checked at source, not discharges. (2) The fifty-third verifier, on D112-D115, is still running.

**D120 (2026-10-24): B8 discharged (10.52).**

eind5.py E1-E2 computes, at the record's point, that every indicial root of L is simple for every l >= 2 -- exactly, the
scalar, vector and tensor types -- and that his (8.13) holds for every l with eps_ind at most 1.94137 x 10^-8: an exact
certificate puts box^C's upper scalar and vector roots right of Re lam = 51 for every l >= 10^4, and a 30-digit scan
over l < 10^4 finds the least distance from Z, at l = 50, box^Ups's root near 1 - l. Section 10.52 (Proposition 10.43)
deduces [Hin26] Lemma 8.4 in five dimensions at the point for every l.

*Notes.* (1) The first run covered the scalar and tensor types only; 10.24's vector type carries box^C's quadratic,
which was added to E1 and E2 before anything was written, with the same bound. (2) The bound is attained at the edge of
(8.13)'s |lam| <= 50 and so depends on that cutoff; he uses (8.13) only for |lam| <= 4. (3) Selftest 2/2 (about four
minutes), mutants 2/2.

**D121 (2026-10-24): the fifty-third verifier's findings on D112-D115 seated.**

One major finding: sharp5.py K3's bookkeeping rule was stated for every iota+ exponent, and at his alpha = 1 it would
record the physical s2, t2 and s4 e-2. Repaired by deducing the class's iota+ index sets (10.46, new paragraph): his
E_+'s (1, 0) is the Kerr parameter change and E-tilde_+'s (1, 0) u (1 + E_ind) the boost, both absent in the class,
where the mass change enters at rho_+^2; so every iota+ exponent the class's sources carry is at least alpha_min, K3's
hypothesis, now stated in sharp5.py and 10.46(ii). Minor findings, all seated: 10.44's READ page for Definition 11.3 (p.
220); Proposition 10.41's exponent 2 = 2 I0 - 1 rests on 10.38(a)'s scaling, a reading, and is so labelled (iplus5.py
P2, ROUTES 4.46); the gap's upper end is 63999567/128, checked exactly (P2); P3 now applies L_0 with the full A_0 to the
seven-component ansatz, with a control; 10.45(d)'s iota+ requirement on f is 3 + min Re E_+ - eps = 9/2 + (1 - e_Ups)
gam_Ups - eps, D113's figure having been (L - L_b) u's order (ROUTES 4.47); 10.43's C3 upper bound justified (a TT
eigentensor extends to a harmonic homogeneous polynomial, G-equivariantly) and its doubled end mark removed.

*Notes.* (1) sharp5.py K3 and K4 and iplus5.py rerun after the repairs: pass; mutants unchanged. (2) The response
paper's "(D1-D108)" is stale; it is rebuilt in Phase D.

**D122 (2026-10-24): the companion papers audited for their dimension; the plan for B1-B4 and B10 (ROUTES 4.55).**

Two background readers audited [Hin26c], and [Hin26a] with [Hin23a], for where the dimension enters. Neither paper is
written for general dimension, but the analysis under each is, and the items split three ways: by citation, by a short
argument at n = 4 from the record's computed inputs, and real work (ROUTES 4.55). One finding was applied at once:
[Hin26a] has no Theorem 7.1, and 10.49(a)'s label now reads [Hin26] Theorem 7.1, his summary of [Hin26a]. One finding
shortens B10: [Hin23a] Theorem 3.35 peels off the radiation field, which five dimensions does not carry, so [Hin26] p.
102's first step suffices there. The readers' claims are not discharges; each is to be checked at source.

**D123 (2026-10-24): B1-B2 at source -- [Hin26c] section 9 at n = 4 (10.53); B5 restated.**

Read at source: [Hin26c] section 9 is written for general n (Definitions 9.3-9.4; Theorem 9.38, Corollary 9.39 and
Proposition 9.40 carry n), and the n = 3 numerals elsewhere in it (Theorems 9.36 and 9.41, Corollary 9.43, Definition
5.13(2), Theorems 10.1 and 11.1) come from the b-density alone, so at n = 4 they become the record's alpha + 2.
Bundles are "purely notational" at source. Section 10.53 records this; B1-B2 are discharged but for Theorem 9.16's
proof at n = 4. [Hin26a]'s h_0 is itself non-explicit (Theorems 4.9, 6.2; Remark 6.3), so B5 is restated (ROUTES
4.56): the record's point computations are to be made uniform in h at its e_C.

*Notes.* (1) The fifty-fourth verifier is running on D116-D122; 10.53 is outside its range. (2) Nothing computed here.

**D124 (2026-10-24): B5 discharged, B6 deduced -- every small h, not one point (uniform5.py, 10.54).**

[Hin26a]'s h_0 is not explicit (D123), so the five-dimensional statement wanted is his: at the record's e, every
sufficiently small h. uniform5.py H1-H2 proves exactly that box^C's indicial roots avoid [-100, 2] but for the simple
Coulomb root at l = 0, 1, for every h in (0, 10^-6] and every type and degree: damping5.py U4's line-crossing
certificate with h a second parameter, the crossing polynomials' critical values in h (leading coefficient in kappa,
value at kappa_0, discriminant in kappa) having no root in (0, 10^-6]. Section 10.54 (Proposition 10.44) deduces his
Theorem 4.9 in five dimensions for every such h, sorts the record's other point computations into those that inherit,
those free of h or improving as h falls, and those holding off a countable set, and deduces the horizon threshold for
every small h.

*Notes.* (1) The certificate's counts are reported right | between | left, 10.12's convention. (2) The deduction in
10.54(c) rests on the record's own statements of which quantities grow with gam_C; the fifty-fifth verifier is to check
it. (3) Selftest 2/2 (about twenty seconds), mutants 2/2.

**D125 (2026-10-24): B9 discharged; B4, B7, B10 deduced at source (transfer5.py, 10.55-10.57).**

transfer5.py computes five-dimensional Tangherlini in Kerr-Schild form, exactly: its connection is two orders below
Minkowski's (mu G_3 + mu^2 G_5), g^00 = -4 mu rho^2 with t* = t - r, and the damping 1-forms with the static time differ
from Minkowski's at r^-3. Section 10.55 deduces the transfer (B9) -- every operator differs from its model in rho^4
Diff_b, one order better than four dimensions -- and B7: the kernel class (10.53(c)), the interior uniqueness by the
radial systems' regular singular point at the horizon, the index 0 at nonzero frequency on Theorem 9.16's reading.
Sections 10.56 and 10.57 read [Hin26a] section 5.2 and [Hin23a] section 3 at source: the first takes only symbol data
from the metric, all computed in five dimensions, leaving the commutators' signs as the one reading; the second is
needed only near a piece of I+ for compactly supported data, its h-dependent couplings drop into the error term at
r^-(3/2), and its peeling theorem is not needed.

*Notes.* (1) transfer5.py: selftest 2/2 (about four minutes), mutants 2/2. (2) The fifty-fourth verifier's report
arrived while this was written; D126 seats it.

**D126 (2026-10-24): the fifty-fourth verifier's findings on D116-D122 seated.**

Verdict PASS with one major finding: Phase A was called "complete" while 10.45(e) and 10.48(c) rest on Phase B readings.
Repaired in 10.49 and ROUTES 4.51 ("10.48" named here in error; D129): complete conditional on its readings, B1-B4, B10
and 10.45(e)'s [Hin26c] Proposition 13.18 and Corollary 13.17 at n = 4 (D117's wording stands in its entry as written
then). Minor findings, all seated: k = 6 is Step 4's floor, not [DS23]'s, which asks k > 3 (ROUTES 4.53; D119's wording
likewise stands); 10.46's quotation of [Hin26] p. 221 made verbatim; the trace weight 2/(D - 2) cited as the record's own
derivation (damping5.py U2), [Hin26a] (3.2) having weight 1 (ROUTES 4.55); eind5.py and 10.52 state that l = 0 and 1 are
10.24(iv)'s; the --only summaries of eind5.py, sharp5.py, uniform5.py and transfer5.py count the checks run. Nits: ROUTES
4.55's -n + 2 + beta attributed to Corollary 9.39, its Theorem 11.1 clause made grammatical; 10.50(f)'s K >= d + 1.

*Notes.* (1) The verifier recomputed 1.94137 x 10^-8 from the closed form z l/(2 (l + 1)(2 l + 1)) at l = 50 and checked
E2's certificate numerically at 61 kappa up to 10^15 kappa*. (2) It did not check C-ii's gluing or Lemma 6.2's
oscillating data, nor anything after d479898.

**D127 (2026-10-24): B3 deduced at source; (2.27), the iota+ spectrum, 10.38(a) and C-ii closed (10.58-10.59).**

[Hin26c] sections 5, 7, 8, 10, 11 and 13 read at source: section 7's estimates use the principal symbol and the
thresholds only, (2.27) is Minkowski algebra, (5.7)'s "1" is (n - 1)/2, and every other n = 3 numeral is a density
shift, rho_I^n rho_+^(n+1) rho_K at n = 4. [Hin26] Proposition 2.25 is stated on R^n, which discharges 10.46(e)'s
(2.27). The iota+ resonances between 5/2 and 3 + eps_+ need no location (sharp5.py K3 sweeps the interval); 10.38(a)'s
exponent is at least 2 > alpha_min under either reading; and [CD03] is dimension-free, so the gluing of C-ii needs only
the Tangherlini mass family and is G-equivariant by uniqueness. Phase B now leaves one kind of reading, named in ROUTES
4.59: the analytic estimates of the companion papers at n = 4 given five-dimensional symbols.

*Notes.* (1) Nothing computed here. (2) The fifty-fifth verifier is running on D123-D126.

**2026-10-24, after the paper was rebuilt (d13d9a3), verbatim:**

> Settling only has to hold within your symmetry class. - the warp session asks that we include the asymmetry class as
> well

**D128 (2026-10-24): the general class planned (ROUTES 4.60).**

Theorem 4 is stated in the T^2-mirror class, which is what settling needs. M relays the request to include the general
class as well: perturbations with no symmetry, whose development should settle to a boosted, centred, slowly rotating
Myers-Perry black hole near Tangherlini. Read against the record: sections 10.13-10.42 and Phase B used no symmetry (the
states, pairings, rigidity, window and Lemma 7.5 were computed for all of so(4) and S_1); the class entered at 10.43,
where it removed his boost, rotations and centre-of-mass motions, made the zero energy pole first order, and fixed the
final parameter to the mass. What it left is ROUTES 4.60's Phase E: the inputs at every b near b0 in the Myers-Perry
family (where [Hin26] takes them at each b from [AHW24] and [Hin26a]), his Lemma 8.15 on the non-Killing rotations, the
low-energy structure with the boosts, his sections 11.3-11.8, 12, 5 and 13 with the full parameters and two orders of
loss at K+, and the gluing to the boosted Myers-Perry family ([CD03] Remark 8.2 names the one missing element). READ for
the plan ([Hin26], alphaXiv, 2026-10-24; printed pages): p. 5, Remark 1.4, "The mode stability result of
Andersson-Hafner-Whiting [AHW24] for linearized gravity holds in the full subextremal range and is used here as a black
box"; p. 25, the zero energy nullspace "is 7-dimensional ... spanned by (i) linearized Kerr metrics ... (ii) deformation
tensors ... of asymptotic translations", with the boosts' generalized states, "a second order pole at sigma = 0, and thus
forward solutions of L_b lose two powers of t*-decay"; p. 144, section 8's parameters "b = (m, a) that are close to
subextremal parameters b0"; p. 154, Proposition 8.8's proof, "By [AHW24, Theorem 6.1(1)], we obtain u = delta*(sigma)
omega", at each b.

**D129 (2026-10-24): the fifty-fifth verifier's findings on D123-D126 seated.**

Verdict: PASS on the computed claims -- uniform5.py 2/2 and mutants 2/2, with an independent 150-digit spot check at h
= 10^-6, 10^-9, 10^-12, 10^-15 and l up to 10^4 (no non-Coulomb root in (-100, 2], the counts at all 34 sampled l);
transfer5.py 2/2 and mutants 2/2, Ricci flatness at four more random rational points -- and PARTIAL on the deductions.
One major finding: 10.54(c) listed 10.38 among the uses of gam_C-proportional quantities through lower bounds only,
where 10.38(iii) is a non-resonance computed at gam_C = 10 and 100 and OPEN at the record's gam_C; repaired (10.38
dropped from the list, its status stated; B5 does not rest on it). Minor findings, all seated: the top-weight parts
are h^3 (kappa - lam^2)^3 and h (kappa - lam^2), only their roots free of h (10.54(a), damping5.py U3's docstring);
the scalar type 0 quartic's leading coefficient h^2 added to -h^3, -h (10.54's proof, uniform5.py); (8.13) holds at
each h with its own eps_ind(h) > 0, the record using only eps_ind > 0 (10.54(d)); transfer5.py T2's homogeneity,
tested at one point, is now exact, G_j(s x) = s^-j G_j(x) as rational functions of x, r and a scale s (10.55's proof);
"10.44(i)" for the lower-triangular A_0 and its gap corrected to 10.44(ii) at two sites (the proposition numbers are
the record's sequential ones: 10.44's section holds Proposition 10.41, 10.54's Proposition 10.44); [Hin26c] p. 168's
quotation given its qualifier "when S = 0 and Q = 0"; D126's "10.48" corrected in place to 10.49 and ROUTES 4.51;
eind5.py's docstring on l = 0 and 1 reworded (simplicity at l = 0 and 1 and (8.13) at l = 1 from 10.24(iv), the scan
covering l = 0 and l >= 2). The quotations the verifier could not retrieve were retrieved here at source (alphaXiv,
2026-10-24): [Hin26c] (5.10) and (5.13) (p. 103) carry "rho d_rho - 1 - S", Definition 5.13(2) (p. 106) "tf-admissible
with weight alpha_sf + 3/2", Corollary 9.43 (p. 200) as quoted, proved through Theorem 9.41 and the index of (9.18);
[Hin26a] p. 60 ("M is an n-dimensional manifold of bounded geometry") and p. 65 (the density identity) as quoted; and
[Hin23a]'s "a radiation field" is p. 9's, Theorem 3.35's improvements being (3.63)-(3.64), 10.57's READ (4) restated
so. Nits: 10.46's paragraph reflowed so that no line opens with "0)". Not checked by it, and not by this entry:
10.54(b) line by line, 10.55(c)'s pole orders at r_h, commits 634eb63 and d13d9a3 (the fifty-sixth reads those).

**D130 (2026-10-24): E1-E2, the inputs at every b near b0 (10.60).**

[Hin26] takes mode stability and the zero energy count at each Kerr parameter from [AHW24]; the record had them at
Tangherlini alone. READ at source (alphaXiv, 2026-10-24): [HHV21] (arXiv:1906.00860v2) pp. 6, 14, 90, 92-98 -- the
perturbative route from Schwarzschild to slowly rotating Kerr, and its p. 14, "we expect the linear stability of
higher-dimensional Schwarzschild black holes ... and their perturbations, slowly rotating Myers-Perry black holes [MP86],
to follow by similar arguments"; [Hin26] pp. 5, 122-124, 136, 144, 153-154, 200-201, 208-209; [Hin26c] p. 157. Deduced:
high energy uniformly near b0 (the conditions at b0 strict, normal hyperbolicity stable), intermediate frequencies by
continuity, low energy by the eleven states against the kernel's upper semicontinuity and his Propositions 10.6-10.7,
whose proofs use only Proposition 8.11 and Lemma 8.12; E2 by 10.34(b) and 10.36. Nothing computed.

**D131 (2026-10-24): E3-E6, [Hin26] sections 11-13 and 5 without the class (general5.py G1, 10.61-10.62).**

READ again for the boosts (printed pages): [Hin26] pp. 25, 40, 76-81, 108-110, 218-221, 231-294, 296-323, Theorem 13.1's
"(1, 0), (1, 1) in E_+" and its proof's weakest terms. Computed (Proposition 10.46): the bookkeeping over every type with
threshold 4 -- six classes eliminated, fourteen recorded, the physical s2, v2, t2 at -2 with no companion and only while
alpha <= 2; his four-dimensional lists reproduced. Deduced: his six steps with the boosts and rotations (the index sets
at iota+ with min Re alpha_min, the boost's logarithms absent by 10.28), Definition 12.1's full U, Theorems 12.3, 12.8,
5.23 and 13.1 in five dimensions without the class. The tensor type's physical state t2 is the one new kind, recorded by
a parameter beside his S_2, V_2. OPEN: the logarithms at (2, 1) and K+, covered either way.

**D132 (2026-10-24): E7, the gluing to the Myers-Perry family; Phase E complete on its readings (general5.py G2,
10.63).**

[CD03] Remark 8.2 (p. 36): "The argument below carries over to any dimension, the only element missing is an equivalent
of Proposition F.1 for the family of translated, rotated, and boosted Myers-Perry metrics". READ (alphaXiv, 2026-10-24):
pp. 34-38, 72, 75-77 (Theorem 7.7, Theorem 8.1 and its proof, the reference family's condition 4, (E.5b), (E.9), Appendix
F, Proposition F.1, (F.4)-(F.6)). Computed (Proposition 10.47): the charges' Jacobian at Tangherlini, diagonal, E = 3 pi
mu/8, J = (pi mu/4) W, P = -E v, E C = E c, determinant (3 pi/8)(pi mu/4)^6 (3 pi mu/8)^8; four dimensions reproduces
(F.4)-(F.6). Deduced: Proposition F.1's equivalent near Tangherlini (inverse function theorem), the gluing of the data of
g_lam after the shell, perturbed without symmetry and with (E.9)'s parity, to a translated, rotated and boosted
Myers-Perry metric, and its development settling to Myers-Perry at O(t*^(-2-eps_K)). general5.py: selftest 2/2 (seconds),
mutants 2/2.

**D133 (2026-10-24): the fifty-sixth verifier seated (10.58-10.63 and the paper).**

Its report: the computed claims pass (general5.py G1-G2 re-derived by its own ADM quadrature on S^3 and by hand
bookkeeping; transfer5 T2, response5 R1-R8, all 65 md5s), the READs it checked match, 10.58-10.62's deductions sound.
One major finding, checked at source ([CD03] pp. 35-38, 72-77, alphaXiv 2026-10-24) and seated: 10.63(b) had the second
fundamental form's parity backwards. (E.9) is stated on the spacetime metric under x^mu -> -x^mu, time included, so its
3 + 1 form bounds gamma^- and k^+; (8.1) as printed has K^-, which boosted Kerr, p. 38's reference family, would fail,
and (E.9)'s Kerr value alpha_- = 2 is that of Kerr's even K; we read (8.1) with k^+. G-invariance gives gamma^- = 0, not
k^+ small. Found in seating it: on 10.50's tau-slice tau = t - mu/r + O(r^-3), so the unperturbed data's k is even at
r^-3, alpha_- = 2, the borderline (E.9) excludes; the gluing moves to a Cauchy surface Sigma'' that is the tau1-slice
near the hole and a static slice far out, where k = 0, [Hin26]'s own initial surface near infinity (his section 5.7.1),
and Theorem 4(ii) is restated on Sigma'' with [CD03]'s condition, alpha_- > 2. Minor findings seated: the glued member's
charges lie in a small ball about the data's (Remark 8.4); Remark 13.2 covers the member's mass and spin, its boost and
translation lying in 10.49's class (E_0 may contain 2 + N); the charge map's smoothness from the exact Myers-Perry
charges ([ER08] (34), pp. 14, 16, READ); 10.60(b)'s uniformity cited to [Hin26] p. 119 (the verifier's p. 121 is printed
p. 119) and [Hin26c] Remark 7.2 (p. 116), p. 157 kept as the spacetime estimate's; 10.60(d)'s dependencies of
Proposition 10.6 (Lemma 10.4, the dual states' decay, p. 208) and the first row's domain membership ((10.48), pp. 204,
214-216, READ); the paper's overclaims (the gluing computed, every input computed, one kind of reading) and stale
references; the nits (a line opening ">=", |P| = E|v|, general5.py's (E.14) for P = -m v, G1's image check automatic,
10.58-10.63). The separation's item (iii), constants not evaluated, is withdrawn as a gap: lambda_1 and delta exist and
are not evaluated, as Hintz's smallness constant is not.

**D134 (2026-10-24): [Hin23a] section 3 at n = 4 by modification (exterior5.py X1-X6, 10.64).**

The user's direction (2026-10-24): "What separates it from proved. The same three things as before: - continue please".
Item (iii) is not a gap (D133). For item (i), [Hin23a]'s section 3, the one reading that is a whole proof in another
dimension, is replaced by a proof by modification. The six places n enters are computed (Proposition 10.48): the
conjugated wave operator's ((n-1)(n-3)/4) r^-2, the b-density, the energy form (3.25) with Lap + 3/4, the gauge
endomorphism (2.11) from Definition 2.2 (his matrix and five intermediates at n = 3; at n = 4 lower triangular with
diagonal 2 gC, gC, 3gC/2, -3gU/2, -gU, 0, -2gU, his Remark 2.3's duality holding at both), the quadratic radiation term
r^(1-k) against the linear (critical at n = 3, r^-(1/2) at n = 4), the Sobolev counts; then each of his steps runs with
the computed quantity in place (10.64(a)-(i)). exterior5.py: selftest 12/12 (about ten seconds), mutants 4/4. Remaining
of item (i): [Hin26c] sections 7-9, [Hin26a] section 5.2, and for part (ii) [HHV21]'s perturbation arguments, Hintz's
boost sections and [CD03]'s argument at n = 4.

**D135 (2026-10-24): [Hin26a] section 5.2 at n = 4 -- the calculus and the commutators (10.65).**

10.56 had narrowed B4 to one reading, that the commutator computations of [Hin26a] sections 5.2.1-5.2.6, not redone at n
= 4, give the signs of the computed five-dimensional symbols. Redone at source (alphaXiv, 2026-10-24): each is the
principal symbol identity a H_(-l+j) a + S a^2 = c_0 a^2 + b_0^2 + b^2 - e^2 + f, in which the dimension enters only
through l, j, S, w and the density defining S, all 10.13's at n = 4; the square roots are Proposition 5.1 (3)-(6),
computed (10.14, 10.22); Lemma 5.14 and Corollary 5.15 are stated in every dimension; and the 3b-calculus is constructed
on R_t x R^(n-1)_x for every n ([Hin23d] pp. 3, 7, 10-12, 109). B4 discharged at source; nothing new computed. The user
noted that arXiv has a connector: it is alphaXiv, through which every READ of the record was taken; its full-text mode
now carries the censuses of [Hin26c] sections 7-9, [HHV21]'s perturbation arguments, [Hin26]'s boost sections and
[CD03]'s gluing.

**D136 (2026-10-24): the fifty-seventh verifier on 10.64 and D133's repairs, seated.** Majors: M1, Theorem 4 (ii) and
10.63(b)-(c) named the base of the perturbed data as g_lam's data, which on Sigma'' are the glued development's (g_lam
on Omega, exact Tangherlini outside a compact set) -- named so now; M2, the order of [Hin23a] Proposition 3.29's
h-dependent entries at n = 4 was stated, not computed -- computed now (exterior5.py X7: from Ric(g) - delta*_(gb,E_C)
Upsilon(g; gb) linearized in g = gb + r^-k h; at n = 3 his four printed entries in L_2's normalization, at n = 4
r^-(1/2) times them, exactly). Minors: each entry is linear in h, not bilinear (m1); the duality is computed at n = 3
and 4, not every n (m3); Lemma 3.6 at n = 4 computed (X8: xbar_I = min(sqrt3/2, 1/(2 mu^(1/4))), r > 2 sqrt(mu), f >
3/4, (3.8) negative) (m4); the class's gluing needs no parity, the other KIDs' charges vanishing on G-invariant data by
averaging (m5); lambda1 and delta exist by the deduction (m6); the norms of 10.62(d) for 'Hintz's norms' (m7); P = -E
v's sign convention (n1); the seating renumbered D136, D135 being 10.65's (m2). exterior5 --selftest 16/16, --mutants
6/6. The censuses of [Hin26c] sections 7-8 (122 rows), [HHV21] (205), [Hin26]'s boost sections (123) and [CD03] (126)
came back from the alphaXiv full texts; their replacements at n = 4 follow.

**D137 (2026-10-24): the censuses' readings carried to n = 4 (10.66-10.68).** From the full-text censuses: [CD03]
Theorem 8.1's proof uses the dimension at five steps written for n = 3, through (5.2)'s weights and through Appendix E's
exponents; gluing5.py D1-D3 computes them (fifteen KIDs; charges R^-(n-2) and R^-(n-1) under the rescaling; s = t + n -
2), and 10.66 runs the proof at n = 4. Without parity the linear KIDs' errors are O(R^-2 alpha), so at n = 4 decay
faster than r^-(3/2) replaces (E.9) -- impossible at n = 3, where (E.5b) caps alpha at 1 -- and Theorem 4 (ii) is
widened accordingly. Recorded: [CD03]'s printed s = t - 1 gives a solution only in rH^(t-3) x rH^(t-2), and (8.7) prints
R^-1 for charges D2 scales as R^-2. [Hin26]'s boost (D4): his phi_S is the Lorentz boost of rapidity c/2; the
Kerr-Schild mass term pulls back to mu r^(2-n) a^n (dt*)^2, his 2m(a^3 - 1) at n = 3 and mu(a^4 - 1) at r^-2 at n = 4,
inside his class. [Hin26c] sections 7-8 (edge5.py E1-E4): the edge form of the wave operator at I+, the K-current (8.10)
reproduced at n = 3 with the threshold unchanged at n = 4, the rotation fields of S^3; 10.67 carries sections 7-8 and
Theorem 9.16's proof to n = 4. [HHV21] (10.68): its two arguments the record uses are dimension-free, Lemma 11.1 with N
= 11. A first run of the boost prototype exhausted memory and restarted the container; the fifty-eighth verifier,
reading 10.65 and D136, was restarted with it.

**D139 (2026-10-24): a second census, by token sweep (10.69).** censusweep.py lists every marker of the dimension on
every page of the passages carried to n = 4 (270 hits, 204 pages). Each was read against the sections. All are accounted
for but one: [Hin26a] p. 62's density on level sets of tau, r^3 |dr dgslash|, chosen so that with |d tau| it is the
metric density -- at n = 4, r^4 |dr dgslash_S3|. It is a norm convention and changes no estimate. Also: the 58th
verifier's brief had named [Hin26c]'s full text for [Hin26a]; corrected by message, 10.65's quotes being from the right
paper.

**D138 (2026-10-24): the fifty-eighth verifier on 10.65 and D136, seated.** Majors: M1, X7's (4,7) entry -2 matched
Hintz's printed -(1/2) d_1 h_ab only by contraction with T, a reading not stated; the entry maps the tf block to a
scalar, so contraction is the natural reading, now stated in exterior5.py, 10.64 and the control, with the coordinate
reading's -1 recorded (HIN329_ALT) -- the computed -2 and the n = 4 power are unaffected. M2, 10.65's calculus rested on
[Hin26d], unread (10.56's OPEN item); read at source (arXiv:2408.06651): Definitions 1.3 and 1.9 are for a smooth
n-dimensional manifold and example (10) builds the 3b-algebra with S^(n-2) fibres, so the item closes. Minors: (E.9) is
used only for J^munu (m1); [Hin23d] p. 10 quoted verbatim (m2); both n conventions stated (m3); X7 is the principal part
(m4); X7's operator is (3.30)'s but for the h-free gamma_Ups term (m5); the label of 10.64 now names the reading (m6).
Nits: xbar_I's cap not computed, stated; timings. The verifier's independent jet-based recomputation reproduced every X7
coefficient at n = 3 and n = 4 at two radii.

**D140 (2026-10-24): the deductions inventoried (10.70).** Four extraction passes listed every deduced item of
10.12-10.69 with its sources and sorted it by one rule: 248 items, D 90 (bookkeeping on computed values), B 60 (a 3 + 1
proof carried by modification), C 31 (perturbation or continuity), A 29 (a general-n result applied), ? 38. The
extractors had no write tool and returned their rows inline; the rows were saved as returned, and merged into
DEDUCTIONS.tsv. The paper's 8.8 now gives the count: the 60 B items are the core of the line-by-line check.

**D141 (2026-10-24): the perturbation steps at proof level (10.71).** The 31 C rows of DEDUCTIONS.tsv share one shape: a
property at one point carried to a neighbourhood. Lemma 10.52 proves the three abstract steps they use -- openness of
invertibility by the Neumann series; dim ker <= N near a Fredholm index-0 point by a rank-N stabilization V = sum f_j
l_j; persistence of strict inequalities on compact sets -- and cites Rouche/Hurwitz and the inverse function theorem.
Each C row is mapped to its lemma and its continuity input, READ from its source; ten rows the rule misfiled (exact,
computed, or B steps) are listed apart.

**D142 (2026-10-24): the general-n steps' hypotheses placed (10.72).** An extraction pass listed each A row's hypotheses
and where the record establishes them: 23 of 28 complete, 5 partial, and one row (10.51 (c)) missed and misfiled. Three
partials were closed by reading at source: [Hin26] Proposition 5.25 (pp. 110-111), a triangular frame system the same in
any n; [Hin26] Lemma 10.13 (p. 217) and [Hin26c] Lemma 14.6 (pp. 264-265), Hardy inequalities in t with general s by the
3b calculus. 10.41 (d)'s inputs are 10.53's and 10.67's; 10.38 (a) is X7's computation for [Hin23a]'s gauge, deduced for
[Hin26]'s.

**D143 (2026-10-24): the fifty-ninth verifier on D137-D139, seated.** gluing5.py and edge5.py 4/4 with mutants 4/4;
censusweep.py reproduced for five papers; quotations verbatim. M1 (major): the parity inventory listed only (E.19) and
(E.20b); [CD03] also uses parity for the Lorentz invariance of J^munu ((E.21)-(E.23), p. 74) and the preservation of
(E.9) under boosts, both on the way to (E.14) -- uses that fall on the Myers-Perry family, which has alpha_- = 3 -- and
(E.20b)'s bulk term is finite because the data are vacuum. Seated in 10.63(b) and the paper's 8.7. M2 (major): that the
reason given for reading (8.1) with k^+ is false. Checked: on the boosted slice t = v x of a static metric, K = v N
Hess_h(x) + O(v^2), odd and of order m r^-2 for Schwarzschild, so r |K^-| ~ r^-1 and printed (8.1) forces alpha_- <= 1 <
alpha; the verifier's reading dropped (8.1)'s factor r. Refuted; the sign argument the verifier gave is the one 10.63(b)
already states. Minors: [Hin26d] pages 4, 8, 26 -> 5, 9, 27 (m1; journal line verified, DOI added); (8.7)'s R^-1 for J
and E C at n = 3 read as a misprint, the n = 3 proof needing the parity-improved error, n = 4 not (m2); gluing5.py D2-D4
and edge5.py E2, E4 now test what they claim (m3); censusweep.py read the CD03 copy's page markers as opening their pages
when they close them, so its window ran one page late -- corrected, with p. 38 added: 278 hits on 205 pages, CD03 48,
all accounted for in 10.69(e) (m4); HHV21's "7-dimensional" on p. 70 (m5). Nits: "deductions by modification"; 10.69(c)'s
dimensions per n; 10.66(d)'s units; 10.63(c)'s parity alternative.

**D144 (2026-10-24): the undecided rows read (10.73).** All 38 ? rows of DEDUCTIONS.tsv read in full. Ten are summaries
and two four-dimensional remarks; ten are bookkeeping on computed values (10.36 (a)'s "reading" that route B's family
is equivariant is discharged by mp5.py M2's computation), three applications with hypotheses placed, five elementary
steps written out where they stand. Two recurring kinds get lemmas: Lemma 10.55 (equivariance) for the five symmetry
steps of the class, and Lemma 10.54 (harmonic synthesis) for the sums over harmonics in 10.27 (a) and 10.33 (a), whose
input -- gauge 1-forms with coefficients bounded uniformly in l -- synth5.py computes (S1-S2, B = -2 H_T/k, A_a = -(2
r/k)(f_a + (r/k) d_a H_T), B = -2 H_T/k_V) with the floor k^2 >= 8 (S3); 3/3, mutants 3/3. 10.40 (a) is a modification
step. DEDUCTIONS.tsv gains a column `final`.

**D145 (2026-10-24): the modification steps' changes placed (10.74).** One extraction pass tabulated the 60 B rows
(10.40 (a) added by hand): the places each says change between n = 3 and n = 4, where each five-dimensional value comes
from, inputs, residual wording, readings. 28 values the rows only state were placed by hand: 11 arithmetic in n, 8
computed, 8 at an earlier section, 1 the record's choice. B-MAP.tsv. A modification step then holds if its source proof
uses n only at its listed places -- the census question -- so 8.8 (ii) reduces to (i). The paper's abstract, 1.3, 8.8
and 9 now say so.

**D146 (2026-10-24): eleven modification steps written out (10.75).** An extraction pass located the source proof behind
each of the 61 modification steps (its choice of result wrong for about a third, reassigned by hand). The short ones
held in full text were read at source and matched step by step to their five-dimensional justifications: [Hin26]
Proposition 8.8 (the contracted Bianchi identity and box^Ups = 2 delta_(E^Ups) G delta* made explicit), Lemma 8.5
(lin5.py E5 computes its conclusion), Lemma 6.10 (replaced by the record's energy identity), Lemma 6.13, Proposition
10.6, the remark after (2.46c); [Hin26c] Corollary 9.43; [CD03] Theorem 8.1, whose twelve steps 10.66 places; and three
that 10.31 (a)-(b) and 10.18 (b) had already written out step by step -- [Hin26] Lemma 7.2, Proposition 7.3 and Lemma
6.1 (1). These eleven rest on their inputs, not on a census. The other 50 carry proofs of several pages each.

**D147 (2026-10-24): the sixtieth verifier on D140-D145, seated.** synth5.py 3/3, gluing5.py and edge5.py 4/4 with
mutants caught; mp5.py 5/5; censusweep.py 278; the counts of 10.70, 10.73 and 10.74 reproduced; the five quotations of
10.72 verbatim; the D143 refutation of the fifty-ninth's M2 confirmed. M1 (major): Lemma 10.54 (ii)'s C^1 clause needs
d_r^2 u, which the hypothesis did not give, and the gauge 1-forms contain d_r H_T -- repaired: the hypothesis takes i <=
2 with two stated bounds on A_j, and 10.73 (vi) writes the weights for 10.33 (a) and the compact interval of 10.27 (a).
M2 (major): the paper's abstract, 1.3, 8.8 and 9 claimed proof level for every non-modification step and "each
computed" for the modification steps' values; now qualified -- two exceptions named (10.38 (a), 10.21 (e)), the values
computed, deduced in an earlier section, arithmetic or the record's choice, 11 rows naming no place, and the reduction a
rule deduced, not proved. Minors: B-MAP.tsv's `kind` column and rule -- under it the 28 hand placements are 11
arithmetic, 12 computed, 4 at an earlier section, 1 choice, where D145 gave 8 and 8 (m1); the 30 readings' sources
reworded (m2); 10.71's misfiled rows are eleven, not ten as D141 said, and its closing sentence now covers them (m3);
beta = min(alpha, n - 2) derived from the decay rates (m4); 10.36 (a)'s equivariance deduced from mp5.py M2's symbolic
block checks, the full metric checked at three spins (m5); 10.70's ? sentence (m6). Also seated: Lemma 10.52's continuity
of the inverse and the onto-witness; the rotations' isometry and strong continuity proved; Proposition 5.25's (h~_1)_0j
coefficient is -e_0 t_IVP (10.72); "278 hits on the 205 pages swept, 81 with a hit"; Kerr's K order sourced; Lemma
14.6's density; the paper's "Settling, proved." heading renamed.

**D148 (2026-10-24): one exception removed; fourteen modification steps written out.** [Hin26] Definitions 4.1-4.2 read
at source: E^Ups_g0 and E^C_g0 use only the background g_0 and the fixed 1-forms, and enter P(g, g_0) and its
linearization (4.13) with g_0's coefficients, so the h-dependent terms are [Hin23a]'s (3.30) term by term and X5, X7's
orders carry: 10.38 (a)'s deduced link is READ (10.72 (iii)), and the one exception left is 10.21 (e). Three more
modification steps matched step by step against their source proofs, read at source: [Hin26] Proposition 6.15 (10.28
(a), with the regularity-in-b paragraph added), Proposition 6.18 (4)-(7) (10.30 (a)), and the injectivity half of
Proposition 9.2 (2) (10.37 (c)). And [Hin26] Propositions 8.11 (10.32 (c)) and 7.4 (10.36 (b)). Sixteen of 61 written
out (10.75); 45 rest on the censuses. Paper: "but for one".

**D149 (2026-10-24): the sixty-first verifier seated; a lemma at the horizon proved, the continuation deduced.** The
verifier read D146-D147 (10.73-10.75 (i)-(xi)) and found four majors. M1: 10.75 (i)'s step (7) used omega's continuation
inside the horizon, which 10.27 (b) had left OPEN and 10.55 (c) does not give. Repaired by proof: Lemma 10.56 (10.76) --
for z X' = A(z) X with A smooth, a solution vanishing to infinite order on one side vanishes (a Gronwall bound), and one
smooth up to 0 from one side extends as a smooth solution (Borel's lemma and variation of constants against a flat
error); the same for f phi'' + Q phi' + R phi = 0 with f's zero simple. With it, deduced at proof level: every
operator's radial system has f = g^-1(dr, dr); omega is smooth up to r_h by the radial components of delta* omega = u, a
regular system; it continues as a solution of box^Ups omega = 0, so Proposition 6.12 applies on X; and the interior
uniqueness (10.15 (a), 10.16, 10.55 (c)) is deduced at proof level (10.76 (b); D157) in place of 'its Frobenius
exponents are finitely many'. M2: 10.75
(iii) rests on 10.19 (d)'s reading; marked, and B-MAP.tsv's row says so. M3: 10.15 (a) and 10.63 (c) named no place;
given their places (the replaced citation; 10.66's seven), so 52 name some and 9 none, 96 placements (32 computed, 52
section, 11 arithmetic, 1 choice; 10.31 (b)'s Z4 token counted computed, m6), 31 rows on a reading. M4: the paper called
the deductions' inputs computed and READ; it now names readings, the modification steps' conclusions, among them (31 of
61; ten of the sixteen written out), in the abstract, 1.3 and 8.8. Minors: (xi) Proposition 10.15, with Q's order
deduced from Proposition 10.45; (viii) [CD03]'s printed s = t - 1 and (8.7) noted; (iv) Corollary 9.43's
tf-admissibility hypothesis placed; (ii) E5 for l <= 12, 10.24 (a) for every l; (vi) the Killing lift from R x (R^n \
0), a superset, and 'justifies it in one line'; (v) Lemma 2.13 on b-manifolds; paper 1.3 adds the record's choice. The
verifier did not read D148.

**D150 (2026-10-25): eleven more modification steps written out.** Read at source and matched step by step at n =
4 (10.75 (xvii)-(xxvii)): [Hin26] Proposition 10.7 and Theorem 10.1, whose proof is 10.40 (a)-(c) (10.39 (e)); Lemmas
10.9-10.11 (10.40 (a)); Lemma 8.15 with Proposition 7.4 and Lemmas 2.15, 7.2 (10.60 (f)); Lemma 11.15 and Proposition
11.14 (10.44 (c)); Theorem 5.23 and Lemma 3.19 (10.66 (f)); Theorem 13.1 (10.62 (d)) and its Step 1 in the class (10.49
(a)); [Hin26c] Theorem 9.36 (10.20 (a)) and Lemma 13.13 (10.41 (b)); [Hin24b] Lemma 3.17 (pp. 51-53, fetched in full
text), which [Hin26] Lemma 8.12's proof cites verbatim (10.32 (b)); and [Hin26a] Theorem 4.9, whose appendix proof is
replaced at n = 4 by Proposition 10.44's certificate (10.54 (a)). Writing them out found nine places of the dimension
their B-MAP rows did not name -- the tf norm's |sigma|^(n/2) and alpha_0's -n/2 in Proposition 10.7, the embedding
(3.72), Lemma 13.13's 5/2 and 3/2, Lemma 11.15's Step 2 index sets and Step 3 condition, so(4)'s bracket in Lemma 8.15
(2), the boost pullback's a^4, and the boundary terms of Lemma 3.17 -- and one reading (Theorem 9.36's radial estimate,
10.19). Counts: 53 rows name places, 8 none; 105 placements (33 computed, 57 section, 14 arithmetic, 1 choice); 32
rows on a reading; twenty-seven written out, fifteen on a reading; 34 rest on the censuses.

**D151 (2026-10-25): three more written out.** [Hin26] Proposition 8.14 (10.34 (c); Steps 0-5 at n = 4, Step 0 not
used, Step 2 the record's modification), (2.27) with Proposition 2.25's proof, b-analysis free of n (10.46 (e)), and
section 5.6's boost pullback (10.62 (c)). Two more places named ((8.33)'s vector in so(4); the boost pullback at r^-2).
Thirty of 61 written out, eighteen on a reading; 31 rest on the censuses.

**D152 (2026-10-25): [Hin23a] section 3's four steps written out.** Propositions 3.17 (10.64 (b)), 3.29 (10.64 (e))
and 3.32 with Lemma 3.33 (10.64 (g)), and Corollary 3.31 (10.64 (f)), read at source (pp. 15-30) and matched step by
step to exterior5.py X1-X7: the leading operator with Lap + 3/4, the symmetric density, Q-bar, the h-free lower
triangular A, the h-entries r^(-1/2) below his, the quadratic term in the error, the Sobolev counts, and Lemma 3.33 not
used since A^0_h = 0. Thirty-four of 61 written out, eighteen on a reading; 27 rest on the censuses.

**D153 (2026-10-25): the sixty-second verifier seated.** It read D148-D149: Lemma 10.56 and 10.76 passed line by
line, 10.75 (xii)-(xvi) and the D149 repairs matched their sources, and B-MAP's counts reproduced. M1: the paper's
verifier record, D149's heading here and ROUTES 4.80's heading said the continuation was proved; only Lemma 10.56 is,
the continuation deduced at proof level from it -- now worded so (10.27's notes too). Minors: 10.76 (a)'s phi''
coefficient is a constant multiple of f (-f, -f/2 in his convention); Lemma 10.56 (c) says flat; the sigma = 0 remark
names its source (u - g-dot^Ups(b-dot))_(r nu) and the subtraction of the Killing and s1 states; the interior is
Lemma 10.56 (c) (B-MAP, 10.55 (c), ROUTES); 10.74's "seven places 10.66 computes" is "places (four computed)"; [CD03]'s
s = t - 1 is on p. 37 (10.75 (viii), 10.66's READ), and (viii) no longer calls it a reading; 10.75 (xii)-(xiii)'s item
references name Propositions 10.25 and 10.27; (xv)'s cokernel argument names (7.13), (7.15) and the pairings; three
wrapped lines that began with a list marker rewrapped, and the wrapping now avoids them; "READ at source since"
dropped; the paper's md5 rows refreshed and its record scoped to (i)-(xi).

**D154 (2026-10-25): [Hin26] section 5's exterior steps written out.** Proposition 5.11 with Proposition 5.14 and
Corollary 5.15 (10.48 (b)): (4.13) term by term, the h-free parts computed (scri5.py), the h-dependent ones [Hin23a]'s
(3.30) (READ) at r^(-1/2) below his (X7), the annihilating diagonal entries at 10.44 (b)'s five-dimensional exponents.
Theorem 5.17 (10.48 (c)), whose proof is [Hin23a] Corollary 3.36's, now on 10.75 (xxxi)-(xxxiv) instead of a reading
of [Hin23a] at n = 4, so 10.48 (c)'s reading is cleared (31 rows on a reading). Thirty-six of 61 written out, eighteen
on a reading; 25 rest on the censuses.

**D155 (2026-10-25): [Hin26] section 12 written out.** Theorem 12.3, the construction of Phi in section 12.2.1,
and Theorem 12.8's peeling of Corollary 11.66's solution (pp. 304-318), matched step by step at n = 4 without the class
(10.62 (b), 10.75 (xxxvii)) and in it (10.47 (d)-(e), (xxxviii)-(xxxix)). Seventeen places named in B-MAP (iota+ over
S^3, the parameters at (2, 0), the source at t*^-4, the induction from alpha_min, Res(L-bar, 2) = {0}, the lists, Case
A's K+ order in the class); section 9's iota+ solution theory marked as the reading it is on 10.47 (d) and 10.62 (b)
(33 rows on a reading). Thirty-nine of 61 written out, twenty-one on a reading; 22 rest on the censuses.

**D156 (2026-10-25): [Hin26] Theorem 11.12 and [Hin26a] Theorem 6.2 written out.** Theorem 11.12 has no proof
of its own -- [Hin26c] Theorem 11.1 applied through Corollary 11.10 in the unweighted densities, at n = 4 with the
shifts (2, 5/2, 1/2) (10.42 (e)). [Hin26a] Theorem 6.2's proof (pp. 67-69): (6.4) with the shift 3/2 and three angular
copies (10.21 (a)), Part (2)'s injectivity (10.21 (c)) and the whole (10.56 (b)), each step matched to cpmodes5.py,
solv5.py, Proposition 10.9 or a named section. Eight places named; 10.21 (c) and 10.56 (b) marked as resting on 10.56
(a)'s reading (35 rows on a reading). Forty-three of 61 written out, twenty-four on a
reading; 18 rest on the censuses.

**D157 (2026-10-25): the sixty-third verifier seated.** It read D150-D153 (10.75 (xvii)-(xxxiv)) against the
sources: no major; (xxii), (xxiii), (xxvii) and (xxxiii) partial; B-MAP's counts, D153's repairs, the paper's counts and
the hygiene passed. Minors seated: m1, (xxvii) now names [Hin24b]'s step replacing g-dot^Ups by g-dot (Lemma 3.14 and
integration by parts against h*); m2, at n = 4 (A_h)_(7,6)'s (2, 0) enters at Step 3, not Step 2, and Step 3's min Re
E^C_I > 1 and (11.26)'s remainder class are named; m3, two source misprints no longer carried -- [Hin23a] (3.47)'s 2
rho_I^-1 rho^3 is 2 rho_I rho^-3 (2 rho_I rho^(-7/2) at n = 4, (xxxiii) and 10.64 (f)), and [Hin26c] p. 60's
(|sigma|^(3/2))^2 is (|sigma|^(-3/2))^2 with r-hat = r |sigma| ((xvii)); m4, three places added to B-MAP (10.49 (a)'s
I+ threshold 3/2, 10.66 (f)'s spin order r^-3 and (3.43)'s normalization 2/pi^2 over S^3), so D150's nine was a floor;
m5, D149's entry here says the interior uniqueness is deduced; m6, ROUTES 4.81's "none of them in [Hin23a]" corrected
(10.48 (c), written out in D154), the paper's [Hin26] sections already section 11 (D155); m7, Appendix C's sources and
verifier record, and [Hin23a]'s p. 15; m8, "at most about seven pages" ((xvii)'s section 10.2) and (xxx)'s pp. 108-109;
m9, (xxxiv)'s B_g; m10, (xviii)'s Paley-Wiener representation, (xxiii)'s (5.46) and (xxviii)'s Part (2) and Step 5
range named; m11, 10.74's n/2 sentence corrected.

**D158 (2026-10-25): [Hin26a] Appendix B written out.** Proposition B.2's microlocal Fredholm argument and
relative index count (10.23 (b)), Theorem B.4's energy, radial-point and propagation estimates on edge-b spaces (10.23
(c)) and section B.4's conclusion (10.23 (d)), read at source (pp. 87-98) and matched step by step: the scalar part's
shift 3/2 and its symmetry for r^3 dr, the thresholds from K1-K2 and F4, the Mellin weight -2 + beta, the index counts
2, 3, 1 and F5's free roots, the cf positivity and characteristic polynomial (F3, C7), the density r^4 and the data
weights (F4). Six places named. Forty-six of 61 written out, twenty-seven on a reading;
15 rest on the censuses.

**D159 (2026-10-25): [Hin26c] Proposition 9.10 and Theorem 9.5 (3), (5) written out.** Proposition 9.10's
proof (pp. 167-168) is written with (n - 1)/2 and r^(n-1) at source; at n = 4 V1's skewness and A_w + S-bar = D S-bar D
give 10.19 (a)'s threshold. Theorem 9.5 (3)'s augmentation argument and (5)'s embedding and ODE (pp. 172-173) give
10.55 (b) on 10.19 (d)'s and 10.53 (e)'s readings. Three places named. Forty-eight of 61 written out,
twenty-nine on a reading; 13 rest on the censuses.

**D160 (2026-10-25): [Hin26] sections 11.3-11.6 written out.** Propositions 11.17 and 11.32 with Lemmas 11.18-11.19 in
the class (10.45 (b)), Steps 1-4 without it (10.61 (b)), the class's reductions of his steps (10.43 (c)) and their
conclusion (10.45 (e)), read at source (pp. 231-262) and matched step by step: Theorem 11.12, Propositions 11.14 and
11.16 at n = 4 ((xl), (xxii), 10.44 (d)), the iota+ cap 3/2 + (1 - e_Ups) gam_Ups, the states one order faster, S_1 =
R^4, b in R + so(4), the boost's iota+ order 2, the unweighted density |dx|/|x|^4. Section 9's solution theory
(Corollary 9.12, Propositions 9.11, 9.30, 9.35) is a reading at n = 4, as (xxxvii) found for Corollary 9.18; so is
[Hin26c] Proposition 13.18. Fourteen places named. Fifty-two of 61 written out, thirty-two on a reading; 9 rest on the
censuses.

**D161 (2026-10-25): [Hin26] sections 11.7-11.8 written out.** Proposition 11.51's induction, Theorem 11.59's
four parts and Corollary 11.66 with Lemma 11.65, read at source (pp. 262-295) and matched in the class (10.46 (a)-(b))
and without it (10.61 (c)): S_1 = R^4 and so(4), absent in the class; Proposition 10.46's lists, or 10.42 (ii)'s, in
place of (9.39b)'s; one order of loss in the class; Remark 10.8's logarithm 10.35 (b)'s question. Twelve places named.
Fifty-five of 61 written out, thirty-five on a reading; 6 rest on the censuses, none
in [Hin26]: [Hin26c]'s sections 5 and 7-13 and [Hin26a]'s Theorem 5.2.

**D162 (2026-10-25): the sixty-fourth verifier seated.** It read D154-D157 at source and found one major and ten
minors. The major (M1): (xxxvii) did not place S^(0)_1, whose patch -d chi_K (x)_s omega^(0)_b,s1 has iota+ order 1 in
every dimension. Read at source ((1.39), footnote 143, (11.135a), Step 1.3), the patch is pure gauge for g-bar to leading
order, the gauge 1-form omits it, and its source [L_b, chi_K] h_b,s1 has order 5 at n = 4 (10.28's A^(3,0)). Its
quadratic terms have order 4, so Theorem 12.8 subtracts S^(0)'_1 at lam_0 = 2. Placed in (xxxvii) and 10.61 (a); B-MAP
gains one place. The minors are seated: two reading marks, whole-section citations of census rows counted (thirteen
items now), wording and pages; 10.75's page-count sentence, stale since D160, corrected. Fifty-five of 61
written out, thirty-seven on a reading; 6 rest on the censuses.

**D163 (2026-10-25): [Hin26c] sections 7-8 written out.** Section 7's radial point, trapping and commutator estimates and
section 8's energy estimates, read at source (pp. 114-157), matched at n = 4 as (lvi)-(lvii). The trapping estimate is
[Hin21] Theorem 3.9, read at source and stated for a manifold of any dimension (p. 36). The one new computation is
(7.22)'s density, 2 rho_+^-5 x_I^-8 for his 2 rho_+^-4 x_I^-6, with its symmetric operator (x_I d_x_I - 3), and (8.14)'s
skewness, checked exactly with the constant n - 2 as a failing control. Eleven places named, two corrected. Fifty-seven
of 61 written out, thirty-seven on a reading; 4 rest on the censuses: 10.19 (d), 10.22 (e), 10.53 (e) and 10.58 (c).

**D164 (2026-10-25): [Hin26c] Theorems 9.5 and 9.16 written out.** Theorem 9.5's proof (section 9.2.3, with
Propositions 9.9 and 9.11 and Lemma 9.13) and Theorem 9.16's (section 9.3) read at source (pp. 161-193) and matched at
n = 4 as (lviii)-(lix). Section 9.3 is written for a general stationary wave operator on R_t x X, and Lemma 9.13 for
fields spanning V(S^(n-1)); the n = 4 inputs are the horizon (10.18), the trapped set and loss (10.19 (b)) and the
dynamics (10.19 (c)). Both rows keep one reading, his scalar-to-bundle remark. Eight places named.
Fifty-nine of 61 written out, thirty-nine on a reading; 2 rest on the censuses: 10.22
(e) and 10.58 (c).

**D165 (2026-10-25): the sixty-fifth verifier seated.** It read D158-D162 at source and found three majors and
eight minors. M1: (li), 10.43 (c), rests on (xlix)'s readings and 10.46 (a)-(b)'s and did not say so; it now does, B-MAP
marks it, and the counts of D162-D164 on a reading were one short. M2: (xxviii) credited the source with the root gap;
the source's Step 5 uses Theorem 7.1 (2) and passes over the endpoint A^(-C_0), and the root gap is now the record's own
route, with A^(2-) checked inside 10.21 (e)'s range. M3 is answered at source: the subtraction of D_U Phi(b', S',
S^(0)'_1, (0, f'_1), 0, ...) is his Step 1.3's general case (p. 315), now quoted; only its placement at lam_0 = 2 is the
record's, now marked. Minors seated: (11.135a)'s gauge 1-form, the commutator's +2, three kinds relabelled computed,
10.32 (b)'s placed column, 10.45 (e)'s weight, (11.107b), (11.66a)-(11.66b), (11.227a), the closing paragraph's ranges,
10.62 (b)'s inputs. The note on D163's counts was already repaired in D164. Fifty-nine of 61 written out,
forty on a reading; 2 rest on the censuses.

**D166 (2026-10-25): [Hin26c] Theorem 10.1, Theorem 11.1 and section 13.2 written out.** The second-last census row,
10.58 (c), as 10.75 (lx): Definitions 5.13, 5.15 and 5.18, section 10's normal operator analysis (Propositions 10.6,
10.12 and 10.14 with Lemmas 10.7-10.10) and its proof of Theorem 10.1, Theorem 11.1's approximation argument, and
section 13.2's Corollary 13.17 and Proposition 13.18, read at source and matched at n = 4. New instrument iplusnorm5.py
(N1-N9, 9/9, mutants 9/9; Proposition 10.57) computes each place at n = 3 against print and at n = 4; nineteen places
named. His (1.3.1) sum omits Re S and his (1.3.2) sum prints +4 Re S where -4 Re S gives his stated threshold; both are
the same at n = 3 and n = 4. Lemma 10.9's parametrix, Hintz's 0-calculus Theorem 1.5 (arXiv:2112.08130), is stated for an
n-dimensional manifold with boundary: READ. The row keeps a reading, now (lvi)-(lix)'s and 10.20's.
Sixty of 61 written out, forty-one on a reading; one rests on its census: 10.22 (e).

**D167 (2026-10-25): [Hin26a] Theorem 5.2 written out; no census row left.** The last census row, 10.22 (e), as
10.75 (lxi): his section 5.2 read at source (pp. 41-66) and matched at n = 4, every five-dimensional place computed in
10.13, 10.14 and 10.22 or READ in 10.65; nine places named. It rests on no reading; 10.21 (c) and 10.23 (c), whose one
reading was Theorem 5.2's, are re-marked with it, and (xlii), (xliii) and (xlv) say so. All 61 modification steps are
written out at n = 4; thirty-nine take a reading among their inputs. The paper's abstract, introduction,
section 8.8 and section 9 now name the readings beside the censuses.

**D168 (2026-10-25): the sixty-sixth verifier seated.** It read D163-D165 at source: no major, four minors. Seated:
(7.11a)-(7.11b) for (7.11); Proposition 7.10's (7.25) is [Hin21] (3-24) for QPQ^-, "almost" Definition 5.8 for P, and
the n = 4 check is (5.9) at the trapped set; 10.45 (e)'s non-change place dropped from B-MAP; (lvii)'s two z's told
apart. Its other checks passed, among them the counts at each commit, (7.22)'s density and (8.10)'s K-current recomputed
at both n, and D165's quotations verbatim.

**D169 (2026-10-25): the readings traced to their roots.** The 39 rows that took a reading, traced through the
sections they cite (10.77, READINGS.tsv): four rested on statements since READ or written out and are re-marked
(10.23 (b), 10.23 (d), 10.46 (e), 10.62 (c)); the thirty-five others rest on ten roots, two of them the source's own
steps at every n, three groups of companion results at n = 4 READ at n = 3, five the record's own questions. The
paper's section 8.8 names them.

**D170 (2026-10-25): three of the record's roots settled.** 10.78: Lemma 10.58 (deduced at proof level) gives
Corollary 8.13's semicontinuity from uniform estimates, so RK rests on RU; RG follows from the uniqueness of each
step's data in Theorem 12.8's proof (p. 315) and G-equivariance; RE is mp5.py M2's covariance, the family taken as
route B's g_b. Seven roots remain. RH at the record's point needs a computation: at the horizon's null conormal dr,
l(dr) has eigenvalues 2a (three times), 4a and 2(1 - e) a with a = c_t(r_h) > 0, so the damping is not small in e, but
the undamped part in B's inner product carries B's conditioning, about 1/e.

**D171 (2026-10-25): RH computed.** 10.79 and `hthresh5.py` T1-T5: [Hin26c] (5.17)'s horizon quantity for box^C, READ at
source with its normalisation (4.28) and the component R+_H+ = {xi_0 > 0} (Definition 4.8), computed at the record's
point in [Hin26a] Lemma 3.3's B. The undamped part, from the operators' definitions, is the B-symmetric part of 2
Gamma_t, spectrum +-(e^(1/2) + e^(-1/2))/r_h: vartheta_0 = 102401/640, not the 1/e the conditioning suggested. With the
damping, vartheta_H+ = -4995.83... at h = 10^-6, and the threshold 1/2 + vartheta_H+ < -100 holds for every h below h_2 =
2.6197... x 10^-5. RH leaves READINGS.tsv; every row it touched keeps RB, so thirty-five rows still take a reading. Of
the record's own roots RP remains.

**D172 (2026-10-25): the sixty-seventh verifier seated.** It read D166-D168 at source: two majors, five minors. M1, that
(1.3.1)'s threshold is not (10.28) unchanged, is answered at source the other way: vartheta_dK+,in by (5.20) contains S's
-(S + S^*), the printed prefactor is -xi/2 (the report read -xi^2), and so D166's own claim that his sum omits Re S was
the error; iplusnorm5.py N6 derives the S part now (9/9, mutants 9/9). M2 accepted and repaired by re-scoping 10.22 (e)'s
row to Theorem 5.2; its second sentence's inputs are 10.21's and carry RB. Minors seated: five placements re-kinded
arithmetic (88/94/38/1), 10.22's stale sentences, the paper's 61, [Hin23e].

**D173 (2026-10-25): RL written out.** 10.80 and `tfnorm5.py` R1-R4 (4/4, mutants 4/4): [Hin26c] Theorem 9.38 and
Corollary 9.39, stated and proved for every n, and Theorem 9.41, written at n = 3, read at source and written out at n =
4 on (xx), (xlvii), (xlviii), (lix) and 10.20-10.21. The proof of (9.117) misprints one intermediate line at every n; the
identity itself holds, with S~ = S-bar for the Minkowskian model. RL leaves the twenty-two rows it touched; each keeps
RB, so thirty-five rows still take a reading. Five roots remain: RB, RU, RC, RI and RP.

**D174 (2026-10-25): RC READ for general n.** 10.81: the calculi behind [Hin26c] Lemmas 3.9, 13.13 and 14.6 are
constructed for every n in [Hin23d] (pp. 22-37, 59, 96-101), read at source; the three lemmas carry no numeral of the
dimension. 10.41 (b), whose one root it was, leaves the readings: thirty-four rows take one. Four roots remain: RB, RU,
RI and RP. D173 re-wrapped five lines that began with a list marker, three of D172's rewrap of (lx) and two of 10.80's.

**D175 (2026-10-25): the sixty-eighth verifier seated.** On D169-D172 (47e3f62): no majors; nine minors. Two semicolons
inside B-MAP.tsv entries made commas (10.15 (a), 10.58 (c)), so either separator counts 214 places and 221 placements;
(5.17)'s prefactor written with his varrho^2 in 10.18, 10.79 and `hthresh5.py`; 10.22 (e)'s r = m named as his inner
bound r_h/2; e named e_C in 10.79; 10.77's counts marked D169's; iplusnorm5.py N5's label narrowed. On the fibre inner
product, 10.79 states the reading that (5.17) asks for one fixed in advance, and `hthresh5.py` T6 (6/6, mutants 6/6)
computes 1/2 + vartheta_H+ = -4995.44, -4877.97 and -2500.47 for B with e' = 10^-5, 1/10 and 3; the verifier's own
construction gave other values in the same direction. Two minors stand as written: the statement counter (Lemma 10.58
sits in section 10.78) and 10.74's 'one reading' for 10.21 (c) and 10.23 (c).

**D176 (2026-10-25): RI written out.** 10.82 and `iotasol5.py` J1-J5 (5/5, mutants 5/5): [Hin26] section 9 --
Propositions 9.2 (both halves), 9.4, 9.9, 9.11, 9.15, 9.22, 9.30 and 9.35, Corollaries 9.12 and 9.18, Lemmas 9.14, 9.21
and 9.26, (9.54)-(9.56) -- read at source and written out at n = 4. The model from -box gives c = (n - 1)/2 for his 1 at
every place it moves a threshold (s < 2 - Re lam, Re lam < 5/2, the I+ weight 3/2 - eps, Re lam < 3/2 for the expansion,
l_scf < 3/2); the conjugation that carries the Fourier side to N_tf is rhat^(lam - 1) at every n, so the injectivity
bound 1 + eps_ind stands; the index 0 half runs on (lx), Proposition 8.6 and Corollary 9.39 at n = 4; the expansions gain
t2 at -2 and t3 at -3; Lemma 9.26's residue has rank 10 on S^3. (9.7) prints rhat^-2 N_tf for the bracket that (9.58)
makes rhat^2 N_tf. RI leaves twelve rows; 10.47 (d)-(e) rest on RB. Three roots remain: RB, RU and RP.

**D177 (2026-10-25): the sixty-ninth verifier seated.** On D173-D175: no majors; nine minors. (3.46)'s norm factor at n
= 4 is |sigma|^(-2 - alpha), the print reversing the sign of n/2 as its density line does ((xviii) named that line;
10.80 and `tfnorm5.py` R3 now say so), harmless, the factor on both sides of the chain; R3's embedding check moved to
ztf in r-hat, where the loss n/2 lives, and its factor check now tests the sign; R4's remainder gains the S term. 10.74
counts 34 rows on a reading. The fibre inner product: the threshold is not inner-product-free -- `hthresh5.py` T6 now
finds 1/2 + vartheta_H+ = +790.43 at e' = 10 and the crossing of -100 at e' = 7.764, B' positive definite throughout --
so 10.79 states the existential reading on Proposition 7.4 alone, Lemma 5.12 cited for the like choice at
vartheta_dK+,out, and drops 'any one'. 10.81 no longer calls [Hin23d] the source of every class [Hin26c] uses (Psi~_3b
comes from the scaled bounded geometry paper, p. 46, not fetched) and names the numerals (d) places; Theorem 2.9 is
p. 27. READINGS.tsv keeps 10.41 (b) with '-' as it keeps the four D169 rows. The paper's `hthresh5.py` bullet reads
6/6. A wrapped LOG line from D163 that began with a list marker is rewrapped.

**D178 (2026-10-25): RP settled.** 10.83, deduced: the six rows that took 10.35 (b)'s second reading use of the zero
energy pole only Hintz's structure -- L~'_b(sigma)^-1 uniformly bounded with sigma d_sigma-regularity (Proposition 10.7,
written out at n = 4 in (xvii)) and the augmentation's explicit columns with sigma^-1 and sigma^-2 -- and at n = 4 those
columns carry no logarithm, the naive entries being of degree -3 inside the target space (10.39). Remark 10.8's sigma log
|sigma| terms do not arise at n = 4; S^(0),(2,0)_0 removes an absent term. RP leaves six rows. Thirty-four rows take a
reading and rest on RB and RU alone; none of the record's own roots remains. Logarithms inside the augmented inverse at n
= 4 are not settled and not used.

**D179 (2026-10-25): the seventieth verifier seated.** On D176-D177: no majors; eight minors. 10.80 (c)'s remainder
carries the S term R4 gained in D177. `tfnorm5.py` R3's embedding check integrated a symbolic power whose condition sympy
returned without the borderline; it now integrates just above and below a = q - n/2 (4/4, mutants 4/4). `hthresh5.py`'s
inner product dependence, unexercised by T6's control, is T7 with its own (7/7, mutants 7/7). `iotasol5.py`: J1's d_t*^2
check is exact, J4 compares the incoming exponent with c - S, J2 checks the ranges of (9.5) and (9.21) and names its n =
4 values as the record's (5/5, mutants 5/5). 10.82: READ from p. 164; (e) names E^C_I,sharp's 2 as 10.59 (c)'s reading.
The marker guard now also refuses a wrapped line that begins with a number and a full stop, and one such line, with four
that began with + or -, is rewrapped. The paper's `hthresh5.py` bullet states that the threshold holds in the inner
product fixed, and its section 8.8 that Hintz's own theorem rests on RB and RU too.

**D180 (2026-10-25): the seventy-first verifier seated.** On D178-D179: no majors; eight minors, every page claim
checked at source where the record holds the page (p. 211's (10.37)-(10.38a) and "used only in section 11.8", p. 212's
(10.41)). 10.83 (a) said section 11 uses two things of the pole; it uses three -- the uniform bound, the explicit
columns, and the coefficients' structure at zf, a value at 0 plus a remainder of positive order, through L~(0)^-1 on
Taylor coefficients, Lemmas 11.21 and 11.33, [Hin26c] Proposition 13.18 and (10.40), all written out at n = 4 in
(xlix), (l), (liii) and (liv) -- and sections 11.3-11.7 invert (10.26)'s L~, not (10.41)'s L~'. 10.83 (c)'s Jensen
clause was wrong: a 1/log |sigma| coefficient does not fit that structure; what excludes it is Proposition 10.6, Lemma
11.21 and Proposition 13.18 at n = 4, now the argument. Proposition 10.7's write-out is (xvii), 10.39 (e); D178 and the
earlier 10.80 (c) and B-MAP 10.39 (e) said (xviii), corrected in place there and in ROUTES 4.101 and LOG D178. 10.83
(d): 10.43 (c) reaches RP through 10.46 (b). D179's marker count was wrong -- one line with a number and a full stop,
four with + or - -- corrected in place; the four numbered lines left (PROOF section 10.21, ROUTES 4.99 and 4.101, LOG
D177) are rewrapped. `iotasol5.py` J2 drops a conjunct true by construction ((9.21)'s end is computed, not checked);
`hthresh5.py` T7's control now moves the e' = 10 check to e' = 3 as well. The paper says what the rows use of the pole,
not its form. No row of READINGS.tsv changes.
