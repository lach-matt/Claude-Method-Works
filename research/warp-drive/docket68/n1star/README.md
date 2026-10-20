# n1star: N1* and the counterpart theorem (item 522)

The session commissioned at item 522 (`../../paper/INSTRUCTIONS-N1STAR-AND-HL-RESPONSE.md`). Start with
`N1STAR-PROOF.md`: **N1* is PROVED** (D21); what is proved, how it was verified and what no verifier has read
after the last edit are listed there. The response paper is `../../paper/RESPONSE-HL-5D.md`, with its check
`../../paper/response5.py` (D22-D23).

- `N1STAR-LOG.md`: M's words to this session, verbatim, and the session's decisions (D1-D36).
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
  study's seeds (T1-T4). `python3 settle5.py --selftest` (4/4, under a minute), `--mutants` (4/4).
- `routes5.py`: the two computed facts behind ROUTES-OPEN.md's route for the mass at past null infinity:
  five-dimensional Vaidya's R_vv, and Tanabe, Tanahashi and Shiromizu's Bondi mass law as the class's P7
  density (Q1-Q2). `python3 routes5.py --selftest` (2/2), `--mutants` (2/2).
- `ROUTES-OPEN.md`: one proposed method for each of the three open items, with the literature READ (D36).
  Nothing in it is proved.
- `data5.py`: Theorem D, the facts about the approximant's slice data that the outward evolution of the constraints
  uses (S0-S6). `python3 data5.py --selftest` (7/7, about 14 minutes), `--mutants` (6/6, about 80
  minutes), `--show` (the principal part).

All ten are stdlib plus sympy (foliation5.py also uses z3; settle5.py numpy and scipy), and import nothing from the
tree. The board's shared record is not edited here.