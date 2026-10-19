# n1star: N1* and the counterpart theorem (item 522)

The session commissioned at item 522 (`../../paper/INSTRUCTIONS-N1STAR-AND-HL-RESPONSE.md`). Start with
`N1STAR-STATUS.md`: N1* is **not proved**; what is proved, what is reduced and what is open are listed there, with
the audit of every place Touati's proof uses smallness.

- `N1STAR-LOG.md`: M's words to this session, verbatim, and the session's decisions (D1-D4).
- `N1STAR-STATUS.md`: the result.
- `ansatz5.py`: route W step 1, the geometric-optics ansatz on 5D Vaidya with the phase v (A1-A5).
  `python3 ansatz5.py --selftest` (5/5, about 3 minutes), `--mutants` (5/5).
- `foliation5.py`: route W steps 3 and 5, the null foliation, Touati's commutator lemma as an identity, the slices and
  the domain (B1-B4). `python3 foliation5.py --selftest` (4/4, seconds), `--mutants` (4/4).

Both are stdlib plus sympy, and import nothing from the tree. The board's shared record is not edited here.
