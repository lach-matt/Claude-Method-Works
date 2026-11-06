"""r6sigma5.py -- SETTLE-GLAM5 round 6: F_4 exists and cancels the degree -6 part of P(g_b0 + Sigma) on the full
five-dimensional gauge-fixed operator (P(Sigma) = O(lam r^(-13/2)) with Sigma_4), and the weight window (l0 - 1, 3)
computed as a whole from exponents measured on fields (the round-5 verifier's list of claims no check exercises).
P(h) := Ric^H(g_b0 + h; g_b0), g_b0 := eta + mu r^-2 k k, mu = 4/5, Cartesian; f1lemma5.py's jets and Ric^H
(imported, not copied); Sigma_2 := (3/10) r^-2 P, P = f1lemma5.PMAT, the l = 0 field of r5op5 O2.

  S1 (exact, sympy) the degree -4 equation: for every F and every harmonic polynomial h_l of degree l = 0..4,
     -(1/2) box_eta (r^-4 F(s) h_l(x) r^-l) = r^-6 h_l r^-l L_l[F], s := (t + r - v1)/r,
     L_l[F] := (s - s^2/2) F'' + (7/2)(1 - s) F' - (1/2)(8 - l(l + 2)) F  (SETTLE-GLAM5 R5-C (v)).
     Control (the code mutated: (7/2) replaced by 3): the identity fails.
  S2 (exact) Frobenius at s = 0: the indicial roots are 0 and -5/2 (difference not an integer); with
     F = sum f_n s^n and S = sum S_n s^n, (n + 1)(n + 7/2) f_(n+1) = S_n + (n(n - 1)/2 + 7n/2 + kappa_l) f_n,
     kappa_l := (8 - l(l + 2))/2, so the solution analytic at 0 is unique given f_0 = F(0), and f_(n+1)/f_n -> 1/2
     (radius 2: s - s^2/2 vanishes again only at s = 2), covering s in [0, 3/2]. For the constant source -1 (the
     static case below): l != 2, F = 2/(8 - l(l + 2)); l = 2, F = -(2/7) s 3F2(1, 1, 7; 2, 9/2; s/2), checked against
     the recursion to order 60 and in L_2 at s = 0.3, 0.9, 1.5 (40 digits). Control: at l = 2 a constant is not a
     solution (L_2[c] = 0).
  S3 (exact, polynomial algebra) the degree -6 part Q_6 of P(g_b0 + Sigma_2): Ric^H(eta + e m + d sigma; eta + e m),
     m := mu r^-2 k k, sigma := Sigma_2, expanded exactly to second order in (e, d) as polynomials in (x, w := 1/r)
     with d_i w = -x_i w^3, and restricted to S^3 harmonic by harmonic (Gauss decomposition, each piece checked
     harmonic). Self-checks: the e and e^2 parts vanish (Tangherlini is vacuum) and the d part vanishes (r^-2 is
     harmonic in R^4); Q_6 := the (e d) + (d^2) part has harmonics l = 0, 1, 2 only, and agrees with the full
     operator's r^6 P(g_b0 + Sigma_2) along the ray (Richardson, r = 128, 512) to 1e-6.
  S4 (computed, 40 digits, full operator) Sigma_4 := r^-4 sum_l F_l(s) H_l(xhat), H_l the harmonic pieces of Q_6
     and L_l[F_l] = -1 (so -(1/2) box Sigma_4 = -Q_6): the fitted decay of |P| along the ray (s = 1/2,
     r = 8 .. 2048) is 6 for Sigma_2, 8 for Sigma_2 + Sigma_4 (degree -6 cancelled; next degree -8), 13/2 for
     Sigma_2 + Sigma_(5/2) + Sigma_4 (the mu Sigma_(5/2) and Sigma_2 Sigma_(5/2) terms). Controls (the code
     mutated): the l = 2 piece with a constant F (static, but not a solution of L_2 F = -1), and -Sigma_4: decay 6
     each; Sigma_2 + Sigma_(5/2) without Sigma_4: decay 6.
  W the window. Its a-dependent conditions, each an exponent: W1 the cap's, measured (below); W2 the N-flux tail's,
     exact on the field; W3 the residual's kernel from the degree measured in S4; and, counted by hand from typed
     scaling rules ([arithmetic]), W4 the h_R rows (S1's scale-invariant F of R^(2a+3) F^2 gives a + 3/2, its integral
     from infinity a + 1/2; the coefficient rows of r5op5 O1 do not depend on a), W5 the class on S (r = 1/rho turns
     int r^(2a+1) phi^2 dr into int (rho^-(a+1) phi)^2 drho/rho: exponent a + 1, inside rho^(l0) L^2_b for
     a + 1 > l0), W6 Step 2 (a + 1/2 >= 2), W7 Lemma R4.5 (widened: the flux and int r^(2a-8) dr finite exactly for
     a < 7/2, Lemma R3.2 on (0, 7/2)), W8 Proposition R5.2 (min(3, a + 1/2) > 1).
     W1 in detail: the energy of the truncation's data on the band at t = T (the exact h_R of r5settle5 G1, its
        expansion at fixed v through r^-5, smoothstep cut-off, weight (2r)^(2a), l = 2) measured at |T| = 1e5, 1e6,
        1e7 for 13 values of a in [1/2, 7/2]: the measured exponents are the affine law 2a - 6 (least squares, its
        coefficients identified as rationals, residual below 2e-3), so the cap -> 0 exactly for a < 3.
     W: the intersection, as sympy intervals, is (l0 - 1, 3) for l0 = 3.1, 3.3, 3.6, 3.9; its upper end comes from
     the measured cap exponent and its lower end from W5's exponent (round 7: round 6 typed the lower end l0 - 1 in
     the window, and W5's result was not used). Controls (the field or a condition mutated): p = 4 dropped from
     Sigma (W1-W2 recomputed on that field: 2a - 5, 2a - 6) gives (l0 - 1, 5/2) and nothing for l0 >= 7/2; Lemma
     R4.5 on (5/2, 7/2) gives (max(l0 - 1, 5/2), 3); q_R = 6 (F_4 with no source) leaves the window unchanged; and
     W5's exponent mutated to a + 1/2 moves the lower end to l0 - 1/2 (W''', round 7).
Labels: computed (S1-S3 exact; S4 mpmath at 40 digits; W1 mpmath quadrature at 30 digits, W2-W3 exact sympy);
W4-W8 [arithmetic] (exponents of typed scaling rules, solved exactly).

    python3 checks/r6sigma5.py     (18 to 29 minutes on this loaded machine, beside the others; S4 most of it)
"""
import os
import random
import sys
import time

