#!/usr/bin/env python3
"""f1_audit.py -- the Warp Theorem's input F1 audited: eq. (17) as our plane's own metric, demoted by seated clause (G)
(item 187) to "a plane's possible reading of the corridor's mouth".  Computed, READ and deduced; checked by two separate
AI sessions in this project, findings applied; not seated; 2026-10-09.  Note: lemmas/F1-AUDIT.md.

WHAT THIS DOES.  Twelve lemmas of warptheorem.py rest on F1 -- H2, O1, O2, Z1, Z2, B1, B2, B4b, B4d, E4 (B3 through B4)
  as the item-192 audit listed them, and G1, G3, which that list carried F1-free although axioms.derive_h2_g1 places the
  horizon with eq. (17)'s F = 0 (G1's E(N) = r0 c^4/(2G) is the plane's horizon relation r_h = 2Gm/c^2).
  PART A re-runs each one's decisive check from its owner, by path (bulk/stability.py, bulk/passage5d.py, copy/coin.py,
         copy/plane.py, copy/exactE.py, bulk/localbulk.py, lemmas/ledger.py, lemmas/b4_static.py, lemmas/b4d_stage6.py,
         lemmas/axioms.py).  Every decisive check still passes.  What they establish is a statement about eq. (17) on a
         matter-free plane at the RS tension (inputs F1 and F2); O1's "nonsingular" is OPEN even there (plane.py P1).
  PART B what survives without F1.  H2's qualitative form and O1's direction are DERIVED from M's 132 (with 130), carried
         as M's -- no axiom is claimed.  For a Z2-symmetric plane of tension q sigma_RS bounding the vacuum bulk, with any
         symmetric plane matter tau: Z1q, q 8 pi G tau(k,k) + kappa5^4 pi(k,k) = R4(k,k) + R5(n,k,n,k), and B1q, Gauss
         -R4 = -12(q^2 - 1)/ell^2 + q 8 pi G tau + kappa5^4 (tau.tau/4 - tau^2/12) with Codazzi (computed, symbolic; on
         the standard-not-READ Gauss equation and Israel junction).  Our plane is q = 1; the q = 1 forms FAIL at position
         2's q < 0, and a plane without Z2 symmetry is outside (its K is not fixed by tau).  pi(k,k) is not sign-definite
         under the NEC.  Two negative results: a horizon on the throat does not force extremality, and a plane tangent
         to the bulk's Killing field reads the bulk's surface gravity.
  PART C states M1 (H-PLANE-READS-MOUTH as a theorem, OPEN) with its clauses and the stronger M1-P2 and M1-global, and
         computes: the 4D-limit candidate's net -Q per ray (against 183); the matter-free plane's near-horizon bulk
         singular at SIM2's y_s; the regular single-plane caps (KR's compact-horizon class) and the plane matter they
         need -- positive, NEC-obeying, never our universe's (so the single-plane form fails ON THE BOARD'S READING
         H-OWN-MATTER-ONLY, at the computed grid points, numerical RK4 without error control); M1-c's error bound from
         our matter and the observed dark energy, which excludes M1-global in its exact form; the question "may our
         plane carry the README's stress at the mouth" put to the cypher (196), which does not decide it; and the green
         table, its statuses imported from warptheorem.py and its inputs from the item-192 list (b1_matter.py).

LABELS.  computed / READ (verbatim + page) / deduced / STRUCTURAL / standard-not-READ / OPEN, on every result.
M'S WORDS USED (verbatim, typing kept; M-RULINGS-2026-10-03.md):
  132  "do the horizons still hold the README too (your item 106), as well as the throat? - yes. And the passage is one
       way by nature, a black hole in and a white hole out, side views of the same corridor object"
       "*different views of the same object"
  129 (1) "... just not a corridor for transit because the corridor is a bridge, so it adds nothing to either position."
  130 (1) "1 - i - no added matter. And in my model a black hole is not matter, it is what the mouth at position 1 looks
       like."
  172 (1) M chose "Yes, it may" (position 2's piece may carry the README's stress)
  179/180 "We know the corridor *does not sit on either position's plane, it only bridges them. So one could surmise
       that the corridor is exclusive to the bulk."
  183  M chose "Yes: never violated as a pair"
  184  "There are no matter free planes"
  187 (3) M chose "Seat both": (G) "the corridor sits in the bulk, on neither plane (179/180), with eq. (17) kept only as
       a plane's possible reading of the corridor's mouth"
  195  "The README is not a pair";  196 "All questions get works through the cypher"
THE BOARD'S READINGS (named; withdrawn if M says otherwise):
  H-PLANE-READS-MOUTH  (ITEM179) eq. (17) at r0 = 2m is what our plane reads of the corridor's mouth.  Here made a
       theorem to prove, M1 (OPEN).
  H-OWN-MATTER-ONLY    the board's gloss of 184 with 129 (1) and 130 (1) (184's record: "each plane carries its own
       universe's matter, and the corridor adds none"): our plane's matter at the mouth is our universe's alone, bounded
       here by nuclear density.  ITEM185 read X22's cap the same way; that is the same reading, not support for it.  It
       sits in tension with 172 (1), where M allowed README stress on position 2's piece although the board had said
       129 (1)/130 (1) read against it.  Put to the cypher (C11): undecided.
  H-STRESS-INDEX       how that question is encoded for tools/cypher.py (C11); the encoding is the board's.
  H-M1-TRACE-INDEX     how M1's single-plane question is encoded for tools/cypher.py (C8); the board's.
  H-RH-IS-2M           (ITEM185) the trace's horizon radius 2m is the size compared with ell, x = 2m/ell.
  H-EQ17-ON-P2         (stage 6) position 2's piece reads eq. (17) -- tested matter-free in C2b; its leg is M1-P2.
  H-POSITIVE-ON-P2     (ITEM185, 139 (2)) in M1-f.
  H-BK-FLUID-NOT-MATTER the board's gloss of 130's "a black hole is not matter": eq. (17)'s Bronnikov-Kim effective
       fluid is not plane matter either.
READ (via lemmas/epass_ground.json, the board's E-PASS ground stage -- READ by board agents, itself not verified):
  Kaus-Reall 0901.4236v1 PDF p.4 "In the bulk, the surface gravity is constant. Hence, by continuity, it will take the
  same value on the brane. Therefore if the horizon is degenerate on the brane then it will also be degenerate in the
  bulk."; PDF pp.4-5 eq. (2.2) "ds^2 = A(rho)^2 dSigma^2 + drho^2 + R(rho)^2 dOmega^2"; PDF p.5 "In the bulk,
  compactness of the horizon implies that R(rho) must vanish somewhere" and (2.8) smoothness; PDF p.6 (2.16) the Israel
  condition "A'(rho0)/A(rho0) = 1/l - lQ^2/(2R(rho0)^4), R'(rho0)/R(rho0) = 1/l + lQ^2/(2R(rho0)^4)"; p.11 "our bulk
  solution is independent of what kind of matter field is present on the brane".
READ (via ../cosmo.py, imported): Planck 2018 H0 = 67.36 km/s/Mpc, Omega_m = 0.3153 (flat taken: Omega_K = 0.001 +-
  0.002, READ in b1_matter.py) -- for the dark-energy density in C10.
standard-not-READ: the Gauss and Codazzi equations; Israel's junction (Z2); Cauchy-Kovalevskaya with constraint
  propagation (as in localbulk.py L4); that the near-horizon geometry of a static degenerate horizon is a warped
  product (KR cite it as proved in their ref. [16]); nuclear density ~2.3e17 kg/m^3 (neutron-star cores several times
  more); Bertotti-Robinson's AdS2 x S2 needing traceless matter rho = 1/(8 pi G L^2) in 4D general relativity.

CLI:  python3 f1_audit.py [--selftest] [--mutants] [--json PATH]     (selftest ~25 s; --mutants ~1 min)
Stdlib + sympy (+ the owners' own needs: z3, mpmath, numpy, scipy, python-flint).  No file is written but --json's.
"""
import contextlib
import importlib.util
import io
import itertools
import json
import math
import os
import re
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
REPO = os.path.dirname(os.path.dirname(WD))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
GROUND = os.path.join(HERE, "epass_ground.json")
CYPHER = os.path.join(REPO, "tools", "cypher.py")
WARPTHEOREM = os.path.join(D68, "warptheorem.py")
B1MATTER = os.path.join(HERE, "b1_matter.py")
COSMO = os.path.join(WD, "cosmo.py")

RHO_NUC = 2.3e17              # kg/m^3, nuclear density (standard-not-READ; ITEM185 uses the same)
RHO_NS = 2.0e18               # kg/m^3, several times nuclear (neutron-star cores; standard-not-READ) -- F1A-R11
ELL_MAX = 13.964e-6           # m, ITEM185's refined upper edge (deduced from READ Adelberger et al. p.3; MK eq. 41)
EDGE_SIM2 = 27.07             # ell > 27.07 m(N), SIM2-FACING's lower edge (computed WITH eq. (17) on our plane: rests on
#                               F1, which M1 grants; to be redone)
EDGE_B4C = 4.0e5              # ell > 4.0e5 m(N), B4c's edge with the write's hold (ITEM179; to be redone)
SNAPSHOT_N = 1.088e29         # item 108's full snapshot
Q_REF = 1.652872              # passage5d.py P3, per m
YS_FLAT, YS_ELL_M = 2.5536, 0.9139   # SIM2-FACING's y_s^th (flat; ell = m), in m -- reproduced in C2
GRID = (0.005, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 0.99, 0.999, 0.9999)   # cap parameter A0/ell (C3-C8)
CROSS_A0 = (0.005, 0.02, 0.05, 0.6, 0.8, 0.95)   # crossing count to rho = 60 ell (three inside the window) -- OC-5, R12
P2_COUNTS = (3, 6)            # position 2's ell_2 / ell: stage 6 J3's 3 (with 138) and the 6 B4D-STAGE6's downstream
#                               note gives when J3's -1/3 is not counted twice (put to M; 174 (2) "For the math")

DEFAULT = {"r0_over_m": sp.Integer(2), "z1_first": None, "q_arg": sp.sqrt(3) / 2, "lam5_sign": -1, "b1_metric": "eq17",
           "o1_key": "main", "bank_K_scale": 1, "j6_flip": False, "axiom_132": "true", "kappa_H": "F",
           "string_grr": "warp", "gauss_sign": 1, "israel_sign": 1, "nh_lam": 4.0, "c1_metric": "eq17",
           "ys_side": -1, "rho_nuc": RHO_NUC, "cy_add_question": False, "cy_drop_route1": False, "m1_green": False,
           "keep_B1_F2": False, "swap_ab": False, "kr_quote": "true", "c3_div": 12, "pi_form": "sms",
           "rho_lambda_on": True, "z2_on_m1": False, "cy_stress_add_q1": False, "g13_f1_free": False}

_CACHE = {}


def _load(path, key, register=False):
    if key in _CACHE:
        return _CACHE[key]
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), HERE, D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        if register:                                   # cypher.py's dataclass resolves through sys.modules
            sys.modules[key] = mod
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    _CACHE[key] = mod
    return mod


def _memo(key, fn):
    if key not in _CACHE:
        with contextlib.redirect_stdout(io.StringIO()):
            _CACHE[key] = fn()
    return _CACHE[key]


def owner(name):
    paths = {"stability": ("bulk", "stability.py"), "passage5d": ("bulk", "passage5d.py"), "coin": ("copy", "coin.py"),
             "plane": ("copy", "plane.py"), "exactE": ("copy", "exactE.py"), "localbulk": ("bulk", "localbulk.py"),
             "ledger": ("lemmas", "ledger.py"), "b4_static": ("lemmas", "b4_static.py"),
             "b4d_stage6": ("lemmas", "b4d_stage6.py"), "axioms": ("lemmas", "axioms.py")}
    return _load(os.path.join(D68, *paths[name]), "f1a_" + name)


def _norm(s):
    return re.sub(r"\s+", " ", s)


