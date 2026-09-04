import math, collections, statistics
from tower2mod import STAGES, L9, L13
from l33b import E
box={8:6912,9:27648,10:110592,11:663552,12:5308416,13:47775744}
for d in range(8,14):
    X=STAGES[d](); n=len(X); b=box[d]
    print(f'L{d}: {n} box {b} fill {100*n/b:.2f}% ({100*n/b:.6f}%) bits box {math.log2(b):.2f} cells {math.log2(n):.2f} surplus {math.log2(b)-math.log2(n):.2f}')
p=[c for c in L9() if c[8]<=2*c[5]+1]; print(f"L9': {len(p)} fill {100*len(p)/27648:.2f}% E={E(p)}")
T=L13(); cls=set((c[2],c[10],c[12]) for c in T); print('joint (k,2Jc,2J) classes on L13:',len(cls))
# entry 38
rk=[sum(c) for c in T]; vals=sorted(set(rk)); print('L13 rank values',len(vals),f'bits {math.log2(len(vals)):.2f} lost {math.log2(len(T))-math.log2(len(vals)):.2f} compression {len(T)/len(vals):.0f}:1 survives {100*math.log2(len(vals))/math.log2(len(T)):.0f}%')
A=L9(); r9=collections.Counter(sum(c) for c in A); print('L9 rank values',len(r9),'fibres min/max',min(r9.values()),max(r9.values()))
src=collections.defaultdict(list)
for c in A: src[(c[0],c[1],c[2],c[7])].append(c)
out=collections.defaultdict(set); pairs=0
for a in A:
    for b in src.get((a[4],a[5],a[6],a[8]),[]):
        comp=(a[0],a[1],a[2],min(a[3],b[3]),b[4],b[5],b[6],a[7],b[8]); pairs+=1
        out[(sum(a),sum(b))].add(sum(comp))
single=sum(1 for v in out.values() if len(v)==1); spread=max(len(v) for v in out.values()); allr=set().union(*out.values())
print('composable pairs',pairs,'distinct input-rank pairs',len(out),f'single output {single} ({100*single/len(out):.0f}%) worst spread {spread} composite rank range [{min(allr)},{max(allr)}]')
