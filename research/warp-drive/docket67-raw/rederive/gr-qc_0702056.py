#!/usr/bin/env python3
"""DOCKET 67 re-derivation for gr-qc/0702056 (Fewster & Smith, absolute QEI).

What is finite/closed-form here is ONLY the flat massless worldline coefficient the
tree quotes as FS eq. (88):   B = -(1/16 pi^3) INT_0^oo |ghat(u)|^2 u^4 du,
ghat(u) = INT g(t) e^{iut} dt, g real, smearing weight g^2 (tree writes f^2).
The general curved-spacetime bound B_A (Hadamard-parametrix series, local geometry)
is NOT closed-form and is not evaluated here.

Checks (each can fail):
 K1 Parseval: (1/16 pi^3) INT_0^oo |ghat|^2 u^4 du == (1/16 pi^2) INT (g'')^2 dt   [symbolic, Gaussian g]
 K2 the same identity for compactly supported g=(1-t^2)^4: Fourier side by quadrature, time side exact
 K3 Lorentzian sampling g^2 = t0/(pi (t^2+t0^2)): the eq.(88)-form bound is EXACTLY 9/64 of the
    Ford-Roman massless figure -3/(32 pi^2 t0^4), i.e. -27/(2048 pi^2 t0^4) -- the tree's own
    independent fixture fewsterteo.NINE_64 = (9,64) (via F&T (6.9)); FS is tighter than Ford-Roman,
    so FS eq.(88) does not contradict the older (weaker) bound.  [symbolic]
 K4 control that fires: a coefficient 1/(8 pi^3) does NOT give 9/64.
 K5 FS's own derivation chain (84)->(88), p.23-24 of gr-qc/0702056v3:
    K5a pull-back of T^split H_{-1} (eq. 81, massless, inertial, H_{-1}=1/(4pi^2 sigma_+),
        sigma = r^2 - (dt - i eps)^2) is (3/(2 pi^2)) (t-t'-i eps)^{-4}   [sympy]
    K5b FT (FS convention, e^{+i xi t}) of (t - i0)^{-4} = pi xi^3 theta(xi)/3  [residue, sympy]
    K5c (86) with its dxi/pi, variables eta = xi + zeta, gives (1/16 pi^3) INT |fhat|^2 eta^4 = (88)
        [symbolic, Gaussian f]; K5d (87) AS TRANSCRIBED by the text layer (no 1/pi on d eta)
        would give 1/(16 pi^2): a factor pi from (88) -- recorded as a transcription/misprint
        DISCREPANCY between (87) and (86)/(88), not a refutation; (86)->(88) is what holds.
 K6 the tree's claim "same form and constant as F&T (5.6) at C = 0": F&T gr-qc/9812032 (5.6)
    left side -(1/4 pi^3) INT_0^oo dw INT_C^oo dw' w'^2 sqrt(w'^2 - C^2) |fhat^{1/2}(w+w')|^2
    at C = 0 equals FS (86)/(88) identically (F&T weight f = FS weight f^2)  [symbolic, Gaussian]
"""
import sys
import sympy as sp

t, u = sp.symbols('t u', real=True)
t0, s = sp.symbols('t0 s', positive=True)
ok = True
def chk(name, cond):
    global ok
    ok &= bool(cond)
    print(("  [OK] " if cond else "  [FAIL] ") + name)

# K1: Gaussian g
g = sp.exp(-t**2/(2*s**2))
ghat = sp.simplify(sp.integrate(g*sp.exp(sp.I*u*t), (t, -sp.oo, sp.oo)))
lhs = sp.simplify(sp.integrate(sp.Abs(ghat)**2*u**4, (u, 0, sp.oo))/(16*sp.pi**3))
rhs = sp.simplify(sp.integrate(sp.diff(g, t, 2)**2, (t, -sp.oo, sp.oo))/(16*sp.pi**2))
print("K1 Gaussian: (1/16pi^3) INT|ghat|^2u^4 =", lhs, "; (1/16pi^2) INT g''^2 =", rhs)
chk("K1 Parseval identity (symbolic, Gaussian)", sp.simplify(lhs-rhs) == 0)

# K2: compactly supported g = (1-t^2)^4 on [-1,1] (C^3, so g'' in L^2), closed-form ghat,
# Fourier side by numeric quadrature, time side exact.
import mpmath as mp
mp.mp.dps = 30
gc = (1-t**2)**4
ghc = sp.simplify(2*sp.integrate(gc*sp.cos(u*t), (t, 0, 1)))
ghf = sp.lambdify(u, ghc, 'mpmath')
R = sp.integrate(sp.diff(gc, t, 2)**2, (t, -1, 1))/(16*sp.pi**2)
pts = [0] + [mp.pi*k for k in range(1, 4001)]
L = mp.quad(lambda w: ghf(w)**2*w**4 if w > mp.mpf('1e-3') else ghf(mp.mpf('1e-3'))**2*w**4, pts)/(16*mp.pi**3)
print("K2 (1-t^2)^4: Fourier side =", mp.nstr(L, 15), " time side =", sp.nsimplify(R), "=", mp.nstr(mp.mpf(sp.N(R, 30)), 15))
chk("K2 Parseval identity (numeric Fourier side vs exact time side, compact g) to 1e-8 rel",
    abs(L-mp.mpf(sp.N(R, 30)))/mp.mpf(sp.N(R, 30)) < 1e-8)

