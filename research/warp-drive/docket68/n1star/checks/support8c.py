#!/usr/bin/env python3
"""support8c.py -- computations behind two deduced steps of the paper's section 8 (sections 8.4 and 8.5).

  K1 (exact, sympy) section 8.5's 'Deduced: ... the uniqueness inside the horizon, with the continuation there ...,
     by a lemma on the radial systems' simple zero at r_h' (supplement N1STAR-PROOF.md 10.76 (a)-(c), Lemma 10.56).
     The Frobenius exponents at r = r_h of the radial systems f phi'' + Q phi' + R phi = 0 of the spectral families at
     sigma, on five-dimensional Tangherlini in a chart regular across the horizon (mu = 1, r_h = 1, f'(r_h) = 2): the
     scalar wave and P_0 = 2 delta G delta* on 1-forms (hthresh5.py's metric and operators), box^C = P_0 + h^-1 L at
     the record's point (hthresh5.py's c, v, e_C, h = 10^-6), and the first-order part of 2 L on symmetric 2-tensors
     (lhor5.py's P) at gam_C = gam_H = 0 and at the record's point (gam_C = 10^6, e_C = 1/102400, c_C = (1/200) dv -
     (3/800) dr, hthresh5.py's c in lhor5.py's chart, t = v - r; c_H = c_r dr, 10.15's). The phi'' coefficient is f Id
     (zero at r_h), and the exponents are 0 (N times) and the eigenvalues of Id - Q(r_h)/f'(r_h), computed to be i
     sigma + lam_j with lam_j real and free of sigma and of the angles (two points of S^3). A nonzero exponent is a
     positive integer for some sigma != 0, Im sigma >= 0, iff some lam_j > 1; where max lam_j <= 1 the solutions smooth
     at r_h are exactly the N-dimensional exponent-0 family, and every exponent is finite, so a solution flat at r_h is
     0 (Lemma 10.56 (a)). Control: box^C with the damping's sign reversed, which puts exponents at positive integers.
  K2 (exact, sympy) the kernel elements' class (supplement 10.77 (c), 10.53): rho^beta near infinity lies in rho^q
     L^2(r^(n-1) dr) iff beta > q + n/2, so Theorem 9.5(1)'s threshold q = -1/2 + S-bar gives the class A^(3/2 + S-bar
     - eps) at n = 4, his 1 + S-bar at n = 3; checked also by integration at beta = crit +- 1/10. Control: the density
     r^(n-2), which gives 1 + S-bar at n = 4.
  K3 (numerical, mpmath at 50 digits) section 8.5's 'the resonances at timelike infinity between 5/2 and 3 + eps_+,
     whose locations the bookkeeping of section 8.4 does not need' (supplement 10.59 (b), 10.47 (b)). eps_+ is row w1
     of proof5/PART-VI4-PARAMS.md: 0 < eps_+ < min(delta_sharp, eps_ind, 1/4, l_I - 3), and eps_ind <= 1.94137e-8
     (section 8.5; checks/eindcert5.py); the scan covers (5/2, 13/4], every admissible eps_+. As iota5.py I4 does below
     5/2: box^C's polynomials at the record's point (damping5.py U3, kappa = l (l + 2)) for scalar l = 0, ..., LMAX
     and l = 10^4, 10^5, vector l = 1, ..., LMAX; their roots in the window, and the images lam + 1 of the roots in (2,
     5/2) (the tower d/dt*, iota5.py's deduction). Reported: counts, whether any is non-real, the extremes, the last l
     with a root in the window, and the least real part above 3, which is held against 3 + eps_ind: no candidate has
     real part in (3, 3 + eps_+], the (G+) condition of row w1, and every candidate has real part >= alpha_min (no
     upper bound is checked: the window runs to 13/4 and candidates reach 3.2499). K3 computes candidates -- box^C's
     roots and their tower images; that the resonances lie among them is iota5.py's deduction, not computed here --
     and the scan covers l <= LMAX = 1200 and l = 10^4, 10^5, not every l.
     Control: the vector polynomial's constant term moved by 10^-9, which puts a root in (3, 3 + eps_ind].
  K4 (exact, sympy) section 8.4's 'its exceptional exponents are 2 and 3/2 + (1 - e_Ups) gam_Ups ... the exponent 2
     resting on a scaling argument' (supplement 10.38 (a), (c); iplus5.py P2's reading). The exponent 2 is the I+
     exponent forced in the 11-component by the coupling of two trace-free tangential components (slot 6, pi-slash_0)
     at the radiative order r^(-(n-1)/2). Computed: the second variation of Ric at eta in R^(1,n), on h =
     a(t - r) r^(-p) T and k = c(t - r) r^(-p) T (T = b (x) b/r^2 - (|b|^2/r^2) P/(n - 1), b a tangential rotation
     1-form, P the tangential projector; a, c polynomials), contracted with d_1 = (d_t - d_r)/2 twice -- the (dx^1)^2
     component -- along a ray at fixed t* = t - r: its order in r is r^-3 at n = 4, p = 3/2 (exact: the order of a
     rational function in s, r = s^-2). With rho_I = t*/r, rho_+ = 1/t* and iplus5.py's normalization rho_I^-1
     rho_+^-2, the source is rho_I^(3 - 1) times a function of rho_+, and the indicial equation of L_0 = -(rho_I d -
     (3/2 + A_0))(rho_I d - rho_+ d) on rho_I^z U e_11 (iplus5.py P1's 3/2, scri5.py's A_0, (7, 7) entry 2 gam_Ups)
     matches powers at z = 2, with coefficient -(z - 3/2 - 2 gam_Ups) = -12/25 != 0 at the point: the term (2, 0),
     not a logarithm. Four dimensions (n = 3, p = 1) gives r^-2 and z = 1, his. Control: the decay coefficient p moved
     to 2, which moves the root to z = 3.

Labels: computed (exact, sympy; K3 numerical, mpmath). Reach: K1 computes the exponents, not Lemma 10.56 or the
continuation, and 2 L's zero-order (curvature) term, which does not enter the exponents, is not built; K2 checks the
step from q to the class, not Theorem 9.5(1); K3 covers the l scanned and the box^C candidates and their tower, not
the resonances themselves (iota5.py I5's connection is not run above 5/2); K4 computes the Ricci part of the coupling
at one ray and one tangential tensor, not the gauge term's h-dependence or Proposition 11.16 in five dimensions.

Run: python3 checks/support8c.py   (about nine minutes)
"""
import os
import sys
import textwrap

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)

