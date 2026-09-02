# crop_titles.py — remove the pre-V16 title band from the fourteen plots named in the working record.
# Crops from the first blank band below the first ink row; measures on columns 15% in to skip a full-height y-label.
from PIL import Image; import numpy as np, shutil, os, sys
figs=['6.1','6.2','7.1','8.2','10.1','15.1','19.1','23.1','23.2','24.1','24.2','24.3','25.1','26.1']
os.makedirs('figures-pre-crop',exist_ok=True)
for f in figs:
    p=f'figures/figure-{f}.png'; shutil.copy(p,f'figures-pre-crop/figure-{f}.png')
    im=Image.open(p); a=np.array(im.convert('L')); H,W=a.shape
    ink=(a[:,int(W*0.15):]<200).sum(axis=1); rows=np.where(ink>0)[0]; y=rows[0]
    while y<H and not (ink[y:y+6]==0).all(): y+=1
    assert y-rows[0] < 0.12*H, f
    im.crop((0,y,W,H)).save(p); print(f,'cropped at',y)
