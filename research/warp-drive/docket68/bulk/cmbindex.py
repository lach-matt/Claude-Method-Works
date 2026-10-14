#!/usr/bin/env python3
"""cmbindex.py -- M's proposal (M-RULINGS item 142): the spectra index against our universe's background radiation,
and whether a point of the Löwdin solution sits at a radiation signature of an element not witnessed here.

First written with three over-claims the verifier found -- a rest-frame coincidence offered as a pass about light that
left at z ~ 1100, "no line at 50 ppm" for narrow lines in 13.6 GHz channels, and "no element signature at all" -- and
a defect test that compared the channel equation with itself; all are corrected (CMBINDEX.md History).

The Löwdin solution (recovered/BODY2-CHAPTER-35-THE-LOWDIN-SOLUTION.md): the periodic order derived from the
many-electron equation over Z = 2-108 ("every element with a measured ground configuration"); "twelve rows,
Z = 109-120", "unwitnessed"; "no g block below Z = 121".  M (item 138): "118 current elements that are observable to our
universe so far" -- so M's "not currently witnessed in our universe" is Z >= 119.
The spectra index: drive/The Method Materials/COORDINATES-2_13.csv, one quantum defect per (Z, charge, l, mult);
charge 1 is the neutral atom (Z = 1 and Z = 2 charge 2 are both "one electron").

READ:
  Fixsen et al. 1996, astro-ph/9605054: "2 to 21 cm^-1" (p.3); "the weighted rms deviation in the frequency range 2 to
      21 cm^-1 is 50 ppm ... of the peak brightness" (p.23), formal chi^2/dof = 46/40; points 0.4538 cm^-1 apart (p.11);
      Table 4 monopole residuals (below), after fitting T, dT and a Galactic template (eq. 3); peak ~400 MJy/sr (Fig. 3)
  Fixsen 2009, arXiv:0911.1955: T0 = 2.72548 +- 0.00057 K
  Sunyaev & Chluba 2009, arXiv:0908.0435: recombination radiation from hydrogen and helium (pp.13-18), its photons
      "~10^3 times redshifted" (p.13); in the FIRAS band, Balmer, Paschen and Brackett features; not yet detected

  B1  FIRAS's 43 monopole residuals, channel by channel: largest |r/sigma| 2.52.  What that excludes: a channel-averaged
      excess above ~50 ppm of the peak in 13.6 GHz channels of the sky-averaged spectrum -- not a narrow line, which a
      channel dilutes by its width over 13.6 GHz.  Control (STRUCTURAL): a 5-sigma injection is flagged
  B2  a COMB SEARCH (matched filter) of Table 4 for a Rydberg series n -> n-1 at free redshift z in [0, 3000]:
      hydrogen-like (delta = 0 -- the index's template for Z = 119, 120) and each Löwdin row's s, p, d defects.  Each
      line puts equal channel-averaged amplitude into the channel holding it (H-TOPHAT-CHANNEL, H-EQUAL-COMB).  The
      largest significance is compared with 400 sign-flip nulls of the same residuals.  Control: a comb injected at
      z = 1089 reads S > 4 at that z (the scan's maximum may alias to another z: 43 channels, 13.6 GHz wide)
  B3  where an atom's lines land: at rest, n -> n-1 lines fall in the FIRAS band for n* = 23-46; from z = 1089 only
      n* = 3-4 do (the background radiation's own lines arrive as Balmer- and Paschen-like features).  The series limit
      cancels between two levels of one series (STRUCTURAL)
  B4  can the index name an element by its defects?  Against MEASURED (or exact) neutral series only, Z = 109-118 match
      none and Z = 119-120 (delta = 0.0, B = 0) match hydrogen and helium.  Against the index's COMPUTED rows the counts sit near
      chance, and the control -- every Z <= 108 row against the others -- gives the same: the Löwdin rows are no less
      distinguishable than ours.  Candidate (the equation's own periodicity, not a measurement): the nearest computed rows
      of Z = 111, 112, 114 are their homologues Au, Hg, Pb; 115-118 sit one step before theirs; 109-110 nearest Hs
  B5  mass: a line sits c m_e/M below the infinite-mass line -- H 163 km/s, Pb 0.79, 270-300 u 0.55-0.61 -- a uniform
      scaling of the whole series, so degenerate with redshift (STRUCTURAL); a 300 u atom's thermal width at 3000 K
      (0.29 km/s) exceeds its gap to lead
  B6  (READ, the index) "no long-lived isotope" marks Z = 104-118 and "no nuclide synthesised" Z = 119-120: the first is
      not distinctive of the Löwdin rows; the second is M's line at 118
Stdlib only.  python3 cmbindex.py [--selftest]
"""
import csv
import math
import os
import random
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
INDEX = os.path.join(REPO, "drive", "The Method Materials", "COORDINATES-2_13.csv")

