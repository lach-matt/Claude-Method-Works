"""diagonal.py -- is the MEASURED channel quantum defect concave in the node count
along a Madelung diagonal, at the closed core preceding each contest?
Uses COORDINATES-2_13.csv, grade == 'measured' ONLY. Never 'computed'."""
import csv, collections
rows=list(csv.DictReader(open("/mnt/project/COORDINATES-2_13.csv", newline='')))
D={}
for r in rows:
    if r['charge']=='1' and r['grade']=='measured':
        D[(int(r['Z']),int(r['l']))]=(float(r['delta']),r['source'][:50])
L="spdfg"
# closed cores and the next live diagonal M
cores={3:("Li",3),11:("Na",4),19:("K",5),37:("Rb",6),55:("Cs",7),87:("Fr",8)}
def diag(M):
    out=[]
    for l in range(0,5):
        n=M-l
        p=n-l-1
        if n>=l+1 and p>=0: out.append((p,n,l))
    return sorted(out)
for Z,(nm,M) in cores.items():
    pts=[]
    for p,n,l in diag(M):
        if (Z,l) in D:
            pts.append((p,n,l,D[(Z,l)][0]))
    print(f"\n{nm} I  (Z={Z}) closed core, next diagonal n+l = {M}   measured channels: {[(L[l]) for p,n,l,d in pts]}")
    for p,n,l,d in pts:
        print(f"    p={p}  {n}{L[l]}   delta={d:7.3f}   n*=n-delta={n-d:6.3f}")
    # stride-2 second differences along the diagonal
    for i in range(1,len(pts)-1):
        (p0,_,l0,d0),(p1,_,l1,d1),(p2,_,l2,d2)=pts[i-1],pts[i],pts[i+1]
        if p1-p0==2 and p2-p1==2:
            sd=d0-2*d1+d2
            print(f"    second difference at p={p1} ({L[l1]}):  {d0:.3f} - 2({d1:.3f}) + {d2:.3f} = {sd:+.3f}   {'CONCAVE' if sd<0 else 'NOT concave'}")
    incs=[(pts[i+1][3]-pts[i][3]) for i in range(len(pts)-1)]
    if incs: print(f"    increments along the diagonal: {[round(x,3) for x in incs]}")
    # the corridor for each member to be least nu = n - a*delta on this diagonal
    if len(pts)>=2:
        print("    corridor of a for each member to enter first (nu = n - a*delta):")
        for i,(p,n,l,d) in enumerate(pts):
            lo,hi=-1e9,1e9
            for j,(q,m,k,e) in enumerate(pts):
                if j==i: continue
                # n - a d < m - a e  <=>  a (e - d) < m - n
                if e-d>1e-9: hi=min(hi,(m-n)/(e-d))
                elif e-d<-1e-9: lo=max(lo,(m-n)/(e-d))
                elif m-n<=0: lo,hi=1,0
            print(f"       {n}{L[l]} first  iff  {lo:6.3f} < a < {hi:6.3f}" if lo<hi else f"       {n}{L[l]} first  never")