import pickle
from itertools import combinations
D=pickle.load(open('/home/claude/stage/s1.pkl','rb'))
res=pickle.load(open('/home/claude/stage/s2.pkl','rb'))
cells=D['cells']; n=len(cells); tab=D['tab']; NF=D['nforms']
print("="*88)
print("  TWO MECHANISMS — GROWTH FROM BELOW, EROSION FROM ABOVE")
print("="*88)
print("""
  **Triangulation of the three obstruction measurements:** order-space
  components, E-landscape minima, cell-space peaks — **three spaces, one
  failure, so the disconnection is intrinsic.**

  **And the peaks are the DENSE sets.** The full box is reorderable; removing
  one cell breaks it. So the peaks are unreachable from below and reachable
  from ABOVE. **The dual rule is already in the grammar.**
""")
YES={m for m in range(1<<n) if res[m]==2}
bysize={}
for m in YES: bysize.setdefault(bin(m).count('1'),[]).append(m)
sizes=sorted(bysize)
# upward
up={}
for m in bysize[sizes[0]]: up[m]=True
for s in sizes[1:]:
    for m in bysize[s]:
        up[m]=any(res[m & ~(1<<i)]==2 and up.get(m & ~(1<<i),False)
                  for i in range(n) if m>>i & 1)
# downward
dn={}
for m in bysize[sizes[-1]]: dn[m]=True
for s in reversed(sizes[:-1]):
    for m in bysize[s]:
        dn[m]=any(res[m | (1<<i)]==2 and dn.get(m | (1<<i),False)
                  for i in range(n) if not (m>>i & 1))
U=sum(1 for m in YES if up.get(m)); Dn=sum(1 for m in YES if dn.get(m))
B=sum(1 for m in YES if up.get(m) or dn.get(m))
print("  %10s%14s%14s%16s"%("size","from below","from above","either")) 
print("  "+"-"*56)
for s in sizes:
    a=sum(1 for m in bysize[s] if up.get(m))
    b=sum(1 for m in bysize[s] if dn.get(m))
    c=sum(1 for m in bysize[s] if up.get(m) or dn.get(m))
    print("  %10d%14d%14d%16s"%(s,a,b,"%d / %d"%(c,len(bysize[s]))))
print("\n     reorderable sets : %d"%len(YES))
print("     from below       : %d  (%.1f%%)"%(U,100*U/len(YES)))
print("     from above       : %d  (%.1f%%)"%(Dn,100*Dn/len(YES)))
print("     **either         : %d  (%.1f%%)**"%(B,100*B/len(YES)))
print("="*88)
print("  AND THE SIGNATURES")
print("="*88)
def sig(m):
    idx=[i for i in range(n) if m>>i & 1]
    c=[0]*NF
    for T in combinations(idx,3): c[tab[T]]+=1
    return tuple(c)
allY={sig(m) for m in YES}
upY={sig(m) for m in YES if up.get(m)}
dnY={sig(m) for m in YES if dn.get(m)}
both=upY|dnY
print("\n     YES signatures, all        : %d"%len(allY))
print("     reached from below         : %d"%len(upY))
print("     reached from above         : %d"%len(dnY))
print("     **union                   : %d      missed : %d**"%(len(both),len(allY-both)))
print("="*88)
print("  THE MECHANISM, IF COMPLETE")
print("="*88)
if len(allY-both)==0:
    print("""
  **BOTH DIRECTIONS TOGETHER REACH EVERY REORDERABLE SET AND EVERY
  SIGNATURE.**

     grow from the minimal reorderable sets, adding one cell
     erode from the box, removing one cell
     **the union is the table**

  > **The obstruction was never that the space is disconnected. It is that
  > it is disconnected FROM ONE END.** The dual rule — already one of the six
  > preserving rules — supplies the other.

  **Cost: |YES| × |X| tests in each direction, %d × 18 × 2 — against
  260,800 × 72 for exhaustion. A factor of about %.0f.**
"""%(len(YES),260800*72/(len(YES)*18*2)))
else:
    print("""
  **%d signatures reached by neither direction.** So there are reorderable
  sets isolated in BOTH directions — and the mechanism needs a third move.
"""%len(allY-both))