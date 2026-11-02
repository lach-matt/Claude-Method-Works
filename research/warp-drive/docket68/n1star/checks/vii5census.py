#!/usr/bin/env python3
"""vii5census.py -- c4: an enumeration for (VII5), every place Parts III-IV name an averaged or equivariant choice.

Part VII's (VII5) and Lemma 3.1 (proof5/PART-VII-ASSEMBLY.md:280-313) say that the construction's choices -- cut-offs
(C1), the stationary gauge 1-forms (C2), the linear maps given by existence statements (C3) and their families in b
(C3'), and one complement (C4) -- are radial, averaged or equivariant, and that "the proofs of Parts III-IV use the
objects of (C3) and (C3') only through the conditions stated at the sites listed". That last step is a reading. This
program makes the reading finite: it lists, for each choice, every line of every Part III and Part IV file that names it
by its printed symbol, separating each symbol's own site (the line ranges Lemma 3.1 cites for it, or, where it cites a
section only, the sentence there that fixes it) from the places it is used.

  Symbols (READ from the proof5 files, spelled as printed):
     C1: the five cut-offs of PART-III-B-FAMILY.md:345-349, chi_r (:353), chi_infty (:165), chi_iota (III.K section 0,
         and III.G'' section 4 where it is defined), chi_- (III.K Definition 2.1, :213-215 -- section 2, not 0 or 3 as
         Lemma 3.1 prints), chi_9 (III.K section 3), Theta (III.I'''' :37-38), and the cut-offs inside t^flat_* (II.C
         Lemma 3.2: the smooth minimum's m_kappa and the smooth maximum tilde R(r), tilde R'), which are printed only in
         PART-II-C-OPERATORS.md; that one Part II file is searched as their site.
     C2: c_Upsilon, c_{Upsilon,H}, c_C at III.B Definition 6.1 and the specific forms Lemma 3.1 cites.
     C3: omega_s1, breve omega; the domain Y_tau and the maps' printed names in III.G'' Table 1.1 and Definition 2.5
         (breve h, h^{(mu), h_{b,s1}, h^{(0)}_{b,s0}); S_{lambda_0}.
     C3': T_{rho,b}, h^{<=1}_{b,s1}, h_{b,v1}, h^{<=2}_{b,v1}. Beside them, h_{b,rem} is reported as the object built
         from (C3') (III.I'''''''''''''' Definition 1.2), not a choice.
     C4: the complement V'.
  V1 (computed, a census) Every occurrence of each symbol in the 46 Part III and 7 Part IV files (and the Part II site
     file) is classified per symbol: at that symbol's site, or a use. --list prints every site line and every use line.
     The reader's task for (VII5) is the list printed under 'used at': at each such line, that only the condition
     stated at the site is used.
  Control (per symbol): every symbol must have at least one hit inside its own site ranges, else the run FAILs (a
     misspelt symbol or a wrong site is caught, not silently listed as absent). Negative controls: a planted symbol,
     and chi_9 with its site moved to PART-III-B-FAMILY.md:345-349, must each be reported as missing its site.

Reach: a literal census sees only the printed symbols; an object used under another name, or implicitly, is not found,
and a homonym printed with the same spelling (e.g. another Theta) is listed as a use.
Labels: computed (text census); symbols and site ranges READ; that each use needs no more than the stated condition is
not computed.

Run: python3 checks/vii5census.py [--list]   (a second; the saved .out is the --list run)
"""
import glob
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P5 = os.path.join(HERE, "proof5")

BF, K, G3, I5, I15 = ("PART-III-B-FAMILY.md", "PART-III-K-NONLINEAR.md", "PART-III-G3-GRAFT.md",
                      "PART-III-I5-UNBOOST.md", "PART-III-I15-AUGMENT5.md")
