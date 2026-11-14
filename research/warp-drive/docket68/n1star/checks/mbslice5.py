#!/usr/bin/env python3
"""mbslice5: Theorem T (iii) and Lemma X1 of FAMILIES5-MB.md on every class slice, as exact polynomial identities
(FAMILIES5-MB.md section 2, minor 1 of its round-8 review; mbsign5 E2-E3 check them at three slice points only); and
[R10] mbsign5 E4 (a), (c) and qsign5 Q1 by the same route, for every (R, theta, mu) and every background.

The slices. A class slice of Tangherlini in ingoing coordinates is v = V(R) with w := V' > 0 and f w < 2 (spacelike),
f = 1 - mu/R^2. Every such slice is w = 2/(f + q^2) with q := sqrt(2/w - f) > 0, and then sqrt(gamma_RR) =
sqrt(w (2 - f w)) = 2 q/(f + q^2) (the parametrisation of the round-8 reader of FAMILIES5-MB). With
S := R^2 - mu + R^2 q^2 every slice quantity is a polynomial over a monomial R^a q^b S^c:
    w = 2 R^2/S,  sqrt(gamma_RR) = 2 q R^2/S,  gamma_RR = 4 q^2 R^4/S^2,  N_s = S/(2 q R^2),
    Y_s^R = (R^2 q^2 - R^2 + mu) S/(4 q^2 R^4),  n^R = -(R^2 q^2 - R^2 + mu)/(2 q R^2),
    K_RR = (R^5 w' - R^2 mu w^3 + 3 R^2 mu w^2 + mu^2 w^3)/(R^5 sqrt(gamma_RR))   (mbsign5 E2's closed form),
and R-derivatives are total derivatives in the jets q, q', q'', ... (and S' = 2R + 2R q^2 + 2R^2 q q' is a polynomial).

The route (exact; no simplification, no gcd). Every quantity is held as (numerator, a, b, c), the numerator a
polynomial with rational coefficients in R, mu, the jets of q and the jets of H and P (sympy's sparse polynomial
ring), the denominator R^a q^b S^c. Sums bring both to the larger exponents, products add them, the total derivative
is D(p/(R^a q^b S^c)) = (R q S D p - p (a q S + b R q' S + c R q S'))/(R^(a+1) q^(b+1) S^(c+1)), and only quantities
whose numerator is a constant times a monomial in R, q (times a power of S) are inverted. A rational function of this
form is identically zero iff its numerator polynomial is the zero polynomial, which is read off exactly. The
theta-integrated Q-density of tensor data on an abstract round slice is mbsign5's own (its constraint map, qsign5's
constraints_fast, and its theta integral; mbsign5 is imported, not modified); every abstract slice function and
derivative in it is replaced by the exact quantity above, symbol by symbol.

  S1 Theorem T (iii) on every class slice, l = 2, 4, 6 and 8 [R10: 6 and 8 added]: the Euler operator in H and in P
     of (theta-integrated Q-density) + 2 |T|^2 T_m(xi, n) sqrt(gamma_RR) is the zero rational function of (R, mu, q,
     q', ...): the Q-density is -2 |T|^2 T_m sqrt(gamma_RR) up to a d/dR, on every slice and every mu. And the
     theta-integrated density over |T|^2 at l = 6 and 8 is, pointwise, the affine interpolant in k_T^2 of l = 2 and 4
     (FAMILIES5-MB.md minor 8 deduces this for every l; k_T^2 is not carried as a free symbol here, since the theta
     integral is taken harmonic by harmonic, so "every l" stays deduced and is checked at two more l).
  S2 Lemma X1 on every class slice, l = 2, 4, 6 and 8 [R10: 4, 6, 8 added]: with P = -(Y_s^R/N_s) H_R the Q-density
     plus |T|^2 (R^3 f H_R^2 + (k_T^2 + 2) R H^2) has zero Euler operator in H; with H = 0 it equals -|T|^2 R^3 P^2
     pointwise.
  S3 the slice identities N_s sqrt(gamma_RR) = 1 and N_s^2 - gamma_RR (Y_s^R)^2 = f, exactly in this representation.
  S4 [R10, R11] mbsign5 E4 (a), (b) and (c) on the static slice for every (R, theta, mu), not at three points: mu = R^2
     (1 - nu^2) (so sqrt f = nu, R and nu free), theta by t = tan(theta/2), and every quantity a polynomial over a
     product of powers of the atoms R, t, 1 - t, 1 + t, 1 + t^2, nu (the same route with more atoms; an inverse is taken
     only of a constant times a product of atoms). (a) after Delta S = -k^2 S the constraints and energies have the
     stated (S, S') structure and every coefficient has t-derivative zero, and they equal exactly the radial
     coefficients mbsign5 E5-E9 use; [R11] (b) the shifts of (a, b, c, e) under L_X gamma and the lapse direction's
     trace-free angular part, every component; (c) D R[L_X gamma] = 0, (D R)^* N = 0 in all five class components,
     M[k_psi] = 0 and the Euler identity for B, for class fields of (R, theta) with every jet free.
  S5 [R10] qsign5 Q1 for every background and every (R, theta), not at three points: G = g^2 with g, kappa0, Y0, nu
     arbitrary positive functions and E = e^(Ia) a free symbol (its derivatives through Ia' = (3c - 1)/R); the seed
     solves the linearised H, M_R, M_th identically and the Euler operator of (Q-density - decomposition) in psi and
     s1 is the zero rational function, atoms R, t, 1 - t, 1 + t, 1 + t^2, E, g, Y0.
  Controls (each must fail, i.e. give a nonzero polynomial): S1 with |T|^2 halved (l = 2..8); S1 with K_RR's w' term
  dropped (a wrong slice); S2 with k_T^2 + 2 replaced by k_T^2 + 3, and with R^3 P^2 doubled (every l); S4 the lapse
  direction without its curvature term, [R11-nits] the vector field X = alpha S d_R + beta S d_th, the lapse psi S', and
  the eigen-relation's cot th - tan th -> cot th (which the theta-freeness test must reject); S5 with 4 nu E^2 -> 3 nu
  E^2 in Gamma.

Labels: computed, exact (polynomial identities over the rationals). Run: python3 checks/mbslice5.py   (a few minutes)
"""
import importlib.util
import os
import sys
import time

