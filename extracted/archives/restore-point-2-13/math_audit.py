#!/usr/bin/env python3
"""math_audit.py -- the Mathematical Compendium, audited as an object and by contents.

Register 1224. The compendium is now an attribution map: 248 objects, each naming
where its mathematics comes from. Two questions follow that the twenty-two prime
audits do not ask.

    AS AN OBJECT   the compendium is itself an index. Its cells are objects and its
                   coordinates are family, grade, depth, source-era and check-length.
                   So R applies, and E(compendium) is a number.

    BY CONTENTS    every object carries a statement, a hypothesis, dependencies, a
                   source, a grade, a check and a name. Each field has a condition it
                   must satisfy, and no audit checked most of them.

Twelve checks, run in two blocks. A failure is reported with its members, not as a
count, because the point is to fix it and not to score it.
"""
import re, math
import importlib.util as iu
from itertools import product
from collections import Counter, defaultdict
from zeno import State, step

def load():
    sp = iu.spec_from_file_location("_mr", "mathreg.py"); mr = iu.module_from_spec(sp)
    try: sp.loader.exec_module(mr)
    except SystemExit: pass
    return mr.REG

def op_R(X, d):
    X = set(X)
    if not X: return set()
    vals = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -10**9), c[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i,j): env(i,j) for i in range(d) for j in range(d) if i != j}
    return {x for x in product(*vals)
            if all(x[i] <= phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i != j)}

YR = re.compile(r"\b(1[6-9]\d\d|20[0-2]\d)\b")
GRADE_ORDER = ["DEFINITIONAL", "CITED", "PROVED", "COMPUTED", "MEASURED",
               "ASSERTED", "OPEN"]

