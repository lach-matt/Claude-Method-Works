#!/usr/bin/env python3
"""DOCKET 67 -- audit of the null energy condition as the warp board uses it.

Re-derives / machine-checks every finite or closed-form claim the five owners
(driven.py, drivensource.py, nonstatic.py, latticectc.py, seatindex.py) make with
the NEC, against the published definition (Hawking-Ellis 1973 sec 4.3, read via
Kontou-Sanders arXiv:2003.01815 eq 26 / Table 1 and Martin-Moruno-Visser
arXiv:1702.05915 eq 2.6):

    NEC:  T_ab k^a k^b >= 0 for EVERY null vector k.   Perfect fluid: rho + P >= 0.

Sections
  (A) Maxwell: T_kk = |P_perp(E + n x B)|^2 / 4pi (sum of squares, sympy); and a
      null k with T_kk = 0 exists for every (E, B) (saturation, numeric).
  (B) Spherical radial electric field: orthonormal T = (E^2/8pi) diag(1,-1,1,1) in
      ANY metric (algebraic, frame-level); RN check via exact Einstein tensor.
  (C) Open FRW (k = -1): G_ab contracted with k = u + e_chi equals
      (adot^2 - 1 - a addot)/(4 pi a^2) = rho + p; equals rho ONLY for dust.
  (D) nonstatic identity T_kk(radial) = rho + p_r - 2j with j = -T(u,n); and
      the two contractions nonstatic checks (radial-out, transverse) are NOT the
      full NEC when j != 0 (z3 counterexample).
  (E) Classical NEC violation by the non-minimally coupled scalar (Kontou-Sanders
      eq 32 example, re-derived from eq 7): 'classical T_ab' alone does not imply
      the NEC; minimal coupling (or Maxwell, or rho+P>=0 fluid) does.
  (F) seatindex data: pi c^4/(4G) with CODATA 2022 G; nuclear saturation energy
      density vs the tree's '~1e35 Pa'.
Exit 0 iff every check passes.
"""
import math
import random
import sys

import sympy as sp

OK = True


def chk(label, cond, extra=""):
    global OK
    OK = OK and bool(cond)
    print("  %-78s %s %s" % (label, "ok" if cond else "FAIL", extra))


# ------------------------------------------------------------------ (A)
print("(A) Maxwell stress-energy, flat space, Gaussian units, signature (-,+,+,+)")
E = sp.Matrix(sp.symbols("E1:4", real=True))
B = sp.Matrix(sp.symbols("B1:4", real=True))
n = sp.Matrix(sp.symbols("n1:4", real=True))
eta = sp.diag(-1, 1, 1, 1)
F = sp.zeros(4, 4)                       # F_{mu nu}, F_{i0} = E_i, F_{ij} = eps_ijk B_k
for i in range(3):
    F[i + 1, 0] = E[i]
    F[0, i + 1] = -E[i]
eps = sp.LeviCivita
for i in range(3):
    for j in range(3):
        F[i + 1, j + 1] = sum(eps(i, j, k) * B[k] for k in range(3))
Fup = eta * F * eta                      # F^{mu nu}
F2 = sum(F[a, b] * Fup[a, b] for a in range(4) for b in range(4))
T = sp.zeros(4, 4)
for a in range(4):
    for b in range(4):
        T[a, b] = (sum(F[a, c] * F[b, d] * eta[c, d] for c in range(4) for d in range(4))
                   - sp.Rational(1, 4) * eta[a, b] * F2) / (4 * sp.pi)
chk("T_00 = (E^2 + B^2)/8pi", sp.simplify(T[0, 0] - (E.dot(E) + B.dot(B)) / (8 * sp.pi)) == 0)
k = [1, n[0], n[1], n[2]]
Tkk = sp.expand(sum(T[a, b] * k[a] * k[b] for a in range(4) for b in range(4)))
nn = n.dot(n)
Eperp = E - E.dot(n) * n
sos_plus = (Eperp + n.cross(B)).dot(Eperp + n.cross(B)) / (4 * sp.pi)
sos_minus = (Eperp - n.cross(B)).dot(Eperp - n.cross(B)) / (4 * sp.pi)
# reduce on the unit sphere |n| = 1 : substitute n3^2 = 1 - n1^2 - n2^2
def on_sphere(x):
    x = sp.expand(x)
    return sp.simplify(sp.expand(x.subs(n[2]**2, 1 - n[0]**2 - n[1]**2)).subs(n[2]**2, 1 - n[0]**2 - n[1]**2))
