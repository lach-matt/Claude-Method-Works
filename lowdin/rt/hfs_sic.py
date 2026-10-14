#!/usr/bin/env python3
"""hfs_sic.py -- session 10, T0 option (a'). The Test-E object (hfs_pol.scf_pol: spin-polarised Hund
occupation, per-channel Dirac exchange, Latter tail, Slater/Janak half-electron in the candidate shell) made
SELF-INTERACTION FREE per Perdew & Zunger 1981, PRB 23, 5048, eq. (33)-(35): each occupied channel (n,l,s)
sees, in addition to the spin-s potential, minus its own Hartree and exchange potential built from the
per-ORBITAL density n_i = f_i |phi_nl|^2 / 4pi, where f_i is the occupancy of ONE spatial orbital of the
shell.  Core shells: f_i = k/(2l+1) (spherically averaged).  The half-electron entrant sits in ONE orbital:
f_i = 1/2 (Slater 1972 / Janak 1978 transition state).  Nothing chosen: same nucleus, Hartree, Dirac exchange,
Latter tail, observed core occupation; the correction is the functional's own self-term, orbital by orbital.
NO free constant.  Perdew-Zunger exchange-only (no correlation, as in hfs.py).
"""
import numpy as np, tfd, warnings; warnings.filterwarnings("ignore")
import ground as G
from hfs import numerov_wf, L
from hfs_pol import split

def hartree(nr, r, dr):
    cum = np.cumsum(nr*dr) - 0.5*nr*dr
    outer = np.cumsum((nr/r*dr)[::-1])[::-1] - 0.5*nr/r*dr
    return cum/r + outer

def scf_sic(Z, charge=1, occ=None, entrant=None, npts=4000, beta=0.3, tol=2e-5, maxit=100, sic=True):
    """occ: list of (n,l,k) for the core (+ entrant if entrant given, k=0.5 added there).
    entrant: (n,l) or None. Returns (Es, hist): Es[(n,l,s)] eigenvalues of every occupied channel."""
    N = Z - charge; q = charge
    if occ is None: occ = list(G.expand(N)) if N > 0 else []
    occ = [list(t) for t in occ]
    ent_s = None
    if entrant is not None:
        n, l = entrant
        k0 = sum(t[2] for t in occ if t[0] == n and t[1] == l)
        ent_s = "d" if k0 >= 2*l+1 else "u"
        found = False
        for t in occ:
            if t[0] == n and t[1] == l: t[2] += 0.5; found = True
        if not found: occ.append([n, l, 0.5])
    up, dn = split([tuple(t) for t in occ])
    chans = [(n, l, k, "u") for n, l, k in up] + [(n, l, k, "d") for n, l, k in dn]
    # per-orbital occupancy f_i for the SIC density
    def f_orb(n, l, k, s):
        if entrant is not None and (n, l) == tuple(entrant) and s == ent_s:
            # this channel holds the half electron; k = k_core_s + 0.5.  Split: core part spherically
            # averaged over 2l+1 orbitals, entrant part in ONE orbital.  Use occupancy-weighted mean f.
            kc = k - 0.5
            if kc <= 0: return 0.5
            # weighted average of per-orbital occupancies over electrons: (kc*(kc/(2l+1)) + 0.5*0.5)/k
            return (kc*(kc/(2*l+1)) + 0.25)/k
        return k/(2*l+1)
    x = np.linspace(np.log(1e-6/Z), np.log(300.0), npts); r = np.exp(x); h = x[1]-x[0]; dr = r*h
    Vt, _ = tfd.potential(Z, charge); Vg = {s: Vt(r).copy() for s in "ud"}
    Vsic = {c: np.zeros(npts) for c in chans}          # per-channel SIC potential on grid
    hist = []; Es = {}
    for it in range(maxit):
        nsig = {"u": np.zeros(npts), "d": np.zeros(npts)}; dens = {}
        for c in chans:
            n, l, k, s = c
            Vtot = Vg[s] + Vsic[c]
            Vf = (lambda rr, V=Vtot: np.interp(np.log(np.asarray(rr, float)), x, V))
            rr, drr, u, E, nd = numerov_wf(Vf, l, n, 1.0, Z)
            if nd != n-l-1: raise RuntimeError(f"Z={Z} {n}{L[l]}{s} nodes {nd}")
            ui = np.interp(r, rr, u, left=0.0, right=0.0); ui /= np.sqrt(np.sum(ui*ui*dr))
            nsig[s] += k*ui*ui; dens[c] = ui*ui; Es[(n, l, s)] = E
        ntot = nsig["u"] + nsig["d"]
        VH = hartree(ntot, r, dr); d = 0.0; Vn = {}
        for s in "ud":
            rho = nsig[s]/(4*np.pi*r*r); Vx = -(6.0*rho/np.pi)**(1.0/3.0)
            Vn[s] = np.minimum(-Z/r + VH + Vx, -q/r)
            d = max(d, float(np.max(np.abs(r*(Vn[s]-Vg[s]))[r < 60])))
        Vsn = {}
        for c in chans:
            if not sic: Vsn[c] = np.zeros(npts); continue
            n, l, k, s = c; f = f_orb(n, l, k, s)
            ni = f*dens[c]                                  # radial per-orbital density (times 4pi r^2)
            rhoi = ni/(4*np.pi*r*r)
            vHi = hartree(ni, r, dr)
            vxi = -(6.0*rhoi/np.pi)**(1.0/3.0)              # spin-polarised Dirac x of a one-spin density
            Vsn[c] = -(vHi + vxi)
            d = max(d, float(np.max(np.abs(r*(Vsn[c]-Vsic[c]))[r < 60])))
        hist.append(d)
        for s in "ud": Vg[s] = (1-beta)*Vg[s] + beta*Vn[s]
        for c in chans: Vsic[c] = (1-beta)*Vsic[c] + beta*Vsn[c]
        if d < tol: break
    return Es, hist, ent_s

if __name__ == "__main__":
    import time
    t = time.time(); Es, h, s = scf_sic(20, 1, entrant=(3, 2))
    print("Ca 3d TS+SIC", Es[(3, 2, s)], "it", len(h), h[-1], round(time.time()-t, 1), "s")
    t = time.time(); Es, h, s = scf_sic(20, 1, entrant=(3, 2), sic=False)
    print("Ca 3d TS noSIC", Es[(3, 2, s)], "it", len(h), h[-1], round(time.time()-t, 1), "s")
