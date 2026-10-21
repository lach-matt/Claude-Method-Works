#!/usr/bin/env python3
"""damping5.py -- strong constraint damping at zero energy in five dimensions: the indicial roots of the constraint
propagation wave operator of [Hin26a] on 4+1 Minkowski, the model at infinity of five-dimensional Tangherlini
(N1STAR-PROOF.md section 10.12; ROUTES-OPEN.md 4.4 item 2; D54).  Labels: computed (exact, sympy; U6 numerical), READ.

Route B's nonlinear step ([Hin26], arXiv:2606.28253v2) uses the gauge-fixed Einstein operator Ric(g) - delta*_{g,C}
Upsilon(g), whose constraint propagation wave operator box^C = 2 delta_g G_g (delta*_g + C) must have no indicial root
of its zero energy operator with real part in [-C_0, 1) ([Hin26] (1.43), "C_0 = 100 suffices by a large margin"); in
four dimensions this is [Hin26a]'s Theorem 4.9 (arXiv:2606.27658v2), with C omega = h^-1 (2 c (x)_s omega - (1 - e) g
iota_{c#} omega), c = r^-1 (dt - v dr), v in (0, 1), e > 0 small and then h > 0 small.  Indicial roots see only the
Minkowski model at infinity ([Hin26] Theorem 7.1's proof: "Parts (3) and (4) only see the Minkowskian model").  This
instrument computes them in five dimensions, from the definitions, with a four-dimensional control against his
printed formulas.  delta* omega = (1/2)(omega_{a;b} + omega_{b;a}), G = Id - (1/2) g tr_g, (delta k)_a = -g^{bc}
k_{ab;c}; the frame (dx^0, dx^1, r T*S^{n-1}), x^0 = t + r, x^1 = t - r, as his (4.10); kappa := l (l + n - 2), the
eigenvalue of the Laplacian on S^{n-1}.

  U1 (computed, exact) The indicial families.  box^C is computed from its definition on Minkowski^{n+1}, n = 3, 4, in
     polar coordinates, on the stationary 1-forms r^-lam (a S dx^0 + b S dx^1 + c r dS) (scalar type) and r^(1-lam) V
     (vector type), S = Re (x_1 + i x_2)^l (sin^l th cos(l ph) on S^2, cos^l th cos(l p_1) on S^3) and V = *dS on S^2,
     V = Re (x_3 + i x_4)^(l-1) (x_1 dx_2 - x_2 dx_1) on S^3, with l a symbol: the zero energy operator returns the same
     type times r^(-lam-2), with a 3 x 3 (scalar l >= 1), 2 x 2 (l = 0) and 1 x 1 (vector) matrix N(lam) whose entries
     are free of the angles and affine in kappa.  Control (n = 3, weight 1): N is his (4.19) with Corollary 4.7's q_00,
     ..., q_// entry by entry, and his p_v ((A.2)'s polynomial), p_s0 and the sextic (A.13) follow as h N_v, h^2
     det N_s0/(lam - 1) and -h^3 det N_sl, at l = 1, 2, 3.  Mutant: the trace reversal G dropped.
  U2 (computed, exact) The weight.  G (g f) = (1 - D/2) g f in D = n + 1 dimensions, so with C omega = h^-1 (2 c (x)_s
     omega - m (1 - e) g iota_{c#} omega), 2 h G C omega = 2 (2 c (x)_s omega) + 2 (-1 + m (1 - e)(D/2 - 1)) g <c,
     omega>, which is his h^-1 (2 c (x)_s omega - e g <c, omega>) -- the form whose semiclassical symbol is his
     Lemma 3.2's l_{g,c,e} -- for every e iff m = 2/(D - 2): 1 in four dimensions, 2/3 in five.  His weight 1 is the
     four-dimensional value of the dimension-adapted 2/(D - 2).  Control: m = 1 in five dimensions.
  U3 (computed, exact) The five-dimensional polynomials (weight 2/3).  Vector type: p_v = -h lam^2 + (2h - 2v) lam + h
     kappa + 6 v (four dimensions: -h lam^2 + (h - 2v) lam + h kappa + 4 v, his).  lam = 2 is a root of scalar types 0
     and 1 for all (v, e, h) (four dimensions: lam = 1, his), the Coulomb rate r^-(n-2).  At h = 0 the scalar-type sextic
     h^3 det N_sl is 8 v (lam - 2) Q_5, Q_5 = e ((v^2 - 1) kappa + (1 + v^2)(lam - 3)(lam + 1)) - 2 v^2 (lam - 2)(lam -
     3), and -16 v^3 (lam - 3)(lam - 2)^2 at e = 0 (four dimensions: 8 v (lam - 1) Q_4 and -16 v^3 (lam - 2)(lam -
     1)^2, his (P1) roots 1, 1, 2); the very negative roots, lam = (h lt)^-1, have the h = 0 limit (2 v lt + 1)(4 e (1 +
     v^2) lt^2 + 2 e v lt - 8 v^2 lt^2 - 6 v lt - 1) in both dimensions.  Control: the exceptional root claimed 1.
  U4 (computed, exact) The certificate.  At (v, e, h) = (1/2, 1/100, 1/1000) and C_0 = 100, for every real kappa >= 3
     the scalar-type sextic and the vector quadratic have no root on Re lam = -100 nor on Re lam = 19/10: shifted to the
     line, the constant coefficient and the Hurwitz determinant Delta_{deg-1} have no root in kappa >= 3 (Sturm), and
     Delta_{deg-1} vanishes whenever two roots sum to zero (Orlando's formula), so no root lies on either line; the
     leading coefficient -h^3 does not vanish, so roots move continuously in kappa and cannot enter the strip; at l = 1
     (Routh arrays) 3 roots have Re lam > 19/10 and 3 have Re lam < -100, and 1 and 1 for the vector type; the scalar
     type 0 quartic, 2 and 2.  So no indicial root at any l has real part in [-100, 19/10], and (1.43) holds with C_0
     = 100 and nine tenths to spare.  Up to the Coulomb root: at the line 2 the same argument for kappa >= 8 (l >= 2,
     counts 3 | 0 | 3 at l = 2), and at l = 1 and l = 0 the cofactors of lam - 2, a quintic and a cubic, 2 | 0 | 3 and
     1 | 0 | 2 (Routh), the vector type 1 | 0 | 1: the only roots with real part in [-100, 2] are lam = 2 at l = 0 and
     l = 1, simple, so none lies in [-100, 2) -- (1.43) in its five-dimensional form, the strip ending at the Coulomb
     root r^-(n-2) as his ends at r^-1.  Four-dimensional control: the same at the lines 9/10 and 1, his Theorem 4.9 at
     these parameters.  Control: the line 21/10, which lam = 2 at l = 1 lies to the left of.
  U5 (computed, exact) His weight transcribed literally fails in five dimensions.  With m = 1, the scalar type 0 cubic
     at h = 0 has the root (7 v^2 - 1 + 3 e (1 + v^2))/(5 v^2 + 1 - 3 e (1 + v^2)), which at e = 0 is
     (7 v^2 - 1)/(5 v^2 + 1), in (-1, 1) for every v in (0, 1); at the parameters of U4 the quartic has a real root in
     (0, 1) (Sturm), in [-C_0, 1), and the scalar type 1 sextic a root in the strip.  Control: the weight 2/3 has no
     root in (0, 1).
  U6 (computed, numerical; a measurement) The configuration over the parameters.  v = 1/2, e in {10^-2, 10^-3,
     10^-4}, h in {10^-2, 10^-3, 10^-4}, l up to 1.5 10^6 (mpmath polyroots, 50 digits): the least real part of the upper
     roots and the largest of the lower, weight 2/3.  Besides the exceptional root lam = 2 at l = 1 (U3), found at all
     nine, the upper roots stay above 1.93 at all nine: above 2 exactly where h <= e (six points), below 2 where h > e
     (three; the least, 1.939, at e = 10^-4, h = 10^-2, l = 5); the lower ones are about -1/h.  Control: h = 3/10.

READ (alphaXiv, 2026-10-21).  [Hin26a] pp. 1-3 (Theorem 1.1, (1.1)-(1.2)), 5, 7, 25 (Definition 3.1, Lemma 3.2), 29,
33-37 (section 4.3, Lemma 4.6, Corollary 4.7, (4.19), Definition 4.8, Theorem 4.9, Remarks 4.10-4.12), 67 (Theorem
6.2), 69-74 (Appendix A: (A.1)-(A.2), A.2, (A.13)), 85.  [Hin26] pp. 1, 4, 25-26, 29 ((1.43)), 82 (Definition 4.2,
(4.6)-(4.9)), 136 (Theorem 7.1).

sympy, mpmath.  python3 damping5.py [--selftest | --mutants]   (about eighty seconds; --verbose lists every sub-check)
"""
import sys
import time

