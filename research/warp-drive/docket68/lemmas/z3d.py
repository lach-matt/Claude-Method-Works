#!/usr/bin/env python3
"""z3d.py -- item 542, lemma Z3d: Z3c against the measured dark energy.  M, 542, to the weak rows: "strengthen the
existing lemmas, and ad more for support".  Z3c derives w >= -1 at every epoch from (Z); nature_rows Z3 recorded the
tension with the banked fit, w(a -> 0) = -1.76, and stopped.  This file says what (Z) does with DESI DR2.  Labels:
computed (exact unless marked numerical), READ, deduced, M's.

  D0 (read) M's words, verbatim in the rulings file, 542.
  D1 (computed, exact) What (Z) forbids on the plane's cosmology.  With H^2 = (8 pi G/3) rho + C'/a^4 (the brane's
     rho^2/(2 sigma) term negligible since the first second) and total conservation on the plane, dH/dt = -4 pi G
     (rho + p) - 2 C'/a^4.  (Z) keeps null energy at every point for every component (320), and Z1 holds C' >= 0, so
     dH/dt <= 0 at every epoch: (Z) forbids super-acceleration of the whole, and each component's true w >= -1.
  D2 (READ) DESI DR2 (Abdul Karim et al., 2503.14738v3, Table V, READ): w0waCDM, (Omega_m, H0, w0, wa) = DESI+CMB
     (0.353, 63.6, -0.42, -1.75); +Pantheon+ (0.3114, 67.51, -0.838, -0.62); +Union3 (0.3275, 65.91, -0.667, -1.09);
     +DESY5 (0.3191, 66.74, -0.752, -0.86); "the significance of rejection of LambdaCDM is 2.8 sigma, 3.8 sigma and 4.2
     sigma for combinations with the Pantheon+, Union3 and DESY5 SNe samples, respectively, and 3.1 sigma for
     DESI+CMB" (Fig. 11); "the favored w(z) shows a phase of w > -1 at low redshifts and a phantom crossing to w < -1
     above redshifts z ~ 0.4" (p. 25); and "the equation of state is not directly observable, and we only observe
     quantities, such as distances, that depend indirectly on w(z)" (p. 25).
  D3 (computed, numerical) The fits keep the whole's null energy at every epoch.  For each fit, rho + p of everything
     (matter, radiation, the fitted dark energy) over rho is positive for every z from 0 to 1e5, its least value 0.42
     to 0.56 (at z = 0 to 0.38); so dH/dt < 0 throughout, as (Z) requires.  The fitted dark energy crosses w = -1 at
     z = 0.35-0.50, and where w < -1 its density is small: (1 + w) rho_DE never outweighs the cold dark matter, rho_c +
     (1 + w) rho_DE > 0 at every z, its least ratio to rho_c 0.90 to 0.95.
  D4 (computed, exact) A decomposition every component of which keeps null energy, reproducing each fit's H(z), and so
     every distance, exactly: vacuum energy (w = -1 exactly) exchanging energy with cold dark matter, rho_vac = -w
     rho_DE and rho_c' = rho_c + (1 + w) rho_DE, the exchange Q = -d rho_vac/dt.  Total conservation holds identically,
     rho_vac > 0 (w < 0 throughout every fit), rho_c' > 0 (D3), the vacuum's rho + p = 0: no component's null energy
     fails at any z.  Das, Corasaniti and Khoury (astro-ph/0510628v2, abstract, READ): "an interaction between dark
     matter and dark energy generically results in an effective dark energy equation of state of w < -1 ... An
     observer who fits the data treating the dark matter as non-interacting will infer an effective dark energy fluid
     with w < -1"; "the combined dark matter plus dark energy fluid satisfies w > -1" (p. 1).  Control: a phantom fluid
     with the whole's rho + p < 0 (dH/dt > 0) admits no such decomposition.
  D5 (deduced) So Z3c stands, strengthened: (Z) bounds the true w of every component and the whole's dH/dt, not the
     effective w that a fit holding the dark matter uncoupled infers; DESI DR2's preferred backgrounds keep the whole's
     null energy at every epoch, rho + p >= 0.42 rho, and are reproduced exactly by components that each keep it.
     The falsifier is stated: (Z) fails if dH/dt > 0 at any epoch, or if the cold dark matter needed beside an
     exchanging vacuum would be negative (rho_c + (1 + w) rho_DE < 0) -- neither holds for any DR2 fit.  The
     background is reproduced, not the perturbations: the growth and the CMB lensing of the exchanging pair are not
     computed here.

python3 z3d.py [--selftest | --mutants]
"""
import contextlib, io, math, os, sys
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((542, "strengthen the existing lemmas, and ad more for support"),)
FITS = {"DESI+CMB": (0.353, 63.6, -0.42, -1.75), "+Pantheon+": (0.3114, 67.51, -0.838, -0.62),
        "+Union3": (0.3275, 65.91, -0.667, -1.09), "+DESY5": (0.3191, 66.74, -0.752, -0.86)}   # DESI DR2 Table V
OMEGA_R_H2 = 4.18e-5                            # photons and three neutrinos, relativistic (standard, not READ)
OMEGA_B_H2 = 0.0224                             # baryons (standard, not READ); the margins barely depend on it


