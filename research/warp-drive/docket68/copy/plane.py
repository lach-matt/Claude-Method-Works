#!/usr/bin/env python3
"""plane.py -- DOCKET 68, M-RULINGS items 101-111: the corridor as M describes it, in Bronnikov-Kim's family -- the pull
as its cost, its two-sided horizon and one-way passage, the three holds, one energy from device to build, and the
README read against the object it defines.  Deduced, computed and READ; verified twice (findings applied, History);
the item-107-111 parts not yet verified; not seated.  Write-up: PLANE.md.
First headed "...items 101 and 102 ...; not verified", then "...items 101, 102 and 104 ...; verified once".

M'S WORDS (verbatim in the rulings file)
  101.11 "total our plane can read".  104(b), choosing the pull: "observers at position 1 can only see the mouth at
  position 1. The corridor interior and position 2 are not observable until the horizon of the corridor is crossed, at
  which point position is no longer observable... Horizons have 2 sides".  106: "Horizon; reciprocal"; "Three distinct
  holds in one fluid wave motion, horizon position 1 only as the corridor opens, when the corridor is fully realized the
  bits are held on both horizons simultaneously because the corridor builds position 2 with the bits in mind, upon the
  corridor closing the bits are then held only at the horizon of position 2."; "Yes, it ends at P2".  107: "The
  information in transit is still the definition of the geometric object, just absent the actual physical mass, which
  makes it appear to be negative mass".  108: "Yes, that's it"; "Whatever is needed".  109: "The horizon of position
  ends as well. A horizon cannot exist without the object of which it needs to exist".  110: "Into position 2".  111:
  "that and only that which is provided by the closing of the horizon."; "one energy read from two sides because both
  positions are currently entangled as a singular state".

THE GEOMETRY (H-BK-CORRIDOR).  Bronnikov-Kim, gr-qc/0212112v1, eq. (17) p.4 (READ): ds^2 = (1 - 2m/r) dt^2 -
(1 - 3m/2r) dr^2 / ((1 - 2m/r)(1 - r0/r)) - r^2 dOmega^2; "a symmetric wormhole geometry for any r0 > 2m >= 0, or for any
r0 > 0 in case m < 0"; for eta = r0 - 3m/2 > 0 near Schwarzschild (BK's framing, after Casadio et al. [33]) "a
nonsingular black hole with a wormhole throat at r = r0 inside the horizon, in other words, a non-traversable wormhole";
eq. (18) rho = m (r0 - 3m/2) / (2 r^2 (r - 3m/2)^2).  The whole window r0/2 < m < 2r0/3 is the board's extension,
computed (BK give neither bound as such).

WHAT FOLLOWS THE WORK (item 82: lead with what passes)
  P1 YOUR CORRIDOR IS IN THE FAMILY, AND ITS HORIZON IS CROSSED ONE WAY, 1 -> 2.  The members with a horizon outside the
     throat and no singularity are exactly r0/2 < m < 2r0/3 (numerical, with a control and a contrast).  In BK's x-form
     (r = r0 + x^2, computed from eq. 17) g_tt = (x^2 + r0 - 2m)/(r0 + x^2) vanishes at x = +-sqrt(2m - r0): a horizon on
     each side.  Between them the dx^2 coefficient changes sign (-10.8 at x = 0 for m = 1, r0 = 1.8): x is TIMELIKE, so
     the throat is a moment, not a place, and every future-directed path that enters position 1's horizon crosses it and
     leaves through position 2's (a white-hole horizon on that side).  Control: for r0 > 2m the coefficient stays
     positive (an ordinary two-way throat).  Position 2 is unseen until position 1's horizon is crossed, then position 1
     is unseen: your H-CORRIDOR-HORIZON, H-ONE-MOUTH-SEEN, H-TWO-SIDED-HORIZON, computed.  BK's "non-traversable" is
     two-way traversal; one-way passage is what the geometry gives.  READ analogue (the verifier, alphaXiv): Simpson &
     Visser 1812.07114v3 p.3, for a < 2m "a one-way spacelike throat ... a bounce into a future incarnation of the
     universe"; pp.4-5, "a bounce into a separate copy of our own universe" -- beside your H-SEPARATE-UNIVERSES.
     Geodesic completeness is not computed: OPEN.
  P2 THE PULL AND THE FLOOR.  The pull our plane reads (Komar at infinity, the static region r > 2m reaching an
     asymptotically flat end) is m, equal to the horizon's area-mass sqrt(A/16 pi) = m (Misner-Sharp at r = 2m; sympy).
     The horizon's own Komar charge, kappa A / 4 pi = 2m sqrt(1 - r0/2m), is smaller (sympy; 0.63 m at r0 = 1.8 m); the
     rest is the tidal stress outside it.  Under H-HORIZON-HOLDS and H-STRONG-BOUND the least horizon has radius
     r_min(N), so the least pull is m = r_min/2: sqrt(N h c^5 ln2 / (8 pi^2 G)) = 4.59404002e8 J x sqrt(N) -- the floor's
     number, unchanged: chain.py's floor was a throat's area-mass, reread here as a horizon's (both r/2).  At that m the
     throat lies behind the horizon, r0 in (0.75, 1) r_min, and the plane's ADM total reads between 1 and 5/4 of the
     floor.
  P3 SUPERSEDED: "if the throat holds it instead, the pull lies between the floor and 4/3 of it" -- item 106 puts the
     bits on horizons, and in a horizon member the throat is a spacelike moment (P1).  Kept as history.
  P4 THE PENROSE INEQUALITY COINCIDES, IN THIS FAMILY, WITH THE REGULARITY CONDITION.  ADM > horizon area-mass iff
     r0 > 3m/2 (sympy) iff rho > 0 iff no singularity.  Premises (verifier): the t = const slice of the static exterior is
     time-symmetric; its scalar curvature is 16 pi rho_eff (eq. 18); r = 2m is its outermost minimal surface.  Bray
     math/9911173v1 eq. 6 p.4, Thm 1 p.8 (READ by a verifier).
  P5 ITEM 102: YOUR ANSWER "Horizon; reciprocal".  The board's reading (R-RECIPROCAL-AS-PRODUCT, ungraded): at the floor
     E x r = N h c ln2 / (4 pi^2) = 3.48772679e-27 J m x N -- by construction (Bekenstein saturated).  Along horizons mass
     grows with size; the two meet only at the floor.  The negative-mass member (m = -2 r0: ADM zero, rho < 0 everywhere,
     no horizon) is the boundary.
  P6 THE THREE HOLDS AND ONE ENERGY (106, 109-111).  Opening: position 1's horizon only; realized: both horizons, one
     entangled state, one energy read from two sides; closing: position 2's horizon, which ends with the corridor (109),
     its energy delivered into position 2 (110) and used, exactly, by the build (111).  The trip carries one E_min(N)
     from the device to the build.  "One energy read from two sides" has a computed counterpart: in the thermofield
     double (geometry.tfd, imported), the state ER=EPR pairs with a two-sided black hole, H_left - H_right has zero
     variance -- the two readings are one -- while in a product state with the same marginals they are independent
     (control).  The opening and closing holds have no static member: they need dynamics, and a Komar "pull" needs a
     Killing vector (H-QUASISTATIC): OPEN.
  P7 THE README AGAINST THE OBJECT IT DEFINES (107, 108).  Apparent mass = carried - defined.  The core README carries
     0.2676901 kg against the 70 kg it defines: -69.7323 kg, negative, as you said.  It appears negative while
     N < N* = 8 pi^2 G M^2 / (h c ln2) = 3.827306673e16 bits/kg^2 x M^2 = 1.875380270e20 bits for 70 kg; the largest
     snapshot (1.088e29 bits) would carry more than it defines.  At N* the closing energy equals Mc^2 (by construction).
     With item 111 the README and the build are one number: a build needing energy E needs N = 8 pi^2 G E^2/(h c^5 ln2).

WHAT IS RULED OUT, AS THE BOUNDARY
  * H-HOLD-PERSISTS (withdrawn by item 109; kept): a closing hold that stayed would be a hole of 0.2677 kg for the core,
    at most 4.583e23 K (Schwarzschild, H-SCHWARZSCHILD-REMNANT; for a BK member T = T_Sch x 2 sqrt(1 - r0/2m)), gone in
    about 7.8e-21 s (Carr-Kohri-Sendouda-Yokoyama 2002.12778v2 p.10 eq. 14, tau ~ 407 (f/15.35)^-1 M10^3 s, all
    Standard Model species, READ by a verifier; the photon-only 1.6e-18 s overestimates by ~200).
  * Two-way traversal (BK p.4); a positive-density member with a total below its horizon's area-mass (Bray); a horizon
    member with m >= 2r0/3 (contrast).
  * If each universe is asymptotically flat with its own Bondi mass (H-ASYMPTOTIC-FLAT-ENDS), plane 2's rise from 0 to
    E_min would need an energy flux the tidal stress could carry only by violating the energy conditions, which BK p.1
    allow ("E_mu nu does not necessarily satisfy the energy conditions"); Madler-Winicour 1609.01731v3 p.16 eq. 61 (READ
    by a verifier).  Your H-ONE-ENERGY-TWO-SIDES (one entangled state) is a different accounting: OPEN which applies.
  * BK p.2: "a restriction can quite probably appear from 5-dimensional geometry" on the throat's size (r_min, core,
    4.0e-28 m): BULK5-O1, OPEN.

NAMED HYPOTHESES
  M's: H-PULL-IS-COST, H-ONE-MOUTH-SEEN, H-CORRIDOR-HORIZON, H-TWO-SIDED-HORIZON (104); H-RECIPROCAL, H-THREE-HOLDS,
    H-SPLIT-AT-P2 (106); H-DEFINITION-MINUS-MASS (107, 108); H-README-AS-NEEDED (108); H-HORIZON-NEEDS-OBJECT (109);
    H-ENERGY-INTO-P2 (110); H-BUILD-IS-CLOSING-ENERGY, H-ONE-ENERGY-TWO-SIDES (111); H-SEPARATE-UNIVERSES (101.5);
    H-READING-ONLY (86.1).
  The board's: H-BK-CORRIDOR (a static 4D brane metric; your "transit phase through a dimension" is a bulk throat);
    H-HORIZON-HOLDS, H-STRONG-BOUND; R-RECIPROCAL-AS-PRODUCT; H-QUASISTATIC; H-TFD-MODEL (one energy modelled by the
    thermofield double); H-ASYMPTOTIC-FLAT-ENDS (boundary); H-SCHWARZSCHILD-REMNANT, H-SM-ONLY (the withdrawn hold's
    figures); H-RS1.

HISTORY (verifiers, 2026-10-06; first-written claims kept in PLANE.md)
  First pass: BK pages; "positive energy at its neck"; P8 a restatement; ADM unnamed; z3 one-line algebra; restatement
  checks; the control mislabelled; the 5D caveat; H-QUASISTATIC; the trajectories' share; traversability; Higgs wording.
  Second pass: the P2 and P4 checks were tautological (now STRUCTURAL); "the pull is the horizon's own mass" -- it is the
  area-mass, the horizon's Komar charge is less; P2 omitted r0 in (0.75, 1) r_min and the ADM range; "the floor was
  always a horizon" over-read; the Penrose premises were unnamed; "crossing ruled out" was wrong -- the passage is
  one-way 1 -> 2; the window's extension was attributed to BK; T assumed Schwarzschild; the evaporation time is now READ
  (~7.8e-21 s, not 1.6e-18 s); P3 superseded by item 106; the reciprocal as a product is the board's gloss; item 106 was
  not quoted in full; wall 13 "closed" was too strong; the energy bookkeeping was omitted; one digit (3.207837767e16).

USAGE
    python3 plane.py | --selftest | --json
"""