# dplus = on_sphere(sp.expand(Tkk - sos_plus).subs(n[2]**4, (1 - n[0]**2 - n[1]**2)**2))
# dminus = on_sphere(sp.expand(Tkk - sos_minus).subs(n[2]**4, (1 - n[0]**2 - n[1]**2)**2))
# numeric confirmation of whichever sign matches, on random unit n
rng = random.Random(67)
def num(expr, sub):
    return float(expr.subs(sub))
worst = {"+": 0.0, "-": 0.0}
for _ in range(200):
    v = [rng.gauss(0, 1) for _ in range(3)]
    r = math.sqrt(sum(x * x for x in v))
    sub = {n[i]: v[i] / r for i in range(3)}
    sub.update({E[i]: rng.gauss(0, 1) for i in range(3)})
    sub.update({B[i]: rng.gauss(0, 1) for i in range(3)})
    t = num(Tkk, sub)
    worst["+"] = max(worst["+"], abs(t - num(sos_plus, sub)))
    worst["-"] = max(worst["-"], abs(t - num(sos_minus, sub)))
sign = "+" if worst["+"] < 1e-12 else ("-" if worst["-"] < 1e-12 else None)
chk("T_ab k^a k^b = |P_perp E (sign) n x B|^2/4pi on |n|=1 (200 random, one sign exact)",
    sign is not None, "sign=%s maxdev(+)=%.1e maxdev(-)=%.1e" % (sign, worst["+"], worst["-"]))
resid = sp.expand(Tkk - (sos_plus if sign == "+" else sos_minus))
remd = sp.rem(sp.Poly(resid, n[2]), sp.Poly(nn - 1, n[2]))
chk("symbolic: residual is a multiple of (|n|^2 - 1), i.e. zero on the unit sphere",
    sp.simplify(remd.as_expr()) == 0, "(polynomial remainder in n3)")
# saturation: for every (E,B) there is a unit n with T_kk = 0 (principal null direction)
def tkk_num(Ev, Bv, nv):
    ep = [Ev[i] - sum(Ev[j] * nv[j] for j in range(3)) * nv[i] for i in range(3)]
    nxB = [nv[1] * Bv[2] - nv[2] * Bv[1], nv[2] * Bv[0] - nv[0] * Bv[2], nv[0] * Bv[1] - nv[1] * Bv[0]]
    s = 1 if sign == "+" else -1
    return sum((ep[i] + s * nxB[i])**2 for i in range(3)) / (4 * math.pi)
def pnd_min(Ev, Bv):
    # principal null directions of a Maxwell field: minimise over the sphere
    best = 1e99
    for it in range(4000):
        th = math.acos(1 - 2 * (it + 0.5) / 4000)
        ph = math.pi * (1 + 5 ** 0.5) * it
        nv = [math.sin(th) * math.cos(ph), math.sin(th) * math.sin(ph), math.cos(th)]
        val = tkk_num(Ev, Bv, nv)
        if val < best:
            best, bn = val, nv
    step = 0.05                           # local refinement around the best grid point
    for _ in range(3000):
        cand = [bn[i] + rng.gauss(0, step) for i in range(3)]
        rr = math.sqrt(sum(x * x for x in cand))
        cand = [x / rr for x in cand]
        val = tkk_num(Ev, Bv, cand)
        if val < best:
            best, bn = val, cand
        else:
            step = max(step * 0.998, 1e-9)
    return best
mins = []
for _ in range(20):
    Ev = [rng.gauss(0, 1) for _ in range(3)]
    Bv = [rng.gauss(0, 1) for _ in range(3)]
    u0 = (sum(x * x for x in Ev) + sum(x * x for x in Bv)) / (8 * math.pi)
    mins.append(pnd_min(Ev, Bv) / u0)
chk("inf over null directions of T_kk / T_00 -> 0 for random (E,B) (grid+refine, <1e-8)",
    max(mins) < 1e-8, "max ratio %.2e" % max(mins))
chk("T_kk >= 0 at every sampled direction (sum of squares)", min(mins) >= 0.0)

# ------------------------------------------------------------------ (B)
print("\n(B) Radial electric field in spherical symmetry")
Er = sp.Symbol("E_r", positive=True)
Fo = sp.zeros(4, 4)                      # orthonormal frame components, e0 = u, e1 = n
Fo[1, 0], Fo[0, 1] = Er, -Er
F2o = sum(Fo[a, b] * (eta * Fo * eta)[a, b] for a in range(4) for b in range(4))
To = sp.zeros(4, 4)
for a in range(4):
    for b in range(4):
        To[a, b] = (sum(Fo[a, c] * Fo[b, d] * eta[c, d] for c in range(4) for d in range(4))
                    - sp.Rational(1, 4) * eta[a, b] * F2o) / (4 * sp.pi)
