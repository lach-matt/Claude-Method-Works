#!/usr/bin/env python3
"""r5models5: programs for the steps FAMILIES5-VLASOV.md (round 5) lists as deduced but not computed
(FAMILIES5-R6.md section 5). Each is a model: it computes the mechanism of the deduction, not the deduction itself.

  M1 (numpy, Gauss-Newton) Proposition L' (solving the constraints up to the KID, and the charge's dichotomy) on a
     model constraint map with the same structure: Phi(u, v) = u' + v'' + w(x) (u^2 - kappa v'^2) on [0, 1], unknowns
     supported in U = (0.2, 0.8). DPhi(0) = u' + v'' has the compactly supported kernel u = -v' (the seeds) and the
     one-dimensional cokernel of constants (the model's KID: int 1 . (u' + v'') = 0). Solving Phi(eps delta + c) =
     m(eps) zeta (zeta a fixed bump, c supported in U, minimum norm): (a) for a seed (DPhi(delta) = 0), |c| = O(eps^2)
     and m(eps)/eps^2 -> Q(delta)/int zeta, Q = int w (1 - kappa) v'^2 (the charge); (b) with w > 0, kappa < 1, Q > 0
     on every seed, so no exactly localised solution near 0 (m != 0 for every eps small); (c) with w changing sign,
     Q changes sign along a one-parameter family of seeds, and the intermediate value theorem gives exactly localised
     solutions: m(eps, s(eps)) = 0 found by bisection, Phi = 0 to the solver's tolerance, c supported in U. Control
     (must fail; the verifier of round 5, minor 5): a delta with DPhi(delta) != 0 gives |c|/eps -> const, not O(eps),
     and m/eps^2 does not converge to Q.
  M2 (numpy, closed forms) Theorem V's diagonal step: on R^2, N odd labels w_A = 2 pi A/N with weights 2 pi/N,
     hierarchical frequencies a_A = Lam^A, the oscillation d g_N = sum_A F_A k_A sin(a_A k_A . x/lam), F_A = sqrt(2 pi
     /N) F(x, w_A) (Gaussian in x, smooth in w). lam_N is chosen as in the proof (halved until |int eta_j d g_N| <=
     1/N for the first N test fields eta_j); then (a) for test fields outside the list, int eta d g_N -> 0 as N grows;
     (b) |d g_N|_L2^2 -> (1/2) int int F^2 dw dx, the label quadrature of the Vlasov energy (cross terms vanish), so
     the sequence is bounded in L^2 uniformly in N. All integrals are closed Gaussian forms. Control (must fail):
     without the hierarchy and with an even N (antipodal labels with a_A = 1), the cross term of an antipodal pair,
     sin(k.x/lam) sin(-k.x/lam), does not average out, so the L^2 limit misses the quadrature (it gives a
     different value).
  M3 (numpy, finite differences) Lemma A' (b) on a model of the leaf map: w[U] solving -(A(U) w')' = f(U) on (0, 1),
     w = 0 at the ends (the leaf equation's ellipticity, with coefficients depending on U pointwise). On a small
     H^2 ball, |w[U]' - w[U']'|_L2 / |U - U'|_L2 (the slope: the shear is first order in the leaf's normal) stays
     bounded over random pairs, high-frequency differences included. Control (must fail; the verifier's minor 4):
     coefficients depending on U' = dU/dx when U does not carry dU as a component (A = A(U')): the ratio grows like the
     difference's frequency.

Labels: computed (models). Run: python3 checks/r5models5.py   (about a minute)
"""
import math
import sys

import numpy as np

# ---------------------------------------------------------------- M1
NX = 241
X = np.linspace(0.0, 1.0, NX)
H = X[1] - X[0]
INS = (X > 0.2 + 1e-12) & (X < 0.8 - 1e-12)


def bump(x, a, b):
    y = 2 * (x - a) / (b - a) - 1
    out = np.zeros_like(y)
    m = np.abs(y) < 1
    out[m] = np.exp(1 - 1 / (1 - y[m]**2))
    return out


