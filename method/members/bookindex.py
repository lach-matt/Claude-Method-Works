# §32.1.1 recomputed: cells (location, support) at chapter and part resolution from every paragraph
# outside the Register that cites a section or chapter.
import re,itertools,collections
L=open('The_Method_1_6-2.md',encoding='utf-8').read().splitlines()
start=[i for i,l in enumerate(L) if l.startswith('# PART 0')][-1]
APP='ABCDEF'
def code(ch): return ch if isinstance(ch,int) else 100+APP.index(ch)   # appendices order after chapters
loc=0; part=0; cells=set(); claims=0; partcells=set(); chpart={0:0}
for i,l in enumerate(L):
    if i<start:
        if re.match(r'^# PART',l): pass
        continue
    m=re.match(r'^# PART ([0IV]+)',l)
    if m: part={'0':0,'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7}[m.group(1)]; continue
    m=re.match(r'^## (\d+)\. ',l)
    if m: loc=int(m.group(1)); chpart[loc]=part; continue
    m=re.match(r'^## Appendix ([A-F])',l)
    if m: loc=m.group(1); chpart[loc]=part; continue
    if l.startswith('#') or not l.strip(): continue
    refs=set(int(x) for x in re.findall(r'§\s?(\d+)\.',l))|set(int(x) for x in re.findall(r'Chapter (\d+)',l))|set(re.findall(r'§\s?([A-F])\.',l))|set(re.findall(r'Appendix ([A-F])',l))
    refs={r for r in refs if (isinstance(r,str) or 1<=r<=35)}
    if refs: claims+=1
    for r in refs:
        cells.add((code(loc),code(r))); partcells.add((chpart[loc],chpart.get(r,part)))
n=41  # 35 chapters + 6 appendices
def R2(X):
    A=[sorted({x[i] for x in X}) for i in range(2)]
    P={}
    for (a,b) in X:
        P[(0,b)]=max(P.get((0,b),-1),a); P[(1,a)]=max(P.get((1,a),-1),b)
    def phi(i,j,v):   # max x_i over cells with x_j<=v
        return max([x[i] for x in X if x[j]<=v] or [-1])
    return {x for x in itertools.product(*A) if x[0]<=phi(0,1,x[1]) and x[1]<=phi(1,0,x[0])}
back=sum(1 for a,b in cells if b<=a); fwd=len(cells)-back
E=len(R2(cells))-len(cells); Ep=len(R2(partcells))-len(partcells)
print(f'claims {claims}  cells {len(cells)}  box {n*n}  density {100*len(cells)/(n*n):.1f}%  E {E}')
print(f'support<=location {back} of {len(cells)}  half-box {n*(n+1)//2}  density {100*back/(n*(n+1)//2):.1f}%  E {len(R2({c for c in cells if c[1]<=c[0]}))-back}')
print(f'forward {fwd} = {100*fwd/len(cells):.0f}%')
print(f'parts: cells {len(partcells)}  box {8*8}  density {100*len(partcells)/64:.1f}%  E {Ep}')
print('part cells',sorted(partcells)); print('closure adds',sorted(R2(partcells)-partcells))
print({k:v for k,v in chpart.items()})
print('V/VI -> IV chapter cells:',sorted((a,b) for a,b in cells if chpart.get(a) in (5,6) and chpart.get(b)==4))
print('cites of ch 20-22 from anywhere in V:',[(a,b) for a,b in cells if chpart.get(a)==5 and b in (19,20,21,22)])
g={0:0,1:0,2:1,3:1,4:2,5:2,6:2,7:2}
tri={(g[a],g[b]) for a,b in partcells}; print('three-group cells',sorted(tri),'E',len(R2(tri))-len(tri))
