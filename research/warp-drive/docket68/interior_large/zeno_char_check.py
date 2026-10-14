"""zeno_char_check.py -- item 397: a joining that holds where a = -g_ss/g_xx < 0, checked on the model first.

Item 396 found a passing through zero in the interior.  There d_s tips outside the light cone while the slices stay
spacelike and the system hyperbolic: c^2 = b^2 + a > 0, so the speeds lambda+- = b +- c stay real, and once a < 0 both
have the sign of b.  The joining of items 394-395 takes sqrt(a), and its energy v^T H v/2 + a (Du)^T H (Du)/2 is no
norm once a < 0.  Both constructions here are built on p = v - b u_x, the derivative along the slices' normal, for
which the same equation reads u_s = p + b u_x, p_s = c^2 u_xx + b p_x, and the energy |p|^2 + c^2 |u_x|^2 is a norm
wherever c^2 > 0, whatever the sign of a.

First construction, the board's (class SAT; kept as written, and it fails).  Point and D^T e liftings on p_s, a point
lifting on u_s, the energy corrected by J_u times the end slopes and by J_u^2; solved for symbolically, the member
whose energy is exactly conserved apart from -gam J_p^2 is unique:
  left copy:   p_s += [-(c^2/2) J_x - tau J_u - (b/2 + gam) J_p]/h_L,  (c^2/2) J_u H^-1 D^T e_N;  u_s += -(b/2) J_u/h_L;
  right copy:  p_s += [-(c^2/2) J_x + tau J_u - (b/2 - gam) J_p]/h_R,  (c^2/2) J_u H^-1 D^T e_0;  u_s += -(b/2) J_u/h_R;
  tau = c^2 (h_L + h_R)/(4 h_L h_R), and d/ds [E - c^2 m_x J_u + tau J_u^2/2] = -gam J_p^2 exactly (frozen a, b).
It forces tau onto the norm's threshold, so the corrected energy is only semi-definite.  With varying coefficients that
gives modes growing like 1/h: even with b = 0 (where it is item 394's coupling at tau* instead of 1.2 tau*) the growth
rate on a bump of a is 1.3, 2.5, 4.8 at n = 8, 16, 32, against 0.00-0.06 at 1.2 tau*; and at 1.2 tau* exactness is lost
once b != 0 (5.5 at n = 32).  Not used.

Second construction (class DSEM), from Duru, Wang & Wiratama, "A conservative and energy stable discontinuous spectral
element method for the shifted wave equation in second order form" (arXiv:2107.05770, SIAM J. Numer. Anal. 2022; their
shift a and coefficient b are our b and c^2, their c = b - a^2 is our a).  The penalised derivative
    Dt = D - (1/2) H^-1 B^,    (B^ u) = u_L - u_R at both copies of each joining,
is skew in H apart from the outer ends, and with W = v - b Dt u the principal part is put in their form
    v_s = b Dt v + Dt(b W) + Dt(c^2 Dt u)  [- b_x v - a_x Dt u, returning it to a u_xx + 2 b u_sx].
Its energy |W|^2_H + |Dt u|^2_(c^2 H) is a strict norm wherever c^2 > 0 (the jump in u sits inside Dt u at the joining
nodes) and is exactly conserved for constant coefficients, either sign of a.  Added here: the jump in W is damped along
the evolution, v_s -= gam J_W/h_L at the left copy and += gam J_W/h_R at the right, gam = eps gk c (gk = 1/2), which
takes -2 gam sum J_W^2 off the energy rate.  Without it a central-flux mode grows at 1.24-1.27 on wave2 at every n.

The model: u_ss = a u_xx + 2 b u_sx + F, the axis folded away, the far end x = 1 weak, as in the interior (item 395);
F makes zeno_interface_check's u exact.  b = beta x (1 - x^2)^2 (beta = 2): odd, zero with zero slope at x = 1, as the
interior's g_sx ~ x F is (an earlier b = sin(pi x), slope -pi at x = 1, put a +-pi/2 mode there in every scheme, which
says nothing about the joining).  Three coefficient sets:
  wave2  -- a = 1 + x^2;
  cross2 -- a = 1 + x^2 - 1.2 sin^2(pi s/10) [g(x - 1/4) + g(x + 1/4)], g(y) = exp(-(y/0.15)^2), even as the
            interior's a is: a band of a < 0 (down to -0.139, over [0.193, 0.297] at its widest, c^2 >= 0.043)
            opens and closes over the joining at x = 1/4 every 10 in s, as the interior's zero did at x = 0.23;
            both speeds then point the same way across that joining (a first, asymmetric bump at x = 1/4 alone
            was not even about the axis, and the folded part's derivative of a was wrong by 0.43 at every n);
  pos2   -- the same band with 0.9 for 1.2, so a stays positive and item 394's coupling can be set beside it.
python3 zeno_char_check.py               -- identities, spectra and the runs (the runs take about 40 minutes)
python3 zeno_char_check.py --selftest | --mutants
"""
import sys
import numpy as np
from scipy.integrate import solve_ivp
import zeno_interface_check as ZC

