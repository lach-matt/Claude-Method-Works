#!/usr/bin/env python3
"""
DOCKET 66 / B-combine66 -- M's standing instruction, run on DOCKET 66's three hypotheses: "some of the hypothesies
lined up ... may turn out, after initial testing, to work better in combination" (docket68/CHARTER.md, verbatim; the
DOCKET 66 charter's order of work, step 3: "Combinations screened with D68's hypotheses, where one member removes an
obstruction another leaves").

WHAT IT SCREENS
  The 7 non-empty combinations of H-DEFECT-SEAT, H-THROAT-BITS and H-QET-EXOTIC, each hypothesis carried in EVERY
  reading its A-report graded:
      H-DEFECT-SEAT   DSTR (static straight string), DWALL (thin wall), DGMON (global monopole), DMON (gauge monopole,
                      exterior), DTEX (texture), DTHR (a defect as the THROAT's support: string-supported wormholes)
      H-THROAT-BITS   TBHOLO (R-HOLO), TBTSH (R-THINSHELL), TBTEL (R-TELEPORT), TBISL (R-ISLAND), TBITB (R-ITB: D68's
                      ITB located at the throat -- always screened WITH the D68 literal ITB, A2: "adds the location only")
      H-QET-EXOTIC    QET (R-QET, M's sentence read operationally), QLIT (R-LIT, the question's parenthetical read as
                      arrival alone; D66-repro residual: wave 1's words here, 'M's sentence alone', kept as history --
                      V66-1 #7)
  = 125 reading-combinations, each with every context of D68's members that BEAR (the task's list): H-IT in none / ITB /
  ITE / ITJ; H-INFO-SHAPE absent / present; H-SETTLE W2 x H-FRAME F1 absent / present; R-QUANTUM (RQ) absent / present
  (A3: QET's only OPEN branch on O-HOLD is the board's R-QUANTUM branch); the S5 seat route is the board's OPEN pathway
  N_S5, present in every variant, and H-SEAT-ROUTES is computed as a named reading.  Cells: 1 ly, N = 7 (all variants)
  and 1 AU, N = 7 (every variant with W2 x F1; the only literal B-EPSWIN reads).

HOW (import, never copy)
  docket68/combine.py's engine is IMPORTED and run unchanged: its Screen (tracked constraints, every minimal support,
  accounts, OPEN status), its board (_board), definitions (_defs) and commitments (_commitments), its views
  (account_view, attributed, counts, signature) and its drift rules (parse_report_class, z3_class).  DOCKET 66's
  commitments enter as TRACKED CONSTRAINTS WITH GROUNDS (board66, commitments66), exactly as combine's own do.
  Encoding choice E-EXTEND: combine's vocabulary (LIT_NAMES, PHYS, NAMED, OPEN_NAMED) is extended IN THIS PROCESS ONLY
  (no file is edited) so the engine sees DOCKET 66's literals; four of combine's tracked items are WIDENED (B-HELD,
  B-SIGLOOP, DEF-SEAT, DEF-TOPO), each built from combine's OWN term (read out of combine's expression, never retyped)
  OR'd with DOCKET 66's route, the original's indicator dropped from the assumptions.  Guard: with every D66 literal
  absent the extended screen gives combine's exact signature (conservative-extension guard, below).

GUARDS (PROOF-ASSISTANT.md: vacuity and encoding drift; the screen refuses to report if any fails)
  * vacuity: board SAT; every D66 reading alone SAT except R-LIT (its FALSE-IF, a CONTENT result); D66's named premises
    jointly SAT; every consistent variant SAT WITH THE OPEN PATHWAYS HELD FALSE (the engine computes supports with them
    false, so a variant consistent only through an OPEN pathway would report vacuous removals) -- with a planted
    control that trips it;
  * conservative extension: D68 variants screened by combine under its own vocabulary and by the extended screen give
    identical signatures;
  * encoding drift: z3's per-obstruction class against the D66 A-reports' own grade text (scratchpad JSON, parsed by
    combine.parse_report_class on fragments anchored VERBATIM in the JSON) and against defects.grades() (A1's own z3);
    every disagreement listed with its reason; five mutated encodings must each be caught;
  * pathway ties: each D66 OPEN pathway opens only where encoded -- controls.
  STRUCTURAL items (cannot fail by construction) are printed and NOT counted.

D66-FIX (2026-10-04; the three wave-1 verifier reports, every problem resolved or answered -- B-combine66.md section 0):
  * M's ruling M-S1A-P3 ('a singular throat is not disqualified'; 'the throat-creation classes stay OPEN') is APPLIED
    to every D66 geometric throat (DEF-TOPO/66, N_WNCC owners DTHR, TBHOLO, TBTSH, TBTEL); wave 1's E-SINGOK (A2's two
    singular readings only, the board reading 'for M') is kept as the reading 'singok-a2' and refused by the drift guard.
  * N_GJWAMB (GJW's one-space version, 'stated, not computed') is replaced by N_GJWPAY: what Maldacena-Milekhin-Popov
    1807.04726 (READ) shows and does not show (throatbits.mmp_scales); R-TELEPORT's O-HOLD on GJW alone is LEFT-IF.
  * N_WALLLOOP is retired: the M4-M4 wall's global time function is computed (defects.vis_time_function, CGS p.15).
  * QET's hold route is N_QETHAD only; N_XI and N_QEIC stay the board's, tied to RQ (wave 1's gating kept as the
    reading 'qet-board-paths').
  * The A-reports' grades are asked of the instruments at run time (report_grades), not of stored scratchpad JSON.

D66-RULINGS (R-apply, 2026-10-04; docket68/M-RULINGS-2026-10-03.md items 27 and 28, M's words verbatim):
  * Item 28, M: "Re-grade D68 (Recommended)" -- "O-MAKE-TOPO reads OPEN via N_WNCC in D68's board-context variants as in
    D66's; history kept".  docket68/combine.py now carries the ruling on its own board (DEF-TOPO: THROAT & N_WNCC), so
    the reading 'singok-board' -- which first showed it here -- IS combine's encoding and moves nothing; D68 wave 2's
    encoding is combine's history mutation 'd68w2-topo', run here as a reading: it moves back exactly the rows
    'singok-board' moved at D66-fix (174 single-reading/context variants, 20 of them context-only), each O-MAKE-TOPO
    OPEN via N_WNCC -> LEFT.  'singok-a2' (wave 1's E-SINGOK) sat on D68 wave 2's board, so it is now built on
    combine's 'd68w2-topo' DEF-TOPO and stays a mutation the drift guard refuses.  N_WNCC is now the board's pathway as
    well as the D66 throats': its tie control is a variant with NO geometric throat (ITB with N_QTOPO), not a D66
    reading without one (every variant without ITB's premise has a throat, combine's B-THROAT).
  * Item 27, M: "Any crossing" -- spec.py's TURN is H-TURN-CROSSING (A1's grades, defects.py); nothing here encodes TURN
    (it lies outside the screen's atoms), so no screen row moves.

VERDICT WORDS (docket68/B-combine.md section 1): REMOVED, REMOVED-IF, NOT-BOUND-IF (a theorem that does not bind; never
a removal), OPEN, SILENT, LEFT.  Added here, and only as a field beside a removal: "defeasible via X" -- an OPEN pathway
X under which the removal's every support can fail (a loop reintroduced, a seat pathology made possible).  The seat
condition M-S1A-P3 (i) (no closed causal curve and no Borde pathology AT THE SEAT; a singular throat not disqualified)
is graded per variant: SATISFIED, SATISFIED-IF {premises}, OPEN (defeasible via), VIOLATED.

M's hypotheses are carried as hypotheses, never as results.  Nothing here is seated.  Writes nothing outside docket66/
except output paths the caller names.  Never edits combine.py, ledger.py, index3.py, specthm.py, LEDGER.md or paper/.

    python3 combine66.py --selftest       guards, grounds, screen, drift, controls -- exits 1 on any failure
    python3 combine66.py                  the report
    python3 combine66.py --json PATH      the report and every variant as JSON
    python3 combine66.py --conservative-full   the conservative-extension guard over all 8,191 D68 variants
"""
import contextlib
import io
import itertools
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.abspath(os.path.join(HERE, ".."))
D68 = os.path.join(WD, "docket68")
for _p in (HERE, D68, WD):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import z3                                    # noqa: E402
import combine as C                          # noqa: E402  -- docket68's engine, imported, run unchanged

_OWN = {}


def own(name):
    """Import an owner once, its import-time prints swallowed (several board owners print)."""
    if name not in _OWN:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            _OWN[name] = __import__(name)
    return _OWN[name]


# =====================================================================================================================
# VOCABULARY (DOCKET 66)
# =====================================================================================================================
D66_HYPS = ["H-DEFECT-SEAT", "H-THROAT-BITS", "H-QET-EXOTIC"]
D66_READINGS = {
    "H-DEFECT-SEAT": {
        "DSTR": "static, straight, positive-tension string at the seat (A1 row 1; H-STATIC-STRING)",
        "DWALL": "thin vacuum domain wall at the seat, VIS with Lambda = 0 both sides (A1 row 2; H-THIN, H-VIS-MINKOWSKI)",
        "DGMON": "global monopole at the seat (A1 row 3)",
        "DMON": "gauge monopole at the seat, exterior (A1 row 4)",
        "DTEX": "texture at the seat (A1 row 5): an event, not a place (DURRER Table 1); unstable (Derrick)",
        "DTHR": "a defect as the THROAT's support: string-supported traversable wormholes (A1 row 6: Visser polyhedral, "
                "GV ring, FGM quantum)",
    },
    "H-THROAT-BITS": {
        "TBHOLO": "R-HOLO: the throat's geometry holds its information at A/(4 l_P^2 ln2) (A2)",
        "TBTSH": "R-THINSHELL: the singular throat is a Poisson-Visser distributional shell (A2)",
        "TBTEL": "R-TELEPORT: compressed to binary information then pushed = traversable-wormhole teleportation, "
                 "GJW/MSY (A2)",
        "TBISL": "R-ISLAND: the island formula's area term (A2)",
        "TBITB": "R-ITB: D68's ITB located at the throat -- 'adds the location only' (A2); screened with ITB",
    },
    "H-QET-EXOTIC": {
        "QET": "R-QET: the bit arrives, a local operation conditioned on it in an entangled ground state leaves a local "
               "negative-energy region (A3; TRUE-IF {H-GROUND, H-CORR, H-ACT, H-INSTANT})",
        "QLIT": "R-LIT: the question's parenthetical read as arrival alone ('information arriving ... creates'), no "
                "conditioned operation, no prior correlation (A3; FALSE-IF {H-MINIMAL|H-1+1, linear QM}).  M's sentence "
                "read operationally is R-QET; wave 1 first labelled R-LIT 'M's sentence alone' (V66-1 #7)",
    },
}
D66_LITS = [k for h in D66_HYPS for k in D66_READINGS[h]]
D66_OF = {k: h for h in D66_HYPS for k in D66_READINGS[h]}
DS4 = ("DSTR", "DWALL", "DGMON", "DMON")              # the classes A1 grades 'OPEN via N_S5 | N_DEFB'
TB_ALL = ("TBHOLO", "TBTSH", "TBTEL", "TBISL", "TBITB")
TB_SING = ("TBHOLO", "TBTSH")                         # A2's readings with a singular geometric throat
D66_THROATS = ("DTHR", "TBHOLO", "TBTSH", "TBTEL")     # every D66 reading that commits a geometric throat (C-* => THROAT)
D66_PHYS = ["CTCW", "SEATLOOP", "DEFBSUP", "ARRNEG"]

#: named premises (assumed only inside a support; every support listed) -- each is a named hypothesis of an A-report
D66_NAMED = {
    "N_MBAL": "H-MASS-BALANCE (A1, FKZ 2305.03887 pp.5,17-18 READ): the two mouths of a traversable string-supported "
              "throat in one space sit at balanced gravitational potential (or the throat closes before T ~ R L c/(G M)); "
              "without it the throat becomes a time machine and the seat mouth lies on the loop",
    "N_SEATOFF": "H-SEAT-OFF-THROAT (A2): the seat lies off the throat, so the throat's own pathology (a singularity, "
                 "Tipler/Borde) is not AT the seat -- M's clarification places them apart ('Singular occurs in the "
                 "throat ... and then push to the seat'), carried as A2 carries it, a named premise",
    "N_FLATQFT": "H-FLAT-QFT (A3): QET is a protocol of Minkowski QFT whose step at the seat follows the bit, so it "
                 "introduces no closed causal curve and no Borde pathology at the seat",
    "N_SEATPERSIST": "H-SEAT-PERSISTS (A1): a seat is a place that persists over the arrival (so a spacetime EVENT is not "
                     "a seat)",
}
#: OPEN pathways (undecided by the sources; held FALSE whenever supports and accounts are computed).  All OPENING (make a
#: removal possible); wave 1's one DEFEATING pathway, N_WALLLOOP, is retired (RETIRED below).
D66_OPEN = {
    "N_DEFB": "OPENING, O-SEAT (A1, defects.HYPOTHESES): a baryon-number-violating defect core shown to SUPPLY the "
              "payload's baryons at the seat.  READ (HK pp.63-65): for GUT string cores and gauge monopoles the "
              "direction is WASH-OUT (eq.(4.33)); emission needs CP-violating couplings and a departure from thermal "
              "equilibrium (p.65), so a supply only IF {CP violation, departure from equilibrium}; feedstock leptons, "
              "rate computed nowhere; for walls and global monopoles not READ (OPEN as unchecked).  Wave 1 first said "
              "'direction and rate computed nowhere' (V66-0 #2)",
    "N_NEGT": "OPENING, O-HOLD (A1): a negative-tension string (or loop) shown to exist -- no mechanism known (Visser "
              "1989 p.5, READ); outside H-CANONICAL (canonical fields satisfy the NEC pointwise, defects.canonical_nec)",
    "N_GJWPAY": "OPENING, O-HOLD (A2): N_GJW-PAYLOAD -- a one-space traversable throat that admits the payload, outside "
                "Maldacena-Milekhin-Popov's family with the SM's fields.  MMP 1807.04726 (READ) realises GJW's one-space "
                "version, REMOVED-IF {H-GJW-COUNTERPART, H-MMP, H-SM-FIELDS} at sub-electroweak scale; its binding "
                "energy equals the payload's rest energy only below l_P, and at r_fit it needs ~1e14 massless charged "
                "species (throatbits.mmp_scales).  MQ 1804.00491's held throat is in nearly-AdS2 (E-ADS).  Wave 1 carried "
                "N_GJWAMB, 'stated, not computed' (V66-1 #2); GJW alone gives an opening, not a hold (V66-0 #1)",
    "N_PINCH": "OPENING, O-HOLD (A2's LEFT-IF outside): the singular throat is outside {H-SINGULAR-IS-THINSHELL, "
               "H-PV-STATIC} -- a curvature-singular, geodesically incomplete pinch (H-SINGULAR-IS-PINCH: 'not modelled', "
               "A2) or a dynamic shell; unchecked, so OPEN",
    "N_QETHAD": "OPENING, O-HOLD (A3's LEFT-IF outside): QET states outside the class the QEI duration bound covers "
                "(H-QET-HADAMARD unchecked -- a short check by the displaced-vacuum argument, not run: V66-0 #7).  QET's "
                "ONLY pathway: N_XI and N_QEIC are the board's R-QUANTUM pathways (tied to RQ), with or without QET",
    "N_WNCC": "OPENING, O-MAKE-TOPO (A1, A2): specthm's throat class W-create-ncc shown nonempty -- a creation whose "
              "pathology (Tipler/Borde, Geroch) is placed at the throat, which M has ruled not disqualifying (ledger "
              "M-S1A-P3: 'a singular throat is not disqualified', 'the throat-creation classes stay OPEN').  Applied to "
              "EVERY D66 geometric throat (DTHR, TBHOLO, TBTSH, TBTEL); not shown realisable (specthm: OPEN, asked at run "
              "time).  Wave 1 credited it to TBHOLO/TBTSH only and called the board reading 'for M' (V66-1 #1).  "
              "D66-RULINGS (M-RULINGS item 28, 'Re-grade D68 (Recommended)'): docket68/combine.py now carries it for "
              "EVERY geometric throat (THROAT), D68's included -- the reading 'singok-board' became the board's encoding; "
              "D68 wave 2's is combine's history mutation 'd68w2-topo'",
}
#: wave 1's pathways no longer carried, with why (history kept)
RETIRED = {
    "N_WALLLOOP": "wave 1: 'the thin wall's global (VIS) causal structure ... not computed'.  D66-fix: computed -- "
                  "Minkowski T is a global time function of the M4-M4 wall (defects.vis_time_function; CGS p.15, Fig.4 "
                  "READ), so under H-VIS-MINKOWSKI no loop and no seat pathology; V66-1 #3",
    "N_GJWAMB": "wave 1: GJW's one-space version 'stated, not computed'.  D66-fix: replaced by N_GJWPAY, what MMP "
                "1807.04726 shows and does not show; V66-1 #2",
}
#: which D66 literal opens each D66 pathway (drift rule Z7; vacuity ties)
PATHWAY_OWNER = {"N_DEFB": set(DS4), "N_NEGT": {"DTHR"}, "N_GJWPAY": {"TBTEL"}, "N_PINCH": set(TB_SING),
                 "N_QETHAD": {"QET"}, "N_WNCC": set(D66_THROATS)}
