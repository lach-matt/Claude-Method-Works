#!/usr/bin/env python3
"""
DOCKET 68 / B-combine -- M's standing instruction, run: "some of the hypothesies lined up for docket 68 may turn out,
after initial testing, to work better in combination."  (CHARTER.md, verbatim.)

WAVE 2 (repair after three adversarial verifications, 2026-10-03).  What changed, and what wave 1 first said, is
recorded in B-combine.md section 0; the principle the repair runs on is stated once here:

  A THEOREM THAT DOES NOT BIND A NON-GEOMETRIC CORRIDOR MAKES THE OBSTRUCTION NOT-BOUND-IF (ITS PREMISE NAMED), NEVER
  REMOVED.  Showing a theorem does not apply is not showing its conclusion false.  Applied symmetrically: to
  O-MAKE-TOPO (Geroch/Tipler) and to O-HOLD's geometric NEC/throat form (Morris-Thorne), under H-IT read as an
  information layer (ITB, premise N_QTOPO), under ER=EPR (ITE, premise N_MS17), and under R-INDEX with H-IT (premise
  N_MEASPHYS; A3's only-if direction kept: without H-IT, R-INDEX releases nothing).  A NOT-BOUND obstruction is not
  removed: what the non-geometric corridor costs to make or hold is a separate question, carried as the OPEN pathway
  N_ILFREE (no source supplies it).

WHAT THIS FILE DOES
  (1) builds the 127 non-empty combinations of the seven hypotheses.  Hypotheses with more than one reading are carried
      in EVERY reading: H-SETTLE W2 / W1 / KR; H-FRAME F1 / F2b / F1+F2b; H-IT ITB / ITE; H-INFO INFO (necessity) /
      INFOS (sufficiency, A3's H-INFO-S).  Each runs with the four reading slots {none, R-INDEX, R-QUANTUM, both}:
      (4*4*3*3*2*2*2 - 1)*4 + 3 = 4,607 variants, all screened.
  (2) SCREENS each variant in z3 against the board holdings the four A-reports cite, at DISTANCE CELLS (N_EPS is tied
      to L and N through settle.eps_any_advantage and the NAMED-NOT-READ Weinberg-family limit; wave 1's N_EPS was a
      free boolean, true at 1 AU where the window is empty).  Every holding and commitment is a TRACKED constraint
      carrying its ground.  An inconsistent variant is named by EVERY minimal unsat core (wave 1 reported the one core
      z3 happened to return); a set of named premises inconsistent with a variant is a PREMISE CLASH, enumerated the
      same way.
  (3) per obstruction, the verdict, with EVERY minimal support (members, closed-world absences, named premises):
        REMOVED        forced by the variant's commitments with no named premise
        REMOVED-IF     forced once the named premises of a support are assumed (supports drawn only from premise sets
                       consistent with the variant, so no conditional removal is vacuous -- STRUCTURAL in this engine;
                       control: the wave-1 engine, which assumed every premise at once, is shown to report vacuous
                       removals at the 1 AU cell)
        NOT-BOUND-IF   the obstruction's theorem is forced not to bind (its premise -- a geometric corridor -- fails)
                       once the named premises of a support are assumed; NOT a removal; the removal's own status
                       (OPEN via N_ILFREE, ...) is reported beside it
        OPEN           possible only through an OPEN pathway the sources leave undecided
        SILENT         not forced either way, without any OPEN pathway
        LEFT           the obstruction stands in every model
  (4) GUARDS.  Vacuity (with every guard that cannot fail labelled STRUCTURAL and not counted as evidence); encoding
      drift: z3's per-obstruction verdict COMPARED WITH THE A-REPORTS' OWN GRADE TEXT, parsed from their JSON, with the
      agreement count reported and every disagreement listed with its reason (wave 1 compared z3 with hand-written
      expectations and agreed 17 of 17; with the reports it agreed 12 of 17); two mutated encodings must each be
      CAUGHT as an unexplained disagreement.
  (5) the complementary combinations TESTED with the members' own instruments (imported), the tests' timing and
      capacity figures being nlcontrol's single Hamiltonian's (H-NLCONTROL-FORM) and the W2 class's capacity OPEN
      beyond A1's computed floor.
  (6) every variant not tested by instrument, with its reason.  No cap.

M's hypotheses are carried as hypotheses, never as results.  Nothing here is seated.  Writes nothing outside
docket68/ except output paths the caller names.

    python3 combine.py --selftest            guards, grounds, screen, tests -- exits 1 on any failure
    python3 combine.py                       the report
    python3 combine.py --json PATH           the full variant table as JSON
    python3 combine.py --table PATH          the 127-combination markdown table (B-combine.md section 6)
"""
import contextlib
import io
import itertools
import json
import math
import os
import re
import sys
import time
from fractions import Fraction as Fr

import z3

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.join(HERE, "..")
sys.path.insert(0, HERE)
sys.path.insert(0, WD)
SCRATCH_REPORTS = ("/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/"
                   "scratchpad/d68")

_IMPORT_LOG = {}


def _quiet(modname):
    """Import a sibling instrument without letting its top-level prints through (several print at import)."""
    if modname in sys.modules:
        return sys.modules[modname]
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        mod = __import__(modname)
    _IMPORT_LOG[modname] = len(buf.getvalue())
    return mod


# =====================================================================================================================
# VOCABULARY
# =====================================================================================================================
HYPS = ["H-IT", "H-SETTLE", "H-FRAME", "H-12", "H-INFO", "H-ZERO", "H-NULL"]     # the charter's seven

SUBREADINGS = {
    "H-SETTLE": {
        "W2": "deterministic drift acting on Bob's per-BRANCH pure state (convention C2 = A1's H-C2; Weinberg/Gisin "
              "type) -- A1 H-SETTLE-W.  M's definition does not say which state the drift acts on: C2 is a named "
              "hypothesis, not M's words",
        "W1": "the same drift acting on Bob's REDUCED state (convention C1): no signal (frame.settle_under_C1 "
              "2.2e-16) -- A1, A2",
        "KR": "causal field-expectation-value form (Kaplan-Rajendran 2106.10576v2) -- A1 H-SETTLE-KR",
    },
    "H-FRAME": {
        "F1": "clause 1: a preferred frame exists (M's words).  Keying every corridor to it is NOT in M's sentence: it "
              "is the docket's H-KEYING, carried as the named premise N_KEYING -- A2 wave 2",
        "F2b": "clause 2b: messages reach the past of the cosmic clock -- A2",
        "F1+F2b": "both clauses together.  Consistent as commitments; excluded only under the docket's keying "
                  "(N_KEYING) or exact FRW (N_FRW), with corridors the only route to the cosmic past (N_2BVIA) -- a "
                  "PREMISE clash, not 'M's sentence contradicts itself' (wave 1's wording)",
    },
    "H-IT": {
        "ITB": "spacetime comes from information; the corridor lives in an information layer (the charter's reading of "
               "M's 'only to an observer').  No READ realisation: ITB commits to nothing unconditionally, so any "
               "consistency it shows is by construction -- A4",
        "ITE": "spacetime from information read as ER=EPR, with Maldacena-Susskind's own stated assumptions (fn.1 p.2 "
               "non-traversability; sec.3.1 p.16; sec.5.4 pp.36-37 linearity) -- A4",
    },
    "H-12": {"H12": "the twelve parameters of the 12-vector as carriers -- A1; content: an unbounded carrier (alpha_s, "
                    "G, v) frees N_EPS from the transferred spin bound, under N_H12W"},
    "H-INFO": {
        "INFO": "necessity: matter cannot exist without information -- A3 (no screen content: UNTESTED-BY-SCREEN)",
        "INFOS": "sufficiency (A3's H-INFO-S): information at the destination suffices to constitute the matter "
                 "('Cosmic/quantum information is all that matters'; 'only the information defining it is "
                 "necessary') -- commits: no holder need already be there",
    },
    "H-ZERO": {"ZERO": "zero = ground state -- A4; content only through N_EQUIL with H-IT (EGJ)"},
    "H-NULL": {"NULL": "null (NEC) is a containment where information lives -- A4; content only through N_EQUIL with "
                       "H-IT"},
}
READINGS = {"RI": "R-INDEX: probability of a cell in the closed index, measured by Q-1 (no energy term) -- A3; "
                  "physical content only with H-IT and N_MEASPHYS",
            "RQ": "R-QUANTUM: QEI-bounded negative energy holds a geometric throat -- A4"}
READING_SLOTS = [(), ("RI",), ("RQ",), ("RI", "RQ")]

OBST = ["O-BITS", "O-MAKE-TOPO", "O-MAKE-DIST", "O-HOLD", "O-MATTER", "O-LOOP"]
FIVE = ["O-BITS", "O-MAKE", "O-HOLD", "O-MATTER", "O-LOOP"]
NB_OBST = ("O-MAKE-TOPO", "O-HOLD")          # the two whose theorem has a geometric premise that can fail
RMV = ("REMOVED", "REMOVED-IF")
NBV = ("NOT-BOUND", "NOT-BOUND-IF")

# named premises a removal or a non-binding may rest on (assumed only inside a support; every support listed)
NAMED = {
    "N_EPS": "eps > eps_any_advantage(L, N) for nlcontrol's Hamiltonian (H-NLCONTROL-FORM; N pairs per teleported "
             "qubit), with eps not excluded by the Weinberg-family limit (NAMED-NOT-READ; an upper limit consistent "
             "with zero) -- with A1's H-MAP, H-TRANSFER, H-SPIN, H-COHERE.  Tied to the distance cell (B-EPSWIN)",
    "N_FRAME3b": "H-FRAME3b: a preferred slicing orders the drift's branching (Gisin's assumption 3b, 2412.20854v1 "
                 "p.6, READ by A1) -- the substance of H-FRAME clause 1, assumed by H-SETTLE when H-FRAME is absent",
    "N_SIGKEY": "the superluminal signal is keyed to the preferred slicing (A1 H-SIG-COR; A2 antitelephone)",
    "N_CORR": "H-CORRIDOR-MODEL: a corridor is an identification of positions by a translation (latticectc H1-H3; "
              "comoving translations in FRW)",
    "N_KEYING": "H-KEYING: every corridor is keyed to the preferred frame (xi_t = 0) -- the docket's modelling "
                "addition to clause 1, not M's words (A2 wave 2)",
    "N_FRW": "H-FRW-EXACT + H-NOT-DE-SITTER: the universe is exactly spatially flat FRW with non-exponential a(t), so "
             "only equal-cosmic-time identifications are isometries (frame.frw_time_function_lemma, z3) -- the "
             "keying forced by the geometry, in every variant (A2 wave 2; perturbations break even the translations)",
    "N_2BVIA": "H-2B-VIA-CORRIDOR: corridors are the only route to the cosmic past (A2), so a message into it means "
               "an unkeyed corridor",
    "N_QTOPO": "the ITB corridor is not a classical Lorentzian object (the charter's reading 'with no throat it does "
               "not apply'; NO READ source) -- the premise under which Geroch/Tipler and Morris-Thorne do not bind",
    "N_MS17": "MS 1306.0533v2 p.17 (READ): non-trivial topologies 'should be allowed as possible quantum states' -- "
              "under H-ER=EPR, for a NON-traversable bridge only (MS fn.1), Planckian for particle pairs (p.17)",
    "N_MEASPHYS": "H-MEASURE-PHYSICAL: under H-IT, the measure-level absence of an NEC is physical (A3 wave 2; no "
                  "instrument or READ source supplies it)",
    "N_H12W": "H-12-CARRIER + H-12-W: Bob's carrier is alpha_s, G or v, drifting in Weinberg (per-branch) form; no "
              "READ bound of any kind and no READ model of such a drift (A1 wave 2)",
}
# OPEN pathways: the sources leave them undecided; never assumed true in a removal
OPEN_NAMED = {
    "N_XI": "a nonminimally coupled (xi > 0) field has no state-independent QEI (Fewster-Osterbrink, board "
            "NARROWED) -- R-QUANTUM's open branch",
    "N_EPSG": "a gravitational KR nonlinearity supplies an NEC-violating effective source (KR p.13; eps_G "
              "unconstrained, KR p.14) -- H-SETTLE-KR's open branch",
    "N_VAC": "pre-existing entanglement (of the vacuum) usable as the channel's pairs with no distribution -- the "
             "closest reading of M's 'it already exists everywhere'.  READ, Reznik quant-ph/0212044v2: causally "
             "disconnected probes can end entangled (p.1); it 'vanishes once the regions become sufficiently "
             "separated' (p.1); p.10: the probes are switched on for T < L/c (causally disconnected); p.12 Fig.2 "
             "(T = 1, Omega = 9.5, one window function): entangled for L/T < 1.1.  DERIVED-FROM-READ: "
             "0.91 L/c < T < L/c, for that window and that gap only.  Whether any setup supplies the pairs a qubit "
             "needs faster than distribution is NOT computed: OPEN",
    "N_EQUIL": "H-EQUIL relaxed: Eling-Guedens-Jacobson gr-qc/0602001v1 eq.(21) p.3 (READ) out of local equilibrium; "
               "geometry.egj_fR_throat: T_kk(r0) >= 0 iff beta <= -r0^2/2 (1.9e69 l_P^2 at 1 m vs EGJ's beta ~ "
               "l_P^2), and r^4 T_kk -> -2 r0^2 for every beta (b = r0^2/r, f = 1 + beta R) -- H-IT with H-ZERO or "
               "H-NULL (A4 wave 2): a pathway, neither excluded nor shown",
    "N_ILFREE": "whatever carries a non-geometric corridor charges nothing to make or hold it -- the charter: 'its "
                "cost is then whatever the information layer charges -- this docket's question'.  No source",
}

LIT_NAMES = ["W2", "W1", "KR", "F1", "F2b", "ITB", "ITE", "H12", "INFO", "INFOS", "ZERO", "NULL", "RI", "RQ"]
PHYS = ["SIG", "LIN", "FRAME", "SIGKEY", "KEYED", "PAST", "LOOP", "GTOPO", "DIST", "THROAT", "HELD", "ILFREE", "RECV",
        "CAP"]
RM = {o: "rm:" + o for o in OBST}
NB = {o: "nb:" + o for o in NB_OBST}
LIT_OF = {lit: h for h, rd in SUBREADINGS.items() for k in rd for lit in k.split("+")}
LIT_OF.update({"RI": "R-INDEX", "RQ": "R-QUANTUM"})

# Inert by construction: commitments recorded for completeness that touch no obstruction atom.  A literal whose every
# commitment is inert is UNTESTED-BY-SCREEN; the difference census (exercised()) measures this rather than asserting it.
INERT = {
    "INFO": "A3: Q-1 delivered (BFL 1106.1791v3 Thm 2); 'matter cannot exist without information' is consistent with "
            "B-RECV (a holder with E > 0 holds the bits) and decides nothing the screen encodes",
}

# Distance cells: (label, L in metres, N pairs per qubit).  The transferred-bound window is COMPUTED per cell.
CELLS = {"1 ly, N = 7": ("LY_M", 1.0, 7), "1 AU, N = 7": ("AU_M", 1.0, 7)}
CELL_MAIN, CELL_AU = "1 ly, N = 7", "1 AU, N = 7"


