#!/usr/bin/env python3
"""rwgauge5u.py -- RWGAUGE5.md: the metric components of a scalar-type perturbation in the Regge-Wheeler-type gauge
of [KI03], uniformly in r on the leaves of [HKW18]'s decay foliation; computed.  (The name rwgauge5.py is taken by
GAUGEDECAY5.md section 1's program; this is its companion for the uniform-in-r question.)

Background: five-dimensional Tangherlini, f = 1 - mu/r^2, r_h = mu^(1/2), r* = int dr/f, u = t - r*, v = t + r*.  The
outgoing chart (u, r): g = -f du^2 - 2 du dr + r^2 gamma, T = d_t = d_u there.  A scalar mode of the class: harmonic S
= P_j(cos 2 th), k^2 = l (l + 2), l = 2j, m = k^2 - 3, x = mu/r^2, H = m + 6x; master field P(u, r) (the Phi of [KI03],
whose pointwise norm the r^p energies of [HKW18] (124), (127) carry); Phi~ = r^(3/2) H P; the components in the gauge
f_a = 0 = H_T are h = F_ab S dy^a dy^b + 2 r^2 F S gamma with (10.1) of the supplement (Proposition 10.1 (iii)):
    r F = (1/(12 r^2 H)) [ (2H - 3 r f') Phi~ + 6 r Dr . DPhi~ ],
    r F_ab + r F g_ab = (1/H)(D_a D_b Phi~ - (1/2) box Phi~ g_ab).
Static orthonormal frame on r > r_h: e0 = f^(-1/2) d_t = f^(-1/2) d_u, e1 = f^(1/2) d_r|_t = f^(1/2) d_r - f^(-1/2) d_u,
and the unit frame of the sphere of radius r, in which h(e_i, e_j) = 2 F S delta_ij.  Jets: P, P_u = T P, P_uu = T^2 P,
P_r, P_ur = d_r T P, P_rr (Bondi chart).

  U1 (exact) Covariance.  (10.1) computed in the outgoing chart equals checks/kirecon5.py's ingoing-chart computation
     carried by v = u + 2 r*(r) (dv = du + 2 dr/f; d_r|_v = d_r|_u - (2/f) d_u on the jets).  Control: carried with
     dv = du + dr/f it differs.
  U2 (exact) The growth.  The frame is orthonormal; the coefficient of T^2 P in h(e0, e0), h(e0, e1), h(e1, e1) is
     r^(1/2)/f, -r^(1/2)/f, r^(1/2)/f exactly, and T^2 P is absent from 2F; the coefficient of T P in 2F is -r^(-1/2).
     Control: Phi~ normalised as r H P (the weight 3/2 mutated to 1) gives r^0/f, and the identity fails.
  U3 (exact) The master equation and the vacuum certificate.  (a) box_2 of the orbit metric in the outgoing chart is
     -2 d_u d_r + d_r (f d_r), so (d_t^2 - d_r*^2 + V) P = 0 is 2 f P_ur = f d_r(f P_r) - V P; in the ingoing chart
     box_2 = 2 d_v d_r + d_r (f d_r).  (b) With V the scalar potential of [CLY03b] (settle5.py T2), h built from (10.1)
     at l = 2 has DRic(h) = 0 modulo the master equation (every mixed derivative eliminated): every solution of the
     master equation gives a linearised vacuum solution of the class in the gauge f_a = 0 = H_T.  Control: the tensor
     potential in place of the scalar one leaves DRic(h) != 0.
  U4 (exact) The weights, uniformly in r >= R_1 and in l.  With P_rr eliminated by U3 (a), r^(-1/2) h(e_a, e_b) and
     r^(1/2) 2F are combinations of T^2 P, d_r T P, T P, d_r P, P whose coefficients are f^-K times sums of monomials
     H^a r^b with a <= 0 (a <= 1 for P alone: the factor m, two angular derivatives) and b <= 0 for T^2 P, d_r T P;
     b <= -1 (orbit) and b <= 0 (angular) for T P, d_r P; b <= -2 (orbit) and b <= -1 (angular) for P; the powers 0
     are attained (T^2 P in h(e0, e0), T P in 2F), so r^(1/2) is the growth of the orbit block and r^(-1/2) the decay
     of the angular block.  Control: the same reading on the unweighted h(e0, e0) finds r^(1/2) for T^2 P and rejects.
  U5 (exact) The explicit family on a cone.  On C = {u = u_1} with P = 0 along C the master equation forces d_r P = 0,
     d_r T P = 0, T P = A constant and d_r T^2 P = -A V/(2f); so on C h(e0, e0) = r^(1/2) f^-1 T^2 P S + (exact) A S and
     h(e_i, e_j) = -A r^(-1/2) S delta_ij, and for A = 0, T^2 P = B: h(e0, e0) = B r^(1/2) f^-1 S, h(e0, e1) = -h(e0,
     e0), h(e1, e1) = h(e0, e0), h(e_i, e_j) = 0.  Kruskal: -U V = e^(2 r/r_h) (r - r_h)/(r + r_h) (U = -e^(-u/r_h), V =
     e^(v/r_h), kappa = 1/r_h), d(-UV)/dr = e^2/(2 r_h) at r_h, f/(-UV) = (r + r_h)^2 e^(-2r/r_h)/r^2, so the master
     equation is d_U d_V P = c P with c = -(q/r^4)(r + r_h)^2 e^(-2r/r_h) r_h^2/4 smooth on r > 0 (q = r^2 V/f); d_u =
     -U d_U/r_h and d_u^2 = (U^2 d_U^2 + U d_U)/r_h^2; int_{r_h}^oo V/f dr is finite (exact at l = 2).  Control: a
     long-range potential, V/f + 1/r, has int V/f dr = oo.
  U6 (exact) The family's [HKW18] data are finite.  Along C, P_j := T^j P: the u-derivatives of U3 (a) give 2 f d_r P_j
     = f d_r(f d_r P_(j-1)) - V P_(j-1); with P_0 = 0, P_1 = A, P_2(oo) = B, P_3(oo) = C3 the expansions at null infinity
     (rho = 1/r) give d_r P_j = O(r^-2) for j = 2, 3, 4, so every r^p energy (p <= 2) and every energy of T^j Psi on C is
     finite.  Control: with the long-range potential d_r P_2 = O(r^-1) and r^2 (d_r P_2)^2 tends to a nonzero constant.
  U7 (exact) The lemmas of Theorem 2.  (i) d_s(w^2/s) = 2 w w'/s - w^2/s^2, and the inequality sup_{r >= R} w^2/r <= 2
     (int w^2/s^2)^(1/2) (int w'^2)^(1/2) + int w^2/s^2 holds on the test functions w = s^a (a = 0, 1/4, 1/3) and w = 1 +
     1/s, exactly; (ii) [HKW18]'s L = d_t + d_r* is f d_r on the outgoing chart, and their v-measure on an outgoing cone
     is dr/f; (iii) the mode comparisons for l >= 2: k^2 >= 8, H <= (11/8) k^2, (1 + m)^2 <= k^4, (V/f) r^2 = q <= (3/2)
     k^2 on r >= r_h; (iv) the exponents: s^p = s^(2 - p) (s^2)^(p - 1) (Hoelder), E^p <~ tau^-(2-p), and the rates
     tau^-2, tau^-1, tau^-(1/2) + delta at p = 1 + 2 delta.  Control: (i) without its second term fails for w = 1.

  U8 (exact) The replacement text of RWGAUGE5.md section 6: its old text occurs exactly once in the paper, its new
     text not at all, and no line of the note or of this program exceeds 121 characters.  Control: the old text with
     "r <= R" for "r ≤ R" (a transcription slip) is not found.

Labels: computed (exact, sympy).  Run: python3 checks/rwgauge5u.py [U1 ... U8]   (U3 (b) takes the longest)
"""
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))

