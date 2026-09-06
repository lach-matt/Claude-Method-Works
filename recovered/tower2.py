import json
L8 = [tuple(c) for c in json.load(open("L8.json"))]
phi = {1:3, 2:4, 3:5}

L9  = [c+(s2p,) for c in L8 for s2p in range(0, c[6]+1)]                      # 2S' <= g
# v: 2S' <= v <= g, parity — two candidate parities
L10a = [c+(v,) for c in L9 for v in range(c[8], c[6]+1) if (v-c[6])%2==0]     # v ≡ g
L10b = [c+(v,) for c in L9 for v in range(c[8], c[6]+1) if (v-c[8])%2==0]     # v ≡ 2S'
print("Λ9 =", len(L9), "| Λ10 (v≡g) =", len(L10a), "| Λ10 (v≡2S') =", len(L10b))
L10 = L10a if len(L10a)==2535 else L10b
L11 = [c+(jc,) for c in L10 for jc in range(0, phi[c[2]]+1)]                  # 2Jc <= phî(k)
L12 = [c+(K,)  for c in L11 for K  in range(0, c[10]+2+1)]                    # 2K <= 2Jc + 2f_max
L12law = sum(c[10]+2*c[5]+1 for c in L11)                                     # variant: cell's own f
L13 = [c+(J,)  for c in L12 for J  in range(max(0,c[11]-1), c[11]+2)]         # |2J-2K| <= 1
print("Λ11 =", len(L11), "| Λ12 =", len(L12), "(law-variant would give %d)" % L12law, "| Λ13 =", len(L13))
json.dump({str(d): [list(c) for c in L] for d,L in [(9,L9),(10,L10),(11,L11),(12,L12)]}, open("tower.json","w"))
json.dump([list(c) for c in L13], open("L13.json","w"))