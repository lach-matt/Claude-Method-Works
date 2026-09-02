# census.py — Phase R1 instrumented census over the six reader-facing members (chat 68).
# Every row is MEASURED by this script; the read decides. Output: DEFECT-CENSUS.tsv (id, class, member, line, item, detail).
import re, collections, sys
D='/home/claude/members/'
F={'main':'The_Method_1_6-2.md','reg':'The_Method_1_6___The_Register-2.md','mc':'The_Method_1_6___Mathematical_Compendium-2.md',
   'pc':'The_Method_1_6___The_Physics_Compendium-2.md','ioi':'The_Method_1_6___The_Index_of_Indices-2.md','sc':'The_Method_1_6___Spectra_Compendium-2.md'}
L={k:open(D+v,encoding='utf-8').read().split('\n') for k,v in F.items()}
rows=[]
def row(cls,mem,ln,item,detail): rows.append((cls,mem,ln,item.replace('\t',' ').replace('\n',' ')[:160],detail.replace('\t',' ').replace('\n',' ')[:200]))
# ---- main heading map and section ranges
heads=[]  # (line, key, level)
for i,l in enumerate(L['main']):
    m=re.match(r'^(#+) (?:§)?(\d+(?:\.\d+)*)\.?\s',l)
    if m: heads.append((i+1,m.group(2),len(m.group(1))))
keys={k for _,k,_ in heads}|{'4.%d'%i for i in range(1,8)}
def rng(key):
    if re.fullmatch(r'4\.[1-7]',key): ln=1440+int(key[2]); return (ln,ln)
    idx=[j for j,(ln,k,lv) in enumerate(heads) if k==key]
    if not idx: return None
    j=idx[-1] if '.' not in key else idx[0]; a=heads[j][0]
    b=len(L['main'])
    for ln,k,lv in heads[j+1:]:
        if not (k==key or k.startswith(key+'.')): b=ln-1; break
    return (a,b)
appx={m.group(1) for l in L['main'] for m in [re.match(r'^## Appendix ([A-Z])\b',l)] if m}
thm_printed={m.group(1) for l in L['main'] for m in [re.match(r'^\s*Theorem (\d+\.\d+)(?:\.| \()',l)] if m}
regnums={int(n) for l in L['reg'] if re.match(r'^### [\d, ]+$',l) for n in re.findall(r'\d+',l)}
# figures placed: number on the ![ line or the next non-empty line
figplaced=set()
for i,l in enumerate(L['main']):
    if l.startswith('!['):
        nxt=next((x for x in L['main'][i+1:i+4] if x.strip()),'')
        for n in re.findall(r'Fig(?:ure|\.)\s?(\d+\.\d+)',l+' '+nxt): figplaced.add(n)
# ---- C1..C5 pointer resolution over all members
for mem,lines in L.items():
    for i,l in enumerate(lines):
        for m in re.finditer(r'§\s?(\d+(?:\.\d+)*)',l):
            if m.group(1) not in keys: row('C1-SECTION-POINTER-UNRESOLVED',mem,i+1,'§'+m.group(1),l.strip())
        for m in re.finditer(r'\b(?:Theorem|Thm\.?)\s(\d+\.\d+)',l):
            t=m.group(1)
            if l.startswith('> **Prior art'): continue
            if t not in thm_printed: row('C2-THEOREM-POINTER-UNPRINTED',mem,i+1,'Theorem '+t,l.strip())
            elif t=='17.1' and re.search(r'§\s?17\.1\b',l): row('C2b-THEOREM-17.1-CITED-AS-§17.1',mem,i+1,'Theorem 17.1 / §17.1',l.strip())
        for m in re.finditer(r'\bFig(?:ure|\.)\s?(\d+\.\d+)',l):
            if m.group(1) not in figplaced: row('C3-FIGURE-POINTER-UNPLACED',mem,i+1,'Figure '+m.group(1),l.strip())
        for m in re.finditer(r'\bAppendix ([A-Z])\b',l):
            if m.group(1) not in appx: row('C4-APPENDIX-POINTER-UNRESOLVED',mem,i+1,'Appendix '+m.group(1),l.strip())
        for m in re.finditer(r'\b(?:R|[Rr]egister|[Ee]ntry|[Ee]ntries)\s(\d{1,4})\b',l):
            n=int(m.group(1))
            if n>1792 or n not in regnums: row('C5-REGISTER-POINTER-UNRESOLVED',mem,i+1,m.group(0),l.strip())
