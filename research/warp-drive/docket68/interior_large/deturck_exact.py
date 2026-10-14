"""deturck_exact.py -- item 404: the DeTurck norm taken apart, every term evaluated exactly at each point.

M, 404: "the DeTurck norm is a coefficient ... we need to evaluate the DeTurck norm to its exact value at each point."
The record's norm (gen_eqs_fw.py) is phi = g_mk xi^m xi^k, a Lorentzian quadratic in the DeTurck vector
    xi^m = g^pq (Gamma^m_pq - Gammabar^m_pq),
with the reference metric gbar = the ansatz at T = S = A = B = 1, F = 0.  Being Lorentzian, phi can add terms of
opposite sign and hide large components.  So nothing here is lumped:
  - xi^m is derived symbolically from the record's own metric and reference (as gen_eqs_fw.py builds them, not copied
    from its pickle), and only xi^s and xi^x survive: xi^tau, xi^theta and xi^phi vanish identically (K1);
  - each surviving component is split exactly into its terms -- one per field and slope, alpha_f dX_f/ds and
    beta_f dX_f/dx, plus the part that carries no derivative -- and the split is checked to recompose the component
    (K2), and phi to recompose the record's own PHI (K3);
  - every term is evaluated at 50 digits from each part's own interpolating polynomial: the x-slopes are that
    polynomial's exact derivative, the s-slopes are the evolved X_s, and at a joining both copies are reported, each
    from its own part, with no penalty and no averaging;
  - phi is reported as its three pieces, g_ss (xi^s)^2, 2 g_sx xi^s xi^x and g_xx (xi^x)^2.
Exact means: exact for the saved representation (the stored doubles, read as exact numbers), to 50 digits.

python3 deturck_exact.py [pickle] [s ...]   -- the table at the steps nearest each s (default: the fifth attempt's
                                               zeno_half_dsem5_10.pkl at s = -1.5, -1.85, -2.006); DETURCK-EXACT.tsv
python3 deturck_exact.py --selftest | --mutants
"""
import sys, pickle
import numpy as np, sympy as sp, mpmath as mp

mp.mp.dps = 50
NAMES = ["T", "S", "A", "B", "F"]
MUT = set()
tau, s, x, th, ph = sp.symbols("tau s x theta phi", real=True)
bt = sp.Symbol("bt", positive=True)
COORDS = [tau, s, x, th, ph]
VAL = {n: sp.Symbol(n) for n in NAMES}
DS = {n: sp.Symbol(n + "_s") for n in NAMES}
DX = {n: sp.Symbol(n + "_x") for n in NAMES}


def metric(T, S, A, B, F):
    """the record's ansatz (gen_eqs_fw.py): FW's RSII large hole in s = r^2 and x"""
    f = 1 - s; g = 2 - x ** 2; Dl = 1 / bt + (1 - x ** 2) / f
    G = sp.zeros(5, 5)
    G[0, 0] = s * T / Dl ** 2
    G[1, 1] = A / (f ** 4 * s) / Dl ** 2
    G[2, 2] = 4 * B / (f ** 2 * g) / Dl ** 2
    G[1, 2] = G[2, 1] = x * F / (2 * f ** 3) / Dl ** 2
    G[3, 3] = x ** 2 * g * S / f ** 2 / Dl ** 2
    G[4, 4] = G[3, 3] * sp.sin(th) ** 2
    return G


def christoffel(G, Gi):
    return [[[sum(Gi[a, d] * (sp.diff(G[d, b], COORDS[c]) + sp.diff(G[d, c], COORDS[b]) - sp.diff(G[b, c], COORDS[d]))
                  for d in range(5)) / 2 for c in range(5)] for b in range(5)] for a in range(5)]