EDGES = [0.0, 0.125, 0.25, 0.5, 0.75, 0.875, 1.0]
BETA = 2.0
MUT = set()                                              # mutants switch parts of a coupling off (--mutants)


def coef(kind):
    amp = {"wave2": 0.0, "cross2": 1.2, "pos2": 0.9}[kind]
    bump = lambda x: np.exp(-((x - 0.25) / 0.15) ** 2) + np.exp(-((x + 0.25) / 0.15) ** 2)   # even, as a is
    return lambda s, x: (1 + x ** 2 - amp * np.sin(np.pi * s / 10) ** 2 * bump(x), BETA * x * (1 - x ** 2) ** 2)


def forcing(cf, s, x):
    u, v, uss, uxx, usx = ZC.exact(s, x); a, b = cf(s, x)
    return uss - a * uxx - 2 * b * usx


class Mesh:
    """the folded halving mesh: part 0 the symmetric [-1/8, 1/8] with an odd number of LGL intervals (its x > 0
    nodes stored), then [1/8, 1/4], ..., [7/8, 1] with n intervals each; the far end weak"""

    def __init__(self, n, kind="cross2", eps=1.0, edges=EDGES, n0=None):
        n0 = n0 or (n + 1 if n % 2 == 0 else n); e1 = edges[1]
        z, wz = ZC.lgl(n0); full = -e1 + 2 * e1 * z; wfull = 2 * e1 * wz
        P = np.where(full > 0)[0]; Mi = np.array([int(np.argmin(np.abs(full + full[p]))) for p in P])
        Df = ZC.bD(full); self.fold = (full, P, Mi, Df)
        self.blk = [(np.arange(len(P)), Df[np.ix_(P, P)] + Df[np.ix_(P, Mi)], wfull[P])]; xs = list(full[P])
        for a_, c_ in zip(edges[1:-1], edges[2:]):
            zz, ww = ZC.lgl(n); loc = a_ + (c_ - a_) * zz; i0 = len(xs); xs += list(loc)
            self.blk.append((np.arange(i0, i0 + n + 1), ZC.bD(loc), (c_ - a_) * ww))
        self.x = np.array(xs); N = len(xs); self.H = np.concatenate([w for _, _, w in self.blk])
        self.D = np.zeros((N, N))
        for idx, Dl, _ in self.blk:
            self.D[np.ix_(idx, idx)] = Dl
        self.D2 = np.zeros((N, N)); D2f = Df @ Df
        self.D2[np.ix_(self.blk[0][0], self.blk[0][0])] = D2f[np.ix_(P, P)] + D2f[np.ix_(P, Mi)]
        for idx, Dl, _ in self.blk[1:]:
            self.D2[np.ix_(idx, idx)] = Dl @ Dl
        self.cf, self.eps = coef(kind), eps

    def joins(self):
        for k in range(len(self.blk) - 1):
            yield k, self.blk[k][0][-1], self.blk[k + 1][0][0]

    def Dt(self, f, par):
        """the penalised derivative; the axis part on its full symmetric nodes, f extended there with parity par"""
        out = np.zeros_like(f); full, P, Mi, Df = self.fold; idx0 = self.blk[0][0]
        g = np.zeros(len(full)); g[P] = f[idx0]; g[Mi] = par * f[idx0]; out[idx0] = (Df @ g)[P]
        for idx, Dl, _ in self.blk[1:]:
            out[idx] = Dl @ f[idx]
        if "nojump" not in MUT:
            for _, iL, iR in self.joins():
                J = f[iL] - f[iR]; out[iL] -= 0.5 * J / self.H[iL]; out[iR] -= 0.5 * J / self.H[iR]
        return out

    def run(self, s_end=20.0):
        s_end = self.eps * abs(s_end); N = len(self.x); u0, v0 = ZC.exact(0.0, self.x)[:2]
        with np.errstate(all="ignore"):
            sol = solve_ivp(self.rhs, (0, s_end), np.concatenate([u0, v0]), method="DOP853", rtol=1e-10,
                            atol=1e-12, dense_output=True)
        errs = [np.abs(sol.sol(s)[:N] - ZC.exact(s, self.x)[0]).max() for s in np.linspace(0, sol.t[-1], 201)]
        return sol.status, sol.t[-1], errs[50], errs[100], errs[-1], max(errs)

    def spectrum(self, s):
        """max Re of eps*lambda for the semi-discrete operator frozen at s: the growth rate along the evolution"""
        N = len(self.x); M = np.zeros((2 * N, 2 * N))
        for k in range(2 * N):
            e = np.zeros(2 * N); e[k] = 1.0; M[:, k] = self.rhs(s, e, forced=False)
        return float(np.max(np.real(self.eps * np.linalg.eigvals(M))))


