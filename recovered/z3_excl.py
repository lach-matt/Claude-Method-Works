import json, sys
tag=sys.argv[1]; cond=sys.argv[2]
P=json.load(open(f"prep_{tag}.json"))
X=[tuple(c) for c in P["cells"]]
els=[frozenset(e) for e in P["elements"]]
k0=json.load(open(f"seed_{tag}.json"))["seed"]
lmax=max(c[1] for c in X); fmax=max(c[5] for c in X)
kmax_=max(c[2] for c in X); gmax=max(c[6] for c in X)
conds={
 "ss": lambda c:c[1]==0 and c[5]==0,
 "sp": lambda c:c[1]==0 and c[5]==1,
 "ps": lambda c:c[1]==1 and c[5]==0,
 "pp": lambda c:c[1]==1 and c[5]==1,
 "null": lambda c:c[3]==0,
 "full": lambda c:c[3]==c[2],
 "c3": lambda c:(c[1]==lmax and c[2]==kmax_ and c[3]==c[2] and c[5]==fmax and c[6]==gmax and c[7]==0),
}
p=conds[cond]
# rebuild signature classes over allowed cells only
allowed=[ci for ci,c in enumerate(X) if not p(c)]
sig={}
for ci in allowed:
    s=tuple(ei for ei,e in enumerate(els) if ci in e)
    if s: sig.setdefault(s,None)
sigs=[frozenset(s) for s in sig]
NE=len(els)
if any(all(ei not in s for s in sigs) for ei in range(NE)):
    print(f"{cond}: INFEASIBLE without it -> UNIVERSAL"); sys.exit()
found=[None]
def bb(ch,cov,k):
    if found[0] is not None: return
    if len(cov)==NE: found[0]=ch; return
    if len(ch)==k: return
    unc=[ei for ei in range(NE) if ei not in cov]
    ei=min(unc,key=lambda e:sum(1 for s in sigs if e in s))
    for si,s in sorted(enumerate(sigs),key=lambda t:-len(t[1])):
        if ei in s and si not in ch: bb(ch|{si},cov|s,k)
res=None
for k in range(1,16):
    found[0]=None; bb(frozenset(),frozenset(),k)
    if found[0] is not None: res=k; break
print(f"{cond}: min without it = {res} vs seed {k0} -> {'UNIVERSAL' if res is None or res>k0 else 'not universal'}")