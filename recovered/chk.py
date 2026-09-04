import re,glob,collections
files=['The_Method_1_6-2.md','The_Method_1_6___The_Register-2.md']+sorted(glob.glob('The_Method_1_6___*Compendium-2.md'))+['The_Method_1_6___The_Index_of_Indices-2.md','THE-LOWDIN-SOLUTION-2.md','The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md']
ph=re.compile(r'\[(new|TBD|TODO|placeholder)')
for f in files:
    b=open(f,'rb').read(); t=b.decode('utf-8')
    print(f"{f[:45]:45s} words {len(t.split()):>7} CRLF {b.count(b'\r')} mojibake {len(re.findall('Ã|â€',t))} placeholders {len(ph.findall(t))}")
M=open('The_Method_1_6-2.md',encoding='utf-8').read()
secs=re.findall(r'^#{2,4} (\d+(?:\.\d+)*) ',M,re.M)
print(">2x:",[s for s,c in collections.Counter(secs).items() if c>2])
R=open('The_Method_1_6___The_Register-2.md',encoding='utf-8').read()
ids=re.findall(r'^### (\d+(?:, \d+)*)$',R,re.M); nums=[int(x) for i in ids for x in i.split(', ')]
print("register headings",len(ids),"distinct",len(set(nums)),"max",max(nums),"dupes",[n for n,c in collections.Counter(nums).items() if c>1])