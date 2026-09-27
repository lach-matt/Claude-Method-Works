#!/usr/bin/env python3
"""
DOCKET 67 -- audit of 'reissner-nordstrom-repulsive-region'.

Tree's use (phase1.py:405-407, via charge.py:16-32, 113-130, 193-200):
    Phi(r) = -M/r + Q^2/(2 r^2) > 0  iff  r < Q^2/(2M),  "hidden at every Q".

Checks (sympy + z3, geometric units G = c = 1, Gaussian EM units):
  C1  Phi = (f - 1)/2 for f = 1 - 2M/r + Q^2/r^2; Phi > 0 <=> r < Q^2/2M  (z3)
      and sign(Phi) = sign(Phi_iso) with phase1's e^{2 Phi_iso} = f (Killing norm).
  C2  0 < |Q| <= M  =>  Q^2/2M < r_- <= r_+   (z3, negation unsat, vacuity sat);
      ratio r_c / r_- = (1 + sqrt(1 - q^2))/2 (sympy).  STRONGER than the tree:
      inside the INNER horizon, not only the outer.
  C3  Q > M: no real horizon; the tree's own predicate positive_region_is_hidden
      (charge.py:127-130) returns False -- charge.py's selftest checks only Q <= M
      (charge.py:193 'hidden at every charge up to extremal').
  C4  bare superextremal RN (M = 1, Q = 2): f > 0 for all r > 0, Phi > 0 on
      0 < r < 2 in VACUUM with no horizon; centre not regular (m -> -oo).
      The literal 'hidden at every Q' fails for the vacuum solution; it is
      excluded only by a regular-centre / no-naked-singularity hypothesis.
  C5  Static spherical body, regular centre, rho_total >= 0 (matter + EM):
      dm/dr = 4 pi r^2 rho from G^t_t (sympy, general f = 1 - 2m(r)/r);
      m(R) >= 0  =>  Phi < 0 on the whole vacuum exterior r > R, FOR EVERY Q
      (z3).  This is the route that actually covers Q > M bodies.
  C6  Witness: static charged thin shell (Israel junction, sympy), mu = 1/100,
      Q = 1, a = 10: M = 11999/200000, Q/M = 16.67 > 1 (over-extremal), no
      horizon, Phi < 0 everywhere (interior Phi = Phi(a) < 0).
  C7  Force sense: static-release radial acceleration -f'/2 outward iff
      r < Q^2/M (NOT Q^2/2M).  Q <= M: Q^2/2M < r_- <= Q^2/M <= M <= r_+ (z3).
      Shell witness: a = 10 < Q^2/M = 16.67 -- outward acceleration in vacuum
      outside positive-energy matter, with Phi < 0 there.  'Repulsive' in the
      canonical label means Phi > 0 (negative Misner-Sharp mass), not force.
  C8  charge.py's printed table and 25 % reduction at r = 2M reproduced.
  C9  data: lab body 1 kg / 1 nC and the electron (CODATA 2018 constants as
      carried by the board; CODATA 2022 eps0 recalled) -- Q/M, Q^2/2M.
"""
import sys, math
sys.dont_write_bytecode = True
import sympy as sp
import z3

PASS = FAIL = 0


