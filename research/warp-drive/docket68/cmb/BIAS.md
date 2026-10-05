# Reading (b) priced at the measured bias sizes (H-CONSCIOUS-SELECTS; verified once; SEATED in ledger.py section 8h on M's "Seat both", item 55; 2026-10-05)

*First headed* "(H-CONSCIOUS-SELECTS; verified once; not seated; 2026-10-05)".

## What M asked

M's order (rulings item 54) was *"3, then 2, then 1 please"*. This file is step 2: read Bösch, Steinkamp & Boller
2006's effect size, and price reading (b)'s channel at it.

**H-CONSCIOUS-SELECTS has two readings** (`unobserved.py`, section 6):
- **Reading (a), Born selection.** Conscious selection follows the Born rule. Bob's marginal is independent of Alice's
  setting (spread 1.1×10⁻¹⁶, computed here through `nosig.py`), so there is no channel.
- **Reading (b), biased selection.** A conscious selection moves Alice's outcome probability from ½ to (1 ± ε)/2 while
  keeping the correlations. That gives a channel of 1 − H((1 − ε)/2) bits per entangled pair.

**Every null result below is what reading (a) predicts.** Evidence against a large ε in reading (b) is not evidence
against M's hypothesis under reading (a).

Both are carried as M's hypothesis, never as results. **O9 stays OPEN.**

Every number below is printed by `bias.py`.
- **Selftest:** 6/6 checks, 1 of them a control, with 3 STRUCTURAL lines printed and not counted.
- **Pricing:** it asks `unobserved.py` for the pricing itself.
- **Verification:** it was verified once, and its findings are applied.

## What was READ, and by which route

### Bösch, Steinkamp & Boller 2006 (Psychol. Bull. 132, 497)

**The primary is behind APA's paywall and was not read.** What was read:

- **The public APA abstract:**
  - 380 studies, with "a significant but very small overall effect size";
  - effect sizes "strongly and inversely related to sample size" and "extremely heterogeneous";
  - all of this "could in principle be a result of publication bias".
- **The numbers, at second hand** (SECONDARY-READ):
  - Wilson & Shadish's comment (a search excerpt only; APA's landing page is paywalled, reported, not routed around):
    the fixed-effects mean is "slightly less than the null value (0.499997, i.e., slightly fewer 1s than 0s)".
  - The Psi Encyclopedia (SPR) gives the random-effects mean, "(0.500035) across 380 studies", and the fixed-effect
    result, "(z = -3.67, p < 0.001)".
- **Both means cover all 380 studies.** The "reversal" is a choice of *model* (H-RE-VS-FE), not of which studies are
  included.
  - The fixed-effect mean weights each bit, so it is the natural per-trial ε.
  - The random-effects mean averages per-study effect sizes, which the small studies drive.
- **The SPR frames the same number both ways.** Its UK page calls it highly significant (verifier-READ).

### The largest RNG data (verifier-READ, open)

- **Alexander 2019 (J. Sci. Explor. 33(3)).** The effect is positive at 200 bits per trial and "negative in direction" at
  2 million; "the bit-wise effect decreased by 33 times".
- **PEAR, Jahn et al. 1997 (abstract, pear-lab.com):** "of the order of 10-4 bits deviation per bit processed".
- **PEAR, Jahn et al. 2000 (PortREG abstract):** the replication "failed by an order of magnitude to attain that of the
  prior experiments, or to achieve any persuasive level of statistical significance".

### Maier, Dechamps & Pflitsch 2018 (Front. Psychol. 9:379)

Open access (CC BY).
- **The manipulation was implicit.** Participants "passively observed", and the study "focused on unconsciously affected
  intentional states … using a rather indirect manipulation" (verifier-READ).
- **Design.** A quantum random-number generator; "A total of 100 trials were performed on each participant"; 12,571
  participants; sequential Bayesian testing stopping at a Bayes factor of 10; a prior δ ~ Cauchy(0, 0.1) "selected
  before data collection"; and a one-tailed test.
- **Result:** *"BF01 of 10.07 for H0. The mean score for positive stimuli for all participants was M = 50.02%, SD =
  5.06"*.
- **Raw data.** Zenodo 10.5281/zenodo.14184851, md5 as Zenodo publishes it. It gives M = 50.0177 % and SD = 5.0617
  (verifier-computed). The paper's 50.02 is rounded.
