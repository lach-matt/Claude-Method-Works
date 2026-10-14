"""zeno_run.py -- item 393: the first Zeno half of the large hole's interior (items 392-393; ../lemmas/zeno_method.py).

One rescaled restart at bt = 1, from the trusted state near s = -0.5 (B7's damped run, Nx = 28, kap = 4, tilt 0.5),
carried over one halving of u = 1/(1 - s) -- the variable of B6's power laws -- at one fixed resolution per mesh part.
  - time: lambda = ln(1 - s), so one halving of u is Delta lambda = ln 2; the fields are carried as Xt = u^-p X with
    B6's exponents p = (T 1, S -2, A 1, B -2, F -1), so that they stay of order one;
  - the bulk coordinate: a halving mesh toward the brane, parts [0, 1/2], [1/2, 3/4], [3/4, 7/8], [7/8, 1], each with
    the same Lobatto points; at each interface the x-derivative is continuous (an algebraic row, as the axis row is);
  - the test (item 392's criterion): the DeTurck norm phi <= 1e-4 and every part's Chebyshev tail <= 1e-6 at the
    half's end; the run is stopped at 20 minutes of wall time.

python3 zeno_run.py trusted                 -- the trusted state: B7's damped Nx = 28 run from s = -0.002 to -0.503
python3 zeno_run.py half [n_per_part] [mesh] -- the Zeno half from that state; mesh "sat" (item 394, the folded axis and
                                              the energy-derived coupling) or "patch" (item 393's derivative continuity)
"""
import numpy as np, sys, time, pickle, os
import core_fw as C, interior_fw as IF, interior_damp as ID
from scipy.integrate import solve_ivp

B, KAP, AT = 1.0, 4.0, 0.5
S0, S1 = -0.002, -0.503
P_EXP = np.array([1.0, -2.0, 1.0, -2.0, -1.0])            # B6: T, A ~ u; S, B ~ u^-2; F ~ u^-1
STATIC = dict(file=C.static_file(B, 24, 24), Ns=24, Nx=24)
TRUSTED = "zeno_trusted_28.pkl"
WALL = 20 * 60.0
SAT_N0, SAT_NS = 15, (10, 10, 10, 10, 14)        # item 394: the axis part and the brane part given more points


