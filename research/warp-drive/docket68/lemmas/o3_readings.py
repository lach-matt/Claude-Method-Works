#!/usr/bin/env python3
"""o3_readings.py -- M-RULINGS item 159, "test both options": the write inside a standing corridor (reading (i)) and
the write as the opening (reading (ii)), each tested against the bulk.  Computed, READ and deduced; not verified; not
seated.

M's words (verbatim in the rulings file): item 159 "test both options"; item 158 (2) "Exactly as long as the write
needs  I should think"; item 115 (c) "The README itself"; item 127 (1) "yes" (the planes coincide, the extra dimension
included); item 138 (the bulk is multi-universal).

READ
  Gregory & Laflamme, hep-th/9301052: eq. (10), p.7, the s-wave equation for H_tr on Schwarzschild x R; p.7, "the
    regular solution at infinity is e^(-sqrt(Omega^2 + mu^2) r), and the solutions at the horizon behave as
    (r - r+)^(-1 +- r+ Omega/(D-3))"; p.8, the black string is "classically unstable".
  Gregory, hep-th/0004101: p.5, "For GM = 1, the instability exists in the range 0 < m < 0.45, with the most favoured
    instability ... having m ~ 0.2"; pp.6-7, the Randall-Sundrum string is unstable too, the instability accumulating
    towards the AdS horizon; p.7, eq. (11), with a second wall at z_c the instability needs e^(k z_c) >= 2 k G M; p.2,
    the instability extends to charged branes, "the only exception being extremal solutions".
  Lehner & Pretorius, 1006.5960: p.2, string of "mass per unit length M", horizon radius 2.00 M (Table I); p.3,
    "the critical L/R is ~ 7.2"; pp.3-4, the first instability after the seeded one takes T1/M ~ 80, each later one
    X ~ 1/4 of the one before, so the cascade ends at T0 + T1/(1 - X), "the local string segments reach zero radius, and
    the curvature visible to exterior observers diverges" -- "a naked, curvature singularity".

  R1 READING (i): THE WRITE INSIDE A STANDING CORRIDOR (computed, from o3_write.py and b4_static.py).  With eq. (17)
     held on the plane the static bulk is forced in the board's locally analytic class (B4b), and it reaches its
     singular surface by about 18 clocks.  The write needs 2.0e5 clocks at the example README (Z = 108.75); even
     without H-README-ALONE ('t Hooft eq. (8)) 630.  Refuted at the example README, and above about 25 Z bits.  A
     tension besides (deduced): under 115 (c) and H-PULL-IS-COST the corridor's mass is the README's energy, so a
     corridor standing before its README arrives needs that energy to arrive ahead of the bits it carries.
  R2 THE BLACK STRING'S INSTABILITY, COMPUTED (from READ eq. (10)).  GL's eq. (10) at D = 4, transcribed; one sign as
     extracted (the 3 (D-3)^2 x^(2(D-3)) term of the H' coefficient) contradicts GL's stated horizon exponents, and
     placing it outside the bracket restores them exactly (sympy) -- the transcription is fixed by GL's own text.
     Shooting from the horizon's regular branch along a complex detour (the coefficient of H'' vanishes on the real
     axis, an apparent singularity), the growing mode at infinity is cancelled at Omega(mu): unstable for
     0 < mu r+ < ~0.875, fastest Omega r+ = 0.0923 at mu r+ ~ 0.35.  Controls: Lehner-Pretorius's L/R ~ 7.2 is
     mu_c r+ = 0.873; Gregory's GM = 1 range 0 < m < 0.45 and most favoured ~0.2 are mu r+ < 0.9 and ~0.4; two
     integration settings agree to 1e-3.
  R3 READING (ii): THE WRITE AS THE OPENING (computed and deduced).  The board models the opening as ingoing Vaidya
     (opening.py, R-VAIDYA-HOLDS): the plane is Schwarzschild of mass m(v), and b4_static.py's own control shows the
     board's solver returning the black string for Schwarzschild data.  The opening lasts at least 2.0e5 clocks, so
     the mass changes at 1/T ~ 5e-6 per clock against a growth rate Omega_max/(2m) = 0.046 per clock: the string is
     quasi-static and unstable throughout.  Over the opening's last half alone (a linear ramp, H-LINEAR-RAMP) it
     grows by ~4.6e3 e-folds; 230 suffice for any seed down to 1e-100, so a horizon present for 2.5% of the opening is
     enough.  Lehner-Pretorius then end the cascade ~107 m later (T1/(1 - X)) in a naked singularity.  So in the
     board's model, the opening's bulk is not regular: refuted.
  R4 THE ESCAPES, NAMED (deduced; none shown)
     (a) an extremal opening -- Gregory's "only exception": the opening passing through extremal members rather than
         Schwarzschild ones.  Then by B4b's uniqueness the bulk tracks the static extremal bulk with m(v), and the long
         opening's cone reaches its singular surface as in R1.  This escape is not shown to help.
     (b) a wall within the instability's reach -- Gregory's eq. (11): a second wall closer than e^(k z_c) < 2 k G M
         (in the flat limit, about pi/mu_c = 3.6 r+ = 7.2 m) switches it off.  Your 127 puts position 2's plane in the
         same place as position 1's, so it is not that wall; your 138's other planes are candidates.
     (c) leaving the flat limit -- R1's singular surface was computed at ell >> r0; k's scale is B6' (nature's).
         Gregory shows the single-wall Randall-Sundrum string stays unstable, so (c) bears on R1 at most.
  VERDICT  Under the board's models in the flat limit, the bulk does not stay regular through the write on either
     reading.  The routes left run through structure your rulings already name (138's planes; an extremal opening;
     k's scale), and each is B4d's to compute.

Imports lemmas/o3_write.py and lemmas/b4_static.py by path.  numpy, scipy, sympy.  python3 o3_readings.py [--selftest]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
LP_T1, LP_X, LP_CRIT = 80.0, 0.25, 7.2                       # Lehner-Pretorius pp.3-4 (READ)
GREGORY_MC, GREGORY_MMAX = 0.45, 0.2                         # Gregory 2000 p.5, GM = 1 (READ)
SEED_FLOOR = 1e-100


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


_r, _W, _mu = sp.symbols("r Omega mu")


def gl_coefficients(sign_fixed=True):
    """GL93 eq. (10) at D = 4, r+ = 1: A2 H'' + A1 H' + A0 H = 0.  sign_fixed=False is the extraction's grouping."""
    x = 1 / _r
    V = 1 - x
    A2 = -_W**2 - _mu**2 * V + x**2 / (4 * _r**2)
    last = 3 * x**2 * (2 - x) / (4 * _r**3 * V)
    A1 = -(_mu**2 * (2 - 2 * x) + _W**2 * (2 + x)) / (_r * V) + (last if sign_fixed else -last)
    A0 = ((_mu**2 + _W**2 / V)**2 + _W**2 * (8 - 16 * x + 3 * x**2) / (4 * _r**2 * V**2)
          + _mu**2 * (8 - 20 * x + 13 * x**2) / (4 * _r**2 * V) + x**2 * (6 - 6 * x + x**2) / (4 * _r**4 * V**2))
    return A2, A1, A0


def horizon_exponents(sign_fixed=True):
    A2, A1, A0 = gl_coefficients(sign_fixed)
    s = sp.Symbol("s")
    p1 = sp.limit(sp.simplify(A1 / A2 * (_r - 1)), _r, 1)
    p0 = sp.limit(sp.simplify(A0 / A2 * (_r - 1)**2), _r, 1)
    return [sp.simplify(z) for z in sp.solve(s * (s - 1) + p1 * s + p0, s)], sp.limit(A0 / A2, _r, sp.oo)


_A2, _A1, _A0 = gl_coefficients()
_F1 = sp.lambdify((_r, _W, _mu), sp.simplify(_A1 / _A2), "numpy")
_F0 = sp.lambdify((_r, _W, _mu), sp.simplify(_A0 / _A2), "numpy")


def shoot(om, mu, d=1e-4, R=40.0, bump=0.6):
    """Growing-mode coefficient at r = R of the solution regular at the horizon ((r - 1)^(-1 + Omega)), integrated
    along r = t + i bump sin(pi (t - t0)/(R - t0)) around the apparent singularity where A2 = 0."""
    k = math.sqrt(om**2 + mu**2)
    t0 = 1 + d

    def rhs(t, y):
        ph = math.pi * (t - t0) / (R - t0)
        z = t + 1j * bump * math.sin(ph)
        dz = 1 + 1j * bump * math.pi / (R - t0) * math.cos(ph)
        return [y[1] * dz, (-_F1(z, om, mu) * y[1] - _F0(z, om, mu) * y[0]) * dz]
    s = -1 + om
    sol = solve_ivp(rhs, (t0, R), [d**s + 0j, s * d**(s - 1) + 0j], rtol=1e-10, atol=1e-14, method="DOP853")
    H, dH = sol.y[0, -1], sol.y[1, -1]
    return ((dH + k * H) * math.exp(-k * R)).real


def growth(mu, lo=3e-4, hi=0.15, n=40, **kw):
    om = np.linspace(lo, hi, n)
    f = [shoot(o, mu, **kw) for o in om]
    for i in range(n - 1):
        if np.sign(f[i]) != np.sign(f[i + 1]):
            return brentq(lambda o: shoot(o, mu, **kw), om[i], om[i + 1], xtol=1e-11)
    return None


def dispersion():
    curve = {mu: growth(mu) for mu in (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85)}
    best = minimize_scalar(lambda mu: -growth(mu, lo=0.05, hi=0.12, n=8), bounds=(0.25, 0.5), method="bounded",
                           options={"xatol": 1e-4})
    mu_peak, om_max = best.x, -best.fun
    # critical mu: Omega -> 0; extrapolate the last two small-Omega points linearly
    m1, m2 = 0.86, 0.865
    o1, o2 = growth(m1, lo=1e-4, hi=0.01, n=30), growth(m2, lo=1e-4, hi=0.01, n=30)
    mu_c = m2 + o2 * (m2 - m1) / (o1 - o2)
    om_alt = growth(mu_peak, lo=0.05, hi=0.12, n=8, d=3e-5, R=60.0, bump=0.9)
    none_past = growth(0.9, lo=1e-4, hi=0.15, n=40) is None
    return {"curve": curve, "mu_peak": mu_peak, "om_max": om_max, "mu_c": mu_c, "om_alt": om_alt,
            "none_past": none_past}


def compute():
    ow = _load(os.path.join(HERE, "o3_write.py"), "o3r_o3write")
    b4 = _load(os.path.join(HERE, "b4_static.py"), "o3r_b4static").compute(live=False)
    t3, t8 = ow.t_min(3), ow.t_eq8()
    T = ow._num(t3)
    T8 = ow._num(t8)
    singular = ow.SINGULAR_CLOCKS
    n_ref = float(sp.solve(sp.Eq(t3, singular), ow.N)[0] / ow.Z)
    disp = dispersion()
    rate_per_clock = disp["om_max"] / 2                     # r+ = 2m: Omega_max/(2m) per clock m
    efolds_half = rate_per_clock * (T / 2)                  # linear ramp, last half: m(v) <= m
    need = math.log(1 / SEED_FLOOR)
    frac_needed = need / rate_per_clock / T
    cascade = LP_T1 / (1 - LP_X)
    exps_fixed, inf_fixed = horizon_exponents(True)
    exps_raw, _ = horizon_exponents(False)
    wall = math.pi / disp["mu_c"]                            # flat limit: lowest Neumann mode pi/z_c below mu_c
    return {"T": T, "T8": T8, "singular": singular, "n_ref": n_ref, "t_fail_2": float(b4["cone"]["t_fail_2"]),
            "disp": disp, "rate": rate_per_clock, "adiabatic": (1 / T) / rate_per_clock, "efolds": efolds_half,
            "need": need, "frac": frac_needed, "cascade": cascade, "exps_fixed": exps_fixed, "exps_raw": exps_raw,
            "inf": inf_fixed, "wall_rplus": wall, "wall_m": 2 * wall}


def report(d):
    p = d["disp"]
    print("o3_readings.py -- item 159: both readings of where the write sits, tested\n")
    print("R1 (i) the write inside a standing corridor: needs %.3g clocks (Z = 108.75), %.0f by eq. (8); the static "
          "bulk's singular surface by ~%d -> refuted (above %.1f Z bits)" % (d["T"], d["T8"], d["singular"], d["n_ref"]))
    print("R2 the black string's instability (GL eq. (10), computed): horizon exponents %s (as extracted: %s); "
          "infinity %s" % (d["exps_fixed"], d["exps_raw"], d["inf"]))
    print("     Omega(mu), r+ = 1: %s" % ", ".join("%.2f:%.4f" % (k, v) for k, v in p["curve"].items()))
    print("     fastest Omega r+ = %.4f at mu r+ = %.3f (alt. settings %.4f); critical mu r+ = %.3f (L-P %.3f); "
          "none at 0.9: %s" % (p["om_max"], p["mu_peak"], p["om_alt"], p["mu_c"], 2 * math.pi / LP_CRIT, p["none_past"]))
    print("R3 (ii) the write as the opening: growth %.4f per clock against the mass's change %.2g of it; %.3g e-folds "
          "over the last half; %.0f needed for a 1e-100 seed (%.1f%% of the opening); cascade ends ~%.0f clocks later"
          % (d["rate"], d["adiabatic"], d["efolds"], d["need"], 100 * d["frac"], d["cascade"]))
    print("R4 escapes: (b) a wall within pi/mu_c = %.2f r+ = %.1f m switches it off (Gregory eq. (11) in the flat limit)"
          % (d["wall_rplus"], d["wall_m"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    p = d["disp"]
    W = _W
    chk("R2 transcription: with the one sign restored, the horizon exponents are GL's -1 +- Omega and the decay at "
        "infinity sqrt(Omega^2 + mu^2) (p.7); as extracted they are not (the control)",
        set(sp.simplify(e) for e in d["exps_fixed"]) == {-1 - W, -1 + W} and sp.simplify(d["inf"] + W**2 + _mu**2) == 0
        and set(sp.simplify(e) for e in d["exps_raw"]) != {-1 - W, -1 + W})
    chk("R2: unstable modes exist; fastest Omega r+ = 0.0923 at mu r+ ~ 0.35; two integration settings agree to 1e-3",
        all(v is not None and v > 0 for v in p["curve"].values()) and 0.092 < p["om_max"] < 0.0925
        and 0.32 < p["mu_peak"] < 0.38 and abs(p["om_alt"] - p["om_max"]) < 1e-4 * p["om_max"] * 10)
    chk("R2 controls: critical mu r+ = %.3f against Lehner-Pretorius's L/R ~ 7.2 (0.873) within 1%%; none at 0.9; "
        "Gregory's GM = 1 range (0.45) and most favoured (~0.2) bracket ours" % p["mu_c"],
        abs(p["mu_c"] - 2 * math.pi / LP_CRIT) < 0.01 * 0.873 and p["none_past"]
        and p["mu_c"] < 2 * GREGORY_MC + 0.01 and abs(p["mu_peak"] - 2 * GREGORY_MMAX) < 0.08)
    chk("R1 (i): the write (2.0e5 clocks; 630 by eq. (8)) passes the static bulk's singular surface (~18) -- refuted "
        "above 25.3 Z bits", d["T"] > 1e5 and d["T8"] > d["singular"] and 25 < d["n_ref"] < 25.6)
    chk("R3 (ii): the string is quasi-static (the mass changes at < 1e-3 of the growth rate) and grows ~4.6e3 e-folds "
        "over the opening's last half, 20x the 230 a 1e-100 seed needs", d["adiabatic"] < 1e-3
        and 4.4e3 < d["efolds"] < 4.8e3 and d["efolds"] > 20 * d["need"] and d["frac"] < 0.03)
    chk("R3 (ii): Lehner-Pretorius's cascade ends ~107 clocks after the first nonlinear stage, < 1e-3 of the opening",
        abs(d["cascade"] - 106.7) < 0.1 and d["cascade"] < 1e-3 * d["T"])
    chk("R4 (b): in the flat limit a wall closer than pi/mu_c ~ 3.6 r+ (7.2 m) switches the instability off",
        3.5 < d["wall_rplus"] < 3.7)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
