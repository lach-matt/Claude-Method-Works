#!/usr/bin/env python3
"""szrun5.py -- runs of dnsolve5.py (or dnsolve5v.py, the swapped gauge) stopped at v = vend, for CERTIFY-10L5-RESULT.md.

dnsolve5.py --run always marches to v = 4.5. The questions of CERTIFY-10L5-RESULT.md section 1 (the second zero of the
expansion) live before v = 2, so this driver builds dnsolve5's own Grid with the same u-grid (-10 to -rcut, logarithmic
in |1 + u|, a = 0.002) and the same v-step (4.5/Nv), but stops at vend; the solver is dnsolve5.run itself, unchanged.

    python3 checks/szrun5.py lam rcut M Nu Nv vend out.npz [ld k] [amp A] [gauge v] [R0 r]

Nu, Nv are the full-run grid numbers (Nv for v up to 4.5), so a run here is the first round(Nv vend/4.5) columns of
the corresponding dnsolve5.py --run.  R0 (default 10, dnsolve5's) moves the outer cone u = -R0 that carries the
wave's data (dnsolve5 places the leading Bondi term there, m = y^3 G/2, n = y^3 F/2), for the truncation test of
CERTIFY-10L5-RESULT.md section 1. Labels: computed (floating point). No check of its own: the solver's selftest is
dnsolve5.py's S1-S5 (dnsolve5v.py's V1-V4 for the swapped gauge).
"""
import os, sys, time, importlib.util
import numpy as np

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


def safe(E):
    """a cell whose 4 x 4 solve is singular (near the singularity, at a small cut) is returned as NaN, so that dnsolve5.run
    masks it as it masks any non-finite cell, instead of stopping the run (np.linalg.solve raises on the whole batch)"""
    raw = E.uv

    def uv(env):
        try:
            return raw(env)
        except np.linalg.LinAlgError:
            shape = np.shape(env['R'])
            vals = [np.broadcast_to(np.asarray(v_, dtype=float), shape) for v_ in E.fm(*[env[k] for k in E.names])]
            rhs = np.stack(vals[:4], -1).reshape(-1, 4)
            Mx = np.stack(vals[4:], -1).reshape(-1, 4, 4)
            out = np.full_like(rhs, np.nan)
            for q in range(len(rhs)):
                try:
                    out[q] = np.linalg.solve(Mx[q], rhs[q])
                except np.linalg.LinAlgError:
                    pass
            return out.reshape(shape + (4,))
    E.uv = uv


def main():
    a = sys.argv[1:]
    lam, rcut, M, Nu, Nv, vend, out = float(a[0]), float(a[1]), int(a[2]), int(a[3]), int(a[4]), float(a[5]), a[6]
    opts = a[7:]
    ld = int(opts[opts.index('ld') + 1]) if 'ld' in opts else 0
    amp = float(opts[opts.index('amp') + 1]) if 'amp' in opts else 1.0
    gauge = opts[opts.index('gauge') + 1] if 'gauge' in opts else 'u'
    R0 = float(opts[opts.index('R0') + 1]) if 'R0' in opts else 10.0
    d5 = load('dnsolve5')
    nv = int(round(Nv * vend / 4.5))
    vend = 4.5 * nv / Nv
    t0 = time.time()
    if gauge == 'u':
        E = d5.Eqs()
        safe(E)
        G = d5.Grid(M, -R0, -rcut, Nu, 0.0, vend, nv, a=0.002, ld=ld)
        A, mask = d5.run(E, G, d5.Data(lam, amp), rcut)
        flds = d5.ALL
    else:
        d5v = load('dnsolve5v')
        E = d5v.Eqs()
        safe(E)
        G = d5.Grid(M, -R0, -rcut, Nu, 0.0, vend, nv, a=0.002, ld=ld)
        A, mask = d5v.run(E, G, d5.Data(lam, amp), rcut)
        flds = d5v.ALLV
    np.savez_compressed(out, mask=mask, u=G.u, v=G.v, x=G.x, xmap=0.0, lam=lam, rcut=rcut, amp=amp, gauge=gauge, R0=R0,
                        **{f: A[f] for f in flds})
    print('written', out, 'cells', int((~mask).sum()), 'of', mask.size, '%.0f s' % (time.time() - t0), flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
