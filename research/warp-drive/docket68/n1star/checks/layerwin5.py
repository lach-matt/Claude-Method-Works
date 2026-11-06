#!/usr/bin/env python3
"""layerwin5.py -- the window of EQUALITY5-LAYER.md: where, near the flat edge of a C_c^inf envelope, the order-lam^3
term linear in the wave dominates the margin and every error term (Lemma L.5, Lemma L.6, Theorem L's exponent ledger).

  W1 (computed, exact constants; sampled) Lemma L.5, the interpolation bound on a half-line: for f smooth, f = 0 on
     (-inf, v_s], E(v) := sup_{(-inf, v]} |f| and M_m(v) := sup_{(-inf, v]} |f^(m)|,
         sup_{(-inf, v]} |f^(i)| <= C_{i,m} E(v)^(1 - i/m) M_m(v)^(i/m),   C_{i,m} := Lambda_{i,m} + (m - 1)^(m - i),
     Lambda_{i,m} the sum of |l_k^(i)(0)| over the Lagrange basis on the nodes 0, -1, ..., -(m - 1) (computed exactly).
     Checked on a grid of (0, 0.3] for f = exp(-1/x) at (i, m) = (1, 6), (3, 6), (2, 8).  Control: the bound without
     the interpolation, sup |f^(i)| <= C E(v) (exponent 1 in place of 1 - i/m), fails near the edge (f'/f = 1/x^2).
  W2 (computed, a model with every constant set to 1) Lemma L.6 and Theorem L's window, for three C_c^inf edges:
     exp(-1/x); exp(-1/x^2); exp(-1/x) sin^2(pi/x) (zeros accumulating at the edge).  For lam = 10^-4, ..., 10^-32 and
     the level y = lam^p (p = 14), v* := the first point where the running maximum E reaches y, the window [v*, v* +
     4 pi lam]; on it env lies in [y/2, 2y], and the ratio
         rho := (m0 + lam^4 e3 + lam e3^2 + lam^(N-k0) e3) / (lam^3 min env),   e3 := sup_{[0, v* + 5 pi lam]} sum_{i<=3}
     |env^(i)|, N - k0 = 4, m0 the margin (0.2) with A = mu0 = 1,
     is printed; it decreases to 0 as lam -> 0 (the model of Theorem L's dominance), and at the two smallest lam the
     window has env in [y/2, 2y] and lies in the layer, (2/9) int_0^(v*+4 pi lam) env^2 < lam/100 (at lam = 10^-4 the
     window is not yet narrow against the edge scale: "lam small enough" is part of the statement).  Controls: the
     level y = lam^2 (m0 dominates: rho grows as lam -> 0), and the coefficient K = 0 (no linear term: rho infinite).
  W3 (computed, exact rationals) Theorem L's exponent ledger: with y = lam^p, Landau's index m and the derivative count
     M of the construction's flat-edge bounds, the conditions (e1)-(e6) of the note hold at p = 14, m = 56 M for every
     M in {8, 64, 1024} once N - k0 >= 4, and also in the exceptional case rho0 in Z_K (exponent 1 + 2/kap on the
     signal, kap = 64).  Control: N - k0 = 3 violates (e4).

Labels: computed.  W2 is a qualitative model: it checks the arithmetic of the dominance with unit constants and three
derivatives (e3), not the M* = 2N + 8 = 26 of the proof (with 26 the exp(-1/x) model needs far smaller lam:
layerband5.py B3), and not Theorem L's constants, which are not evaluated (lamL5.py).
Run: python3 checks/layerwin5.py  (about a minute)
"""
import sys
from fractions import Fraction as Fr

import mpmath as mp
import sympy as sp
import builtins                                                                   # noqa: E402
import textwrap                                                                   # noqa: E402


def print(*args, **kw):                                                           # noqa: A001
    """the builtin print, wrapped at 121 columns (Round 3: every file within 121 characters)"""
    builtins.print(textwrap.fill(" ".join(str(a) for a in args), width=121, subsequent_indent="      ",
                                 break_on_hyphens=False), **kw)

mp.mp.dps = 80


def lagrange_const(i, m):
    x = sp.symbols('x')
    nodes = [-k for k in range(m)]
    tot = 0
    for k, xk in enumerate(nodes):
        lk = sp.prod([(x - xj)/(xk - xj) for j, xj in enumerate(nodes) if j != k])
        tot += abs(sp.diff(lk, x, i).subs(x, 0))
    return tot + (m - 1)**(m - i)


def d_env(x, i):
    return mp.diff(lambda y: mp.e**(-1/y), x, i)


def w1(control=False):
    ok = True
    for (i, m) in ((1, 6), (3, 6), (2, 8)):
        C = lagrange_const(i, m)
        grid = [mp.mpf(k)/400 for k in range(4, 121)]
        Mm, worst, sup_i = mp.mpf(0), mp.mpf(0), mp.mpf(0)
        for x in grid:
            Mm = max(Mm, abs(d_env(x, m)))
            sup_i = max(sup_i, abs(d_env(x, i)))
            E = mp.e**(-1/x)
            rhs = C*E if control else C*E**(1 - mp.mpf(i)/m)*Mm**(mp.mpf(i)/m)
            worst = max(worst, sup_i/rhs)
        good = worst <= 1
        ok &= good
        print("  W1%s (i, m) = (%d, %d): C = %s, max over the grid of lhs/rhs = %s"
              % (" control" if control else "", i, m, C, mp.nstr(worst, 5)), flush=True)
    return ok


