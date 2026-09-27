#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of the Friedmann equations as permute.py uses them.

Source (READ-VIA-RESTATEMENT): Carroll gr-qc/9712019 eqs (8.13), (8.20)-(8.23),
(8.29)-(8.36); Ellis & van Elst gr-qc/9812046v5 p.22 sec 4.2 eqs (106)-(107):
'Any two of these equations imply the third if Sdot != 0 (the latter equation
being a first integral of the other two).'

Tree use: research/warp-drive/permute.py:115-120 (claim), 279-321 (code).
Read-only: permute.py is imported without writing bytecode; nothing under
research/ is written.
"""
import sys, math, random, importlib.util
sys.dont_write_bytecode = True
import sympy as sp

RESULTS = []
def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok)))
    print("%-4s %s  %s" % ("PASS" if ok else "FAIL", name, detail))

t = sp.symbols('t', real=True)
r, th, ph = sp.symbols('r theta phi', real=True)
k, w, G = sp.symbols('k w G', real=True)
a = sp.Function('a')(t)
ad, add = sp.diff(a, t), sp.diff(a, t, 2)

# ---------------- C1: Einstein tensor of FLRW (-+++), from the metric ----------
x = [t, r, th, ph]
g = sp.diag(-1, a**2/(1 - k*r**2), a**2*r**2, a**2*r**2*sp.sin(th)**2)
gi = g.inv()
n = 4
Gam = [[[sp.simplify(sum(gi[l, s]*(sp.diff(g[s, m], x[nn]) + sp.diff(g[s, nn], x[m])
         - sp.diff(g[m, nn], x[s])) for s in range(n))/2) for nn in range(n)]
         for m in range(n)] for l in range(n)]
def Riem(rho, sig, mu, nu):
    e = sp.diff(Gam[rho][nu][sig], x[mu]) - sp.diff(Gam[rho][mu][sig], x[nu])
    e += sum(Gam[rho][mu][l]*Gam[l][nu][sig] - Gam[rho][nu][l]*Gam[l][mu][sig] for l in range(n))
    return e
Ric = sp.Matrix(n, n, lambda m, nn: sp.simplify(sum(Riem(l, m, l, nn) for l in range(n))))
R = sp.simplify(sum(gi[m, nn]*Ric[m, nn] for m in range(n) for nn in range(n)))
Ein = sp.simplify(Ric - R*g/2)
Emix = sp.simplify(gi*Ein)            # G^mu_nu
check("C1a R_00 = -3 addot/a (Carroll 8.13)", sp.simplify(Ric[0, 0] + 3*add/a) == 0)
check("C1b R = 6(a addot + adot^2 + k)/a^2 (Carroll 8.14)",
      sp.simplify(R - 6*(a*add + ad**2 + k)/a**2) == 0)
G00 = sp.simplify(-Emix[0, 0])         # = 8 pi G rho
Gii = sp.simplify(Emix[1, 1])          # = 8 pi G p
check("C1c G^0_0 = -3(H^2 + k/a^2)", sp.simplify(G00 - 3*(ad**2/a**2 + k/a**2)) == 0)
check("C1d G^1_1 = G^2_2 = G^3_3 = -(2 addot/a + H^2 + k/a^2)",
      all(sp.simplify(Emix[i, i] + (2*add/a + ad**2/a**2 + k/a**2)) == 0 for i in (1, 2, 3)))
rho, p = sp.symbols('rho p', real=True)
# Friedmann pair from G^mu_nu = 8 pi G T^mu_nu, T = diag(-rho, p, p, p)
H2 = sp.solve(sp.Eq(G00, 8*sp.pi*G*rho), ad**2)[0]
acc = sp.solve(sp.Eq(Gii, 8*sp.pi*G*p).subs(ad**2, H2), add)[0]
check("C1e constraint: H^2 = (8piG/3) rho - k/a^2 (Carroll 8.36)",
      sp.simplify(H2/a**2 - (8*sp.pi*G*rho/3 - k/a**2)) == 0)
check("C1f acceleration: addot/a = -(4piG/3)(rho + 3p) (Carroll 8.35)",
      sp.simplify(acc/a + 4*sp.pi*G*(rho + 3*p)/3) == 0)
# units 8 pi G / 3 = 1  ->  4 pi G / 3 = 1/2 : the tree's _accel = -0.5 (rho + 3 w rho) a
Gunit = sp.Rational(3, 8)/sp.pi
check("C1g units 8piG/3=1 give addot = -(1/2)(rho+3p) a  == permute._accel coefficient",
      sp.simplify(acc.subs(G, Gunit) + sp.Rational(1, 2)*(rho + 3*p)*a) == 0)
# Lambda as the w = -1 fluid (Carroll 8.29-8.31)
L = sp.symbols('Lambda', real=True)
H2L = sp.solve(sp.Eq(G00, 8*sp.pi*G*rho + L), ad**2)[0]
check("C1h Lambda-term == fluid with rho_v = -p_v = Lambda/(8 pi G)",
      sp.simplify(H2L - H2.subs(rho, rho + L/(8*sp.pi*G))) == 0)

# ---------------- C2: the FLRW reduction of the contracted Bianchi identity ---------
# nabla_mu G^mu_0 for arbitrary a(t), no field equation used
div0 = sum(sp.diff(Emix[m, 0], x[m]) for m in range(n))
div0 += sum(Gam[m][m][l]*Emix[l, 0] for m in range(n) for l in range(n))
div0 -= sum(Gam[l][m][0]*Emix[m, l] for m in range(n) for l in range(n))
check("C2a nabla_mu G^mu_0 == 0 identically for arbitrary a(t), k", sp.simplify(div0) == 0)
rhoG, pG = G00/(8*sp.pi*G), Gii/(8*sp.pi*G)
check("C2b rho_G := G^0_0-part, p_G := G^i_i-part satisfy rho_G' + 3H(rho_G + p_G) == 0 (any a(t))",
      sp.simplify(sp.diff(rhoG, t) + 3*ad/a*(rhoG + pG)) == 0)

# ---------------- C3: the tree's direction, as an algebraic identity -------------
A, Ad, K, W, P = sp.symbols('A Ad K W P', real=True)
rho_c = (Ad/A)**2 + K/A**2                      # permute._rho
Add = -sp.Rational(1, 2)*(rho_c + 3*W*rho_c)*A    # permute._accel
Hs = Ad/A
rhodot_tree = 2*Hs*(Add/A - Hs**2) - 2*K*Ad/A**3  # permute.continuity_residual
rhodot_true = sp.diff(rho_c, A)*Ad + sp.diff(rho_c, Ad)*Add   # chain rule along the flow
check("C3a tree's rhodot formula == chain-rule d/dt of the constraint",
      sp.simplify(rhodot_tree - rhodot_true) == 0)
resid = sp.simplify(rhodot_true + 3*Hs*(rho_c + W*rho_c))
check("C3b constraint + acceleration  =>  continuity, IDENTICALLY in (a, adot, k, w)",
      resid == 0, "residual = %s" % resid)
AddP = -sp.Rational(1, 2)*(rho_c + 3*P)*A
residP = sp.simplify(sp.diff(rho_c, A)*Ad + sp.diff(rho_c, Ad)*AddP + 3*Hs*(rho_c + P))
check("C3c ... for ANY pressure P (not only p = w rho, constant w)", residP == 0)
check("C3d no Hdot != 0 / adot != 0 condition is needed in this direction (residual has no division by adot)",
      resid == 0 and residP == 0)

# ---------------- C4: the other two directions (Ellis-van Elst 'any two imply the third if Sdot != 0')
rr = sp.Function('r')(t)
# R + E => F as first integral: d/dt [adot^2 - rho a^2] = 0
E_rhodot = -3*ad/a*(1 + w)*rr
R_add = -sp.Rational(1, 2)*(1 + 3*w)*rr*a
Q = ad**2 - rr*a**2
dQ = sp.diff(Q, t).subs({sp.diff(rr, t): E_rhodot}).subs({add: R_add})
check("C4a acceleration + continuity  =>  d/dt(adot^2 - rho a^2) = 0 (constraint is a first integral, constant = -k)",
      sp.simplify(dQ) == 0)
# F + E => R needs adot != 0: static counterexample
a0, kk, ww = sp.Rational(1), sp.Rational(1, 4), sp.Rational(1, 3)
rho_s = kk/a0**2
F_ok = (0 - (rho_s - kk/a0**2)) == 0
E_ok = True   # rhodot = 0 = -3*0*(rho+p)
R_ok = (0 == -sp.Rational(1, 2)*(rho_s + 3*ww*rho_s)*a0)
check("C4b constraint + continuity do NOT imply acceleration at adot = 0 (static a=1, k=1/4, w=1/3: F,E hold, R fails)",
      F_ok and E_ok and not R_ok, "addot required = %s != 0" % (-sp.Rational(1, 2)*(rho_s + 3*ww*rho_s)*a0))
# F + E => R when adot != 0
lhs = sp.diff(ad**2/a**2 + k/a**2 - rr, t).subs(sp.diff(rr, t), E_rhodot).subs(rr, ad**2/a**2 + k/a**2)
sol = sp.solve(sp.Eq(lhs, 0), add)
check("C4c constraint + continuity  =>  acceleration when adot != 0 (unique solution for addot)",
      len(sol) == 1 and sp.simplify(sol[0] + sp.Rational(1, 2)*(1 + 3*w)*(ad**2/a**2 + k/a**2)*a) == 0,
      "factor adot appears: %s" % sp.factor(sp.simplify(lhs)).has(ad))

# ---------------- C5: z3 -- no real counterexample, built from the RAW tree formulas
# (not from a sympy-simplified residual, which would be vacuous), with a vacuity guard.
try:
    import z3
    def z3_resid(coef):
        a_, ad_, k_, p_ = z3.Reals('a ad k p')
        H_ = ad_/a_
        rho_ = H_*H_ + k_/(a_*a_)                 # permute._rho
        add_ = -coef*(rho_ + 3*p_)*a_             # permute._accel with p free
        rhodot_ = 2*H_*(add_/a_ - H_*H_) - 2*k_*ad_/(a_*a_*a_)
        return (a_, ad_, k_, p_), rhodot_ + 3*H_*(rho_ + p_)
    (a_, ad_, k_, p_), e = z3_resid(z3.RealVal(1)/2)
    s = z3.Solver(); s.add(a_ > 0, e != 0); res = s.check()
    (b_, bd_, l_, q_), e2 = z3_resid(z3.RealVal(49)/100)
    s2 = z3.Solver(); s2.add(b_ > 0, e2 != 0); res2 = s2.check()
    check("C5a z3: exists a>0, adot, k, p with continuity residual != 0 ?  -> unsat", res == z3.unsat, "z3 %s" % res)
    check("C5b vacuity guard: coefficient 0.49 in place of 1/2 -> sat (encoding can fail)", res2 == z3.sat,
          "z3 %s" % res2)
except ImportError:
    check("C5 z3 available", False, "pip install z3-solver")

# ---------------- C6: the tree's own numerics (read-only import) ---------------
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
spec = importlib.util.spec_from_file_location(
    "permute_ro", "/home/user/Claude-Method-Works/research/warp-drive/permute.py")
pm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pm)
worst_all = 0.0
for ww_ in (1/3, 0.0, -1.0, -1/3):
    for kk_ in (0.0, 0.25, -0.25):
        v = pm.worst_continuity_residual(ww_, kk_)
        worst_all = max(worst_all, v)
check("C6a tree fixture (4 fluids x 3 k): worst scaled residual at rounding level", worst_all < 1e-13,
      "worst = %.3e" % worst_all)
c5, c80 = pm.worst_continuity_residual(1/3, 0.25, steps=500), pm.worst_continuity_residual(1/3, 0.25, steps=8000)
check("C6b flat in dt (500 vs 8000 steps), as permute.py:118-120 says", pm.residual_is_step_independent(),
      "500: %.3e  8000: %.3e" % (c5, c80))
# Named qualifier: the flatness evidences a POINTWISE algebraic identity; it is
# equally flat off any trajectory, so it says nothing about the integrator.
random.seed(67)
off = 0.0
for _ in range(20000):
    A_ = random.uniform(0.05, 20.0); Ad_ = random.uniform(-10, 10)
    k_ = random.uniform(-1, 1); w_ = random.uniform(-2, 2)
    sc = abs(3*(Ad_/A_)*pm._rho(A_, Ad_, k_))
    if sc < 1e-12:
        continue
    off = max(off, abs(pm.continuity_residual(A_, Ad_, k_, w_))/sc)
check("C6c residual is equally at rounding level at 20000 RANDOM phase-space points (no integration at all)",
      off < 1e-12, "worst = %.3e" % off)

nfail = sum(1 for _, ok in RESULTS if not ok)
print("\n%d checks, %d failed -> %s" % (len(RESULTS), nfail, "ALL PASS" if nfail == 0 else "FAILURES"))
sys.exit(1 if nfail else 0)
