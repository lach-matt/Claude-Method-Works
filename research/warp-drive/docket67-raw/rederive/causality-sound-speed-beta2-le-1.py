#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation for key causality-sound-speed-beta2-le-1.

The tree (wall.py:33-40, 201-203, 286-302, 548-558) reads the thin-shell surface
EOS slope beta^2 = dp/dsigma as a squared sound speed and uses beta^2 <= 1 as the
causal ceiling; beta^2_crit(x) = 1 at x* = 0.8437418926, the root of
15 s^3 + 3 s^2 - s - 1 = 0, s = sqrt(1-x).

Checks (sympy exact unless marked numeric; z3 for one polynomial sign claim):
  C1  beta^2_crit(s) = 1  <=>  15 s^3 + 3 s^2 - s - 1 = 0 ; x* to 12 digits
  C2  beta^2_crit is strictly increasing in x on (0,1) (so < 1 for all x < x*)
      -- sympy derivative + z3 proof of the sign of the numerator on 0<s<1
  C3  beta^2_crit equals Pitre-Schneider-Poisson 2026 Gamma_1 converted by
      beta^2 = Gamma p/(mu+p) (their dp = Gamma p/sigma dsigma, dmu = (mu+p)/sigma dsigma)
      with mu, p from their Eqs (3.11)-(3.12) -- exact symbolic identity
  C4  the causality theorem the proxy borrows: a barotropic relativistic perfect
      fluid in 2+1 dimensions (the shell's worldvolume) linearised about rest
      has plane-wave speed^2 = dp/deps exactly; boosted characteristic speeds
      (v +- c_s)/(1 +- v c_s) stay within |.|<=1 for every |v|<1 iff c_s <= 1
  C5  NAMED-HYPOTHESIS probes (RECONSTRUCTED illustrations, not sourced):
      (a) thick wall: if each layer responds with local c_t^2(n) and the
          perturbation has one sign across the wall, dp/dsigma is a positive-
          weight average of c_t^2 -> beta^2 <= max c_t^2: beta^2<=1 is NECESSARY,
          not sufficient, for local causality
      (b) elastic (shear-bearing) surface: uniform areal dilatation sees only the
          bulk modulus, beta^2 = K/(eps+p); longitudinal waves see K + mu_s:
          c_L^2 = beta^2 + mu_s/(eps+p).  With shear, beta^2 <= 1 does NOT imply
          c_L <= 1; the causal window becomes beta^2 <= 1 - mu_s/(eps+p).
          Computed: the shear fraction that would close the window at each x.
  C6  the Vlasov (counter-rotating) slope used by wall.py has ceiling 1/2 < 1
"""
import sympy as sp
import z3

ok = True
def chk(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

s, x = sp.symbols('s x', positive=True)
b2c = (1 - s) * (3 * s**2 + 2 * s + 1) / (4 * s**2 * (1 + 3 * s))

# C1
num = sp.factor(sp.numer(sp.together(b2c - 1)))
print("C1 numerator of beta2_crit - 1 :", num)
target = 15 * s**3 + 3 * s**2 - s - 1
chk("C1 beta2_crit=1 <=> 15s^3+3s^2-s-1=0 (up to sign)",
    sp.simplify(num + target) == 0 or sp.simplify(num - target) == 0)
roots = [r for r in sp.Poly(target, s).nroots(n=30) if r.is_real and 0 < r < 1]
chk("C1 exactly one real root in (0,1)", len(roots) == 1)
sstar = roots[0]
xstar = 1 - sstar**2
print("    s* = %.15f   x* = %.15f" % (sstar, xstar))
chk("C1 x* = 0.8437418926 to 1e-9 (tree's datum)", abs(xstar - sp.Float('0.8437418926')) < 1e-9)
chk("C1 4/5 < x* < 24/25", sp.Rational(4, 5) < xstar < sp.Rational(24, 25))

# C2 monotone: d b2c / ds < 0 on (0,1)  <=> increasing in x
d = sp.together(sp.diff(b2c, s))
dn, dd = sp.fraction(d)
dn = sp.expand(dn)
print("C2 d(beta2_crit)/ds numerator:", sp.factor(dn), "  denominator:", sp.factor(dd))
S = z3.Real('S')
z3num = eval(str(dn).replace('s', 'S'))
z3den = eval(str(sp.expand(dd)).replace('s', 'S'))
sol = z3.Solver()
sol.add(S > 0, S < 1, z3num * z3den >= 0)
r = sol.check()
chk("C2 z3: no s in (0,1) with d(beta2_crit)/ds >= 0  (unsat)", r == z3.unsat)
# vacuity guard: the same solver finds the sign flip outside the box
sol2 = z3.Solver(); sol2.add(S > 0, z3num * z3den < 0)
chk("C2 vacuity guard: negative-slope points exist (sat)", sol2.check() == z3.sat)
for xv, want in ((sp.Rational(3, 10), 0.07933), (sp.Rational(2, 3), (3**0.5 - 1) / 2),
                 (sp.Rational(4, 5), 5**0.5 - 1.5)):
    v = float(b2c.subs(s, sp.sqrt(1 - xv)))
    chk("C2 beta2_crit(%s) = %.6f (tree %.6f)" % (xv, v, want), abs(v - want) < 1e-5)

# C3 PSP 2026 cross-check
R, C = sp.symbols('R C', positive=True)
F = s**2
M = (1 - s**2) * R / 2
mu = (1 - sp.sqrt(F)) / (4 * sp.pi * R)
p = (sp.sqrt(F) - 1 + (M / R) / sp.sqrt(F)) / (8 * sp.pi * R)
Cc = M / R
Gamma1 = (4 - 6 * Cc + 2 * sp.sqrt(1 - 2 * Cc)) / (4 * (1 - 2 * Cc))
Gamma1 = Gamma1.subs(sp.sqrt(1 - 2 * Cc), s**2 * 0 + sp.sqrt(sp.expand(1 - 2 * Cc)))
beta2_psp = sp.simplify(Gamma1 * p / (mu + p))
# 1-2C = 1-(1-s^2) = s^2 -> sqrt = s for s>0
beta2_psp = sp.simplify(beta2_psp.subs(sp.sqrt(s**2), s))
chk("C3 beta2_crit == Gamma_1 * p/(mu+p)  (PSP 2026 Eqs 3.11, 3.12, 3.16c)",
    sp.simplify(beta2_psp - b2c) == 0)
chk("C3 wall.py p0 == PSP p (3.12):  (1-s)^2/(16 pi R s)",
    sp.simplify(p - (1 - s)**2 / (16 * sp.pi * R * s)) == 0)

# C4 perfect fluid in 2+1, linearised about rest, flat worldvolume
t, X, Y, k, w = sp.symbols('t X Y k omega')
eps0, p0, cs2 = sp.symbols('epsilon0 p0 c_s2', positive=True)
de, vx, vy = sp.symbols('de vx vy')
# linearised conservation: d_t de + (eps0+p0) div v = 0 ; (eps0+p0) d_t v + grad dp = 0, dp = cs2 de
# plane wave exp(i(kX - wt)):
A = sp.Matrix([[-sp.I * w, sp.I * k * (eps0 + p0), 0],
               [sp.I * k * cs2, -sp.I * w * (eps0 + p0), 0],
               [0, 0, -sp.I * w * (eps0 + p0)]])
disp = sp.factor(A.det())
wsol = sp.solve(sp.Eq(disp, 0), w)
print("C4 dispersion roots omega:", wsol)
chk("C4 sound branch omega^2 = c_s^2 k^2 with c_s^2 = dp/deps (not dp/drho_rest)",
    any(sp.simplify(ws**2 - cs2 * k**2) == 0 for ws in wsol if ws != 0))
# Derive the linearised equations from T^{ab} = (eps+p)u^a u^b + p eta^{ab} to confirm the matrix
eta = sp.diag(-1, 1, 1)
e = sp.Function('e')(t, X, Y); ux = sp.Function('ux')(t, X, Y); uy = sp.Function('uy')(t, X, Y)
lam = sp.symbols('lam')
qq = sp.symbols('qq')
pf = lambda E: p0 + cs2 * (E - eps0) + qq * (E - eps0)**2   # arbitrary barotrope, slope cs2 at eps0
epsf = eps0 + lam * e
u = sp.Matrix([1, lam * ux, lam * uy])   # u^a to first order
T = sp.zeros(3, 3)
for a in range(3):
    for b in range(3):
        T[a, b] = (epsf + pf(epsf)) * u[a] * u[b] + pf(epsf) * eta[a, b]
coords = [t, X, Y]
divT = [sum(sp.diff(T[a, b], coords[b]) for b in range(3)) for a in range(3)]
lin = [sp.series(dT, lam, 0, 2).removeO().coeff(lam, 1) for dT in divT]
lin = [sp.simplify(sp.expand(l)) for l in lin]
print("C4 linearised div T:", lin)
expect0 = sp.diff(e, t) + (eps0 + p0) * (sp.diff(ux, X) + sp.diff(uy, Y))
expect1 = (eps0 + p0) * sp.diff(ux, t) + cs2 * sp.diff(e, X)
chk("C4 derived: d_t de + (eps+p) div v = 0", sp.simplify(lin[0] - expect0) == 0)
chk("C4 derived: (eps+p) d_t v + c_s^2 grad de = 0", sp.simplify(lin[1] - expect1) == 0)
# boosted characteristic speeds
v, c = sp.symbols('v c', real=True)
Vz, Cz = z3.Reals('V C')
sol3 = z3.Solver()
sol3.add(Vz > -1, Vz < 1, Cz >= 0, Cz <= 1,
         z3.Or(Vz + Cz > 1 + Vz * Cz, -(Vz + Cz) > 1 + Vz * Cz))
chk("C4 z3: c_s<=1, |v|<1 => |(v+c_s)/(1+v c_s)| <= 1  (unsat counterexample)",
    sol3.check() == z3.unsat)
sol4 = z3.Solver(); sol4.add(Vz > -1, Vz < 1, Cz > 1, Vz + Cz > 1 + Vz * Cz)
chk("C4 z3: c_s>1 gives a superluminal characteristic (sat)", sol4.check() == z3.sat)

# C5a thick-wall averaging (numeric)
import random
random.seed(67)
worst = 0.0
for _ in range(20000):
    n = random.randint(2, 8)
    c2 = [random.random() for _ in range(n)]          # all local c_t^2 <= 1
    wgt = [random.random() for _ in range(n)]         # one-signed delta rho
    b2 = sum(ci * wi for ci, wi in zip(c2, wgt)) / sum(wgt)
    worst = max(worst, b2 - max(c2))
chk("C5a beta^2 = <c_t^2>_w never exceeds max c_t^2 (20000 random walls)", worst <= 1e-15)
# converse fails: a wall with one superluminal layer and beta^2 < 1
c2 = [1.5, 0.2]; wgt = [0.2, 0.8]
b2 = sum(ci * wi for ci, wi in zip(c2, wgt)) / sum(wgt)
chk("C5a converse fails: beta^2 = %.2f < 1 with a layer at c_t^2 = 1.5" % b2, b2 < 1 and max(c2) > 1)

# C5b shear: window closes when mu_s/(eps+p) >= 1 - beta2_crit
print("C5b shear fraction mu_s/(eps+p) that closes the causal stable window:")
for xv in (sp.Rational(1, 10), sp.Rational(3, 10), sp.Rational(2, 3), sp.Rational(4, 5)):
    bc = float(b2c.subs(s, sp.sqrt(1 - xv)))
    print("     x = %-5s beta2_crit = %.5f  window open iff mu_s/(eps+p) < %.5f" % (xv, bc, 1 - bc))
chk("C5b example: beta^2 = 0.9 (>beta2_crit at x=4/5), shear 0.2 -> c_L^2 = 1.1 > 1",
    0.9 + 0.2 > 1 and 0.9 > float(b2c.subs(s, sp.sqrt(sp.Rational(1, 5)))))

# C6 Vlasov slope ceiling
U = sp.symbols('u', positive=True)
bv = U**2 * (3 * U**2 + 4) / (2 * (1 + U**2) * (3 * U**2 + 2))
chk("C6 lim_{u->oo} beta2_vlasov = 1/2", sp.limit(bv, U, sp.oo) == sp.Rational(1, 2))
Uz = z3.Real('U')
sol5 = z3.Solver(); sol5.add(Uz > 0, Uz**2 * (3 * Uz**2 + 4) >= 2 * (1 + Uz**2) * (3 * Uz**2 + 2) * 1)
chk("C6 z3: beta2_vlasov < 1 for all u > 0 (unsat)", sol5.check() == z3.unsat)

print("\nALL PASS" if ok else "\nSOME FAIL")
raise SystemExit(0 if ok else 1)
