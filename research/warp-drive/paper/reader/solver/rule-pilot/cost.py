# reader's cost model (S-RULE §6): per-node cost c(M) = c0 + cx (M + 1) microseconds on one core of this machine,
# fitted to the pilot: M = 80: 160-200 us (load-dependent; 180 used), M = 160: 238 us (16.30 s / 68,425 nodes)
c80, c160 = 180.0, 16.30 / 68425 * 1e6
cx = (c160 - c80) / 80; c0 = c80 - 81 * cx
print('c0 = %.0f us, cx = %.3f us per x-node; c(160) = %.0f us' % (c0, cx, c160))
cases = [  # name, cells, (pxi, pv), M, NP
  ('seed 1, D_A', 30 * 30, (26, 39), 192, 64),
  ('seed 2, D_A', 30 * 30, (26, 39), 176, 64),
  ('seed 1, D*', 60 * 30, (30, 45), 336, 80),
  ('seed 2, D*', 60 * 30, (28, 42), 192, 80),
]
for name, cells, (px, pv), M, NP in cases:
    nodes = (px + 1) * (pv + 1) * (M + 1); c = c0 + cx * (M + 1)
    sweep = nodes * c * 1e-6; cell = sweep * NP; tot = cell * cells / 3600
    print('%-12s nodes/cell %7d  c(M) %3.0f us  sweep %6.1f s  cell %6.0f s  total %6.0f core-h  | 32 cores x1.5: %5.0f h | 4 cores (this machine): %4.0f days'
          % (name, nodes, c, sweep, cell, tot, tot / 48, tot / 4 / 24))
