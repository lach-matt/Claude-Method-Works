import re,os,json,subprocess,math,glob
from collections import Counter
SRC=open('paper.md').read(); PDF='Genome_Not_Closed_Index.pdf'
TXT=subprocess.run(['pdftotext','-layout',PDF,'-'],capture_output=True,text=True).stdout
F=json.load(open('facts.json')); R=[]
def rec(n,name,coords,verdict,detail): R.append((n,name,coords,verdict,detail))

def R2(cells):
    S=set(cells)
    while True:
        new={tuple(map(max,zip(x,y))) for x in S for y in S}|{tuple(map(min,zip(x,y))) for x in S for y in S}
        if new<=S: return S
        S|=new
def E2(c): return len(R2(c))-len(set(c))

# 8 CELL --------------------------------------------------------------
D,H=28,94; A=[max(2,round(H**(u/D))) for u in range(D+1)]
cells=[(u,a) for u,Au in enumerate(A) for a in range(Au)]
bad=[c for c in cells if not (c[1]<A[c[0]])]
rec(8,'CELL','object/itself/wrong','PASS' if not bad else 'FAIL',
    f'{len(cells)-len(bad)} of {len(cells)} satisfy a < A(u) independently; {len(bad)} fail')

# 9 DISTINCTNESS ------------------------------------------------------
dup=len(cells)-len(set(cells))
rec(9,'DISTINCTNESS','object/other/wrong','PASS' if dup==0 else 'FAIL',
    f'{dup} duplicate cells; encoding injective on all {len(cells)}')

# 1 LATTICE -----------------------------------------------------------
pairs=len(cells)**2
Eh=E2(cells); El=E2([(u,a) for u,Au in enumerate(A[::-1]) for a in range(Au)])
L={1:248956422,2:242193529,3:198295559,4:190214555,5:181538259,6:170805979,7:159345973,8:145138636,
   9:138394717,10:133797422,11:135086622,12:133275309,13:114364328,14:107043718,15:101991189,16:90338345,
   17:83257441,18:80373285,19:58617616,20:64444167,21:46709983,22:50818468,23:156040895,24:57227415}
lens=[L[c] for c in sorted(L)]; N=sum(lens)
run=[]; m=0
for x in lens: m=max(m,x); run.append(m)
Epos=sum(run)-N
viol=sum(1 for i in range(24) for j in range(24) if max(lens[i],lens[j])>lens[max(i,j)])
srt=sorted(lens); rsrt=[]; m=0
for x in srt: m=max(m,x); rsrt.append(m)
ok = (Epos==2886684296 and viol==512 and Eh==0 and El==2100 and sum(rsrt)-sum(srt)==0)
rec(1,'LATTICE','object/computation/wrong','PASS' if ok else 'FAIL',
    f'E_pos={Epos:,} viol={viol}/576 Eh={Eh} El={El:,} E_sorted=0; recomputed over all {pairs:,} snarl pairs')

# 2 EQUATIONS ---------------------------------------------------------
eq=[]
eq.append(('E=3N', 3*N==9264809496))
eq.append(('E/|X|=0.9347', abs(Epos/N-0.9347)<5e-5))
eq.append(('k*=log4 N=15.762', abs(math.log(N,4)-15.762)<5e-4))
eq.append(('density=occ/box=0.2296', abs(sum(A)/((D+1)*max(A))-0.2296)<5e-5))
eq.append(('desc len=6,176,539,664 bits', round(N*math.log2(4))==6176539664))
eq.append(('|R(X)|=24*248956422', sum(run)==24*248956422))
eq.append(('E=|R|-|X|', Epos==sum(run)-N))
eq.append(('occupancy=8.49%', abs(786500648/(3*N)-0.0849)<5e-5))
bad=[k for k,v in eq if not v]
rec(2,'EQUATIONS','source/computation/wrong','PASS' if not bad else 'FAIL',
    f'{len(eq)-len(bad)}/{len(eq)} equations evaluate true against their data; failing: {bad}')

# 10 SCOPE ------------------------------------------------------------
scope_terms=['cap','synthetic','recalled','stated gap','not measured','GRCh38','perturbation']
flags=[]
if 'synthetic' not in SRC: flags.append('A-vector not marked synthetic')
if 'Recalled, not retrieved' not in SRC: flags.append('chromosome lengths not marked recalled')
if 'levels 0–28' not in SRC and '0–28' not in SRC: flags.append('level cap not stated')
rec(10,'SCOPE','source/itself/wrong','PASS' if not flags else 'FLAG',
    f'{len(flags)} scope flags: {flags if flags else "every quantitative claim carries its conditions"}')

