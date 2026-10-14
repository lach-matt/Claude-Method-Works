#!/usr/bin/env python3
r"""
DOCKET 67, pass S, item 23: asymptotic-flatness-cylindrical-owner-form.

Audits the boundary condition axial.py (research/warp-drive/axial.py:44-45, 187)
calls "asymptotic flatness":  W -> r, W' -> 1, W Psi' -> 0,  for
    ds^2 = -e^{2Phi}dt^2 + dr^2 + e^{2Psi}dz^2 + W^2 dphi^2   (Lambda = 0 gauge).

Independent of axial.py: the Einstein tensor is recomputed here from scratch.

CHECKS
  C1  8 pi u W = -(W Psi')' - W Psi'^2 - W''     (u = -G^t_t / 8 pi), residual 0
  C2  the integrated identity with GENERAL end values:
        INT_0^R 8 pi u W dr = -[W Psi' + W']_0^R - INT_0^R W Psi'^2 dr
      so with a regular axis and W Psi' -> 0 at infinity, W' -> k:
        INT_0^inf 8 pi u W dr = (1 - k) - INT_0^inf W Psi'^2 dr
  C3  cosmic-string consistency: Psi' = 0, u >= 0 compact  ->  deficit angle
      2 pi (1 - k) = 8 pi mu,  mu = 2 pi INT u W dr   (G = c = 1).  So a
      positive-mu static cylinder has k < 1: it is NOT asymptotically flat in
      the owner's form.
  C4  owner's form ALONE (k = 1, regular axis) + u >= 0 everywhere forces
      u == 0, Psi' == 0, W == r -- independent of contraction.  Shown by the
      identity (sign argument) and illustrated numerically.
  C5  vacuum exterior: R^z_z = 0 gives (A Psi')' = 0 with A = W e^{Psi+Phi};
      so in vacuum W Psi' -> 0 forces Psi' == 0 there (Levi-Civita sigma = 0
      branch only).
  C6  EXPLICIT PROFILE under conical ("string") asymptotics, k < 1:
        Psi = -psi0 exp(-r^2/a^2)   (axial contraction, Psi < 0)
        W   = r - delta (r - (sqrt(pi) b/2) erf(r/b)),  W(0)=0, W'(0)=1,
              W' -> 1 - delta
      with u >= 0 EVERYWHERE (dense grid + exact axis value + large-r
      asymptotic ratio).  Pressures are reported, not hidden.
  C7  tail check of the tree's own truncation r_max = 60 for its profiles.
"""
import math
import sys

import sympy as sp

ok_all = True


def rep(label, good, detail=""):
    global ok_all
    ok_all &= bool(good)
    print("  [%s] %s %s" % ("ok" if good else "XX", label, detail))


r = sp.Symbol('r', positive=True)
t, z, ph = sp.symbols('t z phi', real=True)
Phi = sp.Function('Phi')(r)
Psi = sp.Function('Psi')(r)
W = sp.Function('W')(r)
X = [t, r, z, ph]
g = sp.diag(-sp.exp(2 * Phi), 1, sp.exp(2 * Psi), W ** 2)
gi = g.inv()
N = 4
Gam = [[[sp.simplify(sum(gi[A, D] * (sp.diff(g[D, B], X[C]) + sp.diff(g[D, C], X[B])
                                     - sp.diff(g[B, C], X[D])) for D in range(N)) / 2)
         for C in range(N)] for B in range(N)] for A in range(N)]
Ric = sp.zeros(N)
for B in range(N):
    for C in range(N):
        e = 0
        for A in range(N):
            e += sp.diff(Gam[A][B][C], X[A]) - sp.diff(Gam[A][B][A], X[C])
            for D in range(N):
                e += Gam[A][A][D] * Gam[D][B][C] - Gam[A][C][D] * Gam[D][B][A]
        Ric[B, C] = sp.simplify(e)
Rs = sp.simplify(sum(gi[A, B] * Ric[A, B] for A in range(N) for B in range(N)))
Gmix = sp.simplify(gi * Ric - sp.eye(N) * Rs / 2)       # G^a_b
Rmix = sp.simplify(gi * Ric)

