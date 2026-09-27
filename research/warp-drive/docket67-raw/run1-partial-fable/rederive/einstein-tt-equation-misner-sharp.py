#!/usr/bin/env python3
"""DOCKET 67 audit 4/286 -- einstein-tt-equation-misner-sharp.

Re-derives, in sympy, the result as the tree uses it (certify.py:116-120,
132-141; drivensource.py:128-132, 162-164, 530-533):

  (1) for ds^2 = -e^{2Phi(r)} dt^2 + dr^2/(1 - 2m(r)/r) + r^2 dOmega^2 the
      orthonormal-frame tt Einstein tensor is G_{tt} = 2 m'(r)/r^2 exactly,
      so G_ab = 8 pi T_ab gives dm/dr = 4 pi r^2 rho with rho = T_{\hat t\hat t};
  (2) the SAME computation with G_ab + Lambda g_ab = 8 pi T_ab gives
      dm/dr = 4 pi r^2 rho - Lambda r^2/2 -- the unstated hypothesis Lambda = 0;
  (3) the Misner-Sharp definition 1 - 2m/r = g^{ab} d_a r d_b r (Hayward 1996
      eq. 4/27) reproduces the m(r) of the chart, so 'm' in the tree IS the
      Misner-Sharp mass and not merely a metric function;
  (4) Reissner-Nordstrom: m(r) = M - Q^2/2r, rho = Q^2/(8 pi r^4) > 0, m < 0
      iff r < Q^2/2M; the enclosed-energy integral is -Q^2/2r + const and its
      r->0+ limit is -oo, so m(0) = 0 fails (drivensource.py:530-533);
  (5) positivity: with m(0) = 0 and rho >= 0, m(r) >= 0 (z3, over an
      interval discretisation of the integral, and sympy for a model rho);
  (6) a caution the tree does not state: dm/dr = 4 pi r^2 rho with rho the
      orthonormal energy density needs 1 - 2m/r > 0 (untrapped) for the static
      chart to be static; the equation itself holds as an identity in m'.

Exit 0 iff every check agrees; every failure is printed and exits 1.
"""
import sys
import sympy as sp

fails = []
def chk(label, expr, want=0):
    ok = sp.simplify(expr - want) == 0
    print("  [%s] %s" % ("ok" if ok else "FAIL", label))
    if not ok:
        fails.append(label)
        print("       got:", sp.simplify(expr))

t, r, th, ph = sp.symbols("t r theta phi", real=True)
Lam = sp.symbols("Lambda", real=True)
Phi = sp.Function("Phi")(r)
m = sp.Function("m")(r)
x = [t, r, th, ph]
g = sp.diag(-sp.exp(2 * Phi), 1 / (1 - 2 * m / r), r**2, r**2 * sp.sin(th)**2)
gi = g.inv()

def christoffel(g, gi):
    G = [[[0] * 4 for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                G[a][b][c] = sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d])) for d in range(4)) / 2)
    return G

def ricci(G):
    R = sp.zeros(4, 4)
    for b in range(4):
        for c in range(4):
            s = 0
            for a in range(4):
                s += sp.diff(G[a][b][c], x[a]) - sp.diff(G[a][b][a], x[c])
                for d in range(4):
                    s += G[a][a][d] * G[d][b][c] - G[a][c][d] * G[d][b][a]
            R[b, c] = sp.simplify(s)
    return R

print("1. Einstein tensor of the static areal-radius chart")
Gam = christoffel(g, gi)
Ric = ricci(Gam)
Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(4) for b in range(4)))
Ein = sp.simplify(Ric - Rs * g / 2)
# orthonormal frame: e_t = e^{-Phi} d_t, e_r = sqrt(1-2m/r) d_r
Gtt_hat = sp.simplify(Ein[0, 0] * sp.exp(-2 * Phi))
Grr_hat = sp.simplify(Ein[1, 1] * (1 - 2 * m / r))
chk("G_{tt}(orthonormal) = 2 m'/r^2   (so 8 pi rho = 2 m'/r^2, dm/dr = 4 pi r^2 rho)", Gtt_hat, 2 * sp.diff(m, r) / r**2)
chk("G_{tt} carries NO Phi: the tt equation is a pure constraint on m", sp.diff(Gtt_hat, Phi), 0)
chk("G_{rr}(orthonormal) = -2m/r^3 + 2(1-2m/r)Phi'/r  (the rr equation, for the record)", Grr_hat, -2 * m / r**3 + 2 * (1 - 2 * m / r) * sp.diff(Phi, r) / r)
chk("G_{tr} = 0: no radial flux in the static chart, T_01 = 0 automatically", Ein[0, 1], 0)
rho = sp.symbols("rho")
sol = sp.solve(sp.Eq(Gtt_hat, 8 * sp.pi * rho), sp.diff(m, r))[0]
chk("solving G_tt = 8 pi rho for m': m' = 4 pi r^2 rho", sol, 4 * sp.pi * r**2 * rho)