def derive():
    """xi^m in the value and slope symbols, theta = pi/3 as the record sets it; returns (xi_up, G_sym)"""
    fn = {n: sp.Function(n)(s, x) for n in NAMES}
    G = metric(*[fn[n] for n in NAMES]); Gi = G.inv()
    ref = (1, 1, 1, 1, 0) if "ref" not in MUT else (1, 1, 1, 1, 1)
    Gb = metric(*ref); Gbi = Gb.inv()
    Gam = christoffel(G, Gi); Gamb = christoffel(Gb, Gbi)
    if "dropterm" in MUT:
        Gamb[1][1][1] = 0
    xi_up = [sum(Gi[p, q] * (Gam[m][p][q] - Gamb[m][p][q]) for p in range(5) for q in range(5)) for m in range(5)]
    rep = {}
    for n in NAMES:
        rep[sp.diff(fn[n], s)] = DS[n]; rep[sp.diff(fn[n], x)] = DX[n]
    order = sorted(rep, key=lambda q: -sp.count_ops(q))

    def R(e):
        e = e.subs({d: rep[d] for d in order}).subs({fn[n]: VAL[n] for n in NAMES})
        return e.subs(th, sp.pi / 3)
    return [R(e) for e in xi_up], G.subs({fn[n]: VAL[n] for n in NAMES}).subs(th, sp.pi / 3)


def split(e):
    """e = rest + sum over slopes of coef * slope, exactly (e is linear in the slopes)"""
    slopes = [DS[n] for n in NAMES] + [DX[n] for n in NAMES]
    coefs = {d: sp.diff(e, d) for d in slopes}
    rest = e.subs({d: 0 for d in slopes})
    return rest, coefs


class Exact:
    def __init__(self, derived=None):
        xi, Gs = derived or derive()
        self.xi = xi; self.G = Gs
        self.args = [s, x, bt] + [VAL[n] for n in NAMES] + [DS[n] for n in NAMES] + [DX[n] for n in NAMES]
        L = lambda e: sp.lambdify(self.args, e, "mpmath")
        self.parts = {}
        for m, lab in ((1, "s"), (2, "x")):
            rest, coefs = split(xi[m])
            self.parts[lab] = (L(rest), {k: L(v) for k, v in coefs.items()}, L(xi[m]))
        self.g = {k: L(Gs[i, j]) for k, (i, j) in {"ss": (1, 1), "sx": (1, 2), "xx": (2, 2)}.items()}

    def at(self, sv, xv, bv, vals, ds, dx):
        """every term at one point: values, s-slopes and x-slopes as dicts over the five fields (mpf)"""
        a = [sv, xv, bv] + [vals[n] for n in NAMES] + [ds[n] for n in NAMES] + [dx[n] for n in NAMES]
        out = {}
        for lab in ("s", "x"):
            rest, coefs, full = self.parts[lab]
            terms = {"rest": rest(*a)}
            for n in NAMES:
                terms["d%s/ds" % n] = coefs[DS[n]](*a) * ds[n]
                terms["d%s/dx" % n] = coefs[DX[n]](*a) * dx[n]
            out["xi^" + lab] = (sum(terms.values()), terms, full(*a))
        gss, gsx, gxx = (self.g[k](*a) for k in ("ss", "sx", "xx"))
        xs, xx = out["xi^s"][0], out["xi^x"][0]
        sgn = -1 if "phisign" in MUT else 1
        out["phi"] = {"gss xs^2": gss * xs * xs, "2 gsx xs xx": sgn * 2 * gsx * xs * xx, "gxx xx^2": gxx * xx * xx}
        return out


# ------------------------------------------------------------------ the representation: each part's own polynomial
def bary_w(nodes):
    n = len(nodes)
    return [1 / mp.fprod([nodes[j] - nodes[k] for k in range(n) if k != j]) for j in range(n)]


def poly_at(nodes, w, f, xv):
    """value and exact first derivative of the interpolant through (nodes, f) at xv (mpf)"""
    for i, xi in enumerate(nodes):
        if xv == xi:
            d = mp.mpf(0)
            for j, xj in enumerate(nodes):
                if j != i:
                    d += (w[j] / w[i]) / (xi - xj) * (f[j] - f[i])
            return f[i], d
    num = sum(w[j] * f[j] / (xv - nodes[j]) for j in range(len(nodes)))
    den = sum(w[j] / (xv - nodes[j]) for j in range(len(nodes)))
    p = num / den
    dp = sum(w[j] * (p - f[j]) / (xv - nodes[j]) ** 2 for j in range(len(nodes))) / den
    return p, dp


