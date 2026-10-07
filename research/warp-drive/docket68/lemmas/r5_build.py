#!/usr/bin/env python3
"""r5_build.py -- Warp Theorem lemma R5: the build's mechanism -- which field, what "activation" is, and that the energy
suffices for any exact README.

  R5a THE MECHANISM IS YOURS.  Position 2 itself builds (91 (b), H-POSITION-BUILDS); a closed index takes the README,
      verifies it and incorporates it to remain closed (101 answer 8, H-AUTODETECT); the README itself is the trigger
      (139 (3)); matter rearranges to accommodate it (148); the coupling is the mechanism that defines material
      properties (136 B, 114 (b)).  AXIOM
  R5b WHICH FIELD, AND "ACTIVATION" (the board's reading, item 149).  On the board's reading (i) of item 148, adopted under
      item 149, position 2's electron mass equals ours.  With light the same (143) and the relative laws acting only on
      the nucleus and the electron's mass (144), the elementary masses the Higgs field gives are the ones the README's
      values carry, already, and the Higgs field's value, non-zero and the same everywhere, does not change.  So item
      136 answer 2's "activates the Higgs field forming the mass defined in the README" is read as: the README's arrival
      triggers (139 (3)) the arrangement whose masses the Higgs field already sets.  The rearrangement acts through the
      electromagnetic field (atoms and molecules), and through the strong and weak forces wherever the stock's nuclei
      differ from the README's
  R5c THE ENERGY SUFFICES FOR ANY EXACT README (computed).  An exact README (146, labels and values, 147) gives every
      atom at least one bit, so N >= the atom count, 6.7117e27 for a 70 kg body (LOOSE.md L1).  Then
      E >= 459,404,002 J x sqrt(6.7117e27) = 3.76e22 J -- above the chemistry ceiling, 1.1947e10 J, and above the worst
      nuclear case: unbinding and rebinding every nucleon at 8.8 MeV (the binding peak, standard, not READ),
      4.216e28 x 8.8 MeV = 5.94e16 J.  So whatever the stock, E covers its rearrangement.  Control: the example
      README's 2.41e16 J (an identity core, not an exact README) does NOT cover the worst nuclear case
Imports copy/exactE.py by path.  python3 r5_build.py [--selftest]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
EXAMPLE_N = 2742570311524972
ATOMS_70KG = 6.7117e27                 # LOOSE.md L1
CHEM_MAX_J = 1.1947e10                 # LOOSE.md L1
NUCLEONS_70KG = 70 / 1.66053906660e-27
MEV = 1.602176634e-13
BIND_PEAK_MEV = 8.8


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
    ex = _load(os.path.join(D68, "copy", "exactE.py"), "r5_exactE")
    k = ex.e_per_sqrt_bit()
    E_exact_min = k * math.sqrt(ATOMS_70KG)
    nuclear_worst = NUCLEONS_70KG * BIND_PEAK_MEV * MEV
    return {"E_exact_min": E_exact_min, "chem": CHEM_MAX_J, "nuclear_worst": nuclear_worst,
            "E_example": k * math.sqrt(EXAMPLE_N), "N_cover_nuclear": (nuclear_worst / k) ** 2}


def report(d):
    print("r5_build.py -- Warp Theorem lemma R5\n")
    print("R5a the mechanism: yours (91 (b), 101 answer 8, 136 B, 139 (3), 148)")
    print("R5b the board's reading: the Higgs field's value unchanged; EM rearranges atoms and molecules, strong and weak "
          "forces any differing nuclei")
    print("R5c exact README: E >= %.3e J; chemistry <= %.4e J; worst nuclear %.3e J; E covers both from N = %.3e bits; "
          "control, the example core: %.3e J" % (d["E_exact_min"], d["chem"], d["nuclear_worst"], d["N_cover_nuclear"],
                                                d["E_example"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("R5c: an exact README's E (>= 3.76e22 J) covers chemistry and the worst nuclear rearrangement (5.94e16 J)",
        d["E_exact_min"] > d["nuclear_worst"] > d["chem"] and abs(d["E_exact_min"] / 3.7637e22 - 1) < 1e-3)
    chk("R5c control: the example core's E does not cover the worst nuclear case", d["E_example"] < d["nuclear_worst"])
    chk("R5c: the threshold N for the worst case (~1.7e16 bits) is far below any exact README's atom count",
        d["N_cover_nuclear"] < ATOMS_70KG)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
