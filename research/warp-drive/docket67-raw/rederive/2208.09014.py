#!/usr/bin/env python3
r"""
DOCKET 67 re-derivation for arXiv:2208.09014 (Greene, Kabat, Levin, Porrati,
"Back to the Future: Causality on a Moving Braneworld").

THE SOURCE WAS NOT READABLE IN THIS STAGE (alphaXiv quota exceeded on every
call; arxiv.org refused by the egress proxy, 403).  Nothing below is a reading
of GKLP.  What is checked is the PHYSICS the tree attributes to them, derived
here from first principles under hypotheses named in this file:

  G1  bulk = 5D Minkowski R^{1,3} x R_y quotiented by y ~ y + 2 pi R (M4 x S1);
  G2  an UNWRAPPED flat 3-brane at y = beta t, extended along x1..x3, 0<beta<1
      (the brane "moving through the compact dimension");
  G3  brane observers use the induced metric; a second observer is boosted by
      B along x (brane Lorentz boost);
  G4  (commutator) a FREE scalar field in the bulk, commutator by the method of
      images; massless unless stated.

Checks
  C1  |xi|^2 = (2 pi R)^2 in bulk, brane-rest and boosted frames: spacelike, so
      the rank-1 lattice has no causal vector (D21's 'forced' premise).
  C2  induced metric of G2 is -(dt/gamma)^2 + dx^2 (flat 4D Minkowski).
  C3  EXACT WITNESS (beta=3/5, 2 pi R=1): a brane pair that the induced metric
      calls spacelike, whose n=-1 bulk image is strictly timelike (D13 part 1).
  C4  z3: every bulk-causal image gives brane-frame speed <= gamma (bound), and
      the bound is attained -- superluminal by exactly gamma > 1.
  C5  5D free-field commutator interior kernel, derived by the dimensional
      recursion G_{D+2} = (1/pi) d/ds G_D from G_3: massless interior is
      -(1/4pi^2) s^{-3/2} (single sign); massive interior is
      -(1/4pi^2)[cos(mu)+mu sin(mu)]/u^3, u = sqrt(s), which HAS ZEROS.
  C6  image sum at the C3 witness (massless): every image either spacelike
      (contributes 0) or strictly timelike (same sign): non-zero (D13 part 2).
      No image is null at the witness.
  C7  brane-observer velocity addition: forward speed gamma seen from boost B
      is (gamma - B)/(1 - B gamma); pole at B = 1/gamma  <=>  Gamma = 1/beta
      (W7's supercriticality threshold).  Round trip at B=0 stays positive.
  C8  DATA: d = 7.0e-16 (GW170817 upper bound on (v_gw-c)/c) -> beta, 1/beta at
      50 digits; W7's ratio 2.6726124e7 / 1.894565e6.
"""
import sys
import sympy as sp
import mpmath as mp
import z3

mp.mp.dps = 50
ok_all = True
def chk(name, cond):
    global ok_all
    ok_all &= bool(cond)
    print(("  OK   " if cond else "  FAIL ") + name)

beta, B, R = sp.symbols('beta B R', positive=True)
g = 1/sp.sqrt(1-beta**2)
G = 1/sp.sqrt(1-B**2)
L = 2*sp.pi*R
def nrm(v):  # signature (-,+,+,+) on (t, x, y) with extra dims suppressed
    return -v[0]**2 + sum(c**2 for c in v[1:])

print("C1  identification vector")
xi_bulk = [0, 0, L]                      # (t, x, y)
# brane rest frame: boost by beta along y
xi_rest = [-g*beta*L, 0, g*L]
# further boost by B along x (brane boost)
xi_boost = [-G*g*beta*L, G*B*g*beta*L, g*L]
for nm, v in (("bulk", xi_bulk), ("brane rest", xi_rest), ("boosted", xi_boost)):
    chk("|xi|^2 = (2 pi R)^2 in %s frame" % nm, sp.simplify(nrm(v) - L**2) == 0)

