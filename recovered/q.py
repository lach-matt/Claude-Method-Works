import itertools
B={'nothing':0,'one claim':1}; O={'nonexistent':0,'retrievable':1,'buildable':2}; C={'hours':0,'days':1,'unbounded':2}
items={'A':('one claim','nonexistent','unbounded'),'B':('nothing','retrievable','days'),'C':('nothing','retrievable','unbounded'),
'D':('one claim','retrievable','days'),'F':('nothing','buildable','days'),'G':('nothing','retrievable','hours'),
'H':('one claim','retrievable','days'),'I':('one claim','retrievable','days'),'P':('one claim','retrievable','hours'),
'R':('one claim','buildable','unbounded')}
def close(X):
    X=set(X)
    while True:
        n=set(X)
        for a,b in itertools.combinations(X,2):
            n.add(tuple(max(x,y) for x,y in zip(a,b))); n.add(tuple(min(x,y) for x,y in zip(a,b)))
        if n==X: return X
        X=n
def inv(d): return {v:k for k,v in d.items()}
def run(keys):
    cells={(B[b],O[o],C[c]) for k,(b,o,c) in items.items() if k in keys}
    cl=close(cells); ex=cl-cells
    print(len(keys),'open items, unfibred E =',len(ex), sorted((inv(B)[a],inv(O)[b],inv(C)[c]) for a,b,c in ex))
run('ABCDFGHIP'); run('ABCDFGHIPR')