import mpmath as mp
import sympy as sp
from sympy import QQ, Rational as Q
from sympy.polys.rings import ring

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import f1lemma5 as F  # noqa: E402

FAIL = []
print = F.print


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


V1 = Q(7, 10)
xs = sp.symbols("x1 x2 x3 x4")


# ================================================================ S1: the degree -4 equation

def L_op(Fx, s, l, c72=Q(7, 2)):
    return (s - s**2/2)*sp.diff(Fx, s, 2) + c72*(1 - s)*sp.diff(Fx, s) - Q(1, 2)*(8 - l*(l + 2))*Fx


def part_s1():
    print("S1  the degree -4 equation of R5-C (v), from the flat operator")
    t, x1, x2, x3, x4 = F.XS
    RR = F.RR
    s = sp.Symbol("s")
    S = (t + RR - V1)/RR
    harm = {0: sp.Integer(1), 1: x1, 2: x1*x2, 3: x1*x2*x3, 4: x1*x2*x3*x4}
    pts = ({t: Q(1, 3), x1: Q(2), x2: Q(-1), x3: Q(1, 2), x4: Q(3)},
           {t: Q(-2), x1: Q(1), x2: Q(1), x3: Q(-3), x4: Q(1, 5)})
    ok, ctl = True, True
    for l, h in harm.items():
        for Ft in (sp.exp(s/3), 1 + s**3):
            u = RR**-4*Ft.subs(s, S)*h/RR**l
            lhs = (sp.diff(u, t, 2) - sum(sp.diff(u, xx, 2) for xx in (x1, x2, x3, x4)))/2
            rhs = RR**-6*h/RR**l*L_op(Ft, s, l).subs(s, S)
            rhs_m = RR**-6*h/RR**l*L_op(Ft, s, l, c72=Q(3)).subs(s, S)
            for pt in pts:
                ok = ok and abs(sp.N((lhs - rhs).subs(pt), 40)) < 1e-30
                ctl = ctl and abs(sp.N((lhs - rhs_m).subs(pt), 40)) > 1e-20  # the identity holds to 1e-30
    check("S1 -(1/2) box_eta (r^-4 F(s) h_l r^-l) = r^-6 h_l r^-l L_l[F] (l = 0..4, two test F, two points, 40 digits)",
          ok)
    check("S1' control (the code mutated: 7/2 -> 3 in L_l): the identity fails at every case", ctl)


# ================================================================ S2: Frobenius

