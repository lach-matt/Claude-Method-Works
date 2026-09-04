#!/usr/bin/env python3
"""indices.py -- the index of indices, generated.

Every index this work builds on or beside the atomic index: what it holds, what
its coordinates are, whether it closes, whether it carries a time column, and
what role it plays for Λ.

Measured where measurable. Where an index is named in conversation but never
built, that is stated rather than filled in — §29.1's rule, applied to this
document's own scope.

Rebuild:  python3 indices.py > INDICES.md
"""
import itertools, datetime, sys
from zeno import State, step

def clos(X, d):
    X = list(X); A = [sorted({c[i] for c in X}) for i in range(d)]
    def e(a, b):
        m = {}
        for c in X: m[c[b]] = max(m.get(c[b], -99), c[a])
        z = -99; o = {}
        for t in sorted(m): z = max(z, m[t]); o[t] = z
        return o
    ph = {(a, b): e(a, b) for a in range(d) for b in range(d) if a != b}
    return {x for x in itertools.product(*A)
            if all(x[a] <= ph[(a, b)][x[b]] for a in range(d) for b in range(d) if a != b)}

def measure(X, d):
    X = set(X)
    A = [sorted({c[i] for c in X}) for i in range(d)]
    box = 1
    for v in A: box *= len(v)
    return len(X), box, len(clos(X, d)) - len(X)

def run():
    from method_tower import base, max2J
    out = {}
    L8 = [tuple(c) for c in base((3,3,1,3,1))]
    L9  = [c + (s,) for c in L8 for s in range(0, c[6] + 1)]
    L10 = [c + (v,) for c in L9 for v in range(c[8], c[6] + 1)]
    ph = {}; r = 0
    for k in range(0, 4):
        m = max((max2J(l, kk) for l in range(0, 2) for kk in range(1, min(4*l+2, k)+1)), default=0)
        r = max(r, m); ph[k] = r
    L11 = [c + (j,) for c in L10 for j in range(0, ph[c[2]] + 1)]
    L12 = [c + (K,) for c in L11 for K in range(abs(c[10]-2*c[5]), c[10]+2*c[5]+1, 2)]
    L13 = [c + (J,) for c in L12 for J in range(max(0, c[11]-1), c[11] + 2)]

    def comp(X, si, ti):
        S = {tuple(c[i] for i in si) for c in X}
        return sum(1 for c in X if tuple(c[i] for i in ti) in S)

    out["tower"] = [
      ("Λ₈",  len(L8),  8, *measure(L8, 8)[1:],  comp(L8,  (0,1,2,7), (4,5,6))),
      ("Λ₉",  len(L9),  9, *measure(L9, 9)[1:],  comp(L9,  (0,1,2,7), (4,5,6,8))),
      ("Λ₁₀", len(L10),10, None, 0,              comp(L10, (0,1,2,7), (4,5,6,8))),
      ("Λ₁₁", len(L11),11, None, 0,              comp(L11, (0,1,2,7,10), (4,5,6,8,10))),
      ("Λ₁₂", len(L12),12, None, 0,              comp(L12, (0,1,2,7,10), (4,5,6,8,11))),
      ("Λ₁₃", len(L13),13, None, 0,              comp(L13, (0,1,2,7,10), (4,5,6,8,12))),
    ]
    # the drawn objects
    G = {1:[1,18], 2:[1,2]+list(range(13,19)), 3:[1,2]+list(range(13,19))}
    for p in (4,5,6,7): G[p] = list(range(1,19))
    TAB = [(p,g) for p in G for g in G[p]]
    JAN = []
    ORD = [(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
           (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1)]
    Z = 0
    for (n,l) in ORD:
        for _ in range(1, 4*l+3):
            Z += 1
            if Z > 118: break
            JAN.append((n+l, Z))
        if Z > 118: break
    D = [31,28,31,30,31,30,31,31,30,31,30,31]
    CAL = [(m+1,d) for m in range(12) for d in range(1, D[m]+1)]
    BOX = [(a,b,c) for a in range(5) for b in range(5) for c in range(5) if a>=b>=c]
    CHESS = [(r,f) for r in range(8) for f in range(8)]
    out["drawn"] = [("the periodic table", *measure(TAB,2), "(period, group)"),
                    ("Janet's left-step",  *measure(JAN,2), "(n+ℓ, Z)"),
                    ("the calendar",       *measure(CAL,2), "(month, day)"),
                    ("a box ordering",     *measure(BOX,3), "(l, w, h)"),
                    ("a chessboard",       *measure(CHESS,2), "(rank, file)")]
    out["L8"]=L8
    out["TAB"]={p:sorted(G[p]) for p in sorted(G)}
    _j={}
    for k,z in JAN: _j.setdefault(k,[]).append(z)
    out["JAN"]={k:sorted(v) for k,v in sorted(_j.items())}
    out["BOX"]=BOX
    return out

with State("indices") as st:
    M = step(st, "measure every index", run, budget=1500)

L = []; W = L.append
# ---------------------------------------------------- the spectra index, live
def _spectra_index():
    """the Rydberg-channel index, computed from the compendium so it cannot drift"""
    import re as _re, statistics as _st, itertools as _it
    from collections import defaultdict as _dd
    ZN = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"F":9,"Ne":10,"Na":11,
          "Mg":12,"Al":13,"Si":14,"P":15,"S":16,"Cl":17,"Ar":18,"K":19,"Ca":20,
          "Sc":21,"Ti":22,"Fe":26,"Zn":30,"Ga":31,"Cd":48,"Ba":56,"Hg":80,"Bi":83}
    LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}
    rows = [l.rstrip().split("\t") for l in open("SPECTRA-DATA.tsv", encoding="utf-8")][1:]
    H = _dd(list)
    for r in rows:
        m = _re.search(r"n([spdfghik])\b", r[1]); el = _re.match(r"([A-Z][a-z]?)", r[0].strip())
        if not (m and el) or el.group(1) not in ZN: continue
        try: H[(ZN[el.group(1)], int(r[9]), LM[m.group(1)])].append(float(r[7]))
        except Exception: pass
    Zs = sorted({k[0] for k in H}); Cs = sorted({k[1] for k in H}); Ls = sorted({k[2] for k in H})
    ALL = [(Z,c,l) for Z in Zs for c in Cs for l in Ls if c < Z]
    return len(rows), len(H), len(ALL), len(Zs), len(Cs), len(Ls), Cs
