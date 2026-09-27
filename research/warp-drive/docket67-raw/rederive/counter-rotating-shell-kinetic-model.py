#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation for key counter-rotating-shell-kinetic-model
(wall.py:75-107 prose, 397-436 code, 592-615 selftest; designpoint.py:160-161).

The tree marks the model RECONSTRUCTED ("no member or paper states it in this
form").  No source for it could be read in this stage (alphaXiv quota exhausted,
arxiv.org / export.arxiv.org / alphaxiv.org / inspirehep.net 403 at the egress
proxy).  Everything the model claims is finite or closed-form, so it is
re-derived here from first principles, independently of wall.py's code:

 K1  2D isotropic single-speed gas: sigma = n m gamma, p = n m gamma v^2/2.
 K2  junction (Lanczos, Minkowski in / Schwarzschild out): p0/sigma0 = (1-s)/(4s),
     so v^2 = (1-s)/(2s), v = 1 exactly at x = 8/9 (= Andreasson/Buchdahl-type
     Einstein-Vlasov compactness bound with p + 2p_T <= rho, READ-VIA-RESTATEMENT
     in Dadhich arXiv:2504.00064v2 p.7).
 K3  angular momentum conservation u = gamma v = L/R, and the resulting beta^2
     formula u^2(3u^2+4)/(2(1+u^2)(3u^2+2)); its limits 1/2 and ~u^2.
 K4  the Vlasov EOS obeys the Israel conservation law d(sigma A) + p dA = 0
     identically (so treating it as a barotropic surface fluid is consistent).
 K5  INDEPENDENT stability test: the exact shell equation of motion
     M = mu(R) sqrt(1+Rdot^2) - mu(R)^2/(2R), mu = N m sqrt(1+L^2/R^2), with no
     use of beta^2_crit; the V''=0 compactness is found directly and compared
     with wall.py's crossover 0.46897656.
 K6  wall.py's table values (x = 0.3, 0.4, 2/3, 4/5), margin 1.144557648,
     the 4/3 limit, and the minimal polynomial of the crossover in s.
 K7  SENSITIVITY TO THE SINGLE-SPEED HYPOTHESIS: the same statics carried by a
     spread of speeds (the thin limit of an Einstein cluster, and two-speed
     mixtures), each particle conserving its own L.  Low-x margin 4/3 is
     distribution-independent; the crossover is not.