import mpmath as mpm
import sympy as sp

t, r = sp.symbols("t r", positive=True)
lam, e, v, h, m = sp.symbols("lambda e v h m")
K = sp.Symbol("kappa")
L = sp.Symbol("l", positive=True, integer=True)
mu_ = sp.Symbol("mu")
lt = sp.Symbol("lt")
D = sp.diff
PARAMS = {v: sp.Rational(1, 2), e: sp.Rational(1, 100), h: sp.Rational(1, 1000)}
C0 = 100


class Checklist:
    def __init__(self, verbose, quiet=False):
        self.ok, self.verbose, self.quiet = True, verbose, quiet

    def __call__(self, name, good):
        self.ok &= bool(good)
        if self.verbose or (not good and not self.quiet):
            print("      [%s] %s" % ("ok" if good else "FAIL", name), flush=True)


# ------------------------------------------------------------------------------------------------- the operator
def setup(n):
    if n == 3:
        th, ph = sp.symbols("theta phi")
        X, g, ang = [t, r, th, ph], sp.diag(-1, 1, r**2, r**2*sp.sin(th)**2), [th, ph]
    else:
        th, p1, p2 = sp.symbols("theta p1 p2")
        X, g, ang = [t, r, th, p1, p2], sp.diag(-1, 1, r**2, r**2*sp.cos(th)**2, r**2*sp.sin(th)**2), [th, p1, p2]
    N = len(X)
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[a, d]*(D(g[d, b], X[c]) + D(g[d, c], X[b]) - D(g[b, c], X[d])) for d in range(N))/2)
             for c in range(N)] for b in range(N)] for a in range(N)]
    return X, g, gi, Gam, ang


