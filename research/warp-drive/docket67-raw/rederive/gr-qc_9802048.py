#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation / machine checks for Hochberg & Visser, gr-qc/9802048
(PRL 81, 746, 1998), 'The null energy condition in dynamic wormholes'.

C1  Results (1)-(2) in spherical symmetry, from scratch: in the general double-null
    metric ds^2 = -2 e^{-f} dxm dxp + r^2 dOmega^2 the Einstein tensor gives, on
    theta_+ = 0, d theta_+ / d xi_+ = -G_{++}.  So null flare-out (>=0) <=> G_{++} <= 0
    <=> T_{++} <= 0 (Einstein eqs).  Also computed: theta_- need not vanish where
    theta_+ does (two throats), coalescing when static.
C2  Letter eq.(7)-(8), non-symmetric: Raychaudhuri with theta = 0, omega = 0,
    sigma^2 >= 0, dtheta/du >= 0  =>  R_ll <= 0.  z3, over the reals.
C3  [11] eq.(53) (the 'transverse averaged NEC' of result (4), as defined in the
    companion gr-qc/9802046 def. 4.1.3): averaged flare-out
    sum w_i sgn(theta'_i) > 0 with T_i = -(theta'_i + sigma2_i), sigma2_i >= 0,
    implies sum w_i sgn(T_i) < 0.  z3, n = 6 points (a finite box, as all z3 claims here).
