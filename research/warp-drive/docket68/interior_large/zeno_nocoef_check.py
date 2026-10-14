"""zeno_nocoef_check.py -- item 405: a joining with no coefficient, checked on the model before any half.

M, 405: "We cannot have any coefficients in the warp theorem chain, and no penalty coefficient."  The fourth and fifth
attempts' joining (zeno_char_check.DSEM) carries three: the penalised derivative's 1/(2H), the jump damping gk = 1/2,
and the far end's c^2/H.  Item 404 found the only growth at a joining's two endpoints, where those act.  Two
constructions with none, each exact where the other one approximates:

Patched -- the parts share each joining node, so they agree there exactly, and in place of the equation at the shared
  node the two parts' slopes are set equal: D_L u = D_R u, C^1 continuity, exact and parameter-free.  The far end
  takes its slope exactly, D u = g.  These rows are linear in the nodal values, so at every evaluation the joining and
  far-end values follow from the free ones by one linear solve (as the brane rows do in the record's own scheme), and
  their s-derivatives from the same rows differentiated.  Every free node carries the equation with its own part's
  derivative; no penalty, no damping, no average.

OneDomain -- no joining at all: one folded symmetric polynomial on [-1, 1] (even, so no axis node and no axis row),
  the far end's slope exact as above.

The model is zeno_char_check's: u_ss = a u_xx + 2 b u_sx + F, b = 2 x (1 - x^2)^2, with wave2 (a = 1 + x^2), cross2 (a
band of a < 0 opening and closing over the joining at x = 1/4 every 10 in s, both speeds then pointing the same way
across it) and pos2 (the same band kept positive); F makes zeno_interface_check's u exact.  Both directions of
evolution are checked (eps = +1, -1; the interior runs toward decreasing s).

python3 zeno_nocoef_check.py               -- spectra and runs (about 10 minutes)
python3 zeno_nocoef_check.py --selftest | --mutants
"""
import sys
import numpy as np
from scipy.integrate import solve_ivp
import zeno_interface_check as ZC
import zeno_char_check as K

EDGES = K.EDGES
MUT = set()


def exact_uxs(s, x):
    return 2.3 * ZC.K1 * np.sin(2.3 * s) * np.sin(ZC.K1 * x) - 0.3 * 1.7 * ZC.K2 * np.cos(1.7 * s) * np.sin(ZC.K2 * x)


class Constrained:
    """common machinery: nodes x, free indices F and constrained indices C (rows Cm u = g), per-node operators
    Drow, D2row (each free node's own part), the model's coefficients"""

    def setup(self, kind, eps):
        N = len(self.x); self.N = N; self.cf = K.coef(kind); self.eps = eps
        self.C = np.array(sorted(self.crow)); self.F = np.array([i for i in range(N) if i not in self.crow])
        Cm = np.array([self.crow[i] for i in self.C]); self.Cm = Cm
        self.CC = Cm[:, self.C]; self.CF = Cm[:, self.F]
        self.CCi = np.linalg.inv(self.CC)

    def fill(self, uF, gvec):
        u = np.zeros(self.N); u[self.F] = uF
        u[self.C] = self.CCi @ (gvec - self.CF @ uF)
        return u

    def gvec(self, s, deriv=False, forced=True):
        g = np.zeros(len(self.C))
        if forced:
            g[list(self.C).index(self.N - 1)] = (exact_uxs if deriv else ZC.exact_ux)(s, 1.0)
        return g

    def rhs(self, s, y, forced=True):
        nF = len(self.F); uF, vF = y[:nF], y[nF:]
        u = self.fill(uF, self.gvec(s, False, forced)); v = self.fill(vF, self.gvec(s, True, forced))
        a, b = self.cf(s, self.x)
        uss = a * (self.D2 @ u) + 2 * b * (self.D @ v)
        if forced:
            uss = uss + K.forcing(self.cf, s, self.x)
        return np.concatenate([vF, uss[self.F]])

    def run(self, s_end=40.0):
        s_end = self.eps * abs(s_end); u0, v0 = ZC.exact(0.0, self.x)[:2]
        with np.errstate(all="ignore"):
            sol = solve_ivp(self.rhs, (0, s_end), np.concatenate([u0[self.F], v0[self.F]]), method="DOP853",
                            rtol=1e-10, atol=1e-12, dense_output=True)
        nF = len(self.F); errs = []
        for s in np.linspace(0, sol.t[-1], 201):
            u = self.fill(sol.sol(s)[:nF], self.gvec(s))
            errs.append(np.abs(u - ZC.exact(s, self.x)[0]).max())
        return sol.status, sol.t[-1], errs[100], errs[-1], max(errs)

    def spectrum(self, s):
        nF = len(self.F); M = np.zeros((2 * nF, 2 * nF))
        for k in range(2 * nF):
            e = np.zeros(2 * nF); e[k] = 1.0; M[:, k] = self.rhs(s, e, forced=False)
        return float(np.max(np.real(self.eps * np.linalg.eigvals(M))))


