"""
DOCKET 67, result 8/286 -- gr-qc/0009013 (Alcubierre 1994, CQG 11 L73).
Re-derivation of everything closed-form the tree uses, plus a check of the
tree's own numerical pipeline against the metric AS PUBLISHED (x_s = v_s t).

Nothing under research/warp-drive is written: bytecode writing is disabled
before the tree's modules are imported by path.

Checks
  1  typefour.shape == Alcubierre Eq (6); Eq (7) top-hat limit.
  2  Eq (19): Eulerian energy density G^{00}/8pi == -(v_y^2+v_z^2)/(32 pi)
     == -(1/32pi) v_s^2 (rho^2/r_s^2) f'^2, as a SYMBOLIC identity in v(t,x,y,z).
  3  T^{0i} != 0: the Eulerian momentum density in closed form (symbolic), and
     its value in the wall (numeric).  Uniform shift (f == 1) gives T == 0.
  4  NOT STATIC: xi = d_t + v_s d_x is Killing for the published metric with
     constant v_s; (xi ^ dxi)_{txy} = -v_s f_y [1 + v_s^2 (1-f)^2] != 0 off-axis,
     and adding any multiple of the axial Killing field does not cancel it.
  5  NOT SPHERICALLY SYMMETRIC: two curvature invariants have independent
     gradients in the (x', rho) plane, so the surface on which every invariant
     is constant is spanned by xi (timelike here) and the axial rotation --
     it cannot be an SO(3) orbit (a spacelike round 2-sphere).
  6  Eq (12): theta = -Tr K = v_s ((x - x_s)/r_s) f'.  The paper prints x_s
     where x - x_s is meant: a notational discrepancy, recorded, not a refutation.
  7  THE TREE'S PIPELINE.  typefour.d_metric sets d_t g = 0 ("static in these
     coordinates").  The published metric has x_s(t) = v_s t, so d_t g != 0.
     The two spacetimes share rho_E and J_i (Hamiltonian and momentum
     constraints on flat slices see only derivatives of the shift) but not the
     spatial stresses.  Measured: Ricci scalar, T^x_x and T_kk at wall points,
     for the metric as published vs the metric as typefour computes it, and
     anec.py's ANEC integrals recomputed on the published metric.
"""
import sys, os, math
sys.dont_write_bytecode = True
import sympy as sp

TREE = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, TREE)
import typefour as tf          # read-only import, no bytecode written
import anec

t, x, y, z = sp.symbols('t x y z', real=True)
vs = sp.Symbol('v_s', positive=True)
sig, R = sp.Symbol('sigma', positive=True), sp.Symbol('R', positive=True)
X = (t, x, y, z)

results = {}
def rec(k, val): results[k] = val; print("  %-70s %s" % (k, val))

# ---------------------------------------------------------------- 1. shape
rs = sp.Symbol('r_s', positive=True)
f_pub = (sp.tanh(sig * (rs + R)) - sp.tanh(sig * (rs - R))) / (2 * sp.tanh(sig * R))
f_num = sp.lambdify(rs, f_pub.subs({sig: 8, R: 1}), 'math')
print("1. shape function")
d1 = max(abs(f_num(r) - tf.shape(r)) for r in [0.0, 0.3, 0.9, 1.0, 1.1, 2.0, 3.0])
rec("max |Eq(6) - typefour.shape| over 7 radii", d1)
rec("Eq(7) top-hat limit: f(0.5), f(1.5) at sigma=200",
    (float(f_pub.subs({sig: 200, R: 1, rs: 0.5})), float(f_pub.subs({sig: 200, R: 1, rs: 1.5}))))

