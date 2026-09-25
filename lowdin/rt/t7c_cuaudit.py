"""t7c_cuaudit.py -- s24: t7c_corrz.py VERBATIM + env FENT (entrant SIC density weight) + env FOCC (entrant occupation), defaults 0.5/0.5 = standing. Base t7c_corrz.py -- s23: t7c_corr2 + corr="Z" pointwise eps_c(r_s,zeta) (lam0 WP91, eps0a in-project ring table, eps0b OMS66). Base: t7c_corr.py -- t7c_sic.scf_sic_sr VERBATIM + Gell-Mann-Brueckner local correlation (U/P bracket) with PZ orbital SIC of it. Session 21."""
"""t7a_sic.py -- T7a: ORBITAL-RESOLVED Perdew-Zunger 1981 SIC (PRB 23, 5048, eqs 33-35) on the Test-E object.  Session 17.
hfs_sic.scf_sic verbatim except that every channel is split into orbital groups, each with its OWN radial function and OWN V_SIC:
integer-occupied orbitals f_i = 1 (closed or open shell alike -- PZ removes the full self-term of an occupied orbital); the
half-hole entrant orbital f_i = 1/2 (Slater/Janak transition state), separate from its integer-occupied siblings.
Closed channels are unchanged -> gate: Zn I 3d TS in the 4s entrant reproduces hfs_sic to 1e-4 (every channel there is closed or
single-orbital).  No constant.  Es keys: (n,l,s,tag) with tag "ent" for the half-hole orbital, "int" for the integer group.
"""
import numpy as np, tfd, warnings; warnings.filterwarnings("ignore")
import ground as G
from hfs import L
from t7c_kernel import numerov_wf_sr, _derivs, C0
from hfs_pol import split
from hfs_sic import hartree, scf_sic
import os
EXACT=os.environ.get("GB_EXACT","0")=="1"; NOCLAMP=os.environ.get("SIC_NOCLAMP","0")=="1"; FENT=float(os.environ.get("FENT","0.5")); FOCC=float(os.environ.get("FOCC","0.5")); CSIC_ENT=os.environ.get("CSIC_ENT","1")=="1"
A_U,B_U=(1-np.log(2))/np.pi**2,(-0.046908 if EXACT else -0.048); A_P,B_P=A_U/2,(-0.025725 if EXACT else -0.0269)   # s22: GB_EXACT=1 -> Loos-Gill/Onsager exact eps0 (Hoffman eps0^a + OMS eps0^b)

import json as _json
_T=_json.load(open("eps0a_table.json")); _xm=np.array([(1-z)**(1/3) for z in _T["zeta"]]); _e0=np.array(_T["eps0a_Ha"])
_o=np.argsort(_xm); _xm=_xm[_o]; _e0=_e0[_o]
E0B=np.log(2)/6-3*1.2020569031595942/(4*np.pi**2)
LAM1=os.environ.get("LAM1","0")=="1"
from lam1_zeta import lam1 as _lam1
from cellcut import SUBCELL as _SUBCELL, frac_neg as _frac_neg
def _cL(z):
    xp,xm=(1+z)**(1/3),(1-z)**(1/3); chi=xp+xm
    with np.errstate(divide='ignore',invalid='ignore'):
        t=xm**3*np.log(np.where(xm>0,xm,1.0))
    return (1/np.pi**2)*((1-np.log(2))+xp*xm/2*chi-np.log(chi)+0.5*(xp**3*np.log(xp)+t))
def _lam0(z): return _cL(z)/2
def _e0a(z): return np.interp((1-z)**(1/3),_xm,_e0)
def v_gbz(nu,nd):
    """pointwise GB high-density eps_c(r_s,zeta); returns (v_up, v_dn), zero where eps>=0."""
    n=nu+nd; n=np.maximum(n,1e-30); z=np.clip((nu-nd)/n,0.0,1.0)
    rs=(3.0/(4*np.pi*n))**(1.0/3.0); L=np.log(rs)
    lam=_lam0(z); e0=_e0a(z); l1=(_lam1(z) if LAM1 else 0.0)
    eps=lam*L+e0+E0B+l1*rs*L
    h=1e-4; zp=np.clip(z+h,0,1); zm=np.clip(z-h,0,1)
    f=lambda zz: _lam0(zz)*L+_e0a(zz)+((_lam1(zz)*rs*L) if LAM1 else 0.0)
    deps_dz=(f(zp)-f(zm))/(zp-zm+1e-300)
    base=eps-lam/3.0-l1*rs*(L+1.0)/3.0        # -(r_s/3) d eps/d r_s
    vu=base+(1-z)*deps_dz; vd=base-(1+z)*deps_dz
    if _SUBCELL:                                   # s28 ruling D: finite-volume in-cell fraction of eps<0 (cellcut.py)
        w=_frac_neg(eps); return vu*w, vd*w
    ok=eps<0
    return np.where(ok,vu,0.0), np.where(ok,vd,0.0)

def v_gb(rho,pol):
    """GB high-density correlation potential, zero where eps_c>=0 (eps_c<=0 constraint). rho: density (a.u.)."""
    A,B=(A_P,B_P) if pol else (A_U,B_U)
    rs=np.where(rho>1e-30,(3.0/(4*np.pi*np.maximum(rho,1e-30)))**(1.0/3.0),1e30)
    eps=A*np.log(rs)+B; v=eps-A/3.0
    return np.where(eps<0,v,0.0)
