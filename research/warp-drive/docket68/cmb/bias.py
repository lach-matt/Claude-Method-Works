#!/usr/bin/env python3
"""
bias.py -- H-CONSCIOUS-SELECTS reading (b) priced at the READ outcome-bias sizes (O9).

Not seated; verified once (2026-10-05), its findings applied; first-written claims kept under HISTORY.  M (rulings item
54): "3, then 2, then 1 please" -- step 2: READ Bosch-Steinkamp-Boller 2006's effect size and price reading (b)'s channel
at it.  Reading (b) (unobserved.py section 6): a conscious selection that moves Alice's outcome probability from 1/2 to
(1 +- eps)/2 while keeping the correlations shifts Bob's marginal by (eps/2) E(a,b) -- a channel of 1 - H((1 - eps)/2)
bits per entangled pair.  Reading (a), Born selection, is its own reading of M's hypothesis: no channel, Bob's marginal
independent of Alice's setting (computed, below).  Carried as M's hypothesis, never as a result.  O9 stays OPEN.

    python3 bias.py              report
    python3 bias.py --selftest   checks, with CONTROLS
    python3 bias.py --json       the numbers as JSON

WHAT IS READ (2026-10-05; routes recorded; the primary meta-analysis is behind APA's paywall and was NOT read)
  * Bosch, Steinkamp & Boller 2006, Psychol. Bull. 132, 497 -- public APA abstract: 380 studies, 'a significant but very
    small overall effect size', 'strongly and inversely related to sample size', 'extremely heterogeneous', and all of
    it 'could in principle be a result of publication bias'.  The NUMBERS are SECONDARY-READ: Wilson & Shadish's comment
    (APA; search excerpt only -- the landing page is paywalled, reported, not routed around): the fixed-effects mean is
    'slightly less than the null value (0.499997, i.e., slightly fewer 1s than 0s)'; the Psi Encyclopedia (SPR) gives the random-effects mean as '(0.500035) across 380 studies' and the
    fixed-effect result as '(z = -3.67, p < 0.001)'.  Both means cover all 380 studies: the 'reversal' is a choice of
    MODEL (H-RE-VS-FE), not of studies.  The bit-weighted fixed-effect mean is the natural per-trial eps; the random-
    effects mean averages per-study effect sizes, driven by the small studies.  (The SPR's UK page frames the same number
    as highly significant: the SPR frames it both ways, verifier-READ.)
  * The largest RNG data: Alexander 2019, J. Sci. Explor. 33(3) (open; verifier-READ) -- positive at 200 bits per trial,
    'negative in direction' at 2 million, 'the bit-wise effect decreased by 33 times'.  PEAR, Jahn et al. 1997 abstract
    (pear-lab.com, verifier-READ): 'of the order of 10-4 bits deviation per bit processed'; Jahn et al. 2000 PortREG
    abstract (verifier-READ): the replication 'failed by an order of magnitude to attain that of the prior experiments, or
    to achieve any persuasive level of statistical significance'.
  * Maier, Dechamps & Pflitsch 2018, Front. Psychol. 9:379 (CC BY; Firecrawl): a quantum RNG; participants 'passively
    observed'; the study 'focused on unconsciously affected intentional states ... using a rather indirect manipulation'
    (verifier-READ); 'A total of 100 trials were performed on each participant' (verifier-READ); sequential Bayes with a
    stopping rule at BF 10, prior delta ~ Cauchy(0, 0.1) 'selected before data collection', one-tailed: 'The final
    Bayesian one sample t-test (one-tailed) with 12,571 participants revealed a BF01 of 10.07 for H0. The mean score for
    positive stimuli for all participants was M = 50.02%, SD = 5.06'.  The raw data (Zenodo 10.5281/zenodo.14184851, md5
    cc5b41dcc944f25d5b373dd076483f35, as Zenodo publishes it) give M = 50.0177 %, SD = 5.0617 (VERIFIER-COMPUTED; the
    paper's 50.02 is rounded).  Their post-hoc 'non-random oscillative structure' is carried with Grote 2018 (Front.
    Psychol. 9:1350, CC BY, verifier-READ): a permutation reanalysis puts it at p = 0.328, 'no statistical evidence'.
    Fig. 2 and 4 captions say 12,529 participants; the text and raw data 12,571.
  * Radin, Nelson, Dobyns & Houtkooper 2006's reply: an author-posted copy exists, but it is the APA-typeset version and
    whether APA's posting policy covers it is not established -- NOT USED.  Dobyns et al. 2004 (MegaREG) -- NAMED-NOT-READ.

THE TRANSFER, AND THE PRICING'S OWN HYPOTHESES
  pi is a hit rate on RNG bits; reading (b) needs a bias on Alice's outcome for one half of an entangled pair: eps = 2 pi
  - 1 under H-EFFECT-TRANSFER-RNG, keeping the correlations under H-BIAS-KEEPS-CORRELATION.  Pricing per pair assumes one
  constant bias per trial (H-EPS-CONSTANT-PER-TRIAL); the psi side's own model is a constant z per session, z not
  growing with sample size (H-Z-PER-SESSION), under which a channel is priced per act of intention, not per pair.
  Maier's manipulation was implicit: their null bears on reading (b), which is conscious and agentive, only through
  H-IMPLICIT-TO-CONSCIOUS.

NAMED HYPOTHESES
  H-PI-IS-HIT-RATE, H-RE-VS-FE, H-MAIER-PROPORTION (M is the proportion of positive -- goal-congruent under an implicit
  induction -- outcomes), H-IMPLICIT-TO-CONSCIOUS, H-EFFECT-TRANSFER-RNG, H-EPS-CONSTANT-PER-TRIAL, H-Z-PER-SESSION; with
  H-BIAS-KEEPS-CORRELATION and H-BIASED-SELECTION (unobserved.py) and M's H-CONSCIOUS-SELECTS.

HISTORY (verifier, 2026-10-05; first-written claims kept)
  * 'sign reversed with the three largest studies' -- the fixed-effect and random-effects means both cover all 380; the
    reversal is the model.  The fixed-effect row (eps = -6.0e-6) is now carried.
  * Maier's participants were taken to intend an outcome ('fits a participant who intends an outcome'): the manipulation
    was implicit.  M 50.02 was used for 50.0177; the trial count was inferred (~98) where 100 is printed.
  * the eps = 0 'control' was 1 - H(1/2) = 0 by arithmetic; now reading (a)'s marginal spread, computed through nosig.
  * 'trials to measure eps at 3 sigma' is a median z of 3 (50 % power); the 90 % figure is printed beside it.
  * 'very strong evidence for a null effect' needs its prior and its tail: the Bayes factor is recomputed here at three
    priors and at a point alternative of Bosch's size.
"""

