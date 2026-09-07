# PAPER-WORKSHOP.md — how `Cold_Fusion_v1.0` is made and checked

**This file exists because none of it belongs in the paper.**

Matter about the *process* of making a document — the ledger it draws on, the programs that render
and check it, the drafting history, the faults found and fixed on the way — is owed to the record and
not to the reader. A reader of the paper is owed its subject and owes nothing to its production. The
two were mixed in the first draft, in two whole sections and a dozen phrases, and this is where that
matter went.

**The separation is enforced.** `tools/audit_paper.py` runs a **WORKSHOP SEPARATION** check beside the
twenty-five audits, and a paper that has taken any of this back fails it. Its selftest plants a
workshop sentence in the paper to prove the check can fail, because a check that cannot fail is not a
check.

**Why it is beside the twenty-five and not one of them.** The Method's volumes are *about* their own
construction: the register, the audits, the corrections and the process that produced them are the
subject matter. No audit of theirs separates workshop from subject, because in that object there is
nothing to separate. A paper is not like that, so the separation is a requirement of this document and
not of the corpus — the same reason TERM MATCH is run beside the suite rather than inside it.

---

## What the paper is built from

**Every quantity is a ledger row.** `papers/CLAIMS.tsv` carries one row per stated quantity: value,
unit, status, provenance, and the computation that verifies it. `tools/verify_paper.py` runs three
passes over that ledger — it **recomputes** every `DERIVED` row from the instruments, **binds** every
cited constant to the instrument holding it, and fails on any number in the prose that no ledger row
carries.

**The paper's prose states no number of its own.** The source carries `[[C044]]` citations, which
`tools/render_paper.py` resolves against the ledger at render time. A sentence therefore cannot
acquire a figure the mathematics does not produce, because a sentence cannot hold a figure at all.
**This closes a weakness the working papers recorded and did not repair**: pass 3 is a *value* test
and not a *binding* test, and two wrong figures had passed it — three §9 quantities wrong by 1–5
percent, and a 0.855 that should have been 0.854.

**A status is never flattened.** A row's status travels with its value. Where the paper cites a figure
that is `WITHDRAWN`, `RECONSTRUCTED`, `PROJECTED`, `ASSUMED` or a `DESIGN` target, the renderer
**requires** the status to be printed beside it and refuses the citation otherwise. Every bracketed
status in the document is there because the mechanism would not let it be omitted.

**Four outputs, one source.** Markdown, HTML, `.docx` and PDF are emitted from the one resolved text,
which is what makes audit 16 FIDELITY hold by construction rather than by care.

## The residual the mechanism does not close

**The renderer makes a number with no ledger row impossible. It cannot make a citation of the *wrong*
row impossible.** That failure mode is real and has occurred: a cell of §5.4's table cited the
delivered work figure at the wider bore where it needed the same figure through the optimised target
— both valid rows, both the right shape, one of them wrong. It was caught by reading the rendered PDF.

**Audit 14 ARITHMETIC now closes most of it** by recomputing every cell of both restatement tables
from its own row and the factor that produces it, and returning FAIL with the cell named when one
disagrees. What remains open is a citation in *prose* rather than in a table, where no arithmetic
relation constrains it. **That is a recorded limit, not a repaired one.**

## The figures, and why they are generated

A figure is a claim in a different notation. Drawn by hand it could disagree with the prose beside it,
and nothing would catch that — the same weakness the citation mechanism closes for sentences. So
`tools/figures.py` draws every figure from `papers/CLAIMS.tsv` by claim id, exactly as the prose reads
it, and each figure **declares** the ids it uses. Its `--selftest` parses its own source, takes every
string passed to a text call, removes what a citation fills in, and requires **no quantity to
survive**: a figure cannot print a number it did not read from the ledger. Drawing coordinates are
exempt by construction, because they are not in strings.

They are emitted as PNG rather than SVG because PNG is the one raster form all four outputs embed the
same way, which is what lets audit 16 FIDELITY compare those outputs against each other.

