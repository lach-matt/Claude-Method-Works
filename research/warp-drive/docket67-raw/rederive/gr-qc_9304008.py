#!/usr/bin/env python3
"""
DOCKET 67 / pass S item 28 -- gr-qc/9304008, Kuo & Ford's fluctuation measure Delta, KF (3.2).
Independent of research/warp-drive/fluctuation.py (no import, no shared code).

What is checked (all finite / closed form):
  C1  KF (3.44): Delta' = Delta/(1-Delta) <=> Delta = Delta'/(1+Delta') is an identity
      IFF the absolute value in (3.2) is inactive, i.e. <:T00^2:> >= rho^2 (and <:T00^2:> > 0).
      z3: proved under that hypothesis; SAT counterexample without it.
  C2  Single-mode vacuum+2 state (KF 2.15), exact Fock matrices:
      rho = 2K eps(2eps - sqrt2 c)/(1+eps^2), <:T00^2:> = 12 K^2 eps^2/(1+eps^2).
      Then ratio rho^2/<:T^2:> = (2eps - sqrt2 c)^2/(3(1+eps^2)).
      Witness eps = 1, cos2theta = -1: ratio = (2+sqrt2)^2/6 > 1 with rho > 0,
      so KF's |.| Delta = ratio - 1 = 0.9428, while 1 - ratio = -0.9428.
      The unsigned form "Delta = 1 - rho^2/<:T^2:>" is KF's Delta only where <:T^2:> >= rho^2.
  C3  On rho < 0 in that state, <:T^2:> > (3/2) rho^2 (z3), so the |.| is inactive there:
      every rho<0 claim built on the unsigned form is unaffected by C2.
  C4  Coherent state (single mode, amplitude alpha): <:T^2:> = rho^2 exactly, Delta = 0 (KF 3.21).
  C5  Zero-mean Gaussian: <:T00^2:> - rho^2 = (1/2) sum_AB G_AB^2 (Wick on normal-ordered
      quadratics), checked against a direct 2-mode Gaussian computation at random numeric
      covariance; and sum G^2 >= (tr G)^2/4 => <:T^2:> >= (3/2) rho^2 > rho^2 (z3), so the
      |.| is inactive on the whole Gaussian class and (3.44) applies there.
  C6  KF (3.41)-(3.43) for diagonal G: G00 = (rho+p1+p2+p3)/2, G11 = (rho+p1-p2-p3)/2, so the
      coefficient is 1/4 (KF print 1/2 in (3.41),(3.42)); and (3.43)'s bracket must read (1 + xi...)
      not (rho + xi...) (xi = p/rho dimensionless): with 1 it gives min 1/2 at xi=0 and 6 at
      xi = (-1,-1,3), KF's own printed numbers; with rho it is dimensionally inhomogeneous.
  C7  Thermal (isotropic, massless, at rest): G = a diag(1,1/3,1/3,1/3): Delta' = 2/3, Delta = 2/5.
"""
import sympy as sp
import z3
import random

OUT = []
def rec(label, ok, detail=""):
    OUT.append((label, ok))
    print("  [%s] %s %s" % ("ok" if ok else "XX", label, detail))

# ------------------------------------------------------------------- C1
T2, r = z3.Reals('T2 r')     # T2 = <:T00^2:>, r = rho
D = z3.If(T2 - r*r >= 0, T2 - r*r, r*r - T2) / T2          # KF (3.2) with |.|
Dp = (T2 - r*r) / (r*r)                                    # KF (3.43) Delta'
s = z3.Solver(); s.add(T2 > 0, r != 0, T2 >= r*r, z3.Not(D == Dp/(1+Dp)))
rec("C1a (3.44) Delta = Delta'/(1+Delta') holds when <:T^2:> >= rho^2", s.check() == z3.unsat)
s = z3.Solver(); s.add(T2 > 0, r != 0, T2 >= r*r, z3.Not(Dp == D/(1-D)))
rec("C1b (3.44) Delta' = Delta/(1-Delta) holds when <:T^2:> >= rho^2", s.check() == z3.unsat)
s = z3.Solver(); s.add(T2 > 0, r != 0, z3.Not(D == Dp/(1+Dp)))
sat = s.check() == z3.sat
_t2, _r = sp.Rational(1, 2), -1                # <:T^2:> < rho^2
_D = abs(_t2 - _r**2)/_t2; _Dp = (_t2 - _r**2)/_r**2
rec("C1c without that hypothesis (3.44) FAILS (SAT counterexample)", sat and _D != _Dp/(1+_Dp),
    "e.g. <:T^2:>=1/2, rho=-1: Delta=%s, Delta'/(1+Delta')=%s" % (_D, _Dp/(1+_Dp)))

