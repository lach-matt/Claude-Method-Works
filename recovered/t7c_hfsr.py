"""t7c_hfsr.py -- session 22. Scalar-relativistic HF entrant object: t7b_hf.HF with the local operator in the banked KH form
(t7c_kernel.qlog verbatim) built from the LOCAL part of the Fock potential; nonlocal exchange as source -2*M*r^1.5*X (srcM=True) or
-2*r^1.5*X (srcM=False, Cowan-Griffin form). c=None -> exactly the banked t7b path (solve_one inherited). No constant beyond c."""
import math, numpy as np, warnings; warnings.filterwarnings("ignore")
from t7b_hf import HF, _lib, _D, L
from t7c_kernel import qlog, eigen_sr, _derivs, C0
class HFSR(HF):
    def __init__(self, Z, occ, npts=4000, c=C0, srcM=True):
        super().__init__(Z, occ, npts); self.c=c; self.srcM=srcM
    def solve_one(self, l, n, Vloc, X, e0, Pold=None):
        if self.c is None: return super().solve_one(l,n,Vloc,X,e0,Pold)
        r,x,h,N,c=self.r,self.x,self.h,self.npts,self.c; tgt=n-l-1
        Vp,Vpp=_derivs(x,Vloc)
        Vf=lambda rr,V=Vloc: np.interp(np.log(np.asarray(rr,float)),x,V)
        Vpf=lambda rr,V=Vp: np.interp(np.log(np.asarray(rr,float)),x,V)
        Vppf=lambda rr,V=Vpp: np.interp(np.log(np.asarray(rr,float)),x,V)
        yold=(Pold*np.exp(-x/2)) if (Pold is not None and np.any(X)) else np.zeros(N)
        def shoot(e):
            q,M=qlog(r,Vloc,Vp,Vpp,e,l,c); f=1-h*h*q/12.0
            s=-2.0*(M if self.srcM else 1.0)*r**1.5*X
            allowed=np.where(q<0)[0]; m=int(allowed[-1]) if len(allowed) else N//2
            if m>N-4: m=N-4
            if m<2: m=2
            sq=np.sqrt(np.maximum(q,0)); cum=np.cumsum(sq[m:])*h; beyond=np.where(cum>(20.0 if np.any(s) else 60.0))[0]
            ie=m+int(beyond[0]) if len(beyond) else N-1
            if ie<m+3: ie=min(m+3,N-1)
            yoh,yop,yih,yip=(np.zeros(N) for _ in range(4))
            _lib.shoot_x(N,h,f.ctypes.data_as(_D),s.ctypes.data_as(_D),m,ie,1e-30,1e-30*math.exp((l+0.5)*h),float(yold[ie]),float(yold[ie-1]),
                         yoh.ctypes.data_as(_D),yop.ctypes.data_as(_D),yih.ctypes.data_as(_D),yip.ctypes.data_as(_D))
            Mm=np.array([[yoh[m],-yih[m]],[yoh[m+1],-yih[m+1]]]); rhs=np.array([yip[m]-yop[m],yip[m+1]-yop[m+1]])
            if not np.any(s): A,B=1.0,(yoh[m]/yih[m] if yih[m]!=0 else 0.0)
            else:
                try: A,B=np.linalg.solve(Mm,rhs)
                except np.linalg.LinAlgError: return None
            y=np.concatenate([yop[:m+1]+A*yoh[:m+1], yip[m+1:]+B*yih[m+1:]])
            u=np.exp(x/2)*y*np.sqrt(np.maximum(M,1e-300)); nrm=float(np.sum(u*u*self.dr))     # P = M^{1/2} F (banked convention)
            uu=u[:m+1]; a=np.abs(uu); keep=a>1e-7*a.max(); sg=np.sign(uu[keep]); nd=int(np.sum(sg[1:]!=sg[:-1]))
            return u,nrm,nd
        eh=float(eigen_sr(Vf,l,n,1.0,self.Z,c,Vp=Vpf,Vpp=Vppf))
        if not np.any(X):
            u,nrm,nd=shoot(eh); return u/np.sqrt(nrm),eh,nd,0.0
        def g(e):
            out=shoot(e)
            if out is None or not np.isfinite(out[1]) or out[1]<=0: return None
            return math.log(out[1]),out
        hi=eh-1e-7*abs(eh); rhi=g(hi)
        if rhi is None or rhi[0]<0:
            lo,rlo=hi,rhi; step=0.02*abs(eh)+1e-4
            for _ in range(60):
                hi=lo+step; rhi=g(hi)
                if rhi is not None and rhi[0]>0: break
                lo,rlo=hi,rhi; step*=1.5
        else:
            step=0.02*abs(eh)+1e-4; lo=hi-step; rlo=g(lo)
            for _ in range(60):
                if rlo is not None and rlo[0]<0: break
                step*=1.6; lo=hi-step; rlo=g(lo)
        best=None
        for it in range(80):
            mid=0.5*(lo+hi); rm=g(mid)
            if rm is None: hi=mid; continue
            if abs(rm[0])<1e-11 or hi-lo<1e-13*max(1,abs(mid)): best=(mid,rm[1]); break
            if rm[0]>0: hi=mid
            else: lo=mid
        if best is None: best=(mid,rm[1])
        e,(u,nrm,nd)=best
        return u/np.sqrt(nrm),e,nd,abs(math.log(nrm))
if __name__=="__main__":
    import sys
    from t5_scf import ground_occ, minus
    # G1: He 1s at c=1e6 ; Sc 3d TS at c=1e6 vs banked t7b -0.2681
    h=HFSR(2,ground_occ(2),c=1e6); eps,E,it,_=h.run('hf',qtail=1); print("G1 He 1s c=1e6",round(eps[(1,0)],5),"it",it,flush=True)
    for Z,n,l,mode,c,ref in ((21,3,2,'hfs',C0,-0.2686),(57,5,2,'hfs',C0,-0.2017)):
        h=HFSR(Z,minus(ground_occ(Z),n,l,0.5),c=c); eps,E,it,_=h.run(mode,qtail=1)
        print(f"G2 Z={Z} {mode} sr eps(1/2) {eps[(n,l)]:.4f} banked t7c_ts {ref}  it {it}",flush=True)