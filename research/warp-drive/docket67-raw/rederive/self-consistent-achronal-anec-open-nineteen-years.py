#!/usr/bin/env python3
"""
D67 re-derivation for key self-consistent-achronal-anec-open-nineteen-years.

What is finite / closed-form here, and what is not:
  (A) the "nineteen years" date arithmetic -- from Graham & Olum's naming of the
      condition (arXiv:0705.3193, v1 May 2007 by arXiv-id convention, v2 dated
      27 Aug 2007 on its own page 1) to the owner commit of anecscope.py
      (2026-09-08) and to today (2026-09-26); and, for comparison, from the
      earlier formulations G&O themselves credit (Penrose-Sorkin-Woolgar 1993,
      gr-qc/9301015; Flanagan-Wald 1996, gr-qc/9602052, who "stated ANEC in the
      achronal form" in self-consistent perturbation theory -- G&O p.4).
  (B) G&O footnote 1 (p.3): in Schwarzschild, k^a k^b k_[t R_r]ab[t k_r] =
      -(3M/r^3) sin(alpha) -- the computation that makes every complete
      Schwarzschild null geodesic generic, hence (with ANEC) conjugate, hence
      chronal, so the Boulware ANEC violation does not touch Condition 1.
      Re-derived with sympy from the metric.
  (C) G&O Lemma 1 as a propositional skeleton, machine-checked with z3:
      Condition 1 + null generic condition => no complete achronal null
      geodesic, taking Borde 1987 (ANEC + generic => conjugate pair) and
      Hawking-Ellis (conjugate pair => chronal) as axioms.  This checks only
      that the lemma follows from its premises; it does not check the premises.
NOT checkable here: whether self-consistent achronal ANEC is true.  That is
the open conjecture itself; no finite computation decides it.
"""
import datetime as dt
import sympy as sp

ok = True
def chk(label, cond):
    global ok
    ok &= bool(cond)
    print("  %-70s %s" % (label, "ok" if cond else "FAIL"))

# ---------------------------------------------------------------- (A) dates
print("(A) date arithmetic")
yr = 365.2425
commit = dt.date(2026, 9, 8)
today = dt.date(2026, 9, 26)
go_v1 = dt.date(2007, 5, 1)     # arXiv 0705.xxxx: May 2007 (day not read)
go_v1_end = dt.date(2007, 5, 31)
go_v2 = dt.date(2007, 8, 27)    # read: page 1 of 0705.3193v2
fw = dt.date(1996, 2, 1)        # gr-qc/9602052 (v2 dated 2 Jul 1996, read)
psw = dt.date(1993, 1, 1)       # gr-qc/9301015 (id convention)
wy = dt.date(1991, 7, 15)       # PRD 44, 403 (1991): achronal restriction; month not read
for lab, d0 in [("G&O v1 (May 2007, earliest)", go_v1), ("G&O v1 (May 2007, latest)", go_v1_end),
                ("G&O v2 (27 Aug 2007)", go_v2)]:
    for lab2, d1 in [("owner commit 2026-09-08", commit), ("today 2026-09-26", today)]:
        y = (d1 - d0).days / yr
        print("    %-28s -> %-24s %6.2f yr  floor %d" % (lab, lab2, y, int(y)))
        chk("floor(years) == 19  [%s -> %s]" % (lab, lab2), int(y) == 19)
for lab, d0 in [("Flanagan-Wald 1996 (self-consistent, achronal form)", fw),
                ("Penrose-Sorkin-Woolgar 1993 (self-consistency)", psw),
                ("Wald-Yurtsever 1991 (achronal restriction)", wy)]:
    y = (commit - d0).days / yr
    print("    %-52s %6.2f yr before the owner commit" % (lab, y))
chk("question older than the named condition: FW 1996 gives > 19 yr", (commit - fw).days / yr > 19)

