#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation of the Lyapunov inequality as seatindex.py uses it.

Statement checked (modern L^1 form):
  u'' + q(t) u = 0 on [a,b], q real (sign-indefinite), q in L^1, u non-trivial,
  u(a) = u(b) = 0   ==>   (b - a) * INT_a^b q+(t) dt > 4 ,   constant 4 sharp.

Sections
  [1] sympy: the two algebraic steps of the classical proof
        1/(c-a) + 1/(b-c) >= 4/(b-a)                (equality iff c = midpoint)
        |eta(c)|^2 <= (c-a)(b-c)/(b-a) INT |eta'|^2  (Cauchy-Schwarz, vector eta)
  [2] sharpness: centred slab q = m on |t - 1/2| < eps in [0,1]; the product
      (b-a) INT q -> 4 from above as eps -> 0 (sympy series + numeric root).
  [3] random sign-indefinite, DISCONTINUOUS piecewise-constant q (the tree's
      slabs are discontinuous; Lyapunov 1892 assumed continuous q): RK4 from
      u(0)=0, u'(0)=1; at the first zero b check b INT_0^b q+ > 4.
  [4] the tree's own cells (seatindex.py, imported READ-ONLY, no bytecode
      written): the 12 Lyapunov-excluded cells, their numbers, and whether any
      seats by the tree's integrator AND by an independent RK4.  Also the
      tree's use of L (total length) in place of (b - a): valid, conservative.
  [5] matrix extension: 2x2 symmetric tidal matrices T(t) incl. traceless
      (Weyl-only, scalar q = tr T / 2 = 0).  Conjugate point det A = 0 at t*
      ==> t* INT_0^t* lambda_max(T)+ >= 4  (vector variational proof), while the
      scalar Lyapunov number from tr T can be 0.
  [6] composite.py's vacuum Weyl seat (imported READ-ONLY): scalar Lyapunov
      number (from tr T) vs matrix Lyapunov number (from lambda_max(T)+).
