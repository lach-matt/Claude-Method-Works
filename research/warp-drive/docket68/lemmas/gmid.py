#!/usr/bin/env python3
"""gmid.py -- item 542, lemma GMID: the corridor's family through the middle.  M, 542, to the gaps: "add lemmas to
close these gaps. nothing gets narrowed, only expanded to complete the statement".  The statement's scope is every N
>= 7.12e9 with exactly one static corridor; the rows covered the two ends, and corridor_family's verifier (261) found
neither end controlled for r_h > 0.1 ell and r0 < 10 ell, E(N) there "published in neither paper read".  This file
computes the family through that band with corridor_p2's Einstein-DeTurck solver (which reproduces Figueras and
Wiseman's uncharged hole, item 455).  Units ell = G5 = c = 1.  Labels: computed (exact unless marked numerical), READ,
deduced, M's.

  G0 (read) M's words, verbatim in the rulings file, 542.
  G1 (computed, numerical) The family's members from bt = 0.12 to 20 (T = 1/(4 pi bt ell), the brane radius R4 from
     0.198 to 20.0 ell) at two resolutions, N = 20 and N = 24 (pinned in data/gmid_N20.json, gmid_N24.json; a live
     solve at N = 16 checks the pin): Newton residual below 1e-7 at every member; the DeTurck vector's norm xi^2 below
     1.5e-4 at N = 24 at every member but bt = 14 (2.3e-3), falling with N where both are resolved; the two
     resolutions agree on R4 to 4.3e-3 and on the horizon's area to 1.1e-2 at worst (bt = 0.4), to 8e-4 at the median.
     Below R4 = 0.2 ell the members are G0s's (Tangherlini to first order in r_h/ell).
  G2 (computed) One member per temperature, one per entropy: R4 and the area increase strictly with bt at both
     resolutions -- no fold, so no zero mode along the family and no second branch meeting it -- and the surface
     gravity 1/(2 bt ell) is positive at every member.  Since S = A/(4 G5) increases and T > 0, E(N) is single-valued
     and increasing (dE/dN = T ln2 > 0).
  G3 (computed) The ends, matched.  At the small end the area falls below Tangherlini's, 1 - A/(2 pi^2 R4^3) = 0.60
     (R4/ell) at the four smallest members to 1% and identically at both resolutions: a deviation first order in r_h/ell,
     G0s's.  At the large end A/(4 pi R4^2) = 0.998 and bt/R4 = 1.000 at R4 = 20 ell: four-dimensional Schwarzschild
     (T = 1/(4 pi R4)), its corrections O((ell/R4)^2).
  G4 (computed, numerical) The first law through the middle.  E anchored at the smallest member on the small end's E =
     3 pi r_h^2/8 (from its S), carried up by dE = T dS (monotone cubic in log bt), arrives at the largest member at
     the large end's E = (S/4 pi)^(1/2) to 2.2e-4 at N = 24 and 7e-4 at N = 20: the family is one thermodynamic object,
     its two end laws joined by its own temperature, the area law S = N ln2 at every member.
  G5 (computed) E(N) through the band, at the window's top (ell = 13.964 um): N = A ell^2/(4 l_P^2 ln2), E = E_d ell
     c^4/G.  At R4 = 10 ell the family gives N = 3.37e62 and E = 8.44e39 J against the large end's 3.38e62 and 8.45e39 J
     at r0 = 10 ell; at its smallest member, R4 = 0.198 ell, N = 3.62e58 and E = 7.15e37 J (the anchor).
  G6 (READ) Figueras and Wiseman (1105.2558v2, READ): "we have been able to construct braneworld black holes with
     R4/ell in [0.07, 20]" (p. 3), "the inverse temperature as beta = 4 pi beta~ ell" (p. 3), and "for all our
     solutions there is a single negative mode, which for small R4/ell tends to the usual negative mode of 5d
     asymptotically flat Schwarzschild black hole ... the absence of any zero modes and hence new negative modes as one
     moves to larger radius solutions indicates we should expect no dynamical instabilities, at least with
     axisymmetry" (p. 4).
  G7 (deduced) So the statement's middle is carried: through the crossover the static corridor is one family,
     continuous from G0s's small end to the four-dimensional large end, with one member for each N, E(N) increasing
     and fixed by the first law, the surface gravity positive, and no zero mode -- G2's monotonicity here, Figueras and
     Wiseman's spectrum there -- so no other static branch bifurcates from it.  Uniqueness against a static corridor
     not continuously joined to the family is what G0s gives at the small end and the four-dimensional uniqueness
     theorem at the large; through the middle it is the absence of zero modes, not a global theorem.

Imports corridor_p2.py (the solver) by path for the live check.  numpy, scipy.
python3 gmid.py [--selftest | --mutants]     (the selftest's live solve takes about half a minute)
"""
import contextlib, importlib.util, io, json, math, os, sys
import numpy as np
from scipy.interpolate import PchipInterpolator

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
DATA = os.path.join(HERE, "data")
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((542, "add lemmas to close these gaps. nothing gets narrowed, only expanded to complete the statement"),)
BT_MIN = 0.12
G, C, HBAR = 6.67430e-11, 299792458.0, 1.054571817e-34
L_P = math.sqrt(HBAR * G / C ** 3)
ELL = 13.964e-6
_MOD = {}


