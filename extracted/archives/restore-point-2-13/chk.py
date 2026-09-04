import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
src=open("regimes.py",encoding="utf-8").read()
src=src[:src.index("from collections import Counter")]
g={}; exec(src,g)
ROWS=g["ROWS"]; L="spdfg"
print("  1 · IS THE CHARGE FORM RIGHT?\n")
print("      test on the isoelectronic sequences we hold: which function of c")
print("      linearises δ best?\n")
seq=defaultdict(dict)
for r in ROWS: seq[(r["ne"],r["l"])][r["c"]]=r["d"]
FORMS={"ln(c+1)/c":lambda c: np.log(c+1)/c,
       "1/c":lambda c: 1.0/c,
       "ln(c+1)/(c+1)":lambda c: np.log(c+1)/(c+1),
       "c^-1/2":lambda c: c**-0.5,
       "ln(2c)/c":lambda c: np.log(2*c)/c,
       "1/(c+1)":lambda c: 1.0/(c+1)}
print(f"      {'form':<18}{'sequences':>11}{'median r²':>12}{'min r²':>9}")
for nm,f in FORMS.items():
    rr=[]
    for k,d in seq.items():
        if len(d)<3: continue
        cs=sorted(d); x=f(np.array(cs,float)); y=np.array([d[c] for c in cs])
        if y.max()<0.05: continue
        r=SS.linregress(x,y)
        rr.append(r.rvalue**2)
    if len(rr)<5: continue
    print(f"      {nm:<18}{len(rr):>11}{st.median(rr):>12.4f}{min(rr):>9.4f}")
print()
print("  2 · EVERY f CHANNEL, AGAINST ITS DISTANCE TO THE 4f/5f THRESHOLD\n")
fs=[r for r in ROWS if r["l"]==3 and r["p"]==0]
print(f"      {len(fs)} outer-well f channels\n")
print(f"      {'D=Z−T':>7}{'species':>11}{'chg':>5}{'δ':>10}{'y = δ/(scale)':>16}")
EL={30:"Zn",31:"Ga",48:"Cd",56:"Ba",55:"Cs",37:"Rb",38:"Sr",39:"Y",20:"Ca",
    19:"K",12:"Mg",13:"Al",14:"Si",15:"P",16:"S",11:"Na",18:"Ar",5:"B",6:"C",
    4:"Be",3:"Li",2:"He",1:"H",7:"N",8:"O",9:"F",10:"Ne",17:"Cl",21:"Sc",22:"Ti",
    26:"Fe",80:"Hg",83:"Bi",32:"Ge"}
RO={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",9:"IX",11:"XI",15:"XV",16:"XVI"}
k=0.4423
pts=[]
for r in sorted(fs,key=lambda x:-(x["Z"]-x["T"])):
    D=r["Z"]-r["T"]; ne=r["ne"]; c=r["c"]
    sc=((ne-1)/ne)*ne**k*(math.log(c+1)/c)
    y=r["d"]/sc if sc>1e-9 else float("nan")
    pts.append((D,y,r))
    if D>=-14:
        print(f"      {D:>7}{EL.get(r['Z'],r['Z']):>8}{RO.get(c,c):>3}{c:>5}"
              f"{r['d']:>10.4f}{y:>16.4f}")
print()
print("  and the same for d, for comparison\n")
ds=[r for r in ROWS if r["l"]==2 and r["p"]==0]
print(f"      {'D':>7}{'n':>4}{'median y':>11}")
by=defaultdict(list)
for r in ds:
    D=r["Z"]-r["T"]; ne=r["ne"]; c=r["c"]
    sc=((ne-1)/ne)*ne**k*(math.log(c+1)/c)
    if sc>1e-9: by[D].append(r["d"]/sc)
for D in sorted(by):
    if D>=-9: print(f"      {D:>7}{len(by[D]):>4}{st.median(by[D]):>11.4f}")