import sympy as sp
from sympy import QQ
from sympy.calculus.euler import euler_equations
from sympy.polys.rings import ring

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
T0 = time.time()
NJ = 14                                                          # jets kept for q, H and P


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec)
    sys.argv = sys.argv[:1]                                      # mbsign5 reads its flags from argv at import
    spec.loader.exec_module(m)
    return m


MB = load('mbsign5')
NAMES = ['R', 'mu'] + ['q%d' % k for k in range(NJ)] + ['H%d' % k for k in range(NJ)] + ['P%d' % k for k in range(NJ)]
RING, *GENS = ring(','.join(NAMES), QQ)
RR, MU = GENS[0], GENS[1]
QJ = GENS[2:2 + NJ]
HJ = GENS[2 + NJ:2 + 2 * NJ]
PJ = GENS[2 + 2 * NJ:2 + 3 * NJ]
SS = RR**2 - MU + RR**2 * QJ[0]**2
_SP = [RING(1)]


def spow(k):
    while len(_SP) <= k:
        _SP.append(_SP[-1] * SS)
    return _SP[k]


def Dpoly(p):
    """the total derivative in R of a polynomial in R, mu and the jets"""
    out = p.diff(RR)
    for J in (QJ, HJ, PJ):
        if p.diff(J[-1]) != 0:
            raise RuntimeError("jet order exceeded")
        for k in range(NJ - 1):
            dk = p.diff(J[k])
            if dk:
                out += J[k + 1] * dk
    return out


class RF:
    """num / (R^a q^b S^c)"""
    __slots__ = ('n', 'a', 'b', 'c')

    def __init__(self, n, a=0, b=0, c=0):
        self.n, self.a, self.b, self.c = RING(n), a, b, c

    def lift(self, a, b, c):
        return self.n * RR**(a - self.a) * QJ[0]**(b - self.b) * spow(c - self.c)

    def __add__(self, o):
        o = o if isinstance(o, RF) else RF(o)
        a, b, c = max(self.a, o.a), max(self.b, o.b), max(self.c, o.c)
        return RF(self.lift(a, b, c) + o.lift(a, b, c), a, b, c)
    __radd__ = __add__

    def __neg__(self):
        return RF(-self.n, self.a, self.b, self.c)

    def __sub__(self, o):
        return self + (-(o if isinstance(o, RF) else RF(o)))

    def __rsub__(self, o):
        return RF(o) - self

    def __mul__(self, o):
        o = o if isinstance(o, RF) else RF(o)
        return RF(self.n * o.n, self.a + o.a, self.b + o.b, self.c + o.c)
    __rmul__ = __mul__

    def inv(self):
        n = self.n
        for k in range(8):
            try:
                m = n.exquo(spow(k))
            except Exception:
                break                                            # not divisible by S^k, so not by S^(k+1)
            if len(m) == 1:
                (mon, cf), = m.terms()
                if all(e == 0 for i, e in enumerate(mon) if i not in (0, 2)):
                    ea, eb = mon[0], mon[2]
                    return RF(RING(1 / cf) * RR**self.a * QJ[0]**self.b * spow(self.c), ea, eb, k)
        raise ValueError("not invertible in this representation")

    def __pow__(self, k):
        if k < 0:
            return self.inv()**(-k)
        out = RF(1)
        for _ in range(k):
            out = out * self
        return out

    def D(self):
        n, a, b, c = self.n, self.a, self.b, self.c
        q0, q1 = QJ[0], QJ[1]
        num = RR * q0 * SS * Dpoly(n) - n * (a * q0 * SS + b * RR * q1 * SS + c * RR * q0 * Dpoly(SS))
        return RF(num, a + 1, b + 1, c + 1)

    def diff(self, g):
        return RF(self.n.diff(g), self.a, self.b, self.c)

    def iszero(self):
        return self.n == 0


# ------------------------------------------------------------------ the slice, exactly
def slice_quantities(drop_wprime=False):
    f = RF(RR**2 - MU, 2)
    w = RF(2 * RR**2, 0, 0, 1)
    ssq = RF(2 * QJ[0] * RR**2, 0, 0, 1)                         # sqrt(gamma_RR)
    G = ssq * ssq
    N = RF(SS * QQ(1, 2), 2, 1, 0)
    Y = RF((RR**2 * QJ[0]**2 - RR**2 + MU) * SS * QQ(1, 4), 4, 2, 0)
    nR = RF(-(RR**2 * QJ[0]**2 - RR**2 + MU) * QQ(1, 2), 2, 1, 0)
    R5 = RF(RR**5)
    mu = RF(MU)
    wp = RF(0) if drop_wprime else w.D()
    K = (R5 * wp - RF(RR**2) * mu * w**3 + RF(3 * RR**2) * mu * w**2 + mu * mu * w**3) * (R5 * ssq).inv()
    return dict(f=f, w=w, ss=ssq, G=G, N=N, Y=Y, n=nR, K=K)


def jets_of(x, k):
    out = [x]
    for _ in range(k):
        out.append(out[-1].D())
    return out


