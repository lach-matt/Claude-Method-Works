"""nlterm.py -- s38 item 1: term/multiplet energies on the WALK'S FIELD (hfc2, SR HF, no corr), both members of the d/s pair.
Design filed in PREDICTION-TERMS-VALIDATION-SESSION-38.md BEFORE this file existed.
(i)  the lowest term is COMPUTED by the Slater diagonal-sum rule over the open shell's determinants -- not asserted by Hund's rules.
     hund_det (max S then max L) is carried as a comparison column; the record's label is RECALLED-NOT-ENTERED, compared, never input.
(ii) FROZEN average-of-configuration orbitals of each state's own hfc2 SCF (the nlwalk_hf field). No per-term relaxation here.
(iii) LS only; no SO (zeta is a separate column, t7c_so).
sign convention: nlwalk's D_rel(x) = E_neu - E_ion(x)  (negative = bound). With terms E_tot = E_avg + dE_term (dE_term <= 0),
     so D_term(x) = D_rel(x) + dE_term(neu) - dE_term(ion_x).   gap = D_d - D_s.
usage: python3 nlterm.py gate | python3 nlterm.py Z ...   appends nlterm.jsonl (key Z), resumable.
"""
import sys,os,json,time,itertools,numpy as np
os.environ.setdefault("SIC_NOCLAMP","1"); os.environ.setdefault("SUBCELL","1")
import hfc2 as H; H.CORR=False
from t7c_kernel import C0
from t5_scf import ground_occ,minus
import ground as G
from hfterm import radial,E_open,E_avg,hund_det
OUT="nlterm.jsonl"
NAME={21:'Sc',39:'Y',57:'La',58:'Ce',64:'Gd',71:'Lu',72:'Hf',89:'Ac',90:'Th',91:'Pa',92:'U',96:'Cm',104:'Rf'}
TS="SPDFGHIKLMNO"

def channels(Z):
    N=max(n for n,l,k in G.expand(Z)); return {'d':(N-1,2),'s':(N,0),'f':(N-2,3)}

def opens(occ):
    return [(n,l,q) for n,l,q in occ if 1e-9<q<2*(2*l+1)-1e-9]

def dets(l,N):
    so=[(m,s) for m in range(l,-l-1,-1) for s in (+1,-1)]
    return list(itertools.combinations(so,N))

def diag_sum_terms(l,N,Fk1):
    """All (S,L) terms of l^N with their energies, by the Slater diagonal-sum rule.
    Fk1 = {k: F^k} for this shell. Returns list of (2S+1, L, E) sorted by E."""
    if N==0 or N==2*(2*l+1): return [(1,0,0.0)]
    D=dets(l,N); E={}; box={}
    for d in D:
        ML=sum(m for m,s in d); MS=sum(s for m,s in d)/2.0
        e=E_open([(l,N)],[(0,m,s) for m,s in d],{(0,0):Fk1},{(0,0):Fk1})
        box.setdefault((ML,MS),[]).append(e)
    cnt={k:len(v) for k,v in box.items()}; esum={k:sum(v) for k,v in box.items()}
    out=[]
    while True:
        live=[k for k,v in cnt.items() if v>0]
        if not live: break
        ML=max(k[0] for k in live); MS=max(k[1] for k in live if k[0]==ML)
        L,S=ML,MS
        e=esum[(ML,MS)]-sum(x for (mm,ss,x) in out if mm<=... ) if False else None
        # energy of this term = residual mean in its top block
        e=esum[(L,S)]/cnt[(L,S)] if cnt[(L,S)]==1 else None
        if e is None:
            # subtract already-extracted terms that reach this block, then average what's left
            reach=[(t,x) for (t,x) in _reaching(out,L,S)]
            e=(esum[(L,S)]-sum(x for _,x in reach))/(cnt[(L,S)]-len(reach))
        out.append((L,S,e))
        for mL in range(-L,L+1):
            for mS in np.arange(-S,S+1):
                k=(mL,round(float(mS),1))
                k=k if k in cnt else (mL,float(mS))
                if k in cnt: cnt[k]-=1; esum[k]-=e
        out[-1]=(L,S,e)
    return sorted([(int(2*S+1),L,e) for L,S,e in out],key=lambda t:t[2])

