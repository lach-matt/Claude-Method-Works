import numpy as np, json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import eldata as ed
from scipy import stats

plt.rcParams.update({'font.family':'serif','font.serif':['FreeSerif','DejaVu Serif'],
                     'axes.linewidth':0.7,'savefig.dpi':200,'figure.facecolor':'white'})

dHf = {21:-100.,22:-72.,23:-32.,24:10.,26:20.,27:15.,28:20.,29:40.,
39:-114.,40:-82.,41:-40.,42:25.,44:30.,45:20.,46:-19.,47:60.,
57:-104.,58:-100.,59:-104.,60:-100.,62:-96.,63:-88.,64:-92.,65:-92.,
66:-92.,67:-90.,68:-90.,69:-88.,70:-84.,71:-84.,72:-66.,73:-38.,
74:30.,75:25.,77:30.,78:25.,79:50.,90:-72.,92:-42.}
MN = {21:19,22:51,23:54,24:57,26:61,27:64,28:67,29:72,39:20,40:49,41:53,
42:56,44:62,45:65,46:69,47:71,57:33,58:32,59:31,60:30,62:28,63:18,64:27,
65:26,66:25,67:24,68:23,69:22,70:17,71:21,72:50,73:52,74:55,75:58,77:63,
78:66,79:70,90:47,92:45}
MIE = {21:(3.25,1.27),22:(3.65,1.47),23:(4.25,1.64),24:(4.65,1.74),26:(4.93,1.77),
27:(5.10,1.75),28:(5.20,1.75),29:(4.45,1.47),39:(3.20,1.21),40:(3.40,1.39),
41:(4.00,1.62),42:(4.65,1.77),44:(5.40,1.83),45:(5.40,1.76),46:(5.45,1.67),
47:(4.35,1.36),57:(3.05,1.09),58:(3.18,1.19),59:(3.19,1.09),60:(3.19,1.08),
62:(3.20,1.07),63:(3.20,1.04),64:(3.20,1.21),65:(3.21,1.12),66:(3.21,1.11),
67:(3.22,1.11),68:(3.22,1.11),69:(3.22,1.11),70:(3.23,0.99),71:(3.23,1.14),
72:(3.55,1.43),73:(4.05,1.63),74:(4.80,1.81),75:(5.20,1.86),77:(5.55,1.83),
78:(5.65,1.78),79:(5.15,1.57),90:(3.30,1.28),92:(4.05,1.56)}

ZS=[z for z in sorted(dHf) if z in MN and z in MIE]
Y=np.array([dHf[z] for z in ZS],float)
lv=np.array([ed.E[z][1] for z in ZS],float); kv=np.array([ed.E[z][2] for z in ZS],float)
mn=np.array([MN[z] for z in ZS],float)
phi=np.array([MIE[z][0] for z in ZS]); nws=np.array([MIE[z][1] for z in ZS])

def loo(cols):
    X=np.column_stack([np.ones(len(Y))]+cols); pr=np.zeros(len(Y))
    for i in range(len(Y)):
        m=np.ones(len(Y),bool); m[i]=False
        b,*_=np.linalg.lstsq(X[m],Y[m],rcond=None); pr[i]=X[i]@b
    return 1-np.sum((Y-pr)**2)/np.sum((Y-np.mean(Y))**2), pr

fig = plt.figure(figsize=(12.4, 3.9))
gs = fig.add_gridspec(1, 3, width_ratios=[1.25, 1.0, 1.05], wspace=0.34)

# ── (a) benchmark bars ──────────────────────────────────────────
ax = fig.add_subplot(gs[0])
schemes = [
    ('Z alone',            [np.array(ZS,float)],          '#b9b3a9'),
    ('Lach  ℓ + k',        [lv,kv],                        '#2c5f9e'),
    ('Pettifor  MN',       [mn],                           '#c1751a'),
    ('Miedema  φ*, n$_{ws}$', [phi,nws],                   '#6b3fa0'),
    ('Pettifor  MN + MN²', [mn,mn**2],                     '#c1751a'),
    ('Miedema  full',      [phi,nws,(phi-2.1)**2,(nws-1.5)**2], '#6b3fa0'),
]
vals=[]; labs=[]; cols=[]; npars=[]
for nm,c,col in schemes:
    r,_=loo(c); vals.append(r); labs.append(nm); cols.append(col); npars.append(len(c))
order=np.argsort(vals)
y=np.arange(len(vals))
ax.barh(y, [vals[i] for i in order], color=[cols[i] for i in order],
        edgecolor='#333', lw=0.6, height=0.62)
