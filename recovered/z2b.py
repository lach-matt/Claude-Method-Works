import json, sys
tag=sys.argv[1]
P=json.load(open(f"prep_{tag}.json"))
NE=len(P["elements"])
FULL=(1<<NE)-1
masks=[]
for k in P["sig_classes"]:
    m=0
    for ei in map(int,k.split(",")): m|=1<<ei
    masks.append(m)
elem_classes=[[i for i,m in enumerate(masks) if m>>e & 1] for e in range(NE)]
best=[None]
def bb(cov, depth, k, banned):
    if cov==FULL: best[0]=depth; return True
    if depth==k: return False
    # least-covered uncovered element
    e=min((x for x in range(NE) if not cov>>x&1), key=lambda x:len(elem_classes[x]))
    newban=set(banned)
    for ci in elem_classes[e]:
        if ci in banned: continue
        if bb(cov|masks[ci], depth+1, k, newban): return True
        newban.add(ci)
    return False
for k in range(1,16):
    if bb(0,0,k,set()):
        print(f"SEED = {k}")
        json.dump({"seed":k},open(f"seed_{tag}.json","w"))
        break