#: literals with no screen content of their own (recorded, measured by the difference census, never asserted)
D66_INERT = {
    "TBISL": "R-ISLAND: replica wormholes are Euclidean saddles (2006.06872 p.37); no Lorentzian throat, no channel, no "
             "supply -- A2 grades SILENT or LEFT throughout; its only screen content is the seat closure (H-SEAT-OFF-THROAT)",
    "TBITB": "R-ITB: 'adds the location only' (A2); every non-binding is ITB's (the D68 literal, always present with it); "
             "its only screen content is the seat closure (H-SEAT-OFF-THROAT)",
}

#: the D68 members that bear (the task's list), as contexts
IT_CTX = [(), ("ITB",), ("ITE",), ("ITJ",)]
SHAPE_CTX = [(), ("SHAPE",)]
W2F1_CTX = [(), ("W2", "F1")]
RQ_CTX = [(), ("RQ",)]

_ORIG = {"LIT_NAMES": list(C.LIT_NAMES), "PHYS": list(C.PHYS), "NAMED": dict(C.NAMED), "OPEN_NAMED": dict(C.OPEN_NAMED),
         "LIT_OF": dict(C.LIT_OF)}
_STATE = {"extended": False}


def _set_vocab(extended):
    """E-EXTEND: in-place, so combine's methods (which read these module globals at call time) see the active vocabulary.
    Reversible; the conservative-extension guard runs combine under its original vocabulary first."""
    C.LIT_NAMES[:] = _ORIG["LIT_NAMES"] + (D66_LITS if extended else [])
    C.PHYS[:] = _ORIG["PHYS"] + (D66_PHYS if extended else [])
    for name, add in (("NAMED", D66_NAMED), ("OPEN_NAMED", D66_OPEN)):
        d = getattr(C, name)
        d.clear()
        d.update(_ORIG[name])
        if extended:
            d.update(add)
    C.LIT_OF.clear()
    C.LIT_OF.update(_ORIG["LIT_OF"])
    if extended:
        C.LIT_OF.update(D66_OF)
    _STATE["extended"] = extended


@contextlib.contextmanager
def vocabulary(extended):
    prev = _STATE["extended"]
    _set_vocab(extended)
    try:
        yield
    finally:
        _set_vocab(prev)


# =====================================================================================================================
# THE WIDENINGS: combine's own term, read out of combine's expression, OR'd with D66's route
# =====================================================================================================================
def _expr(items, name):
    for n, g, e in items:
        if n == name:
            return g, e
    raise KeyError(name)


def _c_mut(mutate):
    """combine's mutations for a D66 mutation set: 'singok-a2' (wave 1's E-SINGOK) was encoded on D68 wave 2's DEF-TOPO,
    so it reads combine's history encoding 'd68w2-topo' (D66-RULINGS; without it, combine's own N_WNCC disjunct would
    already cover DTHR and TBTEL and the mutation would change nothing)."""
    return tuple(mutate) + (("d68w2-topo",) if "singok-a2" in mutate and "d68w2-topo" not in mutate else ())


def widen_terms(A, win_open, mutate=()):
    """Returns {name: (combine's ground, combine's term, the widened expression)} for B-HELD, B-SIGLOOP, DEF-SEAT and
    DEF-TOPO.  Each term is read from combine's own expression (Implies(HELD, held): held; Implies(ante, Not(LOOPS)):
    ante; rm == rhs: rhs) and checked to be of that shape (GROUND, STRUCTURAL)."""
    I, An, Or, N = z3.Implies, z3.And, z3.Or, z3.Not
    board = C._board(A, win_open, mutate)
    defs = C._defs(A, _c_mut(mutate))
    out = {}
    g, e = _expr(board, "B-HELD")
    assert z3.is_implies(e) and e.arg(0).eq(A["HELD"]), "B-HELD is not Implies(HELD, held)"
    held = e.arg(1)
    negt = A["DTHR"] if "negt-asserted" in mutate else An(A["DTHR"], A["N_NEGT"])
    gjw = A["TBTEL"] if "gjw-ads" in mutate else An(A["TBTEL"], A["N_GJWPAY"])
    if "qet-holds" in mutate:
        qet = A["QET"]
    elif "qet-board-paths" in mutate:              # wave 1's encoding, kept as a reading on record (V66-0 #7)
        qet = An(A["QET"], Or(A["N_XI"], A["N_QEIC"], A["N_QETHAD"]))
    else:
        qet = An(A["QET"], A["N_QETHAD"])
    routes = [negt, gjw, An(Or(A["TBHOLO"], A["TBTSH"]), A["N_PINCH"]), qet]
    out["B-HELD"] = (g, held, I(A["HELD"], Or(held, *routes)))
    g, e = _expr(board, "B-SIGLOOP")
    assert z3.is_implies(e) and e.arg(1).eq(N(A["LOOPS"])), "B-SIGLOOP is not Implies(ante, Not(LOOPS))"
    ante = e.arg(0)
    wall = A["DWALL"] if "wall-loop" in mutate else z3.BoolVal(False)       # CONTROL only: a loop asserted at the wall
    out["B-SIGLOOP"] = (g, ante, I(An(ante, N(A["CTCW"]), N(wall)), N(A["LOOPS"])))
    g, e = _expr(defs, "DEF-SEAT")
    assert z3.is_eq(e) and e.arg(0).eq(A[C.RM["O-SEAT"]]), "DEF-SEAT is not rm == rhs"
    rhs = e.arg(1)
    out["DEF-SEAT"] = (g, rhs, e if "seat-routes" in mutate else (A[C.RM["O-SEAT"]] == Or(rhs, A["DEFBSUP"])))
    g, e = _expr(defs, "DEF-TOPO")
    assert z3.is_eq(e) and e.arg(0).eq(A[C.RM["O-MAKE-TOPO"]]), "DEF-TOPO is not rm == rhs"
    rhs = e.arg(1)
    if "singok-board" in mutate:                   # reading: every geometric throat, D68's included.  D66-RULINGS: this is
        who = A["THROAT"]                          # now combine's own DEF-TOPO (M-RULINGS item 28), so it moves nothing
    elif "singok-a2" in mutate:                    # wave 1's encoding (E-SINGOK), kept as a reading on record; it sat on D68
        who = Or(A["TBHOLO"], A["TBTSH"])          # wave 2's board, so combine's 'd68w2-topo' DEF-TOPO is read (_c_mut)
    else:                                          # M's ruling applied to every D66 geometric throat (V66-1 #1)
        who = Or(*[A[k] for k in D66_THROATS])
    out["DEF-TOPO"] = (g, rhs, A[C.RM["O-MAKE-TOPO"]] == Or(rhs, An(who, A["N_WNCC"])))
    return out


WIDEN_TEXT = {
    "B-HELD": "D66 widening: a geometric throat may also be held through an OPEN pathway of a D66 reading -- DTHR with "
              "N_NEGT (A1: FSW binds given H-CANONICAL; defects.grades 'OPEN via N_NEGT'); TBTEL with N_GJWPAY (A2: GJW "
              "alone gives an opening, not a hold; MQ's held throat is in nearly-AdS2; MMP's one-space throat does not "
              "admit the payload, throatbits.mmp_scales); TBHOLO/TBTSH with N_PINCH (A2: LEFT-IF "
              "{H-SINGULAR-IS-THINSHELL, H-PV-STATIC}; PV sigma_0 < 0 at every a_0 > 2M, throatbits.pv_static); QET "
              "with N_QETHAD only (A3: LEFT-IF {H_flat, H-PATH, H-MIN-SCALAR, H-QET-HADAMARD}; 2.081e-68 of the 1 m "
              "throat's deficit, geometry.r_quantum).  N_XI and N_QEIC stay the board's, tied to RQ (V66-0 #7; wave 1 "
              "gated them through QET too)",
    "B-SIGLOOP": "D66 widening: no signal loop closes unless also a wormhole time machine (CTCW, FKZ) supplies one.  "
                 "Wave 1 added the wall's uncomputed causal structure (DWALL with N_WALLLOOP); D66-fix computed it "
                 "(defects.vis_time_function: Minkowski T a global time function), so the wall supplies none",
    "DEF-SEAT": "D66 widening (H-SEAT-S5 only; under H-SEAT-ROUTES unchanged): O-SEAT is also removed by DEFBSUP, a "
                "baryon-number-violating defect core supplying the baryons (A1: 'OPEN via N_S5 | N_DEFB')",
    "DEF-TOPO": "D66 widening: O-MAKE-TOPO is also removed if specthm's W-create-ncc class is shown nonempty (N_WNCC) "
                "for any D66 geometric throat (DTHR, TBHOLO, TBTSH, TBTEL): M has ruled (ledger M-S1A-P3: 'a singular "
                "throat is not disqualified', 'the throat-creation classes stay OPEN'), a board ruling applied, not a "
                "question for M (V66-1 #1).  Reading 'singok-a2' is wave 1's encoding (TBHOLO / TBTSH only, on D68 wave "
                "2's DEF-TOPO); reading 'singok-board' extends it to D68's throats too -- D66-RULINGS: M ruled 'Re-grade "
                "D68 (Recommended)' (M-RULINGS item 28), so combine's own DEF-TOPO now carries THROAT & N_WNCC and "
                "'singok-board' moves nothing; D68 wave 2's encoding is the reading 'd68w2-topo' (combine's history "
                "mutation)",
}


def board66(A, mutate=()):
    """DOCKET 66's board holdings: (name, ground, expression)."""
    I, An, Or, N = z3.Implies, z3.And, z3.Or, z3.Not
    ds4 = Or(*[A[k] for k in DS4])
    tb = Or(*[A[k] for k in TB_ALL])
    fkz_who = A["THROAT"] if "fkz-generic" in mutate else A["DTHR"]
    wall = A["DWALL"] if "wall-loop" in mutate else z3.BoolVal(False)
    rows = [
        ("B66-DEFB", "A1 (defects.grades: 'O-SEAT, defect at the seat: OPEN via N_S5 | N_DEFB'): a defect core supplies "
                     "the payload's baryons only through N_DEFB (HK pp.63-65 READ: B violation at GUT string / monopole "
                     "cores, whose READ direction is wash-out, eq.(4.33); a supply only IF {CP violation, departure "
                     "from equilibrium}, p.65; rate computed nowhere).  Classes: string, wall, global and gauge monopole "
                     "(A1's four rows; for walls and global monopoles not READ, OPEN as unchecked; the texture moves "
                     "nothing, the throat-support row grades no supply)",
         (I(ds4, A["DEFBSUP"]) if "defb-asserted" in mutate else I(A["DEFBSUP"], An(ds4, A["N_DEFB"])))),
        ("B66-FKZ", "Frolov, Krtous & Zelnikov 2305.03887 (READ by A1, pp.1,5,17-18): a traversable wormhole whose two "
                    "mouths sit in one space at unequal surrounding mass becomes a time machine after T ~ R L c/(G M) "
                    "(1.4e9 yr for an Earth-mass shell, L = 1 ly, defects.figures); the seat mouth lies on the loop.  "
                    "Encoded for DTHR (A1's row; reading 'fkz-generic' extends it to every held throat).  Averted by "
                    "N_MBAL",
         A["CTCW"] == An(fkz_who, A["HELD"], N(A["N_MBAL"]))),
        ("B66-CTCW", "a wormhole time machine is a closed causal curve (O-LOOP-S)", I(A["CTCW"], A["LOOPS"])),
        ("B66-WALL", "A1 / defects.vis_time_function (D66-fix): the M4-M4 wall has a global time function, so no loop "
                     "at a wall (encoded as no constraint; only the CONTROL mutation 'wall-loop' asserts one)",
         I(wall, A["LOOPS"])),
        ("B66-SEAT", "M-S1A-P3 (i) at the seat: a closed causal curve or Borde pathology AT THE SEAT (SEATLOOP) needs a "
                     "source: a CTC at Bob (combine B-DCTC: the D-CTC is at the destination), the FKZ time machine "
                     "(seat mouth on the loop), a throat-bits throat whose "
                     "pathology sits at the seat (outside H-SEAT-OFF-THROAT, A2), or QET outside H-FLAT-QFT (A3).  Static "
                     "string and monopole seats: g^tt < 0, stably causal (defects.static_is_stably_causal); the wall "
                     "seat: Minkowski T a global time function (defects.vis_time_function).  The first two sources "
                     "force it",
         An(I(A["SEATLOOP"], Or(A["CTC"], A["CTCW"], wall, An(tb, N(A["N_SEATOFF"])),
                                An(Or(A["QET"], A["QLIT"]), N(A["N_FLATQFT"])))),
            I(Or(A["CTC"], A["CTCW"], wall), A["SEATLOOP"]))),
        ("B66-LIN", "encoding E-LIN: quantum mechanics is linear unless a member commits a non-linear dynamics -- W2 "
                    "(C-W2), W1 and KR (non-linear by their definitions, combine.SUBREADINGS) -- or the D-CTC (B-DCTC: "
                    "F2b with N_DCTC is non-linear).  combine left LIN free where nothing named it; R-LIT's FALSE-IF is "
                    "scoped to linear QM (A3), so the scope is made explicit here",
         I(N(A["LIN"]), Or(A["W2"], A["W1"], A["KR"], A["CAPD"]))),
    ]
    if "qlit-free" not in mutate:
        rows.append(("B66-ARR", "A3 (qet.py A10, A11 and the eps = 1/2 row; Hotta 0803.2272v3 p.14 READ): in linear QM, "
                                "on the minimal model and in the 1+1 field, the bit's arrival alone leaves local energy "
                                "0 at the seat (|.| < 1e-12); with no correlation (k = 0) no operation extracts; an "
                                "uncorrelated bit extracts 0.  So arrival-alone negative energy (ARRNEG) needs a "
                                "non-linear dynamics, which nothing computes",
                     I(A["ARRNEG"], N(A["LIN"]))))
    if "sm-only" in mutate:
        rows.append(("B66-SM", "H-SM-ONLY (reading, A1): the Standard Model's vacuum manifold S^3 has pi_0 = pi_1 = pi_2 = "
                               "0 (HK p.36, DURRER p.4), so no stable string, wall or monopole (and no string to support "
                               "a throat) exists",
                     N(Or(ds4, A["DTHR"]))))
    if "open-forced" in mutate:      # CONTROL for the vacuity guard: a reading consistent only through an OPEN pathway
        rows.append(("B66-OPENFORCED", "CONTROL ONLY: QET forced to need N_QETHAD", I(A["QET"], A["N_QETHAD"])))
    return rows


