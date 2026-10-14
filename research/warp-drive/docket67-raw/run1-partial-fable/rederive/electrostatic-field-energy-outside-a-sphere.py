#!/usr/bin/env python3
"""DOCKET 67 item 26 -- re-derivation of the result the tree names
'electrostatic-field-energy-outside-a-sphere' (drivensource.py section 4).

Nothing under research/ is edited.  This script only checks.

Checks
  S1  flat-space exterior Coulomb energy  U(a) = Q^2/(8 pi eps0 a)      (sympy)
  S2  Misner-Sharp energy of Reissner-Nordstrom (Hayward gr-qc/9408002
      eq. 4 / 27, read at source): E = M - Q^2/(2r)                      (sympy)
  S3  SI conversion: geometric Q^2/(2r) as a mass is Q^2/(8 pi eps0 c^2 r)
      = X/r with X := Q^2/(8 pi eps0 c^2), the tree's line 147          (sympy)
  S4  inner-horizon ratio r_c/r_- = (1+sqrt(1-q^2))/2                    (sympy)
  N1  X per coulomb^2 under CODATA 2018 (tree) and CODATA 2022 (read at
      source, arXiv:2409.03787 Table XXXII); the tree's pinned 5.0e-8 at
      rel tol 1e-9 and shell_ratio(4472,1,1) = 0.4999847997 at 1e-9     (numeric)
  Z1  the tree's own obligation E2 (mu >= 0, M = mu + X/a  =>  r_c <= a)  (z3)
  Z2  the SAME bound in FULL general relativity for a thin charged shell
      with rest mass m, using the exact junction condition read in
      Gao-Lemos 0804.0295 eq. (44) at rdot = 0 (also Barcelo-Jaramillo
      1112.5265 eq. 7):  M = m - m^2/(2a) + Q^2/(2a),  0 <= m <= a
      (the static-shell existence condition sqrt(f_o(a)) = 1 - m/a >= 0)
      =>  r_c = Q^2/(2M) <= a                                             (z3)
  Z3  the tree's 'bare mass' mu := M - Q^2/(2a) equals m(1 - m/(2a)), so
      mu >= 0  <=>  0 <= m <= 2a; and DRIFT: with m > 2a the bound FAILS,
      but m > 2a is outside the static-shell class (m <= a)              (z3)
  Z4  f_o(a) = (1 - m/a)^2 >= 0: a static shell with 0 <= m <= a never
      sits inside a horizon of its own exterior                           (z3)
"""
import math, sys
import sympy as sp

ok = True
def chk(label, cond):
    global ok
    print("  %-72s %s" % (label, "ok" if cond else "FAIL"))
    ok = ok and bool(cond)

# ---------------------------------------------------------------- S1
Q, eps0, a, r, c, G, M = sp.symbols("Q epsilon_0 a r c G M", positive=True)
E_field = Q / (4 * sp.pi * eps0 * r**2)
U_ext = sp.integrate(sp.Rational(1, 2) * eps0 * E_field**2 * 4 * sp.pi * r**2, (r, a, sp.oo))
print("S1  exterior Coulomb energy outside radius a:", U_ext)
chk("S1  U(a) = Q^2/(8 pi eps0 a)", sp.simplify(U_ext - Q**2 / (8 * sp.pi * eps0 * a)) == 0)

# ---------------------------------------------------------------- S2
# Hayward (4): E = r/2 (1 - g^{-1}(dr,dr)).  Static RN, g^{rr} = f(r).
Qg = sp.symbols("Q_g", positive=True)           # charge in geometric units
f = 1 - 2 * M / r + Qg**2 / r**2
E_MS = r / 2 * (1 - f)
chk("S2  Misner-Sharp E(RN) = M - Q^2/(2r)  [Hayward eq. 4]", sp.simplify(E_MS - (M - Qg**2 / (2 * r))) == 0)
chk("S2  E < 0  <=>  r < Q^2/(2M)  (the contraction radius r_c)",
    sp.solve(sp.Eq(E_MS, 0), r)[0] == Qg**2 / (2 * M))
enc = sp.integrate(4 * sp.pi * r**2 * Qg**2 / (8 * sp.pi * r**4), r)   # indefinite, rho = Q^2/(8 pi r^4)
chk("S2  dE/dr = 4 pi r^2 rho with rho = Q^2/(8 pi r^4) integrates to -Q^2/(2r) + const",
    sp.simplify(enc + Qg**2 / (2 * r)) == 0)
chk("S2  ...and diverges to -oo at r -> 0: no regular centre for RN", sp.limit(enc, r, 0, "+") == -sp.oo)

# ---------------------------------------------------------------- S3
# geometric charge: Q_g^2 = G Q^2 / (4 pi eps0 c^4)  (length^2); mass of a length L is L c^2/G
Qg2_SI = G * Q**2 / (4 * sp.pi * eps0 * c**4)
mass_equiv = (Qg2_SI / (2 * r)) * c**2 / G
X = Q**2 / (8 * sp.pi * eps0 * c**2)
chk("S3  geometric Q^2/(2r) as a mass = X/r, X = Q^2/(8 pi eps0 c^2)  [tree line 147]",
    sp.simplify(mass_equiv - X / r) == 0)
chk("S3  X c^2 / a = U(a): the exterior field energy IS the RN mass deficit at a",
    sp.simplify(X * c**2 / a - U_ext) == 0)

