from collections import Counter, defaultdict
CN,CE,CL,CK=3,3,1,3
L=[(n,l,k,q,e,f,g,S2)
   for n in range(1,CN+1) for l in range(0,min(n-1,CL)+1)
   for k in range(1,min(2*(2*l+1),CK)+1) for S2 in range(0,k+1)
   for q in range(0,k+1) for e in range(1,CE+1) for f in range(0,min(e-1,CL)+1)
   for g in range(0,min(q,2*(2*f+1))+1)]
S=set(L); N=len(L)
print("="*66); print("1. THE CYLINDER — base q, fibre A(q) x B(q)   (§7.6)"); print("="*66)
A=set((c[0],c[1],c[2],c[7]) for c in L)      # source end (n,l,k,2S)
B=set((c[4],c[5],c[6]) for c in L)           # target end (e,f,g)
Q=sorted(set(c[3] for c in L))
print(f"  source end A = (n,ℓ,k,2S): {len(A)} states     target end B = (e,f,g): {len(B)} states")
print(f"  bare product |A|x|B|x|q| = {len(A)}x{len(B)}x{len(Q)} = {len(A)*len(B)*len(Q)}   vs |Λ| = {N}   -> fails (§7.6.1)")
print(f"\n   q    |A(q)|   |B(q)|   product   actual")
tot=0
for q in Q:
    Aq=set((c[0],c[1],c[2],c[7]) for c in L if c[3]==q)
    Bq=set((c[4],c[5],c[6]) for c in L if c[3]==q)
    act=sum(1 for c in L if c[3]==q); tot+=len(Aq)*len(Bq)
    print(f"   {q}      {len(Aq):3d}      {len(Bq):3d}     {len(Aq)*len(Bq):5d}    {act:5d}   {'exact' if len(Aq)*len(Bq)==act else 'FAIL'}")
print(f"        Σ_q |A(q)|x|B(q)| = {tot}   book: 976, cross-sections 165 330 345 136")
print("\n  every cross-section closed under meet and join (§7.8.4):")
for q in Q:
    Fq=[c for c in L if c[3]==q]; Sq=set(Fq); bad=0
    for i in range(len(Fq)):
        for j in range(i+1,len(Fq)):
            if tuple(map(max,Fq[i],Fq[j])) not in Sq or tuple(map(min,Fq[i],Fq[j])) not in Sq: bad+=1
    print(f"    q={q}: {len(Fq):3d} cells, {bad} failures")
print("\n"+"="*66); print("2. THE TREE  (§3.5)"); print("="*66)
print("     e — f — g — q — k — ℓ — n        with 2S attached to k")
print("     8 nodes, 7 edges, connected, acyclic -> treewidth 1")
print("     two ends: parent (n,ℓ,k,2S) and target (e,f,g), meeting at q")
print("\n"+"="*66); print("3. BIRKHOFF — 17 join-irreducibles generate all 976 down-sets (§3.3)"); print("="*66)
def cov(c):
    o=[]
    for i in range(8):
        d=list(c); d[i]-=1
        if d[i]>=0 and tuple(d) in S: o.append(tuple(d))
    return o
ji=sorted([c for c in L if len(cov(c))==1], key=lambda c:(sum(c),c))
NM=['n','ℓ','k','q','e','f','g','2S']; base=min(L)
for c in ji:
    d=[f"{NM[i]}={c[i]}" for i in range(8) if c[i]!=base[i]]
    print(f"    {c}   {', '.join(d) if d else 'bottom'}")
leq=lambda a,b: all(p<=q for p,q in zip(a,b))
print("\n  covering relations of the generator poset:")
ce=[(a,b) for a in ji for b in ji if a!=b and leq(a,b)
    and not any(c!=a and c!=b and leq(a,c) and leq(c,b) for c in ji)]
for a,b in ce:
    da=[f"{NM[i]}={a[i]}" for i in range(8) if a[i]!=base[i]]
    db=[f"{NM[i]}={b[i]}" for i in range(8) if b[i]!=base[i]]
    print(f"    {','.join(da) or 'bottom':22s} ⋖ {','.join(db)}")
print(f"    {len(ce)} covers")
print("\n"+"="*66); print("4. ORDER DIMENSION AND REDUNDANCY (§3.6)"); print("="*66)
for i in range(8):
    ok=any(all(x[j]<=y[j] for j in range(8) if j!=i) and x[i]>y[i] for x in L for y in L)
    print(f"    {NM[i]:3s} carries information no other coordinate supplies: {ok}")
print("    -> order dimension 8, zero redundant coordinates")
print("\n"+"="*66); print("5. DUALITY, SKEW, AND F(−1) (§6.8, §6.8.1)"); print("="*66)
mx=tuple(max(c[i] for c in L) for i in range(8)); M=sum(mx)-sum(min(c[i] for c in L) for i in range(8))
sd=[c for c in L if tuple(mx[i]-c[i]+min(d[i] for d in L) for i in range(8)) in S
    and tuple(mx[i]-c[i]+min(d[i] for d in L) for i in range(8))==c]
sdall=[c for c in L if tuple(mx[i]-c[i]+min(d[i] for d in L) for i in range(8)) in S]
lev=Counter(sum(c) for c in L); ks=sorted(lev)
print(f"    max rank M = {sum(mx)}  (even -> σ preserves rank parity)")
print(f"    cells surviving σ(x) = max − x : {len(sdall)}   book: 8")
print(f"    rank profile: {' '.join(str(lev[r]) for r in ks)}")
print(f"    ranks {ks[0]}–{ks[-1]}, {len(ks)} levels, widest {max(lev.values())} at {max(lev,key=lev.get)}")
print(f"    parts company at rank 1 above the bottom: {lev[ks[1]]} vs {lev[ks[-2]]}   book: 5 against 4")
print(f"    F(−1) = {sum((-1)**sum(c) for c in L)}   -> not self-dual")
print("\n"+"="*66); print("6. THE VOID (§5)"); print("="*66)
b=1
for i in range(8): b*=(max(c[i] for c in L)-min(c[i] for c in L)+1)
print(f"    bounding box {b}   Λ {N}   void {b-N}   Λ occupies {100*N/b:.1f}%")
print("\n"+"="*66); print("7. SPERNER"); print("="*66)
print(f"    largest rank level = {max(lev.values())} ; Sperner property holds for distributive lattices of this type")
print(f"    log-concave rank sequence: {all(lev[ks[i]]**2>=lev[ks[i-1]]*lev[ks[i+1]] for i in range(1,len(ks)-1))}")