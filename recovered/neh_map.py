from itertools import product, combinations
NM=['CYC','MOD','NEST','EDGE','TRANS','COND','TRACE']
DEF=[('CYC','a cyclic and separating vector for the cut algebras','Reeh-Schlieder, or a Hadamard state'),
     ('MOD','the modular flow sigma_t exists','T1 Tomita-Takesaki, automatic given CYC'),
     ('NEST','a nested family M(u) on cuts, ordered by causal inclusion','needs no parametrisation'),
     ('EDGE','corner edge modes: a dressing anchor',"Chandrasekaran-Flanagan's (Gamma_0, Upsilon_0)"),
     ('TRANS','a positive-generator translation U(a), U(a)MU(a)* in M','T2 Borchers-Wiesbrock; iff HSMI'),
     ('COND','conditioning on a sharp cut location via the translation edge mode','their step to reach R'),
     ('TRACE','a semifinite trace, hence a von Neumann entropy','T3+T4, given a crossed product by R')]
RNG=[range(2)]*7
CY,MO,NE,ED,TR,CO,TA=range(7)
def close(x):
    x=list(x); g=True
    while g:
        g=False
        def need(a,b):     # a requires b: if a present (0) then b must be present (0)
            nonlocal g
            if x[b]==1 and x[a]==0: x[a]=1; g=True
        need(MO,CY)        # modular flow needs a cyclic separating vector
        need(TR,NE)        # a translation needs something to translate between
        need(CO,ED)        # conditioning needs the translation edge mode
        need(TA,TR)        # the trace needs the crossed product, which needs the translation
        need(TA,CO)        # and the conditioning that reduces the group to R
        need(TA,MO)        # and the modular flow to cross by
    return tuple(x)
def E(S,d):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            m={}
            for c in S:
                if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
            b,o=-99,{}
            for t in sorted(m): b=max(b,m[t]); o[t]=b
            ph[(i,j)]=o
    return sum(1 for x in product(*vals) if all(x[i]<=ph[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j))-len(S)
V={close(c) for c in {close(x) for x in product(*RNG)}}
print('  THE INGREDIENT INDEX')
print('  0 = present, 1 = absent')
print()
for a,b,c in DEF: print('     %-6s %-58s %s' % (a,b,c))
print()
print('  requirement edges (an ingredient is unavailable if what it needs is):')
for a,b in [('MOD','CYC'),('TRANS','NEST'),('COND','EDGE'),('TRACE','TRANS'),('TRACE','COND'),('TRACE','MOD')]:
    print('     %-6s needs %s' % (a,b))
print()
e=E(V,7)
box=2**7
print('  cells %d of %d   E = %d   -> %s' % (len(V),box,e,'CLOSED' if e==0 else 'OPEN'))
print()
print('  THE MAP: WHICH SURFACES SUPPLY WHAT')
def mk(**kw):
    x=[0]*7
    for k,v in kw.items(): x[NM.index(k)]=v
    return close(tuple(x))
CASES=[
 ('Rindler horizon, Minkowski', mk(), 'Bisognano-Wichmann gives TRANS directly'),
 ('Killing horizon (bifurcate)', mk(), 'HSMI proved: Wall; Casini-Teste-Torroba; Witten'),
 ('perturbed Killing horizon',   mk(), 'Chandrasekaran-Flanagan: EDGE supplies TRANS, COND reduces to R'),
 ('ISOLATED HORIZON (NEH)',      mk(TRANS=1), 'everything else present; TRANS is unproved'),
 ('expanding null surface',      mk(TRANS=1), 'as NEH, and the generator picks up the two-sided term'),
 ('a bare null hypersurface',    mk(EDGE=1,TRANS=1), 'no corner structure, no anchor'),
]
print('  %-30s %s   %s' % ('surface',' '.join('%-5s'%n for n in NM),'note'))
for n,c,note in CASES:
    print('  %-30s %s   %s' % (n,' '.join('%-5d'%v for v in c),note))
print()
print('  THE GAP, LOCATED')
kh=mk(); neh=mk(TRANS=1)
d=[NM[i] for i in range(7) if kh[i]!=neh[i]]
print('     Killing horizon vs isolated horizon differ in: %s' % d)
print('     and the closure propagates it: TRACE goes 0 -> %d' % neh[TA])
print()
print('     so the map is a chain with ONE broken link:')
print('        CYC ok -> MOD ok -> NEST ok -> EDGE ok -> [TRANS ??] -> COND ok -> TRACE blocked')
print()
print('  WHAT EACH SURFACE CAN AND CANNOT REACH')
for n,c,note in CASES:
    print('     %-30s trace: %s' % (n, 'YES' if c[TA]==0 else 'NO'))
print()
print('  AND WHY T2 IS THE WHOLE PROBLEM')
print('     Borchers-Wiesbrock: HSMI is CHARACTERISED by the existence of U(a) with')
print('     positive generator. so TRANS and HSMI are the same cell, not two.')
print('     every other ingredient is supplied on an NEH:')
print('        CYC   a Hadamard state exists on an NEH')
print('        MOD   follows from CYC')
print('        NEST  causal inclusion of cross-sections, no parametrisation needed')
print('        EDGE  Ashtekar NEH structure gives the corner data')
print('        COND  conditioning is a choice, not a theorem')
print('     -> six of seven present, one unproved, and the unproved one gates the trace.')