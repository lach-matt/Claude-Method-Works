#!/usr/bin/env python3
"""lin5.py -- [Hin26] Lemma 8.4 in five dimensions: the indicial roots of the linearized gauge-fixed Einstein operator
L = D Ric + delta*_{E^C} delta_{E^Ups} G on 4+1 Minkowski, by harmonic type, and their factorization through the gauge
potential operator box^Ups = 2 delta_{E^Ups} G delta* and the constraint propagation operator box^C = 2 delta G
delta*_{E^C} (N1STAR-PROOF.md section 10.24; ROUTES-OPEN.md 4.25; D72).  Labels: computed (exact, sympy; numerical,
mpmath, where said), deduced, READ.

[Hin26] (arXiv:2606.28253v2) section 8: L_b = D Ric + delta*_{E^C} delta_{E^Ups} G ((8.1)), 2 L_b = box + 2 E^C delta
G + 2 delta*_{E^C} E^Ups G + 2 R ((8.5)); his Lemma 8.4 lists the indicial roots of its zero energy operator by type and
proves them by "explicit square matrices ... performed with Wolfram Mathematica" (p. 150): det N_s0(rho^-2 L(0), lam) =
det N_s0(box^Ups(0), lam - 1) det N_s0(box^C(0), lam + 1), and for s1, sl (l >= 2), v1, vl (l >= 2) the same with the
factors (lam + 1)(lam - 2) (lam - 1)^-1 lam^-1, -(lam + l)(lam - l - 1), (lam + 1)(lam - 2) lam^-1 (lam - 1)^-1 and
-(lam + l)(lam - l - 1) (pp. 150-151): no root in (0, eps_ind), the roots of each type split evenly, and those from
box^C with real part <= 0 are below -100.  Here, from the definitions: E^Ups h = -gam_U (2 iota_{c_U#} h - m (1 - e_U)
c_U tr h), c_U = r^-1 dt ((6.5)); E^C w = gam_C (2 c (x)_s w - m (1 - e_C) g <c, w>), c = r^-1 (dt - v dr) ((7.3)); the
trace weight m = 2/(D - 2), 2/3 in five dimensions (10.12, 10.15); D Ric h = (1/2)(d^a d_mu h_nu a + d^a d_nu h_mu a -
d^a d_a h_mu nu - d_mu d_nu tr h) on Minkowski.  The indicial family is read off at a point: the static tensor r^-lam u,
u of degree 0 and of one harmonic type, goes to r^-lam-2 N(lam) u; in Cartesian coordinates, r an independent symbol,
with the harmonics of C^2 = R^4 (z = x_1 + i x_2, w = x_3 + i x_4): S = z^l (scalar), V = z^(l-1) beta (vector), T =
z^(l-2) beta (x) beta (tensor), beta = z dw - w dz -- tangential, divergence-free, trace-free and harmonic -- with z^p a
symbol of derivative p z^p dz/z, so that l is symbolic.

  E1 (computed, exact) The type spaces are invariant: at two generic points of R^4 (|x| = 5 and 3) the image of every
     basis tensor of types s0, s2, v1, v2 and t2, times r^2, lies in the span of the basis there, with the same matrix
     N(lam) at both; and (8.5) holds at both points on every basis tensor.  Control: a scalar-type basis with its
     Hessian tensor replaced by the tensor type's, which is not closed.
  E2 (computed, exact) The factorization in five dimensions, every parameter symbolic: det N_L(lam) = c (lam + l)(lam -
     l - 2) det N_Ups(lam - 1) det N_C(lam + 1) / D(lam), c a nonzero number, for s0 (l = 0, D = (lam - 1)^2), s1 (l = 1,
     D = (lam - 1)^2), sl (l >= 2 symbolic, D = 1), v1 (D = lam (lam - 2)), vl (l >= 2 symbolic, D = 1), and the tensor
     type tl (l >= 2 symbolic): det N_L = c (lam + l)(lam - l - 2).  So the physical roots are -l and l + 2 (n - 2 = 2)
     in every type, the mass at s0 the root 2, and D removes the roots box^Ups's Killing 1-forms (dt, dx, the rotations)
     and box^C's Coulomb root give twice.  Control: the four-dimensional factor (lam + l)(lam - l - 1) claimed.
  E3 (computed, exact) Four-dimensional control: at n = 3 and the trace weight 1 the same computation gives his (1)-(5):
     s0 with no factor, s1 and v1 (lam + 1)(lam - 2)/(lam (lam - 1)), sl and vl (lam + l)(lam - l - 1) (pp. 150-151).
  E4 (computed, exact) Cross-checks: det N_Ups is gaugepot5.py G1's (gam -> gam_U, e -> e_U) and det N_C is damping5.py's
     (h -> 1/gam_C, e -> e_C, kappa = l (l + 2)), each up to a constant (and det N_C up to the power of h = 1/gam_C by
     which damping5.py normalizes its polynomials); and at gam_U = gam_C = 0, where 2 L = box, the determinants factor
     into linear factors with integer roots, none in (0, 2), the free operator's indicial gap, as many <= 0 as >= 2 in
     each type.
  E5 (computed; numerical for box^C's roots, mpmath at 50 digits) The roots at the parameter point (v, e_C, gam_C) =
     (1/2, 1/102400, 10^6), (e_U, gam_U) = (1/100, 1/100), for every type and l <= 12, from the factors of E2: all
     simple; none with real part in (0, 1]; as many with real part <= 0 as > 1 in each type; those from box^C with real
     part <= 0 below -101; 0 a root of s0 and s2 only; reported, the least positive real part, the greatest negative
     one (his delta of Proposition 8.6 lies below it) and the least distance from Z of the real part of a non-integer
     root with |lam| <= 50 (his (8.13)), required nonzero.  Lemma 8.5: the kernels of N(L, 0) at s0 and s2 are
     annihilated by N(delta_{E^Ups} G, 0) (exact).  Control: the cancelled factor D kept at s0, where the root 1 then
     enters (0, 1].

Deduced, not computed here: with gaugepot5.py G1's explicit box^Ups roots (every l, every small z = 4 e_U gam_U^2 > 0,
all moving away from the gap as z grows) and Proposition 10.9's box^C roots (none with real part in [-100, 2] but the
Coulomb root 2 at l = 0 and 1, which D removes), E2 gives his Lemma 8.4 in five dimensions for every l: the roots are
box^Ups's plus 1, box^C's minus 1 and -l, l + 2; none has real part in (0, 1]; each type splits evenly; and the box^C
roots with real part <= 0 lie below -101.  Simplicity is computed for l <= 12 at the point and not claimed beyond.

READ.  [Hin26] pp. 144-145 (section 8: (8.1), the choices (1)-(2), Lemma 8.1), 149-151 (Lemma 8.4 and its proof, (8.13),
Lemma 8.5), 151-153 (Proposition 8.6 and its proof, Corollary 8.7), 117 (Lemma 6.6), 135-136 ((7.3)-(7.8)); alphaXiv,
2026-10-23.

sympy.  python3 lin5.py [--selftest | --mutants]   (--verbose lists every sub-check; about 50 and 20 minutes)
"""
import sys
import time

