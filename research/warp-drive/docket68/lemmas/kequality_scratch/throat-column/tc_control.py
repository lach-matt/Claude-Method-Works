#!/usr/bin/env python3
"""tc_control.py -- model B's controls: pure AdS5 (no corridor), its mutation, and a positive control.

Scratch instrument for M-RULINGS items 179-181 (not a board instrument; read-only on the repository).  Owner imported by
path: lemmas/sim2_facing.py (throat_rhs).  Uses tc_symbolic.x1_equations (my own derivation, slice curvatures cA, cS).

  K1  PURE AdS5, EXACT (computed, sympy): with flat slices (cA = cS = 0) alpha = beta = exp(-e y), p = q = -e solves the
      column equations and the constraint identically -- M's control "with no corridor (pure anti-de Sitter)".  D == 0:
      every level surface is umbilic, with k = -e at every depth.
  K2  THE BALANCE DETECTOR ON PURE AdS5 (computed, numerical): mirrored s2 = ell p = -1 at every depth; free far side
      s2 = -(1 - ell/ell_f)/2 at every depth; max |s2(y2) - s2(0)| = 0 (to 1e-12) and s2 is the same at every e.
      So each convention's condition holds at every depth or at none, and no e is singled out: NO LENGTH IS FIXED.
      The same through the owner's throat_rhs with alpha0 = beta0 = 1e12 over y < 3 ell (the corridor's slice curvature
      1/(4 alpha^2) below 1e-14 e^2 there): the column tends to pure AdS5 -- only over a range in y, since alpha decays
      and the curvature term returns (the column is the corridor's, rescaled; its singular end moves to ~ ln(alpha0)/e).
  K3  THE CONTROL CAN FAIL (mutation): the identical detector on the corridor's column (alpha0 = beta0 = 1) reports
      depth dependence of order one and D > 0 -- a detector that passed everything would pass this too; it does not.
  K4  POSITIVE CONTROL: slices of unequal radii (alpha0 = 1, beta0 = 2: R4 = -3/8) -- an umbilic plane at s1 = 1/2 has
      its balance at exactly one e = 1/sqrt(24) (the scan finds it); on eq. (17)'s equal radii the same scan finds the
      balance at every e for s1 = 1 and at none for s1 != 1.  The machinery returns an equality when one exists.
  K5  AT MOST ONE UMBILIC SLICE PER COLUMN (deduced from tc_symbolic X2: at a zero of D, D' = S > 0; checked here): a
      column started at an umbilic slice of unequal radii, followed both ways with the owner's throat_rhs, has D < 0
      before it and D > 0 after it -- one zero.  So two matter-free planes with mirrored or pure-trace far sides cannot
      both be level surfaces of one AdS2 x S2 vacuum column (any Lambda5): the bearing on a two-sided bridge (model C,
      item 182) in this symmetry class.
python3 tc_control.py
"""
import math
import os
import sys

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _owner  # noqa: E402
import tc_symbolic as TS  # noqa: E402

S2M = _owner.sim2()
CONV = {"C-PRZ": (-0.25, 0.75), "C-SHEET-M4": (-0.125, 0.75), "C-S6": (-1 / 3, 1 / 3), "C-S7": (-1 / 6, 1 / 6),
        "C-MIRROR(-1/4)": (-0.25, None)}
EK = [1 / 64, 1 / 8, 1.0, 8.0]


def k1_exact():
    eqs = TS.x1_equations()
    p, q, a, b = eqs["syms"]
    y, e = TS.y, TS.e
    flat = {TS.cA: 0, TS.cS: 0}
    al = sp.exp(-e * y)
    sub = {p: -e, q: -e, a: al, b: al}
    resP = sp.simplify(eqs["P"].subs(flat).subs(sub) - 0)       # p' = 0 for p = -e constant
    resQ = sp.simplify(eqs["Q"].subs(flat).subs(sub) - 0)
    resC = sp.simplify(eqs["cons"].subs(flat).subs(sub))
    # alpha'/alpha = p check
    resA = sp.simplify(sp.diff(al, y) / al + e)
    return {"P": resP, "Q": resQ, "cons": resC, "alpha": resA}