def atoms():
    A = {n: z3.Bool(n) for n in LIT_NAMES + PHYS + list(NAMED) + list(OPEN_NAMED)}
    A.update({RM[o]: z3.Bool(RM[o]) for o in OBST})
    A.update({NB[o]: z3.Bool(NB[o]) for o in NB_OBST})
    return A


# =====================================================================================================================
# THE eps WINDOW PER CELL (z3 over the reals) -- feeds B-EPSWIN
# =====================================================================================================================
def eps_window(L_list=None, N_list=(7, 1000, 1e6)):
    """Is eps_any(L, N) < eps <= eps_max(reading) satisfiable?  eps_any from settle.eps_any_advantage (the infimum eps at
    which N pairs carry 2 bits with drift time T < L/c; wave 1 used settle.eps_to_remove at the DECLARED T = L/2c, which
    is exactly twice it); eps_max from settle's Majumder figure (NAMED-NOT-READ) under both H-MAP readings.  The wave-1
    figure is reported beside it, labelled DECLARED-FRAC.  Exact rationals of the doubles: no parse drift.  Returns
    rows and the vacuity check (eps > 0 alone satisfiable)."""
    ST = _quiet("settle")
    f = ST.BOUNDS_WEINBERG["Majumder+ 1990, 201Hg, PRL 65 2931"]["f_Hz"]
    L_list = L_list or (("1 AU", ST.AU_M), ("1 ly", ST.LY_M), ("4.24 ly", 4.24 * ST.LY_M))
    out = []
    for lab, emax in ST.eps_readings(f).items():
        for Ln, L in L_list:
            for N in N_list:
                eany = ST.eps_any_advantage(L, N)
                ehalf = ST.eps_to_remove(L, N)
                e = z3.Real("eps")
                s = z3.Solver()
                s.add(e > z3.RealVal(str(Fr(eany))), e <= z3.RealVal(str(Fr(emax))))
                s2 = z3.Solver()
                s2.add(e >= z3.RealVal(str(Fr(ehalf))), e <= z3.RealVal(str(Fr(emax))))
                out.append({"reading": lab, "L": Ln, "N": N, "eps_any_advantage": eany, "eps_max": emax,
                            "consistent": s.check() == z3.sat, "eps_at_T=L/2c (DECLARED-FRAC, wave 1)": ehalf,
                            "consistent_at_T=L/2c (wave 1)": s2.check() == z3.sat})
    s = z3.Solver(); e = z3.Real("eps"); s.add(e > 0)
    return out, s.check() == z3.sat


_WIN_CACHE = {}


def cell_window_open(cell):
    """True iff the transferred-bound window is non-empty at this cell under BOTH H-MAP readings; False iff empty under
    both.  A cell where the readings disagree is refused (it would make B-EPSWIN depend on H-MAP)."""
    if cell in _WIN_CACHE:
        return _WIN_CACHE[cell]
    ST = _quiet("settle")
    attr, mult, N = CELLS[cell]
    L = getattr(ST, attr) * mult
    lab = "1 ly" if attr == "LY_M" else "1 AU"
    rows, _ = eps_window(L_list=((lab, L),), N_list=(N,))
    vals = {r["consistent"] for r in rows}
    if len(vals) != 1:
        raise ValueError(f"cell {cell}: the H-MAP readings disagree -- refused")
    _WIN_CACHE[cell] = vals.pop()
    return _WIN_CACHE[cell]


# =====================================================================================================================
# THE BOARD'S HOLDINGS, as tracked constraints.  Each: (name, ground, expression).  ground_checks() re-runs every
# computed ground from its instrument.
# =====================================================================================================================
def _board(A, win_open, mutate=()):
    I, An, Or, N, Eq = z3.Implies, z3.And, z3.Or, z3.Not, (lambda a, b: a == b)
    rel_topo = Or(An(A["ITB"], A["N_QTOPO"]), An(A["ITE"], A["N_MS17"]), An(A["ITB"], A["RI"], A["N_MEASPHYS"]))
    rel_throat = Or(An(A["ITB"], A["N_QTOPO"]), An(A["ITB"], A["RI"], A["N_MEASPHYS"]))
    if "wave1-THROAT" in mutate:          # CONTROL: wave 1's B-THROAT, H-IT read as SUFFICIENT with R-INDEX
        rel_throat = Or(rel_throat, An(A["ITB"], A["RI"]))
    held = Or(An(A["RQ"], A["N_XI"]), An(A["KR"], A["N_EPSG"]),
              An(Or(A["ITB"], A["ITE"]), Or(A["ZERO"], A["NULL"]), A["N_EQUIL"]))
    if "KR-unconditional" in mutate:      # CONTROL: KR holds the throat with no OPEN branch
        held = Or(held, A["KR"])
    return [
        ("B-NOCOM", "no-communication theorem (board D67 NARROWED): nosig.py I = 0.0 bits over 7 angles; fields12.py "
                    "1.44e-15; frame.settle_under_C1 2.2e-16 (the drift on the reduced state, C1); settle.py "
                    "collapse control; KR 2106.10576v2 sec.2.3 (DERIVED-FROM-READ, A1): only a per-branch "
                    "deterministic drift signals among the readings screened",
         I(A["SIG"], A["W2"])),
        ("B-GISIN", "settle.bob_y_exact: Bob's <sigma_y> = tanh(2 eps T) under H-C2 (sympy residual 0); Gisin "
                    "READ-VIA-RESTATEMENT 2412.20854v1 pp.5-7, which covers maps on PURE states only (p.7)",
         I(An(A["W2"], A["FRAME"]), A["SIG"])),
        ("B-C2-SLICE", "frame.drift_ordering (wave 2, COMPUTED for the drift, not the D-CTC): Bob's signal is "
                       "tanh(2 eps (T - t_A)) = 0.537 / 0.291 / 0 as Alice measures before / mid / after his window, "
                       "so a C2 signal is defined only relative to a slicing.  Wave 1 grounded this on the D-CTC "
                       "circuit (1/2 vs 2/3), which needs a CTC at Bob and is withdrawn as a ground",
         I(A["SIG"], A["FRAME"])),
        ("B-FRAME", "encoding: a preferred frame/slicing is asserted only by H-FRAME (either clause, C-F1 / C-F2b) or "
                    "by H-FRAME3b",
         An(I(A["FRAME"], Or(A["F1"], A["F2b"], A["N_FRAME3b"])), I(A["N_FRAME3b"], A["FRAME"]))),
        ("B-PAST", "encoding: a message into the past of the cosmic clock is asserted only by clause 2b",
         I(A["PAST"], A["F2b"])),
        ("B-SIGKEY", "A1 H-SIG-COR; A2 antitelephone: a signal keyed to one slicing needs that slicing",
         An(I(An(A["FRAME"], A["N_SIGKEY"]), A["SIGKEY"]), I(A["SIGKEY"], A["FRAME"]))),
        ("B-ANTITEL", "frame.antitelephone via frame.reply_arrival (sympy, both values computed): a reply keyed to the "
                      "sender's frame arrives at t = -3/5 (a closed loop); keyed to the cosmic frame, 0",
         I(An(A["SIG"], N(A["SIGKEY"])), A["LOOP"])),
        ("B-KEYING", "corridors.py 0/2000 one-frame pairs close; frame.cosmic_keyed_rank_n_is_safe (Sylvester, any "
                     "rank): corridors keyed to one frame -- under the docket's H-KEYING",
         I(An(A["F1"], A["N_KEYING"]), A["KEYED"])),
        ("B-FRW", "frame.frw_time_function_lemma (z3 unsat for any a(t) > 0; control a >= 0 sat): in exact flat FRW "
                  "cosmic time is a global time function and only equal-cosmic-time identifications are isometries "
                  "(frw_killing_table) -- the keying FORCED by the geometry, not by H-FRAME",
         I(A["N_FRW"], A["KEYED"])),
        ("B-TIMEFUNC", "frame.cosmic_keyed_rank_n_is_safe (exact Sylvester, 0 failures at rank 2 and 3); "
                       "frame.frw_time_function_lemma; corridors.py 0/2000",
         I(An(A["KEYED"], A["N_CORR"], N(A["PAST"]), Or(N(A["SIG"]), A["SIGKEY"])), N(A["LOOP"]))),
        ("B-2B", "frame.py part (i).3: a message into the cosmic past through a corridor <=> xi_t != 0 <=> not keyed "
                 "(past_corridor_witness norm -99/10000) -- binding only if corridors are the route (H-2B-VIA-"
                 "CORRIDOR)",
         I(An(A["PAST"], A["N_2BVIA"]), N(A["KEYED"]))),
        ("B-CAP", "settle.eps_any_advantage / capacity: N pairs carry >= 2 bits per teleported qubit before light iff "
                  "eps > eps_any(L, N) -- for nlcontrol's Hamiltonian (H-NLCONTROL-FORM: CMAX = log2 1.25, N < 7 "
                  "impossible at any eps).  The W2 class: <= 1 bit/pair under H-BORN-AT-BOB, not attained at finite "
                  "T (A1); without H-BORN-AT-BOB its capacity is OPEN",
         Eq(A["CAP"], An(A["SIG"], A["N_EPS"]))),
        ("B-EPSWIN", f"combine.eps_window (z3 reals) at this cell: the transferred-bound window is "
                     f"{'NON-EMPTY' if win_open else 'EMPTY'} under both H-MAP readings; an unbounded H-12 carrier "
                     f"(N_H12W) frees N_EPS from it (settle.h12_carrier_case: 2 of 9 cells flip)",
         I(A["N_EPS"], Or(z3.BoolVal(bool(win_open)), An(A["H12"], A["N_H12W"])))),
        ("B-TOPO", "Geroch 1967 (board D67 NARROWED, kinematic theorem stands) / Tipler 1977 (NARROWED) bind a "
                   "corridor made by a classical Lorentzian topology change (GTOPO).  It fails to be one only under a "
                   "named premise: ITB + N_QTOPO (no READ source), ITE + N_MS17 (MS p.17, READ; non-traversable "
                   "bridge only), ITB + R-INDEX + N_MEASPHYS (A3: H-IT necessary, not sufficient)",
         Eq(N(A["GTOPO"]), rel_topo)),
        ("B-THROAT", "Morris-Thorne 1988 (board D67 STANDS) binds a geometric throat (THROAT).  It fails to be one only "
                     "under ITB + N_QTOPO or ITB + R-INDEX + N_MEASPHYS (symmetric with B-TOPO; A3's only-if kept: "
                     "R-INDEX without H-IT releases nothing).  Under ITE the bridge is geometry and MS fn.1 assumes "
                     "it non-traversable: no release.  Wave 1 encoded (ITB and RI) => no throat, H-IT as SUFFICIENT",
         Eq(N(A["THROAT"]), rel_throat)),
        ("B-LOCC", "MS 1306.0533v2 sec.3.2 pp.16-17 (READ here): LOCC cannot create entanglement, no bridge "
                   "'without preexisting bridges'; geometry.locc_entropy_change 8.9e-16; transit."
                   "TRAVERSAL_IS_REMOVED False; combine.product_drift: the drift on a product state gives exactly 0",
         I(N(A["N_VAC"]), A["DIST"])),
        ("B-HELD", "geometry.r_quantum: the QEI duration bound covers 2.08e-68 of the 1 m throat's deficit (minimal "
                   "scalar, in scope); zero.py and geometry.nec_shift_z3: a zero shift moves the NEC by exactly 0; "
                   "geometry.qnec_price: the QNEC prices, does not supply.  Open branches: xi > 0 (N_XI), eps_G "
                   "(N_EPSG), EGJ out of equilibrium with H-IT and H-ZERO or H-NULL (N_EQUIL, A4 wave 2)",
         I(A["HELD"], held)),
        ("B-ILFREE", "no source prices a non-geometric corridor: free making/holding only through N_ILFREE (OPEN)",
         I(A["ILFREE"], A["N_ILFREE"])),
        ("B-RECV", "transit.CARRIES_SUBSTANCE False (a receiver must be there); Bekenstein quant-ph/0404042v1 pp.2, 8 "
                   "(READ, A3): a complete system with E > 0 holds the bits (a FLOOR on the holder: measure."
                   "bekenstein_floor_j 33-379 J at R = 1 m); LEDGER.md S10 REFUSED, S13 and S5 OPEN, both needing a "
                   "prior arrival at <= c (D23); measure.info_s_clash: phi(1) = 0 bits, Bekenstein 0 bits at E = 0",
         A["RECV"]),
    ]


def _defs(A, mutate=()):
    """The obstruction-removal and not-bound atoms, defined.  Definitions, not holdings."""
    E, N, Or, An = (lambda a, b: a == b), z3.Not, z3.Or, z3.And
    hold = Or(An(A["THROAT"], A["HELD"]), An(N(A["THROAT"]), A["ILFREE"]))
    if "wave1-THROAT" in mutate:           # wave 1's DEF-HOLD: no throat counted as removal
        hold = Or(N(A["THROAT"]), A["HELD"])
    return [
        ("DEF-BITS", "O-BITS removed iff the channel carries >= 2 bits per qubit before light",
         E(A[RM["O-BITS"]], A["CAP"])),
        ("DEF-TOPO", "O-MAKE-TOPO removed iff the corridor is not a classical topology change AND making it is free",
         E(A[RM["O-MAKE-TOPO"]], An(N(A["GTOPO"]), A["ILFREE"]))),
        ("DEF-NB-TOPO", "Geroch/Tipler do not bind iff the corridor is not a classical topology change",
         E(A[NB["O-MAKE-TOPO"]], N(A["GTOPO"]))),
        ("DEF-DIST", "O-MAKE-DIST removed iff no entanglement distribution at <= c is needed",
         E(A[RM["O-MAKE-DIST"]], N(A["DIST"]))),
        ("DEF-HOLD", "O-HOLD removed iff a geometric throat is held, or a non-geometric corridor is held for free",
         E(A[RM["O-HOLD"]], hold)),
        ("DEF-NB-HOLD", "Morris-Thorne does not bind iff there is no geometric throat",
         E(A[NB["O-HOLD"]], N(A["THROAT"]))),
        ("DEF-MATTER", "O-MATTER removed iff no receiver/holder must already be at the destination",
         E(A[RM["O-MATTER"]], N(A["RECV"]))),
        ("DEF-LOOP", "O-LOOP removed iff no closed causal curve", E(A[RM["O-LOOP"]], N(A["LOOP"]))),
    ]