def d1(f):
    return np.gradient(f, H, edge_order=2)


def d2(f):
    out = np.zeros_like(f)
    out[1:-1] = (f[2:] - 2 * f[1:-1] + f[:-2]) / H**2
    return out


def Phi(u, v, w, kappa):
    vp = d1(v)
    return d1(u) + d1(vp) + w * (u**2 - kappa * vp**2)                     # d1 d1 so that u = -v' is an exact seed


ZETA = bump(X, 0.3, 0.7)


def solve_up_to_kid(du, dv, eps, w, kappa, iters=12):
    """c = (cu, cv) supported in U and m with Phi(eps delta + c) = m zeta, by Gauss-Newton (minimum norm)"""
    idx = np.where(INS)[0]
    n = len(idx)
    z = np.zeros(2 * n + 1)

    def unpack(z):
        cu, cv = np.zeros(NX), np.zeros(NX)
        cu[idx], cv[idx] = z[:n], z[n:2 * n]
        return cu, cv, z[-1]

    def res(z):
        cu, cv, m = unpack(z)
        return Phi(eps * du + cu, eps * dv + cv, w, kappa) - m * ZETA
    for _ in range(iters):
        r0 = res(z)
        # the Jacobian by linearisation at the current point (exact for the quadratic map up to rounding)
        cu, cv, m = unpack(z)
        u, v = eps * du + cu, eps * dv + cv
        vp = d1(v)
        J = np.zeros((NX, 2 * n + 1))
        for k, i in enumerate(idx):
            e = np.zeros(NX)
            e[i] = 1.0
            J[:, k] = d1(e) + 2 * w * u * e
            J[:, n + k] = d1(d1(e)) - 2 * w * kappa * vp * d1(e)
        J[:, -1] = -ZETA
        step = np.linalg.lstsq(J, -r0, rcond=None)[0]
        z = z + step
        if np.max(np.abs(step)) < 1e-15:
            break
    cu, cv, m = unpack(z)
    return cu, cv, m, float(np.max(np.abs(res(z))))


def seed(shape=1.0):
    """a compactly supported seed of DPhi(0): u = -v', v a bump in U"""
    v = bump(X, 0.3, 0.7) * (np.sin(2 * math.pi * 3 * (X - 0.3)) + shape)
    return -d1(v), v


def charge(du, dv, w, kappa):
    return float(np.trapezoid(w * (du**2 - kappa * d1(dv)**2), X))


