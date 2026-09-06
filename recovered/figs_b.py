import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyArrowPatch
INK='#1a1a1a'; ACC='#b3341f'; BLU='#1f5fa9'; GRY='#8f8f8f'; LT='#e9e5dd'; GRN='#2e6b4f'
plt.rcParams.update({'font.size':9,'axes.edgecolor':INK,'axes.labelcolor':INK,
    'text.color':INK,'xtick.color':INK,'ytick.color':INK,'axes.linewidth':0.8,
    'figure.facecolor':'white','savefig.facecolor':'white','font.family':'DejaVu Sans'})

# ---------- FIG 6: the cap-arity criterion ----------
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(8.4,3.4),gridspec_kw={'width_ratios':[1.05,1]})
# (a) schematic
ax1.set_xlim(0,10); ax1.set_ylim(0,10); ax1.axis('off')
ax1.text(0.2,9.4,'single-argument cap  \u2192  tree edge  \u2192  LATTICE',fontsize=8.3,color=GRN,fontweight='bold')
for (x,y,t) in [(1.6,7.6,"\u2113'"),(4.4,7.6,"m'")]:
    ax1.scatter([x],[y],s=300,color='white',edgecolors=INK,zorder=2)
    ax1.text(x,y,t,ha='center',va='center',fontsize=9,zorder=3)
ax1.plot([1.6,4.4],[7.6,7.6],color=GRN,lw=1.4)
ax1.text(3.0,7.95,"m' \u2264 2\u2113'+2",ha='center',fontsize=7.6,color=GRN)
ax1.text(6.2,7.6,"\u039b_sph\n0 / 114,960 failures",fontsize=7.6,color=GRN,va='center')
ax1.text(0.2,5.4,'multi-argument cap  \u2192  hyperedge  \u2192  SEMILATTICE',fontsize=8.3,color=ACC,fontweight='bold')
for (x,y,t) in [(1.2,3.2,'m'),(2.8,3.2,'n'),(4.4,3.2,'l'),(2.8,1.2,'s')]:
    ax1.scatter([x],[y],s=300,color='white',edgecolors=INK,zorder=2)
    ax1.text(x,y,t,ha='center',va='center',fontsize=9,zorder=3)
for x in (1.2,2.8,4.4):
    ax1.plot([x,2.8],[3.2,1.2],color=ACC,lw=1.2,ls='--')
ax1.text(5.0,2.2,"s \u2264 \u03bd(m,n,l) \u2212 1\n\u03bd is monotone but not\na meet-morphism",fontsize=7.6,color=ACC,va='center')
ax1.text(1.0,0.15,'\u039b_cav:  768 / 15,400 meet failures',fontsize=7.6,color=ACC)
ax1.set_title('(a) the criterion',fontsize=8.8,loc='left')
# (b) measured
labels=['\u039b_cav\n(rectangular)','\u039b_sph\n(spherical)']
join=[0,0]; meet=[768,0]; pairs=[15400,114960]
x=np.arange(2); w=0.34
ax2.bar(x-w/2,[100*j/p for j,p in zip(join,pairs)],w,color=GRY,edgecolor=INK,lw=0.7,label='join failures')
ax2.bar(x+w/2,[100*m/p for m,p in zip(meet,pairs)],w,color=ACC,edgecolor=INK,lw=0.7,label='meet failures')
ax2.set_xticks(x); ax2.set_xticklabels(labels,fontsize=8.2)
ax2.set_ylabel('% of pairs failing closure'); ax2.set_ylim(0,6.4)
ax2.legend(frameon=False,fontsize=8)
ax2.text(0,5.15,'768 / 15,400\n= 4.99%',ha='center',fontsize=8,color=ACC)
ax2.text(1,1.0,'0 / 114,960\n0 rank-modularity\n0 distributivity',ha='center',fontsize=8,color=GRN)
ax2.set_title('(b) predicted in advance, both directions',fontsize=8.8,loc='left')
fig.suptitle('Figure 6.  Cap arity decides lattice closure. The prediction was committed before either object was built.',
             fontsize=9.5,x=0.012,ha='left',y=0.985)
plt.tight_layout(rect=[0,0,1,0.93]); plt.savefig('figs/fig06_caparity.png',dpi=200); plt.close()