print("C2  induced metric on y = beta t")
t, x = sp.symbols('t x', real=True)
# embedding (t, x, y=beta t): pullback of -dt^2+dx^2+dy^2
gtt = -1 + beta**2
chk("g_tt(induced) = -1/gamma^2", sp.simplify(gtt + 1/g**2) == 0)

print("C3  exact witness, beta = 3/5, 2 pi R = 1")
b0 = sp.Rational(3, 5); g0 = 1/sp.sqrt(1-b0**2); Lw = sp.Integer(1)
chk("gamma = 5/4 exactly", g0 == sp.Rational(5, 4))
Dt = Lw/b0                     # brane returns to the same y after one period
Dx = sp.Rational(3, 2)         # between Dt/gamma = 4/3 and Dt = 5/3
induced = -(Dt/g0)**2 + Dx**2
bulk_n = lambda n: -Dt**2 + Dx**2 + (b0*Dt + n*Lw)**2
print("     Dt = %s, Dx = %s, induced norm = %s, bulk image n=-1 norm = %s"
      % (Dt, Dx, induced, bulk_n(-1)))
chk("induced norm > 0 (brane calls the pair SPACELIKE)", induced > 0)
chk("bulk n=-1 image norm < 0 (STRICTLY TIMELIKE)", bulk_n(-1) < 0)
chk("n=0 bulk image spacelike", bulk_n(0) > 0)

print("C4  z3: brane-frame speed bound is exactly gamma")
s = z3.Solver()
bz, gz, Tz, Xz, Yz = z3.Reals('b g T X Y')
# gamma^2 (1 - b^2) = 1; image causal: T^2 >= X^2 + Y^2, T > 0
# brane-frame speed = |X| / (T/gamma) ; claim |X| gamma / T <= gamma  i.e. X^2 <= T^2
s.add(bz > 0, bz < 1, gz > 1, gz*gz*(1-bz*bz) == 1, Tz > 0,
      Tz*Tz >= Xz*Xz + Yz*Yz, (Xz*gz)*(Xz*gz) > (gz*Tz)*(gz*Tz))
r = s.check()
chk("no causal image exceeds brane speed gamma (z3 %s)" % r, r == z3.unsat)
s2 = z3.Solver()
s2.add(bz > 0, bz < 1, gz > 1, gz*gz*(1-bz*bz) == 1, Tz > 0, Yz == 0,
       Xz == Tz)       # null image with Y=0: speed attained = gamma
r2 = s2.check()
chk("speed gamma > 1 attained by a null image at Dy = 0 (z3 %s)" % r2, r2 == z3.sat)

print("C5  5D free-field retarded kernel, interior of the cone")
sv, m, u = sp.symbols('s m u', positive=True)
G3_massive = sp.cos(m*sp.sqrt(sv))/(2*sp.pi*sp.sqrt(sv))
G3_massless = 1/(2*sp.pi*sp.sqrt(sv))
G5_massive = sp.simplify(sp.diff(G3_massive, sv)/sp.pi)
G5_massless = sp.simplify(sp.diff(G3_massless, sv)/sp.pi)
chk("massless: G5 interior = -(1/4 pi^2) s^(-3/2)",
    sp.simplify(G5_massless + 1/(4*sp.pi**2*sv**sp.Rational(3, 2))) == 0)
target = -(sp.cos(m*u) + m*u*sp.sin(m*u))/(4*sp.pi**2*u**3)
chk("massive: G5 interior = -(1/4pi^2)[cos(mu)+mu sin(mu)]/u^3",
    sp.simplify(G5_massive.subs(sv, u**2) - target) == 0)
chk("massive -> massless as m -> 0", sp.limit(target, m, 0) ==
    sp.simplify(G5_massless.subs(sv, u**2)))
