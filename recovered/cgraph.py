import itertools,collections
def stats(nodes,edges):
    adj={v:set() for v in nodes}
    for a,b in edges: adj[a].add(b); adj[b].add(a)
    def bfs(s):
        d={s:0}; q=[s]
        for u in q:
            for w in adj[u]:
                if w not in d: d[w]=d[u]+1; q.append(w)
        return d
    ecc={v:max(bfs(v).values()) for v in nodes}
    # girth: shortest cycle
    girth=None
    for a,b in edges:
        adj[a].discard(b); adj[b].discard(a); d=bfs(a)
        if b in d: girth=d[b]+1 if girth is None else min(girth,d[b]+1)
        adj[a].add(b); adj[b].add(a)
    tri=sum(1 for a,b,c in itertools.combinations(nodes,3) if b in adj[a] and c in adj[a] and c in adj[b])
    # treewidth<=2 test: reduce degree<=2 vertices (series-parallel reduction)
    A={v:set(adj[v]) for v in nodes}
    changed=True
    while changed and A:
        changed=False
        for v in list(A):
            if len(A[v])<=2:
                nb=list(A[v])
                for u in nb: A[u].discard(v)
                if len(nb)==2: A[nb[0]].add(nb[1]); A[nb[1]].add(nb[0])
                del A[v]; changed=True; break
    tw2=(len(A)==0)
    deg=sorted((len(adj[v]) for v in nodes),reverse=True)
    return dict(nodes=len(nodes),edges=len(edges),cycle_rank=len(edges)-len(nodes)+1,girth=girth,triangles=tri,diameter=max(ecc.values()),radius=min(ecc.values()),
                treewidth_le_2=tw2,degrees=deg,leaves=[v for v in nodes if len(adj[v])==1],hub=max(nodes,key=lambda v:len(adj[v])))
base=['n','l','k','q','e','f','g','2S']; bedges=[('n','l'),('l','k'),('k','q'),('e','f'),('f','g'),('q','g'),('k','2S')]
print('Λ8 base:',stats(base,bedges))
# 0 of 35 edge-triples spanning 3 nodes; near-misses = non-edges whose addition makes a triangle
sp=collections.Counter(len(set(sum(t,()))) for t in itertools.combinations(bedges,3)); print('edge triples by nodes spanned:',dict(sp))
adjb={v:set() for v in base}
for a,b in bedges: adjb[a].add(b); adjb[b].add(a)
nm=[(a,b) for a,b in itertools.combinations(base,2) if b not in adjb[a] and adjb[a]&adjb[b]]
print('near-misses (non-edges closing a triangle):',len(nm),nm,'| unused edges',28-7,'safe',21-len(nm))
fig=base+['v','2Jc','2K','2J']; fedges=bedges+[('2S','v'),('g','v'),('k','2Jc'),('2Jc','2K'),('f','2K'),('2K','2J')]
print('Figure 21.1 (12 nodes):',stats(fig,fedges))
ax=base+["2S'",'v','2Jc','2K','2J']; aedges=bedges+[("2S'",'g'),("2S'",'v'),('v','g'),('k','2Jc'),('2Jc','2K'),('f','2K'),('2K','2J')]
print('§12.11.1 axes (13 nodes):',stats(ax,aedges))
# per-stage cycle rank under each reading
for name,N,E in (('figure',fig,fedges),('axes',ax,aedges)):
    out=[]
    for st,keep in ((8,8),(9,9),(10,10),(11,11),(12,12),(13,13)):
        nn=N[:keep] if name=='axes' else (base+(['v'] if st>=10 else [])+(['2Jc'] if st>=11 else [])+(['2K'] if st>=12 else [])+(['2J'] if st>=13 else []))
        ee=[e for e in E if e[0] in nn and e[1] in nn]; s=stats(nn,ee); out.append((st,s['cycle_rank'],s['triangles']))
    print(name,'stage (rank,triangles):',out)