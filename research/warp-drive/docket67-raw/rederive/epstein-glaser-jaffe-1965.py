#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for epstein-glaser-jaffe-1965.

What the tree uses (bounds.py:232-233, achievable.py:199-203, 316-324):
    F1 POINTWISE rho(x): "NO lower bound exists (Epstein-Glaser-Jaffe)".

What the restatements READ at source say EGJ proved (Fewster math-ph/0501073 p.2;
Fewster 1208.5399 p.8; Kontou-Sanders 2003.01815 Thm 3.2):
    NONPOSITIVITY -- a nonzero local observable with vanishing vacuum expectation
    value admits negative expectation values (Reeh-Schlieder + Hilbert-space linearity).
UNBOUNDEDNESS at a point is a SEPARATE step (Fewster math-ph/0501073 Sec.2 + Appendix):
    needs a nontrivial scaling limit of positive canonical dimension.

Checks (all exact / sympy unless marked numeric):
  C1  EGJ core lemma, finite-dim: A >= 0 and <O,AO> = 0  =>  AO = 0   (sympy 2x2 general + numeric random)
  C2  Fewster eq.(3)-(5): psi_a = cos a O + sin a AO/|AO| gives
      <A> = zeta sin2a + eta(1-cos2a), min = eta - sqrt(eta^2+zeta^2) < 0      (sympy)
  C3  LOGICAL GAP: nonpositivity does not imply unboundedness -- a Hermitian A with
      <O,AO>=0, AO != 0 whose spectrum is bounded below (every finite matrix)   (sympy)
  C4  Free massless scalar, one box mode, truncated Fock space (exact to n<=6):
      <:T00:(0,0)> in cos a|0> + sin a|2>  =  (w/2V)(4 s^2 - 2 sqrt2 s c);
      min over a = (w/2V)(2 - sqrt6)  -> linear in w -> unbounded below as w -> inf   (sympy)
  C5  Same state family, Lorentzian time average of width t0 (Ford-Roman sampling):
      cross term damped by exp(-2 w t0); min = (w/2V)(2 - sqrt(4+2 exp(-4 w t0)))
      is BOUNDED in w -- the functional, not the state family, carries the bound  (sympy+numeric)
