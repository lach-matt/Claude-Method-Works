import itertools
from collections import Counter

def F(cells, z): return sum(z**sum(c) for c in cells)

print("="*66); print("The detached-factor lemma"); print("="*66)
# base: the coupled (l,m) part of Lambda_sph, no type axis, no radial axis
def coupled(LM): return [(lp,mp) for lp in range(LM+1) for mp in range(2*lp+3)]
print("\n coupled (l,m) part alone — F(-1) by LMAX")
for LM in range(0,9):
    c=coupled(LM); print(f"   LMAX={LM}: F(1)={len(c):4d}  F(-1)={F(c,-1):3d}")

print("\n same, times a FREE chain of extent k  (k values, 0..k-1)")
for k in [2,3,4,5]:
    row=[]
    for LM in range(0,7):
        cells=[c+(x,) for c in coupled(LM) for x in range(k)]
        row.append(F(cells,-1))
    print(f"   free extent k={k}: F(-1) over LMAX=0..6 -> {row}")

print("\n LEMMA: if X = A x C_k (C_k a free chain of k values),")
print("        F_X(-1) = F_A(-1) * (0 if k even else 1)")
ok=True
for k in range(2,7):
    for LM in range(0,7):
        A=coupled(LM); X=[a+(x,) for a in A for x in range(k)]
        lhs=F(X,-1); rhs=F(A,-1)*(0 if k%2==0 else 1)
        if lhs!=rhs: ok=False; print("   FAIL",k,LM,lhs,rhs)
print("   verified over k=2..6, LMAX=0..6:",ok)

print("\n CONTRAPOSITIVE (the usable form):")
print("   F(-1) != 0  =>  the index has NO free factor of even extent.")

print("\n"+"="*66); print("Applied to the four objects"); print("="*66)
LMAX,NMAX=5,4
sph=[(t,lp,mp,np_) for t in (0,1) for lp in range(LMAX+1)
     for mp in range(2*lp+3) for np_ in range(NMAX+1)]
sph_nt=[(lp,mp,np_) for lp in range(LMAX+1) for mp in range(2*lp+3) for np_ in range(NMAX+1)]
print(f" Lambda_sph      F(1)={len(sph):5d}  F(-1)={F(sph,-1):3d}   free even factor present (TE/TM, k=2)")
print(f"   type removed  F(1)={len(sph_nt):5d}  F(-1)={F(sph_nt,-1):3d}   <- and it is STILL 0")
print("   so F(-1)=0 here is OVERDETERMINED: the free 2-chain is sufficient, not necessary.")
print("   isolate it: coupled part only, LMAX with odd l-count:")
for LM in [0,2,4,6]:
    A=coupled(LM); X=[a+(t,) for a in A for t in (0,1)]
    print(f"     LMAX={LM}: coupled F(-1)={F(A,-1)}   x free C_2 -> {F(X,-1)}")

M=N=L=4
def nu(m,n,l): return (m>0)+(n>0)+(l>0)
cav=[(m,n,l,s) for m in range(M+1) for n in range(N+1) for l in range(L+1)
     for s in range(1,nu(m,n,l))]
cav_int=[(m,n,l,s) for m in range(1,M+1) for n in range(1,N+1) for l in range(1,L+1) for s in (1,2)]
print(f"\n Lambda_cav      F(1)={len(cav):5d}  F(-1)={F(cav,-1):3d}")
print(f"   interior only  F(1)={len(cav_int):5d}  F(-1)={F(cav_int,-1):3d}   = product of chains x C_2")

print("\n Lambda (book)   F(1)= 976  F(-1)= 2   [from the book, not recomputed here]")
print("   2 != 0  =>  Lambda has NO free factor of even extent.")
print("   The proof is already in the book. It has not been read as one.")

print("\n"+"="*66); print("Kernel dimensions"); print("="*66)
rows=[("Ampere -> Maxwell","div . curl = 0","ker(div) = all curls","infinite",
       "INCOMPLETE - covariance supplied externally"),
      ("Lambda_cav","k.E = 0 (transversality)","transverse plane","2",
       "complete; slack = 2-fold polarization"),
      ("Lambda_sph","k.E = 0 + sphere BCs","TE / TM families","2",
       "complete; slack = free C_2 axis"),
      ("Lambda","none - ORDER realised","-","0",
       "complete; slack 0; graph connected")]
w=[18,26,22,9]
print(f" {'object':18s} {'identity':26s} {'kernel':22s} {'dim':9s} verdict")
for r in rows: print(f" {r[0]:18s} {r[1]:26s} {r[2]:22s} {r[3]:9s} {r[4]}")