SIG = sp.Symbol("sigma")
X_ = sp.Symbol("x")
EIND = mp.mpf("1.94137056846e-8")                                      # section 8.5, checks/eindcert5.py
LMAX = 1200


def lam_part(M, n):
    """M = Id - Q(r_h)/f'(r_h): its sigma part, which should be i sigma Id, and the eigenvalues of the rest"""
    S = (M - M.subs(SIG, 0)).applyfunc(sp.simplify)
    Lam = M.subs(SIG, 0).applyfunc(sp.simplify)
    ev = sp.roots(sp.factor(Lam.charpoly(X_).as_expr()), X_)
    return S == sp.I * SIG * sp.eye(n), ev


def k1(control=False):
    import hthresh5 as HT
    import lhor5 as LH
    ops = HT.operators()
    r, th = HT.r, HT.th
    a2, b1 = ops["P0"]
    L1 = ops["L"][1]
    rec = {HT.k_: HT.K, HT.v_: HT.V, HT.e_: HT.E}
    angs = (sp.asin(sp.Rational(3, 5)), sp.asin(sp.Rational(5, 13)))
    res = {}

    def one_forms(name, b):
        out = []
        for ang in angs:
            Q = -(b + 2 * a2[(0, 1)] * (-sp.I * SIG))                   # P = -f d_r^2 + ...: times -1
            M = sp.eye(5) - Q.subs(rec).subs({r: 1, th: ang}) / 2
            out.append(lam_part(M, 5))
        res[name] = out
    sgn = -1 if control else 1
    one_forms("box^C" if not control else "box^C, damping reversed", b1[1] + sgn * L1[1] / HT.H)
    if control:
        lams = [lam for _, ev in res["box^C, damping reversed"] for lam in ev]
        return all(ok for ok, _ in res["box^C, damping reversed"]) and max(lams) <= 1
    one_forms("P_0 (1-forms)", b1[1])
    g, f = HT.metric(1)
    gi = g.inv().applyfunc(sp.simplify)
    sq = sp.sqrt(-g.det().simplify())
    Qs = 2 * gi[0, 1] * (-sp.I * SIG) + sp.diff(sq * gi[1, 1], r) / sq   # box phi = f phi'' + Q phi' + ...
    res["scalar wave"] = [lam_part(sp.Matrix([[1 - Qs.subs({r: 1, th: ang}) / 2]]), 1) for ang in angs]
    X, N, PAIRS = LH.X, LH.N, LH.PAIRS
    w = {p: sp.Function("w%d%d" % p)(*X) for p in PAIRS}
    h = [[w[(min(a, b), max(a, b))] for b in range(N)] for a in range(N)]
    Rh, Gh = LH.rough(h), LH.Gop(h)
    A, B = LH.EC(LH.delta(Gh)), LH.dstar(LH.EH(Gh))
    P = [sp.expand(-Rh[a][b] + 2 * A[a][b] + 2 * B[a][b]) for a, b in PAIRS]
    for label, sub in (("2 L, gam_C = gam_H = 0", {LH.gC: 0, LH.gH: 0}),
                       ("2 L, record's point", {LH.gC: 10**6, LH.eC: sp.Rational(1, 102400), LH.av: sp.Rational(1, 200),
                                                LH.ar: sp.Rational(-3, 800), LH.cv: 0})):
        out = []
        for ang in angs:
            pt = {LH.r: 1, LH.ch: ang, LH.th: sp.asin(sp.Rational(7, 25)), **sub}
            Q = sp.zeros(15, 15)
            for i in range(15):
                Pi = P[i]
                for j, q in enumerate(PAIRS):
                    fn = w[q]
                    co = Pi.coeff(sp.diff(fn, X[1])) + Pi.coeff(sp.diff(fn, X[0], X[1])) * (-sp.I * SIG)
                    Q[i, j] = -co.subs(pt)
            out.append(lam_part((sp.eye(15) - Q / 2).applyfunc(sp.simplify), 15))
        res[label] = out
    ok = True
    print("  K1: exponents at r_h: 0 (N times) and i sigma + lam_j; lam_j (multiplicity), the same at two angles:",
          flush=True)
    for name, out in res.items():
        same = out[0][1] == out[1][1]
        sig_ok = all(s for s, _ in out)
        lams = out[0][1]
        top = max(lams)
        pos = [(lam, m_) for lam in lams if lam > 1 for m_ in range(1, int(sp.ceiling(lam)))]
        print(textwrap.fill("%s: %s; sigma part i sigma Id: %s, angle-free: %s; max lam %s; positive-integer "
              "exponents at sigma != 0, Im sigma >= 0: %s" % (name, ", ".join("%s (%d)" % (k_, v_) for k_, v_ in
                                                 sorted(lams.items(), key=lambda kv: -kv[0])), sig_ok, same, top,
                                                 ", ".join("sigma = %s i" % (lam - m_) for lam, m_ in pos) or "none"),
                            118, initial_indent="      ", subsequent_indent="        "), flush=True)
        ok &= sig_ok and same and all(sp.im(k_) == 0 for k_ in lams)
        want_top = 2 if name.startswith("2 L, gam") else None
        ok &= (top == want_top) if want_top else (top <= 1)
    print("      so for P_0, box^C and 2 L at the record's point and the scalar wave the smooth solutions at r_h are\n"
          "      the exponent-0 family; at gam = 0, 2 L has exponent 1 at sigma = i (Lemma 10.56 does not need either)",
          flush=True)
    return ok