class DSEM(Mesh):
    gk = 0.5

    def rhs(self, s, y, forced=True):
        N = len(self.x); u, v = y[:N], y[N:]; a, b = self.cf(s, self.x); c2 = b * b + a
        ph = self.Dt(u, 1); W = v - b * ph
        if "plain2" in MUT:                                  # the second derivative not in the adjoint form
            uss = 2 * b * self.Dt(v, 1) + a * (self.D2 @ u)
        else:
            uss = b * self.Dt(v, 1) + self.Dt(b * W, -1) + self.Dt(c2 * ph, -1)
            if "nolower" not in MUT:
                uss -= self.Dt(b, -1) * v + self.Dt(a, 1) * ph
        if forced:
            uss += forcing(self.cf, s, self.x)
        for _, iL, iR in self.joins():
            gam = self.eps * self.gk * np.sqrt(max(0.5 * (c2[iL] + c2[iR]), 0.0)) * (-1 if "damp" in MUT else 1)
            JW = W[iL] - W[iR]; uss[iL] -= gam * JW / self.H[iL]; uss[iR] += gam * JW / self.H[iR]
        g = ZC.exact_ux(s, 1.0) if forced else 0.0
        uss[-1] += -(c2[-1] / self.H[-1]) * (ph[-1] - g)
        return np.concatenate([v, uss])


