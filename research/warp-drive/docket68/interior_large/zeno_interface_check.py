"""zeno_interface_check.py -- item 394: the joining of mesh parts checked on a known solution before the second attempt
at the first Zeno half.  A wave equation with the interior's principal structure,
    u_ss = a(x) u_xx + 2 b(x) u_sx + F(s, x),   a = 1 + x^2,  b = 0.3 x  (b = 0 on the axis, as g^sx is),
with u_x = 0 on the axis x = 0 and u given at x = 1, and F made so that
    u = cos(2.3 s) cos(pi x/2) + 0.3 sin(1.7 s) cos(3 pi x/2)
is exact (a manufactured solution).  Characteristic speeds lambda+- = b +- sqrt(b^2 + a); w+ = v - lambda- u_x moves
with lambda+ > 0, w- = v - lambda+ u_x with lambda- < 0.
Three ways of joining the parts of the halving mesh [0, 1/8, 1/4, 1/2, 3/4, 7/8, 1] (Zeno toward both ends):
  patch   -- shared interface nodes fixed by derivative continuity (item 393's joining);
  penalty -- each part keeps its own end nodes, evolved by the equation, with penalties on the characteristic entering
             it and on the jump: u_ss[iR] -= (tau/w) |lambda-| (w-_R - w-_L) + sigma lambda+ |lambda-| (u_R - u_L)/w^2,
             and the mirror at iL with lambda+ and w+; w the Lobatto end weight h/(n (n + 1)).  (d_s - lambda d_x) w = 0
             carries w at velocity -lambda, so w- = v - lambda+ u_x enters the right part and w+ the left;
  sat     -- Legendre-Gauss-Lobatto parts (a summation-by-parts pair, Q + Q^T = B) with the coupling derived from the
             discrete energy E = v^T H v/2 + a (Du)^T H (Du)/2: at the left copy
             u_ss += [-(a/2) J_phi - tau J_u - (b + gam) J_v]/h_L + (a/2) J_u H^-1 D^T e_N, at the right copy
             u_ss += [-(a/2) J_phi + tau J_u - (b - gam) J_v]/h_R + (a/2) J_u H^-1 D^T e_0, J = left - right;
             then d/ds [E - a m_phi J_u + tau J_u^2/2] = -gam J_v^2 exactly (frozen a, b), a norm when
             tau >= a (h_L + h_R)/(4 h_L h_R);
  single  -- one Lobatto grid with the same number of intervals.
Run to s = 40 (about 50 crossings); the measure is the largest error over the run.
python3 zeno_interface_check.py
"""
import numpy as np
from scipy.integrate import solve_ivp

EDGES = [0.0, 0.125, 0.25, 0.5, 0.75, 0.875, 1.0]
K1, K2 = np.pi / 2, 3 * np.pi / 2


def lob(N):
    return np.sort((1 - np.cos(np.pi * np.arange(N + 1) / N)) / 2)


def lgl(N):
    """Legendre-Gauss-Lobatto nodes and weights on [0, 1] (a diagonal-norm summation-by-parts pair)"""
    from numpy.polynomial import legendre as Lg
    inner = np.sort(Lg.legroots(Lg.legder([0] * N + [1])))
    x = np.concatenate([[-1.0], inner, [1.0]])
    w = 2 / (N * (N + 1) * Lg.legval(x, [0] * N + [1]) ** 2)
    return (x + 1) / 2, w / 2


def bD(x):
    n = len(x); w = np.array([1 / np.prod([x[j] - x[k] for k in range(n) if k != j]) for j in range(n)])
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                D[i, j] = (w[j] / w[i]) / (x[i] - x[j])
        D[i, i] = -D[i].sum()
    return D


def exact(s, x):
    u = np.cos(2.3 * s) * np.cos(K1 * x) + 0.3 * np.sin(1.7 * s) * np.cos(K2 * x)
    v = -2.3 * np.sin(2.3 * s) * np.cos(K1 * x) + 0.3 * 1.7 * np.cos(1.7 * s) * np.cos(K2 * x)
    uss = -2.3 ** 2 * np.cos(2.3 * s) * np.cos(K1 * x) - 0.3 * 1.7 ** 2 * np.sin(1.7 * s) * np.cos(K2 * x)
    uxx = -K1 ** 2 * np.cos(2.3 * s) * np.cos(K1 * x) - 0.3 * K2 ** 2 * np.sin(1.7 * s) * np.cos(K2 * x)
    usx = 2.3 * K1 * np.sin(2.3 * s) * np.sin(K1 * x) - 0.3 * 1.7 * K2 * np.cos(1.7 * s) * np.sin(K2 * x)
    return u, v, uss, uxx, usx