def _commitments(A):
    """What each reading commits to unconditionally (active only when its literal is asserted).  H12, ZERO, NULL and
    RI have content only through board holdings with a named premise (B-EPSWIN, B-HELD, B-TOPO/B-THROAT); INFO has
    none (INERT)."""
    An, N = z3.And, z3.Not
    return [
        ("C-W2", "A1: deterministic drift per branch (H-C2); A2 C2", A["W2"], N(A["LIN"])),
        ("C-W1", "frame.settle_under_C1: the drift on rho_B shows 2.2e-16 dependence on Alice", A["W1"], N(A["SIG"])),
        ("C-KR", "KR 2106.10576v2 sec.2.3 pp.7-8 factorisation: superluminal signal at Bob 0 for every eps "
                 "(DERIVED-FROM-READ, A1)", A["KR"], N(A["SIG"])),
        ("C-F1", "A2 clause 1: a preferred frame exists (keying is N_KEYING, not this)", A["F1"], A["FRAME"]),
        ("C-F2b", "A2 clause 2b: a message reaches the past of the cosmic clock", A["F2b"], An(A["PAST"], A["FRAME"])),
        ("C-ITE", "MS 1306.0533v2 (READ here): fn.1 p.2 'We will assume that wormholes remain un-traversable'; "
                  "sec.3.1 p.16 no local operation on one member 'can influence the other'; sec.5.4 pp.36-37 a "
                  "geometric feature is a linear operator; emtension.ENTANGLED_BRIDGE_IS_TRAVERSABLE False",
         A["ITE"], An(A["LIN"], N(A["SIG"]), A["THROAT"], N(A["HELD"]))),
        ("C-INFOS", "A3 H-INFO-S: information at the destination suffices; no holder need already be there",
         A["INFOS"], N(A["RECV"])),
        ("C-RQ", "A4: R-QUANTUM holds a geometric throat with QEI-bounded negative energy", A["RQ"], A["THROAT"]),
    ]


# =====================================================================================================================
# THE ENGINE
# =====================================================================================================================
class Screen:
    def __init__(self, cell=CELL_MAIN, mutate=(), drop=()):
        self.cell = cell
        self.win_open = cell_window_open(cell)
        self.mutate = tuple(mutate)
        self.A = atoms()
        self.s = z3.Solver()
        self.ind = {}            # indicator name -> (constraint name, ground)
        self.byname = {}         # str(expr) -> expr, for every assumption that can appear in a core
        self.nchecks = 0
        board = [b for b in _board(self.A, self.win_open, mutate) if b[0] not in drop]
        for name, ground, expr in board + _defs(self.A, mutate):
            self._track(name, ground, expr)
        for name, ground, lit, expr in _commitments(self.A):
            self._track(name, ground, z3.Implies(lit, expr))
        self.base = [self.byname[n] for n in self.ind]
        self.constraints = {n: e for n, _, e in board}
        for n in LIT_NAMES + list(NAMED) + list(OPEN_NAMED):
            self.byname[n] = self.A[n]
            self.byname[str(z3.Not(self.A[n]))] = z3.Not(self.A[n])

    def _track(self, name, ground, expr):
        b = z3.Bool("@" + name)
        self.s.add(z3.Implies(b, expr))
        self.ind["@" + name] = (name, ground)
        self.byname["@" + name] = b

    # ---------------------------------------------------------------- primitives
    def lits(self, present):
        return [self.A[n] if n in present else z3.Not(self.A[n]) for n in LIT_NAMES]

    def check(self, assumps):
        self.nchecks += 1
        return self.s.check(*assumps)

    def sat(self, assumps):
        """Satisfiable together with every tracked board holding, definition and commitment."""
        return self.check(self.base + assumps) == z3.sat

    def _core_names(self, soft_names):
        return [str(c) for c in self.s.unsat_core() if str(c) in soft_names]

    def all_mus(self, hard, soft, cap=4000):
        """EVERY minimal subset S of `soft` with hard + S unsat (deletion-based shrinking; alternatives by removing each
        element of a found MUS in turn, memoised).  Returns a list of frozensets of names.  Raises if the cap is hit
        (a silent cap would be a silent truncation)."""
        soft = list(soft)
        names = {str(e): e for e in soft}
        found, seen = [], set()
        nodes = [0]

        def shrink(S):
            S = list(S)
            i = 0
            while i < len(S):
                T = S[:i] + S[i + 1:]
                if self.check(hard + [names[n] for n in T]) == z3.unsat:
                    core = set(self._core_names(set(T)))
                    S = [n for n in T if n in core]
                    i = 0 if len(S) < len(T) else i
                else:
                    i += 1
            return frozenset(S)

        def rec(S):
            key = frozenset(S)
            if key in seen:
                return
            seen.add(key)
            nodes[0] += 1
            if nodes[0] > cap:
                raise RuntimeError("all_mus cap hit -- refused rather than truncated")
            if self.check(hard + [names[n] for n in S]) != z3.unsat:
                return
            core = self._core_names(set(S))
            M = shrink(core)
            if M not in found:
                found.append(M)
            for e in M:
                rec([n for n in S if n != e])
        rec(list(names))
        return [m for m in found if not any(o < m for o in found)]

    @staticmethod
    def _hitting_sets(family):
        elems = sorted(set().union(*family)) if family else []
        out = []
        for k in range(0, len(elems) + 1):
            for c in itertools.combinations(elems, k):
                cs = set(c)
                if all(cs & f for f in family) and not any(h <= cs for h in out):
                    out.append(cs)
        return out

    @staticmethod
    def _split(sup):
        mem = sorted((n for n in sup if n in LIT_NAMES), key=LIT_NAMES.index)
        absent = sorted((n[4:-1] for n in sup if n.startswith("Not(")), key=LIT_NAMES.index)
        named = sorted(n for n in sup if n in NAMED)
        return {"members": mem, "absent": absent, "named": named}

    # ---------------------------------------------------------------- one variant
    def variant(self, present, wave1_engine=False):
        """Screen one variant.  present: set of literal names."""
        A = self.A
        L = self.lits(present)
        res = {"present": sorted(present, key=LIT_NAMES.index), "cell": self.cell}
        if not self.sat(L):
            res["consistent"] = False
            cores = self.all_mus([], self.base + L)
            res["clash_cores"] = [sorted(c) for c in cores]
            return res
        res["consistent"] = True
        named = [A[n] for n in NAMED]
        # premise clashes: every minimal set of named premises inconsistent with the variant
        if not self.sat(L + named):
            pm = self.all_mus(self.base + L, named)
        else:
            pm = []
        pclash = []
        for P in pm:
            lc = self.all_mus(self.base + [A[n] for n in P], L)
            pclash.append({"named": sorted(P), "literal_cores": [self._split(c)["members"] +
                                                                  ["not " + x for x in self._split(c)["absent"]]
                                                                  for c in lc]})
        res["premise_clashes"] = pclash
        mss = [sorted(set(NAMED) - h) for h in self._hitting_sets([set(p) for p in pm])]
        res["premise_sets"] = len(mss)
        per = {}
        pos = [A[n] for n in LIT_NAMES if n in present]
        neg = [z3.Not(A[n]) for n in LIT_NAMES if n not in present]
        for o in OBST:
            per[o] = self._obstruction(L, mss, o, wave1_engine, pos, neg)
        res["per"] = per
        return res

    def _supports(self, L, mss, goal_neg, pos, neg):
        """Minimal supports for 'goal' (goal_neg is its negation, hard).  The variant's ABSENCES are part of the variant
        (closed world) and are held fixed; a support is a minimal set of its PRESENT members plus the named premises of
        one consistent premise set.  Returns (kind, supports) with kind None / 'plain' / 'if'."""
        A = self.A
        hard = self.base + neg + [goal_neg]
        if self.check(hard + pos) == z3.unsat:
            return "plain", self.all_mus(hard, pos)
        sups = []
        for M in mss:
            Mx = [A[n] for n in M]
            if self.check(hard + pos + Mx) == z3.unsat:
                for s in self.all_mus(hard, pos + Mx):
                    if s not in sups:
                        sups.append(s)
        sups = [m for m in sups if not any(o < m for o in sups)]
        return ("if", [self._presupposed(s, pos, neg) for s in sups]) if sups else (None, [])

    def _presupposed(self, sup, pos, neg):
        """A named premise can PRESUPPOSE a member (N_EPS at a cell whose window is empty holds only with H12 and
        N_H12W).  A member left out of a support but entailed by it is added back, so a support never hides a member
        it needs."""
        extra = []
        for m in pos + [self.A[n] for n in NAMED]:
            n = str(m)
            if n not in sup and self.check(self.base + neg + [self.byname[x] for x in sup] + [z3.Not(m)]) == z3.unsat:
                extra.append(n)
        return frozenset(sup) | frozenset(extra)

    def _open_status(self, L, rm):
        A = self.A
        closed = L + [z3.Not(A[k]) for k in OPEN_NAMED] + [rm]
        if self.sat(closed):
            return {"verdict": "SILENT"}
        opens = []
        for k in OPEN_NAMED:
            trial = L + [A[k] if j == k else z3.Not(A[j]) for j in OPEN_NAMED] + [rm]
            if self.sat(trial):
                opens.append(k)
        return {"verdict": "OPEN", "via": opens} if opens else {"verdict": "LEFT"}

    def _obstruction(self, L, mss, o, wave1_engine=False, pos=None, neg=None):
        A = self.A
        rm = A[RM[o]]
        if wave1_engine:                           # CONTROL ONLY: wave 1 assumed every named premise at once
            full = L + [A[n] for n in NAMED]
            if self.check(self.base + full + [z3.Not(rm)]) == z3.unsat:
                prem_sat = self.sat(full)
                return {"verdict": "REMOVED-IF", "premises_sat": prem_sat}
            return {"verdict": "not removed"}
        kind, sups = self._supports(L, mss, z3.Not(rm), pos, neg)
        if kind:
            out = {"verdict": "REMOVED" if kind == "plain" else "REMOVED-IF", "supports": [self._split(s) for s in sups]}
        else:
            out = None
            if o in NB:
                k2, s2 = self._supports(L, mss, z3.Not(A[NB[o]]), pos, neg)
                if k2:
                    out = {"verdict": "NOT-BOUND" if k2 == "plain" else "NOT-BOUND-IF",
                           "supports": [self._split(s) for s in s2], "removal": self._open_status(L, rm)}
            if out is None:
                out = self._open_status(L, rm)
        if "supports" in out:
            out["rests_on"] = sorted({m for s in out["supports"] for m in s["members"]}, key=LIT_NAMES.index)
            out["necessary_members"] = sorted(set.intersection(*[set(s["members"]) for s in out["supports"]]),
                                              key=LIT_NAMES.index) if out["supports"] else []
        return out


# =====================================================================================================================
# VARIANTS, VIEWS
# =====================================================================================================================
def variants():
    """Every variant: the 127 combinations x sub-readings x 4 reading slots, then the 3 reading-only variants.
    H-SETTLE 3 readings, H-FRAME 3 (F1, F2b, F1+F2b), H-IT 2, H-INFO 2: (4*4*3*3*2^3 - 1) * 4 + 3 = 4,607."""
    out = []
    for k in range(1, len(HYPS) + 1):
        for combo in itertools.combinations(HYPS, k):
            choices = [list(SUBREADINGS[h]) for h in combo]
            for pick in itertools.product(*choices):
                lits = frozenset(x for p in pick for x in p.split("+"))
                for slot in READING_SLOTS:
                    out.append((combo, lits | frozenset(slot)))
    for slot in READING_SLOTS[1:]:
        out.append(((), frozenset(slot)))
    return out


def wave1_variants():
    """Wave 1's generator (H-INFO in one reading): (4*4*3*2^4 - 1)*4 + 3 = 3,071 -- for the clash census history."""
    sub = dict(SUBREADINGS)
    sub["H-INFO"] = {"INFO": ""}
    out = []
    for k in range(1, len(HYPS) + 1):
        for combo in itertools.combinations(HYPS, k):
            for pick in itertools.product(*[list(sub[h]) for h in combo]):
                lits = frozenset(x for p in pick for x in p.split("+"))
                for slot in READING_SLOTS:
                    out.append(lits | frozenset(slot))
    for slot in READING_SLOTS[1:]:
        out.append(frozenset(slot))
    return out


def counts(res, kinds=RMV + NBV):
    return sorted(o for o, v in res.get("per", {}).items() if v["verdict"] in kinds)


def removed_set(res):
    return counts(res, RMV)


def five_view(res, kinds=RMV + NBV):
    """Fold O-MAKE-TOPO and O-MAKE-DIST into O-MAKE (counted only if both are)."""
    r = set(counts(res, kinds))
    out = [o for o in ("O-BITS", "O-HOLD", "O-MATTER", "O-LOOP") if o in r]
    if "O-MAKE-TOPO" in r and "O-MAKE-DIST" in r:
        out.append("O-MAKE")
    return sorted(out, key=FIVE.index)


def attributed(res, kinds=RMV + NBV, graded=None):
    """Obstructions removed / not-bound with a support containing a member (or a graded literal): what the variant's
    hypotheses do, as opposed to what the board and named premises do alone."""
    g = set(graded) if graded is not None else set(res["present"])
    out = []
    for o, v in res.get("per", {}).items():
        if v["verdict"] in kinds and any(set(s["members"]) & g for s in v["supports"]):
            out.append(o)
    return sorted(out, key=OBST.index)


def signature(res):
    if not res["consistent"]:
        return ("INCONSISTENT", tuple(tuple(c) for c in res["clash_cores"]))
    return ("C", tuple((o, v["verdict"], tuple(v.get("via", ())), tuple(v.get("removal", {}).get("via", ())))
                       for o, v in res["per"].items()),
            tuple(tuple(p["named"]) for p in res["premise_clashes"]))


_WORKER = {}


def _winit(cell, mutate):
    _WORKER["scr"] = Screen(cell=cell, mutate=mutate)


def _wrun(item):
    combo, present = item
    r = _WORKER["scr"].variant(set(present))
    r["combo"] = list(combo)
    return r


def run_screen(scr=None, only=None, procs=None, singles_from=None):
    """Screen every variant (in parallel worker processes, each with its own z3 Screen; COMBINE_SERIAL=1 runs it in
    this process).  The result does not depend on the split: each variant is screened independently."""
    scr = scr or Screen()
    t0 = time.time()
    items = [(combo, tuple(sorted(p))) for combo, p in variants() if not only or only(p)]
    procs = procs or min(4, os.cpu_count() or 1)
    rows = None
    if procs > 1 and os.environ.get("COMBINE_SERIAL") != "1":
        try:
            import multiprocessing as mp
            with mp.get_context("fork").Pool(procs, initializer=_winit, initargs=(scr.cell, scr.mutate)) as pool:
                rows = pool.map(_wrun, items, chunksize=32)
        except Exception as e:          # recorded, then serial: never a silent skip
            print("parallel screen failed, running serially:", repr(e), file=sys.stderr)
            rows = None
    if rows is None:
        rows = []
        for combo, present in items:
            r = scr.variant(set(present))
            r["combo"] = list(combo)
            rows.append(r)
    base = scr.variant(set())
    by = {frozenset(r["present"]): r for r in rows}
    singles = {}
    for r in rows + (singles_from["rows"] if singles_from else []):
        if len(r["present"]) == 1 and r["present"][0] not in singles:
            singles[r["present"][0]] = set(attributed(r)) if r["consistent"] else None
    for r in rows:
        if not r["consistent"]:
            continue
        z = set(attributed(r))
        u = set()
        for m in r["present"]:
            u |= singles.get(m) or set()
        r["attributed"] = sorted(z, key=OBST.index)
        r["union_of_singletons"] = sorted(u, key=OBST.index)
        r["synergy"] = sorted(z - u, key=OBST.index)
        r["interference"] = sorted(u - z, key=OBST.index)
        contributors = set()
        for o in z:
            contributors |= set(r["per"][o]["rests_on"])
        r["contributors"] = sorted(contributors & set(r["present"]), key=LIT_NAMES.index)
        r["complementary"] = len(z) >= 1 and not any((singles.get(m) or set()) >= z for m in r["present"])
        r["member_free"] = sorted((o for o, v in r["per"].items() if v["verdict"] in RMV + NBV and o not in z),
                                  key=OBST.index)
    for r in rows:
        if r["consistent"] and r["interference"]:
            # which present literal undoes it: the single-literal removal that brings the lost obstruction back
            causes = []
            for m in r["present"]:
                other = by.get(frozenset(r["present"]) - {m}) or (singles_from or {}).get("by", {}).get(
                    frozenset(r["present"]) - {m})
                if other and other["consistent"] and set(r["interference"]) & set(other.get("attributed", [])):
                    causes.append(m)
            r["interference_causes"] = causes
    return {"rows": rows, "base": base, "by": by, "seconds": time.time() - t0}


