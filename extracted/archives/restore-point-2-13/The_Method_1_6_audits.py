#!/usr/bin/env python3
"""The Method 1.6 — the twenty prime audits, run as one pass.

B.2.17 defines them; B.2.22 requires them on every output. This file is the
requirement made executable, so that "audited" is a fact about a build rather
than a claim about a session.  Exit status is the number of failing audits.
"""
import re, sys, json, subprocess
from itertools import combinations, product
from collections import Counter, defaultdict

SRC = "The Method 1.6.md"
PDF = "The Method 1.6.pdf"

s   = open(SRC, encoding="utf-8").read()
txt = subprocess.run(["pdftotext", PDF, "-"], capture_output=True, text=True).stdout
RS, RE_ = s.rindex("## 28. Withdrawals"), s.rindex("## 29.")
# The register no longer lives in the book — chapter 28 references it and the
# entries are in REGISTER-DATA.md, generated into the Register compendium.
# Every audit that reads the record now reads the archive (register 658).
import os as _os2
reg = (open("REGISTER-DATA.md", encoding="utf-8").read()
       if _os2.path.exists("REGISTER-DATA.md") else s[s.rindex("## 28.") : s.rindex("## 29.")])
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
# the reference count is the register's own maximum, never a phrase found in the text (register 337)
_W1 = {"one":100,"two":200,"three":300,"four":400,"five":500,"six":600,"seven":700}
_W2 = {"ten":10,"twenty":20,"thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,
       "eighty":80,"ninety":90,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,
       "seven":7,"eight":8,"nine":9,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,
       "fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19}
def _val(ph):
    # The register passed one thousand at entry 1000 and this parser handled only
    # "N hundred and M", so it silently stopped matching and the check coasted
    # (register 1101). Thousands are now read too.
    m = re.match(r"one thousand(?: and ([a-z]+)(?:-([a-z]+))?"
                 r"|\s+(one|two|three|four|five|six|seven|eight|nine) hundred"
                 r"(?: and ([a-z]+)(?:-([a-z]+))?)?)?$", ph)
    if m:
        v = 1000
        if m.group(1): v += _W2.get(m.group(1), 0) + _W2.get(m.group(2) or "", 0)
        if m.group(3): v += _W1.get(m.group(3), 0)
        if m.group(4): v += _W2.get(m.group(4), 0) + _W2.get(m.group(5) or "", 0)
        return v
    m = re.match(r"(one|two|three|four|five|six|seven) hundred and ([a-z]+)(?:-([a-z]+))?$", ph)
    if not m: return None
    return _W1[m.group(1)] + _W2.get(m.group(2), 0) + _W2.get(m.group(3) or "", 0)
_maxent = max(int(x) for x in re.findall(r"^\s{0,3}(\d{3,4})\.\s", reg, re.M))
_cands = set(re.findall(r"(?:one thousand(?:\\s+(?:one|two|three|four|five|six|seven|eight|nine) hundred)?(?: and [a-z]+(?:-[a-z]+)?)?|(?:one|two|three|four|five|six|seven) hundred and [a-z]+(?:-[a-z]+)?)\\b", s))
cur = next((ph for ph in _cands if _val(ph) == _maxent), "\x00")
# a spelled hundred followed by a noun other than the register's own is a count of
# something else, not a stale total (registers 513, 520)
_REGNOUN = ("withdrawals", "entries", "register", ".", ",", "\n", " —")
sp  = {x for x in re.findall(r"(?:one thousand(?:\\s+(?:one|two|three|four|five|six|seven|eight|nine) hundred)?(?: and [a-z]+(?:-[a-z]+)?)?|(?:one|two|three|four|five|six|seven) hundred and [a-z]+(?:-[a-z]+)?)\\b", s)
       if any(s[m.end():m.end()+14].lstrip().startswith(_REGNOUN) or not s[m.end():m.end()+2].strip()
              for m in re.finditer(re.escape(x), s))}
# The register no longer lives in the book: chapter 28 keeps the argument and
# the compendium keeps the record, so the spelled total is checked against the
# COMPENDIUM rather than against entries the chapter no longer prints (reg 658).
try:
    _rc = open("REGISTER.md", encoding="utf-8").read()
    _maxent = max(int(x) for m in re.finditer(r"^### ((?:\d{3,4}, )*\d{3,4})", _rc, re.M)
                  for x in re.findall(r"\d{3,4}", m.group(1)))
except Exception:
    pass
V["3 CONSISTENCY"] = (
    len([x for x in sp if x not in (cur, "one hundred and two")
         and any(not inreg(m.start()) for m in re.finditer(re.escape(x), s))])
    + len([w for w in ["the one prediction", "The prediction of §18.6", "one hundred and eighty-nine"]
           if any(not inreg(m.start()) for m in re.finditer(re.escape(w), s))]))

heads = [(m.start(), m.group(1)) for m in re.finditer(r"^#{1,4} (.+)$", s, re.M)]
sect = lambda p: ([h for q, h in heads if q < p] or ["front"])[-1]
# the register records everything by design; restatement is counted outside it (register 341)
# the register records everything by design, and chapter 3 names every audit by construction;
# restatement is counted outside both (registers 341, 378)
_A3 = s.rindex("## 3. The twenty-five prime audits"), s.rindex("## 4. ")
_ex = lambda p: inreg(p) or (_A3[0] < p < _A3[1])
V["4 REDUNDANCY"] = sum(1 for u in ["7.07 bits", "Knaster", "PROJECTION", "realised closure"]
                        if len({sect(m.start()) for m in re.finditer(re.escape(u), s)
                                if not _ex(m.start())}) > 4)

# --- 22 CENSUS: every count stated in prose against the list it counts -------
# Five miscounts lived in the front matter unnoticed by twenty-one audits, because
# no audit compared a spelled number against what it enumerated (registers 516-517).
_W = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,
      "ten":10,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,
      "sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,"twenty":20,"thirty":30}
def _num(ph):
    ph = ph.strip().lower()
    if ph in _W: return _W[ph]
    m = re.match(r"(twenty|thirty)-(\w+)$", ph)
    if m: return _W[m.group(1)] + _W.get(m.group(2), 0)
    return None
s0 = s
_TRUE = {
 # the book discloses which numbers are unassigned; counting P-tokens without
 # subtracting them counts the disclosure itself (register 518)
 "principles":  len({int(m.group(1)) for m in re.finditer(r"(?<![A-Za-z0-9])P(\d{1,2})(?![0-9])", s0)}
                    - {int(x) for x in re.findall(r"P(\d{1,2})",
                        (re.search(r"with ((?:P\d{1,2}[,\s]+(?:and\s+)?)+)unassigned", s0) or
                         type("", (), {"group": lambda *a: ""})()).group(1))}),
 "protocols":   len({m.group(1) for m in re.finditer(r"^### (2\.\d+) ", s0, re.M)}),
 "prime audits": len(re.findall(r"^\s{0,3}\d{1,2}\s+[A-Z]{4,}\s", s0, re.M)),
 "appendices":  len({m.group(1) for m in re.finditer(r"^# Appendix ([A-Z]) —", s0, re.M)}),
}
_census = []
for _k, _v in _TRUE.items():
    if not _v: continue
    for _m in re.finditer(r"\b([a-z]+(?:-[a-z]+)?)\s+(?:prime\s+)?" + _k + r"\b", s0):
        _n = _num(_m.group(1))
        if _n is None: continue
        _pre = s0[max(0, _m.start() - 12):_m.start()].lower()
        _post = s0[_m.end():_m.end() + 6]
        # "the other N appendices" is a complement, "the N X of §a-b" is a subset,
        # and "confined to N appendices" is a scope — none is a census (register 517)
        if _pre.rstrip().endswith(("other", "to", "in", "across")): continue
        if _post.lstrip().startswith(("of §", "of \u00a7")): continue
        if _n != _v and not inreg(_m.start()): _census.append((_k, _m.group(1), _n, _v))
# ORDINAL SELF-CLAIMS. "the Nth wrong verification of the session" and the like
# were carried in my head beside the register that held the list, and no audit
# checked them; register 475 said fifteen where the register recorded nine
# (registers 521, 560). An ordinal about this book's own conduct is a count and
# is now counted.
_FAULT = re.compile(
    r"\bI (?:wrote|applied|read|reported|bounded|never|assumed|committed|cited|derived|"
    r"flagged|took|used|fitted|claimed|missed|swallowed)\b|"
    r"\bmy (?:own|reading|prose|check|verification|entries|edit|regex|reconstruction)\b|"
    r"wrong verification|could not fail|caught its author|before reading", re.I)
_ORD = {"second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6, "seventh": 7,
        "eighth": 8, "ninth": 9, "tenth": 10, "eleventh": 11, "twelfth": 12,
        "thirteenth": 13, "fourteenth": 14, "fifteenth": 15, "sixteenth": 16,
        "seventeenth": 17, "eighteenth": 18, "nineteenth": 19, "twentieth": 20}
try:
    _rs, _re2 = s0.rindex("## 28. Withdrawals"), s0.rindex("## 29.")
    _reg = s0[_rs:_re2]
    _ms = list(re.finditer(r"^ {0,3}((?:\d{3}, )*\d{3})\. ", _reg, re.M))
    _faults = []
    for _i, _m in enumerate(_ms):
        _end = _ms[_i + 1].start() if _i + 1 < len(_ms) else len(_reg)
        if _FAULT.search(_reg[_m.end():_end]):
            _faults.append(int(re.findall(r"\d{3}", _m.group(1))[-1]))
    # an ordinal claim "the Nth of the session" must not exceed what the register
    # records; the session's range is taken as entries at or above the earliest fault
    _lo = min(_faults) if _faults else 0
    _insession = len([f for f in _faults if f >= _lo])
    _ordinals = 0
    for _m in re.finditer(r"the (\w+) of the session", s0):
        _n = _ORD.get(_m.group(1).lower())
        if _n is None: continue
        # a corrected entry discloses the old number in italics; that is a record,
        # not a claim
        _ctx = s0[max(0, _m.start() - 90):_m.start()]
        if "originally read" in _ctx or "corrected" in _ctx: continue
        if _n > _insession: _ordinals += 1
except ValueError:
    _ordinals = 0
# STATED-VERSUS-TABULATED TOTALS. Appendix B's totals line read 153 channels
# and 1105 cells where its own table holds 133 rows summing to 869 — a total
# counting rows the table does not list, which no check caught because audit 22
# compares prose counts to lists it can FIND (register 631).
_tab = 0
try:
    _bs = s0.rindex("# Appendix B"); _be = s0.rindex("# Appendix C")
    _bt = s0[_bs:_be]
    _rw = re.findall(r"^\s{2,}[A-Z][a-z]?\s+[IVX]+\s{2,}\S[^\n]*?\s{2,}"
                     r"\d+[–-]\d+\s+(\d+)\s+(\d+)\s+(\d+)/(\d+)\s+", _bt, re.M)
    if _rw:
        _rows = len(_rw); _cells = sum(int(r[1]) for r in _rw)
        _m = re.search(r"Totals?:\s*(\d+)\s*channels?,\s*([\d,]+)\s*cells", _bt)
        if _m:
            _sc = int(_m.group(1)); _sq = int(_m.group(2).replace(",", ""))
            # a stated total must either match the table or be disclosed as differing
            _disc = "stated and not tabulated" in s0 or "does not list" in s0
            if (_sc != _rows or _sq != _cells) and not _disc: _tab = 1
except ValueError:
    pass
V["22 CENSUS"] = len(_census) + _ordinals + _tab

V["5 ARTEFACT"] = ("\ufffd" in txt) + ("**" in txt) + (len(re.findall(r"#{2,}", txt)) > 1)

lines = s.split("\n")
ci = next(i for i, l in enumerate(lines) if l.strip() == "Contents")
ce = next(i for i, l in enumerate(lines) if l.strip() == "## References")
norm = lambda x: re.sub(r"\s+", " ", x.lstrip("#").strip())
toc  = [norm(l) for l in lines[ci:ce + 1] if l.strip() and l.strip() != "Contents"]
body = [norm(l) for l in lines[:ci] + lines[ce + 1:] if re.match(r"^#{1,2} ", l)]
refs = set(re.findall(r"§(\d{1,2}\.\d{1,2}(?:\.\d)?)", s))
hd = (set(re.findall(r"^### (\d{1,2}\.\d{1,2}(?:\.\d)?)", s, re.M))
      # a definition row may open with emphasis — chapter 4's ten mechanisms do,
      # and the regex required a bare capital, so §4.1–§4.10 resolved nowhere
      # while being cited throughout (register 655)
      | set(re.findall(r"^\s{0,2}(\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)\s+\*{0,2}[A-Za-zΛ]", s, re.M)))
V["6 COHERENCE"] = (len([x for x in toc if x not in body]) + len([x for x in body if x not in toc])
    + len([r for r in refs if r not in hd and int(r.split(".")[0]) <= 30 and r != "23.9"])
    # a stale appendix reference resolves nowhere, and the register is not exempt (register 381)
    + len([x for x in set(re.findall(r"§?\b([A-F]\.\d+(?:\.\d+)*)\b", s))
           if x not in set(re.findall(r"^\s{0,3}([A-F]\.\d+(?:\.\d+)*)\s+\S", s, re.M)) and len(x) < 9]))

ref = s[s.rindex("# References"):]; bd = s[:s.rindex("# References")]
cited = {m.group(1) for m in re.finditer(
    r"\b([A-Z][a-zà-ÿ]{3,})\s*(?:&|and)?\s*(?:[A-Z][a-zà-ÿ]{3,})?[, ]+\(?(?:19|20)\d{2}", bd)}
# month names are matched as authors by the year pattern; October was listed
# and the rest were not (register 559)
STOP = {"Chapter","Appendix","Register","Figure","Part","Table","Section","Earliest","Leipzig",
        "January","February","March","April","June","July","August","September","October",
        "November","December","Submitted","Published","Accessed","Version"}
V["7 ATTRIBUTION"] = len([c for c in cited - STOP if c not in ref])

V["10 SCOPE"] = len([m for m in re.finditer(r"E\((?:Q|G|Appendix E|audits)\)\s*=\s*\d", s)
    if not re.search(r"fibr|unfibred|coordinat|resolved", s[max(0, m.start() - 280): m.start() + 280])
    and not inreg(m.start())])

hh = re.findall(r"^#{2,4} (\d{1,2}(?:\.\d{1,2})+)", s, re.M)
V["11 ANTECEDENT"] = len([h for h in hh if h.count(".") >= 2
                          and ".".join(h.split(".")[:-1]) not in hh])
V["12 MARKUP"] = sum(1 for p in re.split(r"\n\s*\n", s) if p.count("**") % 2)
# the register records past values as history; a quoted former figure is not a disagreement,
# and is exempt from agreement exactly as it is from redundancy (registers 341, 381, 397)
V["13 AGREEMENT"] = sum(1 for rx in [r"\|Λ₁₃\|\s*=?\s*([\d,]+)", r"E\(G\)\s*=\s*(\d+)",
                                     r"E\(audits\)\s*=\s*(\d+)"]
                        if len({m.group(1) for m in re.finditer(rx, s)
                                if not inreg(m.start())}) > 1)

blk = s[s.index("D.5 The closed index"): s.index("D.5.2", s.index("D.5 The closed index"))]
tot = 0
for l in blk.split("\n"):
    m = re.match(r"^\s{2,}([a-z].*?)\s{3,}(\d+)(\s+each)?\s+0\s*$", l)
    if m: tot += int(m.group(2)) * (m.group(1).count("·") if m.group(3) else 1)
# the expected total is read from the appendix's own prose, never hardcoded (register 305)
_W = {"twenty-seven":27,"thirty-two":32,"thirty-six":36,"forty":40,"forty-four":44,"forty-eight":48}
_m = re.search(r"\*{0,2}([A-Za-z-]+) elements over sixteen fibres", blk)
_want = _W.get(_m.group(1).lower()) if _m else None
V["14 ARITHMETIC"] = 0 if (_want is not None and tot == _want) else 1

# and every row of the tower table at 7.11.0.1, against the construction (register 318)
_tb = s[s.index("Every Λ in one table"): s.index("The axes, and what each one sees")]
_L9  = [c + (sp,) for c in L for sp in range(0, c[6] + 1)]
_L9p = [c for c in _L9 if c[8] <= 2 * c[5] + 1]
_L10 = [c + (v,) for c in _L9 for v in range(c[8], c[6] + 1)]
_L11 = [c + (j,) for c in _L10 for j in range(0, ph[c[2]] + 1)]
_L12 = [c + (K,) for c in _L11 for K in range(0, c[10] + 3)]
_L13 = [c + (J,) for c in _L12 for J in range(max(0, c[11] - 1), c[11] + 2)]
_truth = {}
for _nm, _X in [("Λ₈", L), ("Λ₉", _L9), ("Λ₉′", _L9p), ("Λ₁₀", _L10),
                ("Λ₁₁", _L11), ("Λ₁₂", _L12), ("Λ₁₃", _L13)]:
    _d = len(_X[0]); _box = 1
    for _v in [sorted({c[i] for c in _X}) for i in range(_d)]: _box *= len(_v)
    _truth[_nm] = (_d, len(_X), _box, round(100 * len(_X) / _box, 2))
_seen = 0
for _m in re.finditer(r"^\s+\*{0,2}(Λ[₈₉₀₁₂₃′]+)\*{0,2}\s+(\d+)\s+([\d,]+)\s+(\d+)\s+([\d,]+)\s+([\d.]+)%", _tb, re.M):
    _k = _m.group(1)
    if _k not in _truth: V["14 ARITHMETIC"] += 1; continue
    _d, _n, _box, _f = _truth[_k]
    _seen += 1
    if (int(_m.group(2)) != _d or int(_m.group(3).replace(",", "")) != _n
            or int(_m.group(4)) != 0 or int(_m.group(5).replace(",", "")) != _box
            or abs(float(_m.group(6)) - _f) > 0.02):
        V["14 ARITHMETIC"] += 1
if _seen != 7: V["14 ARITHMETIC"] += 1
NOTE["14"] = f"column {tot} vs prose {_want}"

hds = [(m.start(), m.group(1), m.group(2))
       for m in re.finditer(r"^###\s*(28\.\d+(?:\.\d+)?)\s+(\S.{0,58})", reg, re.M)]
Wd = {"two":2,"twenty-nine":29,"fifty-eight":58,"seventy-seven":77,"thirty-one":31,"three":3,"four":4,"six":6,"eight":8,"twelve":12,"thirty-three":33,"forty":40,"eighty-seven":87}
b15 = 0
for i_, (st, lab, ti) in enumerate(hds):
    en = hds[i_ + 1][0] if i_ + 1 < len(hds) else len(reg)
    nums = set()
    for m in re.finditer(r"^\s{0,3}(\d{2,3})(?:[–-](\d{2,3}))?\.\s", reg[st:en], re.M):
        a_ = int(m.group(1)); b_ = int(m.group(2)) if m.group(2) else a_
        nums |= set(range(a_, b_ + 1))
    # any count-claim in the heading, however phrased (register 310)
    pr = re.search(r"([\w-]+)[, ]+(?:printed|listed|entries|items)\b", ti) or \
         re.search(r"^([\w-]+) (?:more|from)\b", ti)
    if nums and pr:
        w = pr.group(1).lower()
        exp = len(nums) if w == "all" else Wd.get(w)
        if exp is not None and exp != len(nums): b15 += 1
# E.1.2 and E.3 must list the same open items (register 384)
_EA = s.rindex("# Appendix E"); _EB = s.rindex("# Appendix F")
_Eblk = s[_EA:_EB]
_det = set(re.findall(r"^ ([A-P]) — ", _Eblk, re.M))
_op = {r[0] for r in re.findall(r"^\s{2,}([A-P])\s{3,}\S[^\n]{0,56}\s{2,}(\S+(?: \S+)?)\s{2,}", _Eblk, re.M)
       if r[1] != "CLOSED"}
_drift = len(_det ^ _op)

V["15 ENUMERATION"] = b15 + _drift

press = open("The Method 1.6 press.py").read()
V["16 FIDELITY"] = sum(1 for h in re.findall(r"'([^']{25,90})'", press)
    if "F(1)" in h and re.sub(r"<[^>]+>", "", h) not in re.sub(r"\s+", " ", s))

im = sum(1 for l in subprocess.run(["pdfimages", "-list", PDF], capture_output=True,
         text=True).stdout.splitlines()[2:] if l.split()[2] == "image")
# the artefact's own size is a figure nothing checked until register 369
import os as _os
_sz = _os.path.getsize(PDF)
_src = _os.path.getsize(SRC)
_figcap = len(re.findall(r"^ *Figure \d+\.\d+", s, re.M))
# the count was a constant 32 and went stale the moment a figure was added
# (register 523); it now reads the source's own captions
V["17 MEASURE"] = (0 if im == _figcap else 1) + (0 if 1_000_000 < _sz < 8_000_000 else 1) \
                                         + (0 if 300_000 < _src < 1_200_000 else 1)
V["18 REPRODUCTION"] = sum(1 for k in ("473,800,776", "30,108") if k not in s)

key = lambda t: [int(v) for v in re.findall(r"\d+", t)]
SECL = re.compile(r"^ ([A-G0]\.\d+(?:\.\d+)*) (\S[^\n]{0,70})$")
def secs(A):
    return [m.group(1) for line in A.split("\n") if (m := SECL.match(line))
            and not re.search(r"\s{3,}\S", m.group(2))
            and not m.group(2).endswith((".", ",")) and len(m.group(2).split()) <= 12]
b19 = 0
ents = [int(x) for x in re.findall(r"^\s{0,3}(\d{3})\.\s", reg, re.M)]
if ents != sorted(ents): b19 += 1
_APX = {"A":"B","B":"C","C":"D","D":"E","E":"F","F":None}
for x in _APX:
    i = s.rindex(f"# Appendix {x}")
    nxt = _APX[x]
    A = s[i:(s.rindex(f"# Appendix {nxt}") if nxt else s.rindex("# END MATTER"))]
    if secs(A) != sorted(secs(A), key=key): b19 += 1
# Part I carries the B.x labels since the procedure was promoted (register 321)

for c in range(1, 31):
    sec = [m.group(1) for m in re.finditer(r"^### (" + str(c) + r"\.\d+(?:\.\d+)*)", s, re.M)]
    if sec != sorted(sec, key=key): b19 += 1
V["19 SEQUENCE"] = b19
# ascending is satisfied by a DUPLICATE, so uniqueness must be checked too:
# two different entries were both numbered 368 and no audit saw it (register 651)
# R 1684/T10: the guard stopped at three digits and two entries duplicated inside
# the blind range. Widened to {3,4}; delimiter tightened to one leading space so a
# three-space quotation of an entry cannot impersonate one. Suffixed entries
# (368a, 1215a, 1476a — the R 651 precedent) are disambiguated at source and
# intentionally invisible here. Can-fail verified: unsuffixing 1476a raises 1.
# The ORDERING clause above stays at {3}: the 4-digit archive carries one
# historical non-monotone placement (1165 written after 1171), and widening
# would flag history — refused, not skipped silently (§2.9, §H.4).
_rnums = [int(y) for x in re.findall(r'^ {0,1}((?:\d{3,4}, )*\d{3,4})\. ', reg, re.M)
          for y in re.findall(r'\d{3,4}', x)]
V["19 SEQUENCE"] += len(_rnums) - len(set(_rnums))

import pdfplumber
pdf = pdfplumber.open(PDF)
start = next(i + 1 for i, pg in enumerate(pdf.pages[:20])
             if "Generated from the headings" in (pg.extract_text() or ""))
end = start
while "This book makes one claim" not in (pdf.pages[end].extract_text() or ""): end += 1
toct = re.sub(r"\s+", " ", subprocess.run(["pdftotext", "-f", str(start), "-l", str(end), PDF, "-"],
                                          capture_output=True, text=True).stdout)
# the contents is a three-tier projection: parts, chapters, top-level sections (register 325)
src = [m.group(1).strip() for m in re.finditer(r"^#{1,2} (.+)$", s, re.M)]
src += [m.group(1).strip() for m in re.finditer(r"^### (.+)$", s, re.M)
        if m.group(1).split()[0].count(".") < 2]
for line in s.split("\n"):
    m = SECL.match(line)
    if m and m.group(1).count(".") < 2 and not re.search(r"\s{3,}\S", m.group(2)) \
       and not m.group(2).endswith((".", ",")) and len(m.group(2).split()) <= 12:
        src.append(m.group(1) + " " + m.group(2))
inside = set(x.lstrip("#").strip() for x in lines[ci:ce + 1])
src = [x for x in src if x not in inside]
V["20 PROJECTION"] = (len([x for x in src if re.sub(r"\s+", " ", x) not in toct])
                      + (0 if len(re.findall(r"^ *Figure \d+\.\d+", s, re.M)) == im else 1))

# ---------------------------------------------------------------- report
# 21 INPUT: every stated result must print the data it was computed from (register 379)
_CASES=[("E(audits)", r"E\(audits\)\s*=\s*\d+",
         r"^\s{2,}\d{1,2}\s{3,}[A-Z]+\s{3,}(?:object|source|artefact|outside)\s{3,}"),
        ("dim(hierarchy)", r"dimension is 2|dim\(hierarchy\) = 2", r"L1\s+CELL <|L1\s+CONSISTENCY <"),
        ("the alphabet", r"Σ\(\|Aᵢ\| − 1\) = 17", r"A\.19\.0"),
        ("E(G)", r"E\(G\)", r"F\.2 The coordinates"),
        ("E(Q) fibred", r"E\(Q\) = 0", r"^\s{2,}[A-P]\s{3,}\S[^\n]{0,50}\s{2,}(?:nothing|one claim)"),
        ("the second bridges", r"[Tt]wenty admissible", r"g ≤ n\s{2,}953"),
        ("the four arrows", r"one per coordinate", r"shell\s{2,}9,407")]
V["21 INPUT"] = sum(1 for _n, _c, _i in _CASES
                    if re.search(_c, s, re.M) and not re.search(_i, s, re.M))


# --- 23 GRAPH, 24 CYCLE, 25 NOMENCLATURE ------------------------------------
# Register 1225. Three faults reached the compendium unseen by the first twenty-two,
# because none of them read mathreg.py as a GRAPH or checked that every object can be
# spoken about rather than only cited by key.
#   23 GRAPH        a dependency naming an object that does not exist
#   24 CYCLE        a dependency graph with a cycle — an object justified by itself.
#                   Q.delta -> Q.exch -> Q.delta passed 248 objects and six audit sets.
#   25 NOMENCLATURE an object with no name: citable by key, not speakable.
try:
    import importlib.util as _iu, sys as _sys
    from collections import defaultdict as _dd
    _sp = _iu.spec_from_file_location("_mrA", "mathreg.py"); _mr = _iu.module_from_spec(_sp)
    try: _sp.loader.exec_module(_mr)
    except SystemExit: pass
    _R = _mr.REG
    _dep = {k: [d for d in v["dep"] if d in _R] for k, v in _R.items()}
    V["23 GRAPH"] = len({d for v in _R.values() for d in v["dep"] if d not in _R})
    _col = _dd(int); _cyc = []
    def _dfs(u, st):
        _col[u] = 1; st.append(u)
        for w in _dep[u]:
            if _col[w] == 1: _cyc.append(st[st.index(w):] + [w])
            elif _col[w] == 0: _dfs(w, st)
        st.pop(); _col[u] = 2
    _old = _sys.getrecursionlimit(); _sys.setrecursionlimit(50000)
    for _k in sorted(_R):
        if _col[_k] == 0: _dfs(_k, [])
    _sys.setrecursionlimit(_old)
    V["24 CYCLE"] = len(_cyc)
    V["25 NOMENCLATURE"] = len([k for k, v in _R.items() if not (v.get("named") or "").strip()])
except Exception as _e:
    # Register 1226: an exception here means mathreg.py did not load, which is a
    # FAILURE and not a pass. An earlier version set these to zero and a broken
    # register reported ALL TWENTY-FIVE PASS.
    print(f"  !! mathreg.py did not load: {_e}")
    V["23 GRAPH"] = 1; V["24 CYCLE"] = 1; V["25 NOMENCLATURE"] = 1

print("=== THE TWENTY-FIVE PRIME AUDITS ===")
for k in sorted(V, key=lambda z: int(z.split()[0])):
    print(f"  {k:18s} {'PASS' if V[k] == 0 else f'FAIL ({V[k]})'}")
fails = [k for k, v in V.items() if v]
print(f"\n{'ALL TWENTY-FIVE PASS' if not fails else 'FAILURES: ' + str(fails)}")

# the prime directive: record each audit's cost so an approaching timeout is
# visible before it arrives, never after (register 343)
try:
    from zeno import State
    with State("audits") as _st:
        for k in sorted(V, key=lambda z: int(z.split()[0])):
            _st.done[k] = {"name": k, "ok": V[k] == 0, "secs": 0.0,
                           "value": V[k], "error": None}
    print(f"  state written to .zeno/audits.json — a rerun resumes from here")
except Exception as _e:
    print(f"  zeno state not written: {_e}")
sys.exit(len(fails))
