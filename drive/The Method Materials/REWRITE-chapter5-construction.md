# Rewrite — Chapter 5 (was Chapter 7), "The construction of Λ"

**Placement:** Part I — The Lattice, second chapter. Builds the zero-cost index Chapter 4 promised. This is the approved side-by-side pilot (v2), brought into line: Chapter 7 → 5, §7.x → §5.x, Figure 7.1 → 5.1. Cross-references to later chapters (8, 10, 15, 16, 17, §12.11) keep their current numbers; they shift at their own passes. Substance unchanged from the approved pilot — same eight coordinates, seven constraints, four origins, closure proof, counts 216/976/1636/2394, E(Λ)=0, 48.5% envelope density. The spin-envelope honesty (the one place the object is not exact) is kept — it is exactly the boundary register the settled Preface endorses. No time/observation frame arises in this chapter; it is the clean construction.

---

## 5. The construction of Λ

The object this book is about, written Λ, is a set. Its members are not atoms, or states, or energy levels. They are *transitions* — allowed moves of electrons. One member records a single move: where it starts, where it ends, and how many electrons take part. Each member is called a **cell**, and every cell is a list of eight numbers:

      (n, ℓ, k, q, e, f, g, 2S)

The eight entries fall into three groups. The first three say where the move begins. The next four say how many electrons leave and where they land. The last records a spin property of the result:

| coordinate | meaning |
|---|---|
| *n* | source shell (which shell the move starts from) |
| ℓ | source subshell (its orbital angular momentum) |
| *k* | source occupancy (how many electrons sit in that starting subshell) |
| *q* | electrons removed (how many leave in the move) |
| *e* | target shell |
| *f* | target subshell |
| *g* | target occupancy (how many electrons arrive) |
| 2*S* | multiplicity (twice the total spin of the result, kept as a whole number) |

Two fair questions arise: why *eight* numbers, and why *these* eight. Eight is the fewest that pin a transition down once spin coupling is set aside. Why these eight is the work of §5.1, and it is the heart of the construction: each of the eight is held in check by a physical law, and by nothing else.

Eight numbers are enough only while the finer detail of angular momentum is left implicit. When that detail must be carried — the target's spin, its seniority (a label that tells apart states of the same configuration and spin), and the way the angular momenta couple — five more coordinates join the list: 2S′, v, 2J_c, K and 2J. This grows the eight-coordinate object, written **Λ₈**, into a thirteen-coordinate one, **Λ₁₃**. The chain of objects between them (Λ₈, Λ₉, …, Λ₁₃) is what the book calls **the tower**. §12.11 builds it and sets the order in which the coupling coordinates are added: first J_c (the core's angular momentum), then K (the middle coupling), then J (the total). This chapter, and everything in the book that does not turn on coupling, is stated for the base object Λ₈. Where "Λ" appears with no subscript, Λ₈ is meant.

One point about the build should be made plain before the constraints are listed, because it marks the one place where the object is not exact. Of the four physical sources that hold the coordinates in check, three — the Pauli exclusion principle, the hydrogenic solution (the solution for one electron around a bare nucleus), and plain counting — give *exact* limits. A value is either allowed or it is not, with no slack. The fourth source, angular-momentum coupling, is different. The limit it gives, 2S ≤ k, is an **envelope**: it holds every multiplicity that k electrons can carry, but it also lets through some values that no set of k electrons can actually reach. At the counting caps of §5.4, this envelope is met by 48.5% of the cells it allows — so fewer than half of the spin values it permits can really occur. The book does not tuck this away. §12.11.3 states the split between the exact limits and this one envelope, and §12.11.2 shows the envelope is forced — that no exact limit of the needed form exists for spin.

### 5.1 The constraints, and where each comes from

Λ is not the whole set of possible eight-tuples. If it were, it would hold moves that cannot happen. It is instead the part of that set meeting seven conditions, each tracing back to one physical source:

|  | constraint | origin |
|---|---|---|
| 1 | ℓ ≤ n − 1 | hydrogenic solution |
| 2 | k ≤ 2(2ℓ + 1) | Pauli exclusion |
| 3 | q ≤ k | counting — cannot remove more than are present |
| 4 | f ≤ e − 1 | hydrogenic solution |
| 5 | g ≤ 2(2f + 1) | Pauli exclusion |
| 6 | g ≤ q | counting — cannot place more than were removed |
| 7 | 2S ≤ k | vector coupling |

Conditions 1 and 4 say a subshell's angular momentum cannot reach its shell number — a fact of the hydrogen solution. Conditions 2 and 5 are the Pauli limit on how many electrons a subshell holds, 2(2ℓ+1). Conditions 3 and 6 are bookkeeping: you cannot take out more than are there, nor put in more than you took out. Condition 7 is the spin envelope just described.

