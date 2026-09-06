# -*- coding: utf-8 -*-
import hashlib

src = open("BUILD60_compendia.md", encoding="utf-8").read()
lines = src.split("\n")

# ---- pre-asserts ----
assert lines[14610] == "### `L.chains` — the linear extensions", lines[14610]
assert lines[14620] == "### `L.chi` — the membership function", lines[14620]
assert lines[14500] == "### `L.birk` — Birkhoff representation 1937", lines[14500]
assert lines[14800] == "### `L.sperner` — Sperner property / Dilworth", lines[14800]
n_1113_before = src.count("1,113,045,672")

block = """### The surface is a cylinder

**Λ's derived quantities split into two classes — *e*, ν, *V* rising up a series and *T*, *r*, δ, spacing, *w* falling — exchanged under the map ν ↦ ν⁻³, so the sign structure is bipartite; and a bipartite sign structure can reverse orientation only an even number of times along any closed traverse, which makes the surface orientable, a cylinder and not a Möbius band. The finding is a reason, not an absence of one: verified exhaustively, zero orientation-reversing loops among all cycles of length 3 through 5, and both alternative routes to a twist close by construction — a non-monotone quantity contributes an *undefined* edge rather than a reversing one, and a quantity independent of ν contributes *no* edge, leaving no third way to build a reversal. The structural guarantee is underwritten by the shape of the constraint graph itself: it is a tree — eight vertices and seven edges, connected and acyclic, measured in every other shape the lattice contains (§12.9) — so §12.1's orientability follows from the construction and not from a search that merely failed to find a counterexample. The cylinder is a cylinder over the transfer coordinate *q*, the base of the fibration whose fibres the two-body separation (§12.6.1) computes.**

*the two derived-quantity classes of §12.1 under ν ↦ ν⁻³; orientability certified exhaustively over cycles of length 3–5 and structurally from the tree constraint graph; at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1).*

Proved — M §12.1; König 1936; Harary 1953; Listing 1861; Möbius 1865; Freuder 1982.

> **Prior art: a graph is bipartite exactly when it carries no odd cycle — König, *Theorie der endlichen und unendlichen Graphen* (1936); a sign structure whose classes exchange is balanced, every cycle carrying an even number of reversals — Harary, *Michigan Math. J.* 2 (1953); the one-sided band the finding excludes is Listing (1861) and Möbius (1865); a constraint graph of width one is a forest, so carries no cycle to twist — Freuder, *J. ACM* 29 (1982). That Λ's ascending and descending quantities form exactly such a bipartite sign structure under ν ↦ ν⁻³, and that its constraint graph is the tree which forces orientability by construction rather than by search, is this book's.**

### The two-body separation

**The lattice does not factorise, and then it does. As a bare product of its two ends it fails — |A| × |B| × |q| = 33 × 17 × 4 = 2,244 against 976 — because the ends are coupled twice over, q ≤ k tying the transfer to the parent and g ≤ q tying the target's occupancy to the transfer. Conditioned on the coupling they separate exactly: |Λ| = Σ_q |A(q)| × |B(q)| = 33·5 + 33·10 + 23·15 + 8·17 = 165 + 330 + 345 + 136 = 976, exactly. One end is the parent configuration (n, ℓ, k) with its spin 2S, the other the target (e, f) with its occupancy g, and they meet at q, the number transferred — the shape of a two-body problem, two objects and a coupling, separating as a two-body problem separates, into centre-of-mass and relative motion with q in the role of the conserved coupling. The exactness is the tree's doing: q is a cut vertex of the constraint tree (§8.5), so fixing it severs every path between the two sides, and the count of a severed pair is a product — the same separator property that makes the box factorisation (§10.4) close in one pass. The four section counts 165, 330, 345, 136 are the cylinder's profile, computed rather than drawn: the base is q — the axis along which the surface is a cylinder (§12.1) — and the fibre at each q is A(q) × B(q).**

*the two ends A = (n, ℓ, k; 2S) and B = (e, f; g) of the constraint tree, coupled through q by q ≤ k and g ≤ q; separation verified by exhaustive enumeration at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1).*

Proved — M §12.6.1; Newton 1687; Lauritzen 1996.

> **Prior art: that a two-body problem separates into centre-of-mass and relative motion about a conserved coupling is Newton's reduction (*Principia*, 1687); that conditioning on a separating vertex of a tree renders the two sides independent — the property that turns a coupled count into a sum of products — is Lauritzen, *Graphical Models* (1996). That Λ's eight coordinates are two such bodies, parent and target meeting at the transfer, with the bare product 2,244 failing and the conditioned sum returning 976 exactly — the cylinder's profile 165, 330, 345, 136 — is this book's.**

### The fibres, in closed form

**Each side of the cylinder has its own closed expression, and they are different shapes. A_q(z) = Σ_{n=1}^{3} zⁿ Σ_{ℓ=0}^{min(n−1,1)} z^ℓ Σ_{k=max(q,1)}^{min(4ℓ+2,3)} z^k · (1 − z^{min(k,3)+1})/(1 − z) and B_q(z) = Σ_{e=1}^{3} z^e Σ_{f=0}^{min(e−1,1)} z^f · (1 − z^{min(q,4f+2)+1})/(1 − z), each trailing factor a finite geometric sum counting the pendant coordinate — 2S ≤ k on the A side, g ≤ min(q, 4f+2) on the B side. Both verified against enumeration at every q as full polynomial identities, coefficient by coefficient, not merely at the evaluations; the evaluations A_q(1) = 33, 33, 23, 8 and B_q(1) = 5, 10, 15, 17 recover the profile of the two-body separation (§12.6.1). And the two sides are not the same tree: A_q is a caterpillar — the path n—ℓ—k with 2S pendant at k — while B_q is a path, e—f—g, capped by the base, so the whole lattice is a caterpillar because it is these two glued at q, and the pendant sits on the A side only. The fibration iterates: Λ fibres over q with fibre A_q × B_q; A_q fibres over k with fibre an (n, ℓ)-set times the 2S-chain; B_q fibres over f with fibre an e-set times the g-chain — three levels, each verified an exact product at every value of its base, and at the bottom every fibre is a product of chains, a box, with the closed form Box(a, b)(z) = ∏ᵢ z^{aᵢ}(1 − z^{bᵢ−aᵢ+1})/(1 − z). Each level closes for the reason the two-body separation is exact: fixing the base variable severs the fibre into independent factors — the elimination of the box factorisation (§10.4), run level by level to a floor of boxes.**

*the two fibre polynomials at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); identities verified per q by exhaustive coefficient comparison; all three fibration levels verified as exact products.*

Proved — M §12.7; Euclid c. 300 BCE; Euler 1748; Steenrod 1951; Harary & Schwenk 1973; Stanley 1986; Lauritzen 1996.

> **Prior art: the finite geometric sum is Euclid, *Elements* IX.35; counting by generating function is Euler, *Introductio in analysin infinitorum* (1748); the rank generating function of a graded poset is Stanley, *Enumerative Combinatorics I* (1986); the caterpillar is named in Harary & Schwenk (1973); the fibration language is Steenrod, *The Topology of Fibre Bundles* (1951); elimination along a tree, one vertex at a time, is Lauritzen, *Graphical Models* (1996). That the cylinder's two sides carry different trees — caterpillar against path, the pendant on one side only — with closed forms exact at every q, and that the fibration iterates in three levels to a floor of boxes, is this book's.**

### Four numbers, five facts

**The counts 165, 330, 345, 136 carry more than their sum — five facts read off the table, every one verified exhaustively. First, a Pareto frontier inside the lattice: |A_q| falls 33, 33, 23, 8 while |B_q| rises 5, 10, 15, 17, so raising the transfer costs the parent and pays the target, monotonically, and no q improves both — the shape of §23.5's dw/dh > 0 with dV/dh < 0, which the book presents as a fact about brackets and is here a fact about the index itself. Second, a most-probable transfer: the fibre peaks at q = 2 with 345 cells, 35.3% of Λ, the sequence is log-concave hence unimodal, and the mean transfer ⟨q⟩ = 1428/976 = 1.4631, sd 0.930, is S′(1)/S(1) in the base variable — the number of electrons moved, averaged over every admissible configuration. Third, an 8-to-3 compression that loses no count: Λ's generating function has eight variables, the shape has three, and S(1,1,1) = 976 — not a projection that forgets cells but one that forgets which coordinate inside each side and keeps how many, a general fact about caterpillars, a path with one pendant reducing to (base, left, right) whatever its length. Fourth, every cross-section is itself a closed, modular lattice: all eight slices — A_q and B_q at each of the four q — are closed under coordinatewise join and meet with E = 0, and the modular law x ∨ (a ∧ b) = (x ∨ a) ∧ b for x ≤ b holds on all 31,519 conditioned triples across the eight slices with zero failures; each slice is in fact distributive, all 93,966 triples passing, as a sublattice of a product of chains must be — the sublattice closure (§7.3) restricting to each fibre. The shape is not a cylinder over an arbitrary set; it is a cylinder whose every cross-section satisfies this book's own law. Fifth, E(X) gains a local form: E(Λ) = 0 and E(A_q) = E(B_q) = 0 for every q, and the second does not follow from the first — a closed index could in principle carry defective slices, and here none do, a new invariant.**

*the fibre table of the two-body separation (§12.6.1); all five facts at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); closure, the modular law and the distributive law checked on every triple of every slice; the mean exact as 1428/976.*

Proved — M §12.8; Pareto 1896; Laplace 1812; Dedekind 1900; Birkhoff 1937; Harary & Schwenk 1973; Stanley 1989.

> **Prior art: the frontier on which no move improves both objectives is Pareto, *Cours d'économie politique* (1896); the mean as G′(1)/G(1) of a generating function is Laplace, *Théorie analytique des probabilités* (1812); that a positive log-concave sequence is unimodal is elementary, surveyed in Stanley (1989); the modular law is Dedekind (1900); that a sublattice of a product of chains is distributive, hence modular, is Birkhoff (1937); the caterpillar reduction to (base, left, right) rests on Harary & Schwenk (1973). That the fibre table carries all five at once — a Pareto frontier inside an index, a most-probable transfer, a count-preserving compression, cross-sections every one closed and modular, and a local form of E — is this book's.**

### Every other shape the lattice contains

**Intervals, antichains, chains — and one shape absent. An interval [x, y] is a box exactly when no constraint binds across it: I_{x,y} = Box(x, y) ⟺ for every constraint u ≤ φ(v), y_u ≤ φ(x_v) — the record tested sixty of sixty, and the criterion is here proved by exhaustion, agreeing with direct enumeration on all 115,162 comparable intervals without exception. Boxes are 31,604 of 115,162 — 27.4%, the record's sampled 27% now the exact population figure — and the other 72.6% are where the physics is active: some constraint binds. The binding rates rank the constraints — the record's sample reads g ≤ q at 35.6%, q ≤ k at 33.0%, g ≤ 4f + 2 at 4.9% (§12.9), and over the full population of meet-join intervals [x∧y, x∨y] of all 475,800 unordered pairs, exhaustively, the rates are 30.0%, 28.0% and 1.9% — the same order on both bases. The most active constraint is the coupling; the least is the Pauli bound — which §16.8 finds the cheapest to violate; two independent measures, one answer. The eighteen rank levels partition Λ into eighteen antichains while every maximal chain carries exactly eighteen cells, so the minimum antichain partition and the maximum chain meet at eighteen — Mirsky's dual of Dilworth, exactly attained; the largest level, 122 at rank 11, is the largest antichain outright, certified by the Dilworth chain partition of the Sperner property (§8.4), and Λ is exactly eight times its widest level, 976 = 8 × 122. Λ is the lattice of down-sets of its seventeen join-irreducibles — the Birkhoff representation (§8.3) — so its maximal chains are the linear extensions of that seventeen-element poset: e(P) = 1,113,045,672, recomputed independently this build on the rank grading and exact, where counting linear extensions is #P-complete in general. And the two seventeens are one: every cover adds exactly one join-irreducible, so a maximal chain of seventeen steps enumerates the seventeen generators of §8.3 one at a time — the book reports both numbers without connecting them, and the connection is that they are the same count. One shape is absent: the constraint graph is eight vertices and seven edges, connected and acyclic — measured, a tree — so there is no Möbius band, no cycle, no non-planar minor, nothing to twist and nothing to close; the orientability of the surface — the surface is a cylinder (§12.1) — follows by construction, not by search.**

*the interval census exhaustive over all 115,162 comparable intervals at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); binding rates on two bases, the record's sample and the exhaustive meet-join population, each named; e(P) by independent chain-counting on the rank grading.*

Proved — M §12.9; Birkhoff 1937; Stanley 1986; Brightwell & Winkler 1991; Sperner 1928; Dilworth 1950; Mirsky 1971; Listing 1861; Möbius 1865; Kuratowski 1930; Wagner 1937; Freuder 1982.

> **Prior art: a finite distributive lattice is the down-sets of its join-irreducibles — Birkhoff (1937); its maximal chains correspond to the linear extensions of that poset — Stanley, *Enumerative Combinatorics I* (1986), Prop. 3.5.2, carried from the entry this one absorbs; counting linear extensions is #P-complete in general — Brightwell & Winkler (1991); the largest antichain at a rank level is the Sperner property (Sperner 1928), certified by chain partition after Dilworth (1950); the dual — minimum antichain partition equals maximum chain — is Mirsky (1971); the one-sided band the census excludes is Listing (1861) and Möbius (1865); the minor characterisation of planarity is Kuratowski (1930) and Wagner (1937); a width-one constraint graph is a forest — Freuder (1982). That the box criterion is exact on the whole population, that the binding rates rank coupling first and Pauli last on two independent bases, that the eighteens meet with Mirsky attained, that the seventeens are one — a maximal chain enumerating the seventeen generators one cover at a time — and that Λ is eight times its widest antichain, is this book's.**
"""