# ---------- FIG 7: the lattice bracket ----------
na_lo=[0.4871,0.5493,0.5457,0.5255,0.5756,0.5099,0.5938,0.4986,0.6061,0.4900,0.6148,0.4832,0.6214]
na_hi=[0.0060]
mg_lo=[0.4128,0.3919,0.4607,0.4695,0.3818]
mg_hi=[0.0187,0.0014,0.0015,0.0215,0.0015,0.0016]
al_lo=[0.3372,0.8542,0.4376,0.6796,0.4351,0.5979,0.5688]
LO=na_lo+mg_lo+al_lo; HI=na_hi+mg_hi
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(8.4,3.4),gridspec_kw={'width_ratios':[1,1.05]})
ax1.set_xlim(-1.7,1.7); ax1.set_ylim(-1.8,1.8); ax1.axis('off')
ax1.add_patch(Rectangle((-1.5,-0.35),3.0,0.7,fc=LT,ec='none'))
for (dx,dy,t,col) in [(0,1,'(n+1, \u2113)',BLU),(0,-1,'(n\u22121, \u2113)',BLU),
                      (-1,0,'(n, \u2113\u22121)',ACC),(1,0,'(n, \u2113+1)',ACC)]:
    ax1.scatter([dx],[dy],s=340,color='white',edgecolors=col,linewidths=1.4,zorder=2)
    ax1.text(dx,dy,t,ha='center',va='center',fontsize=6.6,zorder=3)
    ax1.plot([0,dx],[0,dy],color=col,lw=1.1,zorder=1)
ax1.scatter([0],[0],s=380,color=INK,zorder=2)
ax1.text(0,0,'(n, \u2113)',ha='center',va='center',fontsize=6.8,color='white',zorder=3)
ax1.text(0,1.55,'channel bracket uses this axis only',ha='center',fontsize=7.6,color=BLU)
ax1.text(0,-1.62,'lattice bracket intersects BOTH',ha='center',fontsize=7.6,color=ACC)
ax1.set_title('(a) bracket by all covers, not one channel',fontsize=8.8,loc='left')
parts=ax2.boxplot([LO,HI],vert=True,widths=0.5,patch_artist=True,
                  medianprops=dict(color=INK,lw=1.2))
for p,c in zip(parts['boxes'],[GRY,ACC]): p.set_facecolor(c); p.set_edgecolor(INK); p.set_alpha(0.75)
for i,(d,c) in enumerate(zip([LO,HI],[GRY,ACC])):
    ax2.scatter(np.random.default_rng(3).normal(i+1,0.055,len(d)),d,s=13,color=INK,zorder=3,alpha=0.8)
ax2.set_yscale('log'); ax2.set_xticks([1,2])
ax2.set_xticklabels([f'\u2113 \u2264 2\n(n={len(LO)})',f'\u2113 \u2265 3\n(n={len(HI)})'],fontsize=8.2)
ax2.set_ylabel('width ratio  lattice / channel')
ax2.axhline(1.0,color=INK,lw=0.8,ls=':')
ax2.text(2.42,1.05,'no tightening',fontsize=7.4,color=GRY,ha='right')
ax2.text(1.0,0.9,f'mean {np.mean(LO):.2f}\n\u2248 {1/np.mean(LO):.1f}\u00d7 tighter',ha='center',fontsize=7.8)
ax2.text(2.0,0.00035,f'mean {np.mean(HI):.4f}\n\u2248 {1/np.mean(HI):.0f}\u00d7 tighter',ha='center',fontsize=7.8,color=ACC)
ax2.set_ylim(3e-4,3)
ax2.set_title('(b) measured on Na I, Mg II, Al I, He I',fontsize=8.8,loc='left')
fig.suptitle('Figure 7.  The lattice bracket. 55 admissible cells, 0 violations; 12 excluded cells, 12 violations.',
             fontsize=9.5,x=0.012,ha='left',y=0.985)
plt.tight_layout(rect=[0,0,1,0.93]); plt.savefig('figs/fig07_bracket.png',dpi=200); plt.close()
print("mean LO",np.mean(LO),"->",1/np.mean(LO)," mean HI",np.mean(HI),"->",1/np.mean(HI))

# ---------- FIG 8: the admissibility mechanism ----------
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(8.4,3.3))
ax1.plot([1,2],[-0.0095,0.0016],'o-',color=ACC,lw=1.8,ms=8)
ax1.axhline(0,color=GRY,lw=0.8,ls=':')
ax1.annotate('',xy=(2,0.0016),xytext=(1,-0.0095),
             arrowprops=dict(arrowstyle='->',color=ACC,lw=1.6))
ax1.set_xticks([1,2]); ax1.set_xticklabels(['\u2113 = 1  (p)','\u2113 = 2  (d)'])
ax1.set_ylabel('quantum defect  \u03b4')
ax1.set_title('(a) He I singlet:  \u03b4 RISES  \u2192  T-order inverts  \u2192  12 violations',
              fontsize=8.4,loc='left',color=ACC)
ax1.text(1.5,-0.004,'\u22120.0095 \u2192 +0.0016\nsign change, and a RISE',ha='center',fontsize=8)
ax1.set_ylim(-0.013,0.005)
ax2.plot([3,4],[0.000148,-0.000081],'o-',color=GRN,lw=1.8,ms=8)
ax2.axhline(0,color=GRY,lw=0.8,ls=':')
ax2.set_xticks([3,4]); ax2.set_xticklabels(['\u2113 = 3  (f)','\u2113 = 4  (g)'])
ax2.set_ylabel('quantum defect  \u03b4')
ax2.set_title('(b) Be II:  \u03b4 FALLS  \u2192  T-order preserved  \u2192  0 violations',
              fontsize=8.4,loc='left',color=GRN)
