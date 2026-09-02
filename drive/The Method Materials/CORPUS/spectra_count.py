# Spectra Compendium: counts from its own channel table. Columns: species | series | n | levels | interior | bracket | n* range | δ | σ | fits | limit
import re,sys,collections
rows=[l for l in open(sys.argv[1] if len(sys.argv)>1 else 'The_Method_1_6___Spectra_Compendium-2.md',encoding='utf-8') if l.startswith('| ') and re.search(r'\| [+-]\d\.\d+(?:e-\d+)? \|',l)]
sp=set(); el=set(); lev=0; inter=0; two=0
for l in rows:
    c=[x.strip() for x in l.strip().strip('|').split('|')]
    s=c[0].replace(' *',''); sp.add(s); el.add(s.split()[0]); lev+=int(c[3]); inter+=int(c[4])
    if '*' in c[0] or int(c[3])==2: two+=1
print(f'{len(rows)} channel rows — {len(rows)-two} series of three or more members and {two} two-member channels — across {len(el)} elements and {len(sp)} species; {lev:,} levels, {inter:,} interior cells.')
# bracket column (ruling 26, register 1763): m/k sums, no-triple, untested
bp=bt=mk=nt=ut=0
for l in rows:
    c=[x.strip() for x in l.strip().strip('|').split('|')]
    m=re.match(r'(\d+)/(\d+)$',c[5])
    if m: mk+=1; bp+=int(m.group(1)); bt+=int(m.group(2))
    elif c[5]=='no-triple': nt+=1
    elif c[5]=='untested': ut+=1
print(f'bracket: {mk} rows tested, {bp} of {bt} cells pass; {nt} no-triple rows; {ut} untested rows.')
