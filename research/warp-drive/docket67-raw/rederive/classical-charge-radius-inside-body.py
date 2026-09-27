#!/usr/bin/env python3
"""DOCKET 67 re-derivation: classical-charge-radius-inside-body.

Tree's use (overturn.py:48-53, 262-263, 375-377): "r_c = Q^2/2M of any body of
charge Q and mass M >= 0 satisfies r_c <= a, its own radius, for every charged
body that exists."  Derivation owner: drivensource.py section 4 + obligations E2.

Checks
  A. z3: E2 as drivensource states it (bare mass mu >= 0)          -> expect unsat
  B. z3: the SAME claim under overturn.py's wording (total M >= 0)  -> expect sat (counterexample)
  C. sympy+z3: EXACT GR static thin shell (Israel junction, flat interior,
     RN exterior): M = mu - mu^2/2a + Q^2/2a; r_c <= a on the normal branch
  D. identity: r_c <= a  <=>  m_MS(a) = M - Q^2/2a >= 0 (Misner-Sharp at surface)
  E. numeric: r_c vs measured size for charged bodies that exist
  F. Bonnor-Cooperstock 1989 numbers as restated in arXiv:0710.5619 eq (3.1),(3.7)
  G. later-literature discrepancy: arXiv:2603.22223 eq (9) integrated vs eq (11)
"""
import math, sys
import sympy as sp
try:
    import z3
except ImportError:
    sys.exit("pip install z3-solver")

ok = True
def rep(name, got, want):
    global ok
    good = (got == want)
    ok &= good
    print(f"  [{'PASS' if good else 'FAIL'}] {name}: {got} (want {want})")

print("A/B. z3 on the flat-space accounting M = mu + X/a, r_c = X/M")
X, a, mu, rc, Mt = z3.Reals("X a mu r_c M")
base = [X > 0, a > 0, Mt == mu + X / a, rc == X / Mt]
s = z3.Solver(); s.add(base + [mu >= 0, z3.Not(rc <= a)])
rep("E2 (mu>=0) negated", str(s.check()), "unsat")
s = z3.Solver(); s.add(base + [Mt > 0, z3.Not(rc <= a)])
r = s.check(); rep("overturn.py wording (M>0 only) admits counterexample", str(r), "sat")
if r == z3.sat:
    m = s.model(); print("     witness:", {str(k): str(m[k]) for k in (X, a, mu, Mt, rc)})

print("\nC. exact GR static charged thin shell (G=c=1)")
M, Q, A, m0 = sp.symbols("M Q a mu", positive=True)
# Israel: sqrt(f_in) - sqrt(f_out) = mu/a, f_in = 1 (flat interior), f_out = 1-2M/a+Q^2/a^2
# normal branch: sqrt(f_out) = 1 - mu/a >= 0  <=>  mu <= a
fout = 1 - 2*M/A + Q**2/A**2
Msol = sp.solve(sp.Eq(fout, (1 - m0/A)**2), M)[0]
print("   M =", sp.simplify(Msol))
excess = sp.factor(sp.simplify(Msol - Q**2/(2*A)))
print("   M - Q^2/2a =", excess)
rep("M - Q^2/2a == mu(2a-mu)/(2a)", sp.simplify(excess - m0*(2*A - m0)/(2*A)) == 0, True)
# z3 nonlinear: normal branch 0<=mu<=a  =>  r_c = Q^2/(2M) <= a
q, aa, u, MM = z3.Reals("q aa u MM")
hyp = [aa > 0, q > 0, u >= 0, u <= aa, MM * 2 * aa == 2 * aa * u - u * u + q * q]
s = z3.Solver(); s.add(hyp + [z3.Not(q * q <= 2 * MM * aa)])
rep("GR shell normal branch: r_c <= a negated", str(s.check()), "unsat")
s = z3.Solver(); s.add(hyp + [u == 0, q * q == 2 * MM * aa]); rep("guard: equality at mu=0 attainable", str(s.check()), "sat")
s = z3.Solver(); s.add([aa > 0, q > 0, u > 2 * aa, MM * 2 * aa == 2 * aa * u - u * u + q * q, MM > 0, z3.Not(q * q <= 2 * MM * aa)])
rep("DRIFT: mu > 2a (beyond throat, other sheet) breaks it", str(s.check()), "sat")

print("\nD. r_c <= a <=> m_MS(a) >= 0 (M>0)")
s = z3.Solver(); s.add([aa > 0, q > 0, MM > 0, z3.Not((q * q <= 2 * MM * aa) == (MM - q * q / (2 * aa) >= 0))])
rep("equivalence negated", str(s.check()), "unsat")

