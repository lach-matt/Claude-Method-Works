import re, os
from PIL import Image
import numpy as np
b=open('/home/claude/book/BOOK.md').read()
print("="*88)
print("  FIGURE AUDIT — every figure, against its caption and its file")
print("="*88)
figs=[(m.group(1),m.group(2)) for m in re.finditer(r'!\[(Figure [\d.]+)\]\(([^)]+)\)',b)]
caps={}
for m in re.finditer(r'\*\*(Figure [\d.]+)\.\*\* ([^\n]+(?:\n(?!\n)[^\n]+)*)',b):
    caps[m.group(1)]=re.sub(r'\s+',' ',m.group(2))
print("\n  %-13s%-24s%11s%9s%8s%8s%s"%("figure","file","px","ink%","gray","cap w","chapter"))
print("  "+"-"*104)
rows=[]
for name,path in figs:
    p='/home/claude/book/'+path
    im=Image.open(p).convert('L')
    a=np.asarray(im,dtype=float)
    ink=float((a<245).mean())
    gray=float(a.mean())
    cap=caps.get(name,'')
    seg=b[:b.index('!['+name)]
    hh=re.findall(r'\n# (\d+)\. ',seg)
    ch=hh[-1] if hh else '?'
    rows.append((name,path,im.size,ink,gray,len(cap.split()),ch,cap))
    print("  %-13s%-24s%11s%8.1f%%%9.0f%8d%8s"%(name,os.path.basename(path),
          "%dx%d"%im.size,100*ink,gray,len(cap.split()),ch))
print()
print("  CHECKS")
noc=[r[0] for r in rows if r[5]==0]
print("     figures without a caption        : %s"%(noc or "none"))
blank=[r[0] for r in rows if r[3]<0.02]
print("     near-blank images (<2%% ink)      : %s"%(blank or "none"))
dark=[r[0] for r in rows if r[4]<120]
print("     unusually dark (mean < 120)      : %s"%(dark or "none"))
small=[(r[0],r[2]) for r in rows if min(r[2])<400]
print("     low resolution (<400 px a side)  : %s"%(small or "none"))
thin=[(r[0],r[5]) for r in rows if 0<r[5]<12]
print("     captions under 12 words         : %s"%(thin or "none"))
seen={}
import hashlib
for name,path,*_ in rows:
    h=hashlib.md5(open('/home/claude/book/'+path,'rb').read()).hexdigest()
    seen.setdefault(h,[]).append(name)
dupes={k:v for k,v in seen.items() if len(v)>1}
print("     duplicate image files            : %s"%(list(dupes.values()) or "none"))
# numbering: figures should be numbered by the chapter they sit in
bad=[(r[0],r[6]) for r in rows if r[0].split()[1].split('.')[0]!=r[6]]
print("     **figure number vs chapter**     : %d mismatched"%len(bad))
for n,c in bad: print("        %s sits in chapter %s"%(n,c))
orphan=[c for c in caps if c not in [r[0] for r in rows]]
print("     captions with no image           : %s"%(orphan or "none"))
files=set(os.listdir('/home/claude/book/fig'))
used={os.path.basename(r[1]) for r in rows}
print("     unused files in fig/             : %s"%(sorted(files-used) or "none"))