import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from collections import Counter

INK='#1a1a1a'; ACC='#b3341f'; BLU='#1f5fa9'; GRY='#8f8f8f'; LT='#e9e5dd'
plt.rcParams.update({'font.size':9,'axes.edgecolor':INK,'axes.labelcolor':INK,
    'text.color':INK,'xtick.color':INK,'ytick.color':INK,'axes.linewidth':0.8,
    'figure.facecolor':'white','savefig.facecolor':'white','font.family':'DejaVu Sans'})

CN,CE,CL,CK=3,3,1,3
L=[(n,l,k,q,e,f,g,S2)
   for n in range(1,CN+1) for l in range(0,min(n-1,CL)+1)
   for k in range(1,min(2*(2*l+1),CK)+1) for S2 in range(0,k+1)
   for q in range(0,k+1) for e in range(1,CE+1) for f in range(0,min(e-1,CL)+1)
   for g in range(0,min(q,2*(2*f+1))+1)]
S=set(L); NM=['n','\u2113','k','q','e','f','g','2S']

# ---------- FIG 1: the constraint tree ----------
fig,ax=plt.subplots(figsize=(8.2,2.9))
pos={'e':(0,0),'f':(1.3,0),'g':(2.6,0),'q':(3.9,0),'k':(5.2,0),'\u2113':(6.5,0),'n':(7.8,0),'2S':(5.2,-1.15)}
edges=[('e','f','f \u2264 e\u22121'),('f','g','g \u2264 2(2f+1)'),('g','q','g \u2264 q'),
       ('q','k','q \u2264 k'),('k','\u2113','k \u2264 2(2\u2113+1)'),('\u2113','n','\u2113 \u2264 n\u22121'),('k','2S','2S \u2264 k')]
ax.add_patch(FancyBboxPatch((-0.42,-0.42),3.45,0.85,boxstyle="round,pad=0.06",
    fc=LT,ec='none',zorder=0))
ax.add_patch(FancyBboxPatch((4.78,-1.55),3.45,1.98,boxstyle="round,pad=0.06",
    fc=LT,ec='none',zorder=0))
ax.text(1.3,0.72,'target end  B  =  (e, f, g)',ha='center',fontsize=8.5,color=GRY)
ax.text(6.5,0.72,'source end  A  =  (n, \u2113, k, 2S)',ha='center',fontsize=8.5,color=GRY)
for a,b,lab in edges:
    (x1,y1),(x2,y2)=pos[a],pos[b]
    ax.plot([x1,x2],[y1,y2],color=INK,lw=1.1,zorder=1)
    mx,my=(x1+x2)/2,(y1+y2)/2
    ax.text(mx,my+(0.16 if y1==y2 else 0),lab,ha='center',va='bottom',fontsize=7.4,
            color=GRY,rotation=0 if y1==y2 else 90)
for nme,(x,y) in pos.items():
    c=ACC if nme=='q' else 'white'
    tc='white' if nme=='q' else INK
    ax.scatter([x],[y],s=430,color=c,edgecolors=INK,linewidths=1.1,zorder=2)
    ax.text(x,y,nme,ha='center',va='center',fontsize=9.5,color=tc,zorder=3,fontweight='bold')
ax.text(3.9,-0.55,'the transfer\n(the coupling)',ha='center',fontsize=7.4,color=ACC)
ax.set_xlim(-0.8,8.5); ax.set_ylim(-1.9,1.15); ax.axis('off')
ax.set_title('Figure 1.  The constraint graph of \u039b is a tree: 8 nodes, 7 edges, treewidth 1',
             fontsize=9.5,pad=6,loc='left')
plt.tight_layout(); plt.savefig('figs/fig01_tree.png',dpi=200); plt.close()

# ---------- FIG 2: the cylinder ----------
Q=[0,1,2,3]
A=[len(set((c[0],c[1],c[2],c[7]) for c in L if c[3]==q)) for q in Q]
B=[len(set((c[4],c[5],c[6]) for c in L if c[3]==q)) for q in Q]
act=[sum(1 for c in L if c[3]==q) for q in Q]
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(8.2,3.2))
ax1.plot(Q,A,'o-',color=BLU,lw=1.6,ms=6,label='|A(q)|  source end')
ax1.plot(Q,B,'s-',color=ACC,lw=1.6,ms=6,label='|B(q)|  target end')
for q,a,b in zip(Q,A,B):
    ax1.annotate(str(a),(q,a),textcoords='offset points',xytext=(0,8),ha='center',fontsize=8,color=BLU)
    ax1.annotate(str(b),(q,b),textcoords='offset points',xytext=(0,-14),ha='center',fontsize=8,color=ACC)
ax1.set_xlabel('transfer  q'); ax1.set_ylabel('states at the end'); ax1.set_xticks(Q)
ax1.set_ylim(0,40); ax1.legend(frameon=False,fontsize=8,loc='center left')
ax1.set_title('(a) one end exhausts as the other fills',fontsize=8.8,loc='left')
bars=ax2.bar(Q,act,width=0.62,color=[GRY,GRY,ACC,GRY],edgecolor=INK,linewidth=0.8)
for q,v,a,b in zip(Q,act,A,B):
    ax2.text(q,v+9,str(v),ha='center',fontsize=8.5,fontweight='bold')
    ax2.text(q,v/2,f'{a}\u00d7{b}',ha='center',va='center',fontsize=7.6,color='white')
ax2.set_xlabel('transfer  q'); ax2.set_ylabel('cells in fibre'); ax2.set_xticks(Q)
ax2.set_ylim(0,400)
ax2.set_title('(b) the fibre profile peaks at the crossing',fontsize=8.8,loc='left')
ax2.text(3.42,300,'\u03a3 = 976',ha='right',fontsize=8.5,color=INK)
fig.suptitle('Figure 2.  \u039b as a cylinder over the transfer: base q, fibre A(q) \u00d7 B(q), profile 165\u00b7330\u00b7345\u00b7136',
             fontsize=9.5,x=0.012,ha='left',y=0.985)
