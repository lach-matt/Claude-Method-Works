#!/usr/bin/env python3
"""DOCKET 67, result 11/286 -- frobenius-theorem, re-derivation.

What the tree (research/warp-drive/foliation.py:104-116, V5/V6 at :658-674)
uses: for the chart  g = -e^{2Phi}dt^2 + e^{2Lambda}dr^2 + R^2 dOmega^2, with
Phi, Lambda, R functions of (t,r), the field  u' = cosh(w) u + sinh(w) n  is unit
timelike and twist-free, u'_[a d_b u'_c] = 0, for ANY w(t,r); and, by the
Frobenius theorem, therefore hypersurface orthogonal (the normal of a foliation).

This script checks, independently of foliation.py (nothing imported from it):

  C1  the twist computed with COVARIANT derivatives equals the twist computed
      with PARTIAL derivatives (the Christoffel symbols cancel under [abc]) --
      the tree's 'd_b' at :111 is legitimate for a torsion-free connection.
  C2  all 64 components of u'_[a nabla_b u'_c] vanish for symbolic w(t,r).
  C3  u'.u' = -1 for every w.
  C4  the CONVERSE direction in the concrete case the tree leans on: for
      Schwarzschild in the Schwarzschild chart and the rapidity w that boosts
      the static observer to the generalised Painleve-Gullstrand observer of
      energy E, an explicit integrating factor exists -- u'_a = -f d_a tau with
      f = 1/sqrt(1+2E) ... exhibited and verified, so the foliation Frobenius
      promises is constructed, not assumed, for this family.
  C5  the general 2-dimensional case: for u'_a with components only along
      (t,r), depending only on (t,r), the kernel of u' is a 1-dimensional
      distribution, which is integrable by ODE existence alone; we verify
      symbolically that the vector s = sinh(w) u + cosh(w) n spans that kernel
      (u'_a s^a = 0) and is unit spacelike, so the leaves are its integral
      curves times the sphere.
  C6  VACUITY GUARD: the twist test is not identically zero for every unit
      timelike field.  A field with a phi-component (rigidly rotating observers
      in Minkowski, u = gamma(d_t + Omega d_phi)) has NONZERO twist.  This is
      also the hypothesis the tree's word 'spherically symmetric' at :113
      carries: the field must have NO angular components, not merely (t,r)-
      dependent components.
  C7  HYPOTHESIS-DRIFT PROBE: a field whose components depend only on (t,r)
      but which carries a phi-component (so is (t,r)-dependent yet NOT
      SO(3)-invariant) has nonzero twist in general -- so 'spherically
      symmetric' must mean SO(3)-invariant (zero angular components), which is
      what the tree's construction u' = cosh w u + sinh w n actually enforces.

Exit 0 iff every check passes.  stdlib + sympy only.
"""
import sys
import itertools
import sympy as sp

fails = []


def check(label, cond):
    print(("PASS " if cond else "FAIL ") + label)
    if not cond:
        fails.append(label)


def christoffel(g, x):
    gi = g.inv()
    n = len(x)
    Gam = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                Gam[a][b][c] = sp.simplify(sum(
                    gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                                - sp.diff(g[b, c], x[d])) for d in range(n)) / 2)
    return Gam


def twist_partial(uc, x):
    n = len(x)
    T = {}
    for a, b, c in itertools.product(range(n), repeat=3):
        T[(a, b, c)] = (uc[a] * (sp.diff(uc[c], x[b]) - sp.diff(uc[b], x[c]))
                        + uc[b] * (sp.diff(uc[a], x[c]) - sp.diff(uc[c], x[a]))
                        + uc[c] * (sp.diff(uc[b], x[a]) - sp.diff(uc[a], x[b])))
    return T


def twist_covariant(uc, x, Gam):
    n = len(x)

    def nab(b, c):  # nabla_b u_c
        return sp.diff(uc[c], x[b]) - sum(Gam[d][b][c] * uc[d] for d in range(n))
    T = {}
    for a, b, c in itertools.product(range(n), repeat=3):
        T[(a, b, c)] = (uc[a] * (nab(b, c) - nab(c, b))
                        + uc[b] * (nab(c, a) - nab(a, c))
                        + uc[c] * (nab(a, b) - nab(b, a)))
    return T


# ------------------------------------------------------------- the chart
t, r, th, ph = sp.symbols("t r theta phi", real=True)
x = [t, r, th, ph]
Phi = sp.Function("Phi")(t, r)
Lam = sp.Function("Lambda")(t, r)
R = sp.Function("R")(t, r)
g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R**2, R**2 * sp.sin(th)**2)
Gam = christoffel(g, x)

w = sp.Function("w")(t, r)
u = sp.Matrix([sp.exp(-Phi), 0, 0, 0])
n_ = sp.Matrix([0, sp.exp(-Lam), 0, 0])
up = sp.cosh(w) * u + sp.sinh(w) * n_
uc = g * up

# C1 covariant == partial twist, component by component
Tp = twist_partial(uc, x)
Tc = twist_covariant(uc, x, Gam)
c1 = all(sp.simplify(Tp[k] - Tc[k]) == 0 for k in Tp)
check("C1  covariant twist == partial twist (Christoffels cancel), 64 comps", c1)

# C2 all 64 covariant components vanish for arbitrary w(t,r)
bad = sum(1 for k in Tc if sp.simplify(Tc[k]) != 0)
check("C2  u'_[a nabla_b u'_c] = 0, w(t,r) arbitrary: nonzero components = %d" % bad, bad == 0)

# C3 unit timelike
check("C3  u'.u' = -1 for every w", sp.simplify((up.T * g * up)[0, 0] + 1) == 0)

