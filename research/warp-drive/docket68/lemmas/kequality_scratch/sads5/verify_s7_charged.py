#!/usr/bin/env python3
"""verify_s7_charged.py -- independent check of charged_param.py's two connected solutions (STAGE7 K4 'ours grows'
rows, k = +1): the four junction equations from sads5_balance._plane_eqs (not the parametrisation) at 60 digits, the
slab's horizon structure, the orientation, and each plane's induced curvature radius.  Computed (numerical, 60 digits).
python3 verify_s7_charged.py
"""
import mpmath as mp
import sympy as sp

import charged_param as CP
import sads5_balance as S

mp.mp.dps = 60
C = S.conventions()
for name in ("S7-u1-1/3-grow", "S7-u1-1/6-grow"):
    st, out = CP.two_planes(1, C[name]["ours"], C[name]["p2"], None)
    for vals, ok, conn in out:
        if not (ok and conn):
            continue
        # refine (p1, p2) jointly by Newton on mu1(p1) = mu2(p2), Q1(p1) = Q2(p2) at 60 digits
        c1 = CP.curve(1, C[name]["ours"], None)
        c2 = CP.curve(1, C[name]["p2"], None)
        f1 = sp.lambdify(CP.p, [c1["mu"], c1["Q"], c1["u"], c1["s"], c1["t"]], "mpmath")
        f2 = sp.lambdify(CP.p, [c2["mu"], c2["Q"], c2["u"], c2["s"], c2["t"]], "mpmath")
        sol = mp.findroot(lambda x, y: [f1(x)[0] - f2(y)[0], f1(x)[1] - f2(y)[1]],
                          (mp.mpf(str(vals["p1"])), mp.mpf(str(vals["p2"]))))
        P1, P2 = sol[0], sol[1]
        mu, Q, u1, s1, t1 = f1(P1)
        _, _, u2, s2, t2 = f2(P2)
        mu_, q_, uu, ss, tt = sp.symbols("mu q u s t", real=True)
        e1, _ = S._plane_eqs(1, C[name]["ours"], mu_, q_, uu, ss, tt, None)
        e2, _ = S._plane_eqs(1, C[name]["p2"], mu_, q_, uu, ss, tt, None)
        r1 = [abs(sp.lambdify((mu_, q_, uu, ss, tt), e, "mpmath")(mu, mp.sqrt(Q), u1, s1, t1)) for e in e1]
        r2 = [abs(sp.lambdify((mu_, q_, uu, ss, tt), e, "mpmath")(mu, mp.sqrt(Q), u2, s2, t2)) for e in e2]
        x = sp.Symbol("x")
        roots = sp.Poly(x**3 + x**2 - sp.Float(str(mu), 50) * x + sp.Float(str(Q), 50), x).nroots(n=40)
        pos_real = [r for r in roots if abs(sp.im(r)) < 1e-30 and sp.re(r) > 0]
        print(name)
        print("  mu/ell_s^2 = %s   Q/ell_s^6 = %s" % (mp.nstr(mu, 20), mp.nstr(Q, 20)))
        print("  a1^2/ell_s^2 = %s   a2^2/ell_s^2 = %s   (a2 < a1: %s)" % (mp.nstr(1 / u1, 20), mp.nstr(1 / u2, 20), u2 > u1))
        print("  junction residuals (4 + 4):", [mp.nstr(r, 3) for r in r1 + r2])
        print("  square roots s1 t1 s2 t2:", [mp.nstr(v, 8) for v in (s1, t1, s2, t2)])
        print("  slab f(R) zeros (x = R^2 > 0):", pos_real, "-> horizon" if pos_real else "-> NO horizon (naked)")
        print("  plane curvature radii (k = +1, closed): a1 = %s ell_s, a2 = %s ell_s" % (mp.nstr(mp.sqrt(1 / u1), 8),
                                                                                       mp.nstr(mp.sqrt(1 / u2), 8)))
