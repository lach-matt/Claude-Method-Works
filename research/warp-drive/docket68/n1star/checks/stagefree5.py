#!/usr/bin/env python3
"""stagefree5.py -- the free stage-N data decide the deep layer for Theorem 1's g_lam (EQUALITY5-LAYER.md, Round 4,
R4.2: Proposition L.19).

As the supplement stands, stage N's data are free (Round 3, R3.4).  Adding to stage N's mean the Cauchy data on
Sigma_tau0 of +-2 A grad grad f, f an exact solution of the scalar wave equation of the seed, changes the A-linear part
of g_lam by exactly +-2 lam^N A grad grad f (a pure-gauge solution in the harmonic gauge; its data satisfy the
linearised constraints, so the correction U does not change at first degree).  At the horizon its vv component is
2 lam^N A (d_v^2 f - mu0^(-1/2) d_v f), sign-definite and non-oscillating; with f's profile less flat than env it
dominates the layer's deep part, and the two signs make the boundary spacelike there, or timelike.

  G1 (exact, every f(v, r, th); the operators of layerlin5.py, imported) For h := 2 grad grad f on the seed:
     dD(h)_a = d_a(box f) (lowered), dRic(h) := dRic^H(h) + (1/2)(nabla dD + (nabla dD)^T) = 0 in all fifteen
     components (so the induced data of h satisfy the linearised constraints for every f), and dRic^H(h) = -grad grad
     (box f): with box f = 0, h solves dRic^H(h) = 0 and dD(h) = 0.  Control: h' := 2 d d f (the Hessian without its
     Christoffel term) has dRic(h') != 0.
  G2 (exact) The scalar wave equation box f = 2 (P d_v f - Q f), P := d_r + 3/(2r), Q := -(1/2) r^-3 d_r(r^3 F d_r .),
     solved from past null infinity by f_M := sum_(n<=M) Psi_n(v) b_n(r), b_0 = r^(-3/2), b_(n+1) := P^-1 Q b_n (P^-1
     from infinity), Psi_n := d_v^-n psi: box f_M = -2 Psi_M Q b_M exactly (M = 3); b_1 = -(3/8)(r^(-5/2) + mu0
     r^(-9/2)).  At the horizon (grad grad f_M)_vv = mu0^(-3/4) psi'' - (7/4) mu0^(-5/4) psi' + ..., the Hessian's vv
     component being d_v^2 f - (F'/2) d_v f - (F F'/2) d_r f.  Control: P^-1 with the weight r^(-1/2) in place of
     r^(-3/2) breaks the telescoping.
  G3 (computed, mpmath; a model with unit constants, env = exp(-1/x), psi := env^(2/3), N = 9, M* = 26) At lam =
     10^-100 and 10^-1000: the free term 2 lam^N psi''/2 exceeds ten times the sum of every other term the record bounds
     at the boundary point -- the rule's first-degree part lam^3 eps_26(x), the degree-two part eps_26(x)^2, the
     remainder lam^(N-5) eps_26(x + lam) (Lemma L.4, its tilt reaching v + c lam, c = 1) and its change lam^(N-5)
     psi_26(x + lam) eps_26(x + lam), the margin m0 -- on the whole range [3 lam, x_1], x_1 printed, where env(x_1) is
     about lam^18 = lam^(3N - 9); and at Theorem L's window (env = lam^14) the free term is below a tenth of the signal
     lam^3 env.  Control: psi := env (as flat as env) dominates nowhere on [3 lam, x_b].
  G4 (READ, located by content; md5 printed) N1STAR-PROOF.md: Lemma 6.2's statement ("For every N there are stage data
     ..."), its proof's range ("Stage m = 1, ..., N - 1"), section 6.4 ("Take the stage data of Lemma 6.2 with N := K
     + 3"); the paper: "every smooth choice of stage data" (Theorem A).  Control: no line fixes stage N's data.

Labels: G1, G2 computed (exact, sympy); G3 computed (mpmath), a model with unit constants; G4 READ.
Run: python3 checks/stagefree5.py   (about two minutes; imports layerlin5.py)
"""
import hashlib
import os
import sys
import textwrap
import time

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import layerlin5 as L                                                             # noqa: E402

T0 = time.time()
v, r, th, mu0 = L.v, L.r, L.th, L.mu0
n = L.n
X = L.X


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


# ------------------------------------------------------------------------------------------------------------ G1
def hessian(f, christoffel=True):
    H = sp.zeros(n)
    for a in range(n):
        for b in range(n):
            e = sp.diff(f, X[a], X[b])
            if christoffel:
                e -= sum(L.Gam[c][a][b]*sp.diff(f, X[c]) for c in range(n))
            H[a, b] = e
    return H


def nabla_cov(w):
    """(nabla w)_(n m) = d_n w_m - Gamma^d_(n m) w_d"""
    return [[sp.diff(w[m], X[nn]) - sum(L.Gam[d][nn][m]*w[d] for d in range(n)) for m in range(n)] for nn in range(n)]


