#!/usr/bin/env python3
"""DOCKET 67 -- audit of GMMPS (arXiv:2604.01047 v1) Prop. 3.1 and Thm 3.6.

Everything below uses ONLY formulas printed in the paper (READ via alphaXiv,
pp. 7, 22-23, 32-33, 35, 37, 40):
  (P1) omega_02 = m/(4 pi^2 sqrt(2 sigma)) K_1(m sqrt(2 sigma))            p.23
  (P2) H = 1/(8 pi^2 sigma) + v log(mu^2 sigma)                             p.23
  (P3) [w] = m^2/(16pi^2)(-1+2g+L), [d_a d_b w] = m^4/(64pi^2)(-5/2+2g+L) eta  (3.2)
       L = log(m^2/(2 mu^2))
  (P4) omega_0(:T:) = -[dd w] - 1/2 eta (m^2 [w] - [box w]) + alpha_1 m^4 eta
                      + (1/4 pi^2)[v_1] eta                                 (3.3)
  (P5) alpha_1 = (1/64pi^2)(-3/2 + 2g + L)                                   Prop 3.1
  (P6) late-time <T> = -(1/64pi^2)[log((m^2+dm^2)/2mu^2) - log(m^2/2mu^2)]
                       (m^2+dm^2)^2 eta                                     (3.21)
  (P7) comparison: -4/(64pi^2) m^2 dm^2 = -8 alpha~S_1 m^4 W, dm^2 = 2 m^2 W   p.37
  (P8) Thm 3.6: alpha~S_1 = 1/(64 pi^2), alpha~TT_1 = 0                      p.33

Checks
  C1  series of (P1) reproduces (P3) (sympy series + mpmath numeric).
  C2  (P4) with (P3) gives (P5) IFF the v_1 term equals m^4/(32 pi^2), i.e.
      [v_1] read in the 1/(8 pi^2)-stripped (Decanini-Folacci) normalisation
      v_1 = m^4/8; with the printed "[w_1] = m^4/(64 pi^2)" substituted
      literally into (1/4pi^2)[v_1] it does NOT.  Notational discrepancy.
  C3  (P6) + (P7) algebra gives alpha~S_1 = 1/(64 pi^2)  (the paper's own step).
  C4  GENERAL LOCAL COVARIANCE, the principle Thm 3.6 invokes: for constant
      Omega the late-time spacetime (R^4, Omega^2 eta) is isometric to (R^4, eta)
      by the dilation x -> Omega x, and the mass m is unchanged.  The locally
      covariant parametrix of g, rewritten for phi_eta = Omega phi_g, is
      Omega^2 H_g(m, mu) = H_eta(Omega m, Omega mu)  -- checked here symbolically
      to O(sigma) and numerically to all orders via the exact flat-space V.
      Hence <T_g> = Omega^-2 T_eta(M = Omega m, mu' = Omega mu) = 0 EXACTLY, at
      every order in W; (P6) equals T_eta(M, mu' = mu), the value with the
      Hadamard scale held fixed relative to the BACKGROUND eta.
  C5  consequences: with the covariant late-time value 0 in (P7), alpha~S_1 = 0;
      the printed 1/(64 pi^2) equals d/d(log mu^2) of the vacuum T coefficient
      (the one-loop running coefficient of the cosmological term).
  C6  TT half: tr r = 0, so det(eta + W r) = -(1 - W^2): no first-order volume
      change; covariant and background-mu evaluations both give alpha~TT_1 = 0.
Exit 0 iff every check behaves as stated.
"""
import sys
import sympy as sp
import mpmath as mp

ok = True
def chk(name, cond):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

m, mu, s, W, g = sp.symbols('m mu sigma W gamma_E', positive=True)
EG = sp.EulerGamma
L = sp.log(m**2 / (2 * mu**2))

# ---------------------------------------------------------------- C1
# K_1(z) small-z series (DLMF 10.31.1), two orders beyond the pole
z = sp.symbols('z', positive=True)
I1 = z/2 + z**3/16
K1ser = 1/z + sp.log(z/2)*I1 - (z/4)*((1 - 2*EG) + (sp.Rational(5, 2) - 2*EG)*z**2/8)
omega = (m / (4*sp.pi**2*sp.sqrt(2*s)) * K1ser).subs(z, m*sp.sqrt(2*s))
omega = sp.expand(sp.expand_log(omega, force=True))
v0, v1 = m**2/(16*sp.pi**2), m**4/(64*sp.pi**2)
H = 1/(8*sp.pi**2*s) + (v0 + v1*s)*sp.log(mu**2*s)
w = sp.expand(sp.expand_log(omega - H, force=True))
w = sp.simplify(w)
w0 = sp.simplify(w.subs(s, 0)) if w.subs(s, 0).is_finite else None
w_s0 = sp.limit(w, s, 0)
w_s1 = sp.limit(sp.diff(w, s), s, 0)
P3_w0 = m**2/(16*sp.pi**2)*(-1 + 2*EG + L)
P3_w1 = m**4/(64*sp.pi**2)*(sp.Rational(-5, 2) + 2*EG + L)
chk("C1a [w] from the K_1 series = (3.2)'s m^2/(16pi^2)(-1+2g+L)",
    sp.simplify(sp.expand_log(w_s0 - P3_w0, force=True)) == 0)
