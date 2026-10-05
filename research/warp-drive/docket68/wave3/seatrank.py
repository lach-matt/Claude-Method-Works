#!/usr/bin/env python3
"""
seatrank.py -- DOCKET 68 wave 3, W3C: ranking seats by signed magnitudes (M-RULINGS item 25, H-SEATRANK).

Not seated.  stdlib + numpy.  signed.py (Q-1s) is IMPORTED, never copied; outside results READ with the route recorded.

    python3 seatrank.py              report
    python3 seatrank.py --selftest   checks, with CONTROLS; STRUCTURAL items printed, never counted
    python3 seatrank.py --json       the numbers as JSON

M'S WORDS (M-RULINGS-2026-10-03.md item 25, verbatim)
  On "Those correlations are weak and fall off sharply with distance", M: "this is where the magnitude of probabilities
  (negative and positive), and complex binary come into play. The stronger negative magnitudes will automatically
  triangulate the stronger positive magnitudes which rank the probability of seating".

THE SETTING.  A quasi-probability w over candidate seats (signed weights summing to 1; Q-1s, signed.py).  A seat's rank
is its positive weight.  Four questions, each computed.

  (1) WHAT THE NEGATIVES FIX EXACTLY.  For any normalised w, the total positive weight is P = 1 + N, N the total negative
      magnitude (signed.pos's own identity, checked here over random quasi-distributions).  So stronger negative
      magnitudes DO force stronger positive magnitudes, automatically -- in aggregate.  This half of H-SEATRANK holds
      as an identity.
  (2) WHAT THE NEGATIVES DO NOT FIX ALONE.  Which seat ranks first.  Counterexample: w = (0.7, 0.5, -0.2) and
      w' = (0.5, 0.7, -0.2) share every negative entry and rank opposite seats first.  Over random quasi-distributions
      with the negative part held fixed and the positive entries permuted, the top seat moves (fraction computed; it
      tends to 1 - 1/n_pos).
  (3) WHAT PROJECTIONS ADD -- M'S TRIANGULATION.  When the quasi-distribution is a Wigner function, its projections are
      true probabilities, and filtered back-projection recovers the whole distribution -- negative region and
      positive peak together (signed.fbp, imported; signed.py's own result: negative-region IoU 1.000 at 180 angles,
      0.037 at 2).  Computed here for the state (|0> + |1>)/sqrt2 (signed.STATE_COEFFS 'sup01'): the location of the
      positive maximum (the top 'seat') and of the negative minimum, reconstructed against exact, as the number of
      projections grows.  So 'triangulate' is literal: the projections rank the seats, and they place the negatives in
      the same act.
  (4) THE COST UNDER WEAK CORRELATIONS.  Estimating a signed weight by sampling: Pashayan, Wallman & Bartlett,
      arXiv:1503.07525v2 (READ via alphaXiv): sampling seats with probability |w|/M, M = sum |w| (eq. 8, p.2; M = 1 iff
      w >= 0, p.2), and scoring M sign(w) gives an unbiased estimate (eq. 9, p.3); to precision eps with confidence
      1 - delta it needs s = (2/eps^2) M^2 ln(2/delta) samples (eq. 12, p.3).  With M = 1 + 2N, separating two seats
      whose weights differ by Delta (eps = Delta/2) needs s = 8 M^2 ln(2/delta) / Delta^2: STRONGER negative magnitudes
      make a weak difference COSTLIER to resolve, by M^2.  Computed, with an empirical check of the estimator.

  GRADE (for wave 3's verification, not seated): H-SEATRANK -- the aggregate statement holds as an identity (1); the
  per-seat ranking is not fixed by the negatives alone (2) but is recovered with them from projections (3); and
  stronger negativity raises, not lowers, the sampling cost of resolving a weak difference (4).  Moves no obstruction
  grade: it ranks seats, it supplies none (O-SEAT unchanged).

NAMED HYPOTHESES
  H-SEATRANK        (M, item 25) carried as M's hypothesis.
  H-SEAT-QUASI      the probability of seating is represented by a quasi-probability over candidate seats.
  H-WIGNER-SEATS    for (3): the seat quasi-distribution is a Wigner function, so its projections are measurable
                    probabilities; for a general quasi-distribution projections need not be non-negative.
  H-NOISELESS       (3) uses exact projections; signed.fbp_finite_sample relaxes it (signed.py's own result).
"""
import json
import math
import os
import random
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.abspath(os.path.join(HERE, ".."))
WD = os.path.abspath(os.path.join(D68, ".."))
for _p in (WD, D68):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import signed  # noqa: E402

RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
M_WORDS_25 = ("The stronger negative magnitudes will automatically triangulate the stronger positive magnitudes which "
              "rank the probability of seating")
