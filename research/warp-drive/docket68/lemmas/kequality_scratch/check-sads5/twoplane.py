#!/usr/bin/env python3
"""Independent two-plane balance in Schwarzschild(-RN)-AdS5 (own code; does not import the author's scripts).

Each plane j sits at R = a_j, u_j = 1/a_j^2.  Each side i of plane j has F_i(u) = k u + Linv2_i - m_i u^2 + Q_i u^3 and a
signed root s_ji = eta_ji sqrt(F_i(u_j)) (eta = +1: that side is the region R > a_j).  Pure tension tau_j:
    sum_i s_ji = -2 tau_j            (tt: rho = -(3/kappa^2) Phi = sigma)
    sum_i F_i'(u_j) / s_ji = 0       (angular: rho + p = 0  <=>  dPhi/du = 0)
A mirrored plane has the same side twice: 2 s = -2 tau, F'(u) = 0.
Signs of the s variables are left free, so ONE polynomial system covers all 2^(#sides) normal orientations; the
orientation is read off a solution afterwards.
Exact: sympy groebner over QQ.  'With corridor' adds z*mu - 1 = 0 (mu != 0) and w*u1*u2*prod(s) - 1 = 0.
"""
import sys
import itertools
import sympy as sp

u1, u2, mu, Q, lam, z, w = sp.symbols('u1 u2 mu Q lam z w')
R = sp.Rational


def Fpoly(k, Linv2, m, Qc, uu):
    return k*uu + Linv2 - m*uu**2 + Qc*uu**3


def plane_eqs(j, uu, sides, tau, k, mirrored=False):
    """sides: list of (Linv2, m, Qc).  Returns (equations, s-symbols)."""
    eqs, ss = [], []
    if mirrored:
        (Linv2, m, Qc), = sides
        s = sp.Symbol('s%d_m' % j)
        Fi = Fpoly(k, Linv2, m, Qc, uu)
        eqs += [s**2 - Fi, 2*s + 2*tau, sp.diff(Fi, uu)]
        ss.append(s)
        return eqs, ss
    Fs, dFs = [], []
    for i, (Linv2, m, Qc) in enumerate(sides):
        s = sp.Symbol('s%d_%d' % (j, i))
        Fi = Fpoly(k, Linv2, m, Qc, uu)
        eqs.append(s**2 - Fi)
        Fs.append(Fi); dFs.append(sp.diff(Fi, uu)); ss.append(s)
    eqs.append(sum(ss) + 2*tau)
    # sum_i F_i'/s_i = 0, cleared of denominators
    tot = 0
    for i in range(len(ss)):
        prod = 1
        for l in range(len(ss)):
            if l != i:
                prod *= ss[l]
        tot += dFs[i]*prod
    eqs.append(tot)
    return eqs, ss


def build(conf, k, corridor=True, extra_vars=()):
    e1, s1 = plane_eqs(1, u1, conf['p1'], conf['tau1'], k, conf.get('p1_mirrored', False))
    e2, s2 = plane_eqs(2, u2, conf['p2'], conf['tau2'], k, conf.get('p2_mirrored', False))
    eqs = e1 + e2
    ss = s1 + s2
    nz = u1*u2
    for s in ss:
        nz *= s
    eqs.append(w*nz - 1)
    vars_ = ss + [w] + [u1, u2, mu] + list(extra_vars)
    if corridor:
        eqs.append(z*mu - 1)
        vars_ = [z] + vars_
    return [sp.expand(e) for e in eqs], vars_, ss


def gb(conf, k, corridor=True, extra_vars=(), order='grevlex'):
    eqs, vars_, ss = build(conf, k, corridor, extra_vars)
    G = sp.groebner(eqs, *vars_, order=order, domain='QQ')
    return G, vars_, ss


S = lambda Linv2, m=0, Qc=0: (Linv2, m, Qc)   # a side

