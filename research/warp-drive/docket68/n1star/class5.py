#!/usr/bin/env python3
"""class5.py -- the T^2-mirror class in [Hin26]'s construction (N1STAR-PROOF.md section 10.43; ROUTES 4.45; D111).

The class is G = O(2) x O(2) acting on R^4 = R^2 x R^2 (the rotations of the (x1, x2) and (x3, x4) planes and the
reflections x2 -> -x2, x4 -> -x4), extended trivially in t.  Which of the objects [Hin26] removes step by step are
G-invariant decides which of his steps survive in the class.

  C1 (computed, exact) The generators.  Of the fifteen Killing fields of 4+1 Minkowski -- d_t, the four d_i, the four
     boosts t d_i + x^i d_t, the six rotations x^a d_b - x^b d_a -- the G-invariant combinations are the multiples of
     d_t alone; Tangherlini's mass change mu' r^-2 (dt + dr)^2 is G-invariant.  Control: under T^2 alone, without the
     reflections, the invariant generators are d_t and the two rotations of the planes, three.
  C2 (computed, exact) The harmonics of S^3 in the class, l <= 8.  Scalar: one G-invariant harmonic at each even l,
     none at odd l.  Vector (divergence-free): none at any l, the invariant 1-forms being a(theta) d theta, whose
     divergence-free ones are singular at both axes.  Tensor (transverse traceless, (rough Laplacian + l(l + 2) - 2) T =
     0): one G-invariant harmonic at each even l >= 2, none at odd l, on the invariant ansatz T = A d theta^2 + B
     cos^2 theta d phi1^2 + C sin^2 theta d phi2^2, C = -A - B, with A, B polynomials in cos^2 theta, smooth at both
     axes; each equation imposed exactly at 48 rational points of the circle.  Controls: under T^2 alone the vector
     type has the plane rotations' duals; the eigenvalue moved by one empties the tensor table.
  C3 (computed, exact upper bounds) The same counts by a second method: the harmonics of S^3 at level l as homogeneous
     degree-l polynomials on R^4 (scalar: harmonic; 1-form: harmonic, divergence-free, x.V = 0; symmetric tensor:
     harmonic, divergence-free, traceless, x.H = 0), invariance as linear conditions, ranks mod 2^31 - 1 (a nullity
     mod p bounds the nullity over Q from above).  All harmonics: SO(4)'s (l + 1)^2, 2 l (l + 2), 2 (l - 1)(l + 3) for
     l <= 8; the G-invariant ones: C2's counts, so C2's ansatz, which exhibits its solutions (a lower bound), misses
     none.  Controls: T^2 alone, two divergence-free 1-forms at each odd l and two TT tensors at each even l >= 2;
     x.H = 0 dropped, the totals break.

Run: python3 class5.py --selftest | --mutants | --only k [--verbose]   (about forty seconds).
"""
import itertools
import sys
import time

import sympy as sp

from damping5 import Checklist

t, x1, x2, x3, x4 = sp.symbols("t x1 x2 x3 x4", real=True)
X = (t, x1, x2, x3, x4)
K1 = (0, -x2, x1, 0, 0)                     # rotation of the (x1, x2) plane
K2 = (0, 0, 0, -x4, x3)                     # rotation of the (x3, x4) plane
R2 = {x2: -x2}
R4 = {x4: -x4}


def nullity(eqs, unknowns):
    """the dimension of the solution space of a homogeneous linear system"""
    eqs = [e for e in eqs if e != 0]
    if not eqs:
        return len(unknowns)
    M, _ = sp.linear_eq_to_matrix(eqs, list(unknowns))
    return len(unknowns) - M.rank()


def bracket(A, B):
    return tuple(sp.expand(sum(A[j] * sp.diff(B[i], X[j]) - B[j] * sp.diff(A[i], X[j]) for j in range(5)))
                 for i in range(5))


def push(V, refl):
    """pushforward of a vector field by a reflection x_k -> -x_k (an involution)"""
    k = X.index(list(refl)[0])
    return tuple(sp.expand((-1 if i == k else 1) * V[i].subs(refl, simultaneous=True)) for i in range(5))


def generators():
    e = [tuple(1 if i == j else 0 for i in range(5)) for j in range(5)]
    gens = [e[0]] + e[1:]
    for i in range(1, 5):                                            # boosts t d_i + x^i d_t
        gens.append(tuple(X[i] if j == 0 else (t if j == i else 0) for j in range(5)))
    for a in range(1, 5):                                            # rotations x^a d_b - x^b d_a
        for b in range(a + 1, 5):
            gens.append(tuple(-X[b] if j == a else (X[a] if j == b else 0) for j in range(5)))
    return gens


