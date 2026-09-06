#!/usr/bin/env python3
"""deriv85.py -- s85 · ITEM 1 · DERIVATION CHECK, SYNTHETIC ONLY.

**THIS IS NOT A MEASUREMENT AND TOUCHES NO ATOMIC FIELD.**  It checks the algebra of
the reduction below on model charge functions before any prediction is filed.  Declared
as a derivation aid (SEARCH BEFORE DERIVING, §E.5).

THE REDUCTION.  In u = 1/r, with S(u) := u*Q(u) = q(r)/r = -V(r):

    f(u) = 2E + 2S(u) - L^2 u^2 ,      I = int_{u1}^{u2} du / sqrt(f)

Let g(u) := L^2 (u-u1)(u2-u) be the UNIQUE constant-charge parabola with the SAME two
turning points.  int du/sqrt(g) = pi/L exactly -- that is s84's anchor.  Then, using
f(u1) = f(u2) = 0 to eliminate E,

    f(u) - g(u) = 2 [ S(u) - CHORD(u) ]        CHORD = the secant of S on [u1,u2]

so with u = u1 + a t, a = u2 - u1, and

    delta(t) := 2 [ CHORD - S ] / (L^2 a^2)   >= 0  iff S is CONVEX in u

    J = (1/pi) int_0^1 dt / sqrt( t(1-t) - delta(t) )

and with kappa := sup_t delta(t)/(t(1-t)):

    J <= 1/sqrt(1-kappa)  ==>  kappa < 3/4  IMPLIES  J < 2  IMPLIES  G-within.

S''(u) = r^3 q''(r), so S convex <=> q'' >= 0 <=> the radial density 4 pi r^2 rho is
falling.  With w(r) := S'(u) = q - r q', the Green's function for -d^2/du^2 gives

    kappa <= K := 2 [ w(r_in) - w(r_out) ] / ( L^2 (1/r_in - 1/r_out) )   -- turning
points only.  kappa <= 1 always, and kappa -> 1 is the region SPLITTING: collapse.
"""
import math
import numpy as np

GLX, GLW = np.polynomial.legendre.leggauss(400)


def regions(f, ulo, uhi, n=40000):
    us = np.exp(np.linspace(math.log(ulo), math.log(uhi), n))
    fs = f(us); pos = fs > 0
    if not pos.any():
        return []
    def bis(a, b):
        for _ in range(200):
            m = math.sqrt(a * b)
            if f(np.array([m]))[0] > 0: b = m
            else: a = m
        return math.sqrt(a * b)
    out, i = [], 0
    while i < n:
        if not pos[i]: i += 1; continue
        j = i
        while j + 1 < n and pos[j + 1]: j += 1
        if i == 0 or j == n - 1: return None
        out.append((bis(us[i-1], us[i]), bis(us[j+1], us[j]))); i = j + 1
    return out


def quad(f, u1, u2):
    th = 0.25 * math.pi * (GLX + 1.0)
    u = u1 + (u2 - u1) * np.sin(th) ** 2
    val = f(u)
    jac = 2.0 * (u2 - u1) * np.sin(th) * np.cos(th)
    return float(0.25 * math.pi * np.sum(GLW * np.where(
        val > 0, jac / np.sqrt(np.maximum(val, 1e-300)), 0.0)))


