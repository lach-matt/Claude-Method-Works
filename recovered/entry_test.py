"""Entry test of The Method 1.3, per §27.12:
rebuild Lambda from the constraint system of §7.1, the caps of §7.4 and the
bounds of §12.11.1, and reproduce the seven tower cell counts.
Nothing is imported from the book except the definitions.
"""
from itertools import product

# caps of §7.4 as used for the tower: (n, e, ell, k, f) = (3,3,1,3,1)
NM, EM, LM, KM, FM = 3, 3, 1, 3, 1

N  = range(1, NM+1)
L  = range(0, LM+1)
K  = range(1, KM+1)          # §10.2 / register 301: k >= 1, the eighth condition
Q  = range(0, KM+1)
E_ = range(1, EM+1)
F  = range(0, FM+1)
G  = range(0, KM+1)
S2 = range(0, KM+1)          # 2S
S2p= range(0, KM+1)          # 2S'
V  = range(0, KM+1)          # seniority v
JC = range(0, 6)             # 2J_c
KK = range(0, 8)             # 2K
JJ = range(0, 9)             # 2J

phi_hat = {1: 3, 2: 4, 3: 5}   # §12.11.3.1, envelope of realised maxima

def lam8():
    for n,l,k,q,e,f,g,s in product(N,L,K,Q,E_,F,G,S2):
        if l > n-1: continue
        if k > 2*(2*l+1): continue
        if q > k: continue
        if f > e-1: continue
        if g > 2*(2*f+1): continue
        if g > q: continue
        if s > k: continue
        yield (n,l,k,q,e,f,g,s)

L8 = list(lam8())

def extend(base, values, ok):
    return [c + (v,) for c in base for v in values if ok(c, v)]

# axis 9: 2S' <= g   (g is index 6)
L9  = extend(L8, S2p, lambda c,v: v <= c[6])
# axis 9': + 2S' <= 2f+1   (f is index 5)
L9p = extend(L8, S2p, lambda c,v: v <= c[6] and v <= 2*c[5]+1)
# axis 10: 2S' <= v <= g
L10 = extend(L9, V,   lambda c,v: c[8] <= v <= c[6])
# axis 11: 2J_c <= phi_hat(k)   (k is index 2)
L11 = extend(L10, JC, lambda c,v: v <= phi_hat[c[2]])
# axis 12: 2K <= 2J_c + 2*f_max
L12 = extend(L11, KK, lambda c,v: v <= c[10] + 2*FM)
# axis 13: |2J - 2K| <= 1
L13 = extend(L12, JJ, lambda c,v: abs(v - c[11]) <= 1)

boxes = {8:6912, 9:27648, "9'":27648, 10:110592, 11:663552, 12:5308416, 13:47775744}
stated = {8:976, 9:1654, "9'":1561, 10:2535, 11:13585, 12:70905, 13:199130}
got = {8:len(L8), 9:len(L9), "9'":len(L9p), 10:len(L10), 11:len(L11),
       12:len(L12), 13:len(L13)}

print("ENTRY TEST (§27.12)")
print(f"{'stage':>6} {'stated':>9} {'computed':>9} {'box':>10} {'fill':>7}  verdict")
for s in [8,9,"9'",10,11,12,13]:
    fill = 100*got[s]/boxes[s]
    v = "OK" if got[s]==stated[s] else "MISMATCH"
    print(f"{'L'+str(s):>6} {stated[s]:>9,} {got[s]:>9,} {boxes[s]:>10,} {fill:>6.2f}%  {v}")

# ---- ambient box check, independently ----
amb8 = len(N)*len(L)*len(K)*len(Q)*len(E_)*len(F)*len(G)*len(S2)
print(f"\nambient box of L8 recomputed: {amb8:,}")
print(f"title identity |PROD A_i| = |X| + E(X) + refused: "
      f"{amb8:,} = {len(L8):,} + E + refused")