## The mathematics, and how it is set

Two mechanisms, split by what each output can honestly do. **Inline** `$…$` is demoted to Unicode in
the one shared inline model, so all four outputs show the same symbols and none prints raw LaTeX at a
reader; a script converts only if *every* character can, because a half-converted subscript reads
worse than none. **Display** equations — a line that is nothing but a formula — are typeset by
matplotlib's mathtext and embedded as images, because an integral with limits and a sum over indices
cannot be built out of Unicode without lying about it.

One bug is worth recording because it was invisible in isolation: the brace form and the
single-character form of a subscript were applied in two passes, so a brace group that correctly fell
back to plain text was then picked up again by the second rule — turning `\lambda_{abs}` into a
half-converted `λₐbs`. They are one left-to-right pass now.

## Reproducing the paper

```
python3 tools/figures.py
python3 tools/render_paper.py papers/Cold_Fusion_v1.0.src.md --all
python3 tools/audit_paper.py
python3 tools/verify_paper.py papers/out/Cold_Fusion_v1.0.md
python3 tools/machine.py --selftest
python3 tools/collector.py --selftest
python3 tools/mucf.py --selftest
python3 tools/render_paper.py --selftest
python3 tools/figures.py --selftest
python3 tools/audit_paper.py --selftest
```

The audits are documented in `docs/AUDIT-PAPER.md`, which records what each of the twenty-five means
when the object is a paper rather than the volumes, and the three faults the suite found **in itself**
before it found any in the paper.

## What was removed from the paper, and where each piece went

| removed from | what it was | where it is now |
|---|---|---|
| the date line | a note that every quantity is a citation | above |
| the abstract's last sentence | the ledger and the binding | above |
| §5.1's pull-quote | *"the one place in this work where a model of ours is validated … against our own corpus"* | rewritten to state the validation without naming the corpus |
| §5.3 | *"an earlier reading of this work said otherwise"* | rewritten as a withdrawal of the figures in the superseded preprints, which is a scholarly notice rather than a drafting note |
| §5.4 | *"prices the first of them against the bred-fuel route only … an omission rather than a finding"* | above, in **What the paper is built from** |
| §7.3 | *"an earlier reconstruction of this work had wrong by nearly seven"* | the sourced figure stands; the history is here |
| §9.3 | *"the one figure in this work that the acceptance census rescales"* | rewritten as *a collection factor* |
| §11's opening | *"a finding is recorded, never repaired … what this paper's method forbids"* | the limits stand; the method's rule is here |
| **§12, in full** | *How this paper is verified* — the ledger, the three passes, the renderer, the statuses, the instruments | above |
| **§15, in full** | *The verification record* — the twenty-five audits, the numbering collision, the commands | above and in `docs/AUDIT-PAPER.md` |
| reference 17 | *"the corpus this paper's method and audit suite are drawn from"* | the citation stands; the note is here |

**Two things were kept in the paper deliberately, and they are not workshop matter.** A **withdrawal**
of a figure published in a cited preprint is a scholarly notice a reader is owed. And a **limit** on
what the paper establishes — §11 — is about the subject, not about the process, however much the two
resemble each other in tone.

## Corrections made during the rebuild, and what they cost

Four went into the paper and two into the instruments.

**The service-life caveat was wrong, and the correct one is narrower.** The draft carried the
companion's finding that the service-life model over-predicts its one checkable point by 2.24. That
figure was computed at a **superseded** sticking — 0.1487 percent through the excited-state channel —
and the main preprint's own §5.29 had already closed it by inverting the measured 150 cycles. At the
corrected sticking the model returns 152.8 cycles against 150, a ratio of 1.019. What the bound-case
rows actually assume is a fuel **density** of 8.5 × liquid where 1.2 has been reached, and carrying
them back multiplies each by 0.8038 — which takes the paper's headline device-internal result from
1.036 to **0.833**, and its best case from 1.231 to **0.990**. The correction makes the claim weaker
and more defensible at once: an unreached density is a stated experimental requirement, where a
mis-fitting model is a fault. `machine.py --alteration` now prints both columns, and the two stale
sites in the older preprints were annotated rather than overwritten.

