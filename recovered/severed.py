from itertools import combinations
from collections import defaultdict
CH={'Buniy'          :(['V1 laws','V2 theory'],'fires'),
    'Hartman'        :(['V1 laws','V2 theory','V3 geometry'],'VACUOUS - trigger needs curvature, jurisdiction needs flatness'),
    'Wall'           :(['V1 laws','V4 algebra','V5 coupling'],'fires'),
    'Graham-Olum'    :(['V3 geometry','V6 solution'],'fires'),
    'spin-statistics':(['V1 laws','V4 algebra'],'fires'),
    'Ostrogradsky'   :(['V1 laws','V7 degeneracy'],'fires')}
N=['V1 laws','V2 theory','V3 geometry','V4 algebra','V5 coupling','V6 solution','V7 degeneracy']
def build(active):
    E=set()
    for ch,(vs,st) in CH.items():
        if ch not in active: continue
        for a,b in combinations(sorted(vs),2): E.add((a,b))
    return E
def components(E):
    adj=defaultdict(set)
    for a,b in E: adj[a].add(b); adj[b].add(a)
    seen=set(); comps=[]
    for v in N:
        if v in seen: continue
        st=[v]; seen.add(v); g=[]
        while st:
            u=st.pop(); g.append(u)
            for w in adj[u]:
                if w not in seen: seen.add(w); st.append(w)
        comps.append(sorted(g))
    return comps
print('  CHARGER STATUS')
for ch,(vs,st) in CH.items(): print('     %-18s %-8s %s' % (ch,'spans %d'%len(vs),st))
print()
allch=set(CH)
E=build(allch); C=components(E)
print('  ALL CHARGERS ACTIVE')
print('     edges %d   components %d : %s' % (len(E),len(C),' | '.join(', '.join(c) for c in C)))
print()
live={ch for ch,(vs,st) in CH.items() if st=='fires'}
E2=build(live); C2=components(E2)
print('  ONLY CHARGERS THAT ACTUALLY FIRE')
print('     edges %d   components %d' % (len(E2),len(C2)))
for c in C2: print('        %s' % ', '.join(c))
print()
hub=[c for c in C2 if 'V1 laws' in c][0]
print('  REACHABLE FROM THE LAW INDEX: %s' % ', '.join(hub))
unreach=[v for v in N if v not in hub]
print('  UNREACHABLE           : %s' % ', '.join(unreach))
print()
print('  WHAT LIVES IN THE UNREACHABLE COMPONENT')
print('     V3 geometry : flat, asymptotically flat, simply connected, globally hyperbolic, generic')
print('     V6 solution : self-consistent semiclassical')
print('     the charger on that edge is GRAHAM-OLUM - the wormhole and time-machine exclusion.')
print()
print('  THE BLIND SPOT, RESTATED')
print('     the exclusion of macroscopic wormholes lives on the edge V3 - V6.')
print('     the law index is not an endpoint of that edge.')
print('     the only path to it runs V1 - V3 via Hartman, and Hartman never fires.')
print('     so the law index cannot reach the theorem that would exclude the core cell,')
print('     and no operation on the law alphabet can change that:')
print('     it is a property of the SYSTEM graph, not of the index.')
print()
print('  WHAT WOULD RECONNECT IT')
for ch,(vs,st) in CH.items():
    if 'V1 laws' in vs and 'V3 geometry' in vs:
        print('     %s - the sole V1-V3 edge. It reconnects if its trigger and jurisdiction' % ch)
        print('        can both be satisfied, i.e. if ANEC violation is proven in FLAT spacetime,')
        print('        or if the theorem is extended to curved backgrounds.')
print('     alternatively a NEW charger spanning V1 and V3, or V1 and V6, would do it.')
print('     candidate: a theorem linking a law-class to self-consistency of the semiclassical solution.')