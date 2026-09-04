from collections import defaultdict
exec(open('/home/claude/entry_test.py').read().split('boxes =')[0])
X=L8; NAME=['n','l','k','q','e','f','g','2S']
ADJ={0:[1],1:[0,2],2:[1,3,7],3:[2,6],6:[3,5],5:[6,4],4:[5],7:[2]}
def sides(cut):
    seen={cut}; comps=[]
    for s in ADJ:
        if s in seen: continue
        st=[s]; c=[]
        while st:
            u=st.pop()
            if u in seen: continue
            seen.add(u); c.append(u); st+=ADJ[u]
        comps.append(sorted(c))
    return comps

print("Opposed monotonicity, tested at every cut of the constraint tree.\n")
print(f"{'cut':>4} {'|A(v)| as v rises':<26} {'|B(v)| as v rises':<26} {'opposed?':>9}")
for c in range(8):
    comps=sides(c)
    if len(comps)!=2: continue
    A,B=comps
    vs=sorted({x[c] for x in X})
    a=[len({tuple(x[i] for i in A) for x in X if x[c]==v}) for v in vs]
    b=[len({tuple(x[i] for i in B) for x in X if x[c]==v}) for v in vs]
    nonincr=all(a[i]>=a[i+1] for i in range(len(a)-1))
    nondecr=all(b[i]<=b[i+1] for i in range(len(b)-1))
    alt   =all(a[i]<=a[i+1] for i in range(len(a)-1)) and all(b[i]>=b[i+1] for i in range(len(b)-1))
    opp = (nonincr and nondecr) or alt
    print(f"{NAME[c]:>4} {str(a):<26} {str(b):<26} {str(opp):>9}")

print("\nand the cause, read off the constraint list of §7.1:")
cons=[("l","n","ℓ ≤ n−1"),("k","l","k ≤ 4ℓ+2"),("q","k","q ≤ k"),
      ("2S","k","2S ≤ k"),("f","e","f ≤ e−1"),("g","f","g ≤ 4f+2"),("g","q","g ≤ q")]
ceil=defaultdict(list); floor=defaultdict(list)
for lo,hi,txt in cons: ceil[hi].append(lo); floor[lo].append(hi)
print(f"{'coordinate':>11} {'is a ceiling for':<16} {'is bounded by':<16} {'both?':>6}")
for v in NAME:
    both = bool(ceil[v]) and bool(floor[v])
    print(f"{v:>11} {str(ceil[v] or '—'):<16} {str(floor[v] or '—'):<16} {str(both):>6}")