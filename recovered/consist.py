import numpy as np
exec(open('chart.py').read().split('print(f"{')[0])
rng=np.random.default_rng(3)
def V(y):
    y=np.asarray(y,float); w=np.abs(y[2:]-y[:-2]); e=np.abs(y[2:]-2*y[1:-1]+y[:-2])/2
    return w.sum()/max(e.sum(),1e-30)
def Sig(y):
    y=np.asarray(y,float); i=np.arange(len(y))
    return 2*np.nanmean([V(y[i%2==0]),V(y[i%2==1])])/V(y)

print("=== Ni chain: which min r, and over which A range? ===")
Z,rows=CH['Ni']; A=np.array([r[0] for r in rows],float)
B=np.array([r[0]*r[1] for r in rows]); sB=np.array([r[0]*r[2] for r in rows])
for lo,hi,lbl in [(52,73,'A=52-73 (20 cells, sec 10.4)'),(56,73,'A=56-73 (16 cells, sec 10.3)')]:
    m=(A>=lo)&(A<=hi); a,b,sb=A[m],B[m],sB[m]
    single=[min(abs(b[i]-b[i-1]),abs(b[i+1]-b[i]))/sb[i] for i in range(1,len(a)-1)]
    comb=[min(abs(b[i]-b[i-1])/np.hypot(sb[i],sb[i-1]),abs(b[i+1]-b[i])/np.hypot(sb[i],sb[i+1])) for i in range(1,len(a)-1)]
    print(f"  {lbl}: min r single-sigma {min(single):7.0f}   min r hypot {min(comb):7.0f}")

print("\n=== Ba I 6snf n=17-25: clause (ii), Sigma, and the POWER of the test ===")
y=np.array([41647.85,41689.80,41725.39,41755.48,41782.02,41804.59,41824.30,41841.63,41856.85])
i=np.arange(9)
print(f"  members 9 -> sub-channels {(i%2==0).sum()},{(i%2==1).sum()} -> 2nd diffs "
      f"{(i%2==0).sum()-2},{(i%2==1).sum()-2}   clause (ii) needs >=3 in each: "
      f"{'PASS' if min((i%2==0).sum()-2,(i%2==1).sum()-2)>=3 else 'FAIL'}")
print(f"  Sigma = {Sig(y):.3f}")
# power: inject a real period-2 alternation of amplitude A into a 9-member Rydberg-like series
def power(nmem,amp,sig,N=4000):
    x=np.arange(nmem); base=-1e5/(x+17.)**2; base=base-base[0]
    d=np.diff(base); d=d*(1+amp*(-1)**np.arange(len(d)))
    yy=np.concatenate([[0],np.cumsum(d)])
    nulls=[]
    for _ in range(N):
        z=np.concatenate([[0],np.cumsum(np.diff(base))])+rng.normal(0,sig,nmem)
        if np.all(np.diff(z)>0): nulls.append(Sig(z))
    thr=np.percentile(nulls,99)
    hits=0; tot=0
    for _ in range(N):
        z=yy+rng.normal(0,sig,nmem)
        if np.all(np.diff(z)>0):
            tot+=1; hits+= Sig(z)>thr
    return thr, hits/max(tot,1)
print("  power of Sigma at 9 members (sigma = 0.1 cm-1, the series' own):")
for amp in [0.05,0.10,0.20,0.40]:
    thr,pw=power(9,amp,0.1)
    print(f"    alternation amplitude {amp:4.2f}: null99 = {thr:5.2f}, detection power = {100*pw:5.1f}%")
print("  power at 21 members for comparison (a nuclear-chain length):")
for amp in [0.05,0.10,0.20]:
    thr,pw=power(21,amp,0.1)
    print(f"    alternation amplitude {amp:4.2f}: null99 = {thr:5.2f}, detection power = {100*pw:5.1f}%")