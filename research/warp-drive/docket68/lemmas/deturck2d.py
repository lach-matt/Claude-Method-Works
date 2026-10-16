#!/usr/bin/env python3
"""deturck2d.py -- item 450: the toolkit for stage 3b's two-dimensional solves (BOUNCE-RESEARCH section 17).  The
Einstein-DeTurck operator E_ab = R_ab + 4 g_ab - nabla_(a xi_b), xi^a = g^bc (Gamma^a_bc - Gammabar^a_bc), which
"renders the Einstein equation strictly elliptic" (Headrick, Kitchen and Wiseman 0905.1822, READ; review: Dias, Santos
and Way 1510.02804), for a static metric in (t, X, u, theta, phi) with an S^2 factor, the unknown functions of (X, u)
entering through their jets; Chebyshev collocation and finite differences of orders 2 and 4 on x = tanh(a X) and u in
[0, 1]; and Newton's method with the Jacobian by the complex step.  M: "1 - both, and compare".  Labels: READ (the
quotation above), computed (sympy exact where marked; numerical otherwise), deduced.  Worked in the conversation; not
verified; not seated.  2026-10-16.

  K0 (read) M's word: 450.
  K1 (computed) The differentiation matrices: Chebyshev to 1e-10 at N = 32 on exp(sin 2x); the Fornberg finite
     differences converge at their orders, 2 and 4, up to the ends.
  K2 (computed) Newton on a manufactured problem with an axis row: Chebyshev reaches rounding by N = 16; the finite
     differences converge at orders 2 and 4.
  K3 (computed) The axis without a row (open_axis): the S^3-polar operator 4u(1-u) f_uu + (6-8u) f_u has indicial
     exponents 0 and -1/2 at u = 0, and the grid that omits u = 0 selects the regular branch by itself (Boyd's
     behavioural condition): Chebyshev to rounding by N = 16, finite differences converging.
  K4 (computed) The operator: Schwarzschild-AdS5, -f dt^2 + dr^2/f + r^2 (dchi^2 + sin^2 chi dOmega_2^2) with
     f = 1 + r^2 - mu/r^2 entered as an unknown function through its jets, gives R_ab + 4 g_ab = 0 to rounding at
     sample points (reference = itself, so xi = 0 identically); the four-dimensional falloff mu/r in its place
     does not.
  K5 (deduced) The toolkit discretizes the operator both ways M asked for, and each part is checked against an
     answer known in closed form before stage3b_v1.py uses it.

python3 deturck2d.py [--selftest | --mutants]
"""
import math
import os
import re
import sys

import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ('"1 - both, and compare',)
JETS = ("", "_X", "_u", "_XX", "_Xu", "_uu")
NEXT = {"": {"X": "_X", "u": "_u"}, "_X": {"X": "_XX", "u": "_Xu"}, "_u": {"X": "_Xu", "u": "_uu"}}
X, u, th = sp.symbols("X u theta")


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


# ---------------------------------------------------------------------------------------------------- the grids
def cheb(N):
    """Trefethen's cheb: x_j = cos(pi j/N), j = 0..N, and the differentiation matrix"""
    x = np.cos(np.pi * np.arange(N + 1) / N)
    c = np.hstack([2, np.ones(N - 1), 2]) * (-1) ** np.arange(N + 1)
    dX = np.subtract.outer(x, x)
    D = np.outer(c, 1 / c) / (dX + np.eye(N + 1))
    return D - np.diag(D.sum(axis=1)), x