import mpmath as mpm
import sympy as sp
from sympy.polys.matrices import DomainMatrix

import damping5 as DP
import gaugepot5 as GP
from damping5 import Checklist

I = sp.I
lam, l, v = sp.symbols("lam l v", real=True)
gU, eU, gC, eC = sp.symbols("gU eU gC eC", real=True)
Zs = sp.Symbol("Zs")                                       # z^p, p given per type
GENS = (lam, gU, eU, gC, eC, v)
POINT = {v: sp.Rational(1, 2), eC: sp.Rational(1, 102400), gC: sp.Integer(10**6), eU: sp.Rational(1, 100),
         gU: sp.Rational(1, 100)}
LMAX = 12


# ------------------------------------------------------------------------------------------------- the operators
class Ctx:
    """(n+1)-Minkowski, Cartesian, static; fields are r^-(lam + deg) times expressions of degree deg in x"""

    def __init__(self, n, p, deg):
        self.n, self.p, self.deg = n, p, deg
        self.x = sp.symbols("x1:%d" % (n + 1), real=True)
        self.r = sp.Symbol("r", positive=True)
        x = self.x
        self.z = x[0] + I * x[1]
        self.w = (x[2] + I * x[3]) if n >= 4 else None
        self.dz = [1, I] + [0] * (n - 2)
        self.dw = [0, 0, 1, I] if n >= 4 else None
        self.N = n + 1
        self.eta = sp.diag(-1, *([1] * n))
        self.m = sp.Rational(2, n - 1)

    def pd(self, f, i):
        x, r = self.x, self.r
        out = sp.diff(f, x[i]) + x[i] / r * sp.diff(f, r)
        if self.dz[i] != 0 and self.p != 0:
            out += sp.diff(f, Zs) * self.p * Zs * self.dz[i] / self.z
        return out

    def d(self, f, a):
        if a == 0:
            return sp.Integer(0)
        return self.pd(f, a - 1) - (lam + self.deg) * self.x[a - 1] / self.r**2 * f


