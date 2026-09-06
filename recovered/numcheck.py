import re,sys
ent=open(sys.argv[1],encoding='utf-8').read()
main=open('The_Method_1_6-2.md',encoding='utf-8').read().split('\n')
ranges=[tuple(map(int,r.split('-'))) for r in sys.argv[2:]]
src='\n'.join('\n'.join(main[a-1:b]) for a,b in ranges)
def nums(s): return set(re.findall(r'(?<![\w.])\d[\d,]*(?:\.\d+)?(?![\w])',s))
en=nums(ent); sn=nums(src)
yrs=lambda x: re.fullmatch(r'1[5-9]\d\d|20[0-2]\d',x)
miss=[x for x in sorted(en,key=lambda z:(len(z),z)) if x not in sn and not yrs(x) and not re.fullmatch(r'\d{1,2}',x)]
print('numbers in entry not in source section(s):', miss)
small=[x for x in sorted(en) if x not in sn and re.fullmatch(r'\d{1,2}',x) and not yrs(x)]
print('small numbers (1-2 digit) in entry not in source:', small)
print('source chars', len(src), 'entry chars', len(ent))