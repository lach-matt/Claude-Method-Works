#!/usr/bin/env python3
"""seed_second.py -- item 530 (SOURCE continued): the second order of the record's own equations at 2w, exact.

M, 530: "Yes , b please" -- route (b) of the 527 report: derive the second-order source symbolically from the record's
own equations, expanded about Tangherlini with the l = 2 seed wave squared, and solve for the outgoing amplitude at
2w; the exact coupling in place of seed_types T7's model couplings.  Labels: computed (exact unless marked), READ,
deduced, estimate, M's.

  Q0 (M's) 530, verbatim.
  Q1 (computed, exact) The record's equations to second order.  hf_mirror5's class in kn_gauge's K1 form -- the 2+1
     reduction h = rho^2 g3 with the Bondi conditions h_rr = h_rth = 0, h_thth = rho^2 r^2, the two scalars psi =
     ln rho + dpsi and omega = (1/2) ln(cot th) + domega, R[h]_ab = (3/2) dpsi dpsi + 2 domega domega, box psi =
     box omega = 0 -- expanded about Tangherlini (mu = 1) to order eps^2 by sympy, the order-0 identically zero.  The
     fields are modes in x = cos 2 th: dpsi = sum Ps_n P_n, domega = sum Om_n P_n, h_vv, h_vr = rho^2 sum A_n P_n,
     rho^2 sum B_n P_n, h_vth = rho^2 sin 2 th sum C_n P_n; each equation is multiplied by the polynomial that clears its
     denominators, divided by the common factor of its rows and projected exactly on P_m; the same multiplier is applied
     to the quadratic terms, every coefficient reduced to lowest terms in x and sin 2 th before it is evaluated (the raw
     sums carry powers to 1/sin^23 2 th that cancel only together).  In the frequency domain (e^-i w v) the main
     equations rr, r th, th th, box psi, box omega give the radial system; v th and v v are the supplementary conditions
     (Bondi's lemma: imposed at one radius, they hold at every radius -- checked); v r is the trivial one.
  Q2 (computed, exact) The l = 2 waves in the record's own variables.  The tensor type is Ps = -1/2, Om = -(3/4) x,
     the scalar type Ps = (2/3) x, Om = 1 (from Kodama-Ishibashi's harmonics on S^3 with both circles' charges zero;
     the record's own F and G polarizations without their h(x) are exactly -F/3 of the one and -F/4 of the other);
     at second order the products reach l' = 4 and n <= 2, so three modes close the tower exactly.  Regular at the
     horizon (the 2 NM exponents -1 + i w excluded), the supplementary rows at r = 2, the incoming amplitudes by a
     Hann-windowed projection on r^-3/2 over [R/2, R], the residual gauge (2 NM directions) fixed by the least h_vv,
     h_vr, h_vth at R; the outgoing projection on r^-3/2 e^{2 i w r*} is gauge-clean to 1e-15 (Q5).
  Q3 (computed, exact) Validation.  The l = 2 reflection of each type reproduces Kodama and Ishibashi's barrier
     (seed_escape's V_T, seed_types' V_S) at x = w r_h = 1.0, 1.5, 2.1, 2.5: tensor 0.557119 at 1.5, 8.28849e-3 at
     2.1, 3.73881e-4 at 2.5; scalar 1.81518e-3 at 1.5, 2.2326e-6 at 2.1 -- ratios 1.0000 (the scalar at 2.1 1.0009),
     the modes pure to 1e-6, the supplementary rows holding at R/2 to 1e-11.  The record's equations are linearized
     five-dimensional gravity mode by mode, and the mode identification is exact.
  Q4 (computed, exact) The second order.  The quadratic source at 2w from the first-order solution (its complex
     amplitude u e^-i w v; the 2w part of a product of real fields is (1/2) Q(u, u)); the driven radial system at 2w
     with the particular solution from the horizon, no incoming wave at 2w, the supplementary rows with their sources,
     the gauge fixed as before; the escaping fraction C = P_out(2w) / P_in(w) at unit record amplitude, so that the
     second-order energy out is C eps^2 of the wave's with eps = lam A, i.e. (9/4) C h_H^2 in seed_derive's strain
     (h_H = (2/3) lam A at the horizon).  C(x) for both types at x = 1.0, 1.5, 2.1, 2.5 is pinned in the data file;
     the outer radius (R = 100 against 150, 2e-5), a pure-gauge admixture at first order (Q5) and the supplementary
     rows at R/2 (second order, 1e-6) check it.
  Q5 (computed) Gauge.  The six constrained regular directions with no outgoing content are the pure gauge modes:
     their outgoing projection is 1e-15 and their h_vv, h_vr, h_vth grow like r^0; the windowed incoming projection is
     not gauge-invariant (it reads the r^-1, r^0 pieces), which is why the gauge is fixed first.  A pure gauge
     admixture of the wave's own size moves C by the amount the data file records (D4).
  Q6 (computed; deduced) Against T7 and at the derived point.  T7's model gave sigma = |out at infinity| / |in at the
     horizon| falling as e^(-s x), s near 2 pi, for couplings f/r^p; the exact equations give the slope the data file
     records over x = 1.0 .. 2.5 for each type, and C(x*) at the derived point x* (527: 10.67 copper, ...) by the same
     deliberately low extrapolation T7 used (slope 3 from the last computed point); against half a bit with
     seed_derive's h_H and E_tot per anchor.  Every channel the full pattern adds (its h(x) tail: 0.988 of the power is
     l = 2) is bounded by the first-order escape times h_H^2 (deduced): the tail reflects at first order and its square
     cannot exceed its reflected power times the strain.
  Caveats.  Monochromatic (the envelope's peak); mu = 1 Tangherlini, the hole not growing during the passage; the
  extrapolation beyond x = 2.5 by slope, as T7; the record's own gauge and variables throughout (route b as approved).

Imports seed_derive.py (the anchors, strain and x*), seed_types.py and seed_escape.py by path; kn_gauge.py's base.
numpy, scipy, sympy.  Heavy stages cached under data/seed_second/ by a hash of this file's pipeline.
python3 seed_second.py [--selftest | --mutants | --build [T,S] [x,x,...]]
"""
import sys, os, io, time, json, pickle, hashlib, inspect, contextlib, importlib.util
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from numpy.polynomial.legendre import leggauss, legval