# =====================================================================================================================
# CENSUSES: clashes by inclusion-exclusion, premise clashes, the difference census (which literal does anything)
# =====================================================================================================================
def _ie(sets_by_family, universe):
    """Inclusion-exclusion over families: presence per family, every intersection, the union, the 'sole' counts."""
    fams = list(sets_by_family)
    out = {"present": {f: len(sets_by_family[f]) for f in fams}, "intersections": {}, "sole": {}}
    union = 0
    for k in range(1, len(fams) + 1):
        for c in itertools.combinations(fams, k):
            inter = set.intersection(*[sets_by_family[f] for f in c])
            if k > 1:
                out["intersections"][" & ".join(c)] = len(inter)
            union += (-1) ** (k + 1) * len(inter)
    out["union_by_ie"] = union
    out["union_direct"] = len(set().union(*sets_by_family.values())) if fams else 0
    for f in fams:
        others = set().union(*[sets_by_family[g] for g in fams if g != f]) if len(fams) > 1 else set()
        out["sole"][f] = len(sets_by_family[f] - others)
    return out


def clash_census(rows):
    """Every minimal core of every inconsistent variant, counted (variants per distinct core); the cores grouped by the
    MINIMAL literal set they contain (the clash's cause), and the groups counted by inclusion-exclusion."""
    inc = [r for r in rows if not r["consistent"]]
    cores, litsets = {}, set()
    for i, r in enumerate(inc):
        for c in r["clash_cores"]:
            lits = frozenset(n for n in c if n in LIT_NAMES)
            holds = tuple(sorted(n[1:] for n in c if n.startswith("@")))
            key = " + ".join(sorted(lits, key=LIT_NAMES.index)) + " | " + " + ".join(holds)
            cores.setdefault(key, set()).add(i)
            litsets.add(lits)
    minimal = [l for l in litsets if not any(o < l for o in litsets)]
    groups = {}
    for i, r in enumerate(inc):
        for c in r["clash_cores"]:
            lits = frozenset(n for n in c if n in LIT_NAMES)
            for m in minimal:
                if m <= lits:
                    groups.setdefault(" + ".join(sorted(m, key=LIT_NAMES.index)), set()).add(i)
    multi = sum(1 for r in inc if len(r["clash_cores"]) > 1)
    return {"inconsistent": len(inc), "distinct_cores": {k: len(v) for k, v in cores.items()},
            "families": _ie(groups, len(inc)), "variants_with_more_than_one_core": multi}


def premise_census(rows):
    fam = {}
    for i, r in enumerate(rows):
        if r["consistent"]:
            for p in r["premise_clashes"]:
                for lc in p["literal_cores"]:
                    key = "{" + ", ".join(p["named"]) + "} with " + (" + ".join(lc) or "(the board alone)")
                    fam.setdefault(key, set()).add(i)
    return _ie(fam, len(rows)) if fam else {"present": {}, "union_by_ie": 0, "union_direct": 0}


def wave1_clash_census():
    """Wave 1's three clash families over wave 1's 3,071 variants, by literal presence (the encoding made each family
    unsat by itself, and they were the only unsat cores): presence, intersections, union by inclusion-exclusion, sole.
    Wave 1 first reported the z3-returned split (a) 640, (b) 256, (c) 256."""
    vs = wave1_variants()
    fam = {"(a) F1+F2b": {i for i, v in enumerate(vs) if {"F1", "F2b"} <= v},
           "(b) ITB+RI+RQ": {i for i, v in enumerate(vs) if {"ITB", "RI", "RQ"} <= v},
           "(c) ITE+W2": {i for i, v in enumerate(vs) if {"ITE", "W2"} <= v}}
    out = _ie(fam, len(vs))
    out["variants"] = len(vs)
    out["wave1_reported_split"] = {"(a) F1+F2b": 640, "(b) ITB+RI+RQ": 256, "(c) ITE+W2": 256}
    return out


def exercised(S):
    """The difference census: for each literal h, in how many consistent variants does dropping h change the result
    (consistency, any per-obstruction verdict, any OPEN pathway, any premise clash)?  A literal that changes nothing
    anywhere is UNTESTED-BY-SCREEN -- measured, not asserted.  Also: in how many variants is h in a support."""
    rows, by, base = S["rows"], S["by"], S["base"]
    out = {}
    for h in LIT_NAMES:
        changed, inc_due, total, insup = 0, 0, 0, 0
        what = {}
        for r in rows:
            if h not in r["present"]:
                continue
            total += 1
            other = by.get(frozenset(r["present"]) - {h}) if len(r["present"]) > 1 else base
            if other is None:
                continue
            if signature(r) != signature(other):
                changed += 1
                if not r["consistent"] and other["consistent"]:
                    inc_due += 1
                    what["consistency"] = what.get("consistency", 0) + 1
                elif r["consistent"] and other["consistent"]:
                    for o in OBST:
                        a, b = r["per"][o], other["per"][o]
                        if (a["verdict"], a.get("via"), a.get("removal")) != (b["verdict"], b.get("via"), b.get("removal")):
                            what[o] = what.get(o, 0) + 1
                    if [p["named"] for p in r["premise_clashes"]] != [p["named"] for p in other["premise_clashes"]]:
                        what["premise clash"] = what.get("premise clash", 0) + 1
            if r["consistent"] and any(h in v.get("rests_on", []) for v in r["per"].values()):
                insup += 1
        out[h] = {"variants_with_h": total, "changed_by_h": changed, "made_inconsistent_by_h": inc_due,
                  "in_a_support": insup, "what_changes": what,
                  "status": "EXERCISED" if changed else "UNTESTED-BY-SCREEN"}
    return out


def exercised_cells(S_au, S):
    """The difference census over the 1 AU re-screen; a variant whose h-less partner was not re-screened (it has no
    W2) is compared with the main cell's result, which is the same there (N_EPS reaches no variant without W2)."""
    by = dict(S["by"])
    by.update(S_au["by"])
    return exercised({"rows": S_au["rows"], "by": by, "base": S["base"]})


def named_census(S):
    """For each named premise: in how many consistent variants is it inadmissible (in a premise clash), and in how many
    is it in a support.  A premise never inadmissible anywhere could never have failed: assuming it is STRUCTURAL."""
    out = {}
    for n in NAMED:
        bad = sum(1 for r in S["rows"] if r["consistent"] and any(n in p["named"] for p in r["premise_clashes"]))
        used = sum(1 for r in S["rows"] if r["consistent"] and
                   any(n in s["named"] for v in r["per"].values() for s in v.get("supports", [])))
        out[n] = {"inadmissible_in": bad, "in_a_support_in": used,
                  "assumption": "CONSTRAINED (can fail)" if bad else "STRUCTURAL (never constrained: cannot fail)"}
    return out


def mentions(scr, atom):
    return sorted(n for n, e in scr.constraints.items() if re.search(r"\b" + re.escape(atom) + r"\b", str(e)))


# =====================================================================================================================
# GUARDS (PROOF-ASSISTANT.md): vacuity and encoding drift
# =====================================================================================================================
def guard_vacuity(scr, scr_au):
    A = scr.A
    out, structural = {}, {}
    none = scr.lits(set())
    out["board_alone_sat"] = scr.sat(none)
    out["each_single_reading_sat"] = {n: scr.sat(scr.lits({n})) for n in LIT_NAMES if n != "INFOS"}
    out["INFOS_alone_unsat (a clash with B-RECV, A3)"] = not scr.sat(scr.lits({"INFOS"}))
    out["named_jointly_sat_with_board (1 ly)"] = scr.sat(none + [A[n] for n in NAMED])
    out["named_jointly_UNSAT_with_board (1 AU: N_EPS excluded)"] = not scr_au.sat(scr_au.lits(set()) +
                                                                                  [scr_au.A[n] for n in NAMED])
    out["all_named_and_open_sat_with_board"] = scr.sat(none + [A[n] for n in list(NAMED) + list(OPEN_NAMED)])
    caught = {
        "ITE & W2 (MS assumptions vs per-branch drift)": not scr.sat(scr.lits({"ITE", "W2"})),
        "INFOS (H-INFO-S vs B-RECV)": not scr.sat(scr.lits({"INFOS"})),
        "planted signal in linear QM (no W2, SIG)": not scr.sat(none + [A["SIG"]]),
        "F1 & F2b under N_KEYING & N_2BVIA (premise clash)": not scr.sat(scr.lits({"F1", "F2b"}) +
                                                                           [A["N_KEYING"], A["N_2BVIA"]]),
        "F2b under N_FRW & N_2BVIA (premise clash: exact FRW excludes clause 2b via corridors)":
            not scr.sat(scr.lits({"F2b"}) + [A["N_FRW"], A["N_2BVIA"]]),
        "ITB & RQ under N_QTOPO (premise clash, A4: one corridor, two accounts)": not scr.sat(
            scr.lits({"ITB", "RQ"}) + [A["N_QTOPO"]]),
        "W2 at 1 AU without H12 under N_EPS (premise clash: window empty)": not scr_au.sat(
            scr_au.lits({"W2"}) + [scr_au.A["N_EPS"]]),
    }
    out["known_contradictions_caught"] = caught
    out["F1 & F2b consistent as commitments (wave 1 called this M's sentence contradicting itself)"] = scr.sat(
        scr.lits({"F1", "F2b"}))
    out["ITB & RI & RQ consistent as commitments (wave 1's clash b was B-THROAT's slip)"] = scr.sat(
        scr.lits({"ITB", "RI", "RQ"}))
    out["board_admits_loop"] = scr.sat(none + [A["LOOP"]])
    out["board_admits_no_loop"] = scr.sat(none + [z3.Not(A["LOOP"])])
    out["board_alone_forces_recv"] = not scr.sat(none + [z3.Not(A["RECV"])])
    scr2 = Screen(drop=("B-RECV",))
    out["CONTROL without_B_RECV_matter_removable"] = scr2.sat(scr2.lits(set()) + [A["rm:O-MATTER"]])
    # N_EPS reaches no variant without W2: proved (it occurs only in B-CAP and B-EPSWIN, and CAP needs SIG needs W2)
    out["N_EPS occurs only in"] = mentions(scr, "N_EPS")
    out["no CAP without W2 (z3)"] = not scr_au.sat(scr_au.lits(set()) + [scr_au.A["CAP"]])
    # CONTENT of the premise-satisfiability check: the wave-1 engine at 1 AU reports vacuous removals
    w1 = [scr_au.variant(v, wave1_engine=True)["per"]["O-BITS"] for v in ({"W2"}, {"W2", "F1"}, {"W2", "ITB"})]
    out["CONTROL wave-1 engine at 1 AU: vacuous REMOVED-IF on O-BITS caught"] = sum(
        1 for p in w1 if p["verdict"] == "REMOVED-IF" and not p["premises_sat"])
    structural["every REMOVED-IF / NOT-BOUND-IF support is drawn from a premise set consistent with the variant"] = (
        "STRUCTURAL: true by construction of the engine (cannot fail); its content is the control above")
    ok = (out["board_alone_sat"] and all(out["each_single_reading_sat"].values())
          and out["INFOS_alone_unsat (a clash with B-RECV, A3)"] and out["named_jointly_sat_with_board (1 ly)"]
          and out["named_jointly_UNSAT_with_board (1 AU: N_EPS excluded)"] and out["all_named_and_open_sat_with_board"]
          and all(caught.values()) and out["board_admits_loop"] and out["board_admits_no_loop"]
          and out["board_alone_forces_recv"] and out["CONTROL without_B_RECV_matter_removable"]
          and out["N_EPS occurs only in"] == ["B-CAP", "B-EPSWIN"] and out["no CAP without W2 (z3)"]
          and out["CONTROL wave-1 engine at 1 AU: vacuous REMOVED-IF on O-BITS caught"] == 3
          and out["F1 & F2b consistent as commitments (wave 1 called this M's sentence contradicting itself)"]
          and out["ITB & RI & RQ consistent as commitments (wave 1's clash b was B-THROAT's slip)"])
    out["STRUCTURAL"] = structural
    return ok, out


def _report_grades():
    G = {}
    for rid in ("A1-settle", "A2-frame", "A3-measure", "A4-geometry"):
        p = os.path.join(SCRATCH_REPORTS, rid + ".json")
        try:
            with open(p) as f:
                G[rid] = json.load(f)["grades"]
        except Exception:
            G[rid] = None
    return G


def _grade(G, rid, key):
    for g in G.get(rid) or []:
        if key in g["hypothesis"]:
            return g
    return None


ORDER = {"CLASH": 5, "R": 4, "NB": 3, "OPEN": 2, "N": 1}


def parse_report_class(text, present, grade=None, G=None, rid=None):
    """The A-report's per-obstruction text -> one class: R (REMOVED / REMOVED-IF), NB (NOT-BOUND-IF), OPEN, N (LEAVES /
    LEFT / SILENT / REINTRODUCED -- 'not removed by this hypothesis'), CLASH.  Rules, stated:
      P1 parentheticals citing another report ('(A1: ...)') are dropped;
      P2 'as H-SETTLE-W' resolves to that grade's text;
      P3 precedence CLASH > NOT-BOUND-IF > REMOVED-IF > OPEN > the rest;
      P4 a '(measure); ... (corridor)' text is read on its corridor clause; a NOT-BOUND-IF whose premise names H-IT,
         in a variant without H-IT, is N (the grade's own conditional is unmet)."""
    t = text
    if t.startswith("as H-SETTLE-W") and G is not None:
        g0 = _grade(G, "A1-settle", "H-SETTLE-W (M's definition")
        return None if g0 is None else ("ALIAS", g0)
    t = re.sub(r"\(A[1-4]:[^)]*\)", "", t)
    if "(corridor)" in t:
        t = t.split(";")[-1]
    if "CLASH" in t:
        return "CLASH"
    if "NOT-BOUND-IF" in t:
        if "H-IT" in t and not ({"ITB", "ITE"} & set(present)):
            return "N"
        return "NB"
    if "REMOVED-IF" in t or t.startswith("REMOVED"):
        return "R"
    if "OPEN" in t:
        return "OPEN"
    return "N"