def parts_of(I, X, Xs):
    """each part's nodes and the five fields' values and s-slopes there, as mpf; the axis part on its full
    symmetric nodes, every field extended evenly (all five are even in x)"""
    full, P, Mi = I.fold
    out = []
    for k, (idx, Dl, D2l, w, loc) in enumerate(I.blk):
        if k == 0:
            nodes = [mp.mpf(float(v)) for v in full]
            vals = {}; dss = {}
            for e, n in enumerate(NAMES):
                fv = np.zeros(len(full)); fv[P] = X[e, idx]; fv[Mi] = X[e, idx]
                sv = np.zeros(len(full)); sv[P] = Xs[e, idx]; sv[Mi] = Xs[e, idx]
                vals[n] = [mp.mpf(float(v)) for v in fv]; dss[n] = [mp.mpf(float(v)) for v in sv]
            stored = [int(np.where(P == p)[0][0]) if p in P else None for p in range(len(full))]
            out.append(dict(nodes=nodes, w=bary_w(nodes), vals=vals, ds=dss, lo=0.0, hi=float(full[-1]),
                            node_x=[float(full[p]) for p in P]))
        else:
            nodes = [mp.mpf(float(v)) for v in loc]
            vals = {n: [mp.mpf(float(v)) for v in X[e, idx]] for e, n in enumerate(NAMES)}
            dss = {n: [mp.mpf(float(v)) for v in Xs[e, idx]] for e, n in enumerate(NAMES)}
            out.append(dict(nodes=nodes, w=bary_w(nodes), vals=vals, ds=dss, lo=float(loc[0]), hi=float(loc[-1]),
                            node_x=[float(v) for v in loc]))
    return out


def evaluate(E, part, sv, bv, xv):
    xm = mp.mpf(xv); vals = {}; ds = {}; dx = {}
    for n in NAMES:
        vals[n], dx[n] = poly_at(part["nodes"], part["w"], part["vals"][n], xm)
        ds[n], _ = poly_at(part["nodes"], part["w"], part["ds"][n], xm)
    return E.at(mp.mpf(sv), xm, mp.mpf(bv), vals, ds, dx)


def load_steps(path, svals):
    import zeno_run as Z
    R = pickle.load(open(path, "rb")); ts, ys = R["t"], R["y"]
    mesh = R.get("mesh", "dsem5")
    kw = dict(edges=Z.DSEM5_EDGES, ns=Z.DSEM5_NS) if mesh == "dsem5" else dict(ns=Z.DSEM_NS)
    I = Z.FoldedDSEM(R.get("n", 10), Z.B, Z.STATIC, Z.KAP, Z.AT, n0=Z.SAT_N0, **kw); m = I.m
    P = np.repeat(Z.P_EXP, m); out = []
    for sv in svals:
        k = int(np.argmin(np.abs((1 - np.exp(ts)) - sv))); lam = ts[k]; ss = 1 - np.exp(lam); e = np.exp(-P * lam)
        X = (e * ys[:5 * m, k]).reshape(5, m)
        Xs = (-(e * (ys[5 * m:, k] - P * ys[:5 * m, k])) / np.exp(lam)).reshape(5, m)
        X, Xs = I.brane_values(ss, X, Xs)                    # F = F_s = 0 on the brane, as the scheme holds them
        out.append((ss, X, Xs))
    return I, out, Z.B


