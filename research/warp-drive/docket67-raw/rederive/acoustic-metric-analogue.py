#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key 'acoustic-metric-analogue'.

Source READ: M. Visser, "Acoustic black holes: horizons, ergospheres, and Hawking
radiation", CQG 15 (1998) 1767, arXiv gr-qc/9712010, eqs (29), (35), (44)-(45),
(53), (55)-(57), and section 7 ("the constant time spatial slices are completely
flat").

Tree use: research/warp-drive/drivensource.py:204-212, 268-269, 390-391, 578.

Every check prints ok/FAIL; exit 1 on any FAIL.  sympy only.
"""
import sys
import sympy as sp

ok_all = True


def chk(label, got, want=0):
    global ok_all
    g = sp.simplify(got - want) if not isinstance(got, bool) else (got == want)
    good = (g == 0) if not isinstance(g, bool) else g
    ok_all &= bool(good)
    print("  %-74s %s" % (label, "ok" if good else "FAIL  (got %s)" % got))


t, th, ph = sp.symbols("t theta phi", real=True)
r = sp.Symbol("r", positive=True)
rp = r
X = [t, r, th, ph]
rho = sp.Function("rho", positive=True)(r)
c = sp.Function("c", positive=True)(r)
v = sp.Function("v", real=True)(r)


def visser_metric(rho, c, v):
    """Visser eq (29) in spherical coords, purely radial background flow v(r) r-hat:
    ds^2 = (rho/c)[-c^2 dt^2 + (dr - v dt)^2 + r^2 dOmega^2]."""
    k = rho / c
    return sp.Matrix([[k * (-(c**2) + v**2), -k * v, 0, 0],
                      [-k * v, k, 0, 0],
                      [0, 0, k * r**2, 0],
                      [0, 0, 0, k * r**2 * sp.sin(th)**2]])


def W_lab(g):
    """W = s^mu d_mu R on the t = const (lab-time) slice: s the unit radial vector
    tangent to the slice (s^t = 0), R the areal radius sqrt(g_thth)."""
    R = sp.sqrt(g[2, 2])
    s_r = 1 / sp.sqrt(g[1, 1])            # s = (0, s_r, 0, 0), g(s,s)=1
    # s is orthogonal to the slice normal n_mu ~ d_mu t automatically (s^t = 0)
    return sp.simplify(s_r * sp.diff(R, r)), R


print("1. THE METRIC FORM (Visser eq 29) WITH rho/c CONSTANT")
k = sp.Symbol("k", positive=True)
g_gen = visser_metric(rho, c, v)
g_k = g_gen.subs(rho, k * c).doit()
tree = sp.Matrix([[-(c**2) + v**2, -v, 0, 0], [-v, 1, 0, 0],
                  [0, 0, r**2, 0], [0, 0, 0, r**2 * sp.sin(th)**2]])
chk("rho = k c: g = k * [-c^2 dt^2 + (dr - v dt)^2 + r^2 dOmega^2] (tree form)",
    sp.simplify((g_k - k * tree).norm()), 0)

print("\n2. W ON LAB-TIME SLICES")
W_hom, R_hom = W_lab(g_k)
chk("rho/c constant: W = 1 exactly (drivensource.py:205-206)", W_hom, 1)
W_inh, R_inh = W_lab(g_gen)
tree_W = 1 + r * sp.diff(sp.log(sp.sqrt(rho / c)), r)
chk("general rho(r), c(r): W = 1 + r d/dr log sqrt(rho/c) (drivensource.py:211)",
    W_inh, tree_W)
# 3-curvature of the slice: conformally flat, Omega^2 (dr^2 + r^2 dOmega^2)
Om2 = sp.Function("O", positive=True)(r)
h = sp.diag(Om2, Om2 * r**2, Om2 * r**2 * sp.sin(th)**2)
Y = [r, th, ph]
hi = h.inv()
Gam = [[[sum(hi[a, d] * (sp.diff(h[d, b], Y[cc]) + sp.diff(h[d, cc], Y[b])
                         - sp.diff(h[b, cc], Y[d])) for d in range(3)) / 2
         for cc in range(3)] for b in range(3)] for a in range(3)]
Ric = sp.zeros(3)
for b in range(3):
    for cc in range(3):
        s_ = 0
        for a in range(3):
            s_ += sp.diff(Gam[a][b][cc], Y[a]) - sp.diff(Gam[a][b][a], Y[cc])
            for d in range(3):
                s_ += Gam[a][a][d] * Gam[d][b][cc] - Gam[a][cc][d] * Gam[d][b][a]
        Ric[b, cc] = sp.simplify(s_)
R3 = sp.simplify(sum(hi[a, b] * Ric[a, b] for a in range(3) for b in range(3)))
chk("slice 3-Ricci scalar vanishes for Omega^2 constant (EXACTLY FLAT)",
    R3.subs(Om2, k).doit(), 0)
print("       slice 3-Ricci scalar, general Omega^2(r):", sp.simplify(R3))

print("\n3. THE HORIZON |v| = c (radial flow) AND THE MISNER-SHARP MASS")
gi = g_k.inv()
chk("g_tt = 0 exactly at v^2 = c^2 (ergosurface, Visser eq 35)",
    g_k[0, 0].subs(v, c), 0)
# radial null rays: g_tt + 2 g_tr dr/dt + g_rr (dr/dt)^2 = 0
u = sp.Symbol("u")
roots = sp.solve(sp.Eq(g_k[0, 0] + 2 * g_k[0, 1] * u + g_k[1, 1] * u**2, 0), u)
chk("radial null speeds dr/dt = v +- c (sound relative to the flow, Visser eq 87)",
    sp.simplify(sum((x - v)**2 for x in roots)), 2 * c**2)
# Misner-Sharp: 1 - 2m/R = g^{ab} d_a R d_b R  (a scalar)
Rk = sp.sqrt(k) * r
gradR2 = sp.simplify(gi[1, 1] * sp.diff(Rk, r)**2)
chk("1 - 2m/R = 1 - v^2/c^2, so 2m/R = 1 exactly at |v| = c",
    gradR2, 1 - v**2 / c**2)
print("       => trapped (2m/R > 1) iff |v| > c: for radial flow the acoustic")
print("          horizon IS the marginally trapped surface.  W = 1 and the tree's")
print("          identity W^2 = 1 - 2m/R + U^2 then force U^2 = v^2/c^2.")
# U for the normal observer of the lab slice: n^mu = (1, v)/(sqrt(k) c)
n = sp.Matrix([1, v, 0, 0]) / (sp.sqrt(k) * c)
chk("n is a unit timelike normal to t = const",
    sp.simplify((n.T * g_k * n)[0]), -1)
Un = sp.simplify(n[1] * sp.diff(Rk, r))
chk("U = n.grad R = v/c ; identity W^2 = 1 - 2m/R + U^2 holds",
    W_hom**2 - (gradR2 + Un**2), 0)

print("\n4. ERGOSURFACE vs HORIZON WITH SWIRL (Visser eqs 44-45, 2+1 bathtub)")
A, B, cc0 = sp.symbols("A B c0", positive=True)
r_erg = sp.sqrt(A**2 + B**2) / cc0
r_hor = A / cc0
chk("B != 0: ergosphere radius exceeds horizon radius (|v| = c is NOT the horizon)",
    sp.simplify(r_erg**2 - r_hor**2), B**2 / cc0**2)
print("       -> '|v| = c_s is the horizon' needs the flow purely radial (B = 0).")

print("\n5. VISSER'S CANONICAL ACOUSTIC BLACK HOLE (eqs 54-57) -- rho, c constant")
r0, C0 = sp.symbols("r0 c", positive=True)
vc = -C0 * r0**2 / r**2
chk("continuity: rho v r^2 = const with rho constant", sp.diff(vc * r**2, r), 0)
chk("horizon |v| = c at r = r0", sp.Abs(vc).subs(r, r0) - C0, 0)
# ds^2 = -(c^2 - v^2) dt^2 - 2 v dr dt + dr^2  with v = vc (inflow: "dr + c r0^2/r^2 dt")
gtt, gtr, grr = -(C0**2 - vc**2), -vc, 1
f = (r0**2 / r**2) / (C0 * (1 - r0**4 / r**4))

def transformed(sgn):
    # d tau = dt + sgn * f dr   <=>   dt = d tau - sgn * f dr
    s_ = -sgn
    return (gtt, sp.simplify(gtr + s_ * f * gtt), sp.simplify(grr + 2 * s_ * f * gtr + f**2 * gtt))

# Visser's general static transformation, eq (62): d tau = dt + v.dx/(c^2 - v^2)
f62 = sp.simplify(vc / (C0**2 - vc**2))
chk("eq (62) coefficient for this inflow = -(r0^2/r^2)/(c(1 - r0^4/r^4))", f62 + f, 0)
g_tt2, g_tr2, g_rr2 = transformed(-1)
chk("eq (62) sign removes the cross term", g_tr2, 0)
chk("(57) g_rr = 1/(1 - r0^4/r^4)", sp.simplify(g_rr2 - 1 / (1 - r0**4 / r**4)), 0)
chk("(57) g_tautau = -c^2 (1 - r0^4/r^4)", sp.simplify(g_tt2 + C0**2 * (1 - r0**4 / r**4)), 0)
_, g_tr_lit, _ = transformed(+1)
print("  DISCREPANCY (recorded, not a refutation): eq (56) read with its +/- CORRELATED")
print("    to (55)'s leaves cross term g_tau_r = %s != 0; the sign that works is the" % g_tr_lit)
print("    one eq (62) gives (i.e. (56) should read -/+).  (57) is unaffected.")
print("       W = 1 on its lab slices (rho/c constant): a real sonic horizon on W = 1.")

print("\n6. rho/c CONSTANT WITH rho VARYING IS ALSO A LAWFUL BACKGROUND")
kk, p0, rr = sp.symbols("k p0 rho_", positive=True)
p_of_rho = p0 + rr**3 / (3 * kk**2)
chk("c = rho/k with barotropic c^2 = dp/drho  <=>  p = p0 + rho^3/(3k^2)",
    sp.diff(p_of_rho, rr) - (rr / kk)**2, 0)

print("\n7. VISSER'S OWN PG-ANALOGUE (eq 53) IS INHOMOGENEOUS -- W COMPUTED")
GM = sp.Symbol("GM", positive=True)
v53 = -sp.sqrt(2 * GM / rp)
rho53 = rp**sp.Rational(-3, 2)
chk("continuity: rho v r^2 = const for rho ~ r^-3/2, v ~ r^-1/2",
    sp.diff(rho53 * v53 * rp**2, rp), 0)
W53 = sp.simplify(1 + rp * sp.diff(sp.log(sp.sqrt(rho53 / 1)), rp))
chk("c = 1, rho ~ r^-3/2: W = 1/4 on lab slices (off the W = 1 surface, below)",
    W53, sp.Rational(1, 4))

print("\n8. AN INHOMOGENEOUS, EXTERNALLY DRIVEN BACKGROUND WITH W > 1")
al, a0, rho0, cs, K = sp.symbols("alpha a rho0 c_s K", positive=True)
rho8 = rho0 * (rp / a0)**al
v8 = -K / (rho8 * rp**2)                 # continuity
chk("continuity satisfied", sp.diff(rho8 * v8 * rp**2, rp), 0)
h8 = cs**2 * sp.log(rho8 / rho0)         # enthalpy for p = p_inf + c_s^2 rho
Phi8 = -h8 - v8**2 / 2                   # Bernoulli (Visser eq 10), steady flow
chk("steady Bernoulli -d_t psi + h + v^2/2 + Phi = const holds by construction",
    sp.diff(h8 + v8**2 / 2 + Phi8, rp), 0)
W8 = sp.simplify(1 + rp * sp.diff(sp.log(sp.sqrt(rho8 / cs)), rp))
chk("c constant, rho ~ r^alpha: W = 1 + alpha/2 > 1 on lab slices", W8, 1 + al / 2)
print("       -> contraction (W > 1) IS reachable by the analogue once rho/c varies")
print("          (barotropic, inviscid, irrotational, external potential Phi, as")
print("          Visser eq 7 allows).  Outside the tree's stated rho/c-constant scope;")
print("          the tree recorded this case as NOT MEASURED, not as impossible.")

print("\n9. FOLIATION: THE SAME HOMOGENEOUS ACOUSTIC METRIC, ANOTHER SLICING")
tau, chi = sp.symbols("tau chi", positive=True)
# v = 0, rho, c constant: -c^2 dt^2 + dr^2 + r^2 dOmega^2.  Milne: t = tau cosh chi,
# r = c tau sinh chi.
tt = tau * sp.cosh(chi)
rr_ = C0 * tau * sp.sinh(chi)
J = sp.Matrix([[sp.diff(tt, tau), sp.diff(tt, chi)], [sp.diff(rr_, tau), sp.diff(rr_, chi)]])
g2 = J.T * sp.diag(-C0**2, 1) * J
chk("Milne slicing: diagonal, g_tautau = -c^2", sp.simplify(g2[0, 1]), 0)
Wm = sp.simplify(sp.diff(rr_, chi) / sp.sqrt(sp.simplify(g2[1, 1])))
chk("W = cosh(chi) > 1 on tau = const slices of the SAME acoustic geometry",
    Wm, sp.cosh(chi))
print("       -> 'THE ANALOGUE CANNOT EXHIBIT CONTRACTION AT ALL' holds for the lab")
print("          (Newtonian) time foliation; W is a component (nonstatic.py:209-215).")

print("\nRESULT:", "ALL CHECKS PASS" if ok_all else "FAILURES")
sys.exit(0 if ok_all else 1)
