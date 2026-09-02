# r2-ch2.py — Phase R2, main Chapter 2 (chat 69). Re-measures Chapter 2's tower-measurable figures on the
# rebuilt tower (tower-2.py beside it). Every printed line is MEASURED; the read decides.
import importlib.util, itertools, numpy as np
spec=importlib.util.spec_from_file_location('tower','tower-2.py'); tw=importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
L8=tw.L8(); S8=set(L8); L9=tw.L9(); S9=set(L9); L13=tw.L13()
def E0(X):
    A=np.array(sorted(X),dtype=np.int16); Xs=set(map(tuple,A.tolist()))
    J=np.maximum(A[:,None,:],A[None,:,:]).reshape(-1,A.shape[1]); Mn=np.minimum(A[:,None,:],A[None,:,:]).reshape(-1,A.shape[1])
    return set(map(tuple,J.tolist()))<=Xs and set(map(tuple,Mn.tolist()))<=Xs
print('|Λ9| =',len(L9),'; E(Λ9) = 0 (join/meet of all pairs in Λ9):',E0(L9),'; projection of Λ9 onto its first 8 coordinates == Λ8:',set(c[:8] for c in L9)==S8, '(L769–770)')
for name,X,d in (('Λ8',L8,8),('Λ9',L9,9)):
    s=[sum(c) for c in X]; b=min(s)
    print('%s: F(−1) with rank = Σx_i: %d ; with graded rank Σx_i − %d: %d  (L771 "F(−1) = 2 unchanged")'%(name,sum((-1)**v for v in s),b,sum((-1)**(v-b) for v in s)))
# join-irreducibles of Λ8 (exactly one lower cover), covers among them, Birkhoff down-sets
def leq(a,b): return all(x<=y for x,y in zip(a,b))
def lower_covers(c):
    below=[d for d in L8 if d!=c and leq(d,c)]
    return [d for d in below if not any(e!=d and e!=c and leq(d,e) and leq(e,c) for e in below)]
J=[c for c in L8 if len(lower_covers(c))==1]
print('|J(Λ8)| =',len(J),'(L852 "|J(Λ)| = 17"; L8517 "|J(Λ)| = 17 = height")')
Jc=[(a,b) for a in J for b in J if a!=b and leq(a,b) and not any(e!=a and e!=b and leq(a,e) and leq(e,b) for e in J)]
print('covering relations within J(Λ8):',len(Jc),'(L853 "twenty covering relations"; L854–855 "twenty implications")')
idx={c:i for i,c in enumerate(J)}; up={i:[idx[b] for (a,b) in Jc if a==J[i]] for i in range(len(J))}
downsets=0
for mask in range(1<<len(J)):
    ok=True
    for i in range(len(J)):
        if mask>>i&1:
            for (a,b) in Jc:
                if b==J[i] and not (mask>>idx[a]&1): ok=False; break
            if not ok: break
    downsets+=ok
print('down-sets of J(Λ8) (Birkhoff):',downsets,'of 2^%d = %d words (L853 "976"; L855 "131,072 words to 976")'%(len(J),1<<len(J)))
A=np.array(L8); sizes=[len(set(A[:,i])) for i in range(8)]
print('alphabet Σ(|A_i| − 1) =',sum(s-1 for s in sizes),'from |A_i| =',sizes,'(L853 "17")')
B=np.array(L13); box=int(np.prod([B[:,i].max()-B[:,i].min()+1 for i in range(13)]))
print('ambient box of Λ13 = ∏ ranges =',box,'(L856, L993 "47,775,744"); Λ8 box =',int(np.prod([A[:,i].max()-A[:,i].min()+1 for i in range(8)])))
