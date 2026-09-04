# K-S χ=±6 slice (Candelas-de la Ossa-He-Szendroi, Triadophilia 2008):
# Hodge pairs (h, h+3) and (h+3, h) for 13 <= h <= 128, EXCLUDING h = 102,103,115,117,119..126.
excl = {102,103,115,117} | set(range(119,127))  # 119,120,121,122,123,124,125,126
hs = [h for h in range(13,129) if h not in excl]
X = set()
for h in hs:
    X.add((h, h+3))   # (h11, h21)
    X.add((h+3, h))
print("slice |X| =", len(X), "(book says 208)")

def closure(X):
    S=set(X); changed=True
    while changed:
        changed=False; new=set()
        L=list(S)
        for a in L:
            for b in L:
                jn=(max(a[0],b[0]),max(a[1],b[1])); mt=(min(a[0],b[0]),min(a[1],b[1]))
                if jn not in S: new.add(jn)
                if mt not in S: new.add(mt)
        if new: S|=new; changed=True
    return S

R = closure(X)
E = len(R)-len(X)
added = R - X
print("|R(X)| =", len(R), "  E = |R|-|X| =", E, "(book says 540)")
# distinct chi values on the added cells: chi = 2(h11 - h21)
chis = sorted({2*(a-b) for (a,b) in added})
print("distinct χ on added cells:", chis, "(book says 5: only 0, ±2, ±4)")
diag0 = [(a,b) for (a,b) in added if a==b]
print("on diagonal χ=0:", len(diag0), "from", (min(diag0) if diag0 else None), "to", (max(diag0) if diag0 else None), "(book says 112, (13,13)..(131,131))")
sums = [a+b for (a,b) in added]
print("h11+h21 range on added:", min(sums), "to", max(sums), "(book says 26 to 262)")