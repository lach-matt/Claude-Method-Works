import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9,"axes.linewidth":0.8})

# ---------- shared data (identical to Appendix A.1) ----------
X = {1:{0,1,2},2:{1,2,4,6},3:{3,4,5,6,8},4:{3,5,6,7,8,10},
     5:{3,5,6,7,8,9,10,12,14},6:{3,4,5,6,7,8,9,10,11,12,13,14,16},
     7:{5,6,7,8,9,10,11,12,13,14,15,16},8:{5,6,7,8,9,10,11,12,13,14,15,16},
     9:{8,9,10,11,12,13,14,15,16,17,18,20,22}}
cells={(z,n) for z,S in X.items() for n in S}
AZ=sorted({z for z,_ in cells}); AN=sorted({n for _,n in cells})
pZ=lambda n:max((z for z,m in cells if m<=n),default=-1)
pN=lambda z:max((m for y,m in cells if y<=z),default=-1)
R={(z,n) for z in AZ for n in AN if z<=pZ(n) and n<=pN(z)}
holes=sorted(R-cells)
sym={1:"H",2:"He",3:"Li",4:"Be",5:"B",6:"C",7:"N",8:"O",9:"F"}
esc=[(9,19),(9,21)]           # value-set escapes 28F,30F
declined=[(9,7)]              # 16F, R5 window decline

# ---------- Figure 1: the chart, its holes, and the closure staircase ----------
fig,ax=plt.subplots(figsize=(9.2,4.2),dpi=200)
for (z,n) in cells:
    ax.add_patch(Rectangle((n-.5,z-.5),1,1,facecolor="#2b3a55",edgecolor="white",lw=.6))
for (z,n) in holes:
    ax.add_patch(Rectangle((n-.5,z-.5),1,1,facecolor="#c0392b",edgecolor="white",lw=.6))
    ax.text(n,z,f"$^{{{z+n}}}$"+sym[z],ha="center",va="center",color="white",fontsize=7.5,fontweight="bold")
for (z,n) in esc:
    ax.add_patch(Rectangle((n-.5,z-.5),1,1,facecolor="none",edgecolor="#e67e22",lw=1.4,hatch="///"))
    ax.text(n,z-0.02,f"$^{{{z+n}}}$"+sym[z],ha="center",va="center",color="#b35c0e",fontsize=7)
for (z,n) in declined:
    ax.add_patch(Rectangle((n-.5,z-.5),1,1,facecolor="none",edgecolor="#7f8c8d",lw=1.2,ls="--"))
    ax.text(n,z,"R5",ha="center",va="center",color="#7f8c8d",fontsize=7)
# closure boundary of R as a staircase outline
for (z,n) in R:
    for dz,dn,x0,y0,x1,y1 in [(0,1,n+.5,z-.5,n+.5,z+.5),(0,-1,n-.5,z-.5,n-.5,z+.5),
                              (1,0,n-.5,z+.5,n+.5,z+.5),(-1,0,n-.5,z-.5,n+.5,z-.5)]:
        if (z+dz,n+dn) not in R:
            ax.plot([x0,x1],[y0,y1],color="#111111",lw=1.6,solid_capstyle="projecting",zorder=5)
ax.set_xlim(-1.2,23.2); ax.set_ylim(0.3,9.9)
ax.set_xticks(range(0,23,2)); ax.set_yticks(AZ); ax.set_yticklabels([f"{z} ({sym[z]})" for z in AZ])
ax.set_xlabel("N (neutrons)"); ax.set_ylabel("Z (protons)")
ax.set_aspect("equal")
from matplotlib.lines import Line2D
leg=[Rectangle((0,0),1,1,facecolor="#2b3a55"),Rectangle((0,0),1,1,facecolor="#c0392b"),
     Rectangle((0,0),1,1,facecolor="none",edgecolor="#e67e22",hatch="///"),
     Rectangle((0,0),1,1,facecolor="none",edgecolor="#7f8c8d",ls="--"),
     Line2D([0],[0],color="#111111",lw=1.6)]
ax.legend(leg,["measured X (77 bound cells)","holes ℛ(X)∖X (E = 9)",
               "value-set escapes (Â$_N$ gaps: N = 19, 21)","declined: window (R5)",
               "boundary of ℛ(X) = the drawn chart (86 cells, E = 0)"],
          loc="lower right",fontsize=7.5,framealpha=.95)
ax.set_title("The measured nuclide chart (Z ≤ 9) and its closure",fontsize=10)
plt.tight_layout(); plt.savefig("/home/claude/fig1_chart_closure.png",bbox_inches="tight"); plt.close()

