#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key no-existence-theorem-ssaf.

The external 'result' is a literature-state claim (throatmass.py:98-99, :174-176):
  'Closed only by a general existence theorem for the static spherically symmetric
   asymptotically flat class, which nobody has.'
A universal negative over the literature is NOT machine-checkable.  What IS finite:
  C1 (sympy)  HPS gr-qc/9701064 eqs (5)-(7), transcribed from the page text READ at
              d67/src/hps/_flat0.txt: flat space f = 1, r = l (regular centre) makes
              both sides vanish identically -> the class is NON-EMPTY (Minkowski, the
              solution Sanders 2007.14311 p.2 excepts).  So 'existence' can only mean
              NON-TRIVIAL (non-flat) existence: a qualifier the tree's wording omits.
  C2 (sympy)  HPS's own printed asymptotics R(l) ~ l, F(l) ~ (a ln l - b)^2, a = 5.3,
              b = 25.5: F -> infinity, so HPS's solution is not asymptotically flat
              (HPS p.8 says so).  It therefore supplies no AF member, and it is
              numerical evidence, not a theorem.  m(l) = (r/2)(1 - r'^2) -> 0 on R = l.
  C3 (z3)     the logic of 'closed ONLY by an existence theorem': on a finite model,
              (a) an exhibited AF solution with m < 0 decides O5 = yes with no theorem,
              (b) a no-go decides O5 = no, (c) a general existence theorem E is
              consistent with BOTH answers, so E alone closes nothing.  The 'only'
              fails as logic.  (The tree already replaced it: hpscentre.O5_ANSWERED_BY
              lists 'an asymptotically flat self-consistent solution with m < 0'.)
Exit 0 iff every check passes.
"""
import sys
import sympy as sp

fails = []
def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  -- " + detail) if detail else ""))
    if not ok:
        fails.append(name)

l = sp.symbols('l', positive=True)
K2 = sp.Rational(1, 5760) / sp.pi
f = sp.Function('f')(l)
r = sp.Function('r')(l)
d = lambda g, n=1: sp.diff(g, l, n)
f1, f2, f3, f4 = d(f), d(f, 2), d(f, 3), d(f, 4)
r1, r2, r3, r4 = d(r), d(r, 2), d(r, 3), d(r, 4)
L = sp.log(f)

# Left sides (HPS p.4, Einstein tensor in the proper-distance gauge)
Gtt = 2*r2/r + r1**2/r**2 - 1/r**2
Gll = f1*r1/(f*r) + r1**2/r**2 - 1/r**2
Gth = f2/(2*f) + r2/r + f1*r1/(2*f*r) - f1**2/(4*f**2)

# Right sides, HPS eqs (5)-(7), xi = 1/6, m = 0, transcribed from page text
tt = (32/r**4 + 7*f1**4/f**4 - 24*f1**3*r1/(f**3*r) + 24*f1**2*r1**2/(f**2*r**2)
      - 32*r1**4/r**4 + 4*f1**2*f2/f**3 - 12*f2**2/f**2 + 80*f1**2*r2/(f**2*r)
      - 160*f1*r1*r2/(f*r**2) + 128*r1**2*r2/r**3 - 64*f2*r2/(f*r) + 32*r2**2/r**2
      - 16*f1*f3/f**2 + 64*r1*f3/(f*r) - 96*f1*r3/(f*r) - 64*r1*r3/r**2
      + 16*f4/f - 64*r4/r
      + L*(16/r**4 - 49*f1**4/f**4 + 44*f1**3*r1/(f**3*r) + 20*f1**2*r1**2/(f**2*r**2)
           - 16*r1**4/r**4 + 16*f1**2*f2/f**3 - 104*f1*r1*f2/(f**2*r) - 36*f2**2/f**2
           + 8*f1**2*r2/(f**2*r) - 80*f1*r1*r2/(f*r**2) + 64*r1**2*r2/r**3
           + 16*f2*r2/(f*r) + 16*r2**2/r**2 - 48*f1*f3/f**2 + 64*r1*f3/(f*r)
           - 16*f1*r3/(f*r) - 32*r1*r3/r**2 + 16*f4/f - 32*r4/r))
ll = (f1**4/f**4 - 16*f1**3*r1/(f**3*r) + 64*f1*r1**3/(f*r**3) - 4*f1**2*f2/f**3
      + 64*f1*r1*f2/(f**2*r) - 64*r1**2*f2/(f*r**2) - 4*f2**2/f**2 - 48*f1**2*r2/(f**2*r)
      + 32*f1*r1*r2/(f*r**2) + 32*f2*r2/(f*r) + 8*f1*f3/f**2 - 32*r1*f3/(f*r)
      - 32*f1*r3/(f*r)
      + L*(16/r**4 + 7*f1**4/f**4 - 20*f1**3*r1/(f**3*r) - 4*f1**2*r1**2/(f**2*r)
           + 32*f1*r1**3/(f*r**3) - 16*r1**4/r**4 - 12*f1**2*f2/f**3 + 48*f1*r1*f2/(f**2*r)
           - 32*r1**2*f2/(f*r**2) - 4*f2**2/f**2 - 16*f1**2*r2/(f**2*r)
           + 16*f1*r1*r2/(f*r**2) + 16*f2*r2/(f*r) - 16*r2**2/r**2 + 8*f1*f3/f**2
           - 16*r1*f3/(f*r) - 16*f1*r3/(f*r) + 32*r1*r3/r**2))
th = (17*f1**4/f**4 - 16*f1**3*r1/(f**3*r) - 32*f1*r1**3/(f*r**3) - 52*f1**2*f2/f**3
      + 32*f1*r1*f2/(f**2*r) + 32*r1**2*f2/(f*r**2) + 28*f2**2/f**2 + 16*f1**2*r2/(f**2*r)
      + 64*f1*r1*r2/(f*r**2) - 32*f2*r2/(f*r) + 24*f1*f3/f**2 - 48*r1*f3/(f*r)
      + 32*f1*r3/(f*r) - 16*f4/f
      + L*(-16/r**4 + 21*f1**4/f**4 - 12*f1**3*r1/(f**3*r) - 8*f1**2*r1**2/(f**2*r**2)
           - 16*f1*r1**3/(f*r**3) + 16*r1**4/r**4 - 52*f1**2*f2/f**3 + 28*f1*r1*f2/(f**2*r)
           + 16*r1**2*f2/(f*r**2) + 20*f2**2/f**2 + 4*f1**2*r2/(f**2*r)
           + 32*f1*r1*r2/(f*r**2) - 32*r1**2*r2/r**3 - 16*f2*r2/(f*r) + 20*f1*f3/f**2
           - 24*r1*f3/(f*r) + 16*f1*r3/(f*r) - 8*f4/f + 16*r4/r))

def on(expr, fv, rv):
    e = expr
    for n in (4, 3, 2, 1):
        e = e.subs(d(f, n), sp.diff(fv, l, n)).subs(d(r, n), sp.diff(rv, l, n))
    return sp.simplify(e.subs(f, fv).subs(r, rv))

# C1: flat space, regular centre, f = 1 and also f = c (any positive constant)
c = sp.symbols('c', positive=True)
for fv, tag in ((sp.Integer(1), "f=1"), (c, "f=c")):
    res = [on(Gtt - K2*tt, fv, l), on(Gll - K2*ll, fv, l), on(Gth - K2*th, fv, l)]
    check("C1 flat space (%s, r=l) solves HPS eqs (5)-(7) identically" % tag,
          all(x == 0 for x in res), "residuals %s" % res)
m_flat = (l/2)*(1 - sp.diff(l, l)**2)
check("C1 Misner-Sharp mass of the flat member is 0", sp.simplify(m_flat) == 0)
# control: a non-solution must NOT pass (Schwarzschild-like r'' != 0 profile)
rv_bad = l + 1/l
def on_num(expr, fv, rv, at):
    e = expr
    for n in (4, 3, 2, 1):
        e = e.subs(d(f, n), sp.diff(fv, l, n)).subs(d(r, n), sp.diff(rv, l, n))
    return float(e.subs(f, fv).subs(r, rv).subs(l, at))
bad = on_num(Gtt - K2*tt, sp.Integer(1), rv_bad, 2)
check("C1 control: f=1, r=l+1/l does NOT solve eq (5) (residual at l=2)",
      abs(bad) > 1e-6, "residual %.6g" % bad)

# C2: HPS printed asymptotics
a, b = sp.Rational(53, 10), sp.Rational(255, 10)
F = (a*sp.log(l) - b)**2
check("C2 HPS F(l) = (5.3 ln l - 25.5)^2 -> infinity (not asymptotically flat)",
      sp.limit(F, l, sp.oo) == sp.oo)
check("C2 no finite limit of F: F(1e6)/F(1e3) != 1",
      abs(float(F.subs(l, 10**6)/F.subs(l, 10**3)) - 1) > 0.1,
      "F(1e3)=%.3f F(1e6)=%.3f" % (float(F.subs(l, 10**3)), float(F.subs(l, 10**6))))
R = l
m_R = (R/2)*(1 - sp.diff(R, l)**2)
check("C2 m(l) on R = l is 0 at leading order (no ADM mass read-off: f unbounded)",
      sp.simplify(m_R) == 0)

# C3: z3, logic of 'closed only by an existence theorem'
try:
    import z3
except ImportError:
    check("C3 z3 importable", False); z3 = None
if z3:
    N = 4
    AF = [z3.Bool('af%d' % i) for i in range(N)]
    NT = [z3.Bool('nt%d' % i) for i in range(N)]     # non-trivial (non-flat)
    NEG = [z3.Bool('neg%d' % i) for i in range(N)]   # m < 0 somewhere
    O5 = z3.Or([z3.And(AF[i], NEG[i]) for i in range(N)])
    E = z3.Or([z3.And(AF[i], NT[i]) for i in range(N)])      # general existence
    X = z3.And(AF[0], NEG[0])                                 # exhibited solution
    NOGO = z3.And([z3.Implies(AF[i], z3.Not(NEG[i])) for i in range(N)])
    def sat(*fs):
        s = z3.Solver(); s.add(*fs); return s.check() == z3.sat
    def valid(fml):
        s = z3.Solver(); s.add(z3.Not(fml)); return s.check() == z3.unsat
    check("C3a exhibited AF m<0 solution decides O5 = yes (no theorem needed)",
          valid(z3.Implies(X, O5)))
    check("C3b a no-go decides O5 = no", valid(z3.Implies(NOGO, z3.Not(O5))))
    check("C3c existence theorem E consistent with O5 = yes", sat(E, O5))
    check("C3c existence theorem E consistent with O5 = no", sat(E, z3.Not(O5)))
    check("C3 vacuity guard: X and NOGO are each satisfiable, and jointly not",
          sat(X) and sat(NOGO) and not sat(X, NOGO))

print("\n%d FAIL" % len(fails) if fails else "\nALL PASS")
sys.exit(1 if fails else 0)
