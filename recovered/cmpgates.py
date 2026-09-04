import re,sys
def blocks(p):
    d={};cur=None
    for ln in open(p,errors='replace'):
        m=re.match(r'### GATE (\d+)$',ln.strip())
        if m: cur=int(m.group(1)); d.setdefault(cur,[]); continue
        if cur is not None: d[cur].append(ln.rstrip())
    return d
a=blocks('GATES-33-OPEN.log'); b=blocks('pack33/GATES-1-53-SESSION-33.log')
lo,hi=int(sys.argv[1]),int(sys.argv[2])
for g in range(lo,hi+1):
    if g not in a: print(g,'MISSING'); continue
    if g not in b: print(g,'NOREF',a[g][:3]); continue
    print(g,'MATCH' if a[g]==b[g] else 'DIFF', '' if a[g]==b[g] else (a[g][-3:],b[g][-3:]))