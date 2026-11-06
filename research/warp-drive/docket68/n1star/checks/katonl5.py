#!/usr/bin/env python3
"""katonl5: the iteration behind Theorem K (FAMILIES5-VLASOV.md section 6) on a model with a non-local source.

Theorem K (proved there) is Kato's local theory for quasi-linear symmetric hyperbolic systems with a zero-order source
F that is non-local: the proof uses of F only (K1) boundedness on H^s balls and (K2) L^2-Lipschitz continuity on them.
Here the Picard iteration of that proof is run on the model
    u_t + (1 + u) u_x = F(u),      F(u) = -(1 - d_x^2)^-1 (u^2)      (periodic, x in [0, 2 pi)),
F non-local, bounded H^s -> H^(s+2) and L^2-Lipschitz on H^1 balls (|F(u) - F(v)|_(L^2) <= |u + v|_(L^inf) |u - v|).
  K1 (numpy, spectral in x, RK4 in t) the iterates u^(n+1)_t + (1 + u^n) u^(n+1)_x = F(u^n), u^(n+1)(0) = u0: the
     differences sup_t |u^(n+1) - u^n|_(L^2) fall geometrically (each ratio < 0.5) and sup_n sup_t |u^n|_(H^2) stays
     bounded (within 5 % of the first iterate's); (K2) is measured, |F(u) - F(v)|/|u - v| <= |u + v|_inf on random
     pairs.
  Control (must fail): a source that is not L^2-Lipschitz, F(u) = 0.5 u_xx (it loses two derivatives): the H^2 norms of
     the iterates grow without bound (the sixth iterate's H^2 norm exceeds twenty times the first, and the last three
     increase), so the iteration does not close. [R6, the verifier of round 5, minor 8: 0.5 u_xx maps H^s to H^(s-2),
     so it violates (K1) as well as (K2).]
  K2 (numpy; R6, the verifier of round 5, Major 3) Theorem K's Cauchy-stability clause on the model. The source is
     tame, (K1'): |F(u)|_(H^s) = |u^2|_(H^(s-2)) <= C |u|_(L^inf) |u|_(H^s) (measured on random u, s = 2). The
     background ubar (data u0) is solved on [0, T_b], T_b = 1.0, inside its lifespan; for data u0 + d eta, d = 4e-3,
     2e-3, 1e-3, the solution exists on all of [0, T_b] and sup_t |u_d - ubar|_(H^2)/d is the same to 5 % for the
     three d (Lipschitz dependence over the background's whole interval, not only for short times). Control (must
     fail): the same on [0, 3.0], past the background's gradient blow-up (the shock), where the background is not a
     solution: the H^2 norm of ubar grows by more than a factor 20 and the ratio test fails.
Labels: computed (numpy, a model). Run: python3 checks/katonl5.py   (about a minute)
"""
import sys

import numpy as np

NX, T, NT = 128, 0.5, 400
x = 2 * np.pi * np.arange(NX) / NX
k = np.fft.fftfreq(NX, 1.0 / NX)


def dx(f, n=1):
    return np.real(np.fft.ifft((1j * k)**n * np.fft.fft(f)))


def F_good(u):
    return -np.real(np.fft.ifft(np.fft.fft(u**2) / (1 + k**2)))


def F_bad(u):
    return 0.5 * dx(u, 2)


def h2(f):
    fh = np.fft.fft(f) / NX
    return float(np.sqrt(2 * np.pi * np.sum((1 + k**2)**2 * np.abs(fh)**2)))


def l2(f):
    return float(np.sqrt(2 * np.pi / NX * np.sum(f**2)))


def iterate(F, nit=8):
    u0 = 0.3 * np.sin(x) + 0.2 * np.cos(2 * x)
    dt = T / NT
    prev = np.tile(u0, (NT + 1, 1))                               # u^0(t) = u0
    diffs, norms = [], []
    for _ in range(nit):
        new = np.empty_like(prev)
        new[0] = u0
        u = u0.copy()
        for j in range(NT):
            def rhs(w, a, s):
                return -(1 + a) * dx(w) + s
            a0, a1 = prev[j], prev[j + 1]
            ah = (a0 + a1) / 2
            s0, s1, sh = F(a0), F(a1), F(ah)
            k1 = rhs(u, a0, s0)
            k2 = rhs(u + dt / 2 * k1, ah, sh)
            k3 = rhs(u + dt / 2 * k2, ah, sh)
            k4 = rhs(u + dt * k3, a1, s1)
            u = u + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            new[j + 1] = u
        diffs.append(max(l2(new[j] - prev[j]) for j in range(0, NT + 1, 10)))
        norms.append(max(h2(new[j]) for j in range(0, NT + 1, 10)))
        prev = new
    return diffs, norms


