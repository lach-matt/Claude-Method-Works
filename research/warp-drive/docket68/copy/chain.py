#!/usr/bin/env python3
"""
chain.py -- the whole chain of warp travel re-run under M's theory (M-RULINGS item 96).  Deduced, computed and READ.
Not seated; verified once (2026-10-06).  M's words are carried as hypotheses, never as results.

M (item 96, verbatim): "Instead of trying to prove my theory of warp travel wrong. We need to focus on proving it right.
Assume that my theory is the only one in which warp travel is actually realizable. The whole chain of warp travel should
be entirely derivable from first principles and provable with math. Rerun the whole chain and reassess the
walls/obstructions/gaps. Those will be our focus."  Carried as H-M-THEORY: M's items 86-98 are the working premise set;
the board's other routes are the boundary (item 82).  A link is PROVED only from named premises; a WALL is a result that
blocks a link even under M's premises; a ROUTE is a named premise under which the wall does not bind; a GAP is what no
result on the board reaches.  Re-run by four readers over the board's owners (2026-10-06), assembled here.  Every
coefficient is evaluated (M-COEFF, item 98): an exact closed form in the constants, then its value; h, c, k_B exact; G
and H0 with their named uncertainties.

THE CHAIN UNDER M'S THEORY (stations, in order)
  ADDRESS  the device at position 1 takes position 2 as an input (H-ADDRESS-INPUT; H-TRIANGULATED-ACTION)
  READ     the object at position 1 is read (the identity core, faithful.py)
  README   the classical specification (H-README, H-COST-IN-README)
  MAKE     a corridor that also contains position 2, two places made one (H-CORRIDOR-CONTAINS-P2, H-IDENTIFY; made, H-MADE,
           or, M's alternative, found and widened, H-COMMON-THROATS)
  KEY      joined at the same instant of the cosmic clock, the CMB frame's beat (H-CMB-FRAME, H-COSMIC-BEAT)
  HOLD     held for a brief, non-zero, relative hold (H-BRIEF-HOLD); appears to contain negative energy, does not
           (H-READING-ONLY); single use (H-CORRIDOR-SINGLE-USE)
  CROSS    the README is present at position 2 (H-IDENTIFY: one point; H-README-IN-HOLD)
  BUILD    position 2 itself builds the copy from its own stock (H-POSITION-BUILDS, H-STOCK-IS-STOCK)
  COPY     the faithful copy is the goal (item 87)
  REPEAT   the device is reusable, corridors repeatable (H-DEVICE-REUSABLE, H-CORRIDOR-REPEATABLE)

WHAT FOLLOWS THE WORK
  * TWO WAYS THROUGH THE FORMATION WALLS, BOTH M'S (Z1, z3 over the board's reading of each theorem).  Of the routes
    encoded: FOUND AND WIDENED (H-COMMON-THROATS, item 86 answer 3: "if found and widened ... common and regular
    occurrences") is consistent and entails causal safety with no setup; a MADE corridor (H-MADE) is consistent and
    entails safety when its making begins at or below light speed before its joining instant (H-PRIOR-SETUP: D23's
    first trip, its corrected form needing only a common causal past) AND the joining is degenerate or non-compact (a
    non-compact one then meets Tipler: a singularity or a point at infinity, which the board's ruling M-S1A-P3 does not
    disqualify).  A corridor made at the joining instant from nothing, with a smooth compact interpolation and the CMB
    clock as time, is inconsistent with Geroch-Borde and finite propagation together.  A corridor made in an
    information layer (ITB, N_QTOPO; the charter's reading, no READ source) clears Geroch only.
    First written: "M'S OWN ANSWER 3 IS THE ROUTE THE THEOREMS LEAVE OPEN ... the only one that clears both walls" --
    the well-posedness clause was stronger than its sources and the quantum clause partly invented (verifier).
  * CARRIED FROM THE FOUR READERS, NOT ALL RECOMPUTED HERE (Z2; the ones computed here are marked): causal safety for
    every repetition (K2 COMPUTED; frame.py's FRW lemma COMPUTED: the geometry picks the beat); D13 satisfied with a zero
    bound once two places are one; demand rows D1-D4 and D8-D12 exclude a throat by their own scope (D7's analogue is
    the hold, below); zero-curvature throats need no plane matter -- locally, under H-RS1 (section 8m), globally OPEN
    (W6); widening is not topology change (COMPUTED, create.py); k* = 0 with nothing shipped (COMPUTED, uses U8); stock
    passes on quantity at a CI body (COMPUTED; Proxima's composition is wall W7).
  * ONE CORRIDOR'S ENERGY HAS A FIRST-PRINCIPLES LOWER BOUND THAT GROWS AS THE SQUARE ROOT OF THE README (Z3).  The
    Misner-Sharp mass at a throat of radius r is r c^4 / (2G) = 6.05127782e43 J/m x r (derived, sympy); Bekenstein's
    eq. (1) (READ in measure.py) gives E r >= N h c ln2 / (4 pi^2) = 3.48772679e-27 J m x N.  At the least r both hold:
    E_min = sqrt(N h c^5 ln2 / (8 pi^2 G)) = 4.59404002e8 J x sqrt(N), r_min = sqrt(N h G ln2 / (2 pi^2 c^3)) =
    7.59185111e-36 m x sqrt(N) (u_r 1.1e-5 from G).  There the neck sits at its own Schwarzschild radius and its area
    is exactly 4 ln2 Planck areas per bit -- the holographic bound (nopath.holographic_bits, computed): the floor is
    the strong-gravity form of Bekenstein's bound (Bousso's extrapolation, H-STRONG-BOUND).  Identity core:
    2.40587833e16 J at 3.97581866e-28 m, below the 0.1 c trip's 3.169e16 J; largest snapshot 1.515e23 J, above every
    trip.  Under H-NECK-HOLDS, H-NECK-ENERGY and H-STRONG-BOUND this is a LOWER BOUND on one corridor's energy that
    grows as the square root of the file; the cost itself is not computed.
    First written: "M's 'the cost is in ... how big the file is' gets an exact form: the cost of one corridor grows as
    the square root of the file" (a floor stated as a cost; verifier).
  * THE WALLS, RANKED (Z4) -- the focus -- each with what would remove it.

    python3 chain.py              report
    python3 chain.py --selftest   checks, CONTROLS and CONTRASTS marked, STRUCTURAL printed and not counted

Z1 [z3; the theorems as the board reads them, each with its source and grade]  Booleans for the chain's facts; each
   theorem an implication; M's premises asserted; satisfiability and entailment (axioms AND NOT safety unsat) per route.
   H-ENCODING: the encoding is the board's reading of each theorem; the clauses are printed beside their sources and
   grades (the drift guard); controls: no theorems; drop one clause; pinch; K2 dropped.
Z2 [imported where marked]  causal/frame (K2, the FRW lemma), uses (k*), stockdest, create (enlargement).
Z3 [derived, sympy; imported]  Misner-Sharp m = (r/2)(1 - g^rr) at a throat, g^rr(r0) = 0; measure.bekenstein_floor_j;
   nopath.holographic_bits; seat's constants; uses.trip_energy.
Z4 [the four readers' reports, each wall with its owner]  as data; their numbers printed from the owners.
Also computed: the cosmic beat (item 97): the CMB temperature falls as 1/a, dT/T = -H0 dt; the measured T0 =
   2.72548 +- 0.00057 K (Fixsen 2009, READ in cmbframe.py) fixes cosmic time locally to (dT/T)/H0; the address error
   (cmbframe's Gaia DR3 row) against Proxima b's orbit (seat's Faria row).

NAMED HYPOTHESES
  M's (items 86-98): H-M-THEORY, H-ADDRESS-INPUT, H-TRIANGULATED-ACTION, H-README, H-COST-IN-README, H-STOCK-IS-STOCK,
  H-POSITION-BUILDS, H-CORRIDOR-CONTAINS-P2, H-IDENTIFY, H-MADE, H-COMMON-THROATS, H-CMB-FRAME, H-COSMIC-BEAT,
  H-BRIEF-HOLD, H-READING-ONLY, H-SEEN-BY-INTERACTION, H-CORRIDOR-SINGLE-USE, H-DEVICE-REUSABLE, H-CORRIDOR-REPEATABLE,
  H-SINGLE-CHANNEL-GROWS, H-README-IN-HOLD, H-NO-MOVEMENT, H-INSTANTANEOUS, H-UNIDENTIFIED-CARRIER, H-RETIRE-A (open);
  M-COEFF and M-DEDUCE (method).
  The board's: H-ENCODING; H-NO-PINCH (a widened throat keeps r > 0; a pinch is topology change); H-WELL-POSED
  (finite propagation, the board's reading, ungraded, NOT READ); H-PRIOR-SETUP (a made corridor's making begins at <= c
  before its joining); H-FOUND-KEYED (a found throat is a keyed Lorentzian quotient whose mouths sit at equal cosmic
  time -- R1's safety rests on it; a foam origin would be quantum, which QTOPO-BREAKS-MODEL says breaks the model);
  H-CORRIDOR-MODEL; H-FRW-EXACT; H-NOT-DE-SITTER; H-NECK-HOLDS; H-NECK-ENERGY (the corridor's cost is the neck's
  Misner-Sharp energy; the matter outside can integrate to the opposite sign, so the plane's total can differ -- OPEN);
  H-STRONG-BOUND (Bekenstein's eq. (1) at Schwarzschild saturation, where it equals the holographic bound -- Bousso's
  extrapolation per nopath.py's DOCKET 67 correction, outside the bound's weakly-self-gravitating class, and used as a
  corridor floor against measure.bekenstein_floor_j's stated scope); H-SPLIT-RULE (unnamed until now: on which side the
  README's record ends); H-RS1; H-REGENERABLE; H-WIRING-SUFFICES; H-IDENTITY-IN-DYNAMICS.

HISTORY (verifier, 2026-10-06)
  * WELL-POSED was "Made & WellPosed -> False", sourced to BULK5-O6 and D23; BULK5-O6 is the bulk-embedding objection
    and D23 as corrected needs only a common causal past.  Now the board's reading, ungraded: "Made & WellPosed &
    !PriorSetup -> False"; routes R7a/R7b (made with a light-time setup) added.
  * QTOPO-ESCAPES asserted !WellPosed with no source; now "QuantumTopo -> !Smooth" (the charter's reading); R3
    relabelled an information-layer corridor.
  * GEROCH-BORDE merged two clauses; now "Topo & CausallyCompact & Smooth -> CTC" with TF-NO-CTC and "CTC -> !Safe".
  * WIDEN-NOT-TOPO and H-NO-PINCH were inert; PINCH-IS-TOPO added, with a pinch control.
  * Tipler was not encoded; now "Topo & !CausallyCompact & EnergyCond -> Singular" (Singular not disqualified,
    M-S1A-P3).
  * Z3 applied Bekenstein at Schwarzschild saturation unnamed (H-STRONG-BOUND added; holographic check added); a floor
    was called a cost; the Z2 list claimed computation for carried results; W5's "3.6e10 J of chemistry" had no owner
    (removed); the Misner-Sharp and sqrt(N) checks were definitional (now STRUCTURAL).

ITEM 99 (M: "Read my answers first, then ask any questions left open."; not yet verified)
  * The neck's area at the floor, A_min = N 2 h G ln2 / (pi c^3) = 7.24277891e-70 m^2 x N, is added to the M-COEFF
    table and checked against the bisected necks: one channel growing in direct proportion to the README (items 93-94).
  * The cost is read as the neck's energy from M's item 89 (H-COST-IN-README); first written "OPEN, which energy M
    means".  H-PRIOR-SETUP read from item 86 answer 4 (R-ENTANGLED-SETUP, CHAIN.md); H-FOUND-KEYED from item 97 with
    frame.py's lemma.  No clause or route changes.
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
        _CACHE["nopath"] = _load("nopath", os.path.join(WD, "nopath.py"), "wd_nopath_chain")
        _CACHE["stockdest"] = _load("stockdest", os.path.join(HERE, "stockdest.py"), "copy_stockdest_chain")
        _CACHE["cmbframe"] = _load("cmbframe", os.path.join(D68, "cmb", "cmbframe.py"), "d68_cmbframe_chain")
    return _CACHE


# ============================================================================================ Z1: the chain's logic
THEOREMS = [
    # (name, clause as text, source and grade)
    ("MADE-IS-TOPO", "Made -> Topo", "create.py: bringing a throat into existence is topology change (D24 OPEN)"),
    ("WIDEN-NOT-TOPO", "Found & Widen & NoPinch & !Made -> !Topo",
     "create.theorems_apply_to_enlargement() = False; GRADES topology-change-vs-metric-change NARROWED (Borde READ)"),
    ("PINCH-IS-TOPO", "Widen & !NoPinch -> Topo", "create.py / D24: the throat radius must stay above 0 throughout"),
    ("GEROCH-BORDE", "Topo & CausallyCompact & Smooth -> CTC",
     "Geroch 1967 / Borde Thm 1, GRADES geroch-1967-topology-change NARROWED, READ-VIA-RESTATEMENT; frame.GRADES O-MAKE"),
    ("TIPLER", "Topo & !CausallyCompact & EnergyCond -> Singular",
     "Tipler 1977, GRADES tipler-1977-singularities-topology-change NARROWED, NOT READ at source; a singular throat is "
     "not disqualified (M-S1A-P3)"),
    ("WELL-POSED", "Made & WellPosed & !PriorSetup -> False",
     "the board's reading (ungraded, NOT READ): finite propagation in a well-posed theory -- an act at P1 cannot make P2 "
     "part of a corridor at the same instant with no prior connection or common causal past (D23 as corrected: a common "
     "causal past suffices); BULK5-O6 is the bulk-embedding analogue, OPEN"),
    ("CMB-IS-TF", "CMBKey -> TimeFunction", "H-CMB-FRAME; frame.py's FRW lemma (z3); LSV p.16 stable causality, READ"),
    ("TF-NO-CTC", "TimeFunction -> !CTC", "a global time function excludes closed timelike curves (LSV p.16, READ)"),
    ("CTC-UNSAFE", "CTC -> !Safe", "a closed timelike curve is the loop safety excludes (definition)"),
    ("K2", "CMBKey & CorridorModel & Corridor -> Safe",
     "frame.cosmic_keyed_rank_n_is_safe, latticectc D21 THEOREM, causal.py K2"),
    ("QTOPO-BREAKS-MODEL", "QuantumTopo -> !CorridorModel",
     "geometry.py / frame.GRADES: under N_QTOPO the corridor is not the Lorentzian quotient K2 covers"),
    ("QTOPO-ESCAPES", "QuantumTopo -> !Smooth",
     "geometry.py ITB/N_QTOPO: Geroch/Tipler say nothing about an information-layer corridor -- the charter's reading, "
     "no READ source"),
    ("CORRIDOR-ORIGIN", "Corridor -> Made | (Found & Widen)", "M's item 86 answer 3: made, or found and widened"),
]

ROUTES = {
    "H-MADE at the joining instant (smooth, compact)": {"Made": True, "PriorSetup": False},
    "R1 found and widened (H-COMMON-THROATS, H-NO-PINCH, H-FOUND-KEYED)": {"Made": False, "Found": True, "Widen": True,
                                                                         "NoPinch": True},
    "R2 made at the instant, degenerate metric": {"Made": True, "PriorSetup": False, "smooth metric": False},
    "R5 made at the instant, non-compact": {"Made": True, "PriorSetup": False, "causally compact": False},
    "R3 made in an information layer (ITB, N_QTOPO; no READ realisation)": {"Made": True, "PriorSetup": False, "QuantumTopo": True,
                                                                          "smooth metric": None, "corridor model": None},
    "R7a made with a light-time setup (H-PRIOR-SETUP), degenerate joining": {"Made": True, "PriorSetup": True,
                                                                           "smooth metric": False},
    "R7b made with a light-time setup (H-PRIOR-SETUP), non-compact joining": {"Made": True, "PriorSetup": True,
                                                                            "causally compact": False},
}


def z3_chain(routes=None, drop=None):
    import z3
    names = ["Corridor", "Made", "Found", "Widen", "NoPinch", "Topo", "CausallyCompact", "Smooth", "TimeFunction",
             "WellPosed", "PriorSetup", "CMBKey", "CTC", "CorridorModel", "Safe", "QuantumTopo", "EnergyCond",
             "Singular"]
    V = {n: z3.Bool(n) for n in names}
    I, A, N, O = z3.Implies, z3.And, z3.Not, z3.Or
    clause = {
        "MADE-IS-TOPO": I(V["Made"], V["Topo"]),
        "WIDEN-NOT-TOPO": I(A(V["Found"], V["Widen"], V["NoPinch"], N(V["Made"])), N(V["Topo"])),
        "PINCH-IS-TOPO": I(A(V["Widen"], N(V["NoPinch"])), V["Topo"]),
        "GEROCH-BORDE": I(A(V["Topo"], V["CausallyCompact"], V["Smooth"]), V["CTC"]),
        "TIPLER": I(A(V["Topo"], N(V["CausallyCompact"]), V["EnergyCond"]), V["Singular"]),
        "WELL-POSED": N(A(V["Made"], V["WellPosed"], N(V["PriorSetup"]))),
        "CMB-IS-TF": I(V["CMBKey"], V["TimeFunction"]),
        "TF-NO-CTC": I(V["TimeFunction"], N(V["CTC"])),
        "CTC-UNSAFE": I(V["CTC"], N(V["Safe"])),
        "K2": I(A(V["CMBKey"], V["CorridorModel"], V["Corridor"]), V["Safe"]),
        "QTOPO-BREAKS-MODEL": I(V["QuantumTopo"], N(V["CorridorModel"])),
        "QTOPO-ESCAPES": I(V["QuantumTopo"], N(V["Smooth"])),
        "CORRIDOR-ORIGIN": I(V["Corridor"], O(V["Made"], A(V["Found"], V["Widen"]))),
    }
    m_axioms = [V["Corridor"], V["CMBKey"], V["EnergyCond"]]      # EnergyCond: H-READING-ONLY, nothing negative held
    classical = {"smooth metric": V["Smooth"], "causally compact": V["CausallyCompact"],
                 "well-posed (H-WELL-POSED)": V["WellPosed"], "corridor model": V["CorridorModel"]}
    drops = set([drop] if isinstance(drop, str) else (drop or []))

    def solve(route, with_theorems=True):
        res = {}
        for negate_safe in (False, True):
            s = z3.Solver()
            if with_theorems:
                for k, c in clause.items():
                    if k not in drops:
                        s.add(c)
            for c in m_axioms:
                s.add(c)
            for k, c in classical.items():
                if k in route and route[k] is None:
                    continue
                s.add(z3.Not(c) if (k in route and route[k] is False) else c)
            for k, val in route.items():
                if k in V:
                    s.add(V[k] if val else z3.Not(V[k]))
            if negate_safe:
                s.add(z3.Not(V["Safe"]))
            res[negate_safe] = str(s.check())
            if not negate_safe and res[False] == "sat":
                m = s.model()
                res["singular"] = bool(z3.is_true(m.eval(V["Singular"], model_completion=True))) and \
                    not str(z3.Solver().check()) == "unknown"
        out = {"consistent": res[False] == "sat", "safety_entailed": res[True] == "unsat"}
        if out["consistent"]:
            s2 = z3.Solver()
            for k, c in clause.items():
                if k not in drops:
                    s2.add(c)
            for c in m_axioms:
                s2.add(c)
            for k, c in classical.items():
                if k in route and route[k] is None:
                    continue
                s2.add(z3.Not(c) if (k in route and route[k] is False) else c)
            for k, val in route.items():
                if k in V:
                    s2.add(V[k] if val else z3.Not(V[k]))
            s2.add(z3.Not(V["Singular"]))
            out["singularity_forced"] = str(s2.check()) == "unsat"
        return out

    rts = routes or ROUTES
    return {r: solve(spec) for r, spec in rts.items()}, (lambda spec: solve(spec, with_theorems=False))


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
        "neck_area_m2_per_bit": (2 * h * G * sp.log(2) / (sp.pi * c ** 3), U_R_G,
                                 "A_min = 4 pi r_min^2 = N 2 h G ln2 / (pi c^3) (item 99: the one channel's size per bit)"),
        "szilard_J_per_bit_310K": (kB * T * sp.log(2), 0.0, "W <= N k_B T ln2 at T = 310 K"),
    }
    out = {}
    for k, (expr, ur, form) in defs.items():
        out[k] = {"form": form, "exact": str(sp.nsimplify(expr)), "value": float(sp.N(expr, 20)),
                  "value_15": str(sp.N(expr, 15)), "u_r": ur}
    out["H0_per_s"] = {"form": "H0 = 67.36 km/s/Mpc / Mpc", "exact": "measured (Planck 2018, +- 0.54 km/s/Mpc)",
                       "value": cosmo.H0(), "value_15": "%.6e" % cosmo.H0(), "u_r": 0.54 / 67.36}
    return out


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
    energy (H-NECK-HOLDS, H-NECK-ENERGY, H-STRONG-BOUND)."""
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
    return {"r_m": hi, "E_J": hi * e_per_m, "holographic_bits": o["nopath"].holographic_bits(hi),
            "schwarzschild_m": 2 * seat.G * hi * e_per_m / seat.C ** 4}


