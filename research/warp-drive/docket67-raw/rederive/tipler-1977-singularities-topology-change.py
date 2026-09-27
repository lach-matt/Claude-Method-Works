#!/usr/bin/env python3
"""DOCKET 67 -- audit of Tipler (1977) Theorem 5 as the warp board uses it.

Tipler, Ann. Phys. (NY) 108, 1 (1977) is NOT readable here (paywalled; arXiv,
ScienceDirect, OSTI, INSPIRE all refused by the egress proxy on 2026-09-26).
The only restatement READ is Borde gr-qc/9406053 (cached v1 text,
d67/src/gr-qc_9406053.txt), section IX.A.  So everything below checks the
tree's use AGAINST BORDE'S RESTATEMENT, not against Tipler's own hypotheses.

  C1  verbatim: every phrase the tree attributes to Tipler/Borde IX.A is in
      the cached text, and the section the tree cites (VIII.A) is checked
      against the text's own headings.
  C2  z3: the tree's gated fact specthm BORDE-ESCAPES
          created & ~cc -> pathology | nongr      (under H_closed)
      is derived from Borde's restatement, with the vacuity guard, and each
      hypothesis is shown load-bearing by a countermodel.
  C3  z3: the conclusion cannot be strengthened to 'singularity' without
      Borde's 'significant additional assumption' (upper bound on lengths
      of timelike curves); the tree does not so strengthen it (checked in C1).
  C4  z3, CONDITIONAL: IF Theorem 5's unnamed 'mild additional assumptions'
      include an energy condition (the paper's abstract, seen only as a
      search-engine snippet, ties its topology-change results to 'the
      Einstein equations (and the weak energy condition)'), then an
      energy-condition-violating source escapes the fact.  Not asserted:
      shown as the dependence it would be.
Exit 0 if every check that is a check passes.
"""
import os, re, sys
import z3

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "src", "gr-qc_9406053.txt")
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
fails = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (" -- " + detail if detail else ""))
    if not ok:
        fails.append(name)


# ------------------------------------------------------------------ C1
txt = open(SRC, encoding="utf-8").read()
flat = re.sub(r"\s+", " ", txt)
quotes = [
    "there is the theorem of Tipler (ref. [8], Theorem 5)",
    "(in the closed universe case) that if topology change",
    "occurs via a non-compact interpolating spacetime, then it contains (under some "
    "mild additional assumptions) a singularity (in the sense of an incomplete timelike "
    "geodesic) or a point at infinity",
    "That it is a singularity that must occur may be inferred only under the "
    "significant additional assumption that there is an upper bound on the lengths "
    "of certain timelike curves in the region of interest",
    "the singularity may be pushed to infinity",
    "the presence of points at infinity is still a highly undesirable feature",
    "Compactness assumptions are not made in this theorem, and topology change is "
    "then shown to lead to singularities, but only under a significant additional "
    "assumption",
    "F.J. Tipler, Ann. of Physics (NY), 108, 1 (1977)",
]
# the page break "34" falls inside the third quote; remove bare page numbers
flat_np = re.sub(r" \d{1,2} (?=[a-z(])", " ", flat)
for q in quotes:
    # the page-number strip must not be applied to the reference line
    check("C1 verbatim: " + q[:60] + "...", q in flat_np or q in flat)

heads = {m.group(1): m.start() for m in re.finditer(
    r"\n(VIII\. A Few Words on Differentiability|IX\. Concluding Comments)", txt)}
posA = txt.find("A ] Dropping causal compactness")
viii = heads.get("VIII. A Few Words on Differentiability", -1)
ix = heads.get("IX. Concluding Comments", -1)
check("C1 section: 'Dropping causal compactness' sits under IX, not VIII",
      0 < viii < ix < posA,
      "VIII@%d IX@%d IX.A@%d -> tree's 'section VIII.A' (specthm.py:587, 1850) is a "
      "citation discrepancy for IX.A" % (viii, ix, posA))

# the tree's own words: disjunctive, never 'singularity' alone
create_src = open(os.path.join(TREE, "create.py"), encoding="utf-8").read()
spec_src = open(os.path.join(TREE, "specthm.py"), encoding="utf-8").read()
check("C1 tree keeps the disjunction (create.py ESCAPES[0])",
      "Tipler: a singularity or A POINT AT INFINITY" in create_src)