z1 = mp.findroot(lambda X: mp.cos(X) + X*mp.sin(X), 2.8)
print("     first zero of cos X + X sin X: X = %s" % mp.nstr(z1, 12))
chk("massive 5D interior kernel has a zero (m sqrt(s) = %.6f)" % float(z1),
    abs(mp.cos(z1) + z1*mp.sin(z1)) < 1e-20)
# check the 3D seed against the known massless 3D retarded function
# G3 = theta(t - r)/(2 pi sqrt(t^2 - r^2)): standard; recursion:
# G_{D+2}(s) = -(1/(2 pi r)) d/dr G_D = (1/pi) d/ds G_D since d/dr = -2r d/ds.
rr, tt = sp.symbols('r t', positive=True)
chk("recursion identity -(1/2 pi r) d_r f(t^2-r^2) == (1/pi) f'(s)",
    sp.simplify(-(1/(2*sp.pi*rr))*sp.diff(G3_massless.subs(sv, tt**2-rr**2), rr)
                - G5_massless.subs(sv, tt**2-rr**2)) == 0)

print("C6  image sum at the witness (massless bulk scalar)")
tot = mp.mpf(0); timelike = []; null = []
for n in range(-50, 51):
    sn = -bulk_n(n)          # s = t^2 - r^2
    if sn > 0:
        timelike.append((n, sn))
        tot += -1/(4*mp.pi**2*mp.mpf(sp.N(sn, 40))**1.5)
    elif sn == 0:
        null.append(n)
print("     timelike images:", timelike, " null images:", null)
print("     interior image sum (Dt>0) = %s" % mp.nstr(tot, 15))
chk("no null image at the witness (distributional terms absent)", not null)
chk("commutator non-zero across an induced-spacelike brane pair", tot != 0)

print("C7  brane-observer kinematics")
v = (g - B)/(1 - B*g)          # relativistic addition of speed gamma and boost -B
# pole
chk("pole of (gamma-B)/(1-B gamma) at B = 1/gamma",
    sp.simplify((1 - B*g).subs(B, 1/g)) == 0)
chk("B = 1/gamma  <=>  Gamma = 1/beta",
    sp.simplify((1/sp.sqrt(1-(1/g)**2)) - 1/beta) == 0)
# out-and-back at B=0: forward speed gamma, backward speed gamma (no brane boost)
chk("B = 0 forward speed = gamma", sp.simplify(v.subs(B, 0) - g) == 0)

print("C8  data")
mp.mp.dps = 50
d = mp.mpf('7.0e-16')
b_max = mp.sqrt(d*(2+d))/(1+d)
print("     beta_max = %s   1/beta = %s" % (mp.nstr(b_max, 12), mp.nstr(1/b_max, 12)))
chk("beta_max = 3.741657e-08 (branelink.BETA_MAX, 7 digits)",
    mp.nstr(b_max, 7) == '3.741657e-8')
chk("1/beta = 2.6726124e7 (W7, 8 digits)", mp.nstr(1/b_max, 8) == '26726124.0')
ratio = mp.mpf('2.6726124e7')/mp.mpf('1.894565e6')
print("     W7 ratio 1/beta / Gamma = %s" % mp.nstr(ratio, 6))
chk("W7 factor 14.1 and Gamma = 1.894565e6 is SUBcritical",
    mp.nstr(ratio, 3) == '14.1' and mp.mpf('1.894565e6') < 1/b_max)
# sensitivity: if the bound tightened 10x (d = 7e-17) 1/beta scales as d^-1/2
b2 = mp.sqrt(mp.mpf('7e-17')*2)
print("     sensitivity: d = 7e-17 -> 1/beta = %s (x sqrt(10))" % mp.nstr(1/b2, 8))

print("C9  not checkable here: the negative content claim ('2208.09014 has no "
      "coupling constant ... in sixteen pages') -- the source was not readable.")
print("\nALL CHECKS PASS" if ok_all else "\nSOME CHECK FAILED")
sys.exit(0 if ok_all else 1)