# C5 kernel of u' is spanned by s = sinh w u + cosh w n, unit spacelike
s = sp.sinh(w) * u + sp.cosh(w) * n_
check("C5a u'_a s^a = 0 (s spans the (t,r)-kernel of u')",
      sp.simplify((uc.T * s)[0, 0]) == 0)
check("C5b s.s = +1", sp.simplify((s.T * g * s)[0, 0] - 1) == 0)
# the kernel of a 1-form on the 2-d (t,r) quotient is 1-dimensional: the
# angular directions are also in the kernel (u'_theta = u'_phi = 0), so the
# full kernel is span{s, d_theta, d_phi}; [d_theta, s] and [d_phi, s] vanish
# because s has (t,r) components depending on (t,r) only:
lie_ok = all(sp.simplify(sp.diff(s[i], th)) == 0 and sp.simplify(sp.diff(s[i], ph)) == 0
             for i in range(4))
check("C5c [d_theta, s] = [d_phi, s] = 0 (kernel is involutive, directly)", lie_ok)

# ----------------------------------------------- C4 explicit integrating factor
# Schwarzschild, static chart: Phi = -Lambda = (1/2) ln(1-2M/r), R = r.
M, E = sp.symbols("M E", positive=True)
f_ = 1 - 2 * M / r
gS = sp.diag(-f_, 1 / f_, r**2, r**2 * sp.sin(th)**2)
# generalised PG observer (foliation.py V7 family): energy per unit mass
# sqrt(1+2E), radial infall speed v = sqrt(2M/r + 2E) w.r.t. the static frame
# (as measured in the static frame's proper units: dr/dtau = -v).
# Boost rapidity w from the static observer: cosh w = sqrt(1+2E)/sqrt(f),
# sinh w = -sqrt(2M/r+2E)/sqrt(f) (ingoing).
k = sp.sqrt(1 + 2 * E)
v = sp.sqrt(2 * M / r + 2 * E)
uS = sp.Matrix([1 / sp.sqrt(f_), 0, 0, 0])
nS = sp.Matrix([0, sp.sqrt(f_), 0, 0])
chw = k / sp.sqrt(f_)
shw = -v / sp.sqrt(f_)
check("C4a cosh^2 w - sinh^2 w = 1 for the PG rapidity",
      sp.simplify(chw**2 - shw**2 - 1) == 0)
upS = chw * uS + shw * nS
ucS = gS * upS
# the candidate time function: tau = t + int v/(f k) dr  (generalised PG time
# up to a constant factor).  Its gradient should be proportional to -u'_a.
dtau = sp.Matrix([1, v / (f_ * k), 0, 0])   # d_a tau, with d_r tau = v/(f k)
ratio = [sp.simplify(-ucS[i] / dtau[i]) for i in (0, 1)]
check("C4b u'_a = -f(r) d_a tau with f = %s (t and r components agree)" % ratio[0],
      sp.simplify(ratio[0] - ratio[1]) == 0 and sp.simplify(ratio[0] - k) == 0)
# so the integrating factor is the CONSTANT k = sqrt(1+2E): u' = -k dtau, and
# the leaves tau = const are the generalised Painleve-Gullstrand slices.
TcS = twist_covariant(ucS, x, christoffel(gS, x))
check("C4c and that field's twist vanishes (consistency with C2)",
      all(sp.simplify(TcS[kk]) == 0 for kk in TcS))

# ------------------------------------------------ C6 vacuity guard, C7 probe
# Minkowski in cylindrical coordinates (t, rho, z, phi): rigid rotation.
rho, z, Om = sp.symbols("rho z Omega", positive=True)
xM = [t, rho, z, ph]
gM = sp.diag(-1, 1, 1, rho**2)
gam = 1 / sp.sqrt(1 - Om**2 * rho**2)
uR = sp.Matrix([gam, 0, 0, gam * Om])
ucR = gM * uR
check("C6a rigid rotor is unit timelike", sp.simplify((uR.T * gM * uR)[0, 0] + 1) == 0)
TR = twist_covariant(ucR, xM, christoffel(gM, xM))
nz = sum(1 for kk in TR if sp.simplify(TR[kk]) != 0)
check("C6b VACUITY GUARD: rigid rotor has NONZERO twist (components != 0: %d)" % nz, nz > 0)

# C7: in the spherical chart, a (t,r)-dependent field WITH a phi-component
# (not SO(3)-invariant) -- e.g. Minkowski (Phi=Lam=0, R=r) with
# u = gamma(d_t + Omega d_phi / (r sin theta)) ... use a simple concrete case
gF = sp.diag(-1, 1, r**2, r**2 * sp.sin(th)**2)
a_ = sp.Function("a")(t, r)   # angular velocity profile depending on (t,r) only
gamF = 1 / sp.sqrt(1 - a_**2 * r**2 * sp.sin(th)**2)
uF = sp.Matrix([gamF, 0, 0, gamF * a_])
ucF = gF * uF
check("C7a phi-carrying field is unit timelike", sp.simplify((uF.T * gF * uF)[0, 0] + 1) == 0)
TF = twist_covariant(ucF, x, christoffel(gF, x))
nzF = sum(1 for kk in TF if sp.simplify(TF[kk]) != 0)
check("C7b HYPOTHESIS PROBE: (t,r)-dependent but phi-carrying field has NONZERO "
      "twist (components != 0: %d) -- 'spherically symmetric' must mean "
      "SO(3)-invariant, i.e. no angular components" % nzF, nzF > 0)

print()
print("SUMMARY: %d checks failed" % len(fails))
for f in fails:
    print("  " + f)
sys.exit(1 if fails else 0)
