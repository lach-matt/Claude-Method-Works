#!/usr/bin/env python3
"""censusweep.py -- a second, mechanical census of the passages carried to n = 4 (N1STAR-PROOF.md section 10.69; D139).

The censuses behind 10.64-10.68 were taken by reading the full texts. This sweep takes another route: every marker of
the dimension -- S^2, S^3, R^3, R^4, R^10, 3 + 1, "dimension", "k-dimensional", n - 1, n - 2, n/2, n + 1, a 7 x 7
count, and the densities |x|^3, r^2 |d..|, x^-6 -- on every page of each carried passage, written to a TSV for
reading against the sections.  The full texts are alphaXiv's (get_paper_content, fullText = true, 2026-10-24); they are
not stored here, so the sweep runs only where they have been fetched: pass their directory with --texts and the CD03
page-marked copy with --cd03.  Labels: computed (a token search), the accounting READ.

Result at 2026-10-24: 270 hits on 204 pages -- [Hin23a] section 3 104, [Hin26a] section 5.2 25, [Hin26c] sections 7-8
and 9.3 26, [Hin26]'s boost sections 65, [HHV21] pp. 89-93 10, [CD03] Theorem 8.1 and Appendix E 40 -- every one
accounted for by 10.53-10.58 and 10.63-10.68, but one: [Hin26a] p. 62's density r^3 |dr dgslash| on level sets of
tau, the metric density times rho^-1 (its p. 65), which is r^4 |dr dgslash_S3| at n = 4 (10.69).

python3 censusweep.py --texts DIR --cd03 FILE --out hits.tsv
"""
import sys
import re
import csv
B = ""          # set from --texts: DIR/mcp-alphaXiv-get_paper_content-
CD03 = ""
OUT = "hits.tsv"
DOCS = {
    "hin23a": ("1792876303206", "PETER HINTZ", "EXTERIOR STABILITY", [(9, 33)]),
    "hin26a": ("1792616766216", "PETER HINTZ", "CONSTRAINT DAMPING ON KERR", [(38, 66)]),
    "hin26c": ("1792874903883", "PETER HINTZ", r"\(NON-\)LINEAR WAVES ON ASYMPTOTICALLY FLAT SPACETIMES\. II",
               [(114, 157), (174, 193)]),
    "hin26": ("1792874903290", "PETER HINTZ", "NONLINEAR STABILITY OF SUBEXTREMAL KERR",
              [(77, 81), (108, 110), (238, 262), (267, 278), (301, 326)]),
    "hhv21": ("1792874904621", r"DIETRICH H[^\n]{0,40}", "LINEAR STABILITY OF KERR BLACK HOLES", [(89, 93)]),
}
PATS = [("S2", r"\bS 2\b(?! ?(e|sc|b)? ?T)"), ("S3", r"\bS 3\b"), ("R3", r"\bR 3\b"), ("R4", r"\bR 4\b"),
        ("R10", r"\bR 10\b"), ("3+1", r"3 \+ 1|1 \+ 3|R 1,3|R 1\+3"), ("dim", r"dimension"),
        ("ndim", r"(three|four|3|4|2|5|7|10)-dimensional"),
        ("n-expr", r"\(n ?− ?[123]\)|n ?− ?[123]\b|n/2|\bn ?\+ ?1\b"),
        ("7", r"\b7 × 7\b|\bC 7\b|namely 7"), ("dens", r"\|x\| ?3\b|r 2 \|d|x −6|\bρ 4 I\b|r 3 \|d")]


def pages(doc):
    f, even, odd, _ = DOCS[doc]
    t = open(B + f + ".txt").read()
    marks = [(m.start(), int(m.group(1))) for m in re.finditer(r"\n(\d{1,3}) " + even + r"\n", t)]
    marks += [(m.start(), int(m.group(1))) for m in re.finditer(r"\n" + odd + r" (\d{1,3})\n", t)]
    marks.sort()
    out = {}
    for (a, p), (b, _) in zip(marks, marks[1:] + [(len(t), 0)]):
        out[p] = re.sub(r"\s+", " ", t[a:b])
    return out


def cd03_pages():
    t = open(CD03).read()
    parts = re.split(r"<<<PAGE (\d+)>>>", t)
    return {int(parts[i]): re.sub(r"\s+", " ", parts[i + 1]) for i in range(1, len(parts) - 1, 2)}


def run():
    rows = []
    allp = {d: pages(d) for d in DOCS}
    allp["cd03"] = cd03_pages()
    ranges = {d: v[3] for d, v in DOCS.items()}
    ranges["cd03"] = [(35, 37), (71, 77)]
    for d, pg in allp.items():
        for lo, hi in ranges[d]:
            for p in range(lo, hi + 1):
                txt = pg.get(p, "")
                if not txt:
                    rows.append((d, p, "MISSING", ""))
                for name, pat in PATS:
                    for m in re.finditer(pat, txt):
                        rows.append((d, p, name, txt[max(0, m.start() - 70):m.end() + 50]))
    with open(OUT, "w") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerows(rows)
    from collections import Counter
    c = Counter((r[0], r[2]) for r in rows)
    for d in allp:
        print(d, {k[1]: v for k, v in c.items() if k[0] == d}, "pages found:", sum(1 for lo, hi in ranges[d]
                                                                                    for p in range(lo, hi + 1)
                                                                                    if p in allp[d]))


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--texts" not in a or "--cd03" not in a:
        print(__doc__)
        sys.exit(0)
    B = a[a.index("--texts") + 1].rstrip("/") + "/mcp-alphaXiv-get_paper_content-"
    CD03 = a[a.index("--cd03") + 1]
    OUT = a[a.index("--out") + 1] if "--out" in a else OUT
    run()