H_PLANCK = 6.62607015e-34          # J s, exact (SI)
K_B = 1.380649e-23                 # J/K, exact (SI)
C = 299792458.0                    # m/s, exact (SI)
U_KG = 1.66053906660e-27           # kg, CODATA 2018 (standard, not READ here)
R_INF = 10973731.568160            # m^-1, CODATA 2018 (standard, not READ here)
ME_U = 5.48579909065e-4            # electron mass in u, CODATA 2018 (standard, not READ here)
T0 = 2.72548                       # K, Fixsen 2009 (READ)
RMS_DELTA = 0.1809                 # the channel equation's rms against 358 measured channels (docs/POPULATE.md)
MEDIAN_ERR = 0.0587                # its median |error| (docs/POPULATE.md)
CM1_GHZ = C * 100 / 1e9
Z_REC = 1089.0                     # a recombination-era redshift (the board's choice of a representative value)

# Fixsen et al. 1996 Table 4: frequency (cm^-1), residual (kJy/sr), 1-sigma (kJy/sr)   (READ; all 43 rows verified)
FIRAS_T4 = [
    (2.27, 5, 14), (2.72, 9, 19), (3.18, 15, 25), (3.63, 4, 23), (4.08, 19, 22), (4.54, -30, 21), (4.99, -30, 18),
    (5.45, -10, 18), (5.90, 32, 16), (6.35, 4, 14), (6.81, -2, 13), (7.26, 13, 12), (7.71, -22, 11), (8.17, 8, 10),
    (8.62, 8, 11), (9.08, -21, 12), (9.53, 9, 14), (9.98, 12, 16), (10.44, 11, 18), (10.89, -29, 22),
    (11.34, -46, 22), (11.80, 58, 23), (12.25, 6, 23), (12.71, -6, 23), (13.16, 6, 22), (13.61, -17, 21),
    (14.07, 6, 20), (14.52, 26, 19), (14.97, -12, 19), (15.43, -19, 19), (15.88, 8, 21), (16.34, 7, 23),
    (16.79, 14, 26), (17.24, -33, 28), (17.70, 6, 30), (18.15, 26, 32), (18.61, -26, 33), (19.06, -6, 35),
    (19.51, 8, 41), (19.97, 26, 55), (20.42, 57, 88), (20.87, -116, 155), (21.33, -432, 282)]
CH = 0.4538                        # cm^-1 between points (p.11)


# ---------------------------------------------------------------- B1: the residuals channel by channel

def b1(table=FIRAS_T4):
    z = [r / s for _, r, s in table]
    i = max(range(len(z)), key=lambda k: abs(z[k]))
    return {"n": len(z), "chi2_diag": sum(x * x for x in z), "max_abs_z": abs(z[i]), "at": table[i][0]}


def planck_jy_sr(nu_ghz):
    nu = nu_ghz * 1e9
    return 2 * H_PLANCK * nu**3 / C**2 / math.expm1(H_PLANCK * nu / (K_B * T0)) * 1e26


def wien_x():
    x = 3.0
    for _ in range(60):
        x = x - (x - 3 * (1 - math.exp(-x))) / (1 - 3 * math.exp(-x))
    return x


def peak():
    nu = wien_x() * K_B * T0 / H_PLANCK / 1e9
    return {"nu_GHz": nu, "I_MJy_sr": planck_jy_sr(nu) / 1e6}


# ---------------------------------------------------------------- B2: the comb search

def nu_alpha_cm1(n, d=0.0):
    """Rest-frame wavenumber (cm^-1) of n -> n-1 for a neutral Rydberg series with defect d (core charge 1)."""
    return R_INF / 100 * (1 / (n - 1 - d) ** 2 - 1 / (n - d) ** 2)


def template(z, d, nmax=80):
    t = [0.0] * len(FIRAS_T4)
    for n in range(2, nmax + 1):
        if n - 1 - d <= 0:
            continue
        f = nu_alpha_cm1(n, d) / (1 + z)
        for i, (fc, _, _) in enumerate(FIRAS_T4):
            if abs(f - fc) <= CH / 2:
                t[i] += 1.0
    return t


