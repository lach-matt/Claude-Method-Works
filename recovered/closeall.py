import numpy as np
from scipy.optimize import brentq
print("="*88)
print("  TESTING THE OMITTED OBJECTS")
print("="*88)
def sgn3(y):
    d1=np.diff(y); d2=np.diff(d1); d3=np.diff(d2)
    f=lambda d: all(np.sign(d)==np.sign(d[0]))
    return f(d1),f(d2),f(d3)
def V(f,x,h):
    a,m,b=f(x-h),f(x),f(x+h); e=abs(m-(a+b)/2)
    return abs(b-a)/e if e>1e-300 else float('inf')
print("\n  %-34s%10s%10s%12s%14s"%("family","monotone","convex","3-monotone","V"))
print("  "+"-"*82)
R=lambda rho: 2.44*(rho)**(-1/3)
x=np.linspace(0.5,3.0,9); y=np.array([R(t) for t in x])
m,c,t=sgn3(y); print("  %-34s%10s%10s%12s%14.1f"%("Roche limit vs density ρ^(−1/3)",m,c,t,V(R,1.5,0.25)))
J=lambda m2: 0.9*m2+0.5
x=np.linspace(1,9,9); y=np.array([J(t) for t in x])
m,c,t=sgn3(y); print("  %-34s%10s%10s%12s%14s"%("Regge J = α′m² + α₀",m,c,t,"INFINITE"))
cc=lambda D: D
x=np.arange(2,11); y=np.array([cc(t) for t in x])
m,c,t=sgn3(y); print("  %-34s%10s%10s%12s%14s"%("central charge c = D",m,c,t,"INFINITE"))
def L1(mu):
    f=lambda z: z-(1-mu)/(z+mu)**2+mu/(z-1+mu)**2
    return brentq(f,-mu+1e-9,1-mu-1e-9,xtol=1e-14)
def hill_r(mu): return (mu/3)**(1/3)
x=np.linspace(0.01,0.08,9); y=np.array([hill_r(t) for t in x])
m,c,t=sgn3(y); print("  %-34s%10s%10s%12s%14.1f"%("Hill radius (μ/3)^(1/3)",m,c,t,V(hill_r,0.04,0.005)))
def dN(Nmax=32,D=24):
    cc2=[0]*(Nmax+1); cc2[0]=1
    for n in range(1,Nmax+1):
        for _ in range(D):
            for k in range(n,Nmax+1): cc2[k]+=cc2[k-n]
    return cc2
d=dN()
ld=np.log(np.array([d[n] for n in range(3,31)],dtype=float))
m,c,t=sgn3(ld); print("  %-34s%10s%10s%12s%14.1f"%("log d(N), string degeneracy",m,c,t,
      abs(ld[12]-ld[10])/abs(ld[11]-(ld[10]+ld[12])/2)))
print("""
  **Regge trajectories and the central charge are EXACTLY LINEAR — both on
  the pole**, joining L4, L5 and the string mass spectrum. **The Roche limit
  and the Hill radius are ordinary bracketable channels.**
""")
print("="*88)
print("  AND THE LAGRANGE STABILITY THRESHOLD")
print("="*88)
mu_c=(1-np.sqrt(1-4/27*(1)))/2
mu_crit=0.5*(1-np.sqrt(69)/9)
print("""
  L4/L5 are linearly stable for μ < μ_crit = (1 − √(69)/9)/2.
""")
print("     μ_crit = %.7f"%mu_crit)
print("     Earth–Moon μ = 0.01215  -> stable : %s"%(0.01215<mu_crit))
print("     Sun–Jupiter μ = 0.000954 -> stable : %s"%(0.000954<mu_crit))
print("""
  **That is a THRESHOLD, not a family** — a single number, not a sequence.
  **The bracket has nothing to act on**, which is itself the finding: the
  method applies to families and is silent on thresholds.
""")
print("="*88)
print("  THE CALABI–YAU DENOMINATOR")
print("="*88)
a=248305; u=495515; both=2*a-u; N=473800776
print("\n     both ≥ 140 / all polytopes        : %.6f%%"%(100*both/N))
print("     both ≥ 140 / those with one ≥ 140 : %.3f%%   <- the meaningful one"%(100*both/u))
print("     ratio of the two statements       : %.0f×"%((both/u)/(both/N)))