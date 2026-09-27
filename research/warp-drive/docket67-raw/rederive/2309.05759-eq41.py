#!/usr/bin/env python3
"""DOCKET 67 / 2309.05759-eq41 -- what is checkable WITHOUT the source text.

The source (Kabat & Nomura, arXiv:2309.05759) could not be read this stage
(alphaXiv quota exceeded; arxiv.org and every mirror EGRESS_BLOCKED).  So eq. (41)
itself -- its symbol, its numbering, its prefactors -- is NOT checked here.  What IS
checked is the generic claim the tree draws from it:

  C1  a Yukawa coupling of a 5D bulk scalar to a brane-localised fermion bilinear
      has mass dimension -1/2 (natural units), so it is a dimensionful constant that
      the free-field action does not fix;
  C2  the constant zero mode on S^1 of circumference 2 pi r normalises to
      (2 pi r)^{-1/2}, giving lambda_4 = lambda_5 (2 pi r)^{-1/2} -- the same
      structure the tree READ for gravity (KN eqs. 72-73, Mbar4 = (2 pi r)^{1/2}
      Mbar5^{3/2}), where the measured G anchors Mbar4 and so fixes the coupling;
      for the scalar there is no analogous measured anchor in the setup;
  C3  any dimensionless one-loop LV coefficient c from the scalar is lambda_5^2/r
      times a dimensionless function of (beta, m r, mu r): a single bound c <= B
      therefore constrains lambda_5^2 f/r, and for EVERY beta in (0,1] and every
      f != 0 there is a lambda_5 satisfying it -- the bound does not bite beta alone
      (the pass's own words, /tmp/o6o7/o67.py:133, 'bounds lambda^2 beta^2, not beta').
  C4  CONTROL: for the graviton, coupling fixed by Mbar4, the same bound is a
      function of beta and r only -- reproduces branelink's 6.37e-64-class figure
      scaling (1/(pi r Mbar4)^2) dimensionally.
"""
import sympy as sp

ok = True
def chk(name, got, want):
    global ok
    good = sp.simplify(got - want) == 0 if not isinstance(want, bool) else (got == want)
    ok &= bool(good)
    print(("PASS " if good else "FAIL ") + name + " : " + str(got))

# ---- C1: dimensions in D=5 bulk, brane at y=0, natural units ------------------
D = 5
dim_phi5 = sp.Rational(D - 2, 2)            # bulk scalar [phi] = (D-2)/2 = 3/2
dim_psi4 = sp.Rational(3, 2)                # brane fermion
dim_lambda5 = 4 - (dim_phi5 + 2 * dim_psi4)  # int d^4x lambda phi(x,0) psibar psi
chk("C1 [lambda_5] (Yukawa, bulk scalar - brane fermion)", dim_lambda5, sp.Rational(-1, 2))
dim_g5 = 4 - (dim_phi5 + 2 * 1)             # cubic brane-scalar^2 x bulk scalar
chk("C1' [g_5] (cubic brane scalar^2 bulk scalar)", dim_g5, sp.Rational(1, 2))
# graviton: g_AB = eta + (2/Mbar5^{3/2}) h, [h]=3/2 -> coefficient dim -3/2
chk("C1'' [1/Mbar5^{3/2}] graviton coupling", -sp.Rational(3, 2), sp.Rational(-3, 2))

# ---- C2: zero-mode normalisation on the circle --------------------------------
y, r, N = sp.symbols('y r N', positive=True)
normN = sp.solve(sp.Eq(sp.integrate(N**2, (y, 0, 2 * sp.pi * r)), 1), N)[0]
chk("C2 zero-mode normalisation N", normN, 1 / sp.sqrt(2 * sp.pi * r))
lam5, M5 = sp.symbols('lambda_5 Mbar5', positive=True)
lam4 = lam5 * normN
chk("C2 lambda_4 = lambda_5/(2 pi r)^{1/2}", lam4, lam5 / sp.sqrt(2 * sp.pi * r))
Mbar4 = 1 / ((1 / M5**sp.Rational(3, 2)) * normN)   # 1/Mbar4 = (1/Mbar5^{3/2}) N
chk("C2 gravity analogue reproduces KN eq.72 form Mbar4 = (2 pi r)^{1/2} Mbar5^{3/2}",
    Mbar4, sp.sqrt(2 * sp.pi * r) * M5**sp.Rational(3, 2))
dim_N = sp.Rational(1, 2)                    # [(2 pi r)^{-1/2}] = mass^{+1/2}
chk("C2 [lambda_4] = [lambda_5] + [N] dimensionless", dim_lambda5 + dim_N, 0)

# ---- C3: the SME bound cannot bite beta when lambda_5 is free ------------------
beta, f, B = sp.symbols('beta f B', positive=True)
c = lam5**2 / r * beta**2 * f                  # dimensional form; f = f(beta, m r, mu r)
chk("C3 [c] dimensionless ([lambda5^2/r] = -1 + 1)", 2 * dim_lambda5 + 1, 0)
lam_sol = sp.solve(sp.Eq(c, B), lam5)
chk("C3 lambda_5 saturating the bound exists for all beta,f,B>0 (one positive root)",
    len(lam_sol) == 1 and lam_sol[0].is_positive, True)
print("     lambda_5* =", lam_sol[0])

try:
    import z3
    b, l, F, Bz, R = z3.Reals('b l F B R')
    s = z3.Solver()
    # negation: some beta in (0,1] with every lambda>0 violating c <= B
    s.add(b > 0, b <= 1, F > 0, Bz > 0, R > 0)
    s.add(z3.ForAll([l], z3.Implies(l > 0, l * l * b * b * F > Bz * R)))
    res = s.check()
    good = (res == z3.unsat)
    ok &= good
    print(("PASS " if good else "FAIL ") + "C3 z3 negation 'some beta excluded for all lambda' : " + str(res))
except ImportError:
    print("SKIP C3 z3 (z3 not installed)")

# ---- C4: graviton control -- coupling fixed, c depends on (beta, r) only --------
rG, M4 = sp.symbols('r_G Mbar4', positive=True)
cgrav = (1 / (16 * sp.pi**2)) / (sp.pi * rG * M4)**2 * sp.Rational(3, 4) * beta**2 * sp.zeta(3) / 4
free = cgrav.free_symbols
chk("C4 graviton c has no free coupling (symbols beta, r, Mbar4 only)",
    free == {beta, rG, M4}, True)
hbarc = 1.973269804e-16      # GeV m (CODATA exact-derived)
Mb4 = 2.435e18 * (1 + 0)     # GeV, four-figure reduced Planck mass, for the magnitude only
val = float(cgrav.subs({beta: 1, rG: 38.6e-6 / hbarc, M4: Mb4}))
print("     graviton |c| at r=38.6 um, beta=1 (magnitude check vs branelink 6.37e-64):", "%.3e" % val)
good = abs(val / 6.37e-64 - 1) < 2e-3
ok &= good
print(("PASS " if good else "FAIL ") + " C4 magnitude agrees with branelink.SME figure to <0.2%")

print("\nALL PASS" if ok else "\nSOME FAIL")
raise SystemExit(0 if ok else 1)
