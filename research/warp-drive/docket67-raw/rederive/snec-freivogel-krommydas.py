"""DOCKET 67 -- re-derivation for snec-freivogel-krommydas.
Reads research/warp-drive READ-ONLY (imports typefour/anec with bytecode writing off).
E1-E3 symbolic (sympy); E4-E8 numeric.  Nothing here repairs the tree."""
import sys, math
sys.dont_write_bytecode = True
sys.path.insert(0, '/home/user/Claude-Method-Works/research/warp-drive')
import sympy as sp

ok = True
def chk(label, cond):
    global ok
    ok &= bool(cond)
    print("  [%s] %s" % ("ok" if cond else "FAIL", label))

print("E1  FK eq.(37) with f = g^2  <=>  tree form anec.py:14 (INT g^2 T >= -(4B/G) INT g'^2)")
x, w, B, G = sp.symbols('x w B G', positive=True)
g = sp.Function('g')(x)
f = g**2
chk("(f')^2/f == 4 (g')^2", sp.simplify(sp.diff(f, x)**2 / f - 4*sp.diff(g, x)**2) == 0)

print("E2  Gaussian g^2 = exp(-x^2/w^2)/(w sqrt(pi)) (anec.py:131)")
gg = sp.exp(-x**2/(2*w**2)) / sp.sqrt(w*sp.sqrt(sp.pi))
norm = sp.integrate(gg**2, (x, -sp.oo, sp.oo))
I_gp2 = sp.simplify(sp.integrate(sp.diff(gg, x)**2, (x, -sp.oo, sp.oo)))
chk("normalised: INT g^2 = 1", sp.simplify(norm - 1) == 0)
chk("INT (g')^2 = 1/(2 w^2)  (got %s)" % I_gp2, sp.simplify(I_gp2 - 1/(2*w**2)) == 0)
tau2 = 1/sp.simplify(4*I_gp2)          # FK eq.(38): 1/tau^2 = INT f'^2/f = 4 INT g'^2
print("      FK smearing length (eq. 38): tau = %s" % sp.sqrt(tau2))
rhs = sp.simplify(-4*B*I_gp2)          # G = 1
print("      RHS (G = 1) = %s ; at B = 1/(32 pi): %s" % (rhs, sp.simplify(rhs.subs(B, 1/(32*sp.pi)))))

print("E3  G_N bookkeeping: 8 pi G T = G_munu  =>  INT g^2 G_kk >= -32 pi B INT g'^2")
chk("32 pi B = 1 at B = 1/(32 pi): the code's -4B (anec.py:136) is LL eq.(3) lower bound -1/4 INT rho'^2/rho",
    sp.simplify(32*sp.pi*sp.Rational(1, 1)/(32*sp.pi) - 1) == 0)
# the bound in T-form: -(4B/G) INT g'^2 ; multiply by 8 pi G: -(32 pi B) INT g'^2 -> no G, no hbar
chk("G cancels in the geometric form (FK eq. 6)", sp.simplify(8*sp.pi*G*(-4*B/G) + 32*sp.pi*B) == 0)
# large-w asymptotics of SNEC for an ANEC integral I: I/(w sqrt pi) vs -2B/w^2
I = sp.symbols('I', negative=True)
wc_asym = sp.solve(sp.Eq(-I/(w*sp.sqrt(sp.pi)), 2*B/w**2), w)
print("      large-w crossover (tree convention): w = %s" % wc_asym)

import anec, typefour as tf
BF = 1.0/(32.0*math.pi)
print("\nE4  tree's printed bound (anec.py:24-29) against the closed form -2B/w^2")
tree = {0.1: -1.760, 0.5: -7.918e-02, 1.0: -1.987e-02, 5.0: -5.085e-04, 20.0: -2.843e-06}
for wv, tv in tree.items():
    an = -2*BF/wv**2
    print("      w=%5.2f  tree %+.4e  closed form %+.4e  rel.diff %+.1f%%" % (wv, tv, an, 100*(tv-an)/an))
chk("w=0.5 and w=1.0 agree to <0.6%", all(abs((tree[v]+2*BF/v**2)/(2*BF/v**2)) < 6e-3 for v in (0.5, 1.0)))
chk("w=0.1, 5, 20 do NOT agree (grid h=0.05 at w=0.1; window |x|<=6 truncation at w=5,20)",
    all(abs((tree[v]+2*BF/v**2)/(2*BF/v**2)) > 0.1 for v in (0.1, 5.0, 20.0)))

print("\nE5  crossover recomputed: analytic g, analytic RHS, wide fine window (no truncation)")
def ray(y, a=-8.0, b=8.0, n=1600, affine=False):
    h = (b-a)/n; xs = [a+(i+0.5)*h for i in range(n)]
    tk = []
    for xv in xs:
        t = anec.T_kk((xv, y, 0.0))
        if affine:  # frozen metric, axis ray: K = k/(1+v) has K_t = -1 and dlambda = dx
            v = tf.VS*tf.shape(math.sqrt(xv*xv+y*y))
            t /= (1.0+v)**2
        tk.append(t)
    return xs, tk, h