def tr(C, h):
    return sum(C.eta[a, a] * h[a, a] for a in range(C.N))


def Gop(C, h):
    return h - C.eta * tr(C, h) / 2


def delta(C, h):
    return [-sum(C.eta[k, k] * C.d(h[a, k], k) for k in range(C.N)) for a in range(C.N)]


def dstar(C, w):
    return sp.Matrix(C.N, C.N, lambda a, b: (C.d(w[b], a) + C.d(w[a], b)) / 2)


def cvecs(C):
    r, x = C.r, C.x
    return [1 / r] + [0] * C.n, [1 / r] + [-v * xi / r**2 for xi in x]


def E_U(C, h):
    cU, _ = cvecs(C)
    cs = [C.eta[k, k] * cU[k] for k in range(C.N)]
    t = tr(C, h)
    return [-gU * (2 * sum(cs[k] * h[k, a] for k in range(C.N)) - C.m * (1 - eU) * cU[a] * t) for a in range(C.N)]


def E_C(C, w):
    _, c = cvecs(C)
    cw = sum(C.eta[k, k] * c[k] * w[k] for k in range(C.N))
    return sp.Matrix(C.N, C.N, lambda a, b: gC * (c[a] * w[b] + c[b] * w[a] - C.m * (1 - eC) * C.eta[a, b] * cw))


def box_U(C, w):
    Gd = Gop(C, dstar(C, w))
    return [2 * (a + b) for a, b in zip(delta(C, Gd), E_U(C, Gd))]


def box_C(C, w):
    return [2 * a for a in delta(C, Gop(C, dstar(C, w) + E_C(C, w)))]


def gauge(C, h):
    """delta_{E^Ups} G h, the linearized gauge 1-form"""
    Gh = Gop(C, h)
    return [a + b for a, b in zip(delta(C, Gh), E_U(C, Gh))]


def dric(C, h):
    N, eta, d = C.N, C.eta, C.d
    dh = [[[d(h[a, b], c) for c in range(N)] for b in range(N)] for a in range(N)]
    t = tr(C, h)
    dt_ = [d(t, a) for a in range(N)]
    out = sp.zeros(N, N)
    for mu in range(N):
        for nu in range(mu, N):
            s = 0
            for al in range(N):
                s += eta[al, al] * (d(dh[nu][al][mu], al) + d(dh[mu][al][nu], al) - d(dh[mu][nu][al], al))
            out[mu, nu] = out[nu, mu] = (s - d(dt_[nu], mu)) / 2
    return out


def Lbar(C, h):
    w = gauge(C, h)
    return dric(C, h) + dstar(C, w) + E_C(C, w)