class Converter:
    """a sympy expression in R, mu, the abstract slice functions Gf, Kf, nf, Nf, Yf (and sqrt(Gf)), H and P with
    their R-derivatives, and rational numbers -> RF, symbol by symbol"""

    def __init__(self, F, sq, order=8):
        Gf, Kf, nf, Nf, Yf, H, P = F
        self.Rsym = MB.R_
        self.Gf, self.H, self.P = Gf, H, P
        self.jets = {Gf: jets_of(sq['G'], order), Kf: jets_of(sq['K'], order), nf: jets_of(sq['n'], order),
                     Nf: jets_of(sq['N'], order), Yf: jets_of(sq['Y'], order)}
        self.ssj = sq['ss']
        self.memo = {}

    def __call__(self, e):
        if e in self.memo:
            return self.memo[e]
        out = self._conv(e)
        self.memo[e] = out
        return out

    def _conv(self, e):
        if e.is_Rational:
            return RF(QQ(int(e.p), int(e.q)))
        if e == self.Rsym:
            return RF(RR)
        if e == MB.mu:
            return RF(MU)
        if e in self.jets:
            return self.jets[e][0]
        if e == self.H:
            return RF(HJ[0])
        if e == self.P:
            return RF(PJ[0])
        if isinstance(e, sp.Derivative):
            fn = e.expr
            k = sum(c for v, c in e.variable_count)
            if fn in self.jets:
                return self.jets[fn][k]
            if fn == self.H:
                return RF(HJ[k])
            if fn == self.P:
                return RF(PJ[k])
            raise ValueError("unknown derivative %s" % e)
        if e.is_Add:
            out = RF(0)
            for t in e.args:
                out = out + self(t)
            return out
        if e.is_Mul:
            out = RF(1)
            for t in e.args:
                out = out * self(t)
            return out
        if e.is_Pow:
            base, ex = e.args
            if base == self.Gf and ex.is_Rational and ex.q == 2:
                return self.ssj**int(ex.p)
            if ex.is_Integer:
                return self(base)**int(ex)
            raise ValueError("power %s" % e)
        raise ValueError("unknown atom %s" % e)


def euler(L, J):
    """the Euler operator of the RF L in the field whose jets are J"""
    out = RF(0)
    for k in range(NJ - 1):
        dk = L.diff(J[k])
        if dk.iszero():
            continue
        t = dk
        for _ in range(k):
            t = t.D()
        out = out + (t if k % 2 == 0 else -t)
    return out


# ------------------------------------------------------------------ the general route: denominators over named atoms
class GField:
    """a sparse polynomial ring over QQ and a list of 'atom' polynomials; an element is num / prod atom_j^e_j"""

    def __init__(self, names, atoms):
        self.ring, *gens = ring(','.join(names), QQ)
        self.g = dict(zip(names, gens))
        self.atoms = [a(self.g) if callable(a) else a for a in atoms]
        self._pw = [[self.ring(1)] for _ in self.atoms]

    def apow(self, j, k):
        L = self._pw[j]
        while len(L) <= k:
            L.append(L[-1] * self.atoms[j])
        return L[k]

    def el(self, num, e=None):
        return GE(self, self.ring(num), tuple(e) if e else (0,) * len(self.atoms))


class GE:
    __slots__ = ('F', 'n', 'e')

    def __init__(self, F, n, e):
        self.F, self.n, self.e = F, n, e

    def _c(self, o):
        return o if isinstance(o, GE) else self.F.el(o)

    def __add__(self, o):
        o = self._c(o)
        e = tuple(max(x, y) for x, y in zip(self.e, o.e))
        a, b = self.n, o.n
        for j, (x, y, z) in enumerate(zip(self.e, o.e, e)):
            if z > x:
                a = a * self.F.apow(j, z - x)
            if z > y:
                b = b * self.F.apow(j, z - y)
        return GE(self.F, a + b, e)
    __radd__ = __add__

    def __neg__(self):
        return GE(self.F, -self.n, self.e)

    def __sub__(self, o):
        return self + (-self._c(o))

    def __mul__(self, o):
        o = self._c(o)
        return GE(self.F, self.n * o.n, tuple(x + y for x, y in zip(self.e, o.e)))
    __rmul__ = __mul__

    def inv(self):
        n, ks = self.n, [0] * len(self.F.atoms)
        for j, a in enumerate(self.F.atoms):
            while True:
                try:
                    q = n.exquo(a)
                except Exception:
                    break
                n, ks[j] = q, ks[j] + 1
        if n == 0 or not n.is_ground:
            raise ValueError("not a product of atoms: cannot invert")
        num = self.F.ring(1 / n.LC)
        for j, x in enumerate(self.e):
            if x:
                num = num * self.F.apow(j, x)
        return GE(self.F, num, tuple(ks))

    def __pow__(self, k):
        if k < 0:
            return self.inv()**(-k)
        out = self.F.el(1)
        for _ in range(k):
            out = out * self
        return out

    def diff(self, g):
        """the partial derivative in the generator g"""
        js = [j for j, x in enumerate(self.e) if x]
        A = self.F.ring(1)
        for j in js:
            A = A * self.F.atoms[j]
        num = self.n.diff(g) * A
        for j in js:
            num = num - self.n * self.e[j] * self.F.atoms[j].diff(g) * A.exquo(self.F.atoms[j])
        return GE(self.F, num, tuple(x + 1 if x else 0 for x in self.e))

    def iszero(self):
        return self.n == 0


TRIG_ATOMS = [lambda g: g['t'], lambda g: 1 - g['t'], lambda g: 1 + g['t'], lambda g: 1 + g['t']**2]


def convert(e, F, table, th):
    """a sympy expression -> GE; table maps sympy atoms (symbols, functions, derivatives, exp(...)) to GE; sin th,
    cos th, tan th, cot th by t = tan(th/2); rational numbers; sums, products, integer powers"""
    t = F.el(F.g['t'])
    one = F.el(1)
    sin_ = F.el(2 * F.g['t']) * (one + t * t).inv()
    cos_ = (one - t * t) * (one + t * t).inv()
    memo = {}

    def cv(x):
        if x in memo:
            return memo[x]
        if x in table:
            out = table[x]
        elif x.is_Rational:
            out = F.el(QQ(int(x.p), int(x.q)))
        elif x == sp.sin(th):
            out = sin_
        elif x == sp.cos(th):
            out = cos_
        elif x == sp.tan(th):
            out = sin_ * cos_.inv()
        elif x == sp.cot(th):
            out = cos_ * sin_.inv()
        elif isinstance(x, (sp.sin, sp.cos, sp.tan, sp.cot)) and (x.args[0] / th).is_Integer:
            out = cv(sp.expand_trig(x))                               # multiple angles, e.g. sin 2th = 2 sin cos
        elif x.is_Add:
            out = F.el(0)
            for a in x.args:
                out = out + cv(a)
        elif x.is_Mul:
            out = F.el(1)
            for a in x.args:
                out = out * cv(a)
        elif x.is_Pow and x.args[1].is_Integer:
            out = cv(x.args[0])**int(x.args[1])
        else:
            raise ValueError("unknown atom %s" % x)
        memo[x] = out
        return out
    return cv(e)


