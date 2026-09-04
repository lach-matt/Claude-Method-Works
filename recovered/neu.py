import math, statistics as st, json
import numpy as np
from scipy import stats as SS
O=[tuple(x) for x in json.load(open("/tmp/step1.json"))]
NE=np.array([o[2] for o in O],float); C=np.array([o[1] for o in O],float)
A=np.array([o[3] for o in O]); LA=np.log(A)
u=np.log(NE)-(2/3)*np.log(C)
X=np.column_stack([u,u**2,np.ones(len(u))])
b,*_=np.linalg.lstsq(X,LA,rcond=None)
q=A/np.exp(X@b)
print("  IS THE BOW THE NEUTRALS?\n")
print(f"      {'Nₑ band':>9}{'neutrals':>20}{'ions':>20}")
print(f"      {'':>9}{'n':>5}{'median a/pred':>15}{'n':>5}{'median a/pred':>15}")
for lo,hi in ((2,7),(7,16),(16,33),(33,60)):
    m=(NE>=lo)&(NE<hi)
    n1=m&(C==1); n2=m&(C>1)
    s1=f"{int(n1.sum()):>5}"+(f"{st.median(q[n1]):>15.3f}" if n1.sum() else f"{'—':>15}")
    s2=f"{int(n2.sum()):>5}"+(f"{st.median(q[n2]):>15.3f}" if n2.sum() else f"{'—':>15}")
    print(f"      {f'{lo}–{hi}':>9}{s1}{s2}")
print()
n1=C==1; n2=C>1
print(f"      all neutrals : {int(n1.sum()):>3} species   median {st.median(q[n1]):.3f}"
      f"   sd {st.pstdev(q[n1]):.3f}")
print(f"      all ions     : {int(n2.sum()):>3} species   median {st.median(q[n2]):.3f}"
      f"   sd {st.pstdev(q[n2]):.3f}")
print()
print("  FIT THE IONS ALONE, THEN PREDICT THE NEUTRALS\n")
Xi=X[n2]; bi,*_=np.linalg.lstsq(Xi,LA[n2],rcond=None)
ri=LA[n2]-Xi@bi
print(f"      ions only : ln a = {bi[0]:.4f}·u {bi[1]:+.4f}·u² {bi[2]:+.4f}")
print(f"                  {int(n2.sum())} species · r² {1-np.var(ri)/np.var(LA[n2]):.4f}"
      f" · rms {float(np.sqrt(np.mean(ri**2))):.4f}\n")
pn=np.exp(X[n1]@bi); qn=A[n1]/pn
print(f"      predicting the {int(n1.sum())} neutrals from the ion fit:")
print(f"          median a/pred {st.median(qn):.3f}   sd {st.pstdev(qn):.3f}")
print(f"          rms in ln a  {float(np.sqrt(np.mean((np.log(A[n1])-np.log(pn))**2))):.4f}")
print()
print(f"      {'Nₑ':>5}{'a measured':>13}{'a predicted':>13}{'ratio':>9}")
idx=np.argsort(NE[n1])
NEn=NE[n1]; An=A[n1]
for i in idx:
    print(f"      {int(NEn[i]):>5}{An[i]:>13.4f}{pn[i]:>13.4f}{An[i]/pn[i]:>9.3f}")