def z3_class(res, o, graded, form):
    """z3's verdict -> the same classes.  Rules, stated:
      Z1 a REMOVED(-IF) / NOT-BOUND(-IF) counts only if some support contains a GRADED literal; otherwise N (removed by
         the board and named premises alone -- e.g. the exact-FRW geometry -- not by the graded hypothesis);
      Z2 O-MAKE-DIST 'OPEN via N_VAC only' is N (the A-reports do not carry N_VAC, which opens it in every variant);
      Z3 for a NOT-BOUND verdict the removal's own status is also returned (an A-report OPEN matches NB + OPEN);
      Z4 the five-way O-MAKE is the weaker of O-MAKE-TOPO and O-MAKE-DIST ('form' TOPO compares O-MAKE-TOPO alone)."""
    if not res["consistent"]:
        return {"CLASH"}
    if o == "O-MAKE" and form == "5":
        a, b = z3_class(res, "O-MAKE-TOPO", graded, form), z3_class(res, "O-MAKE-DIST", graded, form)
        lo = min(max(ORDER[x] for x in a), max(ORDER[x] for x in b))
        return {k for k, v in ORDER.items() if v == lo}
    if o == "O-MAKE":
        o = "O-MAKE-TOPO"
    v = res["per"][o]
    g = set(graded)
    if v["verdict"] in RMV + NBV:
        if not any(set(s["members"]) & g for s in v["supports"]):
            return {"N"}
        if v["verdict"] in RMV:
            return {"R"}
        out = {"NB"}
        if v["removal"]["verdict"] == "OPEN" and v["removal"]["via"] != ["N_VAC"]:
            out.add("OPEN")
        return out
    if v["verdict"] == "OPEN":
        return {"N"} if v["via"] == ["N_VAC"] else {"OPEN"}
    return {"N"}


# (variant, cell, report id, grade key, graded literals, O-MAKE form)
EXPECT = [
    ({"W2"}, CELL_MAIN, "A1-settle", "H-SETTLE-W (M's definition", {"W2"}, "5"),
    ({"W1"}, CELL_MAIN, "A1-settle", "reduced state (convention C1)", {"W1"}, "5"),
    ({"KR"}, CELL_MAIN, "A1-settle", "H-SETTLE-KR", {"KR"}, "5"),
    ({"H12"}, CELL_MAIN, "A1-settle", "H-12 alone", {"H12"}, "5"),
    ({"W2", "H12"}, CELL_MAIN, "A1-settle", "H-SETTLE-W x H-12 under H-TRANSFER", {"W2", "H12"}, "5"),
    ({"W2", "H12"}, CELL_AU, "A1-settle", "under H-12-CARRIER", {"W2", "H12"}, "5"),
    ({"W2", "F1"}, CELL_MAIN, "A1-settle", "H-SETTLE-W x H-FRAME", {"W2", "F1"}, "5"),
    ({"F1"}, CELL_MAIN, "A2-frame", "clause 1 (a preferred frame exists)", {"F1"}, "5"),
    ({"F2b"}, CELL_MAIN, "A2-frame", "clause 2b", {"F2b"}, "5"),
    ({"W2", "F1"}, CELL_MAIN, "A2-frame", "H-FRAME + H-SETTLE-W under C2", {"W2", "F1"}, "5"),
    ({"W1"}, CELL_MAIN, "A2-frame", "under convention C1, with or without", {"W1"}, "5"),
    ({"W1", "F1"}, CELL_MAIN, "A2-frame", "under convention C1, with or without", {"W1"}, "5"),
    ({"INFO"}, CELL_MAIN, "A3-measure", "H-INFO (information is primary", {"INFO"}, "5"),
    ({"INFOS"}, CELL_MAIN, "A3-measure", "H-INFO-S", {"INFOS"}, "5"),
    ({"RI"}, CELL_MAIN, "A3-measure", "R-INDEX", {"RI"}, "5"),
    ({"ITB", "RI"}, CELL_MAIN, "A3-measure", "R-INDEX", {"RI", "ITB"}, "TOPO"),
    ({"W2", "INFO"}, CELL_MAIN, "A3-measure", "H-SETTLE x H-INFO", {"W2", "INFO"}, "5"),
    ({"INFO", "ZERO"}, CELL_MAIN, "A3-measure", "H-INFO x H-ZERO", {"INFO", "ZERO"}, "5"),
    ({"ITE"}, CELL_MAIN, "A4-geometry", "ER=EPR (ITE", {"ITE"}, "6"),
    ({"ITB"}, CELL_MAIN, "A4-geometry", "(ITB), alone", {"ITB"}, "6"),
    ({"ZERO"}, CELL_MAIN, "A4-geometry", "H-ZERO (zero = ground state), alone", {"ZERO"}, "6"),
    ({"ZERO", "ITB"}, CELL_MAIN, "A4-geometry", "H-ZERO with H-IT", {"ZERO", "ITB"}, "6"),
    ({"ZERO", "ITE"}, CELL_MAIN, "A4-geometry", "H-ZERO with H-IT", {"ZERO", "ITE"}, "6"),
    ({"NULL", "ITB"}, CELL_MAIN, "A4-geometry", "H-IT with H-NULL", {"NULL", "ITB"}, "6"),
    ({"NULL"}, CELL_MAIN, "A4-geometry", "H-NULL (null", {"NULL"}, "6"),
    ({"RQ"}, CELL_MAIN, "A4-geometry", "R-QUANTUM", {"RQ"}, "6"),
]

# Every disagreement z3 has with an A-report, with its reason.  The guard passes only if each disagreement found is
# listed here; a mutated encoding must produce one that is NOT.  The count is reported, not hidden.
EXPLAINED = {
    ("A1-settle", "W2", "O-LOOP"): "A1 attributes O-LOOP to H-SETTLE-W alone (REMOVED-IF {H-FRW-EXACT, "
        "H-NOT-DE-SITTER, N_SIGKEY}).  z3: the removal rests on no member -- it is the exact-FRW geometry (N_FRW) with "
        "N_CORR, in EVERY variant without clause 2b; W2 only adds the need for N_SIGKEY.  A1's own H-12-alone grade "
        "(O-LOOP LEAVES) is the same geometry left unattributed, so the two A1 grades disagree with each other",
    ("A1-settle", "W2+H12", "O-LOOP"): "A1's 'as H-SETTLE-W': the same attribution as row W2 -- the O-LOOP removal "
        "rests on the exact-FRW geometry (N_FRW, N_CORR), no member",
    ("A1-settle", "W2+H12", "O-HOLD"): "A1's 'OPEN (G in KR form)' is the KR reading of H-SETTLE (N_EPSG); in a W2 "
        "variant H-SETTLE is read W2 and the KR branch is not present (one reading per variant)",
    ("A2-frame", "F2b", "O-MAKE"): "A2's 'a CTC reopens Geroch's clause' (topology change WITH a CTC) is not carried "
        "as a pathway here: it would trade O-MAKE-TOPO for O-LOOP, and the screen keeps them separate (encoding "
        "choice, named)",
    ("A4-geometry", "ITE+ZERO", "O-HOLD"): "A4's H-ZERO + H-IT grade does not split H-IT's readings.  Under ITE, MS fn.1 "
        "assumes the bridge non-traversable (C-ITE: not HELD), which closes the EGJ route; under ITB it is OPEN via "
        "N_EQUIL as A4 says (row ZERO+ITB agrees)",
}


def guard_drift(scrs, G=None):
    """Compare z3 with the A-reports' own grade text, row by row and obstruction by obstruction."""
    G = G if G is not None else _report_grades()
    rows, n_cmp, n_agree, unexplained = [], 0, 0, []
    for present, cell, rid, key, graded, form in EXPECT:
        scr = scrs[cell]
        r = scr.variant(set(present))
        g = _grade(G, rid, key)
        if g is None:
            unexplained.append((rid, key, "grade not found"))
            continue
        tag = "+".join(sorted(present, key=LIT_NAMES.index))
        if not r["consistent"]:            # an inconsistent variant is compared once, on the grade's verdict
            agree = g["verdict"] == "CLASH"
            n_cmp += 1
            n_agree += agree
            if not agree and EXPLAINED.get((rid, tag, "verdict")) is None:
                unexplained.append((rid, tag, "verdict", g["verdict"], ["CLASH"]))
            rows.append({"variant": tag, "cell": cell, "report": rid, "grade": g["hypothesis"][:80],
                         "obstruction": "(variant)", "report_text": g["verdict"], "report_class": g["verdict"],
                         "z3_class": ["CLASH: " + "; ".join("+".join(c) for c in r["clash_cores"])], "agree": agree,
                         "explained": EXPLAINED.get((rid, tag, "verdict"))})
            continue
        for o, text in g["per_obstruction"].items():
            if o not in FIVE + OBST:
                continue
            rep = parse_report_class(text, present, g, G, rid)
            if isinstance(rep, tuple):
                rep = parse_report_class(rep[1]["per_obstruction"][o], present)
            zc = z3_class(r, o, graded, form)
            agree = rep in zc
            n_cmp += 1
            n_agree += agree
            exp = EXPLAINED.get((rid, tag, o))
            if not agree and exp is None:
                unexplained.append((rid, tag, o, rep, sorted(zc)))
            rows.append({"variant": tag, "cell": cell, "report": rid, "grade": g["hypothesis"][:80], "obstruction": o,
                         "report_text": text[:160], "report_class": rep, "z3_class": sorted(zc), "agree": agree,
                         "explained": exp})
    # ground rows tied to an instrument rather than to report text: settle.h12_carrier_case at 1 AU, N = 7
    ST = _quiet("settle")
    hc, flips = ST.h12_carrier_case()
    cellrow = next(x for x in hc if x["L"] == "1 AU" and x["N"] == 7)
    w = scrs[CELL_AU].variant({"W2"})["per"]["O-BITS"]["verdict"]
    w12 = scrs[CELL_AU].variant({"W2", "H12"})["per"]["O-BITS"]["verdict"]
    ground = {"settle.h12_carrier_case 1 AU N=7 (H-TRANSFER)": cellrow["H-TRANSFER"], "z3 {W2} O-BITS at 1 AU": w,
              "settle (H-12-CARRIER)": cellrow["H-12-CARRIER"], "z3 {W2,H12} O-BITS at 1 AU": w12, "flips": flips}
    ground_ok = (cellrow["H-TRANSFER"] == "EXCLUDED" and w == "LEFT" and cellrow["H-12-CARRIER"].startswith("NOT")
                 and w12 == "REMOVED-IF" and flips == 2)
    ok = not unexplained and ground_ok
    return ok, {"rows": rows, "compared": n_cmp, "agree": n_agree, "unexplained": unexplained,
                "explained_used": sorted({(r["report"], r["variant"], r["obstruction"]) for r in rows
                                          if not r["agree"]}), "ground_rows": ground, "ground_ok": ground_ok,
                "reports_loaded": {k: v is not None for k, v in G.items()}}


def drift_controls(G=None):
    """Each mutated encoding must produce at least one UNEXPLAINED disagreement with the A-reports."""
    out = {}
    for mut in ("KR-unconditional", "wave1-THROAT"):
        scrs = {CELL_MAIN: Screen(mutate=(mut,)), CELL_AU: Screen(cell=CELL_AU, mutate=(mut,))}
        ok, d = guard_drift(scrs, G)
        out[mut] = {"caught": bool(d["unexplained"]), "unexplained": d["unexplained"],
                    "agree": f"{d['agree']}/{d['compared']}"}
    return all(v["caught"] for v in out.values()), out


# =====================================================================================================================
# GROUNDS: every computed ground re-run from its instrument, each compared with an independent computation
# =====================================================================================================================
def board_flags():
    tr = _quiet("transit")
    em = _quiet("emtension")
    led = {}
    with open(os.path.join(WD, "LEDGER.md")) as f:
        for line in f:
            m = re.match(r"^\| (S5|S10|S13) \| \*\*([A-Z]+)\*\*", line)
            if m:
                led[m.group(1)] = m.group(2)
    return {"transit.BEATS_LIGHT": tr.BEATS_LIGHT, "transit.TRAVERSAL_IS_REMOVED": tr.TRAVERSAL_IS_REMOVED,
            "transit.CARRIES_SUBSTANCE": tr.CARRIES_SUBSTANCE, "transit.IT_IS_A_MOVE_NOT_A_COPY":
            tr.IT_IS_A_MOVE_NOT_A_COPY, "emtension.ENTANGLED_BRIDGE_IS_TRAVERSABLE":
            em.ENTANGLED_BRIDGE_IS_TRAVERSABLE, "LEDGER": led}


def ground_checks():
    ST, FR, GE, ME = _quiet("settle"), _quiet("frame"), _quiet("geometry"), _quiet("measure")
    out = {}
    out["B-GISIN bob_y_exact(0.1, 3)"] = ST.bob_y_exact(0.1, 3.0)
    out["B-NOCOM settle_under_C1"] = FR.settle_under_C1()
    out["B-C2-SLICE drift_ordering"] = FR.drift_ordering()
    out["B-ANTITEL antitelephone"] = tuple(FR.antitelephone())
    out["B-ANTITEL reply_arrival(1/2, L=2)"] = FR.reply_arrival(Fr(1, 2), L=Fr(2))
    out["B-TIMEFUNC rank-2"] = FR.cosmic_keyed_rank_n_is_safe(2, 100)
    out["B-TIMEFUNC rank-3"] = FR.cosmic_keyed_rank_n_is_safe(3, 100)
    out["B-FRW frw_time_function_lemma"] = FR.frw_time_function_lemma()
    out["B-2B witness"] = str(FR.past_corridor_witness())
    out["B-CAP CMAX"] = ST.CMAX
    out["B-CAP N=6 at 1 ly"] = ST.eps_to_remove(ST.LY_M, 6)
    out["B-EPSWIN h12_carrier_case flips"] = ST.h12_carrier_case()[1]
    out["B-LOCC local dS"] = GE.locc_entropy_change()[1]
    out["B-HELD fraction covered"] = GE.r_quantum()["fraction_covered"]
    out["B-HELD nec shift (z3)"] = GE.nec_shift_z3()["negation"]
    out["N_EQUIL egj_fR_throat"] = {k: v for k, v in GE.egj_fR_throat().items() if k != "grid_r0=1"}
    out["B-RECV info_s_clash"] = ME.info_s_clash()
    out["flags"] = board_flags()
    return out


