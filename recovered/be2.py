import math
I=146882.86; R=109737.31568; Z=2   # Kramida 2005 states Zeff=2 for Be II
# OBSERVED levels only. All [bracketed] values excluded (Edlen/Johansson formulas).
E={(2,0):0.000,(3,0):88231.915,(4,0):115464.44,(5,0):127335.12,(6,0):133556.44,
   (2,1):31928.744,(3,1):96495.360,(4,1):118760.51,(5,1):128971.62,(6,1):134485.37,
   (3,2):98054.57,(4,2):119421.20,(5,2):129310.13,(6,2):134681.15,(7,2):137919.17,
   (4,3):119446.59,(5,3):129323.85,(6,3):134689.20,(7,3):137924.31,
   (5,4):129325.46,(6,4):134690.16,(7,4):137925.11,(8,4):140024.58,
   (7,5):137925.13,(8,5):140024.70}
T={k:I-v for k,v in E.items()}
print("Be II delta = n - 2*sqrt(R/T), OBSERVED levels only")
for l in range(6):
    row=[(n,n-Z*math.sqrt(R/T[(n,l)])) for n in range(2,9) if (n,l) in T]
    if row: print(f"  l={l}: "+" ".join(f"{n}:{d:+.6f}" for n,d in row))
print("\nB-a  the f->g step, cell by cell:")
for n in (5,6,7):
    if (n,3) in T and (n,4) in T:
        df=n-Z*math.sqrt(R/T[(n,3)]); dg=n-Z*math.sqrt(R/T[(n,4)])
        print(f"  n={n}: delta(f)={df:+.6f}  delta(g)={dg:+.6f}   "
              f"sign change: {df*dg<0}   delta FALLS: {dg<df}   T(f)={T[(n,3)]:.2f} > T(g)={T[(n,4)]:.2f}: {T[(n,3)]>T[(n,4)]}")
print("\nB-c  T monotone in l at fixed n:")
v=t=0
for n in range(2,9):
    ts=[(l,T[(n,l)]) for l in range(6) if (n,l) in T]
    if len(ts)<2: continue
    bad=[(ts[i][0],ts[i+1][0]) for i in range(len(ts)-1) if ts[i+1][1]>ts[i][1]]
    t+=len(ts)-1; v+=len(bad)
    print(f"  n={n}: "+" ".join(f"l{l}:{x:9.2f}" for l,x in ts)+("  OK" if not bad else f"  VIOL {bad}"))
print(f"  comparisons {t}, violations {v}")
print("\nB-b  LATTICE BRACKET")
rats=[];viol=[]
for (n,l) in sorted(T):
    if (n+1,l) not in T or (n-1,l) not in T: continue
    up=[T[c] for c in [(n+1,l),(n,l+1)] if c in T]; dn=[T[c] for c in [(n-1,l),(n,l-1)] if c in T]
    if len(up)<2 or len(dn)<2: continue
    lo,hi=max(up),min(dn); ok=lo<=T[(n,l)]<=hi
    if not ok: viol.append((n,'spdfgh'[l]))
    wc=T[(n-1,l)]-T[(n+1,l)]; rats.append(((n,'spdfgh'[l]),(hi-lo)/wc))
for c,r in rats: print(f"  {c[0]}{c[1]}  ratio {r:.4f}")
print(f"  cells {len(rats)}   VIOLATIONS {len(viol)} {viol}")
if rats: print(f"  mean {sum(r for _,r in rats)/len(rats):.4f}")
print("\nB-d  r_l on the f-g pair, sigma from the compilation (0.06-0.3 cm^-1)")
for n in (5,6,7):
    if (n,3) in T and (n,4) in T:
        dd=(n-Z*math.sqrt(R/T[(n,3)]))-(n-Z*math.sqrt(R/T[(n,4)]))
        nu=Z*math.sqrt(R/T[(n,3)])
        for sig in (0.06,0.2,0.3):
            r=2*Z**2*R*abs(dd)/(nu**3*sig)
            print(f"  n={n} sigma={sig}: dT={T[(n,3)]-T[(n,4)]:.3f} cm^-1  r_l={r:6.2f}  {'ADMISSIBLE' if r>=5 else 'EXITS'}")