# ---------- Figure 2: 4He* exit-channel ladder ----------
# thresholds above 4He g.s. (recalled evaluated values; flagged in caption)
Ttp, Thn, Edd, Egamma = 19.815, 20.578, 23.847, 23.847
fig,ax=plt.subplots(figsize=(5.6,4.6),dpi=200)
def level(y,x0,x1,label,side="right",color="#2b3a55",lw=2):
    ax.hlines(y,x0,x1,color=color,lw=lw)
    ax.text(x1+.03 if side=="right" else x0-.03,y,label,va="center",
            ha="left" if side=="right" else "right",fontsize=8.5)
level(0,.15,.55,"⁴He g.s.")
level(Ttp,.15,.55,"t + p  (19.815)")
level(Thn,.15,.55,"³He + n  (20.578)")
level(Edd,.15,.55,"d + d entry — ⁴He* (23.847)",color="#c0392b")
ax.annotate("",xy=(.24,Ttp),xytext=(.24,Edd),arrowprops=dict(arrowstyle="->",color="#1d6fa5",lw=1.6))
ax.text(.225,(Ttp+Edd)/2,"Q = 4.033 MeV",rotation=90,va="center",ha="right",fontsize=8,color="#1d6fa5")
ax.annotate("",xy=(.35,Thn),xytext=(.35,Edd),arrowprops=dict(arrowstyle="->",color="#1d6fa5",lw=1.6))
ax.text(.365,(Thn+Edd)/2,"Q = 3.269 MeV",rotation=90,va="center",fontsize=8,color="#1d6fa5")
ax.annotate("",xy=(.47,0),xytext=(.47,Edd),arrowprops=dict(arrowstyle="->",color="#8e44ad",lw=1.6,ls="--"))
ax.text(.485,Edd/2,"γ, 23.847 MeV\nbranch ~10⁻⁷",rotation=90,va="center",fontsize=8,color="#8e44ad")
ax.text(.35,Edd+1.1,"every d–d event must exit here:\nall thresholds lie below the entry",
        ha="center",fontsize=8.5,style="italic")
ax.set_ylim(-1.6,27.5); ax.set_xlim(0,1.02)
ax.set_ylabel("excitation above ⁴He ground state (MeV)")
ax.set_xticks([]); [s.set_visible(False) for k,s in ax.spines.items() if k in("top","right","bottom")]
ax.set_title("The compound system ⁴He* and its mandatory exits",fontsize=10)
plt.tight_layout(); plt.savefig("/home/claude/fig2_exit_ladder.png",bbox_inches="tight"); plt.close()

# ---------- Figure 3: fifty orders of magnitude ----------
eV=1.602176634e-19
r_hn, r_tp, r_g = 1/(3.269e6*eV), 1/(4.033e6*eV), 1/(23.847e6*eV)
baseline = 3e-64*(6.022e23/2)          # KN rate x 1 mol D
fig,ax=plt.subplots(figsize=(9.2,2.9),dpi=200)
ax.set_xscale("log"); ax.set_xlim(1e-44,1e15); ax.set_ylim(0,1)
ax.axvline(baseline,color="#2b3a55",lw=2)
ax.text(baseline,0.72," screened D₂ baseline × 1 mol\n ≈ 9×10⁻⁴¹ /s  (Koonin–Nauenberg)",fontsize=8,va="bottom")
for r,lab,c in [(r_g,"⁴He+γ  2.6×10¹¹",'#8e44ad'),(r_tp,"t+p  1.6×10¹²",'#1d6fa5'),(r_hn,"³He+n  1.9×10¹²",'#c0392b')]:
    ax.axvline(r,color=c,lw=2)
ax.text(r_hn*3,0.72,"mandatory rates per watt\nof claimed excess heat",fontsize=8,va="bottom")
ax.annotate("",xy=(r_g,0.42),xytext=(baseline,0.42),arrowprops=dict(arrowstyle="->",lw=1.8,color="#111"))
ax.text(np.sqrt(baseline*r_g),0.47,"the claim under test: enhancement of ≈ 51 orders of magnitude",
        ha="center",fontsize=9,style="italic")
ax.axvspan(1e-3,1e1,color="#dfe6ee",zorder=0)
ax.text(np.sqrt(1e-3*1e1),0.12,"typical neutron-detection floors\n(every calibrated null ⇒ a bound, B.2.15)",ha="center",fontsize=7.5)
ax.set_yticks([]); ax.set_xlabel("fusion events per second (mole-scale deuterium sample)")
[s.set_visible(False) for k,s in ax.spines.items() if k in("top","right","left")]
ax.set_title("The size of the claim after the reduction — exactly as before it",fontsize=10)
plt.tight_layout(); plt.savefig("/home/claude/fig3_fifty_orders.png",bbox_inches="tight"); plt.close()

import math
print("enhancement orders:", math.log10(r_g/baseline))
print("figures written")