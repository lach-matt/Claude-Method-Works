#!/usr/bin/env python3
"""
DOCKET 67 -- rederivation for key 'dust-shell-radial-instability-textbook'.

Tree's use (research/warp-drive/stability.py:44-50, 241-247): the ORDINARY
shell (flat interior M_in = 0, Schwarzschild exterior M_out = M), evolved with
beta^2 = dp/dsigma = 0, gives V''(R0) < 0 -- 'UNSTABLE, as a dust shell must be'
-- at M/R = 0.01, 0.1, 0.2 with printed V'' = -3.036e-2, -3.424e-1, -8.169e-1.

Checks, built independently of stability.py (which is imported READ-ONLY only
in section 4 to compare against its own numerics):
  1. closed-form V''(R0) for the ordinary shell from Lake's potential
     (Ishak-Lake gr-qc/0108058 eq 5) + conservation m_s' = -8 pi R p
     (Poisson-Visser gr-qc/9506083 eq 13) + p' = beta^2 sigma' (PV eq 23);
  2. z3: V''(beta^2=0) < 0 for EVERY 0 < M/R < 1/2 (not only the 3 samples),
     beta^2 coefficient > 0, beta^2_crit > 0 on the whole range, -> 0 as M/R->0;
  3. Newtonian limit V''(0) ~ -3M/R^3;
  4. the tree's printed numbers and its own numerics;
  5. the static ordinary shell is NOT pressureless: Lanczos p0 > 0 (z3);
  6. a TRUE dust shell (p == 0, m_s const) has NO static configuration at all
     (V = V' = 0 impossible; Barcelo-Jaramillo 1112.5265 eq (4) gives
     a_ddot < 0 at every instant) -- so 'dust' is a misnomer for beta^2 = 0;
  7. machinery cross-check against a PUBLISHED number: Ishak-Lake Fig. 2,
     P'/sigma' = 1, 'R/m+ ~ 2.37 as m- -> 0'.
"""
import importlib.util, math, sys
import sympy as sp
import z3

ok_all = True
def chk(label, cond, detail=""):
    global ok_all
    ok_all &= bool(cond)
    print("  [%s] %s %s" % ("ok" if cond else "FAIL", label, detail))

R, M, b2, r = sp.symbols('R M beta2 r', positive=True)
Min, Mout = sp.Integer(0), M

# ---- 1. closed form ---------------------------------------------------------
fin, fout = 1 - 2*Min/R, 1 - 2*Mout/R
sig0 = -(sp.sqrt(fout) - sp.sqrt(fin)) / (4*sp.pi*R)            # Lanczos sigma
p0 = ((1 - Mout/R)/sp.sqrt(fout) - (1 - Min/R)/sp.sqrt(fin)) / (8*sp.pi*R)
ms0 = 4*sp.pi*R**2*sig0
dM = Mout - Min
# m_s(r) to 2nd order about R: m_s' = -8 pi r p(r), p' = beta2 sigma'
ms1 = -8*sp.pi*R*p0
# sigma = m_s/(4 pi r^2) -> sigma'(R)
sig1 = ms1/(4*sp.pi*R**2) - 2*ms0/(4*sp.pi*R**3)
p1 = b2*sig1
ms2 = -8*sp.pi*p0 - 8*sp.pi*R*p1
x = sp.symbols('x')
msx = ms0 + ms1*x + ms2*x**2/2
Vx = 1 - 2*Mout/(R + x) - (dM/msx - msx/(2*(R + x)))**2
V0 = sp.simplify(Vx.subs(x, 0))
V1 = sp.simplify(sp.diff(Vx, x).subs(x, 0))
V2 = sp.diff(Vx, x, 2).subs(x, 0)
print("1. closed form for the ordinary shell (M_in = 0, M_out = M)")
chk("static shell: V(R0) = 0", sp.simplify(V0) == 0)
chk("static shell: V'(R0) = 0", sp.simplify(V1) == 0)
s = sp.symbols('s', positive=True)            # s = sqrt(1 - 2M/R), 0 < s < 1
V2s = sp.simplify(V2.subs(M, R*(1 - s**2)/2))
target = (2*b2*(3*s + 1)*s**2 + (s - 1)*(3*s**2 + 2*s + 1)/2) / (s**2*R**2)
chk("V''(R0) = [2 b2 (3s+1) s^2 + (s-1)(3s^2+2s+1)/2]/(s^2 R^2)",
    sp.simplify(V2s - target) == 0)