def invariant_dim(gens, reflections=True):
    c = sp.symbols(f"c0:{len(gens)}")
    V = tuple(sum(c[k] * gens[k][i] for k in range(len(gens))) for i in range(5))
    eqs = []
    conds = [bracket(K1, V), bracket(K2, V)]
    if reflections:
        conds += [tuple(a - b for a, b in zip(push(V, R2), V)), tuple(a - b for a, b in zip(push(V, R4), V))]
    for comp in conds:
        for e in comp:
            eqs += sp.Poly(e, *X).coeffs()
    sol = sp.linsolve(eqs, c)
    (s,) = list(sol)
    free = set().union(*[sp.sympify(v).free_symbols for v in s]) & set(c)
    return len(free), [k for k in range(len(gens)) if c[k] in free]


def c1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    gens = generators()
    chk("fifteen Killing fields of 4+1 Minkowski", len(gens) == 15)
    d, which = invariant_dim(gens, reflections=(control != 1))
    chk(f"G-invariant generators: {d}, the time translation alone (indices {which})", d == 1 and which == [0])
    dT, whichT = invariant_dim(gens, reflections=False)
    chk(f"control: under T^2 alone {dT} (d_t and the two plane rotations, indices {whichT})",
        dT == 3 and whichT == [0, 9, 14])
    r = sp.sqrt(x1**2 + x2**2 + x3**2 + x4**2)
    k = [1] + [X[i] / r for i in range(1, 5)]                      # dt + dr
    h = sp.Matrix(5, 5, lambda i, j: k[i] * k[j] / r**2)
    ok = True
    for V in (K1, K2):
        J = sp.Matrix(5, 5, lambda i, j: sp.diff(V[i], X[j]))
        L = sp.Matrix(5, 5, lambda i, j: sum(V[m] * sp.diff(h[i, j], X[m]) for m in range(5))) + J.T * h + h * J
        ok &= all(sp.simplify(e) == 0 for e in L)
    for refl in (R2, R4):
        kk = X.index(list(refl)[0])
        S = sp.diag(*[(-1 if i == kk else 1) for i in range(5)])
        ok &= all(sp.simplify(e) == 0 for e in (S * h.subs(refl, simultaneous=True) * S - h))
    chk("Tangherlini's mass change r^-2 (dt + dr)^2 is G-invariant", ok)
    return chk.ok


# ------------------------------------------------------------------------------------------------- C2
th, s = sp.symbols("theta s", positive=True)
cth, sth = sp.cos(th), sp.sin(th)
GAM = sp.diag(1, cth**2, sth**2)                                  # round S^3: (theta, phi1, phi2)
Y = (th, sp.Symbol("p1"), sp.Symbol("p2"))
GINV = GAM.inv()
CH = [[[sp.simplify(sum(GINV[a, d] * (sp.diff(GAM[d, b], Y[c]) + sp.diff(GAM[d, c], Y[b]) - sp.diff(GAM[b, c], Y[d]))
                        for d in range(3)) / 2) for c in range(3)] for b in range(3)] for a in range(3)]


def cov2(T):
    """nabla_k T_ij of a symmetric 2-tensor whose components depend on theta only"""
    return [[[sp.diff(T[i, j], Y[k]) - sum(CH[m][k][i] * T[m, j] + CH[m][k][j] * T[i, m] for m in range(3))
              for k in range(3)] for j in range(3)] for i in range(3)]


def lap2(T):
    D = cov2(T)
    def DD(i, j, k, l):
        v = sp.diff(D[i][j][k], Y[l])
        v -= sum(CH[m][l][i] * D[m][j][k] + CH[m][l][j] * D[i][m][k] + CH[m][l][k] * D[i][j][m] for m in range(3))
        return v
    return sp.Matrix(3, 3, lambda i, j: sum(GINV[k, l] * DD(i, j, k, l) for k in range(3) for l in range(3)))


def div2(T):
    D = cov2(T)
    return [sum(GINV[i, k] * D[i][j][k] for i in range(3) for k in range(3)) for j in range(3)]


def rational(e):
    """theta -> the rational parameterization cos = (1 - s^2)/(1 + s^2), sin = 2 s/(1 + s^2); numerator"""
    e = e.subs({sp.cos(th): (1 - s**2) / (1 + s**2), sp.sin(th): 2 * s / (1 + s**2)})
    return sp.numer(sp.together(sp.expand(e)))