newlines = lines[:14610] + block.split("\n") + lines[14620:]
# heading conversions (positions shift only after insertion point; L.birk is before it)
h1 = newlines.index("### `L.birk` — Birkhoff representation 1937")
newlines[h1] = "### The Birkhoff representation"
h2 = newlines.index("### `L.sperner` — Sperner property / Dilworth")
newlines[h2] = "### The Sperner property"

out = "\n".join(newlines)
open("BUILD61_compendia.md", "w", encoding="utf-8").write(out)

# ---- measured-diff guard ----
old = lines; new = newlines
print("lines:", len(old), "->", len(new), "(expected +40:", len(new)-len(old)==40, ")")
# region check: identical outside [14610:14620)->block and the two heading lines
mism = []
for i in range(14610):
    if old[i] != new[i]:
        mism.append(("pre", i+1, old[i][:60], new[i][:60]))
off = len(new) - len(old)
for i in range(14620, len(old)):
    if old[i] != new[i+off]:
        mism.append(("post", i+1, old[i][:60], new[i+off][:60]))
allowed = {("pre",14501), ("post",14801)}
bad = [m for m in mism if (m[0],m[1]) not in allowed]
print("changed lines outside block:", [(m[0],m[1]) for m in mism], "| unauthorized:", bad)
assert not bad

