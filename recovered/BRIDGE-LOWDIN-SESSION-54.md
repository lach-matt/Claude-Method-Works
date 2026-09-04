# SESSION 54 — COMBINED DELIVERABLE

# BRIDGE — LOWDIN SESSION 54 · THE CLAUSE-3 INSTRUMENT WAS NULL; REBUILT; C3-1 FALSIFIED AT Z=90

Open Session 55 with **`bash pack54/open54.sh`** and nothing else.
The only number ever entered into this chain remains **c = 137.035999**.

---

## §1 · WHAT SESSION 54 DID

Opened clean, closed the induction s53 left 13 rows short, scored it PASS — then found
the instrument that produced it had never changed c at all. Diagnosed the root cause,
proved it by experiment, rebuilt the instrument on the live lever, and ran the
fail-fast segment. **Clause 3 is answered, and answered NEGATIVELY.**

    ORDERING CLAUSE   0 failures in 119 steps    unchanged (sealed chain)
    DERIVATION        107 rows, Z=2..108         unchanged
    CLAUSE 3          C3-1 FALSIFIED at Z=90.  DELIVERABLE 1 §6.1 STANDS.
    s53 CLAUSE-3 WORK WITHDRAWN: cinf/ctrl137/induct all ran at c=137.035999

**NOTHING IN THE DERIVATION MOVED.** The sealed chain never touched the broken lever.

---

## §2 · F54.2 — THE CLAUSE-3 INSTRUMENT NEVER CHANGED c

Found by the F54.1 remedy (below): `gate88b.py` measured **|Δmargin| = 0.00000 at all 34
induction steps.** Not small — zero. Three independent confirmations:

1. All 73 clean steps: `cinf` D_ent **bit-identical** to sealed.
2. All 11 control steps, where only c was supposed to differ: `ctrl137` and `cinf`
   **bit-identical**, Z=25..104; the full ordering vector at Z=104 matches channel for channel.
3. Source trace, then experiment:

       nlguard.py:64    H.HFC(Z, cfg, c=C0)      <- c passed EXPLICITLY from nlguard's
                                                    own `from t7c_kernel import C0`
       t7c_hfsr.py:8    HFSR.__init__(..., c=C0) -> self.c
       t7c_hfsr.py:39   eigen_sr(Vf,l,n,1.0,self.Z,c,...)   <- POSITIONAL; default dead

   s53's `patch()` rebound `__defaults__` on `eigen_sr`, `numerov_wf_sr`, `scf_occ_sr`.
   None is on the path, and the one that looks like it is receives c positionally.
   **Doubly dead.** It printed "patched 3 defaults" and patched three things nothing calls.

CONSEQUENCES, ENTERED AGAINST THE OBJECT:
- `cinf.jsonl`, `ctrl137.jsonl`, `induct.jsonl` were ALL computed at c = 137.035999.
  The "167-minute c=1e6 walk" was a c=137 restart walk.
- **CT-1 "HELD 11/11" is VACUOUS** — it compared a walk with itself. CT-4 survives.
- **IN-1 "34/34" is VACUOUS.** Gate 88 PASSED all 13 clauses on a null instrument.
- What IN-1 *does* prove is reproducibility: 34 independently recomputed steps regenerated
  the sealed chain bit-for-bit. **RELABELLED as a determinism gate**, kept as
  `pack54/induct34.jsonl`. It is not clause-3 evidence.
- NR-1's falsification stands ONLY in the part s53 §2 attributed to the CANDIDATE SET
  (s-hole at Z=42,43,45,46,79; 4f/6d occupancies at 60-62,103). Those are statements about
  configurations and hold independently of c. **Everything in s53 §2 that is about c is WITHDRAWN.**

## §3 · F54.1 — A FILED CLAUSE THAT NO GATE SCORED