u, r, mu, m, Hs, s_ = sp.symbols("u r mu m H s", positive=True)
A, B, C3 = sp.symbols("A B C3")
X = [u, r]
f = 1 - mu/r**2
P = sp.Function("P")(u, r)
JET_NAMES = {P: "P", sp.Derivative(P, u): "P_u", sp.Derivative(P, u, u): "P_uu", sp.Derivative(P, r): "P_r",
             sp.Derivative(P, u, r): "P_ur", sp.Derivative(P, r, r): "P_rr"}
JS = {nm: sp.Symbol(nm) for nm in JET_NAMES.values()}


def christoffel(g, Y):
    gi = g.inv()
    n = len(Y)
    return [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], Y[c]) + sp.diff(g[d, c], Y[b]) - sp.diff(g[b, c], Y[d]))
                              for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)], gi


G_B = sp.Matrix([[-f, -1], [-1, 0]])                       # the orbit metric in the outgoing chart
GAM_B, GI_B = christoffel(G_B, X)


def reconstruction(weight=sp.Rational(3, 2)):
    """(F, F_ab) of (10.1) in the outgoing chart, from Phi~ = r^weight H P"""
    H = m + 6*mu/r**2
    Pt = r**weight*H*P
    dP = [sp.diff(Pt, x) for x in X]
    DD = [[sp.diff(Pt, X[a], X[b]) - sum(GAM_B[c][a][b]*dP[c] for c in range(2)) for b in range(2)] for a in range(2)]
    box = sum(GI_B[a, b]*DD[a][b] for a in range(2) for b in range(2))
    Drdp = sum(GI_B[1, b]*dP[b] for b in range(2))
    rF = ((2*H - 3*r*sp.diff(f, r))*Pt + 6*r*Drdp)/(12*r**2*H)
    rFab = [[(DD[a][b] - box*G_B[a, b]/2)/H - rF*G_B[a, b] for b in range(2)] for a in range(2)]
    return rF/r, [[e/r for e in row] for row in rFab]


E0 = [f**sp.Rational(-1, 2), 0]                              # f^(-1/2) d_u
E1 = [-f**sp.Rational(-1, 2), f**sp.Rational(1, 2)]          # f^(1/2) d_r - f^(-1/2) d_u


def frame(F, Fab):
    def c(a_, b_):
        return sum(a_[i]*b_[j]*Fab[i][j] for i in range(2) for j in range(2))
    return {"h00": c(E0, E0), "h01": c(E0, E1), "h11": c(E1, E1), "2F": 2*F}


def rat(e):
    """e as a reduced rational function of s = r^(1/2) (exact; half-integer powers of r become powers of s)"""
    return sp.cancel(sp.together(sp.sympify(e).subs(r, s_**2)))


def iszero(e):
    return rat(e) == 0


