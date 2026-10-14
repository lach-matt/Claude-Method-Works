#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of 'coulomb-exterior-field-energy' as drivensource.py uses it.

  drivensource.py:144-158  field energy outside a is Q^2/(8 pi eps0 a); M >= X/a,
                           X = Q^2/(8 pi eps0 c^2), whenever the body's own contribution
                           to M is non-negative; r_c = X/M <= a; sup r_c/a = 1 at mu = 0.
  drivensource.py:162-164  regular centre + rho >= 0  =>  m(r) >= 0 inside.
  drivensource.py:426-433  z3 E2 on the model M_tot = mu + X/a.

What is checked here (nothing in research/ is imported or written):
  A  flat-space Coulomb energy outside a                         (sympy)
  B  RN Misner-Sharp mass in SI; G cancels; r_c = X/M            (sympy)
  C  GR: the AREAL integral of rho outside a is exactly X/a; the
     PROPER-volume integral is larger                           (sympy + numeric)
  D  Israel junction, static thin shell, flat interior:
     M = m0 + Q^2/2a - m0^2/2a   (Casadio 1303.1274 eq 3.14)     (sympy)
  E  ADM (Casadio eq 2.23, isotropic eps) <=> Israel (areal a),
     with a = eps + (m0+M)/2 (Casadio eq 3.2)                    (sympy)
  F  z3: tree's E2 re-run; GR shell bound; ADM-parametrised bound; drift guards
  G  shell stress: the supremum mu = 0 needs p < 0 with sigma = 0 (NEC fails on the shell)
  H  interior: static slice dm/dr = 4 pi r^2 rho from G^t_t    (sympy, from the metric)
  I  data: CODATA 2018 vs 2022 eps0; GR binding correction for the tree's configurations
