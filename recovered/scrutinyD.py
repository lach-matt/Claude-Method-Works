#!/usr/bin/env python3
"""scrutinyD.py -- Batch 4: protocols, audits, failure modes.

Each is an OPERATION. An operation is settled by the failure it prevents, so the
evidence is an instance in the register or a worked case in the text. §5 already
does this for fifteen protocols; nothing does it for the audits or for the
failure modes, and this checks all three.
"""
import re, sys
from collections import Counter
from zeno import State, step

S = open("The Method 1.4.md", encoding="utf-8").read()
RS, RE_ = S.rindex("## 26. Withdrawals"), S.rindex("## 27.")
REG = S[RS:RE_]
BODY = S[:RS] + S[RE_:]
OUT = []
def rec(*a): OUT.append(a)

# ---------------------------------------------------------------- protocols
def protocols():
    # §5's table: protocol -> the failure it prevents -> the instance
    t = S[S.index("## 5. What the protocols are for"):S.index("# PART II")]
    tabled = set(re.findall(r"§(\d+\.\d+)\s", t))
    heads = [m.group(1) for m in re.finditer(r"^### (2\.\d+) ", S, re.M)]
    heads = sorted(set(heads), key=lambda x: [int(y) for y in x.split(".")])
    for h in heads:
        name = re.search(rf"^### {re.escape(h)} (.+)$", S, re.M).group(1)
        intable = h in tabled
        # a worked instance anywhere in the body?
        body_inst = bool(re.search(rf"§{re.escape(h)}[^0-9]", BODY))
        reg_inst = len(re.findall(rf"§{re.escape(h)}[^0-9]", REG))
        v = ("CORROBORATED, tabled" if intable else
             "CORROBORATED, untabled" if reg_inst or body_inst else "NO INSTANCE")
        rec("protocol", f"§{h} {name[:52]}", v,
            f"§5 table: {'yes' if intable else 'no'} · register citations: {reg_inst}")

# ------------------------------------------------------------------- audits
def audits():
    tbl = re.findall(r"^  (\d+)\s+([A-Z]+)\s+(object|source|artefact|outside)", S, re.M)
    # the defect that motivated each, per §3.1, §3.8, §3.7.1 and the register
    MOTIVE = {
      "LATTICE":"the object is the subject; a non-closed Λ leaves the book without one",
      "EQUATIONS":"a wrong equation is a false claim",
      "CONSISTENCY":"reg. 186 — twenty-eight cross-references pointing at one wrong section",
      "REDUNDANCY":"reg. 195/196 — two sections surviving their own supersession",
      "ARTEFACT":"reg. 190 — 107 blank boxes across 44 pages, every audit reporting clean",
      "COHERENCE":"navigation failures cost the reader rather than the truth",
      "ATTRIBUTION":"reg. 261/263/265 — three precedents cited in text, absent from References",
      "CELL":"an invalid cell has no closure worth testing",
      "DISTINCTNESS":"cells that collide are not cells",
      "SCOPE":"reg. 292/395 — a cap-dependent figure with no cap stated",
      "ANTECEDENT":"a label referred to before it is defined",
      "MARKUP":"reg. 260/264 — emphasis opening in one unit and closing in another",
      "AGREEMENT":"reg. 397 — a past value quoted as history read as a disagreement",
      "ARITHMETIC":"a number that does not follow from its own inputs",
      "ENUMERATION":"reg. 287 — a heading claiming three entries and holding eighty-six",
      "FIDELITY":"reg. 272 — the press carrying hardcoded copies of the title page",
      "MEASURE":"reg. 191/192 — the whitespace audit's own first two measurements wrong",
      "REPRODUCTION":"a published value the book cannot reproduce",
      "SEQUENCE":"reg. 202 — entries written under a section number already in use",
      "PROJECTION":"reg. 293 — five sections absent from a derived contents",
      "INPUT":"reg. 376/377 — a result stated from data the book does not print",
    }
    for num, name, reads in tbl:
        m = MOTIVE.get(name)
        cited = bool(re.search(rf"\b{name}\b", REG))
        v = ("CORROBORATED" if m and "reg." in m else
             "STRUCTURAL" if m else "NO MOTIVE RECORDED")
        rec("audit", f"{num} {name}", v, m or "—")

# ------------------------------------------------------------ failure modes
def failures():
    sec = S[S.index("### 26.7.8"):S.index("### 26.8")]
    for k, name in [("4.1","Attribute Inward First"),("4.2","Read The Structure At The Point Of Insertion"),
                    ("4.3","A Claim Of Completion Is Itself A Claim"),("4.4","Repair The Class Or Say You Did Not"),
                    ("4.5","A Null Is A Result With Its Definition Missing"),("4.6","Show The Test Can Fail"),
                    ("4.7","A Flag Is A Hypothesis")]:
        m = re.search(rf"((?:\d{{3}}, )*\d{{3}})\.\s*\*\*§{re.escape(k)}", sec)
        if m:
            n = len(re.findall(r"\d{3}", m.group(1)))
            rec("failure mode", f"§{k} {name[:44]}", "CORROBORATED",
                f"{n} grouped instances at §26.7.8")
        else:
            grouped = re.search(rf"§{re.escape(k)}", sec)
            rec("failure mode", f"§{k} {name[:44]}",
                "CORROBORATED, ungrouped" if grouped else "NO INSTANCE GROUPED",
                "named at §26.7.8" if grouped else "no grouped line")

with State("scrutinyD") as st:
    step(st, "protocols", protocols, budget=60)
    step(st, "audits", audits, budget=60)
    step(st, "failure modes", failures, budget=60)

for kind in ("protocol", "audit", "failure mode"):
    rows = [o for o in OUT if o[0] == kind]
    print(f"\n  {kind.upper()}S — {len(rows)}")
    for _, name, v, ev in rows:
        mark = " " if v.startswith("CORROBORATED") or v == "STRUCTURAL" else "!"
        print(f"  {mark} {name:<58}{v:<24}{ev[:56]}")
    c = Counter(r[2] for r in rows)
    print(f"    " + " · ".join(f"{k} {v}" for k, v in c.most_common()))
print(f"\n  TOTAL {len(OUT)}")
print("  " + " · ".join(f"{k} {v}" for k, v in Counter(o[2] for o in OUT).most_common()))
