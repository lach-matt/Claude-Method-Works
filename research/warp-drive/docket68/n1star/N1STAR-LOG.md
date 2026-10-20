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
reverse statement is their Corollary 1.14, on a domain short in one null direction; the boundary spacelike only for mu0
> sqrt(72) l5^2; nothing is claimed beyond Omega, not beyond x = 1; the g_lam margin -delta + C lam; Q's linear and
constant parts; k = 6 only; uniqueness among C^2 solutions; R1 made exact (symbolic 2-jets in normal coordinates of
g3), K for mu(v) added to R3, R6's controls run one at a time; z3-solver listed. The retitling M set (D24) is applied.

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

**D44 (2026-10-20): the thirteenth verifier -- D38-D41, the repairs of D40, sections 10.2 and 10.3.** Two major
findings. (1) Lemma 11.0 ran Lemma 9.5's identity on the region between {v = v_start} and Sigma_tau, which is unbounded
toward past null infinity, where the flux of d^gamma u_1 is known to vanish only at the orders Theorem P controls (k =
6): the twelfth verifier's gap was moved, not closed. Repaired by running the identity for each approximating solution
g_n of Proposition 9.8 on P cap {tau_n <= tau' <= tau}, the region of (9.8)'s own identity, where the data on
Sigma_tau_n are the approximant's residual, explicit, with constants independent of n, and passing the bounds to the
limit by Arzela-Ascoli; the sup-against-L^2 bookkeeping is written (floor((N + 2)/2) <= max(4, N - 3)). The verifier
proposed a finite derivative budget instead; k = 6 is fixed in Theorem P, so that route would re-run section 9 at a
higher k, and the one taken keeps every order. (2) Section 10.2's break time at the first seed, 1.4516 / 1.4508, was a
single step of the root count on both grids, and the amplification 1.00 was sampled before the field had grown: the grid
agreement supported a transient, not a persistent second zero -- as D43's criterion had found the same day. Nine minor
findings and notes, all seated: Proposition 11.2(i)'s nullity argument used the transverse Jacobi field d_{v0} gamma
with the false g0(ell, d_v) = 0 (now gamma' and d_{xhat0} gamma only, with the limits in E_1) and called -(2/r) xi' a
Lipschitz perturbation (it is the unperturbed angular operator); Proposition 11.2(iv) had e^{-2b} = 1 + 2 d_v ů (the
factor is 1, as B2 computes); "an order" is one power of r, two of s, in Theorem M(a) and Proposition 11.3's hypothesis;
Proposition 10.1(iii)-(iv) hid a factor H ~ l^2 in Phi~ (the two derivatives lost are orbit-space for F_ab and angular
for F) and left the l = 0 gauge unfixed (h_0 = c K, now stated); the even-l claim for the tensor type is not needed and
no longer made; T5's region r* in [-20, 50] was covered by the computed slice only to tau = 175 at T = 120 (now T = 170,
covered to 275, the checks restricted to the covered range, the figures unchanged to two digits), and its verdict is a
finite-time observation (rates above 0.08/r_h excluded); T6's "approaching 7 from above" is origin-dependent at that
level (the origin shifted by the launch radius gives 6.89 and 7.23; that the pair brackets 7 is now checked); 10.2's
"ceases to be trapped" and "ceases to be outflow" are given one meaning each, and the amplification is called the lower
bound it is. Open: the literature identifications ([KI03] (3.13)-(3.14), [HKW18] (169)-(186), [CYDL03] (14)) could not
be re-fetched by the verifier (403) and stand as READ by this session. Attacks that held: Lemma 11.2's coefficient 2/(k
- 3) and G_4 = 2 int S_3, the induction at J = 3, Proposition 11.3(0) with its controls, the ODE classes of 11.2(i),
10.3's regularity at the horizon and the absence of l = 1, settle5 6/6 with mutants 6/6, growth5's fields against
hf_mirror5's form and every figure of 10.2 from the pinned data, no line over 121 characters, no model identifier. The
repairs of this entry, D42's section 10.4 and D43's deeper excisions have not been read by a verifier.

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
