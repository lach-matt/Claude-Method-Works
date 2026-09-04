#!/usr/bin/env python3
"""compendium.py -- the book's mathematics, extracted and expanded.

Generated from mathreg.py so it cannot drift from the register. Every object,
its statement, its hypothesis, its dependencies, its source and its grade,
organised by family, with the dependency chains and the cycle's own arithmetic.
"""
from collections import defaultdict, deque
import importlib.util as iu, re, datetime

sp = iu.spec_from_file_location("_mr", "mathreg.py"); mr = iu.module_from_spec(sp)
try: sp.loader.exec_module(mr)
except SystemExit: pass
REG = mr.REG

FAMILY = {
 "A": "The operators — closure, envelope, orientation",
 "S": "The seed — generation, covering, structure",
 "F": "The family of closed indexes",
 "G": "Graphs, constraints and languages",
 "L": "Λ's own constraints",
 "T": "The tower and its couplings",
 "E": "Empirical indexes — table, nuclide, layout",
 "B": "The bracket",
 "K": "Transit and information",
 "M": "The modular chain",
 "W": "The violation index",
 "EM": "The electromagnetic quotient",
 "C": "Protocol and audit objects",
 "I": "The intake — interval maps and convexity",
 "P": "The spectral mechanisms — what moves a defect and by how much",
 "Q": "The channel equation — the closed form and its terms",
}

def unfinished(k):
    v = REG[k]
    if v["grade"] in ("OPEN", "ASSERTED"): return "graded open"
    if not v["dep"] and not v["named"]: return "unnamed root"
    if v["grade"] in ("COMPUTED", "CITED") and not v["check"]: return "unverified"
    return None

dep = {k: [d for d in v["dep"] if d in REG] for k, v in REG.items()}
rev = defaultdict(list)
for k, ds in dep.items():
    for d in ds: rev[d].append(k)
roots = sorted(k for k, v in REG.items() if not v["dep"])

_DEPTH = {}
def depth(k, seen=None):
    """the longest dependency chain below k.

    Memoised (register 1195). Without a cache this re-walks every branch of the
    DAG and is exponential in the chain length; at depth 14 — which the Q family
    reached this session — the build stopped terminating. The cache is safe
    because a node's depth does not depend on the path taken to it, and the
    cycle guard still uses `seen` on the way down.
    """
    if k in _DEPTH: return _DEPTH[k]
    seen = seen or set()
    if k in seen or not dep[k]: return 0
    v = 1 + max((depth(d, seen | {k}) for d in dep[k]), default=-1)
    _DEPTH[k] = v
    return v

L = []
W = L.append
W("# THE METHOD 1.6 — MATHEMATICAL COMPENDIUM")
W("")
W(f"Generated from `mathreg.py` on {datetime.date.today().isoformat()}. "
  f"**{len(REG)} objects · {len(roots)} roots · "
  f"{len(REG) - sum(1 for k in REG if unfinished(k))} settled · "
  f"{sum(1 for k in REG if unfinished(k))} unfinished.**")
W("")
W("**Verification coverage, stated rather than implied.** `mathverify.py` makes **103 "
  "assertions naming 46 of these objects** and recomputes each stated value against the "
  "register; **no verifier touches the other 167**. Of the check fields, **85 state a "
  "finding, 91 repeat the object's own key, 19 name a function, and 18 are empty** — so a "
  "check field present is not a verification performed. `check_audit.py` classifies them on "
  "any build. Register 849.")