def commitments66(A):
    """What each D66 reading commits to unconditionally: (name, ground, literal, expression)."""
    N = z3.Not
    return [
        ("C-DTHR", "A1: every string-supported throat read (Visser polyhedral, GV ring, FGM) is a Lorentzian wormhole "
                   "-- a geometric throat (encoding E-THROAT)", A["DTHR"], A["THROAT"]),
        ("C-TBHOLO", "A2 R-HOLO: the throat sphere of radius r_fit holding A/(4 l_P^2 ln2) bits is geometry",
         A["TBHOLO"], A["THROAT"]),
        ("C-TBTSH", "A2 R-THINSHELL (PV gr-qc/9506083v1 p.1 READ): a distributional Einstein tensor on a geodesically "
                    "complete manifold -- a geometric (singular) throat", A["TBTSH"], A["THROAT"]),
        ("C-TBTEL", "A2 R-TELEPORT (GJW 1608.05687v3, MSY 1704.05333v1 READ): the traversable bridge is geometry, made "
                    "traversable by the coupling", A["TBTEL"], A["THROAT"]),
        ("C-DTEX", "A1 (defects.derrick(3): dE/dlambda = I1 + 3 I2 > 0, no stationary point; DURRER Table 1 p.4 READ: "
                   "textures 'form d = 0 events in spacetime'): a texture seat is an event, so it cannot persist",
         A["DTEX"], N(A["N_SEATPERSIST"])),
        ("C-QLIT", "A3 R-LIT, the question's parenthetical read as arrival alone ('information arriving ... creates'): "
                   "the bit's arrival, with no conditioned operation and no prior correlation, is itself exotic matter "
                   "(arrival-alone negative energy).  M's sentence read operationally is R-QET (V66-1 #7); wave 1's "
                   "words here, 'R-LIT, M's sentence alone: the introduction of information ...', are kept as history",
         A["QLIT"], A["ARRNEG"]),
    ]


# =====================================================================================================================
# THE SCREEN: combine's engine, extended
# =====================================================================================================================
class D66Screen(C.Screen):
    def __init__(self, cell=C.CELL_MAIN, mutate=(), win_open=None):
        if not _STATE["extended"]:
            raise RuntimeError("D66Screen needs the extended vocabulary (E-EXTEND)")
        super().__init__(cell=cell, mutate=mutate, win_open=win_open)
        A = self.A
        self.widened = widen_terms(A, self.win_open, self.mutate)
        for name, (g, _term, expr) in self.widened.items():
            ind = self.byname["@" + name]
            self.base = [b for b in self.base if not b.eq(ind)]        # the original's constraint is now inactive
            del self.ind["@" + name]
            self._track(name + "/66", g + "  ||  " + WIDEN_TEXT[name], expr)
            self.base.append(self.byname["@" + name + "/66"])
            if name in self.constraints:
                self.constraints[name] = expr
        for name, g, expr in board66(A, self.mutate):
            self._track(name, g, expr)
            self.base.append(self.byname["@" + name])
            self.constraints[name] = expr
        for name, g, lit, expr in commitments66(A):
            self._track(name, g, z3.Implies(lit, expr))
            self.base.append(self.byname["@" + name])
        self.open_idx = {k: i for i, k in enumerate(self.open_named)}

    # ------------------------------------------------------------------ helpers over one screened variant
    def _pn(self, present):
        A = self.A
        return ([A[n] for n in C.LIT_NAMES if n in present], [z3.Not(A[n]) for n in C.LIT_NAMES if n not in present])

    def _only_open(self, k):
        return [self.A[j] if j == k else z3.Not(self.A[j]) for j in self.open_named]

    def defeats(self, L, named, goal_fail):
        """OPEN pathways under which a support (its named premises assumed, the variant's literals fixed) admits the
        goal's failure."""
        A = self.A
        prem = [A[n] for n in named]
        return [k for k in self.open_named if self.sat(L + prem + self._only_open(k) + [goal_fail])]

    def screen(self, present):
        """combine's variant(), then the D66 fields: the vacuity flag (consistent with every OPEN pathway false), the
        seat condition, and every removal's defeasibility."""
        A = self.A
        res = self.variant(set(present))
        if not res["consistent"]:
            return res
        L = self.lits(present)
        res["sat_open_false"] = self.sat(L + self.noopen)
        mss = [a["premises"] for a in res["accounts"]]
        pos, neg = self._pn(present)
        # removals: defeasible via
        dfs = {}
        for o, v in res["per"].items():
            if v["verdict"] in C.RMV:
                per_sup = [set(self.defeats(L, s["named"], z3.Not(A[C.RM[o]]))) for s in v["supports"]]
                both = sorted(set.intersection(*per_sup)) if per_sup else []
                if both:
                    dfs[o] = both
        res["defeasible"] = dfs
        # the seat condition M-S1A-P3 (i)
        kind, sups = self._supports(L, mss, A["SEATLOOP"], pos, neg)
        if kind:
            sp = [self._split(s) for s in sups]
            per_sup = [set(self.defeats(L, s["named"], A["SEATLOOP"])) for s in sp]
            seat = {"verdict": "SATISFIED" if kind == "plain" else "SATISFIED-IF", "supports": sp,
                    "defeasible": sorted(set.intersection(*per_sup)) if per_sup else []}
        elif not self.sat(L + self.noopen + [z3.Not(A["SEATLOOP"])]):
            seat = {"verdict": "VIOLATED"}
        else:
            st = self._open_status(L, z3.Not(A["SEATLOOP"]))
            seat = {"verdict": st["verdict"], "via": st.get("via", [])}
        res["seat"] = seat
        res["premise_clash_named"] = sorted(tuple(p["named"]) for p in res["premise_clashes"])
        res["d66_load"] = self.d66_load(present, res)
        return res

    def d66_load(self, present, res):
        """Per lifted obstruction: is a D66 literal LOAD-BEARING?  A support holding a D66 literal is tested with its
        D66 members FREED (the absent literals still fixed false, its D68 members and named premises kept): if the goal
        is still forced, the D66 literal carries nothing there (it entered the support only by entailing a D68 member,
        e.g. R-LIT entails W2 through B66-LIN).  'needed' = every support needs a D66 literal; 'alternative' = some do,
        some do not.  The raw field d66_in_support lists every obstruction with a D66 literal in some support."""
        A = self.A
        d66 = set(present) & set(D66_LITS)
        out = {"d66_in_support": [], "needed": [], "alternative": []}
        if not d66:
            return out
        absent = [z3.Not(A[n]) for n in C.LIT_NAMES if n not in present]
        for o, v in res["per"].items():
            for kind, goal in (("R", A[C.RM[o]]), ("NB", A[C.NB[o]] if o in C.NB else None)):
                if goal is None:
                    continue
                sups = (v["supports"] if (kind == "R" and v["verdict"] in C.RMV) else
                        (v["supports"] if (kind == "NB" and v["verdict"] in C.NBV) else
                         (v["nb"]["supports"] if (kind == "NB" and "nb" in v) else [])))
                if not sups:
                    continue
                if any(set(sp["members"]) & d66 for sp in sups):
                    out["d66_in_support"].append(o + ":" + kind)
                need = []
                for sp in sups:
                    if not set(sp["members"]) & d66:
                        need.append(False)
                        continue
                    hard = (self.base + self.noopen + absent + [A[m] for m in sp["members"] if m not in d66] +
                            [A[x] for x in sp["named"]] + [z3.Not(goal)])
                    need.append(self.check(hard) == z3.sat)
                if all(need):
                    out["needed"].append(o + ":" + kind)
                elif any(need):
                    out["alternative"].append(o + ":" + kind)
        return out


# =====================================================================================================================
# VARIANTS
# =====================================================================================================================
def d66_combos():
    """Every non-empty combination of the three hypotheses, each in every reading: [(combo, readings)]."""
    out = []
    for k in range(1, 4):
        for combo in itertools.combinations(D66_HYPS, k):
            for pick in itertools.product(*[list(D66_READINGS[h]) for h in combo]):
                out.append((combo, pick))
    return out


def contexts():
    return [tuple(x for part in ctx for x in part) for ctx in itertools.product(IT_CTX, SHAPE_CTX, W2F1_CTX, RQ_CTX)]


UNTESTED = []


def variants66():
    """[(combo, readings, context, present)] -- every D66 reading-combination with every bearing D68 context, plus the
    32 context-only variants (D66 absent, the reference each D66 variant is compared with).  R-ITB is ITB located at the
    throat: its variants carry ITB, so the H-IT contexts ITE / ITJ (two readings of H-IT at once, which D68 never
    screens) are NOT TESTED and the none / ITB contexts coincide (deduplicated)."""
    UNTESTED.clear()
    out, seen = [], set()
    for ctx in contexts():
        p = frozenset(ctx)
        if p not in seen:
            seen.add(p)
            out.append(((), (), ctx, p))
    for combo, pick in d66_combos():
        for ctx in contexts():
            lits = set(pick) | set(ctx)
            if "TBITB" in pick:
                if {"ITE", "ITJ"} & set(ctx):
                    UNTESTED.append({"readings": pick, "context": ctx,
                                     "reason": "R-ITB carries D68's ITB; with ITE / ITJ it would be two readings of "
                                               "H-IT at once, which D68's screen never forms"})
                    continue
                lits.add("ITB")
            p = frozenset(lits)
            if p in seen:
                continue
            seen.add(p)
            out.append((combo, pick, ctx, p))
    return out


# =====================================================================================================================
# RUNNING (fork pool; each worker builds its own D66Screen)
# =====================================================================================================================
_W = {}


def _winit(cell, mutate):
    _W["scr"] = D66Screen(cell=cell, mutate=mutate)


def _wrun(item):
    combo, pick, ctx, present = item
    r = _W["scr"].screen(set(present))
    r["combo"], r["readings"], r["context"] = list(combo), list(pick), list(ctx)
    return r


def run(cell=C.CELL_MAIN, mutate=(), items=None, procs=None):
    t0 = time.time()
    items = items if items is not None else variants66()
    C.cell_window_open(cell)                         # computed once in the parent; the fork inherits the cache
    procs = procs or min(4, os.cpu_count() or 1)
    rows = None
    if procs > 1 and os.environ.get("COMBINE66_SERIAL") != "1":
        try:
            import multiprocessing as mp
            with mp.get_context("fork").Pool(procs, initializer=_winit, initargs=(cell, tuple(mutate))) as pool:
                rows = pool.map(_wrun, items, chunksize=16)
        except Exception as e:                      # recorded, then serial: never a silent skip
            print("parallel run failed, running serially:", repr(e), file=sys.stderr)
            rows = None
    if rows is None:
        _winit(cell, tuple(mutate))
        rows = [_wrun(it) for it in items]
    return {"rows": rows, "by": {frozenset(r["present"]): r for r in rows}, "seconds": time.time() - t0,
            "cell": cell, "mutate": list(mutate)}


# =====================================================================================================================
# VIEWS
# =====================================================================================================================
def _vclass(v):
    """A verdict -> R / NB / OPEN / SILENT / LEFT (the NB beside a removal is reported by counts())."""
    w = v["verdict"]
    return "R" if w in C.RMV else "NB" if w in C.NBV else w


def d66_attributed(r, kinds=C.RMV + C.NBV):
    """Obstructions removed / not-bound with a D66 literal LOAD-BEARING in some support (D66Screen.d66_load: 'needed'
    or 'alternative'); kinds RMV counts removals only.  The raw 'a D66 literal appears in a support' is d66_in_support."""
    if not r["consistent"]:
        return []
    want = {"R"} if set(kinds) <= set(C.RMV) else {"R", "NB"}
    ld = r.get("d66_load", {})
    hits = [x for x in ld.get("needed", []) + ld.get("alternative", []) if x.split(":")[1] in want]
    return sorted({x.split(":")[0] for x in hits}, key=C.OBST.index)


def lifted(r):
    """Obstructions removed or not-bound (any route)."""
    return set(C.counts(r)) if r["consistent"] else set()


def compare_to_context(R):
    """Per D66 variant: interference (lifted in the context-only variant, not here, and which D66 literal undoes it),
    new OPEN pathways (via lists gained), and D66 attribution."""
    by = R["by"]
    for r in R["rows"]:
        if not r["readings"] or not r["consistent"]:
            continue
        base = by.get(frozenset(r["present"]) - set(D66_LITS))      # the same variant with the D66 literals removed
        r["d66_attributed"] = d66_attributed(r)
        r["d66_attributed_removed"] = d66_attributed(r, C.RMV)
        if base is None or not base["consistent"]:
            r["interference"], r["new_open"] = None, None
            continue
        lost = sorted(lifted(base) - lifted(r), key=C.OBST.index)
        causes = {}
        for o in lost:
            causes[o] = []
            for m in r["readings"]:
                other = by.get(frozenset(r["present"]) - {m})
                if other and other["consistent"] and o in lifted(other):
                    causes[o].append(m)
        r["interference"] = {"lost": lost, "causes": causes}
        new = {}
        for o in C.OBST:
            a, b = r["per"][o], base["per"][o]
            va = set(a.get("via", []) or a.get("removal", {}).get("via", []))
            vb = set(b.get("via", []) or b.get("removal", {}).get("via", []))
            if va - vb:
                new[o] = sorted(va - vb)
        r["new_open"] = new
        r["new_defeasible"] = {o: sorted(set(ks) - set(base.get("defeasible", {}).get(o, [])))
                               for o, ks in r.get("defeasible", {}).items()
                               if set(ks) - set(base.get("defeasible", {}).get(o, []))}
        bs, rs = base["seat"], r["seat"]
        r["seat_change"] = None if (bs["verdict"], bs.get("defeasible"), [tuple(s["named"]) for s in bs.get("supports", [])]) == \
            (rs["verdict"], rs.get("defeasible"), [tuple(s["named"]) for s in rs.get("supports", [])]) else \
            {"context": bs, "variant": rs}
    return R