def c(s): return out.count(s)
checks = [
 ("### `L.chains`",0), ("### `L.birk`",0), ("### `L.sperner`",0),
 ("### The surface is a cylinder",1), ("### The two-body separation",1),
 ("### The fibres, in closed form",1), ("### Four numbers, five facts",1),
 ("### Every other shape the lattice contains",1),
 ("### The Birkhoff representation",1), ("### The Sperner property",1),
 ("zero orientation-reversing loops",1),
 ("165 + 330 + 345 + 136 = 976, exactly",1),
 ("coefficient by coefficient, not merely at the evaluations",1),
 ("31,519 conditioned triples",1),
 ("31,604 of 115,162",1),
 ("976 = 8 × 122",1),
]
ok=True
for s,e in checks:
    g=c(s); ok &= g==e
    print(("PASS" if g==e else "FAIL"), f"[{s[:45]}] got {g} exp {e}")
print("1,113,045,672 count:", n_1113_before, "->", c("1,113,045,672"), "(net unchanged expected)")

# full §0.4 suite must still pass unchanged
suite = [("order dimension of Λ₈ is 7",1),("Dilworth partition of all 976 cells into 122 chains",1),
("fifteen coordinate-support patterns",1),("riding monotonicity upward",1),("### W-090",1),("### W-091",1),
("### `S.gen`",1),("### `K.bracket`",1),("## THE PRIOR-ART CHAIN",1),
("ω(N(x)) ≤ 8, the coordinate count — proved and tight",1),
("five equivalent forms, all equal to ∏_i(|x_i−y_i|+1)",1),("the maximum local up-degree is 7",1),
("μ_Λ(x,y) = μ_arith(N(x),N(y)) if and only if the interval",1),
("exactly the product of the six edge lifts in tree order",1),
("1.0000 in every stratum for all five shared-coordinate pairs",1),
("`K.decay` `K.markov` `L.voidfrac`",0),("`K.decay` `K.markov` `L.box` `L.voidfrac`",1),
("Chebyshev's sum inequality",2),("116,138 distinct boxes, zero discrepancies",1),
("width 1 if and only if it is a forest",1),("the tree count is 280, the true count 240",1),
("the accepted set is equal as a set to the image",1),("no bit is forced by more than 3 others",1),
("0.7446 % of the space it is written in",1),
("### `L.omega`",1),("### `L.occ`",1),("### `L.metric`",1),("### `L.mobius`",1),("### `L.voidfrac`",1),
("### `L.box`",1),("### `L.bits`",1),("### `L.circuit`",1),
("### The language combinations",1),("### The detachable leaf",1),("### Why a closed expression exists",1),
("### The alternating specialisation",1),("### Palindromic rank polynomial ⟺ self-dual",1),
("### `L.comb`",0),("### `L.Fm1`",0),("### `L.pal`",0),("F(-1) counts the difference",0),
("`L.Fm1`",2),("`L.pal`",1)]
sok=True
for s,e in suite:
    g=c(s); sok &= g==e
    if g!=e: print("SUITE FAIL", s[:50], g, e)
print("§0.4 suite on BUILD61:", "43/43 PASS" if sok else "FAILURES", "| guard:", "PASS" if (ok and sok and not bad) else "FAIL")
data = out.encode("utf-8")
print("BUILD61 md5:", hashlib.md5(data).hexdigest(), "bytes:", len(data), "lines:", out.count(chr(10)))