dPs = sp.diff(Psi, r)
print("C1  THE IDENTITY (independent recomputation)")
u8 = -Gmix[0, 0]
res = sp.simplify(sp.expand(u8 * W + sp.diff(W * dPs, r) + W * dPs ** 2 + sp.diff(W, r, 2)))
rep("8 pi u W + (W Psi')' + W Psi'^2 + W'' == 0", res == 0, "residual=%s" % res)
rep("u independent of Phi", sp.simplify(sp.diff(u8, sp.Derivative(Phi, r))) == 0 and
    sp.simplify(sp.diff(u8, Phi)) == 0)

print("\nC2  INTEGRATED FORM, GENERAL END VALUES")
# the integrand of 8 pi u W is an exact derivative plus -W Psi'^2:
exact = sp.simplify(u8 * W + W * dPs ** 2 - sp.diff(-(W * dPs) - sp.diff(W, r), r))
rep("8 pi u W = d/dr[-(W Psi' + W')] - W Psi'^2", exact == 0)
print("      => INT_0^inf 8 pi u W = (W'(0) - k) + W(0)Psi'(0) - lim W Psi' - INT W Psi'^2")
print("      regular axis (W(0)=0, W'(0)=1), W Psi' -> 0, W' -> k:  = (1 - k) - INT W Psi'^2")

print("\nC3  COSMIC STRING (Psi' = 0): deficit = 8 pi mu")
# Psi' = 0: 8 pi u W = -W''  ->  INT 8 pi u W = 1 - k ; mu = 2 pi INT u W
k_ = sp.Symbol('k', positive=True)
mu = 2 * sp.pi * (1 - k_) / (8 * sp.pi)
deficit = 2 * sp.pi * (1 - k_)
rep("deficit angle 2pi(1-k) == 8 pi mu (G=1), i.e. Vilenkin's 8 pi G mu",
    sp.simplify(deficit - 8 * sp.pi * mu) == 0,
    "(axial.py sec.3 itself states the deficit is 8 pi G mu)")
# explicit positive-u string core
rr = sp.Symbol('rr', positive=True)
dl = sp.Rational(3, 10)
Wstr = rr - dl * (rr - sp.sqrt(sp.pi) / 2 * sp.erf(rr))      # b = 1
ustr = -sp.diff(Wstr, rr, 2) / (8 * sp.pi * Wstr)
kstr = sp.limit(sp.diff(Wstr, rr), rr, sp.oo)
mu_num = sp.N(2 * sp.pi * sp.Integral(ustr * Wstr, (rr, 0, sp.oo)))
print("      example core, delta=0.3: k = %s, mu = %.12f, 1-4mu = %.12f"
      % (kstr, float(mu_num), 1 - 4 * float(mu_num)))
rep("u >= 0 string core has W' -> k = 1 - 4 mu < 1 (owner's form FAILS)",
    abs(float(kstr) - (1 - 4 * float(mu_num))) < 1e-12 and float(kstr) < 1)

print("\nC4  OWNER'S FORM ALONE FORCES THE SIGN, CONTRACTION OR NOT")
print("      k = 1, regular axis:  INT 8 pi u W = -INT W Psi'^2 <= 0.  If u >= 0 everywhere,")
print("      then INT u W >= 0, so both sides vanish: Psi' == 0 and INT u W = 0 with u >= 0,")
print("      W > 0  =>  u == 0  =>  W'' = 0  =>  W = r.  (Pure sign argument; no contraction used.)")
# numeric illustration: Psi' = 0, W = r + w0 r^3 exp(-r^2) (owner form), u changes sign
w0 = 0.4
f = lambda x: -(2 * x * w0 * (3 - 7 * x ** 2 + 2 * x ** 4) * math.exp(-x * x)) / (
    8 * math.pi * (x + w0 * x ** 3 * math.exp(-x * x)))
vals = [f(0.001 + 0.001 * i) for i in range(8000)]
rep("Psi'=0 owner-form profile (w0=0.4) with no contraction still has u<0 somewhere",
    min(vals) < 0 < max(vals), "min u=%.4e max u=%.4e" % (min(vals), max(vals)))

print("\nC5  VACUUM EXTERIOR: (A Psi')' = 0, A = W e^{Psi+Phi}")
A_ = W * sp.exp(Psi + Phi)
res5 = sp.simplify(sp.expand(Rmix[2, 2] + sp.diff(A_ * dPs, r) / A_))
rep("R^z_z = -(A Psi')'/A", res5 == 0)
print("      in vacuum A Psi' = const; A -> W e^{const} so W Psi' -> 0 iff const = 0 iff Psi' == 0")
print("      in the exterior: the owner's form admits only the sigma = 0 Levi-Civita exterior.")

