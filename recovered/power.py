import numpy as np, eldata as ed
from scipy import stats
rng=np.random.default_rng(0)
def boot_r2(X,y,B=4000):
    n=len(y); out=[]
    for _ in range(B):
        i=rng.integers(0,n,n)
        Xi,yi=X[i],y[i]
        try:
            b,*_=np.linalg.lstsq(Xi,yi,rcond=None); p=Xi@b
            out.append(1-np.sum((yi-p)**2)/np.sum((yi-np.mean(yi))**2))
        except Exception: pass
    return np.percentile(out,[2.5,97.5])
def ci_prop(k,n):
    lo,hi=stats.beta.ppf(0.025,k,n-k+1) if k>0 else 0, stats.beta.ppf(0.975,k+1,n-k) if k<n else 1
    return (0.0 if k==0 else stats.beta.ppf(0.025,k,n-k+1),
            1.0 if k==n else stats.beta.ppf(0.975,k+1,n-k))
def ci_r(r,n):
    z=np.arctanh(r); se=1/np.sqrt(n-3)
    return np.tanh(z-1.96*se), np.tanh(z+1.96*se)
print("="*94)
print("STATISTICAL AUDIT — every quantitative claim, with sample size and interval")
print("="*94)
rows=[]

# 1. hydride
dHf={21:-100.,22:-72.,23:-32.,24:10.,26:20.,27:15.,28:20.,29:40.,39:-114.,40:-82.,
41:-40.,42:25.,44:30.,45:20.,46:-19.,47:60.,57:-104.,58:-100.,59:-104.,60:-100.,
62:-96.,63:-88.,64:-92.,65:-92.,66:-92.,67:-90.,68:-90.,69:-88.,70:-84.,71:-84.,
72:-66.,73:-38.,74:30.,75:25.,77:30.,78:25.,79:50.,90:-72.,92:-42.}
ZS=sorted(dHf); Y=np.array([dHf[z] for z in ZS])
X=np.column_stack([np.ones(len(Y)),[ed.E[z][1] for z in ZS],[ed.E[z][2] for z in ZS]])
b,*_=np.linalg.lstsq(X,Y,rcond=None); R2=1-np.sum((Y-X@b)**2)/np.sum((Y-np.mean(Y))**2)
lo,hi=boot_r2(X,Y)
rows.append(("§23.1 hydride, fit R²",len(Y),f"{R2:.3f}",f"[{lo:.2f}, {hi:.2f}]","wide but informative"))

# 2. Pettifor MN
MN={21:19,22:51,23:54,24:57,26:61,27:64,28:67,29:72,39:20,40:49,41:53,42:56,44:62,
45:65,46:69,47:71,57:33,58:32,59:31,60:30,62:28,63:18,64:27,65:26,66:25,67:24,68:23,
69:22,70:17,71:21,72:50,73:52,74:55,75:58,77:63,78:66,79:70,90:47,92:45,1:92,3:1,
4:77,5:86,6:95,7:100,8:101,9:102,11:11,12:73,13:80,14:85,15:90,16:94,17:99,19:10,
20:16,30:76,31:81,32:84,33:89,34:93,35:98,37:9,38:15,48:75,49:79,50:83,51:88,52:92,
53:97,55:8,56:14,80:74,81:78,82:82,83:87,84:91,85:96}
com=sorted(z for z in MN if z in ed.E)
y2=np.array([MN[z] for z in com],float)
l=np.array([ed.E[z][1] for z in com],float); k=np.array([ed.E[z][2] for z in com],float)
n_=np.array([ed.E[z][0] for z in com],float)
X2=np.column_stack([np.ones(len(y2)),n_,l,k,l*l])
b2,*_=np.linalg.lstsq(X2,y2,rcond=None); R22=1-np.sum((y2-X2@b2)**2)/np.sum((y2-np.mean(y2))**2)
lo2,hi2=boot_r2(X2,y2)
rows.append(("§18.2 MN with ℓ² , fit R²",len(y2),f"{R22:.3f}",f"[{lo2:.2f}, {hi2:.2f}]","adequate"))

# 3. magic numbers
mr=[sum(ed.E[m]) for m in (2,8,20,28,50,82)]
allr=[sum(ed.E[z]) for z in sorted(ed.E)]
t,p=stats.ttest_1samp(mr,np.mean(allr))
d=(np.mean(mr)-np.mean(allr))/np.std(mr,ddof=1)
rows.append(("§18.3 magic numbers, p",6,f"{p:.3f}",f"Cohen d = {d:.2f}","UNDERPOWERED"))

# 4. structure map
rows.append(("§23.2 structure map, gain",139,"+0.000","McNemar p = 1.000","adequate"))

# 5. secondary periodicity conservative
lo5,hi5=ci_prop(12,14)
rows.append(("§12.3 sec. periodicity, 12/14",14,"0.857",f"[{lo5:.2f}, {hi5:.2f}]","small but exact"))

# 6. covalent radii 10/10
lo6,hi6=ci_prop(10,10)
rows.append(("§12.3 radii minima, 10/10",10,"1.000",f"[{lo6:.2f}, 1.00]","small but exact"))

# 7. reduction potentials 5/5
lo7,hi7=ci_prop(5,5)
rows.append(("§12.3 E° maxima, 5/5",5,"1.000",f"[{lo7:.2f}, 1.00]","VERY SMALL"))

# 8. rank correlation
r8=-1.0
rows.append(("§12.3 deficit vs k, ρ",5,"−1.000","exact p = 0.0083","VERY SMALL, exact"))

# 9. ionisation / electronegativity
rows.append(("§23.5 ionisation, CV R²",69,"0.280","—","adequate"))
rows.append(("§23.5 electronegativity, CV R²",66,"0.090","—","adequate"))

# 10. exchange labelling
rows.append(("§23.4 exchange AUC",30,"0.589","p = 0.233","small, null result"))

# 11. anomaly enrichment
rows.append(("§23.3 anomaly enrichment",20,"—","every direction reversed","small, null result"))

print(f"  {'claim':<32}{'n':>6}{'estimate':>12}{'interval / test':>26}   assessment")
print("  "+"-"*92)
for c,n,e,i,a in rows:
    print(f"  {c:<32}{n:>6}{e:>12}{i:>26}   {a}")