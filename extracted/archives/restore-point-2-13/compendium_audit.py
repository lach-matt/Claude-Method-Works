#!/usr/bin/env python3
"""compendium_audit.py -- PART 2: completeness.

Register 649: part 1 checked that the five documents AGREE. This checks that
each contains what it says it contains — a compendium claiming 197 objects and
listing 190 is worse than one that disagrees with the book, because nothing
would catch it.

Every check compares a document's stated scope against its own contents.
Under zeno.
"""
import re, os, sys, importlib.util as iu
from zeno import State, step

# ---------------------------------------------------------------- acyclicity
# Register 1208. The dangling-dependency check verifies that every named dependency
# EXISTS. It never checked that the graph is ACYCLIC, and a cycle passed 248 objects
# and six audit sets undetected: Q.delta -> Q.exch -> Q.delta, created when the
# exchange factor was registered as depending on the equation it is a part of.
# A cycle means an object's justification passes through itself.
def check_acyclic(REG):
    import sys
    from collections import defaultdict
    dep = {k: [d for d in v['dep'] if d in REG] for k, v in REG.items()}
    col = defaultdict(int); cyc = []
    def dfs(u, st):
        col[u] = 1; st.append(u)
        for v in dep[u]:
            if col[v] == 1: cyc.append(st[st.index(v):] + [v])
            elif col[v] == 0: dfs(v, st)
        st.pop(); col[u] = 2
    old = sys.getrecursionlimit(); sys.setrecursionlimit(50000)
    for k in sorted(REG):
        if col[k] == 0: dfs(k, [])
    sys.setrecursionlimit(old)
    return cyc

def load(p):
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""