def fornberg(z, xs, m):
    """Fornberg's weights for derivatives 0..m at z from the nodes xs"""
    n = len(xs)
    c = np.zeros((n, m + 1))
    c1, c4 = 1.0, xs[0] - z
    c[0, 0] = 1.0
    for i in range(1, n):
        mn, c2, c5, c4 = min(i, m), 1.0, c4, xs[i] - z
        for j in range(i):
            c3 = xs[i] - xs[j]
            c2 *= c3
            if j == i - 1:
                for k in range(mn, 0, -1):
                    c[i, k] = c1 * (k * c[i - 1, k - 1] - c5 * c[i - 1, k]) / c2
                c[i, 0] = -c1 * c5 * c[i - 1, 0] / c2
            for k in range(mn, 0, -1):
                c[j, k] = (c4 * c[j, k] - k * c[j, k - 1]) / c3
            c[j, 0] = c4 * c[j, 0] / c3
        c1 = c2
    return c


def fd_nodes(xs, order=2):
    """first and second derivative matrices on sorted nodes: centred (order+1)-point stencils inside, one-sided
    (order+2)-point stencils where a centred one does not fit"""
    if "fd_order" in MUT:
        order = 2
    n = len(xs)
    D, D2 = np.zeros((n, n)), np.zeros((n, n))
    h = order // 2
    for i in range(n):
        if h <= i < n - h:
            idx = list(range(i - h, i + h + 1))
        else:
            lo = 0 if i < h else n - order - 2
            idx = list(range(lo, lo + order + 2))
        w = fornberg(xs[i], xs[idx], 2)
        D[i, idx], D2[i, idx] = w[:, 1], w[:, 2]
    return D, D2


def bary_weights(xs):
    n = len(xs)
    return np.array([1 / np.prod([xs[j] - xs[k] for k in range(n) if k != j]) for j in range(n)])


def bary(xs):
    """the polynomial differentiation matrix on distinct nodes"""
    w = bary_weights(xs)
    D = np.zeros((len(xs), len(xs)))
    for i in range(len(xs)):
        for j in range(len(xs)):
            if i != j:
                D[i, j] = (w[j] / w[i]) / (xs[i] - xs[j])
        D[i, i] = -D[i].sum()
    return D


def interp_matrix(nodes, targets):
    """barycentric Lagrange interpolation from nodes to targets"""
    w = bary_weights(nodes)
    M = np.zeros((len(targets), len(nodes)))
    for i, t in enumerate(targets):
        d = t - nodes
        hit = np.where(np.abs(d) < 1e-15)[0]
        if len(hit):
            M[i, hit[0]] = 1.0
        else:
            M[i] = (w / d) / np.sum(w / d)
    return M


class Ops:
    """two-dimensional jet operators on x = tanh(a X) in [-1, 1] (both ends nodes) and u in [0, 1]; open_axis: the
    u-grid omits u = 0, so the axis carries no row and its regularity is behavioural"""

    def __init__(self, Nx, Nu, kind="cheb", order=2, open_axis=False, a=1.0):
        self.kind, self.a = kind, a
        if kind == "cheb":
            Dx, x = cheb(Nx)
            D2x = Dx @ Dx
            if open_axis:
                v = np.cos(np.pi * np.arange(Nu) / Nu)
                Dv = bary(v)
            else:
                Dv, v = cheb(Nu)
            D2v = Dv @ Dv
        else:
            x = np.linspace(-1, 1, Nx + 1)
            Dx, D2x = fd_nodes(x, order)
            v = np.linspace(-1, 1, Nu + 1)[1:] if open_axis else np.linspace(-1, 1, Nu + 1)
            Dv, D2v = fd_nodes(v, order)
        self.x, self.u = x, (1 + v) / 2
        w = a * (1 - x ** 2)
        DX = np.diag(w) @ Dx
        DXX = np.diag(w ** 2) @ D2x + np.diag(-2 * a * x * w) @ Dx
        Du, Duu = 2 * Dv, 4 * D2v
        self.sparse = kind != "cheb"
        kr = (lambda p, q: sps.kron(sps.csr_matrix(p), sps.csr_matrix(q), format="csr")) if self.sparse else np.kron
        Ix, Iu = np.eye(len(x)), np.eye(len(self.u))
        self.D = {"": kr(Ix, Iu), "_X": kr(DX, Iu), "_u": kr(Ix, Du),
                  "_XX": kr(DXX, Iu), "_Xu": kr(DX, Du), "_uu": kr(Ix, Duu)}
        XX, UU = np.meshgrid(x, self.u, indexing="ij")
        self.xg, self.ug = XX.ravel(), UU.ravel()
        self.n = len(self.xg)

    def Xof(self, x):
        with np.errstate(all="ignore"):
            return np.arctanh(np.clip(x, -1 + 1e-16, 1 - 1e-16)) / self.a