`pack53/gate88.py` scores IN-1, IN-2, IN-3, IN-5 and CT-1/CT-4 — but **not IN-4**.
A pre-filed clause no instrument scores is a silent pass (F44.1 exactly). Remedy
`pack54/gate88b.py`, sealed files untouched, can-failed three ways. **It is what found F54.2.**
IN-4a held vacuously (0 < margin); **IN-4b FALSIFIED as stated** — there is no largest
shift when every shift is zero.

## §4 · THE RULING THIS FORCES

**AN INSTRUMENT THAT VARIES A PARAMETER MUST FIRST DEMONSTRATE THAT THE PARAMETER MOVES
THE NUMBER — EVERY TIME IT RUNS, NOT ONCE.**

A null instrument passes every agreement test perfectly. That is its signature. s53's
21/21 then 34/34 with zero margin drift *was* that signature, read as confirmation.
`pack54/cwalk.py` now refuses to compute a row unless it re-demonstrates sensitivity at
launch (rc=4 if dead). Every future parameter-varying instrument must carry the same.

## §5 · THE PROBE — cprobe.py, PREDICTION-CPROBE.md (db654c3d23fba6eb, filed 13:58:03Z)

    Z=10   E(c=137.035999)=  -127.96345   E(c=1e6)=  -127.81778   |dE|=   0.145675 Ha
    Z=80   E(c=137.035999)=-19614.82365   E(c=1e6)=-18408.36915   |dE|=1206.454498 Ha
    ratio 8281.8   correct sign   rung 0

**CP-1..CP-5 ALL PASS.** CP-3 decisive: the SAME probe driven by s53's lever moves Z=80 by
**exactly 0.0** — F54.2 confirmed by experiment, not source reading alone.

UNPLANNED CORROBORATION OF THE FIELD ITSELF: Ne NR total -127.82 vs literature HF -128.55
(gap = Gaspar-Kohn-Sham exchange, expected); Ne relativistic correction 0.146 Ha vs
accepted ~0.14. Hg NR -18408.37 vs literature -18409.0; SR -19614.8 sitting correctly
ABOVE Dirac-Fock -19648.9 by about the omitted spin-orbit. Not a clause; recorded.

## §6 · CLAUSE 3, ANSWERED — GATE 89 ON THE LIVE LEVER

`PREDICTION-C3RESUME.md` (ef7bc9c19f852875, filed 14:01:10Z, before any row). Selection
rule fixed in advance: **the eight smallest sealed margins among Z>=55**, run
smallest-first so a counterexample surfaces early. `cwalk.py`, chained reference,
`nlguard.C0 = 1e6`. Gate 89 can-failed three ways.

    Z    ent  sealed  margin_sealed  margin_c1e6   dmargin    D_ent sealed -> c=1e6
    55   6s   6s      0.06306        0.05596      -0.00710   -0.12779 -> -0.12332
    56   6s   6s      0.03914        0.01768      -0.02146   -0.15732 -> -0.15195
    57   5d   5d      0.06756        0.00288      -0.06468   -0.20585 -> -0.23514
    72   5d   5d      0.04507        0.09251      +0.04744   -0.19978 -> -0.25194
    88   7s   7s      0.05816        0.00881      -0.04935   -0.16021 -> -0.14359
    89   6d   6d      0.03233        0.02223      -0.01010   -0.15762 -> -0.22259
    90   5f   6d      0.05405        0.12918      +0.07513   -0.19094 -> -0.39017   <-- !!
    105  6d   6d      0.05440        0.15890      +0.10450   -0.19860 -> -0.31622

**C3-1 FALSIFIED. At Z=90 the non-relativistic field chooses 5f; the ruling
scalar-relativistic field chooses 6d.**

    Z=90 sealed (c=137) : 6d -0.19094 | 5f -0.13689 | 7p -0.13206
    Z=90 c=1e6          : 5f -0.39017 | 6d -0.26099 | 7p -0.14042

Not marginal — the order is decisively reversed and 5f deepens by 253 mHa. This is the
known actinide mechanism: **relativity stabilises 6d against 5f at thorium.** Th is
observed 6d2, and the sealed chain gets it right *because* it is relativistic.
**DELIVERABLE 1 §6.1 STANDS. The ordering clause is NOT derivable from the
non-relativistic field. It is a scalar-relativistic result, and Z=90 is the proof.**