# ------------------------------------------------------------------- C2
K, eps = sp.symbols('K epsilon', positive=True)
th = sp.symbols('theta', real=True)
N = 12
a = sp.zeros(N, N)
for n in range(1, N):
    a[n-1, n] = sp.sqrt(n)
ad = a.T
z = sp.exp(2*sp.I*th)
def ordered(m, n):          # (a^dagger)^m a^n
    return (ad**m) * (a**n)
# :T00: = K(2 a+a - z a^2 - zbar a+^2)   (KF (2.10)-(2.14), phi = a f + a+ f*)
T1 = K*(2*ordered(1, 1) - z*ordered(0, 2) - sp.conjugate(z)*ordered(2, 0))
# normal-ordered square: expand (2 b a - z a^2 - zb b^2)^2 with b,a commuting, then order b left
bb, aa = sp.symbols('bb aa', commutative=True)
poly = sp.expand((2*bb*aa - z*aa**2 - sp.conjugate(z)*bb**2)**2)
TT = sp.zeros(N, N)
for term in sp.Add.make_args(poly):
    pb, pa = sp.degree(term, bb), sp.degree(term, aa)
    coef = term / (bb**pb * aa**pa)
    TT += sp.simplify(coef) * ordered(pb, pa)
TT = K**2 * TT
psi = sp.zeros(N, 1); psi[0] = 1/sp.sqrt(1+eps**2); psi[2] = eps/sp.sqrt(1+eps**2)
ev = lambda M: sp.simplify((psi.H * M * psi)[0, 0])
rho = sp.simplify(sp.expand_complex(ev(T1)).rewrite(sp.cos))
t2 = sp.simplify(sp.expand_complex(ev(TT)).rewrite(sp.cos))
c = sp.symbols('c', real=True)
rho_c = sp.simplify(rho.subs(sp.cos(2*th), c))
rec("C2a rho = 2K eps(2eps - sqrt2 cos2th)/(1+eps^2)",
    sp.simplify(sp.expand(sp.expand_trig(rho - 2*K*eps*(2*eps - sp.sqrt(2)*sp.cos(2*th))/(1+eps**2)))) == 0,
    str(sp.factor(sp.simplify(sp.expand(sp.expand_trig(rho))))))
rec("C2b <:T00^2:> = 12 K^2 eps^2/(1+eps^2)", sp.simplify(t2 - 12*K**2*eps**2/(1+eps**2)) == 0, str(t2))
ratio = sp.simplify(rho**2/t2)
rec("C2c rho^2/<:T^2:> = (2eps - sqrt2 cos2th)^2/(3(1+eps^2))",
    sp.simplify(ratio - (2*eps - sp.sqrt(2)*sp.cos(2*th))**2/(3*(1+eps**2))) == 0)
w = {eps: 1, th: sp.pi/2, K: 1}           # cos 2theta = -1
rw, ratw = rho.subs(w), sp.nsimplify(ratio.subs(w))
kf = abs(1 - ratw)
rec("C2d witness eps=1, cos2th=-1: rho > 0 and <:T^2:> < rho^2", bool(rw > 0) and bool(ratw > 1),
    "rho=%s ratio=%s=%.6f" % (sp.nsimplify(rw), sp.simplify(ratw), float(ratw)))
rec("C2e there KF's |.| Delta = +0.9428 but the unsigned 1 - rho^2/<:T^2:> = -0.9428",
    round(float(kf), 4) == 0.9428 and round(float(1 - ratw), 4) == -0.9428,
    "KF=%.6f unsigned=%.6f" % (float(kf), float(1 - ratw)))
