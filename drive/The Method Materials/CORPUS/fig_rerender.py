# chat 8: redraws figures 16.1, 12.3, 25.2, 24.1 into figures/ from the book's numbers.
# 24.1 needs fig241_data.json (per-species per-ell |dbar| parsed from the Spectra Compendium channel table; see 1753).
import json,numpy as np,matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, matplotlib.ticker as mt
plt.rcParams.update({'font.family':'serif','font.size':11})
def f161():
    n=np.arange(4,10); d2=np.array([1.3084,1.2830,1.2733,1.2685,1.2659,1.2642]); d1=(n+d2)/2   # Al II 3sns 3S at Z=2; Z=1 = (n+d2)/2
    fig,ax=plt.subplots(1,3,figsize=(10.5,4.3),gridspec_kw={'width_ratios':[0.8,1,1]})
    ax[0].bar(['Z = 1','Z = 2'],[56,56],color='0.55',width=0.55)
    for i in range(2): ax[0].text(i,57,'56/56',ha='center',va='bottom')
    ax[0].set_ylim(0,66); ax[0].set_ylabel('cells bracketed'); ax[0].set_title('the bracket\ncannot see it',fontsize=11)
    ax[1].plot(n,d1,'o-',color='#b03a2e'); ax[1].set_title('Z = 1   (wrong)',color='#b03a2e'); ax[1].text(0.04,0.93,f'spread {d1.max()-d1.min():.2f}',transform=ax[1].transAxes,color='#b03a2e')
    ax[2].plot(n,d2,'o-',color='#2e5d8c'); ax[2].set_title('Z = 2   (correct)',color='#2e5d8c'); ax[2].text(0.96,0.93,f'spread {d2.max()-d2.min():.2f}',transform=ax[2].transAxes,color='#2e5d8c',ha='right')
    for a in ax[1:]: a.set_xlabel('n'); a.grid(alpha=0.3); a.set_xticks(n)
    ax[1].set_ylabel('δ')
    for a in ax: a.spines[['top','right']].set_visible(False)
    fig.tight_layout(); fig.savefig('figures/figure-16.1.png',dpi=150)
def f123():
    q=np.arange(4); A13=[2294,2294,1794,744]; B13=[5,20,50,70]; S13=[a*b for a,b in zip(A13,B13)]; A8=[33,33,23,8]; B8=[5,10,15,17]
    assert S13==[11470,45880,89700,52080]
    fig,ax=plt.subplots(figsize=(8.2,5))
    ax.plot(q,A13,'o-',color='#a8752c',lw=2,ms=7,label='|A(q)| — parent side (falls)')
    ax.plot(q,B13,'s-',color='#2e6f8e',lw=2,ms=7,label='|B(q)| — target side (rises)')
    ax.plot(q,S13,'d--',color='0.15',lw=1.6,ms=7,label='|A×B| — the section')
    ax.plot(q,A8,'o:',color='#a8752c',alpha=0.45,ms=5); ax.plot(q,B8,'s:',color='#2e6f8e',alpha=0.45,ms=5)
    for x,s in zip(q,S13): ax.annotate(f'{s:,}',(x,s),textcoords='offset points',xytext=(0,9),ha='center',fontsize=9.5)
    ax.set_yscale('log'); ax.set_ylim(3,6e5); ax.set_xticks(q); ax.set_xlabel('q — the transfer'); ax.set_ylabel('cells (log)')
    ax.set_title('Raising the transfer costs the parent and pays the target\nsolid: Λ₁₃ · dotted: Λ₈ · peak q = 2 · ⟨q⟩ 1.463 → 1.887',fontsize=11.5)
    ax.grid(alpha=0.25); ax.spines[['top','right']].set_visible(False)
    ax.legend(loc='lower left',bbox_to_anchor=(0.03,0.30),frameon=False,fontsize=10)
    fig.tight_layout(); fig.savefig('figures/figure-12.3.png',dpi=150)
