import numpy as np
exec(open('chart.py').read().split('print(f"{')[0])   # reuse CH

print("Is S_n bracketable? S_n(A) = B(A) - B(A-1), the quantity that sets V.\n")
print(f"{'chain':6}{'S_n monotone in A':>20}{'even-N sub':>13}{'odd-N sub':>12}{'last S_n':>11}{'drip?':>8}")
for el,(Z,rows) in CH.items():
    A=np.array([r[0] for r in rows],float); B=np.array([r[0]*r[1] for r in rows])
    Sn=np.diff(B)/1000.0; An=A[1:]
    N=(An-Z).astype(int)
    ev=Sn[N%2==0]; od=Sn[N%2==1]
    m_all=np.all(np.diff(Sn)<0) or np.all(np.diff(Sn)>0)
    m_ev=np.all(np.diff(ev)<0); m_od=np.all(np.diff(od)<0)
    print(f"{el:6}{str(m_all):>20}{str(m_ev):>13}{str(m_od):>12}{Sn[-1]:>10.2f}{'no':>8}")

print("\nSign changes in successive differences of S_n (the alternation):")
for el,(Z,rows) in list(CH.items())[:3]:
    A=np.array([r[0] for r in rows],float); B=np.array([r[0]*r[1] for r in rows])
    d2=np.sign(np.diff(np.diff(B)))
    print(f"  {el}: {int(np.sum(d2[1:]!=d2[:-1]))} sign reversals in {len(d2)-1} steps")

print("\nDistance from the last measured cell to S_n = 0, extrapolated within parity:")
for el,(Z,rows) in CH.items():
    A=np.array([r[0] for r in rows],float); B=np.array([r[0]*r[1] for r in rows])
    Sn=np.diff(B)/1000.0; An=A[1:]; N=(An-Z).astype(int)
    m=N%2==0
    x,y=An[m][-4:],Sn[m][-4:]
    sl,ic=np.polyfit(x,y,1)
    print(f"  {el:3} last measured A={int(A[-1]):3d}, S_n={Sn[-1]:5.2f} MeV; linear extrap hits 0 at A~{(-ic/sl):5.1f}  -> {int((-ic/sl)-A[-1]):+3d} cells beyond data")