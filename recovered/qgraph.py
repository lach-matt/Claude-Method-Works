# qgraph.py — walk the Mathematical Compendium's "depends on" lines; reproduces register 1749.
import re,sys
s=open('The_Method_1_6___Mathematical_Compendium-2.md',encoding='utf-8').read(); dep={}
for e in re.split(r'\n(?=### `)',s):
    m=re.match(r'### `([^`]+)`',e)
    if not m: continue
    d=re.search(r'depends on (.*?)·',e); dep[m.group(1)]=re.findall(r'`([A-Z0-9]+\.[A-Za-z0-9]+)`',d.group(1)) if d else []
def desc(roots):
    out=set(roots); st=list(roots)
    while st:
        x=st.pop()
        for k,d in dep.items():
            if x in d and k not in out: out.add(k); st.append(k)
    return out
seeds=sys.argv[1:] or ['Q.exch','Q.delta']
full=desc(seeds); fin=desc(['Q.final'])
print('seeds+descendants',len(full),sorted(full)); print('via Q.final',len(fin&full)); print('not via Q.final',sorted(full-fin))