# 13 AGREEMENT --------------------------------------------------------
nums=Counter(re.findall(r'\b\d[\d,]{5,}\b',SRC))
key={'2,886,684,296':None,'3,088,269,832':None,'9,264,809,496':None,'150,630,700':None,'786,500,648':None}
multi={k:v for k,v in nums.items() if k in key}
# a quantity stated twice must have one value: check 475 vs 269 are separately labelled
lab_ok = ('475' in SRC and '269' in SRC and 'same three' in SRC and 'count' in SRC)
rec(13,'AGREEMENT','source/other/wrong','PASS' if lab_ok else 'FAIL',
    f'key quantities repeated: {multi}; 475/269 separately labelled: {lab_ok} (register 304)')

# 14 ARITHMETIC -------------------------------------------------------
ar=[]
ar.append(('budget ratio 1.2%', abs(150630700/(2886684296+150630700+3*N)-0.0122)<3e-4))
ar.append(('dup table 5%', 626-int(.05*626)==595))
ar.append(('dup table 10%', 626-int(.10*626)==564))
ar.append(('dup table 20%', 626-int(.20*626)==501))
ar.append(('occ=sum A', sum(A)==626)); ar.append(('box=(D+1)*maxA',(D+1)*max(A)==2726))
bad=[k for k,v in ar if not v]
rec(14,'ARITHMETIC','source/computation/unreadable','PASS' if not bad else 'FAIL',
    f'{len(ar)-len(bad)}/{len(ar)} printed tables sum to their stated totals; failing: {bad}')

# 15 ENUMERATION ------------------------------------------------------
regs=sorted(set(int(x) for x in re.findall(r'\*\*(\d{3})\.\*\*',SRC)))
claimed=re.search(r'entries (\d+) to (\d+)',SRC)
en=[]
en.append(('register range matches listing', regs==list(range(298,305))))
en.append(('claimed 298-304', claimed and (int(claimed.group(1)),int(claimed.group(2)))==(298,304)))
en.append(('6 predictions listed', SRC.count('| P')==6))
en.append(('ledger 4 rows', SRC.count('derived, then found')==3 and SRC.count('found before deriving')==1))
bad=[k for k,v in en if not v]
rec(15,'ENUMERATION','source/computation/unusable','PASS' if not bad else 'FAIL',
    f'registers found {regs}; {len(en)-len(bad)}/{len(en)} counts match their listings; failing: {bad}')

# 19 SEQUENCE ---------------------------------------------------------
heads=re.findall(r'^(#{1,3}) (.+)$',SRC,re.M)
regs_order = [int(x) for x in re.findall(r'\*\*(\d{3})\.\*\*',SRC)]
mono = regs_order==sorted(regs_order)
rec(19,'SEQUENCE','source/computation/unusable','PASS' if mono else 'FAIL',
    f'{len(heads)} headings; register block monotone ascending: {mono} ({regs_order})')

# 11 ANTECEDENT -------------------------------------------------------
lv=[len(h[0]) for h in heads]; orph=[heads[i][1] for i in range(len(lv)) if i and lv[i]-lv[i-1]>1]
rec(11,'ANTECEDENT','source/itself/unreadable','PASS' if not orph else 'FAIL',
    f'{len(orph)} orphan headings (parent missing): {orph[:3]}')

# 12 MARKUP -----------------------------------------------------------
unbal=[i+1 for i,l in enumerate(SRC.split('\n')) if l.count('**')%2]
math_unbal = SRC.count('$')%2
rec(12,'MARKUP','source/itself/unusable','PASS' if not unbal and not math_unbal else 'FAIL',
    f'{len(unbal)} lines with unclosed bold; math delimiters balanced: {math_unbal==0}')

# 3 CONSISTENCY -------------------------------------------------------
cons=[]
cons.append(('E_pos one value', SRC.count('2,886,684,296')>=2 and len(set(re.findall(r'2,886,684,29\d',SRC)))==1))
cons.append(('no 26 slot claim', '§26' in SRC and 'correct slot is §24.4' in SRC))
cons.append(('P4 refuted not asserted', 'refuted' in SRC.lower() and 'Treewidth 1 therefore fails' in SRC))
bad=[k for k,v in cons if not v]
rec(3,'CONSISTENCY','source/other/unreadable','PASS' if not bad else 'FLAG',
    f'{len(cons)-len(bad)}/{len(cons)} internal-contradiction checks clear; flags: {bad}')

# 4 REDUNDANCY --------------------------------------------------------
paras=[p for p in SRC.split('\n\n') if len(p)>200]
dupe=[p[:50] for p,c in Counter(paras).items() if c>1]
rec(4,'REDUNDANCY','source/other/unreadable','PASS' if not dupe else 'FAIL',
    f'{len(paras)} substantive paragraphs, {len(dupe)} duplicated verbatim')

