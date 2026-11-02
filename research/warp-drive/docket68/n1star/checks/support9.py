#!/usr/bin/env python3
"""support9.py -- computations behind two of the paper's section-9 statements (verifier 259's items 3 and 6, D605).

  S3 (computed, a text census) The constants without a number (supplement EFFECTIVE-CONSTANTS.md section 3): the count
     over proof5's PART files of contradiction, compactness, Rellich, compact inclusion or embedding, Fredholm and
     subsequence (case-insensitive), as D338 counted them over 75 files, recomputed on the files now present; and the
     ledger EFFECTIVE-LEDGER.tsv's rows per class (N1-N4, F, G, X) counted from the file. Which rows give no number is
     a reading (the classes); the counts are computed, and they reproduce D338's and the section's table exactly (the
     76th file, added since, contains none of the words). Control: a word absent from every file counts 0.
  S6 (exact) The paper's (4.1), R[G(., . + c)](X, th) = R[G](X, th + c): the two-scale operator has no explicit phase.
     The structural fact, checked for every W rather than one profile: lead5.py's reduced_ricci (Ric^H of g0 + lam W in
     the wave-map gauge relative to g0, d_v -> d_v + lam^-1 d_s; its background has no s) is applied to W whose 15
     components are generic functions w_ab(s, v, r, theta), and R[W(s + c)] = R[W](s + c) holds in every component at
     orders lam^-1 and lam^0 (c symbolic; compared as R[W(s + c)](s - c) = R[W](s)). The program prints how many of the
     30 parts are nonzero, i.e. tested nontrivially: the 15 lam^0 parts; the 15 lam^-1 parts vanish identically for
     generic W (g0^vv = 0), so they test nothing. Control: every component shifted but W_vv (the slot of chi dv^2: the
     waves shifted, chi not; not a phase shift of the profile) breaks the identity.

Labels: S3 computed (text census); S6 computed (exact, sympy).

Run: python3 checks/support9.py   (about five minutes)
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

    def generic(shifted):
        W = sp.zeros(5)
        for a in range(5):
            for b in range(a, 5):
                arg = L.s + c if (a, b) in shifted else L.s
                W[a, b] = W[b, a] = sp.Function("w%d%d" % (a, b))(arg, L.v, L.r, L.th)
        return W
    pairs = [(a, b) for a in range(5) for b in range(a, 5)]
    R0 = L.reduced_ricci(generic([]))
    R1 = L.reduced_ricci(generic([p for p in pairs if control is False or p != (0, 0)]))
    ok, nonzero, bad = True, [0, 0], []
    for key in R0:
        for k in range(2):
            e0 = sp.sympify(R0[key][k])
            nonzero[k] += e0 != 0
            d = sp.expand(sp.sympify(R1[key][k]).subs(L.s, L.s - c).doit() - e0)
            if d != 0:
                ok = False
                bad.append((key, k - 1))
    print("  S6%s: Ric^H of g0 + lam W, W generic in (s, v, r, th), at W(s + c) equals R[W](s + c) in all %d components"
          ", orders lam^-1 and lam^0: %s; parts nonzero (tested nontrivially): lam^-1 %d of %d, lam^0 %d of %d%s"
          % (" control (W_vv not shifted)" if control else "", len(R0), ok, nonzero[0], len(R0), nonzero[1], len(R0),
             "; identity fails at (component, order) %s" % bad if bad else ""), flush=True)
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
