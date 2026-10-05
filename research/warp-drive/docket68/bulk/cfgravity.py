#!/usr/bin/env python3
"""
cfgravity.py -- BULK2-O6: does Chung-Freese's warped higher dimension change gravity on our plane at the lengths the
torsion balances test?  Computed on M's order (rulings item 67: "run this computation please").

Not seated; not yet verified.  Carried beside M's H-HIGHER-CORRIDOR, H-BULK-PAIRING and H-UNOBSERVED-UNBUILT, never as
results.  O9 stays OPEN.  Worked by deduction from named premises (M-DEDUCE, item 64).

    python3 cfgravity.py              report
    python3 cfgravity.py --selftest   checks, with CONTROLS
    python3 cfgravity.py --json       the numbers as JSON

THE SET-UP.  Chung-Freese's metric (hep-ph/9910235v2 eq. 3, static, READ): ds^2 = dt^2 - e^{-2ku} dh^2 - du^2, our plane
at u = 0, the hidden plane at u = L, the orbifold symmetric about each (H-ORBIFOLD).  pairing.py computed its bulk
stress-energy, G^M_N = (-6, -3, -3, -3, -3) k^2: an ISOTROPIC perfect fluid in the bulk (rho = -6 k^2, p = 3 k^2 in
G = T units; its microphysics is unspecified by CF -- H-CF-FLUID).

PREMISES AND STEPS
  S1 (COMPUTED, check 1) For a transverse-traceless perturbation g_xy = -e^{-2ku} gamma(t, z, u), the linearised mixed
     Einstein tensor is exactly delta G^x_y = -(1/2) box gamma, box the background d'Alembertian.  A perfect fluid has
     delta T^x_y = 0 for such a perturbation, so gamma obeys box gamma = 0 (DEDUCED from S1 and H-CF-FLUID).
  S2 (DEDUCED) Static (omega = 0) modes gamma = e^{i p.x} chi(u): (e^{-3ku} chi')' = -mu^2 e^{-ku} chi, Neumann at both
     planes.  With s = (mu/k) e^{ku} the equation is s^2 chi'' - 2 s chi' + s^2 chi = 0, solved by
     chi = sin(s - s0) - s cos(s - s0), whose s-derivative s sin(s - s0) vanishes at s0 = mu/k and at s1 = s0 e^{kL}
     exactly when s1 - s0 = n pi:  mu_n = n pi k / (e^{kL} - 1)  -- the inverse of the hidden plane's static 'conformal
     length' (e^{kL} - 1)/k.  CHECKED against an independent RK4 shooting of the ODE (check 2).
  S3 (DEDUCED) The static Green's function on our plane is (S/2) sum_n chi_n(0)^2 / (p^2 + mu_n^2) with weight e^{-ku};
     the zero mode gives 4D Newton with W = int_0^L e^{-ku} du = (1 - e^{-kL})/k; each massive mode a Yukawa of range
     1/mu_n and strength alpha_n = W chi_n(0)^2 = W k s0 / I_n, I_n = int_{s0}^{s1} (chi/s)^2 ds (computed by
     quadrature).  For large n, I_n -> n pi / 2 and alpha_n -> 2 e^{-kL} (check 3).
  S4 (NAMED) The massive modes' tensor structure multiplies each Yukawa by 4/3 (H-TENSOR-4/3: the massive spin-2 count;
     in CF's bulk, where time is unwarped, it is not derived).  CONTROL: as k -> 0 the set-up is one flat interval and
     the result is alpha = 2 x 4/3 = 8/3 with range L/pi = R -- Kapner et al.'s READ 'a Yukawa interaction with
     alpha = 8/3 and lambda = R' for a single extra dimension (hep-ph/0611184 p.4).  Brane bending and any radion are
     omitted (H-NO-BENDING).
  S5 (COMPUTED) The deviation from Newton on our plane, delta(r) = (4/3) sum_n alpha_n e^{-mu_n r}, summed exactly for
     the first modes and as a geometric tail beyond; for r << (e^{kL} - 1)/k it is close to 8 (1 - e^{-kL}) / (3 pi k r)
     -- a power law, not a single Yukawa (check 5).
  S6 (READ, NAMED) Lee et al. (arXiv:2002.11761 p.2): 'our work can be viewed as percent-level measurements of G_N at
     separations down to about 50 um'.  Read as |delta(52 um)| <~ 0.01 (H-PERCENT: a criterion, not their fit; a fit of
     a power-law deviation to their data is OPEN).

NAMED HYPOTHESES
  H-CF-FLUID, H-ORBIFOLD, H-TENSOR-4/3, H-NO-BENDING, H-PERCENT (above); pairing.py's H-CF-STATIC, H-L-ILLUSTRATIVE;
  with M's H-HIGHER-CORRIDOR, H-BULK-PAIRING, H-UNOBSERVED-UNBUILT.
"""
import contextlib
import functools
import importlib.util
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _by_path(key, path):
    if key in sys.modules:
        return sys.modules[key]
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    spec.loader.exec_module(mod)
    return mod


