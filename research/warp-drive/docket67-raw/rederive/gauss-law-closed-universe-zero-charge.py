#!/usr/bin/env python3
"""DOCKET 67 re-derivation: gauss-law-closed-universe-zero-charge.

Tree's use (research/warp-drive/permute.py:126-130, 337-340): "in a spatially
closed universe the total electric charge is EXACTLY ZERO. Not approximately,
not by observation -- FORCED, by topology."  permute.total_charge_forced_zero
returns bool(closed): hardcoded, not computed.

Checks (every one computed here; exit 1 if any expectation fails):
 D1  T^3, untwisted: int over the flat 3-torus of div E = 0 for a generic
     smooth periodic E (sympy, symbolic Fourier coefficients).
 D2  S^3, round: int sqrt(h) div_h E = 0 for a smooth non-gradient field
     built from an R^4 vector field projected tangent (sympy).
 D3  S^3 point charge: the radial field of a charge q at the north pole has
     constant flux q through every chi-sphere, so it forces -q at the
     antipode (sympy).  A single charge cannot be placed.
 D4  S^1 x S^2 (charge without charge; pair.py's Wheeler route): E = Q/(4pi)
     d_psi is divergence-free, total source charge = 0, flux through every
     S^2 = Q != 0.  The theorem constrains the SOURCE integral, not flux on a
     non-bounding 2-cycle (sympy).
 D5  Proca (photon mass m): static Gauss law -lap A0 + m^2 A0 = rho.  On T^3
     a uniform rho0 != 0 is solved by A0 = rho0/m^2, E = 0: net charge
     rho0*V != 0 on a compact boundaryless space.  Exactly-zero needs m = 0.
     Proca length for the PDG bound m < 1e-18 eV.
 D6  C-twisted (C* / charge-conjugation-antiperiodic) bundle on S^1 and T^3:
     E(x+L) = -E(x); int div E = -2 * boundary flux != 0.  Explicit field
     carrying net charge q on a compact boundaryless space.
 D7  z3, discrete: on a periodic L^3 lattice (L=3, 81 link variables) the sum
     of lattice divergences is 0 for ALL integer link fields (UNSAT of the
     negation); with C-twisted links across one face, a field with total
     charge 2 exists with integer links (SAT, model printed; total is 2x face flux, so never odd) and charge 1 with real links.  Vacuity guard: the untwisted
     constraint system itself is SAT.
"""
import sys
import sympy as sp

FAIL = []


def chk(label, got, want):
    ok = (got == want)
    print("  [%s] %s: got %s, want %s" % ("ok" if ok else "FAIL", label, got, want))
    if not ok:
        FAIL.append(label)


x, y, z = sp.symbols("x y z", real=True)
TWO_PI = 2 * sp.pi

# ---------------------------------------------------------------- D1
print("D1  flat T^3 = [0,2pi)^3, periodic E")
a = sp.symbols("a0:12", real=True)
Ex = a[0] + a[1] * sp.sin(x + 2 * y) + a[2] * sp.cos(3 * z - x) + a[3] * sp.sin(y) * sp.cos(z)
Ey = a[4] + a[5] * sp.cos(2 * x) * sp.sin(y + z) + a[6] * sp.sin(x - y) + a[7] * sp.cos(y) ** 2
Ez = a[8] + a[9] * sp.sin(z) * sp.cos(x + y) + a[10] * sp.cos(2 * z) + a[11] * sp.sin(x) * sp.sin(y) * sp.sin(z)
div = sp.diff(Ex, x) + sp.diff(Ey, y) + sp.diff(Ez, z)
I1 = sp.simplify(sp.integrate(div, (x, 0, TWO_PI), (y, 0, TWO_PI), (z, 0, TWO_PI)))
chk("int_T3 div E (generic periodic, 12 free coefficients)", I1, 0)
rho_const = sp.Symbol("rho0", positive=True)
# Gauss div E = rho with uniform rho0: integrate -> rho0 * (2pi)^3 must equal 0
chk("uniform rho0 > 0 admissible on T^3 under Maxwell", sp.Eq(rho_const * TWO_PI ** 3, I1) == True, False)

# ---------------------------------------------------------------- D2
print("D2  round S^3, smooth non-gradient tangent field")
chi, th, ph = sp.symbols("chi theta phi", real=True)
X = sp.Matrix([sp.cos(chi), sp.sin(chi) * sp.cos(th), sp.sin(chi) * sp.sin(th) * sp.cos(ph),
               sp.sin(chi) * sp.sin(th) * sp.sin(ph)])  # embedding in R^4