class Patched(Constrained):
    def __init__(self, n, kind="cross2", eps=1.0, edges=EDGES, n0=None):
        n0 = n0 or (n + 1 if n % 2 == 0 else n); e1 = edges[1]
        z, wz = ZC.lgl(n0); full = -e1 + 2 * e1 * z
        P = np.where(full > 0)[0]; Mi = np.array([int(np.argmin(np.abs(full + full[p]))) for p in P])
        Df = ZC.bD(full); D2f = Df @ Df
        parts = [(list(range(len(P))), Df[np.ix_(P, P)] + Df[np.ix_(P, Mi)], D2f[np.ix_(P, P)] + D2f[np.ix_(P, Mi)])]
        xs = list(full[P])
        for a_, c_ in zip(edges[1:-1], edges[2:]):
            zz, _ = ZC.lgl(n); loc = a_ + (c_ - a_) * zz; i0 = len(xs) - 1          # the first node is shared
            xs += list(loc[1:]); Dl = ZC.bD(loc)
            parts.append((list(range(i0, i0 + n + 1)), Dl, Dl @ Dl))
        self.x = np.array(xs); N = len(xs); self.parts = parts
        self.D = np.zeros((N, N)); self.D2 = np.zeros((N, N)); self.crow = {}
        for k, (idx, Dl, D2l) in enumerate(parts):
            own = idx if k == 0 else idx[1:]                     # each node's own part: the shared one goes left
            for j, i in enumerate(idx):
                if i in own:
                    self.D[i, idx] = Dl[j]; self.D2[i, idx] = D2l[j]
        for k in range(len(parts) - 1):                          # C^1 at each shared node: D_L u - D_R u = 0
            (iL, DL, _), (iR, DR, _) = parts[k], parts[k + 1]
            r = np.zeros(N); r[iL] += DL[-1]
            if "c0only" not in MUT:
                r[iR] -= DR[0]
            else:
                r = np.zeros(N); r[iL[-1]] = 1.0; r[iL[-2]] = -1.0       # mutant: the slope condition dropped
            self.crow[iL[-1]] = r
        r = np.zeros(N); idx, Dl, _ = parts[-1]; r[idx] = Dl[-1]; self.crow[N - 1] = r       # far end: D u = g
        if "nofar" in MUT:
            self.crow[N - 1] = np.eye(N)[N - 1]
        self.setup(kind, eps)


class OneDomain(Constrained):
    def __init__(self, n0, kind="cross2", eps=1.0):
        n0 = n0 if n0 % 2 == 1 else n0 + 1
        z, _ = ZC.lgl(n0); full = -1 + 2 * z
        P = np.where(full > 0)[0]; Mi = np.array([int(np.argmin(np.abs(full + full[p]))) for p in P])
        Df = ZC.bD(full); D2f = Df @ Df
        self.x = full[P]; N = len(P)
        self.D = Df[np.ix_(P, P)] + Df[np.ix_(P, Mi)]; self.D2 = D2f[np.ix_(P, P)] + D2f[np.ix_(P, Mi)]
        self.crow = {N - 1: self.D[N - 1].copy()}
        self.setup(kind, eps)


# ------------------------------------------------------------------------------------------------- checks
def consistency(cls, n):
    """the exact solution's own values in the rows and the free nodes' equation: what is left is truncation"""
    I = cls(n, kind="cross2"); s = 3.7
    u, v, uss = ZC.exact(s, I.x)[:3]
    rows = np.abs(I.Cm @ u - I.gvec(s)).max()
    r = I.rhs(s, np.concatenate([u[I.F], v[I.F]]))[len(I.F):] - uss[I.F]
    return rows, np.abs(r).max()


