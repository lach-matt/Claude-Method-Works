I=41449.451   # 92CIO/BUR
# Na I levels, Sansonetti 2008 JPCRD 37 Table 2. Lower-J member, fixed convention.
# EXCLUDED: every level referenced 97DYU/EFR (quantum-defect FORMULA values).
obs={ (3,0):0.00000,(4,0):25739.999,(5,0):33200.673,(6,0):36372.618,(7,0):38012.042,
      (8,0):38968.51,(9,0):39574.85,(10,0):39983.27,(11,0):40271.396,(12,0):40482.236,
      (3,1):16956.170,(4,1):30266.99,(5,1):35040.38,(6,1):37296.32,(7,1):38540.18,
      (8,1):39298.35,(9,1):39794.479,(10,1):40136.810,(11,1):40382.925,
      (3,2):29172.837,(4,2):34548.729,(5,2):37036.752,(6,2):38387.255,(7,2):39200.93,
      (8,2):39728.70,(9,2):40090.31,(10,2):40348.915,
      (4,3):34586.92,(5,3):37057.65,(6,3):38399.79,(7,3):39208.98,(8,3):39734.16,(9,3):40094.19,
      (5,4):37059.54 }
refs={0:'81MAR/ZAL,88ARQ,81JUN/PIN,56RIS,92CIO/BUR',1:'81JUN/PIN,56RIS,95DYU/EFI,98BAU/BUR',
      2:'81MAR/ZAL,81JUN/PIN,56RIS,98BAU/BUR',3:'61JOH,56RIS',4:'70LIT'}
T={k:I-v for k,v in obs.items()}
R=109737.31568
print("delta by (n,l), from OBSERVED levels only:")
import math
for l in range(5):
    row=[(n,n-math.sqrt(R/T[(n,l)])) for n in range(3,13) if (n,l) in T]
    if row: print(f"  l={l}: "+" ".join(f"{n}:{d:+.4f}" for n,d in row))

print("\nl-monotonicity at fixed n (delta must DECREASE in l):")
viol=0; tot=0
for n in range(3,13):
    ds=[(l,n-math.sqrt(R/T[(n,l)])) for l in range(5) if (n,l) in T]
    if len(ds)<2: continue
    bad=[(ds[i][0],ds[i+1][0]) for i in range(len(ds)-1) if ds[i+1][1]>ds[i][1]]
    tot+=len(ds)-1; viol+=len(bad)
    print(f"  n={n:2d}: "+" ".join(f"l{l}:{d:+.4f}" for l,d in ds)+("  OK" if not bad else f"  VIOL {bad}"))
print(f"  adjacent-l comparisons: {tot}, violations: {viol}")

print("\nLATTICE BRACKET vs CHANNEL BRACKET  (T order-reversing in n and l)")
print(f"  {'cell':6s} {'T':>10s} {'chan width':>11s} {'latt width':>11s} {'ratio':>7s}  ok")
rats=[]; bad=0
for (n,l) in sorted(T):
    up=[T[c] for c in [(n+1,l),(n,l+1)] if c in T]
    dn=[T[c] for c in [(n-1,l),(n,l-1)] if c in T]
    if len(up)<2 or len(dn)<2: continue
    if (n+1,l) not in T or (n-1,l) not in T: continue
    lo_c,hi_c=T[(n+1,l)],T[(n-1,l)]
    lo_l,hi_l=max(up),min(dn)
    ok=lo_l<=T[(n,l)]<=hi_l
    if not ok: bad+=1
    wc,wl=hi_c-lo_c,hi_l-lo_l
    rats.append(wl/wc)
    print(f"  {n}{'spdfg'[l]:1s}   {T[(n,l)]:10.3f} {wc:11.3f} {wl:11.3f} {wl/wc:7.4f}  {'OK' if ok else 'VIOLATION'}")
print(f"\n  cells tested: {len(rats)}   bracket violations: {bad}")
print(f"  mean ratio   = {sum(rats)/len(rats):.4f}")
print(f"  median       = {sorted(rats)[len(rats)//2]:.4f}")
print(f"  min / max    = {min(rats):.4f} / {max(rats):.4f}")
print(f"  narrower on  = {sum(1 for r in rats if r<1-1e-12)}/{len(rats)}")
import statistics
byl={}
for (n,l) in sorted(T):
    pass