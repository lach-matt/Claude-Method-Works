# FINDING — α, AND THE 'WHY' OF n+l
# SESSION 64. The live scientific thread. Instrument: pack64/alpha.py.
# THIS FILE IS THE ONE TO READ FIRST IN s65. Everything else in pack64 is closed.

## 0 · WHY THIS THREAD EXISTS, AND WHAT IT REPLACED
Sessions 44-64 closed costs: rungs, bounds, controls, ledgers. **None of that answers
Löwdin.** The Challenge asks for the Madelung rule *ab initio* — and the ledger,
however complete, delivers a parameter-free DEMONSTRATION, not an EXPLANATION. The
assembly says so itself in §0: what is derived is that the ordering follows from the
field, not that it follows from an inequality on n and l. M ruled the session onto the
explanation. This is where it got to.

## 1 · THE REPARAMETRISATION (M's, and it is the move that opened the problem)
Order channels by **n + αl** and ask what the field permits for α.
    hydrogen        α = 0 EXACTLY. E(2s)=E(2p) to 2 µHa (s63 Rung 5). One electron,
                    no screening, l weightless — the unbroken Coulomb degeneracy.
    Madelung        α = 1.
**'Why n+l' becomes 'why does α land on 1'.** That question is quantitative and this
project's sealed data can attack it. The previous form could not be attacked at all.

## 2 · WHAT α = 1 *IS*. NOT A CALIBRATION — A CRITICAL VALUE.
Two channels sharing n+l differ by (Δn,Δl) = (+1,−1). Under n+αl the LOWER-n channel,
which Madelung's tie-break requires first, wins **iff α < 1**.
    α < 1  → tie-break holds        α > 1  → tie-break fails        α = 1 → degenerate

**MEASURED, AND IT IS TOTAL:** every α=1 bound the interval method finds, in both
directions, comes from an equal-n+l pair. Share = **1.000** (`alpha.py sources`). Not
one cross-block pair produces a bound at 1.

**α = 1 IS THE CRITICAL VALUE OF THE TIE-BREAK CLAUSE AND IS NOTHING ELSE.**

Consequence, and it is the first real explanation this project has produced:
  * The ORDERING clause compares whole blocks. Coarse, wide tolerance in α, 119 rows,
    zero inversions. **That is what a law looks like.**
  * The TIE-BREAK clause is the assertion α < 1 strictly, about a quantity the field
    puts AT 1 — at Z=57, 81, 113 the permitted interval collapses to exactly [1,1],
    pushed against 1 from both sides within the same atom. **A rule perched on its own
    critical value is not a law. It is a marginal case, and marginal cases fall both
    ways on details that have nothing to do with n or l.**
  * **NO BETTER COMPUTATION COULD HAVE RESCUED IT.** That answers Löwdin rather than
    reporting to him, and it is the honest content of s63's two-laws restatement.

## 3 · α IS SET BY SCREENING. MEASURED, NOT ARGUED.
Isoelectronic sweep, Ne core held FIXED, only the nuclear charge varying
(`alpha.py iso`). q = Z_nuc − 10 is the net charge the outer electron sees:

        q      α(s→p)    α(p→d)
        3       0.427     0.692
        6       0.295     0.480
       10       0.214     0.334
       16       0.157     0.229

α falls monotonically toward 0 as the ion is stripped — the Coulomb degeneracy
reasserting itself. **α rises as screening rises.** And the periodic table is built
entirely at **q = 1**, the maximum-screening end of every isoelectronic sequence:

    42 measurements at q=1 from the sealed chain (`alpha.py ratios`)
    median α = 1.0816    mean 1.1120    83% at α ≥ 1

**The neutral limit is where α ≈ 1.** Madelung's rule is the rule of NEUTRAL ATOMS
specifically, and n+l is what α ≈ 1 reads as on integers.

## 4 · TWO THINGS THAT ARE **NOT** DERIVED. STATED PLAINLY.

