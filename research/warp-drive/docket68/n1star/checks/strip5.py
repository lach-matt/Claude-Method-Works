#!/usr/bin/env python3
"""strip5: a source confined to a strip of bounded v along N enters at rho^3, not rho^2 (BEYOND5 3(b), D464, D474).

D461 found that the sources from e = g_lambda - g_app are of order r^-4 where the record bounds e (sources5.py Q6),
and concluded that D413's condition fails for them. Verifier 198 found that e is bounded only on P', which has
v <= V'_P (N1STAR-PROOF.md, the region's definition), while I_0 lies at v -> infinity: those sources sit in a strip
of bounded v along N. This is the scalar l = 0 model of the difference (the verifier's script, made a check): on
4 + 1 Minkowski, box phi = S with zero data on N = {v = 0} and nothing incoming, psi = r^(3/2) phi,
-4 psi_uv - (3/4) psi/r^2 = r^(3/2) S, the diamond scheme on a geometric u-grid from -10^5 to -1, and r^2 phi read on
t = 0 (u = -r, v = r) as r grows.

  T1 (computed) S = r^-4 on all of v >= 0: r^2 phi -> -1/2 (within 2e-3 at r = 100-400), the shift G(1) = -f/2 of
     BEYOND5's l = 0 example: an r^-4 source reaches the rho^2 coefficient.
  T2 (computed) S = r^-4 on the strip v in [0, 1] only: r * r^2 phi tends to a constant, -0.784 at r = 400 and still
     drifting (changing by under 1 % from r = 200 to 400; about -0.785 by A + B/r, verifier 199; exactly -pi/4, verifier
     202), so r^2 phi falls like 1/r: the strip's source enters at rho^3, not rho^2.
  T3 (computed) control: halving dv and doubling the u-grid moves r^2 phi at r = 100 by under 1e-3 on all of v >= 0, and
     the strip's value by under 2e-3 relative (4e-4 measured; verifier 199 found the old absolute 1e-3 too weak).
  T4 (computed) the harmonics l = 1, ..., 4, with the potential (l(l + 2) + 3/4)/r^2 in place of 3/4 (D474): on all of v
     >= 0, r^2 phi again tends to a non-zero constant (-1/3, -1/6, -1/15, -1/30 to four digits; within 1 % from r = 200
     to 400); on the strip, r * r^2 phi does not grow from r = 200 to 400 (to 2 %) and r^2 phi is under 2 % of the full
     source's at r = 400. At l = 1 and 3 r * r^2 phi tends to -1/3 and 1/15, so the strip enters at rho^3 as at l = 0; at
     l = 2 and 4 it falls like 1/r, its rho^3 coefficient below the scheme's resolution (halving dv and doubling the
     u-grid moves it by up to 8 % at r = 200), so there the strip enters at rho^3 or later (exactly rho^4: T5). In no
     harmonic computed does it reach rho^2. For l >= 1 the kernel changes sign, so these are values for S = r^-4 Y_l, not
     a bound over |S| <= r^-4 (verifier 199).

  T5 (computed against exact) verifier 202's values from the Riemann function P_(l+1/2) of this operator: the full source
     gives r^2 phi -> -1/2, -1/3, -1/6, -1/15, -1/30 (l = 0-4), and the strip r * r^2 phi -> C_l = -pi/(4 Gamma(1 - l/2)
     Gamma(2 + l/2)), so -pi/4, -1/3, 0, 1/15, 0: zero at every even l >= 2, where the strip enters at rho^4 (-1/6 and
     1/10 at l = 2, 4, by the verifier's quadrature). The scheme reproduces the full-source values to 1e-3 and C_l to 1 %
     (and |r * r^2 phi| < 2e-3 where C_l = 0) at r = 400. The closed form suggests the strip reaches rho^2 at no l (the
     verifier's leading-order expansion, not a bound).

So the sources from e, which live in such a strip, do not reach the r^-2 coefficient at I_0 in this model; as the
l = 0 kernel is positive, it bounds every |S| <= r^-4 on the strip, at l = 0 only (verifier 199). Not
computed: the strip for the record's full operator, and whether its r^-3 term, which carries no structure, is
compatible with Lemma 0.1's rho^3 C^infinity.

Run: python3 checks/strip5.py   (about a minute)
"""
import sys

import numpy as np


