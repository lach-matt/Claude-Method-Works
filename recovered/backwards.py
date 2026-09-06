exec(open('/tmp/pq6.py').read().split('print("="*88)')[0])
import numpy as np, random
from itertools import product, permutations
random.seed(293)
print("="*88)
print("  P3 — BACKWARDS FROM THE OUTPUT")
print("="*88)
print("""
  **OUTPUT.** A boolean at the root: some arrangement has no strict nesting.

  **BACK 1.** The root needs, from each child, the rows that reach that
  child's ends. So each node must RETURN that.

  **BACK 2.** Rows touching one end are pairwise nested — a CHAIN — so the
  return value is a chain, representable by its deepest element.

  **BACK 3.** The set of achievable (deepest-left, deepest-right) pairs is
  therefore O(r²) per node. **The state is polynomial.**

  **BACK 4.** To compute it, each node must know WHICH ROWS live at it.
  **That is the input I do not have.** My code anchors a row only when its
  column set equals a node's leaf set — but on a correct tree a row can
  also be a CONSECUTIVE RUN of a Q-node's children.

  > **The missing established input is a map: row -> (node, child-range).**
""")
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S): return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
def anchor_map(S):
    """for each row, the node and the range of its children whose union is the row"""
    A=alpha(S); sup=sup_of(S); ROWS=set(sup.values())
    root=build(set(A[1]),list(sup.values()))
    if root is None: return None,None
    nodes=[]
    def walk(v):
        nodes.append(v)
        for k in v.kids: walk(k)
    walk(root)
    amap={}
    for r in ROWS:
        found=None
        for v in nodes:
            if v.leaves==r: found=(v,0,len(v.kids)-1 if v.kids else 0,'exact'); break
        if found is None:
            for v in nodes:
                if not v.kids or not (r<v.leaves): continue
                ks=v.kids
                for i in range(len(ks)):
                    acc=frozenset()
                    for j in range(i,len(ks)):
                        acc|=ks[j].leaves
                        if acc==r: found=(v,i,j,'run'); break
                        if not (acc<r) and acc!=r: break
                    if found: break
                if found: break
        amap[r]=found
    return amap,root
print("="*88)
print("  DOES EVERY ROW ANCHOR?")
print("="*88)
n=0; allok=0; kinds={'exact':0,'run':0,'NONE':0}
bad=[]
for _ in range(1500):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,5)))]
    cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
    Aa=alpha(S)
    if len(Aa[0])<2 or len(Aa[1])<2: continue
    am,root=anchor_map(S)
    if am is None: continue
    n+=1
    ok=True
    for r,v in am.items():
        if v is None: kinds['NONE']+=1; ok=False
        else: kinds[v[3]]+=1
    allok+=ok
    if not ok and len(bad)<3: bad.append(sorted(S))
print("\n     instances                : %d"%n)
print("     every row anchored       : %d  (%.1f%%)"%(allok,100*allok/max(n,1)))
print("     anchors that are EXACT   : %d"%kinds['exact'])
print("     anchors that are a RUN   : %d"%kinds['run'])
print("     **rows with NO anchor**  : %d"%kinds['NONE'])
if bad:
    print("\n     instances with an unanchored row:")
    for s in bad: print("       ",str(s)[:64])
print("""
{0}
  WHAT THIS SAYS
{0}
""".format("="*88))
if kinds['NONE']==0:
    print("""  **Every row anchors — %d exactly at a node, %d as a run of children.**
  The map exists and is computable in one pass.

  **That is the established input the traversal was missing.** My seven
  attempts used only the 'exact' case, which is %.0f%% of anchors; the
  remaining %.0f%% were silently skipped, and the skipped constraints are
  the false positives."""%(kinds['exact'],kinds['run'],
      100*kinds['exact']/(kinds['exact']+kinds['run']),
      100*kinds['run']/(kinds['exact']+kinds['run'])))
else:
    print("""  **%d rows fail to anchor.** So the tree does not represent every row as
  a node or a consecutive run, and the traversal cannot be built on it as
  specified. **That is a defect in the tree, not in the traversal.**"""%kinds['NONE'])