"""
import math
import sympy as sp
import sys, os

ok = True
def chk(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

x, s, u, v, R, L, th, Nm = sp.symbols('x s u v R L theta N_m', positive=True)

# ---- K1 -------------------------------------------------------------------
avg = sp.integrate(sp.cos(th)**2, (th, 0, 2 * sp.pi)) / (2 * sp.pi)
chk("K1 isotropic 2D average <v_a v_b> = (v^2/2) delta_ab  (<cos^2> = 1/2)", avg == sp.Rational(1, 2))
# T^ab = n m gamma v^a v^b summed: p = n m gamma v^2 <cos^2>; sigma = n m gamma
chk("K1 p/sigma = v^2/2", sp.simplify((v**2 * avg) - v**2 / 2) == 0)

# ---- K2 -------------------------------------------------------------------
Mx = x * R / 2
S = sp.sqrt(1 - x)
sig_L = (1 - S) / (4 * sp.pi * R)
p_L = ((1 - Mx / R) / S - 1) / (8 * sp.pi * R)   # Lanczos flat-in / Schw-out, static
ps = sp.simplify((p_L / sig_L).subs(x, 1 - s**2))
chk("K2 junction p0/sigma0 = (1-s)/(4s)", sp.simplify(ps - (1 - s) / (4 * s)) == 0)
v2x = 2 * (1 - s) / (4 * s)
sol = sp.solve(sp.Eq(v2x, 1), s)
chk("K2 v = 1 at x = 8/9 exactly", [sp.nsimplify(1 - q**2) for q in sol] == [sp.Rational(8, 9)])
chk("K2 small-x: v^2 ~ x/4 = M/(2R) (half the Newtonian test-orbit value, self-gravity averaged)",
    sp.limit(v2x.subs(s, sp.sqrt(1 - x)) / x, x, 0) == sp.Rational(1, 4))

# ---- K3 -------------------------------------------------------------------
# per unit rest mass, N particles, u = L/R; sigma = N m sqrt(1+u^2)/(4 pi R^2), p = N m u^2/(2 sqrt(1+u^2) 4 pi R^2)
uR = L / R
sig = Nm * sp.sqrt(1 + uR**2) / (4 * sp.pi * R**2)
p = Nm * uR**2 / (2 * sp.sqrt(1 + uR**2)) / (4 * sp.pi * R**2)
chk("K3 p/sigma = v^2/2 with v^2 = u^2/(1+u^2)", sp.simplify(p / sig - (uR**2 / (1 + uR**2)) / 2) == 0)
b2 = sp.simplify(sp.diff(p, R) / sp.diff(sig, R))
b2u = sp.simplify(b2.subs(L, u * R))
tree_b2 = u**2 * (3 * u**2 + 4) / (2 * (1 + u**2) * (3 * u**2 + 2))
chk("K3 beta^2 = u^2(3u^2+4)/(2(1+u^2)(3u^2+2))  [wall.py:86]", sp.simplify(b2u - tree_b2) == 0)
chk("K3 ceiling 1/2 as u -> oo", sp.limit(tree_b2, u, sp.oo) == sp.Rational(1, 2))
chk("K3 beta^2 ~ u^2 as u -> 0 (Newtonian Gamma = 2 of a 2D gas)", sp.limit(tree_b2 / u**2, u, 0) == 1)
chk("K3 beta^2 < 1/2 < 1 for all u (subluminal)", sp.simplify(sp.Rational(1, 2) - tree_b2).factor() is not None
    and all(float(tree_b2.subs(u, t)) < 0.5 for t in (0.01, 0.5, 1, 3, 30, 1e4)))

# ---- K4 -------------------------------------------------------------------
A = 4 * sp.pi * R**2
cons = sp.simplify(sp.diff(sig * A, R) + p * sp.diff(A, R))
chk("K4 d(sigma A)/dR + p dA/dR = 0 identically (Israel conservation holds)", cons == 0)

# ---- K5 independent stability via exact equation of motion ----------------
# Flat interior, Schwarzschild exterior mass M: M = mu sqrt(1+Rdot^2) - mu^2/(2R).
# Rdot^2 = g^2 - 1, g = (M + mu^2/(2R))/mu ; V = 1 - g^2 ; at equilibrium g=1 so V'' = -2 g''.
Msym = sp.symbols('M', positive=True)
mu = Nm * sp.sqrt(1 + L**2 / R**2)
g = (Msym + mu**2 / (2 * R)) / mu
g1 = sp.diff(g, R); g2 = sp.diff(g, R, 2)
def equilibrium(xval):
    """Given x = 2M/R0 at R0 = 1, Nm = 1, solve g = 1, g' = 0 for (M, L)."""
    subs0 = {R: 1, Nm: 1}
    Mv = xval / 2
    # g=1 -> M = mu - mu^2/2 ; with M = x/2 fixed, solve for L then check g'=0 gives x consistency
    # Solve both numerically for (Nm free) instead: fix Nm=1 unknown M,L with x given -> 2 eqs 2 unknowns, but x fixes M/R0.
    # So free unknowns are (Nm, L) with M = x/2, R0 = 1.
    eqs = [sp.Eq(g.subs({R: 1, Msym: Mv}), 1), sp.Eq(g1.subs({R: 1, Msym: Mv}), 0)]
    s_ = math.sqrt(1 - xval)
    v2 = (1 - s_) / (2 * s_)
    L0 = math.sqrt(v2 / (1 - v2))
    N0 = (1 - s_) / math.sqrt(1 + L0**2)
    solv = sp.nsolve([e.lhs - e.rhs for e in eqs], [Nm, L], [N0, L0], prec=30)
    return Mv, float(solv[0]), float(solv[1])
def Vpp(xval):
    Mv, Nv, Lv = equilibrium(xval)
    return float(-2 * g2.subs({R: 1, Msym: Mv, Nm: Nv, L: Lv})), Nv, Lv

# check the equilibrium matches the junction statics (sigma0 = (1-s)/(4 pi), u0^2 = v^2/(1-v^2))
for xv_ in (0.1, 0.3, 0.6):
    Mv, Nv, Lv = equilibrium(xv_)
    s_ = math.sqrt(1 - xv_); v2 = (1 - s_) / (2 * s_)
    chk("K5 EOM equilibrium at x=%.1f reproduces junction statics: u0^2 = v^2/(1-v^2)" % xv_,
        abs(Lv**2 - v2 / (1 - v2)) < 1e-12)

def bisect(f, lo, hi, n=100):
    flo = f(lo)
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return 0.5 * (lo + hi)
xc_eom = bisect(lambda z: Vpp(z)[0], 0.3, 0.6, 60)
print("      EOM (no beta^2_crit used): V''=0 at x = %.10f" % xc_eom)
chk("K5 independent EOM crossover == wall.py 0.46897656 (1e-6)", abs(xc_eom - 0.46897656) < 1e-6)
chk("K5 stable (V''>0) below: x=0.3", Vpp(0.3)[0] > 0)
chk("K5 unstable (V''<0) above: x=2/3, 4/5", Vpp(2 / 3)[0] < 0 and Vpp(0.8)[0] < 0)