class SAT(Mesh):
    """the first construction (fails with varying coefficients; see the docstring)"""

    def rhs(self, s, y, forced=True):
        N = len(self.x); u, v = y[:N].copy(), y[N:].copy(); a, b = self.cf(s, self.x); ux = self.D @ u
        uss = a * (self.D2 @ u) + 2 * b * (self.D @ v) + (forcing(self.cf, s, self.x) if forced else 0); us = v.copy()
        for k, iL, iR in self.joins():
            (idL, DL, wL), (idR, DR, wR) = self.blk[k], self.blk[k + 1]
            couple(u, v, ux, us, uss, 0.5 * (a[iL] + a[iR]), 0.5 * (b[iL] + b[iR]), wL[-1], wR[0], iL, iR, idL, idR,
                   DL, DR, wL, wR, b[idL], b[idR], self.eps)
        uss[-1] += -(a[-1] / self.H[-1]) * (ux[-1] - (ZC.exact_ux(s, 1.0) if forced else 0.0))
        return np.concatenate([us, uss])


class Old(Mesh):
    """items 394-395's coupling (needs a > 0 at every joining)"""

    def rhs(self, s, y, forced=True):
        N = len(self.x); u, v = y[:N], y[N:]; a, b = self.cf(s, self.x); ux = self.D @ u
        uss = a * (self.D2 @ u) + 2 * b * (self.D @ v) + (forcing(self.cf, s, self.x) if forced else 0)
        for k, iL, iR in self.joins():
            (idL, DL, wL), (idR, DR, wR) = self.blk[k], self.blk[k + 1]
            aa, bb = 0.5 * (a[iL] + a[iR]), 0.5 * (b[iL] + b[iR]); hL, hR = wL[-1], wR[0]
            tau = 1.2 * aa * (hL + hR) / (4 * hL * hR); gam = self.eps * 0.5 * np.sqrt(aa)
            Ju, Jv, Jp = u[iL] - u[iR], v[iL] - v[iR], ux[iL] - ux[iR]
            uss[iL] += (-(aa / 2) * Jp - tau * Ju - (bb + gam) * Jv) / hL
            uss[iR] += (-(aa / 2) * Jp + tau * Ju - (bb - gam) * Jv) / hR
            uss[idL] += (aa / 2) * Ju * DL[-1] / wL; uss[idR] += (aa / 2) * Ju * DR[0] / wR
        uss[-1] += -(a[-1] / self.H[-1]) * (ux[-1] - (ZC.exact_ux(s, 1.0) if forced else 0.0))
        return np.concatenate([v, uss])


def couple(u, v, ux, us, uss, aa, bb, hL, hR, iL, iR, idL, idR, DL, DR, wL, wR, bL, bR, eps, gamk=0.5):
    """the first construction's coupling at one joining, added in place to us (u_s) and uss (v_s)"""
    c2 = bb * bb + aa; tau = c2 * (hL + hR) / (4 * hL * hR); gam = eps * gamk * np.sqrt(c2)
    Ju, Jx = u[iL] - u[iR], ux[iL] - ux[iR]; Jp = (v[iL] - bb * ux[iL]) - (v[iR] - bb * ux[iR])
    uss[iL] += (-(c2 / 2) * Jx - tau * Ju - (bb / 2 + gam) * Jp) / hL
    uss[iR] += (-(c2 / 2) * Jx + tau * Ju - (bb / 2 - gam) * Jp) / hR
    uss[idL] += (c2 / 2) * Ju * DL[-1] / wL; uss[idR] += (c2 / 2) * Ju * DR[0] / wR
    SuL, SuR = -(bb / 2) * Ju / hL, -(bb / 2) * Ju / hR
    us[iL] += SuL; us[iR] += SuR; uss[idL] += bL * DL[:, -1] * SuL; uss[idR] += bR * DR[:, 0] * SuR
    return gam, Jp


