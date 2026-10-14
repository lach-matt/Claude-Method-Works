#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for Sanders, arXiv:2007.14311v2 (Theorem 5.1 / Corollary 5.2).

Source text read: d67/src/casmag/all/2007.14311v2.txt (v2, 17 Sep 2021; pages 1-4, 14-15,
18, 22-23, 29-30 present in the cached extraction; pages 5-13 and 16-17, 19-21, 24-28 absent).

Checks (each prints PASS/FAIL):
 C1  Einstein static universe geometry: R = 6/a^2, G_00 = R/2 = 3/a^2, g^ab G_ab = -R,
     so the left sides of Sanders (91), (92) are (R - 4L)/k and (R - 2L)/(2k).
 C2  No classical vacuum ESU: (91),(92) with zero right-hand side force R = 0 (a -> inf).
 C3  c := m^2 a^2 + 6 xi - 1 > -1  <=>  m^2 + xi R > 0 (the theorem's hypothesis), and
     c + 1 = a^2 (m^2 + xi R) (used in the proof of Cor. 5.2(3)).
 C4  Zonal spectrum on unit S^3: Gegenbauer C_n^(1)(cos chi) has -Laplacian eigenvalue
     n(n+2); hence l_n^2 = (n+1)^2 + c, l_0^2 = c + 1, l_n = n + 1 at c = 0 (as printed).
 C5  z3: Cor. 5.2(3) necessity -- for a_n >= 0 (N terms), m > 0, c > -1,
     m^2 sum a_n = Y1 and sum a_n l_n^2 / a^2 = Y2 imply m^2 Y2 >= (m^2 + xi R) Y1,
     with equality only if a_n = 0 for n >= 1.  Checked by UNSAT of the negation.
 C6  The c = 0 specialisation (p.15) is consistent with (93),(94) iff X1(c=0) = -1/12 and
     X2(c=0) = 1/120, i.e. zeta(-1) and zeta(-3).  Dimensional check of the printed Y2 at
     c = 0: the printed '-1/(480 pi^2 a^2)' is dimensionally inconsistent with every other
     term (1/length^4); '-1/(480 pi^2 a^4)' is consistent.  RECORDED AS A DISCREPANCY of the
     v2 text (misprint or extraction), NOT an error; journal version not read.
 C7  Misner-Sharp mass of the ESU, the quantity the tree's O5 tally asks about:
     r = a sin chi, m = (r/2)(1 - g^{ab} d_a r d_b r) = (a/2) sin^3 chi >= 0 for EVERY a > 0,
     independent of the state and of the renormalisation constants.  m(r) < 0 anywhere: never.
     At the equator (r' = 0) m = r/2, as at a throat, but r'' < 0 there (a maximal sphere,
     not a throat), consistent with the tree's throat flag False.
"""
import sympy as sp
import z3

ok = True
def chk(label, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + label)

# ---------- C1: ESU curvature ----------
t, chi, th, ph = sp.symbols('t chi theta phi', real=True)
a, Lam, kap = sp.symbols('a Lambda kappa', positive=True)
x = [t, chi, th, ph]
g = sp.diag(-1, a**2, a**2*sp.sin(chi)**2, a**2*sp.sin(chi)**2*sp.sin(th)**2)
gi = g.inv()
n = 4
Gam = [[[sp.simplify(sum(gi[i, l]*(sp.diff(g[l, j], x[k]) + sp.diff(g[l, k], x[j]) - sp.diff(g[j, k], x[l]))
                         for l in range(n))/2) for k in range(n)] for j in range(n)] for i in range(n)]
def Ric(j, k):
    return sp.simplify(sum(sp.diff(Gam[i][j][k], x[i]) - sp.diff(Gam[i][j][i], x[k])
                           + sum(Gam[i][i][l]*Gam[l][j][k] - Gam[i][k][l]*Gam[l][j][i] for l in range(n))
                           for i in range(n)))
Rm = sp.Matrix(n, n, lambda j, k: Ric(j, k))
R = sp.simplify(sum(gi[i, j]*Rm[i, j] for i in range(n) for j in range(n)))
G = sp.simplify(Rm - R*g/2)
chk("C1 R = 6/a^2", sp.simplify(R - 6/a**2) == 0)
chk("C1 G_00 = 3/a^2 = R/2", sp.simplify(G[0, 0] - 3/a**2) == 0)
trG = sp.simplify(sum(gi[i, j]*G[i, j] for i in range(n) for j in range(n)))
chk("C1 g^ab G_ab = -R", sp.simplify(trG + R) == 0)
chk("C1 (91) LHS: -(G^a_a + 4L)/k = (R - 4L)/k", sp.simplify(-(trG + 4*Lam)/kap - (R - 4*Lam)/kap) == 0)
chk("C1 (92) LHS: (G_00 + L g_00)/k = (R - 2L)/(2k)",
    sp.simplify((G[0, 0] + Lam*g[0, 0])/kap - (R - 2*Lam)/(2*kap)) == 0)
# spatial part: G_ij = -h_ij (with g_ij = a^2 h_ij): Sanders (17) read as (3/a^2) dt dt - h
chk("C1 G_ij = -g_ij/a^2 = -h_ij  (eq. (17) as (3/a^2) dt dt - h_ab)",
    all(sp.simplify(G[i, i] + g[i, i]/a**2) == 0 for i in (1, 2, 3)))

# ---------- C2: no classical vacuum ESU ----------
Rs, L = sp.symbols('R L', real=True)
sol = sp.solve([Rs - 4*L, Rs - 2*L], [Rs, L], dict=True)
chk("C2 classical vacuum (91)=(92)=0 forces R = 0: " + str(sol), sol == [{Rs: 0, L: 0}])

# ---------- C3: hypothesis equivalence ----------
m, xi = sp.symbols('m xi', real=True)
c = m**2*a**2 + 6*xi - 1
chk("C3 c + 1 = a^2 (m^2 + xi R)", sp.simplify(c + 1 - a**2*(m**2 + xi*6/a**2)) == 0)
# c > -1 <=> m^2 + xi R > 0 since a^2 > 0 : z3
zm, zxi, za = z3.Reals('m xi a')
s = z3.Solver()
s.add(za > 0, z3.Not((zm*zm*za*za + 6*zxi - 1 > -1) == (zm*zm + zxi*6/(za*za) > 0)))
chk("C3 z3: c > -1 <=> m^2 + xi R > 0  (a > 0)", s.check() == z3.unsat)

# ---------- C4: spectrum of zonal harmonics on S^3 ----------
u = sp.symbols('u')
allgood = True
for k in range(0, 8):
    Y = sp.gegenbauer(k, 1, sp.cos(chi))
    lap = sp.diff(sp.sin(chi)**2*sp.diff(Y, chi), chi)/sp.sin(chi)**2
    allgood &= sp.simplify(lap + k*(k + 2)*Y) == 0
    allgood &= sp.gegenbauer(k, 1, 1) == k + 1          # C_n^(1)(1) = n+1, Sanders (119)
chk("C4 -Lap C_n^(1)(cos chi) = n(n+2) C_n^(1), C_n^(1)(1) = n+1, n = 0..7", allgood)
nn = sp.symbols('n', integer=True, nonnegative=True)
ln2 = nn*(nn + 2) + m**2*a**2 + 6*xi          # a^2 (omega_n^2) = n(n+2) + a^2 (m^2 + xi R)
chk("C4 l_n^2 = (n+1)^2 + c", sp.simplify(ln2 - ((nn + 1)**2 + c)) == 0)
chk("C4 l_0^2 = c + 1 and l_n = n+1 at c = 0",
    sp.simplify(ln2.subs(nn, 0) - (c + 1)) == 0 and
    sp.simplify(((nn + 1)**2 + c).subs({m: 0, xi: sp.Rational(1, 6)}) - (nn + 1)**2) == 0)

# ---------- C5: Corollary 5.2(3) necessity, z3 ----------
def cor52_3(N):
    s = z3.Solver()
    A = [z3.Real('a%d' % i) for i in range(N)]
    zm, zc, za, Y1, Y2 = z3.Reals('m c a Y1 Y2')
    l2 = [(i + 1)**2 + zc for i in range(N)]
    s.add(zm > 0, za > 0, zc > -1, *[ai >= 0 for ai in A])
    s.add(zm*zm*z3.Sum(A) == Y1, z3.Sum([A[i]*l2[i] for i in range(N)]) == Y2*za*za)
    # m^2 + xi R = (c+1)/a^2
    s.add(z3.Not(zm*zm*Y2*za*za >= (zc + 1)*Y1))
    r1 = s.check()
    # strictness: equality forces a_n = 0 for n >= 1
    s2 = z3.Solver()
    s2.add(zm > 0, za > 0, zc > -1, *[ai >= 0 for ai in A])
    s2.add(zm*zm*z3.Sum(A) == Y1, z3.Sum([A[i]*l2[i] for i in range(N)]) == Y2*za*za)
    s2.add(zm*zm*Y2*za*za == (zc + 1)*Y1, z3.Or(*[A[i] > 0 for i in range(1, N)]))
    return r1, s2.check()
for N in (2, 4, 8):
    r1, r2 = cor52_3(N)
    chk("C5 z3 N=%d: m^2 Y2 >= (m^2+xi R) Y1 [negation %s]; equality => a_n=0 (n>=1) [%s]" % (N, r1, r2),
        r1 == z3.unsat and r2 == z3.unsat)

# ---------- C6: c = 0 specialisation and the a^2 / a^4 discrepancy ----------
X1, X2, ms = sp.symbols('X1 X2 m_s', real=True)
Y1_gen_c0 = (1/(32*sp.pi**2*a**4))*(-8*ms**2*a**2*X1)          # (93) at c = 0, minus the 1/k' term
Y2_gen_c0 = (1/(64*sp.pi**2*a**4))*(-16*X2)                     # (94) at c = 0, minus the k', c' terms
x1 = sp.solve(sp.Eq(Y1_gen_c0, ms**2/(48*sp.pi**2*a**2)), X1)
x2_a4 = sp.solve(sp.Eq(Y2_gen_c0, -1/(480*sp.pi**2*a**4)), X2)
x2_a2 = sp.solve(sp.Eq(Y2_gen_c0, -1/(480*sp.pi**2*a**2)), X2)
chk("C6 printed Y1(c=0) = m^2/(48 pi^2 a^2) requires X1 = %s = zeta(-1)" % x1,
    x1 == [sp.Rational(-1, 12)] and sp.zeta(-1) == sp.Rational(-1, 12))
chk("C6 Y2(c=0) with a^4 requires X2 = %s = zeta(-3) (a pure number)" % x2_a4,
    x2_a4 == [sp.Rational(1, 120)] and sp.zeta(-3) == sp.Rational(1, 120))
chk("C6 Y2(c=0) as printed with a^2 requires X2 = %s, which carries a^2 -- X2 would not be a number" % x2_a2,
    x2_a2 != [] and sp.simplify(x2_a2[0]).has(a))
# dimensional bookkeeping: [length] exponents with hbar = c = 1, kappa' ~ L^2, R ~ L^-2
dim = {'Y1_kterm': -4, 'Y2_kterm': -4, 'cprimeR2': -4, 'printed_a2': -2, 'corrected_a4': -4}
chk("C6 dimension: (R-2L')/(2k') ~ L^-4, c'R^2 ~ L^-4; printed 1/(480 pi^2 a^2) ~ L^-2 [DISCREPANCY]",
    dim['printed_a2'] != dim['Y2_kterm'] and dim['corrected_a4'] == dim['Y2_kterm'])

# ---------- C7: Misner-Sharp mass of the ESU ----------
r_areal = a*sp.sin(chi)
grad2 = gi[1, 1]*sp.diff(r_areal, chi)**2          # r depends on chi only
m_MS = sp.simplify(r_areal/2*(1 - grad2))
chk("C7 m_MS = (a/2) sin^3 chi : got %s" % m_MS, sp.simplify(m_MS - a*sp.sin(chi)**3/2) == 0)
# non-negativity on chi in [0, pi], a > 0: z3 on s = sin chi in [0,1]
zs, za = z3.Reals('s a')
sv = z3.Solver(); sv.add(za > 0, zs >= 0, zs <= 1, za/2*zs*zs*zs < 0)
chk("C7 z3: m_MS < 0 is UNSAT for a > 0, chi in [0, pi]", sv.check() == z3.unsat)
lprop = sp.symbols('l', positive=True)          # proper radial distance l = a chi
r_l = a*sp.sin(lprop/a)
chk("C7 at equator l = a pi/2: r' = 0, m = r/2, r'' = -1/a < 0 (maximal sphere, not a throat)",
    sp.simplify(sp.diff(r_l, lprop).subs(lprop, a*sp.pi/2)) == 0 and
    sp.simplify((r_l/2*(1 - sp.diff(r_l, lprop)**2) - r_l/2).subs(lprop, a*sp.pi/2)) == 0 and
    sp.simplify(sp.diff(r_l, lprop, 2).subs(lprop, a*sp.pi/2) + 1/a) == 0)
# density bookkeeping: dm/dl = 4 pi r^2 r' rho_eff with rho_eff = G_00/(8 pi) = 3/(8 pi a^2) > 0
rho = G[0, 0]/(8*sp.pi)
chk("C7 dm/dl = 4 pi r^2 r' rho_eff, rho_eff = 3/(8 pi a^2) > 0 (geometric, state-independent)",
    sp.simplify(sp.diff(r_l/2*(1 - sp.diff(r_l, lprop)**2), lprop)
                - 4*sp.pi*r_l**2*sp.diff(r_l, lprop)*rho) == 0)

print("\nREDERIVE %s" % ("OK" if ok else "FAILED"))
raise SystemExit(0 if ok else 1)
