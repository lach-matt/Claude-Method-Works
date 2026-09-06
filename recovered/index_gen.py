import re,json,collections
L=open('The_Method_1_6-2.md',encoding='utf-8').read().splitlines()
# section map
sec=[None]*len(L); cur=None; appx=None
for i,l in enumerate(L):
    if i<172: sec[i]=None; continue     # contents block
    m=re.match(r'^## (\d+)\.',l)
    if m: cur=f"§{m.group(1)}"; appx=None
    m=re.match(r'^### (\d+\.\d+)',l)
    if m: cur=f"§{m.group(1)}"
    if re.match(r'^# Appendix ([A-F])',l): appx=re.match(r'^# Appendix ([A-F])',l).group(1); cur=f"App {appx}"
    if re.match(r'^# Index',l): cur='Index'
    if re.match(r'^# References',l): cur='Refs'
    sec[i]=cur
H={}  # section -> heading text
for i,l in enumerate(L):
    if sec[i] and re.match(r'^#{1,3} ',l) and sec[i] not in H: H[sec[i]]=l
T=[ # (level, term, parent, regex, hand)
(1,'bracket',None,r'\bbracket',None),
(2,'bracket failure','bracket',r'bracket fail|fail(s|ed|ure)? (the|its) bracket',None),
(2,'bracket width','bracket',r'bracket width|width of (the|a|its) bracket|bracket.{0,15}\bwidth',None),
(2,'interiority','bracket',r'interiorit',None),
(2,'limit-free','bracket',r'limit-free',None),
(2,'the four rules','bracket',r'four rules|Rule 4[ab]\b|rules 1[–-]4',None),
(3,'interiority','the four rules',r'interiorit',None),
(1,'three bodies',None,r'three[- ]bod',None),
(2,'Λ₃','three bodies',r'Λ₃',None),
(2,'shape sphere','three bodies',r'shape sphere',None),
(1,'closure',None,r'\bclosure\b',None),
(2,'closed index','closure',r'closed index',None),
(2,'closure defect','closure',r'closure defect',None),
(2,'closure operator','closure',r'closure operator',None),
(2,'ℛ(X) = X','closure',r'ℛ\(X\) = X',None),
(1,'cost of a guarantee',None,r'cost of (a|the) guarantee',None),
(2,'V = 4ν/3','cost of a guarantee',r'4ν/3',None),
(2,'the floor','cost of a guarantee',r'\bthe floor\b|V > 2 floor|floor at V',None),
(2,'the pole','cost of a guarantee',r'\bthe pole\b',None),
(2,'ν_V','cost of a guarantee',r'ν_V',None),
(1,'extension',None,r'\bextension',None),
(2,'addable cells','extension',r'addable',None),
(2,'adjoinable axes','extension',r'adjoinable',None),
(2,'imposable constraints','extension',r'imposable',None),
(1,'Löwdin',None,r'Löwdin',None),
(2,'challenge','Löwdin',r'Löwdin.{0,30}challenge|challenge.{0,30}Löwdin',None),
(2,'solution','Löwdin',r'Löwdin solution|solution to Löwdin',None),
(1,'prediction',None,r'\bprediction',None),
(3,'E(X) as budget','prediction',r'\bbudget\b',None),
(3,'Sc VI','prediction',r'Sc VI',None),
(3,'second route','prediction',r'second route',None),
(1,'quantum defect',None,r'quantum defect',None),
(2,'isoelectronic law','quantum defect',r'isoelectronic (law|sequence)',None),
(2,'penetration','quantum defect',r'penetrat',None),
(1,'retrieval',None,r'\bretrieval\b',None),
(2,'retrieval redundancy','retrieval',r'retrieval redundancy|redundancy ρ',None),
(2,'route set','retrieval',r'route set',None),
(1,'self-defence',None,r'self-defen',None),
(2,'totality','self-defence',r'\btotality\b',None),
(2,'process index','self-defence',r'process index',None),
(2,'two routes','self-defence',r'two (disjoint |independent )?routes',None),
(2,'ⅅ_def','self-defence',r'ⅅ_def',None),
(2,'ⅅ_phys','self-defence',r'ⅅ_phys',None),
(1,'self-reference',None,r'self-referen',None),
(3,'alphabet recovery','self-reference',r'alphabet recover|recover(s|ed|able)? (the |its )?alphabet',None),
(3,'bound recovery','self-reference',r'bound recover|recover(s|ed|able)? (the |its |every )?bound',None),
(3,'order recovery','self-reference',r'order recover|recover(s|ed|able)? (the |its |an )?order',None),
(1,'the collection',None,r'\bthe collection\b',None),
(3,'decline modes','the collection',r'decline mode',None),
(3,'isoelectronic pairs','the collection',r'isoelectronic pair',None),
(3,'provenance','the collection',r'provenance',None),
(3,'the census','the collection',r'\bcensus\b',None),
(1,'the index',None,None,['Index']),
(3,'index, self-referencing','the index',None,['Index']),
(1,'the record',None,None,None),
(3,'margins','the record',None,['App C']),
(3,'recomputed','the record',None,['App F']),
(3,'withdrawals','the record',None,['§28']),
(1,'index, self-referencing',None,None,['*this page*']),
]
def locs(rx):
    cnt=collections.Counter(); head=set()
    for i,l in enumerate(L):
        s=sec[i]
        if not s or s in ('Index','Refs'): continue
        n=len(re.findall(rx,l,re.I))
        if n:
            cnt[s]+=n
            if re.match(r'^#{1,3} ',l): head.add(s)
    tot=sum(cnt.values())
    thr=1 if tot<10 else (3 if tot<60 else 6)
    out={s for s,n in cnt.items() if n>=thr}|head
    return out,tot
raw={}
for lvl,t,par,rx,hand in T:
    raw[(t,par)]=(set(hand) if hand else (locs(rx)[0] if rx else set()), locs(rx)[1] if rx else 0)
def key(x):
    m=re.match(r'§(\d+)(?:\.(\d+))?',x)
    if m: return (0,int(m.group(1)),int(m.group(2) or 0))
    if x.startswith('App'): return (1,ord(x[-1]),0)
    return (2,0,0)
# closure: parent ⊇ children (union); count violations before union
viol=0; final={}
for lvl,t,par,rx,hand in T: final[(t,par)]=set(raw[(t,par)][0])
for lvl,t,par,rx,hand in reversed(T):
    if par:
        ps=[k for k in final if k[0]==par]
        for p in ps:
            missing=final[(t,par)]-final[p]; viol+=len(missing); final[p]|=final[(t,par)]
print("violations before union:",viol)
for lvl,t,par,rx,hand in T:
    print(lvl,t,"|",raw[(t,par)][1],"|",' · '.join(sorted(final[(t,par)],key=key)))
json.dump({f"{t}|{par}":sorted(v,key=key) for (t,par),v in final.items()},open('/home/claude/index_locs.json','w'),ensure_ascii=False)