# ======================================================================================= PART A: the owners re-run
def part_a(cfg):
    m = sp.Symbol("m", positive=True)
    r0 = cfg["r0_over_m"] * m
    out = {}
    # A1 H2 (axioms.py): eq. (17)'s horizon at r = 2m holds N A_bit; the throat r0 sits on it only at r0 = 2m
    ax = _memo("ax_h2", lambda: owner("axioms").derive_h2_g1())
    out["A1"] = {"horizon": ax["horizon"], "H2": ax["H2"], "throat_on_horizon": sp.simplify(r0 - ax["horizon"][0]) == 0}
    # A2 O1 (exactE.py, z3): one way under H-FUTURE-INGOING; the two controls refuted
    ids = _memo("ex_ids", lambda: owner("exactE").identities())
    keys = {"main": "one way under H-FUTURE-INGOING: the future cone at the throat has xdot <= 0",
            "ctl": "CONTROL the outgoing chart's 'xdot <= 0' must fail"}
    out["A2"] = {"one_way": ids[keys[cfg["o1_key"]]][1],
                 "controls": [ids[k][1] for k in ("CONTROL the outgoing chart's 'xdot <= 0' must fail",
                                                  "CONTROL the reversed orientation's 'xdot <= 0' must fail")]}
    # A3 O2 (stability.py S1): D'(rho_H) = 0 at the member r0; the r0 = 1.8m control is not extremal
    st = owner("stability")
    d1, _ = _memo(("st", str(r0)), lambda: st.D_derivatives(r0, 2 * m))
    c1, _ = _memo(("st", "9/5"), lambda: st.D_derivatives(sp.Rational(9, 5) * m, 2 * m))
    out["A3"] = {"D1": d1, "control_D1": c1}
    # A4 Z1 (passage5d.py P2): R5(n,k,n,k) = -R4(k,k) = 2r''/r from the bulk series; the foil breaks it
    p5 = owner("passage5d")
    first = None
    if cfg["z1_first"] == "foil":
        bs = _load(os.path.join(D68, "bulk", "bulkseries.py"), "f1a_bulkseries")
        first = {"A": -2 * (1 + sp.Rational(1, 7)) * (1 - 2 / bs.r) / bs.ell}
    tid = _memo(("tidal", cfg["z1_first"]), lambda: p5.tidal(first=first))
    rr = tid["r"]
    out["A4"] = {"identity": sp.simplify(tid["n_kk"] + tid["R4_kk"]) == 0,
                 "closed": sp.simplify(tid["n_kk"] - sp.Rational(1, 2) / ((rr - sp.Rational(3, 2)) ** 2 * rr)) == 0,
                 "n_kk": tid["n_kk"], "R4_kk": tid["R4_kk"], "r": rr}
    # A5 Z2 (passage5d.py P3, coin.py): Q = 8/3 - (4/(3 sqrt3)) artanh(sqrt3/2) = 1.652872 = -2 x coin's per-leg reading
    Q = float(sp.Rational(8, 3) - 4 / (3 * sp.sqrt(3)) * sp.atanh(cfg["q_arg"]))
    leg = owner("coin").anec_closed(1, float(cfg["r0_over_m"]))
    out["A5"] = {"Q": Q, "leg": leg}
    # A6 B1 (localbulk.py L1): with K = -g/ell the Gauss constraint demands R(4) = 0, and eq. (17) has R(4) = 0
    lb = owner("localbulk")
    rL, mL = lb.r, lb.m
    F = 1 - 2 * mL / rL
    H = {"eq17": (1 - 2 * mL / rL) ** 2 / (1 - sp.Rational(3, 2) * mL / rL),
         "sds": None}[cfg["b1_metric"]]
    if H is None:
        F = 1 - 2 * mL / rL - rL**2 / lb.L**2
        H = F
    out["A6"] = {"gauss": lb.gauss_rhs(-1 / lb.ell, cfg["lam5_sign"] * 6 / lb.ell**2),
                 "R4": _memo(("ric", cfg["b1_metric"]), lambda: lb.ricci_scalar(F, H))}
    # A7 B2 (localbulk.py L3 + L4): analytic data -- d rho/du = 2 sqrt(m/2 + u^2), even in u, through the horizon
    lbd = _memo("lb_compute", lambda: lb.compute())
    u = sp.Symbol("u", real=True)
    rs = sp.Symbol("rr", positive=True)
    Fm = 1 - 2 * m / rs
    Hm = (1 - 2 * m / rs) * (1 - r0 / rs) / (1 - sp.Rational(3, 2) * m / rs)
    gu2 = sp.simplify(((Fm / Hm) * (2 * u) ** 2).subs(rs, 2 * m + u**2))    # (d rho/du)^2, the chart's square
    out["A7"] = {"owner_L3": bool(lbd["closed_ok"] and lbd["even"]),
                 "independent": sp.simplify(gu2 - 4 * (m / 2 + u**2)) == 0}   # even, positive: analytic at u = 0
    # A8 B4b (b4_static.py S3, banked grid): holds < ~11.3 clocks regular, K <= 2.7; the per-bit 28.48 reaches K > 1e4
    b4 = owner("b4_static")
    def _b4():
        if cfg["bank_K_scale"] == 1:
            return b4.compute(live=False)
        real_json = b4.json

        class _J:
            @staticmethod
            def load(f):
                d = real_json.load(f)
                for col in d["cols"].values():
                    col["K"] = [k * cfg["bank_K_scale"] for k in col["K"]]
                return d
        b4.json = _J
        try:
            return b4.compute(live=False)
        finally:
            b4.json = real_json
    bd = _memo(("b4", cfg["bank_K_scale"]), _b4)
    out["A8"] = {"t_cert": bd["cone"]["t_cert"], "Kmax_cert": bd["Kmax_cert"], "Kmax_o3": bd["Kmax_o3"],
                 "t_fail_4": bd["cone"]["t_fail_4"]}
    # A9 B4d (b4d_stage6.py J6, STRUCTURAL): sigma = -3 (a_L + a_R)/kappa^2, so a positive plane has a decaying side;
    #    stage 5 makes that side singular (C2 reproduces the throat column's singular depth)
    s6 = owner("b4d_stage6")
    grid = [k / 4 for k in range(-8, 9)]
    flip = -1 if cfg["j6_flip"] else 1
    e = sp.Integer(1)
    j6 = all((not (s6.sigma_over_rs(flip * aL, flip * aR, e) > 0)) or min(aL, aR) < 0 for aL in grid for aR in grid)
    out["A9"] = {"J6": bool(j6), "owner_J6": s6.j6()}
    # A10 E4 (ledger.py E4a/b): M(R) = m + (m/4)(1 - m/(2R - 3m)); cross-checked with plane.py's Misner-Sharp at r0
    lg = _memo("ledger_e4", lambda: owner("ledger").e4())
    bk = _memo("plane_bk", lambda: owner("plane").bk_masses())
    rP, r0P, mP, _ = bk["syms"]
    ms_at = sp.simplify(bk["MS"].subs(r0P, cfg["r0_over_m"] * mP))
    Rl = next(q for q in lg["M"].free_symbols if q.name == "r")
    ml = next(q for q in lg["M"].free_symbols if q.name == "m")
    cross = sp.simplify(ms_at.subs({rP: sp.Symbol("Rx", positive=True), mP: sp.Symbol("mx", positive=True)})
                        - lg["M"].subs({Rl: sp.Symbol("Rx", positive=True), ml: sp.Symbol("mx", positive=True)})) == 0
    out["A10"] = {"closed_ok": lg["closed_ok"], "far": lg["far"], "at_throat": lg["at_throat"], "dM_pos": lg["dM_pos"],
                  "cross_plane": cross, "m": ml}
    return out


# ================================================================================ PART B: what survives without F1
def axiom_texts(cfg):
    """READ: M's 132 and the other rulings used, verbatim in the rulings file (whitespace normalised)."""
    t = _norm(open(RULINGS, encoding="utf-8").read())
    q = {"132_holds": "do the horizons still hold the README too (your item 106), as well as the throat? - yes",
         "132_one_way": "And the passage is one way by nature, a black hole in and a white hole out, side views of the "
                        "same corridor object",
         "132_views": "*different views of the same object",
         "129_1": "the corridor is a bridge, so it adds nothing to either position.",
         "130_1": "1 - i - no added matter. And in my model a black hole is not matter, it is what the mouth at "
                  "position 1 looks like.",
         "179_180": "We know the corridor *does not sit on either position's plane, it only bridges them.",
         "184": "There are no matter free planes",
         "187_G": "with eq. (17) kept only as a plane's possible reading of the corridor's mouth",
         "172_1": "M chose: \"Yes, it may\"",
         "183": "M chose: \"Yes: never violated as a pair\"",
         "194": "Disregard that last ruling. I want that question put to the cypher",
         "195": "The README is not a pair"}
    if cfg["axiom_132"] == "corrupt":
        q["132_holds"] = q["132_holds"].replace("- yes", "- no")
    found = {k: (t.find(v) >= 0) for k, v in q.items()}
    lines = {}
    raw = open(RULINGS, encoding="utf-8").read().split("\n")
    for k in ("132_holds", "184", "195"):
        head = q[k][:24]
        lines[k] = next((i + 1 for i, ln in enumerate(raw) if head in ln), None)
    return {"found": found, "lines": lines}


def ground_reads(cfg):
    """READ (via epass_ground.json): Kaus-Reall's quotes this note rests on, verbatim."""
    g = _norm(json.dumps(json.load(open(GROUND, encoding="utf-8")), ensure_ascii=False))
    q = {"KR_p4_kappa": "In the bulk, the surface gravity is constant. Hence, by continuity, it will take the same value "
                        "on the brane. Therefore if the horizon is degenerate on the brane then it will also be "
                        "degenerate in the bulk.",
         "KR_2.2": "ds^2 = A(ρ)^2 dΣ^2 + dρ^2 + R(ρ)^2 dΩ^2, (2.2)",
         "KR_p5_compact": "In the bulk, compactness of the horizon implies that R(ρ) must vanish somewhere.",
         "KR_2.16": "A′(ρ0)/A(ρ0) = 1/ℓ − ℓQ^2/(2R(ρ0)^4), "
                    "R′(ρ0)/R(ρ0) = 1/ℓ + ℓQ^2/(2R(ρ0)^4). (2.16)",
         "KR_p11_matter": "our bulk solution is independent of what kind of matter field is present on the brane"}
    if cfg["kr_quote"] == "corrupt":
        q["KR_p4_kappa"] = q["KR_p4_kappa"].replace("degenerate in the bulk", "non-degenerate in the bulk")
    return {k: (g.find(v) >= 0) for k, v in q.items()}


def kappa_criterion(cfg):
    """deduced + computed: for -F dt^2 + dr^2/H + r^2 dOmega^2 with the throat (H = 0) on the horizon (F = 0),
    kappa^2 = lim F'^2 H/(4F).  Schwarzschild (F = H; its Einstein-Rosen throat sits on the bifurcation surface) has
    kappa = 1/(4m) != 0; eq. (17) at r0 = 2m has H = O(F^2), so kappa = 0.  So 'throat on horizon' (G3, 132) does
    not force extremality: O2 needs eq. (17)'s particular H, or M1."""
    r, m = sp.symbols("r m", positive=True)
    F = 1 - 2 * m / r
    H_s = F if cfg["kappa_H"] == "F" else F**2
    H17 = F**2 / (1 - sp.Rational(3, 2) * m / r)
    s = sp.Symbol("s", positive=True)
    k2 = lambda H: sp.limit(sp.simplify((sp.diff(F, r) ** 2 * H / (4 * F)).subs(r, 2 * m + s)), s, 0, "+")
    return {"kappa2_schw": sp.simplify(k2(H_s)), "kappa2_eq17": sp.simplify(k2(H17))}


