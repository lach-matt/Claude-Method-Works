import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np, itertools, math
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams.update({'font.family':'serif','font.serif':['FreeSerif','DejaVu Serif'],
 'font.size':8.5,'axes.linewidth':.7,'figure.dpi':300,'savefig.dpi':300,
 'axes.spines.top':False,'axes.spines.right':False})
INK='#1a1a1a';ACC='#8c2f39';MUT='#9a9a9a';BLU='#3d6b8c';W=6.4;FD='fig/'
def R(c):
    S=set(c)
    while True:
        n={tuple(map(max,zip(x,y))) for x in S for y in S}|{tuple(map(min,zip(x,y))) for x in S for y in S}
        if n<=S: return S
        S|=n
def E(c): return len(R(c))-len(set(c))

# --- f9 : the modality flow ------------------------------------------
f,ax=plt.subplots(figsize=(W,2.5)); ax.axis('off')
pos={'forbidden':(0,0),'unknown':(3,0),'realisable':(6,0)}
for n,(x,y) in pos.items():
    ax.add_patch(plt.Circle((x,y),.85,fc='none',ec=INK,lw=1))
    ax.text(x,y,n,ha='center',va='center',fontsize=8.5)
A=dict(arrowstyle='-|>',lw=1.1,color=ACC,shrinkA=26,shrinkB=26)
ax.annotate('',xy=pos['realisable'],xytext=pos['unknown'],arrowprops=A)
ax.text(4.5,.34,'sequencing',ha='center',fontsize=7.5,color=ACC)
ax.annotate('',xy=pos['forbidden'],xytext=pos['unknown'],arrowprops=A)
ax.text(1.5,.34,'saturation',ha='center',fontsize=7.5,color=ACC)
ax.annotate('',xy=(1.5,-.95),xytext=(6,-.95),
  arrowprops=dict(arrowstyle='-|>',lw=1.1,color=BLU,connectionstyle='arc3,rad=.22'))
ax.text(3.6,-1.62,'fixation / loss',ha='center',fontsize=7.5,color=BLU)
ax.set_xlim(-1.4,7.4);ax.set_ylim(-2.2,1.2)
ax.set_title('E does not partition into three quantities. It is one quantity in three states.',
             fontsize=8.5,loc='left')
f.tight_layout();f.savefig(FD+'f9_flow.pdf');plt.close(f)

# --- f10 : four-gamete sensitivity -----------------------------------
def fg(hs,m):
    return any(len({(h[i],h[j]) for h in hs})<4 for i,j in itertools.combinations(range(m),2))
ms=[2,3,4];sens=[]
for m in ms:
    full=list(itertools.product([0,1],repeat=m));a=b=0
    for k in range(2,2**m+1):
        for s in itertools.combinations(full,k):
            if fg(s,m):
                a+=1; b+= (E(s)>0)
    sens.append(b/a)
f,ax=plt.subplots(figsize=(W,2.4))
ax.plot(ms,[s*100 for s in sens],'o-',color=INK,ms=5,lw=1.2)
ax.axhline(100,color=MUT,ls=':',lw=.8)
for x,y in zip(ms,sens): ax.annotate(f'{y:.1%}',(x,y*100),textcoords='offset points',
    xytext=(0,-14),ha='center',fontsize=7.5,color=ACC)
ax.set_xticks(ms);ax.set_xlabel('sites m');ax.set_ylabel('% of four-gamete failures detected')
ax.set_ylim(0,112)
ax.set_title('E against the classical four-gamete test: neither sound nor complete',fontsize=8.5,loc='left')
f.tight_layout();f.savefig(FD+'f10_fourgamete.pdf');plt.close(f)

