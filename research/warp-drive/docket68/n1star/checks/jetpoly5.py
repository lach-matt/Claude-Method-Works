"""jetpoly5: exact truncated multivariate polynomials (Fractions) for the jet checks of classchi5 and augment5.

A Jet is a dict {exponent tuple: Fraction} in NV variables, truncated at total degree DEG. Every identity checked at
the origin with it is exact as long as the quantities used there involve at most DEG - (number of derivatives taken)
orders, which the callers respect (they use at most two derivatives of degree-3 jets at the origin).
Imported by classchi5.py, augment5.py and axisloss5.py. Its own check (run it directly):
  J1 (exact) a product and an inverse of random jets agree with sympy's series to total degree DEG.
  Control (must fail): the same with the truncation at DEG - 1 misses the degree-DEG coefficients.
Labels: computed (exact, Fractions). Run: python3 checks/jetpoly5.py   (seconds)
"""
from fractions import Fraction
import itertools

NV = 5
DEG = 3


class Jet:
    __slots__ = ('c',)

    def __init__(self, c=None):
        self.c = {} if c is None else {k: v for k, v in c.items() if v != 0}

    @staticmethod
    def const(x):
        return Jet({(0,) * NV: Fraction(x)})

    @staticmethod
    def var(i):
        e = [0] * NV
        e[i] = 1
        return Jet({tuple(e): Fraction(1)})

    def __add__(self, o):
        if not isinstance(o, Jet):
            o = Jet.const(o)
        r = dict(self.c)
        for k, v in o.c.items():
            r[k] = r.get(k, 0) + v
        return Jet(r)

    __radd__ = __add__

    def __neg__(self):
        return Jet({k: -v for k, v in self.c.items()})

    def __sub__(self, o):
        return self + (-o if isinstance(o, Jet) else Jet.const(-Fraction(o)))

    def __rsub__(self, o):
        return (-self) + o

    def __mul__(self, o):
        if not isinstance(o, Jet):
            o = Fraction(o)
            return Jet({k: v * o for k, v in self.c.items()})
        r = {}
        for k1, v1 in self.c.items():
            d1 = sum(k1)
            for k2, v2 in o.c.items():
                if d1 + sum(k2) > DEG:
                    continue
                k = tuple(a + b for a, b in zip(k1, k2))
                r[k] = r.get(k, 0) + v1 * v2
        return Jet(r)

    __rmul__ = __mul__

    def __truediv__(self, x):
        if isinstance(x, Jet):
            return self * x.inv()
        return self * (Fraction(1) / Fraction(x))

    def at0(self):
        return self.c.get((0,) * NV, Fraction(0))

    def d(self, i):
        r = {}
        for k, v in self.c.items():
            if k[i] > 0:
                kk = list(k)
                kk[i] -= 1
                r[tuple(kk)] = r.get(tuple(kk), 0) + v * k[i]
        return Jet(r)

    def inv(self):
        a0 = self.at0()
        assert a0 != 0
        e = (self - a0) * (Fraction(1) / a0)
        tot = Jet.const(1)
        term = Jet.const(1)
        for _ in range(DEG):
            term = term * (-e)
            tot = tot + term
        return tot * (Fraction(1) / a0)


def matinv(g):
    """Inverse of a matrix (list of lists) of Jets via the Neumann series about the value at 0."""
    n = len(g)
    import sympy as sp
    g0 = sp.Matrix(n, n, lambda i, j: sp.Rational(g[i][j].at0().numerator, g[i][j].at0().denominator))
    i0 = g0.inv()
    I0 = [[Jet.const(Fraction(int(sp.fraction(i0[i, j])[0]), int(sp.fraction(i0[i, j])[1])))
           for j in range(n)] for i in range(n)]
    E = [[g[i][j] - g[i][j].at0() for j in range(n)] for i in range(n)]
    M = [[-sum((E[i][k] * I0[k][j] for k in range(n)), Jet()) for j in range(n)] for i in range(n)]
    tot = [row[:] for row in I0]
    term = [row[:] for row in I0]
    for _ in range(DEG):
        term = [[sum((term[i][k] * M[k][j] for k in range(n)), Jet()) for j in range(n)] for i in range(n)]
        tot = [[tot[i][j] + term[i][j] for j in range(n)] for i in range(n)]
    return tot