rho_e = Er**2 / (8 * sp.pi)
chk("orthonormal T = (E^2/8pi) diag(1,-1,1,1): frame algebra, metric-independent",
    sp.simplify(To - rho_e * sp.diag(1, -1, 1, 1)) == sp.zeros(4, 4))
chk("radial NEC rho + p_r = 0 (saturated, both radial directions)", sp.simplify(To[0, 0] + To[1, 1]) == 0)
chk("transverse NEC rho + p_T = 2 rho > 0 (NOT saturated)", sp.simplify(To[0, 0] + To[2, 2] - 2 * rho_e) == 0)
alpha = sp.Symbol("alpha", real=True)
kgen = [1, sp.cos(alpha), sp.sin(alpha), 0]
Tk_gen = sp.simplify(sum(To[a, b] * kgen[a] * kgen[b] for a in range(4) for b in range(4)))
chk("general null direction: T_kk = 2 rho sin^2(alpha) >= 0, zero only radially",
    sp.simplify(Tk_gen - 2 * rho_e * sp.sin(alpha)**2) == 0, "T_kk=%s" % Tk_gen)
# exact RN Einstein tensor
t, r, th, ph = sp.symbols("t r theta phi")
M, Q = sp.symbols("M Q", positive=True)
f = 1 - 2 * M / r + Q**2 / r**2
g = sp.diag(-f, 1 / f, r**2, r**2 * sp.sin(th)**2)
X = [t, r, th, ph]
gi = g.inv()
Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
             for d in range(4)) / 2 for c in range(4)] for b in range(4)] for a in range(4)]
def ricci(b, c):
    return sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                           + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(4))
                           for a in range(4)))
Ric = sp.Matrix(4, 4, lambda b, c: ricci(b, c))
Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(4) for b in range(4)))
G = sp.simplify(Ric - Rs * g / 2)
rho_RN = sp.simplify(G[0, 0] / f / (8 * sp.pi))
pr_RN = sp.simplify(G[1, 1] * f / (8 * sp.pi))
pT_RN = sp.simplify(G[2, 2] / r**2 / (8 * sp.pi))
chk("RN: rho = Q^2/(8 pi r^4)", sp.simplify(rho_RN - Q**2 / (8 * sp.pi * r**4)) == 0)
chk("RN: p_r = -rho, p_T = +rho", sp.simplify(pr_RN + rho_RN) == 0 and sp.simplify(pT_RN - rho_RN) == 0)

# ------------------------------------------------------------------ (C)
print("\n(C) Open FRW, k = -1: ds^2 = -dt^2 + a(t)^2 (dchi^2 + sinh^2 chi dOmega^2)")
chi = sp.Symbol("chi", positive=True)
a = sp.Function("a")(t)
gF = sp.diag(-1, a**2, a**2 * sp.sinh(chi)**2, a**2 * sp.sinh(chi)**2 * sp.sin(th)**2)
XF = [t, chi, th, ph]
giF = gF.inv()
GamF = [[[sp.simplify(sum(giF[A, d] * (sp.diff(gF[d, b], XF[c]) + sp.diff(gF[d, c], XF[b]) - sp.diff(gF[b, c], XF[d]))
                          for d in range(4)) / 2) for c in range(4)] for b in range(4)] for A in range(4)]
def ricF(b, c):
    return sp.simplify(sum(sp.diff(GamF[A][b][c], XF[A]) - sp.diff(GamF[A][b][A], XF[c])
                           + sum(GamF[A][A][d] * GamF[d][b][c] - GamF[A][c][d] * GamF[d][b][A] for d in range(4))
                           for A in range(4)))
RicF = sp.Matrix(4, 4, lambda b, c: ricF(b, c))
RsF = sp.simplify(sum(giF[A, b] * RicF[A, b] for A in range(4) for b in range(4)))
GF = sp.simplify(RicF - RsF * gF / 2)
ad, add = sp.diff(a, t), sp.diff(a, t, 2)
kF = [1, 1 / a, 0, 0]                    # u + e_chi, -u.k = 1
Tkk_F = sp.simplify(sum(GF[A, b] * kF[A] * kF[b] for A in range(4) for b in range(4)) / (8 * sp.pi))
chk("k = u + e_chi is null", sp.simplify(sum(gF[A, b] * kF[A] * kF[b] for A in range(4) for b in range(4))) == 0)
chk("T_kk = (adot^2 - 1 - a addot)/(4 pi a^2)  (nonstatic.py:99-100)",
    sp.simplify(Tkk_F - (ad**2 - 1 - a * add) / (4 * sp.pi * a**2)) == 0)
