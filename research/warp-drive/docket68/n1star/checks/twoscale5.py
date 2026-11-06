"""twoscale5: exact two-scale jets for the high-frequency checks of vlasovhf5 (FAMILIES5-VLASOV.md).

A field is a polynomial, with Fraction coefficients, in NV slow variables y (truncated at total degree DEG about the
evaluation point y = 0), in lam (truncated at lam^LMAX; negative powers arise from fast derivatives) and in the two
symbols c = cos s, n = sin s of one fast phase s = u/lam. The derivative along y_i is the two-scale one,
D_i = d/dy_i + lam^-1 u_i d/ds, with d/ds c = -n, d/ds n = c; u_i is a slow jet (the phase's gradient). Every value at
y = 0 is exact as long as no more than DEG derivatives are taken of DEG-jets, which the callers respect (the curvature
takes two). Imported by vlasovhf5.py. Its own check (run it directly):
  T1 (exact) d/ds and the two-scale product rule: D_i(f g) = (D_i f) g + f D_i g on random jets, and D_i of
     u0 exp(lam a c) reproduces the chain rule term lam^-1 u_i (-a n) lam u0 below the truncation order.
  Control (must fail): a mutated d/ds (d/ds c = +n) breaks the product rule's agreement with the chain rule.
Labels: computed (exact, Fractions). Run: python3 checks/twoscale5.py   (seconds)
"""
from fractions import Fraction
import random
import sys

NV = 3
DEG = 2
LMAX = 2
MUTATE_DS = False


class TS:
    """keys (ey, kl, kc, kn): ey a tuple of NV exponents, kl the power of lam, kc, kn the powers of cos s, sin s"""
    __slots__ = ('c',)

    def __init__(self, c=None):
        self.c = {} if c is None else {k: v for k, v in c.items() if v != 0}

    @staticmethod
    def const(x, kl=0, kc=0, kn=0):
        return TS({((0,) * NV, kl, kc, kn): Fraction(x)})

    @staticmethod
    def var(i):
        e = [0] * NV
        e[i] = 1
        return TS({(tuple(e), 0, 0, 0): Fraction(1)})

    @staticmethod
    def poly(coefs):
        """coefs: dict ey -> Fraction (a slow polynomial)"""
        return TS({(ey, 0, 0, 0): Fraction(v) for ey, v in coefs.items() if sum(ey) <= DEG})

    def __add__(self, o):
        if not isinstance(o, TS):
            o = TS.const(o)
        r = dict(self.c)
        for k, v in o.c.items():
            r[k] = r.get(k, 0) + v
        return TS(r)

    __radd__ = __add__

    def __neg__(self):
        return TS({k: -v for k, v in self.c.items()})

    def __sub__(self, o):
        return self + (-o if isinstance(o, TS) else TS.const(-Fraction(o)))

    def __rsub__(self, o):
        return (-self) + o

    def __mul__(self, o):
        if not isinstance(o, TS):
            o = Fraction(o)
            return TS({k: v * o for k, v in self.c.items()})
        r = {}
        for (e1, l1, c1, n1), v1 in self.c.items():
            d1 = sum(e1)
            for (e2, l2, c2, n2), v2 in o.c.items():
                if d1 + sum(e2) > DEG or l1 + l2 > LMAX:
                    continue
                k = (tuple(a + b for a, b in zip(e1, e2)), l1 + l2, c1 + c2, n1 + n2)
                r[k] = r.get(k, 0) + v1 * v2
        return TS(r)

    __rmul__ = __mul__

    def slow_d(self, i):
        r = {}
        for (e, l, kc, kn), v in self.c.items():
            if e[i] > 0:
                ee = list(e)
                ee[i] -= 1
                k = (tuple(ee), l, kc, kn)
                r[k] = r.get(k, 0) + v * e[i]
        return TS(r)

    def ds(self):
        r = {}
        sgn = 1 if MUTATE_DS else -1
        for (e, l, kc, kn), v in self.c.items():
            if kc > 0:
                k = (e, l, kc - 1, kn + 1)
                r[k] = r.get(k, 0) + sgn * kc * v
            if kn > 0:
                k = (e, l, kc + 1, kn - 1)
                r[k] = r.get(k, 0) + kn * v
        return TS(r)

    def lam_shift(self, m):
        return TS({(e, l + m, kc, kn): v for (e, l, kc, kn), v in self.c.items() if l + m <= LMAX})

    def at0(self):
        """{(kl, kc, kn): Fraction} at y = 0"""
        z = (0,) * NV
        r = {}
        for (e, l, kc, kn), v in self.c.items():
            if e == z:
                r[(l, kc, kn)] = r.get((l, kc, kn), 0) + v
        return {k: v for k, v in r.items() if v != 0}

    def slow0(self):
        """the lam^0, trig-free part as a TS"""
        return TS({k: v for k, v in self.c.items() if k[1] == 0 and k[2] == 0 and k[3] == 0})

    def inv(self):
        a0 = self.slow0().c.get(((0,) * NV, 0, 0, 0), Fraction(0))
        assert a0 != 0
        e = (self - a0) * (Fraction(1) / a0)
        tot, term = TS.const(1), TS.const(1)
        for _ in range(DEG + LMAX + 2):
            term = term * (-e)
            tot = tot + term
        return tot * (Fraction(1) / a0)


