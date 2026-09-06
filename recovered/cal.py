import numpy as np
from itertools import product
print("="*88)
print("  THE SAME DIAGNOSIS ON E(calendar) = 7")
print("="*88)
DAYS={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
CAL={(m,d) for m in range(1,13) for d in range(1,DAYS[m]+1)}
def Rop(S,d=2):
    Ls=sorted(S);A=[sorted({x[i] for x in Ls}) for i in range(d)];ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
R=Rop(CAL); EX=R-CAL
print("\n     |CAL| = %d   |R(CAL)| = %d   **E = %d**"%(len(CAL),len(R),len(EX)))
print("     the excess cells :",sorted(EX))
print("""
  **The seven are 29, 30 and 31 February, 31 April, 31 June, 31 September,
  31 November** — the dates the rectangle admits and the year does not.
""")
print("  STEP 1 — is there a separating linear form in (month, day)?\n")
def find_form(S,ex,mx=40):
    for a in range(-mx,mx+1):
        for b in range(-mx,mx+1):
            if (a,b)==(0,0): continue
            vin=[a*x[0]+b*x[1] for x in S]; vout=[a*y[0]+b*y[1] for y in ex]
            if max(vin)<min(vout): return (a,b,max(vin))
    return None
f=find_form(CAL,EX)
print("     ",("%d·month + %d·day <= %d"%f) if f else "none — so not a missing constraint")
print("\n  STEP 2 — do the month supports form a chain?\n")
sup={m:frozenset(range(1,DAYS[m]+1)) for m in range(1,13)}
chain=all(a<=b or b<=a for a in sup.values() for b in sup.values())
print("     supports : %s"%sorted({len(s) for s in sup.values()}))
print("     chain under inclusion : **%s**"%chain)
print("""
  **Every month's day-set is an initial segment, so they nest by length.**
  The criterion says a valid ordering exists.
""")
print("  STEP 3 — sort months by length, descending\n")
order=sorted(range(1,13),key=lambda m:(-DAYS[m],m))
NAMES={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
print("     ",[ "%s(%d)"%(NAMES[m],DAYS[m]) for m in order])
mmap={m:i+1 for i,m in enumerate(order)}
CAL2={(mmap[m],d) for (m,d) in CAL}
R2=Rop(CAL2)
print("\n     after reordering months : |X| = %d   |R(X)| = %d   **E = %d**"%(len(CAL2),len(R2),len(R2)-len(CAL2)))
print("="*88)
print("  BOTH OF THE BOOK'S WORKED DEFECTS ARE PRINTING ORDER")
print("="*88)
print("""
  | index | E as printed | diagnosis | E after sorting |
  |---|---|---|---|
  | classroom periodic table | 36 | bad order | **0** |
  | Gregorian calendar | 7 | bad order | **0** |

  **Neither needs a new coordinate. Neither hides a missing constraint.
  Both are printed in an order that is meaningful for another purpose** —
  chronology for the calendar, chemical family for the table — **and that
  order is not the one that makes the index closed.**

  > **E(X) > 0 with a chain of supports is not a defect of knowledge. It
  > is a defect of presentation, and it is repaired by a sort.**
""")
print("="*88)
print("  WHICH MAKES CHAPTER 1's ARGUMENT BOTH WEAKER AND SHARPER")
print("="*88)
print("""
  **WEAKER:** the classroom table is not incoherent. It is closed under a
  permutation of its own group labels, and the permutation is computable in
  one pass. Chapter 1 presents the 36 as a structural failure; **they are a
  typographic one.**

  **SHARPER:** the interesting question is not 'does E = 0 exist?' but
  **'what does the chosen order buy that the closed order does not?'**

     the classroom order groups elements by valence behaviour
     the closed order groups them by how many periods contain them

  **The table is printed in the order that serves chemistry, and pays 36
  cells for it.** That is a stated trade, and it is a better sentence than
  calling the layout defective.
""")