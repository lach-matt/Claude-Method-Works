import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch
from matplotlib.lines import Line2D
import eldata as ed

plt.rcParams.update({'font.family':'serif','font.serif':['FreeSerif','DejaVu Serif'],
                     'axes.linewidth':0.7,'savefig.dpi':200,'figure.facecolor':'white'})

MN={21:19,22:51,23:54,24:57,26:61,27:64,28:67,29:72,39:20,40:49,41:53,42:56,44:62,
45:65,46:69,47:71,57:33,58:32,59:31,60:30,62:28,63:18,64:27,65:26,66:25,67:24,68:23,
69:22,70:17,71:21,72:50,73:52,74:55,75:58,77:63,78:66,79:70,90:47,92:45,1:92,3:1,
4:77,5:86,6:95,7:100,8:101,9:102,11:11,12:73,13:80,14:85,15:90,16:94,17:99,19:10,
20:16,30:76,31:81,32:84,33:89,34:93,35:98,37:9,38:15,48:75,49:79,50:83,51:88,52:92,
53:97,55:8,56:14,80:74,81:78,82:82,83:87,84:91,85:96}
zs=sorted(ed.E)
def leq(a,b): return all(x<=y for x,y in zip(a,b))
com=sorted(z for z in MN if z in ed.E)
cp=[(a,b) for a in com for b in com if a!=b and leq(ed.E[a],ed.E[b])]
allp=[(a,b) for a in zs for b in zs if a!=b and leq(ed.E[a],ed.E[b])]
mad={z:i for i,z in enumerate(sorted(zs,key=lambda z:(ed.E[z][0]+ed.E[z][1],ed.E[z][0],ed.E[z][2])))}

OK='#1f6f3f'; BAD='#a8203c'; GR='#c9c4bc'

fig=plt.figure(figsize=(12.8,4.15))
gs=fig.add_gridspec(1,3,width_ratios=[1.05,1.25,1.05],wspace=0.30)

# ── (a) the three verdicts ───────────────────────────────────────
ax=fig.add_subplot(gs[0]); ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
rows=[('atomic number  Z', 0, len(allp), True),
      ('Madelung order', 0, len(allp), True),
      ('Pettifor  MN', 960, len(cp), False)]
y=0.80
for nm,v,tot,ok in rows:
    col=OK if ok else BAD
    ax.add_patch(Rectangle((0.04,y-0.105),0.92,0.20,facecolor=col,alpha=0.10,
                           edgecolor=col,lw=1.3))
    ax.text(0.08,y+0.038,nm,fontsize=10.5,fontweight='bold',color=col,va='center')
    ax.text(0.08,y-0.045,f'{v} order violations of {tot} comparable pairs',
            fontsize=8.2,color='#333',va='center')
    ax.text(0.93,y,'LINEAR\nEXTENSION' if ok else 'NOT\nORDER-COMPATIBLE',
            fontsize=8.0,color=col,ha='right',va='center',fontweight='bold')
    y-=0.30
ax.text(0.5,0.075,'a ≤ b in Λ  ⟹  rank(a) ≤ rank(b) ?',ha='center',
        fontsize=9.5,style='italic',color='#444')
ax.set_title('(a)  is each sorting system order-compatible with Λ?',
             fontsize=10,loc='left')

# ── (b) rank against lattice order, three systems ────────────────
ax=fig.add_subplot(gs[1])
# for each comparable pair, plot rank difference
import random
random.seed(3)
samp=random.sample(cp,700)
for i,(nm,R,col) in enumerate([('Z',{z:z for z in com},'#2c5f9e'),
                               ('Madelung',mad,'#c1751a'),
                               ('Pettifor MN',MN,BAD)]):
    d=[R[b]-R[a] for a,b in samp]
    xs=np.full(len(d),i)+np.random.uniform(-0.30,0.30,len(d))
    ax.scatter(xs,d,s=5,color=col,alpha=0.32,edgecolors='none')
    neg=sum(1 for x in d if x<0)
    ax.text(i,ax.get_ylim()[1] if False else 118,f'{100*neg/len(d):.0f}%\nreversed',
            ha='center',fontsize=8.2,color=col,fontweight='bold')
ax.axhline(0,color='#333',lw=1.1)
ax.set_xticks(range(3)); ax.set_xticklabels(['Z','Madelung','Pettifor MN'],fontsize=9)
ax.set_ylabel('rank(b) − rank(a)  for  a ≤ b in Λ',fontsize=9)
ax.set_ylim(-110,135)
ax.set_title('(b)  rank difference across comparable pairs',fontsize=10,loc='left')
ax.grid(axis='y',alpha=0.2,lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
ax.text(0.5,0.045,'points below the line reverse the lattice order',
        transform=ax.transAxes,ha='center',fontsize=7.8,style='italic',color='#666')

# ── (c) the f-block sign reversal ────────────────────────────────
ax=fig.add_subplot(gs[2])
cols={1:'#c1751a',2:'#6b3fa0',3:'#a8203c'}
for lv,lab in [(1,'p-block'),(2,'d-block'),(3,'f-block')]:
    pts=sorted((ed.E[z][2],MN[z]) for z in com if ed.E[z][1]==lv)
    ks=np.array([p[0] for p in pts],float); ms=np.array([p[1] for p in pts],float)
    ax.scatter(ks,ms,s=26,color=cols[lv],alpha=0.75,edgecolors='white',lw=0.4,label=lab)
    b=np.polyfit(ks,ms,1)
    xx=np.linspace(ks.min(),ks.max(),20)
    ax.plot(xx,np.polyval(b,xx),color=cols[lv],lw=1.9)
    ax.annotate(f'{b[0]:+.1f}',(xx[-1],np.polyval(b,xx[-1])),
                xytext=(6,-2),textcoords='offset points',fontsize=8.6,
                color=cols[lv],fontweight='bold')
ax.set_xlabel('k  (subshell occupancy)',fontsize=9)
ax.set_ylabel('Pettifor Mendeleev number',fontsize=9)
ax.set_title('(c)  ∂MN/∂k reverses sign at the f-block',fontsize=10,loc='left')
ax.legend(frameon=False,fontsize=8,loc='upper left')
ax.grid(alpha=0.2,lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
ax.text(0.97,0.05,'a linear function of (n,ℓ,k)\nhas constant ∂/∂k — so none exists',
        transform=ax.transAxes,ha='right',fontsize=7.6,style='italic',color='#555')

plt.savefig('/home/claude/figA_linext.png',bbox_inches='tight')
print('ok')
