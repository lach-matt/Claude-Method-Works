#!/usr/bin/env python3
"""plane.py -- DOCKET 68, M-RULINGS items 101, 102 and 104: the corridor's cost as the pull our plane reads, with the
corridor's two-sided horizon, and the inverse of a mass.  Deduced, computed and READ; its first form verified once
(findings applied, History), the item-104 rework not yet verified; not seated.  Write-up: PLANE.md.  First headed "...items 101 and 102 ...; not verified".

M's words (verbatim in the rulings file): item 101 "11 - total our plane can read"; item 104(b), choosing the pull:
"observers at position 1 can only see the mouth at position 1. The corridor interior and position 2 are not observable
until the horizon of the corridor is crossed, at which point position is no longer observable... Horizons have 2
sides"; item 102 "a information definition of a physical/geometric object is negative mass, because it is the inverse
definition of a positive mass", item 104(a) "leaning towards 1 [the negative], but it could be 2 [the reciprocal]".

THE GEOMETRY (H-BK-CORRIDOR).  Bronnikov-Kim's eq. (17), gr-qc/0212112v1 p.4 (READ): ds^2 = (1 - 2m/r) dt^2 -
(1 - 3m/2r) dr^2 / ((1 - 2m/r)(1 - r0/r)) - r^2 dOmega^2, "a symmetric wormhole geometry for any r0 > 2m >= 0, or for any
r0 > 0 in case m < 0"; and, citing Casadio-Fabbri-Mazzacurati [33], for 3m/2 < r0 < 2m "a nonsingular black hole with
a wormhole throat at r = r0 inside the horizon, in other words, a non-traversable wormhole" (p.4).  It is symmetric: a
horizon at r = 2m on each side.  Eq. (18) p.4: rho = m (r0 - 3m/2) / (2 r^2 (r - 3m/2)^2).

WHAT FOLLOWS THE WORK (item 82: lead with what passes)
  P1 YOUR CORRIDOR, AS YOU DESCRIBE IT, IS IN THE FAMILY.  The members with a horizon outside the throat and no
     singularity are exactly r0/2 < m < 2 r0/3 (horizon 2m > r0; singular radius 3m/2 < r0; checked numerically, with a
     control and a contrast).  Each has a horizon on each side (eq. 17 is symmetric): an observer at position 1 sees
     only the mouth on that side, the interior lies behind the horizon, and the wormhole is non-traversable (BK p.4)
     -- your H-ONE-MOUTH-SEEN, H-CORRIDOR-HORIZON and H-TWO-SIDED-HORIZON.
  P2 THE PULL IS THE HORIZON'S OWN MASS, AND ITS FLOOR IS THE SQRT(N) FLOOR.  The pull our plane reads (Komar, the 1/r
     coefficient of g_tt) is m; the Misner-Sharp mass at the horizon r = 2m is also m (sympy).  If the README is held at
     the horizon -- the surface position 1 sees (H-HORIZON-HOLDS) -- the least horizon has radius r_min(N), so the least
     pull is m = r_min/2: E_pull = r_min c^4 / (2G) = sqrt(N h c^5 ln2 / (8 pi^2 G)) = 4.59404002e8 J x sqrt(N), exactly
     chain.py's floor (the floor was always a horizon: the neck "at its own Schwarzschild radius").  Bekenstein's bound
     with E = the pull and R = the horizon is then met with equality (H-STRONG-BOUND; the BH form, STRUCTURAL).
  P3 IF THE THROAT HOLDS IT INSTEAD, THE PULL IS PINNED BETWEEN THE FLOOR AND 4/3 OF IT.  With r0 = r_min (H-NECK-HOLDS)
     the window r0/2 < m < 2 r0/3 gives 4.59404002e8 J x sqrt(N) < E_pull < 6.12538669e8 J x sqrt(N), exact form
     (1 to 4/3) x sqrt(N h c^5 ln2 / (8 pi^2 G)).  Core README: 2.405878326e16 J to 3.207837768e16 J -- the 0.1 c trip
     (3.169e16 J) lies inside the window.
  P4 THE PENROSE INEQUALITY IS THE FAMILY'S REGULARITY CONDITION.  The plane's ADM total exceeds the horizon's mass,
     m/4 + r0/2 > m, exactly when r0 > 3m/2 (sympy) -- BK's (Casadio's) condition for no singularity.  The Riemannian
     Penrose inequality, ADM >= sqrt(A/16 pi) for non-negative density, equality only for Schwarzschild (Bray,
     math/9911173v1, eq. 6 p.4 and Thm 1 p.8, READ by the verifier via alphaXiv), holds with room: rho > 0 here.
  P5 ITEM 102, BOTH READINGS, AND WHICH MEMBER EACH SELECTS.
     * The reciprocal (your option 2) holds EXACTLY in your horizon corridor: at the floor the energy and the size are
       reciprocal with the README's size as the constant, E_pull x r_horizon = N h c ln2 / (4 pi^2) =
       3.48772679e-27 J m x N (Bekenstein's product, saturated).
     * The negative (your option 1, the one you lean to) holds exactly only in the member with NO horizon, m = -2 r0:
       there the ADM total is zero and, with the Misner-Sharp split (H-MS-SPLIT, the board's choice of quasi-local
       mass), the integrated energy outside the throat is -r0 c^4 / (2G), the negative of the throat's area-mass -- a
       restatement of the zero total, not a second result.  Its pull reads -2 r0 c^4/G and light reads -r0 c^4/G:
       every direct reading is negative ("must appear to contain", item 86.1).  But it has no horizon, so it is not
       the corridor your item 104(b) describes.  Which member you mean is asked.

  P6 YOUR THREE HOLDS (ITEM 106), UNDER H-HORIZON-HOLDS.  Each hold is a horizon at the floor: opening, position 1's
     horizon only (plane 1 reads E_min, plane 2 nothing); realized, both at once -- eq. 17 is symmetric, so both mouths
     carry the same m, and each plane reads E_min; closing, position 2's only.  If the closing hold persists at position
     2 as a horizon of that mass (H-HOLD-PERSISTS), it is a black hole of E_min/c^2 = 0.2677 kg for the core, at a
     Hawking temperature of 4.583e23 K (pair.py): k_B T = 3.95e10 GeV, 3.2e8 times the Higgs mass (higgs.py).  Its
     energy, 2.406e16 J, is then released at position 2 hotter than every Standard Model mass -- a computed bearing on
     your answers 3 & 4 ("newly introduced energy ... triggers a field reaction, such as a higgs field"), not a showing
     of matter assembly.  The photon-only evaporation time, 1.6e-18 s, has no READ owner: NOT READ.

WHAT IS RULED OUT, AS THE BOUNDARY
  * A positive-density member with a total below the throat's area-mass (the Riemannian positive-mass and Penrose
    inequalities, Bray pp.2-4, 8, READ by the verifier): a zero total needs rho < 0 everywhere (eq. 18 at m < 0).
  * A horizon member with m >= 2 r0/3: the singular radius 3m/2 lies outside the throat (contrast).
  * Crossing to position 2's exterior: the horizon members are non-traversable (BK p.4).  The README's presence at
    position 2 needs the step from bridge to your corridor -- wall 9, OPEN.
  * BK p.2: "a restriction can quite probably appear from 5-dimensional geometry" on the throat's size; r_min for the
    core is 4.0e-28 m.  BULK5-O1, OPEN.

NAMED HYPOTHESES
  M's: H-RECIPROCAL, H-THREE-HOLDS, H-SPLIT-AT-P2 (106); H-PULL-IS-COST (104b), H-ONE-MOUTH-SEEN, H-CORRIDOR-HORIZON, H-TWO-SIDED-HORIZON (104b),
    H-INFORMATION-IS-INVERSE-MASS (102, 104a), H-READING-ONLY (86.1), H-DEVICE-SIZES, H-TWELVE-TRAJECTORIES (101.6),
    H-TRAJECTORIES-OPEN (104c), H-DISTANCE-IRRELEVANT (101.7), H-SEPARATE-UNIVERSES (101.5).
  The board's: H-BK-CORRIDOR (the corridor is eq. 17, a static 4D brane metric -- your answer 5's "transit phase through
    a dimension" is a bulk throat, which eq. 17 is not); H-HORIZON-HOLDS / H-NECK-HOLDS (where the README's bits sit --
    the two readings of P2, P3); H-STRONG-BOUND; H-NECK-ENERGY; H-MS-SPLIT; H-TOTAL-IS-ADM (now the boundary: you chose
    the pull); H-RS1 and H-QUASISTATIC (a static family is not a widening process; no dynamics computed); H-HOLD-PERSISTS (the
    closing hold stays a horizon of the same mass at position 2).

HISTORY (verifier, 2026-10-06; first-written claims kept in PLANE.md)
  * BK pages were "p.6" for eqs. 13 and 17 (escape.py's citation): eq. 13 is p.3, eq. 17 and its range p.4 (rulings
    item 105).  "The corridor contains positive energy at its neck": eq. 18 gives rho < 0 everywhere at m = -2 r0; r0/2
    is the throat's area-mass.  P8's "exact additive inverse" restated the zero total and depended on H-MS-SPLIT.
    "A corridor can cost nothing" lacked H-TOTAL-IS-ADM (and M then chose the pull).  The z3 checks were one line of
    algebra each (STRUCTURAL now; the Penrose inequality cited).  Restatement checks were counted.  The control's
    m = 0.6 r0 was "inside the range": it is BK's horizon case.  "No matter on either plane" lacked BK p.2's 5D caveat;
    "making is enlarging ... safe" lacked H-QUASISTATIC; "no more, no less" dropped the trajectories' share; the
    two-sided picture needs traversability; the Higgs wording was a corrected one (ledger D17).

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
    "route": "arXiv PDF via Firecrawl (query, direct quote) and alphaXiv (verifier), 2026-10-06",
    "eq_13": "p.3",
    "eq_17": "p.4: ds^2 = (1 - 2m/r) dt^2 - (1 - 3m/(2r)) dr^2 / ((1 - 2m/r)(1 - r0/r)) - r^2 dOmega^2",
    "range": "p.4: 'This is evidently a symmetric wormhole geometry for any r0 > 2m >= 0, or for any r0 > 0 in case "
             "m < 0. The Schwarzschild metric is restored from (17) in the special case r0 = 3m/2.'",
    "horizon_case": "p.4: 'If eta > 0, the solution describes a nonsingular black hole with a wormhole throat at r = r0 "
                    "inside the horizon, in other words, a non-traversable wormhole [33]' (eta = r0 - 3m/2; r = 2m the "
                    "event horizon)",
    "eq_18": "p.4: rho = m (r0 - 3m/2) / (2 r^2 (r - 3m/2)^2)",
    "p2": "'a restriction can quite probably appear from 5-dimensional geometry'",
    "p6": "'a complete model requires knowledge of the full 5-dimensional space-time'",
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
    """Imported, never copied: chain.py (the floor, its constants, the trip energies via uses), escape.py (R = 0)."""
    if not _CACHE:
        _CACHE["chain"] = _load(os.path.join(HERE, "chain.py"), "copy_chain_plane")
        _CACHE["escape"] = _load(os.path.join(D68, "bulk", "escape.py"), "d68_escape_plane")
        _CACHE["pair"] = _load(os.path.join(WD, "pair.py"), "wd_pair_plane")
        _CACHE["higgs"] = _load(os.path.join(WD, "higgs.py"), "wd_higgs_plane")
    return _CACHE


def bk_masses():
    """Eq. (17), geometric units: ADM (1/r coefficient of g_rr = 1 + 2M/r), Komar (of -g_tt = 1 - 2M/r), the Misner-Sharp
    mass MS(r) = (r/2)(1 - g^rr) at the throat and at the horizon r = 2m, eq. (18)'s rho and dMS/dr - r^2 rho / 2, the
    Penrose comparison ADM - MS(2m), and the light-bending mass (Komar + ADM)/2 (PPN: alpha b = 2(A + B))."""
    import sympy as sp
    r, r0 = sp.symbols("r r0", positive=True)
    m = sp.symbols("m", real=True)
    u = sp.symbols("u", positive=True)
    grr = (1 - sp.Rational(3, 2) * m / r) / ((1 - 2 * m / r) * (1 - r0 / r))
    gtt = 1 - 2 * m / r
    M_adm = sp.simplify(sp.expand(sp.series(grr.subs(r, 1 / u), u, 0, 2).removeO()).coeff(u, 1) / 2)
    M_k = sp.simplify(-sp.expand(gtt.subs(r, 1 / u)).coeff(u, 1) / 2)
    ms = sp.simplify((r / 2) * (1 - 1 / grr))
    rho = m * (r0 - sp.Rational(3, 2) * m) / (2 * r ** 2 * (r - sp.Rational(3, 2) * m) ** 2)
    return {
        "M_adm": M_adm, "M_komar": M_k, "MS": ms,
        "MS_throat": sp.simplify(ms.subs(r, r0)), "MS_horizon": sp.simplify(ms.subs(r, 2 * m)),
        "dMS_minus_rho": sp.simplify(sp.diff(ms, r) - r ** 2 * rho / 2),
        "penrose_gap": sp.simplify(M_adm - ms.subs(r, 2 * m)),
        "M_light": sp.simplify((M_k + M_adm) / 2),
        "m_zero_adm": sp.solve(sp.Eq(M_adm, 0), m),
        "rho_at_minus2r0": sp.simplify(rho.subs(m, -2 * r0)),
        "rho_negative_form": sp.simplify(rho.subs(m, -2 * r0) + 4 * r0 ** 2 / (r ** 2 * (r + 3 * r0) ** 2)) == 0,
        "syms": (r, r0, m),
    }


def horizon_member(m_over_r0):
    """For r0 = 1: is there a horizon outside the throat (2m > r0), and is the singular radius 3m/2 inside the throat
    (3m/2 < r0)?  Scanned numerically on r in (r0, 3 r0]: g_tt changes sign at r = 2m, and 1 - 3m/2r stays > 0."""
    r0 = 1.0
    m = m_over_r0
    sign_change = False
    num_ok = True
    prev = None
    for i in range(1, 30001):
        r = r0 + 2.0 * i / 30000
        gtt = 1 - 2 * m / r
        if prev is not None and (gtt > 0) != (prev > 0):
            sign_change = True
        prev = gtt
        num_ok &= (1 - 1.5 * m / r) > 0
    return {"horizon_outside_throat": sign_change, "no_singularity_outside": num_ok}


def three_holds(E_hold_J):
    """Item 106 (H-THREE-HOLDS) under H-HORIZON-HOLDS and H-PULL-IS-COST: the pull each plane reads at each hold, each
    holding horizon at the floor.  Opening: position 1's horizon only; realized: both (eq. 17 is symmetric, so both
    mouths carry the same m); closing: position 2's only."""
    return {"opening": {"P1": E_hold_J, "P2": 0.0}, "realized": {"P1": E_hold_J, "P2": E_hold_J},
            "closing": {"P1": 0.0, "P2": E_hold_J}}


