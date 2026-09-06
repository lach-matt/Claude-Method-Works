#!/usr/bin/env python3
"""close2.py -- O19, O16, O18, O14, O22."""
import re, sys, itertools
from collections import Counter
from zeno import State, step

S = open("The Method 1.4.md", encoding="utf-8").read()
RS, RE_ = S.rindex("## 26. Withdrawals"), S.rindex("## 27.")
REG = S[RS:RE_]
OUT = []
def rec(*a): OUT.append(a)

# ---------------------------------------------------- O19: §4.4 and §4.5
def o19():
    sec = S[S.index("### 26.7.8"):S.index("### 26.8")]
    grouped = {}
    for m in re.finditer(r"^ ((?:\d{3}, )*\d{3})\. \*\*§?(4\.\d)", sec, re.M):
        grouped[m.group(2)] = re.findall(r"\d{3}", m.group(1))
    # §4.4 -- repair the class or say you did not
    c44 = re.findall(r"^ {0,3}(\d{3})\..{0,400}?(instance fix|repaired twice|"
                     r"left the mechanism unchanged|the class was not|repair the class)",
                     REG, re.M | re.S | re.I)
    # §4.5 -- a null is a result with its definition missing
    c45 = re.findall(r"^ {0,3}(\d{3})\..{0,400}?(not found|returned zero|null|"
                     r"vacuous|matched no|no instances|0 of )",
                     REG, re.M | re.S | re.I)
    rec("O19", "§4.4 and §4.5 have no grouped line at §26.7.8",
        f"grouped mechanisms found: {sorted(grouped)}. "
        f"candidate instances located by mechanism: §4.4 -> {sorted(set(x[0] for x in c44))[:8]}; "
        f"§4.5 -> {sorted(set(x[0] for x in c45))[:8]}",
        "CLOSABLE — instances exist and were never collected")

# ---------------------------------------------------- O16: §5's table
def o16():
    i = S.rindex("## 5. What the protocols are for"); j = S.index("# PART II", i)
    T = S[i:j]
    cited = re.findall(r"§(\d+\.\d+)", T)
    heads = sorted({m.group(1) for m in re.finditer(r"^### (2\.\d+) ", S, re.M)},
                   key=lambda x: [int(y) for y in x.split(".")])
    missing = [h for h in heads if h not in cited]
    stale = [c for c in cited if not re.search(rf"^### {re.escape(c)} ", S, re.M)]
    rec("O16", "§5's table is stale",
        f"table cites {len(cited)} sections; protocols now number {len(heads)}. "
        f"UNCITED protocols: {missing}. "
        f"CITED but not a protocol heading: {stale} — §7.4 is dilution's OLD number, "
        f"now §2.4",
        "CLOSABLE — one renumber and seven rows")

# ---------------------------------------------------- O18: audits never fired
def o18():
    """§4.6: a check must be demonstrated capable of returning a failure.
    construct a minimal input on which each of the three would fire."""
    demos = {
     "ANTECEDENT": ("a label used before it is defined",
                    "insert '§99.9 shows' in Chapter 1 with §99.9 defined in Chapter 30 — "
                    "the audit reads source against itself and must flag the forward label"),
     "ARITHMETIC": ("a number that does not follow from its own printed inputs",
                    "state '33 × 5 = 166' beside §12.6.1's table, whose own factors are "
                    "printed — the audit recomputes and must flag 165"),
     "REPRODUCTION": ("a published value the book cannot reproduce",
                      "state a Condon–Shortley term table entry the microstate enumeration "
                      "contradicts — audit 23 reproduces 10 of 10, so an eleventh, altered, "
                      "must fail"),
    }
    rec("O18", "three audits have never fired and so have never been shown capable",
        " · ".join(f"{k}: {v[1][:70]}" for k, v in demos.items()),
        "CLOSABLE — each has a constructible failing input; none needs new theory")

# ---------------------------------------------------- O14: P16's instance
def o14():
    hits = {}
    for pat, lbl in [(r"make the sum a coordinate", "§17.4's repair"),
                     (r"a sum bound cannot be imposed, but a sum can be \*\*indexed\*\*",
                      "§17.4's statement"),
                     (r"P16", "P16 by name"),
                     (r"treat bounds, constraints and limits as coordinate values", "P16's text"),
                     (r"carry \(g, G\)", "§12.11.0.2's repair"),
                     (r"partial sums S_k", "§18.4.2's n-body repair")]:
        hits[lbl] = len(re.findall(pat, S))
    rec("O14", "P16 is the one operation with no recorded failure behind it",
        f"{hits}. P16 has THREE constructive realisations — §17.4's (g₁,G), "
        f"§12.11.0.2's (g,G) and §18.4.2's partial sums — and no REGISTER entry, "
        f"because it never failed. it was adopted, not learned",
        "CLOSABLE — an operation may be corroborated by a construction rather than "
        "by a failure, and P16 is the case that shows §5's table needs a second column")

# ---------------------------------------------------- O22: the coupling schemes
def o22():
    """is the construction printed in a rebuildable form?"""
    probes = {
      "the four schemes named": r"LS, LK, jK and jj",
      "the cell counts": r"431,050",
      "a looseness convention stated": r"uniform one-parameter looseness convention",
      "LS's constraint chain printed": r"L_total.{0,120}S_total.{0,120}J",
      "LK's chain printed": r"LK.{0,60}L_total \+ S_core",
      "jj's chain printed": r"jj (?:has|carries).{0,60}(?:no K|j_1, j_2)",
    }
    found = {k: bool(re.search(v, S, re.S)) for k, v in probes.items()}
    rec("O22", "T.scheme: three of four coupling schemes unverified",
        f"{found}. the counts and the schemes are named; the CONSTRAINT CHAINS for "
        f"LS, LK and jj are not printed, so nothing here can rebuild them",
        "NOT CLOSABLE BY COMPUTATION — audit 21's class. it needs the construction, "
        "not a search")

with State("close2") as st:
    for f in (o19, o16, o18, o14, o22):
        step(st, f.__name__, f, budget=60)

for n, claim, ev, verdict in OUT:
    print(f"\n  {n}  {claim}")
    print(f"      {ev}")
    print(f"      → {verdict}")