"""
import math
import sys

import sympy as sp

FAILS = []
NPASS = [0]


def chk(label, got, want=True):
    ok = (got == want) if not isinstance(got, sp.Basic) else (sp.simplify(got - want) == 0 if want is not True else bool(got))
    print(("PASS " if ok else "FAIL ") + label + ("" if ok else "   got=%r want=%r" % (got, want)))
    (NPASS.__setitem__(0, NPASS[0] + 1) if ok else FAILS.append(label))


def near(label, got, want, tol):
    ok = abs(got - want) <= tol
    print(("PASS " if ok else "FAIL ") + "%s  got=%.12g want=%.12g tol=%g" % (label, got, want, tol))
    (NPASS.__setitem__(0, NPASS[0] + 1) if ok else FAILS.append(label))


r, a, Q, eps0, c, G, M = sp.symbols("r a Q epsilon0 c G M", positive=True)

# ---------------------------------------------------------------- A
E = Q / (4 * sp.pi * eps0 * r**2)
U_out = sp.integrate(eps0 / 2 * E**2 * 4 * sp.pi * r**2, (r, a, sp.oo))
chk("A  flat Coulomb energy outside a = Q^2/(8 pi eps0 a)", sp.simplify(U_out - Q**2 / (8 * sp.pi * eps0 * a)) == 0)
X = Q**2 / (8 * sp.pi * eps0 * c**2)

# ---------------------------------------------------------------- B
f_SI = 1 - 2 * G * M / (c**2 * r) + G * Q**2 / (4 * sp.pi * eps0 * c**4 * r**2)
m_SI = sp.simplify(c**2 * r / (2 * G) * (1 - f_SI))
chk("B  RN Misner-Sharp mass (kg) m(r) = M - X/r, G cancels", sp.simplify(m_SI - (M - X / r)) == 0)
rc = sp.solve(sp.Eq(m_SI, 0), r)
chk("B  unique zero r_c = X/M", len(rc) == 1 and sp.simplify(rc[0] - X / M) == 0)

# ---------------------------------------------------------------- C
rho_mass = eps0 / 2 * E**2 / c**2           # T^tt energy density / c^2 (kg m^-3), RN exact
areal = sp.integrate(4 * sp.pi * r**2 * rho_mass, (r, a, sp.oo))
chk("C  GR areal integral of rho outside a = X/a exactly", sp.simplify(areal - X / a) == 0)
dm = sp.diff(m_SI, r)
chk("C  dm/dr = 4 pi r^2 rho (so M - m(a) = X/a is the exterior field energy)", sp.simplify(dm - 4 * sp.pi * r**2 * rho_mass) == 0)
# proper-volume integral numerically, geometric units, a strongly relativistic case
Mg, Qg, ag = 1.0, 0.9, 3.0
fg = lambda x: 1 - 2 * Mg / x + Qg**2 / x**2
import itertools
def quad(fun, lo, hi, n=200000):
    # substitution x = lo/t, t in (0,1]
    s = 0.0
    for k in range(n):
        t = (k + 0.5) / n
        x = lo / t
        s += fun(x) * lo / t**2
    return s / n
prop = quad(lambda x: 4 * math.pi * x**2 * (Qg**2 / (8 * math.pi * x**4)) / math.sqrt(fg(x)), ag, None)
chk("C  proper-volume integral (%.6f) > areal Q^2/2a (%.6f): which measure matters" % (prop, Qg**2 / (2 * ag)), prop > Qg**2 / (2 * ag) + 1e-6)

# ---------------------------------------------------------------- D  (geometric units G = c = 1, Gaussian Q)
m0, Mg_, Qs, as_ = sp.symbols("m0 M Q a", positive=True)
fout = 1 - 2 * Mg_ / as_ + Qs**2 / as_**2
# Israel: sigma = -(1/4 pi a)[sqrt f]; 4 pi a^2 sigma = m0  =>  sqrt(f_out) = 1 - m0/a
Msol = sp.solve(sp.Eq(fout, (1 - m0 / as_)**2), Mg_)
chk("D  Israel static shell: M = m0 + Q^2/2a - m0^2/2a", len(Msol) == 1 and sp.simplify(Msol[0] - (m0 + Qs**2 / (2 * as_) - m0**2 / (2 * as_))) == 0)
Misr = m0 + Qs**2 / (2 * as_) - m0**2 / (2 * as_)
chk("D  M - Q^2/2a = m0 (1 - m0/2a)  [the body's own contribution INCLUDES binding]",
    sp.simplify(Misr - Qs**2 / (2 * as_) - m0 * (1 - m0 / (2 * as_))) == 0)
chk("D  tree's additive model M = mu + X/a is exact with mu := m(a+) = M - Q^2/2a (MS mass at the surface)",
    sp.simplify((Misr - Qs**2 / (2 * as_)) + Qs**2 / (2 * as_) - Misr) == 0)

# ---------------------------------------------------------------- E
e = sp.symbols("epsilon", positive=True)
adm = Mg_**2 + 2 * e * Mg_ - 2 * e * m0 - Qs**2          # Casadio 1303.1274 eq (2.23)
a_of_e = e + (m0 + Mg_) / 2                                # Casadio eq (3.2) using (2.24)
israel_times_2a = 2 * as_ * (Mg_ - m0) - Qs**2 + m0**2
chk("E  Israel(a = eps + (m0+M)/2) == ADM quadratic, identically",
    sp.expand(israel_times_2a.subs(as_, a_of_e) - adm) == 0)
rbar = e * (1 + Mg_ / (2 * e))**2 - Qs**2 / (4 * e)        # Casadio eq (2.6)
chk("E  isotropic->areal (2.6) on the ADM branch gives a = eps + (m0+M)/2",
    sp.simplify((rbar - a_of_e).subs(Qs**2, Mg_**2 + 2 * e * Mg_ - 2 * e * m0)) == 0)
Madm = -e + sp.sqrt(e**2 + 2 * e * m0 + Qs**2)
chk("E  ADM eps -> 0 limit: M -> |Q| (finite; bare mass drops out)", sp.limit(Madm, e, 0) == Qs)
chk("E  ...at areal radius (m0+|Q|)/2 >= r_c = Q^2/2M = |Q|/2", sp.simplify(sp.limit(a_of_e.subs(Mg_, Madm), e, 0) - (m0 + Qs) / 2) == 0)

# ---------------------------------------------------------------- F  z3
try:
    import z3
except ImportError:
    print("z3 missing: pip install z3-solver"); sys.exit(2)


def prove(label, hyps, concl):
    s = z3.Solver(); s.add(*hyps); s.add(z3.Not(concl)); res = s.check()
    chk("F  PROVED  " + label + "  (%s)" % res, res == z3.unsat)


def sat(label, cons):
    s = z3.Solver(); s.add(*cons); res = s.check()
    chk("F  SAT     " + label + "  (%s)" % res, res == z3.sat)


Xz, az, mu, rcz, Mt = z3.Reals("X a mu r_c M_tot")
tree = [Xz > 0, az > 0, mu >= 0, Mt == mu + Xz / az, rcz == Xz / Mt]
sat("guard: tree's shell system", tree)
prove("tree E2: r_c <= a (flat additive model, mu >= 0)", tree, rcz <= az)
sat("tree DRIFT: drop mu >= 0 -> counterexample", [Xz > 0, az > 0, Mt == mu + Xz / az, Mt > 0, rcz == Xz / Mt, rcz > az])

m0z, Mz, Qz, A, ez = z3.Reals("m0 M Q a eps")
gr = [A > 0, Qz > 0, m0z >= 0, Mz == m0z + Qz * Qz / (2 * A) - m0z * m0z / (2 * A)]
sat("guard: GR thin shell system with m0 <= 2a", gr + [m0z <= 2 * A])
prove("GR thin shell (Israel): m0 in [0, 2a] => 2 M a >= Q^2 (r_c <= a)", gr + [m0z <= 2 * A], 2 * Mz * A >= Qz * Qz)
prove("GR thin shell: m0 in (0, 2a) => strict 2 M a > Q^2", gr + [m0z > 0, m0z < 2 * A], 2 * Mz * A > Qz * Qz)
sat("GR DRIFT: m0 > 2a would break it (so the geometry must exclude it)", gr + [m0z > 2 * A, 2 * Mz * A < Qz * Qz])
admz = [ez >= 0, m0z >= 0, Qz > 0, Mz >= 0, Mz * Mz + 2 * ez * Mz - 2 * ez * m0z - Qz * Qz == 0, A == ez + (m0z + Mz) / 2]
sat("guard: ADM-parametrised shell", admz + [ez > 0])
prove("ADM shell, eps >= 0, m0 >= 0: m0 <= 2a automatically", admz, m0z <= 2 * A)
prove("ADM shell, eps >= 0, m0 >= 0: 2 M a >= Q^2 (the tree's bound, areal a)", admz, 2 * Mz * A >= Qz * Qz)
mA = z3.Real("m_a")
prove("general body: M = m(a) + Q^2/2a, m(a) >= 0 => r_c = Q^2/2M <= a",
      [A > 0, Qz > 0, mA >= 0, Mz == mA + Qz * Qz / (2 * A)], 2 * Mz * A >= Qz * Qz)

# ---------------------------------------------------------------- G  shell stress at the supremum
sq = sp.sqrt(fout)
p_shell = sp.Rational(1, 8) / sp.pi * ((sp.diff(fout, as_) / (2 * sq) + sq / as_) - 1 / as_)
p0 = sp.simplify(p_shell.subs(Mg_, Qs**2 / (2 * as_)))     # m0 = 0 => M = Q^2/2a, f_out(a) = 1
chk("G  m0 = 0 shell: sigma = 0 and p = -Q^2/(16 pi a^3) < 0", sp.simplify(p0 + Qs**2 / (16 * sp.pi * as_**3)) == 0)
print("     => sigma + p < 0: the NEC fails on the zero-bare-mass shell; the supremum r_c = a")
print("        (drivensource.py:157-159) is attained only by an NEC-violating shell. Bound unaffected.")

# ---------------------------------------------------------------- H  interior, static slice
t, th, ph = sp.symbols("t theta phi")
Phi = sp.Function("Phi")(r); mm = sp.Function("m")(r)
xs = [t, r, th, ph]
g = sp.diag(-sp.exp(2 * Phi), 1 / (1 - 2 * mm / r), r**2, r**2 * sp.sin(th)**2)
gi = g.inv()
Gam = [[[sum(gi[i, l] * (sp.diff(g[l, j], xs[k]) + sp.diff(g[l, k], xs[j]) - sp.diff(g[j, k], xs[l])) for l in range(4)) / 2
         for k in range(4)] for j in range(4)] for i in range(4)]
def Ric(j, k):
    return sp.simplify(sum(sp.diff(Gam[i][j][k], xs[i]) - sp.diff(Gam[i][j][i], xs[k])
                           + sum(Gam[i][i][l] * Gam[l][j][k] - Gam[i][k][l] * Gam[l][j][i] for l in range(4)) for i in range(4)))
R_ = [[Ric(j, k) for k in range(4)] for j in range(4)]
Rs = sp.simplify(sum(gi[j, k] * R_[j][k] for j in range(4) for k in range(4)))
Gtt = sp.simplify(sum(gi[0, k] * R_[k][0] for k in range(4)) - Rs / 2)
chk("H  G^t_t = -2 m'/r^2  => (G = 8 pi T, rho = -T^t_t) m' = 4 pi r^2 rho on a static slice",
    sp.simplify(Gtt + 2 * sp.diff(mm, r) / r**2) == 0)

# ---------------------------------------------------------------- I  data
C_ = 299792458.0
for lab, e0, want in [("CODATA 2018 (tree)", 8.8541878128e-12, None), ("CODATA 2022", 8.8541878188e-12, None)]:
    Xc = 1.0 / (8 * math.pi * e0 * C_**2)
    near("I  X per C^2 [%s]" % lab, Xc, 5.0e-8, 1e-15)
    X4472 = 4472.0**2 * Xc
    ratio_flat = X4472 / (X4472 + 1.0)
    near("I  r_c/a, 4472 C, 1 m, 1 kg bare, flat model [%s]" % lab, ratio_flat, 0.4999847997, 1e-9)
Gn = 6.67430e-11
Xc = 1.0 / (8 * math.pi * 8.8541878188e-12 * C_**2); X4472 = 4472.0**2 * Xc
bind = Gn * 1.0**2 / (2 * 1.0 * C_**2)                     # G m0^2/(2 a c^2), kg
ratio_gr = X4472 / (X4472 + 1.0 - bind)
print("     GR binding correction G m0^2/(2 a c^2) = %.3e kg; r_c/a GR - flat = %.3e" % (bind, ratio_gr - X4472 / (X4472 + 1.0)))
chk("I  GR binding moves the tree's 1 kg / 1 m datum by < 1e-25", abs(ratio_gr - X4472 / (X4472 + 1.0)) < 1e-25)
print("     where binding matters: m0 = a c^2/G ->", "%.3e kg for a = 1 m" % (C_**2 / Gn))

# ---------------------------------------------------------------- J  later literature: Dillon 1303.2706 eq (27)
# Newtonian 'additive' renormalisation, M0 = 0: M_e(R) = (R/G)(1 - exp(-G e^2/(2R^2))) (c = 1).
# It sits BELOW the exterior field energy e^2/2R for every R (1 - e^-x < x), i.e. r_c/R > 1 in that model.
xg = sp.symbols("x", positive=True)
chk("J  Dillon eq (27) model: M_e < e^2/2R for all R (1 - exp(-x) < x, x > 0)",
    sp.simplify(sp.diff(xg - (1 - sp.exp(-xg)), xg) - (1 - sp.exp(-xg))) == 0 and bool((1 - sp.exp(-xg)).subs(xg, 1) < 1))
chk("J  exact GR (Israel) at m0 = 0 gives M = Q^2/2a exactly -- the Newtonian model is not GR",
    sp.simplify(Misr.subs(m0, 0) - Qs**2 / (2 * as_)) == 0)

print("\n%d PASS, %d FAIL(s)" % (NPASS[0], len(FAILS)))
sys.exit(1 if FAILS else 0)
