"""t7c_kernel.py -- T7c: scalar-relativistic radial kernel (Koelling & Harmon 1977: mass-velocity + Darwin, no
spin-orbit) replacing numerov_wf inside scf_occ.  Session 17.  No constant: c = 137.035999 (CODATA, a.u.).

KH equation for the large component P:  P'' = [l(l+1)/r^2 + 2M(V-E)] P + (M'/M)(P' - P/r),  M = 1 + (E-V)/(2c^2).
With P = M^{1/2} F the first-derivative term drops:  F'' = Q F,
   Q = l(l+1)/r^2 + 2M(V-E) - M'/(rM) - M''/(2M) + 3M'^2/(4M^2)         (M' = -V'/2c^2, M'' = -V''/2c^2)
so F rides the SAME C Numerov shoot and the SAME bisection as eigen_fix (log mesh y = r^{-1/2} F,
q_log = (l+1/2)^2 + r^2 (Q - l(l+1)/r^2)).  Coulomb limit: P ~ r^gamma, gamma = sqrt(1 - (Z/c)^2)  (Dirac).
c -> infinity: every extra term vanishes identically -> the non-relativistic kernel, term for term.
Density: P^2 = M F^2.  Gates: (i) c=1e6 regenerates the T5 HFS-TS column; (ii) H 1s at c=137.036 -> -0.5000067.
"""
import numpy as np, warnings; warnings.filterwarnings("ignore")
import step2_run
from step2_run import _shoot
import tfd, ground as G
from hfs import L
C0 = 137.035999

def _derivs(x, Vx):
    """V, V', V'' on a log mesh from V(x): dV/dr = (dV/dx)/r,  d2V/dr2 = (d2V/dx2 - dV/dx)/r^2."""
    r = np.exp(x); h = x[1]-x[0]
    d1 = np.gradient(Vx, h); d2 = np.gradient(d1, h)
    return d1/r, (d2-d1)/(r*r)

def qlog(r, V, Vp, Vpp, E, l, c):
    M = 1.0 + (E - V)/(2*c*c); Mp = -Vp/(2*c*c); Mpp = -Vpp/(2*c*c)
    Qx = 2*M*(V-E) - Mp/(r*M) - Mpp/(2*M) + 3*Mp*Mp/(4*M*M)
    return (l+0.5)**2 + r*r*Qx, M

def eigen_sr(V, l, n, zeta, Z, c=C0, npts=3000, tol=1e-9, Vp=None, Vpp=None):
    rmin, rmax = 1e-5/Z, max(80.0, 4.0*n*n/zeta)
    x = np.linspace(np.log(rmin), np.log(rmax), npts); h = x[1]-x[0]; r = np.exp(x)
    Vr = V(r)
    if Vp is None: Vpr, Vppr = _derivs(x, Vr)
    else: Vpr, Vppr = Vp(r), Vpp(r)
    target = n-l-1
    def too_high(E):
        q,_ = qlog(r, Vr, Vpr, Vppr, E, l, c); y, nd = _shoot(q, h, l)
        return nd > target or (nd == target and y[-1]*(-1)**target < 0)
    Elo, Ehi = -0.6*zeta*zeta, -1e-9; cap = -0.5*Z*Z*(1+ (Z/c)**2)   # relativistic 1s lies below -Z^2/2; widen cap
    while too_high(Elo) and Elo > cap: Elo = max(4*Elo, cap)
    for _ in range(200):
        E = 0.5*(Elo+Ehi)
        if too_high(E): Ehi = E
        else: Elo = E
        if Ehi-Elo < tol*abs(E)+1e-13: break
    return 0.5*(Elo+Ehi)

def numerov_wf_sr(V, l, n, zeta, Z, c=C0, npts=3000, Vp=None, Vpp=None):
    """Same contract as hfs.numerov_wf: returns r, dr, u(=P, normalised), E, nodes."""
    E = eigen_sr(V, l, n, zeta, Z, c, npts, Vp=Vp, Vpp=Vpp)
    rmin, rmax = 1e-5/Z, max(80.0, 4.0*n*n/zeta)
    x = np.linspace(np.log(rmin), np.log(rmax), npts); h = x[1]-x[0]; r = np.exp(x)
    Vr = V(r)
    if Vp is None: Vpr, Vppr = _derivs(x, Vr)
    else: Vpr, Vppr = Vp(r), Vpp(r)
    q, M = qlog(r, Vr, Vpr, Vppr, E, l, c); f = 1 - h*h*q/12.0
    allowed = np.where(q < 0)[0]; m = allowed[-1] if len(allowed) else npts//2
    yo = np.zeros(npts); yo[0] = 1e-30; yo[1] = yo[0]*np.exp((l+0.5)*h)
    for i in range(1, m+1):
        yo[i+1] = ((12-10*f[i])*yo[i] - f[i-1]*yo[i-1])/f[i+1]
        if abs(yo[i+1]) > 1e100: yo[:i+2] /= 1e100
    yi = np.zeros(npts); yi[-1] = 1e-30; yi[-2] = yi[-1]*np.exp(np.sqrt(max(q[-1],1e-12))*h)
    for i in range(npts-2, m, -1):
        yi[i-1] = ((12-10*f[i])*yi[i] - f[i+1]*yi[i+1])/f[i-1]
        if abs(yi[i-1]) > 1e100: yi[i-1:] /= 1e100
    y = np.concatenate([yo[:m+1], yi[m+1:]*(yo[m]/yi[m])]) if yi[m] != 0 else yo
    u = np.exp(x/2)*y*np.sqrt(np.maximum(M, 1e-300))        # P = M^{1/2} F
    dr = r*h
    # forbidden-region tail clean, as hfs.numerov_wf
    a = np.abs(u); mm = int(np.argmax(a)); thr = 1e-9*a[mm]
    tail = np.where(a[mm:] < thr)[0]
    if len(tail): u[mm+tail[0]:] = 0.0
    u /= np.sqrt(np.sum(u*u*dr))
    sg = np.sign(u); sg = sg[sg != 0]; nd = int(np.sum(sg[1:] != sg[:-1]))
    return r, dr, u, E, nd