class Halving(ID.Damped):
    """the damped interior on a halving mesh toward the brane: n Lobatto intervals in each of `parts` parts"""

    def __init__(self, n, b, static, kap, at, parts=4):
        edges = [0.0] + [1 - 0.5 ** k for k in range(1, parts)] + [1.0]
        nodes, self.doms = [0.0], []
        for a, c in zip(edges[:-1], edges[1:]):
            loc = a + (c - a) * C.lobatto01(n)
            i0 = len(nodes) - 1
            nodes += list(loc[1:])
            self.doms.append((i0, i0 + n, C.bary_D(loc), loc))
        super().__init__(len(nodes) - 1, b, static, kap, at)
        xn = np.array(nodes); Nn = len(xn)
        self.xn = xn
        D = np.zeros((Nn, Nn)); D2 = np.zeros((Nn, Nn))
        for k, (i0, i1, Dl, loc) in enumerate(self.doms):
            idx = np.arange(i0, i1 + 1); Dl2 = Dl @ Dl
            rows = range(0 if k == 0 else 1, n + 1)            # each node's row from its own part; interfaces: left
            for r in rows:
                D[i0 + r, idx] = Dl[r]; D2[i0 + r, idx] = Dl2[r]
        self.D, self.D2 = D, D2
        self.ifc = [d[1] for d in self.doms[:-1]]              # interface nodes
        self.alg = [0] + self.ifc                              # algebraic nodes: the axis and the interfaces
        self.inner = np.array([i for i in range(1, Nn - 1) if i not in self.ifc]); self.m = len(self.inner)
        # the rows that fix the algebraic nodes: x-derivative zero on the axis, continuous at each interface
        L = np.zeros((len(self.alg), Nn))
        L[0, self.doms[0][0]:self.doms[0][1] + 1] = self.doms[0][2][0]
        for j, (dl, dr) in enumerate(zip(self.doms[:-1], self.doms[1:])):
            L[j + 1, dl[0]:dl[1] + 1] += dl[2][-1]; L[j + 1, dr[0]:dr[1] + 1] -= dr[2][0]
        self.L = L
        oth = [i for i in range(Nn) if i not in self.alg]
        self.oth = oth
        self.Ainv = np.linalg.inv(L[:, self.alg]); self.Loth = L[:, oth]
        # for S the axis row is S = B (interior_fw.axis): the interfaces alone are solved, the axis value given
        self.Ainv_i = np.linalg.inv(L[1:, self.ifc]); self.L_ax = L[1:, 0]; self.Loth_i = L[1:, oth]

    def axis(self, Xf):
        for e in (0, 2, 3, 4):
            Xf[e, self.alg] = -self.Ainv @ (self.Loth @ Xf[e, self.oth])
        Xf[1, 0] = Xf[3, 0]
        Xf[1, self.ifc] = -self.Ainv_i @ (self.Loth_i @ Xf[1, self.oth] + self.L_ax * Xf[1, 0])

    def _full(self, xb, Xi, V=False):
        Nn = self.Nx + 1; Xf = np.zeros((5, Nn)); Xf[:, self.inner] = Xi; Xf[:4, -1] = xb; Xf[4, -1] = 0
        self.axis(Xf)
        return Xf

    def brane_values(self, s, Xi, Vi):
        """interior_fw's brane solve and implicit V, with V placed on this mesh's inner nodes"""
        from scipy.optimize import fsolve
        x0 = self.lastbr if self.lastbr is not None else Xi[:4, -1].copy()
        xb = fsolve(lambda q: self._r(s, q, Xi), x0, xtol=1e-13)
        self.lastbr = xb
        h = 1e-7; r0 = self._r(s, xb, Xi)
        Jb = np.array([(self._r(s, xb + h * np.eye(4)[k], Xi) - r0) / h for k in range(4)]).T
        dr_in = (self._r(s, xb, Xi + h * Vi) - r0) / h
        dr_s = (self._r(s + h, xb, Xi) - r0) / h
        try:
            vb = np.linalg.solve(Jb, -(dr_in + dr_s))
        except np.linalg.LinAlgError:
            vb = np.linalg.lstsq(Jb, -(dr_in + dr_s), rcond=None)[0]
        Xf = self._full(xb, Xi)
        Vf = np.zeros_like(Xf); Vf[:, self.inner] = Vi; Vf[:4, -1] = vb; Vf[4, -1] = 0
        self.axis(Vf)
        return Xf, Vf

    def tails(self, Xf):
        """each part's Chebyshev tail: max(|c_n-1|, |c_n|)/max|c| over the five fields"""
        out = []
        for i0, i1, Dl, loc in self.doms:
            t = 2 * (loc - loc[0]) / (loc[-1] - loc[0]) - 1
            for e in range(5):
                c = np.polynomial.chebyshev.chebfit(t, Xf[e, i0:i1 + 1], len(t) - 1)
                big = np.abs(c).max()
                out.append(max(abs(c[-1]), abs(c[-2])) / big if big > 0 else 0.0)
        return max(out)