def grounds_ok(g):
    f = g["flags"]
    ordv = g["B-C2-SLICE drift_ordering"]
    egj = g["N_EQUIL egj_fR_throat"]
    lem = g["B-FRW frw_time_function_lemma"]
    tests = {
        "W2 signals: bob_y_exact == tanh(2 eps T) (independent: math.tanh)":
            abs(g["B-GISIN bob_y_exact(0.1, 3)"] - math.tanh(0.6)) < 1e-12,
        "C1 does not signal (settle_under_C1 < 1e-12)": g["B-NOCOM settle_under_C1"] < 1e-12,
        "drift ordering == tanh(2 eps (T - t_A)) at every t_A, and differs across orderings":
            all(abs(v - math.tanh(2 * 0.1 * 3.0 * (1 - k))) < 2e-3 for k, v in ordv.items()) and
            max(ordv.values()) - min(ordv.values()) > 0.5,
        "antitelephone == -u L (independent Lorentz formula) for u = v and u = 0; and u = 1/2, L = 2 -> -1":
            g["B-ANTITEL antitelephone"] == (Fr(-3, 5), Fr(0)) and g["B-ANTITEL reply_arrival(1/2, L=2)"] == Fr(-1),
        "cosmic keyed: 0 failures (rank 2, 3)": g["B-TIMEFUNC rank-2"][1] == 0 and g["B-TIMEFUNC rank-3"][1] == 0,
        "FRW lemma unsat, hypothesis non-empty, control a >= 0 sat":
            lem["claim"] == "unsat" and lem["vacuity"] == "sat" and lem["control_a_ge_0"] == "sat",
        "nlcontrol: N < 7 impossible; CMAX == log2 1.25": g["B-CAP N=6 at 1 ly"] is None and
            abs(g["B-CAP CMAX"] - math.log2(1.25)) < 1e-9,
        "H-12 carrier: 2 of 9 cells flip": g["B-EPSWIN h12_carrier_case flips"] == 2,
        "LOCC: local unitaries keep entropy": g["B-LOCC local dS"] < 1e-12,
        "QEI covers < 1e-60": g["B-HELD fraction covered"] < 1e-60,
        "zero shift leaves NEC": g["B-HELD nec shift (z3)"] == "unsat",
        "EGJ: T_kk(r0) >= 0 needs beta ~ 1e69 l_P^2; r^4 T_kk -> -2 r0^2; beta = 0 control":
            1e68 < egj["beta_crit_over_lP2_at_r0"] < 1e70 and egj["large_r_limit_r4Tkk"] == "-2*r_0**2" and
            egj["CONTROL_beta0_equals_Rkk"],
        "INFOS clash support: phi(1) = 0, Bekenstein 0 bits at E = 0, CARRIES_SUBSTANCE False":
            g["B-RECV info_s_clash"]["phi_1_bits"] == 0 and g["B-RECV info_s_clash"]["bekenstein_bits_at_E0_R1m"] == 0
            and g["B-RECV info_s_clash"]["transit_CARRIES_SUBSTANCE"] is False,
        "board flags as encoded": (f["transit.BEATS_LIGHT"] is False and f["transit.TRAVERSAL_IS_REMOVED"] is False
                                   and f["transit.CARRIES_SUBSTANCE"] is False
                                   and f["emtension.ENTANGLED_BRIDGE_IS_TRAVERSABLE"] is False
                                   and f["LEDGER"] == {"S5": "OPEN", "S10": "REFUSED", "S13": "OPEN"}),
    }
    return all(tests.values()), tests


# =====================================================================================================================
# T. THE COMPLEMENTARY TESTS -- built on the members' instruments
# =====================================================================================================================
def _np():
    import numpy as np
    return np


def tfd_drift(betas=(0.0, 0.5, 1.0, 2.0, 4.0, 8.0, 30.0), eps=0.1, T=3.0):
    """H-SETTLE (W2, C2) inside H-IT's own READ model: Van Raamsdonk's eq.(1) state at d = 2 (geometry.tfd), Alice
    measures z or x, each of Bob's branch states drifts under nlcontrol's H = eps <X> Z (C2), Bob reads sigma_y.
    eps = 0.1, T = 3 are nlcontrol's illustrative parameters (DECLARED for the illustration; the law is tanh(2 eps T)).
    Returns, per beta: S (bits), the C2 signal by nlcontrol.evolve and by settle.bloch_exact, the C1 signal (drift on
    rho_B), and the linear control."""
    np = _np()
    GE, NL, ST = _quiet("geometry"), _quiet("nlcontrol"), _quiet("settle")
    bases = {"z": [np.array([1, 0], complex), np.array([0, 1], complex)],
             "x": [np.array([1, 1], complex) / math.sqrt(2), np.array([1, -1], complex) / math.sqrt(2)]}
    rows = []
    for beta in betas:
        psi = GE.tfd(2, beta)
        S = GE.vn_bits(GE.ptrace(GE.rho_of(psi), 2, 0))
        M = psi.reshape(2, 2)
        y = {}
        for lin in (False, True):
            for b, kets in bases.items():
                num = ex = 0.0
                for a in kets:
                    phi = a.conj() @ M
                    p = float(np.vdot(phi, phi).real)
                    if p < 1e-300:
                        continue
                    phi = phi / math.sqrt(p)
                    out = NL.evolve(phi, eps, lin=lin, T=T)
                    num += p * float(np.real(out.conj() @ NL.Y @ out))
                    if not lin:
                        r = ST.bloch_of(phi)
                        ex += p * ST.bloch_exact(tuple(float(c) for c in r), eps, T)[1]
                y[(lin, b)] = num
                if not lin:
                    y[("exact", b)] = ex
        rho_b = GE.ptrace(GE.rho_of(psi), 2, 1)
        rows.append({"beta": beta, "S_bits": S,
                     "C2_signal_integrator": y[(False, "x")] - y[(False, "z")],
                     "C2_signal_exact": y[("exact", "x")] - y[("exact", "z")],
                     "linear_control": y[(True, "x")] - y[(True, "z")],
                     "C1_signal": float(np.abs(GE.bob_state_after(psi, 2, ("M", np.eye(2))) -
                                               GE.bob_state_after(psi, 2, ("M", np.array([[1, 1], [1, -1]]) / math.sqrt(2)))).max()),
                     "rho_B_trace": float(np.trace(rho_b).real)})
    return rows


def product_drift(eps=0.1, T=3.0, trials=6, seed=4):
    """The drift cannot make its own pairs: on a PRODUCT state each of Bob's branch states is Bob's own state, so the
    drifted ensembles coincide.  Max |<Y>_x - <Y>_z| over random product states (nlcontrol.evolve).  CONTROL: the Bell
    state gives tanh(2 eps T)."""
    np = _np()
    NL = _quiet("nlcontrol")
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(trials):
        a = rng.standard_normal(2) + 1j * rng.standard_normal(2); a /= np.linalg.norm(a)
        b = rng.standard_normal(2) + 1j * rng.standard_normal(2); b /= np.linalg.norm(b)
        psi = np.kron(a, b).reshape(2, 2)
        ys = []
        for kets in ([np.array([1, 0]), np.array([0, 1])], [np.array([1, 1]) / math.sqrt(2), np.array([1, -1]) / math.sqrt(2)]):
            tot = 0.0
            for k in kets:
                phi = k.conj() @ psi
                p = float(np.vdot(phi, phi).real)
                if p < 1e-300:
                    continue
                out = NL.evolve(phi / math.sqrt(p), eps, T=T)
                tot += p * float(np.real(out.conj() @ NL.Y @ out))
            ys.append(tot)
        worst = max(worst, abs(ys[1] - ys[0]))
    bell = NL.bob("x", eps, NL.Y) - NL.bob("z", eps, NL.Y)
    return worst, bell


CODATA_HBAR, CODATA_C = 1.054571817e-34, 299792458.0     # CODATA 2018 (declared standard constants, for a cross-check)


def first_transit(L_ly=1.0, N_per_qubit=7, reading="A (eps = 2 pi f)"):
    """The most-removing consistent combination, priced end to end with imported numbers.  Wave 2: no declared T.
      timing  -- the drift time T = atanh(D_N)/(2 eps) is DISTANCE-INDEPENDENT (settle.drift_time_needed); evaluated
                 at the Weinberg-family limit (NAMED-NOT-READ, reading A) it is a floor on T at that limit, not a
                 measured time.  The read precedes light by 1 - T/(L/c) of the light time once pairs are in place.
                 The eps for ANY advantage is settle.eps_any_advantage; wave 1's eps at T = L/2c (DECLARED-FRAC) is
                 exactly twice it.
      first   -- settle.first_transit_times, for the MIDPOINT source (LEDGER D23 as corrected in DOCKET 67: 'a
                 midpoint source spans D at D/(2c)') and for one-end distribution.
      pairs   -- nlcontrol's Hamiltonian (H-NLCONTROL-FORM): N = 7 per qubit without block coding, 2/CMAX = 6.21 on
                 average with it; the W2 class under H-BORN-AT-BOB: > 2 per qubit on average (1 bit/pair ceiling,
                 not attained at finite T) and >= 3 per qubit without block coding; without H-BORN-AT-BOB: OPEN.
                 Every pair distributed at <= c (B-LOCC).
      holder  -- a FLOOR: a complete system of gravitating energy >= the Bekenstein floor must be at the destination
                 (measure.bekenstein_floor_j, cross-checked against hbar c ln2 bits/(2 pi R) with CODATA constants).
                 No instrument computes a holder near the floor; the one READ-backed holder is the body, Mc^2.
    Counts are measure.py's four for a 70 kg body (H-LISTED, H-GRID, H-RHO, H-THERMO there; H-FAITHFUL: one qubit
    per bit)."""
    ST, ME = _quiet("settle"), _quiet("measure")
    rows, geo, ceil, ob = ME.price_table()
    L = L_ly * ST.LY_M
    c = ST.C_LIGHT
    f = ST.BOUNDS_WEINBERG["Majumder+ 1990, 201Hg, PRL 65 2931"]["f_Hz"]
    eps_lim = ST.eps_readings(f)[reading]
    T = ST.drift_time_needed(N_per_qubit, eps_lim)
    e_any = ST.eps_any_advantage(L, N_per_qubit)
    e_half = ST.eps_to_remove(L, N_per_qubit)
    mid = ST.first_transit_times(L, T, "midpoint")
    one = ST.first_transit_times(L, T, "one-end")
    cls_ceiling = ST.W2_CLASS_CEILING_BITS_PER_PAIR
    out = {"L_m": L, "light_time_s": L / c, "reading": reading, "eps_at_limit (NAMED-NOT-READ)": eps_lim,
           "drift_time_T_s (distance-independent; at the unread limit)": T,
           "drift_time_T_h": T / 3600.0, "early_fraction_once_pairs_in_place": ST.arrival_early_fraction(L, N_per_qubit, eps_lim),
           "eps_any_advantage": e_any, "eps_at_T=L/2c (DECLARED-FRAC, wave 1)": e_half, "ratio": e_half / e_any,
           "first_transit_midpoint": mid, "first_transit_one_end": one,
           "pairs_per_qubit": {"nlcontrol, no block coding": N_per_qubit, "nlcontrol, block-coded average": 2.0 / ST.CMAX,
                               "W2 class under H-BORN-AT-BOB: average strictly above": 2.0 / cls_ceiling,
                               "W2 class under H-BORN-AT-BOB: per qubit at least": int(math.floor(2.0 / cls_ceiling)) + 1,
                               "W2 class without H-BORN-AT-BOB": "OPEN"},
           "counts": []}
    for r in rows:
        q = r["bits"]
        indep = q * CODATA_HBAR * CODATA_C * math.log(2) / (2 * math.pi * 1.0)
        out["counts"].append({"count": r["count"], "bits": q, "teleport_ebits": q,
                              "nlcontrol_pairs_N7 (upper figure, one Hamiltonian)": q * N_per_qubit,
                              "nlcontrol_pairs_block_coded": q * 2.0 / ST.CMAX,
                              "W2_class_pairs_floor (H-BORN-AT-BOB, strictly above)": q * 2.0 / cls_ceiling,
                              "holder_FLOOR_J_R1m": r["bekenstein_floor_J_R1m"], "holder_floor_crosscheck_J": indep})
    out["body_rest_energy_J (massform, the READ-backed holder)"] = geo["O-MATTER: massform.rest_energy_j() (Mc^2, 70 kg)"]
    out["throat_J"] = geo["O-HOLD: wormhole.throat_mass(1 m) c^2"]
    out["vacuum_harvest_window_T_over_light_time (DERIVED-FROM-READ, Reznik p.10, p.12)"] = (1.0 / 1.1, 1.0)
    return out