**Theorem 1 closed on the wrong set.** The proof scanned every charged particle with a lifetime above
10⁻¹² s and called that list complete. It is not: Λc⁺, Ξc⁺ and Bc⁺ all sit above that threshold and
were absent. Running the lifetime test **first** repairs it, because that cut is closed — exactly five
charged particles outlive the mesomolecular formation time, and the set can be checked against the
Review of Particle Physics without judgement. Two of the five lie in the window; one survives the
hadron test. `window.py long_lived()` is the cut, and the selftest asserts it.

**Two numerals had been typed into the source**, both in the repaired Theorem 1 — the thresholds
10⁻¹² s and 10⁻²⁰ s. Audit 24 caught them, which is the audit's whole purpose: the source is supposed
to carry no numerals at all. The repair removed the need for either.

**The paper drew the wrong relation between two rows it cited correctly, at three sites.** §3, §11 and
§13.9 all said the two published final stickings *straddle* the break-point, so that measuring the
sticking would decide whether the heat form of condition 8 is met. It does not: the break-point is
0.1580 percent and the two effective values are 0.505 and 0.532, so it lies **below both**, and the
main preprint's own §5.5 had already said so in those words — *"Nothing straddles: the break-point is
not between the two readings, it is below both."* The heat form reaches 0.31 of what it needs on the
more favourable reading and is short by 3.37 on the other, and no choice between them repairs it. The
straddling reading was true of the *superseded* J=1 stickings, 0.1487 and 0.1851, which §5.26 retired.

**That one is the important entry in this list, because no audit caught it.** Every citation resolved
the right row; every arithmetic relation recomputed correctly; pass 3 found no unbacked number. A
sentence can cite two rows accurately and assert a false relation between them, and nothing in the
harness read the relation. Audit 14 now does: it carries a declared list of the **orderings the prose
depends on** — the break-point below each of the four sticking values, each density-carried figure
below the one it is carried from, each figure the paper states as clearing or not clearing unity —
and its selftest breaks one ordering on purpose. Ten orderings and nine thresholds, checked against
the ledger on every run.

**One ledger row duplicated another.** C843 and C176 were the same quantity — the service life at the
lower dissociation reading — computed by two hooks. C843 was dropped and C845's provenance rewritten
to name C176.

**What did not need fixing, and why it looked as though it did.** Pass 3 of `verify_paper.py` matches
a prose number against the ledger to within 2 percent, so a number can in principle be "carried" by an
unrelated row of similar value. That looseness governs the older preprints, whose prose holds literal
numerals. It cannot reach the consolidated paper: its source holds **no numerals at all**, so every
quantity is bound to a named row by id rather than matched by value.

## The correction that changed the answer

The rebuild's four corrections were all real, and one of them turned out to be the wrong correction to
a real problem. This is what was actually wrong.

**Every "bound case" balance in the record was computed at a retired sticking.** The balance has one
form, `G = N·V·η/E_π`, and running that expression backwards over the printed 90 % table recovers the
service life each cell used. The measured rows give 150, as they should. The bound-case rows give
**588.9** — and 588.9 is `N(0.1487 %, 8.5 LHD)`, the sticking `Cold_Fusion_Binder_Economy` §5.26
retires as an excited-state initial value multiplied by a ground-state survival fraction. At the
corrected value the same density returns **190.1**. Every bound-case figure in the record is therefore
high by **3.10**.

What that costs: the device-internal result. Recomputed rather than scaled, no heat form and no work
form clears unity in any configuration the paper can construct — the largest is **0.513**, reached
only by granting the optimised production target, the wider bore, the wider stopping window and an
unreached fuel density simultaneously. The 1.036 and 1.231 were the retired sticking and nothing else.