# ---- MC entries
mc=L['mc']; ent=[]; fam=None
for i,l in enumerate(mc):
    if l.startswith('## '): fam=l[3:].strip()
    if l.startswith('### '): ent.append([i+1,l[4:].strip(),fam])
nexthead=[i+1 for i,l in enumerate(mc) if l.startswith('## ')]
for k,e in enumerate(ent):
    a=e[0]; b=ent[k+1][0]-1 if k+1<len(ent) else len(mc)
    b=min([b]+[h-1 for h in nexthead if h>a])
    e.append('\n'.join(mc[a:b])); e.append(b)
def nums(s): return set(re.findall(r'(?<![\w.])\d[\d,]*(?:\.\d+)?(?![\w])',s))
yr=lambda x: re.fullmatch(r'1[5-9]\d\d|20[0-2]\d',x)
regtext={}
cur=None
for l in L['reg']:
    m=re.match(r'^### (\d+)\s*$',l)
    if m: cur=int(m.group(1)); regtext[cur]=[]
    elif cur is not None: regtext[cur].append(l)
regtext={k:'\n'.join(v) for k,v in regtext.items()}
for a,title,family,body,b in ent:
    secs=sorted(set(re.findall(r'§\s?(\d+(?:\.\d+)*)',body)))
    rr=sorted({int(x) for x in re.findall(r'\b(?:R|[Rr]egister)\s(\d{1,4})\b',body)})
    src=''.join('\n'.join(L['main'][x[0]-1:x[1]]) for s in secs for x in [rng(s)] if x)+'\n'+'\n'.join(regtext.get(n,'') for n in rr)
    en=nums(body); sn=nums(src)
    miss=[x for x in sorted(en,key=lambda z:(len(z),z)) if x not in sn and not yr(x) and not re.fullmatch(r'\d{1,2}',x)]
    if not secs and not rr: row('C6a-ENTRY-NO-SOURCE-POINTER','mc',a,title,'no § or Register pointer in entry')
    elif miss: row('C6-NUMBERS-NOT-IN-SOURCE','mc',a,title,'%d of %d: %s | sources §%s R%s'%(len(miss),len([x for x in en if not yr(x) and not re.fullmatch(r'\d{1,2}',x)]),' '.join(miss)[:120],' §'.join(secs)[:40],' R'.join(map(str,rr))[:40]))
    lines=[x for x in body.split('\n')[1:] if x.strip()]
    head_ok=bool(lines) and lines[0].startswith('**')
    scope_ok=any(x.startswith('*') and not x.startswith('**') for x in lines[:4])
    grade=[x for x in lines[:6] if re.match(r'^(Proved|Computed|Measured|Conjectured|Open|Observed|Record-carried|Stated)\b',x)]
    prior=any(x.startswith('> **Prior art') for x in lines)
    missing=[n for n,ok in [('headline',head_ok),('scope',scope_ok),('grade',bool(grade)),('prior-art',prior)] if not ok]
    if missing: row('C11-R-FORM-INCOMPLETE','mc',a,title,'missing: '+', '.join(missing)+(' | first lines: '+' / '.join(x[:40] for x in lines[:3]) if lines else ''))
    if grade and grade[0].startswith('Proved') and not rr: row('C10-PROVED-WITHOUT-REGISTER','mc',a,title,grade[0][:120])
    for m in re.finditer(r'\b(?:MC|W)-\d+|\b[A-Z]{1,2}\.[a-z]{3,6}\b|\bBUILD\s?\d+|\bchat \d+|\b3B\.[a-z]+',body):
        row('C13-HANDLE-LEAK','mc',a,m.group(0),'entry: '+title)
inent=set()
for a,title,family,body,b in ent: inent.update(range(a,b+1))
for i,l in enumerate(mc):
    if i+1 not in inent:
        for m in re.finditer(r'\b(?:MC|W)-\d+|\b[A-Z]{1,2}\.[a-z]{3,6}\b|\bBUILD\s?\d+|\bchat \d+|\b3B\.[a-z]+',l): row('C13-HANDLE-LEAK','mc',i+1,m.group(0),'back matter: '+l.strip())
