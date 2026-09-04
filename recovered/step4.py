#!/usr/bin/env python3
"""step4.py -- Session 5. n+l from rule A's entrant table (step3.json). Three checks, no solving.
(i) openings partition into n+l diagonals completing in order, with electron counts;
(ii) within-diagonal order vs n-rule; (iii) pairwise skeleton test over all candidate energies, by charge."""
import json,itertools,collections
R=sorted(json.load(open('step3.json')),key=lambda r:r['Z']); L='spdfg'
nl=lambda s:(int(s[0]),L.index(s[1])); M=lambda s:sum(nl(s))
def openings(key):
    seen=[];out=[]
    for r in R:
        if r[key] not in seen: seen.append(r[key]);out.append((r[key],r['Z']))
    return out
for key in ('A','obs'):
    byM=collections.OrderedDict()
    for s,z in openings(key): byM.setdefault(M(s),[]).append((s,z))
    ok=True;prev=-1
    for m,lst in byM.items():
        first=min(z for s,z in lst);last=max(z for s,z in lst)
        if first<prev: ok=False
        prev=last
        mad=[s for s,z in sorted(lst,key=lambda t:nl(t[0])[0])];got=[s for s,z in lst]
        print(f"{key} M={m}: {' '.join(f'{s}@{z}' for s,z in lst)} e={sum(2*(2*nl(s)[1]+1) for s,z in lst)}"+('' if mad==got else f"  inversion vs n-rule {mad}"))
    print(f"{key}: diagonals complete in order: {ok}")
for key,Ek in (('A','EA'),('B','EB')):
    byc=collections.defaultdict(lambda:[0,0]);within=wv=0
    for r in R:
        E=r[Ek];c=r['chargeA'] if key=='A' else 1
        for a,b in itertools.combinations(E,2):
            if M(a)==M(b):
                within+=1;lo,hi=(a,b) if nl(a)[0]<nl(b)[0] else (b,a)
                if E[lo]>E[hi]: wv+=1
            else:
                lo,hi=(a,b) if M(a)<M(b) else (b,a);byc[c][0]+=1
                if E[lo]>E[hi]: byc[c][1]+=1
    tot=sum(v[0] for v in byc.values());bad=sum(v[1] for v in byc.values())
    print(f"rule {key}: cross-diagonal {tot-bad}/{tot} lower-M binds first; within-diagonal n-rule {within-wv}/{within}; violations by charge {dict((c,tuple(v)) for c,v in sorted(byc.items()))}")