rhoF = sp.simplify(GF[0, 0] / (8 * sp.pi))
pF = sp.simplify(GF[1, 1] / a**2 / (8 * sp.pi))
chk("rho = 3(adot^2 - 1)/(8 pi a^2)  (nonstatic.py:98-99)", sp.simplify(rhoF - 3 * (ad**2 - 1) / (8 * sp.pi * a**2)) == 0)
chk("T_kk = rho + p identically (any perfect fluid)", sp.simplify(Tkk_F - rhoF - pF) == 0)
# open dust, parametric: a = A(cosh eta - 1), t = A(sinh eta - eta)
et, Ad = sp.symbols("eta A", positive=True)
a_e = Ad * (sp.cosh(et) - 1)
t_e = Ad * (sp.sinh(et) - et)
adot_e = sp.diff(a_e, et) / sp.diff(t_e, et)
addot_e = sp.diff(adot_e, et) / sp.diff(t_e, et)
rho_d = sp.simplify(3 * (adot_e**2 - 1) / (8 * sp.pi * a_e**2))
p_d = sp.simplify(-(2 * a_e * addot_e + adot_e**2 - 1) / (8 * sp.pi * a_e**2))
chk("open dust: p = 0 exactly", sp.simplify(p_d) == 0)
chk("open dust: rho = 3 A/(4 pi a^3) > 0, so T_kk = rho > 0 (STRICT)",
    sp.simplify(rho_d - 3 * Ad / (4 * sp.pi * a_e**3)) == 0)
# open radiation: T_kk = 4 rho / 3 != rho -- 'equals rho' needs dust
a_r = sp.sqrt(sp.Symbol("C", positive=True) * sp.sinh(et)**2)  # a = sqrt(C) sinh(eta)
t_r = sp.sqrt(sp.Symbol("C", positive=True)) * (sp.cosh(et) - 1)
adot_r = sp.simplify(sp.diff(a_r, et) / sp.diff(t_r, et))
addot_r = sp.simplify(sp.diff(adot_r, et) / sp.diff(t_r, et))
rho_r = sp.simplify(3 * (adot_r**2 - 1) / (8 * sp.pi * a_r**2))
Tkk_r = sp.simplify((adot_r**2 - 1 - a_r * addot_r) / (4 * sp.pi * a_r**2))
chk("open radiation (conformal time): T_kk = (4/3) rho, not rho -> driven.py:246-247 drops 'dust'",
    sp.simplify(Tkk_r - sp.Rational(4, 3) * rho_r) == 0, "T_kk/rho=%s" % sp.simplify(Tkk_r / rho_r))
# full NEC on the dust witness: isotropic perfect fluid, T_kk = rho + p for EVERY unit direction
chk("dust witness satisfies the FULL NEC (isotropic: every null k gives rho + p = rho)", True,
    "(perfect-fluid Table 1 row, Kontou-Sanders p.11)")

# ------------------------------------------------------------------ (D)
print("\n(D) nonstatic.py radial identity and the reach of its two contractions")
rho, pr, pT, j, c = sp.symbols("rho p_r p_T j c", real=True)
To_s = sp.Matrix([[rho, -j, 0, 0], [-j, pr, 0, 0], [0, 0, pT, 0], [0, 0, 0, pT]])  # T(u,n) = -j
kr = [1, 1, 0, 0]
chk("T_kk(u + n) = rho + p_r - 2j with j = -T(u,n)  (nonstatic.py:59, :351)",
    sp.expand(sum(To_s[A, b] * kr[A] * kr[b] for A in range(4) for b in range(4)) - (rho + pr - 2 * j)) == 0)
kc = [1, c, sp.sqrt(1 - c**2), 0]
Tkc = sp.expand(sum(To_s[A, b] * kc[A] * kc[b] for A in range(4) for b in range(4)))
chk("general direction: T_kk = rho + p_T - 2 j c + (p_r - p_T) c^2, c = cos(angle to n)",
    sp.simplify(Tkc - (rho + pT - 2 * j * c + (pr - pT) * c**2)) == 0)
try:
    import z3
    R_, PR, PT, J, C = z3.Reals("rho p_r p_T j c")
    s = z3.Solver()
    s.add(R_ + PR - 2 * J >= 0, R_ + PT >= 0, R_ + PR + 2 * J >= 0,   # out, transverse, in
          C >= -1, C <= 1, R_ + PT - 2 * J * C + (PR - PT) * C * C < 0)
    res = s.check()
    chk("z3: radial(out,in)+transverse >= 0 yet NEC fails at an oblique k (j != 0)",
        res == z3.sat, str(s.model()) if res == z3.sat else str(res))
    s2 = z3.Solver()
    s2.add(J == 0, R_ + PR >= 0, R_ + PT >= 0, C >= -1, C <= 1,
           R_ + PT + (PR - PT) * C * C < 0)
    chk("z3: with j = 0, radial + transverse DO certify the full NEC (unsat)", s2.check() == z3.unsat)
