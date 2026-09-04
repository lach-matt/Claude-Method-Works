import json, sys
from gen import build
cp=tuple(map(int,sys.argv[1:6]))
X=build(*cp,lambda k:0,False)
d=8
els=[]
for i in range(d):
    for v in sorted({c[i] for c in X}):
        els.append(frozenset(k for k,c in enumerate(X) if c[i]==v))
for i in range(d):
    for j in range(d):
        if i==j: continue
        m={}
        for c in X: m[c[j]]=max(m.get(c[j],-10**9),c[i])
        b=-10**9
        for t in sorted(m):
            if m[t]>b:
                b=m[t]
                els.append(frozenset(k for k,c in enumerate(X) if c[j]<=t and c[i]==b))
els=list(set(els)); els.sort(key=len)
keep=[]
for e in els:
    if not any(k<=e for k in keep): keep.append(e)
# signature classes: cell -> tuple of element ids it covers
sig={}
for ci in set().union(*keep):
    s=tuple(ei for ei,e in enumerate(keep) if ci in e)
    sig.setdefault(s,[]).append(ci)
tag="".join(map(str,cp))
json.dump({"cells":[list(c) for c in X],
           "elements":[sorted(e) for e in keep],
           "sig_classes":{",".join(map(str,k)):v for k,v in sig.items()}},
          open(f"prep_{tag}.json","w"))
print(f"cap {cp}: cells {len(X)}, elements {len(keep)}, signature classes {len(sig)}")