coords = [chi, th, ph]
J = X.jacobian(coords)
h = sp.simplify(J.T * J)  # induced metric diag(1, sin^2 chi, sin^2 chi sin^2 th)
sqrth = sp.sin(chi) ** 2 * sp.sin(th)
chk("induced metric is round", sp.simplify(h - sp.diag(1, sp.sin(chi) ** 2, sp.sin(chi) ** 2 * sp.sin(th) ** 2)),
    sp.zeros(3, 3))
# ambient field W(X) = (X1*X2 + 1, X0**2 - X3, X2*X3, X0 + X1**2) -- no symmetry, not a gradient
W = sp.Matrix([X[1] * X[2] + 1, X[0] ** 2 - X[3], X[2] * X[3], X[0] + X[1] ** 2])
# tangent components V^i = h^{ij} (J^T W)_j
Vlow = J.T * W
hinv = sp.diag(1, 1 / sp.sin(chi) ** 2, 1 / (sp.sin(chi) ** 2 * sp.sin(th) ** 2))
Vup = hinv * Vlow
divh = sum(sp.diff(sqrth * Vup[i], coords[i]) for i in range(3))  # = sqrt(h) div_h V
I2 = sp.integrate(sp.expand(sp.simplify(divh)), (ph, 0, TWO_PI))
I2 = sp.integrate(sp.simplify(I2), (th, 0, sp.pi))
I2 = sp.simplify(sp.integrate(sp.simplify(I2), (chi, 0, sp.pi)))
chk("int_S3 sqrt(h) div V for projected non-gradient field", I2, 0)

# ---------------------------------------------------------------- D3
print("D3  point charge q at the north pole of S^3")
q = sp.Symbol("q", nonzero=True)
Echi = q / (4 * sp.pi * sp.sin(chi) ** 2)  # unit-radius S^3; chi-spheres have area 4 pi sin^2 chi
divE = sp.simplify(sp.diff(sqrth * Echi, chi) / sqrth)
chk("div E = 0 away from the poles", divE, 0)
flux = sp.simplify(Echi * 4 * sp.pi * sp.sin(chi) ** 2)
chk("flux through every chi-sphere", flux, q)
# near chi = pi the outward normal from the south pole is -d_chi: enclosed charge there
south = sp.limit(-Echi * 4 * sp.pi * sp.sin(chi) ** 2, chi, sp.pi, "-")
chk("charge forced at the antipode", sp.simplify(south), -q)
chk("net charge north + south", sp.simplify(q + south), 0)

# ---------------------------------------------------------------- D4
print("D4  S^1 x S^2 (unit S^2), E = Q/(4pi) d_psi: charge without charge")
psi = sp.Symbol("psi", real=True)
Q = sp.Symbol("Q", nonzero=True)
sq4 = sp.sin(th)  # sqrt(h) of dpsi^2 + dOmega^2
Epsi = Q / (4 * sp.pi)
div4 = sp.simplify(sp.diff(sq4 * Epsi, psi) / sq4)
chk("div E = 0 everywhere (rho = 0, total source charge 0)", div4, 0)
flux4 = sp.integrate(sp.integrate(Epsi * sq4, (ph, 0, TWO_PI)), (th, 0, sp.pi))
chk("flux through each S^2 slice", sp.simplify(flux4), Q)

# ---------------------------------------------------------------- D5
print("D5  Proca: -lap A0 + m^2 A0 = rho on T^3")
m = sp.Symbol("m", positive=True)
A0 = rho_const / m ** 2
lhs = -(sp.diff(A0, x, 2) + sp.diff(A0, y, 2) + sp.diff(A0, z, 2)) + m ** 2 * A0
chk("A0 = rho0/m^2, E = -grad A0 = 0 solves Proca Gauss law", sp.simplify(lhs - rho_const), 0)
chk("net charge on T^3 under Proca (rho0 * (2pi)^3)", sp.simplify(rho_const * TWO_PI ** 3) != 0, True)
chk("m -> 0 limit of A0 diverges (Maxwell recovers the constraint)", sp.limit(A0, m, 0, "+"), sp.oo)
hbar_c_eVm = 1.973269804e-7          # CODATA hbar*c in eV m
m_pdg = 1e-18                        # PDG photon-mass upper limit, eV (Ryutov 2007 solar-wind; PDG listing)
lam = hbar_c_eVm / m_pdg
AU = 1.495978707e11
print("     Proca length hbar c / m at m = 1e-18 eV: %.3e m = %.2f AU" % (lam, lam / AU))
chk("Proca length at the PDG bound is finite (bound does not force m = 0)", lam < float("inf"), True)

