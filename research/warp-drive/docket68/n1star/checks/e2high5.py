#!/usr/bin/env python3
"""e2high5: the cut-off resolvent at large sigma, where trapping costs the loss (E2-PILOT section 4, D444).

E2-PILOT section 4's table (D352, checks/e2band5.py) measures ||chi_I R_l(sigma) chi_I|| for the scalar wave on 5D
Tangherlini (mu = 1, harmonic l, V_l = (1 - 1/r^2)((l(l + 2) + 3/4)/r^2 + 9/(4 r^4)), I = {r in [1.2, 4]}) only up to
sigma = 3. Lemma E2.8's proved constant grows linearly in |sigma| (section 3e). Here the actual norm is followed to
large sigma, where the harmonics whose barrier top max V_l is near sigma^2 are trapped at the photon sphere.

Method (computed; a numerical ODE solve, not certified). u_h (u = e^(-i sigma x) at the horizon) and u_inf (outgoing,
sqrt(x) H^(1)_(l+1)(sigma x) at x = 4000) are carried by their log-derivatives w = u'/u, which solve the Riccati
equation w' = V - sigma^2 - w^2 and are smooth where u is a single WKB wave, and by L = log u, up to the barrier peak;
beyond it, where u is a standing wave, by the linear equation with the scale carried along. The kernel
u_h(x_<) u_inf(x_>)/W is formed in logarithms (W = u_h u_inf (w_inf - w_h), constant), and its norm on a uniform grid
of I in x = r_* (at least 40 points per wavelength) is the largest singular value, by power iteration on its
semiseparable structure.

  H1 control: D352's row at sigma = 3 (l = 0, 1, 2, 4, 8, 16, 32: 0.41, 0.42, 0.45, 0.67, 0.73, 0.065, 0.014).
  H2 accuracy: the Wronskian's spread over I (in modulus, D453), and the norm on a grid twice as fine and at a
     tighter tolerance (relative agreement better than 2 x 10^-3: the 40-points-per-wavelength grid sets it).
  H3 at each sigma in {3, 6, 12, 24, 48, 96}, the norm over l (every l to 3 sigma + 4 at sigma <= 6, the 13 around
     the trapped l above), its maximum and where it is attained, and the fit sigma * max = a + b log sigma
     at those sigma (all at one phase of the maximum's oscillation in sigma, period about 1/2, the barrier tops'
     spacing; near sigma = 12 it runs 3.752-4.112 in sigma * max, D453).
  H4 the worst sigma for a fixed harmonic: for l = 4, 8, 16, 32, 64, the largest norm over 11 sigma with
     sigma^2 / max V_l in [0.9, 1.1], and sigma times it.

  --vs-e28 (D452) Lemma E2.8's bound against H3's maxima: its sup over 1 <= l <= 12 and at the trapped l.

Run: python3 checks/e2high5.py   (about 80 minutes);   python3 checks/e2high5.py --vs-e28   (a few minutes)
"""
import math
import sys
import time

import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import h1vp, hankel1

A_, B_ = 1.2, 4.0
X0, X1 = -30.0, 4000.0


def rstar(r):
    return r + 0.5 * math.log((r - 1) / (r + 1))


def r_of(x):
    """r_*(r) = x by Newton in q = log(r - 1)"""
    q = math.log(x - 1) if x > 3 else 2 * (x - 1) + math.log(2)
    for _ in range(60):
        e = math.exp(q)
        F = 1 + e + 0.5 * (q - math.log(2 + e)) - x
        dF = e + 0.5 * (1 - e / (2 + e))
        dq = F / dF
        q -= dq
        if abs(dq) < 1e-15 * max(1.0, abs(q)):
            break
    return 1 + math.exp(q)


def V(r, l):
    return (1 - 1 / r**2) * ((l * (l + 2) + 0.75) / r**2 + 2.25 / r**4)


def vmax(l):
    rr = np.linspace(1.0001, 6, 20001)
    v = (1 - 1 / rr**2) * ((l * (l + 2) + 0.75) / rr**2 + 2.25 / rr**4)
    return float(v.max())


def x_peak(l):
    rr = np.linspace(1.0001, 6, 20001)
    v = (1 - 1 / rr**2) * ((l * (l + 2) + 0.75) / rr**2 + 2.25 / rr**4)
    return rstar(float(rr[v.argmax()]))