import contextlib
import importlib.util
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
_CACHE = {}

BK_READ = {
    "source": "Bronnikov & Kim, 'Possible wormholes in a brane world', gr-qc/0212112v1",
    "route": "arXiv PDF via Firecrawl and alphaXiv (verifiers), 2026-10-06",
    "eq_13": "p.3",
    "eq_17": "p.4: ds^2 = (1 - 2m/r) dt^2 - (1 - 3m/(2r)) dr^2 / ((1 - 2m/r)(1 - r0/r)) - r^2 dOmega^2",
    "range": "p.4: 'This is evidently a symmetric wormhole geometry for any r0 > 2m >= 0, or for any r0 > 0 in case "
             "m < 0. The Schwarzschild metric is restored from (17) in the special case r0 = 3m/2.'",
    "horizon_case": "p.4: 'If eta > 0, the solution describes a nonsingular black hole with a wormhole throat at r = r0 "
                    "inside the horizon, in other words, a non-traversable wormhole [33]' (eta = r0 - 3m/2, framed for "
                    "r0 close to 3m/2)",
    "eq_18": "p.4: rho = m (r0 - 3m/2) / (2 r^2 (r - 3m/2)^2)",
    "p1": "'E_mu nu does not necessarily satisfy the energy conditions'",
    "p2": "'a restriction can quite probably appear from 5-dimensional geometry'",
    "p6": "'a complete model requires knowledge of the full 5-dimensional space-time'",
}
VERIFIER_READ = {
    "simpson_visser": "1812.07114v3 p.3 'A regular black hole geometry with a one-way spacelike throat ... a bounce into "
                      "a future incarnation of the universe'; pp.4-5 'a bounce into a separate copy of our own universe'; "
                      "p.11 eq. 6.5 T_H = T_H,Sch sqrt(1 - a^2/(2m)^2)",
    "carr_et_al": "2002.12778v2 p.9 eq. 12 dM10/dt = -5.34e-5 f(M) M10^-2 s^-1; p.10 f = 15.35 for the Standard Model up "
                  "to 1 TeV, eq. 14 tau ~ 407 (f(M)/15.35)^-1 M10^3 s",
    "madler_winicour": "1609.01731v3 p.16 eq. 61: 'if there is news, then its Bondi mass must decrease. If there is no "
                       "news ... the Bondi mass is constant.'",
    "bray": "math/9911173v1: Riemannian positive mass eq. 5 p.4; Penrose inequality eq. 6 p.4, Thm 1 p.8; ADM Def. 21 p.54",
}


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def owners():
    """Imported, never copied: chain.py (floor, constants, trips), escape.py (R = 0), pair.py (Hawking T), higgs.py
    (m_h), geometry.py (the thermofield double), stockdest.py (the 70 kg payload)."""
    if not _CACHE:
        _CACHE["chain"] = _load(os.path.join(HERE, "chain.py"), "copy_chain_plane")
        _CACHE["escape"] = _load(os.path.join(D68, "bulk", "escape.py"), "d68_escape_plane")
        _CACHE["pair"] = _load(os.path.join(WD, "pair.py"), "wd_pair_plane")
        _CACHE["higgs"] = _load(os.path.join(WD, "higgs.py"), "wd_higgs_plane")
        _CACHE["geometry"] = _load(os.path.join(D68, "geometry.py"), "d68_geometry_plane")
        _CACHE["stockdest"] = _load(os.path.join(HERE, "stockdest.py"), "copy_stockdest_plane")
    return _CACHE


