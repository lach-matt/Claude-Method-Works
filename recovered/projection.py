"""
PROJECTION, strict. Three enumerations of the same list, produced by three
different mechanisms, compared field by field in order.

  A  source markdown headings          (what was written)
  B  PDF outline / bookmarks           (written by hyperref from \section)
  C  typeset table of contents         (written by \tableofcontents from the .toc file)

B and C are independent of each other: different LaTeX machinery, different pass,
different failure modes. Comparing C against A alone would check a derived list
against its own generating rule, which is the defect this audit exists to catch.
"""
import re, subprocess, unicodedata
from pypdf import PdfReader

def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('\u2014','—').replace('\u2013','–').replace('\u2019',"'")
    s = re.sub(r'\s+',' ', s).strip()
    return s

# ---- A : source ---------------------------------------------------------
A=[]
for line in open('paper.md'):
    m=re.match(r'^(#{1,3}) (.+?)\s*$', line)
    if m: A.append((len(m.group(1)), norm(m.group(2))))

# ---- B : PDF outline ----------------------------------------------------
rd=PdfReader('Genome_Not_Closed_Index.pdf')
B=[]
def walk(items, depth=1):
    for it in items:
        if isinstance(it, list): walk(it, depth+1)
        else: B.append((depth, norm(it.title)))
walk(rd.outline)

# ---- C : typeset TOC ----------------------------------------------------
txt = subprocess.run(['pdftotext','-layout','-f','1','-l','2',
                      'Genome_Not_Closed_Index.pdf','-'],
                     capture_output=True, text=True).stdout
C=[]
for line in txt.split('\n'):
    m=re.match(r'^\s*(\d+(?:\.\d+)*)\s+(.+?)\s*\.{2,}\s*\d+\s*$', line)
    if m:
        num, title = m.group(1), norm(m.group(2))
        C.append((num.count('.')+1, title, num))

# ---- strip the numbering hyperref/TOC prepend, to compare titles ---------
def strip_num(t):
    return norm(re.sub(r'^\d+(\.\d+)*\s+', '', t))
Bt=[(d, strip_num(t)) for d,t in B]
Ct=[(d, t) for d,t,_ in C]
At=[(d-1, t) for d,t in A]        # markdown '#' == LaTeX section == depth 1

print(f'A  source headings      : {len(At)}')
print(f'B  PDF outline entries  : {len(Bt)}')
print(f'C  typeset TOC entries  : {len(Ct)}')
print()

fails=[]
# ---- length -------------------------------------------------------------
if not (len(At)==len(Bt)==len(Ct)):
    fails.append(f'LENGTH  A={len(At)} B={len(Bt)} C={len(Ct)}')

# ---- field by field, in order, exact ------------------------------------
n=max(len(At),len(Bt),len(Ct))
print(f'{"i":>3}  {"d":>1} {"A source":<52}{"B outline":<52}{"C toc":<40} ok')
print('-'*152)
for i in range(n):
    a=At[i] if i<len(At) else (None,'<absent>')
    b=Bt[i] if i<len(Bt) else (None,'<absent>')
    c=Ct[i] if i<len(Ct) else (None,'<absent>')
    same_title = a[1]==b[1]==c[1]
    same_depth = a[0]==b[0]==c[0]
    ok = same_title and same_depth
    if not ok:
        fails.append(f'ROW {i}: depths {a[0]}/{b[0]}/{c[0]}  titles '
                     f'A={a[1]!r} B={b[1]!r} C={c[1]!r}')
    print(f'{i:>3}  {str(a[0]):>1} {a[1][:50]:<52}{b[1][:50]:<52}{c[1][:38]:<40} '
          f'{"." if ok else "MISMATCH"}')

# ---- numbering monotone and contiguous ----------------------------------
nums=[tuple(int(x) for x in num.split('.')) for _,_,num in C]
mono = all(nums[i] < nums[i+1] for i in range(len(nums)-1))
tops=[t[0] for t in nums if len(t)==1]
contig = tops==list(range(1,len(tops)+1))
if not mono: fails.append(f'NUMBERING not ascending: {nums}')
if not contig: fails.append(f'TOP-LEVEL numbering not contiguous from 1: {tops}')

print('-'*152)
print(f'numbering strictly ascending : {mono}')
print(f'top-level contiguous from 1  : {contig}  ({len(tops)} sections)')
print()
if fails:
    print(f'PROJECTION  FAIL  — {len(fails)} discrepancies')
    for f in fails: print('   '+f)
else:
    print(f'PROJECTION  PASS  — {n} entries match field by field across three '
          f'independently generated enumerations')