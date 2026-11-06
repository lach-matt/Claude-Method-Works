"""zinv5.py -- SETTLE-GLAM5 round 5: the round-3 verifier's independent check of (R3c), copied from its scratch
script (zcheck3.py) with a driver added; the computation is unchanged.

(R3c), invariant form  L_Z P(h) = DP(h)[L_Z h - 2h] - 2 mu d_mu P(h),  Z = (t - v1) d_t + r d_r, for
P(h) = Ric(g0 + h) - (1/2)(g_{m r} D0_n D^r + g_{n r} D0_m D^r), D^r = g^{ab}(Gam[g] - Gam[g0])^r_ab,
g0 = eta + mu r^-2 (dt + dr)^2 (5D Tangherlini, Kerr-Schild, polar coordinates).
h spherically symmetric with ARBITRARY component functions A, B, C, E of (t, r) (no smallness): the defect is
built symbolically (sympy, no simplification), then every jet of A..E up to order 3 is replaced by independent
random rationals and the point by exact values; the defect must vanish exactly (checked at 60 digits) for every
draw. Mutations (each must fail): m1 P + (3/10) h (mass term), m2 Z with 2 r d_r, m3 without the mu term, m4 gauge
term with g0^ab.
  ZI1 (computed) mode none: the defect vanishes (below 1e-50 against terms of size O(1)), five components.
  ZI2 (computed) controls m1-m4: each mutated identity fails (defect above 1e-3 in some component).
Labels: computed (sympy exact jets, evaluated at 60 digits). Run: python3 checks/zinv5.py (each mode is a separate
process, run in parallel; about forty minutes on a loaded machine); python3 checks/zinv5.py MODE runs one mode.
"""

import random
import sys
import sympy as sp

t, r, th, ph, ps = X = sp.symbols("t r theta phi psi", real=True)
mu, v1, eps = sp.symbols("mu v1 epsilon", real=True)
F = [sp.Function(n)(t, r) for n in "ABCE"]
n = 5
mut = sys.argv[1] if len(sys.argv) > 1 else "all"


def g0m(m):
    g = sp.zeros(5, 5)
    g[0, 0] = -1 + m/r**2; g[0, 1] = g[1, 0] = m/r**2; g[1, 1] = 1 + m/r**2
    g[2, 2] = r**2; g[3, 3] = r**2*sp.sin(th)**2; g[4, 4] = r**2*sp.sin(th)**2*sp.sin(ph)**2
    return g


def hm(a, b, c, e):
    h = sp.zeros(5, 5)
    h[0, 0] = a; h[0, 1] = h[1, 0] = b; h[1, 1] = c
    h[2, 2] = e*r**2; h[3, 3] = e*r**2*sp.sin(th)**2; h[4, 4] = e*r**2*sp.sin(th)**2*sp.sin(ph)**2
    return h


def inv(g):  # block (t, r) 2x2 plus diagonal angular part
    gi = sp.zeros(5, 5)
    det = g[0, 0]*g[1, 1] - g[0, 1]**2
    gi[0, 0] = g[1, 1]/det; gi[1, 1] = g[0, 0]/det; gi[0, 1] = gi[1, 0] = -g[0, 1]/det
    for i in (2, 3, 4):
        gi[i, i] = 1/g[i, i]
    return gi


def christ(g):
    gi = inv(g)
    dg = [[[sp.diff(g[a, b], X[c]) for c in range(n)] for b in range(n)] for a in range(n)]
    G = [[[sum(gi[a, d]*(dg[d][b][c] + dg[d][c][b] - dg[b][c][d]) for d in range(n) if gi[a, d] != 0)/2
           for c in range(n)] for b in range(n)] for a in range(n)]
    return gi, G


def P_op(g, g0, extra=None, gauge_inv=None):
    gi, G = christ(g)
    g0i, G0 = christ(g0)
    gg = gi if gauge_inv is None else g0i
    Ric = sp.zeros(n, n)
    for a in range(n):
        for b in range(a, n):
            v = sum(sp.diff(G[c][a][b], X[c]) for c in range(n)) - sum(sp.diff(G[c][a][c], X[b]) for c in range(n))
            v += sum(G[c][c][d]*G[d][a][b] - G[c][b][d]*G[d][a][c] for c in range(n) for d in range(n))
            Ric[a, b] = Ric[b, a] = v
    Dv = [sum(gg[a, b]*(G[q][a][b] - G0[q][a][b]) for a in range(n) for b in range(n) if gg[a, b] != 0)
          for q in range(n)]
    nab = [[sp.diff(Dv[q], X[m]) + sum(G0[q][m][l]*Dv[l] for l in range(n)) for q in range(n)] for m in range(n)]
    out = sp.zeros(n, n)
    for a in range(n):
        for b in range(a, n):
            out[a, b] = out[b, a] = Ric[a, b] - (sum(g[a, q]*nab[b][q] for q in range(n))
                                                 + sum(g[b, q]*nab[a][q] for q in range(n)))/2
    if extra is not None:
        out = out + extra
    return out