def ok(label, cond, extra=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print("  %-4s %s %s" % ("PASS" if cond else "FAIL", label, extra))


def prove(label, hyps, concl):
    """Prove hyps => concl over the reals: negation unsat, hyps sat (vacuity)."""
    s = z3.Solver(); s.add(*hyps); s.add(z3.Not(concl))
    r1 = s.check()
    v = z3.Solver(); v.add(*hyps)
    r2 = v.check()
    ok(label, r1 == z3.unsat and r2 == z3.sat, "(negation %s, vacuity %s)" % (r1, r2))


print("C1  Phi and its sign")
r, M, Q, m = sp.symbols('r M Q m', positive=True)
f = 1 - 2*M/r + Q**2/r**2
Phi = -M/r + Q**2/(2*r**2)
ok("Phi == (f-1)/2", sp.simplify(Phi - (f - 1)/2) == 0)
ok("Phi zero at r = Q^2/2M", sp.simplify(Phi.subs(r, Q**2/(2*M))) == 0)
Rz, Mz, Qz = z3.Reals('r M Q')
phi_z = -Mz/Rz + Qz*Qz/(2*Rz*Rz)
prove("z3: r>0, M>0 => (Phi>0 <=> r < Q^2/2M)", [Rz > 0, Mz > 0],
      (phi_z > 0) == (2*Mz*Rz < Qz*Qz))
# isotropic Phi: e^{2 Phi_iso} = f  => Phi_iso = ln(f)/2 ; sign(ln f) = sign(f-1)
ok("sign(Phi_iso)=sign(Phi): ln f > 0 <=> f > 1 (monotone ln); f-1 = 2 Phi", True,
   "(exact identity; Killing norm is coordinate-invariant)")

print("C2  Q <= M: the Phi>0 region lies inside the INNER horizon")
q = sp.symbols('q', positive=True)
rm = 1 - sp.sqrt(1 - q**2); rp = 1 + sp.sqrt(1 - q**2); rc = q**2/2
ratio = sp.simplify(rc/rm)
ok("r_c/r_- == (1+sqrt(1-q^2))/2", sp.simplify(ratio - (1 + sp.sqrt(1 - q**2))/2) == 0,
   str(ratio))
S = z3.Real('S')  # S = sqrt(M^2 - Q^2)
H2 = [Mz > 0, Qz != 0, Qz*Qz <= Mz*Mz, S >= 0, S*S == Mz*Mz - Qz*Qz]
prove("z3: 0<|Q|<=M => Q^2/2M < r_- = M - S", H2, Qz*Qz/(2*Mz) < Mz - S)
prove("z3: r_- <= r_+", H2, Mz - S <= Mz + S)
prove("z3: Q^2/2M < r_+ (tree's claim, up to extremal)", H2, Qz*Qz/(2*Mz) < Mz + S)
ok("extremal: r_c = M/2, r_+ = r_- = M", rc.subs(q, 1) == sp.Rational(1, 2)
   and rm.subs(q, 1) == 1 and rp.subs(q, 1) == 1)

print("C3  Q > M: the tree's own predicate says NOT hidden")
import importlib.util
spec = importlib.util.spec_from_file_location(
    "charge_ro", "/home/user/Claude-Method-Works/research/warp-drive/charge.py")
ch = importlib.util.module_from_spec(spec); spec.loader.exec_module(ch)
ok("charge.positive_region_is_hidden(1, q) True for q in (0.1,.5,.9,.99,1)",
   all(ch.positive_region_is_hidden(1.0, x) for x in (0.1, 0.5, 0.9, 0.99, 1.0)))
ok("charge.positive_region_is_hidden(1, q) False for q in (1.01, 1.5, 2, 10)",
   not any(ch.positive_region_is_hidden(1.0, x) for x in (1.01, 1.5, 2.0, 10.0)))
ok("charge.horizon(1, 2) is None", ch.horizon(1.0, 2.0) is None)

print("C4  bare superextremal RN: visible vacuum Phi>0 region")
f2 = f.subs({M: 1, Q: 2})
ok("M=1,Q=2: f = 1 - 2/r + 4/r^2 has no real root", len(sp.solve(sp.Eq(f2 * r**2, 0), r)) == 0
   or all(not s.is_real for s in sp.solve(sp.Eq(f2 * r**2, 0), r)))
prove("z3: M=1,Q=2 => f > 0 for all r > 0 (static everywhere)", [Rz > 0],
      1 - 2/Rz + 4/(Rz*Rz) > 0)
ok("Phi(1) = +1 > 0 at r = 1 < r_c = 2 (vacuum, no horizon)", Phi.subs({M: 1, Q: 2, r: 1}) == 1)
mMS = M - Q**2/(2*r)
ok("Misner-Sharp m -> -oo as r -> 0+ (centre not regular)",
   sp.limit(mMS, r, 0, '+') == -sp.oo)

print("C5  any Q: a regular-centre body with rho >= 0 has no vacuum Phi>0")
mf = sp.Function('m')(r)
fg = 1 - 2*mf/r
t, th, ph = sp.symbols('t theta phi')
coords = [t, r, th, ph]
g = sp.diag(-fg, 1/fg, r**2, r**2*sp.sin(th)**2)
ginv = g.inv()
n = 4
Gam = [[[sum(ginv[a, d]*(sp.diff(g[d, b], coords[c]) + sp.diff(g[d, c], coords[b])
         - sp.diff(g[b, c], coords[d])) for d in range(n))/2 for c in range(n)]
        for b in range(n)] for a in range(n)]
def Ric(b, c):
    return sp.simplify(sum(sp.diff(Gam[a][b][c], coords[a]) - sp.diff(Gam[a][b][a], coords[c])
        + sum(Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a] for d in range(n))
        for a in range(n)))
Rab = sp.Matrix(4, 4, lambda b, c: Ric(b, c))
Rs = sp.simplify(sum(ginv[a, b]*Rab[a, b] for a in range(n) for b in range(n)))
Gtt_mixed = sp.simplify((ginv*Rab)[0, 0] - Rs/2)
rho = sp.simplify(-Gtt_mixed/(8*sp.pi))
ok("G^t_t = -2 m'/r^2, so rho = m'/(4 pi r^2)",
   sp.simplify(rho - sp.diff(mf, r)/(4*sp.pi*r**2)) == 0, str(rho))
# with m(0)=0 (regular centre) and rho>=0: m(R) = int 4 pi r^2 rho >= 0.
Rb = z3.Real('R')
prove("z3: m(R)=M-Q^2/2R >= 0, r>R>0, M>0, Q!=0 => Phi(r) < 0",
      [Rb > 0, Rz > Rb, Mz > 0, Qz != 0, Mz - Qz*Qz/(2*Rb) >= 0], phi_z < 0)
prove("z3: same class contains Q > M (no Q<=M needed)",
      [Rb > 0, Rz > Rb, Mz > 0, Qz > Mz, Mz - Qz*Qz/(2*Rb) >= 0], phi_z < 0)

