#!/usr/bin/env python3
"""The Method 1.2 — the twenty prime audits, run as one pass.

B.2.17 defines them; B.2.22 requires them on every output. This file is the
requirement made executable, so that "audited" is a fact about a build rather
than a claim about a session.  Exit status is the number of failing audits.
"""
import re, sys, json, subprocess
from itertools import combinations, product
from collections import Counter, defaultdict

SRC = "The Method 1.2.md"
PDF = "/mnt/user-data/outputs/The Method 1.2.pdf"

s   = open(SRC, encoding="utf-8").read()
txt = subprocess.run(["pdftotext", PDF, "-"], capture_output=True, text=True).stdout
RS, RE_ = s.rindex("## 21. Withdrawals"), s.rindex("## 22.")
reg = s[RS:RE_]
inreg = lambda p: RS < p < RE_
V, NOTE = {}, {}

# ---------------------------------------------------------------- the object
from method_tower import base, terms, exact_2S, phihat
L = base((3, 3, 1, 3, 1)); S = set(L); D = 8
byr = {}
for c in L: byr.setdefault(sum(c), []).append(c)
leq = lambda a, b: all(x <= y for x, y in zip(a, b))
J = sorted([x for x in L if len([y for y in byr.get(sum(x) - 1, []) if leq(y, x)]) == 1],
           key=lambda c: (sum(c), c))

def RR(X, d):
    vals = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -99), c[i])
        b, o = -99, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in product(*vals)
            if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j)}

jf = mf = rf = 0
for a, b in combinations(L, 2):
    Jn = tuple(max(x, y) for x, y in zip(a, b)); M = tuple(min(x, y) for x, y in zip(a, b))
    jf += Jn not in S; mf += M not in S
    rf += sum(Jn) + sum(M) != sum(a) + sum(b)
rk = Counter(sum(c) for c in L)
mx = [max(c[i] for c in L) for i in range(D)]
n = len(J); below = [[j for j in range(n) if j != i and leq(J[j], J[i])] for i in range(n)]
_ds = 0
def _rec(i, ch):
    global _ds
    if i == n: _ds += 1; return
    _rec(i + 1, ch)
    if all(b in ch for b in below[i]): _rec(i + 1, ch | {i})
_rec(0, frozenset())
V["1 LATTICE"] = (jf + mf + rf + (len(RR(L, D)) - 976) + (len(J) != 17) + (_ds != 976)
                  + (sum(rk.values()) != 976) + (sum(v * (-1) ** r for r, v in rk.items()) != 2)
                  + (sum(1 for c in L if tuple(mx[i] - c[i] for i in range(D)) in S) != 8))

chi = lambda x: (1 <= x[0] and 0 <= x[1] <= x[0] - 1 and 1 <= x[2] <= 4 * x[1] + 2
                 and 0 <= x[3] <= x[2] and 0 <= x[7] <= x[2] and 1 <= x[4]
                 and 0 <= x[5] <= x[4] - 1 and 0 <= x[6] <= min(4 * x[5] + 2, x[3]))
V["8 CELL"] = sum(1 for c in L if not chi(c))

W = {c: sum(1 << i for i, g in enumerate(J) if leq(g, c)) for c in L}
orf = andf = 0
for a, b in combinations(L, 2):
    orf += W[tuple(max(x, y) for x, y in zip(a, b))] != (W[a] | W[b])
    andf += W[tuple(min(x, y) for x, y in zip(a, b))] != (W[a] & W[b])
V["9 DISTINCTNESS"] = (len(L) - len(set(L))) + (len(L) - len(set(W.values()))) + orf + andf

ph = {k: phihat(k, 1) for k in range(4)}
L9  = [c + (x,) for c in L for x in range(0, c[6] + 1)]
L10 = [c + (v,) for c in L9 for v in range(c[8], c[6] + 1)]
L11 = [c + (j,) for c in L10 for j in range(0, ph[c[2]] + 1)]
L12 = [c + (K,) for c in L11 for K in range(0, c[10] + 3)]
L13 = [c + (x,) for c in L12 for x in range(max(0, c[11] - 1), c[11] + 2)]
Aq, Bq = defaultdict(set), defaultdict(set)
for c in L13:
    Aq[c[3]].add((c[0], c[1], c[2], c[7], c[10], c[11], c[12]))
    Bq[c[3]].add((c[4], c[5], c[6], c[8], c[9]))
a = x = 0
for c in L: a += c[6] + 1; x += len(exact_2S(c[5], c[6]))
d9 = x / a
cells = {(x_, y) for x_ in range(21) for y in range(21) if abs(x_ - y) <= 2}
pu = cells - {(0, 0)}; Lp = sorted(pu)
f4 = [(a_, b_) for i, a_ in enumerate(Lp) for b_ in Lp[i + 1:]
      if (min(a_[0], b_[0]), min(a_[1], b_[1])) not in pu]
