# tfd.py -- Thomas-Fermi-Dirac ion, shooting on slope; Latter tail; V_eff = V_es + V_x(local).
import numpy as np
from scipy.integrate import solve_ivp
def _integrate(slope, beta, xmax=60.0):
    x0=1e-6; y0=[1+slope*x0+(4/3)*x0**1.5, slope+2*x0**0.5]
    def f(x,y):
        p=max(y[0],0.0); return [y[1], x*(np.sqrt(p/x)+beta)**3]
    def hit(x,y): return y[0]-beta*beta*x/16.0
    hit.terminal=True; hit.direction=-1
    return solve_ivp(f,(x0,xmax),y0,events=hit,rtol=1e-10,atol=1e-13,dense_output=True,max_step=0.2)
def tfd_ion(Z,N):
    q=Z-N; beta=0.21178*Z**(-2/3); target=q/Z
    lo,hi=-40.0,-1.2   # steeper slope -> boundary charge larger
    for _ in range(80):
        s=0.5*(lo+hi); sol=_integrate(s,beta)
        if sol.status==1:
            x0=sol.t_events[0][0]; ph,dph=sol.y_events[0][0]; g=ph-x0*dph
            if g>target: lo=s
            else: hi=s
        else: hi=s   # never reached boundary: too gentle? (phi stays above line) -> steeper
    sol=_integrate(s,beta); x0=sol.t_events[0][0]
    return sol,x0,beta
def potential(Z,charge):
    N=Z-charge; q=charge
    sol,x0,beta=tfd_ion(Z,N); b=0.88534*Z**(-1/3); r0=b*x0
    def V(r):
        r=np.asarray(r,float); x=r/b
        phi=np.where(x<x0,np.clip(sol.sol(np.minimum(x,x0))[0],0,None),0.0)
        psi=Z*phi/r
        Ves=-q/r0+1/(32*np.pi**2)-psi
        Vx=-(1/np.pi)*(1/np.pi+np.sqrt(2*psi))
        inner=Ves+Vx
        return np.where(x<x0,np.minimum(inner,-q/r),-q/r)
    return V,x0
if __name__=="__main__":
    for Z,N in [(19,18),(55,54),(21,18),(87,86)]:
        sol,x0,beta=tfd_ion(Z,N); print(f"Z={Z} N={N} x0={x0:.3f} r0={0.88534*Z**(-1/3)*x0:.3f} slope={sol.y[1][0]:.5f}")
