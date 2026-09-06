import re,json,sys,hashlib
src=open('BUILD79_compendia.md',encoding='utf-8').read()
L=src.split('\n'); out=L[:]
table=json.load(open('handle_table.json'))
TOK=re.compile(r'(?<![\w/`])(A|S|F|G|L|T|E|B|K|M|W|EM|C|I|P|Q|LS|3B)\.([a-z][a-z0-9_]{1,12})\b(?!`)')
VOL=[(13435,17002),(17246,18407),(18408,20503),(20504,21384)]
BIB=(16815,17002)
HOLD={14903}                       # L.c1..L.c8 — set-builder line, ruling needed
changes=[]
# --- D-1 family headings
for ln,old,new in [(13577+0,None,None)]: pass
heads={14035:('18','21'),14427:('41','68'),15547:('24','25'),16009:('7','10')}
for ln,(o,n) in heads.items():
    l=out[ln-1]; assert f'— {o} objects' in l, (ln,l)
    out[ln-1]=l.replace(f'— {o} objects',f'— {n} objects'); changes.append(('D-1',ln))
# --- D-2 count line
l=out[13436]; assert '**265 objects · 18 roots · 263 settled · 2 unfinished.**' in l
out[13436]=l.replace('recounted from this file on 2026-08-24 (register 1739)','recounted from this file on 2026-08-29').replace('**265 objects · 18 roots · 263 settled · 2 unfinished.**','**299 objects · 18 roots · 297 settled · 2 unfinished.**'); changes.append(('D-2',13437))
# --- D-4 orphan lines: delete line + following blank
for ln in sorted([13717,13829,13991],reverse=True):
    assert re.fullmatch(r'[A-Z]+\.[a-z0-9_]+',out[ln-1]) and out[ln]=='' , ln
    del out[ln-1:ln+1]; changes.append(('D-4',ln))
# --- D-3 handles (on the shifted text; locate by content, per entry)
def entry_bounds(i):
    a=i
    while a>0 and not out[a].startswith('#'): a-=1
    b=i+1
    while b<len(out) and not out[b].startswith('#'): b+=1
    return a,b
held=[]; conv=[]
for i in range(len(out)):
    ln=i+1
    if not any(a<=ln<=b for a,b in VOL) or BIB[0]<=ln<=BIB[1]: continue
    if not TOK.search(out[i]): continue
    if out[i].strip() in ('| 1669 | Newton | `B.newton` |',): continue
    a,b=entry_bounds(i)
    if any(h in out[i] for h in ['L.c1..L.c8']): held.append(ln); continue
    def rep(m):
        h=m.group(0); t,p=table[h]
        before='\n'.join(out[a:i])+'\n'+out[i][:m.start()]
        first = t not in before
        conv.append((ln,h,t,p if first else None))
        return t+(f' ({p})' if (first and p) else '')
    out[i]=TOK.sub(rep,out[i])
new='\n'.join(out)
open('BUILD80_compendia.md','w',encoding='utf-8',newline='').write(new)
print('conversions',len(conv)); 
for c in conv: print('  ',c)
print('HELD',held)
print('changed-line groups',changes)
b=new.encode(); print('BUILD80',len(b),hashlib.md5(b).hexdigest(),b.count(b'\n'))