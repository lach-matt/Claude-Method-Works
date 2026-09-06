import itertools,collections
exec(open('tower-2.py').read().split("if __name__")[0]); cells=L8(); S=set(cells)
alph=[sorted(set(c[i] for c in cells)) for i in range(8)]
box=list(itertools.product(*alph))
CONS={'l<=n-1':lambda c:c[1]<=c[0]-1,'k<=4l+2':lambda c:c[2]<=4*c[1]+2,'q<=k':lambda c:c[3]<=c[2],'f<=e-1':lambda c:c[5]<=c[4]-1,
      'g<=4f+2':lambda c:c[6]<=4*c[5]+2,'g<=q':lambda c:c[6]<=c[3],'2S<=k':lambda c:c[7]<=c[2]}
# constraints 11-18: each of the seven, marginal exclusion (fails only this one), and k>=1 floor built in
marg={}
for nm,f in CONS.items():
    marg[nm]=sum(1 for b in box if not f(b) and all(g(b) for n2,g in CONS.items() if n2!=nm))
print('marginal exclusion:',sorted(marg.items(),key=lambda x:-x[1]))
print('box',len(box),'cells satisfying all seven',sum(1 for b in box if all(f(b) for f in CONS.values())))
# two-body separation: A=(n,l,k,2S) side, B=(e,f,g) side, coupled through q
A=collections.Counter(); Bc=collections.Counter()
for q in alph[3]:
    A[q]=len(set((c[0],c[1],c[2],c[7]) for c in cells if c[3]==q)); Bc[q]=len(set((c[4],c[5],c[6]) for c in cells if c[3]==q))
print('|A_q|',[A[q] for q in alph[3]],'|B_q|',[Bc[q] for q in alph[3]],'products',[A[q]*Bc[q] for q in alph[3]],'sum',sum(A[q]*Bc[q] for q in alph[3]))
print('bare product |A|x|B|x|q| =',len(set((c[0],c[1],c[2],c[7]) for c in cells)),'x',len(set((c[4],c[5],c[6]) for c in cells)),'x',len(alph[3]),'=',len(set((c[0],c[1],c[2],c[7]) for c in cells))*len(set((c[4],c[5],c[6]) for c in cells))*len(alph[3]))
# four numbers: <q>=1428/976, rank sequence unimodal/log-concave, 345 = 35.3%
print('sum q =',sum(c[3] for c in cells),'<q> =',round(sum(c[3] for c in cells)/976,4),'| 345/976 =',round(345/976*100,1),'%')
rk=collections.Counter(sum(c) for c in cells); seq=[rk[r] for r in sorted(rk)]
lc=all(seq[i]**2>=seq[i-1]*seq[i+1] for i in range(1,len(seq)-1)); print('rank sequence',seq,'log-concave',lc)
# bipartite sign: cells split by rank parity
print('even/odd rank cells',sum(1 for c in cells if sum(c)%2==0),sum(1 for c in cells if sum(c)%2))