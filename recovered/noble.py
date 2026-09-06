import math, statistics as st
import numpy as np
Rinf=109737.31568; mp=1836.15267343
# 2[3/2]* J=2 for ns; 2[5/2] J=3 for np; 2[7/2]* J=4 for nd; 2[9/2] J=5/4 for nf
XE={0:{6:67067.547,7:85188.777,8:90804.538,9:93398.253,10:94759.927},
    1:{6:78403.061,7:88469.213,8:92264.950,9:94134.53},
    2:{5:80196.629,6:88911.692,7:92444.927,8:94226.320},
    3:{4:90861.506,5:93378.199,6:94744.718}}
KR={0:{5:79971.7417,6:99626.882,7:105647.4536,8:108324.9822,9:109751.9639},
    1:{5:92294.4012,6:103115.6343,7:107141.171,8:109103.302,9:110209.56},
    2:{4:97797.287,5:104630.57,6:107778.8962,7:109433.9079,8:110403.6385},
    3:{4:105988.81,5:108487.079,6:109843.132}}
RN={0:{7:54620.35,9:79626.50,10:82211.18,11:83595.18,12:84423.40},
    1:{7:68039.48,8:77604.53,9:81253.54,10:83064.98},
    2:{6:69798.00,7:78088.42,8:81514.40,9:83172.08,10:84162.11,11:84785.83},
    3:{5:79690.3,6:82218.92,7:83592.53,8:84419.04}}
SP=[("Kr I",36,83.798,112914.433,KR,{0:4,1:3,2:1,3:0}),
    ("Xe I",54,131.293,97833.787,XE,{0:5,1:4,2:2,3:0}),
    ("Rn I",86,222.018,86692.5,RN,{0:6,1:5,2:3,3:0})]
L="spdf"
print("  THE THREE CLOSURES — Kr I, Xe I, Rn I\n")
OUT={}
for nm,ne,A,lim,S,PM in SP:
    RM=Rinf/(1+1/(A*mp)); u=math.log(ne)
    print(f"  {nm}   Nₑ = {ne}   u = ln {ne} = {u:.4f}   limit {lim}\n")
    print(f"      {'ℓ':>3}{'p':>3}{'n':>4}{'δ':>10}{'σ(δ)':>9}{'δ/√p':>9}")
    vals=[]
    for l in sorted(S):
        d=S[l]; p=PM[l]
        n=np.array(sorted(d),float); E=np.array([d[int(x)] for x in n])
        ns=1*np.sqrt(RM/(lim-E)); dd=n-ns
        use=dd[-min(3,len(dd)):]
        if p<1:
            print(f"      {L[l]:>3}{p:>3}{len(n):>4}{st.median(use):>10.4f}"
                  f"{st.pstdev(use):>9.4f}{'—':>9}")
            continue
        v=st.median(use)/math.sqrt(p); vals.append(v)
        print(f"      {L[l]:>3}{p:>3}{len(n):>4}{st.median(use):>10.4f}"
              f"{st.pstdev(use):>9.4f}{v:>9.4f}")
    OUT[nm]=(u,st.median(vals),vals)
    print(f"\n      a = median δ/√p = {st.median(vals):.4f}   spread {max(vals)-min(vals):.4f}\n")
print("  THE CALIBRATION\n")
uX,aX,_=OUT["Xe I"]; uK,aK,_=OUT["Kr I"]; uR,aR,_=OUT["Rn I"]
print(f"      u₀ = ln 54 = {math.log(54):.4f}   ·   M = a(Xe I) = {aX:.4f}")
print(f"      Kr I : u = {uK:.4f}  (u−u₀ = {uK-math.log(54):+.4f})  a = {aK:.4f}")
print(f"      Rn I : u = {uR:.4f}  (u−u₀ = {uR-math.log(54):+.4f})  a = {aR:.4f}\n")
for nm,uu,aa in (("Kr",uK,aK),("Rn",uR,aR)):
    if aa<aX:
        s=abs(uu-math.log(54))/math.sqrt(2*math.log(aX/aa))
        print(f"      σ from {nm} : {s:.4f}")
    else:
        print(f"      σ from {nm} : a exceeds M — the peak is not at Xe")
print()
print("      previously FITTED: M = 1.5451  u₀ = 3.9854  σ = 1.7206")