_NCH, _NHELD, _NGRID, _NZ, _NC, _NL, _CS = _spectra_index()


W("# THE METHOD 1.6 — THE INDEX OF INDICES")
W("")
W(f"Generated on {datetime.date.today().isoformat()} by `indices.py`. **Every index this work builds")
W("on or beside the atomic index — what it holds, whether it closes, whether it carries time, and")
W("what role it plays for Λ.** Measured where measurable; where an index is named and never built,")
W("that is stated rather than filled in.")
W("")
W("---")
W("")
W("# I · THE ATOMIC INDEX ITSELF")
W("")
W("**Λ = { (n, ℓ, k, q, e, f, g, 2S) ∈ ℤ⁸ : eight constraints, at caps }.**")
W("")
W("![**Figure 1.** Λ₈'s constraint graph. Seven bounds on eight coordinates — a caterpillar with 2S pendant at k. Every edge is a single monotone inequality except one: **g takes two parents**, and g ≤ min(q, 4f+2) is the only non-product term in the whole expression.](figures-compendia/fig-i3-lambda8.png)")
W("")
W("A cell is a **transition**: a source subshell (n, ℓ) holding k electrons, q of them moving, into a")
W("target subshell (e, f) that ends with g, at spin 2S. **Not a state — a move.** Everything else in")
W("this document follows from that.")
W("")
W("| constraint | reads |")
W("|---|---|")
for c, r in (("ℓ ≤ n − 1", "hydrogenic — the subshell fits its shell"),
             ("k ≤ 4ℓ + 2", "**Pauli** — the subshell's capacity"),
             ("q ≤ k", "conservation of the removed — you cannot take more than is held"),
             ("f ≤ e − 1", "hydrogenic again, on the target"),
             ("g ≤ 4f + 2", "**Pauli** again, on the target"),
             ("g ≤ q", "conservation of the placed"),
             ("2S ≤ k", "the multiplicity a subshell can carry"),
             ("k ≥ 1", "*definitional* — a transition needs a mover")):
    W(f"| **{c}** | {r} |")
W("")
W("**The one coupling is g ≤ min(q, 4f+2)**, the single non-product term in the generating function,")
W("and it is the Pauli principle. Remove it and 976 becomes 1,000; the 24 excluded cells all have")
W("f = 0 and g = 3 — three electrons in an s orbital.")
W("")
W("---")
W("")
W("# II · THE TOWER")
W("")
W("**Each stage adds one axis and inherits every bound below.**")
W("")
W("| stage | cells | axes | composable | fraction | the axis added |")
W("|---|---|---|---|---|---|")
AX = ["—", "2S′ ≤ g", "2S′ ≤ v ≤ g", "2J_c ≤ φ̂(k)", "2K ≤ 2J_c + 2f", "\\|2J − 2K\\| ≤ 1"]
for (nm, n, d, box, E, c), ax in zip(M["tower"], AX):
    W(f"| **{nm}** | {n:,} | {d} | {c:,} | **{c/n:.4f}** | {ax} |")
W("")
W("![**Figure 2.** The composable fraction stage by stage. **Λ₈ composes not at all** — four source coordinates against three target. The two counting axes take it to a peak of 0.8087 at Λ₁₀; the three coupling axes lower it every time.](figures-compendia/fig-i1-tower.png)")
W("")
W("> **Counting axes raise the composable fraction; coupling axes lower it. No exception.**")
W("")
W("**Λ₈ composes not at all** — four source coordinates against three target. **Λ₁₀ is the peak at")
W("80.87%**, and every stage after it falls. **The non-composable cells are exactly those with g = 0**")
W("at the peak, since k ≥ 1 forbids an empty target being a source.")
W("")
W("---")
W("")
W("# III · THE INDEXES DRAWN BESIDE IT")
W("")
W("| index | coordinates | cells | box | E | kind |")
W("|---|---|---|---|---|---|")
for nm, n, box, E, coord in M["drawn"]:
    kind = "**state**" if nm != "a box ordering" else "**state**"
    W(f"| {nm} | {coord} | {n} | {box} | **{E}** | {kind} |")