def lie(T, Zv):
    return sp.Matrix(n, n, lambda a, b: sum(Zv[c]*sp.diff(T[a, b], X[c]) for c in range(n))
                     + sum(T[c, b]*sp.diff(Zv[c], X[a]) + T[a, c]*sp.diff(Zv[c], X[b]) for c in range(n)))




def _driver():
    import subprocess
    modes = ["none", "m1", "m2", "m3", "m4"]
    procs = {m: subprocess.Popen([sys.executable, __file__, m], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                 text=True) for m in modes}
    res, fails = {}, []
    for m in modes:
        out = procs[m].communicate()[0]
        lines = [l for l in out.split("\n") if l.startswith("RESULT")]
        val = float(lines[-1].split("max defect")[1].split()[0]) if lines else float("nan")
        res[m] = val
        print(f"  mode {m}: max defect {val:.3e}")
    ok1 = res["none"] < 1e-50
    print(f"  ZI1 (R3c) holds exactly for arbitrary spherically symmetric h (mode none): {'pass' if ok1 else 'FAIL'}")
    ok2 = all(res[m] > 1e-3 for m in modes[1:])
    print(f"  ZI2 controls m1-m4 each fail: {'pass' if ok2 else 'FAIL'}")
    if not ok1:
        fails.append("ZI1")
    if not ok2:
        fails.append("ZI2")
    print("FAILED:", fails if fails else "none")
    return 1 if fails else 0


if mut == "all":
    sys.exit(_driver())
else:
    g0 = g0m(mu)
    h = hm(*F)
    Zv = [t - v1, (2 if mut == "m2" else 1)*r, 0, 0, 0]
    k = lie(h, Zv) - 2*h
    ex = (lambda hh: sp.Rational(3, 10)*hh) if mut == "m1" else (lambda hh: None)
    gi_flag = True if mut == "m4" else None
    Ph = P_op(g0 + h, g0, ex(h), gi_flag)
    Pk = P_op(g0 + h + eps*k, g0, ex(h + eps*k), gi_flag)
    comps = ((0, 0), (0, 1), (1, 1), (2, 2), (4, 4))
    defect = {}
    for (a, b) in comps:
        L = lie(Ph, Zv)[a, b] if False else (sum(Zv[c]*sp.diff(Ph[a, b], X[c]) for c in range(n))
                                             + sum(Ph[c, b]*sp.diff(Zv[c], X[a]) + Ph[a, c]*sp.diff(Zv[c], X[b])
                                                   for c in range(n)))
        D = sp.diff(Pk[a, b], eps).subs(eps, 0)
        M = 0 if mut == "m3" else 2*mu*sp.diff(Ph[a, b], mu)
        defect[(a, b)] = (L - D + M, L, M)
    random.seed(5)
    worst, size = 0, 0
    for draw in range(1):
        jet = {}
        for f in F:
            for i in range(4):
                for j in range(4 - i):
                    key = (f, i, j)
                    jet[key] = sp.Rational(random.randint(-30, 30), random.randint(1, 7))  # O(1)-O(30): not small
        pt = {t: sp.Rational(random.randint(-9, 9), 4), r: sp.Rational(random.randint(5, 20), 3),
              th: sp.pi/3, ph: sp.pi/5, mu: sp.Rational(random.randint(1, 9), 10), v1: sp.Rational(7, 10)}
        for key, (d, L, M) in defect.items():
            def ev(e):
                e = e.doit()
                ders = sorted([dd for dd in e.atoms(sp.Derivative)], key=lambda q: -len(q.variables))
                e = e.subs({dd: jet[(dd.expr, dd.variables.count(t), dd.variables.count(r))] for dd in ders})
                e = e.subs({f: jet[(f, 0, 0)] for f in F}).subs(pt)
                return sp.N(e, 60)
            dv, Lv, Mv = ev(d), ev(L), ev(M)
            worst = max(worst, abs(dv)); size = max(size, abs(Lv), abs(Mv))
            print(mut, draw, key, "defect", sp.N(dv, 6), "|L_Z P|", sp.N(Lv, 6), "|2 mu d_mu P|", sp.N(Mv, 6),
                  flush=True)
    print("RESULT", mut, "max defect", sp.N(worst, 6), "max size", sp.N(size, 6))