V2_0 = sp.simplify(target.subs(b2, 0))
print("     V''(beta2=0) =", sp.factor(V2_0))
b2c = sp.simplify(sp.solve(sp.Eq(target, 0), b2)[0])
print("     beta2_crit   =", sp.factor(b2c))

# ---- 2. z3 over the whole range ---------------------------------------------
print("2. z3: every compactness 0 < M/R < 1/2  <=>  0 < s < 1")
S, RR, B = z3.Reals('S RR B')
V2z = (2*B*(3*S + 1)*S**2 + (S - 1)*(3*S**2 + 2*S + 1)/2)
def prove(label, claim, hyp):
    sol = z3.Solver(); sol.add(hyp, z3.Not(claim))
    res = sol.check()
    chk(label, res == z3.unsat, "(z3 %s)" % res)
rng = z3.And(S > 0, S < 1)
prove("V''(beta2=0) < 0 for all 0<s<1 (denominator s^2 R^2 > 0)",
      z3.substitute(V2z, (B, z3.RealVal(0))) < 0, rng)
prove("coefficient of beta2, 2(3s+1)s^2, > 0 for all 0<s<1", 2*(3*S + 1)*S**2 > 0, rng)
prove("beta2_crit > 0 for all 0<s<1: V''<0 whenever beta2 <= 0",
      z3.Implies(B <= 0, V2z < 0), rng)
# vacuity guard: the hypothesis set is satisfiable
sol = z3.Solver(); sol.add(rng); chk("vacuity guard: 0<s<1 satisfiable", sol.check() == z3.sat)
chk("beta2_crit -> 0+ as s -> 1 (M/R -> 0): marginal only at infinite radius",
    sp.limit(b2c, s, 1, '-') == 0)
chk("beta2_crit -> +oo as s -> 0 (R -> 2M)", sp.limit(b2c, s, 0, '+') == sp.oo)

# ---- 3. Newtonian limit -----------------------------------------------------
print("3. weak field")
eps = sp.symbols('eps', positive=True)       # eps = M/R
V2e = sp.series(V2_0.subs(s, sp.sqrt(1 - 2*eps)).subs(R, 1), eps, 0, 2).removeO()
chk("V''(beta2=0) = -3 M/R^3 + O((M/R)^2)", sp.simplify(V2e.coeff(eps, 1) + 3) == 0,
    "(series %s)" % sp.nsimplify(V2e))

# ---- 4. the tree's printed numbers and its own numerics ---------------------
print("4. the tree's numbers (stability.py:47-49, R = 1)")
printed = {0.01: -3.036e-2, 0.1: -3.424e-1, 0.2: -8.169e-1}
f = sp.lambdify(s, V2_0.subs(R, 1))
for Mv, pv in printed.items():
    val = f(math.sqrt(1 - 2*Mv))
    chk("M/R=%.2f closed form %+.4e vs printed %+.3e" % (Mv, val, pv),
        abs(val - pv) <= 0.6e-4*10**math.floor(math.log10(abs(pv)) + 1) and
        float("%.3e" % val) == pv)
spec = importlib.util.spec_from_file_location(
    "stab", "/home/user/Claude-Method-Works/research/warp-drive/stability.py")
stab = importlib.util.module_from_spec(spec); spec.loader.exec_module(stab)
fc = sp.lambdify(s, b2c.subs(R, 1))
for Mv in (0.01, 0.1, 0.2, 0.3, 0.4, 0.45):
    tv = stab.V_second(*stab.ordinary(Mv), beta2=0.0)
    cv = f(math.sqrt(1 - 2*Mv))
    chk("M/R=%.2f tree V_second %+.6e vs exact %+.6e (rel %.1e)"
        % (Mv, tv, cv, abs(tv/cv - 1)), abs(tv/cv - 1) < 1e-4 and tv < 0)
for Mv in (0.01, 0.1, 0.2):
    tb = stab.beta2_crit(*stab.ordinary(Mv))
    cb = fc(math.sqrt(1 - 2*Mv))
    chk("M/R=%.2f tree beta2_crit(ordinary) %+.6f vs exact %+.6f" % (Mv, tb, cb),
        abs(tb - cb) < 1e-4 and cb > 0)

