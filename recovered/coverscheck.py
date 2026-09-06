import json,collections
exec(open('tower-2.py').read().split("if __name__")[0])
cells=L8(); S=set(cells)
C=json.load(open('census.json')); slots=[tuple(x) for x in C['slots']]; steps=[tuple(x) for x in C['steps']]
def wit(c):
    out=set()
    for (j,v) in slots:
        if c[j]==v: out.add(('A',j,v))
    for (i,j,t,phi) in steps:
        if c[j]<=t and c[i]==phi: out.add(('S',i,j,t))
    return out
W={c:wit(c) for c in cells}; U=set().union(*W.values()); assert len(U)==102
d=json.load(open('covers8.json'))
covs=[tuple(sorted(tuple(x) for x in cv)) for cv in d['covers']]
print('n_covers field',d['n_covers'],'covers listed',len(covs),'distinct',len(set(covs)))
print('sizes',collections.Counter(len(c) for c in covs))
print('all cells in Λ8:',all(x in S for cv in covs for x in cv))
full=sum(1 for cv in covs if set().union(*(W[x] for x in cv))==U)
print('covers that cover all 102 elements:',full,'of',len(covs))
# minimality: any cover with a removable cell?
red=sum(1 for cv in covs if any(set().union(*(W[y] for y in cv if y!=x))==U for x in cv))
print('covers with a redundant cell:',red)
common=set.intersection(*(set(cv) for cv in covs)); print('cells common to all covers:',common)
freq=collections.Counter(x for cv in covs for x in cv)
corner4=(3,0,1,1,3,0,1,1)  # placeholder overwritten below
def pct(pred,label):
    n=sum(1 for cv in covs if pred(cv)); print(f'{label}: {n} = {100*n/len(covs):.1f}%')
unit=[x for x in S if x[0]==3 and x[1]==0 and x[2]==1 and x[3]==1 and x[5]==0 and x[6]==1 and x[7]==1]
print('unit template cells (3,0,1,1,*,0,1,1):',unit)
pct(lambda cv: any(x in unit for x in cv),'unit template (any e) in cover')
# s->s : ℓ=0 to f=0 channel; recorded "s→s NOT a step, holds in 71%": cover contains a cell with l=0 and f=0
pct(lambda cv: any(x[1]==0 and x[5]==0 for x in cv),'s→s (l=0,f=0) cell present')
pct(lambda cv: any(x[1]==0 and x[5]==1 for x in cv),'s→p (l=0,f=1) present')
pct(lambda cv: any(x[1]==1 and x[5]==0 for x in cv),'p→s (l=1,f=0) present')
pct(lambda cv: any(x[1]==1 and x[5]==1 for x in cv),'p→p (l=1,f=1) present')
pct(lambda cv: any(x[3]==0 for x in cv),'null q=0 present'); pct(lambda cv: any(x[3]==x[2] and x[2]==3 for x in cv),'full q=k=3 present')
print('most frequent cells:'); 
for x,n in freq.most_common(8): print(' ',x,n,f'{100*n/len(covs):.1f}%')
print('the four §14.5.10 core cells:')
for x in [(1,0,2,2,3,1,2,2),(2,1,3,3,1,0,0,3),(2,1,3,3,2,1,3,0),(3,1,1,0,3,1,0,0)]: print(' ',x,freq[x],f'{100*freq[x]/len(covs):.1f}%')