# ============================================================================================ compute
def compute():
    o = owners()
    uses, frame, create, sd, cm = (o[k] for k in ("uses", "frame", "create", "stockdest", "cmbframe"))
    seat, fa, ca = uses.owners()
    saved = list(sys.path)
    sys.path[:0] = [D68, WD]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            z1, no_theorems = z3_chain()
            controls = {
                "made_no_theorems": no_theorems(ROUTES["H-MADE at the joining instant (smooth, compact)"]),
                "R2_without_well_posed": z3_chain({"r2": ROUTES["R2 made at the instant, degenerate metric"]},
                                                  drop="WELL-POSED")[0]["r2"],
                "R1_pinched": z3_chain({"p": dict(ROUTES["R1 found and widened (H-COMMON-THROATS, H-NO-PINCH, "
                                                         "H-FOUND-KEYED)"], NoPinch=False)})[0]["p"],
                "R1_without_K2": z3_chain({"k": ROUTES["R1 found and widened (H-COMMON-THROATS, H-NO-PINCH, "
                                                       "H-FOUND-KEYED)"]}, drop="K2")[0]["k"],
                "R7a_without_prior": z3_chain({"q": dict(ROUTES["R7a made with a light-time setup (H-PRIOR-SETUP), "
                                                                "degenerate joining"], PriorSetup=False)})[0]["q"],
            }
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
            plx, splx = cm.PROXIMA_DIR["plx_mas"]
            sig_r = cm.L * splx / plx
            b_a = seat.FARIA_2022["b_a_au"] * seat.AU
            co = coefficients()
            t0, st0 = cm.T0
            beat_dt = (st0 / t0) / co["H0_per_s"]["value"]
    finally:
        sys.path[:] = saved
    return {"coefficients": co, "z1": z1, "controls": controls, "core_bits": core, "snap_bits": snap["grid_0p1A"],
            "floor_core": fl_core, "floor_snap": fl_snap, "floor_4core": fl_4, "misner_sharp": ms,
            "networks": (tested, bad), "frw_lemma": lemma, "ceilings": ceilings, "kstar_nothing_shipped": kstar0,
            "widen_is_topo": widen, "stock_ci": (sdc["binder"], sdc["factor"]), "address_sigma_r_m": sig_r,
            "proxima_b_a_m": b_a, "address_ratio": sig_r / b_a, "T0": (t0, st0), "beat_dt_s": beat_dt,
            "szilard_core_J": co["szilard_J_per_bit_310K"]["value"] * core}