def part_s2():
    print("S2  Frobenius at s = 0, and the solutions for the constant source -1")
    s, rho = sp.symbols("s rho")
    l = sp.Symbol("l")
    ind = sp.expand((s*sp.diff(s**rho, s, 2) + Q(7, 2)*sp.diff(s**rho, s))/s**(rho - 1))
    roots = sp.solve(ind, rho)
    check("S2a the indicial roots of L_l at s = 0 are 0 and -5/2 (difference not an integer)",
          sorted(roots) == [Q(-5, 2), 0], str(roots))
    n = sp.Symbol("n", nonnegative=True)
    kap = (8 - l*(l + 2))/2
    lead = (n + 1)*(n + Q(7, 2))
    ratio = sp.limit((n*(n - 1)/2 + Q(7, 2)*n + kap)/lead, n, sp.oo)
    zeros = sp.solve(s - s**2/2, s)
    check("S2b (n + 1)(n + 7/2) f_(n+1) = S_n + (n(n - 1)/2 + 7n/2 + kappa_l) f_n: the leading factor never vanishes "
          "for n >= 0 (unique analytic solution given F(0)); f_(n+1)/f_n -> 1/2: radius 2, the other zero of s - s^2/2",
          ratio == Q(1, 2) and sorted(zeros) == [0, 2] and not any(r_ >= 0 for r_ in sp.solve(lead, n)),
          f"ratio {ratio}, zeros {zeros}")
    ok = True
    for lv in (0, 1, 3, 4):
        c = Q(2, 8 - lv*(lv + 2))
        ok = ok and sp.simplify(L_op(c + 0*s, s, lv) + 1) == 0
    # l = 2: the recursion with S_n = -delta_(n0), f_0 = 0, against the closed form
    f_ = [sp.Integer(0)]
    for k in range(0, 60):
        Sn = -1 if k == 0 else 0
        f_.append((Sn + (Q(k*(k - 1), 2) + Q(7, 2)*k + 0)*f_[k])/((k + 1)*(k + Q(7, 2))))
    closed = [sp.Integer(0)] + [-Q(2, 7)*sp.rf(7, k)/(sp.rf(Q(9, 2), k)*(k + 1))/2**k for k in range(0, 60)]
    ok2 = all(sp.simplify(f_[k] - closed[k]) == 0 for k in range(61))
    mp.mp.dps = 40
    F2 = lambda x: -mp.mpf(2)/7*x*mp.hyp3f2(1, 1, 7, 2, mp.mpf(9)/2, x/2)
    res = []
    for x in (mp.mpf("0.3"), mp.mpf("0.9"), mp.mpf("1.5")):
        d1 = mp.diff(F2, x)
        d2 = mp.diff(F2, x, 2)
        res.append(abs((x - x**2/2)*d2 + mp.mpf(7)/2*(1 - x)*d1 + 1))
    ctl = sp.simplify(L_op(Q(5, 3) + 0*s, s, 2)) == 0
    check("S2c the constant source -1: F = 2/(8 - l(l + 2)) for l = 0, 1, 3, 4 (exact); at l = 2 the recursion gives "
          "F = -(2/7) s 3F2(1, 1, 7; 2, 9/2; s/2) (exact to order 60) and L_2 F + 1 = 0 at s = 0.3, 0.9, 1.5 "
          "(40 digits)", ok and ok2 and max(res) < mp.mpf(10)**-25, f"max residual {mp.nstr(max(res), 3)}")
    check("S2c' control: at l = 2 a constant is a homogeneous solution (L_2[c] = 0), so no constant answers the "
          "source: F_4 depends on s", ctl)


# ================================================================ S3: Q_6, exactly

Rg, X1, X2, X3, X4, W = ring("x1,x2,x3,x4,w", QQ)
XR = [None, X1, X2, X3, X4]
N5 = 5
ETA = [-1, 1, 1, 1, 1]


def Dr(f, a):
    if a == 0:
        return Rg.zero  # static fields
    return f.diff(XR[a]) - XR[a]*W**3*f.diff(W)


def tadd(A, B, s=1):
    out = dict(A)
    for key, v in B.items():
        out[key] = out.get(key, Rg.zero) + s*v
    return out


def tmul(A, B, order=2):
    out = {}
    for (i, j), u in A.items():
        for (p, q), v in B.items():
            if i + p + j + q <= order:
                out[(i + p, j + q)] = out.get((i + p, j + q), Rg.zero) + u*v
    return out


def tscal(A, c):
    return {key: c*v for key, v in A.items()}


def tdiff(A, a):
    return {key: Dr(v, a) for key, v in A.items()}


def christ_t(gi, dh):
    low = [[[tadd(tadd(dh[s][b][a], dh[s][a][b]), dh[a][b][s], -1) for b in range(N5)] for a in range(N5)]
           for s in range(N5)]
    G = [[[None]*N5 for _ in range(N5)] for _ in range(N5)]
    for r_ in range(N5):
        for a in range(N5):
            for b in range(a, N5):
                acc = {}
                for s in range(N5):
                    acc = tadd(acc, tmul(gi[r_][s], low[s][a][b]))
                G[r_][a][b] = G[r_][b][a] = tscal(acc, Q(1, 2))
    return G


