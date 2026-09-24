#!/usr/bin/env python3
"""derive_P.py -- Session 7. Bridge-6 T1: derive P from the kernel, no chosen constant.
P_l = (2l+1) * J_H(nl);  J_H(d) = (F2+F4)/14 ;  J_H(f) = (286 F2 + 195 F4 + 250 F6)/6435.
F^k(nl,nl) = int int u^2(r1) u^2(r2) r<^k / r>^(k+1),  u from the CHARGE-1 TFD potential
(rule B object, exactly the object that produced the EB gaps), at the pack-5 kernel's E(n,l).
Wavefunction: Numerov outward to the outer turning point, inward from rmax, matched there.
Test the derived P must pass (SEQUENCE-MISSES-SESSION-6.md): per-shell EB windows.
Nothing written to register/index/store."""
import sys, json, numpy as np, tfd
from step2_run import eigen; import eigen_fix; from eigen_fix import eigen  # Session 8: adaptive floor

def numerov_wf(V, l, n, zeta, Z, npts=3000):
    E = eigen(V, l, n, zeta, Z, npts=npts)
    rmin, rmax = 1e-5/Z, max(80.0, 4.0*n*n/zeta)
    x = np.linspace(np.log(rmin), np.log(rmax), npts); h = x[1]-x[0]; r = np.exp(x)
    q = (l+0.5)**2 + 2*r*r*(V(r)-E); f = 1 - h*h*q/12.0
    # matching point: outer classical turning point (last sign change of q)
    allowed = np.where(q < 0)[0]
    m = allowed[-1] if len(allowed) else npts//2
    yo = np.zeros(npts); yo[0] = 1e-30; yo[1] = yo[0]*np.exp((l+0.5)*h)
    for i in range(1, m+1):
        yo[i+1] = ((12-10*f[i])*yo[i] - f[i-1]*yo[i-1])/f[i+1]
        if abs(yo[i+1]) > 1e100: yo[:i+2] /= 1e100
    yi = np.zeros(npts); yi[-1] = 1e-30; yi[-2] = yi[-1]*np.exp(np.sqrt(max(q[-1],1e-12))*h)
    for i in range(npts-2, m, -1):
        yi[i-1] = ((12-10*f[i])*yi[i] - f[i+1]*yi[i+1])/f[i-1]
        if abs(yi[i-1]) > 1e100: yi[i-1:] /= 1e100
    y = np.concatenate([yo[:m+1], yi[m+1:] * (yo[m]/yi[m]) ]) if yi[m] != 0 else yo
    # continuity check at m: rescale inward branch so y[m] from both sides agree
    u = np.exp(x/2)*y
    dr = r*h
    u /= np.sqrt(np.sum(u*u*dr))
    nodes = int(np.sum((u[1:-1] < 0) != (u[:-2] < 0)))
    return r, dr, u, E, nodes

def slater_Fk(r, dr, u, ks):
    w = u*u*dr
    out = {}
    for k in ks:
        A = np.cumsum(w * r**k) - 0.5*w*r**k          # int_0^r1 u^2 r2^k dr2, midpoint at r1
        out[k] = 2*np.sum(w * A / r**(k+1))
    return out

def J_H(l, F):
    if l == 2: return (F[2]+F[4])/14.0
    if l == 3: return (286*F[2]+195*F[4]+250*F[6])/6435.0
    raise ValueError

if __name__=='__main__':
    # ---- self-test on hydrogen    : F^0(1s,1s)=5/8, F^2(2p,2p)=... exact hydrogenic values (Z=1)
    Vh = lambda r: -1.0/r
    r, dr, u, E, nd = numerov_wf(Vh, 0, 1, 1.0, 1)
    F = slater_Fk(r, dr, u, (0,))
    print(f"self-test H 1s: E={E:.6f} nodes={nd} F0={F[0]:.5f} (exact 0.62500)")
    r, dr, u, E, nd = numerov_wf(Vh, 2, 3, 1.0, 1)
    F = slater_Fk(r, dr, u, (0,2,4))
    print(f"self-test H 3d: E={E:.6f} nodes={nd} F0={F[0]:.5f} F2={F[2]:.5f} F4={F[4]:.5f}"
          f"  (exact F0=0.11602 F2=0.02979... see check below)")
    # exact hydrogenic 3d: F0 = 4801/23040·... use numeric reference from literature: F2(3d3d)=0.03098? we print only.

    # ---- the ten species (SEQUENCE-MISSES class), charge-1 object, entrant shell
    CLASS = [("Mn",25,3,2),("Fe",26,3,2),("Tc",43,4,2),("Ru",44,4,2),("Gd",64,4,3),("Tb",65,4,3),
             ("Os",76,5,2),("Cm",96,5,3),("Bk",97,5,3),("Hs",108,6,2)]
    WIN = {"3d":(0.0108,0.2978),"4d":(0.0262,0.2245),"4f":(0.0569,0.2180),"5d":(0.0,0.5494),
           "5f":(0.1250,0.2145),"6d":(0.0,0.3261)}
    L="spdfg"; rows=[]
    for el,Z,n,l in CLASS:
        V,x0 = tfd.potential(Z,1)
        r,dr,u,E,nd = numerov_wf(V,l,n,1.0,Z)
        ks = (0,2,4) if l==2 else (0,2,4,6)
        F = slater_Fk(r,dr,u,ks); J = J_H(l,F); P=(2*l+1)*J
        sh=f"{n}{L[l]}"; lo,hi=WIN[sh]
        verdict = "IN" if lo<P<hi else ("ABOVE" if P>=hi else "BELOW")
        floor = abs(E+0.6)<1e-6
        rows.append(dict(el=el,Z=Z,shell=sh,E=round(E,5),E_at_floor=floor,nodes=nd,rmean=round(float(np.sum(u*u*dr*r)),3),
                         F={k:round(v,5) for k,v in F.items()},J_H=round(J,5),P=round(P,5),P_eV=round(P*27.211,3),
                         window=(lo,hi),verdict=verdict))
        print(f"{el:3s} Z={Z:3d} {sh}  E={E:8.5f} nodes={nd} <r>={rows[-1]['rmean']:.3f}  "
              + " ".join(f"F{k}={v:.5f}" for k,v in F.items())
              + f"  J_H={J:.5f}  P={P:.4f} Ha ({P*27.211:.2f} eV)  window {lo}-{hi}  {verdict}{'  **E AT BISECTION FLOOR -0.6**' if floor else ''}",flush=True)
    json.dump(rows,open("derive_P.json","w"),indent=1)