print("\nE. charged bodies that exist: r_c = Z^2 alpha hbar c / (2 M c^2) vs measured size")
ahc = 7.2973525643e-3 * 197.3269804      # MeV fm (CODATA 2022; not read at source this run)
bodies = [  # name, Z, M [MeV], size [fm], size kind, source of size
    ("electron", 1, 0.51099895069, 2.8e-4, "95% CL upper bound, LEP Bhabha form factor", "arXiv:2506.02450 Table 1 / eq (3) [READ]"),
    ("muon", 1, 105.6583755, 2.4e-4, "95% CL upper bound (F_e=F_mu)", "arXiv:2506.02450 Table 1 [READ]"),
    ("tau", 1, 1776.93, 4.0e-4, "95% CL upper bound (F_e=F_tau); x sqrt2 if F_e=1", "arXiv:2506.02450 Table 1 [READ]"),
    ("proton", 1, 938.27208943, 0.84075, "rms charge radius", "CODATA 2022 [NOT READ this run]"),
    ("pi+", 1, 139.57039, 0.659, "rms charge radius", "PDG 2024 [NOT READ this run]"),
    ("alpha (He-4 nucleus)", 2, 3727.3794118, 1.6785, "rms charge radius", "Angeli-Marinova 2013 [NOT READ]"),
    ("Pb-208 nucleus", 82, 193687.0, 5.5012, "rms charge radius", "Angeli-Marinova 2013 [NOT READ]"),
    ("U-238 nucleus", 92, 221695.0, 5.8571, "rms charge radius", "Angeli-Marinova 2013 [NOT READ]"),
]
rows = []
for n, Z, Mv, size, kind, src in bodies:
    rcv = Z * Z * ahc / (2 * Mv)
    ratio = rcv / size
    if "bound" in kind:
        verdict = "r_c > a_max: FAILS" if ratio > 1.05 else ("MARGINAL (within bound uncertainty)" if ratio > 0.5 else "holds")
    else:
        verdict = "holds" if ratio < 1 else "FAILS"
    rows.append((n, rcv, size, ratio, verdict))
    print(f"   {n:22s} r_c = {rcv:.4e} fm   size = {size:.4e} fm ({kind})   r_c/size = {ratio:.3e}   {verdict}")
print("   W+ : r_c = %.3e fm; no measured size bound read -> OPEN" % (ahc / (2 * 80369.2)))
# macroscopic sphere at field-emission limit E: r_c/a = 3 eps0 E^2 / (2 rho c^2)
eps0, c = 8.8541878188e-12, 299792458.0
for E, rho in [(1e10, 1000.0), (1e10, 20000.0)]:
    print(f"   macroscopic sphere, surface field {E:.0e} V/m, density {rho:.0f} kg/m^3: r_c/a = {3*eps0*E*E/(2*rho*c*c):.2e}  holds")
e_ratio = rows[0][3]; mu_ratio = rows[1][3]; tau_ratio = rows[2][3]
rep("electron r_c exceeds measured size bound", e_ratio > 1, True)
rep("muon r_c exceeds measured size bound", mu_ratio > 1, True)
print(f"   electron: r_c/a_max = {e_ratio:.0f}; muon: {mu_ratio:.1f}; tau: {tau_ratio:.2f} (or {tau_ratio/math.sqrt(2):.2f} with F_e=1)")
# bare (non-EM) mass the electron would need as a classical body of radius a_max
X_e = ahc / 2        # MeV fm  (field energy outside a is X/a)
print(f"   electron as classical body at a = 2.8e-19 m: exterior field energy X/a = {X_e/2.8e-4:.1f} MeV > M = 0.511 MeV -> mu = M - X/a = {0.51099895 - X_e/2.8e-4:.1f} MeV < 0")
# with the 1983 bound used by Bonnor-Cooperstock (1e-16 cm = 1e-3 fm)
print(f"   with the 1983 bound 1e-16 cm: r_c/a = {rows[0][1]/1e-3:.0f}")

print("\nF. Bonnor-Cooperstock 1989 as restated in arXiv:0710.5619 eq (3.1),(3.7) (cm, relativistic units)")
mB, qB, aB = 6.76e-56, 1.38e-34, 1e-16
lhs = qB**2 / aB**2 - 2 * mB / aB
Mbare = mB - qB**2 / (2 * aB)
print(f"   q^2/a^2 - 2m/a = {lhs:.3e}   (restatement: ~2e-36 > 0)")
print(f"   M = m - q^2/2a = {Mbare:.3e} cm (restatement: negative, about 1e-52 cm)")
rep("B-C (3.7) reproduced (1.5e-36..2.5e-36)", 1.5e-36 < lhs < 2.5e-36, True)
rep("B-C (3.1) negative ~1e-52", -1.5e-52 < Mbare < -0.5e-52, True)
# geometrized electron values from CODATA: G m_e/c^2 and sqrt(G/(4 pi eps0)) e/c^2
G = 6.67430e-11; me = 9.1093837139e-31; e = 1.602176634e-19
print(f"   check inputs: G m_e/c^2 = {G*me/c**2*100:.3e} cm, sqrt(G/4pi eps0) e/c^2 = {math.sqrt(G/(4*math.pi*eps0))*e/c**2*100:.3e} cm")

print("\nG. arXiv:2603.22223 eq (9) integrated over space vs its eq (11)")
r, R, mf, al = sp.symbols("r R m_f alpha", positive=True)
T00 = (6*mf*R**2/(r**2+R**2)**sp.Rational(5, 2) + al*r**2/(r**2+R**2)**3 - al*R**2/(r**2+R**2)**3) / (8*sp.pi)
Mint = sp.simplify(sp.integrate(4*sp.pi*r**2*T00, (r, 0, sp.oo)))
M11 = mf + 3*sp.pi*al/(32*R) - 5*sp.pi*al/(32*R)
print("   int T00 (eq 9 as printed) =", Mint, "   eq (11) =", sp.simplify(M11))
print("   difference =", sp.simplify(Mint - M11), " -> DISCREPANCY recorded (peripheral; not a refutation)")
T00b = T00 - 4*al*R**2/(r**2+R**2)**3/(8*sp.pi)   # Poincare term with coefficient 5
print("   with Poincare coefficient 5 instead of 1: int =", sp.simplify(sp.integrate(4*sp.pi*r**2*T00b, (r, 0, sp.oo))))
t0 = sp.simplify((T00b.subs(r, 0)).subs(mf, sp.Symbol('M')+sp.pi*al/(16*R)))
print("   then T00(0) =", t0, "-> negative when M R << alpha (R=1e-20 m: electron)")

print("\nALL CHECKS", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
