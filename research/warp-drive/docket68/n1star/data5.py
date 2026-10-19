#!/usr/bin/env python3
"""data5.py -- N1*, the data: the facts the outward evolution of the constraints uses (N1STAR-PROOF.md section 6).

Commissioned at item 522 (N1STAR-LOG.md D14).  The slice is Sigma = {tau = tau0} of the coordinates of ks5.py, written
in (r, th, phi1, phi2), so that v = tau0 + r on it.  The approximant's slice data are those of g0 + lam [W], W the
record's wave W_TT (lead5.py), with or without its second harmonic chi dv dv on Sigma; a profile f(v, r, th, s),
s = v/lam, is differentiated along Sigma by d_r -> d_r + d_v + lam^-1 d_s and in tau by d_v + lam^-1 d_s. The
constraint map is (J, rho)(K, g) = (2(-div K + d tr K), R(g) - |K|^2 + (tr K)^2), as in Chrusciel and Delay (2003),
(2.1). The correction is parametrised as in Racz (2016): h = a dr dr (the lapse of the foliation by the spheres r =
const), Q = w Pi + q (dth dr + dr dth) (Pi the metric induced on the spheres, q tangential), the other components free
and set to zero. Labels: computed (exact, sympy).

  S0 The background slice data: (J, rho)(g0's data) vanish where mu' = 0 (the seed's data are vacuum) and are
     proportional to mu' in the shell.
  S1 The polarization map h -> h(ell, .) - (1/2) dv tr_g0 h, ell = g0^-1 dv, has rank 5 (onto the covectors), and
     dv dv lies in its kernel.
  S2 The linearisation of (J, rho) at the approximant's slice data, in the directions (a, w, q), has no coefficient of
     order 1/lam: every coefficient is bounded uniformly in lam.  (W_TT is traceless on the spheres: an oscillating
     trace fails, mutants trace_W and trace_slip.)
  S3 Its principal part at the background is parabolic-hyperbolic in r: in d rho no d_r^2 a and no d_r d_th a, the
     coefficients of d_r a and d_th^2 a of opposite signs (forward parabolic in increasing r), no derivative of w, q;
     in (dJ_r, dJ_th) the d_r part is invertible on (w, q) and the d_th part couples them with a positive product
     (hyperbolic in r); a enters dJ to first order only.
  S4 S2 holds also when the second harmonic chi dv dv is nonzero on Sigma: oscillations of the radial components
     (gamma_rr, K_rr, the shift) do not reach the coefficients (the d_r K_rr terms of div K and d tr K cancel).
  S5 The inverse of the slice metric used above is correct through order lam^2 (an instrument check).
  S6 At the approximant's data, with or without chi on Sigma, the order-0 coefficients of the principal terms (a_rr,
     a_rt, a_r, a_tt in rho; w_r, w_t, q_r, q_t in J) equal the background's: alpha and the symmetrized A0 keep their
     signs.  (Lower-order coefficients may oscillate at O(1): that of d_th a in J_th does.)
python3 data5.py [--selftest | --mutants]
"""
import os
import sys

import sympy as sp

MUT = set()
MUTANTS = {"trace_slip": "a1 in place of a2 in W_phi2phi2: W not traceless, 1/lam coefficients appear (S2)",
           "trace_W": "an oscillating trace in place of W_TT: 1/lam coefficients appear (S2)",
           "conformal_h": "h = a gamma in place of a dr dr: d_r^2 a appears, not parabolic (S3)",
           "Q_on_dr2": "w on dr dr in place of Pi: the d_r part loses w, not hyperbolic (S3)",
           "no_lapse": "K without the factor 1/(2N): the seed's data are not vacuum (S0)",
           "inverse_slip": "an extra factor lam in the inverse metric's series: gamma^-1 gamma != 1 at O(lam) (S5)"}

v, th, s, lam, eps, A = sp.symbols("v theta s lam epsilon A", real=True)
r = sp.Symbol("r", positive=True)
Y = [r, th]                      # the coordinates the fields depend on; phi1, phi2 are cyclic
mu = sp.Function("mu")(v)
Ef = sp.Function("E")(v)
Hf = sp.Function("H")(th)
af = sp.Function("a")(r, th)
wf = sp.Function("w")(r, th)
qf = sp.Function("q")(r, th)
C, S_ = sp.cos(th), sp.sin(th)


IL = sp.Symbol("il")            # 1/lam, kept as its own symbol so that it never hides in a denominator


