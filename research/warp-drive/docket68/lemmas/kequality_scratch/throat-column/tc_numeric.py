#!/usr/bin/env python3
"""tc_numeric.py -- model B (the corridor's own throat bulk): the two-plane balance on the computed columns.

Scratch instrument for M-RULINGS items 179-181 (not a board instrument; read-only on the repository).  Owner imported
by path, never copied: lemmas/sim2_facing.py (throat_bulk, throat_rhs, kret_throat).  Numerical (DOP853, rtol 1e-13);
tolerances stated per line.  Units m = 1, e = m/ell, sigma_RS(ell) = 3 nu e.

  N1  NO UMBILIC DEPTH (numerical check of tc_symbolic X2's exact statement): D = q - p > 0 at every grid point of
      (0, y_s) for e = 0 ... 64 (16 values); min D/y reported; and D against its integral representation.
  N2  THE CORRIDOR'S BULK DEPTH IN ell: y_s(e)/ell = e y_s(e) -- a function of e, not a value.
  N3  FREE FAR SIDE (traceless part carried by position 2's universe's bulk, curvature ell_f): s2(y2) on the decaying and
      growing roots (tc_symbolic X4), and the depth where it meets each convention's target:
        C-PRZ        s2 = -1/4, ell_f = 4 ell/3   (KDERIVE, b6_k, multiplane M4 as printed: PRZ's doubled count)
        C-SHEET-M4   s2 = -1/8, ell_f = 4 ell/3   (M4's geometry, one sheet: -1/6 in sigma_RS(ell_f); stage 7 K5)
        C-S6         s2 = -1/3, ell_f = 3 ell     (stage 6 J3: position 2's own ell_2 = 3 ell)
        C-S7         s2 = -1/6, ell_f = 6 ell     (stage 7 K5 applied to stage 6's route: one sheet -1/6, ell_2 = 6 ell)
      The mirrored convention (C-MIRROR, one ell) is N1 + T5c: no depth.
  N4  THE FAR SIDE WHERE N3 HAS A ROOT: the decaying far column started from the jump data, followed with throat_rhs at
      e_f -- the Riccati trap (a_f < -e_f, Pi != 0) and its end, with the Kretschmann scalar.
  N5  H-README-ON-P2 (mirrored P2 carrying matter): rho_m / sigma_RS = (p + 2q)/(3e) - s2; rho_m + p_r,m = 0;
      rho_m + p_th,m = nu (q - p) > 0.  The WEC window of depths per e and per convention: a region, not a point.
      And the count: the Jacobian of (rho_m, p_th,m) in (y2, e) -- two prescribed README numbers would be needed.
python3 tc_numeric.py
"""
import math
import os
import sys

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _owner  # noqa: E402

S2M = _owner.sim2()

ES = [0.0, 1 / 1024, 1 / 256, 1 / 64, 1 / 32, 1 / 16, 1 / 8, 1 / 4, 1 / 2, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0]
CONV = {"C-PRZ": (-0.25, 0.75), "C-SHEET-M4": (-0.125, 0.75), "C-S6": (-1 / 3, 1 / 3), "C-S7": (-1 / 6, 1 / 6)}
NGRID = 6000
_TB = {}


def column(e):
    if e not in _TB:
        tb = S2M.throat_bulk(e)
        s0 = tb["sol0"]
        _TB[e] = (tb["y_s"], lambda yy: s0.sol(yy), tb)
    return _TB[e]


def grid(ys, n=NGRID):
    # dense near 0 and near y_s
    u = np.linspace(0, 1, n + 2)[1:-1]
    return ys * (0.5 - 0.5 * np.cos(math.pi * u))


