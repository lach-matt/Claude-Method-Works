#!/usr/bin/env python3
"""DOCKET 67 -- audit 21/36, hep-th/0302039#domain (Popov 2003, the domain of the
AHS approximation as hpscentre.py uses it).

WHAT IS AND IS NOT CHECKABLE HERE.  The result audited is a DOMAIN statement --
"the AHS approximation has been derived or established only for asymptotically
flat spacetimes (Popov p.1, eq. (70), Sec. VI)" -- i.e. a claim about what a paper
(and, through "only", the literature) says.  It has no closed form to re-derive.
Popov's text could NOT be read this session (alphaXiv: 'assistant quota
exceeded' on get_paper_content, answer_pdf_queries and discover_papers;
arxiv.org / export.arxiv.org / alphaxiv.org / semanticscholar / inspirehep all
refused by the egress proxy with 403).  So this script checks only what is
finite and local:

  C1  sympy: the unit map the tree uses when it transcribes Popov's (B1)-(B3)
      against HPS (5)-(7): 8 pi / (46080 pi^2) = K^2 with K^2 = 1/(5760 pi).
  C2  z3: the tree's two readings of "the AHS approximation" against the tree's
      OWN Sec. IV reading of Popov (hpscentre.py:96-98).  R1 = "the AHS
      EXPRESSION (T)^(4) was derived only under asymptotic flatness";
      R2 = "the APPROXIMATION <T> ~ (T)^(4) (i.e. neglect/control of the
      low-frequency remainder) was established only under asymptotic flatness".
      Encoding (propositional, deliberately minimal; it checks the SCOPE of a
      word, not physics):
        HF_needs_AF  : the high-frequency part's derivation uses AF
        LF_needs_AF  : the low-frequency part's computation uses AF
        expr_is_HF   : the AHS expression IS the high-frequency part (tree, after Popov eq. (67))
        tree_secIV   : expr_is_HF and not HF_needs_AF and LF_needs_AF   (hpscentre.py:96-98)
        R1           : expr_is_HF -> HF_needs_AF   (expression derived only under AF)
        R2           : LF_needs_AF                 (approximation established only under AF)
      Expected: tree_secIV & R1 UNSAT, tree_secIV & R2 SAT.  Guards: vacuity
      (tree_secIV alone SAT) and a control (dropping 'not HF_needs_AF' makes R1 SAT).
  C3  text consistency: DOMAIN_WORD's clause is carried identically by
      hpscentre.py, ledger.py (built from it) and LEDGER.md (generated).
  C4  the tree's side of the verdict: in the recorded selftest output,
      M_NEGATIVE_FOUND_INSIDE_DOMAIN is a RECORD pin ("printed, not counted"),
      and the non-flatness of the instances is checked (throat: HPS's own
      sentence, read from the cached HPS text layer; linear centre: section 8
      theorem; nonlinear centre: measured only for c3 K^2 = 1e-4, x <= 300 K).

Run:  python3 hep-th_0302039_domain.py      (exit 0 iff every check agrees)
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D67 = os.path.dirname(HERE)
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
SELFTEST_OUT = os.path.join(HERE, "hep-th_0302039_domain.hpscentre-selftest.out")
HPS_TEXT = os.path.join(D67, "src", "hps", "hps_0.xml")

ok = True


def chk(label, got, want):
    global ok
    good = got == want
    ok &= good
    print("  [%s] %-70s %s" % ("ok" if good else "FAIL", label, got))


print("C1  sympy: unit map")
import sympy as sp
pi = sp.pi
K2 = sp.Rational(1, 5760) / pi
chk("8 pi / (46080 pi^2) == 1/(5760 pi)", sp.simplify(8 * pi / (46080 * pi ** 2) - K2), 0)
chk("46080 / 8 == 5760", sp.Integer(46080) / 8, 5760)

print("C2  z3: scope of 'the AHS approximation' vs the tree's own Sec. IV reading")
import z3
HF, LF, EX = z3.Bools("HF_needs_AF LF_needs_AF expr_is_HF")
tree_secIV = z3.And(EX, z3.Not(HF), LF)
R1 = z3.Implies(EX, HF)
R2 = LF


def sat(*fs):
    s = z3.Solver()
    s.add(*fs)
    return str(s.check())


chk("vacuity guard: tree_secIV alone", sat(tree_secIV), "sat")
chk("tree_secIV & R1 (expression derived only under AF)", sat(tree_secIV, R1), "unsat")
chk("tree_secIV & R2 (approximation established only under AF)", sat(tree_secIV, R2), "sat")
chk("control: drop 'not HF_needs_AF' -> R1 becomes consistent", sat(z3.And(EX, LF), R1), "sat")

print("C3  text consistency of the domain clause")
CLAUSE = "only for asymptotically flat spacetimes (Popov p.1, eq. (70)"
for f in ("hpscentre.py", "LEDGER.md"):
    t = open(os.path.join(TREE, f), encoding="utf-8").read()
    t1 = re.sub(r'"\s*\n\s*"', "", t)          # join python string continuations
    t1 = re.sub(r"\s+", " ", t1)
    chk("%s carries the clause" % f, CLAUSE in t1, True)
t = open(os.path.join(TREE, "ledger.py"), encoding="utf-8").read()
chk("ledger.py builds the O5 row from hpscentre (imports it)", "hpscentre." in t, True)

print("C4  the tree's side: recorded selftest output")
if os.path.exists(SELFTEST_OUT):
    out = open(SELFTEST_OUT, encoding="utf-8").read()
    chk("hpscentre --selftest ended OK", out.rstrip().endswith("SELFTEST OK"), True)
    chk("M_NEGATIVE_FOUND_INSIDE_DOMAIN is a RECORD pin, value False",
        bool(re.search(r"\[RECORD\] M_NEGATIVE_FOUND_INSIDE_DOMAIN.*False", out)), True)
    chk("record pins are 'printed, not counted'", "printed, not counted" in out, True)
    chk("nonlinear non-flatness checked only at c3 K^2 = 1e-4, x <= 300 K",
        "[ok] c3 K^2 = 1e-4 ONLY, x <= 300 K: 2m/r not decaying" in out, True)
    chk("NONLINEAR_CENTRE_ASYMPTOTICS recorded OPEN",
        bool(re.search(r"\[RECORD\] NONLINEAR_CENTRE_ASYMPTOTICS\s+OPEN", out)), True)
else:
    print("  (selftest output missing; re-run hpscentre.py --selftest into %s)" % SELFTEST_OUT)
    ok = False
if os.path.exists(HPS_TEXT):
    h = re.sub(r"\s+", " ", open(HPS_TEXT, encoding="utf-8").read())
    chk("HPS text layer: 'the metric as a whole is not asymptotically flat'",
        "the metric as a whole is not asymptotically flat" in h, True)
    chk("HPS text layer, fn [20]: scalar mass and temperature set to zero",
        "set the scalar mass and temperature to zero" in h, True)

print("\nREDERIVE %s" % ("AGREES" if ok else "DISAGREES"))
sys.exit(0 if ok else 1)
