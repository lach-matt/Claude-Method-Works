from itertools import product
CONS=[("l<=n-1",1,0),("k<=4l+2",2,1),("q<=k",3,2),("2S<=k",7,2),
      ("f<=e-1",5,4),("g<=4f+2",6,5),("g<=q",6,3)]
UB=[lambda x:x[0]-1,lambda x:4*x[1]+2,lambda x:x[2],lambda x:x[2],
    lambda x:x[4]-1,lambda x:4*x[5]+2,lambda x:x[3]]
sat=lambda x: all(x[v]<=UB[i](x) for i,(nm,v,p) in enumerate(CONS))
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
BOX=[z for z in product(*AX)]; LAM={z for z in BOX if sat(z)}; d=8
def C(S):
    Ls=sorted(S);A=[sorted({x[i] for x in Ls}) for i in range(d)];ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
y=(1,0,1,0,1,0,0,2)
print("="*82)
print("  THE CLAIM: A COMPLETE INDEX ADMITS NO LIE")
print("="*82)
print("""
  The forgery of the last message worked for ONE reason: the constraint
  '2S <= k' was NOT CONTENT. It was INFERRED from the cells. So new cells
  produced a new inference, and the index revised itself.

  **A complete index contains its own constraints as content.** Test what
  changes.
""")
print("="*82)
print("  CASE 1 — CONSTRAINTS INFERRED  (the index as built)")
print("="*82)
C1=C(LAM|{y})
print("\n     add y : closure = %d, fixed point %s"%(len(C1),C(C1)==C1))
print("     lie detected : %s"%("no" if C(C1)==C1 else "yes"))
print("     the index revised its own rule and defended the result")
print("="*82)
print("  CASE 2 — CONSTRAINTS AS CONTENT  (a complete index)")
print("="*82)
print("""
  Index the constraints themselves. A rule cell is
     (bounded, parent, slope, intercept)
  and the rule set is closed under the same order.
""")
RULES={(1,0,1,-1),(2,1,4,2),(3,2,1,0),(7,2,1,0),(5,4,1,-1),(6,5,4,2),(6,3,1,0)}
NAME={0:'n',1:'l',2:'k',3:'q',4:'e',5:'f',6:'g',7:'2S'}
print("     rule cells:")
for b,p,a,c in sorted(RULES):
    print("        %-4s <= %d*%-4s %+d"%(NAME[b],a,NAME[p],c))
def check(cell,rules):
    return [(b,p,a,c) for (b,p,a,c) in rules if cell[b] > a*cell[p]+c]
print("\n     check y against the STATED rules:")
bad=check(y,RULES)
for b,p,a,c in bad:
    print("        VIOLATES  %s <= %d*%s %+d   (%s=%d, bound=%d)"
          %(NAME[b],a,NAME[p],c,NAME[b],y[b],a*y[p]+c))
print("\n     **lie detected : %s**"%("yes" if bad else "no"))
print("="*82)
print("  AND THE FORGER'S ONLY REMAINING MOVE")
print("="*82)
print("""
  To pass CASE 2 the forger must also alter a RULE cell -- change
  (2S, k, 1, 0) into (2S, k, 1, 1). But the rule set is itself an index,
  and the same test applies to it.
""")
R2=(RULES-{(7,2,1,0)})|{(7,2,1,1)}
print("     forged rule set: 2S <= k+1")
print("     cells now admitted that were not: %d"%
      len([z for z in BOX if all(z[b]<=a*z[p]+c for b,p,a,c in R2)
           and not all(z[b]<=a*z[p]+c for b,p,a,c in RULES)]))
print("""
  **AND THAT IS WHERE IT STOPS BEING INTERNAL.** The forged rule is
  self-consistent too. The regress ends only at a rule that is checked
  against something outside every index -- a measured level.

  **SO THE CLAIM IS RIGHT WITH ONE QUALIFICATION:**

     a COMPLETE index -- one whose constraints are content rather than
     inference -- catches every lie about its CELLS, because a lying cell
     contradicts stated content instead of teaching new content.

     it does NOT catch a lie about its RULES, and no index can, because
     checking a rule requires a rule.

  **P19 IS THEREFORE NOT A LUXURY.** Q(X) = 0 means every question about
  the contents has an answer IN the contents -- including 'what bounds
  2S?'. An index that cannot answer that from its own content will answer
  it from whatever cells it is handed, and will believe the answer.
""")
print("="*82)
print("  WHICH IS WHY THE BOOK'S OWN INDEX MATTERS")
print("="*82)
print("""
  Appendix B indexes the PRINCIPLES. Appendix D indexes the PROTOCOLS.
  Section 19.8 indexes the PROCESS. Each is a rule set made into content,
  and each closes with E = 0.

  **That is the same move, three times, and its purpose is exactly this:
  to move rules out of inference and into content, where a lie about them
  becomes a contradiction rather than a lesson.**

  The regress is real and it does not end inside. It ends at Chapter 15's
  1,442 measured levels -- the only content in the book that no index
  supplied.
""")