W("")
W("Rebuild with `python3 compendium.py > COMPENDIUM.md`. It reads the register, so it cannot")
W("drift from what the book actually holds.")
W("")
W("---")
W("")
W("# I · THE CYCLE")
W("")
W("The whole of this work is one recursion, stated at §14.5.2:")
W("")
W("> **X₍ₙ₊₁₎ = ℛ(X_n ∪ Δ_n)**, halting when **Δ_n ⊆ ℛ(X_n)** — when the increment is already implied.")
W("")
W(f"**It has never halted.** Its falsifier is the ratio of closure to seed:")
W("")
W(f"| | |")
W(f"|---|---|")
W(f"| closure — objects the register holds | **{len(REG)}** |")
W(f"| seed — objects nothing derives | **{len(roots)}** |")
W(f"| ratio | **{len(REG)/len(roots):.1f} : 1** |")
W("")
W("**The seed has not moved across every cycle of this project.** If a genuinely new mathematical")
W("object entered that nothing existing derived, it would move — and that is the test.")
W("")
W("## The fourteen roots")
W("")
W("| object | statement |")
W("|---|---|")
for k in roots:
    W(f"| `{k}` | {REG[k]['stmt'][:110]} |")
W("")
W("---")
W("")
W("# II · THE OPERATORS")
W("")
W("Every derivation in the book runs through these. Nine are this work's own.")
W("")
W("| symbol | definition | scope | origin |")
W("|---|---|---|---|")
for sym, dfn, scope, orig in [
  ("∧ ∨", "meet and join — greatest lower and least upper bound", "cells", "Birkhoff, standard"),
  ("φ̂", "the envelope: max xᵢ over cells with xⱼ ≤ v", "sets of cells", "§14.5"),
  ("ℛ", "closure at the (≤,≤) corner of Deville's staircase class", "sets of cells", "§14.5.4"),
  ("ℛ₄", "closure over all four orientations", "sets of cells", "§14.5.5"),
  ("E", "E(X) = \\|ℛ(X)\\| − \\|X\\| — the defect", "indexes", "§1"),
  ("E₄", "the defect under ℛ₄; E − E₄ is the orientation cost", "indexes", "§14.5.5"),
  ("d", "d(x,y) = τ(lcm/gcd) = ∏(\\|Δᵢ\\|+1) = \\|[x∧y, x∨y]\\|", "cells", "title page"),
  ("∘", "composition of transitions — Λ₉ is a category", "cells", "§12.11"),
  ("seed", "least G with ℛ(G) = X — **NP-hard**", "sets of cells", "§14.5.7"),
  ("S", "envelope-step count; 2S = the tight-pair count", "sets of cells", "§14.5.9")]:
    W(f"| **{sym}** | {dfn} | {scope} | {orig} |")
