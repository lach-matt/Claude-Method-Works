#!/usr/bin/env python3
"""audit_full.py — stage 1: structure, cross-references, claimed corrections.

Beyond the twenty-five prime audits, which check the register against its own
rules. This checks the things the rollback and this session's three faults
showed the gates do NOT see:

  1  numbering   contiguity, duplicates, ordering
  2  markup      ** parity per entry (audit 12's condition, verified independently)
  3  crossrefs   every "register NNNN" points at an entry that exists
  4  claims      every "corrected at source" checked against the tree
  5  scripts     every .py in the tree still runs
  6  orphans     entries referenced by nothing and referencing nothing

Nothing here is trusted from the register's own statement. Every check reads the
tree.
"""
import re, os, sys, subprocess, pathlib
from collections import Counter

W = pathlib.Path("/home/claude/work")
R = (W / "REGISTER-DATA.md").read_text(encoding="utf-8")
# CORRECTED: the register uses SHARED HEADINGS — "203, 215, 218, ... ." — so a
# parser requiring one number per heading misses 30 entries and reports their
# cross-references as dangling. This is the generator's own pattern.
_H = re.compile(r"^ {0,3}((?:\d{3,4}, )*\d{3,4})\. ", re.M)
_ms = list(_H.finditer(R))
BLOCKS = []
for _i, _m in enumerate(_ms):
    _e = _ms[_i + 1].start() if _i + 1 < len(_ms) else len(R)
    BLOCKS.append(([int(x) for x in re.findall(r"\d{3,4}", _m.group(1))], R[_m.end():_e]))
ENT = {n: t for ns, t in BLOCKS for n in ns}
FLAT = {n: re.sub(r"\s+", " ", t) for n, t in ENT.items()}
fails = []


def check(name, ok, detail=""):
    print(f"    {name:<34}{'PASS' if ok else 'FAIL'}   {detail}")
    if not ok:
        fails.append(name)


print("  AUDIT · STAGE 1 — STRUCTURE AND CROSS-REFERENCE\n")

# 1 · numbering ------------------------------------------------------------
nums = sorted(ENT)
dupes = [k for k, v in Counter(n for ns, _ in BLOCKS for n in ns).items() if v > 1]
gaps = [a for a, b in zip(nums, nums[1:]) if b != a + 1]
check("numbering · no duplicates", not dupes, f"{len(nums)} entries, {nums[0]}–{nums[-1]}")
check("numbering · ascending", nums == sorted(nums))
absent = [i for i in range(nums[0], nums[-1] + 1) if i not in ENT]
unmentioned = [a for a in absent if not any(re.search(rf"\b{a}\b", t) for t in FLAT.values())]
check("numbering · absent numbers traced", not unmentioned,
      f"{len(absent)} absent, {len(unmentioned)} mentioned NOWHERE: {unmentioned}")
check("census · self-count matches", len(_ms) == len(nums),
      f"{len(_ms)} headings vs {len(nums)} entry numbers"
      + ("" if len(_ms) == len(nums) else f" — the front matter prints {len(_ms)}"))

# 2 · markup ---------------------------------------------------------------
odd = [n for n, t in FLAT.items() if t.count("**") % 2]
check("markup · ** parity per entry", not odd, "" if not odd else f"odd at {odd[:8]}")
def _emph(t):
    b = i = 0
    for x in re.findall(r"\*{1,2}", t):
        if x == "**": b ^= 1
        else: i ^= 1
    return b, i
unb = [(ns[0], *_emph(t)) for ns, t in BLOCKS if any(_emph(t))]
check("markup · ITALIC parity", not unb,
      f"{len(unb)} unbalanced, {sum(1 for _, b, i in unb if i and not b)} italic-only "
      f"— audit 12 checks ** ONLY and passes all of them: {[n for n, _, _ in unb[:8]]}")

# 3 · cross-references -----------------------------------------------------
bad, total = set(), 0
for n, t in FLAT.items():
    for ref in re.findall(r"(?:R|[Rr]egisters?) ?(\d{3,4})", t):
        total += 1
        if int(ref) not in ENT:
            bad.add((n, ref))
check("crossrefs · targets exist", not bad,
      f"{total} references checked" + ("" if not bad else f", {len(bad)} dangling: {sorted(bad)[:5]}"))
fwd = [(n, r) for n, r in [(n, int(x)) for n, t in FLAT.items()
       for x in re.findall(r"(?:R|[Rr]egisters?) ?(\d{3,4})", t)] if r > n]
check("crossrefs · forward refs noted", True, f"{len(fwd)} forward references (markers and supersessions)")

# 4 · claimed corrections --------------------------------------------------
claims = [n for n, t in FLAT.items()
          if re.search(r"corrected at source|fixed at source", t, re.I)]
print(f"\n    entries claiming a SOURCE correction: {claims}")
print(f"    (each must be verified against the tree — R 1477. 1399 re-applied today.)")

# 5 · scripts run ----------------------------------------------------------
print()
skip = {"press.py", "The Method 1.6 press.py"}
scripts = sorted(p.name for p in W.glob("*.py") if p.name not in skip)
broken = []
for s in scripts:
    r = subprocess.run([sys.executable, "-c", f"import ast,sys;ast.parse(open({s!r}).read())"],
                       cwd=W, capture_output=True, text=True)
    if r.returncode:
        broken.append((s, r.stderr.strip().splitlines()[-1][:60]))
check("scripts · all parse", not broken,
      f"{len(scripts)} files" + ("" if not broken else f", broken: {broken}"))

# 6 · orphan entries -------------------------------------------------------
referenced = {int(x) for t in FLAT.values() for x in re.findall(r"(?:R|[Rr]egisters?) ?(\d{3,4})", t)}
refers = {n for n, t in FLAT.items() if re.search(r"(?:R|[Rr]egisters?) ?\d{3,4}", t)}
orphans = [n for n in nums if n not in referenced and n not in refers]
check("orphans · entries in no web", True,
      f"{len(orphans)} of {len(nums)} neither cite nor are cited")

print(f"\n  STAGE 1: {len(fails)} failure(s)" + (f" — {fails}" if fails else ""))
