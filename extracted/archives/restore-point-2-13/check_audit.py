#!/usr/bin/env python3
"""check_audit.py -- which checks in the mathematics register could have failed?

Register 849. Today found the same fault five times, all in the Spectra Compendium:
J-pairs that cannot differ (775) · two-member channels that cannot detect perturbation
(727) · a bracket column set equal to its own denominator (782) · a bracket test a
Rydberg series satisfies by definition (797) · and duplicate rows compared against
themselves (845). Register 784 named the pattern: a device that admits inputs
incapable of failing it reports a pass rate exceeding its own discriminating power.

The mathematics register holds 213 objects and 195 carry a check. This asks of each
one: could it have failed?

Four signatures, in order of how badly they hide:

    SELF-NAMED     the check field repeats the object's own key. It records that a
                   script exists, not what the script found.
    RESTATEMENT    the check repeats the statement in other words, so passing it is
                   passing the definition.
    NO DENOMINATOR a count with no total. "0 failures" without "of N" cannot be
                   distinguished from "0 tested".
    UNFALSIFIABLE  a check whose stated outcome is the only outcome the construction
                   permits.

None of these means the object is wrong. It means the check does not support it, and
the compendium should not read as though it does.
"""
import re, importlib.util as iu
from collections import Counter, defaultdict
from zeno import State, step

def load():
    sp = iu.spec_from_file_location("_m", "mathreg.py"); m = iu.module_from_spec(sp)
    try: sp.loader.exec_module(m)
    except SystemExit: pass
    return m.REG

def classify(REG):
    out = defaultdict(list)
    for k, v in REG.items():
        c = v.get("check")
        if not c:
            out["NO CHECK"].append((k, v["grade"], "")); continue
        c = str(c).strip()
        stmt = str(v.get("stmt") or "")
        # 1 — the check is the object's own key, or a bare script name
        if c == k or c.replace(".py", "") == k or re.fullmatch(r"[\w./-]+\.py", c):
            out["SELF-NAMED"].append((k, v["grade"], c)); continue
        # 2 — a count with no denominator
        has_num = re.search(r"\d", c)
        has_den = re.search(r"\bof\b|/|out of|per|%", c)
        if has_num and not has_den and re.search(r"\b0\s+(failures?|errors?|fails?)\b", c):
            out["NO DENOMINATOR"].append((k, v["grade"], c)); continue
        # 3 — the check largely repeats the statement
        cw = set(re.findall(r"[a-zA-Z]{4,}", c.lower()))
        sw = set(re.findall(r"[a-zA-Z]{4,}", stmt.lower()))
        if cw and sw and len(cw & sw) / len(cw) > 0.6:
            out["RESTATEMENT"].append((k, v["grade"], c)); continue
        out["SUBSTANTIVE"].append((k, v["grade"], c))
    return out

with State("check_audit") as s:
    REG = step(s, "load the mathematics register", load, budget=120)
    cls = step(s, "classify every check", lambda: classify(REG), budget=300)

tot = sum(len(v) for v in cls.values())
print(f"  EVERY CHECK IN THE MATHEMATICS REGISTER — could it have failed?\n")
print(f"  {'class':<18}{'objects':>9}{'':>4}")
for k in ["SUBSTANTIVE", "SELF-NAMED", "RESTATEMENT", "NO DENOMINATOR", "NO CHECK"]:
    v = cls.get(k, [])
    if v: print(f"  {k:<18}{len(v):>9}   {100*len(v)//tot}%")
print()
for k in ["SELF-NAMED", "NO DENOMINATOR", "RESTATEMENT"]:
    v = cls.get(k, [])
    if not v: continue
    print(f"  {k} — {len(v)} objects:")
    for a, g, c in sorted(v)[:14]:
        print(f"      {a:<14}{g:<13}{c[:56]}")
    if len(v) > 14: print(f"      ... and {len(v)-14} more")
    print()