def unfolded(n=(9, 7, 11)):
    """parts [0, 1/2, 3/4, 1], unfolded, for the identities with constant coefficients"""
    edges = [0.0, 0.5, 0.75, 1.0]; blk, xs = [], []
    for (a_, c_), nk in zip(zip(edges[:-1], edges[1:]), n):
        z, w = ZC.lgl(nk); loc = a_ + (c_ - a_) * z; i0 = len(xs); xs += list(loc)
        blk.append((np.arange(i0, i0 + nk + 1), ZC.bD(loc), (c_ - a_) * w))
    N = len(xs); H = np.concatenate([w for _, _, w in blk])

    def Dt(f):
        out = np.zeros_like(f)
        for idx, Dl, _ in blk:
            out[idx] = Dl @ f[idx]
        if "nojump" not in MUT:
            for k in range(len(blk) - 1):
                iL, iR = blk[k][0][-1], blk[k + 1][0][0]; J = f[iL] - f[iR]
                out[iL] -= 0.5 * J / H[iL]; out[iR] -= 0.5 * J / H[iR]
        return out
    D2 = np.zeros((N, N))
    for idx, Dl, _ in blk:
        D2[np.ix_(idx, idx)] = Dl @ Dl
    return blk, N, H, Dt, D2


def dsem_identity(aa, bb, eps, seed=0):
    """constant a, b, the outer ends left free: d/ds [|W|^2 + c^2 |Dt u|^2] against -2 gam sum J_W^2 plus the ends'
    fluxes 2 G(W, Dt u); returns the residual relative to the terms' size"""
    rng = np.random.default_rng(seed); blk, N, H, Dt, D2 = unfolded(); c2 = bb * bb + aa
    gam = eps * DSEM.gk * np.sqrt(c2) * (-1 if "damp" in MUT else 1)
    y = rng.standard_normal(2 * N); u, v = y[:N], y[N:]; ph = Dt(u); W = v - bb * ph
    if "plain2" in MUT:
        uss = 2 * bb * Dt(v) + aa * (D2 @ u)
    else:
        uss = bb * Dt(v) + Dt(bb * W) + Dt(c2 * ph)
    JW = []
    for k in range(len(blk) - 1):
        iL, iR = blk[k][0][-1], blk[k + 1][0][0]; J = W[iL] - W[iR]; JW.append(J)
        uss[iL] -= gam * J / H[iL]; uss[iR] += gam * J / H[iR]
    Wd = uss - bb * Dt(v); phd = Dt(v)                       # W_s and (Dt u)_s
    dE = 2 * np.sum(H * W * Wd) + 2 * c2 * np.sum(H * ph * phd)
    G = lambda i: bb * W[i] ** 2 + 2 * c2 * W[i] * ph[i] + bb * c2 * ph[i] ** 2
    want = -2 * gam * sum(J * J for J in JW) + G(N - 1) - G(0)
    scale = abs(G(N - 1)) + abs(G(0)) + 2 * abs(gam) * sum(J * J for J in JW) + 1.0
    return abs(dE - want) / scale


def skew_residual(seed=0):
    rng = np.random.default_rng(seed); blk, N, H, Dt, _ = unfolded()
    u, v = rng.standard_normal(N), rng.standard_normal(N)
    r = v @ (H * Dt(u)) + Dt(v) @ (H * u) - (v[-1] * u[-1] - v[0] * u[0])
    return abs(r) / (np.abs(u).max() * np.abs(v).max() * N)


def consistency(n=12):
    """the principal operator on smooth even data against a u_xx + 2 b u_sx, relative"""
    I = DSEM(n, "cross2", 1.0); x = I.x; s = 3.7
    u = np.cos(1.3 * x) + 0.2 * np.cos(2.9 * x); v = 0.7 * np.cos(2.1 * x)
    uxx = -1.69 * np.cos(1.3 * x) - 0.2 * 8.41 * np.cos(2.9 * x); vx = -1.47 * np.sin(2.1 * x)
    a, b = I.cf(s, x); want = a * uxx + 2 * b * vx
    got = I.rhs(s, np.concatenate([u, v]), forced=False)[len(x):]
    got[-1] -= -((b[-1] ** 2 + a[-1]) / I.H[-1]) * I.Dt(u, 1)[-1]          # the far end's weak term is not principal
    return float(np.max(np.abs(got - want)) / np.max(np.abs(want)))


