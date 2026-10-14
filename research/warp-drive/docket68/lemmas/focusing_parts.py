#!/usr/bin/env python3
"""focusing_parts.py -- items 418-419: O1b and O1c at the large end, along the README's own parts.

M, 418: "if anything falls in it is still only every part of the one README from position 1" (H-ALL-IS-README).  M,
419: "Continue".  Every route through the object is a part of the README's route, through geometry the README's
earlier parts make.  The parts fall as radial null flux: the ingoing form in D dimensions,
    ds^2 = -f dv^2 + 2 dv dr + r^2 dOmega_(D-2)^2,   f = 1 - mu(v)/r^(D-3) - lam r^2,
mu(v) the README's mass function (the hole's mass is the README's, 136 G), lam the bulk's or plane's Lambda term.  D = 4
is the large end's plane, D = 5 the record's own form (arrival_small V1).  Labels: computed (exact unless marked),
deduced, READ.

  F1 (computed, exact; D = 4, 5) G_ab + Lambda g_ab has one component, (D - 2) mu'(v) / (2 r^(D-2)) on dv dv: the
     README's own flux, nothing else, with T_kk >= 0 on every null k iff mu' >= 0 (an arrival that only adds energy).
  F2 (computed, exact) Each part rides v = const: k = -d_r is an affinely parametrized null geodesic, its expansion
     theta = -(D - 2)/r, and Raychaudhuri's equation holds on it with R_kk = 0 (the flux is parallel to its own rays).
     So r is the part's affine parameter: from our face to the centre is a finite affine length, r at entry.
  F3 (computed, exact) The Kretschmann scalar is c_D mu^2 / r^(2(D-1)) (c_4 = 12, c_5 = 72; with lam = 0), mu' entering
     nowhere.  Along a part with some README mass inside it (mu(v) > 0), x = l5^2 sqrt(K) (quantum_onset.py) reaches
     one at r_q = (c_D mu^2 l^4)^(1/(2(D-1))) > 0, at a finite affine length before the centre: the part reaches 273's
     region with curvature finite all the way (O1b, O1c for that part).
  F4 (computed, exact) Without symmetry: for a twist-free null congruence with theta0 < 0 and R_kk >= 0,
     dtheta/dlambda <= -theta^2/(D - 2) brings theta to -infinity by lambda = (D - 2)/|theta0| (the comparison
     solution).  On a null k, Lambda gives R_kk = Lambda g_kk = 0 and the plane's tension S_ab = -sigma h_ab gives
     S_kk = 0; the README gives T_kk >= 0 (F1).  So in any dimension, whatever the core's exact geometry, every part
     reaches its focus in finite affine parameter (deduced from the computed pieces).
  F5 (computed) The earliest parts, with almost no README mass inside them (mu ~ 0), focus where curvature is small.
     Their centre stays behind our face if the face is born before the README's first part arrives (arrival_small V2,
     5D).  Here, for the smoothstep arrival mu(v) = r_h^(D-3) s(v/w) of onset order n, the event horizon is traced back
     from r_h at v = w (outgoing rays dr/dv = f/2), in clocks of r_h/c.  5D reproduces the record (the control); 4D
     gives the large end's plane its own widths.
  F6 (computed, exact) The 4D self-similar onset mu = lam v: outgoing rays r = X v obey 2 X^2 - X + lam = 0, so an
     escaping ray from the onset exists iff lam <= 1/8 (1/16 in m = mu/2: the four-dimensional threshold V3 names).

What this does not prove: the core's own geometry at the large end is not computed, so F3's curvature growth is exact
on the spherical forms and carried to the brane's core by F4's focusing (completeness), not by an exact curvature law;
F5's horizon is traced with the face static from v = w on (the record's 348 (Q3) qualification).
[Item 420, beside the text (core_face.py): the second closes, by 418 and independently (later infall only makes
the face born earlier; evaporation 4.4e-66 over the arrival).  The first is item 414's open core, (b2) and (c2),
located in the core r << ell: the deviation made at r ~ ell is of order one and, on a scalar proxy, survives inward.]
python3 focusing_parts.py [--selftest | --mutants]
"""
import sys
import numpy as np, sympy as sp

MUT = set()


def metric(D):
    v, r, lam = sp.symbols("v r lam", real=True)
    mu = sp.Function("mu")(v)
    ang = sp.symbols("a1:%d" % (D - 1), real=True)
    f = 1 - mu / r ** (D - (2 if "dimension" in MUT else 3)) - lam * r ** 2
    X = [v, r] + list(ang)
    g = sp.zeros(D, D)
    g[0, 0] = -f; g[0, 1] = g[1, 0] = 1
    w = r ** 2
    for i in range(D - 2):
        g[2 + i, 2 + i] = w
        w = w * sp.sin(ang[i]) ** 2
    return X, g, mu, lam, f


