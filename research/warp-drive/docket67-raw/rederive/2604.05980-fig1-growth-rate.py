"""DOCKET 67 audit, key 2604.05980-fig1-growth-rate.

Pitre, Schneider & Poisson, arXiv:2604.05980v1, Fig. 1 (p.3), as the tree uses it:
wall.py:131-134, 440  PSP_K = 0.6 "PINNED from their Fig. 1: Im{omega}(R^3/M)^{1/2}, 0.52-0.66",
applied to "the l >= 2 even-parity matter mode" (wall.py:454) at compactness x ~ 1e-24.

What Fig. 1 prints (cached alphaXiv page text, p.3, md5 9916ebc7...): l = 2 ONLY;
left panel Im{omega (R^3/M)^{1/2}} vs M/R in [0.00, 0.30] at Gamma = 2, y-ticks 0.52..0.66;
right panel vs Gamma in [1.8, 2.4] at M/R = 0.2, y-ticks 0.56..0.64. The data values are
dots on a plot; no number is printed.

This script (written for this audit; it re-implements the Newtonian thin-shell membrane
equations from first principles rather than importing the sibling audit):
 (1) builds the Newtonian restoring matrix L for (h, j), G = M = R = 1;
 (2) checks it against printed items: l=0 eigenvalue Gamma-3/2 (p.41), l=1 eigenvalues and
     translation zero mode (10.57), the h-row combination and denominator of (10.52b), and --
     NEW here -- the tidal-forcing structure of (10.53a,b): for tidal forcing F ~ (l, 1),
     (L F)_h / F_h = -(l-1)(2 Gamma + l - 2)/4, which is exactly what makes the printed forcing
     coefficients 2Gamma - 4kappa^2/(l-1) + l - 2 and 2Gamma + 4omega^2/(l-1) + l - 2 come out;
 (3) evaluates the Newtonian (M/R -> 0) l = 2 coefficient -- the regime where the tree applies
     PSP_K -- and its Gamma dependence, and the l dependence;
 (4) checks the scale-freeness that makes "masses/radii far from the samples" a non-issue;
 (5) recomputes every number that rests on PSP_K (wall.py:630-653, typefour.py:290) at
     k = 0.6, at the Newtonian l = 2 value, and at l = 3, 4, 10;
 (6) reads the tree's own Vlasov wall's effective Gamma in the Newtonian limit via its Eq (2.7)
     conversion (wall.py imported read-only, no bytecode written).
Exits 1 on any failure.  The j-row of L (tangential equation) is validated only at l = 0, 1:
the printed general-l eigenvalues (p.40) were not in the pages read.
"""
import sys, math
sys.dont_write_bytecode = True
import sympy as sp

FAIL = []
def ok(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)

l, G, lam = sp.symbols('l Gamma lam', positive=True)
h, j = sp.symbols('h j')
sig0 = 1 / (4 * sp.pi)          # M/(4 pi R^2)
pos = sp.Rational(1, 4)         # p/sigma = GM/(4R): radial balance 2p/R = sigma*(GM/R^2)/2
K0 = 2
# first-order potential of the displaced, tangentially redistributed shell:
# mass per solid angle sigma0(1 + l(l+1) j Y), radius 1 + h Y
qext = sig0 * (l * (l + 1) * j + l * h)          # exterior multipole weight (r'^l)
qint = sig0 * (l * (l + 1) * j - (l + 1) * h)    # interior weight (r'^-(l+1))
A = -4 * sp.pi * qext / (2 * l + 1)              # Phi_ext = A r^-(l+1) Y
B = -4 * sp.pi * qint / (2 * l + 1)              # Phi_int = B r^l Y
dsig = -(2 * h - l * (l + 1) * j)                # Lagrangian Delta sigma / sigma
dK_over_K = (l - 1) * (l + 2) * h / 2            # (10.23)
# radial accel (coefficient of Y): background field averaged over faces at displaced radius
# gives +h; perturbed field averaged over faces; membrane delta(pK/sigma)
ar = h + ((l + 1) * A - l * B) / 2 + pos * K0 * ((G - 1) * dsig + dK_over_K)
# tangential accel (coefficient of grad_Omega Y): -avg(Phi1); normal tilt p K n; -grad_s p
at = -(A + B) / 2 + pos * (-K0 * h - G * dsig)
L = -sp.Matrix([[sp.diff(ar, h), sp.diff(ar, j)], [sp.diff(at, h), sp.diff(at, j)]]).applyfunc(sp.simplify)
tr, dt = sp.simplify(L.trace()), sp.factor(L.det())
print("L =", L.tolist()); print("trace =", sp.factor(tr)); print("det =", dt)