ax.set_yticks(y); ax.set_yticklabels([labs[i] for i in order], fontsize=8.5)
for j,i in enumerate(order):
    ax.text(vals[i]+0.015, j, f'{vals[i]:.2f}', va='center', fontsize=8, fontweight='bold')
    ax.text(0.012, j, f'{npars[i]}p', va='center', fontsize=7, color='white'
            if vals[i]>0.12 else '#555')
ax.axvline(0, color='#555', lw=0.8)
ax.set_xlim(-0.14, 1.0)
ax.set_xlabel('cross-validated R²  (leave-one-out)', fontsize=9)
ax.set_title('(a)  benchmarked against prior art', fontsize=10, loc='left')
ax.grid(axis='x', alpha=0.2, lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)

# ── (b) orthogonality of k ──────────────────────────────────────
ax = fig.add_subplot(gs[1])
pairs = [('Mendeleev\nnumber', mn), ('Miedema  φ*', phi), ('Miedema  n$_{ws}$', nws)]
xs = np.arange(len(pairs)); w=0.36
rl = [abs(stats.pearsonr(lv,b)[0]) for _,b in pairs]
rk = [abs(stats.pearsonr(kv,b)[0]) for _,b in pairs]
ax.bar(xs-w/2, rl, w, color='#8ba9c9', edgecolor='#33526e', lw=0.6, label='ℓ  (block index)')
ax.bar(xs+w/2, rk, w, color='#0a7a3a', edgecolor='#08532a', lw=0.6, label='k  (occupancy)')
for x,v in zip(xs-w/2, rl): ax.text(x, v+0.02, f'{v:.2f}', ha='center', fontsize=7.6)
for x,v in zip(xs+w/2, rk): ax.text(x, v+0.02, f'{v:.2f}', ha='center', fontsize=7.6)
ax.set_xticks(xs); ax.set_xticklabels([a for a,_ in pairs], fontsize=8.2)
ax.set_ylabel('| Pearson r | with established descriptor', fontsize=8.6)
ax.set_ylim(0, 1.0)
ax.set_title('(b)  k is orthogonal to prior descriptors', fontsize=10, loc='left')
ax.legend(frameon=False, fontsize=8, loc='upper right')
ax.grid(axis='y', alpha=0.2, lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)

# ── (c) incremental value of k ──────────────────────────────────
ax = fig.add_subplot(gs[2])
bases = [('Pettifor\nMN',[mn], 0.001), ('Pettifor\nMN+MN²',[mn,mn**2], 0.029),
         ('Miedema\nφ*,n$_{ws}$',[phi,nws], 0.043), ('Miedema\nfull',[phi,nws,(phi-2.1)**2,(nws-1.5)**2], 0.363)]
xs=np.arange(len(bases))
b0=[]; b1=[]
for nm,c,pv in bases:
    r0,_=loo(c); r1,_=loo(c+[kv]); b0.append(r0); b1.append(r1)
ax.bar(xs, b0, 0.52, color='#c9c4bc', edgecolor='#8a8378', lw=0.6, label='scheme alone')
ax.bar(xs, np.array(b1)-np.array(b0), 0.52, bottom=b0, color='#0a7a3a',
       edgecolor='#08532a', lw=0.6, label='gain from adding k')
for i,(nm,c,pv) in enumerate(bases):
    d=b1[i]-b0[i]
    star = '**' if pv<0.01 else ('*' if pv<0.05 else 'n.s.')
    ax.text(i, max(b1[i],b0[i])+0.022, f'{d:+.3f}\n{star}', ha='center', fontsize=7.6,
            color='#0a7a3a' if pv<0.05 else '#888', fontweight='bold' if pv<0.05 else 'normal')
ax.set_xticks(xs); ax.set_xticklabels([a for a,_,_ in bases], fontsize=7.8)
ax.set_ylabel('cross-validated R²', fontsize=9)
ax.set_ylim(0, 1.06)
ax.set_title('(c)  does k improve prior art?', fontsize=10, loc='left')
ax.legend(frameon=False, fontsize=7.6, loc='lower left')
ax.grid(axis='y', alpha=0.2, lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
ax.text(0.98, 0.03, '** p<0.01   * p<0.05', transform=ax.transAxes, fontsize=7,
        ha='right', color='#666')

plt.savefig('/home/claude/fig5c_benchmark.png', bbox_inches='tight')
print('ok')