def report(path="zeno_half_dsem5_10.pkl", svals=(-1.5, -1.85, -2.006), per_part=24):
    E = Exact(); I, steps, bv = load_steps(path, svals)
    cols = (["s", "part", "x", "where"] + ["xi^s", "xi^x", "phi"] + ["gss xs^2", "2 gsx xs xx", "gxx xx^2"]
            + ["xi^%s %s" % (c, t) for c in ("s", "x") for t in ["rest"] + ["d%s/d%s" % (n, v) for n in NAMES
                                                                           for v in ("s", "x")]])
    rows = []; jumps = []
    for ss, X, Xs in steps:
        parts = parts_of(I, X, Xs)
        for k in range(len(parts) - 1):                      # the representation's own jump at each joining
            L, Rt = parts[k], parts[k + 1]
            jumps.append([ss, L["node_x"][-1]] + [L["vals"][n][-1] - Rt["vals"][n][0] for n in NAMES]
                         + [L["ds"][n][-1] - Rt["ds"][n][0] for n in NAMES])
        for k, part in enumerate(parts):
            pts = sorted(set([(xv, "node") for xv in part["node_x"]] +
                             [(float(v), "between") for v in np.linspace(part["lo"], part["hi"], per_part)[1:-1]]))
            for xv, where in pts:
                if k > 0 and xv == part["node_x"][0]:
                    where = "joining, right copy"
                elif xv == part["node_x"][-1] and k < len(parts) - 1:
                    where = "joining, left copy"
                o = evaluate(E, part, ss, bv, xv)
                phi = sum(o["phi"].values())
                row = [ss, k, xv, where, o["xi^s"][0], o["xi^x"][0], phi] + [o["phi"][c] for c in
                                                                              ("gss xs^2", "2 gsx xs xx", "gxx xx^2")]
                for c in ("s", "x"):
                    terms = o["xi^" + c][1]
                    row += [terms["rest"]] + [terms["d%s/d%s" % (n, v)] for n in NAMES for v in ("s", "x")]
                rows.append(row)
    with open("DETURCK-EXACT.tsv", "w") as fh:
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            fh.write("\t".join(mp.nstr(v, 17) if isinstance(v, mp.mpf) else str(v) for v in r) + "\n")
    with open("DETURCK-JUMPS.tsv", "w") as fh:
        fh.write("\t".join(["s", "x"] + ["J %s" % n for n in NAMES] + ["J %s_s" % n for n in NAMES]) + "\n")
        for r in jumps:
            fh.write("\t".join(mp.nstr(v, 17) if isinstance(v, mp.mpf) else str(v) for v in r) + "\n")
    return cols, rows, jumps


def summary(cols, rows, jumps=()):
    ci = {c: i for i, c in enumerate(cols)}
    for sv in sorted(set(r[0] for r in rows), reverse=True):
        R = [r for r in rows if r[0] == sv]
        big = max(R, key=lambda r: abs(r[ci["phi"]]))
        print("s = %.3f: %d points; max |phi| %s at x = %.4f (%s)" % (sv, len(R), mp.nstr(abs(big[ci["phi"]]), 4),
                                                                     big[2], big[3]))
        jx = [r for r in R if r[3].startswith("joining")]
        for r in jx:
            if abs(r[2] - 0.125) < 1e-12:
                print("   x = 1/8, %-20s xi^s %s  xi^x %s  phi %s = %s + %s + %s" % (
                    r[3], mp.nstr(r[ci["xi^s"]], 6), mp.nstr(r[ci["xi^x"]], 6), mp.nstr(r[ci["phi"]], 6),
                    mp.nstr(r[ci["gss xs^2"]], 4), mp.nstr(r[ci["2 gsx xs xx"]], 4), mp.nstr(r[ci["gxx xx^2"]], 4)))
                for c in ("s", "x"):
                    terms = sorted(((cols[i], r[i]) for i in range(len(cols)) if cols[i].startswith("xi^%s " % c)),
                                   key=lambda t: -abs(t[1]))[:4]
                    print("      largest terms of xi^%s: %s" % (c, ", ".join("%s %s" % (n.split(" ", 1)[1],
                                                                              mp.nstr(v, 4)) for n, v in terms)))
        for j in jumps:
            if j[0] == sv:
                print("   jump at x = %.4f: X %s | X_s %s" % (j[1], " ".join("%s %s" % (n, mp.nstr(v, 3)) for n, v
                                                                       in zip(NAMES, j[2:7])),
                                                        " ".join(mp.nstr(v, 3) for v in j[7:12])))


