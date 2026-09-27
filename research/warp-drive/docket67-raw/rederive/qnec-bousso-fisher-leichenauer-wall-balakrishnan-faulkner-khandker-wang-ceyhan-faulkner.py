#!/usr/bin/env python3
"""
DOCKET 67 re-derivation: QNEC (Bousso-Fisher-Koeller-Leichenauer-Wall 1509.02542;
Balakrishnan-Faulkner-Khandker-Wang 1706.09432; Ceyhan-Faulkner 1812.04683) as used by
research/warp-drive/anec.py and bounds.py.

What is finite / closed-form here, and what each check tests:
  Q1  QNEC => ANEC by integration (BFKLW p.2: "in situations where the boundary term S'_out
      vanishes at early and late times").  sympy: INT S'' = [S'].  Then an explicit profile
      that saturates QNEC pointwise with [S'] != 0 and has NEGATIVE INT T_kk -- the boundary
      hypothesis is load-bearing, not decorative.
  Q2  z3: the same statement machine-checked on a finite box (discretised generator, n cells):
      pointwise discrete QNEC + zero end-differences  =>  sum T h >= 0   (UNSAT of negation);
      drop the end condition -> SAT (a witness with sum T h < 0).
  Q3  classical limit: RHS carries hbar; hbar -> 0 at fixed S'' returns the NEC T_kk >= 0
      (BFLW 1506.02669 footnote 8).  So on a CLASSICAL T_mu_nu (anec.py's input) QNEC
      says exactly what the NEC says, and no more.
  Q4  affine parametrisation.  ANEC/QNEC use an affine lambda.  For anec.py's frozen metric
      g = -dt^2 + (dx - F dt)^2 + dy^2 + dz^2 (F = v_s f, t-independent), the curve
      k = (1, F+1, 0, 0) has conserved k_t = -(1+F) only after rescaling: the affine tangent
      is K = k/(1+F), with dlambda = dx.  So the ANEC integral is INT T_kk/(1+F)^2 dx, not the
      tree's INT T_kk dx.  Computed numerically with the tree's own typefour/anec functions
      (imported read-only) on y = 0.  Also Gamma^y_kk = F_y: off-axis 'rays' are not geodesics.
Exit 0 iff every check matches what is recorded in the audit JSON.
"""
import math, sys, os
import sympy as sp

ok = True
def chk(label, cond, note=""):
    global ok
    ok &= bool(cond)
    print("  [%s] %s %s" % ("ok" if cond else "FAIL", label, note))

print("Q1  QNEC integrates to ANEC only with the boundary term")
lam, a, w, hb = sp.symbols('lambda a w hbar', positive=True)
L = sp.symbols('L', positive=True)
Sp = sp.Function('Sp')
# fundamental theorem of calculus, generic S'
expr = sp.integrate(sp.diff(Sp(lam), lam), (lam, -L, L))
chk("INT_{-L}^{L} S'' dlambda = S'(L) - S'(-L)", sp.simplify(expr - (Sp(L) - Sp(-L))) == 0)
# saturating profile with non-vanishing boundary term
Sprime = -a * sp.tanh(lam / w)                  # S' -> -a (lambda->+inf), +a (lambda->-inf)
Spp = sp.diff(Sprime, lam)
Tkk = hb / (2 * sp.pi) * Spp                    # QNEC saturated pointwise: T_kk = (hbar/2pi) S''
anec = sp.integrate(Tkk, (lam, -sp.oo, sp.oo))
print("      S' = -a tanh(lambda/w):  [S'] = %s,  INT T_kk = %s" %
      (sp.limit(Sprime, lam, sp.oo) - sp.limit(Sprime, lam, -sp.oo), sp.simplify(anec)))
chk("QNEC holds pointwise (T_kk - (hbar/2pi)S'' = 0 >= 0)", sp.simplify(Tkk - hb/(2*sp.pi)*Spp) == 0)
chk("yet INT T_kk dlambda = -a hbar/pi < 0 : ANEC fails when [S'] != 0",
    sp.simplify(anec + a * hb / sp.pi) == 0)
# with vanishing boundary term: bump S'
Sprime0 = -a * lam * sp.exp(-lam**2 / w**2)
anec0 = sp.integrate(hb / (2*sp.pi) * sp.diff(Sprime0, lam), (lam, -sp.oo, sp.oo))
chk("with S' -> 0 at both ends the saturating profile has INT T_kk = 0 (ANEC, saturated)",
    sp.simplify(anec0) == 0)

print("\nQ2  z3 on a finite box (n = 10 cells, h = 1)")
import z3
n = 10
S = [z3.Real('S%d' % i) for i in range(n + 2)]
T = [z3.Real('T%d' % i) for i in range(1, n + 1)]
def qnec_disc(sv):
    return [T[i - 1] >= (sv[i + 1] - 2 * sv[i] + sv[i - 1]) for i in range(1, n + 1)]