What it does not cost: anything computed at the measured cycle count, because those rows never used
the model. That asymmetry is the whole result — the surviving route is the one that asks for the
least.

**The previous pass's density correction was the wrong axis.** It carried bound-case figures back by
`N(0.505 %, 1.2) / N(0.505 %, 8.5)` — a ratio of corrected-sticking lives — applied to figures
computed at the retired one. The two corrections were being mixed. Once the sticking is right the
density buys very little on its own: 190.1 cycles against 150 measured, and only at a density nobody
has held.

**Two further faults fell out of the same reading.** `Cold_Fusion_Binder_Economy` §5.23 prints the
work balance as "0.3338 at the collector", but 0.3338 is that balance at **perfect** collection — it is
§5.19's own C219 with no efficiency applied, and the 90 % figure would be 0.3005. The acceptance
census restated it faithfully to the label rather than to the number, so C783 read 0.1174 where it
should read **0.1057**. And C840 was labelled "the neutron at its bare heat" when it is the
corrected-sticking heat balance through the optimised target, which is a different quantity.

**The instrument now computes rather than inherits.** `machine.py --corrected` evaluates
`G = N·V·η/E_π` directly over three products, four service lives and four collector configurations,
and its selftest asserts three things: that the expression reproduces every cell of the printed table,
that it does so at the retired sticking rather than the corrected one, and that no heat or work form
clears unity anywhere. `BALANCES_AT_90` stays in the file as the printed record the correction is
against — a status is never flattened, and neither is a table.

## The clause that hid the answer

The paper reported that no heat form and no work form clears unity, and stopped there. That is a
verdict, and the project asked for a specification. Running the balance backwards instead of forwards
found the answer sitting inside the paper's own arithmetic.

`G = N·V·η/E_π = 1`, solved for each term with the others held at the best configuration:

| term | requires | against | |
|---|---|---|---|
| service life `N` | 878.7 cycles | a cap of 198 | forbidden by 4.44 |
| collection `η` | 284.7 % | a fraction | forbidden |
| production cost `E_π` | 1.900 GeV | 11.13 measured, 4.69 optimised | open |
| value per fusion `V` | 152.7 MeV | 26.06 sourced | open |

Two of the four are closed by physics rather than by engineering. So a self-sustaining power source is
a statement about what a fusion is worth, and about nothing else — and `E_π` cannot carry it alone,
because 1.900 GeV is below even the optimised figure. The whole question is the blanket.

**`Cold_Fusion_Specification_and_Procedure` §5.1 had already reached that point and turned away from
it in half a sentence:** *"Breakeven would need a multiplication of 6.33 neutrons per source neutron —
beyond any (n,xn) blanket, and reachable only by fission, **which changes the product rather than the
yield**."* The first half is right. The second half is wrong, and it is the reason the answer was not
in the paper: fission in a **subcritical** blanket releases its energy as heat, on site, inside the
device. That is the product, not a change of it.

Inverting the subcritical relation `F = k/(ν(1−k))` — two sourced inputs, one geometric sum, no fitted
parameter — puts the requirement at **k between 0.469 and 0.770**, against 0.95 for an
accelerator-driven system and unity for a power reactor. The relation checks against a blanket the
paper already uses: the sourced fission-suppressed design's 1.6× multiplication sits at k ≤ 0.246,
which is where a design built to suppress fission belongs.

What it costs to say: the fusion then supplies 7.5–27.4 % of the recovered energy and all of the
neutrons, so the device is a fusion-driven subcritical fission reactor and not a fusion power plant.
Both halves are in §9.2 because neither stands alone. And the deciding comparison for a builder —
against a spallation-driven subcritical system on the same beam — is still unmade, and is now the
largest open item in the paper.

