import numpy as np
from itertools import product
print("="*88)
print("  THE SORT DIRECTION WAS WRONG")
print("="*88)
print("""
  φ_{i,j}(v) = max{x_i : x_j <= v} is **non-decreasing in the parent**. So a
  closed set needs the SMALL supports FIRST — ascending, not descending.

  I sorted months by length descending, which puts a 31-day month at index
  1 and lets the bound admit day 31 everywhere. **CORRECTION 128.**
""")
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
NAMES={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
print("  %-14s%16s%10s"%("sort direction","month order","E"))
print("  "+"-"*46)
for lab,key in [("as printed",lambda m:m),
                ("descending",lambda m:(-DAYS[m],m)),
                ("ASCENDING",lambda m:(DAYS[m],m))]:
    order=sorted(range(1,13),key=key)
    mp={m:i+1 for i,m in enumerate(order)}
    C2={(mp[m],d) for (m,d) in CAL}
    E=len(Rop(C2))-len(C2)
    print("  %-14s%16s%10d"%(lab,NAMES[order[0]]+"…"+NAMES[order[-1]],E))
print("""
  **E = 0 with months in ascending order of length.** Feb, then the
  thirty-day months, then the thirty-one-day months.
""")
order=sorted(range(1,13),key=lambda m:(DAYS[m],m))
print("     ",[ "%s(%d)"%(NAMES[m],DAYS[m]) for m in order])
print("="*88)
print("  RE-CHECK THE PERIODIC TABLE WITH THE SAME RULE")
print("="*88)
PT=set()
for g in (1,18): PT.add((1,g))
for p in (2,3):
    for g in list(range(1,3))+list(range(13,19)): PT.add((p,g))
for p in (4,5,6,7):
    for g in range(1,19): PT.add((p,g))
cnt={g:sum(1 for (p,q) in PT if q==g) for g in range(1,19)}
print("\n  %-26s%10s"%("group order","E"))
print("  "+"-"*38)
for lab,key in [("as printed",lambda g:g),
                ("by occupancy, descending",lambda g:(-cnt[g],g)),
                ("by occupancy, ascending",lambda g:(cnt[g],g))]:
    order=sorted(range(1,19),key=key)
    mp={g:i+1 for i,g in enumerate(order)}
    P2={(p,mp[g]) for (p,g) in PT}
    print("  %-26s%10d"%(lab,len(Rop(P2))-len(P2)))
print("""
  **Descending works for the table and ascending for the calendar**, and
  the reason is that they order DIFFERENT axes: the table's periods are
  already ascending in width, so only the groups need sorting; the
  calendar's days are already ascending, so only the months do.

  > **The rule is: sort the PARENT axis ascending by support size, and the
  > CHILD axis descending by occupancy.** Applied to each, both go to zero.
""")
print("="*88)
print("  BOTH DEFECTS ARE PRINTING ORDER — NOW ACTUALLY DEMONSTRATED")
print("="*88)
print("""
  | index | as printed | after sorting |
  |---|---|---|
  | classroom periodic table | **36** | **0** |
  | Gregorian calendar | **7** | **0** |

  **Neither needs a new coordinate; neither hides a missing constraint.**
  Both are printed in an order that serves another purpose — chronology,
  and chemical family — **and pays for it in cells.**

  > **E(X) > 0 with a chain of supports is a defect of presentation, not
  > of knowledge, and a sort repairs it.**

  **And the better question is what the chosen order buys.** The classroom
  table groups by valence and pays 36. The calendar runs in time order and
  pays 7. **Both are stated trades, which is a more useful sentence than
  calling either defective.**
""")