def ricH_series(mu, amp, pmat):
    """Ric^H(eta + e m + d sigma; eta + e m) to second order in (e, d), as {(i, j): ring element} per component"""
    k = [Rg.one, X1*W, X2*W, X3*W, X4*W]
    h = [[{(1, 0): mu*W**2*k[a]*k[b], (0, 1): amp*pmat[a][b]*W**2} for b in range(N5)] for a in range(N5)]
    H = [[tscal(h[a][b], ETA[a]*ETA[b]) for b in range(N5)] for a in range(N5)]
    HH = [[{} for _ in range(N5)] for _ in range(N5)]
    for a in range(N5):
        for b in range(N5):
            acc = {}
            for c in range(N5):
                acc = tadd(acc, tmul(H[a][c], tscal(H[c][b], ETA[c])))
            HH[a][b] = acc

    def ginv(a, b):
        out = tadd(tscal(H[a][b], -1), HH[a][b])
        return tadd(out, {(0, 0): Rg(ETA[a])}) if a == b else out
    gi = [[ginv(a, b) for b in range(N5)] for a in range(N5)]
    gL = [[tadd(dict(h[a][b]), {(0, 0): Rg(ETA[a])}) if a == b else dict(h[a][b]) for b in range(N5)]
          for a in range(N5)]
    dh = [[[tdiff(h[a][b], c) for c in range(N5)] for b in range(N5)] for a in range(N5)]
    G = christ_t(gi, dh)
    only_e = lambda A: {key: v for key, v in A.items() if key[1] == 0}
    G0 = christ_t([[only_e(gi[a][b]) for b in range(N5)] for a in range(N5)],
                  [[[only_e(dh[a][b][c]) for c in range(N5)] for b in range(N5)] for a in range(N5)])
    Ric = [[None]*N5 for _ in range(N5)]
    for a in range(N5):
        for b in range(a, N5):
            acc = {}
            for c in range(N5):
                acc = tadd(acc, tdiff(G[c][a][b], c))
                acc = tadd(acc, tdiff(G[c][a][c], b), -1)
                for d_ in range(N5):
                    acc = tadd(acc, tmul(G[c][c][d_], G[d_][a][b]))
                    acc = tadd(acc, tmul(G[c][b][d_], G[d_][a][c]), -1)
            Ric[a][b] = Ric[b][a] = acc
    Dv = []
    for q in range(N5):
        acc = {}
        for a in range(N5):
            for b in range(N5):
                acc = tadd(acc, tmul(gi[a][b], tadd(G[q][a][b], G0[q][a][b], -1)))
        Dv.append(acc)
    nab = [[tdiff(Dv[q], m) for q in range(N5)] for m in range(N5)]
    for m in range(N5):
        for q in range(N5):
            for l_ in range(N5):
                nab[m][q] = tadd(nab[m][q], tmul(G0[q][m][l_], Dv[l_]))
    RH = [[None]*N5 for _ in range(N5)]
    for a in range(N5):
        for b in range(a, N5):
            acc = dict(Ric[a][b])
            for q in range(N5):
                acc = tadd(acc, tmul(gL[a][q], nab[b][q]), -Q(1, 2))
                acc = tadd(acc, tmul(gL[b][q], nab[a][q]), -Q(1, 2))
            RH[a][b] = RH[b][a] = acc
    return RH


def on_sphere(p):
    e = sp.Integer(0)
    for mon, cf in p.terms():
        e += sp.Rational(cf.numerator, cf.denominator)*sp.Mul(*[xs[i]**mon[i] for i in range(4)])
    return sp.Poly(e, *xs)


def lap(P):
    return sum(P.diff(x).diff(x) for x in xs)


R2 = sp.Poly(sum(x**2 for x in xs), *xs)


