#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of Fewster & Osterbrink, arXiv:0708.2450, Theorem 4.2
(state-dependent difference QEI, non-minimally coupled scalar, timelike geodesic).

What is finite / closed form here, and is checked:
  A. FO (7) <=> FO (8): the rewriting of the classical NMC stress tensor (BD
     conventions, signature +---), as an algebraic identity at a point in an
     orthonormal frame, n = 3, 4, 5.
  B. FO (8) contracted with the geodesic tangent = FO (9) = coincidence of
     rho1 - xi rho2 + xi rho3 (FO (10)-(14)).
  C. The smearing step (FO 36-43, classical content): along a geodesic,
       int f^2 rho = int [ 1/2 f^2 phi'^2 + 1/2 (1-4xi) f^2 (m^2 phi^2 + S)
                           + 2 xi (f phi' + f' phi)^2 ]
                     - xi int Q_B[f] phi^2 - xi int Q_C[f] phi^2      (on shell)
     with Q_B = 2 f'^2 (FO 47), Q_C = f^2 (R_uu - 1/2 (1-4xi) R) (FO 48):
     the integrand difference is an exact derivative.
  D. z3: the discarded bracket is >= 0 for every field iff xi in [0, 1/4]
     (sufficiency proved; for xi outside, a negative instance is found).
  E. Independent curved-space check in MTW conventions (-+++): explicit
     metric -dt^2 + a^2 dx^2 + b^2 dy^2 + c^2 dz^2, a,b,c functions of (t,x)
     (t-lines are geodesics); T_tt from the MTW NMC stress tensor equals the
     decomposition in C with Q_C^MTW = -f^2 (R_tt + 1/2 (1-4xi) R), up to a
     multiple of the field equation -- i.e. FO (48) after R_uv(BD) = -R_uv(MTW),
     R(BD) = R(MTW).
  F. FO Theorem 4.3 (Minkowski): Qt_A (53) for n = 4, m = 0 reduces to
     (1/4 - xi/3) * S_2/(2pi)^4 int_0^oo u^4 |fhat(u)|^2 du, agreeing with (55)
     (Q_{n,k} -> 1); at xi = 0 it equals the Fewster-Eveson bound
     (1/16 pi^2) int f''^2 (numerically, Gaussian f); non-negative on [0,1/4].
  G. Range is not an artefact (a computed extension, not in FO): for xi > 1/4,
     any smooth solution odd in x has phi = 0 on the worldline x = 0 and
     rho_class = 1/2 (1-4xi) (d_x phi)^2 < 0 there, so for coherent states
     (A * phi) the left side of (44) scales as -A^2 while the Phi^2 terms vanish
     on gamma: no bound of form (44)-(45) with a state-independent Qt_A holds.
  H. The tree's use on HPS: the static worldline of -f(l) dt^2 + dl^2 + r(l)^2 dOmega^2
     is a geodesic iff f'(l0) = 0 (HPS data (9): f'(0) = 0) -> MET;
     xi = 1/6 in [0, 1/4] -> MET; the vacuity instance omega_0 = psi gives
     0 >= -Qt_A; supplementary: Q_C at the HPS throat (f' = f'' = r' = r'' = 0)
     = -f^2 (1-4xi)/r0^2 = -f^2/(3 r0^2) at xi = 1/6 (nonzero: not Ricci-flat).
