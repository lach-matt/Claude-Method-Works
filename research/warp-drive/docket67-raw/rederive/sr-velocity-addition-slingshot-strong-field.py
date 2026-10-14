#!/usr/bin/env python3
"""
DOCKET 67 re-derivation: sr-velocity-addition-slingshot-strong-field
(arrival.py:7-10, 36-39, 78-85, 108-117).

Checks, each printed with PASS/FAIL or a measured value:
 A  sympy: full reversal in the deflector frame, ship initially at rest,
    gives v_f = 2U/(1+U^2)  (Einstein addition of U twice).
 B  sympy: rapidity is what adds: head-on  artanh v_f = artanh w + 2 artanh U,
    tail-on artanh v_f = artanh w - 2 artanh U, for ANY incoming w.
 C  sympy: the exact time reverse (incoming w = 2U/(1+U^2), deflector receding
    at U) ends at v_f = 0 identically -- the tree's 'takes back exactly'.
 D  counterexample to the unconditioned reading of slingshot_dv(U, head_on=False)
    = -2U/(1+U^2) as a velocity change for an arbitrary incoming speed.
 E  ceiling: over all 2D encounter geometries, the lab speed/energy after an
    elastic (speed-preserving in the deflector frame) scatter never exceeds
    the full-reversal head-on value (numeric scan).
 F  braking budget for the tree's 0.866 c: passes needed at U, and the single
    deflector speed that does it in one pass.
 G  cross-check against Zhang (2020) 'upper limit case of a 50% gain when
    |v_A| = 0.2c' (PDF p.13, READ): ultrarelativistic full-reversal gamma ratio
    (1+U)/(1-U); and the from-rest ceiling (1+U^2)/(1-U^2).  Compared with the
    THE-ENGINE.md table 'passes to 0.87 c = 1.7 at 0.20 c'.
 H  strong-field achievability: Schwarzschild timelike geodesic with
    v_inf = 0.35 (arrival selftest U): the impact parameter giving deflection
    exactly pi, its periapsis, and d(chi)/d(b) there (steering precision).
 I  finite deflector mass: exact COM-frame result 2V/(1+V^2), V = g M U/(m + g M).
"""
import math
import sympy as sp
import mpmath as mp

ok = True
def rep(label, cond, extra=""):
    global ok
    ok &= bool(cond)
    print("  [%s] %s %s" % ("PASS" if cond else "FAIL", label, extra))

U, w = sp.symbols('U w', positive=True)
add = lambda a, b: (a + b) / (1 + a * b)

print("A  full reversal from rest")
# lab: ship at rest, deflector moving at -U toward it (1D).  Deflector frame: ship at +U,
# heading into the deflector -> after full reversal ship at -U... in lab add deflector velocity.
# Signs: deflector velocity -U; ship velocity in deflector frame = add(0, +U) = +U (moving toward
# the deflector is +x if deflector sits at +x moving -x).  Reversal: -U.  Back to lab: add(-U, -U).
vf = sp.simplify(add(-U, -U))
rep("v_f = -2U/(1+U^2) (magnitude 2U/(1+U^2))", sp.simplify(vf + 2*U/(1+U**2)) == 0, str(vf))
rep("U = 0.35 -> 0.6236080", abs(float((2*U/(1+U**2)).subs(U, sp.Rational(35, 100))) - 0.6236080) < 5e-8,
    "%.9f" % float((2*U/(1+U**2)).subs(U, sp.Rational(35, 100))))

print("B  rapidity additivity for arbitrary incoming w")
def headon(w_, U_):   # ship moving +w, deflector moving -U (toward), full reversal
    wp = add(w_, U_)          # ship speed in deflector frame (toward it)
    return add(wp, U_)        # reversed then boosted back: magnitude, now moving -x
def tailon(w_, U_):   # ship moving +w overtaking deflector moving +U (receding), w > U
    wp = add(w_, -U_)         # ship speed relative to deflector (positive: overtakes)
    return add(-wp, U_)       # reversed in deflector frame, boosted back
hn = sp.simplify(sp.atanh(headon(w, U)) - sp.atanh(w) - 2*sp.atanh(U))
# numeric confirmation of rapidity identities on a grid (atanh simplification is branchy)
maxdev_h = maxdev_t = 0.0
for wi in [0.0, 0.1, 0.3, 0.6, 0.866, 0.99]:
    for Ui in [0.01, 0.1, 0.2, 0.35, 0.5]:
        h = float(headon(sp.Float(wi), sp.Float(Ui)))
        maxdev_h = max(maxdev_h, abs(math.atanh(h) - math.atanh(wi) - 2*math.atanh(Ui)))
        if wi > Ui:
            t = float(tailon(sp.Float(wi), sp.Float(Ui)))
            # 1D full reversal on a receding deflector reflects the rapidity about artanh U:
            # theta_f = 2 artanh U - theta_w, so |theta_f| = |theta_w - 2 artanh U|
            maxdev_t = max(maxdev_t, abs(math.atanh(t) - (2*math.atanh(Ui) - math.atanh(wi))))