def curvature(X, g):
    D = len(X); gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(D)) / 2) for c in range(D)] for b in range(D)] for a in range(D)]
    def riem(a, b, c, d):
        return sp.simplify(sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
                           + sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(D)))
    Rm = {(a, b, c, d): riem(a, b, c, d) for a in range(D) for b in range(D) for c in range(D) for d in range(D)}
    Ric = sp.Matrix(D, D, lambda b, d: sp.simplify(sum(Rm[(a, b, a, d)] for a in range(D))))
    Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(D) for b in range(D)))
    return Gam, Rm, Ric, Rs, gi


def einstein_and_rays(D):
    """F1-F3 for dimension D"""
    X, g, mu, lam, f = metric(D)
    Gam, Rm, Ric, Rs, gi = curvature(X, g)
    Lam = sp.Rational((D - 1) * (D - 2), 2) * lam                       # lam r^2 in f is Lambda's term
    E = sp.simplify(Ric - Rs * g / 2 + Lam * g)
    nonzero = {(a, b): sp.simplify(E[a, b]) for a in range(D) for b in range(D) if sp.simplify(E[a, b]) != 0}
    # F2: k = -d_r, affine geodesic, expansion, Raychaudhuri
    k = [0, -1] + [0] * (D - 2)
    acc = [sp.simplify(sum(Gam[a][b][c] * k[b] * k[c] for b in range(D) for c in range(D))) for a in range(D)]
    sqrtg = sp.sqrt(sp.Abs(g.det()))
    theta = sp.simplify(sum(sp.diff(sqrtg * k[a], X[a]) for a in range(D)) / sqrtg)
    Rkk = sp.simplify(sum(Ric[a, b] * k[a] * k[b] for a in range(D) for b in range(D)))
    r = X[1]
    dtheta = sp.simplify(-sp.diff(theta, r))                              # d/dlambda along k = -d_r
    raych = sp.simplify(dtheta + theta ** 2 / (D - 2) + Rkk)
    # F3: Kretschmann at lam = 0
    Rl = {}
    K = 0
    for (a, b, c, d) in Rm:
        low = sum(g[a, e] * Rm[(e, b, c, d)] for e in range(D))      # lowered first: g is not diagonal
        if low == 0:
            continue
        up = sum(gi[b, p] * gi[c, q] * gi[d, s_] * Rm[(a, p, q, s_)] for p in range(D) for q in range(D)
                 for s_ in range(D))
        K += low * up
    K = sp.simplify(K.subs(lam, 0))
    return dict(nonzero=nonzero, acc=acc, theta=theta, Rkk=Rkk, raych=raych, K=K, mu=mu, r=r, v=X[0])


def focusing_bound():
    """F4: the comparison solution of dtheta/dlambda = -theta^2/(D - 2) and its blow-up"""
    l, th0, Dm2 = sp.symbols("lambda theta_0 Dm2")
    th = 1 / (1 / th0 + l / Dm2)
    ok = sp.simplify(sp.diff(th, l) + th ** 2 / Dm2) == 0 and sp.simplify(th.subs(l, 0) - th0) == 0
    lstar = sp.solve(sp.Eq(1 / th0 + l / Dm2, 0), l)[0]
    return ok, lstar


def smoothstep(n, xx):
    poly = {1: lambda t: t, 2: lambda t: 3 * t ** 2 - 2 * t ** 3, 3: lambda t: 10 * t ** 3 - 15 * t ** 4 + 6 * t ** 5,
            4: lambda t: 35 * t ** 4 - 84 * t ** 5 + 70 * t ** 6 - 20 * t ** 7}
    if "smooth" in MUT:
        poly[2] = lambda t: t ** 2
    t = min(max(xx, 0.0), 1.0)
    return poly[n](t)


def face_born(D, w, n):
    """F5: trace the event horizon back from (v = w, r = 1) along dr/dv = f/2, f = 1 - s(v/w)/r^(D-3) (r_h = 1), to
    v = 1e-5 w and 1e-8 w (LSODA, rtol 1e-12), and extrapolate r(0) = r(e2) - X e2 with X the slope between them.  Born
    before the onset if r(0) exceeds the integrator's floor, 1e-9 r_h, at v_b = -2 r(0) (the flat region before the
    onset); else born at the onset (returns 0).  Near a threshold r(0) collapses steeply to that floor (computed)."""
    from scipy.integrate import solve_ivp
    def rhs(v, y):
        r = max(y[0], 1e-100)
        return [0.5 * (1 - smoothstep(n, v / w) / r ** (D - 3))]
    e1, e2 = 1e-5 * w, 1e-8 * w
    r1 = solve_ivp(rhs, (w, e1), [1.0], method="LSODA", rtol=1e-12, atol=1e-16).y[0, -1]
    r2 = solve_ivp(rhs, (w, e2), [1.0], method="LSODA", rtol=1e-12, atol=1e-16).y[0, -1]
    if r2 <= 0:
        return 0.0
    X = (r1 - r2) / (e1 - e2); r0 = r2 - X * e2
    return -2 * r0 if r0 > 1e-9 else 0.0


