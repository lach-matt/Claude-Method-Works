#!/usr/bin/env python3
"""augment5: the augmented Einstein-null-dust system in the class, its derivative count, its constraints, and the
speeds on Part I's background (FAMILIES5-NONROUND.md section 3).

Unknowns: g (wave-map gauge relative to the background), and per family A a covector field p_A (the eikonal's
gradient), its expansion th_A, its density q_A = F_A^2. P_A := g^-1 p_A. Equations:
  Ric^H(g) = T := sum_A q_A p_A p_A;  nabla_(P_A) p_A = 0;  P_A(q_A) = -th_A q_A;
  P_A(th_A) = -(th_A - k_A1 - k_A2)^2 - k_A1^2 - k_A2^2 - T(P_A, P_A),   k_Ai := g^-1(p_A, d psi_i)   (classchi5 (R)).

  S1 (computed, a derivative ledger) with the energy at order m (d^j of dg, p_A, th_A, q_A in L^2 for j <= m), every
     source is at order m in the class off the axes: the sources are built in sympy from jet symbols and the highest
     derivative of each unknown in each source is read off. Controls (must fail): (a) the dust transport with th_A
     replaced by div P_A (no Raychaudhuri unknown) contains dp: order m - 1; (b) the general five-dimensional
     Raychaudhuri source |hess u|^2 = |dp|^2-type contains dp; (c) at an axis point kappa_2 = (1/a) d_3 p_3 + ...
     (axisloss5 X1 (b)) contains dp. Each loses one derivative: the loop wave -> p -> th -> q -> T -> wave closes at
     order m only in the first case.
  S2 (exact at rational jets, a general 5D metric and covector field) the propagation identities: P(N) = 2 g^-1(p,
     nabla_P p) with N := g^-1(p, p), and (nabla_P p)_a = (1/2) d_a N + P^b (dp)_ba; and Cartan's L_P (dp) = d(i_P dp).
     Hence under nabla_P p = 0: N is constant along P (N = 0 propagates), then i_P dp = 0 and dp is Lie-transported
     (dp = 0 propagates): p_A stays an exact null gradient du_A. Controls (must fail): the transport without the
     Christoffel term, P^b d_b p_a = 0, does not conserve N; Cartan's identity with a non-closed 2-form in place of dp.
  S3 (exact at jets) div T and tr T for one family: nabla^a T_ab = (P(q) + q div P) p_b + q (nabla_P p)_b and
     g^ab T_ab = q N; so under the augmented equations div T = -(th - div P) q p. Control (must fail): the density
     transport P(q) = -th q/2 leaves a term not proportional to th - div P.
  S4 (exact algebra) with d := th - div P and the exact class identity (R) for div P = box u (classchi5 C3),
     P(d) = -d (th + div P - 2 k1 - 2 k2) - (T - Ric)(P, P): homogeneous in (d, T - Ric).
     Control (must fail): an augmented equation with the shear-free source -th^2/3 leaves an inhomogeneous term.
  S5 (exact at jets) the gauge source: B_g T := -div T + (1/2) d tr T = sum_A d_A q_A p_A + (1/2) d(sum q_A N_A): with the
     record's propagation identities (propagate5.py P1-P2: B_g Ric = 0 and B_g delta*W = -(1/2)(box W + Ric(W))) the
     gauge vector W solves box W + Ric(W) + (first order in W) = 2 B_g T, whose source vanishes with d_A and N_A.
     Control (must fail): without the (1/2) d tr T term the identity fails where N != 0.
  S6 (exact) why the record's citation [DS23] does not cover the augmented system as stated: the transport root of
     P_A meets the light cone at the conormal p_A: P_A(p_A) = 0 and g^-1(p_A, p_A) = 0, so the eigenvalue of the
     transport equals a wave eigenvalue at xi = spatial part of p_A ([DS23] (A4) asks the eigenvalues not to meet).
     Control: a timelike transport field (massive dust) has its root strictly between the two wave roots.
  S7 (exact; floating grid) speeds on Part I's round two-dust background in its chart, g0 = -e^(2 psi) f dvhat^2 + 2
     e^psi dvhat dR + R^2 dOmega^2, tau = vhat - R, with psi <= 0, f <= 1 (FAMILIES5-FULL.md section 2 (e)): every future
     causal vector with dtau = 1 has R |dOmega| <= sqrt(e^psi/(2 - e^psi f)) <= 1 and dR in [-1, e^psi f/(2 - e^psi f)],
     an interval inside [-1, 1] that lies in (-oo, 0) where f < 0 (R = a trapped). So for EVERY family the transport
     boundary terms of the record's Lemma 2.4 have the record's sign (outer: b' - c <= -2 + 1; inner: c(a) < 0), and the
     angular speed is at most 1/R <= 1/a. Control (must fail): e^psi f = 1.9 (excluded by psi <= 0, f <= 1) gives R
     |dOmega| > 1.

Labels: computed (exact, sympy and Fractions at jets via checks/jetpoly5.py; S7's bound also on a floating grid).
Run: python3 checks/augment5.py   (under a minute)
"""
from fractions import Fraction
import os
import random
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jetpoly5 import Jet, matinv, monomials, NV  # noqa: E402