C4  Second area variation: d^2/deps^2 sqrt(gamma)(x, eps f) = f^2 (theta' + theta^2) sqrt(gamma)
    -- the theta^2 term that the Letter's step (10) -> (11) omits off the throat.
    Plus a two-generator toy where A'' > 0 but int f^2 sqrt(g) theta' < 0 at the same eps
    (the toy violates the Letter's eq.(3) per-generator minimum, so it is NOT a
    counterexample to the theorem -- it shows eq.(3), not (9)/(10), must carry the step).
C5  The Letter's parenthetical '(in general (-delta2,0) U (0,+delta2))' after eq.(10):
    a C-infinity A(eps) = exp(-1/|eps|)(2 + sin(1/eps^2)) with A(eps) > A(0) for eps != 0
    whose A'' takes both signs in every (0, delta).  The open set {A'' > 0} accumulates
    at 0 (which is all the argument needs) but is not a punctured interval.
C6  NEC violated => some timelike observer measures negative energy density
    (the tree's 'negative energy' wording): T(l,l) < 0 => T(u,u) < 0 for u = l + eps m.
C7  Later literature, the reach of the 'suspension is an illusion' step: the
    Maeda-Harada-Carr (0901.1153) cosmological Ellis wormhole
    ds^2 = -dt^2 + (t/t0)^2 [dx^2 + (x^2+b^2) dOmega^2]: Einstein tensor computed here;
    NEC (both radial null directions and tangential) holds everywhere for t0 <= b,
    and no sphere has theta_+ = 0 or theta_- = 0 for t0 < 2b (trapped everywhere), so
    there is no Hochberg-Visser throat -- consistent with H&V's theorem and outside it.
"""
import sympy as sp
import z3

ok = {}

# ---------------- C1
xm, xp, th, ph = sp.symbols('xm xp th ph')
f = sp.Function('f')(xm, xp)
r = sp.Function('r')(xm, xp)
X = [xm, xp, th, ph]
g = sp.zeros(4)
g[0, 1] = g[1, 0] = -sp.exp(-f)
g[2, 2] = r**2
g[3, 3] = r**2 * sp.sin(th)**2
gi = g.inv()
def christoffel(g, gi, X):
    n = len(X)
    return [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                              for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
def ricci(g, gi, X):
    n = len(X); G = christoffel(g, gi, X)
    R = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            R[b, c] = sp.simplify(sum(sp.diff(G[a][b][c], X[a]) - sp.diff(G[a][b][a], X[c])
                                      + sum(G[a][a][d]*G[d][b][c] - G[a][c][d]*G[d][b][a] for d in range(n))
                                      for a in range(n)))
    return R
Ric = ricci(g, gi, X)
Rs = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(4) for b in range(4)))
Gpp = sp.simplify(Ric[1, 1] - Rs*g[1, 1]/2)        # g_{++} = 0 so G_{++} = R_{++}
target = -(2/r)*(sp.diff(r, xp, 2) + sp.diff(f, xp)*sp.diff(r, xp))
c1a = sp.simplify(Gpp - target) == 0
theta_p = 2*sp.diff(r, xp)/r
dtheta = sp.diff(theta_p, xp)
# on theta_+ = 0 (r_{,+} = 0):
rp = sp.Symbol('rp')
sub = {sp.Derivative(r, xp): 0}
c1b = sp.simplify((dtheta + Gpp).subs(sub)) == 0
ok['C1 G_{++} = -(2/r)(r_++ + f_+ r_+) and, on theta_+=0, dtheta_+/dxi_+ = -G_{++}'] = c1a and c1b

# two throats: FRW-conformal Morris-Thorne-type example where theta_+ = 0 and theta_- != 0
# (H&V companion sec.6 metric): ds^2 = Om(t)^2(-dt^2 + dl^2 + (l^2+b0^2) dOmega^2); radial
# null expansions  theta_pm ~ (d/dt +- d/dl) ln[Om^2 (l^2+b0^2)].
t = sp.Symbol('t', positive=True); l = sp.Symbol('l', real=True); b0 = sp.Rational(1, 2)
Om = sp.exp(t/3)                                    # an expanding conformal factor, illustrative
lnA = sp.log(Om**2*(l**2 + b0**2))
thp = sp.diff(lnA, t) + sp.diff(lnA, l)
thm = sp.diff(lnA, t) - sp.diff(lnA, l)
lp = sp.solve(sp.Eq(thp, 0), l)
lm = sp.solve(sp.Eq(thm, 0), l)
ok['C1b dynamic example: theta_+=0 and theta_-=0 on different spheres (two throats); static limit coalesces at l=0'] = (
    len(lp) > 0 and len(lm) > 0 and set(lp).isdisjoint(set(lm)) and 0 not in lp and 0 not in lm and
    sp.solve(sp.Eq(sp.diff(sp.log(l**2+b0**2), l), 0), l) == [0])
print('C1 throat_+ at l =', lp, ' throat_- at l =', lm)

# ---------------- C2
dth, sig2, Rll = z3.Reals('dth sig2 Rll')
s = z3.Solver()
# Raychaudhuri at theta=0, omega=0: dth = -sig2 - Rll
s.add(dth == -sig2 - Rll, sig2 >= 0, dth >= 0, Rll > 0)
ok['C2 z3: theta=0, omega=0, sigma^2>=0, dtheta/du>=0 => R_ll<=0 (negation UNSAT)'] = (s.check() == z3.unsat)
s = z3.Solver(); s.add(dth == -sig2 - Rll, sig2 >= 0, dth > 0, Rll >= 0)
ok['C2b z3: strict flare-out dtheta/du>0 => R_ll<0 (negation UNSAT)'] = (s.check() == z3.unsat)
s = z3.Solver(); s.add(dth == -sig2 - Rll, sig2 >= 0, dth >= 0, Rll == 0)
ok['C2c vacuity guard: equality R_ll=0 is reachable (NEC on the verge), SAT'] = (s.check() == z3.sat)

# ---------------- C3
n = 6
w = z3.Reals(' '.join(f'w{i}' for i in range(n)))
d = z3.Reals(' '.join(f'd{i}' for i in range(n)))
q = z3.Reals(' '.join(f'q{i}' for i in range(n)))
sgn = lambda x: z3.If(x > 0, 1, z3.If(x < 0, -1, 0))
s = z3.Solver()
for i in range(n):
    s.add(w[i] > 0, q[i] >= 0)
s.add(z3.Sum([w[i]*sgn(d[i]) for i in range(n)]) > 0)
s.add(z3.Sum([w[i]*sgn(-(d[i] + q[i])) for i in range(n)]) >= 0)
ok['C3 z3 (n=6): averaged flare-out => sgn-averaged NEC strictly violated ([11] eq.53) (negation UNSAT)'] = (s.check() == z3.unsat)
s = z3.Solver()
for i in range(n):
    s.add(w[i] > 0, q[i] >= 0)
s.add(z3.Sum([w[i]*sgn(d[i]) for i in range(n)]) > 0)
ok['C3b vacuity guard: averaged flare-out is satisfiable, SAT'] = (s.check() == z3.sat)
# and the WEIGHTED (non-sgn) average the Letter's eq.(11) uses is NOT reparametrisation invariant:
# [11] p.15 says rescaling the affine parameter per generator (u -> c(x) u, theta' -> theta'/c^2)
# can drive int sqrt(g) theta' to either sign when theta' changes sign.  Check on 2 generators:
c1, c2 = sp.symbols('c1 c2', positive=True)
I = 1*sp.Rational(1)/c1**2 + 1*sp.Rational(-1)/c2**2      # theta'=+1 on one, -1 on the other
ok['C3c int sqrt(g) theta\' takes both signs under per-generator affine rescaling ([11] p.15)'] = (
    I.subs({c1: 1, c2: 2}) > 0 and I.subs({c1: 2, c2: 1}) < 0)

# ---------------- C4
u, x, eps = sp.symbols('u x eps', real=True)
F = sp.Function('F')(x)
a = sp.Function('a')(x, u)                          # sqrt(gamma) along the generator at x
theta = sp.diff(sp.log(a), u)
expr = sp.diff(a.subs(u, eps*F), eps, 2)
claim = (F**2*(sp.diff(theta, u) + theta**2)*a).subs(u, eps*F)
ok['C4 d^2/deps^2 sqrt(g)(x, eps f) = f^2 (theta\' + theta^2) sqrt(g)  [theta^2 term present]'] = (
    sp.simplify(sp.expand(expr.doit() - claim.doit())) == 0)
cc = sp.Rational(1, 10)
a1 = 1 + u**3
a2 = 1 - u**3 + cc*u**6
A = a1 + a2
S = sum(ai*sp.diff(sp.diff(sp.log(ai), u), u) for ai in (a1, a2))   # int f^2 sqrt(g) theta', f = 1
vals = [(float(sp.diff(A, u, 2).subs(u, uu)), float(S.subs(u, uu))) for uu in (0.05, 0.1, 0.2, -0.1)]
print('C4 toy (A\'\', int sqrt(g) theta\') at u=0.05,0.1,0.2,-0.1:', vals)
ok['C4b toy: A\'\'>0 while int sqrt(g) theta\' < 0 at the same eps (so (10) alone does not give (11))'] = all(
    Ap > 0 and Sv < 0 for Ap, Sv in vals)
ok['C4c the toy violates the Letter\'s eq.(3): generator 2 area a2(u)<a2(0) for small u>0 (not a throat)'] = (
    float(a2.subs(u, 0.1)) < 1.0)

# ---------------- C5
e = sp.Symbol('e', positive=True)
Ae = sp.exp(-1/e)*(2 + sp.sin(1/e**2))
App = sp.lambdify(e, sp.diff(Ae, e, 2), 'mpmath')
import mpmath as mp
mp.mp.dps = 50
signs_ok = True
for k in (10, 100, 1000, 10000):
    ep = 1/mp.sqrt(2*mp.pi*k + mp.pi/2)   # sin(1/e^2) = +1  ... A'' dominated by -4/e^6 sin
    em = 1/mp.sqrt(2*mp.pi*k + 3*mp.pi/2) # sin(1/e^2) = -1
    vp, vm = App(ep), App(em)
    signs_ok &= (vp < 0 and vm > 0)
    if k == 10000:
        print('C5 at k=1e4: eps=%.3e A\'\'=%.3e ; eps=%.3e A\'\'=%.3e' % (float(ep), float(vp), float(em), float(vm)))
ok['C5 C-infinity A>A(0) for eps!=0 with A\'\' of both signs arbitrarily near 0: the set {A\'\'>0} is not a punctured interval'] = signs_ok

# ---------------- C6
Tll, Tlm, Tmm, ee = sp.symbols('Tll Tlm Tmm ee', real=True)
Tuu = Tll + 2*ee*Tlm + ee**2*Tmm
# for any Tll<0 there is ee>0 with Tuu<0 and u = l + ee m timelike (m future unit timelike, l future null)
vals6 = [(TLL, TLM, TMM) for TLL in (-1e-3, -1.0) for TLM in (-50.0, 0.0, 50.0) for TMM in (-5.0, 5.0, 500.0)]
def small_eps_ok(TLL, TLM, TMM):
    for k in range(1, 60):
        E = 2.0**-k
        if TLL + 2*E*TLM + E*E*TMM < 0:
            return True
    return False
ok['C6 T(l,l)<0 => T(u,u)<0 for u = l + eps m timelike, some eps>0 (NEC-violation => WEC-violation), grid'] = all(
    small_eps_ok(*v) for v in vals6)

# ---------------- C7
T_, x_, t0, bb = sp.symbols('t x t0 b', positive=True)
th2, ph2 = sp.symbols('th2 ph2')
X2 = [T_, x_, th2, ph2]
aa = T_/t0
g2 = sp.diag(-1, aa**2, aa**2*(x_**2 + bb**2), aa**2*(x_**2 + bb**2)*sp.sin(th2)**2)
g2i = g2.inv()
Ric2 = ricci(g2, g2i, X2)
R2 = sp.simplify(sum(g2i[i, j]*Ric2[i, j] for i in range(4) for j in range(4)))
G2 = sp.simplify(Ric2 - R2*g2/2)
Gmix = sp.simplify(g2i*G2)                            # G^a_b
mu = sp.simplify(-Gmix[0, 0]); pr = sp.simplify(Gmix[1, 1]); pt = sp.simplify(Gmix[2, 2])
mu_ref = 3/T_**2 - t0**2*bb**2/(T_**2*(x_**2 + bb**2)**2)
pr_ref = -1/T_**2 - t0**2*bb**2/(T_**2*(x_**2 + bb**2)**2)
pt_ref = -1/T_**2 + t0**2*bb**2/(T_**2*(x_**2 + bb**2)**2)
ok['C7a MHC eqs (4.58)-(4.60) reproduced from the metric (8piG mu, p_r, p_t)'] = all(
    sp.simplify(A1 - B1) == 0 for A1, B1 in ((mu, mu_ref), (pr, pr_ref), (pt, pt_ref)))
nec_r = sp.simplify(mu + pr)       # radial null NEC
nec_t = sp.simplify(mu + pt)
# with t0 <= b: nec_r = 2/t^2 (1 - t0^2 b^2/(x^2+b^2)^2) >= 0 since (x^2+b^2) >= b^2 >= t0 b
chk = sp.simplify(nec_r - 2/T_**2*(1 - t0**2*bb**2/(x_**2 + bb**2)**2)) == 0
num_ok = True
import random
random.seed(67)
for _ in range(2000):
    bv = random.uniform(0.1, 10); t0v = random.uniform(0.01, 1.0)*bv
    xv = random.uniform(-50, 50); tv = random.uniform(0.01, 100)
    sb = {T_: tv, x_: abs(xv), t0: t0v, bb: bv}
    num_ok &= float(nec_r.subs(sb)) >= -1e-12 and float(nec_t.subs(sb)) >= -1e-12
# null expansions of the round spheres: area radius R = a sqrt(x^2+b^2), theta_pm ~ (d_t +- a^{-1} d_x) ln R
Rar = aa*sp.sqrt(x_**2 + bb**2)
thpm = [sp.simplify(sp.diff(sp.log(Rar), T_) + sgn_*sp.diff(sp.log(Rar), x_)/aa) for sgn_ in (1, -1)]
# theta_+ theta_- > 0 everywhere iff trapped; product numerator:
prod = sp.simplify(thpm[0]*thpm[1]*T_**2)
trapped_ok = True
for _ in range(2000):
    bv = random.uniform(0.1, 10); t0v = random.uniform(0.01, 1.999)*bv
    xv = random.uniform(-50, 50); tv = random.uniform(0.01, 100)
    trapped_ok &= float(prod.subs({T_: tv, x_: abs(xv), t0: t0v, bb: bv})) > 0
print('C7 theta_+ theta_- * t^2 =', prod)
ok['C7b MHC cosmological Ellis wormhole: NEC (radial and tangential) holds everywhere for t0<=b (identity + 2000 samples)'] = chk and num_ok
ok['C7c ... and theta_+ theta_- > 0 everywhere for t0<2b: no theta_pm = 0 sphere, hence no H&V throat (2000 samples)'] = trapped_ok

print()
for k, v in ok.items():
    print(('PASS ' if v else 'FAIL ') + k)
print('\nALL PASS' if all(ok.values()) else '\nSOME FAIL')
raise SystemExit(0 if all(ok.values()) else 1)