# --- f11 : the shape of the measurements -----------------------------
X={(0,0,0,0),(0,0,1,0),(0,1,0,0),(0,1,0,1),(0,1,1,0),(1,0,0,0),(1,0,1,0),(1,1,0,0),(1,1,0,1),(1,1,1,0)}
RX=R(X); gaps=RX-X
allc=set(itertools.product([0,1],repeat=4)); unreach=allc-RX
f,axs=plt.subplots(1,2,figsize=(W,2.9),subplot_kw={'projection':'3d'})
for ax,(el,az) in zip(axs,[(20,-58),(16,-118)]):
    for S,c,s,lab in [(X,INK,42,'measured (10)'),(gaps,ACC,78,'admitted & absent (2)'),
                      (unreach,MUT,30,'outside ℛ (4)')]:
        P=np.array(sorted(S),float)
        if len(P): ax.scatter(P[:,0],P[:,1],P[:,2]+P[:,3]*.30,c=c,s=s,
            marker='o' if c!=ACC else '*',depthshade=False,edgecolors='none',label=lab)
    ax.view_init(el,az);ax.set_xticks([0,1]);ax.set_yticks([0,1]);ax.set_zticks([0,1])
    ax.set_xlabel('b bound',fontsize=7,labelpad=-9);ax.set_ylabel('c content',fontsize=7,labelpad=-9)
    ax.set_zlabel('o sorted (+t)',fontsize=7,labelpad=-9);ax.tick_params(labelsize=6,pad=-3)
axs[0].legend(frameon=False,fontsize=7,loc='upper left',bbox_to_anchor=(-.16,1.06))
f.suptitle('E(session) = 2 at density 0.625.  Synchronic 8/8 measured, diachronic 2/8.',
           fontsize=8.5,x=.02,ha='left')
f.tight_layout(rect=[0,0,1,.93]);f.savefig(FD+'f11_shape.pdf');plt.close(f)

# --- f12 : the law tested --------------------------------------------
lab=['assembly\ngaps','audit\ndefects','variant\noccupancy','chromosome\n(chr,pos)',
     'snarl\norientation','genome\nsequence','pangenome\nalleles']
Ev=[150630700,3,9264809496,2886684296,2100,9264809496,12]
mv=[1,1,1,0,0,0,0]
f,ax=plt.subplots(figsize=(W,2.7))
ax.bar(range(7),Ev,color=[ACC if m else MUT for m in mv],width=.6)
ax.set_yscale('log');ax.set_xticks(range(7));ax.set_xticklabels(lab,fontsize=7)
ax.set_ylabel('E(X)')
for i,(v,m) in enumerate(zip(Ev,mv)):
    ax.text(i,v*2.2,'closed' if m else 'unmoved',ha='center',fontsize=7,
            color=ACC if m else MUT)
ax.set_ylim(1,1e12)
ax.set_title('Larger E, less movement. The law fails 4 of 7 — decisively at the chromosome index.',
             fontsize=8.5,loc='left')
f.tight_layout();f.savefig(FD+'f12_law.pdf');plt.close(f)

# --- f13 : dominance modes -------------------------------------------
modes={'complete dominant':[0,1,1],'complete recessive':[0,0,1],'additive':[0,1,2],
       'partial dominance':[0,2,3],'OVERdominance':[0,2,1],'UNDERdominance':[2,0,2]}
f,axs=plt.subplots(1,6,figsize=(W,1.9),sharey=True)
for ax,(n,v) in zip(axs,modes.items()):
    e=E([(k,x) for k,x in enumerate(v)])
    ax.plot([0,1,2],v,'o-',color=ACC if e else INK,ms=5,lw=1.4)
    ax.set_title(f'{n}\nE = {e}',fontsize=7,color=ACC if e else INK)
    ax.set_xticks([0,1,2]);ax.set_xlabel('dosage k',fontsize=7);ax.tick_params(labelsize=6.5)
axs[0].set_ylabel('phenotype',fontsize=7.5)
f.suptitle('Every monotone dominance mode closes. Only the heterozygote-extreme modes open.',
           fontsize=8.5,x=.01,ha='left')
f.tight_layout(rect=[0,0,1,.86]);f.savefig(FD+'f13_dominance.pdf');plt.close(f)