def words():
    txt = open(RULINGS, encoding="utf-8").read()
    return all(w in txt for _, w in WORDS)


def members(N):
    d = json.load(open(os.path.join(DATA, "gmid_N%d.json" % N)))
    rows = sorted(((float(k), v) for k, v in d.items() if float(k) >= BT_MIN - 1e-12), key=lambda x: x[0])
    bt = np.array([r[0] for r in rows])
    R4 = np.array([r[1]["R4"] for r in rows])
    AH = np.array([r[1]["AH"] for r in rows])
    if MUT.get("fold") and N == 24:
        AH = AH.copy(); AH[5] = AH[6] * 1.01                     # the mutant: a fold, two members at one entropy
    res = np.array([r[1]["R"] for r in rows])
    xi2 = np.array([r[1]["xi2"] for r in rows])
    return dict(bt=bt, R4=R4, AH=AH, res=res, xi2=xi2)


def first_law(m):
    bt, AH = m["bt"], m["AH"]
    S = AH / 4
    if MUT.get("tfac"):
        T = lambda b: 1 / (2 * math.pi * b)                     # noqa: E731  the mutant: T = 1/(2 pi bt)
    else:
        T = lambda b: 1 / (4 * math.pi * b)                     # noqa: E731
    E0 = 3 * math.pi / 8 * (2 * S[0] / math.pi ** 2) ** (2 / 3)
    f = PchipInterpolator(np.log(bt), np.log(S))
    x = np.linspace(np.log(bt[0]), np.log(bt[-1]), 20001)
    Sx, Tx = np.exp(f(x)), T(np.exp(x))
    Ex = E0 + np.concatenate([[0.0], np.cumsum(0.5 * (Tx[1:] + Tx[:-1]) * np.diff(Sx))])
    E_at = PchipInterpolator(x, Ex)
    El = math.sqrt(S[-1] / (4 * math.pi))
    return dict(E0=E0, E_end=float(Ex[-1]), E_large=El, rel=float(Ex[-1] / El - 1), E_at=E_at, f=f)


def si(m, fl):
    """N and E at R4 = 10 (interpolated) and at the smallest member, against the end formulas"""
    lb = float(np.interp(math.log(10.0), np.log(m["R4"]), np.log(m["bt"])))
    AH10 = float(np.exp(PchipInterpolator(np.log(m["bt"]), np.log(m["AH"]))(lb)))
    E10 = float(fl["E_at"](lb))
    conv_N = ELL ** 2 / (4 * L_P ** 2 * math.log(2))
    conv_E = ELL * C ** 4 / G
    r0 = 10 * ELL
    N_l = math.pi * r0 ** 2 / (L_P ** 2 * math.log(2))
    E_l = C ** 4 * r0 / (2 * G)
    S0 = m["AH"][0] / 4
    return dict(N10=AH10 * conv_N, E10=E10 * conv_E, N_l=N_l, E_l=E_l,
                Nmin=m["AH"][0] * conv_N, Emin=fl["E0"] * conv_E, R4min=m["R4"][0], S0=S0)


def live():
    if "cp" not in _MOD:
        spec = importlib.util.spec_from_file_location("gmid_cp2", os.path.join(HERE, "corridor_p2.py"))
        mod = importlib.util.module_from_spec(spec)
        sys.modules["gmid_cp2"] = mod
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        _MOD["cp"] = mod
    cp = _MOD["cp"]
    S = cp.Solver(16)
    p = dict(bt=1.5, mu=0.0, lam=0.0)
    U, h = S.solve(S.guess(p), p, maxit=60)
    d = S.diag(U, p)
    return dict(R=h[-1], R4=d["R4"], AH=d["AH"], xi2=d["xi2"])


def compute():
    a, b = members(20), members(24)
    fa, fb = first_law(a), first_law(b)
    return dict(words=words(), a=a, b=b, fa=fa, fb=fb, si=si(b, fb), live=live())