HERE = os.path.dirname(os.path.abspath(__file__))
RULINGS = os.path.join(HERE, "..", "M-RULINGS-2026-10-03.md")
DATA = os.path.join(HERE, "data", "seed_second.json")
CACHE = os.path.join(HERE, "data", "seed_second")
MUT = set()
MUTANTS = {"half_source": "the quadratic source halved (C falls fourfold; Q4's pinned values)",
           "swap_pattern": "the tensor pattern used for the scalar type (Q3's barrier check)",
           "no_supplementary": "the supplementary rows dropped (the null space is not the gauge's; Q2, Q3)"}
NM = 3
XS = (1.0, 1.5, 2.1, 2.5, 3.0)
EPS = 1e-4
v, r, th, e, mu, w = sp.symbols("v r theta e mu omega", positive=True)
sn, cs = sp.sin(th), sp.cos(th)
xs_, Ss_ = sp.symbols("x S", real=True)
NAMES = ("Ps", "Om", "A", "B", "C")
F1N = ("a", "b", "cc", "dps", "dom"); F2N = ("a2", "b2", "c2", "dps2", "dom2")
MODEOF = {"a": "A", "b": "B", "cc": "C", "dps": "Ps", "dom": "Om"}
ENV = {"Symbol": sp.Symbol, "Function": sp.Function, "Integer": sp.Integer, "Rational": sp.Rational, "Mul": sp.Mul,
       "Add": sp.Add, "Pow": sp.Pow, "Derivative": sp.Derivative, "sin": sp.sin, "cos": sp.cos, "log": sp.log,
       "Tuple": sp.Tuple, "Half": sp.S.Half, "NegativeOne": sp.S.NegativeOne, "One": sp.S.One, "Zero": sp.S.Zero,
       "Float": sp.Float, "sqrt": sp.sqrt, "exp": sp.exp, "tan": sp.tan, "cot": sp.cot, "Abs": sp.Abs, "sign": sp.sign,
       "I": sp.I, "ImmutableDenseMatrix": sp.ImmutableDenseMatrix, "MutableDenseMatrix": sp.Matrix}


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def words():
    s = open(RULINGS).read()
    return "530. **Yes , b please" in s or ("Yes , b please" in s and "530." in s)


# ---------------------------------------------------------------- Q1: the reduction to second order (cached)
def reduce2():
    """the 2+1 equations about Tangherlini to order e^2: E_ab (rr, rth, thth, vr, vth, vv) and the two box equations"""
    X = [v, r, th]; n = 3
    rho = r**2*sn*cs; Fm = 1 - mu/r**2
    f1 = [sp.Function(nm)(v, r, th) for nm in F1N]; f2 = [sp.Function(nm)(v, r, th) for nm in F2N]
    a, b, cc, dps, dom = f1; a2, b2, c2, dps2, dom2 = f2
    hb = rho**2*sp.Matrix([[-Fm, 1, 0], [1, 0, 0], [0, 0, r**2]])
    h = hb + e*sp.Matrix([[a, b, cc], [b, 0, 0], [cc, 0, 0]]) + e**2*sp.Matrix([[a2, b2, c2], [b2, 0, 0], [c2, 0, 0]])

    def ser(x):
        x = sp.expand(x)
        return sum(x.coeff(e, k)*e**k for k in range(3))
    ser_inv = lambda x: sp.expand(sp.series(x, e, 0, 3).removeO())                  # noqa: E731
    gi = h.inv().applyfunc(ser_inv)
    G = [[[ser(sum(gi[i, d]*(sp.diff(h[d, j], X[k]) + sp.diff(h[d, k], X[j]) - sp.diff(h[j, k], X[d]))
                   for d in range(n))/2) for k in range(n)] for j in range(n)] for i in range(n)]

    def Ric(j, k):
        ex = 0
        for i in range(n):
            ex += sp.diff(G[i][j][k], X[i]) - sp.diff(G[i][j][i], X[k])
            for d in range(n):
                ex += G[i][i][d]*G[d][j][k] - G[i][k][d]*G[d][j][i]
        return ser(ex)
    psi = sp.log(rho) + e*dps + e**2*dps2
    om = sp.log(cs/sn)/2 + e*dom + e**2*dom2
    src = lambda j, k: ser(sp.Rational(3, 2)*sp.diff(psi, X[j])*sp.diff(psi, X[k])          # noqa: E731
                           + 2*sp.diff(om, X[j])*sp.diff(om, X[k]))
    out = {}
    for key, jk in (("rr", (1, 1)), ("rth", (1, 2)), ("thth", (2, 2)), ("vr", (0, 1)), ("vth", (0, 2)), ("vv", (0, 0))):
        E = Ric(*jk) - src(*jk)
        out[key] = {k: E.coeff(e, k) for k in range(3)}
    sq = ser_inv(sp.sqrt(-h.det())); isq = ser_inv(1/sp.sqrt(-h.det()))
    box = lambda f: ser(isq*sum(sp.diff(sq*sum(gi[i, j]*sp.diff(f, X[j]) for j in range(n)), X[i])     # noqa: E731
                                for i in range(n)))
    for nm, f in (("box_psi", psi), ("box_om", om)):
        B = box(f)
        out[nm] = {k: B.coeff(e, k) for k in range(3)}
    pt = {r: sp.Rational(17, 10), th: sp.Rational(7, 10), mu: 1, v: 1}
    out["_order0"] = max(float(abs(sp.N(d[0].subs(pt)))) for d in out.values())
    return out