# ---------------------------------------------------------------------------------------------------- Newton
_COMPILED = {}


class Newton:
    """eqs, axis_eqs: one sympy expression per function, in X, u, the params and the jets; Dirichlet rows at x = +-1
    and u = 1 with the values bvals; axis rows at u = 0 when the grid has that node; cstep: jet derivatives by the
    complex step (exact to rounding)"""

    def __init__(self, funcs, eqs, axis_eqs, bvals, params, ops, cstep=True):
        self.funcs, self.ops, self.bvals, self.cstep = funcs, ops, bvals, cstep
        self.js = [sp.Symbol(f + j) for f in funcs for j in JETS]
        ps = list(params.keys())
        self.pvals = [params[p] for p in ps]
        args = [X, u] + ps + self.js

        def comp(exprs):
            out = []
            for e in exprs:
                key = (e, tuple(args), cstep)               # the key holds e, so no other expression takes its id
                if key not in _COMPILED:
                    _COMPILED[key] = (sp.lambdify(args, e, "numpy", cse=True),
                                      None if cstep else [sp.lambdify(args, sp.diff(e, j), "numpy")
                                                          for j in self.js])
                out.append(_COMPILED[key])
            return out
        self.E, self.A = comp(eqs), comp(axis_eqs)

    def jets(self, U):
        n = self.ops.n
        return [self.ops.D[j] @ U[m * n:(m + 1) * n] for m in range(len(self.funcs)) for j in JETS]

    def residual_and_jacobian(self, U):
        o, nf, n = self.ops, len(self.funcs), self.ops.n
        x, uu = o.xg, o.ug
        Xg = o.Xof(x)
        Jv = self.jets(U)
        R = np.zeros(nf * n)
        blocks = [[None] * nf for _ in range(nf)]
        dirich = (np.abs(x) > 1 - 1e-14) | (uu > 1 - 1e-14)
        axis = (uu < 1e-14) & ~dirich
        inner = ~dirich & ~axis
        npre = 2 + len(self.pvals)
        for k in range(nf):
            for mask, (f, dfs) in ((inner, self.E[k]), (axis, self.A[k])):
                if not mask.any():
                    continue
                idx = np.where(mask)[0]
                a = [Xg[idx], uu[idx]] + self.pvals + [jv[idx] for jv in Jv]
                R[k * n + idx] = np.real(np.broadcast_to(f(*a), idx.shape))
                for jj in range(len(self.js)):
                    if self.cstep:
                        ac = list(a)
                        ac[npre + jj] = a[npre + jj] + 1e-30j
                        c = np.broadcast_to(np.imag(f(*ac)) / 1e-30, idx.shape)
                    else:
                        c = np.broadcast_to(dfs[jj](*a), idx.shape)
                    if not np.any(c):
                        continue
                    m, j = divmod(jj, len(JETS))
                    full = np.zeros(n)
                    full[idx] = c
                    term = (sps.diags(full) @ o.D[JETS[j]]) if o.sparse else full[:, None] * o.D[JETS[j]]
                    blocks[k][m] = term if blocks[k][m] is None else blocks[k][m] + term
            idx = np.where(dirich)[0]
            R[k * n + idx] = U[k * n + idx] - self.bvals[k]
            dd = np.zeros(n)
            dd[idx] = 1.0
            eye = sps.diags(dd) if o.sparse else np.diag(dd)
            blocks[k][k] = eye if blocks[k][k] is None else blocks[k][k] + eye
        for k in range(nf):
            for m in range(nf):
                if blocks[k][m] is None:
                    blocks[k][m] = sps.csr_matrix((n, n)) if o.sparse else np.zeros((n, n))
        return R, (sps.bmat(blocks, format="csc") if o.sparse else np.block(blocks))

    def solve(self, U0, tol=1e-11, steptol=1e-13, maxit=30):
        """stops on |R| < tol or a full step below steptol: a residual built from N^4-sized second-derivative
        matrices cannot fall below about N^4 times the rounding unit"""
        U, hist = U0.copy(), []
        for _ in range(maxit):
            R, Jac = self.residual_and_jacobian(U)
            r = float(np.max(np.abs(R)))
            hist.append(r)
            if r < tol:
                break
            dU = spla.spsolve(Jac, -R) if self.ops.sparse else np.linalg.solve(Jac, -R)
            if np.max(np.abs(dU)) < steptol:
                break
            lam = 1.0
            for _ in range(20):
                Rn, _ = self.residual_and_jacobian(U + lam * dU)
                if np.max(np.abs(Rn)) < (1 - 1e-4 * lam) * r or lam < 1e-3:
                    break
                lam /= 2
            U = U + lam * dU
        return U, hist