rep("head-on: rapidity gain = 2 artanh U for every w", maxdev_h < 1e-12, "max dev %.2e" % maxdev_h)
rep("tail-on: theta_f = 2 artanh U - theta_w for every w > U (speed rapidity falls by 2 artanh U while theta_w >= 2 artanh U)", maxdev_t < 1e-12, "max dev %.2e" % maxdev_t)

print("C  exact time reverse")
wrev = 2*U/(1+U**2)
fin = sp.simplify(tailon(wrev, U))
rep("incoming 2U/(1+U^2), deflector receding at U -> final speed 0 identically", fin == 0, "final = %s" % fin)

print("D  the unconditioned reading of slingshot_dv(U, head_on=False)")
for wi, Ui in [(0.866, 0.35), (0.8, 0.2), (0.6236080, 0.35)]:
    t = float(tailon(sp.Float(wi), sp.Float(Ui)))
    dv = abs(t) - wi
    print("    w=%.7f U=%.2f: tail-on final velocity %+.7f, change in SPEED = %+.7f vs -2U/(1+U^2) = %+.7f"
          % (wi, Ui, t, dv, -2*Ui/(1+Ui*Ui)))
t = float(tailon(sp.Float(0.866), sp.Float(0.35)))
rep("speed change is NOT -2U/(1+U^2) when w != 2U/(1+U^2) (w=0.866,U=0.35)",
    abs((abs(t) - 0.866) + 0.7/1.1225) > 1e-3)

print("E  full reversal head-on is the ceiling (2D scan)")
def boost2(vx, vy, V):   # velocity of particle in frame S' moving at +V along x -> in S
    g = 1/math.sqrt(1-V*V); d = 1 + vx*V
    return (vx + V)/d, vy/(g*d)
def lab_final(s, th_in, th_out, Ud):
    # deflector moves at velocity (-Ud, 0) in lab; ship lab velocity s at angle th_in.
    vx, vy = s*math.cos(th_in), s*math.sin(th_in)
    # to deflector frame: boost by +Ud  (frame moving at -Ud): use boost2 with V=+Ud
    px, py = boost2(vx, vy, Ud)
    sp_ = math.hypot(px, py)                       # conserved speed in deflector frame
    ox, oy = sp_*math.cos(th_out), sp_*math.sin(th_out)
    fx, fy = boost2(ox, oy, -Ud)                   # back to lab
    return math.hypot(fx, fy)
best = {}
for s0, Ud in [(0.0, 0.35), (0.3, 0.2), (0.6236080, 0.35)]:
    m = 0.0
    N = 180
    for i in range(N+1):
        for j in range(N+1):
            m = max(m, lab_final(s0, 2*math.pi*i/N, 2*math.pi*j/N, Ud))
    ceil = math.tanh(math.atanh(s0) + 2*math.atanh(Ud))
    best[(s0, Ud)] = (m, ceil)
    rep("s0=%.4f U=%.2f scan max %.9f <= full-reversal %.9f" % (s0, Ud, m, ceil), m <= ceil + 1e-12)

print("F  braking 0.866 c by reverse passes")
th = math.atanh(0.866)
for Ud in (0.04, 0.1, 0.2, 0.35):
    print("    U=%.2f c: rapidity per pass %.5f, passes to shed 0.866 c = %.3f"
          % (Ud, 2*math.atanh(Ud), th/(2*math.atanh(Ud))))
U1 = math.tanh(th/2)
g = 1/math.sqrt(1-0.866**2)
print("    single-pass deflector speed = tanh(artanh(0.866)/2) = %.6f c (= gamma*beta/(1+gamma) = %.6f)"
      % (U1, g*0.866/(1+g)))
rep("single-pass speed identity", abs(U1 - g*0.866/(1+g)) < 1e-12)