_ODE = {}


def _ode():
    """the invariant TT conditions, derived once for T = diag(A, B cos^2, -(A + B) sin^2) with A, B unknown functions"""
    if not _ODE:
        A, B = sp.Function("A")(th), sp.Function("B")(th)
        T = sp.diag(A, B * cth**2, (-A - B) * sth**2)
        lp = lap2(T)
        _ODE.update(A=A, B=B, div=[sp.simplify(e) for e in div2(T)], lap=[sp.simplify(lp[i, i]) for i in range(3)],
                    T=[T[i, i] for i in range(3)],
                    off=[sp.simplify(lp[i, j]) for i in range(3) for j in range(3) if i != j])
    return _ODE


def tensor_count(l, deg, ev=None, npts=48, smooth=True):
    """invariant TT harmonics with (rough Laplacian + ev) T = 0, ev = l(l + 2) - 2 unless given.  A, B polynomials of
    degree deg in c = cos^2 theta; each equation, a trigonometric polynomial of bounded degree once cleared of its
    denominator, is imposed exactly at npts rational points (cos, sin) = ((1 - u^2)/(1 + u^2), 2u/(1 + u^2)) of the
    circle -- more points than twice its degree, so it holds identically"""
    ev = l * (l + 2) - 2 if ev is None else ev
    O = _ode()
    A, B = O["A"], O["B"]
    a = sp.symbols(f"a0:{deg + 1}")
    b = sp.symbols(f"b0:{deg + 1}")
    cc = sp.Symbol("cc")
    Ac = sum(a[k] * cc**k for k in range(deg + 1))
    Bc = sum(b[k] * cc**k for k in range(deg + 1))
    y0, y1, y2, z0, z1, z2 = sp.symbols("y0 y1 y2 z0 z1 z2")
    exprs = list(O["div"]) + [O["lap"][i] + ev * O["T"][i] for i in range(3)]
    sub = {sp.Derivative(A, (th, 2)): y2, sp.Derivative(B, (th, 2)): z2}
    sub1 = {sp.Derivative(A, th): y1, sp.Derivative(B, th): z1}
    exprs = [sp.expand_trig(e.subs(sub).subs(sub1).subs({A: y0, B: z0})) for e in exprs]
    eqs = []
    for k in range(1, npts + 1):
        u = sp.Rational(k, npts + 1)
        cv, sv = (1 - u**2) / (1 + u**2), 2 * u / (1 + u**2)
        c = cv**2
        d1 = -2 * sv * cv                                 # d c / d theta
        d2 = -2 * (2 * c - 1)                             # d^2 c / d theta^2
        vals = {y0: Ac.subs(cc, c), z0: Bc.subs(cc, c),
                y1: sp.diff(Ac, cc).subs(cc, c) * d1, z1: sp.diff(Bc, cc).subs(cc, c) * d1,
                y2: sp.diff(Ac, cc, 2).subs(cc, c) * d1**2 + sp.diff(Ac, cc).subs(cc, c) * d2,
                z2: sp.diff(Bc, cc, 2).subs(cc, c) * d1**2 + sp.diff(Bc, cc).subs(cc, c) * d2}
        for e in exprs:
            v = e.subs({sp.cos(th): cv, sp.sin(th): sv, sp.tan(th): sv / cv}).subs(vals)
            v = sp.expand(v)
            if v != 0:
                eqs.append(v)
    if smooth:
        eqs += [(Ac - Bc).subs(cc, 0), (Ac - (-Ac - Bc)).subs(cc, 1)]     # smooth at cos = 0 and at sin = 0
    return nullity(eqs, list(a) + list(b))


def scalar_count(l):
    if l % 2:
        return 0
    m = l // 2
    q = sp.symbols(f"q0:{m + 1}")
    u, v = x1**2 + x2**2, x3**2 + x4**2
    f = sum(q[k] * u**k * v**(m - k) for k in range(m + 1))
    lap = sum(sp.diff(f, xx, 2) for xx in (x1, x2, x3, x4))
    eqs = sp.Poly(sp.expand(lap), x1, x2, x3, x4).coeffs() if lap != 0 else []
    return nullity(eqs, q)


