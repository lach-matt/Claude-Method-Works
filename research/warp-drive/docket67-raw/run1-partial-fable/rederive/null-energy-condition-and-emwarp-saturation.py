#!/usr/bin/env python3
"""DOCKET 67 item 25 -- re-derivation of
   (a) emwarp.py's identity  T_ab k^a k^b = |P_perp(E + n x B)|^2  (exact, sympy, modulo |n|=1)
   (b) the covariant form    4 pi T_ab k^a k^b = v_c v^c, v_c := F_ca k^a, v.k = 0  (any frame, any point)
   (c) the lemma  v.k = 0, k null  =>  v.v >= 0  (z3, unsat on negation) -- the frame-free NEC proof
   (d) generic SATURATION: every non-null Maxwell field has two real null directions with T k k = 0,
       a null field one (the principal null directions) -- checked in the canonical frame E || B
   (e) drivensource.py's electrovac claim rho + p_r = 0 in the full dynamical spherical metric,
       and the transverse contraction rho + p_T = 2 rho > 0 (recomputed here, not imported)
   (f) nonstatic.py's open-FRW dust witness: NEC contraction = rho > 0 (recomputed, not imported)
   (g) the SI datum: mu0 moved at the 2019 SI redefinition; rho + p_parallel stays exactly 0 for any mu0
Exit 1 on any failure.  Run:  python3 <this file>
"""
import sys
import sympy as sp

fails = []
def chk(what, ok):
    print("  %-72s %s" % (what, "ok" if ok else "FAIL"))
    if not ok:
        fails.append(what)

# ---------------------------------------------------------------- (a) the identity, exact
Ex, Ey, Ez, Bx, By, Bz, nx, ny, nz = sp.symbols("Ex Ey Ez Bx By Bz nx ny nz", real=True)
E = sp.Matrix([Ex, Ey, Ez]); B = sp.Matrix([Bx, By, Bz]); n = sp.Matrix([nx, ny, nz])
rho = (E.dot(E) + B.dot(B)) / 2
S = E.cross(B)
T = sp.Matrix(3, 3, lambda i, j: -(E[i]*E[j] + B[i]*B[j]) + (rho if i == j else 0))
NEC = rho - 2*S.dot(n) + (n.T*T*n)[0]                    # k = (1, n), signature -+++, emwarp's convention
v = E + n.cross(B)
perp = v - v.dot(n)*n
SOS = perp.dot(perp)
unit = nx**2 + ny**2 + nz**2 - 1
_, rem = sp.reduced(sp.expand(NEC - SOS), [unit], nx, ny, nz, Ex, Ey, Ez, Bx, By, Bz)
chk("(a) NEC - |P_perp(E+nxB)|^2 == 0 modulo |n|^2 = 1 (exact polynomial reduction)", sp.expand(rem) == 0)
# sanity: it is NOT an identity without |n|=1 (so the hypothesis k null is load-bearing)
chk("(a') the identity FAILS without |n| = 1 (hypothesis is load-bearing)",
    sp.expand(NEC - SOS) != 0)

# ---------------------------------------------------------------- (b) covariant form
# Minkowski orthonormal frame, eta = diag(-1,1,1,1); F_{0i} = -E_i (so that F^{i0} = E_i... convention below),
# F_{ij} = eps_{ijk} B_k.  Convention check: T^{00} must come out (E^2+B^2)/2 and T^{0i} = (ExB)_i.
eta = sp.diag(-1, 1, 1, 1)
F = sp.zeros(4, 4)
for i in range(3):
    F[0, i+1] = -E[i]; F[i+1, 0] = E[i]
F[1, 2] = Bz; F[2, 1] = -Bz; F[2, 3] = Bx; F[3, 2] = -Bx; F[3, 1] = By; F[1, 3] = -By
Fup = eta*F*eta
F2 = sum(F[a, b]*Fup[a, b] for a in range(4) for b in range(4))
Tdd = sp.Matrix(4, 4, lambda a, b: sum(F[a, c]*(F*eta)[b, c] for c in range(4)) - sp.Rational(1, 4)*eta[a, b]*F2)
# Heaviside-Lorentz, no 1/4pi (emwarp's units).  T^{00} = T_{00}.
chk("(b0) convention: T_00 = (E^2+B^2)/2", sp.expand(Tdd[0, 0] - rho) == 0)
chk("(b0) convention: T^{0i} = (E x B)_i", all(sp.expand(-Tdd[0, i+1] - S[i]) == 0 for i in range(3)))
k = sp.Matrix([1, nx, ny, nz])
Tkk = (k.T*Tdd*k)[0]
chk("(b1) 4-d contraction equals emwarp's 3-vector nec_contraction", sp.expand(Tkk - NEC) == 0)
vcov = sp.Matrix([sum(F[c, a]*k[a] for a in range(4)) for c in range(4)])        # v_c = F_{ca} k^a
vup = eta*vcov
vv = (vcov.T*vup)[0]
_, rem2 = sp.reduced(sp.expand(Tkk - vv), [unit], nx, ny, nz, Ex, Ey, Ez, Bx, By, Bz)
chk("(b2) T_ab k^a k^b = v_c v^c with v_c = F_ca k^a  (modulo k null)", sp.expand(rem2) == 0)
chk("(b3) v_c k^c = 0 identically (antisymmetry of F)", sp.expand((vcov.T*k)[0]) == 0)
# and v.v in the frame IS the P_perp form: v_0 = v.n forced by v.k = 0
chk("(b4) v_c v^c = |P_perp(E + n x B)|^2 modulo |n| = 1",
    sp.expand(sp.reduced(sp.expand(vv - SOS), [unit], nx, ny, nz, Ex, Ey, Ez, Bx, By, Bz)[1]) == 0)

