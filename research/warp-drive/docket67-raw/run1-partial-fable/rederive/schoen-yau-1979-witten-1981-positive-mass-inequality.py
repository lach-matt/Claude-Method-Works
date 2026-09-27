#!/usr/bin/env python3
"""
DOCKET 67 rederivation -- the positive mass theorem (Schoen-Yau 1979/1981, Witten 1981)
as used by certify.py, overturn.py, phase1.py, concentric.py on the warp board.

The theorem itself (M_ADM >= 0 for complete asymptotically flat initial data
satisfying the DEC, rigidity: equality iff Minkowski) is an infinite-dimensional
geometric statement and is NOT re-provable here.  What IS finite/closed-form and
is checked below:

  A. every numerical datum the four owners quote (two-zone masses, Phi pins,
     the Error-1 witness, the header/selftest Phi(1) discrepancy);
  B. the ADM mass of the seated potential  Phi = m/sqrt(r^2+a^2) - m/max(r,R_s),
     read off the far-field 1/r coefficient symbolically (sympy): exactly 0;
  C. the linearised energy density rho = (1/4 pi G) Lap Phi of the seated
     potential, and whether the DEC (rho >= 0 in the static linearised case)
     holds anywhere -- it fails at every r < R_s, symbolically;
  D. the LOGICAL shape of the four owners' uses, in propositional z3:
     PMT := (AF & DEC & complete) -> (M >= 0 & (M = 0 -> Minkowski)).
     With DEC = False the theorem yields NO constraint on the sign of M, so
       (i)  'M_ADM = 0 satisfies the inequality' is TRUE but VACUOUS,
       (ii) 'a bare negative mass is forbidden by the PMT' is NOT derivable
            from the theorem when the negative mass's matter violates the DEC
            (which any negative m(r) with regular centre must, by certify's own
            Misner-Sharp reading).
     z3 exhibits the model: DEC=False, M<0, PMT holds.
  E. the exact-theorem counterexample structure: a non-Minkowski configuration
     with M_ADM = 0 must violate a hypothesis -- concentric.py:51-53 and pair.py
     state this correctly; z3 confirms (AF & DEC & complete & M=0 & not Minkowski)
     is UNSAT under PMT.
"""
import math, sys
import sympy as sp

ok = True
def chk(label, got, want, tol=0.0):
    global ok
    good = (abs(got - want) <= tol) if isinstance(want, float) else (got == want)
    ok &= good
    print("  %-66s %-18s %s" % (label, got if not isinstance(got, float) else "%.7g" % got, "ok" if good else "FAIL"))

print("A. owners' numerical data")
r0, R, b, a = 1.0, 2.0, 1.0, 1.5
m_r0 = -4.0/3.0*math.pi*b*r0**3
m_R = m_r0 + 4.0/3.0*math.pi*a*(R**3 - r0**3)
chk("overturn m(r0) = -(4/3) pi b r0^3", m_r0, -4.188790, 1e-6)
chk("overturn m(R) = +(4/3) pi 9.5", m_R, 39.793507, 1e-6)
chk("  = (4/3) pi (a(R^3-r0^3) - b r0^3) = (4/3) pi 9.5", 4.0/3.0*math.pi*9.5, m_R, 1e-9)
chord0 = 2*(a*(R-r0) - b*r0)
chk("overturn chord(0) = 2[a(R-r0) - b r0]", chord0, 1.0, 1e-12)
chk("m(R) > 0: the two-zone total mass is positive", m_R > 0, True)

A_CORE, R_SHELL = 0.02, 200.0
def phi(r, m): return m/math.sqrt(r*r + A_CORE**2) - m/max(r, R_SHELL)
chk("concentric selftest: Phi(1) at m=5e-3", phi(1.0, 5e-3), 4.9750e-3, 1e-6)
chk("concentric selftest: |Phi(1000)| < 1e-10 at m=5e-3", abs(phi(1000.0, 5e-3)) < 1e-10, True)
# DISCREPANCY (recorded, not repaired, not a failure of the theorem or the rederivation):
print("     concentric.py:50-51 header quotes Phi(1000) = -6.2e-13 and Phi(1) = +4.4e-3 with no m stated.")
print("     at m=5e-3, a=0.02, R_s=200: Phi(1) = %.4e, Phi(1000) = %.4e (= -m a^2/(2 r^3))" % (phi(1.0,5e-3), phi(1000.0,5e-3)))
print("     neither header figure is reproduced by the seated pins; the selftest pins (4.9750e-3, |.|<1e-10) ARE.")
chk("header Phi(1000)=-6.2e-13 reproduced by seated pins? (discrepancy, recorded)", abs(phi(1000.0,5e-3) + 6.2e-13) < 1e-14, False)
chk("header Phi(1)=+4.4e-3 reproduced by seated pins? (discrepancy, recorded)", abs(phi(1.0, 5e-3) - 4.4e-3) < 1e-6, False)
# which m gives Phi(1) = 4.4e-3?  Phi(1)/m = 1/sqrt(1+a^2) - 1/R_s
k = 1/math.sqrt(1 + A_CORE**2) - 1/R_SHELL
print("     Phi(1)/m = %.6f ; header 4.4e-3 needs m = %.4e, selftest 4.9750e-3 needs m = %.4e"
      % (k, 4.4e-3/k, 4.9750e-3/k))
