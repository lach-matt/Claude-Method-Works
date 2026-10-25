#!/usr/bin/env python3
"""bundlesweep.py -- a second, mechanical census of [Hin26c] section 9 for RB (N1STAR-PROOF.md section 10.85; D183).

10.84 places, from a reading of the full text, every step of [Hin26c] section 9 at which a proof uses that the operator
is scalar. This sweep takes another route. It splits section 9 (printed pp. 157-200, from its heading to that of
section 10) into its numbered items, their proofs and its subsection prose; finds in each span every marker of
scalarity or of bundles -- real and imaginary parts and subprincipal symbols, thresholds and spectra, square roots and
sums of squares, Garding and positivity, signs, defect measures, scalar spaces, energy estimates and complex
absorption, bundle words; and holds the spans with a marker against ACCOUNT, the record's placement of each: a site of
10.84 (a)-(f) or of 10.86, or the reason it has none, read from the hits' contexts.  The full text is alphaXiv's
(get_paper_content, fullText = true, 2026-10-24), the file censusweep.py reads, whose page splitter this imports; it is
not stored here, so pass its directory with --texts.  Labels: computed (a token search); the accounting READ.

  W1 the text: section 9 runs over printed pp. 157-200, 44 pages, and each of its 43 numbered items is headed once.
     Control: 42 items claimed.
  W2 every span with a marker is in ACCOUNT, and every span in ACCOUNT has a marker: 341 hits in 38 of section 9's
     62 items, proofs and subsections.
     Control: ACCOUNT without Theorem 9.28.
  W3 10.84 READ (1)'s bundle notation: E_X occurs only on p. 163 (Theorem 9.5), "fiber inner" only on p. 182.
     Control: E_X claimed on p. 164.
  W4 10.84 READ (4)'s perturbation words: within section 9, "perturb" occurs only on p. 184 (footnote 82, of Im z);
     the p. 157 sentence on Theorem 8.14 precedes the section's heading.  Control: p. 157 claimed.

python3 bundlesweep.py --texts DIR [--out hits.tsv] [--selftest | --mutants]
"""
import collections
import csv
import re
import sys

import censusweep as cw
from damping5 import Checklist

PATS = [("subp", r"\bIm (c P|P|˜ P|\(|σ∂|∂)|\bRe (c P|P|˜ P|∂|Q\b)|P ?− ?P ?∗|\bp 1\b|subprincipal"),
        ("thr", r"\bspec\b|fiber inner|¯ S|\bRe S\b|\bβ 1\b|ϑ (in|H)|\bγ [+−] |threshold"),
        ("root", r"square root|√|sum of squares|[\x01\x11] 1 2\b"),
        ("gard", r"G˚arding|Garding|Gårding|\bpositiv"),
        ("sign", r"\bsign\b|non-positive|nonpositive|good sign|correct sign|same sign"),
        ("meas", r"defect measure|Radon measure"),
        ("scal", r"\bscalar\b|C ∞ \(X\)|C ∞ \(∂X\)|C ∞ \(M\)|\bT \[u\]|∆ X|complex absorption"
                 r"|energy (estimate|identity)"),
        ("bund", r"\bE X\b|bundle|tensor")]