print("\nC6  EXPLICIT CONTRACTING PROFILE WITH u >= 0 EVERYWHERE, CONICAL ASYMPTOTICS")
psi0, a, b, delta = sp.Rational(1, 20), sp.Integer(1), sp.Integer(2), sp.Rational(3, 5)
PsiE = -psi0 * sp.exp(-r ** 2 / a ** 2)
WE = r - delta * (r - sp.sqrt(sp.pi) * b / 2 * sp.erf(r / b))
subsd = {Psi: PsiE, W: WE, Phi: 0}


def ev(expr):
    return sp.simplify(expr.subs(subsd).doit())


u8E = sp.simplify(-(sp.diff(WE * sp.diff(PsiE, r), r)) / WE - sp.diff(PsiE, r) ** 2
                  - sp.diff(WE, r, 2) / WE)
rep("W(0)=0", sp.limit(WE, r, 0) == 0)
rep("W'(0)=1 (regular axis)", sp.limit(sp.diff(WE, r), r, 0) == 1)
kE = sp.limit(sp.diff(WE, r), r, sp.oo)
rep("W' -> k = 1 - delta = %s (conical, NOT owner's W'->1)" % kE, kE == 1 - delta)
rep("W Psi' -> 0", sp.limit(WE * sp.diff(PsiE, r), r, sp.oo) == 0)
rep("Psi < 0 everywhere: axial contraction Gamma_z = e^{-Psi} > 1", True,
    "Psi(0) = %s" % PsiE.subs(r, 0))
u8_0 = sp.limit(u8E, r, 0)
rep("8 pi u at the axis = 2 delta/b^2 - 4 psi0/a^2 > 0", sp.simplify(u8_0 - (2 * delta / b ** 2 - 4 * psi0 / a ** 2)) == 0 and u8_0 > 0,
    "= %s" % u8_0)
# large r: ratio of u to the pure -W''/W term tends to 1
tailratio = sp.limit(u8E / (-sp.diff(WE, r, 2) / WE), r, sp.oo)
rep("large r: u / (-W''/(8 pi W)) -> 1, and -W'' > 0, so u > 0 in the tail",
    tailratio == 1, "limit=%s" % tailratio)
uf = sp.lambdify(r, u8E / (8 * sp.pi), "mpmath")
import mpmath as mp
mp.mp.dps = 30
grid = [mp.mpf(i) / 2000 for i in range(1, 2000 * 12 + 1)]       # (0, 12]
umin = min(uf(x) for x in grid)
rep("min u on 24000-point grid over (0,12] is >= 0", umin >= 0, "min u = %s" % mp.nstr(umin, 8))
# check beyond 12 with coarse grid and positivity of each part
grid2 = [mp.mpf(12) + mp.mpf(i) / 10 for i in range(0, 481)]
umin2 = min(uf(x) for x in grid2)
rep("min u over [12,60] >= 0", umin2 >= 0, "min u = %s" % mp.nstr(umin2, 8))
# the integrated balance
Iu = mp.quad(lambda x: 8 * mp.pi * uf(x) * sp.lambdify(r, WE, "mpmath")(x), [0, 2, 6, 20, mp.inf])
Ig = mp.quad(lambda x: sp.lambdify(r, WE * sp.diff(PsiE, r) ** 2, "mpmath")(x), [0, 2, 6, 20, mp.inf])
rep("INT 8 pi u W = (1-k) - INT W Psi'^2", abs(Iu - (1 - mp.mpf(2) / 5) + Ig) < mp.mpf(10) ** -12,
    "INT 8piuW=%s, 1-k=%s, INT W Psi^2=%s, residual=%s" % (mp.nstr(Iu, 15), float(1 - kE), mp.nstr(Ig, 15), mp.nstr(Iu - (1 - mp.mpf(2) / 5) + Ig, 3)))
muE = Iu / 4        # mu = 2 pi INT u W = INT 8 pi u W / 4
print("      mass per unit length mu = %s > 0; deficit/(2pi) = delta = 4 mu + INT W Psi'^2"
      % mp.nstr(muE, 12))
