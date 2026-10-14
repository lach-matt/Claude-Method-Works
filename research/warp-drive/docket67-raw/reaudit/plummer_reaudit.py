"""Re-audit checks: Plummer, MNRAS 71 (1911) 460-470, read as page images (Drive 1SiEv9SIOU1HSb8Tftnl1tI4A2hIXHPwC).
Plummer prints the DENSITY phi = N(1+r^2)^(-5/2) (eq 11,12; units with a=1), strip counts F, Sigma (12) and
projected f, sigma (13); he does NOT print the 3-D enclosed mass or the potential.  The tree's fraction
1-(1+(a/R)^2)^(-3/2) (linstab.py:217, 547-551) is checked here as one integration of Plummer's own eq (12)."""
import sympy as sp, math, sys
sys.path.insert(0,'/home/user/Claude-Method-Works/research/warp-drive')
P=[];F=[]
def chk(n,ok): (P if ok else F).append(n); print(("PASS " if ok else "FAIL ")+n)
r,rho,N,y,z,a,R,q=sp.symbols('r rho N y z a R q',positive=True)
phi=N*(1+rho**2)**sp.Rational(-5,2)
# Plummer eq (1): F(r) = int_r^R 2 pi rho phi(rho) d rho, R -> inf
Fr=sp.integrate(2*sp.pi*rho*phi,(rho,r,sp.oo))
chk("eq(12) F(r) = (2/3) pi N (1+r^2)^(-3/2)", sp.simplify(Fr-sp.Rational(2,3)*sp.pi*N*(1+r**2)**sp.Rational(-3,2))==0)
Sig=sp.integrate(Fr.subs(r,y),(y,0,r))
chk("eq(12) Sigma(r) = (2/3) pi N r (1+r^2)^(-1/2)", sp.simplify(Sig-sp.Rational(2,3)*sp.pi*N*r/sp.sqrt(1+r**2))==0)
fr=sp.simplify(2*sp.integrate(phi.subs(rho,sp.sqrt(r**2+z**2)),(z,0,sp.oo)))
chk("eq(13) f(r) = (4/3) N (1+r^2)^(-2)  ['definite integral equal to 2/3']", sp.simplify(fr-sp.Rational(4,3)*N*(1+r**2)**-2)==0)
chk("  the q-integral int_0^inf dq/(1+q^2)^(5/2) = 2/3", sp.integrate((1+q**2)**sp.Rational(-5,2),(q,0,sp.oo))==sp.Rational(2,3))
sig=sp.integrate(2*sp.pi*y*fr.subs(r,y),(y,0,r))
chk("eq(13) sigma(r) = (4/3) pi N r^2 (1+r^2)^(-1)", sp.simplify(sig-sp.Rational(4,3)*sp.pi*N*r**2/(1+r**2))==0)
chk("p.468 test {Sigma}^2/sigma = pi N/3 = Sigma(inf)/2", sp.simplify(Sig**2/sig-sp.pi*N/3)==0 and sp.limit(Sig,r,sp.oo)==2*sp.pi*N/3)
# Plummer's own mass relation p.462: dm/dr = 4 pi r^2 phi  (Newtonian, flat space)
m=sp.integrate(4*sp.pi*rho**2*phi,(rho,0,r))
chk("dm/dr = 4 pi r^2 phi integrated: m(r) = (4/3) pi N r^3 (1+r^2)^(-3/2)", sp.simplify(m-sp.Rational(4,3)*sp.pi*N*r**3*(1+r**2)**sp.Rational(-3,2))==0)
M=sp.limit(m,r,sp.oo)
out=sp.simplify(1-m/M)
# restore scale a: r -> R/a
tree=1-(1+(a/R)**2)**sp.Rational(-3,2)
chk("fraction outside R (sphere) = 1-(1+(a/R)^2)^(-3/2): the tree's formula", sp.simplify(out.subs(r,R/a)-tree)==0)
proj_out=sp.simplify(1-sig/sp.limit(sig,r,sp.oo))
chk("CONTRAST: Plummer's PROJECTED (cylinder) fraction outside is 1/(1+r^2), not the tree's", sp.simplify(proj_out-1/(1+r**2))==0 and sp.simplify(proj_out-out)!=0)
# Newtonian potential of Plummer's density (not printed by Plummer): Poisson
G=sp.symbols('G',positive=True)
Phi=-G*M/sp.sqrt(r**2+1)
lap=sp.simplify(sp.diff(r**2*sp.diff(Phi,r),r)/r**2)
chk("Poisson: lap(-GM/sqrt(r^2+1)) = 4 pi G phi  (the potential pair is DERIVED, not in Plummer)", sp.simplify(lap-4*sp.pi*G*phi.subs(rho,r))==0)
# gamma: Plummer uses Schuster's gamma = 1.2 -> polytrope index n = 1/(gamma-1) = 5
chk("Schuster gamma = 1.2 is polytrope n = 5", sp.Rational(1,sp.Rational(6,5)-1)==5)
# Plummer's numbers
x=1.5/7.14; C1=3540*x/math.sqrt(1+x*x); print("   Table I C at r=1'.5 (unit 7'.14):",round(C1,1),"printed 727")
chk("Table I: Sigma=3540 r/sqrt(1+r^2) at r=1.5/7.14 ~ printed 727 (+-1)", abs(C1-727)<1.5)
chk("p.465 'expect 7080 stars' = 2 x 3540", 2*3540==7080)
chk("p.468-9: sigma = 1160 r^2/(1+r^2), 1160 = (4/3) pi N -> N = 277", round(1160*3/(4*math.pi))==277)
chk("  Table V C at r=0'.5 (unit 2'): 1160*.0625/1.0625 = 68", round(1160*0.25**2/(1+0.25**2))==68)
chk("  phi = 277/(2')^3 = 34.6 per (1')^3", round(277/8,1)==34.6)
# the tree's datum
import concentric, linstab
f=1-(1+(concentric.A_CORE/concentric.R_SHELL)**2)**-1.5
fx=sp.N(tree.subs({a:sp.Rational(1,50),R:200}),30)
print("   tree data a=%s R_s=%s: f = %s (float %.10e)"%(concentric.A_CORE,concentric.R_SHELL,fx,f))
chk("tree's f = 1.4999999813e-8 at a=0.02, R_s=200", abs(float(fx)-1.49999998125e-8)<1e-18)
print("\n%d PASS, %d FAIL"%(len(P),len(F))); raise SystemExit(1 if F else 0)
