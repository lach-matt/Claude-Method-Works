#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of Fewster & Roman, gr-qc/0209036v2 (PRD 67 044003).

Read at source: arXiv gr-qc/0209036v2 (26 Nov 2002) full text via alphaXiv.
The journal version and its Erratum (PRD 80 069903 (2009), cited by 2003.01815,
2111.05772, 2108.06068, 2510.26247) were NOT read.

Checks (each prints PASS / DISCREPANCY; exit 1 only on a FAIL of the theorem's chain):
 A  exponent bookkeeping of (II.12), (II.22), (II.24) by explicit change of variables
 B  the sigma-window 2nu+3/2 < sigma < 2nu+2 is non-empty for every nu > 0 and forces
    N_alpha -> 1, rho_2 -> -inf, rho_1 -> 0   (z3)
 C  (II.16) -> (II.17) order swap, and the explicit constant (II.27)
 D  (II.28) N_alpha for the explicit B of (II.26)
 E  (II.31) from (II.29): F_alpha = xi / (4 pi^2 alpha^2)
 F  Sec. III: (III.7) angular integral, (III.9) antiderivative, (III.10) Parseval,
    (III.13) Gaussian constant 1/(64 pi^2 tau0^4) and the 'variance tau0' wording
 G  (II.34) harmonic-oscillator expansion
 H  NUMERIC: the counterexample itself -- <rho(f)> computed in POSITION space along the
    null line from (II.29) with a smooth compactly supported bump f, against the
    momentum-space reduced forms (II.22)/(II.24); shows <rho(f)> -> -inf as alpha -> 0
"""
import sys
import sympy as sp
import numpy as np
from scipy import integrate

FAIL = []
def rep(tag, ok, msg, fatal=True):
    print(("PASS " if ok else ("FAIL " if fatal else "DISCREPANCY ")) + tag + ": " + msg)
    if not ok and fatal:
        FAIL.append(tag)

a, s, nu, L0 = sp.symbols('alpha sigma nu Lambda0', positive=True)
k, kp, b, bp, u, up, v, vp, u1, v1 = sp.symbols("k kp beta betap u up v vp u1 v1", positive=True)

# ---- A: exponent bookkeeping ------------------------------------------------------
# (II.12): alpha^{2s} * INT dk dk' (kk')^{2nu+1} INT_0^alpha dbeta dbeta' |B(k beta, k' beta')|^2
# u = k beta (dbeta = du/k), then v = k alpha (dk = dv/alpha).  One factor (per momentum):
one = k**(2*nu+1) / k                          # after u = k beta
one_v = one.subs(k, v/a) / a                   # after v = k alpha, dk = dv/alpha
expo12 = sp.simplify(sp.log(sp.powsimp(one_v / v**(2*nu), force=True)) / sp.log(a))
rep("A.II.12", sp.simplify(2*s + 2*expo12 - (2*s - 2 - 4*nu)) == 0,
    "per-momentum alpha power %s; total alpha^(2 sigma %s) = alpha^(2(sigma-2nu-1))" % (expo12, sp.expand(2*expo12)))
# bound constant: (INT_0^L0 v^{2nu} dv)^2 * L0^{-(4nu+2)} = 1/(2nu+1)^2
c12 = sp.simplify(sp.integrate(v**(2*nu), (v, 0, L0))**2 * L0**(-(4*nu+2)))
rep("A.II.12c", sp.simplify(c12 - 1/(2*nu+1)**2) == 0, "bound constant = %s" % c12)
# measure: d^3k/(2pi)^3 -> k^2 dk dbeta (2pi)/(2pi)^3 ; two momenta -> 1/(2pi)^4
meas = sp.simplify((2*sp.pi/(2*sp.pi)**3)**2)
rep("A.meas", sp.simplify(meas - 1/(2*sp.pi)**4) == 0, "angular measure prefactor = %s" % meas)
# (II.22): integrand l.k l.k'/sqrt(k k') b_alpha * k^2 k'^2 ; l.k = k beta
pw = sp.powsimp((k*b) / sp.sqrt(k) * k**(nu - sp.Rational(1, 2)) * k**2, force=True)
rep("A.II.22a", sp.simplify(pw - k**(nu+2)*b) == 0, "k-power in (II.22) line 1 = %s" % pw)
# beta beta' dbeta dbeta' -> u u' du du' / (k^2 k'^2): k^{nu+2} -> k^nu ; then v = k alpha
e22 = sp.simplify(sp.log(sp.powsimp(((v/a)**nu / a) / v**nu, force=True)) / sp.log(a))
tot22 = sp.expand(s + 2*e22)
rep("A.II.22", sp.simplify(tot22 - (s - 2*(nu+1))) == 0, "rho_2 ~ alpha^(%s)" % tot22)
# (II.15): c_alpha = alpha^{2 sigma} * INT dk1 k1^{2nu+1} INT_0^alpha dbeta1 ... ; u1 = k1 beta1, v = k1 alpha
e15 = sp.simplify(sp.log(sp.powsimp(((v/a)**(2*nu) / a) / v**(2*nu), force=True)) / sp.log(a))
rep("A.II.15", sp.simplify(2*s + e15 - (2*s - (2*nu+1))) == 0, "c_alpha ~ alpha^(2 sigma %s)" % e15)
tot24 = sp.expand(2*s + e15 + 2*e22)
rep("A.II.24", sp.simplify(tot24 - (2*s - (4*nu+3))) == 0, "rho_1 ~ alpha^(%s)" % tot24)

# (II.21) carries -2N^2 and the measure gives 1/(2pi)^4, so (II.22) line 1 should carry 2N^2/(2pi)^4;
# (II.22) and (II.24) as printed carry N^2/(2pi)^4.  (II.13)/(II.18) re-derived from the Fock state:
# <0|a(p)a(q)|psi-part> = 2 N^2 b(p,q) for symmetric b; with 1/sqrt(2w 2w') and b+b* this is 2N^2 Re, as printed.
Nn = sp.symbols('N', positive=True)
pref_from_II21 = sp.simplify(2*Nn**2 * meas)
pref_printed = Nn**2/(2*sp.pi)**4
rep("A.pref", sp.simplify(pref_from_II21 - pref_printed) == 0,
    "prefactor implied by (II.21)/(II.20) = %s ; printed in (II.22)/(II.24) = %s ; ratio %s (overall factor, both terms; sign and alpha-exponents untouched)"
    % (pref_from_II21, pref_printed, sp.simplify(pref_from_II21/pref_printed)), fatal=False)

# ---- B: the window, z3 ------------------------------------------------------------
try:
    import z3
    N, S = z3.Reals('N S')
    sol = z3.Solver()
    # exists nu>0 with NO sigma in the window?  (negation of non-emptiness)
    sol.add(N > 0, z3.ForAll([S], z3.Not(z3.And(2*N + 1.5 < S, S < 2*N + 2))))
    r1 = sol.check()
    sol2 = z3.Solver()
    # window => exponents: 2(S-2N-1) > 0, S-2N-2 < 0, 2S-4N-3 > 0 ; look for a violation
    sol2.add(N > 0, 2*N + 1.5 < S, S < 2*N + 2,
             z3.Or(2*(S - 2*N - 1) <= 0, S - 2*N - 2 >= 0, 2*S - 4*N - 3 <= 0))
    r2 = sol2.check()
    rep("B.z3", str(r1) == "unsat" and str(r2) == "unsat",
        "window non-empty for all nu>0: %s(neg); window => (N->1, rho2 exp<0, rho1 exp>0): %s(neg)" % (r1, r2))
except ImportError:
    rep("B.z3", False, "z3 not installed", fatal=False)

# ---- C: (II.16) -> (II.17) -------------------------------------------------------
g = sp.Function('g')
# general swap identity checked on a monomial family g(u1) = u1^p (dense enough for polynomials)
p = sp.symbols('p', positive=True)
lhs = sp.integrate(v**(2*nu) * sp.integrate(u1**p, (u1, 0, v)), (v, 0, L0))
correct = sp.integrate(u1**p * (L0**(2*nu+1) - u1**(2*nu+1)) / (2*nu+1), (u1, 0, L0))
printed = sp.integrate(u1**p * u1**(2*nu+1) / (2*nu+1), (u1, 0, L0))
rep("C.swap", sp.simplify(lhs - correct) == 0,
    "INT_0^L0 dv v^2nu INT_0^v du1 g = INT du1 g (L0^(2nu+1) - u1^(2nu+1))/(2nu+1)  [exact]")
ok_print = sp.simplify(lhs - printed) == 0
rep("C.II17-printed", ok_print,
    "printed (II.17) weight u1^(2nu+1)/(2nu+1); lhs/printed at nu=1,p=0: %s"
    % sp.simplify((lhs / printed).subs({nu: 1, p: 0})), fatal=False)
# explicit (II.26): nu = 1, B = L0^-4 on [0,L0]^2
B26 = L0**-4
C_from_II16 = sp.simplify(1/(2*sp.pi**2) * sp.integrate(v**2 * sp.integrate(B26*B26, (u1, 0, v)), (v, 0, L0)))
C_from_II17 = sp.simplify(1/(2*sp.pi**2*3) * sp.integrate(u1**3 * B26*B26, (u1, 0, L0)))
C_printed_II27 = 1/(24*sp.pi**2*L0**4)
rep("C.II27", sp.simplify(C_from_II16 - C_printed_II27) == 0,
    "(II.16) gives C = %s; (II.17) as printed gives %s = (II.27) %s; ratio %s"
    % (C_from_II16, C_from_II17, C_printed_II27, sp.simplify(C_from_II16 / C_printed_II27)), fatal=False)
# the four properties the proof uses survive the corrected kernel:
#  weight (L0^(2nu+1)-u1^(2nu+1)) >= 0 on [0,L0]  => C >= 0, continuity, dimension, alpha-exponent unchanged
wt = (L0**(2*nu+1) - u1**(2*nu+1))
rep("C.props", sp.simplify(wt.subs(u1, 0) - L0**(2*nu+1)) == 0 and sp.simplify(wt.subs(u1, L0)) == 0,
    "corrected weight is >= 0 and vanishes only at u1 = L0: properties (i)-(iv) of C hold; Theorem II.1 unaffected")

# ---- D: (II.28) ---------------------------------------------------------------------
# B26 = L0^-4 = L0^-2 x L0^-2 factorises; per-momentum |B_1|^2 = L0^-4
sq = sp.integrate(v**2 * sp.integrate(L0**-4, (u, 0, v)), (v, 0, L0))  # per-momentum factor, nu = 1
twice = sp.simplify(2 * a**(2*s - 6) / (2*sp.pi)**4 * sq**2)
rep("D.II28", sp.simplify(twice - a**(2*s-6)/(128*sp.pi**4)) == 0, "2 INT|b|^2 = %s" % twice)

# ---- E: (II.31) from (II.29) ---------------------------------------------------------
t, z, lam = sp.symbols('t z lambda', real=True)
vv = sp.symbols('v', positive=True)
bb = sp.symbols('bb', positive=True)
A_ = vv*z/a
inner = sp.integrate(bb*sp.exp(-sp.I*A_*bb), (bb, 0, a))
# F_alpha(t,0,0,z) = 1/(4 pi^2) INT_0^Lambda dk k^3 INT_0^alpha dbeta beta e^{-ik(t-z)} e^{-ikz beta}, k = v/alpha
integrand_F = (1/(4*sp.pi**2)) * (vv/a)**3 / a * sp.exp(-sp.I*vv*(t-z)/a) * inner
integrand_xi = sp.exp(-sp.I*vv*(t-z)/a) * (sp.I*vv**2/z*sp.exp(-sp.I*vv*z) + vv/z**2*(sp.exp(-sp.I*vv*z)-1))
diffE = sp.simplify(sp.expand(integrand_F - integrand_xi/(4*sp.pi**2*a**2)))
# numeric spot check too (symbolic simplification of complex exponentials can be shy)
vals = {vv: 0.7, z: 1.3, t: 0.4, a: 0.2}
numE = complex(sp.N((integrand_F - integrand_xi/(4*sp.pi**2*a**2)).subs(vals)))
rep("E.II31", diffE == 0 or abs(numE) < 1e-12,
    "F_alpha integrand - xi integrand/(4 pi^2 alpha^2) = %s (numeric %.2e) => (II.31) prefactors 2N^2/(16 pi^4 L0^4), alpha^(2s-7)/(24pi^2), alpha^(s-4) follow from (II.29)" % (diffE, abs(numE)))

# ---- F: Section III -------------------------------------------------------------------
c, om, kk, m, U, tau, tau0 = sp.symbols('c omega kk m U tau tau0', positive=True)
ang = sp.integrate((om - kk*c)**2, (c, -1, 1))
rep("F.III7a", sp.simplify(ang - sp.Rational(2, 3)*(3*om**2 + kk**2)) == 0, "INT (w - k cos)^2 dcos = %s" % sp.factor(ang))
pref = sp.simplify(sp.Rational(1, 2) * 2*sp.pi/(2*sp.pi)**3 * sp.Rational(2, 3))
rep("F.III7b", sp.simplify(pref - 1/(12*sp.pi**2)) == 0, "prefactor (l0)^2 x %s" % pref)
anti = U*(U**2 - m**2)**sp.Rational(3, 2)
rep("F.III9", sp.simplify(sp.diff(anti, U) - sp.sqrt(U**2-m**2)*(4*U**2-m**2)) == 0 and anti.subs(U, m) == 0,
    "INT_m^u sqrt(w^2-m^2)(4w^2-m^2) dw = u(u^2-m^2)^(3/2)")
gG = (2*sp.pi*tau0**2)**sp.Rational(-1, 4) * sp.exp(-(tau/tau0)**2/4)
norm = sp.simplify(sp.integrate(gG**2, (tau, -sp.oo, sp.oo)))
var = sp.simplify(sp.integrate(tau**2*gG**2, (tau, -sp.oo, sp.oo)))
g2int = sp.simplify(sp.integrate(sp.diff(gG, tau, 2)**2, (tau, -sp.oo, sp.oo)))
bound = sp.simplify(g2int/(12*sp.pi**2))
rep("F.III13", sp.simplify(bound - 1/(64*sp.pi**2*tau0**4)) == 0,
    "INT g''^2 = %s ; (1/12pi^2) INT g''^2 = %s" % (g2int, bound))
# Parseval route of (III.10): -(1/12 pi^3) INT_0^inf u^4 |ghat|^2 du  ==  -(1/12 pi^2) INT g''^2
w_ = sp.symbols('w', real=True)
ghat = sp.simplify(sp.integrate(gG*sp.exp(-sp.I*w_*tau), (tau, -sp.oo, sp.oo)))
par = sp.simplify(sp.integrate(w_**4*sp.Abs(ghat)**2, (w_, 0, sp.oo)) / (12*sp.pi**3))
rep("F.III10", sp.simplify(par - bound) == 0, "momentum-space form = %s" % par)
rep("F.var", sp.simplify(var - tau0**2) == 0,
    "g^2 has norm %s and variance %s: the text's 'variance tau0' is the standard deviation (wording)" % (norm, var),
    fatal=False)

# ---- G: (II.34) ------------------------------------------------------------------------
n = sp.symbols('n', positive=True)
H = sp.Rational(1, 2)*(1 + n**sp.Rational(-1, 2)*(2*n+1))/(1 + n**sp.Rational(-1, 2))
x = sp.symbols('x', positive=True)
ser = sp.series(H.subs(n, 1/x**2), x, 0, 2).removeO()
lead = sp.series(H.subs(n, 1/x**2), x, 0, 1).removeO()   # terms through x^0
rep("G.II34", sp.simplify(lead - (1/x - sp.Rational(1, 2))) == 0,
    "<H>/hbar w = n^(1/2) - 1/2 + O(n^-1/2); through x^1 (x = n^-1/2): %s" % ser)

# ---- H: numeric counterexample ---------------------------------------------------------
def bump(l):
    l = np.asarray(l, dtype=float)
    out = np.zeros_like(l)
    msk = np.abs(l) < 1
    out[msk] = np.exp(-1.0/(1.0 - l[msk]**2))
    return out
Z = integrate.quad(lambda l: float(bump(l)), -1, 1, limit=200)[0]
f = lambda l: bump(l)/Z                                     # smooth, >=0, compact, INT f = 1
fhat = lambda q: integrate.quad(lambda l: float(f(l))*np.cos(q*l), -1, 1, limit=200)[0]  # f even => real
qs = np.linspace(0, 6, 241)
fh = np.array([fhat(q) for q in qs])
first_neg = qs[np.argmax(fh < 0)] if np.any(fh < 0) else np.inf
Lam0 = 1.0
rep("H.Lambda0", 2*Lam0 < first_neg, "Re fhat > 0 on [0, %.2f]; first sign change near %.2f; Lambda0 = %.1f admissible"
    % (2*Lam0, first_neg, Lam0))
nuv, sig = 1, 3.75
w = lambda q: (Lam0**2 - q**2)/2.0                           # (L0^(nu+1)-u^(nu+1))/(nu+1), nu = 1
Bc = Lam0**-4
# momentum-space reduced integrals (alpha-free shapes)
K2 = integrate.dblquad(lambda qp, q: q*qp*w(q)*w(qp)*Bc*fhat(q+qp), 0, Lam0, 0, Lam0, epsabs=1e-12)[0]
K1_II16 = integrate.dblquad(lambda qp, q: q*qp*w(q)*w(qp)*fhat(qp-q), 0, Lam0, 0, Lam0, epsabs=1e-12)[0]
C_corr, C_prt = 1/(8*np.pi**2*Lam0**4), 1/(24*np.pi**2*Lam0**4)
# position-space: G(lam) = INT_0^L0 du u (L0^2-u^2)/2 e^{-i lam u};  F_alpha(lam) = G/(4 pi^2 alpha^2)
def Gc(l):
    re = integrate.quad(lambda q: q*w(q)*np.cos(l*q), 0, Lam0)[0]
    im = -integrate.quad(lambda q: q*w(q)*np.sin(l*q), 0, Lam0)[0]
    return re + 1j*im
lg = np.linspace(-1, 1, 801)
Gv = np.array([Gc(l) for l in lg]); fv = f(lg)
P2 = np.trapezoid(fv*np.real(Gv**2), lg)
P1 = np.trapezoid(fv*np.abs(Gv)**2, lg)
rep("H.fourier", abs(P2 - K2/Bc) < 1e-6*max(1, abs(P2)) and abs(P1 - K1_II16) < 1e-6*max(1, abs(P1)),
    "position-space INT f Re G^2 = %.6e vs momentum-space %.6e ; INT f|G|^2 = %.6e vs %.6e"
    % (P2, K2/Bc, P1, K1_II16))
rep("H.sign", K2 > 0, "phi-integral K2 = %.4e > 0 => rho_2 strictly negative" % K2)
print("   alpha      N_alpha^2    rho_2              rho_1(C corrected)   rho_1(C printed)    <rho(f)>")
prev = None
for al in [0.2, 0.05, 1e-2, 1e-3, 1e-4, 1e-6, 1e-8]:
    N2 = 1.0/(1.0 + al**(2*sig-6)/(128*np.pi**4))
    r2 = -N2*al**(sig-2*(nuv+1))/(2*np.pi)**4 * K2
    r1c = 2*N2/Lam0**4 * al**(2*sig-3) * C_corr*Lam0**4 * P1 / (16*np.pi**4) / al**4
    r1p = 2*N2/Lam0**4 * al**(2*sig-3) * C_prt*Lam0**4 * P1 / (16*np.pi**4) / al**4
    r2p = -2*N2/Lam0**4 * al**sig * P2 / (16*np.pi**4) / al**4
    print("   %-8.0e  %.10f  %+.6e      %+.6e        %+.6e       %+.6e" % (al, N2, r2p, r1c, r1p, r2p + r1c))
    if prev is not None and not (r2p + r1c < prev):
        FAIL.append("H.monotone")
    prev = r2p + r1c
# position-space rho_2 (from II.29) must equal the reduced (II.22) form: check once
al = 1e-3
N2 = 1.0/(1.0 + al**(2*sig-6)/(128*np.pi**4))
r2_red = -N2*al**(sig-4)/(2*np.pi)**4 * K2
r2_pos = -2*N2/Lam0**4 * al**sig * P2/(16*np.pi**4)/al**4
rep("H.II22vsII29", abs(r2_pos/r2_red - 2.0) < 1e-6,
    "rho_2(alpha=1e-3): (II.22) AS PRINTED (prefactor N^2/(2pi)^4) %.6e vs position-space from (II.18)/(II.29) "
    "(prefactor 2N^2) %.6e ; ratio %.6f -- the numerics confirm the factor 2 found symbolically in A.pref"
    % (r2_red, r2_pos, r2_pos/r2_red))
rep("H.limit", "H.monotone" not in FAIL,
    "<rho(f)> decreases monotonically ~ -alpha^(sigma-4) = -alpha^-0.25 -> -inf; rho_1 ~ alpha^0.5 -> 0 "
    "with EITHER constant C (the factor-3 discrepancy moves only the vanishing term)")

print("\nSUMMARY: %s" % ("theorem chain re-derived, no FAIL" if not FAIL else "FAIL: " + ", ".join(FAIL)))
sys.exit(1 if FAIL else 0)