def vector_count(reflections=True):
    """smooth divergence-free invariant 1-forms on S^3 (any l).  With the reflections the invariant 1-forms are
    a(theta) d theta, divergence-free only for a = C/sin 2 theta, singular at both axes: 0.  Without them the plane
    rotations' duals cos^2 theta d phi1 and sin^2 theta d phi2 are invariant, smooth and divergence-free: 2."""
    if reflections:
        A = sp.Function("A")(th)
        a = sp.dsolve(sp.Eq(sp.diff(cth * sth * A, th), 0), A).rhs
        C1 = [x for x in a.free_symbols if x != th][0]
        singular = sp.limit(sp.Abs(a.subs(C1, 1)), th, 0) == sp.oo and sp.limit(sp.Abs(a.subs(C1, 1)), th, sp.pi / 2,
                                                                               "-") == sp.oo
        return 0 if singular else None
    n = 0
    for w in (sp.Matrix([0, cth**2, 0]), sp.Matrix([0, 0, sth**2])):
        n += sp.simplify(sum(sp.diff(sp.sqrt(GAM.det()) * (GINV * w)[i], Y[i]) for i in range(3))) == 0
    return n


def c2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    sc = {l: scalar_count(l) for l in range(0, 9)}
    chk(f"scalar: G-invariant harmonics per l <= 8 {sc}", sc == {l: (1 if l % 2 == 0 else 0) for l in range(0, 9)})
    vc = vector_count(reflections=(control != 1))
    chk(f"vector: G-invariant smooth divergence-free 1-forms {vc} (T^2 alone: {vector_count(False)})", vc == 0)
    shift = 1 if control == 2 else 0
    tc = {l: tensor_count(l, l // 2 + 1, ev=l * (l + 2) - 2 + shift) for l in range(2, 9)}
    chk(f"tensor: G-invariant TT harmonics per 2 <= l <= 8 {tc}", tc == {l: (1 if l % 2 == 0 else 0) for l in tc})
    chk("tensor: none at a wrong eigenvalue (l(l + 2) - 1 at l = 2, 4); off-diagonal parts of the Laplacian zero",
        _offshell(2) == 0 and _offshell(4) == 0 and all(e == 0 for e in _ode()["off"]))
    return chk.ok


def _offshell(l):
    """the count with the eigenvalue shifted by one: must be 0"""
    return tensor_count(l, l // 2 + 1, ev=l * (l + 2) - 1)


# ------------------------------------------------------------------------------------------------- C3
PR = 2**31 - 1


def nullity_mod(rows, n):
    """n minus the rank mod PR of sparse rows {col: coeff}: an upper bound on the nullity over Q"""
    piv = {}
    for r in rows:
        r = {c: a % PR for c, a in r.items() if a % PR}
        while r:
            c = min(r)
            if c not in piv:
                inv = pow(r[c], PR - 2, PR)
                piv[c] = {k: v * inv % PR for k, v in r.items()}
                break
            p, a = piv[c], r[c]
            for k, v in p.items():
                w = (r.get(k, 0) - a * v) % PR
                if w:
                    r[k] = w
                else:
                    r.pop(k, None)
    return n - len(piv)


def ambient(kind, l, inv, drop=None):
    """harmonics of S^3 at level l as homogeneous degree-l polynomials on R^4 -- scalar f, Delta f = 0; 1-form V,
    Delta V = 0, div V = 0, x.V = 0; symmetric H, Delta H = 0, div H = 0, tr H = 0, x.H = 0 -- invariant under G (inv
    'G'), the rotations alone ('T2') or nothing ('none'); the count mod PR, an upper bound"""
    comps = {"s": [()], "v": [(i,) for i in range(4)], "t": [(i, j) for i in range(4) for j in range(i, 4)]}[kind]
    ms = [m for m in itertools.product(range(l + 1), repeat=4) if sum(m) == l]
    key = lambda c: tuple(sorted(c))
    idx = {(c, m): k for k, (c, m) in enumerate((c, m) for c in comps for m in ms)}
    rows = []

    def acc(P, mono, c, m, a):
        d = P.setdefault(mono, {})
        d[idx[(key(c), m)]] = d.get(idx[(key(c), m)], 0) + a

    def shift(m, k, s):
        mm = list(m)
        mm[k] += s
        return tuple(mm)

    def emit(P):
        rows.extend(v for v in P.values() if any(v.values()))

    for c in comps:
        P = {}
        for m in ms:
            for k in range(4):
                if m[k] >= 2:
                    acc(P, shift(m, k, -2), c, m, m[k] * (m[k] - 1))
        emit(P)
    for j in range(4) if kind != "s" else ():
        cs = [(i,) for i in range(4)] if kind == "v" else [(i, j) for i in range(4)]
        P, Q = {}, {}
        for i, c in enumerate(cs):
            for m in ms:
                if m[i]:
                    acc(P, shift(m, i, -1), c, m, m[i])
                acc(Q, shift(m, i, 1), c, m, 1)
        emit(P)
        if drop != "x":
            emit(Q)
        if kind == "v":
            break
    if kind == "t":
        P = {}
        for i in range(4):
            for m in ms:
                acc(P, m, (i, i), m, 1)
        emit(P)
    for a, b in ((0, 1), (2, 3)) if inv != "none" else ():
        for c in comps:                                 # L_xi, xi = x_a d_b - x_b d_a
            P = {}
            for m in ms:
                for p, q, s in ((a, b, 1), (b, a, -1)):
                    if m[q]:
                        acc(P, shift(shift(m, q, -1), p, 1), c, m, s * m[q])
            for slot, i in enumerate(c):
                for k, s in ((b, 1 if i == a else 0), (a, -1 if i == b else 0)):
                    if s:
                        cc = list(c)
                        cc[slot] = k
                        for m in ms:
                            acc(P, m, tuple(cc), m, s)
            emit(P)
    if inv == "G":                                      # x2 -> -x2 and x4 -> -x4, each
        rows += [{k: 1} for (c, m), k in idx.items() if any((m[r] + c.count(r)) % 2 for r in (1, 3))]
    return nullity_mod(rows, len(idx))


def c3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    drop = "x" if control == 2 else None
    dims = {"s": lambda l: (l + 1)**2, "v": lambda l: 2 * l * (l + 2), "t": lambda l: 2 * (l - 1) * (l + 3)}
    tot = {kd: [ambient(kd, l, "none", drop) for l in range(1, 9)] for kd in "svt"}
    chk(f"the model: all harmonics per 1 <= l <= 8 {tot}, SO(4)'s (l + 1)^2, 2 l (l + 2), 2 (l - 1)(l + 3)",
        all(tot[kd] == [dims[kd](l) for l in range(1, 9)] for kd in "svt"))
    inv = "T2" if control == 1 else "G"
    g = {kd: [ambient(kd, l, inv) for l in range(0 if kd == "s" else 1, 9)] for kd in "svt"}
    want = {"s": [1 - l % 2 for l in range(9)], "v": [0] * 8, "t": [(1 - l % 2) * (l >= 2) for l in range(1, 9)]}
    chk(f"G-invariant, upper bounds meeting C2's: scalar l = 0..8 {g['s']}, vector l = 1..8 {g['v']}, tensor {g['t']}",
        g == want)
    t2 = {kd: [ambient(kd, l, "T2") for l in range(1, 9)] for kd in "vt"}
    chk(f"control: T^2 alone, vector l = 1..8 {t2['v']} (two at odd l), tensor {t2['t']} (two at even l)",
        t2 == {"v": [2 * (l % 2) for l in range(1, 9)], "t": [2 * (1 - l % 2) * (l >= 2) for l in range(1, 9)]})
    return chk.ok


CHECKS = [("C1 the generators: G-invariant Killing fields d_t alone (T^2 alone: three); the mass change invariant", c1),
          ("C2 the harmonics in the class: scalar and tensor one at each even l, vector none (l <= 8)", c2),
          ("C3 the same counts as upper bounds: ambient harmonic polynomials, ranks mod p; T^2 alone 2 and 2", c3)]


def run(only=None, verbose=False):
    ok = True
    for k, (name, f) in enumerate(CHECKS, 1):
        if only and k != only:
            continue
        t0 = time.time()
        res = f(0, verbose)
        ok &= res
        print(f"{name[:104]:<104} {'PASS' if res else 'FAIL'} {time.time() - t0:3.0f}s", flush=True)
    print(f"class5.py: {sum(1 for _ in CHECKS) if ok else 'not all'}/{len(CHECKS)}")
    return ok


def mutants():
    caught = 0
    total = 0
    for name, f in CHECKS:
        for k in (1, 2):
            if f is c1 and k == 2:
                continue
            total += 1
            res = f(k, False)
            caught += not res
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"class5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    v = "--verbose" in args
    if "--selftest" in args:
        sys.exit(0 if run(verbose=v) else 1)
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    elif "--only" in args:
        sys.exit(0 if run(int(args[args.index("--only") + 1]), v) else 1)
    print(__doc__)
