#!/usr/bin/env python3
"""DOCKET 67 audit: gr-qc/9406053#escapes -- Borde's escapes as create.py uses them.

Reads (read-only):
  scratchpad/d67/src/gr-qc_9406053.txt   Borde 1994 full text (alphaXiv fullText, earlier
                                          stage of this session; md5 pinned below)
  research/warp-drive/create.py           parsed with ast, never imported or executed
  research/warp-drive/specthm.py          text search only

Checks:
  E1  source identity (md5)
  E2  every phrase create.py attributes to Borde in section 4 / ESCAPES occurs in the source
  E3  Sec. IX structure: the Euclidean route plus A], B], C] "within the general Lorentzian
      framework" = 4 routes; the tree holds 3; which one is missing
  E4  Borde's own framing is non-exhaustive ("several interesting possibilities") and he calls
      C possibly "the correct approach"
  E5  B] has two sub-routes; the second keeps Einstein's equation; B keeps causality violations
  E6  A]'s hypotheses (closed universe, mild additional assumptions); where the tree carries them
  E7  Sec. VIII's C^0 route (a further route outside Sec. IX's list)
  E8  the section number the tree cites (VIII.A) against the source (IX.A)
  E9  ESCAPES flags are literals (hand-set), so any_escape_stays_in_lorentzian_gr() = False is a
      DECLARED value, not a computed one
  E10 z3: does "no route stays in Lorentzian GR without a pathology" follow from what the source
      attributes to each route?  For the tree's three; with B's second sub-route; without
      H_closed; with C; with the C^0 route.
Exit 0 iff every check returns its recorded expectation.
"""
import ast
import hashlib
import os
import re
import sys

import z3

D67 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
SRC = os.path.join(D67, "src/gr-qc_9406053.txt")
WD = "/home/user/Claude-Method-Works/research/warp-drive"
MD5 = "17c67ada52d92fc44065246ef92fee8c"

fails = 0
n = 0


def chk(label, got, want):
    global fails, n
    n += 1
    ok = got == want
    if not ok:
        fails += 1
    print("  [%s] %s: got %r, want %r" % ("ok" if ok else "FAIL", label, got, want))


def norm(s):
    s = s.replace("’", "'").replace("–", "-").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip().lower()


raw = open(SRC, "rb").read()
print("E1 source identity")
chk("md5 of saved Borde text", hashlib.md5(raw).hexdigest(), MD5)
text = raw.decode("utf-8")
T = norm(text)

# Sec. IX span
i9 = text.index("IX. Concluding Comments")
iack = text.index("Acknowledgements")
S9 = norm(text[i9:iack])
i8 = text.index("VIII. A Few Words on Differentiability")
S8 = norm(text[i8:i9])

# --- create.py via ast (never executed)
csrc = open(os.path.join(WD, "create.py")).read()
tree = ast.parse(csrc)
ESC = None
for node in tree.body:
    if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "ESCAPES" for t in node.targets):
        ESC = ast.literal_eval(node.value)
cl = csrc.splitlines()

print("\nE2 phrases the tree attributes to Borde (section 4 and ESCAPES)")
quotes = {
    "a highly undesirable feature": "create.py:82-84, 213-214",
    "such an alteration would have to be fairly severe": "create.py:86-87, 216-217",
    "a point at infinity": "create.py:82, 213",
    "their true value is not so much that they actually rule out topology change, but rather "
    "that they allow us to pinpoint what modifications we have to make in our general framework "
    "so as to allow it": "create.py:93-96, 227-230",
}
for q, site in quotes.items():
    chk("verbatim in source: '%s...' (%s)" % (q[:40], site), norm(q) in T, True)
# 'abandons the Lorentzian framework altogether' is unquoted in the tree; source has 'abandon'
chk("tree's unquoted 'abandons the Lorentzian framework altogether' is a paraphrase of source "
    "'abandon the Lorentzian framework altogether'",
    ("abandon the lorentzian framework altogether" in S9)
    and ("abandons the lorentzian framework altogether" not in T), True)

print("\nE3 Sec. IX route count against the tree's")
subs = re.findall(r"\n([A-C]) \] ([^\n]+)", text[i9:iack])
chk("Sec. IX subsection headers", [(a, b.strip()) for a, b in subs],
    [("A", "Dropping causal compactness"), ("B", "Weakening the curvature constraints"),
     ("C", "Degenerate metrics")])
chk("Euclidean route stated before the list, as outside the Lorentzian framework",
    "abandon the lorentzian framework altogether and to use a euclidean path integral formalism. "
    "but even within the general lorentzian framework there are still several interesting "
    "possibilities" in S9, True)
routes_source = ["Euclidean", "A", "B", "C"]
tree_map = {"drop causal compactness": "A", "weaken the curvature constraints": "B",
            "Euclidean path integral": "Euclidean"}