def box_c(n, w, use_G=True):
    """2 delta G (delta* + C) w on Minkowski^{n+1}, C w = h^-1 (c w + w c - m (1 - e) g <c, w>), c = r^-1 (dt - v dr)"""
    X, g, gi, Gam, ang = setup(n)
    N = len(X)
    c = [1/r, -v/r] + [0]*(N - 2)
    nab = [[D(w[a], X[b]) - sum(Gam[k][b][a]*w[k] for k in range(N)) for b in range(N)] for a in range(N)]
    cw = sum(gi[a, b]*c[a]*w[b] for a in range(N) for b in range(N))
    T = sp.Matrix(N, N, lambda a, b: (nab[a][b] + nab[b][a])/2 + (c[a]*w[b] + c[b]*w[a] - m*(1 - e)*g[a, b]*cw)/h)
    if use_G:
        T = T - g*sum(gi[a, b]*T[a, b] for a in range(N) for b in range(N))/2
    out = []
    for a in range(N):
        s = 0
        for k in range(N):
            for q in range(N):
                if gi[k, q] != 0:
                    s += gi[k, q]*(D(T[a, k], X[q]) - sum(Gam[j][q][a]*T[j, k] + Gam[j][q][k]*T[a, j] for j in range(N)))
        out.append(-2*s)
    return out, ang


def _red(x):
    return sp.simplify(sp.powsimp(sp.expand_trig(sp.expand(x)), force=True))


def scalar_matrix(n, l=L, use_G=True):
    X, g, gi, Gam, ang = setup(n)
    S = sp.sin(ang[0])**l*sp.cos(l*ang[1]) if n == 3 else sp.cos(ang[0])**l*sp.cos(l*ang[1])
    a, b, cc = sp.symbols("a b c")
    w = [r**-lam*(a + b)*S, r**-lam*(a - b)*S] + [r**(1 - lam)*cc*D(S, x) for x in ang]
    R, ang = box_c(n, w, use_G)
    R = [sp.expand(sp.powsimp(sp.expand(x*r**(lam + 2)), force=True)) for x in R]
    rows = [_red((R[0] + R[1])/2/S), _red((R[0] - R[1])/2/S)]
    var = (a, b)
    if l != 0:
        rows.append(_red(R[2]/(r*D(S, ang[0]))))
        var = (a, b, cc)
    M = sp.Matrix([[sp.expand(q).coeff(x) for x in var] for q in rows]).applyfunc(sp.simplify)
    return M