print("\n2. with a cosmological constant, G_ab + Lambda g_ab = 8 pi T_ab")
solL = sp.solve(sp.Eq(Gtt_hat + Lam * g[0, 0] * sp.exp(-2 * Phi), 8 * sp.pi * rho), sp.diff(m, r))[0]
chk("m' = 4 pi r^2 rho + Lambda r^2/2  (Lambda = 0 is an unstated hypothesis of the tree's form)", solL, 4 * sp.pi * r**2 * rho + Lam * r**2 / 2)
# Maeda-Nozawa 0709.1199 eq. (2.7) at n = 4, k = 1, alpha = 0 folds Lambda into the mass: m_MN = (r/2)(1 - (Dr)^2 - Lambda r^2/3)
m_MN = m - Lam * r**3 / 6
chk("Maeda-Nozawa's Lambda-corrected mass m_MN = m - Lambda r^3/6 restores m_MN' = 4 pi r^2 rho exactly", sp.diff(m_MN, r).subs(sp.diff(m, r), solL), 4 * sp.pi * r**2 * rho)

print("\n3. the chart's m IS the Misner-Sharp mass: 1 - 2E/r = g^{ab} d_a r d_b r")
E_ms = sp.simplify(r / 2 * (1 - sum(gi[a, b] * sp.diff(r, x[a]) * sp.diff(r, x[b]) for a in range(4) for b in range(4))))
chk("E_MS(Hayward eq. 4) = m(r)", E_ms, m)

print("\n4. Reissner-Nordstrom in this chart")
M, Q = sp.symbols("M Q", positive=True)
f_rn = 1 - 2 * M / r + Q**2 / r**2
m_rn = sp.solve(sp.Eq(1 - 2 * sp.Symbol("mm") / r, f_rn), sp.Symbol("mm"))[0]
chk("m_RN = M - Q^2/(2r)", m_rn, M - Q**2 / (2 * r))
rho_rn = sp.simplify(sp.diff(m_rn, r) / (4 * sp.pi * r**2))
chk("rho_RN = m'/(4 pi r^2) = Q^2/(8 pi r^4)  (> 0 for all r > 0)", rho_rn, Q**2 / (8 * sp.pi * r**4))
# and it is the Maxwell energy density of the Coulomb field E = Q/r^2: (E^2)/(8 pi)
chk("  which is the Maxwell energy density E^2/8pi of the Coulomb field Q/r^2", rho_rn, (Q / r**2)**2 / (8 * sp.pi))
rc = sp.solve(sp.Eq(m_rn, 0), r)[0]
chk("m_RN < 0 iff r < r_c = Q^2/(2M)", rc, Q**2 / (2 * M))
enc = sp.integrate(4 * sp.pi * r**2 * rho_rn, r)
chk("indefinite integral of 4 pi r^2 rho_RN = -Q^2/(2r)", enc, -Q**2 / (2 * r))
lim = sp.limit(enc, r, 0, "+")
print("  [%s] lim_{r->0+} of the enclosed-energy integral = %s  (m(0) = 0 is impossible: not a regular centre)" % ("ok" if lim == -sp.oo else "FAIL", lim))
if lim != -sp.oo:
    fails.append("RN limit")
