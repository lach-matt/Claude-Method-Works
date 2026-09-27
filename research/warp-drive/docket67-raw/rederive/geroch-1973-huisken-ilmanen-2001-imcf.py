#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Geroch monotonicity of the Hawking (= Geroch, time-symmetric)
mass under inverse mean curvature flow (IMCF), as restated in Mars arXiv:0906.5566 eq.(17)-(18)
and Hirsch arXiv:2210.12237 eq.(6).  Checks:

 A  symbolic: the pointwise algebra that turns the IMCF evolution equations + Gauss equation +
    Gauss-Bonnet into  dm_H/dt = sqrt(|N|/16pi) [ (2-chi)/4 + (1/16pi) int (2|grad H|^2/H^2 + |A0|^2 + R) ].
 B  symbolic: spherically symmetric 3-metric dr^2/(1-2m(r)/r) + r^2 dOmega^2 -- scalar curvature
    computed from Christoffels, m_H(round sphere) = m(r) (Misner-Sharp), IMCF r' = r/2, and
    dm_H/dt = r^3 R/8, identical to the general formula of A.
 C  numeric/symbolic: a NON-round axisymmetric surface in flat R^3; d/dt int H^2 under normal
    speed 1/H computed EXACTLY by differentiating the moved surface, against the Geroch RHS.
 D  counterexample to the hypothesis the tree drops: two disjoint round spheres (chi = 4) in flat
    R^3 under IMCF -- m_H strictly DECREASES although R = 0 >= 0.
 E  Schwarzschild: R = 0, m_H constant = M along IMCF; horizon area 16 pi M^2 saturates the RPI.
