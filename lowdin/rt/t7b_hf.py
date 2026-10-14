"""t7b_hf.py -- T7b (session 18): exact Fock exchange (Fock 1930; numerical HF as Froese Fischer 1977) on the log mesh.
Average-of-configuration HF for shells (n,l,q), q fractional allowed (Slater TS). No constant.
  Direct  : V_a(r) = -Z/r + sum_b (q_b - delta_ab) Y^0_bb(r)/r
  Exchange: X_a(r) = sum_{b!=a} (q_b/2) sum_k c_k(la,lb) Y^k_ab(r)/r P_b + (q_a-1) w_a sum_{k>0} c_k(la,la) Y^k_aa/r P_a,
            c_k = (la k lb;000)^2,  w = (2l+1)/(4l+1)  (Slater average energy of configuration)
  Equation: [-1/2 d2/dr2 + l(l+1)/2r2 + V_a] P_a - X_a = eps_a P_a ; solved as inhomogeneous two-sided Numerov (shoot_x.c) in
            y = r^{-1/2} P on x = ln r, eps fixed by ||P|| = 1 (Fischer's method), nodes checked.
  Total   : E = 1/2 sum_a q_a (eps_a + I_a),  I_a = eps_a - <V_a> + <P_a|X_a>.
  mode='hfs': same solver, exchange -> Dirac local -(3 rho/pi)^(1/3) on the FULL density, Hartree of the full density (no SI
            term), Latter tail min(V, -qtail/r): the T5 object (t5_scf.scf_occ) on the common mesh -- the switch gate.
Gates (MEASURED-STANDARD, Fischer 1977): He 1s eps -0.91796, Ne 2p eps -0.85041.  Session 18."""
import ctypes, math, numpy as np, warnings, io, contextlib; warnings.filterwarnings("ignore")
with contextlib.redirect_stdout(io.StringIO()): import tfd
from t5_scf import scf_occ, ground_occ, minus
from hfs import numerov_wf, L
_lib = ctypes.CDLL('./libshoot_x.so'); _D = ctypes.POINTER(ctypes.c_double)
_lib.shoot_x.argtypes = [ctypes.c_int, ctypes.c_double, _D, _D, ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, _D,_D,_D,_D]
def _c3j0sq(a, k, b):
    J = a+k+b
    if J % 2 or k < abs(a-b) or k > a+b: return 0.0
    g = J//2
    return math.factorial(J-2*a)*math.factorial(J-2*k)*math.factorial(J-2*b)/math.factorial(J+1) * \
           (math.factorial(g)/(math.factorial(g-a)*math.factorial(g-k)*math.factorial(g-b)))**2
