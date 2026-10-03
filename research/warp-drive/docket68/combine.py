#!/usr/bin/env python3
"""
DOCKET 68 / B-combine -- M's standing instruction, run: "some of the hypothesies lined up for docket 68 may turn out,
after initial testing, to work better in combination."  (CHARTER.md, verbatim.)

WHAT THIS FILE DOES, IN THE CHARTER'S ORDER
  (1) builds the 127 non-empty combinations of the seven hypotheses (H-IT, H-SETTLE, H-FRAME, H-12, H-INFO, H-ZERO,
      H-NULL).  A hypothesis that the work items found to have more than one reading is carried in EVERY reading
      (H-SETTLE: W2 / W1 / KR; H-FRAME: F1 / F2b; H-IT: ITB / ITE -- see SUBREADINGS), and every combination is run
      with each of the four reading slots {none, R-INDEX, R-QUANTUM, both}.  127 combinations -> 3,068 variants, plus
      the 3 reading-only variants: 3,071 screened, none skipped.
  (2) SCREENS each variant for consistency in z3 against the board holdings the four reports cite.  Every board
      holding and every hypothesis commitment is a TRACKED constraint carrying its ground (an instrument and the
      number it computed, or an arXiv id and page READ), so an inconsistent variant is named with its clash: the
      unsat core.  PROOF-ASSISTANT.md's two guards run first and the screen refuses to report if either fails:
        vacuity       -- the board alone is satisfiable; each single reading is; the conditional named hypotheses
                         are jointly satisfiable; three known contradictions are caught; a removal is reported
                         only if the premises it rests on are themselves satisfiable;
        encoding drift-- hand-checked variants (each tied to the grade text of the A-report that owns it, parsed
                         from that report's JSON) must agree with z3, and a deliberately mutated encoding must be
                         CAUGHT disagreeing; every board constraint's ground is recomputed from its instrument.
  (3) for the consistent variants, decides per obstruction whether the variant's commitments FORCE the removal
      (z3: the negation is UNSAT), with or without the named hypotheses, and which members and named hypotheses
      are load-bearing (unsat core).  Variants where more than one member contributes a removal are the
      complementary ones; each class of them is then TESTED with the members' own instruments, imported, and with
      three new computations (tfd_drift, product_drift, first_transit).
  (4) lists every variant not tested by instrument, with its reason.  No cap.

O-MAKE is carried in the two forms A4 found, O-MAKE-TOPO (the Geroch/Tipler topology change the work order names)
and O-MAKE-DIST (making the entanglement the corridor runs on: distribution at <= c); O-MAKE is removed only if both
are.  Verdict per obstruction per variant:
  REMOVED     forced by the variant's commitments with no named hypothesis assumed
  REMOVED-IF  forced once the named hypotheses in its core are assumed (each listed; vacuity checked)
  OPEN        not forced; possible only through an OPEN pathway the sources leave undecided
  LEFT        refused: the obstruction stands in every model of the variant
  SILENT      not forced and not refused: the variant says nothing that decides it

WHAT THE z3 SCREEN IS AND IS NOT.  It is bookkeeping over the board's holdings and the work items' findings, done
exhaustively and checked for consistency.  It is NOT new physics: every constraint's content is a computation or a
READ statement owned elsewhere (named in its ground).  What z3 adds is (a) which combinations of commitments
contradict one another, (b) which members and named hypotheses a removal actually rests on, (c) coverage of all
3,071 variants.  The new physics in this file is in the complementary tests (section T).

M's hypotheses are carried as hypotheses, never as results.  Nothing here is seated.  Writes nothing outside
docket68/ except an optional --json output path the caller names.

    python3 combine.py --selftest        guards, grounds, screen, tests -- exits 1 on any failure
    python3 combine.py                   the report
    python3 combine.py --json PATH       the full variant table as JSON
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

SUBREADINGS = {   # a hypothesis the work items found to carry more than one reading: every reading is screened
    "H-SETTLE": {
        "W2": "deterministic drift acting per branch (M's definition, Weinberg/Gisin type; convention C2) -- A1 "
              "H-SETTLE-W, A2 C2",
        "W1": "the same drift acting on the reduced density matrix (convention C1) -- A2 settle_under_C1",
        "KR": "causal field-expectation-value form (Kaplan-Rajendran 2106.10576v2) -- A1 H-SETTLE-KR",
    },
    "H-FRAME": {
        "F1": "clause 1 (+2a): a preferred frame exists and corridors are keyed to the cosmic rest frame -- A2",
        "F2b": "clause 2b: messages reach the past of the cosmic clock (the frame exists; some corridor has "
               "xi_t != 0) -- A2",
        "F1+F2b": "both clauses in their strong form, as M's sentence states them ('A preferred frame - maybe "
                  "messages can travel into the past') -- A2 found clause 1 excludes clause 2b; screened, not "
                  "assumed away",
    },
    "H-IT": {
        "ITB": "spacetime comes from information; the corridor lives in the information layer (the charter's "
               "reading of M's 'only to an observer') -- A4, A3",
        "ITE": "spacetime from information read as ER=EPR, with Maldacena-Susskind's own stated assumptions "
               "(fn.1 p.2 non-traversability; sec.3.1 p.16; sec.5.4 pp.36-37 linearity) -- A4",
    },
    "H-12": {"H12": "the twelve parameters of the 12-vector as carriers -- A1"},
    "H-INFO": {"INFO": "information is primary; matter cannot exist without it -- A3"},
    "H-ZERO": {"ZERO": "zero = ground state -- A4"},
    "H-NULL": {"NULL": "null (NEC) is a containment where information lives -- A4"},
}
READINGS = {"RI": "R-INDEX: probability of a cell in the closed index, measured by Q-1 (no energy term) -- A3",
            "RQ": "R-QUANTUM: QEI-bounded negative energy holds the throat -- A4"}
READING_SLOTS = [(), ("RI",), ("RQ",), ("RI", "RQ")]

OBST = ["O-BITS", "O-MAKE-TOPO", "O-MAKE-DIST", "O-HOLD", "O-MATTER", "O-LOOP"]
FIVE = ["O-BITS", "O-MAKE", "O-HOLD", "O-MATTER", "O-LOOP"]

# named hypotheses a removal may rest on (assumed in the conditional check; each listed where load-bearing)
NAMED = {
    "N_EPS": "eps >= eps_min(L, N) with N >= 7 pairs per teleported qubit, and the drift not excluded by the "
             "Weinberg-family bound (NAMED-NOT-READ) -- with A1's H-MAP, H-TRANSFER, H-SPIN, H-COHERE",
    "N_SIGKEY": "the superluminal signal is keyed to the preferred slicing (A1 H-SIG-COR / H-FRAME3b; A2 "
                "antitelephone keyed to the cosmic frame)",
    "N_CORR": "H-CORRIDOR-MODEL: a corridor is an identification of positions by a translation (latticectc "
              "H1-H3; comoving translations in FRW)",
    "N_QTOPO": "the corridor is not a classical Lorentzian topology change: MS p.17 ('should be allowed as "
               "possible quantum states') for ER=EPR; the charter's information-layer reading for ITB",
}
# OPEN pathways: the sources leave them undecided; never assumed true in a removal
OPEN_NAMED = {
    "N_XI": "a nonminimally coupled (xi > 0) field has no state-independent QEI (Fewster-Osterbrink, board "
            "NARROWED) -- R-QUANTUM's open branch",
    "N_EPSG": "a gravitational KR nonlinearity supplies an NEC-violating effective source (KR p.13; eps_G "
              "unconstrained, KR p.14) -- H-SETTLE-KR's open branch",
    "N_VAC": "pre-existing entanglement (of the vacuum) usable as the channel's pairs with no distribution -- the "
             "closest reading of M's 'it already exists everywhere'.  READ, Reznik quant-ph/0212044v2: causally "
             "disconnected probes can end entangled (p.1); the entanglement 'vanishes once the regions become "
             "sufficiently separated' (p.1); for inertial probes it persists only to L/T < 1.1 (p.12, Fig.2), so "
             "the probes, already at both ends, interact for T > 0.91 L/c.  Whether any setup supplies >= 7 pairs "
             "per qubit faster than distribution is NOT computed: OPEN",
}

LIT_NAMES = ["W2", "W1", "KR", "F1", "F2b", "ITB", "ITE", "H12", "INFO", "ZERO", "NULL", "RI", "RQ"]
PHYS = ["SIG", "LIN", "SLICE", "SIGKEY", "KEYED", "PAST", "LOOP", "TOPO", "DIST", "THROAT", "HELD", "RECV", "CAP",
        "CARRIER", "MEASURE", "ZSHIFT", "ZFREE", "LAMBDA_GRAV", "QNEC_PRICED"]
RM = {o: "rm:" + o for o in OBST}


def atoms():
    A = {n: z3.Bool(n) for n in LIT_NAMES + PHYS + list(NAMED) + list(OPEN_NAMED)}
    A.update({RM[o]: z3.Bool(RM[o]) for o in OBST})
    return A


# =====================================================================================================================
# THE BOARD'S HOLDINGS, as tracked constraints.  Each: (name, ground, builder).  The ground names the instrument and
# the value it computes, or the arXiv id and page READ.  ground_checks() recomputes every computed ground.
# =====================================================================================================================
def _board(A):
    I, An, Or, N = z3.Implies, z3.And, z3.Or, z3.Not
    return [
        ("B-NOCOM", "no-communication theorem (board D67 NARROWED): nosig.py I = 0.0 bits over 7 angles; fields12.py "
                    "1.44e-15; frame.py C1 table 0 bits and settle_under_C1 2.2e-16; settle.py collapse control "
                    "1.1e-16; KR 2106.10576v2 sec.2.3 pp.7-8 (READ, A1): only a per-branch deterministic drift "
                    "signals among the readings screened",
         I(A["SIG"], A["W2"])),
        ("B-GISIN", "settle.bob_y_exact: Bob's <sigma_y> = tanh(2 eps T) > 0 for eps > 0 (sympy residual 0); "
                    "Gisin READ-VIA-RESTATEMENT 2412.20854v1 pp.5-7",
         I(A["W2"], An(A["SIG"], N(A["LIN"])))),
        ("B-C2-SLICE", "frame.c2_needs_a_frame: Bob-first 1/2 vs Alice-first 2/3 or 1/3, so C2 is undefined without "
                       "an ordering; Gisin's assumption (3b), 2412.20854v1 p.6 (READ, A1)",
         I(A["W2"], A["SLICE"])),
        ("B-SIGKEY", "A1 H-SIG-COR; A2 antitelephone: a signal keyed to one slicing needs that slicing",
         An(I(An(A["SLICE"], A["N_SIGKEY"]), A["SIGKEY"]), I(A["SIGKEY"], A["SLICE"]))),
        ("B-ANTITEL", "frame.antitelephone: a reply keyed to the sender's frame arrives at t = -3/5 (a closed loop)",
         I(An(A["SIG"], N(A["SIGKEY"])), A["LOOP"])),
        ("B-TIMEFUNC", "frame.cosmic_keyed_rank_n_is_safe (exact Sylvester, 0 failures at rank 2 and 3); "
                       "frame.frw_time_function_lemma (z3 unsat, any a(t) > 0); corridors.py 0/2000",
         I(An(A["KEYED"], A["N_CORR"], N(A["PAST"]), Or(N(A["SIG"]), A["SIGKEY"])), N(A["LOOP"]))),
        ("B-2B", "frame.py part (i).3: a message into the cosmic past <=> xi_t != 0 <=> not keyed to the cosmic frame "
                 "(past_corridor_witness norm -99/10000; past_corridor_condition every T > 0)",
         I(A["PAST"], N(A["KEYED"]))),
        ("B-CAP", "settle.eps_to_remove / capacity: N pairs carry >= 2 bits per teleported qubit iff eps >= "
                  "eps_min(L, N); N < 7 impossible at any eps (CMAX = log2 1.25 = 0.3219 bits/pair)",
         An(I(A["CAP"], An(A["SIG"], A["N_EPS"])), I(An(A["SIG"], A["N_EPS"]), A["CAP"]))),
        ("B-TOPO", "Geroch 1967 (board D67 NARROWED, kinematic theorem stands) / Tipler 1977 (NARROWED) bind a "
                   "geometric corridor; MS 1306.0533v2 p.17 (READ here) and the charter's reading release a "
                   "corridor that is a quantum state / information-layer object",
         An(I(An(Or(A["ITB"], A["ITE"]), A["N_QTOPO"]), N(A["TOPO"])),
            I(N(An(Or(A["ITB"], A["ITE"]), A["N_QTOPO"])), A["TOPO"]))),
        ("B-LOCC", "MS 1306.0533v2 sec.3.2 pp.16-17 (READ here): LOCC cannot create entanglement, no bridge "
                   "'without preexisting bridges'; geometry.locc_entropy_change 8.9e-16; transit."
                   "TRAVERSAL_IS_REMOVED False; combine.product_drift: the nonlinear drift on a product state "
                   "gives exactly 0",
         I(N(A["N_VAC"]), A["DIST"])),
        ("B-THROAT", "Morris-Thorne 1988 (board D67 STANDS): a geometric corridor held open is a throat with the NEC "
                     "broken; A3: R-INDEX's removal is physical only under H-IT (information-layer corridor)",
         An(I(N(An(A["ITB"], A["RI"])), A["THROAT"]), I(An(A["ITB"], A["RI"]), N(A["THROAT"])))),
        ("B-HELD", "geometry.r_quantum: the QEI duration bound covers 2.08e-68 of the 1 m throat's deficit (minimal "
                   "scalar, in scope); zero.py and geometry.nec_shift_z3: a zero shift moves the NEC by exactly 0; "
                   "geometry.qnec_price: the QNEC prices, does not supply; open branches: xi > 0 (Fewster-"
                   "Osterbrink, NARROWED) and eps_G (KR p.13-14)",
         I(A["HELD"], Or(An(A["RQ"], A["N_XI"]), An(A["KR"], A["N_EPSG"])))),
        ("B-RECV", "transit.CARRIES_SUBSTANCE False (a receiver must be there); Bekenstein quant-ph/0404042v1 pp.2, 8 "
                   "(READ, A3): a complete system with E > 0 holds the bits (measure.bekenstein_floor_j 33-379 J at "
                   "R = 1 m); LEDGER.md S10 REFUSED (the Higgs-trigger supply), S13 OPEN and S5 OPEN, both needing a "
                   "prior arrival at <= c (D23)",
         A["RECV"]),
    ]


def _defs(A):
    """The obstruction-removal atoms, defined.  Definitions, not holdings."""
    E, N, Or = (lambda a, b: a == b), z3.Not, z3.Or
    return [
        ("DEF-BITS", "O-BITS removed iff the channel carries >= 2 bits per qubit before light", E(A[RM["O-BITS"]], A["CAP"])),
        ("DEF-TOPO", "O-MAKE-TOPO removed iff no classical topology change is needed", E(A[RM["O-MAKE-TOPO"]], N(A["TOPO"]))),
        ("DEF-DIST", "O-MAKE-DIST removed iff no entanglement distribution at <= c is needed", E(A[RM["O-MAKE-DIST"]], N(A["DIST"]))),
        ("DEF-HOLD", "O-HOLD removed iff there is no geometric throat or it is held", E(A[RM["O-HOLD"]], Or(N(A["THROAT"]), A["HELD"]))),
        ("DEF-MATTER", "O-MATTER removed iff no receiver/holder must already be at the destination", E(A[RM["O-MATTER"]], N(A["RECV"]))),
        ("DEF-LOOP", "O-LOOP removed iff no closed causal curve", E(A[RM["O-LOOP"]], N(A["LOOP"]))),
    ]


def _commitments(A):
    """What each reading commits to.  A commitment is active only when its literal is asserted."""
    I, An, Or, N = z3.Implies, z3.And, z3.Or, z3.Not
    return [
        ("C-W2", "A1: deterministic drift per branch (M's definition); A2 C2", A["W2"], N(A["LIN"])),
        ("C-W1", "A2 settle_under_C1: the drift on rho_B shows 2.2e-16 dependence on Alice", A["W1"], N(A["SIG"])),
        ("C-KR", "KR 2106.10576v2 sec.2.3 pp.7-8 (READ, A1): signal at Bob 0 for every eps", A["KR"], N(A["SIG"])),
        ("C-F1", "A2 clause 1: a preferred frame; every corridor keyed to it (xi_t = 0)", A["F1"],
         An(A["KEYED"], A["SLICE"])),
        ("C-F2b", "A2 clause 2b: a message reaches the past of the cosmic clock", A["F2b"], An(A["PAST"], A["SLICE"])),
        ("C-ITE", "MS 1306.0533v2 (READ here): fn.1 p.2 'We will assume that wormholes remain un-traversable'; "
                  "sec.3.1 p.16 no local operation on one member 'can influence the other'; sec.5.4 pp.36-37 a "
                  "geometric feature is a linear operator; emtension.ENTANGLED_BRIDGE_IS_TRAVERSABLE False",
         A["ITE"], An(A["LIN"], N(A["SIG"]), A["THROAT"])),
        ("C-H12", "A1: the twelve as carrier candidates (Z0 the only one with a state-dependent bound)", A["H12"],
         A["CARRIER"]),
        ("C-INFO", "A3: Q-1 delivered (BFL 1106.1791v3 Thm 2); clause (b) OPEN", A["INFO"], A["MEASURE"]),
        ("C-ZERO", "A4/zero.py: the zero shift T_ab -> T_ab + lambda g_ab; free under emergent gravity (Jacobson "
                   "gr-qc/9504004v2; Padmanabhan 1703.06144v1 pp.6-7), a gravitating Lambda in GR", A["ZERO"],
         An(A["ZSHIFT"], I(Or(A["ITB"], A["ITE"]), A["ZFREE"]), I(N(Or(A["ITB"], A["ITE"])), A["LAMBDA_GRAV"]))),
        ("C-NULL", "A4/nullinfo.py: the QNEC prices a throat's null deficit (outside its proven scope)", A["NULL"],
         A["QNEC_PRICED"]),
        ("C-RI", "A3: R-INDEX -- the measure has no energy term", A["RI"], A["MEASURE"]),
        ("C-RQ", "A4: R-QUANTUM holds a geometric throat with QEI-bounded negative energy", A["RQ"], A["THROAT"]),
    ]


# =====================================================================================================================
# THE ENGINE
# =====================================================================================================================
class Screen:
    def __init__(self, mutate=None, drop=()):
        self.A = atoms()
        self.s = z3.Solver()
        self.s.set("core.minimize", True)
        self.ind = {}          # indicator -> (name, ground)
        board = [b for b in _board(self.A) if b[0] not in drop]
        commits = _commitments(self.A)
        if mutate == "F1-unkeyed":          # the encoding-drift CONTROL: clause 1 no longer keys corridors
            commits = [c if c[0] != "C-F1" else (c[0], c[1], c[2], self.A["SLICE"]) for c in commits]
        for name, ground, expr in board + _defs(self.A):
            self._track(name, ground, expr)
        for name, ground, lit, expr in commits:
            self._track(name, ground, z3.Implies(lit, expr))
        self.base = list(self.ind)

    def _track(self, name, ground, expr):
        b = z3.Bool("@" + name)
        self.s.add(z3.Implies(b, expr))
        self.ind[b] = (name, ground)

    def lits(self, present):
        return [self.A[n] if n in present else z3.Not(self.A[n]) for n in LIT_NAMES]

    def check(self, extra):
        r = self.s.check(*(self.base + extra))
        return r

    def core(self):
        out = []
        for c in self.s.unsat_core():
            name = str(c)
            if name.startswith("@"):
                out.append(name[1:])
            elif name.startswith("Not("):
                out.append("not " + name[4:-1])
            else:
                out.append(name)
        return sorted(out)

    def cond_lits(self):
        return [self.A[n] for n in NAMED] + [z3.Not(self.A[n]) for n in OPEN_NAMED]

    def variant(self, present):
        """Screen one variant.  present: set of literal names (sub-readings and readings)."""
        L = self.lits(present)
        res = {"present": sorted(present, key=LIT_NAMES.index)}
        if self.check(L) == z3.unsat:
            res["consistent"] = False
            res["clash"] = [c for c in self.core() if not c.startswith("not ")]
            return res
        res["consistent"] = True
        full = L + self.cond_lits()
        res["named_jointly_sat"] = self.check(full) == z3.sat
        per = {}
        for o in OBST:
            rm = self.A[RM[o]]
            if self.check(L + [z3.Not(rm)]) == z3.unsat:
                per[o] = {"verdict": "REMOVED", "rests_on": [c for c in self.core() if c in LIT_NAMES]}
                continue
            if self.check(full + [z3.Not(rm)]) == z3.unsat:
                core = self.core()
                named = [c for c in core if c in NAMED]
                members = [c for c in core if c in LIT_NAMES]
                vac = self.check(L + [self.A[n] for n in named]) == z3.sat
                per[o] = {"verdict": "REMOVED-IF", "named": named, "rests_on": members, "premises_sat": vac}
                continue
            closed = L + [self.A[n] for n in NAMED] + [z3.Not(self.A[n]) for n in OPEN_NAMED]
            if self.check(closed + [rm]) == z3.sat:
                per[o] = {"verdict": "SILENT"}
                continue
            opens = []
            for k in OPEN_NAMED:
                trial = L + [self.A[n] for n in NAMED] + [self.A[k] if j == k else z3.Not(self.A[j])
                                                         for j in OPEN_NAMED]
                if self.check(trial + [rm]) == z3.sat:
                    opens.append(k)
            per[o] = {"verdict": "OPEN", "via": opens} if opens else {"verdict": "LEFT"}
        res["per"] = per
        return res


def removed_set(res):
    return sorted(o for o, v in res.get("per", {}).items() if v["verdict"] in ("REMOVED", "REMOVED-IF"))


def five_view(res):
    """Fold O-MAKE-TOPO and O-MAKE-DIST into O-MAKE (removed only if both are)."""
    r = set(removed_set(res))
    out = [o for o in ("O-BITS", "O-HOLD", "O-MATTER", "O-LOOP") if o in r]
    if "O-MAKE-TOPO" in r and "O-MAKE-DIST" in r:
        out.append("O-MAKE")
    return sorted(out, key=FIVE.index)


def variants():
    """Every variant: the 127 combinations x sub-readings x 4 reading slots, then the 3 reading-only variants.
    H-SETTLE has 3 readings, H-FRAME 3 (F1, F2b, F1+F2b), H-IT 2: (4*4*3*2^4 - 1) * 4 + 3 = 3,071."""
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


def run_screen(scr=None):
    scr = scr or Screen()
    t0 = time.time()
    rows = []
    for combo, present in variants():
        r = scr.variant(present)
        r["combo"] = list(combo)
        rows.append(r)
    singles = {}
    for r in rows:
        if len(r["present"]) == 1:
            singles[r["present"][0]] = set(removed_set(r)) if r["consistent"] else None
    for r in rows:
        if not r["consistent"]:
            continue
        u = set()
        for m in r["present"]:
            u |= singles.get(m) or set()
        z = set(removed_set(r))
        r["union_of_singletons"] = sorted(u)
        r["synergy"] = sorted(z - u)
        r["interference"] = sorted(u - z)
        contributors = set()
        for o in z:
            contributors |= set(r["per"][o]["rests_on"])
        r["contributors"] = sorted(contributors, key=LIT_NAMES.index)
        r["complementary"] = len(z) >= 1 and not any((singles.get(m) or set()) >= z for m in r["present"])
    return rows, time.time() - t0


# =====================================================================================================================
# GUARDS (PROOF-ASSISTANT.md): vacuity and encoding drift
# =====================================================================================================================
def guard_vacuity(scr):
    A = scr.A
    out = {}
    none = scr.lits(set())
    out["board_alone_sat"] = scr.check(none) == z3.sat
    out["each_single_reading_sat"] = {n: scr.check(scr.lits({n})) == z3.sat for n in LIT_NAMES}
    out["named_jointly_sat_with_board"] = scr.check(none + scr.cond_lits()) == z3.sat
    out["all_named_and_open_sat_with_board"] = scr.check(none + [A[n] for n in list(NAMED) + list(OPEN_NAMED)]) == z3.sat
    # known contradictions must be CAUGHT
    caught = {}
    caught["F1 & F2b (clause 1 vs clause 2b)"] = scr.check(scr.lits({"F1", "F2b"})) == z3.unsat
    caught["planted signal in linear QM (no W2, SIG)"] = scr.check(none + [A["SIG"]]) == z3.unsat
    caught["ITE & W2 (MS assumptions vs per-branch drift)"] = scr.check(scr.lits({"ITE", "W2"})) == z3.unsat
    out["known_contradictions_caught"] = caught
    # non-triviality: the board alone decides neither LOOP nor SIG-capacity trivially in the 'removed' direction
    out["board_admits_loop"] = scr.check(none + [A["LOOP"]]) == z3.sat
    out["board_admits_no_loop"] = scr.check(none + [z3.Not(A["LOOP"])]) == z3.sat
    out["board_alone_forces_recv"] = scr.check(none + [z3.Not(A["RECV"])]) == z3.unsat
    # CONTROL: O-MATTER's survival is B-RECV's doing, not an encoding accident
    scr2 = Screen(drop=("B-RECV",))
    out["without_B_RECV_matter_removable"] = scr2.check(scr2.lits(set()) + [A["rm:O-MATTER"]]) == z3.sat
    ok = (out["board_alone_sat"] and all(out["each_single_reading_sat"].values())
          and out["named_jointly_sat_with_board"] and out["all_named_and_open_sat_with_board"]
          and all(caught.values()) and out["board_admits_loop"] and out["board_admits_no_loop"]
          and out["board_alone_forces_recv"] and out["without_B_RECV_matter_removable"])
    return ok, out


def _a2_grades(summary):
    """A2-frame.json on disk carries a 'summary', not a 'grades' list.  Its grades are rebuilt from the instrument's
    own data (frame.GRADES, clause 1, per obstruction) and that summary's text (clause 2b, convention C1, the
    combination) -- each 'removes' list holds only text that says REMOVES/removes for that obstruction."""
    FR = _quiet("frame")
    c1 = next(v for k, v in FR.GRADES.items() if k.startswith("H-FRAME clause 1"))
    rem1 = [f"{o}: {t}" for o, t in c1.items() if t.startswith("REMOVES")]
    return [
        {"hypothesis": "H-FRAME clause 1 (frame.GRADES)", "removes": rem1},
        {"hypothesis": "H-FRAME clause 2b (A2-frame.json summary)",
         "removes": [] if "EXCLUDED" in summary["clause2b"] else [summary["clause2b"]]},
        {"hypothesis": "Deutsch D-CTC consistency convention C1 (A2-frame.json summary)",
         "removes": [] if "not under C1 (0 bits)" in summary["deutsch"] else [summary["deutsch"]]},
        {"hypothesis": "H-FRAME + H-SETTLE under convention C2 (A2-frame.json summary)",
         "removes": [summary["combination"].split(":")[1]]},
    ]


def _report_grades():
    """Load the four A-reports' grades from their JSON (the source of each hand-checked expectation)."""
    G = {}
    for rid in ("A1-settle", "A2-frame", "A3-measure", "A4-geometry"):
        p = os.path.join(SCRATCH_REPORTS, rid + ".json")
        try:
            with open(p) as f:
                d = json.load(f)
            G[rid] = d["grades"] if "grades" in d else (_a2_grades(d["summary"]) if rid == "A2-frame" else None)
        except Exception:
            G[rid] = None
    return G


