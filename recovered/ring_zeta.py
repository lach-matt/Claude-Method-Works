"""ring_zeta.py -- s23: RPA ring-sum correlation energy of the spin-polarised UEG from Benites-Rosado-Manousakis 2024 Eqs 12-14.
eps_r(rs,zeta) in Ry; c0(zeta) = lim eps_r - cL ln rs. Numerics: log grids in kappa,x; trapezoid. usage: python3 ring_zeta.py zeta [rs...]"""
import numpy as np, sys
al=(4/(9*np.pi))**(1/3)
def xs(z): return (1+z)**(1/3),(1-z)**(1/3)
def g(q,nu):
    kp=q+q*q/2; km=q-q*q/2
    with np.errstate(divide='ignore',invalid='ignore'):
        t=1+(nu*nu+kp*km)/(2*q**3)*np.log((kp*kp+nu*nu)/(km*km+nu*nu))-(nu/q)*(np.arctan(kp/nu)+np.arctan(km/nu))
    return t
def cL(z):
    xp,xm=xs(z); chi=xp+xm
    return (1/np.pi**2)*((1-np.log(2))+xp*xm/2*chi-np.log(chi)+0.5*(xp**3*np.log(xp)+xm**3*np.log(xm)))  # Eq.16 as printed (see note)
def eps_r(rs,z,nk=1400,nx=1400):
    xp,xm=xs(z); k=np.exp(np.linspace(np.log(1e-4),np.log(60.0),nk)); x=np.exp(np.linspace(np.log(1e-4),np.log(1e3),nx))
    K,X=np.meshgrid(k,x,indexing='ij')
    Pi=(al*rs/(np.pi*K*K))*sum(s*g(K/s,K*X/(s*s)) for s in (xp,xm) if s>0)
    f=K**3*(np.log1p(Pi)-Pi)
    inner=np.trapz(f,x,axis=1)
    return 3/(2*np.pi*al*al*rs*rs)*np.trapz(inner,k)
if __name__=="__main__":
    z=float(sys.argv[1]); rss=[float(a) for a in sys.argv[2:]] or [0.02,0.01,0.005]
    for rs in rss:
        e=eps_r(rs,z); print(f"zeta {z} rs {rs}  eps_r {e:.5f} Ry  eps_r-cL ln rs = {e-cL(z)*np.log(rs):.5f} Ry  = {(e-cL(z)*np.log(rs))/2:.5f} Ha", flush=True)