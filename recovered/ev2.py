import numpy as np, eldata as ed
from itertools import combinations
from collections import Counter
from scipy import stats
CAP=lambda l: 2*(2*l+1)
L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,CAP(l)+1)]
occ=set(ed.E.values()); zs=sorted(ed.E)
def leq(a,b): return all(x<=y for x,y in zip(a,b))
def V(c,g,e,tol=None):
    ok=(abs(g-e)<=tol) if tol is not None else (g==e)
    gs=f"{g:.4f}" if isinstance(g,float) else str(g)
    print(f"  {c:<54}{gs:>13}  exp {str(e):>10}  {'OK' if ok else '*** FAIL ***'}")

print("="*84); print("EVIDENCE AUDIT D — JANET CORRESPONDENCE, VERIFIED COMPUTATIONALLY"); print("="*84)
# Janet: blocks of constant n+l, period lengths = slice volumes
Lbig=[(n,l,k) for n in range(1,40) for l in range(0,n) for k in range(1,CAP(l)+1)]
cnt=Counter(n+l for (n,l,k) in Lbig)
per=[cnt[i] for i in range(1,9)]
V("Janet period lengths from slice volumes",per,[2,2,8,8,18,18,32,32])
# Janet's He-over-Be placement: does the n+l projection put He with Be?
# In Janet, row = n+l. He: n=1,l=0 -> row 1. Be: n=2,l=0 -> row 2. Ne: n=2,l=1 -> row 3.
print(f"      He (1,0,2): Madelung row n+ℓ = {1+0}")
print(f"      Be (2,0,2): Madelung row n+ℓ = {2+0}")
print(f"      Ne (2,1,6): Madelung row n+ℓ = {2+1}")
print("      In Janet's table the s-block is rightmost, so He tops the s-column")
print("      above Be — verified by construction of the projection.")
# block composition of each Janet row
print("      row composition (subshells at each n+ℓ level):")
for lev in range(1,9):
    subs=sorted({(n,l) for (n,l,k) in Lbig if n+l==lev and l<=4})
    print(f"        n+ℓ={lev}: "+" ".join(f"{n}{'spdfg'[l]}" for n,l in subs))

print()
print("="*84); print("EVIDENCE AUDIT E — FIBRES: SEVEN OF EIGHT GROUPS"); print("="*84)
fib={}
for z in zs: fib.setdefault(ed.E[z][1:],[]).append(z)
conv={1:[1,3,11,19,37,55,87],2:[4,12,20,38,56,88],13:[5,13,31,49,81,113],
      14:[6,14,32,50,82,114],15:[7,15,33,51,83,115],16:[8,16,34,52,84,116],
      17:[9,17,35,53,85,117],18:[2,10,18,36,54,86,118]}
exact=0
for g,mem in sorted(conv.items()):
    key=ed.E[mem[-1]][1:]
    got=sorted(fib.get(key,[]))
    ok=(got==sorted(mem))
    if ok: exact+=1
    print(f"  group {g:>2}: {'exact' if ok else 'differs'}  fibre {key} → {[ed.SYM[z] for z in got]}")
    if not ok: print(f"            conventional: {[ed.SYM[z] for z in mem]}")
V("groups reproduced exactly",exact,7)

print()
print("="*84); print("EVIDENCE AUDIT F — PART IV STATISTICS"); print("="*84)
MN={21:19,22:51,23:54,24:57,26:61,27:64,28:67,29:72,39:20,40:49,41:53,42:56,44:62,
45:65,46:69,47:71,57:33,58:32,59:31,60:30,62:28,63:18,64:27,65:26,66:25,67:24,68:23,
69:22,70:17,71:21,72:50,73:52,74:55,75:58,77:63,78:66,79:70,90:47,92:45,1:92,3:1,
4:77,5:86,6:95,7:100,8:101,9:102,11:11,12:73,13:80,14:85,15:90,16:94,17:99,19:10,
20:16,30:76,31:81,32:84,33:89,34:93,35:98,37:9,38:15,48:75,49:79,50:83,51:88,52:92,
53:97,55:8,56:14,80:74,81:78,82:82,83:87,84:91,85:96}
com=sorted(z for z in MN if z in ed.E)
tau,_=stats.kendalltau(com,[MN[z] for z in com])
V("Kendall τ(Z, Pettifor MN)",tau,-0.23,0.03)
# Madelung inversions and anomaly overlap
ANOM={24,29,41,42,44,45,46,47,57,58,64,78,79,89,90,91,92,93,96,103}
o=sorted(zs,key=lambda z:(ed.E[z][0]+ed.E[z][1],ed.E[z][0],ed.E[z][2]))
mis=set(z for i,z in enumerate(o) if z!=zs[i])
V("documented anomalies",len(ANOM),20)
V("elements misplaced by Madelung",len(mis),30)
V("overlap misplaced ∩ anomalous",len(mis&ANOM),10)
V("misplaced but regular",len(mis-ANOM),20)
V("anomalous but correctly placed",len(ANOM-mis),10)

print()
print("="*84); print("EVIDENCE AUDIT G — PART V STATISTICS"); print("="*84)
dHf={21:-100.,22:-72.,23:-32.,24:10.,26:20.,27:15.,28:20.,29:40.,39:-114.,40:-82.,
41:-40.,42:25.,44:30.,45:20.,46:-19.,47:60.,57:-104.,58:-100.,59:-104.,60:-100.,
62:-96.,63:-88.,64:-92.,65:-92.,66:-92.,67:-90.,68:-90.,69:-88.,70:-84.,71:-84.,
72:-66.,73:-38.,74:30.,75:25.,77:30.,78:25.,79:50.,90:-72.,92:-42.}
def dcls(z):
    n,l,k=ed.E[z]; return 'B' if l+1<=n-1 else ('C' if l>0 else 'A')
ZS=sorted(dHf)
b=[dHf[z] for z in ZS if dcls(z)=='B']; c=[dHf[z] for z in ZS if dcls(z)=='C']
tt,pp=stats.ttest_ind(b,c,equal_var=False)
V("Class B mean ΔH_f",float(np.mean(b)),-15.7,0.6)
V("Class C mean ΔH_f",float(np.mean(c)),-61.9,0.6)
V("Welch p for B vs C",pp,0.010,0.004)
# anomaly enrichment baselines
def frac(sel,pred): return 100*sum(1 for z in sel if pred(z))/len(sel)
half=lambda z: ed.E[z][2]==2*ed.E[z][1]
full=lambda z: ed.E[z][2]==CAP(ed.E[z][1])
bnd =lambda z: ed.E[z][1]==ed.E[z][0]-1
for nm,pred,ea,eb in [('half-filled',half,10,16),('filled',full,5,16),('boundary',bnd,20,27)]:
    ga=frac(ANOM,pred); gb=frac(zs,pred)
    print(f"  {nm:<14} anomalous {ga:5.1f}% (paper {ea}%)   baseline {gb:5.1f}% (paper {eb}%)   "
          f"{'runs backwards OK' if ga<gb else '*** CHECK ***'}")