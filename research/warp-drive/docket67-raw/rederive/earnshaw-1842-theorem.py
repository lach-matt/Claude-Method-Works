#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of Earnshaw's theorem as research/warp-drive/stability.py:114-123
(and chain.py:132-162, 289-339) uses it.

S1  sympy: trace of the Hessian of 1/r is 0 away from r = 0; a sum of point sources of
    SYMBOLIC (any-sign) strengths is harmonic.
S2  sympy: every homogeneous harmonic polynomial of degree k = 1..6 in R^3 has zero mean over
    the unit sphere, so it takes negative values; the leading non-zero Taylor form of a
    non-constant harmonic function at a critical point is such a polynomial, so there is no
    local minimum (strict or not) unless the function is constant.  (That is 'no minimum';
    the step 'no minimum => unstable' is S3/S4 when the Hessian is non-zero, and a named
    classical theorem (Chetaev/Kozlov) otherwise -- evidence given numerically in S5.)
S3  numeric: test particle in the field of fixed point sources of random signs.  At every
    equilibrium located, Hess(phi) is traceless and has a negative eigenvalue => exponential
    growth rate > 0.
S4  numeric: FREE mixed-sign (Bondi: inertial = passive = active) point masses at a static
    equilibrium.  The linearisation K = M^-1 Hess U is NOT symmetric and the kinetic energy is
    indefinite, so 'harmonic => no minimum of U => unstable' (the tree's route) does not apply
    as stated; the trace argument still gives an exponentially growing mode.
S5  numeric: the degenerate case -- phi = x^3 - 3 x y^2 (harmonic, Hessian 0 at the origin,
    not constant): a particle released at rest near the origin leaves it.
S6  sympy: the conclusion rests on the EXACT 1/r kernel.  Lap r^-(1+d) = d(1+d) r^-(3+d);
    Lap e^{-r/L}/r = e^{-r/L}/(L^2 r).  A Yukawa term inside a uniform shell gives
    phi_in = -a G M L e^{-R/L} sinh(r/L)/(R r): isotropic curvature -a G M e^{-R/L}/(3 R L^2)
    at the centre, restoring iff a*M < 0.  Suppression at the Lee et al. 2020 bound
    (lambda < 38.6 um for |alpha| = 1, arXiv:2002.11761) computed for a 1 m shell.
"""
import sys, math, random
import sympy as sp
import numpy as np

FAIL = []
def chk(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ((" -- " + detail) if detail else ""))
    if not cond:
        FAIL.append(name)

x, y, z = sp.symbols('x y z', real=True)
X = (x, y, z)
def lap(f):
    return sum(sp.diff(f, v, 2) for v in X)

# ---------------------------------------------------------------- S1
r = sp.sqrt(x**2 + y**2 + z**2)
H = sp.hessian(1/r, X)
chk("S1a tr Hess(1/r) == 0 (r != 0)", sp.simplify(H.trace()) == 0,
    "H_ij = (3 x_i x_j - delta_ij r^2)/r^5")
q1, q2, q3 = sp.symbols('q1 q2 q3', real=True)     # any sign
a1, b1, c1, a2, b2, c2 = sp.symbols('a1 b1 c1 a2 b2 c2', real=True)
phi = (q1/sp.sqrt((x-a1)**2+(y-b1)**2+(z-c1)**2)
       + q2/sp.sqrt((x-a2)**2+(y-b2)**2+(z-c2)**2) + q3/r)
chk("S1b Laplacian of sum of 3 symbolic-sign point sources == 0", sp.simplify(lap(phi)) == 0)

# ---------------------------------------------------------------- S2
th, ph = sp.symbols('theta phi_', real=True)
for k in range(1, 7):
    mons = [x**i*y**j*z**(k-i-j) for i in range(k+1) for j in range(k+1-i)]
    cs = sp.symbols('c0:%d' % len(mons))
    P = sum(c*m for c, m in zip(cs, mons))
    L = sp.Poly(sp.expand(lap(P)), *X)
    sol = sp.solve(L.coeffs(), cs, dict=True)
    Ph = sp.expand(P.subs(sol[0])) if sol else P
    free = sorted(Ph.free_symbols - set(X), key=str)
    # exact spherical mean of monomials: int x^a y^b z^c dOmega
    def sph_int(a, b, c):
        if a % 2 or b % 2 or c % 2:
            return sp.Integer(0)
        return 2*sp.gamma(sp.Rational(a+1, 2))*sp.gamma(sp.Rational(b+1, 2))*sp.gamma(sp.Rational(c+1, 2))/sp.gamma(sp.Rational(a+b+c+3, 2))
    mean = sum(coef*sph_int(*mon) for mon, coef in sp.Poly(Ph, *X).terms())
    chk("S2 k=%d: dim harmonic = %d (=2k+1), spherical mean == 0" % (k, len(free)),
        len(free) == 2*k+1 and sp.simplify(mean) == 0)

# ---------------------------------------------------------------- S3
rng = np.random.default_rng(1842)
def field_hess(p, src):
    g = np.zeros(3); Hm = np.zeros((3, 3))
    for q, s in src:
        d = p - s; rr = np.linalg.norm(d)
        g += -q*d/rr**3                        # grad of q/r  (phi = -sum q/r, sign irrelevant)
        Hm += q*(3*np.outer(d, d) - np.eye(3)*rr**2)/rr**5
    return g, Hm
n_eq = 0; n_unstable = 0; max_tr = 0.0
for trial in range(400):
    ns = rng.integers(2, 6)
    src = [(rng.choice([-1, 1])*rng.uniform(0.2, 3), rng.normal(size=3)*2) for _ in range(ns)]
    p = rng.normal(size=3)*2
    ok = False
    for it in range(80):                        # Newton on grad = 0
        g, Hm = field_hess(p, src)
        try:
            step = np.linalg.solve(Hm, g)
        except np.linalg.LinAlgError:
            break
        p = p - np.clip(step, -0.5, 0.5)
        if np.linalg.norm(g) < 1e-12:
            ok = True; break
    if not ok or min(np.linalg.norm(p - s) for _, s in src) < 1e-3:
        continue
    g, Hm = field_hess(p, src)
    scale = max(abs(q)/np.linalg.norm(p-s)**3 for q, s in src)
    ev = np.linalg.eigvalsh(Hm)
    n_eq += 1
    max_tr = max(max_tr, abs(np.trace(Hm))/scale)
    if ev.min() < -1e-9*scale and ev.max() > 1e-9*scale:
        n_unstable += 1
chk("S3 fixed sources, random signs: every equilibrium found is a saddle of phi (and of -phi)",
    n_eq > 50 and n_unstable == n_eq,
    "%d equilibria, %d with eigenvalues of both signs, max |tr H|/scale = %.1e" % (n_eq, n_unstable, max_tr))

# ---------------------------------------------------------------- S4
def J(d):
    rr = np.linalg.norm(d)
    return (np.eye(3)*rr**2 - 3*np.outer(d, d))/rr**5
def accel(X3, m):
    n = len(m); a = np.zeros((n, 3))
    for i in range(n):
        for j in range(n):
            if i != j:
                d = X3[j]-X3[i]; a[i] += m[j]*d/np.linalg.norm(d)**3
    return a
def lin(X3, m):
    n = len(m); A = np.zeros((3*n, 3*n))
    for i in range(n):
        for j in range(n):
            if i != j:
                Jd = J(X3[j]-X3[i])
                A[3*i:3*i+3, 3*j:3*j+3] += m[j]*Jd
                A[3*i:3*i+3, 3*i:3*i+3] -= m[j]*Jd
    return A        # delta x'' = A delta x
n_cfg = 0; n_grow = 0; n_nonsym = 0; details = []
for xs in [3.0, 2.0, 5.0, 1.5, 10.0, -2.0, 0.5]:
    pos = np.array([[0, 0, 0], [1, 0, 0], [xs, 0, 0]], float)
    # antisymmetric 3x3 coupling matrix is always singular: its null vector gives the masses
    Cm = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            if i != j:
                d = pos[j, 0]-pos[i, 0]; Cm[i, j] = np.sign(d)/d**2
    m = np.array([Cm[1, 2], Cm[2, 0], Cm[0, 1]])
    res = np.abs(accel(pos, m)).max()
    A = lin(pos, m)
    lam = np.linalg.eigvals(A)                  # growth rate = max Re sqrt(lam)
    rate = max(np.sqrt(lam.astype(complex)).real)
    n_cfg += 1
    signs = ''.join('+' if v > 0 else '-' for v in m)
    nonsym = np.abs(A - A.T).max() > 1e-9
    n_nonsym += nonsym
    if res < 1e-12 and abs(np.trace(A)) < 1e-9 and rate > 1e-6:
        n_grow += 1
    details.append("x3=%g signs=%s resid=%.0e trA=%.0e rate=%.3f" % (xs, signs, res, np.trace(A), rate))
for dline in details:
    print("     " + dline)
chk("S4 free mixed-sign (Bondi) static equilibria: traceless, non-symmetric K, exponential mode",
    n_grow == n_cfg and n_nonsym == n_cfg, "%d/%d configurations" % (n_grow, n_cfg))

# ---------------------------------------------------------------- S5
def rhs(s):
    px, py, vx, vy = s
    # phi = x^3 - 3 x y^2 ; a = -grad phi
    return np.array([vx, vy, -(3*px**2 - 3*py**2), 6*px*py])
s = np.array([1e-3, 0.0, 0.0, 0.0]); dt = 1e-2; t = 0.0
while t < 400 and np.hypot(s[0], s[1]) < 0.5:
    k1 = rhs(s); k2 = rhs(s+dt/2*k1); k3 = rhs(s+dt/2*k2); k4 = rhs(s+dt*k3)
    s = s + dt/6*(k1+2*k2+2*k3+k4); t += dt
chk("S5 degenerate harmonic critical point (Hessian 0, phi = x^3-3xy^2): released at rest at 1e-3, leaves r<0.5",
    np.hypot(s[0], s[1]) >= 0.5, "t_exit = %.1f" % t)

# ---------------------------------------------------------------- S6
rr, d, Ll, R, G, M, al, rho = sp.symbols('r delta lambda R G M alpha rho', positive=True)
lap_rad = lambda f: sp.diff(rr**2*sp.diff(f, rr), rr)/rr**2
chk("S6a Lap r^-(1+d) = d(1+d) r^-(3+d)  (zero only at d = 0)",
    sp.simplify(lap_rad(rr**(-(1+d))) - d*(1+d)*rr**(-(3+d))) == 0)
chk("S6b Lap e^{-r/L}/r = e^{-r/L}/(L^2 r)  (not harmonic)",
    sp.simplify(lap_rad(sp.exp(-rr/Ll)/rr) - sp.exp(-rr/Ll)/(Ll**2*rr)) == 0)
s_ = sp.symbols('s', positive=True)
# shell of mass M radius R, field point at r < R: dA = 2 pi R^2 sin th dth, s ds = R r sin th dth
sigma = M/(4*sp.pi*R**2)
integral = sp.integrate(sp.exp(-s_/Ll)/s_ * 2*sp.pi*R**2*sigma * s_/(R*rho), (s_, R-rho, R+rho))
phi_in = -al*G*integral
target = -al*G*M*Ll*sp.exp(-R/Ll)*sp.sinh(rho/Ll)/(R*rho)
chk("S6c Yukawa interior of a shell: phi_in = -a G M L e^{-R/L} sinh(r/L)/(R r)",
    sp.simplify((phi_in - target).rewrite(sp.exp)) == 0)
newt = sp.integrate(1/s_ * 2*sp.pi*R**2*sigma * s_/(R*rho), (s_, R-rho, R+rho))
chk("S6d Newtonian (L -> inf) interior is constant -G M/R (the tree's degenerate seat)",
    sp.simplify(-G*newt + G*M/R) == 0)
curv = sp.simplify(sp.limit(sp.diff(target, rho, 2), rho, 0))
chk("S6e centre curvature = -a G M e^{-R/L}/(3 R L^2): restoring iff a*M < 0",
    sp.simplify(curv + al*G*M*sp.exp(-R/Ll)/(3*R*Ll**2)) == 0, str(curv))
# stiffness relative to Newtonian scale G M / R^3, at the read bound lambda = 38.6 um, R = 1 m
lam_b = 38.6e-6
for Rm in (1.0, 1e-3, 1e-4):
    ln_ratio = 2*math.log(Rm/lam_b) - Rm/lam_b - math.log(3)
    print("     R = %g m, lambda = 38.6 um, |alpha| = 1: stiffness/(GM/R^3) = 10^%.1f" % (Rm, ln_ratio/math.log(10)))

print("\nALL PASS" if not FAIL else "\nFAILED: %s" % FAIL)
sys.exit(1 if FAIL else 0)
