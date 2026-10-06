#!/usr/bin/env python3
"""
chain.py -- the whole chain of warp travel re-run under M's theory (M-RULINGS item 96).  Deduced, computed and READ.
Not seated; not verified.  M's words are carried as hypotheses, never as results.

M (item 96, verbatim): "Instead of trying to prove my theory of warp travel wrong. We need to focus on proving it right.
Assume that my theory is the only one in which warp travel is actually realizable. The whole chain of warp travel should
be entirely derivable from first principles and provable with math. Rerun the whole chain and reassess the
walls/obstructions/gaps. Those will be our focus."  Carried as H-M-THEORY: M's items 86-97 are the working premise set;
the board's other routes are the boundary (item 82).  A link is PROVED only from named premises; a WALL is a result that
blocks a link even under M's premises; a ROUTE is a named premise under which the wall does not bind; a GAP is what no
result on the board reaches.  Re-run by four readers over the board's owners (2026-10-06), assembled here; every number
is computed now from the owners, imported, never retyped.

THE CHAIN UNDER M'S THEORY (stations, in order)
  ADDRESS  the device at position 1 takes position 2 as an input (H-ADDRESS-INPUT; entanglement plus trajectory
           triangulation, H-TRIANGULATED-ACTION)
  READ     the object at position 1 is read (H-READING... the identity core, faithful.py)
  README   the classical specification (H-README, H-COST-IN-README)
  MAKE     a corridor that also contains position 2, two places made one (H-CORRIDOR-CONTAINS-P2, H-IDENTIFY; H-MADE or,
           M's own alternative, found and widened: H-COMMON-THROATS)
  KEY      joined at the same instant of the cosmic clock, the CMB frame's beat (H-CMB-FRAME, H-COSMIC-BEAT)
  HOLD     held for a brief, non-zero, relative hold (H-BRIEF-HOLD); appears to contain negative energy, does not
           (H-READING-ONLY); single use (H-CORRIDOR-SINGLE-USE)
  CROSS    the README is present at position 2 (H-IDENTIFY: one point; H-README-IN-HOLD)
  BUILD    position 2 itself builds the copy from its own stock (H-POSITION-BUILDS, H-STOCK-IS-STOCK)
  COPY     the faithful copy is the goal (item 87)
  REPEAT   the device is reusable, corridors repeatable (H-DEVICE-REUSABLE, H-CORRIDOR-REPEATABLE)

WHAT FOLLOWS THE WORK
  * M'S OWN ANSWER 3 IS THE ROUTE THE THEOREMS LEAVE OPEN (Z1).  Machine-checked over the board's reading of the
    theorems: with the corridor MADE (H-MADE), a smooth non-degenerate metric, a causally compact interpolation and the
    CMB clock as a global time function, Geroch-Borde's corollary makes the set inconsistent, and so does well-posed
    evolution (position 2 cannot be made part of the corridor from position 1 at the same instant).  With the corridor
    FOUND AND WIDENED (H-COMMON-THROATS, item 86 answer 3: "if found and widened ... common and regular occurrences")
    the whole set is consistent AND causal safety is entailed.  Of the five routes tested, it is the only one that
    clears both walls and keeps safety: degenerate metrics clear Geroch but not well-posedness; quantum topology
    change clears both but loses the proof of safety.
  * WHAT IS PROVED UNDER M'S PREMISES (Z2): causal safety for every repetition (K2; FRW lemma: the geometry picks the
    beat); D13 satisfied with a zero bound once two places are one; demand rows D1-D4, D8-D12 not instantiated (a throat
    is excluded by their own scope); R = 0 throats need no plane matter (8m: H-READING-ONLY in the board's terms);
    widening is not topology change; k* = 0 (nothing shipped); stock passes on quantity; the README is classical, and
    its size sets the corridor's size (Bekenstein).
  * THE CORRIDOR'S ENERGY HAS A FIRST-PRINCIPLES FLOOR, AND IT GOES AS THE SQUARE ROOT OF THE README (Z3).  A neck of
    radius r carries Misner-Sharp energy r c^4 / 2G (derived, sympy); Bekenstein's eq. (1) (READ in measure.py) says a
    region of radius r holding N bits needs E >= N hbar c ln2 / (2 pi r).  Both met at the least r: E_min =
    sqrt(N h c^5 ln2 / (8 pi^2 G)) = 4.59404002e8 J x sqrt(N) (u_r 1.1e-5 from G; M-COEFF, item 98).  For the
    identity core, 2.40587833e16 J at a neck of 3.97581866e-28 m (= 7.59185111e-36 m x sqrt(N)) --
    under the 0.1 c trip's 3.2e16 J; for the largest snapshot, 1.5e23 J -- over every trip.  M's "the cost is in ...
    how big the file is" (item 89) gets an exact form: the cost of one corridor grows as the square root of the file.
    Premises: H-NECK-HOLDS (the README sits in the neck region) and H-NECK-ENERGY (the corridor's cost is the neck's
    energy; the plane's ADM total can be zero, which would remove the floor -- OPEN, which energy M means).
  * THE WALLS, RANKED (Z4) -- the focus.  1 FORMATION (topology change) and 2 REACHING POSITION 2 (well-posedness):
    both cleared by found-and-widened, which then owes 3 THROAT EXISTENCE (do microscopic throats exist, and one
    joining the two places?).  4 THE BUILDER at position 2 (what physics makes a position build from a README; the
    README's 1e15-bit size needs a builder that knows the recipe -- a bare position knows only physics).  5 ENERGY AT
    POSITION 2 for the build (the README's information can buy at most N kT ln2 of work).  6 THE GLOBAL BULK for R = 0
    throats (BULK5-O1).  7 THE COUPLING (what writes the identification).  8 ADDRESS PRECISION (Gaia DR3's radial error
    is hundreds of times Proxima b's orbit).  9 THE READ (non-destructive at synapse resolution).  10 IDENTITY
    COMPLETENESS.  11 THE SPLIT (on which side the README ends).  Each with what would remove it.

    python3 chain.py              report
    python3 chain.py --selftest   checks, CONTROLS and CONTRASTS marked, STRUCTURAL printed and not counted

Z1 [z3; the theorems as the board reads them, each with its source and grade]  Booleans for the chain's facts; each
   theorem an implication; M's premises asserted; satisfiability and entailment (axioms AND NOT safety unsat) per route.
   H-ENCODING: the encoding is the board's reading of each theorem's statement; the clauses are printed beside their
   sources (the drift guard), and a vacuity control (no theorems) and a drop-one control run.
Z2 [imported]  causal/frame (K2, the FRW lemma), uses (k*), stockdest, faithful, create (enlargement).
Z3 [derived, sympy; imported]  Misner-Sharp m = (r/2)(1 - g^rr) at a throat, g^rr(r0) = 0; measure.bekenstein_floor_j;
   seat's constants; uses.trip_energy.
Z4 [the four readers' reports, each wall with its owner]  the ranking and routes, as data.
Also computed: the cosmic beat (item 97): the CMB temperature falls as 1/a, so reading equal cosmic time to dt needs
   dT/T = H0 dt (cosmo.H0); the address error (cmbframe's Gaia DR3 row) against Proxima b's orbit (seat's Faria row).

NAMED HYPOTHESES
  M's (items 86-97): H-M-THEORY, H-ADDRESS-INPUT, H-TRIANGULATED-ACTION, H-README, H-COST-IN-README, H-STOCK-IS-STOCK,
  H-POSITION-BUILDS, H-CORRIDOR-CONTAINS-P2, H-IDENTIFY, H-MADE, H-COMMON-THROATS, H-CMB-FRAME, H-COSMIC-BEAT,
  H-BRIEF-HOLD, H-READING-ONLY, H-SEEN-BY-INTERACTION, H-CORRIDOR-SINGLE-USE, H-DEVICE-REUSABLE, H-CORRIDOR-REPEATABLE,
  H-SINGLE-CHANNEL-GROWS, H-README-IN-HOLD, H-NO-MOVEMENT, H-INSTANTANEOUS, H-UNIDENTIFIED-CARRIER, H-RETIRE-A (open).
  The board's: H-ENCODING, H-NO-PINCH (a widened throat keeps r > 0, so closing is not topology change),
  H-WELL-POSED, H-CORRIDOR-MODEL, H-KEYING (now M's, via H-CMB-FRAME), H-FRW-EXACT, H-NOT-DE-SITTER, H-NECK-HOLDS,
  H-NECK-ENERGY, H-RS1, H-REGENERABLE, H-WIRING-SUFFICES, H-IDENTITY-IN-DYNAMICS.
"""

