#!/usr/bin/env python3
"""aug5.py -- [Hin26] section 10 in five dimensions: the augmentation of the zero energy operator and the decay of its
entries (N1STAR-PROOF.md section 10.39; ROUTES-OPEN.md 4.40; D102).  Labels: computed (exact, sympy), deduced, READ.

[Hin26] (arXiv:2606.28253v2) section 10 augments L-hat_b(sigma) by the columns L-hat_b(sigma)(i sigma^-1 g-dot^Ups_b)
and L-hat_b(sigma)(-sigma^-2 h_b,s1 + i sigma^-1 h-breve^1_b,s1) ((10.5)), whose entries at sigma = 0 are [L_b,
t*]g-dot^Ups_b and [L_b, t*]h-breve^1_b,s1 + (1/2)[[L_b, t*], t*]h_b,s1 ((10.7)-(10.8)); "The issue, however, is that
these entries only have r^-2 decay" ((10.9a)-(10.9b), pp. 201-202), "(Only terms arising from angular momentum
changes, [L_b, t*]g-dot^Ups_b(0, a-dot) in A^((3,0) u (3+E_ind)), have acceptable o(r^-2)-decay.)", whence his
improved states (Lemma 10.3), while for the angular momenta "g-dot^Ups,aug_b(0, a-dot) := chi_K g-dot^Ups_b(0, a-dot)"
((10.24a), p. 207), with "the index set at iota+ ... (4, 0) u (4 + E_ind)".  Here on the model -- 4+1 Minkowski in (T,
x), T = t - r, with sbar5.py's E^Ups (trace weight 2/3) and E^C, L-bar = D Ric + (delta* + E^C)(delta + E^Ups) G:

  A1 (computed, exact) The gauged stationary states. The mass state r^-2 (dt^2 + dr^2) plus delta* omega, omega = r^-1
     (a dt + b dr), a = -2 gam_Ups (e_Ups + 2)/(2 e_Ups gam_Ups^2 + 1), b = (1 - 4 gam_Ups^2)/(2 (2 e_Ups gam_Ups^2 +
     1)), and the rotation state r^-4 (dt (x) w + w (x) dt), w = x^1 dx^2 - x^2 dx^1, plus delta*(p r^-3 w), p = -4
     gam_Ups/3, are in the gauge and solve L-bar g-dot = 0, every parameter symbolic, at the symbolic point (X1, 0, X3,
     0) -- every orbit of the rotations of the planes 12 and 34, which L-bar commutes with and the states are invariant
     under, has a point there -- and the ansatz with log r dt and log r dr beside them returns their coefficients 0.
     Four-dimensional control (trace weight 1): the mass state r^-1 (dt^2 + dr^2) needs omega = c log r dt + b dr, c = 4
     gam_Ups (1 + e_Ups)/(4 e_Ups gam_Ups^2 + 1) -- the logarithm of his (8.19) -- and the rotation r^-3 (dt (x) w + w
     (x) dt) takes p = -2 gam_Ups, no logarithm. Controls: omega dropped (h claimed in the gauge); the four-dimensional
     mass state claimed gauged without the log.
  A2 (computed, exact) The entries.  [L-bar, T]g-dot = L-bar(T g-dot) is stationary, nonzero and homogeneous of degree
     -3 for the mass state and -4 for the rotation state, and [[L-bar, T], T]g-dot = 0; four dimensions: degrees -2 and
     -3, his (10.9a) and his angular momentum's (3, 0).  Control: the five-dimensional mass entry claimed of degree -2.
  A3 (computed, exact) The cutoff state.  For chi = chi(r/T), chi symbolic, L-bar(chi g-dot) = [L-bar, chi]g-dot is
     nonzero and homogeneous of degree -4 (mass) and -5 (rotation) in (T, x): iota+ order 4 and 5; four dimensions: 3
     -- his "iota+-decay order 3, which we must thus consider to be (borderline) unacceptable" (p. 202) -- and 4, his
     (10.24b).  Control: the five-dimensional mass state claimed of iota+ order 3.

Run: python3 aug5.py --selftest | --mutants | --only k [--verbose]   (about eight and four minutes).
"""
import sys
import time

import sympy as sp

import sbar5 as SB
from damping5 import Checklist
from sbar5 import v, eC, gC, eU, gU

