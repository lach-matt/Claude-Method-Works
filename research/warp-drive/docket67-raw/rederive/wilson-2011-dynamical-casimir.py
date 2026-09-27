#!/usr/bin/env python3
"""
DOCKET 67 -- wilson-2011-dynamical-casimir (Wilson et al., arXiv:1105.4714, Nature 479, 376 (2011)).

What is checkable here and what is not.
  NOT CHECKABLE HERE: the measurement itself (a photon-flux / correlation measurement on a
  SQUID-terminated coplanar waveguide).  No experimental datum can be re-derived by a script,
  and the paper could not be read at source this pass (alphaXiv quota exhausted; arxiv.org,
  nature.com, ADS mirrors refused by the egress proxy).
  CHECKABLE HERE (closed form, and it bears on exactly the step warpfolder.py:153-156 files
  NOT-ADJUDICATED -- whether a moving-boundary / DCE process yields USABLE negative energy):
   (A) sympy: the 1+1D moving-mirror flux (Fulling-Davies form, hbar=c=1)
          F(u) = (1/24 pi) [ (3/2)(p''/p')^2 - p'''/p' ]
       satisfies the exact identity  F = (1/48 pi)(p''/p')^2 - (1/24 pi) d/du (p''/p'),
       so for a motion that begins and ends inertial (p''/p' -> 0 at both ends) the TOTAL
       emitted energy is (1/48 pi) Int (p''/p')^2 du >= 0, while F(u) itself may be negative.
       The formula for F is the standard Fulling-Davies result, RECALLED here, not read at source
       this pass; the identity is what is machine-checked.
   (B) numeric: an oscillating-burst boundary (the shape a parametric drive has) -- F dips
       negative, the integral is positive and equals the (A) closed form.
   (C) the tree's own frequency gap (frequency.py, context, not an owner of this key): the ratio
       f_crit / f_drive at 1e9 Hz (tree's DCE_DRIVEN_AT_HZ) and at 1.1e10 Hz (an UNATTRIBUTED
       web-search summary figure, ~11 GHz, NOT read at source).  Shows whether the datum moves
       the tree's conclusion.
stdlib + sympy.  Exit 0 iff every check passes.
"""
import sys, math
sys.dont_write_bytecode = True
import sympy as sp

ok = True
def chk(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  -- " + detail if detail else ""))

# ---------------------------------------------------------------- (A) identity
u = sp.symbols('u', real=True)
p = sp.Function('p')(u)
p1, p2, p3 = sp.diff(p, u), sp.diff(p, u, 2), sp.diff(p, u, 3)
F = (sp.Rational(3, 2)*(p2/p1)**2 - p3/p1)/(24*sp.pi)
rhs = (p2/p1)**2/(48*sp.pi) - sp.diff(p2/p1, u)/(24*sp.pi)
chk("(A) F == (1/48pi)(p''/p')^2 - (1/24pi) d/du(p''/p')  [symbolic]", sp.simplify(F - rhs) == 0)

# concrete symbolic instance: p = u + eps*sin(w u) exp(-u^2/s^2) ; check identity pointwise
eps, w, s = sp.Rational(1, 20), 3, 4
pc = u + eps*sp.sin(w*u)*sp.exp(-u**2/s**2)
Fc = F.subs(p, pc).doit()
rc = rhs.subs(p, pc).doit()
diff_max = max(abs(float((Fc - rc).subs(u, x))) for x in [-7.3, -2.1, 0.37, 1.9, 5.5])
chk("(A') identity holds on a concrete trajectory", diff_max < 1e-12, f"max |diff| = {diff_max:.1e}")

# ---------------------------------------------------------------- (B) numeric burst
f_p1 = sp.lambdify(u, sp.diff(pc, u), 'math')
f_F  = sp.lambdify(u, Fc, 'math')
f_q  = sp.lambdify(u, (sp.diff(pc, u, 2)/sp.diff(pc, u))**2/(48*sp.pi), 'math')
L, N = 30.0, 60001
h = 2*L/(N-1)
xs = [-L + i*h for i in range(N)]
minp1 = min(f_p1(x) for x in xs)
Fv = [f_F(x) for x in xs]
Qv = [f_q(x) for x in xs]
def simpson(v):
    return h/3*(v[0] + v[-1] + 4*sum(v[1:-1:2]) + 2*sum(v[2:-1:2]))
E, Eq = simpson(Fv), simpson(Qv)
Fmin, Fmax = min(Fv), max(Fv)
negfrac = sum(1 for v in Fv if v < 0)/len(Fv)
negint = simpson([min(v, 0.0) for v in Fv])
chk("(B0) p' > 0 on the grid (a physical, timelike mirror)", minp1 > 0, f"min p' = {minp1:.4f}")
chk("(B1) instantaneous flux goes NEGATIVE", Fmin < 0, f"min F = {Fmin:.4e}, max F = {Fmax:.4e}")
chk("(B2) total emitted energy POSITIVE", E > 0, f"Int F du = {E:.6e}")
chk("(B3) total equals (1/48pi) Int (p''/p')^2", abs(E - Eq) < 1e-8*max(1, abs(Eq)), f"{E:.10e} vs {Eq:.10e}")
print(f"     negative-flux fraction of grid = {negfrac:.3f}; Int min(F,0) = {negint:.4e}; "
      f"|neg|/net = {abs(negint)/E:.2f}")

# ---------------------------------------------------------------- (C) tree's frequency gap
F_CRIT_TREE = 5.870709e42           # frequency.py's printed f_P/sqrt(Lambda), taken as the tree states it
for f_drive, label in [(1e9, "tree DCE_DRIVEN_AT_HZ = 1e9"), (1.1e10, "~11 GHz, unattributed web summary, NOT READ")]:
    r = F_CRIT_TREE/f_drive
    print(f"     f_crit / f_drive at {label}: {r:.3e}  ({math.log10(r):.2f} decades)")
r1, r2 = F_CRIT_TREE/1e9, F_CRIT_TREE/1.1e10
chk("(C) moving the drive 1 GHz -> 11 GHz shifts the tree's gap by < 1.1 decades (qualitative verdict unmoved)",
    math.log10(r1/r2) < 1.1, f"{math.log10(r1/r2):.3f} decades; printed 5.87e33 would read {r2:.2e}")

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