def solution(l, s, start, xs, rtol):
    """(S, u, u') on xs with the solution = exp(S) u: Riccati for w = u'/u and L = log u from the horizon ('h') or
    from x = X1 ('inf') to the barrier peak x_p, where it is a single WKB wave, then the linear equation beyond"""
    xp = x_peak(l)

    def ric(x, y):
        w = complex(y[0], y[1])
        dw = V(r_of(x), l) - s * s - w * w
        return [dw.real, dw.imag, w.real, w.imag]

    def lin(x, y):
        u = complex(y[0], y[1])
        upp = (V(r_of(x), l) - s * s) * u
        return [y[2], y[3], upp.real, upp.imag]
    n = len(xs)
    S_, U, UP = np.zeros(n, complex), np.zeros(n, complex), np.zeros(n, complex)
    if start == 'h':
        near, far = xs <= xp, xs > xp
        w0, L0, span, ev = -1j * s, -1j * s * X0, (X0, xp), np.append(xs[near], xp)
    else:
        nu, z = l + 1, s * X1
        near, far = xs >= xp, xs < xp
        w0 = 0.5 / X1 + s * h1vp(nu, z) / hankel1(nu, z)
        L0, span, ev = 0j, (X1, xp), np.append(xs[near][::-1], xp)
    sol = solve_ivp(ric, span, [w0.real, w0.imag, L0.real, L0.imag], t_eval=ev, rtol=rtol, atol=1e-14,
                    method='DOP853')
    assert sol.success, sol.message
    w = sol.y[0] + 1j * sol.y[1]
    L = sol.y[2] + 1j * sol.y[3]
    idx = np.where(near)[0] if start == 'h' else np.where(near)[0][::-1]
    S_[idx], U[idx], UP[idx] = L[:-1], 1.0, w[:-1]
    wp, Lp = w[-1], L[-1]
    fidx = np.where(far)[0] if start == 'h' else np.where(far)[0][::-1]
    if len(fidx):
        end = xs[-1] if start == 'h' else xs[0]
        sol2 = solve_ivp(lin, (xp, end), [1.0, 0.0, wp.real, wp.imag], t_eval=xs[fidx], rtol=rtol, atol=1e-14,
                         method='DOP853')
        assert sol2.success, sol2.message
        S_[fidx], U[fidx], UP[fidx] = Lp, sol2.y[0] + 1j * sol2.y[1], sol2.y[2] + 1j * sol2.y[3]
    return S_, U, UP


def norm_semisep(a, b, h, iters=400):
    """largest singular value of h K, K_ij = a_min(i,j) b_max(i,j), by power iteration on K* K"""
    def mv(v, a_, b_):
        lo = np.cumsum(a_ * v)
        hi = np.cumsum((b_ * v)[::-1])[::-1]
        hi = np.concatenate([hi[1:], [0]])
        return b_ * lo + a_ * hi
    rng = np.random.default_rng(0)
    v = rng.standard_normal(len(a)) + 1j * rng.standard_normal(len(a))
    v /= np.linalg.norm(v)
    lam = 0.0
    for k in range(iters):
        u = mv(v, a, b)
        v2 = np.conj(mv(np.conj(u), a, b))
        nl = np.linalg.norm(v2)
        v = v2 / nl
        if k > 20 and abs(nl - lam) < 1e-12 * nl:
            break
        lam = nl
    return h * math.sqrt(nl)


def cutoff_norm(l, s, ppw=40, rtol=1e-11):
    a, b = rstar(A_), rstar(B_)
    n = max(161, int(ppw * s * (b - a) / (2 * math.pi)) + 1)
    xs = np.linspace(a, b, n)
    h = xs[1] - xs[0]
    Sh, Uh, UPh = solution(l, s, 'h', xs, rtol)
    Si, Ui, UPi = solution(l, s, 'inf', xs, rtol)
    logW = Sh + Si + np.log(Uh * UPi - UPh * Ui)
    lw = logW.mean()
    spread = float(np.ptp(np.abs(np.exp(logW - lw))))
    # K_ij = u_h(x_min) u_inf(x_max) / W = a_min b_max, the scale c balancing the two factors
    c = 0.5 * ((Sh + np.log(np.abs(Uh))).real.max() - (Si - lw + np.log(np.abs(Ui))).real.max())
    A = np.exp(Sh - c) * Uh
    Bv = np.exp(Si - lw + c) * Ui
    return norm_semisep(A, Bv, h), spread, n


MEASURED = {3.0: (1.132, 5), 6.0: (0.61801, 11), 12.0: (0.33551, 23), 24.0: (0.18101, 47), 48.0: (0.097196, 95),
            96.0: (0.051938, 191)}   # H3's maxima and the l attaining them (D444's run)


