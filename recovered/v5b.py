#!/usr/bin/env python3
"""v5b.py -- S95 V5 STAGE (b)/(c): second-order energy E2 of the sealed AOC-RHF object in its own grid basis (spectra from v5a npz).
DECLARED (spec §1 + s95 decisions):
  E2 = 1/4 sum_{ij occ, vw virt spin-orbitals} w_ij (1-f_v)(1-f_w) |<ij||vw>|^2 / (e_i+e_j-e_v-e_w)
    f = q/Q per spin-orbital of a shell (Q = 2(2l+1)); w_ij = f_i f_j for different shells, q(q-1)/(Q(Q-1)) for the same open shell (no self-pair);
    virtual slots: spectrum roots with e < E_cut (Lowdin-projected orthogonal to the sealed occupied of that l, F95.4) PLUS the open shell's own
    radial orbital with weight (1-f). Occupied energies: sealed eps; virtual energies: <v|h_VN|v> of the projected root.
  Angular factors: brute-force sums over m of Gaunt coefficients c^k(lm,l'm') = (-1)^m sqrt((2l+1)(2l'+1)) (l k l';000)(l k l';-m,m-m',m')  [sympy 3j].
    No closed-shell MBPT formula is used. Spin sums explicit (4 direct, 4 exchange, 2 cross).
  Singles (Brillouin fails for AOC): core singles DROPPED (Brillouin exact in V^N for closed shells; only F95.4 noise); open-shell singles
    E2s = f sum_v |<e|h_VN|v>|^2/(e_e - e_v), reported separately.
  Levers: E_cut (20/50/100 Ha) -- must move E2 (instrument rule). l_max from the npz.
usage: v5b.py NPZ [--ecut 50] [--canfail A|C]   prints E2 pieces; writes NPZ.e2-ECUT.json.  CF-A: ecut 0 -> E2 == 0. CF-C: integrals x2 -> E2 x4? no: |..|^2 scales x4 -> declared factor 4.
External can-fails run via v5he.py (He/Ne objects)."""
import sys, os, json, time, numpy as np, itertools
from functools import lru_cache
from sympy.physics.wigner import wigner_3j
from sympy import N as SN
npz=sys.argv[1]; ecut=float(sys.argv[sys.argv.index('--ecut')+1]) if '--ecut' in sys.argv else 50.0
cf=sys.argv[sys.argv.index('--canfail')+1] if '--canfail' in sys.argv else None
if cf=='A': ecut=-1e9
D=np.load(npz); r=D['r']; dr=D['dr']; eps={tuple(json.loads(k.replace('(','[').replace(')',']'))):v for k,v in json.loads(str(D['eps'])).items()}
occ=[tuple(o) for o in json.loads(str(D['occ']))]; N=len(r); lmax=max(int(k[1:]) for k in D.files if k.startswith('w'))
@lru_cache(None)
def w3j(a,b,c,d,e,f): return float(SN(wigner_3j(a,b,c,d,e,f)))
@lru_cache(None)
def gaunt(l,lp,k):
    """matrix c^k[m+l, m'+lp]"""
    C=np.zeros((2*l+1,2*lp+1)); z=w3j(l,k,lp,0,0,0)
    if z==0: return C
    for m in range(-l,l+1):
        for mp in range(-lp,lp+1):
            if abs(m-mp)>k: continue
            C[m+l,mp+lp]=(-1)**m*np.sqrt((2*l+1)*(2*lp+1))*z*w3j(l,k,lp,-m,m-mp,mp)
    return C
@lru_cache(None)
def ang(la,lb,lv,lw):
    """returns ks (list), Dd[k,k'], Dx[k,k'], Dm[k,k'] for |<ab||vw>|^2 = sum_kk' [Rk(ab;vw)Rk'(ab;vw) Dd + Rk(ab;wv)Rk'(ab;wv) Dx - 2 Rk(ab;vw) Rk'(ab;wv) Dm] (m-summed, spin-summed)"""
    kd=[k for k in range(abs(la-lv),la+lv+1,2) if abs(lb-lw)<=k<=lb+lw and (lb+lw+k)%2==0]
    kx=[k for k in range(abs(la-lw),la+lw+1,2) if abs(lb-lv)<=k<=lb+lv and (lb+lv+k)%2==0]
    cav={k:gaunt(la,lv,k) for k in kd}; cbw={k:gaunt(lb,lw,k) for k in kd}; caw={k:gaunt(la,lw,k) for k in kx}; cbv={k:gaunt(lb,lv,k) for k in kx}
    Dd=np.array([[4*np.sum(cav[k]*cav[kp])*np.sum(cbw[k]*cbw[kp]) for kp in kd] for k in kd])
    Dx=np.array([[4*np.sum(caw[k]*caw[kp])*np.sum(cbv[k]*cbv[kp]) for kp in kx] for k in kx])
    Dm=np.array([[2*np.einsum('av,bw,aw,bv',cav[k],cbw[k],caw[kp],cbv[kp]) for kp in kx] for k in kd])
    return kd,kx,Dd,Dx,Dm
