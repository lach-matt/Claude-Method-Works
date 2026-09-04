#!/usr/bin/env python3
"""hfs.py -- Session 8, T1': a DERIVABLE kernel improvement at f. No new constant.

WHAT CHANGES AND WHAT DOES NOT. tfd.py builds V = -Z/r + V_es[rho_TF] + V_x[rho_TF] with Dirac's local
exchange V_x = -(3 rho/pi)^(1/3) (that is the D in TFD) and the Latter tail V <= -q/r. Here the SAME three
pieces are kept and only the density is replaced: rho from the occupied one-electron orbitals of the same
potential, iterated to self-consistency. That is Gaspar 1954 / Kohn-Sham 1965 exchange-only, run as
Herman-Skillman 1963 did (with Latter's tail). Occupations are the OBSERVED ground configuration of the
Z-1 core electrons (ground.py, NIST 5.12) -- the same core the charge-1 TFD object represents statistically.
Nothing is chosen: same nucleus, same exchange functional, same tail, same core count; the density is now
the orbitals' own. Mixing fraction and convergence tolerance are numerics, not physics (result checked
invariant to them).

PREDICTIONS, stated before the run (R 1449):
  (P1) J_H(4f) at Tb moves DOWN toward the Tb3+ value 0.0351 but stays ABOVE it (an orbital-density
       one-electron F^k is HF-like, and HF-like F^k exceed empirical ones). Not below.
  (P2) The four d-shell class steps (Mn Fe Tc Ru) and 5d/6d (Os Hs) stay IN: their windows are wide.
  (P3) 5f (Cm, Bk): NO confident prediction. Margins are 0.009-0.015 Ha under TFD; a self-consistent
       density can move both J_H and the E_B gaps by that much. This is the test the derived law must
       pass; if it fails here it fails honestly, and the failure is the finding.
  (P4) E_B gaps of the class species change by O(10 mHa); the ten class windows are therefore RECOMPUTED
       from the new kernel -- the law is evaluated inside one kernel, never TFD gaps against SCF P.
"""
import sys, json, numpy as np, tfd, warnings; warnings.filterwarnings("ignore")
import step2_run, eigen_fix
from eigen_fix import eigen
from derive_P import numerov_wf, slater_Fk, J_H
import ground as G

L = "spdfg"

def scf(Z, charge=1, npts=4000, beta=0.3, tol=2e-5, maxit=60, verbose=False):
    N = Z - charge; q = charge
    occ = list(G.expand(N))                       # (n, l, k) of the core, observed configuration
    x = np.linspace(np.log(1e-6/Z), np.log(300.0), npts); r = np.exp(x); h = x[1]-x[0]; dr = r*h
    Vtfd, _ = tfd.potential(Z, charge)
    Vg = Vtfd(r)                                   # start from the TFD potential on the grid
    Vfun = lambda rr: np.interp(np.log(np.asarray(rr, float)), x, Vg)
    hist = []
    for it in range(maxit):
        n_r = np.zeros(npts); Es = {}
        for n, l, k in occ:
            rr, drr, u, E, nd = numerov_wf(Vfun, l, n, 1.0, Z)
            if nd != n-l-1: raise RuntimeError(f"Z={Z} it={it} {n}{L[l]} nodes {nd} != {n-l-1} E={E}")
            ui = np.interp(r, rr, u, left=0.0, right=0.0)
            ui /= np.sqrt(np.sum(ui*ui*dr))
            n_r += k*ui*ui; Es[(n, l)] = E
        # Hartree potential of the radial density n_r (int n_r dr = N)
        cum = np.cumsum(n_r*dr) - 0.5*n_r*dr
        outer = np.cumsum((n_r/r*dr)[::-1])[::-1] - 0.5*n_r/r*dr
        VH = cum/r + outer
        rho = n_r/(4*np.pi*r*r)
        Vx = -(3.0*rho/np.pi)**(1.0/3.0)           # Dirac exchange, same as tfd.py's functional
        Vnew = np.minimum(-Z/r + VH + Vx, -q/r)     # Latter tail, same as tfd.py
        d = float(np.max(np.abs(r*(Vnew-Vg))[r < 60]))
        hist.append(d)
        Vg = (1-beta)*Vg + beta*Vnew
        Vfun = lambda rr, Vg=Vg: np.interp(np.log(np.asarray(rr, float)), x, Vg)
        if verbose: print(f"  it {it:2d}  max|r dV| = {d:.2e}", flush=True)
        if d < tol: break
    return Vfun, Es, hist, (r, dr, Vg)

if __name__ == "__main__":
    # sanity: neutral atoms (charge=0 not defined in tfd; use charge=1 objects and report core eigenvalues)
    for Z in (10, 18):
        Vf, Es, hist, _ = scf(Z, 1, verbose=False)
        print(f"Z={Z} charge 1: iters {len(hist)} final dV {hist[-1]:.1e}  core E:",
              {f"{n}{L[l]}": round(E, 4) for (n, l), E in Es.items()})