def rhs85(C, h):
    """box + 2 E^C delta G + 2 delta*_{E^C} E^Ups G, [Hin26] (8.5) on Minkowski"""
    N = C.N
    box = sp.Matrix(N, N, lambda a, b: -sum(C.eta[k, k] * C.d(C.d(h[a, b], k), k) for k in range(N)))
    Gh = Gop(C, h)
    EU = E_U(C, Gh)
    return box + 2 * E_C(C, delta(C, Gh)) + 2 * (dstar(C, EU) + E_C(C, EU))


# ------------------------------------------------------------------------------------------------- bases
def embed(C, spatial=None, t0=None, tt=None):
    N, n = C.N, C.n
    h = sp.zeros(N, N)
    if tt is not None:
        h[0, 0] = tt
    if t0 is not None:
        for i in range(n):
            h[0, i + 1] = h[i + 1, 0] = t0[i]
    if spatial is not None:
        for i in range(n):
            for j in range(n):
                h[i + 1, j + 1] = spatial[i, j]
    return h


def vfield(C):
    if C.n == 3:                                           # x cross grad z^p, degree p
        x, g = C.x, [C.pd(Zs, k) for k in range(3)]
        return [x[1] * g[2] - x[2] * g[1], x[2] * g[0] - x[0] * g[2], x[0] * g[1] - x[1] * g[0]]
    return [Zs * (C.z * C.dw[i] - C.w * C.dz[i]) for i in range(C.n)]


def sgrad(C):
    """the tangential gradient r dS - deg S dr of S = z^deg, of degree deg"""
    return [C.r * C.pd(Zs, i) - C.deg * C.x[i] / C.r * Zs for i in range(C.n)]


def sbasis1(C):
    xr = [xi / C.r for xi in C.x]
    B = [[Zs] + [0] * C.n, [0] + [Zs * q for q in xr]]
    if C.deg != 0:
        B.append([0] + sgrad(C))
    return B


def vbasis1(C):
    return [[0] + vfield(C)]


def nonzero(C, M):
    P = point(C, 0)
    return any(sp.simplify(sp.sympify(q).subs(P)) != 0 for q in M)


def sbasis2(C, broken=False):
    S, x, r, n, deg = Zs, C.x, C.r, C.n, C.deg
    xr = [xi / r for xi in x]
    g = sgrad(C)
    Pi = sp.eye(n) - sp.Matrix(n, n, lambda i, j: xr[i] * xr[j])
    B = [embed(C, tt=S), embed(C, t0=[S * q for q in xr]),
         embed(C, spatial=sp.Matrix(n, n, lambda i, j: S * xr[i] * xr[j])), embed(C, spatial=S * Pi)]
    if deg != 0:
        B += [embed(C, t0=g), embed(C, spatial=sp.Matrix(n, n, lambda i, j: xr[i] * g[j] + xr[j] * g[i]))]
        S0 = S * r**(-deg)
        H = sp.Matrix(n, n, lambda i, j: C.pd(C.pd(S0, j), i))
        T7 = (Pi * H * Pi * r**(deg + 2) + sp.sympify(deg * (deg + n - 2)) / (n - 1) * S * Pi).applyfunc(
            lambda q: sp.expand(sp.powsimp(sp.expand(q), force=True)))
        if broken:                                         # control: the tensor type's tensor in its place
            b = [C.z * C.dw[i] - C.w * C.dz[i] for i in range(n)]
            T7 = sp.Matrix(n, n, lambda i, j: Zs * b[i] * b[j] / C.z**2)
        if nonzero(C, T7):
            B.append(embed(C, spatial=T7))
    return B