CONFS = {
    # T1: M4 geometry (k_R = 3 k_L/4), ours LR orbifold plane mirrored at RS(ell_L=1); P2 one sheet, outer ell_R = 4/3
    'T1':  dict(p1=[S(1, mu)], p1_mirrored=True, tau1=1, p2=[S(1, mu), S(R(9, 16))], tau2=R(-1, 8)),
    'T1d': dict(p1=[S(1, mu)], p1_mirrored=True, tau1=1, p2=[S(1, mu), S(R(9, 16))], tau2=R(-1, 4)),
    'T2':  dict(p1=[S(1, mu)], p1_mirrored=True, tau1=1, p2=[S(1, mu), S(R(1, 4))], tau2=R(-1, 4)),
    'T3':  dict(p1=[S(1, mu)], p1_mirrored=True, tau1=1, p2=[S(1, mu), S(R(1, 9))], tau2=R(-1, 3)),
    'T4':  dict(p1=[S(1, mu)], p1_mirrored=True, tau1=1, p2=[S(1, mu), S(R(1, 36))], tau2=R(-1, 6)),
    # STAGE7 K4 rows: ours two-sided (slab, own ell_1), P2 two-sided (slab, own ell_2); flat-junction curvatures
    'S7a': dict(p1=[S(R(25, 9), mu), S(1)], tau1=R(4, 3), p2=[S(R(25, 9), mu), S(1)], tau2=R(-1, 3)),
    'S7b': dict(p1=[S(R(16, 9), mu), S(R(16, 9))], tau1=R(4, 3), p2=[S(R(16, 9), mu), S(1)], tau2=R(-1, 6)),
    'S7c': dict(p1=[S(R(121, 9), mu), S(1)], tau1=R(4, 3), p2=[S(R(121, 9), mu), S(9)], tau2=R(-1, 3)),
    'S7d': dict(p1=[S(R(121, 9), mu), S(1)], tau1=R(4, 3), p2=[S(R(121, 9), mu), S(R(100, 9))], tau2=R(-1, 6)),
    'S7e': dict(p1=[S(R(25, 9), mu), S(1)], tau1=R(4, 3), p2=[S(R(25, 9), mu), S(R(16, 9))], tau2=R(-1, 6)),
    # V1/V2: our mirror replaced by a corridor-free copy of our own bulk (ell_1 = ell_s = 1)
    'V1':  dict(p1=[S(1, mu), S(1)], tau1=1, p2=[S(1, mu), S(R(9, 16))], tau2=R(-1, 8)),
    'V2':  dict(p1=[S(1, mu), S(1)], tau1=1, p2=[S(1, mu), S(R(1, 4))], tau2=R(-1, 4)),
}


def flat_check(conf):
    """mu = 0, k = 0: does some orientation balance both planes identically in u (the control's modulus)?"""
    res = []
    def sides_of(p, mir):
        return [p[0], p[0]] if mir else p
    sd1 = sides_of(conf['p1'], conf.get('p1_mirrored', False))
    sd2 = sides_of(conf['p2'], conf.get('p2_mirrored', False))
    for et1 in itertools.product((1, -1), repeat=len(sd1)):
        if conf.get('p1_mirrored') and et1[0] != et1[1]:
            continue
        Phi1 = sum(e*sp.sqrt(sp.sympify(sd[0]).subs(mu, 0)) for e, sd in zip(et1, sd1))
        if sp.simplify(Phi1 + 2*conf['tau1']) != 0:
            continue
        for et2 in itertools.product((1, -1), repeat=len(sd2)):
            Phi2 = sum(e*sp.sqrt(sp.sympify(sd[0]).subs(mu, 0)) for e, sd in zip(et2, sd2))
            if sp.simplify(Phi2 + 2*conf['tau2']) == 0:
                res.append((et1, et2))
    return res


if __name__ == '__main__':
    names = sys.argv[1:] or list(CONFS)
    for nm in names:
        c = CONFS[nm]
        print("=== %s  flat (mu=0,k=0) balancing orientations [(eta at P1),(eta at P2)]: %s" % (nm, flat_check(c)))
        for k in (1, 0, -1):
            G, vars_, ss = gb(c, k, corridor=True)
            inc = (list(G) == [1])
            print("   k=%2d  with corridor (mu != 0): groebner = %s" % (k, "[1]  INCONSISTENT (no complex solution)" if inc
                                                                  else "%d elements, NOT trivially inconsistent" % len(G)))
            if not inc:
                print("        ", list(G)[:6])
            # without the mu != 0 constraint: does mu*u1 (or mu) lie in the ideal?  (k=0 expectation)
            G0, v0, _ = gb(c, k, corridor=False)
            red = G0.reduce(mu)[1]
            print("          ideal without mu!=0: GB len %d; mu reduces to %s" % (len(G0), red))