def tangency(cfg):
    """STRUCTURAL (deduced) + computed: a plane tangent to the bulk's static Killing field reads the bulk's surface
    gravity: D_xi xi = P(nabla_xi xi) = P(kappa xi) = kappa xi on the horizon.  Instances: the RS black string,
    e^{-2y/ell}(-F dt^2 + dr^2/F + r^2 dOmega^2) + dy^2, has kappa = 1/(4m) at every depth y (= the plane's); Kaus-
    Reall's near-horizon ansatz, A(rho)^2(-x^2 dt^2 + dx^2/x^2) + drho^2 + ..., has kappa = 0 at every rho."""
    r, m, y, ell, x, rho = sp.symbols("r m y ell x rho", positive=True)
    F = 1 - 2 * m / r
    V = sp.exp(-2 * y / ell) * F
    grr_inv = sp.exp(2 * y / ell) * F if cfg["string_grr"] == "warp" else sp.exp(-4 * y / ell) * F
    s = sp.Symbol("s", positive=True)
    k2 = sp.simplify((grr_inv * sp.diff(V, r) ** 2 + sp.diff(V, y) ** 2) / (4 * V))
    k2_h = sp.simplify(sp.limit(k2.subs(r, 2 * m + s), s, 0, "+"))
    A = sp.Function("A")(rho)
    Vn = A**2 * x**2
    k2n = sp.simplify((x**2 / A**2 * sp.diff(Vn, x) ** 2 + sp.diff(Vn, rho) ** 2) / (4 * Vn))
    return {"string_kappa2": k2_h, "nh_kappa2_at_x0": sp.simplify(k2n.subs(x, 0))}


def gauss_identity(cfg):
    """computed (standard-not-READ: the Gauss equation): for any metric dy^2 + h(x, y) and radial null k tangent to
    y = 0, with K = (1/2) d_y h, R5(k,k) = R4(k,k) + R5(n,k,n,k) - K K(k,k) + (K.K)(k,k).  Checked on two unrelated
    static spherically symmetric families (no field equation used)."""
    t, r, th, ph, y = sp.symbols("t r theta phi y")
    X = [t, r, th, ph, y]

    def parts(A, B, C):
        g = sp.diag(-A, B, C, C * sp.sin(th) ** 2, 1)
        gi = [1 / g[i, i] for i in range(5)]
        n = 5
        Gam = [[[gi[a] * (sp.diff(g[a, b], X[c]) + sp.diff(g[a, c], X[b]) - sp.diff(g[b, c], X[a])) / 2
                 for c in range(n)] for b in range(n)] for a in range(n)]

        def Riem(a, b, c, d):
            return (sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
                    + sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(n)))
        sub = {y: 0}
        Ric5 = lambda b: sum(Riem(a, b, a, b) for a in range(n)).subs(sub)
        nyny = lambda b: (g[4, 4] * Riem(4, b, 4, b)).subs(sub)
        h = [g[i, i].subs(sub) for i in range(4)]
        X4 = X[:4]
        hm = sp.diag(*h)
        G4 = [[[(sp.diff(hm[a, b], X4[c]) + sp.diff(hm[a, c], X4[b]) - sp.diff(hm[b, c], X4[a])) / (2 * hm[a, a])
                for c in range(4)] for b in range(4)] for a in range(4)]
        R4 = lambda b: sum(sp.diff(G4[a][b][b], X4[a]) - sp.diff(G4[a][b][a], X4[b])
                           + sum(G4[a][a][e] * G4[e][b][b] - G4[a][b][e] * G4[e][b][a] for e in range(4))
                           for a in range(4))
        K = [(sp.diff(g[i, i], y) / 2).subs(sub) for i in range(4)]
        Ktr = sum(K[i] / h[i] for i in range(4))
        kt, kr = 1 / sp.sqrt(h[0]), 1 / sp.sqrt(h[1])          # radial null, g(k,k) = -1 + 1 = 0
        kk = lambda a0, a1: a0 * kt**2 + a1 * kr**2
        return (sp.simplify(kk(Ric5(0), Ric5(1))), sp.simplify(kk(R4(0), R4(1))), sp.simplify(kk(nyny(0), nyny(1))),
                sp.simplify(Ktr * kk(K[0], K[1])), sp.simplify(kk(K[0] ** 2 / h[0], K[1] ** 2 / h[1])))
    F = 1 - 2 / r
    fams = [(F * (1 - y / 3 + y**2 / 5), (1 / F) * (1 + y / 2 - y**2 / 7), r**2 * (1 + y / r + y**2 / 3)),
            (F * sp.exp(-2 * y / 3) * (1 + y**2 / r), (1 + 3 / r) * (1 - y / r + y**2), r**2 * sp.exp(-y) * (1 + 2 * y**2 / r**2))]
    sgn = cfg["gauss_sign"]
    res = []
    for fam in fams:
        R5kk, R4kk, nkk, KKkk, KoK = parts(*fam)
        res.append(sp.simplify(R5kk - (R4kk + nkk - sgn * KKkk + sgn * KoK)))
    return {"residuals": res}


def israel(cfg):
    """computed (symbolic; Israel Z2 and Gauss, standard-not-READ): for a Z2-symmetric plane of tension q sigma_RS
    bounding the vacuum bulk (Lambda5 = -6/ell^2), K = -(q/ell) h - s (kappa5^2/2)(tau - tau h/3) in the normal pointing
    into the kept bulk (localbulk's K = -g/ell at q = 1), 8 pi G := kappa5^2/ell, tau ANY symmetric plane matter:
      null (Z1q):   -K K(k,k) + (K.K)(k,k) = -q 8 pi G tau(k,k) - kappa5^4 pi(k,k),   pi = SMS's quadratic term
      scalar (B1q): R4 = 2 Lambda5 + K^2 - K.K  gives  -R4 = -12(q^2 - 1)/ell^2 + q 8 pi G tau + kappa5^4 (tau.tau/4
                    - tau^2/12)
    Our plane is q = 1 (the RS tension of clause (B) as worded).  The q = 1 forms are FALSE at position 2's q < 0
    (139 (1); -1/3, -1/4, -1/6 in the counts stages 6-7 carry) and at multiplane M4's 4/3; a plane without Z2 symmetry is
    outside (tau = 0 with K = -h/ell + diag(0, d, -d, 0) gives R4 = -2 d^2).  pi(k,k) is not sign-definite under the
    NEC (diagonal tau: rho = 0, p1 = 1 gives -1/6) but is rho (rho + p)(u.k)^2/6 for a perfect fluid.  Uniform dark
    energy tau = -rho_L h (or a tension shift q != 1) gives R4 != 0: no exact R4 = 0 trace (C10)."""
    ell, k5 = sp.symbols("ell kappa5", positive=True)
    q = sp.Symbol("q", real=True)
    s = cfg["israel_sign"]
    eta = sp.diag(-1, 1, 1, 1)                                   # an orthonormal frame on the plane
    tau_dn = sp.Matrix(4, 4, lambda i, j: sp.Symbol("tau%d%d" % (min(i, j), max(i, j)), real=True))  # any symmetric
    k = sp.Matrix([1, 1, 0, 0])
    G8 = k5**2 / ell

    def parts(tau, Kextra=None, qq=q):
        tr = sum((eta * tau)[i, i] for i in range(4))
        K = -(qq / ell) * eta - s * (k5**2 / 2) * (tau - tr * eta / 3)
        if Kextra is not None:
            K = K + Kextra
        Km = eta * K
        Ktr = sum(Km[i, i] for i in range(4))
        KK = sum(Km[i, j] * Km[j, i] for i in range(4) for j in range(4))
        tm = eta * tau
        tt = sum(tm[i, j] * tm[j, i] for i in range(4) for j in range(4))
        tkk = (k.T * tau * k)[0]
        tok = (k.T * (tau * eta * tau) * k)[0]
        pi_kk = -tok / 4 + (tr * tkk / 12 if cfg["pi_form"] == "sms" else 0)
        R4 = 2 * (-6 / ell**2) + Ktr**2 - KK
        return {"tr": tr, "Kkk": (k.T * K * k)[0], "KoK": (k.T * (K * eta * K) * k)[0], "Ktr": Ktr, "tt": tt,
                "tkk": tkk, "pi_kk": pi_kk, "R4": R4}
    P = parts(tau_dn)
    null_lhs = -P["Ktr"] * P["Kkk"] + P["KoK"]
    null_q = sp.simplify(sp.expand(null_lhs - (-q * G8 * P["tkk"] - k5**4 * P["pi_kk"])))
    scal_q = sp.simplify(sp.expand(-P["R4"] - (-12 * (q**2 - 1) / ell**2 + q * G8 * P["tr"]
                                               + k5**4 * (P["tt"] / 4 - P["tr"] ** 2 / 12))))
    null_1 = sp.expand(null_lhs - (-G8 * P["tkk"] - k5**4 * P["pi_kk"]))          # the q = 1 forms ("our plane")
    scal_1 = sp.expand(-P["R4"] - (G8 * P["tr"] + k5**4 * (P["tt"] / 4 - P["tr"] ** 2 / 12)))
    qs = (-sp.Rational(1, 3), -sp.Rational(1, 4), -sp.Rational(1, 6), sp.Rational(4, 3))
    q1_fails = {str(qq): (sp.simplify(null_1.subs(q, qq)) != 0, sp.simplify(scal_1.subs(q, qq)) != 0) for qq in qs}
    d = sp.Symbol("d", real=True)
    nz = parts(sp.zeros(4, 4), sp.diag(0, d, -d, 0), sp.Integer(1))
    rr, p1, p2, p3 = sp.symbols("rho p1 p2 p3", real=True)
    pd = parts(sp.diag(rr, p1, p2, p3), None, sp.Integer(1))["pi_kk"]
    rl = sp.Symbol("rho_L", positive=True)
    de = parts(-rl * eta, None, sp.Integer(1))
    shift = parts(sp.zeros(4, 4), None, q)
    return {"null_res": sp.simplify(null_q.subs(q, 1)), "scalar_res": sp.simplify(scal_q.subs(q, 1)),
            "null_q": null_q, "scalar_q": scal_q, "q1_fails": q1_fails,
            "nonZ2_R4": sp.simplify(nz["R4"]),
            "pi_counter": sp.simplify(pd.subs({rr: 0, p1: 1, p2: 0, p3: 0})),
            "pi_fluid": sp.factor(pd.subs({p1: p2, p3: p2})), "pi_fluid_p": p2, "pi_fluid_rho": rr,
            "R4_de": sp.simplify(de["R4"]), "R4_shift": sp.simplify(shift["R4"]), "rho_L": rl, "q": q}


def part_b(cfg):
    return {"axioms": axiom_texts(cfg), "reads": ground_reads(cfg), "kappa": kappa_criterion(cfg), "tangency": tangency(cfg),
            "gauss": _memo(("gauss", cfg["gauss_sign"]), lambda: gauss_identity(cfg)), "israel": israel_m(cfg)}


def israel_m(cfg):
    return _memo(("israel", cfg["israel_sign"], cfg["pi_form"]), lambda: israel(cfg))


# ======================================================================================== PART C: M1 and its matter
def nh_equations(lam=4.0, israel_sign=1):
    """computed: the bulk equations R_AB = -(4/ell^2) g_AB for KR's ansatz (2.2) with k = -1, derived here, against
    the hand-typed right-hand sides used by the integrator (coefficient lam); and the Hamiltonian constraint at an
    equal-radii cut, with the Israel data of plane_matter, against the SMS trace equation."""
    t, x, rho, th, ph, ell = sp.symbols("t x rho theta phi ell", positive=True)
    A, R = sp.Function("A")(rho), sp.Function("R")(rho)
    X = [t, x, rho, th, ph]
    g = sp.diag(-A**2 * x**2, A**2 / x**2, 1, R**2, R**2 * sp.sin(th) ** 2)
    gi = [1 / g[i, i] for i in range(5)]
    Gam = [[[gi[a] * (sp.diff(g[a, b], X[c]) + sp.diff(g[a, c], X[b]) - sp.diff(g[b, c], X[a])) / 2
             for c in range(5)] for b in range(5)] for a in range(5)]
    Ric = lambda b: sp.simplify(sum(sp.diff(Gam[a][b][b], X[a]) - sp.diff(Gam[a][b][a], X[b])
                                    + sum(Gam[a][a][e] * Gam[e][b][b] - Gam[a][b][e] * Gam[e][b][a] for e in range(5))
                                    for a in range(5)))
    Ap, Rp = sp.diff(A, rho), sp.diff(R, rho)
    App_typed = A * (lam / ell**2 - 1 / A**2 - Ap**2 / A**2 - 2 * Ap * Rp / (A * R))
    Rpp_typed = R * (lam / ell**2 + 1 / R**2 - Rp**2 / R**2 - 2 * Ap * Rp / (A * R))
    eA = sp.simplify((Ric(0) + 4 / ell**2 * g[0, 0]) / g[0, 0])
    eR = sp.simplify((Ric(3) + 4 / ell**2 * g[3, 3]) / g[3, 3])
    resA = sp.simplify(eA.subs(sp.diff(A, rho, 2), App_typed).subs(sp.diff(R, rho, 2), Rpp_typed))
    resR = sp.simplify(eR.subs(sp.diff(R, rho, 2), Rpp_typed).subs(sp.diff(A, rho, 2), App_typed))
    Rs = sum(gi[i] * Ric(i) for i in range(5))
    con = sp.simplify(Ric(2) - Rs / 2 * g[2, 2] - 6 / ell**2 * g[2, 2])
    # at an equal-radii cut with Israel data: a = ell A'/A = 1 - (x + 2z), b = ell R'/R = 1 + (2x + z)
    xs, zs = sp.symbols("x z", real=True)
    a_, b_ = 1 - israel_sign * (xs + 2 * zs), 1 + israel_sign * (2 * xs + zs)
    con_cut = sp.expand(a_**2 + 4 * a_ * b_ + b_**2 - 6)
    sms = sp.expand((zs - xs) / 3 + (xs**2 + zs**2) / 2 - (zs - xs) ** 2 / 3)
    ratio = sp.simplify(con_cut / sms)
    return {"resA": resA, "resR": resR, "constraint": sp.expand(con), "cut_vs_sms": ratio}


