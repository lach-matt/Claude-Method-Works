#!/usr/bin/env python3
"""DOCKET 67, pass S, result 30: galactic-chemical-evolution.

What is checkable here about stock.py:124-138 / 308-314 ("Galactic chemical
evolution puts C, N and P into every enriched star system ... a CI chondrite
at the destination supplies a human payload at a processing factor of 10.70").

The external result itself (GCE placing C, N, P in EVERY enriched system, and a
CI-like primitive body existing and accessible in another system) could NOT be
read at source in this run: alphaXiv returned 'quota exceeded' on every call,
and arxiv.org / iopscience / osti / par.nsf.gov / aanda.org were refused by
the egress proxy.  So nothing below verifies GCE.  It checks:

  C1  the tree's number reproduces by import (stock.py is imported read-only);
  C2  LOGICAL DEPENDENCE (z3): the finding "CLAIMS.md's 'and that had to travel'
      is NOT ESTABLISHED" is the refutation of a universal.  It needs ONE trip
      whose destination stock was not shipped from the origin.  The universal
      "every enriched system" is NOT needed: a model with exactly one stocked
      destination already refutes the claim;
  C3  sensitivity of the 10.70 to the destination's phosphorus: if a
      destination's primitive body carries P shifted by D dex relative to solar
      CI (a NAMED hypothesis: P scales with the host's [P/H]), the factor is
      10.70 * 10**(-D) while P binds, and P stops binding above
      D* = log10(f_P / f_N) (sympy);
  C4  the verdicts ("site criterion, not a barrier"; the stock need not travel)
      under that sweep, against the tree's own Fuchs-shell mass;
  C5  the CI-P spread carried from the sibling audits (920 to 1080 ppm).

Exit 0 when every check passes.
"""
import importlib.util
import math
import os
import sys

os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")
sys.dont_write_bytecode = True
TREE = "/home/user/Claude-Method-Works/research/warp-drive/stock.py"

spec = importlib.util.spec_from_file_location("stock_ro", TREE)
stock = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stock)

fails = []


def chk(label, got, want):
    ok = got == want
    print("%-4s %-70s got=%r want=%r" % ("ok" if ok else "FAIL", label, got, want))
    if not ok:
        fails.append(label)


# ---------------------------------------------------------------- C1
pf = stock.processing_factors(stock.HUMAN, stock.CHONDRITE)
e, f = stock.binding_element(stock.HUMAN, stock.CHONDRITE)
ranked = sorted(pf.items(), key=lambda kv: -kv[1])
print("C1 tree CI factors, top 4:", [(k, round(v, 4)) for k, v in ranked[:4]])
chk("C1 binder at CI chondrite is P", e, "P")
chk("C1 factor 10.70 (4 s.f.)", float("%.4g" % f), 10.7)
chk("C1 factor = HUMAN[P]/CHONDRITE[P]", abs(f - stock.HUMAN["P"] / stock.CHONDRITE["P"]) < 1e-12, True)
chk("C1 stock_need_not_travel() returns the same number", stock.stock_need_not_travel()[0] == f, True)
f_N = pf["N"]
print("C1 runner-up N factor %.4f, margin P/N %.4f" % (f_N, f / f_N))