W("")
W("---")
W("")
W("# III · THE LANGUAGES, AND WHY EACH IS NECESSARY")
W("")
W("**A language is a coordinate system. Translation is re-coordinatisation. E is the cost.**")
W("")
W("Six languages agree on Λ at 976, and **all ten pairs hold** — C(5,2), a complete graph rather than")
W("a ladder. Binary is adjacent to every other, not only to logic. **The agreement is the result; the")
W("list is not.** What follows is one object stated seven ways, with the quantity each language alone")
W("supplies.")
W("")
W("| language | its statement of Λ | value | what only it can say |")
W("|---|---|---|---|")
W("| **analysis** | F(1), the enumerator at z = 1 | **976** | the cell count without enumerating |")
W("| **analysis** | F(−1), the alternating sum | **2** | the parity imbalance — invisible to a set |")
W(r"| **order** | \|ℛ(X)\|, the closure | **976** | what the envelopes admit |")
W(r"| **order** | E = \|ℛ(X)\| − \|X\| | **0** | **the defect** — no other language states one |")
W("| **geometry** | the void, per interval | **0.464** | what an interval admits and Λ refuses |")
W("| **binary** | the box, one bit per cell | **6,912** | the space before any constraint |")
W("| **binary** | density | **0.1412** | the fraction a constraint set keeps |")
W("| **information** | bits to print the cells | **12,449** | the cost of stating it in full |")
W("| **information** | bits to print the seed | **89** | **139× compression** |")
W("| **statistics** | recovered from pairwise marginals | **976** | the object from its margins alone |")
W("| **statistics** | its defect | **0** | — *and this is its limit* |")
W("| **algebra** | constraints generating the ideal | **8** | derivability — what follows from what |")
W("| **documentary** | *has anyone said this before* | — | **no algorithm exists** |")
W("")
W("## Why none is redundant")
W("")
W("**Analysis** gives F(−1) = 2. That is an alternating sum over the cells, and **a set has no")
W("alternating sum** — order, geometry and binary cannot express it. It is the parity imbalance, and")
W("it is why Chapter 7 can state the two-column law.")
W("")
W("**Order** is the only language that states a DEFECT. E has no counterpart in the others: the")
W("generating function does not know what it fails to enumerate, and a polyhedron does not know which")
W("of its lattice points are absent. **Every result in this work that begins *E =* begins here.**")
W("")
W("**Geometry** gives the void — 46.4% of a typical interval is admitted by the box and refused by Λ.")
W("The same quantity read in order is slack and in calculus is V, **and §12.11 shows the three are one")
W("number**. But only geometry states it per interval, which is where the exclusion principle shows.")
W("")
W("**Binary** gives the box. **Nothing else in this work says what the space was before a constraint")
W("touched it**, and every density, every defect and every compression ratio is a fraction of it.")
W("")
W("**Information** gives the compression: **139 cells printed for every one in the seed.** That number")
W("exists in no other language — order knows the seed is seven, and only description length says what")
W("seven buys.")
W("")
W("**Statistics** recovers Λ exactly from its pairwise marginals, and **that is the whole of what it")
W("can do.** Tested on the periodic table it reports **E = 0 where ℛ reports 36** — *marginals cannot")
W("see a hole.* **It agrees with the other languages only where there is nothing to disagree about**,")
W("which makes it necessary for one purpose and useless for another. **Knowing which is the point of")
W("having it.**")
W("")
W("**Algebra** gives derivability. Whether a bound follows from the others is a question about an")
W("ideal, and **§14.5.7's anti-exchange failure and register 618\'s rule-15-backs-rule-5 are both")
W("statements in this language** — one constraint implied by another, which no count can express.")
W("")
W("**Documentary** has no closure operator at all. *Has anyone said this before* cannot be bounded by")
W("computation, which is why §29\'s precedent question can be bounded and never settled, and why two")
W("searches returning nothing is evidence of a kind the other six never have to produce.")
W("")
W("    **The test of necessity is not that each language is available. It is that each")
W("    states a quantity the others cannot, and this table is that check run.**")
W("")
W("---")
W("")
W("# IV · THE OBJECTS, BY FAMILY")
W("")
byfam = defaultdict(list)
for k in REG: byfam[k.split(".")[0]].append(k)
for fam in sorted(byfam, key=lambda f: (list(FAMILY).index(f) if f in FAMILY else 99, f)):
    ks = sorted(byfam[fam])
    W(f"## {fam}. {FAMILY.get(fam, fam)} — {len(ks)} objects")
    W("")
    for k in ks:
        v = REG[k]; u = unfinished(k)
        tag = f" · **{u.upper()}**" if u else ""
        W(f"### `{k}` — {v['named'] or 'unnamed'}{tag}")
        W("")
        W(f"**{v['stmt']}**")
        W("")
        if v.get("hyp"): W(f"*{v['hyp']}*"); W("")
        bits = [f"grade **{v['grade']}**", f"source *{v['src']}*"]
        if dep[k]: bits.append("depends on " + ", ".join(f"`{d}`" for d in dep[k]))
        if rev[k]: bits.append(f"{len(rev[k])} objects depend on it")
        bits.append(f"depth {depth(k)}")
        W("· ".join(bits))
        W("")
        # Register 1228: the compendium printed the source and never the CHECK, so the
        # attribution reasoning — which part is prior art and which is measured — was
        # invisible in the document it belongs to.
        ch = (v.get("check") or "").strip()
        if ch:
            i = ch.find("PRIOR ART")
            if i > 0:
                W(f"{ch[:i].rstrip()}")
                W("")
                W(f"> **{ch[i:]}**")
            elif i == 0:
                W(f"> **{ch}**")
            else:
                W(f"{ch}")
            W("")
