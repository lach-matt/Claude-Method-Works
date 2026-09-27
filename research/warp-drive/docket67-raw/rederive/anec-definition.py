"""DOCKET 67 -- anec-definition re-derivation.

Published definition (Kontou-Sanders arXiv:2003.01815v2 eq. (83), p.28; Table 4, p.29):
    ANEC:  INT_{-inf}^{inf} d lambda  T_ab(gamma(lambda)) gamma'^a gamma'^b >= 0
    for all INEXTENDIBLE NULL GEODESICS gamma with AFFINE parameter lambda,
    when the integral is absolutely convergent.
K&S p.28: an averaged energy condition averages a contraction of T 'over a
suitable spacetime region'; they restrict to causal geodesics as 'the most
common choice'.

Parts
  A  overturn.py's 'ANEC-analogue' chords (sympy, closed form)
  B  parametrisation dependence of the ANEC integral (sympy)
  C  anec.py's coordinate-line integrals vs the published definition, using the
     tree's own pipeline (typefour.py), from COPIES in _anecdef_src/ -- no file
     under research/warp-drive is imported or written.
"""
import sys, os, math, json
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "_anecdef_src"))
import sympy as sp

out = {}
print("=" * 78)
print("A. overturn.py two-zone profile: chord integrals, closed form")
a, b, r0, R, p, s = sp.symbols("a b r0 R p s", positive=True)
# chord at impact parameter p < r0: rho=-b for |s|<sqrt(r0^2-p^2), +a out to sqrt(R^2-p^2)
Lin = sp.sqrt(r0**2 - p**2)
Lout = sp.sqrt(R**2 - p**2)
chord_in = 2 * (-b * Lin + a * (Lout - Lin))      # 0 <= p < r0
chord_sh = 2 * a * Lout                          # r0 <= p < R
vals = {a: sp.Rational(3, 2), b: 1, r0: 1, R: 2}
c0 = sp.simplify(chord_in.subs(p, 0))
print("  chord(0) =", c0, " at (a,b,r0,R)=(1.5,1,1,2):", c0.subs(vals))
dchord = sp.simplify(sp.diff(chord_in, p))
print("  d chord/dp (p<r0) =", dchord)
# show derivative >= 0 on (0,r0): (a+b)/Lin >= a/Lout since Lin<=Lout
num = [float(dchord.subs(vals).subs(p, q)) for q in (0.0, 0.2, 0.5, 0.8, 0.99)]
print("  d chord/dp at p=0,.2,.5,.8,.99:", ["%.4f" % x for x in num])
mins = min(float(chord_in.subs(vals).subs(p, q / 100.0)) for q in range(0, 100))
mins2 = min(float(chord_sh.subs(vals).subs(p, 1 + q / 100.0)) for q in range(0, 100))
print("  min chord over p in [0,1):", mins, " over [1,2):", mins2)
m_r0 = -sp.Rational(4, 3) * sp.pi * b * r0**3
m_R = sp.Rational(4, 3) * sp.pi * (a * (R**3 - r0**3) - b * r0**3)
print("  m(r0) =", float(m_r0.subs(vals)), " m(R) =", float(m_R.subs(vals)))
lam = sp.symbols("lambda", positive=True)
print("  scaling a=1.5 lam, b=lam: chord(0) =", sp.simplify(c0.subs({a: sp.Rational(3, 2) * lam, b: lam, r0: 1, R: 2})),
      " m(r0) =", sp.simplify(m_r0.subs({b: lam, r0: 1})))
# When does the chord equal the published ANEC integral?  Flat space, static
# perfect fluid T_ab = (rho+P) u_a u_b + P eta_ab, u=(1,0,0,0), null k=(1,n):
rho_, P_ = sp.symbols("rho P", real=True)
eta = sp.diag(-1, 1, 1, 1)
u = sp.Matrix([1, 0, 0, 0]); ul = eta * u
k = sp.Matrix([1, 1, 0, 0])
T = (rho_ + P_) * ul * ul.T + P_ * eta
Tkk = sp.simplify((k.T * T * k)[0])
print("  static perfect fluid, flat space, k=(1,1,0,0): T_kk =", Tkk)
print("  straight null lines are affine geodesics of flat space with d lambda = dx,")
print("  so chord == published ANEC integral iff INT P dl = 0 on that chord (e.g. dust).")
out["A"] = dict(chord0=float(c0.subs(vals)), min_chord=min(mins, mins2),
                m_r0=float(m_r0.subs(vals)), m_R=float(m_R.subs(vals)),
                Tkk_perfect_fluid=str(Tkk))

print("=" * 78)
print("B. parametrisation dependence")
c = sp.symbols("c", positive=True)
f = sp.Function("F")
# affine rescaling lambda -> c*lambda : K -> K/c, d lambda -> c d lambda
print("  affine rescaling lambda'=c lambda: integral' = (1/c^2)*c * integral = integral/c")
print("  => sign is invariant, magnitude is not (normalisation of k is a choice)")
# non-affine reparametrisation: positive weight w = d lambda / d s can flip sign
x = sp.symbols("x", real=True)
Tpro = sp.Piecewise((-1, (x >= 0) & (x < 1)), (sp.Rational(3, 2), (x >= 1) & (x < 2)), (0, True))
w = sp.Piecewise((2, (x >= 0) & (x < 1)), (1, True))
I0 = sp.integrate(Tpro, (x, 0, 2)); I1 = sp.integrate(Tpro * w, (x, 0, 2))
print("  toy: INT T dlambda = %s ;  with positive weight 2 on [0,1): %s" % (I0, I1))
print("  => along a non-affine parameter the SIGN is not the ANEC sign in general")
out["B"] = dict(toy_affine=str(I0), toy_weighted=str(I1))