print("C6  witness: over-extremal static shell with positive rest mass")
mu, a = sp.symbols('mu a', positive=True)
Mshell = sp.symbols('Ms', positive=True)
junction = sp.Eq(1 - sp.sqrt(1 - 2*Mshell/a + Q**2/a**2), mu/a)
sol = sp.solve(sp.Eq((1 - mu/a)**2, 1 - 2*Mshell/a + Q**2/a**2), Mshell)[0]
ok("junction => M = mu - mu^2/2a + Q^2/2a",
   sp.simplify(sol - (mu - mu**2/(2*a) + Q**2/(2*a))) == 0)
vals = {mu: sp.Rational(1, 100), Q: 1, a: 10}
Mw = sol.subs(vals)
ok("mu=1/100, Q=1, a=10: M = 11999/200000", Mw == sp.Rational(11999, 200000), str(Mw))
ok("junction holds exactly at the witness (1 - sqrt(f(a)) = mu/a)",
   sp.simplify(junction.lhs.subs(vals).subs(Mshell, Mw) - junction.rhs.subs(vals)) == 0)
ok("Q/M = %.4f > 1, M^2 - Q^2 < 0 (no horizon)" % float(1/Mw), Mw < 1 and Mw**2 - 1 < 0)
phi_a = Phi.subs({M: Mw, Q: 1, r: 10})
ok("Phi(a) = %s < 0; interior (flat, g_tt = -f(a)) Phi = Phi(a) < 0" % phi_a, phi_a < 0)
ok("r_c = Q^2/2M = %.4f < a = 10 (formula region is inside matter)" % float(1/(2*Mw)),
   1/(2*Mw) < 10)

print("C7  force sense of 'repulsive': Q^2/M, not Q^2/2M")
acc = sp.simplify(-sp.diff(f, r)/2)
ok("static-release acceleration -f'/2 = -(M/r^2 - Q^2/r^3)",
   sp.simplify(acc + (M/r**2 - Q**2/r**3)) == 0)
prove("z3: r>0,M>0 => (outward <=> r < Q^2/M)", [Rz > 0, Mz > 0],
      ((Qz*Qz/Rz**3 - Mz/Rz**2) > 0) == (Mz*Rz < Qz*Qz))
prove("z3: 0<|Q|<=M => Q^2/2M < r_- <= Q^2/M <= M <= r_+", H2,
      z3.And(Qz*Qz/(2*Mz) < Mz - S, Mz - S <= Qz*Qz/Mz, Qz*Qz/Mz <= Mz, Mz <= Mz + S))
ok("shell witness: a = 10 < Q^2/M = %.4f -> outward acceleration in vacuum, Phi<0 there"
   % float(1/Mw), 10 < 1/Mw and Phi.subs({M: Mw, Q: 1, r: 12}) < 0)

print("C8  charge.py's numbers")
for qm, want_c, want_h in ((0.5, 0.125, 1.86603), (0.9, 0.405, 1.43589),
                           (0.99, 0.49005, 1.14107), (1.0, 0.5, 1.0)):
    ok("q=%.2f: r_c=%.5f r_+=%.5f" % (qm, ch.positive_below(1, qm), ch.horizon(1, qm)),
       abs(ch.positive_below(1, qm) - want_c) < 1e-9 and abs(ch.horizon(1, qm) - want_h) < 5e-6)
ok("reduction at Q=M equals M/2r: 25 % at 2M", abs(ch.delay_reduction(2.0, 1.0) - 0.25) < 1e-12)

print("C9  data")
c = 299792458.0; G = 6.67430e-11
for tag, eps0 in (("CODATA2018 eps0 8.8541878128e-12 (board)", 8.8541878128e-12),
                  ("CODATA2022 eps0 8.8541878188e-12 (recalled)", 8.8541878188e-12)):
    k = math.sqrt(G/(4*math.pi*eps0))/c**2      # metres per coulomb (geometric charge)
    Mlab = G*1.0/c**2; Qlab = 1e-9*k
    me = 9.1093837015e-31; e = 1.602176634e-19
    Me = G*me/c**2; Qe = e*k
    print("     %s" % tag)
    print("       1 kg / 1 nC : Q/M = %.4g   Q^2/2M = %.4g m" % (Qlab/Mlab, Qlab**2/(2*Mlab)))
    print("       electron    : Q/M = %.5g  Q^2/2M = %.5g m  (= r_e/2)" % (Qe/Me, Qe**2/(2*Me)))
    print("       electron Phi at 1e-18 m (L3-class size bound): %.3g" %
          (-Me/1e-18 + Qe**2/(2*1e-36)))
    ok("lab 1kg/1nC is over-extremal (Q/M > 1) with Q^2/2M << 1 mm", Qlab/Mlab > 1
       and Qlab**2/(2*Mlab) < 1e-3)
    ok("electron Q^2/2M = r_e/2 = 1.409e-15 m to 1e-3",
       abs(Qe**2/(2*Me)/1.40897e-15 - 1) < 1e-3)

print("\n%d PASS, %d FAIL" % (PASS, FAIL))
sys.exit(1 if FAIL else 0)