def Yk(Pa,Pb,k):
    w=Pa*Pb*dr; A=np.cumsum(w*r**k)-0.5*w*r**k; B=np.cumsum((w/r**(k+1))[::-1])[::-1]-0.5*w/r**(k+1); return A/r**k+B*r**(k+1)
# occupied and virtual sets per l
Q={(n,l):q for n,l,q in occ}; shells=[(n,l) for n,l,q in occ]; Pocc={k:D['P%d%d'%k] for k in shells}
f={k:Q[k]/(2*(2*k[1]+1)) for k in shells}
virt={}   # l -> (energies, radial functions [N, nv], weights (1-f))
for l in range(lmax+1):
    w=D['w%d'%l]; F=D['F%d'%l]; keep=w<ecut; w=w[keep]; F=F[:,keep]
    occl=[k for k in shells if k[1]==l]
    if occl and F.shape[1]:
        O=np.stack([Pocc[k] for k in occl],1); F=F-O@((O*dr[:,None]).T@F)             # project out sealed occupied
        # drop the roots that were the occupied ones (norm after projection small), re-orthonormalise (Lowdin)
        nrm=np.sqrt(np.sum(F*F*dr[:,None],0)); keep2=nrm>0.5; F=F[:,keep2]/nrm[keep2]; w=w[keep2]
        S=(F*dr[:,None]).T@F; ev,U=np.linalg.eigh(S); F=F@U@np.diag(ev**-0.5)@U.T
        w=np.array([wi for wi in w])   # energies: keep root energies (declared; <v|h|v> refinement not computed at stage c)
    E=list(w); FF=[F[:,i] for i in range(F.shape[1])]; W=[1.0]*len(E)
    for k in occl:
        if f[k]<1: E.append(eps[k]); FF.append(Pocc[k]); W.append(1-f[k])
    virt[l]=(np.array(E),FF,np.array(W))
print("virtual counts per l (ecut %.0f): %s"%(ecut,{l:len(virt[l][0]) for l in virt}),flush=True)
# E2 doubles
t0=time.time(); E2=0.0; parts={}
for ia,a in enumerate(shells):
    for b in shells[ia:]:
        la,lb=a[1],b[1]; wab=(Q[a]*(Q[a]-1)/(2*(2*la+1)*(2*(2*la+1)-1)) if a==b else f[a]*f[b]); sym=(1.0 if a==b else 2.0)  # pair counted once; a!=b twice
        if wab==0: continue
        eab=eps[a]+eps[b]; Epair=0.0
        for lv in range(lmax+1):
            for lw in range(lmax+1):
                kd,kx,Dd,Dx,Dm=ang(la,lb,lv,lw)
                if not kd and not kx: continue
                Ev,Fv,Wv=virt[lv]; Ew,Fw,Ww=virt[lw]
                if not len(Ev) or not len(Ew): continue
                Fvm=np.stack(Fv,1); Fwm=np.stack(Fw,1)
                # R_k(ab;vw) = int Y^k(a,v)/r * P_b P_w dr  -> matrix [v,w]
                Rd={k:((Yk_av:=np.stack([Yk(Pocc[a],Fvm[:,i],k)/r for i in range(Fvm.shape[1])],1)).T@(Pocc[b][:,None]*Fwm*dr[:,None])) for k in kd}
                Rx={k:(np.stack([Yk(Pocc[a],Fwm[:,i],k)/r for i in range(Fwm.shape[1])],1).T@(Pocc[b][:,None]*Fvm*dr[:,None])).T for k in kx}  # [v,w]: R_k(ab;wv)
                den=eab-Ev[:,None]-Ew[None,:]; wt=Wv[:,None]*Ww[None,:]
                num=np.zeros_like(den)
                for i,k in enumerate(kd):
                    for j,kp in enumerate(kd): num+=Dd[i,j]*Rd[k]*Rd[kp]
                for i,k in enumerate(kx):
                    for j,kp in enumerate(kx): num+=Dx[i,j]*Rx[k]*Rx[kp]
                for i,k in enumerate(kd):
                    for j,kp in enumerate(kx): num-=2*Dm[i,j]*Rd[k]*Rx[kp]
                Epair+=0.25*sym*wab*np.sum(wt*num/den)
        parts["%d%d-%d%d"%(a+b)]=Epair; E2+=Epair
# open-shell singles
E2s=0.0
for a in shells:
    if f[a]<1:
        pass  # <e|h_VN|v> requires the operator; stage (c) reports doubles only; singles flagged NOT COMPUTED
print("E2 doubles = %.6f Ha  (%.0fs)  singles: NOT COMPUTED (flag)"%(E2,time.time()-t0),flush=True)
json.dump(dict(npz=os.path.basename(npz),ecut=ecut,E2=E2,parts=parts,nvirt={l:int(len(virt[l][0])) for l in virt}),open(npz.replace('.npz','.e2-%d.json'%int(max(ecut,0))),'w'),indent=0)
if cf=='A': sys.exit(4 if abs(E2)<1e-12 else 1)