plt.tight_layout(rect=[0,0,1,0.93]); plt.savefig('figs/fig02_cylinder.png',dpi=200); plt.close()

# ---------- FIG 3: rank profile ----------
lev=Counter(sum(c) for c in L); ranks=sorted(lev); vals=[lev[r] for r in ranks]
fig,ax=plt.subplots(figsize=(8.2,3.1))
cols=[ACC if v==max(vals) else GRY for v in vals]
ax.bar(ranks,vals,width=0.75,color=cols,edgecolor=INK,linewidth=0.7)
ax.set_xlabel('rank  (coordinate sum)'); ax.set_ylabel('cells'); ax.set_xticks(ranks)
ax.annotate('122 at rank 11',(11,122),textcoords='offset points',xytext=(14,6),
            fontsize=8.5,color=ACC,arrowprops=dict(arrowstyle='-',color=ACC,lw=0.8))
for r,v in [(4,5),(19,4)]:
    ax.annotate(str(v),(r,v),textcoords='offset points',xytext=(0,7),ha='center',
                fontsize=8.5,color=BLU,fontweight='bold')
ax.plot([4,19],[5,4],ls=':',color=BLU,lw=1.0)
ax.text(11.5,14,'one step from each end: 5 against 4  \u2014  the skew',
        ha='center',fontsize=8,color=BLU)
ax.set_ylim(0,142)
ax.set_title('Figure 3.  Rank profile: 18 levels, log-concave, and not symmetric  (F(\u22121) = 2)',
             fontsize=9.5,loc='left',pad=6)
plt.tight_layout(); plt.savefig('figs/fig03_rank.png',dpi=200); plt.close()

# ---------- FIG 4: Birkhoff generator poset ----------
def dn(c):
    o=[]
    for i in range(8):
        d=list(c); d[i]-=1
        if tuple(d) in S: o.append(tuple(d))
    return o
ji=sorted([c for c in L if len(dn(c))==1],key=lambda c:(sum(c),c))
base=min(L)
leq=lambda a,b: all(p<=q for p,q in zip(a,b))
cov=[(a,b) for a in ji for b in ji if a!=b and leq(a,b)
     and not any(c!=a and c!=b and leq(a,c) and leq(c,b) for c in ji)]
def lbl(c):
    d=[f"{NM[i]}={c[i]}" for i in range(8) if c[i]!=base[i]]
    return ",".join(d) if d else 'bottom'
lvl={}
for c in ji: lvl.setdefault(sum(c),[]).append(c)
posn={}
for r in sorted(lvl):
    row=sorted(lvl[r]); n_=len(row)
    for i,c in enumerate(row): posn[c]=((i-(n_-1)/2)*2.0, r-min(lvl))
fig,ax=plt.subplots(figsize=(8.2,4.4))
for a,b in cov:
    x1,y1=posn[a]; x2,y2=posn[b]
    ax.plot([x1,x2],[y1,y2],color=GRY,lw=0.9,zorder=1)
for c,(x,y) in posn.items():
    ax.scatter([x],[y],s=70,color='white',edgecolors=INK,linewidths=1.0,zorder=2)
    ax.text(x,y-0.30,lbl(c),ha='center',va='top',fontsize=6.9,color=INK,zorder=3)
ax.set_xlim(-6.2,6.2); ax.set_ylim(-1.0,max(y for _,y in posn.values())+0.7)
ax.axis('off')
ax.set_title('Figure 4.  The 17 join-irreducibles and their 20 covering relations.\n'
             'All 976 down-sets of this poset are precisely the 976 cells \u2014 a 57-fold compression.',
             fontsize=9.5,loc='left',pad=6)
plt.tight_layout(); plt.savefig('figs/fig04_birkhoff.png',dpi=200); plt.close()

# ---------- FIG 5: duality convention ----------
mx=tuple(max(c[i] for c in L) for i in range(8))
mn=tuple(min(c[i] for c in L) for i in range(8))
survA=[c for c in L if tuple(mx[i]-c[i] for i in range(8)) in S]
survB=[c for c in L if tuple(mx[i]+mn[i]-c[i] for i in range(8)) in S]
cA=Counter(sum(c) for c in survA); cB=Counter(sum(c) for c in survB)
rr=sorted(set(list(cA)+list(cB)))
fig,ax=plt.subplots(figsize=(8.2,3.1))
w=0.4
ax.bar([r-w/2 for r in rr],[cB.get(r,0) for r in rr],width=w,color=GRY,
       edgecolor=INK,linewidth=0.6,label='\u03c3(x) = max + min \u2212 x   \u2192  112 survivors, mixed rank')
ax.bar([r+w/2 for r in rr],[cA.get(r,0) for r in rr],width=w,color=ACC,
       edgecolor=INK,linewidth=0.6,label='\u03c3(x) = max \u2212 x   \u2192  8 survivors, all even rank')
ax.set_xlabel('rank'); ax.set_ylabel('cells whose \u03c3-image lands in \u039b'); ax.set_xticks(rr)
ax.legend(frameon=False,fontsize=8.2,loc='upper right')
ax.set_title('Figure 5.  The duality convention resolved by computation, not convention.\n'
             'Only max \u2212 x reproduces the stated count; its survivors are symmetric about rank 10, contributing +8.',
             fontsize=9.5,loc='left',pad=6)
plt.tight_layout(); plt.savefig('figs/fig05_duality.png',dpi=200); plt.close()
print("figs A written")