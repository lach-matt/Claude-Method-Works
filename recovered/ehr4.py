from fractions import Fraction as F
def counts4(N):
    c=s=0
    for a in range(N+1):
        for b in range(a,N+1):
            if 2*a < b: 
                sb=False
            else: sb=True
            for cc in range(b,N+1):
                st = sb and (3*b >= 2*cc)
                for d in range(cc,N+1):
                    if st and (4*cc >= 3*d): s+=1
                    if (a>=b-a) and (b-a>=cc-b) and (cc-b>=d-cc): c+=1
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
TOP=66
data=[]
for N in range(1,TOP+1):
    data.append((N,)+counts4(N))
print(f"n=4 counts computed to N={TOP}")
res={}
for name,idx in (("concave",1),("starshaped",2)):
    found=None
    for p in (1,2,3,4,6,12):
        for r in range(p):
            sub=[(x[0],x[idx]) for x in data if x[0]%p==r]
            if len(sub)<6: continue
            coef,ok=poly_fit(sub,4)
            if ok: found=(p,r,coef[4]); break
        if found: break
    res[name]=found
    print(f"  {name:<11} " + (f"period {found[0]}, class {found[1]}, "
          f"leading coefficient {found[2]}" if found else "no exact fit to period 12"))
if res["concave"] and res["starshaped"]:
    a=res["concave"][2]; b=res["starshaped"][2]
    print(f"  LIMIT = {a/b} = {float(a/b)*100:.4f}%   "
          f"(measured at N={TOP}: {100*data[-1][1]/data[-1][2]:.4f}%)")