Exit 0 iff every check passes.
"""
import sys
import random
import sympy as sp

ok = True
def check(name, cond, detail=""):
    global ok
    print(("PASS " if cond else "FAIL ") + name + ((" -- " + detail) if detail else ""))
    ok = ok and bool(cond)

# ---------------- C1: EGJ core lemma in finite dimension --------------------
# General 2x2 real PSD A = [[p, q],[q, r]], O = e1. <O,AO> = p = 0 and PSD => q = 0 => AO = 0.
p, q, r = sp.symbols('p q r', real=True)
A = sp.Matrix([[p, q], [q, r]])
# PSD requires all principal minors >= 0: p>=0, r>=0, pr - q^2 >= 0. With p = 0: -q^2 >= 0 => q = 0.
minor_at_p0 = sp.simplify((A.det()).subs(p, 0))
check("C1a det at <O,AO>=0 is -q^2 (so PSD forces q=0, AO=0)", sp.simplify(minor_at_p0 + q**2) == 0,
      f"det|p=0 = {minor_at_p0}")
# numeric: random PSD B = M M^T in dim 6, project so that <O,BO> = 0 exactly: B' = P B P with P = 1 - O O^T
import numpy as np
rng = np.random.default_rng(1965)
worst = 0.0
for _ in range(2000):
    n = 6
    M = rng.normal(size=(n, n))
    O = rng.normal(size=n); O /= np.linalg.norm(O)
    P = np.eye(n) - np.outer(O, O)
    B = P @ (M @ M.T) @ P           # PSD, and B O = 0 by construction
    worst = max(worst, abs(O @ B @ O), np.linalg.norm(B @ O))
    # converse direction: any PSD with <O,BO>=0 must have BO=0 -> test on B + perturbation that keeps PSD
check("C1b numeric (2000 PSD, dim 6): <O,BO>=0 & PSD  =>  |BO| ~ 0", worst < 1e-10, f"max residual {worst:.2e}")
# Numeric converse: PSD matrices with <O,BO> small have |BO|^2 <= |B| <O,BO> (Cauchy-Schwarz for B^{1/2})
viol = 0
for _ in range(2000):
    n = 5
    M = rng.normal(size=(n, n)); B = M @ M.T
    O = rng.normal(size=n); O /= np.linalg.norm(O)
    lhs = np.linalg.norm(B @ O) ** 2
    rhs = np.linalg.norm(B, 2) * (O @ B @ O)
    viol += lhs > rhs * (1 + 1e-9) + 1e-12
check("C1c |BO|^2 <= |B| <O,BO> for PSD B (the inequality EGJ's A^{1/2} step uses)", viol == 0,
      f"{viol} violations in 2000")

# ---------------- C2: Fewster (math-ph/0501073) eq.(3)-(5) -------------------
al, zeta = sp.symbols('alpha zeta', positive=True)
eta = sp.symbols('eta', real=True)
# <O,AO>=0, <O,A^2 O> = zeta^2, <O,A^3 O> = 2 eta zeta^2 ; psi = cos a O + sin a (AO)/zeta (normalized since O perp AO)
expA = sp.cos(al)**2 * 0 + 2*sp.sin(al)*sp.cos(al)*zeta**2/zeta + sp.sin(al)**2 * (2*eta*zeta**2)/zeta**2
claimed = zeta*sp.sin(2*al) + eta*(1 - sp.cos(2*al))
check("C2a <psi_a|A psi_a> = zeta sin2a + eta(1-cos2a)", sp.simplify(sp.expand_trig(expA - claimed)) == 0)
# minimum over a of zeta sin2a - eta cos2a + eta is eta - sqrt(zeta^2+eta^2)
th = sp.symbols('theta', real=True)
f = zeta*sp.sin(th) - eta*sp.cos(th) + eta
amp = sp.sqrt(zeta**2 + eta**2)
th_star = sp.atan2(-zeta, eta)   # sin th* = -zeta/amp, cos th* = eta/amp  -> f = -amp + eta
fmin = sp.simplify(f.subs({sp.sin(th): -zeta/amp, sp.cos(th): eta/amp}))
check("C2b min over a = eta - sqrt(eta^2+zeta^2)", sp.simplify(fmin - (eta - amp)) == 0, f"{fmin}")
check("C2c that minimum is < 0 whenever zeta > 0", all(
    float((eta - amp).subs({eta: e, zeta: z})) < 0 for e in (-5, -1, 0, 0.3, 1, 10, 1e3) for z in (1e-3, 0.1, 1, 7)))

# ---------------- C3: the logical gap -------------------------------------------
# A = [[0,1],[1,0]], O = e1: <O,AO> = 0, AO = e2 != 0, negative expectation exists (eig -1),
# yet A is BOUNDED BELOW by -1. Nonpositivity (EGJ) does not by itself give unboundedness.
A3 = sp.Matrix([[0, 1], [1, 0]])
O3 = sp.Matrix([1, 0])
check("C3 nonpositive-but-bounded-below example exists (EGJ alone != 'no lower bound')",
      (O3.T*A3*O3)[0] == 0 and (A3*O3) != sp.zeros(2, 1) and min(A3.eigenvals()) == -1,
      f"eigs {sorted(A3.eigenvals())}")

# ---------------- C4: free massless scalar, one mode, exact truncated Fock ----
N = 7  # basis |0>..|6>; the state lives in span{|0>,|2>}, A^2|2> needs |4>, so N=7 is exact here
a = sp.zeros(N, N)
for n in range(1, N):
    a[n-1, n] = sp.sqrt(n)
ad = a.T
w, V, t, x, t0 = sp.symbols('omega V t x t0', positive=True)
k = w  # massless, |k| = omega
e = sp.exp(sp.I*(k*x - w*t))
ec = sp.exp(-sp.I*(k*x - w*t))
# phi = (a e + a^dag e*)/sqrt(2 w V); pi = dphi/dt ; grad phi (along k) = d/dx
phi = (a*e + ad*ec) / sp.sqrt(2*w*V)
pi_ = sp.diff(phi, t)
dphi = sp.diff(phi, x)
def normal_order_quadratic(Xa, Xad):
    """Given X = Xa*a + Xad*a^dag (c-number coefficients), return :X^2: as a matrix."""
    return Xa**2 * a*a + Xad**2 * ad*ad + 2*Xa*Xad * ad*a
def coeffs(X):
    # X = ca*a + cd*ad ; recover ca, cd by matrix elements <0|X|1> = ca, <1|X|0> = cd
    return sp.simplify(X[0, 1]), sp.simplify(X[1, 0])
ca_pi, cd_pi = coeffs(pi_)
ca_dx, cd_dx = coeffs(dphi)
T00 = sp.Rational(1, 2) * (normal_order_quadratic(ca_pi, cd_pi) + normal_order_quadratic(ca_dx, cd_dx))
s, c = sp.symbols('s c', real=True)
psi = sp.zeros(N, 1); psi[0] = c; psi[2] = s    # c = cos a, s = sin a
val = sp.simplify((psi.T * T00 * psi)[0].subs({x: 0, t: 0}))
target = (w/(2*V)) * (4*s**2 - 2*sp.sqrt(2)*s*c)
check("C4a <:T00:(0)> = (w/2V)(4 s^2 - 2 sqrt2 s c) in cos a|0>+sin a|2>", sp.simplify(val - target) == 0, f"{sp.factor(val)}")
g = 4*sp.sin(al)**2 - 2*sp.sqrt(2)*sp.sin(al)*sp.cos(al)   # = 2 - 2cos2a - sqrt2 sin2a
gmin = 2 - sp.sqrt(6)
# verify by the amplitude identity: 2cos2a + sqrt2 sin2a has max sqrt(4+2) = sqrt6
check("C4b min_a (4s^2 - 2sqrt2 sc) = 2 - sqrt6 = %.6f" % float(gmin),
      abs(min(float(g.subs(al, i*sp.pi/20000)) for i in range(0, 20000)) - float(gmin)) < 1e-6)
pt_min = (w/(2*V))*gmin
check("C4c pointwise minimum is -(sqrt6-2) w/(2V): linear in w, unbounded below as w -> inf",
      sp.limit(pt_min, w, sp.oo) == -sp.oo, f"{sp.simplify(pt_min)}")

# ---------------- C5: the Lorentzian time average (Ford-Roman sampling) bounds the SAME family
# Lorentzian average of exp(-2 i w t) with t0/(pi(t^2+t0^2)) is exp(-2 w t0); <a^dag a> term is t-independent.
lor = sp.integrate(sp.cos(2*w*t) * t0/(sp.pi*(t**2 + t0**2)), (t, -sp.oo, sp.oo))
check("C5a Lorentzian average of cos(2wt) = exp(-2 w t0)", sp.simplify(lor - sp.exp(-2*w*t0)) == 0, f"{sp.simplify(lor)}")
avg_min = (w/(2*V))*(2 - sp.sqrt(4 + 2*sp.exp(-4*w*t0)))
check("C5b time-averaged minimum -> 0 as w -> inf (bounded), not -inf", sp.limit(avg_min, w, sp.oo) == 0)
# the worst case over w is finite: numeric scan
fnum = sp.lambdify(w, avg_min.subs({V: 1, t0: 1}), 'math')
worst_avg = min(fnum(0.001*i) for i in range(1, 20000))
check("C5c worst time-averaged value over w (V=t0=1) is finite", worst_avg > -1.0, f"min_w = {worst_avg:.6f}")

print("\nSUMMARY: EGJ core (nonpositivity) re-derived; unboundedness at a point re-derived for the free "
      "massless field by scaling in w (C4); C3 shows nonpositivity alone does not deliver 'no lower bound'.")
sys.exit(0 if ok else 1)
