"""sox_qres.py -- s32: q-resolved second-order exchange of the UEG, g_2b(q), k_F units, Ry.
eps_2b = int dq g_2b(q) = E0B (0.0483584 Ry = 0.0241792 Ha, Onsager-Mittag-Stephen 1966).
Reduction (PREDICTION-SOSEX): the SOX integrand depends on (k1,k2) only via P = k1+k2, so
  g_2b(q) = (3/(16 pi^5)) 4 pi q^2 (1/q^2) int d^3P rho_q(P) / (|q+P|^2 (q^2 + q.P)),
  rho_q(P) = |L_q cap (P - L_q)|, L_q = {k<1, |k+q|>1}, computed as a 2-D (z, rho^2) integral over L_q with the
  azimuthal measure of the second lens condition analytic (two arccos). Lens edges are exact (rho^2 mapped per z).
Internal check: for q > 2, L_q is the unit ball and rho_q(P) = (4pi/3)(1 - 3P/4 + P^3/16).
usage: python3 sox_qres.py q1 q2 ...   (appends to sox_qres.jsonl; SKIP if q present)"""
import numpy as np, json, sys, os
NZ=int(os.environ.get("NZ",160)); NU=int(os.environ.get("NU",160)); NPP=int(os.environ.get("NPP",96)); NPV=int(os.environ.get("NPV",96))
PRE=3.0/(16*np.pi**5)

def rho_q(q,Ppar,Pperp):
    """rho_q(P) for arrays Ppar,Pperp of equal shape (flat). Returns same shape."""
    zlo=max(-1.0,-q/2); z=zlo+(1-zlo)*(np.arange(NZ)+0.5)/NZ; dz=(1-zlo)/NZ
    lo=np.maximum(0.0,1-(z+q)**2); hi=1-z*z; w=np.maximum(hi-lo,0.0)          # rho^2 interval per z
    ug=(np.arange(NU)+0.5)/NU
    U=lo[:,None]+w[:,None]*ug[None,:]                                          # rho^2 grid (NZ,NU)
    RHO=np.sqrt(U); Z=np.broadcast_to(z[:,None],U.shape)
    out=np.empty(Ppar.shape)
    for i,(pp,pv) in enumerate(zip(Ppar,Pperp)):
        a1=(pp-Z)**2+U+pv*pv-1.0; b1=(pp-Z+q)**2+U+pv*pv-1.0
        d=2*RHO*pv
        with np.errstate(divide='ignore',invalid='ignore'):
            A=np.where(d>0,a1/d,np.where(a1<0,-np.inf,np.inf))
            B=np.where(d>0,b1/d,np.where(b1>0,np.inf,-np.inf))
        A=np.clip(A,-1,1); B=np.clip(B,-1,1)
        meas=2*(np.arccos(A)-np.arccos(B)); meas=np.where(A<B,meas,0.0)
        out[i]=np.sum(meas*(w[:,None]/NU))*dz*0.5                                # int dz int rho drho = int dz int du/2
    return out

def g2b(q):
    # P grid: Ppar = -q + wq, wq in (0, 2+q) stretched toward 0 (denominator q(q+Ppar) = q wq); Pperp^2 = v uniform in (0,4)
    u=(np.arange(NPP)+0.5)/NPP; W=2+q; wq=W*u*u; dw=W*2*u/NPP
    v=4*(np.arange(NPV)+0.5)/NPV; dv=4.0/NPV
    WQ,V=np.meshgrid(wq,v,indexing='ij'); Ppar=-q+WQ; Pperp=np.sqrt(V)
    m=(Ppar**2+V<=4.0+1e-12)                                                   # |P|<=2 support
    r=np.zeros(WQ.shape); r[m]=rho_q(q,Ppar[m],Pperp[m])
    integrand=r/((WQ**2+V)*(q*WQ))                                              # 1/(|q+P|^2 (q^2+q Ppar))
    d3P=2*np.pi*0.5*(dw[:,None]*dv)                                             # 2pi Pperp dPperp dPpar = pi dv dPpar
    I=np.sum(integrand*d3P)
    return PRE*4*np.pi*I                                                        # q^2 (1/q^2) cancel

if __name__=="__main__":
    fn="sox_qres.jsonl"; done=set()
    if os.path.exists(fn):
        for l in open(fn): done.add(round(json.loads(l)["q"],8))
    for a in sys.argv[1:]:
        q=float(a)
        if round(q,8) in done: print("SKIP",q); continue
        if q>2:  # internal check of rho_q against the ball autoconvolution
            P=np.array([0.3,1.0,1.7]); rr=rho_q(q,P,np.zeros(3)); ex=(4*np.pi/3)*(1-3*P/4+P**3/16); chk=float(np.max(np.abs(rr/ex-1)))
        else: chk=None
        g=g2b(q); row={"q":q,"g2b_Ry":g,"NZ":NZ,"NU":NU,"NPP":NPP,"NPV":NPV,"ballchk":chk}
        open(fn,"a").write(json.dumps(row)+"\n"); print(json.dumps(row),flush=True)
