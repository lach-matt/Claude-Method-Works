import numpy as np, itertools
rng = np.random.default_rng(7)

# Atkinson (2003) ACP 3, 2233 -- Table 1 recommended 298 K rate constants
# units 1e-12 cm3 molecule-1 s-1
nalk = [(1,0.00640,.20),(2,0.248,.20),(3,1.09,.20),(4,2.36,.20),(5,3.80,.25),
        (6,5.20,.20),(7,6.76,.20),(8,8.11,.20),(9,9.70,.20),(10,11.0,.20),
        (11,12.3,.20),(12,13.2,.20),(13,15.1,.25)]
C = np.array([a for a,b,c in nalk]); K = np.array([b for a,b,c in nalk]); U = np.array([c for a,b,c in nalk])

print("=== A. n-alkane channel: leave-one-out deductive bracket ===")
print(" C   k_meas    bracket lo-hi        width   width/k  exp 2u interval width/k")
cov=0; rows=[]
for i in range(1,len(C)-1):
    lo,hi = K[i-1],K[i+1]                       # monotone increasing in C
    w = hi-lo; ok = lo<=K[i]<=hi; cov+=ok
    expw = 2*U[i]*K[i]*2                        # full +/-u interval width
    rows.append((C[i],K[i],lo,hi,w,w/K[i],expw/K[i]))
    print(f"{C[i]:3d} {K[i]:7.3f}  [{lo:7.3f},{hi:7.3f}]  {w:7.3f}  {w/K[i]:6.2f}   {expw/K[i]:6.2f}   {'OK' if ok else 'FAIL'}")
print(f"coverage {cov}/{len(C)-2}")
mw = np.mean([r[5] for r in rows]); me = np.mean([r[6] for r in rows])
print(f"mean bracket width  = {mw*100:.0f}% of value")
print(f"mean exp. interval  = {me*100:.0f}% of value   ratio = {mw/me:.2f}")
print(f"series total spread = {K.max()/K.min():.0f}x  ({K.max()-K.min():.2f} units)")

print("\n=== B. does the bracket survive measurement error? ===")
# treat published k as truth +/- stated u; resample 'measured' neighbours, ask if truth is contained
N=200000; fails=np.zeros(len(C))
for t in range(N):
    m = K*(1+rng.normal(0,U/2,len(K)))   # stated u read as 2-sigma
    for i in range(1,len(C)-1):
        if not (min(m[i-1],m[i+1])<=K[i]<=max(m[i-1],m[i+1])): fails[i]+=1
for i in range(1,len(C)-1):
    print(f" C{C[i]:<3d} containment {100*(1-fails[i]/N):5.1f}%")
print(f" pooled containment {100*(1-fails.sum()/(N*(len(C)-2))):.1f}%   (deductive claim: 100%)")

print("\n=== C. what a zero-effort baseline gets ===")
# log-linear interpolation between the same two neighbours = the Ritz analogue
errs=[]
for i in range(1,len(C)-1):
    p = np.exp(np.interp(C[i],[C[i-1],C[i+1]],[np.log(K[i-1]),np.log(K[i+1])]))
    errs.append(abs(p-K[i])/K[i])
print(f" log-interp point estimate: median |err| {100*np.median(errs):.1f}%, max {100*max(errs):.1f}%")
print(f" vs stated experimental uncertainty on the same cells: {100*np.mean(U[1:-1]):.0f}%")

print("\n=== D. channel discipline: order by carbon number alone ===")
allk = [(1,'methane',.00640),(2,'ethane',.248),(3,'propane',1.09),
 (4,'n-butane',2.36),(4,'2-methylpropane',2.12),
 (5,'n-pentane',3.80),(5,'2-methylbutane',3.6),(5,'neopentane',0.825),
 (6,'n-hexane',5.20),(6,'2-methylpentane',5.2),(6,'3-methylpentane',5.2),
 (6,'2,2-dimethylbutane',2.23),(6,'2,3-dimethylbutane',5.78),
 (7,'n-heptane',6.76),(7,'2,4-dimethylpentane',4.8),(7,'2,2,3-trimethylbutane',3.81),
 (8,'n-octane',8.11),(8,'2,2,4-trimethylpentane',3.34),(8,'2,3,4-trimethylpentane',6.6),
 (8,'2,2,3,3-tetramethylbutane',0.972),
 (9,'n-nonane',9.70),(9,'3,3-diethylpentane',4.8),
 (10,'n-decane',11.0),(10,'3,4-diethylhexane',6.9)]
viol=[(a,b) for a,b in itertools.combinations(allk,2) if a[0]<b[0] and a[2]>b[2]]
comp=[(a,b) for a,b in itertools.combinations(allk,2) if a[0]<b[0]]
print(f" strictly-lower-carbon pairs: {len(comp)}, monotonicity violations: {len(viol)} ({100*len(viol)/len(comp):.0f}%)")
for a,b in viol[:5]: print(f"   {a[1]}(C{a[0]}) {a[2]} > {b[1]}(C{b[0]}) {b[2]}")
print(f"   ... worst: neopentane C5 0.825 < propane C3 1.09")