def geometry(g, u):
    """Christoffels, gradient, Hessian, box u (Jets), Ricci and Riemann at 0, for a metric g (5x5 Jets), function u."""
    n = len(g)
    gi = matinv(g)
    dg = [[[g[a][b].d(c) for c in range(n)] for b in range(n)] for a in range(n)]
    Gam = [[[sum((gi[c][d] * (dg[d][b][a] + dg[d][a][b] - dg[a][b][d]) for d in range(n)), Jet()) * Fraction(1, 2)
             for b in range(n)] for a in range(n)] for c in range(n)]
    du = [u.d(a) for a in range(n)]
    H = [[u.d(a).d(b) - sum((Gam[c][a][b] * du[c] for c in range(n)), Jet()) for b in range(n)] for a in range(n)]
    box = sum((gi[a][b] * H[a][b] for a in range(n) for b in range(n)), Jet())
    G0 = [[[Gam[c][a][b].at0() for b in range(n)] for a in range(n)] for c in range(n)]
    dG0 = [[[[Gam[c][a][b].d(e).at0() for e in range(n)] for b in range(n)] for a in range(n)] for c in range(n)]

    def riem_up(a, b, c, d):            # R^a_bcd = d_c Gam^a_db - d_d Gam^a_cb + Gam^a_ce Gam^e_db - Gam^a_de Gam^e_cb
        return (dG0[a][d][b][c] - dG0[a][c][b][d]
                + sum(G0[a][c][e] * G0[e][d][b] - G0[a][d][e] * G0[e][c][b] for e in range(n)))
    Ric0 = [[sum(riem_up(a, b, a, d) for a in range(n)) for d in range(n)] for b in range(n)]
    gi0 = [[gi[a][b].at0() for b in range(n)] for a in range(n)]
    g0 = [[g[a][b].at0() for b in range(n)] for a in range(n)]
    return dict(gi=gi, gi0=gi0, g0=g0, Gam=Gam, du=du, H=H, box=box, Ric0=Ric0, riem_up=riem_up)


def monomials(nvars_used, deg):
    """exponent tuples of exactly degree deg in the first nvars_used variables."""
    out = []
    for combo in itertools.combinations_with_replacement(range(nvars_used), deg):
        e = [0] * NV
        for i in combo:
            e[i] += 1
        out.append(tuple(e))
    return out


if __name__ == '__main__':
    import random
    import sys
    import sympy as sp
    rng = random.Random(3)
    ys = sp.symbols('z0:%d' % NV)

    def rjet():
        c = {}
        for dgr in range(DEG + 1):
            for m in monomials(3, dgr):
                c[m] = Fraction(rng.randint(-9, 9), rng.randint(1, 5))
        c[(0,) * NV] = Fraction(rng.randint(2, 9), 1)
        return Jet(c)

    def tosym(j):
        return sum(sp.Rational(v.numerator, v.denominator) * sp.prod([y**k for y, k in zip(ys, m)])
                   for m, v in j.c.items())

    def trunc(e, D):
        p = sp.Poly(sp.expand(e), *ys)
        return sum(c * sp.prod([y**k for y, k in zip(ys, m)]) for m, c in p.terms() if sum(m) <= D)
    A, B = rjet(), rjet()
    prod_ok = sp.expand(tosym(A * B) - trunc(tosym(A) * tosym(B), DEG)) == 0
    t = sp.Symbol('t')
    a0 = tosym(A).subs({y: 0 for y in ys})
    ser = sp.series(1 / (a0 + t * (tosym(A) - a0)), t, 0, DEG + 1).removeO().subs(t, 1)
    inv_ok = sp.expand(tosym(A.inv()) - trunc(ser, DEG)) == 0
    DEG -= 1
    ctl = sp.expand(tosym(A * B) - trunc(tosym(A) * tosym(B), DEG + 1)) != 0
    print("J1 product:", prod_ok, " inverse:", inv_ok, " control (truncation one lower misses terms):", ctl)
    ok = prod_ok and inv_ok and ctl
    print("PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
