"""hfc2.py -- s27 item 4: HFSR 'hf' + self-consistent chain-Z correlation potential (PZ orbital SIC, chain mode "all") per shell; total energy
E = E_HF[P] + E_c^SIC[P]. usage: [CORR=0] python3 hfc2.py Z ...   Appends hfc2.jsonl (key Z,corr). CORR=0 = consistency gate (must == s26 D_HF).
Second-order piece := obj_2 - obj_s26. No constant beyond c; no measured input."""
import sys,os,json,time,numpy as np
os.environ.setdefault("SIC_NOCLAMP","1")
from t7c_hfsr import HFSR
from t7c_kernel import C0
from t5_scf import ground_occ,minus
import t7c_cuaudit as T
from t7b_hf import _c3j0sq
CORR=os.environ.get("CORR","1")=="1"
OUT="hfc2.jsonl"
SH={55:('Cs','6s'),64:('Gd','5d'),39:('Y','4d'),21:('Sc','3d'),57:('La','5d'),71:('Lu','5d'),70:('Yb','4f')}
def eps_c(nu,nd):
    """GB high-density eps_c(r_s,zeta) exactly as T.v_gbz (zero where eps>=0)."""
    n=nu+nd; n=np.maximum(n,1e-30); z=np.clip((nu-nd)/n,0.0,1.0)
    rs=(3.0/(4*np.pi*n))**(1.0/3.0); L=np.log(rs)
    e=T._lam0(z)*L+T._e0a(z)+T.E0B+((T._lam1(z)*rs*L) if T.LAM1 else 0.0)
    return np.where(e<0,e,0.0)
def spin_split(occ,P):
    nu=0; nd=0; sp={}
    for a,b,q in occ:
        cap=2*(2*b+1); up=min(q,cap/2); dn=max(q-cap/2,0); nu=nu+up*P[(a,b)]**2; nd=nd+dn*P[(a,b)]**2
        sp[(a,b)]=(up,dn)
    return nu,nd,sp
