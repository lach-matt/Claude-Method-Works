"""mx2.py -- item 221, chemistry: a linear symmetric MX2 (CuF2: Cu(II), d9) under one law, the symmetric stretch scanned
(coarse 7 x 0.05 A, then fine 7 x 0.02 A about the coarse minimum), lowest converged state over the listed spins and
the default/atom guesses at each point; quartic through the fine points.  UKS PBE0/def2-TZVP, as mol.py.  The free F
atom and the law's Cu atom are banked separately (atoms_law.py; F here).
usage: python3 mx2.py M X r0 spins LAWNAME delta_eV  -> JSON"""
import sys, json, time
import numpy as np
from pyscf import gto, dft
import law
HA = 27.211386245988
M, X, r0 = sys.argv[1], sys.argv[2], float(sys.argv[3])
spins, name, d = [int(s) for s in sys.argv[4].split(",")], sys.argv[5], float(sys.argv[6])
t = time.time()

def solve(r, spin):
    best = None
    for g in ("minao", "atom"):
        try:
            mol = gto.M(atom="%s 0 0 0; %s 0 0 %.6f; %s 0 0 %.6f" % (M, X, r, X, -r), basis="def2-tzvp", spin=spin, verbose=0)
            mf = dft.UKS(mol); mf.xc = "pbe0"; mf.max_cycle = 200; mf.init_guess = g
            if d: law.apply_law(mf, [(0, 2, d / HA, 10.0)])
            e = mf.kernel()
            if not mf.converged:
                mf2 = dft.UKS(mol); mf2.xc = "pbe0"; mf2.max_cycle = 300; mf2.damp = 0.5
                if d: law.apply_law(mf2, [(0, 2, d / HA, 10.0)])
                e = mf2.kernel(mf.make_rdm1()); mf = mf2
            if mf.converged and (best is None or e < best[0]):
                best = (float(e), round(law.lowdin_shell_pop(mf, 0, 2), 4))
        except Exception:
            pass
    return best

def point(r):
    b = [(s,) + x for s in spins for x in [solve(r, s)] if x]
    if not b: return None
    s, e, nd = min(b, key=lambda x: x[1])
    return (round(r, 4), e, s, nd)

coarse = [p for p in (point(r0 + 0.05 * (i - 3)) for i in range(7)) if p]
rc = min(coarse, key=lambda p: p[1])[0]
fine = [p for p in (point(rc + 0.02 * (i - 3)) for i in range(7)) if p]
xs = [p[0] for p in fine]; ys = [p[1] for p in fine]
c = np.polyfit(xs, ys, 4); d1 = np.polyder(c); d2 = np.polyder(c, 2)
rts = [x.real for x in np.roots(d1) if abs(x.imag) < 1e-9 and np.polyval(d2, x.real) > 0]
re = min(rts, key=lambda x: abs(x - xs[int(np.argmin(ys))]))
mol = gto.M(atom="F 0 0 0", basis="def2-tzvp", spin=1, verbose=0); mf = dft.UKS(mol); mf.xc = "pbe0"; eF = float(mf.kernel())
o = dict(mol=M + X + "2", law=name, delta_eV=d, re=round(float(re), 4), Emin=float(np.polyval(c, re)), E_F_atom=eF,
         fit_resid_meV=round(float(max(abs(np.polyval(c, x) - y) for x, y in zip(xs, ys))) * HA * 1000, 3),
         coarse=coarse, fine=fine, sec=int(time.time() - t))
print("RESULT " + json.dumps(o), flush=True)