# The record's placement of each span with a marker: 10.84's sites, 10.85's, or why it has none (each READ from the
# hits' contexts).
ACCOUNT = {
    "9.4": "READ (1): S in C^oo(X) and the scalar sentence",
    "s9.1.2": "(a): (9.8)'s Re and Im of P_h,z, self-adjoint parts on E_X; the signs are of Im z, a number",
    "s9.1.3": "none: the b-cotangent bundle of the phase space, not E_X",
    "s9.1.4": "none: the sign of sigma, a number",
    "s9.2": "(b): (9.16a)-(9.16c), section 5's thresholds",
    "9.5": "(b), (f): section 5's thresholds; (9.21) on E_X; the energy estimate near r = m (D182)",
    "9.7": "none: literature",
    "s9.2.1": "none: rho_oo positive, a scalar weight; the normal bundle of H",
    "9.9": "(a)-(c): (9.27)-(9.29)",
    "9.10": "(a)-(c): (9.32), (9.34)-(9.38b)",
    "9.11": "(a)-(d): (9.42), (9.47), (9.49)-(9.52)",
    "s9.3": "none: 'High-energy estimates', the heading",
    "9.16": "(b): S-bar from (5.2); 'High-energy estimates', titles; the rest inherited",
    "9.18": "none: literature",
    "s9.3.1": "(a), (f), 10.86 (f): real principal type with complex absorption, Q Id; rho_oo a scalar weight",
    "9.19": "10.86 (f): real principal type for G Id",
    "9.20": "none: the dual metric function and rho_oo, scalar symbols",
    "9.21": "(a): (9.65), Q_0 a self-adjoint endomorphism",
    "9.22": "(a), (c): (9.66b), (9.68)-(9.69)",
    "9.23": "(a), (c): (9.66b), (9.68)-(9.69)",
    "9.25": "(a)-(c): (9.72)",
    "9.26": "(b), (c): vartheta_in, (9.75)",
    "9.27": "(a)-(d): (9.51)-(9.52) by analogy, g_00",
    "s9.3.4": "(a), (b): (9.79)-(9.81); the fiber inner product, READ (1)",
    "9.28": "(a)-(c), (e), (f); at Gamma (b)'s conjugation by (5.9)'s Q (D182)",
    "9.30": "(c), (e)",
    "9.31": "(e)",
    "9.32": "(a), (e)",
    "9.33": "(b), (f)",
    "s9.3.5": "(f)",
    "9.35": "(f)",
    "s9.4": "(b): s_0 > 1/2 + vartheta_H+",
    "9.36": "(a)-(c), (f): Proposition 9.9 at sigma = 0; the energy estimate near r = m (D182); chi a cut-off",
    "s9.5": "(b): the threshold conditions of (9.15)",
    "9.38": "(b), (f): S-bar, S*",
    "9.40": "READ (1): the tensor case reduced to the scalar one",
    "s9.6": "none: 'Uniform low-energy estimates', the heading",
    "9.41": "(b), (f): (9.16c); scalar cut-offs",
}


def section9():
    P = cw.pages("hin26c")
    text, pos = "", []
    for p in range(157, 201):
        s = P[p]
        if p == 157:
            s = s[s.find("9. General-purpose"):]
        if p == 200:
            s = s[:re.search(r"\b10\. [A-Z]", s).start()]
        pos.append((len(text), p))
        text += s + " "
    return text, pos


def spans(text):
    starts = []
    for m in re.finditer(r"\b(Theorem|Proposition|Lemma|Corollary|Remark|Definition|Notation) (9\.\d+) \(", text):
        i, d = m.end(), 1                                  # a heading: a balanced title closed by ")."
        while i < len(text) and d and i - m.end() < 140:
            d += {"(": 1, ")": -1}.get(text[i], 0)
            i += 1
        if d == 0 and text[i:i + 1] == ".":
            starts.append((m.start(), m.group(2), "stmt"))
    for m in re.finditer(r"Proof of (Theorem|Proposition|Lemma|Corollary) (9\.\d+)", text):
        starts.append((m.start(), m.group(2), "proof"))
    for m in re.finditer(r"(?<![\d.(§])(9\.\d(?:\.\d)?)\. (?=[A-Z])", text):
        pre = text[max(0, m.start() - 14):m.start()]
        if re.search(r"(§|Theorem|Proposition|Figure|Lemma|Remark|Corollary|of) ?$", pre):
            continue                                       # a reference, not a subsection heading
        starts.append((m.start(), "s" + m.group(1), "prose"))
    starts.sort()
    return [(a, (starts[k + 1][0] if k + 1 < len(starts) else len(text)), key, kind)
            for k, (a, key, kind) in enumerate(starts)]


