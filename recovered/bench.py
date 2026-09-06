import numpy as np, eldata as ed
from scipy import stats

dHf = {21:-100.,22:-72.,23:-32.,24:10.,26:20.,27:15.,28:20.,29:40.,
39:-114.,40:-82.,41:-40.,42:25.,44:30.,45:20.,46:-19.,47:60.,
57:-104.,58:-100.,59:-104.,60:-100.,62:-96.,63:-88.,64:-92.,65:-92.,
66:-92.,67:-90.,68:-90.,69:-88.,70:-84.,71:-84.,72:-66.,73:-38.,
74:30.,75:25.,77:30.,78:25.,79:50.,90:-72.,92:-42.}

# Pettifor Mendeleev number (1984 scale)
MN = {21:19,22:51,23:54,24:57,26:61,27:64,28:67,29:72,39:20,40:49,41:53,
42:56,44:62,45:65,46:69,47:71,57:33,58:32,59:31,60:30,62:28,63:18,64:27,
65:26,66:25,67:24,68:23,69:22,70:17,71:21,72:50,73:52,74:55,75:58,77:63,
78:66,79:70,90:47,92:45}

# Miedema parameters: electrostatic potential phi* (V), electron density nws^(1/3) (d.u.)
MIE = {21:(3.25,1.27),22:(3.65,1.47),23:(4.25,1.64),24:(4.65,1.74),26:(4.93,1.77),
27:(5.10,1.75),28:(5.20,1.75),29:(4.45,1.47),39:(3.20,1.21),40:(3.40,1.39),
41:(4.00,1.62),42:(4.65,1.77),44:(5.40,1.83),45:(5.40,1.76),46:(5.45,1.67),
47:(4.35,1.36),57:(3.05,1.09),58:(3.18,1.19),59:(3.19,1.09),60:(3.19,1.08),
62:(3.20,1.07),63:(3.20,1.04),64:(3.20,1.21),65:(3.21,1.12),66:(3.21,1.11),
67:(3.22,1.11),68:(3.22,1.11),69:(3.22,1.11),70:(3.23,0.99),71:(3.23,1.14),
72:(3.55,1.43),73:(4.05,1.63),74:(4.80,1.81),75:(5.20,1.86),77:(5.55,1.83),
78:(5.65,1.78),79:(5.15,1.57),90:(3.30,1.28),92:(4.05,1.56)}

ZS=[z for z in sorted(dHf) if z in MN and z in MIE]
Y=np.array([dHf[z] for z in ZS],float)
print(f"n = {len(ZS)} elements common to all three schemes\n")

F={
 'Lach: l+k'            : [np.array([ed.E[z][1] for z in ZS],float),
                           np.array([ed.E[z][2] for z in ZS],float)],
 'Lach: l+n+k'          : [np.array([ed.E[z][1] for z in ZS],float),
                           np.array([ed.E[z][0] for z in ZS],float),
                           np.array([ed.E[z][2] for z in ZS],float)],
 'Pettifor: MN'         : [np.array([MN[z] for z in ZS],float)],
 'Pettifor: MN + MN^2'  : [np.array([MN[z] for z in ZS],float),
                           np.array([MN[z]**2 for z in ZS],float)],
 'Miedema: phi + nws'   : [np.array([MIE[z][0] for z in ZS]),
                           np.array([MIE[z][1] for z in ZS])],
 'Miedema: full form'   : [np.array([MIE[z][0] for z in ZS]),
                           np.array([MIE[z][1] for z in ZS]),
                           np.array([(MIE[z][0]-2.1)**2 for z in ZS]),
                           np.array([(MIE[z][1]-1.5)**2 for z in ZS])],
 'Atomic number Z'      : [np.array(ZS,float)],
 'Lach + Miedema'       : [np.array([ed.E[z][1] for z in ZS],float),
                           np.array([ed.E[z][2] for z in ZS],float),
                           np.array([MIE[z][0] for z in ZS]),
                           np.array([MIE[z][1] for z in ZS])],
}

def ev(cols):
    X=np.column_stack([np.ones(len(Y))]+cols)
    b,*_=np.linalg.lstsq(X,Y,rcond=None); p=X@b
    r2=1-np.sum((Y-p)**2)/np.sum((Y-np.mean(Y))**2)
    pr=np.zeros(len(Y))
    for i in range(len(Y)):
        m=np.ones(len(Y),bool); m[i]=False
        bb,*_=np.linalg.lstsq(X[m],Y[m],rcond=None); pr[i]=X[i]@bb
    lr2=1-np.sum((Y-pr)**2)/np.sum((Y-np.mean(Y))**2)
    return r2, lr2, float(np.sqrt(np.mean((Y-pr)**2))), X.shape[1]-1

print(f"{'scheme':<24}{'params':>7}{'fit R2':>9}{'LOO R2':>9}{'LOO RMSE':>10}")
print('-'*59)
res={}
for k,v in F.items():
    r2,lr2,rm,npar=ev(v); res[k]=(r2,lr2,rm,npar)
    print(f"{k:<24}{npar:>7}{r2:>9.3f}{lr2:>9.3f}{rm:>10.1f}")

print("\nPaired comparison of LOO squared errors, Lach(l+k) vs each:")
def loo_err(cols):
    X=np.column_stack([np.ones(len(Y))]+cols); pr=np.zeros(len(Y))
    for i in range(len(Y)):
        m=np.ones(len(Y),bool); m[i]=False
        b,*_=np.linalg.lstsq(X[m],Y[m],rcond=None); pr[i]=X[i]@b
    return (Y-pr)**2
base=loo_err(F['Lach: l+k'])
for k in ['Pettifor: MN','Pettifor: MN + MN^2','Miedema: phi + nws','Miedema: full form']:
    o=loo_err(F[k]); t,p=stats.wilcoxon(base,o)
    better = 'Lach better' if base.mean()<o.mean() else 'other better'
    print(f"  vs {k:<22} Wilcoxon p={p:.4f}   ({better})")