def trusted():
    I = ID.Damped(28, B, STATIC, KAP, AT); I.lastbr = ID.static_brane(B); m = I.m
    Y0 = I.initial(S0, 2); t0 = time.time()
    sol = solve_ivp(I.rhs, (S0, S1), Y0, method="Radau", rtol=1e-8, atol=1e-10)
    took = time.time() - t0
    # march the brane solve along the steps, as rescaled.py does, to carry its root to s1
    I2 = ID.Damped(28, B, STATIC, KAP, AT); I2.lastbr = ID.static_brane(B)
    for k in range(len(sol.t)):
        Y = sol.y[:, k]; I2.brane_values(sol.t[k], Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    Y = sol.y[:, -1]
    Xf, Vf = I2.brane_values(sol.t[-1], Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    phi = np.nanmax(np.abs(IF.phi_at(I2, sol.t[-1], Y)))
    lapse = lapse_of(I2, sol.t[-1], Xf)
    pickle.dump(dict(s=sol.t[-1], Y=Y, Xf=Xf, Vf=Vf, xn=I2.xn, br=I2.lastbr, phi=phi, lapse=lapse, steps=len(sol.t),
                     took=took, status=sol.status), open(TRUSTED, "wb"))
    print("trusted: status %d, %d steps, %.0f s; s = %.4f; phi_max %.2e; lapse axis %.4f brane %.4f" % (
        sol.status, len(sol.t), took, sol.t[-1], phi, lapse[0], lapse[-1]), flush=True)


class FoldedSAT(ID.Damped):
    """item 394: the axis folded away and the parts joined by the energy-derived coupling (zeno_interface_check.py).
    Part 0 is the symmetric [-1/8, 1/8] with an odd number of Legendre-Gauss-Lobatto intervals, no node on the axis;
    every field is even in x (g_sx ~ x F is odd), so only its x > 0 half is stored and derivatives act on even
    extensions.  Parts [1/8, 1/4], [1/4, 1/2], [1/2, 3/4], [3/4, 7/8], [7/8, 1] halve toward the brane, n intervals
    each; each part keeps its own end nodes.  At each interface, per field, with a = -g_ss/g_xx and b = g_sx/g_xx
    (each field's principal part is g^cd d_c d_d X; the DeTurck form makes it diagonal):
      left copy:  X_ss += [-(a/2) J_x - tau J - (b + gam) J_s]/h_L, and (a/2) J H^-1 D^T e_N over the left part;
      right copy: X_ss += [-(a/2) J_x + tau J - (b - gam) J_s]/h_R, and (a/2) J H^-1 D^T e_0 over the right part;
    J = left - right, tau = 1.2 a (h_L + h_R)/(4 h_L h_R), gam = 0.5 sqrt(a).  The brane keeps the record's rows."""

    def __init__(self, n, b, static, kap, at, edges=(0.125, 0.25, 0.5, 0.75, 0.875, 1.0), n0=None, ns=None):
        import zeno_interface_check as ZC
        n0 = n0 or (n + 1 if n % 2 == 0 else n)
        assert n0 % 2 == 1, "the folded part needs an odd number of intervals (no node on the axis)"
        ns = list(ns or [n] * (len(edges) - 1))
        e1 = edges[0]; z, wz = ZC.lgl(n0); full = -e1 + 2 * e1 * z; wfull = 2 * e1 * wz
        P = np.where(full > 0)[0]; Mi = np.array([int(np.argmin(np.abs(full + full[p]))) for p in P])
        Df = C.bary_D(full); D2f = Df @ Df
        self.fold = (full, P, Mi)
        blk = [(np.arange(len(P)), Df[np.ix_(P, P)] + Df[np.ix_(P, Mi)], D2f[np.ix_(P, P)] + D2f[np.ix_(P, Mi)],
                wfull[P], full[P])]
        xs = list(full[P])
        for (a_, c_), nk in zip(zip(edges[:-1], edges[1:]), ns):
            zz, ww = ZC.lgl(nk); loc = a_ + (c_ - a_) * zz; i0 = len(xs); xs += list(loc)
            Dl = C.bary_D(loc); blk.append((np.arange(i0, i0 + nk + 1), Dl, Dl @ Dl, (c_ - a_) * ww, loc))
        super().__init__(len(xs) - 1, b, static, kap, at)
        self.blk = blk; self.xn = np.array(xs); Nn = len(xs)
        self.D = np.zeros((Nn, Nn)); self.D2 = np.zeros((Nn, Nn))
        for idx, Dl, D2l, w, loc in blk:
            self.D[np.ix_(idx, idx)] = Dl; self.D2[np.ix_(idx, idx)] = D2l
        self.inner = np.arange(0, Nn - 1); self.m = Nn - 1

    def axis(self, Xf):
        return                                                   # no axis node: the axis is folded away

    def _full(self, xb, Xi, V=False):
        Xf = np.zeros((5, self.Nx + 1)); Xf[:, self.inner] = Xi; Xf[:4, -1] = xb; Xf[4, -1] = 0
        return Xf

    brane_values = Halving.brane_values

    def rhs(self, s, Y):
        m = self.m; Xi = Y[:5 * m].reshape(5, m); Vi = Y[5 * m:].reshape(5, m)
        Xf, Vf = self.brane_values(s, Xi, Vi)
        DX = Xf @ self.D.T; DXX = Xf @ self.D2.T; DV = Vf @ self.D.T
        I = self.inner; xs = self.xn[I]; ss = np.full(m, s); a = []
        for e in range(5):
            a += [Xf[e, I], Vf[e, I], DX[e, I], np.zeros(m), DXX[e, I], DV[e, I]]
        bc = lambda L: np.array([np.broadcast_to(np.asarray(r, dtype=float), (m,)) for r in L])
        rest = bc(IF.f_rest(ss, xs, self.b, *a))
        if self.kap:
            with np.errstate(all="ignore"):
                rest = rest + bc(ID.f_damp(ss, xs, self.b, self.kap, self.at, *a))
        co = IF.f_coef(ss, xs, self.b, *a)
        M = np.empty((m, 5, 5))
        for e in range(5):
            for k in range(5):
                M[:, e, k] = np.broadcast_to(np.asarray(co[e][k], dtype=float), (m,))
        Xss = np.zeros_like(Xf)
        Xss[:, I] = np.linalg.solve(M, -rest.T[:, :, None])[:, :, 0].T
        gss, gsx, gxx = C.metric_sx(s, self.xn, self.b, Xf)
        for j in range(len(self.blk) - 1):
            (idL, DL, _, wL, _), (idR, DR, _, wR, _) = self.blk[j], self.blk[j + 1]
            iL, iR = idL[-1], idR[0]; hL, hR = wL[-1], wR[0]
            aa = 0.5 * (-gss[iL] / gxx[iL] - gss[iR] / gxx[iR]); bb = 0.5 * (gsx[iL] / gxx[iL] + gsx[iR] / gxx[iR])
            tau = 1.2 * aa * (hL + hR) / (4 * hL * hR); gam = 0.5 * np.sqrt(aa)
            Ju = Xf[:, iL] - Xf[:, iR]; Jv = Vf[:, iL] - Vf[:, iR]; Jp = DX[:, iL] - DX[:, iR]
            Xss[:, iL] += (-(aa / 2) * Jp - tau * Ju - (bb + gam) * Jv) / hL
            Xss[:, iR] += (-(aa / 2) * Jp + tau * Ju - (bb - gam) * Jv) / hR
            Xss[:, idL] += (aa / 2) * np.outer(Ju, DL[-1] / wL)
            Xss[:, idR] += (aa / 2) * np.outer(Ju, DR[0] / wR)
        return np.concatenate([Y[5 * m:], Xss[:, I].ravel()])

    def tails(self, Xf):
        """each part's Chebyshev tail; part 0 rebuilt on its full symmetric nodes"""
        out = []
        full, P, Mi = self.fold
        for k, (idx, Dl, D2l, w, loc) in enumerate(self.blk):
            if k == 0:
                vals = np.zeros((5, len(full))); vals[:, P] = Xf[:, idx]; vals[:, Mi] = Xf[:, idx]; pts = full
            else:
                vals = Xf[:, idx]; pts = loc
            t = 2 * (pts - pts[0]) / (pts[-1] - pts[0]) - 1
            for e in range(5):
                c = np.polynomial.chebyshev.chebfit(t, vals[e], len(t) - 1); big = np.abs(c).max()
                out.append(max(abs(c[-1]), abs(c[-2])) / big if big > 0 else 0.0)
        return max(out)


def lapse_of(I, s, Xf):
    """the lapse of the s-slices, N = 1/sqrt(-g^ss), from the (s, x) block of the metric"""
    gss, gsx, gxx = C.metric_sx(s, I.xn, I.b, Xf)
    det = gss * gxx - gsx ** 2
    return 1 / np.sqrt(np.abs(-gxx / det))


def half(n=12, mesh="sat"):
    T = pickle.load(open(TRUSTED, "rb"))
    if mesh == "sat":                                          # item 394: more points where the restart tails need them
        I = FoldedSAT(n, B, STATIC, KAP, AT, n0=SAT_N0, ns=SAT_NS)
    else:
        I = Halving(n, B, STATIC, KAP, AT)
    m = I.m
    Xg = np.array([C.bary_interp(T["xn"], T["Xf"][e], I.xn).ravel() for e in range(5)])
    Vg = np.array([C.bary_interp(T["xn"], T["Vf"][e], I.xn).ravel() for e in range(5)])
    I.lastbr = T["br"].copy()
    s1 = T["s"]; lam1 = np.log(1 - s1); lam2 = lam1 + np.log(2.0)
    P = np.repeat(P_EXP, m)
    X0 = Xg[:, I.inner].ravel(); V0 = Vg[:, I.inner].ravel()
    f1 = np.exp(lam1)
    Xt0 = np.exp(P * lam1) * X0                                # Xt = u^-p X = e^(p lambda) X
    Wt0 = np.exp(P * lam1) * (-f1 * V0) + P * Xt0              # Wt = Xt_lambda
    t0 = time.time()
    state = dict(n=0)

    def rhs(lam, Z):
        if time.time() - t0 > WALL:
            raise TimeoutError("20-minute stop")
        state["n"] += 1
        f = np.exp(lam); s = 1.0 - f
        Xt, Wt = Z[:5 * m], Z[5 * m:]
        e = np.exp(-P * lam)
        X = e * Xt; Xl = e * (Wt - P * Xt); Xs = -Xl / f
        d = I.rhs(s, np.concatenate([X, Xs]))
        Xll = f * f * d[5 * m:] + Xl
        return np.concatenate([Wt, np.exp(P * lam) * Xll + 2 * P * Wt - P * P * Xt])

    marks = list(np.linspace(lam1, lam2, 5)[1:])
    log = []
    try:
        sol = solve_ivp(rhs, (lam1, lam2), np.concatenate([Xt0, Wt0]), method="Radau", rtol=1e-8, atol=1e-10,
                        dense_output=True)
        status, msg = sol.status, sol.message
    except TimeoutError as ex:
        sol, status, msg = None, -9, str(ex)
    took = time.time() - t0
    if sol is None:
        print("half: stopped at 20 minutes", flush=True)
        pickle.dump(dict(status=status, msg=msg, took=took), open("zeno_half_%s_%d.pkl" % (mesh, n), "wb"))
        return
    I.lastbr = T["br"].copy()                                  # march the brane root from the restart, in order
    log = assess_steps(I, sol.t, sol.y, [lam1] + marks, P)
    ok = bool(log) and log[-1]["phi"] <= 1e-4 and log[-1]["tail"] <= 1e-6
    print("half: status %d (%s), %d steps, %d evaluations, %.0f s; pass: %s" % (status, msg, len(sol.t), state["n"],
                                                                           took, ok), flush=True)
    pickle.dump(dict(status=status, msg=msg, took=took, log=log, ok=ok, n=n, t=sol.t, y=sol.y, mesh=mesh),
                open("zeno_half_%s_%d.pkl" % (mesh, n), "wb"))


def assess_steps(I, ts, ys, marks, P):
    """the brane root marched along every step in order (warm-starting from a later state finds a spurious root:
    README B5); at each mark (the nearest step at or past it) the DeTurck norm, the tails and the lapse"""
    m = I.m; log = []; todo = list(marks)
    for k in range(len(ts)):
        lam = ts[k]; Z = ys[:, k]; f = np.exp(lam); s = 1 - f; e = np.exp(-P * lam)
        X = e * Z[:5 * m]; Xs = -(e * (Z[5 * m:] - P * Z[:5 * m])) / f
        Xf, Vf = I.brane_values(s, X.reshape(5, m), Xs.reshape(5, m))
        if todo and lam >= todo[0] - 1e-12:
            todo.pop(0)
            Y = np.concatenate([X, Xs])
            phi = np.nanmax(np.abs(IF.phi_at(I, s, Y)))
            tl = I.tails(Xf); lp = lapse_of(I, s, Xf); u = 1 / (1 - s)
            log.append(dict(lam=lam, s=s, u=u, phi=phi, tail=tl, lapse_ax=lp[0], lapse_br=lp[-1], T_ax=Xf[0, 0],
                            T_br=Xf[0, -1], Tu_ax=Xf[0, 0] / u, Su2_br=Xf[1, -1] * u * u))
            print("lam %.4f s %8.4f u %.4f: phi_max %.2e  tail %.2e  lapse ax %.4f br %.4f  T/u ax %.4f  "
                  "S u^2 br %.4f" % (lam, s, u, phi, tl, lp[0], lp[-1], Xf[0, 0] / u, Xf[1, -1] * u * u), flush=True)
    return log


def reassess(n=12):
    """the saved half re-assessed with the brane root marched in order (no rerun)"""
    T = pickle.load(open(TRUSTED, "rb")); R = pickle.load(open("zeno_half_%d.pkl" % n, "rb"))
    I = Halving(n, B, STATIC, KAP, AT); I.lastbr = T["br"].copy()
    P = np.repeat(P_EXP, I.m); ts = R["t"]
    marks = list(np.linspace(ts[0], ts[-1], 5))
    log = assess_steps(I, ts, R["y"], marks, P)
    ok = bool(log) and log[-1]["phi"] <= 1e-4 and log[-1]["tail"] <= 1e-6
    print("re-assessed: %d steps marched; pass: %s" % (len(ts), ok), flush=True)
    R.update(log=log, ok=ok, reassessed=True)
    pickle.dump(R, open("zeno_half_%d.pkl" % n, "wb"))


if __name__ == "__main__":
    if sys.argv[1] == "trusted":
        trusted()
    elif sys.argv[1] == "half":
        half(int(sys.argv[2]) if len(sys.argv) > 2 else 12, sys.argv[3] if len(sys.argv) > 3 else "sat")
    elif sys.argv[1] == "reassess":
        reassess(int(sys.argv[2]) if len(sys.argv) > 2 else 12)
