#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for gr-qc/0209075#renorm-4.4 (AMM 2003, eqs. 4.4, 4.5a/b, 4.9-4.11, B37, B43-B44).
Checks, each asserted:
 C1  (4.4) three-term Taylor subtraction at k^2=0 of the dispersion kernel leaves exactly -(k^2)^3/(s^3(s+k^2)).
 C2  the subtracted response functions F^(T), F^(S) vanish as k^2 -> 0 (O(k^2)): no k-independent piece.
 C3  hence (4.5a),(4.5b) = k^2 * bracket: E(0)=0 exactly, dE/dk^2(0) = +1/(8piG) (T), -1/(4piG) (S).
 C4  (B44) closed form with I_0(z) (signs restored: -2/5 - 2/3 z^2 + z^4 I_0) reproduces the numerical integral.
 C5  (4.9),(4.11) log coefficients 1/(960 pi^2) and (1-6xi)^2/(96 pi^2); (4.10) coefficient 1/(1920 pi^2).
 C6  structure shared with GMMPS 2604.01047 (5.1),(5.2): rho^S ~ (s-a)^2, a = 2m^2/(6xi-1); rho^T ~ (s-4m^2)^2.
 C7  AMM's thrice-subtracted polarization and a GMMPS-type form gamma (a-gamma)^2 J(gamma), J = int w/(s(s-gamma)),
     differ by a POLYNOMIAL in gamma with ZERO constant term (degree <= 2): neither polarization form carries a
     k-independent term, so in GMMPS's F_S the only k^0 term is b_0 (alpha~^S_1); AMM's scheme differs ALSO at
     order gamma and gamma^2 (finite renormalisations of 1/G and beta), not only at k^0.
