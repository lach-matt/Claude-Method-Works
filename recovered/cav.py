import itertools, math
from fractions import Fraction

M=N=L=4

def nu(m,n,l): return (m>0)+(n>0)+(l>0)

# ---------- C1: build with polarization as coordinate ----------
cells=[]
for m in range(M+1):
    for n in range(N+1):
        for l in range(L+1):
            for s in range(1, nu(m,n,l)):   # 1 .. nu-1
                cells.append((m,n,l,s))
S=set(cells)
formula = 2*M*N*L + M*N + M*L + N*L
# direct TE/TM count
te = ((M+1)*(N+1)-1)*L
tm = M*N*(L+1)
print("C1 |Lcav| =",len(S)," formula =",formula," TE+TM =",te+tm,
      " match:",len(S)==formula==te+tm)

# ---------- C2: join / meet closure ----------
join_fail=0; meet_fail=0; meet_examples=[]
cl=list(S)
for i in range(len(cl)):
    for j in range(i+1,len(cl)):
        x,y=cl[i],cl[j]
        jn=tuple(max(a,b) for a,b in zip(x,y))
        mt=tuple(min(a,b) for a,b in zip(x,y))
        if jn not in S: join_fail+=1
        if mt not in S:
            meet_fail+=1
            if len(meet_examples)<3: meet_examples.append((x,y,mt))
tot=len(cl)*(len(cl)-1)//2
print("C2 pairs =",tot," join failures =",join_fail," meet failures =",meet_fail,
      " (%.1f%%)"%(100*meet_fail/tot))
for e in meet_examples: print("    meet fail:",e)

# ---------- C4: the (m,n,l) product of chains ----------
box=[(m,n,l) for m in range(M+1) for n in range(N+1) for l in range(L+1)]
B=set(box)
d_fail=0; mod_fail=0; jf=0; mf=0
def rk(x): return sum(x)
for x in box:
    for y in box:
        jn=tuple(max(a,b) for a,b in zip(x,y))
        mt=tuple(min(a,b) for a,b in zip(x,y))
        if jn not in B: jf+=1
        if mt not in B: mf+=1
        if rk(jn)+rk(mt)!=rk(x)+rk(y): mod_fail+=1
print("C4 |box| =",len(B)," join fail =",jf," meet fail =",mf,
      " rank-modularity violations =",mod_fail)

# distributivity on triples (sample all, it's small enough)
dv=0
for x in box:
    for y in box:
        for z in box:
            a=tuple(max(p,min(q,r)) for p,q,r in zip(x,y,z))
            b=tuple(min(max(p,q),max(p,r)) for p,q,r in zip(x,y,z))
            if a!=b: dv+=1
print("   distributivity violations over",len(box)**3,"triples:",dv)

# Sperner: largest antichain = largest rank level
from collections import Counter
lev=Counter(rk(x) for x in box)
print("   rank levels:",dict(sorted(lev.items()))," width =",max(lev.values()))

# ---------- occupancy measure and E(X) ----------
mu={x: max(0, nu(*x)-1) for x in box}
empty=[x for x in box if mu[x]==0]
print("E  cells with mu=0:",len(empty)," predicted M+N+L+1 =",M+N+L+1,
      " match:",len(empty)==M+N+L+1)
print("   total modes = sum mu =",sum(mu.values())," == |Lcav| :",sum(mu.values())==len(S))

# ---------- C5: F(1), F(-1) ----------
F1=len(S)
Fm1=sum((-1)**(m+n+l+s) for (m,n,l,s) in S)
Fm1_box=sum((-1)**(m+n+l) for (m,n,l) in box)
print("C5 F(1) =",F1," F(-1)[Lcav] =",Fm1," F(-1)[box] =",Fm1_box)
for MM in range(2,7):
    cc=[(m,n,l,s) for m in range(MM+1) for n in range(MM+1) for l in range(MM+1)
        for s in range(1,nu(m,n,l))]
    print("    cap",MM,": F(1)=",len(cc)," F(-1)=",sum((-1)**sum(c) for c in cc))

# ---------- C6: bracket comparison on an ideal non-degenerate cavity ----------
a,b,d=1.0,0.6,1.4
def f(m,n,l): return 0.5*math.sqrt((m/a)**2+(n/b)**2+(l/d)**2)

Mx=8
ratios=[]; strictly_narrower=0; total=0; chan_only=0
for m in range(1,Mx):
    for n in range(1,Mx):
        for l in range(1,Mx):
            lo_ch=f(m-1,n,l); hi_ch=f(m+1,n,l)
            lo_lt=max(f(m-1,n,l),f(m,n-1,l),f(m,n,l-1))
            hi_lt=min(f(m+1,n,l),f(m,n+1,l),f(m,n,l+1))
            wc=hi_ch-lo_ch; wl=hi_lt-lo_lt
            assert lo_lt<=f(m,n,l)<=hi_lt, (m,n,l)
            total+=1
            if wl<wc-1e-12: strictly_narrower+=1
            ratios.append(wl/wc)
print("C6 interior cells tested:",total,
      " lattice bracket strictly narrower on",strictly_narrower,
      "(%.1f%%)"%(100*strictly_narrower/total))
print("   mean width ratio  = %.4f"%(sum(ratios)/len(ratios)))
print("   median            = %.4f"%(sorted(ratios)[len(ratios)//2]))
print("   min / max         = %.4f / %.4f"%(min(ratios),max(ratios)))

# ---------- C7: domain exit, two routes ----------
c=2.99792458e8
def omega_c(Q,V): return (math.pi**2*c**3*Q/V)**(1/3)
for (Q,V,name) in [(1e4,1e-3,"1 L, Q=1e4"),(1e6,1e-3,"1 L, Q=1e6"),
                   (1e4,1e-6,"1 cm^3, Q=1e4"),(1e9,1e-3,"1 L, Q=1e9 (SRF)")]:
    w=omega_c(Q,V); print("C7 %-18s omega_c=%.3e rad/s   f_c=%.3e Hz"%(name,w,w/(2*math.pi)))
# route 2: count modes below f in box vs Weyl law, find where spacing = f/Q
V=1e-3; Q=1e4
def weyl_N(fr): return 8*math.pi*V*fr**3/(3*c**3)          # both polarizations
def spacing(fr): return 1.0/(8*math.pi*V*fr**2/c**3)        # df per mode
lo,hi=1e8,1e13
for _ in range(200):
    mid=math.sqrt(lo*hi)
    if spacing(mid) > mid/Q: lo=mid
    else: hi=mid
print("   route 2 (Weyl spacing = linewidth): f_c = %.3e Hz"%lo)
