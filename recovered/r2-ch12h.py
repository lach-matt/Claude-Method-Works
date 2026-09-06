# r2-ch12h.py — Phase R2, main §12.11.0.3 "Every second bridge, priced" (chat 73). Beside tower-2.py.
# Λ8 from tower-2.py; every ordered source–target coordinate bound x ≤ y imposed as a second bridge; the cut set tested for
# closure on every pair (976²) and for the fibre factorisation Σ_q |A_q||B_q| = |X| (A_q sources (n,ℓ,k,2S), B_q targets (e,f,g)).
import importlib.util, os, itertools, collections
_sp=importlib.util.spec_from_file_location('tower2', os.path.join(os.path.dirname(os.path.abspath(__file__)),'tower-2.py'))
_t2=importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_t2)
L8=_t2.L8(); S8=set(L8)
names=['n','ℓ','k','q','e','f','g','2S']; ix={v:i for i,v in enumerate(names)}
edges=[('n','ℓ'),('ℓ','k'),('k','q'),('k','2S'),('q','g'),('e','f'),('f','g')]   # tower-2.py's seven bounds
SRC=['n','ℓ','k','2S']; TGT=['e','f','g']
adj=collections.defaultdict(set)
for a,b in edges: adj[a].add(b); adj[b].add(a)
def reach(start, removed):
    seen={start}; st=[start]
    while st:
        v=st.pop()
        for w in adj[v]:
            if w!=removed and w not in seen: seen.add(w); st.append(w)
    return seen
print(f'constraint graph of Λ8: {len(names)} nodes, {len(edges)} edges, connected {len(reach("n",None))==8}')
seps=[]
for v in names:
    ok=all(t not in reach(s, v) for s in SRC if s!=v for t in TGT if t!=v)
    if ok: seps.append(v)
print(f'vertices whose removal separates every remaining source coordinate from every remaining target coordinate: {seps} | of these, outside both signatures: {[v for v in seps if v not in SRC+TGT]}')
def price(cond, label):
    X=[c for c in L8 if cond(c)]; XS=set(X)
    bj=bm=0
    for a in X:
        for b in X:
            j=tuple(map(max,a,b)); m=tuple(map(min,a,b))
            if j not in XS: bj+=1
            if m not in XS: bm+=1
    A=collections.defaultdict(set); B=collections.defaultdict(set)
    for c in X: A[c[3]].add((c[0],c[1],c[2],c[7])); B[c[3]].add((c[4],c[5],c[6]))
    fact=sum(len(A[q])*len(B[q]) for q in A)-len(X)
    Ag={(c[0],c[1],c[2],c[7]) for c in X}; Bg={(c[4],c[5],c[6]) for c in X}
    glob=len(Ag)*len(Bg)-len(X)
    return len(X), bj, bm, fact, glob
rows=[]
print(f'{"bridge":<8}{"cells":>6}{"join":>6}{"meet":>6}{"Σq|Aq||Bq|−|X|":>16}{"|A||B|−|X|":>12}')
n0,bj0,bm0,f0,g0=price(lambda c:True,'none'); print(f'{"none":<8}{n0:>6}{bj0:>6}{bm0:>6}{f0:>16}{g0:>12}')
for x in SRC+TGT:
    for y in SRC+TGT:
        if (x in SRC)==(y in SRC): continue
        r=price(lambda c,x=x,y=y: c[ix[x]]<=c[ix[y]], f'{x} ≤ {y}')
        rows.append((f'{x} ≤ {y}',)+r)
implied=[r for r in rows if r[1]==976]; real=[r for r in rows if r[1]<976]
real.sort(key=lambda r:-r[1])
for r in real: print(f'{r[0]:<8}{r[1]:>6}{r[2]:>6}{r[3]:>6}{r[4]:>16}{r[5]:>12}')
print(f'candidate bridges {len(rows)} = 4 × 3 × 2; implied on every cell (not admissible): {[r[0] for r in implied]}; admissible {len(real)}')
print(f'closure survives all admissible (join and meet defects 0 on every pair): {all(r[2]==0 and r[3]==0 for r in real)} | rows destroying the factorisation {sum(1 for r in real if r[4]>0)}, defects {min(r[4] for r in real if r[4]>0)} to {max(r[4] for r in real)} | defect-zero rows {[(r[0],r[1]) for r in real if r[4]==0]}')
print(f'five smallest cut sets: {[(r[0],r[1]) for r in sorted(real,key=lambda r:r[1])[:5]]}')
