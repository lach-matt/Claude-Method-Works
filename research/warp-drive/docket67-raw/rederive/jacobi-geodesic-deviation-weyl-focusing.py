#!/usr/bin/env python3
"""
DOCKET 67 -- audit: jacobi-geodesic-deviation-weyl-focusing
(Jacobi / geodesic-deviation equation for null rays, optical tidal matrix,
Ricci = trace, Weyl = trace-free; Raychaudhuri-Sachs area focusing), as used in
research/warp-drive/concentric.py.

READ-ONLY toward research/: concentric.py and composite.py are imported (with
bytecode writing disabled) only to reproduce the tree's own numbers.

Checks
 J1  symbolic: for ANY traceless 2x2 K, det(lam I - K) = lam^2 + det K,
     det K invariant under K -> -K (area focusing quadratic & sign-blind);
     with a trace, det picks up a LINEAR term -lam tr K (Ricci focusing is
     first order and sign-bearing).
 J2  symbolic (sympy): linearised static metric -(1+2P)dt^2+(1-2P)dx^2,
     P = m/sqrt(r^2+a^2) + c.  Exact Riemann; exact null k; orthonormal
     screen.  O(m) trace of the optical tidal matrix = 2 lap(P) (density),
     O(m^2) trace for a = 0 = -4 m^2/b^4 at closest approach.
 J3  the shell constant c: tidal matrix changes only at O(m c).
 J4  reproduce the tree's |trace|/|max| (3.99e-1, 1.97e-2, 7.55e-4) and
     decompose: tree recipe (k = (1,1,0,0) non-null, coordinate screen,
     finite-difference h = 1e-3) vs exact-null orthonormal screen.
 J5  sign convention of composite.tidal vs MTW optical tidal matrix.
 J6  independent Jacobi integration (analytic Riemann, RK4, exactly null
     geodesic, orthonormal parallel screen, MTW sign) -> conjugate points vs
     the tree's 228.5 / 182.2 / 165.4 / 158.0 / 154.4 and 'none' at 3e-3;
     thin-lens estimate; geodesic-bundle truth at m = 5e-3.
"""
import math, sys, time
import sympy as sp

sys.dont_write_bytecode = True
TREE = "/home/user/Claude-Method-Works/research/warp-drive"

PASS = []
def check(label, cond, detail=""):
    PASS.append(bool(cond))
    print("  [%s] %s %s" % ("PASS" if cond else "FAIL", label, detail))

# ----------------------------------------------------------------- J1
print("J1  area focusing from a traceless tidal integral is quadratic and sign-blind")
lam, k1, k2, tr = sp.symbols("lam k1 k2 tr", real=True)
K0 = sp.Matrix([[k1, k2], [k2, -k1]])
d0 = sp.expand((lam * sp.eye(2) - K0).det())
check("det(lam I - K) = lam^2 - k1^2 - k2^2 for traceless K", sp.simplify(d0 - (lam**2 - k1**2 - k2**2)) == 0, str(d0))
check("invariant under K -> -K (sign-blind)", sp.simplify(d0 - sp.expand((lam * sp.eye(2) + K0).det())) == 0)
Kt = K0 + tr / 2 * sp.eye(2)
d1 = sp.expand((lam * sp.eye(2) - Kt).det())
check("with a trace: linear term -lam*tr appears (Ricci: first order, sign-bearing)",
      sp.simplify(d1 - (lam**2 - lam * tr + tr**2 / 4 - k1**2 - k2**2)) == 0, str(d1))

# ----------------------------------------------------------------- J2
print("\nJ2  exact Riemann of the tree's linearised metric (sympy)")
t, x, y, z = sp.symbols("t x y z", real=True)
m, a, c = sp.symbols("m a c", real=True)
X = [t, x, y, z]
r2 = x**2 + y**2 + z**2
P = m / sp.sqrt(r2 + a**2) + c
g = sp.diag(-(1 + 2 * P), 1 - 2 * P, 1 - 2 * P, 1 - 2 * P)
gi = sp.diag(*[1 / g[i, i] for i in range(4)])
Gam = [[[sp.simplify(sum(gi[A, E] * (sp.diff(g[E, B], X[C]) + sp.diff(g[E, C], X[B]) - sp.diff(g[B, C], X[E]))
                          for E in range(4)) / 2) for C in range(4)] for B in range(4)] for A in range(4)]