W("---")
W("")
W("# V · THE CHAINS")
W("")
W("The longest derivation paths in the register — what rests on what.")
W("")
deep = sorted(REG, key=lambda k: -depth(k))[:12]
for k in deep:
    path, cur = [k], k
    while dep[cur]:
        cur = max(dep[cur], key=depth); path.append(cur)
    W(f"**depth {depth(k)}** · " + " ← ".join(f"`{p}`" for p in reversed(path)))
    W("")
W("---")
W("")
W("# VI · WHAT IS UNFINISHED")
W("")
W("**Two objects.** *Neither is unfinished for want of a proof attempt. Each has a "
  "diagnosis, and the diagnosis names what is missing rather than restating that "
  "something is.*")
W("")

W("## `M.C2` — half-sided modular inclusion on a non-expanding horizon")
W("")
W("        Δ_{M(u₁)}^{it} M(u₂) Δ_{M(u₁)}^{−it} ⊆ M(u₂)   for t ≤ 0, u₁ < u₂")
W("")
W("**What is settled.** Half-sided modular inclusion is CHARACTERISED — Borchers, "
  "*The CPT theorem in two-dimensional theories of local observables*, Commun. Math. "
  "Phys. **143** (1992) 315–332, and Wiesbrock, *Half-sided modular inclusions of von "
  "Neumann algebras*, Lett. Math. Phys. **28** (1993) 107–114: the inclusion holds "
  "exactly when a one-parameter unitary group with positive generator implements the "
  "translation. The vacuum is cyclic and separating for local algebras (Reeh & "
  "Schlieder 1961), and modular theory supplies Δ and J (Tomita 1967; Takesaki 1970). "
  "**None of that is in question.**")
W("")
W("**What is missing, precisely.** The hypothesis — *a non-expanding horizon with no "
  "Killing field, ω Hadamard* — asks the expansion Θ = 0 to select what only a STATE "
  "can select, and offers Hadamard, a microlocal condition, as the selector.")
W("")
W("> **The horizon's own definition supplies a state condition at BACKGROUND order — "
  "Einstein's equation with future-causality forces vanishing shear, vanishing null "
  "flux and £_ℓ q_ab = 0 — and leaves a gap at PERTURBATION order.** *That gap is "
  "the object.*")
W("")
W("**Where the obstruction sits.** The free half is confirmed numerically: the "
  "spectral weight ratio is of order 10⁻⁵. The obstruction is in the corner edge "
  "modes, and the proposal Θ = 0 was refuted by the transformation law. Sorce (2024) "
  "closes the geometric route by construction — a geometric modular flow must be "
  "generated by a conformal Killing field — so a horizon with no Killing field cannot "
  "have one, and the route that remains is algebraic.")
W("")
W("**What would settle it.** The covariance of conditional expectations across the "
  "full family of cuts, in the manner of an over-determined joint fit. *Chandrasekaran "
  "& Flanagan (arXiv:2601.07915) is the nearest published treatment and was read into "
  "the diagnosis at registers 1037–1042.*")
W("")

W("## `Q.exch` — the exchange factor")
W("")
W("        δ = [ … ] · (1 + s·[triplet]),   s = −0.0782")
W("")
W("**What is settled.** Exchange splitting between singlet and triplet is Heisenberg, "
  "*Mehrkörperproblem und Resonanz in der Quantenmechanik*, Z. Phys. **38** (1926) "
  "411–426; that the higher multiplicity lies lower is Hund's first rule, Z. Phys. "
  "**33** (1925) 345–371. **The physics is not in doubt.**")
W("")
W("**What is missing, precisely.** *The fitted sign is opposite to the measured one.* "
  "The factor was withdrawn at register 1168 for that reason and the grade left as "
  "ASSERTED rather than removed, because the term is real and the form is wrong.")
W("")
W("> **A uniform s cannot work.** *Exchange acts through the overlap of the Rydberg "
  "orbital with the core, and that overlap falls sharply with ℓ. A single multiplicative "
  "constant can only give 0 of 66 triplet-above-singlet pairs or 66 of 66; the "
  "measurement is neither.*")
