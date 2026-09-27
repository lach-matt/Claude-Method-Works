#!/usr/bin/env python3
"""
DOCKET 67, pass S, 14/36 -- gr-qc/0209075#criterion (AMM linear-response validity criterion).

The result is a DEFINITION (a proposed necessary condition), not a theorem and not a
measurement.  What is finite and checkable here:

  A. TEXT FIDELITY.  Every string the owner (research/warp-drive/linstab.py) attributes to
     AMM in quotation marks is searched for in the arXiv v1 text layer (alphaXiv), after a
     normalisation that undoes the text layer's known damage: line-break hyphens, control bytes
     (ffi and delta render as \\x0e), all whitespace, and the dropped ligatures fi / ff / fl / ffi.  Clauses of the source the
     owner does NOT carry are searched for too, so a drop is SHOWN, not asserted.
  B. WHY THE GAUGE-INVARIANT CLAUSE IS LOAD-BEARING (sympy).  In Minkowski, a pure-gauge
     perturbation h_ab = d_a X_b + d_b X_a with a time-growing X has components that grow
     without bound, while the linearised Riemann tensor -- a scalar-building object made
     only from h_ab and its derivatives -- vanishes identically for ARBITRARY X.  So a
     component-wise growth verdict is gauge-dependent; AMM's restriction to gauge-invariant
     scalars built only from h_ab is what makes the criterion well posed.
  C. WHY H1 (background solves (2.9)) IS LOAD-BEARING (sympy).  Toy: x'' = F(x) with
     F(x) = -x (bounded dynamics).  Linearising about a NON-solution x0 leaves a zeroth-order
     source r = F(x0) - x0''.  With x0 = -(t/2) sin t, r = cos t... and the zero-data
     response is unbounded although every homogeneous solution is bounded.  A boundedness
     verdict computed off-solution is therefore not a property of the dynamics
     (one direction; linstab.py's own selftest W1/W2 carry both).
  D. LOGIC (z3).  AMM: Valid -> NoGrowth (necessary).  Checked: (i) Growth -> not Valid is
     entailed; (ii) NoGrowth -> Valid is NOT entailed (countermodel); (iii) with NoGrowth
     undetermined (the tree's 'NOT EVALUABLE'), Valid is undetermined both ways.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "amm_0209075.txt")   # alphaXiv text layer, v1
OWNER = "/home/user/Claude-Method-Works/research/warp-drive/linstab.py"

fails = 0
def chk(label, got, want):
    global fails
    ok = (got == want)
    fails += (not ok)
    print(("  [ok]   " if ok else "  [FAIL] ") + label + "  ->  " + repr(got))

def norm(s):
    s = s.replace("-\n", "")
    s = re.sub(r"[\x00-\x08\x0b-\x1f]", "", s)   # text layer renders ffi / delta as control bytes
    for lig in ("ffi", "ffl", "ff", "fi", "fl"):
        s = s.replace(lig, "")
    s = re.sub(r"\s+", "", s)
    return s.lower()

print("A. TEXT FIDELITY against", SRC)
src = norm(open(SRC).read())
own = open(OWNER).read()

quoted_by_owner = {
    "abstract/III quote (linstab.py:26-29)":
        "solutions to the semi-classical Einstein equations should be stable to linearized "
        "perturbations, in the sense that no gauge invariant perturbation should become "
        "unbounded in time.",
    "III p.10 quote (linstab.py:103-104)":
        "with finite non-singular initial data for which any linearized gauge "
        "invariant scalar quantity grows without bound",
    "p.8 quote (linstab.py:273)": "the first variation vanishes by (2.9)",
    "p.9 quote (linstab.py:274-276)":
        "is evaluated in the background geometry of the leading order solution of the "
        "semi-classical equations (2.9)",
}
for k, q in quoted_by_owner.items():
    chk("owner quote present verbatim in source: " + k, norm(q) in src, True)

source_clauses = {
    "'A necessary condition for the validity of the large N semi-classical equations of motion (2.9)'":
        "A necessary condition for the validity of the large N semi-classical equations of motion (2.9)",
    "'Such a quantity must be constructed only from the linearized metric perturbation h'":
        "Such a quantity must be constructed only from the linearized metric perturbation h",
    "'Singular gauge transformations in the initial data for g'":
        "Singular gauge transformations in the initial data for g",
    "'around a given semi-classical geometry g ... that solves eq.(2.9)' (p.8)":
        "around a given semi-classical geometry g",
    "'Clearly this is a necessary, though perhaps not a sufficient condition' (p.13)":
        "Clearly this is a necessary, though perhaps not a sufficient condition",
    "'at least not for that particular state' (p.13)":
        "at least not for that particular state",
}
for k, q in source_clauses.items():
    chk("source clause present: " + k, norm(q) in src, True)

owner_carries = {
    "'constructed only from' (h_ab-only clause)": "constructed only from",
    "'Singular gauge' clause": "singular gauge",
    "'sufficient' (any statement on sufficiency)": "sufficien",
    "'large-N' / 'large N'": "large-n",
    "'NECESSARY'": "necessary",
}
print("   what the OWNER carries (case-insensitive search of linstab.py):")
for k, q in owner_carries.items():
    print("     %-48s %s" % (k, q in own.lower()))
chk("owner drops the h_ab-only clause", "constructed only from" in own.lower(), False)
chk("owner drops the singular-gauge exclusion", "singular gauge" in own.lower(), False)
chk("owner says nothing about sufficiency (canonical's 'not sufficient' is not the owner's)",
    "sufficien" in own.lower(), False)
chk("owner carries 'large-N' (SETTING, H2)", "large-n" in own.lower(), True)

print("\nB. GAUGE: pure-gauge growth is invisible to the linearised Riemann tensor (sympy)")
import sympy as sp
t, x, y, z = sp.symbols("t x y z", real=True)
X = [sp.Function("X%d" % i)(t, x, y, z) for i in range(4)]
co = [t, x, y, z]
h = [[sp.diff(X[b], co[a]) + sp.diff(X[a], co[b]) for b in range(4)] for a in range(4)]
def riem(h):
    R = 0
    nz = 0
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    e = sp.Rational(1, 2) * (sp.diff(h[a][d], co[b], co[c]) + sp.diff(h[b][c], co[a], co[d])
                                             - sp.diff(h[b][d], co[a], co[c]) - sp.diff(h[a][c], co[b], co[d]))
                    if sp.simplify(e) != 0:
                        nz += 1
    return nz
chk("linearised Riemann of h = dX + dX, arbitrary X(t,x,y,z): nonzero components", riem(h), 0)
Xg = [t**2, 0, 0, 0]
hg00 = 2 * sp.diff(Xg[0], t)
chk("with X_0 = t^2, h_00 = 4t: grows without bound", (sp.simplify(hg00 - 4*t) == 0, sp.limit(hg00, t, sp.oo)), (True, sp.oo))

print("\nC. H1: off-solution linearisation carries a residual source (sympy)")
x0 = -(t/2) * sp.sin(t)
r = sp.simplify(-x0 - sp.diff(x0, t, 2))          # F(x0) - x0'' with F(x) = -x
chk("residual r = F(x0) - x0'' for x0 = -(t/2) sin t", sp.simplify(r - sp.cos(t)) == 0, True)
d = sp.Function("d")
sol = sp.dsolve(sp.Eq(d(t).diff(t, 2) + d(t), r), d(t), ics={d(0): 0, d(t).diff(t).subs(t, 0): 0})
chk("zero-data response to r", sp.simplify(sol.rhs - t*sp.sin(t)/2) == 0, True)
hom = sp.dsolve(sp.Eq(d(t).diff(t, 2) + d(t), 0), d(t)).rhs
chk("every homogeneous solution bounded (C1 cos t + C2 sin t)",
    set(str(a) for a in hom.atoms(sp.Function)) == {"cos(t)", "sin(t)"}, True)
chk("but the off-solution response t sin(t)/2 is unbounded (at t = 2 pi n + pi/2)",
    sp.limit((t*sp.sin(t)/2).subs(t, 2*sp.pi*sp.Symbol("n", positive=True, integer=True) + sp.pi/2),
             sp.Symbol("n", positive=True, integer=True), sp.oo), sp.oo)

print("\nD. LOGIC: a necessary condition (z3)")
import z3
V, NG = z3.Bools("Valid NoGrowth")
AMM = z3.Implies(V, NG)
s = z3.Solver(); s.add(AMM, z3.Not(NG), V)
chk("Growth -> not Valid entailed (AMM & Growth & Valid unsat)", s.check() == z3.unsat, True)
s = z3.Solver(); s.add(AMM, NG, z3.Not(V))
chk("NoGrowth -> Valid NOT entailed (countermodel sat)", s.check() == z3.sat, True)
s1 = z3.Solver(); s1.add(AMM, V); s2 = z3.Solver(); s2.add(AMM, z3.Not(V))
chk("NoGrowth undetermined: Valid and not-Valid both consistent", (s1.check(), s2.check()), (z3.sat, z3.sat))

print("\n%d failed" % fails)
sys.exit(1 if fails else 0)
