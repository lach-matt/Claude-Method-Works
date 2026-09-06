import numpy as np, tfd
from derive_P import numerov_wf, slater_Fk
import warnings; warnings.filterwarnings("ignore")
def Fk_ref(r,u,ks):
    # dense trapezoid double integral (reference), analytic u
    w=u*u*np.gradient(r); out={}
    for k in ks:
        A=np.cumsum(w*r**k)-0.5*w*r**k
        out[k]=2*np.sum(w*A/r**(k+1))
    return out
r=np.linspace(1e-6,80,400001)
u1s=2*r*np.exp(-r); u3d=(4/(81*np.sqrt(30)))*r**3*np.exp(-r/3)
u1s/=np.sqrt(np.trapz(u1s**2,r)); u3d/=np.sqrt(np.trapz(u3d**2,r))
print("analytic H1s F0",Fk_ref(r,u1s,(0,)))
print("analytic H3d",Fk_ref(r,u3d,(0,2,4)))
Vh=lambda r:-1/r
for npts in (3000,6000,12000):
    rr,dr,u,E,nd=numerov_wf(Vh,2,3,1.0,1,npts=npts)
    print(npts,"numerov H3d",{k:round(v,5) for k,v in slater_Fk(rr,dr,u,(0,2,4)).items()},"E",round(E,6))