def vbasis2(C):
    x, r, n = C.x, C.r, C.n
    V = vfield(C)
    xr = [xi / r for xi in x]
    B = [embed(C, t0=V), embed(C, spatial=sp.Matrix(n, n, lambda i, j: xr[i] * V[j] + xr[j] * V[i]))]
    V0 = [q * r**(-C.deg) for q in V]
    Dv = sp.Matrix(n, n, lambda i, j: (C.pd(V0[j], i) + C.pd(V0[i], j)) / 2)
    Pi = sp.eye(n) - sp.Matrix(n, n, lambda i, j: xr[i] * xr[j])
    T3 = (Pi * Dv * Pi * r**(C.deg + 1)).applyfunc(lambda q: sp.expand(sp.powsimp(sp.expand(q), force=True)))
    if nonzero(C, T3):
        B.append(embed(C, spatial=T3))
    return B


def tbasis2(C):
    b = [C.z * C.dw[i] - C.w * C.dz[i] for i in range(C.n)]
    return [embed(C, spatial=sp.Matrix(C.n, C.n, lambda i, j: Zs * b[i] * b[j]))]


# ------------------------------------------------------------------------------------------------- indicial families
def point(C, which=0):
    vals = ([1, 2, 2, 4], [1, 2, 2, 0])[which] if C.n == 4 else ([1, 2, 2], [2, 1, 2])[which]
    rr = sp.sqrt(sum(q**2 for q in vals))
    return {**dict(zip(C.x, vals)), C.r: rr, Zs: 1}


def flat(C, T):
    if isinstance(T, sp.MatrixBase):
        return [T[a, b] for a in range(C.N) for b in range(a, C.N)]
    return list(T)


def Nmat(C, basis, outs, which=0, scale=1):
    """the matrix N with out_k = sum_j N_jk basis_j at the point, and whether the images lie in the span"""
    P = point(C, which)
    ev = lambda q: sp.expand(sp.sympify(q).subs(P))
    E = sp.Matrix([[ev(q) for q in flat(C, b)] for b in basis]).T
    O = sp.Matrix([[ev(scale * q) for q in flat(C, o)] for o in outs]).T
    assert E.rank() == len(basis)
    Eh = E.H
    N = ((Eh * E).applyfunc(sp.cancel).inv() * (Eh * O)).applyfunc(lambda q: sp.cancel(sp.expand(q)))
    res = (E * N - O).applyfunc(lambda q: sp.cancel(sp.expand(q)))
    return N, all(q == 0 for q in res)


def fastdet(N):
    gens = GENS + ((l,) if N.has(l) else ())
    nd = [sp.fraction(sp.cancel(q)) for q in N]
    den = sp.lcm([d for _, d in nd])
    Mp = (N * den).applyfunc(lambda q: sp.expand(sp.cancel(q)))
    dM = DomainMatrix.from_Matrix(Mp).convert_to(sp.QQ[gens])
    return sp.factor(dM.domain.to_sympy(dM.det()) / den**N.shape[0])


def ctx_of(n, typ):
    deg = {"s0": 0, "s1": 1, "s2": 2, "sl": l, "v1": 1, "v2": 2, "vl": l, "t2": 2, "tl": l}[typ]
    kind = typ[0]
    if kind == "s":
        return Ctx(n, deg, deg)
    if kind == "v":
        return Ctx(n, deg - 1, deg) if n == 4 else Ctx(n, deg, deg)
    return Ctx(n, deg - 2, deg)


def bases(C, typ):
    kind = typ[0]
    if kind == "s":
        return sbasis1(C), sbasis2(C)
    if kind == "v":
        return vbasis1(C), vbasis2(C)
    return None, tbasis2(C)


_D = {}


def dets(n, typ):
    """(det N_Ups, det N_C, det N_L, N_L, closure) for a type, cached"""
    if (n, typ) not in _D:
        C = ctx_of(n, typ)
        B1, B2 = bases(C, typ)
        dU = dC = sp.Integer(1)
        ok = True
        if B1 is not None:
            NU, o1 = Nmat(C, B1, [box_U(C, b) for b in B1], scale=C.r**2)
            NC, o2 = Nmat(C, B1, [box_C(C, b) for b in B1], scale=C.r**2)
            dU, dC, ok = fastdet(NU), fastdet(NC), o1 and o2
        NL, o3 = Nmat(C, B2, [Lbar(C, b) for b in B2], scale=C.r**2)
        _D[(n, typ)] = (dU, dC, fastdet(NL), NL, ok and o3)
    return _D[(n, typ)]


