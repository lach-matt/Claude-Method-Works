import json, math, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
plt.rcParams.update({'font.family':'FreeSerif','font.size':9,'axes.linewidth':.7,
    'figure.dpi':320,'savefig.dpi':320,'axes.grid':True,'grid.alpha':.25,'grid.linewidth':.5})
D=json.load(open('data.json'))
INK='#1a1a1a'; ACC='#8c2f39'; ACC2='#2f5d8c'

# Fig 1 — the coordinate index: occupied vs closure per chromosome
f,ax=plt.subplots(figsize=(6.4,2.9))
n=D['chrom']['names']; l=[x/1e6 for x in D['chrom']['lens']]; m=[x/1e6 for x in D['chrom']['M']]
x=range(len(n))
ax.fill_between(x,l,m,color=ACC,alpha=.22,label='admitted and absent  (E)')
ax.plot(x,m,color=ACC,lw=1.3,label='ℛ(X): running maximum')
ax.bar(x,l,color=INK,width=.55,label='X: assembled bases')
ax.set_xticks(list(x)); ax.set_xticklabels(n,fontsize=6.5)
ax.set_ylabel('Mbp'); ax.set_xlabel('chromosome, as conventionally labelled')
ax.legend(frameon=False,fontsize=7.5,loc='upper right')
ax.set_title(f"E = {D['chrom']['E']:,} cells  ({D['chrom']['ratio']:.1%} of |X|)",fontsize=9,loc='left')
f.tight_layout(); f.savefig('fig/f1_coordinate.png'); plt.close(f)

# Fig 2 — the three prediction budgets
f,ax=plt.subplots(figsize=(5.2,2.5))
b=D['budget']; lbl=['coordinate\n(forbidden)','ignorance\n(unknown)','contingent\n(realisable)']
v=[b['coordinate'],b['ignorance'],b['contingent']]
bars=ax.barh(lbl,v,color=[ACC,'#2f8c4f',ACC2],height=.55)
ax.set_xscale('log'); ax.set_xlabel('admitted-and-absent cells (log)')
for bar,val in zip(bars,v): ax.text(val*1.15,bar.get_y()+bar.get_height()/2,f'{val:,}',va='center',fontsize=7.5)
ax.set_xlim(1e8,4e10)
ax.set_title('only the middle budget ever reached zero',fontsize=9,loc='left')
f.tight_layout(); f.savefig('fig/f2_budgets.png'); plt.close(f)

# Fig 3 — E/N -> |S|-1
f,ax=plt.subplots(figsize=(3.5,2.4))
N=[s['N'] for s in D['seq']]; r=[s['ratio'] for s in D['seq']]
ax.plot(N,r,'o-',color=INK,ms=4,lw=1.2,label='random sequence')
ax.axhline(3,color=ACC,ls='--',lw=1,label='|Σ| − 1 = 3')
ax.plot(N,[0]*len(N),'s-',color=ACC2,ms=4,lw=1.2,label='monotone sequence')
ax.set_xscale('log'); ax.set_xlabel('N'); ax.set_ylabel('E / N'); ax.set_ylim(-.3,3.4)
ax.legend(frameon=False,fontsize=7)
f.tight_layout(); f.savefig('fig/f3_content.png'); plt.close(f)

# Fig 4 — the two branches
f,ax=plt.subplots(figsize=(3.5,2.4))
k=D['kmer']['k']
ax.plot(k,D['kmer']['alpha'],color=ACC,lw=1.3,label='4^k  (alphabet)')
ax.plot(k,D['kmer']['length'],color=ACC2,lw=1.3,label='N−k+1  (length)')
ax.axvline(D['kmer']['kstar'],color=INK,ls=':',lw=1)
ax.text(D['kmer']['kstar']+.25,1e6,f"k* = {D['kmer']['kstar']:.2f}",fontsize=7.5,rotation=90,va='bottom')
ax.set_yscale('log'); ax.set_xlabel('k'); ax.set_ylabel('distinct k-mers, bound')
ax.legend(frameon=False,fontsize=7,loc='lower right')
f.tight_layout(); f.savefig('fig/f4_crossing.png'); plt.close(f)

# Fig 5 — the snarl tower, both orientations
f,(a1,a2)=plt.subplots(1,2,figsize=(6.4,2.5),sharey=True)
A=D['snarl']['A']; Dl=D['snarl']['D']
for ax,vec,ttl,e in ((a1,A[::-1],'as labelled: level 0 outermost',D['snarl']['E_level']),
                     (a2,A,'read by height',D['snarl']['E_height'])):
    ax.bar(range(len(vec)),vec,color=INK if e==0 else ACC,width=.8)
    ax.set_title(f'{ttl}\nE = {e:,}',fontsize=8.5,loc='left')
    ax.set_xlabel('level' if e else 'height u = D − level')
a1.set_ylabel('observed alleles A')
f.tight_layout(); f.savefig('fig/f5_snarl.png'); plt.close(f)

# Fig 6 — inversion-count stability
f,ax=plt.subplots(figsize=(3.5,2.3))
d={int(k):v for k,v in D['chrom']['dist3'].items()}
ks=sorted(d); ax.bar(ks,[d[k] for k in ks],color=INK,width=.7)
ax.bar([3],[d.get(3,0)],color=ACC,width=.7)
ax.set_xlabel('autosome inversions under ±3% length perturbation')
ax.set_ylabel('trials of 2000')
ax.set_title(f"observed value 3 reproduces {D['chrom']['stab3']}/2000",fontsize=8.5,loc='left')
f.tight_layout(); f.savefig('fig/f6_stability.png'); plt.close(f)
print("6 figures written")