#!/usr/bin/env python3
"""register_review.py — is every entry self-explanatory where it needs to be?

M's instruction: a full register review and audit. Read it all, check that it
is self-explanatory where it needs to be, see whether gaps can be filled from
the mathematics itself, then assess a new list of open problems.

THE TEST, DECLARED BEFORE THE RUN. An entry is SELF-CONTAINED when a reader
who has not read the rest of the register can tell what it claims and how it
was checked. The failure modes are mechanical enough to find:

  A  BARE BACK-REFERENCE   "as 1391 found" with no restatement of WHAT it found
  B  UNSOURCED FIGURE      a number with no method, script, or citation
  C  DANGLING PRONOUN      opens with "It" / "That" / "This" and no antecedent
  D  ORPHAN OBJECT         names an object never defined anywhere
  E  UNRESOLVED PROMISE    "will be tested" / "next session" never followed up
  F  NAKED CLAIM           a verdict word with no supporting number

None of these is fatal alone. A back-reference is fine if the entry restates
what it refers to. What matters is entries carrying SEVERAL at once, and
entries whose central claim is unreachable without another entry in hand.

This script FINDS candidates. It does not judge them — the reading does.
"""
import re

# PR5 skip list, closed at register 1617. These five carry an asterisk that
# IS the notation — Λ*, a wildcard tuple, Python [w]*n, a jK parity marker,
# and the glob vi_*. Balancing them as markup would change what they say.
SKIP_PARITY = {313, 604, 668, 747, 1003}

from collections import Counter, defaultdict

SRC = "/home/claude/work/REGISTER-DATA.md"
raw = open(SRC, encoding="utf-8").read()
H = re.compile(r"^ {0,3}((?:\d{3,4}, )*\d{3,4})\. ", re.M)
ms = list(H.finditer(raw))

ENT = {}
ORDER = []
for i, m in enumerate(ms):
    e = ms[i + 1].start() if i + 1 < len(ms) else len(raw)
    body = re.sub(r"\s+", " ", raw[m.end():e]).strip()
    for num in re.findall(r"\d{3,4}", m.group(1)):
        ENT[int(num)] = body
    ORDER.append(int(re.findall(r"\d{3,4}", m.group(1))[0]))

print(f"  REGISTER REVIEW — {len(ms)} headings, {len(ENT)} numbers\n")

# ---- A. back-references, and whether they are restated -------------------
REF = re.compile(r"\b(?:register|registers|R)\s+(\d{3,4})", re.I)
bare = []
for n in ORDER:
    b = ENT[n]
    refs = set(int(x) for x in REF.findall(b))
    if not refs:
        continue
    # a reference is RESTATED if the sentence containing it also carries a
    # number, a quoted phrase, or a colon-introduced restatement
    for r in refs:
        seg = ""
        for s in re.split(r"(?<=[.!?]) ", b):
            if re.search(rf"\b(?:register|registers|R)\s+{r}\b", s, re.I):
                seg = s
                break
        has = bool(re.search(r"\d|'|\"|—|:", seg))
        if not has:
            bare.append((n, r, seg[:90]))

print("  A · BARE BACK-REFERENCES — cite an entry without restating it\n")
print(f"    found: {len(bare)}")
for n, r, s in bare[:10]:
    print(f"      {n} → {r}:  …{s}…")

# ---- C. dangling openers -------------------------------------------------
OPEN = re.compile(r"^\*{0,2}(It|That|This|These|Those|They|Both|Neither|Such)\b")
dang = [n for n in ORDER if OPEN.match(ENT[n].lstrip("*"))]
print(f"\n  C · ENTRIES OPENING ON A PRONOUN WITH NO ANTECEDENT\n")
print(f"    found: {len(dang)}  {dang[:14]}")

# ---- E. unresolved promises ---------------------------------------------
PROM = re.compile(r"\b(will be (?:tested|checked|run|built|written|done)|"
                  r"next session|to be (?:done|tested|checked)|remains to|"
                  r"not yet (?:run|built|tested|written)|owed)\b", re.I)
prom = [(n, PROM.search(ENT[n]).group(0)) for n in ORDER if PROM.search(ENT[n])]
print(f"\n  E · UNRESOLVED PROMISES\n")
print(f"    found: {len(prom)}")
for n, p in prom[:12]:
    print(f"      {n}: '{p}'")

# ---- D. orphan objects ---------------------------------------------------
OBJ = re.compile(r"\b([A-Z][a-z]?\.[a-z][a-z0-9]+)\b")
named = Counter()
for n in ORDER:
    for o in set(OBJ.findall(ENT[n])):
        named[o] += 1
try:
    import sys
    sys.path.insert(0, "/home/claude/work")
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        import mathreg
    defined = set(mathreg.REG)
except Exception:
    defined = set()
orphan = {o: c for o, c in named.items() if o not in defined}
print(f"\n  D · OBJECTS NAMED IN THE REGISTER BUT NOT IN mathreg.py\n")
print(f"    objects named   : {len(named)}")
print(f"    defined in reg  : {len(defined)}")
print(f"    ORPHANS         : {len(orphan)}")
for o, c in sorted(orphan.items(), key=lambda x: -x[1])[:14]:
    print(f"      {o:<18}{c:>4} mention(s)")