with contextlib.redirect_stdout(io.StringIO()):
    bulk = _by_path("bulk_bulk", os.path.join(HERE, "bulk.py"))
    pairing = _by_path("bulk_pairing", os.path.join(HERE, "pairing.py"))
    searches = _by_path("bulk_searches", os.path.join(HERE, "searches.py"))

L_M = bulk.CF["L_illustrative_m"]
LEE_SPAN = searches.TORSION["lee_span_m"]
PERCENT = 0.01
TENSOR = 4.0 / 3.0
N_EXACT = 40


# ------------------------------------------------------------------ S1: the TT perturbation obeys box gamma = 0
def tt_linearised():
    """delta G^x_y (mixed) for g_xy = -e^{-2ku} eps gamma(t,z,u) in CF's static metric, and box gamma; returns their
    ratio (sympy), and the same for a CONTROL perturbation that is not transverse-traceless (gamma in g_xx)."""
    import sympy as sp
    t, x, y, z, u, k, eps = sp.symbols("t x y z u k epsilon", real=True)
    X = [t, x, y, z, u]
    n = 5
    gam = sp.Function("gamma")(t, z, u)

    def lin_mixed(slot):
        a2 = sp.exp(-2 * k * u)
        g = sp.diag(1, -a2, -a2, -a2, -1)
        if slot == "xy":
            g[1, 2] = g[2, 1] = -a2 * eps * gam
        else:
            g[1, 1] = -a2 * (1 + eps * gam)
        gi = g.inv().applyfunc(lambda e: sp.series(e, eps, 0, 2).removeO())
        d = lambda e, i: sp.diff(e, X[i])
        trunc = lambda e: sp.series(sp.expand(e), eps, 0, 2).removeO()
        G3 = [[[sp.expand(sum(gi[a, q] * (d(g[q, b], c) + d(g[q, c], b) - d(g[b, c], q)) for q in range(n)) / 2)
                for c in range(n)] for b in range(n)] for a in range(n)]
        riem = lambda a, b, c, q: (d(G3[a][b][q], c) - d(G3[a][b][c], q)
                                   + sum(G3[a][c][e] * G3[e][b][q] - G3[a][q][e] * G3[e][b][c] for e in range(n)))
        Ric = sp.zeros(n)
        for b in range(n):
            for q in range(n):
                Ric[b, q] = trunc(sum(riem(a, b, a, q) for a in range(n)))
        R = trunc(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
        G = Ric - R * g / 2
        col = 2 if slot == "xy" else 1
        mixed = trunc(sum(gi[1, c] * G[c, col] for c in range(n)))
        return sp.simplify(sp.diff(mixed, eps).subs(eps, 0))

    sqrtg = sp.exp(-3 * k * u)
    box = sp.simplify((sp.diff(sqrtg * sp.diff(gam, t), t) - sp.diff(sqrtg * sp.exp(2 * k * u) * sp.diff(gam, z), z)
                       - sp.diff(sqrtg * sp.diff(gam, u), u)) / sqrtg)
    return sp.simplify(lin_mixed("xy") / box), sp.simplify(lin_mixed("xx") / box)


# ------------------------------------------------------------------ S2-S3: the static modes
def mu_closed(n, k, kL):
    return n * math.pi * k / math.expm1(kL)


def mu_shoot(n, kL, steps=20000):
    """The n-th Neumann eigenvalue of chi'' - 3 chi' + mu^2 e^{2u} chi = 0 on [0, kL] (units k = 1), by RK4 shooting
    and bisection on chi'(kL) = 0 -- independent of the closed form."""
    def end_slope(mu):
        h = kL / steps
        y, v, uu = 1.0, 0.0, 0.0
        f = lambda uu, y, v: (v, 3 * v - mu * mu * math.exp(2 * uu) * y)
        for _ in range(steps):
            k1 = f(uu, y, v)
            k2 = f(uu + h / 2, y + h / 2 * k1[0], v + h / 2 * k1[1])
            k3 = f(uu + h / 2, y + h / 2 * k2[0], v + h / 2 * k2[1])
            k4 = f(uu + h, y + h * k3[0], v + h * k3[1])
            y += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
            v += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
            uu += h
        return v
    guess = mu_closed(n, 1.0, kL)
    lo, hi = guess * (1 - 0.3 / n), guess * (1 + 0.3 / n)
    flo = end_slope(lo)
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        fm = end_slope(mid)
        if flo * fm <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


@functools.lru_cache(maxsize=None)
def alpha_exact(n, kL, per_pi=400):
    """alpha_n = W chi_n(0)^2 (units k = 1), the norm integral by Simpson over s in [s0, s0 + n pi]."""
    W = -math.expm1(-kL)
    s0 = n * math.pi / math.expm1(kL)
    m = 2 * per_pi * n
    h = n * math.pi / m
    f = lambda s: ((math.sin(s - s0) - s * math.cos(s - s0)) / s) ** 2
    I = sum((1 if i in (0, m) else (4 if i % 2 else 2)) * f(s0 + i * h) for i in range(m + 1)) * h / 3
    return W * s0 / I


def deviation(r_m, kL, L_m=L_M, tensor=True, n_exact=N_EXACT):
    """delta(r): the summed Yukawas of the massive modes on our plane, relative to 4D Newton."""
    k = kL / L_m
    x = math.pi * k * r_m / math.expm1(kL)
    head = sum(alpha_exact(n, kL) * math.exp(-n * x) for n in range(1, n_exact + 1))
    tail = 2 * math.exp(-kL) * math.exp(-(n_exact + 1) * x) / (-math.expm1(-x))
    return (TENSOR if tensor else 1.0) * (head + tail)


def inv_k_allowed(kL, r_m=LEE_SPAN[0], target=PERCENT):
    """The largest 1/k (metres) with delta(r_m) <= target at this kL (bisection in L)."""
    lo, hi = 1e-12, 1.0
    for _ in range(80):
        mid = math.sqrt(lo * hi)
        if deviation(r_m, kL, L_m=mid * kL) > target:
            hi = mid
        else:
            lo = mid
    return lo


def compute():
    rows = []
    for d in (pairing.design(T) for T in (pairing.YEAR_S, 86400.0, 3600.0, 1.0)):
        kL = d["kL_needed"]
        inv_k = L_M / kL
        ik_max = inv_k_allowed(kL)
        rows.append({"T_s": d["T_s"], "kL": kL, "inv_k_um": 1e6 * inv_k,
                     "lambda1_m": 1.0 / mu_closed(1, kL / L_M, kL), "alpha1_tensor": TENSOR * alpha_exact(1, kL),
                     "delta_52um": deviation(52e-6, kL), "delta_1mm": deviation(1e-3, kL),
                     "delta_3mm": deviation(3e-3, kL), "delta_52um_scalar": deviation(52e-6, kL, tensor=False),
                     "approx_52um": 8 * (-math.expm1(-kL)) / (3 * math.pi * (kL / L_M) * 52e-6),
                     "inv_k_max_um": 1e6 * ik_max, "L_max_um": 1e6 * ik_max * kL,
                     "verdict": "EXCLUDED by H-PERCENT" if deviation(52e-6, kL) > PERCENT else "ALLOWED by H-PERCENT"})
    return {"rows": rows, "L_m": L_M, "lee_span_m": LEE_SPAN, "percent": PERCENT}


def report():
    d = compute()
    print("cfgravity.py -- BULK2-O6: Chung-Freese's bulk and gravity on our plane (not verified; not seated)\n")
    print("static modes mu_n = n pi k / (e^{kL} - 1); each a Yukawa of strength ~2 e^{-kL} (x 4/3, H-TENSOR-4/3); "
          "summed, delta(r) ~ 8 (1 - e^{-kL}) / (3 pi k r)\n")
    for r in d["rows"]:
        print("  T = %9.0f s: kL = %5.2f, 1/k = %6.1f um, first range %.2e m (alpha %.1e) -> delta at 52 um %.3f, "
              "1 mm %.4f, 3 mm %.4f  [%s]" % (r["T_s"], r["kL"], r["inv_k_um"], r["lambda1_m"], r["alpha1_tensor"],
                                             r["delta_52um"], r["delta_1mm"], r["delta_3mm"], r["verdict"]))
        print("      percent-level at 52 um needs 1/k <= %.3f um, i.e. L <= %.2f um at this kL" % (
            r["inv_k_max_um"], r["L_max_um"]))


def selftest():
    n_pass = n_fail = n_ctl = 0
    structural = []

    def chk(label, ok, ctl=False):
        nonlocal n_pass, n_fail, n_ctl
        n_ctl += ctl
        n_pass += bool(ok)
        n_fail += (not ok)
        print("  %s %s%s" % ("ok  " if ok else "FAIL", "CONTROL: " if ctl else "", label))

    rt, rc = tt_linearised()
    chk("S1: for a transverse-traceless perturbation of CF's static metric, delta G^x_y / box gamma = %s (a constant: "
        "box gamma = 0 for a perfect-fluid bulk)" % rt, str(rt) == "-1/2")
    chk("a perturbation that is not transverse-traceless (gamma in g_xx) gives a different ratio (%s), so the check "
        "can fail" % (str(rc)[:50]), str(rc) != "-1/2", ctl=True)
    shots = {(n, kL): mu_shoot(n, kL) for n in (1, 2) for kL in (1.0, 3.0)}
    rels = {key: abs(v / mu_closed(key[0], 1.0, key[1]) - 1) for key, v in shots.items()}
    chk("S2: the closed form mu_n = n pi k / (e^{kL} - 1) agrees with RK4 shooting of the ODE at kL = 1, 3, n = 1, 2 "
        "(max rel. %.1e)" % max(rels.values()), max(rels.values()) < 1e-6)
    a_flat = alpha_exact(1, 1e-6)
    chk("CONTROL k -> 0: one flat interval, first range L/pi and alpha = %.4f x 4/3 = %.4f -- Kapner's READ 8/3 for "
        "a single extra dimension (lambda = R)" % (a_flat, TENSOR * a_flat),
        abs(TENSOR * a_flat - 8 / 3) < 1e-4 and abs(1 / mu_closed(1, 1e-6 / L_M, 1e-6) - L_M / math.pi) < 1e-9, ctl=True)
    al = [alpha_exact(n, 10.0) / (2 * math.exp(-10.0)) for n in (5, 20, 40)]
    chk("S3: alpha_n approaches 2 e^{-kL} for large n (kL = 10: ratios %s at n = 5, 20, 40)" % [round(a, 4) for a in al],
        all(abs(a - 1) < 0.05 for a in al) and abs(al[2] - 1) < abs(al[0] - 1) + 1e-12)
    d = compute()
    chk("S5: the summed deviation agrees with the leading form 8 (1 - e^{-kL}) / (3 pi k r) at 52 um for every design "
        "(%s, within 5 %%)" % [(round(r["delta_52um"], 3), round(r["approx_52um"], 3)) for r in d["rows"]],
        all(abs(r["delta_52um"] / r["approx_52um"] - 1) < 0.05 for r in d["rows"]))
    structural.append("the deviation is a POWER LAW, ~ 8 (1 - e^{-kL}) / (3 pi k r), from many modes of strength ~2 e^{-kL}, not one "
                      "Yukawa: single-Yukawa exclusion curves do not apply directly; H-PERCENT is a criterion, not a fit")
    structural.append("1/k = L/kL: the verdict is about the illustrative L = 1 mm; at each kL the design survives "
                      "H-PERCENT for L below the printed L_max")
    structural.append("H-TENSOR-4/3 changes every delta by 4/3 only; the scalar values are printed alongside and give "
                      "the same verdicts")
    for s in structural:
        print("  STRUCTURAL: " + s)
    print("cfgravity.py: %d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute(), indent=1, default=str))
    else:
        report()