# ---------------------------------------------------------------------------------------------- selftest / mutants
def selftest(quiet=False):
    ok = []
    xi, Gs = derive()
    z = [sp.simplify(xi[m]) == 0 for m in (0, 3, 4)]
    ok.append(("K1 xi^tau, xi^theta, xi^phi vanish identically", all(z)))
    import random
    rnd = random.Random(7); worst2 = mp.mpf(0); worst3 = mp.mpf(0)
    import core_fw as C
    PHI = sp.lambdify([C.s, C.x, C.bt] + [sp.Symbol(n + t) for n in NAMES for t in C.tags], C.PHI, "mpmath")
    E = Exact((xi, Gs))
    for _ in range(6):
        sv = -mp.mpf(rnd.uniform(0.2, 2.0)); xv = mp.mpf(rnd.uniform(0.05, 0.95)); bv = mp.mpf(1)
        vals = {n: mp.mpf(rnd.uniform(0.5, 1.5)) for n in NAMES}; vals["F"] = mp.mpf(rnd.uniform(-0.3, 0.3))
        ds = {n: mp.mpf(rnd.uniform(-1, 1)) for n in NAMES}; dx = {n: mp.mpf(rnd.uniform(-1, 1)) for n in NAMES}
        o = E.at(sv, xv, bv, vals, ds, dx)
        for c in ("s", "x"):
            tot, terms, full = o["xi^" + c]
            worst2 = max(worst2, abs(tot - full) / (abs(full) + mp.mpf(10) ** -30))
        args = []
        for n in NAMES:
            args += [vals[n], ds[n], dx[n], 0, 0, 0]
        ref = PHI(sv, xv, bv, *args); mine = sum(o["phi"].values())
        worst3 = max(worst3, abs(mine - ref) / abs(ref))
    ok.append(("K2 each component recomposes exactly from its terms (worst %s)" % mp.nstr(worst2, 3), worst2 < 1e-40))
    ok.append(("K3 phi recomposes the record's PHI (eqs_fw.pkl) (worst %s)" % mp.nstr(worst3, 3), worst3 < 1e-30))
    one = {n: mp.mpf(1) for n in NAMES}; one["F"] = mp.mpf(0); zero = {n: mp.mpf(0) for n in NAMES}
    o = E.at(mp.mpf(-0.7), mp.mpf(0.4), mp.mpf(1), one, zero, zero)
    r = max(abs(o["xi^s"][0]), abs(o["xi^x"][0]))
    ok.append(("K4 control: the reference metric itself has xi = 0 (%s)" % mp.nstr(r, 3), r < 1e-40))
    # nodes and test points share one spelling: a float-built node is not mpf("0.13"), and 1e-18 from a node the
    # quotient form loses ~16 digits -- the report reads nodes and points from the same stored doubles
    nodes = [mp.mpf(v) for v in ("0", "0.13", "0.4", "0.61", "0.9", "1")]; w = bary_w(nodes)
    f = [3 * t ** 5 - t ** 3 + 2 * t for t in nodes]
    e5 = max(abs(poly_at(nodes, w, f, mp.mpf(t))[1] - (15 * mp.mpf(t) ** 4 - 3 * mp.mpf(t) ** 2 + 2))
             for t in ("0.13", "0.27", "0.9"))
    ok.append(("K5 the polynomial's slope is exact, at a node and between (%s)" % mp.nstr(e5, 3), e5 < 1e-40))
    if not quiet:
        for name, good in ok:
            print("%s  %s" % ("PASS" if good else "FAIL", name))
    return all(g for _, g in ok), ok


def mutants():
    caught = []
    for mname, what in (("ref", "reference metric with F = 1"), ("dropterm", "one reference Christoffel dropped"),
                        ("phisign", "the cross term's sign flipped")):
        MUT.clear(); MUT.add(mname)
        good, ok = selftest(quiet=True)
        caught.append((what, not good, [n.split()[0] for n, g in ok if not g]))
    MUT.clear()
    for what, c, fails in caught:
        print("%s  %-40s failed: %s" % ("caught" if c else "MISSED", what, ", ".join(fails) or "none"))
    return all(c for _, c, _ in caught)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        good, _ = selftest(); print("selftest: %s" % ("PASS" if good else "FAIL")); sys.exit(0 if good else 1)
    elif "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    else:
        args = [a for a in sys.argv[1:]]
        path = args[0] if args and args[0].endswith(".pkl") else "zeno_half_dsem5_10.pkl"
        svals = tuple(float(a) for a in args if not a.endswith(".pkl")) or (-1.5, -1.85, -2.006)
        cols, rows, jumps = report(path, svals)
        summary(cols, rows, jumps)