ax2.text(3.5,0.00006,'+0.000148 \u2192 \u22120.000081\nsign change, but a FALL',ha='center',fontsize=8)
ax2.set_ylim(-0.00022,0.00024)
fig.suptitle('Figure 8.  The falsification that corrected the framework.  T = Z\u00b2R/(n\u2212\u03b4)\u00b2 is increasing in \u03b4,\n'
  'so \u2113-order is preserved iff \u03b4 is non-increasing. A sign change is not the failure condition \u2014 a RISE is.',
  fontsize=9.3,x=0.012,ha='left',y=0.995)
plt.tight_layout(rect=[0,0,1,0.87]); plt.savefig('figs/fig08_mechanism.png',dpi=200); plt.close()

# ---------- FIG 9: the r_l exit ----------
fig,ax=plt.subplots(figsize=(8.2,3.3))
n=[5,6,7]; r=[11.5,4.80,4.01]; DT=[1.610,0.960,0.800]; sg=[0.14,0.20,0.20]
cols=[GRN if v>=5 else ACC for v in r]
ax.bar(n,r,width=0.5,color=cols,edgecolor=INK,lw=0.8)
ax.axhline(5,color=INK,lw=1.3,ls='--')
ax.text(7.45,5.25,'B.2.2 threshold  r = 5',fontsize=8.2,ha='right')
nn=np.linspace(4.8,7.4,80)
ax.plot(nn,11.5*(5/nn)**3*(0.14/0.20),color=GRY,lw=1.1,ls=':')
ax.text(6.75,8.4,'\u03bd\u207b\u00b3 trend',fontsize=7.6,color=GRY)
for x,v,d,s in zip(n,r,DT,sg):
    ax.text(x,v+0.35,f'{v:.2f}',ha='center',fontsize=8.6,fontweight='bold')
    ax.text(x,0.45,f'\u0394T={d}\n\u03c3={s}',ha='center',fontsize=7.4,color='white')
ax.text(6.5,2.0,'admissible \u2192 EXITS\nthe deduction is still correct here;\nthe interval has shrunk below \u03c3',
        fontsize=8,color=ACC,ha='center')
ax.set_xticks(n); ax.set_xticklabels(['5f\u20135g','6f\u20136g','7f\u20137g'])
ax.set_ylabel('separation ratio  r$_\u2113$ = \u0394T / \u03c3'); ax.set_ylim(0,13)
ax.set_title('Figure 9.  The first observed r$_\u2113$ exit on real data, under the compilation\u2019s own uncertainties (Be II).\n'
   'B.2.2 asks whether levels are separated; B.2.3 asks whether the answer is resolvable. Here the second fails first.',
   fontsize=9.3,loc='left',pad=6)
plt.tight_layout(); plt.savefig('figs/fig09_rexit.png',dpi=200); plt.close()

# ---------- FIG 10: the prediction budget ----------
fig,ax=plt.subplots(figsize=(8.2,3.3))
preds=['Be II fails at \u2113=3\u21924','r$_\u2113$ eventually bites','Be I / Ne I fail',
       'coverage drops on raw levels','Al I labelling generalises']
status=['REFUTED\n(and corrected the framework)','CONFIRMED\n(first exit)','open','open','open']
cols=[ACC,GRN,GRY,GRY,GRY]
y=np.arange(5)[::-1]
for i,(p,s,c) in enumerate(zip(preds,status,cols)):
    yy=y[i]
    ax.add_patch(Rectangle((0,yy-0.32),4.2,0.64,fc=LT,ec=INK,lw=0.6))
    ax.text(0.12,yy,p,va='center',fontsize=8.3)
    ax.text(4.45,yy,s,va='center',fontsize=7.8,color=c,
            fontweight='bold' if c!=GRY else 'normal')
    if c!=GRY:
        ax.add_patch(FancyArrowPatch((4.28,yy),(4.40,yy),arrowstyle='->',color=c,lw=1.2,mutation_scale=9))
ax.text(0,4.85,'E(X) = 5  before the Be II campaign',fontsize=9,fontweight='bold')
ax.text(0,-0.95,'E(X) = 3  after  \u2014  5 \u2212 2 = 3, the budget spent equals the cells closed, cell for cell',
        fontsize=9,fontweight='bold',color=BLU)
ax.set_xlim(-0.1,8.0); ax.set_ylim(-1.4,5.4); ax.axis('off')
ax.set_title('Figure 10.  \u00a713.6 says E(X) is the prediction budget. The extension had E = 5 and had made exactly\n'
   'five predictions \u2014 the empty-cell list and the working queue were built independently and coincided.',
   fontsize=9.3,loc='left',pad=6)
plt.tight_layout(); plt.savefig('figs/fig10_budget.png',dpi=200); plt.close()
print("figs B written")