OCR note: the alphaXiv text layer drops minus signs (e.g. c_AB printed 'diag(1; 1)'); signs are restored only where a
limit fixes them (C4) and the conclusion never depends on an unrestored sign.
"""
import sympy as sp, mpmath as mp
ok = []
def check(name, cond, info=""):
    ok.append(bool(cond)); print(("PASS " if cond else "FAIL ") + name + ("  " + info if info else ""))

s, x, g, m, xi, z = sp.symbols('s x gamma m xi z', positive=True)
# C1
lhs = 1/(s+x) - (1/s - x/s**2 + x**2/s**3)
check("C1 (4.4) subtraction identity", sp.simplify(lhs - (-x**3/(s**3*(s+x)))) == 0)

# spectral functions (B37a,b); theta(s-4m^2) implicit
def rhoT(sv, mv): return (1/(60*mp.pi**2))*mp.sqrt(1-4*mv**2/sv)*(sv/4-mv**2)**2
def rhoS(sv, mv, xv): return (1/(24*mp.pi**2))*mp.sqrt(1-4*mv**2/sv)*(mv**2+(1-6*xv)*sv/2)**2
def F(rho, k2, mv=1.0, *a):
    return k2*mp.quad(lambda sv: rho(sv, mv, *a)/(sv**3*(sv+k2)), [4*mv**2, 40*mv**2, 1e3, mp.inf])
mp.mp.dps = 30
# C2 small-k^2: F/k^2 -> int rho/s^4
for name, rho, a in (("T", rhoT, ()), ("S xi=0", rhoS, (0.0,)), ("S xi=0.3", rhoS, (0.3,))):
    lim = mp.quad(lambda sv: rho(sv, 1.0, *a)/sv**4, [4, 40, 1e3, mp.inf])
    r = [F(rho, k2, 1.0, *a)/k2 for k2 in (1e-4, 1e-6)]
    check(f"C2 F^({name})(k^2)/k^2 -> finite int rho/s^4 = {mp.nstr(lim,8)}", all(abs(v/lim-1) < 1e-3 for v in r),
          f"ratios {[mp.nstr(v/lim,8) for v in r]}")
# C3 symbolic: E(k2) = k2*(c1 + k2*(c2 + Fhat(k2))) with Fhat analytic at 0 and Fhat(0)=0
k2, G, al, be = sp.symbols('k2 G alpha beta')
Fh = sp.Function('Fh')
ET = k2*(2*al*k2 + 1/(8*sp.pi*G) + k2*Fh(k2))
ES = k2*(12*be*k2 - 1/(4*sp.pi*G) + k2*Fh(k2))
for nm, E, c in (("T", ET, 1/(8*sp.pi*G)), ("S", ES, -1/(4*sp.pi*G))):
    e0 = E.subs(k2, 0); d0 = sp.diff(E, k2).subs(k2, 0)
    check(f"C3 ({nm}) E(0)=0, dE/dk2(0)={c}", sp.simplify(e0) == 0 and sp.simplify(d0 - c) == 0)
# C4 (B44) with I_0(z) = -2 + z log((z+1)/(z-1)), z = sqrt(1+4m^2/k^2)
def FT_closed(k2v, mv=1.0):
    zz = mp.sqrt(1+4*mv**2/k2v); I0 = -2 + zz*mp.log((zz+1)/(zz-1))
    return (1/(960*mp.pi**2))*(-mp.mpf(2)/5 - mp.mpf(2)/3*zz**2 + zz**4*I0)
dev = max(abs(FT_closed(k)/F(rhoT, k) - 1) for k in (0.01, 0.5, 3.0, 50.0, 1e4))
check("C4 (B44) closed form == numerical F^(T)", dev < 1e-8, f"max rel dev {mp.nstr(dev,3)}")
Iz = -2 + z*sp.log((z+1)/(z-1))
ser = sp.series((-sp.Rational(2,5) - sp.Rational(2,3)*z**2 + z**4*Iz).rewrite(sp.log), z, sp.oo, 4).removeO()
check("C4b bracket -> 2/(7 z^2) as z->oo (k^2->0)", sp.simplify(sp.limit(z**2*(-sp.Rational(2,5)-sp.Rational(2,3)*z**2+z**4*Iz), z, sp.oo) - sp.Rational(2,7)) == 0)
# C5 log slopes
def slope(rho, *a):
    k1, kk2 = mp.mpf(1e8), mp.mpf(1e10)
    return (F(rho, kk2, 1.0, *a) - F(rho, k1, 1.0, *a))/mp.log(kk2/k1)
sT = slope(rhoT); check("C5 (4.9) slope 1/(960 pi^2)", abs(sT*960*mp.pi**2 - 1) < 1e-6, mp.nstr(sT*960*mp.pi**2, 10))
for xv in (0.0, 0.3):
    sS = slope(rhoS, xv); tgt = (1-6*xv)**2/(96*mp.pi**2)
    check(f"C5 (4.11) slope (1-6xi)^2/(96 pi^2), xi={xv}", abs(sS/tgt - 1) < 1e-6, mp.nstr(sS/tgt, 10))
check("C5 (4.10) 2*alpha(mu) - 2*alpha = (1/960pi^2) ln(mu^2/m^2)  =>  coefficient 1/1920pi^2",
      sp.Rational(1,2)*sp.Rational(1,960) == sp.Rational(1,1920))
# C6 structure vs GMMPS
a = 2*m**2/(6*xi-1)
check("C6 (m^2+(1-6xi)s/2)^2 == ((1-6xi)/2)^2 (s-a)^2, a=2m^2/(6xi-1) [GMMPS 5.1 a]",
      sp.simplify((m**2+(1-6*xi)*s/2)**2 - ((1-6*xi)/2)**2*(s-a)**2) == 0)
check("C6 (s/4-m^2)^2 == (s-4m^2)^2/16 [GMMPS 5.2 a=4m^2]", sp.expand((s/4-m**2)**2 - (s-4*m**2)**2/16) == 0)
# C7 polarization forms differ by a polynomial with zero constant term
A = sp.symbols('A')
integrand = -g**3*(s-A)**2/(s**3*(s-g)) + g*(A-g)**2/(s*(s-g))
num, den = sp.fraction(sp.cancel(sp.together(integrand)))
check("C7 (s-gamma) pole cancels between the two forms", sp.degree(den, s) >= 1 and not sp.simplify(den.subs(s, g)) == 0)
P = sp.expand(sp.cancel(integrand))
poly_g = sp.Poly(sp.expand(P*s**3), g)
coeffs = {mon[0]: sp.factor(cf) for mon, cf in zip(poly_g.monoms(), poly_g.coeffs())}
print("   D(gamma) integrand * s^3, by power of gamma:", coeffs)
check("C7 no gamma^0 term, max degree 2", 0 not in coeffs and max(coeffs) <= 2)
# convergence of the gamma^1, gamma^2 coefficient integrals with w = sqrt(1-4m^2/s) (m=1)
for p, cf in coeffs.items():
    f = sp.lambdify(s, (cf/s**3).subs(A, sp.Rational(-2, 1)), 'mpmath')  # a for xi=0: 2/(0-1) = -2
    val = mp.quad(lambda sv: mp.sqrt(1-4/sv)*f(sv), [4, 40, 1e3, mp.inf])
    print(f"   coefficient of gamma^{p} (xi=0, m=1, per unit c): {mp.nstr(val, 10)}")
    check(f"C7 gamma^{p} coefficient finite", mp.isfinite(val))
print("ALL PASS" if all(ok) else f"{ok.count(False)} FAIL")
raise SystemExit(0 if all(ok) else 1)