PASHAYAN_2015 = {"source": "arXiv:1503.07525v2", "route": "READ via alphaXiv (answer_pdf_queries), pp.1-3, 6",
                 "used": "M = ||W||_1 >= 1, = 1 iff nonnegative (p.2); sampling |W|/M with estimator M Sign[W] is "
                         "unbiased (eqs. 8-9); s(eps, delta) = (2/eps^2) M^2 ln(2/delta) (eq. 12, p.3)"}


# ============================================================================ (1) what the negatives fix
def identity_check(trials=2000, seed=11):
    rng = random.Random(seed)
    worst = 0.0
    for _ in range(trials):
        p = signed.rand_quasi(rng, rng.randint(2, 12))
        worst = max(worst, abs(signed.pos(p) - (1 + signed.neg(p))))
    return worst


# ============================================================================ (2) what they do not fix alone
COUNTEREXAMPLE = ((0.7, 0.5, -0.2), (0.5, 0.7, -0.2))


def top(p):
    return max(range(len(p)), key=lambda i: p[i])


def top_moves_fraction(trials=3000, seed=13):
    rng = random.Random(seed)
    moved = total = 0
    npos_seen = []
    for _ in range(trials):
        n = rng.randint(3, 10)
        p = signed.rand_quasi(rng, n, npos=rng.randint(2, n - 1))
        posidx = [i for i, x in enumerate(p) if x > 0]
        vals = [p[i] for i in posidx]
        rng.shuffle(vals)
        q = list(p)
        for i, v in zip(posidx, vals):
            q[i] = v
        same_neg = all(p[i] == q[i] for i in range(n) if p[i] < 0)
        total += same_neg
        moved += same_neg and top(p) != top(q)
        npos_seen.append(len(posidx))
    return moved / total, float(np.mean([1 - 1 / k for k in npos_seen]))


# ============================================================================ (3) what projections add
def triangulation(Ks=(2, 4, 16, 180), state="sup01"):
    rows = []
    for K in Ks:
        g, X, Pm, Wr = signed.fbp(state, K)
        We = signed.wigner_exact(state, X, Pm)
        imx_e, imx_r = np.unravel_index(np.argmax(We), We.shape), np.unravel_index(np.argmax(Wr), Wr.shape)
        imn_e, imn_r = np.unravel_index(np.argmin(We), We.shape), np.unravel_index(np.argmin(Wr), Wr.shape)
        dx = float(g[1] - g[0])
        rows.append({"K": K,
                     "max_exact": (float(g[imx_e[0]]), float(g[imx_e[1]])), "max_recon": (float(g[imx_r[0]]),
                                                                                         float(g[imx_r[1]])),
                     "max_err": float(math.hypot(g[imx_e[0]] - g[imx_r[0]], g[imx_e[1]] - g[imx_r[1]])),
                     "min_err": float(math.hypot(g[imn_e[0]] - g[imn_r[0]], g[imn_e[1]] - g[imn_r[1]])),
                     "grid_step": dx, "max_abs_err": float(np.max(np.abs(Wr - We)))})
    return rows


# ============================================================================ (4) the cost under weak correlations
def samples_needed(Delta, N, delta=0.05):
    M = 1 + 2 * N
    eps = Delta / 2.0
    return 2.0 / eps ** 2 * M ** 2 * math.log(2.0 / delta)


def empirical_estimator(w, seat, shots=200000, seed=17):
    """Pashayan's estimator for w[seat]: sample i with |w_i|/M, score M sign(w_i) [i == seat].  Returns (mean, var,
    predicted var = M |w_seat| - w_seat^2)."""
    rng = np.random.default_rng(seed)
    w = np.asarray(w, float)
    M = np.abs(w).sum()
    idx = rng.choice(len(w), size=shots, p=np.abs(w) / M)
    score = np.where(idx == seat, M * np.sign(w[idx]), 0.0)
    return float(score.mean()), float(score.var()), float(M * abs(w[seat]) - w[seat] ** 2)


def collect():
    frac, expect = top_moves_fraction()
    return {"identity_worst": identity_check(), "counterexample": COUNTEREXAMPLE,
            "counterexample_tops": [top(p) for p in COUNTEREXAMPLE],
            "top_moves_fraction": frac, "top_moves_expected": expect,
            "triangulation": triangulation(),
            "samples": {N: {D: samples_needed(D, N) for D in (0.1, 0.01, 0.001)} for N in (0.0, 0.5, 2.0, 10.0)},
            "estimator": empirical_estimator([0.6, 0.55, -0.15], 1), "READ": [PASHAYAN_2015]}


