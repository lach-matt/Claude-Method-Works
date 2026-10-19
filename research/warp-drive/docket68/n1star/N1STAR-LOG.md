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
`foliation5.py` (B1-B4; selftest 4/4, mutants 4/4). Two results beyond the handoff: (1) the structure of Touati's
commutator lemma holds on five-dimensional Vaidya exactly, [L0, box~] u = (2/r)(d_r(L0 u) + 2 d_v(L0 u) + box~ u)
for the principal part, with a first-order remainder for the covariant operator (B3, corrected at D8); (2) the
record's two-quadrature waves produce, at order lam, a non-oscillating term
R_v th = F0^2 d_th phi, phi = (1/2) arctan(cos 2th), which Touati's single-cosine ansatz never has and which needs a
mean O(lam) metric correction (A5).

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
