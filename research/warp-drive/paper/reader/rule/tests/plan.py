#!/usr/bin/env python3
"""Cost model and Zeno-segmented production plan for the rule of P-APPC2 (report I-RULE, the plan).
usage: plan.py CP80 CP160 CI80 CI160 SETUP [BYTES_PER_INT]
  CPm: cpu microseconds per node per evaluation of P (320-bit) at M = 80, 160; CIm: per node per inner sweep (binary64);
  SETUP: cpu microseconds per node of a cell's setup (seed, X(J_s), B) and its finishing (edges, element values).
  The model is linear in M + 1 for each part, as measured."""
import sys, math
cp80, cp160, ci80, ci160, setup = (float(a) for a in sys.argv[1:6]); bpi = float(sys.argv[6]) if len(sys.argv) > 6 else 40.5
lin = lambda a80, a160: (lambda M: a80 + (a160 - a80) * (M - 80) / 80.0)
cP, cI = lin(cp80, cp160), lin(ci80, ci160)
def cell_core_s(px, pv, M, No, Ni):
    n = (px + 1) * (pv + 1) * (M + 1)
    return n * (No * cP(M) + No * Ni * cI(M) + setup) * 1e-6
def xi(u): y = (u + 1) / 0.002; return math.copysign(math.log(abs(y) + math.sqrt(y * y + 1)), y)
def u_of(x): return 0.002 * math.sinh(x) - 1
XI0 = xi(-10)
for M in (80, 160, 176, 184, 192, 200, 320, 328):
    print('M %3d: c_P %.0f us, c_I %.1f us per node' % (M, cP(M), cI(M)))

def plan(title, cases, cores, eff, speed=1.0):
    print('\n' + title)
    for name, xie, nc, nr, px, pv, segs, NoNi, NtNs, nel, p in cases:
        w = (xie - XI0) / nc; tot = 0; hand = 0
        print('  %s: %d x %d cells, (p_xi, p_v) = (%d, %d), (N_o, N_i) = %s, (N_t, N_s) = %s, p = %d' % (name, nc, nr, px, pv, NoNi, NtNs, p))
        print('    seg  columns  u range              M   cells  core-h    wall-h   hand-off MB (compact; canonical text)')
        for k, (a, b, M) in enumerate(segs):
            ch = (b - a) * nr * cell_core_s(px, pv, M, NoNi[0], NoNi[1]) / 3600 / speed
            ints = 4 * nr * (pv + 1) * (M + 1); tot += ch; hand += ints * bpi
            print('    %2d   [%2d,%2d)  [%7.3f, %7.3f]  %3d  %4d   %7.1f   %6.1f   %5.1f; %5.1f'
                  % (k, a, b, u_of(XI0 + a * w), u_of(XI0 + b * w), M, (b - a) * nr, ch, ch / (cores * eff), ints * bpi / 1e6, ints * 95 / 1e6))
        Me = max(m for _, _, m in segs); ev = nel * (NtNs[0] + 1) * (NtNs[1] + 1) * (Me + 1) * 5 * bpi
        print('    total %.0f core-h; %.1f days at %d cores (%.0f%% efficiency); hand-offs %.0f MB in all; element values %.2f GB in all'
              % (tot, tot / (cores * eff) / 24, cores, 100 * eff, hand / 1e6, ev / 1e9))

zeno32 = lambda M: [(0, 16, M), (16, 24, M), (24, 28, M), (28, 30, M), (30, 31, M), (31, 32, M)]
zeno64 = lambda M1, M2=None: [(0, 32, M1), (32, 48, M1), (48, 56, M2 or M1), (56, 60, M2 or M1), (60, 62, M2 or M1), (62, 63, M2 or M1), (63, 64, M2 or M1)]
# P-APPC2's provisional parameters (sized for G0h)
prov = [('(1, D_A)', -3421 / 500, 32, 30, 26, 39, zeno32(184), (9, 25), (104, 136), 4, 56),
        ('(2, D*)', -4473 / 1000, 64, 30, 28, 42, zeno64(184), (10, 25), (152, 184), 4, 61),
        ('(1, D*)', -4517 / 1000, 64, 30, 30, 45, zeno64(200, 328), (10, 25), (136, 200), 6, 64)]
plan('P-APPC2 provisional parameters, this machine (3 free cores):', prov, 3, 0.9)
# resized to the G0i targets (S-RULE §1's conversion, accuracy three decades below the quantum, §4's rates)
g0i = [('(1, D_A)', -3421 / 500, 32, 30, 24, 36, zeno32(176), (8, 25), (104, 136), 4, 54),
       ('(2, D*)', -4473 / 1000, 64, 30, 26, 39, zeno64(176), (8, 25), (152, 184), 4, 58),
       ('(1, D*)', -4517 / 1000, 64, 30, 28, 42, zeno64(192, 320), (9, 25), (136, 200), 6, 62)]
plan('Resized to the G0i targets, this machine (3 free cores):', g0i, 3, 0.9)
for cores in (32, 64):
    plan('P-APPC2 provisional parameters, %d cores at 1.5x this machine per core:' % cores, prov, cores, 0.9, 1.5)
