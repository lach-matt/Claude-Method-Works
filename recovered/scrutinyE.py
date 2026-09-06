#!/usr/bin/env python3
"""scrutinyE.py -- Batch 5: the 132 mathematical objects, remainder.

112 checks reproduced from the construction in the math audit. This takes the
objects that carry no check, sorts them by what would settle each, and reports
which are settled by a proof in the book, which by a citation, and which by
nothing.
"""
import re, sys
from collections import Counter, defaultdict
from zeno import State, step
from mathreg import REG

S = open("The Method 1.4.md", encoding="utf-8").read()
OUT = []

# citations this session already found mis-stated or unentered
CITE_STATUS = {
 "Freuder 1982": ("MIS-CITED, corrected this session",
                  "gives backtrack-free search at strong (w+1)-consistency, NOT global "
                  "consistency; that is Dechter 1992"),
 "Montanari 1974": ("ENTERED this session", "path consistency implies global consistency "
                    "for monotone constraints"),
 "Bergman double-projection; Baker–Pixley 1975 (majority term)":
     ("CARRIED, reg. 224", "a sublattice of a finite product is determined by its two-fold "
      "projections; the book's central theorem, fifty years late"),
 "binary path consistency / 2-decomposability (Kimura et al. 2024)":
     ("CARRIED, reg. 226", "the property E(X) = 0 is a named class in CSP"),
 "global consistency (CSP)": ("CARRIED", "the identification licensing Freuder and Montanari"),
 "Racah 1943 seniority": ("CARRIED, reg. 263", "entered late; the tower rests on it directly"),
 "Birkhoff representation 1937": ("CARRIED", "verified here: 976 down-sets of 17 generators"),
 "Sperner property / Dilworth": ("CARRIED", "verified here: widest level 122 at rank 11"),
 "Newton decrement, Nesterov–Nemirovskii 1994": ("CARRIED", "verified: lambda^2 = (2/3)T"),
 "Aitken Δ² / Seki Kōwa": ("CARRIED", "verified: lands at T/3 to four figures"),
 "self-concordance": ("CARRIED", "verified: crosses unity between nu = 405 and 406"),
 "Reeh–Schlieder": ("CARRIED, unread", "[A] grade -- abstract only"),
 "Tomita–Takesaki": ("CARRIED, unread", "[S] grade -- secondary only"),
 "Borchers 1992 / Wiesbrock 1993": ("CARRIED", "the characterisation, an iff"),
 "Takesaki duality 1973": ("CARRIED, with a caveat the book states",
                           "stated for R; the 2024 generalisation is NOT automatic"),
 "semifiniteness": ("CARRIED", "von Neumann classification"),
 "Sorce 2024": ("CARRIED", "geometric modular flow needs a conformal Killing field"),
 "Brunetti–Fredenhagen–Verch 2003": ("CARRIED", "the functor whose four parts are the partition"),
 "node counting": ("STRUCTURAL", "the hydrogenic radial solution; standard"),
 "Pauli": ("STRUCTURAL", "standard"),
 "vector coupling": ("STRUCTURAL", "standard"),
 "data-processing inequality + Pinsker": ("CARRIED", "the decay theorem's two steps"),
 "Helly number": ("CARRIED", "Helly 1923, in the references"),
 "monotone interpolation bracket": ("STRUCTURAL", "the bracket's own definition"),
 "closure operator (Moore family)": ("CARRIED", "standard"),
 "closure defect": ("CARRIED", "Galois / formal concept analysis, claimed as application"),
 "projection onto coordinate i": ("DEFINITIONAL", "—"),
 "monotone upper envelope / staircase bound":
     ("NAMED THIS SESSION", "Deville, Barták and Van Hentenryck 1999 -- the staircase class"),
 "the recovery operator": ("DEFINITIONAL", "—"),
 "extensivity": ("PROVED in the book", "one line, A.4"),
 "adjunction never repairs (M Thm 10.1)": ("PROVED in the book", "Theorem 10.1"),
 "modularity (equality, not submodularity)": ("CARRIED", "verified: 0 violations on 475,800 pairs"),
 "divisor lattice embedding": ("CARRIED", "verified: gcd = meet, lcm = join"),
 "distinct-prime-counting function": ("PROVED in the book", "one prime per coordinate"),
 "Möbius function of a distributive lattice": ("CARRIED", "standard"),
 "caterpillar tree": ("CARRIED", "verified: 8 nodes, 7 edges, one of degree 3"),
 "palindromic rank polynomial ⟺ self-dual": ("CARRIED", "verified: not palindromic, 8 survivors"),
 "monotone boolean circuit": ("CARRIED", "verified: 20 gates accept exactly 976 of 131,072"),
 "Brylawski 1973": ("CARRIED, reg. 355", "the n-body index, correct and not first"),
}

def run():
    unchecked = [(k, v) for k, v in REG.items() if not v["check"]]
    by = defaultdict(list)
    for k, v in unchecked:
        nm = v["named"]
        if nm and nm in CITE_STATUS:
            st, note = CITE_STATUS[nm]
        elif nm:
            st, note = "NAMED, unverified here", nm
        else:
            st, note = ("SETTLED BY THE BOOK'S OWN PROOF"
                        if v["grade"] == "PROVED" else
                        "RESTS ON THE BOOK'S COMPUTATION ALONE"
                        if v["grade"] == "COMPUTED" else
                        "DEFINITIONAL, nothing owed" if v["grade"] == "DEFINITIONAL" else
                        v["grade"]), "—"
        by[st].append((k, v["grade"], v["stmt"][:70], note))
    return by

with State("scrutinyE") as st:
    by = step(st, "sort the unchecked objects", run, budget=60)

tot = sum(len(v) for v in by.values())
print(f"  objects registered {len(REG)}   verified by computation this session 77")
print(f"  carrying no check: {tot}\n")
order = sorted(by, key=lambda k: -len(by[k]))
for k in order:
    print(f"  {k}  —  {len(by[k])}")
    for oid, grade, stmt, note in sorted(by[k]):
        print(f"      {oid:<12}{grade:<13}{stmt}")
        if note != "—": print(f"      {'':<12}{'':<13}→ {note[:88]}")
    print()
print("  " + " · ".join(f"{k} {len(v)}" for k, v in sorted(by.items(), key=lambda x: -len(x[1]))))
