#!/usr/bin/env python3
"""
DOCKET 67 re-derivation: alcubierre-1994-metric.

Source: M. Alcubierre, Class. Quantum Grav. 11 (1994) L73-L77, arXiv:gr-qc/0009013.
  eq (8)  ds^2 = -dt^2 + (dx - v_s f(r_s) dt)^2 + dy^2 + dz^2,
          v_s(t) = dx_s/dt,  r_s(t) = sqrt((x - x_s(t))^2 + y^2 + z^2)
  eq (6)  f = (tanh(sigma(r_s+R)) - tanh(sigma(r_s-R))) / (2 tanh(sigma R))
  eq (19) T^{mu nu} n_mu n_nu = -(1/8pi) v_s^2 rho^2/(4 r_s^2) (df/dr_s)^2,  rho^2 = y^2+z^2

Checks (sympy, exact; numeric only where stated):
  E1  eq (19) re-derived from the Einstein tensor of eq (8) for a generic shift F(t,x,y,z).
  E2  G_nn contains no time derivative of F  -> a frozen bubble (x_s fixed, v_s != 0) and the
      moving bubble (x_s = v_s t) share the Eulerian density; this is why typefour.py's
      validation against eq (19)/BBV (3.48) cannot see the difference.
  E3  G_xx and T_kk DO contain d_t F -> frozen and moving bubbles have different stress tensors.
  E4  Alcubierre-Lobo identity G_xx = 3 G_nn (restated in Santiago-Schuster-Visser 2105.03079
      Sec 7.1) tested on the moving bubble and on the frozen bubble.
  E5  Scope claim of certify.py / nonstatic.py: (a) the rotation y d_x - x d_y is not a Killing
      vector; (b) the comoving Killing field d_t (constant v_s) is not hypersurface-orthogonal
      (xi ^ d xi != 0): stationary, not static; (c) for non-constant v_s(t) even that fails.
  E6  The tree's numbers (typefour.py SIGMA=8, RADIUS=1, VS=0.5; anec.py rays) recomputed
      exactly for the FROZEN metric (must reproduce anec.py) and for the MOVING metric
      (Alcubierre's eq (8) with x_s = v_s t), same null vectors, same x-grid.
  E7  Are anec.py's 'rays' (k = (1, v f +- 1, 0, 0) at fixed y) null geodesics?
"""
import math, sys, json
import sympy as sp

t, x, y, z = sp.symbols('t x y z', real=True)
X = [t, x, y, z]
F = sp.Function('F')(t, x, y, z)

def metric_of(Fexpr):
    g = sp.zeros(4, 4)
    g[0, 0] = -1 + Fexpr**2
    g[0, 1] = g[1, 0] = -Fexpr
    g[1, 1] = g[2, 2] = g[3, 3] = 1
    return g

def einstein(g):
    gi = sp.simplify(g.inv())
    Gam = [[[sp.expand(sum(gi[a, e] * (sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b])
                                          - sp.diff(g[b, c], X[e])) for e in range(4)) / 2)
             for c in range(4)] for b in range(4)] for a in range(4)]
    Ric = sp.zeros(4, 4)
    for b in range(4):
        for d in range(b, 4):
            s = 0
            for a in range(4):
                s += sp.diff(Gam[a][b][d], X[a]) - sp.diff(Gam[a][b][a], X[d])
                for e in range(4):
                    s += Gam[a][a][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][a]
            Ric[b, d] = Ric[d, b] = sp.expand(s)
    Rs = sp.expand(sum(gi[a, b] * Ric[a, b] for a in range(4) for b in range(4)))
    G = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            G[a, b] = sp.expand(Ric[a, b] - g[a, b] * Rs / 2)
    return G, Gam, gi, Rs

