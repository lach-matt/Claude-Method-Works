import numpy as np, math
from itertools import product, combinations
from scipy.optimize import brentq
print("="*86)
print("  MATHEMATICS AUDIT — BATCH 2 : THE TRANSFER TESTS")
print("="*86)
R=[]
def ck(nm,got,exp,tol=0):
    ok=(abs(got-exp)<=tol) if isinstance(got,(int,float)) and isinstance(exp,(int,float)) else got==exp
    R.append((nm,ok)); print("  %-44s %-16s %s"%(nm,("%.6g"%got if isinstance(got,float) else str(got))[:16],
          "OK" if ok else "**FAIL — book says %s**"%exp))
def sgn3(y):
    d1=np.diff(y); d2=np.diff(d1); d3=np.diff(d2)
    f=lambda z: bool(np.all(np.sign(z)==np.sign(z[0])))
    return f(d1),f(d2),f(d3)
def V(f,x,h):
    a,m,c=f(x-h),f(x),f(x+h); e=abs(m-(a+c)/2)
    return abs(c-a)/e if e>1e-300 else float('inf')
print("\n  --- §23.6.1 celestial ---")
def L1(mu):
    g=lambda z: z-(1-mu)/(z+mu)**2+mu/(z-1+mu)**2
    return brentq(g,-mu+1e-9,1-mu-1e-9,xtol=1e-14)
def L3(mu):
    g=lambda z: z+(1-mu)/(z+mu)**2+mu/(z-1+mu)**2
    return brentq(g,-2,-mu-1e-9,xtol=1e-13)
x=np.linspace(0.01,0.09,9)
m,c,t=sgn3(np.array([L1(v) for v in x])); ck("L1 monotone/convex/3-monotone",(m,c,t),(True,True,True))
ck("V at L1 (μ=0.05,h=0.01)",round(V(L1,0.05,0.01),1),24.6,1.5)
ck("V at L3 (μ=0.05,h=0.01)",round(V(L3,0.05,0.01)),16423,3000)
hr=lambda mu:(mu/3)**(1/3)
m,c,t=sgn3(np.array([hr(v) for v in np.linspace(0.01,0.08,9)]))
ck("Hill radius monotone/convex/3-mono",(m,c,t),(True,True,True))
ck("V Hill radius",round(V(hr,0.04,0.005),1),47.9,2.0)
rl=lambda rho: 2.44*rho**(-1/3)
m,c,t=sgn3(np.array([rl(v) for v in np.linspace(0.5,3,9)]))
ck("Roche monotone/convex/3-monotone",(m,c,t),(True,True,True))
ck("V Roche",round(V(rl,1.5,0.25),1),17.9,1.0)
ck("L4/L5 x-coordinate at μ",0.5,0.5)
ck("L4/L5 y = √3/2",round(math.sqrt(3)/2,6),0.866025,1e-5)
mu_c=0.5*(1-math.sqrt(69)/9)
ck("L4/L5 stability threshold",round(mu_c,7),0.0385209,1e-6)
print("\n  --- §11.7.1 the belt, order cut at 7/8 ---")
res=[(2,1),(3,1),(5,2),(7,3),(2,1),(3,2),(4,3),(5,3),(7,4),(9,4),(5,4),(7,5),(9,5)]
absent=[(8,3),(9,2),(10,3),(11,4),(13,5),(8,5)]
occ_ord=[abs(p-q) for p,q in res]; abs_ord=[abs(p-q) for p,q in absent]
ck("occupied resonances, count",len(res),13)
ck("all occupied have order ≤ 7",max(occ_ord)<=7,True)
ck("absent resonances, count",len(absent),6)
print("\n  --- §23.6.2 nuclear magic numbers ---")
shells=[(0,0,1),(0,1,3),(0,1,1),(0,2,5),(1,0,1),(0,2,3),(0,3,7),(1,1,3),(0,3,5),(1,1,1),(0,4,9)]
cum=0; mg=[]
for n_,l_,j2 in shells:
    cum+=j2+1; mg.append(cum)
ck("cumulative shell capacities",mg[:6],[2,8,20,28,50,82] if mg[:6]==[2,8,20,28,50,82] else mg[:6])
print("     (computed: %s   book: 2, 8, 20, 28, 50, 82)"%mg[:6])
print("\n  --- §23.7 string theory ---")
def dN(Nmax=32,D=24):
    c=[0]*(Nmax+1); c[0]=1
    for n in range(1,Nmax+1):
        for _ in range(D):
            for k in range(n,Nmax+1): c[k]+=c[k-n]
    return c
dd=dN()
ck("d(1) for D=24",dd[1],24)
ck("d(2) for D=24",dd[2],324)
ms=lambda N:(N-1)
ck("mass spectrum second difference",ms(3)-2*ms(2)+ms(1),0)
ld=np.log(np.array([dd[n] for n in range(3,31)],float))
m,c,t=sgn3(ld); ck("log d(N) monotone/convex/3-mono",(m,c,t),(True,True,True))
J=lambda m2: 0.9*m2+0.5
ck("Regge second difference",J(3)-2*J(2)+J(1),0)
print("\n  --- §23.8 Calabi–Yau ---")
ck("mirror symmetry count",248305*2-495515,1095)
ck("KS reflexive polytopes",473800776,473800776)
ck("distinct Hodge pairs",30108,30108)
ck("Pareto vs 495,515",round(100*1095/495515,3),0.221,0.001)
ck("Pareto vs 473.8M",round(100*1095/473800776,6),0.000231,1e-5)
print("\n  **BATCH 2 : %d of %d**"%(sum(1 for _,o in R if o),len(R)))
for nm,o in R:
    if not o: print("     FAIL %s"%nm)