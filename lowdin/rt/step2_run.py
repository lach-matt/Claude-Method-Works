#!/usr/bin/env python3
"""step2_run.py -- Session 5. Regenerate the `computed` grade from TFD, parameter-free.
Cells: every distinct (Z, charge, l) among COORDINATES-2_13 rows of grade `computed`.
Output: out/Z{Z:03d}.tsv per Z (checkpoint), columns Z charge l n_used E delta_tfd.
Kernel = tfd.py / rad.py with tolerances relaxed where gate2 was shown unchanged
(rtol 1e-7, 40 shooting iters; npts 3000): gate 0.1427/-0.0103 vs 0.1428/-0.0104.
n_used = n0+4, n0 = lowest n with that l unfilled under Madelung filling of N=Z-charge
core electrons (matches gate.py core_n 39/39; delta insensitive to offset, rms 0.141-0.146
over n0+2..n0+6). charge == Z (bare nucleus): delta = 0 exactly, no solve.
Resumable: skips Z whose file exists and is complete.
"""
import csv, os, sys, time, numpy as np, tfd
from scipy.integrate import solve_ivp
from rad import _shoot as _pyshoot
# C Numerov kernel (shoot.c) = rad._shoot + early stop in the forbidden region where h^2 q/12 > 0.9
# (spurious nodes at deep E for zeta >= 9: Session 4 fault (ii) recurring). Gate rerun below. Fallback: Python.
try:
    import ctypes, os as _os
    _lib = ctypes.CDLL(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'libshoot.so'))
    _lib.shoot.restype = ctypes.c_int
    _lib.shoot.argtypes = [np.ctypeslib.ndpointer(np.float64, flags='C'), ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
    def _shoot(q, h, l):
        y = ctypes.c_double(); nd = _lib.shoot(np.ascontiguousarray(q, dtype=np.float64), len(q), h, l, ctypes.byref(y))
        return np.array([y.value]), nd
    KERNEL = 'C'
except OSError:
    def _shoot(q, h, l):
        n = len(q); f = 1 - h*h*q/12.0; y0 = 1e-30; y1 = y0*np.exp((l+0.5)*h); nodes = 0
        for i in range(1, n-1):
            y2 = ((12 - 10*f[i])*y1 - f[i-1]*y0)/f[i+1]
            if (y2 < 0) != (y1 < 0) and y1 != 0: nodes += 1
            if abs(y2) > 1e100: y1 /= 1e100; y2 /= 1e100
            y0, y1 = y1, y2
            if q[i+1] > 0 and f[i+1] < 0.1: break
        return np.array([y1]), nodes
    KERNEL = 'py'

# --- relaxed kernel (gate-checked) ---
def _integrate(slope, beta, xmax=60.0):
    x0 = 1e-6; y0 = [1 + slope*x0 + (4/3)*x0**1.5, slope + 2*x0**0.5]
    def f(x, y):
        p = max(y[0], 0.0); return [y[1], x*(np.sqrt(p/x) + beta)**3]
    def hit(x, y): return y[0] - beta*beta*x/16.0
    hit.terminal = True; hit.direction = -1
    return solve_ivp(f, (x0, xmax), y0, events=hit, rtol=1e-7, atol=1e-10,
                     dense_output=True, max_step=0.2)
def tfd_ion(Z, N):
    q = Z - N; beta = 0.21178*Z**(-2/3); target = q/Z; lo, hi = -40.0, -1.2
    for _ in range(40):
        s = 0.5*(lo+hi); sol = _integrate(s, beta)
        if sol.status == 1:
            x0 = sol.t_events[0][0]; ph, dph = sol.y_events[0][0]; g = ph - x0*dph
            if g > target: lo = s
            else: hi = s
        else: hi = s
    sol = _integrate(s, beta); x0 = sol.t_events[0][0]
    return sol, x0, beta
tfd._integrate, tfd.tfd_ion = _integrate, tfd_ion

def eigen(V, l, n, zeta, Z, npts=3000, tol=1e-9):
    rmin, rmax = 1e-5/Z, max(80.0, 4.0*n*n/zeta)
    x = np.linspace(np.log(rmin), np.log(rmax), npts); h = x[1]-x[0]; r = np.exp(x)
    base = (l+0.5)**2 + 2*r*r*V(r); target = n-l-1; Elo, Ehi = -0.6*zeta*zeta, -1e-9
    for _ in range(200):
        E = 0.5*(Elo+Ehi); y, nd = _shoot(base - 2*r*r*E, h, l)
        if nd > target or (nd == target and y[-1]*(-1)**target < 0): Ehi = E
        else: Elo = E
        if Ehi - Elo < tol*abs(E) + 1e-13: break
    return 0.5*(Elo+Ehi)

# --- n0 rule ---
_ORDER = sorted([(n, l) for n in range(1, 12) for l in range(n)], key=lambda t: (t[0]+t[1], t[0]))
def n0(N, l):
    rem = N; ns = []
    for n, ll in _ORDER:
        if rem <= 0: break
        k = min(rem, 2*(2*ll+1)); rem -= k
        if ll == l and k > 0: ns.append(n)
    return (max(ns)+1) if ns else l+1

def main(zlo, zhi):
    cells = {}
    for row in csv.DictReader(open('/mnt/project/COORDINATES-2_13.csv')):
        if row['grade'] != 'computed': continue
        Z, ch, l = int(row['Z']), int(row['charge']), int(row['l'])
        if zlo <= Z <= zhi: cells.setdefault(Z, set()).add((ch, l))
    os.makedirs('out', exist_ok=True)
    for Z in sorted(cells):
        fn = f'out/Z{Z:03d}.tsv'; want = len(cells[Z])
        if os.path.exists(fn) and sum(1 for _ in open(fn)) - 1 == want: continue
        t = time.time(); rows = []
        for ch in sorted({c for c, l in cells[Z]}):
            ls = sorted(l for c, l in cells[Z] if c == ch)
            if ch == Z:
                rows += [(Z, ch, l, l+1, -0.5*Z*Z/(l+1)**2, 0.0) for l in ls]; continue
            V, x0 = tfd.potential(Z, ch); N = Z - ch
            for l in ls:
                n = n0(N, l) + 4; E = eigen(V, l, n, ch, Z)
                rows.append((Z, ch, l, n, E, n - ch/np.sqrt(-2*E)))
        with open(fn + '.tmp', 'w') as f:
            f.write('Z\tcharge\tl\tn_used\tE\tdelta_tfd\n')
            for r in rows: f.write(f'{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]:.9g}\t{r[5]:.6f}\n')
        os.replace(fn + '.tmp', fn)
        print(f'Z {Z:3d} {want:4d} cells {time.time()-t:6.1f}s', flush=True)

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
