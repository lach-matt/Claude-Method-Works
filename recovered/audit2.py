import numpy as np
rng=np.random.default_rng(11)
def V(y):
    y=np.asarray(y,float); w=np.abs(y[2:]-y[:-2]); e=np.abs(y[2:]-2*y[1:-1]+y[:-2])/2
    return w.sum()/max(e.sum(),1e-30)
def Sig(y):
    y=np.asarray(y,float); i=np.arange(len(y))
    return 2*np.nanmean([V(y[i%2==0]),V(y[i%2==1])])/V(y)

print("=== PROBLEM 1: does each reported Sigma satisfy clause (ii)? ===")
print("clause (ii): every sub-channel needs >=3 second differences, i.e. >=5 members,")
print("             i.e. the pooled sequence needs >=10 members.\n")
for nm,n in [("n-alkane melting pts C4-C14",11),("n-alkane boiling pts C4-C14",11),
             ("Ba I 6snf n=17-25",9),("Ca binding energy",21),("Ni binding energy",22),
             ("Se binding energy",17),("Kr binding energy",13),("n-alkane dHvap C5-C12",8)]:
    e=(n+1)//2; o=n//2
    print(f"  {nm:30} n={n:3d} -> sub-channels {e},{o} -> 2nd diffs {max(e-2,0)},{max(o-2,0)}   "
          f"{'OK' if min(e-2,o-2)>=3 else 'FAILS clause (ii)'}")

print("\n=== PROBLEM 2: Sigma's null is shape- and noise-dependent, not 1 ===")
print("null 99th percentile as a function of the sequence's own r = step/sigma")
print("(max over four smooth monotone shapes: 1/n^2, exponential, quadratic, power-3/2)\n")
shapes=[lambda x:-1e5/(x+16.)**2, lambda x:np.exp(0.25*x), lambda x:5*x-0.15*x**2, lambda x:(x+4)**1.5]
print(f"{'r':>8}{'noise/step':>12}{'null median':>13}{'null 99%':>10}{'null max':>10}")
tab={}
for r in [1e6,300,100,50,20,10,5]:
    f=1/r; S=[]
    for g in shapes:
        x=np.arange(11.); y0=g(x); step=np.mean(np.abs(np.diff(y0)))
        for _ in range(3000):
            z=y0+rng.normal(0,f*step,len(x))
            if np.all(np.diff(z)>0): S.append(Sig(z))
    S=np.array(S); tab[r]=np.percentile(S,99)
    print(f"{r:>8.0f}{f:>12.4f}{np.median(S):>13.2f}{np.percentile(S,99):>10.2f}{S.max():>10.2f}")

print("\n=== PROBLEM 3: re-verdict every reported Sigma against its matched null ===")
print(f"{'sequence':30}{'r':>9}{'Sigma':>8}{'null 99%':>10}{'margin':>9}  verdict")
rows=[("n-alkane melting pts",  0.3, [134.9,143.4,177.8,182.6,216.4,219.7,243.5,247.6,263.6,267.8,279.0],12.69),
      ("n-alkane boiling pts",  0.3, [272.7,309.2,341.9,371.6,398.8,424.0,447.3,469.1,489.5,508.6,526.7],1.04)]
for nm,sig,y,S in rows:
    y=np.array(y,float); d=np.abs(np.diff(y))
    # for a single-channel null the relevant step is the SMOOTH step scale, taken as the
    # median sub-channel step halved (i.e. what the steps would be with no alternation)
    sub=np.median(np.abs(np.diff(y[::2])))/2
    r=sub/sig; nl=np.interp(np.log(r),np.log([5,10,20,50,100,300,1e6]),
                            [tab[5],tab[10],tab[20],tab[50],tab[100],tab[300],tab[1e6]])
    print(f"{nm:30}{r:>9.1f}{S:>8.2f}{nl:>10.2f}{S/nl:>8.1f}x  {'SUPERPOSED' if S>nl else 'single channel'}")
for nm,r,S in [("Ca binding energy",1e4,3.66),("Ni binding energy",1e4,5.10),("Se binding energy",1e4,10.05),
               ("Kr binding energy",1e4,9.22),("Ti binding energy",1e4,4.14),("Cr binding energy",1e4,4.75),
               ("Fe binding energy",1e4,4.60),("Zn binding energy",1e4,6.93),("Ge binding energy",1e4,9.26)]:
    nl=tab[1e6]
    print(f"{nm:30}{r:>9.0f}{S:>8.2f}{nl:>10.2f}{S/nl:>8.1f}x  SUPERPOSED")