def k2(control=False):
    beta, q, Sb = sp.symbols("beta q Sbar", real=True)
    rr = sp.Symbol("r", positive=True)
    crit = {}
    for n in (3, 4):
        dens = n - 2 if control else n - 1
        e_ = 2 * q - 2 * beta + dens                                   # |r^-beta|^2 r^(2q) r^dens
        sol = sp.solve(sp.Eq(e_, -1), beta)[0]                         # integrable at oo iff e_ < -1 iff beta > sol
        crit[n] = sp.simplify(sol.subs(q, -sp.Rational(1, 2) + Sb))
        for d_, fin in ((sp.Rational(1, 10), True), (-sp.Rational(1, 10), False)):
            qv = sp.Rational(-1, 2)
            bv = sol.subs(q, qv) + d_
            I = sp.integrate(rr**(2 * qv - 2 * bv + dens), (rr, 1, sp.oo))
            if bool(I.is_finite) != fin:
                return False
    if control:
        return sp.simplify(crit[4] - (sp.Rational(3, 2) + Sb)) == 0
    ok = sp.simplify(crit[4] - (sp.Rational(3, 2) + Sb)) == 0 and sp.simplify(crit[3] - (1 + Sb)) == 0
    print("  K2: rho^beta in rho^q L^2(r^(n-1) dr) iff beta > q + n/2; at q = -1/2 + S-bar: n = 4 %s, n = 3 %s (his\n"
          "      Theorem 9.5(5)); integrals finite at crit + 1/10 and infinite at crit - 1/10" % (crit[4], crit[3]),
          flush=True)
    return ok