def bk_masses():
    """Eq. (17), geometric units: ADM, Komar at infinity, Misner-Sharp at the throat and horizon, eq. (18)'s rho check,
    the Penrose gap, the light-bending mass, the horizon's own Komar charge kappa A/4pi, and the x-form dx^2 coefficient."""
    import sympy as sp
    r, r0 = sp.symbols("r r0", positive=True)
    m = sp.symbols("m", real=True)
    u, x = sp.symbols("u x", real=True)
    grr = (1 - sp.Rational(3, 2) * m / r) / ((1 - 2 * m / r) * (1 - r0 / r))
    gtt = 1 - 2 * m / r
    M_adm = sp.simplify(sp.expand(sp.series(grr.subs(r, 1 / u), u, 0, 2).removeO()).coeff(u, 1) / 2)
    M_k = sp.simplify(-sp.expand(gtt.subs(r, 1 / u)).coeff(u, 1) / 2)
    ms = sp.simplify((r / 2) * (1 - 1 / grr))
    rho = m * (r0 - sp.Rational(3, 2) * m) / (2 * r ** 2 * (r - sp.Rational(3, 2) * m) ** 2)
    # surface gravity at r = 2m for ds^2 = f dt^2 - g dr^2: kappa = f' / (2 sqrt(f g)) at the horizon
    fg = sp.simplify(gtt * grr)
    kappa = sp.simplify((sp.diff(gtt, r) / (2 * sp.sqrt(fg))).subs(r, 2 * m))
    komar_h = sp.simplify(kappa * (2 * m) ** 2)
    # x-form: r = r0 + x^2, dr^2 = 4 x^2 dx^2 = 4 (r - r0) dx^2
    cxx = sp.simplify((grr * 4 * (r - r0)).subs(r, r0 + x ** 2))
    return {
        "M_adm": M_adm, "M_komar": M_k, "MS": ms,
        "MS_throat": sp.simplify(ms.subs(r, r0)), "MS_horizon": sp.simplify(ms.subs(r, 2 * m)),
        "dMS_minus_rho": sp.simplify(sp.diff(ms, r) - r ** 2 * rho / 2),
        "penrose_gap": sp.simplify(M_adm - ms.subs(r, 2 * m)),
        "M_light": sp.simplify((M_k + M_adm) / 2),
        "m_zero_adm": sp.solve(sp.Eq(M_adm, 0), m),
        "rho_at_minus2r0": sp.simplify(rho.subs(m, -2 * r0)),
        "rho_negative_form": sp.simplify(rho.subs(m, -2 * r0) + 4 * r0 ** 2 / (r ** 2 * (r + 3 * r0) ** 2)) == 0,
        "kappa": kappa, "komar_horizon": komar_h, "cxx": cxx,
        "syms": (r, r0, m, x),
    }