Exit 0 iff every check agrees.
"""
import sys, math, random, importlib
sys.dont_write_bytecode = True
import sympy as sp

WD = "/home/user/Claude-Method-Works/research/warp-drive"
OK = True


def chk(label, cond, detail=""):
    global OK
    OK &= bool(cond)
    print("  %-66s %s %s" % (label, "ok" if cond else "FAIL", detail))


# ---------------------------------------------------------------- [1]
print("[1] sympy: the algebra of the classical proof")
a, b, c = sp.symbols("a b c", real=True)
expr = sp.together(1 / (c - a) + 1 / (b - c) - 4 / (b - a))
num, den = sp.fraction(sp.factor(expr))
chk("1/(c-a)+1/(b-c)-4/(b-a) = (a+b-2c)^2/((c-a)(b-c)(b-a))",
    sp.simplify(expr - (a + b - 2 * c) ** 2 / ((c - a) * (b - c) * (b - a))) == 0,
    str(sp.factor(expr)))
# Cauchy-Schwarz step: |eta(c)| <= sqrt(c-a) ||eta'||_[a,c], same on [c,b];
# minimise  X + Y  s.t. X^2/(c-a) + ... : sup|eta(c)|^2 / INT|eta'|^2 = (c-a)(b-c)/(b-a)
x, y = sp.symbols("x y", positive=True)   # INT_a^c |eta'|^2 = x, INT_c^b = y
p, qq = sp.symbols("p q", positive=True)  # p = c-a, qq = b-c
# eta(c)^2 <= min(p x, qq y); maximise over x+y = 1 -> p x = qq y
xs = sp.solve(sp.Eq(p * x, qq * (1 - x)), x)[0]
bound = sp.simplify(p * xs)
chk("sup eta(c)^2 / INT|eta'|^2 = (c-a)(b-c)/(b-a)", sp.simplify(bound - p * qq / (p + qq)) == 0, str(bound))
chk("max over c of (c-a)(b-c)/(b-a) = (b-a)/4 at the midpoint",
    sp.simplify((p * qq / (p + qq)).subs(qq, p) - (2 * p) / 4) == 0)

# ---------------------------------------------------------------- [2]
print("[2] sharpness of the constant 4: centred slab on [0,1]")
eps, s = sp.symbols("epsilon s", positive=True)   # s = sqrt(m)
# u = t on [0, 1/2-eps]; symmetric zero at 1 iff u'(1/2) = 0:
#   cos(s eps) - (1/2 - eps) s sin(s eps) = 0
F = sp.cos(s * eps) - (sp.Rational(1, 2) - eps) * s * sp.sin(s * eps)
prods = []
for e in (0.25, 0.1, 0.03, 0.01, 0.001, 1e-5):
    Fe = sp.lambdify(s, F.subs(eps, e))
    lo, hi = 1e-9, math.pi / (2 * e) * 0.999999
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if Fe(lo) * Fe(mid) <= 0:
            hi = mid
        else:
            lo = mid
    sv = 0.5 * (lo + hi)
    prod = 1.0 * (2 * e) * sv * sv          # (b-a) INT q = 1 * m * 2 eps
    prods.append(prod)
    print("     eps = %-8g  m = %-14.6g (b-a) INT q = %.8f" % (e, sv * sv, prod))
chk("every product > 4 (strict)", all(pv > 4 for pv in prods))
chk("products decrease monotonically toward 4", all(prods[i] > prods[i + 1] for i in range(len(prods) - 1)))
chk("limit eps->0 is 4 to 1e-4", abs(prods[-1] - 4) < 1e-4, "%.8f" % prods[-1])
chk("constant q on [0,1] (q = pi^2): product pi^2 = 9.8696 > 4", math.pi ** 2 > 4)

# ---------------------------------------------------------------- [3]
print("[3] random sign-indefinite discontinuous q, RK4, first zero b")


def rk4_first_zero(qf, L, n):
    h = L / n
    u, v = 0.0, 1.0
    I = 0.0
    t = 0.0
    for i in range(n):
        def f(tt, uu, vv):
            return vv, -qf(tt) * uu
        k1 = f(t, u, v)
        k2 = f(t + h / 2, u + h / 2 * k1[0], v + h / 2 * k1[1])
        k3 = f(t + h / 2, u + h / 2 * k2[0], v + h / 2 * k2[1])
        k4 = f(t + h, u + h * k3[0], v + h * k3[1])
        un = u + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        vn = v + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        I += h * max(qf(t + h / 2), 0.0)
        if i > 2 and un <= 0.0:
            bz = t + h * u / (u - un)
            return bz, I
        u, v, t = un, vn, t + h
    return None, I


random.seed(67)
n_seat, worst, viol = 0, 1e9, 0
for trial in range(600):
    L = random.uniform(1.0, 12.0)
    k = random.randint(1, 8)
    cuts = sorted(random.uniform(0, L) for _ in range(k - 1))
    edges = [0.0] + cuts + [L]
    vals = [random.uniform(-20, 40) * random.choice([0.02, 0.2, 1, 5]) for _ in range(k)]

    def qf(t, edges=edges, vals=vals):
        for j in range(len(vals)):
            if t <= edges[j + 1]:
                return vals[j]
        return vals[-1]
    bz, I = rk4_first_zero(qf, L, 6000)
    if bz is not None:
        n_seat += 1
        prod = bz * I
        worst = min(worst, prod)
        if prod <= 4:
            viol += 1
print("     %d of 600 random profiles seat; min b*INT_0^b q+ = %.4f" % (n_seat, worst))
chk("no seating profile violates (b-a) INT q+ > 4", viol == 0 and n_seat > 50, "violations=%d" % viol)

# ---------------------------------------------------------------- [4]
print("[4] the tree's cells (seatindex.py imported read-only)")
sys.path.insert(0, WD)
si = importlib.import_module("seatindex")
excl = [(m, l) for m in si.MS for l in si.LS if si.lyapunov_excluded(m, l, si.TOTAL)]
cells = [(m, l, cc) for (m, l) in excl for cc in si.CPOS if cc + l <= si.TOTAL]
print("     excluded (m,l):", excl, " -> %d cells" % len(cells))
print("     Lyapunov numbers L m l / 4:", [round(si.lyapunov_number(m, l, si.TOTAL), 4) for (m, l) in excl])
chk("12 exterior cells, as CLAIMS.md states", len(cells) == 12)
tree_seat = [cl for cl in cells if si.seats(si.slab(cl[0], cl[2], cl[1]), si.TOTAL) is not None]
my_seat = [cl for cl in cells if rk4_first_zero(si.slab(cl[0], cl[2], cl[1]), si.TOTAL, 12000)[0] is not None]
chk("none seats by the tree's integrator", tree_seat == [])
chk("none seats by an independent RK4 (12000 steps)", my_seat == [])
# Also with hostile outside (q<0 elsewhere): q+ unchanged, so still excluded
my_h = [cl for cl in cells for hh in (-5.0, -20.0)
        if rk4_first_zero(si.slab(cl[0], cl[2], cl[1], outside=hh), si.TOTAL, 12000)[0] is not None]
chk("none seats with outside q = -5 or -20 either (q+ unchanged)", my_h == [])
# boundary: exclusion is L m l <= 4; strict '>' in the theorem makes '<=' correct
chk("exclusion test uses <= (theorem is strict >), so equality is excluded correctly",
    si.lyapunov_excluded(4.0 / si.TOTAL, 1.0, si.TOTAL) is True)
# the tree uses L, not b-a: for a zero at b <= L, L INT_0^L q+ >= b INT_0^b q+ > 4
m_, l_, c_ = 16.0, 0.5, 1.5
bz, I = rk4_first_zero(si.slab(m_, c_, l_), si.TOTAL, 12000)
print("     illustration m=16,l=0.5,c=1.5: first zero b=%.4f, b INT_0^b q+ = %.4f, L m l = %.1f" % (bz, bz * I, si.TOTAL * m_ * l_))
chk("tree's L-form is weaker than b-form (conservative, never over-excludes)", si.TOTAL * m_ * l_ >= bz * I > 4)
# the theorem's 4 is attained only in the limit: cells just above exclusion can seat
mm = 4.0 / si.TOTAL / 0.1 * 1.02   # l = 0.1 slab at midpoint-ish with L m l = 4.08
bz2, _ = rk4_first_zero(si.slab(mm, 5.95, 0.1), si.TOTAL, 24000)
print("     thin central slab with L m l = 4.08 (Lyapunov number 1.02): first zero %s" % (None if bz2 is None else round(bz2, 4)))
chk("a cell with Lyapunov number 1.02 DOES seat -> bound nearly sharp on the tree's own axes", bz2 is not None)

# ---------------------------------------------------------------- [5]
print("[5] matrix (Jacobi) extension: Weyl-only tidal matrices")


def jacobi_conj(Tf, L, n):
    """A'' = -T A, A(0)=0, A'(0)=I; RK4; first det A = 0; accumulate INT lambda_max(T)+ and INT tr(T)/2 +."""
    h = L / n
    A = [[0.0, 0.0], [0.0, 0.0]]
    D = [[1.0, 0.0], [0.0, 1.0]]
    t, Imax, Itr = 0.0, 0.0, 0.0

    def mul(T, X):
        return [[-(T[r][0] * X[0][cc] + T[r][1] * X[1][cc]) for cc in range(2)] for r in range(2)]

    def add(X, Y, s):
        return [[X[r][cc] + s * Y[r][cc] for cc in range(2)] for r in range(2)]
    det_prev = None
    for i in range(n):
        T0, Th, T1 = Tf(t), Tf(t + h / 2), Tf(t + h)
        k1a, k1d = D, mul(T0, A)
        k2a, k2d = add(D, k1d, h / 2), mul(Th, add(A, k1a, h / 2))
        k3a, k3d = add(D, k2d, h / 2), mul(Th, add(A, k2a, h / 2))
        k4a, k4d = add(D, k3d, h), mul(T1, add(A, k3a, h))
        An = [[A[r][cc] + h / 6 * (k1a[r][cc] + 2 * k2a[r][cc] + 2 * k3a[r][cc] + k4a[r][cc]) for cc in range(2)] for r in range(2)]
        Dn = [[D[r][cc] + h / 6 * (k1d[r][cc] + 2 * k2d[r][cc] + 2 * k3d[r][cc] + k4d[r][cc]) for cc in range(2)] for r in range(2)]
        tr, dd = Th[0][0] + Th[1][1], Th[0][0] * Th[1][1] - Th[0][1] * Th[1][0]
        lmax = tr / 2 + math.sqrt(max(tr * tr / 4 - dd, 0.0))
        Imax += h * max(lmax, 0.0)
        Itr += h * max(tr / 2, 0.0)
        det = An[0][0] * An[1][1] - An[0][1] * An[1][0]
        if i > 3 and det <= 0.0:
            return t + h, Imax, Itr
        A, D, t = An, Dn, t + h
    return None, Imax, Itr


