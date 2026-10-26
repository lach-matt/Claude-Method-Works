#!/usr/bin/env python3
"""harm5.py -- [Hin26] section 2.4 at n = 4 (proof5 Part III.A'): the indicial roots of the Minkowski wave operator
by harmonic type, and the kernels of the symmetric gradient's indicial family, on 4+1 Minkowski.  Labels: computed
(exact, sympy).

On Minkowski in Cartesian coordinates the tensor wave operator box = -eta^{kl} d_k d_l acts componentwise, and on a
static tensor r^-lam u, u homogeneous of degree 0 and of one harmonic type, box(r^-lam u) = r^-lam-2 N(lam) u.  The
bases and the derivative are those of lin5.py (supplement section 10.24): harmonics of C^2 = R^4, z = x1 + i x2,
w = x3 + i x4, S = z^l (scalar), V = z^(l-1) beta (vector), T = z^(l-2) beta (x) beta (tensor), beta = z dw - w dz,
z^p a symbol, so l is symbolic.

  K1 (computed) functions: det N = -(lam + l)(lam - l - 2): the roots -l and l + 2 (n = 3: -l, l + 1).
  K2 (computed) 1-forms, scalar type l: roots {-l, l + 2} (time component, degree l) and {-l + 1, l + 1},
     {-l - 1, l + 3} (spatial components, degrees l - 1 and l + 1); vector type l: {-l, l + 2}, each once.
     Control n = 3: scalar type l gives -l - 1, -l, -l + 1, l, l + 1, l + 2, the example after [Hin26] Definition 2.30.
  K3 (computed) symmetric 2-tensors: scalar, vector and tensor type l; every root is -d or d + 2 for a degree d of a
     Cartesian component, and the determinant is the product over the components.
  K4 (computed) the symmetric gradient's indicial family N(delta*, lam) on 1-forms is injective except at lam = 0 for
     types s0, s1 (translations) and lam = -1 for v1 (rotations): the stationary Killing 1-forms of Minkowski, at every n.

Controls (the selftest runs them): n = 3 reproduces the source's example in K2 and the roots -l, l + 1 in K1; K4's
expected kernels are asserted, so a change in the bases or in delta* that moved them would fail.
"""
import importlib.util, os, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("lin5", os.path.join(HERE, "lin5.py"))
lin5 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lin5)
lam, l, Zs = lin5.lam, lin5.l, lin5.Zs


def box(C, h, sign=1):
    """componentwise -eta^{kl} d_k d_l on a static tensor (h a list for 1-forms, a Matrix for 2-tensors)"""
    if isinstance(h, sp.MatrixBase):
        return sp.Matrix(h.shape[0], h.shape[1],
                         lambda a, b: -sum((C.eta[k, k] if k else sign * C.eta[k, k]) * C.d(C.d(h[a, b], k), k)
                                           for k in range(C.N)))
    return [-sum((C.eta[k, k] if k else sign * C.eta[k, k]) * C.d(C.d(q, k), k) for k in range(C.N)) for q in h]


def dstar1(C, w):
    N, d = C.N, C.d
    return sp.Matrix(N, N, lambda a, b: (d(w[a], b) + d(w[b], a)) / 2)


def Nbox(n, typ, rank, sign=1):
    C = lin5.ctx_of(n, typ)
    B1, B2 = lin5.bases(C, typ)
    B = B1 if rank == 1 else B2
    N, ok = lin5.Nmat(C, B, [box(C, b, sign) for b in B], scale=C.r**2)
    return N, ok


def roots_of(N):
    return sp.factor(lin5.fastdet(N))


def k1(n=4, sign=1):
    C = lin5.Ctx(n, l, l)
    f = Zs
    out = box(C, [f], sign)[0]
    P = lin5.point(C)
    val = sp.factor(sp.cancel(sp.expand((C.r**2 * out).subs(P)) / sp.expand(f.subs(P))))
    return val


def k2(n=4):
    res = {}
    for typ in (["s0", "s1", "sl", "v1", "vl"] if n == 4 else ["s0", "s1", "sl", "v1", "vl"]):
        N, ok = Nbox(n, typ, 1)
        res[typ] = (roots_of(N), ok)
    return res


def k3(n=4):
    res = {}
    for typ in ["s0", "s1", "s2", "v1", "v2", "t2"]:
        N, ok = Nbox(n, typ, 2)
        res[typ] = (roots_of(N), ok)
    return res


def k4(n=4):
    """rank deficiency set of N(delta*, lam): the gcd of the maximal minors of the image matrix"""
    import itertools
    res = {}
    for typ in ["s0", "s1", "s2", "v1", "v2"]:
        C = lin5.ctx_of(n, typ)
        B1, _ = lin5.bases(C, typ)
        P = lin5.point(C)
        ev = lambda q: sp.expand(sp.sympify(q).subs(P))
        cols = []
        for b in B1:
            h = dstar1(C, b)
            cols.append([ev(C.r * h[a, c]) for a in range(C.N) for c in range(a, C.N)])
        M = sp.Matrix(cols).T
        k = M.shape[1]
        g = sp.Integer(0)
        for rows in itertools.combinations(range(M.shape[0]), k):
            mnr = sp.expand(M.extract(list(rows), list(range(k))).det())
            if mnr != 0:
                g = mnr if g == 0 else sp.gcd(g, mnr)
            if g != 0 and sp.degree(g, lam) == 0:
                break
        res[typ] = sp.factor(g)
    return res


def selftest(verbose=False):
    ok = True
    v = k1(4)
    good = sp.simplify(v - (lam + l) * (lam - l - 2)) == 0 or sp.simplify(v + (lam + l) * (lam - l - 2)) == 0
    print("K1 functions n = 4: N =", v, "PASS" if good else "FAIL"); ok &= good
    vc = k1(3)
    good = sp.simplify(vc - (lam + l) * (lam - l - 1)) == 0 or sp.simplify(vc + (lam + l) * (lam - l - 1)) == 0
    print("K1 control n = 3: N =", vc, "PASS" if good else "FAIL"); ok &= good
    r2 = k2(4)
    for typ, (d, cl) in r2.items():
        print("K2 1-forms n = 4", typ, ":", d, "closed" if cl else "NOT CLOSED")
        ok &= cl
    r2c = k2(3)
    d3 = r2c["sl"][0]
    exp3 = sp.expand((lam + l + 1) * (lam + l) * (lam + l - 1) * (lam - l) * (lam - l - 1) * (lam - l - 2))
    good3 = sp.simplify(sp.expand(d3) - exp3) == 0 or sp.simplify(sp.expand(d3) + exp3) == 0
    print("K2 control n = 3, s_l:", d3, "PASS" if good3 else "FAIL"); ok &= good3
    r3 = k3(4)
    for typ, (d, cl) in r3.items():
        print("K3 2-tensors n = 4", typ, ":", d, "closed" if cl else "NOT CLOSED")
        ok &= cl
    r4 = k4(4)
    want = {"s0": lam, "s1": lam, "s2": 1, "v1": lam + 1, "v2": 1}
    for typ, d in r4.items():
        good = sp.simplify(sp.factor(d) / want[typ]).is_number if want[typ] != 1 else sp.degree(d, lam) == 0
        print("K4 N(delta*, lam) n = 4", typ, ": gcd of maximal minors", d, "PASS" if good else "FAIL"); ok &= bool(good)
    print("selftest:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    sys.exit(0 if selftest("-v" in sys.argv) else 1)
