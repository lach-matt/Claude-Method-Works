import itertools,collections,numpy as np
exec(open('tower-2.py').read().split("if __name__")[0]); cells=L8(); S=set(cells)
alph=[sorted(set(c[i] for c in cells)) for i in range(8)]
box=list(itertools.product(*alph)); print('box',len(box))
pairs=list(itertools.combinations(range(8),2))
def close(X):
    sup={p:set((x[p[0]],x[p[1]]) for x in X) for p in pairs}
    return [b for b in box if all((b[i],b[j]) in sup[(i,j)] for (i,j) in pairs)]
C=close(cells); print('closure of Λ8:',len(C),'E =',len(C)-976)
# delete-restore, all 976
restored=sum(1 for x in cells if x in set(close([c for c in cells if c!=x])))
print('deleted cell restored:',restored,'of 976')
# add one outside cell: growth over all 5,936
outside=[b for b in box if b not in S]
growth=collections.Counter()
for b in outside:
    growth[len(close(cells+[b]))-976]+=1
g=sorted(growth.items()); vals=[k for k,n in growth.items() for _ in range(n)]
print('growth (closure size − 976) over',len(outside),'added cells: min',min(vals),'median',sorted(vals)[len(vals)//2],'max',max(vals))
print('cells giving exactly +72 (1,048):',growth.get(72,0)); print('distribution head:',g[:12])
