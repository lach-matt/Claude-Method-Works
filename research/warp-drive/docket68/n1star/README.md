# n1star: N1* and the counterpart theorem (item 522)

The session commissioned at item 522 (`../../paper/INSTRUCTIONS-N1STAR-AND-HL-RESPONSE.md`). Start with
`N1STAR-PROOF.md`: N1* is not yet claimed as PROVED: no citation is outstanding, and the last repairs await one
independent check; what is proved, what is verified and what is left are listed there.

- `N1STAR-LOG.md`: M's words to this session, verbatim, and the session's decisions (D1-D17).
- `N1STAR-STATUS.md`: the first assessment (D6), kept as the record of the audit of Touati's smallness.
- `N1STAR-PROOF.md`: the proof as it stands: Theorem E (evolution), Theorem A (the approximant) and Theorem D (the
  data, solved outward in r), checked by independent verifiers (D12, D15, D16); every standard theorem it invokes READ
  at source (its section 7, D17). Start here.
- `ansatz5.py`: route W step 1, the geometric-optics ansatz on 5D Vaidya with the phase v (A1-A5).
  `python3 ansatz5.py --selftest` (5/5, about 3 minutes), `--mutants` (5/5).
- `foliation5.py`: route W steps 3 and 5, the null foliation, Touati's commutator lemma as an identity, the slices and
  the domain (B1-B4). `python3 foliation5.py --selftest` (4/4, seconds), `--mutants` (5/5).
- `ks5.py`: the coordinates of the proof, 5D Vaidya in ingoing Kerr-Schild form on R x R^4, regular at the T^2 axes;
  Touati's commutator lemma there as an exact identity (K1-K5). `python3 ks5.py --selftest` (5/5, about 2 minutes),
  `--mutants` (4/4, about 8 minutes).
- `lead5.py`: Theorem A's stage 0, the leading equation (E2) for the record's waves in the proof's gauge (L1-L5).
  `python3 lead5.py --selftest` (5/5, seconds), `--mutants` (4/4).
- `data5.py`: Theorem D, the facts about the approximant's slice data that the outward evolution of the constraints
  uses (S0-S6). `python3 data5.py --selftest` (7/7, about 14 minutes), `--mutants` (six mutants), `--show` (the
  principal part).

All five are stdlib plus sympy, and import nothing from the tree. The board's shared record is not edited here.
