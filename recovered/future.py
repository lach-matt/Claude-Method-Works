from collections import defaultdict
exec(open('/home/claude/entry_test.py').read().split('boxes =')[0])
X=L8
past=lambda x:(x[0],x[1],x[2],x[7]); pres=lambda x:x[3]; fut=lambda x:(x[4],x[5],x[6])

# 1. is the future a function of (past, present)?
fib=defaultdict(set)
for x in X: fib[(past(x),pres(x))].add(fut(x))
sizes=sorted(len(v) for v in fib.values())
print(f"(past, present) pairs: {len(fib)}")
print(f"  futures per pair: min {sizes[0]}  median {sizes[len(sizes)//2]}  max {sizes[-1]}")
print(f"  pairs determining a single future: {sum(1 for v in fib.values() if len(v)==1)}"
      f" of {len(fib)} = {100*sum(1 for v in fib.values() if len(v)==1)/len(fib):.1f}%")

# 2. does the past enter at all, given the present?
byq=defaultdict(list)
for (p,q),F in fib.items(): byq[q].append((p,frozenset(F)))
print("\nfor fixed present q, is the future set the same for every past?")
for q in sorted(byq):
    Fs={F for _,F in byq[q]}
    print(f"  q={q}: {len(byq[q]):>2} distinct pasts, {len(Fs)} distinct future sets, "
          f"|future| = {sorted({len(F) for F in Fs})}")

# 3. monotonicity: does the future set grow with the present?
Fq={q: {fut(x) for x in X if x[3]==q} for q in sorted({x[3] for x in X})}
print("\nfuture set against the present:")
prev=None; mono=True
for q in sorted(Fq):
    inc = prev is None or prev <= Fq[q]
    if prev is not None and not prev <= Fq[q]: mono=False
    print(f"  q={q}: |future| = {len(Fq[q]):>2}  contains the previous set: {inc}")
    prev=Fq[q]
Aq={q: {past(x) for x in X if x[3]==q} for q in sorted(Fq)}
print(f"  |past| by q: {[len(Aq[q]) for q in sorted(Aq)]}   "
      f"|future| by q: {[len(Fq[q]) for q in sorted(Fq)]}")
print(f"  future nested increasing in q: {mono}")

# 4. and the past: nested decreasing?
prevA=None; monoA=True
for q in sorted(Aq):
    if prevA is not None and not Aq[q] <= prevA: monoA=False
    prevA=Aq[q]
print(f"  past nested decreasing in q: {monoA}")

# 5. is the future set an interval of the target lattice -- a bracket?
for q in sorted(Fq):
    F=Fq[q]
    lo=tuple(min(c[i] for c in F) for i in range(3))
    hi=tuple(max(c[i] for c in F) for i in range(3))
    box=[c for c in {fut(x) for x in X} if all(lo[i]<=c[i]<=hi[i] for i in range(3))]
    print(f"  q={q}: future set is the full interval [{lo},{hi}] of the target lattice: "
          f"{set(box)==F}")