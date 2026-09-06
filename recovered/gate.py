import numpy as np, json
from tf import potential
from rad import defect
# measured (Z,charge): {l: delta}; sources: index measured grade / store / R 1258 (Rb I, Y III)
M = {
 'Na I':(11,1,{0:1.34857,1:0.85615,2:0.01488,3:0.0016}),
 'K I': (19,1,{0:2.1912,1:1.7268,2:0.246,3:0.0112}),
 'Ca II':(20,2,{0:1.8265,1:1.4775,2:0.6341,3:0.0248}),
 'Sc III':(21,3,{0:1.5848,1:1.2838,2:0.65335,3:0.045}),
 'Rb I':(37,1,{0:3.1357,1:2.6566,2:1.3307,3:0.0143}),
 'Sr II':(38,2,{0:2.7113,1:2.3501,2:1.4577,3:0.0618}),
 'Y III':(39,3,{0:2.4462,1:2.1216,2:1.3965,3:0.1466}),
 'Cs I':(55,1,{0:4.0512,1:3.59251,2:2.46643,3:0.03254}),
 'Ba II':(56,2,{0:3.5984,1:3.2408,2:2.4147,3:0.7559}),
 'Fr I':(87,1,{0:5.07221,1:4.59521,2:3.42371}),
}
# lowest Rydberg n outside the core for each l, then n+3 to see the asymptote
core_n = {11:{0:3,1:3,2:3,3:4},19:{0:4,1:4,2:3,3:4},20:{0:4,1:4,2:3,3:4},21:{0:4,1:4,2:3,3:4},
          37:{0:5,1:5,2:4,3:4},38:{0:5,1:5,2:4,3:4},39:{0:5,1:5,2:4,3:4},
          55:{0:6,1:6,2:5,3:4},56:{0:6,1:6,2:5,3:4},87:{0:7,1:7,2:6,3:5}}
out={}; res=[]
for sp,(Z,ch,md) in M.items():
    V = potential(Z, ch)
    row=[]
    for l,dm in md.items():
        n0=core_n[Z][l]
        d1,_=defect(V,l,n0,ch,Z); d2,_=defect(V,l,n0+4,ch,Z)
        row.append((l,dm,d1,d2)); res.append(d2-dm)
    out[sp]=row
    print(f"{sp:7s}"+"  ".join(f"l{l}: meas {dm:6.3f} TF {d1:6.3f}/{d2:6.3f}" for l,dm,d1,d2 in row))
res=np.array(res); print(f"\nrms(TF asymptote - measured) over {len(res)} channels = {np.sqrt((res**2).mean()):.3f}; mean signed = {res.mean():+.3f}")
json.dump(out,open('gate.json','w'))