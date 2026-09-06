import sys, random; sys.path.insert(0,"/home/claude/method")
from itertools import product
import violations as V
random.seed(7)
# is E=0 a fact about the physics, or about binary coordinates?
# test: random subsets of the box, and Horn-closed families over random implications
box=list(product([0,1],repeat=8))
print("random subsets of {0,1}^8, no implication structure at all:")
for n in (20,40,57,80):
    Es=[]
    for _ in range(25):
        X=set(random.sample(box,n)); Es.append(len(V.RR(X,8))-len(X))
    print(f"  |X|={n:3d}  E ranges {min(Es)} .. {max(Es)}   zero in {sum(1 for e in Es if e==0)}/25")
print("\nfamilies closed under RANDOM implication sets:")
for trial in range(6):
    imp=random.sample([(a,b) for a in V.LAWS for b in V.LAWS if a!=b], random.randint(4,12))
    def cl(S):
        S=set(S); g=True
        while g:
            g=False
            for a,b in imp:
                if a in S and b not in S: S.add(b); g=True
        return V.vec(S)
    X={cl(set(c)) for c in [ [l for l,v in zip(V.LAWS,x) if v] for x in box ]}
    print(f"  {len(imp):2d} implications -> |X|={len(X):3d}  E={len(V.RR(X,8))-len(X)}")