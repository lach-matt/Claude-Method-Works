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
  U3 (exact) The master equation and the vacuum certificate.  (a) box_2 of the orbit metric in the outgoing chart is -2
     d_u d_r + d_r (f d_r), so (d_t^2 - d_r*^2 + V) P = 0 is 2 f P_ur = f d_r(f P_r) - V P; in the ingoing chart box_2 =
     2 d_v d_r + d_r (f d_r); U4's elimination of P_rr satisfies (2.1) identically, and potential_general is settle5.py's
     potential at l = 2, 4, 6, 8.  (b) With V the scalar potential of [CLY03b] (settle5.py T2), h built from (10.1) at l
     = 2, 4 and 6 has DRic(h) = 0 modulo the master equation (every mixed derivative eliminated): every solution of the
     master equation gives a linearised vacuum solution of the class in the gauge f_a = 0 = H_T.  Control: the tensor
     potential in place of the scalar one leaves DRic(h) != 0.
  U4 (exact) The weights, uniformly in r >= R_1 and in l.  With P_rr eliminated by U3 (a), r^(-1/2) h(e_a, e_b) and
     r^(1/2) 2F are combinations of T^2 P, d_r T P, T P, d_r P, P whose coefficients are f^-K times sums of monomials H^a
     r^b with a <= 0 (a <= 1 for P alone: the factor m, two angular derivatives) and b <= 0 for T^2 P, d_r T P; b <= -1
     (orbit) and b <= 0 (angular) for T P, d_r P; b <= -2 (orbit) and b <= -1 (angular) for P; the powers 0 are attained
     (T^2 P in h(e0, e0), T P in 2F), so r^(1/2) is the growth of the orbit block and r^(-1/2) the decay of the angular
     block; Theorem 2's weights for (a), (b), (c) are checked on the measured powers of every entry. Control: the same
     reading on the unweighted h(e0, e0) finds r^(1/2) for T^2 P and rejects.
  U5 (exact) The explicit family on a cone.  On C = {u = u_1} with P = 0 along C the master equation, order by order in u
     - u_1, forces d_r P = 0, d_r T P = 0, T P = A constant and d_r T^2 P = -A V/(2f); so on C h(e0, e0) = r^(1/2) f^-1
     T^2 P S + (exact) A S and h(e_i, e_j) = -A r^(-1/2) S delta_ij, and for A = 0, T^2 P = B: h(e0, e0) = B r^(1/2) f^-1
     S, h(e0, e1) = -h(e0, e0), h(e1, e1) = h(e0, e0), h(e_i, e_j) = 0.  Kruskal: -U V = e^(2 r/r_h) (r - r_h)/(r + r_h)
     (U = -e^(-u/r_h), V = e^(v/r_h), kappa = 1/r_h), d(-UV)/dr = e^2/(2 r_h) at r_h, f/(-UV) = (r + r_h)^2
     e^(-2r/r_h)/r^2, so the master equation is d_U d_V P = c P with c = -(q/r^4)(r + r_h)^2 e^(-2r/r_h) r_h^2/4 smooth
     on r > 0 (q = r^2 V/f); d_u = -U d_U/r_h and d_u^2 = (U^2 d_U^2 + U d_U)/r_h^2; d(-UV)/dr > 0 on r > 0; c_A asserted
     exactly; int_{r_h}^oo V/f dr = 11/2 at l = 2, r_h = 1.  Control: a long-range potential, V/f + 1/r, has int V/f dr =
     oo.
  U6 (exact) The family's [HKW18] data are finite.  Along C, P_j := T^j P: the u-derivatives of U3 (a) give 2 f d_r P_j =
     f d_r(f d_r P_(j-1)) - V P_(j-1); with P_0 = 0, P_1 = A, P_2(oo) = B, P_3(oo) = C3 the expansions at null infinity
     (rho = 1/r) give d_r P_j = -(m + 15/4) P_(j-1)(oo) r^-2/2 + O(r^-3) for j = 2, 3, 4 (re-checked by
     r-differentiation), so every r^p energy (p <= 2) and every energy of T^j Psi on C is finite.  Control: with the
     long-range potential d_r P_2 = O(r^-1) and r^2 (d_r P_2)^2 tends to a nonzero constant.
  U7 (exact) The lemmas of Theorem 2.  (i) d_s(w^2/s) = 2 w w'/s - w^2/s^2, and the inequality sup_{r >= R} w^2/r <= 2
     (int w^2/s^2)^(1/2) (int w'^2)^(1/2) + int w^2/s^2 holds on the test functions w = 1, s^(1/4), s^(1/3), 1 + 1/s,
     exactly; (ii) [HKW18]'s L = d_t + d_r* is f d_r on the outgoing chart (their v is r* + const on an outgoing cone,
     dv = dr/f by U5), and their (89) gives T(L, T) = (1/2)(L psi)^2 + (1/2) f r^-2 |D psi|^2 there; (iii) on S^3,
     int |D Y|^2 = (k^2 - 6) int |Y|^2 for Y = (D D - gamma Lap/3) P_j(cos 2 th), j = 1, 2, and the constant C_1 = 9/(2
     f_1) + 8; the mode comparisons for l >= 2: k^2 >= 8, H <= (11/8) k^2, k^4 - (1 + m)^2 = 4 k^2 - 4; (iv) the
     exponents: s^p = s^(2 - p) (s^2)^(p - 1), int_R^oo s^-p = R^(1-p)/(p-1), the interpolation E^p <= (E^1)^(2-p)
     (E^2)^(p-1) on three test functions at p = 6/5, 3/2, 9/5, and -(2 - p)/2 = delta - 1/2 at p = 1 + 2 delta.
     Controls: (i) without its second term fails for w = 1; the interpolation without the E^2 factor fails.
  U8 (exact) The replacement text of RWGAUGE5.md section 6: its old text occurs exactly once in the paper, its new
     text not at all, and no line of the note or of this program exceeds 121 characters.  Control: the old text with
     "r <= R" for "r ≤ R" (a transcription slip) is not found.
  U9 (exact) The angular Sobolev inequality of RWGAUGE5.md R2.0.1 (Lemma A): the dimensions (l + 1)^2 of the degree-l
     harmonics on S^3, vol = 2 pi^2, 1 + l(l + 2) = (l + 1)^2, sum (l + 1)^-2 = pi^2/6 and the constant 1/12; the
     reproducing kernel ((l + 1)/(2 pi^2)) U_l(cos psi); sum of the six rotations squared = Lap; ||Lap w||^2 = sum
     ||Om_i Om_j w||^2; generators of operator norm 1, L_Om P = 0, and the constants of the tensor version.  Controls:
     the Casimir over ordered pairs fails; the series with (1 - Lap)^(3/4) diverges.
  U10 (exact) R2.0.5: [HKW18] (163), (168), (169) applied to the perturbation (10.1) builds from P give Phi = P exactly,
     at general l (every other jet cancels after the master equation).  Control: V times 1 + mu/r^2 leaves a
     non-constant coefficient.

