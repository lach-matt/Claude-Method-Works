import re
s=open('mkmd2.py').read()

# --- load data4 alongside the others
s=s.replace("E = json.load(open('/home/claude/paper/data3.json'))",
            "E = json.load(open('/home/claude/paper/data3.json'))\n"
            "F = json.load(open('/home/claude/paper/data4.json'))")

# --- version bump and subtitle
s=s.replace("Draft v2.0. Prepared with a computing collaborator under the protocols of The Method v1.4.\nSupersedes v1.x, *The closure defect of an index*.",
            "Draft v3.0. Prepared with a computing collaborator under the protocols of The Method v1.4.\n"
            "Supersedes v2.0. Every correction in Part XI post-dates that draft.")

# --- 1.6: add the third possibility, that a vocabulary may not be indexable at all
old="**No third mode was found.**"
new=("**A vocabulary may also not be indexable at all.** V2 of Part VIII has four terms: two are "
     "non-operative, one belongs elsewhere, and one — field content — is **categorical**. Ordering it "
     "is arbitrary, and E depends on the choice: six of twenty-four orderings close it and eighteen do "
     "not. **E is defined only where the terms are graded and related.** Given a bag of unrelated "
     "categorical scope conditions, the operator returns a number that depends on how the bag was sorted.\n\n"
     "**No third failure mode was found.**")
assert old in s; s=s.replace(old,new,1)

# --- Part II: Lambda is not the clean case
old2="""![The tower]({FIG}f2_1.png)

### 2.2 Why it closes"""
new2="""![The tower]({FIG}f2_1.png)

### 2.1b And it closes in every coupling scheme

The tower as built uses LS coupling within the core and jK pair coupling to the outer electron. That is
one of four standard schemes — LS, LK, jK and jj — and **the scheme is not a coordinate.**

Rebuilt in all four with a uniform one-parameter looseness convention:

{hdr(['scheme','Λ₁₃ cells','E at every level'])}
{chr(10).join(row([k, f(v), 0]) for k,v in F['schemes']['cells_L13'].items())}

**Closure is not scheme-contingent.** Cell counts differ by more than a factor of two and E is zero
throughout, because every scheme is a chain of vector-coupling bounds whose *loose* form binds one
coordinate by a monotone function of one other — §1.8's condition.

> **What is scheme-contingent is what the letters mean.** 2K is J_c + ℓ_outer in jK, L_total + S_core
> in LK, and jj has no K at all. The tower carries an unstated jurisdiction.

*A first run reported the alternatives as failing. It had applied two-parent bounds to them and
one-parent bounds to jK, and the difference was my convention, not the schemes.*

### 2.2 Why it closes"""
assert old2 in s; s=s.replace(old2,new2,1)

# --- Part VIII vocabulary section: replace the seven-vocabulary table
old3="""{hdr(['vocabulary','terms'])}
{row(['V1 laws','the fifteen letters'])}
{row(['V2 theory','causal, field content, interacting, d > 2'])}
{row(['V3 geometry','flat, asymptotically flat, simply connected, globally hyperbolic, generic'])}
{row(['V4 algebra','determinism, ultralocality, stability, vacuum lowest energy, vacuum not annihilated'])}
{row(['V5 coupling','minimal coupling'])}
{row(['V6 solution','self-consistent semiclassical'])}
{row(['V7 degeneracy','non-degenerate higher-derivative'])}

**No vocabulary can fully state any charger. Zero of {len(SY['spans'])}, minimum span two.**"""
new3="""**The partition is not seven and it is not mine.** A locally covariant QFT is a functor
**A : Loc → Alg** (Brunetti–Fredenhagen–Verch 2003), and that object has exactly four parts: the source
objects, the target objects, the functor itself, and functionals on the target.

{hdr(['vocabulary','what it is','terms'])}
{chr(10).join(row([a,b,', '.join(c[:5])+(', …' if len(c)>5 else '')]) for a,b,c in F['bfv']['parts'])}

**Three of my seven vocabularies dissolve.** ξ and degeneracy are parameters of the *theory* — they sit
in the Lagrangian, so they determine the functor. V2 was the functor itself, described by a list of
properties rather than graded, which is exactly why it was not an index.

**And the terms that refuse to place are relations**, not properties:

{chr(10).join('- '+r for r in F['bfv']['relations'])}

> That is why V6 looked like a vocabulary and why it "carried the conjecture." **The self-consistent
> achronal ANEC is not a property of a universe. It is a relation between a spacetime and a state** —
> G(g) = 8π⟨T⟩_ψ — and a relation cannot be a coordinate of either side.

Two hesitations resolve by derivation. **ξ belongs to T**, since it changes the action. **NEC_pt belongs
to S**, since ⟨T_μν⟩k^μk^ν is a functional on the algebra evaluated at a state.

**No vocabulary can fully state any charger. Zero of {len(SY['spans'])}, minimum span two.**"""
assert old3 in s; s=s.replace(old3,new3,1)