def g1(control=False):
    f = sp.Function('f')(v, r, th)
    h = 2*hessian(f, christoffel=not control)
    R, dDl = L.ops(h, twoscale=False)
    DD = nabla_cov(dDl)
    dRic = [[R[m, nn] + (DD[nn][m] + DD[m][nn])/2 for nn in range(n)] for m in range(n)]
    ric_zero = all(L.is_zero(dRic[m][nn]) for m in range(n) for nn in range(m, n))
    if control:
        return ric_zero
    boxf = sum(L.gi[a, b]*hessian(f)[a, b] for a in range(n) for b in range(n))
    dD_ok = all(L.is_zero(dDl[m] - sp.diff(boxf, X[m])) for m in range(n))
    HB = hessian(boxf)
    RH_ok = all(L.is_zero(R[m, nn] + HB[m, nn]) for m in range(n) for nn in range(m, n))
    out("  G1 h = 2 grad grad f, f(v, r, th) arbitrary: dD(h) = d(box f): %s; dRic(h) = 0 (15 components): %s;"
        " dRic^H(h) = -grad grad(box f): %s  [%.0f s]" % (dD_ok, ric_zero, RH_ok, time.time() - T0))
    return dD_ok and ric_zero and RH_ok


# ------------------------------------------------------------------------------------------------------------ G2
q = sp.Symbol('q', positive=True)


def Pinv_inf(S, weight=sp.Rational(3, 2)):
    """r^-w int_infinity^r s^w S(s) ds, termwise in s^(1/2) (a divergent term is refused)"""
    e = sp.expand((S*r**weight).subs(r, q**2)*2*q)                 # ds = 2 q dq
    P = sp.Poly(sp.expand(e*q**80), q)
    res = 0
    for (k,), co in P.terms():
        p = k - 80
        if p >= -1:
            raise ValueError('no decay')
        res += co*q**(p + 1)/(p + 1)
    return sp.expand(res.subs(q, sp.sqrt(r))*r**(-weight))


def Qs(b):
    return sp.expand(-sp.Rational(1, 2)*r**-3*sp.diff(r**3*L.F*sp.diff(b, r), r))


def scalar_b(M, weight=sp.Rational(3, 2)):
    bs = [r**sp.Rational(-3, 2)]
    for _ in range(M):
        bs.append(Pinv_inf(Qs(bs[-1]), weight))
    return bs


def g2(control=False):
    M = 3
    bs = scalar_b(M, sp.Rational(1, 2) if control else sp.Rational(3, 2))
    Ps = [sp.Function('Psi%d' % k)(v) for k in range(M + 1)]
    fM = sum(Ps[k]*bs[k] for k in range(M + 1))
    box = sum(L.gi[a, b]*hessian(fM)[a, b] for a in range(n) for b in range(n))
    rep = {sp.Derivative(Ps[k], v): Ps[k - 1] for k in range(1, M + 1)}
    box = sp.expand(box.subs(rep))
    tele = sp.simplify(box + 2*Ps[M]*Qs(bs[M])) == 0
    if control:
        return tele
    b1_ok = sp.simplify(bs[1] + sp.Rational(3, 8)*(r**sp.Rational(-5, 2) + mu0*r**sp.Rational(-9, 2))) == 0
    vv = sp.expand(hessian(fM)[0, 0].subs(rep).subs(rep))
    rh = sp.sqrt(mu0)
    vvh = sp.expand(vv.subs(r, rh))
    psi = Ps[0]
    c2 = sp.simplify(vvh.coeff(sp.Derivative(psi, (v, 2))))
    c1 = sp.simplify(vvh.coeff(sp.Derivative(psi, v)))
    lead_ok = sp.simplify(c2 - mu0**sp.Rational(-3, 4)) == 0 and sp.simplify(c1 + sp.Rational(7, 4)*mu0**sp.Rational(
        -5, 4)) == 0
    hess_vv = sp.simplify(hessian(sp.Function('f')(v, r, th))[0, 0] - (
        sp.diff(sp.Function('f')(v, r, th), v, 2) - sp.diff(L.F, r)/2*sp.diff(sp.Function('f')(v, r, th), v)
        - L.F*sp.diff(L.F, r)/2*sp.diff(sp.Function('f')(v, r, th), r))) == 0
    out("  G2 box f_M = -2 Psi_M Q b_M (M = 3): %s; b_1 = -(3/8)(r^(-5/2) + mu0 r^(-9/2)): %s; b_2 = %s; Hessian vv ="
        " d_v^2 f - (F'/2) d_v f - (F F'/2) d_r f: %s; at the horizon (grad grad f_M)_vv = %s psi'' + %s psi' + ...:"
        " %s" % (tele, b1_ok, sp.factor(bs[2]), hess_vv, c2, c1, lead_ok))
    return tele and b1_ok and lead_ok and hess_vv


# ------------------------------------------------------------------------------------------------------------ G3
U = sp.Symbol('u')