s = z3.Solver()
s.add(qnec_disc(S))
s.add(S[1] - S[0] == 0, S[n + 1] - S[n] == 0)       # S' = 0 at both ends
s.add(z3.Sum(T) < 0)
r1 = s.check()
chk("pointwise QNEC + S'(ends)=0  AND  sum T < 0 : UNSAT (so QNEC => ANEC on the box)", r1 == z3.unsat, str(r1))
s2 = z3.Solver()
s2.add(qnec_disc(S))
s2.add(z3.Sum(T) < 0)
r2 = s2.check()
wit = ""
if r2 == z3.sat:
    m = s2.model()
    tot = sum(float(m.eval(t_).as_fraction()) for t_ in T)
    d0 = float(m.eval(S[1] - S[0]).as_fraction()); d1 = float(m.eval(S[n + 1] - S[n]).as_fraction())
    wit = "(witness: sum T = %.3g, S'(start) = %.3g, S'(end) = %.3g)" % (tot, d0, d1)
chk("drop the end condition: SAT (QNEC alone does not give ANEC)", r2 == z3.sat, wit)
s3 = z3.Solver()
s3.add(qnec_disc(S)); s3.add(S[n + 1] - S[n] - (S[1] - S[0]) >= 0); s3.add(z3.Sum(T) < 0)
chk("weaker: [S'] >= 0 suffices (UNSAT)", s3.check() == z3.unsat)

print("\nQ3  classical limit")
Tsym, Spp_s = sp.symbols('T_kk Spp', real=True)
bound = hb / (2 * sp.pi) * Spp_s
chk("hbar -> 0 at fixed S'': QNEC RHS -> 0, i.e. QNEC -> NEC (T_kk >= 0)", sp.limit(bound, hb, 0) == 0)

print("\nQ4  the tree's ray integral vs the affine ANEC integral (frozen metric, y = 0)")
t, x, y, z = sp.symbols('t x y z', real=True)
Ff = sp.Function('F')(x, y, z)
g = sp.Matrix([[-1 + Ff**2, -Ff, 0, 0], [-Ff, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
k = sp.Matrix([1, Ff + 1, 0, 0])
chk("k = (1, F+1, 0, 0) is null", sp.simplify((k.T * g * k)[0]) == 0)
k_low_t = sp.simplify((g * k)[0])
chk("k_t = -(1+F) (not constant along the ray where F varies)", sp.simplify(k_low_t + 1 + Ff) == 0, "k_t = %s" % k_low_t)
K = k / (1 + Ff)
chk("K = k/(1+F) has K_t = -1 (conserved Killing energy: affine) and K^x = 1 (dlambda = dx)",
    sp.simplify((g * K)[0] + 1) == 0 and sp.simplify(K[1] - 1) == 0)
X = [t, x, y, z]; gi = g.inv()
def Gam(a_, b_, c_):
    return sp.Rational(1, 2) * sum(gi[a_, d_] * (sp.diff(g[d_, b_], X[c_]) + sp.diff(g[d_, c_], X[b_]) - sp.diff(g[b_, c_], X[d_])) for d_ in range(4))
gy = sp.simplify(sum(Gam(2, b_, c_) * k[b_] * k[c_] for b_ in range(4) for c_ in range(4)))
chk("Gamma^y_ab k^a k^b = F_y : zero on the axis, NONZERO off it (y != 0 'rays' are not geodesics)",
    sp.simplify(gy - sp.diff(Ff, y)) == 0, "Gamma^y_kk = %s" % gy)

WD = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, WD)
cwd = os.getcwd(); os.chdir(WD)
try:
    import anec, typefour as tf     # read-only import; nothing is written
finally:
    os.chdir(cwd)
def Fnum(p): return tf.VS * tf.shape(math.sqrt(sum(c * c for c in p)))
def ray(yv, a_=-4.0, b_=4.0, N=320):
    hh = (b_ - a_) / N
    tree = aff = 0.0; mn = 1e9
    for i in range(N):
        xv = a_ + (i + 0.5) * hh
        tk = anec.T_kk((xv, yv, 0.0))
        tree += tk * hh
        aff += tk / (1.0 + Fnum((xv, yv, 0.0)))**2 * hh
        mn = min(mn, tk)
    return tree, aff, mn
tr, af, mn = ray(0.0)
print("      y = 0.0: tree INT T_kk dx = %+.5f ;  affine INT T_KK dlambda = %+.5f ; min T_kk = %+.4f" % (tr, af, mn))
chk("tree integral reproduces anec.py's -0.0807 at y = 0 (2%)", abs(tr + 0.0807) < 0.02 * 0.0807)
chk("affine on-axis ANEC integral is also negative (sign survives the reparametrisation)", af < 0)
chk("affine value agrees with the sibling alcubierre audit E8 frozen -0.05241 (2%)", abs(af + 0.05241) < 0.02 * 0.05241)
Fy = (Fnum((0.9, 0.3 + 1e-5, 0)) - Fnum((0.9, 0.3 - 1e-5, 0))) / 2e-5
print("      F_y at (0.9, 0.3, 0) = %+.4f  (the y-acceleration of the tree's y = 0.3 'ray')" % Fy)
chk("off-axis ray at y = 0.3 has nonzero geodesic deviation (|F_y| > 0.1)", abs(Fy) > 0.1)

print("\nOVERALL:", "PASS" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
