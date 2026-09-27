"""DOCKET 67 -- audit of 'LeMaitre & Poisson (2019): radial threshold Gamma_1' as wall.py uses it.
Independent sympy re-derivation.  Reads wall.py READ-ONLY (no bytecode written into the tree).
Checks:
 (A) Israel statics, Minkowski in / Schwarzschild out: mu, p from the junction conditions.
 (B) TURNING-POINT route (Pitre et al. Sec III, which cites LP2019 [34] for 'max mass = onset of radial
     instability'): dM/dsigma = 0 with dp = Gamma p/sigma dsigma, dmu = (mu+p)/sigma dsigma  -> Gamma_1.
 (C) DYNAMICAL route (equation of motion of the shell, V(R) potential): V''(R0)=0 -> beta2_crit = dp/dmu,
     converted with Pitre Eq (2.7) Gamma = beta2 (mu+p)/p.  Must equal (B) identically.
 (D) CONVENTION: per Pitre footnote 1, LP2019 Eq (34) defines the index as d ln p/d ln mu.  Compute the
     threshold in that convention and show it is NOT (3.16c) -- i.e. the printed (3.16c) is Pitre's form,
     not LP's printed form.  Newtonian limits of both.
 (E) wall.gamma1_published == (3.16c) with C = x/2.
"""
import sys, math
sys.dont_write_bytecode = True
import sympy as sp

ok = True
def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)

R, M, s, C = sp.symbols('R M s C', positive=True)
beta2, Gam = sp.symbols('beta2 Gamma', real=True)

# (A) statics from junction conditions: mu = (sqrt(f_in)-sqrt(f_out))/(4 pi R),
# p = (1/8pi)[ (f'/(2 sqrt f) + sqrt f / R)_out - (same)_in ]
f_out = 1 - 2*M/R
mu0 = (1 - sp.sqrt(f_out))/(4*sp.pi*R)
p0 = (sp.diff(f_out, R)/(2*sp.sqrt(f_out)) + sp.sqrt(f_out)/R - 1/R)/(8*sp.pi)
sub = {M: R*(1 - s**2)/2}       # s = sqrt(1-2M/R)
mu_s = sp.simplify(mu0.subs(sub)); p_s = sp.simplify(p0.subs(sub))
check("(A) mu = (1-s)/(4 pi R)", sp.simplify(mu_s - (1-s)/(4*sp.pi*R)) == 0)
check("(A) p = (1-s)^2/(16 pi R s)", sp.simplify(p_s - (1-s)**2/(16*sp.pi*R*s)) == 0)

# (B) turning point.  Invert (mu,p) -> (M,R): q = p/mu = (1-s)/(4s)  => s = 1/(1+4q);  R = (1-s)/(4 pi mu)
mu, p = sp.symbols('mu p', positive=True)
q = p/mu
s_q = 1/(1 + 4*q)
R_mp = (1 - s_q)/(4*sp.pi*mu)
M_mp = sp.simplify(R_mp*(1 - s_q**2)/2)
check("(B) M(mu,p) consistent with (A)", sp.simplify(M_mp.subs({mu: mu_s, p: p_s}) - R*(1-s**2)/2) == 0)
sig = sp.symbols('sigma', positive=True)
dMdsig = sp.diff(M_mp, mu)*(mu + p)/sig + sp.diff(M_mp, p)*Gam*p/sig
G1 = sp.solve(sp.Eq(dMdsig, 0), Gam)
check("(B) one root in Gamma", len(G1) == 1)
G1 = sp.simplify(G1[0])
check("(B) Gamma_1 = 3/2 + 4q + 4q^2   (Pitre 3.16a)", sp.simplify(G1 - (sp.Rational(3,2) + 4*q + 4*q**2)) == 0)
G316c = (4 - 6*C + 2*sp.sqrt(1 - 2*C))/(4*(1 - 2*C))
G1_s = sp.simplify((sp.Rational(3,2) + 4*q + 4*q**2).subs(q, (1-s)/(4*s)))
check("(B) (3.16a) == (3.16c) with C=(1-s^2)/2", sp.simplify(G1_s - G316c.subs(C, (1-s**2)/2)) == 0)
slope = sp.simplify(sp.diff(dMdsig, Gam))
check("(B) dM/dsigma increasing in Gamma (so >=0 iff Gamma>=Gamma_1)", sp.simplify(slope) .subs({mu:1,p:sp.Rational(1,10),sig:1}) > 0)