def k3(control=False):
    import damping5 as DP
    pk, p0, pv = DP.polys(4, sp.Rational(2, 3))
    if control:
        pv = pv + sp.Rational(1, 10**9)
    mp.mp.dps = 50
    E, V, H = mp.mpf(1) / 102400, mp.mpf(1) / 2, mp.mpf(10)**-6
    lo, hi, tiny = mp.mpf(5) / 2, 3 + mp.mpf(1) / 4, mp.mpf(10)**-30
    win, tower, last, cplx, cnt = [], [], {}, 0, {}
    for name, P, ls in (("s0", p0, [0]), ("sl", pk, list(range(1, LMAX + 1)) + [10**4, 10**5]),
                        ("vl", pv, list(range(1, LMAX + 1)) + [10**4, 10**5])):
        co = [sp.lambdify((DP.e, DP.v, DP.h, DP.K), c, "mpmath") for c in sp.Poly(P, DP.lam).all_coeffs()]
        for lv in ls:
            rts = mp.polyroots([c(E, V, H, lv * (lv + 2)) for c in co], maxsteps=500, extraprec=300)
            w = [z for z in rts if lo < mp.re(z) <= hi]
            tw = [z + 1 for z in rts if 2 + tiny < mp.re(z) < lo]
            if w:
                last[name] = lv
            cnt[name] = cnt.get(name, 0) + len(w)
            cplx += sum(1 for z in w + tw if abs(mp.im(z)) > tiny)
            win += [(name, lv, z) for z in w]
            tower += [(name + " tower", lv, z) for z in tw if mp.re(z) <= hi]
    allc = win + tower
    above = [(nm, lv, mp.re(z)) for nm, lv, z in allc if mp.re(z) > 3 + tiny]
    least = min(above, key=lambda x: x[2])
    at3 = [(nm, lv) for nm, lv, z in allc if abs(z - 3) <= tiny]
    alpha_min = mp.mpf(3) / 2 + mp.mpf(99) / 10000
    inside = all(mp.re(z) >= alpha_min for _, _, z in allc)
    ok = least[2] > 3 + EIND and inside and not any(lv >= 10**4 for _, lv, _ in win)
    if control:
        return ok
    print(textwrap.fill("K3: box^C's roots at the record's point with real part in (5/2, 13/4]: %d (s0 %d, scalar l "
          ">= 1 %d, last at l = %s; vector %d, last at l = %s), none at l = 10^4, 10^5; tower images of the roots in "
          "(2, 5/2): %d; non-real: %d; real parts %s to %s; exactly 3: %s; least above 3: %s + %s (%s, l = %d) > 3 + "
          "eps_ind = 3 + %s: no candidate in (3, 3 + eps_+]; all >= alpha_min = 1.5099: %s"
          % (len(win), cnt["s0"], cnt["sl"], last.get("sl"), cnt["vl"], last.get("vl"), len(tower), cplx,
             mp.nstr(min(mp.re(z) for _, _, z in allc), 12), mp.nstr(max(mp.re(z) for _, _, z in allc), 12),
             at3, 3, mp.nstr(least[2] - 3, 8), least[0], least[1], mp.nstr(EIND, 6), inside),
                        118, initial_indent="  ", subsequent_indent="      "), flush=True)
    return ok