def run():
    R = load()
    dep = {k: [d for d in v["dep"] if d in R] for k, v in R.items()}
    memo = {}
    def depth(k):
        if k in memo: return memo[k]
        if not dep[k]: memo[k] = 0; return 0
        memo[k] = 1 + max(depth(d) for d in dep[k]); return memo[k]
    F = {}

    # ============================================================ AS AN OBJECT
    fams = sorted({k.split(".")[0] for k in R})
    def era(v):
        ys = [int(y) for y in YR.findall(" ".join(str(v.get(x) or "")
                                                  for x in ("src","check")))]
        return min(ys) if ys else 9999
    ERAS = [1700, 1800, 1900, 1930, 1950, 1970, 1990, 2010, 9999]
    def ebin(y):
        for i, b in enumerate(ERAS):
            if y <= b: return i
        return len(ERAS)
    # Register 1224. FAMILY is a NOMINAL coordinate — the families have no order, so
    # alphabetical position is not a rank and R's envelopes are meaningless on it. The
    # compendium is therefore NOT an index in the book's sense along that axis, and
    # E computed with it is a number about the alphabet and not about the object.
    # The ordinal coordinates are grade, depth and era; family is carried as a LABEL.
    cells = set()
    for k, v in R.items():
        cells.add((fams.index(k.split(".")[0]),
                   GRADE_ORDER.index(v["grade"]) if v["grade"] in GRADE_ORDER else 0,
                   min(depth(k), 9),
                   ebin(era(v))))
    Rc = op_R(cells, 4)
    ord_cells = {c[1:] for c in cells}            # grade, depth, era — all ordinal
    Ro = op_R(ord_cells, 3)
    F["object: E(compendium) computed"] = (len(cells), len(Rc), len(Rc)-len(cells),
                                           len(ord_cells), len(Ro), len(Ro)-len(ord_cells))

    # ============================================================ BY CONTENTS
    F["contents: every object has a statement"] = [k for k, v in R.items()
                                                   if not (v.get("stmt") or "").strip()]
    F["contents: every object has a hypothesis"] = [k for k, v in R.items()
                                                    if not (v.get("hyp") or "").strip()]
    F["contents: every object has a source"] = [k for k, v in R.items()
                                                if not (v.get("src") or "").strip()]
    F["contents: every object has a dated source"] = [
        k for k, v in R.items()
        if not YR.search(" ".join(str(v.get(x) or "") for x in ("src","check")))]
    F["contents: every object has a name"] = [k for k, v in R.items()
                                              if not (v.get("named") or "").strip()]
    F["contents: every object has a check"] = [k for k, v in R.items()
                                               if not (v.get("check") or "").strip()]
    F["contents: no dangling dependency"] = sorted(
        {d for v in R.values() for d in v["dep"] if d not in R})
    # acyclicity
    col = defaultdict(int); cyc = []
    def dfs(u, st):
        col[u] = 1; st.append(u)
        for w in dep[u]:
            if col[w] == 1: cyc.append(st[st.index(w):] + [w])
            elif col[w] == 0: dfs(w, st)
        st.pop(); col[u] = 2
    import sys; old = sys.getrecursionlimit(); sys.setrecursionlimit(50000)
    for k in sorted(R):
        if col[k] == 0: dfs(k, [])
    sys.setrecursionlimit(old)
    F["contents: the dependency graph is acyclic"] = [" -> ".join(c) for c in cyc]
    # a CITED object should carry a source older than the book
    F["contents: CITED objects name a year"] = [
        k for k, v in R.items() if v["grade"] == "CITED"
        and not YR.search(" ".join(str(v.get(x) or "") for x in ("src","check")))]
    # a PROVED object must not rest on an ASSERTED or OPEN one
    weak = {k for k, v in R.items() if v["grade"] in ("ASSERTED", "OPEN")}
    F["contents: no PROVED rests on ASSERTED or OPEN"] = [
        f"{k} <- {d}" for k in R if R[k]["grade"] == "PROVED"
        for d in dep[k] if d in weak]
    # the check must not merely restate the statement
    def sim(a, b):
        wa = set(re.findall(r"[a-z]{4,}", a.lower()))
        wb = set(re.findall(r"[a-z]{4,}", b.lower()))
        return len(wa & wb)/max(len(wa | wb), 1)
    F["contents: the check adds to the statement"] = [
        k for k, v in R.items()
        if (v.get("check") or "") and sim(v["stmt"], v["check"]) > 0.72]
    # a prior-art note must not claim the result AND cite it
    # A prior-art note must carry MEASURED CONTENT alongside the citation, so that a
    # reader can see what this work added. Measured content is a number, a count or an
    # explicit statement of what is inherited rather than proved. Register 1224: an
    # earlier version of this check demanded specific words and failed 191 objects that
    # state their measurement as figures.
    def has_measure(t):
        if re.search(r"\b(measure|measured|measurement|computed|this work|inherited|"
                     r"not proved here|is new|not new|not this work|is the computation|"
                     r"what is added|adds nothing|the measurement)\b",
                     t, re.I): return True
        # a count, a fraction, a ratio or an rms alongside the citation
        body = re.sub(r"\((?:1[6-9]\d\d|20[0-2]\d)\)|\b(?:1[6-9]\d\d|20[0-2]\d)\b", "", t)
        body = re.sub(r"\b(?:vol|no|pp?|ch|sec)\.?\s*[\dIVXL]+", "", body, flags=re.I)
        return bool(re.search(r"\d+\s*(?:of|/)\s*\d+|\d+\.\d{2,}|\d{2,}%|"
                              r"rms|R\^?2|sigma", body))
    # DEFINITIONAL and CITED objects are exempt: a definition has nothing to measure,
    # and a CITED object IS the prior art rather than a measurement against it.
    F["contents: prior art carries measured content"] = [
        k for k, v in R.items()
        if "PRIOR ART" in (v.get("check") or "")
        and v["grade"] not in ("DEFINITIONAL", "CITED")
        and not has_measure(v["check"])]
    return R, F, cells

with State("math_audit") as s:
    REG, F, CELLS = step(s, "audit the compendium as an object and by contents",
                         run, budget=900)

print("  THE MATHEMATICAL COMPENDIUM, AUDITED\n")
n, rn, e, no, rno, eo = F.pop("object: E(compendium) computed")
print("  AS AN OBJECT\n")
print("      FAMILY is nominal — the families have no order, so its alphabetical")
print("      position is not a rank. E computed with it is a number about the")
print("      alphabet, not about the compendium.\n")
print(f"      with family    |X| = {n:>4}   |ℛ(X)| = {rn:>5}   E = {e:>5}")
print(f"      ORDINAL only   |X| = {no:>4}   |ℛ(X)| = {rno:>5}   E = {eo:>5}"
      f"   {'CLOSED' if eo == 0 else ''}")
print("      (grade · dependency depth · source era — all three carry an order)\n")

print("  BY CONTENTS\n")
bad = 0
for k, v in F.items():
    ok = (len(v) == 0)
    bad += 0 if ok else 1
    print(f"      {k:<52}{'PASS' if ok else 'FAIL ' + str(len(v))}")
    if not ok:
        for x in v[:6]: print(f"          {x}")
        if len(v) > 6: print(f"          … {len(v)-6} more")
print()
print(f"  {len(F)-bad} of {len(F)} content checks pass")