class HFC(HFSR):
    def corr_pot(self,P):
        """per-shell added local potential: v_c[n_up,n_dn](sigma_a) - v_c[P_a^2/w,0]; the shell's spin taken as majority (up) unless it is only down-filled."""
        r=self.r; w=4*np.pi*r*r; nu,nd,sp=spin_split(self.occ,P); vu,vd=T.v_gbz(nu/w,nd/w); V={}
        for a,b,q in self.occ:
            up,dn=sp[(a,b)]; vs=(up*vu+dn*vd)/q                       # occupation-weighted spin average for a shell holding both spins
            V[(a,b)]=vs-T.v_gbz(P[(a,b)]**2/w,0*r)[0]
        return V
    def E_c(self,P):
        r,dr=self.r,self.dr; w=4*np.pi*r*r; nu,nd,_=spin_split(self.occ,P)
        E=float(np.sum((nu+nd)*eps_c(nu/w,nd/w)*dr))
        for a,b,q in self.occ: E-=q*float(np.sum(P[(a,b)]**2*eps_c(P[(a,b)]**2/w,0*r)*dr))
        return E
    def run2(self,qtail=1,beta=0.4,tol=2e-6,maxit=100):
        occ=self.occ; r,dr=self.r,self.dr; P,eps=self.seed(qtail); keys=[(n,l) for n,l,q in occ]; Q={(n,l):q for n,l,q in occ}
        for it in range(maxit):
            Y0={k:self.Yk(P[k],P[k],0) for k in keys}; Vc=self.corr_pot(P) if CORR else {k:0.0 for k in keys}
            newP={};neweps={};dmax=0.0
            for a in keys:
                n,l=a; Vloc=-self.Z/r+sum((Q[b] if b!=a else self._ceff(a,Q))*Y0[b]/r for b in keys)+Vc[a]; X=np.zeros(self.npts)
                for b in keys:
                    nb,lb=b
                    if b==a:
                        c=self._ceff(a,Q)*(2*l+1)/(4*l+1)
                        if abs(c)>1e-14:
                            for k in range(2,2*l+1,2): Vloc=Vloc-c*_c3j0sq(l,k,l)*self.Yk(P[a],P[a],k)/r
                    else:
                        for k in range(abs(l-lb),l+lb+1,2): X+=0.5*Q[b]*_c3j0sq(l,k,lb)*self.Yk(P[a],P[b],k)/r*P[b]
                u,e,nd,res=self.solve_one(l,n,Vloc,X,eps[a],P[a])
                if nd!=n-l-1: raise RuntimeError(f"Z={self.Z} {n}{l} nodes {nd}")
                if np.sum(u*P[a]*dr)<0: u=-u
                dmax=max(dmax,abs(e-eps[a])); newP[a]=(1-beta)*P[a]+beta*u; newP[a]/=np.sqrt(np.sum(newP[a]**2*dr)); neweps[a]=(1-beta)*eps[a]+beta*e
            P,eps=newP,neweps
            if dmax<tol and it>2: break
        self.P,self.eps=P,eps
        # E_HF from converged P: E = 1/2 sum q (eps + I),  I = eps - <Vloc_full> + <X> - <Vc>  (Vc removed: it is not part of the HF energy)
        Y0={k:self.Yk(P[k],P[k],0) for k in keys}; Vc=self.corr_pot(P) if CORR else {k:0.0 for k in keys}; E=0.0
        for a in keys:
            n,l=a; Vloc=-self.Z/r+sum((Q[b] if b!=a else self._ceff(a,Q))*Y0[b]/r for b in keys); X=np.zeros(self.npts)
            for b in keys:
                nb,lb=b
                if b==a:
                    c=self._ceff(a,Q)*(2*l+1)/(4*l+1)
                    for k in range(2,2*l+1,2): Vloc=Vloc-c*_c3j0sq(l,k,l)*self.Yk(P[a],P[a],k)/r
                else:
                    for k in range(abs(l-lb),l+lb+1,2): X+=0.5*Q[b]*_c3j0sq(l,k,lb)*self.Yk(P[a],P[b],k)/r*P[b]
            eHF=eps[a]-np.sum(P[a]*Vc[a]*P[a]*dr)                     # HF-part eigenvalue: remove the added correlation potential
            Ia=eHF-np.sum(P[a]*(Vloc+self.Z/r)*P[a]*dr)+np.sum(P[a]*X*dr)
            E+=0.5*Q[a]*(eHF+Ia)
        Ec=self.E_c(P) if CORR else 0.0
        return float(E),float(Ec),it+1,eps
if __name__=="__main__":
    done={(d['Z'],d['corr']) for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
    H26={d['Z']:d for d in map(json.loads,open('hfdscf.jsonl'))}
    for Z in map(int,sys.argv[1:]):
        if (Z,CORR) in done: print("SKIP",Z,CORR); continue
        el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); t0=time.time()
        occ0=ground_occ(Z); occ1=[(a,b,q) for a,b,q in minus(occ0,n,l,1.0) if q>0]
        E0,Ec0,it0,e0=HFC(Z,occ0,c=C0).run2(); E1,Ec1,it1,e1=HFC(Z,occ1,c=C0).run2()
        D_HF=E1-E0; D_2=(E1+Ec1)-(E0+Ec0); h=H26.get(Z,{})
        o=dict(Z=Z,el=el,sh=sh,corr=CORR,E_HF_neu=round(E0,5),E_HF_ion=round(E1,5),Ec_neu=round(Ec0,5),Ec_ion=round(Ec1,5),D_HF=round(D_HF,5),
               D_2=round(D_2,5),obj_2=round(-D_2,5),D_HF_s26=h.get('D_HF'),Delta_c_s26=h.get('Delta_c'),obj_s26=h.get('obj'),
               second_order=round(-D_2-h['obj'],5) if h else None,eps_ent=round(float(e0[(n,l)]),5),it=[it0,it1],sec=int(time.time()-t0))
        open(OUT,"a").write(json.dumps(o)+"\n"); print(o,flush=True)