def n1_n2():
    rows = []
    for e in ES:
        ys, f, tb = column(e)
        yy = grid(ys * (1 - 1e-7))
        U = np.array([f(z) for z in yy]).T
        al, be, p, q = U
        D = q - p
        a = (p + q) / 2
        cons = p**2 + q**2 + 4 * p * q - 6 * e * e - 1 / (4 * be**2) + 1 / (4 * al**2)
        # integral representation at three depths (quad on the dense solution)
        rep = []
        for frac in (0.1, 0.5, 0.9):
            Y = frac * ys
            inner = lambda tt: quad(lambda s: float(np.sum(f(s)[2:4]) / 2), tt, Y, epsabs=1e-13, epsrel=1e-12)[0]
            Sx = lambda tt: 1 / (4 * f(tt)[0]**2) + 1 / (4 * f(tt)[1]**2)
            val = quad(lambda tt: Sx(tt) * math.exp(-4 * inner(tt)), 0, Y, epsabs=1e-12, epsrel=1e-10, limit=200)[0]
            Dy = float(f(Y)[3] - f(Y)[2])
            rep.append(abs(val - Dy) / abs(Dy))
        i = int(np.argmin(D / yy))
        rows.append({"e": e, "y_s": ys, "e_ys": e * ys, "D_min": float(D.min()), "D_over_y_min": float((D / yy)[i]),
                     "at_frac": float(yy[i] / ys), "all_pos": bool(np.all(D > 0)), "a_plus_e_max": float(np.max(a + e)),
                     "beta_end": float(be[-1]), "alpha_end": float(al[-1]), "cons_max_rel": float(
                         np.max(np.abs(cons) / (p**2 + q**2 + 6 * e * e + 1 / (4 * be**2) + 1 / (4 * al**2)))),
                     "rep_rel": max(rep)})
    return rows


_ST = {}


def stable_column(e):
    """(alpha, beta, at = a + e, D = q - p): the owner's column re-expressed in variables free of cancellation near
    y = 0 (identities checked exactly in tc_symbolic X2: D' = -4aD + S, a' = e^2 - a^2 - D^2/4).  Cross-checked
    against the owner's p, q (N3 prints the largest difference)."""
    if e in _ST:
        return _ST[e]
    ys, f, _ = column(e)

    def rhs(yy, u):
        al, be, at, D = u
        a = at - e
        return [(a - D / 2) * al, (a + D / 2) * be, -at * at + 2 * e * at - D * D / 4,
                -4 * a * D + 1 / (4 * al * al) + 1 / (4 * be * be)]
    sol = solve_ivp(rhs, [0, ys * (1 - 1e-6)], [1.0, 1.0, 0.0, 0.0], method="DOP853", rtol=1e-13, atol=1e-30,
                    dense_output=True, max_step=ys / 2000)
    yy = grid(ys * 0.99, 2000)
    dif = max(max(abs(sol.sol(z)[2] - e - sol.sol(z)[3] / 2 - f(z)[2]), abs(sol.sol(z)[2] - e + sol.sol(z)[3] / 2 - f(z)[3]))
              / (abs(f(z)[2]) + abs(f(z)[3]) + 1e-300) for z in yy)
    def cons(z):
        al, be, at, D = sol.sol(z)
        p, q = at - e - D / 2, at - e + D / 2
        c = p * p + q * q + 4 * p * q - 6 * e * e - 1 / (4 * be * be) + 1 / (4 * al * al)
        return abs(c) / (p * p + q * q + 6 * e * e + 1 / (4 * be * be) + 1 / (4 * al * al))
    cmax = max(cons(z) for z in grid(ys * (1 - 1e-6), 2000))
    _ST[e] = (ys, sol.sol, (dif, cmax))
    return _ST[e]


def s2_stable(e, ef, at):
    """Decaying and growing roots of tc_symbolic X4 in cancellation-free form; Delta = e^2 - e_f^2."""
    A = e - at                                   # |a|
    sq = np.sqrt(A * A - e * e + ef * ef)
    Dl = e * e - ef * ef
    return -Dl / (2 * e * (A + sq)), -(A + sq) / (2 * e)


def h_excess(e, ef, at):
    """sign of s2_dec(y) - s2_dec(0): h = -at (1 + (2e - at)/(sqrt((e - at)^2 - e^2 + e_f^2) + e_f)) (deduced form)."""
    sq = np.sqrt((e - at)**2 - e * e + ef * ef)
    return -at * (1 + (2 * e - at) / (sq + ef))


def s2_roots(e, ef, a):
    disc = a * a - e * e + ef * ef
    sq = np.sqrt(disc)
    return (a + sq) / (2 * e), (a - sq) / (2 * e)        # decaying, growing (tc_symbolic X4)