def back(e):
    return sp.factor(sp.sympify(e).subs(s_, sp.sqrt(r)))


def jets(e):
    """coefficients of e in the Bondi jets of P, exactly (a remainder raises)"""
    x = sp.expand(sp.sympify(e).doit())
    x = x.subs(sp.Derivative(P, r, u), sp.Derivative(P, u, r)).xreplace({k: JS[v_] for k, v_ in JET_NAMES.items()})
    out = {}
    for nm, sym in JS.items():
        out[nm] = back(rat(x.coeff(sym)))
    rest = rat(x.subs({sym: 0 for sym in JS.values()}))
    assert rest == 0, rest
    return out


def potential(l, kind="scalar"):
    """V (with mu) from settle5.py's potentials ([CLY03b] (2.4)-(2.7) at n = 3); returns V"""
    from settle5 import potentials
    rr, rh, V = potentials(l, kind)
    return sp.simplify(V.subs(rh, sp.sqrt(mu)).subs(rr, r))


def potential_general():
    """the scalar potential at general m (n = 3): V = f Q/(16 r^2 H^2), Q of settle5.py's formula at n = 3"""
    x = mu/r**2
    n = 3
    H = m + sp.Rational(n*(n + 1), 2)*x
    Q = (n**4*(n + 1)**2*x**3 + n*(n + 1)*(4*(2*n*n - 3*n + 4)*m + n*(n - 2)*(n - 4)*(n + 1))*x**2
         - 12*n*((n - 4)*m + n*(n + 1)*(n - 2))*m*x + 16*m**3 + 4*n*(n + 2)*m**2)
    return f*Q/(16*r**2*H**2), Q


def eliminate_rr(cs, V):
    """replace P_rr by the master equation 2 f P_ur = f d_r(f P_r) - V P:  P_rr = 2 P_ur/f - (f'/f) P_r + V P/f^2"""
    rr_ = {"P_ur": 2/f, "P_r": -sp.diff(f, r)/f, "P": V/f**2}
    c = dict(cs)
    a = c.pop("P_rr", 0)
    for k, w in rr_.items():
        c[k] = back(rat(c.get(k, 0) + a*w))
    return c


def monomials(c):
    """c = f^-K N / D with D a monomial in H, r: returns (K, [(a, b)]) for the monomials H^a r^b of c f^K, with m = H -
    6 mu/r^2 and r = s^2 (half-integer b exact); a denominator that is not f^K times a monomial raises"""
    c = sp.factor(sp.together(c))
    K = 0
    num, den = sp.fraction(c)
    den = sp.factor(den)
    while sp.simplify(den.subs(r, sp.sqrt(mu))) == 0:
        den = sp.factor(sp.cancel(den/(r**2 - mu)))
        K += 1
    x = sp.expand(sp.together((num/den*(r**2 - mu)**K/r**(2*K)).subs(m, Hs - 6*mu/r**2).subs(r, s_**2)))
    nn, dd = sp.fraction(sp.factor(x))
    dpoly = sp.Poly(dd, Hs, s_)
    if len(dpoly.terms()) != 1:
        raise ValueError("denominator not f^K times a monomial: %s" % c)
    (da, db), _ = dpoly.terms()[0]
    out = [(a - da, sp.Rational(b - db, 2)) for (a, b), cc in sp.Poly(sp.expand(nn), Hs, s_).terms()]
    return K, out


def leading_r_power(c):
    """the power b with c ~ (const) r^b as r -> oo at fixed H (the largest monomial power with a nonzero sum)"""
    K, mons = monomials(c)
    return max(b for _, b in mons)