W("")
W("![**Figure 3.** Every index this work builds or draws, by cells against defect. **Circles are transition indexes** — their cells are moves, so they carry a time column. **Squares are state indexes** — a cell is one position, and the question of composition does not arise.](figures-compendia/fig-i2-landscape.png)")
W("")
W("**None of these is a transition index, so none can carry a time column.** A state cell has one")
W("position; the question *is my target another cell's source* does not arise.")
W("")
W("**Janet closes at E = 0 and the classroom table does not.** That is a fact about the two tables")
W("**in coordinates chemists fixed for other reasons** — §21.6 shows any composite count has SOME")
W("coordinate system where E = 0, so the result is that Janet's 1928 ordering, chosen for shell")
W("filling, happens to close.")
W("")
W("---")
W("")
W("# IV · THE VIOLATION INDEX")
W("")
W("**The companion paper's object, indexed over nine letters.** It is here because it is the one")
W("index this work reasons about without holding — **its cells are not printed anywhere**, and what")
W("follows is everything that is.")
W("")
W("| letter | meaning | rungs |")
W("|---|---|---|")
for _l,_m,_r in (("X","exotic matter required",4),("S","semiclassical corrections",3),
                 ("IC","initial conditions",3),("U","unitarity",3),
                 ("NEC","null energy condition points",5),("L","locality",2),
                 ("SD","superdeterminism",2),("DNc","dynamical, continuous",3),
                 ("DNd","dynamical, discrete",3)):
    W(f"| **{_l}** | {_m} | {_r} |")
W("")
W("**4 · 3 · 3 · 3 · 5 · 2 · 2 · 3 · 3 = 19,440**, and the index holds **2,370** — 12.19% density.")
W("")
W("## What the companion prints")
W("")
W("| object | threshold | cells | reachable |")
W("|---|---|---|---|")
for _o,_t,_c,_r in (("classical black hole","none","2,370","1,410"),
                    ("Hawking-evaporating","NEC ≥ 1","2,196","1,410"),
                    ("Planck-scale wormhole","NEC ≥ 2","1,764","1,134"),
                    ("macroscopic wormhole","NEC ≥ 3","1,146","738"),
                    ("universal horizon","X ≥ 2","1,374","840"),
                    ("time machine","X = 3","558","360")):
    W(f"| {_o} | `{_t}` | {_c} | {_r} |")
W("")
W("**Twelve numbers, and one column is a second predicate on the same cells.** Differenced, the")
W("cells give NEC = 0 at 174, NEC = 1 at 432, NEC = 2 at 618, NEC ≥ 3 at 1,146. **All 174 cells at")
W("NEC = 0 are unreachable** — removing them removes no reachable cell — and **exactly 64% of NEC = 1")
W("and 64% of NEC = 2 cells are reachable**, 276 of 432 and 396 of 618.")
W("")
W("## Its defect, and the one constraint printed")
W("")
W("**E = 30, collapsing as 1 × 30** — one core cell repeated across the free coordinates — with the")
W("core at **(X = 0, U = 0, NEC = 3)**. At fifteen letters: 18,072 cells, **E = 816 = 1 × 816.**")
W("**Multiplicities 3, 5, 10, 30 at 4, 5, 7 and 9 coordinates**, and 5 is not a product of any two")
W("rung counts, so **the edge list constrains the free letters as well as the support.**")
W("")
W("**The constraint the companion prints**, at arity 3:")
W("")
W("> **NEC ≥ 3 ∧ X = 0 → U ≥ 1** — cells 2,370, E = 30, core 1")
W("")
W("with three variants: `NEC ≥ 3 → U ≥ 1` at arity 2 giving **E = 0**, and `NEC ≥ 3 ∧ U = 0 → X ≥ 1`")
W("and `NEC ≥ 3 → (IC ∨ U ∨ X)` both giving E = 30. **A jurisdicted forcing and an unjurisdicted")
W("disjunction give identical defects; arity 2 gives none.**")
W("")
W("## What is not printed, and what nine searches established")
W("")
W("**The edge list itself.** §5.7 of the companion says so outright. Nine searches were run against")
W("the twelve numbers; the best holds **cells exactly 2,370 at distance 29**, with the whole residual")
W("on the NEC interior — **NEC ≥ 2 sixteen too high, NEC ≥ 3 nine too low, missing in opposite")
W("directions.**")
W("")
W("**Eight alphabets were tried and none moved it**: simple implications, disjunctive heads,")
W("conjunctive bodies, all 47 single-rule edits, four alternative rung readings, two threshold")
W("semantics, seeding at NEC = 3, and weighted sums with gated deviations. **The rungs and the ≥")
W("reading are confirmed correct** — every alternative is two orders of magnitude worse.")
W("")
W("    **And the reachable column reduces to the same missing artefact.** Three local")
W("    readings of reachability give ~99% against a printed 60%; the companion's own")
W("    `here?` column says reachable means reachable FROM HERE, directed from one")
W("    position in a transition graph. **Both columns need the edge list.**")
W("")
W("---")
W("")
W("# V · THE INDEXES BUILT FROM IT")
W("")
W("Each of these exists because Λ exists — it indexes something Λ's cells have, or something the")
W("act of building Λ produced.")
W("")
W("## The electromagnetic quotient")
W("")
W("**Λ modulo the dipole selection rules** — Δℓ = ±1, ΔS = 0, parity. A quotient, not a subset:")
W("cells are identified when the rules cannot distinguish them.")
W("")
W("**Its E = 0 is VACUOUS** — §12.11.8 — because the image is a complete rectangle. **It closes")
W("because it is a box, not because the selection rules constrain it**, and that is the one closure")
W("in this work that certifies nothing.")
W("")
W("![**Figure 4.** The crossing. Within one atom a dipole-allowed transition is the LEAST likely to be followable; across the 118 elements it is the most. **The rule that forbids composition inside an atom is the rule that enables it between atoms.**](figures-compendia/fig-i4-crossing.png)")
W("")
W("**Its measured role is the crossing.** Within one element, EM-allowed transitions compose at")
W("**11.6%** against the forbidden **40.7%**. Across the 118 elements the order reverses — **89.7%")
W("against 77.9%.** *The rule that forbids composition inside an atom is the rule that enables it")
W("between atoms.*")
W("")
W("## The time index")
W("")
W("**Not a coordinate. The second column.** §12.11.0: composition IS the temporal order — a cell's")
W("source end is a before, its target end an after, and q is what changed between them.")
W("")
W("**An index has a time column exactly when its cells are moves.** Λ₈ 976/0, Λ₉ 1,654/1,169,")
W("Λ₁₀ 2,535/2,050 — and the periodic table and the calendar **cannot have one**, because a state")
W("cell has one position and there is nothing to compose.")
W("")
W("**What Λ lacks is not a clock but a denominator** — claims per session — which §12.11.1.1 now")
W("supplies. *A date must never enter Λ: a transition is a type, and types are not dated.*")
W("")
W("## The space index")
W("")
W("**The first column.** What the index holds, as against what it can compose. **Λ has no spatial")
W("coordinate**: n and e are shell numbers, not positions, and nothing in the eight is a place.")
W("")
W("**The nearest thing to a spatial reading is the observability one**: an observer's register is")
W("Λ-valued because observation IS an atomic state change, so an unregistered event is an")
W("admitted-and-absent cell and **E(local register) measures what is not yet real to that observer.**")
W("*That is a definition with a falsifiable consequence and it is not yet built.*")
W("")
W("## The languages")
W("")
W("**A language is a coordinate system; translation is re-coordinatisation; E is the cost.**")
W("")
W("| language | closure operator | delete | add |")
W("|---|---|---|---|")
W("| order | ℛ | restored | absorbed |")
W("| geometry | monotone polyhedron | restored | absorbed |")
W("| algebra / logic | ideal, Gröbner basis | still derivable | T·h enters the ideal |")
W("| analysis | coefficients of F | restored | absorbed |")
W("| information | description length | E_bits stays 0 | **grows** |")
W("| **statistics** | max-entropy on the marginals | restored | **grows** |")
W("| documentary | **none — no algorithm** | — | — |")
W("")
W("**Six agree on Λ at 976 and all ten pairs hold** — C(5,2), a complete graph, not a ladder.")
W("**Statistics was tested and qualifies with a caveat**: it recovers Λ at 976 and E = 0, but gives")
W("**E = 0 on the periodic table where ℛ gives 36** — *marginals cannot see a hole.* It agrees with")
W("the others only where there is nothing to disagree about.")
W("")
W("## The book's own indexes")
W("")
W("| index | coordinates | cells | E | what it holds |")
W("|---|---|---|---|---|")
W("| the audits | object<source<artefact<outside · what · how · depends | 21 | **16** | twenty-two audits |")
W("| the register | corroboration ≤ φ̂(repair) | 33 | **6** | the corrections |")
W("| Q | blocks · obstacle · cost · depends | 8 | **5** | what the book does not know |")
W("| the protocols | trigger · object · failure · earned | 19 | **105** | twenty-four protocols |")
W("| the constraints | parents · form · carried · source · role | 15 | **21 / E₄ 6** | every constraint in the book |")
W("| the mathematics | kind · language · status · verification · precedent | 27 | **0** | fibred, sixteen fibres |")
W("| the numbers | fibre · kind · role | — | **40** | every figure the book prints |")
W(f"| **the channel survey** | **Z · core charge · ℓ** | **{_NGRID:,}** | **{_NGRID-_NHELD:,}** | **{_NCH} Rydberg channels across {_NHELD} cells** |")
W("")
W("**These exist because the book exists, not because Λ does** — but they are built by Λ's method,")
W("and the audits index's two frontier cells are the same pair ℛ₄ refuses at §14.5.6, reached by two")
W("computations sharing no code.")

