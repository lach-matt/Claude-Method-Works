from collections import Counter

CN,CE,CL,CK=3,3,1,3
L=[(n,l,k,q,e,f,g,S2)
   for n in range(1,CN+1) for l in range(0,min(n-1,CL)+1)
   for k in range(1,min(2*(2*l+1),CK)+1) for S2 in range(0,k+1)
   for q in range(0,k+1) for e in range(1,CE+1) for f in range(0,min(e-1,CL)+1)
   for g in range(0,min(q,2*(2*f+1))+1)]
S=set(L)
mx=tuple(max(c[i] for c in L) for i in range(8))
mn=tuple(min(c[i] for c in L) for i in range(8))
print("realised ranges:", list(zip(mn,mx)))

# Convention A: sigma(x) = max - x  (componentwise)
A=[c for c in L if tuple(mx[i]-c[i] for i in range(8)) in S]
# Convention B: sigma(x) = max + min - x  (reflection within realised range)
B=[c for c in L if tuple(mx[i]+mn[i]-c[i] for i in range(8)) in S]

for name,X in (("A: max - x",A),("B: max + min - x",B)):
    ranks=[sum(c) for c in X]
    ev=all(r%2==0 for r in ranks)
    print(f"sigma = {name:18s} survivors = {len(X):3d}   all even rank: {ev}"
          f"   rank multiset: {sorted(Counter(ranks).items())}")

# contribution to F(-1): survivors of even rank contribute +1 each under pairing arguments
for name,X in (("A",A),("B",B)):
    contrib=sum((-1)**sum(c) for c in X)
    print(f"convention {name}: signed survivor sum = {contrib:+d}")
print(f"F(-1) over Lambda = {sum((-1)**sum(c) for c in L):+d}")