def horizon_member(m_over_r0):
    """For r0 = 1: a horizon outside the throat (g_tt changes sign on (r0, 3 r0]) and no singular radius outside it."""
    r0, m = 1.0, m_over_r0
    sign_change, num_ok, prev = False, True, None
    for i in range(1, 30001):
        r = r0 + 2.0 * i / 30000
        gtt = 1 - 2 * m / r
        if prev is not None and (gtt > 0) != (prev > 0):
            sign_change = True
        prev = gtt
        num_ok &= (1 - 1.5 * m / r) > 0
    return {"horizon_outside_throat": sign_change, "no_singularity_outside": num_ok}


def one_energy_tfd(d=6, beta=0.7):
    """H-TFD-MODEL: in geometry.tfd (|psi> = sum_i e^{-beta E_i/2} |i>|i>, E_i = i) the variance of H_left - H_right, and
    in the product state rho_L x rho_R with the same marginals (the control)."""
    import numpy as np
    geo = owners()["geometry"]
    psi = geo.tfd(d, beta)
    H = np.diag(np.arange(d, dtype=float))
    I = np.eye(d)
    D = np.kron(H, I) - np.kron(I, H)
    rho = np.outer(psi, psi.conj())
    var_tfd = float(np.real(np.trace(rho @ D @ D)) - np.real(np.trace(rho @ D)) ** 2)
    p = np.abs(psi.reshape(d, d).diagonal()) ** 2
    rl = np.diag(p)
    rho_prod = np.kron(rl, rl)
    var_prod = float(np.real(np.trace(rho_prod @ D @ D)) - np.real(np.trace(rho_prod @ D)) ** 2)
    var_side = float(np.sum(p * np.arange(d) ** 2) - np.sum(p * np.arange(d)) ** 2)
    return {"var_diff_tfd": var_tfd, "var_diff_product": var_prod, "var_one_side": var_side}


