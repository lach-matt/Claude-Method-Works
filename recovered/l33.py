import collections, statistics
from tower2mod import L8
L=L8(); S=set(L)
A=set((c[0],c[1],c[2],c[7]) for c in L); Q=set(c[3] for c in L); B=set((c[4],c[5],c[6]) for c in L)
print('|A|,|Q|,|B| =',len(A),len(Q),len(B),'product',len(A)*len(Q)*len(B),'defect',len(A)*len(Q)*len(B)-len(L))
# two-sided cuts: tree edges n-l, l-k, k-q, q-g, g-f, f-e, k-2S. Removing vertex c splits into components.
E={(0,1),(1,2),(2,3),(3,6),(6,5),(5,4),(2,7)}
def comps(rm):
    adj=collections.defaultdict(set)
    for a,b in E:
        if rm not in (a,b): adj[a].add(b); adj[b].add(a)
    seen=set(); out=[]
    for v in range(8):
        if v==rm or v in seen: continue
        st=[v]; comp=set()
        while st:
            u=st.pop()
            if u in seen: continue
            seen.add(u); comp.add(u); st+=list(adj[u])
        out.append(sorted(comp))
    return out
names='n l k q e f g 2S'.split()
for rm in range(8):
    cs=comps(rm)
    if len(cs)==2:
        # conditioned factorisation defect
        tot=0
        for val in set(c[rm] for c in L):
            sub=[c for c in L if c[rm]==val]
            p=[set(tuple(c[i] for i in comp) for c in sub) for comp in cs]
            tot+=len(p[0])*len(p[1])
        print(f'cut at {names[rm]}: two components {cs}, conditioned product {tot}, defect {tot-len(L)}')
    else: print(f'cut at {names[rm]}: {len(cs)} components (not two-sided)')
# Markov table
pp=collections.defaultdict(set)
for c in L: pp[((c[0],c[1],c[2],c[7]),c[3])].add((c[4],c[5],c[6]))
fut=[len(v) for v in pp.values()]
print('(past,present) pairs',len(pp),'futures per pair min/median/max',min(fut),statistics.median(fut),max(fut),'any pair determining one future:',min(fut)==1)
byq=collections.defaultdict(lambda:(set(),[]))
for (a,q),F in pp.items(): byq[q][0].add(a); byq[q][1].append(frozenset(F))
prev=None
for q in sorted(byq):
    pasts,Fs=byq[q]; one=len(set(Fs))==1; F=Fs[0]
    print(f' present {q}: pasts {len(pasts)}, one future set: {one}, size {len(F)}, nests previous: {prev is None or prev<=F}, interval-saturated: {len(F)==len(set((e,f,g) for e in range(1,4) for f in range(0,2) for g in range(0,4) if (min(F)<=(e,f,g)<=max(F)) and f<=e-1 and g<=min(4*f+2,3)))}')
    prev=F
# tick decomposition over composable cells (g>=1)
C=[c for c in L if c[6]>=1]; print('composable cells',len(C))
print(' k-g:',collections.Counter(c[2]-c[6] for c in C))
tab=collections.Counter((c[2]-c[3],c[3]-c[6]) for c in C); print(' (k-q,q-g):',dict(tab))
print(' pure k-q>0:',sum(v for (a,b),v in tab.items() if a>0 and b==0),'pure q-g>0:',sum(v for (a,b),v in tab.items() if b>0 and a==0),'both:',sum(v for (a,b),v in tab.items() if a>0 and b>0))
cnt=collections.Counter('counting' if c[3]<4*c[5]+2 else ('tied' if c[3]==4*c[5]+2 else 'shell') for c in C)
print(' g ceiling:',{k:f'{100*v/len(C):.1f}%' for k,v in cnt.items()})