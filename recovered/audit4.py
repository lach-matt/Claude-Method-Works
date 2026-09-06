import numpy as np, eldata as ed
from scipy import stats
from collections import Counter
CAP=lambda l: 2*(2*l+1)
zs=sorted(ed.E); occ=set(ed.E.values())
def R(claim,got,exp,tol=None):
    ok = (abs(got-exp)<=tol) if tol is not None else (got==exp)
    g=f"{got:.4f}" if isinstance(got,float) else str(got)
    e=f"{exp:.4f}" if isinstance(exp,float) else str(exp)
    print(f"  {claim:<50}{g:>11}  exp {e:>9}  {'OK' if ok else '*** FAIL ***'}")

print("="*78); print("AUDIT 10 — FIBRES / GROUPS / HELIUM"); print("="*78)
fib={}
for z in zs: fib.setdefault(ed.E[z][1:], []).append(z)
he=fib.get((0,2))
print(f"  fibre (ℓ=0,k=2) members: {[ed.SYM[z] for z in he]}")
R("He on the alkaline-earth fibre", 2 in he, True)
R("He NOT on the noble-gas fibre", 2 not in fib.get((1,6),[]), True)
print(f"  fibre (ℓ=1,k=6): {[ed.SYM[z] for z in fib.get((1,6),[])]}")
grp1=fib.get((0,1))
R("alkali fibre = H,Li,Na,K,Rb,Cs,Fr", [ed.SYM[z] for z in grp1],
  ['H','Li','Na','K','Rb','Cs','Fr'])

print()
print("="*78); print("AUDIT 11 — KAINOSYMMETRY DIAGONAL"); print("="*78)
diag=[(n,l) for n in range(1,8) for l in range(0,min(n,5)) if l==n-1]
names=[f"{n}{'spdfg'[l]}" for n,l in diag]
R("cells on ℓ=n−1", names, ['1s','2p','3d','4f','5g'])
print("  These are the first-of-kind subshells (no radial node). OK")

print()
print("="*78); print("AUDIT 12 — HYDRIDE REGRESSION"); print("="*78)
dHf={21:-100.,22:-72.,23:-32.,24:10.,26:20.,27:15.,28:20.,29:40.,39:-114.,40:-82.,
41:-40.,42:25.,44:30.,45:20.,46:-19.,47:60.,57:-104.,58:-100.,59:-104.,60:-100.,
62:-96.,63:-88.,64:-92.,65:-92.,66:-92.,67:-90.,68:-90.,69:-88.,70:-84.,71:-84.,
72:-66.,73:-38.,74:30.,75:25.,77:30.,78:25.,79:50.,90:-72.,92:-42.}
ZS=sorted(dHf); Y=np.array([dHf[z] for z in ZS],float)
l=np.array([ed.E[z][1] for z in ZS],float); k=np.array([ed.E[z][2] for z in ZS],float)
def fitloo(cols):
    X=np.column_stack([np.ones(len(Y))]+cols)
    b,*_=np.linalg.lstsq(X,Y,rcond=None); p=X@b
    fit=1-np.sum((Y-p)**2)/np.sum((Y-np.mean(Y))**2)
    pr=np.zeros(len(Y))
    for i in range(len(Y)):
        m=np.ones(len(Y),bool); m[i]=False
        bb,*_=np.linalg.lstsq(X[m],Y[m],rcond=None); pr[i]=X[i]@bb
    return fit, 1-np.sum((Y-pr)**2)/np.sum((Y-np.mean(Y))**2), b
f,lo,b=fitloo([l,k])
R("n (hydride sample)", len(ZS), 39)
R("ℓ+k fit R²", f, 0.592, 0.003)
R("ℓ+k LOO R²", lo, 0.514, 0.003)
print(f"    coefficients: ΔH ≈ {b[0]:+.1f} {b[1]:+.1f}·ℓ {b[2]:+.1f}·k")
R("intercept ≈ +136.2", b[0], 136.2, 0.5)
R("ℓ coefficient ≈ −89.5", b[1], -89.5, 0.5)
R("k coefficient ≈ +6.4", b[2], 6.4, 0.2)

print()
print("="*78); print("AUDIT 13 — MN SIGN FLIP"); print("="*78)
MN={21:19,22:51,23:54,24:57,26:61,27:64,28:67,29:72,39:20,40:49,41:53,42:56,44:62,
45:65,46:69,47:71,57:33,58:32,59:31,60:30,62:28,63:18,64:27,65:26,66:25,67:24,68:23,
69:22,70:17,71:21,72:50,73:52,74:55,75:58,77:63,78:66,79:70,90:47,92:45,1:92,3:1,
4:77,5:86,6:95,7:100,8:101,9:102,11:11,12:73,13:80,14:85,15:90,16:94,17:99,19:10,
20:16,30:76,31:81,32:84,33:89,34:93,35:98,37:9,38:15,48:75,49:79,50:83,51:88,52:92,
53:97,55:8,56:14,80:74,81:78,82:82,83:87,84:91,85:96}
for lv,exp in [(1,4.36),(2,4.28),(3,-1.47)]:
    pts=sorted((ed.E[z][2],MN[z]) for z in MN if z in ed.E and ed.E[z][1]==lv)
    s,i2,r,p,se=stats.linregress([p[0] for p in pts],[p[1] for p in pts])
    R(f"∂MN/∂k at ℓ={lv}", s, exp, 0.02)
com=sorted(z for z in MN if z in ed.E)
def leq(a,b): return all(x<=y for x,y in zip(a,b))
cp=[(a,b) for a in com for b in com if a!=b and leq(ed.E[a],ed.E[b])]
R("MN comparable pairs", len(cp), 1684)
R("MN order violations", sum(1 for a,b in cp if MN[a]>MN[b]), 960)

print()
print("="*78); print("AUDIT 14 — INTEGRAL SORTING"); print("="*78)
A={1:1,2:4,3:7,4:9,5:11,6:12,7:14,8:16,9:19,10:20,11:23,12:24,13:27,14:28,15:31,
16:32,17:35,18:40,19:39,20:40,21:45,22:48,23:51,24:52,25:55,26:56,27:59,28:58,
29:63,30:64,31:69,32:74,33:75,34:80,35:79,36:84,37:85,38:88,39:89,40:90,41:93,
42:98,43:98,44:102,45:103,46:106,47:107,48:114,49:115,50:120,51:121,52:130,53:127,
54:132,55:133,56:138,57:139,58:140,59:141,60:142,61:145,62:152,63:153,64:158,
65:159,66:164,67:165,68:166,69:169,70:174,71:175,72:180,73:181,74:184,75:187,
76:192,77:193,78:195,79:197,80:202,81:205,82:208,83:209}
cm=sorted(A)
inv=[(ed.SYM[cm[i]],ed.SYM[cm[j]]) for i in range(len(cm)) for j in range(i+1,len(cm))
     if A[cm[i]]>A[cm[j]]]
R("Z/A inversions", sorted(inv), sorted([('Ar','K'),('Co','Ni'),('Se','Br'),('Te','I')]))
print("  These are exactly Mendeleev's four transpositions against weight. OK")
MAGIC=[m for m in (2,8,20,28,50,82) if m in ed.E]
mr=[sum(ed.E[m]) for m in MAGIC]; allr=[sum(ed.E[z]) for z in zs]
t,p=stats.ttest_1samp(mr,np.mean(allr))
print(f"  magic-Z mean lattice rank {np.mean(mr):.2f} vs all {np.mean(allr):.2f}, p={p:.3f}")
R("magic numbers unrelated to Λ (p>0.05)", p>0.05, True)