def Rup(A, B, C, D):
    return (sp.diff(Gam[A][B][D], X[C]) - sp.diff(Gam[A][B][C], X[D])
            + sum(Gam[A][C][E] * Gam[E][B][D] - Gam[A][D][E] * Gam[E][B][C] for E in range(4)))
t0 = time.time()
Rlow = {}
for A_ in range(4):
    for B_ in range(4):
        for C_ in range(4):
            for D_ in range(C_ + 1, 4):
                if A_ >= B_:
                    continue
                val = sum(g[A_, E] * Rup(E, B_, C_, D_) for E in range(4))
                Rlow[(A_, B_, C_, D_)] = val
def Rl(A_, B_, C_, D_):
    s = 1
    if A_ == B_ or C_ == D_:
        return 0
    if A_ > B_:
        A_, B_, s = B_, A_, -s
    if C_ > D_:
        C_, D_, s = D_, C_, -s
    return s * Rlow[(A_, B_, C_, D_)]
print("       Riemann built in %.1f s" % (time.time() - t0))
args = (x, y, z, m, a, c)
Rnum = {key: sp.lambdify(args, val, "math") for key, val in Rlow.items()}
Gnum = [[[sp.lambdify(args, Gam[A_][B_][C_], "math") for C_ in range(4)] for B_ in range(4)] for A_ in range(4)]
Pnum = sp.lambdify(args, P, "math")

def Rn(p, mm, aa, cc):
    vals = {key: f(p[0], p[1], p[2], mm, aa, cc) for key, f in Rnum.items()}
    def get(A_, B_, C_, D_):
        s = 1
        if A_ == B_ or C_ == D_:
            return 0.0
        if A_ > B_:
            A_, B_, s = B_, A_, -s
        if C_ > D_:
            C_, D_, s = D_, C_, -s
        return s * vals[(A_, B_, C_, D_)]
    return get

def metric_num(p, mm, aa, cc):
    f = Pnum(p[0], p[1], p[2], mm, aa, cc)
    return [-(1 + 2 * f), 1 - 2 * f, 1 - 2 * f, 1 - 2 * f]

def tidal_mtw(p, k, E, mm, aa, cc):
    """MTW optical tidal matrix R_{a b c d} e_i^a k^b e_j^c k^d."""
    R = Rn(p, mm, aa, cc)
    out = [[0.0, 0.0], [0.0, 0.0]]
    for i in range(2):
        for j in range(2):
            s = 0.0
            for A_ in range(4):
                if E[i][A_] == 0: continue
                for B_ in range(4):
                    if k[B_] == 0: continue
                    for C_ in range(4):
                        if E[j][C_] == 0: continue
                        for D_ in range(4):
                            if k[D_] == 0: continue
                            s += R(A_, B_, C_, D_) * E[i][A_] * k[B_] * E[j][C_] * k[D_]
            out[i][j] = s
    return out

def null_screen_at(p, mm, aa, cc):
    gg = metric_num(p, mm, aa, cc)
    k = [1.0, math.sqrt(-gg[0] / gg[1]), 0.0, 0.0]
    e1 = [0.0, 0.0, 1 / math.sqrt(gg[2]), 0.0]
    e2 = [0.0, 0.0, 0.0, 1 / math.sqrt(gg[3])]
    return k, (e1, e2)

# symbolic O(m) and O(m^2) trace at closest approach (0,b,0) along x
b = sp.symbols("b", positive=True)
eps = sp.symbols("eps", real=True)
pt = {x: 0, y: b, z: 0}
Pb = P.subs(pt)
kt = 1
kx = sp.sqrt((1 + 2 * Pb) / (1 - 2 * Pb))
ktr = 0
for (iy, e) in ((2, 1 / sp.sqrt(1 - 2 * Pb)), (3, 1 / sp.sqrt(1 - 2 * Pb))):
    kk = [kt, kx, 0, 0]
    s = 0
    for B_ in (0, 1):
        for D_ in (0, 1):
            s += Rl(iy, B_, iy, D_).subs(pt) * e * e * kk[B_] * kk[D_]
    ktr += s
