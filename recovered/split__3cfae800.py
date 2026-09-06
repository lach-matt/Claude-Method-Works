import numpy as np
exec(open('chart.py').read().split('print(f"{')[0])   # CH

def V_of(y):
    y=np.asarray(y,float)
    if len(y)<3: return np.nan,0
    w=np.abs(y[2:]-y[:-2]); e=np.abs(y[2:]-2*y[1:-1]+y[:-2])/2
    return w.sum()/max(e.sum(),1e-30), len(y)-2

print("=== Does resolving the channel destroy the low-V regime? ===\n")
print("A. n-alkane melting points (K), C4-C14")
C=np.arange(4,15); mp=np.array([134.9,143.4,177.8,182.6,216.4,219.7,243.5,247.6,263.6,267.8,279.0])
v,n=V_of(mp);            print(f"   pooled  (C4..C14)      V = {v:6.2f}   ({n} cells)")
v,n=V_of(mp[C%2==0]);    print(f"   even-C sub-channel     V = {v:6.2f}   ({n} cells)")
v,n=V_of(mp[C%2==1]);    print(f"   odd-C  sub-channel     V = {v:6.2f}   ({n} cells)")

print("\nB. nuclear binding energy, nine chains: pooled vs parity-resolved")
print(f"   {'chain':6}{'pooled V':>10}{'even-N V':>11}{'odd-N V':>10}{'ratio':>9}")
tot=[]
for el,(Z,rows) in CH.items():
    A=np.array([r[0] for r in rows],float); B=np.array([r[0]*r[1] for r in rows])
    N=(A-Z).astype(int)
    vp,_=V_of(B); ve,ne=V_of(B[N%2==0]); vo,no=V_of(B[N%2==1])
    sub=np.nanmean([ve,vo]); tot.append((vp,sub))
    print(f"   {el:6}{vp:10.2f}{ve:11.2f}{vo:10.2f}{sub/vp:9.1f}x")
tp=np.array(tot)
print(f"   mean pooled V = {tp[:,0].mean():.2f}   mean resolved V = {tp[:,1].mean():.1f}   lift = {tp[:,1].mean()/tp[:,0].mean():.0f}x")

print("\nC. controls: sequences with NO superposition should not move")
for name,y in [("Ba I 6s-nf binding energies (Ritz-smooth, synthetic)", 1/np.arange(5,20.)**2*1e5),
               ("n-alkane boiling points C4-C14", [272.7,309.2,341.9,371.6,398.8,424.0,447.3,469.1,489.5,508.6,526.7]),
               ("n-alkane dHvap C5-C12", [26.4,31.6,36.6,41.5,46.6,51.4,56.6,61.5])]:
    y=np.asarray(y,float); i=np.arange(len(y))
    vp,_=V_of(y); ve,_=V_of(y[i%2==0]); vo,_=V_of(y[i%2==1])
    print(f"   {name:48s} pooled {vp:8.1f} -> resolved {np.nanmean([ve,vo]):8.1f}")