HALF = sp.Rational(1, 2)
NUM = {v: sp.Rational(1, 3), eC: sp.Rational(1, 5), gC: 10, eU: sp.Rational(1, 7), gU: sp.Rational(3, 2)}
PTS = {4: [(1, 2, 2, 4), (2, 3, 6, 0), (2, 4, 4, 8)], 3: [(3, 4, 0), (2, 3, 6), (6, 8, 0)]}
A5 = -2 * gU * (eU + 2) / (2 * eU * gU**2 + 1)
B5 = (1 - 4 * gU**2) / (2 * (2 * eU * gU**2 + 1))
C4 = 4 * gU * (1 + eU) / (4 * eU * gU**2 + 1)
B4 = (1 - 4 * gU**2) / (4 * eU * gU**2 + 1)
P = {4: -sp.Rational(4, 3) * gU, 3: -2 * gU}


def ops(n):
    """L-bar = D Ric + (delta* + E^C) Ups, Ups(h) = (delta + E^Ups) G h, on (n+1)-Minkowski in (T, x)"""
    C = SB.Mink(n)
    N, e, d, m = C.N, C.eta, C.d, sp.Rational(2, n - 1)

    def dric(h):
        tr = C.tr(h)
        out = sp.zeros(N)
        for a in range(N):
            for b in range(a, N):
                s = -sum(e[c, c] * d(d(h[a, b], c), c) for c in range(N))
                s += sum(e[c, c] * (d(d(h[c, b], c), a) + d(d(h[c, a], c), b)) for c in range(N))
                s -= d(d(tr, a), b)
                out[a, b] = out[b, a] = s / 2
        return out

    def gauge(h):
        Gh = C.G(h)
        return [p + q for p, q in zip(C.delta(Gh), C.EU(Gh, m))]

    def L(h):
        w = gauge(h)
        return dric(h) + C.dstar(w) + C.EC(w, m)
    return C, gauge, L


def frame(C):
    x, r, N = C.x, C.r, C.N
    dt = [sp.Integer(1)] + [sp.Integer(0)] * C.n
    dr = [sp.Integer(0)] + [q / r for q in x]
    w = [0, -x[1], x[0]] + [0] * (C.n - 2)
    sym = lambda a, b: sp.Matrix(N, N, lambda i, j: (a[i] * b[j] + a[j] * b[i]) * HALF)
    return dt, dr, w, sym


def at(expr, C, pt, T=0, num=None):
    sub = {**dict(zip(C.x, pt)), C.T: T, **(num or {})}
    return sp.simplify(sp.sympify(expr).subs(sub))


def states(n, log=True, drop=False):
    """the gauged mass and rotation states; their gauge 1-forms solved on the ansatz, log terms allowed if log"""
    C, gauge, L = ops(n)
    r = C.r
    dt, dr, w, sym = frame(C)
    a, b, c, e, p, q = sp.symbols("a b c e p q")
    lg = sp.log(r) if log else 0
    hm = (sym(dt, dt) + sym(dr, dr)) * r**(-(n - 2))
    om = [r**(-(n - 3)) * (a * dt[i] + b * dr[i]) + lg * (c * dt[i] + e * dr[i]) for i in range(C.N)]
    hA = sym(dt, w) * (2 / r**n)
    oA = [(p + q * lg) * r**(-(n - 1)) * wi for wi in w]
    out = {}
    for name, h, om_, unk in (("mass", hm, om, (a, b, c, e)), ("rot", hA, oA, (p, q))):
        if drop:
            out[name] = (h, {})
            continue
        g = h + C.dstar(om_)
        eqs = [sp.expand(at(z, C, pt)) for pt in PTS[n][:2] for z in gauge(g)]
        sol = sp.solve([z for z in eqs if z != 0], unk, dict=True)
        if not sol:
            out[name] = (None, None)
            continue
        s0 = {u: sol[0].get(u, 0) for u in unk}
        out[name] = (g.subs(s0), s0)
    return C, gauge, L, out