Exit 0 iff every check passes.
"""
import sys
import sympy as sp
import z3

PASS, FAIL = [], []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(("PASS " if ok else "FAIL ") + name + ((" -- " + detail) if detail else ""))


xi, m = sp.symbols('xi m', real=True)

# ---------------------------------------------------------------- A, B
for n in (3, 4, 5):
    eta = sp.diag(*([1] + [-1] * (n - 1)))          # BD signature +---
    phi = sp.Symbol('phi')
    p = sp.symbols('p0:%d' % n)                      # nabla_mu phi (frame)
    H = sp.Matrix(n, n, lambda i, j: sp.Symbol('H%d%d' % (min(i, j), max(i, j))))
    Ric = sp.Matrix(n, n, lambda i, j: sp.Symbol('R%d%d' % (min(i, j), max(i, j))))
    etainv = eta.inv()
    R = sum(etainv[i, j] * Ric[i, j] for i in range(n) for j in range(n))
    box = sum(etainv[i, j] * H[i, j] for i in range(n) for j in range(n))
    dphi2 = sum(etainv[i, j] * p[i] * p[j] for i in range(n) for j in range(n))
    G = Ric - sp.Rational(1, 2) * eta * R
    P = box + (m**2 + xi * R) * phi                  # P_xi phi  (FO (5))
    ok7_8 = True
    for i in range(n):
        for j in range(n):
            # nabla nabla phi^2 = 2 p p + 2 phi H ; box phi^2 = 2 dphi2 + 2 phi box
            dd_phi2 = 2 * p[i] * p[j] + 2 * phi * H[i, j]
            box_phi2 = 2 * dphi2 + 2 * phi * box
            T7 = (p[i] * p[j] + sp.Rational(1, 2) * eta[i, j] * (m**2 * phi**2 - dphi2)
                  + xi * (eta[i, j] * box_phi2 - dd_phi2 - G[i, j] * phi**2))
            T8 = ((1 - 2 * xi) * p[i] * p[j]
                  + sp.Rational(1, 2) * (1 - 4 * xi) * eta[i, j] * (m**2 * phi**2 - dphi2)
                  - 2 * xi * (phi * H[i, j] + sp.Rational(1, 2) * Ric[i, j] * phi**2
                              - sp.Rational(1, 4) * (1 - 4 * xi) * eta[i, j] * R * phi**2
                              - eta[i, j] * phi * P))
            if sp.expand(T7 - T8) != 0:
                ok7_8 = False
    check("A: FO (7) == FO (8) identically, n=%d" % n, ok7_8)
    # B: rho = T_00 (u = e_0, geodesic so nabla_u nabla_u phi = H00 = phi'')
    T00 = ((1 - 2 * xi) * p[0]**2 + sp.Rational(1, 2) * (1 - 4 * xi) * (m**2 * phi**2 - dphi2)
           - 2 * xi * (phi * H[0, 0] + sp.Rational(1, 2) * Ric[0, 0] * phi**2
                       - sp.Rational(1, 4) * (1 - 4 * xi) * R * phi**2 - phi * P))
    S = sum(p[i]**2 for i in range(1, n))
    rho1 = sp.Rational(1, 2) * p[0]**2 + sp.Rational(1, 2) * (1 - 4 * xi) * (m**2 * phi**2 + S)
    rho2 = 2 * phi * H[0, 0]
    rho3 = -Ric[0, 0] * phi**2 + sp.Rational(1, 2) * (1 - 4 * xi) * R * phi**2 + 2 * phi * P
    check("B: FO (9) == [rho1 - xi rho2 + xi rho3]_c (FO 10-14), n=%d" % n,
          sp.expand(T00 - (rho1 - xi * rho2 + xi * rho3)) == 0)

# ---------------------------------------------------------------- C
tau = sp.Symbol('tau', real=True)
F = sp.Function('f')(tau)
ph = sp.Function('phi')(tau)
Sg, Ruu, Rs = sp.Function('S')(tau), sp.Function('Ruu')(tau), sp.Function('R')(tau)
rho_onshell = (sp.Rational(1, 2) * ph.diff(tau)**2
               + sp.Rational(1, 2) * (1 - 4 * xi) * (m**2 * ph**2 + Sg)
               - 2 * xi * ph * ph.diff(tau, 2)
               - xi * (Ruu - sp.Rational(1, 2) * (1 - 4 * xi) * Rs) * ph**2)
QB = 2 * F.diff(tau)**2
QC = F**2 * (Ruu - sp.Rational(1, 2) * (1 - 4 * xi) * Rs)
discarded = (sp.Rational(1, 2) * F**2 * ph.diff(tau)**2
             + sp.Rational(1, 2) * (1 - 4 * xi) * F**2 * (m**2 * ph**2 + Sg)
             + 2 * xi * (F * ph.diff(tau) + F.diff(tau) * ph)**2)
diff = sp.expand(F**2 * rho_onshell - (discarded - xi * QB * ph**2 - xi * QC * ph**2))
boundary = -2 * xi * F**2 * ph * ph.diff(tau)
check("C: f^2 rho - [discarded - xi Q_B phi^2 - xi Q_C phi^2] = d/dtau(-2 xi f^2 phi phi')",
      sp.simplify(diff - sp.expand(boundary.diff(tau))) == 0,
      "Q_B = 2 f'^2 (FO 47), Q_C = f^2 (R_uu - (1-4xi)R/2) (FO 48) recovered")

# ---------------------------------------------------------------- D
X, a, b, c, Sv = z3.Reals('xi a b c S')
Dq = 0.5 * a * a + 0.5 * (1 - 4 * X) * Sv + 2 * X * c * c   # Sv = m^2 phi^2 + S >= 0
s = z3.Solver()
s.add(X >= 0, X <= z3.RealVal('1/4'), Sv >= 0, Dq < 0)
check("D1: z3 -- discarded bracket >= 0 for all fields when 0 <= xi <= 1/4",
      s.check() == z3.unsat, "UNSAT of the negation")
s = z3.Solver(); s.add(X > z3.RealVal('1/4'), Sv >= 0, Dq < 0)
r1 = s.check()
s2 = z3.Solver(); s2.add(X < 0, Sv >= 0, Dq < 0)
r2 = s2.check()
check("D2: z3 -- negative instance exists for xi > 1/4 and for xi < 0 (proof step fails there)",
      r1 == z3.sat and r2 == z3.sat)

# ---------------------------------------------------------------- E  (MTW, explicit metric)
t, x, y, z = sp.symbols('t x y z', real=True)
co = [t, x, y, z]
A_ = sp.Function('A')(t, x); B_ = sp.Function('B')(t, x); C_ = sp.Function('C')(t, x)
g = sp.diag(-1, A_**2, B_**2, C_**2)
gi = g.inv()
Nd = 4
Gam = [[[sum(gi[al, be] * (g[be, mu].diff(co[nu]) + g[be, nu].diff(co[mu]) - g[mu, nu].diff(co[be]))
             for be in range(Nd)) / 2 for nu in range(Nd)] for mu in range(Nd)] for al in range(Nd)]


def riem(al, be, mu, nu):     # MTW: R^al_{be mu nu}
    r = Gam[al][be][nu].diff(co[mu]) - Gam[al][be][mu].diff(co[nu])
    r += sum(Gam[al][mu][la] * Gam[la][be][nu] - Gam[al][nu][la] * Gam[la][be][mu] for la in range(Nd))
    return r


Ric_ = sp.Matrix(Nd, Nd, lambda i, j: sp.simplify(sum(riem(k, i, k, j) for k in range(Nd))))
Rsc = sp.simplify(sum(gi[i, j] * Ric_[i, j] for i in range(Nd) for j in range(Nd)))
Gein = Ric_ - g * Rsc / 2
Phi = sp.Function('Phi')(t, x, y, z)


def cov2(fun, i, j):
    return fun.diff(co[i], co[j]) - sum(Gam[k][i][j] * fun.diff(co[k]) for k in range(Nd))


boxP = sum(gi[i, j] * cov2(Phi, i, j) for i in range(Nd) for j in range(Nd))
Phi2 = Phi**2
box2 = sum(gi[i, j] * cov2(Phi2, i, j) for i in range(Nd) for j in range(Nd))
dP2 = sum(gi[i, j] * Phi.diff(co[i]) * Phi.diff(co[j]) for i in range(Nd) for j in range(Nd))
# MTW NMC stress tensor; field equation E := box phi - m^2 phi - xi R phi = 0
Ttt = (Phi.diff(t)**2 - g[0, 0] * (dP2 + m**2 * Phi**2) / 2
       + xi * (Gein[0, 0] * Phi2 + g[0, 0] * box2 - cov2(Phi2, 0, 0)))
Efield = boxP - m**2 * Phi - xi * Rsc * Phi
Sspat = sum(gi[i, i] * Phi.diff(co[i])**2 for i in range(1, Nd))
decomp = (sp.Rational(1, 2) * Phi.diff(t)**2 + sp.Rational(1, 2) * (1 - 4 * xi) * (m**2 * Phi**2 + Sspat)
          - 2 * xi * Phi * cov2(Phi, 0, 0)
          + xi * Phi**2 * (Ric_[0, 0] + sp.Rational(1, 2) * (1 - 4 * xi) * Rsc))
rem = sp.simplify(sp.expand(Ttt - decomp))
ratio = sp.simplify(rem / (Phi * Efield))
check("E1: geodesic t-lines: Gamma^a_tt = 0", all(sp.simplify(Gam[k][0][0]) == 0 for k in range(Nd)))
check("E2: MTW T_tt = decomposition + const * phi * (field eq.)", ratio.free_symbols <= {xi},
      "const = %s; so Q_C^MTW = -f^2 (R_tt + (1-4xi)R/2) == FO (48) under R_uv(BD) = -R_uv(MTW), R(BD) = R(MTW)" % ratio)
# conformal-trace sanity of the MTW tensor: m = 0, xi = 1/6 => trace ~ field eq
Tfull = sp.Matrix(Nd, Nd, lambda i, j: Phi.diff(co[i]) * Phi.diff(co[j]) - g[i, j] * (dP2 + m**2 * Phi**2) / 2
                  + xi * (Gein[i, j] * Phi2 + g[i, j] * box2 - cov2(Phi2, i, j)))
trace = sum(gi[i, j] * Tfull[i, j] for i in range(Nd) for j in range(Nd)).subs({m: 0, xi: sp.Rational(1, 6)})
tr_ratio = sp.simplify(sp.expand(trace) / (Phi * Efield.subs({m: 0, xi: sp.Rational(1, 6)})))
check("E3: sanity -- MTW tensor traceless on shell at m = 0, xi = 1/6 (conformal)", tr_ratio.free_symbols == set(),
      "trace = %s * phi * E" % tr_ratio)

# ---------------------------------------------------------------- F  (Theorem 4.3)
u, k, al = sp.symbols('u k alpha', positive=True)
inner = sp.integrate(k * ((1 - 2 * xi) * k**2 + 2 * xi * (u - k)**2), (k, 0, u))   # n=4, m=0: k^{n-2}/omega = k
check("F1: (53) inner integral, n=4 m=0 == u^4 (1/4 - xi/3)", sp.simplify(inner - u**4 * (sp.Rational(1, 4) - xi / 3)) == 0)
n_ = 4
coef55 = sp.Rational(1, n_) - 4 * xi / (n_ - 1) + 2 * xi / (n_ - 2)                  # (55), Q_{n,k} -> 1 at m = 0
check("F2: (55) at m=0, n=4 gives the same coefficient", sp.simplify(coef55 - (sp.Rational(1, 4) - xi / 3)) == 0)
check("F3: coefficient >= 0 on [0,1/4] (value at 1/4: %s; at 1/6: %s = 7/9 of minimal)" %
      (coef55.subs(xi, sp.Rational(1, 4)), sp.Rational(1, 4) - sp.Rational(1, 18)),
      sp.solve_univariate_inequality(coef55 >= 0, xi, relational=False).contains(sp.Rational(1, 4)))
# numeric: xi = 0 equals Fewster-Eveson (1/16 pi^2) int f''^2 for Gaussian f
import math
from scipy.integrate import quad
sig = 0.7
fh = lambda w: math.sqrt(2 * math.pi) * sig * math.exp(-(w * sig)**2 / 2)           # FT of exp(-t^2/2sig^2)
S2 = 4 * math.pi
Q53 = S2 / (2 * math.pi)**4 * quad(lambda uu: uu**4 / 4 * fh(uu)**2, 0, 60)[0]
f2 = lambda tt: (tt**2 / sig**4 - 1 / sig**2) * math.exp(-tt**2 / (2 * sig**2))
FE = quad(lambda tt: f2(tt)**2, -40, 40)[0] / (16 * math.pi**2)
check("F4: Qt_A^{xi=0} (53) == (1/16pi^2) int f''^2 (FO: 'recovers [16]')", abs(Q53 / FE - 1) < 1e-9,
      "%.12g vs %.12g" % (Q53, FE))

# ---------------------------------------------------------------- G  (range necessity, extension)
r = sp.Symbol('r', positive=True)
Fg = lambda s_: sp.exp(-s_**2)
rr = sp.sqrt(x**2 + y**2 + z**2)
psi = (Fg(t + rr) - Fg(t - rr)) / rr          # smooth spherical solution of the 3+1 wave equation
phiG = sp.diff(psi, x)                          # odd in x, still a solution
wave = -phiG.diff(t, 2) + phiG.diff(x, 2) + phiG.diff(y, 2) + phiG.diff(z, 2)   # evaluated at a point below (no simplify: exact spot value)
pt = {x: sp.Rational(0), y: sp.Rational(3, 10), z: sp.Rational(-1, 5), t: sp.Rational(1, 3)}
okwave = abs(float(sp.N(wave.subs(pt), 30))) < 1e-10
check("G1: phi = d_x[(F(t+r)-F(t-r))/r] solves the massless wave equation (spot value)", okwave)
# rho_class (flat, FO (9) with R = 0, m = 0) on x = 0 worldline (y=z=0 limit via x->0 at small y,z)
def rho_flat(ph_, X_, pnt):
    d = {s_: ph_.diff(s_) for s_ in (t, x, y, z)}
    val = (sp.Rational(1, 2) * d[t]**2 + sp.Rational(1, 2) * (1 - 4 * X_) * (d[x]**2 + d[y]**2 + d[z]**2)
           - 2 * X_ * ph_ * ph_.diff(t, 2))
    return float(val.subs(pnt))
ok = True
vals = []
for tt in (0.0, 0.4, 0.9, 1.5):
    pnt = {x: 0, y: sp.Rational(1, 7), z: sp.Rational(1, 9), t: sp.nsimplify(tt)}
    ph0 = float(phiG.subs(pnt))
    dx = float(phiG.diff(x).subs(pnt))
    rr_ = rho_flat(phiG, sp.Rational(1, 3), pnt)
    vals.append(rr_)
    ok &= abs(ph0) < 1e-12 and abs(rr_ - 0.5 * (1 - 4 / 3) * dx**2) < 1e-9 * max(1, dx**2)
check("G2: on x = 0: phi = 0 and rho = (1-4xi)/2 (d_x phi)^2 (xi = 1/3 > 1/4 gives rho < 0)", ok,
      "rho samples %s; the Phi^2 terms of (45) vanish on gamma, so rho(f^2) ~ -A^2 for coherent amplitude A" %
      ["%.4g" % v for v in vals])

# ---------------------------------------------------------------- H  (HPS usage)
l, th, ph_a = sp.symbols('l theta varphi', real=True)
fl = sp.Function('f')(l); rl = sp.Function('r')(l)
co2 = [t, l, th, ph_a]
g2 = sp.diag(-fl, 1, rl**2, rl**2 * sp.sin(th)**2)
g2i = g2.inv()
Gam2 = [[[sp.simplify(sum(g2i[a_, b_] * (g2[b_, mu].diff(co2[nu]) + g2[b_, nu].diff(co2[mu]) - g2[mu, nu].diff(co2[b_]))
                           for b_ in range(4)) / 2) for nu in range(4)] for mu in range(4)] for a_ in range(4)]
# static worldline u = f^{-1/2} d_t: acceleration a^l = Gamma^l_tt / f
acc = sp.simplify(Gam2[1][0][0] / fl)
check("H1: static observer acceleration = f'/(2f); zero iff f'(0) = 0 (HPS data (9) f'(0) = 0 -> MET)",
      sp.simplify(acc - fl.diff(l) / (2 * fl)) == 0, "a = %s" % acc)


def riem2(a_, b_, mu, nu):
    r_ = Gam2[a_][b_][nu].diff(co2[mu]) - Gam2[a_][b_][mu].diff(co2[nu])
    r_ += sum(Gam2[a_][mu][la] * Gam2[la][b_][nu] - Gam2[a_][nu][la] * Gam2[la][b_][mu] for la in range(4))
    return r_


Ric2 = sp.Matrix(4, 4, lambda i, j: sp.simplify(sum(riem2(k_, i, k_, j) for k_ in range(4))))
R2 = sp.simplify(sum(g2i[i, j] * Ric2[i, j] for i in range(4) for j in range(4)))
f0, r0 = sp.symbols('f0 r0', positive=True)
sub = {}
thr = lambda e: sp.simplify(e.subs({fl.diff(l, 2): 0, rl.diff(l, 2): 0}).subs({fl.diff(l): 0, rl.diff(l): 0}).subs({fl: f0, rl: r0}))
Ruu_MTW = thr(Ric2[0, 0] / fl)
R_MTW = thr(R2)
QCcoef = sp.simplify(-Ruu_MTW - sp.Rational(1, 2) * (1 - 4 * xi) * R_MTW)   # FO (48) in BD
check("H2: HPS throat (f'=f''=r'=r''=0): R_uu = %s, R = %s (MTW); Q_C/f^2 (FO 48, BD) = %s" %
      (Ruu_MTW, R_MTW, QCcoef), sp.simplify(QCcoef + (1 - 4 * xi) / r0**2) == 0,
      "at xi = 1/6: %s ; at r0 = 0.0242789 l_P: %.1f l_P^-2 (supplementary, not a tree claim)" %
      (QCcoef.subs(xi, sp.Rational(1, 6)), float(QCcoef.subs({xi: sp.Rational(1, 6), r0: 0.0242789}))))
check("H3: xi = 1/6 in [0, 1/4]", 0 <= sp.Rational(1, 6) <= sp.Rational(1, 4))
# vacuity: omega_0 = psi => :omega: = 0 => rho_quant = 0, <:Phi^2:> = 0 ; inequality 0 >= -Qt_A with Qt_A >= 0
QtA = sp.Symbol('QtA', nonnegative=True)
check("H4: omega_0 = psi instance reads 0 >= -Qt_A, true for every Qt_A >= 0 (vacuous)",
      sp.ask(sp.Q.nonnegative(QtA)) is True)

print("\n%d PASS, %d FAIL" % (len(PASS), len(FAIL)))
sys.exit(1 if FAIL else 0)