def phys(n, lv):
    return (lam + lv) * (lam - lv - (n - 2))


DEN = {4: {"s0": (lam - 1)**2, "s1": (lam - 1)**2, "v1": lam * (lam - 2)},
       3: {"s0": lam * (lam - 1), "s1": lam * (lam - 1), "v1": lam * (lam - 1)}}
LVAL = {"s0": 0, "s1": 1, "sl": l, "v1": 1, "vl": l, "tl": l}


def ratio_is_const(n, typ, physn=None):
    dU, dC, dL, _, ok = dets(n, typ)
    lv = LVAL[typ]
    pf = phys(physn if physn else n, lv) / DEN[n].get(typ, 1)
    q = sp.cancel(dL / (dU.subs(lam, lam - 1) * dC.subs(lam, lam + 1) * pf))
    return ok and q != 0 and not (q.free_symbols & {lam, l, gU, eU, gC, eC, v}), q


# ------------------------------------------------------------------------------------------------- E1
def e1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for typ in (("s2",) if control else ("s0", "s2", "v1", "v2", "t2")):
        C = ctx_of(4, typ)
        B2 = sbasis2(C, broken=control == 1) if typ[0] == "s" else bases(C, typ)[1]
        outs = [Lbar(C, b) for b in B2]
        N0, ok0 = Nmat(C, B2, outs, 0, scale=C.r**2)       # the images carry r^-2
        N1, ok1 = Nmat(C, B2, outs, 1, scale=C.r**2)
        same = (N0 - N1).applyfunc(sp.cancel) == sp.zeros(*N0.shape)
        k85 = True
        for b, o in zip(B2, outs):
            dif = 2 * o - rhs85(C, b)
            for which in (0, 1):
                P = point(C, which)
                k85 &= all(sp.cancel(sp.expand(sp.sympify(q).subs(P))) == 0 for q in flat(C, dif))
        chk(f"{typ}: {len(B2)} basis tensors, the images in their span at both points, N(lam) the same, (8.5) holds",
            ok0 and ok1 and same and k85)
    return chk.ok


# ------------------------------------------------------------------------------------------------- E2
def e2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for typ in (("s0",) if control else ("s0", "s1", "sl", "v1", "vl", "tl")):
        good, q = ratio_is_const(4, typ, physn=3 if control == 1 else None)
        dL = dets(4, typ)[2]
        lv = LVAL[typ]
        f = f"(lam + {lv})(lam - {lv} - 2)"
        chk(f"n + 1 = 5, {typ}: det N_L = {q} {f} det N_Ups(lam - 1) det N_C(lam + 1) / {DEN[4].get(typ, 1)}"
            + ("" if typ != "tl" else f"; det N_L = {dL}"), good)
    return chk.ok


# ------------------------------------------------------------------------------------------------- E3
def e3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for typ in ("s0", "s1", "sl", "v1", "vl"):
        good, q = ratio_is_const(3, typ)
        chk(f"n + 1 = 4 (his Lemma 8.4), {typ}: det N_L / (det N_Ups(lam - 1) det N_C(lam + 1)) = {q} x "
            f"{sp.factor(phys(3, LVAL[typ]) / DEN[3].get(typ, 1))}", good)
    return chk.ok


# ------------------------------------------------------------------------------------------------- E4
def proportional(p, q, h_=None):
    """p = c q, c a nonzero number -- times a power of h_ if given"""
    r_ = sp.cancel(p / q)
    if r_ == 0:
        return False
    if h_ is None:
        return not (r_.free_symbols & {lam, l, gU, eU, gC, eC, v})
    num, den = sp.fraction(r_)
    mono = lambda q_: sp.Poly(q_, h_).is_monomial
    return (num.free_symbols | den.free_symbols) <= {h_} and mono(num) and mono(den)