def _reaching(out,L,S):
    return [((l_,s_),x) for (l_,s_,x) in out if abs(L)<=l_ and abs(S)<=s_]

def term_label(mult,L): return f"{mult}{TS[L]}"

def state(Z,occ):
    h=H.HFC(Z,occ,c=C0); E,_,it,eps=h.run2()
    op=opens(occ); openk=[(n,l) for n,l,q in op]; shells=[(l,int(round(q))) for n,l,q in op]
    if not shells: return dict(E=float(E),it=it,dE=0.0,open=[],lowest=None,hund=None)
    Fk,Gk=radial(h,openk); so=hund_det(shells)
    dE=E_open(shells,so,Fk,Gk)-E_avg(shells,Fk,Gk)
    low=None
    big=[(i,(l,N)) for i,(l,N) in enumerate(shells) if 1<N<2*(2*l+1)-1]
    if len(big)==1:
        i,(l,N)=big[0]; ts=diag_sum_terms(l,N,Fk[(i,i)])
        low=[term_label(m,L) for m,L,_ in ts[:3]]
    hl=None
    if len(shells)>=1:
        Stot=sum(min(N,2*l+1)-max(N-(2*l+1),0) for l,N in shells)/2.0
        Ltot=sum(sum(list(range(l,-l-1,-1))[:min(N,2*l+1)])+sum(list(range(l,-l-1,-1))[:max(N-(2*l+1),0)]) for l,N in shells)
        hl=term_label(int(2*Stot+1),int(Ltot))
    return dict(E=float(E),it=it,dE=float(dE),open=[(n,l,q) for n,l,q in op],lowest=low,hund=hl)

if __name__=="__main__":
    a=sys.argv[1:]
    if a and a[0]=="gate":
        F={0:0.0,2:1.0,4:1.0}
        print("PT8 d2 :",[ (term_label(m,L),round(e,4)) for m,L,e in diag_sum_terms(2,2,F)])
        print("PT8 f2 :",[ (term_label(m,L),round(e,4)) for m,L,e in diag_sum_terms(3,2,{0:0.0,2:1.0,4:1.0,6:1.0})][:4])
        sys.exit()
    done={d['Z'] for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
    for Z in map(int,a):
        if Z in done: print("SKIP",Z); continue
        t0=time.time(); ch=channels(Z); occ0=ground_occ(Z)
        neu=state(Z,occ0); res={}
        for tag in ('d','s'):
            n,l=ch[tag]; res[tag]=state(Z,[(x,y,q) for x,y,q in minus(occ0,n,l,1.0) if q>0])
        o=dict(Z=Z,el=NAME.get(Z,str(Z)))
        for tag in ('d','s'):
            D=neu['E']-res[tag]['E']; Dt=D+neu['dE']-res[tag]['dE']
            o[f"D_{tag}"]=round(D,5); o[f"Dterm_{tag}"]=round(Dt,5); o[f"dE_{tag}"]=round(res[tag]['dE'],5)
            o[f"low_{tag}"]=res[tag]['lowest']; o[f"hund_{tag}"]=res[tag]['hund']
        o.update(dE_neu=round(neu['dE'],5),low_neu=neu['lowest'],hund_neu=neu['hund'],
                 gap_avg=round(o['D_d']-o['D_s'],5),gap_term=round(o['Dterm_d']-o['Dterm_s'],5),
                 it=[neu['it'],res['d']['it'],res['s']['it']],sec=int(time.time()-t0))
        open(OUT,"a").write(json.dumps(o)+"\n"); print(o,flush=True)
