import collections,itertools
from rop import R
exec(open('tower-2.py').read().split("if __name__")[0]); cells=L8(); S=set(cells)
rank=collections.Counter(sum(c) for c in cells)
F=sum((-1)**sum(c) for c in cells); print('F(-1) =',F,'| rank polynomial degrees',min(rank),'..',max(rank))
top=tuple(max(c[i] for c in cells) for i in range(8)); print('top',top,'rank',sum(top))
surv=sorted(sum(c) for c in cells if tuple(t-x for t,x in zip(top,c)) in S); print('survivors of x->top-x:',len(surv),surv)
alph=[sorted(set(c[i] for c in cells)) for i in range(8)]; print('Σ(|A_i|-1) =',sum(len(a)-1 for a in alph))
# spin-sum localisation: k=2 cells' contribution
print('F(-1) by k:',{k:sum((-1)**sum(c) for c in cells if c[2]==k) for k in (1,2,3)})
# amplification over all 5,936 insertions
box=list(itertools.product(*alph)); out=[b for b in box if b not in S]
A=[len(R(cells+[y]))-976-1 for y in out]; A.sort()
print('amplification over all',len(out),'insertions: min',A[0],'median',A[len(A)//2],'max',A[-1])