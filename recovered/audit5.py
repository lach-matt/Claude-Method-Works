from pypdf import PdfReader
import re, os, subprocess
P='/mnt/user-data/outputs/the-lach-cylinder.pdf'
print("="*80)
print("  AUDIT 5 — THE ARTEFACT   (the built PDF, not the source)")
print("="*80)
r=PdfReader(P)
pages=len(r.pages)
txt=[p.extract_text() for p in r.pages]
all_t="\n".join(txt)
print("\n  5a  pages : %d      size : %.2f MB"%(pages,os.path.getsize(P)/1e6))
nulls=all_t.count(chr(0))
badpg=[i+1 for i,t in enumerate(txt) if chr(0) in t]
print("  5b  **missing glyphs (NULL) : %d**   pages affected : %s"%(nulls,badpg or "none"))
# any other replacement-ish artefacts
for ch,nm in [('\ufffd','U+FFFD replacement'),('\u25a1','white square'),('\u25af','white rectangle')]:
    n=all_t.count(ch)
    if n: print("      %s : %d"%(nm,n))
print("  5c  title page")
tp=[l.strip() for l in txt[0].split("\n") if l.strip()]
for l in tp: print("       ",l[:76])
print("  5d  running header on a sample of interior pages")
hdr=set()
for i in (8,30,60,90,115):
    if i<pages:
        first=txt[i].split("\n")[0].strip()
        hdr.add(first[:40])
print("       ",hdr)
print("  5e  figures rendered")
from PIL import Image
imgs=0; blanks=[]
for i,p in enumerate(r.pages):
    xo=p.get("/Resources",{}).get("/XObject",{})
    try: xo=xo.get_object()
    except Exception: xo={}
    for k,v in (xo or {}).items():
        try:
            o=v.get_object()
            if o.get("/Subtype")=="/Image": imgs+=1
        except Exception: pass
print("       image objects embedded : %d      source figure files : %d"%(imgs,
      len([f for f in os.listdir('/home/claude/book/fig') if f.endswith('.png')])))
print("  5f  the operator symbols actually present")
print("       ℛ : %d      ⅅ : %d"%(all_t.count('ℛ'),all_t.count('ⅅ')))
print("  5g  text extractable on every page")
empty=[i+1 for i,t in enumerate(txt) if len(t.strip())<20]
print("       pages with almost no extractable text : %s"%(empty or "none"))
print("  5h  last page is References")
print("       ",txt[-1].split("\n")[2][:70] if len(txt[-1].split("\n"))>2 else txt[-1][:70])
ok = (nulls==0 and not empty and imgs>=28)
print("\n  **AUDIT 5 : %s**"%("PASS" if ok else "FAIL"))