def m1():
    print("M1 (model) Proposition L': the charge, its dichotomy, and the intermediate-value construction")
    ok = True
    kappa = 0.3
    wpos = 1.0 + 0.5 * X
    du, dv = seed()
    Q = charge(du, dv, wpos, kappa)
    rows = []
    for eps in (4e-2, 2e-2, 1e-2):
        cu, cv, m, r = solve_up_to_kid(du, dv, eps, wpos, kappa)
        rows.append((eps, float(np.max(np.abs(np.concatenate([cu, cv])))), m, r))
    zint = float(np.trapezoid(ZETA, X))
    ratios = [r[2] / r[0]**2 * zint for r in rows]
    c_order = [r[1] / r[0]**2 for r in rows]
    conv_m = abs(ratios[2] - ratios[1]) < 0.6 * abs(ratios[1] - ratios[0])          # an O(eps) correction
    conv_c = abs(c_order[2] - c_order[1]) < 0.6 * abs(c_order[1] - c_order[0])
    a_ok = abs(ratios[-1] - Q) < 0.01 * abs(Q) and conv_m and conv_c and all(r[3] < 1e-9 for r in rows)
    b_ok = Q > 0 and all(r[2] > 0 for r in rows)
    print("   (a) Q(delta) = %.6f; m(eps) int zeta/eps^2 = %s -> Q (differences halving): %s; |c|/eps^2 = %s "
          "(converging: c = O(eps^2)); residuals %s" %
          (Q, ", ".join("%.6f" % x for x in ratios), a_ok, ", ".join("%.4f" % x for x in c_order),
           ", ".join("%.1e" % r[3] for r in rows)))
    print("   (b) w > 0, kappa < 1: Q > 0 and m(eps) > 0 at every eps: no exactly localised solution: %s" % b_ok)
    # (c) w changing sign: a family of seeds whose charge changes sign
    wch = np.tanh(8 * (X - 0.5))
    fam = lambda s: (-d1(bump(X, 0.25, 0.45) + s * bump(X, 0.55, 0.75)),            # noqa: E731
                     bump(X, 0.25, 0.45) + s * bump(X, 0.55, 0.75))
    q0, q1 = charge(*fam(0.0), wch, kappa), charge(*fam(2.0), wch, kappa)
    eps = 2e-2
    lo, hi = 0.0, 2.0
    mlo = solve_up_to_kid(*fam(lo), eps, wch, kappa)[2]
    mhi = solve_up_to_kid(*fam(hi), eps, wch, kappa)[2]
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        mm = solve_up_to_kid(*fam(mid), eps, wch, kappa)[2]
        if (mm > 0) == (mlo > 0):
            lo, mlo = mid, mm
        else:
            hi = mid
    cu, cv, mfin, rfin = solve_up_to_kid(*fam(hi), eps, wch, kappa)
    duf, dvf = fam(hi)
    full = Phi(eps * duf + cu, eps * dvf + cv, wch, kappa)
    supp = bool(np.all(cu[~INS] == 0) and np.all(cv[~INS] == 0))
    c_ok = q0 * q1 < 0 and mlo * mhi < 0 and abs(mfin) < 1e-10 and float(np.max(np.abs(full))) < 1e-9 and supp
    print("   (c) w = tanh(8 (x - 1/2)): Q(s = 0) = %.5f, Q(s = 2) = %.5f; at eps = 0.02 the bisection gives s* = %.6f "
          "with m = %.1e, max |Phi| = %.1e, c supported in U: %s; exactly localised: %s" %
          (q0, q1, hi, mfin, float(np.max(np.abs(full))), supp, c_ok))
    # control: a delta with DPhi(delta) != 0
    dub, dvb = seed()
    dub = dub + bump(X, 0.35, 0.65)                                           # leaves a linear residual
    rowsb = []
    for eps in (4e-2, 2e-2, 1e-2):
        cu, cv, m, r = solve_up_to_kid(dub, dvb, eps, wpos, kappa)
        rowsb.append((eps, float(np.max(np.abs(np.concatenate([cu, cv])))) / eps, m / eps**2 * zint))
    Qb = charge(dub, dvb, wpos, kappa)
    ctl = min(r[1] for r in rowsb) > 0.1 and abs(rowsb[-1][2] - Qb) > 0.05 * abs(Qb)
    print("   control (DPhi(delta) != 0): |c|/eps = %s (O(eps), not O(eps^2)); m int zeta/eps^2 = %s vs Q = %.4f "
          "(rejected): %s" % (", ".join("%.4f" % r[1] for r in rowsb), ", ".join("%.3f" % r[2] for r in rowsb), Qb,
                              ctl))
    return a_ok and b_ok and c_ok and ctl


# ---------------------------------------------------------------- M2
def gauss_int(c0, s2, K, phase=0.0):
    """int over R^2 of c0 exp(-|x|^2/(2 s2)) cos(K.x + phase) dx (closed form)"""
    return c0 * 2 * math.pi * s2 * math.exp(-0.5 * s2 * float(K @ K)) * math.cos(phase)


