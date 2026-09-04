import sys, re, json, itertools
sys.path.insert(0,'/home/claude/method')
from collections import Counter
print('  AUDIT 23 -- EXTERNAL, MECHANICAL')
print('  compare the term-counting subroutine against published LS term tables')
print()
def terms(l,k):
    orbs=[(ml,ms) for ml in range(-l,l+1) for ms in (1,-1)]
    cnt=Counter()
    for combo in itertools.combinations(range(len(orbs)),k):
        ML=sum(orbs[i][0] for i in combo); MS2=sum(orbs[i][1] for i in combo)
        cnt[(2*ML,MS2)]+=1
    out=[]
    while cnt:
        L2=max(a for (a,b) in cnt); S2=max(b for (a,b) in cnt if a==L2)
        for a in range(-L2,L2+1,2):
            for b in range(-S2,S2+1,2):
                if (a,b) in cnt:
                    cnt[(a,b)]-=1
                    if cnt[(a,b)]==0: del cnt[(a,b)]
        out.append((S2,L2))
    return out
LET='SPDFGHIKLMNO'
def sym(S2,L2): return '%d%s' % (S2+1, LET[L2//2])
# published LS terms (Condon-Shortley / any standard atomic structure text)
PUB={('p',2):['1S','1D','3P'],
     ('p',3):['2P','2D','4S'],
     ('p',4):['1S','1D','3P'],
     ('d',2):['1S','1D','1G','3P','3F'],
     ('d',3):['2P','2D','2D','2F','2G','2H','4P','4F'],
     ('f',2):['1S','1D','1G','1I','3P','3F','3H'],
     ('s',1):['2S'],('p',1):['2P'],('d',1):['2D'],('f',1):['2F']}
L={'s':0,'p':1,'d':2,'f':3}
ok=0; tot=0
print('  %-8s %-34s %-34s %s' % ('shell','computed','published','match'))
for (sh,k),pub in sorted(PUB.items()):
    got=sorted(sym(S2,L2) for S2,L2 in terms(L[sh],k))
    exp=sorted(pub); tot+=1
    m = got==exp
    ok+=m
    print('  %-8s %-34s %-34s %s' % ('%s^%d'%(sh,k), ' '.join(got), ' '.join(exp), 'YES' if m else 'NO'))
print()
print('     %d of %d published term tables reproduced' % (ok,tot))
print()
# also check total microstate counts = C(4l+2, k)
from math import comb
print('  microstate totals (must equal C(4l+2,k)):')
bad=0
for sh in 'spdf':
    for k in range(1,min(4*L[sh]+3,7)):
        n=sum((S2+1)*(L2+1) for S2,L2 in terms(L[sh],k))
        c=comb(4*L[sh]+2,k)
        if n!=c: bad+=1; print('     MISMATCH %s^%d: %d vs %d' % (sh,k,n,c))
print('     mismatches: %d' % bad)
print()
print('  AUDIT 24 -- INTERNAL, DEBT: numeric claims with no dataset behind them')
md=open('/mnt/user-data/outputs/Transitions.md').read()
D=json.load(open('data.json')); E=json.load(open('data3.json'))
def flat(o,acc=None):
    if acc is None: acc=set()
    if isinstance(o,dict):
        for v in o.values(): flat(v,acc)
    elif isinstance(o,(list,tuple)):
        for v in o: flat(v,acc)
    elif isinstance(o,(int,float)):
        acc.add(str(o)); acc.add(f'{o:,}' if isinstance(o,int) else str(o))
    elif isinstance(o,str):
        acc.add(o)
    return acc
known=flat(D)|flat(E)
nums=re.findall(r'(?<![\w.])(\d{1,3}(?:,\d{3})+|\d+\.\d+|\d{2,})(?![\w.])', md)
c=Counter(nums)
unbacked=[n for n in c if n not in known and n.replace(',','') not in known]
print('     distinct numeric tokens in the paper : %d' % len(c))
print('     matched to a dataset value           : %d' % (len(c)-len(unbacked)))
print('     UNBACKED                             : %d  (%.0f%%)' % (len(unbacked),100*len(unbacked)/len(c)))
print()
print('     a sample of unbacked tokens (may be citations, years, page refs):')
for n in sorted(unbacked, key=lambda x:-c[x])[:18]:
    i=md.find(n); ctx=md[max(0,i-45):i+len(n)+25].replace('\n',' ')
    print('        %-10s x%-2d  ...%s...' % (n,c[n],ctx))