def headline(R):
    """Maxima over consistent D66 variants: member-attributed removals per ACCOUNT (any member; never across two
    accounts), non-bindings per account, and the D66-attributed removals / non-bindings per variant (a support holding a
    D66 literal).  Each with the variants attaining it and a smallest one."""
    best = {k: [0, 0, None] for k in ("member_removed", "not_bound", "d66_removed", "d66_nb")}

    def upd(k, v, pres):
        if v > best[k][0]:
            best[k] = [v, 1, pres]
        elif v == best[k][0] and v > 0:
            best[k][1] += 1
            if len(pres) < len(best[k][2]):
                best[k][2] = pres
    for r in R["rows"]:
        if not r["readings"] or not r["consistent"]:
            continue
        pres = sorted(r["present"])
        accs, _ = C.account_view(r)
        upd("member_removed", max((len(a["member_removed"]) for a in accs), default=0), pres)
        upd("not_bound", max((len(a["not_bound"]) for a in accs), default=0), pres)
        rm = r.get("d66_attributed_removed", [])
        upd("d66_removed", len(rm), pres)
        upd("d66_nb", len([o for o in r.get("d66_attributed", []) if o not in rm]), pres)
    return best


def survivors(R):
    """Obstructions (seven forms) removed or not-bound in NO consistent D66 variant, with their OPEN status census."""
    rows = [r for r in R["rows"] if r["readings"] and r["consistent"]]
    out = {}
    for o in C.OBST:
        if any(o in lifted(r) for r in rows):
            continue
        cen = {}
        for r in rows:
            v = r["per"][o]
            key = v["verdict"] + (" via " + ", ".join(v.get("via", [])) if v.get("via") else "")
            cen[key] = cen.get(key, 0) + 1
        out[o] = cen
    return out


def removal_census(R):
    """Every obstruction lifted in some consistent D66 variant: by what (D66 member, D68 member, or no member)."""
    rows = [r for r in R["rows"] if r["readings"] and r["consistent"]]
    out = {}
    for o in C.OBST:
        n_any = n_d66 = n_d68 = n_none = n_ent = 0
        for r in rows:
            v = r["per"][o]
            sups = C._sups_with(v, C.RMV + C.NBV)
            if not sups:
                continue
            n_any += 1
            mem = set().union(*[set(s["members"]) for s in sups])
            if o in d66_attributed(r):
                n_d66 += 1
            elif mem & set(D66_LITS):
                n_ent += 1
            elif mem:
                n_d68 += 1
            else:
                n_none += 1
        if n_any:
            out[o] = {"lifted": n_any, "D66 literal load-bearing": n_d66,
                      "D66 literal in a support, not load-bearing (entails a D68 member)": n_ent,
                      "D68 member only": n_d68, "no member": n_none}
    return out


def clash_census(R):
    rows = [r for r in R["rows"] if r["readings"]]
    inc = [r for r in rows if not r["consistent"]]
    cores = {}
    for r in inc:
        for c in r["clash_cores"]:
            key = tuple(sorted(x for x in c if not x.startswith("Not(")))
            cores[key] = cores.get(key, 0) + 1
    pcl = {}
    for r in rows:
        if r["consistent"]:
            for p in r["premise_clash_named"]:
                pcl[p] = pcl.get(p, 0) + 1
    return {"variants": len(rows), "consistent": len(rows) - len(inc), "inconsistent": len(inc),
            "cores (assumption names, absences dropped)": {" + ".join(k): v for k, v in sorted(cores.items())},
            "premise clashes": {" + ".join(k): v for k, v in sorted(pcl.items())}}


def seat_census(R):
    rows = [r for r in R["rows"] if r["readings"] and r["consistent"]]
    out = {}
    for r in rows:
        s = r["seat"]
        key = s["verdict"]
        if s.get("supports") and s["verdict"] == "SATISFIED-IF":
            key += " {" + " | ".join(", ".join(x["named"]) for x in s["supports"]) + "}"
        if s.get("defeasible"):
            key += "; defeasible via " + ", ".join(s["defeasible"])
        out[key] = out.get(key, 0) + 1
    return out


def by_combo(R):
    """The 7 combinations: consistent count, D66-attributed lifts, interference, new OPEN pathways."""
    out = {}
    for r in R["rows"]:
        if not r["readings"]:
            continue
        k = " x ".join(r["combo"])
        e = out.setdefault(k, {"variants": 0, "consistent": 0, "d66_attributed_lifts": 0, "interference": {},
                               "new_open": {}, "new_defeasible": {}, "seat": {}})
        e["variants"] += 1
        if not r["consistent"]:
            continue
        e["consistent"] += 1
        if r.get("d66_attributed"):
            e["d66_attributed_lifts"] += 1
        for o in (r.get("interference") or {}).get("lost", []):
            for m in r["interference"]["causes"][o] or ["(context)"]:
                kk = "%s by %s" % (o, m)
                e["interference"][kk] = e["interference"].get(kk, 0) + 1
        for o, ks in (r.get("new_open") or {}).items():
            for kx in ks:
                kk = "%s via %s" % (o, kx)
                e["new_open"][kk] = e["new_open"].get(kk, 0) + 1
        for o, ks in (r.get("new_defeasible") or {}).items():
            for kx in ks:
                kk = "%s via %s" % (o, kx)
                e["new_defeasible"][kk] = e["new_defeasible"].get(kk, 0) + 1
        sv = r["seat"]["verdict"] + ("; defeasible" if r["seat"].get("defeasible") else "")
        e["seat"][sv] = e["seat"].get(sv, 0) + 1
    return out


def pathway_census(R):
    """For each D66 OPEN pathway: in how many consistent variants it appears in an OPEN verdict, and on which forms."""
    out = {k: {} for k in D66_OPEN}
    for r in R["rows"]:
        if not r.get("consistent") or not r["readings"]:
            continue
        for o, v in r["per"].items():
            for k in set(v.get("via", []) or v.get("removal", {}).get("via", [])) & set(D66_OPEN):
                out[k][o] = out[k].get(o, 0) + 1
        for o, ks in r.get("defeasible", {}).items():
            for k in set(ks) & set(D66_OPEN):
                out[k]["defeats " + o] = out[k].get("defeats " + o, 0) + 1
        for k in set(r["seat"].get("defeasible", [])) & set(D66_OPEN):
            out[k]["defeats the seat"] = out[k].get("defeats the seat", 0) + 1
    return out


def member_removal_census(R):
    """Member-attributed removals per account (any member): the maximum and what they are."""
    mx, what = 0, {}
    for r in R["rows"]:
        if not r["readings"] or not r["consistent"]:
            continue
        accs, _ = C.account_view(r)
        for ac in accs:
            n = len(ac["member_removed"])
            if n > mx:
                mx, what = n, {}
            if n == mx and n:
                for o in ac["member_removed"]:
                    sup = [s["members"] for s in C._sups_with(r["per"].get(o, {"verdict": "-"}), C.RMV)] if o in r["per"] \
                        else [s["members"] for f in C.FOLD.get(o, ()) for s in C._sups_with(r["per"][f], C.RMV)]
                    key = "%s by %s" % (o, " | ".join("{" + ", ".join(m) + "}" for m in sup))
                    what[key] = what.get(key, 0) + 1
    return {"max_member_removals_per_account": mx, "what": what}


# =====================================================================================================================
# GUARDS
# =====================================================================================================================
def _sample_d68(step):
    vs = C.variants()
    return [(combo, frozenset(p)) for i, (combo, p) in enumerate(vs) if i % step == 0]


def conservative_extension(step=24, procs=None):
    """D68 variants (every step-th of combine.variants(), plus the 32 contexts): combine's Screen under combine's OWN
    vocabulary, then D66Screen under the extended one.  The signatures (verdict, OPEN via, NB beside, premise-clash
    sets) must be identical, and so must the D68-literal supports of every lifted obstruction."""
    items = _sample_d68(step)
    ctx = [((), frozenset(c)) for c in {frozenset(c) for c in contexts()}]
    items = items + [x for x in ctx if x[1] not in {p for _, p in items}]
    t0 = time.time()
    with vocabulary(False):
        s0 = C.Screen(cell=C.CELL_MAIN)
        base = {}
        for combo, p in items:
            r = s0.variant(set(p))
            base[p] = (C.signature(r), _sup_sig(r))
    with vocabulary(True):
        s1 = D66Screen(cell=C.CELL_MAIN)
        diff = []
        for combo, p in items:
            r = s1.variant(set(p))
            if (C.signature(r), _sup_sig(r)) != base[p]:
                diff.append(sorted(p))
    return {"compared": len(items), "differ": diff, "seconds": time.time() - t0}


def _sup_sig(r):
    if not r["consistent"]:
        return None
    return tuple((o, tuple(sorted(tuple(s["members"]) + tuple(s["named"]) for s in C._sups_with(v, C.RMV + C.NBV))))
                 for o, v in r["per"].items())


def vacuity(scr):
    """Vacuity guards (each a query whose answer is content) and the STRUCTURAL items."""
    A = scr.A
    L = lambda pres: scr.lits(set(pres))
    out = {}
    out["board alone SAT"] = scr.sat(L(()))
    singles = {}
    for k in D66_LITS:
        pres = {k, "ITB"} if k == "TBITB" else {k}
        singles[k] = scr.sat(L(pres))
    out["singles SAT"] = singles
    named = [A[n] for n in D66_NAMED]
    out["D66 named premises jointly SAT with the board (OPEN false)"] = scr.sat(L(()) + scr.noopen + named)
    out["D66 named premises jointly SAT with every D66 reading that names one (OPEN false)"] = all(
        scr.sat(L(pres) + scr.noopen + named) for pres in ({"DTHR"}, {"TBHOLO"}, {"QET"}))
    # each D66 OPEN pathway can hold together with its own reading (it is a live possibility, not a dead atom)
    out["each D66 pathway SAT with its owner"] = {k: scr.sat(L(sorted(own_)[:1]) + [A[k]]) for k, own_ in
                                                  PATHWAY_OWNER.items()}
    return out


def pathway_ties(scr):
    """CONTROLS: each D66 pathway opens (or defeats) only where encoded.  For an OPENING pathway k on obstruction o:
    with k alone true the removal of o is possible with the owner present and impossible with a non-owner present.
    (D66-fix: N_WALLLOOP retired -- the wall's causal structure is computed; N_WNCC's owner test now uses DTHR, the
    reading M's ruling newly covers.)"""
    A = scr.A
    # D66-RULINGS (M-RULINGS item 28): N_WNCC is now also the D68 board's pathway for every geometric throat, and every
    # variant without ITB's non-geometric premise has one (combine's B-THROAT), so its non-owner is ITB WITH N_QTOPO (no
    # geometric throat) -- D66-fix used QET, which a throat now accompanies on the board
    spec = {"N_DEFB": ("O-SEAT", "DSTR", "QET", ()), "N_NEGT": ("O-HOLD", "DTHR", "DSTR", ()),
            "N_GJWPAY": ("O-HOLD", "TBTEL", "TBISL", ()), "N_PINCH": ("O-HOLD", "TBTSH", "TBTEL", ()),
            "N_QETHAD": ("O-HOLD", "QET", "TBISL", ()), "N_WNCC": ("O-MAKE-TOPO", "DTHR", "ITB", ("N_QTOPO",))}
    out = {}
    for k, (o, yes, no, extra) in spec.items():
        a = scr.sat(scr.lits({yes}) + scr._only_open(k) + [A[C.RM[o]]])
        b = scr.sat(scr.lits({no}) + scr._only_open(k) + [A[x] for x in extra] + [A[C.RM[o]]])
        out[k] = {"opens with " + yes: a, "opens with " + no + "".join(" + " + x for x in extra): b, "ok": a and not b}
    return out


# ------------------------------------------------------------------------------------------------ encoding drift
_RG = {}


def report_grades():
    """The DOCKET 66 A-reports' own grades, never retyped, normalised to {key, per, seat, own} -- D66-fix: asked of the
    INSTRUMENTS at run time (defects.a1_grades(), throatbits.grades(), qet.grades()), so a corrected instrument is what
    the drift guard reads.  Wave 1 read stored scratchpad JSON (A1-defects.json written by hand beside defects.py,
    A2-throatbits-report.json, A3-qet.json), which went stale the moment an instrument changed."""
    if _RG:
        return dict(_RG)
    G = {}
    D, TB, Q = own("defects"), own("throatbits"), own("qet")
    spec = TB.specthm_verdicts()
    srcs = (("A1-defects", lambda: D.a1_grades(), "hypothesis", "per_obstruction", None, "defects.a1_grades()"),
            ("A2-throatbits", lambda: TB.grades(spec), "reading", "per", None, "throatbits.grades()"),
            ("A3-qet", lambda: Q.grades(spec), "reading", "per", "verdict_on_own_content", "qet.grades()"))
    for rid, fn, kk, pk, ok, lab in srcs:
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                gs = fn()
            G[rid] = [{"key": g[kk], "per": g[pk], "seat": g.get("seat_conditions", ""),
                       "own": g.get(ok, "") if ok else "", "source": lab} for g in gs]
        except Exception as e:
            G[rid] = None
            G[rid + " error"] = repr(e)
    _RG.update(G)
    return G


def _field_text(grade, field, o):
    if field == "seat":
        return grade["seat"]
    if field == "own":
        return grade["own"]
    per = grade["per"]
    return per if isinstance(per, str) else per.get(o, "")


