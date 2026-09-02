# l-ch1.py — Phase R2 chapter-1 instrument (chat 69). Measures on the rebuilt Λ₈ (tower-2.py, unchanged) every
import math, itertools, collections
# tower-measurable figure printed in main Chapter 1: |Λ|, box/void, rank statistics (rank = Σxᵢ, Ch. 9 L1947),
# F(-1), rank-generating-function peak, C(976,2), the P22 fabricated-cell experiment (2S-rule relaxations), E_bits.
import importlib.util, sys
spec=importlib.util.spec_from_file_location('tower','tower-2.py'); tw=importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
L=tw.L8(); S=set(L); print('|Λ8|',len(L))
box=3*2*3*4*3*2*4*4; print('box',box,'void',box-len(L))
ranks=[sum(c) for c in L]; cnt=collections.Counter(ranks)
print('rank min/max',min(ranks),max(ranks),'mean %.4f'%(sum(ranks)/len(ranks)),'cells of rank 13:',cnt[13])
print('F(-1)=',sum((-1)**r for r in ranks),' rank distribution',sorted(cnt.items()))
print('C(976,2)=',976*975//2,' C(8,2)=',math.comb(8,2))
# P22: box generator with a 2S rule parameter
def cells(rule):
    out=[]
    for n in range(1,4):
      for l in range(0,min(1,n-1)+1):
        for k in range(1,min(3,4*l+2)+1):
          for q in range(0,k+1):
            for e in range(1,4):
              for f in range(0,min(1,e-1)+1):
                for g in range(0,min(4*f+2,q)+1):
                  for S2 in range(0,rule(k)+1):
                    out.append((n,l,k,q,e,f,g,S2))
    return out
base=cells(lambda k:k); assert len(base)==976
after=cells(lambda k:{1:2,2:2,3:3}[k]); forged=cells(lambda k:k+1)
y=(1,0,1,0,1,0,0,2); print('y in Λ8:',y in S,' y in after:',y in set(after))
print('rule 2S≤2 at k=1: |after|=',len(after),' new cells=',len(after)-976,' (Ch.1 prints 74 further + y = 75)')
print('rule 2S≤k+1: |forged|=',len(forged),' new cells=',len(forged)-976,' (Ch.1 prints 225)')
# E_bits = log2 C(|R|,E) for E=36: which |R| gives 105.1?
for n in (118,126,140,154): print(' log2 C(%d,36) = %.1f'%(n,math.log2(math.comb(n,36))))
print('105.1/1.168 =',round(105.1/1.168,1),' 47.4/0.130 =',round(47.4/0.130,1))
print('0.010/0.00018 =',round(0.010/0.00018,1))
