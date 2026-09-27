#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for 'harmonic-function-maximum-principle'.

The tree's use (research/warp-drive/stability.py:115-118, and chain.py:140-143
which stability.py cites):
  "the potential of any point sources is harmonic away from them whatever their
   signs -- the Hessian of 1/r is traceless -- so a harmonic function has no
   strict minimum"

What is checked here, each as a numbered block that prints PASS/FAIL:
  S1  trace of Hess(1/r) = 0 in R^3, exactly (sympy); in R^n it is (3-n)/r^3,
      so 'three dimensions' is a hypothesis the tree carries implicitly.
  S2  exact spherical mean of 1/|x-z| over a sphere of radius rho about x0,
      d=|x0-z|:  = 1/d if d>rho (mean-value property),  = 1/rho if d<rho
      (the shell theorem -- the constant-potential exception).
  S3  the proof, for EXACTLY the tree's class (finite sums of m_i/|x-z_i|, any
      signs): S2 termwise gives mean = centre value on every sphere whose closed
      ball is source-free; a strict local min (or max) would make the mean
      strictly larger (smaller) than the centre value -> contradiction.  The
      logic step is recorded; the mean-value identity is checked numerically on
      random mixed-sign configurations to 1e-10.
  S4  z3: a real symmetric 3x3 matrix with trace 0 is never positive definite,
      and a PSD one with trace 0 is the zero matrix (so at a critical point of a
      harmonic function the Hessian is indefinite or identically zero).
  S5  'degenerate Hessian at a point' is NOT 'constant potential':
      u = x^3 - 3 x y^2 is harmonic, has grad = 0 and Hess = 0 at the origin, is
      not constant and is not a minimum.  (chain.py:336's wording 'Hessian
      identically zero' is the correct form; stability.py:118-119 'the
      DEGENERATE case, constant potential' is looser wording.)
  S6  numeric: equilibria of random mixed-sign point-source potentials found by
      Newton's method; every Hessian there is indefinite with trace ~ 0.
  S7  stress of the NAMED hypothesis 'superposition of 1/r terms': a Yukawa
      kernel e^{-r/L}/r has Laplacian e^{-r/L}/(L^2 r) != 0; the Yukawa shell's
      interior potential is proportional to sinh(r/L)/r, which has a STRICT
      extremum at the centre (min or max according to the sign of alpha*M).
      Harmonicity, and the 'any signs' conclusion, need the exact 1/r kernel.
  S8  continuous extension used by the tree (the uniform shell of the device):
      a uniform shell = integral of point terms, each outside a small interior
      sphere, so S2 applies termwise; checked by exact integral.

Stdlib + sympy + z3 (+ numpy absent is fine; pure python numerics).
Exit 0 iff every block passes.
"""
import math, random, sys
import sympy as sp

FAIL = []


def chk(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("  -- " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)


# ------------------------------------------------------------------ S1
x, y, z = sp.symbols("x y z", real=True)
r = sp.sqrt(x**2 + y**2 + z**2)
H = sp.hessian(1 / r, (x, y, z))
tr = sp.simplify(H.trace())
chk("S1a trace Hess(1/r) == 0 in R^3", tr == 0, "trace = %s" % tr)
# each diagonal entry is (3 x_i^2 - r^2)/r^5, as chain.py:140 states
ok = all(sp.simplify(H[i, i] - (3 * v**2 - r**2) / r**5) == 0
         for i, v in enumerate((x, y, z)))
chk("S1b diagonal entries equal (3 r_i^2 - r^2)/r^5 (chain.py:140)", ok)
# general n: Laplacian of 1/rho in R^n, rho radial: f'' + (n-1)/rho f'
n, rho = sp.symbols("n rho", positive=True)
f = 1 / rho
lap_n = sp.simplify(sp.diff(f, rho, 2) + (n - 1) / rho * sp.diff(f, rho))
chk("S1c Laplacian of 1/r in R^n = (3-n)/r^3 (zero only at n=3)",
    sp.simplify(lap_n - (3 - n) / rho**3) == 0, "lap = %s" % lap_n)
g = rho**(2 - n)
chk("S1d the harmonic kernel in R^n is r^(2-n)",
    sp.simplify(sp.diff(g, rho, 2) + (n - 1) / rho * sp.diff(g, rho)) == 0)

# ------------------------------------------------------------------ S2
R_, d_ = sp.symbols("rho_s d", positive=True)
u = sp.symbols("u", real=True)
integrand = 1 / sp.sqrt(R_**2 + d_**2 - 2 * R_ * d_ * u)
F = sp.integrate(integrand, (u, -1, 1)) / 2           # mean over the sphere
F = sp.simplify(F)
closed = (sp.Abs(R_ + d_) - sp.Abs(R_ - d_)) / (2 * R_ * d_)
# evaluate exactly on both sides of d = rho
outside = sp.simplify(F.subs({R_: sp.Rational(1), d_: sp.Rational(3)}))
inside = sp.simplify(F.subs({R_: sp.Rational(3), d_: sp.Rational(1)}))
chk("S2a mean of 1/|x-z| over sphere, source outside (rho=1,d=3) = 1/d",
    sp.nsimplify(outside) == sp.Rational(1, 3), "got %s" % outside)
chk("S2b mean of 1/|x-z| over sphere, source inside (rho=3,d=1) = 1/rho",
    sp.nsimplify(inside) == sp.Rational(1, 3), "got %s" % inside)
# symbolic: case d > rho
dd = sp.symbols("dd", positive=True)                  # d = rho + dd
def _desq(e):
    """sqrt(P) with P a perfect square of a positive expression -> that expression."""
    return e.replace(lambda w: isinstance(w, sp.Pow) and w.exp == sp.Rational(1, 2),
                     lambda w: sp.sqrt(sp.factor(w.base)))


Fo = sp.simplify(_desq(sp.integrate(integrand.subs(d_, R_ + dd), (u, -1, 1)) / 2))
chk("S2c symbolic: for d = rho + delta > rho, mean = 1/d exactly",
    sp.simplify(Fo - 1 / (R_ + dd)) == 0, "mean = %s" % Fo)
Fi = sp.simplify(_desq(sp.integrate(integrand.subs(R_, d_ + dd), (u, -1, 1)) / 2))
chk("S2d symbolic: for rho = d + delta > d, mean = 1/rho exactly (shell theorem)",
    sp.simplify(Fi - 1 / (d_ + dd)) == 0, "mean = %s" % Fi)


# ------------------------------------------------------------------ S3
def phi(p, src):
    return sum(m / math.dist(p, q) for m, q in src)


def sphere_mean(p, rad, src, N=40):
    """Gauss-Legendre in cos(theta) x uniform in azimuth (exact for the
    trigonometric polynomial in azimuth to high order)."""
    # Gauss-Legendre nodes by Newton iteration (stdlib only)
    nodes, weights = [], []
    for i in range(1, N + 1):
        t = math.cos(math.pi * (i - 0.25) / (N + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, t
            for k in range(2, N + 1):
                p0, p1 = p1, ((2 * k - 1) * t * p1 - (k - 1) * p0) / k
            dp = N * (t * p1 - p0) / (t * t - 1)
            dt = p1 / dp
            t -= dt
            if abs(dt) < 1e-16:
                break
        nodes.append(t)
        weights.append(2 / ((1 - t * t) * dp * dp))
    M = 2 * N
    s = 0.0
    for t, w in zip(nodes, weights):
        st = math.sqrt(1 - t * t)
        for j in range(M):
            a = 2 * math.pi * j / M
            q = (p[0] + rad * st * math.cos(a), p[1] + rad * st * math.sin(a),
                 p[2] + rad * t)
            s += w * phi(q, src)
    return s / (2 * M)


random.seed(67)
worst = 0.0
for trial in range(40):
    src = [(random.choice([-1, 1]) * random.uniform(0.2, 3.0),
            tuple(random.uniform(-3, 3) for _ in range(3))) for _ in range(6)]
    p = tuple(random.uniform(-3, 3) for _ in range(3))
    dmin = min(math.dist(p, q) for _, q in src)
    rad = 0.5 * dmin                       # closed ball source-free
    mv = sphere_mean(p, rad, src)
    c = phi(p, src)
    scale = sum(abs(m) / math.dist(p, q) for m, q in src)
    worst = max(worst, abs(mv - c) / scale)
chk("S3a mean-value identity on 40 random mixed-sign 6-source configs",
    worst < 1e-10, "worst relative deviation %.2e" % worst)
print("      S3b (logic) strict local min at x0 => for small rho, u > u(x0) on the"
      " sphere => mean > u(x0); S3a/S2 give mean = u(x0): contradiction."
      "  Same for strict max.  Holds for every sign pattern since S2 is"
      " linear in m.")

# ------------------------------------------------------------------ S4
import z3
a = [[z3.Real("a%d%d" % (min(i, j), max(i, j))) for j in range(3)] for i in range(3)]
tr0 = a[0][0] + a[1][1] + a[2][2] == 0
m1 = a[0][0]
m2 = a[0][0] * a[1][1] - a[0][1] * a[0][1]
m3 = (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[1][2])
      - a[0][1] * (a[0][1] * a[2][2] - a[1][2] * a[0][2])
      + a[0][2] * (a[0][1] * a[1][2] - a[1][1] * a[0][2]))
s = z3.Solver()
s.add(tr0, m1 > 0, m2 > 0, m3 > 0)          # Sylvester: positive definite
r4a = s.check()
chk("S4a z3: trace-0 symmetric 3x3 & positive definite is UNSAT", r4a == z3.unsat,
    str(r4a))
# PSD (all principal minors >= 0) & trace 0 => zero matrix
s = z3.Solver()
pm1 = [a[i][i] >= 0 for i in range(3)]
pm2 = [a[i][i] * a[j][j] - a[i][j] * a[i][j] >= 0 for i in range(3) for j in range(i + 1, 3)]
s.add(tr0, *pm1, *pm2, m3 >= 0)
s.add(z3.Or(*[a[i][j] != 0 for i in range(3) for j in range(i, 3)]))
r4b = s.check()
chk("S4b z3: trace-0 PSD symmetric 3x3 that is nonzero is UNSAT", r4b == z3.unsat,
    str(r4b))
# vacuity guard: the constraints without trace-0 are satisfiable
s = z3.Solver(); s.add(m1 > 0, m2 > 0, m3 > 0)
chk("S4c vacuity guard: positive definite alone is SAT", s.check() == z3.sat)

# ------------------------------------------------------------------ S5
uu = x**3 - 3 * x * y**2
lap = sp.simplify(sp.diff(uu, x, 2) + sp.diff(uu, y, 2) + sp.diff(uu, z, 2))
g0 = [sp.diff(uu, v).subs({x: 0, y: 0, z: 0}) for v in (x, y, z)]
H0 = sp.hessian(uu, (x, y, z)).subs({x: 0, y: 0, z: 0})
neg = uu.subs({x: -sp.Rational(1, 10**6), y: 0, z: 0})
chk("S5 x^3-3xy^2: harmonic, grad=0, Hess=0 at 0, nonconstant, value<0 arbitrarily near 0",
    lap == 0 and all(v == 0 for v in g0) and H0 == sp.zeros(3, 3) and neg < 0,
    "degenerate-Hessian critical point that is neither constant nor a minimum")


# ------------------------------------------------------------------ S6
def grad_hess(p, src):
    gr = [0.0] * 3
    Hm = [[0.0] * 3 for _ in range(3)]
    for m, q in src:
        dv = [p[i] - q[i] for i in range(3)]
        r2 = sum(t * t for t in dv)
        r1 = math.sqrt(r2)
        for i in range(3):
            gr[i] += -m * dv[i] / r1**3
            for j in range(3):
                Hm[i][j] += m * (3 * dv[i] * dv[j] - (r2 if i == j else 0)) / r1**5
    return gr, Hm


def solve3(A, b):
    import copy
    M = [row[:] + [bb] for row, bb in zip(copy.deepcopy(A), b)]
    for c in range(3):
        piv = max(range(c, 3), key=lambda k: abs(M[k][c]))
        M[c], M[piv] = M[piv], M[c]
        if abs(M[c][c]) < 1e-300:
            return None
        for k in range(3):
            if k != c:
                fct = M[k][c] / M[c][c]
                M[k] = [M[k][t] - fct * M[c][t] for t in range(4)]
    return [M[i][3] / M[i][i] for i in range(3)]


def eig3(A):
    """eigenvalues of symmetric 3x3 by the trigonometric method."""
    p1 = A[0][1]**2 + A[0][2]**2 + A[1][2]**2
    q = (A[0][0] + A[1][1] + A[2][2]) / 3
    p2 = sum((A[i][i] - q)**2 for i in range(3)) + 2 * p1
    p = math.sqrt(p2 / 6)
    if p == 0:
        return [q, q, q]
    B = [[(A[i][j] - (q if i == j else 0)) / p for j in range(3)] for i in range(3)]
    detB = (B[0][0] * (B[1][1] * B[2][2] - B[1][2] * B[2][1])
            - B[0][1] * (B[1][0] * B[2][2] - B[1][2] * B[2][0])
            + B[0][2] * (B[1][0] * B[2][1] - B[1][1] * B[2][0]))
    rr = max(-1.0, min(1.0, detB / 2))
    ph = math.acos(rr) / 3
    e1 = q + 2 * p * math.cos(ph)
    e3 = q + 2 * p * math.cos(ph + 2 * math.pi / 3)
    return sorted([e1, 3 * q - e1 - e3, e3])


random.seed(1842)
found = indefinite = 0
worst_tr = 0.0
for trial in range(300):
    src = [(random.choice([-1, 1]) * random.uniform(0.2, 3.0),
            tuple(random.uniform(-2, 2) for _ in range(3))) for _ in range(random.randint(2, 7))]
    p = [random.uniform(-2, 2) for _ in range(3)]
    for it in range(80):
        gr, Hm = grad_hess(p, src)
        st = solve3(Hm, [-t for t in gr])
        if st is None:
            break
        p = [p[i] + st[i] for i in range(3)]
        if max(abs(t) for t in p) > 50:
            break
    gr, Hm = grad_hess(p, src)
    if max(abs(t) for t in p) > 50 or min(math.dist(p, q) for _, q in src) < 1e-3:
        continue
    scale = max(abs(m) / math.dist(p, q)**3 for m, q in src)
    if math.sqrt(sum(t * t for t in gr)) / (scale * 1.0) > 1e-9:
        continue
    found += 1
    ev = eig3(Hm)
    worst_tr = max(worst_tr, abs(sum(ev)) / scale)
    if ev[0] < 0 < ev[2]:
        indefinite += 1
chk("S6 equilibria of random mixed-sign potentials: all Hessians indefinite",
    found > 20 and indefinite == found,
    "%d equilibria found, %d indefinite, worst |trace|/scale %.1e" % (found, indefinite, worst_tr))

# ------------------------------------------------------------------ S7
L = sp.symbols("L", positive=True)
rr_ = sp.symbols("r", positive=True)
yk = sp.exp(-rr_ / L) / rr_
lapy = sp.simplify(sp.diff(yk, rr_, 2) + 2 / rr_ * sp.diff(yk, rr_))
chk("S7a Laplacian of Yukawa kernel e^{-r/L}/r = e^{-r/L}/(L^2 r) != 0",
    sp.simplify(lapy - sp.exp(-rr_ / L) / (L**2 * rr_)) == 0, "lap = %s" % lapy)
# Yukawa shell (radius Rs, unit surface mass) potential at interior radius s:
# integral over the shell of e^{-D/L}/D, D^2 = Rs^2 + s^2 - 2 Rs s u
Rs, s_, D = sp.symbols("R_s s D", positive=True)
# change variables u -> D: dD = -Rs s du / D ;  integral_{-1}^{1} e^{-D/L}/D du
#   = (1/(Rs s)) * integral_{Rs-s}^{Rs+s} e^{-D/L} dD
shellY = sp.simplify(sp.integrate(sp.exp(-D / L), (D, Rs - s_, Rs + s_)) / (Rs * s_) / 2)
target = L * sp.exp(-Rs / L) * sp.sinh(s_ / L) / (Rs * s_)
chk("S7b Yukawa shell interior mean potential = L e^{-R/L} sinh(s/L)/(R s)",
    sp.simplify((shellY - target).rewrite(sp.exp)) == 0, "got %s" % shellY)
h = sp.sinh(s_ / L) / s_
ser = sp.series(h, s_, 0, 4).removeO()
chk("S7c sinh(s/L)/s = 1/L + s^2/(6 L^3) + ...: strict extremum at the centre",
    sp.simplify(ser - (1 / L + s_**2 / (6 * L**3))) == 0,
    "centre is a strict MIN of +h and a strict MAX of -h: sign(alpha*M) decides")
# Newtonian shell for contrast: L -> infinity of the 1/r part is constant (S2d)

# ------------------------------------------------------------------ S8
# uniform shell radius Rs, total mass 1; small sphere radius eps about interior
# point at distance c from centre.  Mean over the small sphere of the shell
# potential equals the shell potential at the point (= 1/Rs, constant): by S2d
# the shell potential inside is 1/Rs identically, so the mean-value identity
# holds trivially, and every interior point is a NON-strict extremum.
# computed: shell of radius Rs about the origin, field point at |p| = c < Rs;
# the shell potential is the spherical mean of 1/|x-p| over the shell sphere.
c_, gap = sp.symbols("c gap", positive=True)
shell_in = sp.simplify(_desq(sp.integrate(
    (1 / sp.sqrt(Rs**2 + c_**2 - 2 * Rs * c_ * u)).subs(Rs, c_ + gap), (u, -1, 1)) / 2))
dshell = sp.simplify(sp.diff(shell_in.subs(gap, Rs - c_), c_))
chk("S8 uniform shell interior potential = 1/R_s for every c < R_s; d/dc = 0 "
    "(Hessian identically 0: the constant-potential exception, neutral not stable)",
    sp.simplify(shell_in.subs(gap, Rs - c_) - 1 / Rs) == 0 and dshell == 0,
    "phi_in = %s, dphi/dc = %s" % (sp.simplify(shell_in.subs(gap, Rs - c_)), dshell))

print()
print("RESULT:", "ALL PASS" if not FAIL else "FAILED: " + ", ".join(FAIL))
sys.exit(1 if FAIL else 0)