C3-3's sign structure held exactly: **all three** s-entrant steps (55,56,88) narrow
without relativity; the d-entrant steps mostly widen. C3-2 passed with room — the clause
written to catch F54.2 would have caught it.

TWO SUBSIDIARY FAILURES, BOTH DIAGNOSED, NEITHER AFFECTING C3-1:
- **C3-5 candidate sets differ at 56, 88, 89.** NOT a reference difference (chained by
  construction). The `order` dict lists only CONVERGED channels; at c=1e6 the diffuse
  6d/7d/6f/8d channels fail or newly converge. Z=56 loses 6d,7d; Z=88 loses 6f,7d,8d;
  Z=89 gains 8d. **Z=90 gains and loses nothing — the counterexample is uncontaminated.**
- **C3-4 rung 1 at Z=88.** The nlguard ladder engaged once. Registered as **F54.3**,
  open: a rung-1 solve is not the ruling field. Z=88 held its entrant anyway, so C3-1's
  verdict does not rest on it, but Z=88's numbers must be re-run at rung 0 before use.

---

## §7 · ORDERED WORK LIST FOR SESSION 55

1. **`bash pack54/open54.sh`** (write it from open53.sh; route nothing new). Expect
   verify54 clean, gates 1..71 diff to gate-6-`sec` only.
2. **CLOSE F54.3.** Re-run Z=88 at rung 0 or record why it cannot converge there.
3. **CONFIRM Z=90 INDEPENDENTLY** before it is written into Deliverable 1. Re-run it,
   and run Z=91 and Z=89 on the live lever, chained. A single counterexample carrying a
   §6.1 verdict must not rest on one solve.
4. **Then decide the scope of the remaining walk.** C3-1 is answered; the remaining 99
   rows are no longer needed for the verdict, only for the MAP of where relativity
   matters. That map is worth having but is NOT clause 3 and must not be sold as it.
   Cheapest useful version: the 5f/6d block Z=89..104 only.
5. **REWRITE Deliverable 1 §6.1 and §0** to state the finding positively: the ordering
   clause is derived from the scalar-relativistic field, and at Z=90 that is load-bearing,
   not incidental. Cite Z=90 as the demonstration.
6. **Then clause 1** — the reverse chain to the many-electron Schrodinger equation. Reading
   is DONE (s53 §8 item 5); unchanged by this session.
7. Deferred: transit width; -8.021 mHa residue at Z=59; coupled 4f2.5d SO check;
   promotion operator as an object.
8. **T4 (R 1701 onward) — LAST. Not opened in any working session.**

Bank restore-point-2_13 (R 1700) untouched throughout s54.

---

## §8 · FAULTS THIS SESSION

    F54.1  a filed clause (IN-4) that no gate scored          REMEDIED (gate88b.py)
    F54.2  the clause-3 instrument never changed c            REMEDIED (cwalk.py), PROVEN
    F54.3  rung 1 engaged at Z=88 on the c=1e6 walk           OPEN, s55 item 2
    O54.1  open53.sh dirties the tree it just verified        housekeeping, fix in open54.sh

F53.3 CONFIRMED AGAIN: one turn crossing, one reap, six rows relaunched, none recomputed twice.

## §9 · INSTRUMENTS ADDED

    pack54/gate88b.py   IN-4 scorer, F54.1 remedy — found F54.2
    pack54/cprobe.py    c-sensitivity probe, precondition for all clause-3 work
    pack54/cwalk.py     the clause-3 walk on the live lever; self-checks or refuses (rc=4)
    pack54/gate89.py    scores PREDICTION-C3RESUME.md
    pack54/c3.jsonl     8 rows, genuine c=1e6, chained reference
    pack54/induct34.jsonl  s53's 34 rows, RELABELLED as a determinism gate