# ------------------------------------------- the spectra index, its own section

# --------------------------------------------- redundancy under R
W("")
W("---")
W("")
W("## How much of an index determines the rest")
W("")
W("**Remove cells at random and ask whether ℛ puts them back.** The largest fraction "
  "removable with exact recovery is a property of the index, and it had never been "
  "measured for any of these.")
W("")
W("| index | dimension | envelopes | coupling | **redundancy** |")
W("|---|---|---|---|---|")
W("| Λ | 8 | 56 | 29% | **61%** |")
W("| Λ_spectra^obs | 3 | 6 | 17% | **20%** |")
W("| a box ordering | 3 | 6 | 50% | 0% |")
W("| Janet | 2 | 2 | 50% | 0% |")
W("| the periodic table | 2 | 2 | 0% | 0% |")
W("| the calendar | 2 | 2 | 0% | 0% |")
W("")
W("**Coupling does not explain it.** The fraction of coordinate pairs whose envelope "
  "actually constrains gives **r² = 0.002, p = 0.94** against redundancy: Janet and the "
  "box ordering both couple at 50% and recover nothing, while Λ_spectra^obs couples at 17% "
  "and recovers a fifth. *That conjecture was stated before the measurement and is wrong.*")
W("")
W("**DIMENSION explains it, and the projection test shows so on a single object.** Λ "
  "restricted to its own first d coordinates, constraints unchanged:")
W("")
W("        d = 8   61%        d = 5   30%")
W("        d = 7   30%        d = 4    5%")
W("        d = 6   30%        d = 3    0%")
W("")
W("ℛ works on **pairwise** envelopes, so an index of dimension d carries d(d−1) of them — "
  "**56 for Λ, 6 for Λ_spectra^obs, 2 for a plane.** With two envelopes there is almost "
  "nothing to reconstruct from, and that is what the operator is rather than a fact about "
  "any subject.")