def run():
    F = {}
    M = load("COMPENDIUM.md"); S = load("SPECTRA.md")
    R = load("REGISTER.md");   I = load("INDICES.md")
    B = load("The Method 1.6.md")

    sp = iu.spec_from_file_location("_mr", "mathreg.py"); mr = iu.module_from_spec(sp)
    try: sp.loader.exec_module(mr)
    except SystemExit: pass
    REG = mr.REG

    # --- MATHEMATICAL: every register object present, once
    ids = re.findall(r"^### `([^`]+)`", M, re.M)
    F["math: every object listed"] = len(set(REG) - set(ids))
    F["math: no object listed twice"] = len(ids) - len(set(ids))
    m = re.search(r"\*\*(\d+) objects · (\d+) roots · (\d+) settled · (\d+) unfinished", M)
    F["math: header matches its own list"] = 0 if (m and int(m.group(1)) == len(ids)) else 1
    roots = len([k for k, v in REG.items() if not v["dep"]])
    F["math: root count correct"] = 0 if (m and int(m.group(2)) == roots) else 1
    # every dependency named must itself be an entry
    dep = {d for v in REG.values() for d in v["dep"]}
    F["math: no dangling dependency"] = len(dep - set(REG))

    # --- SPECTRA: the row count it claims
    # register 1215: the compendium was rebuilt as a coordinate supply and the
    # header now reads "N channel rows across M elements . K interior cells parsed."
    m = re.search(r"\*\*(\d+) channel rows across \d+ elements", S)
    rows = len(re.findall(r"^\| [A-Z][a-z]? [IVX]+ ?\*? \|", S, re.M))
    F["spectra: header matches its own table"] = 0 if (m and int(m.group(1)) == rows) else 1
    tot = sum(int(x) for x in re.findall(r"^\| [A-Z][a-z]? [IVX]+ ?\*? \|[^|]*\|[^|]*\|[^|]*\|\s*(\d+)\s*\|", S, re.M))
    # the disclosure paragraph quotes the ORIGINAL Appendix B sum; the live total
    # is stated in the header and is what must match (register 673)
    m2 = re.search(r"\*\*\d+ channel rows across \d+ elements · ([\d,]+) interior\s*"
                   r"cells parsed\.\*\*", S)
    F["spectra: interior sum stated correctly"] = 0 if (
        m2 and int(m2.group(1).replace(",", "")) == tot) else 1

    # --- REGISTER: every entry, in order, none lost
    # a grouped label covers EVERY number it names, so the compendium's unit is
    # the entry and its coverage is the set of numbers (register 650)
    # Register 1244: these patterns were \\d{3} exactly, so every entry from 1000
    # onward was invisible to the audit as well as to the generator.
    labels = [m.group(1) for m in re.finditer(r"^### ((?:\d{3,4}, )*\d{3,4})", R, re.M)]
    covered = [int(x) for lab in labels for x in re.findall(r"\d{3,4}", lab)]
    ent = covered
    F["register: no number covered twice"] = len(covered) - len(set(covered))
    m = re.search(r"\*\*(\d+) entries, (\d+) to (\d+)\.\*\*", R)
    F["register: header matches its own list"] = 0 if (m and int(m.group(1)) == len(labels)) else 1
    F["register: range correct"] = 0 if (m and int(m.group(2)) == min(covered)
                                         and int(m.group(3)) == max(covered)) else 1
    # every entry the BOOK keeps must be in the compendium
    bRS = B.rindex("## 28. Withdrawals"); bRE = B.rindex("## 29.")
    kept = {int(y) for x in re.findall(r"^ {0,3}((?:\d{3}, )*\d{3,4})\. ", B[bRS:bRE], re.M)
            for y in re.findall(r"\d{3,4}", x)}
    F["register: contains every entry the book keeps"] = len(kept - set(ent))

    # --- REFERENCES: every entry must be cited somewhere in the book.
    # The reconstruction orphaned six by dropping the only register entries that
    # cited them, and no audit looked (register 656).
    Rf = B[B.rindex("# References"):]
    Bd = B[:B.rindex("# References")]
    auth = {m.group(1).split(",")[0].split("&")[0].strip()
            for m in re.finditer(r"\*\*([A-Z][^*]{2,60}?)\*\*\s*\(?(?:19|20)\d{2}", Rf)}
    # the register left the book, so a reference cited only by a register entry is
    # cited by the WORK — the check spans the book and the register (register 658)
    Rg = open("REGISTER.md", encoding="utf-8").read() if os.path.exists("REGISTER.md") else ""
    F["references: every entry cited in the work"] = len([a for a in auth
                                                          if a not in Bd and a not in Rg])

    # --- INDICES: the tables it claims
    m = re.search(r"Λ₈ — all (\d+) cells", I)
    l8 = len(re.findall(r"^\| \d+ \| \d \| \d \| \d \| \d \| \d \| \d \| \d \| \d \|", I, re.M))
    F["indices: Λ₈ table complete"] = 0 if (m and int(m.group(1)) == l8) else 1
    # nine since the Loewdin work added section IX, the thirteen indexes built
    # in it (register 1351: the Index of Indices must hold every index in full)
    F["indices: has all nine sections"] = 9 - len(re.findall(r"^# [IVX]+ · ", I, re.M))
    # every figure referenced exists
    figs = re.findall(r"\]\(([^)]+\.png)\)", I)
    F["indices: every figure file present"] = len([f for f in figs if not os.path.exists(f)])
    return F, len(ids), rows, len(ent), l8

with State("compendium_audit") as st:
    F, n_obj, n_row, n_ent, n_l8 = step(st, "check each compendium against its own claims", budget=900,
                                        fn=None) if False else step(
        st, "check each compendium against its own claims", run, budget=900)

print(f"  PART 2 · COMPLETENESS\n")
print(f"  mathematical: {n_obj} objects · spectra: {n_row} rows · "
      f"register: {n_ent} entries · indices: {n_l8} Λ₈ cells\n")
for k, v in F.items():
    print(f"  {k:<46}{'PASS' if v == 0 else f'FAIL ({v})'}")
bad = [k for k, v in F.items() if v]
print("\n" + ("PART 2 PASSES" if not bad else f"FAILURES: {bad}"))
sys.exit(1 if bad else 0)