class Fast:
    """the two-scale derivative D_i = d_i + lam^-1 u_i d/ds; u_i slow jets; directions >= NV are Killing (D = 0)"""

    def __init__(self, du, drop=None):
        self.du, self.drop = du, drop

    def D(self, f, i):
        if i >= NV:
            return TS()
        out = f.slow_d(i)
        if self.drop != i:
            out = out + (self.du[i] * f.ds()).lam_shift(-1)
        return out


def expo(x, terms=LMAX + 1):
    """exp(x) for x with no lam^0 part (x = O(lam)), truncated"""
    tot, term = TS.const(1), TS.const(1)
    for k in range(1, terms + 1):
        term = term * x * Fraction(1, k)
        tot = tot + term
    return tot


def matinv(g):
    """inverse of a matrix of TS whose lam^0 trig-free value at y = 0 is invertible, by a Neumann series"""
    import sympy as sp
    n = len(g)
    g0 = sp.Matrix(n, n, lambda i, j: sp.Rational(g[i][j].at0().get((0, 0, 0), 0)))
    i0 = g0.inv()
    I0 = [[TS.const(Fraction(int(sp.fraction(i0[i, j])[0]), int(sp.fraction(i0[i, j])[1]))) for j in range(n)]
          for i in range(n)]
    E = [[g[i][j] - TS.const(g[i][j].at0().get((0, 0, 0), 0)) for j in range(n)] for i in range(n)]
    M = [[-sum((E[i][k] * I0[k][j] for k in range(n)), TS()) for j in range(n)] for i in range(n)]
    tot = [row[:] for row in I0]
    term = [row[:] for row in I0]
    for _ in range(DEG + LMAX + 2):
        term = [[sum((term[i][k] * M[k][j] for k in range(n)), TS()) for j in range(n)] for i in range(n)]
        tot = [[tot[i][j] + term[i][j] for j in range(n)] for i in range(n)]
    return tot


def christoffel(F, g, gi):
    n = len(g)
    dg = [[[F.D(g[a][b], c) for c in range(n)] for b in range(n)] for a in range(n)]
    low = [[[(dg[d][b][c] + dg[d][c][b] - dg[b][c][d]) * Fraction(1, 2) for c in range(n)] for b in range(n)]
           for d in range(n)]
    return [[[sum((gi[a][d] * low[d][b][c] for d in range(n)), TS()) for c in range(n)] for b in range(n)]
            for a in range(n)]