def D(e, k):
    """derivative along Sigma: k = 0 is r (through v = tau0 + r and s = v/lam), k = 1 is th, k = 2, 3 cyclic"""
    if k == 0:
        return sp.diff(e, r) + sp.diff(e, v) + sp.diff(e, s)*IL
    if k == 1:
        return sp.diff(e, th)
    return sp.Integer(0)


def Dt(e):
    return sp.diff(e, v) + sp.diff(e, s)*IL


def orders(e):
    """{k: coefficient of lam^k}, lam^p il^q counted as order p - q; lam and il must occur only as plain factors"""
    out = {}
    e = sp.expand(e)
    for term in (e.args if isinstance(e, sp.Add) else [e]):
        pw = term.as_powers_dict()
        p_, q_ = sp.sympify(pw.get(lam, 0)), sp.sympify(pw.get(IL, 0))
        if not (p_.is_integer and q_.is_integer):
            raise ValueError("a non-integer power of lam: %s" % str(term)[:120])
        k = int(p_) - int(q_)
        rest = term/(lam**pw.get(lam, 0)*IL**pw.get(IL, 0))
        if rest.has(lam) or rest.has(IL):
            raise ValueError("lam hidden inside a factor: %s" % str(term)[:120])
        out[k] = out.get(k, 0) + rest
    return out


def trunc(e, top=1):
    return sum((c_*lam**k if k >= 0 else c_*IL**(-k)) for k, c_ in orders(e).items() if k <= top)


def coeff(e, k):
    return orders(e).get(k, sp.Integer(0))


def wave(with_w=True, with_chi=False):
    """the angular components (th, phi1, phi2) of W and its chi part (W_tautau = W_taur = W_rr = chi)"""
    if not with_w:
        return [0, 0, 0], 0
    y3 = r**sp.Rational(-3, 2)
    if "trace_W" in MUT:
        F = A*Ef*Hf*y3*sp.cos(s)
        return [r**2*F, r**2*C**2*F, r**2*S_**2*F], 0
    a1 = A*Ef*Hf*y3*(2*C**2*sp.cos(s) - S_**2*sp.sin(s))/3
    a2 = A*Ef*Hf*y3*(2*S_**2*sp.sin(s) - C**2*sp.cos(s))/3
    ch = A*Ef*Hf*y3*sp.cos(2*s) if with_chi else 0       # a second harmonic chi dv dv, nonzero on Sigma
    if "trace_slip" in MUT:
        return [-2*r**2*(a1 + a2), 2*r**2*C**2*a1, 2*r**2*S_**2*a1], ch
    return [-2*r**2*(a1 + a2), 2*r**2*C**2*a1, 2*r**2*S_**2*a2], ch


def slice_data(with_w=True, with_chi=False):
    """(gamma, K) on Sigma of g0 + lam W, as truncated series in lam; K = (1/2N)(d_tau gamma - L_beta gamma)"""
    Wa, ch = wave(with_w, with_chi)
    m = mu/r**2
    gtt = -1 + m + lam*ch
    btr = m + lam*ch
    gam = sp.diag(1 + m + lam*ch, r**2 + lam*Wa[0], r**2*C**2 + lam*Wa[1], r**2*S_**2 + lam*Wa[2])
    gi = sp.zeros(4)
    for i in range(4):
        g0_, d_ = gam[i, i].subs(lam, 0), gam[i, i] - gam[i, i].subs(lam, 0)    # d_ carries its own factor lam
        if "inverse_slip" in MUT:
            d_ = lam*d_
        gi[i, i] = trunc(1/g0_ - d_/g0_**2 + d_**2/g0_**3, 2)
    beta = [btr, 0, 0, 0]
    N2 = trunc(-gtt + gi[0, 0]*btr**2, 2)
    N20 = N2.subs(lam, 0)
    dl = trunc((N2 - N20)/(2*N20), 1)
    Ninv = (1 - dl + sp.Rational(3, 2)*dl**2)/sp.sqrt(N20)
    if "no_lapse" in MUT:
        Ninv = 1
    G = christoffel(gam, gi)
    K = sp.zeros(4)
    for i in range(4):
        for j in range(4):
            lie = D(beta[j], i) + D(beta[i], j) - 2*sum(G[k][i][j]*beta[k] for k in range(4))
            K[i, j] = trunc(sp.expand((Dt(gam[i, j]) - lie)*Ninv/2), 1)
    return gam, gi, K