def analyse(E, l, Q):
    """Q(u) = enclosed charge as a function of u = 1/r.  Returns J, kappa, K, sanity."""
    L = l + 0.5
    S = lambda u: u * Q(u)
    f = lambda u: 2.0 * E + 2.0 * S(u) - L * L * u * u
    qmax = float(np.atleast_1d(Q(np.array([1e7])))[0])
    regs = regions(f, 1e-8, 4.0 * (qmax + 1.0) / (L * L))
    if not regs:
        return None
    u1, u2 = regs[0]
    a = u2 - u1
    J = (L / math.pi) * quad(f, u1, u2)

    # delta(t) and kappa, on a t-grid clustered at both endpoints
    th = np.linspace(1e-6, math.pi - 1e-6, 4001)
    t = 0.5 * (1 - np.cos(th))
    u = u1 + a * t
    S1, S2 = float(S(np.array([u1]))[0]), float(S(np.array([u2]))[0])
    chord = S1 + (S2 - S1) * t
    delta = 2.0 * (chord - S(u)) / (L * L * a * a)
    ratio = delta / (t * (1 - t))
    kappa = float(np.max(ratio))

    # the SAME thing read off f directly: kappa = sup (1 - f/g)
    g = L * L * (u - u1) * (u2 - u)
    kappa_f = float(np.max(1.0 - f(u) / np.maximum(g, 1e-300)))

    # K, from the two turning points only.  w = q - r q' = S'(u), by finite difference.
    def Sp(uu):
        h = 1e-6 * max(uu, 1.0)
        return float((S(np.array([uu + h]))[0] - S(np.array([uu - h]))[0]) / (2 * h))
    K = 2.0 * (Sp(u2) - Sp(u1)) / (L * L * a)
    return dict(J=J, kappa=kappa, kappa_f=kappa_f, K=K, u1=u1, u2=u2,
                r_out=1.0 / u1, r_in=1.0 / u2, n_reg=len(regs),
                bound=(1.0 / math.sqrt(1 - kappa)) if kappa < 1 else float('inf'))


def main():
    print("=== D1 · THE ANCHOR: constant q gives kappa = 0 and J = 1 ===============")
    worst_k = worst_j = 0.0
    for q0 in (1.0, 7.0, 90.0):
        for l in (0, 1, 2, 3):
            for E in (-0.05, -0.5):
                R = analyse(E, l, lambda u, c=q0: np.full_like(u, c))
                if R is None: continue
                worst_k = max(worst_k, abs(R['kappa']))
                worst_j = max(worst_j, abs(R['J'] - 1))
    print(f"  max |kappa| = {worst_k:.3e}   max |J-1| = {worst_j:.3e}")

    print("\n=== D2 · THE REDUCTION: J vs 1/sqrt(1-kappa), screened models ===========")
    print("  model q(r) = 1 + (Z-1) exp(-r/d)   [SYNTHETIC -- not an atom]")
    print("   Z    d    l      J      kappa   1/sqrt(1-k)   K(turn-pt)  holds?")
    bad = 0
    for Z, d in ((20, 0.35), (57, 0.30), (90, 0.28)):
        for l in (0, 1, 2, 3):
            Q = lambda u, Z=Z, d=d: 1.0 + (Z - 1.0) * np.exp(-1.0 / (u * d))
            R = analyse(-0.20, l, Q)
            if R is None:
                print(f"  {Z:3d} {d:5.2f} {l:2d}    -- no allowed region")
                continue
            ok = R['J'] <= R['bound'] + 1e-9
            bad += (not ok)
            print(f"  {Z:3d} {d:5.2f} {l:2d}  {R['J']:7.4f}  {R['kappa']:7.4f}  "
                  f"{R['bound']:9.4f}   {R['K']:9.4f}    {'yes' if ok else '**NO**'}")
    print(f"  theorem J <= 1/sqrt(1-kappa) violated in {bad} case(s)")

    print("\n=== D3 · kappa AND f READ THE SAME NUMBER ===============================")
    Q = lambda u: 1.0 + 89.0 * np.exp(-1.0 / (u * 0.28))
    R = analyse(-0.20, 3, Q)
    print(f"  kappa from S-chord {R['kappa']:.9f}   kappa from 1-f/g {R['kappa_f']:.9f}"
          f"   diff {abs(R['kappa']-R['kappa_f']):.2e}")

    print("\n=== D4 · kappa -> 1 IS THE REGION SPLITTING (collapse) ==================")
    for d in (0.28, 0.20, 0.15, 0.126, 0.125, 0.124):
        Q = lambda u, d=d: 1.0 + 89.0 * np.exp(-1.0 / (u * d))
        R = analyse(-0.20, 3, Q)
        print(f"  d={d:.3f}  kappa={R['kappa']:.5f}  J={R['J']:.4f}  "
              f"regions={R['n_reg']}")


if __name__ == '__main__':
    main()