def ric2_order(n, p):
    """the order in r of Ric''(h, k)(d_1, d_1) along a ray at fixed t* = t - r, h = a r^-p T, k = c r^-p T"""
    t = sp.Symbol("t", real=True)
    xs = sp.symbols("x1:%d" % (n + 1), real=True)
    X, N = [t, *xs], n + 1
    r = sp.sqrt(sum(x**2 for x in xs))
    eta = sp.diag(-1, *[1] * n)
    b = [-xs[2], xs[3], xs[0], -xs[1]] if n == 4 else [-xs[1], xs[0], 0]
    b2 = sum(q_**2 for q_ in b)
    Pj = [[(1 if i == j else 0) - xs[i] * xs[j] / r**2 for j in range(n)] for i in range(n)]
    T = [[b[i] * b[j] / r**2 - b2 / r**2 * Pj[i][j] / (n - 1) for j in range(n)] for i in range(n)]
    u = t - r

    def field(A):
        M = sp.zeros(N, N)
        for i in range(n):
            for j in range(n):
                M[i + 1, j + 1] = A * r**(-p) * T[i][j]
        return M
    h, k = field(1 + u + u**2), field(2 - u + u**3)

    def D1(Hm):
        dH = [[[sp.diff(Hm[x, y], X[z]) for z in range(N)] for y in range(N)] for x in range(N)]
        return [[[(dH[d][q_][c] + dH[d][c][q_] - dH[q_][c][d]) / 2 for c in range(N)] for q_ in range(N)]
                for d in range(N)]
    Dh, Dk = D1(h), D1(k)
    G1 = [[[eta[a, a] * Dh[a][q_][c] for c in range(N)] for q_ in range(N)] for a in range(N)]
    G2 = [[[eta[a, a] * Dk[a][q_][c] for c in range(N)] for q_ in range(N)] for a in range(N)]
    G12 = [[[-sum(eta[a, a] * h[a, f] * eta[f, f] * Dk[f][q_][c] + eta[a, a] * k[a, f] * eta[f, f] * Dh[f][q_][c]
                  for f in range(N)) for c in range(N)] for q_ in range(N)] for a in range(N)]
    V = [sp.Rational(1, 2)] + [-x / (2 * r) for x in xs]                 # d_1 = (d_t - d_r)/2
    s = sp.Symbol("s", positive=True)
    w0 = [sp.Rational(q_, 5) for q_ in (1, 2, 2, 4)] if n == 4 else [sp.Rational(q_, 3) for q_ in (1, 2, 2)]
    Rr = s**-2
    sub = {t: sp.Rational(1, 2) + Rr, **{xs[i]: Rr * w0[i] for i in range(n)}}
    tot = 0
    for q_ in range(N):
        for c in range(N):
            e_ = sum(sp.diff(G12[a][q_][c], X[a]) for a in range(N)) - sum(sp.diff(G12[a][a][c], X[q_])
                                                                          for a in range(N))
            e_ += sum(G1[a][a][d] * G2[d][q_][c] + G2[a][a][d] * G1[d][q_][c] - G1[a][q_][d] * G2[d][a][c]
                      - G2[a][q_][d] * G1[d][a][c] for a in range(N) for d in range(N))
            tot += (V[q_] * V[c]).subs(sub) * e_.subs(sub)
    num, den = sp.fraction(sp.together(sp.expand(tot)))
    on = min(m_[0] for m_ in sp.Poly(sp.expand(num), s).monoms())
    od = min(m_[0] for m_ in sp.Poly(sp.expand(den), s).monoms())
    return sp.Rational(on - od, 2)


def k4(control=False):
    import iplus5 as IP
    import scri5 as S5
    from sbar5 import gU
    z = sp.Symbol("z")
    p5 = 2 if control else sp.Rational(3, 2)
    o5 = ric2_order(4, p5)
    z5 = sp.solve(sp.Eq(z, o5 - 1), z)[0]                              # rho_I^z = rho_I^(order) * rho_I^-1
    if control:
        return z5 == 2
    o4 = ric2_order(3, 1)
    z4 = sp.solve(sp.Eq(z, o4 - 1), z)[0]
    rem = IP.leading(4)                                                # L_0's 3/2: the remainder lies in rho_I Diff_b
    lead_ok = sp.together(rem).subs(IP.q, 0) == 0
    A77 = S5.five528()[6, 6]
    coef = -(z5 - sp.Rational(3, 2) - A77)
    cpt = coef.subs(gU, sp.Rational(1, 100))
    ok = o5 == 3 and z5 == 2 and o4 == 2 and z4 == 1 and lead_ok and A77 == 2 * gU and cpt == sp.Rational(-12, 25)
    print(textwrap.fill("K4: Ric''(h, k)(d_1, d_1) along the ray at fixed t*: r^-%s at n = 4, p = 3/2; r^-%s at n = "
          "3, p = 1; L_0's I+ exponent 3/2 (iplus5.py P1: remainder in rho_I Diff_b: %s); indicial matching: z = %s at "
          "n = 4 (his z = %s at n = 3); A_0's (7, 7) entry %s, coefficient -(z - 3/2 - 2 gam_Ups) = %s, %s at the point"
          % (o5, o4, lead_ok, z5, z4, A77, coef, cpt), 118, initial_indent="  ", subsequent_indent="      "),
          flush=True)
    return ok


CHECKS = [("K1", k1), ("K2", k2), ("K3", k3), ("K4", k4)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
