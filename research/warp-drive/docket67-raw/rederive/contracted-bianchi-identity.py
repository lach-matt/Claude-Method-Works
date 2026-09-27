#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of the contracted Bianchi identity as the tree uses it.

Checks (every one computed, sympy exact arithmetic):
  A1  generic 4D metric (all 10 components, random rational cubic polynomials about a
      point), Levi-Civita connection: nabla_mu G^{mu nu} = 0 EXACTLY at the point, via
      degree-3 Taylor jets (g, dg, ddg, dddg are all that enter).  Several draws.
  A2  general spherically symmetric, time-dependent metric
      -e^{2 Phi(t,r)} dt^2 + e^{2 Lam(t,r)} dr^2 + R(t,r)^2 dOmega^2, arbitrary functions:
      nabla_mu G^mu_nu = 0 symbolically.
  A3  FLRW with arbitrary a(t), k: the nu=t component of the identity IS
      rhodot + 3H(rho+p) = 0 once rho, p are read off G (the reduction permute.py uses).
  B1  CONTROL for permute.py:104-106 ("follows from the symmetries of the Riemann tensor
      alone"): a tensor with every ALGEBRAIC Riemann symmetry, phi(x)(g g - g g) on flat
      space, whose contracted 'G' is not divergence-free.  The identity needs the
      DIFFERENTIAL (second) Bianchi identity of a connection's curvature.
  B2  CONTROL for the Levi-Civita hypothesis: a metric-compatible connection WITH torsion
      on flat space; its curvature's 'Einstein tensor' has non-zero divergence.
  B3  permute.py section 5 (read-only import): the continuity residual is identically zero
      as an algebraic function of (a, adot, k, w) -- the RK4 trajectory never enters it,
      so 'flat in dt' cannot discriminate identity from truncation.  Positive control: a
      wrong acceleration law gives an O(1) residual at every step count.
  C1  hpscentre.py divergence(): for diagonal static T(l) on -f dt^2 + dl^2 + r^2 dOmega^2,
      nabla_mu T^mu_l equals d_l T^l_l + (f'/2f)(T^l_l - T^t_t) + (2r'/r)(T^l_l - T^th_th);
      the theta component vanishes iff T^th_th = T^ph_ph; t, phi components vanish.
  C2  hpscentre.py:1401 step: E^t_t = E^l_l = 0 plus nabla E = 0 forces E^th_th = 0 only
      where r' != 0.  Control: at r' = 0 (a throat) the identity leaves E^th_th free.
Exit 0 iff every check passes.
"""
import random
import sys
sys.dont_write_bytecode = True   # never write .pyc into research/warp-drive
import importlib.util
import sympy as sp

PASS = []
FAIL = []


def chk(label, got, want):
    ok = (got == want)
    (PASS if ok else FAIL).append(label)
    print("  [%s] %s  -> %s" % ("ok" if ok else "FAIL", label, got))


def christoffel(g, ginv, X):
    n = len(X)
    return [[[sp.expand(sum(ginv[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                          - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
              for c in range(n)] for b in range(n)] for a in range(n)]


def riemann_from_gamma(Gam, X):
    """R^a_{bcd} = d_c Gam^a_{db} - d_d Gam^a_{cb} + Gam^a_{ce}Gam^e_{db} - Gam^a_{de}Gam^e_{cb}
    (Gam^a_{bc}: derivative index c, as in nabla_c V^a = d_c V^a + Gam^a_{cb} V^b)."""
    n = len(X)
    R = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    R[a, b, c, d] = (sp.diff(Gam[a][d][b], X[c]) - sp.diff(Gam[a][c][b], X[d])
                                     + sum(Gam[a][c][e] * Gam[e][d][b] - Gam[a][d][e] * Gam[e][c][b]
                                           for e in range(n)))
    return R


def div_upper(Gam, T, X):
    """nabla_a T^{ab} for a (2,0) tensor T with connection Gam^a_{cb} (c = derivative index)."""
    n = len(X)
    out = []
    for b in range(n):
        s = 0
        for a in range(n):
            s += sp.diff(T[a, b], X[a])
            for e in range(n):
                s += Gam[a][a][e] * T[e, b] + Gam[b][a][e] * T[a, e]
        out.append(s)
    return out


def div_mixed(Gam, T, X):
    """nabla_mu T^mu_nu for a (1,1) tensor T[mu, nu] = T^mu_nu (Levi-Civita)."""
    n = len(X)
    out = []
    for nu in range(n):
        s = 0
        for mu in range(n):
            s += sp.diff(T[mu, nu], X[mu])
            for lam in range(n):
                s += Gam[mu][mu][lam] * T[lam, nu] - Gam[lam][mu][nu] * T[mu, lam]
        out.append(sp.simplify(s))
    return out


def einstein_mixed(g, X):
    n = len(X)
    ginv = sp.simplify(g.inv())
    Gam = christoffel(g, ginv, X)
    Gam = [[[sp.simplify(Gam[a][b][c]) for c in range(n)] for b in range(n)] for a in range(n)]
    R = riemann_from_gamma(Gam, X)
    Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(R[a, b, a, d] for a in range(n))))
    Rs = sp.simplify(sum(ginv[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    Gmix = sp.Matrix(n, n, lambda m, v: sp.simplify(sum(ginv[m, a] * Ric[a, v] for a in range(n))
                                                   - (Rs / 2 if m == v else 0)))
    return Gmix, Gam, ginv


# ---------------------------------------------------------------- A1: generic 4D, jets
def truncate(expr, X, deg):
    p = sp.Poly(sp.expand(expr), *X)
    return sum(c * sp.prod([x ** k for x, k in zip(X, m)]) for m, c in p.terms() if sum(m) <= deg)


def generic_jet_check(seed, n=4):
    rnd = random.Random(seed)
    X = sp.symbols('x0:%d' % n)
    eta = sp.diag(*([-1] + [1] * (n - 1)))
    monos = [sp.Integer(1)] + list(X)
    monos += [X[i] * X[j] for i in range(n) for j in range(i, n)]
    monos += [X[i] * X[j] * X[k] for i in range(n) for j in range(i, n) for k in range(j, n)]
    h = sp.zeros(n, n)
    for i in range(n):
        for j in range(i, n):
            e = sum(sp.Rational(rnd.randint(-9, 9), rnd.randint(5, 20)) * m for m in monos[1:])
            e += sp.Rational(rnd.randint(-3, 3), 10)  # value at the point: generic, not eta
            h[i, j] = h[j, i] = e
    g = eta + h
    g0 = g.subs({x: 0 for x in X})
    assert g0.det() != 0
    g0inv = g0.inv()
    # g^{-1} to degree 3: g = g0 + d, d(0)=0;  g^{-1} = sum_k (-g0^{-1} d)^k g0^{-1}
    d = g - g0
    ginv = sp.zeros(n, n)
    term = g0inv
    for _ in range(4):
        ginv += term
        term = (-g0inv * d * term).applyfunc(lambda z: truncate(z, X, 3))
    ginv = ginv.applyfunc(lambda z: truncate(z, X, 3))
    Gam = christoffel(g, ginv, X)
    Gam = [[[truncate(Gam[a][b][c], X, 2) for c in range(n)] for b in range(n)] for a in range(n)]
    R = riemann_from_gamma(Gam, X)
    R = {k: truncate(v, X, 1) for k, v in R.items()}
    Ric = sp.Matrix(n, n, lambda b, dd: sum(R[a, b, a, dd] for a in range(n)))
    Rs = truncate(sum(ginv[a, b] * Ric[a, b] for a in range(n) for b in range(n)), X, 1)
    Gup = sp.Matrix(n, n, lambda m, v: truncate(
        sum(ginv[m, a] * ginv[v, b] * Ric[a, b] for a in range(n) for b in range(n))
        - Rs * ginv[m, v] / 2, X, 1))
    dv = div_upper(Gam, Gup, X)
    at0 = [sp.nsimplify(sp.expand(z).subs({x: 0 for x in X})) for z in dv]
    # non-vacuity: G itself and its derivatives are non-zero
    gnz = any(sp.expand(Gup[i, j]).subs({x: 0 for x in X}) != 0 for i in range(n) for j in range(n))
    dG = sp.diff(Gup[0, 1], X[2]).subs({x: 0 for x in X})
    return at0, gnz, dG != 0


SKIP_SLOW = "--fast" in sys.argv
print("A1. GENERIC 4D METRIC (10 random rational cubic components), EXACT AT THE POINT")
for seed in (() if SKIP_SLOW else (1, 2, 3)):
    at0, gnz, dnz = generic_jet_check(seed)
    chk("seed %d: nabla_mu G^{mu nu}(0) = 0 for all four nu" % seed, at0, [0, 0, 0, 0])
    chk("seed %d: non-vacuous (G(0) != 0 and dG(0) != 0)" % seed, (gnz, dnz), (True, True))

# ---------------------------------------------------------------- A2: spherical, t-dependent
print("\nA2. GENERAL SPHERICALLY SYMMETRIC TIME-DEPENDENT METRIC, ARBITRARY FUNCTIONS")
t, r, th, ph = sp.symbols('t r theta phi', positive=True)
X4 = (t, r, th, ph)
Phi, Lam, Rf = sp.Function('Phi')(t, r), sp.Function('Lam')(t, r), sp.Function('R')(t, r)
g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), Rf ** 2, Rf ** 2 * sp.sin(th) ** 2)
Gmix, Gam, _ = einstein_mixed(g, X4)
chk("nabla_mu G^mu_nu = 0 identically (Phi, Lam, R arbitrary)", div_mixed(Gam, Gmix, X4), [0, 0, 0, 0])
chk("non-vacuous: G^t_t is not identically zero", sp.simplify(Gmix[0, 0]) != 0, True)

# ---------------------------------------------------------------- A3: FLRW
print("\nA3. FLRW, ARBITRARY a(t), k: THE t-COMPONENT IS THE CONTINUITY EQUATION")
k = sp.symbols('k')
a = sp.Function('a')(t)
chi = sp.symbols('chi', positive=True)
gF = sp.diag(-1, a ** 2 / (1 - k * r ** 2), a ** 2 * r ** 2, a ** 2 * r ** 2 * sp.sin(th) ** 2)
GF, GamF, _ = einstein_mixed(gF, X4)
rho = sp.simplify(-GF[0, 0])            # 8 pi G rho = -G^t_t
p = sp.simplify(GF[1, 1])               # 8 pi G p   =  G^r_r
H = sp.diff(a, t) / a
chk("8 pi G rho = 3(adot^2 + k)/a^2 (Friedmann constraint)",
    sp.simplify(rho - 3 * (sp.diff(a, t) ** 2 + k) / a ** 2), 0)
chk("isotropy G^r_r = G^th_th = G^ph_ph", (sp.simplify(GF[1, 1] - GF[2, 2]), sp.simplify(GF[2, 2] - GF[3, 3])), (0, 0))
chk("rhodot + 3H(rho + p) = 0 identically in a(t), k", sp.simplify(sp.diff(rho, t) + 3 * H * (rho + p)), 0)
chk("full divergence nabla_mu G^mu_nu = 0 (FLRW)", div_mixed(GamF, GF, X4), [0, 0, 0, 0])

# ---------------------------------------------------------------- B1: algebraic symmetries alone
print("\nB1. CONTROL: ALGEBRAIC RIEMANN SYMMETRIES ALONE DO NOT GIVE div G = 0")
x = sp.symbols('y0:4')
eta = sp.diag(-1, 1, 1, 1)
phi = sp.Function('varphi')(*x)
Rl = {}
for A in range(4):
    for B in range(4):
        for C in range(4):
            for D in range(4):
                Rl[A, B, C, D] = phi * (eta[A, C] * eta[B, D] - eta[A, D] * eta[B, C])
sym_ok = all(Rl[A, B, C, D] == -Rl[B, A, C, D] and Rl[A, B, C, D] == -Rl[A, B, D, C]
             and Rl[A, B, C, D] == Rl[C, D, A, B]
             and sp.expand(Rl[A, B, C, D] + Rl[A, C, D, B] + Rl[A, D, B, C]) == 0
             for A in range(4) for B in range(4) for C in range(4) for D in range(4))
chk("phi(x)(g_ac g_bd - g_ad g_bc) has all algebraic Riemann symmetries (incl. first Bianchi)", sym_ok, True)
Ric = sp.Matrix(4, 4, lambda B, D: sum(eta[A, C] * Rl[A, B, C, D] for A in range(4) for C in range(4)))
Rsc = sp.expand(sum(eta[A, B] * Ric[A, B] for A in range(4) for B in range(4)))
Gl = (Ric - Rsc * eta / 2).applyfunc(sp.expand)
chk("its contraction G_ab = -3 phi eta_ab", sp.simplify(Gl + 3 * phi * eta), sp.zeros(4, 4))
divB1 = [sp.expand(sum(eta[A, A] * sp.diff(Gl[A, B], x[A]) for A in range(4))) for B in range(4)]
chk("div G = -3 d_b phi != 0 unless phi const (Schur) -> identity needs the DIFFERENTIAL Bianchi",
    [sp.simplify(divB1[B] + 3 * sp.diff(phi, x[B])) for B in range(4)] == [0] * 4 and divB1[1] != 0, True)

# ---------------------------------------------------------------- B2: torsion
print("\nB2. CONTROLS: DROP LEVI-CIVITA -- (i) torsion, metric-compatible; (ii) torsion-free, non-metric")
Xs = sp.symbols('z0:4')
n = 4


def einstein_div_for(GamX, label):
    RT = riemann_from_gamma(GamX, Xs)
    RicT = sp.Matrix(n, n, lambda B, D: sp.expand(sum(RT[A, B, A, D] for A in range(n))))
    RsT = sp.expand(sum(eta[A, B] * RicT[A, B] for A in range(n) for B in range(n)))
    GupT = sp.Matrix(n, n, lambda M, V: sp.expand(sum(eta[M, A] * eta[V, B] * RicT[A, B]
                                                      for A in range(n) for B in range(n)) - RsT * eta[M, V] / 2))
    dT = [sp.expand(z) for z in div_upper(GamX, GupT, Xs)]
    chk(label, any(z != 0 for z in dT), True)
    print("     nabla_mu G^{mu 0} =", dT[0])


def nabla_eta(GamX):
    # nabla_C eta_AB = -Gam^E_{CA} eta_EB - Gam^E_{CB} eta_AE
    return all(sp.expand(sum(-GamX[E][C][A] * eta[E, B] - GamX[E][C][B] * eta[A, E] for E in range(n))) == 0
               for A in range(n) for B in range(n) for C in range(n))


# (i) K_{A C B} = F_{AB} v_C, F antisymmetric -> metric compatible; torsion F^A_B v_C - F^A_C v_B
Fm = sp.zeros(4, 4)
Fm[0, 1], Fm[1, 0] = Xs[2], -Xs[2]
Fm[2, 3], Fm[3, 2] = Xs[0] * Xs[1], -Xs[0] * Xs[1]
vv = [Xs[3], 1, Xs[0], 0]
GamT = [[[eta[A, A] * Fm[A, B] * vv[C] for B in range(n)] for C in range(n)] for A in range(n)]
tors = any(sp.expand(GamT[A][C][B] - GamT[A][B][C]) != 0 for A in range(n) for B in range(n) for C in range(n))
chk("(i) connection is metric-compatible (nabla eta = 0) with non-zero torsion", (nabla_eta(GamT), tors), (True, True))
einstein_div_for(GamT, "(i) torsion: nabla_mu G^{mu nu} != 0")
# (ii) symmetric (torsion-free) connection Gam^A_{CB} = delta^A_C U_B + delta^A_B U_C, flat eta
U = [Xs[1] ** 2, Xs[0] * Xs[2], 0, Xs[3]]
GamN = [[[(U[B] if A == C else 0) + (U[C] if A == B else 0) for B in range(n)] for C in range(n)] for A in range(n)]
chk("(ii) connection is torsion-free and NOT metric-compatible", (all(GamN[A][C][B] == GamN[A][B][C]
    for A in range(n) for B in range(n) for C in range(n)), nabla_eta(GamN)), (True, False))
einstein_div_for(GamN, "(ii) non-metricity: nabla_mu G^{mu nu} != 0")

# ---------------------------------------------------------------- B3: permute.py section 5
print("\nB3. permute.py SECTION 5 (read-only import): WHAT THE RK4 'MEASUREMENT' MEASURES")
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")  # read-only import
spec = importlib.util.spec_from_file_location(
    "permute_ro", "/home/user/Claude-Method-Works/research/warp-drive/permute.py")
pm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pm)
A_, Ad_, K_, W_ = sp.symbols('a adot k w', real=True)
rho_s = (Ad_ / A_) ** 2 + K_ / A_ ** 2
add_s = -sp.Rational(1, 2) * (rho_s + 3 * W_ * rho_s) * A_
Hs = Ad_ / A_
rhodot_s = 2 * Hs * (add_s / A_ - Hs ** 2) - 2 * K_ * Ad_ / A_ ** 3
chk("continuity_residual(a, adot, k, w) == 0 as an ALGEBRAIC identity (no trajectory)",
    sp.simplify(rhodot_s + 3 * Hs * (rho_s + W_ * rho_s)), 0)
rng = random.Random(7)
def _scaled_offtraj(a, adot, k, w):
    return abs(pm.continuity_residual(a, adot, k, w)) / abs(3.0 * (adot / a) * pm._rho(a, adot, k))


pts = []
while len(pts) < 1000:
    a_, ad_, k_, w_ = rng.uniform(0.2, 5), rng.uniform(-3, 3), rng.uniform(-1, 1), rng.uniform(-2, 1)
    if abs(ad_) > 1e-3 and abs(pm._rho(a_, ad_, k_)) > 1e-3:
        pts.append((a_, ad_, k_, w_))
off = max(_scaled_offtraj(*q) for q in pts)
chk("scaled residual (tree's own scaling, /3H rho) at 1000 random points OFF any trajectory < 1e-13",
    off < 1e-13, True)
print("     max scaled |residual| at random (a, adot, k, w): %.3e" % off)
table = {}
for w in (1 / 3, 0.0, -1.0, -2 / 3):
    for kk in (0.0, 0.25, -0.25):
        table[(w, kk)] = pm.worst_continuity_residual(w, kk)
worst = max(table.values())
chk("tree's fixture: residual < 1e-13 at all 12 (w, k) -- reproduced", worst < 1e-13, True)
print("     worst scaled residual over the 12 cases: %.3e" % worst)
series = [pm.worst_continuity_residual(1 / 3, 0.25, steps=nn) for nn in (500, 2000, 8000)]
print("     steps 500/2000/8000:", ["%.3e" % s for s in series])
chk("tree's residual_is_step_independent() returns True -- reproduced", pm.residual_is_step_independent(), True)


def wrong_resid(a, adot, k, w):  # positive control: acceleration law with 3w -> 2w
    rho_ = pm._rho(a, adot, k)
    add = -0.5 * (rho_ + 2.0 * w * rho_) * a
    H_ = adot / a
    rhodot = 2.0 * H_ * (add / a - H_ * H_) - 2.0 * k * adot / a ** 3
    return (rhodot + 3.0 * H_ * (rho_ + w * rho_)) / (3.0 * H_ * rho_)


chk("POSITIVE CONTROL: a wrong acceleration law (3w -> 2w) gives |residual| = |w|/3 = 1/9 at w=1/3",
    abs(abs(wrong_resid(1.0, 0.9, 0.19, 1 / 3)) - 1 / 9) < 1e-12, True)

# ---------------------------------------------------------------- C1/C2: hpscentre
print("\nC1. hpscentre.py divergence() FORMULA, STATIC SPHERICAL, DIAGONAL T(l)")
l = sp.symbols('l', real=True)
f = sp.Function('f')(l)
rr = sp.Function('r')(l)
XL = (t, l, th, ph)
gS = sp.diag(-f, 1, rr ** 2, rr ** 2 * sp.sin(th) ** 2)
ginvS = gS.inv()
GamS = christoffel(gS, ginvS, XL)
GamS = [[[sp.simplify(GamS[A][B][C]) for C in range(4)] for B in range(4)] for A in range(4)]
Ttt, Tll, Tth, Tph = [sp.Function(nm)(l) for nm in ('Ttt', 'Tll', 'Tth', 'Tph')]
Tm = sp.diag(Ttt, Tll, Tth, Tph)
dvS = div_mixed(GamS, Tm, XL)
f1, r1 = sp.diff(f, l), sp.diff(rr, l)
formula = sp.diff(Tll, l) + f1 / (2 * f) * (Tll - Ttt) + 2 * r1 / rr * (Tll - Tth)
chk("l-component equals hpscentre's formula (with T^ph_ph = T^th_th)",
    sp.simplify(dvS[1].subs(Tph, Tth) - formula), 0)
chk("t- and phi-components vanish identically", (dvS[0], dvS[3]), (0, 0))
chk("theta-component = cot(theta)(T^th_th - T^ph_ph): needs T^ph_ph = T^th_th",
    sp.simplify(dvS[2] - sp.cos(th) / sp.sin(th) * (Tth - Tph)), 0)
GS, GamS2, _ = einstein_mixed(gS, XL)
chk("nabla_mu G^mu_nu = 0 on this metric (the check at hpscentre.py:1235)", div_mixed(GamS2, GS, XL), [0, 0, 0, 0])

print("\nC2. hpscentre.py:1401 -- 'thth follows once tt, ll vanish (Bianchi)' NEEDS r' != 0")
Eth = sp.Function('Eth')(l)
resid = formula.subs({Ttt: 0, Tll: 0, Tth: Eth})
chk("with E^t_t = E^l_l = 0 the identity reads -(2 r'/r) E^th_th = 0",
    sp.simplify(resid + 2 * r1 / rr * Eth), 0)
throat = resid.subs(sp.Derivative(rr, l), 0)
chk("CONTROL: at r' = 0 (throat) the identity imposes nothing on E^th_th", sp.simplify(throat), 0)
xx = sp.symbols('x', positive=True)
c2, c4 = sp.symbols('c2 c4')
e0, e2 = sp.symbols('e0 e2')
# centre r = x + c2 x^3 + ...: r'/r = 1/x + O(x) -> E^th_th forced at every order where tt, ll vanish
cen = sp.series(-2 * sp.diff(xx + c2 * xx ** 3, xx) / (xx + c2 * xx ** 3) * (e0 + e2 * xx ** 2), xx, 0, 3).removeO()
chk("at a regular centre (r ~ x) the forcing is 2(e0/x + ...) -> e0 = e2 = 0 once it must vanish",
    sp.solve([sp.expand(cen * xx).coeff(xx, 0), sp.expand(cen * xx).coeff(xx, 2)], [e0, e2]), {e0: 0, e2: 0})

print("\n%d/%d checks pass" % (len(PASS), len(PASS) + len(FAIL)))
if FAIL:
    print("FAILED:", FAIL)
sys.exit(0 if not FAIL else 1)
