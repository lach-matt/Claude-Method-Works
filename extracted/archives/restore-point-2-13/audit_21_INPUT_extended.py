#!/usr/bin/env python3
"""Audit 21 INPUT, extended by one case.

INPUT (ss3.7.1): every stated result must print the data it was computed from.
As shipped it carries SEVEN HARDCODED CASES, so it tests the seven results
registers 376 and 377 exposed and nothing else.  That is the literal mechanism
ss32.1.3 names and ss28.7.8 groups five times: an instrument with a literal in
it is narrowed to the cases its author foresaw.

This adds the eighth case -- the smallest edit that catches the defect located
here -- and reports both the shipped result and the extended one, so the
difference is the finding rather than the claim.

  claim   : "nine further literatures named and unentered", asserted at
            ss29.1, ss29.2 and ss29.7.1, and pointed at from Appendix E item C
  input   : a printed list of nine literatures that have NOT been entered
  status  : Appendix E item C says "Named in ss29.7"; ss29.7's table names the
            nine literatures that HAVE been entered
"""
import re, sys

SRC = "The Method 1.6.md"
s = open(SRC, encoding="utf-8").read()

# ---- the seven cases as shipped -------------------------------------------
SHIPPED = [
    ("E(audits)",       r"E\(audits\)\s*=\s*\d+",
                        r"^\s{2,}\d{1,2}\s{3,}[A-Z]+\s{3,}(?:object|source|artefact|outside)\s{3,}"),
    ("dim(hierarchy)",  r"dimension is 2|dim\(hierarchy\) = 2", r"L1\s+CELL <|L1\s+CONSISTENCY <"),
    ("the alphabet",    r"Σ\(\|Aᵢ\| − 1\) = 17", r"A\.19\.0"),
    ("E(G)",            r"E\(G\)", r"F\.2 The coordinates"),
    ("E(Q) fibred",     r"E\(Q\) = 0",
                        r"^\s{2,}[A-P]\s{3,}\S[^\n]{0,50}\s{2,}(?:nothing|one claim)"),
    ("the second bridges", r"[Tt]wenty admissible", r"g ≤ n\s{2,}953"),
    ("the four arrows", r"one per coordinate", r"shell\s{2,}9,407"),
]

# ---- the eighth --------------------------------------------------------------
# claim regex: the book asserting a count of unentered literatures
# input regex: any line naming an unentered literature in a list of its own
CLAIM_8 = r"nine (?:more|further)?\s*(?:literatures\s+)?(?:named and|literatures named and) unentered"
INPUT_8 = r"^\s{2,}(?:unentered|not entered)\b|^\s{2,}\d\.\s+\S.*\bunentered\b"

EXTENDED = SHIPPED + [("the unentered literatures", CLAIM_8, INPUT_8)]


def run(cases):
    out = []
    for name, claim, inp in cases:
        asserted = bool(re.search(claim, s, re.M))
        printed = bool(re.search(inp, s, re.M))
        out.append((name, asserted, printed, asserted and not printed))
    return out


print("  case                         claim asserted   input printed   FAILS")
rows = run(EXTENDED)
for name, a, p, f in rows:
    print(f"  {name:<26} {str(a):>14}  {str(p):>14}   {'YES' if f else '.'}")

shipped_fails = sum(1 for r in run(SHIPPED) if r[3])
ext_fails = sum(1 for r in rows if r[3])
print(f"\n  INPUT as shipped   : {shipped_fails} failure(s) over 7 cases")
print(f"  INPUT + one case   : {ext_fails} failure(s) over 8 cases")

# ---- the supporting count, so this result prints its own inputs -------------
print("\n  the assertion, located:")
for m in re.finditer(CLAIM_8, s, re.M):
    ln = s[:m.start()].count("\n") + 1
    print(f"    line {ln:>5}   {s[m.start():m.start()+62].strip()}")

print("\n  every occurrence of 'unentered' in the source:")
for m in re.finditer(r"unentered", s):
    ln = s[:m.start()].count("\n") + 1
    lo = s.rfind("\n", 0, m.start()) + 1
    print(f"    line {ln:>5}   {s[lo:lo+96].strip()}")

named = ["partial order in chemistry (ss29.11.1, register 251)",
         "the seniority scheme, lattice-ordered (ss29.9.1, Q item N)"]
print(f"\n  unentered literatures actually named anywhere: {len(named)}")
for n in named:
    print(f"    - {n}")
print("  both were added AFTER the nine, each recorded as 'E(search) grows by one'.")
print("  of the nine themselves, none is named.")

sys.exit(ext_fails)
