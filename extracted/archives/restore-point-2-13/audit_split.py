#!/usr/bin/env python3
"""audit_split.py -- which audits pertain to the INDICES, and which to the book.

Register 634: for the literature, the audits that matter are the ones testing
the indices and their functions — not the ones testing whether the artefact
renders. This classifies all twenty-two and reports the split, under zeno.
"""
from zeno import State, step
def run():
    A = [
      (1,  "LATTICE",       "index", "Λ's cells, closure and defect recomputed from the construction"),
      (2,  "EQUATIONS",     "index", "the printed identities re-derived — F(1), F(−1), d(x,y), E"),
      (3,  "CONSISTENCY",   "book",  "the spelled register total against the entries"),
      (4,  "REDUNDANCY",    "book",  "a claim stated twice in two places"),
      (5,  "ARTEFACT",      "book",  "the PDF's glyphs, images and size"),
      (6,  "COHERENCE",     "book",  "every § reference resolves to a heading"),
      (7,  "ATTRIBUTION",   "book",  "every cited name has a reference entry"),
      (8,  "CELL",          "index", "every cell the text names exists in the index"),
      (9,  "DISTINCTNESS",  "index", "no two index coordinates collapse"),
      (10, "SCOPE",         "index", "an E value is stated with the index it belongs to"),
      (11, "ANTECEDENT",    "book",  "no subsection without its parent"),
      (12, "MARKUP",        "book",  "no literal markup in the rendered text"),
      (13, "AGREEMENT",     "index", "one quantity, one value across the whole work"),
      (14, "ARITHMETIC",    "index", "the tower's own table against the recomputed tower"),
      (15, "ENUMERATION",   "book",  "a heading's count against what it holds"),
      (16, "FIDELITY",      "book",  "the press's own strings against the source"),
      (17, "MEASURE",       "book",  "figure count, file sizes"),
      (18, "REPRODUCTION",  "index", "the two headline figures reproduce"),
      (19, "SEQUENCE",      "book",  "headings and entries ascend"),
      (20, "PROJECTION",    "index", "no claim of predictive power anywhere"),
      (21, "INPUT",         "index", "every computation names its input set"),
      (22, "CENSUS",        "book",  "prose counts against the lists they count"),
    ]
    return A
with State("audit_split") as st:
    A=step(st,"classify the twenty-two",run,budget=60)
idx=[a for a in A if a[2]=="index"]; bk=[a for a in A if a[2]=="book"]
print(f"  THE INDEX AUDITS — {len(idx)} of 22, and these are the ones the literature needs\n")
for n,nm,_,d in idx: print(f"    {n:>3}  {nm:<14}{d}")
print(f"\n  THE ARTEFACT AUDITS — {len(bk)} of 22, about the book rather than the index\n")
for n,nm,_,d in bk: print(f"    {n:>3}  {nm:<14}{d}")
print(f"\n  {len(idx)} index · {len(bk)} artefact")