def vector_entry(n, l=L, use_G=True):
    X, g, gi, Gam, ang = setup(n)
    if n == 3:
        S = sp.sin(ang[0])**l*sp.cos(l*ang[1])
        V = [-D(S, ang[1])/sp.sin(ang[0]), sp.sin(ang[0])*D(S, ang[0])]
    else:
        V = [0, sp.sin(ang[0])**(l - 1)*sp.cos((l - 1)*ang[2])*sp.cos(ang[0])**2, 0]
    w = [0, 0] + [r**(1 - lam)*x for x in V]
    R, ang = box_c(n, w, use_G)
    R = [sp.expand(sp.powsimp(sp.expand(x*r**(lam + 2)), force=True)) for x in R]
    k = [i for i, x in enumerate(V) if x != 0][0]
    return _red(R[2 + k]/(r*V[k]))


_CACHE = {}


def matrices(n, use_G=True):
    key = (n, use_G)
    if key not in _CACHE:
        Ml = scalar_matrix(n, L, use_G)
        M0 = scalar_matrix(n, 0, use_G)
        Vl = vector_entry(n, L, use_G)
        kap = L*(L + n - 2)

        def to_k(x):
            """a2 l^2 + a1 l + a0 with a1 = (n - 2) a2 -> a2 kappa + a0 (None if not of that form)"""
            P = sp.Poly(sp.expand(x*h), L)
            if P.degree() > 2:
                return None
            a2, a1, a0 = ([0]*(2 - P.degree()) + P.all_coeffs())
            if sp.simplify(a1 - (n - 2)*a2) != 0:
                return None
            return sp.simplify((a2*K + a0)/h)
        Mk = Ml.applyfunc(to_k)
        Vk = to_k(Vl)
        _CACHE[key] = (Ml, M0, Vl, Mk, Vk, kap)
    return _CACHE[key]


def polys(n, mv, use_G=True):
    Ml, M0, Vl, Mk, Vk, kap = matrices(n, use_G)
    pk = sp.expand(sp.simplify(Mk.subs(m, mv).det()*h**3))
    p0 = sp.expand(sp.simplify(M0.subs(m, mv).det()*h**2))
    pv = sp.expand(Vk.subs(m, mv)*h)
    return pk, p0, pv


# ------------------------------------------------------------------------------------------------- U1
def hintz_N(lv):
    """[Hin26a] (4.19) with Corollary 4.7's q's at a scalar type l (l = 0: the 2 x 2 block), transcribed"""
    q00 = (1 - 3*v + e + e*v)*lam + (-1 + 3*v + e + e*v)
    q10 = (1 - e)*(1 + v)*lam - (1 + e)*(1 + v)
    q01 = -(1 - e)*(1 - v)*lam + (1 + e)*(1 - v)
    q11 = (-1 - 3*v - e + e*v)*lam + (1 + 3*v - e + e*v)
    qsl = -2*v*lam + 4*v
    kap = lv*(lv + 1)
    if lv == 0:
        return (-lam**2 + lam)*sp.eye(2) + sp.Matrix([[1, -1], [-1, 1]]) + sp.Matrix([[q00, q01], [q10, q11]])/h
    q0s, q1s, qs0, qs1 = (1 - v)*kap, (1 + v)*kap, -2*e*(1 + v), -2*e*(1 - v)
    return ((-lam**2 + lam)*sp.eye(3) + sp.diag(kap, kap, kap - 1) + sp.Matrix([[1, -1, -kap], [-1, 1, kap], [-2, 2, 1]])
            + sp.Matrix([[q00, q01, q0s], [q10, q11, q1s], [qs0, qs1, qsl]])/h)


def hintz_A13(lv):
    k = lv*(lv + 1)
    return (h**3*lam**6 + (2*(4 - e)*v - 3*h)*h**2*lam**5
            + (4*(5 - 2*e)*v**2 - 4*e - 2*(13 - e)*h*v - (3*k - 1)*h**2)*h*lam**4
            + (8*((2 - e)*v**2 - e)*v - 4*((18 - 3*e)*v**2 - e)*h + 2*((10 + e)*v + 2*(e - 4)*v*k)*h**2
               + 3*(1 + 2*k)*h**3)*lam**3
            + (-16*v*((4 - e)*v**2 - e) + 4*((19 + 2*e)*v**2 - ((5 - e)*v**2 - 2*e)*k + e)*h
               + 2*(5 - e + 2*(8 - e)*k)*v*h**2 + (3*(lv**2 + lv - 1)*k - 2)*h**3)*lam**2
            + (8*((10 + e)*v**2 + e*(1 + (1 - v**2)*k))*v + 4*((11*k - 2)*v**2 - e*(1 + 3*v**2 + (1 + 2*v**2)*k))*h
               - 2*(6 + 8*k - (4 - e)*k**2)*v*h**2 - 3*k**2*h**3)*lam
            + (-8*v*(4*v**2 + e*(2*(1 + v**2) + (1 - v**2)*k)) - 4*(2*(2 + 3*k)*v**2 + e*(1 - v**2)*k*(lv**2 + lv - 1))*h
               - 2*(2 + (3 - e)*k)*k*v*h**2 - (lv - 1)*k**2*(lv + 2)*h**3))