def closing_horizon(E_hold_J):
    """If the closing hold persists at position 2 as a horizon of the same mass (H-HOLD-PERSISTS): its mass, Hawking
    temperature (pair.hawking_temperature, imported) and k_B T against the Higgs mass (higgs.M_HIGGS, imported).  The
    photon-only evaporation time 5120 pi G^2 M^3 / (hbar c^4) is printed as NOT READ, not counted."""
    o = owners()
    pr, hg = o["pair"], o["higgs"]
    M = E_hold_J / pr.C ** 2
    T = pr.hawking_temperature(M)
    kT_GeV = pr.KB * T / (pr.E_CHARGE * 1e9)
    t_evap = 5120 * math.pi * pr.G ** 2 * M ** 3 / (pr.HBAR * pr.C ** 4)
    return {"M_kg": M, "T_K": T, "kT_GeV": kT_GeV, "m_higgs_GeV": hg.M_HIGGS, "kT_over_mh": kT_GeV / hg.M_HIGGS,
            "t_evap_s_NOT_READ": t_evap, "E_released_J": E_hold_J}


def compute():
    import sympy as sp
    o = owners()
    ch, esc = o["chain"], o["escape"]
    bk = bk_masses()
    r, r0, m = bk["syms"]
    co = ch.coefficients()
    uses = ch.owners()["uses"]
    seat, fa = uses.owners()[0], uses.owners()[1]
    core = fa.identity_core()["total_bits"]
    fl = ch.corridor_floor(core)
    c4G = seat.C ** 4 / seat.G
    rmin = fl["r_m"]
    with contextlib.redirect_stdout(io.StringIO()):
        throats = esc.bk_throats()
        trip01 = uses.trip_energy(0.1)
    emin = co["E_min_J_per_sqrt_bit"]["value"]
    m_zero = float(bk["m_zero_adm"][0].subs(r0, rmin))
    return {
        "bk_read": BK_READ,
        "M_adm": str(bk["M_adm"]), "M_komar": str(bk["M_komar"]), "MS_throat": str(bk["MS_throat"]),
        "MS_horizon": str(bk["MS_horizon"]), "dMS_minus_rho": str(bk["dMS_minus_rho"]),
        "penrose_gap": str(bk["penrose_gap"]), "M_light": str(bk["M_light"]),
        "m_zero_adm": [str(z) for z in bk["m_zero_adm"]], "rho_at_minus2r0": str(bk["rho_at_minus2r0"]),
        "rho_negative_form": bool(bk["rho_negative_form"]),
        "member_0p6": horizon_member(0.6), "member_0p4": horizon_member(0.4), "member_0p7": horizon_member(0.7),
        "bk_R": [str(t[0]) for t in throats],
        "core_bits": core, "r_min_core_m": rmin, "floor_core_J": fl["E_J"],
        "E_min_per_sqrt_bit_J": emin, "u_r_G": co["E_min_J_per_sqrt_bit"]["u_r"],
        "pull_window_per_sqrt_bit_J": (emin, 4.0 / 3.0 * emin),
        "pull_window_core_J": (float(bk["M_komar"].subs(m, rmin / 2)) * c4G,
                               float(bk["M_komar"].subs(m, 2 * rmin / 3)) * c4G),
        "pull_horizon_holds_core_J": float(bk["M_komar"].subs(m, rmin / 2)) * c4G,
        "bekenstein_product_per_bit_Jm": co["bekenstein_J_m_per_bit"]["value"],
        "E_times_r_core_Jm": fl["E_J"] * fl["r_m"],
        "trip_0p1c_J": trip01,
        "zero_member": {"m_over_r0": -2, "adm_J": float(bk["M_adm"].subs({m: m_zero, r0: rmin})) * c4G,
                        "pull_J": m_zero * c4G, "light_J": float(bk["M_light"].subs({m: m_zero, r0: rmin})) * c4G,
                        "throat_area_mass_J": float(bk["MS_throat"].subs(r0, rmin)) * c4G},
        "c4_over_G_J_per_m": c4G,
        "three_holds_core_J": three_holds(fl["E_J"]),
        "closing_core": closing_horizon(fl["E_J"]),
    }


