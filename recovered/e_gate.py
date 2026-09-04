import itertools
from gen import build
def Rn_count(X,d=8):
    X=list(X); A=[sorted({c[i] for c in X}) for i in range(d)]
    def env(i,j):
        m={}
        for c in X: m[c[j]]=max(m.get(c[j],-10**9),c[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return sum(1 for x in itertools.product(*A)
               if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j))
X=build(3,3,1,3,1, lambda k:0, False)
print("cells:",len(X),"| R(X):",Rn_count(X),"| E =",Rn_count(X)-len(X))