import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
INK="#1a1a1a"; ACC="#8c2d19"; ACC2="#2f5d7c"; MUT="#6b6b6b"
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8,'axes.edgecolor':MUT,
    'axes.labelcolor':INK,'xtick.color':MUT,'ytick.color':MUT,'axes.linewidth':0.6,
    'xtick.labelsize':7,'ytick.labelsize':7,'legend.frameon':False})

# ---- f26 : the step law ----
fig,ax=plt.subplots(1,2,figsize=(6.6,2.5))
d=np.array([2,3,4,5]); step=np.array([1,2,4,8]); meas=[True,True,True,True]
ax[0].plot(d,2.0**(d-2),'-',color=MUT,lw=1.0,zorder=1,label='$2^{\\,d-2}$')
ax[0].scatter(d[:3],step[:3],s=42,color=ACC,zorder=3,label='exhaustive')
ax[0].scatter([5],[8],s=42,facecolors='none',edgecolors=ACC,linewidths=1.2,zorder=3,
              label='by construction')
for x,y in zip(d,step): ax[0].annotate(str(y),(x,y),textcoords="offset points",xytext=(6,-2),
              fontsize=7,color=INK)
ax[0].set_yscale('log',base=2); ax[0].set_xticks(d)
ax[0].set_xlabel('dimension $d$'); ax[0].set_ylabel('growth step $f(d)$')
ax[0].set_title('the step is $2^{\\,d-2}$',fontsize=8.5,color=INK,pad=6)
ax[0].legend(fontsize=6.5,loc='upper left')
box=2.0**d; keep=3*2.0**(d-2)
ax[1].bar(d-0.17,box,width=0.34,color="#dfe7ee",edgecolor=MUT,lw=0.5,label='the box $2^d$')
ax[1].bar(d+0.17,keep,width=0.34,color=ACC2,edgecolor=MUT,lw=0.5,label='largest reorderable')
for x,y in zip(d,keep): ax[1].annotate("%d"%y,(x+0.17,y),textcoords="offset points",
              xytext=(0,3),ha='center',fontsize=6.5,color=INK)
ax[1].set_xticks(d); ax[1].set_xlabel('dimension $d$'); ax[1].set_ylabel('cells')
ax[1].set_title('and the ratio is exactly $3/4$',fontsize=8.5,color=INK,pad=6)
ax[1].legend(fontsize=6.5,loc='upper left')
for a in ax: a.spines['top'].set_visible(False); a.spines['right'].set_visible(False)
plt.tight_layout(); plt.savefig('fig/f26_steplaw.png',dpi=300,bbox_inches='tight'); plt.close()

# ---- f27 : the arity boundary ----
fig,ax=plt.subplots(1,2,figsize=(6.6,2.5))
ar=[2,3,4,5]; dist=[2,14,141,129]; ok=[2,14,114,121]
frac=[o/t for o,t in zip(ok,dist)]
ax[0].bar(ar,[1]*4,width=0.6,color="#f0e4e0",edgecolor=MUT,lw=0.5)
ax[0].bar(ar,frac,width=0.6,color=ACC2,edgecolor=MUT,lw=0.5)
for x,f,o,t in zip(ar,frac,ok,dist):
    ax[0].annotate("%d/%d"%(o,t),(x,f),textcoords="offset points",xytext=(0,3),
                   ha='center',fontsize=6.5,color=INK)
ax[0].axvline(3.5,color=ACC,lw=1.0,ls='--')
ax[0].annotate('the boundary',(3.5,0.30),textcoords="offset points",xytext=(5,0),
               fontsize=7,color=ACC,rotation=90,va='center')
ax[0].set_xticks(ar); ax[0].set_ylim(0,1.15)
ax[0].set_xlabel('constraint arity'); ax[0].set_ylabel('fraction 2-SAT expressible')
ax[0].set_title('the language leaves 2-SAT at arity 4',fontsize=8.5,color=INK,pad=6)
dd=[3,4,5,6]; a2=[0.620,0.500,0.376,0.262]; a3=[0.380,0.401,0.386,0.355]
a4=[0.000,0.098,0.238,0.383]
ax[1].stackplot(dd,a2,a3,a4,colors=[ACC2,"#9db8c9","#f0e4e0"],edgecolor=MUT,lw=0.4)
ax[1].plot(dd,a2,color=ACC2,lw=0)
ax[1].annotate('arity 2',(3.15,0.30),fontsize=7,color='white')
ax[1].annotate('arity 3',(3.15,0.80),fontsize=7,color=INK)
ax[1].annotate('arity $\\geq$ 4',(5.1,0.88),fontsize=7,color=INK)
ax[1].set_xticks(dd); ax[1].set_xlim(3,6); ax[1].set_ylim(0,1)
ax[1].set_xlabel('dimension $d$'); ax[1].set_ylabel('share of constraints')
ax[1].set_title('and higher arity takes over with $d$',fontsize=8.5,color=INK,pad=6)
for a in ax: a.spines['top'].set_visible(False); a.spines['right'].set_visible(False)
plt.tight_layout(); plt.savefig('fig/f27_arity.png',dpi=300,bbox_inches='tight'); plt.close()

# ---- f28 : the mathematics index, closed ----
fig,ax=plt.subplots(figsize=(6.6,2.9))
K=['definition','mechanism','formula','theorem','law','method','measurement']
L=['order','combin','analysis','complexity','physics','algeom']
cells={('definition','order'):1,('definition','combin'):1,('mechanism','order'):1,
 ('formula','combin'):2,('formula','analysis'):3,('formula','physics'):1,
 ('theorem','order'):5,('theorem','combin'):3,('theorem','analysis'):2,
 ('law','complexity'):1,('method','order'):1,('method','combin'):1,
 ('method','analysis'):1,('measurement','combin'):2,('measurement','physics'):1,
 ('measurement','algeom'):1}
M=np.full((len(K),len(L)),np.nan)
for (k,l),v in cells.items(): M[K.index(k)][L.index(l)]=v
im=ax.imshow(M,cmap='Blues',vmin=0,vmax=5.5,aspect='auto')
for i in range(len(K)):
    for j in range(len(L)):
        if not np.isnan(M[i][j]):
            ax.text(j,i,"%d"%M[i][j],ha='center',va='center',fontsize=7.5,
                    color='white' if M[i][j]>=3 else INK)
        else:
            ax.text(j,i,"·",ha='center',va='center',fontsize=8,color="#cccccc")
ax.set_xticks(range(len(L))); ax.set_xticklabels(L,fontsize=7,rotation=25,ha='right')
ax.set_yticks(range(len(K))); ax.set_yticklabels(K,fontsize=7)
ax.set_title('the mathematics as an index — 32 elements, 16 fibres, E = 0 in every one',
             fontsize=8.5,color=INK,pad=8)
for s in ax.spines.values(): s.set_visible(False)
ax.set_xticks(np.arange(-.5,len(L),1),minor=True)
ax.set_yticks(np.arange(-.5,len(K),1),minor=True)
ax.grid(which='minor',color='white',lw=1.2); ax.tick_params(which='minor',length=0)
plt.tight_layout(); plt.savefig('fig/f28_mathindex.png',dpi=300,bbox_inches='tight'); plt.close()
import os
for f in ['f26_steplaw','f27_arity','f28_mathindex']:
    p='fig/%s.png'%f
    print("  %-22s %7d bytes"%(f,os.path.getsize(p)))