def n3():
    out = {}
    for name, (target, rf) in CONV.items():
        rows = []
        for e in ES:
            if e == 0:
                continue                                    # sigma_RS(ell) = 0: the unit is empty
            ys, g, dif = stable_column(e)
            ef = rf * e
            yy = grid(ys * (1 - 1e-6))
            at = np.array([g(z)[2] for z in yy])
            dec, gro = s2_stable(e, ef, at)
            dec0 = -(e - ef) / (2 * e)                      # the y2 -> 0 value, exactly (|a| = e)
            h = h_excess(e, ef, at)
            roots = []
            if abs(target - dec0) < 1e-12:
                kind = "only at y2 = 0 (coincidence): s2_dec - target > 0 at every grid point y2 > 0 (min h/y^3 = %.3e)" % (
                    float(np.min(h / yy**3)))
                ok = bool(np.all(h > 0))
            else:
                ok = True
                for lab, arr in (("decaying", dec), ("growing", gro)):
                    gg = arr - target
                    idx = np.where(np.sign(gg[:-1]) * np.sign(gg[1:]) < 0)[0]
                    for j in idx:
                        k = 0 if lab == "decaying" else 1
                        fun = lambda z: s2_stable(e, ef, g(z)[2])[k] - target
                        roots.append((lab, float(brentq(fun, yy[j], yy[j + 1], xtol=1e-14))))
                kind = "roots: " + (", ".join("%s y2=%.6f (y2/y_s=%.4f, y2/ell=%.5f)" % (lab, y2, y2 / ys, y2 * e)
                                              for lab, y2 in roots) or "none at any y2 >= 0")
            rows.append({"e": e, "dec_range": (dec0, float(dec[-1])), "gro_max": float(gro.max()), "roots": roots,
                         "y_s": ys, "monotone_dec": bool(np.all(np.diff(at) < 0)), "kind": kind, "ok": ok,
                         "stable_vs_owner": dif, "at_max": float(at.max())})
        out[name] = rows
    return out


def far_column(e, ef, y2, branch="decaying"):
    """Position 2's universe's bulk beyond its plane, started from the jump data at depth y2 (outward coordinate z)."""
    ys, f, _ = column(e)
    al, be, p, q = f(y2)
    a = (p + q) / 2
    sq = math.sqrt(a * a - e * e + ef * ef)
    kbar = (-a - sq) / 2 if branch == "decaying" else (-a + sq) / 2
    pf, qf = p + 2 * kbar, q + 2 * kbar
    c0 = pf**2 + qf**2 + 4 * pf * qf - 6 * ef * ef - 1 / (4 * be**2) + 1 / (4 * al**2)

    def rhs(z, u):
        return S2M.throat_rhs(z, list(u) + [0.0] * 6, ef)[:4]

    def small(z, u):
        return min(u[0], u[1]) - 1e-9
    small.terminal = True

    def blow(z, u):
        return abs(u[2]) + abs(u[3]) - 1e12
    blow.terminal = True
    sol = solve_ivp(rhs, [0, 200.0], [al, be, pf, qf], method="DOP853", rtol=1e-12, atol=1e-14, events=[small, blow],
                    dense_output=True, max_step=0.01)
    zend = float(sol.t[-1])
    af = (sol.y[2] + sol.y[3]) / 2
    K = [S2M.kret_throat([sol.y[0][i], sol.y[1][i], sol.y[2][i], sol.y[3][i]], ef) for i in range(len(sol.t))]
    trapped = bool(np.all(af <= -ef + 1e-12))
    Kat = {}
    for thr in (1e-2, 1e-4, 1e-6):
        idx = np.where(sol.y[0] <= thr)[0]
        if len(idx):
            i = idx[0]
            Kat[thr] = float(S2M.kret_throat([sol.y[0][i], sol.y[1][i], sol.y[2][i], sol.y[3][i]], ef))
    return {"z_end": zend, "z_end_over_ellf": zend * ef, "status": sol.status, "a_f0": float(af[0]),
            "trapped": trapped, "K_start": float(K[0]), "K_end": float(K[-1]), "c0": float(c0),
            "which_zero": "alpha" if sol.y[0][-1] < sol.y[1][-1] else "beta",
            "Pi0": float(qf - pf), "K_at_alpha": Kat}


