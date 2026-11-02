#!/usr/bin/env python3
"""support9.py -- computations behind two of the paper's section-9 statements (verifier 259's items 3 and 6, D605).

  S3 (computed, a text census) The constants without a number (supplement EFFECTIVE-CONSTANTS.md section 3): the count
     over proof5's PART files of contradiction, compactness, Rellich, compact inclusion or embedding, Fredholm and
     subsequence (case-insensitive), as D338 counted them over 75 files, recomputed on the files now present; and the
     ledger EFFECTIVE-LEDGER.tsv's rows per class (N1-N4, F, G, X) counted from the file. Which rows give no number is
     a reading (the classes); the counts are computed, and they reproduce D338's and the section's table exactly (the
     76th file, added since, contains none of the words). Control: a word absent from every file counts 0.
  S6 (exact) The paper's (4.1), R[G(., . + c)](X, th) = R[G](X, th + c): the two-scale operator has no explicit phase.
     lead5.py's reduced_ricci (Ric^H of g0 + lam W in the wave-map gauge relative to g0, d_v -> d_v + lam^-1 d_s) on its
     stage-0 profile W (W_TT and chi dv^2, chi = B cos 2s + C sin s with B, C generic functions of (v, r, theta), the
     phase explicit) with the phase shifted, s -> s + c, equals its value at the
     unshifted profile with s replaced by s + c, in every component at orders lam^-1 and lam^0 (c symbolic). Control:
     shifting the waves but not chi (not a phase shift of the profile) breaks the identity.

Labels: S3 computed (text census); S6 computed (exact, sympy).

Run: python3 checks/support9.py   (a few minutes)
"""
import csv
import glob
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)

TERMS = [("contradiction", r"contradiction"), ("compactness", r"compactness"), ("Rellich", r"rellich"),
         ("compact inclusion or embedding", r"compact (?:inclusion|embedding)"), ("Fredholm", r"fredholm"),
         ("subsequence", r"subsequence")]
D338 = {"contradiction": 19, "compactness": 44, "Rellich": 5, "compact inclusion or embedding": 5, "Fredholm": 74,
        "subsequence": 28}


def s3(control=False):
    fs = sorted(glob.glob(os.path.join(HERE, "proof5", "PART-*.md")))
    text = {f: open(f, encoding="utf-8").read().lower() for f in fs}
    if control:
        return sum(len(re.findall("zzqxw", t)) for t in text.values()) != 0
    counts = {name: sum(len(re.findall(pat, t)) for t in text.values()) for name, pat in TERMS}
    nfiles = sum(any(re.search(pat, t) for _, pat in TERMS) for t in text.values())
    led = os.path.join(HERE, "EFFECTIVE-LEDGER.tsv")
    classes = {}
    if os.path.exists(led):
        with open(led, encoding="utf-8") as fh:
            rows = list(csv.reader(fh, delimiter="\t"))
        head = [h.strip().lower() for h in rows[0]]
        col = head.index("class") if "class" in head else None
        for row in rows[1:]:
            if col is not None and len(row) > col:
                classes[row[col].strip()] = classes.get(row[col].strip(), 0) + 1
    print("  S3: %d PART files (D338 counted 75); counts now %s, in %d files; D338's %s; the ledger's rows per class: %s"
          % (len(fs), counts, nfiles, D338, dict(sorted(classes.items())) or "no ledger found"), flush=True)
    table = {"N1": 6, "N2": 15, "N3": 1, "N4": 13, "F": 41, "G": 37, "X": 52}     # the section's table
    return counts == D338 and nfiles == 35 and classes == table


def s6(control=False):
    import lead5 as L
    c = sp.Symbol("c", real=True)
    Bf = sp.Function("B")(L.v, L.r, L.th)
    Cf = sp.Function("C")(L.v, L.r, L.th)
    chi_x = Bf*sp.cos(2*L.s) + Cf*sp.sin(L.s)                          # chi with its phase explicit (B, C generic)
    W = L.wave(with_chi=True).applyfunc(lambda e: e.subs(L.chi, chi_x).doit())
    shift = {L.s: L.s + c}
    Ws = W.applyfunc(lambda e: e.subs(shift))
    if control:                                                        # the waves shifted, chi not
        Ws = L.wave(with_chi=True).applyfunc(lambda e: e.subs(shift).subs(L.chi.subs(shift), chi_x).doit())
    R0 = L.reduced_ricci(W)
    R1 = L.reduced_ricci(Ws)
    ok = True
    for key in R0:
        for k in range(2):
            d = sp.simplify(sp.expand(R1[key][k] - sp.sympify(R0[key][k]).subs(shift)))
            ok &= d == 0
    if control:
        return ok
    print("  S6: Ric^H of g0 + lam W at the profile shifted by c equals the unshifted value at s + c, all %d"
          " components, orders lam^-1 and lam^0: %s" % (len(R0), ok), flush=True)
    return ok


CHECKS = [("S3", s3), ("S6", s6)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
