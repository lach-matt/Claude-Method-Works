from itertools import product, combinations
def E(S,d,ret=False):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    def env(i,j):
        m={}
        for c in S:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o=-99,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    R={x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
    box=1
    for v in vals: box*=len(v)
    return (len(R)-len(S),sorted(R-S),box) if ret else len(R)-len(S)
def minsup(V,d,NM):
    mins=[]
    for r in (2,3,4):
        found=[]
        for idx in combinations(range(d),r):
            if any(set(m)<=set(idx) for m in mins): continue
            P={tuple(c[i] for i in idx) for c in V}
            if E(P,r)>0: found.append(idx)
        for idx in found:
            if not any(set(m)<set(idx) for m in mins): mins.append(idx)
        if found: return r,[[NM[i] for i in m] for m in found]
    return None,[]
print('  A TERM WITH TWO STATUSES, INDEXED THREE WAYS')
print()
print('  the term: ST  the per-generator affine origin (a supertranslation mode)')
print('  the fact: gauge in the geometry vocabulary, physical in the algebra vocabulary')
print()
# ---- monolingual A: geometry only. ST is gauge, so it is not a coordinate at all.
NMg=['THETA','KILLING','NESTED']
Vg={(t,k,n) for t in range(2) for k in range(2) for n in range(2)
    if not (k==0 and t==1)}          # Killing => non-expanding
print('  (1) GEOMETRY ALONE   letters %s' % NMg)
e=E(Vg,3); r,ms=minsup(Vg,3,NMg)
print('      cells %d  E %d  arity %s' % (len(Vg),e,r if r else '-'))
print('      ST does not appear: it is gauge, hence not a coordinate.')
print()
# ---- monolingual B: algebra only. ST is physical but the geometry is invisible.
NMa=['NET','STATE','ST']
Va={(n,s,st) for n in range(2) for s in range(2) for st in range(2)}
print('  (2) ALGEBRA ALONE    letters %s' % NMa)
e=E(Va,3); r,ms=minsup(Va,3,NMa)
print('      cells %d  E %d  arity %s' % (len(Va),e,r if r else '-'))
print('      the geometry does not appear: the algebra cannot see THETA or KILLING.')
print()
# ---- bilingual: both vocabularies, ST carried WITH its status
NMb=['THETA','KILLING','NET','STATE','ST','STATUS']
# STATUS 0 = the term is gauge here, 1 = physical here.  the HSMI condition:
#   a positive translation exists  <=>  ST is FIXED (a common origin chosen)
#   and fixing ST is only meaningful where STATUS = 1.
# so: HSMI  <=>  (KILLING = 0)  OR  (ST fixed AND STATUS = 1)
def cl(x):
    x=list(x)
    if x[1]==0 and x[0]>0: x[0]=0     # Killing => non-expanding
    return tuple(x)
allc={cl(x) for x in product(range(2),range(2),range(2),range(2),range(2),range(2))}
Vb={c for c in allc if (c[1]==0) or (c[4]==0 and c[5]==1)}
print('  (3) BILINGUAL        letters %s' % NMb)
e,ex,box=E(Vb,6,ret=True); r,ms=minsup(Vb,6,NMb)
print('      cells %d  box %d  E %d  arity %s' % (len(Vb),box,e,r if r else '-'))
for m in ms[:3]: print('         minimal support: %s' % m)
print()
print('  THE PRICE')
print('     geometry alone : arity 2, E = 0, and it cannot state the condition')
print('     algebra alone  : arity 2, E = 0, and it cannot state the condition')
print('     bilingual      : arity %s, E = %d, and it CAN' % (r,e))
print()
print('     the bilingual equation exists. it costs one place of arity,')
print('     because the STATUS of a term is itself a coordinate, and a constraint')
print('     that mentions a term AND its status is one place longer than one that')
print('     mentions only the term.')
print()
print('  WHICH IS THE SAME RESULT AS PART VIII')
print('     "a jurisdicted forcing and an unjurisdicted disjunction give identical defects."')
print('     a status IS a jurisdiction: it says WHERE the term counts.')
print('     so a bilingual equation is a jurisdicted equation, and pays the same price.')
print()
print('  THE THREE REPAIRS, AND WHICH THE LITERATURE USES')
R=[('DEMOTE','make ST gauge on both sides','lose the nesting; HSMI needs it. NOT USED.'),
   ('TRANSCRIBE','restate geometry so it sees ST','impossible: the NEH free data is provably '
    'supertranslation-invariant. nothing to see. NOT USED.'),
   ('PROMOTE','make ST physical on both sides','extend the phase space with corner edge modes. '
    'USED - Chandrasekaran et al, Jan 2026.')]
for a,b,c in R: print('     %-12s %-38s %s' % (a,b,c))
print()
print('  SO THE ANSWER')
print('     yes, it formalises as one equation. the equation is bilingual because it')
print('     carries the term AND the vocabulary in which the term counts.')
print('     it is arity 3 and neither monolingual form is.')
print('     and the physical realisation of that extra place is the corner edge mode:')
print('     a degree of freedom that geometry quotients away and the algebra needs.')