#!/usr/bin/env python3
"""vii5census.py -- c4: an enumeration for (VII5), every place Parts III-IV name an averaged or equivariant choice.

Part VII's (VII5) and Lemma 3.1 (proof5/PART-VII-ASSEMBLY.md, section 3) say that the construction's choices -- cut-offs
(C1), the stationary gauge 1-forms (C2), the linear maps given by existence statements (C3) and their families in b
(C3'), and one complement (C4) -- are radial, averaged or equivariant, and that "the proofs of Parts III-IV use the
objects of (C3) and (C3') only through the conditions stated at the sites listed". That last step is a reading. This
program makes the reading finite: it lists, for each choice, every line of every Part III and Part IV file that names it
by its printed symbol, separating each symbol's own site (the line ranges Lemma 3.1 cites for it, or, where it cites a
section only, the sentence there that fixes it) from the places it is used.

  Symbols (READ from the proof5 files, spelled as printed):
     C1: the five cut-offs of PART-III-B-FAMILY.md:345-349, chi_r (:353), chi_infty (:165), chi_iota (III.K section 0,
         and III.G'' section 4 where it is defined), chi_- (III.K Definition 2.1, :215-217 -- section 2, not 0 or 3 as
         Lemma 3.1 prints), chi_9 (III.K section 3), Theta (III.I'''' :37-38), and the cut-offs inside t^flat_* (II.C
         Lemma 3.2: the smooth minimum's m_kappa and the smooth maximum tilde R(r), tilde R'), which are printed only in
         PART-II-C-OPERATORS.md; that one Part II file is searched as their site.
     C2: c_Upsilon, c_{Upsilon,H}, c_C at III.B Definition 6.1 and the specific forms Lemma 3.1 cites.
     C3: omega_s1, breve omega; the domain Y_tau and the maps' printed names in III.G'' Table 1.1 and Definition 2.5
         (breve h, h^{(mu), h_{b,s1}, h^{(0)}_{b,s0}, h^{(-2)}_{b,tau} and its h^{(-2)}_b, h^{<=k}_{b,s1},
         h^{<=k}_{b,v1}); S_{lambda_0}. Since D621 also the other spellings of the 1-form towers that (C3) names since
         D608 (an independent reader's m2): the bottoms omega^{(0)}_{b0,s1}, omega^{(-1)}_{b0,v1}, omega^{(0)}_{b0,s0}
         (site PART-III-I10-CORR4.md:127-147, the site (C3) cites), and four objects built from the towers, each at
         the sentence that defines it: omega^{<=k}_tau (I10:148-149), omega_nu (I10 Definition 2.1, :174-176),
         omega^{<=4} (PART-III-I9-COMMOTION.md:76-77) and omega^{<=1}_natural (PART-III-I5-UNBOOST.md Definition 1.1,
         :77-78).
     C3': T_{rho,b}, h^{<=1}_{b,s1}, h_{b,v1}, h^{<=2}_{b,v1}. Beside them, h_{b,rem} is reported as the object built
         from (C3') (III.I'''''''''''''' Definition 1.2), not a choice. Since D626 (a second reader's N2) C3 adds the s2
         bottom omega^{(-1)}_{b_0}, and C3' every spelling of the 1-form towers and states at b: omega^{(0)}_{b,s0},
         omega^{(0)}_{b,s1}, omega^{(-1)}_{b,v1} (III.D'' (3.1)), its proof's omega_{b,s0}, omega_{b,s1}, omega_{b,v1},
         III.D''' Proposition 3.1's omega^{<=k} (bare: it also lies inside omega^{<=k}_tau and omega^{<=k}_b),
         omega^{<=k+1}, omega^{(0),<=, omega^{(-1),<=k}_{b,v1}, omega^{(mu)}_b, omega^{(mu),<=k}_b, its proof's
         omega_{s0}, omega_{v1}, Table 1.1's omega^{(mu-1)}_b, and I16's omega^{<=1}_{b,natural}; each at its defining
         display.
     C4: the complement V'.
  V1 (computed, a census) Every occurrence of each symbol in the 46 Part III and 7 Part IV files (and the Part II site
     file) is classified per symbol: at that symbol's site, or a use. Since D626 a symbol printed across a line break
     (its lines joined with one space) is found too, at the line it starts on. --list prints every site line and every
     use line. The reader's task for (VII5) is the list printed under 'used at': at each such line, that only the condition
     stated at the site is used.
  V2 (computed, D626) Completeness of the 1-form spellings: every distinct printed spelling of omega in Parts III-IV
     (with its accent and every sub- and superscript) either contains a C3/C3'/C4 symbol or is excluded by a rule with
     its reason (OMEGA_EXCLUDE: Minkowski models, dual states, the zero-energy gauge potential, generic forms and
     components). Control: a planted spelling must be reported as neither.
  Control (per symbol): every symbol must have at least one hit inside its own site ranges, else the run FAILs (a
     misspelt symbol or a wrong site is caught, not silently listed as absent). Negative controls: a planted symbol,
     and chi_9 with its site moved to PART-III-B-FAMILY.md:345-349, must each be reported as missing its site.

Reach: a literal census sees only the printed symbols; an object used under another name, or implicitly, is not found,
and a homonym printed with the same spelling (e.g. another Theta) is listed as a use.
Labels: computed (text census); symbols and site ranges READ; that each use needs no more than the stated condition is
not computed.

Run: python3 checks/vii5census.py [--list]   (a second; the saved .out is the --list run)
"""
import bisect
import glob
import os
import re
import sys
import textwrap

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P5 = os.path.join(HERE, "proof5")

