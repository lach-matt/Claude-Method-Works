#!/usr/bin/env python3
"""o3_readings.py -- M-RULINGS item 159, "test both options": the write in a hold after the corridor stands (reading
(i)) and the write as the opening (reading (ii)), each tested against the bulk.  Computed, READ and deduced; verified
once (findings applied, O3-READINGS.md History); not seated.  First headed "... not verified; not seated".

M's words (verbatim in the rulings file): item 159 "test both options"; item 158 (2) "Exactly as long as the write
needs  I should think"; item 115 (c) "The README itself"; item 127 (1) "yes" (the planes coincide, the extra dimension
included, "while the corridor exists"); item 138 (the bulk is multi-universal).

READ
  Gregory & Laflamme, hep-th/9301052: eq. (10), p.7, the s-wave equation for H_tr on Schwarzschild x R; p.7, "the
    regular solution at infinity is e^(-sqrt(Omega^2 + mu^2) r), and the solutions at the horizon behave as
    (r - r+)^(-1 +- r+ Omega/(D-3))"; pp.8-9, unstable, and "stabilized if the extra dimensions are compactified to a
    scale smaller than the minimum wavelength for which instability occurs".
  Emparan, Suzuki & Tanabe, 1302.6382: p.31, eqs. (7.3)-(7.6), the same perturbation equation (from GL's
    hep-th/9404071) in n = D - p - 3, with r0 = 1.
  Camps, Emparan & Haddad, 1003.3636: p.2, eq. (1.5), Omega = k/sqrt(n+1) (1 - (n+2)/(n sqrt(n+1)) k r0) to O(k^3);
    "the slope of the curve Omega(k) near k = 0 is exactly ... determined".
  Gregory, hep-th/0004101: p.5, "For GM = 1, the instability exists in the range 0 < m < 0.45, with the most favoured
    instability ... having m ~ 0.2"; pp.6-7, the single-wall Randall-Sundrum string is unstable too; p.7, eq. (11), the
    second-wall condition, and "for large mass black holes, e^(k z_c) >= 2 k G M for the existence of the instability";
    p.2, "the only exception being extremal solutions" (for the charged branes of its ref. [2]); p.4, the RS string is
    singular at the AdS horizon.
  Lehner & Pretorius, 1006.5960: p.2, string of "mass per unit length M", horizon radius 2.00 M (Table I); p.3, "the
    critical L/R is ~ 7.2"; pp.3-4, T1/M ~ 80, X ~ 1/4, t0 ~ T0 + T1/(1 - X), and -- an extrapolation: "the simulation
    results imply", "if the self-similar cascade continues" -- "the end-state will thus be a naked, curvature
    singularity"; p.4, rotation does not suppress the unstable modes.

  R1 READING (i) (deduced; numbers imported from o3_write.py).  As first tested -- the write inside a standing corridor,
     with the write the README's arrival (H-WRITE-IS-ARRIVAL) -- it is inconsistent: under 115 (c) and H-PULL-IS-COST
     the corridor's mass is the README's energy, so a standing corridor means the README has already arrived.  The
     coherent form is (i'): a write after arrival, an internal encoding of what has arrived.  W3's gas bound does not
     bound it; O3's static window [max(h/(4E), 1/(2 xi)), ~11.3 clocks) applies to it as before.  (i') is not refuted
     here.  The arrival itself -- the opening -- still lasts >= 2.0e5 clocks (630 by eq. (8)) on either reading, so
     what the opening's bulk does is B4d's on (i') too.
  R2 THE BLACK STRING'S INSTABILITY, COMPUTED (from READ eq. (10)).  GL's eq. (10) at D = 4, with one sign as extracted
     (the 3 (D-3)^2 x^(2(D-3)) term of the H' coefficient) contradicting GL's stated horizon exponents; restored, the
     equation is identical (sympy) to EST's eqs. (7.3)-(7.6) at n = 1 -- a second printed source fixing every term;
     the extracted form is not.  Shooting from the horizon's regular branch along a complex detour round the point
     where the H'' coefficient vanishes (the imaginary part of the result stays ~1e-9: an apparent singularity), the
     growing mode at infinity is cancelled at Omega(mu): unstable for 0 < mu r+ < 0.876, fastest Omega r+ = 0.0923 at
     mu r+ ~ 0.35.  Controls: Lehner-Pretorius's L/R ~ 7.2 is mu_c r+ = 0.873; Gregory's GM = 1 range and most
     favoured mode are consistent; CEH's small-k form within 3-6% for k r+ = 0.03-0.1 (the next-order term does not
     match CEH's cleanly at n = 1, where CEH p.7 flag a slower fall-off); two integration settings agree.
  R3 READING (ii): THE WRITE AS THE OPENING (computed and deduced, under named steps).
     H-QUASI-STATIC-STRING (the board's; outside B4b's static scope, B4d's to decide): near the plane and within its
     causal reach, the Vaidya opening's bulk is the black string of m(v).  Then, with H-MASS-RISES (a horizon present
     through the write -- not a late-arriving shell): the fixed mode mu = 0.35/r+(final) grows at >= Omega(0.35)/2 =
     0.046 per clock for any m(v) <= m (Omega(x)/x falls monotonically, computed), so >= 9.2e3 e-folds over 2.0e5
     clocks -- 29 over the eq.-(8) floor of 630, which then needs a seed above e^-29 (H-SEED; quantum noise ~ l_P/m is
     ~e^-16).  Lehner-Pretorius's extrapolated endpoint follows ~107 clocks after the nonlinear stage: classically a
     naked curvature singularity, Planck curvature in practice.  So in the board's quasi-static model the opening's
     bulk is not regular.
  R4 THE ESCAPES (deduced; none shown)
     open:  (d) the opening's bulk is not the black string (H-QUASI-STATIC-STRING fails -- B4d); (e) a late-arriving
            shell (H-MASS-RISES fails); (f) the short write (630 clocks) with seeds below e^-29; (i') above;
            (a) an extremal opening -- the board's mapping of Gregory's exception onto eq. (17)'s degenerate horizon;
            it collapses into (i)'s static problem only under the same static-uniqueness step as H-QUASI-STATIC-STRING.
     closed: (b) a nearby wall -- in the flat limit eq. (11) reduces to sin(m z_c) = 0 (deduced), so a wall closer than
            pi/mu_c = 3.59 r+ stops the final string; but from m = 0 every allowed mode mu = n pi/z_c crosses the whole
            unstable band, growing by (T/2) Int_0^mu_c Omega(x)/x dx = (T/2) 0.216 -- 2.2e4 e-folds at 2.0e5 clocks,
            68 at 630, whatever z_c (computed); and a wall within 7.2 m leaves no room for B4c's surface T.  Your 127's
            coinciding planes act as one wall (multiplane.py M4: tensions +4/3, -1/3) with the bulk semi-infinite beyond
            -- Gregory's single-wall case, unstable; 127's scope is "while the corridor exists".  Charge (non-extremal)
            and rotation do not help (READ: Gregory p.2; Lehner-Pretorius p.4).  Leaving the flat limit does not help
            (ii): the RS string is itself singular at the AdS horizon (Gregory p.4).
  VERDICT  (i) as first tested is inconsistent; its coherent form (i') stands in O3's static window, untested beyond it.
     (ii) is refuted in the board's quasi-static model, under H-QUASI-STATIC-STRING, H-MASS-RISES and H-README-ALONE
     (or H-SEED).  On both, the opening lasts >= 2.0e5 clocks and its bulk is B4d's.

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


def shoot(om, mu, d=1e-4, R=40.0, bump=0.6, both=False):
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
    c = (dH + k * H) * math.exp(-k * R)
    return (c.real, c.imag) if both else c.real


def growth(mu, lo=3e-4, hi=0.15, n=40, **kw):
    om = np.linspace(lo, hi, n)
    f = [shoot(o, mu, **kw) for o in om]
    for i in range(n - 1):
        if np.sign(f[i]) != np.sign(f[i + 1]):
            return brentq(lambda o: shoot(o, mu, **kw), om[i], om[i + 1], xtol=1e-11)
    return None


def dispersion():
    xs = [0.02, 0.05] + [round(0.1 * k, 2) for k in range(1, 9)] + [0.85]
    curve = {mu: growth(mu, lo=1e-4, hi=0.15, n=40, R=80.0, bump=1.2) for mu in xs}
    best = minimize_scalar(lambda mu: -growth(mu, lo=0.05, hi=0.12, n=8), bounds=(0.25, 0.5), method="bounded",
                           options={"xatol": 1e-4})
    mu_peak, om_max = best.x, -best.fun
    m1, m2 = 0.86, 0.865                                    # critical mu: Omega -> 0, extrapolated linearly
    o1, o2 = growth(m1, lo=1e-4, hi=0.01, n=30), growth(m2, lo=1e-4, hi=0.01, n=30)
    mu_c = m2 + o2 * (m2 - m1) / (o1 - o2)
    om_alt = growth(mu_peak, lo=0.05, hi=0.12, n=8, d=3e-5, R=60.0, bump=0.9)
    none_past = growth(0.9, lo=1e-4, hi=0.15, n=40) is None
    imag = abs(shoot(om_max, mu_peak, both=True)[1]) / max(abs(shoot(0.5 * om_max, mu_peak)), 1e-300)
    om35 = growth(0.35, lo=0.05, hi=0.12, n=8)
    return {"curve": curve, "mu_peak": mu_peak, "om_max": om_max, "mu_c": mu_c, "om_alt": om_alt,
            "none_past": none_past, "imag": imag, "om35": om35}


def band_integral(curve, mu_c):
    """Int_0^mu_c Omega(x)/x dx by the trapezoid rule on the computed curve, with Omega/x -> 1/sqrt(2) at 0 (CEH's
    exact slope at n = 1) and 0 at mu_c."""
    pts = [(0.0, 1 / math.sqrt(2))] + sorted((x, w / x) for x, w in curve.items()) + [(mu_c, 0.0)]
    return sum((b[0] - a[0]) * (a[1] + b[1]) / 2 for a, b in zip(pts, pts[1:]))


def est_identity():
    """GL93 eq. (10) at D = 4 (both forms) against EST 1302.6382 eqs. (7.3)-(7.6) at n = 1, r0 = 1, k = mu."""
    r, W, k, n = _r, _W, _mu, 1
    f = 1 - 1 / r**n
    A = n**2 - 4 * W**2 * r**2 - (4 * k**2 * r**2 + 2 * n**2) * f + n**2 * f**2
    P = (3 * n**3 - 12 * n * W**2 * r**2 + (3 * n**2 - 6 * n**3 - 8 * n * k**2 * r**2 - 4 * r**2 * W**2
         + 8 * n * W**2 * r**2) * f - (6 * n**2 - 3 * n**3 + 4 * k**2 * r**2 - 4 * n * k**2 * r**2) * f**2
         + 3 * n**2 * f**3) / (r * f * A)
    Q = ((n**2 - W**2 * r**2) * (n**2 - 4 * W**2 * r**2)
         + (3 * n**3 - n**4 + n**2 * k**2 * r**2 + 10 * n**2 * W**2 * r**2 + 8 * k**2 * W**2 * r**4) * f
         + (n**2 * (1 - 6 * n - n**2) + 2 * k**2 * r**2 * (2 * k**2 * r**2 - 2 * n - n**2)
            + W**2 * r**2 * (4 + 4 * n - 5 * n**2)) * f**2
         + (-2 * n**2 + 3 * n**3 + n**4 + 4 * k**2 * r**2 + 8 * n * k**2 * r**2 + n**2 * k**2 * r**2) * f**3
         + n**2 * f**4) / (r**2 * f**2 * A)
    out = {}
    for fixed in (True, False):
        A2, A1, A0 = gl_coefficients(fixed)
        out[fixed] = (sp.simplify(A1 / A2 - P) == 0, sp.simplify(A0 / A2 - Q) == 0)
    return out


def compute():
    ow = _load(os.path.join(HERE, "o3_write.py"), "o3r_o3write")
    t3, t8 = ow.t_min(3), ow.t_eq8()
    T = ow._num(t3)
    T8 = ow._num(t8)
    disp = dispersion()
    curve = disp["curve"]
    ratios = [w / x for x, w in sorted(curve.items())]
    monotone = all(a > b for a, b in zip(ratios, ratios[1:]))
    rate_fixed = disp["om35"] / 2                          # mode mu = 0.35/r+(final): >= Omega(0.35)/(2m) per clock
    I = band_integral(curve, disp["mu_c"])
    ceh = {k: (curve[k], k / math.sqrt(2) * (1 - 3 / math.sqrt(2) * k)) for k in (0.02, 0.05, 0.1)}
    exps_fixed, inf_fixed = horizon_exponents(True)
    exps_raw, _ = horizon_exponents(False)
    return {"T": T, "T8": T8, "disp": disp, "monotone": monotone, "rate": rate_fixed,
            "adiabatic": (1 / T) / rate_fixed, "efolds": rate_fixed * T, "efolds8": rate_fixed * T8,
            "I": I, "band": T / 2 * I, "band8": T8 / 2 * I, "cascade": LP_T1 / (1 - LP_X),
            "exps_fixed": exps_fixed, "exps_raw": exps_raw, "inf": inf_fixed, "est": est_identity(),
            "wall_rplus": math.pi / disp["mu_c"], "ceh": ceh}


def report(d):
    p = d["disp"]
    print("o3_readings.py -- item 159: both readings of where the write sits, tested\n")
    print("R1 (i) with the write as arrival is inconsistent with 115 (c) and H-PULL-IS-COST; (i'), a write after "
          "arrival, has O3's static window; the arrival lasts >= %.3g clocks (%.0f by eq. (8)) on either" % (d["T"], d["T8"]))
    print("R2 GL eq. (10): horizon exponents %s (as extracted %s); equal to EST (7.3)-(7.6): %s (as extracted: %s)"
          % (d["exps_fixed"], d["exps_raw"], d["est"][True], d["est"][False]))
    print("     Omega(mu), r+ = 1: %s" % ", ".join("%.2f:%.4f" % (k, v) for k, v in p["curve"].items()))
    print("     fastest %.4f at %.3f (alt. %.4f; imaginary residue %.1e); critical %.3f (L-P %.3f); none at 0.9: %s"
          % (p["om_max"], p["mu_peak"], p["om_alt"], p["imag"], p["mu_c"], 2 * math.pi / LP_CRIT, p["none_past"]))
    print("     CEH small k: %s" % ", ".join("%.2f: %.4f vs %.4f" % (k, a, b) for k, (a, b) in d["ceh"].items()))
    print("R3 (ii) under H-QUASI-STATIC-STRING, H-MASS-RISES: Omega(x)/x falls: %s; the mode 0.35/r+ grows >= %.4f per "
          "clock -- %.3g e-folds over the write, %.0f over 630; mass change %.1e of the growth; L-P ~%.0f clocks"
          % (d["monotone"], d["rate"], d["efolds"], d["efolds8"], d["adiabatic"], d["cascade"]))
    print("R4 (b) a wall stops the final string below pi/mu_c = %.2f r+, but from m = 0 every mode crosses the band: "
          "Int Omega/x = %.3f, %.3g e-folds (%.0f at 630)" % (d["wall_rplus"], d["I"], d["band"], d["band8"]))


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
    chk("R2 transcription: restored, the horizon exponents are GL's -1 +- Omega and the decay sqrt(Omega^2 + mu^2) "
        "(p.7); as extracted they are not",
        set(sp.simplify(e) for e in d["exps_fixed"]) == {-1 - W, -1 + W} and sp.simplify(d["inf"] + W**2 + _mu**2) == 0
        and set(sp.simplify(e) for e in d["exps_raw"]) != {-1 - W, -1 + W})
    chk("R2 READ control: restored, the equation is identical to EST's eqs. (7.3)-(7.6) at n = 1 in every term; as "
        "extracted it is not", d["est"][True] == (True, True) and d["est"][False] != (True, True))
    chk("R2: unstable modes exist; fastest Omega r+ = 0.0923 at mu r+ ~ 0.35; a second setting agrees to 1e-3; the "
        "detour's imaginary residue is small (an apparent singularity)",
        all(v is not None and v > 0 for v in p["curve"].values()) and 0.092 < p["om_max"] < 0.0925
        and 0.32 < p["mu_peak"] < 0.38 and abs(p["om_alt"] - p["om_max"]) < 1e-3 * p["om_max"] and p["imag"] < 1e-4)
    chk("R2 controls: critical mu r+ = %.3f against Lehner-Pretorius's L/R ~ 7.2 (0.873) within 1%%; none at 0.9; "
        "consistent with Gregory's GM = 1 range and favoured mode; within 7%% of CEH's small-k form at k r+ = 0.02-0.1"
        % p["mu_c"], abs(p["mu_c"] - 2 * math.pi / LP_CRIT) < 0.01 * 0.873 and p["none_past"]
        and p["mu_c"] < 2 * GREGORY_MC and abs(p["mu_peak"] - 2 * GREGORY_MMAX) < 0.08
        and all(abs(a / b - 1) < 0.07 for a, b in d["ceh"].values()))
    chk("R3 (ii): Omega(x)/x falls monotonically, so the mode 0.35/r+ grows >= 0.046 per clock for any m(v) <= m: "
        ">= 9.2e3 e-folds over 2.0e5 clocks, ~29 over 630; quasi-static (mass change < 1e-3 of the growth)",
        d["monotone"] and 0.045 < d["rate"] < 0.047 and 9.0e3 < d["efolds"] < 9.4e3 and 27 < d["efolds8"] < 31
        and d["adiabatic"] < 1e-3)
    chk("R4 (b): a wall stops the final string below pi/mu_c = 3.59 r+, but every mode crossing the band from m = 0 "
        "grows by (T/2) Int Omega/x = (T/2) 0.216: 2.2e4 e-folds (68 at 630)",
        3.55 < d["wall_rplus"] < 3.63 and 0.20 < d["I"] < 0.23 and 2.0e4 < d["band"] < 2.3e4 and 60 < d["band8"] < 75)
    chk("STRUCTURAL (imported/READ arithmetic): Lehner-Pretorius's 80/(1 - 1/4) = 106.7 clocks", abs(d["cascade"] - 106.7) < 0.1)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