# ---- K6 the tree's numbers --------------------------------------------------
def b2crit(xv_):
    s_ = math.sqrt(1 - xv_)
    return (1 - s_) * (3 * s_**2 + 2 * s_ + 1) / (4 * s_**2 * (1 + 3 * s_))
def b2v(xv_):
    s_ = math.sqrt(1 - xv_)
    v2 = (xv_ / (1 + s_)) / (2 * s_)
    u2 = v2 / (1 - v2)
    return u2 * (3 * u2 + 4) / (2 * (1 + u2) * (3 * u2 + 2))
table = {0.3: (0.090800, 0.079332), 0.4: (0.130697, 0.122892), 2 / 3: (0.281089, 0.366025), 0.8: (0.399187, 0.736068)}
for xv_, (a, b) in table.items():
    chk("K6 wall.py:89-93 x=%.4f supplied %.6f required %.6f" % (xv_, a, b),
        abs(b2v(xv_) - a) < 6e-7 and abs(b2crit(xv_) - b) < 6e-7)
chk("K6 margin at x=0.3 = 1.144557648", abs(b2v(0.3) / b2crit(0.3) - 1.144557648) < 1e-8)
chk("K6 margin -> 4/3 as x -> 0", abs(b2v(1e-9) / b2crit(1e-9) - 4 / 3) < 1e-6)
# closed-form crossover: beta2_vlasov(s) = beta2_crit(s)
v2s = (1 - s) / (2 * s)
u2s = sp.simplify(v2s / (1 - v2s))
bvs = sp.simplify((u**2 * (3 * u**2 + 4) / (2 * (1 + u**2) * (3 * u**2 + 2))).subs(u**2, u2s))
bcs = (1 - s) * (3 * s**2 + 2 * s + 1) / (4 * s**2 * (1 + 3 * s))
num = sp.factor(sp.numer(sp.together(bvs - bcs)))
print("      numerator of beta2_vlasov - beta2_crit in s:", num)
roots = [r for r in sp.Poly(sp.numer(sp.together(bvs - bcs)), s).nroots() if abs(sp.im(r)) < 1e-14 and 1/3 < sp.re(r) < 1]
xs_ = sorted(float(1 - sp.re(r)**2) for r in roots)
print("      real roots in s in (1/3,1) -> x =", xs_)
chk("K6 the crossover is an algebraic root; one crossing in (0, 8/9) at 0.468976...",
    len([z for z in xs_ if 0 < z < 8 / 9]) == 1 and abs(xs_[0] - 0.46897656) < 1e-7)


xc_exact = (17 - sp.sqrt(33)) / 24
chk("K6 crossover in closed form: 6s^2-3s-1 = 0, s = (3+sqrt33)/12, x = (17 - sqrt33)/24",
    sp.simplify(1 - ((3 + sp.sqrt(33)) / 12)**2 - xc_exact) == 0 and abs(float(xc_exact) - 0.46897656) < 1e-8)
print("      x_c = (17 - sqrt33)/24 = %.15f" % float(xc_exact))

# ---- K7 single-speed hypothesis ------------------------------------------------
# A shell of rest-mass weights w_i with speeds u_i (gamma v) at R0 = 1; each conserves L_i: u_i(R) = u_i/R.
def beta2_mix(ws, us):
    def sig(Rv): return sum(w * math.sqrt(1 + (uu / Rv)**2) for w, uu in zip(ws, us)) / Rv**2
    def pp(Rv): return sum(w * (uu / Rv)**2 / (2 * math.sqrt(1 + (uu / Rv)**2)) for w, uu in zip(ws, us)) / Rv**2
    h = 1e-6
    return (pp(1 + h) - pp(1 - h)) / (sig(1 + h) - sig(1 - h))
def ratio_p_sigma(ws, us):
    E = sum(w * math.sqrt(1 + uu * uu) for w, uu in zip(ws, us))
    P = sum(w * uu * uu / (2 * math.sqrt(1 + uu * uu)) for w, uu in zip(ws, us))
    return P / E
# (a) thin limit of an Einstein cluster: layer variable q = 2m/R in [0, x]; energy weight dq/sqrt(1-q);
#     circular-orbit speed v^2(q) = q/(2(1-q)); rest-mass weight = energy weight / gamma.
def cluster(xv_, n=4000):
    ws, us = [], []
    for k in range(n):
        q = (k + 0.5) / n * xv_
        v2 = q / (2 * (1 - q))
        if v2 >= 1: return None
        gam = 1 / math.sqrt(1 - v2)
        ws.append((xv_ / n) / math.sqrt(1 - q) / gam)
        us.append(gam * math.sqrt(v2))
    return ws, us
