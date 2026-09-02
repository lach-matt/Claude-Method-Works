# Appendix F recomputed from the main volume. Rules as F.3 states them, coarse and rerunnable:
# an OCCURRENCE is a number in body text or a table (locators, register/chapter/figure numbers, years in
# bibliography lines and code blocks excluded); coordinates are assigned from the PARAGRAPH carrying it.
import re,sys,itertools,collections
L=open(sys.argv[1] if len(sys.argv)>1 else 'The_Method_1_6-2.md',encoding='utf-8').read().splitlines()
start=[i for i,l in enumerate(L) if l.startswith('# PART 0')][-1]
paras=[]; cur=[]; kind=None; incode=False
def flush():
    global cur
    if cur: paras.append((kind,'\n'.join(cur))); cur=[]
for l in L[start:]:
    if l.strip().startswith('```'): incode=not incode; flush(); continue
    if incode: continue
    if l.startswith('#'): flush(); continue
    if not l.strip(): flush(); continue
    k='table' if (l.startswith('|') or l.startswith('    ') or l.startswith('  ') and re.search(r'\S\s{3,}\S',l)) else 'prose'
    if cur and k!=kind: flush()
    kind=k; cur.append(l)
flush()
NUM=re.compile(r'(?<![\w§.])(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:\s?×\s?10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+)?(?![\w.]\d)')
EXCL=re.compile(r'(§\s?[\dA-F.]+|register(?:s)?\s+\d+(?:[–-]\d+)?|\bR\s?\d{3,4}\b|Chapter \d+|Chapters \d+(?: to \d+)?|Figure \d+\.\d+|Fig\. \d+|Part [IV]+|\(\d{4}\)|\b(1[6-9]\d\d|20[0-2]\d)\b(?=[),;. ])|\bn = \d+|\bZ = \d+|\bℓ = \d+|\bq = \d+|\bd = \d+|\bk = \d+)')
UNIT=r'cm⁻¹|\bfm\b|\bnm\b|\beV\b|hartree|\bkeV\b|MeV|\bpc\b|\bkm\b|\bs\b|\bK\b'
occ=[]
for k,p in paras:
    if re.search(r'^\s*(\*\*)?[A-Z][A-Za-z\-]+, [A-Z]\..*\(\d{4}\)',p) or re.match(r'^\s*[·•-] ',p): continue   # bibliography
    q=EXCL.sub(' ',p)
    for m in NUM.finditer(q):
        s=m.group(0)
        if len(s)==1 and s in '01' and not re.search(r'[=<>≤≥]\s*$',q[:m.start()]): continue   # bare 0/1 are words, not claims
        occ.append((s,k,p))
def cue(p): return bool(re.search(r'§|[Rr]egister|Appendix|recomput|comput|script|\.py|verified|measured|counted|fitted|derived|Table',p))
def qkind(s,p):
    if re.search(UNIT,p): return 'measurement'
    if '%' in p or 'density' in p.lower(): return 'density'
    if re.search(r'\bE\(|defect|E =',p): return 'defect'
    if re.search(r'[≤≥<>]|bracket|bound|between|inside',p): return 'bound'
    if re.search(r'\bper\b|\brate\b|ratio|:\s?1\b|\d\s?:\s?\d',p): return 'rate'
    return 'count'
METH=r'computed|recomputed|counted|measured|fitted|minimis|derived|generated|regressed|solved|proved|verified'
INSET=r'\b(over|across|on|from|of) (the )?\d|\bevery\b|\ball \d|\beach of\b'        # an input SET named
def defn(p):
    meth=bool(re.search(METH,p)); inp=bool(re.search(INSET,p))
    return 2 if meth and inp else 1 if meth else 0          # asserted < stated < stated with inputs (F.3.4: stated ⇔ method named and no input set)
def inputs(k,p):
    if k=='table' or re.search(r'Appendix B|the table|Table|listed|printed',p): return 2   # printed
    if re.search(INSET,p): return 1                                                         # enumerated ⇔ an input set named
    return 0                                                                                # named