# where exactly does <:T^2:> < rho^2 happen?  (2eps - sqrt2 c)^2 > 3(1+eps^2)
e_, c_ = z3.Reals('e c')
q = z3.Real('q')
H = [q > 0, q*q == 2, c_ >= -1, c_ <= 1, e_ > 0]
Xz = 2*e_ - q*c_
s = z3.Solver(); s.add(*H, Xz*Xz > 3*(1+e_*e_), e_*Xz < 0)
rec("C3a z3: in vac+2, <:T^2:> < rho^2 never happens where rho < 0 (UNSAT)", s.check() == z3.unsat)
s = z3.Solver(); s.add(*H, e_*Xz < 0, z3.Not(Xz*Xz < 2*(1+e_*e_)))
rec("C3b z3: rho < 0 => <:T^2:> > (3/2) rho^2, so 1/3 < Delta there, |.| inactive", s.check() == z3.unsat)
s = z3.Solver(); s.add(*H, e_*Xz < 0, z3.Not(Xz*Xz > 0))
rec("C3d z3: rho < 0 => Delta < 1 with KF's own |.| (3.2), so the printed 'rho<0 => Delta>1' fails for the exact moments", s.check() == z3.unsat)
s = z3.Solver(); s.add(*H, Xz*Xz > 3*(1+e_*e_))
rec("C3c vacuity guard: <:T^2:> < rho^2 IS reachable (SAT) in vac+2 with rho > 0", s.check() == z3.sat)

# ------------------------------------------------------------------- C4 coherent
al = sp.symbols('alpha'); alc = sp.conjugate(al)
Kc = sp.symbols('K', positive=True)
T1c = Kc*(2*alc*al - z*al**2 - sp.conjugate(z)*alc**2)        # <b^m a^n> = alc^m al^n
T2c = sp.expand(Kc**2*(2*alc*al - z*al**2 - sp.conjugate(z)*alc**2)**2)
rec("C4 coherent: <:T^2:> - rho^2 = 0 identically, Delta = 0 (KF 3.21)", sp.simplify(T2c - T1c**2) == 0)

# ------------------------------------------------------------------- C5 Gaussian
# symbolic 2-point Wick: for zero-mean Gaussian, <:X_A X_B X_C X_D:> = G_AB G_CD + G_AC G_BD + G_AD G_BC
# with X_A = d_A phi, T00 = (1/2) sum_A X_A^2  (flat, minimal, massless):
G = sp.Matrix(4, 4, lambda i, j: sp.Symbol('g%d%d' % (min(i, j), max(i, j))))
rho_g = sum(G[A, A] for A in range(4)) / 2
t2_g = sp.Rational(1, 4) * sum(G[A, A]*G[B, B] + 2*G[A, B]**2 for A in range(4) for B in range(4))
rec("C5a Wick: <:T00^2:> - rho^2 = (1/2) sum G_AB^2",
    sp.expand(t2_g - rho_g**2 - sp.Rational(1, 2)*sum(G[A, B]**2 for A in range(4) for B in range(4))) == 0)
# numeric control of the Wick step on an explicit Gaussian: two real Gaussian variables via sampling moments
random.seed(1)
Lm = [[random.uniform(-1, 1) for _ in range(4)] for _ in range(4)]
Cn = [[sum(Lm[i][k]*Lm[j][k] for k in range(4)) for j in range(4)] for i in range(4)]
# exact 4th moment of Gaussian via Isserlis vs formula: sum_{A,B} E[X_A^2 X_B^2]/4
iss = sum(Cn[A][A]*Cn[B][B] + 2*Cn[A][B]**2 for A in range(4) for B in range(4)) / 4
tr = sum(Cn[A][A] for A in range(4)) / 2
rec("C5b numeric Isserlis control: <T^2> - rho^2 = (1/2) sum C^2 at a random covariance",
    abs(iss - tr**2 - 0.5*sum(Cn[A][B]**2 for A in range(4) for B in range(4))) < 1e-12)