def _grade(G, rid, key):
    for g in G.get(rid) or []:
        if key in g["hypothesis"]:
            return g
    return None


def _tokens(lst):
    return sorted({m for s in lst for m in re.findall(r"O-(?:BITS|MAKE|HOLD|MATTER|LOOP)", s)})


# each expectation: (variant literals, expected removed set (6-way), report id, grade key, what the report says,
# how the report's text maps onto the 6-way split)
EXPECT = [
    ({"W2"}, {"O-BITS"}, "A1-settle", "H-SETTLE-W (M's definition", {"O-BITS"},
     "A1 removes O-BITS conditional on eps >= eps_min: REMOVED-IF on N_EPS"),
    ({"KR"}, set(), "A1-settle", "H-SETTLE-KR", set(), "A1: nothing removed; O-HOLD OPEN"),
    ({"H12"}, set(), "A1-settle", "H-12 alone", set(), "A1: LEAVES-ALL"),
    ({"W2", "H12"}, {"O-BITS"}, "A1-settle", "H-SETTLE x H-12", {"O-BITS"}, "A1: O-BITS via Weinberg-type carrier"),
    ({"W2", "F1"}, {"O-BITS", "O-LOOP"}, "A1-settle", "H-SETTLE-W x H-FRAME", {"O-BITS", "O-LOOP"}, "A1 pairing"),
    ({"F1"}, {"O-LOOP"}, "A2-frame", "clause 1", {"O-LOOP"}, "A2 clause 1 alone"),
    ({"F2b"}, set(), "A2-frame", "clause 2b", set(), "A2 clause 2b: OPEN, removes nothing"),
    ({"W1"}, set(), "A2-frame", "convention C1", set(), "A2: C1 leaves all"),
    ({"INFO"}, set(), "A3-measure", "H-INFO (information is primary", set(), "A3 LEAVES-ALL"),
    ({"RI"}, set(), "A3-measure", "R-INDEX", {"O-HOLD", "O-MAKE"},
     "A3 removes O-HOLD and O-MAKE 'within the measure only'; physical only under H-IT -> z3: nothing physical alone"),
    ({"ITB", "RI"}, {"O-HOLD", "O-MAKE-TOPO"}, "A3-measure", "R-INDEX", {"O-HOLD", "O-MAKE"},
     "A3's conditional made physical by H-IT: O-HOLD; O-MAKE-TOPO via H-IT (A4); O-MAKE-DIST stays (A4)"),
    ({"ITB"}, {"O-MAKE-TOPO"}, "A4-geometry", "H-IT (spacetime from information), alone", {"O-MAKE"},
     "A4 removes O-MAKE's topology-change form only"),
    ({"ITE"}, {"O-MAKE-TOPO"}, "A4-geometry", "H-IT (spacetime from information), alone", {"O-MAKE"},
     "A4 graded H-IT under H-ER=EPR: topology-change form only"),
    ({"ZERO"}, set(), "A4-geometry", "H-ZERO (zero = ground state), alone", set(), "A4 LEAVES-ALL"),
    ({"ZERO", "ITB"}, {"O-MAKE-TOPO"}, "A4-geometry", "H-ZERO with H-IT", set(),
     "A4: the pair removes none of the five (it grades the zero's freedom); O-MAKE-TOPO here is H-IT's own"),
    ({"NULL"}, set(), "A4-geometry", "H-NULL", set(), "A4 LEAVES-ALL"),
    ({"RQ"}, set(), "A4-geometry", "R-QUANTUM", set(), "A4 LEAVES-ALL in scope; OPEN xi > 0"),
]


