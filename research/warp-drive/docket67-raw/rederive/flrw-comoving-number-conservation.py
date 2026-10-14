#!/usr/bin/env python3
"""
D67 re-derivation: flrw-comoving-number-conservation.

Tree's use (research/warp-drive/permute.py:42-46): "In FLRW ... the COMOVING
COORDINATE OF A GALAXY DOES NOT CHANGE. ... n a^3 = constant, so the COUNT is
conserved exactly."

Checked here, symbolically (sympy) for general k and general a(t):
  C1  Gamma^i_tt = 0: the curves x^i = const are timelike geodesics
      (so a free comoving observer stays comoving) -- the textbook half.
  C2  a geodesic with nonzero peculiar velocity has a^2 dx/dtau = const != 0:
      its comoving coordinate DOES change; peculiar momentum decays as 1/a.
  C3  del_mu (n u^mu) = 0 with u = d/dt  <=>  d(n a^3)/dt = 0 -- the number law
      follows from a CONSERVED CURRENT, which is an extra hypothesis.
  C4  del_mu T^{mu nu} = 0 (forced by Bianchi) does NOT force del_mu N^mu = 0:
      an explicit particle-creation source Gamma(t) satisfies the first and
      violates the second (n a^3 not constant).
  C5  permute.count_is_conserved measures its own definition: n0 (a0/a)^3 a^3
      simplifies identically to n0 a0^3, so its spread is 0 for ANY a.
  C6  numeric: comoving displacement of a body with the Sun's measured
      peculiar velocity (Fixsen et al. 1996, astro-ph/9605054 p.26: 371 +- 1
      km/s relative to the comoving frame) over the last 1 Gyr, in a flat
      LCDM with the tree's own H0 -- nonzero.
Exit 0 iff every check comes out as stated.
"""
import math
import sys
import sympy as sp

ok = True


def rep(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print("  %-66s %s %s" % (label, "ok" if cond else "FAIL", detail))


t, r, th, ph, k, c = sp.symbols("t r theta phi k c", real=True)
a = sp.Function("a")(t)
X = [t, r, th, ph]
g = sp.diag(-c**2, a**2 / (1 - k * r**2), a**2 * r**2, a**2 * r**2 * sp.sin(th)**2)
gi = g.inv()


def Gam(l, m, n):
    return sp.simplify(sum(gi[l, s] * (sp.diff(g[s, m], X[n]) + sp.diff(g[s, n], X[m])
                                      - sp.diff(g[m, n], X[s])) for s in range(4)) / 2)


# C1
rep("C1 Gamma^i_tt = 0 for i=r,theta,phi (general k, a)",
    all(Gam(i, 0, 0) == 0 for i in (1, 2, 3)))

# C2: flat radial geodesic, affine tau: x'' + 2 (a'/a) t' x' = 0  =>  a^2 x' conserved
tau = sp.symbols("tau")
T = sp.Function("T")(tau)
x = sp.Function("x")(tau)
A = sp.Function("A")
geo_x = sp.diff(x, tau, 2) + 2 * sp.diff(A(T), T) / A(T) * sp.diff(T, tau) * sp.diff(x, tau)
Pc = A(T)**2 * sp.diff(x, tau)
dP = sp.simplify(sp.diff(Pc, tau) - A(T)**2 * geo_x)
rep("C2 d/dtau (a^2 dx/dtau) = a^2 * (geodesic eq)  [so a^2 x' is conserved]", dP == 0)
print("       => x' = P/a^2: P != 0 gives a comoving coordinate that CHANGES;")
print("          physical peculiar momentum a x' = P/a decays but is nonzero.")

# C3: divergence of N^mu = n(t) u^mu, u = (1/c) d/dt normalised: u^t = 1/c
n = sp.Function("n")(t)
sqrtg = sp.sqrt(-g.det())
N = [n / c, 0, 0, 0]
divN = sp.simplify(sum(sp.diff(sqrtg * N[m], X[m]) for m in range(4)) / sqrtg)
target = sp.simplify(sp.diff(n * a**3, t) / (c * a**3))
rep("C3 del_mu(n u^mu) == d(n a^3)/dt / (c a^3)", sp.simplify(divN - target) == 0,
    "div N = %s" % divN)

# C4: creation source: del_mu N^mu = n Gamma  =>  n a^3 = n0 exp(int Gamma dt)
Gm, n0, t0 = sp.symbols("Gamma n0 t0", positive=True)
sol = sp.dsolve(sp.Eq(sp.diff(n, t) + 3 * sp.diff(a, t) / a * n, Gm * n), n)
na3 = sp.simplify(sol.rhs * a**3)
rep("C4 with del.N = Gamma n (Gamma const), n a^3 = C exp(Gamma t) -- not const",
    sp.simplify(sp.diff(na3, t)) != 0, "n a^3 = %s" % na3)
print("       del_mu T^{mu nu} = 0 is a statement about rho, p only; Gamma does not")
print("       appear in it, so Bianchi/Einstein cannot rule the source out.")

# C5: the tree's function is a tautology
aa, a0 = sp.symbols("a a0", positive=True)
tree = n0 * (a0 / aa)**3 * aa**3
rep("C5 permute.comoving_number(n0,a)*a^3 == n0*a0^3 identically", sp.simplify(tree - n0 * a0**3) == 0)

# C6: numeric comoving displacement over last 1 Gyr
H0_kms_Mpc = 67.36          # Planck 2018 VI, via cosmo.py (the tree's pin)
Om, OL = 0.3153, 0.6847     # Planck 2018 VI Table 2 (TT,TE,EE+lowE+lensing)
Mpc = 3.0856775814913673e22
H0 = H0_kms_Mpc * 1e3 / Mpc
Gyr = 1e9 * 365.25 * 86400
v0 = 371e3                   # m/s, Fixsen et al. 1996


def H(a_):
    return H0 * math.sqrt(Om / a_**3 + OL)


# integrate backwards in time from a=1 for 1 Gyr: d a/dt = a H; comoving dchi/dt = v_pec/a,
# with v_pec(a) = v0 * (1/a) (free decay, a0 = 1).  Going back, v_pec was larger.
steps = 200000
dt = -1.0 * Gyr / steps
a_ = 1.0
chi = 0.0
for _ in range(steps):
    def f(ac):
        return ac * H(ac), v0 / ac / ac
    k1 = f(a_)
    k2 = f(a_ + 0.5 * dt * k1[0])
    k3 = f(a_ + 0.5 * dt * k2[0])
    k4 = f(a_ + dt * k3[0])
    a_ += dt * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
    chi += abs(dt) * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
chi_Mpc = chi / Mpc
rep("C6 comoving displacement of a 371 km/s body over last 1 Gyr > 0",
    chi_Mpc > 0.3, "= %.3f comoving Mpc (a went 1 -> %.4f)" % (chi_Mpc, a_))
# with the current Planck 2018 I value 369.82 km/s (NAMED, not read here):
print("       with 369.82 km/s the figure scales to %.3f Mpc -- same conclusion"
      % (chi_Mpc * 369.82 / 371.0))

print("\nRESULT", "ALL CHECKS AS STATED" if ok else "A CHECK FAILED")
sys.exit(0 if ok else 1)
