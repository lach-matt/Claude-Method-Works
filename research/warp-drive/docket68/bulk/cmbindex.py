#!/usr/bin/env python3
"""cmbindex.py -- M's proposal (M-RULINGS item 142): the spectra index against our universe's background radiation,
and whether a point of the Löwdin solution sits at a radiation signature of an element not witnessed here.

The Löwdin solution (recovered/BODY2-CHAPTER-35-THE-LOWDIN-SOLUTION.md): the periodic order derived from the
many-electron equation, 107/107 over Z = 2-108; "twelve unwitnessed rows, Z = 109-120"; "no g block below Z = 121".
The spectra index: drive/The Method Materials/COORDINATES-2_13.csv -- one quantum defect delta per (Z, charge, l, mult),
Z = 1-120, graded measured / exact / computed (the channel equation, register 1205; rms 0.1809 on the 358 measured
channels, docs/POPULATE.md).  charge 1 is the neutral atom (Z = 1, charge 1 is hydrogen, "one electron").

READ:
  Fixsen et al. 1996, astro-ph/9605054 (FIRAS): spectra "from 2 to 21 cm^-1"; "The RMS deviations are less than 50
      parts per million of the peak"; |y| < 15e-6, |mu| < 9e-5 (95% CL); Table 4, the monopole residuals (below).
  Fixsen 2009, arXiv:0911.1955 abstract: T0 = 2.72548 +- 0.00057 K.
  Sunyaev & Chluba 2009, arXiv:0908.0435: the recombination radiation is computed from hydrogen and helium (pp.13-18),
      relative distortion ~1e-10 to 1e-7 (Fig. 8), "may become observable in the near future" (abstract) -- not detected.

  B1  the background radiation as measured: FIRAS's 43 monopole residuals about the blackbody, every one within
      2.6 sigma; no line.  Control: a line injected at 5 sigma into one channel is flagged
  B2  where the background radiation sits: Wien peak nu = x k T0/h with x = 3(1 - e^-x), 160.2 GHz (STRUCTURAL)
  B3  what of an atom falls there: Rydberg transitions n -> n-1 of any neutral atom, nu = c R_M [1/(n-1-d)^2 - 1/(n-d)^2]
      -- the series limit cancels (STRUCTURAL), so the index's rule "the limit is never computed" is kept.  In the FIRAS
      band n runs over a computed range
  B4  can the index name an element by its lines there?  A neutral Rydberg series in this band carries delta mod 1 per
      channel.  For each Löwdin row Z = 109-120, the witnessed elements (Z = 1-108) whose s, p, d defects all lie within
      the channel equation's own rms (0.1809) of it: six to fifteen for each of Z = 109-118; Z = 119 and 120 match
      hydrogen.  Control: at a tolerance of 0.001 the same test
      returns one or none.  Z = 119 and 120 read delta = 0.0 (B = 0) in every neutral channel: hydrogen-like in the index
  B5  the other fingerprint, mass: a Rydberg line sits c m_e/M below the infinite-mass line -- hydrogen 163 km/s, lead
      0.79, any nucleus of mass 270-300 u 0.55-0.61; against one FIRAS channel, ~25,000 km/s wide (STRUCTURAL)
  B6  (READ, the index itself) every neutral row Z >= 109 carries "no long-lived isotope" or "no nuclide synthesised"
Imports nothing from the board; reads the index by path.  Stdlib only.  python3 cmbindex.py [--selftest]
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
INDEX = os.path.join(REPO, "drive", "The Method Materials", "COORDINATES-2_13.csv")

H_PLANCK = 6.62607015e-34          # J s, exact (SI)
K_B = 1.380649e-23                 # J/K, exact (SI)
C = 299792458.0                    # m/s, exact (SI)
R_INF = 10973731.568160            # m^-1, CODATA 2018 (standard, not READ here)
ME_U = 5.48579909065e-4            # electron mass in u, CODATA 2018 (standard, not READ here)
T0 = 2.72548                       # K, Fixsen 2009 (READ)
RMS_DELTA = 0.1809                 # the channel equation's rms on 358 measured channels (docs/POPULATE.md)
CM1_GHZ = C * 100 / 1e9            # 1 cm^-1 in GHz

# Fixsen et al. 1996 Table 4: frequency (cm^-1), residual (kJy/sr), 1-sigma uncertainty (kJy/sr)   (READ)
FIRAS_T4 = [
    (2.27, 5, 14), (2.72, 9, 19), (3.18, 15, 25), (3.63, 4, 23), (4.08, 19, 22), (4.54, -30, 21), (4.99, -30, 18),
    (5.45, -10, 18), (5.90, 32, 16), (6.35, 4, 14), (6.81, -2, 13), (7.26, 13, 12), (7.71, -22, 11), (8.17, 8, 10),
    (8.62, 8, 11), (9.08, -21, 12), (9.53, 9, 14), (9.98, 12, 16), (10.44, 11, 18), (10.89, -29, 22),
    (11.34, -46, 22), (11.80, 58, 23), (12.25, 6, 23), (12.71, -6, 23), (13.16, 6, 22), (13.61, -17, 21),
    (14.07, 6, 20), (14.52, 26, 19), (14.97, -12, 19), (15.43, -19, 19), (15.88, 8, 21), (16.34, 7, 23),
    (16.79, 14, 26), (17.24, -33, 28), (17.70, 6, 30), (18.15, 26, 32), (18.61, -26, 33), (19.06, -6, 35),
    (19.51, 8, 41), (19.97, 26, 55), (20.42, 57, 88), (20.87, -116, 155), (21.33, -432, 282)]
FIRAS_CHANNEL_CM1 = 0.4538          # the spacing of Fixsen et al.'s spectral points, cm^-1 (p.11)


def b1(table=FIRAS_T4):
    z = [r / s for _, r, s in table]
    return {"n": len(z), "chi2_diag": sum(x * x for x in z), "max_abs_z": max(abs(x) for x in z),
            "at": table[max(range(len(z)), key=lambda i: abs(z[i]))][0]}


def b1_injected(sigmas=5.0, at=10):
    t = list(FIRAS_T4)
    f, r, s = t[at]
    t[at] = (f, r + sigmas * s, s)
    return b1(t)


def wien_x():
    x = 3.0
    for _ in range(60):
        x = x - (x - 3 * (1 - math.exp(-x))) / (1 - 3 * math.exp(-x))
    return x


def b2():
    x = wien_x()
    return {"x": x, "peak_GHz": x * K_B * T0 / H_PLANCK / 1e9,
            "band_GHz": (FIRAS_T4[0][0] * CM1_GHZ, FIRAS_T4[-1][0] * CM1_GHZ)}


def r_m(mass_u):
    return R_INF / (1 + ME_U / mass_u)


def nu_alpha(n, d=0.0, mass_u=1e9):
    return C * r_m(mass_u) * (1 / (n - 1 - d) ** 2 - 1 / (n - d) ** 2) / 1e9          # GHz


def b3(d=0.37):
    lo, hi = b2()["band_GHz"]
    ns = [n for n in range(2, 400) if lo <= nu_alpha(n) <= hi]
    # the limit cancels: levels E = L - R/(n - d)^2 for two different L give the same n -> n-1 line
    lines = []
    for L in (1.0e7, 4.3e7):
        e = lambda n: L - R_INF / (n - d) ** 2
        lines.append(e(30) - e(29))
    return {"n_range": (min(ns), max(ns)), "limit_free": abs(lines[0] - lines[1]) < 1e-6 * abs(lines[0])}


def load_index():
    out, bounds = {}, {}
    for r in csv.DictReader(open(INDEX, encoding="utf-8")):
        if r["charge"] == "1" and int(r["l"]) <= 2:
            out.setdefault(int(r["Z"]), {})[int(r["l"])] = float(r["delta"])
            bounds.setdefault(int(r["Z"]), set()).add(r["bound"])
    return out, bounds


def circ(a, b):
    d = abs((a - b) % 1.0)
    return min(d, 1 - d)


def lookalikes(D, Z, tol):
    return [w for w in range(1, 109) if w in D and all(circ(D[Z][l], D[w][l]) <= tol for l in (0, 1, 2))]


def b4():
    D, _ = load_index()
    one = {Z: lookalikes(D, Z, RMS_DELTA) for Z in range(109, 121)}
    two = {Z: lookalikes(D, Z, 2 * RMS_DELTA) for Z in range(109, 121)}
    tight = {Z: lookalikes(D, Z, 0.001) for Z in range(109, 121)}
    zero_rows = [Z for Z in range(109, 121) if all(D[Z][l] == 0.0 for l in (0, 1, 2))]
    return {"one_rms": {Z: len(v) for Z, v in one.items()}, "two_rms": {Z: len(v) for Z, v in two.items()},
            "tight": {Z: len(v) for Z, v in tight.items()}, "zero_rows": zero_rows,
            "fingerprints": {Z: tuple(round(D[Z][l] % 1, 3) for l in (0, 1, 2)) for Z in range(109, 121)}}


def b5():
    v = lambda M: C * (ME_U / M) / (1 + ME_U / M) / 1e3                            # km/s below the infinite-mass line
    peak = b2()["peak_GHz"]
    return {"H": v(1.00728), "Pb": v(207.2), "U": v(238.03), "SH": (v(300.0), v(270.0)),
            "firas_channel_kms": FIRAS_CHANNEL_CM1 * CM1_GHZ / peak * C / 1e3}


def b6():
    _, bounds = load_index()
    flagged = [Z for Z in range(109, 121)
               if any(("no long-lived isotope" in b) or ("no nuclide synthesised" in b) for b in bounds[Z])]
    return {"flagged": flagged}


def compute():
    return {"b1": b1(), "b1_inj": b1_injected(), "b2": b2(), "b3": b3(), "b4": b4(), "b5": b5(), "b6": b6()}


def report(d):
    a, ai, b, c, e, f, g = d["b1"], d["b1_inj"], d["b2"], d["b3"], d["b4"], d["b5"], d["b6"]
    print("cmbindex.py -- the spectra index against the background radiation (item 142)\n")
    print("B1 FIRAS monopole residuals (Fixsen et al. 1996 Table 4): %d points, sum of (r/sigma)^2 = %.1f (diagonal; "
          "correlations ignored), largest |r/sigma| = %.2f at %.2f cm^-1 -- no line.  Control: a 5-sigma line injected "
          "reads %.2f" % (a["n"], a["chi2_diag"], a["max_abs_z"], a["at"], ai["max_abs_z"]))
    print("B2 Wien x = %.9f; peak %.1f GHz at T0 = %.5f K; FIRAS band %.0f-%.0f GHz"
          % (b["x"], b["peak_GHz"], T0, b["band_GHz"][0], b["band_GHz"][1]))
    print("B3 Rydberg n -> n-1 lines of a neutral atom fall in that band for n = %d to %d; the series limit cancels: %s"
          % (c["n_range"][0], c["n_range"][1], c["limit_free"]))
    print("B4 the Löwdin rows' neutral (s, p, d) defects mod 1, and the witnessed elements (Z <= 108) matching within the "
          "channel equation's rms %.4f / twice it / 0.001:" % RMS_DELTA)
    for Z in range(109, 121):
        print("   Z = %d  %s  %2d / %2d / %d" % (Z, e["fingerprints"][Z], e["one_rms"][Z], e["two_rms"][Z], e["tight"][Z]))
    print("   rows reading delta = 0.0 in every neutral channel (hydrogen-like in the index): %s" % e["zero_rows"])
    print("B5 a Rydberg line sits below the infinite-mass line by: H %.1f km/s, Pb %.3f, U %.3f, mass 270-300 u %.3f-%.3f;"
          " one FIRAS channel at the peak spans %.0f km/s" % (f["H"], f["Pb"], f["U"], f["SH"][0], f["SH"][1],
                                                              f["firas_channel_kms"]))
    print("B6 (the index) neutral rows Z >= 109 marked no long-lived isotope / no nuclide synthesised: %d of 12"
          % len(g["flagged"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    a, ai, b, c, e, f, g = d["b1"], d["b1_inj"], d["b2"], d["b3"], d["b4"], d["b5"], d["b6"]
    chk("B1: every FIRAS monopole residual lies within 2.6 sigma of the blackbody (no line)", a["max_abs_z"] < 2.6)
    chk("B1 control: a line injected at 5 sigma into one channel is flagged (> 3 sigma)", ai["max_abs_z"] > 3)
    chk("B2 (STRUCTURAL): the Wien peak at T0 = 2.72548 K is 160.2 GHz", abs(b["peak_GHz"] - 160.2) < 0.1)
    chk("B3 (STRUCTURAL): a Rydberg n -> n-1 line is the same for any series limit", c["limit_free"])
    chk("B3: Rydberg alpha lines of a neutral atom fill the FIRAS band over a range of n",
        c["n_range"][0] > 10 and c["n_range"][1] < 60)
    chk("B4: at the channel equation's own rms each of Z = 109-118 has at least five witnessed look-alikes",
        min(e["one_rms"][Z] for Z in range(109, 119)) >= 5)
    chk("B4: Z = 119 and 120 each match exactly one witnessed element at that rms -- hydrogen",
        all(lookalikes(load_index()[0], Z, RMS_DELTA) == [1] for Z in (119, 120)))
    chk("B4 control: at a tolerance of 0.001 the same test returns one look-alike or none for every row",
        max(e["tight"].values()) <= 1)
    chk("B4: Z = 119 and 120 read delta = 0.0 in every neutral channel (recorded, not repaired)",
        e["zero_rows"] == [119, 120])
    chk("B5 (STRUCTURAL): a mass of 270-300 u is within 0.3 km/s of lead, against a FIRAS channel of > 10,000 km/s",
        f["Pb"] - f["SH"][1] < 0.3 and f["firas_channel_kms"] > 1e4)
    chk("B6 (READ): the index marks every neutral row Z = 109-120 with no long-lived isotope or no nuclide",
        g["flagged"] == list(range(109, 121)))
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
