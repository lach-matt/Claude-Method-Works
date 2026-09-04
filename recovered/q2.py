import itertools
B={'nothing':0,'novelty':1,'one claim':2,'a result':3}; O={'retrievable':0,'buildable':1,'nonexistent':2}; C={'hours':0,'days':1,'unbounded':2}
def ok(c): return not (c[1]==O['buildable'] and c[2]>C['days'])
def close(X,con=True):
    X=set(X)
    while True:
        n=set(X)
        for a,b in itertools.combinations(X,2):
            for c in (tuple(map(max,zip(a,b))),tuple(map(min,zip(a,b)))):
                if (not con) or ok(c): n.add(c)
        if n==X: return X
        X=n
items={'A':('physical','one claim','nonexistent','unbounded'),'B':('bibliographic','nothing','retrievable','days'),
'C':('bibliographic','nothing','retrievable','unbounded'),'D':('computational','one claim','retrievable','days'),
'F':('mathematical','nothing','buildable','days'),'G':('bibliographic','nothing','retrievable','hours'),
'H':('physical','one claim','retrievable','days'),'I':('physical','one claim','retrievable','days'),
'K':('mathematical','nothing','retrievable','hours'),'M':('computational','one claim','buildable','days'),
'N':('mathematical','nothing','retrievable','days'),'O':('mathematical','one claim','buildable','days'),
'P':('physical','one claim','retrievable','hours')}
def cell(i): d,b,o,c=i; return (B[b],O[o],C[c])
def E(its,con=True,fib=True):
    if not fib:
        X={cell(v) for v in its.values()}; return len(close(X,con)-X)
    tot=0
    for d in {v[0] for v in its.values()}:
        X={cell(v) for v in its.values() if v[0]==d}; tot+=len(close(X,con)-X)
    return tot
print('thirteen: fibred+constraint',E(items),'| unfibred+constraint',E(items,fib=False),'| unfibred, no constraint',E(items,con=False,fib=False))
for lab,R in [('R as printed: one claim·buildable·unbounded',('mathematical','one claim','buildable','unbounded')),
              ('R as entered: nothing·buildable·unbounded',('mathematical','nothing','buildable','unbounded'))]:
    it=dict(items); it['R']=R
    print(lab,'| admissible under constraint:',ok(cell(R)),'| fibred+con',E(it),'| unfibred+con',E(it,fib=False),'| unfibred no-con',E(it,con=False,fib=False))