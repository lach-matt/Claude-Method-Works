# Instructions: finish N1* and the counterpart theorem, then write the response paper to Huneau and Luk

**For a new session.** You are commissioned to finish one open lemma, N1*, and with it the five-dimensional counterpart
of Huneau and Luk's high-frequency theorem (THM-HF5). Then you are to write a formal paper that answers their theorem.
These instructions are self-contained: you have not seen the conversation that built the proof, and you do not need
it. Everything is in the repository, on the branch and at the paths named here.

## 0. The commission, in the author's words

The author (M, Matthew Lach, the byline the tree's papers use) wrote on 2026-10-19, item 522 of
`research/warp-drive/docket68/M-RULINGS-2026-10-03.md`:

> "Prepare instructions for another session to finish N1* and the counterpart theorem, and then right a formal
> response paper to the Huneau and Luk's theorem. That session will need access to all you work on the proof, so
> it'll all need to be pushed to the repo and identified there for the other session"

The board session that built the proof keeps working on other parts of the theory (SOURCE) in parallel.

## 1. Where the work is

- **Branch:** `claude/warp-drive-theory-ditjk4` of `lach-matt/Claude-Method-Works`. It is not merged to `main`.
  Fetch it and base your own branch on it:
  ```
  git fetch origin claude/warp-drive-theory-ditjk4
  git checkout -b <your branch> origin/claude/warp-drive-theory-ditjk4
  ```
  The last commit that touches this file is the handoff point (first made at item 522, brought forward to the
  branch's head at item 524):
  ```
  git log -1 -- research/warp-drive/paper/INSTRUCTIONS-N1STAR-AND-HL-RESPONSE.md
  ```
- **Every file of the proof is listed with its md5 in `research/warp-drive/docket68/handoff-n1star/MANIFEST.tsv`.**
  The md5s are those of the handoff commit. The record files (rulings, write-ups, register) keep growing on the board
  branch after it, so check their md5s at the handoff commit.
- **Since the first handoff (522) the board has continued SOURCE, not N1*.** `docket68/lemmas/seed_escape.py`
  computes the seed's escape at 10 l5 by linear scattering (SOURCE-REQUIRED "Item 522", BOUNCE-RESEARCH section 54).
  It is not part of the commission and N1* does not rest on it, nor it on N1* (521). Nothing else in the proof has
  changed: the instruments listed in the manifest are byte-identical to 522's.
- **The scratch derivations** behind items 517-520 are in `research/warp-drive/docket68/handoff-n1star/scratch/`, with a
  README saying what each derives. The seated instruments are authoritative.

**Do not edit the board's shared record.** That means `M-RULINGS-2026-10-03.md`, `WARPTHEOREM.md`, `chainmap.html`,
`warptheorem.py`, `lemmas/SOURCE-REQUIRED.md` and `lemmas/BOUNCE-RESEARCH.md`. The board session edits them on its own
branch, and two branches editing them will collide. Put your work in new files:
- instruments in `research/warp-drive/docket68/n1star/`;
- the paper in `research/warp-drive/paper/`;
- a log, `research/warp-drive/docket68/n1star/N1STAR-LOG.md`, where you record M's words to you verbatim with dates
  and your decisions.

The board session will integrate your results into the record when M directs.

## 2. What is being proved

**THM-HF5** (item 511; statement verbatim in `lemmas/hf_theorem5.py`). Let mu0 >= sqrt(72) l5^2, A > 0 and env smooth
with compact support. For lam in (0, lam0], let g_lam be the five-dimensional vacuum metric with T^2 symmetry and both
reflections whose free data at past null infinity are
- F = lam A env(v) h(x) sin(v/lam), G = lam A env(v) h(x) cos(v/lam), with h = sqrt(2/(1 + x^2)),

on the seed of mass mu0 before the shell. Let D be the region from past null infinity to the record's quantum boundary
x = l5^2 sqrt(K) = 1 of the limit, r >= r_q(v) = (sqrt(72) mu(v) l5^2)^(1/4). Then:
- (i) g_lam exists on D for every lam <= lam0;
- (ii) g_lam -> g0 uniformly on D, with |g_lam - g0| = O(lam) and d g_lam bounded and weakly convergent, where g0 is
  five-dimensional Vaidya with mu' = (2/9) A^2 env^2; the mean mass converges at O(lam^2);
- (iii) one zero of the outgoing expansion per column (no inner apparent horizon); the horizon converges at O(lam);
- (iv) x = 1 is spacelike and every characteristic leaves D through it.

**The counterpart theorem** (item 520, `lemmas/counterpart5.py` P5) is THM-HF5 on
D_T = D ∩ {v <= v_end + T}, for each fixed T. Huneau-Luk's and Touati's theorems hold on a fixed time interval too.
Settling for all later v is the nonlinear stability of five-dimensional Tangherlini in the class, which is open and is
not part of the commission.

**N1\*** (open, named at 520). For lam <= lam0, the vacuum solution with the record's data exists on D_T, and its
remainder after the geometric-optics approximant obeys energy estimates uniform in lam. Three conditions apply:
- the formulation loses no derivatives;
- it is regular across the axes, the fixed points of the T^2 action;
- it works on the large background g0: five-dimensional Vaidya, black hole included, interior to x = 1.

With N1* proved, (i) follows, and the rates in (ii)-(iii) follow from the estimates. (iv) and the limit are already
exact.

## 3. What is already in hand, and what was corrected

**In hand.** Each item is listed with its evidence; re-run it before relying on it.

- **(iv)**: x = 1 is spacelike, and every characteristic leaves D. Computed, exact; Z3. Evidence: hf_theorem5 F2.
- **The limit**: averaged waves are null dust, and g0 is Vaidya with Isaacson's flux mu' = (2/9) A^2 env^2.
  Computed, exact; Wolfram; Lean. Evidence: hf_theorem5 F3, `lean/HFTarget.lean`.
- **v is null at every lam.** No component holds a second v-derivative, the hypersurface equations hold no
  v-derivative, and the one product of rates is the dust. Computed, exact. Evidence: hf_theorem5 F5.
- **The sequence's rates**, at two seeds: the C^0 departure halves, the mean mass quarters, the horizon departure
  halves. Computed, numerical. Evidence: hf_core5, hf_theorem5 F4.
- **K = 72 mu^2/r^8**, and the waves are high-frequency on all of D once lam < l5/10. Computed, exact. Evidence:
  counterpart5 P1.
- **Every Gronwall constant is lam-independent** (the crude exponent is 1.384e4 at every lam). Computed. Evidence:
  counterpart5 P1.
- **The exact reduction**: in the class, 5D vacuum is 2+1 gravity on h = rho^2 g3 with
  R[h] = (3/2) dpsi^2 + 2 domega^2 and box_h psi = box_h omega = 0. Computed, exact. Evidence: kn_gauge K1-K2.
- **A multiplier bounds T^2-invariant test fields** on growing Vaidya, across the horizon to x = 1, with constant 35.
  Computed. Evidence: kn_gauge K5.

**Corrected at 520. Do not repeat these errors:**
- **The KN (Bondi-type) gauge loses two angular derivatives.** Its theta-theta equation fixes h_vv through
  d_theta^2 h_vr, and h_vv is the coefficient of d_r^2 in box_h (counterpart5 P2). Do not prove N1* in it. Use it to
  compute, not to estimate.
- **The class's linear problem is linearized gravity, not the test-field wave equation.** The background Killing norms
  psi0 = ln(r^2 s c) and omega0 = (1/2) ln(c/s) are not constant. The linearization of their wave operator in the base
  metric holds h_vv, d_r h_vv, d_theta h_vr and d_r h_vth with O(1) coefficients (counterpart5 P3). On a fixed domain
  that coupling only enters a fixed constant; you still have to estimate it.
- **The "seed phase" and the "0.21 second order" of 517 are not part of the counterpart theorem.** They belong to the
  application at 10 l5 (counterpart5 P1). Do not treat them as obstacles to N1*.

## 4. Read first, in this order

1. `docket68/lemmas/hf_theorem5.py`: the theorem, F1-F7, and its notes at 514 and 520.
2. `docket68/lemmas/counterpart5.py`: P0-P5, the measurement of what is left.
3. `docket68/lemmas/kn_gauge.py`: the reduction (K1-K4), the multiplier (K5), K8, and the 520 notes on K5, K6 and K8.
4. `docket68/lemmas/SOURCE-REQUIRED.md`: items 497 to 521, newest first (522's SOURCE part is not N1*).
5. `docket68/lemmas/BOUNCE-RESEARCH.md`: sections 44-53 (section 54 is SOURCE's).
6. `docket68/lemmas/hf_core5.py` and `src_hole.py`: the computed sequence and the seed.
7. `docket68/lemmas/gauge5.py`: ten gauges against the five needs.
8. M's words for items 497-524 in `docket68/M-RULINGS-2026-10-03.md`. The rulings that bind you are listed in section 8
   below.

## 5. Reproduce before you work

Run each selftest from `research/warp-drive/docket68/lemmas/` and confirm the counts:
- `hf_theorem5.py --selftest` (7/7)
- `hf_core5.py --selftest` (10/10)
- `hf_anchor5.py --selftest` (5/5)
- `gauge5.py --selftest` (7/7)
- `kn_gauge.py` (18/18; it reads its cached core, and `--build-k8` rebuilds it in about three minutes)
- `counterpart5.py --selftest` (8/8)
- the mutants of the last two (10/10 and 4/4)

The full register selftest (`python3 warptheorem.py --selftest`, 12/12) takes about 80 minutes; run it once, in the
background. Python 3.11 with numpy, sympy and mpmath. `pip install z3-solver` gives Z3. Lean 4.33 core is restored in
cloud sessions by `.claude/hooks/session-start.sh` (`sci check lean`). The Wolfram connector, if attached, cross-checks
symbolic work; label Mathics3 results "computed (Mathics3)".

## 6. Re-READ every outside source at source

Read these yourself and quote verbatim, with page or equation. Do not rely on the board's summaries.
- **Huneau and Luk**, "High-frequency backreaction for the Einstein equations under polarized U(1)-symmetry", Duke
  Math. J. 167 (2018) 3315-3402, arXiv:1706.09499. This is the theorem you answer: state it exactly, with its
  hypotheses (small data, elliptic gauge, the time interval, the class of backgrounds).
- Huneau and Luk, arXiv:1907.10743 (trilinear compensated compactness, the direct direction); their review,
  arXiv:2404.07659; arXiv:2506.21779 (U(1), from Einstein-dust to Einstein-Vlasov).
- **Touati**, Commun. Math. Phys. 402 (2023) 3109, arXiv:2206.12318, Theorem 2.2. Note where the smallness (2.9) and
  the planar phase (2.10) enter, and the derivative loss regained by a null foliation and a Fourier cut-off. Also
  arXiv:2206.13062 (constraints) and arXiv:2402.17530 (multiphase).
- **Luk and Rodnianski**, arXiv:2009.08968 (double null, local, 3+1).
- Giannakopoulos, Hilditch and Zilhao, Phys. Rev. D 102, 064035 (2020): Bondi-like gauges are weakly hyperbolic.
- Choquet-Bruhat 1969 (the WKB construction); Burnett 1989; Isaacson 1968.
- For the linear problem: Kodama and Ishibashi, Prog. Theor. Phys. 110 (2003) 701 and 901; Dafermos and Rodnianski,
  the red-shift effect (CPAM 2009); Schlue, Anal. PDE 6 (2013) 515.
- For uniqueness and the end state: Hollands and Yazadjiev, Commun. Math. Phys. 283 (2008) 749.
- Rendall 1990 (the characteristic problem) if you keep characteristic data.

## 7. The routes, and what each must settle

**Route W: five-dimensional generalised wave gauge, Touati's construction carried to 4+1 and a large background.**
Recommended. In 5D coordinates the T^2 axes are smooth points, symmetry is preserved by uniqueness, and wave gauge
has no angular loss. It must settle:
1. **The ansatz.** The ansatz to order lam^2 on Vaidya with the ingoing phase v (null for g0). Find the 5D
   polarization conditions and the 5D energy condition, the analogue of Touati's (2.28). Check them against F3's
   computed dust identity, -2 (P1_v^2 + P1_v P2_v + P2_v^2).
2. **Smallness.** Where Touati uses smallness ((2.9), (2.10), the closing of his bootstrap), replace it on the fixed
   domain. Bootstrap on short slabs with lam-independent constants and continue across D_T. Every constant must be
   independent of lam; counterpart5 P1 shows the approximant's ones are.
3. **The derivative loss** between the transport and wave equations: Touati's null foliation (here the ingoing cones
   v = const, regular on D) and his Fourier cut-off.
4. **The data.** Either construct Cauchy data on a slice before the shell reaches the hole, solving the 5D constraints
   with the ansatz (Touati's arXiv:2206.13062 in 4 space dimensions), or justify the characteristic data at past null
   infinity. Whichever you choose, restate (i) on it, with the label, and keep it equivalent to the record's run data.
5. **The interior** to x = 1. D is the data's domain of dependence, and its inner boundary is spacelike (hf_theorem5
   F2). The ingoing cones' caustic at r = 0 lies outside D.

**Route D: double null in five dimensions** (Luk and Rodnianski's, with S^3 sections). Angular regularity comes from
elliptic estimates on S^3, which also handle the axes. It needs the 4+1 Bianchi structure; longer.

**Do not use** the KN or Bondi gauge, or the reduced 2+1 system near the axes (the torus frame degenerates there).

**What a finished N1\* looks like.** A proof, every step labelled:
- computed: exact identities with an instrument and a selftest whose mutants it catches;
- deduced: standard arguments, with the theorem invoked READ and its hypotheses checked;
- READ.

Plus constants evaluated where the argument has them. Seat it as instruments in `docket68/n1star/`, each with
`--selftest` and `--mutants`. If N1* cannot be finished, stop and report exactly what is proved and what is left. Do
not write a paper that claims the theorem.

## 8. M's rules that bind you

- **PROVED** means a computed solution meeting the specification, consistent with established physics (440, 441).
  For the paper, "proved" means proved: every claim carries its label.
- **Prior art first** (442): read what exists before computing what it leaves.
- **No inner or Cauchy horizon and no bounce** (481, 484, 519). The domain ends at the spacelike x = 1. Nothing is
  excised.
- **No proof for every lambda before SOURCE**: 509 placed that proof after the SOURCE work. M has now commissioned it
  here (522), so it is yours to do.
- **Work inline**, with no multi-agent workflows. Send **one** independent verifier at a time (249). Report, then
  pause. Be efficient and concise (475).
- **Don't guess, run the hypothesis.** Kill processes by exact PID; never `pkill -f`. Keep lines at 121 characters or
  fewer. Put no model identifiers in any file. Do not scan the corpus tree wholesale (the repository's `CLAUDE.md`).

## 9. The paper: a formal response to Huneau and Luk

Write it once N1* is proved and verified.

**Location.** `research/warp-drive/paper/`, as Markdown beside the tree's papers, with a check script that re-derives
its numbers. A PDF render is optional and comes after the audit.

**Title.** Propose one and mark it "proposed"; titles are the author's.

**What "response" means here.** State Huneau and Luk's theorem exactly, then answer it with the five-dimensional
counterpart:
- what carries over: the reduction to a 2+1 system, here with two scalars, psi and omega, whose target form is flat
  and positive definite;
- what changes: one more dimension; the T^2-mirror class, with its axes; a large black-hole background instead of
  small data; data at past null infinity; the interior to a spacelike boundary;
- what the proof needed beyond theirs.

Also say what your result does not reach: settling at late times, and the application at physical wavelengths.

**Public form.** The paper must stand without the board's record. Cite nothing from the corpus volumes under
`method/` or `drive/`. Do not use the board's internal row names as evidence. Do not use the research tree's
directory name in the paper's text: the site guard refuses it (see the repository's `CLAUDE.md`). Whether and where
the paper is released is M's decision.

**A structure to adapt, not a template:**
1. Abstract.
2. Introduction: the Burnett conjecture, Huneau and Luk's theorem, why five dimensions and a black hole.
3. Setting: the class, the reduction (exact), the background, the data.
4. The theorem: statement on D_T, with its constants.
5. The approximant: phase, profiles, the dust, the limit.
6. Proof of N1*: the gauge, the energy estimates, the bootstrap, the derivative loss regained.
7. The remaining parts: (iii) and (iv).
8. Relation to Huneau and Luk, Touati, and Luk and Rodnianski, point by point.
9. What is not proved.
10. References, each READ, with identifier and page.

**Appendices:**
- A: every computation, with its instrument and check;
- B: M's words verbatim, with item numbers, as the author's postulates where they enter;
- C: a source map from each claim to its file, check, run or quotation;
- D: reproduction steps and the md5 table.

## 10. Audit, then report

- When N1* and the paper pass their checks, send **one** independent verifier: read-only, re-deriving with its own
  code, and re-READing the quotations. Check its real status before reporting on it.
- Seat every finding beside the text, or answer it with a reason.
- Commit and push your branch at each milestone. Do not open a pull request unless M asks.
- Then report to M:
  - what is proved, and on what;
  - what the verifier found;
  - what is left;
  - what needs the author: the title, release, and any scope question.
- The board session will integrate the result into the register and the map when M directs.
