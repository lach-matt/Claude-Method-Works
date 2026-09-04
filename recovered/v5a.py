#!/usr/bin/env python3
"""v5a.py -- S95 V5 STAGE (a): virtual spectrum per l of the SEALED one-electron operator on the sealed grid, row 89 (sides: core = cfg(88); ent = cfg(88)+6d).
DECLARED construction (spec SPEC-SECOND-ORDER-V5 §2, with the linearisation the spec did not foresee):
  sealed equation (t7c_kernel.qlog): y'' + q(E) y = s,  q = (l+1/2)^2 + r^2 Qx(E),  Qx = 2M(V-E) - Mp/(rM) - Mpp/(2M) + 3Mp^2/(4M^2),  M = 1+(E-V)/2c^2.
  Linearisation: M, Mp, Mpp frozen at E_ref -> A y = E B y,  A = D2 + diag[(l+1/2)^2 + r^2(2 M_ref V + D_ref)] + EXCH,  B = diag(2 r^2 M_ref).
  Exchange: the V^N nonlocal kernel (all occupied shells at full Q; sealed Slater G_k, sealed _c3j0sq) acting on F = r^{1/2} y; in B^{-1/2}-scaled form
  its matrix is sqrt(M_i/M_j) r_i^{1/2} S_ij r_j^{1/2} h (S symmetric). The factor sqrt(M_i/M_j) is the KH-level non-self-adjointness of the sealed
  kernel's srcM=True convention; SYMMETRISED here to 1 (declared; measured by the consistency check below).
  Consistency check (per occupied shell a, E_ref := sealed eps_a): nearest generalized eigenvalue vs sealed eps_a, and |<y|P_a>|. This isolates the
  symmetrisation + discretisation error. For the open shell (AOC ceff != Q) the V^N operator is NOT the sealed operator of that shell; reported separately.
usage: v5a.py SIDE [--eref X] [--lmax 6]   SIDE in {core, ent}. Writes pack95/v5a-89-SIDE.npz (spectra) and prints the check table. No scoring."""
import sys, os, json, time, numpy as np, scipy.linalg as sla
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(HERE,'..','rt')); os.chdir(os.path.join(HERE,'..','rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0, _derivs
from t7b_hf import _c3j0sq
assert H.CORR is False
ROWS={d['Z']:d for d in map(json.loads,open('nlchain.jsonl'))}
side=sys.argv[1]; lmax=int(sys.argv[sys.argv.index('--lmax')+1]) if '--lmax' in sys.argv else 6
eref_cli=float(sys.argv[sys.argv.index('--eref')+1]) if '--eref' in sys.argv else None
Z=89; cfg=NC.cfg_from_chain(88,ROWS); 
if side=='ent': cfg=NC.add(cfg,(6,2))
def solve(Z,cfg):
    for rung,(beta,maxit) in enumerate(NG.LADDER):
        g=H.HFC(Z,[tuple(x) for x in cfg],c=C0); E,_,it,eps=g.run2(beta=beta,maxit=maxit)
        if it<maxit: return g,float(E),rung,it
    raise RuntimeError
t0=time.time(); g,E,rung,it=solve(Z,cfg); print("solved %s E=%.5f rung %d it %d (%.1fs) occ=%s"%(side,E,rung,it,time.time()-t0,g.occ))
r,x,h,dr,N=g.r,g.x,g.h,g.dr,g.npts; P=g.P; eps=g.eps; keys=[(n,l) for n,l,q in g.occ]; Q={(n,l):q for n,l,q in g.occ}; c=C0
# direct potential (V^N): -Z/r + sum_b Q_b Y0_b / r  (no ceff: the operator a VIRTUAL sees)
Y0={k:g.Yk(P[k],P[k],0) for k in keys}; Vdir=-Z/r+sum(Q[b]*Y0[b]/r for b in keys)
# Slater kernel G_k(r_i,r_j) = r_<^k / r_>^(k+1)
def Gk(k):
    ri=r[:,None]; rj=r[None,:]; lo=np.minimum(ri,rj); hi=np.maximum(ri,rj); return lo**k/hi**(k+1)
def exch_S(l):
    S=np.zeros((N,N))
    for b in keys:
        nb,lb=b
        for k in range(abs(l-lb),l+lb+1,2):
            coef=0.5*Q[b]*_c3j0sq(l,k,lb)
            if coef>1e-14: S+=coef*(P[b][:,None]*Gk(k)*P[b][None,:])
    return S
D2=(np.diag(-2*np.ones(N))+np.diag(np.ones(N-1),1)+np.diag(np.ones(N-1),-1))/(h*h)
Vp,Vpp=_derivs(x,Vdir)
def build(l,Eref,S):
    M=1+(Eref-Vdir)/(2*c*c); Mp=-Vp/(2*c*c); Mpp=-Vpp/(2*c*c)
    Dref=-Mp/(r*M)-Mpp/(2*M)+3*Mp*Mp/(4*M*M)
    A=D2+np.diag((l+0.5)**2+r*r*(2*M*Vdir+Dref)); Bd=2*r*r*M; Bi=1/np.sqrt(Bd)
    C=A*Bi[:,None]*Bi[None,:]; C+=np.sqrt(r)[:,None]*S*np.sqrt(r)[None,:]*h      # symmetrised exchange (sqrt(M_i/M_j) -> 1)
    C=0.5*(C+C.T); return C,Bi
out={}
for l in range(lmax+1):
    t1=time.time(); S=exch_S(l)
    occ_l=[a for a in keys if a[1]==l]
    for a in occ_l:                                   # consistency: E_ref = sealed eps_a
        C,Bi=build(l,eps[a],S); w,v=sla.eigh(C); j=np.argmin(abs(w-eps[a]))
        y=v[:,j]*Bi; F=np.sqrt(r)*y; F/=np.sqrt(np.sum(F*F*dr)); ov=abs(np.sum(F*P[a]*dr))
        print("  check l=%d %s: sealed eps %.6f  lin %.6f  dE %+.2e  overlap %.6f  (aoc=%s)"%(l,a,eps[a],w[j],w[j]-eps[a],ov,"OPEN" if Q[a]<2*(2*l+1) else "closed"),flush=True)
    Eref=eref_cli if eref_cli is not None else 0.0
    C,Bi=build(l,Eref,S); w,v=sla.eigh(C)
    nb=int(np.sum(w<0)); print(" l=%d E_ref %.2f: %d negative roots, %d roots < 20 Ha, %d < 100 Ha; lowest %s  (%.1fs)"%(l,Eref,nb,int(np.sum(w<20)),int(np.sum(w<100)),np.round(w[:4],4),time.time()-t1),flush=True)
    keep=w<150; F=(np.sqrt(r)[:,None]*(v[:,keep]*Bi[:,None])); F/=np.sqrt(np.sum(F*F*dr[:,None],0))
    out['w%d'%l]=w[keep]; out['F%d'%l]=F
np.savez(os.path.join(HERE,'v5a-89-%s.npz'%side),r=r,dr=dr,eps=json.dumps({str(k):v for k,v in eps.items()}),occ=json.dumps(g.occ),E=E,Eref=Eref,**{('P%d%d'%k):P[k] for k in keys},**out)
print("wrote v5a-89-%s.npz  total %.1fs"%(side,time.time()-t0))