# ---------------------------------------------------------------------------------------------------- the operator
def jetsyms(funcs):
    return {f + j: sp.Symbol(f + j) for f in funcs for j in JETS}


def make_D(funcs, J):
    def D(e, c):
        """total derivative of e along coordinate c (0 t, 1 X, 2 u, 3 theta, 4 phi), by the chain rule on jets"""
        if c in (0, 4):
            return sp.Integer(0)
        if c == 3:
            return sp.diff(e, th)
        v = X if c == 1 else u
        r = sp.diff(e, v)
        if "no_chain" in MUT:
            return r
        fs = e.free_symbols
        for f in funcs:
            for j in ("", "_X", "_u"):
                if J[f + j] in fs:
                    r += sp.diff(e, J[f + j]) * J[f + NEXT[j][v.name]]
        return r
    return D


def inverse(g):
    """block inverse: tt, the (X, u) block, theta, phi"""
    gi = sp.zeros(5, 5)
    gi[0, 0] = 1 / g[0, 0]
    det = g[1, 1] * g[2, 2] - g[1, 2] ** 2
    gi[1, 1], gi[2, 2], gi[1, 2] = g[2, 2] / det, g[1, 1] / det, -g[1, 2] / det
    gi[2, 1] = gi[1, 2]
    gi[3, 3], gi[4, 4] = 1 / g[3, 3], 1 / g[4, 4]
    return gi


def christoffel(g, gi, D):
    dg = [[[D(g[a, b], c) for c in range(5)] for b in range(5)] for a in range(5)]
    return [[[sum(gi[a, d] * (dg[d][b][c] + dg[d][c][b] - dg[b][c][d]) for d in range(5) if gi[a, d] != 0) / 2
              for c in range(5)] for b in range(5)] for a in range(5)]


def operator(g, gbar, funcs, comps=((0, 0), (1, 1), (2, 2), (1, 2), (3, 3)), Lam=4):
    """E_ab = R_ab + Lam g_ab - nabla_(a xi_b) for the listed components, xi^a, and the jet symbols; nothing is
    simplified"""
    J = jetsyms(funcs)
    D = make_D(funcs, J)
    gi = inverse(g)
    G = christoffel(g, gi, D)
    Gb = christoffel(gbar, inverse(gbar), D)
    xi_up = [sum(gi[b, c] * (G[a][b][c] - Gb[a][b][c]) for b in range(5) for c in range(5) if gi[b, c] != 0)
             for a in range(5)]
    xi = [sum(g[a, b] * xi_up[b] for b in range(5) if g[a, b] != 0) for a in range(5)]
    sg = -1 if "ricci_sign" in MUT else 1
    out = {}
    for (a, b) in comps:
        R = (sum(D(G[c][a][b], c) for c in range(5)) - sum(D(G[c][a][c], b) for c in range(5))
             + sg * sum(G[c][c][d] * G[d][a][b] for c in range(5) for d in range(5))
             - sum(G[c][b][d] * G[d][a][c] for c in range(5) for d in range(5)))
        nab = (D(xi[b], a) + D(xi[a], b)) / 2 - sum(G[c][a][b] * xi[c] for c in range(5))
        out[(a, b)] = R + Lam * g[a, b] - nab
    return out, xi_up, J