def n4(n3out):
    rows = []
    for name in ("C-SHEET-M4", "C-S6"):                 # the coincidence-only conventions: the far side at y2 = 0
        for e in (1 / 32, 1.0):
            rows.append((name, e, 0.0, far_column(e, CONV[name][1] * e, 0.0, "decaying")))
    for name, rws in n3out.items():
        target, rf = CONV[name]
        for r in rws:
            for lab, y2 in r["roots"]:
                if r["e"] in (1 / 32, 1 / 4, 1.0, 4.0):
                    fc = far_column(r["e"], rf * r["e"], y2, lab)
                    rows.append((name, r["e"], y2, fc))
    return rows


def n5():
    """Mirrored P2 carrying the README's matter, its law at s2: rho_m/sigma_RS and the WEC window."""
    out = {}
    for s2 in (-0.25, -1 / 3, -1 / 6, -0.125, 1.0):
        rows = []
        for e in ES[1:]:
            ys, f, _ = column(e)
            yy = grid(ys * (1 - 1e-7))
            U = np.array([f(z) for z in yy]).T
            al, be, p, q = U
            rho_m = (p + 2 * q) / (3 * e) - s2             # in sigma_RS(ell)
            nec_th = (q - p) / (3 * e)                      # (rho_m + p_th,m) / sigma_RS
            pos = rho_m >= 0
            if pos.any():
                i0 = int(np.argmax(pos))
                lo = brentq(lambda z: (f(z)[2] + 2 * f(z)[3]) / (3 * e) - s2, yy[max(i0 - 1, 0)], yy[i0]) if i0 > 0 else 0.0
                win = (lo / ys, float(yy[np.where(pos)[0][-1]] / ys))
            else:
                win = None
            rows.append({"e": e, "rho_m_at_0": float((p[0] + 2 * q[0]) / (3 * e) - s2), "max_rho_m": float(rho_m.max()),
                         "window_frac": win, "nec_th_min": float(nec_th.min())})
        out[s2] = rows
    # the count: Jacobian of (rho_m, p_th_m) [nu/m units] in (y2, e) at a sample point, by central differences
    jac = []
    for (e0, fr) in ((1 / 32, 0.5), (1 / 8, 0.5), (1.0, 0.5)):
        def F(y2, e, s2=-0.25):
            ys, f, _ = column(e)
            al, be, p, q = f(y2)
            return np.array([(p + 2 * q) - 3 * s2 * e, -(2 * p + q) + 3 * s2 * e])
        ys0, _, _ = column(e0)
        y0 = fr * ys0
        hy, he = 1e-5 * ys0, 1e-5 * e0
        Fy = (F(y0 + hy, e0) - F(y0 - hy, e0)) / (2 * hy)
        # e-derivative: recompute columns at e0 +- he (not cached in ES)
        Fe = (F(y0, e0 + he) - F(y0, e0 - he)) / (2 * he)
        jac.append((e0, fr, float(Fy[0] * Fe[1] - Fy[1] * Fe[0]), float(np.linalg.cond(np.array([Fy, Fe]).T))))
    return out, jac


def max_rho_m(e, s2):
    ys, f, _ = column(e)
    yy = grid(ys * (1 - 1e-7), 1500)
    v = np.array([(f(z)[2] + 2 * f(z)[3]) / (3 * e) - s2 for z in yy])
    i = int(np.argmax(v))
    lo, hi = yy[max(i - 1, 0)], yy[min(i + 1, len(yy) - 1)]
    from scipy.optimize import minimize_scalar
    r = minimize_scalar(lambda z: -((f(z)[2] + 2 * f(z)[3]) / (3 * e) - s2), bounds=(lo, hi), method="bounded",
                        options={"xatol": 1e-12})
    return -r.fun, r.x / ys


def n5_thresholds():
    """e* where the best depth's rho_m crosses zero, per P2 law: positive README energy on a mirrored P2 needs e < e*
    (ell > ell* = m/e*).  s2 = +1 is SIM2's H-SPLIT-AT-OUR-TENSION: it must reproduce SIM2's 27.07m (the control)."""
    out = []
    for s2 in (1.0, -0.125, -1 / 6, -0.25, -1 / 3):
        lo, hi = 1 / 64, 1 / 2
        es = brentq(lambda ee: max_rho_m(ee, s2)[0], lo, hi, xtol=1e-12)
        out.append((s2, es, 1 / es, max_rho_m(es, s2)[1]))
    return out


