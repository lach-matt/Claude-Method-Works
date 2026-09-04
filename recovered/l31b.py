import time
from l31 import ext
X=ext(None)
for name,w in {'max':lambda c:max(c[4],c[5],c[9],c[8])<=max(c[0],c[1],c[2],c[7]),'min':lambda c:min(c[4],c[5],c[9],c[8])<=min(c[0],c[1],c[2],c[7])}.items():
    Y=[c for c in X if w(c)]; S=set(Y); jf=mf=0; t0=time.time()
    for i in range(len(Y)):
        x=Y[i]
        for y in Y[i+1:]:
            if tuple(map(max,x,y)) not in S: jf+=1
            if tuple(map(min,x,y)) not in S: mf+=1
    print(f'{name}: {len(Y)} cells, join failures {jf}, meet failures {mf}, {round(time.time()-t0)}s')