random.seed(670)
n5, worst5, viol5, weyl_seats = 0, 1e9, 0, 0
for trial in range(300):
    L = random.uniform(2.0, 12.0)
    k = random.randint(1, 5)
    edges = [0.0] + sorted(random.uniform(0, L) for _ in range(k - 1)) + [L]
    traceless = trial % 2 == 0
    blocks = []
    for _ in range(k):
        w1, w2 = random.uniform(-3, 3), random.uniform(-3, 3)
        r = 0.0 if traceless else random.uniform(-2, 2)
        blocks.append([[r + w1, w2], [w2, r - w1]])

    def Tf(t, edges=edges, blocks=blocks):
        for j in range(len(blocks)):
            if t <= edges[j + 1]:
                return blocks[j]
        return blocks[-1]
    ts, Imax, Itr = jacobi_conj(Tf, L, 4000)
    if ts is not None:
        n5 += 1
        worst5 = min(worst5, ts * Imax)
        if ts * Imax < 4:
            viol5 += 1
        if traceless:
            weyl_seats += 1
print("     %d of 300 seat (det A = 0); %d of them traceless (scalar q = 0 identically)" % (n5, weyl_seats))
print("     min t* INT lambda_max(T)+ = %.4f" % worst5)
chk("traceless (Weyl-only) seats exist: scalar Lyapunov (q = tr T/2 = 0) cannot exclude them", weyl_seats > 0)
chk("matrix form t* INT lambda_max(T)+ >= 4 holds in every seat", viol5 == 0, "violations=%d" % viol5)

