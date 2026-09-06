# F67.4 — THE Δδ MEASUREMENT BASIS IS A 10% SAMPLE, FILTERED BY THE SAME `fail` SET
# THAT F67.2 SHOWED TO BE UNRELIABLE — AND THE FILTER RUNS ALONG THE EXACT AXIS THE
# FINDING MEASURES.
# Raised 2026-08-20, SESSION 67, on M's ruling that items 1 and 2 are to be done ONLY
# IF ITEM 3 (Δδ) REQUIRES THEM. This file is the test of that condition.
# Counts and sets off sealed rows, Standing 5. NO solve was run. No prediction was
# needed; nothing here is scored. No sealed file is edited.

## THE DEPENDENCE, TRACED IN FOUR STEPS
  1. `FINDING-ALPHA-THE-WHY.md` §4(a): **α = Δδ is DERIVED.** Δδ ≈ 1 is not, and that
     one quantity is the whole remaining distance to Löwdin (§7).
  2. α is measured by `pack64/alpha.py ratios` as
     α = [D(n,l+1) − D(n,l)] / [D(n+1,l) − D(n,l)], read off `rows[Z]['order']`.
  3. **A channel in `rows[Z]['fail']` is ABSENT from `order`.** The triple is then
     skipped silently — `if a in D and b in D and cc in D`. No warning, no count.
  4. F67.2 established at Z=51 5d that a channel in `fail` may be **present in the
     field and findable**. `fail` is therefore not a physical exclusion. It is, at
     least in part, an instrument artefact.

**So the question "does item 3 require items 1 and 2" is the question "how much of α's
sample does that artefact remove". It is measurable, and here it is.**

## THE MEASUREMENT — sealed rows only

    α triples surviving into the finding                        42
    α triples BLOCKED by a channel in `fail`                   377
    of which blocked by a failed d channel                     351
    distinct Z at which at least one α triple is blocked        94

**The finding rests on 42 of 419 — a ten per cent sample.** The other 90% is not
"missing data" in the ordinary sense: it is a null produced by the solver, and every
one of those nulls is a place where the field has a value the instrument did not return.

## AND THE FILTER IS NOT UNIFORM. IT RUNS ALONG l — WHICH IS §5's ENTIRE CLAIM.

    transition   surviving   blocked   survival        median α of survivors
    s -> p               6         6      50.0%              0.5276
    p -> d              19       149      11.3%              1.0688
    d -> f              17       222       7.1%              1.5017

**Survival falls monotonically with l, and median α rises monotonically with l, across
the same three points.** A factor of seven in survival between the transition with the
lowest α and the transition with the highest.

`FINDING-ALPHA-THE-WHY.md` §5 reads exactly this l-dependence as the result:
*"α is not one number. It depends on l: ≈0.5 for s→p, ≈1.1–1.5 once d and f are
involved ... The tie-break dies at n+ℓ = 7 and 8 because those are the first blocks
whose competing pair spans d and f."* **That is the load-bearing sentence of the whole
'why', and it is measured across three samples whose survival rates differ by 7×,
filtered by a mechanism now known to be partly artefact.**

## WHAT THIS DOES **NOT** SAY
It does **not** say §5 is wrong. The confound runs both ways and that is stated plainly:
higher-l channels are more diffuse, and diffuseness plausibly drives BOTH the
convergence failure AND the defect decrement. If so the correlation is physical and §5
stands. **Nothing here distinguishes the two, and no attempt is made to — that would be
proposing a mechanism in the session that raised the doubt (F65.1).**

What it says is narrower and harder: **the sample is not known to be unbiased, the bias
would run along the measured axis, and the finding does not currently state this.**

## THE ANSWER TO M's CONDITION — YES, ITEM 3 REQUIRES ITEM 2
Item 1 (the single Z=51 5d confirming solve) is a ledger question and Δδ does not
depend on it. **Item 2 does.** The sweep answers the only question that decides whether
§5 survives:

  * **If the CLASS C rate across the failure population is ~0**, the exclusion is
    PHYSICAL — the field genuinely does not hold those states findably — the filter is
    a fact about atoms rather than about the solver, and §5 stands with the survival
    rates stated beside it. **That is itself a Löwdin-relevant statement**, because it
    says the missing α values are missing for the same reason the tie-break is marginal.
  * **If the CLASS C rate is material**, α's sample is filtered by the solver, the
    l-dependence in §5 is not established, and it must be re-measured on the recovered
    channels before any analytic §7 work is aimed at "why Δδ ≈ 1" — because that target
    would be a number produced by a bracket walk.

**Either outcome is worth the cost, and the cost is small: ~3 s a cell on the sealed
scan.** The sweep classifies; it does not recover. Recovering an α value additionally
needs a converged solve per channel, which is the expensive kind — that is a SECOND
decision, to be taken only if the C rate warrants it and only on the cells that warrant
it, and it is not proposed here.

## SCOPE THE SWEEP WOULD NEED — STATED BEFORE IT IS RULED ON
The blocked triples are not only d. α(d→f) needs f channels, and the sealed chain's
untouched failure population is:

    d node-count failures   162   (38 now measured: 37 CLASS B, 1 CLASS C)
    f node-count failures   149   (0 measured)
    g node-count failures    63   (0 measured)

d alone leaves the 222 d→f-blocked triples unexplained, and d→f is the transition with
BOTH the lowest survival and the highest α — the single most load-bearing cell of the
table above. **A d-only sweep cannot answer the question this fault raises.**

## STATUS
OPEN. M's ruling owed on the sweep's scope (d only / d+f / d+f+g) and on whether the
Z=51 ledger solve rides along. Nothing run, nothing predicted, nothing edited.
