# FINDING R4-06 — Chapter 34's two universals. The reset rule is held and states itself; both universals are false; and the true reasons are derived. NOT REPAIRED.

Candidate **D-21** of `CANDIDATES-R4-subject-matter.tsv`. Measured from the seated member
`LW1-ground.py` (register 1306, the observed NIST ASD 5.12 configurations) and from the corpus's own
`walk.py`, imported by path.

Three instruments, each with a selftest over the corpus's own recorded numbers:
`method/proofs/universals.py`, `method/proofs/walkresets.py`, `method/proofs/fdomain.py`.

> **This file supersedes its own first version, written earlier the same day.** That version scored
> §34.6's second clause over all eighteen recalibrations and reported *"four subshells carrying ten
> resets between them."* **That was wrong.** Eight of the eighteen do not move `a` at all. The
> corrected count is **two subshells and three moves**, and the correction favours the book. The
> mistake is kept here rather than quietly replaced, which is the discipline the Register is built
> on.

---

## 1. The reset rule was never missing. It is in the instrument, in its own first lines.

M asked whether the reasoning exists in the repository before anything is derived. For the reset
rule it does, and it is not buried: `walk.py`, in the recovered estate at
`extracted/archives/restore-point-2-13/`, opens by stating its own rule.

> **"THE HANDSHAKE — `a` resets only when the previous atom's value fails.**
> **walk Z upward. keep `a` if it still lies in the new bracket. if not, move it the MINIMUM
> distance to re-enter."**

Run against the seated ground configurations it reproduces §34.6 exactly: **106 steps · 106
satisfied · 18 recalibrations**, at the eighteen elements the chapter names.

**And the rule says nothing about subshells.** It is a rule about a carried value and a moving
corridor. So *"it never resets mid-subshell"* was never a consequence of the rule. It is an
observation about where the rule happened to fire, and §34.6 presents it as a reason.

## 2. Eight of the eighteen do not move `a`

`walk.py` tests `lo < a < hi` strictly and then steps `a` past the endpoint by 10⁻⁶. When the
carried value sits **exactly on** a corridor endpoint the test fails and a recalibration is
recorded, but the value does not change.

| | count | where |
|---|---|---|
| **real moves** | **9** | K 19, Rb 37, Cs 55, Ce 58, Hg 80, Tl 81, Fr 87, Pa 91, Lr 103 |
| **boundary touches**, \|Δa\| = 2 × 10⁻⁶ | **8** | Mo 42, Tc 43, Rh 45, Gd 64, Tb 65, Cm 96, Bk 97, Rf 104 |
| **initial placement**, no value carried yet | **1** | Li 3 |

The nine values `a` takes are **0.5774 · 1.0000 · 1.2168 · 0.7071 · 0.8090 · 1.0000 · 1.3938 ·
1.3660 · 1.9841**, and four of them — at K, Rb, Cs and Fr — are the ns/(n−1)d crossings §34.5 gives
a closed form for.

**And that corroborates §34.5's formula while contradicting two of its printed values.** The walk's
corridor computes **0.5773503, 1.0000000, 1.2167605, 1.3938469**, which is exactly what
(√(n−1) + √(n−4))/3 gives at n = 4 to 7. **§34.5 prints 1.2168450 and 1.3938270 at n = 6 and 7.** So
two independent routes — the chapter's own closed form and `walk.py`'s corridor, which share no code
— agree with each other and neither gives the printed values. That is the record's **16z-04**,
already confirmed by measurement as **34re-01**, and it is not new here; what is new is the third
route. There is no precision defence: a closed form over integers is exact.

> **A correction to this file's own first version**, which said the four values *are* §34.5's
> printed crossings. They are the values of §34.5's **formula**. Two of the four printed figures
> differ from it at the fifth decimal, and saying otherwise credited the book with a corroboration
> it does not have.

**The distinction is not pedantry.** *"Each subshell fills at constant `a`"* is a claim about a
**value**. A boundary touch cannot falsify it; a real move can. Scoring all eighteen, as the first
version of this finding did, counts eight non-events as counterexamples.

## 3. The first clause is very nearly right

**Eight of the nine real moves are at the opening of the subshell that is entering** — K 19 (4s),
Rb 37 (5s), Cs 55 (6s), Ce 58 (4f), Tl 81 (6p), Fr 87 (7s), Pa 91 (5f), Lr 103 (7p).

**One is not: Hg 80**, whose entrant is 6s, opened long before at caesium. That is §34.6's own
*"return from an exception"* class — Au is 6s¹, Hg returns to 6s².

**So `a` never moves inside the filling of the subshell that is entering.** Read that way §34.6's
first clause is true, and its own three-way classification is what makes it true.

## 4. The second clause is false, and the reason is that subshells overlap

*"which is why each subshell fills at constant `a`"* does not follow, and it fails:

| subshell | opens | full | the real move inside it |
|---|---|---|---|
| **5d** | Z 57 | Z 79 | **Ce 58**, 1.2168 → 0.7071, entrant **4f** |
| **6d** | Z 89 | never completes in the table | **Pa 91**, 1.3938 → 1.3660, entrant **5f**; **Lr 103**, 1.3660 → 1.9841, entrant **7p** |

**Every other subshell does fill at constant `a`.**

**And the mechanism is exact.** A move made at the opening of one subshell lands inside another's
filling whenever two are partly filled at once. That happens only in the d block, because **d
straddles f**: 5d is open when 4f enters, and 6d is open when 5f and then 7p enter. The clause fails
for precisely the two subshells that overlap an f block, and for no others.

**What is owed on §34.6, and it is M's.** The measured statement is available and is not weaker than
the false one:

