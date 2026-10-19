"""the global solve across the horizon with a field-valued reference: FW's outside, the previous solution's smooth
extension inside, blended in s"""
import numpy as np, sys, time
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from across import Across, cp2, JETS
from refslab import CR
DT = cp2.DT


class AcrossRef(Across):
    def __init__(self, Ns, Nx, smin, ref):
        Across.__init__(self, Ns, Nx, smin)
        self.c = CR(False)
        self.refjets = [self.D[j] @ ref[m].ravel() for m in range(5) for j in JETS]

    def residual(self, U, p, jac=True):
        n = self.n
        Jv = self.jets(U)
        Rv = np.zeros(6 * n)
        Jm = np.zeros((6 * n, 6 * n)) if jac else None
        for reg, fl in (("inner", self.c["inner"]), ("axis", self.c["axis"]), ("brane", self.c["brane"])):
            idx = np.where(self.mask[reg])[0]
            a = ([self.sg[idx], self.xg[idx], p["bt"], p["mu"], p["lam"]] + [jv[idx] for jv in Jv]
                 + [rj[idx] for rj in self.refjets] + [0.0])
            for k, fk in enumerate(fl):
                Rv[k * n + idx] = np.real(np.broadcast_to(fk(*a), idx.shape))
                if not jac:
                    continue
                for jj in range(36):
                    ac = list(a)
                    ac[5 + jj] = a[5 + jj] + 1e-30j
                    cf = np.broadcast_to(np.imag(fk(*ac)) / 1e-30, idx.shape)
                    if np.any(cf):
                        m, j = divmod(jj, 6)
                        Jm[k * n + idx, m * n:(m + 1) * n] += cf[:, None] * self.D[JETS[j]][idx]
        idx = np.where(self.mask["dir"])[0]
        for k, v in enumerate([1.0, 1.0, 1.0, 0.0, 1.0, p["mu"]]):
            Rv[k * n + idx] = U[k * n + idx] - v
            if jac:
                Jm[k * n + idx, :] = 0.0
                Jm[k * n + idx, k * n + idx] = 1.0
        it = self.top
        Rv[5 * n + it] = self.I0 @ U[5 * n:6 * n]
        if jac:
            Jm[5 * n + it, :] = 0.0
            Jm[5 * n + it, 5 * n:6 * n] = self.I0
        return Rv, Jm

    def xi2(self, U, p):
        a = [self.sg, self.xg, p["bt"], p["mu"], p["lam"]] + self.jets(U) + self.refjets + [0.0]
        return np.abs(self.c["xi2"](*a)).reshape(self.Ns + 1, self.Nx + 1)


def chi(s, s0=-0.15, s1=-0.30):
    """0 for s >= s0, 1 for s <= s1, smooth (C-infinity) between"""
    t = np.clip((s0 - s) / (s0 - s1), 0, 1)
    f = lambda z: np.where(z > 0, np.exp(-1 / np.maximum(z, 1e-300)), 0.0)
    return f(t) / (f(t) + f(1 - t))


def extend(A, U, s_new, s_edge):
    """the solution A, U on s_new: spectral inside [s_edge, 1], quadratic Taylor from s_edge below it"""
    t, Dt = cp2.cheb01(A.Ns); Ds = -Dt / (1 - A.smin)
    out = []
    inside = s_new >= s_edge
    M = DT.interp_matrix(A.s, s_new[inside]); Me = DT.interp_matrix(A.s, np.array([s_edge]))
    for m in range(6):
        Fm = A.field(U, m); G = np.zeros((len(s_new), A.Nx + 1))
        G[inside] = M @ Fm
        f0, f1, f2 = (Me @ Fm)[0], (Me @ (Ds @ Fm))[0], (Me @ (Ds @ Ds @ Fm))[0]
        d = (s_new[~inside] - s_edge)[:, None]
        G[~inside] = f0 + f1 * d + 0.5 * f2 * d**2
        out.append(G)
    return np.stack(out)