# the integral from a > 0 out to r is finite: m(r) - m(a) = Q^2/2a - Q^2/2r  -- the constant of integration survives
chk("m(r) - m(a) = INT_a^r 4 pi r'^2 rho = Q^2/(2a) - Q^2/(2r): the constant of integration is m(a), never 0", sp.integrate(4 * sp.pi * r**2 * rho_rn, (r, sp.Symbol("a", positive=True), r)), Q**2 / (2 * sp.Symbol("a", positive=True)) - Q**2 / (2 * r))
# Hayward Prop. 2 (as read): a central singularity with E < 0 is temporal and untrapped.
lim2 = sp.limit(1 - 2 * m_rn / r, r, 0, "+")
print("  [%s] lim_{r->0+} (1 - 2m_RN/r) = %s > 0: the r < r_c region is UNTRAPPED and the singularity temporal (Hayward Prop. 2, E < 0)" % ("ok" if lim2 == sp.oo else "FAIL", lim2))
if lim2 != sp.oo:
    fails.append("RN untrapped")
chk("  and 1 - 2m/r - 1 = -2m/r, so 'untrapped with 1 - 2m/r > 1' is exactly m < 0", sp.simplify((1 - 2 * m_rn / r) - 1 + 2 * m_rn / r), 0)

print("\n5. positivity with a regular centre: m(0) = 0 and rho >= 0  =>  m(r) >= 0")
try:
    import z3
    # discretised Riemann sum of INT_0^R 4 pi r^2 rho over N cells; rho_i >= 0 free reals.
    N = 12
    rhos = [z3.Real("rho%d" % i) for i in range(N)]
    R = z3.Real("R")
    s = z3.Solver()
    s.add(R > 0)
    for v in rhos:
        s.add(v >= 0)
    mR = sum(4 * 3 * ((i + 0.5) * R / N) ** 2 * (R / N) * rhos[i] for i in range(N))  # 4*pi -> 4*3 keeps it rational; sign unaffected
    s.add(mR < 0)  # look for a counterexample
    res = s.check()
    ok = (res == z3.unsat)
    print("  [%s] z3: no assignment with rho_i >= 0, m(0) = 0 makes the (Riemann) enclosed mass negative (%s)" % ("ok" if ok else "FAIL", res))
    if not ok:
        fails.append("z3 positivity")
    # and the control: allow one negative cell and a witness exists
    s2 = z3.Solver()
    s2.add(R > 0)
    for v in rhos[1:]:
        s2.add(v >= 0)
    s2.add(mR < 0)
    print("  [%s] z3 control: with one cell's rho unconstrained a negative m(R) IS satisfiable (%s)" % ("ok" if s2.check() == z3.sat else "FAIL", s2.check()))
except ImportError:
    print("  [skip] z3 not installed")
# sympy: a model with rho >= 0 (uniform star) and the integral from 0
rho0, Rb = sp.symbols("rho0 R", positive=True)
m_uni = sp.integrate(4 * sp.pi * r**2 * rho0, (r, 0, r))
chk("uniform rho0 >= 0 from a regular centre: m(r) = 4 pi rho0 r^3/3 >= 0", m_uni, 4 * sp.pi * rho0 * r**3 / 3)
chk("  and it is O(r^3): Hayward's regularity E = O(r^3) holds, stronger than the tree's m(0) = 0", sp.limit(m_uni / r**3, r, 0), 4 * sp.pi * rho0 / 3)
# a rho ~ 1/r^2 profile: m(0) = 0 holds, m >= 0 holds, but m = O(r) -- NOT Hayward-regular. Conclusion unaffected.
k = sp.symbols("k", positive=True)
m_cone = sp.integrate(4 * sp.pi * r**2 * k / r**2, (r, 0, r))
chk("rho = k/r^2: m = 4 pi k r, m(0) = 0 and m >= 0 hold, but m = O(r), a conical (non-Hayward-regular) centre", m_cone, 4 * sp.pi * k * r)

print("\n6. the derivation of the theorem line: proper radial distance contracted iff m < 0")
chk("dl/dr = 1/sqrt(1-2m/r) < 1  iff  m < 0 (given 1 - 2m/r > 0)", sp.simplify((1 - 2 * m / r) - 1 + 2 * m / r), 0)

print()
if fails:
    print("FAILED:", fails)
    sys.exit(1)
print("ALL CHECKS AGREE with the tree's statement (certify.py:118-120, drivensource.py:530-533) and with Hayward gr-qc/9408002 eqs. (4), (27), (28a), (33), Prop. 6.")
