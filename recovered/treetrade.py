from itertools import combinations, product
from collections import defaultdict
N=['V1 laws','V2 theory','V3 geometry','V4 algebra','V5 coupling','V6 solution','V7 degeneracy']
BASE={'Buniy':['V1 laws','V2 theory'],'Graham-Olum':['V3 geometry','V6 solution'],
      'spin-statistics':['V1 laws','V4 algebra'],'Ostrogradsky':['V1 laws','V7 degeneracy']}
def stats(spans):
    E=set()
    for vs in spans:
        for a,b in combinations(sorted(vs),2): E.add((a,b))
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
    return len(E),comp,len(E)-len(N)+comp
CASES=[
 ('Hartman dead, Wall live (actual)',
   list(BASE.values())+[['V1 laws','V4 algebra','V5 coupling']]),
 ('Hartman live (3 indices), Wall live (3)',
   list(BASE.values())+[['V1 laws','V2 theory','V3 geometry'],['V1 laws','V4 algebra','V5 coupling']]),
 ('Hartman reduced to V1-V3, Wall live (3)',
   list(BASE.values())+[['V1 laws','V3 geometry'],['V1 laws','V4 algebra','V5 coupling']]),
 ('Hartman live (3), Wall reduced to V1-V4',
   list(BASE.values())+[['V1 laws','V2 theory','V3 geometry'],['V1 laws','V4 algebra']]),
 ('BOTH reduced to two-index statements',
   list(BASE.values())+[['V1 laws','V3 geometry'],['V1 laws','V4 algebra']]),
]
print('  %-42s %6s %6s %7s %s' % ('configuration','edges','comps','cycles','verdict'))
for lab,spans in CASES:
    e,c,cy=stats(spans)
    v = 'CONNECTED TREE' if (c==1 and cy==0) else ('connected, %d cycle(s)'%cy if c==1 else 'DISCONNECTED (%d comps)'%c)
    print('  %-42s %6d %6d %7d %s' % (lab,e,c,cy,v))
print()
print('  THE TRADE')
print('     Hartman dead  -> V3, V6 unreachable from the law index')
print('     Hartman live  -> connected, but it triangulates V1-V2-V3')
print('     the only way to have both is for Hartman to span TWO indices, not three,')
print('     i.e. for the theorem to hold without one of its vocabularies.')
print()
print('  WHICH VOCABULARY WOULD HAVE TO GO')
print('     Hartman hypotheses : unitary(V1), Lorentz(V1), interacting(V2), d>2(V2), flat(V3)')
print('        dropping V2 (interacting, d>2) leaves V1-V3  -> connects without a cycle')
print('        dropping V3 (flat) leaves V1-V2              -> does NOT connect V3 at all')
print('     Wall hypotheses    : determinism(V4), ultralocality(V4), Lorentz(V1), stability(V4), minimal coupling(V5)')
print('        dropping V5 (minimal coupling) leaves V1-V4  -> removes the second cycle')
print()
print('  SO THE SYSTEM IS A CONNECTED TREE IFF:')
print('     Hartman holds for INTERACTING theories in ANY dimension on CURVED backgrounds')
print('        (drop V2, keep V3) - i.e. exactly the curved-space extension')
print('     AND Wall holds for NON-MINIMALLY coupled fields')
print('        (drop V5) - i.e. exactly the coupling extension')
print()
print('  ECHO OF LAMBDA-9')
print('     Lambda_9 : the tree or the tightness. Taking the exact bound adds a cycle.')
print('     the system: connected or acyclic. Connecting V3 adds a cycle,')
print('        unless the connecting theorem sheds a vocabulary.')
print('     same trade, one level up, and in both cases the resolution is the same:')
print('        a statement that needs fewer places.')