def main():
    print("N1/N2  the umbilic defect D = q - p on the throat column, and the column's depth in ell")
    print("  e        y_s        e*y_s     min D      min D/y (at y/y_s)   D>0 all   max(a+e)     cons rel   int.rep rel  alpha,beta end")
    r12 = n1_n2()
    for r in r12:
        print("  %-8.5g %-10.6f %-9.5f %-10.3e %-8.5f (%.3f)       %-8s %-12.3e %-10.1e %-11.1e %.1e, %.3f" % (
            r["e"], r["y_s"], r["e_ys"], r["D_min"], r["D_over_y_min"], r["at_frac"], r["all_pos"], r["a_plus_e_max"],
            r["cons_max_rel"], r["rep_rel"], r["alpha_end"], r["beta_end"]))
    ok1 = all(r["all_pos"] for r in r12) and all(r["a_plus_e_max"] <= 1e-12 for r in r12)
    print("  N1 verdict: D > 0 at every grid point of every column, a <= -e throughout:", ok1)
    mono = all(r12[i + 1]["e_ys"] > r12[i]["e_ys"] for i in range(1, len(r12) - 1))
    print("  N2: e*y_s rises with e at every step (e > 0):", mono, "-- the corridor's bulk depth in ell is a function of e")

    print("\nN3  free far side: s2(y2) on the decaying root (range from y2 -> 0 to y2 -> y_s) and the growing root's maximum")
    n3o = n3()
    for name, rws in n3o.items():
        target, rf = CONV[name]
        print("  %s: target s2 = %.6f, ell_f/ell = %.6f" % (name, target, 1 / rf))
        for r in rws:
            print("    e=%-8.5g dec s2 (%.6f -> %.2e), a~ strictly falling %s; gro max %.6f; max a~ %.1e; stable vs owner"
                  " %.1e (y<=0.99y_s), its constraint %.1e; %s" % (
                      r["e"], r["dec_range"][0], r["dec_range"][1], r["monotone_dec"], r["gro_max"], r["at_max"],
                      r["stable_vs_owner"][0], r["stable_vs_owner"][1], r["kind"]))
    print("\nN4  the far side at the N3 roots (decaying, Pi != 0): Riccati trap and end")
    for name, e, y2, fc in n4(n3o):
        print("  %s e=%-6.4g y2=%.5f: a_f(0)=%.5f (-e_f=%.5f) Pi0=%.3e trapped=%s; ends at z=%.5f (z e_f=%.4f), %s -> 0, "
              "K %.3g, then %s; far constraint at start %.1e" % (name, e, y2, fc["a_f0"], -CONV[name][1] * e, fc["Pi0"],
                                                                fc["trapped"], fc["z_end"], fc["z_end_over_ellf"],
                                                                fc["which_zero"], fc["K_start"],
                                                                ", ".join("%.2g at alpha=%.0e" % (v, k) for k, v in
                                                                          sorted(fc["K_at_alpha"].items(), reverse=True)),
                                                                fc["c0"]))
    print("\nN5  H-README-ON-P2: mirrored P2 with matter; rho_m/sigma_RS = (p+2q)/(3e) - s2; WEC window as y2/y_s")
    n5o, jac = n5()
    for s2, rws in n5o.items():
        print("  P2's law s2 = %.4f:" % s2)
        for r in rws:
            print("    e=%-8.5g rho_m(depth->0)=%.5f  max rho_m=%.5f  WEC window=%s  min (rho_m+p_th,m)/sigma_RS=%.2e" % (
                r["e"], r["rho_m_at_0"], r["max_rho_m"],
                ("[%.4f, %.4f]" % r["window_frac"]) if r["window_frac"] else "none", r["nec_th_min"]))
    print("  positive-energy thresholds (a bound, not an equality): best-depth rho_m = 0 at e*, so WEC needs ell > ell*:")
    for s2, es, lst, fr in n5_thresholds():
        print("    P2 law s2 = %+.4f: e* = %.7f, ell* = %.4f m, best depth %.4f y_s%s" % (
            s2, es, lst, fr, "   <- SIM2 S7 control: 27.07m" if s2 == 1.0 else ""))
    print("  the count: det d(rho_m, p_th,m)/d(y2, e) at s2 = -1/4 (nu/m units), and its condition number:")
    for e0, fr, det, cond in jac:
        print("    e=%.5g, y2 = %.2f y_s: det = %.6g, cond = %.3g" % (e0, fr, det, cond))
    return ok1


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