def solve(u0, Tf, nt):
    """the model solved directly (RK4, spectral, 2/3 dealiasing), with the H^2 norm along the way"""
    dt = Tf / nt
    keep = np.abs(k) < NX / 3

    def rhs(w):
        w = np.real(np.fft.ifft(np.fft.fft(w) * keep))
        return -(1 + w) * dx(w) + F_good(w)
    u = u0.copy()
    traj = [u.copy()]
    for _ in range(nt):
        k1 = rhs(u)
        k2 = rhs(u + dt / 2 * k1)
        k3 = rhs(u + dt / 2 * k2)
        k4 = rhs(u + dt * k3)
        u = u + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        traj.append(u.copy())
    return traj


def k2():
    print("K2 (numpy) Cauchy stability over the background's whole interval, with the tame source")
    rng = np.random.default_rng(3)
    tame = []
    for _ in range(20):
        u = sum(rng.normal() * np.cos(m * x + rng.uniform(0, 6)) / (1 + m**2) for m in range(1, 9))
        tame.append(h2(F_good(u)) / (float(np.max(np.abs(u))) * h2(u)))
    tame_ok = max(tame) <= 1.0 + 1e-9
    u0 = 0.3 * np.sin(x) + 0.2 * np.cos(2 * x)
    eta = 0.5 * np.cos(x) - 0.3 * np.sin(3 * x)

    def ratios(Tf, nt):
        bar = solve(u0, Tf, nt)
        out = []
        for d in (4e-3, 2e-3, 1e-3):
            ud = solve(u0 + d * eta, Tf, nt)
            out.append(max(h2(a - b) for a, b in zip(ud[::10], bar[::10])) / d)
        return out, h2(bar[-1]) / h2(bar[0])
    r, grow = ratios(1.0, 800)
    lip = max(r) < 1.05 * min(r) and grow < 20
    rc, growc = ratios(3.0, 2400)
    ctl = not (max(rc) < 1.05 * min(rc) and growc < 20)
    print("   tame bound |F(u)|_H2 / (|u|_inf |u|_H2) <= %.4f <= 1 on 20 random u: %s" % (max(tame), tame_ok))
    print("   T_b = 1.0: sup_t |u_d - ubar|_H2 / d = %s for d = 4e-3, 2e-3, 1e-3 (equal to 5 %%: %s); |ubar|_H2 grows by "
          "%.2f" % (", ".join("%.4f" % v for v in r), max(r) < 1.05 * min(r), grow))
    print("   control (T = 3.0, past the shock): ratios %s, |ubar|_H2 grows by %.3g (rejected): %s" %
          (", ".join("%.4g" % v for v in rc), growc, ctl))
    return tame_ok and lip and ctl


def main():
    ok2 = k2()
    print('K2', 'PASS' if ok2 else 'FAIL')
    d, n = iterate(F_good)
    ratios = [d[i + 1] / d[i] for i in range(len(d) - 1) if d[i] > 1e-14]
    geo = all(r < 0.5 for r in ratios)
    bounded = max(n) < 1.05 * n[0]
    rng = np.random.default_rng(1)
    lip = True
    for _ in range(20):
        u = sum(rng.normal() * np.cos(m * x + rng.uniform(0, 6)) / (1 + m**2) for m in range(1, 8))
        v = u + 1e-2 * sum(rng.normal() * np.sin(m * x) / (1 + m) for m in range(1, 8))
        lip &= l2(F_good(u) - F_good(v)) <= float(np.max(np.abs(u + v))) * l2(u - v) * (1 + 1e-9)
    print("K1 (numpy) Picard iteration with the non-local source -(1 - d_x^2)^-1 (u^2):")
    print("   sup_t |u^(n+1) - u^n|_L2: %s; ratios %s (< 0.5: %s)" %
          (", ".join("%.2e" % v for v in d), ", ".join("%.3f" % r for r in ratios), geo))
    print("   sup_t |u^n|_H2: %s (bounded within 5 %%: %s); (K2) measured on 20 random pairs: %s" %
          (", ".join("%.4f" % v for v in n), bounded, lip))
    db, nb = iterate(F_bad, nit=6)
    grows = nb[-1] > 20 * nb[0] and nb[-1] > nb[-2] > nb[-3]
    print("   control (F = 0.5 u_xx, not L2-Lipschitz): sup_t |u^n|_H2 = %s: grows without bound (rejected): %s" %
          (", ".join("%.3g" % v for v in nb), grows))
    ok = geo and bounded and lip and grows
    print('K1', 'PASS' if ok else 'FAIL')
    ok = ok and ok2
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
