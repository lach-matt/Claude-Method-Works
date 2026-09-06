import pdfplumber, numpy as np
P='/mnt/user-data/outputs/the-lach-cylinder.pdf'
print("="*84)
print("  AUDIT 5 — WHITESPACE, measured with pdfplumber geometry")
print("="*84)
rows=[]
with pdfplumber.open(P) as pdf:
    H=pdf.pages[0].height; W=pdf.pages[0].width
    TOP=13*2.83; BOT=H-17*2.83          # frame edges in top-down coords
    CAP=BOT-TOP
    print("\n     page %.0f x %.0f pt   frame height %.0f pt"%(W,H,CAP))
    for i,pg in enumerate(pdf.pages):
        ch=pg.chars
        body=[c for c in ch if TOP-4 < c['top'] < BOT+4]
        if not body: rows.append((i+1,0.0,None,None,0)); continue
        top=min(c['top'] for c in body); bot=max(c['bottom'] for c in body)
        frac=(bot-top)/CAP
        rows.append((i+1,frac,round(top),round(bot),len(body)))
fr=[r[1] for r in rows if r[4]>50]
print("     pages : %d      median inked fraction : %.0f%%"%(len(rows),100*np.median(fr)))
print("     mean %.0f%%   min %.0f%%   max %.0f%%"%(100*np.mean(fr),100*min(fr),100*max(fr)))
print()
print("  PAGES WITH A GAP AT THE FOOT  (content ends well above the frame)")
print("  %6s%10s%12s%12s%10s"%("page","inked","last y","frame bot","chars"))
print("  "+"-"*52)
flag=[r for r in rows if r[4]>50 and r[1]<0.80]
for p,f,t,b,n in sorted(flag,key=lambda x:x[1]):
    print("  %6d%9.0f%%%12s%12.0f%10d"%(p,100*f,b,BOT,n))
print("\n     **pages under 80%% inked (excluding front matter) : %d**"%len(flag))
print("     under 60%%                                        : %d"%len([r for r in flag if r[1]<0.60]))
print("     front-matter pages, by design                    : %d"%len([r for r in rows if r[4]<=50]))