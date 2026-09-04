#!/usr/bin/env python3
"""regmath.py -- which register entries are corroborable by mathematics?

An entry is CORROBORABLE when a proof, theorem, equation or expression settles
it. It is then owed a reference to that object, and the reference must be
searchable -- findable from the entry and from the object alike.

Three classes, and the third is the finding:
  CARRIED    the entry already names or states the object
  OWED       the entry is corroborable and does not name it
  NARRATIVE  no mathematical object settles it -- a process fact, a decision,
             a defect of navigation
"""
import re, sys
from collections import Counter
from zeno import State, step
from mathreg import REG

S = open("The Method 1.4.md", encoding="utf-8").read()
RS, RE_ = S.rindex("## 26. Withdrawals"), S.rindex("## 27.")
REGTXT = S[RS:RE_]

def entries():
    out, pat = [], re.compile(r"^ {0,3}((?:\d{3}, )*\d{3})\. ", re.M)
    ms = list(pat.finditer(REGTXT))
    for i, m in enumerate(ms):
        end = ms[i+1].start() if i+1 < len(ms) else len(REGTXT)
        nums = [int(x) for x in re.findall(r"\d{3}", m.group(1))]
        out.append((nums, REGTXT[m.end():end].strip()))
    return out

# ---- what counts as a mathematical corroborator, present in the entry -------
MATH_MARK = [
 (r"[=≤≥<>≠∈⊆∏Σ√∎]",                       "a relation or an operator"),
 (r"\bE\(|\bℛ\(|φ̂|χ_?Λ|ⅅ|\bJ\(Λ\)|F\(−?1\)", "a named quantity of this book"),
 (r"\bΛ(₈|₉|₁₀|₁₁|₁₂|₁₃|₉′)?\b",             "the lattice or a stage of the tower"),
 (r"\btheorem\b|\bproof\b|\blemma\b|\bproposition\b", "a theorem, proof or lemma"),
 (r"\b\d[\d,]{2,}\b",                        "a computed count"),
 (r"\b\d+(\.\d+)?%",                         "a computed rate"),
 (r"Baker|Pixley|Bergman|Birkhoff|Dilworth|Racah|Freuder|Montanari|Dechter|"
  r"Deville|Brylawski|Nesterov|Aitken|Sperner|Kimura|Edlén|Edlen",
                                             "an attributed result"),
]
# entries whose SUBJECT is mathematical even when the text carries no symbol
SUBJ = [
 (r"closure|closed|E\(X\)|defect",           "closure"),
 (r"arity|two[- ]parent|tree|cycle|treewidth","constraint shape"),
 (r"density|fibration|fibred|coordinate",     "the box and its coordinates"),
 (r"bracket|containment|monoton",             "the bracket"),
 (r"parastatistic|coupling|seniority|spin",   "the tower"),
 (r"precedent|attribut|cited",                "attribution"),
]
NARRATIVE = re.compile(
 r"cross-reference|heading|numbering|contents|markup|emphasis|apostrophe|"
 r"stale|prepend|indent|renumber|typo|caption|glyph|font|whitespace|"
 r"figure \d|dpi|the press|hardcode|literal|regex|character class", re.I)

def classify():
    rows = []
    for nums, txt in entries():
        marks = [why for pat, why in MATH_MARK if re.search(pat, txt)]
        subj  = [why for pat, why in SUBJ if re.search(pat, txt, re.I)]
        narr  = bool(NARRATIVE.search(txt))
        # does the entry point at a section, where the object would live?
        ref   = bool(re.search(r"§[\dA-G]", txt))
        if marks:
            cls = "CARRIED" if ref or "theorem" in " ".join(marks) else "CARRIED, unreferenced"
        elif subj and not narr:
            cls = "OWED"
        elif narr:
            cls = "NARRATIVE"
        else:
            cls = "OWED" if subj else "NARRATIVE"
        rows.append((nums, cls, marks, subj, ref, txt))
    return rows

with State("regmath") as st:
    rows = step(st, "classify every register entry", classify, budget=120)

c = Counter(r[1] for r in rows)
tot = sum(c.values())
print(f"  register entries parsed (lines, some carrying several numbers): {tot}")
print(f"  distinct entry numbers: {len({n for r in rows for n in r[0]})}\n")
for k, v in c.most_common():
    print(f"    {k:<24}{v:>5}   {100*v/tot:>5.1f}%")

print("\n  CARRIED but with no § reference -- corroborable, stated, not searchable:")
n = 0
for nums, cls, marks, subj, ref, txt in rows:
    if cls == "CARRIED, unreferenced":
        n += 1
        if n <= 10:
            print(f"    {','.join(map(str,nums)):<10} {re.sub(chr(10),' ',txt)[:96]}")
print(f"    ... {n} in total")

print("\n  OWED -- mathematical in subject, carrying neither an object nor a reference:")
n = 0
for nums, cls, marks, subj, ref, txt in rows:
    if cls == "OWED":
        n += 1
        if n <= 10:
            print(f"    {','.join(map(str,nums)):<10} [{','.join(subj)}] {re.sub(chr(10),' ',txt)[:78]}")
print(f"    ... {n} in total")

# ---- searchability: can an entry be found FROM the object, and vice versa? --
print("\n  SEARCHABILITY, both directions")
obj_to_reg = sum(1 for k, v in REG.items() if re.search(r"reg\.|register", v["src"]))
reg_to_sec = sum(1 for r in rows if r[4])
print(f"    register entries carrying a § reference        {reg_to_sec:>4} of {tot}"
      f"  ({100*reg_to_sec/tot:.0f}%)")
print(f"    mathematical objects citing a register entry   {obj_to_reg:>4} of {len(REG)}"
      f"  ({100*obj_to_reg/len(REG):.0f}%)")
print(f"    entries findable BY the object they corroborate: no index exists")
sys.exit(0)