W("")
W("**But only INDEPENDENT coordinates count.** Adding the electron count Nₑ = Z − c + 1 to "
  "Λ_spectra^obs — a function of two coordinates it already has — takes redundancy from **20% "
  "to 0%**, while doubling the envelopes and raising coupling from 17% to 33%. *A derived "
  "coordinate adds no information and obliges ℛ to reproduce it exactly, so recovery "
  "becomes strictly harder.* Registers 1119–1122.")
W("")
W("")
W("---")
W("")
W("## The channel survey — Λ_spectra^obs")
W("")
W(f"**Coordinates: Z · core charge · ℓ.** Each cell is a Rydberg channel — a fixed parent "
  f"core, a fixed ℓ, n running. The compendium holds **{_NCH} channels across {_NHELD} of "
  f"the survey's {_NGRID:,} cells**.")
W("")
W("**This is not the coordinate index, and the two were once both called Λ_spectra.** "
  "Λ_spectra proper is the four-coordinate index (Z, charge, ℓ, 2S+1) at 104,832 cells "
  "with **E = 0** — see *Λ_spectra — the channel index*, below. Λ_spectra^obs is the "
  "three-coordinate **survey of what has been measured**. The column beside each cap "
  "below is grid minus held — the **unwitnessed** count — and *not* a closure defect: "
  "reading it as E would say the index is open when it is a fixed point. R 1657.")
W("")
W("**Where its alphabets come from, and why that differs from Λ.** Λ's coordinates are bounded "
  "by the physics — ℓ < n, k ≤ 4ℓ+2 — and all 118 ground configurations are known within its "
  "caps, so Λ is complete at 976 cells. **Λ_spectra^obs is not.** Rydberg series are unbounded in n "
  "and ℓ runs to n−1, so the index is **infinite unless capped**, and every cap is a decision. "
  "Three defensible ones give:")
W("")
W("| alphabet | grid | unwitnessed |")
W("|---|---|---|")
W(f"| as measured — charge {_CS} | {_NGRID:,} | {_NGRID-_NHELD:,} |")
W("| charge 1 to Z−1 over the elements held | 4,376 | 4,148 |")
W("| all 118 elements, ℓ 0–7 | 55,224 | 54,996 |")
W("")
W("**All three grids are closed** — each is a fixed point of ℛ, verified by double "
  "projection. The number beside each is what has *not* been measured under that cap, "
  "so it is a result about the cap and about the state of the literature; it is never "
  "a closure defect. *Registers 959–962, 1657.*")
W("")
W("**What the index says about cells it does not hold.** Every cell carries a grade, and the "
  "grade records how far the statement travelled:")
W("")
W("| grade | cells | what it means |")
W("|---|---|---|")
W(f"| MEASURED | 205 | a defect computed from levels |")
W(f"| BRACKETED | 5 | bounded above and below by DIFFERENT mechanisms |")
W(f"| BOUNDED | 42 | bounded on one side, adjacent to a measurement |")
W(f"| PROPAGATED | 954 | a bound inherited through a chain of 2 to 13 steps |")
W(f"| FORMAL | 73 | the only bound is one a mechanism already implies |")
W(f"| UNCONSTRAINED | 33 | **no statement at all** |")
W("")
W("**97.5% of the index carries a defensible statement.** The three relations that propagate "
  "are **P.lcollapse** along ℓ, **P.iso** along an isoelectronic sequence, and **P.charge** "
  "along the charge states of one element. *Registers 963–965, 981.*")
W("")
W("![**Figure 5.** Λ_spectra^obs drawn as a lattice — element across, ℓ into the page, ionisation "
  "stage up. Green is measured, orange bounded from two sides by different mechanisms, gold from "
  "one; the faint markers are cells the structure admits and nobody has measured. **The occupied "
  "region is a wedge at low Z and low ℓ**, which is where long Rydberg series have been "
  "tabulated — and the emptiness above it is the shape of what an index says it does not "
  "know.](figures-compendia/fig-spectra-lattice.png)")
W("")
W("**And the last 33 are of three kinds, only two of which a capture can fix.** P I, Cd I, "
  "Ti II and Ar I want longer captures. **Sc I and Ti I have no Rydberg series at all** — their "
  "levels are 3d.4s.4p and 3d².4s mixtures with no n running, so fourteen cells are unreachable "
  "by any capture. *Register 983.* **The ceiling is 98.6%, not 100%, and that is a fact about "
  "the open-shell transition metals rather than about the collection.**")
W("")
W("")
W("---")
W("")
W("# VI · THE INDEXES NAMED AND NOT BUILT")
W("")
W("**§29.1: the absence is not evidence.** These were named in the course of the work and no index")
W("exists for them. Saying so is the point of this section.")
W("")
W("**Sound.** Phonon modes are discrete and indexable — ω, lattice momentum, polarisation, occupation")
W("— but they index a **material**, not an atom. **No such index is built here**, and it would sit")
W("beside Λ rather than inside it, since Λ has no coordinate a lattice vibration could occupy.")
W("")
W("**Frequency.** A transition's frequency is ΔE/h, and ΔE is not a coordinate of Λ — **§6.2 gives")
W("first ionisation energies to the bracket and the bracket REFUSES**, at Be→B, N→O, Mg→Al and P→S,")
W("four steps of twelve. *That refusal is the book's most direct statement about frequency: the")
W("coordinates cannot bracket it, and where they refuse a mechanism is entering.*")
W("")
W("**The multiverse.** §32.6.1 places this outside all four of the book's indexes, with the")
W("destination coordinate, because §E.1.4 shows **the open set cannot express an unclosable question.**")
W("*It is not an index that has not been built. It is the shape of a question this work cannot pose*")
W("— and Theorem 12.1 is why: Λ's order structure contributes nothing predictively beyond what the")
W("coordinates supply, and its coordinates are n, ℓ, k, q, e, f, g, 2S.")
W("")
W("---")
W("")
W("# VII · THE FULL TABLES")
W("")
W("**Every index small enough to print, printed.** The tower above Λ₈ runs to 64,290 cells at Λ₁₃")
W("and is given by its construction instead; the violation index has no cells to give.")
W("")
W("## Λ₈ — all 976 cells")
W("")
W("| # | n | ℓ | k | q | e | f | g | 2S |")
W("|---|---|---|---|---|---|---|---|---|")
for _i, _c in enumerate(sorted(M["L8"]), 1):
    W("| " + str(_i) + " | " + " | ".join(str(_v) for _v in _c) + " |")
