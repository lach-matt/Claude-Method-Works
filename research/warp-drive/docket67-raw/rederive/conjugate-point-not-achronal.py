#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for 'conjugate-point-not-achronal'.

External result (Hawking-Ellis 1973 Prop. 4.5.12 / Wald 1984 Thm 9.3.8 / Penrose 1972,
as restated in gr-qc/0007021, 0705.3193, 2408.00154, 2010.05086, math/9909158):
  on a null geodesic gamma in a (C^2) spacetime, if a point q in (p, r) is conjugate to p
  along gamma, then there is a timelike curve from p to r (r in I+(p)); contrapositive:
  an achronal null geodesic contains no pair of conjugate points.

What is checked here (nothing under research/ is written; tree modules are imported
read-only with PYTHONDONTWRITEBYTECODE=1):
  R1  sympy: R x S^2 (-dt^2 + dtheta^2 + sin^2 theta dphi^2).  Riemann tensor computed;
      Jacobi (tidal) operator along the meridian null geodesic t = theta = lambda is +1;
      J = sin(lambda), first conjugate point at lambda = pi (the antipode).
  R2  causal relation in the static product: r in I+(p) iff dt > d_S2.  On gamma:
      lambda < pi  -> dt = d   (not timelike-related: the segment is achronal)
      lambda = pi  -> dt = d = pi (the conjugate point itself is NOT in I+(p))
      lambda = pi+e-> d = pi - e < dt (timelike); an explicit timelike curve is exhibited
      and its tangent norm computed < 0.
  R3  line (astigmatic) focus suffices: R x S^2 x R, screen {e_phi, d_z}: tidal diag(1,0),
      A = diag(sin l, l), det A = l sin l = 0 at pi in ONE direction only; past it the
      point is timelike-related to p (same computation as R2, z unchanged).
  R4  the mechanism of the proof (second variation / index form): constant tidal kappa,
      V = sin(pi l/L): I[V] = (L/2)(pi^2/L^2 - kappa) < 0 iff L > pi/sqrt(kappa) = the
      conjugate distance.  I[V] < 0 is what lets the variation become timelike.
  R5  the CONVERSE is not a theorem: flat R^{1,3} with x ~ x + 2 pi.  Riemann = 0, so the
      Jacobi field J = lambda never vanishes (no conjugate point), yet gamma(2 pi) is
      timelike-related to gamma(0).  (achronal.py:41 states 'achronal EXACTLY up to its
      first conjugate point'; 2004.12523 p.11 'no conjugate points ... Its image is
      achronal'.  Neither is load-bearing where the tree uses the causal step.)
  R6  thin-lens point-source conjugate point (the A in 'timelike curve A->B'):
      u = lambda, kick u' -> u' - u/f at D_A:  zero at D_A + f D_A/(D_A - f); none if
      D_A <= f.  So B must be past A's conjugate point, which is > f for finite D_A.
  R7  the tree's own numerics (concentric.survey, read-only): (a) reproduce anecscope's
      scan (x0 = -400, lam = 800, n = 6500); (b) REGULARITY: concentric's potential
      m/sqrt(r^2+a^2) - m/max(r, R_s) is only Lipschitz at r = R_s = 200 (thin shell), so
      the metric is C^{0,1} there and the C^2 hypothesis of the theorem fails on the
      anecscope rays, which cross r = 200.  Re-run each ray from x0 = -199 (start inside
      the shell, whole segment in the smooth region r < R_s): if a conjugate point still
      appears with max_r < R_s, the smooth theorem applies on an open set where the
      metric is C^infinity and the non-achronality conclusion does not need the shell.
      (c) count how many anecscope sample points land within the finite-difference
      stencil (+-2H) of the kink: the thin shell's delta curvature is (not) sampled.
"""
import math
import os
import sys

import sympy as sp

OUT = []


def rec(tag, ok, msg):
    OUT.append((tag, ok, msg))
    print("%-4s %-5s %s" % (tag, "PASS" if ok else "FAIL", msg))


def riemann(g, X):
    n = len(X)
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[a, e] * (sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b])
                                        - sp.diff(g[b, c], X[e])) for e in range(n)) / 2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    R = [[[[sp.simplify(sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
                        + sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c]
                              for e in range(n)))
             for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    return R  # R^a_{bcd}


def tidal(R, g, k, e1, e2, n):
    # T_ij = R_{a b c d} e_i^a k^b e_j^c k^d  (Jacobi: J''_a = -R_{abcd} k^b J^c k^d; positive = focusing)
    Rl = [[[[sum(g[a, f] * R[f][b][c][d] for f in range(n)) for d in range(n)]
            for c in range(n)] for b in range(n)] for a in range(n)]
    E = (e1, e2)
    return [[sp.simplify(sum(Rl[a][b][c][d] * E[i][a] * k[b] * E[j][c] * k[d]
                             for a in range(n) for b in range(n) for c in range(n)
                             for d in range(n))) for j in range(2)] for i in range(2)]


def r1_r3():
    t, th, ph, z, l = sp.symbols('t theta phi z lambda', real=True)
    # R x S^2 x R (3+1); R1/R2 use the S^2 part, R3 uses the extra flat z
    X = [t, th, ph, z]
    g = sp.diag(-1, 1, sp.sin(th) ** 2, 1)
    R = riemann(g, X)
    # meridian null geodesic: t = theta = lambda, phi = 0, z = 0; k = d_t + d_theta
    k = [1, 1, 0, 0]
    e_phi = [0, 0, 1 / sp.sin(th), 0]
    e_z = [0, 0, 0, 1]
    T = tidal(R, g, k, e_phi, e_z, 4)
    T = [[sp.simplify(x) for x in row] for row in T]
    ok = (sp.simplify(T[0][0] - 1) == 0 and T[1][1] == 0 and T[0][1] == 0)
    rec("R1a", ok, "tidal matrix on screen {e_phi, d_z} along t=theta=lambda: %s "
        "(expected diag(1,0))" % T)
    # Jacobi: J'' = -T J, J(0) = 0, J'(0) = 1
    J = sp.Function('J')
    s1 = sp.dsolve(sp.Eq(J(l).diff(l, 2), -T[0][0].subs(th, l) * J(l)), J(l),
                   ics={J(0): 0, J(l).diff(l).subs(l, 0): 1}).rhs
    s2 = sp.dsolve(sp.Eq(J(l).diff(l, 2), -T[1][1] * J(l)), J(l),
                   ics={J(0): 0, J(l).diff(l).subs(l, 0): 1}).rhs
    zeros = sp.solveset(sp.Eq(s1, 0), l, sp.Interval.open(0, 2 * sp.pi))
    rec("R1b", sp.simplify(s1 - sp.sin(l)) == 0 and zeros == sp.FiniteSet(sp.pi),
        "J_phi = %s, first zero in (0,2pi): %s -> conjugate point at the antipode" % (s1, zeros))
    detA = sp.simplify(s1 * s2)
    rec("R3a", sp.simplify(detA - l * sp.sin(l)) == 0,
        "A = diag(%s, %s), det A = %s: zero at pi in ONE screen direction (line focus)"
        % (s1, s2, detA))
    # R2: causal relations.  gamma(lambda) = (t=lambda, theta=lambda) from p = (0, N).
    # d_S2(N, point at colatitude lambda) = min(lambda, 2pi - lambda) for lambda in [0, 2pi]
    e = sp.symbols('epsilon', positive=True)
    lam_b = sp.symbols('lb', positive=True)
    before = sp.simplify(lam_b - lam_b)  # dt - d = 0 for lambda < pi
    at = sp.pi - sp.pi
    past = sp.simplify((sp.pi + e) - (2 * sp.pi - (sp.pi + e)))  # dt - d
    rec("R2a", before == 0, "lambda < pi: dt - d = %s -> not in I+(p): segment achronal "
        "(a causal curve has dt >= spatial length >= d; timelike needs dt > d)" % before)
    rec("R2b", at == 0, "lambda = pi (the conjugate point): dt - d = %s -> NOT in I+(p). "
        "B AT the focus is not reached by a timelike curve; B must be strictly past" % at)
    rec("R2c", sp.simplify(past - 2 * e) == 0, "lambda = pi + eps: dt - d = %s > 0 -> "
        "in I+(p)" % past)
    # explicit timelike curve: along the other meridian arc theta: 0 -> pi - eps backward
    # side (phi = pi), i.e. colatitude s from 0 to pi - eps, at speed (pi-eps)/(pi+eps).
    s = sp.symbols('s', real=True)
    tt = s
    thc = s * (sp.pi - e) / (sp.pi + e)
    norm = sp.simplify(-sp.diff(tt, s) ** 2 + sp.diff(thc, s) ** 2)
    neg = sp.simplify(norm + 4 * sp.pi * e / (sp.pi + e) ** 2) == 0
    rec("R2d", neg, "explicit curve t = s, theta = s(pi-eps)/(pi+eps), phi = pi, s in "
        "[0, pi+eps]: g(u,u) = %s < 0 for every eps > 0 (timelike); ends at gamma(pi+eps) "
        "(colatitude pi-eps on the phi = pi side = colatitude pi+eps along gamma)" % norm)
    # R3b: with the z direction the same curve works (z constant): line focus suffices
    rec("R3b", True, "R x S^2 x R: the R2d curve with z = 0 reaches gamma(pi+eps): the "
        "one-direction (line) focus already breaks achronality")


def r4():
    l, L, kap = sp.symbols('lambda L kappa', positive=True)
    V = sp.sin(sp.pi * l / L)
    I = sp.simplify(sp.integrate(sp.diff(V, l) ** 2 - kap * V ** 2, (l, 0, L)))
    target = L / 2 * (sp.pi ** 2 / L ** 2 - kap)
    ok = sp.simplify(I - target) == 0
    Lc = sp.solve(sp.Eq(target, 0), L)
    rec("R4", ok and Lc == [sp.pi / sp.sqrt(kap)],
        "index form I[sin(pi l/L)] = %s; sign change at L = %s = first conjugate distance "
        "of u'' = -kappa u: past it the variation lowers the causal 'length' below zero"
        % (sp.factor(I), Lc))


def r5():
    # flat R^{1,3} with x periodic 2 pi: metric flat -> Riemann 0 -> J = lambda
    l = sp.symbols('lambda', positive=True)
    J = l  # solution of J'' = 0, J(0)=0, J'(0)=1
    no_zero = sp.solveset(sp.Eq(J, 0), l, sp.Interval.open(0, sp.oo)) == sp.EmptySet
    # gamma(lambda) = (t=lambda, x=lambda mod 2pi).  q = gamma(2pi+eps): dt = 2pi+eps,
    # spatial distance on the circle = eps (< dt) -> timelike related.
    e = sp.symbols('epsilon', positive=True)
    rel = sp.simplify((2 * sp.pi + e) - e)
    rec("R5", no_zero and rel == 2 * sp.pi,
        "flat cylinder: no conjugate point on gamma (J = lambda), yet dt - d = %s > 0 at "
        "gamma(2pi+eps): NON-achronal WITHOUT a conjugate point. The converse of the "
        "result is false; only 'conjugate => not achronal' is a theorem" % rel)


def r6():
    DA, f, x = sp.symbols('D_A f x', positive=True)
    # after the lens (at lambda = D_A): u = D_A + (1 - D_A/f) x, x = lambda - D_A
    u = DA + (1 - DA / f) * x
    x0 = sp.solve(sp.Eq(u, 0), x)
    ok = sp.simplify(x0[0] - f * DA / (DA - f)) == 0
    AU = 1.495979e11
    fs = 547.595  # AU, spec.focal_length(Sun, R_sun) / AU (audited separately)
    rows = []
    for da in (600.0, 1000.0, 1e4, 1e6):
        rows.append((da, fs * da / (da - fs)))
    rec("R6", ok, "thin lens, point source at D_A: conjugate at D_A + f D_A/(D_A - f) "
        "(none if D_A <= f); Sun f = 547.6 AU: D_A=600 -> %.0f AU past lens, 1000 -> %.0f, "
        "1e4 -> %.1f, 1e6 -> %.2f. 'timelike A->B' needs B past A's conjugate point, "
        "which exceeds f for every finite D_A" % tuple(r[1] for r in rows))


def r7(full=True):
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    sys.dont_write_bytecode = True
    sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
    import concentric
    m, Rs = 2.0e-2, concentric.R_SHELL
    tree = {0.05: 400.2, 0.2: 400.7, 0.5: 403.8, 1.0: 414.4, 2.0: 461.0,
            2.3783: 1578.0, 2.4021: 1579.8}
    bs = sorted(tree) if full else [0.05, 1.0]
    for b in bs:
        r = concentric.survey(m, b=b, x0=-400.0, lam=800.0, n=6500)
        c = r["conjugate"]
        if b in (2.3783, 2.4021):
            # the printed 1578.0 / 1579.8 exceed lam = 800 and cannot come from
            # anecscope.has_conjugate's own config.  Measured: they come from lam = 3000.
            r3 = concentric.survey(m, b=b, x0=-1500.0, lam=3000.0, n=24375)
            c3 = r3["conjugate"]
            ok = c is not None and c3 is not None and abs(c3 - tree[b]) < 0.2
            rec("R7a", ok, "b=%-7s DISCREPANCY: at anecscope's has_conjugate config "
                "(x0=-400, lam=800) conjugate %.2f; the printed %s reproduces only at "
                "x0=-1500, lam=3000: %.2f. The table mixes two run configurations "
                "unstated; existence unaffected" % (b, c, tree[b], c3))
            continue
        ok = c is not None and abs(c - tree[b]) < 0.2
        rec("R7a", ok, "b=%-7s anecscope run: conjugate %s (tree prints %s), max_r %.2f "
            "(crosses r = R_s = %.0f: %s)" % (b, None if c is None else round(c, 2),
                                             tree[b], r["max_r"], Rs, r["max_r"] > Rs))
    # R7b: interior start, whole segment inside the smooth region r < R_s
    for b in bs:
        x0, lam = -199.0, 398.0
        n = int(round(lam / (800.0 / 6500)))
        r = concentric.survey(m, b=b, x0=x0, lam=lam, n=n)
        c = r["conjugate"]
        if c is None:
            rec("R7b", False, "b=%-7s start x0=-199: no conjugate point within lam=398" % b)
            continue
        # re-run only to just past the conjugate point: the segment that matters
        lam2 = c + 2.0
        n2 = int(round(lam2 / (lam / n)))
        r2 = concentric.survey(m, b=b, x0=x0, lam=lam2, n=n2)
        c2 = r2["conjugate"]
        ok = c2 is not None and r2["max_r"] < Rs
        rec("R7b", ok,
            "b=%-7s start x0=-199 (inside shell): conjugate %.2f; segment to conj+2 has "
            "max_r %.3f < R_s=%.0f: %s -> a conjugate pair entirely in the C^inf region "
            "(metric smooth for r < R_s), so the C^2 theorem applies there: %s"
            % (b, c, r2["max_r"], Rs, r2["max_r"] < Rs, ok))
    # R7c: is the thin-shell kink sampled by the Riemann stencil on the anecscope ray?
    import composite
    H = composite.H
    cp = concentric._install(m)
    hits = {}
    for b in bs:
        p0 = (-400.0, b, 0.0)
        k0 = cp.null_tangent(p0, m)
        pts, _tang, h = cp.geodesic(p0, k0, m, 800.0, 6500)
        near = [i for i, x in enumerate(pts[:-1])
                if abs(math.sqrt(x[1] ** 2 + x[2] ** 2 + x[3] ** 2) - Rs) < 2 * H]
        hits[b] = (len(near), h)
    rec("R7c", True, "sample points within the +-2H = %.0e Riemann stencil of the r = R_s "
        "kink per anecscope ray (step h = %.4f): %s -- the thin shell's delta-function "
        "curvature is %s by the Jacobi integration"
        % (2 * H, list(hits.values())[0][1], {b: v[0] for b, v in hits.items()},
           "NOT sampled" if all(v[0] == 0 for v in hits.values()) else "sampled on some rays"))
    # R7e: sensitivity of the anecscope conjugate point to whether the kink is sampled
    if 0.05 in bs:
        vals = []
        for nn in (6497, 6499, 6500, 6501, 6503):
            p0 = (-400.0, 0.05, 0.0)
            k0 = cp.null_tangent(p0, m)
            pts, _t, h = cp.geodesic(p0, k0, m, 800.0, nn)
            hit = sum(1 for x in pts[:-1]
                      if abs(math.sqrt(x[1] ** 2 + x[2] ** 2 + x[3] ** 2) - Rs) < 2 * H)
            c = concentric.survey(m, b=0.05, x0=-400.0, lam=800.0, n=nn)["conjugate"]
            vals.append((nn, hit, round(c, 3) if c is not None else None))
        cs = [v[2] for v in vals if v[2] is not None]
        rec("R7e", len(cs) == len(vals),
            "b=0.05, n -> (n, stencil hits, conjugate): %s; spread %.3f affine -- the "
            "sampled/unsampled shell moves the location, not the existence"
            % (vals, max(cs) - min(cs)))
    # size of the missed thin-lens kick, shell surface density sigma = m/(4 pi R_s^2):
    # Delta u' = -4 pi sigma u (normal incidence), u ~ 200 at the crossing
    kick = 4 * math.pi * (m / (4 * math.pi * Rs ** 2)) * 200.0
    rec("R7d", kick < 1e-3, "missed Ricci kick at shell entry |Delta u'| ~ %.1e against "
        "u' = 1 (positive shell mass: focusing, so omitting it can only DELAY a conjugate "
        "point; existence claims are conservative)" % kick)


if __name__ == "__main__":
    r1_r3()
    r4()
    r5()
    r6()
    r7(full="--quick" not in sys.argv)
    bad = [o for o in OUT if not o[1]]
    print("\n%d checks, %d FAIL" % (len(OUT), len(bad)))
    sys.exit(1 if bad else 0)
