import sys; sys.path.insert(0,"/tmp")
import l2
cells={(f,s,mv) for _,f,s,mv,_ in l2.LAD}
axes=[len(l2.FAMILY),len(l2.SEAT),len(l2.MOVES)]
E,p=l2.minE(cells,axes)
cs={tuple(p[i].index(x[i]) for i in range(3)) for x in cells}
extra=l2.opR(cs,3)-cs
inv=[{p[i].index(v):v for v in range(axes[i])} for i in range(3)]
print(f"min E = {E}. the cells R admits and the index does not hold:\n")
for x in sorted(extra):
    f,s,mv=[inv[i][x[i]] for i in range(3)]
    print(f"   ({l2.FAMILY[f]}, {l2.SEAT[s]}, {l2.MOVES[mv]})")