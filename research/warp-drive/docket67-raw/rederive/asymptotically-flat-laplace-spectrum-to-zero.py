#!/usr/bin/env python3
"""DOCKET 67 re-derivation: 'an asymptotically flat complete spatial slice has
Laplace spectrum running continuously down to zero (w_min = 0)'
(research/warp-drive/fewsterteo.py:95-97, 175-176, 609-610).

What is checked, and how:
  S1 sympy  F&T (5.6)'s C is sqrt(kappa/a^2 + mu^2) (their (5.7)); for kappa = 1
            it equals sqrt(inf spec(-Lap_{H^3_a} + mu^2)) -- the radial reduction
            psi = u/sinh(chi) turns -Lap into -(1/a^2)(d^2/dchi^2 - 1).
  S2 sympy  flat R^3: Rayleigh quotient of chi(r/R) scales EXACTLY as 1/R^2
            (so inf spec = 0); Weyl residual for sin(kr)*gaussian envelope of
            width L is O(1/L^2) -> [0,oo) in sigma_ess.
  S3 numeric on the CORRIDOR (concentric.py's Phi, m = 5e-3, a = 0.02, R_s = 200,
            b = 1; metric forms RECONSTRUCTED, two of them): the static KG
            operator K = -(N/sqrt h) d_i(N sqrt h h^ij d_j) (the operator whose
            spectrum is omega^2 for a static, not ultrastatic, slice) and the
            Laplace-Beltrami operator of h: Rayleigh quotients of far-out test
            functions -> 0 like 1/R^2, and the k = 1 Weyl residual -> 0.
  S4 controls: H^3 (a = 1) quotients stay >= 1 (the instrument CAN see a gap);
            mass mu gives inf >= mu^2 inf N^2 (massless is load-bearing);
            Robin boundary on an incomplete slice gives eigenvalue -alpha^2
            (completeness / nonnegative extension is load-bearing for '>= 0');
            Wigner-von Neumann: an O(1/r) oscillating perturbation carries an
            L^2 eigenvalue embedded at E = 1 ('continuously' needs a decay
            hypothesis the tree does not state; the tree does not use it).
  S5 numeric: the tree's 'most generous' cavity gap C = b/R_s = 0.005 vs the
            Dirichlet ball gap pi/R_s (and Neumann 0), pushed through the
            tree's ratio() read-only (bytecode writing disabled).
"""
import sys, math, os
sys.dont_write_bytecode = True
import sympy as sp
import numpy as np
from scipy import integrate

ok_all = True
def chk(name, cond, detail=""):
    global ok_all
    ok_all &= bool(cond)
    print("  [%s] %s %s" % ("ok" if cond else "FAIL", name, detail))

print("S1  F&T (5.6)/(5.7): C^2 = kappa/a^2 + mu^2 = inf spec on H^3")
chi, a, mu, lam = sp.symbols('chi a mu lambda', positive=True)
u = sp.Function('u')
psi = u(chi) / sp.sinh(chi)
# radial Laplace-Beltrami on H^3 of radius a: (1/(a^2 sinh^2)) d/dchi (sinh^2 d/dchi)
lap = sp.diff(sp.sinh(chi)**2 * sp.diff(psi, chi), chi) / (a**2 * sp.sinh(chi)**2)
red = sp.simplify(-lap * sp.sinh(chi) - (-(sp.diff(u(chi), chi, 2) - u(chi)) / a**2))
chk("-Lap(u/sinh) * sinh == -(u'' - u)/a^2", red == 0)
# so -Lap + mu^2 = -(1/a^2) d^2 + 1/a^2 + mu^2 on L^2(dchi): inf spec = 1/a^2 + mu^2
C57 = sp.sqrt(1 / a**2 + mu**2)
chk("C (5.7, kappa=1) == sqrt(1/a^2 + mu^2) == sqrt(inf spec)", sp.simplify(C57**2 - (1/a**2 + mu**2)) == 0)
chk("C -> mu as a -> oo (Minkowski row of (5.7))", sp.limit(C57, a, sp.oo) == mu)