def verif(p):
    if re.search(r'\bcaps?\b|varied|under variation|at every|each cap|at cap',p): return 2
    if re.search(r'recomput|verified|checked|reproduc|confirmed|tested|independently',p): return 1
    return 0
cells=collections.defaultdict(set); fibre=collections.Counter()
for s,k,p in occ:
    f=qkind(s,p); fibre[f]+=1; cells[f].add((defn(p),inputs(k,p),verif(p)))
def R(X):
    A=[sorted({x[i] for x in X}) for i in range(3)]
    def phi(i,j,v): return max([x[i] for x in X if x[j]<=v] or [-1])
    return {x for x in itertools.product(*A) if all(x[i]<=phi(i,j,x[j]) for i in range(3) for j in range(3) if i!=j)}
distinct=len({s for s,_,_ in occ}); tables=sum(1 for _,k,_ in occ if k=='table'); prose=len(occ)-tables
nocue=sum(1 for _,_,p in occ if not cue(p))
print(f'F.1: {distinct:,} distinct claim-bearing numbers, {len(occ):,} occurrences: {tables:,} inside tables and {prose:,} in prose. {nocue:,} — {100*nocue/len(occ):.0f}% — no cue.')
tot=0
print('F.3: fibre occurrences distinct admitted E')
for f in ['count','defect','measurement','bound','rate','density']:
    X=cells[f]; adm={x for x in R(X) if not (x[0]==1 and x[1]==1)} if X else set(); a=len(adm); E=a-len(X); tot+=E   # F.3.4's constraint imposed
    print(f'  {f:12s} {fibre[f]:>6,} {len(X):>4} {a:>4} {E:>3}')
print(f'  all {len(occ):,} E {tot}')
v=collections.Counter(verif(p) for _,_,p in occ); d=collections.Counter(defn(p) for _,_,p in occ)
print(f'F.3.1: verification asserted {v[0]:,} recomputed {v[1]:,} under variation {v[2]:,}; definition asserted {d[0]:,} stated {d[1]:,} with inputs {d[2]:,}; {100*v[0]/len(occ):.0f}% asserted')
import math,os
# F.4.2 (ruling 25, register 1762): surviving = D's elements (77, D.5.3/D.5.10's printed count)
# + Math Compendium labelled objects + Physics Compendium labelled parameter objects;
# withdrawn = one claim per Register entry (the book's own sentence), the entry heading count.
# ---- RULING 63 + RULING 66 (chat 52): the entry count is the WHOLE REGISTER, gated against editorial. ----
# Ruling 63 gates the figure so editorial material never enters it; Ruling 66 prepended the genesis
# block (entries 1-164) and ruled that the register's stated extent is the whole record. The count is
# therefore every entry heading from '### 1' to the end, 1 to 1786 = 1,629 — the four front-matter
# subheads excluded (they are not entries), the WORKING-REGISTER file unreachable (editorial, file gate).
# Located BY CONTENT, not by a hardcoded line, so the genesis prepend cannot silently break it.
def register_entries(path):
    assert os.path.basename(path)!='WORKING-REGISTER.md', 'RULING 63: editorial file reached the count'
    L=open(path,encoding='utf-8').read().splitlines()
    g=[i for i,l in enumerate(L) if l.rstrip()=='### 1']
    assert len(g)==1, f'expected exactly one "### 1" genesis start, found {len(g)}'
    F=g[0]+1   # 1-based line where the entries begin (genesis entry 1)
    b=[i for i,l in enumerate(L) if l.rstrip()=='### 165']
    assert len(b)==1, f'expected exactly one "### 165" mature-record boundary, found {len(b)}'
    subs=[l for i,l in enumerate(L) if i+1<F and l.startswith('### ')]
    assert len(subs)==4, f'front-matter subheads: expected 4, found {len(subs)}'
    heads=[l for i,l in enumerate(L) if i+1>=F and l.startswith('### ')]
    nums=[]; grp=0
    for h in heads:
        assert re.match(r'^### [\d,\s]+$',h.rstrip()), f'non-entry heading past the boundary: {h!r}'
        gg=[int(x) for x in re.findall(r'\d+',h)]; nums+=gg; grp+= len(gg)>1
    assert len(heads)+len(subs)==sum(1 for l in L if l.startswith('### ')), 'heading partition lost'
    return len(heads),nums,grp
