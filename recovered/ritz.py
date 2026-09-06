import math, statistics as st
import numpy as np
from itertools import product, permutations
from scipy.optimize import curve_fit
Rinf=109737.31568; mp=1836.15267343
S={
"Cd I s":(1,112.41,72540.05,{6:51483.980,7:62563.435,8:66682.029,9:68682.325,10:69806.814,11:70502.04,12:70961.993}),
"Cd I p":(1,112.41,72540.05,{5:43692.384,6:59907.28,7:65501.412,8:68059.393}),
"Cd I d":(1,112.41,72540.05,{5:59485.768,6:65353.372,7:67989.814,8:69400.900,9:70244.09,10:70787.850,11:71158.957}),
"Cd I f":(1,112.41,72540.05,{4:65586.0,5:68093.7,6:69456.4,7:70277.4,8:70809.7,9:71174.2}),
"In I s":(1,114.82,46670.107,{6:24372.957,7:36301.864,8:40636.98,9:42719.02,10:43881.26,11:44595.86,12:45067.19}),
"In I d":(1,114.82,46670.107,{5:32892.230,6:39048.53,7:41836.41,8:43335.93,9:44234.70,10:44815.06}),
"In I f":(1,114.82,46670.107,{4:39707.59,5:42220.25,6:43584.66,7:44406.31,8:44938.81,9:45303.31}),
"Rb I s":(1,84.912,33690.81,{6:20132.510,7:26311.437,8:29046.816,9:30499.031,10:31362.331,11:31917.221,12:32294.911}),
"Rb I p":(1,84.912,33690.81,{6:23715.081,7:27835.02,8:29834.94,9:30958.91,10:31653.85,11:32113.55}),
"Rb I d":(1,84.912,33690.81,{5:25700.536,6:28687.127,7:30280.113,8:31221.440,9:31821.855,10:32227.610}),
"Sr II s":(2,87.906,88965.18,{6:47736.53,7:64964.10,8:73237.1,9:77857.6,10:80701.8,11:82576.1}),
"Sr II d":(2,87.906,88965.18,{5:53286.31,6:67522.87,7:74621.3,8:78688.8,9:81240.2,10:82951.5}),
"Sr II f":(2,87.906,88965.18,{4:60990.04,5:71065.8,6:76553.4,7:79861.3,8:82005.9,9:83472.7}),
}
LM={"s":0,"p":1,"d":2,"f":3}
print("  THE RITZ EXPANSION  δ(n) = δ₀ + δ₂/(n−δ₀)²\n")
print(f"      {'series':<10}{'n':>3}{'δ₀':>10}{'δ₂':>10}{'rms':>10}{'δ₂/δ₀':>10}{'−ℓ(ℓ+1)/3':>12}")
OUT=[]
for nm,(c,A,lim,d) in S.items():
    RM=Rinf/(1+1/(A*mp))
    n=np.array(sorted(d),float); E=np.array([d[int(x)] for x in n])
    ns=c*np.sqrt(RM/(lim-E)); dd=n-ns
    if len(n)<4: continue
    def f(_,d0,d2): return d0+d2/(n-d0)**2
    try: pr,_=curve_fit(f,np.arange(len(n)),dd,p0=[dd[-1],0.1],maxfev=200000)
    except Exception: continue
    r=dd-f(None,*pr); l=LM[nm[-1]]
    seat=-l*(l+1)/3
    OUT.append((nm,l,pr[0],pr[1],pr[1]/pr[0] if abs(pr[0])>1e-6 else float("nan"),seat))
    print(f"      {nm:<10}{len(n):>3}{pr[0]:>10.4f}{pr[1]:>10.4f}"
          f"{float(np.sqrt(np.mean(r**2))):>10.5f}"
          f"{pr[1]/pr[0]:>10.4f}{seat:>12.3f}")
print()
print("  Λ_ryd — THE SERIES INDEX  (Ritz order × ℓ × sign)\n")
cells=set()
for nm,l,d0,d2,rat,seat in OUT:
    cells.add((0,l,1 if d0>0 else 0))
    cells.add((1,l,1 if d2>0 else 0))
def opR(X,dd):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(dd)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(dd) for j in range(dd) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]]
            for i in range(dd) for j in range(dd) if i!=j)}
best=None
for lp in permutations(range(4)):
    cs={(a,lp.index(b),c) for a,b,c in cells}
    E=len(opR(cs,3))-len(cs)
    if best is None or E<best[0]: best=(E,lp,cs)
E,lp,cs=best
print(f"      |X| = {len(cells)}   minimum E over ℓ-orderings = {E}")
print(f"      ℓ order : {' < '.join('spdf'[i] for i in lp)}\n")
print("  THE SIGN OF δ₂ BY ℓ\n")
for l in range(4):
    v=[d2 for nm,ll,d0,d2,rat,seat in OUT if ll==l]
    if not v: continue
    print(f"      ℓ = {'spdf'[l]} : {len(v)} series · "
          f"{sum(1 for x in v if x>0)} positive · {sum(1 for x in v if x<0)} negative"
          f"   median {st.median(v):+.4f}")