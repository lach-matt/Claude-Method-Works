import pdfplumber, numpy as np
P='/mnt/user-data/outputs/the-lach-cylinder.pdf'
with pdfplumber.open(P) as pdf:
    H=pdf.pages[0].height
    TOP=13*2.83; BOT=H-17*2.83; CAP=BOT-TOP
    rows=[]
    for i,pg in enumerate(pdf.pages):
        body=[c for c in pg.chars if TOP-4 < c['top'] < BOT+4]
        tops=[c['top'] for c in body if c['top']>=34]
        bots=[c['bottom'] for c in body]
        for im in pg.images:                      # images count as ink
            tops.append(im['top']); bots.append(im['bottom'])
        if len(body)<50 and not pg.images:
            rows.append((i+1,None,None,0,'')); continue
        t=min(tops) if tops else TOP; b=max(bots) if bots else BOT
        gt=max(0.0,(t-TOP-22)/CAP); gb=max(0.0,(BOT-b)/CAP)
        first=''.join(c['text'] for c in sorted(body,key=lambda c:(c['top'],c['x0']))[:60])
        rows.append((i+1,gt,gb,len(body),first))
print("="*86)
print("  AUDIT 5 — WHITESPACE, with figures counted as ink")
print("="*86)
gt=[r[1] for r in rows if r[1] is not None]; gb=[r[2] for r in rows if r[2] is not None]
print("\n     pages measured : %d"%len(gt))
print("     head gap : median %.1f%%   over 15%% : %d"%(100*np.median(gt),len([x for x in gt if x>0.15])))
print("     foot gap : median %.1f%%   over 15%% : %d"%(100*np.median(gb),len([x for x in gb if x>0.15])))
print()
print("  HEAD GAPS > 15%")
n=0
for p,a,b,c,f in rows:
    if a is not None and a>0.15: n+=1; print("  %6d%9.0f%%  %s"%(p,100*a,f[:56]))
print("     **%d**"%n)
print()
print("  FOOT GAPS > 15%   (the real gaps)")
n=0
for p,a,b,c,f in rows:
    if b is not None and b>0.15: n+=1; print("  %6d%9.0f%%  %s"%(p,100*b,f[:56]))
print("     **%d**"%n)
print()
print("     worst-case interior gap : %.0f%% on page %d"%(
    100*max(x[2] for x in rows if x[2] is not None and x[0] not in (1,2,122,125)),
    max([x for x in rows if x[2] is not None and x[0] not in (1,2,122,125)],key=lambda x:x[2])[0]))