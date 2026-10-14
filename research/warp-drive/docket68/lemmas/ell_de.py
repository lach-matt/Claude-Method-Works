#!/usr/bin/env python3
"""ell_de.py -- item 379, option 3: ell tied to the dark energy.  What the literature's tie is, whether it carries over
to the theorem's bulk, what it would fix inside the theorem, and whether the record's window admits it.  Worked in the
conversation (computed, stdlib; READ where marked; search summary where marked; deduced where marked; not verified by a
separate session); 2026-10-14.

  D0 (read) M's words, verbatim in the rulings file, 379: "Let's look at 3 first, and maybe 2 after that".
  D1 (READ; search summary) The literature's tie.  Montero, Vafa and Valenzuela, arXiv:2205.12293v3, READ:
     "l ∼ λΛ^(−1/4) ∼ 1 μm", "we estimate 10^(−4) < λ < 1 or the central region λ ∼ 10^(−1) − 10^(−3)",
     "λ_Casimir = 3ζ(5)/(2π)^6 = 5·10^(−5)", "l ≈ 7.42 μm", "Λ^(−1/4) ≈ 88 μm"; the tie comes from a light Kaluza-Klein
     tower of one compact dimension whose one-loop energy goes as "V_1-loop ∼ m^4 ∼ l^(−4)".  Blumenhagen, Brinkmann and
     Makridou, arXiv:2208.01057v2, READ: "a strongly warped throat with its redshifted KK tower provides a natural string
     theoretic mechanism that realizes the scaling m ∼ Λ^α with the factor α = 1/4, the dark dimension being the one
     along the throat" -- a compact Klebanov-Strassler throat glued to a Calabi-Yau, an anti-D3-brane at its tip.  Cohen,
     Kaplan and Nelson, hep-th/9803132, READ: "L^3 Λ^4 ≲ L M_P^2", and with L the horizon "Λ ∼ 10^(−2.5) eV".  Lee et
     al., arXiv:2002.11761, READ: "λ_d = (ħc/ρ_d)^(1/4) ≈ 85 μm", gravitational-strength Yukawas "< 38.6 μm"; it states
     no bound on a warped bulk's radius.  Its best Yukawa fit, 7.1 um at Delta chi^2 = 3.3 ("None of these Yukawas
     improved χ^2 at the 2σ level"), is not a finding and is not support for anything here.  Kapner et al. 2007 (search
     summary): the 1/r^2 law holds to 56 um; Sundrum's fat graviton, sized at the dark-energy length, was tested by it.
  D2 (deduced) None of these carries over as a mechanism.  The dark dimension's tie is its Casimir energy, which is
     calculable because it depends on the circle's size, a modulus; the throat's needs a tip.  The bulk the theorem
     uses -- FAR's coincident sheets, AdS on each side, no second boundary -- has no compact direction, no tip and no
     modulus: its graviton modes are a continuum, and ell is fixed by the bulk's Lambda5, not a size that can vary.  A
     brane energy hbar c/ell^4 induced by bulk fields exists by dimensional analysis, but as a local term it is absorbed
     in the tension's renormalization, so its coefficient is not calculable there.  The dark energy is the tension's
     detuning dsigma (SMS (18)), set apart from ell.  So in the theorem a dark-energy tie is a postulate, not a
     consequence; Cohen-Kaplan-Nelson's is a bound on local field theory, not a statement about a bulk.  Wall C (the
     global bulk) is open; a compact direction, a tip or a modulus would be new structure.
  D3 (computed) The tie and its window.  Write ell = lam L_DE, L_DE = (hbar c/dsigma)^(1/4) = 88.097 um, which is
     (8 pi/3)^(1/4) sqrt(l_P L_H): the geometric mean of the Planck length and the de Sitter radius L_H = sqrt(3/Lambda4)
     = 1.659e26 m.  The record's window becomes 4.11e-30 <= lam <= 0.15851 (the classical floor 22.4 l_P to the table-top
     ceiling 13.964 um).  The dark dimension's 1e-4 < lam < 1 is ell in 8.81 nm to 88.1 um, 80.0% of it (in log) under
     the ceiling; its central 1e-3 to 1e-1 is 88.1 nm to 8.81 um, all inside; its Casimir value lam_C =
     (3 zeta(5)/(2 pi)^6)^(1/4) = 0.08432 gives ell = 7.43 um, inside, 0.53 of the ceiling.
  D4 (computed; deduced) In 201's coordinates the tie is, exactly, sigma - 2 dsigma = (3/(4 pi lam^2))
     sqrt(sigma_P dsigma): the tension is the geometric mean of the Planck density and the offset, times
     3/(4 pi lam^2).  201's two numbers (sigma, dsigma) become (lam, dsigma), so lam is sigma restated.  The record's
     positions test a universal lam: 2P (l_P x sqrt 2) keeps lam exactly; 2b (G x 2) has lam/sqrt 2.  A universal tie
     would put every 2b step off it, against 246's index and 247.  Read per cell, as 244 and 247 read the criteria, lam
     is each cell's coordinate, and the tie fixes nothing until lam is fixed.
  D5 (computed) What the tie would fix, in the theorem's terms.  Lambda4 ell^2 = 4 pi^2 lam^4/N^2 and Lambda4 l_P^2 =
     2 pi^3 lam^4/N^4, N the CFT's rank of ell_map E1: the dark energy is 1/N^2 in bulk units and 1/N^4 in Planck units;
     L_H = (sqrt 3/(2 pi lam^2)) N ell.  N_L = pi^2 lam^2 sqrt(2/ln2) sqrt(N_max): the two ends meet at the square root
     of the universe's bit cap N_max = 1.5918e122 -- times 0.1192 at lam_C, 0.4212 at the ceiling.  And
     dsigma/(sigma - 2 dsigma) = (4 pi/3) lam^4 (l_P/ell)^2, 1.00e-63 at lam_C.
  D6 (computed) The coefficient-one forms tried are all excluded.  N_L = sqrt(N_max) needs lam = 0.2442 (21.5 um);
     L_H = N ell, 0.5250 (46.3 um); N^4 = N_max, 0.5199 (45.8 um); Cohen-Kaplan-Nelson saturated at L = L_H, ell =
     sqrt(l_P L_H) = 51.8 um (lam 0.588), 116 um with the reduced Planck length.  Each lies 1.54 to 8.3 times above the
     ceiling.  Only lam <= 0.1585 survives; the literature's Casimir 0.0843 does.
  D7 (computed; READ) The numbers the tie would set at lam_C (7.43 um): N 5.76e29, N_L 1.50e60, sigma^(1/4) 1.26e4 GeV,
     and the five-dimensional Planck energy hbar c/l5 = 1.58e9 GeV -- inside the dark dimension's species scale
     "10^9 − 10^10 GeV" (READ), the same formula M5^3 = M_P^2/ell for one extra dimension (deduced).  The small end's
     identity core: r_h 9.08e-21 m, E 1.58e9 J.  The large end's start 6.27e21 kg; the Earth's cap r0/ell 1194.
  D8 (computed) The interior.  Under the tie the Planck span (ell/l_P)^(8/3) is 9.20e81 lam^(8/3): 1.26e79 at lam_C,
     9.2e73 at 1e-3, 2.0e71 at 1e-4.  Option 3 puts ell where the interior is far beyond the runs' reach (2.5e3, the
     span at 18.8 l_P, ell_map E5); item 377's matching approach stays the only route.
  D9 (deduced) What option 3 gives.  It does not fix ell: it trades ell for lam, and nothing in the theory or in the
     warped-bulk literature fixes lam.  It makes ell testable at the table-top: gravity off Newton's law by
     2 ell^2/(3 r^2), ell between 88 nm and 8.8 um on the dark dimension's central band, each factor gained in the
     ceiling cutting lam's top by the same factor.  It and option 2 are the two ends of one family,
     ell = lam l_P^a L_DE^(1-a): option 3 is a = 0, a Planck-scale tension a = 1; at lam = 1 the window admits
     0.026 <= a <= 0.956.

Imports p2_gravity.py and ell_map.py by path.  Stdlib only.
python3 ell_de.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((379, "Let's look at 3 first, and maybe 2 after that"),)
MVV = ("l ∼ λΛ^(−1/4) ∼ 1 μm", "10^(−4) < λ < 1", "λ ∼ 10^(−1) − 10^(−3)", "λ_Casimir = 3ζ(5)/(2π)^6 = 5·10^(−5)",
       "l ≈ 7.42 μm", "Λ^(−1/4) ≈ 88 μm", "10^9 − 10^10 GeV")                 # 2205.12293v3, READ
BBM = "realizes the scaling m ∼ Λ^α with the factor α = 1/4"                     # 2208.01057v2, READ
CKN = ("L^3 Λ^4 ≲ L M_P^2", "Λ ∼ 10^(−2.5) eV")                                  # hep-th/9803132, READ
LEE = ("λ_d = (ħc/ρ_d)^(1/4) ≈ 85 μm", "< 38.6 μm")                              # 2002.11761, READ
MVV_LAM = (1e-4, 1.0)                    # the dark dimension's range for lam
MVV_CENTRAL = (1e-3, 1e-1)               # its central band
MVV_L_READ, MVV_LDE_READ = 7.42e-6, 88e-6
MVV_SPECIES = (1e9, 1e10)                # GeV
_MOD = {}


def _load(path, key):
    if key in _MOD:
        return _MOD[key]
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), HERE, D68]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    _MOD[key] = mod
    return mod


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def compute():
    pg = _load(os.path.join(HERE, "p2_gravity.py"), "de_pg")
    em = _load(os.path.join(HERE, "ell_map.py"), "de_em")
    c, G, hb, LN2, dsig, ceil = pg.C, pg.G, pg.HBAR, pg.LN2, pg.DSIG, pg.ELL_MAX
    h = 2 * math.pi * hb
    eV = 1.602176634e-19
    base = em.compute()
    lP = math.sqrt(hb * G / c ** 3)
    sP = c ** 7 / (hb * G ** 2)
    L4 = 8 * math.pi * G * dsig / c ** 4
    LH = math.sqrt(3 / L4)
    LDE = ((h if MUT.get("de_length_h") else hb) * c / dsig) ** 0.25
    Nmax = sP / ((1.0 if MUT.get("nmax_nats") else 8 * LN2) * dsig)
    zeta5 = sum(n ** -5.0 for n in range(1, 4000))
    lamC4 = 3 * zeta5 / (2 * math.pi) ** 6
    lamC = lamC4 if MUT.get("casimir_no_quarter") else lamC4 ** 0.25
    N = lambda e: math.sqrt((math.pi / 2) * (e / lP) ** 2 * (2.0 if MUT.get("hhr_g4_twice") else 1.0))
    NL = lambda e: (math.pi ** 2 / (2 * LN2)) * (e / lP) ** 2
    span = lambda e: (e / lP) ** (2.0 if MUT.get("span_power_two") else 8 / 3)
    sig_l = lambda e: 3 * c ** 4 / (4 * math.pi * G * e ** 2)                   # SMS (19): sigma - 2 dsigma
    pw = 1.0 if MUT.get("tie_lam_once") else 2.0
    tie_sig = lambda lam: 3 / (4 * math.pi * lam ** pw) * math.sqrt(sP * dsig)
    M5 = lambda e: hb * c / (lP ** 2 * e) ** (1 / 3) / eV / 1e9
    gev = lambda s: (s * (hb * c) ** 3) ** 0.25 / eV / 1e9

    def lam_of(Gx, sig, ds, hx=hb):
        """a universe's lam: its ell (SMS (19)) over its own dark-energy length"""
        e = math.sqrt(3 * c ** 4 / (4 * math.pi * Gx * (sig - 2 * ds)))
        return e / (hx * c / ds) ** 0.25
    sig0 = pg.SIGMA_WINDOW[0]
    lam_ours = lam_of(G, sig0, dsig)
    p2s = 1.0 if MUT.get("p2_G_only") else 0.25        # 2P: l_P x sqrt 2 by G x 2; sigma and offset x 1/4 with sigma_P
    lam_2P = lam_of(2 * G, sig0 * p2s, dsig * p2s) / lam_ours
    lam_2b = lam_of(pg.Q4 * G, sig0, dsig) / lam_ours

    lam_max, lam_floor = ceil / LDE, em.FLOOR_LP * lP / LDE
    ident = {}
    for lam in (1e-4, lamC, 0.1, lam_max):
        e = lam * LDE
        ident[lam] = dict(tie=tie_sig(lam) / sig_l(e) - 1,
                          L4=L4 * e ** 2 / (4 * math.pi ** 2 * lam ** 4 / N(e) ** 2) - 1,
                          L4P=L4 * lP ** 2 / (2 * math.pi ** 3 * lam ** 4 / N(e) ** 4) - 1,
                          NL=NL(e) / math.sqrt(Nmax) / (math.pi ** 2 * lam ** 2 * math.sqrt(2 / LN2)) - 1,
                          LH=LH / (N(e) * e) / (math.sqrt(3) / (2 * math.pi * lam ** 2)) - 1)
    lPr = math.sqrt(8 * math.pi) * lP
    ckn, ckn_r = math.sqrt(lP * LH), math.sqrt(lPr * LH)
    one = {"N_L = sqrt(N_max)": (1 / (math.pi ** 2 * math.sqrt(2 / LN2))) ** 0.5,
           "L_H = N ell": (math.sqrt(3) / (2 * math.pi)) ** 0.5,
           "N^4 = N_max": (1 / (2 * math.pi ** 2 * LN2)) ** 0.25,
           "CKN, L = L_H": ckn / LDE, "CKN, reduced l_P": ckn_r / LDE}
    eC = lamC * LDE
    r = eC / ceil
    at = dict(ell=eC, N=N(eC), NL=NL(eC), NL_sq=NL(eC) / math.sqrt(Nmax), sig14=gev(sig_l(eC) + 2 * dsig),
              M5=M5(eC), ds_rel=dsig / sig_l(eC), rh=base["rh"] * r ** base["pw_rh"],
              E=base["E"] * r ** base["pw_E"], m_start=base["m_start"] * r, earth_q=base["earth_q"] / r)
    spans = {lam: span(lam * LDE) for lam in (1e-4, 1e-3, lamC)}
    lo_ceil = (ceil if not MUT.get("family_positivity") else em.POS_M1 * lP) / LDE
    a_lo = math.log(1 / lo_ceil) / math.log(LDE / lP)
    a_hi = 1 - math.log(em.FLOOR_LP) / math.log(LDE / lP)
    return dict(LDE=LDE, LH=LH, LDE_geo=(8 * math.pi / 3) ** 0.25 * math.sqrt(lP * LH) / LDE - 1, Nmax=Nmax,
                lamC=lamC, lamC4=lamC4, lam_max=lam_max, lam_floor=lam_floor,
                mvv_frac=math.log10(lam_max / MVV_LAM[0]) / math.log10(MVV_LAM[1] / MVV_LAM[0]),
                mvv_ell=tuple(x * LDE for x in MVV_LAM), mvv_central=tuple(x * LDE for x in MVV_CENTRAL),
                lam_2P=lam_2P, lam_2b=lam_2b, ident=ident, one=one, ckn=ckn, ckn_r=ckn_r, at=at,
                NL_sq_ceil=NL(ceil) / math.sqrt(Nmax), span_coef=(LDE / lP) ** (8 / 3), spans=spans,
                floor_span=span(em.FLOOR_LP * lP), runs_k=em.RUNS_K, a_lo=a_lo, a_hi=a_hi)


