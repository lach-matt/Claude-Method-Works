import re
from itertools import product
from collections import defaultdict, Counter
NUM=re.compile(r'(?<![\w.])(\d{1,3}(?:,\d{3})+|\d+\.\d+%?|\d+%)(?![\w])')
def classify(par):
    p=par.lower()
    if re.search(r'cm⁻¹|cm-1|\bev\b|\bnm\b|wavelength|energy|level', p): q='measurement'
    elif re.search(r'e\(|defect|failur|violation|missing|absent', p):     q='defect'
    elif '%' in par and re.search(r'densit|fraction|realis', p):          q='density'
    elif re.search(r'rate|per cent of|share', p):                         q='rate'
    elif re.search(r'≤|≥|bound|cap\b|ceiling|envelope', p):               q='bound'
    else:                                                                 q='count'
    METH=re.search(r'comput|enumerat|exhaustiv|sampl|verif|recomput|by code|stated code|test|check|prov', p)
    INP =re.search(r'\bλ\b|cells|channels|pairs|caps|terms|fibre|§\d|all \d|over \d', p)
    if METH and INP: d=2
    elif METH:       d=1
    else:            d=0
    if re.search(r'printed|listed|table|the eight|the seven|enumerated', p): i=2
    elif INP:                                                                i=1
    else:                                                                    i=0
    if re.search(r'four caps|at caps|cap-stab|under variation|every cap', p): v=2
    elif re.search(r'recomput|reproduc|verified|exhaustiv', p):               v=1
    else:                                                                     v=0
    return q,(d,i,v)
def build(src):
    pop=defaultdict(list)
    for par in re.split(r'\n\s*\n', src):
        n=NUM.findall(par)
        if not n: continue
        q,c=classify(par)
        for _ in n: pop[q].append(c)
    return pop
def R(cells):
    D=3; vals=[sorted({c[i] for c in cells}) for i in range(D)]
    def env(i,j):
        m={}
        for c in cells: m[c[j]]=max(m.get(c[j],-99),c[i])
        b=-99;o={}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(D) for j in range(D) if i!=j}
    return {x for x in product(*vals)
            if all(x[i]<=phi[(i,j)][x[j]] for i in range(D) for j in range(D) if i!=j)}