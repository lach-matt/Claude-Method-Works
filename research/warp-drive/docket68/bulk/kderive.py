#!/usr/bin/env python3
"""kderive.py -- what the work says about k so far (M-RULINGS item 140: "the math in our work should give you pieces
to both derive and prove k. Our math is not dependent on k, k is dependent on our work").

First written as a derivation of a bound, k >= sqrt(pi/ln2)/l_P, and a value (ell = the one-bit throat).  The verifier
showed both fail (KDERIVE.md History); they are withdrawn.  What the work does say:

  K1  the one-bit throat, exactly: r_min(1) = 2 G E(1)/c^4 = l_P sqrt(ln2/pi) = 7.5918511091462209829e-36 m -- below the
      Planck length (0.4697 l_P).  The chain's E is coded as sqrt(hbar c^5 ln2/(4 pi G)) per sqrt(bit) (chain.py); this
      is the same expression, so K1 checks the transcription, not new physics (STRUCTURAL as a physics claim)
  K2  where the chain is classical: quantum-gravity corrections to a horizon of radius r go as (l_P/r)^2 (the board's
      estimate, standard order, not READ); at r = r_min(N) that is pi/(N ln2) -- small for any README of many bits,
      of order one at a few bits.  This holds whatever k is.
  K3  what the work fixes about the bulk: the RATIO of the two curvatures, from M's quarter (item 139: position 2's
      plane a quarter of ours, opposite sign): tau2/tau1 = (k_R - k_L)/k_L = -1/4 -> k_R = 3 k_L / 4 (multiplane.py M4).
      No dimensionful link between the corridor and the bulk has been found, so the SCALE of k is not fixed by the work
      yet.  Every result of the chain is free of k (KSCALE.md; censor.py; positivity.py).
  K4  why the withdrawn value cannot stand: at ell = r_min(1) the 5D Planck length l5 = (l_P^2 ell)^(1/3) exceeds ell
      (ell/l5 = 0.60), so a classical bulk is outside its domain there
Stdlib + sympy.  python3 kderive.py [--selftest]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)

H = sp.Rational(662607015, 10**42)
HBAR = H / (2 * sp.pi)
C = sp.Integer(299792458)
G = sp.Rational(66743, 10**15)


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def compute():
    ex = _load(os.path.join(D68, "copy", "exactE.py"), "kd_exactE")
    mp = _load(os.path.join(HERE, "multiplane.py"), "kd_multiplane")
    e1 = sp.Float(str(ex.e_per_sqrt_bit()), 25)
    lP = sp.sqrt(HBAR * G / C**3)
    r1 = lP * sp.sqrt(sp.log(2) / sp.pi)
    N = sp.Symbol("N", positive=True)
    qcorr = sp.simplify((lP / (r1 * sp.sqrt(N))) ** 2)              # (l_P / r_min(N))^2, r_min(N) = sqrt(N) r_min(1)
    m4 = mp.m4()
    ratio = sp.simplify(m4["kR"] / mp.kL)
    tension_ratio = sp.simplify(m4["tau2_over_rs"] / m4["tau1_over_rs"])
    ell = r1                                                         # the withdrawn value, for K4 only
    l5 = (lP**2 * ell) ** sp.Rational(1, 3)
    return {"r1_owner": 2 * G * e1 / C**4, "r1": r1, "lP": lP, "r1_over_lP": r1 / lP, "qcorr": qcorr,
            "kR_over_kL": ratio, "tension_ratio": tension_ratio, "ell_over_l5": sp.simplify(ell / l5)}


NSYM = sp.Symbol("N", positive=True)


def report(d):
    print("kderive.py -- what the work says about k so far (item 140)\n")
    print("K1 the one-bit throat: %s m (exactE), l_P sqrt(ln2/pi) = %s m = %s l_P"
          % (sp.N(d["r1_owner"], 20), sp.N(d["r1"], 20), sp.N(d["r1_over_lP"], 6)))
    print("K2 quantum corrections at r_min(N), (l_P/r)^2 = %s: %s at N = 1, %s at the example N = 2742570311524972"
          % (d["qcorr"], sp.N(d["qcorr"].subs(NSYM, 1), 4), sp.N(d["qcorr"].subs(NSYM, 2742570311524972), 4)))
    print("K3 the work fixes the ratio k_R/k_L = %s (position 2's tension / ours = %s); not the scale"
          % (d["kR_over_kL"], d["tension_ratio"]))
    print("K4 the withdrawn value ell = r_min(1): ell / l5 = %s < 1 -- a classical bulk is outside its domain"
          % sp.N(d["ell_over_l5"], 4))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("K1 (transcription): exactE's throat equals l_P sqrt(ln2/pi) to 1e-15",
        abs(d["r1_owner"] / sp.N(d["r1"], 30) - 1) < 1e-15)
    Gbad = G * (1 + sp.Rational(1, 10**9))
    chk("K1 control: with G one part in 1e9 high the closed form misses it",
        abs(d["r1_owner"] / sp.N(sp.sqrt(HBAR * Gbad / C**3) * sp.sqrt(sp.log(2) / sp.pi), 30) - 1) > 1e-12)
    chk("K1: the one-bit throat is below the Planck length (0.4697 l_P)", 0.469 < float(d["r1_over_lP"]) < 0.470)
    chk("K2: the quantum-correction estimate at r_min(N) is pi/(N ln2): of order one at N = 1, 1.65e-15 at the example",
        sp.simplify(d["qcorr"] - sp.pi / (NSYM * sp.log(2))) == 0 and
        1e-15 < float(d["qcorr"].subs(NSYM, 2742570311524972)) < 2e-15)
    chk("K3: M's quarter fixes k_R = 3 k_L / 4 (tension ratio -1/4)",
        d["kR_over_kL"] == sp.Rational(3, 4) and d["tension_ratio"] == sp.Rational(-1, 4))
    chk("K4: at the withdrawn value the bulk's curvature length is below the 5D Planck length",
        float(d["ell_over_l5"]) < 1)
    big = 100 * d["r1"]
    chk("K4 control: at a hundred times that length the curvature length is above the 5D Planck length",
        float(big / (d["lP"]**2 * big) ** sp.Rational(1, 3)) > 1)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