WALLS = [
    ("W1 FORMATION", "making the identification is topology change; with a smooth compact interpolation Geroch-Borde "
     "force a CTC, which the CMB clock excludes (D24 OPEN; frame.GRADES O-MAKE; create.py)",
     "R1 found and widened (M's answer 3): no topology change.  R7: made with a light-time setup and a degenerate (READ "
     "Horowitz 1991, Borde IX.C) or non-compact (Tipler: a singularity, not disqualified by M-S1A-P3) joining.  R6 a "
     "folded brane reconnecting through the bulk (PROPOSED)"),
    ("W2 REACHING POSITION 2", "finite propagation (the board's reading, ungraded): an act at P1 cannot make P2 part of a "
     "corridor at the same instant with no prior connection (D23 as corrected: a common causal past suffices)",
     "R1: a pre-existing throat already reaches P2.  R7: the making begins at <= c before the joining (H-PRIOR-SETUP)"),
    ("W3 THROAT EXISTENCE (R1)", "found-and-widened needs throats, keyed at the cosmic beat (H-FOUND-KEYED), common "
     "enough that one joins P1 to the chosen P2 (G9; the Ellis-throat null searches NOT READ in D24)",
     "READ the searches and the throat literature (Visser, Lorentzian Wormholes); compute the abundance needed; a foam "
     "origin is quantum and would need its own safety proof"),
    ("W4 THE CORRIDOR'S ENERGY", "Z3's floor at P1: one corridor needs at least the printed energy under H-NECK-ENERGY "
     "and H-STRONG-BOUND", "the plane-total reading (the matter outside the neck can integrate to the opposite sign; "
     "H-NECK-ENERGY OPEN -- which energy M means)"),
    ("W5 THE BUILDER AT POSITION 2", "no READ or computed mechanism makes a position execute a specification "
     "(STOCKDEST OPEN 6, COPY-O2, S1C-O2); the core-sized README needs a builder that knows the recipe (H-REGENERABLE)",
     "READ constructor theory (Deutsch-Marletto) as the frame for M's H-POSITION-BUILDS; or the README carries the "
     "recipe (its size rises toward the snapshot's)"),
    ("W6 ENERGY AT POSITION 2", "E_fab computed nowhere (seat.py); the README's information buys at most N k_B T ln2 of "
     "work (Szilard; computed)", "the stock's own free energy, or energy through the corridor"),
    ("W7 THE DESTINATION'S COMPOSITION", "Proxima b and d unmeasured (COPY-O4); what a site's composition adds to the "
     "README (COPY-O5)", "a transit, an emission spectrum, direct imaging"),
    ("W8 THE GLOBAL BULK", "zero-curvature throats need no plane matter locally under H-RS1 (8m); a global bulk with both "
     "mouths in one universe is BULK5-O1; the Weyl term's sustainer BULK4-O8", "construct the bulk, or READ Vollick and "
     "Bronnikov-Kim refs. 29, 35"),
    ("W9 THE COUPLING", "what at P1 widens the throat or writes the identification (O6 moved); H-TRIANGULATED-ACTION "
     "names no dynamics", "a Lagrangian for the device's input, or the stabilisation scalar (BULK3-O3)"),
    ("W10 ADDRESS PRECISION", "the radial error at Proxima against Proxima b's orbit (computed); under R1 it is "
     "subordinate to W3, since a found throat's far mouth is where it is", "micro-arcsecond astrometry or a longer "
     "baseline; the address carries its frame (the CMB slice)"),
    ("W11 THE READ", "the only read at synapse resolution destroys the tissue (COPY-O3)", "a non-destructive read; or "
     "H-RETIRE-A (left open by M) admits a destructive one"),
    ("W12 IDENTITY COMPLETENESS", "H-WIRING-SUFFICES unproved (COPY-O1); no fidelity criterion", "a READ whole-brain "
     "synapse total; a tolerance"),
    ("W13 THE SPLIT", "when the single-use corridor closes, on which side the README's record ends (H-SPLIT-RULE)",
     "a rule, derived or ruled by M"),
]