def to_xS(ex):
    """a trigonometric polynomial in theta -> polynomial in x = cos 2 th and S = sin 2 th (S-degree 0 or 1)"""
    ex = ex.subs({sp.Abs(cs): cs, sp.Abs(sn): sn, sp.sign(cs): 1, sp.sign(sn): 1})
    ex = sp.expand(sp.expand_trig(sp.expand(ex)))
    ex = sp.expand(ex.subs({sp.sin(2*th): 2*sn*cs, sp.cos(2*th): cs**2 - sn**2, sp.sin(4*th): 4*sn*cs*(cs**2 - sn**2),
                            sp.cos(4*th): 1 - 8*sn**2*cs**2, sp.sin(3*th): 3*sn - 4*sn**3, sp.cos(3*th): 4*cs**3 - 3*cs,
                            sp.sin(6*th): 2*(3*sn - 4*sn**3)*(4*cs**3 - 3*cs),
                            sp.sin(8*th): 2*(4*sn*cs*(cs**2 - sn**2))*(1 - 8*sn**2*cs**2)}))
    poly = sp.Poly(ex, sn, cs); out = 0
    for (i, j), c in poly.terms():
        k = min(i, j); i2, j2 = i - k, j - k
        if i2 % 2 or j2 % 2:
            raise ValueError("odd power %d %d" % (i, j))
        out += c*(Ss_/2)**k*((1 - xs_)/2)**(i2//2)*((1 + xs_)/2)**(j2//2)
    out = sp.expand(out); red = 0
    for (p,), c in sp.Poly(out, Ss_).terms():
        red += c*(1 - xs_**2)**(p//2)*Ss_**(p % 2)
    return sp.expand(red)


def rows_first(red, nm_):
    """the first-order rows of every equation with the mode ansatz, projected exactly on P_m; the common factor and the
    denominator kept (they multiply the quadratic source the same way)"""
    modes = {nm: [sp.Function(nm + str(n))(v, r) for n in range(nm_)] for nm in NAMES}
    Pth = lambda n: sp.legendre(n, cs**2 - sn**2)                                  # noqa: E731
    rho2 = r**4*sn**2*cs**2
    a, b, cc, dps, dom = [sp.Function(nm)(v, r, th) for nm in F1N]
    sub = {dps: sum(modes["Ps"][n]*Pth(n) for n in range(nm_)), dom: sum(modes["Om"][n]*Pth(n) for n in range(nm_)),
           a: rho2*sum(modes["A"][n]*Pth(n) for n in range(nm_)), b: rho2*sum(modes["B"][n]*Pth(n) for n in range(nm_)),
           cc: rho2*2*sn*cs*sum(modes["C"][n]*Pth(n) for n in range(nm_))}
    allf = [g for nm in modes for g in modes[nm]]
    out, commons, denoms = {}, {}, {}
    for eq in ("rr", "rth", "thth", "vr", "vth", "vv", "box_psi", "box_om"):
        E1 = red[eq][1].subs({sp.Abs(cs): cs, sp.Abs(sn): sn})
        num, den = sp.together(E1).as_numer_denom()
        denoms[eq] = den
        E = sp.expand(num.subs(sub).doit())
        terms = {}
        for d in sp.Add.make_args(E):
            c, rest = d.as_independent(*allf, as_Add=False)
            terms[rest] = terms.get(rest, 0) + c
        polys = {k_: to_xS(c) for k_, c in terms.items()}
        g = None
        for px in polys.values():
            g = px if g is None else sp.gcd(g, px)
        commons[eq] = g
        proj = {}
        for k_, px in polys.items():
            px0 = sp.expand(sp.cancel(px/g)).subs(Ss_, 1)
            for m in range(nm_ + 3):
                val = sp.integrate(px0*sp.legendre(m, xs_), (xs_, -1, 1))*sp.Rational(2*m + 1, 2)
                if val != 0:
                    proj.setdefault(m, {})[k_] = val
        out[eq] = {m: sum(c*k for k, c in dd.items()) for m, dd in proj.items()}
    return dict(NM=nm_, rows=out, common=commons, denom=denoms)


def freq_system(rw):
    """the frequency-domain radial system: M hi = R y for the highest derivatives, the supplementary rows as forms"""
    nm_ = rw["NM"]
    F = {nm: [sp.Function(nm + str(n))(v, r) for n in range(nm_)] for nm in NAMES}
    R = {nm: [sp.Function(nm + str(n) + "r")(r) for n in range(nm_)] for nm in NAMES}
    ph = sp.exp(-sp.I*w*v)
    tosec = {F[nm][n]: R[nm][n]*ph for nm in NAMES for n in range(nm_)}
    syms = {nm: [[sp.Symbol("%s%d_%d" % (nm, n, k)) for k in range(4)] for n in range(nm_)] for nm in NAMES}

    def tosym(ex):
        ex = sp.expand(ex.subs(tosec).doit()/ph)
        rep = {}
        for nm in NAMES:
            for n in range(nm_):
                for k in (3, 2, 1):
                    rep[sp.Derivative(R[nm][n], (r, k))] = syms[nm][n][k]
        ex = ex.subs(rep)
        return sp.expand(ex.subs({R[nm][n]: syms[nm][n][0] for nm in NAMES for n in range(nm_)}))
    EQ = {eq: {m: tosym(ex) for m, ex in dd.items()} for eq, dd in rw["rows"].items()}
    hi, state = [], []
    for n in range(nm_):
        hi += [syms["Ps"][n][2], syms["Om"][n][2], syms["C"][n][2], syms["A"][n][1], syms["B"][n][1]]
        state += [syms["Ps"][n][0], syms["Ps"][n][1], syms["Om"][n][0], syms["Om"][n][1], syms["C"][n][0],
                  syms["C"][n][1], syms["A"][n][0], syms["B"][n][0]]
    eqlist = [EQ[eq][m] for eq in ("rr", "rth", "thth", "box_psi", "box_om") for m in range(nm_)]
    Mx, rhs = sp.linear_eq_to_matrix(eqlist, hi)
    sup = {}
    extra = [syms["A"][n][2] for n in range(nm_)]
    for eq in ("vth", "vv"):
        for m in range(nm_):
            Ms, rs = sp.linear_eq_to_matrix([EQ[eq][m]], list(state) + list(hi) + extra)
            assert rs == sp.zeros(1, 1)
            sup[(eq, m)] = Ms
    return dict(NM=nm_, hi=hi, state=state, M=Mx, rhs=rhs, sup=sup)


# ---------------------------------------------------------------- caching
def _hash_stages():
    src = "".join(inspect.getsource(f) for f in (reduce2, to_xS, rows_first, freq_system))
    return hashlib.md5(src.encode()).hexdigest()


def _hash():
    src = _hash_stages() + "".join(inspect.getsource(f) for f in (System, Profiles, Source, Window, pattern, solve))
    return hashlib.md5(src.encode()).hexdigest()


def _stage(name, build, *args):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, name + ".pkl")
    if os.path.exists(path):
        d = pickle.load(open(path, "rb"))
        if d.get("hash") == _hash_stages():
            return d["obj"]
    t0 = time.time(); obj = build(*args)
    pickle.dump(dict(hash=_hash_stages(), obj=obj), open(path, "wb"))
    print("   built %s in %.0fs" % (name, time.time() - t0), flush=True)
    return obj


def stages(nm_=NM):
    red = _stage("reduce2", reduce2)
    rw = _stage("rows_NM%d" % nm_, rows_first, red, nm_)
    fq = _stage("freq_NM%d" % nm_, freq_system, rw)
    return red, rw, fq


# ---------------------------------------------------------------- the radial system and the source
class System:
    def __init__(self, fq, use=("vth", "vv")):
        self.NM = fq["NM"]; nm_ = self.NM
        self.state, self.hi = fq["state"], fq["hi"]; self.NS = len(self.state)
        self.Mf = sp.lambdify((r, mu, w), fq["M"], "numpy", cse=True)
        Rsym = sp.Matrix([[fq["rhs"][i].coeff(s_) for s_ in self.state] for i in range(len(self.hi))])
        self.Rf = sp.lambdify((r, mu, w), Rsym, "numpy", cse=True)
        idx = {str(h): i for i, h in enumerate(self.hi)}
        NS = self.NS
        self.sel = np.zeros((NS, len(self.hi))); self.pick = np.zeros((NS, NS)); self.iA1 = []
        for n in range(nm_):
            b0 = 8*n
            self.pick[b0, b0 + 1] = 1; self.sel[b0 + 1, idx["Ps%d_2" % n]] = 1
            self.pick[b0 + 2, b0 + 3] = 1; self.sel[b0 + 3, idx["Om%d_2" % n]] = 1
            self.pick[b0 + 4, b0 + 5] = 1; self.sel[b0 + 5, idx["C%d_2" % n]] = 1
            self.sel[b0 + 6, idx["A%d_1" % n]] = 1; self.sel[b0 + 7, idx["B%d_1" % n]] = 1
            self.iA1.append(idx["A%d_1" % n])
        self.sup = {k: sp.lambdify((r, mu, w), Ms, "numpy", cse=True) for k, Ms in fq["sup"].items() if k[0] in use}

    def L(self, rr, om, mu_=1.0):
        Mn = np.array(self.Mf(rr, mu_, om), dtype=complex)
        return np.linalg.solve(Mn, np.array(self.Rf(rr, mu_, om), dtype=complex))

    def Amat(self, rr, om, mu_=1.0):
        return self.pick + self.sel @ self.L(rr, om, mu_)

    def sup_rows(self, rr, om, mu_=1.0):
        L = self.L(rr, om, mu_); A = self.pick + self.sel @ L; h = 1e-6*rr
        Lp = (self.L(rr + h, om, mu_) - self.L(rr - h, om, mu_))/(2*h)
        App = Lp[self.iA1, :] + L[self.iA1, :] @ A
        NS, NH = self.NS, len(self.hi); rows = []
        for key in sorted(self.sup):
            Ms = np.array(self.sup[key](rr, mu_, om), dtype=complex).ravel()
            rows.append(Ms[:NS] + Ms[NS:NS + NH] @ L + Ms[NS + NH:] @ App)
        return np.array(rows).reshape(len(rows), NS)


def split_axes(px):
    """polynomial in x, S -> (p, j, core): px = S^p (1 - x^2)^j core(x, ...) with core(+-1) != 0"""
    px = sp.expand(px)
    if px == 0:
        return 0, 0, sp.Integer(0)
    degs = {m[0] for m in sp.Poly(px, Ss_).monoms()}
    assert len(degs) == 1, degs
    p = degs.pop(); core = sp.expand(px.subs(Ss_, 1)); j = 0
    while True:
        q, rem = sp.div(sp.Poly(core, xs_), sp.Poly(1 - xs_**2, xs_))
        if rem.is_zero and not q.is_zero:
            core = q.as_expr(); j += 1
        else:
            break
    return p, j, core


class Profiles:
    """the first-order fields' d_r^j d_th^k on the theta nodes from the mode amplitudes and their r-derivatives"""
    PI = {"a": r**4*sn**2*cs**2, "b": r**4*sn**2*cs**2, "cc": r**4*sn**2*cs**2*2*sn*cs, "dps": sp.Integer(1),
          "dom": sp.Integer(1)}

    def __init__(self, nm_, NQ=48):
        self.NM, self.NQ = nm_, NQ
        self.xq, self.wq = leggauss(NQ); self.thq = np.arccos(self.xq)/2
        self.P = np.array([legval(self.xq, [0]*m + [1]) for m in range(nm_ + 1)])
        K = {n: sp.Function("K%d" % n)(r) for n in range(nm_)}
        ks = [sp.Symbol("K%d_%d" % (n, m)) for m in range(3) for n in range(nm_)]
        self.fun = {}
        for nm in F1N:
            fs = self.PI[nm]*sum(K[n]*sp.legendre(n, cs**2 - sn**2) for n in range(nm_))
            for j in range(3):
                for k in range(3 - j):
                    ex = sp.diff(fs, r, j, th, k) if (j or k) else fs
                    rep = {}
                    for n in range(nm_):
                        rep[sp.Derivative(K[n], (r, 2))] = sp.Symbol("K%d_2" % n)
                        rep[sp.Derivative(K[n], r)] = sp.Symbol("K%d_1" % n)
                    ex = ex.subs(rep).subs({K[n]: sp.Symbol("K%d_0" % n) for n in range(nm_)})
                    self.fun[(nm, j, k)] = sp.lambdify([r, th] + ks, ex, "numpy")

    def slots(self, nm, rr, K0, K1, K2):
        args = [rr, self.thq] + list(K0) + list(K1) + list(K2)
        return {(j, k): np.broadcast_to(self.fun[(nm, j, k)](*args), (self.NQ,)).astype(complex)
                for (n2, j, k) in self.fun if n2 == nm}


class Source:
    """the quadratic terms of one equation's order e^2, with the first-order equation's multiplier and projection"""
    def __init__(self, eq, red, rw, prof):
        self.eq, self.NM, self.prof = eq, rw["NM"], prof
        self.den = sp.lambdify((r, th, mu), rw["denom"][eq], "numpy")
        g = sp.factor(rw["common"][eq])
        self.gf = sp.lambdify((r, mu, xs_, Ss_), g, "numpy")
        F1 = {nm: sp.Function(nm)(v, r, th) for nm in F1N}; F2 = {nm: sp.Function(nm)(v, r, th) for nm in F2N}
        E2 = red[eq][2].subs({sp.Abs(cs): cs, sp.Abs(sn): sn, sp.sign(cs): 1, sp.sign(sn): 1})
        Q = E2.subs({F2[nm]: 0 for nm in F2N}).doit()
        self.slot = {}; rep = {}
        for dv in Q.atoms(sp.Derivative):
            nm = [n_ for n_ in F1N if F1[n_] == dv.expr][0]
            cnt = {v: 0, r: 0, th: 0}
            for var, c in dv.variable_count:
                cnt[var] += int(c)
            key = (nm, cnt[v], cnt[r], cnt[th])
            rep[dv] = self.slot.setdefault(key, sp.Symbol("S_%s_%d%d%d" % key))
        Q = Q.xreplace(rep)
        for nm in F1N:
            Q = Q.xreplace({F1[nm]: self.slot.setdefault((nm, 0, 0, 0), sp.Symbol("S_%s_000" % nm))})
        self.keys = sorted(self.slot)
        PQ = sp.Poly(sp.expand(Q), *[self.slot[k] for k in self.keys])
        self.terms = []
        for mon, ck in PQ.terms():
            Nk, Dk = sp.cancel(sp.together(ck)).as_numer_denom()
            pN, jN, PN = split_axes(to_xS(Nk)); pD, jD, PD = split_axes(to_xS(Dk))
            if PN != 0:
                self.terms.append((mon, sp.lambdify((r, xs_, mu), sp.cancel(PN/PD), "numpy"), pN - pD, jN - jD))

    def eval(self, rr, om, modes, mu_=1.0):
        pr = self.prof
        sl = {nm: pr.slots(nm, rr, *modes[MODEOF[nm]]) for nm in F1N}
        vals = [(-1j*om)**i*sl[nm][(j, k)] for (nm, i, j, k) in self.keys]
        S = np.sin(2*pr.thq); xx = np.cos(2*pr.thq); omx = 1 - xx**2
        q = np.zeros(pr.NQ, dtype=complex)
        for mon, f, pS, jx in self.terms:
            term = np.broadcast_to(np.asarray(f(rr, xx, mu_), dtype=complex), (pr.NQ,))*S**pS*omx**jx
            for ex, val in zip(mon, vals):
                if ex:
                    term = term*val**ex
            q = q + term
        fac = 0.5 if "half_source" not in MUT else 0.25
        integ = fac*q*self.den(rr, pr.thq, mu_)/self.gf(rr, mu_, xx, S)
        return np.array([(2*m + 1)/2*np.sum(pr.wq*pr.P[m]*integ) for m in range(self.NM)])


# ---------------------------------------------------------------- the solve
def rstar(rr):
    return rr + 0.5*np.log((rr - 1)/(rr + 1))


def integrate(sysm, om, y0, r0, RMAX, t_eval, src=None, rtol=1e-10, atol=1e-14):
    NS = sysm.NS

    def rhs(rr, y):
        yc = y[:NS] + 1j*y[NS:]; dy = sysm.Amat(rr, om) @ yc
        if src is not None:
            dy = dy + src(rr)
        return np.concatenate([dy.real, dy.imag])
    s = solve_ivp(rhs, [r0, RMAX], np.concatenate([y0.real, y0.imag]), method="DOP853", rtol=rtol, atol=atol,
                  t_eval=t_eval, dense_output=True)
    if s.status != 0:
        raise RuntimeError("integration failed at r = %.6f: %s" % (s.t[-1] if len(s.t) else r0, s.message))
    Y = s.y[:NS, :] + 1j*s.y[NS:, :]

    def yd(rr):
        yy = s.sol(rr); return yy[:NS] + 1j*yy[NS:]
    return Y, yd


class Window:
    def __init__(self, Om, R0, R1, N=3000):
        self.rs = np.linspace(R0, R1, N); self.w = np.hanning(N); self.w /= self.w.sum()
        self.pin = self.rs**1.5; self.pout = self.rs**1.5*np.exp(-2j*Om*rstar(self.rs))

    def amps(self, yd, nm_):
        Ys = np.array([yd(rr) for rr in self.rs])
        a_in = np.zeros(2*nm_, dtype=complex); a_out = np.zeros_like(a_in)
        for n in range(nm_):
            for q, i0 in enumerate((0, 2)):
                f = Ys[:, 8*n + i0]
                a_in[2*n + q] = np.sum(self.w*self.pin*f); a_out[2*n + q] = np.sum(self.w*self.pout*f)
        return a_in, a_out


def pattern(kind, nm_):
    t = np.zeros(2*nm_, dtype=complex)
    if kind == "T" or (kind == "S" and "swap_pattern" in MUT):
        t[0] = -0.5; t[3] = -0.75
    elif kind == "S":
        t[2] = 2/3; t[1] = 1.0
    return t


def power(a, nm_):
    wn = 2/(2*np.arange(nm_) + 1)
    return float(np.sum(wn*(1.5*np.abs(a[0::2])**2 + 2*np.abs(a[1::2])**2)))


def solve(om, kind, red, rw, fq, RMAX=150.0, eps=EPS, RC=2.0, second=True, gauge_shift=0.0, verbose=False):
    """first order: the l = 2 wave of one type scattered off the hole; second order: its 2w emission.  Numbers only."""
    nm_ = rw["NM"]
    sysm = System(fq, use=() if "no_supplementary" in MUT else ("vth", "vv")); NS = sysm.NS
    idxABC = [8*n + i for n in range(nm_) for i in (4, 6, 7)]

    def pole(Om, src=None):
        """A(r) = A_-1/(r - 1) + A_0 + ... (and b likewise) from the two radii 1 + eps, 1 + 2 eps"""
        A1_, A2_ = sysm.Amat(1 + eps, Om), sysm.Amat(1 + 2*eps, Om)
        out = [2*eps*(A1_ - A2_), 2*A2_ - A1_]
        if src is not None:
            b1_, b2_ = src(1 + eps), src(1 + 2*eps); out += [2*eps*(b1_ - b2_), 2*b2_ - b1_]
        return out

    def basis(Om):
        """the regular solutions at 1 + eps by the pole's Frobenius expansion, y = y0 + (r - 1) y1: A_-1 y0 = 0 (the
        null space; the irregular exponents -1 + i w have |.| > 1) and (I - A_-1) y1 = A_0 y0 -- eigenvectors of the
        degenerate cluster carry irregular admixtures that leave as outgoing waves"""
        Am1, A0_ = pole(Om)
        U, sv, Vh = np.linalg.svd(Am1)
        nreg = NS - int((sv > 0.5).sum())
        Y0 = Vh[NS - nreg:].conj().T
        return Y0 + eps*np.linalg.solve(np.eye(NS) - Am1, A0_ @ Y0)

    def propagate(Om, B, src=None, y0=None):
        W = Window(Om, 0.5*RMAX, RMAX); dense, YC, YR, AI, AO = [], [], [], [], []
        cols = [B[:, j] for j in range(B.shape[1])] if src is None else [y0]
        for y0 in cols:
            Yj, yd = integrate(sysm, Om, y0, 1 + eps, RMAX, [RC, RMAX], src=src)
            ai, ao = W.amps(yd, nm_)
            dense.append(yd); YC.append(Yj[:, 0]); YR.append(Yj[:, 1]); AI.append(ai); AO.append(ao)
        return dense, np.array(YC).T, np.array(YR).T, np.array(AI).T, np.array(AO).T

    def gauge_fix(YR, c, null):
        if null.shape[1] == 0:
            return c
        d, *_ = np.linalg.lstsq(YR[idxABC] @ null, -(YR[idxABC] @ c), rcond=None)
        return c + null @ d
    t0 = time.time()
    B1 = basis(om); nb = B1.shape[1]
    dense1, YC, YR, AIN, AOUT = propagate(om, B1)
    Sc = sysm.sup_rows(RC, om) @ YC if sysm.sup else np.zeros((0, nb))
    target = pattern(kind, nm_)
    Mc = np.vstack([AIN, Sc]); bc = np.concatenate([target, np.zeros(Sc.shape[0])])
    c0, _, rk1, _ = np.linalg.lstsq(Mc, bc, rcond=None)
    null1 = np.linalg.svd(Mc)[2][rk1:].conj().T
    c1 = gauge_fix(YR, c0, null1)
    sg = np.linalg.svd(np.vstack([Sc, AOUT]))
    rkg = int((sg[1] > 1e-9*sg[1][0]).sum()); G = sg[2][rkg:].conj().T
    out_leak = float(np.abs(AOUT @ G).max()) if G.shape[1] else 0.0
    if gauge_shift and G.shape[1]:
        scale = np.abs((YR @ c1)[idxABC]).max()/max(np.abs((YR @ G[:, 0])[idxABC]).max(), 1e-300)
        c1 = c1 + gauge_shift*scale*G[:, 0]

    def y1(rr):
        return sum(c1[j]*dense1[j](rr) for j in range(nb))
    W1 = Window(om, 0.5*RMAX, RMAX); a_in1, a_out1 = W1.amps(y1, nm_)
    RB = 0.5*RMAX
    SB = sysm.sup_rows(RB, om) if sysm.sup else None
    bondi1 = float(np.abs(SB @ y1(RB)).max()/(np.abs(SB).max()*np.abs(y1(RB)).max())) if sysm.sup else float("nan")
    out = dict(om=om, kind=kind, NM=nm_, RMAX=RMAX, rank1=int(rk1), nbasis=int(nb), null1=int(null1.shape[1]),
               ngauge=int(G.shape[1]), gauge_out_leak=out_leak, R1=power(a_out1, nm_)/power(a_in1, nm_),
               a_in1=[abs(x) for x in a_in1], a_out1=[abs(x) for x in a_out1], bondi1=bondi1,
               resid1=float(np.linalg.norm(Mc @ c1 - bc)), secs1=time.time() - t0)
    if verbose:
        print("   [1st %s x=%.3f] rank %d/%d null %d gauge %d (out leak %.1e) R1 %.6e Bondi %.1e %.0fs"
              % (kind, om, rk1, nb, out["null1"], out["ngauge"], out_leak, out["R1"], bondi1, out["secs1"]), flush=True)
    if not second:
        return out
    prof = Profiles(nm_)
    SRC = {eq: Source(eq, red, rw, prof) for eq in ("rr", "rth", "thth", "box_psi", "box_om", "vth", "vv")}
    idx = {str(hh): i for i, hh in enumerate(sysm.hi)}

    def modes_at(rr):
        y = y1(rr); L = sysm.L(rr, om); hi = L @ y; h = 1e-5*rr
        hip = (sysm.L(rr + h, om) @ y1(rr + h) - sysm.L(rr - h, om) @ y1(rr - h))/(2*h)
        md = {}
        for nm, i0 in (("Ps", 0), ("Om", 2), ("C", 4)):
            md[nm] = (y[i0::8], y[i0 + 1::8], np.array([hi[idx["%s%d_2" % (nm, n)]] for n in range(nm_)]))
        for nm, i0 in (("A", 6), ("B", 7)):
            md[nm] = (y[i0::8], np.array([hi[idx["%s%d_1" % (nm, n)]] for n in range(nm_)]),
                      np.array([hip[idx["%s%d_1" % (nm, n)]] for n in range(nm_)]))
        return md
    ode_eqs = ("rr", "rth", "thth", "box_psi", "box_om")

    def svec(rr):
        md = modes_at(rr)
        return np.concatenate([SRC[eq].eval(rr, om, md) for eq in ode_eqs])

    def bvec(rr):
        return -sysm.sel @ np.linalg.solve(np.array(sysm.Mf(rr, 1.0, 2*om), dtype=complex), svec(rr))
    B2 = basis(2*om); nb2 = B2.shape[1]
    dense2, YC2, YR2, AIN2, AOUT2 = propagate(2*om, B2)
    # the regular particular solution starts from the pole balance at the horizon, (r - 1) y' = A_-1 y + b_-1 at
    # order 0: started from zero it carries an outgoing-from-horizon admixture of order eps times the forcing
    Am1, A0_, bm1, b0_ = pole(2*om, src=bvec)
    y0p = np.linalg.lstsq(Am1, -bm1, rcond=None)[0]
    pole_res = float(np.linalg.norm(Am1 @ y0p + bm1)/np.linalg.norm(bm1))
    y0p = y0p + eps*np.linalg.solve(np.eye(NS) - Am1, A0_ @ y0p + b0_)      # the next order of the expansion
    (yp,), YCp, YRp, ainp, aoutp = propagate(2*om, B2, src=bvec, y0=y0p)

    def sup_particular(rr):
        def hi_at(r_):
            return sysm.L(r_, 2*om) @ yp(r_) - np.linalg.solve(np.array(sysm.Mf(r_, 1.0, 2*om), dtype=complex), svec(r_))
        y = yp(rr); hi = hi_at(rr); h = 1e-5*rr
        App = ((hi_at(rr + h) - hi_at(rr - h))/(2*h))[sysm.iA1]
        md = modes_at(rr); vals = []; NH = len(sysm.hi)
        for key in sorted(sysm.sup):
            Ms = np.array(sysm.sup[key](rr, 1.0, 2*om), dtype=complex).ravel()
            vals.append(Ms[:NS] @ y + Ms[NS:NS + NH] @ hi + Ms[NS + NH:] @ App + SRC[key[0]].eval(rr, om, md)[key[1]])
        return np.array(vals)
    Sc2 = sysm.sup_rows(RC, 2*om) @ YC2 if sysm.sup else np.zeros((0, nb2))
    sp_ = sup_particular(RC) if sysm.sup else np.zeros(0)
    Mc2 = np.vstack([AIN2, Sc2]); bc2 = -np.concatenate([ainp[:, 0], sp_])
    c20, _, rk2, _ = np.linalg.lstsq(Mc2, bc2, rcond=None)
    null2 = np.linalg.svd(Mc2)[2][rk2:].conj().T
    if null2.shape[1]:
        d, *_ = np.linalg.lstsq(YR2[idxABC] @ null2, -(YRp[idxABC, 0] + YR2[idxABC] @ c20), rcond=None)
        c2 = c20 + null2 @ d
    else:
        c2 = c20

    def y2(rr):
        return yp(rr) + sum(c2[j]*dense2[j](rr) for j in range(nb2))
    W2 = Window(2*om, 0.5*RMAX, RMAX); a_in2, a_out2 = W2.amps(y2, nm_)
    C = 4*power(a_out2, nm_)/power(a_in1, nm_)
    yh = y2(1 + eps); ah = np.zeros(2*nm_, dtype=complex); ah[0::2] = yh[0::8]; ah[1::2] = yh[2::8]
    bondi2 = float("nan")
    if sysm.sup:
        supB = sup_particular(RB) + sysm.sup_rows(RB, 2*om) @ np.array([dense2[j](RB) for j in range(nb2)]).T @ c2
        bondi2 = float(np.abs(supB).max()/(np.abs(sysm.sup_rows(RB, 2*om)).max()*np.abs(y2(RB)).max()))
    out.update(dict(rank2=int(rk2), null2=int(null2.shape[1]), a_in2=[abs(x) for x in a_in2],
                    a_out2=[abs(x) for x in a_out2], C=C, sigma_T7=float(np.sqrt(power(a_out2, nm_)/power(ah, nm_))),
                    bondi2=bondi2, pole_res=pole_res, eps=eps, secs=time.time() - t0))
    if verbose:
        print("   [2nd %s x=%.3f] rank %d/%d null %d Bondi %.1e | C = %.4e sigma(T7 norm) %.3e  %.0fs"
              % (kind, om, rk2, nb2, out["null2"], bondi2, C, out["sigma_T7"], out["secs"]), flush=True)
    return out


# ---------------------------------------------------------------- the data file: the runs, cached by the pipeline's hash
def data(build=False, kinds=("T", "S"), xs=XS, verbose=True):
    d = json.load(open(DATA)) if os.path.exists(DATA) else {}
    if d.get("hash") != _hash():
        d = dict(hash=_hash(), runs={})
    want = ["%s x=%.3f" % (k, x) for k in kinds for x in xs] + ["T x=2.100 R100", "T x=2.100 gauge", "T x=3.000 eps3"]
    missing = [k for k in want if k not in d["runs"]]
    if missing and not build:
        raise RuntimeError("seed_second: %d runs missing from the cache; run --build (%s)"
                           % (len(missing), ", ".join(missing)))
    if missing:
        red, rw, fq = stages()
        for key in missing:
            kind, xtxt = key.split()[:2]; x = float(xtxt[2:])
            kw = (dict(RMAX=100.0) if key.endswith("R100") else dict(gauge_shift=1.0) if key.endswith("gauge")
                  else dict(eps=1e-3) if key.endswith("eps3") else {})
            d["runs"][key] = solve(x, kind, red, rw, fq, verbose=verbose, **kw)
            os.makedirs(os.path.dirname(DATA), exist_ok=True)
            json.dump(d, open(DATA, "w"), indent=1)
    return d


def compute(build=False):
    d = data(build=build)
    runs = d["runs"]
    ST = _load("seed_types.py", "ss_seed_types"); SE = ST.SE
    SD = _load("seed_derive.py", "ss_seed_derive")
    ki = {}
    for k in ("T", "S"):
        for x in XS:
            ki["%s x=%.3f" % (k, x)] = (SE.refl(2, x)[0] if k == "T" else ST.refl_S(2, x)[0])
    slopes = {}
    for k in ("T", "S"):
        lx = np.array(XS[1:]); lc = np.log([runs["%s x=%.3f" % (k, x)]["C"] for x in XS[1:]])   # x >= 1.5: the fall
        slopes[k] = dict(fit=float(-np.polyfit(lx, lc, 1)[0]), last=float(-(lc[-1] - lc[-2])/(lx[-1] - lx[-2])),
                         amp=float(-np.polyfit(lx, lc, 1)[0]/2))
    sd = SD.compute()
    fl = sd["fl"]; point = {}
    for n in SD.ANCH:
        d0 = sd["rows"][n][fl["lamP"]]; wv = sd["win"][n]; a = sd["an"][n]
        Clast = max(runs["%s x=%.3f" % (k, XS[-1])]["C"] for k in ("T", "S"))
        Cx = Clast*np.exp(-6.0*(d0["x"] - XS[-1]))                  # a deliberately low slope, 6 in C (3 in amplitude)
        frac = 9/4*Cx*wv["hH"]**2
        point[n] = dict(x=d0["x"], hH=wv["hH"], C=Cx, frac=frac, ratio=frac*a["Etot"]/a["h"], t7=sd["so"][n]["ratio"])
    t7 = json.load(open(os.path.join(HERE, "data", "seed_derive.json")))["vals"]
    return dict(words=words(), runs=runs, ki=ki, slopes=slopes, point=point, t7=t7, hash=d["hash"])


def checks(o):
    ch = {}; R = o["runs"]
    ch["Q0 M's words (530) in the rulings file"] = o["words"]
    ch["Q3 the l = 2 reflection of both types reproduces KI's barriers at every x to 2e-3 (2e-2 below 1e-6)"] = all(
        abs(R[k]["R1"]/o["ki"][k] - 1) < (2e-3 if o["ki"][k] > 1e-6 else 2e-2) for k in o["ki"])
    ch["Q2 the null space is the residual gauge (2 NM) at both orders, the gauge's outgoing leak below 1e-12"] = all(
        R[k]["null1"] == 2*NM and R[k]["ngauge"] == 2*NM and R[k]["gauge_out_leak"] < 1e-12 and R[k].get("null2") == 2*NM
        for k in R)
    ch["Q1 Bondi's lemma: the supplementary rows hold at R/2 to 1e-9 (first order) and 1e-4 (second)"] = all(
        R[k]["bondi1"] < 1e-9 and R[k]["bondi2"] < 1e-4 for k in R)
    ch["Q4 C(2.1): tensor 4.343e-7, scalar 8.038e-8 (pinned 2026-10-20); R = 100 agrees to 1e-4"] = (
        abs(R["T x=2.100"]["C"]/4.343e-7 - 1) < 2e-3 and abs(R["S x=2.100"]["C"]/8.038e-8 - 1) < 2e-3
        and abs(R["T x=2.100 R100"]["C"]/R["T x=2.100"]["C"] - 1) < 1e-4)
    ch["Q5 a pure gauge admixture of the wave's own size at first order moves C by under 1e-3"] = (
        abs(R["T x=2.100 gauge"]["C"]/R["T x=2.100"]["C"] - 1) < 1e-3)
    ch["Q4 the horizon start: C(3.0) at eps = 1e-3 and 1e-4 agree to 10 %, the pole balance residual under 1e-3"] = (
        abs(R["T x=3.000 eps3"]["C"]/R["T x=3.000"]["C"] - 1) < 0.1 and all(R[k]["pole_res"] < 1e-3 for k in R))
    ch["Q6 C falls with x for both types; the amplitude slope over x >= 1.5 in [3, 10] (T7's model: near 2 pi)"] = all(
        3.0 < o["slopes"][k]["amp"] < 10.0 for k in ("T", "S")) and all(
        R["%s x=%.3f" % (k, XS[i + 1])]["C"] < R["%s x=%.3f" % (k, XS[i])]["C"]
        for k in ("T", "S") for i in range(len(XS) - 1))
    ch["Q6 at the derived point the second order lets out under 1e-6 half bits at every anchor"] = all(
        p["ratio"] < 1e-6 for p in o["point"].values())
    return ch


def report(o=None):
    o = o or compute()
    print("seed_second.py -- the second order of the record's equations at 2w, exact (item 530)")
    for k in sorted(o["runs"]):
        R = o["runs"][k]
        print("  %-18s R1 %.6e (KI %.6e)  C %.4e  sigma(T7 norm) %.3e  Bondi %.0e/%.0e  gauge leak %.0e" % (
            k, R["R1"], o["ki"].get(k.split(" R")[0].split(" g")[0], float("nan")), R["C"], R["sigma_T7"], R["bondi1"],
            R["bondi2"], R["gauge_out_leak"]))
    for k, s in o["slopes"].items():
        print("  slope of ln C in x, %s: fit %.2f (amplitude %.2f), last interval %.2f"
              % (k, s["fit"], s["amp"], s["last"]))
    for n, p in o["point"].items():
        print("  %-12s x* %.2f h_H %.2e: C(x*) %.1e -> %.1e of the wave = %.1e half bits (T7's model: %.1e)" % (
            n, p["x"], p["hH"], p["C"], p["frac"], p["ratio"], p["t7"]))
    for k, val in checks(o).items():
        print("  [%s] %s" % ("ok" if val else "FAIL", k))


def selftest():
    c = checks(compute())
    n = sum(c.values())
    for k_, v_ in c.items():
        print("%-118s %s" % (k_[:118], "PASS" if v_ else "FAIL"))
    print("seed_second.py: %d/%d" % (n, len(c)))
    return n == len(c)


def mutants():
    """each mutant re-runs the stage it touches live (first order: a minute; the source: the x = 2.1 tensor run)"""
    caught = 0
    red, rw, fq = stages()
    base = data()["runs"]
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        try:
            if m_ == "half_source":
                o = solve(2.1, "T", red, rw, fq)
                failed = [] if abs(o["C"]/base["T x=2.100"]["C"] - 1) < 2e-3 else ["Q4 C(2.1) tensor %.3e" % o["C"]]
            elif m_ == "swap_pattern":
                o = solve(2.1, "S", red, rw, fq, second=False)
                ST = _load("seed_types.py", "ss_seed_types")
                failed = [] if abs(o["R1"]/ST.refl_S(2, 2.1)[0] - 1) < 2e-3 else ["Q3 scalar reflection %.3e" % o["R1"]]
            else:
                o = solve(2.1, "T", red, rw, fq, second=False)
                ok = o["null1"] == 2*NM and o["ngauge"] == 2*NM
                failed = [] if ok else ["Q2 null %d gauge %d" % (o["null1"], o["ngauge"])]
        except Exception as ex:                                  # noqa: BLE001
            failed = ["raised %s" % type(ex).__name__]
        caught += bool(failed)
        print("mutant %-16s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    if "--build" in sys.argv:
        report(compute(build=True)); sys.exit(0)
    report()