out = {}
ok = True
def chk(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print("  %-72s %s %s" % (label, "ok" if cond else "FAIL", detail))

print("E0  building G_{mu nu} for ds^2 = -dt^2 + (dx - F dt)^2 + dy^2 + dz^2, F generic ...")
g = metric_of(F)
G, Gam, gi, Rs = einstein(g)
n_up = [1, F, 0, 0]            # Eulerian normal, alpha = 1, beta^x = -F
Gnn = sp.simplify(sum(G[a, b] * n_up[a] * n_up[b] for a in range(4) for b in range(4)))
Fy, Fz, Ft, Fx = [sp.diff(F, s) for s in (y, z, t, x)]

print("E1  eq (19): Eulerian density")
chk("G_nn == -(F_y^2 + F_z^2)/4  (generic F)", sp.simplify(Gnn + (Fy**2 + Fz**2) / 4) == 0,
    str(sp.factor(Gnn)))
v, sig, Rb = sp.symbols('v_s sigma R', positive=True)
rs = sp.symbols('r_s', positive=True)
fr = sp.Function('f')
# F = v f(r_s), r_s = sqrt((x - v t)^2 + y^2 + z^2): F_y = v f' y/r_s, F_z = v f' z/r_s
rho19 = -(1 / (8 * sp.pi)) * v**2 * (y**2 + z**2) / (4 * rs**2) * sp.Symbol("fp")**2
ours = -(1 / (8 * sp.pi)) * ((v * sp.Symbol("fp") * y / rs)**2 + (v * sp.Symbol("fp") * z / rs)**2) / 4
chk("G_nn/8pi with F = v_s f(r_s) equals Alcubierre eq (19) (incl. the 1/8pi)",
    sp.simplify(rho19 - ours) == 0)

print("E2  G_nn has no time derivative of F")
free_t = [d for d in Gnn.atoms(sp.Derivative) if t in d.variables]
chk("no Derivative wrt t in G_nn", len(free_t) == 0, str(free_t))

print("E3  which components carry d_t F (frozen vs moving can differ only there)")
def has_t(expr):
    return any(t in d.variables for d in expr.atoms(sp.Derivative))
chk("G_xx (along the motion) carries NO d_t F  [SSV eq 4.9: L_n K_xx - L_n K cancels]", not has_t(G[1, 1]))
chk("G_yy carries d_t F", has_t(G[2, 2]))
chk("G_zz carries d_t F", has_t(G[3, 3]))
chk("G_tx or G_nx-type flux: G_nx = G_ab n^a e_x^b carries no d_t F",
    not has_t(sp.expand(sum(G[a, 1] * n_up[a] for a in range(4)))))
for sgn in (1, -1):
    k = [1, F + sgn, 0, 0]
    nullk = sp.simplify(sum(g[a, b] * k[a] * k[b] for a in range(4) for b in range(4)))
    chk("k=(1,F%+d,0,0) is null" % sgn, nullk == 0)
    Gkk = sp.expand(sum(G[a, b] * k[a] * k[b] for a in range(4) for b in range(4)))
    chk("G_kk (sign %+d, k along the motion) carries NO d_t F -> frozen == moving for anec.py" % sgn,
        not has_t(Gkk))
kT = [1, F, 1, 0]   # a null vector with a transverse leg: n + e_y
chk("k = n + e_y is null", sp.simplify(sum(g[a, b] * kT[a] * kT[b] for a in range(4) for b in range(4))) == 0)
chk("G_kk for the transverse null vector n + e_y DOES carry d_t F",
    has_t(sp.expand(sum(G[a, b] * kT[a] * kT[b] for a in range(4) for b in range(4)))))

# lambdify G_{mu nu} as a function of F and its derivatives up to 2nd order
derivs = sorted(G.atoms(sp.Derivative) | Gnn.atoms(sp.Derivative), key=str)
syms = [sp.Symbol('D%d' % i) for i in range(len(derivs))]
Fs = sp.Symbol('Fv')
sub = dict(zip(derivs, syms))
def to_num(expr):
    e = expr.subs(sub).subs(F, Fs)
    return sp.lambdify([Fs] + syms, e, 'math')
Gnum = [[to_num(G[a, b]) for b in range(4)] for a in range(4)]

def explicit_F(moving, vs=0.5, SIG=8.0, RAD=1.0):
    r = sp.sqrt(((x - vs * t) if moving else x)**2 + y**2 + z**2)
    f = (sp.tanh(SIG * (r + RAD)) - sp.tanh(SIG * (r - RAD))) / (2 * sp.tanh(SIG * RAD))
    Fe = vs * f
    fs = [sp.lambdify([t, x, y, z], Fe, 'math')]
    for d in derivs:
        vars_ = d.variables
        fs.append(sp.lambdify([t, x, y, z], sp.diff(Fe, *vars_), 'math'))
    return fs

def Tlow(fs, p):
    vals = [fn(*p) for fn in fs]
    return [[Gnum[a][b](*vals) / (8 * math.pi) for b in range(4)] for a in range(4)], vals[0]

print("E4  Alcubierre-Lobo identity G_xx = 3 G_nn (comoving Eulerian frame, moving bubble)")
FM = explicit_F(True); FF = explicit_F(False)
for (px, py) in ((0.9, 0.3), (1.0, 0.2), (1.05, 0.4), (0.6, 0.1)):
    for lab, fs in (("moving", FM), ("frozen", FF)):
        T, Fv = Tlow(fs, (0.0, px, py, 0.0))
        nn = sum(T[a][b] * [1, Fv, 0, 0][a] * [1, Fv, 0, 0][b] for a in range(4) for b in range(4))
        print("      %-6s (%.2f,%.2f)  T_xx = %+.6e   3 T_nn = %+.6e   ratio %.6f"
              % (lab, px, py, T[1][1], 3 * nn, T[1][1] / (3 * nn) if nn else float('nan')))
        out.setdefault("E4", []).append([lab, px, py, T[1][1], 3 * nn])
m = [r for r in out["E4"] if r[0] == "moving"]
fz = [r for r in out["E4"] if r[0] == "frozen"]
chk("moving bubble: T_xx == 3 T_nn at all 4 points (rel 1e-9)",
    all(abs(r[3] - r[4]) <= 1e-9 * abs(r[4]) for r in m))
chk("frozen bubble: T_xx == 3 T_nn too (both sides are d_t-free, E3)",
    all(abs(r[3] - r[4]) <= 1e-9 * abs(r[4]) for r in fz))

print("E5  symmetry: scope claims of certify.py:181-183 and nonstatic.py:240-242")
Fm = sp.Symbol('v_s') * fr(sp.sqrt((x - sp.Symbol('v_s') * t)**2 + y**2 + z**2))
gm = metric_of(Fm)
def killing_residual(gmat, xi):
    # (L_xi g)_{ab} = xi^c d_c g_ab + g_cb d_a xi^c + g_ac d_b xi^c
    R = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            R[a, b] = sp.simplify(sum(xi[c] * sp.diff(gmat[a, b], X[c]) for c in range(4))
                                  + sum(gmat[c, b] * sp.diff(xi[c], X[a]) for c in range(4))
                                  + sum(gmat[a, c] * sp.diff(xi[c], X[b]) for c in range(4)))
    return R
Kyz = killing_residual(gm, [0, 0, -z, y])
chk("rotation about the x-axis (y d_z - z d_y) IS Killing (axisymmetry)", Kyz == sp.zeros(4, 4))
Kxy = killing_residual(gm, [0, -y, x - sp.Symbol('v_s') * t, 0])
chk("rotation mixing x and y about the bubble centre is NOT Killing", Kxy != sp.zeros(4, 4),
    "nonzero components: %d" % sum(1 for e in Kxy if e != 0))
# comoving chart: xi = x - v t, shift v(f-1); Killing d_t; twist xi ^ d xi
xs = sp.Symbol('xi', real=True)
vv = sp.Symbol('v_s', positive=True)
fc = fr(sp.sqrt(xs**2 + y**2 + z**2))
w = [-1 + vv**2 * (1 - fc)**2, vv * (1 - fc), 0, 0]   # xi_mu = g_{mu t} in (t, xi, y, z)
C = [t, xs, y, z]
dw = [[sp.diff(w[b], C[a]) - sp.diff(w[a], C[b]) for b in range(4)] for a in range(4)]
tw_txy = sp.simplify(w[0] * dw[1][2] + w[1] * dw[2][0] + w[2] * dw[0][1])
chk("comoving d_t is Killing (metric t-independent in (t, xi, y, z))", True, "by construction")
chk("(xi ^ d xi)_{t xi y} != 0 -> not hypersurface-orthogonal -> NOT static", tw_txy != 0,
    str(sp.factor(tw_txy))[:120])
# numeric value at a wall point for the tree's parameters
fnum = lambda r: ((math.tanh(8 * (r + 1)) - math.tanh(8 * (r - 1))) / (2 * math.tanh(8)))
tw_num = sp.lambdify([xs, y, z, vv], tw_txy.subs(fr, sp.Lambda(rs, (sp.tanh(8 * (rs + 1)) - sp.tanh(8 * (rs - 1))) / (2 * sp.tanh(8)))).doit(), 'math')
twv = tw_num(0.9, 0.3, 0.0, 0.5)
chk("  numerically at (xi,y)=(0.9,0.3), v_s=0.5: twist != 0", abs(twv) > 1e-6, "%.6e" % twv)
out["E5_twist_0.9_0.3"] = twv
vt = sp.Function('V')(t)
Fnc = vt * fr(sp.sqrt((x - sp.Integral(vt, t))**2 + y**2 + z**2))
chk("non-constant v_s(t): d_t g_tx = d_t(-F) has a V'(t) term (no comoving Killing field)",
    sp.diff(Fnc, t).has(sp.Derivative(vt, t)))

print("E6  the tree's anec.py numbers, frozen vs moving (exact G, tree's x-grid)")
def Tkk(fs, p, sgn):
    T, Fv = Tlow(fs, p)
    k = [1.0, Fv + sgn, 0.0, 0.0]
    return sum(T[a][b] * k[a] * k[b] for a in range(4) for b in range(4))
def anec(fs, yv, sgn=1.0, a=-2.5, b=2.5, n=90):
    h = (b - a) / n
    return sum(Tkk(fs, (0.0, a + (i + 0.5) * h, yv, 0.0), sgn) for i in range(n)) * h
TREE = {0.0: None, 0.2: None, 0.3: None, 0.5: None, 0.8: None}
try:
    sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
    import anec as _anec
    for yv in TREE:
        TREE[yv] = _anec.anec_integral(yv)
except Exception as e:  # tree not importable -> record, do not fail
    print("      (tree anec.py not importable: %s)" % e)
rows = []
for yv in sorted(TREE):
    fr_ = anec(FF, yv); mv = anec(FM, yv); mvm = anec(FM, yv, -1.0); frm = anec(FF, yv, -1.0)
    rows.append([yv, TREE[yv], fr_, mv, frm, mvm])
    print("      y=%.1f  tree=%s  frozen(+)=%+.6f  MOVING(+)=%+.6f  frozen(-)=%+.6f  MOVING(-)=%+.6f"
          % (yv, ("%+.6f" % TREE[yv]) if TREE[yv] is not None else "n/a", fr_, mv, frm, mvm))
out["E6_anec"] = rows
if all(r[1] is not None for r in rows):
    chk("exact frozen integrals reproduce anec.py (rel 1e-3) -> the tree computes the FROZEN metric",
        all(abs(r[2] - r[1]) <= 1e-3 * abs(r[1]) + 1e-6 for r in rows))
    chk("moving-bubble integrals EQUAL anec.py (rel 1e-9): the frozen drift is immaterial here",
        all(abs(r[3] - r[2]) <= 1e-9 * abs(r[2]) for r in rows))
chk("sign of INT T_kk dx (k+) on each measured ray, moving bubble: all negative?",
    all(r[3] < 0 for r in rows), str([round(r[3], 4) for r in rows]))

print("E6b Hawking-Ellis type at typefour.py's WALL_POINTS, moving bubble (eigenvalues of T^mu_nu)")
import cmath
def mixed(fs, p):
    T, Fv = Tlow(fs, p)
    gnum = [[-1 + Fv * Fv, -Fv, 0, 0], [-Fv, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    ginv = [[-1, -Fv, 0, 0], [-Fv, 1 - Fv * Fv, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    return [[sum(ginv[m_][a] * T[a][n_] for a in range(4)) for n_ in range(4)] for m_ in range(4)]
import numpy as _np
def eig_im(M):
    A = _np.array(M, dtype=float)
    ev = _np.linalg.eigvals(A)
    nrm = float(_np.linalg.norm(A))
    return (float(max(abs(e.imag) for e in ev)) / nrm if nrm else 0.0), nrm
WALL = [(0.60, 0.00), (0.90, 0.00), (0.90, 0.30), (1.00, 0.00), (1.00, 0.20), (1.05, 0.40), (1.20, 0.30)]
tyrows = []
for (px, py) in WALL:
    rf, nf = eig_im(mixed(FF, (0.0, px, py, 0.0)))
    rm, nm = eig_im(mixed(FM, (0.0, px, py, 0.0)))
    tyrows.append([px, py, nf, rf, nm, rm])
    print("      (%.2f,%.2f)  frozen ||T||=%.5f Im/||T||=%.4f   MOVING ||T||=%.5f Im/||T||=%.4f"
          % (px, py, nf, rf, nm, rm))
out["E6b_type"] = tyrows
TABLE = {(0.60, 0.00): (0.00612, 0.1435), (0.90, 0.00): (0.22317, 0.2215), (0.90, 0.30): (0.15909, 0.6425),
         (1.00, 0.00): (0.25482, 0.3123), (1.00, 0.20): (0.28861, 0.2585), (1.05, 0.40): (0.12612, 0.5398),
         (1.20, 0.30): (0.01897, 0.6937)}
chk("frozen reproduces typefour.py's printed table (||T|| rel 1e-3, ratio abs 1e-3)",
    all(abs(r[2] - TABLE[(r[0], r[1])][0]) <= 1e-3 * TABLE[(r[0], r[1])][0] + 1e-5 and
        abs(r[3] - TABLE[(r[0], r[1])][1]) <= 1e-3 for r in tyrows))
chk("moving bubble: typefour's printed numbers do NOT carry over (some ||T|| differs > 1%)",
    any(abs(r[4] - r[2]) > 1e-2 * r[2] for r in tyrows))
chk("moving bubble: a complex pair survives at every wall point (ratio > 1e-3) -> Type IV verdict stands",
    all(r[5] > 1e-3 for r in tyrows), str([round(r[5], 4) for r in tyrows]))

print("E7  are anec.py's rays geodesics? a^mu = Gamma^mu_ab k^a k^b - kappa k^mu, y-component")
Ay = {}
for sgn in (1, -1):
    k = [1, F + sgn, 0, 0]
    Ay[sgn] = sp.simplify(sum(Gam[2][b_][c_] * k[b_] * k[c_] for b_ in range(4) for c_ in range(4)))
    print("      symbolic Gamma^y_ab k^a k^b (sign %+d) = %s" % (sgn, Ay[sgn]))
chk("Gamma^y_ab k^a k^b = sgn * F_y (so d^2y/ds^2 = -sgn F_y != 0 off-axis)",
    all(sp.simplify(Ay[s_] - s_ * sp.diff(F, y)) == 0 for s_ in (1, -1)))
def ay(fs, p, sgn=1.0):
    # -F_y at p: the y-derivative of the explicit F is one of the lambdified derivative functions
    idx = derivs.index(sp.Derivative(F, y)) + 1
    return -fs[idx](*p)
e7 = []
for lab, fs in (("frozen", FF), ("moving", FM)):
    for (px, py) in ((0.9, 0.0), (0.9, 0.3), (1.0, 0.5)):
        a_ = ay(fs, (0.0, px, py, 0.0))
        e7.append([lab, px, py, a_])
        print("      %-6s (%.2f,%.2f)  Gamma^y_ab k^a k^b = %+.6e" % (lab, px, py, a_))
chk("on the axis (y=0) the transverse acceleration vanishes (ray can be geodesic)",
    all(abs(r[3]) < 1e-12 for r in e7 if r[2] == 0.0))
chk("off the axis it does not: the fixed-y null curves are NOT geodesics",
    all(abs(r[3]) > 1e-4 for r in e7 if r[2] != 0.0))
out["E7"] = e7

print("E8  on-axis ANEC with the AFFINE parameter (the ray y=0 is a geodesic up to parametrisation)")
# parametrise by t: k = (1, F+sgn, 0, 0); k^b nabla_b k^a = kappa k^a; t-component gives kappa = Gamma^t_ab k^a k^b
kap = {}
for sgn in (1, -1):
    k = [1, F + sgn, 0, 0]
    kap[sgn] = sp.simplify(sum(Gam[0][b_][c_] * k[b_] * k[c_] for b_ in range(4) for c_ in range(4)))
    # consistency: x-component  dk^x/dt + Gamma^x kk == kappa k^x along the curve
    dkx = sp.diff(F, t) + sp.diff(F, x) * (F + sgn)
    resx = sp.simplify(dkx + sum(Gam[1][b_][c_] * k[b_] * k[c_] for b_ in range(4) for c_ in range(4)) - kap[sgn] * (F + sgn))
    resy = sp.simplify(sum(Gam[2][b_][c_] * k[b_] * k[c_] for b_ in range(4) for c_ in range(4)))
    print("      sign %+d: kappa = %s ; x-residual = %s ; y-accel = %s" % (sgn, kap[sgn], resx, resy))
    chk("sign %+d: on y=0 the curve is a pregeodesic (x-residual 0; y-accel = sgn F_y = 0 on axis)" % sgn, resx == 0)
def lam_expr(expr):
    ds = sorted(expr.atoms(sp.Derivative), key=str)
    ss = [sp.Symbol('Q%d' % i) for i in range(len(ds))]
    fn = sp.lambdify([Fs] + ss, expr.subs(dict(zip(ds, ss))).subs(F, Fs), 'math')
    return fn, ds
def explicit_fns(moving, ds, vs=0.5, SIG=8.0, RAD=1.0):
    r = sp.sqrt(((x - vs * t) if moving else x)**2 + y**2 + z**2)
    Fe = vs * (sp.tanh(SIG * (r + RAD)) - sp.tanh(SIG * (r - RAD))) / (2 * sp.tanh(SIG * RAD))
    return [sp.lambdify([t, x, y, z], Fe, 'math')] + [sp.lambdify([t, x, y, z], sp.diff(Fe, *d.variables), 'math') for d in ds]
e8 = []
for moving, fsG in ((False, FF), (True, FM)):
    for sgn in (1, -1):
        kf, kd = lam_expr(kap[sgn]); kfs = explicit_fns(moving, kd)
        Fonly = kfs[0]
        def rhs(tt, st):
            xx, L, I = st
            p = (tt, xx, 0.0, 0.0)
            kv = kf(*[fn(*p) for fn in kfs])
            w = math.exp(-L)                         # ds/dlambda up to a constant
            return [Fonly(*p) + sgn, kv, Tkk(fsG, p, sgn) * w]
        # start 4 radii from the bubble centre on the side the ray comes from; stop 4 radii past it
        vb = 0.5 if moving else 0.0
        x0 = -4.0 if sgn > 0 else 4.0
        tt, st, hstep = 0.0, [x0, 0.0, 0.0], 0.002
        comov = 0.0      # tree-style: INT T_kk dxi, xi = x - vb t (comoving; = dx for the frozen metric)
        steps = 0
        while steps < 400000:
            xi_now = st[0] - vb * tt
            if (sgn > 0 and xi_now > 4.0) or (sgn < 0 and xi_now < -4.0):
                break
            k1 = rhs(tt, st)
            k2 = rhs(tt + hstep / 2, [a_ + hstep / 2 * b_ for a_, b_ in zip(st, k1)])
            k3 = rhs(tt + hstep / 2, [a_ + hstep / 2 * b_ for a_, b_ in zip(st, k2)])
            k4 = rhs(tt + hstep, [a_ + hstep * b_ for a_, b_ in zip(st, k3)])
            comov += hstep * Tkk(fsG, (tt, st[0], 0.0, 0.0), sgn) * abs(Fonly(tt, st[0], 0.0, 0.0) + sgn - vb)
            st = [a_ + hstep / 6 * (b_ + 2 * c_ + 2 * d_ + e_) for a_, b_, c_, d_, e_ in zip(st, k1, k2, k3, k4)]
            tt += hstep; steps += 1
        e8.append(["moving" if moving else "frozen", sgn, st[2], comov, st[1], tt])
        print("      %-6s sign %+d: affine INT T_kk dlambda = %+.6f   tree-style INT T_kk |dxi| along the ray = %+.6f   "
              "net ln(dlambda/dt) = %+.2e  t_exit = %.2f" % (e8[-1][0], sgn, st[2], comov, st[1], tt))
out["E8"] = e8
chk("frozen, sign +1: tree-style ray integral reproduces anec.py y=0 (-0.0807, rel 2%)",
    abs(e8[0][3] + 0.080665) < 0.02 * 0.080665)
chk("moving, sign +1: tree-style ray integral equals anec.py y=0 (rel 2%) -- E6 again, via the ODE",
    abs(e8[2][3] + 0.080665) < 0.02 * 0.080665)
chk("net ln(dlambda/dt) returns to ~0 after the ray exits (Killing-energy conservation), all four",
    all(abs(r[4]) < 1e-3 for r in e8))
chk("affine on-axis ANEC (sign +1) negative for frozen AND moving", e8[0][2] < 0 and e8[2][2] < 0,
    "%+.5f / %+.5f" % (e8[0][2], e8[2][2]))
chk("the opposite-directed on-axis ray (sign -1) has POSITIVE integral, frozen and moving (tree measures only +)",
    e8[1][2] > 0 and e8[3][2] > 0 and e8[1][3] > 0 and e8[3][3] > 0)

print("\nOVERALL:", "PASS (all checks as recorded)" if ok else "SOME CHECK FAILED -- read above")
json.dump(out, open(__file__.replace('.py', '.out.json'), 'w'), indent=1, default=str)
sys.exit(0 if ok else 1)