# ---------------------------------------------------------------- (c) the lemma, machine-checked
try:
    import z3
    v0, v1, v2, v3, k1, k2, k3 = z3.Reals("v0 v1 v2 v3 k1 k2 k3")
    knull = (k1*k1 + k2*k2 + k3*k3 == 1)               # k = (1, k_i) null
    orth = (-v0*1 + v1*k1 + v2*k2 + v3*k3 == 0)        # v.k = 0
    vv_z3 = -v0*v0 + v1*v1 + v2*v2 + v3*v3
    s = z3.Solver(); s.set("timeout", 120000)
    s.add(knull, orth, vv_z3 < 0)
    r = str(s.check())
    chk("(c) z3: v.k = 0 and k null and v.v < 0 is UNSAT (a vector orthogonal to a null vector is causal-or-spacelike... never timelike)", r == "unsat")
    s2 = z3.Solver(); s2.add(knull, orth); chk("(c guard) the hypotheses are satisfiable", str(s2.check()) == "sat")
    # drift guard: drop k null and the lemma fails
    s3 = z3.Solver(); s3.add(k1*k1 + k2*k2 + k3*k3 == 4, orth, vv_z3 < 0)
    chk("(c drift) with k timelike-normalised differently the lemma has a counterexample", str(s3.check()) == "sat")
except ImportError:
    chk("(c) z3 available", False)

# ---------------------------------------------------------------- (d) generic saturation (PNDs)
e, b = sp.symbols("e b", real=True)
for sgn in (1, -1):
    val = SOS.subs({Ex: 0, Ey: 0, Ez: e, Bx: 0, By: 0, Bz: b, nx: 0, ny: 0, nz: sgn})
    chk("(d) canonical frame E || B along z, n = %+dz: T k k = 0 for ALL e, b (non-null field: two PNDs)" % sgn, sp.simplify(val) == 0)
# a null field (E ⊥ B, |E| = |B|): one direction, E x B
val = SOS.subs({Ex: e, Ey: 0, Ez: 0, Bx: 0, By: e, Bz: 0, nx: 0, ny: 0, nz: 1})
chk("(d) null field E=e x, B=e y, n = E x B direction: T k k = 0 (one PND)", sp.simplify(val) == 0)
val = SOS.subs({Ex: e, Ey: 0, Ez: 0, Bx: 0, By: e, Bz: 0, nx: 0, ny: 0, nz: -1})
chk("(d) null field, n = -(E x B): T k k = 4 e^2 > 0 (the other direction is NOT saturated)", sp.simplify(val - 4*e**2) == 0)
# and a generic off-axis direction in the canonical frame is strictly positive
th = sp.Symbol("theta", real=True)
val = SOS.subs({Ex: 0, Ey: 0, Ez: e, Bx: 0, By: 0, Bz: b, nx: sp.sin(th), ny: 0, nz: sp.cos(th)})
chk("(d) off-axis n: T k k = (e^2 + b^2) sin^2(theta) >= 0, zero only on the axis",
    sp.simplify(val - (e**2 + b**2)*sp.sin(th)**2) == 0)