class HF:
    def __init__(self, Z, occ, npts=4000):
        self.Z=Z; self.occ=[(n,l,float(q)) for n,l,q in occ]; self.npts=npts
        self.x=np.linspace(np.log(1e-6/Z),np.log(300.0),npts); self.r=np.exp(self.x); self.h=self.x[1]-self.x[0]; self.dr=self.r*self.h
    def Yk(self, Pa, Pb, k):
        w=Pa*Pb*self.dr; r=self.r
        A=np.cumsum(w*r**k)-0.5*w*r**k                       # int_0^r  r'^k
        B=np.cumsum((w/r**(k+1))[::-1])[::-1]-0.5*w/r**(k+1) # int_r^inf r'^-(k+1)
        return A/r**k + B*r**(k+1)                           # r * Y^k/r ... this is Y^k(r) (dimension of charge)
    def seed(self, qtail):
        Vf,Es,_,_=scf_occ(self.Z,[(n,l,q) for n,l,q in self.occ],qtail)
        P={}; eps={}
        for n,l,q in self.occ:
            rr,drr,u,E,nd=numerov_wf(Vf,l,n,1.0,self.Z)
            ui=np.interp(self.r,rr,u,left=0.0,right=0.0); ui/=np.sqrt(np.sum(ui*ui*self.dr)); P[(n,l)]=ui; eps[(n,l)]=E
        return P,eps
    def solve_one(self, l, n, Vloc, X, e0, Pold=None):
        """solve [-1/2 d2 + l(l+1)/2r2 + Vloc] P - X = eps P with ||P||=1, nodes n-l-1; returns P, eps."""
        r,x,h,N=self.r,self.x,self.h,self.npts; tgt=n-l-1
        s=-2.0*r**1.5*X
        yold=(Pold*np.exp(-x/2)) if (Pold is not None and np.any(X)) else np.zeros(N)
        def shoot(e):
            q=(l+0.5)**2+2*r*r*(Vloc-e); f=1-h*h*q/12.0
            allowed=np.where(q<0)[0]; m=int(allowed[-1]) if len(allowed) else N//2
            if m>N-4: m=N-4
            if m<2: m=2
            sq=np.sqrt(np.maximum(q,0)); cum=np.cumsum(sq[m:])*h; beyond=np.where(cum>(20.0 if np.any(s) else 60.0))[0]
            ie=m+int(beyond[0]) if len(beyond) else N-1
            if ie<m+3: ie=min(m+3,N-1)
            yoh,yop,yih,yip=(np.zeros(N) for _ in range(4))
            _lib.shoot_x(N,h,f.ctypes.data_as(_D),s.ctypes.data_as(_D),m,ie,1e-30,1e-30*math.exp((l+0.5)*h),float(yold[ie]),float(yold[ie-1]),
                         yoh.ctypes.data_as(_D),yop.ctypes.data_as(_D),yih.ctypes.data_as(_D),yip.ctypes.data_as(_D))
            # match y[m], y[m+1]:  yop+A yoh = yip + B yih
            M=np.array([[yoh[m],-yih[m]],[yoh[m+1],-yih[m+1]]]); rhs=np.array([yip[m]-yop[m],yip[m+1]-yop[m+1]])
            if not np.any(s): A,B=1.0,(yoh[m]/yih[m] if yih[m]!=0 else 0.0)
            else:
                try: A,B=np.linalg.solve(M,rhs)
                except np.linalg.LinAlgError: return None
            y=np.concatenate([yop[:m+1]+A*yoh[:m+1], yip[m+1:]+B*yih[m+1:]])
            u=np.exp(x/2)*y; nrm=float(np.sum(u*u*self.dr))
            uu=u[:m+1]; a=np.abs(uu); keep=a>1e-7*a.max(); sg=np.sign(uu[keep]); nd=int(np.sum(sg[1:]!=sg[:-1]))  # nodes inside r_m only
            return u,nrm,nd
        if not np.any(X):                       # homogeneous: banked eigen instrument on the same mesh interpolant
            from eigen_fix import eigen
            Vf=lambda rr,V=Vloc: np.interp(np.log(np.asarray(rr,float)),x,V)
            e=float(eigen(Vf,l,n,1.0,self.Z)); out=shoot(e); u,nrm,nd=out
            return u/np.sqrt(nrm),e,nd,0.0
        # bracketed bisection on ln N(e): N -> inf at e_h (own homogeneous eigenvalue of Vloc), N decreasing below it
        from eigen_fix import eigen
        Vf=lambda rr,V=Vloc: np.interp(np.log(np.asarray(rr,float)),x,V)
        eh=float(eigen(Vf,l,n,1.0,self.Z))
        def g(e):
            out=shoot(e)
            if out is None or not np.isfinite(out[1]) or out[1]<=0: return None
            return math.log(out[1]),out
        hi=eh-1e-7*abs(eh); rhi=g(hi)
        if getattr(self,'dbg',False): print(f"   dbg {n}{L[l]} eh {eh:.6f} lnN(hi) {rhi[0] if rhi else None}",flush=True)
        if rhi is None or rhi[0]<0:            # source pushes the other way (rare): search upward
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
            if getattr(self,'dbg',False) and rm is not None: print(f"   dbg {n}{L[l]} e {mid:.6f} lnN {rm[0]:+.3e} nd {rm[1][2]}",flush=True)
            if rm is None: hi=mid; continue
            if abs(rm[0])<1e-11 or hi-lo<1e-13*max(1,abs(mid)): best=(mid,rm[1]); break
            if rm[0]>0: hi=mid
            else: lo=mid
        if best is None: best=(mid,rm[1])
        e,(u,nrm,nd)=best
        u=u/np.sqrt(nrm)
        return u,e,nd,abs(math.log(nrm))
    frac=None   # s28 F26.2 lift: {(n,l): (q_c, f)} -> own-shell pair factor c_eff = [q_c(q_c-1)+2 f q_c]/(q_c+f); default (Q-1)
    def _ceff(self,a,Q):
        if self.frac and a in self.frac:
            qc,f=self.frac[a]; return (qc*(qc-1.0)+2.0*f*qc)/(qc+f)
        return Q[a]-1.0
    def run(self, mode='hf', qtail=1, beta=0.4, tol=2e-6, maxit=100, seed=None, verbose=False):
        occ=self.occ; r,dr=self.r,self.dr
        P,eps=seed if seed is not None else self.seed(qtail)
        keys=[(n,l) for n,l,q in occ]; Q={(n,l):q for n,l,q in occ}
        hist=[]
        for it in range(maxit):
            n_r=sum(Q[k]*P[k]*P[k] for k in keys)
            if mode=='hfs':
                cum=np.cumsum(n_r*dr)-0.5*n_r*dr; outer=np.cumsum((n_r/r*dr)[::-1])[::-1]-0.5*n_r/r*dr; VH=cum/r+outer
                rho=n_r/(4*np.pi*r*r); Vx=-(3.0*rho/np.pi)**(1.0/3.0)
                Vall=np.minimum(-self.Z/r+VH+Vx,-qtail/r)
            Y0={k:self.Yk(P[k],P[k],0) for k in keys}
            newP={}; neweps={}; dmax=0.0
            for a in keys:
                n,l=a
                if mode=='hfs': Vloc=Vall; X=np.zeros(self.npts)
                else:
                    Vloc=-self.Z/r+sum((Q[b] if b!=a else self._ceff(a,Q))*Y0[b]/r for b in keys)
                    X=np.zeros(self.npts)
                    for b in keys:
                        nb,lb=b
                        if b==a:                      # within-shell exchange is LOCAL (prop. to P_a): into Vloc
                            w=(2*l+1)/(4*l+1); c=self._ceff(a,Q)*w
                            if abs(c)>1e-14:
                                for k in range(2,2*l+1,2): Vloc=Vloc-c*_c3j0sq(l,k,l)*self.Yk(P[a],P[a],k)/r
                        else:
                            for k in range(abs(l-lb),l+lb+1,2): X+=0.5*Q[b]*_c3j0sq(l,k,lb)*self.Yk(P[a],P[b],k)/r*P[b]
                u,e,nd,res=self.solve_one(l,n,Vloc,X,eps[a],P[a])
                if nd!=n-l-1: raise RuntimeError(f"Z={self.Z} {n}{L[l]} nodes {nd}!={n-l-1} eps={e:.4f} mode={mode}")
                if np.sum(u*P[a]*dr)<0: u=-u
                dmax=max(dmax,abs(e-eps[a]))
                newP[a]=(1-beta)*P[a]+beta*u; newP[a]/=np.sqrt(np.sum(newP[a]**2*dr)); neweps[a]=(1-beta)*eps[a]+beta*e
            P,eps=newP,neweps; hist.append(dmax)
            if verbose: print(f"  it {it:3d} max|d eps| {dmax:.2e}",flush=True)
            if dmax<tol and it>2: break
        # total energy at convergence (unmixed final quantities from a last evaluation)
        self.P,self.eps=P,eps
        Etot=self.energy(mode,qtail)
        return eps,Etot,it+1,hist
    def energy(self, mode, qtail):
        P,eps,Q=self.P,self.eps,{(n,l):q for n,l,q in self.occ}; r,dr=self.r,self.dr; keys=list(P)
        if mode=='hfs':
            n_r=sum(Q[k]*P[k]*P[k] for k in keys)
            cum=np.cumsum(n_r*dr)-0.5*n_r*dr; outer=np.cumsum((n_r/r*dr)[::-1])[::-1]-0.5*n_r/r*dr; VH=cum/r+outer
            rho=n_r/(4*np.pi*r*r); Vx=-(3.0*rho/np.pi)**(1.0/3.0)
            return sum(Q[k]*eps[k] for k in keys)-0.5*np.sum(n_r*VH*dr)-0.25*np.sum(n_r*Vx*dr)
        Y0={k:self.Yk(P[k],P[k],0) for k in keys}; E=0.0
        for a in keys:
            n,l=a; Vloc=-self.Z/r+sum((Q[b] if b!=a else self._ceff(a,Q))*Y0[b]/r for b in keys)
            X=np.zeros(self.npts)
            for b in keys:
                nb,lb=b
                if b==a:
                    w=(2*l+1)/(4*l+1); c=self._ceff(a,Q)*w
                    for k in range(2,2*l+1,2): Vloc=Vloc-c*_c3j0sq(l,k,l)*self.Yk(P[a],P[a],k)/r
                else:
                    for k in range(abs(l-lb),l+lb+1,2): X+=0.5*Q[b]*_c3j0sq(l,k,lb)*self.Yk(P[a],P[b],k)/r*P[b]
            Ia=eps[a]-np.sum(P[a]*(Vloc+self.Z/r)*P[a]*dr)+np.sum(P[a]*X*dr)   # I = <T - Z/r>
            E+=0.5*Q[a]*(eps[a]+Ia)
        return float(E)
if __name__=="__main__":
    import sys
    # GATE A: He 1s HF eps -0.91796 (E -2.86168); Ne 2p eps -0.85041 (E -128.5471). Fischer 1977, MEASURED-STANDARD.
    for Z,occ,sh in ((2,[(1,0,2)],(1,0)),(10,[(1,0,2),(2,0,2),(2,1,6)],(2,1))):
        h=HF(Z,occ); eps,E,it,hist=h.run('hf',qtail=1)
        print(f"GATE A  Z={Z} {sh[0]}{L[sh[1]]} eps {eps[sh]:.5f}  E {E:.5f}  it {it}  last d {hist[-1]:.1e}",flush=True)