# (2) printed checks
ok("l=0: lambda = Gamma - 3/2 (p.41)", sp.simplify(L[0, 0].subs(l, 0) - (G - sp.Rational(3, 2))) == 0)
ev1 = set(sp.simplify(e) for e in L.subs(l, 1).eigenvals())
ok("l=1: eigenvalues {0, (3Gamma-4)/2} (10.57)", ev1 == {0, sp.simplify((3 * G - 4) / 2)})
ok("l=1: zero mode j = h (translation)", sp.simplify(L.subs(l, 1) * sp.Matrix([1, 1])) == sp.zeros(2, 1))
ok("(10.52b) combination (2l+1)(Gamma-w^2) - (2l^3-l^2+9l+6)/4 = (2l+1)(L11 - w^2)",
   sp.simplify((2 * l + 1) * L[0, 0] - ((2 * l + 1) * G - (2 * l**3 - l**2 + 9 * l + 6) / 4)) == 0)
ok("(10.52b) denominator (2l+1)Gamma - 2(l+1) proportional to L12",
   sp.simplify(-2 * (2 * l + 1) * L[0, 1] / (l * (l + 1)) - ((2 * l + 1) * G - 2 * (l + 1))) == 0)
F = sp.Matrix([l, 1])     # tidal forcing from U = e r^l Y: radial l e, tangential e (common sign)
ratio = sp.simplify((L * F)[0] / F[0])
ok("(10.53a,b) forcing structure: (L F)_h/F_h = -(l-1)(2Gamma+l-2)/4  [got %s]" % sp.factor(ratio),
   sp.simplify(ratio + (l - 1) * (2 * G + l - 2) / 4) == 0)

# (3) growth rates
def kappa(ll, g):
    Ln = L.subs({l: ll, G: g})
    a, b = float(Ln.trace()), float(Ln.det())
    disc = a * a - 4 * b
    lm = (a - math.sqrt(disc)) / 2 if disc >= 0 else None
    return math.sqrt(-lm) if (lm is not None and lm < 0) else 0.0
k22 = kappa(2, 2)
print("\nNewtonian l=2 coefficient kappa_2(Gamma) = Im omega sqrt(R^3/GM):")
for g in (1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 3.0, 5.0, 100.0):
    print("   Gamma = %6.2f   kappa_2 = %.5f" % (g, kappa(2, g)))
ok("kappa_2(Gamma=2) = %.5f, i.e. 14%% below the tree's 0.6" % k22, abs(k22 - 0.5147) < 5e-4)
ok("kappa_2(Gamma=2) sits below Fig.1-left's lowest y-tick 0.52 by %.4f (axis floor; a dot there is consistent only if the axis limit is < 0.52)" % (0.52 - k22),
   0 < 0.52 - k22 < 0.01)
k18, k24 = kappa(2, 1.8), kappa(2, 2.4)
ok("Newtonian kappa_2 over Gamma in [1.8,2.4]: %.4f .. %.4f (spread %.1f%%) -- not flat in Gamma" % (k24, k18, 100 * (k18 - k24) / k24),
   k18 - k24 > 0.07)
# radially stable fluid shells need Gamma >= 3/2 (Newtonian); supremum of kappa_2 on that class
k15 = kappa(2, 1.5)
ok("on the radially stable class Gamma >= 3/2, kappa_2 <= %.4f (at Gamma = 3/2); 0.6 is inside (0.346, %.3f]" % (k15, k15),
   0.6 < k15 and all(kappa(2, 1.5 + 0.01 * i) <= k15 + 1e-12 for i in range(1, 300)))
gs = sp.nsolve(sp.Symbol('g'), 1.6) if False else None
lo, hi = 1.5, 2.0
for _ in range(60):
    mid = (lo + hi) / 2
    if kappa(2, mid) > 0.6: lo = mid
    else: hi = mid
print("   kappa_2 = 0.6 exactly at Gamma = %.4f (Newtonian l = 2)" % lo)
kinf = math.sqrt(0.12)
ok("stiff limit Gamma -> oo: kappa_2 -> sqrt(0.12) = %.4f" % kinf, abs(kappa(2, 1e7) - kinf) < 1e-4)
print("\nl dependence at Gamma = 2 (Newtonian):")
kl = {}
for ll in (2, 3, 4, 5, 10, 20, 100):
    kl[ll] = kappa(ll, 2)
    print("   l = %3d   kappa_l = %.4f   kappa_l/(l/2) = %.4f" % (ll, kl[ll], kl[ll] / (ll / 2)))
ok("kappa_l increases monotonically with l (2..100)", all(kl[a] < kl[b] for a, b in [(2, 3), (3, 4), (4, 5), (5, 10), (10, 20), (20, 100)]))
ok("kappa_3 = %.4f > 0.6: the tree's constant understates l >= 3 by a factor >= %.2f" % (kl[3], kl[3] / 0.6), kl[3] / 0.6 > 1.8)
ok("kappa_l/(l/2) -> 1 (eikonal, membrane with pressure: omega^2 = -(p/sigma) k^2 = -l^2/4)", abs(kl[100] / 50 - 1) < 0.01)

# (4) scale-freeness: omega sqrt(R^3/GM) depends only on (M/R, Gamma, l) -- no other scale in
# the model (vacuum, thin shell, p = K sigma^Gamma with K fixed by equilibrium). Check: L has no
# free dimensional parameter after G = M = R = 1.
ok("L depends only on (l, Gamma): no residual scale", L.free_symbols <= {l, G})

