import json, sys
tag=sys.argv[1]
P=json.load(open(f"prep_{tag}.json"))
els=[frozenset(e) for e in P["elements"]]
sigs=[frozenset(map(int,k.split(","))) for k in P["sig_classes"]]  # element-ids per class
NE=len(els)
found=[None]
def bb(chosen_sigs, covered, k):
    if found[0] is not None: return
    if len(covered)==NE: found[0]=chosen_sigs; return
    if len(chosen_sigs)==k: return
    unc=[ei for ei in range(NE) if ei not in covered]
    ei=min(unc,key=lambda e:sum(1 for s in sigs if e in s))
    for si,s in sorted(enumerate(sigs),key=lambda t:-len(t[1])):
        if ei in s and si not in chosen_sigs:
            bb(chosen_sigs|{si}, covered|s, k)
for k in range(1,16):
    found[0]=None
    bb(frozenset(),frozenset(),k)
    if found[0] is not None:
        print(f"SEED = {k}")
        json.dump({"seed":k},open(f"seed_{tag}.json","w"))
        break