#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key gw-energy-flux-strain.

Tree's use (branelink.py:204-206, 344-347):
    L/(4 pi D^2) = c^3 w^2 h^2 / (16 pi G)   =>   h = (2/(D w)) sqrt(G L / c^3)

Published form (Maggiore eq. 1.153 as restated in Gerosa's GGI 2026 notes L01 p.5,
G = c = 1):  dE/(dA dt) = (1/32pi) <hdot_ij^TT hdot_ij^TT> = (1/16pi) <hdot_+^2 + hdot_x^2>.

Checks, all symbolic unless stated:
 1. The rod's quadrupole (same matrix as branelink.verify_symbolic) projected TT along
    n(theta, phi); flux c^3/(32 pi G) <hdot^TT hdot^TT> integrated over the sphere
    equals the quadrupole luminosity G/(5c^5)<Q''' Q'''> = (2/45) G M^2 l^4 W^6/c^5.
    (Consistency of three textbook formulas: flux, far-field strain 2G/(c^4 r) Lambda Q'',
    and quadrupole luminosity.  The strain formula is NAMED, not read here.)
 2. h_+ = A0 (1+cos^2 th)/2 cos(...), h_x = A0 cos th sin(...): the rod's pattern is the
    binary's pattern (Gerosa L03 p.2, Maggiore 3.330-331).
 3. What the tree's h IS: h_tree^2 == sky-average of <h_+^2 + h_x^2> (total mean-square
    strain).  For a single linear polarisation of PEAK amplitude h the flux is
    c^3 w^2 h^2/(32 pi G) -- a factor 2.
 4. Direction dependence: face-on peak amplitude A0 = sqrt(5/2) h_tree; edge-on
    A_+ = A0/2; the flux ratio at theta to the isotropic figure spans [5/16, 5/2].
 5. Numeric at the tree's design point: h_tree, the range, and the shift in the
    "brane beats bulk by N orders" figure (bits/s/W scale as h^2).
 6. Hypothesis checks at the design point: far zone D >> lambda, slow motion v << c,
    source size << lambda.