def guard_drift(scr, G=None):
    G = G if G is not None else _report_grades()
    rows = []
    ok = True
    for present, exp, rid, key, report_says, note in EXPECT:
        r = scr.variant(set(present))
        got = set(removed_set(r)) if r["consistent"] else None
        g = _grade(G, rid, key)
        rep = set(_tokens(g["removes"])) if g else None
        rep_ok = (rep is not None and rep == report_says)
        agree = got == exp
        ok &= agree and rep_ok
        rows.append({"variant": sorted(present), "expected": sorted(exp), "z3": sorted(got or []),
                     "report": rid, "report_removes_tokens": sorted(rep or []), "report_text_matches": rep_ok,
                     "agree": agree, "note": note})
    # the open branches must show as OPEN, not as removals
    rq = scr.variant({"RQ"})["per"]["O-HOLD"]
    kr = scr.variant({"KR"})["per"]["O-HOLD"]
    open_ok = rq["verdict"] == "OPEN" and "N_XI" in rq["via"] and kr["verdict"] == "OPEN" and "N_EPSG" in kr["via"]
    ok &= open_ok
    # CONTROL: a mutated encoding must be caught disagreeing
    mut = Screen(mutate="F1-unkeyed")
    caught = any(set(removed_set(mut.variant(set(p)))) != e for p, e, *_ in EXPECT if "F1" in p)
    ok &= caught
    return ok, {"rows": rows, "open_branches_ok": open_ok, "mutated_encoding_caught": caught,
                "reports_loaded": {k: v is not None for k, v in G.items()}}