print("=" * 78)
print("C. anec.py coordinate lines vs the published definition (tree pipeline, copies)")
import typefour as tf
import anec
import achronal
VS = 0.5
rays = (0.0, 0.2, 0.3, 0.5, 0.8)
rec = {0.0: -0.0807, 0.2: -0.0865, 0.3: -0.0946, 0.5: -0.1290, 0.8: -0.3441}
C = {}
print("  C1 reproduce anec.py (x in [-2.5,2.5], n=90) and widen the window")
for y in rays:
    i90 = anec.anec_integral(y)
    iw = anec.anec_integral(y, a=-6.0, b=6.0, n=240)
    print("    y=%.1f  n90 %+.6f (rec %+.4f)   [-6,6] n240 %+.6f" % (y, i90, rec[y], iw))
    C["y=%.1f" % y] = dict(anec_py=i90, recorded=rec[y], wide=iw)

print("  C2 is the fixed-y coordinate line a null geodesic?  A^mu = k^b d_b k^mu + Gamma^mu_bc k^b k^c")
def accel(pp, k, hh=1e-5):
    # covariant acceleration along the curve with tangent k (k^t = 1, stationary metric:
    # k^b d_b = k^x d_x since k^y = k^z = 0 and d_t = 0)
    G = tf.christoffel(pp, VS)
    kp = anec.null_vector((pp[0] + hh, pp[1], pp[2]), VS)
    km = anec.null_vector((pp[0] - hh, pp[1], pp[2]), VS)
    dk = [k[1] * (kp[m] - km[m]) / (2 * hh) for m in range(4)]
    return [dk[m] + sum(G[m][bb][cc] * k[bb] * k[cc] for bb in range(4) for cc in range(4)) for m in range(4)]
geo = {}
for y in (0.0, 0.3, 0.8):
    worst_perp, worst_par = 0.0, 0.0
    for xx in (-1.1, -0.95, -0.9, 0.9, 0.95, 1.05):
        pp = (xx, y, 0.0)
        k = anec.null_vector(pp, VS)
        acc = accel(pp, k)
        # parallel test in (t,x): a^x - (k^x/k^t) a^t measures non-pregeodesic part
        par = acc[1] - k[1] / k[0] * acc[0]
        worst_perp = max(worst_perp, abs(acc[2]))
        worst_par = max(worst_par, abs(par))
    geo[y] = (worst_perp, worst_par)
    print("    y=%.1f  max|A^y| = %.3e   max|A^x - (k^x/k^t)A^t| = %.3e" % (y, worst_perp, worst_par))
C["geodesic_test"] = {str(k_): v for k_, v in geo.items()}

print("  C3 on y=0 (a pregeodesic): conserved k_t and the affine parameter")
for xx in (-3.0, -1.0, -0.9, 0.0, 0.9):
    pp = (xx, 0.0, 0.0)
    g = tf.metric(pp, VS); k = anec.null_vector(pp, VS)
    kt = sum(g[0][nn] * k[nn] for nn in range(4))
    v = VS * tf.shape(abs(xx))
    print("    x=%+.2f  k_t = %+.6f   -(1+v) = %+.6f" % (xx, kt, -(1 + v)))
print("    => affine tangent K = k/(1+v) (K_t = -1, K^x = 1, so d lambda = dx)")
print("       and the published ANEC integral on y=0 is INT T_kk/(1+v)^2 dx")
def affine_weighted(y, a_=-6.0, b_=6.0, n=240):
    h = (b_ - a_) / n
    s_ = 0.0
    for i in range(n):
        xx = a_ + (i + 0.5) * h
        v = VS * tf.shape(math.sqrt(xx * xx + y * y))
        s_ += anec.T_kk((xx, y, 0.0), VS) / (1 + v) ** 2
    return s_ * h
aw0 = affine_weighted(0.0)
aw0n = affine_weighted(0.0, n=480)
print("    y=0 affine ANEC integral: %+.6f (n240)  %+.6f (n480);  anec.py coordinate %+.6f"
      % (aw0, aw0n, C["y=0.0"]["anec_py"]))
C["y0_affine"] = dict(n240=aw0, n480=aw0n)

print("  C4 cross-check against the tree's own affine geodesic integrator (achronal.py copy)")
r0_ = achronal.survey_ray(0.0)
r3_ = achronal.survey_ray(0.3)
print("    achronal y0=0.0 geodesic INT T_kk dlambda = %+.6f  (C3 gives %+.6f)" % (r0_["anec"], aw0n))
print("    achronal y0=0.3 geodesic INT T_kk dlambda = %+.6f  (anec.py line %+.6f)" % (r3_["anec"], C["y=0.3"]["anec_py"]))
C["achronal_geodesic"] = {"0.0": r0_["anec"], "0.3": r3_["anec"]}

print("  C5 sign robustness of the coordinate-line integrals under the same positive weight")
for y in rays:
    print("    y=%.1f  INT T_kk/(1+v)^2 dx = %+.6f" % (y, affine_weighted(y)))
    C["y=%.1f" % y]["weighted"] = affine_weighted(y)

out["C"] = C
json.dump(out, open(os.path.join(HERE, "anec-definition.out.json"), "w"), indent=1, default=str)
print("\nwritten", os.path.join(HERE, "anec-definition.out.json"))