"""
import math
import sys

import sympy as sp

ok = True


def chk(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)


t, W, M, ell, G, c, r = sp.symbols('t Omega M ell G c r', positive=True)
th, ph = sp.symbols('theta phi', real=True)

# 1. rod quadrupole (identical to branelink.verify_symbolic)
A = M * ell ** 2 / 12
I = sp.Matrix([[A * sp.cos(W * t) ** 2, A * sp.sin(W * t) * sp.cos(W * t), 0],
               [A * sp.sin(W * t) * sp.cos(W * t), A * sp.sin(W * t) ** 2, 0],
               [0, 0, 0]])
Q = I - sp.eye(3) * I.trace() / 3
n = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])
P = sp.eye(3) - n * n.T


def TT(X):
    return sp.simplify(P * X * P - P * (P * X).trace() / 2)


Q2 = Q.applyfunc(lambda e: sp.diff(e, t, 2))
hTT = TT(Q2) * 2 * G / (c ** 4 * r)                     # far-field strain (NAMED)
hdot = hTT.applyfunc(lambda e: sp.diff(e, t))
per = 2 * sp.pi / W
avg = lambda e: sp.simplify(sp.integrate(sp.expand(sp.expand_trig(e)), (t, 0, per)) / per)
hh = avg(sum(hdot[i, j] ** 2 for i in range(3) for j in range(3)))
F = c ** 3 / (32 * sp.pi * G) * hh                        # published flux, TT form
Ltot = sp.simplify(sp.integrate(sp.integrate(F * r ** 2 * sp.sin(th), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi)))
Q3 = Q.applyfunc(lambda e: sp.diff(e, t, 3))
Lquad = avg(G / (5 * c ** 5) * sum(Q3[i, j] ** 2 for i in range(3) for j in range(3)))
chk("1. sphere integral of c^3/(32piG)<hdot^TT hdot^TT> r^2 == G/(5c^5)<Q'''Q'''>",
    sp.simplify(Ltot - Lquad) == 0)
chk("1b. that luminosity == (2/45) G M^2 l^4 W^6/c^5",
    sp.simplify(Lquad - sp.Rational(2, 45) * G * M ** 2 * ell ** 4 * W ** 6 / c ** 5) == 0)

# 2. polarisations at phi = 0: basis e_theta, e_phi
eth = sp.Matrix([sp.cos(th), 0, -sp.sin(th)])
eph = sp.Matrix([0, 1, 0])
hTT0 = hTT.subs(ph, 0)
hp = sp.simplify((eth.T * hTT0 * eth)[0] - 0 * t)
hp = sp.simplify(((eth.T * hTT0 * eth)[0] - (eph.T * hTT0 * eph)[0]) / 2)
hx = sp.simplify((eth.T * hTT0 * eph)[0])
A0 = sp.simplify(hp.subs({th: 0, t: 0}))
A0 = sp.Abs(A0)
chk("2a. h_+^2 == [A0 (1+cos^2 th)/2 cos(2 W t)]^2  (A0 = G M l^2 W^2/(3 c^4 r))",
    sp.simplify(hp ** 2 - (G * M * ell ** 2 * W ** 2 / (3 * c ** 4 * r)
                * (1 + sp.cos(th) ** 2) / 2 * sp.cos(2 * W * t)) ** 2) == 0)
chk("2b. |h_x| == A0 cos th |sin(2 W t)|",
    sp.simplify(hx ** 2 - (G * M * ell ** 2 * W ** 2 / (3 * c ** 4 * r)
                           * sp.cos(th) * sp.sin(2 * W * t)) ** 2) == 0)
chk("2c. polarisation form: <hdot^TT hdot^TT> == 2 <hdot_+^2 + hdot_x^2>  (so 1/32pi <-> 1/16pi)",
    sp.simplify(sp.trigsimp(hh.subs(ph, 0)) - 2 * avg(sp.diff(hp, t) ** 2 + sp.diff(hx, t) ** 2)) == 0)

# 3. what the tree's h is
w = 2 * W
L = sp.Rational(2, 45) * G * M ** 2 * ell ** 4 * W ** 6 / c ** 5
h_tree_sq = 4 * G * L / (c ** 3 * w ** 2 * r ** 2)       # tree: h = (2/(D w)) sqrt(G L/c^3)
msq = avg(hp ** 2 + hx ** 2)                              # <h_+^2 + h_x^2>(theta)
msq_sky = sp.simplify(sp.integrate(msq * sp.sin(th), (th, 0, sp.pi)) / 2)
chk("3a. h_tree^2 == sky-average of <h_+^2 + h_x^2>  (the tree's h is the sky-rms total strain)",
    sp.simplify(h_tree_sq - msq_sky) == 0)
hlin = sp.Symbol('h', positive=True)
Flin = c ** 3 / (16 * sp.pi * G) * avg(sp.diff(hlin * sp.cos(w * t), t) ** 2)
chk("3b. single linear polarisation, peak h: F = c^3 w^2 h^2/(32 pi G)  (half the tree's form)",
    sp.simplify(Flin - c ** 3 * w ** 2 * hlin ** 2 / (32 * sp.pi * G)) == 0)
hcirc = c ** 3 / (16 * sp.pi * G) * avg(sp.diff(hlin * sp.cos(w * t), t) ** 2 + sp.diff(hlin * sp.sin(w * t), t) ** 2)
chk("3c. circular, peak h in each polarisation: F = c^3 w^2 h^2/(16 pi G)  (the tree's form exactly)",
    sp.simplify(hcirc - c ** 3 * w ** 2 * hlin ** 2 / (16 * sp.pi * G)) == 0)

# 4. direction dependence
A0sq = (G * M * ell ** 2 * W ** 2 / (3 * c ** 4 * r)) ** 2
chk("4a. face-on peak A0^2 == (5/2) h_tree^2", sp.simplify(A0sq - sp.Rational(5, 2) * h_tree_sq) == 0)
ratio = sp.simplify(msq / msq_sky)
chk("4b. flux(theta)/isotropic == (5/8)[(1+cos^2)^2/4 ... ] : face-on 5/2, edge-on 5/16",
    sp.simplify(ratio.subs(th, 0) - sp.Rational(5, 2)) == 0 and sp.simplify(ratio.subs(th, sp.pi / 2) - sp.Rational(5, 16)) == 0)

# 5. numeric at the design point (constants as the tree asks them: foliation.py)
Cn, Gn = 2.99792458e8, 6.67430e-11
D = 4.2465 * 9.4607304725808e15
Mk, lk, Wk = 1.0e6, 100.0, 100.0
Ln = 2 / 45 * Gn * Mk ** 2 * lk ** 4 * Wk ** 6 / Cn ** 5
wn = 2 * Wk
hn = (2 / (D * wn)) * math.sqrt(Gn * Ln / Cn ** 3)
print("   L_GW = %.6e W ; h_tree = %.4e ; face-on A0 = %.4e ; edge-on A+ = %.4e"
      % (Ln, hn, math.sqrt(2.5) * hn, math.sqrt(2.5) * hn / 2))
chk("5a. h_tree reproduces the tree's 4.3359e-48", abs(hn / 4.3359e-48 - 1) < 1e-4)
shift = math.log10(2.5)
print("   bits/s/W ~ h^2: best direction shifts '26.62 orders' by at most %.3f orders -> >= %.2f"
      % (shift, 26.62 - shift))
# detector-seen PEAK amplitude^2 of an optimally oriented interferometer, / h_tree^2:
# face-on circular A0^2 = 5/2; edge-on linear A+^2 = (A0/2)^2 = 5/8
pk = [sp.Rational(5, 2), sp.Rational(5, 8)]
chk("5c. detector-seen peak^2 / h_tree^2 spans [5/8, 5/2] (face-on, edge-on)",
    sp.simplify(A0sq / h_tree_sq - pk[0]) == 0 and sp.simplify(A0sq / 4 / h_tree_sq - pk[1]) == 0)
print("   if bits/s ~ (peak/h_n)^2: the 26.62-order gap lies in [%.2f, %.2f]"
      % (26.62 - math.log10(2.5), 26.62 - math.log10(0.625)))
chk("5b. direction choice moves the 26.62-order gap by < 1 order", shift < 1)
# 6. hypotheses at the design point
lam = 2 * math.pi * Cn / wn
v = Wk * lk / 2
print("   lambda_GW = %.4e m ; D/lambda = %.3e ; v_tip/c = %.3e ; l/lambda = %.3e"
      % (lam, D / lam, v / Cn, lk / lam))
chk("6a. far zone D >> lambda", D / lam > 1e6)
chk("6b. slow motion v << c and source << lambda", v / Cn < 1e-3 and lk / lam < 1e-3)
# out-of-scope observation (not graded): centripetal hoop stress of the rod
# sigma_max ~ rho W^2 l^2 / 8 for a uniform rod about its centre
print("   (out of scope) peak tensile stress of a uniform rod ~ rho W^2 l^2/8 = %.2e Pa at rho = 7850"
      % (7850 * Wk ** 2 * lk ** 2 / 8))
print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