def scf_occ_sr(Z, occ, qtail, c=C0, npts=4000, beta=0.3, tol=2e-5, maxit=80):
    """t5_scf.scf_occ verbatim with numerov_wf -> numerov_wf_sr; V', V'' taken on the SCF mesh."""
    N = sum(k for _,_,k in occ)
    x = np.linspace(np.log(1e-6/Z), np.log(300.0), npts); r = np.exp(x); h = x[1]-x[0]; dr = r*h
    Vt,_ = tfd.potential(Z, max(int(round(Z-N)),1)); Vg = Vt(r)
    def mk(Vg):
        Vp, Vpp = _derivs(x, Vg)
        f  = lambda rr: np.interp(np.log(np.asarray(rr,float)), x, Vg)
        fp = lambda rr: np.interp(np.log(np.asarray(rr,float)), x, Vp)
        fpp= lambda rr: np.interp(np.log(np.asarray(rr,float)), x, Vpp)
        return f, fp, fpp
    Vf, Vpf, Vppf = mk(Vg)
    for it in range(maxit):
        n_r = np.zeros(npts); Es = {}
        for n,l,k in occ:
            rr,drr,u,E,nd = numerov_wf_sr(Vf,l,n,1.0,Z,c,Vp=Vpf,Vpp=Vppf)
            if nd != n-l-1: raise RuntimeError(f"Z={Z} {n}{L[l]} nodes {nd}")
            ui = np.interp(r,rr,u,left=0.0,right=0.0); ui /= np.sqrt(np.sum(ui*ui*dr)); n_r += k*ui*ui; Es[(n,l)] = E
        cum = np.cumsum(n_r*dr)-0.5*n_r*dr; outer = np.cumsum((n_r/r*dr)[::-1])[::-1]-0.5*n_r/r*dr; VH = cum/r+outer
        rho = n_r/(4*np.pi*r*r); Vx = -(3.0*rho/np.pi)**(1.0/3.0)
        Vn = np.minimum(-Z/r+VH+Vx, -qtail/r); d = float(np.max(np.abs(r*(Vn-Vg))[r<60]))
        Vg = (1-beta)*Vg+beta*Vn; Vf, Vpf, Vppf = mk(Vg)
        if d < tol: break
    Etot = sum(k*Es[(n,l)] for n,l,k in occ)-0.5*np.sum(n_r*VH*dr)-0.25*np.sum(n_r*Vx*dr)
    return Vf, Es, Etot, it+1

if __name__ == "__main__":
    import sys, json
    from hfs import numerov_wf
    Vh = lambda r: -1.0/np.asarray(r, float)
    e_nr = numerov_wf(Vh,0,1,1.0,1)[3]; e_inf = numerov_wf_sr(Vh,0,1,1.0,1,c=1e6)[3]; e_c = numerov_wf_sr(Vh,0,1,1.0,1)[3]
    print(f"H 1s  nonrel {e_nr:.7f}  sr(c=1e6) {e_inf:.7f}  sr(c=137.036) {e_c:.7f}  Dirac -0.5000067  shift {e_c-e_inf:+.7f}")
    # hydrogenic Z=70 1s: Dirac 1s = c^2(sqrt(1-(Z/c)^2)-1); also via an interpolated potential (SCF-mesh style) to test V'' noise
    Z=70; Vz = lambda r: -Z/np.asarray(r,float); ed = C0**2*(np.sqrt(1-(Z/C0)**2)-1)
    e_a = numerov_wf_sr(Vz,0,1,1.0,Z)[3]
    x = np.linspace(np.log(1e-6/Z), np.log(300.0), 4000); Vg = Vz(np.exp(x)); Vp,Vpp = _derivs(x,Vg)
    fi = lambda rr: np.interp(np.log(np.asarray(rr,float)),x,Vg); fpi=lambda rr: np.interp(np.log(np.asarray(rr,float)),x,Vp); fppi=lambda rr: np.interp(np.log(np.asarray(rr,float)),x,Vpp)
    e_i = numerov_wf_sr(fi,0,1,1.0,Z,Vp=fpi,Vpp=fppi)[3]
    e_2p = numerov_wf_sr(Vz,1,2,1.0,Z)[3]; ed2p = C0**2*(1/np.sqrt(1+(Z/C0)**2/(1+np.sqrt(1-(Z/C0)**2))**2)-1)  # Dirac 2p1/2
    ed2p32 = C0**2*(1/np.sqrt(1+(Z/C0)**2/(1+np.sqrt(4-(Z/C0)**2))**2)-1)
    print(f"Z=70 1s  sr(analytic V) {e_a:.4f}  sr(interp V) {e_i:.4f}  Dirac {ed:.4f}  nonrel {-Z*Z/2:.4f}")
    print(f"Z=70 2p  sr {e_2p:.4f}   Dirac 2p1/2 {ed2p:.4f}  2p3/2 {ed2p32:.4f}  (KH j-average lies between)")