#: (report, grade key, field, verbatim fragment, obstruction / 'SEAT' / 'OWN', variant, graded literals, rule note).
#: Every fragment must occur VERBATIM in the stored grade text (anchor check), and the fragment is what is parsed: by
#: combine.parse_report_class (P1 parentheticals dropped, P8 first clause, P9 LEFT-IF -> OPEN) for an obstruction, by
#: SEAT_PARSE for the seat, FALSE-IF -> CLASH for a reading's own content.  The fragment is the grade's leading clause
#: except where a rule note says which clause is compared and why.
DRIFT_ROWS = [
    # A1 -- H-DEFECT-SEAT (per_obstruction is one string)
    ("A1-defects", "), string (static", "per", "O-SEAT OPEN via N_S5 | N_DEFB", "O-SEAT", {"DSTR"}, {"DSTR"}, ""),
    ("A1-defects", "), string (static", "per", "O-HOLD LEAVES", "O-HOLD", {"DSTR"}, {"DSTR"}, ""),
    ("A1-defects", "), string (static", "per", "O-LOOP none (static)", "O-LOOP", {"DSTR"}, {"DSTR"}, ""),
    ("A1-defects", "), string (static", "per", "O-MAKE-TOPO LEAVES", "O-MAKE-TOPO", {"DSTR"}, {"DSTR"}, ""),
    ("A1-defects", "), string (static", "per", "O-MAKE-DIST LEAVES", "O-MAKE-DIST", {"DSTR"}, {"DSTR"}, "Z2'"),
    ("A1-defects", "), string (static", "per", "O-BITS LEAVES", "O-BITS", {"DSTR"}, {"DSTR"}, ""),
    ("A1-defects", "), string (static", "seat", "M-S1A-P3 (i) PASSES", "SEAT", {"DSTR"}, {"DSTR"}, ""),
    ("A1-defects", "domain wall", "per", "O-SEAT OPEN via N_S5 | N_DEFB", "O-SEAT", {"DWALL"}, {"DWALL"}, ""),
    ("A1-defects", "domain wall", "per", "O-HOLD LEAVES", "O-HOLD", {"DWALL"}, {"DWALL"}, ""),
    ("A1-defects", "domain wall", "per", "O-LOOP none", "O-LOOP", {"DWALL"}, {"DWALL"},
     "D66-fix: wave 1 graded 'O-LOOP OPEN' (N_WALLLOOP, Z7); the wall's time function is computed"),
    ("A1-defects", "domain wall", "per", "O-MAKE-TOPO LEAVES", "O-MAKE-TOPO", {"DWALL"}, {"DWALL"}, ""),
    ("A1-defects", "domain wall", "per", "O-MAKE-DIST LEAVES", "O-MAKE-DIST", {"DWALL"}, {"DWALL"}, "Z2'"),
    ("A1-defects", "domain wall", "per", "O-BITS LEAVES", "O-BITS", {"DWALL"}, {"DWALL"}, ""),
    ("A1-defects", "domain wall", "seat", "M-S1A-P3 (i) PASSES under H-VIS-MINKOWSKI", "SEAT", {"DWALL"}, {"DWALL"},
     "D66-fix: wave 1 graded 'CTC/Borde at a wall seat OPEN'"),
    ("A1-defects", "global monopole", "per", "O-SEAT OPEN via N_S5 | N_DEFB", "O-SEAT", {"DGMON"}, {"DGMON"}, ""),
    ("A1-defects", "global monopole", "per", "O-HOLD LEAVES", "O-HOLD", {"DGMON"}, {"DGMON"}, ""),
    ("A1-defects", "global monopole", "per", "O-LOOP none (static)", "O-LOOP", {"DGMON"}, {"DGMON"}, ""),
    ("A1-defects", "global monopole", "per", "others LEAVES", "O-MAKE-TOPO", {"DGMON"}, {"DGMON"}, ""),
    ("A1-defects", "global monopole", "per", "others LEAVES", "O-MAKE-DIST", {"DGMON"}, {"DGMON"}, "Z2'"),
    ("A1-defects", "global monopole", "per", "others LEAVES", "O-BITS", {"DGMON"}, {"DGMON"}, ""),
    ("A1-defects", "global monopole", "seat", "PASSES (static)", "SEAT", {"DGMON"}, {"DGMON"}, ""),
    ("A1-defects", "gauge monopole", "per", "O-SEAT OPEN via N_S5 | N_DEFB", "O-SEAT", {"DMON"}, {"DMON"}, ""),
    ("A1-defects", "gauge monopole", "per", "O-HOLD LEAVES", "O-HOLD", {"DMON"}, {"DMON"}, ""),
    ("A1-defects", "gauge monopole", "per", "O-LOOP none outside r_+", "O-LOOP", {"DMON"}, {"DMON"}, ""),
    ("A1-defects", "gauge monopole", "per", "others LEAVES", "O-MAKE-TOPO", {"DMON"}, {"DMON"}, ""),
    ("A1-defects", "gauge monopole", "per", "others LEAVES", "O-BITS", {"DMON"}, {"DMON"}, ""),
    ("A1-defects", "gauge monopole", "seat", "PASSES outside r_+", "SEAT", {"DMON"}, {"DMON"}, ""),
    ("A1-defects", "texture", "per", "no obstruction moved", "O-SEAT", {"DTEX"}, {"DTEX"}, "Z6"),
    ("A1-defects", "texture", "per", "no obstruction moved", "O-HOLD", {"DTEX"}, {"DTEX"}, ""),
    ("A1-defects", "texture", "per", "no obstruction moved", "O-LOOP", {"DTEX"}, {"DTEX"}, ""),
    ("A1-defects", "texture", "per", "no obstruction moved", "O-BITS", {"DTEX"}, {"DTEX"}, ""),
    ("A1-defects", "texture", "seat", "EMPTY IF {H-SEAT-PERSISTS}", "SEAT", {"DTEX"}, {"DTEX"}, ""),
    ("A1-defects", "THROAT's support", "per", "Outside it, OPEN via N_NEGT", "O-HOLD", {"DTHR"}, {"DTHR"},
     "'LEFT given H-CANONICAL ... Outside it, OPEN via N_NEGT' is LEFT-IF {H-CANONICAL}: P9 reads OPEN, so the OPEN "
     "clause is compared (P8 alone would read the leading LEFT)"),
    ("A1-defects", "THROAT's support", "per", "O-LOOP reintroduced for mouths in one space", "O-LOOP", {"DTHR"},
     {"DTHR"}, "combine reads REINTRODUCED as N; Z7 gives {N, OPEN}"),
    ("A1-defects", "THROAT's support", "per", "O-MAKE-TOPO OPEN via N_WNCC", "O-MAKE-TOPO", {"DTHR"},
     {"DTHR"}, "D66-fix: wave 1 graded 'O-MAKE-TOPO binds if made from flat space'; M's ruling M-S1A-P3 applied"),
    ("A1-defects", "THROAT's support", "per", "O-BITS LEAVES", "O-BITS", {"DTHR"}, {"DTHR"}, ""),
    ("A1-defects", "THROAT's support", "seat", "M-S1A-P3 (i) disqualifies it unless the masses balance", "SEAT", {"DTHR"},
     {"DTHR"}, "EXPLAINED (presupposes the held throat); CONTENT check fkz_conditional"),
    # A2 -- H-THROAT-BITS (throatbits.py's own grade table)
    ("A2-throatbits", "R-HOLO:", "per", "LEFT: a capacity is a ceiling on entropy, not a channel", "O-BITS",
     {"TBHOLO"}, {"TBHOLO"}, ""),
    ("A2-throatbits", "R-HOLO:", "per", "OPEN via specthm W-create-ncc (OPEN)", "O-MAKE-TOPO", {"TBHOLO"}, {"TBHOLO"}, ""),
    ("A2-throatbits", "R-HOLO:", "per", "SILENT (this reading distributes nothing)", "O-MAKE-DIST", {"TBHOLO"},
     {"TBHOLO"}, "Z2'"),
    ("A2-throatbits", "R-HOLO:", "per", "LEFT-IF {H-SINGULAR-IS-THINSHELL, H-PV-STATIC}", "O-HOLD", {"TBHOLO"},
     {"TBHOLO"}, "P9: LEFT-IF reads OPEN; the outside is N_PINCH"),
    ("A2-throatbits", "R-HOLO:", "per", "OPEN via N_S5 (D68 unchanged: H-SEAT-S5, M-RULINGS item 7)", "O-SEAT",
     {"TBHOLO"}, {"TBHOLO"}, "Z6"),
    ("A2-throatbits", "R-HOLO:", "per", "SILENT (no loop asserted", "O-LOOP", {"TBHOLO"}, {"TBHOLO"}, ""),
    ("A2-throatbits", "R-HOLO:", "seat", "SATISFIED-IF {H-SEAT-OFF-THROAT} in R-HOLO and R-THINSHELL", "SEAT",
     {"TBHOLO"}, {"TBHOLO"}, ""),
    ("A2-throatbits", "R-THINSHELL:", "per", "LEFT (a shell is geometry; it carries no channel)", "O-BITS", {"TBTSH"},
     {"TBTSH"}, ""),
    ("A2-throatbits", "R-THINSHELL:", "per", "OPEN via specthm W-create-ncc (OPEN)", "O-MAKE-TOPO", {"TBTSH"},
     {"TBTSH"}, ""),
    ("A2-throatbits", "R-THINSHELL:", "per", "SILENT", "O-MAKE-DIST", {"TBTSH"}, {"TBTSH"}, "Z2'"),
    ("A2-throatbits", "R-THINSHELL:", "per", "LEFT-IF {H-SINGULAR-IS-THINSHELL, H-PV-STATIC}", "O-HOLD", {"TBTSH"},
     {"TBTSH"}, "P9"),
    ("A2-throatbits", "R-THINSHELL:", "per", "OPEN via N_S5", "O-SEAT", {"TBTSH"}, {"TBTSH"}, "Z6"),
    ("A2-throatbits", "R-THINSHELL:", "per", "SILENT (PV's manifold has two asymptotic regions and no loop)", "O-LOOP",
     {"TBTSH"}, {"TBTSH"}, ""),
    ("A2-throatbits", "R-THINSHELL:", "seat", "SATISFIED-IF {H-SEAT-OFF-THROAT} in R-HOLO and R-THINSHELL", "SEAT",
     {"TBTSH"}, {"TBTSH"}, ""),
    ("A2-throatbits", "R-TELEPORT:", "per", "LEFT: GJW p.4", "O-BITS", {"TBTEL"}, {"TBTEL"}, ""),
    ("A2-throatbits", "R-TELEPORT:", "per", "NOT-BOUND-IF {H-ER=EPR} -- D68's ITE grade carried in", "O-MAKE-TOPO",
     {"TBTEL", "ITE"}, {"ITE"}, "carried in from D68's ITE, not added: compared with ITE present, credited to ITE"),
    ("A2-throatbits", "R-TELEPORT:", "per", "LEFT-IF {H-GJW-COUNTERPART, MS sec.3.2 (board READ)}", "O-MAKE-DIST",
     {"TBTEL"}, {"TBTEL"}, "P9; Z2'"),
    ("A2-throatbits", "R-TELEPORT:", "per", "LEFT-IF {H-GJW-COUNTERPART, H-ADS-TFD, H-COUPLED} for a hold on GJW alone",
     "O-HOLD", {"TBTEL"}, {"TBTEL"}, "P9.  D66-fix: wave 1's leading clause was 'REMOVED-IF {...} in GJW's setting'"),
    ("A2-throatbits", "R-TELEPORT:", "per", "For a throat that admits the payload in one space: LEFT-IF {H-MMP, "
     "H-SM-FIELDS}", "O-HOLD", {"TBTEL"}, {"TBTEL"},
     "P9: the outside is N_GJWPAY.  MQ's and MMP's REMOVED-IF clauses lie outside the board's setting (E-ADS; scale)"),
    ("A2-throatbits", "R-TELEPORT:", "per", "Without ITE the bridge's creation is OPEN via specthm W-create-ncc",
     "O-MAKE-TOPO", {"TBTEL"}, {"TBTEL"}, "D66-fix: M's ruling M-S1A-P3 applied to the bridge's creation"),
    ("A2-throatbits", "R-TELEPORT:", "per", "OPEN via N_S5", "O-SEAT", {"TBTEL"}, {"TBTEL"}, "Z6"),
    ("A2-throatbits", "R-TELEPORT:", "per", "SILENT (GJW p.13", "O-LOOP", {"TBTEL"}, {"TBTEL"}, ""),
    ("A2-throatbits", "R-TELEPORT:", "seat", "R-TELEPORT adds GJW p.13 (no CTC)", "SEAT", {"TBTEL"}, {"TBTEL"},
     "alias: R-TELEPORT adds to the R-HOLO / R-THINSHELL clause"),
    ("A2-throatbits", "R-ISLAND:", "per", "LEFT-IF {H-ISLAND-COUNTERPART}", "O-BITS", {"TBISL"}, {"TBISL"}, "EXPLAINED"),
    ("A2-throatbits", "R-ISLAND:", "per", "SILENT (replica wormholes are Euclidean saddles", "O-MAKE-TOPO", {"TBISL"},
     {"TBISL"}, ""),
    ("A2-throatbits", "R-ISLAND:", "per", "SILENT", "O-MAKE-DIST", {"TBISL"}, {"TBISL"}, "Z2'"),
    ("A2-throatbits", "R-ISLAND:", "per", "SILENT (no traversable throat in this reading)", "O-HOLD", {"TBISL"},
     {"TBISL"}, ""),
    ("A2-throatbits", "R-ISLAND:", "per", "OPEN via N_S5", "O-SEAT", {"TBISL"}, {"TBISL"}, "Z6"),
    ("A2-throatbits", "R-ISLAND:", "per", "SILENT", "O-LOOP", {"TBISL"}, {"TBISL"}, ""),
    ("A2-throatbits", "R-ITB:", "per", "LEFT (D68 geometry.GRADES ITB: 'LEAVES')", "O-BITS", {"TBITB", "ITB"},
     {"TBITB", "ITB"}, ""),
    ("A2-throatbits", "R-ITB:", "per", "NOT-BOUND-IF {N_QTOPO} -- D68's ITB grade carried in", "O-MAKE-TOPO",
     {"TBITB", "ITB"}, {"TBITB", "ITB"}, ""),
    ("A2-throatbits", "R-ITB:", "per", "LEFT (D68 ITB: 'LEAVES')", "O-MAKE-DIST", {"TBITB", "ITB"}, {"TBITB", "ITB"},
     "Z2'"),
    ("A2-throatbits", "R-ITB:", "per", "NOT-BOUND-IF {N_QTOPO} in its geometric form", "O-HOLD", {"TBITB", "ITB"},
     {"TBITB", "ITB"}, ""),
    ("A2-throatbits", "R-ITB:", "per", "OPEN via N_S5", "O-SEAT", {"TBITB", "ITB"}, {"TBITB", "ITB"}, "Z6"),
    ("A2-throatbits", "R-ITB:", "per", "NOT-BOUND-IF {N_QTOPO} for corridors (D68 ITB)", "O-LOOP", {"TBITB", "ITB"},
     {"TBITB", "ITB"}, ""),
    # A3 -- H-QET-EXOTIC (qet.grades, as stored)
    ("A3-qet", "R-QET:", "per", "LEFT: QET needs the classical bit", "O-BITS", {"QET"}, {"QET"}, ""),
    ("A3-qet", "R-QET:", "per", "SILENT: QET makes no topology", "O-MAKE-TOPO", {"QET"}, {"QET"}, ""),
    ("A3-qet", "R-QET:", "per", "SILENT: QET consumes correlation that already exists", "O-MAKE-DIST", {"QET"}, {"QET"},
     "Z2'"),
    ("A3-qet", "R-QET:", "per", "LEFT-IF {H_flat, H-PATH, H-MIN-SCALAR, H-QET-HADAMARD}", "O-HOLD", {"QET"}, {"QET"}, "P9"),
    ("A3-qet", "R-QET:", "per", "Under ITB the geometric form is NOT-BOUND-IF {N_QTOPO}", "O-HOLD", {"QET", "ITB"},
     {"ITB"}, "the board's grade (A3: 'QET adds nothing to it'), credited to ITB"),
    ("A3-qet", "R-QET:", "per", "LEFT-IF {H-QET-BUDGET, H-MINIMAL for the ratio}", "O-SEAT", {"QET"}, {"QET"}, "P9; Z6"),
    ("A3-qet", "R-QET:", "per", "SILENT: the protocol is causal", "O-LOOP", {"QET"}, {"QET"}, ""),
    ("A3-qet", "R-QET:", "seat", "M-S1A-P3 (i): SATISFIED-IF {H-FLAT-QFT}", "SEAT", {"QET"}, {"QET"}, ""),
    ("A3-qet", "R-LIT:", "own", "FALSE-IF {H-MINIMAL or H-1+1 as the test models, linear QM}", "OWN", {"QLIT"}, {"QLIT"},
     "own content: FALSE-IF -> CLASH"),
    ("A3-qet", "R-LIT:", "per", "SILENT (its operative content is R-QET's)", "O-HOLD", {"QLIT", "W2"}, {"QLIT"},
     "R-LIT is consistent only with a non-linear member: compared in {QLIT, W2}"),
    ("A3-qet", "R-LIT:", "per", "SILENT (its operative content is R-QET's)", "O-SEAT", {"QLIT", "W2"}, {"QLIT"}, "Z6"),
    ("A3-qet", "R-LIT:", "per", "SILENT (its operative content is R-QET's)", "O-BITS", {"QLIT", "W2"}, {"QLIT"}, ""),
    ("A3-qet", "R-LIT:", "seat", "M-S1A-P3 (i): SATISFIED-IF {H-FLAT-QFT}", "SEAT", {"QLIT", "W2"}, {"QLIT"}, ""),
]