lap = sum(sp.diff(m / sp.sqrt(r2 + a**2), v, 2) for v in (x, y, z)).subs(pt)
ser = sp.series(ktr.subs(c, 0).subs(m, eps * m), eps, 0, 3).removeO()
o1 = sp.simplify(ser.coeff(eps, 1) * eps / eps)
o2 = sp.simplify(ser.coeff(eps, 2))
check("O(m) trace of MTW tidal matrix at (0,b,0) = 2 lap(Phi): Ricci linear in density",
      sp.simplify(o1 - 2 * lap) == 0, "O(m) = %s" % sp.simplify(o1))
o2pm = sp.simplify(o2.subs(a, 0))
check("O(m^2) trace at a = 0 = -4 m^2/b^4 (linearised metric not vacuum at 2nd order)",
      sp.simplify(o2pm + 4 * m**2 / b**4) == 0, "O(m^2)|a=0 = %s" % o2pm)

# ----------------------------------------------------------------- J3
print("\nJ3  the shell's interior constant c changes the tidal field only at O(m c)")
mm, bb = 5e-3, 1.0
for aa in (0.02,):
    k, E = null_screen_at((0.0, bb, 0.0), mm, aa, 0.0)
    T0 = tidal_mtw((0.0, bb, 0.0), k, E, mm, aa, 0.0)
    cc = -mm / 200.0
    k, E = null_screen_at((0.0, bb, 0.0), mm, aa, cc)
    Tc = tidal_mtw((0.0, bb, 0.0), k, E, mm, aa, cc)
    rel = abs(Tc[0][0] - T0[0][0]) / abs(T0[0][0])
    check("|T(c=-m/R_s) - T(0)|/|T| <= 10|c| (c = %.1e)" % cc, rel < 10 * abs(cc), "rel = %.3e" % rel)
    # flatness of the pure-constant metric
    Rc = Rn((0.3, 0.7, 0.1), 0.0, aa, cc)
    check("P = constant alone: Riemann identically 0 (shell interior is flat)",
          max(abs(Rc(*kk)) for kk in Rlow) == 0.0)

# ----------------------------------------------------------------- J4, J5
print("\nJ4  the tree's |trace|/|max| reproduced and decomposed (m = 5e-3, b = 1, R_s = 200)")
sys.path.insert(0, TREE)
import concentric, composite
tree_vals = {0.5: 3.99e-1, 0.1: 1.97e-2, 0.02: 7.55e-4}
cc = -mm / 200.0
rows = []
for aa in (0.5, 0.1, 0.02):
    tr_tree = concentric.trace_ratio(mm, a=aa)
    # tree recipe with EXACT derivatives: k=(1,1,0,0), coordinate screen
    kT = [1.0, 1.0, 0.0, 0.0]
    ET = ([0., 0., 1., 0.], [0., 0., 0., 1.])
    Tt = tidal_mtw((0.0, bb, 0.0), kT, ET, mm, aa, cc)
    rec_exact = abs(Tt[0][0] + Tt[1][1]) / max(abs(Tt[0][0]), abs(Tt[1][1]))
    # exact null k, orthonormal screen
    k, E = null_screen_at((0.0, bb, 0.0), mm, aa, cc)
    Tn = tidal_mtw((0.0, bb, 0.0), k, E, mm, aa, cc)
    null_exact = abs(Tn[0][0] + Tn[1][1]) / max(abs(Tn[0][0]), abs(Tn[1][1]))
    # linear-order density part alone: 2 lap(P) / T_max(linear)
    lapv = -3 * mm * aa**2 / (bb**2 + aa**2) ** 2.5
    Tn_lin = tidal_mtw((0.0, bb, 0.0), k, E, mm * 1e-4, aa, cc * 1e-4)
    dens_part = abs(2 * lapv * 1e-4) / max(abs(Tn_lin[0][0]), abs(Tn_lin[1][1]))
    # finite-difference h dependence of the tree's own tidal
    composite.phi = concentric.potential(mm, aa, 200.0)
    hs = {}
    for h in (4e-3, 1e-3, 2.5e-4):
        R = composite.riemann_lower((0.0, bb, 0.0), mm, h=h)
        Tf = [[-sum(R[m_][a_][n_][b_] * kT[m_] * ET[i][a_] * kT[n_] * ET[j][b_]
                    for m_ in range(4) for a_ in range(4) for n_ in range(4) for b_ in range(4))
               for j in range(2)] for i in range(2)]
        hs[h] = abs(Tf[0][0] + Tf[1][1]) / max(abs(Tf[0][0]), abs(Tf[1][1]))
    rows.append((aa, tr_tree, rec_exact, null_exact, dens_part, hs))
    print("   a=%.2f tree=%.4e (quoted %.3g)  recipe-exact=%.4e  null-screen-exact=%.4e  density-only(O(m))=%.4e"
          % (aa, tr_tree, tree_vals[aa], rec_exact, null_exact, dens_part))
    print("          tree tidal FD h: 4e-3 -> %.4e, 1e-3 -> %.4e, 2.5e-4 -> %.4e" % (hs[4e-3], hs[1e-3], hs[2.5e-4]))