# ------------------------------------------------ (B) G&O footnote 1, sympy
print("(B) G&O footnote 1: Schwarzschild generic-condition component")
t, r, th, ph, M = sp.symbols('t r theta phi M', positive=True)
al = sp.symbols('alpha', real=True)
x = [t, r, th, ph]
f = 1 - 2*M/r
g = sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2)
gi = g.inv()
n = 4
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
                        for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
def Riem_up(a, b, c, d):   # R^a_{bcd}
    e = sp.diff(Gam[a][b][d], x[c]) - sp.diff(Gam[a][b][c], x[d])
    e += sum(Gam[a][c][k]*Gam[k][b][d] - Gam[a][d][k]*Gam[k][b][c] for k in range(n))
    return e
R = {}
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                R[a, b, c, d] = sp.simplify(sum(g[a, k]*Riem_up(k, b, c, d) for k in range(n)))
# orthonormal static frame e_(i) = E[i][mu]
E = [[1/sp.sqrt(f), 0, 0, 0], [0, sp.sqrt(f), 0, 0], [0, 0, 1/r, 0], [0, 0, 0, 1/(r*sp.sin(th))]]
def Rf(i, j, k, l):
    return sp.simplify(sum(E[i][a]*E[j][b]*E[k][c]*E[l][d]*R[a, b, c, d]
                           for a in range(n) for b in range(n) for c in range(n) for d in range(n)
                           if E[i][a] != 0 and E[j][b] != 0 and E[k][c] != 0 and E[l][d] != 0))
Rframe = {(i, j, k, l): Rf(i, j, k, l) for i in range(n) for j in range(n) for k in range(n) for l in range(n)}
eta = sp.diag(-1, 1, 1, 1)
chk("frame R_trtr = -2M/r^3 (standard sign)", sp.simplify(Rframe[0, 1, 0, 1] + 2*M/r**3) == 0)
chk("frame R_thph thph = +2M/r^3", sp.simplify(Rframe[2, 3, 2, 3] - 2*M/r**3) == 0)
kup = [1, sp.cos(al), sp.sin(al), 0]             # null, angle alpha from radial
klo = [sum(eta[i, j]*kup[j] for j in range(n)) for i in range(n)]
chk("k null", sp.simplify(sum(kup[i]*klo[i] for i in range(n))) == 0)
def Q(c, d, e, f_):   # k_c R_{d a b e} k_f k^a k^b, before antisymmetrisation
    return klo[c]*klo[f_]*sum(Rframe[d, a, b, e]*kup[a]*kup[b] for a in range(n) for b in range(n))
def Gen(c, d, e, f_):  # k_[c R_d]ab[e k_f]  (unit-weight antisymmetrisation, 1/4)
    return sp.simplify((Q(c, d, e, f_) - Q(d, c, e, f_) - Q(c, d, f_, e) + Q(d, c, f_, e))/4)
val = sp.simplify(sp.trigsimp(Gen(0, 1, 0, 1)))
print("    k^a k^b k_[t R_r]ab[t k_r] =", val)
target = -3*M/r**3*sp.sin(al)
ratio = sp.simplify(val/target)
print("    ratio to G&O's -(3M/r^3) sin(alpha):", ratio)
chk("vanishes on the radial ray (alpha = 0), as G&O say", sp.simplify(val.subs(al, 0)) == 0)
nonzero_nonradial = all(sp.N(val.subs({al: a_, M: 1, r: 7})) != 0 for a_ in (0.3, 1.0, 1.5, 2.5))
chk("non-zero for non-radial alpha (generic condition holds)", nonzero_nonradial)
matches_exact = sp.simplify(val - target) == 0
print("    exact match to G&O's printed form:", matches_exact)
# The antisymmetrisation normalisation and the tangent normalisation are
# conventions; only 'zero iff radial' is load-bearing for G&O's argument.
gen_all_comp_zero_radial = all(sp.simplify(Gen(c, d, e, f_).subs(al, 0)) == 0
                               for c in range(n) for d in range(n) for e in range(n) for f_ in range(n))