def m2():
    print("M2 (model) Theorem V's diagonal: weak convergence and an L^2 bound uniform in N")
    Fw = lambda w: 1.0 + 0.4 * math.cos(w) + 0.2 * math.sin(2 * w)                  # noqa: E731
    # F(x, w) = Fw(w) exp(-|x|^2/2); d g_N = sum_A F_A k_A sin(a_A k_A.x/lam)
    energy = 0.5 * sum(Fw(2 * math.pi * j / 4096)**2 for j in range(4096)) * 2 * math.pi / 4096 * math.pi
    tests = [(np.array([0.3 * j, -0.2 * j]), 0.5 + 0.1 * j) for j in range(40)]     # eta_j: centres, widths

    def pair_int(KA, KB, sA, sB):
        """int sA sB with sA = exp(-|x|^2/2) sin(KA.x): (1/2) int e^-|x|^2 (cos((KA-KB).x) - cos((KA+KB).x))"""
        return 0.5 * (gauss_int(1.0, 0.5, KA - KB) - gauss_int(1.0, 0.5, KA + KB))

    def eta_int(KA, cen, wid):
        """int eta exp(-|x|^2/2) sin(KA.x), eta = exp(-|x - cen|^2/(2 wid^2)): a shifted Gaussian, closed form"""
        s2 = 1.0 / (1.0 + 1.0 / wid**2)
        m = s2 * cen / wid**2
        pref = math.exp(-0.5 * (float(cen @ cen) / wid**2 - float(m @ m) / s2))
        return pref * 2 * math.pi * s2 * math.exp(-0.5 * s2 * float(KA @ KA)) * math.sin(float(KA @ m))

    def build(N, lam, Lam, hier=True):
        ws = [2 * math.pi * A / N for A in range(N)]
        a = [Lam**A if hier else 1.0 for A in range(N)]
        Ks = [a[A] / lam * np.array([math.cos(ws[A]), math.sin(ws[A])]) for A in range(N)]
        wts = [math.sqrt(2 * math.pi / N) * Fw(w) for w in ws]
        return ws, a, Ks, wts

    def l2sq(N, lam, Lam, hier=True):
        ws, a, Ks, wts = build(N, lam, Lam, hier)
        tot = 0.0
        for A in range(N):
            for B in range(N):
                kAkB = math.cos(ws[A] - ws[B])                                       # k_A . k_B (unit)
                tot += wts[A] * wts[B] * kAkB * pair_int(Ks[A], Ks[B], 1, 1)
        return tot

    def weak(N, lam, Lam, eta):
        ws, a, Ks, wts = build(N, lam, Lam)
        return max(abs(sum(wts[A] * math.cos(ws[A]) * eta_int(Ks[A], eta[0], eta[1]) for A in range(N))),
                   abs(sum(wts[A] * math.sin(ws[A]) * eta_int(Ks[A], eta[0], eta[1]) for A in range(N))))
    rows = []
    for N in (5, 9, 15, 25):
        Lam = 3.0
        lam = 1.0
        while max(weak(N, lam, Lam, tests[j]) for j in range(min(N, len(tests)))) > 1.0 / N:
            lam /= 2
        en = l2sq(N, lam, Lam)
        out_test = weak(N, lam, Lam, (np.array([0.77, 0.41]), 0.9))
        rows.append((N, lam, en, out_test))
    # the quadrature of (1/2) int int F^2 dw dx at each N (cross terms dropped): its N-dependence is the trapezoid's
    quad = lambda N: 0.5 * sum((2 * math.pi / N) * Fw(2 * math.pi * A / N)**2 for A in range(N)) * math.pi  # noqa
    a_ok = rows[-1][3] < rows[0][3] and rows[-1][3] < 1e-3
    b_ok = all(abs(r[2] - quad(r[0])) < 1e-6 * quad(r[0]) for r in rows) and \
        abs(rows[-1][2] - energy) < 1e-6 * energy
    print("   %s" % "; ".join("N = %d: lam_N = %.3g, |dg_N|^2 = %.6f, int eta dg_N (eta outside the list) = %.2e" % r
                              for r in rows))
    print("   (a) weak convergence on an outside test field: %s; (b) |dg_N|^2 equals the label quadrature (1/2) sum "
          "(2 pi/N) int F_A^2 (cross terms vanish) and tends to the Vlasov energy %.6f: %s" % (a_ok, energy, b_ok))
    # control: even N, no hierarchy (antipodal pairs at equal frequency)
    N = 6
    en_bad = l2sq(N, 1e-3, 1.0, hier=False)
    ctl = abs(en_bad - quad(N)) > 1e-3 * quad(N)
    print("   control (N = 6, a_A = 1): |dg|^2 = %.6f vs the quadrature %.6f: the antipodal cross terms survive "
          "(rejected): %s" % (en_bad, quad(N), ctl))
    return a_ok and b_ok and ctl