A = lambda x: 1 + x ** 2
Bc = lambda x: 0.3 * x


def forcing(s, x):
    u, v, uss, uxx, usx = exact(s, x)
    return uss - A(x) * uxx - 2 * Bc(x) * usx


class Mesh:
    def __init__(self, mode, n, edges=EDGES, tau=1.0, sigma=1.0, weak_axis=False):
        self.mode, self.tau, self.sigma, self.weak = mode, tau, sigma, weak_axis
        if mode == "single":
            edges = [0.0, 1.0]; n = n * (len(EDGES) - 1)
        parts = list(zip(edges[:-1], edges[1:]))
        xs, blocks, self.ifc = [], [], []
        self.wts = []
        for k, (a, c) in enumerate(parts):
            if mode == "sat":
                z, wz = lgl(n); loc = a + (c - a) * z; self.wts.append((c - a) * wz)
            else:
                loc = a + (c - a) * lob(n)
            full = loc.copy()
            if mode == "patch" and k > 0:
                loc = loc[1:]                                    # shared node with the part before
            i0 = len(xs); xs += list(loc); blocks.append((i0, full, c - a))
        self.x = np.array(xs); N = len(xs)
        D = np.zeros((N, N)); D2 = np.zeros((N, N))
        if mode == "patch":
            starts = []
            for k, (i0, loc, h) in enumerate(blocks):
                g0 = i0 if k == 0 else i0 - 1                    # global index of the part's first node
                idx = np.arange(g0, g0 + n + 1); Dl = bD(loc); starts.append((idx, Dl))
                for r in range(0 if k == 0 else 1, n + 1):
                    D[idx[r], idx] = Dl[r]; D2[idx[r], idx] = (Dl @ Dl)[r]
            self.alg = [0] + [st[0][-1] for st in starts[:-1]]
            L = np.zeros((len(self.alg), N)); L[0, starts[0][0]] = starts[0][1][0]
            for j in range(len(starts) - 1):
                (il, Dl), (ir, Dr) = starts[j], starts[j + 1]
                L[j + 1, il] += Dl[-1]; L[j + 1, ir] -= Dr[0]
            oth = [i for i in range(N) if i not in self.alg]
            self.oth, self.Ainv, self.Loth = oth, np.linalg.inv(L[:, self.alg]), L[:, oth]
        else:
            self.blk = []
            for k, (i0, loc, h) in enumerate(blocks):
                idx = np.arange(i0, i0 + n + 1); Dl = bD(loc)
                D[np.ix_(idx, idx)] = Dl; D2[np.ix_(idx, idx)] = Dl @ Dl
                self.blk.append((idx, Dl, self.wts[k] if self.wts else None))
                if k < len(blocks) - 1:
                    self.ifc.append((i0 + n, i0 + n + 1, h / (n * (n + 1)), blocks[k + 1][2] / (n * (n + 1))))
            self.alg = [0]
            self.oth = list(range(1, N))
        self.D, self.D2 = D, D2
        if self.weak:
            self.alg = [i for i in self.alg if i != 0]
            self.h0 = self.wts[0][0] if self.wts else (edges[1] - edges[0]) / (n * (n + 1))
        self.ev = np.array([i for i in range(0 if self.weak else 1, N - 1) if i not in self.alg])   # evolved nodes

    def fill(self, s, ue, ve):
        """the full u and v from the evolved nodes: the brane (x = 1) given, the algebraic nodes solved"""
        N = len(self.x); u = np.zeros(N); v = np.zeros(N)
        u[self.ev], v[self.ev] = ue, ve
        u[-1], v[-1] = exact(s, 1.0)[:2]
        for f in (u, v):
            if self.weak:
                break
            if self.mode == "patch":
                f[self.alg] = -self.Ainv @ (self.Loth @ f[self.oth])
            else:
                f[0] = -(self.D[0, 1:] @ f[1:]) / self.D[0, 0]
        return u, v

    def rhs(self, s, y):
        m = len(self.ev); u, v = self.fill(s, y[:m], y[m:])
        x = self.x; ux = self.D @ u; uxx = self.D2 @ u; vx = self.D @ v
        uss = A(x) * uxx + 2 * Bc(x) * vx + forcing(s, x)
        if self.weak:
            uss[0] += A(x[0]) * ux[0] / self.h0                     # weak u_x = 0 on the axis
        if self.mode == "penalty":
            for iL, iR, wL, wR in self.ifc:
                xi = x[iL]; b, a = Bc(xi), A(xi); lp, lm = b + np.sqrt(b * b + a), b - np.sqrt(b * b + a)
                wpL, wpR = v[iL] - lm * ux[iL], v[iR] - lm * ux[iR]
                wmL, wmR = v[iL] - lp * ux[iL], v[iR] - lp * ux[iR]
                # (d_s - lambda d_x) w = 0 carries w at velocity -lambda: w+ (built with lambda-) moves left at -lambda+,
                # w- moves right at -lambda- = |lambda-|.  Entering the right part at iR: w-; entering the left at iL: w+
                uss[iR] -= self.tau / wR * abs(lm) * (wmR - wmL) + self.sigma * lp * abs(lm) * (u[iR] - u[iL]) / wR ** 2
                uss[iL] -= self.tau / wL * lp * (wpL - wpR) + self.sigma * lp * abs(lm) * (u[iL] - u[iR]) / wL ** 2
        if self.mode == "sat":
            for j, (iL, iR, _, _) in enumerate(self.ifc):
                (idL, DL, wL), (idR, DR, wR) = self.blk[j], self.blk[j + 1]
                a, b = A(x[iL]), Bc(x[iL]); hL, hR = wL[-1], wR[0]
                tau = 1.2 * a * (hL + hR) / (4 * hL * hR); gam = self.tau
                Ju, Jv, Jp = u[iL] - u[iR], v[iL] - v[iR], ux[iL] - ux[iR]
                uss[iL] += (-(a / 2) * Jp - tau * Ju - (b + gam) * Jv) / hL
                uss[iR] += (-(a / 2) * Jp + tau * Ju - (b - gam) * Jv) / hR    # -(a/2) J_phi at both copies
                uss[idL] += (a / 2) * Ju * DL[-1] / wL               # H^-1 D^T e_N (a/2) J_u over the left part
                uss[idR] += (a / 2) * Ju * DR[0] / wR                # H^-1 D^T e_0 (a/2) J_u over the right part
        return np.concatenate([v[self.ev], uss[self.ev]])

    def run(self, s_end=40.0):
        u0, v0 = exact(0.0, self.x)[:2]
        sol = solve_ivp(self.rhs, (0, s_end), np.concatenate([u0[self.ev], v0[self.ev]]), method="DOP853",
                        rtol=1e-10, atol=1e-12, dense_output=True)
        m = len(self.ev); errs = []
        for s in np.linspace(0, sol.t[-1], 401):
            u, _ = self.fill(s, sol.sol(s)[:m], sol.sol(s)[m:])
            errs.append(np.abs(u - exact(s, self.x)[0]).max())
        e2 = errs[int(round(2.0 / s_end * 400))] if sol.t[-1] >= 2.0 else float("nan")
        return sol.status, sol.t[-1], max(errs), errs[len(errs) // 2], errs[-1], len(sol.t), e2


if __name__ == "__main__":
    import sys
    runs = (("sat", 0.0, 0), ("sat", 0.5, 0))
    if "--all" in sys.argv:
        runs = (("single", 0, 0), ("patch", 0, 0), ("penalty", 1.0, 1.0)) + runs
    for n in (8, 12):
        for mode, tau, sig in runs:
            st, t, emax, emid, eend, steps, e2 = Mesh(mode, n, tau=tau, sigma=sig).run()
            print("n=%2d %-8s tau=%.2f sigma=%.2f: status %d to s=%.1f, %6d steps; error at s=2 %.2e, s=20 %.2e, "
                  "s=40 %.2e; max %.2e" % (n, mode, tau, sig, st, t, steps, e2, emid, eend, emax), flush=True)


class Folded:
    """the axis folded away: part 0 is the symmetric [-e1, e1] with an odd number of LGL intervals (no node at x = 0),
    only its x > 0 half stored, derivatives taken on even extensions; parts 1.. as in sat; u given at x = 1"""
    def __init__(self, n, edges=EDGES, gam=0.5, n0=None):
        n0 = n0 or (n + 1 if n % 2 == 0 else n)                  # odd
        e1 = edges[1]; z, wz = lgl(n0); full = -e1 + 2 * e1 * z; wfull = 2 * e1 * wz
        P = np.where(full > 0)[0]; Mi = np.array([np.argmin(np.abs(full + full[p])) for p in P])
        Df = bD(full); D2f = Df @ Df
        D0 = Df[np.ix_(P, P)] + Df[np.ix_(P, Mi)]; D20 = D2f[np.ix_(P, P)] + D2f[np.ix_(P, Mi)]
        self.blk = [(np.arange(len(P)), D0, D20, wfull[P])]
        xs = list(full[P])
        for a, c in zip(edges[1:-1], edges[2:]):
            zz, ww = lgl(n); loc = a + (c - a) * zz; i0 = len(xs); xs += list(loc)
            Dl = bD(loc); self.blk.append((np.arange(i0, i0 + n + 1), Dl, Dl @ Dl, (c - a) * ww))
        self.x = np.array(xs); N = len(xs); self.gam = gam
        self.D = np.zeros((N, N)); self.D2 = np.zeros((N, N))
        for idx, Dl, D2l, w in self.blk:
            self.D[np.ix_(idx, idx)] = Dl; self.D2[np.ix_(idx, idx)] = D2l
        self.ev = np.arange(0, N - 1)

    def fill(self, s, ue, ve):
        N = len(self.x); u = np.zeros(N); v = np.zeros(N); u[self.ev], v[self.ev] = ue, ve
        u[-1], v[-1] = exact(s, 1.0)[:2]
        return u, v

    def rhs(self, s, y):
        m = len(self.ev); u, v = self.fill(s, y[:m], y[m:]); x = self.x
        ux = self.D @ u; uss = A(x) * (self.D2 @ u) + 2 * Bc(x) * (self.D @ v) + forcing(s, x)
        for j in range(len(self.blk) - 1):
            (idL, DL, _, wL), (idR, DR, _, wR) = self.blk[j], self.blk[j + 1]
            iL, iR = idL[-1], idR[0]; a, b = A(x[iL]), Bc(x[iL]); hL, hR = wL[-1], wR[0]
            tau = 1.2 * a * (hL + hR) / (4 * hL * hR)
            Ju, Jv, Jp = u[iL] - u[iR], v[iL] - v[iR], ux[iL] - ux[iR]
            uss[iL] += (-(a / 2) * Jp - tau * Ju - (b + self.gam) * Jv) / hL
            uss[iR] += (-(a / 2) * Jp + tau * Ju - (b - self.gam) * Jv) / hR
            uss[idL] += (a / 2) * Ju * DL[-1] / wL
            uss[idR] += (a / 2) * Ju * DR[0] / wR
        return np.concatenate([v[self.ev], uss[self.ev]])

    run = Mesh.run


def exact_ux(s, x):
    return -K1 * np.cos(2.3 * s) * np.sin(K1 * x) - 0.3 * K2 * np.sin(1.7 * s) * np.sin(K2 * x)


class FoldedWeak(Folded):
    """item 395: the far end (x = 1, the brane's place) imposed weakly as well -- its node evolved, its slope pulled to
    the prescribed value g by u_ss[N] += -(a/h_N)(u_x[N] - g), which replaces the boundary's energy term a v_N u_x[N]
    by a v_N g (data); with kappa != 0 the slope is a Robin condition u_x = kappa u + g, as the Israel rows are"""
    def __init__(self, n, kappa=0.0, **kw):
        super().__init__(n, **kw); self.kappa = kappa; self.ev = np.arange(0, len(self.x))
        self.hN = self.blk[-1][3][-1]

    def fill(self, s, ue, ve):
        return ue.copy(), ve.copy()

    def rhs(self, s, y):
        d = super().rhs(s, y); m = len(self.ev); u = y[:m]; x = self.x
        ux = self.D @ u
        g = exact_ux(s, 1.0) - self.kappa * exact(s, 1.0)[0] + self.kappa * u[-1]
        d[m + m - 1] += -(A(x[-1]) / self.hN) * (ux[-1] - g)
        return d
