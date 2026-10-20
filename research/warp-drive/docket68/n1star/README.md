# n1star: N1* and the counterpart theorem (item 522)

The session commissioned at item 522 (`../../paper/INSTRUCTIONS-N1STAR-AND-HL-RESPONSE.md`). Start with
`N1STAR-PROOF.md`: **N1* is PROVED** (D21); what is proved, how it was verified and what no verifier has read
after the last edit are listed there. The response paper is `../../paper/RESPONSE-HL-5D.md`, with its check
`../../paper/response5.py` (D22-D23).

- `N1STAR-LOG.md`: M's words to this session, verbatim, and the session's decisions (D1-D40).
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
  perturbation types, the potentials, the l = 2 ringdown against the published values, the settling times at the
  study's seeds (T1-T4); no growing mode for l = 2..10 and the late-time tail t^-7 against Cardoso, Yoshida, Dias and
  Lemos (T5-T6, section 10.3). `python3 settle5.py --selftest` (6/6, about a minute), `--mutants` (6/6).
- `growth5.py`: the go/no-go at the wavelength 10 l5 (ROUTES-OPEN.md section 2): the solver of
  `../lemmas/hf_mirror5.py` run on hf_core5's domain at lam = 10 l5 for mu0 = 100 and 1000 l5^2, the growth factor
  exp int K dv of the computed solution recorded at every step (two measures, fifteen maxima), the breakdown of the
  scheme's premise (a second zero of the expansion, the core boundary untrapped) and a finite-difference linear
  amplification (G0-G4, section 10.2). `python3 growth5.py --selftest` reads `data/growth5_runs.json`;
  `--run L lam Ny Nx [delta]` regenerates one run (minutes to an hour), `--merge`, `--report`.
- `routes5.py`: the two computed facts behind ROUTES-OPEN.md's route for the mass at past null infinity:
  five-dimensional Vaidya's R_vv, and Tanabe, Tanahashi and Shiromizu's Bondi mass law as the class's P7
  density (Q1-Q2). `python3 routes5.py --selftest` (2/2), `--mutants` (2/2).
- `ROUTES-OPEN.md`: one proposed method for each of the three open items, with the literature READ (D36).
  Nothing in it is proved.
- `bondi5.py`: Theorem M, the Bondi mass at past null infinity (section 11): the five-dimensional Bondi hierarchy in
  the class with every coefficient from s^1 general (the orders below the waves' vanish; the mass law from R_vv at
  order r^-3), the chart from the wave-gauge expansion, the Hawking mass of the Bondi spheres, the numerics'
  coefficient (B1-B4). `python3 bondi5.py --selftest` (4/4, about ten minutes, B2 the slow one), `--mutants`
  (5/5), `--verbose` lists every sub-check.
- `data5.py`: Theorem D, the facts about the approximant's slice data that the outward evolution of the constraints
  uses (S0-S6). `python3 data5.py --selftest` (7/7, about 14 minutes), `--mutants` (6/6, about 80
  minutes), `--show` (the principal part).

All twelve are stdlib plus sympy (foliation5.py also uses z3; settle5.py numpy and scipy; bondi5.py and growth5.py
numpy, growth5.py importing the solver beside it), and the eleven others import
nothing from the tree. The board's shared record is not edited here.