# (C) dynamical route.  m(R) = 4 pi R^2 mu(R); d(mu A) = -p dA  -> m' = -8 pi R p, and p' = beta2 mu'
# with mu' = -2(mu+p)/R.  Equation of motion: Rdot^2 + V = 0, V = 1 - (M/m + m/(2R))^2.
Rv = sp.symbols('Rv', positive=True)
mf = sp.Function('m')(Rv)
V = 1 - (M/mf + mf/(2*Rv))**2
m0, m1, m2 = sp.symbols('m0 m1 m2')
Vpp = sp.diff(V, Rv, 2).subs(sp.Derivative(mf, (Rv, 2)), m2).subs(sp.Derivative(mf, Rv), m1).subs(mf, m0)
Vp = sp.diff(V, Rv).subs(sp.Derivative(mf, Rv), m1).subs(mf, m0)
Vv = V.subs(mf, m0)
mu_R, p_R = mu_s.subs(R, Rv), p_s.subs(R, Rv)
dmu = -2*(mu_R + p_R)/Rv
dp = beta2*dmu
vals = {m0: 4*sp.pi*Rv**2*mu_R, m1: -8*sp.pi*Rv*p_R, m2: -8*sp.pi*(p_R + Rv*dp), M: Rv*(1-s**2)/2}
check("(C) V(R0) = 0", sp.simplify(Vv.subs(vals)) == 0)
check("(C) V'(R0) = 0", sp.simplify(Vp.subs(vals)) == 0)
Vpp0 = sp.simplify(Vpp.subs(vals))
b2c = sp.solve(sp.Eq(Vpp0, 0), beta2)
check("(C) one root in beta2", len(b2c) == 1)
b2c = sp.simplify(b2c[0])
check("(C) beta2_crit = (1-s)(3s^2+2s+1)/(4 s^2 (1+3s))  (wall.beta2_crit)",
      sp.simplify(b2c - (1-s)*(3*s**2+2*s+1)/(4*s**2*(1+3*s))) == 0)
check("(C) dV''/dbeta2 > 0 at s=1/2 (stable iff beta2 > crit)", sp.diff(Vpp0, beta2).subs({s: sp.Rational(1,2), Rv: 1}) > 0)
G_dyn = sp.simplify(b2c*(mu_s + p_s)/p_s)
check("(C) Eq(2.7)-converted dynamical threshold == (3.16c) identically in s",
      sp.simplify(G_dyn - G316c.subs(C, (1-s**2)/2)) == 0)

# (D) LP2019 convention (per Pitre fn 1): Gamma_LP := d ln p / d ln mu = beta2 * mu/p
G_LP = sp.simplify(b2c*mu_s/p_s)
print("     LP-convention threshold (d ln p/d ln mu):", sp.factor(G_LP))
G_LP_C = sp.simplify(G_LP.subs(s, sp.sqrt(1-2*C)))
print("     in C:", G_LP_C, " series:", sp.series(G_LP_C, C, 0, 3))
check("(D) LP-convention threshold differs from (3.16c) (not identically equal)",
      sp.simplify(G_LP - G316c.subs(C, (1-s**2)/2)) != 0)
check("(D) relation Gamma_LP = Gamma_1 * mu/(mu+p)", sp.simplify(G_LP - G_dyn*mu_s/(mu_s+p_s)) == 0)
check("(D) both Newtonian limits = 3/2", sp.limit(G_LP, s, 1) == sp.Rational(3,2) and sp.limit(G_dyn, s, 1) == sp.Rational(3,2))
ser = sp.series(G316c, C, 0, 3).removeO()
check("(D) (3.16c) = 3/2 + C + 7/4 C^2 + O(C^3)   (Pitre 3.17)", sp.simplify(ser - (sp.Rational(3,2) + C + sp.Rational(7,4)*C**2)) == 0)
for Cv in (sp.Rational(1,10), sp.Rational(1,5), sp.Rational(3,10), sp.Rational(2,5)):
    a = float(G316c.subs(C, Cv)); b = float(G_LP_C.subs(C, Cv))
    print(f"     C={float(Cv):.2f}: (3.16c) Gamma_1={a:.6f}   LP-convention threshold={b:.6f}   ratio={a/b:.6f}")

# (E) wall.py read-only
sys.path.insert(0, '/home/user/Claude-Method-Works/research/warp-drive')
try:
    import wall
    f = sp.lambdify(C, G316c, 'mpmath')
    import mpmath as mp; mp.mp.dps = 40
    err = max(abs(wall.gamma1_published(x) - float(f(mp.mpf(x)/2)))/float(f(mp.mpf(x)/2))
              for x in [10**(-6+k*0.05) for k in range(0, 116) if 10**(-6+k*0.05) <= 0.8])
    print(f"     wall.gamma1_published vs 40-digit (3.16c), x=2C in [1e-6,0.8]: max rel err {err:.2e}")
    check("(E) wall.gamma1_published is (3.16c) with C = x/2", err < 1e-13)
    # does wall's own Gamma use rest-mass density (Pitre) rather than LP's energy density? (statement check)
except Exception as e:
    print("     wall import failed:", e); ok = False

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