# ---------------------------------------------------------------- D6
print("D6  C-twisted (antiperiodic) E")
L = sp.Symbol("L", positive=True)
xs = sp.Symbol("s", real=True)
# 1D: charge q at s = L/2 on a circle of length L with E(s+L) = -E(s)
E1 = sp.Piecewise((-q / 2, xs < L / 2), (q / 2, True))
chk("antiperiodicity E(L^-) = -E(0^+)", sp.simplify(E1.subs(xs, L) + E1.subs(xs, 0)), 0)
jump = sp.simplify(E1.subs(xs, 3 * L / 4) - E1.subs(xs, L / 4))
chk("enclosed charge (jump at L/2) = q, the only source", jump, q)
# 3D: antiperiodic-in-x field with half-integer mode on [0,2pi)^3
b = sp.Symbol("b", nonzero=True)
Ex6 = b * sp.cos(x / 2)          # E(x+2pi) = -E(x)
I6 = sp.integrate(sp.diff(Ex6, x), (x, 0, TWO_PI), (y, 0, TWO_PI), (z, 0, TWO_PI))
chk("int div E over C-twisted T^3 = -2 b (2pi)^2", sp.simplify(I6 + 2 * b * TWO_PI ** 2), 0)
chk("net charge on C-twisted T^3 is nonzero", sp.simplify(I6) != 0, True)

# ---------------------------------------------------------------- D7
print("D7  z3: lattice Gauss law on a periodic 3^3 lattice")
try:
    import z3
except ImportError:
    print("  z3 not available; pip install z3-solver")
    FAIL.append("z3 missing")
else:
    N = 3
    idx = [(i, j, k) for i in range(N) for j in range(N) for k in range(N)]
    Evar = {(s, d): z3.Int("E_%d%d%d_%d" % (s + (d,))) for s in idx for d in range(3)}

    def shift(s, d, n):
        t = list(s)
        t[d] = (t[d] + n) % N
        return tuple(t)

    def wrapped_back(s, d):
        return s[d] == 0  # the link entering s from s - e_d crosses the face

    def charge(s, twisted):
        tot = 0
        for d in range(3):
            back = Evar[(shift(s, d, -1), d)]
            sign = -1 if (twisted and d == 0 and wrapped_back(s, d)) else 1
            tot = tot + Evar[(s, d)] - sign * back
        return tot

    Qtot = z3.Sum([charge(s, False) for s in idx])
    so = z3.Solver()
    so.add(Qtot != 0)
    r = so.check()
    chk("untwisted: exists integer link field with total charge != 0", str(r), "unsat")
    sv = z3.Solver()
    sv.add(Qtot == 0)
    chk("vacuity guard: untwisted system satisfiable", str(sv.check()), "sat")
    # vacuity guard 2: a nonzero LOCAL charge is achievable (the claim is not trivially all-zero)
    sv2 = z3.Solver()
    sv2.add(charge(idx[0], False) == 1)
    chk("vacuity guard: nonzero local charge exists untwisted", str(sv2.check()), "sat")
    Qtw = z3.Sum([charge(s, True) for s in idx])
    st = z3.Solver()
    st.add(Qtw == 2)
    rt = st.check()
    chk("C-twisted across the x-face: total charge 2 achievable (integer links)", str(rt), "sat")
    if str(rt) == "sat":
        mdl = st.model()
        nz = [(str(v), mdl[v]) for v in Evar.values() if mdl[v] is not None and mdl[v].as_long() != 0]
        print("     witness nonzero links:", nz[:8])
    st2p = z3.Solver()
    st2p.add(Qtw % 2 != 0)
    chk("C-twisted, integer links: total = 2*(face-crossing flux), never odd", str(st2p.check()), "unsat")
    # real-valued links: any net charge (the continuum D6 case, E = +-q/2)
    Rvar = {k: z3.Real("R_%d%d%d_%d" % (k[0] + (k[1],))) for k in Evar}

    def rcharge(s):
        tot = 0
        for d in range(3):
            back = Rvar[(shift(s, d, -1), d)]
            sign = -1 if (d == 0 and wrapped_back(s, d)) else 1
            tot = tot + Rvar[(s, d)] - sign * back
        return tot
    sr = z3.Solver()
    sr.add(z3.Sum([rcharge(s) for s in idx]) == 1)
    chk("C-twisted, real links: total charge 1 achievable", str(sr.check()), "sat")

print()
if FAIL:
    print("FAILURES:", FAIL)
    sys.exit(1)
print("ALL CHECKS PASS")
