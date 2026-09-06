from itertools import combinations
from collections import defaultdict
N=['T','M','A','S']
FULL={'T':'THEORY (the functor)','M':'SPACETIME (source objects)',
      'A':'ALGEBRA (target objects)','S':'STATE (functionals)'}
# each charger: (trigger home, jurisdiction homes, currency homes, fires?)
CH={
 'Buniy-Hsu-Murray'      :(['S'],['T'],['A'],True),
 'Hartman-Kundu-Tajdini' :(['S'],['T','M'],['A','T'],False),
 'Wall (GSL)'            :(['M','S'],['T','A'],['A','T'],True),
 'Graham-Olum'           :(['M','S'],['M'],['T'],True),
 'spin-statistics'       :(['A'],['T','A','S'],['A'],True),
 'Ostrogradsky'          :(['T'],['T'],['A'],True),
}
def spans(c):
    t,j,cu,f=CH[c]; return sorted(set(t)|set(j)|set(cu))
print('  THE SYSTEM ON T / M / A / S')
for k,v in FULL.items(): print('     %-2s %s' % (k,v))
print()
print('  %-24s %-10s %-14s %-12s %-14s %s' % ('charger','trigger','jurisdiction','currency','spans','fires'))
for c in CH:
    t,j,cu,f=CH[c]
    print('  %-24s %-10s %-14s %-12s %-14s %s'
          % (c,','.join(t),','.join(j),','.join(cu),','.join(spans(c)),'yes' if f else 'NO'))
print()
def graph(active):
    E=set()
    for c in active:
        for a,b in combinations(spans(c),2): E.add(tuple(sorted((a,b))))
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
    return E,comps,len(E)-len(N)+len(comps)
for lab,act in [('all chargers',set(CH)),
                ('only those that fire',{c for c in CH if CH[c][3]})]:
    E,comps,cy=graph(act)
    print('  %-24s edges %d  components %d  cycles %d  tree %s'
          % (lab,len(E),len(comps),cy,cy==0 and len(comps)==1))
    print('     %s' % ' | '.join(','.join(c) for c in comps))
print()
E,comps,cy=graph({c for c in CH if CH[c][3]})
deg=defaultdict(int)
for a,b in E: deg[a]+=1; deg[b]+=1
print('  degrees (live):', dict(sorted(deg.items(), key=lambda kv:-kv[1])))
print()
print('  WHAT CHANGED AGAINST THE SEVEN-VOCABULARY VERSION')
print('     old: 7 nodes, 8 edges, 2 components once Hartman is removed;')
print('          V3 geometry and V6 solution unreachable from V1 laws.')
print('     new: %d nodes, %d edges, %d component(s), %d cycles.' % (len(N),len(E),len(comps),cy))
print()
print('     the severance was an artefact. V6 was not a node - "self-consistent')
print('     semiclassical" is a RELATION between M and S, not a property of either.')
print('     treating it as a vocabulary created a leaf that only Graham-Olum touched.')
print()
print('     and M stays reachable without Hartman, because WALL spans T, A and M and fires.')
print()
print('  SO WHAT IS THE OBSTRUCTION, RESTATED')
print('     it is not connectivity. every vocabulary is reachable.')
print('     it is that Graham-Olum\'s TRIGGER is achronal ANEC violation (M and S),')
print('     and the core cell has NEC_ach = 0: a LONG wormhole violates the ANEC and')
print('     satisfies the achronal ANEC. the charger is reachable and does not fire')
print('     on the cell in question.')
print()
print('     old statement: "the exclusion lives in a component the law index cannot reach."')
print('     new statement: "the exclusion is reachable and its trigger is not met."')
print('     the second is weaker as an explanation of the defect, and it is correct.')
print()
print('  WHAT STILL EXPLAINS THE DEFECT')
print('     the arity, unchanged: two ternary obstructions, one inside the law letters')
print('     and one on the T/M/S cross-edge. Part VII and 8.2 are untouched.')