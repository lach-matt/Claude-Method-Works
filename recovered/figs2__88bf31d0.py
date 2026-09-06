import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
plt.rcParams.update({"figure.dpi":300,"savefig.dpi":300,"font.family":"DejaVu Serif",
 "font.size":8.5,"axes.spines.top":False,"axes.spines.right":False,"axes.grid":True,
 "grid.alpha":0.18,"grid.linewidth":0.5,"axes.titlesize":9.5,"axes.titleweight":"bold"})
INK,ACC,MUT,PALE="#1a1a1a","#b3472a","#5b6b73","#c8cdd0"
def save(f,n): f.tight_layout(); f.savefig(f"fig/OMTT_{n}.png",bbox_inches="tight",facecolor="white"); plt.close(f)

# fig 9 — pushback
med=[3234,2938,1827,1246,827,571,392,335,353,434,499,514,813,1102,1426,1421,1174,1555]
mx =[3234,3859,4043,4064,4225,2879,1973,1308,1042,1478,2439,3063,3775,5091,4827,4406,3776,1555]
rk=list(range(3,21))
f,ax=plt.subplots(figsize=(5.6,3.0))
ax.fill_between(rk,med,mx,color=PALE,alpha=.55,label="median to maximum")
ax.plot(rk,med,"o-",color=INK,lw=1.6,ms=4,label="median pushback")
ax.axhline(16,color=ACC,lw=1.3,ls="--")
ax.annotate("floor 16 — no cell is free",(3.3,16),textcoords="offset points",
            xytext=(4,10),fontsize=7.5,color=ACC)
ax.set_xlabel("rank"); ax.set_ylabel("producing pairs"); ax.set_xticks(rk[::2])
ax.legend(frameon=False,fontsize=7.5)
ax.set_title("Resistance to deletion is weakest where the index is widest")
save(f,"fig09_pushback")

# fig 10 — the step law
caps=["(3,3,1,3)","(3,3,1,4)","(4,4,1,3)","(4,4,1,4)","(5,5,1,3)"]
step=[4,4,9,9,16]; ji=[17,21,19,23,21]
f,(a1,a2)=plt.subplots(1,2,figsize=(7.2,2.8))
x=np.arange(5)
a1.bar(x,step,0.55,color=INK)
for i,v in enumerate(step): a1.text(i,v+.35,str(v),ha="center",fontsize=8)
a1.set_xticks(x); a1.set_xticklabels(caps,rotation=20,ha="right")
a1.set_ylabel("cells"); a1.set_ylim(0,19)
a1.set_title("The step — the minimum that can leave")
a2.bar(x-0.19,ji,0.38,color=MUT,label="join-irreducibles")
a2.bar(x+0.19,ji,0.38,color=PALE,label="meet-irreducibles")
a2.plot(x,[0]*5,"D",color=ACC,ms=6,label="doubly irreducible")
a2.set_xticks(x); a2.set_xticklabels(caps,rotation=20,ha="right")
a2.legend(frameon=False,fontsize=7); a2.set_ylabel("cells")
a2.set_title("No cell is irreducible on both sides")
save(f,"fig10_step")

# fig 11 — the tick
f,(a1,a2)=plt.subplots(1,2,figsize=(7.2,2.7))
a1.bar([0,1,2],[389,540,240],0.5,color=[ACC,INK,MUT])
for i,v in zip([0,1,2],[389,540,240]): a1.text(i,v+12,str(v),ha="center",fontsize=8)
a1.set_xticks([0,1,2]); a1.set_xlabel("tick, k − g"); a1.set_ylabel("cells")
a1.annotate("reversible",(0,389),textcoords="offset points",xytext=(0,32),
            ha="center",fontsize=7.5,color=ACC)
a1.set_title("The clock's tick")
lbl=["not removed\n(k > q)","removed, not placed\n(q > g)"]
a2.barh([0,1],[430,430],0.45,color=[INK,ACC])
for i,v in enumerate([430,430]): a2.text(v+8,i,str(v),va="center",fontsize=8.5)
a2.set_yticks([0,1]); a2.set_yticklabels(lbl); a2.set_xlim(0,520)
a2.set_xlabel("cells"); a2.invert_yaxis(); a2.grid(axis="y",alpha=0)
a2.set_title("Two sources of irreversibility, exactly balanced")
save(f,"fig11_tick")

# fig 12 — the two indices
f,ax=plt.subplots(figsize=(5.4,3.2))
ax.add_patch(plt.Circle((-0.42,0),0.78,fc=INK,alpha=.20,ec=INK,lw=1.2))
ax.add_patch(plt.Circle(( 0.42,0),0.78,fc=ACC,alpha=.20,ec=ACC,lw=1.2))
ax.text(-0.86,0.32,"Λ₉\n1,654\nE = 0",ha="center",fontsize=8.5)
ax.text( 0.86,0.32,"rev(Λ₉)\n1,654\nE = 0",ha="center",fontsize=8.5)
ax.text(0,0,"389\nE = 0\ngroupoid",ha="center",va="center",fontsize=9,weight="bold")
ax.text(0,-1.02,"g = q = k",ha="center",fontsize=8,color=MUT,style="italic")
ax.text(0,1.16,"union: 2,919 cells · 830,625 failing pairs · E = 2,857 — not closed",
        ha="center",fontsize=8,color=ACC)
ax.set_xlim(-1.9,1.9); ax.set_ylim(-1.3,1.45); ax.axis("off")
ax.set_title("Three positions exist; the fourth does not",pad=6)
save(f,"fig12_two_indices")
print("done")