for xv_ in (0.1, 0.3, 0.5):
    ws, us = cluster(xv_)
    s_ = math.sqrt(1 - xv_)
    chk("K7a thin-cluster spread has the SAME statics p0/sigma0 = (1-s)/(4s) at x=%.1f" % xv_,
        abs(ratio_p_sigma(ws, us) - (1 - s_) / (4 * s_)) < 2e-6)
def cl_margin(xv_):
    c = cluster(xv_)
    return None if c is None else beta2_mix(*c) / b2crit(xv_)
chk("K7a thin-cluster spread margin -> 4/3 as x -> 0 (its speeds are non-relativistic there too)",
    abs(cl_margin(1e-4) - 4 / 3) < 1e-3)
xc_cl = bisect(lambda z: cl_margin(z) - 1, 0.05, 0.66, 50)
print("      thin-Einstein-cluster spread (expires at x = 2/3): crossover x = %.6f; margin at 0.3 = %.6f"
      % (xc_cl, cl_margin(0.3)))
print("      single-speed (wall.py):                           crossover x = 0.468977; margin at 0.3 = %.6f"
      % (b2v(0.3) / b2crit(0.3)))
chk("K7a crossover MOVES with the speed distribution (|dx| > 1e-3)", abs(xc_cl - 0.46897656) > 1e-3)
# (b) two-speed mixtures at the same statics: equal rest-mass halves, speeds chosen to match p0/sigma0
def two_speed(xv_, spread):
    s_ = math.sqrt(1 - xv_); target = (1 - s_) / (4 * s_)
    # u_a = c(1-spread), u_b = c(1+spread); solve c
    lo, hi = 1e-9, 50.0
    for _ in range(200):
        c = 0.5 * (lo + hi)
        if ratio_p_sigma([0.5, 0.5], [c * (1 - spread), c * (1 + spread)]) < target: lo = c
        else: hi = c
    return [0.5, 0.5], [c * (1 - spread), c * (1 + spread)]
for sp_ in (0.0, 0.5, 0.9):
    xc2 = bisect(lambda z: beta2_mix(*two_speed(z, sp_)) / b2crit(z) - 1, 0.05, 0.85, 50)
    print("      two-speed mixture, spread %.1f: crossover x = %.6f" % (sp_, xc2))
    if sp_ == 0.0:
        chk("K7b zero spread reproduces wall.py crossover", abs(xc2 - 0.46897656) < 1e-5)

# (c) extreme two-population shells: rest-mass fraction f at rest (u=0), the rest at one speed, same statics.
#     NOT a realizable collisionless thin shell of individually orbiting particles (a particle at rest on a
#     thin shell has no centrifugal support); reported only to show which hypothesis carries the 4/3 limit.
def rest_plus_fast(xv_, f):
    s_ = math.sqrt(1 - xv_); target = (1 - s_) / (4 * s_)
    lo, hi = 1e-9, 1e6
    for _ in range(300):
        c = math.sqrt(lo * hi)
        if ratio_p_sigma([f, 1 - f], [0.0, c]) < target: lo = c
        else: hi = c
    return [f, 1 - f], [0.0, c]
for f in (0.0, 0.5, 0.9, 0.99, 0.999):
    m03 = beta2_mix(*rest_plus_fast(0.3, f)) / b2crit(0.3)
    m16 = beta2_mix(*rest_plus_fast(1 / 6, f)) / b2crit(1 / 6)
    m001 = beta2_mix(*rest_plus_fast(1e-3, f)) / b2crit(1e-3)
    print("      rest fraction %.3f: margin at x=1e-3 %.5f ; x=1/6 %.5f ; x=0.3 %.5f" % (f, m001, m16, m03))
m_lo = beta2_mix(*rest_plus_fast(1e-6, 0.999)) / b2crit(1e-6)
print("      rest fraction 0.999 at x = 1e-6: margin %.5f" % m_lo)
chk("K7c even the extreme mixture tends to 4/3 as x -> 0 (every component becomes non-relativistic)",
    abs(m_lo - 4 / 3) < 1e-3)
xc99 = bisect(lambda z: beta2_mix(*rest_plus_fast(z, 0.99)) / b2crit(z) - 1, 0.01, 0.3, 50)
print("      rest fraction 0.99: crossover x = %.6f (vs 0.468977 single-speed)" % xc99)
chk("K7c but the CROSSOVER is not bounded below by 0.469 outside the single-speed class (f=0.99 -> < 0.1)",
    xc99 < 0.1)

print("\nALL PASS" if ok else "\nSOME FAIL")
sys.exit(0 if ok else 1)