def scf_sic_corr(Z, charge=1, occ=None, entrant=None, npts=4000, beta=0.3, tol=2e-5, maxit=100, sic=True, mode="all", lam=1.0, cl=C0, corr=None):
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
            if t[0] == n and t[1] == l: t[2] += FOCC; found = True
        if not found: occ.append([n, l, FOCC])
    up, dn = split([tuple(t) for t in occ])
    chans = []
    for lst, s in ((up, "u"), (dn, "d")):
        for n, l, k in lst:
            if entrant is not None and (n, l) == tuple(entrant) and s == ent_s:
                kc = k - FOCC
                if kc > 1e-9: chans.append((n, l, kc, s, 1.0, "int"))     # kc integer-occupied orbitals, f_i = 1 each
                chans.append((n, l, FOCC, s, FENT, "ent"))                    # the half-hole orbital, f_i = 1/2, own phi and V_SIC
            else:
                chans.append((n, l, k, s, 1.0, "int"))                       # integer-occupied orbitals: f_i = 1 (closed or open)
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
    Vt, _ = tfd.potential(Z, charge); Vg = {s: Vt(r).copy() for s in "ud"}; Vraw = {s: Vt(r).copy() for s in "ud"}
    Vsic = {c: np.zeros(npts) for c in chans}          # per-channel SIC potential on grid
    hist = []; Es = {}
    for it in range(maxit):
        nsig = {"u": np.zeros(npts), "d": np.zeros(npts)}; dens = {}
        for c in chans:
            n, l, k, s, f, tag = c
            Vtot = (Vraw[s] if (NOCLAMP and np.any(Vsic[c])) else Vg[s]) + Vsic[c]   # s22 4a: PZ-81, no Latter clamp on a SIC channel
            Vp, Vpp = _derivs(x, Vtot)
            Vf = (lambda rr, V=Vtot: np.interp(np.log(np.asarray(rr, float)), x, V))
            Vfp = (lambda rr, V=Vp: np.interp(np.log(np.asarray(rr, float)), x, V))
            Vfpp = (lambda rr, V=Vpp: np.interp(np.log(np.asarray(rr, float)), x, V))
            rr, drr, u, E, nd = numerov_wf_sr(Vf, l, n, 1.0, Z, cl, Vp=Vfp, Vpp=Vfpp)
            if nd != n-l-1: raise RuntimeError(f"Z={Z} {n}{L[l]}{s} nodes {nd}")
            ui = np.interp(r, rr, u, left=0.0, right=0.0); ui /= np.sqrt(np.sum(ui*ui*dr))
            nsig[s] += k*ui*ui; dens[c] = ui*ui; Es[(n, l, s, tag)] = E
        ntot = nsig["u"] + nsig["d"]
        VH = hartree(ntot, r, dr); d = 0.0; Vn = {}; cmask = {}; Vrawn = {}
        for s in "ud":
            rho = nsig[s]/(4*np.pi*r*r); Vx = -(6.0*rho/np.pi)**(1.0/3.0)
            if corr=="Z":
                _vu,_vd = v_gbz(nsig["u"]/(4*np.pi*r*r), nsig["d"]/(4*np.pi*r*r)); Vc = _vu if s=="u" else _vd
            else:
                Vc = np.zeros(npts) if corr is None else (v_gb(ntot/(4*np.pi*r*r),False) if corr=="U" else v_gb(rho,True))
            Vn[s] = np.minimum(-Z/r + VH + Vx + Vc, -q/r); cmask[s] = ((-Z/r + VH + Vx + Vc) < -q/r)
            Vrawn[s] = -Z/r + VH + Vx + Vc
            if NOCLAMP: cmask[s] = np.ones(npts,bool)
            d = max(d, float(np.max(np.abs(r*(Vn[s]-Vg[s]))[r < 60])))
        Vsn = {}
        for c in chans:
            if (not sic) or mode=="none" or (mode=="ent" and c[5]!="ent"): Vsn[c] = np.zeros(npts); continue
            n, l, k, s, f, tag = c
            ni = f*dens[c]                                  # radial per-orbital density (times 4pi r^2)
            rhoi = ni/(4*np.pi*r*r)
            vHi = hartree(ni, r, dr)
            vxi = -(6.0*rhoi/np.pi)**(1.0/3.0)              # spin-polarised Dirac x of a one-spin density
            vci = np.zeros(npts) if corr is None else (v_gbz(rhoi,0*rhoi)[0] if corr=="Z" else v_gb(rhoi,True))*cmask[s]
            if (not CSIC_ENT) and c[5]=="ent": vci = np.zeros(npts)   # s24 mask-remainder test: entrant correlation SIC off   # one-orbital density is fully polarised; m
            Vsn[c] = -(vHi + vxi + vci)*(1.0 if c[5]=="ent" else lam)
            d = max(d, float(np.max(np.abs(r*(Vsn[c]-Vsic[c]))[r < 60])))
        hist.append(d)
        for s in "ud": Vg[s] = (1-beta)*Vg[s] + beta*Vn[s]; Vraw[s] = (1-beta)*Vraw[s] + beta*Vrawn[s]
        for c in chans: Vsic[c] = (1-beta)*Vsic[c] + beta*Vsn[c]
        if d < tol: break
    scf_sic_corr.last = dict(chans=chans, Vsic=Vsic, dens=dens, r=r, dr=dr)
    return Es, hist, ent_s
