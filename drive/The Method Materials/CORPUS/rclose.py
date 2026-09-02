# §32.4.1: R(X) = {x in box : x_i in A_i(X) for all i, and x_i <= phi_ij(x_j) for all i != j},
# phi_ij(a) = max{ y_i : y in X, y_j <= a }.  Tests the three closure properties on random subsets,
# then closure-under-intersection of fixed points over pairs.
import random, itertools, sys
random.seed(20260824)
D,V=4,5                                   # small ambient box: 4 coordinates, values 0..4 (625 cells)
BOX=list(itertools.product(range(V),repeat=D))
def R(X):
    if not X: return frozenset()
    A=[sorted({x[i] for x in X}) for i in range(D)]
    P=[[[-1]*V for _ in range(D)] for _ in range(D)]
    for y in X:
        for i in range(D):
            for j in range(D):
                if i!=j:
                    for a in range(y[j],V):
                        if y[i]>P[i][j][a]: P[i][j][a]=y[i]
    out=[]
    for x in itertools.product(*A):
        if all(x[i]<=P[i][j][x[j]] for i in range(D) for j in range(D) if i!=j): out.append(x)
    return frozenset(out)
def rand_subset():
    k=random.randint(1,40); return frozenset(random.sample(BOX,k))
ext=mono=idem=0; NS=3000
subsets=[rand_subset() for _ in range(NS)]
closures=[]
for X in subsets:
    C=R(X); closures.append(C)
    if not X<=C: ext+=1
    if R(C)!=C: idem+=1
    Y=X|frozenset(random.sample(BOX,3))
    if not C<=R(Y): mono+=1
print('subsets',NS,'extensive failures',ext,'monotone failures',mono,'idempotent failures',idem)
fixed=list({c for c in closures if c})
NP=int(sys.argv[1]) if len(sys.argv)>1 else 3000
fail=0; nonempty=0
for _ in range(NP):
    A,B=random.sample(fixed,2); I=A&B
    if I: nonempty+=1
    if R(I)!=I: fail+=1
print('distinct fixed points',len(fixed),'pairs',NP,'nonempty intersections',nonempty,'closure failures',fail)
