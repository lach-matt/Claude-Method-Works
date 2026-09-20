import numpy as np, spglib, time, sys, collections
exec(open('prim.py').read().split('HN=hallmap()\nprint(')[0])

def system(sg):
    for lim,nm in ((2,"triclinic"),(15,"monoclinic"),(74,"orthorhombic"),
                   (142,"tetragonal"),(167,"trigonal"),(194,"hexagonal"),(230,"cubic")):
        if sg<=lim: return nm

def site_types(R,T,denom=12):
    g=np.arange(denom)/denom
    P=np.array([[x,y,z] for x in g for y in g for z in g])
    fix=np.zeros((len(P),len(R)),bool)
    for i,(Ri,ti) in enumerate(zip(R,T)):
        q=(P@Ri.T+ti)%1.0; d=(q-P)%1.0; d=np.minimum(d,1-d)
        fix[:,i]=np.all(d<1e-6,axis=1)
    out={}
    for j in range(len(P)):
        out.setdefault(frozenset(np.flatnonzero(fix[j]).tolist()), P[j])
    return out

def conj_canon(R,T,subs):
    idx={(K(R[i]),tuple(int(round(x*24))%24 for x in T[i])):i for i in range(len(R))}
    canon={}
    for S in subs:
        best=None
        for gi in range(len(R)):
            Rg,tg=R[gi],T[gi]
            Rgi=np.rint(np.linalg.inv(Rg)).astype(int); tgi=(-Rgi@tg)%1.0
            img=set(); ok=True
            for s in S:
                A=Rg@R[s]; a=(Rg@T[s]+tg)%1.0
                B=A@Rgi; b=(A@tgi+a)%1.0
                k=(K(B),tuple(int(round(x*24))%24 for x in b))
                if k not in idx: ok=False; break
                img.add(idx[k])
            if ok:
                t=tuple(sorted(img))
                if best is None or t<best: best=t
        canon[S]=best
    g={}
    for S,c in canon.items(): g.setdefault(c,[]).append(S)
    return g

HN=hallmap(); rows=[]; bad=[]; t0=time.time()
CACHE={}
for sg in range(1,231):
    P,R,T,nc = primitive_ops(sg,HN)
    R=[np.asarray(x,float) for x in R]; T=[np.asarray(x,float) for x in T]
    Rn=np.array(R); Tn=np.array(T)
    subs=site_types(Rn,Tn)
    groups=conj_canon(Rn,Tn,list(subs.keys()))
    # NO CACHE.  A cache keyed on the sorted rotation SET is wrong: `cls`
    # holds indices into the UNSORTED list, so reusing a table between two
    # space groups with the same point group but a different operation order
    # corrupts it.  That produced 90 non-integral rows out of 1,120.
    cls,Tab=char_table(R)
    dims=[int(round(float(np.real(x[0])))) for x in Tab]
    for canon,mem in sorted(groups.items(), key=lambda kv:(-len(kv[0]),kv[0])):
        S=mem[0]; p=subs[S]
        O=[]
        for Ri,ti in zip(R,T):
            q=(Ri@p+ti)%1.0
            if all(np.max(np.minimum(np.abs(q-o),1-np.abs(q-o)))>1e-4 for o in O): O.append(q)
        O=np.array(O)
        chi=[]
        for c in cls:
            Rr=R[c[0]]; tt=T[c[0]]
            q=(O@Rr.T+tt)%1.0; d=np.abs(q-O); d=np.minimum(d,1-d)
            chi.append(int(np.sum(np.all(d<1e-4,axis=1)))*np.trace(Rr))
        chi=np.array(chi,float)
        m=[float(np.real(sum(len(cls[i])*chi[i]*np.conj(Tab[r][i])
           for i in range(len(cls)))/len(R))) for r in range(len(Tab))]
        if not all(abs(x-round(x))<1e-6 for x in m): bad.append((sg,len(S),"nonint")); continue
        mr=[int(round(x)) for x in m]
        modes=sum(dm*mm for dm,mm in zip(dims,mr))
        if modes!=3*len(O): bad.append((sg,len(S),"modes %d vs %d"%(modes,3*len(O)))); continue
        rows.append((sg,system(sg),len(R),len(S),len(O),modes,
                     sum(1 for x in mr if x),
                     "+".join("%dx%d"%(mm,dm) for dm,mm in zip(dims,mr) if mm)))
    if sg%50==0: print("  sg %d  %.0fs  %d rows  %d bad"%(sg,time.time()-t0,len(rows),len(bad)),file=sys.stderr)
print("\nswept 230 space groups in %.1f s"%(time.time()-t0),file=sys.stderr)
print("site types seated : %d"%len(rows),file=sys.stderr)
print("failures          : %d  %s"%(len(bad),collections.Counter(b[2] for b in bad)),file=sys.stderr)
with open("PHONON-SITES.tsv","w") as f:
    f.write("sg\tsystem\tpg_order\tsite_order\tmultiplicity\tmodes\tn_irreps\tdecomposition\n")
    for r in rows: f.write("\t".join(str(x) for x in r)+"\n")
print("wrote PHONON-SITES.tsv",file=sys.stderr)
