import json
L8 = [tuple(c) for c in json.load(open("L8.json"))]
phi = {1:3, 2:4, 3:5}
L9  = [c+(s2p,) for c in L8 for s2p in range(0, c[6]+1)]
L10 = [c+(v,) for c in L9 for v in range(c[8], c[6]+1)]        # 2S' <= v <= g, no parity
L11 = [c+(jc,) for c in L10 for jc in range(0, phi[c[2]]+1)]
L12 = [c+(K,)  for c in L11 for K  in range(0, c[10]+2+1)]
L12law = sum(c[10]+2*c[5]+1 for c in L11)
L13 = [c+(J,)  for c in L12 for J  in range(max(0,c[11]-1), c[11]+2)]
print("Λ10 =", len(L10), "| Λ11 =", len(L11), "| Λ12 =", len(L12),
      "(law-variant %d)" % L12law, "| Λ13 =", len(L13))
n2K0 = sum(1 for c in L12 if c[11]==0)
print("cells with 2K=0 in Λ12 =", n2K0, "(consistency: Λ13 = 3·Λ12 −", n2K0, "=", 3*len(L12)-n2K0, ")")
if len(L10)==2535:
    json.dump({str(d): [list(c) for c in L] for d,L in [(9,L9),(10,L10),(11,L11),(12,L12),(13,L13)]},
              open("tower.json","w"))
    print("tower banked to tower.json")