Exit 0 iff every check passes."""
import sys
import sympy as sp
import mpmath as mp

ok = True
def check(name, cond, detail=""):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ((" -- " + detail) if detail else ""))

# ---------------- A: pointwise algebra ----------------
H, A0sq, R, K, gH2, area, chi = sp.symbols('H A0sq R K gradH2 area chi', real=True)
Asq = A0sq + H**2/2                      # |A|^2 = |A0|^2 + H^2/2  (2-surface)
Ric_nn = (R - 2*K + H**2 - Asq)/2        # twice-contracted Gauss equation
# integrand of d/dt int H^2 dmu for speed f = 1/H:  dH/dt = -Lap f - (|A|^2+Ric)f, dmu/dt = H f dmu = dmu
# after integrating by parts  int -2 H Lap(1/H) = -2 int |grad H|^2/H^2
integrand = -2*gH2/H**2 + 2*H*(-(Asq + Ric_nn)/H) + H**2
target = -2*gH2/H**2 - A0sq - R + 2*K - H**2/2
check("A1 d/dt int H^2 integrand = -2|dH|^2/H^2 - |A0|^2 - R + 2K - H^2/2",
      sp.simplify(integrand - target) == 0)
# integrate: int 2K = 4 pi chi (Gauss-Bonnet); symbols for integrals
I_H2, I_pos = sp.symbols('I_H2 I_pos', real=True)   # I_pos = int(2|dH|^2/H^2 + |A0|^2 + R)
dIH2 = -I_pos + 4*sp.pi*chi - I_H2/2
A_ = sp.symbols('Area', positive=True)
mH = sp.sqrt(A_/(16*sp.pi))*(1 - I_H2/(16*sp.pi))
# dA/dt = A under IMCF
dmH = sp.diff(mH, A_)*A_ + sp.diff(mH, I_H2)*dIH2
geroch = sp.sqrt(A_/(16*sp.pi))*((2 - chi)/4 + I_pos/(16*sp.pi))
check("A2 dm_H/dt = sqrt(|N|/16pi)[(2-chi)/4 + (1/16pi) int(2|dH|^2/H^2+|A0|^2+R)]",
      sp.simplify(dmH - geroch) == 0)
check("A3 chi=2 (connected sphere): constant term vanishes, so R>=0 => dm_H/dt >= 0",
      sp.simplify(geroch.subs(chi, 2) - sp.sqrt(A_/(16*sp.pi))*I_pos/(16*sp.pi)) == 0)

# ---------------- B: spherical symmetry ----------------
r, th, ph = sp.symbols('r theta phi', positive=True)
m = sp.Function('m')(r)
x = [r, th, ph]
g = sp.diag(1/(1 - 2*m/r), r**2, r**2*sp.sin(th)**2)
gi = g.inv()
n = 3
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
                         for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
def Ric(b, c):
    return sp.simplify(sum(sp.diff(Gam[a][b][c], x[a]) - sp.diff(Gam[a][b][a], x[c])
                           + sum(Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a] for d in range(n))
                           for a in range(n)))
Rs = sp.simplify(sum(gi[b, c]*Ric(b, c) for b in range(n) for c in range(n)))
check("B1 scalar curvature R = 4 m'(r)/r^2", sp.simplify(Rs - 4*sp.diff(m, r)/r**2) == 0, str(Rs))
Hs = 2*sp.sqrt(1 - 2*m/r)/r                       # mean curvature of the round sphere
Asph = 4*sp.pi*r**2
mHs = sp.sqrt(Asph/(16*sp.pi))*(1 - Asph*Hs**2/(16*sp.pi))
check("B2 m_H(round sphere) = m(r)  [Misner-Sharp reduction]", sp.simplify(mHs - m) == 0)
drdt = sp.sqrt(1 - 2*m/r)/Hs                       # proper normal speed 1/H
check("B3 IMCF on round spheres: dr/dt = r/2 (area ~ e^t)", sp.simplify(drdt - r/2) == 0)
dmHdt = sp.diff(mHs, r)*drdt
gen = sp.sqrt(Asph/(16*sp.pi))*(Rs*Asph)/(16*sp.pi)   # formula A with chi=2, dH=0, A0=0
check("B4 dm_H/dt = r^3 R/8 = general Geroch formula (so monotone iff m' >= 0 iff R >= 0)",
      sp.simplify(dmHdt - gen) == 0 and sp.simplify(dmHdt - r**3*Rs/8) == 0)

# ---------------- C: non-round surface in flat R^3 ----------------
t, eps = sp.symbols('t epsilon', real=True)
a = sp.Rational(3, 20)
rr = 1 + a*(3*sp.cos(t)**2 - 1)/2           # r(theta) = 1 + a P2(cos theta)
X = sp.Matrix([rr*sp.sin(t), rr*sp.cos(t)])  # (rho, z)
def geom(Xc):
    Xp = Xc.diff(t); Xpp = Xp.diff(t)
    s = sp.sqrt(Xp[0]**2 + Xp[1]**2)
    nu = sp.Matrix([-Xp[1], Xp[0]])/s
    k1 = -(Xpp.dot(nu))/s**2
    k2 = nu[0]/Xc[0]
    return Xp, s, nu, k1, k2
Xp, s, nu, k1, k2 = geom(X)
Hc = k1 + k2
Xe = X + eps*nu/Hc
_, se, _, k1e, k2e = geom(Xe)
He = k1e + k2e
intg_e = 2*sp.pi*Xe[0]*se*He**2
dint = sp.diff(intg_e, eps).subs(eps, 0)
f_d = sp.lambdify(t, dint, 'mpmath')
f_H2 = sp.lambdify(t, 2*sp.pi*X[0]*s*Hc**2, 'mpmath')
f_pos = sp.lambdify(t, 2*sp.pi*X[0]*s*(2*(Hc.diff(t)/s)**2/Hc**2 + (k1 - k2)**2/2), 'mpmath')
f_area = sp.lambdify(t, 2*sp.pi*X[0]*s, 'mpmath')
f_dA = sp.lambdify(t, sp.diff(2*sp.pi*Xe[0]*se, eps).subs(eps, 0), 'mpmath')
mp.mp.dps = 30
Q = lambda f: mp.quad(f, [0, mp.pi/2, mp.pi])
lhs = Q(f_d); IH2 = Q(f_H2); Ipos = Q(f_pos); Ar = Q(f_area); dAr = Q(f_dA)
rhs = -Ipos + 4*mp.pi*2 - IH2/2
check("C1 d|N|/dt = |N| under IMCF (non-round surface)", abs(dAr - Ar) < mp.mpf('1e-20'),
      "d|N|/dt=%s |N|=%s" % (mp.nstr(dAr, 15), mp.nstr(Ar, 15)))
check("C2 exact d/dt int H^2 equals Geroch RHS (R=0, chi=2) on non-round surface",
      abs(lhs - rhs) < mp.mpf('1e-18'), "lhs=%s rhs=%s" % (mp.nstr(lhs, 18), mp.nstr(rhs, 18)))
mHc = mp.sqrt(Ar/(16*mp.pi))*(1 - IH2/(16*mp.pi))
dmHc = mp.sqrt(Ar/(16*mp.pi))*Ipos/(16*mp.pi)
check("C3 m_H < 0 on this flat-space surface and dm_H/dt > 0 (Willmore: int H^2 > 16pi)",
      mHc < 0 and dmHc > 0, "m_H=%s dm_H/dt=%s intH2/16pi=%s" % (mp.nstr(mHc, 10), mp.nstr(dmHc, 10), mp.nstr(IH2/(16*mp.pi), 10)))

# ---------------- D: disconnected counterexample ----------------
# two unit spheres far apart in flat R^3: each evolves r_i = e^{t/2}; int H^2 = 2*16pi for all t
T = sp.symbols('T', nonnegative=True)
Ad = 2*4*sp.pi*sp.exp(T)
mHd = sp.sqrt(Ad/(16*sp.pi))*(1 - 32*sp.pi/(16*sp.pi))
dmHd = sp.diff(mHd, T)
check("D1 two spheres (chi=4), R=0: m_H = -sqrt(e^T/2), dm_H/dt < 0 -> monotonicity FAILS without connectedness",
      sp.simplify(mHd + sp.sqrt(sp.exp(T)/2)) == 0 and sp.simplify(dmHd.subs(T, 0)) < 0,
      "dm_H/dt|_0 = %s ; formula constant term (2-chi)/4 = %s" % (sp.nsimplify(dmHd.subs(T, 0)), sp.Rational(2 - 4, 4)))
gd = geroch.subs({chi: 4, I_pos: 0, A_: 8*sp.pi})
check("D2 the general formula predicts the same decrease (chi=4, I_pos=0)",
      sp.simplify(gd - dmHd.subs(T, 0)) == 0, str(sp.simplify(gd)))
# torus-type (chi=0) smooth leaves: constant term +1/2 >= 0 -- genus is not the failure, disconnection is
check("D3 chi<=2 (any connected closed surface) keeps the constant term >= 0",
      all(sp.Rational(2 - c, 4) >= 0 for c in (2, 0, -2, -4)))

# ---------------- E: Schwarzschild ----------------
M = sp.symbols('M', positive=True)
Rsch = sp.simplify(Rs.subs(m, M).doit())
mHsch = sp.simplify(mHs.subs(m, M).doit())
check("E1 Schwarzschild slice: R = 0 and m_H(round sphere) = M for all r (equality case)",
      Rsch == 0 and sp.simplify(mHsch - M) == 0)
Ahor = 4*sp.pi*(2*M)**2
check("E2 horizon r=2M: sqrt(|S|/16pi) = M, RPI saturated", sp.simplify(sp.sqrt(Ahor/(16*sp.pi)) - M) == 0)

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