def _rk4(f, s, h):
    k1 = f(s)
    k2 = f([a + h / 2 * b for a, b in zip(s, k1)])
    k3 = f([a + h / 2 * b for a, b in zip(s, k2)])
    k4 = f([a + h * b for a, b in zip(s, k3)])
    return [a + h / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(s, k1, k2, k3, k4)]


def _rhs(inv_l2, lam):
    def f(s):
        _, A, Ap, R, Rp = s
        App = A * (lam * inv_l2 - 1 / A**2 - Ap**2 / A**2 - 2 * Ap * Rp / (A * R))
        Rpp = R * (lam * inv_l2 + 1 / R**2 - Rp**2 / R**2 - 2 * Ap * Rp / (A * R))
        return (1.0, Ap, App, Rp, Rpp)
    return f


C3_DIV = [12]                 # divisor of the cubic coefficient c3 in the cap's series start (F1A-R7: 12, not 10)


def _cap_start(A0, inv_l2, lam):
    """The regular cap's series start: A = A0 + c2 rho^2, R = rho + c3 rho^3, c2 = (lam/l^2 - 1/A0^2) A0/6,
    c3 = (lam/l^2 - 4 c2/A0)/12 = (1/A0^2 + 2/l^2)/18 at lam = 4 (re-derived by a separate session; F1A-R7)."""
    c2 = (lam * inv_l2 - 1 / A0**2) * A0 / 6
    c3 = (lam * inv_l2 - 4 * c2 / A0) / C3_DIV[0]
    e = A0 * 1e-3
    return [e, A0 + c2 * e * e, 2 * c2 * e, e + c3 * e**3, 1 + 3 * c3 * e * e]


def hamiltonian(s, inv_l2=1.0, lam=4.0):
    """The rho-rho constraint of KR's ansatz (derived in nh_equations): A'^2/A^2 + 4A'R'/(AR) + R'^2/R^2 + 1/A^2 - 1/R^2
    - (3 lam/2)/l^2 = 0.  Returned times rho^2, so the O(1/rho^2) terms of a cap start do not swamp the residual."""
    rho, A, Ap, R, Rp = s
    c = Ap**2 / A**2 + 4 * Ap * Rp / (A * R) + Rp**2 / R**2 + 1 / A**2 - 1 / R**2 - 1.5 * lam * inv_l2
    return c * rho * rho


def cap_crossings(A0, inv_l2=1.0, lam=4.0, rmax=60.0, nper=4000):
    return _memo(("cross", A0, inv_l2, lam, rmax, nper, C3_DIV[0]),
                 lambda: _cap_crossings(A0, inv_l2, lam, rmax, nper))


def _cap_crossings(A0, inv_l2, lam, rmax, nper):
    """Sign changes of A - R along the cap (the stepping of _cap_cut) until rho = rmax or the continuation ends at
    A -> 0 beyond the cut (a curvature singularity on the side the Z2 plane discards; DOP853 confirms it for the
    in-window caps, a separate check).  Returns (crossings, 'rho_max' | 'A->0')."""
    f = _rhs(inv_l2, lam)
    s = _cap_start(A0, inv_l2, lam)
    h = A0 / nper
    n_x, prev = 0, s[1] - s[3]
    try:
        while s[0] < rmax:
            s = _rk4(f, s, min(h * max(1.0, s[3] / A0) * min(1.0, s[1] / A0), 0.01))
            if not (math.isfinite(s[1]) and math.isfinite(s[3])) or s[1] < 1e-3 * A0:
                return n_x, "A->0"
            dd = s[1] - s[3]
            n_x += (prev > 0) != (dd > 0)
            prev = dd
    except (OverflowError, ZeroDivisionError):
        return n_x, "A->0"
    return n_x, "rho_max"


def cap_to(A0, rho_end, inv_l2=1.0, lam=4.0, n=20000):
    f = _rhs(inv_l2, lam)
    s = _cap_start(A0, inv_l2, lam)
    h = (rho_end - s[0]) / n
    for _ in range(n):
        s = _rk4(f, s, h)
    return s


def cap_cut(A0, inv_l2=1.0, lam=4.0, rmax=12.0, nper=4000):
    return _memo(("cap", A0, inv_l2, lam, rmax, nper, C3_DIV[0]), lambda: _cap_cut(A0, inv_l2, lam, rmax, nper))


def _cap_cut(A0, inv_l2, lam, rmax, nper):
    """The smooth cap R(0) = 0, R'(0) = 1, A(0) = A0 (KR (2.8)), integrated out to the first rho0 where A = R -- the
    plane there reads AdS2(L) x S2(L), L = A = R: eq. (17)'s near-horizon geometry with L = 2m.  None if no cut."""
    f = _rhs(inv_l2, lam)
    s = _cap_start(A0, inv_l2, lam)
    h = A0 / nper
    while s[0] < rmax:
        hh = min(h * max(1.0, s[3] / A0), 0.01)
        ns = _rk4(f, s, hh)
        if s[1] - s[3] > 0 >= ns[1] - ns[3]:
            lo, hi = 0.0, hh
            for _ in range(60):
                mid = (lo + hi) / 2
                if _rk4(f, s, mid)[1] - _rk4(f, s, mid)[3] > 0:
                    lo = mid
                else:
                    hi = mid
            c = _rk4(f, s, (lo + hi) / 2)
            return {"rho0": c[0], "L": c[3], "Ap_A": c[2] / c[1], "Rp_R": c[4] / c[3], "A": c[1]}
        s = ns
        if not (s[1] > 0 and math.isfinite(s[1]) and math.isfinite(s[3])):
            return None
    return None


def plane_matter(cut, israel_sign=1, swap=False):
    """Israel (Z2, outward normal, KR's orientation): A'/A = (1/ell)(1 - s(rho + 2p)/sigma), R'/R = (1/ell)(1 +
    s(2 rho + p)/sigma) for AdS2-invariant plane matter tau^t_t = tau^x_x = -rho, tau^th_th = tau^ph_ph = p.  KR's
    (2.16) is the Maxwell case p = rho.  Returns rho/sigma, p/sigma; rho + p_r = 0 by the AdS2 symmetry."""
    a, b = cut["Ap_A"], cut["Rp_R"]                                # ell = 1
    if swap:
        a, b = b, a
    s = israel_sign
    u, v = (1 - a) / s, (b - 1) / s                                # u = (rho + 2p)/sigma, v = (2 rho + p)/sigma
    rho, p = (2 * v - u) / 3, (2 * u - v) / 3
    con = (a * a + 4 * a * b + b * b - 6) / max(1.0, a * a + b * b)
    return {"rho": rho, "p": p, "a": a, "b": b, "con_rel": con}


def ys(ell_over_m, side=-1, lam=4.0):
    return _memo(("ys", ell_over_m, side, lam), lambda: _ys(ell_over_m, side, lam))


def _ys(ell_over_m, side, lam):
    """Q = 0 data (a matter-free plane at the RS tension; KR (2.16) with Q = 0): A = R = 2m, A'/A = R'/R = 1/ell at the
    plane, integrated into the kept bulk until A -> 0 (the curvature singularity of KR's singular branch; SIM2's
    y_s^th).  side = -1 is into the kept bulk; +1 the wrong side (a mutant)."""
    inv = 0.0 if ell_over_m is None else 1.0 / ell_over_m
    f = _rhs(inv * inv, lam)
    s = [0.0, 2.0, side * 2.0 * inv, 2.0, side * 2.0 * inv]
    scale = 1.0 if ell_over_m is None else min(1.0, ell_over_m)
    h = 2e-3 * scale
    try:
        while s[1] > 1e-3:
            s = _rk4(f, s, h * max(1e-4, min(1.0, s[1] / 0.5)) ** 2)
            if s[0] > 50 or not math.isfinite(s[1]):
                return None
    except (OverflowError, ZeroDivisionError):                     # the singular end, reached inside a step
        pass
    return s[0]