tree_routes = [tree_map[e[0]] for e in ESC]
chk("len(create.ESCAPES)", len(ESC), 3)
chk("routes in source", len(routes_source), 4)
chk("source routes missing from the tree", sorted(set(routes_source) - set(tree_routes)), ["C"])
chk("create.py:78 heading says 'ALL THREE'", "ALL THREE" in cl[77], True)
chk("create.py:349 says 'BORDE'S THREE ESCAPES'", "BORDE'S THREE ESCAPES" in cl[348], True)
chk("create.py mentions degenerate metrics anywhere", "degenerate" in csrc.lower(), False)

print("\nE4 Borde's framing of the list")
chk("'several interesting possibilities' (non-exhaustive)", "several interesting possibilities" in S9, True)
chk("C: 'this might well prove to be the correct approach'",
    "this might well prove to be the correct approach to describing topology change" in S9, True)
chk("C: 'use these kinds of singularities in order to get topology change'",
    "use these kinds of singularities in order to get topology change" in S9, True)
chk("C: Horowitz 'even in standard general relativity (couched in first-order language)'",
    "even in standard general relativity (couched in first-order language)" in S9, True)
chk("C: causal structure 'will not necessarily be well-defined'",
    "will not necessarily be well-defined" in S9, True)
chk("intro: degenerate-metric route named as one of 'two ways in which classical evolution may be rescued'",
    "there are two ways in which classical evolution may be rescued. one way is to allow the metric "
    "to become degenerate at isolated points" in T, True)

print("\nE5 B]'s two sub-routes")
chk("B keeps causality violations: 'this would not affect the presence of causality violations'",
    "this would not affect the presence of causality violations" in S9, True)
chk("B sub-route 1: 'alter einstein's equation'", "alter einstein's equation" in S9, True)
chk("B sub-route 2: energy-condition violation large enough to violate (ii)",
    "violations of the energy conditions large enough to allow assumption (ii) to be violated" in S9, True)
chk("B sub-route 2 is tied to wormhole creation in the source",
    "some discussions of wormhole creation are, for example, based precisely on large violations "
    "of the energy condition" in S9, True)
b_entry = norm(ESC[1][2])
chk("create.ESCAPES[1] records sub-route 2", "energy" in b_entry, False)
chk("create.ESCAPES[1] records 'would not affect ... causality violations'", "causality" in b_entry, False)

print("\nE6 A]'s hypotheses")
chk("A: 'in the closed universe case'", "(in the closed universe case)" in S9, True)
chk("A: 'under some mild additional assumptions'", "under some mild additional assumptions" in S9, True)
chk("A: singularity needs 'the significant additional assumption' of an upper bound on timelike lengths",
    "only under the significant additional assumption that there is an upper bound on the lengths "
    "of certain timelike curves" in S9, True)
a_entry = norm(ESC[0][2])
chk("create.ESCAPES[0] carries the closed-universe case", "closed" in a_entry, False)
sp = open(os.path.join(WD, "specthm.py")).read()
chk("specthm.py carries H_closed (closed-universe case of Tipler's Theorem 5)",
    '"H_closed": ("the closed-universe case of Tipler\'s Theorem 5' in sp, True)
chk("specthm PROP_TEXT: open/asymptotically-flat case 'no source here forces either'",
    "flat universe that drops causal compactness no" in sp and "source here forces either" in sp, True)

print("\nE7 Sec. VIII: the C^0 route")
chk("'need not be diffeomorphic, even if causality violations are forbidden'",
    "need not be diffeomorphic, even if causality violations are forbidden" in S8, True)
chk("create.py names the C^0 route", ("continuous" in csrc.lower() and "c^0" in csrc.lower()), False)

print("\nE8 section citation")
chk("specthm.py cites 'section VIII.A' / 'VIII.A' for the escapes",
    len(re.findall(r"VIII\.A", sp)) >= 2, True)
chk("source Sec. VIII is 'A Few Words on Differentiability'", "VIII. A Few Words on Differentiability" in text, True)
chk("the escapes are in Sec. IX", "a ] dropping causal compactness" in S9, True)

print("\nE9 the ESCAPES flags are literals")
esc_node = [nd for nd in tree.body if isinstance(nd, ast.Assign)
            and any(getattr(t, "id", "") == "ESCAPES" for t in nd.targets)][0]
flags_literal = all(isinstance(el.elts[1], ast.Constant) for el in esc_node.value.elts)
chk("every in-GR flag in ESCAPES is an ast.Constant (hand-set, not computed)", flags_literal, True)
chk("the flags", [e[1] for e in ESC], [False, False, False])

