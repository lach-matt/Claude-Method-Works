import math
I=121267.61   # Mg II ionisation energy, Martin & Zalubas 1980
R=109737.31568
# Mg II observed levels, lower-J member. EXCLUDED: 10p (printed in brackets = calculated).
# EXCLUDED: 5p J=1/2 and 7f — lost to OCR in the retrieved text, not guessed.
obs={(3,0):0.00,(4,0):69804.95,(5,0):92790.51,(6,0):103196.75,(7,0):108784.33,
     (8,0):112129.20,(9,0):114289.36,(10,0):115764.99,
     (3,1):35669.31,(4,1):80619.50,(6,1):105622.34,(7,1):110203.58,
     (8,1):113030.25,(9,1):114896.79,
     (3,2):71490.19,(4,2):93310.59,(5,2):103419.70,(6,2):108900.02,(7,2):112197.05,
     (8,2):114332.68,(9,2):115794.41,
     (4,3):93799.63,(5,3):103689.86,(6,3):109062.32,(8,3):114403.55,(9,3):115844.60,
     (10,3):116875.25,
     (5,4):103705.66,(6,4):109072.05,(7,4):112307.79,(8,4):114407.88,(9,4):115847.67,
     (10,4):116877.54,(11,4):117639.51,
     (6,5):109074.00,(7,5):112309.06,(8,5):114408.74,(9,5):115848.28,(10,5):116878.04}
T={k:I-v for k,v in obs.items()}
Z=2  # Mg II, singly ionised -> Z_eff = 2
print("Mg II  delta = n - Z*sqrt(R/T)")
for l in range(6):
    row=[(n,n-Z*math.sqrt(R/T[(n,l)])) for n in range(3,12) if (n,l) in T]
    if row: print(f"  l={l}: "+" ".join(f"{n}:{d:+.4f}" for n,d in row))
print("\nl-monotonicity at fixed n:")
viol=tot=0
for n in range(3,12):
    ds=[(l,n-Z*math.sqrt(R/T[(n,l)])) for l in range(6) if (n,l) in T]
    if len(ds)<2: continue
    bad=[(ds[i][0],ds[i+1][0]) for i in range(len(ds)-1) if ds[i+1][1]>ds[i][1]]
    tot+=len(ds)-1; viol+=len(bad)
    print(f"  n={n:2d}: "+" ".join(f"l{l}:{d:+.4f}" for l,d in ds)+("  OK" if not bad else f"  VIOL {bad}"))
print(f"  comparisons {tot}, violations {viol}")
print("\nLATTICE vs CHANNEL BRACKET")
print(f"  {'cell':6s} {'T':>10s} {'chan w':>10s} {'latt w':>10s} {'ratio':>7s}  ok")
rats=[];bad=0
for (n,l) in sorted(T):
    if (n+1,l) not in T or (n-1,l) not in T: continue
    up=[T[c] for c in [(n+1,l),(n,l+1)] if c in T]
    dn=[T[c] for c in [(n-1,l),(n,l-1)] if c in T]
    if len(up)<2 or len(dn)<2: continue
    lo_c,hi_c=T[(n+1,l)],T[(n-1,l)]; lo_l,hi_l=max(up),min(dn)
    ok=lo_l<=T[(n,l)]<=hi_l
    if not ok: bad+=1
    wc,wl=hi_c-lo_c,hi_l-lo_l; rats.append(wl/wc)
    print(f"  {n}{'spdfgh'[l]:1s}   {T[(n,l)]:10.2f} {wc:10.2f} {wl:10.2f} {wl/wc:7.4f}  {'OK' if ok else 'VIOLATION'}")
print(f"\n  cells {len(rats)}  violations {bad}  narrower {sum(1 for r in rats if r<1-1e-12)}/{len(rats)}")
print(f"  mean {sum(rats)/len(rats):.4f}   median {sorted(rats)[len(rats)//2]:.4f}"
      f"   min/max {min(rats):.4f}/{max(rats):.4f}")
na=[0.4871,0.5493,0.5457,0.5255,0.0060,0.5756,0.5099,0.5938,0.4986,0.6061,0.4900,0.6148,0.4832,0.6214]
both=rats+na
print(f"\n  POOLED Na I + Mg II: {len(both)} cells, mean {sum(both)/len(both):.4f}, "
      f"median {sorted(both)[len(both)//2]:.4f}, violations {bad+0}")