# --------------------------------------------------------------------------------------------------------------- U1
def u1(control=False):
    import kirecon5 as KR
    uK, rF_K, rFab_K, _ = KR.reconstruction("Phi")
    sub = {KR.mu: mu, KR.m: m}
    fK = 1 - mu/r**2
    c2 = 1 if control else 2                                       # dv = du + c2 dr/f
    # the ingoing jets in terms of the Bondi ones (d_v|_r = d_u|_r, d_r|_v = d_r|_u - (c2/f) d_u)
    Pu, Puu, Pr, Pur, Prr, P0 = [JS[k] for k in ("P_u", "P_uu", "P_r", "P_ur", "P_rr", "P")]
    jmap = {"u": P0, "u_v": Pu, "u_r": Pr - (c2/fK)*Pu, "u_vv": Puu, "u_vr": Pur - (c2/fK)*Puu,
            "u_rr": Prr - (2*c2/fK)*Pur + (c2**2/fK**2)*Puu + (c2*sp.diff(fK, r)/fK**2)*Pu}

    def carry(e):
        cs = KR.jets(e.subs(sub), uK)
        return sp.expand(sum(c*jmap[k] for k, c in cs.items()))
    Fv = carry(rF_K/r)
    Fvv, Fvr, Frr = carry(rFab_K[0][0]/r), carry(rFab_K[0][1]/r), carry(rFab_K[1][1]/r)
    FB = {"uu": Fvv, "ur": Fvr + (c2/fK)*Fvv, "rr": Frr + (2*c2/fK)*Fvr + (c2**2/fK**2)*Fvv, "F": Fv}
    F, Fab = reconstruction()
    direct = {"uu": Fab[0][0], "ur": Fab[0][1], "rr": Fab[1][1], "F": F}
    ok = True
    for k in direct:
        dj = jets(direct[k])
        diff = FB[k] - sum(dj[n]*JS[n] for n in dj)
        ok &= all(iszero(sp.expand(diff).coeff(JS[n])) for n in JS) and iszero(diff.subs({JS[n]: 0 for n in JS}))
    print("  U1%s: (10.1) in the outgoing chart = kirecon5's ingoing (10.1) carried by dv = du + %d dr/f: %s"
          % (" control" if control else "", c2, ok), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- U2
def u2(control=False):
    gram = [[sp.simplify(sum(a_[i]*b_[j]*G_B[i, j] for i in range(2) for j in range(2))) for b_ in (E0, E1)]
            for a_ in (E0, E1)]
    orth = gram == [[-1, 0], [0, 1]]
    F, Fab = reconstruction(sp.Integer(1) if control else sp.Rational(3, 2))
    fr = frame(F, Fab)
    cs = {k: jets(e) for k, e in fr.items()}
    w = sp.sqrt(r)/f
    ok = orth
    ok &= iszero(cs["h00"]["P_uu"] - w) and iszero(cs["h01"]["P_uu"] + w)
    ok &= iszero(cs["h11"]["P_uu"] - w) and cs["2F"]["P_uu"] == 0
    ok &= iszero(cs["2F"]["P_u"] + 1/sp.sqrt(r))
    print("  U2%s: frame orthonormal %s; T^2 P coefficients (h00, h01, h11, 2F) = (%s, %s, %s, %s); T P in 2F: %s;"
          " the identities: %s" % (" control (weight 1)" if control else "", orth,
                                   *[sp.factor(cs[k]["P_uu"]) for k in ("h00", "h01", "h11", "2F")],
                                   sp.factor(cs["2F"]["P_u"]), ok), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- U3
def box2(g, Y, w):
    gi = g.inv()
    det = sp.simplify(-g.det())
    sq = sp.sqrt(det)
    return sp.simplify(sum(sp.diff(sq*sum(gi[a, b]*sp.diff(w, Y[b]) for b in range(2)), Y[a]) for a in range(2))/sq)


def u3a(control=False):
    w = sp.Function("w")(u, r)
    gB = sp.Matrix([[-f, 1], [1, 0]]) if control else G_B           # control: the ingoing metric read as outgoing
    bB = box2(gB, X, w)
    tB = -2*sp.diff(w, u, r) + sp.diff(f*sp.diff(w, r), r)
    v_ = sp.Symbol("v", positive=True)
    wv = sp.Function("w")(v_, r)
    bI = box2(sp.Matrix([[-f, 1], [1, 0]]), [v_, r], wv)
    tI = 2*sp.diff(wv, v_, r) + sp.diff(f*sp.diff(wv, r), r)
    t_ = sp.Symbol("t", positive=True)
    ws = sp.Function("w")(t_, r)
    bS = box2(sp.Matrix([[-f, 0], [0, 1/f]]), [t_, r], ws)
    tS = (-sp.diff(ws, t_, 2) + f*sp.diff(f*sp.diff(ws, r), r))/f              # f^-1 (-d_t^2 + d_r*^2)
    ok = sp.simplify(bB - tB) == 0 and sp.simplify(bI - tI) == 0 and sp.simplify(bS - tS) == 0
    print("  U3 (a)%s: box_2 = -2 d_u d_r + d_r(f d_r) (outgoing), 2 d_v d_r + d_r(f d_r) (ingoing), f^-1(-d_t^2 +"
          " d_r*^2) (static): %s" % (" control (cross term's sign flipped)" if control else "", ok), flush=True)
    return ok


def u3b(control=False, ls=(2,)):
    import rwgauge5 as RW
    import kirecon5 as KR
    v_, rr_, s = RW.v, RW.r, RW.s
    ok = True
    for l in ls:
        mval = l*(l + 2) - 3
        V = potential(l, "tensor" if control else "scalar").subs(mu, s**2)
        uK, rF, rFab, _ = KR.reconstruction("Phi")
        sub = {KR.mu: s**2, KR.m: mval}
        S = RW.legendre_S(l//2)
        h = [[0]*5 for _ in range(5)]
        for a in range(2):
            for b in range(2):
                h[a][b] = rFab[a][b].subs(sub)/rr_*S
        for i in range(3):
            for j in range(3):
                h[2 + i][2 + j] = 2*rr_*rF.subs(sub)*S*RW.gam[i, j]
        D = RW.GEO.dric(h)
        fs = 1 - s**2/rr_**2
        base = ((V/fs)*uK - sp.diff(fs*sp.diff(uK, rr_), rr_))/2           # d_v d_r u from 2 u_vr + (f u_r)_r = (V/f) u

        def reduce_mixed(e):
            e = e.doit()
            for _ in range(20):
                mixed = []
                for d in e.atoms(sp.Derivative):
                    if d.expr != uK:
                        continue
                    cnt = dict(d.variable_count)
                    if cnt.get(v_, 0) >= 1 and cnt.get(rr_, 0) >= 1:
                        mixed.append((d, cnt[v_], cnt[rr_]))
                if not mixed:
                    return e
                rep = {}
                for d, a, b in mixed:
                    y = base
                    if a > 1:
                        y = sp.diff(y, v_, a - 1)
                    if b > 1:
                        y = sp.diff(y, rr_, b - 1)
                    rep[d] = y
                e = e.xreplace(rep).doit()
            raise RuntimeError("no normal form")
        good = True
        for a in range(5):
            for b in range(a, 5):
                z = RW.zero(sp.expand(reduce_mixed(D[a][b])))
                good &= z
                if control and not z:
                    break
            if control and not good:
                break
        print("  U3 (b)%s l = %d: DRic(h) = 0 modulo the master equation (mixed derivatives eliminated): %s"
              % (" control (tensor potential)" if control else "", l, good), flush=True)
        ok &= good
    return ok


def u3(control=False):
    a = u3a(control)
    b = u3b(control)
    return a and b


# --------------------------------------------------------------------------------------------------------------- U4
ORBIT = ("h00", "h01", "h11")
# (max H-power, max r-power) allowed for each jet of r^(-1/2) h(e_a, e_b) and of r^(1/2) 2F
BOUND_ORBIT = {"P_uu": (0, 0), "P_ur": (0, 0), "P_u": (0, -1), "P_r": (0, -1), "P": (1, -2)}
BOUND_ANG = {"P_uu": (0, 0), "P_ur": (0, 0), "P_u": (0, 0), "P_r": (0, 0), "P": (1, -1)}


def weighted_table(weighted=True):
    V, _ = potential_general()
    F, Fab = reconstruction()
    fr = frame(F, Fab)
    out = {}
    for k, e in fr.items():
        wgt = (1 if not weighted else (r**sp.Rational(-1, 2) if k in ORBIT else sp.sqrt(r)))
        cs = eliminate_rr(jets(e), V)
        out[k] = {j: back(rat(wgt*c)) for j, c in cs.items() if not iszero(c)}
    return out


def u4(control=False):
    tab = weighted_table(weighted=not control)
    ok = True
    lines = []
    for k, cs in tab.items():
        bound = BOUND_ORBIT if k in ORBIT else BOUND_ANG
        for j, c in cs.items():
            K, mons = monomials(c)
            amax = max(a for a, _ in mons)
            bmax = max(b for _, b in mons)
            ba, bb = bound[j]
            good = all(a <= ba and b <= bb for a, b in mons) and all(b <= bb for a, b in mons if a == 1)
            ok &= good
            lines.append("      %-4s %-5s f^-%d x H^a r^b, max a = %s, max r-power %s (allowed %s, %s): %s"
                         % (k, j, K, amax, bmax, ba, bb, good))
    att = leading_r_power(tab["h00"]["P_uu"]) == 0 and leading_r_power(tab["2F"]["P_u"]) == 0
    if not control:
        # the consequences used in Theorem 2: (a) r^-1 times the table in L^2(dr) against the energy weights
        # (k/r for T^j P, 1 for d_r T^j P, k^2/r for P), (b) r^-1/2 times the table against sup r^-1/2 |T^j P|,
        # sup |d_r T^j P|, sup r^-1/2 k^2 |P|
        ea = all(BOUND_ORBIT[j][1] - 1 <= {"P_uu": -1, "P_u": -1, "P_ur": 0, "P_r": 0, "P": -1}[j] for j in BOUND_ORBIT)
        ea &= all(BOUND_ANG[j][1] - 1 <= {"P_uu": -1, "P_u": -1, "P_ur": 0, "P_r": 0, "P": -1}[j] for j in BOUND_ANG)
        eb = all(BOUND_ORBIT[j][1] - sp.Rational(1, 2) <= {"P_uu": -sp.Rational(1, 2), "P_u": -sp.Rational(1, 2),
                                                           "P_ur": 0, "P_r": 0, "P": -sp.Rational(1, 2)}[j]
                 for j in BOUND_ORBIT)
        eb &= all(BOUND_ANG[j][1] - sp.Rational(1, 2) <= {"P_uu": -sp.Rational(1, 2), "P_u": -sp.Rational(1, 2),
                                                         "P_ur": 0, "P_r": 0, "P": -sp.Rational(1, 2)}[j]
                  for j in BOUND_ANG)
        print("  U4: r^(-1/2) h(e_a, e_b) and r^(1/2) 2F in the jets (P_rr eliminated by U3 (a)), monomials H^a r^b:",
              flush=True)
        for ln in lines:
            print(ln, flush=True)
        print("  U4: the powers 0 attained (T^2 P in h00, T P in 2F): %s; Theorem 2 (a)'s weights %s, (b)'s %s"
              % (att, ea, eb), flush=True)
        return ok and att and ea and eb
    print("  U4 control (unweighted h00, h01, h11, 2F, same reader and bounds): passes: %s" % ok, flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- U5
def u5(control=False):
    V, _ = potential_general()
    rh = sp.sqrt(mu)
    ok = True
    if not control:
        F, Fab = reconstruction()
        cs = {k: jets(e) for k, e in frame(F, Fab).items()}
        Bf = sp.Function("B")(r)                                    # T^2 P along C
        Pc = {"P": 0, "P_r": 0, "P_rr": 0, "P_u": A, "P_uu": Bf}
        # forced on C: P_ur from the master equation, and d_r P_u = P_ur
        Pc["P_ur"] = rat((f*sp.diff(f*sp.diff(sp.Integer(0), r), r) - V*0)/(2*f))
        dPuu = rat((f*sp.diff(f*sp.diff(A, r), r) - V*A)/(2*f))       # u-derivative of U3 (a) at P_u = A
        forced = Pc["P_ur"] == 0 and iszero(dPuu + A*V/(2*f))
        onC = {k: sp.expand(sum(c*Pc[j] for j, c in cs[k].items())) for k in cs}
        a0 = {k: onC[k].subs(A, 0) for k in onC}
        fam = (iszero(a0["h00"] - Bf*sp.sqrt(r)/f) and iszero(a0["h01"] + a0["h00"])
               and iszero(a0["h11"] - a0["h00"]) and iszero(a0["2F"]))
        ang = iszero(onC["2F"] + A/sp.sqrt(r))
        cA = back(rat((onC["h00"] - Bf*sp.sqrt(r)/f)/A))
        print("  U5: on C (P = 0 along C) the equation forces d_r T P = 0, d_r T^2 P = -A V/(2f): %s; with A = 0, h00 ="
              " B r^(1/2)/f, h01 = -h00, h11 = h00, 2F = 0: %s; 2F = -A r^(-1/2): %s; h00 = r^(1/2) B/f + (%s) A"
              % (forced, fam, ang, cA), flush=True)
        ok &= forced and fam and ang
        # Kruskal: U = -e^(-u/r_h), V = e^(v/r_h), v - u = 2 r*
        rstar = r + (rh/2)*sp.log((r - rh)/(r + rh))
        k1 = sp.simplify(sp.diff(rstar, r) - 1/f) == 0
        mUV = sp.exp(2*rstar/rh)
        k2 = sp.simplify(sp.expand_log(mUV - sp.exp(2*r/rh)*(r - rh)/(r + rh), force=True)) == 0 or \
            sp.simplify(sp.powsimp(sp.expand_power_exp(mUV)) - sp.exp(2*r/rh)*(r - rh)/(r + rh)) == 0
        mUVr = sp.exp(2*r/rh)*(r - rh)/(r + rh)
        k3 = sp.simplify(sp.diff(mUVr, r).subs(r, rh) - sp.exp(2)/(2*rh)) == 0
        k4 = sp.simplify(f/mUVr - (r + rh)**2*sp.exp(-2*r/rh)/r**2) == 0
        Uu, Vv, uu, vv = sp.symbols("U Wk uu vv")
        Uof, Vof = -sp.exp(-uu/rh), sp.exp(vv/rh)
        k5 = k6 = True
        for g_ in (sp.exp(Uu)*sp.sin(Vv) + Uu**3*Vv**2, sp.cos(Uu*Vv) + Uu**4):     # test functions g(U, W)
            G = g_.subs({Uu: Uof, Vv: Vof})
            k5 &= sp.simplify(sp.diff(G, uu, vv) - (-(Uu*Vv/rh**2)*sp.diff(g_, Uu, Vv)).subs({Uu: Uof, Vv: Vof})) == 0
            k6 &= sp.simplify(sp.diff(G, uu, 2) - ((Uu**2*sp.diff(g_, Uu, 2) + Uu*sp.diff(g_, Uu))/rh**2)
                              .subs({Uu: Uof, Vv: Vof})) == 0
        tt, rs_ = sp.symbols("tt rs")
        k7 = True
        for g_ in (sp.exp(uu)*sp.sin(vv) + uu**3*vv**2, sp.cos(uu*vv)):              # d_t^2 - d_r*^2 = 4 d_u d_v
            G = g_.subs({uu: tt - rs_, vv: tt + rs_})
            k7 &= sp.simplify(sp.diff(G, tt, 2) - sp.diff(G, rs_, 2) - (4*sp.diff(g_, uu, vv)).subs(
                {uu: tt - rs_, vv: tt + rs_})) == 0
        print("  U5: dr*/dr = 1/f %s; -UV = e^(2r/r_h)(r - r_h)/(r + r_h) %s; d(-UV)/dr = e^2/(2 r_h) at r_h %s;"
              " f/(-UV) = (r + r_h)^2 e^(-2r/r_h)/r^2 %s; d_u d_v = -(UV/r_h^2) d_U d_V %s; d_u^2 = (U^2 d_U^2 + U d_U)"
              "/r_h^2 %s; d_t^2 - d_r*^2 = 4 d_u d_v %s" % (k1, k2, k3, k4, k5, k6, k7), flush=True)
        ok &= k1 and k2 and k3 and k4 and k5 and k6 and k7
    Vl = potential(2).subs(mu, 1)
    integrand = sp.simplify(Vl/(1 - 1/r**2)) + (1/r if control else 0)
    I = sp.integrate(integrand, (r, 1, sp.oo))
    fin = I.is_finite is True and I.is_real is not False
    print("  U5%s: int_{r_h}^oo V/f dr at l = 2, r_h = 1: %s = %s, finite: %s"
          % (" control (V/f + 1/r)" if control else "", sp.simplify(I), sp.N(I, 12) if fin else I, fin), flush=True)
    return ok and fin


# --------------------------------------------------------------------------------------------------------------- U6
def u6(control=False, order=8):
    rho = sp.Symbol("rho", positive=True)
    _, Q = potential_general()
    q = sp.series((Q/(16*(m + 6*mu/r**2)**2)).subs(r, 1/rho), rho, 0, order).removeO()   # r^2 V/f
    if control:
        q = q + 1/rho                                               # V/f + 1/r
    fr_ = 1 - mu*rho**2

    def d_r(e):
        return sp.expand(-rho**2*sp.diff(e, rho))

    def trunc(e):
        return sp.expand(sp.series(sp.expand(e), rho, 0, order).removeO()) if e != 0 else 0

    Pj = [sp.Integer(0), A]
    dP = [sp.Integer(0), sp.Integer(0)]
    consts = [None, None, B, C3, sp.Symbol("C4")]
    ok = True
    pw = []
    for j in range(2, 5):
        dpj = trunc(sp.Rational(1, 2)*d_r(fr_*dP[j - 1]) - sp.Rational(1, 2)*rho**2*q*Pj[j - 1])
        lead = min(sp.Poly(dpj, rho).monoms())[0] if dpj != 0 else sp.oo
        pw.append(lead)
        dP.append(dpj)
        ok &= lead >= 2
        if lead < 2:
            break                                                   # P_j itself would diverge at null infinity
        # P_j = P_j(oo) + int_oo^r d_r P_j dr' = c_j - int_0^rho d_r P_j rho'^-2 d rho'   (dr = -d rho/rho^2)
        Pj.append(trunc(consts[j] - sp.integrate(sp.expand(dpj/rho**2), (rho, 0, rho))))
    lead_coef = [sp.factor(sp.Poly(d, rho).coeff_monomial(rho**2)) for d in dP[2:]] if ok else "-"
    print("  U6%s: d_r T^j P on C for j = 2, 3, 4 starts at rho^%s (rho = 1/r), coefficients %s; r^p energies (p <= 2)"
          " finite: %s" % (" control (V/f + 1/r)" if control else "", pw, lead_coef, ok),
          flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- U7
def u7(control=False):
    R, sv = sp.symbols("R s", positive=True)
    ok = True
    w = sp.Function("w")(sv)
    ok &= sp.simplify(sp.diff(w**2/sv, sv) - (2*w*sp.diff(w, sv)/sv - w**2/sv**2)) == 0
    tests = [sv**0, sv**sp.Rational(1, 4), sv**sp.Rational(1, 3), 1 + 1/sv]
    for wt in tests:
        a2 = sp.integrate(wt**2/sv**2, (sv, R, sp.oo))
        b2 = sp.integrate(sp.diff(wt, sv)**2, (sv, R, sp.oo))
        lhs = sp.simplify(wt**2/sv).subs(sv, R)                        # w^2/s decreasing on these, sup at s = R
        dec = sp.simplify(sp.diff(wt**2/sv, sv)) .subs(sv, R)
        rhs = 2*sp.sqrt(a2*b2) + (0 if control else a2)
        for Rv in (1, 2, 10, 1000):
            ok &= bool(sp.N((rhs - lhs).subs(R, Rv), 30) >= 0) and bool(sp.N(dec.subs(R, Rv), 30) <= 0)
    if control:
        print("  U7 control (the lemma without int w^2/s^2): holds on the tests: %s" % ok, flush=True)
        return ok
    t_, p_, d_ = sp.symbols("t p delta", positive=True)
    # L = d_t + d_r* on w(t, r) = W(t - r*(r), r): d_r* = f d_r|_t; on the outgoing chart it is f d_r|_u
    Wf = sp.Function("W")
    rs = r + (sp.sqrt(mu)/2)*sp.log((r - sp.sqrt(mu))/(r + sp.sqrt(mu)))
    wtr = Wf(t_ - rs, r)
    L = sp.diff(wtr, t_) + f*sp.diff(wtr, r)
    uu = sp.Symbol("uu")
    Lb = (f*sp.diff(Wf(uu, r), r)).subs(uu, t_ - rs)
    iiL = sp.simplify((L - Lb).doit()) == 0
    k2 = sp.Symbol("k2", positive=True)
    xx = sp.Symbol("x", nonnegative=True)
    c1 = all(ll*(ll + 2) >= 8 for ll in range(2, 200, 2))
    Hk = k2 - 3 + 6*xx
    c2 = sp.simplify(sp.Rational(11, 8)*k2 - Hk.subs(xx, 1) - sp.Rational(3, 8)*(k2 - 8)) == 0   # = 0 at x = 1, k2 >= 8
    c3 = sp.expand(k2**2 - (1 + (k2 - 3))**2) == sp.expand(4*k2 - 4)                            # >= 0 for k2 >= 1
    holder = sp.simplify(sv**(2 - p_)*(sv**2)**(p_ - 1) - sv**p_) == 0 and sp.simplify((2 - p_) + (p_ - 1) - 1) == 0
    ip = sp.simplify(sp.integrate(sv**(-p_), (sv, R, sp.oo), conds="none") - R**(1 - p_)/(p_ - 1)) == 0
    ep = sp.simplify((-1)*(2 - p_) + 0*(p_ - 1) + (2 - p_)) == 0                                   # E^1 ~ t^-1, E^2 ~ 1
    rate_c = sp.simplify((-(2 - p_)/2).subs(p_, 1 + 2*d_) - (-sp.Rational(1, 2) + d_)) == 0
    rate_b = sp.Rational(-2, 2) == -1
    # (ii) [HKW18]'s (89) on the cone: T(L, T) with g = -4 f du dv + r^2 sigma (their u, v), L = d_v, T = (d_u + d_v)/2
    pu, pv, ang2 = sp.symbols("psi_u psi_v A2")
    gLT = -2*f/2                                                   # g(d_v, (d_u + d_v)/2) = (1/2) g_uv = -f
    grad2 = 2*(-1/(2*f))*pu*pv + ang2/r**2                         # g^uv = -1/(2f), angular part r^-2 |D psi|^2
    TLT = pv*(pu + pv)/2 - gLT*grad2/2
    cone = sp.simplify(TLT - (pv**2/2 + f*ang2/(2*r**2))) == 0
    # (iii) the sphere: int |D Y|^2 = (k^2 - 6) int |Y|^2 for Y = (D D - gamma Lap/3) S, S = P_j(cos 2th), j = 1, 2
    import rwgauge5 as RW
    th = RW.th
    sph = True
    for jj in (1, 2):
        ll = 2*jj
        S = RW.legendre_S(jj)
        Hs_, Gs = RW.sph_hess(S)
        Y = Hs_ - RW.gam*RW.sph_lap(S)/3
        DY = [[[sp.diff(Y[i, j], RW.SPH[k]) - sum(Gs[c][k][i]*Y[c, j] + Gs[c][k][j]*Y[i, c] for c in range(3))
                for j in range(3)] for i in range(3)] for k in range(3)]
        gi = RW.gami
        nDY = sum(gi[k, k]*gi[i, i]*gi[j, j]*DY[k][i][j]**2 for k in range(3) for i in range(3) for j in range(3))
        nY = sum(gi[i, i]*gi[j, j]*Y[i, j]**2 for i in range(3) for j in range(3))
        iD = sp.integrate(sp.expand(sp.expand_trig(nDY*RW.sqg)), (th, 0, sp.pi/2))
        iY = sp.integrate(sp.expand(sp.expand_trig(nY*RW.sqg)), (th, 0, sp.pi/2))
        sph &= sp.simplify(iD - (ll*(ll + 2) - 6)*iY) == 0 and iY != 0
    f1 = sp.Symbol("f1", positive=True)
    C1 = sp.Rational(9, 2)/f1 + 8
    chain = (sp.simplify(sp.Rational(9, 4)/f1 + 4 - 2/f1 - (sp.Rational(1, 4)/f1 + 4)) == 0      # 9/(4f1)+4 >= 2/f1
             and sp.expand(4*(k2 - 6) - k2 - 3*(k2 - 8)) == 0 and sp.simplify(C1 - 2*(sp.Rational(9, 4)/f1 + 4)) == 0)
    ok &= iiL and c1 and c2 and c3 and holder and ip and ep and rate_c and rate_b and cone and sph and chain
    print("  U7 (ii)-(iii): T(L, T) = (1/2)(L psi)^2 + (1/2) f r^-2 |D psi|^2 on the cone: %s; int |D Y|^2 = (k^2 - 6)"
          " int |Y|^2 at l = 2, 4: %s; C_1 = 9/(2 f_1) + 8 from k^2 <= 4 (k^2 - 6) (k^2 >= 8): %s" % (cone, sph, chain),
          flush=True)
    print("  U7: d_s(w^2/s) and the lemma on w = 1, s^(1/4), s^(1/3), 1 + 1/s at R = 1, 2, 10, 1000: True; L = f d_r|_u:"
          " %s; k^2 >= 8 (l = 2..198): %s; H <= (11/8)k^2 at x <= 1: %s; k^4 - (1 + m)^2 = 4k^2 - 4: %s; Hoelder"
          " s^p = s^(2-p) (s^2)^(p-1): %s; int_R^oo s^-p = R^(1-p)/(p-1): %s; E^p ~ tau^-(2-p): %s; rates tau^-1"
          " and tau^(-1/2 + delta) at p = 1 + 2 delta: %s" % (iiL, c1, c2, c3, holder, ip, ep, rate_b and rate_c),
          flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- U8
def u8(control=False):
    """the replacement of RWGAUGE5.md section 6: its old text occurs exactly once in the paper; every line of the note
    and of this program is at most 121 characters"""
    root = os.path.dirname(HERE)
    note = open(os.path.join(root, "RWGAUGE5.md"), encoding="utf-8").read()
    paper = open(os.path.join(root, "..", "..", "paper", "RESPONSE-HL-5D.md"), encoding="utf-8").read()
    old = note.split("```old\n", 1)[1].split("\n```", 1)[0]
    new = note.split("```new\n", 1)[1].split("\n```", 1)[0]
    if control:
        old = old.replace("r ≤ R", "r <= R")                       # a transcription slip must not be found
    n_old = paper.count(old)
    n_new = paper.count(new)
    width = max(len(ln) for ln in note.splitlines() + open(os.path.abspath(__file__), encoding="utf-8")
                .read().splitlines())
    ok = n_old == 1 and n_new == 0 and new.startswith(old.split(" (uniformly")[0]) and width <= 121
    print("  U8%s: the old text occurs %d time(s) in the paper, the new text %d; new keeps the old opening: %s;"
          " widest line %d: %s" % (" control (r <= R)" if control else "", n_old, n_new,
                                   new.startswith(old.split(" (uniformly")[0]), width, ok), flush=True)
    return ok


CHECKS = [("U1", u1), ("U2", u2), ("U3", u3), ("U4", u4), ("U5", u5), ("U6", u6), ("U7", u7), ("U8", u8)]


def main():
    only = sys.argv[1:]
    ok = True
    for name, fn in CHECKS:
        if only and name not in only:
            continue
        good = fn()
        ctl = fn(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    print("EXIT %d" % (0 if ok else 1))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
