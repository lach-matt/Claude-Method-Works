"""gs3_brute.py -- G-S3: brute MC of the screened SOX (q sampled uniformly on [0,qmax]; k1,k2 in the sphere of radius x_sigma; F(Pi(q)) inside)
vs the reduced sox_scr at (rs,zeta) = (2,0),(2,1). Independent path: no S(q) table, no scaling law, no PCHIP. Both truncated at qmax=12 for the comparison."""
import numpy as np, sox_scr as X, ring_zeta as R, sys
rs=2.0; qmax=12.0; N=int(sys.argv[1]) if len(sys.argv)>1 else 20_000_000; chunk=1_000_000
def brute(z,seed):
    rng=np.random.default_rng(seed); xp,xm=R.xs(z); tot=0.0; tot2=0.0; n=0
    while n<N:
        m=min(chunk,N-n); q=qmax*rng.random(m); acc=np.zeros(m)
        Fq=X.F(X.Pi(np.maximum(q,1e-9),rs,z))
        for x in (xp,xm):
            if x<=0: continue
            kmin=np.maximum(0.0,x-q); Vsh=4*np.pi/3*(x**3-kmin**3); Rr=q+2*x
            k=np.cbrt(kmin**3+rng.random(m)*(x**3-kmin**3)); ct=2*rng.random(m)-1; ph=2*np.pi*rng.random(m); st=np.sqrt(1-ct*ct)
            k1=np.stack([k*st*np.cos(ph),k*st*np.sin(ph),k*ct],1); ok1=(k*k+2*q*k1[:,2]+q*q)>x*x
            use_r=rng.random(m)<0.5
            r=Rr*rng.random(m); ct2=2*rng.random(m)-1; ph2=2*np.pi*rng.random(m); st2=np.sqrt(1-ct2*ct2)
            rv=np.stack([r*st2*np.cos(ph2),r*st2*np.sin(ph2),r*ct2],1); k2r=-k1+rv; k2r[:,2]-=q
            kb=np.cbrt(kmin**3+rng.random(m)*(x**3-kmin**3)); ctb=2*rng.random(m)-1; phb=2*np.pi*rng.random(m); stb=np.sqrt(1-ctb*ctb)
            k2s=np.stack([kb*stb*np.cos(phb),kb*stb*np.sin(phb),kb*ctb],1); k2=np.where(use_r[:,None],k2r,k2s)
            n2=np.einsum('ij,ij->i',k2,k2); ok2=(n2<x*x)&((n2+2*q*k2[:,2]+q*q)>x*x)
            rvec=k2+k1; rvec[:,2]+=q; r2=np.einsum('ij,ij->i',rvec,rvec); insh=(n2<x*x)&(n2>=kmin*kmin); inr=r2<Rr*Rr
            pmix=0.5*insh/Vsh+0.5*inr/(4*np.pi*Rr*np.maximum(r2,1e-300)); D=q*q+q*(k1[:,2]+k2[:,2]); ok=ok1&ok2&(D>0)&(pmix>0)
            acc+=Vsh*np.where(ok,1.0/np.where(ok,r2*D*pmix,1.0),0.0)
        w=qmax*acc*Fq            # int_0^qmax dq S_sigma-sum(q) F(q)
        tot+=w.sum(); tot2+=(w*w).sum(); n+=m
    mean=tot/n; se=np.sqrt(max(tot2/n-mean*mean,0)/n); pref=3/(32*np.pi**5)*4*np.pi/2
    return pref*mean, pref*se
def reduced(z):
    xp,xm=R.xs(z); tot=0.0
    for x in (xp,xm):
        if x<=0: continue
        m=X.QQ<=qmax/x; Fq=X.F(X.Pi(x*X.QQ[m],rs,z)); tot+=x**3*(np.trapezoid(X.SQQ[m]*Fq,X.QQ[m])+X.QQ[0]*X.SQQ[0]/2*Fq[0])
    return 3/(32*np.pi**5)*4*np.pi*tot/2
for z,seed in ((0.0,11),(1.0,13)):
    b,se=brute(z,seed); r=reduced(z); print(f"G-S3 (rs 2, zeta {z}): brute {b:.6f} +- {se:.6f}  reduced {r:.6f}  diff {b-r:+.2e} = {(b-r)/se:+.1f} se  ->",'PASS' if abs(b-r)<3*se else 'FAIL',flush=True)