def vs_e28():
    """--vs-e28 (D452): Lemma E2.8's bound B_l(sigma) (checks/e2morawetz5.py, s optimised per l and sigma) against
    H3's measured maxima: its sup over 1 <= l <= 12 and its value at the trapped l"""
    import e2morawetz5 as E
    r, x, f = E.grid()
    for s, (act, lt) in MEASURED.items():
        rows = [(l, (E.best(l, r, x, f, sigma=s) or (None, math.inf))[1]) for l in range(1, 13)]
        lm, bm = max(rows, key=lambda t: t[1])
        bt = (E.best(lt, r, x, f, sigma=s) or (None, math.inf))[1]
        print("  sigma %4g: measured max %.4g (l = %d); E2.8 sup over l <= 12 %.4g (at l = %d), ratio %.3g; E2.8 at the "
              "trapped l %.4g, ratio %.3g" % (s, act, lt, bm, lm, bm / act, bt, bt / act), flush=True)
    return 0


def main():
    if sys.argv[1:2] == ["--vs-e28"]:
        sys.path.insert(0, __file__.rsplit("/", 1)[0])
        return vs_e28()
    ok = {}
    t0 = time.time()
    ref = {0: 0.41, 1: 0.42, 2: 0.45, 4: 0.67, 8: 0.73, 16: 0.065, 32: 0.014}
    got = {l: cutoff_norm(l, 3.0)[0] for l in ref}
    ok["H1"] = all(abs(got[l] - ref[l]) <= 0.006 + 0.012 * ref[l] for l in ref)
    print("  H1 sigma = 3, D352's row: " + ", ".join("l %d %.4g (%.3g)" % (l, got[l], ref[l]) for l in ref), flush=True)
    worst = 0.0
    for l, s in ((8, 3.0), (60, 30.0), (24, 12.0)):
        n1, sp1, n = cutoff_norm(l, s)
        n2, sp2, _ = cutoff_norm(l, s, ppw=80, rtol=1e-12)
        worst = max(worst, abs(n1 - n2) / n2, sp1, sp2)
        print("  H2 l %d sigma %g: %.8g (%d points) vs %.8g (twice as fine, rtol 1e-12); Wronskian spread %.1e, %.1e"
              % (l, s, n1, n, n2, sp1, sp2), flush=True)
    ok["H2"] = worst < 2e-3
    print("  H3 (every l from 0 to 3 sigma + 4 at sigma <= 6; at sigma >= 12 the l within 6 of l_top, the l whose"
          " barrier top is the first above sigma^2: the full scans of D444's first run, to sigma = 24, peaked"
          " there)", flush=True)
    peaks = {}
    for s in (3.0, 6.0, 12.0, 24.0, 48.0, 96.0):
        ltop = next(l for l in range(0, 10 * int(s) + 10) if vmax(l) > s * s)
        ls = range(0, int(3 * s) + 5) if s <= 6 else range(max(0, ltop - 6), ltop + 7)
        rows = [(l, cutoff_norm(l, s)[0], s * s / vmax(l)) for l in ls]
        lm, nm, ratio = max(rows, key=lambda t: t[1])
        peaks[s] = (lm, nm, ltop)
        edge = lm in (rows[0][0], rows[-1][0]) and s > 6
        print("      sigma %4g: max %.5g at l = %d (l_top %d; sigma^2/max V_l = %.4f)%s; sigma * max = %.4f"
              % (s, nm, lm, ltop, ratio, " AT THE WINDOW'S EDGE" if edge else "", s * nm), flush=True)
    xs = np.array([math.log(s) for s in peaks])
    ys = np.array([s * peaks[s][1] for s in peaks])
    b_, a_ = np.polyfit(xs, ys, 1)
    res = ys - (a_ + b_ * xs)
    print("      fit sigma * max = a + b log sigma: a = %.4f, b = %.4f, residuals %s" % (
        a_, b_, " ".join("%+.3f" % q for q in res)), flush=True)
    ok["H3"] = all(peaks[s][0] == peaks[s][2] - 1 or peaks[s][0] == peaks[s][2] for s in peaks if s > 6) \
        and abs(res).max() < 0.05 and b_ > 0
    print("  H4 (the worst sigma near each barrier top)", flush=True)
    h4 = []
    for l in (4, 8, 16, 32, 64):
        top = math.sqrt(vmax(l))
        best = max(((cutoff_norm(l, top * f)[0], top * f) for f in np.linspace(math.sqrt(0.9), math.sqrt(1.1), 11)))
        h4.append((l, top, best[1], best[0]))
        print("      l %2d: sqrt(max V_l) = %.4f; largest norm %.5g at sigma = %.4f (sigma^2/max V_l = %.4f); sigma * "
              "norm = %.4f" % (l, top, best[0], best[1], best[1]**2 / top**2, best[1] * best[0]), flush=True)
    ok["H4"] = all(x[3] > 0 for x in h4)
    print("  (%.0f s)" % (time.time() - t0))
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
