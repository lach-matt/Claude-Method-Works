import itertools, numpy as np
np.random.seed(7)

# ---------- COMMITTED BEFORE COMPUTING (B.2.13) ----------
# C1: X (natural coords) is join-closed but NOT meet-closed; E(X) = M+N+L+1.
# C2: no chain-order of the three families {TM, TE_a, TE_b} gives monotone caps (all 6 fail).
# C3: min-form caps preserve sublattice closure; the sum-form cap here breaks it.
# C4: for generic (a,b,d) the only degeneracies are the M*N*L TE/TM pairs.
# C5: overlap-greedy labelling of a perturbed near-degenerate spectrum yields >=1
#     bracket violation localized at mixed pairs; optimal (block-exhaustive) labelling yields 0.

M=N=L=6
def z(x): return 1 if x>0 else 0
def cap(m,n,l): return z(m)+z(n)+z(l)-2   # polarization cap (sum-form)

X = set()
for m,n,l in itertools.product(range(M+1),range(N+1),range(L+1)):
    b = cap(m,n,l)
    for p in range(0, b+1):
        X.add((m,n,l,p))
print("|X| =", len(X), " formula 2MNL+MN+ML+NL =", 2*M*N*L+M*N+M*L+N*L)

def meet(u,v): return tuple(min(a,b) for a,b in zip(u,v))
def join(u,v): return tuple(max(a,b) for a,b in zip(u,v))

# join closure check (exhaustive, B.2.7)
Xl = list(X)
jfail = sum(1 for u,v in itertools.combinations(Xl,2) if join(u,v) not in X)
mfail = sum(1 for u,v in itertools.combinations(Xl,2) if meet(u,v) not in X)
print("join failures:", jfail, "| meet failures:", mfail)

# closure to fixpoint
R = set(X)
while True:
    add = set()
    Rl = list(R)
    for u,v in itertools.combinations(Rl,2):
        w = meet(u,v)
        if w not in R: add.add(w)
        w = join(u,v)
        if w not in R: add.add(w)
    if not add: break
    R |= add
E = len(R)-len(X)
added = sorted(R-X)
print("E(X) =", E, " committed M+N+L+1 =", M+N+L+1)
print("added cells (pattern):", sorted(set(tuple(z(c) for c in a[:3]) for a in added)))

# R closed => sublattice of product of chains => distributive (verify median law on sample)
Rl = list(R); ok=True
idx = np.random.randint(0,len(Rl),(4000,3))
for i,j,k in idx:
    a,b,c = Rl[i],Rl[j],Rl[k]
    lhs = meet(join(a,b), join(join(b,c), join(c,a)))
    rhs = join(join(meet(a,b), meet(b,c)), meet(c,a))
    if lhs!=rhs: ok=False; break
print("distributive (median law, 4000 triples):", ok)

# three-box decomposition exact & disjoint? (compute it, per the collaborator's note)
TM  = {(m,n,l,0) for m in range(1,M+1) for n in range(1,N+1) for l in range(0,L+1)}
TEa = {(m,n,l,pp) for m in range(1,M+1) for n in range(0,N+1) for l in range(1,L+1)
       for pp in ([1] if n>0 else [0])}  # careful: coding TE as p=1 when TM coexists
# honest recoding: family membership from pattern, not p-value tricks:
fam = {}
for c in X:
    m,n,l,p = c
    if p==1: fam[c]='TE'                      # second polarization at all-nonzero
    elif m>=1 and n>=1: fam[c]='TM'           # p=0, m,n>=1 (l may be 0): TM_mnl
    else: fam[c]='TE'                          # p=0 with m=0 or n=0: TE only
cnt = {'TM':0,'TE':0}
for c in X: cnt[fam[c]]+=1
print("TM cells:", cnt['TM'], "= MN(L+1)?", M*N*(L+1),
      "| TE cells:", cnt['TE'], "= ((M+1)(N+1)-1)L?", ((M+1)*(N+1)-1)*L)

# C2: family chain-order monotone caps? families as boxes:
# TM: x<=M-1,y<=N-1,zc<=L ; TEa(m>=1): x<=M-1,y<=N,zc<=L-1 ; TEb(m=0,n>=1): x<=0,y<=N-1,zc<=L-1
capsF = {'TM':(M-1,N-1,L), 'TEa':(M-1,N,L-1), 'TEb':(0,N-1,L-1)}
good=[]
for perm in itertools.permutations(['TM','TEa','TEb']):
    seq=[capsF[f] for f in perm]
    mono = all(all(seq[i][k]<=seq[i+1][k] for k in range(3)) for i in range(2))
    if mono: good.append(perm)
print("monotone family chain-orders:", good if good else "none (all 6 fail)")

# C3: min-form vs sum-form caps (random trials)
def trial(capfun, tries=300):
    fails=0
    for _ in range(tries):
        pts=[]
        while len(pts)<2:
            x=tuple(np.random.randint(0,5,3))
            b=capfun(x)
            if b>=0: pts.append((x,np.random.randint(0,b+1)))
        (x1,p1),(x2,p2)=pts
        xm=tuple(min(a,b) for a,b in zip(x1,x2)); pm=min(p1,p2)
        if not (capfun(xm)>=0 and pm<=capfun(xm)): fails+=1
    return fails
g1=lambda x: min(x[0], 4*x[1]+2, x[2]+3)          # min-form (book's Pauli shape)
g2=lambda x: z(x[0])+z(x[1])+z(x[2])-2            # sum-form (cavity)
print("min-form meet failures:", trial(g1), "| sum-form meet failures:", trial(g2), "/300")