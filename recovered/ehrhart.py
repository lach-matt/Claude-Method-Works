from fractions import Fraction as F
def counts(n,N):
    """concave and starshaped lattice points with 0 <= S_1 <= ... <= S_n <= N"""
    c=s=0
    def rec(S):
        nonlocal c,s
        k=len(S)
        if k==n:
            d=[S[0]]+[S[i]-S[i-1] for i in range(1,n)]
            if all(d[i]>=d[i+1] for i in range(n-1)): 
                nonlocal_c()
            return
        lo=S[-1] if S else 0
        for v in range(lo,N+1): rec(S+[v])
    # direct nested loops are faster; do it explicitly per n
    return None
def enum(n,N):
    c=s=0
    stack=[[]]
    while stack:
        S=stack.pop()
        k=len(S)
        if k==n:
            d=[S[0]]+[S[i]-S[i-1] for i in range(1,n)]
            conc=all(d[i]>=d[i+1] for i in range(n-1))
            star=all(S[i]*(i+2)>=S[i+1]*(i+1) for i in range(n-1))
            if star: s+=1
            if conc: c+=1
            continue
        lo=S[-1] if S else 0
        for v in range(lo,N+1): stack.append(S+[v])
    return c,s

def fit(vals, deg):
    """exact polynomial interpolation through the last deg+1 points; verify on the rest"""
    import itertools
    pts=vals[-(deg+1):]
    xs=[p[0] for p in pts]; ys=[F(p[1]) for p in pts]
    # Lagrange -> coefficients via solving Vandermonde with Fractions
    m=len(xs)
    A=[[F(x)**j for j in range(m)]+[ys[i]] for i,x in enumerate(xs)]
    for i in range(m):
        p=next(r for r in range(i,m) if A[r][i]!=0)
        A[i],A[p]=A[p],A[i]
        piv=A[i][i]
        A[i]=[a/piv for a in A[i]]
        for r in range(m):
            if r!=i and A[r][i]!=0:
                f=A[r][i]; A[r]=[a-f*b for a,b in zip(A[r],A[i])]
    coef=[A[i][m] for i in range(m)]
    ok=all(sum(coef[j]*F(x)**j for j in range(m))==F(y) for x,y in vals)
    return coef, ok

for n in (2,3,4):
    data=[]
    top = 34 if n<=3 else 20
    for N in range(1,top+1):
        c,s=enum(n,N); data.append((N,c,s))
    cc=[(N,c) for N,c,s in data]; ss=[(N,s) for N,c,s in data]
    for name,vals in (("concave",cc),("starshaped",ss)):
        for deg in range(n, n+3):
            coef,ok=fit(vals,deg)
            if ok:
                lead=coef[deg]
                print(f"n={n} {name:<11} exact polynomial of degree {deg}, "
                      f"leading coefficient {lead}")
                if name=="concave": lc=lead
                else: ls=lead
                break
        else:
            print(f"n={n} {name:<11} no exact polynomial up to degree {n+2} "
                  f"— quasi-polynomial, period > 1")
            lc=ls=None
    if lc is not None and ls is not None:
        print(f"      LIMITING DENSITY = {lc}/{ls} = {lc/ls} = {float(lc/ls)*100:.4f}%")
        print(f"      measured at N={data[-1][0]}: {100*data[-1][1]/data[-1][2]:.4f}%")
    print()