Labels: computed (exact, sympy).  Run: python3 checks/rwgauge5u.py [U1 ... U10]   (U3 (b) takes the longest)
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


def say(msg, **_):
    """print, wrapped at 121 characters with a hanging indent (the .out obeys the line width too)"""
    import textwrap
    ind = len(msg) - len(msg.lstrip())
    for ln in textwrap.wrap(msg, width=121, subsequent_indent=" "*(ind + 4), break_on_hyphens=False) or [""]:
        print(ln, flush=True)


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
    x = sp.expand(sp.together((num/den/r**(2*K)).subs(m, Hs - 6*mu/r**2).subs(r, s_**2)))   # c f^K
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
    say("  U1%s: (10.1) in the outgoing chart = kirecon5's ingoing (10.1) carried by dv = du + %d dr/f: %s"
          % (" control" if control else "", c2, ok))
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
    say("  U2%s: frame orthonormal %s; T^2 P coefficients (h00, h01, h11, 2F) = (%s, %s, %s, %s); T P in 2F: %s;"
          " the identities: %s" % (" control (weight 1)" if control else "", orth,
                                   *[sp.factor(cs[k]["P_uu"]) for k in ("h00", "h01", "h11", "2F")],
                                   sp.factor(cs["2F"]["P_u"]), ok))
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
    say("  U3 (a)%s: box_2 = -2 d_u d_r + d_r(f d_r) (outgoing), 2 d_v d_r + d_r(f d_r) (ingoing), f^-1(-d_t^2 +"
          " d_r*^2) (static): %s" % (" control (cross term's sign flipped)" if control else "", ok))
    if control:
        return ok
    # the elimination of P_rr used by U4 satisfies (2.1) identically, with potential_general's V
    V, _ = potential_general()
    el = eliminate_rr({"P_rr": sp.Integer(1)}, V)
    Prr = sum(c*JS[j] for j, c in el.items())
    E21 = 2*f*JS["P_ur"] - f*(sp.diff(f, r)*JS["P_r"] + f*Prr) + V*JS["P"]
    elim = all(iszero(sp.expand(E21).coeff(JS[j])) for j in JS) and iszero(E21.subs({JS[j]: 0 for j in JS}))
    # potential_general is settle5.py's potential ([CLY03b]) at l = 2, 4, 6, 8
    pg = all(iszero(V.subs(m, ll*(ll + 2) - 3) - potential(ll)) for ll in (2, 4, 6, 8))
    say("  U3 (a): P_rr = 2 P_ur/f - (f'/f) P_r + V P/f^2 satisfies (2.1) identically: %s; potential_general equals"
        " settle5.py's scalar potential at l = 2, 4, 6, 8: %s" % (elim, pg))
    return ok and elim and pg


