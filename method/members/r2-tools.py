# r2-tools.py — Phase R2 chapter checker (chat 70). Clerical checks only; computation is per-chapter (r2-chN.py).
# usage: python3 r2-tools.py {lines|pointers|figures|census|layout|constants} A B
import re, sys, collections
D='/home/claude/members/'
F={'main':'The_Method_1_6-2.md','reg':'The_Method_1_6___The_Register-2.md','mc':'The_Method_1_6___Mathematical_Compendium-2.md',
   'pc':'The_Method_1_6___The_Physics_Compendium-2.md','ioi':'The_Method_1_6___The_Index_of_Indices-2.md','sc':'The_Method_1_6___Spectra_Compendium-2.md'}
L={k:open(D+v,encoding='utf-8').read().split('\n') for k,v in F.items()}
M=L['main']; R=L['reg']
cmd=sys.argv[1]; A=int(sys.argv[2]) if len(sys.argv)>2 else 1; B=int(sys.argv[3]) if len(sys.argv)>3 else A
seg=[(i,M[i-1]) for i in range(A,B+1)]
heads={}   # '16.1' -> (line, text) for ### and ####; 'ch16' -> line; 'appA' -> line; 'A.4' -> line
for i,l in enumerate(M,1):
    m=re.match(r'^(#{2,4}) (.+)$',l)
    if not m: continue
    t=m.group(2)
    m2=re.match(r'^(\d+)\. ',t)
    if m.group(1)=='##' and m2: heads['ch'+m2.group(1)]=(i,t)
    m3=re.match(r'^Appendix ([A-G])',t)
    if m.group(1)=='##' and m3: heads['app'+m3.group(1)]=(i,t)
    m4=re.match(r'^([A-G]\.\d+|\d+\.\d+(?:\.\d+)*)\s',t)
    if m4: heads[m4.group(1)]=(i,t)
regheads={}  # entry number -> (line, heading) incl. grouped
for i,l in enumerate(R,1):
    m=re.match(r'^### ([\d, ]+)',l)
    if m:
        for n in re.findall(r'\d+',m.group(1)): regheads.setdefault(n,(i,l[:60]))
def other_sites(tok, exclude_range, members=('main','reg','mc','pc','ioi','sc')):
    out=[]
    pat=re.compile(r'(?<![\d.,])'+re.escape(tok)+r'(?![\d.])')
    for k in members:
        for i,l in enumerate(L[k],1):
            if k=='main' and exclude_range[0]<=i<=exclude_range[1]: continue
            if pat.search(l): out.append((k,i))
    return out
if cmd=='lines':
    for i,l in seg: print(f'{i:5d}| {l}')
elif cmd=='pointers':
    seen=collections.OrderedDict()
    for i,l in seg:
        for m in re.finditer(r'§\s?(\d+\.\d+(?:\.\d+)*|\d+)(?!\d)',l): seen.setdefault(('§',m.group(1)),[]).append(i)
        for m in re.finditer(r'\b(?:Chapter|Ch\.)\s?(\d+)',l): seen.setdefault(('Ch',m.group(1)),[]).append(i)
        for m in re.finditer(r'\bAppendix ([A-G])\b(?!\.)',l): seen.setdefault(('App',m.group(1)),[]).append(i)
        for m in re.finditer(r'(?<![A-Za-z§])([A-G]\.\d+)(?![\d.])',l): seen.setdefault(('AppSec',m.group(1)),[]).append(i)
        for m in re.finditer(r'\b(?:Registers?|reg\.|entries|entry)\s?(\d+(?:\s?[–-]\s?\d+)?(?:,\s?\d+)*)',l):
            for n in re.findall(r'\d+',m.group(1)): seen.setdefault(('Reg',n),[]).append(i)
        for m in re.finditer(r'\b(Theorem|Lemma|Figure|Table)\s?(\d+\.\d+)',l): seen.setdefault((m.group(1),m.group(2)),[]).append(i)
    for (kind,key),lines in seen.items():
        lines=sorted(set(lines)); ls=','.join(map(str,lines[:6]))+('…' if len(lines)>6 else '')
        if kind=='§':
            h=heads.get(key)
            if h is None and key.count('.')==0: h=heads.get('ch'+key)
            print(f'§{key:<9} at L{ls:<28} -> ' + (f'L{h[0]} "{h[1][:60]}"' if h else 'UNRESOLVED (no heading)'))
        elif kind=='Ch':
            h=heads.get('ch'+key); print(f'Ch.{key:<8} at L{ls:<28} -> ' + (f'L{h[0]} "{h[1][:60]}"' if h else 'UNRESOLVED'))
        elif kind=='App':
            h=heads.get('app'+key); print(f'App.{key:<7} at L{ls:<28} -> ' + (f'L{h[0]} "{h[1][:60]}"' if h else 'UNRESOLVED'))
        elif kind=='AppSec':
            h=heads.get(key); print(f'{key:<10} at L{ls:<28} -> ' + (f'L{h[0]} "{h[1][:60]}"' if h else 'UNRESOLVED (no ### heading)'))
        elif kind=='Reg':
            h=regheads.get(key); print(f'Reg {key:<6} at L{ls:<28} -> ' + (f'R L{h[0]} "{h[1]}"'+(' [GROUPED]' if ',' in h[1] else '') if h else 'UNRESOLVED (no Register heading)'))
        else:
            o=other_sites(f'{kind} {key}',(A,B),('main',)); placed=[i for i,l in enumerate(M,1) if l.startswith('![') and key in l] if kind=='Figure' else []
            print(f'{kind} {key:<6} at L{ls:<28} -> other main sites {len(o)} {o[:3]}' + (f' placed {placed}' if kind=="Figure" else ''))
