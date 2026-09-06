"""lam1_zeta.py -- s23: Loos-Gill 2011 closed-form lambda_1(zeta) = lam1a(0)*Lam1a(zeta) + lam1b(0)*Lam1b(zeta) (their Eqs 16,17; Li2 via scipy spence)."""
import numpy as np
from scipy.special import spence
al=(9*np.pi/4)**(-1/3)
L1A0=al/(24*np.pi**3)*(np.pi**2-6); L1B0=al/(4*np.pi**3)*(np.pi**2-12*np.log(2))
def Li2(z): return spence(1-z)
def lam1(z):
    z=np.clip(np.asarray(z,float),1e-9,1-1e-12)                      # zeta=0 limit is regular; tiny offset avoids 0/0
    kd=(1-z)**(1/3); ku=(1+z)**(1/3); s2=kd*kd+ku*ku; d2=kd*kd-ku*ku
    r=(kd-ku)/(kd+ku)
    La=3/(np.pi**2-6)*((np.pi**2/6+0.25)*s2-1.5*kd*ku-s2/d2*kd*ku*np.log(kd/ku)-d2/2*(Li2(r)-Li2(-r)))
    Lb=3/(np.pi**2-12*np.log(2))*(np.pi**2/6*s2+(1-np.log(2))*(kd-ku)**2-kd*kd/2*Li2(r)-ku*ku/2*Li2(-r)
        +1/(kd*ku)*(kd**4*np.log(kd/(kd+ku))+kd*kd*ku*ku*np.log(kd*ku/(kd+ku)**2)+ku**4*np.log(ku/(kd+ku))))
    return L1A0*La+L1B0*Lb
if __name__=="__main__":
    print("lam1(0)",float(lam1(0.0)),"exact",al/(4*np.pi**3)*(7*np.pi**2/6-12*np.log(2)-1))
    print("lam1(1)",float(lam1(1.0)),"exact",2**(-4/3)*al/(4*np.pi**3)*(13*np.pi**2/12-12*np.log(2)+0.5))
    print("lam1(0.5)",float(lam1(0.5)),"lam1(0.996)",float(lam1(0.996)))