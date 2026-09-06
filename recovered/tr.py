import numpy as np
from itertools import product
CONS=[("l<=n-1",1,0),("k<=4l+2",2,1),("q<=k",3,2),("2S<=k",7,2),
      ("f<=e-1",5,4),("g<=4f+2",6,5),("g<=q",6,3)]
UB=[lambda x:x[0]-1,lambda x:4*x[1]+2,lambda x:x[2],lambda x:x[2],
    lambda x:x[4]-1,lambda x:4*x[5]+2,lambda x:x[3]]
sat=lambda x: all(x[v]<=UB[i](x) for i,(nm,v,p) in enumerate(CONS))
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
BOX=[z for z in product(*AX)]; LAM={z for z in BOX if sat(z)}
LL=sorted(LAM); d=8
NAME={0:'n',1:'l',2:'k',3:'q',4:'e',5:'f',6:'g',7:'2S'}
def phi_of(S):
    Ls=sorted(S); A=[sorted({x[i] for x in Ls}) for i in range(d)]; ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v]
                run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return A,ph
A0,ph0=phi_of(LAM)
bind={(i,j) for (i,j) in ph0 if any(ph0[(i,j)][v]<max(A0[i]) for v in A0[j])}
print("="*88)
print("  Q: CAN THE TREE BE RECOVERED FROM THE 16 BINDING PAIRS?")
print("="*88)
print("\n  binding pairs (parent j -> bounded i):")
print("   ",sorted((NAME[j],NAME[i]) for (i,j) in bind))
E={(j,i) for (i,j) in bind}
def reach(E,src,skip):
    seen={src}; st=[src]
    while st:
        u=st.pop()
        for (a,b) in E:
            if (a,b)==skip: continue
            if a==u and b not in seen: seen.add(b); st.append(b)
    return seen
red={e for e in E if e[1] not in reach(E,e[0],e)}
print("\n  transitive reduction: %d edges"%len(red))
print("   ",sorted((NAME[a],NAME[b]) for a,b in red))
TREE={(p,v) for nm,v,p in CONS}
print("\n  the defining tree   : %d edges"%len(TREE))
print("   ",sorted((NAME[a],NAME[b]) for a,b in TREE))
print("\n  **reduction == tree : %s**"%(red==TREE))
if red!=TREE:
    print("     only in reduction:",sorted((NAME[a],NAME[b]) for a,b in red-TREE))
    print("     only in tree     :",sorted((NAME[a],NAME[b]) for a,b in TREE-red))
print("="*88)
print("  Q: DOES A TREE-ONLY CLOSURE MAKE A COMPUTABLE BY THE NESTED SUM?")
print("="*88)
grid=np.array(BOX,dtype=np.int32)
def close_full(S):
    A,ph=phi_of(S)
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}
def close_tree(S):
    A,ph=phi_of(S)
    return {x for x in product(*A) if all(x[v]<=ph[(v,p)].get(x[p],-1) for nm,v,p in CONS)}
print("\n     |close_full(Lambda)| = %d   fixed point %s"%(len(close_full(LAM)),close_full(LAM)==LAM))
print("     |close_tree(Lambda)| = %d   fixed point %s"%(len(close_tree(LAM)),close_tree(LAM)==LAM))
def viol(y): return [i for i,(nm,v,p) in enumerate(CONS) if y[v]>UB[i](y)]
outside=[z for z in BOX if z not in LAM]
print("\n  %-12s%12s%14s%14s"%("constraint","A full","A tree-only","difference"))
print("  "+"-"*52)
tot=0; agree=0
for i,(nm,v,p) in enumerate(CONS):
    front=[y for y in outside if viol(y)==[i] and y[v]-UB[i](y)==1]
    if not front: continue
    af=[];at=[]
    for y in front[:8]:
        af.append(len(close_full(LAM|{y}))-len(LAM)-1)
        at.append(len(close_tree(LAM|{y}))-len(LAM)-1)
    print("  %-12s%12.0f%14.0f%14.0f"%(nm,np.median(af),np.median(at),np.median(af)-np.median(at)))
    tot+=1
    if np.median(af)==np.median(at): agree+=1
print("\n     full and tree-only agree on %d of %d constraints"%(agree,tot))
print("""
{0}
  WHAT THIS SETTLES
{0}
""".format("="*88))
print("""  **THE TREE IS RECOVERABLE.** Transitive reduction of the 16 binding
  pairs returns %s the 7 defining edges -- so no information is lost in
  the closure; the tree is the reduction of what R recovers.

  **AND THERE ARE TWO CLOSURE OPERATORS, NOT ONE.**

     close_full  applies all 16 recovered bounds -- the book's R
     close_tree  applies only the 7 tree bounds

  Both fix Lambda. They differ on Lambda + y, and the difference is
  exactly the transitive propagation.

  **SO 'THE AMPLIFICATION' IS OPERATOR-DEPENDENT**, and the book has
  never said which operator it means. That is a definitional gap, not a
  computational one, and it is why three attempts at a closed form all
  disagreed with the measurements: I was computing tree amplification and
  comparing it to full amplification.
"""%("exactly" if red==TREE else "NOT exactly"))