import re,glob,collections
rng=re.compile(r'\b[Rr]egisters?\s+((?:\d{3,4}(?:\s*[–\-]\s*\d{3,4})?)(?:\s*(?:,|and|/|;)\s*\d{3,4}(?:\s*[–\-]\s*\d{3,4})?)*)')
def nums(s):
    out=set()
    for part in re.split(r'\s*(?:,|and|/|;)\s*',s):
        m=re.match(r'(\d{3,4})\s*[–\-]\s*(\d{3,4})$',part.strip())
        if m:
            a,b=int(m.group(1)),int(m.group(2))
            if 165<=a<=b<=1731 and b-a<200: out.update(range(a,b+1))
        elif part.strip().isdigit():
            n=int(part);
            if 165<=n<=1731: out.add(n)
    return out
def cites(text):
    c=collections.Counter()
    for m in rng.finditer(text):
        for n in nums(m.group(1)): c[n]+=1
    for m in re.finditer(r'\*R (\d{3,4})(?:[,–\- ]+(\d{3,4}))?\*',text):  # compendium source *R nnn*
        for g in m.groups():
            if g and 165<=int(g)<=1731: c[int(g)]+=1
    return c
if __name__=='__main__':
    R=open('The_Method_1_6___The_Register-2.md',encoding='utf-8').read()
    # entries citing entries: only bodies after "### N"
    ent=re.split(r'\n### (\d+(?:, \d+)*)\n',R)
    byent=collections.Counter()
    for i in range(1,len(ent),2):
        ids={int(x) for x in ent[i].split(', ')}
        for n,k in cites(ent[i+1]).items():
            if n not in ids: byent[n]+=k
    main=open('The_Method_1_6-2.md',encoding='utf-8').read()
    bymain=cites(main)
    comp=collections.Counter()
    for f in glob.glob('The_Method_1_6___*Compendium-2.md')+glob.glob('*Index_of_Indices-2.md')+['THE-LOWDIN-SOLUTION-2.md','The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md']:
        comp+=cites(open(f,encoding='utf-8').read())
    print("entries cited by other entries:",len(byent))
    print("top 12 by entry-citations:",byent.most_common(12))
    print("entries cited in main:",len(bymain),"| in companions:",len(comp),"| main∪companions:",len(set(bymain)|set(comp)))
    print("top main:",bymain.most_common(10))
    allc=byent+bymain+comp
    print("cited anywhere:",len(allc))
    # check all cited ids exist
    heads=set()
    for i in range(1,len(ent),2): heads.update(int(x) for x in ent[i].split(', '))
    missing=sorted(n for n in allc if n not in heads); print("cited but no entry:",missing[:40],len(missing))