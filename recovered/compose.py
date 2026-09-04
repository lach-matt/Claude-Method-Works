import json
T = json.load(open("tower.json"))
L9  = [tuple(c) for c in T["9"]]
L10 = [tuple(c) for c in T["10"]]
L11 = [tuple(c) for c in T["11"]]
L12 = [tuple(c) for c in T["12"]]
L13 = [tuple(c) for c in T["13"]]
# coord idx: 0 n,1 l,2 k,3 q,4 e,5 f,6 g,7 2S, 8 2S', 9 v, 10 2Jc, 11 2K, 12 2J

def comp(L, tgt_idx, src_idx):
    srcs = set(tuple(c[i] for i in src_idx) for c in L)
    n = sum(1 for c in L if tuple(c[i] for i in tgt_idx) in srcs)
    return n, len(L), n/len(L)

# four-tuple: target (e,f,g,2S') vs source (n,l,k,2S)
four_t, four_s = (4,5,6,8), (0,1,2,7)
for name, L in [("L9",L9),("L10",L10),("L11",L11),("L12",L12)]:
    n, tot, fr = comp(L, four_t, four_s)
    print(f"{name}: 4-tuple composable = {n} / {tot} = {fr:.4f}")
# five-tuple at L13: target (e,f,g,2S',2J) vs source (n,l,k,2S,2Jc)
n, tot, fr = comp(L13, (4,5,6,8,12), (0,1,2,7,10))
print(f"L13: 5-tuple composable = {n} / {tot} = {fr:.4f}")