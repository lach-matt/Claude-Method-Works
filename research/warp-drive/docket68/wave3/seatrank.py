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

THE SETTING.  A quasi-probability w over candidate seats (signed weights summing to 1; Q-1s, signed.py; H-SEAT-QUASI).
A seat's rank is its positive weight.  Five questions, each computed.

  (1) THE AGGREGATE.  For any normalised w, the total positive weight is P = 1 + N, N the total negative magnitude
      (signed.pos's identity).  This is true by normalisation of EVERY signed measure (printed STRUCTURAL): it neither
      tests nor supports the per-seat claim.
  (2) UNCONSTRAINED, THE NEGATIVES FIX ONLY THE TOTAL.  Counterexample: w = (0.7, 0.5, -0.2) and w' = (0.5, 0.7, -0.2)
      share every negative entry and rank opposite seats first.  With the negative part held fixed and the positive
      entries permuted, the top seat moves in a fraction near 1 - 1/n_pos -- by construction of the unconstrained model,
      which carries no link between negatives and positives beyond the sum.
  (3) IN A PHYSICAL FAMILY, THE NEGATIVES DO LOCATE THE POSITIVE PEAK (H-CONSTRAINED-FAMILY).  For the qubit states
      cos(theta)|0> + e^(i phi) sin(theta)|1> (the Wigner functions W = e^(-r^2)/pi [cos^2 theta + sin^2 theta (2 r^2 - 1)
      + sqrt2 sin 2theta (x cos phi + p sin phi)], computed; checked against signed.wigner_exact at theta = pi/4,
      phi = 0), the location and depth of the negative minimum predict the location of the positive maximum
      (leave-one-out nearest neighbour over the family) to about one grid step; CONTROL: random pairing does not.  The
      peak lies opposite the minimum.  This supports a literal 'triangulate' GIVEN knowledge of the family; it does not
      show the negatives decide alone.  (Found by the W3C verifier; reproduced here.)
  (4) WHAT PROJECTIONS RECOVER.  When the quasi-distribution is a Wigner function (H-WIGNER-SEATS), its projections are
      true probabilities and filtered back-projection recovers it (signed.fbp, imported; signed.py: negative-region IoU
      1.000 at 180 angles, 0.037 at 2).  For the one state sup01, computed: the argmax ('top seat') and argmin
      (negative minimum) located against exact as projections are added.  In this reconstruction the projections are
      the INPUT and the negatives an OUTPUT recovered alongside the peak -- it is tomographic triangulation, not M's
      mechanism (M's agent is 'the stronger negative magnitudes').
  (5) THE COST OF RESOLVING A WEAK DIFFERENCE, IF SEATS ARE ESTIMATED BY SAMPLING THE QUASI-DISTRIBUTION (H-QUASI-SAMPLING).
      Pashayan, Wallman & Bartlett, arXiv:1503.07525v2 (READ via alphaXiv): sampling with probability |w|/M,
      M = sum |w| (eq. 8, p.2; M = 1 iff w >= 0, p.2) and scoring M sign(w) is unbiased (eq. 9, p.3); eq. 12 (p.3) gives
      a SUFFICIENT sample count s = (2/eps^2) M^2 ln(2/delta) -- stated for the forward-negativity bound M_-> of their
      Markov-chain estimator; it is used here with M_c in its place (p.3: this estimator minimises the range), and the
      paper calls it 'an upper bound on the rate of convergence' (p.3).  Estimating the DIFFERENCE w_i - w_j directly
      (score range [-M, M], eps = Delta): s_suff = 2 M^2 ln(2/delta) / Delta^2 -- worst case.  The TYPICAL cost is set by
      the estimator's variance, M (|w_i| + |w_j|) - Delta^2: at fixed seat weights it grows LINEARLY in M, not as M^2;
      M^2 returns only if the seat weights themselves grow with N.  Computed both, with an empirical check.  If instead
      the seats are MEASURED (H-WIGNER-SEATS: projections are non-negative), sampling the physical process costs
      (1/(2 eps^2)) ln(2/delta) with no M factor (Pashayan eq. 1, p.1): negativity 'bounds the efficiency of a classical
      estimation' (p.5), not of a measurement.

  GRADE (proposed, for verification; not seated): H-SEATRANK -- the aggregate reading is true by normalisation; in an
  unconstrained quasi-distribution the negatives fix only the total; within a physical family (H-CONSTRAINED-FAMILY)
  the negatives' location and depth do locate the positive peak; tomography recovers peak and negatives together from
  projections (H-WIGNER-SEATS, one state); negativity raises the cost of estimating seats only under H-QUASI-SAMPLING,
  and then about linearly at fixed seat weights.  It ranks seats and supplies none: no obstruction grade moves.

NAMED HYPOTHESES
  H-SEATRANK          (M, item 25) carried as M's hypothesis.
  H-SEAT-QUASI        the probability of seating is a quasi-probability over candidate seats.
  H-CONSTRAINED-FAMILY the seat quasi-distribution belongs to a known physical family (for (3): single-qubit Wigner
                      functions in the {|0>, |1>} span).
  H-WIGNER-SEATS      the seat quasi-distribution is a Wigner function, so its projections are measurable probabilities.
  H-QUASI-SAMPLING    seats are estimated by Monte Carlo over the quasi-distribution, not measured.
  H-WEAK-AS-DELTA     M's 'correlations are weak' is read as a small difference Delta between seat weights; no
                      correlation or distance is modelled here.
  H-NOISELESS         (4) uses exact projections; signed.fbp_finite_sample relaxes it (signed.py's own result).

OPEN
  - 'complex binary' (M, item 25): not addressed in this file; the board's reading of complex values in a signed
    measure is signed.py's Im H = pi N (Q1s-signed.md).
  - a per-seat claim for the negatives alone, outside a known family.

HISTORY (first said, corrected after the W3C verifier, 2026-10-05):
  - '(4) ... needs s = 8 M^2 ln(2/delta)/Delta^2 samples: STRONGER negative magnitudes make a weak difference COSTLIER to
    resolve, by M^2' -- a worst-case sufficient bound read as a requirement, with a 4x slack (two estimates at delta
    each, eps = Delta/2) and at '95%' that was 90% by the union bound; typical cost grows ~ M at fixed seat weights,
    and only under H-QUASI-SAMPLING.
  - '"triangulate" is literal: the projections rank the seats' credited projections to M's negatives.
  - 'H-SEATRANK holds in aggregate' credited an identity of normalisation to M's hypothesis.
  - the constrained-family test was missing; 'complex binary' and H-WEAK-AS-DELTA were not named.
  - a control computed |0.5|+|0.3|+|0.2| = 1 (vacuous); the eq.-12 ratio checks were counted (they are structural).
  - (3)'s first run sampled the family on 24 x 33 (theta, phi) and gave median 0.150 (3 grid steps); denser sampling
    gives 0.100 (36 x 48) and 0.071 (48 x 64, the default): nearest-neighbour resolution.  The W3C verifier reported
    0.025 on its own sampling of 792 states -- a different scheme, recorded, not adopted.
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
PASHAYAN_2015 = {"source": "arXiv:1503.07525v2", "route": "READ via alphaXiv (answer_pdf_queries), pp.1-5",
                 "used": "eq. 1 direct sampling (1/2eps^2) ln(2/delta) (p.1); M = ||W||_1 >= 1, = 1 iff nonnegative "
                         "(p.2); |W|/M sampling, estimator M Sign[W] unbiased (eqs. 8-9); eq. 12 s = (2/eps^2) "
                         "M_->^2 ln(2/delta), 'an upper bound on the rate of convergence' (p.3); p.5 'bounds the "
                         "efficiency of a classical estimation'"}
Z_ONE_SIDED_95 = 1.6448536269514722     # standard normal quantile at 0.95


# ============================================================================ (1) the aggregate (structural)
def identity_check(trials=2000, seed=11):
    rng = random.Random(seed)
    worst = 0.0
    for _ in range(trials):
        p = signed.rand_quasi(rng, rng.randint(2, 12))
        worst = max(worst, abs(signed.pos(p) - (1 + signed.neg(p))))
    return worst


# ============================================================================ (2) unconstrained: only the total
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
        total += 1
        moved += top(p) != top(q)
        npos_seen.append(len(posidx))
    return moved / total, float(np.mean([1 - 1 / k for k in npos_seen]))


# ============================================================================ (3) a physical family
G = np.linspace(-3.5, 3.5, 141)
X, PM = np.meshgrid(G, G, indexing="ij")


def wigner_qubit(theta, phi):
    r2 = X ** 2 + PM ** 2
    return np.exp(-r2) / np.pi * (math.cos(theta) ** 2 + math.sin(theta) ** 2 * (2 * r2 - 1)
                                  + math.sqrt(2) * math.sin(2 * theta) * (X * math.cos(phi) + PM * math.sin(phi)))


def family_features(n_theta=48, n_phi=64):
    feats, peaks = [], []
    for th in np.linspace(0.05, math.pi / 2 - 0.05, n_theta):
        for ph in np.linspace(0, 2 * math.pi, n_phi, endpoint=False):
            W = wigner_qubit(th, ph)
            if W.min() >= 0:
                continue
            i = np.unravel_index(np.argmin(W), W.shape)
            j = np.unravel_index(np.argmax(W), W.shape)
            feats.append((G[i[0]], G[i[1]], float(W.min())))
            peaks.append((G[j[0]], G[j[1]]))
    return np.array(feats), np.array(peaks)


def family_prediction(seed=19, n_theta=48, n_phi=64):
    """Leave-one-out nearest neighbour: predict each state's peak from the others' (minimum location, depth)."""
    f, pk = family_features(n_theta, n_phi)
    scale = np.array([1.0, 1.0, 1.0 / max(1e-12, np.ptp(f[:, 2]))])
    fs = f * scale
    err = []
    for k in range(len(f)):
        d = np.sum((fs - fs[k]) ** 2, axis=1)
        d[k] = np.inf
        m = int(np.argmin(d))
        err.append(float(np.hypot(*(pk[m] - pk[k]))))
    rng = np.random.default_rng(seed)
    perm = rng.permutation(len(f))
    ctrl = [float(np.hypot(*(pk[perm[k]] - pk[k]))) for k in range(len(f))]
    opp = [abs((math.atan2(pk[k][1], pk[k][0]) - math.atan2(f[k][1], f[k][0]) + math.pi) % (2 * math.pi) - math.pi)
           for k in range(len(f))]
    return {"n_states": len(f), "median_err": float(np.median(err)), "median_ctrl": float(np.median(ctrl)),
            "grid_step": float(G[1] - G[0]), "median_angle_between": float(np.median(opp))}


# ============================================================================ (4) what projections recover
def triangulation(Ks=(2, 4, 8, 16, 180), state="sup01"):
    rows = []
    for K in Ks:
        g, Xg, Pg, Wr = signed.fbp(state, K)
        We = signed.wigner_exact(state, Xg, Pg)
        imx_e, imx_r = np.unravel_index(np.argmax(We), We.shape), np.unravel_index(np.argmax(Wr), Wr.shape)
        imn_e, imn_r = np.unravel_index(np.argmin(We), We.shape), np.unravel_index(np.argmin(Wr), Wr.shape)
        rows.append({"K": K,
                     "max_err": float(math.hypot(g[imx_e[0]] - g[imx_r[0]], g[imx_e[1]] - g[imx_r[1]])),
                     "min_err": float(math.hypot(g[imn_e[0]] - g[imn_r[0]], g[imn_e[1]] - g[imn_r[1]])),
                     "grid_step": float(g[1] - g[0]), "max_abs_err": float(np.max(np.abs(Wr - We)))})
    return rows


# ============================================================================ (5) the cost, under H-QUASI-SAMPLING
def samples_sufficient(Delta, M, delta=0.05):
    """Hoeffding (Pashayan eq. 12 form, M_c in place of M_->) for the difference estimator, score range [-M, M]."""
    return 2.0 * M ** 2 * math.log(2.0 / delta) / Delta ** 2


def samples_typical(w_i, w_j, M, z=Z_ONE_SIDED_95):
    """CLT: the difference estimator's variance M(|w_i| + |w_j|) - Delta^2; n = z^2 var / Delta^2 (one-sided)."""
    Delta = w_i - w_j
    var = M * (abs(w_i) + abs(w_j)) - Delta ** 2
    return z ** 2 * var / Delta ** 2


def samples_direct(Delta, delta=0.05):
    """Measuring the seats (non-negative projections): Pashayan eq. 1 with eps = Delta/2 per seat ... used here for the
    difference of two frequencies, range [-1, 1]: 2 ln(2/delta)/Delta^2 -- no M factor."""
    return 2.0 * math.log(2.0 / delta) / Delta ** 2


def weights_with(N, wi=0.30, wj=0.25):
    """A quasi-distribution holding seats i, j at (wi, wj) with total negativity N: (wi, wj, 1 + N - wi - wj, -N)."""
    return [wi, wj, 1.0 + N - wi - wj, -N]


def empirical_order_errors(w, i, j, n, reps=400, seed=23):
    """Fraction of reps in which Pashayan's estimator, n samples, orders seats i, j wrongly."""
    rng = np.random.default_rng(seed)
    w = np.asarray(w, float)
    M = np.abs(w).sum()
    pr = np.abs(w) / M
    wrong = 0
    for _ in range(reps):
        idx = rng.choice(len(w), size=n, p=pr)
        sc = M * np.sign(w[idx])
        est_i = np.mean(np.where(idx == i, sc, 0.0))
        est_j = np.mean(np.where(idx == j, sc, 0.0))
        wrong += (est_i - est_j) * (w[i] - w[j]) <= 0
    return wrong / reps


def empirical_estimator(w, seat, shots=200000, seed=17):
    """Pashayan's estimator for w[seat]: (mean, variance, predicted variance M |w_seat| - w_seat^2)."""
    rng = np.random.default_rng(seed)
    w = np.asarray(w, float)
    M = np.abs(w).sum()
    idx = rng.choice(len(w), size=shots, p=np.abs(w) / M)
    score = np.where(idx == seat, M * np.sign(w[idx]), 0.0)
    return float(score.mean()), float(score.var()), float(M * abs(w[seat]) - w[seat] ** 2)


def cost_table():
    rows = []
    for N in (0.0, 0.5, 2.0, 10.0):
        w = weights_with(N)
        M = sum(abs(x) for x in w)
        rows.append({"N": N, "M": M, "sufficient": samples_sufficient(0.05, M), "typical": samples_typical(0.30, 0.25, M),
                     "measured": samples_direct(0.05)})
    return rows


def collect():
    frac, expect = top_moves_fraction()
    w2 = weights_with(2.0)
    return {"identity_worst": identity_check(), "counterexample": COUNTEREXAMPLE,
            "counterexample_tops": [top(p) for p in COUNTEREXAMPLE],
            "top_moves_fraction": frac, "top_moves_expected": expect,
            "family": family_prediction(), "triangulation": triangulation(), "cost": cost_table(),
            "empirical_N2": {n: empirical_order_errors(w2, 0, 1, n) for n in (2000, 5000, 20000)},
            "estimator": empirical_estimator([0.6, 0.55, -0.15], 1), "READ": [PASHAYAN_2015]}


def report():
    d = collect()
    print("W3C -- ranking seats by signed magnitudes (M-RULINGS item 25, H-SEATRANK)")
    print('  M: "%s"' % M_WORDS_25)
    print("\n(1) P = 1 + N for every normalised quasi-distribution (worst %.1e): true by normalisation" % d["identity_worst"])
    print("(2) unconstrained: %s share their negatives, tops at seat indices %s; negatives fixed, positives permuted: "
          "top moves in %.3f (1 - 1/n_pos: %.3f)" % (d["counterexample"], d["counterexample_tops"],
                                                       d["top_moves_fraction"], d["top_moves_expected"]))
    f = d["family"]
    print("(3) a physical family (%d qubit states with negativity): the minimum's location and depth predict the peak "
          "to median %.3f (grid step %.3f); CONTROL random pairing %.3f; peak opposite the minimum (median angle "
          "%.2f rad)" % (f["n_states"], f["median_err"], f["grid_step"], f["median_ctrl"], f["median_angle_between"]))
    print("(4) projections recover (sup01, H-WIGNER-SEATS; negatives are outputs here, not inputs):")
    for r in d["triangulation"]:
        print("    K = %3d: argmax within %.3f, argmin within %.3f; max |error| %.4f"
              % (r["K"], r["max_err"], r["min_err"], r["max_abs_err"]))
    print("(5) separating seats 0.30 and 0.25 (Delta 0.05, 95%):")
    for r in d["cost"]:
        print("    N = %-5g M = %-5g: sufficient (Hoeffding, H-QUASI-SAMPLING) %.3g; typical (CLT) %.3g; measured "
              "(no M) %.3g" % (r["N"], r["M"], r["sufficient"], r["typical"], r["measured"]))
    print("    empirical at N = 2: wrong orderings %s" % {k: "%.4f" % v for k, v in d["empirical_N2"].items()})
    m, v, pv = d["estimator"]
    print("    estimator on w = (0.6, 0.55, -0.15), seat index 1: mean %.4f (true 0.55), variance %.4f (predicted %.4f)"
          % (m, v, pv))


def selftest():
    n_ok = n_bad = n_ctl = 0
    structural = []

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = bool(got == want) if not isinstance(want, (list, tuple)) else got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-92s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:92], got))

    print("seatrank.py selftest")
    txt = " ".join(open(RULINGS, encoding="utf-8").read().split())
    chk("M's item-25 words found verbatim in the rulings file", M_WORDS_25 in txt, True)
    chk("CONTROL: an unnormalised weighting breaks P = 1 + N (sum 1.3: P - (1 + N) = 0.3)",
        abs(signed.pos([1.0, 0.5, -0.2]) - (1 + signed.neg([1.0, 0.5, -0.2])) - 0.3) < 1e-12, True, ctl=True)
    chk("(2) the counterexample shares its negatives and ranks opposite seats first",
        ([x for x in COUNTEREXAMPLE[0] if x < 0] == [x for x in COUNTEREXAMPLE[1] if x < 0],
         [top(p) for p in COUNTEREXAMPLE]), (True, [0, 1]))
    frac, expect = top_moves_fraction()
    chk("(2) negatives fixed, positives permuted: the top seat moves in a fraction near 1 - 1/n_pos (within 0.05)",
        abs(frac - expect) < 0.05, True)
    chk("(3) the family's W matches signed.wigner_exact for sup01 at theta = pi/4, phi = 0 (to 1e-12)",
        float(np.max(np.abs(wigner_qubit(math.pi / 4, 0.0) - signed.wigner_exact("sup01", X, PM)))) < 1e-12, True)
    f = family_prediction()
    chk("(3) within the family the minimum's location and depth predict the peak to within 2 grid steps (median %.3f)"
        % f["median_err"], f["median_err"] <= 2 * f["grid_step"], True)
    coarse = family_prediction(n_theta=24, n_phi=33)
    chk("(3) the prediction error falls as the family is sampled more densely (726 states %.3f -> %d states %.3f): "
        "it is sampling resolution, not a floor" % (coarse["median_err"], f["n_states"], f["median_err"]),
        f["median_err"] < coarse["median_err"], True)
    chk("CONTROL: random pairing does not (median error above 10 grid steps)", f["median_ctrl"] > 10 * f["grid_step"],
        True, ctl=True)
    tri = triangulation()
    chk("(4) at 180 projections the argmax and argmin are located to one grid step",
        (tri[-1]["max_err"] <= 1.5 * tri[-1]["grid_step"], tri[-1]["min_err"] <= 1.5 * tri[-1]["grid_step"]),
        (True, True))
    chk("(4) the reconstruction error falls from K = 2 to K = 180", tri[-1]["max_abs_err"] < tri[0]["max_abs_err"], True)
    ct = cost_table()
    chk("(5) at fixed seat weights the typical (CLT) cost grows about linearly in M: N = 2 (M = 5) over N = 0 within 4-6x",
        4.0 < ct[2]["typical"] / ct[0]["typical"] < 6.0, True)
    emp = collect()["empirical_N2"]
    chk("(5) empirically at N = 2 the typical cost, not the sufficient one, is the scale: 2e4 samples order the seats "
        "correctly in >= 99%% (sufficient bound says %.3g)" % ct[2]["sufficient"], emp[20000] <= 0.01, True)
    m, v, pv = empirical_estimator([0.6, 0.55, -0.15], 1)
    chk("(5) the estimator is unbiased (mean within 0.01 of 0.55) with the predicted variance (within 3%)",
        (abs(m - 0.55) < 0.01, abs(v / pv - 1) < 0.03), (True, True))
    m0, v0, _ = empirical_estimator([0.5, 0.3, 0.2], 1)
    chk("CONTROL: on a non-negative weighting (M = 1) the estimator's variance is w(1 - w) = 0.21 (within 3%)",
        abs(v0 / 0.21 - 1) < 0.03, True, ctl=True)
    structural.append("(1) P = 1 + N, worst deviation %.1e over 2000 random cases: true by normalisation"
                      % identity_check())
    structural.append("(5) the sufficient-count ratios (M^2, 1/Delta^2) re-evaluate the formula as written")
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
