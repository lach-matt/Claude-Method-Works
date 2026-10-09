#!/usr/bin/env python3
"""Probe beyond the author's enumeration: let the SLAB's own AdS curvature lam = 1/L_s^2 be free (the corridor's bulk
measured in its own length, not fixed by a flat-junction convention).  Then the count is 4 equations in 4 unknowns
(u1, u2, mu, lam), so isolated solutions are generic.  Are any admissible?
Own code; imports only twoplane.py (also mine).
"""
import sys
import itertools
import sympy as sp
import mpmath as mp
from twoplane import plane_eqs, u1, u2, mu, lam, z, w, R, S

mp.mp.dps = 40

def conf_free(tau1, L1inv2, tau2, L2inv2, p1_mirrored=False):
    if p1_mirrored:
        return dict(p1=[S(lam, mu)], p1_mirrored=True, tau1=tau1, p2=[S(lam, mu), S(L2inv2)], tau2=tau2)
    return dict(p1=[S(lam, mu), S(L1inv2)], tau1=tau1, p2=[S(lam, mu), S(L2inv2)], tau2=tau2)

CF = {
    # ours at RS of its own bulk ell_1 = 1, P2 at T1/T2 quarter, own ell_2 per flat convention
    'V1free': conf_free(1, 1, R(-1, 8), R(9, 16)),
    'V2free': conf_free(1, 1, R(-1, 4), R(1, 4)),
    'S7a-free': conf_free(R(4, 3), 1, R(-1, 3), 1),
    'S7c-free': conf_free(R(4, 3), 1, R(-1, 3), 9),
    'S7d-free': conf_free(R(4, 3), 1, R(-1, 6), R(100, 9)),
    'S7e-free': conf_free(R(4, 3), 1, R(-1, 6), R(16, 9)),
    # ours mirrored at RS(ell=1) but slab curvature free: off-RS relative to the slab (C1-like for ours)
    'T1mir-free': conf_free(1, None, R(-1, 8), R(9, 16), p1_mirrored=True),
    'T2mir-free': conf_free(1, None, R(-1, 4), R(1, 4), p1_mirrored=True),
}


def solve_conf(c, k):
    e1, s1 = plane_eqs(1, u1, c['p1'], c['tau1'], k, c.get('p1_mirrored', False))
    e2, s2 = plane_eqs(2, u2, c['p2'], c['tau2'], k, c.get('p2_mirrored', False))
    ss = s1 + s2
    nz = u1*u2*lam
    for s in ss:
        nz *= s
    eqs = [sp.expand(e) for e in e1 + e2 + [w*nz - 1, z*mu - 1]]
    vars_ = [z, w] + ss + [u1, u2, mu, lam]
    G = sp.groebner(eqs, *vars_, order='lex', domain='QQ')
    return G, vars_, ss


def horizons(k, Linv2, m, Qc=0):
    # f(R) = k + Linv2 R^2 - m/R^2 + Qc/R^4 ; roots in x = R^2 > 0 of Linv2 x^3 + k x^2 - m x + Qc
    xs = sp.Poly([Linv2, k, -m, Qc], sp.Symbol('x')).nroots(n=30)
    return sorted([float(sp.re(x)) for x in xs if abs(sp.im(x)) < 1e-20 and sp.re(x) > 0])


def admissible(sol, ss, k, c):
    """Return (ok, note)."""
    U1, U2, M, Lm = (sol[u1], sol[u2], sol[mu], sol[lam])
    for v in (U1, U2, M, Lm) + tuple(sol[s] for s in ss):
        if abs(sp.im(v)) > 1e-25:
            return False, 'complex'
    U1, U2, M, Lm = [float(sp.re(v)) for v in (U1, U2, M, Lm)]
    if U1 <= 0 or U2 <= 0 or Lm <= 0:
        return False, 'u or lam <= 0 (u1=%.4g u2=%.4g lam=%.4g)' % (U1, U2, Lm)
    sv = {str(s): float(sp.re(sol[s])) for s in ss}
    es1 = 1 if sv[str(ss[0])] > 0 else -1
    es2 = 1 if sv[str(ss[-2])] > 0 else -1   # P2's slab side is its first side
    a1, a2 = U1**-0.5, U2**-0.5
    hz = horizons(k, Lm, M)
    note = 'a1=%.6g a2=%.6g mu=%.6g L_s=%.6g eta_s=(%d,%d) slab horizons R=%s s=%s' % (
        a1, a2, M, Lm**-0.5, es1, es2, [round(x**0.5, 6) for x in hz], {k_: round(v, 6) for k_, v in sv.items()})
    if (es1, es2) == (1, 1):
        return False, 'disjoint (+1,+1): ' + note
    if (es1, es2) == (-1, 1):
        if not a2 < a1:
            return False, 'slab (-,+) needs a2<a1: ' + note
        lo, hi = a2, a1
    elif (es1, es2) == (1, -1):
        if not a1 < a2:
            return False, 'slab (+,-) needs a1<a2: ' + note
        lo, hi = a1, a2
    else:  # (-1,-1) two-exterior bridge: need an outer horizon below both planes
        if not hz:
            return False, 'two-exterior (-,-) but no horizon: ' + note
        rh = max(hz)**0.5
        if not (a1 > rh and a2 > rh):
            return False, 'two-exterior: a plane inside the horizon: ' + note
        return True, 'TWO-EXTERIOR BRIDGE ' + note
    if any(lo < x**0.5 < hi for x in hz):
        return False, 'horizon inside the slab: ' + note
    return True, 'CONNECTED SLAB ' + note


if __name__ == '__main__':
    names = sys.argv[1:] or list(CF)
    for nm in names:
        c = CF[nm]
        for k in (1, 0, -1):
            G, vars_, ss = solve_conf(c, k)
            if list(G) == [1]:
                print("%-11s k=%2d : INCONSISTENT over C" % (nm, k))
                continue
            # last element univariate in lam (lex order, lam last)
            dim0 = G.is_zero_dimensional
            print("%-11s k=%2d : GB %d elements, zero-dim=%s" % (nm, k, len(G), dim0))
            if not dim0:
                print("      ", [g for g in G][-3:])
                continue
            sols = sp.solve_poly_system(list(G), *vars_) if False else None
            # numeric: univariate in lam then back-substitute via the triangular lex basis
            uni = [g for g in G if g.free_symbols <= {lam}]
            p = sp.Poly(uni[0], lam)
            print("       univariate in lam: degree %d" % p.degree())
            roots = p.nroots(n=40, maxsteps=200)
            nadm = 0
            for r in roots:
                sub = {lam: r}
                ok_all = True
                for v in reversed(vars_[:-1]):
                    cand = [g.subs(sub) for g in G if v in g.free_symbols and g.free_symbols <= set(sub) | {v}]
                    cand = [sp.Poly(sp.expand(cc), v) for cc in cand if sp.expand(cc) != 0]
                    if not cand:
                        ok_all = False; break
                    cand.sort(key=lambda P: P.degree())
                    rr = cand[0].nroots(n=40)
                    # keep the root satisfying all others
                    best = None
                    for x in rr:
                        if all(abs(complex(P.eval(x))) < 1e-15*max(1, abs(complex(x)))**P.degree()*1e6 for P in cand):
                            best = x; break
                    if best is None:
                        best = rr[0]
                    sub[v] = best
                if not ok_all:
                    continue
                ok, note = admissible(sub, ss, k, c)
                if not note.startswith('complex'):
                    print("       root: %s  -> %s" % ('ADMISSIBLE' if ok else 'rejected', note))
                nadm += ok
            print("       admissible: %d" % nadm)