def ricci(F, g, gi, G=None):
    n = len(g)
    if G is None:
        G = christoffel(F, g, gi)
    tr = [sum((G[a][a][x] for a in range(n)), TS()) for x in range(n)]
    R = [[TS()] * n for _ in range(n)]
    for b in range(n):
        for c in range(b, n):
            e = sum((F.D(G[a][b][c], a) for a in range(n)), TS()) - F.D(tr[b], c)
            for a in range(n):
                for x in range(n):
                    e = e + G[a][a][x] * G[x][b][c] - G[a][c][x] * G[x][a][b]
            R[b][c] = e
            R[c][b] = e
    return R, G


def rpoly(rng, deg=DEG, scale=1, const=None):
    """a random slow polynomial with small rational coefficients"""
    import itertools
    co = {}
    for ey in itertools.product(range(deg + 1), repeat=NV):
        if sum(ey) <= deg:
            co[ey] = Fraction(rng.randint(-4, 4), rng.randint(1, 4) * scale)
    if const is not None:
        co[(0,) * NV] = Fraction(const)
    return TS.poly(co)


def harmonics(vals, kl):
    """the lam^kl part of an at0() dict as Fourier coefficients {m: complex Fraction pair (re, im)} of e^(i m s)"""
    import sympy as sp
    s = sp.Symbol('s', real=True)
    e = sum(sp.Rational(v.numerator, v.denominator) * sp.cos(s)**kc * sp.sin(s)**kn
            for (l, kc, kn), v in vals.items() if l == kl)
    e = sp.expand(sp.expand_trig(sp.fu(e)) if e != 0 else 0)
    z = sp.Symbol('z')
    ez = sp.expand(sp.sympify(e).rewrite(sp.exp).subs(sp.exp(sp.I * s), z).subs(sp.exp(-sp.I * s), 1 / z))
    out = {}
    for t in sp.Add.make_args(sp.expand(ez)):
        if t == 0:
            continue
        p = sp.degree(t, z) if t.has(z) else 0
        pw = t.as_powers_dict().get(z, 0)
        out[int(pw)] = sp.nsimplify(out.get(int(pw), 0) + t / z**pw)
    return {m: sp.simplify(v) for m, v in out.items() if sp.simplify(v) != 0}


def t1():
    global MUTATE_DS
    rng = random.Random(3)
    du = [rpoly(rng, const=k + 1) for k in range(NV)]
    F = Fast(du)
    f = rpoly(rng) + rpoly(rng) * TS.const(1, 1, 1, 0) + rpoly(rng) * TS.const(1, 1, 0, 1)
    g = rpoly(rng) + rpoly(rng) * TS.const(1, 1, 0, 1)
    ok = all(F.D(f * g, i).at0() == (F.D(f, i) * g + f * F.D(g, i)).at0() for i in range(NV))
    a = rpoly(rng, const=1)
    u0 = rpoly(rng, const=2)

    def chain():
        x = expo(a * TS.const(1, 1, 1, 0))                    # exp(lam a cos s)
        lhs = F.D(u0 * x, 0)
        rhs = u0.slow_d(0) * x + u0 * (a.slow_d(0) * TS.const(1, 1, 1, 0)) * x \
            + u0 * (du[0] * a * TS.const(-1, 0, 0, 1)) * x     # lam^-1 u_0 (-a sin s) lam = -u_0 a sin s
        low = lambda d: {k: v for k, v in d.items() if k[0] <= LMAX - 1}   # noqa: E731 (top order truncated)
        return low(lhs.at0()) == low(rhs.at0())
    ok2 = chain()
    MUTATE_DS = True
    ctl = not chain()
    MUTATE_DS = False
    print("T1 (exact) two-scale product rule: %s; chain rule for exp(lam a cos s): %s; control (mutated d/ds) "
          "rejected: %s" % (ok, ok2, ctl))
    return ok and ok2 and ctl


if __name__ == '__main__':
    r = t1()
    print("PASS" if r else "FAIL")
    sys.exit(0 if r else 1)
