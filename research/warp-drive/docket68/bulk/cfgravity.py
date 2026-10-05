#!/usr/bin/env python3
"""
cfgravity.py -- BULK2-O6: does Chung-Freese's warped higher dimension change gravity on our plane at the lengths the
torsion balances test?  Computed on M's order (rulings item 67: "run this computation please").

Not seated; verified once (2026-10-05), findings applied (HISTORY below).  Carried beside M's H-HIGHER-CORRIDOR, H-BULK-PAIRING and H-UNOBSERVED-UNBUILT, never as
results.  O9 stays OPEN.  Worked by deduction from named premises (M-DEDUCE, item 64).

    python3 cfgravity.py              report
    python3 cfgravity.py --selftest   checks, with CONTROLS
    python3 cfgravity.py --json       the numbers as JSON

THE SET-UP.  Chung-Freese's metric (hep-ph/9910235v2 eq. 3, static, READ): ds^2 = dt^2 - e^{-2ku} dh^2 - du^2, our plane
at u = 0, the hidden plane at u = L, the orbifold symmetric about each (H-ORBIFOLD).  pairing.py computed its bulk
stress-energy, G^M_N = (-6, -3, -3, -3, -3) k^2: an ISOTROPIC perfect fluid (rho = -6 k^2, p = +3 k^2 in G = T units),
whose microphysics CF do not give.

PREMISES AND STEPS
  S1 (COMPUTED, check 1) Newton's law on our plane comes from the lapse, g_00 = 1 + 2 Phi.  For a static perturbation
     (Phi, and any g_ii, g_uu, g_zu parts) the linearised R^0_0 is exactly Delta Phi, Delta = e^{2ku} d_z^2 + d_u^2
     - 3k d_u; the background R^0_0 = 0.  The 5D Einstein equation R^0_0 = kappa (T^0_0 - T/3) then reads
     Delta Phi = kappa (2/3) delta(rho + 2p) + the planes' sources (DEDUCED).
  S1b (COMPUTED, check 3) Hydrostatics of the static fluid: the u-component of div T = 0 gives
     delta p' = -(rho + p) Phi', so delta p = +3 k^2 Phi / kappa -- never zero, because rho + p = -3 k^2 / kappa (the NEC
     violation).  With a sound speed c_s^2 = delta p / delta rho, the lapse equation becomes
     (Delta - m^2) Phi = source with m^2 = (4 + 2 / c_s^2) k^2 (DEDUCED).  m^2 > 0 screens 4D Newton beyond ~1/k; m^2 < 0
     is unstable; only c_s^2 = -1/2 -- the background's own p/rho, itself gradient-unstable -- gives m^2 = 0.
     H-CF-FLUID is therefore SHARPENED: a barotropic bulk fluid with dp/drho = -1/2, and plane matter whose
     perturbations keep delta(T^0_0 - T/3) = 0 (H-PLANE-EOS: the verifier's Israel-junction reading of CF's planes,
     p_b = -(2/3) rho_b, NOT re-run here).  Under it everything below stands; otherwise it does not.
  S2 (DEDUCED, check 4) The static modes of Delta: (e^{-3ku} chi')' = -mu^2 e^{-ku} chi, Neumann at both planes.  With
     s = (mu/k) e^{ku}: chi = sin(s - s0) - s cos(s - s0), and mu_n = n pi k / (e^{kL} - 1) -- the inverse of the
     conformal length int_0^L e^{ku} du.  CHECKED against RK4 shooting.  The TT graviton obeys the same operator
     (delta G^x_y = -(1/2) box gamma, check 2), so the spectrum is shared.
  S3 (DEDUCED, check 6) The zero mode gives 4D Newton with W = int_0^L e^{-ku} du; each massive mode a Yukawa of range
     1/mu_n and strength alpha_n = W chi_n(0)^2 -> 2 e^{-kL}.  All modes share the same 5D source factor, so the relative
     factor is 1 (COMPUTED).  x 4/3 applies only if a stabilising sector restores pure 4D coupling to the zero mode
     (H-STABILISED: Adelberger et al. hep-ph/0611223 p.2, 'the volume of the extra dimensions must be stabilized by
     radions').  CONTROL (check 5): as k -> 0 each mode has alpha = 2; with H-STABILISED this is Kapner et al.'s READ
     'alpha = 8/3 and lambda = R' for a single extra dimension (hep-ph/0611184 p.4), valid for R <~ s_min.
  S4 (COMPUTED, check 7) delta(r) = sum_n alpha_n e^{-mu_n r} ~ 2 (1 - e^{-kL}) / (pi k r) for r << the conformal
     length: a 1/r^2 term in the potential -- the 5D law -- not a single Yukawa.
  S5 (READ, two criteria) (a) Lee et al. (arXiv:2002.11761 p.2): 'percent-level measurements of G_N at separations down
     to about 50 um' -- read as |delta(52 um)| <~ 0.01 (H-PERCENT); the calibration at 17-19 cm sees delta <~ 3e-4, so a
     constant absorbed into G changes nothing.  (b) Adelberger et al. hep-ph/0611223 Table I, p.3: a fit of Kapner's
     55 um - 9.53 mm data to V = -G Ma Mb / r beta_2 (1 mm / r) gives |beta_2| <= 4.5e-4 (68 %) -- exactly the shape
     delta = beta_2 (1 mm / r); applicable where the conformal length exceeds the data's 9.53 mm.
  Brane bending cannot enter: time is unwarped, so a plane displacement leaves g_00 unchanged at linear order, and any
  g_uu or g_zu part is inside S1's identity.

NAMED HYPOTHESES
  H-CF-FLUID (sharpened, above), H-PLANE-EOS, H-ORBIFOLD, H-STABILISED, H-PERCENT; pairing.py's H-CF-STATIC,
  H-L-ILLUSTRATIVE; with M's H-HIGHER-CORRIDOR, H-BULK-PAIRING, H-UNOBSERVED-UNBUILT.

HISTORY (verifier, 2026-10-05; first-written claims kept)
  * S1 first derived the potential from the TT mode alone ('gamma obeys box gamma = 0 ... DEDUCED from S1 and
    H-CF-FLUID'); Newton's law comes from the lapse, where a perfect fluid DOES respond (delta p = 3 k^2 Phi) unless
    dp/drho = -1/2.  H-CF-FLUID is sharpened, and the k^2 mass term for any other fluid is now deduced.
  * S4 first multiplied every Yukawa by 4/3 (H-TENSOR-4/3) and named H-NO-BENDING; the computed factor is 1, x 4/3 needs
    a stabilised radion (H-STABILISED), and bending cannot enter.  The first figures (delta 0.87-8.3 at 52 um; L_max
    4.9-17.5 um) were the x 4/3 ones; the computed ones are 0.65-6.2 and 6.4-18.8 um.
  * the S1 control put gamma in g_xx, where delta G^x_y vanishes by symmetry -- it could not fail; now the flat
    d'Alembertian against CF's.
  * 'the hidden plane's static length, which the warp makes long' -- a conformal length, not a proper one.
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
STABILISED = 4.0 / 3.0     # H-STABILISED only
BETA2_BOUND = 4.5e-4      # Adelberger et al. hep-ph/0611223 Table I p.3, 68 %, Kapner's 55 um - 9.53 mm data
KAPNER_SPAN = searches.TORSION["kapner_span_m"]
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
    box_flat = sp.diff(gam, t, 2) - sp.diff(gam, z, 2) - sp.diff(gam, u, 2)
    lxy = lin_mixed("xy")
    return sp.simplify(lxy / box), sp.simplify(lxy / box_flat)


def lapse_linearised():
    """Static perturbation g_00 = 1 + 2 eps Phi, g_ii = -e^{-2ku}(1 + 2 eps psi), g_uu = -(1 + 2 eps B), g_zu = -eps Cz:
    returns (background R^0_0, delta R^0_0 / Delta Phi, delta R^0_0 / flat Laplacian Phi) and the linearised u-component
    of div T for a static perfect fluid (rho0 + eps r1, p0 + eps p1)."""
    import sympy as sp
    t, x, y, z, u, k, eps = sp.symbols("t x y z u k epsilon", real=True)
    X = [t, x, y, z, u]
    n = 5
    Phi, psi, B, Cz = (sp.Function(nm)(z, u) for nm in ("Phi", "psi", "B", "Cz"))
    a2 = sp.exp(-2 * k * u)
    g = sp.diag(1 + 2 * eps * Phi, -a2 * (1 + 2 * eps * psi), -a2 * (1 + 2 * eps * psi), -a2 * (1 + 2 * eps * psi),
                -(1 + 2 * eps * B))
    g[3, 4] = g[4, 3] = -eps * Cz
    gi = g.inv().applyfunc(lambda e: sp.series(e, eps, 0, 2).removeO())
    d = lambda e, i: sp.diff(e, X[i])
    trunc = lambda e: sp.series(sp.expand(e), eps, 0, 2).removeO()
    G3 = [[[sp.expand(sum(gi[a, q] * (d(g[q, b], c) + d(g[q, c], b) - d(g[b, c], q)) for q in range(n)) / 2)
            for c in range(n)] for b in range(n)] for a in range(n)]
    riem = lambda a, b, c, q: (d(G3[a][b][q], c) - d(G3[a][b][c], q)
                               + sum(G3[a][c][e] * G3[e][b][q] - G3[a][q][e] * G3[e][b][c] for e in range(n)))
    R00 = trunc(sum(gi[0, c] * trunc(sum(riem(a, c, a, 0) for a in range(n))) for c in range(n)))
    lin = sp.simplify(sp.diff(R00, eps).subs(eps, 0))
    Dg = sp.exp(2 * k * u) * sp.diff(Phi, z, 2) + sp.diff(Phi, u, 2) - 3 * k * sp.diff(Phi, u)
    Dflat = sp.diff(Phi, z, 2) + sp.diff(Phi, u, 2)
    rho0, p0 = sp.symbols("rho0 p0", real=True)
    r1, p1 = sp.Function("r1")(z, u), sp.Function("p1")(z, u)
    rho, pr = rho0 + eps * r1, p0 + eps * p1
    uup = [1 / sp.sqrt(g[0, 0]), 0, 0, 0, 0]
    udn = [sum(g[i, j] * uup[j] for j in range(n)) for i in range(n)]
    T = sp.Matrix(n, n, lambda M, N: (rho + pr) * uup[M] * udn[N] - (pr if M == N else 0))
    sqrtg = sp.sqrt(-g.det())
    div_u = trunc(sum(d(sqrtg * T[M, 4], M) for M in range(n)) / sqrtg
                  - sum(G3[Lq][M][4] * T[M, Lq] for M in range(n) for Lq in range(n)))
    hydro = sp.simplify(sp.diff(div_u, eps).subs(eps, 0))
    expect = -(sp.diff(p1, u) + (rho0 + p0) * sp.diff(Phi, u))
    return (sp.simplify(R00.subs(eps, 0)), sp.simplify(lin / Dg), sp.simplify(lin / Dflat),
            sp.simplify(hydro - expect) == 0)


def lapse_mass2_over_k2(cs2):
    """m^2 / k^2 = 4 + 2 / c_s^2 (S1b): kappa (2/3) delta(rho + 2p), delta p = 3 k^2 Phi / kappa, delta rho = delta p / c_s^2."""
    return 4.0 + 2.0 / cs2


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


def deviation(r_m, kL, L_m=L_M, stabilised=False, n_exact=N_EXACT):
    """delta(r): the summed Yukawas of the massive modes on our plane, relative to 4D Newton."""
    k = kL / L_m
    x = math.pi * k * r_m / math.expm1(kL)
    head = sum(alpha_exact(n, kL) * math.exp(-n * x) for n in range(1, n_exact + 1))
    tail = 2 * math.exp(-kL) * math.exp(-(n_exact + 1) * x) / (-math.expm1(-x))
    return (STABILISED if stabilised else 1.0) * (head + tail)


def inv_k_allowed(kL, r_m=LEE_SPAN[0], target=PERCENT, stabilised=False):
    """The largest 1/k (metres) with delta(r_m) <= target at this kL (bisection in L)."""
    lo, hi = 1e-12, 1.0
    for _ in range(80):
        mid = math.sqrt(lo * hi)
        if deviation(r_m, kL, L_m=mid * kL, stabilised=stabilised) > target:
            hi = mid
        else:
            lo = mid
    return lo


def conformal_length_m(kL, L_m):
    return math.expm1(kL) * L_m / kL


def beta2(kL, L_m):
    """delta = beta_2 (1 mm / r) in the power-law regime: beta_2 = 2 W / (pi x 1 mm), W = (1 - e^{-kL}) / k."""
    return 2 * (-math.expm1(-kL)) * (L_m / kL) / (math.pi * 1e-3)


def L_allowed_beta2(kL):
    lo, hi = 1e-9, 1.0
    for _ in range(80):
        mid = math.sqrt(lo * hi)
        if beta2(kL, mid) > BETA2_BOUND:
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
        ik_max_s = inv_k_allowed(kL, stabilised=True)
        Lb = L_allowed_beta2(kL)
        d52 = deviation(52e-6, kL)
        rows.append({"T_s": d["T_s"], "kL": kL, "inv_k_um": 1e6 * inv_k,
                     "lambda1_m": 1.0 / mu_closed(1, kL / L_M, kL), "alpha1": alpha_exact(1, kL),
                     "delta_52um": d52, "delta_1mm": deviation(1e-3, kL), "delta_3mm": deviation(3e-3, kL),
                     "delta_52um_stabilised": deviation(52e-6, kL, stabilised=True),
                     "delta_calib_17cm": deviation(0.17, kL),
                     "approx_52um": 2 * (-math.expm1(-kL)) / (math.pi * (kL / L_M) * 52e-6),
                     "beta2_at_1mm": beta2(kL, L_M),
                     "inv_k_max_um": 1e6 * ik_max, "L_max_um": 1e6 * ik_max * kL,
                     "L_max_stabilised_um": 1e6 * ik_max_s * kL,
                     "L_max_beta2_um": 1e6 * Lb, "beta2_applies": conformal_length_m(kL, Lb) > KAPNER_SPAN[1],
                     "nec_density_rise": (L_M / (ik_max * kL)) ** 2,
                     "verdict": "EXCLUDED by H-PERCENT" if d52 > PERCENT else "ALLOWED by H-PERCENT"})
    mass = {cs2: lapse_mass2_over_k2(cs2) for cs2 in (1.0, 1.0 / 3.0, -1.0, -0.5, -0.25)}
    return {"rows": rows, "L_m": L_M, "lee_span_m": LEE_SPAN, "percent": PERCENT, "lapse_mass2_over_k2": mass}


def report():
    d = compute()
    print("cfgravity.py -- BULK2-O6: Chung-Freese's bulk and gravity on our plane (verified once; not seated)\n")
    print("the lapse obeys (Delta - m^2) Phi = source with m^2/k^2 = 4 + 2/c_s^2:  " + ", ".join(
        "c_s^2 = %+.2f -> %+.1f" % (c, m) for c, m in d["lapse_mass2_over_k2"].items())
          + "\n  -> 4D Newton survives only for c_s^2 = -1/2 (H-CF-FLUID, sharpened; itself gradient-unstable)\n")
    print("under it: static modes mu_n = n pi k / (e^{kL} - 1), each a Yukawa of strength ~2 e^{-kL} (factor 1, computed; "
          "x 4/3 under H-STABILISED); summed, delta(r) ~ 2 (1 - e^{-kL}) / (pi k r)\n")
    for r in d["rows"]:
        print("  T = %9.0f s: kL = %5.2f, 1/k = %6.1f um -> delta at 52 um %.3f (x4/3: %.3f), 1 mm %.4f, 3 mm %.4f, "
              "17 cm %.1e; beta_2 %.3f vs <= 4.5e-4  [%s]" % (
                  r["T_s"], r["kL"], r["inv_k_um"], r["delta_52um"], r["delta_52um_stabilised"], r["delta_1mm"],
                  r["delta_3mm"], r["delta_calib_17cm"], r["beta2_at_1mm"], r["verdict"]))
        print("      survives at L <= %.1f um (H-PERCENT; %.1f um under H-STABILISED); beta_2 fit: L <= %.1f um (%s); "
              "the NEC-violating density then rises x%.0e" % (
                  r["L_max_um"], r["L_max_stabilised_um"], r["L_max_beta2_um"],
                  "applies" if r["beta2_applies"] else "power law does not span the data -- not applicable",
                  r["nec_density_rise"]))


def selftest():
    n_pass = n_fail = n_ctl = 0
    structural = []

    def chk(label, ok, ctl=False):
        nonlocal n_pass, n_fail, n_ctl
        n_ctl += ctl
        n_pass += bool(ok)
        n_fail += (not ok)
        print("  %s %s%s" % ("ok  " if ok else "FAIL", "CONTROL: " if ctl else "", label))

    bg, r_lapse, r_flat, hydro_ok = lapse_linearised()
    chk("S1: background R^0_0 = %s, and for a static lapse perturbation (with g_ii, g_uu, g_zu parts) delta R^0_0 / "
        "Delta Phi = %s" % (bg, r_lapse), str(bg) == "0" and str(r_lapse) == "1")
    chk("against the flat Laplacian the ratio is not 1 (%s...), so the check can fail" % str(r_flat)[:40],
        str(r_flat) != "1", ctl=True)
    rt, rflat = tt_linearised()
    chk("S2 (shared spectrum): the TT mode gives delta G^x_y / box gamma = %s, CF's own d'Alembertian" % rt,
        str(rt) == "-1/2")
    chk("S1b: hydrostatics of the static fluid gives delta p' = -(rho + p) Phi' exactly: %s" % hydro_ok, hydro_ok)
    shots = {(n, kL): mu_shoot(n, kL) for n in (1, 2) for kL in (1.0, 3.0)}
    rels = {key: abs(v / mu_closed(key[0], 1.0, key[1]) - 1) for key, v in shots.items()}
    chk("S2: the closed form mu_n = n pi k / (e^{kL} - 1) agrees with RK4 shooting of the ODE at kL = 1, 3, n = 1, 2 "
        "(max rel. %.1e)" % max(rels.values()), max(rels.values()) < 1e-6)
    a_flat = alpha_exact(1, 1e-6)
    chk("k -> 0: one flat interval, first range L/pi and alpha = %.4f per mode (with H-STABILISED x 4/3 = %.4f, Kapner's "
        "READ 8/3 for R <~ s_min)" % (a_flat, STABILISED * a_flat),
        abs(a_flat - 2) < 1e-4 and abs(1 / mu_closed(1, 1e-6 / L_M, 1e-6) - L_M / math.pi) < 1e-9, ctl=True)
    al = [alpha_exact(n, 10.0) / (2 * math.exp(-10.0)) for n in (5, 20, 40)]
    chk("S3: alpha_n approaches 2 e^{-kL} for large n (kL = 10: ratios %s at n = 5, 20, 40)" % [round(a, 4) for a in al],
        all(abs(a - 1) < 0.05 for a in al) and abs(al[2] - 1) < abs(al[0] - 1) + 1e-12)
    d = compute()
    chk("S4: the summed deviation agrees with the leading form 2 (1 - e^{-kL}) / (pi k r) at 52 um for every design "
        "(%s, within 5 %%)" % [(round(r["delta_52um"], 3), round(r["approx_52um"], 3)) for r in d["rows"]],
        all(abs(r["delta_52um"] / r["approx_52um"] - 1) < 0.05 for r in d["rows"]))
    back = [deviation(52e-6, r["kL"], L_m=1e-6 * r["L_max_um"]) for r in d["rows"]]
    chk("the printed L_max reproduces delta(52 um) = 0.0100 on re-evaluation (%s)" % [round(b, 5) for b in back],
        all(abs(b - PERCENT) < 1e-4 for b in back))
    structural.append("S1b's mass term m^2 = (4 + 2/c_s^2) k^2 is deduced from S1, S1b and the trace-reversed 5D "
                      "Einstein equation; c_s^2 = -1/2 is the only Newtonian fluid, and it is gradient-unstable")
    structural.append("the deviation is a POWER LAW from many modes of strength ~2 e^{-kL}: single-Yukawa curves do not "
                      "apply directly; H-PERCENT is a criterion, the beta_2 fit (READ) a second, where it spans the data")
    structural.append("1/k = L/kL: the verdict is about the illustrative L = 1 mm; at each kL the design survives below "
                      "the printed L_max, with the NEC-violating density (~k^2) rising as (1 mm / L_max)^2")
    structural.append("H-PLANE-EOS rests on the verifier's Israel-junction reading of CF's planes (p_b = -(2/3) rho_b), "
                      "not re-run here")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
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