def threshold(D, n, lo=0.05, hi=60.0):
    """the width w above which the face is born at the onset itself (bisection on face_born < 0)"""
    if face_born(D, hi, n) < 0:
        return None
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if face_born(D, mid, n) < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def self_similar_4d():
    X, lam = sp.symbols("X lam", positive=True)
    poly = 2 * X ** 2 - X + lam
    disc = sp.discriminant(poly, X)
    return poly, sp.solve(sp.Eq(disc, 0), lam)[0]


def report():
    for D in (4, 5):
        o = einstein_and_rays(D)
        print("D = %d: G + Lambda g nonzero only at %s = %s; theta = %s; R_kk = %s; Raychaudhuri residual %s; K = %s" % (
            D, list(o["nonzero"]), list(o["nonzero"].values()), o["theta"], o["Rkk"], o["raych"], o["K"]))
    ok, ls = focusing_bound(); print("F4 comparison solution exact: %s; focus by lambda = %s" % (ok, ls))
    for D in (5, 4):
        print("F5 D = %d: face born at v =" % D, "  ".join("w=%g n=%d: %+.3f" % (w, n, face_born(D, w, n))
                                                         for w in (0.5, 1, 4) for n in (1, 2, 3, 4)))
        print("      widest arrival with the face born before the onset:", "  ".join(
            "n=%d: %s" % (n, "always" if threshold(D, n) is None else "%.2f" % threshold(D, n)) for n in (1, 2, 3, 4)))
    poly, lc = self_similar_4d(); print("F6 4D self-similar onset: %s = 0 has a root iff lam <= %s" % (poly, lc))


def selftest(quiet=False):
    ok = []
    def say(m):
        if not quiet:
            print(m, flush=True)
    for D, cD in ((4, 12), (5, 72)):
        o = einstein_and_rays(D); mu, r, v = o["mu"], o["r"], o["v"]
        f1 = (list(o["nonzero"]) == [(0, 0)]
              and sp.simplify(o["nonzero"][(0, 0)] - (D - 2) * sp.diff(mu, v) / (2 * r ** (D - 2))) == 0)
        f2 = all(a == 0 for a in o["acc"]) and sp.simplify(o["theta"] + (D - 2) / r) == 0 and o["Rkk"] == 0 \
            and o["raych"] == 0
        f3 = sp.simplify(o["K"] - cD * mu ** 2 / r ** (2 * (D - 1))) == 0
        ok += [f1, f2, f3]
        say("F1-F3 D = %d: only the flux (D-2) mu'/(2 r^(D-2)) on dv dv: %s; the part's ray affine, theta = -(D-2)/r, "
            "Raychaudhuri with R_kk = 0: %s; K = %d mu^2/r^%d: %s" % (D, f1, f2, cD, 2 * (D - 1), f3))
    f4, ls = focusing_bound(); th0, Dm2 = sp.symbols("theta_0 Dm2")
    f4 = f4 and sp.simplify(ls + Dm2 / th0) == 0
    ok.append(f4); say("F4 the comparison solution, its focus at lambda = (D-2)/|theta0|: %s" % f4)
    # F5: the record's 5D control (arrival_small V2, V3) -- born before the onset for w <= 4 at every order, 1.76 to
    # 0.26 clocks before; at order 2 born at the onset from w = 9 exactly (V3's lambda = 3/w^2 <= 1/27)
    b5 = [face_born(5, w, n) for w in (0.5, 1, 4) for n in (1, 2, 3, 4)]
    t2 = threshold(5, 2)
    f5 = (all(b < 0 for b in b5) and abs(max(-b for b in b5) - 1.76) < 0.02 and abs(min(-b for b in b5) - 0.26) < 0.02
          and t2 is not None and abs(t2 - 9) < 0.15)
    t41 = threshold(4, 1)
    f5 = f5 and t41 is not None and abs(t41 - 8) < 0.15                  # the 4D linear onset: exact 1/w <= 1/8
    ok.append(f5); say("F5 control, 5D: born before the onset for w <= 4 at orders 1-4, %.2f to %.2f clocks before "
                       "(recorded 1.76 to 0.26); order 2 at the onset from w = %.2f (V3: 9); 4D order 1 from w = "
                       "%.2f (exact: 8): %s" % (max(-b for b in b5), min(-b for b in b5), t2 or -1, t41 or -1, f5))
    poly, lc = self_similar_4d()
    f6 = lc == sp.Rational(1, 8)
    ok.append(f6); say("F6 4D self-similar onset naked iff lam <= 1/8 (1/16 in m): %s" % f6)
    return all(ok)


def mutants():
    caught = 0; names = ["dimension", "smooth"]
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            r = selftest(quiet=True)
        except Exception:
            r = False
        caught += not r; print("mutant %-10s %s" % (m, "caught" if not r else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
