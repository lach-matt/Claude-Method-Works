#!/usr/bin/env python3
"""Intake audit of Transitions v3.0 against The Method 1.4's instruments.

Nothing here is written into the book.  This is the compute step: every
checkable claim the paper makes about itself, recomputed, so that integration
carries findings rather than assertions.  Protocol 2.14 -- compute, then write.
"""
import re, math, sys
from zeno import State, step

SRC = "/mnt/user-data/uploads/Transitions.md"
s = open(SRC, encoding="utf-8").read()
L = s.split("\n")
out = []


def check(name, got, want, note=""):
    ok = (got == want) if not isinstance(want, float) else abs(got - want) < 5e-3
    out.append((name, got, want, ok, note))
    return ok


# ---- 1. audit 22's own arithmetic --------------------------------------------
per = dict(X=8, Sc=4, IC=6, U=8, NEC=7, L=4, SD=5, DNc=4, DNd=2)
check("audit22: unchecked-by-coordinate sum", sum(per.values()), 32,
      "stated UNCHECKED = 32; the row sums to the TOTAL pairs (48)")
check("audit22: checked + unchecked = pairs", 16 + 32, 48, "consistent")
check("audit22: conflations+partial+matches", 7 + 2 + 7, 16, "consistent")
check("audit22: conflation rate among checked", round(100 * 9 / 16), 56, "9/16")

# ---- 2. densities -------------------------------------------------------------
for nm, cells, box, want in [("periodic table", 90, 126, 71.43),
                             ("Lambda_8", 976, 6912, 14.12),
                             ("violation(15)", 18072, 622080, 2.91),
                             ("violation(9)", 2370, 19440, 12.19),
                             ("Lambda_13", 199130, 47775744, 0.42),
                             ("axis index", 9, 5184, 0.17),
                             ("charger index", 6, 192, 3.1)]:
    check(f"density {nm}", round(100 * cells / box, 2), want)

# ---- 3. the fifteen-letter arithmetic ----------------------------------------
check("15-letter: |R(X)| = cells + E", 18072 + 816, 18888, "= 37,776 / 2")
check("15-letter: half of 37,776", 37776 // 2, 18888, "SD_field cut")
check("15-letter: collapse exact", 1 * 816, 816)
check("9-letter: collapse exact", 1 * 30, 30)

# ---- 4. the product formula, D10 ---------------------------------------------
def E_prod(nA, EA, nB, EB):
    return nA * EB + nB * EA + EA * EB
check("D10 on Lambda x violation(9)", E_prod(976, 0, 2370, 30), 29280)

# ---- 5. the possibility bound, audit 27 --------------------------------------
# 0 <= E <= box - cells, applied to every (cells, box, E) triple the paper prints
triples = [("periodic table", 90, 126, 36), ("Lambda_8", 976, 6912, 0),
           ("violation(15)", 18072, 622080, 816), ("violation(9)", 2370, 19440, 30),
           ("Lambda_13", 199130, 47775744, 0), ("axis index", 9, 5184, 499),
           ("charger index", 6, 192, 25), ("V3 geometry", 25, 48, 0),
           ("V6 solution", 14, 24, 0), ("null surface", 32, 64, 0),
           ("ANEC proofs", 8, 12, 0), ("slide, 15 letters", 1, 40, 5),
           ("slide, withdrawn", 1, 40, 8856)]
for nm, c, b, e in triples:
    check(f"audit27 {nm}", 0 <= e <= b - c, True, f"ceiling {b - c}")

# ---- 6. molecular decay: text says 1.9 per atom, figure says 2.57 ------------
atoms = [2, 3, 4, 6, 8, 10, 12]
feas = [93.7, 59.3, 27.0, 4.15, 0.594, 0.0829, 0.0122]
n = len(atoms)
mx, my = sum(atoms) / n, sum(math.log(f) for f in feas) / n
slope = (sum((a - mx) * (math.log(f) - my) for a, f in zip(atoms, feas))
         / sum((a - mx) ** 2 for a in atoms))
factor = math.exp(-slope)
check("molecular decay factor per atom", round(factor, 2), 2.57,
      "log-linear fit over all seven points; text says 'roughly 1.9'")

# ---- 7. structural / markup checks on the source -----------------------------
part10 = s[s.index("## Part X ·"):s.index("### 10.2")]
rows = [l for l in part10.split("\n") if l.startswith("| ") and "|" in l[2:]
        and "---" not in l and "letters" not in l]
check("Part X: indices in the 10.1 table", len(rows), 6,
      "the Part is titled 'Six more indices'")

# markdown tables lacking a separator row
bad_tables = []
for i, l in enumerate(L):
    if l.startswith("|") and i + 1 < len(L) and L[i + 1].startswith("|"):
        if not re.match(r"^\|[\s:|-]+\|$", L[i + 1]) and (i == 0 or not L[i - 1].startswith("|")):
            bad_tables.append((i + 1, l[:58]))
check("markup: tables with no header separator", len(bad_tables), 0)

# duplicated rows in the Open table
open_tbl = s[s.index("## Part XIII · Open"):s.index("### 12.1")]
keys = [l.split("|")[1].strip() for l in open_tbl.split("\n")
        if l.startswith("| ") and "---" not in l]
dupes = {k for k in keys if keys.count(k) > 1}
check("Part XIII: duplicated open items", len(dupes), 0, str(dupes))

# audit numbering in 12.2c
nums = sorted(int(m) for m in re.findall(r"^\| (\d\d) ", s[s.index("### 12.2c"):], re.M))
check("12.2c: audit numbers contiguous", nums == list(range(min(nums), max(nums) + 1)),
      True, f"present {nums}")
check("12.2c: heading says four blind spots", len(nums), 4, "the table carries this many audits")

# section-number sequence across Parts XI-XIII
secs = re.findall(r"^### (\d+\.\d+[a-z]?) ", s, re.M)
check("section numbers monotone", secs == sorted(secs, key=lambda t: (
    int(t.split(".")[0]), t)), True, " ".join(secs[-12:]))

# version strings
check("version: header vs body", len(set(re.findall(r"v[0-9]\.[0-9]", s)) - {"v1.4"}), 1,
      str(sorted(set(re.findall(r'v[0-9]\.[0-9]', s)))))

# abstract paragraph repeated
abst = s[s.index("## Abstract"):s.index("## Contents")]
check("abstract: BFV sentence stated once",
      abst.count("vocabulary partition is") + abst.count("partition is then derived"), 1)

# ---- report ------------------------------------------------------------------
with State("transitions-intake") as st:
    step(st, "intake checks", lambda: len(out), budget=30)

w = max(len(r[0]) for r in out)
print(f"\n  {'check':<{w}}  {'computed':>14}  {'stated':>10}   ok")
for nm, got, want, ok, note in out:
    g = f"{got:,}" if isinstance(got, int) and not isinstance(got, bool) else str(got)
    wv = f"{want:,}" if isinstance(want, int) and not isinstance(want, bool) else str(want)
    print(f"  {nm:<{w}}  {g:>14}  {wv:>10}   {'.' if ok else 'FAIL'}")
    if not ok and note:
        print(f"  {'':<{w}}  -> {note}")

fails = [r for r in out if not r[3]]
print(f"\n  {len(out) - len(fails)} of {len(out)} reproduce; {len(fails)} do not")
sys.exit(len(fails))