# ------------------------------------------------------------------------------------------------- A1
def a1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    a, b, c, e, p, q = sp.symbols("a b c e p q")
    X1, X3 = sp.symbols("X1 X3", positive=True)
    for n in ((4,) if control == 1 else (3,) if control == 2 else (4, 3)):
        C, gauge, L, out = states(n, log=control != 2, drop=control == 1)
        gm, sm = out["mass"]
        gr, sr = out["rot"]
        if gm is None or gr is None:
            chk(f"n + 1 = {n + 1}: the states are gauged on the ansatz", False)
            continue
        if control != 1:
            if n == 4:
                form = all(sp.simplify(sm[k] - val) == 0 for k, val in ((a, A5), (b, B5), (c, 0), (e, 0)))
            else:
                form = all(sp.simplify(sm[k] - val) == 0 for k, val in ((b, B4), (c, C4), (e, 0)))
            form &= sp.simplify(sr[p] - P[n]) == 0 and sr[q] == 0
            chk(f"n + 1 = {n + 1}: the gauge 1-forms in closed form, mass {sm}, rotation {sr}", form)
        orb = (X1, 0, X3, 0)[:n]                           # every SO(2) x SO(2) orbit, up to reflection
        for name, g in (("mass", gm), ("rotation", gr)):
            t0 = time.time()
            Lg = L(g)
            zero = all(at(z, C, orb) == 0 for z in gauge(g))
            zero &= all(at(Lg[i, j], C, orb) == 0 for i in range(C.N) for j in range(i, C.N))
            chk(f"n + 1 = {n + 1}: the {name} state in the gauge and L-bar g-dot = 0 at (X1, 0, X3, 0), parameters "
                f"symbolic ({time.time() - t0:.0f}s)", zero)
    return chk.ok


# ------------------------------------------------------------------------------------------------- A2
def a2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in ((4,) if control else (4, 3)):
        C, gauge, L, out = states(n)
        T = C.T
        for name, k in (("mass", n - 2), ("rot", n - 1)):
            g = out[name][0]
            t0 = time.time()
            LT, LTT = L(T * g), L(T**2 * g)
            deg = k + 1 - (1 if control == 1 and name == "mass" else 0)
            M = [sp.Matrix(C.N, C.N, lambda i, j: at(LT[i, j], C, pt, num=NUM)) for pt in PTS[n]]
            M3 = sp.Matrix(C.N, C.N, lambda i, j: at(LT[i, j], C, PTS[n][0], T=3, num=NUM))
            dbl = all(at(LTT[i, j] - 2 * T * LT[i, j], C, pt, T=Tv, num=NUM) == 0
                      for pt in PTS[n][:2] for Tv in (0, 2) for i in range(C.N) for j in range(i, C.N))
            good = M[0] != sp.zeros(C.N) and M[1] != sp.zeros(C.N) and M3 == M[0]
            good &= (M[2] * 2**deg - M[0]).applyfunc(sp.simplify) == sp.zeros(C.N) and dbl
            chk(f"n + 1 = {n + 1}: [L-bar, T] on the {name} state stationary, nonzero, of degree -{deg}; "
                f"[[L-bar, T], T] = 0 (max entry at the first point {max(abs(z) for z in M[0])}; "
                f"{time.time() - t0:.0f}s)", good)
    return chk.ok


# ------------------------------------------------------------------------------------------------- A3
def a3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    chi = sp.Function("chi")
    for n in ((4,) if control else (4, 3)):
        C, gauge, L, out = states(n)
        T, r = C.T, C.r
        for name, k in (("mass", n - 2), ("rot", n - 1)):
            g = out[name][0]
            t0 = time.time()
            Lc = L(chi(r / T) * g)
            order = k + 2 - (1 if control == 1 and name == "mass" else 0)
            pt = PTS[n][0]
            r0 = sp.sqrt(sum(z**2 for z in pt))
            V1 = sp.Matrix(C.N, C.N, lambda i, j: at(Lc[i, j], C, pt, T=r0, num=NUM))
            V2 = sp.Matrix(C.N, C.N, lambda i, j: at(Lc[i, j], C, [2 * z for z in pt], T=2 * r0, num=NUM))
            good = V1 != sp.zeros(C.N) and (V2 * 2**order - V1).applyfunc(sp.simplify) == sp.zeros(C.N)
            chk(f"n + 1 = {n + 1}: L-bar(chi(r/T) g-dot) for the {name} state nonzero, homogeneous of degree "
                f"-{order} ({time.time() - t0:.0f}s)", good)
    return chk.ok


CHECKS = [("A1 the gauged mass and rotation states on the model; four dimensions: the log of his (8.19)", a1, 2),
          ("A2 [L-bar, T] g-dot of degree -3 (mass) and -4 (rotation), [[L-bar, T], T] g-dot = 0; four: -2, -3", a2, 1),
          ("A3 L-bar(chi(r/T) g-dot) of iota+ order 4 (mass) and 5 (rotation); four dimensions: 3 and 4", a3, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<112} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"aug5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"aug5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    verbose = "--verbose" in args
    if "--only" in args:
        k = int(args[args.index("--only") + 1])
        name, fn, nc = CHECKS[k - 1]
        print(name, "PASS" if fn(verbose=True) else "FAIL")
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    else:
        sys.exit(0 if selftest(verbose) else 1)