SAT_CASES = ((0.5, 0.0), (1.0, 0.7), (0.0, 0.4), (-0.3, 0.6), (-0.09, -0.31), (-1e-5, -0.106))


def main():
    print("energy identities, relative residual (constant a, b; either sign of a):")
    for aa, bb in SAT_CASES:
        r = max(dsem_identity(aa, bb, e, seed=k) for e in (1.0, -1.0) for k in range(3))
        print("  a = %+.5f  b = %+.3f  (speeds %+.4f %+.4f): penalised derivative %.1e" % (
            aa, bb, bb + np.sqrt(bb * bb + aa), bb - np.sqrt(bb * bb + aa), r))
    print("  Dt skew in H apart from the outer ends: %.1e" % max(skew_residual(k) for k in range(3)))
    print("  principal operator against a u_xx + 2 b u_sx on smooth data (n = 12): %.1e" % consistency())
    print("growth rate along the evolution, max Re(eps lambda), frozen at s = 5 (the band at its widest):")
    for kind in ("wave2", "pos2", "cross2"):
        for eps in (1.0, -1.0):
            for name, cls in (("item 394-395", Old), ("first construction", SAT), ("penalised derivative", DSEM)):
                if cls is Old and kind == "cross2":
                    continue
                r = [cls(n, kind, eps).spectrum(5.0 * eps) for n in (8, 16, 32)]
                print("  %-6s eps %+d %-21s n = 8 %6.2f  16 %6.2f  32 %6.2f" % ((kind, eps, name) + tuple(r)),
                      flush=True)
    print("runs to |s| = 40 against the exact solution (four openings of the band):")
    for kind, cls, ns in (("wave2", DSEM, (12,)), ("pos2", Old, (12,)), ("pos2", DSEM, (12,)),
                          ("cross2", DSEM, (8, 12, 16))):
        for eps in (1.0, -1.0):
            for n in ns:
                st, t, e10, e20, e40, em = cls(n, kind, eps).run(40.0)
                print("  %-6s %-5s eps %+d n = %2d: status %d to s = %+.0f; error |s| = 10 %.1e, 20 %.1e, 40 %.1e, "
                      "max %.1e" % (kind, cls.__name__, eps, n, st, t, e10, e20, e40, em), flush=True)


def selftest(quiet=False):
    ok = []
    r = max(dsem_identity(aa, bb, e, seed=k) for aa, bb in SAT_CASES for e in (1.0, -1.0) for k in range(2))
    ok.append(("D1 energy identity exact for a of either sign (residual %.1e)" % r, r < 1e-10))
    r = max(skew_residual(k) for k in range(3))
    ok.append(("D2 Dt skew in H apart from the outer ends (residual %.1e)" % r, r < 1e-12))
    r = consistency()
    ok.append(("D3 the principal part is a u_xx + 2 b u_sx (rel. difference %.1e at n = 12)" % r, r < 1e-6))
    g = max(DSEM(n, "wave2", e).spectrum(0.0) for n in (8, 16) for e in (1.0, -1.0))
    ok.append(("D4 no growing joining mode on wave2, either direction (max %.2f)" % g, g < 0.1))
    st, t, e5, e10, e20, em = DSEM(12, "cross2", -1.0).run(6.0)
    ok.append(("D5 through one opening of the a < 0 band, backward in s (error %.1e)" % em, st == 0 and em < 1e-4))
    if not quiet:
        for name, good in ok:
            print("%s  %s" % ("PASS" if good else "FAIL", name))
    return all(g for _, g in ok), ok


def mutants():
    caught = []
    for mname, what in (("nojump", "Dt without its jump term"), ("damp", "jump damping against the evolution"),
                        ("nolower", "the lower-order return dropped"), ("plain2", "second derivative not adjoint")):
        MUT.clear(); MUT.add(mname)
        good, ok = selftest(quiet=True)
        caught.append((what, not good, [nm.split()[0] for nm, g in ok if not g]))
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
        main()
