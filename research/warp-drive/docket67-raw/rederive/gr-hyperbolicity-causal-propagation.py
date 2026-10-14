#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for gr-hyperbolicity-causal-propagation.

The external result (Choquet-Bruhat 1952 / Choquet-Bruhat--Geroch 1969, as restated
and applied by R.J. Low, gr-qc/9812067, Thm 2.4 / Cor 2.5 / Cor 4.1): for Einstein +
matter obeying a quasilinear symmetric hyperbolic system whose ray cone lies inside
the light cone, changing initial data on K subset Sigma leaves D(Sigma \\ K) isometric.
The tree (phase1.py:114-119, 309-340) uses it to say: a corridor of length L is not
complete before L/2c after the first action (best case, midpoint), and the first
traversal cannot beat light; it computes 1.5 L/c vs L/c.

Checks (each prints PASS/FAIL/NOTE):
 C1 principal symbol of the harmonic-gauge (linearised) Einstein operator: speeds +-c.
 C2 tree data: L/2c for L = 4 ly, in s and Julian years; tree ly vs IAU ly.
 C3 single causal origin in flat 1+1: completion time min over origin = L/2c at midpoint.
 C4 Low's bound on first arrival at B: t0 + |xB-x0|/c.  Tree's scheme (midpoint,
    complete-then-traverse) gives 1.5 L/c; a front-following scheme from A gives L/c.
    Both >= L/c: 'never a lead' agrees; '1.5' is scheme-specific, not the bound.
 C5 without the single-origin hypothesis: N pre-positioned independent actors
    complete at L/(2Nc) after the first action -- the literal clause needs the hypothesis.
 C6 the matter hypothesis: a matter sector with characteristic speed v > c widens the
    domain of influence; completion floor becomes L/(2 max(c,v)).
 C7 energy condition vs causal propagation: tachyonic-potential scalar (Kontou-Sanders
    2003.01815 example) has T_00 < 0 for admissible data but principal symbol = light cone.
