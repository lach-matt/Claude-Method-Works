#!/usr/bin/env python3
"""ell_fix.py -- item 380, "I don't believe in free variables": every number the theorem uses and what fixes it, why
no row of the theorem can fix ell, what the theory's own scales and objects would give it with no free coefficient, and
which kinds of object fix a scale without one.  Worked in the conversation (computed, stdlib; READ where marked; deduced
and estimate where marked; not verified by a separate session); 2026-10-14.

  X0 (read) M's words, verbatim in the rulings file: 380 "I don't believe in free variables"; 140 "Our math is not
     dependent on k, k is dependent on our work".
  X1 (computed; the record) The audit.  Of the numbers the theorem uses, c and h are exact; G and the offset dsigma =
     rho_Lambda c^2 are measured; the README's N is the object's (130 (2)); k_R = k_L/2 and position 2's -sigma/4 are
     the work's (B6, 139 (1)); position 2's offset is derived (322); alpha = 0 is relativity's (326); the Earth's mass
     is measured and its README (A) an estimate (372).  One number is fixed by nothing yet: sigma, our plane's tension,
     inside its window.  Every other name ell carries is that number: k = 1/ell, G5 = G ell, Lambda5 = -6/ell^2,
     l5 = (l_P^2 ell)^(1/3), the dual rank N, the crossover N_L, and 379's lam.  One threshold is the board's own: the
     classical floor's 1 % (m1_large: the bulk's curvature 40 (l_P/ell)^(8/3) below 1 % of the Planck scale).
  X2 (computed; deduced) No row can fix it.  The theorem is stated in N and ell, and its invariants do not move with ell
     (for the identity core the small end's r_h/l5 = 72762.24 and E G5/(c^4 l5^2) = 6.2373e9; the large end's E/E1 =
     sqrt N).  Every condition the record puts on ell is an inequality: positivity ell > 2.0 l_P (197); the bulk below
     the Planck curvature, ell > 4.0 l_P; the board's 1 % floor, ell >= 22.4 l_P; the table-top, ell <= 13.964 um.
     Even from the board's floor the window spans 28.6 decades, and nothing in it picks a point.
  [Item 381 (ell_positivity Y1-Y5): the positivity floor ell > 8.5415 m1 = 2.0 l_P is item 197's, for position 2's
     plane held at a depth; under 275 the planes coincide everywhere, the floor has no premise and is withdrawn, and
     B5a holds at every ell.  Kept as written; the window's change is put to M.]
  X3 (computed) The theory's two given scales, at coefficient one.  A tie to the dark energy gives 21.5 to 116 um (379
     D6), above the ceiling in every form tried.  A tension at a Planck density -- the plane's vacuum energy at its own
     cutoff -- gives ell = 0.117 l_P (the five-dimensional density), 0.489 l_P (the four-dimensional) or 12.3 l_P (the
     reduced, 8 pi G = 1): the first two below positivity and the Planck curvature; the third above both, below only the
     board's 1 % floor.  So "coefficient one" is itself a convention: which Planck density is taken moves ell by 105.
  X4 (computed; deduced) The one coefficient-one value the record's physics leaves standing: the plane's tension equal
     to the Planck energy density in Einstein's own coupling, sigma = c^7/(hbar (8 pi G)^2), so ell = sqrt(48 pi) l_P =
     12.28 l_P = 1.985e-34 m.  Its bulk sits at 5.0 % of the Planck curvature (B8 makes the bulk's law Einstein's
     exactly; 353's M-PLANCK-ENDS governs Planck-scale places).  The dual rank there is 15.39 (not an integer) and the
     crossover N_L = 1074 bits: the identity core (2.7e15 bits) and the Earth's README sit at the large end, which
     starts at 1.67e-7 kg.  The interior's Planck span there is 803, inside the runs' 2.5e3.
  X5 (computed; estimate) The other objects the record holds that carry a length.  The Earth (372): its README (A) at
     the crossover, N_L = A, gives ell = 0.584 nm (A is an estimate, order 1e51-1e52 bits: ell 0.19 to 0.61 nm); its
     crossover N* at the crossover gives 7.08 mm, which is also its corridor at the large end's start, above the
     ceiling.  The Higgs (322): the five-dimensional Planck energy at the quartic's zero, 3.68e10 GeV at m_t = 172.57
     GeV, gives ell = 0.588 nm; within the top mass's 1 sigma (0.29 GeV) it runs from 0.024 to 9.6 nm, and it is 8 pi
     smaller with the reduced Planck length.  The two agree to 0.8 %.  That is a coincidence, recorded and not proposed:
     nothing relates the Earth's mass to the Higgs quartic, A is known to a factor of a few, and the Higgs value moves
     by a factor 390 within 1 sigma.
  X6 (READ; deduced; computed) The kinds of object that fix a scale with no free variable, and what the record holds:
     - observation (247): fixes ell as it fixed G and rho_Lambda.  At 52 um the correction 2 ell^2/(3 r^2) is 4.8 % at
       the ceiling, 2.5e-4 at 1 um and 8.5e-11 at 0.59 nm: present tests reach only the window's top (estimate);
     - an equality from relativity or consistency, as 326 found for alpha: none in the record (X2);
     - an integer fixed by topology.  In the one framework where ell is not a parameter, AdS/CFT from branes, ell in
       Planck units is the dual rank, ell/l_P = N sqrt(2/pi) (Hawking, Hertog and Reall (2.2), READ in ell_map), and N
       is set by a tadpole the manifold's topology fixes.  Giddings, Kachru and Polchinski, hep-th/0105097, READ:
       "χ(X)/24 = N_D3 + (1/(2κ_10^2 T_3)) ∫ H_3 ∧ F_3"; "It is not possible to take N to be parametrically large,
       because the negative contributions to the Bianchi identity are determined by the topology of the manifold"; in
       their example "MK = N ≤ 72".  Through HHR's relation (stated for the non-compact bulk), N from 28 to 72 is ell
       from 22.3 to 57.4 l_P, the window's floor, where the interior's Planck span is 3.96e3 to 4.91e4 against the
       runs' 2.5e3.  The same paper keeps a modulus free classically ("the overall radius of the compact dimensions is
       always left unfixed"), so an integer is not the whole story there either;
     - a natural unit: X4's value, if Einstein's own coupling is taken as the theory's unit;
     - the work (140): the Earth's value (X5) is the one length the work supplies; which point of the family the cap
       must occupy is stated by no ruling, so it is M's to rule on, and the board does not propose it.
  X7 (deduced) Under 380 the theorem is missing one object.  No row can supply it (X2).  Of the no-coefficient values,
     the dark-energy ties miss the window above and two of the three Planck ties miss it below; one, X4's, stands, and
     only the board's own 1 % threshold sets it aside.  The integer kind puts ell at the same end.  Both point to option
     2's end of the window, where the interior comes within the runs' reach.

Imports p2_gravity.py, ell_map.py, ell_de.py, earth_cap.py and p2_offset.py by path.  Stdlib only.
python3 ell_fix.py [--selftest | --mutants]
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
WORDS = ((380, "I don't believe in free variables"), (140, "Our math is not dependent on k, k is dependent on our work"))
GKP = ("χ(X)/24 = N_D3 + (1/(2κ_10^2 T_3)) ∫ H_3 ∧ F_3",
       "It is not possible to take N to be parametrically large, because the negative contributions to the Bianchi "
       "identity are determined by the topology of the manifold", "MK = N ≤ 72",
       "the overall radius of the compact dimensions is always left unfixed")          # hep-th/0105097, READ
GKP_N = (28, 72)                         # the classical floor's rank (ell_map E3) and GKP's example bound
A_RANGE = (1e51, 1e52)                   # earth_cap K5: the Earth's README, order of magnitude (estimate)
MT, MT_SIG, MH, A3 = 172.57, 0.29, 125.09, 0.1180       # p2_offset's inputs: PDG 2024 top, M's Higgs, alpha_s
R_TEST = 52e-6                           # the shortest separation of the table-top tests (Lee et al. 2020, READ in 379)
# the audit: (name, what fixes it, status)
AUDIT = (("c", "exact (SI)", "exact"), ("h", "exact (SI)", "exact"), ("G", "CODATA", "measured"),
         ("dsigma = rho_Lambda c^2", "201; rho_Lambda observed", "measured"), ("N", "the object (130 (2))", "object"),
         ("E(N)", "G1, from N", "derived"), ("k_R = k_L/2", "B6, 200 (1)", "work"),
         ("position 2's plane -sigma/4", "139 (1)", "work"), ("position 2's offset", "322, the junction", "derived"),
         ("alpha (Gauss-Bonnet)", "326, relativity", "relativity"), ("M_earth", "IERS GM", "measured"),
         ("A (the Earth's README)", "372, K5", "estimate"), ("sigma (ell)", "nothing yet; the window", "unfixed"),
         ("the classical floor's 1 %", "m1_large, the board's threshold", "board"))
ELL_NAMES = ("k", "G5", "Lambda5", "l5", "N_CFT", "N_L", "lam")
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
    pg = _load(os.path.join(HERE, "p2_gravity.py"), "fx_pg")
    em = _load(os.path.join(HERE, "ell_map.py"), "fx_em")
    de = _load(os.path.join(HERE, "ell_de.py"), "fx_de")
    ec = _load(os.path.join(HERE, "earth_cap.py"), "fx_ec")
    po = _load(os.path.join(HERE, "p2_offset.py"), "fx_po")
    c, G, hb, LN2, dsig, ceil = pg.C, pg.G, pg.HBAR, pg.LN2, pg.DSIG, pg.ELL_MAX
    h, eV = 2 * math.pi * hb, 1.602176634e-19
    lP = math.sqrt(hb * G / c ** 3)
    m1 = lP * math.sqrt(LN2 / math.pi) / 2
    pos, floor = em.POS_M1 * m1, em.FLOOR_LP * lP
    planck_floor = 40 ** (3 / 8) * lP                    # 40 (l_P/ell)^(8/3) = 1: the bulk at the Planck curvature

    # X1: every name ell carries, as a function of ell alone (given c, hbar, G, dsigma)
    names = lambda e: dict(k=1 / e, G5=G * e, Lambda5=-6 / e ** 2, l5=(lP ** 2 * e) ** (1 / 3),
                           N_CFT=math.sqrt(math.pi / 2) * e / lP, N_L=math.pi ** 2 / (2 * LN2) * (e / lP) ** 2,
                           lam=e / (hb * c / dsig) ** 0.25)
    n1, n2 = names(1e-12), names(2e-12)
    unfixed = [a for a in AUDIT if a[2] == "unfixed"]
    board = [a for a in AUDIT if a[2] == "board"]

    # X2: invariants at two ell
    def inv(e, N=2.7426e15):
        l5 = (lP ** 2 * e) ** (1 / 3)
        rh = (2 * N * LN2 / math.pi ** 2) ** (1 / 3) * l5
        G5 = G * (ceil if MUT.get("g5_fixed_length") else e)      # the theorem: G5 = G ell
        E = 3 * math.pi * c ** 4 * rh ** 2 / (8 * G5)
        return rh / l5, E * G * e / (c ** 4 * l5 ** 2)
    i1, i2 = inv(1e-12), inv(1e-6)
    decades = math.log10(ceil / floor)

    # X3: the Planck end (sigma = hbar c / L^4 with SMS (19): ell^2 = 3 c^4/(4 pi G sigma))
    k3 = 3 / (4 * math.pi)
    p5 = k3 ** 1.5 * lP                                   # L = l5: ell^(2/3) = (3/(4 pi)) l_P^(2/3)
    p4 = k3 ** (1.0 if MUT.get("planck_no_root") else 0.5) * lP
    pr = k3 ** 0.5 * 8 * math.pi * lP                    # L = sqrt(8 pi) l_P
    red = math.sqrt((12 if MUT.get("red_4piG") else 48) * math.pi) * lP   # sigma = c^7/(hbar (8 pi G)^2) in SMS (19)
    cand = dict(ell=red, lp=red / lP, curv=40 * (lP / red) ** (8 / 3), N=math.sqrt(math.pi / 2) * red / lP,
                NL=math.pi ** 2 / (2 * LN2) * (red / lP) ** 2, start=red * c ** 2 / (em.START * G),
                span=(red / lP) ** (8 / 3), sig=c ** 7 / (hb * (8 * math.pi * G) ** 2))
    # the mutant red_4piG takes (4 pi G)^2 in ell but keeps sig: sig_check then fails
    cand["sig_check"] = 3 * c ** 4 / (4 * math.pi * G * red ** 2) / cand["sig"] - 1
    dO = de.compute()
    de_lo = min(dO["one"].values()) * dO["LDE"]
    de_hi = max(dO["one"].values()) * dO["LDE"]

    # X4: the Earth and the Higgs
    M_E = ec.GM_EARTH / G
    A = ec.SNAPSHOT[0] * M_E / ec.SNAPSHOT[1]
    Nstar = 8 * math.pi ** 2 * G * M_E ** 2 / (h * c * LN2)
    ell_of_NL = lambda n: lP * math.sqrt(n * 2 * LN2 / math.pi ** 2)
    ell_A, ell_Ns = ell_of_NL(A), ell_of_NL(Nstar)
    ell_A_rng = tuple(ell_of_NL(a) for a in A_RANGE)
    start_earth = ec.ELL_START * G * M_E / c ** 2          # ell at which the Earth's corridor starts the large end
    lpx = math.sqrt(8 * math.pi) * lP if MUT.get("higgs_reduced") else lP
    ell_M5 = lambda E_GeV: (hb * c / (E_GeV * 1e9 * eV)) ** 3 / lpx ** 2
    cross = {mt: po.quartic(MH, mt, A3)["cross"] for mt in (MT - MT_SIG, MT, MT + MT_SIG)}
    ell_H = {mt: ell_M5(E) for mt, E in cross.items()}
    ell_H_red = ell_M5(cross[MT]) / (8 * math.pi)

    # X5: observation's reach, and the integer kind through HHR
    corr = lambda e: 2 * e ** 2 / (3 * R_TEST ** 2)
    ellN = lambda N: N * math.sqrt(2 / math.pi) * lP
    span = lambda e: (e / lP) ** (8 / 3)
    return dict(unfixed=unfixed, board=board, planck_floor=planck_floor / lP, cand=cand,
                moved=[k for k in ELL_NAMES if n1[k] != n2[k]], audit_n=len(AUDIT),
                inv1=i1, inv2=i2, pos=pos / lP, floor=floor / lP, ceil=ceil, decades=decades,
                p5=p5 / lP, p4=p4 / lP, pr=pr / lP, de_lo=de_lo, de_hi=de_hi,
                A=A, Nstar=Nstar, ell_A=ell_A, ell_Ns=ell_Ns, ell_A_rng=ell_A_rng, start_earth=start_earth,
                cross=cross, ell_H=ell_H, ell_H_red=ell_H_red, coinc=ell_H[MT] / ell_A - 1,
                h_spread=max(ell_H.values()) / min(ell_H.values()),
                corr=dict(ceil=corr(ceil), um=corr(1e-6), H=corr(ell_H[MT])),
                gkp_ell=tuple(ellN(N) / lP for N in GKP_N), gkp_span=tuple(span(ellN(N)) for N in GKP_N),
                runs_k=em.RUNS_K)


def report(o):
    print("ell_fix.py -- what fixes ell (item 380)\n")
    print("X1 %d numbers audited; unfixed: %s; ell's names that move with it: %s"
          % (o["audit_n"], ", ".join(a[0] for a in o["unfixed"]), ", ".join(o["moved"])))
    print("X2 invariants at ell = 1e-12 and 1e-6 m: r_h/l5 %.6f / %.6f, E G5/(c^4 l5^2) %.6f / %.6f"
          % (o["inv1"][0], o["inv2"][0], o["inv1"][1], o["inv2"][1]))
    print("X2 floors: positivity %.2f l_P, Planck curvature %.2f l_P, the board's 1 %% %.1f l_P; ceiling %.3e m: %.1f "
          "decades" % (o["pos"], o["planck_floor"], o["floor"], o["ceil"], o["decades"]))
    print("X3 Planck end: %.4f, %.4f, %.2f l_P (all below %.1f l_P); dark-energy end: %.3e to %.3e m (above %.3e m)"
          % (o["p5"], o["p4"], o["pr"], o["floor"], o["de_lo"], o["de_hi"], o["ceil"]))
    cd = o["cand"]
    print("X4 reduced Planck tension %.4e J/m^3 (SMS (19) rel %.1e): ell %.4f l_P = %.4e m; curvature %.2f %% of Planck;"
          " N %.2f; N_L %.0f bits; large end from %.3e kg; span %.0f" % (cd["sig"], cd["sig_check"], cd["lp"], cd["ell"],
                                                                     100 * cd["curv"], cd["N"], cd["NL"], cd["start"],
                                                                     cd["span"]))
    print("X5 Earth: A %.3e bits -> ell %.4e m (range %.2e-%.2e); N* %.4e -> %.4e m; the Earth starts the large end"
          " at %.4e m" % (o["A"], o["ell_A"], o["ell_A_rng"][0], o["ell_A_rng"][1], o["Nstar"], o["ell_Ns"],
                         o["start_earth"]))
    print("X5 Higgs: quartic zero %s GeV -> ell %s m; reduced %.3e m; spread x%.0f; Higgs vs Earth %+.2f %%"
          % (" / ".join("%.3e" % v for v in o["cross"].values()), " / ".join("%.3e" % v for v in o["ell_H"].values()),
             o["ell_H_red"], o["h_spread"], 100 * o["coinc"]))
    print("X6 table-top at 52 um: %.3g (ceiling), %.3g (1 um), %.3g (the Higgs value)"
          % (o["corr"]["ceil"], o["corr"]["um"], o["corr"]["H"]))
    print("X6 integer kind: N %d..%d -> ell %.1f..%.1f l_P; Planck span %.3e..%.3e (runs %.1e)"
          % (GKP_N[0], GKP_N[1], o["gkp_ell"][0], o["gkp_ell"][1], o["gkp_span"][0], o["gkp_span"][1], o["runs_k"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("X0 380 and 140 verbatim inside their own items", all(" ".join(t.split()) in _item(n) for n, t in WORDS))
    add("X1 fourteen entries audited: one unfixed number (sigma), one board threshold (the 1 % floor); every name ell "
        "carries moves with it", o["audit_n"] == 14 and [a[0] for a in o["unfixed"]] == ["sigma (ell)"]
        and [a[0] for a in o["board"]] == ["the classical floor's 1 %"] and o["moved"] == list(ELL_NAMES))
    add("X2 the invariants do not move with ell; floors 2.0, 4.0 and 22.4 l_P, ceiling 13.964 um: 28.6 decades from "
        "the board's floor", abs(o["inv1"][0] / o["inv2"][0] - 1) < 1e-12
        and abs(o["inv1"][1] / o["inv2"][1] - 1) < 1e-12 and "%.7g" % o["inv1"][0] == "72762.24"
        and "%.5g" % o["inv1"][1] == "6.2373e+09" and "%.2g" % o["pos"] == "2" and "%.2g" % o["planck_floor"] == "4"
        and "%.3g" % o["floor"] == "22.4" and "%.1f" % o["decades"] == "28.6")
    add("X3 Planck ties 0.117 and 0.489 l_P below positivity and the Planck curvature, 12.3 l_P between them and the "
        "board's floor; dark-energy ties 21.5-116 um above the ceiling; the convention moves ell by 105",
        "%.3g" % o["p5"] == "0.117" and "%.3g" % o["p4"] == "0.489" and "%.3g" % o["pr"] == "12.3"
        and max(o["p5"], o["p4"]) < o["pos"] < o["planck_floor"] < o["pr"] < o["floor"]
        and "%.3g" % (o["de_lo"] * 1e6) == "21.5" and "%.3g" % (o["de_hi"] * 1e6) == "116" and o["de_lo"] > o["ceil"]
        and round(o["pr"] / o["p5"]) == 105)
    cd = o["cand"]
    add("X4 the reduced Planck tension: ell = sqrt(48 pi) l_P = 12.28 l_P (1.985e-34 m), curvature 5.0 % of Planck, "
        "N 15.39, N_L 1074 bits, the large end from 1.67e-7 kg, span 803 inside the runs' 2.5e3",
        abs(cd["sig_check"]) < 1e-12 and "%.4g" % cd["lp"] == "12.28" and "%.4g" % cd["ell"] == "1.985e-34"
        and "%.2g" % cd["curv"] == "0.05" and "%.4g" % cd["N"] == "15.39" and round(cd["NL"]) == 1074
        and "%.3g" % cd["start"] == "1.67e-07" and round(cd["span"]) == 803 and cd["span"] < o["runs_k"])
    add("X5 the Earth: N_L = A at 0.584 nm (0.19-0.61 nm); N* and the large end's start at 7.08 mm, above the ceiling",
        "%.3g" % o["ell_A"] == "5.84e-10" and "%.2g" % o["ell_A_rng"][0] == "1.9e-10"
        and "%.2g" % o["ell_A_rng"][1] == "6.1e-10" and "%.3g" % o["ell_Ns"] == "0.00708"
        and abs(o["ell_Ns"] / o["start_earth"] - 1) < 2e-3 and o["ell_Ns"] > o["ceil"])
    eh = o["ell_H"]
    add("X5 the Higgs: zero at 3.68e10 GeV, ell 0.588 nm; 0.024-9.6 nm within 1 sigma; 8 pi less reduced; 0.8 % "
        "from the Earth's, a coincidence", "%.3g" % o["cross"][MT] == "3.68e+10" and "%.3g" % eh[MT] == "5.88e-10"
        and "%.2g" % eh[MT - MT_SIG] == "2.4e-11" and "%.2g" % eh[MT + MT_SIG] == "9.6e-09"
        and "%.2g" % o["ell_H_red"] == "2.3e-11" and "%.1f" % (100 * abs(o["coinc"])) == "0.8"
        and o["h_spread"] > 300)
    add("X6 observation: 4.8 % at the ceiling, 2.5e-4 at 1 um, 8.5e-11 at the Higgs value (52 um)",
        "%.2g" % o["corr"]["ceil"] == "0.048" and "%.2g" % o["corr"]["um"] == "0.00025"
        and "%.2g" % o["corr"]["H"] == "8.5e-11")
    add("X6 the integer kind: N 28-72 is ell 22.3-57.4 l_P, the floor; span 3.96e3-4.91e4 against the runs' 2.5e3",
        "%.3g" % o["gkp_ell"][0] == "22.3" and "%.3g" % o["gkp_ell"][1] == "57.4"
        and "%.3g" % o["gkp_span"][0] == "3.96e+03" and "%.3g" % o["gkp_span"][1] == "4.91e+04"
        and o["gkp_span"][0] < 2 * o["runs_k"] and len(GKP) == 4)
    return res


MUTANTS = {"g5_fixed_length": "the small end's E with G5 = G x a fixed length, not G ell: not covariant (X2)",
           "planck_no_root": "the four-dimensional Planck tension's ell without its square root (X3)",
           "higgs_reduced": "the Higgs tie taken with the reduced Planck length by default (X5, X6)",
           "red_4piG": "the reduced Planck tension's ell with (4 pi G)^2 in place of (8 pi G)^2 (X4)"}


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
        print("  mutant %-15s %-70s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
