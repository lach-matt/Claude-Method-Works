import math, statistics as st
import numpy as np
Rinf=109737.31568; mp=1836.15267343
CD={0:{6:51483.980,7:62563.435,8:66682.029,9:68682.325,10:69806.814,11:70502.04,12:70961.993},
    1:{5:43692.384,6:59907.28,7:65501.412,8:68059.393},
    2:{5:59485.768,6:65353.372,7:67989.814,8:69400.900,9:70244.09,10:70787.850,11:71158.957},
    3:{4:65586.0,5:68093.7,6:69456.4,7:70277.4,8:70809.7,9:71174.2}}
IN={0:{6:24372.957,7:36301.864,8:40636.98,9:42719.02,10:43881.26,11:44595.86,12:45067.19},
    1:{6:31816.982,7:38861.43,8:41827.10,9:43369.09,10:44275.17},
    2:{5:32892.230,6:39048.53,7:41836.41,8:43335.93,9:44234.70,10:44815.06},
    3:{4:39707.59,5:42220.25,6:43584.66,7:44406.31,8:44938.81,9:45303.31}}
SPEC=[("Cd I",48,1,112.41,72540.05,CD,{0:5,1:3,2:2,3:0}),
      ("In I",49,1,114.82,46670.107,IN,{0:5,1:3,2:2,3:0})]
L="spdf"
print("  THE PEAK CAPTURE — Cd I, In I at Nₑ = 48, 49\n")
OUT={}
for nm,Z,c,A_,lim,S,PM in SPEC:
    RM=Rinf/(1+1/(A_*mp))
    print(f"  {nm}   Nₑ = {Z-c+1}   limit {lim}\n")
    print(f"      {'ℓ':>3}{'p':>3}{'n':>4}{'δ':>10}{'σ(δ)':>9}{'δ/√p':>9}")
    for l in sorted(S):
        d=S[l]
        n=np.array(sorted(d),float); E=np.array([d[int(x)] for x in n])
        ns=c*np.sqrt(RM/(lim-E)); dd=n-ns
        use=dd[-min(4,len(dd)):]
        p=PM[l]
        if p<1: continue
        print(f"      {L[l]:>3}{p:>3}{len(n):>4}{st.median(use):>10.4f}"
              f"{st.pstdev(use):>9.4f}{st.median(use)/math.sqrt(p):>9.4f}")
        OUT.setdefault(nm,[]).append(st.median(use)/math.sqrt(p))
    a=st.median(OUT[nm])
    ne=Z-c+1; u=math.log(ne/c**(2/3))
    pred=math.exp(-2.2523+1.3620*u-0.1749*u*u)
    print(f"\n      a = median δ/√p = {a:.4f}")
    print(f"      u = ln(Nₑ/c^(2/3)) = {u:.4f}")
    print(f"      predicted a = {pred:.4f}   ratio {a/pred:.3f}\n")
print("  THE THREE PARAMETERS TESTED\n")
u0=1.3620/(2*0.1749); M=math.exp(-2.2523+1.3620*u0-0.1749*u0*u0)
print(f"      u₀ = {u0:.4f}  ⇒  Nₑ/c^(2/3) = {math.exp(u0):.1f}   (peak position)")
print(f"      M  = {M:.4f}                            (ceiling on δ/√p)")
print(f"      σ  = {1/math.sqrt(2*0.1749):.4f}                            (log-width)\n")
for nm in OUT:
    print(f"      {nm}: largest δ/√p = {max(OUT[nm]):.4f}   "
          f"{'ABOVE the ceiling' if max(OUT[nm])>M else 'below the ceiling'}")