def report(d):
    print("plane.py -- items 101, 102, 104: the pull as the cost, the two-sided horizon, the inverse of a mass")
    print("Bronnikov-Kim eq. (17) (READ, p.4): %s" % d["bk_read"]["range"])
    print("  %s" % d["bk_read"]["horizon_case"])
    print("  pull (Komar) = %s; Misner-Sharp at the horizon r = 2m = %s; at the throat = %s; ADM = %s" % (
        d["M_komar"], d["MS_horizon"], d["MS_throat"], d["M_adm"]))
    print("  Penrose gap ADM - MS(2m) = %s  (> 0 iff r0 > 3m/2, BK's no-singularity condition)" % d["penrose_gap"])
    lo, hi = d["pull_window_per_sqrt_bit_J"]
    print("  horizon members r0/2 < m < 2r0/3; with r0 = r_min(N): %.9e < E_pull / sqrt(N) < %.9e J" % (lo, hi))
    print("  core README (%.6e bits): pull %.9e J (horizon holds) ... window %.9e to %.9e J (throat holds); 0.1 c trip "
          "%.4e J" % (d["core_bits"], d["pull_horizon_holds_core_J"], d["pull_window_core_J"][0],
                      d["pull_window_core_J"][1], d["trip_0p1c_J"]))
    print("  item 102 reciprocal: E x r at the floor = %.9e J m = %.9e J m/bit x N" % (
        d["E_times_r_core_Jm"], d["bekenstein_product_per_bit_Jm"]))
    z = d["zero_member"]
    print("  item 102 negative (boundary, no horizon): m = -2 r0: ADM %.3e J, pull %.6e J, light %.6e J, throat "
          "area-mass %.6e J" % (z["adm_J"], z["pull_J"], z["light_J"], z["throat_area_mass_J"]))


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
    chk("eq. (17)'s pull (Komar) is m and the Misner-Sharp mass at the horizon r = 2m is m (sympy: %s, %s): the pull is "
        "the horizon's mass" % (d["M_komar"], d["MS_horizon"]),
        sp.simplify(S(d["M_komar"]) - ms) == 0 and sp.simplify(S(d["MS_horizon"]) - ms) == 0)
    chk("eq. (17)'s ADM total is m/4 + r0/2 and the throat's Misner-Sharp mass is r0/2 (sympy: %s, %s)" % (
        d["M_adm"], d["MS_throat"]),
        sp.simplify(S(d["M_adm"]) - (ms / 4 + r0s / 2)) == 0 and sp.simplify(S(d["MS_throat"]) - r0s / 2) == 0)
    chk("dMS/dr = r^2 rho / 2 with BK's eq. (18) rho (READ p.4): the derived masses agree with the printed density "
        "(residual %s)" % d["dMS_minus_rho"], d["dMS_minus_rho"] == "0")
    gap = S(d["penrose_gap"])
    chk("P4: ADM exceeds the horizon's mass exactly when r0 > 3m/2 (gap %s; sign at m = 0.6 r0: +, at m = 0.7 r0: -) -- "
        "the Penrose inequality is BK's no-singularity condition" % d["penrose_gap"],
        sp.simplify(gap - (r0s / 2 - 3 * ms / 4)) == 0 and gap.subs({ms: 0.6, r0s: 1}) > 0 and
        gap.subs({ms: 0.7, r0s: 1}) < 0)
    m6, m4, m7 = d["member_0p6"], d["member_0p4"], d["member_0p7"]
    chk("P1: m = 0.6 r0 has a horizon outside the throat and no singular radius outside it (your corridor's kind)",
        m6["horizon_outside_throat"] and m6["no_singularity_outside"])
    chk("m = 0.4 r0 (2m < r0) has no horizon outside the throat", not m4["horizon_outside_throat"], ctl=True)
    chk("m = 0.7 r0 (> 2r0/3) puts the singular radius 3m/2 outside the throat", not m7["no_singularity_outside"],
        contrast=True)
    chk("eqs. (13) and (17) have R = 0 (escape.bk_throats, imported: %s)" % d["bk_R"], d["bk_R"] == ["0", "0"])
    lo, hi = d["pull_window_core_J"]
    chk("P3: with the throat holding the core README the pull lies in (%.9e, %.9e) J, and the 0.1 c trip (%.6e J) falls "
        "inside that window" % (lo, hi, d["trip_0p1c_J"]), lo < d["trip_0p1c_J"] < hi)
    chk("P2: with the horizon holding it the least pull equals chain.py's bisected floor (%.9e J vs %.9e J)" % (
        d["pull_horizon_holds_core_J"], d["floor_core_J"]),
        abs(d["pull_horizon_holds_core_J"] / d["floor_core_J"] - 1) < 1e-9)
    chk("P5 (boundary): the ADM total vanishes only at m = -2 r0 (%s), where BK's eq. (18) density is negative "
        "everywhere (%s)" % (d["m_zero_adm"], d["rho_at_minus2r0"]),
        d["m_zero_adm"] == ["-2*r0"] and d["rho_negative_form"])
    ch_ = d["closing_core"]
    chk("P6 (item 106): if the closing hold persists at position 2 as a horizon of the core's floor mass (%.6e kg), its "
        "Hawking temperature (%.6e K, pair.py) gives k_B T = %.4e GeV, %.3e times the Higgs mass (%.2f GeV, higgs.py)" % (
            ch_["M_kg"], ch_["T_K"], ch_["kT_GeV"], ch_["kT_over_mh"], ch_["m_higgs_GeV"]), ch_["kT_over_mh"] > 1e6)
    h3 = d["three_holds_core_J"]
    structural.append("P6: the three holds' pulls (P1, P2) in J: opening (%.4e, %.0f), realized (%.4e, %.4e), closing "
                      "(%.0f, %.4e) -- the realized hold's equal pair is eq. 17's symmetry (by construction)" % (
                          h3["opening"]["P1"], h3["opening"]["P2"], h3["realized"]["P1"], h3["realized"]["P2"],
                          h3["closing"]["P1"], h3["closing"]["P2"]))
    structural.append("P6: the photon-only evaporation time 5120 pi G^2 M^3/(hbar c^4) = %.3e s -- NOT READ (no owner on "
                      "the board), not counted" % ch_["t_evap_s_NOT_READ"])
    z = d["zero_member"]
    structural.append("P5: at m = -2 r0 the pull reads %.6e J, light %.6e J, the ADM total %.1e J; with H-MS-SPLIT the "
                      "energy outside the throat is %.6e J, the negative of the throat's area-mass -- a restatement of "
                      "the zero total (first counted as P8)" % (z["pull_J"], z["light_J"], z["adm_J"],
                                                                 -z["throat_area_mass_J"]))
    structural.append("P5 reciprocal: E x r at the floor = %.9e J m = N x %.9e J m/bit -- the floor's definition, "
                      "Bekenstein saturated (first written nowhere)" % (d["E_times_r_core_Jm"],
                                                                      d["bekenstein_product_per_bit_Jm"]))
    structural.append("the pull window's ends are r_min/2 and 2 r_min/3 times c^4/G = %.9e J/m (M-COEFF: c^4/G, u_r "
                      "2.2e-5); an error dm off m = -2 r0 costs dm c^4/(4G) = %.9e J per metre" % (
                          d["c4_over_G_J_per_m"], d["c4_over_G_J_per_m"] / 4))
    structural.append("Penrose and positive-mass inequalities: Bray math/9911173v1 eq. 5-6 p.4, Thm 1 p.8 (READ by the "
                      "verifier); the old z3 forms were one line of algebra each (first counted)")
    structural.append("H-QUASISTATIC: a static family in r0 is not a widening process; no dynamics computed")
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
