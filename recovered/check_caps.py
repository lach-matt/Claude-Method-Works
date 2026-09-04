from itertools import product
# coordinates (n, l, k, q, e, f, g, 2S); caps of §7.4 = (n,e,l,k,f)=(3,3,1,3,1)
# box = product of (cap+1) over the 5 capped coords? Handoff: box 6,912; void 5,936; |L8|=976
# box 6912 = |bounding product|. Let's reconstruct the box from the loop bounds.
import lam8
L8 = lam8.L8()
assert len(L8)==976, len(L8)
# ranges actually taken by each coordinate
cols=list(zip(*L8))
names=['n','l','k','q','e','f','g','2S']
for nm,col in zip(names,cols):
    print(nm, "min",min(col),"max",max(col))
# box: full cartesian product of each coord's [min..max] inclusive
box=1
for col in cols:
    box*= (max(col)-min(col)+1)
print("box (min..max product):", box)
print("void = box - |L8|:", box-976)