def jet_names(exprs, fns):
    """the derivative and function atoms of fns in exprs, with generator names"""
    out = {}
    for e in exprs:
        for d in e.atoms(sp.Derivative):
            if d.expr in fns:
                nm = '%s_%s' % (d.expr.func.__name__, '_'.join('%s%d' % (str(v)[0], c) for v, c in d.variable_count))
                out[d] = nm
        for fn in fns:
            if e.has(fn):
                out[fn] = '%s_0' % fn.func.__name__
    return out


# ------------------------------------------------------------------ S4: mbsign5 E4 (a), (c) exactly
def s4():
    print("S4 mbsign5 E4 (a) and (c) exactly, on the static slice, every (R, theta, mu) (mu = R^2 (1 - nu^2), "
          "sqrt f = nu; theta by t = tan(theta/2))", flush=True)
    t0 = time.time()
    r, th, k2 = MB.r, MB.th, MB.k2
    nu = sp.Symbol('nu', positive=True)
    musub = {MB.mu: r**2 * (1 - nu**2)}

    def pre(e):
        e = sp.sympify(e).subs(musub)
        return e.replace(lambda x: x.is_Pow and x.exp.is_Rational and x.exp.q == 2,
                         lambda x: sp.Pow(sp.factor(x.base), x.exp))          # sqrt(R^2 nu^2) = R nu (R, nu > 0)
    names = ['A', 'F', 'p', 'q', 'w']
    fns = [sp.Function(nm)(r) for nm in names]
    A, Fq, p, q, w = fns
    SF, GHAT, G0, X4, eps = MB.SF, MB.GHAT, MB.G0, MB.X4, MB.eps
    gh = sp.diag(1, 0, 0, 0) * A * SF + 2 * Fq * SF * r**2 * GHAT
    kk = sp.zeros(4, 4)
    kk[0, 0] = p * SF
    kk[0, 1] = kk[1, 0] = r * q * sp.diff(SF, th)
    kk += r**2 * w * SF * GHAT
    Hc, _ = MB.QS.constraints_fast(G0 + eps * gh, sp.zeros(4, 4), X4)
    R1 = sp.diff(Hc, eps).subs(eps, 0)
    R2 = sp.diff(Hc, eps, 2).subs(eps, 0)
    Hk, Mk = MB.QS.constraints_fast(G0, eps * kk, X4)
    MK = [sp.diff(x, eps).subs(eps, 0) for x in Mk]
    HK2 = sp.diff(Hk, eps, 2).subs(eps, 0)
    N = sp.sqrt(MB.f_)
    exprs = {'C': R1, 'M_R': MK[0], 'M_th': MK[1], 'M_phi1': MK[2], 'M_phi2': MK[3], 'E_V': -N * R2 / 2,
             'E_K': -N * HK2 / 2}
    shape_want = {'C': {(1, 0)}, 'M_R': {(1, 0)}, 'M_th': {(0, 1)}, 'M_phi1': set(), 'M_phi2': set(),
                  'E_V': {(2, 0), (0, 2)}, 'E_K': {(2, 0), (0, 2)}}
    # the eigen-relation, as mbsign5's eig_point imposes it, with theta kept symbolic
    c_, s_ = MB.c_, MB.s_

    def eig_rel(ct):
        S2 = -k2 * SF - ct * sp.diff(SF, th)
        S3 = sp.diff(S2, th).subs(sp.Derivative(SF, (th, 2)), S2)
        return S2, S3, sp.diff(S3, th).subs(sp.Derivative(SF, (th, 2)), S2)
    REL = eig_rel(c_ / s_ - s_ / c_)

    def eig(e, rel=REL, fs_=None):
        S2, S3, S4_ = rel
        e = e.subs(sp.Derivative(SF, (th, 4)), S4_).subs(sp.Derivative(SF, (th, 3)), S3)
        e = e.subs(sp.Derivative(SF, (th, 2)), S2).subs(sp.Derivative(SF, th), MB.s1).subs(SF, MB.s0)
        return pre(MB.JR.from_funcs(e, fs_ or fns))
    names_b = ['al', 'be', 'ps']
    fns_b = [sp.Function(nm)(r) for nm in names_b]
    jets = [x for nm in names + names_b for x in MB.JR.J[nm]]
    gnames = ['r', 't', 'nu', 'k2', 's0', 's1'] + [str(x) for x in jets]
    F = GField(gnames, [lambda g: g['r']] + TRIG_ATOMS + [lambda g: g['nu']])
    table = {r: F.el(F.g['r']), nu: F.el(F.g['nu']), k2: F.el(F.g['k2']), MB.s0: F.el(F.g['s0']),
             MB.s1: F.el(F.g['s1'])}
    table.update({x: F.el(F.g[str(x)]) for x in jets})
    i0, i1 = F.ring.gens.index(F.g['s0']), F.ring.gens.index(F.g['s1'])
    shape_ok, free_ok, rad_ok = True, True, True
    coef = {}
    for nm, e in exprs.items():
        G = convert(eig(e), F, table, th)
        parts = {}
        for mon, cf in G.n.terms():
            key = (mon[i0], mon[i1])
            m2 = list(mon)
            m2[i0] = m2[i1] = 0
            parts[key] = parts.get(key, F.ring(0)) + F.ring({tuple(m2): cf})
        parts = {kk_: GE(F, v, G.e) for kk_, v in parts.items() if v != 0}
        shape_ok &= set(parts) <= shape_want[nm]
        for v in parts.values():
            free_ok &= v.diff(F.g['t']).iszero()
        coef[nm] = parts
    # the radial coefficients E5-E9 use (mbsign5's angular_reduce at its first rational angle) are these, exactly
    vol = F.el(F.g['r'])**3 * F.el(F.g['nu']).inv()
    k2e = F.el(F.g['k2'])
    z0 = F.el(0)
    rad_mine = {'C': coef['C'].get((1, 0), z0), 'M0': coef['M_R'].get((1, 0), z0),
                'M1': coef['M_th'].get((0, 1), z0),
                'EV': vol * (coef['E_V'].get((2, 0), z0) + k2e * coef['E_V'].get((0, 2), z0)),
                'EK': vol * (coef['E_K'].get((2, 0), z0) + k2e * coef['E_K'].get((0, 2), z0))}
    ref = {'C': MB.angular_reduce(R1, fns, 'C')[0].get((1, 0), 0),
           'M0': MB.angular_reduce(MK[0], fns, 'M_R')[0].get((1, 0), 0),
           'M1': MB.angular_reduce(MK[1], fns, 'M_th')[0].get((0, 1), 0)}
    rV = MB.angular_reduce(-N * R2 / 2, fns, 'E_V')[0]
    rK = MB.angular_reduce(-N * HK2 / 2, fns, 'E_K')[0]
    vols = r**3 / sp.sqrt(MB.f_)
    ref['EV'] = sp.expand(vols * (rV.get((2, 0), 0) + k2 * rV.get((0, 2), 0)))
    ref['EK'] = sp.expand(vols * (rK.get((2, 0), 0) + k2 * rK.get((0, 2), 0)))
    for kk_, v in ref.items():
        rad_ok &= (rad_mine[kk_] - convert(pre(v), F, table, th)).iszero()
    print("   (a) C ~ S, M_R ~ S, M_th ~ S', M_phi = 0, E_V and E_K ~ S^2, S'^2: %s; every coefficient free of theta "
          "(its t-derivative the zero rational function): %s; the radial coefficients mbsign5 E5-E9 use are these "
          "exactly: %s (%.0f s)" % (shape_ok, free_ok, rad_ok, time.time() - t0), flush=True)
    # [R11] control on the theta-freeness test itself: the eigen-relation with cot th - tan th -> cot th (not the
    # class Laplacian) leaves theta-dependent coefficients, which the test must find
    REL_bad = eig_rel(c_ / s_)
    free_bad = True
    for nm in ('C', 'E_V'):                                       # the ones in which S'' enters
        Gb = convert(eig(exprs[nm], REL_bad), F, table, th)
        pb = {}
        for mon, cf in Gb.n.terms():
            key = (mon[i0], mon[i1])
            m2 = list(mon)
            m2[i0] = m2[i1] = 0
            pb[key] = pb.get(key, F.ring(0)) + F.ring({tuple(m2): cf})
        free_bad &= all(GE(F, v, Gb.e).diff(F.g['t']).iszero() for v in pb.values()
                        if v != 0)
    print("   control on the theta-freeness test: with cot th - tan th -> cot th in the eigen-relation, the "
          "coefficients of C and E_V depend on theta (rejected): %s" % (not free_bad), flush=True)
    # [R11] (b) exactly: the gauge maps L_X gamma (X = alpha S d_R + beta S' d_th) and the lapse direction's trace-free
    # angular part, every (R, theta, mu) (mbsign5 E4 (b) checks them at three rational angles)
    al, be, ps_ = fns_b
    gi, Gm = MB.christoffel(G0, X4)
    Ric = MB.ricci(X4, Gm)
    Xv = [al * SF, be * sp.diff(SF, th), 0, 0]
    LX = sp.Matrix(4, 4, lambda i, j: sum(Xv[k] * sp.diff(G0[i, j], X4[k]) + G0[k, j] * sp.diff(Xv[k], X4[i])
                                          + G0[i, k] * sp.diff(Xv[k], X4[j]) for k in range(4)))
    f_ = MB.f_

    def claim_of(c_coef):
        da = sp.diff(1 / f_, r) * al + 2 * sp.diff(al, r) / f_
        db = al / (r * f_) + r * sp.diff(be, r)
        dc = 2 * al / r - c_coef * k2 * be
        de = 2 * be
        SH = MB.shat()
        cl = sp.diag(1, 0, 0, 0) * da * SF + r**2 * (dc * SF * GHAT + de * SH)
        cl[0, 1] = cl[1, 0] = r * db * sp.diff(SF, th)
        return cl

    def zero_b(M_, fs_):
        return all(convert(eig(M_[i, j], fs_=fs_), F, table, th).iszero() for i in range(4) for j in range(i, 4))
    gok = zero_b(LX - claim_of(sp.Rational(2, 3)), fns_b)
    # [R11-nits] control on the input: X = alpha S d_R + beta S d_th (S in place of S' in the theta component) is not
    # the class mode's vector field, and the shift formulas must fail for it
    Xb = [al * SF, be * SF, 0, 0]
    LXb = sp.Matrix(4, 4, lambda i, j: sum(Xb[k] * sp.diff(G0[i, j], X4[k]) + G0[k, j] * sp.diff(Xb[k], X4[i])
                                           + G0[i, k] * sp.diff(Xb[k], X4[j]) for k in range(4)))
    gctl = not zero_b(LXb - claim_of(sp.Rational(2, 3)), fns_b)
    kps = MB.hess(ps_ * SF, X4, Gm) - ps_ * SF * Ric
    ang = sp.Matrix(3, 3, lambda i, j: kps[i + 1, j + 1])
    SHa = sp.Matrix(3, 3, lambda i, j: MB.shat()[i + 1, j + 1])
    gh3 = sp.diag(1, s_**2, c_**2)
    tf = ang - (sum(ang[i, i] / gh3[i, i] for i in range(3)) / 3) * gh3

    def tf_claim(cf):
        return cf * ps_ * (SHa - (sum(SHa[i, i] / gh3[i, i] for i in range(3)) / 3) * gh3)
    zok = all(convert(eig((tf - tf_claim(1))[i, j], fs_=fns_b), F, table, th).iszero() for i in range(3)
              for j in range(i, 3))
    # [R11-nits] control on the input: the lapse psi S' in place of psi S (not a scalar mode) must fail the claim
    kpb = MB.hess(ps_ * sp.diff(SF, th), X4, Gm) - ps_ * sp.diff(SF, th) * Ric
    angb = sp.Matrix(3, 3, lambda i, j: kpb[i + 1, j + 1])
    tfb = angb - (sum(angb[i, i] / gh3[i, i] for i in range(3)) / 3) * gh3
    zctl = not all(convert(eig((tfb - tf_claim(1))[i, j], fs_=fns_b), F, table, th).iszero() for i in range(3)
                   for j in range(i, 3))
    print("   (b) L_X gamma, X = alpha S d_R + beta S' d_th, shifts (a, b, c, e) by ((1/f)' alpha + 2 alpha'/f, "
          "alpha/(R f) + R beta', 2 alpha/R - (2 k^2/3) beta, 2 beta), every component: %s; the lapse direction's "
          "trace-free angular part is psi (S_hat)^TF: %s; controls (the input mutated): X = alpha S d_R + beta S d_th "
          "fails the shift formulas (rejected): %s; the lapse psi S' fails the claim (rejected): %s (%.0f s)"
          % (gok, zok, gctl, zctl, time.time() - t0), flush=True)
    # (c) the mode-free identities, every (R, theta, mu)
    gi, Gm = MB.christoffel(G0, X4)
    Ric = MB.ricci(X4, Gm)
    n = 4
    Nn = sp.sqrt(MB.f_)
    vol4 = r**3 * s_ * c_ / sp.sqrt(MB.f_)

    def lap0(u):
        return sum(sp.diff(vol4 * gi[i, i] * sp.diff(u, X4[i]), X4[i]) for i in range(n)) / vol4

    def divv(V):
        return sum(sp.diff(vol4 * gi[i, i] * V[i], X4[i]) for i in range(n)) / vol4

    def divT(T):
        DT = MB.cov2(T, X4, Gm)
        return [sum(gi[c, a] * DT[a][b][c] for a in range(n) for c in range(n) if gi[c, a] != 0) for b in range(n)]

    def trace(T):
        return sum(gi[i, i] * T[i, i] for i in range(n))

    def DR(h):
        return -lap0(trace(h)) + divv(divT(h)) - sum(gi[i, i] * gi[j, j] * Ric[i, j] * h[i, j] for i in range(n)
                                                       for j in range(n))

    def Mom(k):
        dk = divT(k)
        tk = trace(k)
        return [dk[i] - sp.diff(tk, X4[i]) for i in range(n)]

    def zero_all(es, fs):
        es = [pre(x) for x in es]
        jn = jet_names(es, fs)
        Fc = GField(['r', 't', 'nu'] + sorted(set(jn.values())), [lambda g: g['r']] + TRIG_ATOMS + [lambda g: g['nu']])
        tb = {r: Fc.el(Fc.g['r']), nu: Fc.el(Fc.g['nu'])}
        tb.update({d: Fc.el(Fc.g[v]) for d, v in jn.items()})
        return all(convert(x, Fc, tb, th).iszero() for x in es)
    Xr, Xt = sp.Function('Xr')(r, th), sp.Function('Xt')(r, th)
    Xv = [Xr, Xt, 0, 0]
    LX = sp.Matrix(4, 4, lambda i, j: sum(Xv[k] * sp.diff(G0[i, j], X4[k]) + G0[k, j] * sp.diff(Xv[k], X4[i])
                                          + G0[i, k] * sp.diff(Xv[k], X4[j]) for k in range(4)))
    i_ok = zero_all([DR(LX)], [Xr, Xt])
    hf = [sp.Function(nm)(r, th) for nm in ('hrr', 'hrt', 'htt', 'h11', 'h22')]
    h = sp.Matrix([[hf[0], hf[1], 0, 0], [hf[1], hf[2], 0, 0], [0, 0, hf[3], 0], [0, 0, 0, hf[4]]])
    els = [eq.lhs for eq in euler_equations(Nn * DR(h) * vol4, hf, [r, th])]
    ii_ok = zero_all(els, hf)
    ps = sp.Function('psi')(r, th)
    kps = MB.hess(ps, X4, Gm) - ps * Ric
    iii_ok = zero_all(Mom(kps), [ps])
    kf = [sp.Function(nm)(r, th) for nm in ('krr', 'krt', 'ktt', 'k11', 'k22')]
    k = sp.Matrix([[kf[0], kf[1], 0, 0], [kf[1], kf[2], 0, 0], [0, 0, kf[3], 0], [0, 0, 0, kf[4]]])
    b = Nn * (sum(gi[i, i] * gi[j, j] * k[i, j] * kps[i, j] for i in range(n) for j in range(n))
              - trace(k) * trace(kps)) * vol4
    lhs = euler_equations(b, [ps], [r, th])[0].lhs
    M = Mom(k)
    rhs = vol4 * (2 * sum(gi[i, i] * sp.diff(Nn, X4[i]) * M[i] for i in range(n)) + Nn * divv(M))
    iv_ok = zero_all([lhs - rhs], kf + [ps])
    ctl = not zero_all(Mom(MB.hess(ps, X4, Gm)), [ps])
    print("   (c) D R[L_X gamma] = 0: %s; the Euler operator of N D R[h] sqrt(gamma) zero in all five components: %s; "
          "M[k_psi] = 0: %s; Euler_psi of N(<k, k_psi> - tr k tr k_psi) sqrt(gamma) = sqrt(gamma)(2 dN.M[k] + N div "
          "M[k]): %s; control: k = D^2 psi without - psi Ric does not solve M (rejected): %s (%.0f s)"
          % (i_ok, ii_ok, iii_ok, iv_ok, ctl, time.time() - t0), flush=True)
    ok = shape_ok and free_ok and rad_ok and gok and zok and i_ok and ii_ok and iii_ok and iv_ok
    print('S4', 'PASS' if ok else 'FAIL', flush=True)
    return ok, ctl and gctl and zctl and not free_bad


