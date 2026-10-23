# n1star: N1* and the counterpart theorem (item 522)

The session commissioned at item 522 (`../../paper/INSTRUCTIONS-N1STAR-AND-HL-RESPONSE.md`). Start with
`N1STAR-PROOF.md`: **N1* is PROVED** (D21); what is proved, how it was verified and what no verifier has read
after the last edit are listed there. The response paper is `../../paper/RESPONSE-HL-5D.md`, with its check
`../../paper/response5.py` (D22-D23).

- `N1STAR-LOG.md`: M's words to this session, verbatim, and the session's decisions (D1-D75).
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
- `hierarchy5.py`: the first rungs' rapid decay (section 10.9; D51): Hung's Proposition A.5 at k = 1 in five dimensions
  -- the commuted equation of the radiation field, the p-current identity for the commuted field, his conditions (A.3),
  (A.5), (A.7)-(A.9) with the radii and constants at four modes, and the l = 0 obstruction (V_inf = 3/4, V^(1)_inf =
  -5/4) (H1-H4). `python3 hierarchy5.py --selftest` (4/4, about a minute), `--mutants` (6/6).
- `coupled5.py`: the coupled estimate for the last two components of the gauge vector (section 10.10; D52): Hung's
  section 6 in five dimensions -- the identities (6.8)-(6.10) and a fourth, the pair's matrix, the T-current with exact
  positivity, the Morawetz current for a pair and its bulk, positive for every k^2 >= 8 without Hung's substitutions and
  uniform in l, and the r^p current (K1-K6). `python3 coupled5.py --selftest` (6/6, about a minute), `--mutants` (6/6).
- `lzerorate5.py`: the l = 0 sector by another route (section 10.11; D53): the commuted hierarchy at l = 0 with V^(1)_inf
  = -5/4 absorbed by a Hardy inequality on the outgoing leaf for p < 1, the window exact at R_null = 10 r_h, the base
  hierarchy at l = 0 without an angular term, and the cut-off source of P-hat (Y1-Y5). `python3 lzerorate5.py --selftest`
  (5/5, about forty seconds), `--mutants` (7/7).
- `damping5.py`: route B's constraint damping in five dimensions (section 10.12; D54): the indicial roots of [Hin26a]'s
  constraint propagation operator on 4+1 Minkowski from the definitions, the trace weight 2/(D - 2), and the exact
  certificate at a point below the five-dimensional bound of his Lemma 4.4, h < e chosen here, the strip [-100, 2] free
  but for the Coulomb root at l = 0 and 1, his four-dimensional formulas as the control (U1-U6). `python3 damping5.py
  --selftest` (6/6, about eighty seconds), `--mutants` (6/6).