V["2 EQUATIONS"] = sum([len(L9) != 1654, len(L10) != 2535, len(L11) != 13585,
                        len(L12) != 70905, len(L13) != 199130, round(100 * d9, 1) != 63.7,
                        sum(len(Aq[q]) * len(Bq[q]) for q in Aq) != 199130, len(f4) != 4,
                        tuple(ph[k] for k in (1, 2, 3)) != (3, 4, 5)])

# ---------------------------------------------------------------- the source
cur = re.search(r"(?:one|two) hundred and [a-z-]+", s).group(0)
sp  = {x for x in re.findall(r"(?:one|two) hundred and (?:[a-z]+(?:-[a-z]+)?)\b", s)}
V["3 CONSISTENCY"] = (
    len([x for x in sp if x not in (cur, "one hundred and two")
         and any(not inreg(m.start()) for m in re.finditer(re.escape(x), s))])
    + len([w for w in ["the one prediction", "The prediction of §18.6", "one hundred and eighty-nine"]
           if any(not inreg(m.start()) for m in re.finditer(re.escape(w), s))]))

heads = [(m.start(), m.group(1)) for m in re.finditer(r"^#{1,4} (.+)$", s, re.M)]
sect = lambda p: ([h for q, h in heads if q < p] or ["front"])[-1]
V["4 REDUNDANCY"] = sum(1 for u in ["7.07 bits", "Knaster", "PROJECTION", "realised closure"]
                        if len({sect(m.start()) for m in re.finditer(re.escape(u), s)}) > 4)

V["5 ARTEFACT"] = ("\ufffd" in txt) + ("**" in txt) + (len(re.findall(r"#{2,}", txt)) > 1)

lines = s.split("\n")
ci = next(i for i, l in enumerate(lines) if l.strip() == "Contents")
ce = next(i for i, l in enumerate(lines) if l.strip() == "## References")
norm = lambda x: re.sub(r"\s+", " ", x.lstrip("#").strip())
toc  = [norm(l) for l in lines[ci:ce + 1] if l.strip() and l.strip() != "Contents"]
body = [norm(l) for l in lines[:ci] + lines[ce + 1:] if re.match(r"^#{1,2} ", l)]
refs = set(re.findall(r"§(\d{1,2}\.\d{1,2}(?:\.\d)?)", s))
hd = (set(re.findall(r"^### (\d{1,2}\.\d{1,2}(?:\.\d)?)", s, re.M))
      | set(re.findall(r"^\s{0,2}(\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)\s+[A-ZΛ]", s, re.M)))
V["6 COHERENCE"] = (len([x for x in toc if x not in body]) + len([x for x in body if x not in toc])
    + len([r for r in refs if r not in hd and int(r.split(".")[0]) <= 25 and r != "21.9"]))

ref = s[s.rindex("# References"):]; bd = s[:s.rindex("# References")]
cited = {m.group(1) for m in re.finditer(
    r"\b([A-Z][a-zà-ÿ]{3,})\s*(?:&|and)?\s*(?:[A-Z][a-zà-ÿ]{3,})?[, ]+\(?(?:19|20)\d{2}", bd)}
STOP = {"Chapter","Appendix","Register","Figure","Part","Table","Section","Earliest","Leipzig","October"}
V["7 ATTRIBUTION"] = len([c for c in cited - STOP if c not in ref])

V["10 SCOPE"] = len([m for m in re.finditer(r"E\((?:Q|G|Appendix E|audits)\)\s*=\s*\d", s)
    if not re.search(r"fibr|unfibred|coordinat|resolved", s[max(0, m.start() - 280): m.start() + 280])
    and not inreg(m.start())])

hh = re.findall(r"^#{2,4} (\d{1,2}(?:\.\d{1,2})+)", s, re.M)
V["11 ANTECEDENT"] = len([h for h in hh if h.count(".") >= 2
                          and ".".join(h.split(".")[:-1]) not in hh])
V["12 MARKUP"] = sum(1 for p in re.split(r"\n\s*\n", s) if p.count("**") % 2)
V["13 AGREEMENT"] = sum(1 for rx in [r"\|Λ₁₃\|\s*=?\s*([\d,]+)", r"E\(G\)\s*=\s*(\d+)"]
                        if len({m.group(1) for m in re.finditer(rx, s)}) > 1)

blk = s[s.index("E.5 The closed index"): s.index("E.5 The closed index") + 2000]
tot = 0
for l in blk.split("\n"):
    m = re.match(r"^\s{2,}([a-z].*?)\s{3,}(\d+)(\s+each)?\s+0\s*$", l)
    if m: tot += int(m.group(2)) * (m.group(1).count("·") if m.group(3) else 1)