"""
import sympy as sp

ok = True
def rep(tag, cond, msg):
    global ok
    print(f"{'PASS' if cond else 'FAIL'}  {tag}: {msg}")
    ok = ok and bool(cond)

# ---- C1: principal symbol of box_g in harmonic gauge (flat background, linearised)
c, w, kx, ky, kz = sp.symbols('c omega k_x k_y k_z', positive=True)
eta_inv = sp.diag(-1/c**2, 1, 1, 1)          # g^{mu nu} for coordinates (t,x,y,z)
k = sp.Matrix([-w, kx, ky, kz])               # covector (k_t = -omega)
symbol = sp.expand((k.T * eta_inv * k)[0])    # g^{mu nu} k_mu k_nu
sols = sp.solve(sp.Eq(symbol, 0), w)
speed = sp.simplify(sols[0] / sp.sqrt(kx**2 + ky**2 + kz**2))
rep("C1", sp.simplify(speed - c) == 0,
    f"harmonic-gauge principal symbol {symbol} = 0 gives phase speed {speed} (the null cone of g; "
    "each of the 10 components of h-bar obeys box h-bar = 0 -- the symbol is scalar x identity)")

# ---- C2: tree data
C_SI = 299792458.0
LY_TREE = 9.4607e15
LY_IAU = 299792458.0 * 365.25 * 86400.0     # IAU light-year: c x Julian year
YR = 3.15576e7
L = 4.0 * LY_TREE
T_est = L / (2 * C_SI)
rep("C2a", abs(T_est - 6.3113e7) / 6.3113e7 < 1e-3, f"L/2c = {T_est:.6e} s (tree pins 6.3113e7 at rel tol 1e-3)")
print(f"NOTE  C2a': exact value {T_est:.5e} s = 2 Julian yr = 6.31152e7 s; the tree's printed pin 6.3113e7 differs by "
      f"{abs(T_est-6.3113e7)/T_est:.2e} relative -- a last-digit DISCREPANCY inside the tree's own tolerance, not an error of the theorem")
rep("C2b", abs(T_est / YR - 2.0) < 1e-3, f"= {T_est/YR:.7f} Julian yr (tree pins 2.0)")
print(f"NOTE  C2c: tree ly {LY_TREE:.5e} vs IAU {LY_IAU:.10e}: rel diff {abs(LY_TREE-LY_IAU)/LY_IAU:.2e}; "
      "c is exact by SI definition. No datum here can move the inequality 1.5 > 1.")

# ---- C3: single origin completion time
x0, Ls, cs = sp.symbols('x0 L c', positive=True)
T = sp.Max(x0, Ls - x0) / cs
# minimise over x0 in [0, L]: max(x0, L-x0) >= L/2 with equality iff x0 = L/2
opt = sp.simplify(T.subs(x0, Ls/2))
rep("C3a", sp.simplify(opt - Ls/(2*cs)) == 0, f"T(x0=L/2) = {opt}")
import random
random.seed(1)
worst = min(max(u, 1-u) for u in (random.random() for _ in range(100000)))
rep("C3b", worst >= 0.5, f"sampled min over x0 of max(x0,L-x0)/L = {worst:.6f} >= 1/2 (no origin beats midpoint)")

# ---- C4: first-arrival bound vs the tree's scheme
# Low Sec.4: D^+(Sigma\K), K = J^+(p) cap Sigma, is unchanged, so the earliest point of B's
# worldline reachable is where it leaves D^+(Sigma\K): t0 + |xB - x0|/c (flat background).
def low_bound(x_origin, xB, t0=0.0, cc=1.0):
    return t0 + abs(xB - x_origin) / cc
Lu = 1.0
tree_scheme = Lu/2 + Lu          # complete from midpoint (L/2c), then traverse L/c
front_follow = low_bound(0.0, Lu) # decision at A, build on the light front, ride behind it
rep("C4a", tree_scheme / Lu == 1.5, f"tree scheme (midpoint, complete-then-traverse): {tree_scheme} L/c -> penalty 1.5")
rep("C4b", front_follow >= Lu and low_bound(0.5, Lu) + 0.5 >= Lu,
    f"Low bound for a traveller departing A with the decision at A: {front_follow} L/c; "
    "a front-following scheme attains it (tie, never a lead)")
print("NOTE  C4c: 'never a lead' (single_transition_beats_light() = False) agrees with the source bound; "
      "the factor 1.5 (single_transition_penalty) is one scheme's value, not a lower bound -- the "
      "source-implied floor on the ratio is 1. A discrepancy of over-precision, not a refutation.")

# ---- C5: pre-positioned independent actors
for N in (1, 2, 4, 10):
    # N actors at segment midpoints (2i+1)L/(2N), all acting at t=0 on prearranged clocks
    comp = max(min(abs(xx - (2*i+1)*Lu/(2*N)) for i in range(N)) for xx in [j/1000 for j in range(1001)])
    print(f"NOTE  C5: N={N:2d} independent actors -> completion {comp:.4f} L/c after first action (L/2Nc = {Lu/(2*N):.4f})")
rep("C5", abs(comp - Lu/20) < 1e-9,
    "literal 'not complete before L/2c after the first action' needs a SINGLE CAUSAL ORIGIN "
    "(all actions downstream of one event, Low's K = J^+(p) cap Sigma); positioning the actors "
    "from one point costs >= L/2c again, so the bound moves to the positioning, it does not vanish")

# ---- C6: matter characteristic speed v > c
v = sp.symbols('v', positive=True)
Tv = Ls / (2*sp.Max(cs, v))
rep("C6", sp.simplify(Tv.subs(v, 2*cs) - Ls/(4*cs)) == 0 and sp.simplify(Tv.subs(v, cs/2) - Ls/(2*cs)) == 0,
    "with a matter ray cone wider than g's light cone (speed v=2c) the floor halves to L/4c; with v<=c it is L/2c. "
    "The tree's 'characteristic speed c' is a HYPOTHESIS ON THE MATTER SECTOR, not a property of Einstein's "
    "equations alone")

# ---- C7: WEC violation with causal principal part (tachyonic potential, flat, 1+1)
m, phidot, phix, phi = sp.symbols('m phidot phi_x phi', real=True)
V = -m**2 * phi**2
T00 = sp.Rational(1, 2)*(phidot**2 + phix**2) + V
val = T00.subs({phidot: 0, phix: 0, phi: 1, m: 1})
# principal part of phi_tt - phi_xx - 2 m^2 phi = 0 is the flat wave operator: speed 1 (= c)
w1, k1 = sp.symbols('w1 k1', positive=True)
psym = -w1**2 + k1**2
rep("C7", val < 0 and sp.solve(psym, w1) == [k1],
    f"T_00 = {val} < 0 (WEC fails) while the characteristic speed is w/k = 1 = c: energy-condition "
    "violation does not by itself widen the domain of influence (Kontou-Sanders 2003.01815 p.12: "
    "T=0 on O subset Sigma => T=0 on D(O)). Evidence FOR the tree's use with exotic matter, "
    "provided the exotic sector's principal part is causal")

# ---- C8: measured speed of gravity (GW170817, 1710.05834: -3e-15 <= (v_gw-c)/c <= +7e-16)
for eps in (-3e-15, 7e-16):
    Tg = L / (2 * C_SI * (1 + eps))
    print(f"NOTE  C8: v_gw = c(1{eps:+.0e}) -> floor {Tg:.10e} s, shift {Tg-T_est:+.3e} s; penalty ratio unchanged at 1.5 to 1e-14")
rep("C8", abs(L/(2*C_SI*(1+7e-16)) - T_est)/T_est < 1e-14,
    "the only empirical input to 'characteristic speed c' moves the floor by < 1e-14 relative; no conclusion moves")

print("\nRESULT:", "ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
raise SystemExit(0 if ok else 1)
