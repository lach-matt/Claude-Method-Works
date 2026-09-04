"""t7c_mult.py -- session 19 (bridge-18 s3(3)): is the mixed-sign 4f scatter the multiplet coordinate (R 1665)?
meas = -(IP + E_hole) is LEVEL-to-LEVEL; t7c_pol is the spin-polarised configuration average (the max-S manifold average).
The gap is Hund-II: stab(k) = E(lowest L term) - E(average of max-S manifold) for k same-spin f electrons (holes for n>7),
computed by exact CI over the C(7,k) all-parallel-spin determinants with F^k (k=2,4,6) from OUR 4f orbital (SR-pol TS object,
c=137.035999). Corrected = t7c_pol + stab(neutral) - stab(ion). No measured input, no constant. Predictions PM1/PM2 stated in chat first."""
import sys, json, itertools, numpy as np, warnings; warnings.filterwarnings("ignore")
from sympy.physics.wigner import gaunt
from t5_scf import ground_occ, minus
from t7c_pol import scf_pol_sr, split
from t7c_kernel import numerov_wf_sr, C0
L=3; MS=range(-L,L+1)
# Gaunt: G[k][(m1,m2)] = int Y*_{3m1} Y_{k,m1-m2} Y_{3m2}, real
G={k:{(a,b):float(gaunt(L,k,L,-a,a-b,b))*(-1)**a for a in MS for b in MS if abs(a-b)<=k} for k in (0,2,4,6)}
def Fk(u,r,dr):
    F={}
    for k in (0,2,4,6):
        rho=u*u
        inner=np.cumsum(rho*r**k*dr)-0.5*rho*r**k*dr           # int_0^r rho r'^k
        outer=np.cumsum((rho/r**(k+1)*dr)[::-1])[::-1]-0.5*rho/r**(k+1)*dr
        F[k]=float(np.sum(rho*dr*(inner/r**(k+1)+outer*r**k)))
    return F
def V2(a,b,c,d,F):   # <ab|1/r12|cd>, all m_l of same spin
    if a+b!=c+d: return 0.0
    return sum(F[k]*4*np.pi/(2*k+1)*G[k].get((a,c),0.0)*G[k].get((d,b),0.0) for k in (2,4,6) if abs(a-c)<=k)  # k=0 constant, cancels
def ci(k,F):
    dets=[tuple(c) for c in itertools.combinations(list(MS),k)]
    if k<2: return 0.0
    n=len(dets); H=np.zeros((n,n)); idx={d:i for i,d in enumerate(dets)}
    for i,D in enumerate(dets):
        S=set(D)
        # diagonal
        H[i,i]=sum(V2(a,b,a,b,F)-V2(a,b,b,a,F) for a,b in itertools.combinations(D,2))
        # single excitations a->p, double a,b->p,q
        for a in D:
            for p in MS:
                if p in S: continue
                E1=tuple(sorted((S-{a})|{p})); j=idx[E1]
                # sign: permutation parity of moving
                sgn=(-1)**(sorted(D).index(a)+sorted(E1).index(p))
                H[j,i]+= sgn*sum(V2(p,b,a,b,F)-V2(p,b,b,a,F) for b in D if b!=a)
        for a,b in itertools.combinations(D,2):
            for p,q in itertools.combinations([m for m in MS if m not in S],2):
                E2=tuple(sorted((S-{a,b})|{p,q})); j=idx[E2]
                sd=sorted(D); se=sorted(E2)
                sgn=(-1)**(sd.index(a)+sd.index(b)+se.index(p)+se.index(q))
                H[j,i]+= sgn*(V2(p,q,a,b,F)-V2(p,q,b,a,F))
    w=np.linalg.eigvalsh(H)
    return float(w[0]-np.mean(np.diag(H)))   # lowest term - manifold average (trace/n = average over all M_L)
if __name__=="__main__":
    T5={json.loads(l)['Z']:json.loads(l) for l in open('t5.jsonl')}
    P={json.loads(l)['Z']:json.loads(l) for l in open('t7c_pol.jsonl')}
    HOLES={66:(4,5),68:(2,3),69:(1,2),70:(0,1)}
    for Z in map(int,sys.argv[1:]):
        r=T5[Z]; occ=minus(ground_occ(Z),4,3,0.5)
        probe,Es,h=scf_pol_sr(Z,1,occ=occ,c=C0)
        # recover the 4f orbital: rerun the SCF and grab u -- scf_pol_sr keeps V private, so rebuild via probe? Simplest: reuse its final Vf via closure
        Vf=probe.__closure__[[c.cell_contents for c in probe.__closure__].__len__()-1] if False else None
        # direct: get u from numerov on the converged 'd' channel potential held in probe's closure
        cells={n:c.cell_contents for n,c in zip(probe.__code__.co_freevars,probe.__closure__)}
        Vf=cells['Vf']; s='d'
        rr,drr,u,E,nd=numerov_wf_sr(Vf[s][0],3,4,1.0,Z,C0,Vp=Vf[s][1],Vpp=Vf[s][2])
        u=u/np.sqrt(np.sum(u*u*drr)); F=Fk(u,rr,drr)
        kn,ki=HOLES[Z]; sn=ci(kn,F); si=ci(ki,F)
        corr=P[Z]['t7c_pol']+sn-si; dev0=P[Z]['dev_pct']; dev1=round(100*(corr-r['meas'])/abs(r['meas']),1)
        row=dict(Z=Z,el=r['el'],F2=round(F[2],4),F4=round(F[4],4),F6=round(F[6],4),holes=[kn,ki],stab_n=round(sn,4),stab_i=round(si,4),
                 t7c_pol=P[Z]['t7c_pol'],corr=round(corr,4),meas=r['meas'],dev0=dev0,dev1=dev1)
        open('t7c_mult.jsonl','a').write(json.dumps(row)+'\n'); print(row,flush=True)
