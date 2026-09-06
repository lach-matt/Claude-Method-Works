from itertools import product, combinations
print("="*90)
print("  SIGGERS 2016 — WHAT THE READING GIVES")
print("="*90)
print("""
  **Rival (1974):** every sublattice L of a finite distributive lattice P is
  P minus a CLOSED family I_L of irreducible intervals.

  For P = ∏ chains the irreducible intervals are [α^(i), β^(j)], and
  **Lemma 3.5(ii): [α^(i),β^(j)] ⊆ ∪I  ⟺  for all x ∈ L, x_i ≥ α ⇒ x_j > β.**

  > **That is exactly the recovered bound φ_ij of Chapter 10.** The book's
  > operator 𝓡 recovers Rival's closed family of irreducible intervals.

  **Corollary 4.2:** L ↦ D_P(L) is a ONE-TO-ONE correspondence between the
  sublattices of P and the spanned PREORDER extensions of C^∞.

  **Lemma 5.1:**  L subdirect ⟺ D has no down-edges
                  L tight     ⟺ D is a POSET (acyclic)

  > **Subdirect is exactly the book's 'uses every value on every axis' — the
  > recovered-alphabet condition that broke three of my constructions.**
""")
print("="*90)
print("  VERIFY: SUBLATTICES = PREORDER EXTENSIONS OF C^∞")
print("="*90)
def count_sublattices(r,c):
    cells=list(product(range(r),range(c)))
    n=len(cells); S=set(cells); out=0
    for m in range(1,1<<n):
        T={cells[i] for i in range(n) if m>>i & 1}
        ok=True
        for x,y in combinations(sorted(T),2):
            if (max(x[0],y[0]),max(x[1],y[1])) not in T: ok=False; break
            if (min(x[0],y[0]),min(x[1],y[1])) not in T: ok=False; break
        if ok: out+=1
    return out
def count_preorders(r,c):
    """C^infty for Z_r x Z_c : vertices = {1..r-1}^(1) ∪ {1..c-1}^(2) ∪ {0,∞}
       spanned preorder extensions = transitive reflexive digraphs containing C^inf"""
    V=[('a',i) for i in range(1,r)]+[('b',j) for j in range(1,c)]+[('0',),('I',)]
    idx={v:i for i,v in enumerate(V)}; n=len(V)
    base=[[False]*n for _ in range(n)]
    for i in range(n): base[i][i]=True
    for i in range(1,r):
        for j in range(i+1,r): base[idx[('a',i)]][idx[('a',j)]]=True
    for i in range(1,c):
        for j in range(i+1,c): base[idx[('b',i)]][idx[('b',j)]]=True
    for v in V:
        if v!=('0',): base[idx[('0',)]][idx[v]]=True
        if v!=('I',): base[idx[v]][idx[('I',)]]=True
    free=[(i,j) for i in range(n) for j in range(n) if i!=j and not base[i][j]]
    cnt=0
    for mask in range(1<<len(free)):
        M=[row[:] for row in base]
        for k,(i,j) in enumerate(free):
            if mask>>k & 1: M[i][j]=True
        ok=True
        for i in range(n):
            for j in range(n):
                if not M[i][j]: continue
                for k in range(n):
                    if M[j][k] and not M[i][k]: ok=False; break
                if not ok: break
            if not ok: break
        if ok: cnt+=1
    return cnt
print("\n  %8s%16s%20s%12s"%("box","sublattices","preorder extensions","match"))
print("  "+"-"*58)
for r,c in [(2,2),(2,3),(3,3),(2,4)]:
    a=count_sublattices(r,c)
    b=count_preorders(r,c) if (r-1)+(c-1)+2<=7 else None
    print("  %8s%16d%20s%12s"%("%dx%d"%(r,c),a,(str(b) if b is not None else "too large"),
          ("YES" if b==a else "no") if b is not None else "—"))
print("="*90)
print("  AND WHAT IT SAYS ABOUT THE DECISION PROBLEM")
print("="*90)
print("""
  **Corollary 6.6:** a one-to-one correspondence between EMBEDDINGS of L into
  products of chains and surjective homomorphisms of disjoint unions of chains
  to J(L). **Subdirect embeddings ↔ homomorphisms injective on each chain.
  Tight embeddings ↔ chain decompositions of J(L).**

  > **So reorderability into d axes is a CHAIN-COVERING question on J(X)** —
  > and by Dilworth the minimum number of chains covering a poset is its
  > WIDTH, computable by bipartite matching in polynomial time.

  **That is the matching problem §23.4 identified hours ago and could not
  place.** It is Dilworth's theorem, reached through Larson and Siggers.
""")