#: disagreements whose cause is not a fault on either side -- each with its reason; the guard passes only if every
#: disagreement found is listed here, and a mutated encoding must produce one that is NOT
EXPLAINED66 = {
    ("A2-throatbits", "R-ISLAND:", "O-BITS"):
        "VOCABULARY.  A2 grades R-ISLAND's O-BITS 'LEFT-IF {H-ISLAND-COUNTERPART}'; combine's P9 reads every LEFT-IF as "
        "OPEN because in D68 each LEFT-IF set had an OPEN outside.  Here the condition is the reading's own "
        "identification: outside it R-ISLAND says nothing about bits, so no pathway exists and z3 gives LEFT (N).  "
        "Both sides say O-BITS is not removed",
    ("A1-defects", "THROAT's support", "SEAT"):
        "PRESUPPOSITION.  A1's sentence 'disqualifies it unless the masses balance' is about a TRAVERSABLE string-supported "
        "throat, which A1's own O-HOLD grade makes OPEN (N_NEGT).  z3 holds OPEN pathways false, so the seat reads "
        "SATISFIED, defeasible via N_NEGT; the conditional itself is checked as CONTENT (fkz_conditional: with the throat "
        "held, the seat is free iff N_MBAL)",
}


#: an alias row ('as R-HOLO') is read on the aliased row's own anchored seat fragment
SEAT_ALIAS = {"R-TELEPORT adds GJW p.13 (no CTC)": ("R-TELEPORT:",
                                                     "SATISFIED-IF {H-SEAT-OFF-THROAT} in R-HOLO and R-THINSHELL")}


def SEAT_PARSE(frag):
    t = frag.upper()
    if "EMPTY IF" in t:
        return "PCLASH"
    if "DISQUALIF" in t:
        return "VIOL"
    if "SATISFIED-IF" in t:
        return "SATIF"
    if "PASSES" in t:
        return "SAT"
    if "OPEN" in t:
        return "OPEN"
    return None


def seat_class(r, graded):
    """z3's seat verdict -> classes.  Z7 (seat): a SATISFIED defeasible via the graded literal's own pathway reads
    {SAT, OPEN}; a premise clash naming N_SEATPERSIST reads PCLASH."""
    if not r["consistent"]:
        return {"CLASH"}
    if ("N_SEATPERSIST",) in [tuple(p) for p in r["premise_clash_named"]]:
        return {"PCLASH"}
    s = r["seat"]
    own_paths = {k for k, o in PATHWAY_OWNER.items() if o & set(graded)}
    defeat_own = bool(set(s.get("defeasible", [])) & own_paths)
    if s["verdict"] == "SATISFIED":
        return {"SAT", "OPEN"} if defeat_own else {"SAT"}
    if s["verdict"] == "SATISFIED-IF":
        return {"SATIF", "OPEN"} if defeat_own else {"SATIF"}
    if s["verdict"] == "VIOLATED":
        return {"VIOL"}
    return {"OPEN"}


def z3_class66(r, o, graded):
    """combine.z3_class / _form_class (Z1-Z6), plus Z7: a removal (of O-LOOP's either form, or any obstruction) that is
    defeasible via an OPEN pathway the graded literal owns reads {N, OPEN} -- not removed by the hypothesis, and
    undecided."""
    if not r["consistent"]:
        return {"CLASH"}
    if o == "O-MAKE-TOPO":
        cls = C.z3_class(r, "O-MAKE-TOPO", graded, "TOPO")
    elif o == "O-MAKE-DIST":
        cls = C._form_class(r, "O-MAKE-DIST", graded)[1]
    elif o == "O-LOOP":
        cls = C.z3_class(r, "O-LOOP", graded, "5")
    else:
        cls = C._form_class(r, o, graded)[1]
    own_paths = {k for k, ow in PATHWAY_OWNER.items() if ow & set(graded)}
    forms = ("O-LOOP-C", "O-LOOP-S") if o == "O-LOOP" else (o,)
    if any(set(r.get("defeasible", {}).get(f, [])) & own_paths for f in forms):
        cls = set(cls) | {"N", "OPEN"}
    return set(cls)


def guard_drift(scr, G=None, rows=DRIFT_ROWS):
    """Every DRIFT_ROWS row: anchor (the fragment occurs verbatim in the report), report class, z3 class, agreement."""
    G = G or report_grades()
    out = []
    cache = {}
    for rid, key, field, frag, o, variant, graded, note in rows:
        grade = next((g for g in (G.get(rid) or []) if key in g["key"]), None)
        anchored = grade is not None and frag in str(_field_text(grade, field, o))
        if o == "SEAT":
            if frag in SEAT_ALIAS:
                skey, sfrag = SEAT_ALIAS[frag]
                src = next((g for g in (G.get(rid) or []) if skey in g["key"]), None)
                anchored = anchored and src is not None and sfrag in str(src["seat"])
                rep = SEAT_PARSE(sfrag)
            else:
                rep = SEAT_PARSE(frag)
        elif o == "OWN":
            rep = "CLASH" if "FALSE-IF" in frag else None
        else:
            rep = C.parse_report_class(frag, variant)
        p = frozenset(variant)
        if p not in cache:
            cache[p] = scr.screen(set(p))
        r = cache[p]
        if o == "SEAT":
            zc = seat_class(r, graded)
        elif o == "OWN":
            zc = {"CLASH"} if not r["consistent"] else {"CONSISTENT"}
        else:
            zc = z3_class66(r, o, graded)
        agree = rep in zc
        out.append({"report": rid, "key": key, "obstruction": o, "fragment": frag, "variant": sorted(variant),
                    "anchored": anchored, "report_class": rep, "z3_class": sorted(zc), "agree": agree,
                    "explained": (not agree) and (rid, key, o) in EXPLAINED66, "note": note})
    return out


def drift_summary(rows):
    return {"rows": len(rows), "anchored": sum(r["anchored"] for r in rows), "agree": sum(r["agree"] for r in rows),
            "explained": [(r["report"], r["key"], r["obstruction"]) for r in rows if r["explained"]],
            "unexplained": [(r["report"], r["key"], r["obstruction"], r["report_class"], r["z3_class"])
                            for r in rows if not r["agree"] and not r["explained"]]}


MUTATIONS = ("defb-asserted", "negt-asserted", "gjw-ads", "qet-holds", "wall-loop", "qlit-free", "singok-a2")
#: wave 1's six were these with 'wall-clean' (the wall's pathway struck out); D66-fix replaced it by 'wall-loop' (a loop
#: asserted at the wall, against the computed time function) and added 'singok-a2' (wave 1's E-SINGOK against the
#: corrected reports: the drift guard must refuse it)


def drift_mutations(G=None):
    """Each mutated encoding must produce at least one UNEXPLAINED disagreement."""
    G = G or report_grades()
    out = {}
    for m in MUTATIONS:
        s = D66Screen(mutate=(m,))
        out[m] = drift_summary(guard_drift(s, G))["unexplained"]
    return out


# =====================================================================================================================
# CONTENT CHECKS (specific questions the combinations ask)
# =====================================================================================================================
def fkz_conditional(scr):
    """A1's seat sentence, as a conditional: with a string-supported throat HELD (its OPEN pathway N_NEGT true), the
    seat is free of a loop iff N_MBAL.  Returns (free with N_MBAL forced?, loop possible without it?)."""
    A = scr.A
    L = scr.lits({"DTHR"}) + scr._only_open("N_NEGT") + [A["HELD"]]
    free_with = not scr.sat(L + [A["N_MBAL"], A["SEATLOOP"]])
    loop_without = scr.sat(L + [z3.Not(A["N_MBAL"]), A["SEATLOOP"]])
    forced_without = not scr.sat(L + [z3.Not(A["N_MBAL"]), z3.Not(A["SEATLOOP"])])
    return {"seat free given N_MBAL": free_with, "seat loop possible without N_MBAL": loop_without,
            "seat loop FORCED without N_MBAL": forced_without}


def qlit_with_nonlinear(scr):
    """R-LIT's FALSE-IF is scoped to linear QM: alone it clashes; with W2 (a non-linear member) the encoding no longer
    refutes it -- consistency by absence of a refutation (nothing computes arrival-alone energy under W2), STRUCTURAL
    in what it shows, CONTENT in that the clash core names B66-ARR and B66-LIN."""
    r0 = scr.screen({"QLIT"})
    r1 = scr.screen({"QLIT", "W2"})
    r2 = scr.screen({"QLIT", "W2", "F1"})
    return {"QLIT alone consistent": r0["consistent"],
            "QLIT clash cores": [sorted(x for x in c if not x.startswith("Not(")) for c in r0.get("clash_cores", [])],
            "QLIT + W2 consistent": r1["consistent"], "QLIT + W2 + F1 consistent": r2["consistent"],
            "QLIT + W2 + F1 lifted, D66 load-bearing": d66_attributed(r2) if r2["consistent"] else None,
            "QLIT + W2 + F1, D66 literal in a support": r2.get("d66_load", {}).get("d66_in_support")}


def throat_interference(scr):
    """The geometric-throat readings against ITB: each makes N_QTOPO inadmissible (a premise clash), so ITB's
    non-bindings fall -- as R-QUANTUM's throat does in D68."""
    out = {}
    for k in ("DTHR", "TBHOLO", "TBTSH", "TBTEL"):
        r = scr.screen({k, "ITB"})
        out[k] = {"consistent": r["consistent"], "premise clashes": r.get("premise_clash_named"),
                  "O-HOLD": r["per"]["O-HOLD"]["verdict"] if r["consistent"] else None,
                  "O-MAKE-TOPO": r["per"]["O-MAKE-TOPO"]["verdict"] if r["consistent"] else None}
    r = scr.screen({"TBITB", "ITB"})
    out["TBITB (control: no throat commitment)"] = {"premise clashes": r.get("premise_clash_named"),
                                                     "O-HOLD": r["per"]["O-HOLD"]["verdict"]}
    return out


# =====================================================================================================================
# GROUNDS (each re-run from its owner, imported)
# =====================================================================================================================
def grounds(with_specthm=True):
    g = {}
    D = own("defects")
    zg = D.grades()
    g["defects.grades"] = zg
    tkk, sos, vfree = D.canonical_nec(1)
    tkk_p, sos_p, _ = D.canonical_nec(-1)
    g["canonical NEC (sum of squares) / phantom control"] = (bool(sos), bool(sos_p))
    st = D.static_is_stably_causal()
    g["static seats: g^tt"] = {k: str(v) for k, v in st.items()}
    g["derrick d=3 stationary / d=1 control"] = (D.derrick(3)[1], D.derrick(1)[1])
    TB = own("throatbits")
    pv = TB.pv_static()
    g["PV sigma_0 < 0 at every a_0 > 2M"] = pv["sigma0_negative_all"]
    g["PV conservation / flipped control"] = (TB.pv_conservation(False), TB.pv_conservation(True))
    if with_specthm:
        sv = TB.specthm_verdicts()
        g["specthm verdicts"] = {k: sv[k] for k in ("S-1", "S-2", "S-3", "Rec", "W-create-cc", "W-create-ncc",
                                                     "W-enlarge") if k in sv}
    Q = own("qet")
    m = Q.model(1.5, 1.0)
    g["QET arrival alone: local energy at B"] = Q.ev(Q.post_alice(m), m["HB"] + m["V"])
    mv = Q.minimal_values(1.5, 1.0)
    g["QET E_B, E_A at (h, k) = (1.5, 1), model units"] = (mv["E_B"], mv["E_A"])
    g["QET no-signalling"] = Q.no_signalling(m)
    GEO = own("geometry")
    g["geometry.r_quantum fraction (1 m)"] = GEO.r_quantum()["fraction_covered"]
    MF = own("massform")
    vals = MF.mechanism_values()
    v1 = dict(vals)
    v1["C1"] = True
    g["massform TEMPLATE: default / with C1's link holding"] = (MF.derive_readings(vals)["TEMPLATE"][0],
                                                               MF.derive_readings(v1)["TEMPLATE"][0])
    g["massform TEMPLATE counts"] = [c for n, _w, c in MF.READINGS if n == "TEMPLATE"][0]
    g["massform (TEMPLATE, C3) reason"] = MF.READING_REASONS[("TEMPLATE", "C3")]
    g["massform held-seat route forms baryons"] = MF.HELD_SEAT_ROUTE["forms baryons"]
    g["massform STABLE_RANGE"] = MF.STABLE_RANGE
    SE = own("seat")
    g["seat.grade_o_seat(board)"] = SE.grade_o_seat(SE.board_state())
    g["defects FKZ figure (yr, Earth shell, L = 1 ly)"] = D.figures()["FKZ T ~ R L c/(G M) yr, Earth shell, L = 1 ly"]
    # D66-fix grounds
    vt = D.vis_time_function()
    g["wall: T a global time function (both sides, continuous) / R control"] = (
        all(vt[x]["pullback_is_g"] and vt[x]["gTT"] == -1 for x in (1, -1)) and vt["continuous at z=0"],
        vt[1]["gRR"] == 1)
    sa, sj = D.monopole_conjugate()
    g["global monopole: Jacobi zero at the axis crossing / halved-curvature control"] = (
        sj is not None and abs(sj / sa - 1) < 1e-6, D.monopole_conjugate(k_scale=0.5)[1] is None)
    g["gauge monopole S-1 conditions (1e17 GeV) / 1e-27 kg control"] = (
        D.gauge_monopole_lens()["S-1 conditions hold"],
        D.gauge_monopole_lens(1e-27 * 2.99792458e8 ** 2 / 1.602176634e-10)["S-1 conditions hold"])
    mrow = [r for r in own("ledger").RULED_BY_M if r[0] == "M-S1A-P3"][0]
    mt = " ".join(str(x) for x in mrow)
    g["ledger M-S1A-P3: singular throat not disqualified, throat-creation classes stay OPEN"] = (
        "a singular throat is not" in mt and "the throat-creation classes stay OPEN" in mt)
    mm = TB.mmp_scales()
    g["MMP: binding = payload rest energy below l_P in every coupling / (5.31) without pi^(3/2)"] = (
        all(r["r_e_where_binding_equals_payload_m"] < mm["l_P_m"] for r in mm["by_coupling"]),
        abs(mm["CONTROL (5.31) without its pi^(3/2), ratio"] - 1) > 0.5,
        abs(mm["binding forms (5.31) vs (7.58), ratio"] - 1) < 1e-12)
    return g


