#!/usr/bin/env python3
"""
DOCKET 67 / vacuum-ricci-flat-traceless-tidal -- re-derivation and machine checks.

External result as the tree uses it (composite.py:43-44, 105-106, 230, 319-335):
  "vacuum demands R_kk = 0, so the optical tidal matrix is TRACELESS: what focuses
   is pure Weyl."
Standard content (Sachs 1961; restated as Gao & Wald 2000 eq.13 splitting focusing
into sigma^2 + R_kk): on a screen {e1,e2} orthogonal to a null k (and an auxiliary
null l, k.l = -1), T_ij = R_{a m b n} e_i^a k^m e_j^b k^n (MTW sign) satisfies
   tr T = R_ab k^a k^b    and    T = C-part (trace-free) + (1/2) R_kk * I.
Vacuum Einstein (R_ab = 0, Lambda = 0) => tr T = 0.

Checks
  V1  PROOF (4D, by linearity): the algebraic curvature tensors of 4D Minkowski
      span a 20-dim space; Kulkarni-Nomizu products of elementary symmetric
      matrices give a basis (rank asserted = 20).  On every basis element, exact
      rational arithmetic: tr T = R_kk; Weyl part of T has trace 0; T - T_Weyl =
      (1/2) R_kk I.  Linear in R + tensorial => holds for every curvature tensor
      and every null k / screen.
  V1v vacuity guard: an element with R_kk != 0 exists in the basis (trace not
      trivially 0).
  V2  exact Schwarzschild (areal chart, symbolic M, NO sign assumption): all 10
      Ricci components vanish; explicit screen on a generic null vector: tr T = 0,
      T eigenvalues +-3 M L^2 / r^5.  Holds for M < 0 (r > 0) too.
  V3  the tree's metric -(1+2Phi)dt^2+(1-2Phi)dx^2, Phi = -M/r, is NOT Ricci-flat:
      R_kk (exactly null k along +x) = 0 at O(M), nonzero at O(M^2); exact value at
      the tree's static point.
  V4  reproduce the tree's static figure 1.62e-4 (composite.py:322-325) with exact
      derivatives, and split it: non-null k = (1,1,0,0) (g(k,k) = -4 Phi) vs the
      genuine O(M^2) Ricci of the linearised metric.
  V5  sign convention of composite.tidal vs MTW, and which transverse direction
      physically converges for M > 0 (neighbouring geodesics with the tree's own
      integrator, convention-free).  A discrepancy, not a refutation of V1-V2.
  V6  along-ray trace leak with the tree's Euler screen transport (composite.py:331).
"""
import sys, os, math, itertools
import sympy as sp

TREE = "/home/user/Claude-Method-Works/research/warp-drive"
results = []
def rec(name, ok, val=""):
    results.append((name, bool(ok), val))
    print("%-5s %-74s %s" % ("PASS" if ok else "FAIL", name, val))

# ------------------------------------------------------------------ V1
eta = sp.diag(-1, 1, 1, 1)
def kn(h, k):
    R = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a, b, c, d in itertools.product(range(4), repeat=4):
        R[a][b][c][d] = h[a, c]*k[b, d] + h[b, d]*k[a, c] - h[a, d]*k[b, c] - h[b, c]*k[a, d]
    return R
def Esym(p, q):
    m = sp.zeros(4, 4); m[p, q] = 1; m[q, p] = 1; return m
syms = [Esym(p, q) for p in range(4) for q in range(p, 4)]
cands = []
for i in range(len(syms)):
    for j in range(i, len(syms)):
        cands.append(kn(syms[i], syms[j]))
def flat(R): return [R[a][b][c][d] for a, b, c, d in itertools.product(range(4), repeat=4)]
Mflat = sp.Matrix([flat(R) for R in cands])
rank = Mflat.rank()
rec("V1a Kulkarni-Nomizu products span the algebraic curvature tensors (rank)", rank == 20, "rank=%d" % rank)
# pick a basis
basis, cur = [], sp.zeros(0, 256)
for R in cands:
    t = cur.col_join(sp.Matrix([flat(R)]))
    if t.rank() > cur.rows:
        cur = t; basis.append(R)
    if len(basis) == 20: break
