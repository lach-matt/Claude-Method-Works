# The three-body problem, and which pairs exist

> **DRAFT — UNFINISHED, AND DELIBERATELY SO.**
> This chapter records where the work stands. The material currently sits as a
> four-line coda to §34 of *The Method 1.6*; it is larger than that and is
> given its own chapter here. Every claim carries its register number.
> Written at register 1569.

---

## 1 · What is and is not claimed

**The method offers no solution to the general three-body problem.** It offers
a statement about **which pairs of bodies the problem's own coordinates
carry** — and that statement turns out to have consequences.

A Rydberg atom is three bodies: a nucleus, a core of Nₑ − 1 electrons, and one
outer electron. *The claim below is about the INDEX of that problem, not about
the interaction.*

## 2 · The pair that has no variable

**Λ_var** places every variable of the problem on (body, role), and **closes
with E = 0**.

| body | input | intermediate | output |
|---|---|---|---|
| **nucleus** | Z | · | · |
| **core** | Nₑ | ℓ_core, n_out | · |
| **core + rydberg** | · | p, n₀, T | · |
| **nucleus + core** | c | u | · |
| **rydberg** | ℓ | · | δ |
| **nucleus + rydberg** | **—** | **—** | **—** |

> **No variable in the index relates the Rydberg electron to the nucleus
> directly.** Every quantity connecting them — the effective charge c, the
> collapse variable u — is a nucleus–core quantity that the Rydberg electron
> then reads.

**This is the screening statement appearing as a fact about coordinates**, and
it must be read carefully. *The nucleus does attract the outer electron, and
strongly. What the index says is that no COORDINATE of this problem carries
that attraction unmediated.*

**And the channel equation has exactly that shape.** δ = √p · f(u) is a
core–rydberg factor times a nucleus–core factor, **with no third factor
because the index holds no third pair.**

## 3 · The constraint the ladders inherit

Because **Z = Nₑ + c − 1**, only two of the three electronic quantities are
independent. **A ladder fixing one varies the other two, and no ladder can
vary Z alone.**

*This is why the isoelectronic, isonuclear and isoionic ladders are three
views of a two-dimensional space rather than three independent axes — a fact
about the coordinates, not about the experiments.*

## 4 · Two Helly orders, one problem

**The two-state three-body structure is one problem at two Helly numbers,
differing by N − 1** (R 1520).

The known-mass and unknown-mass cases are the same object measured at
different orders. **Certificates transfer UPWARD only**: an infeasibility
proved at low order holds at high order, but feasibility at low order proves
nothing above it. *This is Fishburn's warning again, in the three-body
setting.*

**The envelope IS the feasible set, of dimension N − 1.**

## 5 · The shared mechanism

The three-body structure, the Löwdin corridor and M.C2 were joined as **one
object under one measure** (R 1515–1521). Each is a system of linear
inequalities; each has a Helly number; each has a conflict graph whose maximum
clique is its verdict.

    Λ              clique 1    closed
    M.C2           clique 1    conditional
    nuclear        clique 2    refuted
    Löwdin         clique 3    obstructed

**Where the geometry degenerates, use another face.** The nuclear corridor is
rank-one, so the geometric face is degenerate and the statistical face —
fractional Helly — is the live one. *The measure does not change; the language
does.*

## 6 · The nuclear corridor, and a structural emptiness

The nuclear shell model corridor is the sharpest result in this family.

**Six consecutive pairs all require the same combination 4β + α. Three demand
it positive and three demand it negative.** The feasible set is therefore
**structurally empty** — established by exact rational arithmetic, not by
numerical near-miss.

**And the refuted family is named**: Nilsson's modified oscillator,
H = HO − κℏω₀[2 l·s + μ(l² − ⟨l²⟩_N)], Nilsson (1955), where β = −κμℏω and
α = 2κℏω (R 1393). *So the corridor tested the Nilsson potential in its
spherical limit.* The transfermium orbital check found 11 of 12 pass and one
fails on parity — but that is the deformed regime, which does not test the
spherical-limit refutation either way.

## 7 · What is open

- **Why N − 1?** The gap between the two Helly orders is measured and not
  explained.
- **The nuclear correction into the artefacts.** The six-pair count and the
  4β + α identity are established but register 1370, HANDOFF and the
  Mathematical Compendium still carry the earlier undercount and the
  "coincidence" reading. **This is owed and is the concrete next step.**
- **Whether the conflict-graph measure extends past these four objects.**
  Four is not a pattern.

---

*The three-body contribution is negative in form and useful in consequence: the
index carries no nucleus–rydberg pair, so the channel equation has two factors
and not three, the three ladders span two dimensions and not three, and the
same Helly measure that reads the corridor reads this.*