for aa, tr_tree, rec_exact, null_exact, dens_part, hs in rows:
    check("tree reproduces its quoted ratio at a=%.2f" % aa, abs(tr_tree / tree_vals[aa] - 1) < 0.01, "%.4e" % tr_tree)
a02 = rows[2]
check("a=0.02: exact-null ratio is several times the tree's 7.55e-4 (tree k=(1,1,0,0) non-null)",
      a02[3] > 5 * a02[1], "null %.3e vs tree %.3e" % (a02[3], a02[1]))
check("a=0.02: exact-null ratio ~ density part + 4m/(3b) (O(m^2) of linearised metric)",
      abs(a02[3] - (a02[4] + 4 * mm / 3)) / a02[3] < 0.05,
      "%.3e vs %.3e + %.3e" % (a02[3], a02[4], 4 * mm / 3))
check("a=0.02: tree's 7.55e-4 ~ the O(m) density part alone (non-null-k term cancels the O(m^2))",
      abs(a02[1] / a02[4] - 1) < 0.1, "tree %.3e vs density %.3e" % (a02[1], a02[4]))
check("a=0.5 and 0.1: ratio is density-dominated on either recipe (monotone conclusion stands)",
      rows[0][3] > rows[1][3] > rows[2][3] and rows[0][1] > rows[1][1] > rows[2][1])
g_kk = metric_num((0.0, bb, 0.0), mm, 0.02, cc)
gkk = g_kk[0] + g_kk[1]
check("k = (1,1,0,0) is NOT null at (0,1,0): g(k,k) = -4 Phi", abs(gkk + 4 * Pnum(0.0, bb, 0.0, mm, 0.02, cc)) < 1e-15,
      "g(k,k) = %.4e" % gkk)

print("\nJ5  sign of composite.tidal against the MTW optical tidal matrix")
composite.phi = concentric.potential(mm, 0.02, 200.0)
kT = [1.0, 1.0, 0.0, 0.0]
Ttree = composite.tidal((0.0, bb, 0.0), kT, [0., 0., 1., 0.], [0., 0., 0., 1.], mm)
Tm = tidal_mtw((0.0, bb, 0.0), kT, ([0., 0., 1., 0.], [0., 0., 0., 1.]), mm, 0.02, cc)
check("composite.tidal = -(MTW tidal) at (0,1,0), a = 0.02", abs(Ttree[0][0] + Tm[0][0]) / abs(Tm[0][0]) < 1e-3,
      "tree T_yy = %+.5e, MTW = %+.5e" % (Ttree[0][0], Tm[0][0]))

# ----------------------------------------------------------------- J6
print("\nJ6  independent Jacobi integration (analytic Riemann, MTW sign) vs tree conjugate points")

def christ(p, mm_, aa, cc_):
    return [[[Gnum[A_][B_][C_](p[0], p[1], p[2], mm_, aa, cc_) for C_ in range(4)] for B_ in range(4)] for A_ in range(4)]