check("C1 tree scopes to the closed case only in specthm (H_closed)",
      "the closed-universe case of Tipler's Theorem 5" in spec_src
      and "closed" not in create_src[create_src.find("DROP CAUSAL COMPACTNESS"):
                                     create_src.find("WEAKEN THE CURVATURE")].lower(),
      "create.py:81-84 omits 'closed universe'; specthm.py:586-589 restores it")
check("C1 status drift recorded: specthm.py claims Tipler READ",
      "rests on papers READ (Geroch, Borde gr-qc/9406053, " in spec_src
      and '"Tipler), not on a module"' in spec_src,
      "specthm.py:1133-1134 lists Tipler among papers READ; the 1977 paper is "
      "NAMED-NOT-READ (only Borde's restatement is READ)")

# ------------------------------------------------------------------ C2
B = z3.Bools("closed created cc compact mild sing pinf ubound nongr EC")
closed, created, cc, compact, mild, sing, pinf, ubound, nongr, EC = B
pathology = z3.Or(sing, pinf)          # PROP_TEXT: 'a singularity or a point at infinity'

T5 = z3.Implies(z3.And(closed, created, z3.Not(compact), mild), z3.Or(sing, pinf))
T5_sing = z3.Implies(z3.And(closed, created, z3.Not(compact), mild, ubound), sing)
# Borde II.C (READ): closed universe, M compact => 'trivially causally compact'
CPT_CC = z3.Implies(z3.And(closed, compact), cc)
premises = z3.And(T5, T5_sing, CPT_CC)

f_tree = z3.Implies(z3.And(created, z3.Not(cc)), z3.Or(pathology, nongr))
f_strict = z3.Implies(z3.And(created, z3.Not(cc)), pathology)


def entails(hyps, goal):
    s = z3.Solver(); s.add(hyps, z3.Not(goal))
    r = s.check()
    return r == z3.unsat, (s.model() if r == z3.sat else None)


def sat(*fs):
    s = z3.Solver(); s.add(*fs); return s.check() == z3.sat


check("C2 vacuity guard: premises & closed & mild & created & ~cc satisfiable",
      sat(premises, closed, mild, created, z3.Not(cc)))
ok, _ = entails(z3.And(premises, closed, mild), f_tree)
check("C2 tree fact BORDE-ESCAPES follows under H_closed (= closed & mild)", ok)
ok, _ = entails(z3.And(premises, closed, mild), f_strict)
check("C2 ... and follows WITHOUT the 'nongr' disjunct (the disjunct is slack, "
      "a weakening, harmless)", ok)
ok, m = entails(z3.And(premises, mild), f_tree)
check("C2 closed-universe hypothesis is load-bearing (countermodel without it)",
      not ok, "countermodel: %s" % m)
ok, m = entails(z3.And(premises, closed), f_tree)
check("C2 Tipler's 'mild additional assumptions' are load-bearing",
      not ok, "countermodel: %s" % m)
ok, m = entails(z3.And(T5, T5_sing, closed, mild), f_tree)
check("C2 the step ~cc => ~compact (Borde II.C) is load-bearing: Theorem 5 is "
      "stated for NON-COMPACT M, the tree for NOT CAUSALLY COMPACT M", not ok,
      "countermodel without CPT_CC: %s" % m)

# ------------------------------------------------------------------ C3
ok, m = entails(z3.And(premises, closed, mild),
                z3.Implies(z3.And(created, z3.Not(cc)), sing))
check("C3 'singularity' alone is NOT forced without the upper-bound assumption",
      not ok, "countermodel: %s" % m)
ok, _ = entails(z3.And(premises, closed, mild, ubound),
                z3.Implies(z3.And(created, z3.Not(cc)), sing))
check("C3 ... and IS forced once Borde's 'significant additional assumption' holds", ok)

# ------------------------------------------------------------------ C4 (conditional)
T5_ec = z3.Implies(z3.And(closed, created, z3.Not(compact), mild, EC), z3.Or(sing, pinf))
prem_ec = z3.And(T5_ec, CPT_CC)
ok, m = entails(z3.And(prem_ec, closed, mild, z3.Not(EC)), f_strict)
check("C4 CONDITIONAL: if Theorem 5 carries an energy condition, a source that "
      "violates it is not forced into a pathology", not ok,
      "countermodel: %s  -- NOT asserted: whether EC is among Tipler's "
      "hypotheses is unread here" % m)
ok, _ = entails(z3.And(prem_ec, closed, mild, EC), f_strict)
check("C4 ... with the energy condition in force the fact is recovered", ok)

print()
print("RESULT: %d failure(s)" % len(fails))
sys.exit(1 if fails else 0)