def sweep():
    text, pos = section9()

    def page(i):
        return max(p for a, p in pos if a <= i)
    sp_ = spans(text)
    rows, hits = [], collections.defaultdict(collections.Counter)
    for a, b, key, kind in sp_:
        for name, pat in PATS:
            for m in re.finditer(pat, text[a:b]):
                hits[key][name] += 1
                rows.append((key, kind, page(a + m.start()), name, text[a + m.start() - 60:a + m.end() + 40]))
    return text, pos, sp_, hits, rows, page


def w1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    text, pos, sp_, *_ = sweep()
    pages = [p for _, p in pos]
    chk(f"section 9 on printed pp. {pages[0]}-{pages[-1]}, {len(pages)} pages", pages == list(range(157, 201)))
    heads = collections.Counter(key for _, _, key, kind in sp_ if kind == "stmt")
    want = 42 if control else 43
    chk(f"{len(heads)} numbered items, each headed once", len(heads) == want and set(heads.values()) == {1}
        and set(heads) == {f"9.{k}" for k in range(1, 44)})
    return chk.ok


def w2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    _, _, sp_, hits, rows, _ = sweep()
    acc = {k: v for k, v in ACCOUNT.items() if not (control and k == "9.28")}
    marked = {k for k, c in hits.items() if sum(c.values())}
    keys = {key for _, _, key, _ in sp_}
    chk(f"{len(rows)} hits in {len(marked)} of {len(keys)} spans; every marked span placed", marked <= set(acc))
    chk("every placement names a marked span", set(acc) <= marked)
    return chk.ok


def w3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    text, pos, *_ , page = sweep()
    ex = {page(m.start()) for m in re.finditer(r"\bE X\b", text)}
    fi = {page(m.start()) for m in re.finditer(r"fiber inner", text)}
    chk(f"E_X on pp. {sorted(ex)}, 'fiber inner' on pp. {sorted(fi)}", ex == ({164} if control else {163})
        and fi == {182})
    return chk.ok


def w4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    text, pos, *_, page = sweep()
    pp = {page(m.start()) for m in re.finditer(r"perturb", text)}
    chk(f"'perturb' within section 9 on pp. {sorted(pp)}", pp == ({157} if control else {184}))
    return chk.ok


CHECKS = [("W1 section 9 on pp. 157-200, its 43 numbered items each headed once", w1),
          ("W2 every span with a scalarity or bundle marker placed by 10.84 or 10.86, and no placement idle", w2),
          ("W3 E_X only on p. 163, 'fiber inner' only on p. 182", w3),
          ("W4 'perturb' within section 9 only on p. 184 (footnote 82)", w4)]


def run(verbose=False):
    ok = True
    for name, fn in CHECKS:
        res = fn(0, verbose)
        ok &= res
        print(f"{name[:104]:<104} {'PASS' if res else 'FAIL'}", flush=True)
    print(f"bundlesweep.py: {len(CHECKS) if ok else 'not all'}/{len(CHECKS)}")
    return ok


def mutants():
    caught = 0
    for name, fn in CHECKS:
        res = fn(1, False)
        caught += not res
        print(f"mutant 1 of {name[:2]}: {'caught' if not res else 'MISSED'}")
    print(f"bundlesweep.py mutants: {caught}/{len(CHECKS)}")
    return caught == len(CHECKS)


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--texts" not in a:
        print(__doc__)
        sys.exit(2 if a else 0)                      # asked to run without the full text: not a pass (D184)
    cw.B = a[a.index("--texts") + 1].rstrip("/") + "/mcp-alphaXiv-get_paper_content-"
    if "--out" in a:
        rows = sweep()[4]
        with open(a[a.index("--out") + 1], "w") as fh:
            csv.writer(fh, delimiter="\t").writerows(rows)
    if "--mutants" in a:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if run("-v" in a) else 1)