def deriv(state, mm_, aa, cc_, sgn):
    xx, kk, e1, e2, A, dA = state
    p = (xx[1], xx[2], xx[3])
    G = christ(p, mm_, aa, cc_)
    acc = [-sum(G[q][al][be] * kk[al] * kk[be] for al in range(4) for be in range(4)) for q in range(4)]
    de = []
    for e in (e1, e2):
        de.append([-sum(G[q][al][be] * kk[al] * e[be] for al in range(4) for be in range(4)) for q in range(4)])
    T = tidal_mtw(p, kk, (e1, e2), mm_, aa, cc_)
    ddA = [[-sgn * sum(T[r_][s_] * A[s_][c_] for s_ in range(2)) for c_ in range(2)] for r_ in range(2)]
    return (kk, acc, de[0], de[1], dA, ddA)

def axpy(state, d, h):
    out = []
    for s_, d_ in zip(state, d):
        if isinstance(s_[0], list):
            out.append([[s_[i][j] + h * d_[i][j] for j in range(2)] for i in range(2)])
        else:
            out.append([s_[i] + h * d_[i] for i in range(4)])
    return out

def jacobi(mm_, aa=0.02, Rs=200.0, bb_=1.0, x0=-150.0, L=300.0, n=1500, sgn=+1, theta=0.0):
    cc_ = -mm_ / Rs          # inside the shell for the whole ray (max r < 200)
    p0 = (x0, bb_, 0.0)
    gg = metric_num(p0, mm_, aa, cc_)
    s = math.sqrt(-gg[0] / gg[1])
    k0 = [1.0, s * math.cos(theta), s * math.sin(theta), 0.0]
    e1 = [0.0, 0.0, 1 / math.sqrt(gg[2]), 0.0]
    e2 = [0.0, 0.0, 0.0, 1 / math.sqrt(gg[3])]
    st = [[0.0, p0[0], p0[1], p0[2]], k0, e1, e2, [[0.0, 0.0], [0.0, 0.0]], [[1.0, 0.0], [0.0, 1.0]]]
    h = L / n
    conj, prev_det, rmax = None, None, 0.0
    traj = []
    for i in range(n):
        traj.append(list(st[0]))
        dA = st[4]
        det = dA[0][0] * dA[1][1] - dA[0][1] * dA[1][0]
        if i > 5 and conj is None and det <= 0.0:
            conj = (i - 1) * h + h * prev_det / (prev_det - det)
        prev_det = det
        rmax = max(rmax, math.sqrt(st[0][1]**2 + st[0][2]**2 + st[0][3]**2))
        d1 = deriv(st, mm_, aa, cc_, sgn)
        d2 = deriv(axpy(st, d1, h / 2), mm_, aa, cc_, sgn)
        d3 = deriv(axpy(st, d2, h / 2), mm_, aa, cc_, sgn)
        d4 = deriv(axpy(st, d3, h), mm_, aa, cc_, sgn)
        comb = []
        for q in range(6):
            if isinstance(st[q][0], list):
                comb.append([[(d1[q][i_][j] + 2 * d2[q][i_][j] + 2 * d3[q][i_][j] + d4[q][i_][j]) / 6 for j in range(2)] for i_ in range(2)])
            else:
                comb.append([(d1[q][i_] + 2 * d2[q][i_] + 2 * d3[q][i_] + d4[q][i_]) / 6 for i_ in range(4)])
        st = axpy(st, comb, h)
    traj.append(list(st[0]))
    gk = metric_num((st[0][1], st[0][2], st[0][3]), mm_, aa, cc_)
    null_res = sum(gk[i_] * st[1][i_]**2 for i_ in range(4))
    return conj, rmax, null_res, traj, h

tree_conj = {5e-3: 228.5, 1e-2: 182.2, 2e-2: 165.4, 4e-2: 158.0, 8e-2: 154.4}
t0 = time.time()
res = {}
for mm_ in (3e-3, 5e-3, 1e-2, 2e-2, 4e-2, 8e-2):
    cj, rmax, nr, _, _ = jacobi(mm_, n=1500)
    f = 1.0 / (4 * mm_)
    thin = 150.0 + (1 / (1 / f - 1 / 150.0) if 1 / f > 1 / 150.0 else float("inf"))
    res[mm_] = cj
    print("   m=%.0e  conj(MTW, analytic) = %s   tree = %s   thin-lens 150+v = %.1f   g(k,k)_end = %.1e"
          % (mm_, ("%.2f" % cj) if cj else "none", tree_conj.get(mm_, "none"), thin, nr))