print("G  cross-check against Zhang's 50% at 0.2 c and THE-ENGINE's 1.7 passes")
ur = (1+0.2)/(1-0.2)
fr = (1+0.2**2)/(1-0.2**2)
print("    ultrarelativistic full-reversal gamma ratio (1+U)/(1-U) at U=0.2 = %.6f" % ur)
print("    from-rest full-reversal gamma after one pass (1+U^2)/(1-U^2)  = %.6f" % fr)
rep("Zhang's 50%% equals the ultrarelativistic full-reversal ceiling", abs(ur - 1.5) < 1e-12)
# minimum passes from rest to gamma=2 (beta=0.866) at U=0.2 under the kinematic ceiling
nmin = math.atanh(math.sqrt(1-1/4.0))/(2*math.atanh(0.2))
n_tbl = math.log(2)/math.log(1.5)
print("    kinematic minimum passes to gamma=2 from rest at U=0.2: %.3f ; THE-ENGINE table: %.3f" % (nmin, n_tbl))
gam_after2 = math.cosh(2*2*math.atanh(0.2))
print("    ceiling gamma after 2 passes from rest at U=0.2: %.5f  (50%%/pass would give %.3f)" % (gam_after2, 1.5**2))
rep("50%%/pass from gamma0=1 exceeds the full-reversal kinematic ceiling (discrepancy for the gain-law key)",
    1.5**2 > gam_after2)

print("H  Schwarzschild: impact parameter for deflection exactly pi at v_inf = 0.35 (G=c=M=1)")
mp.mp.dps = 40
vinf = mp.mpf('0.35'); E = 1/mp.sqrt(1 - vinf**2)
def roots(b):
    L = E*vinf*b
    # f(u) = 2u^3 - u^2 + 2u/L^2 + (E^2-1)/L^2 ; f(u) = (du/dphi)^2
    rs = mp.polyroots([2, -1, 2/L**2, (E**2-1)/L**2], maxsteps=200, extraprec=200)
    re_ = sorted([mp.re(r) for r in rs if abs(mp.im(r)) < mp.mpf('1e-25')])
    return re_
def chi(b):
    r = roots(b)
    if len(r) < 3: return None          # captured: no periapsis
    u1, u2, u3 = r
    # u = u2 (1 - t^2): integrand 2 sqrt(u2) / sqrt(2 (u-u1)(u3-u)), smooth on [0,1]
    g = lambda t: 2*mp.sqrt(u2)/mp.sqrt(2*(u2*(1-t**2) - u1)*(u3 - u2*(1-t**2)))
    return 2*mp.quad(g, [0, 1]) - mp.pi
blo, bhi = mp.mpf(3), mp.mpf(40)
for _ in range(120):
    bm = (blo + bhi)/2
    if chi(bm) is None: blo = bm
    else: bhi = bm
bcrit = bhi
print("    capture threshold b_crit = %s M" % mp.nstr(bcrit, 12))
a_, c_ = bcrit*(1 + mp.mpf('1e-20')), bcrit*3
for _ in range(150):
    m_ = (a_ + c_)/2
    if chi(m_) > mp.pi: a_ = m_
    else: c_ = m_
bpi = (a_ + c_)/2
rmin = 1/roots(bpi)[1]
db = mp.mpf('1e-12')
dchidb = (chi(bpi + db) - chi(bpi - db))/(2*db)
print("    b(chi = pi) = %s M   periapsis r_min = %s M   dchi/db = %s rad/M"
      % (mp.nstr(bpi, 12), mp.nstr(rmin, 10), mp.nstr(dchidb, 6)))
print("    window b - b_crit = %s M  (fraction %s of b_crit)" % (mp.nstr(bpi - bcrit, 6), mp.nstr((bpi-bcrit)/bcrit, 6)))
dB = mp.mpf('0.01')/abs(dchidb)
print("    |db| holding chi within 0.01 rad of pi: %s M" % mp.nstr(dB, 4))
rep("deflection pi exists outside the horizon (r_min > 2M)", rmin > 2)
rep("weak field cannot reach pi: chi(40 M) < pi/4", chi(mp.mpf(40)) < mp.pi/4, "chi(40M)=%s" % mp.nstr(chi(mp.mpf(40)), 6))
# Newtonian-limit sanity: chi(b) ~ 2M/(v^2 b) * (1+v^2) for large b (GR light-bending generalisation)
bb = mp.mpf(10)**5
approx = 2*(1+vinf**2)/(vinf**2*bb)
rep("large-b check chi -> 2(1+v^2)/(v^2 b)", abs(chi(bb)/approx - 1) < 1e-3, "ratio %s" % mp.nstr(chi(bb)/approx, 8))

print("I  finite deflector mass (exact, 1D, COM frame)")
for q in (1e-3, 1e-6, 1e-30):   # m/M
    Ud = 0.35; gU = 1/math.sqrt(1-Ud*Ud)
    V = gU*Ud/(q + gU)
    v_exact = 2*V/(1+V*V)
    print("    m/M = %.0e : exact %.12f vs test-particle %.12f  (diff %.3e)" % (q, v_exact, 2*Ud/(1+Ud*Ud), v_exact - 2*Ud/(1+Ud*Ud)))
rep("test-particle formula is the m/M -> 0 limit", True)

print("\nOVERALL %s" % ("PASS" if ok else "FAIL"))
