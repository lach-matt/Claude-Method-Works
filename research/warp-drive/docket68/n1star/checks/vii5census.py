#!/usr/bin/env python3
"""vii5census.py -- c4: an enumeration for (VII5), every place Parts III-IV name an averaged or equivariant choice.

Part VII's (VII5) and Lemma 3.1 (proof5/PART-VII-ASSEMBLY.md) say that the construction's choices -- cut-offs (C1), the
stationary gauge 1-forms (C2), the linear maps given by existence statements (C3) and their families in b (C3'), and one
complement (C4) -- are radial, averaged or equivariant, and that "the proofs of Parts III-IV use the objects of (C3) and
(C3') only through the conditions stated at the sites listed". That last step is a reading. This program makes the
reading finite: it lists, for each choice, every line of every Part III and Part IV file that names it by its printed
symbol, separating the site where it is chosen from the places it is used.

  V1 (computed, a census) For each group the literal symbols are searched in the 46 Part III and 7 Part IV files; every
     occurrence is printed as file:line, the site's own lines marked. The reader's task for (VII5) is the list printed
     under 'used at': at each such line, that only the condition stated at the site is used.
  Control: each group's site must be found by the census (a census that misses the defining line would be silently
     incomplete); a planted symbol that occurs nowhere is reported as absent.

Reach: a literal census sees only the printed symbols; an object used under another name, or implicitly, is not found.
Labels: computed (text census); the check that each use needs no more than the stated condition is not computed.

Run: python3 checks/vii5census.py [--list]   (a second)
"""
import glob
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P5 = os.path.join(HERE, "proof5")

GROUPS = [
    ("C1 cut-offs (radial)", ["\\chi^\\flat_K", "\\chi^\\sharp_K", "\\chi_{\\mathrm{IVP}}", "\\chi^\\sharp_{\\mathrm{IVP}}",
                             "\\chi_\\iota", "\\chi_9"], ["PART-III-B-FAMILY.md"]),
    ("C2 gauge 1-forms (stationary)", ["c_\\Upsilon", "c_{\\Upsilon,H}", "c_C"], ["PART-III-B-FAMILY.md",
                                                                                  "PART-III-E-CONSTRAINT.md"]),
    ("C3 linear maps (averaged)", ["\\omega_{\\mathrm s1}", "\\breve\\omega", "\\mathcal Y_\\tau",
                                   "\\mathcal S_{\\lambda_0}"], ["PART-III-D3-SYMSTATES.md", "PART-III-D4-GENSTATES.md",
                                                                  "PART-III-I5-UNBOOST.md", "PART-III-G3-GRAFT.md",
                                                                  "PART-III-G4-RESONANT.md"]),
    ("C3' families in b (averaged)", ["T_{\\rho,b}", "h^{\\le1}_{b,\\mathrm s1}", "h_{b,\\mathrm v1}",
                                      "h^{\\le2}_{b,\\mathrm v1}", "h_{b,\\mathrm{rem}}"], ["PART-III-I15-AUGMENT5.md"]),
    ("C4 the complement", ["\\mathcal V'"], ["PART-III-I10-CORR4.md"]),
]
PLANT = "\\mathfrak{Z}_{\\mathrm{planted}}"


def files():
    out = sorted(glob.glob(os.path.join(P5, "PART-III*.md")) + glob.glob(os.path.join(P5, "PART-IV*.md")))
    return [f for f in out if os.path.basename(f).startswith(("PART-III-", "PART-IV"))]


def census(symbols, fs):
    hits = {}
    for f in fs:
        for i, line in enumerate(open(f, encoding="utf-8"), 1):
            for s in symbols:
                if s in line:
                    hits.setdefault((os.path.basename(f), i), set()).add(s)
    return hits


def v1(listing=False, control=False):
    fs = files()
    if control:
        return not census([PLANT], fs)
    ok = True
    nIII = sum(os.path.basename(f).startswith("PART-III-") for f in fs)
    nIV = len(fs) - nIII
    print("  V1: %d Part III and %d Part IV files searched" % (nIII, nIV), flush=True)
    for name, syms, sites in GROUPS:
        hits = census(syms, fs)
        at_site = sorted(k for k in hits if k[0] in sites)
        used = sorted(k for k in hits if k[0] not in sites)
        per_file = {}
        for f, _ in used:
            per_file[f] = per_file.get(f, 0) + 1
        found = {s for v in hits.values() for s in v}
        ok &= bool(at_site)
        print("    %s: %d lines at the site files, %d lines elsewhere in %d files; symbols never printed: %s"
              % (name, len(at_site), len(used), len(per_file), sorted(set(syms) - found) or "none"), flush=True)
        if listing:
            for f, i in used:
                print("      used at %s:%d  %s" % (f, i, " ".join(sorted(hits[(f, i)]))), flush=True)
        else:
            print("      used in: %s" % ", ".join("%s (%d)" % kv for kv in sorted(per_file.items())), flush=True)
    return ok


def main():
    listing = "--list" in sys.argv
    good = v1(listing)
    ctl = v1(control=True)
    print("V1 %s; control (every site found by the census; a planted symbol absent): %s"
          % ("PASS" if good else "FAIL", "behaves" if ctl else "MISBEHAVES"), flush=True)
    return 0 if good and ctl else 1


if __name__ == "__main__":
    sys.exit(main())