**Seven constraints, four origins, and nothing else.** This is the claim the chapter rests on, and it is one a reader can check rather than take on faith: read down the origin column and every entry is Pauli, the hydrogenic solution, counting, or vector coupling — there is no fifth kind, and no line whose source is a number chosen to make the count come out. The table is the whole of the input, printed. Everything Part III later draws from Λ depends on that being true, because a single constraint from a fifth source — a fitted cutoff, say — would make it impossible to tell afterward which of Λ's properties belong to the indexing and which were carried in on the back of that one bound. The four-origin table is what keeps the two separable, and it is short enough to audit in a glance.

### 5.2 Every constraint is of one form

Look again at the seven conditions. Each has the same shape:

      xᵢ ≤ φ(xⱼ)

— one coordinate held below a function of one *other* coordinate, and that function is monotone (it never turns downward: raise the input and the bound does not fall). Not one condition adds two coordinates together; not one subtracts. This is not just how they happen to be written. Chapter 17 shows it is forced: a set cut out by a bound that summed two coordinates would not be closed in the sense §5.3 makes exact, and closure is the one thing the rest of the book cannot do without.

The single shape has a plain consequence, drawn out in full in Chapter 8. Draw a picture whose points are the eight coordinates, with a line between two of them whenever a condition ties one to the other. Because each condition ties just one coordinate to one other, this picture is a **tree** — all of one piece, with no closed loops.

![Figure 5.1](figures/figure-5.1.png)

Figure 5.1. Each of the seven conditions ties one coordinate to one other. The result is eight points joined by seven lines, all of one piece and with no loops: a tree. A tree has **treewidth 1** — the lowest real value of the measure that says how hard the object is to reason over. Three results later in the book rest on this one fact, and it helps to name them now, so the tree is seen to earn its place rather than sit there for show. All three are drawn out in Chapter 8. First, **the void needs no sieve**: a tree has no loops, so counting the cells needs no correction for overlap, and Chapter 10 gives a count in closed form. Second, **the order can be recovered**: the orders on the eight coordinates can be rebuilt from an unlabelled bag of cells by passing the known parts along the tree, shown at 20 of 20 in Chapter 15. Third, **the picture holds no spare routes**: there is exactly one path between any two points, so the two-route safeguard the object leans on to defend itself (Chapter 16) cannot come from the conditions, and has to come from other, derived quantities instead. The third is a real limit on how the object can be built, and it shows up here, three chapters before it is needed.

### 5.3 Λ is closed

The property all of this has been pointing toward is **closure**. Take any two cells x and y in Λ. Build two new cells from them: their high cell x ∨ y, made by taking the larger value in each of the eight slots, and their low cell x ∧ y, made by taking the smaller. The claim is that both of these are again cells of Λ. The object is closed under taking highs and lows.

The reason is short enough to see in one line. Every condition reads xᵢ ≤ φ(xⱼ) with φ monotone, so if the i-th slot of x ∨ y is taken from x, then (x∨y)ᵢ = xᵢ ≤ φ(xⱼ) ≤ φ((x∨y)ⱼ) — the first step because x is in Λ, the second because φ never turns downward and (x∨y)ⱼ is at least xⱼ. The condition survives; the slot-from-y case and the low cell run the same way. The **full proof — both cells, both branches, each of the seven conditions written out — is carried in the Mathematical Compendium** [MC-01], which also records that this is the definition of a sublattice of a product of chains (Birkhoff, 1940), and that what makes Λ one is precisely that all its constraints have the single monotone form.

Closure is just what makes Λ a *lattice*, and it is the hinge Part III turns on.

There is a second way to say the same thing, and it is the way the book leans on most. Write ℛ(X) for the set you get by adding to X every cell that X's own bounds already call for — the closure of X under highs and lows, built from X's own values and nothing brought in from outside. (ℛ is set out in full in §11 and Appendix A; the point to hold here is that nothing external enters — ℛ(X) is what a reader could rebuild from the cells alone.) Now write

      E(X) = |ℛ(X)| − |X|

for the number of cells the bounds call for but that X does not hold — the gap between what X's own bounds ask for and what X actually has. A set is closed exactly when E(X) = 0: nothing is called for that is not already there.

For Λ, **E(Λ) = 0**. This is checked not by the proof alone but by direct count at four cap settings, where Λ holds 216, 976, 1,636 and 2,394 cells. At each one, ℛ adds nothing (E = 0), the answer is reached in a single pass, and it holds steady under a second pass — ℛ(ℛ(Λ)) = ℛ(Λ). So Λ is a true fixed point of ℛ, not merely closed by luck at one size.

### 5.4 A note on caps

Λ as defined has no end: n and e run over all shells. Every *count* in the book is therefore given at set, finite caps on n, e, ℓ and k — the four numbers 216, 976, 1,636 and 2,394 above come from four such settings. The counts depend on the caps and move with them; wherever a number depends on the caps, it is marked. The *shape* does not depend on the caps — a claim Chapter 8 makes exact, where the pattern that makes the cells is shown to be the same across a twenty-eight-fold spread in cell count. Every claim about shape has been checked at no fewer than four settings, so that nothing rests on where the counting happened to stop.