# duplicates by title / theorem citation across families
tn=collections.defaultdict(list)
for a,title,family,body,b in ent:
    tn[re.sub(r'[^a-z0-9]+',' ',title.lower()).strip()].append((a,family))
    for t in set(re.findall(r'\b(?:Theorem|Thm\.?)\s(\d+\.\d+)',body)): tn['thm '+t].append((a,family))
for k,v in tn.items():
    if len(v)>1 and len({f for _,f in v})>1: row('C12-DUPLICATE-HOME','mc',v[0][0],k,'; '.join('L%d [%s]'%(a,f[:30]) for a,f in v))
# ---- C7 withdrawn-figure survival (main)
alltext={k:'\n'.join(v) for k,v in L.items()}
for i,l in enumerate(L['main']):
    if re.search(r'\b(withdrawn|withdraws?|recomputed|corrected|superseded|retracted)\b',l):
        for n in sorted({x for x in nums(l) if not yr(x) and not re.fullmatch(r'\d{1,2}',x)}):
            pat=r'(?<![\w.])'+re.escape(n)+r'(?![\w])'
            cnt={k:len(re.findall(pat,t)) for k,t in alltext.items()}; cnt['main']-=len(re.findall(pat,l))
            tot=sum(cnt.values())
            if tot: row('C7-WITHDRAWAL-LINE-NUMBER-SURVIVES','main',i+1,n,'other sites: '+' '.join('%s=%d'%(k,c) for k,c in cnt.items() if c)+' | '+l.strip()[:110])
# ---- C8 named statements
names=collections.Counter(); where=collections.defaultdict(set)
for mem,lines in L.items():
    for i,l in enumerate(lines):
        for m in re.finditer(r"\b(?:the|The) ((?:[\w'’\-]+ ){1,3})(lemma|law|criterion|theorem|rule|principle|axiom|inequality|bound)\b",l):
            key=(m.group(1).strip().lower(),m.group(2)); names[key]+=1; where[key].add(mem)
for (nm,kind),c in names.most_common():
    phrase=nm+' '+kind
    stated=any(re.search(r'\*\*[^*]*'+re.escape(phrase)+r'|^#+ .*'+re.escape(nm),l,re.I) for l in L['main'])
    row('C8-NAMED-STATEMENT','all',0,phrase,'sites=%d in %s | bold/heading statement in main: %s'%(c,','.join(sorted(where[(nm,kind)])),'yes' if stated else 'NO'))
# ---- C9 overgeneralisation words (reader-facing members)
for mem,lines in L.items():
    for i,l in enumerate(lines):
        for m in re.finditer(r'\b(at every cap|every configuration|in every case|without exception|for all caps|at all caps|always|never)\b',l):
            row('C9-OVERGENERALISATION-WORD',mem,i+1,m.group(1),l.strip())
# ---- C13 handle leaks outside MC
for mem in ['main','reg','pc','ioi','sc']:
    for i,l in enumerate(L[mem]):
        for m in re.finditer(r'\bMC-\d+\b|\bW-\d{2,3}\b|\bBUILD-?\d+\b|\b3B\.[a-z]+\b|\b[LKMWTEB]\.(?:tree|three|tri|two|one|four|five|six)\b',l):
            row('C13-HANDLE-LEAK',mem,i+1,m.group(0),l.strip())
# ---- write
with open('/home/claude/DEFECT-CENSUS.tsv','w',encoding='utf-8') as f:
    f.write('id\tclass\tmember\tline\titem\tdetail\n')
    for n,(c,m,ln,it,dt) in enumerate(rows,1): f.write('%d\t%s\t%s\t%s\t%s\t%s\n'%(n,c,m,ln,it,dt))
cnt=collections.Counter(c for c,_,_,_,_ in rows)
print('rows',len(rows)); 
for c in sorted(cnt): print(' ',c,cnt[c],'|',dict(collections.Counter(m for cc,m,_,_,_ in rows if cc==c)))
print('headings',len(heads),'keys',len(keys),'appendices',sorted(appx),'theorems printed',sorted(thm_printed),'reg numbers',len(regnums),'figs placed',len(figplaced),'MC entries',len(ent))