def harm_proj(P, n, d=4):
    """the harmonic part of a homogeneous polynomial of degree n in R^d (checked harmonic by the caller)"""
    out, L, c, R2j = sp.Poly(0, *xs), P, sp.Integer(1), sp.Poly(1, *xs)
    for j in range(0, n//2 + 1):
        out += R2j*L*c
        L, R2j = lap(L), R2j*R2
        c = -c/(2*(j + 1)*(2*n + d - 4 - 2*j))
    return out


def decompose(P):
    """the restriction of P to S^3 as {l: harmonic homogeneous polynomial of degree l}"""
    homog, out = {}, {}
    for mon, cf in P.terms():
        n = sum(mon)
        homog[n] = homog.get(n, sp.Poly(0, *xs)) + sp.Poly(cf*sp.Mul(*[xs[i]**mon[i] for i in range(4)]), *xs)
    for n, rem in homog.items():
        deg = n
        while not rem.is_zero:
            hp = harm_proj(rem, deg)
            assert lap(hp).is_zero
            q_, rr = sp.div(rem - hp, R2)
            assert rr.is_zero
            out[deg] = out.get(deg, sp.Poly(0, *xs)) + hp
            rem, deg = q_, deg - 2
    return {l: hp for l, hp in out.items() if not hp.is_zero}


MU = Q(4, 5)
AMP = Q(3, 10)


def part_s3():
    print("S3  the degree -6 part of P(g_b0 + Sigma_2), exactly")
    pm = [[Q(int(F.PMAT[a, b]*7), 7) for b in range(5)] for a in range(5)]
    RH = ricH_series(MU, AMP, pm)
    pieces = {}
    for key in ((1, 0), (2, 0), (0, 1)):
        pieces[key] = sum(len(decompose(on_sphere(RH[a][b].get(key, Rg.zero)))) for a in range(5)
                          for b in range(a, 5))
    check("S3a self-checks: the e and e^2 parts (Ric(g_b0) = 0) and the d part (box r^-2 = 0 in R^4) vanish on S^3",
          all(v == 0 for v in pieces.values()), str(pieces))
    Q6 = {}
    for a in range(5):
        for b in range(a, 5):
            Q6[(a, b)] = decompose(on_sphere(RH[a][b].get((1, 1), Rg.zero) + RH[a][b].get((0, 2), Rg.zero)))
    ls = sorted({l for d in Q6.values() for l in d})
    check("S3b Q_6 := the (e d) + (d^2) part is not 0 and has the harmonics l = 0, 1, 2 only", ls == [0, 1, 2]
          and any(Q6[k] for k in Q6), str(ls))
    return Q6


# ================================================================ S4: on the full operator

XH = [mp.mpf("0.5")]*4
RAYS = (8, 32, 128, 512, 2048)


def ray_point(r, s=mp.mpf("0.5")):
    r = mp.mpf(r)
    return [mp.mpf("0.7") + (s - 1)*r] + [r*c for c in XH]


def fit(vals):
    return [float(mp.log(vals[i - 1]/vals[i])/mp.log(4)) for i in range(1, len(vals))]


def part_s4(Q6):
    print("S4  Sigma_4 on the full operator: the decay of P along a ray of W (s = 1/2)")
    mp.mp.dps = 40
    t, x1, x2, x3, x4 = F.XS
    RR = F.RR
    S = (t + RR - V1)/RR
    sub = dict(zip(xs, [x1, x2, x3, x4]))
    Fl = {0: Q(1, 4), 1: Q(2, 5), 2: -Q(2, 7)*S*sp.hyper([1, 1, 7], [2, Q(9, 2)], S/2)}

    def sigma4(F_l2=None, sign=1):
        M = sp.zeros(5, 5)
        for (a, b), dec in Q6.items():
            e = 0
            for l, hp in dec.items():
                Fx = Fl[l] if (l != 2 or F_l2 is None) else F_l2
                e += Fx*hp.as_expr().subs(sub)/RR**l
            M[a, b] = M[b, a] = sign*e/RR**4
        return M
    G0 = F.gb0()
    J0 = F.Jets(G0)
    Sig2 = RR**-2*F.PMAT*AMP
    Sig52 = RR**Q(-5, 2)*sp.hyper([Q(5, 2), Q(1, 2)], [2], S/2)*F.PMAT*AMP
    S4 = sigma4()
    cases = (("Sigma_2", Sig2), ("Sigma_2 + Sigma_4", Sig2 + S4), ("Sigma_2 + Sigma_(5/2) + Sigma_4", Sig2 + Sig52 + S4),
             ("control: l = 2 piece constant", Sig2 + sigma4(F_l2=Q(1, 3))),
             ("control: -Sigma_4", Sig2 + sigma4(sign=-1)),
             ("control: Sigma_2 + Sigma_(5/2), no Sigma_4", Sig2 + Sig52))
    res, mats = {}, {}
    for name, Sg in cases:
        Js = F.Jets(G0 + Sg)
        Ms = [F.ricH(Js.at(ray_point(r), 0), J0.at(ray_point(r), 0)) for r in RAYS]
        mats[name] = Ms
        res[name] = fit([mp.mnorm(M, 1) for M in Ms])
    # S3's Q_6 against the operator: r^6 P(g_b0 + Sigma_2) at r = 256, 512, Richardson (next term r^-8)
    xh = {x_: sp.Rational(1, 2) for x_ in xs}
    Ms2 = mats["Sigma_2"]
    r1, r2 = mp.mpf(128), mp.mpf(512)
    worst = mp.mpf(0)
    for (a, b), dec in Q6.items():
        exact = sum(sp.N(hp.as_expr().subs(xh), 45) for hp in dec.values())
        v1_, v2_ = Ms2[2][a, b]*r1**6, Ms2[3][a, b]*r2**6
        rich = (16*v2_ - v1_)/15
        worst = max(worst, abs(rich - mp.mpf(str(exact))))
    check("S3c Q_6 (exact) agrees with the full operator's r^6 P(g_b0 + Sigma_2) on the ray (Richardson, r = 128, "
          "512; next term r^-8)", worst < mp.mpf(10)**-6, f"max difference {mp.nstr(worst, 3)}")
    tl = {k: v[-1] for k, v in res.items()}
    print("    fitted decay exponents (r = 8 .. 2048):", {k: [round(x, 4) for x in v] for k, v in res.items()})
    check("S4 |P(g_b0 + Sigma_2)| decays like r^-6, |P(g_b0 + Sigma_2 + Sigma_4)| like r^-8 (F_4 cancels degree -6), "
          "|P(g_b0 + Sigma_2 + Sigma_(5/2) + Sigma_4)| like r^(-13/2): P(Sigma) = O(lam r^(-13/2)) with Sigma_4",
          abs(tl["Sigma_2"] - 6) < 0.02 and abs(tl["Sigma_2 + Sigma_4"] - 8) < 0.02
          and abs(tl["Sigma_2 + Sigma_(5/2) + Sigma_4"] - 6.5) < 0.05)
    check("S4' controls (the l = 2 piece constant; -Sigma_4; no Sigma_4 with Sigma_(5/2)): decay 6 each",
          all(abs(tl[k] - 6) < 0.05 for k in tl if k.startswith("control")))
    return round(2*tl["Sigma_2 + Sigma_(5/2) + Sigma_4"])/sp.Integer(2), \
        round(2*tl["control: Sigma_2 + Sigma_(5/2), no Sigma_4"])/sp.Integer(2)


# ================================================================ W: the window, computed

def part_w(qR, qR_flat):
    print("W  the weight window: the cap's and the tail's exponents measured (W1-W2), the residual's degree measured "
          "(S4); the rows', the class's and Step 2's exponents counted by hand ([arithmetic], W4-W8)")
    import r5settle5 as R5
    a = sp.Symbol("a", positive=True)
    rnd = random.Random(41)
    cs = {k: sp.Rational(rnd.randint(1, 9), rnd.randint(1, 5))*rnd.choice([1, -1]) for k in range(4, 10)}
    cs[10] = sp.Rational(3, 7)
    vv = sp.Symbol("vv")
    Pi = [sp.Integer(2), Q(5, 2), sp.Integer(3), Q(7, 2), sp.Integer(4)]
    G = R5.flat_truth(cs, vv, kmax=10)

    def hR_coeffs(Pi_):
        Sg = R5.sigma_coeffs(cs, vv, Pi_, kmax=10)
        return {k: sp.expand(G[k] - Sg[k]) for k in range(4, 11)}
    fields = {"Sigma with p = 4": hR_coeffs(Pi), "control: p = 4 dropped": hR_coeffs(Pi[:-1])}
    lead = {n: min(Q(k, 2) for k, c in d.items() if c != 0) for n, d in fields.items()}
    print("    h_R's leading decay at fixed v (exact):", {n: str(v) for n, v in lead.items()})
    mp.mp.dps = 30
    v1, Vb, dl = mp.mpf("0.7"), mp.mpf("1.7"), mp.mpf("0.5")

    def chi(v):
        if v <= Vb:
            return mp.mpf(0), mp.mpf(0)
        x = (v - Vb)/dl
        return (3*x**2 - 2*x**3, (6*x - 6*x**2)/dl) if x < 1 else (mp.mpf(1), mp.mpf(0))
    a_grid = [Q(n, 4) for n in range(2, 15)]
    cap_exp, flux_exp = {}, {}
    for name, d in fields.items():
        cf = {k: sp.lambdify(vv, c, "mpmath") for k, c in d.items() if c != 0}
        dcf = {k: sp.lambdify(vv, sp.diff(c, vv), "mpmath") for k, c in d.items() if c != 0}

        def cap(T, av):
            def dens(v):
                r = v + T
                c, cp = chi(v)
                h = sum(cf[k](v)*r**(-mp.mpf(k)/2) for k in cf)
                hv = sum(dcf[k](v)*r**(-mp.mpf(k)/2) for k in cf)
                hr = sum(-mp.mpf(k)/2*cf[k](v)*r**(-mp.mpf(k)/2 - 1) for k in cf)
                dt = (1 - c)*hv - cp*h               # d_t at fixed x of the cut data = d_v at fixed r
                drr = (1 - c)*(hv + hr) - cp*h        # d_r at fixed t (v = t + r)
                return (2*r)**(2*av)*(dt**2 + drr**2 + 8*((1 - c)*h)**2/r**2)*r**3
            return mp.quad(dens, [v1, Vb, Vb + dl])
        ce = {}
        for av in a_grid:
            avm = mp.mpf(av.p)/av.q
            c5, c6, c7 = [cap(mp.mpf(10)**e, avm) for e in (5, 6, 7)]
            ce[av] = (float(mp.log(c6/c5)/mp.log(10)), float(mp.log(c7/c6)/mp.log(10)))
        cap_exp[name] = ce
        rS, RS = sp.symbols("rS RS", positive=True)
        ph = sum(rS**Q(-k, 2)*c.subs(vv, V1) for k, c in d.items() if c != 0)
        fe = {}
        for av in a_grid:
            dens = sp.expand((2*rS)**(2*av)*(sp.diff(ph, rS)**2 + 8*ph**2/rS**2)*rS**3)
            # the tail int_R^oo of c r^e is R^(e + 1): the largest such exponent over the terms
            fe[av] = max(sp.Rational(tm.as_coeff_exponent(rS)[1]) for tm in sp.Add.make_args(dens)) + 1
        flux_exp[name] = fe

    def crossing(meas):
        """the measured exponents fitted by an affine function of a (least squares), its coefficients identified as
        rationals of denominator at most 20 (tolerance 1e-3, the fit's residual checked below 2e-3), and its zero"""
        pts = sorted((float(k), float(v)) for k, v in meas.items())
        n_ = len(pts)
        sx, sy = sum(p_[0] for p_ in pts), sum(p_[1] for p_ in pts)
        sxx, sxy = sum(p_[0]**2 for p_ in pts), sum(p_[0]*p_[1] for p_ in pts)
        slope = (n_*sxy - sx*sy)/(n_*sxx - sx**2)
        icpt = (sy - slope*sx)/n_
        sl_q = sp.nsimplify(slope, tolerance=1e-3, rational=True)
        ic_q = sp.nsimplify(icpt, tolerance=1e-3, rational=True)
        resid = max(abs(y - (float(sl_q)*x + float(ic_q))) for x, y in pts)
        assert sl_q.q <= 20 and ic_q.q <= 20 and resid < 2e-3, (slope, icpt, resid)
        return -ic_q/sl_q, (sl_q, ic_q, resid)
    x_cap, fit_cap = crossing({av: v[1] for av, v in cap_exp["Sigma with p = 4"].items()})
    x_cap7, fit_cap7 = crossing({av: v[1] for av, v in cap_exp["control: p = 4 dropped"].items()})
    check("W1 the cap's measured exponents (13 values of a in [1/2, 7/2], |T| = 1e6 .. 1e7) are the affine law 2a - 6 "
          "(fit residual below 2e-3): the cap vanishes exactly for a < 3", fit_cap[:2] == (2, -6) and x_cap == 3,
          f"fit (slope, intercept, residual) {[str(fit_cap[0]), str(fit_cap[1]), round(fit_cap[2], 5)]}; p = 4 dropped: "
          f"{[str(fit_cap7[0]), str(fit_cap7[1])]}, zero {x_cap7}; samples (a, exponent): "
          + str([(str(av), round(v[1], 4)) for av, v in list(cap_exp["Sigma with p = 4"].items())[::4]]))
    x_fl, _ = crossing({av: float(v) for av, v in flux_exp["Sigma with p = 4"].items()})
    x_fl7, _ = crossing({av: float(v) for av, v in flux_exp["control: p = 4 dropped"].items()})
    ok2 = all(flux_exp["Sigma with p = 4"][av] == 2*av - 7 for av in a_grid)
    check("W2 the N-flux tail of h_R(v1, .) has exponent 2a - 7 (exact, 13 values of a): finite and vanishing "
          "exactly for a < 7/2", ok2 and x_fl == Q(7, 2), f"zero {x_fl}; p = 4 dropped: {x_fl7}")
    rho, r_ = sp.symbols("rho r", positive=True)

    def power(expr):
        """e with expr = const * rho^e (sympy)"""
        return sp.simplify(sp.expand_log(sp.log(sp.simplify(expr/expr.subs(rho, 1))), force=True)/sp.log(rho))

    def kernel_cond(q):
        I = sp.integrate((2*r_)**(2*a)*r_**(-2*q)*r_**3, (r_, rho, sp.oo), conds="none")
        e = power(I)/2   # ||(2r)^a r^-q||_(L^2(r >= rho)) is a constant times rho^e
        return sp.solve_univariate_inequality(-e > 1, a, relational=False) & sp.Interval.open(0, q - 2)
    res_set, res_set_flat = kernel_cond(qR), kernel_cond(qR_flat)
    check("W3 the residual's kernel from the measured degree q_R (S4): integrable in sigma exactly for a < q_R - 3",
          res_set == sp.Interval.open(0, qR - 3) and res_set_flat == sp.Interval.open(0, qR_flat - 3),
          f"q_R = {qR}: {res_set}; q_R = {qR_flat} (F_4 with no source): {res_set_flat}")
    R_, c_ = sp.symbols("R c", positive=True)
    beta1 = sp.solve(sp.Eq(sp.diff(sp.log(R_**(2*a + 3)*R_**(-2*c_)), R_), 0), c_)[0]
    beta0 = -power(sp.integrate(r_**(-beta1), (r_, rho, sp.oo), conds="none"))
    rows = {"B(H) . d phi, deformation": beta1, "C(H) phi through Hardy, (B)": beta1 - 1}
    rows_set = sp.Intersection(*[sp.solve_univariate_inequality(q > 1, a, relational=False) for q in rows.values()])
    check("W4 [arithmetic: the scaling rules entered] S1's pointwise exponent is a + 3/2 and its integral from "
          "infinity a + 1/2 (sympy); the h_R rows 3/2 + a "
          "and a + 1/2 are > 1 exactly for a > 1/2; the coefficient rows (r5op5 O1) do not depend on a",
          beta1 == a + Q(3, 2) and beta0 == a + Q(1, 2) and rows_set == sp.Interval.open(Q(1, 2), sp.oo),
          f"beta1 = {beta1}, beta0 = {beta0}, rows > 1 on {rows_set}")
    rr = sp.Symbol("rr", positive=True)
    per = (rr**(2*a + 1)).subs(rr, 1/rho)*sp.diff(1/rho, rho)*(-1)*rho   # r^(2a+1) dr per drho/rho
    cls_exp = sp.simplify(-power(per)/2)
    check("W5 [arithmetic: the weight entered] r = 1/rho: r^(2a+1) dr = rho^(-2(a+1)) drho/rho, the class exponent "
          "a + 1 (sympy); inside rho^(l0) L^2_b "
          "for a + 1 > l0", cls_exp == a + 1, str(cls_exp))
    x_cap_r, x_fl_r, x_cap7_r, x_fl7_r = x_cap, x_fl, x_cap7, x_fl7
    step2 = sp.solve_univariate_inequality(beta0 >= 2, a, relational=False)
    hd = sp.integrate(r_**(2*a - 8), (r_, 1, sp.oo), conds="piecewise")
    cond45 = sp.solve_univariate_inequality(hd.args[0].cond, a, relational=False)   # sympy's convergence condition
    lem45 = sp.Interval.open(0, x_fl_r) & cond45 & sp.Interval.open(0, Q(8 - 1, 2))
    r52 = sp.solve_univariate_inequality(sp.Min(3, a + Q(1, 2)) > 1, a, relational=False)
    check("W6-W8 [arithmetic: the thresholds entered] Step 2: a + 1/2 >= 2 on [3/2, oo); Lemma R4.5 widened: the "
          "flux (W2) and int r^(2a-8) dr (sympy's "
          "own convergence condition) finite on (0, 7/2), Lemma R3.2 on (0, (J' - 1)/2) = (0, 7/2); Proposition "
          "R5.2: min(3, a + 1/2) > 1 on (1/2, oo)",
          step2 == sp.Interval(Q(3, 2), sp.oo) and lem45 == sp.Interval.open(0, Q(7, 2))
          and r52 == sp.Interval.open(Q(1, 2), sp.oo), f"{step2}, {lem45}, {r52}")

    def window(l0v, capx, flx, lemma45, rs, cls=cls_exp):
        # [R7 (minor 2)] the class's lower end is W5's computed exponent, not typed: a with cls(a) > l0
        cls_set = sp.solve_univariate_inequality(cls > l0v, a, relational=False)
        sets = [sp.Interval.open(0, capx), sp.Interval.open(0, flx), rs, rows_set,
                cls_set, step2, lemma45, r52]
        return sp.Intersection(*sets)
    ok, ctl_a, ctl_b, ctl_c, ctl_d, info = True, True, True, True, True, {}
    for l0v in (Q(31, 10), Q(33, 10), Q(36, 10), Q(39, 10)):
        w = window(l0v, x_cap_r, x_fl_r, lem45, res_set)
        info[str(l0v)] = str(w)
        ok = ok and w == sp.Interval.open(l0v - 1, 3)
        wa = window(l0v, x_cap7_r, x_fl7_r, lem45, res_set)
        ctl_a = ctl_a and (wa == sp.Interval.open(l0v - 1, Q(5, 2)) if l0v < Q(7, 2) else wa == sp.EmptySet)
        wb = window(l0v, x_cap_r, x_fl_r, sp.Interval.open(Q(5, 2), Q(7, 2)), res_set)
        ctl_b = ctl_b and wb == sp.Interval.open(sp.Max(l0v - 1, Q(5, 2)), 3)
        wc = window(l0v, x_cap_r, x_fl_r, lem45, res_set_flat)
        ctl_c = ctl_c and wc == w
        wd = window(l0v, x_cap_r, x_fl_r, lem45, res_set, cls=cls_exp - Q(1, 2))
        ctl_d = ctl_d and wd == (sp.Interval.open(l0v - Q(1, 2), 3) if l0v < Q(7, 2) else sp.EmptySet)
    check("W the intersection of the conditions is (l0 - 1, 3) for l0 = 3.1, 3.3, 3.6, 3.9 (its upper end from the "
          "measured cap exponent, its lower end from W5's class exponent)", ok, str(info))
    check("W' controls: p = 4 dropped from Sigma (W1-W2 recomputed: crossings 5/2 and 3) gives (l0 - 1, 5/2), empty "
          "for l0 >= 7/2; Lemma R4.5 on (5/2, 7/2) gives (max(l0 - 1, 5/2), 3)", ctl_a and ctl_b)
    check("W'' with q_R = 6 (F_4 without its source: P(Sigma) = O(lam r^-6), measured in S4) the window is unchanged: "
          "the cap's a < 3 binds first (R6.0 (r6-F4))", ctl_c)
    check("W''' [R7] control (W5's class exponent mutated to a + 1/2): the window's lower end moves to l0 - 1/2, so W "
          "uses W5's result", ctl_d)


def main():
    t0 = time.time()
    part_s1()
    part_s2()
    Q6 = part_s3()
    qR, qR_flat = part_s4(Q6)
    part_w(qR, qR_flat)
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
