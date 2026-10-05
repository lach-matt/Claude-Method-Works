# Reading (b) priced at the measured bias sizes (H-CONSCIOUS-SELECTS; not verified; not seated; 2026-10-05)

## What M asked

M's order (rulings item 54) was *"3, then 2, then 1 please"*. This file is step 2: read Bösch, Steinkamp & Boller
2006's effect size, and price reading (b)'s channel at it.

**What reading (b) is.** It comes from `unobserved.py`, section 6, and is M's H-CONSCIOUS-SELECTS taken as a biased
selection. A conscious selection moves Alice's outcome probability from ½ to (1 ± ε)/2 while keeping the correlations.
That shifts Bob's marginal by (ε/2)·E(a,b): a channel of 1 − H((1 − ε)/2) bits per entangled pair.

It is carried as M's hypothesis, never as a result. **O9 stays OPEN.**

Every number below is printed by `bias.py`.
- **Selftest:** 5/5 checks, 1 of them a control, with 3 STRUCTURAL lines printed and not counted.
- **Pricing:** it asks `unobserved.py` for the pricing itself.

## What was READ, and by which route

### Bösch, Steinkamp & Boller 2006 (Psychol. Bull. 132, 497)

**The primary is behind APA's paywall and was not read.** What was read:

- **The public APA abstract** (psycnet record 2006-08436-001):
  - 380 studies, with "a significant but very small overall effect size";
  - effect sizes "strongly and inversely related to sample size" and "extremely heterogeneous";
  - a Monte Carlo showing all of this "could in principle be a result of publication bias".
- **The number, at second hand** (SECONDARY-READ). The Psi Encyclopedia (Society for Psychical Research, open, via
  Firecrawl) writes: *"A recent, determinedly conservative meta-analysis found a significant effect size (0.500035)
  across 380 studies, although this finding remains ambiguous, as the outcome is reversed when three large experiments
  with negative effects sizes are included (z = -3.67, p < 0.001)."*
- **A second-hand match.** A search excerpt of Wilson & Shadish's comment shows the same "(0.500035)". Its APA landing
  page is paywalled; that is reported, not routed around.

### Maier, Dechamps & Pflitsch 2018 (Front. Psychol. 9:379)

Open access (CC BY), read via Firecrawl.

- **Design:** a quantum random-number generator, an online sample of 12,571, and sequential Bayesian testing with a
  stopping rule at a Bayes factor of 10.
- **Result:** *"The final Bayesian one sample t-test (one-tailed) with 12,571 participants revealed a BF01 of 10.07 for
  H0. The mean score for positive stimuli for all participants was M = 50.02%, SD = 5.06, providing very strong evidence
  for a null effect"*.

### Named, not read

Radin, Nelson, Dobyns & Houtkooper's 2006 reply, and Bösch et al.'s rejoinder *"In the eye of the beholder"*. Only
their titles were read.

## Computed

### The bias sizes

- **Bösch et al.** π = 0.500035 is a hit rate on intended outcomes (H-PI-IS-HIT-RATE). It gives **ε = 2π − 1 =
  7.0×10⁻⁵**. Its sign reverses when the three largest studies are included.
- **Maier et al.** From their M, SD and N: **ε = (4.0 ± 9.0)×10⁻⁴**, with a 95 % interval of
  [−1.4×10⁻³, 2.2×10⁻³] (H-MAIER-PROPORTION).
  - The interval contains both zero and Bösch's 7.0×10⁻⁵, so this large study can neither confirm nor exclude an
    effect of Bösch's size.
  - Their SD would be a binomial proportion's at about 98 trials per participant. The trial count was not read
    (STRUCTURAL).

### The channel at those sizes

The species count is 9.51×10²⁷ bits.

| case | ε | bits per entangled pair | pairs per bit, at capacity | pairs for the species count |
|---|---|---|---|---|
| Bösch 2006 (second-hand) | 7.0×10⁻⁵ | 3.53×10⁻⁹ | 2.83×10⁸ | 2.69×10³⁶ |
| Maier 2018, central | 4.0×10⁻⁴ | 1.15×10⁻⁷ | 8.66×10⁶ | 8.24×10³⁴ |
| Maier 2018, 95 % upper | 2.2×10⁻³ | 3.39×10⁻⁶ | 2.95×10⁵ | 2.80×10³³ |
| ε = 0 (publication bias; reading (a)) | 0 | 0 | — | no channel |

- **A fixed bias works as well as a chosen one.** At every ε, an unwilled bias toward "+" plus a setting switch gives the
  same capacity.
- **The small-ε law holds.** `unobserved.py`'s capacity matches ε²/(2 ln 2) to 10⁻⁶.

## The transfer is a hypothesis (H-EFFECT-TRANSFER-RNG)

- **π measures something else.** It is a hit rate on a random-number generator's bits. Reading (b) needs a bias on
  Alice's outcome for one half of an entangled pair. That a bias in the one, if real, carries over to the other is a
  named hypothesis.
- **So is keeping the correlations** (H-BIAS-KEEPS-CORRELATION).
- **The bias that fits is agentive.** Chalmers–McQueen's biased variant is agentive, which fits a participant who
  intends an outcome.

## For M

- **If the intention-on-RNG effect is real at Bösch's size, reading (b) gives a channel.** It carries about 3.5×10⁻⁹
  bits per entangled pair: some 2.8×10⁸ pairs per bit, and 2.7×10³⁶ pairs for the species count.
- **That size is not established.**
  - Bösch's own abstract says publication bias could account for it.
  - Its sign reverses with the three largest studies.
  - The largest study read (Maier, 12,571 participants) finds strong evidence for no effect, though its interval is too
    wide to exclude an effect of Bösch's size.
- **If ε = 0, reading (b) has no measured support and there is no channel.** It then stays your hypothesis, untested at
  the level that would matter.
- **What would settle it** is a measurement of ε, with its sign, at the size in question. Using the binomial standard
  error σ_ε = 1/√N:
  - Bösch's 7×10⁻⁵ at 3σ takes **1.8×10⁹ trials**;
  - 10⁻⁵ takes **9.0×10¹⁰ trials**.
  - Maier's 12,571 participants at about 98 trials each come to about 1.2×10⁶.

## Named hypotheses

H-PI-IS-HIT-RATE, H-MAIER-PROPORTION and H-EFFECT-TRANSFER-RNG. Also H-BIAS-KEEPS-CORRELATION and H-BIASED-SELECTION
(`unobserved.py`), and M's H-CONSCIOUS-SELECTS.

## OPEN

1. Bösch et al.'s primary text, with its fixed-effect estimate and its confidence interval. It is behind APA's paywall.
2. Radin et al.'s reply and Bösch et al.'s rejoinder. Only the titles were read.
3. Any measurement of an intention bias on an entangled-pair outcome, as opposed to an RNG bit.
4. Maier et al.'s trial count per participant.

## History

- **A selftest check** that Maier et al.'s SD was "binomial-consistent at a plausible session" used an arbitrary window.
  It was moved to STRUCTURAL before any report.
- **"Preregistered"** was first written for Maier et al.'s stopping rule. That word was not read in their text, and it
  was removed before any report.