ENVS = {"exp(-1/x)": lambda x: mp.e**(-1/x),
        "exp(-1/x^2)": lambda x: mp.e**(-1/x**2),
        "exp(-1/x) sin^2(pi/x)": lambda x: mp.e**(-1/x)*mp.sin(mp.pi/x)**2}


def first_reach(f, y, hi=mp.mpf('0.5')):
    """first point where the running maximum of f on (0, .] reaches y: scan down to the first sample >= y, refine"""
    xs = [hi*mp.mpf(2)**(-k/mp.mpf(64)) for k in range(0, 64*40)]
    xs = sorted(xs)
    prev = None
    for x in xs:
        if f(x) >= y:
            lo = prev if prev is not None else x/2
            # the running max first reaches y on (lo, x]; bisect on max(f) over a fine sub-grid
            a, b = lo, x
            for _ in range(200):
                mid = (a + b)/2
                sub = [a + (mid - a)*k/16 for k in range(17)]
                if max(f(z) for z in sub) >= y:
                    b = mid
                else:
                    a = mid
            return b
        prev = x
    return None


def w2(p=14, K=1, control_name=""):
    rows, ok = [], True
    for name, f in ENVS.items():
        ratios, flags = [], []
        for e in (4, 8, 16, 32):
            lam = mp.mpf(10)**(-e)
            y = lam**p
            vs = first_reach(f, y)
            L = 4*mp.pi*lam
            win = [vs + L*k/64 for k in range(65)]
            envs = [f(z) for z in win]
            lo, hi = min(envs), max(envs)
            ext = [vs + 5*mp.pi*lam*k/32 for k in range(33)] + [vs*k/64 for k in range(1, 65)]
            e3 = max(sum(abs(mp.diff(f, z, i)) for i in range(4)) for z in ext)
            mass = mp.mpf(2)/9*mp.quad(lambda z: f(z)**2, [0, vs/2, vs + L])
            m0 = mp.sqrt(1 + mass) - 1 + (1 + mass)**mp.mpf(-0.75)*mp.mpf(2)/9*hi**2/2
            num = m0 + lam**4*e3 + lam*e3**2 + lam**4*e3
            rho = num/(lam**3*lo*K) if K else mp.inf
            ratios.append(rho)
            flags.append((lo >= y/2) and (hi <= 2*y) and (mass < lam/100))
        dec = all(ratios[k + 1] < ratios[k] for k in range(len(ratios) - 1)) and ratios[-1] < mp.mpf('1e-2')
        ok &= dec and flags[-1] and flags[-2]
        rows.append(name)
        print("  W2%s %-22s rho at lam = 1e-4, 1e-8, 1e-16, 1e-32: %s; window in [y/2, 2y] and in the layer: %s"
              % (control_name, name, ", ".join(mp.nstr(x, 3) for x in ratios), flags), flush=True)
    return ok


def ledger(p, m_over_M, M, Nk0, kap=None):
    """the exponent conditions (e1)-(e6) of the note, exact; kap: the exceptional case (signal exponent 1 + 2/kap)"""
    p, M = Fr(p), Fr(M)
    m = m_over_M*M
    q0 = Fr(6)
    s = p*(1 + (Fr(2, kap) if kap else 0))         # the signal is lam^3 y^(1 + 2/kap)
    c = {"e1 m0 = O(y^2)": 2*p > 3 + s,
         "e2 lam^4 e_M": 4 + p*(1 - M/m) > 3 + s,
         "e3 quadratic parts": 1 + 2*p*(1 - M/m) > 3 + s,
         "e4 the remainder w": Nk0 + p*(1 - M/m) > 3 + s,
         "e5 Landau window": p/m < 1,
         "e6 L.4's hypothesis": p*(1 - M/m) > q0}
    return c


def w3():
    ok = True
    for M in (8, 64, 1024):
        for kap in (None, 64):
            c = ledger(14, 56, M, 4, kap)
            ok &= all(c.values())
    c = ledger(14, 56, 64, 4)
    print("  W3 p = 14, m = 56 M, N - k0 = 4: " + "; ".join("%s %s" % (k, v) for k, v in c.items()), flush=True)
    return ok


def w3_control():
    c = ledger(14, 56, 64, 3)
    print("  W3 control N - k0 = 3: (e4) holds: %s" % c["e4 the remainder w"], flush=True)
    return all(c.values())


def main():
    ok = True
    g, ctl = w1(), w1(control=True)
    print("W1 %s" % ("PASS" if g and not ctl else "FAIL"), flush=True)
    ok &= g and not ctl
    g = w2()
    c1 = w2(p=2, control_name=" control y = lam^2")
    c2 = w2(K=0, control_name=" control K = 0")
    print("W2 %s" % ("PASS" if g and not c1 and not c2 else "FAIL"), flush=True)
    ok &= g and not c1 and not c2
    g, ctl = w3(), w3_control()
    print("W3 %s" % ("PASS" if g and not ctl else "FAIL"), flush=True)
    ok &= g and not ctl
    print("layerwin5: %s" % ("all checks pass, every control fails" if ok else "FAILURES"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
