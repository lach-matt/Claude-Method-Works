import math
I=48278.37   # Martin & Zalubas 1979, Al I
R=109737.31568
# Al I observed levels, lower-J member. EXCLUDED: every value printed in [ ]
# (10s-16s, 9f, 10f) = calculated from Eriksson & Isberg series formulae.
obs={(4,0):25347.756,(5,0):37689.413,(6,0):42144.402,(7,0):44273.122,
     (8,0):45457.233,(9,0):46183.896,
     (3,1):0.000,(4,1):32949.807,(5,1):40271.965,(6,1):43335.013,(7,1):44919.654,
     (3,2):32435.435,(4,2):38929.405,(5,2):42233.722,(6,2):44166.417,(7,2):45344.164,
     (8,2):46093.424,(9,2):46593.32,(10,2):46940.97,(11,2):47192.3,(12,2):47378.7,
     (13,2):47521.1,
     (4,3):41319.372,(5,3):43831.090,(6,3):45194.663,(7,3):46015.756,(8,3):46547.924}
T={k:I-v for k,v in obs.items()}
print("A-c  delta = n - sqrt(R/T), Martin & Zalubas labelling, Z_eff=1")
for l in range(4):
    row=[(n,n-math.sqrt(R/T[(n,l)])) for n in range(3,14) if (n,l) in T]
    if row: print(f"  l={l}: "+" ".join(f"{n}:{d:+.4f}" for n,d in row))
print("\n  Appendix C states Al I: ns +1.7670  np +1.3365  nd +0.0248  nf +0.0429")
print("\nA-c  l-monotonicity of T at fixed n (T must DECREASE in l):")
v=t=0
for n in range(3,14):
    ts=[(l,T[(n,l)]) for l in range(4) if (n,l) in T]
    if len(ts)<2: continue
    bad=[(ts[i][0],ts[i+1][0]) for i in range(len(ts)-1) if ts[i+1][1]>ts[i][1]]
    t+=len(ts)-1; v+=len(bad)
    print(f"  n={n:2d}: "+" ".join(f"l{l}:{x:9.2f}" for l,x in ts)+("  OK" if not bad else f"  VIOL {bad}"))
print(f"  comparisons {t}, violations {v}")
print("\nA-a/A-b  LATTICE vs CHANNEL BRACKET")
print(f"  {'cell':6s} {'T':>9s} {'chan w':>9s} {'latt w':>9s} {'ratio':>7s}  ok")
rats=[];bad=[];lo_l_cells=[];hi_l_cells=[]
for (n,l) in sorted(T):
    if (n+1,l) not in T or (n-1,l) not in T: continue
    up=[T[c] for c in [(n+1,l),(n,l+1)] if c in T]
    dn=[T[c] for c in [(n-1,l),(n,l-1)] if c in T]
    if len(up)<2 or len(dn)<2: continue
    lo_c,hi_c=T[(n+1,l)],T[(n-1,l)]; lo,hi=max(up),min(dn)
    ok=lo<=T[(n,l)]<=hi
    if not ok: bad.append((n,l))
    wc,wl=hi_c-lo_c,hi-lo; rats.append(wl/wc)
    (lo_l_cells if l<=2 else hi_l_cells).append(wl/wc)
    print(f"  {n}{'spdf'[l]:1s}   {T[(n,l)]:9.2f} {wc:9.2f} {wl:9.2f} {wl/wc:7.4f}  {'OK' if ok else 'VIOLATION'}")
print(f"\n  cells {len(rats)}   VIOLATIONS {len(bad)} {bad}")
print(f"  mean {sum(rats)/len(rats):.4f}   l<=2 mean {sum(lo_l_cells)/len(lo_l_cells):.4f} (n={len(lo_l_cells)})")
if hi_l_cells: print(f"  l>=3 mean {sum(hi_l_cells)/len(hi_l_cells):.4f} (n={len(hi_l_cells)})")