UNITS='zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
TENS={2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
def _u99(n):
    if n<20: return UNITS[n]
    return TENS[n//10]+('-'+UNITS[n%10] if n%10 else '')
def words(n):   # the fifteen sites print the count in words; it is generated, never typed
    assert 0<n<10000, n
    th,r=divmod(n,1000); h,r2=divmod(r,100); out=[]
    if th: out.append(_u99(th)+' thousand')
    if h: out.append(_u99(h)+' hundred')
    if r2: out.append(('and ' if (th or h) else '')+_u99(r2))
    return ' '.join(out)
DELEM=77; B=os.path.dirname(os.path.abspath(sys.argv[1] if len(sys.argv)>1 else '.'))
MC=os.path.join(B,'The_Method_1_6___Mathematical_Compendium-2.md'); PC=os.path.join(B,'The_Method_1_6___The_Physics_Compendium-2.md'); RG=os.path.join(B,'The_Method_1_6___The_Register-2.md')
if all(os.path.exists(x) for x in (MC,PC,RG)):
    mth=sum(1 for l in open(MC,encoding='utf-8') if l.startswith('### `'))
    phy=sum(1 for l in open(PC,encoding='utf-8') if l.startswith('### '))
    wd,RNUMS,RGRP=register_entries(RG)   # RULING 63: gated count, boundary asserted
    sv=DELEM+mth+phy; pp=sv/(sv+wd); bits=-(pp*math.log2(pp)+(1-pp)*math.log2(1-pp))
    print(f'F.4.2 ruled row: withdrawn {wd:,}  surviving {sv:,} (77+{mth}+{phy})  {wd/sv:.2f} : 1  p {pp:.3f}  bits {bits:.3f}')
else:
    sv=wd=None; print('F.4.2 ruled row: compendium/Register files not beside source; printed figures stand')
n=len(occ); p=n/(n+190); print(f'F.4.2 first-reading third row (frozen): {n:,}  {190/n:.2f} : 1  p {p:.3f}  bits {-(p*math.log2(p)+(1-p)*math.log2(1-p)):.3f}')
if '--write' in sys.argv:
    # RULING 63. The eight Appendix F anchors this block once carried are DEAD: Appendix F was
    # rebuilt on a new domain and F.4.1/F.4.2 now read "Retained as a reference, withdrawn as
    # content". All eight returned 0 matches when measured. They are not kept as no-ops - a
    # substitution that silently matches nothing is the failure this ruling exists to end.
    # The live targets are the seventeen sites in the MAIN volume that state the entry count.
    f=sys.argv[1]; T=open(f,encoding='utf-8').read(); c=0
    hi=max(RNUMS); lo=min(RNUMS); W=words(wd)
    PW=re.compile(r'one thousand [a-z]+ hundred and [a-z]+(?:-[a-z]+)?')
    n=len(PW.findall(T)); assert n==15, f'word-form count sites: expected 15, found {n}'
    T=PW.sub(W,T); c+=n
    P1=r'\b[\d,]+ entries, \d+ to \d+, at this build'
    assert len(re.findall(P1,T))==1, 'site L7363 anchor'
    T=re.sub(P1,f'{wd:,} entries, {lo} to {hi}, at this build',T); c+=1
    P2=r'(436 entries when this paragraph was written, )[\d,]+( at this build)'
    assert len(re.findall(P2,T))==1, 'site L7648 anchor'
    T=re.sub(P2,lambda m:f'{m.group(1)}{wd:,}{m.group(2)}',T); c+=1
    assert c==17, c
    open(f,'w',encoding='utf-8').write(T)
    print(f'register entry count written to {c} sites: {wd:,} ({W}), {lo} to {hi}')

