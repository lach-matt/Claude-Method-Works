#!/usr/bin/env python3
"""
bias.py -- H-CONSCIOUS-SELECTS reading (b) priced at the READ outcome-bias sizes (O9).

Not seated; not yet verified.  M (rulings item 54): "3, then 2, then 1 please" -- step 2: READ Bosch-Steinkamp-Boller
2006's effect size and price reading (b)'s channel at it.  Reading (b) (unobserved.py section 6): a conscious selection
that moves Alice's outcome probability from 1/2 to (1 +- eps)/2 while keeping the correlations shifts Bob's marginal by
(eps/2) E(a,b) -- a channel of 1 - H((1 - eps)/2) bits per entangled pair.  unobserved.py priced it at chosen eps;
this file prices it at the eps the READ intention-on-RNG literature supports.  Carried as M's hypothesis, never as a
result.  O9 stays OPEN.

    python3 bias.py              report
    python3 bias.py --selftest   checks, with CONTROLS
    python3 bias.py --json       the numbers as JSON

WHAT IS READ (2026-10-05; routes recorded; the primary meta-analysis is behind APA's paywall and was NOT read)
  * Bosch, Steinkamp & Boller 2006, Psychol. Bull. 132, 497 -- public APA abstract (psycnet.apa.org record
    2006-08436-001): 380 studies, 'a significant but very small overall effect size', 'strongly and inversely related to
    sample size', 'extremely heterogeneous', and a Monte Carlo showing all three 'could in principle be a result of
    publication bias'.  The NUMBER is SECONDARY-READ: Psi Encyclopedia (SPR, open; Firecrawl 2026-10-05): 'A recent,
    determinedly conservative meta-analysis found a significant effect size (0.500035) across 380 studies, although this
    finding remains ambiguous, as the outcome is reversed when three large experiments with negative effects sizes are
    included (z = -3.67, p < 0.001).'  A search excerpt of Wilson & Shadish's comment (APA, paywalled landing page --
    reported, not routed around) shows the same '(0.500035)'.  So pi = 0.500035 is a hit rate on intended outcomes
    (H-PI-IS-HIT-RATE), and its sign reverses with the largest studies.
  * Maier, Dechamps & Pflitsch 2018, Front. Psychol. 9:379 (CC BY; Firecrawl 2026-10-05): a quantum RNG, an online
    sample of 12,571, sequential Bayes with a stopping rule at BF 10: 'The final Bayesian one sample t-test (one-tailed)
    with 12,571 participants revealed a BF01 of 10.07 for H0. The mean score for positive stimuli for all participants
    was M = 50.02%, SD = 5.06, providing very strong evidence for a null effect'.  The interval on eps below is computed
    here from M, SD and N (H-MAIER-PROPORTION: M is the proportion of RNG-selected outcomes the participant intended).
  * Radin, Nelson, Dobyns & Houtkooper 2006 reply (title only); Bosch et al.'s rejoinder 'In the eye of the beholder'
    (title only).  NAMED-NOT-READ.

THE TRANSFER (H-EFFECT-TRANSFER-RNG)
  pi is a hit rate on a random-number generator's bits, intention-aligned; reading (b) needs a bias on Alice's outcome
  for one half of an entangled pair.  eps = 2 pi - 1 maps the one onto the other.  That the RNG bias, if real, carries
  over to a measurement on an entangled qubit is a NAMED hypothesis, as is the bias keeping the correlations
  (H-BIAS-KEEPS-CORRELATION, unobserved.py).  Chalmers-McQueen's biased variant is agentive (unobserved.py), which fits
  an intending participant.

NAMED HYPOTHESES
  H-PI-IS-HIT-RATE, H-MAIER-PROPORTION, H-EFFECT-TRANSFER-RNG; with H-BIAS-KEEPS-CORRELATION and H-BIASED-SELECTION
  (unobserved.py) and M's H-CONSCIOUS-SELECTS.
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

BOSCH_PI = {"pi": 0.500035, "reversed_with_largest_z": -3.67, "studies": 380,
            "route": "SECONDARY-READ: Psi Encyclopedia (SPR), EECS article; Wilson & Shadish 2006 search excerpt; the "
                     "primary (APA) not read"}
MAIER = {"N": 12571, "M_percent": 50.02, "SD_percent": 5.06, "BF01": 10.07,
         "route": "READ: Front. Psychol. 9:379 (2018), CC BY, Results ('Final Sample')"}


def eps_from_pi(pi):
    return 2 * pi - 1


def maier_interval():
    m = MAIER["M_percent"] / 100
    se = MAIER["SD_percent"] / 100 / math.sqrt(MAIER["N"])
    eps, s_eps = eps_from_pi(m), 2 * se
    return {"eps": eps, "sigma_eps": s_eps, "upper95": eps + 1.96 * s_eps, "lower95": eps - 1.96 * s_eps,
            "trials_per_participant_if_binomial": 0.25 / (MAIER["SD_percent"] / 100) ** 2}


def priced():
    mi = maier_interval()
    cases = [("Bosch 2006 random-effects pi 0.500035 (SECONDARY)", eps_from_pi(BOSCH_PI["pi"])),
             ("Maier 2018 central estimate", mi["eps"]),
             ("Maier 2018 95 % upper bound", mi["upper95"])]
    o9 = unobserved.o9_pricing(eps_list=tuple(abs(e) for _, e in cases))
    rows = []
    for (name, e), r in zip(cases, o9["capacity_rows"]):
        rows.append({"case": name, "eps": e, "bits_per_pair": r["bits_per_pair"],
                     "small_eps_approx": e * e / (2 * math.log(2)),
                     "bits_per_pair_fixed_bias_switch": r["bits_per_pair_fixed_bias_switch"],
                     "pairs_for_species_count": r["pairs_for_species_count"],
                     "pairs_per_bit_at_capacity": 1.0 / r["bits_per_pair"]})
    # eps = 0: Bob's marginal shift (eps/2) E vanishes, and so does the capacity 1 - H(1/2)
    control = max(abs(r["shift_per_eps"]) * 0.0 for r in o9["shifts_reading_b"]) + (
        1 + sum(q * math.log2(q) for q in (0.5, 0.5)))
    # trials to measure eps at 3 sigma: sigma_eps = 2 sqrt(p(1-p)/N) = 1/sqrt(N) at p = 1/2
    need = {"%.0e" % e: (3.0 / e) ** 2 for e in (7.0e-5, 1.0e-5)}
    return {"maier": mi, "rows": rows, "trials_for_3sigma": need, "species_bits": o9["species_bits"], "control_eps0_bits": control,
            "shifts_reading_b": o9["shifts_reading_b"]}


def compute():
    return priced()


def report():
    d = compute()
    mi = d["maier"]
    print("H-CONSCIOUS-SELECTS reading (b) at the READ bias sizes (not verified; not seated)\n")
    print("Bosch et al. 2006: pi = %.6f -> eps = %.1e (sign reversed with the three largest studies, z = %.2f); "
          "publication bias could account for it (abstract)" % (BOSCH_PI["pi"], eps_from_pi(BOSCH_PI["pi"]),
                                                               BOSCH_PI["reversed_with_largest_z"]))
    print("Maier et al. 2018 (sequential Bayes stopping at BF 10, quantum RNG, N %d, BF01 %.2f): eps = %.1e +- %.1e; 95 %% "
          "interval [%.1e, %.1e]; SD %.2f %% is binomial for ~%.0f trials per participant" % (
              MAIER["N"], MAIER["BF01"], mi["eps"], mi["sigma_eps"], mi["lower95"], mi["upper95"],
              MAIER["SD_percent"], mi["trials_per_participant_if_binomial"]))
    print("\nreading (b) priced (bits per entangled pair; pairs for the species count, %.2e bits):" % d["species_bits"])
    for r in d["rows"]:
        print("    %-52s eps %.1e: %.2e bits/pair (fixed bias + switch %.2e); %.2e pairs per bit; %.2e pairs" % (
            r["case"], r["eps"], r["bits_per_pair"], r["bits_per_pair_fixed_bias_switch"],
            r["pairs_per_bit_at_capacity"], r["pairs_for_species_count"]))
    print("    eps = 0 (the publication-bias reading, and reading (a)): %.1e bits/pair -- no channel" %
          d["control_eps0_bits"])
    print("trials to measure eps at 3 sigma (binomial, sigma_eps = 1/sqrt(N)): " + ", ".join(
        "eps %s: %.1e" % (k, v) for k, v in d["trials_for_3sigma"].items()) +
          "; Maier et al. at ~%.0f trials each: ~%.1e" % (mi["trials_per_participant_if_binomial"],
                                                         MAIER["N"] * mi["trials_per_participant_if_binomial"]))


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
    chk("eps from pi: 2 x 0.500035 - 1 = %.2e (= 7.0e-5)" % b["eps"], abs(b["eps"] - 7.0e-5) < 1e-12)
    chk("unobserved.py's capacity at that eps agrees with the small-eps law eps^2/(2 ln 2) to 1e-6 relative (%.4e vs "
        "%.4e)" % (b["bits_per_pair"], b["small_eps_approx"]),
        abs(b["bits_per_pair"] / b["small_eps_approx"] - 1) < 1e-6)
    chk("the fixed-bias-plus-switch capacity equals the chosen-bias capacity at every READ eps",
        all(abs(r["bits_per_pair_fixed_bias_switch"] / r["bits_per_pair"] - 1) < 1e-6 for r in d["rows"]))
    chk("eps = 0 gives no channel (%.1e bits/pair)" % d["control_eps0_bits"], d["control_eps0_bits"] < 1e-100,
        ctl=True)
    chk("Maier et al.'s 95 %% interval on eps contains 0 [%.1e, %.1e] and contains Bosch's eps 7.0e-5" % (
        mi["lower95"], mi["upper95"]), mi["lower95"] < 0 < mi["upper95"] and mi["lower95"] < b["eps"] < mi["upper95"])
    structural.append("pi is a hit rate on RNG bits; that it transfers to an outcome on one half of an entangled pair "
                      "is H-EFFECT-TRANSFER-RNG, and that the bias keeps the correlations is H-BIAS-KEEPS-CORRELATION")
    structural.append("Maier et al.'s SD %.2f %% is what a binomial proportion gives at ~%.0f trials per participant; "
                      "the trial count was not READ" % (MAIER["SD_percent"], mi["trials_per_participant_if_binomial"]))
    structural.append("Bosch's own abstract: the effect 'could in principle be a result of publication bias' -- then "
                      "eps = 0 and reading (b) has no measured support; reading (b) stays M's hypothesis either way")
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