def report(o):
    print("ell_de.py -- ell tied to the dark energy (item 379, option 3)\n")
    print("D3 L_DE = %.5e m (geometric mean of l_P and L_H = %.4e m, rel %.1e); lam in [%.3e, %.5f]"
          % (o["LDE"], o["LH"], o["LDE_geo"], o["lam_floor"], o["lam_max"]))
    print("D3 dark dimension 1e-4..1: ell %.3e..%.3e m (%.1f%% of its log-range under the ceiling); central %.3e..%.3e"
          % (o["mvv_ell"][0], o["mvv_ell"][1], 100 * o["mvv_frac"], o["mvv_central"][0], o["mvv_central"][1]))
    print("D3 Casimir lam_C^4 = %.4e, lam_C = %.5f: ell = %.4e m; at the read 88 um, %.3e m"
          % (o["lamC4"], o["lamC"], o["at"]["ell"], o["lamC"] * MVV_LDE_READ))
    print("D4 2P keeps lam (x %.12f); 2b has lam x %.6f" % (o["lam_2P"], o["lam_2b"]))
    for lam, d in o["ident"].items():
        print("D4/D5 lam %.4g: rel. residues tie %.1e, L4 ell^2 %.1e, L4 l_P^2 %.1e, N_L %.1e, L_H %.1e"
              % (lam, d["tie"], d["L4"], d["L4P"], d["NL"], d["LH"]))
    print("D5 N_max %.5e; N_L/sqrt(N_max) %.4f at lam_C, %.4f at the ceiling; dsigma/(sigma - 2 dsigma) %.3e"
          % (o["Nmax"], o["at"]["NL_sq"], o["NL_sq_ceil"], o["at"]["ds_rel"]))
    for k, lam in o["one"].items():
        print("D6 %-18s lam %.4f, ell %.4e m, %.2f x the ceiling" % (k, lam, lam * o["LDE"], lam / o["lam_max"]))
    a = o["at"]
    print("D7 at lam_C: N %.3e, N_L %.3e, sigma^(1/4) %.3e GeV, hbar c/l5 %.3e GeV; r_h %.3e m, E %.3e J; start %.3e kg;"
          " Earth's cap %.0f ell" % (a["N"], a["NL"], a["sig14"], a["M5"], a["rh"], a["E"], a["m_start"], a["earth_q"]))
    print("D8 span = %.3e lam^(8/3): %s; at the floor %.3e > the runs' %.1e"
          % (o["span_coef"], ", ".join("%.3e at %.4g" % (v, k) for k, v in o["spans"].items()), o["floor_span"],
             o["runs_k"]))
    print("D9 ell = lam l_P^a L_DE^(1-a) at lam = 1: the window admits %.3f <= a <= %.3f" % (o["a_lo"], o["a_hi"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    a = o["at"]
    add("D0 379 verbatim inside its own item", all(" ".join(t.split()) in _item(n) for n, t in WORDS))
    add("D1 the reads agree with the computed: lam_C^4 = 5e-5, lam_C x 88 um = 7.42 um, L_DE 88 um (Lee's 85 um at "
        "his rho_d); species scale at lam_C inside 1e9-1e10 GeV", "%.0e" % o["lamC4"] == "5e-05"
        and "%.3g" % (o["lamC"] * MVV_LDE_READ) == "%.3g" % MVV_L_READ and round(o["LDE"] * 1e6) == 88
        and MVV_SPECIES[0] < a["M5"] < MVV_SPECIES[1] and len(MVV) == 7 and BBM and len(CKN) == 2 and len(LEE) == 2)
    add("D3 the window: L_DE 88.097 um = (8pi/3)^(1/4) sqrt(l_P L_H) (L_H 1.659e26 m); lam in [4.11e-30, 0.15851]; "
        "80.0% of the dark dimension's range; lam_C 0.08432, ell 7.43 um",
        "%.5g" % (o["LDE"] * 1e6) == "88.097" and abs(o["LDE_geo"]) < 1e-12 and "%.4g" % o["LH"] == "1.659e+26"
        and "%.3g" % o["lam_floor"] == "4.11e-30" and "%.5f" % o["lam_max"] == "0.15851"
        and "%.3f" % o["mvv_frac"] == "0.800" and "%.4g" % o["lamC"] == "0.08432"
        and "%.3g" % (a["ell"] * 1e6) == "7.43" and o["mvv_central"][1] < o["lam_max"] * o["LDE"])
    add("D4 the tie is exactly sigma - 2 dsigma = (3/(4 pi lam^2)) sqrt(sigma_P dsigma); 2P keeps lam, 2b lam/sqrt 2",
        all(abs(d["tie"]) < 1e-12 for d in o["ident"].values()) and abs(o["lam_2P"] - 1) < 1e-12
        and abs(o["lam_2b"] - 2 ** -0.5) < 1e-12)
    add("D5 Lambda4 ell^2 = 4pi^2 lam^4/N^2, Lambda4 l_P^2 = 2pi^3 lam^4/N^4, N_L = pi^2 lam^2 sqrt(2/ln2) sqrt(N_max), "
        "L_H = (sqrt3/(2pi lam^2)) N ell; N_max 1.5918e122; 0.1192 and 0.4212; 1.00e-63",
        all(abs(d[k]) < 1e-12 for d in o["ident"].values() for k in ("L4", "L4P", "NL", "LH"))
        and "%.5g" % o["Nmax"] == "1.5918e+122" and "%.4f" % a["NL_sq"] == "0.1192"
        and "%.4f" % o["NL_sq_ceil"] == "0.4212" and "%.3g" % a["ds_rel"] == "1e-63")
    one = o["one"]
    add("D6 coefficient-one forms: 0.2442 (21.5 um), 0.5250, 0.5199, CKN 51.8 um (0.588), 116 um reduced; all above "
        "the ceiling", "%.4f" % one["N_L = sqrt(N_max)"] == "0.2442" and "%.4f" % one["L_H = N ell"] == "0.5250"
        and "%.4f" % one["N^4 = N_max"] == "0.5199" and "%.3g" % (o["ckn"] * 1e6) == "51.8"
        and "%.3g" % one["CKN, L = L_H"] == "0.588" and "%.3g" % (o["ckn_r"] * 1e6) == "116"
        and "%.3g" % (one["N_L = sqrt(N_max)"] * o["LDE"] * 1e6) == "21.5"
        and min(one.values()) / o["lam_max"] > 1.5 and o["lamC"] < o["lam_max"])
    add("D7 at lam_C: N 5.76e29, N_L 1.50e60, sigma^(1/4) 1.26e4 GeV, hbar c/l5 1.58e9 GeV, r_h 9.08e-21 m, E 1.58e9 J, "
        "start 6.27e21 kg, the Earth's cap 1194 ell", "%.3g" % a["N"] == "5.76e+29" and "%.3g" % a["NL"] == "1.5e+60"
        and "%.3g" % a["sig14"] == "1.26e+04" and "%.3g" % a["M5"] == "1.58e+09" and "%.3g" % a["rh"] == "9.08e-21"
        and "%.3g" % a["E"] == "1.58e+09" and "%.3g" % a["m_start"] == "6.27e+21" and round(a["earth_q"]) == 1194)
    sp = o["spans"]
    add("D8 the span 9.20e81 lam^(8/3): 1.26e79 at lam_C, 9.2e73 at 1e-3, 2.0e71 at 1e-4; above the runs' reach even "
        "at the floor", "%.3g" % o["span_coef"] == "9.2e+81" and "%.3g" % sp[o["lamC"]] == "1.26e+79"
        and "%.2g" % sp[1e-3] == "9.2e+73" and "%.2g" % sp[1e-4] == "2e+71" and o["floor_span"] > o["runs_k"])
    add("D9 the family ell = lam l_P^a L_DE^(1-a): the window at lam = 1 admits 0.026 <= a <= 0.956",
        "%.3f" % o["a_lo"] == "0.026" and "%.3f" % o["a_hi"] == "0.956")
    return res


MUTANTS = {"casimir_no_quarter": "the dark dimension's lam taken as lam_Casimir, not its fourth root (D1, D3, D7)",
           "de_length_h": "the dark-energy length with h for hbar (D1, D3)",
           "hhr_g4_twice": "HHR's N read with G4 = 2 G5/ell, the other brane convention (D5, D7)",
           "nmax_nats": "N_max without its 8 ln2, the bit cap mistaken (D5)",
           "tie_lam_once": "the tie in 201's coordinates with lam to the first power (D4)",
           "p2_G_only": "2P as G x 2 alone, sigma and the offset left unscaled (D4)",
           "span_power_two": "the Planck span as (ell/l_P)^2, not (ell/l5)^4 = (ell/l_P)^(8/3) (D8)",
           "family_positivity": "the family's lower end taken at positivity, not at the table-top ceiling (D9)"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-18s %-70s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