print("       (%.0f s)" % (time.time() - t0))
check("m=3e-3: no conjugate point within L = 300 (tree: 'none')", res[3e-3] is None)
for mm_, tv in tree_conj.items():
    check("m=%.0e: independent conjugate point within 0.5 of tree's %.1f" % (mm_, tv),
          res[mm_] is not None and abs(res[mm_] - tv) < 0.5, "%.2f" % (res[mm_] or -1))
print("   the tree's sign (A'' = +R A, composite.tidal = -MTW) re-run in the independent integrator:")
flip = {}
for mm_, tv in tree_conj.items():
    flip[mm_], _, _, _, _ = jacobi(mm_, n=1500, sgn=-1)
    print("   m=%.0e  MTW-sign %.3f   tree-sign %.3f   shift %+.3f   tree %.1f" % (mm_, res[mm_], flip[mm_], flip[mm_] - res[mm_], tv))
check("tree-sign integration reproduces the tree's own 228.45 to < 0.1 at m=5e-3",
      abs(flip[5e-3] - 228.45) < 0.1, "%.3f" % flip[5e-3])
check("the sign convention shifts the m=5e-3 conjugate point by 0.1-0.3 (> tree's quoted +-0.04)",
      0.1 < abs(flip[5e-3] - res[5e-3]) < 0.3, "%.3f" % (flip[5e-3] - res[5e-3]))
check("the sign convention never moves a conjugate point by more than 0.5 % (seats/no-seat unchanged)",
      all(abs(flip[k] - res[k]) / res[k] < 5e-3 for k in flip))
cj_fine, _, _, _, _ = jacobi(5e-3, n=3000)
check("converged: n=3000 moves the m=5e-3 conjugate point by < 0.05", abs(cj_fine - res[5e-3]) < 0.05,
      "%.3f vs %.3f" % (cj_fine, res[5e-3]))

# geodesic-bundle truth: perturb initial direction in y, find zero of screen separation
def bundle(mm_):
    _, _, _, tr0, h0 = jacobi(mm_, n=1500)
    _, _, _, tr1, _ = jacobi(mm_, n=1500, theta=1e-6)
    sep = [tr1[i][2] - tr0[i][2] for i in range(len(tr0))]
    for i in range(10, len(sep)):
        if sep[i - 1] > 0 and sep[i] <= 0:
            return (i - 1) * h0 + h0 * sep[i - 1] / (sep[i - 1] - sep[i])
    return None
print("   bundle truth: rays from the source point, direction perturbed by 1e-6 in the (x,y) plane")
for mm_ in (5e-3, 2e-2):
    zc = bundle(mm_)
    print("   m=%.0e  bundle %.3f   Jacobi MTW-sign %.3f   Jacobi tree-sign %.3f   tree %.1f" % (mm_, zc, res[mm_], flip[mm_], tree_conj[mm_]))
    check("m=%.0e: radial neighbour ray crosses within 0.1 of the MTW-sign Jacobi point" % mm_,
          zc is not None and abs(zc - res[mm_]) < 0.1, "bundle %.3f vs %.3f" % (zc or -1, res[mm_]))
    check("m=%.0e: MTW sign is closer to bundle truth than the tree's sign" % mm_,
          abs(zc - res[mm_]) < abs(zc - flip[mm_]), "|d| %.3f vs %.3f" % (abs(zc - res[mm_]), abs(zc - flip[mm_])))
check("... the RADIAL direction focuses for the negative-mass (repulsive) core", zc is not None)

# tree's own survey at m = 5e-3 (for the record)
t0 = time.time()
sv = concentric.survey(5e-3)
check("tree's survey(5e-3) conjugate = 228.45 +- 0.3", abs(sv["conjugate"] - 228.45) < 0.3, "%.3f (%.0f s)" % (sv["conjugate"], time.time() - t0))

print("\n%d/%d PASS" % (sum(PASS), len(PASS)))
sys.exit(0 if all(PASS) else 1)