V["14 ARITHMETIC"] = 0 if tot in (32, 36) else 1

hds = [(m.start(), m.group(1), m.group(2))
       for m in re.finditer(r"^###\s*(21\.\d+(?:\.\d+)?)\s+(\S.{0,58})", reg, re.M)]
Wd = {"two":2,"three":3,"four":4,"six":6,"eight":8,"twelve":12,"thirty-three":33,"forty":40,"eighty-seven":87}
b15 = 0
for i_, (st, lab, ti) in enumerate(hds):
    en = hds[i_ + 1][0] if i_ + 1 < len(hds) else len(reg)
    nums = set()
    for m in re.finditer(r"^\s{0,3}(\d{2,3})(?:[–-](\d{2,3}))?\.\s", reg[st:en], re.M):
        a_ = int(m.group(1)); b_ = int(m.group(2)) if m.group(2) else a_
        nums |= set(range(a_, b_ + 1))
    pr = re.search(r"([\w-]+) printed here", ti)
    if nums and pr:
        w = pr.group(1).lower()
        if (len(nums) if w == "all" else Wd.get(w)) != len(nums): b15 += 1
V["15 ENUMERATION"] = b15

press = open("The Method 1.2 press.py").read()
V["16 FIDELITY"] = sum(1 for h in re.findall(r"'([^']{25,90})'", press)
    if "F(1)" in h and re.sub(r"<[^>]+>", "", h) not in re.sub(r"\s+", " ", s))

im = sum(1 for l in subprocess.run(["pdfimages", "-list", PDF], capture_output=True,
         text=True).stdout.splitlines()[2:] if l.split()[2] == "image")
V["17 MEASURE"] = 0 if im == 32 else 1
V["18 REPRODUCTION"] = sum(1 for k in ("473,800,776", "30,108") if k not in s)

key = lambda t: [int(v) for v in re.findall(r"\d+", t)]
SECL = re.compile(r"^ ([A-G]\.\d+(?:\.\d+)*) (\S[^\n]{0,70})$")
def secs(A):
    return [m.group(1) for line in A.split("\n") if (m := SECL.match(line))
            and not re.search(r"\s{3,}\S", m.group(2))
            and not m.group(2).endswith((".", ",")) and len(m.group(2).split()) <= 12]
b19 = 0
ents = [int(x) for x in re.findall(r"^\s{0,3}(\d{3})\.\s", reg, re.M)]
if ents != sorted(ents): b19 += 1
for x in "ABCDEFG":
    i = s.rindex(f"# Appendix {x}")
    nxt = {"A":"B","B":"C","C":"D","D":"E","E":"F","F":"G","G":None}[x]
    A = s[i:(s.rindex(f"# Appendix {nxt}") if nxt else s.rindex("# END MATTER"))]
    if secs(A) != sorted(secs(A), key=key): b19 += 1
for c in range(1, 26):
    sec = [m.group(1) for m in re.finditer(r"^### (" + str(c) + r"\.\d+(?:\.\d+)*)", s, re.M)]
    if sec != sorted(sec, key=key): b19 += 1
V["19 SEQUENCE"] = b19

import pdfplumber
pdf = pdfplumber.open(PDF)
start = next(i + 1 for i, pg in enumerate(pdf.pages[:20])
             if "Generated from the headings" in (pg.extract_text() or ""))
end = start
while "This book makes one claim" not in (pdf.pages[end].extract_text() or ""): end += 1
toct = re.sub(r"\s+", " ", subprocess.run(["pdftotext", "-f", str(start), "-l", str(end), PDF, "-"],
                                          capture_output=True, text=True).stdout)
src = [m.group(1).strip() for m in re.finditer(r"^#{1,4} (.+)$", s, re.M)]
for line in s.split("\n"):
    m = SECL.match(line)
    if m and not re.search(r"\s{3,}\S", m.group(2)) and not m.group(2).endswith((".", ",")) \
       and len(m.group(2).split()) <= 12:
        src.append(m.group(1) + " " + m.group(2))
inside = set(x.lstrip("#").strip() for x in lines[ci:ce + 1])
src = [x for x in src if x not in inside]
V["20 PROJECTION"] = (len([x for x in src if re.sub(r"\s+", " ", x) not in toct])
                      + (0 if len(re.findall(r"^ *Figure \d+\.\d+", s, re.M)) == im else 1))

# ---------------------------------------------------------------- report
print("=== THE TWENTY PRIME AUDITS ===")
for k in sorted(V, key=lambda z: int(z.split()[0])):
    print(f"  {k:18s} {'PASS' if V[k] == 0 else f'FAIL ({V[k]})'}")
fails = [k for k, v in V.items() if v]
print(f"\n{'ALL TWENTY PASS' if not fails else 'FAILURES: ' + str(fails)}")
sys.exit(len(fails))
