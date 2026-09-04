from itertools import product
def R(X):
    X=list(X)
    if not X: return frozenset()
    d=len(X[0]); A=[sorted(set(x[i] for x in X)) for i in range(d)]
    def phi(i,j,t): return max(x[i] for x in X if x[j]<=t)
    PH={(i,j):{t:phi(i,j,t) for t in A[j]} for i in range(d) for j in range(d) if i!=j}
    return frozenset(x for x in product(*A) if all(x[i]<=PH[(i,j)][x[j]] for (i,j) in PH))
def box(dims): return list(product(*[range(k) for k in dims]))
def moore(U):
    n=len(U); closed=[]
    for m in range(1<<n):
        X=[U[k] for k in range(n) if m>>k&1]
        if R(X)==frozenset(X): closed.append(frozenset(X))
    return closed
def rates(closed,skip_empty):
    C=[c for c in closed if c or not skip_empty]
    pairs=[(a,b) for i,a in enumerate(C) for b in C[i+1:]]
    S=set(C)
    i_ok=sum(1 for a,b in pairs if (a&b) in S); u_ok=sum(1 for a,b in pairs if (a|b) in S)
    return len(C),len(pairs),100*i_ok/len(pairs),100*u_ok/len(pairs)
if __name__=='__main__':
    exec(open('tower-2.py').read().split("if __name__")[0]); L=L8()
    print('E(Λ8) =',len(R(L))-len(L))
    for dims in [(2,2),(3,2),(2,2,2),(3,3),(4,3),(2,2,3)]:
        U=box(dims); C=moore(U); n=len(U)
        print(dims,'|U|',n,'closed incl ∅',len(C),'excl ∅',len([c for c in C if c]),'E=2^n-|Cl|',2**n-len(C),
              '| rates incl ∅ (∩,∪): %.1f %.1f'%rates(C,False)[2:],'| excl ∅: %.1f %.1f'%rates(C,True)[2:])
