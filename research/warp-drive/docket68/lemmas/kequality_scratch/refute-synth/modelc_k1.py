#!/usr/bin/env python3
"""Independent re-derivation (refute pass) of Model C's k = 1 two-plane balance with the bridge's ell_s FREE.

Bulk: f_j(r) = k + r^2/ell_j^2 - mu_j/r^2, k = 1.  Static plane at r = R, per-sheet Israel, normals into kept sides:
  TENSION  lam R = sum_j eps_j sqrt(f_j(R))          (lam = kappa^2 sigma / 3)
  BALANCE  sum_j eps_j (k - 2 mu_j/R^2)/sqrt(f_j(R)) = 0
eps = +1 when the kept side is r < R ('decaying'), -1 when r > R ('growing').
Ours: bridge side (ell_s, mu) decaying + own bulk (ell_1 = 1, mu = 0) decaying, tension lam1.
Position 2: bridge side decaying + own bulk (ell_2 = c, mu = 0) growing, tension lam2 = ratio * lam1.
Elimination is exact: each plane gives (mu, w = 1/ell_s^2) as rational functions of a rational parameter for R,
then a resultant gives a univariate polynomial whose real roots are ALL candidate solutions (exhaustive).
"""
import sys
import sympy as sp
import mpmath as mp

mp.mp.dps = 60
z, y = sp.symbols("z y", positive=True)


def plane_curves(lam1, ratio, c):
    R = 2 * z / (1 - z**2)
    t = (1 + z**2) / (1 - z**2)                 # sqrt(1 + R^2), exact for 0 < z < 1
    s = lam1 * R - t
    mu1 = lam1 * R**3 / (2 * t)                  # from BALANCE with the TENSION substituted
    w1 = (s**2 - 1 + mu1 / R**2) / R**2
    R2 = 2 * c * y / (1 - y**2)
    t2 = (1 + y**2) / (1 - y**2)                 # sqrt(1 + R2^2/c^2)
    lam2 = ratio * lam1
    s2 = t2 + lam2 * R2
    mu2 = -lam2 * R2**3 / (2 * t2)
    w2 = (s2**2 - 1 + mu2 / R2**2) / R2**2
    return dict(R=R, t=t, s=s, mu1=mu1, w1=w1, R2=R2, t2=t2, s2=s2, mu2=mu2, w2=w2)


def residuals(lam1, ratio, c, R1, R2, mu, ell_s):
    """Direct (unsquared) residuals of the four junction equations, as an independent check."""
    lam2 = ratio * lam1
    fs = lambda r: 1 + r**2 / ell_s**2 - mu / r**2
    f1 = lambda r: 1 + r**2
    f2 = lambda r: 1 + r**2 / c**2
    e1 = mp.sqrt(fs(R1)) + mp.sqrt(f1(R1)) - lam1 * R1
    e2 = (1 - 2 * mu / R1**2) / mp.sqrt(fs(R1)) + 1 / mp.sqrt(f1(R1))
    e3 = mp.sqrt(fs(R2)) - mp.sqrt(f2(R2)) - lam2 * R2
    e4 = (1 - 2 * mu / R2**2) / mp.sqrt(fs(R2)) - 1 / mp.sqrt(f2(R2))
    return [e1, e2, e3, e4]