- **The post-hoc "non-random oscillative structure"** in their abstract is carried together with Grote 2018 (Front.
  Psychol. 9:1350, CC BY). A permutation reanalysis puts it at p = 0.328, "no statistical evidence".
- **A count discrepancy.** The Fig. 2 and Fig. 4 captions say 12,529 participants. The text and the raw data say 12,571.

### Not used, or not read

- **Radin, Nelson, Dobyns & Houtkooper's 2006 reply.** An author-posted copy exists, but it is APA's typeset version,
  and whether APA's posting policy covers it is not established. Not used.
- **Dobyns et al. 2004 (MegaREG).** NAMED-NOT-READ.

## Computed

### The bias sizes

| source | ε | note |
|---|---|---|
| Bösch 2006, random-effects mean | **+7.0×10⁻⁵** | second-hand; driven by small studies |
| Bösch 2006, fixed-effect mean | **−6.0×10⁻⁶** | second-hand; z = −3.67, contrary to intention |
| PEAR 1997 | ~ +2×10⁻⁴ | order of magnitude; not replicated in 2000 |
| Maier 2018, raw data | **+3.5×10⁻⁴ ± 9.0×10⁻⁴** | 95 % interval [−1.42×10⁻³, +2.12×10⁻³]; implicit manipulation |

### Maier et al.'s Bayes factor, and what it is sensitive to

- **The recomputation reproduces theirs.** From the raw data, the Bayes factor against an effect is **10.08** at their
  prior (r = 0.1); the paper's rounded M gives 9.60.
- **It depends on the prior:** 1.59 at r = 0.01, and 70.5 at r = 0.707.
- **Against an effect of Bösch's size it is 0.97** (point alternative): no evidence either way.
- **So their "very strong evidence for a null effect"** is evidence against effects of order δ ≈ 0.1 under their
  one-sided prior. At Bösch's size it is uninformative.
- **Two more qualifications:**
  - one-tailed means the test says nothing about ε < 0;
  - Maier's null bears on reading (b), which is conscious, only through H-IMPLICIT-TO-CONSCIOUS.
- **The trial count checks out.** Their SD is what 100 binomial trials give, within 1.2 % (5.00 vs 5.06 %).

### The channel at those sizes (H-EPS-CONSTANT-PER-TRIAL)

The species count is 9.51×10²⁷ bits.

| case | ε | bits per entangled pair | pairs per bit, at capacity | pairs for the species count |
|---|---|---|---|---|
| Bösch, random-effects | +7.0×10⁻⁵ | 3.53×10⁻⁹ | 2.83×10⁸ | 2.69×10³⁶ |
| Bösch, fixed-effect | −6.0×10⁻⁶ | 2.60×10⁻¹¹ | 3.85×10¹⁰ | 3.66×10³⁸ |
| PEAR 1997 (order) | +2.0×10⁻⁴ | 2.89×10⁻⁸ | 3.47×10⁷ | 3.30×10³⁵ |
| Maier, central | +3.5×10⁻⁴ | 9.04×10⁻⁸ | 1.11×10⁷ | 1.05×10³⁵ |
| Maier, 95 % upper | +2.1×10⁻³ | 3.25×10⁻⁶ | 3.07×10⁵ | 2.92×10³³ |
| reading (a), or ε = 0 | 0 | 0 | — | no channel |

- **A fixed bias works as well as a chosen one.** At every ε, an unwilled bias plus a setting switch gives the same
  capacity.
- **The capacity depends on |ε|, so the sign does not matter.**

### What it takes to measure ε

The binomial error is σ_ε = 1/√N.

| ε | trials for a median z of 3 (50 % power) | trials for 90 % power at 3σ |
|---|---|---|
| 7.0×10⁻⁵ | 1.8×10⁹ | 3.7×10⁹ |
| 1.0×10⁻⁵ | 9.0×10¹⁰ | 1.8×10¹¹ |
| 6.0×10⁻⁶ | 2.5×10¹¹ | 5.1×10¹¹ |

Maier et al. ran 1,257,100 trials. The bit-weighted data behind the fixed-effect mean are what point to |ε| ≈ 6×10⁻⁶,
with the sign against intention. The primaries for those data (MegaREG) are named, not read.

## The hypotheses the pricing rests on

- **H-EFFECT-TRANSFER-RNG.** π is a hit rate on a random-number generator's bits. That a bias there carries over to
  Alice's outcome on an entangled pair is a hypothesis.
