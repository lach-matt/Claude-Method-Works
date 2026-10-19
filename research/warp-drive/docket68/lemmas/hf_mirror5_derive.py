#!/usr/bin/env python3
"""hf_mirror5_derive.py -- the equations hf_mirror5.py evolves, derived from the metric and regularized.

  1. The 5D vacuum equations for the T^2-symmetric metric with both reflections, reduced on the two Killing circles:
     R_ab = 0 on the base (v, y, x) and R_phi_k phi_k = 0, in ingoing Bondi form compactified at past null infinity,
     r = y^-2, x = cos 2 theta (one sympy pass, about 20 s).
  2. The regular fields: P1 = y^3 (2 c^2 G - s^2 F)/3, P2 = y^3 (2 s^2 F - c^2 G)/3, beta = y^6 b, V = y^5 (1 - x^2) q,
     W = 1 + y^3 w.  Every exponential is written e^z = 1 + z phi1(z), so each cancellation at infinity is an exact
     polynomial identity; the equations are binned in powers of y and every power below the lowest surviving one is
     checked to vanish identically.
  3. The axis: (A1 + 2 A2) and (2 A1 + A2) carry the factors (x - 1) and (x + 1) on their v-derivative terms exactly
     (checked); their remainders vanish on the axes only on-shell, which hf_mirror5.py treats by exact division of the
     polynomial interpolant.
  4. W's hypersurface equation is the trace 4 (1 - x^2) y^4 e^{2(P1 + P2)} E_xx - A1 - A2 (no v-derivatives, checked).

python3 hf_mirror5_derive.py --quick   re-derives E_yy, E_yx, A1, A2 (a few minutes) and compares with the stored data
python3 hf_mirror5_derive.py --full    re-derives everything (E_vv's binning alone took 6811 s) and rewrites the data
"""
import sys, os, json, gzip, time, pickle
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
EQS = os.path.join(HERE, "data", "hf_mirror5_eqs.json.gz")
v, y, x = sp.symbols("v y x", real=True)
X = [v, y, x]
ORDER = {v: "v", y: "y", x: "x"}


def einstein():
    be, W, V, P1, P2 = [sp.Function(n)(v, y, x) for n in ("beta", "W", "V", "P1", "P2")]
    S = P1 + P2
    r = y**-2
    hx = r**2*sp.exp(-2*S)/(4*(1 - x**2))
    gam = sp.Matrix([[-sp.exp(2*be)*W + hx*V**2, -2*y**-3*sp.exp(2*be), -hx*V],
                     [-2*y**-3*sp.exp(2*be), 0, 0], [-hx*V, 0, hx]])
    Q1 = sp.log(r) + sp.log((1 + x)/2)/2 + P1
    Q2 = sp.log(r) + sp.log((1 - x)/2)/2 + P2
    gi = sp.simplify(gam.inv())
    Gam = [[[sp.simplify(sum(gi[i, l]*(sp.diff(gam[l, j], X[k]) + sp.diff(gam[l, k], X[j]) - sp.diff(gam[j, k], X[l]))
                             for l in range(3))/2) for k in range(3)] for j in range(3)] for i in range(3)]
    R3 = sp.zeros(3)
    for j in range(3):
        for k in range(j, 3):
            R3[j, k] = R3[k, j] = sp.expand(sum(sp.diff(Gam[i][j][k], X[i]) - sp.diff(Gam[i][j][i], X[k])
                                                + sum(Gam[i][i][l]*Gam[l][j][k] - Gam[i][k][l]*Gam[l][j][i] for l in range(3))
                                                for i in range(3)))
    cov2 = lambda Q: sp.Matrix(3, 3, lambda i, j: sp.diff(Q, X[i], X[j]) - sum(Gam[k][i][j]*sp.diff(Q, X[k]) for k in range(3)))
    H1, H2 = cov2(Q1), cov2(Q2)
    E = sp.Matrix(3, 3, lambda i, j: R3[i, j] - (H1[i, j] + H2[i, j] + sp.diff(Q1, X[i])*sp.diff(Q1, X[j])
                                                  + sp.diff(Q2, X[i])*sp.diff(Q2, X[j])))
    box = lambda H: sum(gi[i, j]*H[i, j] for i in range(3) for j in range(3))
    dot = lambda A, B: sum(gi[i, j]*sp.diff(A, X[i])*sp.diff(B, X[j]) for i in range(3) for j in range(3))
    out = {nm: sp.expand(E[i, j]) for (i, j), nm in [((1, 1), "yy"), ((1, 2), "yx"), ((2, 2), "xx"), ((0, 1), "vy"),
                                                      ((0, 2), "vx"), ((0, 0), "vv")]}
    out["A1"] = sp.expand(box(H1) + dot(Q1, Q1 + Q2)); out["A2"] = sp.expand(box(H2) + dot(Q2, Q1 + Q2))
    return out, dict(beta=be, W=W, V=V, P1=P1, P2=P2)