def find_A0_for_x(xt, lam=4.0):
    lo, hi = 1e-4, 0.999999
    for _ in range(45):
        mid = (lo * hi) ** 0.5 if hi / lo > 10 else (lo + hi) / 2
        c = cap_cut(mid, lam=lam)
        if c is None or c["L"] > xt:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def part_c(cfg):
    lam, sgn = cfg["nh_lam"], cfg["israel_sign"]
    out = {}
    # C1 the 4D-limit candidate: plane matter = G(eq17)/(8 pi G) (bulk Weyl term zero).  Its radial null part is
    #    R4(k,k) = -2r''/r < 0 at every r tested (a pointwise fact; 183 allows a paired negative member), and its integral
    #    over both legs is -Q: negative net per light ray, which is what 183 excludes.
    p5 = owner("passage5d")
    tid = _memo(("tidal", cfg["c1_metric"]),
                lambda: p5.tidal(schwarzschild=(cfg["c1_metric"] == "schw")))
    rr = tid["r"]
    vals = [float(tid["R4_kk"].subs(rr, v)) for v in (2.01, 2.5, 3.0, 10.0, 100.0)]
    out["C1"] = {"R4kk": vals, "net": 2 * owner("coin").anec_closed(1, 2)}
    ex = owner("exactE")                                           # constants and the example README
    Esym = _memo("ax_h2", lambda: owner("axioms").derive_h2_g1())["E"]  # E(N) = sqrt(N h c^5 ln2/(8 pi^2 G)), G1
    G, c = float(ex.G_SI), float(ex.C_SI)
    val = {"G": float(ex.G_SI), "N": 1.0, "c": float(ex.C_SI), "h": float(ex.H_SI)}
    E1 = float(Esym.subs({sym: val[sym.name] for sym in Esym.free_symbols}))
    m1 = G * E1 / c**4
    mN = m1 * math.sqrt(ex.N_EXAMPLE)
    need_3m = abs(float(tid["R4_kk"].subs(rr, 3.0))) * c**2 / (8 * math.pi * G * mN**2) if vals[2] != 0 else 0.0
    out["C1"].update({"m1": m1, "mN": mN, "need_3m_kgm3": need_3m, "ours_over_need": cfg["rho_nuc"] / need_3m
                      if need_3m else float("inf")})
    # C2 the vacuum plane: Q = 0 data are singular at finite depth (SIM2's y_s^th reproduced)
    out["C2"] = {"ys_flat": ys(None, cfg["ys_side"], lam), "ys_ell_m": ys(1.0, cfg["ys_side"], lam)}
    # C2b the same data on a NEGATIVE-tension plane (the growing side; H-EQ17-ON-P2, stage 6 J3).  Numerical (RK4, no
    #     error control), sampled: no singularity to y = 50m at ell = 2m and 4.79m; singular at the sampled 4.80m, 8m and
    #     at position 2's ell_2 under both counts (3 x 27.07m, stage 6 J3; 6 x 27.07m, B4D-STAGE6's downstream note).
    #     The 27.07m edge itself rests on F1 (SIM2-FACING computed it with eq. (17) on our plane).
    gs = -cfg["ys_side"]
    out["C2b"] = {"ell_2": ys(2.0, gs, lam), "ell_479": ys(4.79, gs, lam), "ell_480": ys(4.80, gs, lam),
                  "ell_8": ys(8.0, gs, lam)}
    for k_ in P2_COUNTS:
        out["C2b"]["p2_%d" % k_] = ys(k_ * EDGE_SIM2, gs, lam)
    # C3 integrator controls: AdS5 (A0 = ell) exactly A = cosh, R = sinh; the exact cap A0 = ell/2: A = ell/2,
    #    R = (ell/sqrt2) sinh(sqrt2 rho/ell), cut at L = ell/2 with a = 0, b = sqrt6; and the cap's series start meets the
    #    Hamiltonian constraint (F1A-R7: the irregular mode decays, so only this check sees a wrong start)
    s = cap_to(1.0, 1.0, lam=lam)
    half = cap_cut(0.5, lam=lam)
    out["C3"] = {"ads5_err": max(abs(s[1] - math.cosh(1.0)), abs(s[3] - math.sinh(1.0))),
                 "half": half, "half_m": plane_matter(half, sgn, cfg["swap_ab"]) if half else None,
                 "start_con": max(abs(hamiltonian(_cap_start(A0, 1.0, lam), 1.0, lam)) for A0 in GRID)}
    # C4-C5 the cap family on the grid (numerical, RK4 without error control)
    rows = []
    for A0 in GRID:
        cut = cap_cut(A0, lam=lam)
        rows.append({"A0": A0, "cut": cut, "m": plane_matter(cut, sgn, cfg["swap_ab"]) if cut else None})
    flat = cap_cut(1.0, inv_l2=0.0, lam=lam, rmax=50)
    out["C4"] = {"rows": rows, "no_cut": [cap_cut(A0, lam=lam) is None for A0 in (1.2, 1.5)],
                 "crossings": [cap_crossings(A0, lam=lam) for A0 in CROSS_A0],
                 "c_flat": (flat["L"] * flat["Ap_A"] + 2 * flat["L"] * flat["Rp_R"]) / 3 if flat else None}
    # C6 the window and H-OWN-MATTER-ONLY.  The window's lower edges rest on F1 (SIM2-FACING's 27.07m) or are to be
    #    redone (B4c's 4.0e5m); the example-README figure uses only the upper edge 13.964 um.
    A0e = find_A0_for_x(2 / EDGE_SIM2, lam)
    ce = cap_cut(A0e, lam=lam)
    me = plane_matter(ce, sgn, cfg["swap_ab"])
    sigma_kgm3 = 3 * c**2 / (4 * math.pi * G * ELL_MAX**2)
    cf = out["C4"]["c_flat"] or float("nan")
    x_ex = 2 * mN / ELL_MAX
    need_ex = sigma_kgm3 * cf / x_ex                               # flat asymptote, x ~ 1e-23 (computed limit C5)
    # threshold: rho_need <= rho_ours needs the Bertotti-Robinson regime, rho = c^2/(8 pi G L^2) (C5's limit)
    L_star = math.sqrt(c**2 / (8 * math.pi * G * cfg["rho_nuc"]))
    N_star = (L_star / 2 / m1) ** 2
    L_ns = math.sqrt(c**2 / (8 * math.pi * G * RHO_NS * cfg["rho_nuc"] / RHO_NUC))
    ell_need = 3 * cf * c**2 / (4 * math.pi * G * 2 * mN * cfg["rho_nuc"])   # ell at which the flat-regime need
    out["C6"] = {"ell_need_example_m": ell_need, "x_edge": 2 / EDGE_SIM2, "L_edge": ce["L"], "rho_edge": me["rho"],
                 "x_b4c": 2 / EDGE_B4C, "rho_b4c": cf / (2 / EDGE_B4C),
                 "sigma_over_nuc": sigma_kgm3 / cfg["rho_nuc"], "ours_over_sigma": cfg["rho_nuc"] / sigma_kgm3,
                 "need_example_over_nuc": need_ex / cfg["rho_nuc"], "L_star_m": L_star, "N_star": N_star,
                 "N_star_ns": (L_ns / 2 / m1) ** 2}
    # C7 two capped sides cannot cancel their anisotropy: b > a at every cut (Pi^Omega > Pi^Sigma), so Pi_L = -Pi_R
    #    (stage 6 J1's matter-free condition) fails for two caps
    out["C7"] = {"b_gt_a": [r["m"]["b"] > r["m"]["a"] for r in rows if r["m"]]}
    out["C8"] = cypher_m1(cfg, rows)
    out["C9"] = green_table(cfg)
    out["C10"] = m1c_bound(cfg, tid, mN, G, c)
    out["C11"] = cypher_stress(cfg)
    return out


# ---------------------------------------------------------------------------------- C10 M1-c's error bound (F1A-R4)
def m1c_bound(cfg, tid, mN, G, c):
    """computed: how far our universe's matter moves our plane's trace off eq. (17) (M1-c is stated to that order).
    The measure is the board's: our matter's 8 pi G rho/c^2 against eq. (17)'s radial tidal term |R4(k,k)| at r, for
    the example README.  (i) Our densest matter at the mouth, bounded by nuclear density: C1's figure at r = 3m.
    (ii) The uniform dark energy (rho_L = (1 - Omega_m) 3 H0^2/(8 pi G), READ Planck via cosmo.py, flat): its trace
    4 rho_L against the same term; eq. (17)'s term falls as r^-3, so eps_L(r) grows as r^3 and reaches 1 at R_L.
    (iii) Exact eq. (17) out to R* = infinity (M1-global) needs R4 = 0 on P1, and B1q gives R4 != 0 for any uniform
    dark energy, as plane matter (tau = -rho_L h) or as a tension shift (q != 1): EXCLUDED in its exact form (deduced
    from B1q, computed, with the READ dark-energy density).  (iv) The reach-limited shares: Z2's per-leg integral and
    E4's total - pull within r = 30m."""
    cosmo = _load(COSMO, "f1a_cosmo")
    H0 = cosmo.H0_KMSMPC * 1e3 / cosmo.MPC
    rho_L = (1 - cosmo.OMEGA_M) * 3 * H0**2 / (8 * math.pi * G) if cfg["rho_lambda_on"] else 0.0
    rr = tid["r"]
    R4f = sp.lambdify(rr, sp.Abs(tid["R4_kk"]), "math")
    need = lambda r: R4f(r) * c**2 / (8 * math.pi * G * mN**2)     # kg/m^3 at which 8 pi G rho/c^2 = |R4(k,k)|
    tidal = need(3.0) > 0                                          # a vacuum trace (the Schwarzschild foil) has none
    eps_L = lambda r: 4 * rho_L / need(r) if tidal else float("inf")
    R_L = float("inf")
    if rho_L > 0 and tidal:
        lo, hi = 3.0, 1e80
        for _ in range(300):
            mid = math.sqrt(lo * hi)
            lo, hi = (mid, hi) if eps_L(mid) < 1 else (lo, mid)
        R_L = math.sqrt(lo * hi)
    isr = israel_m(cfg)
    rl = isr["rho_L"]
    de_ok = rho_L > 0 and sp.simplify(isr["R4_de"]) != 0 and sp.simplify(isr["R4_de"].subs(rl, 0)) == 0
    sh_ok = sp.simplify(isr["R4_shift"].subs(isr["q"], 1)) == 0 and sp.simplify(isr["R4_shift"]) != 0
    p5 = owner("passage5d")
    import mpmath as mp
    f = lambda u: p5.q_of_u(float(u)) * p5.rho_u(float(u))
    leg_all = float(mp.quad(f, [0, 1, 10, mp.inf]))
    leg_30 = float(mp.quad(f, [0, 1, math.sqrt(28.0)]))
    lg = _memo("ledger_e4", lambda: owner("ledger").e4())
    Rl = next(q_ for q_ in lg["M"].free_symbols if q_.name == "r")
    ml = next(q_ for q_ in lg["M"].free_symbols if q_.name == "m")
    e4_30 = float(((lg["M"] - lg["at_throat"]) / (lg["far"] - lg["at_throat"])).subs({Rl: 30 * ml}).subs(ml, 1))
    return {"rho_L_kgm3": rho_L, "eps_nuc_3m": cfg["rho_nuc"] / need(3.0) if tidal else float("inf"),
            "eps_L_3m": eps_L(3.0),
            "eps_L_30m": eps_L(30.0), "R_L_m_units": R_L, "R_L_metres": R_L * mN, "exact_excluded_de": bool(de_ok),
            "exact_excluded_shift": bool(sh_ok), "leg_all": leg_all, "leg_30_share": leg_30 / leg_all,
            "e4_30_share": e4_30}


# ------------------------------------------------------------------------------------------------ C8 the cypher (196)
def cypher_m1(cfg, rows):
    """H-M1-TRACE-INDEX (the board's).  Cells: static near-horizon configurations whose plane trace is eq. (17)'s
    AdS2(2m) x S2(2m), on the computed grid x = 2m/ell: the regular single-plane caps (x, rho-rank > 0, regular 1) and
    the matter-free plane's Q = 0 bulk (x, 0, regular 0; singular at y_s, C2).  The question: (x, 0, 1) -- single
    plane, our matter only, regular.  Its absence is by construction (C2 found the rho = 0 configuration singular), so
    the closures restate C2: the PROJECTION to (rho, regular) is excluded alike -- a two-coordinate dependence the
    closures see.  The cypher adds no independent exclusion.  Control (must flip): add a coordinate 'extremal' and
    Route 1's READ non-extremal vacuum RS-II families as (x, 0, 1, 0) (ITEM185: Tangherlini, KTN, FW, AC-PYT cover the
    grid's x); only there does a three-way reading (extremal, regular, no added matter) apply."""
    cy = _load(CYPHER, "f1a_cypher", register=True)
    good = [r for r in rows if r["m"]]
    xs = sorted(r["cut"]["L"] for r in good)
    xr = {x: i for i, x in enumerate(xs)}
    rr = sorted(r["m"]["rho"] for r in good)
    rho_rank = {v: i + 1 for i, v in enumerate(rr)}
    caps = [[xr[r["cut"]["L"]], rho_rank[r["m"]["rho"]], 1] for r in good]
    vac = [[xr[x], 0, 0] for x in xs if ys(2.0 / x) is not None]
    qcells = [[i, 0, 1] for i in range(len(xs))]
    cells_a = caps + vac + (qcells if cfg["cy_add_question"] else [])
    caps4 = [cl + [1] for cl in caps]
    vac4 = [cl + [1] for cl in vac]
    route1 = [] if cfg["cy_drop_route1"] else [[i, 0, 1, 0] for i in range(len(xs))]
    cells_b = caps4 + vac4 + route1
    q4 = [[i, 0, 1, 1] for i in range(len(xs))]
    proj = [list(t) for t in sorted({(cl[1], cl[2]) for cl in cells_a})]
    wit = {"analysis": {"speaks": True, "witness": "continuous law rho/sigma = f(2m/ell) along the caps (C4-C5, computed)"}}
    opts = {"statistics_order": 2, "algebra_budget": 20000}

    def ask(name, coords, cells, questions):
        out = {}
        for rn in sorted(cy.ROSTERS):
            ix = cy.Index(name, coords, cells, None, wit)
            res = cy.run(ix, rn, opts)
            per = {}
            for lang in cy.ROSTERS[rn]["languages"]:
                if lang in cy.ADMISSION:
                    adm, _ = cy.ADMISSION[lang][0](ix, opts)
                    if adm is None:
                        per[lang] = "SILENT"
                    else:
                        enc = [tuple(ix.code[i][v] for i, v in enumerate(q)) for q in questions]
                        per[lang] = sum(e in adm for e in enc)
                elif lang in cy.DECLARED_ONLY:
                    per[lang] = "DECLARED"
                else:
                    per[lang] = "NOT-RUN"
            out[rn] = {"per": per, "bearing": res["operator_bearing_measured"], "degenerate": res["degenerate"],
                       "E": {v.language: v.E for v in res["_verdicts"]}}
        return out
    a = ask("H-M1-TRACE-INDEX: eq. (17)-trace near-horizon configurations", ["x", "rho", "regular"], cells_a, qcells)
    b = ask("CONTROL: with Route 1's non-extremal families", ["x", "rho", "regular", "extremal"], cells_b, q4)
    pj = ask("PROJECTION of H-M1-TRACE-INDEX to (rho, regular)", ["rho", "regular"], proj, [[0, 1]])
    reg = [cl for cl in cells_a if cl[2] == 1]
    seen = {}
    for cl in reg:
        seen.setdefault(cl[0], set()).add(cl[1])
    return {"a": a, "b": b, "proj": pj, "n_q": len(qcells), "one_cap_per_x": all(len(v) == 1 for v in seen.values())}