def solve(lam1, ratio, c, verbose=True):
    d = plane_curves(lam1, ratio, c)
    P = sp.numer(sp.together(d["mu1"] - d["mu2"]))
    Q = sp.numer(sp.together(d["w1"] - d["w2"]))
    P = sp.Poly(sp.expand(P), y)
    Q = sp.Poly(sp.expand(Q), y)
    res = sp.resultant(P.as_expr(), Q.as_expr(), y)
    res = sp.Poly(sp.factor(res), z) if res != 0 else None
    sols = []
    if res is None:
        return "RESULTANT-ZERO", sols
    for fac, _ in sp.factor_list(res.as_expr())[1]:
        fz = sp.Poly(fac, z)
        if fz.degree() < 1:
            continue
        for rr in sp.real_roots(fz):
            zv = mp.mpf(sp.N(rr, 80))
            if not (0 < zv < 1):
                continue
            # back-substitute: roots y of P(z0, y) in (0,1) that also zero Q
            Pz = sp.Poly(P.as_expr().subs(z, sp.Float(sp.N(rr, 80), 80)), y)
            for yv in sp.Poly(Pz, y).nroots(n=50, maxsteps=500):
                if abs(sp.im(yv)) > 1e-30:
                    continue
                yv = mp.mpf(sp.re(yv))
                if not (0 < yv < 1):
                    continue
                # polish both with findroot on the 2x2 system
                F = sp.lambdify((z, y), [d["mu1"] - d["mu2"], d["w1"] - d["w2"]], "mpmath")
                try:
                    zz, yy = mp.findroot(lambda a, b: F(a, b), (zv, yv))
                except Exception:
                    continue
                vals = {k: sp.lambdify((z, y), v, "mpmath")(zz, yy) for k, v in d.items()}
                if abs(vals["mu1"] - vals["mu2"]) > mp.mpf(10)**-40 or abs(vals["w1"] - vals["w2"]) > mp.mpf(10)**-40:
                    continue
                adm = vals["s"] > 0 and vals["s2"] > 0 and vals["w1"] > 0 and vals["mu1"] > 0
                ell_s = 1 / mp.sqrt(vals["w1"]) if vals["w1"] > 0 else mp.nan
                mu = vals["mu1"]
                R1, R2 = vals["R"], vals["R2"]
                rec = dict(adm=adm, mu=mu, ell_s=ell_s, R1=R1, R2=R2, s=vals["s"], s2=vals["s2"], w=vals["w1"])
                if adm:
                    rh2 = (ell_s**2 / 2) * (-1 + mp.sqrt(1 + 4 * mu / ell_s**2))
                    rec["r_h"] = mp.sqrt(rh2)
                    rec["res"] = max(abs(e) for e in residuals(lam1, ratio, c, R1, R2, mu, ell_s))
                    rec["crit1"] = 1 / ell_s + 1            # critical (flat-balance) tension for ours' two sides
                    rec["crit2"] = 1 / ell_s - 1 / mp.mpf(c)  # critical for position 2's two sides
                key = tuple(round(float(x), 12) for x in (mu, R1, R2))
                if all(tuple(round(float(x), 12) for x in (q["mu"], q["R1"], q["R2"])) != key for q in sols):
                    sols.append(rec)
    return "OK", sols


if __name__ == "__main__":
    lam1 = sp.Integer(2)   # reading (iii): ours at RS of its own ell_1 = 1 (lam = 2/ell_1)
    grid = [(sp.Rational(-1, 8), sp.Rational(4, 3), "per-sheet M4 (-1/8, 4ell/3)"),
            (sp.Rational(-1, 4), sp.Rational(4, 3), "KDERIVE/b6_k PRZ (-1/4, 4ell/3)"),
            (sp.Rational(-1, 3), sp.Integer(3), "stage 6 J3 (-1/3, 3ell)"),
            (sp.Rational(-1, 6), sp.Integer(6), "stage 7 K5 route (-1/6, 6ell)"),
            (sp.Rational(-1, 6), sp.Integer(3), "K5 one sheet at J3's ell_2 (-1/6, 3ell)"),
            (sp.Rational(-1, 4), sp.Integer(1), "hybrid (-1/4, ell)"),
            (sp.Rational(-1, 8), sp.Integer(1), "hybrid (-1/8, ell)"),
            (sp.Rational(-1, 3), sp.Rational(1, 3), "K4 ell_1-unit row (-1/3, ell_1/3)"),
            (sp.Rational(-1, 6), sp.Rational(3, 10), "K4 ell_1-unit row (-1/6, 3ell_1/10)"),
            (sp.Rational(-1, 4), sp.Integer(3), "(-1/4, 3ell)"),
            (sp.Rational(-1, 4), sp.Integer(6), "(-1/4, 6ell)"),
            (sp.Rational(-1, 8), sp.Integer(3), "(-1/8, 3ell)"),
            (sp.Rational(-1, 8), sp.Integer(6), "(-1/8, 6ell)"),
            (sp.Rational(-1, 3), sp.Rational(4, 3), "(-1/3, 4ell/3)"),
            (sp.Rational(-1, 6), sp.Rational(4, 3), "(-1/6, 4ell/3)"),
            (sp.Rational(-1, 3), sp.Integer(1), "(-1/3, ell)"),
            (sp.Rational(-1, 6), sp.Integer(1), "(-1/6, ell)")]
    only = sys.argv[1:] and int(sys.argv[1])
    for i, (ratio, c, name) in enumerate(grid):
        if only and i != only - 1:
            continue
        st, sols = solve(lam1, ratio, c)
        adm = [q for q in sols if q["adm"]]
        print("%-42s ratio=%-5s ell_2=%-5s  admissible solutions: %d  (non-admissible real: %d)"
              % (name, ratio, c, len(adm), len(sols) - len(adm)))
        for q in adm:
            print("   ell_s=%s mu=%s r_h=%s R1=%s R2=%s" % tuple(mp.nstr(q[k], 12) for k in ("ell_s", "mu", "r_h", "R1", "R2")))
            print("   max unsquared residual=%s ; ours lam1=2 vs critical 1/ell_s+1/ell_1=%s ; pos2 lam2=%s vs critical %s"
                  % (mp.nstr(q["res"], 3), mp.nstr(q["crit1"], 10), mp.nstr(ratio * 2, 6), mp.nstr(q["crit2"], 10)))
        sys.stdout.flush()
