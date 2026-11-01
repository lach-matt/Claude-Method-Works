#!/usr/bin/env python3
"""e2meas5.py -- e2high5's H3 measurement continued above sigma = 96 (E2-PILOT section 3j, D567).

e2high5 H3 measures ||chi_I R_l(sigma) chi_I|| at sigma in {3, 6, 12, 24, 48, 96}; E2-PILOT section 3j compares the
certified band bound with it there (ratios 9.70 ... 19.0). This continues the measurement to sigma = 128, 160 and 192,
the band's printed points above 96. At each sigma, ltop is the least l with max V_l > sigma^2 (the first harmonic
whose barrier top lies above sigma^2), and the norm is taken over the 13 harmonics l = ltop - 6, ..., ltop + 6 around
it, as H3 does above sigma = 6. The method is e2high5's cutoff_norm (a numerical ODE solve; computed, not certified).

Measured (D567): sigma = 96: max 0.0519376 at l = 191 (ltop 191), sigma times the max 4.986; sigma = 128: max
0.0399913 at l = 255 (ltop 255), sigma times the max 5.1189. Each sigma takes about one to two hours.

    python3 checks/e2meas5.py [SIGMAS]       (default 96,128,160,192)
"""
import sys
import time

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import e2high5 as H  # noqa: E402

SIGMAS = [float(x) for x in (sys.argv[1].split(',') if len(sys.argv) > 1 else ('96', '128', '160', '192'))]


def main():
    t = time.time()
    for s in SIGMAS:
        ltop = next(l for l in range(0, 10 * int(s) + 10) if H.vmax(l) > s * s)
        best = (0.0, None)
        for l in range(max(0, ltop - 6), ltop + 7):
            nrm = H.cutoff_norm(l, s)[0]
            if nrm > best[0]:
                best = (nrm, l)
        print(f'sigma {s:g}: ltop {ltop}, max over l in [{ltop-6}, {ltop+6}] = {best[0]:.6g} at l = {best[1]}; '
              f'sigma*max = {s*best[0]:.5g} ({time.time()-t:.0f} s)', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