# -------------------------------------------- generic Einstein tensor for Eq (8)
v = sp.Function('v')(*X)
g = sp.Matrix([[-1 + v**2, -v, 0, 0], [-v, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
gi = g.inv()
assert sp.simplify(g.det()) == -1
Gam = [[[sp.simplify(sum(gi[a, e] * (sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b])
                                     - sp.diff(g[b, c], X[e])) for e in range(4)) / 2)
         for c in range(4)] for b in range(4)] for a in range(4)]
def ricci(b, d):
    s = 0
    for a in range(4):
        s += sp.diff(Gam[a][b][d], X[a]) - sp.diff(Gam[a][a][b], X[d])
        for e in range(4):
            s += Gam[a][a][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][a][b]
    return sp.expand(s)
Ric = sp.Matrix(4, 4, lambda b, d: ricci(b, d))
Rs = sp.expand(sum(gi[b, d] * Ric[b, d] for b in range(4) for d in range(4)))
Gdn = sp.expand(Ric - g * Rs / 2)
Gup = sp.expand(gi * Gdn * gi)          # G^{mu nu}
Gmix = sp.expand(gi * Gdn)              # G^mu_nu
RicSq = sp.expand(sum((gi * Ric * gi)[a, b] * Ric[a, b] for a in range(4) for b in range(4)))

# ------------------------------------------------------------ 2. Eq (19)
print("2. Eq (19), Eulerian energy density, symbolic identity")
vy, vz = sp.diff(v, y), sp.diff(v, z)
eq19 = sp.simplify(Gup[0, 0] / (8 * sp.pi) + (vy**2 + vz**2) / (32 * sp.pi))
rec("G^00/8pi + (v_y^2+v_z^2)/32pi  (must be 0)", eq19)
# and in Alcubierre's variables, with x_s = v_s t and f generic:
F = sp.Function('f')
rs_expr = sp.sqrt((x - vs * t)**2 + y**2 + z**2)
v_true = vs * F(rs_expr)
rho_pub = -(vs**2 / (32 * sp.pi)) * ((y**2 + z**2) / rs_expr**2) * sp.Derivative(F(rs), rs).subs(rs, rs_expr)**2
lhs = (Gup[0, 0] / (8 * sp.pi)).subs(v, v_true).doit()
rec("Eq(19) in f: G^00/8pi - [-(1/32pi) v_s^2 rho^2/r_s^2 f'^2]", sp.simplify(lhs - rho_pub))

# ---------------------------------------------------- 3. momentum density
print("3. T^{0i} (Eulerian momentum density J^i = T^{0i} with alpha = 1)")
J = [sp.simplify(Gup[0, i] / (8 * sp.pi)) for i in (1, 2, 3)]
for i, Ji in zip("xyz", J):
    rec("J^%s generic" % i, Ji)
rec("uniform shift (v = const): G == 0", sp.simplify(Gup.subs(v, sp.Symbol('c'))) == sp.zeros(4, 4))

# ------------------- numeric evaluation machinery: derivative atoms -> numbers
def numeric_evaluator(expr):
    atoms = sorted(expr.atoms(sp.Derivative), key=str)
    syms = {a: sp.Symbol('D%d' % k) for k, a in enumerate(atoms)}
    e2 = expr.subs(syms).subs(v, sp.Symbol('V'))
    fn = sp.lambdify([sp.Symbol('V')] + [syms[a] for a in atoms], e2, 'math')
    return atoms, fn
def make_case(v_expr):
    """returns point -> dict of numeric values for v and each derivative atom"""
    cache = {}
    def deriv_fun(atom):
        if atom not in cache:
            order = []
            for var, n in atom.variable_count:
                order += [var] * n
            cache[atom] = sp.lambdify(X, sp.diff(v_expr, *order), 'math')
        return cache[atom]
    vf = sp.lambdify(X, v_expr, 'math')
    def at(p, atoms):
        try:
            return [vf(*p)] + [deriv_fun(a)(*p) for a in atoms]
        except ZeroDivisionError:      # r_s = 0 exactly (the bubble centre): step off it by 1e-9
            q = (p[0], p[1] + 1e-9, p[2], p[3])
            return [vf(*q)] + [deriv_fun(a)(*q) for a in atoms]
    return at

SIG, RAD, VSN = 8.0, 1.0, 0.5
f_tanh = lambda r: (sp.tanh(SIG * (r + RAD)) - sp.tanh(SIG * (r - RAD))) / (2 * sp.tanh(SIG * RAD))
v_published = VSN * f_tanh(sp.sqrt((x - VSN * t)**2 + y**2 + z**2))   # x_s(t) = v_s t
v_frozen    = VSN * f_tanh(sp.sqrt(x**2 + y**2 + z**2))               # typefour: d_t g = 0
CASES = {"published": make_case(v_published), "frozen(typefour)": make_case(v_frozen)}

T_mix_ev = [[numeric_evaluator(Gmix[a, b] / (8 * sp.pi)) for b in range(4)] for a in range(4)]
Gup_ev = [[numeric_evaluator(Gup[a, b] / (8 * sp.pi)) for b in range(4)] for a in range(4)]
R_ev, RicSq_ev = numeric_evaluator(Rs), numeric_evaluator(RicSq)

def T_mixed(case, p):
    at = CASES[case]
    return [[T_mix_ev[a][b][1](*at(p, T_mix_ev[a][b][0])) for b in range(4)] for a in range(4)]
def T_up(case, p):
    at = CASES[case]
    return [[Gup_ev[a][b][1](*at(p, Gup_ev[a][b][0])) for b in range(4)] for a in range(4)]
def scalar(ev, case, p):
    at = CASES[case]; return ev[1](*at(p, ev[0]))
def gnum(p):
    vv = VSN * tf.shape(math.sqrt(p[1]**2 + p[2]**2 + p[3]**2))
    return [[-1 + vv * vv, -vv, 0, 0], [-vv, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], vv
def T_kk(case, p):
    Tm = T_mixed(case, p); gm, vv = gnum(p)
    Tl = [[sum(gm[m][a] * Tm[a][n] for a in range(4)) for n in range(4)] for m in range(4)]
    k = [1.0, vv + 1.0, 0.0, 0.0]
    return sum(Tl[m][n] * k[m] * k[n] for m in range(4) for n in range(4))

P = (0.0, 0.9, 0.3, 0.0)     # t = 0: the published bubble is centred at the origin
for case in CASES:
    Tu = T_up(case, P)
    rec("[%s] T^{00}, T^{0x}, T^{0y} at (x,y)=(0.9,0.3)" % case, (Tu[0][0], Tu[0][1], Tu[0][2]))
rec("typefour.eulerian_density(0.9,0.3)", tf.eulerian_density((0.9, 0.3, 0.0)))
rec("BBV/Eq(19) closed form at (0.9,0.3)",
    float(rho_pub.subs(F, sp.Lambda(rs, f_tanh(rs))).doit().subs({vs: VSN, t: 0, x: 0.9, y: 0.3, z: 0})))
Tm_tf, _ = tf.stress_mixed((0.9, 0.3, 0.0))
Tm_fr = T_mixed("frozen(typefour)", P)
rec("max |typefour.stress_mixed - sympy(frozen)| at (0.9,0.3)",
    max(abs(Tm_tf[a][b] - Tm_fr[a][b]) for a in range(4) for b in range(4)))

# ------------------------------------------------------------ 4. not static
print("4. staticity: twist of the Killing field xi = d_t + v_s d_x (published metric)")
fF = F(rs_expr)
g_true = g.subs(v, v_true).doit()
xi_up = sp.Matrix([1, vs, 0, 0])
xi_dn = (g_true * xi_up).applyfunc(sp.simplify)
# Killing check: Lie derivative of g along xi vanishes
Lg = sp.zeros(4, 4)
for a in range(4):
    for b in range(4):
        Lg[a, b] = sum(xi_up[c] * sp.diff(g_true[a, b], X[c]) + g_true[c, b] * sp.diff(xi_up[c], X[a])
                       + g_true[a, c] * sp.diff(xi_up[c], X[b]) for c in range(4))
rec("Lie_xi g == 0 (xi is Killing for constant v_s)", sp.simplify(Lg) == sp.zeros(4, 4))
rec("xi.xi", sp.simplify((xi_dn.T * xi_up)[0]))
def wedge(w, a, b, c):
    dw = lambda i, j: sp.diff(w[j], X[i]) - sp.diff(w[i], X[j])
    return sp.simplify(w[a] * dw(b, c) + w[b] * dw(c, a) + w[c] * dw(a, b))
tw = wedge(xi_dn, 0, 1, 2)
fy = sp.diff(fF, y)
rec("(xi^dxi)_{txy}", tw)
rec("(xi^dxi)_{txy} + v_s f_y [1 + v_s^2 (1-f)^2]  (must be 0)", sp.simplify(tw + vs * fy * (1 + vs**2 * (1 - fF)**2)))
# the axial Killing field phi = y d_z - z d_y cannot cancel it: the txy component is b-independent at z = 0
bsym = sp.Symbol('b')
phi_up = sp.Matrix([0, 0, -z, y])
comb_dn = (g_true * (xi_up + bsym * phi_up)).applyfunc(sp.simplify)
tw_comb = wedge(comb_dn, 0, 1, 2)
rec("(  (xi + b phi) ^ d(xi + b phi) )_{txy} at z=0 minus (xi^dxi)_{txy}", sp.simplify((tw_comb - tw).subs(z, 0)))
twn = float(tw.subs(F, sp.Lambda(rs, f_tanh(rs))).doit().subs({vs: VSN, t: 0, x: 0.9, y: 0.3, z: 0}))
rec("(xi^dxi)_{txy} numeric at (0.9,0.3), v_s=0.5", twn)

# ------------------------------------------------- 5. not spherically symmetric
print("5. spherical symmetry: independent invariant gradients in the (x', rho) plane")
def grad2(ev, case, p, h=1e-4):
    fx = (scalar(ev, case, (p[0], p[1] + h, p[2], p[3])) - scalar(ev, case, (p[0], p[1] - h, p[2], p[3]))) / (2 * h)
    fy_ = (scalar(ev, case, (p[0], p[1], p[2] + h, p[3])) - scalar(ev, case, (p[0], p[1], p[2] - h, p[3]))) / (2 * h)
    return fx, fy_
gR, gS = grad2(R_ev, "published", P), grad2(RicSq_ev, "published", P)
cross = gR[0] * gS[1] - gR[1] * gS[0]
rec("grad R, grad Ric^2 at (0.9,0.3)", (gR, gS))
rec("|grad R x grad Ric2| / (|grad R||grad Ric2|)",
    abs(cross) / (math.hypot(*gR) * math.hypot(*gS)))
xixi = float(sp.simplify((xi_dn.T * xi_up)[0]).subs(F, sp.Lambda(rs, f_tanh(rs))).doit().subs({vs: VSN, t: 0, x: 0.9, y: 0.3, z: 0}))
rec("xi.xi at (0.9,0.3) (timelike if < 0)", xixi)
rec("rho_E on the axis vs off-axis at the same r_s = 0.9487",
    (T_up("published", (0.0, 0.9487, 0.0, 0.0))[0][0], T_up("published", (0.0, 0.9, 0.3, 0.0))[0][0]))

# ------------------------------------------------------------- 6. Eq (12)
print("6. Eq (12): expansion of the Eulerian volume elements")
# paper: beta^x = -v_s f, K_ij = (1/2)(d_i beta_j + d_j beta_i) [its Eq (10)], theta = -Tr K [Eq (11)]
beta_dn = sp.Matrix([-v_true, 0, 0])
K = sp.Matrix(3, 3, lambda i, j: (sp.diff(beta_dn[j], X[i + 1]) + sp.diff(beta_dn[i], X[j + 1])) / 2)
theta = sp.simplify(-K.trace())
fprime = sp.Derivative(F(rs), rs).subs(rs, rs_expr)
rec("theta = -Tr K", theta)
rec("theta - v_s ((x - x_s)/r_s) f'   (must be 0)", sp.simplify(theta - vs * ((x - vs * t) / rs_expr) * fprime))
rec("theta - v_s (x_s/r_s) f' as PRINTED, with x_s = v_s t (not 0)",
    sp.simplify(theta - vs * ((vs * t) / rs_expr) * fprime))
# sign: behind the ship (x < x_s) in the wall f' < 0 so theta > 0: expansion behind.
th_num = sp.lambdify((t, x, y, z), theta.subs(F, sp.Lambda(rs, f_tanh(rs))).doit().subs(vs, VSN), 'math')
rec("theta at (x,y)=(-1.0,0.0) [behind] and (+1.0,0.0) [ahead], t=0", (th_num(0, -1.0, 0, 0), th_num(0, 1.0, 0, 0)))

# ---------------------------- 7. the tree's pipeline: frozen vs published
print("7. typefour freezes x_s: consequences")
for p in [(0.0, 0.9, 0.3, 0.0), (0.0, 1.0, 0.2, 0.0), (0.0, 0.9, 0.0, 0.0)]:
    row = {}
    for case in CASES:
        Tm = T_mixed(case, p)
        row[case] = dict(R=scalar(R_ev, case, p), Txx=Tm[1][1], Tyy=Tm[2][2],
                         T0x_mixed=Tm[0][1], T00_up=T_up(case, p)[0][0], Tkk=T_kk(case, p))
    row["anec.T_kk"] = anec.T_kk(p[1:])
    rec("point (x,y)=(%.1f,%.1f)" % (p[1], p[2]), row)


# Lobo & Visser gr-qc/0406083 Appendix A (motion along their z == our x; orthonormal frame
# e_t = n, e_i = d_i, so G_{ii}(orthonormal) = G_{ii}(coordinate, lower) here):
#   A10: G_zz = -(3/4) v^2 (f_x^2 + f_y^2)      -> our G_xx = -(3/4) v_s^2 (f_y^2 + f_z^2)
#   A5 : G_xx = v^2 [1/4 f_x^2 - 1/4 f_y^2 - f_z^2 + (1-f) f_zz] -> our G_yy = v_s^2[1/4 f_y^2 - 1/4 f_z^2 - f_x^2 + (1-f) f_xx]
def lower_T(case, p):
    Tm = T_mixed(case, p); gm, _ = gnum(p)
    return [[sum(gm[m][a] * Tm[a][n] for a in range(4)) for n in range(4)] for m in range(4)]
fl = sp.lambdify((x, y, z), f_tanh(sp.sqrt(x**2 + y**2 + z**2)), 'math')
def fd(fun, p, i, h=1e-4):
    q1, q2 = list(p), list(p); q1[i] += h; q2[i] -= h
    return (fun(*q1) - fun(*q2)) / (2 * h)
for p in [(0.0, 0.9, 0.3, 0.0), (0.0, 1.0, 0.2, 0.0)]:
    sp3 = p[1:]
    fx, fy, fz = fd(fl, sp3, 0), fd(fl, sp3, 1), fd(fl, sp3, 2)
    fxx = (fl(sp3[0] + 1e-4, sp3[1], sp3[2]) - 2 * fl(*sp3) + fl(sp3[0] - 1e-4, sp3[1], sp3[2])) / 1e-8
    fv = fl(*sp3)
    A10 = -(3.0 / 4.0) * VSN**2 * (fy**2 + fz**2) / (8 * math.pi)
    A5 = VSN**2 * (0.25 * fy**2 - 0.25 * fz**2 - fx**2 + (1 - fv) * fxx) / (8 * math.pi)
    Tp, Tf = lower_T("published", p), lower_T("frozen(typefour)", p)
    rec("LV A10 (T_xx along motion) at (%.1f,%.1f): closed / published / frozen" % sp3[:2], (A10, Tp[1][1], Tf[1][1]))
    rec("LV A5  (T_yy transverse)   at (%.1f,%.1f): closed / published / frozen" % sp3[:2], (A5, Tp[2][2], Tf[2][2]))

# ANEC integrals along y = const rays, x in [-6, 6], as anec.sample_ray does
def anec_int(case, yv, n=480, a=-6.0, b=6.0):
    h = (b - a) / n
    xs = [a + i * h for i in range(n + 1)]
    vals = [T_kk(case, (0.0, xx, yv, 0.0)) for xx in xs]
    return sum(h * (vals[i] + vals[i + 1]) / 2 for i in range(n))
for yv in (0.0, 0.2, 0.3, 0.5, 0.8):
    rec("ANEC y=%.1f : published / frozen / anec.anec_integral" % yv,
        (anec_int("published", yv), anec_int("frozen(typefour)", yv), anec.anec_integral(yv)))

# 7b. WHY T_kk agrees: with flat slices and alpha = 1 the constraints give rho_E and J_i from
# derivatives of the shift alone; the evolution equation gives the spatial stress, and the two
# spacetimes differ there by Delta_ij = -(v_s/8pi)(d_x K_ij - delta_ij d_x K) (trace-reversed),
# which vanishes for xx and for the t-row.  Checked symbolically: T_xx, T_0x, T_00 (lower) identical; T_yy not.
def lowerT_sym(vexpr):
    gg = g.subs(v, vexpr).doit()
    return (gg * Gmix.subs(v, vexpr).doit() / (8 * sp.pi)).applyfunc(sp.simplify)
F2 = sp.Function('F2')
Tl_pub = lowerT_sym(vs * F2(x - vs * t, y, z))
Tl_frz = lowerT_sym(vs * F2(x, y, z))
def at_t0(e):  # compare at t = 0, where the two shift profiles coincide
    return sp.simplify(e.subs(t, 0))
for (a, b, lab) in [(0, 0, "T_tt"), (0, 1, "T_tx"), (1, 1, "T_xx"), (2, 2, "T_yy"), (1, 2, "T_xy"), (3, 3, "T_zz")]:
    d = at_t0(Tl_pub[a, b] - Tl_frz[a, b])
    rec("7b  published - frozen, lower %s at t=0 (symbolic)" % lab, d)
# K_ij = -(d_i beta_j + d_j beta_i)/2 with beta_x = -v  =>  K_xx = d_x v, K_xi = d_i v / 2
K_sym = sp.Matrix(3, 3, lambda i, j: (sp.diff(vs * F2(x, y, z), X[j + 1]) * (1 if i == 0 else 0)
                                       + sp.diff(vs * F2(x, y, z), X[i + 1]) * (1 if j == 0 else 0)) / 2)
Ktr = K_sym.trace()
pred = sp.Matrix(3, 3, lambda i, j: -(vs / (8 * sp.pi)) * (sp.diff(K_sym[i, j], x) - (1 if i == j else 0) * sp.diff(Ktr, x)))
for (i, j, lab) in [(0, 0, "xx"), (1, 1, "yy"), (0, 1, "xy"), (2, 2, "zz")]:
    d = at_t0(Tl_pub[i + 1, j + 1] - Tl_frz[i + 1, j + 1])
    rec("7b  (published - frozen)_%s minus -(v_s/8pi)(d_x K_%s - delta d_x K)  (must be 0)" % (lab, lab),
        sp.simplify(d - pred[i, j]))

# 7c. anec.py's ray k = (1, v+1, 0, 0): geodesic on the axis only; transverse acceleration d_y v off it.
kf = sp.Matrix([1, v + 1, 0, 0])
acc = [sp.simplify(sum(kf[n] * sp.diff(kf[m], X[n]) for n in range(4))
                   + sum(Gam[m][n][r] * kf[n] * kf[r] for n in range(4) for r in range(4))) for m in range(4)]
rec("7c  acceleration of anec's ray field, a^y", acc[2])
rec("7c  a^x - a^t (v+1)   (0 => a is parallel to k where a^y = a^z = 0)", sp.simplify(acc[1] - acc[0] * (v + 1)))
rec("7c  a^t (the non-affinity kappa)", acc[0])

# 7d. ANEC along the axis null GEODESIC of the published (moving) spacetime, affinely parametrised:
# x' = v(t,x)+1, dlambda/dt = exp(-int kappa dt), I = int T_kk (dt/dlambda) dt.
def ray_anec(case, vfun, sign=1.0, t0=0.0, x0=-6.0, xend=6.0, h=2e-3):
    kap_ev = numeric_evaluator(acc[0].subs(v, sp.Symbol('V')) if False else acc[0])
    at = CASES[case]
    def kappa(tt, xx): return kap_ev[1](*at((tt, xx, 0.0, 0.0), kap_ev[0]))
    def Tkk_moving(tt, xx):
        vv = vfun(tt, xx)
        Tm = T_mixed(case, (tt, xx, 0.0, 0.0))
        gm = [[-1 + vv * vv, -vv, 0, 0], [-vv, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        Tl = [[sum(gm[m][a] * Tm[a][n] for a in range(4)) for n in range(4)] for m in range(4)]
        k = [1.0, vv + sign, 0.0, 0.0]
        return sum(Tl[m][n] * k[m] * k[n] for m in range(4) for n in range(4))
    tt, xx, lnw, I_aff, I_dt, I_dx = t0, x0, 0.0, 0.0, 0.0, 0.0
    while (xx - (VSN * tt if case == "published" else 0.0)) < xend:
        f1 = vfun(tt, xx) + sign
        f2 = vfun(tt + h / 2, xx + h * f1 / 2) + sign
        f3 = vfun(tt + h / 2, xx + h * f2 / 2) + sign
        f4 = vfun(tt + h, xx + h * f3) + sign
        Tk = Tkk_moving(tt, xx)
        I_aff += Tk * math.exp(-lnw) * h
        I_dt += Tk * h
        I_dx += Tk * f1 * h
        lnw += kappa(tt, xx) * h
        xx += h * (f1 + 2 * f2 + 2 * f3 + f4) / 6
        tt += h
    return I_aff, I_dt, I_dx
vpub = lambda tt, xx: VSN * tf.shape(abs(xx - VSN * tt))
vfrz = lambda tt, xx: VSN * tf.shape(abs(xx))
for sgn in (1.0, -1.0):
    rec("7d  axis geodesic, published, k^x = v%+d: (affine, dt, dx) integrals" % int(sgn),
        ray_anec("published", vpub, sgn, x0=-6.0 if sgn > 0 else 6.0, xend=6.0 if sgn > 0 else -6.0) if sgn > 0
        else "see below")
def ray_anec_back(case, vfun, h=2e-3):
    # backward ray: k^x = v - 1, start at x = +6, run until x - x_s < -6
    at = CASES[case]
    kap_ev = numeric_evaluator(acc[0])
    def kappa(tt, xx): return kap_ev[1](*at((tt, xx, 0.0, 0.0), kap_ev[0]))
    tt, xx, lnw, I_aff, I_dt = 0.0, 6.0, 0.0, 0.0, 0.0
    while (xx - (VSN * tt if case == "published" else 0.0)) > -6.0:
        vv = vfun(tt, xx)
        Tm = T_mixed(case, (tt, xx, 0.0, 0.0))
        gm = [[-1 + vv * vv, -vv, 0, 0], [-vv, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        Tl = [[sum(gm[m][a] * Tm[a][n] for a in range(4)) for n in range(4)] for m in range(4)]
        k = [1.0, vv - 1.0, 0.0, 0.0]
        Tk = sum(Tl[m][n] * k[m] * k[n] for m in range(4) for n in range(4))
        I_aff += Tk * math.exp(-lnw) * h; I_dt += Tk * h
        lnw += kappa(tt, xx) * h
        xx += h * (vv - 1.0); tt += h
    return I_aff, I_dt
rec("7d  axis geodesic, published, k^x = v-1: (affine, dt) integrals", ray_anec_back("published", vpub))
rec("7d  axis geodesic, frozen,    k^x = v+1: (affine, dt, dx) integrals", ray_anec("frozen(typefour)", vfrz, 1.0))
rec("7d  anec.anec_integral(0.0) (int T_kk dx at t = 0)", anec.anec_integral(0.0))

# 7e. The one importer the transverse stresses reach: typefour's Hawking-Ellis type (complex eigenvalue pair).
import numpy as np
for pt in tf.WALL_POINTS:
    row = {}
    for case in CASES:
        Tm = np.array(T_mixed(case, (0.0, pt[0], pt[1], 0.0)))
        ev = np.linalg.eigvals(Tm)
        n = np.linalg.norm(Tm)
        row[case] = (round(float(n), 5), round(float(max(abs(ev.imag)) / n), 4))
    row["typefour.classify"] = tuple(round(u, 4) if isinstance(u, float) else u for u in tf.classify((pt[0], pt[1], 0.0)))
    rec("7e  (||T||, |Im|/||T||) at %s" % str(pt), row)

import json
out = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67/rederive/gr-qc_0009013.out.json"
with open(out, "w") as fh:
    json.dump({k: str(v) for k, v in results.items()}, fh, indent=1)
print("written", out)