# K3: Lorentzian: g^2 = t0/(pi(t^2+t0^2)) -> Ford-Roman -3/(32 pi^2 t0^4)
gL = sp.sqrt(t0/(sp.pi*(t**2+t0**2)))
BL = -sp.integrate(sp.simplify(sp.diff(gL, t, 2)**2), (t, -sp.oo, sp.oo))/(16*sp.pi**2)
BL = sp.simplify(BL)
print("K3 Lorentzian bound from FS(88) coefficient:", BL)
FR = -sp.Rational(3, 32)/(sp.pi**2*t0**4)
print("K3 ratio to Ford-Roman:", sp.simplify(BL/FR))
chk("K3 ratio == 9/64 (tree fixture NINE_64)", sp.simplify(BL/FR - sp.Rational(9, 64)) == 0)
chk("K3 bound is tighter (less negative) than Ford-Roman: consistent", sp.simplify(BL/FR) < 1)

# K4: control
BLw = 2*BL  # coefficient 1/(8 pi^3)
chk("K4 control: 1/(8 pi^3) does not give 9/64", sp.simplify(BLw/FR - sp.Rational(9, 64)) != 0)

# K5a: pull-back coefficient
r, dt, eps = sp.symbols('r dt epsilon', positive=True)
sg = sp.Symbol('sg')  # s = dt - i eps treated as a formal symbol
Gf = 1/(4*sp.pi**2*(r**2 - sg**2))
# d_t d_t' acting on function of (t - t') = -d_s^2 ; sum_i d_i d_i' = -Laplacian (radial, 3D)
tt = -sp.diff(Gf, sg, 2)
lap = sp.diff(Gf, r, 2) + 2*sp.diff(Gf, r)/r
ss = -lap
coef = sp.simplify(sp.limit(sp.Rational(1, 2)*(tt + ss)*sg**4, r, 0))
print("K5a pull-back coefficient of (t-t'-i eps)^-4:", coef)
chk("K5a coefficient == 3/(2 pi^2)  (FS eq. 84)", sp.simplify(coef - sp.Rational(3, 2)/sp.pi**2) == 0)

# K5b: FT of (t - i eps)^-4 with e^{i xi t}; xi>0 closes in the upper half plane, pole at t = i eps
xi = sp.Symbol('xi', positive=True)
tc = sp.Symbol('tc')
res = sp.residue(sp.exp(sp.I*xi*tc)/(tc - sp.I*eps)**4, tc, sp.I*eps)
ft = sp.simplify(sp.limit(2*sp.pi*sp.I*res, eps, 0))
print("K5b FT of (t-i0)^-4 at xi>0:", ft, "; at xi<0 the pole is not enclosed -> 0")
chk("K5b == pi xi^3/3  (FS p.24, citing Gel'fand-Shilov)", sp.simplify(ft - sp.pi*xi**3/3) == 0)

# K5c/K5d: (86) and (87) on a Gaussian f
eta, zeta = sp.symbols('eta zeta', positive=True)
fh2 = lambda w: 2*sp.pi*s**2*sp.exp(-s**2*w**2)   # |fhat|^2 of Gaussian exp(-t^2/(2 s^2))
B86 = sp.simplify(sp.integrate(sp.integrate(fh2(xi+zeta)*zeta**3, (zeta, 0, sp.oo)), (xi, 0, sp.oo))/(4*sp.pi**2*sp.pi))
B88 = sp.simplify(sp.integrate(fh2(eta)*eta**4, (eta, 0, sp.oo))/(16*sp.pi**3))
B87t = sp.simplify(sp.integrate(sp.integrate(fh2(eta)*zeta**3, (zeta, 0, eta)), (eta, 0, sp.oo))/(4*sp.pi**2))
print("K5c (86) =", B86, "; (88) =", B88, "; (87) as transcribed =", B87t, "; ratio (87t)/(88) =", sp.simplify(B87t/B88))
chk("K5c (86) == (88)", sp.simplify(B86 - B88) == 0)
chk("K5d (87) as transcribed differs from (88) by exactly pi (discrepancy recorded, not a refutation)",
    sp.simplify(B87t/B88 - sp.pi) == 0)

# K6: F&T (5.6) left side at C = 0
w, wp = sp.symbols('w wp', positive=True)
C = 0
FT56 = sp.simplify(sp.integrate(sp.integrate(wp**2*sp.sqrt(wp**2 - C**2)*fh2(w+wp), (wp, 0, sp.oo)), (w, 0, sp.oo))/(4*sp.pi**3))
print("K6 F&T (5.6) double integral at C=0:", FT56)
chk("K6 F&T (5.6) at C=0 == FS (88): same form and constant", sp.simplify(FT56 - B88) == 0)

print("\nRESULT:", "ALL CHECKS PASS" if ok else "A CHECK FAILED")
sys.exit(0 if ok else 1)
