"""ci2b.py -- s73. THE FULL TEST: CI-2, CI-6 over all ten s<->d rows, CI-7.
Extends pack73/ci2.py. Same Slater-Condon single replacement, same sealed ck / Yk.

REPRESENTATIVE FREEDOM IS REMOVED BY ENUMERATION, NOT BY CHOICE.
ci2.py picked one determinant pair per row. For N != 5 that choice is not unique, and a
chosen representative is a design decision made by the assistant. Instead: enumerate EVERY
pair (A-det from config A, B-det from config B) that shares (M_L,M_S) and differs by exactly
one spin-orbital. The constraint solves itself -- the replaced orbital must be d(m=0) with
spin opposite to the s electron -- so the enumeration is exact and finite.
Reported: count, max|V|, min|V|. The floor test uses max|V|: "is the coupling alive anywhere
in the shared sector". No representative is chosen by hand.

CI-2 CONTROL: the same V with the OPEN spectator shell SPHERICALLY AVERAGED (every m equally
weighted, q/(2(2l+1)) each) -- the L4 field exactly as the walk solves it. Predicted ZERO.
CI-7 CONTROL: 2x2 with S=I (derived, RULINGS-S73), diagonalised; lower root <= min(E_A,E_B).

Pd 46 is NOT a single replacement: 4d10 vs 4d8 5s2 differ by TWO spin-orbitals. Handled by
the double-replacement rule, which is a DIFFERENT clause of Slater-Condon, and flagged.
No constant beyond c.
"""
import sys, os, json, time, itertools, numpy as np
from t7c_hfsr import HFSR
from t7c_kernel import C0
from t5_scf import ground_occ
from hfterm import ck

FLOOR = 5e-5
OUT = "ci2b.jsonl"

# ---- rows: A = the sealed generator's configuration; B = one electron moved d -> s
ROWS = {24:('Cr',3,2,4,0), 29:('Cu',3,2,4,0), 41:('Nb',4,2,5,0), 42:('Mo',4,2,5,0),
        44:('Ru',4,2,5,0), 45:('Rh',4,2,5,0), 46:('Pd',4,2,5,0), 47:('Ag',4,2,5,0),
        78:('Pt',5,2,6,0), 79:('Au',6-1,2,6,0)}
ROWS[79] = ('Au',5,2,6,0)

def occ_of(Z):
    """(occA, occB, nd, ns) -- B moves as many electrons d->s as A is short of the s2 shell."""
    A = {(n,l):q for n,l,q in ground_occ(Z)}
    el,nd,ld,ns,ls = ROWS[Z]
    qd = A.get((nd,ld),0); qs = A.get((ns,ls),0)
    k = 2 - qs                                    # electrons to move, 1 normally, 2 at Pd
    B = dict(A); B[(nd,ld)] = qd - k; B[(ns,ls)] = qs + k
    f = lambda D: sorted([(n,l,q) for (n,l),q in D.items() if q>0])
    return f(A), f(B), (nd,ld), (ns,ls), k

def spinorbs(occ):
    so=[]
    for (n,l,q) in occ:
        q=int(round(q)); ml=list(range(l,-l-1,-1)); up=min(q,2*l+1); dn=q-up
        so += [(n,l,m,+1) for m in ml[:up]] + [(n,l,m,-1) for m in ml[:dn]]
    return so

# ---- radial, cached
class Rad:
    def __init__(self,h): self.h=h; self.c={}
    def __call__(self,a,b,cc,d,kap):
        k=(a,b,cc,d,kap)
        if k not in self.c:
            h=self.h
            self.c[k]=float(np.sum(h.P[a]*h.P[cc]*h.Yk(h.P[b],h.P[d],kap)/h.r*h.dr))
        return self.c[k]

def V1(rad, common, A, B, KMAX=8):
    """single replacement A->B. common: list of (n,l,m,ms) or (n,l,m,ms,w) with weight w."""
    (na,la,ma,sa),(nb,lb,mb,sb) = A,B
    if sa!=sb: return 0.0
    V=0.0
    for t in common:
        nk,lk,mk,sk = t[:4]; w = t[4] if len(t)>4 else 1.0
        if w==0.0: continue
        for kap in range(KMAX+1):
            cD = ck(la,ma,lb,mb,kap)*ck(lk,mk,lk,mk,kap)
            if cD: V += w*cD*rad((na,la),(nk,lk),(nb,lb),(nk,lk),kap)
            if sk==sa:
                cX = ck(la,ma,lk,mk,kap)*ck(lb,mb,lk,mk,kap)
                if cX: V -= w*cX*rad((na,la),(nk,lk),(nk,lk),(nb,lb),kap)
    return V

