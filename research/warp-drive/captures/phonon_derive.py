#!/usr/bin/env python3
"""
phonon_derive.py -- the derivation behind captures/PHONON-SITES.tsv, as ONE
self-contained module.

    python3 phonon_derive.py        rebuild the capture

Needs numpy and spglib, neither vendored.  Importable: `phonondex.py --derive`
runs it, and the k-point extension imports `primitive_ops` and `char_table`
from here rather than copying them.

CONSOLIDATED 2026-09-20.  The first banked version was three files chained by
`exec(open('build.py'))` and `exec(open('prim.py'))` -- scratchpad names that do
not exist in this directory, so THE BANKED DERIVATION WAS NOT RUNNABLE FROM THE
REPOSITORY.  A first attempt to repair it with `__file__` inside the exec made
it worse: inside exec'd text `__file__` is the OUTER file's, so the chain
recursed into itself.  Both are recorded here rather than quietly fixed.
"""
import numpy as np
import spglib
import time
import sys
import collections

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



def hallmap():
    m={}
    for h in range(1,531):
        t=spglib.get_spacegroup_type(h); n=t.number if hasattr(t,'number') else t['number']
        m.setdefault(n,h)
    return m

def hnf_basis(vecs, D=24):
    """Basis of the lattice generated by Z^3 and the given fractional vectors.

    Columns of the returned P are the primitive vectors in CONVENTIONAL
    fractional coordinates.
    """
    M=np.vstack([np.eye(3)*D, np.round(np.asarray(vecs)*D)]).astype(np.int64)
    # column-style HNF by integer row reduction on the transpose
    A=M.T.copy()                                   # 3 x N
    piv=[]
    r=0
    for c in range(3):
        # find a row r..2 with nonzero entry in some column, use gcd elimination
        while True:
            nz=[j for j in range(A.shape[1]) if A[r,j]!=0]
            if not nz: break
            j0=min(nz,key=lambda j:abs(A[r,j]))
            for j in nz:
                if j==j0: continue
                q=A[r,j]//A[r,j0]
                A[:,j]-=q*A[:,j0]
            nz2=[j for j in range(A.shape[1]) if A[r,j]!=0 and j!=j0]
            if not nz2:
                A[:,[c,j0]]=A[:,[j0,c]]
                break
        r+=1
    P=A[:,:3].astype(float)/D
    if abs(np.linalg.det(P))<1e-9: raise RuntimeError("degenerate primitive basis")
    return P

def primitive_ops(sg,HN):
    d=spglib.get_symmetry_from_database(HN[sg])
    R=np.asarray(d['rotations']); T=np.asarray(d['translations'])%1.0
    I=K(np.eye(3))
    C=[T[i] for i in range(len(R)) if K(R[i])==I]
    P=hnf_basis(C)
    Pi=np.linalg.inv(P)
    out={}
    for Ri,ti in zip(R,T):
        Rp=Pi@Ri@P; tp=(Pi@ti)%1.0
        Rr=np.rint(Rp)
        if np.max(np.abs(Rp-Rr))>1e-6: raise RuntimeError("non-integer rotation in primitive basis")
        key=(K(Rr), tuple(int(round(x*24))%24 for x in tp))
        out[key]=(Rr,tp)
    return P, [v[0] for v in out.values()], [v[1] for v in out.values()], len(C)



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


def main():
    HN=hallmap(); rows=[]    ; bad=[]; t0=time.time()
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

if __name__ == "__main__":
    main()