def grounds_checks(g, scr):
    """(name, ok, control?) per ground."""
    out = []
    zg = g["defects.grades"]
    r_thr = scr.screen({"DTHR"})
    r_str = scr.screen({"DSTR"})
    out.append(("GROUND defects.grades O-HOLD outside H-CANONICAL = 'OPEN via N_NEGT', and the screen's DTHR O-HOLD is "
                "OPEN via exactly [N_NEGT]",
                zg["O-HOLD, defect as throat support, outside H-CANONICAL"] == "OPEN via N_NEGT" and
                r_thr["per"]["O-HOLD"]["verdict"] == "OPEN" and r_thr["per"]["O-HOLD"]["via"] == ["N_NEGT"], False))
    out.append(("GROUND defects.grades O-SEAT = 'OPEN via N_S5 | N_DEFB', and the screen's DSTR O-SEAT is OPEN via "
                "exactly {N_DEFB, N_S5}",
                zg["O-SEAT, defect at the seat"] == "OPEN via N_S5 | N_DEFB" and
                set(r_str["per"]["O-SEAT"]["via"]) == {"N_DEFB", "N_S5"}, False))
    out.append(("GROUND defects.grades: static seat PASSES and the screen's DSTR seat is SATISFIED with no defeat",
                zg["seat condition, static straight string / monopole"].startswith("PASSES") and
                r_str["seat"]["verdict"] == "SATISFIED" and not r_str["seat"].get("defeasible"), False))
    out.append(("GROUND canonical fields satisfy the NEC (T_kk a sum of squares; defects.canonical_nec) -- H-CANONICAL's "
                "content behind B-HELD's DTHR route needing N_NEGT", g["canonical NEC (sum of squares) / phantom control"][0],
                False))
    out.append(("GROUND CONTROL the phantom field is NOT a sum of squares (the NEC theorem can fail)",
                not g["canonical NEC (sum of squares) / phantom control"][1], True))
    out.append(("GROUND static string / monopole / RN-exterior seats: g^tt < 0 (defects.static_is_stably_causal)",
                all(v.startswith("-") for v in g["static seats: g^tt"].values()), False))
    out.append(("GROUND texture: Derrick, no stationary point in d = 3 (C-DTEX's ground)",
                g["derrick d=3 stationary / d=1 control"][0] is False, False))
    out.append(("GROUND CONTROL Derrick in d = 1 admits one (the Derrick test can fail)",
                g["derrick d=3 stationary / d=1 control"][1] is True, True))
    out.append(("GROUND PV thin shell: sigma_0 < 0 at every a_0 > 2M (throatbits.pv_static) -- the singular throat's hold "
                "needs negative surface energy (TBTSH's route needs N_PINCH)", g["PV sigma_0 < 0 at every a_0 > 2M"], False))
    out.append(("GROUND CONTROL PV conservation holds and fails with the M/a sign flipped",
                g["PV conservation / flipped control"] == (True, False), True))
    if "specthm verdicts" in g:
        out.append(("GROUND specthm W-create-ncc is OPEN at its owner (z3 at run time) -- N_WNCC is an OPEN pathway, "
                    "not a removal", g["specthm verdicts"].get("W-create-ncc") == "OPEN", False))
    out.append(("GROUND QET: the bit's arrival alone leaves local energy 0 at B (|.| < 1e-12; qet.post_alice) -- "
                "B66-ARR's ground", abs(g["QET arrival alone: local energy at B"]) < 1e-12, False))
    out.append(("GROUND CONTROL QET with the conditioned operation extracts E_B = 0.14252 > 0 at (h, k) = (1.5, 1), "
                "model units (A3 prints it '0.1425 h'; it is the raw model value, E_B/h = 0.0950) -- the arrival test "
                "can fail", abs(g["QET E_B, E_A at (h, k) = (1.5, 1), model units"][0] - 0.14252) < 5e-5, True))
    out.append(("GROUND QET no-signalling (B's reduced state moves < 1e-14): the bit is required, O-BITS LEFT",
                g["QET no-signalling"] < 1e-14, False))
    out.append(("GROUND geometry.r_quantum covers 2.08e-68 of the 1 m throat's deficit (QET's hold bound, A3)",
                abs(g["geometry.r_quantum fraction (1 m)"] / 2.081e-68 - 1) < 2e-3, False))
    out.append(("GROUND massform: TEMPLATE is REFUSED on C1 alone, and STANDS with C1's link holding "
                "(massform.derive_readings) -- at a defect core |phi| = 0 is held with no local source, so C1's "
                "P-UNIFORM ground fails there; the restoration half still fails by topology (A1 F8)",
                g["massform TEMPLATE: default / with C1's link holding"] == ("REFUSED", "STANDS") and
                tuple(g["massform TEMPLATE counts"]) == ("C1",), False))
    out.append(("GROUND massform: TEMPLATE makes no new baryon number (READING_REASONS) and the held-seat route forms no "
                "baryons -- so a defect-core TEMPLATE is not a supply of substance; DEF-SEAT's S10 / S13 stay refused",
                g["massform (TEMPLATE, C3) reason"][0] is False and "baryon" in g["massform (TEMPLATE, C3) reason"][1]
                and g["massform held-seat route forms baryons"] is False, False))
    out.append(("GROUND seat.grade_o_seat(board) = OPEN (the board's S5 route, unchanged)",
                g["seat.grade_o_seat(board)"] == "OPEN", False))
    # D66-fix
    r_wall = scr.screen({"DWALL"})
    out.append(("GROUND (D66-fix) the M4-M4 wall: Minkowski T is a global time function (defects.vis_time_function, CGS "
                "p.15 Fig.4) -- and the screen's DWALL seat is SATISFIED with no defeat, O-LOOP removed by the board "
                "with no defeat (N_WALLLOOP retired)",
                g["wall: T a global time function (both sides, continuous) / R control"][0] and
                r_wall["seat"]["verdict"] == "SATISFIED" and not r_wall["seat"].get("defeasible") and
                not r_wall.get("defeasible"), False))
    out.append(("GROUND CONTROL the radial coordinate R is not a time function (the wall test can fail)",
                g["wall: T a global time function (both sides, continuous) / R control"][1], True))
    out.append(("GROUND (D66-fix) the global monopole's axis recrossing is a conjugate point (defects.monopole_conjugate)",
                g["global monopole: Jacobi zero at the axis crossing / halved-curvature control"][0], False))
    out.append(("GROUND CONTROL a halved curvature misses the axis crossing (the conjugate-point test can fail)",
                g["global monopole: Jacobi zero at the axis crossing / halved-curvature control"][1], True))
    out.append(("GROUND (D66-fix) the gauge monopole at 1e17 GeV meets S-1's conditions through spec.focal_length "
                "(defects.gauge_monopole_lens)", g["gauge monopole S-1 conditions (1e17 GeV) / 1e-27 kg control"][0],
                False))
    out.append(("GROUND CONTROL a 1e-27 kg monopole fails them (the S-1 placement test can fail)",
                not g["gauge monopole S-1 conditions (1e17 GeV) / 1e-27 kg control"][1], True))
    out.append(("GROUND (D66-fix) ledger M-S1A-P3 carries M's ruling ('a singular throat is not disqualified'; 'the "
                "throat-creation classes stay OPEN'), and defects.grades gives a made string-supported throat 'OPEN via "
                "N_WNCC' -- the screen's DTHR O-MAKE-TOPO is OPEN via exactly [N_WNCC]",
                g["ledger M-S1A-P3: singular throat not disqualified, throat-creation classes stay OPEN"] and
                zg["O-MAKE-TOPO, defect-supported throat made from flat space"] == "OPEN via N_WNCC" and
                r_thr["per"]["O-MAKE-TOPO"]["verdict"] == "OPEN" and r_thr["per"]["O-MAKE-TOPO"]["via"] == ["N_WNCC"],
                False))
    mmg = g["MMP: binding = payload rest energy below l_P in every coupling / (5.31) without pi^(3/2)"]
    out.append(("GROUND (D66-fix) MMP 1807.04726: the binding energy equals the payload's rest energy only below l_P "
                "(throatbits.mmp_scales), and its two printed forms agree -- N_GJWPAY's ground", mmg[0] and mmg[2], False))
    out.append(("GROUND CONTROL (5.31) without its pi^(3/2) disagrees with (7.58) (the comparison can fail)", mmg[1], True))
    r_q = scr.screen({"QET"})
    out.append(("GROUND (D66-fix, V66-0 #7) QET alone: O-HOLD OPEN via exactly [N_QETHAD]; N_XI / N_QEIC appear only "
                "with RQ (the board's R-QUANTUM)", r_q["per"]["O-HOLD"]["verdict"] == "OPEN" and
                r_q["per"]["O-HOLD"]["via"] == ["N_QETHAD"], False))
    return out


# =====================================================================================================================
# RUN ALL
# =====================================================================================================================
def guard_readings(items_small):
    """Named readings run through the screen (not mutations: alternatives on record), on the D66 single readings x
    contexts and the context-only variants: which rows each moves."""
    out = {}
    base = run(C.CELL_MAIN, (), items_small)
    for m in ("seat-routes", "singok-board", "singok-a2", "fkz-generic", "qet-board-paths", "d68w2-topo"):
        R = run(C.CELL_MAIN, (m,), items_small)
        moved = []
        for r in R["rows"]:
            b = base["by"][frozenset(r["present"])]
            if not r["consistent"] or not b["consistent"]:
                if r["consistent"] != b["consistent"]:
                    moved.append((sorted(r["present"]), "consistency"))
                continue
            for o in C.OBST:
                x, y = r["per"][o], b["per"][o]
                if (x["verdict"], x.get("via"), r.get("defeasible", {}).get(o)) != \
                        (y["verdict"], y.get("via"), b.get("defeasible", {}).get(o)):
                    moved.append((sorted(r["present"]), o, x["verdict"], x.get("via"), y["verdict"], y.get("via")))
            if r["seat"] != b["seat"]:
                moved.append((sorted(r["present"]), "SEAT", r["seat"]["verdict"], b["seat"]["verdict"]))
        out[m] = {"variants": len(R["rows"]), "moved": moved}
    return out


def sm_only_census(scr_sm, items):
    n = inc = 0
    for combo, pick, ctx, p in items:
        if not set(pick) & set(DS4 + ("DTHR",)):
            continue
        n += 1
        inc += not scr_sm.sat(scr_sm.lits(set(p)))
    return {"variants with a string, wall, monopole or string-supported throat": n, "inconsistent under H-SM-ONLY": inc}


def run_all(with_specthm=True, conservative_step=24):
    t0 = time.time()
    out = {}
    out["conservative"] = conservative_extension(conservative_step)
    _set_vocab(True)
    items = variants66()
    out["untested"] = list(UNTESTED)
    out["n_variants"] = len(items)
    R = compare_to_context(run(C.CELL_MAIN, (), items))
    items_au = [it for it in items if {"W2", "F1"} <= set(it[3])]
    R_au = compare_to_context(run(C.CELL_AU, (), items_au))
    out["R"], out["R_au"] = R, R_au
    scr = D66Screen()
    out["vacuity"] = vacuity(scr)
    out["vacuity_open_false"] = {"1 ly": [sorted(r["present"]) for r in R["rows"] if r["consistent"]
                                          and not r["sat_open_false"]],
                                 "1 AU": [sorted(r["present"]) for r in R_au["rows"] if r["consistent"]
                                          and not r["sat_open_false"]]}
    sc = D66Screen(mutate=("open-forced",))
    rq = sc.screen({"QET"})
    out["vacuity_control"] = {"QET consistent": rq["consistent"], "sat_open_false": rq.get("sat_open_false"),
                              "O-HOLD verdict (vacuous if REMOVED)": rq["per"]["O-HOLD"]["verdict"]
                              if rq["consistent"] else None}
    rl = D66Screen(mutate=("defb-asserted",)).screen({"DSTR"})
    out["load_control"] = {"O-SEAT verdict": rl["per"]["O-SEAT"]["verdict"], "d66 load-bearing": d66_attributed(rl)}
    out["ties"] = pathway_ties(scr)
    G = report_grades()
    out["drift"] = guard_drift(scr, G)
    out["drift_summary"] = drift_summary(out["drift"])
    out["drift_mutations"] = drift_mutations(G)
    out["fkz"] = fkz_conditional(scr)
    out["qlit"] = qlit_with_nonlinear(scr)
    out["throat_interference"] = throat_interference(scr)
    small = [it for it in items if len(it[1]) <= 1]
    out["readings"] = guard_readings(small)
    out["sm_only"] = sm_only_census(D66Screen(mutate=("sm-only",)), items)
    out["grounds"] = grounds(with_specthm)
    out["grounds_checks"] = grounds_checks(out["grounds"], scr)
    for lab, RR in (("1 ly", R), ("1 AU", R_au)):
        out[lab] = {"clash": clash_census(RR), "survivors": survivors(RR), "removals": removal_census(RR),
                    "headline": headline(RR), "member_removals": member_removal_census(RR),
                    "seat": seat_census(RR), "by_combo": by_combo(RR), "pathways": pathway_census(RR),
                    "seconds": RR["seconds"]}
    out["structural"] = structural(scr)
    out["seconds"] = time.time() - t0
    return out


def structural(scr):
    """Items that cannot fail by construction: printed, not counted."""
    w = scr.widened
    return [
        "STRUCTURAL the widened terms are combine's own: B-HELD's held = %d chars, B-SIGLOOP's antecedent, DEF-SEAT's rhs, "
        "DEF-TOPO's rhs read from combine's expressions (asserted shape at build)" % len(str(w["B-HELD"][1])),
        "STRUCTURAL TBISL and TBITB are inert on every obstruction atom (their only content is the seat closure): any "
        "consistency they show is by construction",
        "STRUCTURAL R-LIT with W2 is consistent by the absence of a refutation: nothing computes arrival-alone energy "
        "under a non-linear dynamics",
        "STRUCTURAL OPEN pathways are held false in supports and accounts (combine's engine); every D66 OPEN pathway "
        "is tied to its owner literal, so no D66 literal can be credited a removal through one",
        "STRUCTURAL D66-fix: the wall supplies no loop by encoding (B66-WALL is empty outside the 'wall-loop' control); "
        "its CONTENT is defects.vis_time_function, re-run in the grounds",
        "STRUCTURAL the 1 AU, N = 1e3 / 1e6 and 4.2465 ly cells are board equalities (combine.cells_read_table); no D66 "
        "commitment names N_EPS or B-EPSWIN, so those cells add no D66 content",
    ]


