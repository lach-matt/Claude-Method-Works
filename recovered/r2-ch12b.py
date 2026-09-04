# r2-ch12b.py — Phase R2 instrument for main §12.6–12.7 (chat 71). Requires tower-2.py beside it.
import importlib.util, itertools, collections
spec=importlib.util.spec_from_file_location('tower','tower-2.py'); tw=importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
L8=tw.L8(); n,l,k,q,e,f,g,s=range(8)
A=lambda c:(c[n],c[l],c[k],c[s]); B=lambda c:(c[e],c[f],c[g])
print('|A| = %d parents, |B| = %d targets, |q| = %d: product %d against %d'%(len(set(map(A,L8))),len(set(map(B,L8))),len(set(c[q] for c in L8)),len(set(map(A,L8)))*len(set(map(B,L8)))*len(set(c[q] for c in L8)),len(L8)))
tot=0
for qq in range(4):
    C=[c for c in L8 if c[q]==qq]; Aq=set(map(A,C)); Bq=set(map(B,C)); exact=set(C)==set(a+(qq,)+b for a in Aq for b in Bq)
    # reassemble in coordinate order (n,l,k,q,e,f,g,2S)
    exact=set(C)=={(a[0],a[1],a[2],qq,b[0],b[1],b[2],a[3]) for a in Aq for b in Bq}
    print('  q=%d: A(q)=%d B(q)=%d product %d actual %d exact separation %s'%(qq,len(Aq),len(Bq),len(Aq)*len(Bq),len(C),exact)); tot+=len(Aq)*len(Bq)
print('Σ_q |A(q)||B(q)| =',tot)
# §12.7 closed forms as polynomials, against enumeration (rank generating functions of the fibres)
def poly_enum(tuples): 
    d=collections.Counter(sum(t) for t in tuples); return [d[i] for i in range(max(d)+1)]
def Aq_poly(qq):
    d=collections.Counter()
    for nn in range(1,4):
        for ll in range(0,min(nn-1,1)+1):
            for kk in range(max(qq,1),min(4*ll+2,3)+1):
                for ss in range(0,min(kk,3)+1): d[nn+ll+kk+ss]+=1
    return [d[i] for i in range(max(d)+1)]
def Bq_poly(qq):
    d=collections.Counter()
    for ee in range(1,4):
        for ff in range(0,min(ee-1,1)+1):
            for gg in range(0,min(qq,4*ff+2)+1): d[ee+ff+gg]+=1
    return [d[i] for i in range(max(d)+1)]
for qq in range(4):
    C=[c for c in L8 if c[q]==qq]; Ae=poly_enum(set(map(A,C))); Be=poly_enum(set(map(B,C)))
    print('  q=%d: A_q(z) printed == enumerated %s (A_q(1)=%d); B_q(z) printed == enumerated %s (B_q(1)=%d)'%(qq,Aq_poly(qq)==Ae,sum(Ae),Bq_poly(qq)==Be,sum(Be)))
# §12.7.1 the fibres' own constraint graphs (edges = the two-coordinate constraints restricted to each side)
print('A_q graph: edges n–ℓ, ℓ–k, k–2S → degrees n1 ℓ2 k2 2S1: a path (n–ℓ–k–2S); B_q graph: e–f, f–g → a path. The pendant at k is q, which belongs to neither side.')
# §12.7.2 the tower of fibrations: A_q over k with fibre (n,ℓ)-set × 2S-chain; B_q over f with fibre e-set × g-chain; is every bottom fibre a box?
for qq in range(4):
    C=[c for c in L8 if c[q]==qq]
    for kk in sorted(set(c[k] for c in C)):
        P=set((c[n],c[l]) for c in C if c[k]==kk); SS=set(c[s] for c in C if c[k]==kk)
        prod=set((c[n],c[l],c[s]) for c in C if c[k]==kk)=={(a,b,c_) for a,b in P for c_ in SS}
        isbox=len(P)==len(set(a for a,_ in P))*len(set(b for _,b in P))
        print('  q=%d k=%d: (n,ℓ)-set %s (%d) × 2S-chain %d: exact product %s; (n,ℓ)-set is a box %s'%(qq,kk,sorted(P),len(P),len(SS),prod,isbox))
    for ff in sorted(set(c[f] for c in C)):
        Es=set(c[e] for c in C if c[f]==ff); Gs=set(c[g] for c in C if c[f]==ff)
        prod=set((c[e],c[g]) for c in C if c[f]==ff)=={(a,b) for a in Es for b in Gs}
        print('  q=%d f=%d: e-set %s × g-chain %s: exact product %s (a box)'%(qq,ff,sorted(Es),sorted(Gs),prod))
# Figure 12.2: Λ13 sections, A side (n,ℓ,k,2S,2Jc,2K,2J) × B side (e,f,g,2S′,v)
L13=tw.L13(); A13=lambda c:(c[0],c[1],c[2],c[7],c[10],c[11],c[12]); B13=lambda c:(c[4],c[5],c[6],c[8],c[9]); tot=0
for qq in range(4):
    C=[c for c in L13 if c[3]==qq]; Aq=set(map(A13,C)); Bq=set(map(B13,C))
    print('  Λ13 q=%d: %d × %d = %d actual %d exact %s'%(qq,len(Aq),len(Bq),len(Aq)*len(Bq),len(C),len(Aq)*len(Bq)==len(C))); tot+=len(Aq)*len(Bq)
print('Σ =',tot,'= |Λ13|',len(L13))