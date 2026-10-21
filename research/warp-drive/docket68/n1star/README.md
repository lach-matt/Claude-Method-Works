# n1star: N1* and the counterpart theorem (item 522)

The session commissioned at item 522 (`../../paper/INSTRUCTIONS-N1STAR-AND-HL-RESPONSE.md`). Start with
`N1STAR-PROOF.md`: **N1* is PROVED** (D21); what is proved, how it was verified and what no verifier has read
after the last edit are listed there. The response paper is `../../paper/RESPONSE-HL-5D.md`, with its check
`../../paper/response5.py` (D22-D23).

- `N1STAR-LOG.md`: M's words to this session, verbatim, and the session's decisions (D1-D49).
- `N1STAR-STATUS.md`: the first assessment (D6), kept as the record of the audit of Touati's smallness.
- `N1STAR-PROOF.md`: the proof as it stands. Theorem E (evolution), Theorem A (the approximant) and Theorem D (the data,
  solved outward in r), checked by independent verifiers (D12, D15, D16, D18-D21), every standard theorem they invoke
  READ at source (section 7, D17-D18); part (iii) and the mean-mass rate (section 8, D24-D30); Theorem P (section 9: the
  same solution from the record's data at past null infinity, D32), PROVED: one major gap found by a verifier and
  repaired (D34), the repair confirmed by a second (D35); and section 10, settling and the wavelength (D33). Start here.
- `ansatz5.py`: route W step 1, the geometric-optics ansatz on 5D Vaidya with the phase v (A1-A5).
  `python3 ansatz5.py --selftest` (5/5, about 3 minutes), `--mutants` (5/5).
- `foliation5.py`: route W steps 3 and 5, the null foliation, Touati's commutator lemma as an identity, the slices and
  the domain (B1-B4). `python3 foliation5.py --selftest` (4/4, seconds), `--mutants` (5/5).
- `ks5.py`: the coordinates of the proof, 5D Vaidya in ingoing Kerr-Schild form on R x R^4, regular at the T^2 axes;
  Touati's commutator lemma there as an exact identity (K1-K5). `python3 ks5.py --selftest` (5/5, about 2 minutes),
  `--mutants` (4/4, about 8 minutes).
- `lead5.py`: Theorem A's stage 0, the leading equation (E2) for the record's waves in the proof's gauge (L1-L5).
  `python3 lead5.py --selftest` (5/5, seconds), `--mutants` (4/4).
- `horizon5.py`: part (iii) for lam > 0, Proposition 8.1 (H1-H3, H2b). `python3 horizon5.py --selftest` (4/4, about
  a minute), `--mutants` (4/4).
- `mass5.py`: the mean-mass rate, Lemma 8.2 and Proposition 8.2 (M1-M4). `python3 mass5.py --selftest` (4/4, about two
  minutes), `--mutants` (5/5).
- `past5.py`: Theorem P, the construction from past null infinity (section 9): the past domain, the operator and the
  transport near past null infinity, the leading wave's decay, the stage-0 source, the rotations, and the flux of the
  record's radiation field, and the mollifier's commutator (P1-P8). `python3 past5.py --selftest` (8/8, about 4
  minutes), `--mutants` (9/9).
- `settle5.py`: late-time settling, linearly, on the copper study's barrier (seed_escape.py E1): the class's
  perturbation types, the potentials, the l = 2 ringdown against the published values, the settling times at the study's
  seeds (T1-T4); no growing mode for l = 2..10 to tau = 275 r_h and the late-time tail t^-7 against Cardoso, Yoshida,
  Dias and Lemos (T5-T6, section 10.3). `python3 settle5.py --selftest` (6/6, about a minute), `--mutants` (6/6).
- `growth5.py`: the go/no-go at the wavelength 10 l5 (ROUTES-OPEN.md section 2): the solver of
  `../lemmas/hf_mirror5.py` run on hf_core5's domain at lam = 10 l5 for mu0 = 100 and 1000 l5^2, the growth factor exp
  int K dv of the computed solution recorded at every step (two measures, fifteen maxima), the breakdown of the scheme's
  premise (a persistent second zero of the expansion, or the core boundary no longer outflow) and a finite-difference
  linear amplification (G0-G5, section 10.2): at both seeds the premise fails before the shell's peak (the second zero
  holds from v = 1.500 and 1.583, two and three grids agreeing, and the boundary ceases to be outflow at 1.516 and
  1.680; deeper excisions fail earlier), so no approximant on D_T comes from the record's scheme at 10 l5 at any
  excision depth. `python3 growth5.py --selftest` reads `data/growth5_runs.json` (G0 live, G1-G5 pinned, twelve runs);
  `--run L lam Ny Nx [delta] [v_end] [--yex Y]` regenerates one run (five minutes to an hour), `--merge` trims the run
  files into the data file, `--report`.
- `routes5.py`: the two computed facts behind ROUTES-OPEN.md's route for the mass at past null infinity:
  five-dimensional Vaidya's R_vv, and Tanabe, Tanahashi and Shiromizu's Bondi mass law as the class's P7
  density (Q1-Q2). `python3 routes5.py --selftest` (2/2), `--mutants` (2/2).
- `ROUTES-OPEN.md`: one proposed method for each of the three open items, with the literature READ (D36), and in
  section 4 the route for the decay of the gauge-vector system and the nonlinear settling (D46), with 4.6 W7, Hung's
  Proposition 4.2 in five dimensions, computed (D47), and 4.7 his Proposition 4.1 in five dimensions, deduced on it
  (D48; the proposition and its proof are N1STAR-PROOF.md section 10.5), and 4.8 the rungs, deduced (D49; section
  10.6). Nothing in the file itself is proved.