def closing_remnant(E_J):
    """The withdrawn H-HOLD-PERSISTS's figures (boundary): mass, Schwarzschild Hawking T (pair.py, an upper bound for a
    BK member), k_B T against m_h (higgs.py), and Carr et al.'s Standard Model lifetime (READ by a verifier)."""
    o = owners()
    pr, hg = o["pair"], o["higgs"]
    M = E_J / pr.C ** 2
    T = pr.hawking_temperature(M)
    kT_GeV = pr.KB * T / (pr.E_CHARGE * 1e9)
    M10 = M * 1e3 / 1e10
    return {"M_kg": M, "T_Sch_K": T, "kT_GeV": kT_GeV, "kT_over_mh": kT_GeV / hg.M_HIGGS, "m_h_GeV": hg.M_HIGGS,
            "tau_SM_s": 407.0 * M10 ** 3, "tau_photon_only_s": 5120 * math.pi * pr.G ** 2 * M ** 3 / (pr.HBAR * pr.C ** 4)}


def compute():
    import sympy as sp
    o = owners()
    ch, esc, sd = o["chain"], o["escape"], o["stockdest"]
    bk = bk_masses()
    r, r0, m, x = bk["syms"]
    co = ch.coefficients()
    uses = ch.owners()["uses"]
    seat, fa = uses.owners()[0], uses.owners()[1]
    core = fa.identity_core()["total_bits"]
    snap = fa._measure()["grid_0p1A"]
    fl, fs = ch.corridor_floor(core), ch.corridor_floor(snap)
    c2 = seat.C ** 2
    c4G = seat.C ** 4 / seat.G
    rmin = fl["r_m"]
    M_obj = sd.PAYLOAD_KG
    # N* = 8 pi^2 G M^2 / (h c ln2), from the owners' constants (M-COEFF: h, c exact; G measured)
    h = ch.owners()["cosmo"]._HBAR * 2 * math.pi
    nstar_per_kg2 = 8 * math.pi ** 2 * seat.G / (h * seat.C * math.log(2))
    nstar = nstar_per_kg2 * M_obj ** 2
    fl_star = ch.corridor_floor(nstar)
    with contextlib.redirect_stdout(io.StringIO()):
        throats = esc.bk_throats()
        trip01 = uses.trip_energy(0.1)
    emin = co["E_min_J_per_sqrt_bit"]["value"]
    m_zero = float(bk["m_zero_adm"][0].subs(r0, rmin))
    cxx = bk["cxx"]
    return {
        "bk_read": BK_READ, "verifier_read": VERIFIER_READ,
        "M_adm": str(bk["M_adm"]), "M_komar": str(bk["M_komar"]), "MS_throat": str(bk["MS_throat"]),
        "MS_horizon": str(bk["MS_horizon"]), "dMS_minus_rho": str(bk["dMS_minus_rho"]),
        "penrose_gap": str(bk["penrose_gap"]), "M_light": str(bk["M_light"]),
        "m_zero_adm": [str(z) for z in bk["m_zero_adm"]], "rho_at_minus2r0": str(bk["rho_at_minus2r0"]),
        "rho_negative_form": bool(bk["rho_negative_form"]),
        "komar_horizon": str(bk["komar_horizon"]),
        "komar_horizon_at_1p8": float(bk["komar_horizon"].subs({m: 1, r0: 1.8})),
        "cxx_x0_m1_r1p8": float(cxx.subs({x: 0, m: 1, r0: 1.8})),
        "cxx_x0_m0p4_r1": float(cxx.subs({x: 0, m: 0.4, r0: 1.0})),
        "member_0p6": horizon_member(0.6), "member_0p4": horizon_member(0.4), "member_0p7": horizon_member(0.7),
        "bk_R": [str(t[0]) for t in throats],
        "tfd": one_energy_tfd(),
        "core_bits": core, "snap_bits": snap, "r_min_core_m": rmin, "floor_core_J": fl["E_J"],
        "E_min_per_sqrt_bit_J": emin, "u_r_G": co["E_min_J_per_sqrt_bit"]["u_r"],
        "pull_horizon_holds_core_J": float(bk["M_komar"].subs(m, rmin / 2)) * c4G,
        "adm_range_at_floor": (float(bk["M_adm"].subs({m: rmin / 2, r0: 0.75 * rmin})) * c4G / fl["E_J"],
                               float(bk["M_adm"].subs({m: rmin / 2, r0: rmin})) * c4G / fl["E_J"]),
        "bekenstein_product_per_bit_Jm": co["bekenstein_J_m_per_bit"]["value"],
        "E_times_r_core_Jm": fl["E_J"] * fl["r_m"],
        "trip_0p1c_J": trip01,
        "zero_member": {"adm_J": float(bk["M_adm"].subs({m: m_zero, r0: rmin})) * c4G, "pull_J": m_zero * c4G,
                        "light_J": float(bk["M_light"].subs({m: m_zero, r0: rmin})) * c4G},
        "payload_kg": M_obj, "carried_core_kg": fl["E_J"] / c2, "carried_snap_kg": fs["E_J"] / c2,
        "apparent_core_kg": fl["E_J"] / c2 - M_obj, "apparent_snap_kg": fs["E_J"] / c2 - M_obj,
        "nstar_per_kg2": nstar_per_kg2, "nstar": nstar, "floor_at_nstar_J": fl_star["E_J"], "Mc2_J": M_obj * c2,
        "remnant": closing_remnant(fl["E_J"]),
        "c4_over_G_J_per_m": c4G,
    }


