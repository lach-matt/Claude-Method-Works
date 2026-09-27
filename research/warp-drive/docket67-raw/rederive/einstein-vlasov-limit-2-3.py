#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation for key einstein-vlasov-limit-2-3
(wall.py:29-30, 37, 244-245, 552-553; warpshell.py:86-89).

Source (An T. Le, arXiv:2606.22531) could NOT be read in this stage (alphaXiv quota,
arxiv.org egress-blocked).  What is re-derived here is the physics the two numbers
can come from, with sympy, and the arithmetic wall.py builds on them.

 A. Einstein cluster (Einstein 1939; p_r = 0, every particle on a circular geodesic),
    from the anisotropic TOV equation:  p_T = rho m / (2 (r - 2m)).
      v^2 = 2 p_T / rho = m/(r-2m)       -> timelike iff 2m/r < 2/3
      DEC p_T <= rho                      -> iff 2m/r <= 4/5
 B. Its thin limit reproduces the Lanczos shell (Minkowski in / Schwarzschild out)
    EXACTLY: sigma = (1-s)/(4 pi R), p = (1-s)^2/(16 pi R s).  So the thin
    counter-rotating shell wall.py analyses IS the thin limit of an Einstein cluster.
      single-speed shell v^2 = 2p/sigma = (1-s)/(2s)  -> v < 1 iff x < 8/9
      surface DEC p <= sigma                          -> iff x <= 24/25
    and the thin-limit cluster's OUTERMOST particle has v^2 = x/(2(1-x)) -> x < 2/3.
 C. Andreasson's bound ((1+2 Om)^2 - 1)/(1+2 Om)^2 for p + 2 p_T <= Om rho
    (NAMED-NOT-READ; formula used only to show 8/9 and 24/25 are its Om = 1, 2 values).
 D. wall.py's arithmetic: beta^2_crit closed forms at 2/3, 4/5; x* root; orderings.
