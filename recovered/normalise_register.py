import re
src=open('REGISTER_MERGED.md').read()
L=src.split('\n')
heads=[i for i,l in enumerate(L) if re.match(r'^### \d',l)]

KEEP=re.compile(r'[._()/`0-9§]|[^\x00-\x7f]')          # identifiers, code, symbols, non-ASCII: never recased
ELEM=re.compile(r'^[A-Z][a-z]?$')                        # element symbols / single letters
def upcase(h):
    out=[]
    for tok in re.split(r'(\s+)',h):
        if not tok or tok.isspace() or KEEP.search(tok) or ELEM.match(tok.strip("',;:—-")): out.append(tok)
        else: out.append(tok.upper())
    return ''.join(out)

TOK=re.compile(r'(\*\*.+?\*\*|(?<!\*)\*(?!\*).+?(?<!\*)\*(?!\*))',re.S)
def italicise(par):
    if par.startswith(('|','>','    ','- ','1.','!','#')) or par.strip().startswith('```'): return par   # tables, quotes, code, lists: leave
    parts=TOK.split(par); out=[]
    for p in parts:
        if not p: continue
        if p.startswith('*'): out.append(p); continue
        core=p.strip()
        if not core: out.append(p); continue
        lead=p[:len(p)-len(p.lstrip())]; trail=p[len(p.rstrip()):]
        out.append(f'{lead}*{core}*{trail}')
    s=''.join(out)
    s=re.sub(r'\*\*\*(?!\*)',r'* **',s)     # italic-run closing directly into bold: separate
    s=re.sub(r'(?<!\*)\*\*\*',r'** *',s)
    return s

stats={'A':0,'B':0,'C':0,'cited':0}
for k,i in enumerate(heads):
    end=heads[k+1] if k+1<len(heads) else len(L)
    if '· **cited**' in L[i]: L[i]=L[i].replace(' · **cited**',''); stats['cited']+=1
    n=re.match(r'^### (\d+)',L[i]).group(1)
    if n=='1725': continue
    body='\n'.join(L[i+1:end]).strip('\n')
    pars=[p for p in re.split(r'\n\n+',body)]
    if not pars or not pars[0].strip(): continue
    first=pars[0]
    mm=re.match(r'\*\*(.+?)\*\*\s*(.*)',first,flags=re.S)
    if mm:
        head,rest=mm.group(1),mm.group(2)
        stats['B' if head!=upcase(head) else 'C']+=1
    else:
        # split off first sentence as headline
        sm=re.match(r'(.+?[.!?])(\s+|$)(.*)',first,flags=re.S)
        if sm: head,rest=sm.group(1),sm.group(3)
        else: head,rest=first,''
        head=head.strip().strip('*')
        if not head.endswith(('.', '!', '?')): head+='.'
        stats['A']+=1
    newfirst='**'+upcase(head)+'**'+(' '+italicise(rest.strip()) if rest.strip() else '')
    pars=[newfirst]+[italicise(p) for p in pars[1:]]
    L[i+1:end]=['']+'\n\n'.join(pars).split('\n')+['']
    heads=[j for j,l in enumerate(L) if re.match(r'^### \d',l)]  # recompute after splice
m='\n'.join(L)

entry='''### 1725

**THE RECORD NORMALISED TO ITS OWN SETTLED FORM — 1,517 ENTRIES, ONE HEADLINE AND ONE BODY EACH, AND THE EVOLUTION KEPT BY THIS ENTRY.** *The register's form evolved as the register did: entries 165–223 were plain prose with no headline; 224 introduced a bold sentence-case headline; the italic body followed at 419; the capitalised headline settled at 791 and was universal from 1434. Five forms on one page, and the "cited" tag on headings was used only to entry 800 and then dropped for the load-bearing table. Ruled: every entry brought to the settled form — capitalised headline, italic body, identifiers and symbols kept as written — and the heading tags removed. Nothing in any entry's content was changed; where an early entry had no headline, its first sentence is the headline. The prior states are preserved in* The Register-1 *(the file this was built from), which is the witness for this correction. The evolution is not erased by being made uniform; it is recorded here, once, as the register records every correction — both states kept, the later one on the page.* *(a correction; a new protocol: a form change is a register entry.)*
'''
m=m.rstrip('\n')+'\n\n'+entry
m=m.replace('**1517 entries, 165 to 1724.**','**1518 entries, 165 to 1725.**')
m=m.replace('| **a correction** | 369 |','| **a correction** | 370 |').replace('| **a new protocol** | 66 |','| **a new protocol** | 67 |')
old='**An entry is cited by a chapter'
m=m.replace(old,'**Every entry has one form: a capitalised headline, then the body in italics** (entry 1725 records how the form was reached).\n\n'+old,1)
open('REGISTER_NORM.md','w').write(m)
print(stats, 'entries now', len(re.findall(r'^### \d+',m,flags=re.M)))
