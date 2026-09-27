#!/usr/bin/env python3
import sys; sys.dont_write_bytecode = True
"""D67 re-derivation: flrw-perfect-fluid-first-law (permute.py:79-85, 248-274, 434-440).
Reads permute.py READ-ONLY (imports it by path); writes nothing.  Exits 1 on any failed check."""
import sys, importlib.util
import sympy as sp

FAIL = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ((" -- " + detail) if detail else ""))
    if not ok: FAIL.append(name)

t, r, th, ph = sp.symbols('t r theta phi')
k = sp.Symbol('k')
a = sp.Function('a')(t); rho = sp.Function('rho')(t); p = sp.Function('p')(t)
X = [t, r, th, ph]
# (1) nabla_mu T^{mu nu} = 0 for a perfect fluid on FLRW (any k), signature (-+++)
g = sp.diag(-1, a**2/(1-k*r**2), a**2*r**2, a**2*r**2*sp.sin(th)**2)
gi = g.inv()
Gam = [[[sp.simplify(sum(gi[l, s]*(sp.diff(g[s, m], X[n]) + sp.diff(g[s, n], X[m]) - sp.diff(g[m, n], X[s]))
         for s in range(4))/2) for n in range(4)] for m in range(4)] for l in range(4)]
u = [1, 0, 0, 0]
T = sp.Matrix(4, 4, lambda m, n: (rho+p)*u[m]*u[n] + p*gi[m, n])
div = [sp.simplify(sum(sp.diff(T[m, n], X[m]) for m in range(4))
       + sum(Gam[m][m][l]*T[l, n] for m in range(4) for l in range(4))
       + sum(Gam[n][m][l]*T[m, l] for m in range(4) for l in range(4))) for n in range(4)]
H = sp.diff(a, t)/a
cont = sp.diff(rho, t) + 3*H*(rho+p)
chk("(1) nabla_mu T^{mu 0} = rho' + 3H(rho+p) for every k", sp.simplify(div[0] - cont) == 0, str(sp.simplify(div[0])))
chk("(1b) spatial components vanish identically (homogeneity)", all(sp.simplify(div[i]) == 0 for i in (1, 2, 3)))
# (2) equivalent to d(rho a^3) = -p d(a^3)
first = sp.diff(rho*a**3, t) + p*sp.diff(a**3, t)
chk("(2) d(rho a^3)/dt + p d(a^3)/dt == a^3 (rho' + 3H(rho+p))", sp.simplify(first - a**3*cont) == 0)
# (2b) continuity also follows from the two Friedmann equations (Baumann 0907.5424 eqs 21-23)
rhoF = 3*(H**2 + k/a**2)
pF = -(2*sp.diff(a, t, 2)/a + H**2 + k/a**2)
chk("(2b) Friedmann (21)+(22) imply continuity (Bianchi) for every k",
    sp.simplify(sp.diff(rhoF, t) + 3*H*(rhoF+pF)) == 0)
# (3) constant w: rho a^{3(1+w)} = const solves it, exactly, symbolically
A, w, r0 = sp.symbols('A w rho0', positive=True)
w = sp.Symbol('w', real=True)
rA = r0*A**(-3*(1+w))
res = sp.diff(rA*A**3, A) + w*rA*sp.diff(A**3, A)
chk("(3) d(rho a^3) + w rho d(a^3) == 0 exactly for rho = rho0 a^{-3(1+w)}, all real w", sp.simplify(res) == 0)
f = sp.Function('f')
sol = sp.dsolve(sp.Eq(sp.diff(f(A), A), -3*(1+w)*f(A)/A), f(A))
chk("(3b) dsolve of d rho/d a = -3(1+w) rho/a gives C a^{-3(1+w)}", sp.simplify(sol.rhs*A**(3*(1+w))).free_symbols <= {sp.Symbol('C1')}, str(sol))
# (3c) constant-w hypothesis is load-bearing: CPL w(a) = w0 + wa(1-a) -> rho a^{3(1+w0)} NOT const
w0, wa = sp.symbols('w0 wa', real=True)
wA = w0 + wa*(1-A)
rhoCPL = A**(-3*(1+w0+wa))*sp.exp(-3*wa*(1-A))
chk("(3c) CPL rho(a) solves continuity with w(a)", sp.simplify(sp.diff(rhoCPL, A) + 3*(1+wA)*rhoCPL/A) == 0)
chk("(3c') but rho a^{3(1+w0)} is not constant when wa != 0",
    sp.simplify(sp.diff(rhoCPL*A**(3*(1+w0)), A).subs({w0: -0.752, wa: -0.86, A: sp.Rational(1, 2)})) != 0)
# (4) dS = 0 needs the Gibbs relation T dS = dE + p dV - mu dN with dN = 0 (or mu = 0): radiation
Tt = sp.Function('T')(t); c = sp.Symbol('c', positive=True)
rho_r = c*Tt**4; p_r = rho_r/3; s_r = (rho_r + p_r)/Tt
Tsol = sp.Symbol('T0', positive=True)/a
contR = (sp.diff(rho_r, t) + 3*H*(rho_r+p_r)).subs(Tt, Tsol).doit()
chk("(4) radiation: T = T0/a solves continuity", sp.simplify(contR) == 0)
chk("(4b) and then s a^3 = const (dS = 0)", sp.simplify(sp.diff((s_r*a**3).subs(Tt, Tsol).doit(), t)) == 0)
# (4c) with mu dN != 0 the same continuity does NOT give dS = 0: T dS = mu dN
mu, dN, dE, dV, P = sp.symbols('mu dN dE dV P')
TdS = dE + P*dV - mu*dN
chk("(4c) continuity (dE = -p dV) leaves T dS = -mu dN -- zero only if mu dN = 0",
    sp.simplify(TdS.subs(dE, -P*dV) + mu*dN) == 0)
