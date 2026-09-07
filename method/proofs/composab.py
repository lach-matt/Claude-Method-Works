#!/usr/bin/env python3
"""composab.py — §12.11's composability table against the Mathematical Compendium's own series.
R3 completion item A8, on M's "complete R3 please".

THE TWO STATEMENTS. The main volume prints a table at §12.11 and concludes: "Λ9 is the only stage of
the tower that composes ... composability is lost at axis 10 ... Λ9 sits alone at the top of the
stricter grading", with the table's reason for Λ10 being "no — no source seniority exists". The
Mathematical Compendium prints, of the same tower: "composability peaks at Λ10 and falls after:
0.0000, 0.7068, 0.8087, 0.6956, 0.6592, 0.6381 across Λ8 to Λ13."

BOTH CANNOT DESCRIBE THE SAME PREDICATE. One says Λ10 does not compose at all; the other measures it
at its PEAK. Register 314's general claim -- "an axis can be exact and not composable; none is
composable and not exact" -- is not touched by this; what is touched is the supporting evidence, and
that is exactly what the chat-witnessed correction said: Λ10 was never structurally barred and Λ9 is
not alone.

WHAT IS MEASURED. A cell composes when its TARGET tuple is some cell's SOURCE tuple, at the same
stage -- the corpus's own definition ("the composable cells only, those whose target is a legal
source"). The source/target coordinate pairings are not assumed: they are the ones that REPRODUCE the
compendium's printed fractions, and four of the six do so exactly.

  Λ8   src (n,l,k,2S)      tgt (e,f,g)          shapes differ, 4 against 3   -> 0.0000  printed 0.0000
  Λ9   src (n,l,k,2S)      tgt (e,f,g,2S')                                   -> 0.7068  printed 0.7068
  Λ10  src (n,l,k,2S)      tgt (e,f,g,2S')      THE SAME SHAPES AS Λ9        -> 0.8087  printed 0.8087
  Λ12  src (n,l,k,2S,2Jc)  tgt (e,f,g,2S',2K)                                -> 0.6592  printed 0.6592

Λ11 and Λ13 are NOT reproduced by any pairing this search tried, and that is reported rather than
smoothed: an exhaustive sweep of every same-size source/target index pair over the plausible
coordinate pools finds none matching 0.6956 or 0.6381.

stdlib only; imports the seated tower by path and never copies it.  --selftest asserts the four.
"""
import argparse, importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.join(os.path.dirname(HERE), "members")
NAMES = "n l k q e f g 2S 2S' v 2Jc 2K 2J".split()
PRINTED = {8: 0.0000, 9: 0.7068, 10: 0.8087, 11: 0.6956, 12: 0.6592, 13: 0.6381}
PAIRING = {8: ((0, 1, 2, 7), (4, 5, 6)),
           9: ((0, 1, 2, 7), (4, 5, 6, 8)),
           10: ((0, 1, 2, 7), (4, 5, 6, 8)),
           12: ((0, 1, 2, 7, 10), (4, 5, 6, 8, 11))}


def tower():
    spec = importlib.util.spec_from_file_location("t2", os.path.join(MEM, "tower-2.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def fraction(cells, src, tgt):
    if len(src) != len(tgt):
        return 0.0, 0
    S = {tuple(c[j] for j in src) for c in cells}
    n = sum(1 for c in cells if tuple(c[j] for j in tgt) in S)
    return n / len(cells), n


def measure():
    t2 = tower()
    out = {}
    for d, (s, t) in sorted(PAIRING.items()):
        cells = t2.STAGES[d]()
        f, n = fraction(cells, s, t)
        out[d] = dict(cells=len(cells), comp=n, frac=f, src=s, tgt=t)
    return out


def report():
    M = measure()
    print("§12.11's composability, measured on the seated tower\n")
    print(f"  {'stage':>6} {'cells':>8} {'composable':>11} {'fraction':>9} {'printed':>9}  source -> target")
    for d in sorted(M):
        r = M[d]
        s = ",".join(NAMES[i] for i in r["src"]); t = ",".join(NAMES[i] for i in r["tgt"])
        mark = "OK" if abs(r["frac"] - PRINTED[d]) < 5e-5 else "DIFFERS"
        print(f"  Λ{d:<5} {r['cells']:8} {r['comp']:11} {r['frac']:9.4f} {PRINTED[d]:9.4f}  "
              f"({s}) -> ({t})  {mark}")
    print("\n  Λ11 and Λ13 are not reproduced by any pairing an exhaustive same-size sweep over the")
    print("  plausible coordinate pools tried. Reported, not smoothed.")

    print("\nWHAT THIS DECIDES ABOUT §12.11's TABLE")
    print("  The table gives Λ10 as 'no — no source seniority exists' and the prose concludes")
    print("  'Λ9 is the only stage of the tower that composes' and 'Λ9 sits alone'.")
    print(f"  MEASURED: Λ10 composes at {M[10]['frac']:.4f} — {M[10]['comp']} of {M[10]['cells']} cells —")
    print("  USING THE SAME SOURCE AND TARGET SHAPES THAT MAKE Λ9 WORK, and that is its PEAK.")
    print("  Λ12 composes at 0.6592 on the shapes one axis wider. So the compendium's series and the")
    print("  main volume's table are two different predicates wearing one word.")
    print("\n  REGISTER 314's CLAIM IS UNTOUCHED: 'an axis can be exact and not composable; none is")
    print("  composable and not exact' does not depend on which stages compose. What falls is the")
    print("  supporting evidence — 'Λ10 was never structurally barred' and 'Λ9 is not alone' — and")
    print("  that is the correction the retraction audit recorded. The claim survives; the evidence")
    print("  does not. Nothing is repaired here.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print(f"  OK   {name}: {got}")
        else: fail += 1; print(f"  FAIL {name}: got {got}, want {want}")
    M = measure()
    for d in sorted(PAIRING):
        eq(f"Λ{d} fraction reproduces the compendium", round(M[d]["frac"], 4), PRINTED[d])
    eq("Λ8 composes with nothing", M[8]["comp"], 0)
    eq("Λ9 composable cells", M[9]["comp"], 1169)
    eq("Λ10 composable cells", M[10]["comp"], 2050)
    eq("Λ12 composable cells", M[12]["comp"], 46740)
    eq("Λ10 uses Λ9's own source shape", M[10]["src"], M[9]["src"])
    eq("Λ10 uses Λ9's own target shape", M[10]["tgt"], M[9]["tgt"])
    eq("Λ10 is the peak of the four measured", max(M, key=lambda d: M[d]["frac"]), 10)
    eq("so Λ9 does not sit alone", sum(1 for d in M if M[d]["frac"] > 0) > 1, True)
    print(f"\nOK: {ok}  FAIL: {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