def hintz_ps0():
    return (h**2*lam**3 + (2*(3 - e)*h*v - h**2)*lam**2 + (4*(2 - e)*v**2 - 4*e - 2*(e + 3)*h*v - 2*h**2)*lam
            - 4*((2 + e)*v**2 + e + h*v))


def u1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    use_G = control != 1
    for n in (3, 4):
        Ml, M0, Vl, Mk, Vk, kap = matrices(n, use_G)
        free = set().union(*[x.free_symbols for x in list(Ml) + list(M0) + [Vl]])
        chk("n = %d: the indicial matrices are free of the angles and of r" % n,
            not (free - {lam, e, v, h, m, L}))
        chk("n = %d: affine in kappa = l(l + n - 2): every entry is a2 l^2 + (n - 2) a2 l + a0" % n,
            all(x is not None for x in list(Mk) + [Vk]))
        chk("n = %d: the l = 0 matrix is the 2 x 2 block at kappa = 0" % n,
            sp.simplify(Mk[:2, :2].subs(K, 0) - M0) == sp.zeros(2, 2))
    Ml, M0, Vl, Mk, Vk, kap = matrices(3, use_G)
    ok = True
    for lv in (0, 1, 2, 3):
        mine = (M0 if lv == 0 else Mk.subs(K, lv*(lv + 1))).subs(m, 1)
        ok &= sp.simplify(mine - hintz_N(lv)) == sp.zeros(*mine.shape)
    chk("n = 3, weight 1: N is [Hin26a] (4.19) with Corollary 4.7's q's, entry by entry, at l = 0, 1, 2, 3", ok)
    pv = sp.expand(Vk.subs(m, 1)*h)
    chk("n = 3: h N_v = -h lam^2 + (h - 2v) lam + (l(l + 1) h + 4v), his p_v",
        sp.simplify(pv - (-h*lam**2 + (h - 2*v)*lam + (K*h + 4*v))) == 0)
    p0 = sp.factor(sp.simplify(M0.subs(m, 1).det()*h**2))
    chk("n = 3: h^2 det N_s0/(lam - 1) = his p_s0", sp.simplify(p0/(lam - 1) - hintz_ps0()) == 0)
    ok = True
    for lv in (1, 2, 3):
        ok &= sp.expand(-h**3*Mk.subs({K: lv*(lv + 1), m: 1}).det() - hintz_A13(lv)) == 0
    chk("n = 3: -h^3 det N_sl = his (A.13) at l = 1, 2, 3", ok)
    return chk.ok


# ------------------------------------------------------------------------------------------------- U2
def u2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in (3, 4):
        Dm = n + 1
        X, g, gi, Gam, ang = setup(n)
        N = len(X)
        cs = sp.symbols("c0:%d" % N)
        ws = sp.symbols("w0:%d" % N)
        cw = sum(gi[a, b]*cs[a]*ws[b] for a in range(N) for b in range(N))
        mv = sp.Rational(2, Dm - 2) if not (control == 1 and n == 4) else 1
        Cm = sp.Matrix(N, N, lambda a, b: cs[a]*ws[b] + cs[b]*ws[a] - mv*(1 - e)*g[a, b]*cw)
        GC = Cm - g*sum(gi[a, b]*Cm[a, b] for a in range(N) for b in range(N))/2
        want = sp.Matrix(N, N, lambda a, b: cs[a]*ws[b] + cs[b]*ws[a] - e*g[a, b]*cw)
        chk("D = %d: G (2 c (x)_s w - m (1 - e) g <c, w>) = 2 c (x)_s w - e g <c, w> with m = 2/(D - 2) = %s"
            % (Dm, mv), (GC - want).applyfunc(sp.simplify) == sp.zeros(N, N))
    msol = sp.solve(sp.Eq(-1 + m*(1 - e)*(sp.Rational(5, 2) - 1), -e), m)
    chk("D = 5: the coefficient -1 + m (1 - e)(D/2 - 1) equals -e for every e iff m = 2/3", msol == [sp.Rational(2, 3)])
    return chk.ok