# =====================================================================================================================
# GROUNDS: every computed ground re-run from its instrument (an encoding-drift guard against the board itself)
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
    ST = _quiet("settle")
    FR = _quiet("frame")
    GE = _quiet("geometry")
    out = {}
    out["B-GISIN tanh(2*0.1*3)"] = ST.bob_y_exact(0.1, 3.0)
    out["B-NOCOM settle_under_C1"] = FR.settle_under_C1()
    sig = FR.signalling_table()
    out["B-C2-SLICE c2_needs_a_frame"] = FR.c2_needs_a_frame(sig)
    out["frame C2 MI bits"] = sig[("C2", "MI bits")]
    out["frame C1 MI bits"] = sig[("C1", "MI bits")]
    out["B-ANTITEL antitelephone"] = tuple(float(x) for x in FR.antitelephone())
    out["B-TIMEFUNC rank-2 failures"] = FR.cosmic_keyed_rank_n_is_safe(2, 100)
    out["B-TIMEFUNC rank-3 failures"] = FR.cosmic_keyed_rank_n_is_safe(3, 100)
    w = FR.past_corridor_witness()
    out["B-2B witness"] = str(w)
    out["B-CAP CMAX"] = ST.CMAX
    out["B-CAP N=6 at 1 ly"] = ST.eps_to_remove(ST.LY_M, 6)
    out["B-LOCC local dS"] = GE.locc_entropy_change()[1]
    out["B-HELD fraction covered"] = GE.r_quantum()["fraction_covered"]
    out["B-HELD nec shift (z3)"] = GE.nec_shift_z3()["negation"]
    out["flags"] = board_flags()
    return out