> *`a` never moves inside the filling of the subshell that is entering — every recalibration is at
> that subshell's opening, at an aufbau exception in it, or at the return from one. It moves inside
> a subshell that is open but not entering, and that happens only where the d block straddles an f
> block: 5d at cerium, 6d at protactinium and at lawrencium.*

---

## 5. The f domain. The premise is false at 5f, the conclusion is true, and the true reason proves more than §34.9 claims.

**§34.9 (main L9702):** *"**f is outside the domain and the law says so.** At any f opening
p = n−ℓ−1 = 0, the floor of the node count — no subshell has fewer nodes than none — **so no rival
lies below and L = −∞.**"*

**The premise is arithmetic and it is wrong at 5f**, which opens at protactinium with
p = 5 − 3 − 1 = **1**. The record has this as 34re-07 and it is exact.

### The derivation, and it is three lines

Write **ρ(r) = n_r − ℓ_r − 1** for a subshell's node count, so the law's own argument under the root
is p_r = ρ(r) + q_r/2(2ℓ_r+1). Admissibility is the law's own, q_r < 2(2ℓ_r+1), so that fractional
term lies in [0, 1). At an **opening** the entrant has q_g = 0, so p_g = ρ(g) exactly, an integer.

> **CLAIM.** At an opening, an admissible rival lies below the entrant — p_r < p_g — **if and only
> if its node count is strictly smaller**, ρ(r) < ρ(g).
>
> **PROOF.** If ρ(r) < ρ(g) then p_r < ρ(r) + 1 ≤ ρ(g) = p_g, since the fractional term is under one
> and node counts are integers. If ρ(r) ≥ ρ(g) then p_r ≥ ρ(r) ≥ ρ(g) = p_g. No cases remain. ∎
>
> **COROLLARY.** L = −∞ at the opening of g exactly when **every subshell of smaller node count is
> full**.

**Two ways that happens, and §34.9 states only the first.** Either ρ(g) = 0 and the set below is
empty — the node floor, which is the right reason at 4f — or ρ(g) > 0 and everything below is
already complete. **5f is the second kind:** ρ = 1, and the four node-floor subshells 1s, 2p, 3d and
4f are all full at thorium, so each fails the law's own admissibility test. **The floor is reached
by exhaustion instead of by arithmetic.**

Checked at all twenty-four openings of the observed order, the claim holds at every one.

> **AND THE RECORD ALREADY HAD THIS, which the first version of this file denied.** It said *"the
> conclusion survives, and this is the part the record does not carry."* That is false. Deviation
> **16z-05** carries it exactly, banked, in the conversation numbered 127:
>
> > *"MEASURED: 4f: 4 − 3 − 1 = 0. 5f: 5 − 3 − 1 = **1**. At Pa (Z = 91, entrant 5f) the corridor is
> > one-sided because **every admissible rival has larger n (all smaller-n subshells full) —
> > admissibility, not the node floor**; register 1403 calls Pa's floor 'degenerate at zero', not
> > −∞. The conclusion (no two-sided f corridor, 1337) stands; the stated reason holds at one of the
> > two f openings."*
>
> And it was computed earlier still, in the conversation "The Method 1.6" at message 1957, in the
> session that wrote the chapter: *"and 5f: p = 5−3−1 = 1. one rival could be below it — 4f, p = 0.
> **but 4f is FULL by the time 5f opens (Pa, Z=91), so it is not admissible.** the corridor is
> one-sided there too."* **Twelve messages later the chapter summary drops the 5f clause and carries
> only "at any f opening p = 0" — which is how the false premise reached §34.9 and register 1350.**
>
> **What survives as this file's own is narrower and should be stated as such:** the proof that the
> equivalence is general (a rival lies below an opening iff its node count is smaller), the check of
> it at all twenty-four openings, and the measurement below, which proves more than either the book
> or the record claims. **The second time in this pass that a search-first rule was under-applied.**

### And the measurement then proves something stronger than the book asserts

**L = −∞ at exactly five of the twenty-four openings: 1s, 2p, 3d, 4f and 5f.** So *"no rival lies
below"* is **not an f-only property** — it fires once for every ℓ, at that ℓ's node-floor member.

| ℓ | openings with L = −∞ | |
|---|---|---|
| s | 1 of 8 | 1s |
| p | 1 of 6 | 2p |
| d | 1 of 8 | 3d |
| **f** | **2 of 2** | **4f, 5f — every one** |

**f is the only ℓ every one of whose openings is outside the domain**, and that is what *"f is
outside the domain"* is true of. s, p and d each lose their node-floor member and keep the rest. f
loses both, 4f by the floor and 5f by exhaustion. **The reason f loses both is that f arrives late
enough for every node-floor subshell to have closed before its second member opens.**

**What is owed on §34.9, and it is M's.** The conclusion stands. The reason must change, and it was
already known when the chapter was written. The true reason covers both f openings in one clause and
proves the stronger claim as well:

> *At an opening, the rivals below the entrant are exactly the admissible subshells of smaller node
> count. At 4f there are none, because zero is the floor. At 5f there are none because every
> subshell of smaller node count is full. f is the only ℓ of which that is true at every opening,
> and that is what puts f outside the domain.*

---

## What is untouched

**Register 1333's 8 / 6 / 4 partition stands**, measured exact by finding R4-01, and nothing here
disputes it. **No placement policy is chosen here**: the eighteen belong to `walk.py`'s own minimum-
distance rule, and register 1580's three-value piercing set is a different question with a different
answer. **§34.8's figures 1.028 and 1.785 are not touched**; the record carries them as 34re-04
UNREPRODUCIBLE and they stay there.

**Nothing is repaired.**