def V2(rad, A1,A2, B1,B2, KMAX=8):
    """double replacement (A1,A2)->(B1,B2):  <ab|g|cd> - <ab|g|dc>."""
    def el(a,b,c,d):
        (na,la,ma,sa),(nb,lb,mb,sb),(nc,lc,mc,sc),(nd,ld,md,sd)=a,b,c,d
        if sa!=sc or sb!=sd: return 0.0
        v=0.0
        for kap in range(KMAX+1):
            cc = ck(la,ma,lc,mc,kap)*ck(ld,md,lb,mb,kap)
            if cc: v += cc*rad((na,la),(nb,lb),(nc,lc),(nd,ld),kap)
        return v
    return el(A1,A2,B1,B2) - el(A1,A2,B2,B1)

def pairs(Z, occA, dk, sk):
    """Every (A-det, B-det) sharing (M_L,M_S) and differing by exactly one spin-orbital.
    Forced: replaced = d(m=0, spin -sigma), added = s(m=0, spin -sigma), s electron = spin sigma."""
    nd,ld = dk; ns,ls = sk
    core = [t for t in spinorbs(occA) if (t[0],t[1]) not in (dk,sk)]
    N = {(n,l):q for n,l,q in occA}[dk]
    dso = [(nd,ld,m,s) for m in range(ld,-ld-1,-1) for s in (+1,-1)]
    out=[]
    for sig in (+1,-1):
        a = (nd,ld,0,-sig); b = (ns,ls,0,-sig)
        rest = [t for t in dso if t!=a]
        for combo in itertools.combinations(rest, int(N)-1):
            common = core + list(combo) + [(ns,ls,0,sig)]
            out.append((common,a,b))
    return out

def averaged_common(occA, dk, sk, sig):
    """Spectator set with the OPEN shell spherically averaged: every (m,ms) at weight q/cap."""
    out=[]
    for (n,l,q) in occA:
        cap=2*(2*l+1)
        if (n,l)==sk:
            out.append((n,l,0,sig,1.0)); continue
        w=q/cap
        for m in range(l,-l-1,-1):
            for s in (+1,-1): out.append((n,l,m,s,w))
    return out

def run(Z):
    el,nd,ld,ns,ls = ROWS[Z]; occA,occB,dk,sk,k = occ_of(Z)
    t0=time.time()
    hA=HFSR(Z,occA,c=C0); _,EA,_,_ = hA.run('hf',qtail=1)
    hB=HFSR(Z,occB,c=C0); _,EB,_,_ = hB.run('hf',qtail=1)
    rad=Rad(hA)
    o=dict(Z=Z,el=el,k=k,occA=[list(t) for t in occA],occB=[list(t) for t in occB],
           EA=float(EA),EB=float(EB))
    if k==2:
        # Pd: double replacement. A extras (m,+),(-m,-); B extras s(0,+),s(0,-)
        vs=[]
        for m in range(ld,-ld-1,-1):
            A1=(nd,ld,m,+1); A2=(nd,ld,-m,-1); B1=(ns,ls,0,+1); B2=(ns,ls,0,-1)
            vs.append(abs(V2(rad,A1,A2,B1,B2)))
        o.update(kind='double', npair=len(vs), Vmax=max(vs), Vmin=min(vs), Vavg=None)
    else:
        P=pairs(Z,occA,dk,sk)
        vs=[abs(V1(rad,c,a,b)) for c,a,b in P]
        # CI-2: same replacement, spherically averaged spectator
        av=[abs(V1(rad,averaged_common(occA,dk,sk,sig),(nd,ld,0,-sig),(ns,ls,0,-sig)))
            for sig in (+1,-1)]
        o.update(kind='single', npair=len(vs), Vmax=max(vs), Vmin=min(vs), Vavg=max(av))
    # CI-7: 2x2 with S=I
    V=o['Vmax']; H=np.array([[o['EA'],V],[V,o['EB']]])
    w=np.linalg.eigvalsh(H)
    o.update(lower=float(w[0]), minE=min(o['EA'],o['EB']),
             ci7=bool(w[0] <= min(o['EA'],o['EB'])+1e-12),
             clears=bool(o['Vmax']>FLOOR), sec=int(time.time()-t0))
    return o

if __name__=="__main__":
    Zs=[int(a) for a in sys.argv[1:]]
    done={json.loads(x)['Z'] for x in open(OUT)} if os.path.exists(OUT) else set()
    for Z in Zs:
        if Z in done: print("SKIP",Z,flush=True); continue
        o=run(Z); open(OUT,"a").write(json.dumps(o)+"\n")
        av='-' if o['Vavg'] is None else f"{o['Vavg']*1e3:.2e}"
        print(f"{o['el']:>3} Z={Z:<3} {o['kind']:<6} pairs={o['npair']:<4} "
              f"|V|max={o['Vmax']*1e3:8.4f} mHa  |V|min={o['Vmin']*1e3:8.4f}  "
              f"avgd={av:>9}  {'CLEARS' if o['clears'] else 'BELOW '}  CI7={o['ci7']}  {o['sec']}s",
              flush=True)