# symmetry sanity on basis (pair antisym, pair sym, first Bianchi)
def symok(R):
    for a, b, c, d in itertools.product(range(4), repeat=4):
        if R[a][b][c][d] != -R[b][a][c][d] or R[a][b][c][d] != -R[a][b][d][c] \
           or R[a][b][c][d] != R[c][d][a][b] or R[a][b][c][d] + R[a][c][d][b] + R[a][d][b][c] != 0:
            return False
    return True
rec("V1b every basis element has Riemann symmetries incl. first Bianchi", all(symok(R) for R in basis), "20 elements")
etai = eta.inv()
k = [1, 1, 0, 0]; l = [sp.Rational(1, 2), -sp.Rational(1, 2), 0, 0]
e = [[0, 0, 1, 0], [0, 0, 0, 1]]
kl = sum(eta[a, b]*k[a]*l[b] for a in range(4) for b in range(4))
def ricci(R):
    return [[sum(etai[a, c]*R[a][b][c][d] for a in range(4) for c in range(4)) for d in range(4)] for b in range(4)]
def weyl(R):
    Ric = ricci(R); Rs = sum(etai[b, d]*Ric[b][d] for b in range(4) for d in range(4))
    g = eta; C = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a, b, c, d in itertools.product(range(4), repeat=4):
        C[a][b][c][d] = (R[a][b][c][d]
            - sp.Rational(1, 2)*(g[a, c]*Ric[b][d] - g[a, d]*Ric[b][c] + g[b, d]*Ric[a][c] - g[b, c]*Ric[a][d])
            + Rs/6*(g[a, c]*g[b, d] - g[a, d]*g[b, c]))
    return C
def tid(R):   # MTW: A'' = -T A,  T_ij = R_{a m b n} e_i^a k^m e_j^b k^n
    return sp.Matrix(2, 2, lambda i, j: sum(R[a][m][b][n]*e[i][a]*k[m]*e[j][b]*k[n]
                                           for a, m, b, n in itertools.product(range(4), repeat=4)))
ok_tr = ok_w = ok_split = ok_wtrace = True; nonzero_rkk = 0
for R in basis:
    Ric = ricci(R); Rkk = sum(Ric[b][d]*k[b]*k[d] for b in range(4) for d in range(4))
    T = tid(R); C = weyl(R); TC = tid(C)
    Cric = ricci(C)
    ok_wtrace &= all(Cric[b][d] == 0 for b in range(4) for d in range(4))
    ok_tr &= (T.trace() - Rkk == 0)
    ok_w &= (TC.trace() == 0)
    ok_split &= (T - TC - Rkk/2*sp.eye(2) == sp.zeros(2, 2))
    nonzero_rkk += (Rkk != 0)
rec("V1c k.l = -1, screen orthonormal and orthogonal to k,l", kl == -1, "k.l=%s" % kl)
rec("V1d Weyl tensor built from each basis element is totally trace-free", ok_wtrace, "")
rec("V1e tr T = R_ab k^a k^b on all 20 basis elements (=> every R, by linearity)", ok_tr, "exact rationals")
rec("V1f tr T_Weyl = 0 on all 20 (Weyl focusing is trace-free)", ok_w, "")
rec("V1g T = T_Weyl + (1/2) R_kk I on all 20", ok_split, "")
rec("V1v vacuity guard: R_kk != 0 on some basis element", nonzero_rkk > 0, "%d of 20 have R_kk != 0" % nonzero_rkk)

# V1h cosmological constant: vacuum with Lambda, R_ab = Lambda g_ab; maximally symmetric part
Lam = sp.symbols('Lambda')
RL_ds = [[[[Lam/3*(eta[a, c]*eta[b, d] - eta[a, d]*eta[b, c]) for d in range(4)] for c in range(4)]
          for b in range(4)] for a in range(4)]
Ric_ds = ricci(RL_ds)
rec("V1h Lambda-vacuum (R_ab = Lambda g_ab, not Ricci-flat): R_kk = Lambda g(k,k) = 0, tr T = 0",
    all(sp.simplify(Ric_ds[b][d] - Lam*eta[b, d]) == 0 for b in range(4) for d in range(4))
    and sp.simplify(tid(RL_ds).trace()) == 0, "tr T = %s" % sp.simplify(tid(RL_ds).trace()))

