import numpy as np, spglib, time
from collections import defaultdict

def K(M): return tuple(int(round(x)) for x in np.asarray(M).ravel())
I3=K(np.eye(3))

def _try_table(G, cls, N, seed):
    n, order = len(cls), len(G)
    A = np.tensordot(np.random.default_rng(seed).normal(size=n), N, axes=(0, 0))
    _w, V = np.linalg.eig(A)
    out = []
    for t in range(n):
        v = V[:, t]
        if abs(v[0]) < 1e-9:
            return None
        om = v / v[0]
        base = np.array([om[i] / len(cls[i]) for i in range(n)])
        s2 = sum(len(cls[i]) * abs(base[i]) ** 2 for i in range(n))
        if abs(s2) < 1e-12:
            return None
        chi = base * np.sqrt(order / s2)
        if np.real(chi[0]) < 0:
            chi = -chi
        out.append(chi)
    T = np.array(out)
    # VALIDATE: dims integral, sum of squares = |G|, rows orthonormal.
    dims = [complex(x[0]) for x in T]
    if any(abs(d.imag) > 1e-6 or abs(d.real - round(d.real)) > 1e-6 for d in dims):
        return None
    if abs(sum(round(d.real) ** 2 for d in dims) - order) > 1e-6:
        return None
    for r in range(n):
        for q in range(n):
            ip = sum(len(cls[i]) * T[r][i] * np.conj(T[q][i]) for i in range(n)) / order
            if abs(ip - (1.0 if r == q else 0.0)) > 1e-6:
                return None
    idx = sorted(range(n), key=lambda r: (round(T[r][0].real),
                                          [round(float(np.real(x)), 4) for x in T[r]]))
    return T[idx]


def char_table(G):
    """Burnside class-algebra, with the table VALIDATED before it is returned.

    A single random combination of the class-sum matrices can have near-
    degenerate eigenvalues, and numpy then returns mixed eigenvectors.  That
    produced 93 non-integral decompositions out of 1,145 on the first full
    sweep, concentrated in point groups of order 16 and 48.  The table is now
    checked for integral dimensions, sum(dim^2) = |G|, and row orthonormality,
    and the seed is retried until it passes.
    """
    idx = {K(M): i for i, M in enumerate(G)}
    seen, cls = set(), []
    for i, M in enumerate(G):
        if i in seen:
            continue
        c = sorted({idx[K(X @ M @ np.linalg.inv(X))] for X in G})
        cls.append(c); seen |= set(c)
    cls.sort(key=lambda c: 0 if K(G[c[0]]) == I3 else 1)
    n = len(cls)
    co = [0] * len(G)
    for ci, c in enumerate(cls):
        for g in c:
            co[g] = ci
    N = np.zeros((n, n, n))
    for i in range(n):
        for j in range(n):
            cnt = np.zeros(n)
            for a in cls[i]:
                for b in cls[j]:
                    cnt[co[idx[K(G[a] @ G[b])]]] += 1
            for k in range(n):
                N[i][j][k] = cnt[k] / len(cls[k])
    for seed in range(200):
        T = _try_table(G, cls, N, seed)
        if T is not None:
            return cls, T
    raise RuntimeError("no valid character table after 200 seeds, |G|=%d" % len(G))


def orbit(R,T,p):
    O=[]
    for Ri,ti in zip(R,T):
        q=tuple(np.round((Ri@p+ti)%1.0,6)%1.0)
        if q not in O: O.append(q)
    return np.array(O)

def mech_decomp(R,T,Grot,cls,Tab,pts):
    chi=[]
    for c in cls:
        Rr=Grot[c[0]]
        # find a full op whose rotation is Rr
        j=[k for k in range(len(R)) if K(R[k])==K(Rr)][0]
        q=(pts@R[j].T+T[j])%1.0
        # FIXED points: image of point i must equal point i, not merely land
        # somewhere in the orbit -- the orbit is closed, so the latter counts
        # every point and gave diamond the wrong character.
        d=np.abs(q-pts); d=np.minimum(d,1-d)
        n=int(np.sum(np.all(d<1e-4,axis=1)))
        chi.append(n*np.trace(Rr))
    chi=np.array(chi,float)
    m=[float(np.real(sum(len(cls[i])*chi[i]*np.conj(Tab[r][i])
       for i in range(len(cls)))/len(Grot))) for r in range(len(Tab))]
    return chi,m

# --- validate: compose each archetype from its occupied sites ----------------
FCC=[[0,0,0],[0,.5,.5],[.5,0,.5],[.5,.5,0]]
off=lambda b,d:[[(x+d[0])%1,(y+d[1])%1,(z+d[2])%1] for x,y,z in b]
CASES={
 "diamond (Si)":((np.eye(3)*5.43,FCC+off(FCC,(.25,.25,.25)),[14]*8),"T2g + T1u",6),
 "rocksalt (NaCl)":((np.eye(3)*5.64,FCC+off(FCC,(.5,.5,.5)),[11]*4+[17]*4),"2 T1u",6),
 "zincblende (GaAs)":((np.eye(3)*5.65,FCC+off(FCC,(.25,.25,.25)),[31]*4+[33]*4),"2 T2",6),
 "fluorite (CaF2)":((np.eye(3)*5.46,FCC+off(FCC,(.25,.25,.25))+off(FCC,(.75,.75,.75)),
                     [20]*4+[9]*8),"T2g + 2 T1u",9),
 "perovskite (SrTiO3)":((np.eye(3)*3.905,[[0,0,0],[.5,.5,.5],[0,.5,.5],[.5,0,.5],[.5,.5,0]],
                     [38,22,8,8,8]),"4 T1u + T2u",15),
 "CsCl":((np.eye(3)*4.12,[[0,0,0],[.5,.5,.5]],[55,17]),"2 T1u",6),
}
print("VALIDATION: build each archetype as a SUM OVER ITS OCCUPIED SITE ORBITS\n")
for nm,(cell,lit,expm) in CASES.items():
    prim=spglib.standardize_cell(cell,to_primitive=True,symprec=1e-5)
    sym=spglib.get_symmetry(prim,symprec=1e-5)
    R=np.asarray(sym['rotations']); T=np.asarray(sym['translations'])%1.0
    seen={}; Grot=[]
    for Ri in R:
        if K(Ri) not in seen: seen[K(Ri)]=1; Grot.append(np.asarray(Ri,float))
    cls,Tab=char_table(Grot)
    dims=[int(round(float(np.real(t[0])))) for t in Tab]
    # group primitive atoms into orbits
    pos=np.asarray(prim[1]); nums=list(prim[2])
    used=set(); total=[0]*len(Tab); nsite=0
    for i in range(len(pos)):
        if i in used: continue
        O=orbit(R,T,pos[i])
        for j in range(len(pos)):
            d=np.abs(O-pos[j]); d=np.minimum(d,1-d)
            if np.any(np.all(d<1e-4,axis=1)): used.add(j)
        _c,m=mech_decomp(R,T,Grot,cls,Tab,O); nsite+=1
        total=[a+b for a,b in zip(total,m)]
    tot=sum(d*round(mm) for d,mm in zip(dims,total))
    exact=all(abs(mm-round(mm))<1e-6 for mm in total)
    terms=" + ".join("%d x d%d"%(round(mm),d) for d,mm in zip(dims,total) if round(mm))
    print("%-21s %d site-orbit(s)  %-22s %2d/%2d modes  exact=%s   [%s]"
          % (nm,nsite,terms,tot,expm,exact,lit))