# ---------------------------------------------------------------- [6]
print("[6] composite.py's vacuum Weyl seat (read-only import; ~1-2 min)")
co = importlib.import_module("composite")


def composite_lyap(M, b=co.B_DEFAULT, x0=co.X0_DEFAULT, lam=co.LAM_DEFAULT, n=co.NSTEP):
    p0 = (x0, b, 0.0)
    k0 = co.null_tangent(p0, M)
    pts, tang, h = co.geodesic(p0, k0, M, lam, n)
    e1, e2 = [0., 0., 1., 0.], [0., 0., 0., 1.]
    A = [[0.0, 0.0], [0.0, 0.0]]
    dA = [[1.0, 0.0], [0.0, 1.0]]
    conj, Imax, Itr = None, 0.0, 0.0
    for i in range(len(pts) - 1):
        x = pts[i]
        k = list(tang[i])
        p = (x[1], x[2], x[3])
        T = co.tidal(p, k, e1, e2, M)
        Ts = [[T[0][0], 0.5 * (T[0][1] + T[1][0])], [0.5 * (T[0][1] + T[1][0]), T[1][1]]]
        tr = Ts[0][0] + Ts[1][1]
        dd = Ts[0][0] * Ts[1][1] - Ts[0][1] ** 2
        lmax = tr / 2 + math.sqrt(max(tr * tr / 4 - dd, 0.0))
        if conj is None:
            Imax += h * max(lmax, 0.0)
            Itr += h * max(tr / 2, 0.0)
        acc = [[-sum(T[r][s] * A[s][cc] for s in range(2)) for cc in range(2)] for r in range(2)]
        for r in range(2):
            for cc in range(2):
                A[r][cc] += h * dA[r][cc] + 0.5 * h * h * acc[r][cc]
                dA[r][cc] += h * acc[r][cc]
        if i > 5 and conj is None and (A[0][0] * A[1][1] - A[0][1] * A[1][0]) <= 0.0:
            conj = i * h
            break
        G = co.christoffel(p, M)
        for e in (e1, e2):
            de = [-sum(G[a_][al][be] * k[al] * e[be] for al in range(4) for be in range(4)) for a_ in range(4)]
            for a_ in range(4):
                e[a_] += h * de[a_]
    return conj, Imax, Itr


for M in (2.0e-3, -2.0e-3):
    conj, Imax, Itr = composite_lyap(M)
    print("     M = %+g: conjugate at %s;  scalar number t* INT (trT/2)+ = %.3e;  matrix number t* INT lambda_max+ = %.4f"
          % (M, None if conj is None else round(conj, 3), (conj or 0) * Itr, (conj or 0) * Imax))
    chk("M=%+g seats (composite reproduces its own seat)" % M, conj is not None)
    if conj is not None:
        chk("M=%+g scalar Lyapunov number << 4 (Ricci-only form would exclude)" % M, conj * Itr < 0.5)
        chk("M=%+g matrix Lyapunov number >= 4 (matrix form does NOT exclude)" % M, conj * Imax >= 4.0)

print("\nALL CHECKS AGREE" if OK else "\nSOME CHECK FAILED")
sys.exit(0 if OK else 1)