- `semiclass5.py`: the semiclassical inputs of the constraint damping in five dimensions (section 10.13; D55):
  [Hin26a]'s fibrewise theory at the weight 2/(D - 2), the subprincipal symbol from its definition (his four-dimensional
  formulas as the control, one misprint named), the weight thresholds at the critical sets, the interior saddle's
  positivity with its admissible e, and the admissibility of damping5.py's point (W1-W6). `python3 semiclass5.py
  --selftest` (6/6, about a minute), `--mutants` (6/6).
- `cform5.py`: a constraint damping 1-form of [Hin26a] Proposition 5.1's kind on five-dimensional Tangherlini (section
  10.14; D56): one explicit c in Kerr-Schild time, its conditions (1), (3) and (6) checked exactly on the Tangherlini
  metric at damping5.py's point, (4)-(6) on sf, and the smallest r_0 measured (C1-C7). `python3 cform5.py --selftest`
  (7/7, about a minute and a half), `--mutants` (7/7).
- `gaugepot5.py`: the gauge potential operator of [Hin26] section 6 in five dimensions (section 10.15; D57): its
  indicial roots on 4+1 Minkowski, its zero energy mode equations on Tangherlini and the identities that leave W* the
  only kernel of the unmodified operator, the cokernel functional at the horizon, and the pairings of his Lemma 6.11 and
  (6.26), his four-dimensional values as the control (G1-G7). `python3 gaugepot5.py --selftest` (7/7, about a minute and
  a half), `--mutants` (7/7).
- `modes5.py`: mode stability of the 1-form wave operator -- the gauge potential operator with E^Upsilon = 0 -- at
  nonzero frequency on five-dimensional Tangherlini (section 10.16; D58): box = d delta + delta d on every 1-form, and
  the scalar-wave and Maxwell master equations on arbitrary harmonics, with their potentials positive at l >= 1 and the
  l = 0 Maxwell sector by its own equation (M1-M5). `python3 modes5.py --selftest` (5/5, under a minute), `--mutants`
  (5/5).
- `trap5.py`: the trapping input of the high-energy mode stability in five dimensions (section 10.17; D59): the
  subprincipal operator of the 1-form wave operator, the photon sphere r^2 = 2 mu as the trapped set with its expansion
  rate, and Hintz's frame with its nilpotent connection on Tangherlini, so that the gauge potential operator is strongly
  trapping admissible (T0-T4). `python3 trap5.py --selftest` (5/5, about 12 seconds), `--mutants` (5/5).
- `thresh5.py`: the structure and threshold quantities of the gauge potential operator in five dimensions (section
  10.18; D60): its Minkowskian form -2 d_t* rho (rho d_rho - 3/2 - S-bar) with S-bar and its spectrum, the horizon
  threshold 3/2 under 10.15's horizon modification (deduced), and Tangherlini's decay to Minkowski (U1-U4). `python3
  thresh5.py --selftest` (4/4, about 8 seconds), `--mutants` (4/4).
- `hienergy5.py`: the remaining inputs of Hintz's high-energy and Fredholm estimates in five dimensions (section 10.19;
  D62): the threshold at the incoming radial set, -1/2 - S-bar (deduced), the photon sphere's hypotheses with its gap
  and loss, and the global dynamics, dr future timelike inside (V1-V4). `python3 hienergy5.py --selftest` (4/4, about 25
  seconds), `--mutants` (6/6).
- `lowenergy5.py`: the five-dimensional inputs of Hintz's low-energy theory (section 10.20; D64): the transition face
  model on 4+1 Minkowski, its Bessel reduction, the outgoing solution excluded exactly below 2 (the lower end 0 READ),
  and the weights (L1-L3). `python3 lowenergy5.py --selftest` (3/3, about 7 seconds), `--mutants` (4/4).
- `cpmodes5.py`: the five-dimensional steps of Hintz's deduction of the constraint propagation operator's mode stability
  (section 10.21; D66): its endomorphism at infinity with three angular copies, the radial sets and (B.13)'s l-window
  (deduced), and the weights (K1-K3). `python3 cpmodes5.py --selftest` (3/3, about 5 seconds), `--mutants` (3/3).
- `solv5.py`: the remaining five-dimensional inputs of Hintz's solvability theorem for the constraint propagation
  operator (section 10.22; D67): Tangherlini a 3sc-metric with two powers to spare, the time functions of his energy
  estimates near X and inside the black hole, and his Proposition 5.1 (4)-(5) at the weights of 10.21 (Q1-Q4). `python3
  solv5.py --selftest` (4/4, about 15 seconds), `--mutants` (4/4).
- `tface5.py`: the five-dimensional inputs of Hintz's transition face theorem for the constraint propagation operator
  and of the tf-admissibility that follows from it (section 10.23; D69, D71, D72), at (v, e) = (1/2, 1/102400) and for
  C_0 <= 100: the operator on 4+1 Minkowski homogeneous of degree -2, the weights (0, 2 + C_0] at the origin, the
  threshold at the cone face (the sink's is 10.22's, met), his section B.4's weights, data and closing integral, the
  weights beta' of both halves of tf-admissibility, the adjoint's from the conjugated adjoint's computed spectrum, and
  the free roots and counts of his index-0 argument (F1-F5; Theorem B.1 and tf-admissibility for beta in [-C_0, 2)
  deduced in 10.23, at h = 10^-6 if below h_0). `python3 tface5.py --selftest` (5/5, about 25 seconds), `--mutants`
  (8/8).
- `lin5.py`: Hintz's Lemma 8.4 in five dimensions, the indicial roots of the linearized gauge-fixed Einstein operator on
  4+1 Minkowski by harmonic type, the tensor type included (section 10.24; D72, D73): the types preserved and his (8.5)
  at two points, the factorization det N_L = c (lam + l)(lam - l - 2) det N_Ups(lam - 1) det N_C(lam + 1) / D with every
  parameter symbolic, his four-dimensional factorizations as the control, the factors checked against gaugepot5.py and
  damping5.py, and at one parameter point, for l <= 12, the roots simple, none with real part in (0, 1], each type split
  evenly and Lemma 8.5 (E1-E5; Lemma 8.4 for every l at that point, Lemma 8.5 and, but for one threshold, Proposition
  8.6 for small gam_Ups deduced in 10.24). `python3 lin5.py --selftest` (5/5, about 50 minutes), `--mutants` (4/4, about
  20 minutes).
- `sbar5.py`: Hintz's Lemma 8.2 and (8.7) in five dimensions (section 10.25; D74): the endomorphism S-bar by which the
  linearized gauge-fixed Einstein operator's d_t* terms differ from the wave operator's on 4+1 Minkowski, its spectrum
  -- the gauge potential and constraint propagation operators' with five zeros, min spec S-bar = 0 -- and the decay
  3/2 - eps and thresholds it gives (S1-S3; Proposition 8.6 deduced on readings in 10.25, at Proposition 10.9's point
  for small gam_Ups). `python3 sbar5.py --selftest` (3/3, about a minute), `--mutants` (3/3).
- `strap5.py`: Hintz's Proposition 8.3 in five dimensions (section 10.26; D75): the subprincipal matrix of the
  linearized gauge-fixed Einstein operator at the trapped set -- his printed 10 x 10 reproduced in four dimensions with
  his sign, and with 10.17's after e_1 -> -e_1, the 15 x 15 in five with its spectrum and a constant triangularizing
  basis, and, for a c with no angular part, the rotation-adapted block triangular form (P1-P3; strong trapping
  admissibility on Tangherlini deduced in 10.26). `python3 strap5.py --selftest` (3/3, a few seconds), `--mutants`
  (3/3).
- `gmodes5.py`: mode stability of the linearized Einstein operator on five-dimensional Tangherlini at sigma != 0, the
  input [Hin26] Proposition 8.8 takes from [AHW24] (section 10.27; D78): the Kodama-Ishibashi reduction of D Ric
  computed for every harmonic at a point of S^3 -- the tensor, vector and scalar types' master equations, their
  potentials positive at l >= 2, the scalar type through [KI03]'s first-order system and one constraint, l <= 1 pure
  gauge at sigma != 0 -- and the horizon in ingoing coordinates (G1-G5; Proposition 8.8 deduced in 10.27). `python3
  gmodes5.py --selftest` (5/5, about five minutes), `--mutants` (5/5).
- `zstates5.py`: [Hin26] section 6.5.1 and Proposition 8.9 in five dimensions (section 10.28; D80, D82): Tangherlini's
  orders against Minkowski (g - gbar at rho^2, Gamma at rho^3, r* without a logarithm), the defects of the asymptotic
  translations and boosts, the rotations Killing (V_1 = so(4)), the linearized metrics d_mu g and h_A -- the derivatives
  at zero rotation of the one-spin Myers-Perry family, checked Ricci-flat at exact points -- with their gauge sources
  (delta G h_A = 0, E^Ups h_A at rho^4), and the needed exponents against box^Ups(0)'s indicial roots, four-dimensional
  Schwarzschild the control (Z1-Z6; Propositions 6.15 and 8.9 deduced in 10.28 on Lemma 6.13, which 10.29 deduces on
  10.20's readings). `python3 zstates5.py --selftest` (6/6, about half a minute), `--mutants` (7/7).
- `genstates5.py`: [Hin26] Lemma 6.13 and Proposition 6.18 (1)-(3) in five dimensions (section 10.29; D81): the
  generalized zero energy states on the time translation, the boosts carried to second order and the rotations, their
  leading terms solved exactly on 4+1 Minkowski with E^Ups, part (1)'s Tangherlini source without a rho^2 term, his
  printed four-dimensional numbers and (6.40) as the control, and the gap's top lam_s1,2 = 2 + z/12 + O(z^2) (H1-H5;
  Lemma 6.13, on 10.20's readings, and the states deduced in 10.29). `python3 genstates5.py --selftest` (5/5, about a
  minute), `--mutants` (8/8).
- `data5.py`: Theorem D, the facts about the approximant's slice data that the outward evolution of the constraints
  uses (S0-S6). `python3 data5.py --selftest` (7/7, about 14 minutes), `--mutants` (6/6, about 80
  minutes), `--show` (the principal part).

All thirty-eight are stdlib plus sympy (foliation5.py also uses z3; damping5.py, semiclass5.py and lowenergy5.py mpmath,
and so every program importing them; settle5.py numpy and scipy; bondi5.py and growth5.py numpy, growth5.py importing
the solver `../lemmas/hf_mirror5.py` and `hf_core5.y_core` beside it, past5.py importing lead5.py), growing5.py,
lzero5.py and coupled5.py import wavegauge5.py, lzerorate5.py imports hierarchy5.py, semiclass5.py imports damping5.py,
cform5.py imports semiclass5.py and damping5.py, gaugepot5.py imports damping5.py, modes5.py imports gaugepot5.py and
damping5.py, trap5.py and thresh5.py import gaugepot5.py, damping5.py and modes5.py, hienergy5.py imports gaugepot5.py,
damping5.py, thresh5.py and trap5.py, lowenergy5.py imports thresh5.py and damping5.py, cpmodes5.py imports damping5.py,
solv5.py imports cform5.py and damping5.py, tface5.py imports cform5.py, gaugepot5.py, semiclass5.py and damping5.py,
lin5.py imports damping5.py and gaugepot5.py, sbar5.py imports damping5.py, strap5.py imports damping5.py, gmodes5.py
imports damping5.py, zstates5.py imports damping5.py, genstates5.py imports damping5.py and zstates5.py, and the others
import nothing from the tree. The board's shared record is not edited here.