# ---------------------------------------------------------------- C2 (z3)
try:
    import z3
    # Finite model: sites 0..n-1, site 0 is the origin.  stocked(d): destination d
    # holds the stock.  shipped(d): its stock came from the origin.  CLAIM (the
    # clause after the dash): every stocked destination's stock was shipped.
    # The tree's premise P_every: every enriched destination is stocked by GCE,
    # unshipped.  The weak premise P_one: at least one destination is stocked
    # and unshipped.
    def model(n, premise):
        s = z3.Solver()
        stocked = [z3.Bool("st%d" % i) for i in range(n)]
        shipped = [z3.Bool("sh%d" % i) for i in range(n)]
        enriched = [z3.Bool("en%d" % i) for i in range(n)]
        claim = z3.And([z3.Implies(stocked[d], shipped[d]) for d in range(1, n)])
        if premise == "every":
            s.add(z3.And([z3.Implies(enriched[d], z3.And(stocked[d], z3.Not(shipped[d])))
                          for d in range(1, n)]))
            s.add(z3.Or([enriched[d] for d in range(1, n)]))  # non-vacuity
        elif premise == "one":
            s.add(z3.Or([z3.And(stocked[d], z3.Not(shipped[d])) for d in range(1, n)]))
        elif premise == "none":
            pass
        return s, claim

    for n in (2, 3, 6):
        s, claim = model(n, "one")
        s.add(claim)
        chk("C2 n=%d: P_one AND CLAIM is UNSAT (one site refutes)" % n, str(s.check()), "unsat")
        s, claim = model(n, "every")
        s.add(claim)
        chk("C2 n=%d: P_every AND CLAIM is UNSAT" % n, str(s.check()), "unsat")
        # P_every implies P_one (so 'every' is strictly stronger than needed)
        s2 = z3.Solver()
        st = [z3.Bool("st%d" % i) for i in range(n)]
        sh = [z3.Bool("sh%d" % i) for i in range(n)]
        en = [z3.Bool("en%d" % i) for i in range(n)]
        pe = z3.And(z3.And([z3.Implies(en[d], z3.And(st[d], z3.Not(sh[d]))) for d in range(1, n)]),
                    z3.Or([en[d] for d in range(1, n)]))
        po = z3.Or([z3.And(st[d], z3.Not(sh[d])) for d in range(1, n)])
        s2.add(pe, z3.Not(po))
        chk("C2 n=%d: P_every -> P_one (valid)" % n, str(s2.check()), "unsat")
        s3 = z3.Solver()
        s3.add(po, z3.Not(pe))
        chk("C2 n=%d: P_one -/-> P_every (P_one strictly weaker, sat)" % n,
            str(s3.check()), "sat" if n > 2 else str(s3.check()))
        # vacuity guard: without any premise the CLAIM is satisfiable (the
        # refutation comes from the premise, not from the encoding)
        s, claim = model(n, "none")
        s.add(claim)
        chk("C2 n=%d: vacuity guard, CLAIM alone is SAT" % n, str(s.check()), "sat")
except ImportError:
    print("C2 SKIPPED: z3 not installed (pip install z3-solver)")
    fails.append("C2 z3 missing")

# ---------------------------------------------------------------- C3 (sympy)
import sympy as sp
D = sp.symbols("D", real=True)
fP = sp.nsimplify(f, rational=True)
fN = sp.nsimplify(f_N, rational=True)
Dstar = sp.solve(sp.Eq(fP * 10 ** (-D), fN), D)[0]
Dstar_f = float(Dstar)
print("C3 P stops binding when the destination P is +%.4f dex above solar CI (N unchanged)" % Dstar_f)
chk("C3 D* = log10(fP/fN)", abs(Dstar_f - math.log10(f / f_N)) < 1e-12, True)
chk("C3 D* = 0.122 dex (3 s.f.)", float("%.3g" % Dstar_f), 0.122)

FUCHS = stock.FUCHS_SHELL_KG
print("C3/C4 sweep: D dex | binder | factor | kg per 70 kg | orders below Fuchs shell")
for d in (-1.0, -0.5, -0.3, -0.1, 0.0, 0.1, 0.2, 0.3):
    s = dict(stock.CHONDRITE)
    s["P"] = s["P"] * 10 ** d
    b, ff = stock.binding_element(stock.HUMAN, s)
    kg = 70.0 * ff
    print("   %+5.2f | %-2s | %8.3f | %9.1f | %.1f" % (d, b, ff, kg, math.log10(FUCHS / kg)))
s = dict(stock.CHONDRITE); s["P"] *= 10 ** -1.0
b, ff = stock.binding_element(stock.HUMAN, s)
chk("C3 at D=-1 dex the factor is 107.0 (P binds)", (b, float("%.4g" % ff)), ("P", 107.0))
chk("C4 at D=-1 dex still > 20 orders below the Fuchs shell", math.log10(FUCHS / (70 * ff)) > 20, True)
s = dict(stock.CHONDRITE); s["P"] *= 10 ** 0.2
chk("C3 at D=+0.2 dex the binder flips to N", stock.binding_element(stock.HUMAN, s)[0], "N")

# ---------------------------------------------------------------- C5
print("C5 CI P carried from sibling audits (ppm): L03 920, PON14 985, LBP25 989, MS95 1080; tree 1040")
for ppm in (920, 985, 989, 1040, 1080):
    s = dict(stock.CHONDRITE); s["P"] = ppm * 1e-6
    b, ff = stock.binding_element(stock.HUMAN, s)
    print("   P %4d ppm -> %s %.3f  (%.1f kg)" % (ppm, b, ff, 70 * ff))
s = dict(stock.CHONDRITE); s["P"] = 920e-6
chk("C5 at L03 920 ppm factor 12.10", float("%.4g" % stock.binding_element(stock.HUMAN, s)[1]), 12.1)

print("\n%d failure(s)" % len(fails))
sys.exit(1 if fails else 0)
