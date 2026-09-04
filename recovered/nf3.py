import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from math import comb, log2
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,
  'axes.edgecolor':'#333333','axes.linewidth':0.8,'axes.labelcolor':'#222222',
  'xtick.color':'#333333','ytick.color':'#333333','axes.spines.top':False,
  'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})
INK='#1a1a1a'; ACC='#8c2d19'; MID='#5a7d9a'; LIGHT='#b8b8b8'; GOOD='#3d6b47'
OUT='/home/claude/book/fig/'
R=109737.3

# ---------- F24  slack as description length ----------
rows=[('periodic table\n18-column',126,36),('calendar',372,7),
      ('subnet with a hole',256,8),('Janet left-step',120,0),('Λ',976,0)]
fig,ax=plt.subplots(1,2,figsize=(10.4,4.3))
names=[r[0] for r in rows]
bits=[log2(comb(r[1],r[2])) if r[2]>0 else 0.0 for r in rows]
cols=[ACC if b>0 else GOOD for b in bits]
y=np.arange(len(rows))
ax[0].barh(y,bits,0.6,color=cols,edgecolor='white',linewidth=0.6)
ax[0].set_yticks(y); ax[0].set_yticklabels(names,fontsize=8.5)
ax[0].invert_yaxis()
for i,b in enumerate(bits):
    ax[0].text(b+2 if b>0 else 2,i,f'{b:.1f} bits' if b>0 else 'zero bits',
               va='center',fontsize=8.5,color=INK if b>0 else GOOD)
ax[0].set_xlim(0,128)
ax[0].set_xlabel('$E_{bits} = \\log_2 C(|\\mathcal{R}(X)|,\\, E)$')
ax[0].set_title('what an index costs beyond its own coordinates',fontsize=10,color=INK,loc='left')
T=lambda v: R/v**2
def we(v,h=1):
    a,m,b=T(v-h),T(v),T(v+h); return abs(b-a),abs(m-(a+b)/2)
nus=np.arange(3,90)
lv=[log2(we(v)[0]/we(v)[1]) for v in nus]
ax[1].plot(nus,lv,color=MID,lw=1.8)
ax[1].axhline(1,color=INK,ls='--',lw=1.2)
ax[1].text(86,1.12,'one bit — the floor',ha='right',fontsize=8.5,color=INK)
ax[1].plot([2],[log2(32/11)],marker='o',color=ACC,ms=7)
ax[1].annotate('Rydberg floor  $\\log_2(32/11)=1.54$',(2,log2(32/11)),
    xytext=(11,1.9),fontsize=8.5,color=ACC,arrowprops=dict(arrowstyle='-|>',color=ACC,lw=1.0))
ax[1].set_xlabel('ν'); ax[1].set_ylabel('$\\log_2 V$ — bits of precision surrendered')
ax[1].set_ylim(0,7)
ax[1].set_title('a guarantee never costs less than one bit',fontsize=10,color=INK,loc='left')
plt.tight_layout(); plt.savefig(OUT+'f24_slack.png',dpi=150); plt.close()
print("f24 ok")

# ---------- F25  the Sc VI bracket, squeezed ----------
d4,d5=1.0057,0.9812
d2=(d4-d5)/(1/16-1/25); d0=d4-d2/16
Z,I=6,892700.
E=lambda dv,n=6: I-Z*Z*R/(n-dv)**2
bands=[('§17.6  monotone only\nδ∞ < δ(6s) < δ(5s)',E(d5),E(d0),LIGHT),
       ('§14.4  + convexity\nδ(6s) ≥ 2δ(5s) − δ(4s)',E(d5),E(2*d5-d4),MID)]
est=E(d0+d2/36)
fig,ax=plt.subplots(figsize=(9.8,3.9))
for i,(lab,lo,hi,cl) in enumerate(bands):
    ax.barh(i,hi-lo,left=lo,height=0.42,color=cl,edgecolor='white',linewidth=0.8)
    ax.text(lo-260,i,lab,ha='right',va='center',fontsize=8.5,color=INK)
    ax.text((lo+hi)/2,i-0.34,f'{hi-lo:.0f} cm$^{{-1}}$',ha='center',fontsize=8.5,color=INK)
ax.axvline(est,color=ACC,lw=1.6)
ax.annotate(f'two-point Ritz estimate\n{est:.0f} cm$^{{-1}}$  ·  13.5743 nm',(est,1.52),
    xytext=(est+380,1.62),fontsize=8.5,color=ACC,
    arrowprops=dict(arrowstyle='-|>',color=ACC,lw=1.0))
ax.set_yticks([]); ax.set_ylim(-0.7,2.0)
ax.set_xlabel('Sc VI 3s$^2$3p$^3$($^4$S°)6s   $^3$S°$_1$   /   cm$^{-1}$')
ax.set_xlim(735300,739100)
ax.set_title('a committed prediction, tightened 1.8× and still inside its original bound',
             fontsize=10,color=INK,loc='left')
plt.tight_layout(); plt.savefig(OUT+'f25_scvi.png',dpi=150); plt.close()
print("f25 ok  widths",round(E(d0)-E(d5)),round(E(2*d5-d4)-E(d5)))