print("     -> header and selftest differ (m ~ 4.42e-3 vs 5e-3): a DISCREPANCY in the owner's prose, not in the theorem")
bad = lambda r: 5e-3/math.sqrt(r*r + A_CORE**2) - 5e-3/R_SHELL
chk("Error-1 witness |bad(1000)| > 1e-6 (bare -m monopole)", abs(bad(1000.0)) > 1e-6, True)
chk("  bad(r) -> -m/R_s + m/r: at r=1000, value", bad(1000.0), 5e-3/1000 - 5e-3/200, 1e-12)
print("     note: bad(r) has 1/r coefficient +m, i.e. ADM mass -m in the Phi = -M/r convention, but ALSO")
print("     tends to the constant -m/R_s, so it is not asymptotically flat at all -- the 'ADM mass -m' reading")
print("     needs the constant subtracted; recorded, not repaired.")

print("\nB. ADM mass of the seated potential, symbolically (far field r >= R_s)")
r, m, aa, Rs = sp.symbols('r m a R_s', positive=True)
Phi_out = m/sp.sqrt(r**2 + aa**2) - m/r
series = sp.series(Phi_out, r, sp.oo, 4).removeO()
print("     Phi(r) for r >= R_s = ", sp.simplify(series))
coef_1r = sp.limit(Phi_out * r, r, sp.oo)
chk("1/r coefficient of Phi outside the shell (M_ADM in Newtonian reading)", coef_1r == 0, True)
print("     leading term is -m a^2/(2 r^3): a pure quadrupole-order tail, no monopole -> M_ADM = 0 EXACTLY")
# certify's conformastatic metric: g_tt = -e^{2Phi}, g_ij = e^{-2Phi} delta_ij.
# ADM mass of e^{-2Phi} delta: M_ADM = -lim r*Phi (in G=c=1, Phi -> -M/r).  Same coefficient.
chk("conformastatic ADM mass = -lim r Phi = 0", sp.limit(-r*Phi_out, r, sp.oo) == 0, True)

print("\nC. linearised density of the seated potential: rho = Lap Phi / (4 pi)  (G=1)")
Phi_in = m/sp.sqrt(r**2 + aa**2) - m/Rs           # r < R_s: shell constant
lap = sp.simplify(sp.diff(r**2*sp.diff(Phi_in, r), r)/r**2)
rho_in = sp.simplify(lap/(4*sp.pi))
print("     rho(r < R_s) =", rho_in)
chk("rho inside the shell is negative for every r > 0 (core is Plummer with mass -m... sign)", 
    sp.simplify(rho_in.subs({m: 1, aa: 1, r: 1})) < 0, True)
# Plummer: Lap(m/sqrt(r^2+a^2)) = -3 m a^2/(r^2+a^2)^{5/2}  -> rho = -3 m a^2 /(4 pi (r^2+a^2)^{5/2}) < 0 for m > 0
tot_core = sp.integrate(4*sp.pi*r**2*rho_in, (r, 0, sp.oo))
chk("integral of the core density = -m (the core carries mass -m)", sp.simplify(tot_core + m) == 0, True)
print("     so with Phi > 0 chosen (m > 0), the core has rho < 0 everywhere: the DEC's rho >= 0 fails at every r < R_s.")
print("     The shell at R_s carries +m as a delta function; total = 0.  Consistent with certify.py:84-85 'DEC VIOLATED'.")

print("\nD/E. propositional shape of the four uses, z3")
try:
    import z3
except ImportError:
    print("     z3 not installed -- pip install z3-solver"); sys.exit(1)
AF, DEC, COMP, MINK = z3.Bools('AF DEC COMP MINK')
M = z3.Real('M')
PMT = z3.Implies(z3.And(AF, DEC, COMP), z3.And(M >= 0, z3.Implies(M == 0, MINK)))
# (i) with DEC false, is M < 0 consistent with the theorem?  (a 'bare negative mass' whose matter violates the DEC)
s = z3.Solver(); s.add(PMT, AF, COMP, z3.Not(DEC), M < 0)
res = s.check(); chk("PMT & AF & complete & NOT DEC & M<0 : SAT (theorem silent on bare negative DEC-violating mass)", str(res), "sat")
print("     model:", s.model())
# (ii) with DEC true, M < 0 is refuted
s = z3.Solver(); s.add(PMT, AF, COMP, DEC, M < 0)
chk("PMT & AF & complete & DEC & M<0 : UNSAT (this is what the theorem forbids)", str(s.check()), "unsat")
# (iii) M = 0, not Minkowski, DEC true : UNSAT -> rigidity forces DEC failure for the seated device (pair.py / concentric.py:51-53)
s = z3.Solver(); s.add(PMT, AF, COMP, DEC, M == 0, z3.Not(MINK))
chk("PMT & AF & complete & DEC & M=0 & NOT Minkowski : UNSAT (rigidity)", str(s.check()), "unsat")
# (iv) M = 0, DEC false, not Minkowski : SAT -- the seated device's actual situation; theorem says nothing
s = z3.Solver(); s.add(PMT, AF, COMP, z3.Not(DEC), M == 0, z3.Not(MINK))
chk("PMT & AF & complete & NOT DEC & M=0 & NOT Minkowski : SAT (the seated device; theorem vacuous)", str(s.check()), "sat")
# (v) Is 'M >= 0' DERIVABLE for the seated device from PMT?  Ask: PMT & NOT DEC & M<0 -- already SAT in (i): so no.
print("     => 'the inequality is satisfied' (concentric:49-50) is a fact about the device's M_ADM, not a")
print("        consequence the theorem licenses; 'forbidden by the positive mass theorem' (phase1:397-399,")
print("        concentric:7-8) is NOT derivable from the theorem for a DEC-violating negative mass.")

print("\nSUMMARY: %s" % ("OK" if ok else "FAILED (see rows)"))
sys.exit(0 if ok else 1)