# ------------------------------------------------------------------------------- C11 the stress question (196; OC-4)
STRESS_LAW = [("P1", "own", 1, "184 with 129 (1): our plane carries our universe's matter"),
              ("P2", "own", 1, "184: position 2's plane carries its universe's matter"),
              ("P2", "readme", 1, "172 (1): position 2's piece may carry the README's stress"),
              ("P1", "added", 0, "130 (1): no added matter"), ("P2", "added", 0, "130 (1): no added matter")]


def cypher_stress(cfg):
    """H-STRESS-INDEX (the board's).  The question H-OWN-MATTER-ONLY answers by reading: may our plane P1 carry the
    README's stress at the corridor's mouth while the corridor holds?  Cells: (plane, stress kind, allowed), one per
    ruling (STRESS_LAW).  The plane and the stress kind are nominal, so their value orders are the encoding's choice;
    every order is swept (2 x 6).  A language DECIDES only if, in every order, it admits exactly one of (P1, readme, 1)
    and (P1, readme, 0), the same one.  Control (must flip): the index with (P1, readme, 1) seated as a cell."""
    cy = _load(CYPHER, "f1a_cypher", register=True)
    law = [tuple(c_[:3]) for c_ in STRESS_LAW]
    q1, q0 = ("P1", "readme", 1), ("P1", "readme", 0)
    if cfg["cy_stress_add_q1"]:
        law = law + [q1]
    ctl = sorted(set(law + [q1]), key=str)
    opts = {"statistics_order": 2, "algebra_budget": 20000}

    def sweep(cells):
        out = {}
        for rn in sorted(cy.ROSTERS):
            per = {}
            for lang in cy.ROSTERS[rn]["languages"]:
                if lang not in cy.ADMISSION:
                    per[lang] = "DECLARED" if lang in cy.DECLARED_ONLY else "NOT-RUN"
                    continue
                ver = set()
                for po in itertools.permutations(["P1", "P2"]):
                    for so in itertools.permutations(["own", "readme", "added"]):
                        ix = cy.Index("H-STRESS-INDEX", ["plane", "stress", "allowed"], cells,
                                      {"plane": list(po), "stress": list(so), "allowed": [0, 1]},
                                      {"analysis": {"speaks": False}})
                        adm, _ = cy.ADMISSION[lang][0](ix, opts)
                        if adm is None:
                            ver.add("SILENT")
                            continue
                        enc = lambda qq: tuple(ix.code[i][v] for i, v in enumerate(qq)) in adm
                        ver.add((enc(q1), enc(q0)))
                ver = sorted(ver, key=str)
                per[lang] = {"verdicts": ver, "decides": "allowed" if ver == [(True, False)] else
                             ("excluded" if ver == [(False, True)] else ("SILENT" if ver == ["SILENT"] else "no"))}
            out[rn] = per
        return out
    return {"law": sweep(law), "control": sweep(ctl)}


# ------------------------------------------------------------------------------------------------ C9 the green table
AFTER = {
    "G1": ("DERIVED", ["M1"]),          # E(N) = r0 c^4/(2G) is the plane's horizon relation, M1-c at the horizon
    "G3": ("PROVED", ["M1"]),
    "H2": ("DERIVED", ["M132"]),        # M's 132 verbatim, carried as M's (no axiom claimed)
    "H2t": ("PROVED", ["M1", "M1-P2"]),  # axioms.py's H2 is plural: P1's future and P2's past horizon
    "O1a": ("DERIVED", ["M132", "M130"]),
    "O1b": ("DERIVED", ["M1"]),         # no curvature singularity (M1-e) only
    "O1c": ("OPEN", []),                # geodesic completeness: never computed, even for eq. (17) (plane.py P1)
    "O2": ("DERIVED", ["M1"]),
    "Z1q": ("PROVED", []),
    "Z1t": ("PROVED", ["M1"]),
    "Z2r": ("PROVED", ["M1"]),          # our leg, within the reach, to M1-c's order
    "Z2": ("PROVED", ["M1-global", "M1-P2"]),
    "B1q": ("PROVED", []),
    "B2q": ("PROVED", []),
    "B2t": ("PROVED", ["M1"]),
    "B3": ("OPEN", ["M1", "F3", "F4", "F5"]), "B4b": ("READING", ["M1", "F4"]),
    "B4d": ("OPEN", ["M1", "F2", "F4", "F5"]),
    "E4r": ("PROVED", ["M1"]),          # total - pull within the reach: (E/4)(1 - m/(2R* - 3m)), to M1-c's order
    "E4": ("PROVED", ["M1-global"]),    # the exact E/4 is the far-field mass
    "M1": ("OPEN", []), "M1-P2": ("OPEN", []), "M1-global": ("EXCLUDED", []),
}
AUDITED = ("G1", "G3", "H2", "O1", "O2", "Z1", "Z2", "B1", "B2", "B3", "B4b", "B4d", "E4")
COVERS = {"G1": ["G1"], "G3": ["G3"], "H2": ["H2", "H2t"], "O1": ["O1a", "O1b", "O1c"], "O2": ["O2"],
          "Z1": ["Z1q", "Z1t"], "Z2": ["Z2r", "Z2"], "B1": ["B1q"], "B2": ["B2q", "B2t"], "E4": ["E4r", "E4"]}


def green_table(cfg):
    """STRUCTURAL: the board's green rule (a lemma is GREEN iff its status is PROVED, DERIVED or AXIOM and every input
    is green).  M's carried rulings (M132, M130) count as green inputs -- the sibling convention (b1_matter.py's
    AXIOM_ITEMS), meaning M's carried statement, not an axiom M declared.  BEFORE: statuses as the item-192 list recorded them (warptheorem.py, re-seated on item 206, cross-checked where a name is seated whole) --
    LEMMAS, inputs from the item-192 audit's list as b1_matter.py records it (AUDIT_INPUTS), with G1 and G3 corrected
    to carry F1 (F1A-R2).  AFTER: this audit's proposal (AFTER), with M1, M1-P2 and M1-global in F1's place."""
    wt = _load(WARPTHEOREM, "f1a_warptheorem")
    b1m = _load(B1MATTER, "f1a_b1matter")
    live = {name.split()[0]: st for _, name, st, _ in wt.LEMMAS}
    # item 210: rows superseded by B4d stay on record with the status they were seated with
    live.update({name.split()[0]: st for _, name, st, _ in getattr(wt, "SUPERSEDED", [])})
    # The item-192 list is history: item 206 re-seated the table, splitting O1, Z1, Z2 and E4 into the parts this audit
    # proposed (COVERS).  BEFORE reads the statuses that list recorded; the live table is checked against it wherever an
    # audited name is still seated whole, and each name no longer seated must have a part of its split seated.
    wstat = {k: b1m.AUDIT_STATUS[k] for k in AUDITED}
    reseated = sorted(k for k in AUDITED if k not in live)
    G = {"PROVED", "DERIVED", "AXIOM"}
    green_in = {"M132": True, "M130": True}
    listed = {k: (wstat[k], b1m.AUDIT_INPUTS[k].split()) for k in AUDITED}
    corrected = {k: (st, list(ins) + (["F1"] if k in ("G1", "G3") and not cfg["g13_f1_free"] else []))
                 for k, (st, ins) in listed.items()}
    after = dict(AFTER)
    if cfg["z2_on_m1"]:
        after["Z2"], after["E4"] = ("PROVED", ["M1"]), ("PROVED", ["M1"])
    if cfg["keep_B1_F2"]:
        after["B1q"] = ("PROVED", ["F2"])
    if cfg["m1_green"]:
        after["M1"] = ("PROVED", [])

    def greens(table):
        done, changed = {}, True
        while changed:
            changed = False
            for k, (st, ins) in table.items():
                ok = st in G and all(done.get(i, green_in.get(i, False)) for i in ins)
                if done.get(k) != ok:
                    done[k] = ok
                    changed = True
        return done
    return {"status_agree": all(live[k] == b1m.AUDIT_STATUS[k] for k in AUDITED if k in live)
            and all(any(p in live for p in COVERS.get(k, [])) for k in reseated), "reseated": reseated,
            "F1_listed": {k: "F1" in b1m.AUDIT_INPUTS[k].split() for k in AUDITED},
            "before_listed": greens(listed), "before": greens(corrected), "after": greens(after),
            "with_M1": greens(dict(after, M1=("PROVED", []))),
            "with_M1_P2": greens(dict(after, **{"M1": ("PROVED", []), "M1-P2": ("PROVED", [])})),
            "covers": COVERS}


# ========================================================================================================= compute
def compute(cfg=None):
    cfg = dict(DEFAULT, **(cfg or {}))
    C3_DIV[0] = cfg["c3_div"]
    return {"A": part_a(cfg), "B": part_b(cfg), "C": part_c(cfg), "NH": _memo(("nh_eq", cfg["nh_lam"], cfg["israel_sign"]),
                                                                 lambda: nh_equations(cfg["nh_lam"], cfg["israel_sign"])),
            "cfg": cfg}


