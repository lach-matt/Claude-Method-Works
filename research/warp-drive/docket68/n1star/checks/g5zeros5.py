#!/usr/bin/env python3
"""g5zeros5.py -- growth5.py's own run, with every zero of the round spheres' expansion recorded, written to a scratch
file instead of data/ (growth5.py --run writes a part file into data/; the pinned standard runs of 2026-10-20 predate
the zero record, D45).  The solver is growth5.run itself, unchanged.  Labels: computed (floating point).

    python3 checks/g5zeros5.py L lam Ny Nx v_end out.json [cfl c]

growth5's step is fixed by the radial grid alone (growth5.fixed_step: dv = min(lam/8, CFL dy/speed), CFL = 2); at
Nx = 24 and 32 that step is unstable in angle on the seed itself, before the wave arrives (CERTIFY-10L5-RESULT.md
section 1), so `cfl c` replaces growth5.CFL for the angular refinement runs (the scheme is otherwise unchanged).
"""
import os, sys, json
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
import growth5 as G                                                             # noqa: E402


def main():
    L, lam, Ny, Nx, v_end, out = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), \
        float(sys.argv[5]), sys.argv[6]
    if 'cfl' in sys.argv:
        G.CFL = float(sys.argv[sys.argv.index('cfl') + 1])
    rec = G.run(L, lam, Ny, Nx, 0.0, v_end, log=lambda *a: print(*a, flush=True))
    rec['cfl'] = G.CFL
    rec['samples'] = []
    json.dump(rec, open(out, 'w'))
    print('wrote', out, rec['seconds'], 's; breakdown', G.breakdown(rec), flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