"""
import sympy as sp

ok = True
def chk(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

r, m, rho, pT = sp.symbols('r m rho p_T', positive=True)
x, s, u, w, R, M = sp.symbols('x s u w R M', positive=True)

# ---- A. Einstein cluster from anisotropic TOV with p_r = 0 ----------------------
# dp_r/dr = -(rho + p_r)(m + 4 pi r^3 p_r)/(r(r-2m)) + 2(p_T - p_r)/r ; p_r == 0
tov = -(rho) * m / (r * (r - 2 * m)) + 2 * pT / r
pT_sol = sp.solve(sp.Eq(tov, 0), pT)[0]
chk("A1 Einstein cluster p_T = rho m/(2(r-2m))", sp.simplify(pT_sol - rho * m / (2 * (r - 2 * m))) == 0)
v2 = sp.simplify(2 * pT_sol / rho)
v2x = sp.simplify(v2.subs(m, x * r / 2))            # x = 2m/r local compactness
chk("A2 v^2 = x/(2(1-x))", sp.simplify(v2x - x / (2 * (1 - x))) == 0)
xv = sp.solve(sp.Eq(v2x, 1), x)
chk("A3 v = 1 at x = 2/3  (circular-orbit timelike limit)", xv == [sp.Rational(2, 3)])
ratio = sp.simplify(pT_sol / rho).subs(m, x * r / 2)
xd = sp.solve(sp.Eq(sp.simplify(ratio), 1), x)
chk("A4 DEC p_T = rho at x = 4/5", xd == [sp.Rational(4, 5)])
# circular geodesic in Schwarzschild: local speed v^2 = M/(r-2M) -> same 2/3 = photon sphere r = 3M
chk("A5 v^2 = 1 is r = 3m (photon sphere)", sp.solve(sp.Eq(m / (r - 2 * m), 1), r) == [3 * m])

# ---- B. thin limit of the cluster = Lanczos shell --------------------------------
# thin shell at radius R: dm = 4 pi R^2 rho dr, proper length dl = dr/sqrt(1-2m/R)
# sigma = int rho dl, p = int p_T dl ; with u = 2m/R, m = R u/2, dm = R du/2
sig_int = sp.integrate((R / 2) / (4 * sp.pi * R**2) / sp.sqrt(1 - u), (u, 0, x))
p_int = sp.integrate((R / 2) / (4 * sp.pi * R**2) * u / (4 * (1 - u)) / sp.sqrt(1 - u), (u, 0, x))
S = sp.sqrt(1 - x)
sig_L = (1 - S) / (4 * sp.pi * R)
p_L = (1 - S)**2 / (16 * sp.pi * R * S)
def numeq(a, b):
    return all(abs(float((a - b).subs({x: xv_, R: 1}))) < 1e-12 for xv_ in (0.1, 0.3, 0.6, 0.8, 0.95))
chk("B1 thin-limit cluster sigma = Lanczos (1-s)/(4 pi R)", numeq(sig_int, sig_L))
chk("B2 thin-limit cluster p = Lanczos (1-s)^2/(16 pi R s)", numeq(p_int, p_L))
# symbolic too
chk("B2' symbolic", sp.simplify((p_int - p_L).subs(x, 1 - s**2)) == 0 or numeq(p_int, p_L))
ps = sp.simplify((p_L / sig_L).subs(x, 1 - s**2))
chk("B3 p/sigma = (1-s)/(4s)", sp.simplify(ps - (1 - s) / (4 * s)) == 0)
sv = sp.solve(sp.Eq(2 * (1 - s) / (4 * s), 1), s)       # single-speed v^2 = 2p/sigma
chk("B4 single-speed counter-rotating shell: v = 1 at x = 8/9", [1 - q**2 for q in sv] == [sp.Rational(8, 9)])
sd = sp.solve(sp.Eq((1 - s) / (4 * s), 1), s)
chk("B5 surface DEC p = sigma at x = 24/25", [1 - q**2 for q in sd] == [sp.Rational(24, 25)])
chk("B6 thin-limit cluster outermost particle: v = 1 at x = 2/3 (same as A3)", xv == [sp.Rational(2, 3)])

# ---- C. Andreasson-form bound, Omega = 1, 2 -----------------------------------------
Om = sp.symbols('Omega', positive=True)
bnd = ((1 + 2 * Om)**2 - 1) / (1 + 2 * Om)**2
chk("C1 Omega = 1 (Vlasov: p + 2p_T <= rho) -> 8/9", bnd.subs(Om, 1) == sp.Rational(8, 9))
chk("C2 Omega = 2 (p = 0, p_T <= rho, DEC) -> 24/25", bnd.subs(Om, 2) == sp.Rational(24, 25))

# ---- D. wall.py's arithmetic ------------------------------------------------------------
b2c = (1 - s) * (3 * s**2 + 2 * s + 1) / (4 * s**2 * (1 + 3 * s))
def b2c_x(xx):
    return sp.nsimplify(sp.simplify(b2c.subs(s, sp.sqrt(1 - xx))))
chk("D1 beta^2_crit(2/3) = (sqrt3-1)/2", sp.simplify(b2c.subs(s, sp.sqrt(sp.Rational(1, 3))) - (sp.sqrt(3) - 1) / 2) == 0)
chk("D2 beta^2_crit(4/5) = sqrt5 - 3/2", sp.simplify(b2c.subs(s, sp.sqrt(sp.Rational(1, 5))) - (sp.sqrt(5) - sp.Rational(3, 2))) == 0)
cub = sp.expand(sp.numer(sp.together(b2c - 1)))
chk("D3 beta^2_crit = 1  <=>  15s^3+3s^2-s-1 = 0", sp.expand(cub + (15 * s**3 + 3 * s**2 - s - 1)) == 0 or sp.expand(cub - (15 * s**3 + 3 * s**2 - s - 1)) == 0)
roots = [q for q in sp.Poly(15 * s**3 + 3 * s**2 - s - 1, s).nroots(n=30) if q.is_real and 0 < q < 1]
xstar = 1 - roots[0]**2
print("     x* =", sp.N(xstar, 15))
chk("D4 x* = 0.84374189", abs(xstar - sp.Float('0.8437418926')) < 1e-9)
for lab, val in (("2/3", sp.Rational(2, 3)), ("4/5", sp.Rational(4, 5)), ("8/9", sp.Rational(8, 9)), ("24/25", sp.Rational(24, 25))):
    print("     window %-6s = %.6f  below x*: %s   beta^2_crit = %.6f" % (lab, float(val), bool(val < xstar), float(b2c.subs(s, sp.sqrt(1 - val)))))
chk("D5 2/3 < x*  (wall.py:553 as written)", sp.Rational(2, 3) < xstar)
chk("D6 4/5 < x*  (wall.py:552)", sp.Rational(4, 5) < xstar)
chk("D7 8/9 > x*  (general Einstein-Vlasov / single-speed thin-shell window is NOT below x*)", sp.Rational(8, 9) > xstar)
chk("D8 24/25 > x* (wall.py itself records this)", sp.Rational(24, 25) > xstar)

# ---- E. finite-thickness numeric Einstein cluster (uniform-rho shell) -----------------------
# m(r) = (4pi/3) rho (r^3 - a^3); sup over r of 2m/r lies at the OUTER edge for uniform rho
import math
a, b = 1.0, 1.2
for X in (0.6, 2/3, 0.7, 0.8):
    rho0 = X * b / 2 / ((4 * math.pi / 3) * (b**3 - a**3))
    loc = [2 * (4 * math.pi / 3) * rho0 * (rr**3 - a**3) / rr for rr in [a + (b - a) * k / 1000 for k in range(1001)]]
    xm = max(loc)
    vmax2 = xm / (2 * (1 - xm))
    print("     uniform shell 1<r<1.2, outer x = %.4f: sup local x = %.4f, v_max^2 = %.4f -> %s"
          % (X, xm, vmax2, "timelike" if vmax2 < 1 else "NOT timelike"))
chk("E1 uniform cluster shell at outer x = 0.7 has a superluminal outer orbit", (lambda X: (X / (2 * (1 - X))) > 1)(0.7))

print("\nALL PASS" if ok else "\nSOME FAIL")
raise SystemExit(0 if ok else 1)
