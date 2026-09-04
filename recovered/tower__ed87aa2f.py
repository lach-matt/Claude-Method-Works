from itertools import product
import json, sys

# ---- Lambda_8 from §7.1 + §7.4 caps (3,3,1,3): n<=3, e<=3, l,f<=1, k<=3, and k>=1 ----
L8 = []
for n in (1,2,3):
    for l in range(0, min(n-1,1)+1):
        for k in range(1, min(4*l+2,3)+1):
            for q in range(0, k+1):
                for e in (1,2,3):
                    for f in range(0, min(e-1,1)+1):
                        for g in range(0, min(4*f+2,q)+1):
                            for S2 in range(0, k+1):
                                L8.append((n,l,k,q,e,f,g,S2))
L8 = sorted(set(L8))
alph = [sorted(set(c[i] for c in L8)) for i in range(8)]
box = 1
for a in alph: box *= len(a)
print("Λ8: cells =", len(L8), " box =", box)

# E via double projection over the box
def E_defect(X, alph):
    Xs = set(X); d = len(alph)
    pairs = [(i,j) for i in range(d) for j in range(i+1,d)]
    proj = {p: set((x[p[0]],x[p[1]]) for x in Xs) for p in pairs}
    R = 0
    for y in product(*alph):
        if all((y[i],y[j]) in proj[(i,j)] for (i,j) in pairs): R += 1
    return R - len(Xs)
print("Λ8: E =", E_defect(L8, alph))

# rank = coordinate sum; fingerprints
rk = {}
for c in L8: rk[sum(c)] = rk.get(sum(c),0)+1
lo, hi = min(rk), max(rk)
fwd = [rk[r] for r in range(lo, lo+6)]
bwd = [rk[r] for r in range(hi, hi-6, -1)]
F1 = sum(rk.values()); mean = sum(r*v for r,v in rk.items())/F1
Fm1 = sum(v*(-1)**r for r,v in rk.items())
mx = tuple(a[-1] for a in alph)
selfdual = sum(1 for c in L8 if tuple(m-x for m,x in zip(mx,c)) == c)
print("rank span %d..%d | fwd %s | bwd %s" % (lo,hi,fwd,bwd))
print("F(1)=%d  mean rank=%.4f  F(-1)=%d  self-dual=%d" % (F1, mean, abs(Fm1), selfdual))
json.dump([list(c) for c in L8], open("L8.json","w"))