def fit(t, res):
    num = sum(ti * r / s**2 for ti, r, (_, _, s) in zip(t, res, FIRAS_T4))
    den = sum(ti * ti / s**2 for ti, (_, _, s) in zip(t, FIRAS_T4))
    if den == 0:
        return None
    A = num / den
    sA = 1 / math.sqrt(den)
    return A, sA


ZGRID = [0.0] + [10 ** (k / 400) - 1 for k in range(1, 1392)]          # z from 0 to ~3000, log-spaced in 1+z


def comb_scan(d, res=None):
    res = res if res is not None else [r for _, r, _ in FIRAS_T4]
    best, lims = (0.0, None, None), []
    for z in ZGRID:
        f = fit(template(z, d), res)
        if f is None:
            continue
        A, sA = f
        S = A / sA
        lims.append(abs(A) + 2 * sA)
        if abs(S) > abs(best[0]):
            best = (S, z, A)
    return {"S": best[0], "z": best[1], "A": best[2], "lim_median": statistics.median(lims)}


def comb_null(d, trials=400, seed=142):
    rng = random.Random(seed)
    base = [r for _, r, _ in FIRAS_T4]
    out = []
    for _ in range(trials):
        out.append(abs(comb_scan(d, [r * rng.choice((-1, 1)) for r in base])["S"]))
    return out


def comb_injected(d=0.0, z=Z_REC, k=5.0):
    t = template(z, d)
    sA = fit(t, [0.0] * len(t))[1]
    res = [r + k * sA * ti for (_, r, _), ti in zip(FIRAS_T4, t)]
    out = comb_scan(d, res)
    A, sA2 = fit(t, res)
    out["S_at_injected"] = A / sA2
    out["lines_in_band"] = int(sum(t))
    return out


# ---------------------------------------------------------------- B3: where lines land

def b3(d=0.0):
    lo, hi = FIRAS_T4[0][0], FIRAS_T4[-1][0]
    rest = [n for n in range(2, 400) if lo <= nu_alpha_cm1(n, d) <= hi]
    rec = [n for n in range(2, 400) if lo <= nu_alpha_cm1(n, d) / (1 + Z_REC) <= hi]
    L1, L2 = 1.0e7, 4.3e7
    e = lambda L, n: L - R_INF / (n - 0.37) ** 2
    return {"rest": (min(rest), max(rest)), "rec": (min(rec), max(rec)),
            "limit_free": abs((e(L1, 30) - e(L1, 29)) - (e(L2, 30) - e(L2, 29))) < 1e-6}


# ---------------------------------------------------------------- B4: the defect fingerprint

def load_index():
    series, bounds = {}, {}
    for r in csv.DictReader(open(INDEX, encoding="utf-8")):
        if r["charge"] != "1":
            continue
        Z, l, mult = int(r["Z"]), int(r["l"]), int(r["mult"])
        bounds.setdefault(Z, set()).add(r["bound"])
        if l <= 2:
            series.setdefault((Z, mult), {})[l] = (float(r["delta"]), r["grade"])
    return series, bounds


def circ(a, b):
    x = abs((a - b) % 1.0)
    return min(x, 1 - x)


def dist(s1, s2):
    return max(circ(s1[l][0], s2[l][0]) for l in (0, 1, 2))


def b4():
    S, _ = load_index()
    full = {k: v for k, v in S.items() if all(l in v for l in (0, 1, 2))}
    measured = {k: v for k, v in full.items() if k[0] <= 108 and all(v[l][1] in ("measured", "exact") for l in (0, 1, 2))}
    computed = {k: v for k, v in full.items() if k[0] <= 108}

    def matches(Z, pool, tol):
        mine = [v for k, v in full.items() if k[0] == Z]
        return sorted({k[0] for k, v in pool.items() if any(dist(m, v) <= tol for m in mine)})

    vs_meas = {Z: matches(Z, measured, RMS_DELTA) for Z in range(109, 121)}
    vs_comp = {Z: len(matches(Z, computed, RMS_DELTA)) for Z in range(109, 121)}
    zs_comp = sorted({k[0] for k in computed})
    ctrl = [len([w for w in matches(Z, {k: v for k, v in computed.items() if k[0] != Z}, RMS_DELTA)])
            for Z in zs_comp]
    chance = len(zs_comp) * (2 * RMS_DELTA) ** 3
    nearest = {}
    for Z in range(109, 119):
        mine = [v for k, v in full.items() if k[0] == Z]
        nearest[Z] = min(((min(dist(m, v) for m in mine), k[0]) for k, v in computed.items()), key=lambda x: x[0])
    return {"n_measured_series": len(measured), "measured_Z": sorted({k[0] for k in measured}), "vs_meas": vs_meas,
            "vs_comp": vs_comp, "ctrl_median": statistics.median(ctrl), "ctrl_range": (min(ctrl), max(ctrl)),
            "chance": chance, "nearest": nearest,
            "zero_rows": [Z for Z in range(109, 121) if all(v[l][0] == 0.0 for k, v in full.items() if k[0] == Z
                                                             for l in (0, 1, 2))]}


