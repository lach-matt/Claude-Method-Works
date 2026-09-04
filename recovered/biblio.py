#!/usr/bin/env python3
"""biblio.py -- the bibliography as an index, and the identification tested.

The claim: the bibliography is the one open index of the method, and it is what
the multiverse reading of §27.2.2 is to the book.

Two things must be separated before that can be agreed:
  §27.2.2 / §30.6.1  the multiverse CANNOT BE POSED -- §E.1.4 shows the open set
                     cannot express an unclosable question, because every value
                     of its obstacle column names a route
  Q item C           the unentered literatures CAN be posed -- obstacle
                     'retrievable', cost 'unbounded'

So the test is whether the bibliography's obstacle column names a route. If it
does, it is an open item and not the multiverse. If it does not, the
identification holds.
"""
import itertools
from zeno import State, step

def R(X, d):
    A = [sorted({x[i] for x in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for x in X: m[x[j]] = max(m.get(x[j], -10**9), x[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in itertools.product(*A)
            if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j)}

# ---------------------------------------------------------------- coordinates
# era      0 pre-digital (<1950)   1 print, digitised   2 born-digital / deposited
# rho      retrieval redundancy, §19.1     0: rho<=1   1: rho 2-3   2: rho>=4
# access   0 blocked  1 secondary  2 abstract  3 full text     (App. B)
# entered  0 named, unentered  1 entered by one query  2 entered deeply
AX = [3, 3, 4, 3]

def admissible(e, r, a, n):
    if r > 0 and e < 1: return False      # redundancy is a property of the era, §19.5
    if r > 1 and e < 2: return False
    if a > 1 and r < 1: return False      # you cannot reach a full text at rho <= 1
    if a > 2 and r < 2: return False
    if n > 0 and a < 1: return False      # you cannot enter what you cannot reach
    if n > 1 and a < 3: return False      # entering DEEPLY needs the full text
    return True

CELLS = {(e, r, a, n) for e in range(3) for r in range(3)
         for a in range(4) for n in range(3) if admissible(e, r, a, n)}

# --------------------------------------------------- the corpus's own sources
SRC = [
 ("Edlen, Handbuch XXVII 1964",      0, 0, 0, 0, "blocked; read at one remove via Curtis"),
 ("Ritz, Phys. Zeit. 1908",          0, 0, 0, 0, "blocked, rho <= 2"),
 ("Paschen & Gotze 1922",            0, 0, 0, 0, "scanned, OCR, not exposed"),
 ("Dunz 1911",                       0, 0, 0, 0, "blocked"),
 ("Curtis, Phys. Scripta 1987",      1, 1, 3, 2, "read in full, the secondary route"),
 ("Racah 1942, 1943",                1, 1, 2, 1, "attributed, entered late"),
 ("Condon & Shortley 1935",          1, 1, 2, 1, "audit 23 reproduces 10 of 10 tables"),
 ("Birkhoff 1937",                   1, 1, 2, 1, "cited for the representation"),
 ("Baker & Pixley 1975",             1, 1, 2, 1, "reg. 224, the central theorem"),
 ("Freuder 1982",                    2, 2, 3, 1, "the certificate -- and MIS-cited"),
 ("Montanari 1974",                  2, 2, 3, 1, "the monotone certificate"),
 ("Dechter 1992",                    2, 2, 3, 0, "IN THE BIBLIOGRAPHY, CITED FOR NOTHING"),
 ("Deville et al. 1999",             2, 2, 3, 0, "located this session, not entered"),
 ("van Beek & Dechter 1995, 1997",   2, 2, 3, 1, "tightness and row-convexity"),
 ("Kimura et al. 2024",              2, 2, 3, 1, "2-decomposability, reg. 226"),
 ("Brylawski 1973",                  1, 1, 2, 1, "the n-body index, reg. 355"),
 ("Nesterov & Nemirovskii 1994",     1, 1, 2, 1, "the Newton decrement"),
 ("Moore 1966 / IEEE 1788",          1, 1, 2, 1, "the cost framing"),
 ("Kreuzer-Skarke catalogue",        2, 2, 1, 0, "a file format, Q item D"),
 ("partial order in chemistry",      2, 2, 2, 0, "named and unentered, reg. 251"),
 ("the seniority lattice question",  2, 2, 2, 0, "named and unentered, Q item N"),
 ("the nine unentered literatures",  2, 2, 2, 0, "Q item C, cost UNBOUNDED"),
]

def close():
    occ = {tuple(s[1:5]) for s in SRC}
    return R(CELLS, 4), R(occ, 4), occ

with State("biblio") as st:
    Rall, Rocc, occ = step(st, "close the bibliography index", close, budget=60)

box = 1
for a in AX: box *= a
print(f"  the bibliography as an index")
print(f"    admissible cells      {len(CELLS)}")
print(f"    ambient box           {box}")
print(f"    density               {100*len(CELLS)/box:.1f}%")
print(f"    E(admissible set)     {len(Rall)-len(CELLS)}")
print(f"\n    sources placed        {len(SRC)}")
print(f"    distinct cells        {len(occ)}")
print(f"    E(the corpus's own bibliography)   {len(Rocc)-len(occ)}")
print(f"    possibility bound     0 <= E <= {len(CELLS)-len(occ)}")

print(f"\n  the cells the bibliography admits and does not hold:")
V=[["pre-digital","digitised print","born-digital"],
   ["rho <= 1","rho 2-3","rho >= 4"],
   ["blocked","secondary","abstract","full text"],
   ["named, unentered","entered by one query","entered deeply"]]
for g in sorted(Rocc-occ):
    print(f"    {V[0][g[0]]:<16}{V[1][g[1]]:<10}{V[2][g[2]]:<12}{V[3][g[3]]}")

print(f"""
  THE IDENTIFICATION, TESTED

  §E.1.4's criterion: the open set cannot express an unclosable question,
  because every value of its obstacle column NAMES A ROUTE.

    the multiverse reading (§27.2.2)   obstacle = none. no search settles it in
                                       either direction. NOT POSABLE.
    the bibliography                   obstacle = 'retrievable', cost
                                       'unbounded'. Q item C. POSABLE.

  So the two are NOT the same object. But they share the property that decides
  the debt, and it is not retrievability:""")

print(f"""
    §27.1  novelty has ONE route -- search -- and can never have two.
           D(novelty) = 0, necessarily and permanently. Not undefended:
           UNDEFENDABLE.

  The reference index has four coordinates. THREE are internal -- access,
  referent, checked are all recordable from the book's own pages. ONE is not:
  VERDICT requires reading someone else's theorem, and the index that supplies
  it is the bibliography.

    D(bibliography) = 0 by §27.1
    => D(verdict) = 0, inherited
    => the reference index carries one coordinate that CANNOT BE DEFENDED BY
       TWO ROUTES, however many sources are entered.

  That is why the debt is unpayable, and blocked access is not the reason.
  Blocked access caps FOUR of twenty-eight terms. The undefendability of
  verdict caps ALL of them.""")