`tools/powersource.py` is the instrument. It runs the inverse rather than the forward balance, and its
selftest asserts that solving for a term and substituting it back returns exactly unity, that the two
closed axes are closed, that the relation reproduces the sourced blanket's regime, and that the
requirement lands deeply subcritical — plus the constructed case where it would not, so the result is
a fact about the numbers rather than a tautology.

## The comparison that dissolved

§11 had recorded, correctly, that the bred-fuel and power-source balances were never compared against
spending the same beam on a spallation-driven subcritical system — and that this was the largest open
item in the paper, because a simpler machine doing better would make the result true but pointless.

Making it found that the question was posed wrongly. **The muon channel does not replace spallation.**
The same protons strike the same target and make both, in the same collisions — which is the premise
§9.2 depends on in the first place. So the channel is *additive in neutrons* and there is no
alternative to price. What remains is one number: what pion-transparency costs the target's own
spallation yield, since a target the pions can escape from is narrower than a facility would otherwise
choose.

That reduces to `f < w·Y_fus/Y`, and `Y_fus` is already in the ledger — 52.41 neutrons per proton with
both collector alterations. Even against a very productive spallation target the requirement is only
that transparency cost stay under 21 %.

Three conservatisms all run the same way: a 14.1 MeV neutron counted as worth one spallation neutron
when it is worth more in a fast blanket; the alpha not counted; and transparency treated as a
straightforward loss, which in a blanket-coupled system it is not — an escaping neutron enters the
blanket rather than being lost.

**What survives as open is narrower and is stated as such**: what a spallation-optimised target at
8 GeV yields, and what transparency costs it. Both are ordinary target-design calculations outside
this corpus, and §10 Stage D measures the pair on one apparatus.

`tools/powersource.py --spallation` is the instrument; the selftest asserts the additive structure,
that the break-even falls as the spallation yield rises, and that taking the 14.1 MeV neutron at
worth one is the conservative choice rather than the flattering one.

## Closing the last two figures, and finding the second question was also posed wrongly

The spallation comparison left two target figures open, and they were the paper's last open items.
Both close, and the second closes by dissolving the way the first one did.

**What a spallation-optimised target returns** is not a mystery. A target thick enough to contain the
cascade degrades essentially all of the beam into it, and the neutron yield *per unit of energy
deposited* is a flat property of the material rather than of the machine — 25 to 30 per GeV for a
heavy metal. At 8 GeV: 200 to 240 neutrons per proton, which is the top of `--spallation`'s scan and
the place where the requirement on transparency is tightest.

**What transparency costs it** was the question that changed. The production target this work
specifies is the published mercury jet, and its two dimensions differ by two orders of magnitude
against the interaction length: 2.00 λ along the beam, 0.027 λ across. It stops 86.5 % of primaries
and retains 2.6 % of the cascade they start.

**So it is not a narrow spallation target — it is a production foil.** In a bare neutron source that
would be the whole of the loss, because the neutrons must be made in the target; there is nowhere
else. In a blanket-coupled system there is somewhere else. The cascade crosses into the blanket and
develops there, so the yield of the assembly is `E[φ·y_target + (1−φ)·y_blanket]` and the penalty
against a fully-containing target is `(1−φ)(1−y_blanket/y_target)` — **negative** for any blanket that
out-yields the target per GeV. Depleted uranium does, by about 1.5, giving −48.7 %: a gain.

**The load-bearing part is the sign, not the magnitude.** The penalty is exactly zero at parity and
turns positive only for a blanket *worse* per GeV than the target it replaces, which is not the
blanket §9.2 specifies. So the conclusion survives both sourced inputs being wrong by any amount short
of reversing that inequality — and the selftest asserts the sign turns at parity rather than anywhere
convenient.

**What is left is a margin rather than a question.** `--target`'s retention is geometry, not transport;
Proposition 10's blanket relation is point kinetics. Both are used as requirements rather than as
predictions, both say so where they appear, and §10 Stage D measures what they estimate — on one
apparatus, the same beam and the same blanket with the fuel cell in and out.