# ---------------------------------------------------------------- B5, B6

def b5():
    v = lambda M: C * (ME_U / M) / (1 + ME_U / M) / 1e3
    thermal = math.sqrt(K_B * 3000 / (300 * U_KG)) / 1e3
    pk = peak()["nu_GHz"]
    ch = lambda f_cm1: CH * CM1_GHZ / (f_cm1 * CM1_GHZ) * C / 1e3
    return {"H": v(1.00728), "Pb": v(207.2), "U": v(238.03), "SH": (v(300.0), v(270.0)), "thermal_300u_3000K": thermal,
            "channel_kms": (ch(FIRAS_T4[-1][0]), CH * CM1_GHZ / pk * C / 1e3, ch(FIRAS_T4[0][0]))}


def b6():
    _, bounds = load_index()
    ll = [Z for Z in sorted(bounds) if any("no long-lived isotope" in b for b in bounds[Z])]
    ns = [Z for Z in sorted(bounds) if any("no nuclide synthesised" in b for b in bounds[Z])]
    return {"long_lived": ll, "no_nuclide": ns}


# ----------------------------------------------------------------

def compute(nulls=True):
    D = {"b1": b1(), "peak": peak(), "b3": b3(), "b4": b4(), "b5": b5(), "b6": b6()}
    S, _ = load_index()
    combs = {"delta = 0 (H-like; Z = 119, 120)": 0.0}
    for Z in range(109, 119):
        for l, name in ((0, "s"), (1, "p"), (2, "d")):
            dd = [v[l][0] for k, v in S.items() if k[0] == Z and l in v][0] % 1.0
            combs["Z = %d %s" % (Z, name)] = dd
    D["combs"] = {k: comb_scan(d) for k, d in combs.items()}
    D["inj"] = comb_injected()
    if nulls:
        nl = comb_null(0.0)
        D["null"] = {"median": statistics.median(nl), "p": sum(1 for x in nl if x >= abs(D["combs"]["delta = 0 (H-like; Z = 119, 120)"]["S"])) / len(nl),
                     "q95": sorted(nl)[int(0.95 * len(nl))]}
    return D