def checks(o):
    a, b, fa, fb, s, lv = o["a"], o["b"], o["fa"], o["fb"], o["si"], o["live"]
    same = np.allclose(a["bt"], b["bt"])
    dR = np.abs(a["R4"] / b["R4"] - 1)
    dA = np.abs(a["AH"] / b["AH"] - 1)
    big = b["xi2"] > 1.5e-4
    g1 = (same and (a["res"] < 1e-7).all() and (b["res"] < 1e-7).all() and big.sum() <= 1 and b["xi2"].max() < 3e-3
          and dR.max() < 5e-3 and dA.max() < 1.2e-2 and np.median(dA) < 1e-3)
    mono = all((np.diff(m["R4"]) > 0).all() and (np.diff(m["AH"]) > 0).all() for m in (a, b))
    g2 = mono and (b["bt"] > 0).all()
    sm = [(1 - m["AH"][:4] / (2 * math.pi ** 2 * m["R4"][:4] ** 3)) / m["R4"][:4] for m in (a, b)]
    g3 = (all(abs(x - 0.60).max() < 0.006 for x in sm) and abs(sm[0] - sm[1]).max() < 1e-3
          and abs(b["AH"][-1] / (4 * math.pi * b["R4"][-1] ** 2) - 1) < 3e-3
          and abs(b["bt"][-1] / b["R4"][-1] - 1) < 1e-3)
    g4 = abs(fb["rel"]) < 1e-3 and abs(fa["rel"]) < 1e-3
    g5 = abs(s["N10"] / s["N_l"] - 1) < 1e-2 and abs(s["E10"] / s["E_l"] - 1) < 2e-2
    gl = abs(lv["AH"] / float(b["AH"][list(b["bt"]).index(1.5)]) - 1) < 5e-4 and lv["R"] < 1e-7
    return {"G0": o["words"], "G1": g1 and gl, "G2": g2, "G3": g3, "G4": g4, "G5": g5}


def report(o=None):
    o = o or compute(); ck = checks(o)
    a, b, fa, fb, s, lv = o["a"], o["b"], o["fa"], o["fb"], o["si"], o["live"]
    print("G0 M's words:", o["words"])
    print("G1 %d members, bt %.2f-%.0f, R4 %.3f-%.2f ell; residual <= %.1e; xi2 (N = 24) <= %.1e; N20/N24: R4 %.1e, "
          "area %.1e (median %.1e); live N = 16 at bt = 1.5: area %.6f against %.6f"
          % (len(b["bt"]), b["bt"][0], b["bt"][-1], b["R4"][0], b["R4"][-1], max(a["res"].max(), b["res"].max()),
             b["xi2"].max(), np.abs(a["R4"] / b["R4"] - 1).max(), np.abs(a["AH"] / b["AH"] - 1).max(),
             np.median(np.abs(a["AH"] / b["AH"] - 1)), lv["AH"], b["AH"][list(b["bt"]).index(1.5)]))
    print("G2 R4 and area strictly increasing in bt at both resolutions: %s" % ck["G2"])
    sm = (1 - b["AH"][:4] / (2 * math.pi ** 2 * b["R4"][:4] ** 3)) / b["R4"][:4]
    print("G3 small end (1 - A/(2 pi^2 R4^3))/R4 = %s; large end A/(4 pi R4^2) = %.4f, bt/R4 = %.4f"
          % (np.round(sm, 3), b["AH"][-1] / (4 * math.pi * b["R4"][-1] ** 2), b["bt"][-1] / b["R4"][-1]))
    print("G4 first law, small end to large: E %.5f against %.5f (N = 24, %.1e); N = 20: %.1e"
          % (fb["E_end"], fb["E_large"], fb["rel"], fa["rel"]))
    print("G5 at R4 = 10 ell: N %.3g, E %.3g J (large end at r0 = 10 ell: %.3g, %.3g J); at R4 = %.3f ell: N %.3g, "
          "E %.3g J" % (s["N10"], s["E10"], s["N_l"], s["E_l"], s["R4min"], s["Nmin"], s["Emin"]))
    for k, v in ck.items():
        print("%s %s" % (k, v))
    return ck


def selftest(quiet=False):
    with contextlib.redirect_stdout(io.StringIO()) if quiet else contextlib.nullcontext():
        ck = report()
    ok = all(ck.values())
    if not quiet:
        print("selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


MUTANTS = {"fold": "a fold in the family, two members at one entropy (G2)",
           "tfac": "the temperature read as 1/(2 pi bt), twice the solver's (G4)"}


def mutants():
    caught = 0
    for m, what in MUTANTS.items():
        MUT.clear(); MUT[m] = True
        try:
            ok = selftest(quiet=True)
        except Exception:
            ok = False
        caught += not ok
        print("mutant %-8s %s  (%s)" % (m, "caught" if not ok else "MISSED", what))
    MUT.clear()
    print("%d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