BF, K, G3, I5, I15 = ("PART-III-B-FAMILY.md", "PART-III-K-NONLINEAR.md", "PART-III-G3-GRAFT.md",
                      "PART-III-I5-UNBOOST.md", "PART-III-I15-AUGMENT5.md")
I10 = "PART-III-I10-CORR4.md"
D3, D4, I16 = "PART-III-D3-SYMSTATES.md", "PART-III-D4-GENSTATES.md", "PART-III-I16-BASEPOINTS.md"
IIC = "PART-II-C-OPERATORS.md"
CUT5 = [(BF, 345, 349)]
TABLE = [(G3, 40, 80), (G3, 179, 182)]
FAM = [(I15, 67, 72), (I15, 118, 122)]
GROUPS = [
    ("C1 cut-offs (radial)", [
        ("\\chi^\\flat_K", CUT5), ("\\chi_K", CUT5), ("\\chi^\\sharp_K", CUT5), ("\\chi_{\\mathrm{IVP}}", CUT5),
        ("\\chi^\\sharp_{\\mathrm{IVP}}", CUT5), ("\\chi_r", [(BF, 353, 353)]), ("\\chi_\\infty", [(BF, 165, 165)]),
        ("\\chi_\\iota", [(K, 62, 66), (G3, 263, 264)]), ("\\chi_-", [(K, 215, 217)]), ("\\chi_9", [(K, 338, 339)]),
        ("\\Theta", [(I5, 37, 38)]), ("m_\\kappa", [(IIC, 433, 434)]), ("\\tilde R(r)", [(IIC, 444, 446)]),
        ("\\tilde R'", [(IIC, 445, 449)])]),
    ("C2 gauge 1-forms (stationary)", [
        ("c_\\Upsilon", [(BF, 430, 433), ("PART-III-D3-SYMSTATES.md", 30, 32)]),
        ("c_{\\Upsilon,H}", [(BF, 430, 433), ("PART-III-D3-SYMSTATES.md", 30, 32)]),
        ("c_C", [(BF, 430, 433), ("PART-III-E-CONSTRAINT.md", 19, 21), ("PART-IV5-CDMODES.md", 34, 38)])]),
    ("C3 linear maps (averaged)", [
        ("\\omega_{\\mathrm s1}", [(I5, 62, 66)]), ("\\breve\\omega", [(I5, 62, 66)]), ("\\mathcal Y_\\tau", TABLE),
        ("\\breve h", TABLE), ("h^{(\\mu)", TABLE), ("h_{b,\\mathrm s1}", TABLE), ("h^{(0)}_{b,\\mathrm s0}", TABLE),
        ("h^{(-2)}_", TABLE), ("h^{\\le k}_{b,\\mathrm s1}", TABLE), ("h^{\\le k}_{b,\\mathrm v1}", TABLE),
        ("\\mathcal S_{\\lambda_0}", [("PART-III-J-PARAM.md", 225, 227)]),
        ("\\omega^{(0)}_{b_0,\\mathrm s1}", [(I10, 127, 147)]), ("\\omega^{(-1)}_{b_0,\\mathrm v1}", [(I10, 127, 147)]),
        ("\\omega^{(0)}_{b_0,\\mathrm s0}", [(I10, 127, 147)]), ("\\omega^{\\le k}_\\tau", [(I10, 148, 149)]),
        ("\\omega_\\nu", [(I10, 174, 176)]), ("\\omega^{\\le4}", [("PART-III-I9-COMMOTION.md", 76, 77)]),
        ("\\omega^{\\le1}_\\natural", [(I5, 77, 78)]), ("\\omega^{(-1)}_{b_0}", [(I10, 127, 147)])]),
    ("C3' families in b (averaged)", [
        ("T_{\\rho,b}", FAM), ("h^{\\le1}_{b,\\mathrm s1}", FAM), ("h_{b,\\mathrm v1}", FAM),
        ("h^{\\le2}_{b,\\mathrm v1}", FAM),
        # D626: the 1-form towers and states at b, whose b0 values (C3) averages (a second reader's N2), each at its
        # defining display: III.D'' Proposition 3.1 (3.1) and proof, III.D''' Proposition 3.1 and proof, I16 (P3)
        ("\\omega^{(0)}_{b,\\mathrm s0}", [(D3, 138, 139)]), ("\\omega^{(0)}_{b,\\mathrm s1}", [(D3, 138, 139)]),
        ("\\omega^{(-1)}_{b,\\mathrm v1}", [(D3, 138, 139)]), ("\\omega_{b,\\mathrm s0}", [(D3, 189, 189)]),
        ("\\omega_{b,\\mathrm s1}", [(D3, 199, 199)]), ("\\omega_{b,\\mathrm v1}", [(D3, 269, 269)]),
        ("\\omega^{\\le k}", [(D4, 110, 111)]), ("\\omega^{\\le k+1}", [(D4, 207, 207)]),
        ("\\omega^{(0),\\le", [(D4, 119, 119)]), ("\\omega^{(-1),\\le k}_{b,\\mathrm v1}", [(D4, 148, 148)]),
        ("\\omega^{(\\mu)}_b", [(D4, 162, 164)]), ("\\omega^{(\\mu),\\le k}_b", [(D4, 166, 166)]),
        ("\\omega^{(\\mu-1)}_b", TABLE), ("\\omega_{\\mathrm s0}", [(D4, 184, 184)]),
        ("\\omega_{\\mathrm v1}", [(D4, 223, 223)]), ("\\omega^{\\le1}_{b,\\natural}", [(I16, 385, 385)])]),
    ("C3' built object (not a choice: built from the C3' families)", [("h_{b,\\mathrm{rem}}", [(I15, 67, 72)])]),
    ("C4 the complement", [("\\mathcal V'", [("PART-III-I10-CORR4.md", 89, 94)])]),
]
# V2 (D626): every printed spelling of omega in Parts III-IV is either covered by a C3/C3'/C4 symbol (it contains one)
# or excluded here, by a rule with its reason; a spelling that is neither fails V2.
OMEGA_EXCLUDE = [
    (r"\\(?:bar\s*|breve\{\\bar)\\omega", "a Minkowski model 1-form (bar or breve-bar), explicit: "
                                         "PART-III-D3-SYMSTATES.md (1.2), PART-III-D4-GENSTATES.md section 3 (its "
                                         "models, genstates5.py H1-H3), III.B section 5"),
    (r"\\omega\^\{?\*", "a dual state, the kernel of an adjoint operator (PART-III-D2, -E, -E2, -F4, -F5): used in the "
                       "zero-energy counts of those files only, in no file of the construction (the III.G-III.K "
                       "files)"),
    (r"\\dot\\omega", "the zero-energy gauge potential, the unique solution of a natural problem "
                      "(PART-III-F4-ZERO.md (2.1); Part VII Lemma 3.1's proof)"),
    (r"\\omega_\{\(0\)\}", "the source's zero-energy state, in PART-III-D2-ZEROENERGY.md's remarks on the source"),
    (r"\\omega\^\\sharp", "a musical dual, or the explicit V_b + c_0|x|^-3 V(W) of PART-III-E2-V1STATES.md:129-130"),
    (r"\\(?:tilde\\)?omega(?:_\\pi)?$", "a generic 1-form (or a coordinate on S^3), or its type-pi part"),
    (r"\\omega(?:_[0-2]|_[abcdirt]|_\{[a-z];[a-z]?\}|_\\mu|_\\lambda|_V|\^[iaT]|\^\\beta|\^\\gamma|\^\{\([01]\)\})$",
     "components of a generic 1-form or covector, a multi-index, or the Cauchy data of another equation (IV5, IV7)"),
]
OMEGA_TOKEN = re.compile(r"(\\(?:breve|bar|tilde|hat|dot|check)(?:\s*\{\\bar\\omega\}|\s*\\omega)|\\omega)(?![A-Za-z])")