# ------------------------------------------------------------------------------------------------- U3
def u3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    pk, p0, pv = polys(4, sp.Rational(2, 3))
    chk("n = 4: p_v = -h lam^2 + (2h - 2v) lam + h kappa + 6v",
        sp.simplify(pv - (-h*lam**2 + (2*h - 2*v)*lam + h*K + 6*v)) == 0)
    ex = 1 if control == 1 else 2
    chk("n = 4: lam = %d is a root of scalar types 0 and 1 for all (v, e, h)" % ex,
        sp.simplify(p0.subs(lam, ex)) == 0 and sp.simplify(pk.subs({K: 3, lam: ex})) == 0)
    chk("n = 4: it is simple at the parameters of U4 (the cofactors do not vanish there)",
        sp.cancel(p0/(lam - 2)).subs(PARAMS).subs(lam, 2) != 0
        and sp.cancel(pk.subs(K, 3)/(lam - 2)).subs(PARAMS).subs(lam, 2) != 0)
    Q5 = e*((v**2 - 1)*K + (1 + v**2)*(lam - 3)*(lam + 1)) - 2*v**2*(lam - 2)*(lam - 3)
    chk("n = 4: at h = 0 the sextic is 8 v (lam - 2) Q_5, and -16 v^3 (lam - 3)(lam - 2)^2 at e = 0",
        sp.expand(pk.subs(h, 0) - 8*v*(lam - 2)*Q5) == 0
        and sp.expand(pk.subs({h: 0, e: 0}) + 16*v**3*(lam - 3)*(lam - 2)**2) == 0)
    pk4, p04, pv4 = polys(3, 1)
    Q4 = e*((v**2 - 1)*K + (1 + v**2)*(lam - 2)*(lam + 1)) - 2*v**2*(lam - 1)*(lam - 2)
    chk("n = 3 (his): 8 v (lam - 1) Q_4 and -16 v^3 (lam - 2)(lam - 1)^2",
        sp.expand(pk4.subs(h, 0) - 8*v*(lam - 1)*Q4) == 0
        and sp.expand(pk4.subs({h: 0, e: 0}) + 16*v**3*(lam - 2)*(lam - 1)**2) == 0)
    neg = (2*v*lt + 1)*(4*e*(1 + v**2)*lt**2 + 2*e*v*lt - 8*v**2*lt**2 - 6*v*lt - 1)
    ok = True
    for p in (pk, pk4):
        q = sp.expand(sp.expand(p.subs(lam, 1/(h*lt))*h**3*lt**6))
        ok &= sp.expand(q.subs(h, 0) - neg) == 0
    chk("the very negative roots lam = (h lt)^-1: the same h = 0 limit in four and five dimensions", ok)
    return chk.ok


# ------------------------------------------------------------------------------------------------- U4
def hurwitz_det(cs, k):
    nn = len(cs) - 1
    a = lambda i: cs[i] if 0 <= i <= nn else 0                                               # noqa: E731
    return sp.Matrix(k, k, lambda i, j: a(2*j - i + 1)).det(method="berkowitz")


def routh_rhp(cs):
    nn = len(cs) - 1
    if cs[0] < 0:
        cs = [-c for c in cs]
    r1, r2 = list(cs[0::2]), list(cs[1::2])
    rows = [r1, r2 + [0]*(len(r1) - len(r2))]
    for _ in range(nn - 1):
        a, b = rows[-2], rows[-1]
        assert b[0] != 0, "singular Routh array"
        rows.append([(b[0]*a[i + 1] - a[0]*b[i + 1])/b[0] for i in range(len(a) - 1)] + [0])
    col = [rw[0] for rw in rows[:nn + 1]]
    return sum(1 for i in range(nn) if col[i]*col[i + 1] < 0)


def right_of(P, x):
    return routh_rhp(sp.Poly(sp.expand(P.subs(lam, x + mu_)), mu_).all_coeffs())


def no_crossing(P, x, kmin):
    cs = sp.Poly(sp.expand(P.subs(lam, x + mu_)), mu_).all_coeffs()
    ok = True
    for poly in (sp.Poly(sp.expand(cs[-1]), K), sp.Poly(sp.expand(hurwitz_det(cs, len(cs) - 2)), K)):
        ok &= (poly.as_expr() != 0) if poly.degree() <= 0 else (poly.count_roots(kmin, None) == 0)
    return ok