chk("C1b coefficient of sigma in w = (3.2)'s m^4/(64pi^2)(-5/2+2g+L)",
    sp.simplify(sp.expand_log(w_s1 - P3_w1, force=True)) == 0)
# numeric cross-check against the exact Bessel function
mp.mp.dps = 40
mm, muu = mp.mpf('1.3'), mp.mpf('0.7')
def w_exact(sig):
    x = mm*mp.sqrt(2*sig)
    om = mm/(4*mp.pi**2*mp.sqrt(2*sig))*mp.besselk(1, x)
    Hh = 1/(8*mp.pi**2*sig) + (mm**2/(16*mp.pi**2) + mm**4*sig/(64*mp.pi**2))*mp.log(muu**2*sig)
    return om - Hh
Ln = mp.log(mm**2/(2*muu**2))
a0 = mm**2/(16*mp.pi**2)*(-1 + 2*mp.euler + Ln)
a1 = mm**4/(64*mp.pi**2)*(mp.mpf(-5)/2 + 2*mp.euler + Ln)
sg = mp.mpf('1e-8')
# O(sigma^2 log sigma) remainder is ~1e-15 here
chk("C1c numeric: w(sigma) - [w] - [w_1']sigma = O(sigma^2 log sigma) at sigma=1e-8",
    abs(w_exact(sg) - a0 - a1*sg) < mp.mpf('1e-13'))

# ---------------------------------------------------------------- C2
# [box w] = eta^{ab} [d_a d_b w] = 4 w1 ; T = eta * (w1 - m^2 w0/2 + alpha1 m^4 + V1term)
def alpha1_from(V1term):
    a = sp.symbols('a')
    # careful: -[dd w] - 1/2 eta(m^2[w] - [box w])  ->  -w1 - 1/2 (m^2 w0 - 4 w1) = w1 - m^2 w0/2
    expr = (P3_w1 - m**2*P3_w0/2) + a*m**4 + V1term
    return sp.solve(sp.Eq(expr, 0), a)[0]
P5 = (1/(64*sp.pi**2))*(sp.Rational(-3, 2) + 2*EG + L)
a_std = alpha1_from(m**4/(32*sp.pi**2))                 # (1/4pi^2) * (m^4/8)
a_lit = alpha1_from(m**4/(64*sp.pi**2)/(4*sp.pi**2))    # (1/4pi^2) * printed [w_1]
chk("C2a (3.3) gives Prop 3.1's alpha_1 with v_1 = m^4/8 (1/(8pi^2)-stripped normalisation)",
    sp.simplify(sp.expand_log(a_std - P5, force=True)) == 0)
chk("C2b with printed [w_1] = m^4/(64pi^2) inserted literally, (3.3) does NOT give Prop 3.1 "
    "(normalisation discrepancy, recorded, not a refutation)",
    sp.simplify(sp.expand_log(a_lit - P5, force=True)) != 0)
print("     literal-substitution alpha_1 - printed alpha_1 =",
      sp.simplify(sp.expand_log(a_lit - P5, force=True)))

# ---------------------------------------------------------------- C3
dm2 = 2*m**2*W
T321 = -(1/(64*sp.pi**2))*(sp.log((m**2+dm2)/(2*mu**2)) - sp.log(m**2/(2*mu**2)))*(m**2+dm2)**2
trace321_lin = sp.series(4*T321, W, 0, 2).removeO()
chk("C3a first order of tr(3.21) = -4 m^2 dm^2/(64 pi^2) (p.37)",
    sp.simplify(trace321_lin - (-4*m**2*dm2/(64*sp.pi**2))) == 0)
at = sp.symbols('at')
sol = sp.solve(sp.Eq(trace321_lin, -8*at*m**4*W), at)[0]
chk("C3b paper's comparison gives alpha~S_1 = 1/(64 pi^2)  (Thm 3.6, S half reproduced)",
    sp.simplify(sol - 1/(64*sp.pi**2)) == 0)

# ---------------------------------------------------------------- C4
Om, Mm, mup = sp.symbols('Omega M muprime', positive=True)
se = sp.symbols('sigma_eta', positive=True)
def Hpar(mass, scale, sig):      # flat-space parametrix to O(sigma), paper's normalisation (P2)
    return 1/(8*sp.pi**2*sig) + (mass**2/(16*sp.pi**2) + mass**4*sig/(64*sp.pi**2))*sp.log(scale**2*sig)
