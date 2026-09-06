L="spdfg"
# (core name, species, charge, next diagonal M, {l: delta}, provenance)
CASES=[
 ("Ar","K I",1,5,{2:0.246,1:1.727,0:2.191},"COORDINATES measured"),
 ("Kr","Rb I",1,6,{3:0.0143,2:1.3307,1:2.6566,0:3.1357},"REGISTER R 1258"),
 ("Kr","Sr II",2,6,{3:0.062,2:1.458,1:2.35,0:2.711},"COORDINATES measured"),
 ("Xe","Cs I",1,7,{3:0.033,2:2.466,1:3.593,0:4.051},"COORDINATES measured"),
 ("Xe","Ba II",2,7,{3:0.756,2:2.415,1:3.241,0:3.598},"COORDINATES measured"),
]
for core,sp,c,M,dl,prov in CASES:
    pts=sorted([(M-l-l-1, M-l, l, dl[l]) for l in dl if M-l>=l+1])
    print(f"\n{sp:<6} ({core} core, charge {c})  diagonal n+l={M}   [{prov}]")
    print("    "+"  ".join(f"{n}{L[l]}:δ={d:.3f}" for p,n,l,d in pts))
    inc=[round(pts[i+1][3]-pts[i][3],3) for i in range(len(pts)-1)]
    print(f"    increments in p: {inc}   {'monotone decreasing -> CONCAVE' if all(inc[i]>inc[i+1] for i in range(len(inc)-1)) else 'NOT concave'}")
    # entrant order by n - a*delta at a=1 (pure one-electron n*)
    order=sorted(pts,key=lambda t:t[1]-t[3])
    print("    n* order (a=1):", " < ".join(f"{n}{L[l]}" for p,n,l,d in order))
    for i,(p,n,l,d) in enumerate(pts):
        lo,hi=-1e9,1e9
        for j,(q,m,k,e) in enumerate(pts):
            if j==i: continue
            if e-d>1e-9: hi=min(hi,(m-n)/(e-d))
            elif e-d<-1e-9: lo=max(lo,(m-n)/(e-d))
        print(f"       {n}{L[l]} first iff {max(lo,-9):6.3f} < a < {min(hi,9):6.3f}" if lo<hi else f"       {n}{L[l]} never first")