import contextlib
import importlib.util
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _by_path(key, path):
    if key in sys.modules:
        return sys.modules[key]
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    spec.loader.exec_module(mod)
    return mod


with contextlib.redirect_stdout(io.StringIO()):
    unobserved = _by_path("cmb_unobserved", os.path.join(HERE, "unobserved.py"))

BOSCH = {"pi_random_effects": 0.500035, "pi_fixed_effect": 0.499997, "z_fixed_effect": -3.67, "studies": 380,
         "route": "SECONDARY-READ: Wilson & Shadish 2006 search excerpt (both means); Psi Encyclopedia (SPR) (0.500035, "
                  "z = -3.67); the primary (APA) not read"}
PEAR_1997_EPS_ORDER = 2e-4      # 'of the order of 10-4 bits deviation per bit processed' (verifier-READ): pi - 1/2 ~ 1e-4
MAIER = {"N": 12571, "trials": 100, "M_paper": 50.02, "SD_paper": 5.06, "M_raw": 50.0177, "SD_raw": 5.0617,
         "BF01": 10.07, "prior_r": 0.1,
         "route": "READ: Front. Psychol. 9:379 (2018), CC BY; raw values VERIFIER-COMPUTED from Zenodo 14184851"}


def eps_from_pi(pi):
    return 2 * pi - 1


def maier_interval(raw=True):
    m = (MAIER["M_raw"] if raw else MAIER["M_paper"]) / 100
    sd = (MAIER["SD_raw"] if raw else MAIER["SD_paper"]) / 100
    se = sd / math.sqrt(MAIER["N"])
    eps, s_eps = eps_from_pi(m), 2 * se
    return {"eps": eps, "sigma_eps": s_eps, "upper95": eps + 1.96 * s_eps, "lower95": eps - 1.96 * s_eps,
            "binomial_sd_at_100": math.sqrt(0.25 / MAIER["trials"]), "total_trials": MAIER["N"] * MAIER["trials"],
            "binomial_sigma_eps": 1 / math.sqrt(MAIER["N"] * MAIER["trials"])}