def _braced(t, i):
    d = 0
    for j in range(i, len(t)):
        if t[j] == "{":
            d += 1
        elif t[j] == "}":
            d -= 1
            if d == 0:
                return j + 1
    return len(t)


def wrap(text):
    print(textwrap.fill(text, 119, subsequent_indent="        ", break_long_words=False, break_on_hyphens=False),
          flush=True)


def omega_spellings(fs):
    """{spelling: number of occurrences} over the joined text of fs: omega with its prefix accent and every sub- and
    superscript that follows"""
    out = {}
    for path in fs:
        txt, _ = joined(path)
        for m in OMEGA_TOKEN.finditer(txt):
            j, tok = m.end(), m.group(0)
            while j < len(txt) and txt[j] in "^_":
                k = j + 1
                if k < len(txt) and txt[k] == " ":
                    k += 1
                if k < len(txt) and txt[k] == "{":
                    e = _braced(txt, k)
                elif k < len(txt) and txt[k] == "\\":
                    mm = re.match(r"\\[A-Za-z]+", txt[k:])
                    e = k + (len(mm.group(0)) if mm else 1)
                else:
                    e = k + 1
                tok += txt[j:e]
                j = e
            out[tok] = out.get(tok, 0) + 1
    return out


def v2(extra=(), show=True):
    fs = [f for f in files() if not f.endswith(IIC)]
    syms = [sym for name, es in GROUPS if name.startswith(("C3", "C4")) for sym, _ in es]
    sp = omega_spellings(fs)
    for t in extra:
        sp[t] = sp.get(t, 0) + 1
    covered = {t for t in sp if any(sym in t for sym in syms)}
    why = {}
    for t in sp:
        if t not in covered:
            r = [reason for pat, reason in OMEGA_EXCLUDE if re.match(pat, t)]
            why[t] = r[0] if r else None
    left = sorted(t for t, r in why.items() if r is None)
    if show:
        wrap("  V2: %d distinct spellings of omega in Parts III-IV (%d occurrences): %d contain a C3/C3'/C4 symbol, "
             "%d excluded by a rule with its reason, %d neither%s" % (len(sp), sum(sp.values()), len(covered),
                                                                      len(why) - len(left), len(left),
                                                                      (": " + " ".join(left)) if left else ""))
        by = {}
        for t, r in why.items():
            if r:
                by.setdefault(r, []).append(t)
        for r, ts in sorted(by.items()):
            wrap("      excluded (%d spellings, %d occurrences): %s" % (len(ts), sum(sp[t] for t in ts), r))
    return not left


