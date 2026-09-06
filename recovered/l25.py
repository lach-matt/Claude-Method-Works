import collections,time
from tower2mod import L8,L9,L10
t0=time.time()
A=L9(); print('L9',len(A))
# source (n,l,k,2S) = idx 0,1,2,7 ; target (e,f,g,2S') = idx 4,5,6,8
src=collections.defaultdict(list); 
for c in A: src[(c[0],c[1],c[2],c[7])].append(c)
legal=sum(1 for c in A if (c[4],c[5],c[6],c[8]) in src)   # target appears as some source
print('targets that are legal sources (appear as a source of some cell):',legal)
# legal by form: e in 1..3, f<=e-1, g<=4f+2, 2S'<=g  vs source forms n,l<=n-1,k<=4l+2 (k>=1!), 2S<=k
form=sum(1 for c in A if 1<=c[4]<=3 and c[5]<=c[4]-1 and c[6]<=4*c[5]+2 and c[8]<=c[6])
print('targets satisfying the source constraint forms:',form,'; targets with g=0:',sum(1 for c in A if c[6]==0))
pairs=0; nxt={}
for a in A:
    bs=src.get((a[4],a[5],a[6],a[8]),[]); nxt[a]=bs; pairs+=len(bs)
print('composable pairs',pairs)
# closure: composite runs a.src -> b.tgt with q=min(q_a,q_b); is it a cell of L9?
S=set(A); fail=0
for a in A:
    for b in nxt[a]:
        c=(a[0],a[1],a[2],min(a[3],b[3]),b[4],b[5],b[6],a[7],b[8])
        if c not in S: fail+=1
print('closure failures',fail)
# associativity over triples a->b->c : (c∘b)∘a vs c∘(b∘a)
trip=0; afail=0
for a in A:
    for b in nxt[a]:
        for c in nxt[b]:
            trip+=1
            ba=(a[0],a[1],a[2],min(a[3],b[3]),b[4],b[5],b[6],a[7],b[8])
            cb=(b[0],b[1],b[2],min(b[3],c[3]),c[4],c[5],c[6],b[7],c[8])
            x=(ba[0],ba[1],ba[2],min(ba[3],c[3]),c[4],c[5],c[6],ba[7],c[8])
            y=(a[0],a[1],a[2],min(a[3],cb[3]),cb[4],cb[5],cb[6],a[7],cb[8])
            if x!=y: afail+=1
print('composable triples',trip,'assoc failures',afail)
# cells of L9 with a successor / predecessor
has_next=sum(1 for a in A if nxt[a]); print('L9 cells with a composable successor',has_next,'of',len(A),'; g=0 cells',sum(1 for c in A if c[6]==0))
# L10: composability by target (e,f,g,2S') matching a source (n,l,k,2S) ignoring v
B=L10(); srcB=set((c[0],c[1],c[2],c[7]) for c in B)
hn=[c for c in B if (c[4],c[5],c[6],c[8]) in srcB]
print('L10',len(B),'cells with composable successor',len(hn),'non-composable',len(B)-len(hn),'g=0 cells',sum(1 for c in B if c[6]==0),
      'non-composable == g=0 set:', set(B)-set(hn)==set(c for c in B if c[6]==0))
print('time',round(time.time()-t0))