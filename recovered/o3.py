from collections import defaultdict
def build(NM,EM,LM,KM,FM,tight,upto):
    phi={k:min(2*k+1,5) for k in range(1,KM+1)}
    for k in (1,2,3): phi[k]={1:3,2:4,3:5}.get(k,phi.get(k,2*k+1))
    out=[]
    for n in range(1,NM+1):
     for l in range(0,min(LM,n-1)+1):
      for k in range(1,min(KM,2*(2*l+1))+1):
       for q in range(0,k+1):
        for s in range(0,k+1):
         for e in range(1,EM+1):
          for f in range(0,min(FM,e-1)+1):
           for g in range(0,min(q,2*(2*f+1))+1):
            for sp in range(0,g+1):
             for v in range(sp,g+1):
              for jc in range(0,phi.get(k,2*k+1)+1):
               if upto==11: out.append((n,l,k,q,e,f,g,s,sp,v,jc)); continue
               cap=jc+2*f if tight else jc+2*FM
               for K in range(0,cap+1):
                if upto==12: out.append((n,l,k,q,e,f,g,s,sp,v,jc,K)); continue
                for J in range(max(0,K-1),K+2):
                 out.append((n,l,k,q,e,f,g,s,sp,v,jc,K,J))
    return out
def sect(Y,A,B):
    tot=0; per=[]
    for q in range(0,4):
        a={tuple(y[i] for i in A) for y in Y if y[3]==q}
        b={tuple(y[i] for i in B) for y in Y if y[3]==q}
        n=sum(1 for y in Y if y[3]==q); per.append(len(a)*len(b)-n); tot+=len(a)*len(b)
    return tot-len(Y), per

cands={}
caps=[(3,3,1,3,1),(3,3,1,3,2),(4,4,1,3,1),(3,3,2,3,1)]
for cp in caps:
    for upto,A,B in ((12,[0,1,2,7,10,11],[4,5,6,8,9]),(13,[0,1,2,7,10,11,12],[4,5,6,8,9])):
        try:
            X=build(*cp,False,upto); T=build(*cp,True,upto)
        except Exception: continue
        cut=len(X)-len(T)
        d,per=sect(T,A,B)
        cands[f"cells cut Λ{upto} caps{cp}"]=cut
        cands[f"defect Λ{upto} caps{cp}"]=d
        for i,p in enumerate(per): cands[f"section q={i} defect Λ{upto} caps{cp}"]=p
        # projections of the cut
        cutset=set(X)-set(T)
        cands[f"distinct (Jc,K) cut Λ{upto} caps{cp}"]=len({(c[10],c[11]) for c in cutset})
        cands[f"distinct (f,Jc,K) cut Λ{upto} caps{cp}"]=len({(c[5],c[10],c[11]) for c in cutset})
        cands[f"distinct A-side cut Λ{upto} caps{cp}"]=len({tuple(c[i] for i in A) for c in cutset})
        cands[f"cells with f<fmax Λ{upto} caps{cp}"]=sum(1 for c in X if c[5]<cp[4])
hits=[(k,v) for k,v in cands.items() if v==2475]
print(f"candidate quantities computed: {len(cands)}")
print(f"exact hits on 2,475: {hits if hits else 'none'}")
near=sorted(((abs(v-2475),k,v) for k,v in cands.items()))[:8]
print("\nnearest values:")
for d,k,v in near: print(f"  {v:>9,}  (off by {d:>7,})  {k}")
print("\n2,475 = 3² × 5² × 11.  3.5% of 70,905 = 2,481.7")