W("")
W("**976 rows. F(1) = 976, F(−1) = 2, E = 0, density 0.1412 of a box of 6,912.**")
W("")
W("## The periodic table — all 90 cells, (period, group)")
W("")
W("| period | groups occupied |")
W("|---|---|")
for _p in sorted(M["TAB"]):
    W(f"| {_p} | " + ", ".join(str(_g) for _g in M["TAB"][_p]) + " |")
W("")
W("**90 cells in a box of 126. E = 36** — and the 36 are the cells the coordinates admit and no")
W("element occupies, which must be supplied from outside.")
W("")
W("## Janet — all 118, (n+ℓ, Z)")
W("")
W("| n+ℓ | atomic numbers |")
W("|---|---|")
for _k in sorted(M["JAN"]):
    _v = M["JAN"][_k]
    W(f"| {_k} | {_v[0]}–{_v[-1]} ({len(_v)}) |")
W("")
W("**118 cells, E = 0.** The same 118 elements as the table above, reordered by n+ℓ.")
W("")
W("## The calendar — 365 cells, (month, day)")
W("")
W("| month | days | month | days |")
W("|---|---|---|---|")
_D = [31,28,31,30,31,30,31,31,30,31,30,31]
_MN = ["January","February","March","April","May","June","July","August",
       "September","October","November","December"]
for _i in range(6):
    W(f"| {_MN[_i]} | {_D[_i]} | {_MN[_i+6]} | {_D[_i+6]} |")
W("")
W("**365 cells in a box of 372. E = 7** — February's missing 30th and 31st, and the four thirty-day")
W("months' 31sts. **365 = 5 · 73, and 73 exceeds every rung**, so it is genuinely constrained.")
W("")
W("## A box ordering — all 35, l ≥ w ≥ h")
W("")
W("| l ≥ w ≥ h |")
W("|---|")
_row = []
for _c in sorted(M["BOX"]):
    _row.append("·".join(str(_v) for _v in _c))
for _i in range(0, len(_row), 7):
    W("| " + "  ".join(_row[_i:_i+7]) + " |")
W("")
W("**35 cells in a box of 125, E = 0.** 35 = 5 · 7 and 7 exceeds the rung of 5: a real constraint.")
W("")
W("---")
W("")
W("# VIII · WHAT EACH INDEX IS, AND WHAT ONLY IT CONTRIBUTES")
W("")
W("**Λ is the only index here built from physics.** The rest are built from Λ, from the "
  "act of building Λ, or from drawing the same subject another way. *This section states "
  "for each one: what it is, where it comes from in the published record, and the one "
  "thing it contributes to the atomic index that no other index can.*")
W("")
W("---")
W("")

W("## Λ — the atomic index")
W("")
W("**What it is.** Eight integer coordinates (n, ℓ, k, q, e, f, g, 2S) under eight "
  "inequalities, 976 cells, E = 0.")
W("")
W("**Where it comes from.** The constraints are not this work's: ℓ ≤ n−1 is the "
  "hydrogen solution (Bohr 1913; Schrödinger 1926); k ≤ 4ℓ+2 is Stoner's subshell "
  "capacity (1924) made exclusive by Pauli (1925); 2S ≤ k is Pauli with Hund's first "
  "rule (1925). **Λ assembles them; it introduces none.**")
W("")
W("**What only it contributes.** *The transfer.* Λ is the only index here whose cells "
  "are MOVES rather than positions — a cell carries a source subshell, a target "
  "subshell and a count transferred. **Everything about composition, time columns and "
  "categories follows from that and from nothing else in this compendium.**")
W("")

W("## The tower Λ₈…Λ₁₃")
W("")
W("**What it is.** Λ with the coupling quantum numbers adjoined one at a time — "
  "seniority, the core J, K, then J. Cell counts 976, 1654, 2535, 13585, 70905, "
  "199130, E = 0 at every stage.")
W("")
W("**Where it comes from.** Each axis is Racah or Condon & Shortley: seniority is "
  "Racah, *Theory of complex spectra III*, Phys. Rev. **63** (1943) 367–382; the core J "
  "and the recoupling coefficients are Racah, Phys. Rev. **62** (1942) 438–462; the "
  "jK and LK schemes are Condon & Shortley (1935), ch. X.")
W("")
W("**What only it contributes.** *The price of an axis.* The tower is the only "
  "construction here that adds one coordinate at a time and measures what each costs "
  "and buys — **cycle rank, composability, exactness, and the point at which the tree "
  "becomes a graph.** No single index can show that; it takes a sequence.")
W("")

