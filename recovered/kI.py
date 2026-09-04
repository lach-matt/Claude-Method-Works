import math, statistics as st
import numpy as np
Rinf=109737.31568; mp=1836.15267343
RM=Rinf/(1+1/(39.0983*mp)); lim=35009.8140; c=1
S={0:{5:21026.551,6:27450.7104,7:30274.2487,8:31765.3767,9:32648.3511,
      10:33214.2267,11:33598.5597,12:33871.4788,13:34072.2393,14:34224.2113,
      15:34342.0150,16:34435.1762,17:34510.1190,18:34571.3017},
   1:{4:12985.185724,5:24701.382,6:28999.27,7:31069.90,8:32227.44,9:32940.2030,
      10:33410.2306,11:33736.4979,12:33972.2064,13:34148.0284,14:34282.6573,
      15:34388.0315,16:34472.0505,17:34540.1250,18:34596.0448},
   2:{3:21536.988,4:27398.147,5:30185.7476,6:31696.1661,7:32598.4437,8:33178.2324,
      9:33572.1249,10:33851.6418,11:34057.0385,12:34212.3393,13:34332.5823,
      14:34427.5667,15:34503.8967,16:34566.1522,17:34617.5815},
   3:{4:28127.85,5:30606.73,6:31953.17,7:32764.80,8:33291.40,9:33652.32,
      10:33910.42,11:34101.36,12:34246.37,13:34359.36,14:34448.98}}
PM={0:4,1:3,2:0,3:0}; L="spdf"
print("  K I   Nₑ = 19   limit 35009.814   —  one step before the crossing\n")
print(f"      {'ℓ':>3}{'p':>3}{'n':>4}{'δ (top 4)':>12}{'σ':>9}{'n₀':>5}{'n*':>9}")
OUT={}
for l in sorted(S):
    d=S[l]
    n=np.array(sorted(d),float); E=np.array([d[int(x)] for x in n])
    ns=c*np.sqrt(RM/(lim-E)); dd=n-ns
    use=dd[-4:]; OUT[l]=st.median(use); n0=PM[l]+l+1
    print(f"      {L[l]:>3}{PM[l]:>3}{len(n):>4}{st.median(use):>12.4f}"
          f"{st.pstdev(use):>9.5f}{n0:>5}{n0-st.median(use):>9.4f}")
print()
lo=min(range(4),key=lambda l:(PM[l]+l+1)-OUT[l])
print(f"      lowest n* : {L[lo]}  →  next electron to {PM[lo]+lo+1}{L[lo]}")
print(f"      truth at Z = 20 (Ca I) : 4s\n")
print("  THE d SERIES IN FULL — the collapse approaching\n")
d=S[2]; n=np.array(sorted(d),float); E=np.array([d[int(x)] for x in n])
ns=np.sqrt(RM/(lim-E)); dd=n-ns
for a,b in zip(n,dd): print(f"          {int(a):>3}d   δ = {b:.4f}")
print()
print(f"      K I  δ(nd) = {OUT[2]:.4f}   ·   Ca I δ(nd) = 0.9559")
print(f"      one proton, and δ(nd) rises by {0.9559-OUT[2]:.4f}")