def christoffel(g, gi):
    n = 4
    dg = [[[D(g[a, b], k) for k in range(n)] for b in range(n)] for a in range(n)]
    return [[[trunc(sum(gi[a, d]*(dg[d][b][c] + dg[d][c][b] - dg[b][c][d]) for d in range(n))/2, 1)
              for c in range(n)] for b in range(n)] for a in range(n)]


def constraints(gam, gi, K):
    """(J_r, J_th, rho) of (gamma, K), truncated at lam^1"""
    n = 4
    G = christoffel(gam, gi)
    R = 0
    for b in range(n):
        for c in range(n):
            if gi[b, c] == 0:
                continue
            e = 0
            for a in range(n):
                e += D(G[a][b][c], a) - D(G[a][b][a], c)
                for d in range(n):
                    e += G[a][a][d]*G[d][b][c] - G[a][c][d]*G[d][b][a]
            R += gi[b, c]*e
    trK = sum(gi[i, j]*K[i, j] for i in range(n) for j in range(n))
    K2 = sum(gi[i, k]*gi[j, l]*K[i, j]*K[k, l] for i in range(n) for j in range(n) for k in range(n) for l in range(n)
             if gi[i, k] != 0 and gi[j, l] != 0)
    rho = R - K2 + trK**2
    J = []
    for i in range(2):
        divK = 0
        for j in range(n):
            for k in range(n):
                if gi[j, k] == 0:
                    continue
                cov = D(K[i, j], k) - sum(G[l][k][i]*K[l, j] + G[l][k][j]*K[i, l] for l in range(n))
                divK += gi[j, k]*cov
        J.append(2*(-divK + D(trK, i)))
    return J, rho


def perturbed(with_w=True, with_chi=False):
    gam, gi, K = slice_data(with_w, with_chi)
    h = sp.zeros(4)
    if "conformal_h" in MUT:
        h = gam*af
    else:
        h[0, 0] = af
    Q = sp.zeros(4)
    if "Q_on_dr2" in MUT:
        Q[0, 0] = wf
    else:
        for i in (1, 2, 3):
            Q[i, i] = wf*gam[i, i]
    Q[0, 1] = Q[1, 0] = qf
    gp = gam + eps*h
    gpi = sp.zeros(4)
    for i in range(4):
        for j in range(4):
            gpi[i, j] = trunc(gi[i, j] - eps*sum(gi[i, k]*h[k, l]*gi[l, j] for k in range(4) for l in range(4)), 1)
    Kp = K + eps*Q
    J, rho = constraints(gp, gpi, Kp)
    lin = [sp.expand(sp.diff(x, eps).subs(eps, 0)) for x in J + [rho]]
    base = [sp.expand(x.subs(eps, 0)) for x in J + [rho]]
    return lin, base


def jet(e):
    """replace the derivatives of a, w, q by symbols; return (expression, symbols)"""
    sym = {}
    for f, nm in ((af, "a"), (wf, "w"), (qf, "q")):
        for i in range(3):
            for j in range(3 - i):
                key = f if i + j == 0 else sp.Derivative(f, *([r]*i + [th]*j))
                sym[key] = sp.Symbol("%s_%s%s" % (nm, "r"*i, "t"*j) if i + j else nm)
    ders = sorted([k for k in sym if isinstance(k, sp.Derivative)], key=lambda k: -len(k.variables))
    for k in ders:
        e = e.subs(k, sym[k])
    for f in (af, wf, qf):
        e = e.subs(f, sym[f])
    return e, sym


def canonical(e):
    """an exact rational normal form: the jets of mu, E, H become symbols, mu = P^2 - r^2, r = R^2, and cos, sin of s
    and th become rational functions of z and y; an expression vanishes identically iff its normal form is 0"""
    P, R, z, y = sp.symbols("P R z y", positive=True)
    jets = {}
    for f_, x_, nm in ((mu, v, "m"), (Ef, v, "e"), (Hf, th, "h")):
        for k in (3, 2, 1):
            jets[sp.Derivative(f_, (x_, k))] = sp.Symbol("%s%d" % (nm, k))
    x = e
    for d_ in sorted(jets, key=lambda d_: -d_.derivative_count):
        x = x.subs(d_, jets[d_])
    x = x.subs({Ef: sp.Symbol("e0"), Hf: sp.Symbol("h0")}).subs(mu, P**2 - r**2).subs(r, R**2)
    x = sp.expand_trig(x.rewrite(sp.sin).rewrite(sp.cos))
    x = x.subs({sp.cos(s): (z + 1/z)/2, sp.sin(s): (z - 1/z)/(2*sp.I),
                sp.cos(th): (y + 1/y)/2, sp.sin(th): (y - 1/y)/(2*sp.I)})
    return sp.cancel(sp.together(x))