# (5) numbers resting on PSP_K
c, Gsi, a, de, Msun, AU = 299792458.0, 6.67430e-11, 9.80665, 0.2, 1.98847e30, 1.495978707e11
def rho_ceil(k): return 3 * a**2 / (4 * math.pi * Gsi * (k * c * de)**2)
def rmin(M, k, n=1.0): return (Gsi * M * (k * c * de / (n * a))**2) ** (1 / 3)
def efold(M, R, k): return k * math.sqrt(Gsi * M / R**3) * c * de / a
def R_at(x, k): return c * math.sqrt(3 * x / (8 * math.pi * Gsi * rho_ceil(k)))
def M_at(x, k): return rho_ceil(k) * 4 / 3 * math.pi * R_at(x, k)**3
ok("tree rho_max 2.657927437e-4 reproduced at k=0.6 (%.9e)" % rho_ceil(0.6), abs(rho_ceil(0.6) / 2.657927437e-4 - 1) < 1e-9)
ok("tree R_min 964.4 m (N<1) at k=0.6 (%.1f)" % rmin(1e6, 0.6), abs(rmin(1e6, 0.6) - 964.4) < 0.5)
ok("tree R 4.478398718 km (N<0.1) at k=0.6 (%.9f)" % (rmin(1e6, 0.6, 0.1) / 1e3), abs(rmin(1e6, 0.6, 0.1) / 1e3 - 4.478398718) < 1e-8)
ok("tree 1%% binding: 1034.4 AU, 2.075e9 Msun at k=0.6 (%.1f AU, %.4g Msun)" % (R_at(0.0396, 0.6) / AU, M_at(0.0396, 0.6) / Msun),
   abs(R_at(0.0396, 0.6) / AU - 1034.4) < 1 and abs(M_at(0.0396, 0.6) / Msun - 2.075e9) < 1e6)
ok("tree x=0.3: 4.327e10 Msun at k=0.6 (%.4g)" % (M_at(0.3, 0.6) / Msun), abs(M_at(0.3, 0.6) / Msun - 4.327e10) < 1e7)
N10 = efold(1e6, 10.0, 0.6)
print("   typefour.py:290 efoldings(1e6 kg, 10 m) at k=0.6: %.4g" % N10)
print("\n   k source                rho_max(kg/m^3)  R_min(1e6kg,N<1)  R(N<0.1)   M_1%%(Msun)  R_1%%(AU)  M_x0.3(Msun)  N(1e6kg,10m)")
rows = [("tree 0.6", 0.6), ("Newt l=2 G=1.5", k15), ("Newt l=2 G=2", k22), ("Newt l=2 G=2.4", k24),
        ("Newt l=3 G=2", kl[3]), ("Newt l=4 G=2", kappa(4, 2)), ("Newt l=10 G=2", kl[10])]
for lab, k in rows:
    print("   %-22s %.4e      %8.1f m       %8.1f m  %.4g   %7.1f   %.4g   %.4g"
          % (lab, rho_ceil(k), rmin(1e6, k), rmin(1e6, k, 0.1), M_at(0.0396, k) / Msun, R_at(0.0396, k) / AU, M_at(0.3, k) / Msun, efold(1e6, 10, k)))
ok("typefour.py:290 (N > 100) survives any k >= %.4f; min Newtonian l=2 over Gamma>=3/2 is sqrt(0.12)=%.3f -> N = %.4g"
   % (100 / N10 * 0.6, kinf, efold(1e6, 10, kinf)), efold(1e6, 10, kinf) > 100)
ok("the '2e9 Msun over 1000 AU' order survives l=2 Newtonian (M scales as k): %.3g Msun, %.0f AU" % (M_at(0.0396, k22) / Msun, R_at(0.0396, k22) / AU),
   1e9 < M_at(0.0396, k22) / Msun < 3e9)

# (6) the tree's Vlasov wall mapped to a Gamma through Eq (2.7) in the Newtonian limit
try:
    sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        import wall
    x = 1e-9
    _, _, s_, p_ = wall.statics(x, 1.0)
    gv = wall.beta2_vlasov(x) * (s_ + p_) / p_
    print("\n   tree's counter-rotating Vlasov wall, Eq (2.7) Gamma at x = 1e-9: %.6f" % gv)
    ok("the tree's own wall maps to Gamma -> 2 (= 4/3 x 3/2) in the Newtonian limit, where kappa_2 = %.4f not 0.6" % kappa(2, gv),
       abs(gv - 2.0) < 1e-5)
    print("   (a collisionless shell is not a barotropic fluid under non-radial perturbation; this mapping is radial-only)")
except Exception as e:
    ok("import wall.py read-only (%r)" % e, False)

print("\nRESULT:", "ALL PASS" if not FAIL else "FAILURES: %s" % FAIL)
sys.exit(1 if FAIL else 0)