print("\nE10 z3: does 'no route stays in Lorentzian GR without a pathology' follow?")
# Per route r: G_r = the route stays in Lorentzian GR (smooth non-degenerate Lorentz metric,
# Einstein's equation unaltered); P_r = it carries a pathology in the tree's sense
# (M-S1A-P3: a closed causal curve, a singularity, or a point at infinity).
# Source-attributed facts ONLY; anything the source leaves open is left free.
R = ["Euc", "A_closed", "A_open", "B1_alterEinstein", "B2_ECviolation", "C_degenerate", "C0_metric"]
G = {r: z3.Bool("G_" + r) for r in R}
P = {r: z3.Bool("P_" + r) for r in R}
facts = {
    # "abandon the Lorentzian framework altogether"
    "Euc": [z3.Not(G["Euc"])],
    # Tipler Thm 5, closed-universe case, mild additional assumptions: singularity or point at infinity
    "A_closed": [P["A_closed"]],
    # open universe, cc dropped: the source forces nothing ("cut and truncated in an entirely arbitrary manner")
    "A_open": [],
    # altering Einstein's equation leaves GR
    "B1_alterEinstein": [z3.Not(G["B1_alterEinstein"])],
    # EC violation keeps Einstein's equation; cc kept, so Thm 1's CTC stays:
    # "would not affect the presence of causality violations"
    "B2_ECviolation": [G["B2_ECviolation"], P["B2_ECviolation"]],
    # degenerate at isolated points: Borde lists it 'within the general Lorentzian framework' and
    # calls the points 'these kinds of singularities'; whether that is a departure or a pathology in
    # the tree's sense is not fixed by the source -> free
    "C_degenerate": [],
    # C^0 metric, causal structure only: S1, S2 need not be diffeomorphic without causality violation
    # -> P false for the CTC; whether C^0 'stays in GR' (no curvature, no dynamics) is free
    "C0_metric": [],
}


def claim(rs):
    return z3.And([z3.Not(z3.And(G[r], z3.Not(P[r]))) for r in rs])


def status(rs):
    base = [f for r in rs for f in facts[r]]
    s1 = z3.Solver(); s1.add(base); s1.add(z3.Not(claim(rs)))
    s2 = z3.Solver(); s2.add(base); s2.add(claim(rs))
    neg, pos = s1.check(), s2.check()
    s0 = z3.Solver(); s0.add(base)
    assert s0.check() == z3.sat, "vacuity: source facts inconsistent for %r" % rs
    if neg == z3.unsat:
        return "FOLLOWS"
    if pos == z3.unsat:
        return "REFUTED"
    return "UNDETERMINED"


cases = [
    ("tree's three under H_closed (Euc, A_closed, B1)", ["Euc", "A_closed", "B1_alterEinstein"], "FOLLOWS"),
    ("+ B's second sub-route (EC violation)", ["Euc", "A_closed", "B1_alterEinstein", "B2_ECviolation"], "FOLLOWS"),
    ("tree's three WITHOUT H_closed (A open)", ["Euc", "A_open", "B1_alterEinstein"], "UNDETERMINED"),
    ("Borde's four under H_closed (+ C degenerate)",
     ["Euc", "A_closed", "B1_alterEinstein", "B2_ECviolation", "C_degenerate"], "UNDETERMINED"),
    ("+ Sec. VIII C^0 route", ["Euc", "A_closed", "B1_alterEinstein", "B2_ECviolation", "C0_metric"],
     "UNDETERMINED"),
]
for label, rs, want in cases:
    chk(label, status(rs), want)

# C under each definitional reading
def with_reading(rs, extra):
    base = [f for r in rs for f in facts[r]] + extra
    s = z3.Solver(); s.add(base); s.add(z3.Not(claim(rs)))
    return "FOLLOWS" if s.check() == z3.unsat else "FAILS"

four = ["Euc", "A_closed", "B1_alterEinstein", "B2_ECviolation", "C_degenerate"]
chk("C read as Borde's word 'singularities' (P_C true)", with_reading(four, [P["C_degenerate"]]), "FOLLOWS")
chk("C read as Garcia-Heveling's 'nothing special happens' and inside GR (G_C, not P_C)",
    with_reading(four, [G["C_degenerate"], z3.Not(P["C_degenerate"])]), "FAILS")
chk("C read as leaving standard (second-order, non-degenerate) GR (not G_C)",
    with_reading(four, [z3.Not(G["C_degenerate"])]), "FOLLOWS")

# the specthm encoding: created & ~cc -> pathology v nongr, under H_closed (Tipler: pathology)
cr, cc, pa, ng, hc = z3.Bools("created cc pathology nongr H_closed")
tipler = z3.Implies(z3.And(hc, cr, z3.Not(cc)), pa)
enc = z3.Implies(z3.And(cr, z3.Not(cc)), z3.Or(pa, ng))
s = z3.Solver(); s.add(tipler, hc, z3.Not(enc))
chk("specthm BORDE-ESCAPES formula implied by Tipler Thm 5 under H_closed", s.check(), z3.unsat)
s = z3.Solver(); s.add(tipler, z3.Not(hc), z3.Not(enc))
chk("... and not implied without H_closed", s.check(), z3.sat)

print("\n%d checks, %d failures" % (n, fails))
sys.exit(1 if fails else 0)