def maier_bayes(r, point=None, raw=False, n=40000):
    """BF01 for Maier's one-sample one-tailed test, normal approximation: d_hat = (M - 50)/SD, likelihood N(d_hat; delta,
    1/N); H1 a half-Cauchy(0, r) on delta > 0 (Maier's prior at r = 0.1), or a point alternative.  Their 10.07 at r = 0.1
    is the check.  The integral runs to d_hat + 12/sqrt(N), beyond which the likelihood is below e^-72."""
    m = MAIER["M_raw"] if raw else MAIER["M_paper"]
    sd = MAIER["SD_raw"] if raw else MAIER["SD_paper"]
    d, s = (m - 50) / sd, 1 / math.sqrt(MAIER["N"])
    lik = lambda delta: math.exp(-0.5 * ((d - delta) / s) ** 2)
    if point is not None:
        return lik(0.0) / lik(point)
    hi = d + 12 * s
    h = hi / n
    tot = 0.0
    for i in range(n + 1):
        x = i * h
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        tot += w * lik(x) * 2 / (math.pi * r * (1 + (x / r) ** 2))
    return lik(0.0) / (tot * h / 3)


def priced():
    mi = maier_interval()
    cases = [("Bosch 2006 random-effects mean (SECONDARY)", eps_from_pi(BOSCH["pi_random_effects"])),
             ("Bosch 2006 fixed-effect mean (SECONDARY)", eps_from_pi(BOSCH["pi_fixed_effect"])),
             ("PEAR 1997, order of magnitude", PEAR_1997_EPS_ORDER),
             ("Maier 2018 central (raw data)", mi["eps"]),
             ("Maier 2018 95 % upper bound", mi["upper95"])]
    o9 = unobserved.o9_pricing(eps_list=tuple(abs(e) for _, e in cases))
    rows = []
    for (name, e), r in zip(cases, o9["capacity_rows"]):
        rows.append({"case": name, "eps": e, "bits_per_pair": r["bits_per_pair"],
                     "small_eps_approx": e * e / (2 * math.log(2)),
                     "bits_per_pair_fixed_bias_switch": r["bits_per_pair_fixed_bias_switch"],
                     "pairs_for_species_count": r["pairs_for_species_count"],
                     "pairs_per_bit_at_capacity": 1.0 / r["bits_per_pair"]})
    # trials: sigma_eps = 2 sqrt(p(1-p)/N) = 1/sqrt(N) at p = 1/2; a median z of 3 is (3/eps)^2 (50 % power), 90 %
    # power at 3 sigma is ((3 + 1.2816)/eps)^2
    need = {"%.1e" % e: {"median_z3": (3.0 / e) ** 2, "power90_z3": ((3.0 + 1.2816) / e) ** 2}
            for e in (7.0e-5, 6.0e-6, 1.0e-5)}
    bayes = {"r=%g" % r: maier_bayes(r, raw=True) for r in (0.01, 0.1, 0.707)}
    bayes["r=0.1 from the paper's rounded M, SD"] = maier_bayes(0.1)
    bayes["point at Bosch's size (raw)"] = maier_bayes(None, point=eps_from_pi(BOSCH["pi_random_effects"]) / 2
                                                       / (MAIER["SD_raw"] / 100), raw=True)
    return {"maier": mi, "maier_paper": maier_interval(raw=False), "rows": rows, "trials_for_3sigma": need,
            "species_bits": o9["species_bits"], "reading_a_marginal_spread": o9["max_marginal_shift_a"],
            "bayes": bayes, "shifts_reading_b": o9["shifts_reading_b"]}


def compute():
    return priced()


def report():
    d = compute()
    mi, mp = d["maier"], d["maier_paper"]
    print("H-CONSCIOUS-SELECTS reading (b) at the READ bias sizes (verified once; not seated)\n")
    print("Reading (a), Born selection: Bob's marginal spread over Alice's settings %.1e -- no channel; every null below "
          "is what it predicts" % d["reading_a_marginal_spread"])
    print("Bosch et al. 2006, all 380 studies (SECONDARY): random-effects pi %.6f -> eps %+.1e; fixed-effect pi %.6f -> "
          "eps %+.1e (z = %.2f, contrary to intention); the model is the difference (H-RE-VS-FE)" % (
              BOSCH["pi_random_effects"], eps_from_pi(BOSCH["pi_random_effects"]), BOSCH["pi_fixed_effect"],
              eps_from_pi(BOSCH["pi_fixed_effect"]), BOSCH["z_fixed_effect"]))
    print("Maier et al. 2018 (implicit manipulation, quantum RNG, N %d x %d trials = %d): eps %+.2e +- %.2e, 95 %% "
          "[%.2e, %.2e] (raw data); from the paper's rounded M: %+.1e" % (
              MAIER["N"], MAIER["trials"], mi["total_trials"], mi["eps"], mi["sigma_eps"], mi["lower95"],
              mi["upper95"], mp["eps"]))
    print("    binomial check: SD at 100 trials %.2f %% vs %.2f %% observed; binomial sigma_eps %.2e" % (
        100 * mi["binomial_sd_at_100"], MAIER["SD_raw"], mi["binomial_sigma_eps"]))
    print("    BF01 (normal approximation, one-tailed): " + ", ".join("%s: %.2f" % (k, v) for k, v in d["bayes"].items()))
    print("\nreading (b) priced (bits per entangled pair; species count %.2e bits; H-EPS-CONSTANT-PER-TRIAL):" %
          d["species_bits"])
    for r in d["rows"]:
        print("    %-44s eps %+.1e: %.2e bits/pair (fixed bias + switch %.2e); %.2e pairs per bit; %.2e pairs" % (
            r["case"], r["eps"], r["bits_per_pair"], r["bits_per_pair_fixed_bias_switch"],
            r["pairs_per_bit_at_capacity"], r["pairs_for_species_count"]))
    print("trials to measure eps at 3 sigma (sigma_eps = 1/sqrt(N)): " + "; ".join(
        "eps %s: median z 3 at %.1e, 90 %% power at %.1e" % (k, v["median_z3"], v["power90_z3"])
        for k, v in d["trials_for_3sigma"].items()))