# ---------------------------------------------------------------- M3
def leaf(U, Ufun_coef, f_src, n=400):
    """w with -(A w')' = f on (0, 1), w(0) = w(1) = 0, A = A(U at midpoints)"""
    x = np.linspace(0, 1, n + 1)
    h = 1.0 / n
    Um = 0.5 * (U[1:] + U[:-1])
    A = Ufun_coef(Um, (U[1:] - U[:-1]) / h)
    main = (A[:-1] + A[1:]) / h**2
    off = -A[1:-1] / h**2
    M = np.diag(main) + np.diag(off, 1) + np.diag(off, -1)
    w = np.zeros(n + 1)
    w[1:-1] = np.linalg.solve(M, f_src(U[1:-1]))
    return w


def m3():
    print("M3 (model) Lemma A' (b): the leaf map is L^2-Lipschitz on a small H^2 ball when its coefficients are U's")
    n = 400
    x = np.linspace(0, 1, n + 1)
    h = 1.0 / n
    rng = np.random.default_rng(7)
    good = lambda Um, Up: 1.0 + 0.5 * np.tanh(Um)                                   # noqa: E731
    bad = lambda Um, Up: 1.0 + 0.5 * np.tanh(Up)                                    # noqa: E731
    f_src = lambda U: 1.0 + U**2                                                     # noqa: E731
    l2 = lambda f: float(np.sqrt(np.sum(f**2) * h))                                 # noqa: E731
    U0 = 0.2 * np.sin(math.pi * x)
    rg, rb = [], []
    for kfreq in (2, 8, 32, 64):
        for _ in range(3):
            # a difference in a small H^2 ball: amplitude 1e-3/(k pi)^2
            dU = 1e-3 / (kfreq * math.pi)**2 * np.sin(kfreq * math.pi * x + rng.uniform(0, 6))
            for coef, store in ((good, rg), (bad, rb)):
                w1 = leaf(U0, coef, f_src, n)
                w2 = leaf(U0 + dU, coef, f_src, n)
                # the output is the leaf's slope (the shear is first order in the leaf's normal)
                store.append((kfreq, l2(np.diff(w2 - w1) / h) / l2(dU)))
    gmax = max(r[1] for r in rg)
    by_k = lambda rows, k: max(r[1] for r in rows if r[0] == k)                     # noqa: E731
    good_ok = gmax < 2 * min(r[1] for r in rg if r[0] == 2) + 1.0
    ctl = by_k(rb, 64) > 5 * by_k(rb, 2)
    print("   coefficients A(U): ratio |dw|_L2/|dU|_L2 by frequency 2, 8, 32, 64: %s (bounded: %s)" %
          (", ".join("%.4f" % by_k(rg, k) for k in (2, 8, 32, 64)), good_ok))
    print("   control (A(U'), U' not a component): %s (grows with the frequency; rejected): %s" %
          (", ".join("%.4f" % by_k(rb, k) for k in (2, 8, 32, 64)), ctl))
    return good_ok and ctl


def main():
    res = {}
    for name, fn in (('M1', m1), ('M2', m2), ('M3', m3)):
        res[name] = fn()
        print(name, 'PASS' if res[name] else 'FAIL', flush=True)
    return 0 if all(res.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