W("## The periodic table — (period, group)")
W("")
W("**What it is.** 90 cells in a box of 126, E = **36**.")
W("")
W("**Where it comes from.** Mendeleev, *Über die Beziehungen der Eigenschaften zu den "
  "Atomgewichten der Elemente*, Z. Chem. **12** (1869) 405–406. At least a thousand "
  "periodic systems have been published since (van Spronsen; Scerri, *A Tale of Seven "
  "Scientists*, 2016).")
W("")
W("**What only it contributes.** *The control.* It is the one index whose coordinates "
  "were fixed by other people for other reasons, long before this work, and which "
  "nonetheless supplies **118 elements and 18,288 constraint tests with zero failures.** "
  "**An index built by the author cannot be a control; this one can.**")
W("")

W("## Janet's left-step table — (n+ℓ, Z)")
W("")
W("**What it is.** The same 118 elements, ordered on n+ℓ. 118 cells in a box of 944, "
  "E = **0**.")
W("")
W("**Where it comes from.** Charles Janet, *Considérations sur la structure du noyau de "
  "l'atome*, Beauvais (1929), with the table first published in **1928**. *Janet "
  "recognised the (n+ℓ) rule before Madelung, who arrived at it around 1926 and did not "
  "publish until 1936.* The shell-length sequence 2, 8, 8, 18, 18, 32, 32 follows from "
  "the rule by the Klechkovski–Hakala formulas.")
W("")
W("**What only it contributes.** *That E is coordinate-relative, demonstrated on one "
  "subject rather than argued.* The periodic table and Janet index THE SAME 118 "
  "elements and give E = 36 and E = 0. **No pair of indexes anywhere else in this work "
  "makes that point as cleanly, because no other pair shares its subject exactly.**")
W("")
W("**And an open problem sits underneath it.** *Why* the n+ℓ ordering holds is "
  "unresolved — Löwdin's challenge, still open; see Allen & Knight, *The Löwdin "
  "challenge: origin of the n+l, n (Madelung) rule*, Int. J. Quantum Chem. **90** "
  "(2003) 80–88. **This work uses the ordering and does not explain it**, and the "
  "orbital-collapse result (registers 1187–1190) is a measurement against Janet's "
  "boundaries, not a derivation of them.")
W("")

W("## The nuclide chart — (Z, N)")
W("")
W("**What it is.** The measured nuclides indexed by proton and neutron count, "
  "E = **9**.")
W("")
W("**Where it comes from.** The chart is Segrè's, in use since the 1940s; the values "
  "are the AME2020 evaluation.")
W("")
W("**What only it contributes.** *A defect whose cells are identifiable physics.* The "
  "nine cells are the mass formula's pairing and clustering terms. **It is the only "
  "index here where E > 0 and every missing cell can be named**, which is what makes "
  "the defect a measurement rather than a score.")
W("")

W("## The calendar — (month, day)")
W("")
W("**What it is.** 365 cells in a box of 372, E = **7**.")
W("")
W("**Where it comes from.** The Gregorian reform of 1582, on the Julian arrangement of "
  "46 BC. *The month lengths are a political inheritance, not a natural one.*")
W("")
W("**What only it contributes.** *A subject with no physics in it at all.* The calendar "
  "shows the operator working on an object whose constraints are entirely conventional, "
  "**and 365 = 5 · 73 with E = 7 is the price of keeping January first.** No other "
  "index here separates the method from the physics so completely.")
W("")

W("## The box ordering and the chessboard")
W("")
W("**What they are.** ℓ ≥ w ≥ h over five values: 35 cells in 125, E = 0. And "
  "(rank, file): 64 cells in 64, E = 0.")
W("")
W("**What only they contribute.** *The floor and the ceiling.* The chessboard is a full "
  "product — E = 0 because there is no constraint at all. The box ordering is a genuine "
  "constraint that still closes. **Between them they show that E = 0 carries "
  "information only when the ambient box exceeds the cells**, which is why the "
  "compendium reports box alongside every defect.")
W("")

W("## The electromagnetic quotient")
W("")
W("**What it is.** Λ₉ under the dipole selection rules: |Δℓ| = 1 and ΔS = 0.")
W("")
W("**Where it comes from.** The parity rule is Laporte, Z. Phys. **23** (1924) 135; "
  "the spin rule is Russell & Saunders, Astrophys. J. **61** (1925) 38; both have their "
  "group-theoretic ground in Wigner, Z. Phys. **43** (1927) 624.")
W("")
W("**What only it contributes.** *That a selection rule is a QUOTIENT and not an "
  "extension.* Adjoining the multipole and ΔS as coordinates gives E = 3; taking the "
  "image gives E = 0. **It is the only index here that demonstrates the difference "
  "between adding a coordinate and dividing by one.**")
W("")

W("## Λ_spectra — the channel index")
W("")
W("**What it is.** (Z, charge, ℓ, 2S+1) over 104,832 cells, with a defect for each.")
W("")
W("**Where it comes from.** Quantum defect theory is Seaton, MNRAS **118** (1958) "
  "504–518, and Rep. Prog. Phys. **46** (1983) 167–257. *A published survey of the "
  "same object exists*: Theodosiou, Inokuti & Manson, At. Data Nucl. Data Tables **35** "
  "(1986) 473–486, Hartree–Slater, for all ionisation stages of all ions with Z ≤ 50.")
W("")
W("**What only it contributes.** *Values.* Every other index here holds cells and asks "
  "whether they close. **Λ_spectra holds cells that carry NUMBERS**, which is why it "
  "is the only index on which the Method equation's metric half — E_W — has anything to "
  "measure at all (registers 1196–1199).")
W("")