def complementary_tests(S, S_au):
    np = _np()
    FR, GE, ST, ME = _quiet("frame"), _quiet("geometry"), _quiet("settle"), _quiet("measure")
    T = {}
    # T-A  W2 x F1 (and F1 with anything): the drift's own ordering dependence, the antitelephone, cosmic keying
    ordv = FR.drift_ordering()
    at = FR.antitelephone()
    T["T-A W2xF1"] = {
        "drift signal vs Alice's time in Bob's window (frame.drift_ordering)": ordv,
        "exact tanh(2 eps (T - t_A))": {k: math.tanh(0.6 * (1 - k)) for k in ordv},
        "reply keyed to sender / cosmic (frame.reply_arrival)": tuple(str(x) for x in at),
        "cosmic-keyed failures rank 2/3": (FR.cosmic_keyed_rank_n_is_safe(2, 100)[1], FR.cosmic_keyed_rank_n_is_safe(3, 100)[1]),
        "H-IT's model adds no signal to key (geometry.it_no_signal)": GE.it_no_signal(),
        "wave 1 first said": "C2 0.0817 bits per use and 1/2 vs 2/3 ordering dependence (D-CTC circuit): withdrawn as "
                             "a ground -- the D-CTC needs a CTC at Bob, excluded by clause 1",
    }
    T["T-A W2xF1"]["pass"] = (all(abs(ordv[k] - math.tanh(0.6 * (1 - k))) < 2e-3 for k in ordv) and ordv[1.0] == 0.0
                              and at == (Fr(-3, 5), Fr(0)) and T["T-A W2xF1"]["cosmic-keyed failures rank 2/3"] == (0, 0)
                              and T["T-A W2xF1"]["H-IT's model adds no signal to key (geometry.it_no_signal)"] < 1e-12)
    # T-B  W2 inside H-IT's model
    td = tfd_drift()
    sigs = [r["C2_signal_exact"] for r in td]
    T["T-B W2xIT (tfd_drift)"] = {"rows": td, "pass": (
        all(abs(r["C2_signal_integrator"] - r["C2_signal_exact"]) < 5e-3 for r in td) and
        all(abs(r["linear_control"]) < 1e-12 and r["C1_signal"] < 1e-12 for r in td) and
        abs(sigs[0] - math.tanh(0.6)) < 1e-9 and sigs[-1] < 1e-5 and all(a >= b - 1e-12 for a, b in zip(sigs, sigs[1:])))}
    # T-C  W2 cannot make its own pairs
    pw, bell = product_drift()
    T["T-C W2 x O-MAKE-DIST (product_drift)"] = {"product_max_signal": pw, "bell_control": bell,
                                                 "local_unitary_dS (geometry)": GE.locc_entropy_change()[1],
                                                 "nonlocal_control_dS (geometry)": GE.locc_entropy_change(nonlocal_control=True)[1]}
    T["T-C W2 x O-MAKE-DIST (product_drift)"]["pass"] = bool(pw < 1e-12 and bell > 0.5)
    # T-D  ITB x RI: a RECORD of the holder floors (O-MATTER), cross-checked; it does not test O-HOLD
    ft = first_transit()
    floors = [c["holder_FLOOR_J_R1m"] for c in ft["counts"]]
    xchk = max(abs(c["holder_FLOOR_J_R1m"] - c["holder_floor_crosscheck_J"]) / c["holder_FLOOR_J_R1m"] for c in ft["counts"])
    T["T-D ITBxRI (holder FLOOR record)"] = {
        "holder_floor_J_range (FLOORS, not prices)": (min(floors), max(floors)), "throat_J": ft["throat_J"],
        "body Mc^2 J": ft["body_rest_energy_J (massform, the READ-backed holder)"],
        "max relative difference vs CODATA cross-check": xchk,
        "what it is": "a record of the floor on O-MATTER's holder; it does NOT test the O-HOLD verdict (which is "
                      "NOT-BOUND-IF, from B-THROAT); wave 1 first called it a test that O-HOLD is removed"}
    T["T-D ITBxRI (holder FLOOR record)"]["pass"] = xchk < 1e-3
    # T-E  the most-removing consistent variant, end to end
    win, vac = eps_window()
    one_ly = [w for w in win if w["L"] == "1 ly" and w["N"] == 7]
    one_au = [w for w in win if w["L"] == "1 AU" and w["N"] == 7]
    flips = sum(1 for w in win if w["consistent"] != w["consistent_at_T=L/2c (wave 1)"])
    au_T = ST.first_transit_times(ST.AU_M, ft["drift_time_T_s (distance-independent; at the unread limit)"], "midpoint")
    T["T-E max (end to end)"] = {"first_transit": ft, "eps_window": win, "eps_vacuity": vac,
                                 "window flips from wave 1's T = L/2c": flips,
                                 "CONTROL midpoint at 1 AU (T > L/2c): beats light at firing": au_T["beats_light_launched_at_firing"]}
    T["T-E max (end to end)"]["pass"] = (
        vac and all(w["consistent"] for w in one_ly) and not any(w["consistent"] for w in one_au) and flips == 0
        and abs(ft["ratio"] - 2.0) < 1e-6
        and ft["first_transit_midpoint"]["beats_light_launched_at_firing"]
        and not ft["first_transit_one_end"]["beats_light_launched_at_firing"]
        and not au_T["beats_light_launched_at_firing"]
        and 0 < ft["early_fraction_once_pairs_in_place"] < 1)
    # T-F  RQ x KR: two OPENs on O-HOLD; the in-scope number is re-run
    T["T-F RQxKR (O-HOLD OPEN)"] = {"in_scope_fraction": GE.r_quantum()["fraction_covered"],
                                    "note": "xi > 0 (no state-independent QEI) and eps_G (no bound) both OPEN at source"}
    T["T-F RQxKR (O-HOLD OPEN)"]["pass"] = T["T-F RQxKR (O-HOLD OPEN)"]["in_scope_fraction"] < 1e-60
    # T-G  W2 x H12 at 1 AU: the synergy H-12 supplies (settle.h12_carrier_case)
    hc, fl = ST.h12_carrier_case()
    T["T-G W2xH12 at 1 AU (h12_carrier_case)"] = {"rows": hc, "flips": fl,
                                                 "z3 {W2} at 1 AU": S_au["by"][frozenset({"W2"})]["per"]["O-BITS"]["verdict"],
                                                 "z3 {W2,H12} at 1 AU": S_au["by"][frozenset({"W2", "H12"})]["per"]["O-BITS"]["verdict"]}
    T["T-G W2xH12 at 1 AU (h12_carrier_case)"]["pass"] = (fl == 2 and T["T-G W2xH12 at 1 AU (h12_carrier_case)"]["z3 {W2} at 1 AU"] == "LEFT"
                                                          and T["T-G W2xH12 at 1 AU (h12_carrier_case)"]["z3 {W2,H12} at 1 AU"] == "REMOVED-IF")
    # T-H  ZERO/NULL x ITB: the EGJ pathway (N_EQUIL), OPEN, never a removal
    egj = GE.egj_fR_throat()
    T["T-H (ZERO|NULL)xIT (egj_fR_throat)"] = {k: v for k, v in egj.items() if k != "grid_r0=1"}
    T["T-H (ZERO|NULL)xIT (egj_fR_throat)"]["T_kk at 1.05 r0, beta = 0 / beta = -r0^2/2"] = (
        egj["grid_r0=1"][0.0][1.05], egj["grid_r0=1"][0.5][1.05])
    T["T-H (ZERO|NULL)xIT (egj_fR_throat)"]["pass"] = (egj["CONTROL_beta0_equals_Rkk"] and
                                                       egj["large_r_limit_r4Tkk"] == "-2*r_0**2")
    # T-I  INFOS x board: the clash's computed support
    T["T-I INFOS vs B-RECV (info_s_clash)"] = ME.info_s_clash()
    T["T-I INFOS vs B-RECV (info_s_clash)"]["pass"] = (ME.info_s_clash()["phi_1_bits"] == 0 and
                                                       ME.info_s_clash()["bekenstein_bits_at_E0_R1m"] == 0)
    # class table: complementary variants grouped by (attributed set, contributors)
    cover = {}
    for SS in (S, S_au):
        for r in SS["rows"]:
            if not r.get("complementary"):
                continue
            c = set(r["contributors"])
            tests = []
            if "F1" in c:
                tests.append("T-A W2xF1")
            if "W2" in c and ({"ITB", "ITE"} & c):
                tests.append("T-B W2xIT (tfd_drift)")
            if "W2" in c:
                tests.append("T-C W2 x O-MAKE-DIST (product_drift)")
            if {"ITB", "RI"} <= c:
                tests.append("T-D ITBxRI (holder FLOOR record)")
            if {"W2", "ITB"} <= c:
                tests.append("T-E max (end to end)")
            if {"W2", "H12"} <= c:
                tests.append("T-G W2xH12 at 1 AU (h12_carrier_case)")
            if ({"ZERO", "NULL"} & c) and ({"ITB", "ITE"} & c):
                tests.append("T-H (ZERO|NULL)xIT (egj_fR_throat)")
            if "ITB" in c and not tests:
                tests.append("T-B W2xIT (tfd_drift)" if "W2" in c else "T-D ITBxRI (holder FLOOR record)")
            key = r["cell"] + " | " + "|".join(r["attributed"]) + " <- " + ",".join(r["contributors"])
            cover.setdefault(key, {"variants": 0, "tests": set()})
            cover[key]["variants"] += 1
            cover[key]["tests"] |= set(tests)
    for v in cover.values():
        v["tests"] = sorted(v["tests"])
    return T, cover


# =====================================================================================================================
# AGGREGATION, REPORT, SELFTEST
# =====================================================================================================================
def aggregate(rows):
    by = {}
    for r in rows:
        key = tuple(r["combo"]) if r["combo"] else ("(readings only)",)
        by.setdefault(key, []).append(r)
    table = []
    for key, lst in by.items():
        cons = [r for r in lst if r["consistent"]]
        best = max(cons, key=lambda r: (len(five_view(r)), len(counts(r)), len(removed_set(r))), default=None)
        clashes = sorted({"+".join(sorted({n for c in r["clash_cores"] for n in c if n in LIT_NAMES},
                                          key=LIT_NAMES.index)) for r in lst if not r["consistent"]})
        pcl = sorted({"{" + ",".join(p["named"]) + "}" for r in cons for p in r["premise_clashes"]})
        table.append({"combo": list(key), "variants": len(lst), "consistent": len(cons),
                      "inconsistent": len(lst) - len(cons), "clashes": clashes, "premise_clashes": pcl,
                      "best": {o: best["per"][o]["verdict"] for o in OBST} if best else None,
                      "best_five": five_view(best) if best else [],
                      "best_variant": best["present"] if best else None,
                      "complementary_variants": sum(1 for r in cons if r.get("complementary"))})
    return table


def survivors(rows):
    cons = [r for r in rows if r["consistent"]]
    rm_ever, nb_ever = set(), set()
    for r in cons:
        rm_ever |= set(counts(r, RMV))
        nb_ever |= set(counts(r, NBV))
    open_any = {o for r in cons for o, v in r["per"].items() if v["verdict"] == "OPEN"}
    five_ever = set()
    for r in cons:
        five_ever |= set(five_view(r))
    return {"removed_in_no_consistent_variant": sorted(set(OBST) - rm_ever, key=OBST.index),
            "removed_or_not_bound_in_no_consistent_variant": sorted(set(OBST) - rm_ever - nb_ever, key=OBST.index),
            "five_view_never": sorted(set(FIVE) - five_ever, key=FIVE.index),
            "open_somewhere": sorted(open_any, key=OBST.index)}


def load_bearing(rows):
    lb, named = set(), set()
    for r in rows:
        if r["consistent"]:
            for v in r["per"].values():
                if v["verdict"] in RMV + NBV:
                    lb |= set(v["rests_on"])
                    for s in v["supports"]:
                        named |= set(s["named"])
    return sorted(lb, key=LIT_NAMES.index), sorted(named)


def untested(rows, cell):
    reasons = {"INCONSISTENT (named clash; nothing to test)": 0,
               "NO MEMBER CONTRIBUTION (nothing removed or not-bound by a member; any removal is the board's under "
               "named premises)": 0,
               "SINGLE CONTRIBUTOR (one member's set covers the variant's; graded in that member's report)": 0}
    listed = []
    for r in rows:
        if not r["consistent"]:
            reason = "INCONSISTENT (named clash; nothing to test)"
        elif r.get("complementary"):
            continue
        elif not r["attributed"]:
            reason = ("NO MEMBER CONTRIBUTION (nothing removed or not-bound by a member; any removal is the board's "
                      "under named premises)")
        else:
            reason = "SINGLE CONTRIBUTOR (one member's set covers the variant's; graded in that member's report)"
        reasons[reason] += 1
        listed.append((cell, r["present"], reason))
    return reasons, listed


def rule2(S, S_au, ex):
    """Charter rule 2 per literal, from the screen: retired only if EXERCISED and removing/not-binding nothing in every
    combination; an inert literal is UNTESTED-BY-SCREEN."""
    out = {}
    for h in LIT_NAMES:
        att = set()
        for SS in (S, S_au):
            for r in SS["rows"]:
                if r["consistent"] and h in r["present"]:
                    for o in attributed(r, graded={h}):
                        att.add((r["cell"], o, r["per"][o]["verdict"]))
        st = ex[h]["status"]
        if st.startswith("UNTESTED-BY-SCREEN"):
            verdict = "UNTESTED-BY-SCREEN (inert encoding): retirement not established"
        elif h == "INFOS":
            verdict = "CLASH with B-RECV in every variant: a board-versus-M clash, M's to rule; not a retirement"
        elif att:
            verdict = "kept: contributes " + ", ".join(sorted({f"{o} {v}" for _, o, v in att}))
        else:
            what = ex[h]["what_changes"]
            verdict = ("kept: exercised (changes " + ", ".join(sorted(what)) + ") but removes / not-binds nothing; "
                       "not retired while an OPEN pathway or premise clash is its effect" if what else
                       "exercised, no effect")
        out[h] = {"status": st, "rule2": verdict}
    return out


def run_all(with_tests=True):
    scr, scr_au = Screen(), Screen(cell=CELL_AU)
    vac_ok, vac = guard_vacuity(scr, scr_au)
    G = _report_grades()
    drift_ok, drift = guard_drift({CELL_MAIN: scr, CELL_AU: scr_au}, G)
    ctl_ok, ctl = drift_controls(G)
    out = {"refused": not (vac_ok and drift_ok and ctl_ok), "vacuity": vac, "drift": drift, "drift_controls": ctl}
    if out["refused"]:
        return out
    S = run_screen(scr)
    S_au = run_screen(scr_au, only=lambda p: "W2" in p, singles_from=S)
    out["screen"] = {"seconds": S["seconds"], "au_seconds": S_au["seconds"]}
    out["rows"], out["rows_au"] = S["rows"], S_au["rows"]
    out["base"] = S["base"]
    out["table"] = aggregate(S["rows"])
    out["survivors"] = survivors(S["rows"])
    out["survivors_au"] = survivors(S_au["rows"])
    out["load_bearing"] = load_bearing(S["rows"])
    out["load_bearing_au"] = load_bearing(S_au["rows"])
    out["clash_census"] = clash_census(S["rows"])
    out["premise_census"] = premise_census(S["rows"])
    out["premise_census_au"] = premise_census(S_au["rows"])
    out["wave1_clash_census"] = wave1_clash_census()
    ex = exercised(S)
    ex_au = exercised_cells(S_au, S)
    for h in LIT_NAMES:
        ex[h]["at 1 AU (W2 variants)"] = {k: ex_au[h][k] for k in ("changed_by_h", "in_a_support", "what_changes")}
        if ex[h]["status"] != "EXERCISED" and ex_au[h]["changed_by_h"]:
            ex[h]["status"] = "EXERCISED (at 1 AU only)"
    out["exercised"] = ex
    out["named_census"] = named_census(S)
    out["named_census_au"] = named_census(S_au)
    out["rule2"] = rule2(S, S_au, ex)
    if with_tests:
        g = ground_checks()
        out["grounds"] = g
        out["grounds_ok"] = grounds_ok(g)
        out["tests"], out["cover"] = complementary_tests(S, S_au)
    u1, l1 = untested(S["rows"], CELL_MAIN)
    u2, l2 = untested(S_au["rows"], CELL_AU)
    out["untested"] = {CELL_MAIN: u1, CELL_AU: u2}
    out["untested_list"] = l1 + l2
    out["_S"], out["_S_au"] = S, S_au
    return out


def _fmt(x):
    return json.dumps(x, default=str)


def best_variants(rows):
    cons = [r for r in rows if r["consistent"]]
    m = max(len(five_view(r)) for r in cons)
    top = [r for r in cons if len(five_view(r)) == m]
    m2 = max(len(counts(r)) for r in top)
    return m, [r for r in top if len(counts(r)) == m2]