- `bondi5.py`: Theorem M, the Bondi mass at past null infinity (section 11): the five-dimensional Bondi hierarchy in
  the class with every coefficient from s^1 general (the orders below the waves' vanish; the mass law from R_vv at
  order r^-3), the chart from the wave-gauge expansion, the Hawking mass of the Bondi spheres, the numerics'
  coefficient (B1-B4). `python3 bondi5.py --selftest` (4/4, about ten minutes, B2 the slow one), `--mutants`
  (5/5), `--verbose` lists B1's and B2's sub-checks (until D47 the flag ran those two alone and exited 0).
- `wavegauge5.py`: the passage to the harmonic gauge on five-dimensional Tangherlini in the class (sections 10.4-10.5,
  Propositions 10.2-10.3; D42): the Lichnerowicz identity and Gamma[pi_X] = box X, the l = 0 stationary one-form W*
  regular at the horizon, the gauge-fixed mass change K* linear in t, the scalar gauge vector's three 1+1 equations per
  mode (l = 2, 4), the tensor type already harmonic, the gauge-vector system triangular, every rung a scalar wave
  equation whose potential obeys Hung's positivity condition (W1-W6), and Hung's Proposition 4.2 in five dimensions: in
  his components with the gauge condition admixed, box H = A H + U H with U along nabla_L in two rows, r^2 A_main with
  eigenvalues (l+a)(l+a+2), the horizon-regular rows with nabla_L' coefficients 2f', f' > 0, and l = 0 (W7; D47); and the
  identities of his Proposition 4.1 in five dimensions: the radiation field's potential, coercive at every l >= 2 where
  his has a zero at l = 2, the first-order term, the p-current, red-shift and T-current divergences, the angular
  eigenvalues on S^3, the k-degree of the matrices and l = 0 (W8; D48), on which Proposition 10.3 is deduced. `python3
  wavegauge5.py --selftest` (8/8, about seven and a half minutes, W7 and W8 most of them), `--mutants` (8/8, about six
  minutes), `--verbose` lists every sub-check, `--l4` runs W6 at l = 4 as well (72 minutes).
- `hung4.py`: the four-dimensional control of W7: Hung's Proposition 4.2 (arXiv:1909.06733) recomputed from the
  Schwarzschild metric with the instrument W7 runs, his seven rows as Appendix C combines them, reproducing the
  printed A, B and U rows and naming the two misprints in the printed combinations ((HG3) for (ME3) in row 7; f (ME3),
  M/r^3 and 4M(r - 2M)/r^3 in row 6) (C1-C2), and the red-shift divergence of his (2.13) at r = 2M for one component,
    whose c sigma/(4M^2)|Q|^2 and (c/(2M^2)) Q Q_R terms the print halves and omits (C3; D48). `python3 hung4.py
      --selftest` (3/3, about two and a half minutes), `--mutants` (4/4).
- `rungs5.py`: the rungs of the gauge-vector system (section 10.6, Propositions 10.4-10.5; D49): the Morawetz identity
  [HKW18] (123) at n = 3 for a scalar with potential and source; the positivity of its bulk for the Maxwell potential -4
  mu/r^4 and the free rung with [HKW18]'s f and beta = 1/(2 sqrt mu) and half the angular term borrowed, certified by a
  Sturm count on a polynomial of degree ten (W > 0 on the exterior, W >= r^-3/5 and r^-3/7; W0 alone is not); Hung's
  (A.3) with room; the radiation variable's V_inf = k^2 + 3/4 and the p-current with the source; the g-current (M1-M5).
  `python3 rungs5.py --selftest` (5/5, about half a minute), `--mutants` (6/6).
- `growing5.py`: the growing source (section 10.7; D50): [KI03]'s master equation and reconstruction at n = 3 checked
  against the Einstein equations; J = -Gamma[h_RW] in h_RW's components; the direct system (Hung's (4.21)-(4.23) in five
  dimensions); the rung sources in canonical form with their bad weights; the substitutions (Hung's (4.27)-(4.30)) and
  the residual sources, every weight checked (G1-G5). `python3 growing5.py --selftest` (5/5, about twelve minutes),
  `--mutants` (5/5).
- `lzero5.py`: the l = 0 sector (section 10.8; D50): the identities of Hung's section 8 in five dimensions -- the
  components of box W, P = r (dW)_tr - 2 W0 with box_s P = d_t S_W, the (W0, W3) form with the red-shift sign, c_1(oo),
  the two radial ODEs and their singular solutions, the substitution P + (u + r) S_W/2 (Z1-Z5). `python3 lzero5.py
  --selftest` (5/5, about a quarter of a minute), `--mutants` (5/5).
- `data5.py`: Theorem D, the facts about the approximant's slice data that the outward evolution of the constraints
  uses (S0-S6). `python3 data5.py --selftest` (7/7, about 14 minutes), `--mutants` (6/6, about 80
  minutes), `--show` (the principal part).

All seventeen are stdlib plus sympy (foliation5.py also uses z3; settle5.py numpy and scipy; bondi5.py and growth5.py
numpy, growth5.py importing the solver `../lemmas/hf_mirror5.py` and `hf_core5.y_core` beside it, past5.py importing
lead5.py), growing5.py and lzero5.py import wavegauge5.py, and the others import nothing from the tree. The board's
shared record is not edited here.