# (5) hypothesis 'perfect fluid' is load-bearing: bulk viscosity p -> p - 3 zeta H (Weinberg 1971)
zeta, Tq, n = sp.symbols('zeta T n', positive=True)
# with p_eff: d(rho a^3) = -(p - 3 zeta H) d(a^3)  ->  T dS = d(rho a^3) + p d(a^3) = 3 zeta H d(a^3)
Hs = sp.Symbol('H', positive=True); aS = sp.Symbol('a', positive=True)
dSdt = 3*zeta*Hs*(3*aS**2*aS*Hs)/Tq     # d(a^3)/dt = 3 a^3 H
chk("(5) bulk viscosity: T dS/dt = 9 zeta H^2 a^3 > 0 (expansion DOES dissipate)", sp.simplify(dSdt*Tq - 9*zeta*Hs**2*aS**3) == 0 and dSdt.is_positive)
# (6) two perfect fluids exchanging energy (dust decaying to radiation, rate Gamma): total conserved, S_r grows
G = sp.Symbol('Gamma', positive=True); rm = sp.Symbol('rho_m', positive=True); rr = sp.Symbol('rho_r', positive=True)
drm = -3*Hs*rm - G*rm; drr = -4*Hs*rr + G*rm
chk("(6) total rho_m + rho_r obeys continuity with p = rho_r/3", sp.simplify(drm + drr + 3*Hs*(rm + rr + rr/3)) == 0)
# radiation entropy S_r = (4/3) rho_r a^3 / T:  T dS_r/dt = d(rho_r a^3)/dt + p_r d(a^3)/dt = Gamma rho_m a^3
TdSr = (drr*aS**3 + rr*3*aS**2*aS*Hs) + (rr/3)*3*aS**3*Hs
chk("(6b) T dS_r/dt = Gamma rho_m a^3 > 0: entropy produced although each fluid is 'perfect'", sp.simplify(TdSr - G*rm*aS**3) == 0)
# (7) the tree's own labels: which w gives a^-2 (curvature)?
for wv, exp_ in ((sp.Rational(1, 3), -4), (0, -3), (-1, 0), (-sp.Rational(1, 3), -2), (-sp.Rational(2, 3), -1)):
    print("      w = %-5s -> rho ~ a^%s" % (wv, -3*(1+wv)))
chk("(7) curvature term k/a^2 corresponds to w = -1/3, NOT -2/3 (w=-2/3 is a^-1, domain-wall-like)",
    -3*(1 + sp.Rational(-1, 3)) == -2 and -3*(1 + sp.Rational(-2, 3)) == -1)
rk = -3*k/aS**2; pk_needed = sp.Symbol('pk')
pk = sp.solve(sp.diff(rk, aS)*aS*Hs + 3*Hs*(rk + pk_needed), pk_needed)[0]
chk("(7b) -3k/a^2 read as a fluid has p = -rho/3", sp.simplify(pk - (-rk/3)) == 0)
# (8) run the tree's own fixtures, read-only, and quantify 'machine precision'
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("permute", "/home/user/Claude-Method-Works/research/warp-drive/permute.py")
pm = importlib.util.module_from_spec(spec)
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(pm)
worst = 0.0
for wv, name in ((1/3, "radiation"), (0.0, "dust"), (-1.0, "vacuum"), (-2/3, "tree label 'curvature-like'")):
    resid = pm.first_law_residual(1.3, wv); scale = abs(pm.rho_of_a(1.3, wv))*3*1.3**2
    worst = max(worst, abs(resid)/scale)
    print("      %-28s residual %.3e  relative %.3e  is_isentropic=%s" % (name, resid, abs(resid)/scale, pm.is_isentropic(wv)))
chk("(8) tree fixtures pass at tol 1e-9", all(pm.is_isentropic(x) for x in (1/3, 0.0, -1.0, -2/3)))
print("      worst relative residual %.1e vs double eps 2.2e-16: finite-difference (h=1e-6) truncation+roundoff, not 'machine precision'" % worst)
# (8b) tautology: the check passes ANY w used consistently, and fails a mismatched rho -- it tests the solution against its own equation
def resid_mismatch(aa, w_rho, w_p, h=1e-6):
    e = lambda x: pm.rho_of_a(x, w_rho)*x**3
    return ((e(aa+h)-e(aa-h))/(2*h) + w_p*pm.rho_of_a(aa, w_rho)*((aa+h)**3-(aa-h)**3)/(2*h))
chk("(8b) residual is O(1) when rho(a) is not the continuity solution for the stated p (w_rho=0, w_p=1/3)",
    abs(resid_mismatch(1.3, 0.0, 1/3)) > 0.1, "%.3f" % resid_mismatch(1.3, 0.0, 1/3))
chk("(8c) and ~0 for an arbitrary w used consistently (w=5.7): no physics is measured, only the identity",
    abs(pm.first_law_residual(1.3, 5.7)) <= 1e-9*abs(pm.rho_of_a(1.3, 5.7))*3*1.3**2*max(1, 1))
print("\n%d checks failed" % len(FAIL) if FAIL else "\nALL CHECKS PASS")
sys.exit(1 if FAIL else 0)
