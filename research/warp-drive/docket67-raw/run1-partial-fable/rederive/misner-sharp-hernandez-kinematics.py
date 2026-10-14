#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of the Misner-Sharp-Hernandez kinematic variables
(U, Gamma) and their boost law under a change of (spacelike) foliation, as used
by research/warp-drive/foliation.py:128-134, :642-656, :800-840.

Sources read at alphaXiv:
  Hayward gr-qc/9408002 eq. (27):  1 - 2E/r = e^{-lambda} (r')^2 - rdot^2,
      stated for ANY spatial hypersurface Sigma (Section IV), tau proper time
      along the normal; "the form actually given by Misner & Sharp [4]".
  Musco, Miller & Rezzolla gr-qc/0412063 eqs. (6),(7),(14): U = D_t R,
      Gamma = D_r R in the COMOVING (fluid) frame, Gamma^2 = 1 + U^2 - 2M/R;
      eqs. (15)-(20),(26): Hernandez-Misner observer time u, f du = a dt - b dr,
      metric -f^2 du^2 - 2 f b dr du + R^2 dOmega^2, D_r = D_k - D_t,
      Gamma = D_k R - U.
  Escriva 2504.05813 eqs. (2.3),(2.5): same definitions, comoving gauge.

Checks (each prints PASS/FAIL; exit 1 on any FAIL):
  C1  orthonormal dyad, boosted dyad is orthonormal for arbitrary w(t,r)
  C2  U = u^a d_a R, Gamma = n^a d_a R  (the tree's V3 convention, PLUS sign)
  C3  boost law U' = ch U + sh G, G' = sh U + ch G  (tree :131-132)
  C4  invariant G'^2 - U'^2 = G^2 - U^2 = g^{ab} d_aR d_bR  (Hayward (27))
  C5  the prose sign at foliation.py:129 ("U = -u^a d_a R") is INCONSISTENT
      with the stated boost law -- a misprint, recorded as a discrepancy
  C6  Frobenius: u'_[a d_b u'_c] = 0 for arbitrary w(t,r)  (tree section 2)
  C7  Hernandez-Misner change of foliation does NOT boost (U, Gamma): in the
      observer-time chart the fluid frame's radial unit vector gives
      n^a d_a R = D_k R - D_t R, i.e. Gamma = D_k R - U (Musco eq. 26),
      so U and Gamma are the SAME fluid-frame scalars in both slicings.
      The slice normal of the H-M slicing is NULL: it is outside the tree's
      class of unit-timelike-normal foliations.
  C8  concrete witness: Schwarzschild, static slicing (U,G) = (0, k) and
      Painleve-Gullstrand slicing (U,G) = (-sqrt(2m/R), 1), computed from the
      metrics, lie on one hyperbola and are joined by the tree's boost.
  C9  z3: O1 (boost preserves the invariant) and O12 (transitivity) re-checked
      independently of the tree's harness; vacuity guard first.
"""
import sys
import sympy as sp

fails = []


def report(tag, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + tag + ("  -- " + detail if detail else ""))
    if not ok:
        fails.append(tag)


t, r, th, ph = sp.symbols("t r theta phi", real=True)
Phi = sp.Function("Phi")(t, r)
Lam = sp.Function("Lambda")(t, r)
R = sp.Function("R")(t, r)
w = sp.Function("w")(t, r)
x = [t, r, th, ph]
g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R**2, R**2 * sp.sin(th)**2)
gi = g.inv()
dR = [sp.diff(R, v) for v in x]

u = sp.Matrix([sp.exp(-Phi), 0, 0, 0])
n = sp.Matrix([0, sp.exp(-Lam), 0, 0])
ch, sh = sp.cosh(w), sp.sinh(w)
up = ch * u + sh * n
npr = sh * u + ch * n


def dot(a, b):
    return sp.simplify((a.T * g * b)[0, 0])


# C1
report("C1 dyad orthonormal, boosted dyad orthonormal (w(t,r) arbitrary)",
       dot(u, u) == -1 and dot(n, n) == 1 and dot(u, n) == 0
       and sp.simplify(dot(up, up) + 1) == 0 and sp.simplify(dot(npr, npr) - 1) == 0
       and sp.simplify(dot(up, npr)) == 0)

# C2
U = sp.exp(-Phi) * sp.diff(R, t)
G = sp.exp(-Lam) * sp.diff(R, r)
Uc = sum(u[a] * dR[a] for a in range(4))
Gc = sum(n[a] * dR[a] for a in range(4))
report("C2 U = +u^a d_aR, Gamma = n^a d_aR (tree V3 convention)",
       sp.simplify(Uc - U) == 0 and sp.simplify(Gc - G) == 0)

# C3
Up = sum(up[a] * dR[a] for a in range(4))
Gp = sum(npr[a] * dR[a] for a in range(4))
report("C3 boost law U' = ch U + sh G, G' = sh U + ch G (foliation.py:131-132)",
       sp.simplify(Up - (ch * U + sh * G)) == 0 and sp.simplify(Gp - (sh * U + ch * G)) == 0)

# C4
gradR2 = sum(gi[a, b] * dR[a] * dR[b] for a in range(4) for b in range(4))
report("C4 G'^2 - U'^2 = G^2 - U^2 = g^{ab} d_aR d_bR  (Hayward (27): 1-2E/r)",
       sp.simplify(Gp**2 - Up**2 - (G**2 - U**2)) == 0
       and sp.simplify(gradR2 - (G**2 - U**2)) == 0)
# Hayward's exact printed form: Phi = 0 gauge (tau proper time along normal)
hay = sp.exp(-2 * Lam) * sp.diff(R, r)**2 - sp.diff(R, t)**2
report("C4b Hayward (27) e^{-lambda}(r')^2 - rdot^2 is the Phi=0 member of C4",
       sp.simplify((G**2 - U**2).subs(Phi, 0) - hay) == 0)

# C5  the prose sign at :129
Ualt = -Uc                     # what the prose line says
Ualt_p = -Up                   # its boosted value
report("C5 prose sign 'U = -u^a d_aR' (foliation.py:129) is a misprint: with it the "
       "stated law fails (residual != 0); code V3 uses +",
       sp.simplify(Ualt_p - (ch * Ualt + sh * G)) != 0
       and sp.simplify(Ualt_p - (ch * Ualt - sh * G)) == 0,
       "with the minus sign the law would read U' = ch U - sh G")

# C6  Frobenius for the boosted normal, w(t,r) free
ulow = g * up
frob_ok = True
for a in range(4):
    for b in range(4):
        for c in range(4):
            expr = (ulow[a] * (sp.diff(ulow[c], x[b]) - sp.diff(ulow[b], x[c]))
                    + ulow[b] * (sp.diff(ulow[a], x[c]) - sp.diff(ulow[c], x[a]))
                    + ulow[c] * (sp.diff(ulow[b], x[a]) - sp.diff(ulow[a], x[b])))
            if sp.simplify(expr) != 0:
                frob_ok = False
report("C6 Frobenius u'_[a d_b u'_c] = 0 for arbitrary w(t,r) (all 64 comps)", frob_ok)

# C7  Hernandez-Misner observer-time chart (Musco eq. 17)
uu, rr = sp.symbols("u r", real=True)
f = sp.Function("f")(uu, rr)
b = sp.Function("b")(uu, rr)
Rh = sp.Function("R")(uu, rr)
h = sp.Matrix([[-f**2, -f * b], [-f * b, 0]])          # (u, r) block
fluid = sp.Matrix([1 / f, 0])                            # comoving fluid, r fixed
nrad = sp.Matrix([-1 / f, 1 / b])                        # solved: n.u=0, n.n=1
d2 = lambda a, c: sp.simplify((a.T * h * c)[0, 0])
Dt_R = sp.diff(Rh, uu) / f                               # Musco (18) applied to R
Dk_R = sp.diff(Rh, rr) / b                               # Musco (19) applied to R
report("C7a H-M chart: fluid 4-velocity unit, radial n unit and orthogonal",
       d2(fluid, fluid) == -1 and d2(nrad, nrad) == 1 and d2(fluid, nrad) == 0)
report("C7b H-M chart: U = fluid^a d_aR = D_t R and Gamma = n^a d_aR = D_k R - D_t R "
       "(Musco (20),(26)) -- (U,Gamma) NOT boosted by the H-M re-slicing",
       sp.simplify(fluid[0] * sp.diff(Rh, uu) + fluid[1] * sp.diff(Rh, rr) - Dt_R) == 0
       and sp.simplify(nrad[0] * sp.diff(Rh, uu) + nrad[1] * sp.diff(Rh, rr) - (Dk_R - Dt_R)) == 0)
# the H-M slice normal is null: slices u = const have normal covector du, norm h^{uu}
hi = h.inv()
report("C7c H-M slice normal is NULL (h^{uu} = 0): outside the tree's unit-timelike-normal class",
       sp.simplify(hi[0, 0]) == 0)

# C8  Schwarzschild witness, computed from the metrics
m, T, Rs = sp.symbols("m T R", positive=True)
k = sp.sqrt(1 - 2 * m / Rs)
# static chart: (t, R)
gs = sp.Matrix([[-(1 - 2 * m / Rs), 0], [0, 1 / (1 - 2 * m / Rs)]])
# Painleve-Gullstrand chart: (T, R)
gpg = sp.Matrix([[-(1 - 2 * m / Rs), sp.sqrt(2 * m / Rs)], [sp.sqrt(2 * m / Rs), 1]])


def UG_from_chart(gm):
    """(U, Gamma) of the chart's own foliation (time = const), areal radius R the
    second coordinate: u_a = -N d_a(time), n the unit vector along R in the slice."""
    gmi = gm.inv()
    N = 1 / sp.sqrt(-gmi[0, 0])
    u_up = gmi * sp.Matrix([-N, 0])          # u^a = g^{ab} u_b
    Uv = sp.simplify(u_up[1])                 # u^a d_a R = u^R
    n_up = sp.Matrix([0, 1 / sp.sqrt(gm[1, 1])])
    # n must be orthogonal to u: in the slice, d_R is tangent, u is normal -> automatic
    Gv = sp.simplify(n_up[1])
    return Uv, Gv, sp.simplify((u_up.T * gm * n_up)[0, 0])


U_s, G_s, o_s = UG_from_chart(gs)
U_pg, G_pg, o_pg = UG_from_chart(gpg)
report("C8a static Schwarzschild slicing: (U, Gamma) = (0, sqrt(1-2m/R))",
       U_s == 0 and sp.simplify(G_s**2 - k**2) == 0 and float(G_s.subs({m: 1, Rs: 4})) > 0 and o_s == 0
       and abs(float((G_s - k).subs({m: 1, Rs: 4}))) < 1e-12,
       "compared by square + sign (sympy leaves sqrt(R/(R-2m)) vs sqrt(1-2m/R) unreduced)")
report("C8b Painleve-Gullstrand slicing: (U, Gamma) = (-sqrt(2m/R), 1)",
       sp.simplify(U_pg + sp.sqrt(2 * m / Rs)) == 0 and sp.simplify(G_pg - 1) == 0 and o_pg == 0)
report("C8c both on the hyperbola Gamma^2 - U^2 = 1 - 2m/R",
       sp.simplify(G_s**2 - U_s**2 - k**2) == 0 and sp.simplify(G_pg**2 - U_pg**2 - k**2) == 0)
c_ = sp.simplify((G_s * G_pg - U_s * U_pg) / k**2)      # tree O12 formula, k^2 = invariant
s_ = sp.simplify((U_pg * G_s - U_s * G_pg) / k**2)
report("C8d the tree's O12 boost joins them: c^2-s^2=1, c U_s + s G_s = U_pg, s U_s + c G_s = G_pg",
       sp.simplify(c_**2 - s_**2 - 1) == 0
       and sp.simplify(c_ * U_s + s_ * G_s - U_pg) == 0
       and sp.simplify(s_ * U_s + c_ * G_s - G_pg) == 0,
       "rapidity: cosh w = %s, sinh w = %s" % (c_, s_))
num = {m: 1, Rs: 4}
print("     numeric at m=1, R=4: cosh w = %.6f, sinh w = %.6f, w = %.6f"
      % (float(c_.subs(num)), float(s_.subs(num)), float(sp.asinh(s_.subs(num)))))

# C9  z3
try:
    import z3
    Uz, Gz, cz, sz, kz = z3.Reals("U G c s k")
    U1, G1, U2, G2 = z3.Reals("U1 G1 U2 G2")
    so = z3.Solver(); so.add(cz * cz - sz * sz == 1, cz > 0, sz != 0)
    report("C9 guard: a non-trivial boost exists", so.check() == z3.sat)
    so = z3.Solver()
    so.add(cz * cz - sz * sz == 1, cz > 0,
           z3.Not((sz * Uz + cz * Gz)**2 - (cz * Uz + sz * Gz)**2 == Gz * Gz - Uz * Uz))
    report("C9 O1 boost preserves Gamma^2 - U^2 (negation unsat)", so.check() == z3.unsat)
    so = z3.Solver()
    so.add(G1 > 0, G2 > 0, kz > 0, G1 * G1 - U1 * U1 == kz, G2 * G2 - U2 * U2 == kz,
           cz * kz == G1 * G2 - U1 * U2, sz * kz == U2 * G1 - U1 * G2,
           z3.Not(z3.And(cz * cz - sz * sz == 1, cz > 0,
                         cz * U1 + sz * G1 == U2, sz * U1 + cz * G1 == G2)))
    report("C9 O12 transitivity on one branch (negation unsat)", so.check() == z3.unsat)
except ImportError:
    report("C9 z3 available", False, "pip install z3-solver")

print()
print("RESULT:", "ALL PASS" if not fails else "FAILED: " + ", ".join(fails))
sys.exit(1 if fails else 0)