def certificate(n, mv, x1):
    pk, p0, pv = polys(n, mv)
    pk, p0, pv = (p.subs(PARAMS) for p in (pk, p0, pv))
    kmin = n - 1
    res = {}
    for nm, P in (("sl", pk), ("vl", pv)):
        P1 = P.subs(K, kmin)
        deg = sp.Poly(P1, lam).degree()
        rgt, lft = right_of(P1, x1), deg - right_of(P1, -C0)
        res[nm] = (no_crossing(P, -C0, kmin) and no_crossing(P, x1, kmin), rgt, deg - rgt - lft, lft)
    deg = sp.Poly(p0, lam).degree()
    rgt, lft = right_of(p0, x1), deg - right_of(p0, -C0)
    res["s0"] = (True, rgt, deg - rgt - lft, lft)
    return res


def coulomb(n, mv):
    """The strip [-C0, n - 2]: lines crossed or not, then counts (right | between | left) at l = 2, at l = 1 and l = 0
    on the cofactors of lam - (n - 2), and for the vector type at l = 1; and whether lam = n - 2 is simple."""
    pk, p0, pv = (p.subs(PARAMS) for p in polys(n, mv))
    ex, k1, k2 = n - 2, n - 1, 2*n                                       # kappa = l (l + n - 2) at l = 1, 2

    def counts(P):
        deg = sp.Poly(P, lam).degree()
        rgt, lft = right_of(P, ex), deg - right_of(P, -C0)
        return (rgt, deg - rgt - lft, lft)
    q1, q0 = sp.cancel(pk.subs(K, k1)/(lam - ex)), sp.cancel(p0/(lam - ex))
    cross = (no_crossing(pk, ex, k2) and no_crossing(pk, -C0, k1) and no_crossing(pv, ex, k1)
             and no_crossing(pv, -C0, k1))
    return (cross, counts(pk.subs(K, k2)), counts(q1), counts(q0), counts(pv.subs(K, k1)),
            q1.subs(lam, ex) != 0 and q0.subs(lam, ex) != 0)


def u4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    x1 = sp.Rational(21, 10) if control == 1 else sp.Rational(19, 10)
    res = certificate(4, sp.Rational(2, 3), x1)
    chk("n = 4, weight 2/3, (v, e, h) = (1/2, 1/100, 1/1000): no crossing of Re lam = -100 or %s for kappa >= 3 (scalar,"
        " vector)" % x1, res["sl"][0] and res["vl"][0])
    chk("at l = 1 the counts (right of %s | between | left of -100) are 3 | 0 | 3 and 1 | 0 | 1; scalar type 0: "
        "2 | 0 | 2" % x1, res["sl"][1:] == (3, 0, 3) and res["vl"][1:] == (1, 0, 1) and res["s0"][1:] == (2, 0, 2))
    if control != 0:
        return chk.ok
    want = (True, (3, 0, 3), (2, 0, 3), (1, 0, 2), (1, 0, 1), True)
    chk("up to the Coulomb root: in [-100, 2] the only roots are lam = 2 at l = 0, 1, simple (line 2 not crossed for "
        "kappa >= 8; 3 | 0 | 3 at l = 2, the cofactors 2 | 0 | 3 at l = 1 and 1 | 0 | 2 at l = 0, vector 1 | 0 | 1)",
        coulomb(4, sp.Rational(2, 3)) == want)
    res4 = certificate(3, 1, sp.Rational(9, 10))
    chk("n = 3 (his Theorem 4.9 at these parameters): the same at the lines 9/10 and 1",
        all(res4[k][0] for k in res4) and res4["sl"][1:] == (3, 0, 3) and res4["vl"][1:] == (1, 0, 1)
        and res4["s0"][1:] == (2, 0, 2) and coulomb(3, 1) == want)
    return chk.ok