def checks(d):
    A, B, C, NH = d["A"], d["B"], d["C"], d["NH"]
    m = sp.Symbol("m", positive=True)
    out = []
    add = lambda name, ok: out.append((name, bool(ok)))
    # ---- PART A
    add("A1 H2/G1 (axioms.py, computed): eq. (17)'s horizon r = 2m holds N A_bit, and the throat r0 = 2m sits on it",
        A["A1"]["horizon"] == [2 * m] and A["A1"]["H2"] and A["A1"]["throat_on_horizon"])
    add("A2 O1 (exactE.py, z3): one way under H-FUTURE-INGOING proved; both controls refuted",
        A["A2"]["one_way"] == "proved" and A["A2"]["controls"] == ["refuted", "refuted"])
    add("A3 O2 (stability.py S1, computed): D'(rho_H) = 0 at r0 = 2m; the r0 = 1.8m control is not extremal",
        A["A3"]["D1"] == 0 and A["A3"]["control_D1"] != 0)
    add("A4 Z1 (passage5d.py P2, computed): R5(n,k,n,k) = -R4(k,k) = (1/2)/((r - 3/2)^2 r) from the bulk series",
        A["A4"]["identity"] and A["A4"]["closed"])
    add("A5 Z2 (passage5d.py P3, coin.py): Q = 1.652872/m = -2 x the per-leg reading", abs(A["A5"]["Q"] - Q_REF) < 1e-6
        and abs(A["A5"]["Q"] + 2 * A["A5"]["leg"]) < 1e-9)
    add("A6 B1 (localbulk.py L1): with K = -g/ell Gauss demands R(4) = 0, and eq. (17) has R(4) = 0",
        A["A6"]["gauss"] == 0 and A["A6"]["R4"] == 0)
    add("A7 B2 (localbulk.py L3 + independent): d rho/du = 2 sqrt(m/2 + u^2), even -- analytic data through the horizon",
        A["A7"]["owner_L3"] and A["A7"]["independent"])
    add("A8 B4b (b4_static.py S3, banked): t_cert in (10, 12) clocks with K <= 5 in its cone; the per-bit hold K > 1e4",
        10 < A["A8"]["t_cert"] < 12 and A["A8"]["Kmax_cert"] < 5 and A["A8"]["Kmax_o3"] > 1e4)
    add("A9 B4d (b4d_stage6.py J6, STRUCTURAL): a positive-tension plane has a decaying side (owner grid and its "
        "sigma_over_rs)", A["A9"]["J6"] and A["A9"]["owner_J6"])
    add("A10 E4 (ledger.py; plane.py cross-check): M(R) = m + (m/4)(1 - m/(2R - 3m)), m at the throat, 5m/4 far, "
        "dM/dR > 0", A["A10"]["closed_ok"] and A["A10"]["dM_pos"] and A["A10"]["cross_plane"]
        and sp.simplify(A["A10"]["far"] - 5 * A["A10"]["m"] / 4) == 0)
    # ---- PART B
    ax = B["axioms"]["found"]
    add("B1 READ: M's 132 (both halves), 129 (1), 130 (1), 172 (1), 179/180, 183, 184, 187's (G), 194, 195 verbatim in "
        "the rulings file", all(ax.values()))
    add("B2 READ (via epass_ground.json): Kaus-Reall p.4 (kappa constant), (2.2), p.5 (compact), (2.16), p.11 (matter)",
        all(B["reads"].values()))
    k = B["kappa"]
    add("B3 deduced/computed: a throat on the horizon does not force kappa = 0 (Schwarzschild kappa^2 = 1/(16m^2)); "
        "eq. (17) at r0 = 2m has kappa = 0", sp.simplify(k["kappa2_schw"] - 1 / (16 * m**2)) == 0
        and k["kappa2_eq17"] == 0)
    tg = B["tangency"]
    add("B4 STRUCTURAL/computed: the black string's kappa is 1/(4m) at every depth (the plane's); KR's ansatz has "
        "kappa = 0 at every rho", sp.simplify(tg["string_kappa2"] - 1 / (16 * m**2)) == 0 and tg["nh_kappa2_at_x0"] == 0)
    add("B5 computed: the contracted Gauss identity R5(k,k) = R4(k,k) + R5(n,k,n,k) - K K(k,k) + (K.K)(k,k) checked on "
        "two families (the identity itself is the standard-not-READ Gauss equation)",
        all(r == 0 for r in B["gauss"]["residuals"]))
    isr = B["israel"]
    add("B6 computed (symbolic, any symmetric tau): Z1q for a Z2 plane of tension q sigma_RS, q 8 pi G tau(k,k) + "
        "kappa5^4 pi(k,k) = R4(k,k) + R5(n,k,n,k); its q = 1 form (our plane) FAILS at q = -1/3, -1/4, -1/6, 4/3",
        isr["null_q"] == 0 and isr["null_res"] == 0 and all(v[0] for v in isr["q1_fails"].values()))
    add("B7 computed (symbolic): B1q, -R4 = -12(q^2-1)/ell^2 + q 8 pi G tau + kappa5^4 (tau.tau/4 - tau^2/12); the q = 1 "
        "form fails at position 2's q; a non-Z2 plane is outside (tau = 0, K = -h/ell + diag(0,d,-d,0): R4 = -2d^2)",
        isr["scalar_q"] == 0 and isr["scalar_res"] == 0 and all(v[1] for v in isr["q1_fails"].values())
        and sp.simplify(isr["nonZ2_R4"] + 2 * sp.Symbol("d", real=True) ** 2) == 0)
    pf = isr["pi_fluid"]
    add("B8 computed: pi(k,k) is not sign-definite under the NEC (diagonal tau, rho = 0, p1 = 1: -1/6), but is "
        "rho (rho + p)/6 for a perfect fluid -- so Z2's inequality holds for perfect fluids or matter << sigma",
        isr["pi_counter"] == -sp.Rational(1, 6)
        and sp.simplify(pf - isr["pi_fluid_rho"] * (isr["pi_fluid_rho"] + isr["pi_fluid_p"]) / 6) == 0)
    # ---- PART C
    c1 = C["C1"]
    add("C1 computed: the 4D-limit candidate (Weyl term zero) has R4(k,k) < 0 at every r tested and net -Q per ray "
        "(against 183); at r = 3m for the example README it needs 1.0e80 kg/m^3, nuclear density supplies 2.3e-63 of it",
        all(v < 0 for v in c1["R4kk"]) and abs(c1["net"] + Q_REF) < 1e-5 and 0.95e80 < c1["need_3m_kgm3"] < 1.05e80
        and 2.2e-63 < c1["ours_over_need"] < 2.4e-63)
    add("C2 computed: matter-free (Q = 0) data reach the singularity at y_s = 2.5536m (flat), 0.9139m (ell = m) -- "
        "SIM2's numbers", C["C2"]["ys_flat"] is not None and abs(C["C2"]["ys_flat"] - YS_FLAT) < 2e-3
        and C["C2"]["ys_ell_m"] is not None and abs(C["C2"]["ys_ell_m"] - YS_ELL_M) < 2e-3)
    c2b = C["C2b"]
    add("C2b numerical (RK4, sampled): on a negative-tension plane (growing side) no singularity to y = 50m at ell = 2m "
        "and 4.79m; singular at the sampled 4.80m, 8m (3.95m deep) and at position 2's ell_2 = 3 x 27.07m (2.634m) and "
        "6 x 27.07m (2.593m)",
        c2b["ell_2"] is None and c2b["ell_479"] is None and c2b["ell_480"] is not None and c2b["ell_8"] is not None
        and abs(c2b["ell_8"] - 3.951) < 0.01 and c2b["p2_3"] is not None and abs(c2b["p2_3"] - 2.634) < 0.01
        and c2b["p2_6"] is not None and abs(c2b["p2_6"] - 2.593) < 0.01)
    add("C3 computed: integrator controls -- AdS5 (A0 = ell) to 1e-9; the exact cap A0 = ell/2 cuts at L = ell/2 with "
        "rho/sigma = (2 sqrt6 - 3)/3, p/sigma = (3 - sqrt6)/3", C["C3"]["ads5_err"] < 1e-9 and C["C3"]["half"]
        is not None and abs(C["C3"]["half"]["L"] - 0.5) < 1e-8 and abs(C["C3"]["half_m"]["rho"]
                                                                       - (2 * math.sqrt(6) - 3) / 3) < 1e-8
        and abs(C["C3"]["half_m"]["p"] - (3 - math.sqrt(6)) / 3) < 1e-8)
    add("C3b computed: the cap's series start meets the Hamiltonian constraint (rho^2 x residual < 1e-10 at every grid "
        "A0); a wrong cubic coefficient leaves an O(1) residual that no other check sees", C["C3"]["start_con"] < 1e-10)
    rows = C["C4"]["rows"]
    okrows = [r for r in rows if r["m"]]
    add("C4 numerical (RK4, the 12 grid caps): each cuts, with the constraint to 1e-9, rho > 0 and rho + p > 0 (rho + p_r "
        "= 0 by AdS2); L/ell rises and rho/sigma falls along the grid; one crossing of A = R, to rho = 60 ell or to the "
        "continuation's end beyond the cut, at A0 = 0.005, 0.02, 0.05 (in the window), 0.6, 0.8, 0.95; none at 1.2, 1.5",
        len(okrows) == len(GRID) and all(abs(r["m"]["con_rel"]) < 1e-9 and r["m"]["rho"] > 0
                                         and r["m"]["rho"] + r["m"]["p"] > 0 for r in okrows)
        and all(okrows[i]["cut"]["L"] < okrows[i + 1]["cut"]["L"] and okrows[i]["m"]["rho"] > okrows[i + 1]["m"]["rho"]
                for i in range(len(okrows) - 1)) and all(C["C4"]["no_cut"])
        and [c_[0] for c_ in C["C4"]["crossings"]] == [1] * len(CROSS_A0))
    small = [r["m"]["rho"] * r["cut"]["L"] for r in okrows[:1]]
    big = okrows[-1]["m"]["rho"] * okrows[-1]["cut"]["L"] ** 2 if okrows else 0
    add("C5 computed: limits -- rho/sigma -> 0.6627 ell/L as L/ell -> 0 (the ell = infinity cap) and -> (1/6)(ell/L)^2 as "
        "L/ell -> infinity (4D GR's Bertotti-Robinson matter rho = 1/(8 pi G L^2))",
        C["C4"]["c_flat"] is not None and abs(C["C4"]["c_flat"] - 0.6627) < 2e-3 and small
        and abs(small[0] - C["C4"]["c_flat"]) < 0.01 * C["C4"]["c_flat"] and abs(big - 1 / 6) < 1e-3)
    c6 = C["C6"]
    add("C6 computed (gates at the printed figures): at SIM2's edge rho = 8.02 sigma_RS (>= 8.0); B4c's edge 1.3e5; "
        "sigma_RS = 7.17e18 x nuclear (ell <= 13.964 um); the example README needs 1.67e41 x nuclear; ours suffices "
        "only for 2m >= 1.53e4 m, N >= 4.0e78 (4.6e77 at 2e18 kg/m^3) >> 1.088e29; without the upper edge ell >= 2.3e36 m",
        8.0 <= c6["rho_edge"] < 8.05 and 1.30e5 < c6["rho_b4c"] < 1.35e5 and 7.1e18 < c6["sigma_over_nuc"] < 7.2e18
        and 1.6e41 < c6["need_example_over_nuc"] < 1.7e41 and 1.52e4 < c6["L_star_m"] < 1.53e4
        and 4.0e78 < c6["N_star"] < 4.1e78 and 4.6e77 < c6["N_star_ns"] < 4.7e77 and c6["N_star"] > 1e40 * SNAPSHOT_N
        and 2.3e36 < c6["ell_need_example_m"] < 2.4e36)
    add("C7 computed: b > a at every cap's cut, so two capped sides cannot cancel their anisotropy (J1's Pi_L = -Pi_R)",
        C["C7"]["b_gt_a"] and all(C["C7"]["b_gt_a"]) and len(C["C7"]["b_gt_a"]) == len(GRID))
    cya, cyb = C["C8"]["a"]["1173"], C["C8"]["b"]["1173"]
    num = lambda per: {k_: v for k_, v in per.items() if isinstance(v, int)}
    add("C8 cypher (196, H-M1-TRACE-INDEX): no operator-bearing language admits the question cell (every roster); the "
        "index has one cap per grid x (by construction)",
        all(all(v == 0 for v in num(r["per"]).values()) and len(num(r["per"])) >= 2 for r in C["C8"]["a"].values())
        and len(num(cya["per"])) >= 4 and not cya["degenerate"] and C["C8"]["one_cap_per_x"])
    pj = C["C8"]["proj"]["1173"]["per"]
    add("C8 projection: on (rho, regular) alone order, algebra, geometry and information also admit no (0, 1) -- the "
        "exclusion is the index's own two-coordinate dependence (C2 restated), not an independent finding",
        all(pj.get(lg_) == 0 for lg_ in ("order", "algebra", "geometry", "information")))
    add("C8 control: with Route 1's READ non-extremal families added, every operator-bearing language admits it -- a "
        "three-way reading applies to the control index only", all(v == C["C8"]["n_q"] for v in num(cyb["per"]).values())
        and len(num(cyb["per"])) >= 4)
    g = C["C9"]
    bef = ["H2", "O1", "O2", "Z1", "Z2", "B1", "B2", "E4"]
    add("C9 STRUCTURAL (imported): warptheorem.py's statuses agree with the item-192 list wherever a name is still "
        "seated whole (O1, Z1, Z2, E4 re-seated split on item 206, a part of each seated); that list puts F1 under the "
        "ten audited lemmas and none under G1, G3; corrected for G1, G3 (axioms.py places the horizon with eq. (17)'s "
        "F = 0), none of the ten green-status F1 lemmas is green",
        g["status_agree"] and g["reseated"] == ["E4", "O1", "Z1", "Z2"]
        and all(g["F1_listed"][k_] for k_ in bef + ["B3", "B4b", "B4d"])
        and not g["F1_listed"]["G1"] and not g["F1_listed"]["G3"] and g["before_listed"]["G1"]
        and g["before_listed"]["G3"] and not any(g["before"][k_] for k_ in bef + ["G1", "G3"]))
    add("C9 STRUCTURAL: after the edits, with M1 OPEN, exactly H2, O1a, Z1q, B1q, B2q are green",
        sorted(k_ for k_, v in g["after"].items() if v) == sorted(["H2", "O1a", "Z1q", "B1q", "B2q"]))
    gain = sorted(k_ for k_, v in g["with_M1"].items() if v and not g["after"][k_])
    gain2 = sorted(k_ for k_, v in g["with_M1_P2"].items() if v and not g["with_M1"][k_])
    add("C9 STRUCTURAL: with M1 proved, G1, G3, O1b, O2, Z1t, Z2r, B2t, E4r (and M1) turn green; with M1-P2 too, H2t; "
        "Z2 and E4 (M1-global, excluded in its exact form), O1c, B3, B4b, B4d never",
        gain == sorted(["G1", "G3", "O1b", "O2", "Z1t", "Z2r", "B2t", "E4r", "M1"]) and gain2 == ["H2t", "M1-P2"]
        and not any(g["with_M1_P2"][k_] for k_ in ("Z2", "E4", "O1c", "B3", "B4b", "B4d", "M1-global")))
    c10 = C["C10"]
    add("C10 computed (M1-c's bound): nuclear density is 2.3e-63 of eq. (17)'s tidal term at 3m; the READ dark energy "
        "(~5.8e-27 kg/m^3) is 1e-106 of it at 3m and reaches it at r ~ 3e35 m(N); exact eq. (17) to infinity is "
        "excluded (B1q: R4 != 0 for tau = -rho_L h and for q != 1); within 30m lie 99.96% of Z2's leg and 98.2% of E/4",
        5.5e-27 < c10["rho_L_kgm3"] < 6.2e-27 and 2.2e-63 < c10["eps_nuc_3m"] < 2.4e-63 and c10["eps_L_3m"] < 1e-100
        and 1e35 < c10["R_L_m_units"] < 1e36 and c10["exact_excluded_de"] and c10["exact_excluded_shift"]
        and abs(c10["leg_all"] - Q_REF / 2) < 1e-6 and 0.9995 < c10["leg_30_share"] < 0.9998
        and abs(c10["e4_30_share"] - (1 - 1 / 57)) < 1e-9)
    st = C["C11"]
    dec = lambda sw: [(rn, lg_, v["decides"]) for rn, per in sw.items() for lg_, v in per.items()
                      if isinstance(v, dict) and v["decides"] in ("allowed", "excluded")]
    nb = [v for v in st["law"]["1173"].values() if isinstance(v, dict) and v["decides"] != "SILENT"]
    add("C11 cypher (196, H-STRESS-INDEX): may our plane carry the README's stress at the mouth?  Over every value order "
        "no language of any roster decides it; the control (that cell seated) is decided 'allowed' by at least one",
        not dec(st["law"]) and len(nb) >= 4
        and any(v == "allowed" for _, _, v in dec(st["control"])) and not any(v == "excluded" for _, _, v in
                                                                            dec(st["control"])))
    add("NH computed: KR's (2.4)/(2.6) derived for the ansatz equal the integrator's right-hand sides; the cut's "
        "Hamiltonian constraint is the SMS trace equation", NH["resA"] == 0 and NH["resR"] == 0
        and NH["cut_vs_sms"].is_number and NH["cut_vs_sms"] != 0)
    return out