- **H-BIAS-KEEPS-CORRELATION.** The biased selection keeps the correlations.
- **H-EPS-CONSTANT-PER-TRIAL.** Pricing per pair assumes one constant bias per trial.
  - **The psi side's own model is different (H-Z-PER-SESSION).** A constant z per session, with z not growing with sample
    size. Under it, a channel would be priced per act of intention, not per pair, and the numbers above would not apply.
- **H-IMPLICIT-TO-CONSCIOUS.** This is how Maier's implicit-manipulation null bears on a conscious selection.
- **H-RE-VS-FE.** Which of Bösch's two means is the per-trial ε.

## For M

- **Under reading (a), Born selection, nothing here applies.** Every null is what it predicts, and there is no channel.
- **Under reading (b), the channel depends on which measured size is taken.**
  - Bösch's random-effects mean, +7×10⁻⁵, gives about 3.5×10⁻⁹ bits per pair.
  - The bit-weighted fixed-effect mean, −6×10⁻⁶, against intention, gives about 2.6×10⁻¹¹.
  - Each needs between 10³⁶ and 10³⁹ pairs for the species count.
- **No size is established.**
  - Bösch's abstract allows publication bias.
  - The two means disagree in sign.
  - PEAR's effect did not replicate.
  - The largest study with open data (Maier) has an implicit design. Its null is uninformative at Bösch's size.
- **If the psi side's own model holds (a fixed z per session), the per-pair pricing does not apply at all.** A different
  channel model would be needed. That is OPEN.

## Named hypotheses

- H-PI-IS-HIT-RATE.
- H-RE-VS-FE.
- H-MAIER-PROPORTION. M is the proportion of positive outcomes: goal-congruent under an implicit induction.
- H-IMPLICIT-TO-CONSCIOUS.
- H-EFFECT-TRANSFER-RNG.
- H-EPS-CONSTANT-PER-TRIAL and H-Z-PER-SESSION.
- From `unobserved.py`: H-BIAS-KEEPS-CORRELATION and H-BIASED-SELECTION.
- M's: H-CONSCIOUS-SELECTS.

## OPEN

1. **Bösch et al.'s primary,** with both estimates and their intervals. It is behind APA's paywall.
2. **The MegaREG primary** (Dobyns et al. 2004), and Radin et al.'s reply by a route whose permission is established.
3. **A channel model under H-Z-PER-SESSION:** what a per-act-of-intention effect would carry.
4. **Any measurement of an intention bias on an entangled-pair outcome,** with conscious intention.

## History

### Before any report

- **A binomial-plausibility check** with an arbitrary window was moved to STRUCTURAL.
- **"Preregistered"** was removed. The open text states that the prior was chosen before the data and that the test was
  one-tailed, not that the study was preregistered.

### Verifier, 2026-10-05

- **The sign.** It said Bösch's sign is *"reversed with the three largest studies"*. Both means cover all 380 studies;
  the reversal is the model. The fixed-effect row is now carried.
- **Maier's participants.** It said Chalmers–McQueen's agentive bias *"fits a participant who intends an outcome"*, and
  read Maier's participants that way. Their manipulation was implicit.
- **Maier's numbers.** M 50.02 was used, which is rounded (the raw value is 50.0177). The trial count was inferred
  (~98) where the text prints 100.
- **The control.** The *"ε = 0 gives no channel"* control was 1 − H(½) = 0 by arithmetic. It is now reading (a)'s
  marginal, computed through `nosig.py`.
- **The trial counts.** *"Trials to measure ε at 3σ"* gave a median z of 3, i.e. 50 % power. The 90 % figure is now
  beside it.
- **The Bayes factor.** *"Very strong evidence for a null effect"* now carries its prior, its tail, and its lack of
  sensitivity at Bösch's size.
- **Reading (a)** had been reduced to an "ε = 0" row. It now has its own place.
- **The psi side.** PEAR 1997 and 2000, Alexander 2019, and Maier's oscillation together with Grote's reanalysis are
  now carried.
- **Quotation length.** The Psi Encyclopedia quotation was a full sentence from a copyrighted page. It is trimmed to
  short phrases.
- **A tolerance.** The small-ε check's tolerance was first 10⁻⁶. It failed at ε = 6×10⁻⁶ by floating-point cancellation,
  and it is now 10⁻⁴.