def report(d):
    print("plane.py -- items 101-111: the corridor in Bronnikov-Kim's family")
    print("BK eq. (17) (READ, p.4): %s" % d["bk_read"]["range"])
    print("  pull (Komar, infinity) = %s = MS at the horizon (%s); the horizon's own Komar charge = %s; ADM = %s" % (
        d["M_komar"], d["MS_horizon"], d["komar_horizon"], d["M_adm"]))
    print("  one-way: x-form dx^2 coefficient at x = 0: %.4f (m = 1, r0 = 1.8: x timelike); %.4f (m = 0.4, r0 = 1)" % (
        d["cxx_x0_m1_r1p8"], d["cxx_x0_m0p4_r1"]))
    print("  least pull (horizon holds, core): %.9e J; ADM at that m between %.4f and %.4f of it" % (
        d["pull_horizon_holds_core_J"], d["adm_range_at_floor"][0], d["adm_range_at_floor"][1]))
    t = d["tfd"]
    print("  one energy (thermofield double): var(H_L - H_R) = %.3e; product state %.4f; one side %.4f" % (
        t["var_diff_tfd"], t["var_diff_product"], t["var_one_side"]))
    print("  README against its object (%.0f kg): core carries %.7f kg -> apparent %.4f kg; snapshot carries %.4e kg" % (
        d["payload_kg"], d["carried_core_kg"], d["apparent_core_kg"], d["carried_snap_kg"]))
    print("  N* = 8 pi^2 G M^2/(h c ln2) = %.9e bits/kg^2 x M^2 = %.9e bits; floor there %.9e J vs Mc^2 %.9e J" % (
        d["nstar_per_kg2"], d["nstar"], d["floor_at_nstar_J"], d["Mc2_J"]))
    rm = d["remnant"]
    print("  boundary (withdrawn H-HOLD-PERSISTS): %.4e kg, T <= %.4e K, tau ~ %.2e s (SM, READ) vs %.2e s photon-only" %
          (rm["M_kg"], rm["T_Sch_K"], rm["tau_SM_s"], rm["tau_photon_only_s"]))