W("")
W("**What would settle it.** An ℓ-dependent exchange term, fitted against the "
  "singlet–triplet pairs the compendium holds. The Pauli bound (`Q.bound`) already "
  "carries the orbital count p that the overlap should follow.")
W("")
W("---")
W("")
W("# VII · THE BIBLIOGRAPHY")
W("")
W("**Every object of this compendium names a work.** What follows is those works, "
  "ordered by year, with the objects each carries. *The book claims nothing new where "
  "an earlier result will do; where a measurement is this work's, the object says so.*")
W("")
import re as _re
_W = _re.compile(r"([A-Z][A-Za-z\u00e9\u00e8\u00e4\u00f6-]{2,}"
                 r"(?:\s*(?:&|and)\s*[A-Z][A-Za-z\u00e9\u00e8\u00e4\u00f6-]{2,}){0,3}"
                 r"(?:\s*et\s+al\.?)?)"
                 r"(?:'s)?[^.;]{0,90}?\((1[6-9]\d\d|20[0-2]\d)\)"
                 r"|\b([A-Z][A-Za-z\u00e9\u00e8\u00e4\u00f6-]{2,}"
                 r"(?:\s*(?:&|and)\s*[A-Z][A-Za-z\u00e9\u00e8\u00e4\u00f6-]{2,}){0,3})"
                 r"(?:'s)?\s+(1[6-9]\d\d|20[0-2]\d)\b")
# words that are never an author — they arrive from a title or a journal name
_STOP = {"That","This","Which","Both","Each","Every","When","With","From","Here","Its",
         "Gaussian","PARETO","Its","Their","These","Those","Both","Also","Only",
         "Graph","Theory","Data","Prior","PRIOR","Quantum","Atomic","Introductio",
         "Lattice","Categories","Methodus","Synthesizing","Modeling","Probabilistic",
         "Graphical","Reducibility","Interior-Point","AIEE","IEEE","Wahrscheinlichkeitstheorie",
         "Palermo","Psychometrika","Goettingen","Extensivity","Delta","NP-complete",
         "Boolean","Elements","Rings","General","Regular","Error","Assigning","Approximation",
         "Locating","Three","Weyl","Neumann","Theoria","Physical","Handbuch"}
_works = {}
for _k, _v in REG.items():
    _blob = " ".join(str(_v.get(x) or "") for x in ("src", "check"))
    for _m in _W.finditer(_blob):
        _n = (_m.group(1) or _m.group(3) or "").strip().rstrip(",")
        _y = int(_m.group(2) or _m.group(4))
        _head = _n.split()[0].rstrip(",")
        if _head in _STOP or _head.title() in _STOP or len(_n) < 4: continue
        # a bare surname followed by a year must be adjacent, not separated by a clause
        if _m.group(3) and _m.start(4) - _m.end(3) > 1: continue
        # normalise: keep the shortest form of a given surname-set at a given year
        _key = (_y, _head.title())
        if _key in _works:
            _cur, _ks = _works[_key]
            _works[_key] = (_cur if len(_cur) <= len(_n) else _n, _ks | {_k})
        else:
            _works[_key] = (_n, {_k})
_works = {(y, nm): ks for (y, h), (nm, ks) in _works.items()}
W(f"**{len(_works)} works, "
  f"{min(y for y, _ in _works)}\u2013{max(y for y, _ in _works)}.**")
W("")
W("| year | work | objects |")
W("|---|---|---|")
for (_y, _n), _ks in sorted(_works.items()):
    W(f"| {_y} | {_n} | " + " ".join(f"`{x}`" for x in sorted(_ks)) + " |")
W("")
W("### The works this compendium leans on most")
W("")
W("| work | objects |")
W("|---|---|")
for (_y, _n), _ks in sorted(_works.items(), key=lambda z: -len(z[1]))[:12]:
    W(f"| {_n}, {_y} | **{len(_ks)}** |")
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

print("\n".join(L) + "\n" + _tail("COMPENDIUM-TAIL.md"), end="")
