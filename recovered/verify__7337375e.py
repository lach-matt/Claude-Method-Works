import itertools, json, random
from gen import build
X=build(3,3,1,3,1, lambda k:0, False)
XS=set(X)
def Rn_set_count(S,d=8):
    S=list(S); A=[sorted({c[i] for c in S}) for i in range(d)]
    def env(i,j):
        m={}
        for c in S: m[c[j]]=max(m.get(c[j],-10**9),c[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return sum(1 for x in itertools.product(*A)
               if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j))
D=json.load(open("covers8.json"))
covers=[[tuple(c) for c in cv] for cv in D["covers"]]
# the recorded corners (bit-word identified):
c3=(2,1,3,3,2,1,3,0)
def is_c1(c): return c[0]==1 and c[1]==0 and c[4]==3 and c[5]==1        # 0 0 · · 1 1 · ·
def is_c4(c): return c==(3,1,1,0,3,1,0,0)                              # 11001100
random.seed(11)
sample=random.sample(covers,200)
bad=[cv for cv in sample if Rn_set_count(cv)!=976]
print("sample 200 exact covers vs sealed Rn: failures =",len(bad))
no_c1=[cv for cv in covers if not any(is_c1(c) for c in cv)]
no_c4=[cv for cv in covers if not any(is_c4(c) for c in cv)]
print("covers lacking ANY corner-1-type cell:",len(no_c1))
print("covers lacking the 11001100 cell:",len(no_c4))
for name,pool in [("no-corner1",no_c1),("no-11001100",no_c4)]:
    if pool:
        r=Rn_set_count(pool[0])
        print(f"  sealed Rn on one {name} cover -> |R| = {r} ({'PASS closes to 976' if r==976 else 'FAIL'})")
        print("   cover:",pool[0])