def ansatz(out, fn, keys):
    F, G, b, q, w = [sp.Function(n)(v, y, x) for n in ("F", "G", "b", "q", "w")]
    c2, s2 = (1 + x)/2, (1 - x)/2
    sub = {fn["P1"]: y**3*(2*c2*G - s2*F)/3, fn["P2"]: y**3*(2*s2*F - c2*G)/3, fn["beta"]: y**6*b,
           fn["V"]: y**5*(1 - x**2)*q, fn["W"]: 1 + y**3*w}
    def tosym(e):
        reps = {d: sp.Symbol(str(d.expr.func) + "_" + "".join(sorted(ORDER[s] for s, k in d.variable_count for _ in range(k))))
                for d in e.atoms(sp.Derivative)}
        e = e.subs(reps)
        for f in (F, G, b, q, w):
            e = e.subs(f, sp.Symbol(str(f.func)))
        return e
    res = {k: tosym(out[k].subs(sub).doit()) for k in keys if k in out}
    if "W" in keys:
        Fs, Gs = sp.Symbol("F"), sp.Symbol("G")
        Ssum = y**3*((1 + x)/2*Gs + (1 - x)/2*Fs)/3
        res["W"] = tosym((4*(1 - x**2)*y**4*sp.exp(2*Ssum)*out["xx"] - out["A1"] - out["A2"]).subs(sub).doit())
    return res


PHI = sp.Function("phi1")
def bins(e):
    """powers of y with e^z = 1 + z phi1(z); returns (lowest surviving power, {power: coefficient})"""
    def ypow(t):
        return int(t.as_powers_dict().get(y, 0))
    e = sp.expand(e)
    cache, pw = {}, {}
    for t in sp.Add.make_args(e):
        n, d = t.as_numer_denom()
        if d not in cache:
            ky, ex, rest = 0, sp.Integer(1), sp.Integer(1)
            for f in sp.Mul.make_args(sp.factor(d)):
                bse, ep = f.as_base_exp()
                if bse == y: ky += int(ep)
                elif isinstance(f, sp.exp): ex *= sp.exp(-f.args[0])
                elif isinstance(bse, sp.exp): ex *= sp.exp(-bse.args[0]*ep)
                else:
                    assert not f.has(y) and not f.has(sp.exp), f
                    rest *= f
            cache[d] = (ky, ex, 1/rest)
        ky, ex, xr = cache[d]
        m = n*ex
        m = m.xreplace({a: 1 + sp.expand(a.args[0])*PHI(sp.expand(a.args[0])) for a in m.atoms(sp.exp)})
        for s_ in sp.Add.make_args(sp.expand(m)):
            p = ypow(s_) - ky
            pw[p] = pw.get(p, 0) + s_/y**ypow(s_)*xr
    lo = None
    for p in sorted(pw):
        c = sp.cancel(sp.together(pw[p]))
        pw[p] = c
        if c != 0:
            lo = p
            break
    return lo, pw


def regularize(lo, pw, axis=None):
    return sp.Add(*[y**(p - lo)*sp.cancel(sp.together(pw[p] if axis is None else pw[p]/axis)) for p in sorted(pw) if p >= lo])