def selftest(d):
    n_pass = n_fail = n_ctl = n_con = 0
    structural = []

    def chk(label, ok, ctl=False, contrast=False):
        nonlocal n_pass, n_fail, n_ctl, n_con
        tag = "CONTROL: " if ctl else ("CONTRAST: " if contrast else "")
        print("  %s %s%s" % ("ok  " if ok else "FAIL", tag, label))
        n_pass += bool(ok)
        n_fail += not ok
        n_ctl += bool(ctl)
        n_con += bool(contrast)

    import sympy as sp
    r0s, ms = sp.Symbol("r0", positive=True), sp.Symbol("m", real=True)
    S = lambda e: sp.sympify(e, locals={"m": ms, "r0": r0s})
    chk("the pull (Komar at infinity) is m and equals the horizon's area-mass, Misner-Sharp at r = 2m (sympy: %s, %s)" % (
        d["M_komar"], d["MS_horizon"]),
        sp.simplify(S(d["M_komar"]) - ms) == 0 and sp.simplify(S(d["MS_horizon"]) - ms) == 0)
    chk("ADM = m/4 + r0/2 and the throat's area-mass r0/2 (sympy: %s, %s)" % (d["M_adm"], d["MS_throat"]),
        sp.simplify(S(d["M_adm"]) - (ms / 4 + r0s / 2)) == 0 and sp.simplify(S(d["MS_throat"]) - r0s / 2) == 0)
    chk("dMS/dr = r^2 rho / 2 with BK's eq. (18) (READ): residual %s" % d["dMS_minus_rho"], d["dMS_minus_rho"] == "0")
    chk("P2: the horizon's own Komar charge kappa A/4pi = %s is below the pull m (0.63 m at r0 = 1.8 m: %.4f)" % (
        d["komar_horizon"], d["komar_horizon_at_1p8"]), 0 < d["komar_horizon_at_1p8"] < 1)
    m6, m4, m7 = d["member_0p6"], d["member_0p4"], d["member_0p7"]
    chk("P1: m = 0.6 r0 has a horizon outside the throat and no singular radius outside it",
        m6["horizon_outside_throat"] and m6["no_singularity_outside"])
    chk("m = 0.4 r0 has no horizon outside the throat", not m4["horizon_outside_throat"], ctl=True)
    chk("m = 0.7 r0 puts the singular radius outside the throat", not m7["no_singularity_outside"], contrast=True)
    chk("P1: between the horizons x is timelike (dx^2 coefficient %.4f < 0 at x = 0, m = 1, r0 = 1.8): one-way passage" %
        d["cxx_x0_m1_r1p8"], d["cxx_x0_m1_r1p8"] < 0)
    chk("an ordinary throat (r0 > 2m: m = 0.4, r0 = 1) keeps x spacelike (coefficient %.4f > 0)" % d["cxx_x0_m0p4_r1"],
        d["cxx_x0_m0p4_r1"] > 0, ctl=True)
    chk("eqs. (13) and (17) have R = 0 (escape.bk_throats, imported: %s)" % d["bk_R"], d["bk_R"] == ["0", "0"])
    t = d["tfd"]
    chk("P6: one energy read from two sides -- in the thermofield double var(H_L - H_R) = %.2e while each side varies "
        "(%.4f)" % (t["var_diff_tfd"], t["var_one_side"]), t["var_diff_tfd"] < 1e-12 and t["var_one_side"] > 0.1)
    chk("in the product state with the same marginals the two readings are independent: var(H_L - H_R) = %.4f = 2 x one "
        "side" % t["var_diff_product"], abs(t["var_diff_product"] - 2 * t["var_one_side"]) < 1e-9 and
        t["var_diff_product"] > 0.1, ctl=True)
    chk("P7: the core README appears negative against its %.0f kg object (%.4f kg) and the largest snapshot positive "
        "(%.4e kg)" % (d["payload_kg"], d["apparent_core_kg"], d["apparent_snap_kg"]),
        d["apparent_core_kg"] < 0 < d["apparent_snap_kg"])
    chk("P7: the bisected floor at N* = %.9e bits equals Mc^2 (%.9e J vs %.9e J): the closed form N* = 8 pi^2 G M^2/"
        "(h c ln2) holds" % (d["nstar"], d["floor_at_nstar_J"], d["Mc2_J"]),
        abs(d["floor_at_nstar_J"] / d["Mc2_J"] - 1) < 1e-9)
    chk("P5 (boundary): the ADM total vanishes only at m = -2 r0 (%s), where eq. (18)'s density is negative everywhere" % (
        d["m_zero_adm"]), d["m_zero_adm"] == ["-2*r0"] and d["rho_negative_form"])
    structural.append("P2: with the horizon holding, the least pull equals the floor (%.9e J vs %.9e J) -- by "
                      "construction, 2m = r_min (first counted)" % (d["pull_horizon_holds_core_J"], d["floor_core_J"]))
    structural.append("P2: at m = r_min/2 the throat lies in (0.75, 1) r_min and the ADM total reads %.4f to %.4f of the "
                      "floor" % d["adm_range_at_floor"])
    structural.append("P4: ADM - MS(2m) = %s > 0 iff r0 > 3m/2 -- one line of algebra (first counted)" % d["penrose_gap"])
    structural.append("P5: E x r at the floor = %.9e J m = N x %.9e J m/bit -- by construction (Bekenstein saturated)" % (
        d["E_times_r_core_Jm"], d["bekenstein_product_per_bit_Jm"]))
    z = d["zero_member"]
    structural.append("P5 boundary: at m = -2 r0 pull %.6e J, light %.6e J, ADM %.1e J" % (z["pull_J"], z["light_J"],
                                                                                         z["adm_J"]))
    rm = d["remnant"]
    structural.append("withdrawn H-HOLD-PERSISTS (item 109): %.6e kg, T_Sch %.6e K (upper bound for a BK member), k_B T = "
                      "%.4e GeV = %.3e m_h; tau ~ %.2e s (Carr et al., SM, READ by a verifier) vs %.2e s photon-only" % (
                          rm["M_kg"], rm["T_Sch_K"], rm["kT_GeV"], rm["kT_over_mh"], rm["tau_SM_s"],
                          rm["tau_photon_only_s"]))
    structural.append("P3 superseded by item 106 (the bits on horizons); its window was (1, 4/3) x the floor; the 0.1 c "
                      "trip %.6e J" % d["trip_0p1c_J"])
    structural.append("H-QUASISTATIC: the opening and closing holds have no static member; a Komar pull needs a Killing "
                      "vector")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("plane.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, n_con, len(structural)))
    return n_fail == 0


def main(argv):
    d = compute()
    if "--json" in argv:
        print(json.dumps(d, indent=1, default=str))
        return 0
    if "--selftest" in argv:
        return 0 if selftest(d) else 1
    report(d)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