def kretschmann_builder(g, funcs, args):
    """a numerical K = R_abcd R^abcd from Gamma and its derivatives, lambdified over args (theta at pi/3)"""
    J = jetsyms(funcs)
    D = make_D(funcs, J)
    gi = inverse(g)
    G = christoffel(g, gi, D)
    Gl = [G[a][b][c] for a in range(5) for b in range(5) for c in range(5)]
    dGl = [D(G[a][b][c], d) for a in range(5) for b in range(5) for c in range(5) for d in range(5)]
    ex = [e.subs(th, sp.pi / 3) for e in Gl + dGl + [g[a, b] for a in range(5) for b in range(5)]
          + [gi[a, b] for a in range(5) for b in range(5)]]
    fn = sp.lambdify(args, ex, "numpy", cse=True)

    def K(*vals):
        arr = fn(*vals)
        npt = max(np.size(v) for v in arr)
        arr = [np.broadcast_to(np.asarray(v, dtype=float), (npt,)) for v in arr]
        Gm = np.array(arr[:125]).reshape(5, 5, 5, npt)
        dG = np.array(arr[125:750]).reshape(5, 5, 5, 5, npt)            # dG[a,b,c,d] = d_d Gamma^a_bc
        gm = np.array(arr[750:775]).reshape(5, 5, npt)
        gim = np.array(arr[775:800]).reshape(5, 5, npt)
        Rm = (np.einsum("adbcn->abcdn", dG) - np.einsum("acbdn->abcdn", dG)
              + np.einsum("acen,edbn->abcdn", Gm, Gm) - np.einsum("aden,ecbn->abcdn", Gm, Gm))
        Rl = np.einsum("aen,ebcdn->abcdn", gm, Rm)
        Ru = np.einsum("bfn,cgn,dhn,ebcdn->efghn", gim, gim, gim, Rm)
        return np.einsum("abcdn,abcdn->n", Rl, Ru)
    return K


# ---------------------------------------------------------------------------------------------------- checks
def k1():
    D, x = cheb(32)
    f = np.exp(np.sin(2 * x))
    ok_c = np.max(np.abs(D @ f - 2 * np.cos(2 * x) * f)) < 1e-10
    rates = {}
    for o in (2, 4):
        e = []
        for N in (32, 64):
            xs = np.linspace(-1, 1, N + 1)
            Df, D2f = fd_nodes(xs, o)
            ff = np.exp(np.sin(2 * xs))
            e.append(np.max(np.abs(D2f @ ff - (-4 * np.sin(2 * xs) + 4 * np.cos(2 * xs) ** 2) * ff)))
        rates[o] = math.log2(e[0] / e[1])
    return ok_c, rates


def _toy(fex_expr, coef_uu, coef_u, open_axis, runs):
    f, fXX, fuu, fu = sp.symbols("f f_XX f_uu f_u")
    L = sp.diff(fex_expr, X, 2) + coef_uu * sp.diff(fex_expr, u, 2) + coef_u * sp.diff(fex_expr, u)
    E = fXX + coef_uu * fuu + coef_u * fu + f ** 2 - (L + fex_expr ** 2)
    ex = sp.lambdify((X, u), fex_expr, "numpy")
    out = {}
    for kind, order, N in runs:
        ops = Ops(N, N, kind, order, open_axis=open_axis)
        nw = Newton(["f"], [E], [sp.Symbol("f") - 1], [1.0], {}, ops)
        U, _ = nw.solve(np.ones(ops.n))
        out[(kind, order, N)] = float(np.max(np.abs(U - ex(ops.Xof(ops.xg), ops.ug))))
    return out