**(a) α = Δδ IS DERIVED. Δδ ≈ 1 IS NOT.**
In quantum-defect form E(n,l) = −1/2(n−δ_l)², one unit of n is one unit of effective
quantum number and one unit of l is δ_l − δ_{l+1}. Hence **α = Δδ**, the quantum-defect
decrement. It checks against measured spectra: potassium gives Δδ(s→p) = 0.47 against
our 0.5214 at Z=20. **That step is a derivation.** What sets Δδ ≈ 1 is not.

**(b) THE ORTHOGONALITY-COUNTING ARGUMENT FAILED AND IS WITHDRAWN.**
Proposed in session: δ_l counts the core shells of the same l the valence orbital must
be orthogonal to; shells of angular momentum l begin at n = l+1; so N_l − N_{l+1} = 1
by counting, hence α = 1. **TESTED AND FALSIFIED** (`alpha.py ratios`, last block):

    dN = 1   n=8    median α 1.092
    dN = 2   n=34   median α 1.077

dN does not discriminate. **The counting story is wrong and is not carried forward.**
Something else sets Δδ. This is the open problem.

## 5 · THE 17%, WHICH IS NOT NOISE
Seven of 42 measurements have α < 1. **Six are the s→p transition and every one of
those is an alkaline earth** (Z = 4, 12, 20, 38, 56, 88); the seventh is 5p→d at Xe.

    Z=4  0.483   Z=12 0.592   Z=20 0.521   Z=38 0.534   Z=56 0.518   Z=88 0.608
    Z=54 5p→d 0.676

**α(s→p) ≈ 0.5 is not an anomaly — it is the known spectroscopy** (K: Δδ(s→p)=0.47,
Δδ(p→d)=1.46). **α is not one number. It depends on l:** ≈0.5 for s→p, ≈1.1–1.5 once
d and f are involved. And that is the shape the result needs, because the tie-break
pair in each block spans a specific pair of l values:

    n+l = 4,5,6   pairs span s↔p and p↔d, low l      α < 1  → tie-break HOLDS
    n+l = 7,8     pairs are 4f/5d and 5f/6d, d↔f     α > 1  → tie-break FAILS

**The tie-break dies at n+l = 7 and 8 because those are the first blocks whose
competing pair spans d and f.** Not a fact about heavy elements. A fact about which
l values collide.

## 6 · THE ONE TEST FOR SESSION 65, AND THE DEFECT THAT BLOCKS IT
The claim of §5 must be checked **at the Z where each block actually opens**, not at
whatever atom α happened to be measurable. `alpha.py blocks` does this and **returns
NO-DATA at every block**, correctly and by design: the ratio measure needs a base
channel (n,l), and at Z_open that channel is already full, so there is no denominator.

**s65's first task is to define a continuous α valid at Z_open with the base channel
unavailable, and re-run `alpha.py blocks`.** The prediction to file BEFORE running:

    T-B  For every equal-n+l block the chain reaches, α evaluated at that block's own
         opening Z is < 1 exactly where the lower-n channel enters first, and > 1
         exactly where it does not. 11 blocks. **PREDICTED: agreement at 11 of 11.**
    FALSIFIER: any block where α and the observed first-entry order disagree → α does
         not govern the tie-break and §2 must be withdrawn, not reinterpreted.

That test is cheap — sealed data, no solves — and it either converts §5 from a pattern
into a result, or kills it.

## 7 · WHAT WOULD FINISH THE DERIVATION
Δδ. Everything above reduces the Challenge to a single question: **what sets the
quantum-defect decrement, and why is it near 1 at neutrality?** The counting argument
is dead (§4b). The remaining route is the radial equation itself — the centrifugal
term l(l+1)/2r² against a well that is −Z/r inside the core and −1/r outside, with the
defect set by the phase accumulated in the crossover region. That is analytic work, it
does not fit the predict-run-score machinery, and it may not come off.

**IF IT DOES NOT COME OFF, THE HONEST OUTCOME IS TO PUBLISH THE DEMONSTRATION AND
STATE THE WHY AS OPEN.** That is still more than the field has: no one has previously
shown the ordering survives with zero empirical input and every approximation costed,
nor reproduced La and Ac unprompted, nor bounded the exception class. §2 of this file
stands on its own regardless of §7.