def shared_exact():
    """Patched: the joining values the rows give satisfy the rows to round-off, and the shared node is one value"""
    I = Patched(10); rng = np.random.default_rng(1); uF = rng.standard_normal(len(I.F))
    u = I.fill(uF, I.gvec(1.3)); return np.abs(I.Cm @ u - I.gvec(1.3)).max()


def main():
    print("consistency (rows on the exact solution | free-node equation's truncation):")
    for cls, ns in ((Patched, (8, 12, 16)), (OneDomain, (21, 31, 41))):
        for n in ns:
            print("  %-9s n %2d: %.1e | %.1e" % (cls.__name__, n, *consistency(cls, n)))
    print("spectra, max Re(eps lambda) over s in {0, 2.5, 5, 7.5} (the band open at 5; <= 0 holds):")
    for cls, ns in ((Patched, (8, 12, 16)), (OneDomain, (21, 31, 41))):
        for kind in ("wave2", "cross2", "pos2"):
            for eps in (1.0, -1.0):
                row = [max(cls(n, kind=kind, eps=eps).spectrum(s) for s in (0.0, 2.5, 5.0, 7.5)) for n in ns]
                print("  %-9s %-6s eps %+d: %s" % (cls.__name__, kind, eps, "  ".join("n %2d %+.2e" % (n, r)
                                                                                   for n, r in zip(ns, row))))
    print("runs to |s| = 40 (status, error at |s| = 20, at the end, max):")
    for cls, ns in ((Patched, (8, 12, 16)), (OneDomain, (21, 31, 41))):
        for kind in ("wave2", "cross2"):
            for eps in (1.0, -1.0):
                for n in ns:
                    st, se, e20, ee, em = cls(n, kind=kind, eps=eps).run()
                    print("  %-9s %-6s eps %+d n %2d: status %d s %+.1f  %.1e %.1e %.1e" % (
                        cls.__name__, kind, eps, n, st, se, e20, ee, em), flush=True)


def selftest(quiet=False):
    ok = []
    e = shared_exact(); ok.append(("N1 the joining and far-end rows hold to round-off (%.1e)" % e, e < 1e-11))
    r4, t4 = consistency(Patched, 4); r8, t8 = consistency(Patched, 8)
    ok.append(("N2 Patched: rows exact on the exact solution apart from truncation, falling with n (%.1e -> %.1e)"
               % (max(r4, t4), max(r8, t8)), max(r8, t8) < 1e-3 * max(r4, t4)))
    o9 = max(consistency(OneDomain, 9)); o17 = max(consistency(OneDomain, 17))
    ok.append(("N3 OneDomain: the same (%.1e -> %.1e)" % (o9, o17), o17 < 1e-3 * o9))
    I = Patched(10); sh = [k for k in range(len(I.parts) - 1)]
    one = all(I.parts[k][0][-1] == I.parts[k + 1][0][0] for k in sh)
    ok.append(("N4 Patched: each joining is one shared node (no copies, no jump)", one))
    s4 = Patched(4, kind="wave2").spectrum(0.0); s12 = Patched(12, kind="wave2").spectrum(0.0)
    ok.append(("N5 finding pinned: Patched's growing mode on wave2 rises with n (max Re %.2f at n = 4, %.1f at n = 12)"
               % (s4, s12), s12 > 4 * s4 > 4.0))
    if not quiet:
        for name, good in ok:
            print("%s  %s" % ("PASS" if good else "FAIL", name))
    return all(g for _, g in ok), ok


def mutants():
    caught = []
    for mname, what in (("c0only", "the slope condition at the joining dropped"), ("nofar", "the far end's slope "
                                                                                          "replaced by u = 0")):
        MUT.clear(); MUT.add(mname)
        good, ok = selftest(quiet=True)
        caught.append((what, not good, [n.split()[0] for n, g in ok if not g]))
    MUT.clear()
    for what, c, fails in caught:
        print("%s  %-45s failed: %s" % ("caught" if c else "MISSED", what, ", ".join(fails) or "none"))
    return all(c for _, c, _ in caught)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        good, _ = selftest(); print("selftest: %s" % ("PASS" if good else "FAIL")); sys.exit(0 if good else 1)
    elif "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    else:
        main()