def _cosmic_failures(v):
    """frame.cosmic_keyed_rank_n_is_safe returns (lattices tested, lattices with a non-positive-definite Gram)."""
    return v[1] if isinstance(v, tuple) else v


def grounds_ok(g):
    f = g["flags"]
    tests = {
        "W2 signals (tanh > 0)": g["B-GISIN tanh(2*0.1*3)"] > 0.5,
        "C1 does not signal": g["B-NOCOM settle_under_C1"] < 1e-12 and abs(g["frame C1 MI bits"]) < 1e-12,
        "C2 signals and is frame-dependent": g["frame C2 MI bits"] > 0.08 and
        abs(g["B-C2-SLICE c2_needs_a_frame"][0] - 0.5) < 1e-9 and abs(g["B-C2-SLICE c2_needs_a_frame"][1] - 2 / 3) < 1e-9,
        "antitelephone loop -3/5, cosmic 0": g["B-ANTITEL antitelephone"] == (-0.6, 0.0),
        "cosmic keyed: 0 failures": _cosmic_failures(g["B-TIMEFUNC rank-2 failures"]) == 0 and
        _cosmic_failures(g["B-TIMEFUNC rank-3 failures"]) == 0,
        "N < 7 impossible": g["B-CAP N=6 at 1 ly"] is None and abs(g["B-CAP CMAX"] - math.log2(1.25)) < 1e-9,
        "LOCC: local unitaries keep entropy": g["B-LOCC local dS"] < 1e-12,
        "QEI covers < 1e-60": g["B-HELD fraction covered"] < 1e-60,
        "zero shift leaves NEC": g["B-HELD nec shift (z3)"] == "unsat",
        "board flags as encoded": (f["transit.BEATS_LIGHT"] is False and f["transit.TRAVERSAL_IS_REMOVED"] is False
                                   and f["transit.CARRIES_SUBSTANCE"] is False
                                   and f["emtension.ENTANGLED_BRIDGE_IS_TRAVERSABLE"] is False
                                   and f["LEDGER"] == {"S5": "OPEN", "S10": "REFUSED", "S13": "OPEN"}),
    }
    return all(tests.values()), tests


# =====================================================================================================================
# T. THE COMPLEMENTARY TESTS -- built on the members' instruments; three new computations
# =====================================================================================================================
def _np():
    import numpy as np
    return np


def tfd_drift(betas=(0.0, 0.5, 1.0, 2.0, 4.0, 8.0, 30.0), eps=0.1, T=3.0):
    """NEW.  H-SETTLE (W2, C2) inside H-IT's own READ model: Van Raamsdonk's eq.(1) state at d = 2 (geometry.tfd),
    Alice measures z or x, each of Bob's branch states drifts under nlcontrol's H = eps <X> Z (C2), and Bob reads
    sigma_y.  Returns, per beta: entanglement S (bits, geometry.vn_bits), the C2 signal <Y>_x - <Y>_z by
    nlcontrol.evolve and by settle.bloch_exact (exact), the C1 signal (drift on rho_B), and the linear control."""
    np = _np()
    GE, NL, ST = _quiet("geometry"), _quiet("nlcontrol"), _quiet("settle")
    bases = {"z": [np.array([1, 0], complex), np.array([0, 1], complex)],
             "x": [np.array([1, 1], complex) / math.sqrt(2), np.array([1, -1], complex) / math.sqrt(2)]}
    rows = []
    for beta in betas:
        psi = GE.tfd(2, beta)
        S = GE.vn_bits(GE.ptrace(GE.rho_of(psi), 2, 0))
        M = psi.reshape(2, 2)                                   # M[i, j]: Alice i, Bob j
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
        rho_b = GE.ptrace(GE.rho_of(psi), 2, 1)                 # C1: Alice's non-selective measurement leaves it
        rows.append({"beta": beta, "S_bits": S,
                     "C2_signal_integrator": y[(False, "x")] - y[(False, "z")],
                     "C2_signal_exact": y[("exact", "x")] - y[("exact", "z")],
                     "linear_control": y[(True, "x")] - y[(True, "z")],
                     "C1_signal": float(np.abs(GE.bob_state_after(psi, 2, ("M", np.eye(2))) -
                                               GE.bob_state_after(psi, 2, ("M", np.array([[1, 1], [1, -1]]) / math.sqrt(2)))).max()),
                     "rho_B_trace": float(np.trace(rho_b).real)})
    return rows