def report(D):
    a, pk, c, e, f, g = D["b1"], D["peak"], D["b3"], D["b4"], D["b5"], D["b6"]
    print("cmbindex.py -- the spectra index against the background radiation (item 142)\n")
    print("B1 FIRAS residuals: %d points, diagonal sum (r/sigma)^2 = %.1f (the paper's own, with correlations and 3 "
          "fitted parameters: 46/40); largest |r/sigma| %.2f at %.2f cm^-1.  Peak %.1f GHz, %.0f MJy/sr: 50 ppm = "
          "%.0f kJy/sr channel-averaged" % (a["n"], a["chi2_diag"], a["max_abs_z"], a["at"], pk["nu_GHz"],
                                             pk["I_MJy_sr"], 50e-6 * pk["I_MJy_sr"] * 1e3))
    print("B2 comb search, z in [0, 3000] (largest S = A/sigma_A, at z; median 2-sigma limit on A, kJy/sr):")
    for k, v in D["combs"].items():
        print("   %-34s S = %+.2f at z = %8.1f   limit %.1f" % (k, v["S"], v["z"], v["lim_median"]))
    if "null" in D:
        print("   sign-flip nulls (H-like comb, 400): median max|S| %.2f, 95th percentile %.2f; p of the observed %.2f"
              % (D["null"]["median"], D["null"]["q95"], D["null"]["p"]))
    print("   control: a comb injected at z = %.0f (%d lines in band), 5 sigma: S at that z = %.2f; the scan's largest "
          "S = %.2f at z = %.1f (z aliases: 43 channels 13.6 GHz wide)"
          % (Z_REC, D["inj"]["lines_in_band"], D["inj"]["S_at_injected"], D["inj"]["S"], D["inj"]["z"]))
    print("B3 n -> n-1 lines in the FIRAS band: at rest n* = %d-%d; from z = %.0f, n* = %d-%d; limit cancels %s"
          % (c["rest"][0], c["rest"][1], Z_REC, c["rec"][0], c["rec"][1], c["limit_free"]))
    print("B4 neutral series with s, p, d all measured or exact: %d (Z = %s)" % (e["n_measured_series"], e["measured_Z"]))
    print("   Löwdin rows matched within rms %.4f by MEASURED (or exact) series: %s" % (RMS_DELTA, e["vs_meas"]))
    print("   by COMPUTED rows (Z <= 108): %s; chance %.1f; control (each Z <= 108 against the others) median %s, range %s"
          % (e["vs_comp"], e["chance"], e["ctrl_median"], e["ctrl_range"]))
    print("   nearest computed row (distance, Z) for Z = 109-118: %s" % {k: (round(v[0], 4), v[1]) for k, v in e["nearest"].items()})
    print("   rows reading delta = 0.0 in every neutral channel: %s" % e["zero_rows"])
    print("B5 below the infinite-mass line: H %.1f km/s, Pb %.3f, U %.3f, 270-300 u %.3f-%.3f; thermal width of 300 u at "
          "3000 K %.2f km/s; a FIRAS channel spans %.0f / %.0f / %.0f km/s (top, peak, bottom of the band)"
          % (f["H"], f["Pb"], f["U"], f["SH"][0], f["SH"][1], f["thermal_300u_3000K"], *f["channel_kms"]))
    print("B6 (the index) 'no long-lived isotope': Z = %s; 'no nuclide synthesised': Z = %s"
          % (g["long_lived"], g["no_nuclide"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    D = compute(nulls=True)
    a, c, e, f, g = D["b1"], D["b3"], D["b4"], D["b5"], D["b6"]
    chk("B1: every FIRAS residual lies within 2.6 sigma (channel-averaged)", a["max_abs_z"] < 2.6)
    chk("B1 control (STRUCTURAL): a 5-sigma injection is flagged", b1([(fq, r + (5 * s if i == 10 else 0), s)
                                                                     for i, (fq, r, s) in enumerate(FIRAS_T4)])["max_abs_z"] > 3)
    chk("B2: no comb, H-like or any Löwdin row's s/p/d, exceeds |S| = 4 anywhere in z = 0-3000",
        all(abs(v["S"]) < 4 for v in D["combs"].values()))
    chk("B2: the H-like comb's largest |S| is ordinary against sign-flip nulls (p > 0.05)", D["null"]["p"] > 0.05)
    chk("B2 control: a 5-sigma comb injected at z = 1089 reads S > 4 at that z, and the scan's largest S exceeds 4",
        D["inj"]["S_at_injected"] > 4 and D["inj"]["S"] > 4)
    chk("B3: from z = 1089 only n* = 3-4 lines fall in the band; at rest n* = 23-46", c["rec"] == (3, 4) and c["rest"] == (23, 46))
    chk("B3 (STRUCTURAL): the series limit cancels", c["limit_free"])
    chk("B4: against measured series, Z = 109-118 match none", all(e["vs_meas"][Z] == [] for Z in range(109, 119)))
    chk("B4: Z = 119 and 120 (delta = 0.0) match hydrogen (exact) and helium (measured)",
        all(e["vs_meas"][Z] == [1, 2] for Z in (119, 120)) and e["zero_rows"] == [119, 120])
    chk("B4 control: the Löwdin rows' computed look-alike counts lie within the range of ours against each other",
        all(e["ctrl_range"][0] <= v <= e["ctrl_range"][1] for v in e["vs_comp"].values()))
    chk("B4 candidate: the nearest computed rows of Z = 111, 112, 114 are their homologues Au, Hg, Pb; of 109, 110, Hs",
        [e["nearest"][Z][1] for Z in (109, 110, 111, 112, 114)] == [108, 108, 79, 80, 82])
    chk("B5: a 300 u atom's thermal width at 3000 K exceeds its gap to lead", f["thermal_300u_3000K"] > f["Pb"] - f["SH"][1])
    chk("B6 (READ): 'no long-lived isotope' marks Z = 104-118, 'no nuclide synthesised' Z = 119-120",
        g["long_lived"] == list(range(104, 119)) and g["no_nuclide"] == [119, 120])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