n = NV


def s1():
    print("S1 (derivative ledger): highest derivative of each unknown in each source (order m: dg, p, th, q)")
    # jet symbols: g0 (metric), g1 (dg), g2 (d^2 g); p0, p1 (dp); t0, t1 (dth); q0, q1 (dq); x (position)
    g0, g1, g2, p0, p1, t0, t1, q0, q1, x = sp.symbols('g0 g1 g2 p0 p1 t0 t1 q0 q1 x')
    level = {g0: ('g', 0), g1: ('g', 1), g2: ('g', 2), p0: ('p', 0), p1: ('p', 1), t0: ('th', 0), t1: ('th', 1),
             q0: ('q', 0), q1: ('q', 1)}
    order = {'g': 1, 'p': 0, 'th': 0, 'q': 0}          # the energy controls d^m of dg, p, th, q: g at m+1, others at m
    Ginv = 1 / g0                                     # torus |K|^-2: bounded off the axes
    kap = Ginv * p0 * g1                              # kappa_i = g^-1(p, dG/(2G)): classchi5 C1
    srcs = {
        'wave: T = q p p, Q(dg, dg)': q0 * p0**2 + g1**2,
        'p transport: Gam(dg) p p': g1 * p0**2,
        'th transport (class, off axes)': (t0 - 2 * kap)**2 + 2 * kap**2 + q0 * p0**4,
        'q transport: th q': t0 * q0,
    }
    ctl = {
        '(a) q transport with div P': p1 * q0 + g1 * p0 * q0,
        '(b) th transport, general 5D: |hess u|^2': p1**2 + (g1 * p0)**2,
        '(c) th transport at an axis point: kappa2 = d3 p3 / a': (t0 - p1 / g0)**2 + (p1 / g0)**2,
    }

    def worst(expr):
        """the smallest regularity level among the jet symbols in expr (level = order - derivatives)."""
        lv = []
        for sym in expr.free_symbols:
            if sym in level:
                name, k = level[sym]
                lv.append(order[name] - k)
        return min(lv)
    ok = True
    for k, e in srcs.items():
        w = worst(e)
        print("   %-40s lowest level m%+d -> %s" % (k, w, 'closes' if w >= 0 else 'LOSES'))
        ok &= w >= 0
    bad = True
    for k, e in ctl.items():
        w = worst(e)
        print("   control %-38s lowest level m%+d -> %s" % (k, w, 'closes' if w >= 0 else 'LOSES'))
        bad &= w < 0
    return ok and bad


def rnd(rng, den=9):
    return Fraction(rng.randint(-4 * den, 4 * den), den * 5)


def rjet(rng, c0, deg=3):
    e = Jet.const(c0)
    for d in range(1, deg + 1):
        for m in monomials(n, d):
            e = e + Jet({m: rnd(rng) / (2 * d)})
    return e


def metric(rng):
    g = [[None] * n for _ in range(n)]
    base = [-1, 1, 1, 1, 1]
    for i in range(n):
        for j in range(i, n):
            c0 = Fraction(base[i] if i == j else 0) + (Fraction(rng.randint(-3, 3), 20) if i != j else 0)
            g[i][j] = g[j][i] = rjet(rng, c0, deg=2)
    return g


