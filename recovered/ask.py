from itertools import product
CONS=[("l<=n-1",1,0),("k<=4l+2",2,1),("q<=k",3,2),("2S<=k",7,2),
      ("f<=e-1",5,4),("g<=4f+2",6,5),("g<=q",6,3)]
UB=[lambda x:x[0]-1,lambda x:4*x[1]+2,lambda x:x[2],lambda x:x[2],
    lambda x:x[4]-1,lambda x:4*x[5]+2,lambda x:x[3]]
sat=lambda x: all(x[v]<=UB[i](x) for i,(nm,v,p) in enumerate(CONS))
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
BOX=[z for z in product(*AX)]; LAM={z for z in BOX if sat(z)}; d=8
def phi_of(S):
    Ls=sorted(S);A=[sorted({x[i] for x in Ls}) for i in range(d)];ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return A,ph
A0,ph0=phi_of(LAM)
def admits(ph,A,x):
    """does THIS index admit x? -- asked of the index, not of a successor"""
    if any(x[i] not in A[i] for i in range(d)): return False
    return all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)
y=(1,0,1,0,1,0,0,2)
print("="*82)
print("  THE INDEX WAS NEVER ASKED")
print("="*82)
print("""
  Two different operations were run together in the last two messages:

     ASK      : does Lambda admit y?          -- a question TO the index
     REPLACE  : recompute the index as C(Lambda + y)  -- a new index
""")
print("  ASK Lambda about y:")
print("     Lambda admits y : %s"%admits(ph0,A0,y))
print("     y satisfies the stated constraints : %s"%sat(y))
print("     **the complete index answered correctly, from its own content**")
print("\n  REPLACE Lambda by C(Lambda + y):")
A1,ph1=phi_of(LAM|{y})
S1={x for x in product(*A1) if admits(ph1,A1,x)}
print("     new index size  : %d"%len(S1))
print("     new index admits y : %s"%admits(ph1,A1,y))
print("     **a DIFFERENT index answered a different question**")
print("="*82)
print("  SO THE FAILURE WAS PROCEDURAL, NOT STRUCTURAL")
print("="*82)
print("""
  Lambda answers 'what bounds 2S given k = 1?' from its own content:
""")
print("     phi(2S | k) at k=1 : %d"%ph0[(7,2)][1])
print("     y asks for         : %d"%y[7])
print("     verdict            : REFUSED")
print("""
  **The index never believed the lie. It was never consulted.** The lie
  succeeded only against a procedure that DISCARDED the index and rebuilt
  it around the new cell.

  **A COMPLETE INDEX CAN ALWAYS ANSWER. IT CANNOT DEFEND ITSELF AGAINST
  BEING REPLACED**, because replacement is not a question -- it is an act
  performed on the index by whoever holds it.
""")
print("="*82)
print("  AND THE BOOK ALREADY HAS THE PROTOCOL FOR THIS")
print("="*82)
print("""
     D.2.13  COMMIT BEFORE YOU LOOK

  which says: fix the standard, then admit the data. That is exactly the
  distinction above. **Ask the index, then decide whether to extend it --
  never extend first and ask afterwards.**

  E1 in Chapter 10 says the same for cells, E2 for axes, E3 for
  constraints: **an extension must be checked AGAINST the index, not
  absorbed INTO it and re-derived.**
""")
print("  TEST — the correct procedure, on 200 fabrications:")
import random
random.seed(101)
outside=[z for z in BOX if z not in LAM]
caught=sum(1 for _ in range(200) if not admits(ph0,A0,random.choice(outside)))
print("     asked of Lambda   : %d of 200 refused"%caught)
rebuilt=0
for _ in range(200):
    yy=random.choice(outside)
    A2,ph2=phi_of(LAM|{yy})
    if admits(ph2,A2,yy): rebuilt+=1
print("     rebuilt around it : %d of 200 admitted"%rebuilt)
print("""
{0}
  THE STATEMENT
{0}

  **A complete index answers every question about its contents, always,
  because self-reference means the answers ARE the contents.**

     R(Lambda) = Lambda  is not a curiosity. It is the guarantee that the
     index's answers and its contents are the same object, so it can
     never be short of an answer and never give one that contradicts
     itself.

  **The only way to make it wrong is to stop asking it** -- to replace it
  with a successor built around the very cell it would have refused.

  **That is not a weakness of the index. It is a weakness of a procedure,
  and D.2.13 is the remedy the book already carries.**
""".format("="*82))