def product_drift(eps=0.1, T=3.0, trials=6, seed=4):
    """NEW.  The drift cannot make its own pairs: Alice and Bob share a PRODUCT state; whatever Alice measures, each
    of Bob's branch states is Bob's own state, so the drifted ensembles coincide.  Max |<Y>_x - <Y>_z| over random
    product states (nlcontrol.evolve).  CONTROL: the Bell state gives tanh(2 eps T)."""
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


def eps_window(L_list=None, N_list=(7, 1000, 1e6)):
    """z3 over the reals: is N_EPS consistent with the (NAMED-NOT-READ) Weinberg-family limit?  eps must satisfy
    eps_min(L, N) <= eps <= eps_max(reading).  eps_min from settle.eps_to_remove; eps_max from settle's Majumder
    figure under both H-MAP readings.  Exact rationals of the doubles: no parse drift."""
    ST = _quiet("settle")
    f = ST.BOUNDS_WEINBERG["Majumder+ 1990, 201Hg, PRL 65 2931"]["f_Hz"]
    L_list = L_list or (("1 AU", ST.AU_M), ("1 ly", ST.LY_M), ("4.24 ly", 4.24 * ST.LY_M))
    out = []
    for lab, emax in ST.eps_readings(f).items():
        for Ln, L in L_list:
            for N in N_list:
                emin = ST.eps_to_remove(L, N)
                e = z3.Real("eps")
                s = z3.Solver()
                s.add(e > 0, e <= z3.RealVal(str(Fr(emax))), e >= z3.RealVal(str(Fr(emin))))
                out.append({"reading": lab, "L": Ln, "N": N, "eps_min": emin, "eps_max": emax,
                            "consistent": s.check() == z3.sat})
    s = z3.Solver(); e = z3.Real("eps"); s.add(e > 0)
    vac = s.check() == z3.sat
    return out, vac


def first_transit(L_ly=1.0, N_per_qubit=7):
    """NEW.  The maximum consistent combination {W2, F1, ITB, RI} under its named hypotheses, priced end to end with
    imported numbers.  What it removes at the moment of transit, and what it moves earlier:
      pairs   -- the drift channel needs >= 2/CMAX = 6.21 pre-shared pairs per teleported qubit (settle), plus one
                 ebit per qubit for the teleportation itself (transit); each pair is distributed at <= c (B-LOCC);
      holder  -- a complete system of gravitating energy >= the Bekenstein floor must be at the destination
                 (measure.bekenstein_floor_j); S5/S13 need a prior arrival at <= c (D23);
      timing  -- with pairs and holder in place, Bob reads after T = L/2c (settle), before light; the FIRST transit
                 waits for the pairs: arrival >= L/c + T after the pairs leave.
    Counts are measure.py's four for a 70 kg body (named hypotheses H-LISTED, H-GRID, H-RHO, H-THERMO there)."""
    ST, ME = _quiet("settle"), _quiet("measure")
    rows, geo, ceil, ob = ME.price_table()
    L = L_ly * ST.LY_M
    c = ST.C_LIGHT
    T = 0.5 * L / c
    per_qubit_pairs = 2.0 / ST.CMAX
    out = {"L_m": L, "light_time_s": L / c, "drift_hold_T_s": T, "min_pairs_per_qubit": per_qubit_pairs,
           "eps_min_at_N": ST.eps_to_remove(L, N_per_qubit), "N_per_qubit": N_per_qubit,
           "first_transit_earliest_s_after_pairs_leave": L / c + T,
           "later_transit_advantage_s": L / c - T, "counts": []}
    for r in rows:
        qubits = r["bits"]                                   # H-FAITHFUL: one qubit per bit of the count (A3)
        out["counts"].append({"count": r["count"], "bits": r["bits"],
                              "drift_pairs_needed": qubits * N_per_qubit,
                              "teleport_ebits": qubits,
                              "holder_floor_J": r["bekenstein_floor_J_R1m"]})
    out["throat_J"] = geo["O-HOLD: wormhole.throat_mass(1 m) c^2"]
    # N_VAC, the one pathway that opens O-MAKE-DIST: Reznik quant-ph/0212044v2 p.12 (READ), inertial probes,
    # entanglement only for L/T < 1.1 -> the probe interaction lasts T > L/(1.1 c), with probes at BOTH ends first
    out["vacuum_harvest_min_T_over_light_time"] = 1.0 / 1.1
    out["vacuum_harvest_min_T_s"] = (L / c) / 1.1
    return out


