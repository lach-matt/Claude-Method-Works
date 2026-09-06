from collections import defaultdict
import sys
NM,EM,LM,KM,FM=3,3,1,3,1
NAME=['n','l','k','q','e','f','g','2S',"2S'",'v','2Jc','K','2J']
phi={1:3,2:4,3:5}

def build(stage):
    out=[]
    for n in range(1,NM+1):
     for l in range(0,min(LM,n-1)+1):
      for k in range(1,min(KM,2*(2*l+1))+1):
       for q in range(0,k+1):
        for s in range(0,k+1):
         for e in range(1,EM+1):
          for f in range(0,min(FM,e-1)+1):
           for g in range(0,min(q,2*(2*f+1))+1):
            base=(n,l,k,q,e,f,g,s)
            if stage==8: out.append(base); continue
            for sp in range(0,g+1):
             if stage=="9p" and sp>2*f+1: continue
             c9=base+(sp,)
             if stage in (9,"9p"): out.append(c9); continue
             for v in range(sp,g+1):
              c10=c9+(v,)
              if stage==10: out.append(c10); continue
              for jc in range(0,phi[k]+1):
               c11=c10+(jc,)
               if stage==11: out.append(c11); continue
               for K in range(0,jc+2*FM+1):
                c12=c11+(K,)
                if stage==12: out.append(c12); continue
                for J in range(max(0,K-1),K+2):
                 out.append(c12+(J,))
    return out

EDGES={  # (child, parent) in the §7.1 form x_child ≤ φ(x_parent)
 8 :[(1,0),(2,1),(3,2),(7,2),(5,4),(6,5),(6,3)],
 9 :[(1,0),(2,1),(3,2),(7,2),(5,4),(6,5),(6,3),(8,6)],
"9p":[(1,0),(2,1),(3,2),(7,2),(5,4),(6,5),(6,3),(8,6),(8,5)],
 10:[(1,0),(2,1),(3,2),(7,2),(5,4),(6,5),(6,3),(9,6),(8,9)],
 11:[(1,0),(2,1),(3,2),(7,2),(5,4),(6,5),(6,3),(9,6),(8,9),(10,2)],
 12:[(1,0),(2,1),(3,2),(7,2),(5,4),(6,5),(6,3),(9,6),(8,9),(10,2),(11,10)],
 13:[(1,0),(2,1),(3,2),(7,2),(5,4),(6,5),(6,3),(9,6),(8,9),(10,2),(11,10),(12,11)],
}

def analyse(stage):
    X=build(stage); d=len(X[0]); E=EDGES[stage]
    par=defaultdict(list)
    for c,p in E: par[c].append(p)
    two=[c for c in par if len(par[c])>1]
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
    fails=[]
    for cut in range(d):
        cs=comps(cut)
        if len(cs)!=2: continue
        A,B=cs
        vs=sorted({x[cut] for x in X})
        a=[len({tuple(x[i] for i in A) for x in X if x[cut]==v}) for v in vs]
        b=[len({tuple(x[i] for i in B) for x in X if x[cut]==v}) for v in vs]
        down=lambda z: all(z[i]>=z[i+1] for i in range(len(z)-1))
        up  =lambda z: all(z[i]<=z[i+1] for i in range(len(z)-1))
        opp=(down(a) and up(b)) or (up(a) and down(b))
        if not opp: fails.append(NAME[cut])
    lab={8:"Λ₈",9:"Λ₉","9p":"Λ₉′",10:"Λ₁₀",11:"Λ₁₁",12:"Λ₁₂",13:"Λ₁₃"}[stage]
    print(f"{lab:>4} |X|={len(X):>7,}  two-parent coordinates: {[NAME[c] for c in two] or '—':<18} "
          f"opposition fails at: {fails or '—'}   match: {sorted(fails)==sorted(NAME[c] for c in two)}")
    sys.stdout.flush()

for s in [8,9,"9p",10,11,12,13]: analyse(s)