def u3b(control=False, ls=(2, 4, 6)):
    """DRic of h_ab = F_ab S, h_ij = 2 r^2 F S gamma with abstract F's (rwgauge5.py's tensor calculus, ingoing chart),
    then F, F_ab replaced by (10.1) (kirecon5.py) as linear combinations of the jets J(a, b) = d_v^a d_r^b of the
    master field, every mixed jet reduced by the master equation 2 u_vr = (V/f) u - (f u_r)_r; every coefficient of
    the reduced combination must vanish (trigonometric functions through w = tan(th/2), r = sigma^2: exact)"""
    import rwgauge5 as RW
    import kirecon5 as KR
    v_, rr_, th, s = RW.v, RW.r, RW.th, RW.s
    fs = 1 - s**2/rr_**2
    ok = True
    for l in ls:
        mval = l*(l + 2) - 3
        V = potential(l, "tensor" if control else "scalar").subs(mu, s**2).subs(r, rr_)
        S = RW.legendre_S(l//2)
        names = ("Fvv", "Fvr", "Frr", "FF")
        Fs = {n: sp.Function(n)(v_, rr_) for n in names}
        h = [[0]*5 for _ in range(5)]
        h[0][0], h[0][1], h[1][1] = Fs["Fvv"]*S, Fs["Fvr"]*S, Fs["Frr"]*S
        h[1][0] = h[0][1]
        for i in range(3):
            h[2 + i][2 + i] = 2*rr_**2*Fs["FF"]*S*RW.gam[i, i]
        D = RW.GEO.dric(h)

        def Dv(Am):
            return {(a + 1, b): c for (a, b), c in Am.items()}

        def Dr(Am):
            out = {}
            for (a, b), c in Am.items():
                dc = sp.diff(c, rr_)
                if dc != 0:
                    out[(a, b)] = out.get((a, b), 0) + dc
                out[(a, b + 1)] = out.get((a, b + 1), 0) + c
            return out
        base = {(0, 0): V/fs/2, (0, 1): -sp.diff(fs, rr_)/2, (0, 2): -fs/2}            # u_vr
        memo = {}

        def nf_jet(a, b):
            if a == 0 or b == 0:
                return {(a, b): sp.Integer(1)}
            if (a, b) not in memo:
                Xm = base
                for _ in range(b - 1):
                    Xm = normalize(Dr(Xm))
                for _ in range(a - 1):
                    Xm = normalize(Dv(Xm))
                memo[(a, b)] = Xm
            return memo[(a, b)]

        def normalize(Am):
            out = {}
            for (a, b), c in Am.items():
                if a and b:
                    for k, x in nf_jet(a, b).items():
                        out[k] = out.get(k, 0) + c*x
                else:
                    out[(a, b)] = out.get((a, b), 0) + c
            return out
        uK, rF, rFab, _ = KR.reconstruction("Phi")
        sub = {KR.mu: s**2, KR.m: mval}
        nm2ab = {"u": (0, 0), "u_v": (1, 0), "u_r": (0, 1), "u_vv": (2, 0), "u_vr": (1, 1), "u_rr": (0, 2)}

        def to_lc(e):
            return normalize({nm2ab[k]: c for k, c in KR.jets(e.subs(sub), uK).items()})
        Flc = {"FF": to_lc(rF/rr_), "Fvv": to_lc(rFab[0][0]/rr_), "Fvr": to_lc(rFab[0][1]/rr_),
               "Frr": to_lc(rFab[1][1]/rr_)}
        w, sg = sp.symbols("w sigma", positive=True)
        cw, sw = (1 - w**2)/(1 + w**2), 2*w/(1 + w**2)
        trig = {sp.tan(th): sw/cw, sp.cot(th): cw/sw, sp.sec(th): 1/cw, sp.csc(th): 1/sw, sp.cos(th): cw,
                sp.sin(th): sw}

        def zero_coeff(c):
            c = sp.expand_trig(c).subs(trig).subs(rr_, sg**2)
            return sp.cancel(sp.together(c)) == 0
        good = True
        count = 0
        for a in range(5):
            for b in range(a, 5):
                e = sp.expand(D[a][b].doit())
                terms = {}
                for term in sp.Add.make_args(e):
                    if term == 0:
                        continue
                    key = None
                    for fac in sp.Mul.make_args(term):
                        if (isinstance(fac, sp.Derivative) and fac.expr in Fs.values()) or fac in Fs.values():
                            key = fac
                    if key is None:
                        raise ValueError("a term of DRic without the perturbation: %s" % term)
                    terms[key] = terms.get(key, 0) + term/key
                total = {}
                for key, coef in terms.items():
                    fn, cnt = (key.expr, dict(key.variable_count)) if isinstance(key, sp.Derivative) else (key, {})
                    Xm = Flc[[n for n, F_ in Fs.items() if F_ == fn][0]]
                    for _ in range(cnt.get(rr_, 0)):
                        Xm = normalize(Dr(Xm))
                    for _ in range(cnt.get(v_, 0)):
                        Xm = normalize(Dv(Xm))
                    for k, x in Xm.items():
                        total[k] = total.get(k, 0) + coef*x
                comp = all(zero_coeff(c) for c in total.values())
                count += len(total)
                good &= comp
                if control and not comp:
                    break
            if control and not good:
                break
        say("  U3 (b)%s l = %d: DRic(h) = 0 modulo the master equation, %d jet coefficients over the 15 components "
              "(mixed derivatives eliminated): %s" % (" control (tensor potential)" if control else "", l, count, good),
              flush=True)
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
        # Theorem 2's weights, from the measured (max H-power, max r-power) of every entry: the extra weight w (r^-1
        # for (a), r^-1/2 for (b), r^0 for (c)) times the coefficient must be bounded by what the energies and Lemma S
        # control: (a) k/r for T^j P, 1 for d_r T^j P, k^2/r for P (H <= (11/8) k^2); (b) r^-1/2 for T^j P and k^2 P,
        # 1 for d_r T^j P; (c) 1 for T^j P (j = 1, 2) and d_r T^j P, r^-1/2 for k^2 P
        need = {"a": {"P_uu": -1, "P_u": -1, "P_ur": 0, "P_r": 0, "P": -1},
                "b": {"P_uu": -sp.Rational(1, 2), "P_u": -sp.Rational(1, 2), "P_ur": 0, "P_r": 0,
                      "P": -sp.Rational(1, 2)},
                "c": {"P_uu": 0, "P_u": 0, "P_ur": 0, "P_r": 0, "P": -sp.Rational(1, 2)}}
        extra = {"a": -1, "b": -sp.Rational(1, 2), "c": 0}
        meas = {}
        for k, cs in tab.items():
            for j, c in cs.items():
                K, mons = monomials(c)
                meas[(k, j)] = (max(a for a, _ in mons), max(b for _, b in mons))
        wt = {e: all(bm + extra[e] <= need[e][j] and am <= (1 if j == "P" else 0) for (k, j), (am, bm) in meas.items())
              for e in need}
        ea, eb, ec = wt["a"], wt["b"], wt["c"]
        say("  U4: r^(-1/2) h(e_a, e_b) and r^(1/2) 2F in the jets (P_rr eliminated by U3 (a)), monomials H^a r^b:",
              flush=True)
        for ln in lines:
            say(ln)
        say("  U4: the powers 0 attained (T^2 P in h00, T P in 2F): %s; Theorem 2's weights from the measured powers:"
            " (a) %s, (b) %s, (c) %s" % (att, ea, eb, ec))
        return ok and att and ea and eb and ec
    say("  U4 control (unweighted h00, h01, h11, 2F, same reader and bounds): passes: %s" % ok)
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
        # forced on C: P = (u - u1) a(r) + (u - u1)^2 b(r)/2 + (u - u1)^3 c(r)/6 + ..., (2.1) order by order in u - u1
        du_, af, bf_, cf = sp.Symbol("du"), sp.Function("a")(r), sp.Function("b")(r), sp.Function("c")(r)
        Pt_ = du_*af + du_**2*bf_/2 + du_**3*cf/6
        E21 = sp.expand(2*f*sp.diff(Pt_, du_, r) - f*sp.diff(f*sp.diff(Pt_, r), r) + V*Pt_)
        o0, o1 = E21.coeff(du_, 0), E21.coeff(du_, 1)
        da = sp.solve(o0, sp.diff(af, r))
        db = sp.solve(o1.subs(sp.diff(af, r, 2), 0).subs(sp.diff(af, r), da[0] if da else 1), sp.diff(bf_, r))
        forced = (len(da) == 1 and da[0] == 0 and len(db) == 1 and iszero(db[0] + af*V/(2*f)))
        Pc = {"P": 0, "P_r": 0, "P_rr": 0, "P_ur": 0, "P_u": A, "P_uu": Bf}   # at u = u1: P_ur = a' = 0
        onC = {k: sp.expand(sum(c*Pc[j] for j, c in cs[k].items())) for k in cs}
        a0 = {k: onC[k].subs(A, 0) for k in onC}
        fam = (iszero(a0["h00"] - Bf*sp.sqrt(r)/f) and iszero(a0["h01"] + a0["h00"])
               and iszero(a0["h11"] - a0["h00"]) and iszero(a0["2F"]))
        ang = iszero(onC["2F"] + A/sp.sqrt(r))
        cA = back(rat((onC["h00"] - Bf*sp.sqrt(r)/f)/A))
        cA_ok = iszero(cA + (2*m*r**4 - 3*m*mu*r**2 - 6*mu**2)/(sp.sqrt(r)*(r**2 - mu)*(m*r**2 + 6*mu)))
        say("  U5: on C (P = 0 along C) the equation forces d_r T P = 0, d_r T^2 P = -A V/(2f): %s; with A = 0, h00 ="
              " B r^(1/2)/f, h01 = -h00, h11 = h00, 2F = 0: %s; 2F = -A r^(-1/2): %s; h00 = r^(1/2) B/f + (%s) A"
              % (forced, fam, ang, cA))
        say("  U5: c_A = -(2 m r^4 - 3 m mu r^2 - 6 mu^2)/(r^(1/2)(r^2 - mu)(m r^2 + 6 mu)): %s" % cA_ok)
        ok &= forced and fam and ang and cA_ok
        # Kruskal: U = -e^(-u/r_h), V = e^(v/r_h), v - u = 2 r*
        rstar = r + (rh/2)*sp.log((r - rh)/(r + rh))
        k1 = sp.simplify(sp.diff(rstar, r) - 1/f) == 0
        mUV = sp.exp(2*rstar/rh)
        k2 = sp.simplify(sp.expand_log(mUV - sp.exp(2*r/rh)*(r - rh)/(r + rh), force=True)) == 0 or \
            sp.simplify(sp.powsimp(sp.expand_power_exp(mUV)) - sp.exp(2*r/rh)*(r - rh)/(r + rh)) == 0
        mUVr = sp.exp(2*r/rh)*(r - rh)/(r + rh)
        k3 = sp.simplify(sp.diff(mUVr, r).subs(r, rh) - sp.exp(2)/(2*rh)) == 0
        k4 = sp.simplify(f/mUVr - (r + rh)**2*sp.exp(-2*r/rh)/r**2) == 0
        k3b = sp.simplify(sp.diff(mUVr, r) - 2*r**2*sp.exp(2*r/rh)/(rh*(r + rh)**2)) == 0   # F' > 0 on (0, oo)
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
        say("  U5: dr*/dr = 1/f %s; -UV = e^(2r/r_h)(r - r_h)/(r + r_h) %s; d(-UV)/dr = e^2/(2 r_h) at r_h %s;"
              " f/(-UV) = (r + r_h)^2 e^(-2r/r_h)/r^2 %s; d_u d_v = -(UV/r_h^2) d_U d_V %s; d_u^2 = (U^2 d_U^2 + U d_U)"
              "/r_h^2 %s; d_t^2 - d_r*^2 = 4 d_u d_v %s; d(-UV)/dr = 2 r^2 e^(2r/r_h)/(r_h (r + r_h)^2) > 0 on"
            " r > 0: %s" % (k1, k2, k3, k4, k5, k6, k7, k3b))
        ok &= k1 and k2 and k3 and k4 and k5 and k6 and k7 and k3b
    Vl = potential(2).subs(mu, 1)
    integrand = sp.simplify(Vl/(1 - 1/r**2)) + (1/r if control else 0)
    I = sp.integrate(integrand, (r, 1, sp.oo))
    fin = I.is_finite is True and I.is_real is not False and (control or I == sp.Rational(11, 2))
    say("  U5%s: int_{r_h}^oo V/f dr at l = 2, r_h = 1: %s = %s, finite: %s"
          % (" control (V/f + 1/r)" if control else "", sp.simplify(I), sp.N(I, 12) if fin else I, fin))
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
    if ok:
        q0 = m + sp.Rational(15, 4)
        ok &= all(sp.expand(lc + c*q0/2) == 0 for lc, c in zip(lead_coef, (A, B, C3)))
        # independently: d/dr of P_j(1/r) is dP_j, and 2 f d_r P_j = f d_r(f d_r P_(j-1)) - V P_(j-1), to the order kept
        Vr = f*(Q/(16*(m + 6*mu/r**2)**2))/r**2
        for j in range(2, 5):
            Pr_ = Pj[j].subs(rho, 1/r)
            Pm = Pj[j - 1].subs(rho, 1/r)
            d1 = sp.expand((sp.diff(Pr_, r) - dP[j].subs(rho, 1/r)).subs(r, 1/rho))
            E = (2*f*sp.diff(Pr_, r) - f*sp.diff(f*sp.diff(Pm, r), r) + Vr*Pm).subs(r, 1/rho)
            E = sp.expand(sp.series(sp.together(E), rho, 0, order).removeO())
            ok &= d1 == 0 and all(E.coeff(rho, k) == 0 for k in range(order))
    say("  U6%s: d_r T^j P on C for j = 2, 3, 4 starts at rho^%s (rho = 1/r), coefficients %s (= -(m + 15/4)/2 times"
        " A, B, C3; the recursion re-checked by r-differentiation); r^p energies (p <= 2) finite: %s"
        % (" control (V/f + 1/r)" if control else "", pw, lead_coef, ok))
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
    # Hoelder for the r^p energies: int s^p w'^2 <= (int s w'^2)^(2-p) (int s^2 w'^2)^(p-1) on [1, oo), exactly
    # for w' = s^-2, s^-3, s^-2 (1 + 1/s) and p = 6/5, 3/2, 9/5; the control drops the E^2 factor
    hold_ok = True
    for wp in (sv**-2, sv**-3, sv**-2*(1 + 1/sv)):
        Ef = lambda q_: sp.integrate(sv**q_*wp**2, (sv, 1, sp.oo))
        for pp in (sp.Rational(6, 5), sp.Rational(3, 2), sp.Rational(9, 5)):
            lhs_h = Ef(pp)
            rhs_h = Ef(1) if control else Ef(1)**(2 - pp)*Ef(2)**(pp - 1)
            hold_ok &= bool(sp.N(rhs_h - lhs_h, 40) >= 0)
    if control:
        say("  U7 control (the lemma without int w^2/s^2; Hoelder without the E^2 factor): hold on the tests: %s, %s"
            % (ok, hold_ok))
        return ok or hold_ok
    t_, p_, d_ = sp.symbols("t p delta", positive=True)
    # L = d_t + d_r* on w(t, r) = W(t - r*(r), r): d_r* = f d_r|_t; on the outgoing chart it is f d_r|_u (test functions)
    rs = r + (sp.sqrt(mu)/2)*sp.log((r - sp.sqrt(mu))/(r + sp.sqrt(mu)))
    a_, b_ = sp.symbols("a b")
    iiL = True
    for Wt in (a_**3*b_ + sp.sin(a_)*b_**2, sp.exp(a_)/b_):
        wtr = Wt.subs({a_: t_ - rs, b_: r})
        L = sp.diff(wtr, t_) + f*sp.diff(wtr, r)
        Lb = (f*sp.diff(Wt, b_)).subs({a_: t_ - rs, b_: r})
        iiL &= sp.simplify(L - Lb) == 0
    k2 = sp.Symbol("k2", positive=True)
    xx = sp.Symbol("x", nonnegative=True)
    c1 = all(ll*(ll + 2) >= 8 for ll in range(2, 200, 2))
    Hk = k2 - 3 + 6*xx
    c2 = sp.simplify(sp.Rational(11, 8)*k2 - Hk.subs(xx, 1) - sp.Rational(3, 8)*(k2 - 8)) == 0   # = 0 at x = 1, k2 >= 8
    c3 = sp.expand(k2**2 - (1 + (k2 - 3))**2) == sp.expand(4*k2 - 4)                            # >= 0 for k2 >= 1
    holder = sp.simplify(sv**(2 - p_)*(sv**2)**(p_ - 1) - sv**p_) == 0 and sp.simplify((2 - p_) + (p_ - 1) - 1) == 0
    ip = sp.simplify(sp.integrate(sv**(-p_), (sv, R, sp.oo), conds="none") - R**(1 - p_)/(p_ - 1)) == 0
    rate_c = sp.simplify((-(2 - p_)/2).subs(p_, 1 + 2*d_) - (-sp.Rational(1, 2) + d_)) == 0   # (c)'s exponent
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
    ok &= iiL and c1 and c2 and c3 and holder and ip and hold_ok and rate_c and cone and sph and chain
    say("  U7 (ii)-(iii): T(L, T) = (1/2)(L psi)^2 + (1/2) f r^-2 |D psi|^2 on the cone: %s; int |D Y|^2 = (k^2 - 6)"
          " int |Y|^2 at l = 2, 4: %s; C_1 = 9/(2 f_1) + 8 from k^2 <= 4 (k^2 - 6) (k^2 >= 8): %s" % (cone, sph, chain))
    say("  U7: d_s(w^2/s) and the lemma on w = 1, s^(1/4), s^(1/3), 1 + 1/s at R = 1, 2, 10, 1000: True; L = f d_r|_u:"
          " %s; k^2 >= 8 (l = 2..198): %s; H <= (11/8)k^2 at x <= 1: %s; k^4 - (1 + m)^2 = 4k^2 - 4: %s; Hoelder"
          " s^p = s^(2-p) (s^2)^(p-1): %s; int_R^oo s^-p = R^(1-p)/(p-1): %s; the interpolation E^p <= (E^1)^(2-p)"
          " (E^2)^(p-1) on three test functions at p = 6/5, 3/2, 9/5: %s; -(2 - p)/2 = delta - 1/2 at p = 1 + 2 delta:"
          " %s" % (iiL, c1, c2, c3, holder, ip, hold_ok, rate_c))
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
    say("  U8%s: the old text occurs %d time(s) in the paper, the new text %d; new keeps the old opening: %s;"
        " widest line %d (<= 121: %s); all: %s" % (" control (r <= R)" if control else "", n_old, n_new,
                                                    new.startswith(old.split(" (uniformly")[0]), width,
                                                    width <= 121, ok))
    return ok


# --------------------------------------------------------------------------------------------------------------- U9
def u9(control=False):
    """the angular Sobolev inequality of Theorem 2' on S^3: sup|w|^2 <= (1/12) ||(1 - Lap) w||^2, its constants, the
    Casimir of the six rotations, and the ingredients of the tensor version"""
    import rwgauge5 as RW
    th, p1, p2 = RW.th, RW.p1, RW.p2
    x1, x2, x3, x4 = sp.symbols("x1:5", real=True)
    xs = [x1, x2, x3, x4]
    hopf = {x1: sp.cos(th)*sp.cos(p1), x2: sp.cos(th)*sp.sin(p1), x3: sp.sin(th)*sp.cos(p2), x4: sp.sin(th)*sp.sin(p2)}
    sq = sp.sin(th)*sp.cos(th)

    def lap(w):                                                    # Lap on S^3 in Hopf coordinates
        return (sp.diff(sq*sp.diff(w, th), th)/sq + sp.diff(w, p1, 2)/sp.cos(th)**2 + sp.diff(w, p2, 2)/sp.sin(th)**2)

    pairs = [(a, b) for a in range(4) for b in range(4) if a < b] if not control else \
        [(a, b) for a in range(4) for b in range(4) if a != b]       # control: every ordered pair (twice the sum)

    def Om(a, b, g):
        return xs[a]*sp.diff(g, xs[b]) - xs[b]*sp.diff(g, xs[a])
    tests = [sp.legendre(j, x1**2 + x2**2 - x3**2 - x4**2) for j in (1, 2, 3)] + [x1*x3 + x2**2*x4 + x1]
    cas = True
    for g in tests:
        lhs = sum(Om(a, b, Om(a, b, g)) for a, b in pairs).subs(hopf)
        cas &= sp.simplify(sp.expand_trig(lhs - lap(g.subs(hopf)))) == 0
    if control:
        Lc = sp.Symbol("L", integer=True, nonnegative=True)
        series = sp.summation((Lc + 1)**2/(Lc + 1)**3, (Lc, 0, sp.oo))   # (1 - Lap)^(3/4) in place of (1 - Lap)
        say("  U9 control (the Casimir over ordered pairs; the series with (1 - Lap)^(3/4)): %s, finite %s"
            % (cas, series.is_finite))
        return cas or bool(series.is_finite)
    L = sp.Symbol("L", integer=True, nonnegative=True)
    dims = all(sp.binomial(ll + 3, 3) - sp.binomial(ll + 1, 3) == (ll + 1)**2 for ll in range(0, 21))
    vol = sp.integrate(sq, (th, 0, sp.pi/2))*(2*sp.pi)**2
    cas1 = all(sp.expand(1 + ll*(ll + 2) - (ll + 1)**2) == 0 for ll in range(0, 21))
    zeta2 = sp.summation(1/(L + 1)**2, (L, 0, sp.oo))
    const = sp.simplify(zeta2/vol)
    # the reproducing kernel of degree l at a point: K = ((l + 1)/(2 pi^2)) U_l(cos psi), |K|^2 = K(0) = (l + 1)^2/vol
    psi = sp.Symbol("psi", positive=True)
    ker = True
    for ll in range(0, 7):
        K = (ll + 1)/(2*sp.pi**2)*sp.chebyshevu(ll, sp.cos(psi))
        nK = sp.integrate(sp.expand(K**2*4*sp.pi*sp.sin(psi)**2), (psi, 0, sp.pi))
        lapK = sp.diff(sp.sin(psi)**2*sp.diff(K, psi), psi)/sp.sin(psi)**2
        ker &= (sp.simplify(nK - K.subs(psi, 0)) == 0 and sp.simplify(K.subs(psi, 0) - (ll + 1)**2/vol) == 0
                and sp.simplify(lapK + ll*(ll + 2)*K) == 0)
    # ||Lap w||^2 = sum_{ij} ||Om_i Om_j w||^2 on a test function (exact integration over S^3)
    w = x1*x3 + x2**2*x4 + x1

    def integ(e):
        e = sp.expand(sp.expand_trig(e*sq))
        return sp.integrate(sp.integrate(sp.integrate(e, (p1, 0, 2*sp.pi)), (p2, 0, 2*sp.pi)), (th, 0, sp.pi/2))
    nl = integ(lap(w.subs(hopf))**2)
    no = sum(integ(Om(a, b, Om(c, d, w)).subs(hopf)**2) for a, b in pairs for c, d in pairs)
    lapnorm = sp.simplify(nl - no) == 0
    # the tensor version: the rotation generators have operator norm 1, and L_Om P = 0 for P = 1 - x x^T/|x|^2
    opn = True
    proj = True
    X4 = sp.Matrix(xs)
    Pm = sp.eye(4) - X4*X4.T/(X4.T*X4)[0]
    for a, b in pairs:
        om = sp.zeros(4)
        om[a, b], om[b, a] = 1, -1
        opn &= max(abs(e) for e in (om.T*om).eigenvals()) == 1
        Omv = om*X4                                                # the vector field Om^C = om_CD x_D
        LP = sp.Matrix(4, 4, lambda A_, B_: sum(Omv[C]*sp.diff(Pm[A_, B_], xs[C]) for C in range(4))
                       + sum(Pm[C, B_]*om[C, A_] + Pm[A_, C]*om[C, B_] for C in range(4)))
        proj &= all(sp.simplify(e) == 0 for e in LP)
    cA_, cB_, cC_, cD_ = sp.symbols("a b c d", nonnegative=True)
    cs4 = sp.expand(4*(cA_**2 + cB_**2 + cC_**2 + cD_**2) - (cA_ + cB_ + cC_ + cD_)**2)  # = sum of squares of diffs
    cs4_ok = sp.expand(cs4 - sum((s1 - s2)**2 for i_, s1 in enumerate((cA_, cB_, cC_, cD_))
                                 for s2 in (cA_, cB_, cC_, cD_)[i_ + 1:])) == 0
    consts = (4*1, 4*4*6 + 4*4*6, 4*16*36) == (4, 192, 2304)
    ok = dims and vol == 2*sp.pi**2 and cas1 and zeta2 == sp.pi**2/6 and const == sp.Rational(1, 12) and ker and \
        cas and lapnorm and opn and proj and cs4_ok and consts
    say("  U9: dim of degree-l harmonics on S^3 = (l + 1)^2 (l <= 20) %s; vol = %s; 1 + l(l + 2) = (l + 1)^2 %s;"
        " sum (l + 1)^-2 = %s, so sup|w|^2 <= %s ||(1 - Lap) w||^2; the kernel ((l + 1)/(2 pi^2)) U_l: norm^2 = value"
        " = (l + 1)^2/vol, eigenvalue -l(l + 2), l <= 6: %s; sum over the six rotations of Om^2 = Lap on four test"
        " functions: %s; ||Lap w||^2 = sum ||Om_i Om_j w||^2 (test function): %s; rotation generators of norm 1: %s;"
        " L_Om P = 0: %s; (a + b + c + d)^2 <= 4 (a^2 + ... + d^2): %s; the constants 4, 192, 2304: %s"
        % (dims, vol, cas1, zeta2, const, ker, cas, lapnorm, opn, proj, cs4_ok, consts))
    return ok


# -------------------------------------------------------------------------------------------------------------- U10
def u10(control=False):
    """[HKW18] (163), (168), (169) applied to the perturbation that (10.1) builds from P (static chart, mixed indices
    in (163), Hcheck = r F, hcheck_AB = r F_AB by (159)-(162) in the gauge): Phi = P exactly, every other jet cancelling
    once the master equation removes d_t^2 P; the control multiplies V by 1 + mu/r^2"""
    n = 3
    x = mu/r**2
    H = m + 6*x
    V, _ = potential_general()
    if control:
        V = V*(1 + x)

    def add(A_, B_, c=1):
        out = dict(A_)
        for k, val in B_.items():
            out[k] = out.get(k, 0) + c*val
        return out

    def scal(A_, c):
        return {k: c*val for k, val in A_.items()}
    base = {(0, 0): -V, (0, 1): f*sp.diff(f, r), (0, 2): f**2}       # P_tt = f (f P_r)_r - V P
    memo = {}

    def njet(a, b):
        if a < 2:
            return {(a, b): sp.Integer(1)}
        if (a, b) not in memo:
            Xm = base
            for _ in range(b):
                Xm = Dr(Xm)
            for _ in range(a - 2):
                Xm = Dt(Xm)
            memo[(a, b)] = Xm
        return memo[(a, b)]

    def norm(A_):
        out = {}
        for (a, b), c in A_.items():
            if c == 0:
                continue
            for k, val in (njet(a, b).items() if a >= 2 else [((a, b), sp.Integer(1))]):
                out[k] = out.get(k, 0) + c*val
        return out

    def Dr(A_):
        out = {}
        for (a, b), c in A_.items():
            out[(a, b)] = out.get((a, b), 0) + sp.diff(c, r)
            out[(a, b + 1)] = out.get((a, b + 1), 0) + c
        return norm(out)

    def Dt(A_):
        return norm({(a + 1, b): c for (a, b), c in A_.items()})
    fp = sp.diff(f, r)
    gam_ = {("t", "t", "r"): fp/(2*f), ("r", "t", "t"): f*fp/2, ("r", "r", "r"): -fp/(2*f)}  # -f dt^2 + dr^2/f
    idx = ("t", "r")
    gl = {("t", "t"): -f, ("r", "r"): 1/f, ("t", "r"): 0, ("r", "t"): 0}
    gu = {("t", "t"): -1/f, ("r", "r"): f}
    Pt0 = {(0, 0): r**sp.Rational(3, 2)*H}                         # Phi~ = r^(3/2) H P
    d1 = {"t": Dt(Pt0), "r": Dr(Pt0)}
    DD = {}
    for a in idx:
        for b in idx:
            e = Dt(d1[b]) if a == "t" else Dr(d1[b])
            for c in idx:
                gc = gam_.get((c, a, b), gam_.get((c, b, a), 0))
                if gc != 0:
                    e = add(e, d1[c], -gc)
            DD[(a, b)] = e
    box = add(scal(DD[("t", "t")], gu[("t", "t")]), scal(DD[("r", "r")], gu[("r", "r")]))
    rF = add(scal(Pt0, (2*H - 3*r*fp)/(12*r**2*H)), scal(d1["r"], 6*r*gu[("r", "r")]/(12*r**2*H)))
    rFab = {ab: add(add(scal(DD[ab], 1/H), scal(box, -gl[ab]/(2*H))), scal(rF, -gl[ab])) for ab in DD}
    Xh = add(scal(rFab[("t", "t")], gu[("t", "t")]), scal(rF, -2))     # hcheck^t_t - 2 Hcheck
    Yh = add(scal(rFab[("r", "r")], gu[("r", "r")]), scal(rF, -2))     # hcheck^r_r - 2 Hcheck
    Zt = add(add(scal(add(Dr(Xh), Dr(Yh)), f), scal(Xh, -((n - 2)*f/r + fp/2))), scal(Yh, 2*f/r - fp/2))
    Zt = scal(Zt, 1/((m + 3)/r**2 - sp.diff(f, r, 2) - n*fp/r))        # (168)
    Phi = scal(add(scal(Zt, n), scal(add(Xh, Yh), -r)), 1/(r**sp.Rational(1, 2)*(m + 3 - n + 6*x)))   # (169)
    res = {k: rat(val) for k, val in Phi.items()}
    res = {k: val for k, val in res.items() if val != 0}
    ok = list(res) == [(0, 0)] and res[(0, 0)] == 1
    say("  U10%s: [HKW18] (169)'s Phi of the (10.1) perturbation, reduced by the master equation, at general l: jets %s,"
        " coefficient of P %s: Phi = P exactly: %s" % (" control (V (1 + mu/r^2))" if control else "", sorted(res),
                                                      back(res.get((0, 0), 0)) if not control else "not 1", ok))
    return ok


CHECKS = [("U1", u1), ("U2", u2), ("U3", u3), ("U4", u4), ("U5", u5), ("U6", u6), ("U7", u7), ("U8", u8),
          ("U9", u9), ("U10", u10)]


def main():
    only = sys.argv[1:]
    ok = True
    for name, fn in CHECKS:
        if only and name not in only:
            continue
        good = fn()
        ctl = fn(control=True)
        say("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    say("EXIT %d" % (0 if ok else 1))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