def report(R):
    if R["refused"]:
        print("REFUSED: a guard failed.\nvacuity:", _fmt(R["vacuity"]), "\ndrift:", _fmt(R["drift"])[:4000],
              "\ncontrols:", _fmt(R["drift_controls"]))
        return
    rows = R["rows"]
    cons = [r for r in rows if r["consistent"]]
    print(f"DOCKET 68 / B-combine (wave 2).  {len(rows)} variants over {len(R['table'])} combinations (127 + "
          f"readings-only) at {CELL_MAIN}; consistent {len(cons)}, inconsistent {len(rows) - len(cons)}; "
          f"z3 {R['screen']['seconds']:.1f} s.  At {CELL_AU}: {len(R['rows_au'])} W2 "
          f"variants re-screened.")
    d = R["drift"]
    print(f"\nDRIFT GUARD: z3 agrees with the A-reports' own grade text on {d['agree']} of {d['compared']} "
          f"(variant, obstruction) comparisons; disagreements, each explained: {len(d['explained_used'])}")
    for k in d["explained_used"]:
        print("   ", k, "--", EXPLAINED[k][:150])
    print("CONTROLS (mutated encodings caught):", _fmt({k: v["caught"] for k, v in R["drift_controls"].items()}))
    print("VACUITY:", _fmt(R["vacuity"]["known_contradictions_caught"]))
    print("STRUCTURAL (cannot fail, not evidence):", _fmt(R["vacuity"]["STRUCTURAL"]))
    cc = R["clash_census"]
    print("\nCLASHES (every minimal core; inclusion-exclusion):", _fmt(cc["families"]),
          "| variants with >1 core:", cc["variants_with_more_than_one_core"])
    print("PREMISE CLASHES at", CELL_MAIN, _fmt(R["premise_census"]))
    print("PREMISE CLASHES at", CELL_AU, "(W2 variants)", _fmt(R["premise_census_au"]))
    print("WAVE 1 clash census, recomputed:", _fmt(R["wave1_clash_census"]))
    m, top = best_variants(rows)
    print(f"\nMOST REMOVED OR NOT-BOUND (five-way) in a consistent variant: {m} of 5; {len(top)} variants attain it, "
          f"e.g. {top[0]['present']}")
    for o, v in top[0]["per"].items():
        print(f"    {o:12s} {v['verdict']:13s} " + _fmt({k: v[k] for k in v if k != 'verdict'})[:300])
    print("\nSURVIVORS", CELL_MAIN, _fmt(R["survivors"]))
    print("SURVIVORS", CELL_AU, _fmt(R["survivors_au"]))
    print("LOAD-BEARING", R["load_bearing"], "| at 1 AU", R["load_bearing_au"])
    print("\nEXERCISED (difference census):")
    for h, v in R["exercised"].items():
        print(f"   {h:6s} {v['status']:26s} changed in {v['changed_by_h']}/{v['variants_with_h']}; in a support "
              f"{v['in_a_support']}; {v['what_changes']} | 1 AU: {v['at 1 AU (W2 variants)']}")
    print("NAMED premises:", _fmt(R["named_census"]))
    print("\nRULE 2:")
    for h, v in R["rule2"].items():
        print(f"   {h:6s} {v['rule2']}")
    syn = {}
    for r in rows + R["rows_au"]:
        if r.get("synergy"):
            k = (r["cell"], tuple(r["synergy"]), tuple(r["contributors"]))
            syn[k] = syn.get(k, 0) + 1
    print("\nSYNERGY:", syn)
    itf = {}
    for r in rows + R["rows_au"]:
        if r.get("interference"):
            k = (r["cell"], tuple(r["interference"]), tuple(r.get("interference_causes", [])))
            itf[k] = itf.get(k, 0) + 1
    print("INTERFERENCE (a member's removal undone in combination; cause = the literal whose removal restores it):")
    for k, v in sorted(itf.items(), key=lambda kv: -kv[1]):
        print(f"  {v:5d}  {k}")
    if "tests" in R:
        print("\nGROUNDS:", R["grounds_ok"])
        print("\nCOMPLEMENTARY CLASSES -> tests:")
        for k, v in R["cover"].items():
            print(f"  {k:80s} {v}")
        for k, v in R["tests"].items():
            vv = {kk: vv for kk, vv in v.items() if kk != "rows"}
            print(f"\n  {k}: {_fmt(vv)[:1600]}")
            if "rows" in v:
                for row in v["rows"]:
                    print("     ", {kk: (round(vv, 6) if isinstance(vv, float) else vv) for kk, vv in row.items()})
    print("\nNOT TESTED BY INSTRUMENT (variants, by reason):", _fmt(R["untested"]))


ABBR = {"H-IT": "IT", "H-SETTLE": "SET", "H-FRAME": "FR", "H-12": "12", "H-INFO": "INF", "H-ZERO": "ZER",
        "H-NULL": "NUL"}
SH = {"O-BITS": "BITS", "O-MAKE-TOPO": "TOPO", "O-MAKE-DIST": "DIST", "O-HOLD": "HOLD", "O-MATTER": "MATTER",
      "O-LOOP": "LOOP"}
VSH = {"REMOVED": "R", "REMOVED-IF": "R-IF", "NOT-BOUND": "NB", "NOT-BOUND-IF": "NB-IF", "OPEN": "OPEN",
       "SILENT": "S", "LEFT": "L"}


def markdown_table(R):
    by = {}
    for r in R["rows"]:
        by.setdefault(tuple(r["combo"]) or ("(readings only)",), []).append(r)
    au = {}
    for r in R["rows_au"]:
        au.setdefault(tuple(r["combo"]) or ("(readings only)",), []).append(r)
    out = ["| # | combination | variants | consistent | clash (literals in core) | premise clashes | best consistent "
           "variant: BITS/TOPO/DIST/HOLD/MATTER/LOOP | five-way removed or not-bound | complementary | 1 AU: W2 "
           "variants with O-BITS removed |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for i, t in enumerate(R["table"], 1):
        key = tuple(t["combo"])
        name = "+".join(ABBR.get(h, h) for h in key)
        cl = "; ".join(t["clashes"]) or "-"
        pc = "; ".join(t["premise_clashes"]) or "-"
        best = "/".join(VSH[t["best"][o]] for o in OBST) if t["best"] else "-"
        bv = ",".join(t["best_variant"] or [])
        lst = au.get(key, [])
        a = sum(1 for r in lst if r["consistent"] and r["per"]["O-BITS"]["verdict"] in RMV)
        acol = f"{a}/{len(lst)}" if lst else "-"
        out.append(f"| {i} | {name} | {t['variants']} | {t['consistent']} | {cl} | {pc} | {best} ({bv}) | "
                   f"{','.join(x.replace('O-', '') for x in t['best_five']) or 'none'} | {t['complementary_variants']} "
                   f"| {acol} |")
    return "\n".join(out) + "\n"


def selftest():
    t0 = time.time()
    checks = []

    def ck(name, cond, detail=""):
        checks.append((name, bool(cond), detail))

    R = run_all(with_tests=True)
    ck("guards did not refuse", not R["refused"])
    if R["refused"]:
        for n, c, d in checks:
            print(("PASS " if c else "FAIL ") + n, d)
        print(_fmt({k: v for k, v in R.items() if k in ("vacuity", "drift_controls")})[:3000])
        print(_fmt(R["drift"]["unexplained"])[:3000], R["drift"].get("ground_rows"))
        return 1
    V, D = R["vacuity"], R["drift"]
    ck("VACUITY board alone SAT", V["board_alone_sat"])
    ck("VACUITY each single reading SAT (INFOS excepted: a clash, below)", all(V["each_single_reading_sat"].values()))
    ck("VACUITY named premises jointly SAT with the board at 1 ly", V["named_jointly_sat_with_board (1 ly)"])
    ck("CONTENT named premises jointly UNSAT with the board at 1 AU (N_EPS excluded)",
       V["named_jointly_UNSAT_with_board (1 AU: N_EPS excluded)"])
    ck("VACUITY named + OPEN jointly SAT with the board", V["all_named_and_open_sat_with_board"])
    for k, v in V["known_contradictions_caught"].items():
        ck("CONTROL contradiction caught: " + k, v)
    ck("RESULT F1 & F2b consistent as commitments", V["F1 & F2b consistent as commitments (wave 1 called this M's "
                                                       "sentence contradicting itself)"])
    ck("RESULT ITB & RI & RQ consistent as commitments", V["ITB & RI & RQ consistent as commitments (wave 1's clash b "
                                                           "was B-THROAT's slip)"])
    ck("NON-TRIVIAL board admits a loop and no loop", V["board_admits_loop"] and V["board_admits_no_loop"])
    ck("CONTROL without B-RECV, O-MATTER becomes removable", V["CONTROL without_B_RECV_matter_removable"])
    ck("PROOF N_EPS occurs only in B-CAP and B-EPSWIN, and no CAP without W2 (so the 1 AU re-screen of W2 variants "
       "covers every variant N_EPS can reach)", V["N_EPS occurs only in"] == ["B-CAP", "B-EPSWIN"] and
       V["no CAP without W2 (z3)"])
    ck("CONTROL wave-1 engine at 1 AU reports 3 of 3 vacuous REMOVED-IF (the premise check has content)",
       V["CONTROL wave-1 engine at 1 AU: vacuous REMOVED-IF on O-BITS caught"] == 3)
    ck(f"DRIFT z3 vs A-reports: every disagreement explained ({D['agree']}/{D['compared']} agree)", not D["unexplained"],
       D["unexplained"])
    ck("DRIFT ground rows (settle.h12_carrier_case vs z3 at 1 AU)", D["ground_ok"], D["ground_rows"])
    for k, v in R["drift_controls"].items():
        ck(f"CONTROL mutated encoding '{k}' caught as an unexplained disagreement", v["caught"])
    rows = R["rows"]
    cons = [r for r in rows if r["consistent"]]
    ck("COVERAGE 4,607 variants screened ((4*4*3*3*8 - 1) * 4 + 3)", len(rows) == 4607, len(rows))
    ck("COVERAGE 127 combinations + readings-only", len(R["table"]) == 128, len(R["table"]))
    ck("COVERAGE every combination has >= 1 consistent variant", all(t["consistent"] >= 1 for t in R["table"]))
    cc = R["clash_census"]["families"]
    ck("CENSUS inclusion-exclusion union == inconsistent count", cc["union_by_ie"] == cc["union_direct"] ==
       R["clash_census"]["inconsistent"], (cc["union_by_ie"], R["clash_census"]["inconsistent"]))
    w1 = R["wave1_clash_census"]
    ck("HISTORY wave-1 clashes by inclusion-exclusion: (a) present 768, union 1,152 over 3,071",
       w1["variants"] == 3071 and w1["present"]["(a) F1+F2b"] == 768 and w1["union_by_ie"] == 1152 and
       w1["sole"]["(a) F1+F2b"] == 640, w1)
    clfams = set(cc["present"])
    ck("RESULT the unconditional clashes are exactly W2+ITE and INFOS (+ B-RECV), every core enumerated",
       clfams == {"W2 + ITE", "INFOS"}, sorted(clfams))
    m, top = best_variants(rows)
    ck("RESULT no consistent variant removes or makes NOT-BOUND all five", m < 5, m)
    sv = R["survivors"]
    ck("RESULT O-MATTER removed or not-bound in no consistent variant (both cells)",
       "O-MATTER" in sv["removed_or_not_bound_in_no_consistent_variant"] and
       "O-MATTER" in R["survivors_au"]["removed_or_not_bound_in_no_consistent_variant"])
    ck("RESULT O-MAKE-DIST removed or not-bound in no consistent variant; OPEN via N_VAC",
       "O-MAKE-DIST" in sv["removed_or_not_bound_in_no_consistent_variant"] and "O-MAKE-DIST" in sv["open_somewhere"])
    ck("RESULT O-HOLD and O-MAKE-TOPO are never REMOVED at 1 ly (only NOT-BOUND-IF)",
       {"O-HOLD", "O-MAKE-TOPO"} <= set(sv["removed_in_no_consistent_variant"]))
    w2itb = R["_S"]["by"][frozenset({"W2", "ITB"})]
    ck("RESULT {W2, ITB}: O-HOLD NOT-BOUND-IF without R-INDEX (the symmetric encoding)",
       w2itb["per"]["O-HOLD"]["verdict"] == "NOT-BOUND-IF")
    itbri = R["_S"]["by"][frozenset({"ITB", "RI"})]
    ck("RESULT {ITB, RI}: O-HOLD NOT-BOUND-IF with two supports ({N_QTOPO} and {RI, N_MEASPHYS}), never REMOVED",
       itbri["per"]["O-HOLD"]["verdict"] == "NOT-BOUND-IF" and
       sorted(tuple(s["named"]) for s in itbri["per"]["O-HOLD"]["supports"]) == [("N_MEASPHYS",), ("N_QTOPO",)])
    w2a = R["_S"]["by"][frozenset({"W2"})]
    ck("RESULT {W2} at 1 ly: O-BITS REMOVED-IF needs a preferred slicing (N_FRAME3b) and N_EPS",
       w2a["per"]["O-BITS"]["verdict"] == "REMOVED-IF" and
       all({"N_EPS", "N_FRAME3b"} <= set(s["named"]) for s in w2a["per"]["O-BITS"]["supports"]))
    ck("RESULT O-LOOP removed with no member in the board-alone variant (exact FRW, N_CORR)",
       R["base"]["per"]["O-LOOP"]["verdict"] == "REMOVED-IF" and
       any(set(s["named"]) == {"N_FRW", "N_CORR"} for s in R["base"]["per"]["O-LOOP"]["supports"]))
    ex = R["exercised"]
    ck("RESULT INFO (necessity) is UNTESTED-BY-SCREEN (difference census: changes nothing)",
       ex["INFO"]["status"] == "UNTESTED-BY-SCREEN")
    ck("RESULT H12 load-bearing at 1 AU (synergy W2 x H12), its support naming N_H12W",
       "H12" in R["load_bearing_au"][0] and "N_H12W" in R["load_bearing_au"][1])
    ck("RESULT ZERO and NULL exercised (O-HOLD OPEN via N_EQUIL with H-IT), load-bearing for no removal",
       ex["ZERO"]["status"] == "EXERCISED" and ex["NULL"]["status"] == "EXERCISED" and
       not ({"ZERO", "NULL"} & set(R["load_bearing"][0])))
    ok, tests = R["grounds_ok"]
    for k, v in tests.items():
        ck("GROUND " + k, v)
    for k, v in R["tests"].items():
        ck("TEST " + k, v["pass"])
    ck("COVERAGE every complementary class has a test", all(v["tests"] for v in R["cover"].values()),
       [k for k, v in R["cover"].items() if not v["tests"]])
    n_comp = sum(1 for r in cons if r.get("complementary"))
    ck("COVERAGE untested + complementary = all variants", sum(R["untested"][CELL_MAIN].values()) + n_comp == len(rows),
       (sum(R["untested"][CELL_MAIN].values()), n_comp))
    npass = sum(1 for _, c, _ in checks if c)
    for n, c, d in checks:
        print(("PASS " if c else "FAIL ") + n + (f"  [{d}]" if d not in ("", None) and not c else ""))
    print(f"\n{npass}/{len(checks)} checks pass, "
          f"{sum(1 for n, _, _ in checks if n.startswith('CONTROL'))} of them controls; "
          f"{len(V['STRUCTURAL'])} STRUCTURAL guard(s) reported, not counted; {time.time() - t0:.0f} s")
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    R = run_all(with_tests="--fast" not in sys.argv)
    if "--json" in sys.argv:
        p = sys.argv[sys.argv.index("--json") + 1]
        with open(p, "w") as f:
            json.dump({k: v for k, v in R.items() if not k.startswith("_")}, f, default=str, indent=1)
    if "--table" in sys.argv and not R["refused"]:
        p = sys.argv[sys.argv.index("--table") + 1]
        with open(p, "w") as f:
            f.write(markdown_table(R))
    report(R)