def selftest():
    n_pass = n_fail = n_ctl = 0
    structural = []

    def chk(label, ok, ctl=False):
        nonlocal n_pass, n_fail, n_ctl
        n_ctl += ctl
        n_pass += bool(ok)
        n_fail += (not ok)
        print("  %s %s%s" % ("ok  " if ok else "FAIL", "CONTROL: " if ctl else "", label))

    d = compute()
    mi = d["maier"]
    b = d["rows"][0]
    chk("the Bayes factor recomputed from Maier et al.'s raw M, SD, N and their prior (r = 0.1) reproduces their BF01 "
        "10.07 within 3 %% (%.2f; from the rounded 50.02, %.2f)" % (d["bayes"]["r=0.1"],
                                                                  d["bayes"]["r=0.1 from the paper's rounded M, SD"]), abs(d["bayes"]["r=0.1"] / MAIER["BF01"] - 1) < 0.03)
    chk("Maier et al.'s SD is binomial at their 100 trials within 2 %% (%.3f vs %.3f %%)" % (
        100 * mi["binomial_sd_at_100"], MAIER["SD_raw"]), abs(100 * mi["binomial_sd_at_100"] / MAIER["SD_raw"] - 1) < 0.02)
    # 1e-4, not 1e-6: at eps = 6e-6 the capacity 1 - H((1-eps)/2) ~ 2.6e-11 is a difference of numbers near 1, so double
    # precision leaves ~2e-6 relative (first written 1e-6, which failed there)
    chk("unobserved.py's capacity agrees with the small-eps law eps^2/(2 ln 2) to 1e-4 relative at every READ eps",
        all(abs(r["bits_per_pair"] / r["small_eps_approx"] - 1) < 1e-4 for r in d["rows"]))
    chk("the fixed-bias-plus-switch capacity equals the chosen-bias capacity at every READ eps (1e-4 relative)",
        all(abs(r["bits_per_pair_fixed_bias_switch"] / r["bits_per_pair"] - 1) < 1e-4 for r in d["rows"]))
    chk("reading (a): Bob's marginal is independent of Alice's setting, computed through nosig.joint (%.1e < 1e-12)" %
        d["reading_a_marginal_spread"], d["reading_a_marginal_spread"] < 1e-12, ctl=True)
    chk("a point alternative at Bosch's size is uninformative in Maier's data (BF01 %.2f within [0.5, 2])" %
        d["bayes"]["point at Bosch's size (raw)"], 0.5 < d["bayes"]["point at Bosch's size (raw)"] < 2)
    structural.append("eps = 2 pi - 1 (%.1e at Bosch's random-effects mean) is arithmetic; its transfer to an entangled "
                      "pair is H-EFFECT-TRANSFER-RNG, its constancy per trial H-EPS-CONSTANT-PER-TRIAL" % b["eps"])
    structural.append("Maier et al.'s manipulation was implicit: their null bears on reading (b), conscious and agentive, "
                      "only through H-IMPLICIT-TO-CONSCIOUS")
    structural.append("Bosch's own abstract: the effect 'could in principle be a result of publication bias' -- then "
                      "eps = 0; reading (b) stays M's hypothesis either way, and reading (a) is untouched by every null")
    for s in structural:
        print("  STRUCTURAL: " + s)
    print("bias.py: %d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute(), indent=1, default=str))
    else:
        report()
