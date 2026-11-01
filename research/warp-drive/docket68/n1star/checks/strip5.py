#!/usr/bin/env python3
"""strip5: a source confined to a strip of bounded v along N enters at rho^3, not rho^2 (BEYOND5 3(b), D464).

D461 found that the sources from e = g_lambda - g_app are of order r^-4 where the record bounds e (sources5.py Q6),
and concluded that D413's condition fails for them. Verifier 198 found that e is bounded only on P', which has
v <= V'_P (N1STAR-PROOF.md, the region's definition), while I_0 lies at v -> infinity: those sources sit in a strip
of bounded v along N. This is the scalar l = 0 model of the difference (the verifier's script, made a check): on
4 + 1 Minkowski, box phi = S with zero data on N = {v = 0} and nothing incoming, psi = r^(3/2) phi,
-4 psi_uv - (3/4) psi/r^2 = r^(3/2) S, the diamond scheme on a geometric u-grid from -10^5 to -1, and r^2 phi read on
t = 0 (u = -r, v = r) as r grows.

  T1 (computed) S = r^-4 on all of v >= 0: r^2 phi -> -1/2 (within 2e-3 at r = 100-400), the shift G(1) = -f/2 of
     BEYOND5's l = 0 example: an r^-4 source reaches the rho^2 coefficient.
  T2 (computed) S = r^-4 on the strip v in [0, 1] only: r * r^2 phi tends to a constant, about -0.78 (changing by under
     1 % from r = 200 to 400), so r^2 phi falls like 1/r: the strip's source enters at rho^3, not rho^2.
  T3 (computed) control: halving dv and doubling the u-grid moves r^2 phi at r = 100 by under 1e-3 in both cases.

So the sources from e, which live in such a strip, do not reach the r^-2 coefficient at I_0 in this model. Not
computed: the strip for the record's full operator, and whether its r^-3 term, which carries no structure, is
compatible with Lemma 0.1's rho^3 C^infinity.

Run: python3 checks/strip5.py   (about 30 s)
"""
import sys

import numpy as np


def run(strip, d=1.0, V=420.0, dv=0.02, U=1e5, n=6000, targets=(25, 50, 100, 200, 400)):
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
        F = -0.25 * (r**1.5 * S + 0.75 * pc / r**2)
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
    ok["T3"] = abs(h2[100] - h[100]) < 1e-3 and abs(s2[100] - s[100]) < 1e-3
    print("  control at r = 100, dv/2 and 2n: %.5f against %.5f; %.5f against %.5f"
          % (h2[100], h[100], s2[100], s[100]))
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