def christoffel(g, gi):
    dg = [[[g[a][b].d(c) for c in range(n)] for b in range(n)] for a in range(n)]
    return [[[sum((gi[c][d] * (dg[d][b][a] + dg[d][a][b] - dg[a][b][d]) for d in range(n)), Jet()) * Fraction(1, 2)
              for b in range(n)] for a in range(n)] for c in range(n)]


def s2_s3_s5(seed):
    rng = random.Random(seed)
    g = metric(rng)
    gi = matinv(g)
    Gam = christoffel(g, gi)
    p = [rjet(rng, Fraction(rng.randint(-5, 5), 3)) for _ in range(n)]
    q = rjet(rng, Fraction(2))
    P = [sum((gi[a][b] * p[b] for b in range(n)), Jet()) for a in range(n)]
    N = sum((gi[a][b] * p[a] * p[b] for a in range(n) for b in range(n)), Jet())
    nabPp = [sum((P[b] * (p[a].d(b) - sum((Gam[c][b][a] * p[c] for c in range(n)), Jet())) for b in range(n)), Jet())
             for a in range(n)]
    om = [[p[a].d(b) - p[b].d(a) for b in range(n)] for a in range(n)]        # (dp)_ba = d_b p_a - d_a p_b = om[a][b]
    PN = sum((P[a] * N.d(a) for a in range(n)), Jet()).at0()
    rhs = (2 * sum((gi[a][b] * p[a] * nabPp[b] for a in range(n) for b in range(n)), Jet())).at0()
    ok1 = PN == rhs
    ok2 = all((nabPp[a] - N.d(a) * Fraction(1, 2) - sum((P[b] * om[a][b] for b in range(n)), Jet())).at0() == 0
              for a in range(n))
    # control: transport without the Christoffel term
    flat = [sum((P[b] * p[a].d(b) for b in range(n)), Jet()) for a in range(n)]
    rhs_bad = (2 * sum((gi[a][b] * p[a] * flat[b] for a in range(n) for b in range(n)), Jet())).at0()
    ctl1 = PN != rhs_bad
    # Cartan on omega = dp (as a 2-form W_ab = d_a p_b - d_b p_a)
    W = [[p[b].d(a) - p[a].d(b) for b in range(n)] for a in range(n)]

    def cartan_defect(W):
        iPW = [sum((P[a] * W[a][b] for a in range(n)), Jet()) for b in range(n)]
        LW = [[sum((P[c] * W[a][b].d(c) + W[c][b] * P[c].d(a) + W[a][c] * P[c].d(b) for c in range(n)), Jet())
               for b in range(n)] for a in range(n)]
        return max(abs((LW[a][b] - iPW[b].d(a) + iPW[a].d(b)).at0()) for a in range(n) for b in range(n))
    ok3 = cartan_defect(W) == 0
    Wbad = [[(W[a][b] + (Jet.var(0) * Jet.var(1) if (a, b) == (2, 3) else Jet())
              - (Jet.var(0) * Jet.var(1) if (a, b) == (3, 2) else Jet())) for b in range(n)] for a in range(n)]
    ctl2 = cartan_defect(Wbad) != 0
    # S3: div T and tr T
    T = [[q * p[a] * p[b] for b in range(n)] for a in range(n)]

    def cov_divT(T):
        out = []
        for b in range(n):
            tot = Jet()
            for a in range(n):
                for c in range(n):
                    term = T[a][b].d(c) - sum((Gam[d][c][a] * T[d][b] + Gam[d][c][b] * T[a][d] for d in range(n)),
                                              Jet())
                    tot = tot + gi[a][c] * term
            out.append(tot)
        return out
    divT = cov_divT(T)
    divP = sum((P[a].d(a) + sum((Gam[a][a][b] * P[b] for b in range(n)), Jet()) for a in range(n)), Jet())
    Pq = sum((P[a] * q.d(a) for a in range(n)), Jet())
    ok4 = all((divT[b] - (Pq + q * divP) * p[b] - q * nabPp[b]).at0() == 0 for b in range(n))
    trT = sum((gi[a][b] * T[a][b] for a in range(n) for b in range(n)), Jet())
    ok5 = (trT - q * N).at0() == 0
    # under the augmented equations (th arbitrary value, P(q) = -th q, nabla_P p = 0 imposed algebraically at 0)
    th = Fraction(7, 3)
    divT_aug = [((-th * q + q * divP) * p[b]).at0() for b in range(n)]   # nabla_P p = 0
    ok6 = all(divT_aug[b] == (-(th - divP.at0()) * q.at0() * p[b].at0()) for b in range(n))
    divT_bad = [((-th * q / 2 + q * divP) * p[b]).at0() for b in range(n)]
    ctl3 = any(divT_bad[b] != (-(th - divP.at0()) * q.at0() * p[b].at0()) for b in range(n))
    # S5: B_g T = -div T + (1/2) d tr T = (th - div P) q p + (1/2) d(q N) under the augmented equations
    BgT = [(-(Pq + q * divP) * p[b] - q * nabPp[b] + trT.d(b) * Fraction(1, 2)).at0() for b in range(n)]
    ok7 = all(BgT[b] == (-(divT[b]) + trT.d(b) * Fraction(1, 2)).at0() for b in range(n))
    BgT_aug = [(th * q.at0() - q.at0() * divP.at0()) * p[b].at0() + (q * N).d(b).at0() / 2 for b in range(n)]
    direct = [(-(-th * q + q * divP) * p[b]).at0() + trT.d(b).at0() / 2 for b in range(n)]
    ok8 = BgT_aug == direct
    ctl4 = any((q * N).d(b).at0() != 0 for b in range(n))    # the d tr T term matters where N != 0
    print("   seed %d: P(N) = 2 g^-1(p, nabla_P p): %s; nabla_P p = dN/2 + i_P dp: %s; Cartan: %s; "
          "div T = (P q + q div P) p + q nabla_P p: %s; tr T = q N: %s" % (seed, ok1, ok2, ok3, ok4, ok5))
    print("      augmented: div T = -(th - div P) q p: %s; B_g T formula: %s, %s" % (ok6, ok7, ok8))
    print("      controls: no Christoffel term breaks P(N): %s; non-closed 2-form breaks Cartan: %s; P(q) = -th q/2 "
          "breaks div T: %s; d tr T term nonzero where N != 0: %s" % (ctl1, ctl2, ctl3, ctl4))
    return ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7 and ok8 and ctl1 and ctl2 and ctl3 and ctl4


