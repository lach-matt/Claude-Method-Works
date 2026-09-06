from itertools import combinations
from collections import defaultdict
IDX={'V1 laws':15,'V2 theory':4,'V3 geometry':5,'V4 algebra':5,
     'V5 coupling':1,'V6 solution':1,'V7 degeneracy':1}
CH={'Buniy'          :['V1 laws','V2 theory'],
    'Hartman'        :['V1 laws','V2 theory','V3 geometry'],
    'Wall'           :['V1 laws','V4 algebra','V5 coupling'],
    'Graham-Olum'    :['V3 geometry','V6 solution'],
    'spin-statistics':['V1 laws','V4 algebra'],
    'Ostrogradsky'   :['V1 laws','V7 degeneracy']}
print('  THE SYSTEM OF INDICES')
for v,n in IDX.items(): print('     %-16s %2d terms' % (v,n))
print()
print('  CHARGERS AS MAPS BETWEEN INDICES')
E=set(); deg=defaultdict(int)
for ch,vs in CH.items():
    print('     %-18s spans %d : %s' % (ch,len(vs),' - '.join(vs)))
    for a,b in combinations(sorted(vs),2): E.add((a,b))
for a,b in E: deg[a]+=1; deg[b]+=1
print()
N=list(IDX)
print('  THE INDEX GRAPH')
print('     nodes %d   edges %d   cycles = E - N + components' % (len(N),len(E)))
adj=defaultdict(set)
for a,b in E: adj[a].add(b); adj[b].add(a)
seen=set(); comp=0
for v in N:
    if v in seen: continue
    comp+=1; st=[v]; seen.add(v)
    while st:
        u=st.pop()
        for w in adj[u]:
            if w not in seen: seen.add(w); st.append(w)
print('     components %d   cycles %d   tree: %s' % (comp,len(E)-len(N)+comp,len(E)-len(N)+comp==0))
print()
print('  DEGREES')
for v in sorted(N,key=lambda x:-deg[x]): print('     %-16s degree %d' % (v,deg[v]))
print()
print('  THE CYCLES')
for ch,vs in CH.items():
    if len(vs)>=3:
        print('     %-18s creates a triangle: %s' % (ch,' - '.join(sorted(vs))))
print()
print('  CUT VERTICES OF THE SYSTEM')
def comps(nodes):
    a=defaultdict(set)
    for x,y in E:
        if x in nodes and y in nodes: a[x].add(y); a[y].add(x)
    s=set(); c=0
    for v in nodes:
        if v in s: continue
        c+=1; st=[v]; s.add(v)
        while st:
            u=st.pop()
            for w in a[u]:
                if w not in s: s.add(w); st.append(w)
    return c
base=comps(set(N))
cuts=[v for v in N if comps(set(N)-{v})>base]
print('     %s' % (', '.join(cuts) if cuts else 'none'))
print()
print('  CONSEQUENCE')
print('     Freuder: a TREE-structured constraint network is globally consistent after arc consistency.')
print('     the system of indices is not a tree - two chargers span three indices each.')
print('     so the system cannot be closed by propagating between indices,')
print('     for exactly the reason Lambda_9-prime cannot: an added edge makes a cycle.')
print()
print('     and Montanari does not rescue it: cross-index constraints are not monotone bounds,')
print('     they are conjunctions of conditions in different vocabularies.')
print()
print('  WHAT WOULD CLOSE IT')
print('     removing either three-index charger leaves %d cycles.' % (len(E)-len(N)+comp-2))
print('     both would have to become two-index statements - i.e. a theorem would have to')
print('     drop one of its vocabularies. Hartman would need to drop geometry (flatness),')
print('     Wall to drop coupling (minimal coupling). Neither is a bookkeeping choice.')