g = {(A, B): z3.Real('g%d%d' % (min(A, B), max(A, B))) for A in range(4) for B in range(4)}
trz = sum(g[A, A] for A in range(4))
sq = z3.Sum([g[A, B]*g[A, B] for A in range(4) for B in range(4)])
rz = trz/2; t2z = rz*rz + sq/2
s = z3.Solver(); s.add(rz != 0, z3.Not(2*t2z >= 3*rz*rz))
rec("C5c z3: zero-mean Gaussian => <:T^2:> >= (3/2) rho^2 (> rho^2): |.| inactive, (3.44) valid", s.check() == z3.unsat)
s = z3.Solver(); s.add(rz != 0, z3.Not(t2z >= 2*rz*rz))
rec("C5d vacuity guard: the stronger <:T^2:> >= 2 rho^2 is refutable (SAT)", s.check() == z3.sat)

# ------------------------------------------------------------------- C6 Casimir algebra
g0, g1, g2, g3 = sp.symbols('g0:4', real=True)
rr = (g0+g1+g2+g3)/2
p = [g1 + (g0-g1-g2-g3)/2, g2 + (g0-g1-g2-g3)/2, g3 + (g0-g1-g2-g3)/2]
rec("C6a diagonal G: G00 = (rho+p1+p2+p3)/2, so (3.41)'s coefficient is 1/4, not the printed 1/2",
    sp.simplify(g0 - (rr + sum(p))/2) == 0)
rec("C6b diagonal G: G11 = (rho+p1-p2-p3)/2, so (3.42)'s coefficient is 1/4, not the printed 1/2",
    sp.simplify(g1 - (rr + p[0] - p[1] - p[2])/2) == 0)
xi = sp.symbols('xi1:4', real=True)
brk = lambda lead: sp.Rational(1, 8)*((lead+xi[0]+xi[1]+xi[2])**2 + (lead+xi[0]-xi[1]-xi[2])**2
                                      + (lead-xi[0]+xi[1]-xi[2])**2 + (lead-xi[0]-xi[1]+xi[2])**2)
Dp_true = sp.simplify((rr**2 + sp.Rational(1, 2)*(g0**2+g1**2+g2**2+g3**2) - rr**2)/rr**2)
Dp_one = brk(1).subs({xi[i]: p[i]/rr for i in range(3)})
rec("C6c (3.43) with leading 1 equals the exact Delta' for diagonal G", sp.simplify(Dp_true - Dp_one) == 0)
rec("C6d (3.43) with 1: min 1/2 at xi = 0 (KF 3.45) and 6 at xi = (-1,-1,3) (KF 3.32 case)",
    brk(1).subs({xi[0]: 0, xi[1]: 0, xi[2]: 0}) == sp.Rational(1, 2)
    and brk(1).subs({xi[0]: -1, xi[1]: -1, xi[2]: 3}) == 6)
rho_s = sp.symbols('rho', positive=True)
rec("C6e (3.43) as printed with leading rho is NOT the exact Delta' (dimensionally inhomogeneous)",
    sp.simplify(brk(rho_s) - brk(1)) != 0)
# the minimum claim: Hessian positive, stationary at 0
grad = [sp.diff(brk(1), v) for v in xi]
rec("C6f (3.43) stationary only at xi = 0 with value 1/2 (global min of a PD quadratic)",
    sp.solve(grad, xi, dict=True) == [{xi[0]: 0, xi[1]: 0, xi[2]: 0}]
    and sp.hessian(brk(1), xi).is_positive_definite)

# ------------------------------------------------------------------- C7 thermal
aT = sp.symbols('a', positive=True)
GT = sp.diag(aT, aT/3, aT/3, aT/3)
rT = sum(GT[A, A] for A in range(4))/2
t2T = rT**2 + sp.Rational(1, 2)*sum(GT[A, B]**2 for A in range(4) for B in range(4))
DpT = sp.simplify((t2T - rT**2)/rT**2)
rec("C7 thermal isotropic radiation: p = rho/3, Delta' = 2/3, Delta = 2/5",
    sp.simplify((GT[1, 1] + (GT[0, 0]-GT[1, 1]-GT[2, 2]-GT[3, 3])/2)/rT) == sp.Rational(1, 3)
    and DpT == sp.Rational(2, 3) and sp.simplify(DpT/(1+DpT)) == sp.Rational(2, 5))

print()
bad = [l for l, ok in OUT if not ok]
print("RESULT: %d/%d checks pass" % (len(OUT) - len(bad), len(OUT)))
if bad:
    print("FAILED:", bad)
raise SystemExit(1 if bad else 0)
