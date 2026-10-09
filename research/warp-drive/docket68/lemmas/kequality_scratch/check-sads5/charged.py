#!/usr/bin/env python3
"""Charged (RN-AdS5) slab, own code.  Slab F = k u + Linv2 - mu u^2 + Q u^3 (Q = q^2 > 0).  Outer bulks: Q_out = 0
('charged planes', flux zero outside) or Q_out = Q ('neutral planes', flux continuous), outer mu = 0.
Unknowns u1, u2, mu, Q: 4 equations, 4 unknowns -> isolated solutions generic.  Which are admissible?
"""
import sys
import sympy as sp
import mpmath as mp
from twoplane import plane_eqs, u1, u2, mu, Q, z, w, R, S, CONFS

mp.mp.dps = 50
v = sp.Symbol('v')  # Q != 0


def charged_conf(base, flux):
    c = dict(base)
    def conv(sides, mirrored):
        out = []
        for (Li2, m, Qc) in sides:
            if m == mu:
                out.append((Li2, mu, Q))
            else:
                out.append((Li2, m, Q if flux == 'continuous' else 0))
        return out
    c['p1'] = conv(base['p1'], base.get('p1_mirrored', False))
    c['p2'] = conv(base['p2'], base.get('p2_mirrored', False))
    return c


def horizons(k, Li2, m, Qc):
    x = sp.Symbol('x')
    rts = sp.Poly(Li2*x**3 + k*x**2 - m*x + Qc, x).nroots(n=30)
    return sorted(float(sp.re(r))**0.5 for r in rts if abs(sp.im(r)) < 1e-20 and sp.re(r) > 0)


def analyse(name, c, k):
    e1, s1 = plane_eqs(1, u1, c['p1'], c['tau1'], k, c.get('p1_mirrored', False))
    e2, s2 = plane_eqs(2, u2, c['p2'], c['tau2'], k, c.get('p2_mirrored', False))
    ss = s1 + s2
    nz = u1*u2
    for s in ss:
        nz *= s
    eqs = [sp.expand(e) for e in e1 + e2 + [w*nz - 1, z*mu - 1, v*Q - 1]]
    vars_ = [z, v, w] + ss + [u1, u2, mu, Q]
    G = sp.groebner(eqs, *vars_, order='lex', domain='QQ')
    if list(G) == [1]:
        print("%-14s k=%2d: INCONSISTENT over C" % (name, k)); return
    if not G.is_zero_dimensional:
        print("%-14s k=%2d: positive-dimensional; tail %s" % (name, k, list(G)[-2:])); return
    uni = [g for g in G if g.free_symbols <= {Q}][0]
    P = sp.Poly(uni, Q)
    roots = P.nroots(n=50, maxsteps=500)
    out = []
    for r in roots:
        if abs(sp.im(r)) > 1e-30 or sp.re(r) <= 0:
            continue
        sub = {Q: sp.re(r)}
        good = True
        for var in reversed(vars_[:-1]):
            cand = [sp.Poly(sp.expand(g.subs(sub)), var) for g in G
                    if var in g.free_symbols and g.free_symbols <= set(sub) | {var}]
            cand = [cc for cc in cand if not cc.is_zero]
            if not cand:
                good = False; break
            cand.sort(key=lambda p: p.degree())
            rr = [x for x in cand[0].nroots(n=50) if abs(sp.im(x)) < 1e-25]
            if not rr:
                good = False; break
            sub[var] = sp.re(rr[0])
        if not good:
            continue
        U1, U2, M, QQ = [float(sub[x]) for x in (u1, u2, mu, Q)]
        if U1 <= 0 or U2 <= 0:
            continue
        sv = [float(sub[s]) for s in ss]
        es1 = 1 if sv[0] > 0 else -1
        es2 = 1 if sv[len(s1)] > 0 else -1
        a1, a2 = U1**-0.5, U2**-0.5
        Li2s = c['p1'][0][0]
        hz = horizons(k, Li2s, M, QQ)
        if (es1, es2) == (1, 1):
            verdict = 'disjoint (+,+)'
        elif (es1, es2) == (-1, -1):
            verdict = 'two-exterior ' + ('ok' if hz and min(a1, a2) > max(hz) else 'NO (no horizon below both)')
        else:
            lo, hi = (a2, a1) if (es1, es2) == (-1, 1) else (a1, a2)
            order_ok = ((es1, es2) == (-1, 1) and a2 < a1) or ((es1, es2) == (1, -1) and a1 < a2)
            hz_in = any(lo < h < hi for h in hz)
            verdict = 'CONNECTED' if order_ok and not hz_in else ('order wrong' if not order_ok else 'horizon in slab')
        out.append((verdict, a1, a2, M, QQ, hz, sv))
    print("%-14s k=%2d: deg %d in Q; real positive-u roots:" % (name, k, P.degree()))
    for o in out:
        print("      %-28s a1=%.6g a2=%.6g mu=%.6g Q=q^2=%.6g horizons R=%s s=%s" % (
            o[0], o[1], o[2], o[3], o[4], [round(h, 5) for h in o[5]], [round(x, 5) for x in o[6]]))
    if not out:
        print("      none")


if __name__ == '__main__':
    names = sys.argv[1:] or ['V1', 'V2', 'S7a', 'S7b', 'S7c', 'S7d', 'S7e', 'T1', 'T2']
    for nm in names:
        for flux in ('zero-outside', 'continuous'):
            c = charged_conf(CONFS[nm], flux)
            for k in (1, 0, -1):
                analyse('%s/%s' % (nm, flux[:4]), c, k)