def quick():
    t0 = time.time()
    out, fn = einstein()
    res = ansatz(out, fn, ["yy", "yx", "A1", "A2"])
    print("derived and substituted %.0fs" % (time.time() - t0), flush=True)
    stored = json.loads(gzip.open(EQS).read())
    ns = {k: getattr(sp, k) for k in dir(sp)}
    ok = True
    lo, pw = bins(res["yy"]); Eb = regularize(lo, pw)
    ok &= lo == 4 and sp.simplify(Eb - eval(stored["Eb"], ns)) == 0
    print("E_yy: lowest power %s, matches stored: %s (%.0fs)" % (lo, ok, time.time() - t0), flush=True)
    lo, pw = bins(res["yx"]); Eq = regularize(lo, pw)
    rng = np.random.default_rng(3)
    def same(a, b):
        syms = sorted((a.free_symbols | b.free_symbols), key=str)
        for _ in range(3):
            vals = {s: sp.Rational(int(rng.integers(-9, 10)), 7) for s in syms}
            fa = a.xreplace(vals).replace(lambda f: isinstance(f, sp.Function) and str(f.func) == "phi1",
                                          lambda f: (sp.exp(f.args[0]) - 1)/f.args[0] if f.args[0] != 0 else 1)
            fb = b.xreplace(vals).replace(lambda f: isinstance(f, sp.Function) and str(f.func) == "phi1",
                                          lambda f: (sp.exp(f.args[0]) - 1)/f.args[0] if f.args[0] != 0 else 1)
            if abs(sp.N(fa - fb, 30)) > 1e-20*(1 + abs(sp.N(fa, 30))):
                return False
        return True
    k = lo == 2 and same(Eq, eval(stored["Eq"], ns)); ok &= k
    print("E_yx: lowest power %s, matches stored: %s (%.0fs)" % (lo, k, time.time() - t0), flush=True)
    l1, p1 = bins(res["A1"]); l2, p2 = bins(res["A2"])
    pw = {p: p1.get(p, 0) + 2*p2.get(p, 0) for p in set(p1) | set(p2)}
    EFn = regularize(min(l1, l2), pw)
    c = sp.expand(sp.diff(EFn, sp.Symbol("F_vy")))
    ct = sp.cancel(sp.together(c/(x - 1)))
    rest = sp.expand(EFn - c*sp.Symbol("F_vy"))
    k = (sp.fraction(ct)[1] == 1 and same(ct, eval(stored["EFn_c"], ns)) and same(rest, eval(stored["EFn_r"], ns))); ok &= k
    print("A1 + 2 A2: lowest power %d; F_vy coefficient carries (x - 1) exactly; matches stored: %s (%.0fs)" % (min(l1, l2), k, time.time() - t0))
    print("hf_mirror5_derive quick: %s" % ("PASS" if ok else "FAIL"))
    return ok


def full(dest=EQS):
    """every component, binned and regularized, packed as the instrument reads it (hours: E_vv's binning dominates)"""
    t0 = time.time()
    out, fn = einstein()
    res = ansatz(out, fn, ["yy", "yx", "vy", "vx", "vv", "A1", "A2", "W"])
    B = {}
    for k in res:
        B[k] = bins(res[k])
        print("%s: lowest surviving power %s (%.0fs)" % (k, B[k][0], time.time() - t0), flush=True)
    pk = {"Eb": regularize(*B["yy"]), "Eq": regularize(*B["yx"]), "EW": regularize(*B["W"]),
          "Evy": regularize(*B["vy"]), "Evx": regularize(*B["vx"]), "Evv": regularize(*B["vv"])}
    for nm, (c1, c2), sym, ax in (("EFn", (1, 2), "F_vy", x - 1), ("EGn", (2, 1), "G_vy", x + 1)):
        lo = min(B["A1"][0], B["A2"][0])
        pw = {p_: c1*B["A1"][1].get(p_, 0) + c2*B["A2"][1].get(p_, 0) for p_ in set(B["A1"][1]) | set(B["A2"][1])}
        E = regularize(lo, pw)
        c = sp.expand(sp.diff(E, sp.Symbol(sym)))
        ct = sp.cancel(sp.together(c/ax))
        assert sp.fraction(ct)[1] == 1, nm
        pk[nm + "_c"], pk[nm + "_r"] = ct, sp.expand(E - c*sp.Symbol(sym))
    gzip.open(dest, "wb", compresslevel=9).write(json.dumps({k: sp.srepr(e) for k, e in pk.items()}, sort_keys=True).encode())
    print("written %s (%.0fs)" % (dest, time.time() - t0))


if __name__ == "__main__":
    if "--quick" in sys.argv:
        sys.exit(0 if quick() else 1)
    if "--full" in sys.argv:
        full(sys.argv[sys.argv.index("--full") + 1] if len(sys.argv) > sys.argv.index("--full") + 1 else EQS)
        sys.exit(0)
    print(__doc__)
