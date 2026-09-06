from collections import defaultdict
import sys
exec(open('/home/claude/pauli.py').read().split('def analyse')[0])

def analyse(stage):
    X=build(stage); d=len(X[0]); E=EDGES[stage]
    par=defaultdict(list); chi=defaultdict(list)
    for c,p in E: par[c].append(p); chi[p].append(c)
    adj=defaultdict(set)
    for c,p in E: adj[c].add(p); adj[p].add(c)
    def comps(cut):
        seen={cut}; out=[]
        for s in range(d):
            if s in seen: continue
            st=[s]; c=[]
            while st:
                u=st.pop()
                if u in seen: continue
                seen.add(u); c.append(u); st+=list(adj[u])
            out.append(sorted(c))
        return out
    lab={8:"Λ₈",9:"Λ₉","9p":"Λ₉′",10:"Λ₁₀",11:"Λ₁₁",12:"Λ₁₂",13:"Λ₁₃"}[stage]
    viol=0; tested=0; mixed=[]; allshrink=[]
    for cut in range(d):
        cs=comps(cut)
        if len(cs)<2: continue
        vs=sorted({x[cut] for x in X})
        if len(vs)<2: continue
        dirs=[]
        for C in cs:
            sz=[len({tuple(x[i] for i in C) for x in X if x[cut]==v}) for v in vs]
            down=all(sz[i]>=sz[i+1] for i in range(len(sz)-1))
            up=all(sz[i]<=sz[i+1] for i in range(len(sz)-1))
            holds_parent=any(p in C for p in par[cut])
            holds_child =any(c in C for c in chi[cut])
            tested+=1
            pred = "shrink" if holds_parent else ("grow" if holds_child else "flat")
            got  = "shrink" if (down and not up) else ("grow" if (up and not down) else "flat")
            if pred!=got: viol+=1
            dirs.append(got)
        if "shrink" in dirs and "grow" in dirs: mixed.append(NAME[cut])
        elif set(dirs)=={"shrink"}: allshrink.append(NAME[cut])
    two=[NAME[c] for c in par if len(par[c])>1]
    print(f"{lab:>4} |X|={len(X):>7,}  two-parent: {str(two):<14} "
          f"components tested {tested:>2}  law violations {viol}  "
          f"opposed cuts {mixed}  all-shrink cuts {allshrink or '—'}")
    sys.stdout.flush()
    return viol

tot=sum(analyse(s) for s in [8,9,"9p",10,11,12,13])
print(f"\nlaw: a component shrinks iff it holds a parent of the cut, grows iff it holds a child.")
print(f"total violations across all stages and all cuts: {tot}")