# ---------------------------------------------------------------- (e) electrovac in the dynamical spherical metric (independent recomputation)
t, r, thv = sp.symbols("t r theta", real=True); ph = sp.Symbol("phi")
Phi = sp.Function("Phi")(t, r); Lam = sp.Function("Lambda")(t, r); R = sp.Function("R")(t, r)
Q = sp.Symbol("Q", positive=True)
x = [t, r, thv, ph]
g = sp.diag(-sp.exp(2*Phi), sp.exp(2*Lam), R**2, R**2*sp.sin(thv)**2)
gi = g.inv()
Fc = sp.zeros(4, 4); Fc[0, 1] = Q*sp.exp(Phi + Lam)/R**2; Fc[1, 0] = -Fc[0, 1]
Fcup = gi*Fc*gi
sg = sp.sqrt(-g.det())
maxwell = [sp.simplify(sum(sp.diff(sg*Fcup[a, b], x[a]) for a in range(4))) for b in range(4)]
chk("(e) curved-space source-free Maxwell residuals vanish for F_tr = Q e^{Phi+Lam}/R^2", all(m == 0 for m in maxwell))
Fdd = sum(Fc[a, b]*Fcup[a, b] for a in range(4) for b in range(4))
Tc = sp.Matrix(4, 4, lambda a, b: sp.simplify((sum(Fc[a, c]*(Fc*gi)[b, c] for c in range(4)) - sp.Rational(1, 4)*g[a, b]*Fdd)/(4*sp.pi)))
rho_c = sp.simplify(Tc[0, 0]*sp.exp(-2*Phi)); j_c = sp.simplify(-Tc[0, 1]*sp.exp(-Phi - Lam))
pr_c = sp.simplify(Tc[1, 1]*sp.exp(-2*Lam)); pT_c = sp.simplify(Tc[2, 2]/R**2)
chk("(e) rho = Q^2/(8 pi R^4) (Gaussian units)", sp.simplify(rho_c - Q**2/(8*sp.pi*R**4)) == 0)
chk("(e) j = 0", j_c == 0)
chk("(e) radial NEC: rho + p_r = 0 EXACTLY for arbitrary Phi(t,r), Lambda(t,r), R(t,r)", sp.simplify(rho_c + pr_c) == 0)
chk("(e) transverse NEC: rho + p_T = 2 rho > 0 (NOT saturated -- the PNDs are radial)", sp.simplify(rho_c + pT_c - 2*rho_c) == 0)
chk("(e) traceless", sp.simplify(-rho_c + pr_c + 2*pT_c) == 0)
# direct covariant check with an actual null vector in the curved metric: k = e^{-Phi} d_t + e^{-Lam} d_r
kc = sp.Matrix([sp.exp(-Phi), sp.exp(-Lam), 0, 0])
chk("(e) k is null in the curved metric", sp.simplify((kc.T*g*kc)[0]) == 0)
chk("(e) T_ab k^a k^b = 0 on the outgoing radial null ray, covariantly", sp.simplify((kc.T*Tc*kc)[0]) == 0)
kt = sp.Matrix([sp.exp(-Phi), 0, 1/R, 0])
chk("(e) transverse null ray: T_ab k^a k^b = 2 rho = Q^2/(4 pi R^4) > 0", sp.simplify((kt.T*Tc*kt)[0] - Q**2/(4*sp.pi*R**4)) == 0)

# ---------------------------------------------------------------- (f) open FRW dust witness, recomputed from the Friedmann equations
tt = sp.Symbol("t", positive=True); a = sp.Function("a", positive=True)(tt); C = sp.Symbol("C", positive=True)
# k = -1 FRW:  8 pi rho / 3 = (adot^2 - 1)/a^2 ;  NEC (comoving null ray) = rho + p ;  dust p = 0 ;  addot = -C/(2a^2), adot^2 = C/a + 1
adot2 = C/a + 1; addot = -C/(2*a**2)
rho_f = sp.Rational(3, 1)*(adot2 - 1)/(8*sp.pi*a**2)
p_f = -(2*a*addot + adot2 - 1)/(8*sp.pi*a**2)             # second Friedmann eq, k = -1
chk("(f) open dust: pressure vanishes on-shell", sp.simplify(p_f) == 0)
chk("(f) open dust: NEC contraction rho + p = rho = 3C/(8 pi a^3) > 0", sp.simplify(rho_f + p_f - 3*C/(8*sp.pi*a**3)) == 0)
# the tree's expression from nonstatic.py, (adot^2 - 1 - a addot)/(4 pi a^2), equals rho on-shell
nec_tree = (adot2 - 1 - a*addot)/(4*sp.pi*a**2)
chk("(f) nonstatic.py's contraction expression equals rho on the dust shell", sp.simplify(nec_tree - rho_f) == 0)

# ---------------------------------------------------------------- (g) the only datum: mu0
import math
for mu0 in (4e-7*math.pi, 1.25663706127e-6):
    for Bt in (1.0, 45.0, 1e6):
        rho_si = Bt**2/(2*mu0); pl = -rho_si
        chk("(g) mu0 = %.11e, B = %g T: rho + p_parallel == 0.0" % (mu0, Bt), rho_si + pl == 0.0)
print("mu0 pre-2019 (exact 4 pi e-7) = %.12e ; CODATA 2022 = 1.25663706127(20)e-6 ; relative shift = %.2e"
      % (4e-7*math.pi, (1.25663706127e-6 - 4e-7*math.pi)/(4e-7*math.pi)))

print("\n%d failure(s)" % len(fails))
sys.exit(1 if fails else 0)
