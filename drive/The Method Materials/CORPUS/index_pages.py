# Print index: map every §-locator in the main volume's Index block to the page its heading
# starts on in a pressed PDF, and write a press-only copy of the source with page numbers in the Index.
# usage: python3 index_pages.py <src.md> <first-pass.pdf> <out.md>
import re,sys,subprocess
src,pdf,out=sys.argv[1:4]
L=open(src,encoding='utf-8').read().splitlines()
heads={}   # locator -> heading text
allh=[]    # (level, text) for the generic Contents
DEPTH=int(sys.argv[4]) if len(sys.argv)>4 else 2
body=[i for i,l in enumerate(L) if l.startswith('# PART 0')]
body=body[-1] if body else 1
for l in L[body:]:
    mh=re.match(r'^(#{1,3}) (.*)',l)
    if mh and len(mh.group(1))<=DEPTH+1 and not l.startswith('# PART'): allh.append((len(mh.group(1)),mh.group(2))); heads.setdefault('H:'+mh.group(2),mh.group(2))
    m=re.match(r'^## (\d+)\. (.*)',l)
    if m: heads.setdefault('§'+m.group(1),m.group(2)); continue
    m=re.match(r'^### (\d+\.\d+) (.*)',l)
    if m: heads.setdefault('§'+m.group(1),m.group(2)); continue
    m=re.match(r'^## Appendix ([A-Z]) — (.*)',l)
    if m: heads.setdefault('App '+m.group(1),m.group(2))
pages=subprocess.run(['pdftotext','-layout',pdf,'-'],capture_output=True,text=True).stdout.split('\f')
def norm(s): return re.sub(r'[^a-z0-9]+',' ',re.sub(r'\*|_|`','',s).lower()).strip()
ptext=[norm(p) for p in pages]
# the printed TOC also carries every heading: take the LAST page after the front matter on which the heading opens a line
haslit=any(re.match(r'^\s*#{0,3}\s*Contents\s*$',l) for l in L)
# FRONT BOUNDARY BY CONTENT (chat 16). The old rule was positional — `i>3` for a literal Contents,
# `1` otherwise — and both let a heading match ITSELF inside the printed Contents. That produced a
# STABLE WRONG map: once an entry read page N, the Contents on page N kept re-matching it there, and
# the convergence check passed. Measured at BUILD-16: math ~139/308, ioi 29/61, physics 24/61,
# spectra 5/31, main 13 entries plus every App locator. Convergence is not correctness.
# A Contents page is identified by its leader dots, not by its number.
# The boundary is a LINE, not a page. A page-level skip cannot work: in the Index of Indices the
# Contents tail and the first body heading share page 2, so skipping the page loses the heading and
# keeping it re-admits the Contents. Every Contents entry carries leader dots and no real heading
# does, so the dots are the discriminator. front stays only to drop a title page when one exists.
def bodylines(p): return [l for l in p.splitlines() if '……' not in l]
front=0
pm={}
for loc,h in heads.items():
    num=loc.replace('§','').replace('App ','appendix '); want=norm(num+' '+h) if not loc.startswith('H:') else norm(h)
    _sl=0 if (want and want[-1].isdigit()) else 6   # W-082 repair (chat 51, B12): a trailing-numeral discriminator
    _wp=want[:max(12,len(want)-_sl)]                 # must not be deleted by the drift slack, or a prose line takes the map
    for i,p in enumerate(pages):
        if i<front: continue
        lines=[norm(l) for l in bodylines(p)]
        # W-082 (chat 50). The prefix branch below carries six characters of slack for PDF text drift.
        # For a heading whose ONLY discriminator is a trailing numeral the slack deletes exactly the
        # discriminator, and a PROSE line that merely opens with the same words then takes the mapping
        # — Physics 'channel equation, a — 0.3772' was captured by p14's 'channel equation a 8 channel
        # equation e0 8 ...' four pages ahead of its own heading. The slack is KEPT, because drift
        # truncates a heading; the guard is that a heading line cannot be much LONGER than the heading.
        if any(l==want or (len(want)>12 and l.startswith(_wp) and len(l)<=len(want)+6) or (l.startswith(norm(num)+' ') and want.startswith(l) and len(l)>len(norm(num))+8) for l in lines):
            pm[loc]=i+1; break
    # WRAPPED-HEADING FALLBACK (chat 16). The test above compares whole LINES, so a heading long
    # enough to wrap in the PDF matches nothing and drops out of the Contents silently. norm() over
    # the whole page collapses the wrap. Long headings only, so a short string cannot match spuriously.
    if loc not in pm and len(want)>18:
        for i,p in enumerate(pages):
            if i<front: continue
            if want in norm("\n".join(bodylines(p))): pm[loc]=i+1; break