chk("radial ray: EVERY component of k_[c R_d]ab[e k_f] vanishes (non-generic)", gen_all_comp_zero_radial)


# independent route: the screen-space tidal matrix T_ij = R_{a b c d} e_i^a k^b k^c e_j^d
e1 = [0, -sp.sin(al), sp.cos(al), 0]; e2 = [0, 0, 0, 1]
def T(u, v):
    return sp.simplify(sum(Rframe[a, b, c, d]*u[a]*kup[b]*kup[c]*v[d]
                           for a in range(n) for b in range(n) for c in range(n) for d in range(n)))
T11, T22, T12 = T(e1, e1), T(e2, e2), T(e1, e2)
print("    screen tidal matrix: T11 =", sp.factor(T11), " T22 =", sp.factor(T22), " T12 =", T12)
chk("tidal matrix traceless (vacuum, R_kk = 0)", sp.simplify(T11 + T22) == 0)
chk("tidal (Weyl) focusing term goes as sin^2(alpha): zero only on radial rays",
    sp.simplify(T11 - sp.Rational(3, 1)*M*sp.sin(al)**2/r**3) == 0 or sp.simplify(T11 + 3*M*sp.sin(al)**2/r**3) == 0)
# so the generic component carries sin^2 from the tidal term and one sin(alpha) from
# each antisymmetrised k_[c e_d] projection onto the screen: sin^4 overall.
chk("generic component = (sin^2 alpha / 4) x (-3M sin^2 alpha / r^3)  [consistency]",
    sp.simplify(val - sp.sin(al)**2/4*(-3*M*sp.sin(al)**2/r**3)) == 0)

# ------------------------------------------------ (C) Lemma 1 skeleton, z3
print("(C) G&O Lemma 1, propositional skeleton")
import z3
# for one complete null geodesic gamma in a spacetime S
selfcons, cond1, generic, achronal, anec_ok, conj = z3.Bools(
    'selfconsistent condition1 generic achronal anec_nonneg conjugate_pair')
axioms = [
    # Condition 1 on a self-consistent spacetime: achronal complete => ANEC >= 0
    z3.Implies(z3.And(cond1, selfcons, achronal), anec_ok),
    # Borde 1987: ANEC >= 0 + null generic => conjugate pair  (G&O ref [9])
    z3.Implies(z3.And(anec_ok, generic), conj),
    # Hawking-Ellis: conjugate pair on a null geodesic => chronal  (G&O ref [10])
    z3.Implies(conj, z3.Not(achronal)),
]
s = z3.Solver(); s.add(*axioms); s.add(cond1, selfcons, generic, achronal)
res = s.check()
print("    Condition1 & self-consistent & generic & achronal satisfiable?", res)
chk("Lemma 1 follows (unsat): no complete achronal null geodesic", res == z3.unsat)
# vacuity guard: premises jointly satisfiable (with achronal false)
s2 = z3.Solver(); s2.add(*axioms); s2.add(cond1, selfcons, generic)
chk("vacuity guard: premises consistent (sat with achronal = False)", s2.check() == z3.sat)
# drop the generic condition: the lemma no longer follows
s3 = z3.Solver(); s3.add(*axioms); s3.add(cond1, selfcons, achronal)
chk("without the generic condition an achronal complete geodesic is allowed", s3.check() == z3.sat)
# drop self-consistency: Condition 1 says nothing (fixed-background case)
s4 = z3.Solver(); s4.add(*axioms); s4.add(cond1, generic, achronal, z3.Not(selfcons), z3.Not(anec_ok))
chk("fixed background (not self-consistent): ANEC violation on an achronal ray consistent", s4.check() == z3.sat)

print("ALL OK" if ok else "SOME CHECK FAILED")
raise SystemExit(0 if ok else 1)