def is_zero(e):
    """exact zero test: a 50-digit evaluation at two sample points rejects at once; zero is confirmed exactly by the
    rational normal form"""
    q_ = sp.Symbol("q_")
    fns = {mu.func: sp.Lambda(q_, 1 + q_**2/7), Ef.func: sp.Lambda(q_, 1 + q_/3), Hf.func: sp.Lambda(q_, 1 + q_**2/5)}
    for pt in ((sp.Rational(7, 3), sp.Rational(2, 5), sp.Rational(5, 7), sp.Rational(3, 11)),
               (sp.Rational(13, 4), sp.Rational(1, 3), sp.Rational(-4, 9), sp.Rational(9, 5))):
        x = e
        for f_, l_ in fns.items():
            x = x.subs(f_, l_)
        x = x.doit().subs({r: pt[0], th: pt[1], v: pt[2], s: pt[3], A: sp.Rational(3, 2), lam: sp.Rational(1, 7)})
        x = x.subs({z: sp.Rational(k + 2, k + 5) for k, z in enumerate(sorted(x.free_symbols, key=str))})
        if abs(sp.N(x, 50)) > 1e-30:
            return False
    return canonical(e) == 0


def compute():
    lin_w, _ = perturbed(True)
    lin_0, base_0 = perturbed(False)
    lin_c, _ = perturbed(True, True)
    gam, gi, _ = slice_data(True, True)
    inv = [orders(x) for x in (gi*gam - sp.eye(4))]
    return dict(lin_w=lin_w, lin_0=lin_0, base_0=base_0, lin_c=lin_c, inv=inv)


def checks(o):
    c = {}
    mp, mpp = sp.symbols("mup mupp")
    base = [sp.simplify(coeff(x, 0).subs(sp.Derivative(mu, (v, 2)), mpp).subs(sp.Derivative(mu, v), mp))
            for x in o["base_0"]]
    vac = all(sp.simplify(x.subs(mp, 0)) == 0 and sp.diff(x, mpp) == 0 for x in base)
    prop = sp.simplify(base[2]) != 0 and all(sp.simplify(sp.diff(x, mp, 2)) == 0 for x in base)
    c["S0 the background slice data: (J, rho) = 0 where mu' = 0, linear in mu' (no mu''), rho != 0 in the shell"] = (
        vac and prop)
    c["S1 the polarization map has rank 5 and dv dv in its kernel"] = s1()
    def no_inverse(lin):
        for x in lin:
            for k_, c_ in orders(jet(x)[0]).items():
                if k_ < 0 and not is_zero(c_):
                    return False
        return True
    c["S2 the linearised constraints at the approximant's data have no coefficient of order 1/lam"] = (
        no_inverse(o["lin_w"]))
    Jr, Jt, rho = [jet(coeff(x, 0))[0] for x in o["lin_0"]]
    sy = jet(sp.Integer(0))[1]
    g = {str(v_): v_ for v_ in sy.values()}
    cf = lambda e, nm: sp.simplify(sp.expand(e).coeff(g[nm]))
    par = (cf(rho, "a_rr") == 0 and cf(rho, "a_rt") == 0
           and all(cf(rho, nm) == 0 for nm in ("w_r", "w_t", "q_r", "q_t", "w_rr", "q_rr", "w_tt", "q_tt")))
    cr, ctt = cf(rho, "a_r"), cf(rho, "a_tt")
    ratio = sp.simplify(ctt/cr) if cr != 0 else sp.oo
    par = par and cr != 0 and sp.simplify(ratio.subs(mu, sp.Rational(1, 2)).subs(r, 3)) < 0
    c1, c2, c3, c4 = cf(Jr, "w_r"), cf(Jr, "q_t"), cf(Jt, "q_r"), cf(Jt, "w_t")
    hyp = (cf(Jr, "q_r") == 0 and cf(Jt, "w_r") == 0 and c1 != 0 and c3 != 0
           and all(cf(J_, nm) == 0 for J_ in (Jr, Jt) for nm in ("a_rr", "a_rt", "a_tt")))
    if hyp:
        sp2 = sp.simplify(c2*c4/(c1*c3))
        hyp = sp.simplify(sp2.subs(mu, sp.Rational(1, 2)).subs(r, 3)) > 0
    c["S3 parabolic-hyperbolic in r at the background (rho in a; (J_r, J_th) in (w, q))"] = par and hyp
    c["S4 S2 holds also with a second harmonic chi dv dv nonzero on Sigma (radial oscillations do not reach)"] = (
        no_inverse(o["lin_c"]))
    c["S5 the slice data's inverse metric: gamma^-1 gamma = 1 through order lam^2"] = all(
        is_zero(c_) for d_ in o["inv"] for k_, c_ in d_.items() if k_ <= 2)
    names = (("w_r", "w_t", "q_r", "q_t"), ("w_r", "w_t", "q_r", "q_t"), ("a_rr", "a_rt", "a_r", "a_tt"))

    def principal(lin):                               # (J_r, J_th) principal in (w, q); rho principal in a
        return [sp.expand(jet(coeff(x, 0))[0]).coeff(g[nm]) for x, nms in zip(lin, names) for nm in nms]
    p0 = principal(o["lin_0"])
    c["S6 at the approximant's data (chi = 0 or not) the order-0 principal coefficients equal the background's"] = all(
        is_zero(sp.expand(x - y)) for lin in (o["lin_w"], o["lin_c"]) for x, y in zip(principal(lin), p0))
    return {k: bool(v_) for k, v_ in c.items()}


