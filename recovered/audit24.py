import re, json
from collections import Counter
md=open('/mnt/user-data/outputs/Transitions.md').read()
D=json.load(open('data.json')); E=json.load(open('data3.json'))
def flat(o,acc=None):
    if acc is None: acc=set()
    if isinstance(o,dict):
        for v in o.values(): flat(v,acc)
    elif isinstance(o,(list,tuple)):
        for v in o: flat(v,acc)
    elif isinstance(o,(int,float)):
        acc.add(str(o))
        if isinstance(o,int): acc.add(f'{o:,}')
        else:
            acc.add(f'{o:.1f}'); acc.add(f'{o:.2f}')
    elif isinstance(o,str): acc.add(o)
    return acc
known=flat(D)|flat(E)
# strip the bibliography and the equations appendix: those are citations and definitions
body=md.split('## Appendix B')[0]
body=re.sub(r'^### \d+\.\d+.*$','',body,flags=re.M)          # section headings
body=re.sub(r'\*\*\(\d+\)\*\*','',body)                       # equation numbers
lines=[l for l in body.split('\n') if not re.match(r'^\s*[-*] [A-Z][a-z]+, ',l)]
body='\n'.join(lines)
nums=re.findall(r'(?<![\w.§])(\d{1,3}(?:,\d{3})+|\d+\.\d+|\d{2,})(?![\w.])', body)
YEAR=lambda s: s.isdigit() and 1850<=int(s)<=2030 and len(s)==4
SEC =lambda s: re.fullmatch(r'\d+\.\d+',s) and float(s)<15
c=Counter(n for n in nums if not YEAR(n) and not SEC(n))
unb=[n for n in c if n not in known and n.replace(',','') not in known]
print('  AUDIT 24 -- INTERNAL DEBT, refined')
print('     excluded: bibliography, equation numbers, section numbers, publication years')
print()
print('     distinct numeric claims : %d' % len(c))
print('     backed by a dataset     : %d' % (len(c)-len(unb)))
print('     UNBACKED                : %d  (%.0f%%)' % (len(unb),100*len(unb)/len(c)))
print()
print('     every unbacked token, with context:')
for n in sorted(unb, key=lambda x:(-c[x],x)):
    i=body.find(n); ctx=body[max(0,i-60):i+len(n)+30].replace('\n',' ')
    ctx=re.sub(r'\s+',' ',ctx)
    print('        %-9s x%-2d %s' % (n,c[n],ctx))