def words():
    txt = open(RULINGS, encoding="utf-8").read()
    return all(w in txt for _, w in WORDS)


def raychaudhuri():
    """D1: dH/dt from H^2 = (8 pi G/3) rho + C/a^4 and rho' = -3 H (rho + p)"""
    t, G, C = sp.symbols("t G C", positive=True)
    a = sp.Function("a")(t)
    rho, p = sp.Function("rho")(t), sp.Function("p")(t)
    H = sp.sqrt(8 * sp.pi * G / 3 * rho + C / a ** 4)
    Hd = sp.diff(H, t)
    Hsym = sp.symbols("H", positive=True)
    Hd = Hd.subs(sp.Derivative(rho, t), -3 * Hsym * (rho + p)).subs(sp.Derivative(a, t), Hsym * a)
    Hd = sp.simplify(Hd.subs(Hsym, H))
    sign = -1 if MUT.get("csign") else 1
    want = -4 * sp.pi * G * (rho + p) - sign * 2 * C / a ** 4
    return sp.simplify(Hd - want) == 0


def densities(fit, z):
    om, h0, w0, wa = fit
    h = h0 / 100
    orad = OMEGA_R_H2 / h ** 2
    ob = OMEGA_B_H2 / h ** 2
    ode = 1 - om - orad
    a = 1 / (1 + z)
    w = w0 + wa * (1 - a)
    if MUT.get("phantom"):
        w = w - 1.2                                              # the control: a phantom that outweighs matter
    rde = ode * a ** (-3 * (1 + w0 + wa)) * np.exp(-3 * wa * (1 - a))
    if MUT.get("phantom"):
        rde = ode * a ** (-3 * (1 + w0 + wa - 1.2)) * np.exp(-3 * wa * (1 - a))
    rm, rr = om * a ** -3, orad * a ** -4
    rc = (om - ob) * a ** -3
    return dict(w=w, rde=rde, rm=rm, rr=rr, rc=rc)


def margins(fit):
    z = np.concatenate([np.linspace(0, 5, 5001), np.logspace(np.log10(5.001), 5, 3000)])
    d = densities(fit, z)
    rho = d["rm"] + d["rr"] + d["rde"]
    rpp = d["rm"] + 4 / 3 * d["rr"] + (1 + d["w"]) * d["rde"]
    dark = d["rc"] + (1 + d["w"]) * d["rde"]
    om, h0, w0, wa = fit
    zc = (1 / (1 + (1 + w0) / wa) - 1) if wa != 0 else float("inf")
    return dict(whole=float((rpp / rho).min()), zmin=float(z[np.argmin(rpp / rho)]),
                dark=float((dark / d["rc"]).min()), wneg=bool((d["w"] < 0).all()), zc=zc, wmin=float(d["w"].min()))


def decomposition():
    """D4: rho_vac = -w rho_DE and rho_c' = rho_c + (1 + w) rho_DE reproduce the fit's total and conserve it"""
    t = sp.symbols("t")
    Hf, rde, rc, w = (sp.Function(n)(t) for n in ("H", "rde", "rc", "w"))
    cons = {sp.Derivative(rde, t): -3 * Hf * (1 + w) * rde, sp.Derivative(rc, t): -3 * Hf * rc}
    rvac = -w * rde
    rcp = rc + (1 + w) * rde
    if MUT.get("split"):
        rcp = rc + w * rde                                       # the mutant: the vacuum's share counted twice
    same = sp.simplify(rvac + rcp - (rc + rde)) == 0
    Q = -sp.diff(rvac, t)                                         # energy into the cold dark matter
    lhs = sp.diff(rcp, t) + 3 * Hf * rcp - Q
    ok = sp.simplify(lhs.subs(cons)) == 0
    return same and ok


def compute():
    return dict(words=words(), ray=raychaudhuri(), m={k: margins(v) for k, v in FITS.items()}, dec=decomposition())


def checks(o):
    m = o["m"]
    d3 = all(r["whole"] > 0.4 and r["dark"] > 0.85 and 0.3 < r["zc"] < 0.55 for r in m.values())
    d4 = o["dec"] and all(r["wneg"] for r in m.values())
    return {"D0": o["words"], "D1": o["ray"], "D3": d3, "D4": d4}


def report(o=None):
    o = o or compute(); ck = checks(o)
    print("D0 M's words:", o["words"])
    print("D1 dH/dt = -4 pi G (rho + p) - 2 C'/a^4: %s" % o["ray"])
    for k, r in o["m"].items():
        print("D3 %-11s least (rho + p)/rho %.3f (z = %.2f); w = -1 at z = %.2f; least w %.2f; "
              "least (rho_c + (1 + w) rho_DE)/rho_c %.3f" % (k, r["whole"], r["zmin"], r["zc"], r["wmin"], r["dark"]))
    print("D4 exchanging vacuum + cold dark matter reproduce the total and conserve it: %s" % o["dec"])
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


MUTANTS = {"csign": "the dark radiation's sign in dH/dt flipped (D1)",
           "phantom": "the control: a phantom fluid whose rho + p outweighs matter (D3)",
           "split": "the vacuum's share counted twice in the decomposition (D4)"}


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