# ------------------------------------------------------------------------------------------------- U5
def u5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    mv = sp.Rational(2, 3) if control == 1 else 1
    pk, p0, pv = polys(4, mv)
    cub0 = sp.cancel(p0/(lam - 2)).subs(h, 0)
    root = sp.solve(cub0, lam)
    want = (7*v**2 - 1 + 3*e*(1 + v**2))/(5*v**2 + 1 - 3*e*(1 + v**2))
    if control == 0:
        chk("weight 1, n = 4: the scalar type 0 cubic at h = 0 has the root (7 v^2 - 1 + 3e (1 + v^2))/(5 v^2 + 1 "
            "- 3e (1 + v^2))", len(root) == 1 and sp.simplify(root[0] - want) == 0)
        w0 = want.subs(e, 0)
        chk("at e = 0 it is (7 v^2 - 1)/(5 v^2 + 1), in (-1, 1) for v in (0, 1)",
            sp.simplify(1 - w0 - 2*(1 - v**2)/(5*v**2 + 1)) == 0 and sp.simplify(w0 + 1 - 12*v**2/(5*v**2 + 1)) == 0)
    P0 = sp.Poly(p0.subs(PARAMS), lam)
    chk("at the parameters of U4 the scalar type 0 quartic has a real root in (0, 1), inside [-C_0, 1)",
        P0.count_roots(0, 1) >= 1)
    res = certificate(4, mv, sp.Rational(19, 10))
    chk("and the scalar type 1 sextic a root in the strip [-100, 19/10]", res["sl"][2] >= 1)
    return chk.ok


# ------------------------------------------------------------------------------------------------- U6
def scan(eps, hs, lmax_exp=6.3):
    pk, p0, pv = polys(4, sp.Rational(2, 3))
    co = [sp.lambdify((e, v, h, K), c, "mpmath") for c in sp.Poly(pk, lam).all_coeffs()]
    mpm.mp.dps = 50
    out = {}
    ls = list(range(1, 60)) + sorted({int(10**(k/6)) for k in range(11, int(6*lmax_exp))})
    for ev in eps:
        for hv in hs:
            E, H, V = mpm.mpf(ev), mpm.mpf(hv), mpm.mpf(1)/2
            up, lo, exc = mpm.inf, -mpm.inf, False
            for lv in ls:
                rs = mpm.polyroots([c(E, V, H, lv*(lv + 2)) for c in co], maxsteps=400, extraprec=200)
                for z in rs:
                    if lv == 1 and not exc and abs(z - 2) < mpm.mpf(10)**-30:
                        exc = True                    # the exceptional root lam = 2 at l = 1 (U3), set aside
                    elif mpm.re(z) > -1:
                        up = min(up, mpm.re(z))
                    else:
                        lo = max(lo, mpm.re(z))
            out[(ev, hv)] = (float(up), float(lo), exc)
    return out


def u6(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    eps, hs = ["0.01", "0.001", "0.0001"], ["0.01", "0.001", "0.0001"]
    if control == 1:
        hs = ["0.3"]
    res = scan(eps, hs)
    if verbose:
        for k, (up, lo, exc) in res.items():
            print("        e = %s, h = %s: the other upper roots >= %.4f, lower roots <= %.1f" % (k[0], k[1], up, lo))
    chk("lam = 2 is a root at l = 1 at every (e, h) of the grid (to 10^-30)", all(x[2] for x in res.values()))
    chk("the other upper roots stay above 1.93 and the lower below -95 at every (e, h) of the grid, l <= 1.5 10^6",
        all(up > 1.93 and lo < -95 for up, lo, _ in res.values()))
    if control == 0:
        chk("the other upper roots are above 2 where h <= e (six points) and below 2 where h > e (three)",
            all((res[(ev, hv)][0] > 2) == (float(hv) <= float(ev)) for ev, hv in res))
    return chk.ok


CHECKS = [("U1 the indicial families from the definition; four-dimensional control: [Hin26a] (4.19), (A.2), p_s0, "
           "(A.13)", u1, 1),
          ("U2 the weight: G C has his form, the symbol l_{g,c,e}, iff m = 2/(D - 2) (1 in four dimensions, 2/3 in "
           "five)", u2, 1),
          ("U3 the five-dimensional polynomials: lam = 2 exceptional; h = 0 roots 2, 2, 3; the negative roots as his",
           u3, 1),
          ("U4 the certificate: at (1/2, 1/100, 1/1000) no indicial root in [-100, 2), any l; his in [-100, 1)", u4, 1),
          ("U5 his weight 1 transcribed literally fails in five dimensions: a root in (0, 1)", u5, 1),
          ("U6 the configuration over a grid of (e, h), l <= 1.5 10^6 (numerical)", u6, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<112} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"damping5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"damping5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest("--verbose" in sys.argv) else 1)