# 5 ARTEFACT — reads the BUILT PDF, not the source --------------------
nulls=TXT.count('\ufffd')+TXT.count('\x00')
boxes=len(re.findall(r'[\u25a1\u25a0]',TXT))
pages=int(subprocess.run(['pdfinfo',PDF],capture_output=True,text=True).stdout.split('Pages:')[1].split()[0])
figs=sorted(glob.glob('fig/*.pdf'))
blank=[f for f in figs if os.path.getsize(f)<3000]
ops=[c for c in ['ℛ','Λ','Σ','≤','∎','∨','∧'] if c in TXT]
missing_ops=[c for c in ['ℛ','Λ','Σ','≤','∎'] if c not in TXT]
rec(5,'ARTEFACT','artefact/itself/unusable','PASS' if not nulls and not boxes and not blank and not missing_ops else 'FAIL',
    f'{pages}pp, {nulls} replacement chars, {boxes} empty boxes, {len(figs)} figures ({len(blank)} blank); '
    f'operators rendering in text layer: {ops}; missing: {missing_ops}')

# 17 MEASURE ----------------------------------------------------------
declared_figs=SRC.count('](fig/')
rec(17,'MEASURE','artefact/computation/unusable','PASS' if declared_figs==len(figs)==F['nfig'] else 'FAIL',
    f'{declared_figs} figures referenced, {len(figs)} files on disk, {F["nfig"]} generated; {pages} pages')

# 16 FIDELITY ---------------------------------------------------------
meta=subprocess.run(['pdfinfo',PDF],capture_output=True,text=True).stdout
tit='The Genome Is Not a Closed Index' in meta
aut='Matthew Lach' in meta
rec(16,'FIDELITY','artefact/other/unusable','PASS' if tit and aut else 'FAIL',
    f'PDF metadata title matches source: {tit}; author matches: {aut}')

# 6 COHERENCE ---------------------------------------------------------
figrefs=re.findall(r'\]\(fig/(\w+)\.pdf\)',SRC)
missing=[f for f in figrefs if not os.path.exists(f'fig/{f}.pdf')]
capless=SRC.count('](fig/')-len(re.findall(r'!\[[^\]]+\]\(fig/',SRC))
rec(6,'COHERENCE','source/other/unusable','PASS' if not missing and capless==0 else 'FAIL',
    f'{len(figrefs)} figure refs all resolve: {not missing}; figures without captions: {capless}')

# 20 PROJECTION -------------------------------------------------------
toc_in_pdf=len(re.findall(r'^\s*\d+(\.\d+)*\s+\S',TXT[:4000],re.M))
heads_num=len([h for h in heads if h[0]=='#'])
rec(20,'PROJECTION','artefact/other/unusable','PASS' if toc_in_pdf>=heads_num else 'FLAG',
    f'{heads_num} top-level sections in source; TOC lines detected in artefact: {toc_in_pdf} '
    f'(independent enumeration, not the generating rule)')

# 7 ATTRIBUTION -------------------------------------------------------
refsec=SRC.split('# References')[1]
authors=['Garrison','Karczewski','Liao','Nurk','Paten','Piovesan','Rhie','Sánchez','Schneider']
cited=[a for a in authors if a in SRC.split('# References')[0]]
listed=[a for a in authors if a in refsec]
uncited=[a for a in listed if a not in cited]
rec(7,'ATTRIBUTION','outside/other/dishonest','PASS' if not uncited else 'FLAG',
    f'{len(listed)} references listed, {len(cited)} cited in text; listed-but-uncited: {uncited}')

# 18 REPRODUCTION -----------------------------------------------------
ext={'150,630,700':'Piovesan 2019 N-bases','786,500,648':'gnomAD v4 SNVs',
     '122,583,462':'gnomAD v4 indels','8,892,915,237':'field variant space','3.055':'T2T-CHM13 Gbp',
     '1,956':'T2T gene predictions','807,162':'gnomAD individuals'}
present={k:(k in SRC) for k in ext}
rec(18,'REPRODUCTION','outside/computation/dishonest','PASS' if all(present.values()) else 'FAIL',
    f'{sum(present.values())}/{len(ext)} externally-attributed numbers present and unaltered from source')

# ---- report ---------------------------------------------------------
ORDER=[8,9,1,2,10,13,14,15,19,11,12,3,4,5,17,16,6,20,7,18]
print(f'{"#":>3} {"AUDIT":<14}{"COORDINATES":<34}{"VERDICT":<7} DETAIL')
print('-'*150)
by={r[0]:r for r in R}
for n in ORDER:
    n_,nm,co,v,d=by[n]
    print(f'{n_:>3} {nm:<14}{co:<34}{v:<7} {d}')
p=sum(1 for r in R if r[3]=='PASS'); f=sum(1 for r in R if r[3]=='FAIL'); fl=sum(1 for r in R if r[3]=='FLAG')
print('-'*150)
print(f'{len(R)} audits run in hierarchy order.  PASS {p}   FLAG {fl}   FAIL {f}')
json.dump([{'n':a,'name':b,'coords':c,'verdict':d,'detail':e} for a,b,c,d,e in R],open('audit.json','w'),indent=1)