MUTANTS = [
    ("r0 = 9m/5 (another Bronnikov-Kim member)", {"r0_over_m": sp.Rational(9, 5)}),
    ("the passage5d foil (non-umbilic first order)", {"z1_first": "foil"}),
    ("artanh(1/2) in Q", {"q_arg": sp.Rational(1, 2)}),
    ("Lambda5 of the wrong sign", {"lam5_sign": 1}),
    ("Schwarzschild-de Sitter in place of eq. (17)", {"b1_metric": "sds"}),
    ("read the outgoing control as the one-way claim", {"o1_key": "ctl"}),
    ("the banked curvature x 100", {"bank_K_scale": 100}),
    ("stage 6's sign convention flipped", {"j6_flip": True}),
    ("a corrupted 132 quote", {"axiom_132": "corrupt"}),
    ("Schwarzschild given a double-zero H", {"kappa_H": "F2"}),
    ("the black string's inverse metric mis-warped", {"string_grr": "bad"}),
    ("the Gauss K-terms with the wrong sign", {"gauss_sign": -1}),
    ("Israel's sign flipped", {"israel_sign": -1}),
    ("Lambda5 coefficient 3 in the near-horizon ODE", {"nh_lam": 3.0}),
    ("the black string's tidal term for the 4D candidate", {"c1_metric": "schw"}),
    ("Q = 0 data integrated toward the wrong side", {"ys_side": 1}),
    ("our matter 1e65 x nuclear", {"rho_nuc": RHO_NUC * 1e65}),
    ("the question cells put into the index", {"cy_add_question": True}),
    ("Route 1 dropped from the control", {"cy_drop_route1": True}),
    ("M1 marked green", {"m1_green": True}),
    ("B1q kept on F2", {"keep_B1_F2": True}),
    ("a and b read swapped", {"swap_ab": True}),
    ("a corrupted Kaus-Reall quote", {"kr_quote": "corrupt"}),
    ("the cap start's cubic coefficient over 10 (F1A-R7)", {"c3_div": 10}),
    ("SMS's pi without its trace term", {"pi_form": "no_trace"}),
    ("no dark energy", {"rho_lambda_on": False}),
    ("Z2 and E4 keyed to M1 alone (F1A-R1, OC-1)", {"z2_on_m1": True}),
    ("(P1, readme, 1) seated in the stress index", {"cy_stress_add_q1": True}),
    ("G1 and G3 read F1-free, as the item-192 list has them (F1A-R2)", {"g13_f1_free": True}),
]


def selftest(verbose=True):
    t0 = time.time()
    res = checks(compute())
    ok = sum(c for _, c in res)
    if verbose:
        for name, c in res:
            print("  [%s] %s" % ("ok" if c else "FAIL", name))
        print("selftest: %d/%d (%.0f s)" % (ok, len(res), time.time() - t0))
    return ok == len(res)


def mutants():
    base = checks(compute())
    names = [n for n, _ in base]
    if not all(c for _, c in base):
        print("baseline selftest fails; mutants not run")
        return False
    killed = {n: [] for n in names}
    all_kill = True
    for label, over in MUTANTS:
        try:
            res = checks(compute(over))
            fails = [n for n, c in res if not c]
        except Exception as exc:                                    # a mutant that crashes a check also kills it
            fails = ["(crash: %s)" % type(exc).__name__]
        for n in fails:
            if n in killed:
                killed[n].append(label)
        print("  mutant %-52s fails %d check(s): %s" % (label, len(fails), ", ".join(f.split(" ")[0] for f in fails)))
        all_kill &= bool(fails)
    unkilled = [n for n, v in killed.items() if not v]
    for n in unkilled:
        print("  NOT KILLED: %s" % n)
    print("mutants: %d/%d mutants kill a check; %d/%d checks killed by some mutant"
          % (sum(1 for _ in MUTANTS) if all_kill else -1, len(MUTANTS), len(names) - len(unkilled), len(names)))
    return all_kill and not unkilled


def report(d):
    A, C = d["A"], d["C"]
    print("f1_audit.py -- input F1 (eq. (17) as our plane's own metric) across the twelve lemmas resting on it\n")
    print("PART A, the owners' decisive checks re-run (statements about eq. (17) on a matter-free RS-tension plane, F1 and "
          "F2; O1's 'nonsingular' OPEN even there):")
    print("  H2 horizon %s; O1 one way %s; O2 D' = %s (control %s); Z1 identity %s; Z2 Q = %.6f/m; B1 R4 = %s; "
          "B4b t_cert = %.2f clocks; E4 far mass 5m/4"
          % (A["A1"]["horizon"], A["A2"]["one_way"], A["A3"]["D1"], A["A3"]["control_D1"], A["A4"]["identity"],
             A["A5"]["Q"], A["A6"]["R4"], A["A8"]["t_cert"]))
    print("\nPART C, M1 (H-PLANE-READS-MOUTH as a theorem; OPEN):")
    print("  C1 4D-limit candidate: R4(k,k) at r = 2.01..100m = %s (< 0 pointwise); net per ray %.6f/m (against 183)"
          % (", ".join("%.3g" % v for v in C["C1"]["R4kk"]), C["C1"]["net"]))
    print("     needed at r = 3m, example README: %.3g kg/m^3; nuclear density supplies %.2g of it"
          % (C["C1"]["need_3m_kgm3"], C["C1"]["ours_over_need"]))
    print("  C2 matter-free plane's near-horizon bulk singular at y_s = %.4fm (flat), %.4fm (ell = m)"
          % (C["C2"]["ys_flat"], C["C2"]["ys_ell_m"]))
    c2b = C["C2b"]
    print("  C2b the same data on a negative-tension plane (growing side; RK4, sampled): ell = 2m %s, 4.79m %s, 4.80m %s, "
          "8m %s, 3 x 27.07m %s, 6 x 27.07m %s (None = no singularity to y = 50m)" % tuple(
              ("%.4fm" % v) if v is not None else "None" for v in (c2b["ell_2"], c2b["ell_479"], c2b["ell_480"],
                                                                    c2b["ell_8"], c2b["p2_3"], c2b["p2_6"])))
    print("  C3b cap start: rho^2 x Hamiltonian residual, max over the grid = %.2g" % C["C3"]["start_con"])
    print("  C4 regular single-plane caps reading AdS2(2m) x S2(2m) (RK4, grid):  2m/ell    rho/sigma     p/sigma")
    for r in C["C4"]["rows"]:
        if r["m"]:
            print("       A0/ell = %-7g %10.5g %12.6g %11.5g" % (r["A0"], r["cut"]["L"], r["m"]["rho"], r["m"]["p"]))
    print("     crossings of A = R to rho = 60 ell at A0 = %s: %s" % (list(CROSS_A0), C["C4"]["crossings"]))
    c6 = C["C6"]
    print("  C5 rho/sigma -> %.4f ell/(2m) small, -> (1/6)(ell/2m)^2 large (Bertotti-Robinson)" % C["C4"]["c_flat"])
    print("  C6 at 2m/ell = %.4f (SIM2's edge, itself resting on F1): rho = %.3f sigma_RS; at B4c's edge %.3g sigma_RS; "
          "sigma_RS/nuclear = %.3g at ell = 13.964 um; needed at the example README %.3g x nuclear; nuclear density would "
          "do only for 2m >= %.3g m, N >= %.2g bits (%.2g at 2e18 kg/m^3); without the upper edge, ell >= %.2g m"
          % (c6["x_edge"], c6["rho_edge"], c6["rho_b4c"], c6["sigma_over_nuc"], c6["need_example_over_nuc"],
             c6["L_star_m"], c6["N_star"], c6["N_star_ns"], c6["ell_need_example_m"]))
    for key, lab in (("a", "H-M1-TRACE-INDEX"), ("proj", "projection (rho, regular)"), ("b", "control (Route 1 added)")):
        for rn, v in C["C8"][key].items():
            print("  C8 cypher %-26s roster %-5s question admitted: %s" % (lab, rn, v["per"]))
    g = C["C9"]
    print("  C9 green before (item-192 list): %s | corrected for G1, G3: %s"
          % (sorted(k for k, v in g["before_listed"].items() if v), sorted(k for k, v in g["before"].items() if v)))
    print("     after edits: %s | with M1: %s | with M1 and M1-P2: %s" % (
        sorted(k for k, v in g["after"].items() if v), sorted(k for k, v in g["with_M1"].items() if v),
        sorted(k for k, v in g["with_M1_P2"].items() if v)))
    c10 = C["C10"]
    print("  C10 rho_L = %.3g kg/m^3 (READ Planck via cosmo.py); eps at 3m: nuclear %.2g, dark energy %.2g; eps_L = 1 at "
          "r = %.3g m(N) = %.3g m for the example README; exact M1-global excluded: %s (as tau), %s (as a tension shift); "
          "within 30m: %.4f of Z2's leg, %.4f of E4's E/4"
          % (c10["rho_L_kgm3"], c10["eps_nuc_3m"], c10["eps_L_3m"], c10["R_L_m_units"], c10["R_L_metres"],
             c10["exact_excluded_de"], c10["exact_excluded_shift"], c10["leg_30_share"], c10["e4_30_share"]))
    for key in ("law", "control"):
        for rn, per in C["C11"][key].items():
            print("  C11 stress question, %-7s roster %-5s %s" % (key, rn, {lg_: (v["decides"] if isinstance(v, dict)
                                                                            else v) for lg_, v in per.items()}))


def _jsonable(o):
    if isinstance(o, dict):
        return {str(k): _jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_jsonable(v) for v in o]
    if isinstance(o, (bool, int, float, str)) or o is None:
        return o
    return str(o)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    d = compute()
    if "--json" in sys.argv:
        json.dump(_jsonable(d), open(sys.argv[sys.argv.index("--json") + 1], "w"), indent=1)
    report(d)