PLANT = ("\\mathfrak{Z}_{\\mathrm{planted}}", [(BF, 1, 10 ** 6)])
MOVED = ("\\chi_9", CUT5)
MOVED_IN = ("\\chi_9", [(K, 1, 10)])                                # same file, other lines


def files():
    out = sorted(glob.glob(os.path.join(P5, "PART-III*.md")) + glob.glob(os.path.join(P5, "PART-IV*.md")))
    out = [f for f in out if os.path.basename(f).startswith(("PART-III-", "PART-IV"))]
    return out + [os.path.join(P5, IIC)]


def at_site(sym_sites, f, i):
    return any(f == sf and lo <= i <= hi for sf, lo, hi in sym_sites)


def joined(path):
    """the file as one string, each line stripped and followed by one space, with the offset of each line's start: a
    symbol printed across a line break (as omega^{(0)}_{b_0,mathrm / s1}) is found, at the line it starts on (D626)"""
    txt, starts = [], []
    n = 0
    for line in open(path, encoding="utf-8").read().split("\n"):
        starts.append(n)
        t = line.strip() + " "
        txt.append(t)
        n += len(t)
    return "".join(txt), starts


def census(entries, fs):
    """{(file, line): {symbol: is_site}} for every line on which a symbol of entries is printed or starts."""
    hits = {}
    for path in fs:
        f = os.path.basename(path)
        txt, starts = joined(path)
        for s, sites in entries:
            k = txt.find(s)
            while k >= 0:
                i = bisect.bisect_right(starts, k)
                hits.setdefault((f, i), {})[s] = at_site(sites, f, i)
                k = txt.find(s, k + 1)
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
    moved_in = missing_site([MOVED_IN], fs) == [MOVED_IN[0]]
    print("  control: planted symbol reported missing its site: %s; chi_9 with its site moved to %s:345-349 reported "
          "missing: %s; moved within its own file (%s:1-10): %s" % (planted, BF, moved, K, moved_in), flush=True)
    return planted and moved and moved_in


def main():
    listing = "--list" in sys.argv
    good1 = v1(listing)
    good2 = v2()
    planted2 = not v2(extra=("\\omega^{(7)}_{b,\\mathrm s9}",), show=False)
    wrap("  V2 control: a planted spelling omega^{(7)}_{b,s9} is reported as neither: %s" % planted2)
    ctl = control() and planted2
    print("V1 %s; V2 %s; control (a planted and a moved site, and a planted spelling, reported): %s"
          % ("PASS" if good1 else "FAIL", "PASS" if good2 else "FAIL", "behaves" if ctl else "MISBEHAVES"), flush=True)
    return 0 if good1 and good2 and ctl else 1


if __name__ == "__main__":
    sys.exit(main())
