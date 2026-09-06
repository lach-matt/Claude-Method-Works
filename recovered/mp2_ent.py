"""mp2_ent.py -- s34 (PREDICTION-MP2ENT): second-order pair correlation of the entrant with the core (and siblings), on the chain's own
spin-averaged HFS neutral orbitals; virtuals = discretised spectrum of the SAME local potential in a box (log mesh, generalized symmetric eigenproblem).
usage: python3 mp2_ent.py Z [Z ...]   (Z=2: He gate)   env LMAX (default 4), NPTS (600), RMAX (60). Appends mp2_ent.jsonl (key Z,LMAX). No constant."""
import sys,os,json,time,numpy as np
from scipy.linalg import eigh
from functools import lru_cache
from sympy.physics.wigner import wigner_6j, wigner_3j
from t5_scf import scf_occ, ground_occ
LMAX=int(os.environ.get("LMAX","4")); NPTS=int(os.environ.get("NPTS","600")); RMAX=float(os.environ.get("RMAX","60"))
OUT="mp2_ent.jsonl"
SH={2:('He','1s'),21:('Sc','3d'),39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),64:('Gd','5d'),71:('Lu','5d'),70:('Yb','4f')}
@lru_cache(None)
def w6(a,b,c,d,e,f): return float(wigner_6j(a,b,c,d,e,f))
@lru_cache(None)
def Ck(l,k,lp):   # <l||C^k||l'> = (-1)^l sqrt((2l+1)(2l'+1)) (l k l'; 0 0 0)
    return (-1)**l*np.sqrt((2*l+1)*(2*lp+1))*float(wigner_3j(l,k,lp,0,0,0))
def spectrum(Vf,Z):
    x=np.linspace(np.log(1e-5/Z),np.log(RMAX),NPTS); r=np.exp(x); h=x[1]-x[0]
    V=Vf(r); out={}
    # u=r^{1/2} y:  -1/2 y'' + [(l+1/2)^2/2 + r^2 V] y = E r^2 y ; y(0)=y(end)=0
    T=np.zeros((NPTS,NPTS)); i=np.arange(NPTS); T[i,i]=1.0/h**2; T[i[:-1],i[:-1]+1]=-0.5/h**2; T[i[1:],i[1:]-1]=-0.5/h**2
    B=np.diag(r*r)
    for l in range(LMAX+1):
        A=T+np.diag((l+0.5)**2/2+r*r*V)
        E,Y=eigh(A,B)
        P=Y*np.sqrt(r)[:,None]                      # P = u = r^{1/2} y ; normalise int P^2 dr = sum P^2 r h
        P/=np.sqrt(np.sum(P*P*(r*h)[:,None],axis=0))[None,:]
        out[l]=(E,P)
    return r,h,out
def Yk(f,r,dr,k):   # Y_k(r) = int f(r') r_<^k / r_>^{k+1} dr'  for radial density f (already includes dr weighting outside)
    a=np.cumsum(f*r**k*dr)-0.5*f*r**k*dr; b=np.cumsum((f/r**(k+1)*dr)[::-1])[::-1]-0.5*f/r**(k+1)*dr
    return a/r**(k+1)+b*r**k
