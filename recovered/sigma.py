import numpy as np
exec(open('chart.py').read().split('print(f"{')[0])
# For a SMOOTH single channel: w ~ 2h*y', e ~ h^2*y''/2, so V ~ 4y'/(h y'') -- V halves when h doubles.
# Define the superposition statistic  S = 2 * V_resolved / V_pooled.   S ~ 1 => one channel.  S >> 1 => two.
def V(y):
    y=np.asarray(y,float)
    if len(y)<3: return np.nan
    w=np.abs(y[2:]-y[:-2]); e=np.abs(y[2:]-2*y[1:-1]+y[:-2])/2
    return w.sum()/max(e.sum(),1e-30)
def W(y):
    y=np.asarray(y,float); return np.abs(y[2:]-y[:-2]).mean()
def sigma(y):
    y=np.asarray(y,float); i=np.arange(len(y))
    return 2*np.nanmean([V(y[i%2==0]),V(y[i%2==1])])/V(y)

print(f"{'sequence':42}{'V pooled':>10}{'V split':>9}{'Sigma':>8}{'width pooled':>14}{'width split':>13}")
cases=[]
C=np.arange(4,15)
mp=np.array([134.9,143.4,177.8,182.6,216.4,219.7,243.5,247.6,263.6,267.8,279.0])
cases.append(("n-alkane melting points C4-C14",mp,"K"))
cases.append(("n-alkane boiling points C4-C14",np.array([272.7,309.2,341.9,371.6,398.8,424.0,447.3,469.1,489.5,508.6,526.7]),"K"))
for el in ['Ca','Ni','Se']:
    Z,rows=CH[el]; A=np.array([r[0] for r in rows],float)
    cases.append((f"{el} binding energy, A={int(A[0])}-{int(A[-1])}",np.array([r[0]*r[1] for r in rows])/1000,"MeV"))
cases.append(("Rydberg-like 1/n^2 (smooth control)",1e5/np.arange(5,20.)**2,"cm-1"))
cases.append(("n-alkane dHvap C5-C12 (rounding-limited)",np.array([26.4,31.6,36.6,41.5,46.6,51.4,56.6,61.5]),"kJ/mol"))
for name,y,u in cases:
    i=np.arange(len(y)); vs=np.nanmean([V(y[i%2==0]),V(y[i%2==1])])
    ws=np.nanmean([W(y[i%2==0]),W(y[i%2==1])])
    print(f"{name:42}{V(y):10.2f}{vs:9.1f}{sigma(y):8.2f}{W(y):11.2f} {u:<3}{ws:10.2f} {u}")

print("\nSigma across all nine nuclear chains:")
sg=[]
for el,(Z,rows) in CH.items():
    A=np.array([r[0] for r in rows],float); B=np.array([r[0]*r[1] for r in rows]); N=(A-Z).astype(int)
    y=B; i=(np.arange(len(y))+ (N[0]%2))%2
    S=2*np.nanmean([V(B[N%2==0]),V(B[N%2==1])])/V(B); sg.append(S)
    print(f"   {el:3} Sigma = {S:5.2f}")
print(f"   mean {np.mean(sg):.2f}, min {min(sg):.2f}, max {max(sg):.2f}  (single-channel expectation: 1)")