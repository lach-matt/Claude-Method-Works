from fractions import Fraction as F
def enum(n,N):
    c=s=0; stack=[[]]
    while stack:
        S=stack.pop(); k=len(S)
        if k==n:
            d=[S[0]]+[S[i]-S[i-1] for i in range(1,n)]
            if all(S[i]*(i+2)>=S[i+1]*(i+1) for i in range(n-1)): s+=1
            if all(d[i]>=d[i+1] for i in range(n-1)): c+=1
            continue
        lo=S[-1] if S else 0
        for v in range(lo,N+1): stack.append(S+[v])
    return c,s
def poly_fit(pts,deg):
    xs=[F(x) for x,_ in pts[:deg+1]]; ys=[F(y) for _,y in pts[:deg+1]]
    m=deg+1
    A=[[xs[i]**j for j in range(m)]+[ys[i]] for i in range(m)]
    for i in range(m):
        p=next(r for r in range(i,m) if A[r][i]!=0); A[i],A[p]=A[p],A[i]
        piv=A[i][i]; A[i]=[a/piv for a in A[i]]
        for r in range(m):
            if r!=i and A[r][i]!=0:
                f=A[r][i]; A[r]=[a-f*b for a,b in zip(A[r],A[i])]
    coef=[A[i][m] for i in range(m)]
    ok=all(sum(coef[j]*F(x)**j for j in range(m))==F(y) for x,y in pts)
    return coef,ok
for n,top in ((2,60),(3,44),(4,26)):
    data=[(N,)+enum(n,N) for N in range(1,top+1)]
    res={}
    for name,idx in (("concave",1),("starshaped",2)):
        found=None
        for p in (1,2,3,4,6,12):
            sub=[(N,d[idx]) for N,*d0 in [(x[0],x[1],x[2]) for x in data]
                 for d in [ (None,x[1],x[2]) ] if False]  # placeholder
            sub=[(x[0],x[idx]) for x in data if x[0]%p==1%p or p==1]
            sub=[(x[0],x[idx]) for x in data if x[0]%p==(1%p)]
            if len(sub)<n+2: continue
            coef,ok=poly_fit(sub,n)
            if ok: found=(p,coef[n]); break
        res[name]=found
        if found: print(f"n={n} {name:<11} quasi-period {found[0]}, degree {n}, "
                        f"leading coefficient {found[1]}")
        else: print(f"n={n} {name:<11} no fit found")
    if res["concave"] and res["starshaped"]:
        a=res["concave"][1]; b=res["starshaped"][1]
        print(f"      LIMIT = {a}/{b} = {a/b} = {float(a/b)*100:.4f}%"
              f"   (measured at N={top}: {100*data[-1][1]/data[-1][2]:.4f}%)")
    print()