# ---------------------------------------------------------------- S4
q = sp.symbols("q", positive=True)
rc_over_rminus = (q**2 / 2) / (1 - sp.sqrt(1 - q**2))
chk("S4  r_c/r_- = (1 + sqrt(1-q^2))/2", sp.simplify(rc_over_rminus - (1 + sp.sqrt(1 - q**2)) / 2) == 0)

# ---------------------------------------------------------------- N1
C = 2.99792458e8
EPS0_2018 = 8.8541878128e-12     # tree, drivensource.py:278 (CODATA 2018)
EPS0_2022 = 8.8541878188e-12     # arXiv:2409.03787 Table XXXII, u_r 1.6e-10 (READ)
def X_of_Q(Qc, eps): return Qc * Qc / (8.0 * math.pi * eps * C * C)
def shell_ratio(Qc, a_m, mu, eps):
    Xv = X_of_Q(Qc, eps); return Xv / (mu * a_m + Xv)
for tag, eps in (("CODATA 2018 (tree)", EPS0_2018), ("CODATA 2022 (read)", EPS0_2022)):
    Xv = X_of_Q(1.0, eps)
    dev = abs(Xv - 5.0e-8) / 5.0e-8
    print("N1  %s: X per C^2 = %.12e kg m, rel dev from pinned 5.0e-8 = %.3e" % (tag, Xv, dev))
    chk("N1  %s: tree's pin 5.0e-8 @ 1e-9 holds" % tag, dev < 1e-9)
    sr = shell_ratio(4472.0, 1.0, 1.0, eps)
    print("N1  %s: shell_ratio(4472 C, 1 m, 1 kg) = %.12f" % (tag, sr))
    chk("N1  %s: tree's pin 0.4999847997 @ 1e-9 holds" % tag, abs(sr - 0.4999847997) / 0.4999847997 < 1e-9)
    chk("N1  %s: shell_ratio(4472,1,0) == 1.0 exactly" % tag, shell_ratio(4472.0, 1.0, 0.0, eps) == 1.0)
print("N1  eps0 move 2018 -> 2022: rel %.3e (4.5 sigma_2018, arXiv:2409.03787 Table XXXVIII); X moves by the same fraction the other way"
      % ((EPS0_2022 - EPS0_2018) / EPS0_2018))

# ---------------------------------------------------------------- Z1-Z4
import z3
def unsat(label, hyps, goal):
    s = z3.Solver(); s.add(*hyps); s.add(z3.Not(goal))
    chk("%s  [unsat]" % label, s.check() == z3.unsat)
def sat(label, hyps):
    s = z3.Solver(); s.add(*hyps)
    chk("%s  [sat]" % label, s.check() == z3.sat)

Xz, az, mu, rc, Mt = z3.Reals("X a mu r_c M")
tree = [Xz > 0, az > 0, mu >= 0, Mt == mu + Xz / az, rc == Xz / Mt]
sat("Z1  guard: tree's shell system satisfiable", tree)
unsat("Z1  tree E2: mu >= 0, M = mu + X/a  =>  r_c <= a", tree, rc <= az)
sat("Z1  guard: r_c = a attained at mu = 0", tree + [mu == 0, rc == az])

# full GR, G = c = 1: Q2 stands for Q^2 (geometric).  X = Q2/2.
m, Q2, Mg, rcg = z3.Reals("m Q2 M_g r_c_g")
gr = [az > 0, Q2 > 0, m >= 0, m <= az, Mg == m - m * m / (2 * az) + Q2 / (2 * az), rcg == Q2 / (2 * Mg)]
sat("Z2  guard: GR static-shell system satisfiable", gr)
unsat("Z2  GR shell (Gao-Lemos eq.44, rdot=0), 0 <= m <= a  =>  M > 0", gr, Mg > 0)
unsat("Z2  GR shell, 0 <= m <= a  =>  r_c <= a   (THE BOUND survives the binding term)", gr, rcg <= az)
sat("Z2  guard: r_c = a attained at m = 0 in GR too", gr + [m == 0, rcg == az])
unsat("Z2  GR shell: r_c = a  <=>  m = 0  (on 0 <= m <= a)", gr, (rcg == az) == (m == 0))

mu_g = z3.Real("mu_g")
gr2 = [az > 0, Q2 > 0, Mg == m - m * m / (2 * az) + Q2 / (2 * az), mu_g == Mg - Q2 / (2 * az)]
unsat("Z3  tree's mu = M - Q^2/(2a) = m(1 - m/(2a))  identically", gr2, mu_g == m * (1 - m / (2 * az)))
unsat("Z3  mu >= 0  <=>  0 <= m <= 2a", gr2, (mu_g >= 0) == z3.And(m >= 0, m <= 2 * az))
sat("Z3  DRIFT: m > 2a gives mu < 0 and r_c > a (the tree's own drift guard, in GR variables)",
    gr2 + [m > 2 * az, rcg == Q2 / (2 * Mg), Mg > 0, z3.Not(rcg <= az)])
unsat("Z3  ...but m > 2a violates the static-shell class m <= a: the counterexample is not a static shell",
      [az > 0, m > 2 * az], z3.Not(m <= az))

fo = z3.Real("f_o_a")
unsat("Z4  f_o(a) = 1 - 2M/a + Q^2/a^2 = (1 - m/a)^2 >= 0 for the GR shell (no horizon at the shell)",
      gr2 + [fo == 1 - 2 * Mg / az + Q2 / (az * az)], z3.And(fo == (1 - m / az) ** 2, fo >= 0))

print("\nRESULT:", "ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