def column_generic(e, al0, be0, cA=1.0, cS=1.0, use_owner=True, yend=None):
    """Follow (alpha, beta, p, q) from p = q = -e.  use_owner: the owner's throat_rhs (cA = cS = 1 hard-coded there);
    else my derived equations with (cA, cS)."""
    def rhs(yy, u):
        if use_owner:
            return S2M.throat_rhs(yy, list(u) + [0.0] * 6, e)[:4]
        al, be, p, q = u
        return [p * al, q * be, 4 * e * e - 2 * p * p - 2 * p * q - cA / (4 * al * al),
                4 * e * e - 2 * q * q - 2 * p * q + cS / (4 * be * be)]

    def small(yy, u):
        return min(u[0], u[1]) - 1e-9
    small.terminal = True
    pq0 = -e
    # the constraint fixes p = q = -e only when R4 = 0; for unequal radii start from the umbilic root
    R4 = -cA / (2 * al0**2) + cS / (2 * be0**2)
    k = -math.sqrt(e * e + R4 / 12) if e * e + R4 / 12 >= 0 else float("nan")
    if abs(R4) > 0:
        pq0 = k
    Y = yend if yend is not None else (12.0 if e < 0.5 else 12.0 / e)
    sol = solve_ivp(rhs, [0, Y], [al0, be0, pq0, pq0], method="DOP853", rtol=1e-13, atol=1e-30, events=[small],
                    dense_output=True, max_step=Y / 4000)
    return sol


def detector(e, sol, conv_target, rf):
    """The balance detector: does the convention's tension condition single out a depth?  Returns the umbilic defect,
    the depth dependence of s2, and the sign-change count of s2 - target."""
    T = sol.t[-1]
    yy = np.linspace(T * 1e-4, T * (1 - 1e-6), 3000)
    U = np.array([sol.sol(z) for z in yy]).T
    al, be, p, q = U
    a = (p + q) / 2
    D = q - p
    if rf is None:                                   # mirrored, one ell: needs p = q; s2 = ell p
        s2 = p / e
    else:
        ef = rf * e
        A = -a
        s2 = -(e * e - ef * ef) / (2 * e * (A + np.sqrt(A * A - e * e + ef * ef)))     # decaying root
    g = s2 - conv_target
    return {"D_max_rel": float(np.max(np.abs(D)) / e), "s2_spread": float(np.max(s2) - np.min(s2)),
            "s2_0": float(s2[0]), "everywhere": bool(np.all(np.abs(g) < 1e-10)), "nowhere": bool(np.all(np.abs(g) > 1e-10)),
            "crossings": int(np.sum(np.sign(g[:-1]) * np.sign(g[1:]) < 0))}


def k2_k3():
    rows = []
    for e in EK:
        cases = {"pure AdS5 (my eqs, cA=cS=0)": column_generic(e, 1.0, 1.0, 0.0, 0.0, use_owner=False, yend=6.0 / e),
                 "owner throat_rhs, alpha0=beta0=1e12, y<3ell": column_generic(e, 1e12, 1e12, use_owner=True,
                                                                               yend=3.0 / e),
                 "MUTATION: corridor column (owner, alpha0=beta0=1)": column_generic(e, 1.0, 1.0, use_owner=True)}
        for lab, sol in cases.items():
            for name, (tg, rf) in CONV.items():
                d = detector(e, sol, tg, rf)
                rows.append((e, lab, name, d))
    return rows


def k4_positive():
    eqs = TS.x1_equations()
    p, q, a, b = eqs["syms"]
    cons = sp.lambdify((p, q, a, b, TS.e), eqs["cons"].subs({TS.cA: 1, TS.cS: 1}), "math")
    out = {}
    # unequal radii: the umbilic balance at s1 = 1/2 -- scan e and find the root
    f = lambda ee, s1, al0, be0: cons(-s1 * ee, -s1 * ee, al0, be0, ee)
    grid = np.linspace(0.01, 2.0, 2000)
    for (al0, be0, s1) in ((1.0, 2.0, 0.5), (1.0, 1.0, 1.0), (1.0, 1.0, 0.5), (1.0, 1.0, 0.25)):
        v = np.array([f(ee, s1, al0, be0) for ee in grid])
        if np.max(np.abs(v)) < 1e-12:
            roots = ["every e"]
        else:
            idx = np.where(np.sign(v[:-1]) * np.sign(v[1:]) < 0)[0]
            roots = [brentq(lambda ee: f(ee, s1, al0, be0), grid[i], grid[i + 1], xtol=1e-15) for i in idx]
        out[(al0, be0, s1)] = {"roots": roots, "max_abs": float(np.max(np.abs(v))), "identically_zero":
                               bool(np.max(np.abs(v)) < 1e-12)}
    return out


