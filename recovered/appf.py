# Appendix F recomputed from the main volume (register 1756). Rules as F.3 states them, coarse and rerunnable:
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
def defn(p):
    meth=bool(re.search(r'computed|recomputed|counted|measured|fitted|minimis|derived|generated|regressed|solved|proved|verified',p))
    inp=bool(re.search(r'\bfrom\b|\bover\b|\bacross\b|\busing\b|\bon the\b|\bof the\b',p))
    return 2 if meth and inp else 1 if meth else 0          # asserted < stated < stated with inputs
def inputs(k,p):
    if k=='table' or re.search(r'Appendix B|the table|Table|listed|printed',p): return 2   # printed
    if re.search(r'\b(over|across|on|of) (the )?\d|every|all \d|each of',p): return 1       # enumerated
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
    X=cells[f]; a=len(R(X)) if X else 0; E=a-len(X); tot+=E
    print(f'  {f:12s} {fibre[f]:>6,} {len(X):>4} {a:>4} {E:>3}')
print(f'  all {len(occ):,} E {tot}')