W("## The violation index")
W("")
W("**What it is.** The companion paper's object over nine and fifteen letters, with a "
  "core of three conditions whose joint failure is irreducible.")
W("")
W("**Where it comes from.** The conditions are physics — the null energy condition "
  "(Penrose 1965), ghost states (Pais & Uhlenbeck 1950), the equations of motion. *The "
  "core is a MINIMAL UNSATISFIABLE SUBSET* in the sense of Chinneck & Dravnieks, "
  "*Locating minimal infeasible constraint sets in linear programs*, ORSA J. Comput. "
  "**3** (1991) 157–168.")
W("")
W("**What only it contributes.** *An index this work reasons about without holding.* "
  "Its cells are not printed anywhere. **It is the only test of whether the method "
  "says anything when the object is out of reach**, and the answer is that it locates "
  "a three-condition core from published summary numbers alone.")
W("")

W("## Λ_phys — the parameter index")
W("")
W("**What it is.** Every number the work takes from physics, on four coordinates — "
  "kind (exact → fitted), source (mathematics → this work), domain (universal → one "
  "species), and how many registered objects rest on it. **22 parameters.**")
W("")
W("**Where it comes from.** The parameters are Rydberg 1890, Bohr 1913, Stoner 1924, "
  "Pauli 1925, Hund 1925, Fermi 1928, Hartree 1928, Janet 1928, Mayer & Mayer 1933, "
  "Goeppert-Mayer 1941, Seaton 1958, Edlén 1964, Griffin, Andrew & Cowan 1969, "
  "CODATA 2018 — and eight numbers fitted here. *The Physics Compendium holds them in "
  "full, each with a definition, a dated source and a failure mode.*")
W("")
W("**What only it contributes.** *Where the work would break first.* Every other index "
  "here asks whether a set of cells closes. **Λ_phys asks what the whole construction "
  "rests on, and the answer is a shape:** eight of the twenty-two parameters are this "
  "work's own, **none of them is universal**, seven of the eight hold only in a region "
  "or for one species — and the three carrying the most objects are all READ from "
  "published tables rather than fitted: the ionisation limit (25 objects), the aufbau "
  "ordering (19), the Janet block boundary (15).")
W("")
W("**And three of its failure modes are MEASURED rather than anticipated** — Seaton's "
  "ratio at 1.25 where the dipole term gives 1.00, the Thomas–Fermi exponent rising "
  "from 0.84 to 1.52 with charge against a single fitted 0.494, and the exchange "
  "coefficient whose fitted sign is opposite to the measured one.")
W("")

W("## The languages")
W("")
W("**What they are.** Six readings of one index — order, analysis, algebra, geometry, "
  "information, statistics — with documentary as a seventh that has no operator.")
W("")
W("**Where they come from.** Each operator is standard in its own field: closure from "
  "Moore (1910), max-entropy on marginals from Deming & Stephan (1940) and Csiszár "
  "(1975), conditional independence from Dawid (1979).")
W("")
W("**What only they contribute.** *That translation is re-coordinatisation and E is "
  "its cost.* **And the agreement theorem: E(X) = 0 if and only if the languages "
  "agree** — six indexes, three operators, no exception (register 1176).")
W("")

W("## The book's own indexes")
W("")
W("**What they are.** The book at chapter resolution (E = 578) and at part resolution "
  "(E = 0); the register (E = 6 at 68.8% density); the reference index (38 cells, "
  "E = 0, and not a tree).")
W("")
W("**What only they contribute.** *The method self-applied.* **This is the only place "
  "where E > 0 is a theorem about SHAPE rather than a gap in collection** — the book's "
  "chapters do not close because chapters are not a coordinate system, and saying so "
  "with a number is the point.")
W("")
W("---")
W("")
W("## The one-line summary")
W("")
W("| index | the one thing only it gives |")
W("|---|---|")
W("| **Λ** | the transfer — cells that are moves |")
W("| **the tower** | the price of an axis, measured one at a time |")
W("| **the periodic table** | a control the author did not build |")
W("| **Janet** | E is coordinate-relative, on one subject |")
W("| **the nuclide chart** | a defect whose every cell is nameable physics |")
W("| **the calendar** | a subject with no physics in it |")
W("| **box and chessboard** | the floor and ceiling of what E = 0 means |")
W("| **the EM quotient** | quotient versus extension |")
W("| **Λ_spectra** | values, so the metric defect has something to measure |")
W("| **the violation index** | reasoning about an index without holding it |")
W("| **Λ_phys** | where the work would break first |")
W("| **the languages** | translation as re-coordinatisation |")
W("| **the book's own** | E > 0 as a theorem about shape |")
W("")
W("**Λ is the only one built from physics. The rest are built from Λ, from the act of "
  "building Λ, or from drawing the same subject another way — and that is the claim: "
  "an index is a coordinate system, and the coordinates come from the subject or from "
  "nowhere.**")
W("")

# --- hand-authored tail, appended rather than generated (registers 1373, 1386, 1388) ---
# The generator does not write this region. It is declared here so that
# roundtrip.py's DECLARE question has an answer, and so a rebuild cannot
# silently discard it. If the tail is missing the generator REFUSES:
# a generator that cannot produce its whole output must not produce part of it.
import os as _os, sys as _sys
def _tail(_name):
    _p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), _name)
    if not _os.path.exists(_p):
        _sys.stderr.write(f"REFUSING: {_name} is absent; the output would be incomplete.\n")
        _sys.exit(2)
    return open(_p, encoding="utf-8").read()

print("\n".join(L) + "\n" + _tail("INDICES-TAIL.md"), end="")