def der_polys(a, K):
    """d^k/dx^k exp(-a/x) = P_k(1/x) exp(-a/x): P_(k+1)(u) = u^2 (a P_k(u) - P_k'(u))"""
    Ps = [sp.Integer(1)]
    for _ in range(K):
        Ps.append(sp.expand(U**2*(a*Ps[-1] - sp.diff(Ps[-1], U))))
    return [sp.lambdify(U, p, 'mpmath') for p in Ps]


PE = der_polys(1, 26)
PP = der_polys(sp.Rational(2, 3), 26)


def eps(polys, a, x):
    return sum(abs(p(1/x)) for p in polys)*mp.exp(-a/x)


def domination(lam, psi_a=mp.mpf(2)/3, N=9):
    polysP = PP if psi_a != 1 else PE
    env = lambda x: mp.exp(-1/x)                                                     # noqa: E731
    psi2 = lambda x: polysP[2](1/x)*mp.exp(-psi_a/x)                                # noqa: E731

    def terms(x):
        free = 2*lam**N*psi2(x)/2
        e26 = eps(PE, 1, x)
        e26s = eps(PE, 1, x + lam)
        p26s = eps(polysP, psi_a, x + lam)
        m0 = (env(x)**2 + x*env(x)**2)/9
        bound = lam**3*e26 + e26**2 + lam**(N - 5)*e26s + lam**(N - 5)*p26s*e26s + m0
        return free, bound
    xs = [3*lam*(mp.mpf('0.05')/(3*lam))**(mp.mpf(k)/600) for k in range(601)]
    dom = [terms(x)[0] >= 10*terms(x)[1] for x in xs]
    k1 = 0
    while k1 < len(xs) and dom[k1]:
        k1 += 1
    x1 = xs[k1 - 1] if k1 > 0 else None
    xw = 1/(14*mp.log(1/lam))
    fw, _ = terms(xw)
    window_ok = fw <= lam**3*env(xw)/10
    xb = mp.sqrt(lam)
    anywhere = any(d for x, d in zip(xs, dom) if x <= xb)
    return x1, k1, window_ok, anywhere, (mp.log(env(x1))/mp.log(lam) if x1 else None), xb, xw


def g3(control=False):
    if control:
        return any(domination(mp.mpf(10)**-e, psi_a=1)[3] for e in (100, 1000))
    rows, ok = [], True
    for e in (100, 1000):
        lam = mp.mpf(10)**-e
        x1, k1, window_ok, _, lev, xb, xw = domination(lam)
        good = x1 is not None and k1 > 300 and window_ok and x1 > xb and x1 < xw
        ok &= good
        rows.append("lam = 1e-%d: dominated on [3 lam, x_1] with x_1 = %s (env(x_1) = lam^%s; x_b = %s, window x_w ="
                    " %s), free term at the window below a tenth of lam^3 env: %s" % (
                        e, mp.nstr(x1, 5), mp.nstr(lev, 5), mp.nstr(xb, 3), mp.nstr(xw, 5), window_ok))
    out("  G3 " + "; ".join(rows))
    return ok


# ------------------------------------------------------------------------------------------------------------ G4
PINS_PROOF = {
    "Lemma 6.2 statement": "For every N there are stage data for Theorem A satisfying (F1)",
    "Lemma 6.2 proof range": "Stage m = 1, ..., N - 1, everything of the earlier stages given",
    "6.4": "Take the stage data of Lemma 6.2 with N := K + 3",
    "6.4 seed data": "equal to the seed's data on Sigma cap {r <",
}
PINS_PAPER = {"Theorem A": "every smooth choice of stage data there are profiles with (E1)"}


def g4(control=False):
    proof = os.path.join(HERE, '..', 'N1STAR-PROOF.md')
    paper = os.path.join(HERE, '..', '..', '..', 'paper', 'RESPONSE-HL-5D.md')
    raw = open(proof, 'rb').read()
    lines = raw.decode('utf-8').split('\n')
    praw = open(paper, 'rb').read()
    plines = praw.decode('utf-8').split('\n')
    if control:
        return any("Stage m = 1, ..., N," in ln or "stage N's data" in ln.lower() for ln in lines)
    found = {k: [i + 1 for i, ln in enumerate(lines) if p in ln] for k, p in PINS_PROOF.items()}
    pfound = {k: [i + 1 for i, ln in enumerate(plines) if p in ln] for k, p in PINS_PAPER.items()}
    ok = all(len(h) == 1 for h in found.values()) and all(len(h) == 1 for h in pfound.values())
    out("  G4 N1STAR-PROOF.md md5 %s: %s; RESPONSE-HL-5D.md md5 %s: %s" % (
        hashlib.md5(raw).hexdigest(), "; ".join("%s %s" % (k, ",".join(map(str, h)) or "missing")
                                               for k, h in found.items()),
        hashlib.md5(praw).hexdigest(), "; ".join("%s %s" % (k, ",".join(map(str, h)) or "missing")
                                                for k, h in pfound.items())))
    return ok


def main():
    ok = True
    for name, f in (("G4", g4), ("G2", g2), ("G3", g3), ("G1", g1)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("stagefree5: %s  [%.0f s]" % ("all checks pass, every control fails" if ok else "FAILURES", time.time() - T0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
