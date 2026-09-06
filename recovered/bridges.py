from itertools import combinations
exec(open('/home/claude/entry_test.py').read().split('boxes =')[0])
NAME=['n','l','k','q','e','f','g','2S']
Aside=[0,1,2,7]; Bside=[4,5,6]

def stats(X):
    S=set(X)
    jf=mf=0
    for a,b in combinations(X,2):
        if tuple(map(max,a,b)) not in S: jf+=1
        if tuple(map(min,a,b)) not in S: mf+=1
    tot=0
    for q in range(0,4):
        A={(x[0],x[1],x[2],x[7]) for x in X if x[3]==q}
        B={(x[4],x[5],x[6])      for x in X if x[3]==q}
        tot+=len(A)*len(B)
    return jf,mf,tot-len(X)

jf,mf,dfct=stats(L8)
print(f"Lambda_8 as built (one bridge, q): cells {len(L8)}  join fail {jf}  meet fail {mf}  "
      f"factorisation defect {dfct}")
print(f"\nevery second A-B bridge, priced:")
print(f"{'bridge':>12} {'cells':>7} {'joinF':>7} {'meetF':>7} {'factor defect':>14}")
rows=[]
for i in Aside:
    for j in Bside:
        for lo,hi in ((j,i),(i,j)):        # x_lo <= x_hi
            Y=[x for x in L8 if x[lo]<=x[hi]]
            if len(Y)==len(L8) or len(Y)==0: continue   # trivial or empty
            jf,mf,d=stats(Y)
            rows.append((f"{NAME[lo]}<={NAME[hi]}",len(Y),jf,mf,d))
for r in sorted(rows,key=lambda r:-r[1]):
    print(f"{r[0]:>12} {r[1]:>7} {r[2]:>7} {r[3]:>7} {r[4]:>14}")

# is q the unique articulation point separating the two ends?
G={'n':['l'],'l':['n','k'],'k':['l','q','2S'],'q':['k','g'],'g':['q','f'],'f':['g','e'],'e':['f'],'2S':['k']}
def comps(rm):
    seen=set(); c=0
    for s in G:
        if s==rm or s in seen: continue
        c+=1; st=[s]
        while st:
            u=st.pop()
            if u in seen or u==rm: continue
            seen.add(u); st+=G[u]
    return c
print("\ncut vertices of the constraint graph, and what each separates:")
for v in G:
    n=comps(v)
    if n>1:
        seen=set(); parts=[]
        for s in G:
            if s==v or s in seen: continue
            st=[s]; p=[]
            while st:
                u=st.pop()
                if u in seen or u==v: continue
                seen.add(u); p.append(u); st+=G[u]
            parts.append(sorted(p))
        sep = any(set(p)=={'n','l','k','2S'} for p in parts)
        print(f"  remove {v:>2}: {n} components {parts}   separates the two ends: {sep}")