print("S2  flat R^3: exact 1/R^2 scaling and Weyl sequences")
r, R, k, L, r0 = sp.symbols('r R k L r0', positive=True)
f = sp.exp(-r**2 / R**2)            # test function chi(r/R)
num = sp.integrate(sp.diff(f, r)**2 * r**2, (r, 0, sp.oo))
den = sp.integrate(f**2 * r**2, (r, 0, sp.oo))
RQ = sp.simplify(num / den)
chk("Rayleigh quotient of exp(-r^2/R^2) on R^3 = 3/R^2", sp.simplify(RQ - 3 / R**2) == 0, "(%s)" % RQ)
# Weyl: radial u = r psi, -Lap psi = -(1/r) u''; u = sin(k x) g(x), g gaussian of width L
x = sp.symbols('x', real=True)
g = sp.exp(-x**2 / (2 * L**2))
uu = sp.sin(k * x) * g
res = sp.simplify(-sp.diff(uu, x, 2) - k**2 * uu)
N2 = sp.integrate(sp.expand(sp.simplify(res**2).rewrite(sp.exp)), (x, -sp.oo, sp.oo))
D2 = sp.integrate(sp.expand((uu**2).rewrite(sp.exp)), (x, -sp.oo, sp.oo))
W = sp.simplify(N2 / D2)
Wlead = sp.limit(W * L**2, L, sp.oo)
chk("Weyl residual^2 ||(-d^2-k^2)u||^2/||u||^2 ~ %s / L^2 -> 0" % Wlead,
    sp.limit(W, L, sp.oo) == 0 and Wlead.is_positive)

print("S3  the corridor (concentric.py Phi; m=5e-3, a=0.02, R_s=200, b=1)")
m_, a_, Rs = 5.0e-3, 0.02, 200.0
def Phi(rr):
    return m_ / math.sqrt(rr * rr + a_ * a_) - m_ / max(rr, Rs)
def mass(rr):   # RECONSTRUCTED Schwarzschild-form mass: Plummer core -m, shell +m at R_s
    return -m_ * rr**3 / (rr * rr + a_ * a_) ** 1.5 + (m_ if rr >= Rs else 0.0)
# form A: weak-field isotropic  N^2 = 1+2Phi, h = (1-2Phi) delta
def wA(rr):
    p = Phi(rr); N = math.sqrt(1 + 2 * p); s = (1 - 2 * p)
    return N * s ** 1.5 / s * rr * rr, s ** 1.5 / N * rr * rr     # (kinetic weight, mass weight)
# form B: -F dt^2 + dr^2/F + r^2 dOmega^2, F = 1 - 2 m(r)/r  (radial functions only)
def wB(rr):
    F = 1 - 2 * mass(rr) / rr if rr > 0 else 1.0
    N = math.sqrt(F)
    # sqrt(h) = r^2/sqrt(F) (per solid angle), h^rr = F
    return N * (rr * rr / math.sqrt(F)) * F, (rr * rr / math.sqrt(F)) / N
def wLB(form):
    def w(rr):
        kin, ms = form(rr)
        if form is wA:
            p = Phi(rr); s = 1 - 2 * p
            return s ** 0.5 * rr * rr, s ** 1.5 * rr * rr
        F = 1 - 2 * mass(rr) / rr
        return math.sqrt(F) * rr * rr, rr * rr / math.sqrt(F)
    return w
def bump(c, w):
    # C^1 compact bump (1 - t^2)^2 on [c-w, c+w]
    def f(rr):
        t = (rr - c) / w
        return (1 - t * t) ** 2 if abs(t) < 1 else 0.0
    def fp(rr):
        t = (rr - c) / w
        return -4 * t * (1 - t * t) / w if abs(t) < 1 else 0.0
    return f, fp
def rq(weights, c, w):
    f, fp = bump(c, w)
    pts = [c - w, c, c + w]
    nk = integrate.quad(lambda rr: weights(rr)[0] * fp(rr) ** 2, c - w, c + w, limit=400, points=[c])[0]
    nm = integrate.quad(lambda rr: weights(rr)[1] * f(rr) ** 2, c - w, c + w, limit=400, points=[c])[0]
    return nk / nm
