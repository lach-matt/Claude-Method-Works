# Print index (register 1756): map every §-locator in the main volume's Index block to the page its heading
# starts on in a pressed PDF, and write a press-only copy of the source with page numbers in the Index.
# usage: python3 index_pages.py <src.md> <first-pass.pdf> <out.md>
import re,sys,subprocess
src,pdf,out=sys.argv[1:4]
L=open(src,encoding='utf-8').read().splitlines()
body=[i for i,l in enumerate(L) if l.startswith('# PART 0')][-1]
heads={}   # locator -> heading text
for l in L[body:]:
    m=re.match(r'^## (\d+)\. (.*)',l)
    if m: heads.setdefault('§'+m.group(1),m.group(2)); continue
    m=re.match(r'^### (\d+\.\d+) (.*)',l)
    if m: heads.setdefault('§'+m.group(1),m.group(2)); continue
    m=re.match(r'^## Appendix ([A-F]) — (.*)',l)
    if m: heads.setdefault('App '+m.group(1),m.group(2))
pages=subprocess.run(['pdftotext','-layout',pdf,'-'],capture_output=True,text=True).stdout.split('\f')
def norm(s): return re.sub(r'[^a-z0-9]+',' ',re.sub(r'\*|_|`','',s).lower()).strip()
ptext=[norm(p) for p in pages]
# the printed TOC also carries every heading: take the LAST page after the front matter on which the heading opens a line
front=next((i for i,p in enumerate(pages) if re.search(r'^\s*(1\.|PART 0)',p,re.M) and i>3),3)
pm={}
for loc,h in heads.items():
    key=norm(h)[:40]; num=loc.replace('§','').replace('App ','Appendix ')
    hit=None
    for i,p in enumerate(pages):
        if i<front: continue
        if re.search(r'^\s*'+re.escape(num)+r'\.?\s+'+re.escape(key[:20]),norm(p).replace('\n',' '),re.M) or (key and key[:30] in ptext[i] and re.search(r'^\s*'+re.escape(num)+r'\b',p,re.M)):
            hit=i+1; break
    if hit: pm[loc]=hit
print('headings',len(heads),'mapped',len(pm))
ix=[i for i,l in enumerate(L) if l.startswith('## Index')][-1]
missing=set(); n=0
def sub(m):
    global n
    loc=m.group(0); n+=1
    if loc in pm: return f'{loc} ({pm[loc]})'
    missing.add(loc); return loc
for i in range(ix,len(L)):
    if L[i].startswith('## ') and i>ix: break
    if '……' in L[i]: L[i]=re.sub(r'§\d+(?:\.\d+)?|App [A-F]',sub,L[i])
print('locators',n,'unmapped',sorted(missing)[:20],len(missing))
open(out,'w',encoding='utf-8').write('\n'.join(L)+'\n')