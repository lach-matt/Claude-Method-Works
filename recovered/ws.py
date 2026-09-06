from pypdf import PdfReader
import re
P='/mnt/user-data/outputs/the-lach-cylinder.pdf'
r=PdfReader(P)
H=841.89; W=595.28   # A4 in points
TOP=H-13*2.83; BOT=17*2.83   # frame from engine.py
CAP=TOP-BOT
print("="*82)
print("  AUDIT 5f — WHITESPACE   (measured from glyph positions, not line counts)")
print("="*82)
print("""
  For each page the vertical extent actually inked is measured, and compared
  with the frame height. **A page whose content stops far above the bottom is
  carrying whitespace a reader will see as a gap.**
""")
rows=[]
for i,pg in enumerate(r.pages):
    ys=[]
    def visit(text,cm,tm,fd,fs):
        if text.strip(): ys.append(tm[5])
    try: pg.extract_text(visitor_text=visit)
    except Exception: pass
    if not ys: rows.append((i+1,0.0,0,0)); continue
    ys=[y for y in ys if BOT-20<y<TOP+20]
    if not ys: rows.append((i+1,0.0,0,0)); continue
    top=max(ys); bot=min(ys)
    used=top-bot
    frac=used/CAP
    rows.append((i+1,frac,round(top),round(bot)))
short=[x for x in rows if x[1]<0.55]
print("  %6s%12s%12s%12s"%("page","inked","top y","bottom y"))
print("  "+"-"*44)
for p,f,t,b in rows:
    if f<0.55: print("  %6d%11.0f%%%12s%12s"%(p,100*f,t,b))
print("\n     pages measured                : %d"%len(rows))
print("     **under 55%% inked             : %d**"%len(short))
print("     under 35%%                     : %d"%len([x for x in short if x[1]<0.35]))
import numpy as np
fr=[x[1] for x in rows if x[1]>0]
print("     median inked fraction         : %.0f%%"%(100*np.median(fr)))
print("     minimum (excluding title)     : %.0f%% on page %d"%(100*min(x[1] for x in rows[2:]),
      min(rows[2:],key=lambda x:x[1])[0]))
print("="*82)
print("  ORPHANED HEADINGS — a heading in the last 12% of a page")
print("="*82)
bad=[]
for i,pg in enumerate(r.pages):
    items=[]
    def v2(text,cm,tm,fd,fs):
        if text.strip(): items.append((tm[5],text.strip(),fs))
    try: pg.extract_text(visitor_text=v2)
    except Exception: continue
    if not items: continue
    for y,t,fs in items:
        if fs and fs>=10.0 and y<BOT+0.12*CAP and len(t)>3:
            bad.append((i+1,t[:44],round(y)))
print()
if bad:
    for p,t,y in bad[:12]: print("     page %-4d y=%-5s %s"%(p,y,t))
    print("\n     **orphaned headings : %d**"%len(bad))
else:
    print("     **orphaned headings : none**")