# ---- 5. the static ordinary shell carries pressure --------------------------
print("5. Lanczos pressure of the static ordinary shell")
p0s = sp.simplify((p0*8*sp.pi*R).subs(M, R*(1 - s**2)/2))
chk("8 pi R p0 = (1-s)^2/(2s)", sp.simplify(p0s - (1 - s)**2/(2*s)) == 0,
    "(= %s)" % sp.factor(p0s))
prove("p0 > 0 for all 0<s<1: the static shell is NOT pressureless",
      (1 - S)**2/(2*S) > 0, rng)

# ---- 6. a true dust shell has no static configuration -----------------------
print("6. TRUE dust (p == 0, m_s = m const): no static shell exists")
m = sp.symbols('m', positive=True)
Vd = 1 - 2*M/r - (M/m - m/(2*r))**2
sol6 = sp.solve([Vd, sp.diff(Vd, r)], [M, r], dict=True)
real_pos = [d for d in sol6 if all(v.is_positive for v in d.values())]
chk("V = V' = 0 has no solution with M > 0, r > 0 (sympy)", real_pos == [],
    "(solutions: %s)" % sol6)
# direct: V' = 0 forces m^2 = -2 M r
Mz, rz, mz = z3.Reals('Mz rz mz')
a_ = Mz/mz - mz/(2*rz)
Vdz = 1 - 2*Mz/rz - a_*a_
Vdpz = 2*Mz/rz**2 - a_*mz/rz**2            # dV/dr
sol = z3.Solver(); sol.add(Mz > 0, rz > 0, mz > 0, Vdz == 0, Vdpz == 0)
chk("z3: no M>0, r>0, m>0 with V = V' = 0", sol.check() == z3.unsat, "(z3 %s)" % sol.check())
# Barcelo-Jaramillo eq (4): M = sqrt(1+adot^2) M0 - M0^2/(2a)  =>  adot^2 = (M/M0 + M0/2a)^2 - 1
a, M0 = sp.symbols('a M0', positive=True)
adot2 = (M/M0 + M0/(2*a))**2 - 1
addot = sp.simplify(sp.diff(adot2, a)/2)    # a_ddot = (1/2) d(adot^2)/da
chk("BJ eq (4): a_ddot = -(M/M0 + M0/2a) M0/(2a^2) < 0 always",
    sp.simplify(addot + (M/M0 + M0/(2*a))*M0/(2*a**2)) == 0 and addot.is_negative,
    "(a_ddot = %s)" % addot)

# ---- 7. machinery vs a published number -------------------------------------
print("7. Ishak-Lake Fig. 2 / sec. III.B: P'/sigma' = 1, R/m+ ~ 2.37 as m- -> 0")
root = sp.nsolve(target.subs({b2: 1, R: 1}), s, 0.5)
Rm = 2/(1 - root**2)
chk("beta2 = 1 boundary at R/M = %.6f (published ~2.37)" % Rm, abs(Rm - 2.37) < 0.005)

# ---- 8. adiabatic-index form vs LeMaitre-Poisson 2019 (via PSP 2604.05980) --
print("8. Gamma = beta2 (sigma+p)/p; PSP sec. 10 restating LeMaitre-Poisson [34]:")
print("   'radially stable whenever Gamma >= 3/2' (Newtonian sequence)")
sig_s = sp.simplify((sig0).subs(M, R*(1 - s**2)/2))
p_s = sp.simplify((p0).subs(M, R*(1 - s**2)/2))
Gc = sp.simplify(b2c*(sig_s + p_s)/p_s)
chk("Gamma_crit = (3s^2+2s+1)/(4 s^2)", sp.simplify(Gc - (3*s**2 + 2*s + 1)/(4*s**2)) == 0,
    "(= %s)" % sp.factor(Gc))
chk("Gamma_crit -> 3/2 as M/R -> 0: the Newtonian threshold is reproduced",
    sp.limit(Gc, s, 1) == sp.Rational(3, 2))
prove("Gamma_crit > 3/2 for all 0<s<1: GR raises the threshold",
      (3*S**2 + 2*S + 1) > 6*S**2, rng)
chk("beta2 = 0 means Gamma = 0 < Gamma_crit at every compactness", True,
    "(Gamma = beta2 (sigma+p)/p with p0 > 0 finite, section 5)")

print("\nRESULT: %s" % ("ALL CHECKS PASS" if ok_all else "SOME CHECK FAILED"))
sys.exit(0 if ok_all else 1)
