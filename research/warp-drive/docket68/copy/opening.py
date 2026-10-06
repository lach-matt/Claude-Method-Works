#!/usr/bin/env python3
"""opening.py -- DOCKET 68, M-RULINGS item 113 (second of three): how the corridor opens and closes -- the two holds of
item 106 that no static Bronnikov-Kim member has.  Deduced, computed and READ; verified once (findings applied,
History); not seated.  Write-up: OPENING.md.  First headed "...; not verified; not seated."

M's words (verbatim in the rulings file): item 106 "Three distinct holds in one fluid wave motion, horizon position 1
only as the corridor opens, ... upon the corridor closing the bits are then held only at the horizon of position 2";
item 109 "A horizon cannot exist without the object of which it needs to exist"; item 110 "Into position 2"; item 111
"one energy read from two sides"; item 86 answer 5 "however long is dictated for the travel. I suspect it is incredibly
short, maybe even immeasurable but not zero. And this answer is also a relative one."

THE BOARD'S READING (R-VAIDYA-HOLDS, ungraded).  Each transition is null dust -- radiation moving at light speed, a
"fluid wave": ingoing Vaidya at position 1, ds^2 = -(1 - 2m(v)/r) dv^2 + 2 dv dr + r^2 dOmega^2, m rising 0 -> m_f;
outgoing Vaidya at position 2, -2 du dr, m falling m_f -> 0.  Written here, curvature computed; nothing about it READ.

WHAT FOLLOWS THE WORK (item 82)
  O1 EACH PIECE SATISFIES EVERY POINTWISE ENERGY CONDITION WHEN ITS MASS RUNS YOUR WAY.  Ingoing: the only nonzero
     component of the Einstein tensor is G_vv = 2 m'(v)/r^2; outgoing: G_uu = -2 m'(u)/r^2 (sympy).  T is a rank-one null
     tensor (m'/4 pi r^2) l l, so T(k,k) = (m'/4 pi r^2)(l.k)^2 for EVERY vector k: the null, weak, strong and dominant
     conditions all hold exactly when m rises at the opening and falls at the closing (by the form of T).  Controls:
     the code's Einstein-tensor test fails for charged Vaidya (extra components appear) and its R test fails for
     Vaidya-de Sitter (R = 4 Lambda).
  O2 EACH PIECE HAS R = 0.  Null dust is traceless: R = 0 for both (sympy).  Bronnikov-Kim's corridor has R = 0 too, but
     as brane vacuum (T = 0, E traceless), not traceless matter; across the joins R stays zero only if the junction
     stress is traceless (H-JUNCTION, OPEN).
  O3 THE CORRIDOR ITSELF BREAKS THE NULL ENERGY CONDITION ON BOTH SIDES OF ITS HORIZON -- SO THE JOINS ARE WHERE THAT
     ENTERS.  For eq. (17), G^r_r - G^t_t = -2 (2 r0 - 3m)(r - 2m) / (r^2 (2r - 3m)^2) (sympy): for horizon members
     (2 r0 > 3m) the radial null condition fails at every r != 2m, outside the horizon and inside it (where the
     inequality reverses), though rho > 0.  The Vaidya pieces end in Schwarzschild of mass m_f, not in the corridor, whose
     exterior carries the violating stress out to infinity; reaching the corridor from the opening still needs it.  D7
     (a quantum inequality on negative energy held for a duration) is met trivially by the Vaidya pieces, and is silent
     on your main path anyway (LEDGER M-D68-87).
  O4 THE ENERGY: IN = OUT BY CONSTRUCTION; WHICH MASS IS OPEN.  Both mass functions run between 0 and the same m_f, so the
     opening carries m_f c^4/G in and the closing the same out (by construction).  With m_f = r_min/2 that is the floor,
     4.59404002e8 J x sqrt(N); if the opening must supply the corridor's ADM total instead, up to 5/4 of it (PLANE.md
     point 2; H-MF-IS-AREA-MASS).  Position 2's horizon ends when its m reaches 0 -- imposed by m -> 0, your item 109.
  O5 A FLOOR ON THE OPENING'S DURATION, UNDER A PUBLISHED CONJECTURE.  Barrow & Gibbons 1408.1820v3 p.2 eq. 2 (READ by a
     verifier): "the closely related conjecture that there is a maximum power defined by P_max = cF_max = c^5/4G, the
     so-called Dyson Luminosity ... or some multiple of it to account for geometrical factors O(1)"; p.3 the factor "does
     not seem to be so precisely determined".  Applied to inflow (H-MAX-POWER-INFLOW, the board's extension: the
     conjecture and Cardoso et al. 1803.03271v2 p.3 bound luminosity at future null infinity), dm/dt <= c/4 gives
     tau >= 4 m_f/c = 2 r_min/c = sqrt(2 N h G ln2 / (pi^2 c^5)) = 0.9394372787 t_P sqrt(N) = 5.0647e-44 s x sqrt(N):
     2.652e-36 s for the core; with the Planck luminosity c^5/G instead, r_min/(2c) = 6.631e-37 s -- a factor-4 range.  A
     floor on the opening, beside your answer 5 (the hold itself is "however long is dictated for the travel", and
     relative; tau is advanced time at position 1, H-HOLD-FRAME).  For N of order 1 the bound is below the Planck time
     and the model breaks down.
  O6 THE CLOSING IS NOT BOUNDED BY IT.  Cardoso et al. App. B p.9 (READ by a verifier) treat outgoing Vaidya: "The
     luminosity of this spacetime ... is unbounded ... not a counter-example ... because the radiation comes out of a
     past horizon" -- position 2's closing is that case (a white hole, plane.py P1).
  O7 THE HORIZON HOLDS THE README ONLY AS IT GROWS.  During the opening the apparent horizon r = 2m(v) is spacelike (its
     norm 4 m' dv^2 > 0); under H-HORIZON-HOLDS (the apparent horizon) its capacity is N (m(v)/m_f)^2, so the whole
     README sits on position 1's horizon only at the end of the opening, and at the closing it shrinks as (1 - f)^2 N --
     which forces the reading before it ends (H-SPLIT-AT-P2).

WHAT IS RULED OUT, AS THE BOUNDARY (and the tensions)
  * Position 1 keeps its mass: in this model nothing lowers position 1's m after the opening, so a classical event
    horizon forms there and persists -- against item 106 (at closing, bits on position 2's horizon only) and item 109's
    principle applied to position 1, unless your one-entangled-state accounting (item 111) applies.  OPEN.
  * Position 2 has a white-hole past: outgoing Vaidya with m falling from m_f is, read back, Schwarzschild of mass m_f
    with its past horizon; under per-universe bookkeeping (H-ASYMPTOTIC-FLAT-ENDS) position 2 carried m_f before the
    opening -- against item 109 and item 106.  OPEN.
  * Classical white holes are unstable to infalling matter (Eardley 1974, NOT READ): OPEN.
  * The inflow is the eikonal limit: wavelengths << r_min (3.976e-28 m, core) means quanta >> h c / r_min = 499.6 J each,
    at most about 4.8e13 of them -- a spherically converging emitter around position 1 (wall 9); whether the inflow is
    the README or carries none is unnamed (OPEN).
  * The joins (H-JUNCTION): OPEN.

NAMED HYPOTHESES
  M's: H-THREE-HOLDS (106), H-HORIZON-NEEDS-OBJECT (109), H-ENERGY-INTO-P2 (110), H-ONE-ENERGY-TWO-SIDES (111),
    H-BRIEF-HOLD (86.5).
  The board's: R-VAIDYA-HOLDS; H-MAX-POWER-INFLOW; H-HOLD-FRAME; H-MF-IS-AREA-MASS; H-HORIZON-HOLDS (the apparent horizon),
    H-STRONG-BOUND; H-JUNCTION; H-QUASISTATIC (a Komar pull needs a static geometry); H-ASYMPTOTIC-FLAT-ENDS (against
    H-ONE-ENERGY-TWO-SIDES).

HISTORY (verifier, 2026-10-06; first-written claims kept in OPENING.md)
  Checks 3-6 restated checks 1-2 and their "controls" were the same formula at the other sign (now STRUCTURAL; genuine
  controls added: charged Vaidya, Vaidya-de Sitter); "the only curvature component" (the Einstein tensor's; Weyl is
  nonzero) and the radial-only NEC (it holds in all directions, with WEC, SEC, DEC); "neither transition needs negative
  energy, so D7 does not bind them" omitted that the corridor violates the NEC (now computed); "the whole sequence stays
  in R = 0" needed the junction; "energy in = energy out" was by construction; position 1's kept mass, position 2's
  white-hole past and which mass were omitted; maximum power is READ (Barrow & Gibbons, a conjecture, factor uncertain)
  and bounds the opening only (Cardoso et al.); "your item 86 answer 5, computed" over-read; the capacity schedule and
  the inflow's quanta were omitted.

USAGE
    python3 opening.py | --selftest | --json
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

READ_HERE = {
    "gibbons": "hep-th/0210109v1 (alphaXiv): p.1 'I suggest that classical General Relativity ... incorporates a "
               "Principal of Maximal Tension ... c^4/4G'; p.2 eq. 1 'The tension or force between two bodies cannot "
               "exceed F_g = c^4/4G'",
    "barrow_gibbons": "1408.1820v3 p.2 eq. 2 (a verifier, alphaXiv): 'the closely related conjecture that there is a "
                      "maximum power defined by P_max = cF_max = c^5/4G, the so-called Dyson Luminosity (Dyson, 1963), "
                      "or some multiple of it to account for geometrical factors O(1)'; p.3 'does not seem to be so "
                      "precisely determined at present'",
    "cardoso_et_al": "1803.03271v2 (a verifier, alphaXiv): p.1 'initial conditions which give rise to arbitrarily large "
                     "luminosities'; p.3 conjecture: bounded by the Planck luminosity for spacetimes 'free from past "
                     "horizons'; App. B p.9 outgoing Vaidya 'unbounded ... because the radiation comes out of a past "
                     "horizon'",
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
    if not _CACHE:
        _CACHE["chain"] = _load(os.path.join(HERE, "chain.py"), "copy_chain_open")
    return _CACHE


def _einstein(g, X):
    import sympy as sp
    n = 4
    gi = g.inv()
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.Matrix(n, n, lambda b, c: sp.simplify(sum(
        sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
        + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(n)) for a in range(n))))
    R = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    return sp.simplify(Ric - R * g / 2), R, gi


def vaidya(sign, extra=None):
    """sign = +1 ingoing, -1 outgoing.  extra: None; 'charge' (m -> m - q^2/2r); 'lambda' (m -> m + Lambda r^3/6)."""
    import sympy as sp
    v, r, th, ph = sp.symbols("v r theta phi", positive=True)
    q, L = sp.symbols("q Lambda", positive=True)
    m = sp.Function("m")
    M = m(v)
    if extra == "charge":
        M = M - q ** 2 / (2 * r)
    elif extra == "lambda":
        M = M + L * r ** 3 / 6
    g = sp.Matrix([[-(1 - 2 * M / r), sign, 0, 0], [sign, 0, 0, 0], [0, 0, r ** 2, 0],
                   [0, 0, 0, r ** 2 * sp.sin(th) ** 2]])
    G, R, _ = _einstein(g, [v, r, th, ph])
    others = [(i, j) for i in range(4) for j in range(4) if (i, j) != (0, 0) and sp.simplify(G[i, j]) != 0]
    mp = sp.Symbol("mprime")
    return {"R": str(R), "G00": str(sp.simplify(G[0, 0].subs(sp.Derivative(m(v), v), mp))), "others": others}


def bk_radial_nec():
    """Eq. (17) in (t, r, theta, phi), signature (-+++): G^r_r - G^t_t, the radial null combination."""
    import sympy as sp
    t, r, th, ph = sp.symbols("t r theta phi", positive=True)
    r0, m = sp.symbols("r0 m", positive=True)
    gtt = -(1 - 2 * m / r)
    grr = (1 - sp.Rational(3, 2) * m / r) / ((1 - 2 * m / r) * (1 - r0 / r))
    g = sp.diag(gtt, grr, r ** 2, r ** 2 * sp.sin(th) ** 2)
    G, R, gi = _einstein(g, [t, r, th, ph])
    mixed = gi * G
    comb = sp.factor(sp.simplify(mixed[1, 1] - mixed[0, 0]))
    target = -2 * (2 * r0 - 3 * m) * (r - 2 * m) / (r ** 2 * (2 * r - 3 * m) ** 2)
    out_val = float(comb.subs({m: 1, r0: 1.8, r: 3}))
    in_val = float(comb.subs({m: 1, r0: 1.8, r: 1.9}))
    return {"comb": str(comb), "matches": sp.simplify(comb - target) == 0, "outside_r3": out_val, "inside_r1p9": in_val}


def compute():
    o = owners()
    ch = o["chain"]
    co = ch.coefficients()
    seat, fa = ch.owners()["uses"].owners()[0], ch.owners()["uses"].owners()[1]
    core = fa.identity_core()["total_bits"]
    fl = ch.corridor_floor(core)
    c = seat.C
    h = ch.owners()["cosmo"]._HBAR * 2 * math.pi
    hbar = h / (2 * math.pi)
    t_P = math.sqrt(hbar * seat.G / c ** 5)
    rmin = fl["r_m"]
    ing, out = vaidya(+1), vaidya(-1)
    chg, lam = vaidya(+1, "charge"), vaidya(+1, "lambda")
    return {
        "read_here": READ_HERE,
        "ingoing": ing, "outgoing": out, "charged": chg, "de_sitter": lam, "bk_nec": bk_radial_nec(),
        "core_bits": core, "r_min_core_m": rmin, "E_hold_core_J": fl["E_J"],
        "tau_min_core_s": 2 * rmin / c, "tau_min_per_sqrt_bit_s": 2 * co["r_min_m_per_sqrt_bit"]["value"] / c,
        "tau_over_tP_per_sqrt_bit": 2 * co["r_min_m_per_sqrt_bit"]["value"] / c / t_P,
        "tau_planck_lum_core_s": rmin / (2 * c), "tau_cos_core_s": math.pi * rmin / c,
        "quantum_energy_J": h * c / rmin, "max_quanta": fl["E_J"] / (h * c / rmin),
    }


def report(d):
    print("opening.py -- item 113 (2 of 3): the opening and closing holds as null dust (R-VAIDYA-HOLDS)")
    for k in ("ingoing", "outgoing", "charged", "de_sitter"):
        x = d[k]
        print("  %-9s R = %-12s G_00 = %-18s other components %s" % (k, x["R"], x["G00"], x["others"]))
    b = d["bk_nec"]
    print("  corridor (eq. 17): G^r_r - G^t_t = %s; at m = 1, r0 = 1.8: %.4f (r = 3), %.4f (r = 1.9)" % (
        b["comb"], b["outside_r3"], b["inside_r1p9"]))
    print("  opening floor (H-MAX-POWER-INFLOW): 2 r_min/c = %.10f t_P sqrt(N) = %.6e s x sqrt(N); core %.6e s; Planck "
          "luminosity %.6e s" % (d["tau_over_tP_per_sqrt_bit"], d["tau_min_per_sqrt_bit_s"], d["tau_min_core_s"],
                                 d["tau_planck_lum_core_s"]))
    print("  inflow quanta >> %.4f J each, at most %.3e of them (core)" % (d["quantum_energy_J"], d["max_quanta"]))


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

    ing, out, chg, lam, b = d["ingoing"], d["outgoing"], d["charged"], d["de_sitter"], d["bk_nec"]
    chk("O1: ingoing null dust: G_vv = %s, every other Einstein component zero (sympy)" % ing["G00"],
        ing["G00"] == "2*mprime/r**2" and ing["others"] == [])
    chk("O1: outgoing null dust: G_uu = %s, every other Einstein component zero (sympy)" % out["G00"],
        out["G00"] == "-2*mprime/r**2" and out["others"] == [])
    chk("charged Vaidya (m - q^2/2r) is not pure null dust: other components appear (%s)" % chg["others"],
        chg["others"] != [], ctl=True)
    chk("O2: both pieces have R = 0 (sympy: %s, %s)" % (ing["R"], out["R"]), ing["R"] == "0" and out["R"] == "0")
    chk("Vaidya-de Sitter (m + Lambda r^3/6) has R = %s, not 0" % lam["R"], lam["R"] != "0", ctl=True)
    chk("O3: the corridor's radial null combination is %s (sympy) and is negative outside the horizon (%.4f at r = 3) "
        "and positive inside it (%.4f at r = 1.9), where the inequality reverses -- violated on both sides" % (
            b["comb"], b["outside_r3"], b["inside_r1p9"]),
        b["matches"] and b["outside_r3"] < 0 and b["inside_r1p9"] > 0)
    structural.append("O1: T = (m'/4 pi r^2) l l, so T(k,k) = (m'/4 pi r^2)(l.k)^2 for every k: NEC, WEC, SEC, DEC hold "
                      "iff m' >= 0 ingoing, m' <= 0 outgoing (by the form; first counted as four checks)")
    structural.append("O4: energy in = energy out = m_f c^4/G = %.9e J for the core -- by construction" %
                      d["E_hold_core_J"])
    structural.append("O5: 2 r_min/c = %.10f t_P sqrt(N) = %.9e s x sqrt(N); core %.6e s; with c^5/G %.6e s "
                      "(H-MAX-POWER-INFLOW; Barrow-Gibbons a conjecture, factor O(1))" % (
                          d["tau_over_tP_per_sqrt_bit"], d["tau_min_per_sqrt_bit_s"], d["tau_min_core_s"],
                          d["tau_planck_lum_core_s"]))
    structural.append("O6: the closing is unbounded by the conjecture (a past horizon; Cardoso et al. App. B)")
    structural.append("boundary: inflow quanta >> h c/r_min = %.4f J, at most %.3e (core)" % (
        d["quantum_energy_J"], d["max_quanta"]))
    structural.append("H-JUNCTION, position 1's kept mass, position 2's white-hole past: OPEN")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("opening.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
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
