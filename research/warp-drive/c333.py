import itertools, random, time
from common import *
from lean3 import lean
random.seed(7)
box=list(itertools.product(range(3),repeat=3))
n=0; bad={}
t0=time.time()
while time.time()-t0 < 240:
    k=random.randint(1,27)
    X=random.sample(box,k)
    if not all({x[i] for x in X}=={0,1,2} for i in range(3)): continue
    r=lean(observed(X)); n+=1
    if r: bad.setdefault(r,[]).append(X)
print("3x3x3 random surjective cases:",n,"FAIL:",{k:(len(v),v[0]) for k,v in bad.items()} or "none")