flat = lambda rr: (rr * rr, rr * rr)
table = []
for name, W_ in (("K, form A", wA), ("K, form B", wB), ("Lap_h, form A", wLB(wA)), ("Lap_h, form B", wLB(wB))):
    vals = []
    for w in (1e1, 1e2, 1e3, 1e4, 1e5):
        q = rq(W_, 3 * w, w); qf = rq(flat, 3 * w, w)
        vals.append((w, q, q * w * w, q / qf))
    table.append((name, vals))
    print("   %s:" % name)
    for w, q, qw2, rel in vals:
        print("      width %8.0e  quotient %.6e   quotient*w^2 %.6f   /flat %.9f" % (w, q, qw2, rel))
    chk("%s: quotient -> 0 (last %.3e) and quotient*w^2 -> flat constant (rel %.2e)"
        % (name, vals[-1][1], abs(vals[-1][3] - 1)), vals[-1][1] < 1e-8 and abs(vals[-1][3] - 1) < 1e-6)
    chk("%s: every quotient > 0 (K >= 0 on these)" % name, all(v[1] > 0 for v in vals))
# test functions straddling the core and the shell (the strong-field region) are > 0 too
qc = rq(wA, 150.0, 149.9); qcB = rq(wB, 150.0, 149.9)
chk("quotient > 0 for a test function over core+interior (form A %.3e, B %.3e)" % (qc, qcB), qc > 0 and qcB > 0)

# Weyl residual for K at k = 1 in form B, radial, u-variable is not exact for K;
# compute ||(K - k^2) psi||/||psi|| directly with finite differences on a far window
def weyl_resid(Lw, kk=1.0, form="B"):
    c = 50 * Lw + 1000.0
    rr = np.linspace(c - 8 * Lw, c + 8 * Lw, 400001)
    h = rr[1] - rr[0]
    env = np.exp(-((rr - c) ** 2) / (2 * Lw * Lw))
    psi = np.sin(kk * rr) * env / rr
    if form == "B":
        F = 1 - 2 * np.array([mass(x) for x in rr[::1000]]) / rr[::1000]
        F = np.interp(rr, rr[::1000], F)
        N = np.sqrt(F); sq = rr * rr / np.sqrt(F); hrr = F
    else:
        P = np.array([Phi(x) for x in rr[::1000]]); P = np.interp(rr, rr[::1000], P)
        N = np.sqrt(1 + 2 * P); s = 1 - 2 * P; sq = rr * rr * s ** 1.5; hrr = 1 / s
    dpsi = np.gradient(psi, h)
    flux = N * sq * hrr * dpsi
    Kpsi = -(N / sq) * np.gradient(flux, h)
    wgt = sq / N
    resid = Kpsi - kk * kk * psi
    num = np.trapezoid(wgt * resid ** 2, rr); den = np.trapezoid(wgt * psi ** 2, rr)
    return math.sqrt(num / den)
wr = [(Lw, weyl_resid(Lw, 1.0, "B"), weyl_resid(Lw, 1.0, "A")) for Lw in (10.0, 30.0, 100.0)]
for Lw, rb, ra in wr:
    print("      Weyl residual at k=1, envelope width %5.0f: form B %.4e  form A %.4e  (x L: %.4f %.4f)" % (Lw, rb, ra, rb * Lw, ra * Lw))
chk("K's Weyl residual at omega^2 = 1 falls like 1/L (1 in sigma_ess(K))",
    wr[-1][1] < wr[0][1] / 5 and wr[-1][2] < wr[0][2] / 5)

print("S4  controls and load-bearing hypotheses")
# H^3, a = 1: radial measure sinh^2, bump quotients
def rqH(c, w):
    f, fp = bump(c, w)
    nk = integrate.quad(lambda x: math.sinh(x) ** 2 * fp(x) ** 2, c - w, c + w, limit=400, points=[c])[0]
    nm = integrate.quad(lambda x: math.sinh(x) ** 2 * f(x) ** 2, c - w, c + w, limit=400, points=[c])[0]
    return nk / nm