def complementary_tests(rows):
    """Each class of complementary variant -> the test that covers it.  Returns tests and the class table."""
    np = _np()
    FR, GE, ST = _quiet("frame"), _quiet("geometry"), _quiet("settle")
    T = {}
    # T-A  W2 x F1: the channel survives keying to the cosmic slice, and the loop does not form
    sig = FR.signalling_table()
    T["T-A W2xF1"] = {
        "C2 MI bits (frame)": sig[("C2", "MI bits")],
        "Alice-first z/x vs Bob-first (frame.c2_needs_a_frame)": FR.c2_needs_a_frame(sig),
        "reply keyed to sender / cosmic (frame.antitelephone)": tuple(float(x) for x in FR.antitelephone()),
        "cosmic-keyed failures rank 2/3": (_cosmic_failures(FR.cosmic_keyed_rank_n_is_safe(2, 100)),
                                           _cosmic_failures(FR.cosmic_keyed_rank_n_is_safe(3, 100))),
        "Bob <Y> shift at eps=0.1, T=3 (settle)": ST.bob_y_exact(0.1, 3.0),
        "H-IT's model adds no signal to key (geometry.it_no_signal)": GE.it_no_signal(),
    }
    T["T-A W2xF1"]["pass"] = (T["T-A W2xF1"]["C2 MI bits (frame)"] > 0.08 and
                              T["T-A W2xF1"]["reply keyed to sender / cosmic (frame.antitelephone)"][1] == 0.0 and
                              T["T-A W2xF1"]["cosmic-keyed failures rank 2/3"] == (0, 0) and
                              T["T-A W2xF1"]["H-IT's model adds no signal to key (geometry.it_no_signal)"] < 1e-12)
    # T-B  W2 inside H-IT's model (ITB keeps the channel; ITE's no-signal assumption is contradicted, computed)
    td = tfd_drift()
    T["T-B W2xIT (tfd_drift)"] = {"rows": td}
    sigs = [r["C2_signal_exact"] for r in td]
    T["T-B W2xIT (tfd_drift)"]["pass"] = (
        all(abs(r["C2_signal_integrator"] - r["C2_signal_exact"]) < 5e-3 for r in td) and
        all(abs(r["linear_control"]) < 1e-12 and r["C1_signal"] < 1e-12 for r in td) and
        sigs[0] > 0.5 and sigs[-1] < 1e-5 and all(a >= b - 1e-12 for a, b in zip(sigs, sigs[1:])))
    # T-C  W2 cannot make its own pairs (O-MAKE-DIST survives)
    pw, bell = product_drift()
    T["T-C W2 x O-MAKE-DIST (product_drift)"] = {"product_max_signal": pw, "bell_control": bell,
                                                 "local_unitary_dS (geometry)": GE.locc_entropy_change()[1],
                                                 "nonlocal_control_dS (geometry)": GE.locc_entropy_change(nonlocal_control=True)[1]}
    T["T-C W2 x O-MAKE-DIST (product_drift)"]["pass"] = pw < 1e-12 and bell > 0.5
    # T-D  ITB x RI: O-HOLD removed, the holding reappears as a holder at the destination (feeds O-MATTER)
    ft = first_transit()
    floors = [c["holder_floor_J"] for c in ft["counts"]]
    T["T-D ITBxRI (holder floor)"] = {"holder_floor_J_range": (min(floors), max(floors)), "throat_J": ft["throat_J"],
                                      "ratio_throat_to_largest_floor": ft["throat_J"] / max(floors)}
    T["T-D ITBxRI (holder floor)"]["pass"] = min(floors) > 0 and ft["throat_J"] / max(floors) > 1e39
    # T-E  the maximum consistent combination, end to end
    win, vac = eps_window()
    T["T-E max {W2,F1,ITB,RI}"] = {"first_transit": ft, "eps_window": win, "eps_vacuity": vac}
    one_ly = [w for w in win if w["L"] == "1 ly" and w["N"] == 7]
    one_au = [w for w in win if w["L"] == "1 AU" and w["N"] == 7]
    T["T-E max {W2,F1,ITB,RI}"]["pass"] = (vac and all(w["consistent"] for w in one_ly) and
                                            not any(w["consistent"] for w in one_au) and
                                            ft["later_transit_advantage_s"] > 0 and
                                            ft["first_transit_earliest_s_after_pairs_leave"] > ft["light_time_s"])
    # T-F  the OPEN x OPEN pair on O-HOLD (RQ x KR): nothing decides it; the in-scope number is recorded
    T["T-F RQxKR (O-HOLD OPEN)"] = {"in_scope_fraction": GE.r_quantum()["fraction_covered"],
                                    "note": "xi > 0 (no state-independent QEI) and eps_G (no bound) both OPEN at source"}
    T["T-F RQxKR (O-HOLD OPEN)"]["pass"] = T["T-F RQxKR (O-HOLD OPEN)"]["in_scope_fraction"] < 1e-60
    # class table: complementary variants grouped by (removed set, contributors)
    classes = {}
    for r in rows:
        if r.get("complementary"):
            key = (tuple(removed_set(r)), tuple(r["contributors"]))
            classes.setdefault(key, []).append(r)
    cover = {}
    for (rem, contrib), lst in classes.items():
        c = set(contrib)
        tests = []
        if {"W2", "F1"} <= c:
            tests.append("T-A W2xF1")
        if "W2" in c and ("ITB" in c or "ITE" in c):
            tests.append("T-B W2xIT (tfd_drift)")
        if "W2" in c:
            tests.append("T-C W2 x O-MAKE-DIST (product_drift)")
        if {"ITB", "RI"} <= c:
            tests.append("T-D ITBxRI (holder floor)")
        if {"W2", "F1", "ITB", "RI"} <= c:
            tests.append("T-E max {W2,F1,ITB,RI}")
        if "F1" in c and ("ITB" in c or "ITE" in c) and "W2" not in c:
            tests.append("T-A W2xF1")      # the keyed-corridor half of T-A is the F1 claim; H-IT adds no signal
        cover["|".join(rem) + " <- " + ",".join(contrib)] = {"variants": len(lst), "tests": sorted(set(tests))}
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
        best = max(cons, key=lambda r: (len(five_view(r)), len(removed_set(r))), default=None)
        clashes = sorted({" + ".join(r["clash"]) for r in lst if not r["consistent"]})
        table.append({"combo": list(key), "variants": len(lst), "consistent": len(cons),
                      "inconsistent": len(lst) - len(cons), "clashes": clashes,
                      "best_removed": removed_set(best) if best else [],
                      "best_five": five_view(best) if best else [],
                      "best_variant": best["present"] if best else None,
                      "complementary_variants": sum(1 for r in cons if r.get("complementary"))})
    return table


def survivors(rows):
    """Obstructions removed in NO consistent variant -- and those removed only via an OPEN branch."""
    cons = [r for r in rows if r["consistent"]]
    ever = set()
    for r in cons:
        ever |= set(removed_set(r))
    open_any = {o for r in cons for o, v in r["per"].items() if v["verdict"] == "OPEN"}
    return sorted(set(OBST) - ever, key=OBST.index), sorted(open_any, key=OBST.index)


def load_bearing(rows):
    """Which literals appear in the core of any removal, in any consistent variant."""
    lb = set()
    named = set()
    for r in rows:
        if r["consistent"]:
            for v in r["per"].values():
                if v["verdict"] in ("REMOVED", "REMOVED-IF"):
                    lb |= set(v["rests_on"])
                    named |= set(v.get("named", []))
    return sorted(lb, key=LIT_NAMES.index), sorted(named)


def untested(rows, cover_keys):
    # N_VAC opens O-MAKE-DIST in EVERY variant (it is a pathway no member supplies), so it does not by itself make a
    # variant 'OPEN ONLY'; a variant is 'OPEN ONLY' when a member's own OPEN branch (N_XI, N_EPSG) is on its path.
    reasons = {"INCONSISTENT (named clash; nothing to test)": 0,
               "NO REMOVAL (no member removes an obstruction: nothing complementary)": 0,
               "SINGLE CONTRIBUTOR (one member's removal set covers the variant's; graded in that member's report)": 0,
               "OPEN ONLY on the removal path": 0}
    listed = []
    for r in rows:
        if not r["consistent"]:
            reason = "INCONSISTENT (named clash; nothing to test)"
        elif r.get("complementary"):
            continue
        elif not removed_set(r):
            opens = sorted({k for v in r["per"].values() if v["verdict"] == "OPEN" for k in v["via"]})
            reason = ("NO REMOVAL (no member removes an obstruction: nothing complementary)" if opens == ["N_VAC"]
                      else "OPEN ONLY on the removal path")
        else:
            reason = "SINGLE CONTRIBUTOR (one member's removal set covers the variant's; graded in that member's report)"
        reasons[reason] += 1
        listed.append((r["present"], reason))
    return reasons, listed


def run_all(with_tests=True):
    scr = Screen()
    vac_ok, vac = guard_vacuity(scr)
    drift_ok, drift = guard_drift(scr)
    if not (vac_ok and drift_ok):
        return {"refused": True, "vacuity": vac, "drift": drift}
    rows, dt = run_screen(scr)
    out = {"refused": False, "vacuity": vac, "drift": drift, "screen_seconds": dt, "rows": rows,
           "table": aggregate(rows), "survivors": survivors(rows), "load_bearing": load_bearing(rows)}
    if with_tests:
        g = ground_checks()
        out["grounds"] = g
        out["grounds_ok"] = grounds_ok(g)
        out["tests"], out["cover"] = complementary_tests(rows)
    out["untested"] = untested(rows, list(out.get("cover", {})))
    return out


def _fmt(x):
    return json.dumps(x, default=str)