IIC = "PART-II-C-OPERATORS.md"
CUT5 = [(BF, 345, 349)]
TABLE = [(G3, 40, 80), (G3, 179, 182)]
FAM = [(I15, 67, 72), (I15, 118, 122)]
GROUPS = [
    ("C1 cut-offs (radial)", [
        ("\\chi^\\flat_K", CUT5), ("\\chi_K", CUT5), ("\\chi^\\sharp_K", CUT5), ("\\chi_{\\mathrm{IVP}}", CUT5),
        ("\\chi^\\sharp_{\\mathrm{IVP}}", CUT5), ("\\chi_r", [(BF, 353, 353)]), ("\\chi_\\infty", [(BF, 165, 165)]),
        ("\\chi_\\iota", [(K, 62, 66), (G3, 263, 264)]), ("\\chi_-", [(K, 213, 215)]), ("\\chi_9", [(K, 336, 337)]),
        ("\\Theta", [(I5, 37, 38)]), ("m_\\kappa", [(IIC, 433, 434)]), ("\\tilde R(r)", [(IIC, 444, 446)]),
        ("\\tilde R'", [(IIC, 445, 449)])]),
    ("C2 gauge 1-forms (stationary)", [
        ("c_\\Upsilon", [(BF, 430, 433), ("PART-III-D3-SYMSTATES.md", 30, 32)]),
        ("c_{\\Upsilon,H}", [(BF, 430, 433), ("PART-III-D3-SYMSTATES.md", 30, 32)]),
        ("c_C", [(BF, 430, 433), ("PART-III-E-CONSTRAINT.md", 19, 21), ("PART-IV5-CDMODES.md", 34, 38)])]),
    ("C3 linear maps (averaged)", [
        ("\\omega_{\\mathrm s1}", [(I5, 62, 66)]), ("\\breve\\omega", [(I5, 62, 66)]), ("\\mathcal Y_\\tau", TABLE),
        ("\\breve h", TABLE), ("h^{(\\mu)", TABLE), ("h_{b,\\mathrm s1}", TABLE), ("h^{(0)}_{b,\\mathrm s0}", TABLE),
        ("\\mathcal S_{\\lambda_0}", [("PART-III-J-PARAM.md", 225, 227)])]),
    ("C3' families in b (averaged)", [
        ("T_{\\rho,b}", FAM), ("h^{\\le1}_{b,\\mathrm s1}", FAM), ("h_{b,\\mathrm v1}", FAM),
        ("h^{\\le2}_{b,\\mathrm v1}", FAM)]),
    ("C3' built object (not a choice: built from the C3' families)", [("h_{b,\\mathrm{rem}}", [(I15, 67, 72)])]),
    ("C4 the complement", [("\\mathcal V'", [("PART-III-I10-CORR4.md", 89, 94)])]),
]
PLANT = ("\\mathfrak{Z}_{\\mathrm{planted}}", [(BF, 1, 10 ** 6)])
MOVED = ("\\chi_9", CUT5)


def files():
    out = sorted(glob.glob(os.path.join(P5, "PART-III*.md")) + glob.glob(os.path.join(P5, "PART-IV*.md")))
    out = [f for f in out if os.path.basename(f).startswith(("PART-III-", "PART-IV"))]
    return out + [os.path.join(P5, IIC)]


def at_site(sym_sites, f, i):
    return any(f == sf and lo <= i <= hi for sf, lo, hi in sym_sites)


def census(entries, fs):
    """{(file, line): {symbol: is_site}} for every line naming a symbol of entries."""
    hits = {}
    for path in fs:
        f = os.path.basename(path)
        for i, line in enumerate(open(path, encoding="utf-8"), 1):
            for s, sites in entries:
                if s in line:
                    hits.setdefault((f, i), {})[s] = at_site(sites, f, i)
    return hits


def missing_site(entries, fs):
    hits = census(entries, fs)
    found = {s for v in hits.values() for s, site in v.items() if site}
    return [s for s, _ in entries if s not in found]


def v1(listing=False):
    fs = files()
    ok = True
    nIII = sum(os.path.basename(f).startswith("PART-III-") for f in fs)
    print("  V1: %d Part III, %d Part IV and 1 Part II (site) files searched" % (nIII, len(fs) - nIII - 1), flush=True)
    for name, entries in GROUPS:
        hits = census(entries, fs)
        miss = missing_site(entries, fs)
        ok &= not miss
        print("    %s: site found for %d of %d symbols%s" % (name, len(entries) - len(miss), len(entries),
              "; SITE MISSING: %s" % " ".join(miss) if miss else ""), flush=True)
        for s, _ in entries:
            sl = sorted(k for k, v in hits.items() if v.get(s) is True)
            ul = sorted(k for k, v in hits.items() if v.get(s) is False)
            print("      %-28s site lines %3d; used on %3d lines in %2d files"
                  % (s, len(sl), len(ul), len({f for f, _ in ul})), flush=True)
        if listing:
            for (f, i), v in sorted(hits.items()):
                site = sorted(s for s, t in v.items() if t)
                used = sorted(s for s, t in v.items() if not t)
                if site:
                    print("      site    %s:%d  %s" % (f, i, " ".join(site)), flush=True)
                if used:
                    print("      used at %s:%d  %s" % (f, i, " ".join(used)), flush=True)
    return ok


def control():
    fs = files()
    planted = missing_site([PLANT], fs) == [PLANT[0]]
    moved = missing_site([MOVED], fs) == [MOVED[0]]
    print("  control: planted symbol reported missing its site: %s; chi_9 with its site moved to %s:345-349 reported "
          "missing: %s" % (planted, BF, moved), flush=True)
    return planted and moved


def main():
    listing = "--list" in sys.argv
    good = v1(listing)
    ctl = control()
    print("V1 %s; control (every symbol found at its own site; a planted and a moved site reported missing): %s"
          % ("PASS" if good else "FAIL", "behaves" if ctl else "MISBEHAVES"), flush=True)
    return 0 if good and ctl else 1


if __name__ == "__main__":
    sys.exit(main())
