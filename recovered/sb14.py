import numpy as np, eldata as ed
from collections import Counter
from itertools import combinations

cols=[(n,l) for n in range(1,8) for l in range(0,min(n,5))]
def cleq(a,b): return a[0]<=b[0] and a[1]<=b[1]

print("="*72); print("AF.  IS THE COLUMN POSET A YOUNG DIAGRAM SHAPE?"); print("="*72)
shape=[sum(1 for (n,l) in cols if n==nn) for nn in range(1,8)]
print(f"  row lengths by n: {shape}")
print(f"  partition form: {sorted(shape,reverse=True)}")
print("  This is the staircase 1,2,3,4,5,5,5 truncated at l<=4.")
print("  Down-sets of a Young-diagram-shaped poset are counted by the")
print("  hook-length / determinant formula for plane partitions of that shape.")
# verify 120 via lattice-path / determinant
from math import comb
# number of down-sets of a staircase poset = number of order ideals
# check against direct enumeration
ds=[]; order=sorted(cols)
def enum(i,ch):
    if i==len(order): ds.append(frozenset(ch)); return
    c=order[i]; enum(i+1,ch)
    if all(d in ch for d in cols if cleq(d,c) and d!=c): enum(i+1,ch|{c})
enum(0,frozenset())
print(f"  direct enumeration: {len(ds)} down-sets")
print(f"  is 120 = C(10,3)? {comb(10,3)}   = 8!/(3!*...)? ")
print(f"  120 = 5! = {np.math.factorial(5) if hasattr(np,'math') else 120}")
print("  Note: 120 = 5! and also C(10,3). Both are coincidences unless")
print("  a bijection is exhibited; none is claimed here.")

print()
print("="*72); print("AG.  CHAIN LENGTH / DIMENSION OF THE POSET"); print("="*72)
L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
def leq(a,b): return all(x<=y for x,y in zip(a,b))
# order dimension: minimum number of linear extensions whose intersection is the order
# Lambda embeds in N^3, so dim <= 3. Is it exactly 3?
# dim >= 3 iff there is a 3-dimensional "standard example" or the poset is not 2-dimensional
# 2-dimensional iff the incomparability graph is a permutation graph
import networkx as nx
G=nx.Graph()
G.add_nodes_from(L)
for a,b in combinations(L,2):
    if not leq(a,b) and not leq(b,a): G.add_edge(a,b)
print(f"  incomparability graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
# a permutation graph is a comparability graph AND its complement is too
# test: is G a comparability graph? (transitive orientation exists)
# quick necessary condition: permutation graphs are perfect & contain no C5
c5=False
for cyc in nx.simple_cycles(G, length_bound=5):
    if len(cyc)==5:
        sub=G.subgraph(cyc)
        if sub.number_of_edges()==5: c5=True; break
print(f"  contains induced C5 (rules out permutation graph): {c5}")
print(f"  -> order dimension is {'3 (not 2-dimensional)' if c5 else 'possibly 2, needs full test'}")
print("  Lambda sits in N^3 so dim <= 3; if not 2-dimensional then dim = 3 exactly,")
print("  meaning three coordinates are NECESSARY, not merely convenient.")