def k5_one_zero():
    out = []
    for (e, al0, be0) in ((1 / 8, 1.0, 0.8), (1.0, 1.0, 0.8), (1.0, 1.0, 1.0), (1 / 32, 2.0, 1.5)):
        R4 = -1 / (2 * al0**2) + 1 / (2 * be0**2)
        k = -math.sqrt(e * e + R4 / 12)
        rhs = lambda yy, u: S2M.throat_rhs(yy, list(u) + [0.0] * 6, e)[:4]

        def small(yy, u):
            return min(u[0], u[1]) - 1e-6
        small.terminal = True
        zeros, signs = 0, []
        for Y in (-3.0, 3.0):
            sol = solve_ivp(rhs, [0, Y], [al0, be0, k, k], method="DOP853", rtol=1e-12, atol=1e-14, events=[small],
                            dense_output=True)
            T = sol.t[-1]
            yy = np.linspace(T * 1e-3, T * 0.999, 2000)
            D = np.array([sol.sol(z)[3] - sol.sol(z)[2] for z in yy])
            signs.append((float(T), bool(np.all(D < 0)), bool(np.all(D > 0))))
            zeros += int(np.sum(np.sign(D[:-1]) * np.sign(D[1:]) < 0))
        out.append((e, al0, be0, k, signs, zeros))
    return out


def main():
    ex = k1_exact()
    print("K1 pure AdS5, exact: residuals of p', q', the constraint and alpha'/alpha = p on alpha = beta = exp(-e y),"
          " p = q = -e:", ex)
    ok1 = all(v == 0 for v in ex.values())
    print("   every level surface umbilic (D == 0), k = -e at every depth:", ok1)
    print("\nK2/K3 the balance detector (s2 of each convention along the column):")
    ok2 = ok3 = True
    for e, lab, name, d in k2_k3():
        print("  e=%-7.4g %-48s %-15s D_max/e=%.1e  s2(0)=%+.6f  spread=%.2e  everywhere=%s nowhere=%s crossings=%d" % (
            e, lab, name, d["D_max_rel"], d["s2_0"], d["s2_spread"], d["everywhere"], d["nowhere"], d["crossings"]))
        if lab.startswith("MUTATION"):
            ok3 &= d["D_max_rel"] > 1e-3 and d["s2_spread"] > 1e-3
        else:
            ok2 &= d["D_max_rel"] < 1e-9 and d["s2_spread"] < 1e-9 and (d["everywhere"] or d["nowhere"])
    print("  K2 verdict (pure AdS5: umbilic everywhere, s2 depth-independent, each condition everywhere or nowhere):", ok2)
    print("  K3 verdict (the mutation is caught: depth dependence and D > 0 on the corridor's column):", ok3)
    print("\nK4 positive control: the balance condition as a function of e (constraint at p = q = -s1 e):")
    pc = k4_positive()
    for key, v in pc.items():
        print("  alpha0=%.0f beta0=%.0f s1=%.2f: roots in e %s; identically zero: %s; max|residual| %.3g" % (
            key[0], key[1], key[2], [r if isinstance(r, str) else "%.12f" % r for r in v["roots"]],
            v["identically_zero"], v["max_abs"]))
    ok4 = (len(pc[(1.0, 2.0, 0.5)]["roots"]) == 1 and abs(pc[(1.0, 2.0, 0.5)]["roots"][0] - 1 / math.sqrt(24)) < 1e-12
           and pc[(1.0, 1.0, 1.0)]["identically_zero"] and not pc[(1.0, 1.0, 0.5)]["roots"]
           and not pc[(1.0, 1.0, 0.25)]["roots"])
    print("  1/sqrt(24) = %.12f; K4 verdict: %s" % (1 / math.sqrt(24), ok4))
    print("\nK5 one umbilic slice per column (start umbilic at y = 0, follow both ways):")
    ok5 = True
    for e, al0, be0, k, signs, zeros in k5_one_zero():
        (Tm, negm, posm), (Tp, negp, posp) = signs
        print("  e=%-6.4g alpha0=%.2f beta0=%.2f k=%.6f: y in [%.3f, 0): D<0 everywhere %s; y in (0, %.3f]: D>0 everywhere %s;"
              " other zeros %d" % (e, al0, be0, k, Tm, negm, Tp, posp, zeros))
        ok5 &= negm and posp and zeros == 0
    print("  K5 verdict:", ok5)
    allok = ok1 and ok2 and ok3 and ok4 and ok5
    print("\ncontrols:", "PASS" if allok else "FAIL")
    return allok


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