import contextlib
import importlib.util
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)


def _load(name, path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    m = importlib.util.module_from_spec(spec)
    saved = list(sys.path)
    try:
        sys.path.insert(0, WD)
        sys.path.insert(0, D68)
        sys.path.insert(0, os.path.dirname(path))
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(m)
    finally:
        sys.path[:] = saved
    return m


_CACHE = {}


def owners():
    if not _CACHE:
        _CACHE["uses"] = _load("uses", os.path.join(HERE, "uses.py"), "copy_uses_chain")
        _CACHE["measure"] = _load("measure", os.path.join(D68, "measure.py"), "d68_measure_chain")
        _CACHE["frame"] = _load("frame", os.path.join(D68, "frame.py"), "d68_frame_chain")
        _CACHE["cosmo"] = _load("cosmo", os.path.join(WD, "cosmo.py"), "wd_cosmo_chain")
        _CACHE["create"] = _load("create", os.path.join(WD, "create.py"), "wd_create_chain")
        _CACHE["stockdest"] = _load("stockdest", os.path.join(HERE, "stockdest.py"), "copy_stockdest_chain")
    return _CACHE


# ============================================================================================ Z1: the chain's logic
THEOREMS = [
    # (name, source and grade, clause as text)
    ("MADE-IS-TOPO", "create.py (bringing a throat into existence is topology change; D24 OPEN)",
     "Made -> Topo"),
    ("WIDEN-NOT-TOPO", "create.theorems_apply_to_enlargement() = False; GRADES topology-change-vs-metric-change "
                       "NARROWED (Borde READ); premise H-NO-PINCH",
     "Found & Widen & NoPinch & !Made -> !Topo"),
    ("GEROCH-BORDE", "Geroch 1967 / Borde's corollary, GRADES geroch-1967-topology-change NARROWED, "
                     "READ-VIA-RESTATEMENT (the make reader's statement; frame.GRADES O-MAKE)",
     "Topo & CausallyCompact & Smooth & TimeFunction -> False"),
    ("WELL-POSED", "hyperbolic evolution (BULK5-O6 Anderson; D23 as corrected): an act at P1 cannot make P2 part of a "
                   "corridor at the same instant unless a connection already exists",
     "Made & WellPosed -> False"),
    ("CMB-IS-TF", "H-CMB-FRAME: the cosmic clock is a global time function (frame.py's FRW lemma; LSV p.16 stable "
                  "causality, READ)",
     "CMBKey -> TimeFunction"),
    ("TF-NO-CTC", "a global time function excludes closed timelike curves (LSV p.16, READ)",
     "TimeFunction -> !CTC"),
    ("K2", "frame.cosmic_keyed_rank_n_is_safe, latticectc D21 THEOREM, causal.py K2: keyed identifications in the "
           "corridor model close no loop",
     "CMBKey & CorridorModel & Corridor -> Safe"),
    ("QTOPO-BREAKS-MODEL", "geometry.py / frame.GRADES: under N_QTOPO the corridor is not the Lorentzian quotient "
                           "K2 covers (O-LOOP NOT-BOUND-IF)",
     "QuantumTopo -> !CorridorModel"),
    ("QTOPO-ESCAPES", "geometry.py O-MAKE-TOPO NOT-BOUND-IF {N_QTOPO}: quantum topology change is outside Geroch's "
                      "class and outside hyperbolic classical evolution",
     "QuantumTopo -> !Smooth & !WellPosed"),
    ("CORRIDOR-ORIGIN", "a corridor is made or found and widened (M's item 86 answer 3)",
     "Corridor -> Made | (Found & Widen)"),
]


def z3_chain():
    import z3
    names = ["Corridor", "Made", "Found", "Widen", "NoPinch", "Topo", "CausallyCompact", "Smooth", "TimeFunction",
             "WellPosed", "CMBKey", "CTC", "CorridorModel", "Safe", "QuantumTopo"]
    V = {n: z3.Bool(n) for n in names}
    I, A, N, O = z3.Implies, z3.And, z3.Not, z3.Or
    clause = {
        "MADE-IS-TOPO": I(V["Made"], V["Topo"]),
        "WIDEN-NOT-TOPO": I(A(V["Found"], V["Widen"], V["NoPinch"], N(V["Made"])), N(V["Topo"])),
        "GEROCH-BORDE": N(A(V["Topo"], V["CausallyCompact"], V["Smooth"], V["TimeFunction"])),
        "WELL-POSED": N(A(V["Made"], V["WellPosed"])),
        "CMB-IS-TF": I(V["CMBKey"], V["TimeFunction"]),
        "TF-NO-CTC": I(V["TimeFunction"], N(V["CTC"])),
        "K2": I(A(V["CMBKey"], V["CorridorModel"], V["Corridor"]), V["Safe"]),
        "QTOPO-BREAKS-MODEL": I(V["QuantumTopo"], N(V["CorridorModel"])),
        "QTOPO-ESCAPES": I(V["QuantumTopo"], A(N(V["Smooth"]), N(V["WellPosed"]))),
        "CORRIDOR-ORIGIN": I(V["Corridor"], O(V["Made"], A(V["Found"], V["Widen"]))),
    }
    # M's premises (items 86-97) and the board's default physics premises
    m_axioms = {"H-CORRIDOR-CONTAINS-P2/H-IDENTIFY": V["Corridor"], "H-CMB-FRAME": V["CMBKey"]}
    classical = {"smooth metric": V["Smooth"], "causally compact": V["CausallyCompact"],
                 "well-posed (H-WELL-POSED)": V["WellPosed"], "corridor model": V["CorridorModel"]}
    routes = {
        "H-MADE (as stated)": {"Made": True},
        "R1 found and widened (H-COMMON-THROATS, H-NO-PINCH)": {"Made": False, "Found": True, "Widen": True,
                                                                "NoPinch": True},
        "R2 made, degenerate metric (Borde IX.C)": {"Made": True, "smooth metric": False},
        "R5 made, non-compact interpolation": {"Made": True, "causally compact": False},
        "R3 made, quantum topology change (N_QTOPO)": {"Made": True, "QuantumTopo": True, "smooth metric": None,
                                                        "well-posed (H-WELL-POSED)": None, "corridor model": None},
    }

    def solve(route, with_theorems=True, drop=None):
        out = {}
        for want_safe_negated in (False, True):
            s = z3.Solver()
            if with_theorems:
                for k, c in clause.items():
                    if k != drop:
                        s.add(c)
            for c in m_axioms.values():
                s.add(c)
            for k, c in classical.items():
                if k in route and route[k] is None:
                    continue
                if k in route and route[k] is False:
                    s.add(z3.Not(c))
                else:
                    s.add(c)
            for k, val in route.items():
                if k in V:
                    s.add(V[k] if val else z3.Not(V[k]))
            if want_safe_negated:
                s.add(z3.Not(V["Safe"]))
            out[want_safe_negated] = str(s.check())
        return {"consistent": out[False] == "sat", "safety_entailed": out[True] == "unsat"}

    results = {r: solve(spec) for r, spec in routes.items()}
    vacuity = solve(routes["H-MADE (as stated)"], with_theorems=False)
    drop_geroch = solve(routes["R2 made, degenerate metric (Borde IX.C)"], drop="WELL-POSED")
    return {"routes": results, "vacuity_made_no_theorems": vacuity, "R2_without_well_posed": drop_geroch}


# ============================================================================================ Z3: corridor energy
def neck_misner_sharp_symbolic():
    """Misner-Sharp mass m(r) = (r/2)(1 - g^rr) (geometric units) for ds^2 = -e^{2Phi}dt^2 + dr^2/(1 - b/r) + r^2 dOmega;
    at a throat b(r0) = r0, so g^rr(r0) = 0 and m(r0) = r0/2: E_neck = r0 c^4 / (2G)."""
    import sympy as sp
    r, r0 = sp.symbols("r r0", positive=True)
    b = sp.Function("b")
    grr_inv = 1 - b(r) / r
    m = sp.simplify(r / 2 * (1 - grr_inv))
    at_throat = sp.simplify(m.subs(r, r0).subs(b(r0), r0))
    return str(m), str(at_throat)


def corridor_floor(N):
    """The least neck radius at which the neck's Misner-Sharp energy meets Bekenstein's floor for N bits, and that
    energy (H-NECK-HOLDS, H-NECK-ENERGY)."""
    o = owners()
    seat = o["uses"].owners()[0]
    e_per_m = seat.C ** 4 / (2.0 * seat.G)
    lo, hi = 1e-60, 1e10
    for _ in range(400):
        mid = math.sqrt(lo * hi)
        if mid * e_per_m >= o["measure"].bekenstein_floor_j(N, R=mid):
            hi = mid
        else:
            lo = mid
    return {"r_m": hi, "E_J": hi * e_per_m, "E_planck_J": math.sqrt(1.054571817e-34 * seat.C ** 5 / seat.G)}


# ============================================================================================ M-COEFF (item 98)
U_R_G = 2.2e-5          # foliation.py's comment on G_NEWTON (CODATA 2018 u_r, "not typed" there): named, not READ here


def coefficients():
    """Every coefficient of the chain's formulas as an exact closed form in the constants and its value (M-COEFF).
    h, c and k_B enter EXACTLY (SI 2019 definitions, read off the owners cosmo.py and seat.py); G (CODATA 2018, seat via
    foliation) and H0 (Planck 2018, cosmo.py, +- 0.54) are measured, entered at their values, uncertainties named."""
    import sympy as sp
    o = owners()
    seat = o["uses"].owners()[0]
    cosmo = o["cosmo"]
    h = sp.Rational("%.8e" % (cosmo._HBAR * 2 * math.pi))        # 6.62607015e-34, exact by definition
    kB = sp.Rational(repr(cosmo._KB))                            # 1.380649e-23, exact by definition
    c = sp.Integer(int(seat.C))                                  # 299792458, exact by definition
    G = sp.Rational(repr(seat.G))                                # 6.6743e-11, measured
    hbar = h / (2 * sp.pi)
    T = sp.Integer(310)                                          # measure's H-ERASE temperature
    defs = {
        "bekenstein_J_m_per_bit": (hbar * c * sp.log(2) / (2 * sp.pi), 0.0,
                                   "E r >= N hbar c ln2 / (2 pi) = N h c ln2 / (4 pi^2)"),
        "neck_J_per_m": (c ** 4 / (2 * G), U_R_G, "E_neck = r c^4 / (2 G)"),
        "E_min_J_per_sqrt_bit": (sp.sqrt(hbar * c ** 5 * sp.log(2) / (4 * sp.pi * G)), U_R_G / 2,
                                 "E_min = sqrt(N h c^5 ln2 / (8 pi^2 G))"),
        "r_min_m_per_sqrt_bit": (sp.sqrt(hbar * G * sp.log(2) / (sp.pi * c ** 3)), U_R_G / 2,
                                 "r_min = sqrt(N h G ln2 / (2 pi^2 c^3))"),
        "szilard_J_per_bit_310K": (kB * T * sp.log(2), 0.0, "W <= N k_B T ln2 at T = 310 K"),
    }
    out = {}
    for k, (expr, ur, form) in defs.items():
        out[k] = {"form": form, "exact": str(sp.nsimplify(expr)), "value": float(sp.N(expr, 20)),
                  "value_15": str(sp.N(expr, 15)), "u_r": ur}
    out["H0_per_s"] = {"form": "H0 = 67.36 km/s/Mpc / Mpc", "exact": "measured (Planck 2018, +- 0.54 km/s/Mpc)",
                       "value": cosmo.H0(), "value_15": "%.6e" % cosmo.H0(), "u_r": 0.54 / 67.36}
    return out


# ============================================================================================ compute
def compute():
    o = owners()
    uses, measure, frame, cosmo, create, sd = (o[k] for k in ("uses", "measure", "frame", "cosmo", "create",
                                                              "stockdest"))
    seat, fa, ca = uses.owners()
    saved = list(sys.path)
    sys.path[:0] = [D68, WD]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            z1 = z3_chain()
            core = fa.identity_core()["total_bits"]
            snap = fa._measure()
            fl_core, fl_snap = corridor_floor(core), corridor_floor(snap["grid_0p1A"])
            fl_4 = corridor_floor(4 * core)
            ms = neck_misner_sharp_symbolic()
            tested, bad = frame.cosmic_keyed_rank_n_is_safe(3, 100)
            lemma = frame.frw_time_function_lemma()
            ceilings = {b: uses.trip_energy(b) for b in (0.8, 0.2, 0.1, 0.01)}
            kstar0 = seat.breakeven(0.0, 0.1, 1e-11)
            widen = create.theorems_apply_to_enlargement()
            sdc = sd.compute()["reservoirs"]["CI chondrite (primitive)"]
            cm = _load("cmbframe", os.path.join(D68, "cmb", "cmbframe.py"), "d68_cmbframe_chain")
            plx, splx = cm.PROXIMA_DIR["plx_mas"]
            sig_r = cm.L * splx / plx
            b_a = seat.FARIA_2022["b_a_au"] * seat.AU
            h0 = cosmo.H0()
    finally:
        sys.path[:] = saved
    co = coefficients()
    return {"coefficients": co, "z1": z1, "core_bits": core, "snap_bits": snap["grid_0p1A"], "floor_core": fl_core, "floor_snap": fl_snap,
            "floor_4core": fl_4, "misner_sharp": ms, "networks": (tested, bad), "frw_lemma": lemma,
            "ceilings": ceilings, "kstar_nothing_shipped": kstar0, "widen_is_topo": widen,
            "stock_ci": (sdc["binder"], sdc["factor"]), "address_sigma_r_m": sig_r, "proxima_b_a_m": b_a,
            "address_ratio": sig_r / b_a, "H0": h0}


WALLS = [
    ("W1 FORMATION", "making the identification is topology change; Geroch-Borde with the CMB clock as time function "
     "forbids it for a smooth, causally compact interpolation (D24 OPEN; frame.GRADES O-MAKE; create.py)",
     "R1 found and widened (M's answer 3): no topology change. Else R2 degenerate metric (READ Horowitz 1991, Borde "
     "IX.C), R5 non-compact (Tipler, READ at source), R6 a folded brane reconnecting through the bulk (PROPOSED)"),
    ("W2 REACHING POSITION 2", "in a well-posed theory an act at P1 cannot make P2 part of a corridor at the same "
     "instant (D23 as corrected; BULK5-O6)", "R1: a pre-existing throat already reaches P2; the act at P1 widens it"),
    ("W3 THROAT EXISTENCE", "R1 needs microscopic throats, common enough that one joins P1 to the chosen P2 (G9; the "
     "Ellis-throat null searches NOT READ)", "READ the searches and the foam literature (Wheeler; Visser ch. 6, 13); "
     "compute the abundance a found-throat route needs"),
    ("W4 THE BUILDER AT POSITION 2", "H-POSITION-BUILDS has no mechanism (STOCKDEST OPEN 6; S1C-O2); the README's "
     "1e15-bit size needs a builder that knows the recipe (H-REGENERABLE), and a bare position knows only physics",
     "READ constructor theory (Deutsch-Marletto) as the frame for 'a position that builds'; or the README carries the "
     "recipe (its size then rises toward the snapshot's)"),
    ("W5 ENERGY AT POSITION 2", "E_fab computed nowhere; the README's information buys at most N kT ln2 of work "
     "(Szilard): 8.1e-6 J for the core against up to 3.6e10 J of chemistry", "the stock's own free energy, or energy "
     "through the corridor (priced by Z3's floor)"),
    ("W6 THE GLOBAL BULK", "R = 0 throats need no plane matter locally (8m) but a global bulk with both mouths in one "
     "universe is BULK5-O1; the Weyl term's sustainer BULK4-O8", "construct the bulk, or READ Vollick and "
     "Bronnikov-Kim refs. 29, 35"),
    ("W7 THE COUPLING", "what at P1 writes the identification (O6 moved); H-TRIANGULATED-ACTION names no dynamics",
     "a Lagrangian for the device's input, or the stabilisation scalar (BULK3-O3)"),
    ("W8 ADDRESS PRECISION", "Gaia DR3's radial error at Proxima is hundreds of times Proxima b's orbit; nothing is "
     "sent to P2, so the address is extrapolated from received light", "micro-arcsecond astrometry or a longer "
     "baseline; the address carries its frame (the CMB slice)"),
    ("W9 THE READ", "the only read at synapse resolution destroys the tissue (COPY-O3)", "a non-destructive read; or "
     "H-RETIRE-A (left open by M) admits a destructive one"),
    ("W10 IDENTITY COMPLETENESS", "H-WIRING-SUFFICES unproved (COPY-O1); no formal fidelity criterion",
     "a READ whole-brain synapse total; a fidelity tolerance"),
    ("W11 THE SPLIT", "when the single-use corridor closes, on which side the README's physical record ends "
     "(unnamed: H-SPLIT-RULE)", "a rule, derived or ruled by M"),
]


def report():
    d = compute()
    z1 = d["z1"]
    print("chain.py -- the whole chain under M's theory (item 96; not verified; not seated)\n")
    print("Z1 the chain's logic (z3), each route: consistent? causal safety entailed?")
    for r, v in z1["routes"].items():
        print("   %-55s consistent: %-5s safety entailed: %s" % (
            r, v["consistent"], v["safety_entailed"] if v["consistent"] else "- (vacuous: the set is inconsistent)"))
    print("   vacuity control (H-MADE, no theorems): consistent %s" % z1["vacuity_made_no_theorems"]["consistent"])
    print("   the clauses (drift guard):")
    for name, src, cl in THEOREMS:
        print("     %-20s %-55s  [%s]" % (name, cl, src[:90]))
    print("Z2 proved under M's premises: K2 %d networks, %d loops; FRW lemma %s; k* (nothing shipped) = %s; widening is "
          "topology change: %s; stock at a CI body: %s at %.1f kg/kg" % (
              d["networks"][0], d["networks"][1], d["frw_lemma"].get("claim"), d["kstar_nothing_shipped"],
              d["widen_is_topo"], d["stock_ci"][0], d["stock_ci"][1]))
    fc, fs = d["floor_core"], d["floor_snap"]
    print("Z3 Misner-Sharp: m = %s, at a throat m = %s" % d["misner_sharp"])
    print("   one corridor's least energy (H-NECK-HOLDS, H-NECK-ENERGY): core %.3e J at a neck of %.3e m; largest "
          "snapshot %.3e J at %.3e m; E / (sqrt(hbar c^5/G) sqrt N) = %.9f" % (
              fc["E_J"], fc["r_m"], fs["E_J"], fs["r_m"], fc["E_J"] / (fc["E_planck_J"] * math.sqrt(d["core_bits"]))))
    print("   against the trips: %s" % ", ".join("%g c: %.3e J (core %s, snapshot %s)" % (
        b, e, "fits" if fc["E_J"] < e else "over", "fits" if fs["E_J"] < e else "over") for b, e in d["ceilings"].items()))
    print("M-COEFF (item 98): every coefficient, exact form and value (h, c, k_B exact; G u_r %.1e; H0 u_r %.1e):" % (
        U_R_G, d["coefficients"]["H0_per_s"]["u_r"]))
    for k, v in d["coefficients"].items():
        print("   %-24s %-46s = %s%s" % (k, v["form"], v["value_15"],
                                       "" if not v["u_r"] else "  (u_r %.1e)" % v["u_r"]))
    print("   core: E_min = %.10e J (= coefficient x sqrt(%.6e)); r_min = %.10e m" % (
        d["coefficients"]["E_min_J_per_sqrt_bit"]["value"] * math.sqrt(d["core_bits"]), d["core_bits"],
        d["coefficients"]["r_min_m_per_sqrt_bit"]["value"] * math.sqrt(d["core_bits"])))
    print("Cosmic beat (item 97): dT/T per cosmic second = H0 = %.3e /s (reading equal cosmic time to 1 s needs that "
          "precision; under R1 the geometry keys the joining, no reading needed)" % d["H0"])
    print("Address (W8): Gaia DR3 radial error %.3e m = %.0f x Proxima b's orbit (%.3e m)" % (
        d["address_sigma_r_m"], d["address_ratio"], d["proxima_b_a_m"]))
    print("\nZ4 THE WALLS, RANKED (the focus), with what would remove each:")
    for w, what, route in WALLS:
        print("  %s\n     %s\n     -> %s" % (w, what, route))


def selftest():
    n_pass = n_fail = n_ctl = n_con = 0
    structural = []

    def chk(label, ok, ctl=False, contrast=False):
        nonlocal n_pass, n_fail, n_ctl, n_con
        n_ctl += ctl
        n_con += contrast
        n_pass += bool(ok)
        n_fail += (not ok)
        print("  %s %s%s" % ("ok  " if ok else "FAIL", "CONTROL: " if ctl else ("CONTRAST: " if contrast else ""), label))

    d = compute()
    r = d["z1"]["routes"]
    made, r1 = r["H-MADE (as stated)"], r["R1 found and widened (H-COMMON-THROATS, H-NO-PINCH)"]
    r2, r5 = r["R2 made, degenerate metric (Borde IX.C)"], r["R5 made, non-compact interpolation"]
    r3 = r["R3 made, quantum topology change (N_QTOPO)"]
    chk("Z1: with the corridor MADE (smooth, causally compact, CMB clock, well-posed) M's premises are inconsistent",
        not made["consistent"])
    chk("Z1: FOUND AND WIDENED (M's answer 3) is consistent and entails causal safety",
        r1["consistent"] and r1["safety_entailed"])
    chk("Z1: a degenerate metric clears Geroch but not well-posedness; a non-compact interpolation likewise (both "
        "inconsistent while H-WELL-POSED holds)", (not r2["consistent"]) and (not r5["consistent"]))
    chk("Z1: quantum topology change is consistent but no longer entails safety (K2's model is lost)",
        r3["consistent"] and not r3["safety_entailed"], contrast=True)
    chk("the same made-corridor premises with NO theorems are consistent -- the inconsistency is the theorems'",
        d["z1"]["vacuity_made_no_theorems"]["consistent"], ctl=True)
    chk("drop the well-posedness clause and the degenerate-metric route becomes consistent -- that clause is "
        "the one R2 cannot clear", d["z1"]["R2_without_well_posed"]["consistent"], ctl=True)
    chk("Z2: keyed corridor networks close no loop (%d of %d); frame.py's FRW lemma is %s" % (
        d["networks"][1], d["networks"][0], d["frw_lemma"].get("claim")),
        d["networks"][1] == 0 and d["frw_lemma"].get("claim") == "unsat")
    chk("Z2: widening a throat is not topology change (create.theorems_apply_to_enlargement() = %s)" % d["widen_is_topo"],
        d["widen_is_topo"] is False)
    chk("Z3: Misner-Sharp at a throat is r0/2 (sympy: %s)" % d["misner_sharp"][1], d["misner_sharp"][1] == "r0/2")
    fc, fs, f4 = d["floor_core"], d["floor_snap"], d["floor_4core"]
    chk("Z3: the corridor's least energy goes as the square root of the README: 4 x the bits gives %.6f x the energy" % (
        f4["E_J"] / fc["E_J"]), abs(f4["E_J"] / fc["E_J"] - 2) < 1e-6)
    chk("Z3: E_min / sqrt(hbar c^5 / G) / sqrt(N) = sqrt(ln2 / (4 pi)): measured %.9f, exact %.9f" % (
        fc["E_J"] / (fc["E_planck_J"] * math.sqrt(d["core_bits"])), math.sqrt(math.log(2) / (4 * math.pi))),
        abs(fc["E_J"] / (fc["E_planck_J"] * math.sqrt(d["core_bits"])) / math.sqrt(math.log(2) / (4 * math.pi)) - 1)
        < 1e-6)
    co = d["coefficients"]
    chk("M-COEFF: the evaluated coefficient %.12e J per sqrt(bit) x sqrt(N) reproduces the bisected floor for the core "
        "(%.12e J) and the snapshot" % (co["E_min_J_per_sqrt_bit"]["value"], fc["E_J"]),
        abs(co["E_min_J_per_sqrt_bit"]["value"] * math.sqrt(d["core_bits"]) / fc["E_J"] - 1) < 1e-9 and
        abs(co["E_min_J_per_sqrt_bit"]["value"] * math.sqrt(d["snap_bits"]) / fs["E_J"] - 1) < 1e-9)
    chk("M-COEFF: the evaluated radius coefficient %.12e m per sqrt(bit) reproduces the bisected neck (%.12e m)" % (
        co["r_min_m_per_sqrt_bit"]["value"], fc["r_m"]),
        abs(co["r_min_m_per_sqrt_bit"]["value"] * math.sqrt(d["core_bits"]) / fc["r_m"] - 1) < 1e-9)
    chk("Z3: the core's corridor (%.3e J) fits under the 0.1 c trip (%.3e J); the largest snapshot's (%.3e J) fits under "
        "none" % (fc["E_J"], d["ceilings"][0.1], fs["E_J"]),
        fc["E_J"] < d["ceilings"][0.1] and all(fs["E_J"] > e for e in d["ceilings"].values()), contrast=True)
    chk("W8: the address's radial error (%.3e m) is more than 100 x Proxima b's orbit (%.3e m)" % (
        d["address_sigma_r_m"], d["proxima_b_a_m"]), d["address_ratio"] > 100)
    structural.append("the z3 clauses are the board's reading of each theorem (H-ENCODING), printed beside their "
                      "sources; a clause is only as good as its source's grade (most NARROWED, READ-VIA-RESTATEMENT)")
    structural.append("k* with nothing shipped = %s (uses U8)" % d["kstar_nothing_shipped"])
    structural.append("the cosmic beat: dT/T per cosmic second = H0 = %.3e /s" % d["H0"])
    structural.append("Z3 rests on H-NECK-HOLDS and H-NECK-ENERGY; with the plane's ADM total as the cost (which "
                      "can be 0, the hold reader's computation, unseated) the floor is removed -- OPEN, which energy M "
                      "means")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("chain.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, n_con, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    else:
        report()