# pressures (Phi = 0), reported
pr = ev(Gmix[1, 1] / (8 * sp.pi))
pz = ev(Gmix[2, 2] / (8 * sp.pi))
pp = ev(Gmix[3, 3] / (8 * sp.pi))
uu = u8E / (8 * sp.pi)
fs = {n: sp.lambdify(r, e, "mpmath") for n, e in
      (("u+p_r", uu + pr), ("u+p_z", uu + pz), ("u+p_phi", uu + pp))}
for n, fn in fs.items():
    vals = [fn(x) for x in grid[::20]]
    print("      Phi=0: %-8s min %s  max %s" % (n, mp.nstr(min(vals), 6), mp.nstr(max(vals), 6)))
print("      Phi = 0 violates the z-direction NEC somewhere.  Phi is FREE (u does not contain")
print("      it) so choose Phi = Psi: then 8 pi (u + p_z) = [(W Phi')' + W Phi'^2 - (W Psi')'")
print("      - W Psi'^2]/W = 0 identically, and the other two are checked below.")
subs2 = {Psi: PsiE, W: WE, Phi: PsiE}
def ev2(expr):
    return sp.simplify(expr.subs(subs2).doit())
nec = {"u+p_r": ev2((-Gmix[0, 0] + Gmix[1, 1]) / (8 * sp.pi)),
       "u+p_z": ev2((-Gmix[0, 0] + Gmix[2, 2]) / (8 * sp.pi)),
       "u+p_phi": ev2((-Gmix[0, 0] + Gmix[3, 3]) / (8 * sp.pi))}
uu2 = ev2(-Gmix[0, 0] / (8 * sp.pi))
rep("u unchanged by Phi = Psi", sp.simplify(uu2 - u8E / (8 * sp.pi)) == 0)
rep("Phi = Psi: u + p_z == 0 identically", sp.simplify(nec["u+p_z"]) == 0)
necmins = {}
for n in ("u+p_r", "u+p_phi"):
    fn = sp.lambdify(r, nec[n], "mpmath")
    necmins[n] = min(min(fn(x) for x in grid), min(fn(x) for x in grid2))
    tl = sp.limit(nec[n] / (-sp.diff(WE, r, 2) / (8 * sp.pi * WE)), r, sp.oo)
    rep("Phi = Psi: min %s over (0,60] >= 0, tail ratio to -W''/(8 pi W) -> %s" % (n, tl),
        necmins[n] >= 0 and tl == 1, "min = %s" % mp.nstr(necmins[n], 8))
    ax = sp.limit(nec[n], r, 0)
    rep("  and %s at the axis = %s > 0" % (n, ax), ax > 0)
print("      => with Phi = Psi the profile satisfies the WEC (u >= 0 and every u + p_i >= 0,")
print("         T diagonal, so type I) on the checked grid, with exact axis and tail limits.")
fpr = sp.lambdify(r, nec["u+p_r"] - uu2, "mpmath"); fpp = sp.lambdify(r, nec["u+p_phi"] - uu2, "mpmath")
fu = sp.lambdify(r, uu2, "mpmath")
dec = min(min(fu(x) - abs(fpr(x)), fu(x) - abs(fpp(x)), fu(x) - abs(-fu(x))) for x in grid)
print("      DEC margin min_r [u - max|p_i|] on (0,12] = %s  (reported, not required)" % mp.nstr(dec, 6))

print("\nC7  THE TREE'S TRUNCATION r_max = 60")
worst = max(math.exp(-(60.0 / a_) ** 2) * 60 ** 5 for a_ in (1.0, 0.7, 2.2, 0.5, 3.0, 1.7, 1.4, 0.9, 2.0, 0.6, 2.5))
rep("Gaussian tails of axial.py's profiles at r=60 below 1e-150", worst < 1e-150, "bound=%.3e" % worst)

print("\nVERDICT DATA:  identity re-derived (C1,C2); owner's form excludes every positive-mu")
print("static cylinder (C3,C4); under the literature's conical ('string') asymptotics a")
print("contracting static cylinder with u >= 0 everywhere exists (C6).")
print("\nALL CHECKS %s" % ("OK" if ok_all else "FAILED"))
sys.exit(0 if ok_all else 1)
