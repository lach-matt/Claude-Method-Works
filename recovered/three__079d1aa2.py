from collections import defaultdict
exec(open('/home/claude/entry_test.py').read().split('boxes =')[0])
X=L8; NAME=['n','l','k','q','e','f','g','2S']
# the constraint tree: n—l—k—q—g—f—e with 2S pendant at k
ADJ={0:[1],1:[0,2],2:[1,3,7],3:[2,6],6:[3,5],5:[6,4],4:[5],7:[2]}

def sides(cut):
    """split the tree at one node: the two components its removal leaves"""
    seen={cut}; comps=[]
    for s in ADJ:
        if s in seen: continue
        st=[s]; c=[]
        while st:
            u=st.pop()
            if u in seen: continue
            seen.add(u); c.append(u); st+=ADJ[u]
        comps.append(sorted(c))
    return comps

print("BALANCE  |Λ| = Σ_v |A(v)|·|B(v)|, tested at every cut of the constraint tree\n")
print(f"{'cut':>4} {'components':<34} {'Σ|A||B|':>9} {'|Λ|':>6} {'defect':>8}")
for c in range(8):
    comps=sides(c)
    if len(comps)!=2: 
        print(f"{NAME[c]:>4} {str([[NAME[i] for i in p] for p in comps]):<34} "
              f"{'—':>9} {len(X):>6}  {len(comps)} components, not a two-sided split")
        continue
    A,B=comps
    tot=0
    for v in sorted({x[c] for x in X}):
        a={tuple(x[i] for i in A) for x in X if x[c]==v}
        b={tuple(x[i] for i in B) for x in X if x[c]==v}
        tot+=len(a)*len(b)
    lab=str([[NAME[i] for i in A],[NAME[i] for i in B]])
    print(f"{NAME[c]:>4} {lab:<34} {tot:>9} {len(X):>6} {tot-len(X):>8}")

print("\nand the unconditioned product, for contrast:")
A={(x[0],x[1],x[2],x[7]) for x in X}; B={(x[4],x[5],x[6]) for x in X}
Q={x[3] for x in X}
print(f"  |past|·|present|·|future| = {len(A)}·{len(Q)}·{len(B)} = {len(A)*len(Q)*len(B)}"
      f"  against |Λ| = {len(X)}   defect {len(A)*len(Q)*len(B)-len(X)}")

# is the past–future graph a path or a triangle?
print("\nedges of the three-part graph, read off the constraint tree:")
past={0,1,2,7}; pres={3}; fut={4,5,6}
E=set()
for u in ADJ:
    for v in ADJ[u]:
        pu = 'past' if u in past else ('present' if u in pres else 'future')
        pv = 'past' if v in past else ('present' if v in pres else 'future')
        if pu!=pv: E.add(tuple(sorted((pu,pv))))
print(f"  {sorted(E)}")
print(f"  past–future edge present: {('future','past') in E or ('past','future') in E}")
print(f"  shape: {'triangle (treewidth 2)' if len(E)==3 else 'path (treewidth 1)'}")