# --- Part VIII: Hartman is not vacuous
old4="""Hartman is **vacuous in this index**: its trigger is ANEC violation and its jurisdiction is flat spacetime, and ANEC
violation requires curvature. The two are mutually exclusive, so the charge never fires."""
new4="""**Hartman is not vacuous — it fires, in flat spacetime.** Computed in a V1 × V3 product built *without*
its content pre-loaded, it excludes exactly the flat, ANEC-violating, currency-unpaid cells. An earlier
version of this section reported it as vacuous, on a computation that had built the cross-edge
*ANEC violation → curvature or topology* into the index — which is Hartman's contrapositive and more.
**The conclusion had been assumed in the premise.**

What is true is narrower and leaves the consequence intact: **its jurisdiction is FLAT = 0, and the
wormhole question lives at FLAT ≥ 1.** The edge exists and does not span the distance.

Two further precisions. **ANEC violation does not require curvature** — a flat spacetime with a
compactified dimension violates it by the Casimir effect. The correct antecedent is *curvature or
non-trivial topology*, and that disjunction makes the V1–V3 cross-edge **itself arity 3**, with minimal
supports {{NEC_pt, FLAT, CONN}} and {{X_exp, FLAT, CONN}}. **The system has two independent arity-3
obstructions: one inside V1, one on the edge.**

And **Hartman's V2 dependence is spurious.** Its own appendix shows the inequality holds for free
scalars, and 2d has its own results rather than a counterexample. Operatively it spans V1 + V3 only, so
the cycle it creates is not real: 7 nodes, 7 edges, 1 component, 1 cycle. **The graph is connected and
the path does not reach the destination.**"""
assert old4 in s; s=s.replace(old4,new4,1)

# --- Part VIII coverage: correct the ANEC figure
old5="""Indexed by geometry, field content, coupling, curvature and backreaction, the available proofs cover a fraction of
the cases, and **every curved-space proof crosses at the same place — free, minimally coupled fields** — just as
every path from source to target in Λ₉ crosses at **q**, the unique articulation point separating the two halves of
the lattice. Extending any single proof relaxes one pin and leaves the other."""
new5="""Indexed by geometry × field content × coupling × backreaction, the eight covered cases form a **closed**
index — E = {F['anec_index']['E']}, box {F['anec_index']['box']}, no non-monotone relations — and the
coverage is {F['anec_index']['covered']} of {F['anec_index']['cases']} cases.

**But the fraction misleads.** Non-minimal coupling is covered **nowhere**:
{F['anec_index']['coup1_covered']} of {F['anec_index']['coup1_total']} cases. And that is not an absence
of effort — Urban and Olum's counterexample is a non-minimally coupled scalar in conformally flat
spacetime, where the ANEC is **violated**, and Fewster notes state-independent QEIs can fail there.

> **COUP = 1 is a wall, not a frontier. The coverage boundary is the boundary of where the condition is
> true**, and ANEC coverage is essentially complete on the domain where the ANEC holds.

*An earlier version reported coverage as 30 of 48 and claimed every curved-space proof crosses at
*free, minimally coupled*. Only* minimally coupled *is shared — curved and interacting is covered, by
Wall and by Iizuka — and the Λ₉ articulation analogy does not hold, since COUP = 1 has no traffic at all.*"""
assert old5 in s; s=s.replace(old5,new5,1)

open('mkmd2.py','w').write(s)
print('patched: 6 corrections applied')