def run(strip, d=1.0, V=420.0, dv=0.02, U=1e5, n=6000, targets=(25, 50, 100, 200, 400), l=0):
    u = -np.geomspace(U, 1.0, n)
    du = np.diff(u)
    psi = np.zeros(n)
    out = {}
    v = 0.0
    while v < V:
        vm = v + dv / 2
        um = (u[:-1] + u[1:]) / 2
        r = (vm - um) / 2
        S = r**-4.0 * ((vm <= d) if strip else 1.0)
        pc = (psi[:-1] + psi[1:]) / 2
        F = -0.25 * (r**1.5 * S + (l * (l + 2) + 0.75) * pc / r**2)
        D = np.diff(psi) + du * dv * F
        psi = np.concatenate([[0.0], np.cumsum(D)])
        v += dv
        for R in targets:
            if R not in out and v >= R:
                i = np.argmin(abs(u + R))
                rr = (v - u[i]) / 2
                out[R] = rr**0.5 * psi[i]          # r^2 phi
    return out


def main():
    ok = {}
    h = run(False)
    s = run(True)
    print("  r^2 phi, source on all of v >= 0: %s" % ", ".join("r = %d: %.5f" % (k, v) for k, v in h.items()))
    print("  r * r^2 phi, source on the strip v in [0, 1]: %s" % ", ".join("r = %d: %.4f" % (k, k * v)
                                                                         for k, v in s.items()))
    ok["T1"] = all(abs(h[R] + 0.5) < 2e-3 for R in (100, 200, 400))
    ok["T2"] = abs(400 * s[400] / (200 * s[200]) - 1) < 0.01 and abs(s[400]) < 0.01 * abs(h[400])
    h2 = run(False, dv=0.01, n=12000, V=110.0, targets=(100,))
    s2 = run(True, dv=0.01, n=12000, V=110.0, targets=(100,))
    rel = abs(s2[100] / s[100] - 1)
    ok["T3"] = abs(h2[100] - h[100]) < 1e-3 and rel < 2e-3
    print("  control at r = 100, dv/2 and 2n: %.5f against %.5f; strip %.6f against %.6f (relative %.1e)"
          % (h2[100], h[100], s2[100], s[100], rel))
    t4 = True
    T4V = {}
    for l in (1, 2, 3, 4):
        hl = run(False, l=l, targets=(100, 200, 400))
        sl = run(True, l=l, targets=(100, 200, 400))
        conv_h = abs(hl[400] / hl[200] - 1) < 0.01 and abs(hl[400]) > 1e-3
        conv_s = abs(400 * sl[400]) <= 1.02 * abs(200 * sl[200]) and abs(sl[400]) < 0.02 * abs(hl[400])
        t4 &= conv_h and conv_s
        T4V[l] = (hl[400], sl[400])
        print("  l = %d: r^2 phi on all of v >= 0: %s; r * r^2 phi on the strip: %s"
              % (l, ", ".join("r = %d: %.5f" % (k, v) for k, v in hl.items()),
                 ", ".join("r = %d: %.4f" % (k, k * v) for k, v in sl.items())), flush=True)
    ok["T4"] = t4
    # T5: verifier 202's exact values from the Riemann function: the full source gives r^2 phi -> G_l, the strip
    # r * r^2 phi -> C_l = -pi/(4 Gamma(1 - l/2) Gamma(2 + l/2)), zero at every even l >= 2 (1/Gamma's poles)
    import mpmath
    G = {0: -0.5, 1: -1 / 3, 2: -1 / 6, 3: -1 / 15, 4: -1 / 30}
    t5 = True
    for l in range(5):
        Cl = float(-mpmath.pi / 4 * mpmath.rgamma(1 - mpmath.mpf(l) / 2) * mpmath.rgamma(2 + mpmath.mpf(l) / 2))
        hv = h[400] if l == 0 else T4V[l][0]
        sv = 400 * (s[400] if l == 0 else T4V[l][1])
        good = abs(hv / G[l] - 1) < 1e-3 and (abs(sv - Cl) < 0.01 * abs(Cl) if Cl != 0 else abs(sv) < 2e-3)
        t5 &= good
        print("  l = %d: r^2 phi %.5f against %.5f; strip r * r^2 phi %.4f against C_l = %.5f" % (l, hv, G[l], sv, Cl))
    ok["T5"] = t5
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
