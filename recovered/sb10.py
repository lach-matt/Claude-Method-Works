import numpy as np, eldata as ed
from collections import Counter
from itertools import combinations

L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
occ=set(ed.E[z] for z in ed.E)
cols=[(n,l) for n in range(1,8) for l in range(0,min(n,5))]
cap={c:2*(2*c[1]+1) for c in cols}

print("="*74); print("P.  SPERNER PROPERTY — is the largest antichain the largest rank?"); print("="*74)
rk=Counter(sum(c) for c in L)
maxrank=max(rk.values())
print(f"  largest rank level: {maxrank} cells")
# max antichain via Dilworth/Mirsky bound: for a product of chains, Sperner property holds
# (product of chains is a normalised matching / LYM poset -> Sperner)
print("  Λ is a subposet of a product of 3 chains.")
print("  Products of chains are Peck posets (rank-symmetric, unimodal, strongly Sperner).")
print("  But Λ is NOT rank-symmetric (shown earlier), so Λ is not Peck.")
print("  → Sperner property must be checked, not inherited. Testing:")
# greedy check: is there an antichain bigger than maxrank?
def leq(a,b): return all(x<=y for x,y in zip(a,b))
# max antichain = max independent set in comparability graph = via Dilworth = min chain cover
# use Mirsky: min antichain cover = longest chain. For max antichain use bipartite matching (Dilworth)
import networkx as nx
G=nx.DiGraph()
for a in L:
    for b in L:
        if a!=b and leq(a,b): G.add_edge(('L',a),('R',b))
B=nx.Graph()
B.add_nodes_from([('L',a) for a in L], bipartite=0)
B.add_nodes_from([('R',a) for a in L], bipartite=1)
B.add_edges_from(G.edges())
m=nx.bipartite.maximum_matching(B, top_nodes=[('L',a) for a in L])
size=len([1 for k in m if k[0]=='L'])
maxanti=len(L)-size
print(f"  maximum antichain size (Dilworth): {maxanti}")
print(f"  largest rank level:                {maxrank}")
print(f"  Sperner property holds: {maxanti==maxrank}")