lhs = Om**2*Hpar(m, mu, Om**2*se)           # parametrix of g = Omega^2 eta, for phi_eta = Omega phi_g
rhs = Hpar(Om*m, Om*mu, se)
chk("C4a Omega^2 H_g(m, mu; sigma_g = Omega^2 sigma_eta) == H_eta(Omega m, Omega mu; sigma_eta)",
    sp.simplify(sp.expand_log(lhs - rhs, force=True)) == 0)
chk("C4b ... and != H_eta(Omega m, mu) (the scale does not stay fixed w.r.t. eta)",
    sp.simplify(sp.expand_log(lhs - Hpar(Om*m, mu, se), force=True)) != 0)
# all orders: exact flat-space Hadamard V is m^2 f(m^2 sigma); check numerically at a few points
def V_exact(mass, sig):
    # V such that omega = 1/(8pi^2 sig) + V log(sig) + smooth: V = (m/(8 pi^2 sqrt(2sig))) I_1(m sqrt(2 sig))
    x = mass*mp.sqrt(2*sig)
    return mass/(8*mp.pi**2*mp.sqrt(2*sig))*mp.besseli(1, x)
chk("C4c exact V: V(m; sigma) at sigma=1e-10 matches m^2/16pi^2 + m^4 sigma/64pi^2",
    abs(V_exact(mm, mp.mpf('1e-10')) - (mm**2/(16*mp.pi**2) + mm**4*mp.mpf('1e-10')/(64*mp.pi**2))) < mp.mpf('1e-21'))
Omn = mp.mpf('1.37')
allord = all(abs(Omn**2*V_exact(mm, Omn**2*sv) - V_exact(Omn*mm, sv)) < mp.mpf('1e-30')
             for sv in (mp.mpf('0.01'), mp.mpf('0.5'), mp.mpf('3')))
chk("C4d all orders: Omega^2 V(m; Omega^2 sigma) == V(Omega m; sigma) (exact Bessel V)", allord)

def Tvac(mass, scale):           # (3.3) generalised: vacuum T coefficient of eta for mass, scale, alpha_1 fixed by (P5)
    return (-(1/(64*sp.pi**2))*(sp.Rational(-3, 2) + 2*EG + sp.log(mass**2/(2*scale**2))) + P5)*mass**4
T_cov = sp.simplify(sp.expand_log(Tvac(Om*m, Om*mu), force=True))
T_bg = sp.simplify(sp.expand_log(Tvac(Om*m, mu), force=True))
T321_exact = -(1/(64*sp.pi**2))*(sp.log(Om**2*m**2/(2*mu**2)) - sp.log(m**2/(2*mu**2)))*(Om**2*m**2)**2
chk("C4e covariant late-time value (mu' = Omega mu) is EXACTLY 0 at every order in W",
    T_cov == 0)
chk("C4f (3.21) == the value with mu held fixed w.r.t. the background eta, exactly",
    sp.simplify(sp.expand_log(T_bg - T321_exact, force=True)) == 0)
chk("C4g ... which is nonzero for Omega != 1", sp.simplify(T_bg.subs(Om, 2)) != 0)

# ---------------------------------------------------------------- C5
sol_cov = sp.solve(sp.Eq(0, -8*at*m**4*W), at)[0]
chk("C5a covariant late-time value 0 in the paper's own comparison (p.37) gives alpha~S_1 = 0",
    sol_cov == 0)
lm = sp.symbols('lm')   # log mu^2
run = sp.diff(Tvac(m, sp.exp(lm/2)), lm)
chk("C5b 1/(64pi^2) m^4 = d T_vac / d log(mu^2): the printed value is the mu-running coefficient",
    sp.simplify(run - m**4/(64*sp.pi**2)) == 0)

# ---------------------------------------------------------------- C6
eta = sp.diag(-1, 1, 1, 1)
r = sp.diag(0, 1, -1, 0)
chk("C6a tr r = 0 (TT perturbation (3.23))", (eta.inv()*r).trace() == 0)
chk("C6b det(eta + W r) = -(1 - W^2): no first-order volume change",
    sp.expand((eta + W*r).det() + (1 - W**2)) == 0)
# background-mu evaluation of a volume-preserving linear map: the only log term is log det -> O(W^2)
chk("C6c first-order log|det| term vanishes, so alpha~TT_1 = 0 both ways",
    sp.series(sp.log(-(eta + W*r).det()), W, 0, 2).removeO() == 0)

print("\nRESULT:", "ALL CHECKS BEHAVE AS STATED" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