# ------------------------------------------------------------------ S5: qsign5 Q1 exactly
def s5():
    print("S5 qsign5 Q1 exactly: the momentum-seed identity for arbitrary G = g^2, kappa0, Y0, nu and E = e^(Ia), "
          "every (R, theta)", flush=True)
    t0 = time.time()
    QS = MB.QS
    R, th = QS.R, QS.th
    G_, k0_, Y0_, Nu_, Ia_, PSI, S1 = QS.G_, QS.k0_, QS.Y0_, QS.Nu_, QS.Ia_, QS.PSI, QS.S1
    bc = QS.load('bandconst5')
    eps_ = sp.Symbol('eps')
    dKt, dp, ds1, ds2, dkap = [sp.Function(nm)(R, th) for nm in ('dKt', 'dp', 'ds1', 'ds2', 'dkappa')]
    G1, G2 = R**2 * sp.sin(th)**2, R**2 * sp.cos(th)**2
    g = sp.diag(G_, R**2, G1, G2)
    Kt = 3 * Y0_ + eps_ * dKt
    K = sp.zeros(4, 4)
    K[0, 0] = G_ * (k0_ + eps_ * dkap)
    K[0, 1] = K[1, 0] = sp.sqrt(G_) * eps_ * dp
    K[1, 1] = R**2 * (Kt / 3 + eps_ * ds1)
    K[2, 2] = G1 * (Kt / 3 + eps_ * ds2)
    K[3, 3] = G2 * (Kt / 3 - eps_ * ds1 - eps_ * ds2)
    Hq, Mq, _ = bc.constraints(g, K, bc.X4)
    lin = [sp.expand(sp.diff(e, eps_).subs(eps_, 0)) for e in (Hq, Mq[0], Mq[1])]
    quad = sp.expand(sp.diff(Hq, eps_, 2).subs(eps_, 0) / 2)
    dk = sp.solve(sp.Eq(lin[0], 0), dkap)[0]
    sc, c, beta, E, Ktf, ph, s2f = QS.seed_fields(G_, k0_, Y0_, Ia_, PSI, S1)
    a = (3 * c - 1) / R
    gfun = sp.Function('g')(R)

    def prep(e):
        for kk_ in range(7, 0, -1):
            e = e.subs(sp.Derivative(Ia_, (R, kk_)), sp.diff(a, R, kk_ - 1))
        e = e.subs(G_, gfun**2).doit()
        for kk_ in range(7, 0, -1):
            e = e.subs(sp.Derivative(Ia_, (R, kk_)), sp.diff(a, R, kk_ - 1).subs(G_, gfun**2).doit())
        # (g^2)^(k/2) = g^k, g > 0; e^(k Ia) = EE^k
        e = e.replace(lambda x: x.is_Pow and x.base == gfun**2 and x.exp.is_Rational and x.exp.q == 2,
                      lambda x: gfun**x.exp.p)
        return e.replace(lambda x: isinstance(x, sp.exp) and (x.args[0] / Ia_).is_Integer,
                         lambda x: EE**int(x.args[0] / Ia_))
    fs = [gfun, k0_, Y0_, Nu_, PSI, S1]
    EE = sp.Symbol('EE', positive=True)

    def zero_all(es):
        es = [prep(x) for x in es]
        jn = jet_names(es, fs)
        Fq = GField(['R', 't', 'EE'] + sorted(set(jn.values()) | {'g_0', 'Y0_0'}),
                    [lambda g_: g_['R']] + TRIG_ATOMS + [lambda g_: g_['EE'], lambda g_: g_['g_0'],
                                                         lambda g_: g_['Y0_0']])
        tb = {R: Fq.el(Fq.g['R']), EE: Fq.el(Fq.g['EE'])}
        tb.update({d: Fq.el(Fq.g[v]) for d, v in jn.items()})
        return all(convert(x, Fq, tb, th).iszero() for x in es)
    subs_ = {dKt: Ktf, dp: R * ph, ds1: S1, ds2: s2f}
    lin_ok = zero_all([e.subs(dkap, dk).subs(subs_).doit() for e in lin])
    qd = Nu_ * sc * quad.subs(dkap, dk).subs(subs_).doit()
    dec, _ = QS.decomposition(Nu_, G_, E, PSI, S1, s2f)
    el = [eq.lhs for eq in euler_equations(qd - dec, [PSI, S1], [R, th])]
    id_ok = zero_all(el)
    dec_m, _ = QS.decomposition(Nu_, G_, E, PSI, S1, s2f, m_gam=sp.Rational(3, 4))
    el_m = [eq.lhs for eq in euler_equations(qd - dec_m, [PSI, S1], [R, th])]
    ctl = not zero_all([el_m[0]])
    print("   the seed (psi, s1) solves the linearised H, M_R, M_th identically: %s; the Euler operator of (Q-density "
          "- decomposition) in psi and s1 is the zero rational function of (R, t, the jets of g, kappa0, Y0, nu, psi, "
          "s1, and e^(Ia)): %s; control: 4 nu E^2 -> 3 nu E^2 gives a nonzero Euler operator (rejected): %s (%.0f s)"
          % (lin_ok, id_ok, ctl, time.time() - t0), flush=True)
    ok = lin_ok and id_ok
    print('S5', 'PASS' if ok else 'FAIL', flush=True)
    return ok, ctl


