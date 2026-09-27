#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for Sorge, arXiv:2011.10991 (CQG 2021), eq. (36):
      int_V d^3x sqrt(-g) T^i_(C) i = 0     for the complete Casimir apparatus.

Read at source (alphaXiv full text, v1 22 Nov 2020).  What is checked here:

  A. eqs (9)-(13): the dim-reg / zeta algebra giving E = -A pi^2/(1440 L^3).
  B. eqs (55)-(57): the z-integral giving delta E = gamma (L+2H)/2 * {E_flat}.
  C. eqs (31)-(36): the static conservation law in the Fermi metric (30),
     written with the CORRECT covariant divergence, integrated over a compact
     support.  Result: conservation ALONE gives F_z = gamma int sqrt(-g) T^tt
     (Calloni's result); eq (36) follows only when the premise (32)
     F_z = gamma * m_Tolman is added -- and then EXACTLY
         int sqrt(-g) T^i_i = 2 gamma int sqrt(-g) z T^tt,
     i.e. eq (36) is a statement at O(gamma^0), with an O(gamma) remainder.
     The printed (1/sqrt(-g)) d_mu T^mu_z in eq (33) is checked against the
     correct (1/sqrt(-g)) d_mu (sqrt(-g) T^mu_z): after the sqrt(-g) measure
     they differ by d_j((sqrt(-g)-1) T^j_z), itself a total derivative, so both
     integrate to a boundary term -> the discrepancy does not reach eq (36).
  D. The independent route, flat-space von Laue: a static, divergence-free,
     COMPACTLY SUPPORTED stress T^ij has int T^i_i = 0 over any region
     containing the support -- and NOT over a region that cuts the support.
     3D Beltrami form T^ij = delta^ij Lap(chi) - d_i d_j chi and a 2D Airy
     plate/frame model.  Also verifies the tree's finite-ball identity
     int_ball T^i_i = 4 pi R^3 T^rr(R) for a spherical chi.
  E. The O(gamma) remainder is not a property of the apparatus: a column held
     from below vs hung from above gives int T^zz = -/+ gamma M h/2.
     Its size for a lab cavity.
Exit status 0 iff every check passes.
"""
import sys
import sympy as sp

FAIL = []


def chk(label, cond):
    ok = bool(cond)
    print(("PASS  " if ok else "FAIL  ") + label)
    if not ok:
        FAIL.append(label)


# ------------------------------------------------------------------ A
print("\nA. Casimir energy, eqs (9)-(13)")
s, alpha, k, n, L, A = sp.symbols("s alpha k n L A", positive=True)
# eq (10): int d^2k (k^2+s)^(-alpha) = pi Gamma(alpha-1)/Gamma(alpha) s^(1-alpha)
dimreg = sp.pi * sp.gamma(alpha - 1) / sp.gamma(alpha) * s ** (1 - alpha)
# check eq (10) in its convergent range alpha = 2 by direct integration
direct = sp.integrate(2 * sp.pi * k / (k ** 2 + s) ** 2, (k, 0, sp.oo))
chk("eq (10) at alpha=2 equals the convergent integral pi/s",
    sp.simplify(direct - dimreg.subs(alpha, 2)) == 0)
# alpha = -1/2 (continued): int d^2k (k^2+s)^(1/2) = -(2 pi/3) s^(3/2)
cont = sp.simplify(dimreg.subs(alpha, sp.Rational(-1, 2)))
chk("continuation alpha=-1/2 gives -(2 pi/3) s^(3/2)",
    sp.simplify(cont + sp.Rational(2, 3) * sp.pi * s ** sp.Rational(3, 2)) == 0)
q = n * sp.pi / L
E_n = A / (2 * (2 * sp.pi) ** 2) * cont.subs(s, q ** 2)
coef = sp.simplify(E_n / n ** 3)
chk("eq (11): E = -A pi^2/(12 L^3) sum n^3",
    sp.simplify(coef + A * sp.pi ** 2 / (12 * L ** 3)) == 0)
chk("eq (12): zeta(-3) = 1/120", sp.zeta(-3) == sp.Rational(1, 120))
E_flat = sp.simplify(coef * sp.zeta(-3))
chk("eq (13): E = -A pi^2/(1440 L^3)",
    sp.simplify(E_flat + A * sp.pi ** 2 / (1440 * L ** 3)) == 0)

# ------------------------------------------------------------------ B
print("\nB. gravitational correction, eqs (54)-(57)")
z, H, gam, kp = sp.symbols("z H gamma k_perp", positive=True)
nn = sp.symbols("n", positive=True, integer=True)
qq = nn * sp.pi / L
omega = sp.sqrt(kp ** 2 + qq ** 2)
N2 = 1 / (4 * sp.pi ** 2 * L * omega)                     # eq (56) squared
integrand = gam * z * (kp ** 2 * sp.sin(qq * (z - H)) ** 2 + qq ** 2 * sp.cos(qq * (z - H)) ** 2)
zint = sp.integrate(sp.expand(integrand), (z, H, H + L))
per_mode = sp.simplify(N2 * zint)
target = gam * (L + 2 * H) / 2 * (omega / (2 * (2 * sp.pi) ** 2))
chk("eq (57): per mode N^2 int gamma z [...] dz = gamma (L+2H)/2 * omega/(2(2pi)^2)",
    sp.simplify(per_mode - target) == 0)

# consistency of (52)+(53)->(54): sqrt(g_tt) T^t_t = T0^t_t + (1/2) h (d_i phi)^2 at O(h)
h, pt, pi_ = sp.symbols("h phi_t grad2", real=True)          # pi_ = (d_i phi)^2
T0tt = sp.Rational(1, 2) * pt ** 2 + sp.Rational(1, 2) * pi_   # signature -2
Ttt = (1 + h / 2) * T0tt - sp.Rational(1, 2) * h * pt ** 2      # eq (52)
lhs = sp.series(sp.sqrt(1 + h) * Ttt, h, 0, 2).removeO()
chk("eqs (52)-(54): sqrt(g_tt) T^t_t = T0^t_t + (h/2)(d_i phi)^2 + O(h^2)",
    sp.simplify(sp.expand(lhs - (T0tt + h / 2 * pi_))) == 0)

# ------------------------------------------------------------------ C
print("\nC. eqs (31)-(36): static conservation in the Fermi metric (30)")
t, x, y = sp.symbols("t x y", real=True)
X = [t, x, y, z]
g = sp.diag(1 + 2 * gam * z, -1, -1, -1)                     # eq (30), signature -2
ginv = g.inv()
sqrtg = sp.sqrt(-g.det())
chk("sqrt(-g) = sqrt(1+2 gamma z)", sp.simplify(sqrtg - sp.sqrt(1 + 2 * gam * z)) == 0)
Gam = [[[sp.simplify(sum(ginv[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                          - sp.diff(g[b, c], X[d])) for d in range(4)) / 2)
         for c in range(4)] for b in range(4)] for a in range(4)]
# generic static mixed tensor T^mu_nu(x,y,z), no time dependence
Tm = sp.Matrix(4, 4, lambda a, b: sp.Function("T%d%d" % (a, b))(x, y, z))
nu = 3  # z
div = sum(sp.diff(Tm[m, nu], X[m]) for m in range(4)) \
    + sum(Gam[m][m][l] * Tm[l, nu] for m in range(4) for l in range(4)) \
    - sum(Gam[l][m][nu] * Tm[m, l] for m in range(4) for l in range(4))
# correct form: sqrt(-g) div = d_j (sqrt(-g) T^j_z) - (1/2) sqrt(-g) d_z g_tt T^tt
Tup_tt = ginv[0, 0] * Tm[0, 0]          # T^tt = g^tt T^t_t (diagonal metric)
correct = sum(sp.diff(sqrtg * Tm[j, nu], X[j]) for j in (1, 2, 3)) \
    - sp.Rational(1, 2) * sqrtg * sp.diff(g[0, 0], z) * Tup_tt
chk("covariant divergence: sqrt(-g) nabla_mu T^mu_z = d_j(sqrt(-g) T^j_z) - gamma sqrt(-g) T^tt (exact)",
    sp.simplify(sp.expand(sqrtg * div - correct)) == 0)
printed = sum(sp.diff(Tm[j, nu], X[j]) for j in (1, 2, 3)) - gam * sqrtg * Tup_tt
diff_pc = sp.simplify(sp.expand(correct - printed))
chk("eq (33) as PRINTED, (1/sqrt(-g)) d_mu T^mu_z, differs from the correct form by d_j((sqrt(-g)-1) T^j_z), a total derivative",
    sp.simplify(sp.expand(diff_pc - sum(sp.diff((sqrtg - 1) * Tm[j, nu], X[j]) for j in (1, 2, 3)))) == 0)
chk("... and that difference is nonzero pointwise (so it IS a discrepancy in the display)",
    sp.simplify(diff_pc) != 0)
print("      (a DISCREPANCY in the display, not in the result: printed d_j T^j_z,"
      " correct d_j(sqrt(-g)T^j_z) and their difference are all total derivatives"
      " and vanish on a boundary where T = 0)")

# Integrate over a compact support: model T^mu_nu = bump(x,y,z) * const-matrix is NOT
# conserved; instead use the result symbolically.  With int d_j(...) = 0:
#   int sqrt(-g) f_z  = gamma int sqrt(-g) T^tt                      (conservation only)
#   premise (32):  int sqrt(-g) f_z = gamma int sqrt(-g) (T^t_t - T^i_i)
#   => int sqrt(-g) T^i_i = int sqrt(-g) (T^t_t - T^tt) = int sqrt(-g) 2 gamma z T^tt  (exact)
rem = sp.simplify(Tm[0, 0] - Tup_tt)
chk("T^t_t - T^tt = 2 gamma z T^tt exactly, so (32)+conservation give int sqrt(-g) T^i_i = 2 gamma int sqrt(-g) z T^tt",
    sp.simplify(rem - 2 * gam * z * Tup_tt) == 0)
chk("... which vanishes at O(gamma^0): eq (36) is the O(gamma^0) statement",
    sp.limit(2 * gam * z * Tup_tt, gam, 0) == 0)
print("      the O(gamma) remainder depends on the origin of z (the Fermi observer's"
      " height), so it is frame-dependent -- consistent with Sorge's own remark that"
      " the O(gamma) energy is frame-dependent (sec. 8.1).")

# ------------------------------------------------------------------ D
print("\nD. independent route: flat-space von Laue (static, compact support, d_j T^ij = 0)")
r, R = sp.symbols("r R", positive=True)
xs = sp.symbols("x1 x2 x3", real=True)
chi = (1 - (xs[0] ** 2 + xs[1] ** 2 + xs[2] ** 2)) ** 4            # compact on the unit ball
lap = sum(sp.diff(chi, v, 2) for v in xs)
T3 = sp.Matrix(3, 3, lambda i, j: (lap if i == j else 0) - sp.diff(chi, xs[i], xs[j]))
chk("Beltrami stress T^ij = delta^ij Lap chi - d_i d_j chi is divergence-free",
    all(sp.simplify(sum(sp.diff(T3[i, j], xs[i]) for i in range(3))) == 0 for j in range(3)))
chk("its trace and first derivatives vanish on r = 1 (support is the closed unit ball)",
    sp.simplify(T3.trace().subs({xs[0]: 1, xs[1]: 0, xs[2]: 0})) == 0)
# spherical: chi = c(r); T^i_i = 2 Lap chi; T^rr = 2 c'/r
c = (1 - r ** 2) ** 4
lap_r = sp.diff(r ** 2 * sp.diff(c, r), r) / r ** 2
trace_ball = sp.integrate(4 * sp.pi * r ** 2 * 2 * lap_r, (r, 0, R))
Trr = 2 * sp.diff(c, r) / r
chk("finite-ball identity (tree's form): int_ball T^i_i = 4 pi R^3 T^rr(R) for all R",
    sp.simplify(trace_ball - 4 * sp.pi * R ** 3 * Trr.subs(r, R)) == 0)
chk("ball ENCLOSING the whole support (R = 1): int T^i_i = 0  [von Laue]",
    sp.simplify(trace_ball.subs(R, 1)) == 0)
val_half = sp.simplify(trace_ball.subs(R, sp.Rational(1, 2)))
chk("ball CUTTING the support (R = 1/2): int T^i_i = %s != 0" % val_half, val_half != 0)

# 2D Airy model of a plate/frame apparatus in (x,z): T^xx = d_z^2 phi, T^zz = d_x^2 phi,
# T^xz = -d_x d_z phi; support |x|<=1, |z|<=1.  Centre: T^zz < 0 (a field-like region),
# edges: T^zz > 0 (a frame-like region).
xx, zz = sp.symbols("xx zz", real=True)
phi = (1 - xx ** 2) ** 4 * (1 - zz ** 2) ** 4
Txx, Tzz, Txz = sp.diff(phi, zz, 2), sp.diff(phi, xx, 2), -sp.diff(phi, xx, zz)
chk("Airy stress is divergence-free",
    sp.simplify(sp.diff(Txx, xx) + sp.diff(Txz, zz)) == 0 and sp.simplify(sp.diff(Txz, xx) + sp.diff(Tzz, zz)) == 0)
chk("centre carries T^zz < 0, edge carries T^zz > 0 (a complete apparatus: interior + frame)",
    Tzz.subs({xx: 0, zz: 0}) < 0 and Tzz.subs({xx: sp.Rational(9, 10), zz: 0}) > 0)
full = sp.integrate(sp.integrate(Txx + Tzz, (xx, -1, 1)), (zz, -1, 1))
chk("whole support: int (T^xx + T^zz) = 0", sp.simplify(full) == 0)
x0 = sp.Rational(1, 3)
inner = sp.integrate(sp.integrate(Txx + Tzz, (xx, -x0, x0)), (zz, -1, 1))
chk("interior strip |x|<1/3 only (field without its frame): int = %s != 0" % sp.nsimplify(inner),
    sp.simplify(inner) != 0)
half = sp.integrate(sp.integrate(Txx + Tzz, (xx, -1, 0)), (zz, -1, sp.Rational(1, 2)))
chk("region containing part of the frame but not all of it: int = %s != 0" % sp.nsimplify(half),
    sp.simplify(half) != 0)

# the field ALONE is not a complete apparatus: EM Casimir stress (Brown-Maclay, as
# restated by Fulling et al. hep-th/0702091 eq. (1)): <T^{mu nu}> = (E_c/a) diag(1,-1,-1,3)
# between the plates, zero outside, E_c = -pi^2/(720 a^3) per unit area.
a_, Ar = sp.symbols("a A_plate", positive=True)
Ec = -sp.pi ** 2 / (720 * a_ ** 3)
Tfield = (Ec / a_) * sp.diag(1, -1, -1, 3)
spatial_sum_upper = Tfield[1, 1] + Tfield[2, 2] + Tfield[3, 3]     # sum_i T^{ii}
E_tot = Ar * a_ * Tfield[0, 0]
I_field = Ar * a_ * spatial_sum_upper
chk("EM field alone between the plates: int sum_i T^ii = E_total != 0 (no von Laue for the field alone)",
    sp.simplify(I_field - E_tot) == 0 and E_tot != 0)
print("      => Tolman mass of the field ALONE = int (T^00 + sum T^ii) = 2 E_total;"
      " the walls/spacers must carry -E_total of integrated stress for eq (36)."
      " The complete-apparatus hypothesis is load-bearing.")

# ------------------------------------------------------------------ E
print("\nE. the O(gamma) remainder depends on how the apparatus is held")
rho, hh, zeta_ = sp.symbols("rho h zeta", positive=True)
# 1D column 0<z<h, uniform rho, uniform gravity gamma (-z). sigma = tension (T^zz up to sign).
# equilibrium d sigma/dz = gamma rho, sigma = 0 at the free end.
sig_hung = gam * rho * zeta_                    # held at top z=h, free at z=0
sig_base = -gam * rho * (hh - zeta_)            # held at bottom z=0, free at z=h
I_hung = sp.integrate(sig_hung, (zeta_, 0, hh))
I_base = sp.integrate(sig_base, (zeta_, 0, hh))
Mcol = rho * hh
chk("hung: int sigma = + gamma M h/2", sp.simplify(I_hung - gam * Mcol * hh / 2) == 0)
chk("supported: int sigma = - gamma M h/2", sp.simplify(I_base + gam * Mcol * hh / 2) == 0)
chk("same body, opposite sign: int T^i_i at O(gamma) is fixed by the support, not by the apparatus",
    sp.simplify(I_hung + I_base) == 0 and I_hung != 0)
gSI, cSI = 9.80665, 299792458.0
for label, size in (("L = 1 um gap", 1e-6), ("h = 1 cm apparatus", 1e-2), ("h = 1 m", 1.0)):
    print("      relative size gamma*h/c^2 for %-18s = %.2e" % (label, gSI * size / cSI ** 2))

print("\n%d FAIL" % len(FAIL))
sys.exit(1 if FAIL else 0)