def s4():
    th, thh, k1, k2, T, R = sp.symbols('th thhat k1 k2 TPP RicPP')
    Pth = -(th - k1 - k2)**2 - k1**2 - k2**2 - T                  # augmented
    Pthh = -(thh - k1 - k2)**2 - k1**2 - k2**2 - R                 # exact, classchi5 (R)
    d = th - thh
    ok = sp.expand(Pth - Pthh - (-d * (th + thh - 2 * k1 - 2 * k2) - (T - R))) == 0
    Pth_bad = -th**2 / 3 - T
    resid = sp.expand(Pth_bad - Pthh - (-d * (th + thh - 2 * k1 - 2 * k2) - (T - R)))
    ctl = sp.simplify(resid.subs(th, thh)) != 0                   # inhomogeneous: survives at d = 0, T = R
    print("S4 P(d) = -d (th + div P - 2 k1 - 2 k2) - (T - Ric)(P, P):", ok, "; control (shear-free source leaves",
          sp.factor(resid.subs({th: thh, T: R})), "at d = 0):", ctl)
    return ok and ctl


def s6():
    rng = random.Random(4)
    # a Lorentzian metric at a point (5D), inverse G; a null covector p; the transport P = G p
    G = sp.diag(-1, 1, 1, 1, 1)
    for i in range(5):
        for j in range(i + 1, 5):
            G[i, j] = G[j, i] = sp.Rational(rng.randint(-3, 3), 25)
    xi = [sp.Rational(rng.randint(-5, 5), 4) for _ in range(4)]
    # null p with spatial part xi: solve G(p, p) = 0 for p0
    p0 = sp.Symbol('p0')
    pv = sp.Matrix([p0] + xi)
    sols = sp.solve(sp.expand((pv.T * G * pv)[0]), p0)
    lam = sp.Symbol('lam')
    ok = True
    for s in sols:
        pp = pv.subs(p0, s)
        P = G * pp
        lamT = -sum(P[i + 1] * xi[i] for i in range(4)) / P[0]          # transport root at the conormal xi
        eta = sp.Matrix([lamT] + xi)
        wave = sp.simplify((eta.T * G * eta)[0])
        ok &= sp.simplify(lamT - s) == 0 and wave == 0
    # control: timelike transport field V (massive dust): its root at xi lies strictly between the wave roots
    V = sp.Matrix([1, sp.Rational(1, 3), 0, sp.Rational(1, 5), 0])
    lamV = -sum(V[i + 1] * xi[i] for i in range(4)) / V[0]
    roots = sp.solve(sp.expand((sp.Matrix([lam] + xi).T * G * sp.Matrix([lam] + xi))[0]), lam)
    rv = sorted([sp.N(r) for r in roots])
    between = rv[0] < sp.N(lamV) < rv[1]
    timelike = (V.T * G.inv() * V)[0] < 0
    print("S6 transport root = wave root at the conormal of a null p (both signs of p0):", ok,
          "; control: timelike transport root strictly between the wave roots:", bool(between and timelike))
    return ok and bool(between and timelike)


