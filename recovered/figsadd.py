#!/usr/bin/env python3
"""figsadd.py -- reference figures for the compendium ADDITIONS. Sealed data only."""
import json, numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
OUT='/mnt/user-data/outputs/figures-compendia/'
rows=[json.loads(l) for l in open('rt/nlchain.jsonl')]

# ---- A1: the chain as a transition index (schematic) ----
fig,ax=plt.subplots(figsize=(10,3.2)); ax.axis('off')
steps=[('cfg(Z\u22121)','the carried state'),('SCF field\nof (Z, cfg(Z\u22121))','the V$^{N-1}$ ion'),
       ('candidate\nspectrum','every frontier (n,\u2113)'),('entrant =\ndeepest channel','the move'),
       ('cfg(Z)','the next state')]
xs=np.linspace(0.06,0.94,5)
for (t,s),x in zip(steps,xs):
    ax.add_patch(FancyBboxPatch((x-0.075,0.42),0.15,0.34,boxstyle='round,pad=0.012',
                 fc='#f4f2ee',ec='#8a1f11',lw=1.2,transform=ax.transAxes))
    ax.text(x,0.66,t,ha='center',va='center',fontsize=9,fontweight='bold',transform=ax.transAxes)
    ax.text(x,0.32,s,ha='center',va='center',fontsize=7.5,color='#555',transform=ax.transAxes)
for x0,x1 in zip(xs[:-1],xs[1:]):
    ax.add_patch(FancyArrowPatch((x0+0.078,0.59),(x1-0.078,0.59),transform=ax.transAxes,
                 arrowstyle='-|>',mutation_scale=14,color='#1a1a1a',lw=1.2))
ax.add_patch(FancyArrowPatch((xs[-1],0.40),(xs[0],0.40),transform=ax.transAxes,
             connectionstyle='arc3,rad=0.32',arrowstyle='-|>',mutation_scale=14,
             color='#8a1f11',lw=1.3,ls='--'))
ax.text(0.5,0.06,'Z \u2192 Z+1 : the output state seeds the next move',ha='center',
        fontsize=8.5,color='#8a1f11',transform=ax.transAxes)
ax.set_title('\u039b_chain is a transition index: each cell is one MOVE, Z\u22121 \u2192 Z,\n'
             'and the moves are totally ordered \u2014 the time column is the walk itself',fontsize=10)
plt.tight_layout(); plt.savefig(OUT+'fig-add-ioi-chain.png',dpi=170); plt.close()

# ---- A2: provenance / status strip of the index ----
fig,ax=plt.subplots(figsize=(11,2.6))
V5={38,56,72,89,105}; EXC={57:'La',89:'Ac',90:'Th'}
for r in rows:
    z=r['Z']
    if z<=108:
        ax.add_patch(plt.Rectangle((z-0.5,0),1,1,color='#2da44e',ec='white',lw=0.3))
    else:
        ax.add_patch(plt.Rectangle((z-0.5,0),1,1,fill=False,ec='#e36209',lw=1.1))
for z in V5:
    ax.plot(z,1.25,marker='v',color='#1f6feb',ms=7)
for z,nm in EXC.items():
    ax.plot(z,-0.25,marker='o',mfc='none',mec='black',ms=7)
    ax.annotate(nm,(z,-0.55),ha='center',fontsize=7)
ax.axvline(108.5,color='k',ls='--',lw=1)
ax.text(38,1.55,'\u25bc contested rows (\u039b_V5)',fontsize=7.5,color='#1f6feb')
ax.text(95,1.55,'boundary Z=108',fontsize=7.5)
ax.text(30,-0.95,'\u25cb tie-break exceptions, derived (collapse)',fontsize=7.5)
ax.text(112,0.5,'unwitnessed',fontsize=7.5,color='#e36209',ha='center',rotation=0,va='center')
ax.set_xlim(0,122); ax.set_ylim(-1.3,2.0); ax.set_yticks([]); ax.set_xlabel('Z')
ax.spines[['left','top','right']].set_visible(False)
ax.set_title('The provenance of \u039b_chain, cell by cell: 107 SCORED (solid) \u00b7 12 UNWITNESSED (open)\n'
             'with the five contested rows and the three derived exceptions marked',fontsize=10)
plt.tight_layout(); plt.savefig(OUT+'fig-add-ioi-provenance.png',dpi=170); plt.close()

# ---- A3: the pinned g channels, as reference constants ----
fig,ax=plt.subplots(figsize=(9,4.6))
series={}
for r in rows:
    for ch,d in r['order']:
        series.setdefault(ch,[]).append((r['Z'],d))
GC={'5g':(-0.020000,'#8250df'),'6g':(-1/72,'#9a6ee8'),'7g':(-1/98,'#b28df0'),'8g':(-1/128,'#c9adf6')}
for ch in ('4f','5d'):
    zs,ds=zip(*sorted(series[ch]))
    ax.plot(zs,ds,color='0.75',lw=1.0)
    ax.annotate(ch+'  (responds to Z)',(zs[len(zs)//2],ds[len(ds)//2]),fontsize=7.5,color='0.45')
for ch,(v,c) in GC.items():
    zs,ds=zip(*sorted(series[ch]))
    ax.plot(zs,ds,color=c,lw=2.0)
    ax.annotate('%s = \u22121/(2\u00b7%s\u00b2) = %.6f   (%d elements, spread \u2264 1e\u22125)'
                %(ch,ch[0],v,len(zs)),(121,v),fontsize=7.6,color=c,va='center')
ax.set_xlim(0,190); ax.set_ylim(-0.5,0.01)
ax.set_xlabel('Z'); ax.set_ylabel('channel depth (Ha)')
ax.set_xticks(range(0,121,20))
ax.set_title('The pinned rows: every g channel sits at its hydrogenic depth across the whole walk\n'
             'while the f and d channels beside them move \u2014 the constants of the derived supply',fontsize=10)
plt.tight_layout(); plt.savefig(OUT+'fig-add-sc-gpin.png',dpi=170); plt.close()

# ---- A4: the margin, row by row ----
fig,ax=plt.subplots(figsize=(11,4.2))
zs=[r['Z'] for r in rows if r['Z']<=108]; ms=[r['margin'] for r in rows if r['Z']<=108]
ax.bar(zs,ms,width=0.9,color='#2da44e',alpha=0.75)
for z in V5:
    r=next(x for x in rows if x['Z']==z)
    ax.bar([z],[r['margin']],width=0.9,color='#1f6feb')
    ax.annotate(str(z),(z,r['margin']+0.012),ha='center',fontsize=7,color='#1f6feb')
ax.set_xlabel('Z'); ax.set_ylabel('margin (Ha)')
ax.set_xlim(0,110)
ax.set_title('The entrant margin at every scored row \u2014 the quantity all later scrutiny is measured against\n'
             'blue: the five contested rows, where the correlation clause was computed (all widen)',fontsize=10)
plt.tight_layout(); plt.savefig(OUT+'fig-add-sc-margin.png',dpi=170); plt.close()
print('four addition figures written')