FEX = (1 + sp.Rational(3, 10) * u * (1 - u) / sp.cosh(X) ** 2 * sp.exp(sp.tanh(X) + u)
       + sp.Rational(1, 5) * u ** 2 * (1 - u) * sp.tanh(X) / sp.cosh(X) ** 2 * sp.cos(3 * u))
RUNS = [("cheb", 2, 16), ("fd", 2, 16), ("fd", 2, 32), ("fd", 4, 16), ("fd", 4, 32)]


def k2():
    return _toy(FEX, 1, 0, False, RUNS)


def k3():
    return _toy(FEX, 4 * u * (1 - u), 6 - 8 * u, True, RUNS)


def k4():
    """Schwarzschild-AdS5 with X = r and u = chi: f enters as the unknown F through its jets"""
    mu = sp.Rational(3, 10)
    J = jetsyms("F")
    g = sp.zeros(5, 5)
    g[0, 0], g[1, 1], g[2, 2] = -J["F"], 1 / J["F"], X ** 2
    g[3, 3], g[4, 4] = X ** 2 * sp.sin(u) ** 2, X ** 2 * sp.sin(u) ** 2 * sp.sin(th) ** 2
    E, xi, _ = operator(g, g, "F")
    worst, ctrl = 0.0, 0.0
    for (Xv, uv, tv) in ((1.3, 0.4, 0.9), (2.2, 1.1, 1.7), (0.9, 2.5, 0.3)):
        # the control is the four-dimensional falloff mu/r, which no five-dimensional vacuum has
        for fe, store in ((1 + X ** 2 - mu / X ** 2, "w"), (1 + X ** 2 - mu / X, "c")):
            sub = {J["F"]: fe, J["F_X"]: sp.diff(fe, X), J["F_XX"]: sp.diff(fe, X, 2)}
            sub = {k: v.subs(X, Xv) for k, v in sub.items()}
            sub.update({J["F_u"]: 0, J["F_Xu"]: 0, J["F_uu"]: 0, X: Xv, u: uv, th: tv})
            r = max(abs(float(v.subs(sub))) for v in E.values())
            if store == "w":
                worst = max(worst, r)
            else:
                ctrl = max(ctrl, r)
    return worst, ctrl, all(sp.simplify(x) == 0 for x in xi)


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words(); ok.append(r); say("K0 words: %s" % r)
    c, rates = k1()
    r = c and 1.7 < rates[2] < 2.5 and 3.5 < rates[4] < 5.0
    ok.append(r); say("K1 Chebyshev 1e-10 at N=32: %s; FD second-derivative orders %.2f, %.2f: %s" % (c, rates[2],
                                                                                                     rates[4], r))
    for name, res in (("K2 (axis row)", k2()), ("K3 (behavioural axis)", k3())):
        p2 = math.log2(res[("fd", 2, 16)] / res[("fd", 2, 32)])
        p4 = math.log2(res[("fd", 4, 16)] / res[("fd", 4, 32)])
        r = res[("cheb", 2, 16)] < 1e-12 and 1.4 < p2 < 2.6 and p4 > 3.0
        ok.append(r)
        say("%s Chebyshev N=16 err %.1e; FD orders %.2f, %.2f: %s" % (name, res[("cheb", 2, 16)], p2, p4, r))
    w, cc, xi0 = k4()
    r = w < 1e-10 and cc > 1e-2 and xi0
    ok.append(r); say("K4 Schwarzschild-AdS5 through jets: R+4g %.1e; mu/r control %.1e; xi = 0: %s" % (w, cc, r))
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    caught = 0
    names = ("no_chain", "ricci_sign", "fd_order")
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-10s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    selftest()
