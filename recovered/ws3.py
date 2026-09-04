import pdfplumber, numpy as np
P='/mnt/user-data/outputs/the-lach-cylinder.pdf'
with pdfplumber.open(P) as pdf:
    H=pdf.pages[0].height
    TOP=13*2.83; BOT=H-17*2.83; CAP=BOT-TOP
    rows=[]
    for i,pg in enumerate(pdf.pages):
        body=[c for c in pg.chars if TOP-4 < c['top'] < BOT+4]
        if len(body)<50: rows.append((i+1,None,None,0,'')); continue
        t=min(c['top'] for c in body); b=max(c['bottom'] for c in body)
        # ignore the running header line (top ~ 26) when it exists
        hdr=[c for c in body if c['top']<34]
        t2=min([c['top'] for c in body if c['top']>=34] or [t])
        gap_top=(t2-TOP-22)/CAP    # 22pt allows for header+rule
        gap_bot=(BOT-b)/CAP
        first=''.join(c['text'] for c in sorted(body,key=lambda c:(c['top'],c['x0']))[:60])
        rows.append((i+1,gap_top,gap_bot,len(body),first))
print("="*86)
print("  AUDIT 5 — WHITESPACE, gaps at head and foot separated")
print("="*86)
gt=[r[1] for r in rows if r[1] is not None]
gb=[r[2] for r in rows if r[2] is not None]
print("\n     pages with body text : %d"%len(gt))
print("     head gap  median %.1f%%   max %.0f%%"%(100*np.median(gt),100*max(gt)))
print("     foot gap  median %.1f%%   max %.0f%%"%(100*np.median(gb),100*max(gb)))
print()
print("  GAP AT THE HEAD  > 15% of the frame")
print("  %6s%10s%s"%("page","gap","what starts the page"))
print("  "+"-"*80)
n1=0
for p,a,b,n,f in rows:
    if a is not None and a>0.15:
        n1+=1; print("  %6d%9.0f%%  %s"%(p,100*a,f[:58]))
print("     **%d pages**"%n1)
print()
print("  GAP AT THE FOOT  > 15% of the frame")
print("  %6s%10s%s"%("page","gap","what ends the page"))
print("  "+"-"*80)
n2=0
for p,a,b,n,f in rows:
    if b is not None and b>0.15:
        n2+=1; print("  %6d%9.0f%%  %s"%(p,100*b,f[:58]))
print("     **%d pages**"%n2)