def report():
    d = compute()
    co = d["coefficients"]
    print("chain.py -- the whole chain under M's theory (item 96; verified once; not seated)\n")
    print("Z1 the chain's logic (z3): consistent?  safety entailed?  singularity forced?")
    for r, v in d["z1"].items():
        print("   %-72s %-5s %-5s %s" % (r, v["consistent"], v["safety_entailed"] if v["consistent"] else "-",
                                       v.get("singularity_forced", "-")))
    print("   the clauses (drift guard):")
    for name, cl, src in THEOREMS:
        print("     %-19s %-48s [%s]" % (name, cl, src[:100]))
    print("Z2 computed here: K2 %d networks, %d loops; FRW lemma %s; k* (nothing shipped) = %s; widening is topology "
          "change: %s; stock at a CI body: %s at %.1f kg/kg (the rest carried from the readers)" % (
              d["networks"][0], d["networks"][1], d["frw_lemma"].get("claim"), d["kstar_nothing_shipped"],
              d["widen_is_topo"], d["stock_ci"][0], d["stock_ci"][1]))
    print("M-COEFF (item 98): every coefficient, exact form and value (h, c, k_B exact; G u_r %.1e; H0 u_r %.1e):" % (
        U_R_G, co["H0_per_s"]["u_r"]))
    for k, v in co.items():
        print("   %-24s %-46s = %s%s" % (k, v["form"], v["value_15"], "" if not v["u_r"] else "  (u_r %.1e)" % v["u_r"]))
    fc, fs = d["floor_core"], d["floor_snap"]
    print("Z3 Misner-Sharp: m = %s, at a throat m = %s" % d["misner_sharp"])
    print("   one corridor's least energy: core %.10e J at a neck of %.10e m (its Schwarzschild radius %.10e m; "
          "holographic bits %.6e vs N %.6e); largest snapshot %.4e J at %.4e m" % (
              fc["E_J"], fc["r_m"], fc["schwarzschild_m"], fc["holographic_bits"], d["core_bits"], fs["E_J"],
              fs["r_m"]))
    print("   trips whose energy lies above the floor: %s" % ", ".join("%g c: %.4e J (core %s, snapshot %s)" % (
        b, e, "below" if fc["E_J"] < e else "above", "below" if fs["E_J"] < e else "above")
        for b, e in d["ceilings"].items()))
    print("Cosmic beat (item 97): dT/T = -H0 dt, H0 = %.6e /s; T0 = %.5f +- %.5f K (Fixsen) fixes cosmic time locally "
          "to %.3e s (%.2e yr); under R1 the joining is keyed by the throat (H-FOUND-KEYED), not by a reading" % (
              co["H0_per_s"]["value"], d["T0"][0], d["T0"][1], d["beat_dt_s"], d["beat_dt_s"] / 3.15576e7))
    print("Address (W10): Gaia DR3 radial error %.4e m = %.0f x Proxima b's orbit (%.4e m)" % (
        d["address_sigma_r_m"], d["address_ratio"], d["proxima_b_a_m"]))
    print("Szilard (W6): the core's README buys at most %.4e J of work at 310 K" % d["szilard_core_J"])
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
    r, c = d["z1"], d["controls"]
    made = r["H-MADE at the joining instant (smooth, compact)"]
    r1 = r["R1 found and widened (H-COMMON-THROATS, H-NO-PINCH, H-FOUND-KEYED)"]
    r2, r5 = r["R2 made at the instant, degenerate metric"], r["R5 made at the instant, non-compact"]
    r3 = r["R3 made in an information layer (ITB, N_QTOPO; no READ realisation)"]
    r7a = r["R7a made with a light-time setup (H-PRIOR-SETUP), degenerate joining"]
    r7b = r["R7b made with a light-time setup (H-PRIOR-SETUP), non-compact joining"]
    chk("Z1: a corridor MADE at the joining instant (smooth, compact, CMB clock, well-posed) is inconsistent",
        not made["consistent"])
    chk("Z1: FOUND AND WIDENED is consistent and entails causal safety, no singularity forced",
        r1["consistent"] and r1["safety_entailed"] and not r1["singularity_forced"])
    chk("Z1: MADE with a light-time setup and a degenerate joining is consistent and entails safety",
        r7a["consistent"] and r7a["safety_entailed"])
    chk("Z1: MADE with a light-time setup and a non-compact joining is consistent, entails safety, and forces a "
        "singularity (Tipler; not disqualified, M-S1A-P3)",
        r7b["consistent"] and r7b["safety_entailed"] and r7b["singularity_forced"])
    chk("Z1: made at the instant with a degenerate or non-compact joining, or in an information layer, stays "
        "inconsistent (finite propagation)", not r2["consistent"] and not r5["consistent"] and not r3["consistent"],
        contrast=True)
    chk("the made-corridor premises with NO theorems are consistent -- the inconsistency is the theorems'",
        c["made_no_theorems"]["consistent"], ctl=True)
    chk("drop finite propagation and the degenerate route at the instant becomes consistent -- that is the clause it "
        "cannot clear", c["R2_without_well_posed"]["consistent"], ctl=True)
    chk("found and widened with a PINCH is inconsistent (H-NO-PINCH is load-bearing)", not c["R1_pinched"]["consistent"],
        ctl=True)
    chk("found and widened without K2 no longer entails safety (K2 carries it)",
        c["R1_without_K2"]["consistent"] and not c["R1_without_K2"]["safety_entailed"], ctl=True)
    chk("the degenerate made route without the light-time setup is inconsistent (H-PRIOR-SETUP is load-bearing)",
        not c["R7a_without_prior"]["consistent"], ctl=True)
    chk("Z2: keyed corridor networks close no loop (%d of %d); frame.py's FRW lemma is %s" % (
        d["networks"][1], d["networks"][0], d["frw_lemma"].get("claim")),
        d["networks"][1] == 0 and d["frw_lemma"].get("claim") == "unsat")
    chk("Z2: widening a throat is not topology change (create.theorems_apply_to_enlargement() = %s)" % d["widen_is_topo"],
        d["widen_is_topo"] is False)
    co, fc, fs = d["coefficients"], d["floor_core"], d["floor_snap"]
    chk("Z3: at the floor the neck holds exactly the holographic count (nopath.holographic_bits %.9e against N %.9e) and "
        "sits at its own Schwarzschild radius (%.9e m vs %.9e m)" % (fc["holographic_bits"], d["core_bits"],
                                                                     fc["schwarzschild_m"], fc["r_m"]),
        abs(fc["holographic_bits"] / d["core_bits"] - 1) < 1e-6 and abs(fc["schwarzschild_m"] / fc["r_m"] - 1) < 1e-9)
    chk("M-COEFF: the evaluated coefficient %.12e J per sqrt(bit) x sqrt(N) reproduces the bisected floor for the core "
        "(%.12e J) and the snapshot" % (co["E_min_J_per_sqrt_bit"]["value"], fc["E_J"]),
        abs(co["E_min_J_per_sqrt_bit"]["value"] * math.sqrt(d["core_bits"]) / fc["E_J"] - 1) < 1e-9 and
        abs(co["E_min_J_per_sqrt_bit"]["value"] * math.sqrt(d["snap_bits"]) / fs["E_J"] - 1) < 1e-9)
    chk("M-COEFF: the evaluated radius coefficient %.12e m per sqrt(bit) reproduces the bisected neck (%.12e m)" % (
        co["r_min_m_per_sqrt_bit"]["value"], fc["r_m"]),
        abs(co["r_min_m_per_sqrt_bit"]["value"] * math.sqrt(d["core_bits"]) / fc["r_m"] - 1) < 1e-9)
    chk("M-COEFF, item 99: the evaluated area coefficient %.12e m^2 per bit reproduces the bisected neck's area for the "
        "core, and the snapshot's area over the core's equals its bits over the core's (%.9e vs %.9e): the one "
        "channel's area grows in direct proportion to the README (H-SINGLE-CHANNEL-GROWS)" % (
            co["neck_area_m2_per_bit"]["value"], (fs["r_m"] / fc["r_m"]) ** 2, d["snap_bits"] / d["core_bits"]),
        abs(co["neck_area_m2_per_bit"]["value"] * d["core_bits"] / (4 * math.pi * fc["r_m"] ** 2) - 1) < 1e-9 and
        abs((fs["r_m"] / fc["r_m"]) ** 2 / (d["snap_bits"] / d["core_bits"]) - 1) < 1e-9)
    chk("Z3: the core's floor (%.6e J) lies below the 0.1 c trip (%.6e J); the largest snapshot's (%.4e J) above every "
        "trip" % (fc["E_J"], d["ceilings"][0.1], fs["E_J"]),
        fc["E_J"] < d["ceilings"][0.1] and all(fs["E_J"] > e for e in d["ceilings"].values()), contrast=True)
    chk("W10: the address's radial error (%.4e m) is more than 100 x Proxima b's orbit (%.4e m)" % (
        d["address_sigma_r_m"], d["proxima_b_a_m"]), d["address_ratio"] > 100)
    structural.append("Z3 Misner-Sharp at a throat is r0/2 (sympy: %s) -- follows from b(r0) = r0 (first counted)" %
                      d["misner_sharp"][1])
    structural.append("Z3 the floor scales as sqrt(N): 4 x the bits gives %.6f x the energy -- E ~ r with E ~ 1/r "
                      "(first counted)" % (d["floor_4core"]["E_J"] / fc["E_J"]))
    structural.append("the z3 clauses are the board's reading of each theorem (H-ENCODING), printed beside their "
                      "sources; WELL-POSED is ungraded and NOT READ; QTOPO-ESCAPES is the charter's reading")
    structural.append("k* with nothing shipped = %s (uses U8)" % d["kstar_nothing_shipped"])
    structural.append("the cosmic beat: T0's measured precision fixes cosmic time locally to %.3e s" % d["beat_dt_s"])
    structural.append("Z3 rests on H-NECK-HOLDS, H-NECK-ENERGY and H-STRONG-BOUND; the neck's energy is the one read as "
                      "the cost from M's own answers (item 99: H-COST-IN-README -- the plane's total can be zero at "
                      "any N); first written 'with the plane's total as the cost the floor is removed -- OPEN, which energy "
                      "M means'")
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
