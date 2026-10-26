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
  K5 (computed) [Hin26] Lemma 2.29 at general N (proof5 Part III.A' Lemma 2.1): the operators box, delta* and delta in
     the null splittings, reduced by type with Part III.A' Lemma 1.5's identities (formula), equal entry by entry the
     matrices of the Cartesian componentwise operators on the splitting's basis of each type (cartesian), at N = 2 and
     N = 3, for s0, s1, s2, sl, v1, v2, vl and (N = 3) t2, tl, l symbolic.
  K6 (computed) the determinants of the type-wise matrices of box at N = 3 factor as prod (lam + d)(lam - d - 2) over
     the degree lists of Part III.A' Lemma 2.3.

Controls (the selftest runs them): n = 3 reproduces the source's example in K2 and the roots -l, l + 1 in K1; K4's
expected kernels are asserted, so a change in the bases or in delta* that moved them would fail; K5 at N = 2 is the
source's Lemma 2.29, and the N = 2 formula held against the N = 3 computation (s1, box on 1-forms) must fail.

python3 harm5.py [--selftest]   (about 30 minutes, most of it K5 on symmetric 2-tensors)
"""
import importlib.util, os, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
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


# --------------------------------------------------------------------- Lemma 2.29 at general N, reduced by type
def ang(N, k2, op, name):
    """an angular operator on one harmonic of a type (Lemma 1.2 of Part III.A'): returns {name: coefficient}"""
    R = {("d", "S"): {"dS": 1},
         ("delta", "dS"): {"S": k2}, ("delta", "gS"): {"dS": -1}, ("delta", "hS"): {"dS": (N - 1) * (k2 - N) / N},
         ("delta", "V"): {}, ("delta", "dV"): {"V": (k2 - N) / 2}, ("delta", "T"): {},
         ("tr", "gS"): {"S": N}, ("tr", "hS"): {}, ("tr", "dV"): {}, ("tr", "T"): {},
         ("g", "S"): {"gS": 1},
         ("dstar", "dS"): {"hS": 1, "gS": -k2 / N}, ("dstar", "V"): {"dV": 1},
         ("lap", "S"): {"S": k2}, ("lap", "dS"): {"dS": k2 - N + 1}, ("lap", "gS"): {"gS": k2},
         ("lap", "hS"): {"hS": k2 - 2 * N}, ("lap", "V"): {"V": k2 - 1}, ("lap", "dV"): {"dV": k2 - N - 2},
         ("lap", "T"): {"T": k2 - 2}}
    return R[(op, name)]


def opmats(N):
    """the operators of Lemma 2.29 in the splittings, at general N: entries are lists of (coefficient, op or None)"""
    c, L = lambda x: [(x, None)], lam
    dg = lambda m: [(-L**2 + (N - 1) * L + m, None), (1, "lap")]
    Z = []
    box1 = [[dg(N / 2), c(-N / 2), [(-1, "delta")]],
            [c(-N / 2), dg(N / 2), [(1, "delta")]],
            [[(-2, "d")], [(2, "d")], dg(1)]]
    box2 = [[dg(N), c(-N), [(-2, "delta")], Z, Z, [(-sp.Rational(1, 2), "tr")]],
            [c(-N / 2), dg(N), [(1, "delta")], c(-N / 2), [(-1, "delta")], [(sp.Rational(1, 2), "tr")]],
            [[(-2, "d")], [(2, "d")], dg((N + 4) / 2), Z, c(-(N + 2) / 2), [(-1, "delta")]],
            [Z, c(-N), Z, dg(N), [(2, "delta")], [(-sp.Rational(1, 2), "tr")]],
            [Z, [(-2, "d")], c(-(N + 2) / 2), [(2, "d")], dg((N + 4) / 2), [(1, "delta")]],
            [[(-2, "g")], [(4, "g")], [(-4, "dstar")], [(-2, "g")], [(4, "dstar")], dg(2)]]
    ds = [[c(-L / 2), Z, Z], [c(L / 4), c(-L / 4), Z], [[(sp.Rational(1, 2), "d")], Z, c(-(L + 1) / 4)],
          [Z, c(L / 2), Z], [Z, [(sp.Rational(1, 2), "d")], c((L + 1) / 4)], [[(1, "g")], [(-1, "g")], [(1, "dstar")]]]
    de = [[c(L - N), c(-L + N), [(1, "delta")], Z, Z, [(sp.Rational(1, 2), "tr")]],
          [Z, c(L - N), Z, c(-L + N), [(1, "delta")], [(-sp.Rational(1, 2), "tr")]],
          [Z, Z, c(L - N - 1), Z, c(-L + N + 1), [(1, "delta")]]]
    return {"box1": box1, "box2": box2, "dstar": ds, "delta": de}


SLOTS1 = {"s0": [(0, "S"), (1, "S")], "s1": [(0, "S"), (1, "S"), (2, "dS")], "v": [(2, "V")]}
SLOTS2 = {"s0": [(0, "S"), (1, "S"), (3, "S"), (5, "gS")],
          "s1": [(0, "S"), (1, "S"), (2, "dS"), (3, "S"), (4, "dS"), (5, "gS")],
          "s2": [(0, "S"), (1, "S"), (2, "dS"), (3, "S"), (4, "dS"), (5, "gS"), (5, "hS")],
          "v1": [(2, "V"), (4, "V")], "v2": [(2, "V"), (4, "V"), (5, "dV")], "t": [(5, "T")]}


def slots(typ, rank):
    deg = typ[1:]
    if rank == 1:
        return SLOTS1["v" if typ[0] == "v" else ("s0" if deg == "0" else "s1")]
    if typ[0] == "t":
        return SLOTS2["t"]
    if typ[0] == "v":
        return SLOTS2["v1" if deg == "1" else "v2"]
    return SLOTS2[{"0": "s0", "1": "s1"}.get(deg, "s2")]


def formula(N, typ, op):
    """the type-wise matrix of op ('box1', 'box2', 'dstar', 'delta') from the operator form and Lemma 1.2"""
    deg = {"0": 0, "1": 1, "2": 2}.get(typ[1:], l)
    k2 = deg * (deg + N - 1)
    absent = {"s": {0: {"dS", "hS"}, 1: {"hS"}}, "v": {1: {"dV"}}}.get(typ[0], {}).get(deg, set())
    M = opmats(sp.Integer(N))[op]
    rin = 1 if op in ("box1", "dstar") else 2
    sin, sout = slots(typ, rin), slots(typ, 2 if op in ("box2", "dstar") else 1)
    A = sp.zeros(len(sout), len(sin))
    for j, (cj, nj) in enumerate(sin):
        for i, (ci, ni) in enumerate(sout):
            tot = 0
            for coef, o in M[ci][cj]:
                img = {nj: 1} if o is None else ang(sp.Integer(N), k2, o, nj)
                tot += coef * sum(v for nm, v in img.items() if nm == ni and nm not in absent)
            A[i, j] = sp.expand(tot)
    return A


def cart_basis(C, typ, rank):
    """the splitting's basis of one type as Cartesian tensors (lin5's degree-normalised fields)"""
    n, r, S = C.n, C.r, Zs
    xr = [xi / r for xi in C.x]
    if typ[0] == "t":
        return lin5.tbasis2(C)
    if typ[0] == "v":
        G = lin5.vfield(C)
        if rank == 1:
            return [[0] + G]
        sym = sp.Matrix(n, n, lambda i, j: xr[i] * G[j] + xr[j] * G[i])
        B = [lin5.embed(C, t0=G, spatial=sym), lin5.embed(C, t0=G, spatial=-sym)]
        if typ[1:] != "1":
            B.append(lin5.vbasis2(C)[2])
        return B
    deg = typ[1:]
    G = lin5.sgrad(C) if deg != "0" else None
    if rank == 1:
        B = [[S] + [S * q for q in xr], [S] + [-S * q for q in xr]]
        return B + ([[0] + G] if G else [])
    XX = sp.Matrix(n, n, lambda i, j: xr[i] * xr[j])
    Pi = sp.eye(n) - XX
    Ea = lin5.embed(C, tt=S, t0=[S * q for q in xr], spatial=S * XX)
    Eb = lin5.embed(C, tt=2 * S, spatial=-2 * S * XX)
    Ee = lin5.embed(C, tt=S, t0=[-S * q for q in xr], spatial=S * XX)
    Ep = lin5.embed(C, spatial=S * Pi)
    if deg == "0":
        return [Ea, Eb, Ee, Ep]
    sym = sp.Matrix(n, n, lambda i, j: xr[i] * G[j] + xr[j] * G[i])
    Ec, Ef = lin5.embed(C, t0=G, spatial=sym), lin5.embed(C, t0=G, spatial=-sym)
    B = [Ea, Eb, Ec, Ee, Ef, Ep]
    if deg != "1":
        B.append(lin5.sbasis2(C)[-1])
    return B


def cartesian(n, typ, op):
    C = lin5.ctx_of(n, typ)
    rin = 1 if op in ("box1", "dstar") else 2
    rout = 2 if op in ("box2", "dstar") else 1
    Bin, Bout = cart_basis(C, typ, rin), cart_basis(C, typ, rout)
    if op in ("box1", "box2"):
        outs, sc = [box(C, b) for b in Bin], C.r**2
    elif op == "dstar":
        outs, sc = [dstar1(C, b) for b in Bin], C.r
    else:
        outs, sc = [lin5.delta(C, b) for b in Bin], C.r
    return lin5.Nmat(C, Bout, outs, scale=sc)


def k5(n, ops=("box1", "box2", "dstar", "delta")):
    """Lemma 2.29 at N = n - 1: the operator form reduced by type against the Cartesian computation, entry by entry"""
    types = ["s0", "s1", "s2", "sl", "v1", "v2", "vl"] + (["t2", "tl"] if n == 4 else [])
    out = []
    for typ in types:
        for op in ops:
            if typ[0] == "t" and op != "box2":
                continue
            F = formula(n - 1, typ, op)
            Cm, closed = cartesian(n, typ, op)
            diff = (F - Cm).applyfunc(lambda q: sp.simplify(q))
            out.append((typ, op, closed and diff == sp.zeros(*F.shape), F))
    return out


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
    for n in (3, 4):
        for typ, op, good, _ in k5(n):
            print("K5 Lemma 2.1 at N =", n - 1, typ, op, ": formula = Cartesian", "PASS" if good else "FAIL")
            ok &= good
    F2, (C3, _) = formula(2, "s1", "box1"), cartesian(4, "s1", "box1")
    good = (F2 - C3).applyfunc(sp.simplify) != sp.zeros(*F2.shape)
    print("K5 control: the N = 2 formula against the N = 3 computation differs", "PASS" if good else "FAIL"); ok &= good
    D = {("s0", "box1"): [0, 1], ("s1", "box1"): [0, 1, 2], ("s2", "box1"): [1, 2, 3], ("sl", "box1"): [l - 1, l, l + 1],
         ("v1", "box1"): [1], ("v2", "box1"): [2], ("vl", "box1"): [l],
         ("s0", "box2"): [0, 0, 1, 2], ("s1", "box2"): [0, 1, 1, 1, 2, 3], ("s2", "box2"): [0, 1, 2, 2, 2, 3, 4],
         ("sl", "box2"): [l - 2, l - 1, l, l, l, l + 1, l + 2], ("v1", "box2"): [1, 2], ("v2", "box2"): [1, 2, 3],
         ("vl", "box2"): [l - 1, l, l + 1], ("t2", "box2"): [2], ("tl", "box2"): [l]}
    for (typ, op), degs in D.items():
        det = sp.factor(formula(3, typ, op).det())
        want = sp.prod([(lam + d) * (lam - d - 2) for d in degs])
        good = sp.simplify(det / want).is_number and sp.simplify(det / want) != 0
        print("K6 det", typ, op, "= c prod (lam + d)(lam - d - 2), d in", degs, "PASS" if good else "FAIL"); ok &= good
    print("selftest:", "PASS" if ok else "FAIL")
    return ok


if __name__ == "__main__":
    sys.exit(0 if selftest("-v" in sys.argv) else 1)