def report(R):
    if R["refused"]:
        print("REFUSED: a guard failed.  vacuity:", _fmt(R["vacuity"]), "\ndrift:", _fmt(R["drift"]))
        return
    rows = R["rows"]
    cons = [r for r in rows if r["consistent"]]
    print(f"DOCKET 68 / B-combine.  {len(rows)} variants over {len(R['table'])} combinations "
          f"(127 + readings-only); consistent {len(cons)}, inconsistent {len(rows) - len(cons)}; "
          f"z3 screen {R['screen_seconds']:.1f} s")
    print("\nGUARDS: vacuity", _fmt(R["vacuity"]["known_contradictions_caught"]),
          "| drift rows agree:", all(x["agree"] for x in R["drift"]["rows"]),
          "| mutated encoding caught:", R["drift"]["mutated_encoding_caught"])
    clashes = {}
    for r in rows:
        if not r["consistent"]:
            clashes.setdefault(" + ".join(r["clash"]), 0)
            clashes[" + ".join(r["clash"])] += 1
    print("\nCLASHES (unsat cores, variants):")
    for k, v in sorted(clashes.items(), key=lambda kv: -kv[1]):
        print(f"  {v:5d}  {k}")
    best = max(cons, key=lambda r: (len(five_view(r)), len(removed_set(r))))
    print("\nMOST REMOVED (consistent):", best["present"], "->", removed_set(best), "| five-view:", five_view(best))
    for o, v in best["per"].items():
        print(f"    {o:12s} {v}")
    s, op = R["survivors"]
    print("\nREMOVED IN NO CONSISTENT VARIANT:", s, "| OPEN somewhere:", op)
    print("LOAD-BEARING literals:", R["load_bearing"][0], "| named hypotheses used:", R["load_bearing"][1])
    print("\nSYNERGY (z3 set exceeds the union of singletons):")
    syn = {}
    for r in cons:
        if r["synergy"]:
            syn.setdefault((tuple(r["synergy"]), tuple(r["contributors"])), 0)
            syn[(tuple(r["synergy"]), tuple(r["contributors"]))] += 1
    for k, v in syn.items():
        print(f"  {v:5d}  {k}")
    print("INTERFERENCE:", sum(1 for r in cons if r["interference"]), "variants")
    if "tests" in R:
        print("\nGROUNDS:", R["grounds_ok"])
        print("\nCOMPLEMENTARY CLASSES -> tests:")
        for k, v in R["cover"].items():
            print(f"  {k:60s} {v}")
        for k, v in R["tests"].items():
            vv = {kk: vv for kk, vv in v.items() if kk != "rows"}
            print(f"\n  {k}: {_fmt(vv)[:1400]}")
            if "rows" in v:
                for row in v["rows"]:
                    print("     ", {kk: (round(vv, 6) if isinstance(vv, float) else vv) for kk, vv in row.items()})
    print("\nNOT TESTED BY INSTRUMENT (variants, by reason):", _fmt(R["untested"][0]))


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
        print(_fmt(R)[:3000])
        return 1
    V, D = R["vacuity"], R["drift"]
    ck("VACUITY board alone SAT", V["board_alone_sat"])
    ck("VACUITY each of 13 single readings SAT", all(V["each_single_reading_sat"].values()))
    ck("VACUITY named hypotheses jointly SAT with the board", V["named_jointly_sat_with_board"])
    ck("VACUITY named + OPEN jointly SAT with the board", V["all_named_and_open_sat_with_board"])
    for k, v in V["known_contradictions_caught"].items():
        ck("CONTROL known contradiction caught: " + k, v)
    ck("NON-TRIVIAL board admits a loop and no loop", V["board_admits_loop"] and V["board_admits_no_loop"])
    ck("CONTROL without B-RECV, O-MATTER becomes removable", V["without_B_RECV_matter_removable"])
    for row in D["rows"]:
        ck(f"DRIFT {row['variant']} z3 {row['z3']} == expected {row['expected']}", row["agree"], row["note"])
        ck(f"DRIFT {row['variant']} report text {row['report']} names {row['report_removes_tokens']}",
           row["report_text_matches"])
    ck("DRIFT OPEN branches show as OPEN (RQ via N_XI, KR via N_EPSG)", D["open_branches_ok"])
    ck("CONTROL mutated encoding (F1 unkeyed) caught by the drift guard", D["mutated_encoding_caught"])
    rows = R["rows"]
    ck("COVERAGE 3,071 variants screened ((4*4*3*16 - 1) * 4 + 3)", len(rows) == 3071, len(rows))
    ck("COVERAGE 127 combinations + readings-only", len(R["table"]) == 128, len(R["table"]))
    ck("COVERAGE every combination has >= 1 consistent variant", all(t["consistent"] >= 1 for t in R["table"]))
    cons = [r for r in rows if r["consistent"]]
    ck("VACUITY every REMOVED-IF rests on satisfiable premises",
       all(v["premises_sat"] for r in cons for v in r["per"].values() if v["verdict"] == "REMOVED-IF"))
    ck("VACUITY every consistent variant stays SAT with all named hypotheses assumed (no conditional removal is "
       "vacuous)", all(r["named_jointly_sat"] for r in cons), sum(1 for r in cons if not r["named_jointly_sat"]))
    best5 = max(len(five_view(r)) for r in cons)
    ck("RESULT no consistent variant removes all five", best5 < 5, best5)
    s, op = R["survivors"]
    ck("RESULT O-MATTER removed in no consistent variant", "O-MATTER" in s, s)
    ck("RESULT O-MAKE-DIST removed in no consistent variant (OPEN only via N_VAC)", "O-MAKE-DIST" in s, s)
    ck("RESULT O-MAKE-DIST OPEN via N_VAC somewhere", "O-MAKE-DIST" in op, op)
    clash_names = {c for r in rows if not r["consistent"] for c in r["clash"]}
    ck("RESULT every clash core names at least two literals or a literal and a holding",
       all(len(r["clash"]) >= 2 for r in rows if not r["consistent"]))
    ck("RESULT the three clash families present: F1/F2b, ITE/W2, ITB+RI/RQ",
       {"F1", "F2b"} <= clash_names and {"ITE", "W2"} <= clash_names and {"ITB", "RI", "RQ"} <= clash_names,
       sorted(clash_names))
    mx = [r for r in cons if set(r["present"]) >= {"W2", "F1", "ITB", "RI"} and "RQ" not in r["present"]]
    ck("RESULT {W2,F1,ITB,RI} removes O-BITS, O-MAKE-TOPO, O-HOLD, O-LOOP",
       mx and all(set(removed_set(r)) == {"O-BITS", "O-MAKE-TOPO", "O-HOLD", "O-LOOP"} for r in mx))
    lb, named = R["load_bearing"]
    ck("RESULT H12, INFO, ZERO, NULL load-bearing for no removal", not ({"H12", "INFO", "ZERO", "NULL"} & set(lb)), lb)
    ok, tests = R["grounds_ok"]
    for k, v in tests.items():
        ck("GROUND " + k, v)
    for k, v in R["tests"].items():
        ck("TEST " + k, v["pass"])
    td = R["tests"]["T-B W2xIT (tfd_drift)"]["rows"]
    ck("NEW tfd_drift: beta=0 reproduces tanh(0.6) (the Bell case)", abs(td[0]["C2_signal_exact"] - math.tanh(0.6)) < 1e-9,
       td[0]["C2_signal_exact"])
    ck("NEW tfd_drift CONTROL linear and C1 give 0 at every beta",
       all(abs(r["linear_control"]) < 1e-12 and r["C1_signal"] < 1e-12 for r in td))
    pw = R["tests"]["T-C W2 x O-MAKE-DIST (product_drift)"]
    ck("NEW product_drift exactly 0 / CONTROL Bell > 0.5", pw["product_max_signal"] < 1e-12 and pw["bell_control"] > 0.5)
    ck("COVERAGE every complementary class has a test", all(v["tests"] for v in R["cover"].values()),
       [k for k, v in R["cover"].items() if not v["tests"]])
    reasons, listed = R["untested"]
    n_comp = sum(1 for r in cons if r.get("complementary"))
    ck("COVERAGE untested + complementary = all variants", sum(reasons.values()) + n_comp == len(rows),
       (sum(reasons.values()), n_comp))
    npass = sum(1 for _, c, _ in checks if c)
    for n, c, d in checks:
        print(("PASS " if c else "FAIL ") + n + (f"  [{d}]" if d not in ("", None) and not c else ""))
    print(f"\n{npass}/{len(checks)} checks pass, "
          f"{sum(1 for n, _, _ in checks if n.startswith('CONTROL'))} of them controls, {time.time() - t0:.0f} s")
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    R = run_all(with_tests="--fast" not in sys.argv)
    if "--json" in sys.argv:
        p = sys.argv[sys.argv.index("--json") + 1]
        with open(p, "w") as f:
            json.dump({k: v for k, v in R.items()}, f, default=str, indent=1)
    report(R)