def report():
    d = collect()
    print("W3C -- ranking seats by signed magnitudes (M-RULINGS item 25, H-SEATRANK)")
    print('  M: "%s"' % M_WORDS_25)
    print("\n(1) P = 1 + N for every normalised quasi-distribution (worst deviation over random cases %.1e)"
          % d["identity_worst"])
    print("(2) counterexample %s: same negatives, tops at seats %s -- the negatives alone do not rank"
          % (d["counterexample"], d["counterexample_tops"]))
    print("    negatives held fixed, positives permuted: the top seat moves in %.3f of cases (1 - 1/n_pos averages "
          "%.3f)" % (d["top_moves_fraction"], d["top_moves_expected"]))
    print("(3) triangulation from projections (sup01; grid step %.3f):" % d["triangulation"][0]["grid_step"])
    for r in d["triangulation"]:
        print("    K = %3d projections: top located within %.3f, negative minimum within %.3f; max |error| %.4f"
              % (r["K"], r["max_err"], r["min_err"], r["max_abs_err"]))
    print("(4) samples to separate two seats differing by Delta (95% confidence; Pashayan eq. 12, M = 1 + 2N):")
    for N, row in d["samples"].items():
        print("    N = %-5g M = %-5g  " % (N, 1 + 2 * N) + "  ".join("Delta %g: %.3g" % (D, s) for D, s in row.items()))
    m, v, pv = d["estimator"]
    print("    estimator check on w = (0.6, 0.55, -0.15), seat 2: mean %.4f (true 0.55), variance %.4f (predicted %.4f)"
          % (m, v, pv))


def selftest():
    n_ok = n_bad = n_ctl = 0
    structural = []

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-92s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:92], got))

    print("seatrank.py selftest")
    txt = " ".join(open(RULINGS, encoding="utf-8").read().split())
    chk("M's item-25 words found verbatim in the rulings file", M_WORDS_25 in txt, True)
    chk("CONTROL: an unnormalised weighting breaks the identity (sum 1.3: P - (1 + N) = 0.3)",
        abs(signed.pos([1.0, 0.5, -0.2]) - (1 + signed.neg([1.0, 0.5, -0.2])) - 0.3) < 1e-12, True, ctl=True)
    chk("(2) the counterexample shares its negatives and ranks opposite seats first",
        ([x for x in COUNTEREXAMPLE[0] if x < 0] == [x for x in COUNTEREXAMPLE[1] if x < 0],
         [top(p) for p in COUNTEREXAMPLE]), (True, [0, 1]))
    frac, expect = top_moves_fraction()
    chk("(2) with negatives fixed the top seat moves in a fraction near 1 - 1/n_pos (within 0.05)",
        abs(frac - expect) < 0.05, True)
    tri = triangulation()
    chk("(3) with 180 projections the top and the negative minimum are located to one grid step",
        (tri[-1]["max_err"] <= 1.5 * tri[-1]["grid_step"], tri[-1]["min_err"] <= 1.5 * tri[-1]["grid_step"]),
        (True, True))
    chk("(3) the reconstruction error falls as projections are added (K = 2 to 180)",
        tri[-1]["max_abs_err"] < tri[0]["max_abs_err"], True)
    chk("(4) Pashayan eq. 12: samples scale as M^2 -- N = 2 (M = 5) costs 25x N = 0 at the same Delta",
        abs(samples_needed(0.01, 2.0) / samples_needed(0.01, 0.0) - 25.0) < 1e-9, True)
    chk("(4) and as 1/Delta^2 -- a 10x weaker difference costs 100x",
        abs(samples_needed(0.001, 0.5) / samples_needed(0.01, 0.5) - 100.0) < 1e-9, True)
    m, v, pv = empirical_estimator([0.6, 0.55, -0.15], 1)
    chk("(4) the estimator is unbiased (mean within 0.01 of 0.55) with the predicted variance (within 3%)",
        (abs(m - 0.55) < 0.01, abs(v / pv - 1) < 0.03), (True, True))
    chk("CONTROL: for a non-negative weighting M = 1 (Pashayan p.2) -- no sampling overhead",
        float(np.abs(np.array([0.5, 0.3, 0.2])).sum()), 1.0, ctl=True)
    structural.append("(1) P = 1 + N over 2000 random quasi-distributions, worst deviation %.1e: the definition of "
                      "normalisation rearranged, so it cannot fail for a weighting that sums to 1 -- printed, not "
                      "counted (the CONTROL above shows it fails when the sum is not 1)" % identity_check())
    for x in structural:
        print("  [STRUCTURAL] " + x)
    print("\n%d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted"
          % (n_ok, n_ok + n_bad, n_ctl, len(structural)))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