def e4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    g0, gl, gv = GP.indicial(4, sp.Rational(2, 3))
    sub = {GP.gam: gU, GP.e: eU, GP.L: l, GP.lam: lam}
    okU = (proportional(dets(4, "s0")[0], g0.subs(sub)) and proportional(dets(4, "sl")[0], gl.subs(sub))
           and proportional(dets(4, "vl")[0], gv.subs(sub)))
    chk("det N_Ups is gaugepot5.py G1's (s0, sl, vl), up to constants", okU)
    pk, p0, pv = DP.polys(4, sp.Rational(2, 3))
    subC = {DP.h: 1 / gC, DP.e: eC, DP.v: v, DP.lam: lam}
    okC = (proportional(dets(4, "s0")[1], p0.subs(subC), gC)
           and proportional(dets(4, "sl")[1], pk.subs(subC).subs(DP.K, l * (l + 2)), gC)
           and proportional(dets(4, "vl")[1], pv.subs(subC).subs(DP.K, l * (l + 2)), gC))
    chk("det N_C is damping5.py's (h = 1/gam_C, kappa = l (l + 2)), up to constants and its normalization by a power "
        "of h", okC)
    ok0 = True
    gap = (0, 2) if control != 1 else (0, 3)                          # control: (0, 3) claimed
    for typ in ("s0", "s1", "sl", "v1", "vl", "tl"):
        dL = dets(4, typ)[2].subs({gU: 0, gC: 0})
        for lv in ((LVAL[typ],) if typ in ("s0", "s1", "v1") else (2, 3, 7)):
            P = sp.Poly(sp.expand(sp.numer(sp.together(dL.subs(l, lv)))), lam)
            rts = sp.roots(P)
            ok0 &= sum(rts.values()) == P.degree() and all(z.is_integer for z in rts)
            ok0 &= not any(gap[0] < z < gap[1] for z in rts)
            ok0 &= sum(k for z, k in rts.items() if z <= 0) == sum(k for z, k in rts.items() if z >= 2)
    chk(f"at gam_U = gam_C = 0 (2 L = box): integer roots in every type (l = 2, 3, 7 where symbolic), none in {gap}, "
        f"as many <= 0 as >= 2", ok0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- E5
def roots_at_point(typ, lv, keep_den=False):
    """the roots of det N_L at the point, from the factors of E2: (roots, which came from box^C)"""
    mpm.mp.dps = 50
    dU, dC, _, _, _ = dets(4, {"s0": "s0", "s1": "s1", "v1": "v1"}.get(typ, typ))
    out, fromC = [], []
    if typ[0] != "t":
        U = sp.Poly(sp.expand(sp.numer(sp.together(dU.subs(l, lv).subs(POINT).subs(lam, lam - 1)))), lam)
        Cp = sp.Poly(sp.expand(sp.numer(sp.together(dC.subs(l, lv).subs(POINT).subs(lam, lam + 1)))), lam)
        ru = [complex(z) for z in mpm.polyroots([mpm.mpf(sp.Rational(c)) for c in U.all_coeffs()], maxsteps=400,
                                                extraprec=400)]
        rc = [complex(z) for z in mpm.polyroots([mpm.mpf(sp.Rational(c)) for c in Cp.all_coeffs()], maxsteps=400,
                                                extraprec=400)]
        den = [] if keep_den else {"s0": [1, 1], "s1": [1, 1], "v1": [0, 2]}.get(typ, [])
        for z0 in den:                                        # remove the cancelled roots, one from each list
            for lst in (ru, rc):
                k = min(range(len(lst)), key=lambda i: abs(lst[i] - z0))
                if abs(lst[k] - z0) < 1e-20:
                    lst.pop(k)
                    break
        out, fromC = ru + rc, rc
    return out + [complex(-lv), complex(lv + 2)], fromC


def e5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ok = True
    zero_types = set()
    worst, negmax, dz = 1e9, -1e9, 1e9
    cases = [("s0", 0), ("s1", 1), ("v1", 1)] + [(t, k) for t in ("sl", "vl", "tl") for k in range(2, LMAX + 1)]
    if control:
        cases = [("s0", 0)]
    for typ, lv in cases:
        rts, fromC = roots_at_point(typ, lv, keep_den=control == 1)
        n_ = len(rts)
        simple = all(abs(rts[i] - rts[j]) > 1e-30 for i in range(n_) for j in range(i + 1, n_))
        gap = not any(0 < z.real <= 1 for z in rts)
        left = sum(1 for z in rts if z.real <= 0)
        right = sum(1 for z in rts if z.real > 1)
        cneg = all(z.real < -101 for z in fromC if z.real <= 0)
        if any(abs(z) < 1e-30 for z in rts):
            zero_types.add(typ if typ[1] in "01" else f"{typ[0]}{lv}")
        pos = [z.real for z in rts if z.real > 0]
        worst = min(worst, min(pos) if pos else 1e9)
        negmax = max([negmax] + [z.real for z in rts if z.real < -1e-30])   # his delta lies below it
        for z in rts:                                       # (8.13): non-integer roots with |lam| <= 50
            if abs(z) <= 50 and abs(z - round(z.real)) > 1e-30:
                dz = min(dz, abs(z.real - round(z.real)))
        ok &= simple and gap and left == right and left + right == n_ and cneg and dz > 1e-30
        if verbose and control == 0 and (lv <= 3):
            print(f"        {typ} l = {lv}: {n_} roots, {left} | {right}, least positive real part {min(pos):.6f}")
    chk(f"at the point, l <= {LMAX}: simple, none in (0, 1], even split, box^C's nonpositive ones below -101; the least "
        f"positive real part {worst:.6f}, the greatest negative {negmax:.4e}; the least distance from Z of a "
        f"non-integer root's real part, |lam| <= 50, {dz:.4e}; 0 a root of {sorted(zero_types)} only",
        ok and zero_types == ({"s0"} if control else {"s0", "s2"}))
    if control:
        return chk.ok
    # Lemma 8.5: ker N(L, 0) at s0 and s2 is annihilated by N(delta_{E^Ups} G, 0)
    ok85 = True
    for typ in ("s0", "s2"):
        C = ctx_of(4, typ)
        B1, B2 = bases(C, typ)
        NL = dets(4, typ)[3].subs(POINT).subs(lam, 0)
        ker = NL.nullspace()
        Ng, okg = Nmat(C, B1, [[q.subs(POINT) for q in gauge(C, b)] for b in B2], scale=C.r)
        Ng0 = Ng.subs(POINT).subs(lam, 0)
        ok85 &= len(ker) == 1 and okg and all(q == 0 for q in (Ng0 * ker[0]).applyfunc(sp.simplify))
    chk("Lemma 8.5: ker N(L, 0) is one-dimensional at s0 and at s2 and lies in ker N(delta_{E^Ups} G, 0)", ok85)
    return chk.ok


CHECKS = [("E1 the type spaces invariant at two points, the same N(lam), and (8.5) on Minkowski", e1, 1),
          ("E2 Lemma 8.4 in five dimensions: det N_L = c (lam + l)(lam - l - 2) det N_Ups(lam - 1) det N_C(lam + 1) / D",
           e2, 1),
          ("E3 four-dimensional control: his Lemma 8.4 (1)-(5), Mathematica's factorizations reproduced", e3, 0),
          ("E4 cross-checks with gaugepot5.py G1 and damping5.py; at gam = 0 integer roots outside (0, 2)", e4, 1),
          ("E5 the roots at the point (l <= 12): simple, none in (0, 1], even split; Lemma 8.5 at s0 and s2", e5, 1)]


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
    print(f"lin5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"lin5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