# --- f14 : Λ_G in 3D --------------------------------------------------
A=[2,2,2,3,3,4,5,6,8,10]
S=[(u,a) for u,Au in enumerate(A) for a in range(Au)]
T=[(k,e) for k in range(3) for e in range(k+1)]
LG=[(u,a,k,e) for (u,a) in S for (k,e) in T]
cell={c:(c[0],c[1],c[2]+c[3]*.26) for c in LG}
ed=[(cell[c],cell[n]) for c in LG for d in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    for n in [(c[0]+d[0],c[1]+d[1],c[2]+d[2],c[3]+d[3])] if n in cell]
CM={0:'#c9d6df',1:'#5b8ca8',2:'#8c2f39'}
f=plt.figure(figsize=(W,4.6))
for i,(el,az,t) in enumerate([(20,-62,'(a) the staircase extruded along dosage'),
                              (74,-90,'(b) from above — the (u,a) staircase'),
                              (6,-90,'(c) along a — the monotone bound A(u)'),
                              (12,-6,'(d) along u — the triangle e ≤ k')]):
    ax=f.add_subplot(2,2,i+1,projection='3d')
    for p,q in ed: ax.plot([p[0],q[0]],[p[1],q[1]],[p[2],q[2]],color='#c0c0c0',lw=.25,alpha=.5)
    ax.scatter([c[0] for c in LG],[c[1] for c in LG],[c[2]+c[3]*.26 for c in LG],
               c=[CM[c[3]] for c in LG],s=10,edgecolors='none')
    ax.view_init(el,az);ax.set_title(t,fontsize=7.5,loc='left',pad=-2)
    ax.set_xlabel('u',fontsize=7,labelpad=-9);ax.set_ylabel('a',fontsize=7,labelpad=-9)
    ax.set_zlabel('k (+e)',fontsize=7,labelpad=-9);ax.tick_params(labelsize=5.5,pad=-3)
    ax.set_box_aspect((2,1.5,1))
h=[plt.Line2D([],[],marker='o',ls='',color=CM[i],label=f'e = {i}') for i in range(3)]
f.legend(handles=h,loc='lower center',ncol=3,frameon=False,fontsize=7.5,bbox_to_anchor=(.5,0))
f.suptitle('Λ_G — E = 0 at density 0.1531. Shown: 270 cells, A(u) = '+str(A),fontsize=8.5,x=.02,ha='left')
f.tight_layout(rect=[0,.035,1,.95]);f.savefig(FD+'f14_lambdaG.pdf');plt.close(f)

# --- f15 : epistasis opens it ----------------------------------------
T2=[(k1,e1,k2,e2) for k1 in range(3) for e1 in range(k1+1) for k2 in range(3) for e2 in range(k2+1)]
cases=[('independent',lambda c:False),('complementary\nlethal',lambda c:c[0]==0 and c[2]==0),
       ('synthetic\nlethal',lambda c:c[0]==1 and c[2]==1),
       ('heterozygote\nadvantage',lambda c:not(c[0]==1 or c[2]==1))]
names=[];Es=[];keeps=[]
for n,rm in cases:
    k=[c for c in T2 if not rm(c)];names.append(n);Es.append(E(k));keeps.append(len(k))
f,ax=plt.subplots(figsize=(W,2.5))
ax.bar(range(4),Es,color=[MUT]+[ACC]*3,width=.55)
for i,(e,k) in enumerate(zip(Es,keeps)):
    ax.text(i,e+.28,f'E = {e}\n{k}/36 cells',ha='center',fontsize=7.5)
ax.set_xticks(range(4));ax.set_xticklabels(names,fontsize=7.5);ax.set_ylabel('E')
ax.set_ylim(0,12.5)
ax.set_title('Λ_G is closed because it contains no epistasis. Every interaction is a cell removal.',
             fontsize=8.5,loc='left')
f.tight_layout();f.savefig(FD+'f15_epistasis.pdf');plt.close(f)
print('f9–f15 written; four-gamete sensitivities:',[f'{s:.1%}' for s in sens])