# ------------------------------------------------------------------ V2
t, r, th, ph, M = sp.symbols('t r theta phi M', real=True)
X = [t, r, th, ph]
f = 1 - 2*M/r
g = sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2); gi = g.inv()
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
         for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
def Rup(a, b, c, d):
    return (sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
            + sum(Gam[a][c][q]*Gam[q][b][d] - Gam[a][d][q]*Gam[q][b][c] for q in range(4)))
RU = [[[[sp.simplify(Rup(a, b, c, d)) for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
Ric2 = [[sp.simplify(sum(RU[a][b][a][d] for a in range(4))) for d in range(4)] for b in range(4)]
rec("V2a Schwarzschild, symbolic M (any sign): all Ricci components = 0",
    all(Ric2[b][d] == 0 for b in range(4) for d in range(4)), "")
RL = [[[[sp.simplify(sum(g[a, q]*RU[q][b][c][d] for q in range(4))) for d in range(4)] for c in range(4)]
       for b in range(4)] for a in range(4)]
E, L = sp.symbols('E L', positive=True)
thv = sp.pi/2
kr = sp.sqrt(E**2 - f*L**2/r**2)
kv = [E/f, kr, 0, L/r**2]
sub = {th: thv}
gs = g.subs(sub)
null = sp.simplify(sum(gs[a, b]*kv[a]*kv[b] for a in range(4) for b in range(4)))
e1 = [0, 0, 1/r, 0]
# e2: spacelike unit in (t,r,phi), orthogonal to k: take e2 = alpha*(d_t-ish) ; solve generally
p, q_ = sp.symbols('p q')
e2g = [p, q_, 0, 0]  # combos of t,r plus we add phi part w
w = sp.symbols('w')
e2g = [p, q_, 0, w]
eqs = [sp.expand(sum(gs[a, b]*e2g[a]*kv[b] for a in range(4) for b in range(4)))]
# choose w = 0 is not always possible; choose p = 0 then q from orth, then normalise
sol = sp.solve([eqs[0].subs(p, 0)], [q_], dict=True)[0]
e2 = [0, sol[q_], 0, w]
n2 = sp.simplify(sum(gs[a, b]*e2[a]*e2[b] for a in range(4) for b in range(4)))
e2 = [sp.simplify(c/sp.sqrt(n2)) for c in e2]
e2 = [c.subs(w, 1) for c in e2]
def Tij(u, v):
    return sp.simplify(sum(RL[a][m][b][n].subs(sub)*u[a]*kv[m]*v[b]*kv[n]
                           for a, m, b, n in itertools.product(range(4), repeat=4)))
T11, T22, T12 = Tij(e1, e1), Tij(e2, e2), Tij(e1, e2)
rec("V2b k null (generic E, L, r)", null == 0, "g(k,k)=%s" % null)
rec("V2c exact Schwarzschild optical tidal matrix: tr T = 0 identically", sp.simplify(T11 + T22) == 0,
    "T11=%s T22=%s T12=%s" % (T11, sp.simplify(T22), T12))
rec("V2d eigenvalues +-3 M L^2/r^5 (sign of M only swaps the focusing direction)",
    sp.simplify(T11 - 3*M*L**2/r**5) == 0 or sp.simplify(T11 + 3*M*L**2/r**5) == 0, "T11=%s" % T11)

# ------------------------------------------------------------------ V3/V4 linearised metric
x, y, z = sp.symbols('x y z', real=True)
Y = [t, x, y, z]
rr = sp.sqrt(x**2 + y**2 + z**2)
Phi = -M/rr
gl = sp.diag(-(1 + 2*Phi), 1 - 2*Phi, 1 - 2*Phi, 1 - 2*Phi); gli = gl.inv()
Gl = [[[sum(gli[a, d]*(sp.diff(gl[d, b], Y[c]) + sp.diff(gl[d, c], Y[b]) - sp.diff(gl[b, c], Y[d]))
        for d in range(4))/2 for c in range(4)] for b in range(4)] for a in range(4)]
def RupL(a, b, c, d):
    return (sp.diff(Gl[a][b][d], Y[c]) - sp.diff(Gl[a][b][c], Y[d])
            + sum(Gl[a][c][q]*Gl[q][b][d] - Gl[a][d][q]*Gl[q][b][c] for q in range(4)))
bv, Mv = sp.Rational(3, 10), sp.Rational(-2, 1000)
pt = {x: 0, y: bv, z: 0}
def RLnum(Msub, point):
    RUn = [[[[RupL(a, b, c, d) for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
    out = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    gln = gl.subs(point).subs(M, Msub)
    for a, b, c, d in itertools.product(range(4), repeat=4):
        out[a][b][c][d] = sp.nsimplify(0) if False else sum(gln[a, q]*RUn[q][b][c][d].subs(point).subs(M, Msub) for q in range(4))
    return out
# symbolic R_kk with exactly null k along +x
gxx = (1 - 2*Phi); gtt = (1 + 2*Phi)
kx_null = sp.sqrt(gtt/gxx)
knull = [1, kx_null, 0, 0]
Rkk_sym = sum(sum(RupL(a, b, a, d) for a in range(4))*knull[b]*knull[d] for b in range(4) for d in range(4))
Rkk_pt = sp.simplify(Rkk_sym.subs(pt))
ser = sp.series(Rkk_pt, M, 0, 3).removeO()
c1, c2 = sp.simplify(ser.coeff(M, 1)), sp.simplify(ser.coeff(M, 2))
rec("V3a linearised metric, null k along +x at closest approach: R_kk O(M) = 0", c1 == 0, "O(M) coeff=%s" % c1)
rec("V3b ... but O(M^2) != 0 (NOT an exact vacuum)", c2 != 0, "R_kk = %s * M^2 + O(M^3)" % c2)
Rkk_exact = sp.N(Rkk_pt.subs(M, Mv), 20)
# generic point off closest approach, symbolic O(M^2)
ser_g = sp.series(sp.simplify(Rkk_sym.subs({z: 0})), M, 0, 3).removeO()
c1g = sp.simplify(ser_g.coeff(M, 1)); c2g = sp.simplify(ser_g.coeff(M, 2))
rec("V3c along the whole ray (x, y, 0): R_kk O(M) = 0 identically", c1g == 0, "O(M^2) coeff = %s" % c2g)

# tidal matrices at the static point, exact derivatives
RLp = RLnum(Mv, pt)
def Tmat(RLx, kk, ee, sign=+1):
    return sp.Matrix(2, 2, lambda i, j: sign*sum(RLx[a][m][b][n]*ee[i][a]*kk[m]*ee[j][b]*kk[n]
                                                for a, m, b, n in itertools.product(range(4), repeat=4)))
ee_tree = [[0, 0, 1, 0], [0, 0, 0, 1]]
T_tree_exact = Tmat(RLp, [1, 1, 0, 0], ee_tree, sign=-1)   # composite.tidal convention
ratio_tree_exact = abs(T_tree_exact.trace()) / max(abs(T_tree_exact[0, 0]), abs(T_tree_exact[1, 1]))
sys.path.insert(0, TREE)
import composite as C
Tfd = C.tidal((0.0, 0.3, 0.0), [1.0, 1.0, 0.0, 0.0], [0., 0., 1., 0.], [0., 0., 0., 1.], -2.0e-3)
ratio_fd = abs(Tfd[0][0] + Tfd[1][1]) / max(abs(Tfd[0][0]), abs(Tfd[1][1]))
gln = gl.subs(pt).subs(M, Mv)
gkk = sp.N(gln[0, 0] + gln[1, 1], 15)
kn_ = [1, sp.sqrt(-gln[0, 0]/gln[1, 1]), 0, 0]
en_ = [[0, 0, 1/sp.sqrt(gln[2, 2]), 0], [0, 0, 0, 1/sp.sqrt(gln[3, 3])]]
T_null = Tmat(RLp, kn_, en_, sign=+1)
ratio_null = abs(sp.N(T_null.trace())) / max(abs(sp.N(T_null[0, 0])), abs(sp.N(T_null[1, 1])))
def tid_h(p, kk, e1, e2, Mm, h):
    R = C.riemann_lower(p, Mm, h); EE = (e1, e2)
    return [[-sum(R[m][a][n][b]*kk[m]*EE[i][a]*kk[n]*EE[j][b] for m in range(4) for a in range(4)
                  for n in range(4) for b in range(4)) for j in range(2)] for i in range(2)]
hs = (4e-3, 2e-3, 1e-3, 5e-4, 2.5e-4, 1e-4, 5e-5)
sweep = []
for hh in hs:
    Th = tid_h((0.0, 0.3, 0.0), [1.0, 1.0, 0.0, 0.0], [0., 0., 1., 0.], [0., 0., 0., 1.], -2.0e-3, hh)
    sweep.append(abs(Th[0][0] + Th[1][1]) / max(abs(Th[0][0]), abs(Th[1][1])))
print("       h-sweep of the tree's static ratio:", ", ".join("h=%g:%.3e" % (hh, v) for hh, v in zip(hs, sweep)))
rec("V4a tree's static 1.62e-4 reproduced at its own h = 1e-3", abs(ratio_fd - 1.6229e-4) < 5e-7, "FD %.4e" % ratio_fd)
rec("V4b DISCREPANCY: the ratio is NOT h-independent (composite.py:326 says it is): x29 over h 4e-3..5e-5",
    sweep[0] / sweep[-1] > 10, "h=4e-3: %.3e -> h=5e-5: %.3e" % (sweep[0], sweep[-1]))
rec("V4c h -> 0 limit equals the exact-derivative value for the tree's k = (1,1,0,0)",
    abs(sweep[-1] - float(ratio_tree_exact)) / float(ratio_tree_exact) < 0.01,
    "FD(h=5e-5) %.4e  exact %.4e" % (sweep[-1], float(ratio_tree_exact)))
rec("V4d tree's k = (1,1,0,0) is NOT null in its metric: g(k,k) = -4 Phi", abs(float(gkk) + 4*float((-Mv/bv))) < 1e-12,
    "g(k,k) = %.6e" % float(gkk))
rec("V4e with an exactly null k and orthonormal screen: tr T = R_kk exactly (V1 at work)",
    abs(sp.N(T_null.trace() - Rkk_exact)) < 1e-15, "tr T = %.6e  R_kk = %.6e" % (sp.N(T_null.trace()), Rkk_exact))
rec("V4f on that correct screen |tr|/|max| = %.3e ~ 4|M|/(3b) = %.3e: traceless to ~1%%, NOT four digits"
    % (float(ratio_null), 4*abs(float(Mv))/(3*float(bv))), 5e-3 < float(ratio_null) < 1.2e-2, "")
rs = []
for mm in (sp.Rational(-1, 1000), sp.Rational(-2, 1000), sp.Rational(-4, 1000)):
    RLm = RLnum(mm, pt); Tm = Tmat(RLm, [1, 1, 0, 0], ee_tree, sign=-1)
    rs.append(float(abs(Tm.trace()) / max(abs(Tm[0, 0]), abs(Tm[1, 1]))))
rec("V4g tree-k exact ratio scales as M^2 (tr ~ M^3): the O(M^2) Ricci and the non-null-k term cancel",
    abs(rs[1]/rs[0] - 4) < 0.1 and abs(rs[2]/rs[1] - 4) < 0.1, "ratios %s" % ["%.4e" % v for v in rs])
# ANEC-type integral of the linearised metric's O(M^2) R_kk along the straight ray
c2f = sp.lambdify((x, y), c2g)
Nn = 400000; xa, xb = -2000.0, 2000.0; hh = (xb - xa)/Nn
Iint = sum(c2f(xa + (i + .5)*hh, 0.3) for i in range(Nn))*hh
Ian = -math.pi/(4*0.3**3)
rec("V4h int R_kk dx along the ray (O(M^2) coeff) = -pi/(4 b^3): linearised metric's fictitious "
    "ANEC integral is NEGATIVE, sign-blind", abs(Iint/Ian - 1) < 1e-3, "numeric %.6f  analytic %.6f" % (Iint, Ian))
print("       vs Weyl focal power 4|M|/b^2: |int R_kk/2| / (4|M|/b^2) = pi|M|/(32 b) = %.2e at |M|=2e-3, %.2e at 4e-2"
      % (math.pi*2e-3/(32*0.3), math.pi*4e-2/(32*0.3)))

# ------------------------------------------------------------------ V5 sign convention
Tp = C.tidal((0.0, 0.3, 0.0), [1.0, 1.0, 0.0, 0.0], [0., 0., 1., 0.], [0., 0., 0., 1.], 2.0e-3)
RLpp = RLnum(sp.Rational(2, 1000), pt)
T_mtw = Tmat(RLpp, [1, 1, 0, 0], ee_tree, sign=+1)
rec("V5a composite.tidal = -(MTW optical tidal matrix R_{a m b n} e^a k^m e^b k^n)",
    abs(Tp[0][0] + float(T_mtw[0, 0])) < 1e-4 and abs(Tp[1][1] + float(T_mtw[1, 1])) < 1e-4,
    "tree diag (%.4f, %.4f)  MTW diag (%.4f, %.4f)" % (Tp[0][0], Tp[1][1], float(T_mtw[0, 0]), float(T_mtw[1, 1])))
# convention-free: neighbouring geodesics with the tree's integrator, M>0
def endpoint(p0, Mm, lam=26.0, n=2600):
    k0 = C.null_tangent(p0, Mm)
    pts, tang, h = C.geodesic(p0, k0, Mm, lam, n)
    return pts
Mp = 2.0e-3; d = 1e-3; x0 = -1.0e-9
# start at closest approach with parallel rays (source at infinity analogue); watch separations
base = endpoint((0.0, 0.3, 0.0), Mp)
rad = endpoint((0.0, 0.3 + d, 0.0), Mp)
tan = endpoint((0.0, 0.3, d), Mp)
def sep(a, b, i): return math.sqrt(sum((a[i][j] - b[i][j])**2 for j in (1, 2, 3)))
i_end = len(base) - 1
s_rad = [sep(base, rad, i) for i in (0, i_end)]
s_tan = [sep(base, tan, i) for i in (0, i_end)]
rec("V5b physics, M>0: TANGENTIAL (z) neighbours converge, RADIAL (y) diverge (tree's geodesics)",
    s_tan[1] < s_tan[0] and s_rad[1] > s_rad[0],
    "radial %.4e->%.4e  tangential %.4e->%.4e" % (s_rad[0], s_rad[1], s_tan[0], s_tan[1]))
print("       MTW T for M>0 focuses z (T_zz = %+.4f > 0): consistent with V5b." % float(T_mtw[1, 1]))
print("       composite.tidal gives T_yy = %+.4f > 0 for M>0, i.e. evolves A'' = -T A focusing the"
      " RADIAL direction -- opposite to V5b.  Trace unaffected (V1); conjugate-point EXISTENCE for"
      " either sign unaffected at linear order (traceless T and -T both have one focusing"
      " eigendirection).  Recorded, not repaired." % Tp[0][0])

# conjugate lambda under both sign conventions vs the geodesic-bundle truth
def rep(Mm, sgn, b=0.3, x0=-40.0, lam=75.0, n=900):
    p0 = (x0, b, 0.0); k0 = C.null_tangent(p0, Mm); pts, tang, h = C.geodesic(p0, k0, Mm, lam, n)
    e1, e2 = [0., 0., 1., 0.], [0., 0., 0., 1.]; A = [[0, 0], [0, 0]]; dA = [[1., 0], [0, 1.]]; conj = None; which = None
    for i in range(len(pts) - 1):
        xx_ = pts[i]; kk = list(tang[i]); pp = (xx_[1], xx_[2], xx_[3])
        T = [[sgn*v for v in row] for row in C.tidal(pp, kk, e1, e2, Mm)]
        acc = [[-sum(T[r_][q]*A[q][cc] for q in range(2)) for cc in range(2)] for r_ in range(2)]
        for r_ in range(2):
            for cc in range(2):
                A[r_][cc] += h*dA[r_][cc] + 0.5*h*h*acc[r_][cc]; dA[r_][cc] += h*acc[r_][cc]
        if i > 5 and conj is None and A[0][0]*A[1][1] - A[0][1]*A[1][0] <= 0:
            conj = i*h; which = 'radial' if A[0][0] <= 0 else 'tangential'
        G = C.christoffel(pp, Mm)
        for ev in (e1, e2):
            de = [-sum(G[a_][al][be]*kk[al]*ev[be] for al in range(4) for be in range(4)) for a_ in range(4)]
            for a_ in range(4): ev[a_] += h*de[a_]
    return conj, which
def cross(Mm, comp, d=1e-5, lam=75.0, n=3000):
    p0 = (-40.0, 0.3, 0.0)
    P, _, h = C.geodesic(p0, C.null_tangent(p0, Mm, (1.0, 0.0, 0.0)), Mm, lam, n)
    Q, _, _ = C.geodesic(p0, C.null_tangent(p0, Mm, (1.0, d, 0.0) if comp == 'y' else (1.0, 0.0, d)), Mm, lam, n)
    j = 2 if comp == 'y' else 3; prev = None
    for i in range(10, len(P)):
        sv = Q[i][j] - P[i][j]
        if prev is not None and prev > 0 and sv <= 0: return i*h
        prev = sv
    return None
for Mm in (2e-3, -2e-3):
    tr_, mt_ = rep(Mm, 1), rep(Mm, -1)
    truth = ('radial', cross(Mm, 'y')) if cross(Mm, 'y') else ('tangential', cross(Mm, 'z'))
    rec("V5c M=%+g: conjugate lambda identical under tree sign and MTW sign; truth direction %s" % (Mm, truth[0]),
        tr_[0] == mt_[0] and abs(tr_[0] - truth[1]) < 0.5 and mt_[1] == truth[0] and tr_[1] != truth[0],
        "tree %s  MTW %s  bundle %.3f" % (tr_, mt_, truth[1]))

# ------------------------------------------------------------------ V6 along-ray leak
lk = {}
for Mm, n in ((2e-3, 450), (2e-3, 900), (2e-3, 1800), (1e-3, 900), (4e-3, 900)):
    lk[(Mm, n)] = C.survey(Mm, n=n)["traceless_ratio"]
rec("V6a along-ray leak < 2e-2 at M = 2e-3 (composite.py:331 check)", lk[(2e-3, 900)] < 2e-2, "leak = %.3e" % lk[(2e-3, 900)])
rec("V6b DISCREPANCY: leak is step-independent (n 450->1800), so NOT first-order Euler transport (composite.py:328-330)",
    abs(lk[(2e-3, 450)]/lk[(2e-3, 1800)] - 1) < 0.03, "n=450 %.4e, 900 %.4e, 1800 %.4e" % (lk[(2e-3, 450)], lk[(2e-3, 900)], lk[(2e-3, 1800)]))
rec("V6c leak scales linearly in |M| and matches the null-screen O(M^2) Ricci ratio (V4f) to 10%",
    abs(lk[(4e-3, 900)]/lk[(2e-3, 900)] - 2) < 0.1 and abs(lk[(2e-3, 900)]/lk[(1e-3, 900)] - 2) < 0.1
    and abs(lk[(2e-3, 1800)]/float(ratio_null) - 1) < 0.1,
    "M=1e-3 %.3e, 2e-3 %.3e, 4e-3 %.3e ; V4f %.3e" % (lk[(1e-3, 900)], lk[(2e-3, 900)], lk[(4e-3, 900)], float(ratio_null)))
print("       extrapolated to the window rows (composite.py:62-68): 4|M|/(3b) = %s"
      % ", ".join("|M|=%g: %.1f%%" % (mm, 100*4*mm/0.9) for mm in (2e-3, 5e-3, 1e-2, 2e-2, 4e-2)))

npass = sum(1 for _, ok, _ in results if ok)
print("\n%d/%d checks PASS" % (npass, len(results)))
sys.exit(0 if npass == len(results) else 1)