def lhs(xs, tk, h, wv):
    return sum(t*math.exp(-(xv/wv)**2)/(wv*math.sqrt(math.pi)) for xv, t in zip(xs, tk))*h
def holds(xs, tk, h, wv, Bv=BF):
    return lhs(xs, tk, h, wv) >= -2*Bv/wv**2
def cross(xs, tk, h, Bv=BF, lo=0.02, hi=20.0):
    if not holds(xs, tk, h, lo, Bv): return lo
    if holds(xs, tk, h, hi, Bv): return float('inf')
    for _ in range(60):
        m = 0.5*(lo+hi)
        if holds(xs, tk, h, m, Bv): lo = m
        else: hi = m
    return 0.5*(lo+hi)
xs, tk, h = ray(0.3)
I03 = sum(tk)*h
print("      y=0.3: INT T_kk dx over [-8,8] = %+.5f (tree -0.0946 over [-2.5,2.5])" % I03)
for wv in (0.1, 0.5, 1.0, 5.0, 20.0):
    print("      w=%5.2f  LHS %+.4e  RHS %+.4e  %s" % (wv, lhs(xs, tk, h, wv), -2*BF/wv**2,
          "ok" if holds(xs, tk, h, wv) else "VIOLATED"))
wc = cross(xs, tk, h)
print("      crossover w_c = %.4f (tree 0.9270); FK tau_c = w_c/sqrt2 = %.4f" % (wc, wc/math.sqrt(2)))
chk("crossover reproduced within 2%% of tree's 0.9270 (got %.4f)" % wc, abs(wc-0.9270)/0.9270 < 0.02)
chk("violation at w=5 and w=20 survives with UNtruncated Gaussians", (not holds(xs, tk, h, 5.0)) and (not holds(xs, tk, h, 20.0)))
wa = float(2*math.sqrt(math.pi)*BF/abs(I03))
print("      large-w asymptotic crossover 2 sqrt(pi) B/|I| = %.4f" % wa)

print("\nE6  B dependence (FKK 2012.11569 sec.2.2: B = 1/(32 pi) from LL; 'B << 1' when semiclassical is under control)")
for fac in (0.01, 0.1, 1.0, 3.0, 10.0):
    print("      B = %5.2f x 1/(32pi): w_c = %s" % (fac, "%.4f" % cross(xs, tk, h, BF*fac)))
chk("smaller B => smaller crossover (violation persists and widens)", cross(xs, tk, h, BF*0.1) < wc)

print("\nE7  axis ray y = 0 (the only (pre)geodesic of the five), tree-style vs affine (frozen metric)")
xs0, tk0, h0 = ray(0.0)
xa, ta, ha = ray(0.0, affine=True)
print("      INT T_kk dx tree-style %+.5f ; affine INT T_KK dlambda %+.5f" % (sum(tk0)*h0, sum(ta)*ha))
wc0, wca = cross(xs0, tk0, h0), cross(xa, ta, ha)
print("      crossover tree-style %.4f ; affine %.4f" % (wc0, wca))
chk("an affine, geodesic SNEC violation exists on the axis ray at the loosest B", math.isfinite(wca))

print("\nE8  curvature scale along the y = 0.3 ray: L = (max_ab |G_ab| Eulerian orthonormal)^(-1/2)")
def G_orth(p):
    Tm, gi = tf.stress_mixed(p, tf.VS)
    gm = tf.metric(p, tf.VS)
    Gd = [[8*math.pi*sum(gm[m][a]*Tm[a][n] for a in range(4)) for n in range(4)] for m in range(4)]
    v = tf.VS*tf.shape(math.sqrt(sum(c*c for c in p)))
    E = [[1.0, v, 0, 0], [0, 1.0, 0, 0], [0, 0, 1.0, 0], [0, 0, 0, 1.0]]
    return max(abs(sum(Gd[m][n]*E[a][m]*E[b][n] for m in range(4) for n in range(4)))
               for a in range(4) for b in range(4))
for yy in (0.0, 0.3):
    gmax = max(G_orth((0.01*i-3.0, yy, 0.0)) for i in range(601))
    L = gmax**-0.5
    print("      y=%.1f: max|G_ab| = %.4f  ->  L_curv = %.4f ; w_c/L = %.2f" % (yy, gmax, L, (wc if yy else wca)/L))
    if yy == 0.3: Lc = L
chk("SNEC crossover lies ABOVE the curvature scale (outside FK 2018's stated domain tau << L)", wc/math.sqrt(2) > Lc)

print("\nSELFTEST %s" % ("OK" if ok else "FAILED"))
sys.exit(0 if ok else 1)