qH = [rqH(3 * w, w) for w in (1.0, 3.0, 5.0, 8.0)]
print("      H^3 quotients:", ["%.4f" % q for q in qH])
chk("CONTROL: on H^3 (a=1) every quotient >= 1 = gap^2 (instrument sees a gap)", min(qH) >= 1.0)
# massive field: K + mu^2 N^2 has quotient >= mu^2 * inf N^2 > 0
Nmin2 = min(1 + 2 * Phi(x) for x in np.linspace(0.0, 1e4, 20001))
chk("massive field: inf N^2 over the corridor = %.6f > 0, so a mass mu gives gap >= mu*%.4f" % (Nmin2, math.sqrt(Nmin2)), Nmin2 > 0)
al = sp.symbols('alpha', positive=True)
ur = sp.exp(-al * r)
chk("Robin u'(0) = -alpha u(0) on the half-line: -u'' = -alpha^2 u, u in L^2",
    sp.simplify(-sp.diff(ur, r, 2) + al**2 * ur) == 0 and sp.simplify(sp.diff(ur, r).subs(r, 0) + al * ur.subs(r, 0)) == 0
    and sp.integrate(ur**2, (r, 0, sp.oo)) == 1 / (2 * al))
gg = 2 * r - sp.sin(2 * r)
uw = sp.sin(r) / (1 + gg**2)
V = sp.simplify((sp.diff(uw, r, 2) + uw) / uw)
Vn = sp.lambdify(r, V, "mpmath")
import mpmath
tail = max(abs(Vn(mpmath.mpf(x))) * x for x in (1e3, 3e3 + 0.7, 1e4 + 0.3, 3e4 + 1.1))
norm_u = integrate.quad(lambda x: (math.sin(x) / (1 + (2 * x - math.sin(2 * x)) ** 2)) ** 2, 0, 2000, limit=4000)[0]
chk("Wigner-von Neumann: -u'' + V u = 1*u, |V| r bounded (max %.2f), u in L^2 (norm^2 %.6f)" % (float(tail), norm_u),
    float(tail) < 20 and norm_u < 1)

print("S5  the cavity 'most generous gap' against the Dirichlet/Neumann ball")
here = os.path.dirname(os.path.abspath(__file__))
tree = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, tree)
cwd = os.getcwd(); os.chdir(tree)
try:
    import fewsterteo as ft
    r_tree = ft.ratio(ft.cavity_gap())
    r_dir = ft.ratio(math.pi / Rs)
    r_neu = ft.ratio(0.0)
finally:
    os.chdir(cwd)
print("      C = b/R_s = %.4f -> ratio %.9f ; Dirichlet pi/R_s = %.5f -> %.9f ; Neumann 0 -> %.9f"
      % (1 / Rs, r_tree, math.pi / Rs, r_dir, r_neu))
print("      orders moved: tree %.3e, Dirichlet %.3e" % (-math.log10(r_tree), -math.log10(r_dir)))
chk("Dirichlet gap is pi x the tree's 'most generous' C; ratio still > 0.99999 (conclusion unmoved)",
    abs((math.pi / Rs) / ft.cavity_gap() - math.pi) < 1e-12 and r_dir > 0.99999)
chk("tree's corridor gap 0 -> ratio 1 to 1e-8", abs(r_neu - 1) < 1e-8)

# photon-mass threshold: a mass gap C = mu c^2 tau/hbar with tau = b/c ; ratio >= 0.999999 needs C <= 0.005
hbarc_eV_m = 197.3269804e6 * 1e-15   # eV m  (hbar c, exact under SI 2019 to the digits shown)
for b in (1.0, 1e3, 1.5e11):
    print("      b = %.1e m: a mass gap stays inside C <= 0.005 for m c^2 <= %.3e eV" % (b, 0.005 * hbarc_eV_m / b))
print("\nALL CHECKS:", "PASS" if ok_all else "FAIL")
sys.exit(0 if ok_all else 1)