def run(Z):
    el,sh=SH[Z]; occ=ground_occ(Z); t0=time.time()
    Vf,Es,Et,it=scf_occ(Z,occ,1)
    r,h,spec=spectrum(Vf,Z); dr=r*h
    # occupied: lowest states per l by count; entrant a
    nocc={}
    for n,l,k in occ: nocc[l]=max(nocc.get(l,0),n-l)
    la=int("spdf".index(sh[1])); na=int(sh[0]); ia=na-la-1
    def orb(l,j): E,P=spec[l]; return E[j],P[:,j]
    def virt(l): E,P=spec[l]; j0=nocc.get(l,0); return E[j0:],P[:,j0:]
    shells=[(n,l,k) for n,l,k in occ]
    ea,Pa=orb(la,ia)
    # check eigenvalue vs SCF
    chk=abs(ea-Es[(na,la)])
    def E2closed(lb,Pb,eb,same):
        # pair (a,b) both treated as closed shells; returns E2 and its radial share beyond r_s>10 (entrant density weight of the pair term is not separable:
        # we partition by the entrant orbital density itself: share = int_{r_s>10} Pa^2 dr, stated as the density tail share)
        tot=0.0; parts={}
        Vs={l:virt(l) for l in range(LMAX+1)}
        # precompute R^k[lr][ls] matrices for pairs (a r),(b s): Yk of Pa*Pr for each r
        for lr in range(LMAX+1):
            Er,Pr=Vs[lr]
            for ls in range(LMAX+1):
                Es_,Ps=Vs[ls]
                Den=Er[:,None]+Es_[None,:]-ea-eb
                Rk={}   # k -> R^k(ab,rs) matrix [r,s]
                Rkx={}  # k -> R^k(ab,sr) = int Pa Ps Yk(Pb Pr): matrix [r,s]
                ks=[k for k in range(0,2*LMAX+la+lb+2) if (abs(la-lr)<=k<=la+lr) and (abs(lb-ls)<=k<=lb+ls) and (la+lr+k)%2==0 and (lb+ls+k)%2==0]
                kx=[k for k in range(0,2*LMAX+la+lb+2) if (abs(la-ls)<=k<=la+ls) and (abs(lb-lr)<=k<=lb+lr) and (la+ls+k)%2==0 and (lb+lr+k)%2==0]
                for k in ks:
                    Yar=np.stack([Yk(Pa*Pr[:,j],r,dr,k) for j in range(Pr.shape[1])])          # [r, grid]
                    Rk[k]=Yar@((Pb[:,None]*Ps)*dr[:,None])                                      # [r,s]
                for k in kx:
                    Yas=np.stack([Yk(Pa*Ps[:,j],r,dr,k) for j in range(Ps.shape[1])])          # [s, grid]
                    Rkx[k]=(Yas@((Pb[:,None]*Pr)*dr[:,None])).T                                # [r,s]  = R^k(ab,sr)
                for L in range(abs(la-lb),la+lb+1):
                    if not (abs(lr-ls)<=L<=lr+ls): continue
                    for S in (0,1):
                        if same and (L+S)%2: continue
                        D=np.zeros_like(Den); Ex=np.zeros_like(Den)
                        for k in ks: D+=(-1)**(la+ls+L)*w6(la,lb,L,ls,lr,k)*Ck(la,k,lr)*Ck(lb,k,ls)*Rk[k]
                        for k in kx: Ex+=(-1)**(la+lr+L)*w6(la,lb,L,lr,ls,k)*Ck(la,k,ls)*Ck(lb,k,lr)*Rkx[k]
                        M=D+(-1)**(lr+ls+L+S)*Ex
                        c=-(0.5 if not same else 0.25)*(2*L+1)*(2*S+1)*np.sum(M*M/Den)
                        tot+=c
        return tot
    res={}; E2c={}
    for n,l,k in shells:
        if (n,l)==(na,la): continue
        eb,Pb=orb(l,n-l-1)
        e=E2closed(l,Pb,eb,False); E2c[f"{n}{'spdf'[l]}"]=round(e,5)
    Ea=E2closed(la,Pa,ea,True); Na=[k for n,l,k in shells if (n,l)==(na,la)][0]
    core=sum(E2c.values()); ent_core=core/(2*(2*la+1)); sib=(2.0/Na)*Ea if Na>1 else 0.0
    # tail share of the entrant density (r_s>10) on the box grid: needs total density; approximate with the SCF density at large r via Vf? use Pa^2 beyond r where 4pi r^2 n < ... skip: report <r> instead
    rmean=float(np.sum(Pa*Pa*r*dr))
    out=dict(Z=Z,el=el,sh=sh,LMAX=LMAX,NPTS=NPTS,RMAX=RMAX,eps_a=round(float(ea),5),eps_scf=round(float(Es[(na,la)]),5),E2_core_pairs=E2c,E2_aa_closed=round(float(Ea),5),
             Na=Na,E2_ent_core=round(float(ent_core),5),E2_ent_sib=round(float(sib),5),E2_ent=round(float(ent_core+sib),5),r_mean=round(rmean,3),sec=int(time.time()-t0))
    if Z==2: out['E2_He_total']=round(float(Ea),5)
    open(OUT,'a').write(json.dumps(out)+'\n'); print(out,flush=True)
done={(d['Z'],d['LMAX']) for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
for Z in map(int,sys.argv[1:]):
    if (Z,LMAX) in done: print("SKIP",Z,LMAX); continue
    run(Z)