def f252():
    lo,hi_m,hi_c,ritz=735860,738547,737380,736688
    fig,ax=plt.subplots(figsize=(9.8,4.2))
    ax.barh(0,hi_m-lo,left=lo,height=0.45,color='0.72'); ax.barh(1,hi_c-lo,left=lo,height=0.45,color='#4f7594')
    ax.text((lo+hi_m)/2,-0.33,f'{hi_m-lo:,} cm⁻¹',ha='center',va='top',fontsize=10); ax.text((lo+hi_c)/2,0.67,f'{hi_c-lo:,} cm⁻¹',ha='center',va='top',fontsize=10)
    ax.axvline(ritz,color='#8b2a0f',lw=2.2)
    ax.annotate('two-point Ritz estimate\n736,688 cm⁻¹  ·  13.5743 nm',xy=(ritz,1.62),xytext=(ritz+380,1.75),color='#8b2a0f',fontsize=10.5,arrowprops=dict(arrowstyle='->',color='#8b2a0f'),va='center')
    ax.set_yticks([0,1]); ax.set_yticklabels(['§25.6.1  monotone only\nδ∞ < δ(6s) < δ(5s)','§25.6.2  + convexity\nδ(6s) ≥ 2δ(5s) − δ(4s)'])
    ax.set_ylim(-0.7,2.05); ax.set_xlim(735300,739100); ax.xaxis.set_major_formatter(mt.FuncFormatter(lambda x,p:f'{x:,.0f}'))
    ax.set_xlabel('Sc VI 3s²3p³(⁴S°)6s ³S°₁   /   cm⁻¹'); ax.set_title('a committed prediction, tightened 1.8× and still inside its original bound',fontsize=11.5,loc='left')
    ax.spines[['top','right']].set_visible(False); fig.tight_layout(); fig.savefig('figures/figure-25.2.png',dpi=150)
def f241():
    d=json.load(open('fig241_data.json'))
    def get(sp):
        out={}
        for k in (sp, sp+' *'):
            for l,v in d.get(k,{}).items(): out.setdefault(int(l),[]).extend(v)
        return out
    species=['Al I','Al II','Ar II','Be I','Be II','Bi I','C II','Ca II','Cd II','Ga I','He I','Hg II','K I','K II','Li I','Li II','Mg II','N II','Na I','Na II','Ne I','Si I','Si II','Zn II']   # He II drawn separately below
    FLOOR=5e-5; fig,ax=plt.subplots(figsize=(10.5,5.8)); cols=plt.cm.viridis(np.linspace(0,0.92,len(species)+1))
    for c,sp in zip(cols,species):
        g=get(sp); ls=sorted(g); ax.plot(ls,[max(np.mean(g[l]),FLOOR) for l in ls],'-',color=c,lw=1.2,label=sp)
        for l in ls:
            for v in g[l]: ax.plot(l,max(v,FLOOR),'o',ms=4,color=c,mfc=(c if v>0 else 'white'))
    g=get('He II'); ls=sorted(g); ax.plot(ls,[np.mean(g[l]) for l in ls],'D-',color='#1f6f8b',lw=1.4,ms=5,label='He II (corrected series, 1758)')
    # the three rises the caption names: perturbed channels and the fine-structure floor
    for sp,l0,l1 in [('Al I',2,3),('Al II',3,4),('He I',2,6)]:
        g=get(sp); ax.plot([l0,l1],[np.mean(g[l0]),np.mean(g[l1])],'-',color='none')
        dx=-0.35 if sp=='Al II' else 0
        ax.annotate('',xy=(l1,np.mean(g[l1])*1.6),xytext=(l1+dx,np.mean(g[l1])*4.5),arrowprops=dict(arrowstyle='->',color='0.35',lw=0.9))
        ax.text(l1+dx,np.mean(g[l1])*5.2,sp,ha='center',fontsize=8,color='0.35')
    ax.set_yscale('log'); ax.set_xticks(range(7)); ax.set_xticklabels(list('spdfghi')); ax.set_xlim(-0.3,6.3)
    ax.set_xlabel(r'orbital angular momentum  $\ell$'); ax.set_ylabel(r'$|\bar{\delta}|$  quantum defect'); ax.set_ylim(8e-7,8)
    ax.grid(alpha=0.25); ax.spines[['top','right']].set_visible(False)
    ax.legend(ncol=3,fontsize=8.5,loc='upper right',frameon=False,columnspacing=0.9,handlelength=1.6,title=r'penetration falls with $\ell$ across the collection',title_fontproperties={'style':'italic','size':10})
    fig.text(0.99,0.01,r'open markers: $|\bar{\delta}|$ < 10⁻⁴ in the table (below its resolution; drawn at 5 × 10⁻⁵)',ha='right',fontsize=8.5,color='0.3')
    fig.tight_layout(rect=(0,0.03,1,1)); fig.savefig('figures/figure-24.1.png',dpi=150)
if __name__=='__main__':
    f161(); f123(); f252(); f241(); print('four figures written')