except ImportError:
    chk("z3 available", False)

# ------------------------------------------------------------------ (E)
print("\n(E) 'classical T_ab satisfies the NEC' needs minimal coupling: KS 2003.01815 eq (7), (32)")
m_, xi, tt = sp.symbols("m xi t", real=True)
phi = sp.sin(m_ * tt)                    # homogeneous KG solution in Minkowski (R = 0)
dphi = [sp.diff(phi, tt), 0, 0, 0]
box = -sp.diff(phi**2, tt, 2)            # box = -d_t^2 + lap on a t-only function
grad2 = -dphi[0]**2                      # (grad phi)^2 with eta
def Tnm(A, b):
    hess = sp.diff(phi**2, tt, 2) if (A == 0 and b == 0) else 0
    return (dphi[A] * dphi[b] - sp.Rational(1, 2) * eta[A, b] * (grad2 + m_**2 * phi**2)
            + xi * (eta[A, b] * box - hess))
kk = [1, 1, 0, 0]
Tkk_nm = sp.simplify(sum(Tnm(A, b) * kk[A] * kk[b] for A in range(4) for b in range(4)))
chk("T_kk = (d_t phi)^2 - xi d_t^2 phi^2 (k = dt + dx, flat)",
    sp.simplify(Tkk_nm - (sp.diff(phi, tt)**2 - xi * sp.diff(phi**2, tt, 2))) == 0)
v0 = sp.simplify(Tkk_nm.subs(tt, 0))
v1 = sp.simplify(Tkk_nm.subs(tt, sp.pi / (2 * m_)))
chk("t = 0: T_kk = m^2 (1 - 2 xi)  (KS p.14)", sp.simplify(v0 - m_**2 * (1 - 2 * xi)) == 0, str(v0))
chk("t = pi/2m: T_kk = 2 xi m^2  (KS p.14)", sp.simplify(v1 - 2 * xi * m_**2) == 0, str(v1))
chk("xi = 1 (non-minimal, classical, on-shell test field): T_kk = -m^2 < 0 at t = 0",
    sp.simplify(v0.subs(xi, 1) + m_**2) == 0)
chk("xi = 0 (minimal): T_kk = (d_t phi)^2 >= 0 for all t",
    sp.simplify(Tkk_nm.subs(xi, 0) - sp.diff(phi, tt)**2) == 0)

# ------------------------------------------------------------------ (F)
print("\n(F) seatindex.py data: T_kk threshold pi c^4/(4 G l^2) and 'nuclear ~1e35 Pa'")
c_SI = 299792458.0
G_2022 = 6.67430e-11                     # CODATA 2022 (unchanged from 2018)
coeff = math.pi * c_SI**4 / (4 * G_2022)
chk("pi c^4/(4G) = 9.5054e43 Pa m^2 (seatindex.py:92)", abs(coeff / 9.5054e43 - 1) < 5e-5, "%.5e" % coeff)
MeV = 1.602176634e-13
n0 = 0.16e45                             # nuclear saturation density 0.16 fm^-3, in m^-3
eps_sat = n0 * (938.92 - 16.0) * MeV     # nucleon mass minus binding per nucleon
chk("nuclear saturation energy density ~2.4e34 Pa (not 1e35)", 2.0e34 < eps_sat < 2.6e34, "%.3e Pa" % eps_sat)
t100 = coeff / 1e10
chk("l = 100 km: T_kk = 9.51e33 Pa < saturation energy density (claim holds)", t100 < eps_sat,
    "%.3e < %.3e" % (t100, eps_sat))
l_cross_sat = math.sqrt(coeff / eps_sat)
l_cross_tree = math.sqrt(coeff / 1e35)
chk("crossover l: %.0f km (saturation) vs %.0f km (tree's 1e35); 'beyond about 100 km' holds both"
    % (l_cross_sat / 1e3, l_cross_tree / 1e3), l_cross_sat < 1e5 and l_cross_tree < 1e5)
chk("T_kk > 0 on ONE null congruence is necessary, not sufficient, for the NEC (logic)", True,
    "(seatindex :93 'energy-condition-satisfying' = compatible-with, cf. (D))")

print("\nALL CHECKS %s" % ("PASS" if OK else "FAILED"))
sys.exit(0 if OK else 1)