def s1():
    """rank of h -> h(ell, .) - (1/2) dv tr h on symmetric 5x5 h, at the background in EF coordinates (v, r, angles)"""
    rr, tt, M = sp.symbols("rr tt M", positive=True)
    f = 1 - M/rr**2
    g = sp.diag(-f, 0, rr**2, rr**2*sp.cos(tt)**2, rr**2*sp.sin(tt)**2)
    g[0, 1] = g[1, 0] = 1
    gi = g.inv()
    dv = sp.Matrix([1, 0, 0, 0, 0])
    ell = gi*dv
    rows = []
    basis = []
    for i in range(5):
        for j in range(i, 5):
            h = sp.zeros(5)
            h[i, j] = h[j, i] = 1
            basis.append(h)
    for h in basis:
        tr = sum(gi[a, b]*h[a, b] for a in range(5) for b in range(5))
        rows.append([sp.simplify(sum(ell[a]*h[a, b] for a in range(5)) - dv[b]*tr/2) for b in range(5)])
    Mx = sp.Matrix(rows).T
    pt = {rr: sp.Rational(7, 3), tt: sp.pi/5, M: sp.Rational(1, 2)}
    rank = Mx.subs(pt).rank(simplify=True)
    hv = dv*dv.T
    trv = sum(gi[a, b]*hv[a, b] for a in range(5) for b in range(5))
    kern = all(sp.simplify(sum(ell[a]*hv[a, b] for a in range(5)) - dv[b]*trv/2) == 0 for b in range(5))
    return rank == 5 and kern


def selftest():
    c = checks(compute())
    for k, v_ in c.items():
        print("%-118s %s" % (k[:118], "PASS" if v_ else "FAIL"))
    print("%s: %d/%d" % (os.path.basename(__file__), sum(c.values()), len(c)))
    return all(c.values())


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear()
        MUT.add(m_)
        try:
            c = checks(compute())
            failed = [k[:30] for k, v_ in c.items() if not v_]
        except Exception as ex:                       # noqa: BLE001
            failed = ["raised %s" % type(ex).__name__]
        caught += bool(failed)
        print("mutant %-13s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--show" in sys.argv:
        o = compute()
        Jr, Jt, rho = [jet(coeff(x, 0))[0] for x in o["lin_0"]]
        g = {str(v_): v_ for v_ in jet(sp.Integer(0))[1].values()}
        for nm, e, ks in (("rho", rho, ("a_r", "a_tt", "a_t", "a", "w", "q")), ("J_r", Jr, ("w_r", "q_t", "a_r", "a")),
                          ("J_th", Jt, ("q_r", "w_t", "a_t", "a"))):
            for k in ks:
                print(nm, k, sp.factor(sp.simplify(sp.expand(e).coeff(g[k]))))
        sys.exit(0)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