def main():
    print("mbslice5: Theorem T (iii) and Lemma X1 on every class slice, as exact polynomial identities", flush=True)
    td = MB.tensor_density()
    Gf, Kf, nf, Nf, Yf, H, P = td['F']
    R_ = MB.R_
    HR = sp.diff(H, R_)
    print("   the abstract theta-integrand from mbsign5's constraint map (%.0f s)" % (time.time() - T0), flush=True)
    sq = slice_quantities()
    sq_bad = slice_quantities(drop_wprime=True)
    # S3
    one = sq['N'] * sq['ss'] - RF(1)
    lap = sq['N'] * sq['N'] - sq['G'] * sq['Y'] * sq['Y'] - sq['f']
    s3 = one.iszero() and lap.iszero()
    print("S3 N_s sqrt(gamma_RR) = 1: %s; N_s^2 - gamma_RR (Y_s^R)^2 = f: %s" % (one.iszero(), lap.iszero()))
    print('S3', 'PASS' if s3 else 'FAIL', flush=True)
    ok = s3
    s1, ctl1, ctlK = True, True, True
    iq = {}
    for n in (0, 1, 2, 3):
        A, B, C, kT2, l = MB.class_tt(n)
        nT = sp.integrate(sp.expand(sp.expand_trig((A**2 + B**2 + C**2) * MB.s_ * MB.c_)), (MB.th, 0, sp.pi / 2))
        Iq = MB.theta_integral(td['dens'], td['TA'], n)
        iq[l] = (Iq, nT, kT2)
        Tm = R_**3 * ((Nf * P + Yf * HR) * P + sp.Rational(1, 2) * Nf * (-P**2 + HR**2 / Gf)) \
            + sp.Rational(1, 2) * Nf * (kT2 + 2) * R_ * H**2
        for scale, label in ((1, 'identity'), (sp.Rational(1, 2), '|T|^2 halved')):
            cv = Converter(td['F'], sq)
            L = cv(Iq + 2 * scale * nT * Tm * sp.sqrt(Gf))
            eH, eP = euler(L, HJ), euler(L, PJ)
            z = eH.iszero() and eP.iszero()
            if scale == 1:                                       # what the integrand depends on: the slice's generality
                qs = [k for k in range(NJ) if L.n.diff(QJ[k]) != 0]
                print("   S1, l = %d: the integrand's numerator has %d terms and involves mu: %s and the jets q^(%s) of "
                      "the free slice function" % (l, len(L.n), L.n.diff(MU) != 0, ", ".join(map(str, qs))))
            print("   S1, l = %d (|T|^2 = %s, k_T^2 = %d), %s: Euler operator in H zero %s, in P zero %s (numerator "
                  "terms %d, %d; %.0f s)" % (l, nT, kT2, label, eH.iszero(), eP.iszero(), len(eH.n), len(eP.n),
                                             time.time() - T0), flush=True)
            if scale == 1:
                s1 &= z
            else:
                ctl1 &= not z
        if n == 0:
            cv = Converter(td['F'], sq_bad)
            L = cv(Iq + 2 * nT * Tm * sp.sqrt(Gf))
            zb = euler(L, HJ).iszero() and euler(L, PJ).iszero()
            ctlK = not zb
            print("   control: K_RR with its w' term dropped (a wrong slice), l = 2: identity fails (rejected): %s "
                  "(%.0f s)" % (ctlK, time.time() - T0), flush=True)
    # [R9] every l: the theta-integrated density over |T|^2 is affine in k_T^2 (FAMILIES5-MB.md minor 8, deduced);
    # computed here pointwise in R on every slice for l = 2, 4, 6, 8: (Iq/|T|^2)(l) is the affine interpolant of l = 2, 4
    cv = Converter(td['F'], sq)
    u = {l_: cv(v[0]) * RF(QQ(1) / QQ(int(v[1].p), int(v[1].q))) for l_, v in iq.items()}
    aff = True
    for l_ in (6, 8):
        lam_ = QQ(iq[l_][2] - iq[2][2], iq[4][2] - iq[2][2])
        aff &= (u[l_] - u[2] - RF(lam_) * (u[4] - u[2])).iszero()
    print("   the theta-integrated density over |T|^2 at l = 6 and 8 is the affine interpolant in k_T^2 of l = 2 and 4, "
          "pointwise, on every slice: %s (every l: the minor-8 deduction, which this checks at two more l)" % aff)
    s1 &= aff
    print('S1', 'PASS' if s1 else 'FAIL', flush=True)
    ok &= s1
    # S2: Lemma X1, l = 2, 4, 6, 8
    fR = 1 - MB.mu / R_**2
    s2, ctl2, b_ctl = True, True, True
    for l_ in sorted(iq):
        Iq, nT, kT2 = iq[l_]
        res = {}
        for extra, label in ((2, 'identity'), (3, 'k_T^2 + 3')):
            dX = Iq.subs(P, -Yf / Nf * HR).doit() + nT * (R_**3 * fR * HR**2 + (kT2 + extra) * R_ * H**2)
            res[label] = euler(cv(dX), HJ).iszero()
        d0 = Iq.subs(H, 0).doit()
        b_ok = cv(d0 + nT * R_**3 * P**2).iszero()
        b_ctl &= not cv(d0 + 2 * nT * R_**3 * P**2).iszero()
        s2 &= res['identity'] and b_ok
        ctl2 &= not res['k_T^2 + 3']
        print("   S2, l = %d: with P = -(Y_s^R/N_s) H_R, Q-density + |T|^2 (R^3 f H_R^2 + (k_T^2 + 2) R H^2) has zero "
              "Euler operator in H: %s; with H = 0 the Q-density is -|T|^2 R^3 P^2 pointwise: %s (%.0f s)" %
              (l_, res['identity'], b_ok, time.time() - T0), flush=True)
    print("   controls: k_T^2 + 3 in place of k_T^2 + 2 fails at every l (rejected): %s; R^3 P^2 doubled fails at every "
          "l (rejected): %s" % (ctl2, b_ctl))
    print('S2', 'PASS' if s2 else 'FAIL', flush=True)
    ok &= s2
    s4ok, ctl4 = s4()
    s5ok, ctl5 = s5()
    ok &= s4ok and s5ok
    ctl = ctl1 and ctlK and ctl2 and b_ctl and ctl4 and ctl5
    print("controls rejected:", 'PASS' if ctl else 'FAIL')
    print("S1-S5:", 'PASS' if ok else 'FAIL', "(%.0f s)" % (time.time() - T0))
    return 0 if ok and ctl else 1


if __name__ == '__main__':
    sys.exit(main())
