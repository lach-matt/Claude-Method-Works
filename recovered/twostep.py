import pickle
from itertools import combinations
D=pickle.load(open('/home/claude/stage/s1.pkl','rb'))
res=pickle.load(open('/home/claude/stage/s2.pkl','rb'))
cells=D['cells']; n=len(cells); tab=D['tab']; NF=D['nforms']
YES={m for m in range(1<<n) if res[m]==2}
bysize={}
for m in YES: bysize.setdefault(bin(m).count('1'),[]).append(m)
sizes=sorted(bysize)
def sig(m):
    idx=[i for i in range(n) if m>>i & 1]
    c=[0]*NF
    for T in combinations(idx,3): c[tab[T]]+=1
    return tuple(c)
print("="*88)
print("  TEST A — DOES 2-CELL GROWTH REACH THE MISSED SIGNATURES?")
print("="*88)
r1={}
for m in bysize[sizes[0]]: r1[m]=True
for s in sizes[1:]:
    for m in bysize[s]:
        r1[m]=any(res[m & ~(1<<i)]==2 and r1.get(m & ~(1<<i),False) for i in range(n) if m>>i & 1)
r2=dict(r1)
for s in sizes:
    for m in bysize[s]:
        if r2.get(m): continue
        hit=False
        on=[i for i in range(n) if m>>i & 1]
        for a,b in combinations(on,2):
            p=m & ~(1<<a) & ~(1<<b)
            if res[p]==2 and r2.get(p,False): hit=True; break
        if hit: r2[m]=True
allY={sig(m) for m in YES}
s1={sig(m) for m in YES if r1.get(m)}
s2={sig(m) for m in YES if r2.get(m)}
print("\n     YES signatures                    : %d"%len(allY))
print("     reached by 1-cell growth          : %d      missed %d"%(len(s1),len(allY-s1)))
print("     **reached by 1- or 2-cell growth  : %d      missed %d**"%(len(s2),len(allY-s2)))
print("="*88)
print("  TEST B — AND THE SETS, NOT THE SIGNATURES")
print("="*88)
print("""
  **A different question.** Signatures can be covered while sets are not —
  several sets share a signature. Count the SETS.
""")
print("\n  %8s%10s%14s%14s"%("size","YES sets","1-cell","1- or 2-cell"))
print("  "+"-"*48)
for s in sizes:
    a=sum(1 for m in bysize[s] if r1.get(m)); b=sum(1 for m in bysize[s] if r2.get(m))
    print("  %8d%10d%14d%14d"%(s,len(bysize[s]),a,b))
A1=sum(1 for m in YES if r1.get(m)); A2=sum(1 for m in YES if r2.get(m))
print("\n     sets reached : 1-cell %d (%.1f%%)   1-or-2 %d (%.1f%%)"%(A1,100*A1/len(YES),A2,100*A2/len(YES)))
print("="*88)
print("  TEST C — THE STEP SIZE ACTUALLY NEEDED  (a structural measurement)")
print("="*88)
print("""
  **Not a coverage test.** For every reorderable set, measure the distance to
  its nearest SMALLER reorderable subset. **The maximum over all sets is the
  step size any growth mechanism must allow.**
""")
from collections import Counter
dist=Counter(); worst=[]
for s in sizes:
    for m in bysize[s]:
        on=[i for i in range(n) if m>>i & 1]
        found=None
        for k in (1,2,3,4):
            if k>len(on): break
            for T in combinations(on,k):
                p=m
                for i in T: p &= ~(1<<i)
                if res[p]==2: found=k; break
            if found: break
        if found is None: found=99
        dist[found]+=1
        if found>=3: worst.append((s,found))
print("\n  %14s%14s"%("step needed","sets"))
print("  "+"-"*30)
for k in sorted(dist): print("  %14s%14d"%(("%d"%k if k<99 else ">4"),dist[k]))
print("\n     **maximum step needed : %s**"%(max(k for k in dist if k<99) if any(k<99 for k in dist) else ">4"))
if worst:
    ws={}
    for s,k in worst: ws.setdefault(k,[]).append(s)
    for k in sorted(ws): print("     step %d needed by sets of size %s"%(k,sorted(set(ws[k]))))
print("="*88)
print("  THE COST BOUND")
print("="*88)
mx=max((k for k in dist if k<99),default=None)
print("""
     step size needed : %s
     branching per set: |X|^step = 18^%s
     **so a complete growth mechanism at this box costs %s tests per set**
"""%(mx,mx,"18^%d = %d"%(mx,18**mx) if mx else "unbounded"))