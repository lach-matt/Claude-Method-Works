import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter
INK='#1a1a1a'; ACC='#b3341f'; BLU='#1f5fa9'; GRY='#8f8f8f'
plt.rcParams.update({'font.size':9,'axes.edgecolor':INK,'axes.labelcolor':INK,
 'text.color':INK,'xtick.color':INK,'ytick.color':INK,'axes.linewidth':0.8,
 'figure.facecolor':'white','savefig.facecolor':'white','font.family':'DejaVu Sans'})
CN,CE,CL,CK=3,3,1,3
L=[(n,l,k,q,e,f,g,S2)
   for n in range(1,CN+1) for l in range(0,min(n-1,CL)+1)
   for k in range(1,min(2*(2*l+1),CK)+1) for S2 in range(0,k+1)
   for q in range(0,k+1) for e in range(1,CE+1) for f in range(0,min(e-1,CL)+1)
   for g in range(0,min(q,2*(2*f+1))+1)]
S=set(L); NM=['n','\u2113','k','q','e','f','g','2S']; base=min(L)

# FIG 3 — rank profile
lev=Counter(sum(c) for c in L); ranks=sorted(lev); vals=[lev[r] for r in ranks]
fig,ax=plt.subplots(figsize=(8.2,3.1))
ax.bar(ranks,vals,width=0.75,color=[ACC if v==max(vals) else GRY for v in vals],
       edgecolor=INK,linewidth=0.7)
ax.set_xlabel('rank  (coordinate sum)'); ax.set_ylabel('cells'); ax.set_xticks(ranks)
ax.annotate('122 at rank 11',(11,122),textcoords='offset points',xytext=(14,6),
            fontsize=8.5,color=ACC,arrowprops=dict(arrowstyle='-',color=ACC,lw=0.8))
for r,v in [(4,5),(19,4)]:
    ax.annotate(str(v),(r,v),textcoords='offset points',xytext=(0,7),ha='center',
                fontsize=8.5,color=BLU,fontweight='bold')
ax.plot([4,19],[5,4],ls=':',color=BLU,lw=1.0)
ax.text(11.5,14,'one step from each end: 5 against 4  \u2014  the skew',ha='center',fontsize=8,color=BLU)
ax.set_ylim(0,142)
ax.set_title('Figure 3.  Rank profile: 18 levels, log-concave, and not symmetric  (F(\u22121) = 2)',
             fontsize=9.5,loc='left',pad=6)
plt.tight_layout(); plt.savefig('build/figures/Indexing_Electromagnetism_fig03.png',dpi=200); plt.close()

# FIG 4 — Birkhoff generator poset
def dn(c): return [tuple(d) for d in ([*c[:i],c[i]-1,*c[i+1:]] for i in range(8)) if tuple(d) in S]
ji=sorted([c for c in L if len(dn(c))==1],key=lambda c:(sum(c),c))
leq=lambda a,b: all(p<=q for p,q in zip(a,b))
cov=[(a,b) for a in ji for b in ji if a!=b and leq(a,b)
     and not any(c!=a and c!=b and leq(a,c) and leq(c,b) for c in ji)]
def lbl(c):
    d=[f"{NM[i]}={c[i]}" for i in range(8) if c[i]!=base[i]]
    return ", ".join(d) if d else 'bottom'
lvl={}
for c in ji: lvl.setdefault(sum(c),[]).append(c)
mnr=min(lvl); posn={}
for r in sorted(lvl):
    row=sorted(lvl[r]); n_=len(row)
    for i,c in enumerate(row): posn[c]=((i-(n_-1)/2)*2.55,(r-mnr)*1.0)
fig,ax=plt.subplots(figsize=(9.6,4.8))
for a,b in cov:
    x1,y1=posn[a]; x2,y2=posn[b]; ax.plot([x1,x2],[y1,y2],color=GRY,lw=0.9,zorder=1)
for idx,(c,(x,y)) in enumerate(sorted(posn.items(),key=lambda t:(t[1][1],t[1][0]))):
    ax.scatter([x],[y],s=78,color='white',edgecolors=INK,linewidths=1.0,zorder=2)
    up=(idx%2==0)
    ax.text(x,y+(0.26 if up else -0.26),lbl(c),ha='center',
            va='bottom' if up else 'top',fontsize=7.0,color=INK,zorder=3)
xs=[p[0] for p in posn.values()]; ys=[p[1] for p in posn.values()]
ax.set_xlim(min(xs)-2.0,max(xs)+2.0); ax.set_ylim(min(ys)-0.85,max(ys)+0.85); ax.axis('off')
ax.set_title('Figure 4.  The 17 join-irreducibles and their 20 covering relations.\n'
 'Every one of the 976 cells is a down-set of this poset, and every down-set is a cell \u2014 a 57-fold compression.\n'
 'The covers are the constraints made visible: a target subshell requires its shell; you may remove what you have.',
 fontsize=9.3,loc='left',pad=8)
plt.tight_layout(); plt.savefig('build/figures/Indexing_Electromagnetism_fig04.png',dpi=200); plt.close()
print("regenerated fig03 (rank, %d levels) and fig04 (%d JI, %d covers)"%(len(lev),len(ji),len(cov)))