print('headings',len(heads),'mapped',len(pm))
_un=[k for k in heads if k not in pm]
if _un: print('UNMAPPED HEADINGS (absent from the Contents):',[ (k, heads[k][:60]) for k in _un ])
ixs=[i for i,l in enumerate(L) if l.startswith('## Index')]
ix=ixs[-1] if ixs else len(L)
missing=set(); n=0
def sub(m):
    global n
    loc=m.group(0); n+=1
    if loc in pm: return f'{loc} ({pm[loc]})'
    missing.add(loc); return loc
for i in range(ix,len(L)):
    if L[i].startswith('## ') and i>ix: break
    if '……' in L[i]: L[i]=re.sub(r'§\d+(?:\.\d+)?|App [A-Z]',sub,L[i])
print('locators',n,'unmapped',sorted(missing)[:20],len(missing))
# Contents with page numbers, replacing the source's literal contents block (which build.py otherwise strips)
ci=[i for i,l in enumerate(L) if re.match(r'^\s*#{0,3}\s*Contents\s*$',l)]
if ci:
    i=ci[0]; parts=[k for k,l in enumerate(L) if k>i and re.match(r'^# PART 0',l)]; j=parts[1] if len(parts)>1 else i+1
    toc=['## Contents','']
    for l in L[body:]:
        m=re.match(r'^# (PART .*)',l)
        if m:
            if m.group(1).startswith('PART 0'): continue   # RULED, author, chat 16: PART 0 is not listed
            toc.append(''); toc.append('**'+m.group(1)+'**'); toc.append(''); continue
        m=re.match(r'^## (\d+)\. (.*)',l)
        # `1. ` at line start is an ORDERED LIST to pandoc, so every chapter printed as a list item
        # with list spacing (chat 16, found in the object). Escaping the period keeps it a plain line.
        if m: toc.append(f"{m.group(1)}\\. {m.group(2)} …… {pm.get('§'+m.group(1),'')}  "); continue
        m=re.match(r'^## (Appendix [A-Z]) — (.*)',l)
        if m: toc.append(f"{m.group(1)} — {m.group(2)} …… {pm.get('App '+m.group(1)[-1],'')}  "); continue
        m=re.match(r'^## (Index|References)\b',l)
        if m: toc.append(f"{m.group(1)}  "); continue
    L=L[:i]+toc+['']+L[j:]
    print('contents block written',len(toc),'lines')
else:
    _title=allh[0][1] if allh and allh[0][0]==1 else None   # a volume's own title is not a Contents entry
    toc=['## Contents','']+[('  ' if lv==3 else '')+f"{h} …… {pm.get('H:'+h,'')}  " for lv,h in allh if h!='Contents' and h!=_title and pm.get('H:'+h)]
    k=1 if L and L[0].startswith('# ') else 0
    L=L[:k]+['']+toc+['']+L[k:]
    print('generic contents written',len(toc)-2,'headings')
open(out,'w',encoding='utf-8').write('\n'.join(L)+'\n')