elif cmd=='figures':
    toks=collections.OrderedDict()
    for i,l in seg:
        l2=re.sub(r'§\s?[\d.]+|\bL\d+\b|\b(?:Chapter|Ch\.|Register|Registers|reg\.|Figure|Theorem|Table|Appendix)\s?[\dA-G.,–-]+','',l)
        for m in re.finditer(r'(?<![\w.])(\d{1,3}(?:,\d{3})+|\d+\.\d+|\d+)(\s?%)?',l2):
            t=m.group(1)+(' %' if m.group(2) else '')
            if re.fullmatch(r'\d',m.group(1)) : continue   # single digits: not audited by grep
            toks.setdefault(t,[]).append(i)
    for t,lines in toks.items():
        core=t.replace(' %','')
        o=other_sites(core,(A,B))
        cnt=collections.Counter(k for k,_ in o)
        first=[f'{k}:L{i}' for k,i in o[:3]]
        print(f'{t:>12}  L{",".join(map(str,sorted(set(lines))[:5])):<24} other sites {len(o):4d} {dict(cnt)} {first}')
elif cmd=='census':
    rows=[l.split('\t') for l in open(D+'DEFECT-CENSUS.tsv',encoding='utf-8').read().split('\n')[1:] if l]
    for r in rows:
        if r[2]=='main' and A<=int(r[3])<=B: print('\t'.join(r)[:230])
    print('rows in range:',sum(1 for r in rows if r[2]=='main' and A<=int(r[3])<=B))
elif cmd=='layout':
    for i,l in seg:
        if len(re.findall(r'\S {2,}\S',l))>=3: print(f'L{i} column-dump ({len(re.findall(r"\S {2,}\S",l))} gaps): {l[:80]}')
        if l.startswith('    ') and not re.match(r'^\s*([-*]|\d+\.)\s',l): print(f'L{i} 4-space paragraph (renders as code): {l.strip()[:70]}')
    # duplicate table headers / plain-line subheads
    for i,l in seg:
        if re.match(r'^\d+\.\d+ [A-Z]',l): print(f'L{i} plain-line subhead: {l[:70]}')
elif cmd=='constants':
    # every printed occurrence of the core tower and structural constants, all six volumes, against tower-2.py values and the banked invariants
    consts={'976':'|Λ8|','1,654':'|Λ9|','2,535':'|Λ10|','13,585':'|Λ11|','70,905':'|Λ12|','199,130':'|Λ13|','475,800':'C(976,2)'}
    for c,name in consts.items():
        o=other_sites(c,(0,0)); cnt=collections.Counter(k for k,_ in o); print(f'{c:>8} {name:<8} sites {len(o):4d} {dict(cnt)}')
    # variants that would betray a stale or mistyped tower value
    for bad in ['1,653','1,655','2,534','2,536','13,584','13,586','70,904','70,906','199,129','199,131','975','977','1654 ','2535 ','13585','70905','199130']:
        o=other_sites(bad.strip(),(0,0))
        if o: print(f'VARIANT {bad!r}: {len(o)} sites {o[:4]}')