# =====================================================================================================================
# REPORT
# =====================================================================================================================
def _j(o):
    if isinstance(o, (set, frozenset)):
        return sorted(o)
    if isinstance(o, tuple):
        return list(o)
    return str(o)


def report(out, path=None):
    P = print
    P("DOCKET 66 / B-combine66 -- the three D66 hypotheses in combination, with D68's bearing members\n")
    P("variants screened: %d at 1 ly, N = 7; %d at 1 AU, N = 7 (the W2 x F1 variants); %.0f s"
      % (len(out["R"]["rows"]), len(out["R_au"]["rows"]), out["seconds"]))
    P("conservative extension: %d D68 variants compared, %d differ" % (out["conservative"]["compared"],
                                                                     len(out["conservative"]["differ"])))
    for lab in ("1 ly", "1 AU"):
        d = out[lab]
        P("\n== %s ==" % lab)
        P("clashes:", json.dumps(d["clash"], indent=1, default=_j))
        P("member-attributed removals per account (any member):", json.dumps(d["member_removals"], default=_j))
        P("headline:", json.dumps(d["headline"], default=_j))
        P("lifted obstructions, by what:", json.dumps(d["removals"], indent=1, default=_j))
        P("survivors (lifted in no consistent D66 variant):", json.dumps(d["survivors"], indent=1, default=_j))
        P("seat condition census:", json.dumps(d["seat"], indent=1, default=_j))
        P("D66 pathways:", json.dumps(d["pathways"], indent=1, default=_j))
        P("by combination:", json.dumps(d["by_combo"], indent=1, default=_j))
    P("\ndrift:", json.dumps(out["drift_summary"], indent=1, default=_j))
    P("mutations caught:", {k: len(v) for k, v in out["drift_mutations"].items()})
    P("FKZ conditional:", out["fkz"])
    P("R-LIT:", json.dumps(out["qlit"], default=_j))
    P("throat interference with ITB:", json.dumps(out["throat_interference"], default=_j))
    P("readings under the guard:", {k: (v["variants"], len(v["moved"])) for k, v in out["readings"].items()})
    P("H-SM-ONLY:", out["sm_only"])
    P("untested:", len(out["untested"]))
    for s in out["structural"]:
        P(s)
    if path:
        slim = dict(out)
        for k in ("R", "R_au"):
            slim[k] = {"seconds": out[k]["seconds"], "rows": [
                {kk: r.get(kk) for kk in ("present", "readings", "context", "combo", "consistent", "clash_cores",
                                          "premise_clash_named", "seat", "defeasible", "d66_attributed", "d66_load",
                                          "interference", "new_open", "new_defeasible", "seat_change")}
                | ({"per": {o: {"verdict": v["verdict"], "via": v.get("via"),
                                "nb": (v.get("nb") or {}).get("verdict"),
                                "supports": [s["members"] + s["named"] for s in v.get("supports", [])]}
                            for o, v in r["per"].items()}} if r["consistent"] else {})
                for r in out[k]["rows"]]}
        with open(path, "w") as f:
            json.dump(slim, f, indent=1, default=_j)
        P("wrote", path)


# =====================================================================================================================
# SELFTEST
# =====================================================================================================================
def selftest(conservative_step=24, json_path=None):
    t0 = time.time()
    out = run_all(with_specthm=True, conservative_step=conservative_step)
    res = []

    def ck(name, cond, control=False):
        res.append((name, bool(cond), control))
        print(("PASS " if cond else "FAIL ") + ("[control] " if control else "") + name)

    R, Rau = out["R"], out["R_au"]
    ly, au = out["1 ly"], out["1 AU"]
    # -- vacuity
    v = out["vacuity"]
    ck("VACUITY board alone SAT (extended)", v["board alone SAT"])
    ck("VACUITY every D66 reading alone SAT except R-LIT (12 of 13)",
       all(s for k, s in v["singles SAT"].items() if k != "QLIT") and sum(v["singles SAT"].values()) == 12)
    ck("VACUITY D66 named premises jointly SAT with the board and with DTHR / TBHOLO / QET (OPEN false)",
       v["D66 named premises jointly SAT with the board (OPEN false)"] and
       v["D66 named premises jointly SAT with every D66 reading that names one (OPEN false)"])
    ck("VACUITY each D66 OPEN pathway can hold with its owner", all(v["each D66 pathway SAT with its owner"].values()))
    ck("VACUITY every consistent variant is SAT with every OPEN pathway false (1 ly and 1 AU): no vacuous removal",
       not out["vacuity_open_false"]["1 ly"] and not out["vacuity_open_false"]["1 AU"])
    vc = out["vacuity_control"]
    ck("CONTROL a reading consistent only through an OPEN pathway ('open-forced') trips the vacuity flag, and the engine "
       "then reports a vacuous REMOVED -- the guard is what stops it", vc["QET consistent"] and
       vc["sat_open_false"] is False and vc["O-HOLD verdict (vacuous if REMOVED)"] == "REMOVED", control=True)
    # -- conservative extension
    cons = out["conservative"]
    ck("GUARD conservative extension: %d D68 variants, combine (own vocabulary) and D66Screen (extended) give identical "
       "signatures and supports" % cons["compared"], cons["compared"] >= 300 and not cons["differ"])
    lc = out["load_control"]
    ck("CONTROL the load-bearing test can fail: a planted D66 removal ('defb-asserted', DSTR) reads REMOVED and is "
       "credited to the D66 literal", lc["O-SEAT verdict"] == "REMOVED" and lc["d66 load-bearing"] == ["O-SEAT"],
       control=True)
    # -- pathway ties
    for k, t in out["ties"].items():
        ck("CONTROL pathway tie %s: %s" % (k, {a: b for a, b in t.items() if a != "ok"}), t["ok"], control=True)
    # -- drift
    ds = out["drift_summary"]
    ck("DRIFT every fragment anchored verbatim in its A-report (%d of %d)" % (ds["anchored"], ds["rows"]),
       ds["anchored"] == ds["rows"])
    ck("DRIFT %d of %d comparisons agree; every disagreement explained (%d explained, 0 unexplained)"
       % (ds["agree"], ds["rows"], len(ds["explained"])), not ds["unexplained"] and len(ds["explained"]) == 2)
    for m, un in out["drift_mutations"].items():
        ck("CONTROL mutation '%s' caught by the drift guard (%d unexplained rows)" % (m, len(un)), len(un) >= 1,
           control=True)
    # -- content
    f = out["fkz"]
    ck("CONTENT A1's FKZ conditional: with the string-supported throat held, the seat is free given N_MBAL and a loop is "
       "FORCED without it", f["seat free given N_MBAL"] and f["seat loop FORCED without N_MBAL"])
    q = out["qlit"]
    ck("CONTENT R-LIT alone is inconsistent, its core naming C-QLIT, B66-ARR and B66-LIN",
       (not q["QLIT alone consistent"]) and any({"@C-QLIT", "@B66-ARR", "@B66-LIN"} <= set(c) for c in q["QLIT clash cores"]))
    ck("CONTENT R-LIT with W2 is not refuted by the encoding; with W2 x F1 R-LIT appears in an O-BITS support only by "
       "entailing W2 (B66-LIN), and is load-bearing in none",
       q["QLIT + W2 consistent"] and q["QLIT + W2 + F1 consistent"] and
       q["QLIT + W2 + F1 lifted, D66 load-bearing"] == [] and "O-BITS:R" in q["QLIT + W2 + F1, D66 literal in a support"])
    ti = out["throat_interference"]
    ck("CONTENT each geometric-throat reading (DTHR, TBHOLO, TBTSH, TBTEL) with ITB makes {N_QTOPO} a premise clash and "
       "O-HOLD stops being NOT-BOUND-IF",
       all(("N_QTOPO",) in [tuple(p) for p in ti[k]["premise clashes"]] and ti[k]["O-HOLD"] != "NOT-BOUND-IF"
           for k in ("DTHR", "TBHOLO", "TBTSH", "TBTEL")))
    ck("CONTROL R-ITB (no throat commitment) with ITB keeps O-HOLD NOT-BOUND-IF and has no {N_QTOPO}-alone premise "
       "clash (only D68's own {N_CORR, N_QTOPO})",
       ti["TBITB (control: no throat commitment)"]["O-HOLD"] == "NOT-BOUND-IF" and
       ("N_QTOPO",) not in [tuple(p) for p in ti["TBITB (control: no throat commitment)"]["premise clashes"]],
       control=True)
    # -- results
    for lab, d in (("1 ly", ly), ("1 AU", au)):
        hl = d["headline"]
        ck("RESULT %s: no D66 literal is load-bearing in any support of any removal or non-binding (0 in %d "
           "consistent variants)" % (lab, d["clash"]["consistent"]),
           hl["d66_removed"][0] == 0 and hl["d66_nb"][0] == 0 and
           all(x["D66 literal load-bearing"] == 0 for x in d["removals"].values()))
        ck("RESULT %s: member-attributed removals per account at most 1, and it is O-BITS by {W2, F1}" % lab,
           d["member_removals"]["max_member_removals_per_account"] == 1 and
           all(k.startswith("O-BITS by") and "W2" in k and "F1" in k for k in d["member_removals"]["what"]))
        ck("RESULT %s: O-SEAT survives every consistent D66 variant (lifted in none)" % lab, "O-SEAT" in d["survivors"])
        ck("RESULT %s: O-MAKE-DIST survives every consistent D66 variant" % lab, "O-MAKE-DIST" in d["survivors"])
    ck("RESULT 1 ly: O-SEAT reads OPEN via {N_DEFB, N_S5} in exactly the consistent variants holding a string, wall or "
       "monopole, and OPEN via N_S5 alone in every other",
       all((set(r["per"]["O-SEAT"].get("via", [])) == ({"N_DEFB", "N_S5"} if set(r["present"]) & set(DS4) else {"N_S5"}))
           and r["per"]["O-SEAT"]["verdict"] == "OPEN" for r in R["rows"] if r["consistent"]))
    ck("RESULT 1 ly: O-HOLD is removed in no consistent variant; where it is lifted it is NOT-BOUND-IF, every support "
       "carrying ITB (D68's), never a D66 literal",
       all(r["per"]["O-HOLD"]["verdict"] not in C.RMV for r in R["rows"] if r["consistent"]) and
       all(set().union(*[set(s["members"]) for s in C._sups_with(r["per"]["O-HOLD"], C.NBV)]) <= {"ITB"}
           for r in R["rows"] if r["consistent"] and r["per"]["O-HOLD"]["verdict"] in C.NBV))
    ck("RESULT readings: H-SEAT-ROUTES moves O-SEAT to LEFT in every consistent single-reading variant (DEFB excluded "
       "with S5); singok-a2 (wave 1's encoding, on D68 wave 2's DEF-TOPO) moves only O-MAKE-TOPO, to LEFT; "
       "fkz-generic only defeasibility; qet-board-paths (wave 1's QET "
       "gating) only O-HOLD's via list, never its verdict.  (D66-fix also required singok-board to move only "
       "O-MAKE-TOPO, to OPEN via N_WNCC, in variants holding no D66 throat; it is now D68's own encoding and is checked "
       "below with d68w2-topo)",
       all(m[1] == "O-SEAT" and m[2] == "LEFT" for m in out["readings"]["seat-routes"]["moved"] if m[1] != "consistency")
       and all(m[1] in ("O-MAKE-TOPO",) and m[2] == "LEFT" for m in out["readings"]["singok-a2"]["moved"])
       and all(m[1] in ("O-LOOP-S", "SEAT") for m in out["readings"]["fkz-generic"]["moved"])
       and all(m[1] == "O-HOLD" and m[2] == m[4] for m in out["readings"]["qet-board-paths"]["moved"]))
    # D66-RULINGS (M-RULINGS item 28): combine.py carries the ruling, so 'singok-board' is the board's own encoding, and
    # D68 wave 2's encoding ('d68w2-topo', combine's history mutation) moves back exactly what 'singok-board' moved at
    # D66-fix: 174 single-reading/context variants, 20 of them context-only, each O-MAKE-TOPO OPEN via N_WNCC -> LEFT
    hw = out["readings"]["d68w2-topo"]["moved"]
    ck("RESULT readings (D66-RULINGS, M-RULINGS item 28: 'Re-grade D68 (Recommended)'): singok-board moves NOTHING (it is "
       "now docket68/combine.py's own DEF-TOPO); the history encoding d68w2-topo (D68 wave 2) moves only O-MAKE-TOPO, "
       "OPEN via [N_WNCC] -> LEFT, never in a variant holding a D66 throat, in exactly the 174 variants (20 context-only) "
       "singok-board moved at D66-fix",
       out["readings"]["singok-board"]["moved"] == [] and
       all(m[1] == "O-MAKE-TOPO" and m[2] == "LEFT" and m[4] == "OPEN" and m[5] == ["N_WNCC"] and
           not set(m[0]) & set(D66_THROATS) for m in hw) and
       len(hw) == 174 and sum(1 for m in hw if not set(m[0]) & set(D66_LITS)) == 20)
    ck("CONTROL the readings census can fail: singok-a2 (wave 1's encoding) moves O-MAKE-TOPO in variants holding DTHR "
       "or TBTEL, which d68w2-topo never moves",
       any(set(m[0]) & {"DTHR", "TBTEL"} for m in out["readings"]["singok-a2"]["moved"]), control=True)
    sm = out["sm_only"]
    ck("RESULT H-SM-ONLY: every variant with a string, wall, monopole or string-supported throat is inconsistent (%d)"
       % sm["inconsistent under H-SM-ONLY"],
       sm["inconsistent under H-SM-ONLY"] == sm["variants with a string, wall, monopole or string-supported throat"])
    # -- grounds
    for name, ok, ctl in out["grounds_checks"]:
        ck(name, ok, control=ctl)
    for s in out["structural"]:
        print("     " + s)
    n = len(res)
    npass = sum(1 for _, ok, _ in res if ok)
    nctl = sum(1 for _, _, c in res if c)
    print("\n%d counted checks, %d passed, %d failed; %d controls; %d STRUCTURAL items printed, not counted; %.0f s"
          % (n, npass, n - npass, nctl, len(out["structural"]), time.time() - t0))
    if json_path:
        report(out, json_path)
    return npass == n, out


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--selftest" in a:
        jp = a[a.index("--json") + 1] if "--json" in a else None
        ok, _ = selftest(json_path=jp)
        sys.exit(0 if ok else 1)
    if "--conservative-full" in a:
        r = conservative_extension(step=1)
        print(json.dumps({"compared": r["compared"], "differ": r["differ"], "seconds": r["seconds"]}, default=_j))
        sys.exit(0 if not r["differ"] else 1)
    out = run_all()
    report(out, a[a.index("--json") + 1] if "--json" in a else None)