def s7():
    psi, f, vd, Od = sp.symbols('psi f vdot Odot', real=True)
    E = sp.exp(psi)
    Rd = vd - 1                                         # tau = vhat - R, dtau = 1
    quad = -(-E**2 * f * vd**2 + 2 * E * vd * Rd)       # R^2 |dOmega|^2 <= quad for causal vectors
    quad = sp.expand(quad)
    vmax = sp.solve(sp.diff(quad, vd), vd)[0]
    qmax = sp.simplify(quad.subs(vd, vmax))
    ok1 = sp.simplify(qmax - E / (2 - E * f)) == 0
    roots = sp.solve(quad, vd)
    Rds = sorted([sp.simplify(r - 1) for r in roots], key=lambda e: sp.N(e.subs({psi: -0.3, f: 0.5})))
    ok2 = sp.simplify(Rds[0] + 1) == 0 and sp.simplify(Rds[1] - E * f / (2 - E * f)) == 0
    import math
    worst_ang, worst_lo, worst_hi, trapped_ok = 0.0, 0.0, -9.0, True
    for i in range(41):
        ps = -3.0 + 3.0 * i / 40
        for j in range(61):
            ff = -5.0 + 6.0 * j / 60
            e = math.exp(ps)
            ang = math.sqrt(e / (2 - e * ff))
            hi = e * ff / (2 - e * ff)
            worst_ang = max(worst_ang, ang)
            worst_hi = max(worst_hi, hi)
            if ff < 0:
                trapped_ok &= hi < 0
    ok3 = worst_ang <= 1 + 1e-12 and worst_hi <= 1 + 1e-12 and trapped_ok
    e_bad = 1.9
    ctl = math.sqrt(1.0 / (2 - e_bad)) > 1                # psi = 0, f = 1.9 (f > 1): R|dOmega| up to sqrt(10)
    print("S7 max R^2|dOmega|^2 = e^psi/(2 - e^psi f):", ok1, "; dR in [-1, e^psi f/(2 - e^psi f)]:", ok2,
          "; on psi in [-3,0], f in [-5,1]: R|dOmega| <= %.6f, dR <= %.6f, dR < 0 where f < 0: %s"
          % (worst_ang, worst_hi, trapped_ok))
    print("   control: e^psi f = 1.9 gives R|dOmega| up to %.4f > 1: %s" % (math.sqrt(1.0 / (2 - e_bad)), ctl))
    return ok1 and ok2 and ok3 and ctl


if __name__ == '__main__':
    res = [s1()]
    print("S2, S3, S5 (exact at rational jets, a general 5D metric, covector field and density)")
    res += [s2_s3_s5(sd) for sd in (2, 9, 31)]
    res += [s4(), s6(), s7()]
    print("PASS" if all(res) else "FAIL")
    sys.exit(0 if all(res) else 1)
