# r2-ch12a.py — Phase R2 instrument for main §12.1–12.5 (chat 71). The only tower-independent measurable claim: §12.1's parity statement.
import itertools
asc=['e','nu','V']; desc=['T','r','delta','spacing','w']; Q=asc+desc; cls={q:(0 if q in asc else 1) for q in Q}
tot=bad=0
for L in (3,4,5):
    seen=set()
    for cyc in itertools.permutations(Q,L):
        if cyc[0]!=min(cyc): continue
        key=(cyc[0],)+min(cyc[1:],cyc[1:][::-1])
        if key in seen: continue
        seen.add(key); tot+=1
        if sum(cls[cyc[i]]!=cls[cyc[(i+1)%L]] for i in range(L))%2: bad+=1
print('cycles of length 3–5 on the complete graph of the 8 derived quantities: %d; with an odd number of reversing edges: %d'%(tot,bad))