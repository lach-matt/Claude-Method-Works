"""Re-audit checks: Earnshaw, Trans. Camb. Phil. Soc. 7 (1842) 97-112 (Drive 12iiWL9w9aYRRJBskU60Lo0nEDN3e4hOS).
Checks Earnshaw's own steps: Art.3 (d2V sum = 0 -> hyperboloid), Art.11-12 (linearised motion, fixed
particles, P alone moveable, exponential 'translation'), Art.8 (evanescent case; shell example),
Art.15 (attraction and repulsion alike; any arrangement), Art.16 (power n: sum = (n-2)(...))."""
import sympy as sp, random, math
P=[];F=[]
def chk(n,ok): (P if ok else F).append(n); print(("PASS " if ok else "FAIL ")+n)
x,y,z=sp.symbols('x y z',real=True); n=sp.symbols('n',positive=True)
rr=sp.sqrt(x**2+y**2+z**2)
lap=lambda e: sp.diff(e,x,2)+sp.diff(e,y,2)+sp.diff(e,z,2)
chk("Art.3/15: d2V/dx2+d2V/dy2+d2V/dz2 = 0 for V = m/D (away from the particle), either sign of m", sp.simplify(lap(1/rr))==0)
chk("Art.16: for force ~ 1/D^n, V ~ D^-(n-1)/(n-1): sum of 2nd derivs = (n-2) D^-(n+1) (zero only at n=2)",
    sp.simplify(lap(rr**(-(n-1))/(n-1)) - (n-2)*rr**(-(n+1)))==0)
# Art.11-12: fixed sources of random signs; find an equilibrium of the moveable particle; Hessian traceless,
# and (symmetric) has a positive eigenvalue -> x'' = +a^2 x -> C'e^{at}+C''e^{-at}
import numpy as np
random.seed(3); np.random.seed(3)
found=0; saddles=0
for trial in range(400):
    src=np.random.uniform(-1,1,(4,3)); q=np.random.choice([-1.0,1.0],4)*np.random.uniform(0.5,1.5,4)
    def grad(p):
        d=p-src; D=np.linalg.norm(d,axis=1); return -(q[:,None]*d/D[:,None]**3).sum(0)   # grad of V=sum q/D
    def hess(p):
        H=np.zeros((3,3))
        for s,qq in zip(src,q):
            d=p-s; D=np.linalg.norm(d); H+=qq*(3*np.outer(d,d)/D**5-np.eye(3)/D**3)
        return H
    p=np.random.uniform(-1,1,3)
    for it in range(60):
        H=hess(p); gv=grad(p)
        try: p=p-np.linalg.solve(H,gv)
        except np.linalg.LinAlgError: break
        if np.linalg.norm(gv)<1e-12: break
    if np.linalg.norm(grad(p))<1e-10 and np.min(np.linalg.norm(p-src,axis=1))>1e-3:
        found+=1; H=hess(p); ev=np.linalg.eigvalsh(H)
        if abs(np.trace(H))<1e-8*np.abs(ev).max() and ev.max()>0 and ev.min()<0: saddles+=1
print("   equilibria found:",found," with traceless Hessian of mixed signature:",saddles)
chk("Art.12/15: every equilibrium among fixed mixed-sign sources has d2V of both signs (one direction of 'translation')", found>10 and saddles==found)
t,a=sp.symbols('t a',positive=True); X=sp.Function('X')
sol=sp.dsolve(sp.Eq(X(t).diff(t,2),a**2*X(t)))
chk("Art.12: x'' = a^2 x integrates to C'e^{at}+C''e^{-at} ('a result which shews that x must increase continually')", 'exp(a*t)' in str(sol.rhs) and 'exp(-a*t)' in str(sol.rhs))
# Art.8: particle inside a spherical surface of attracting particles: unattracted (V constant) -- shell theorem
R,rho,u=sp.symbols('R rho u',positive=True)
Vin=sp.integrate(2*sp.pi*R**2*sp.sin(u)/sp.sqrt(R**2+rho**2-2*R*rho*sp.cos(u)),(u,0,sp.pi))
Vin=sp.simplify(Vin.subs(rho,R/3)); Vin2=sp.simplify(sp.integrate(2*sp.pi*R**2*sp.sin(u)/sp.sqrt(R**2+(R/2)**2-2*R*(R/2)*sp.cos(u)),(u,0,sp.pi)))
chk("Art.8 example: V inside a uniform spherical shell is the same at rho=R/3 and R/2 (=4 pi R): degenerate case", sp.simplify(Vin-Vin2)==0 and sp.simplify(Vin-4*sp.pi*R)==0)
# Art.16/19-22 escape: repulsive power n>2 plus Newtonian attraction can give all d2V negative (stable in all directions)
# 1-D lattice check of sign: V = sum_j [ mu/D_j - m/((n-1) D_j^(n-1)) ]  ... Earnshaw's own Art.20 form; laplacian = -(n-2) m sum D^-(n+1) <0 for n>2
mu,m=sp.symbols('mu m',positive=True)
Vr=mu/rr - m*rr**(-(n-1))/(n-1)
chk("Art.20: with Newtonian attraction mu/D plus repulsion ~1/D^n, lap V = -(n-2) m D^-(n+1): independent of mu, negative for n>2",
    sp.simplify(lap(Vr)+(n-2)*m*rr**(-(n+1)))==0)
print("\n%d PASS, %d FAIL"%(len(P),len(F))); raise SystemExit(1 if F else 0)
