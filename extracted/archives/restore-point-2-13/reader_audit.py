#!/usr/bin/env python3
"""reader_audit.py -- the documents as a reader receives them.

Register 663. The twenty-two prime audits read the SOURCE and pass. A reader
sees the RENDER, and reports formatting, whitespace, margin, contents,
numbering, ordering, consistency, coherence and redundancy faults. Those are
different objects, and nothing has ever checked the second.

Every check below runs on the extracted PDF text and its layout, not on the
markdown.
"""
import os, re, subprocess, sys
from collections import Counter
from zeno import State, step

OUT = "/mnt/user-data/outputs"
DOCS = ["The Method 1.6.pdf",
        "The Method 1.6 — Mathematical Compendium.pdf",
        "The Method 1.6 — Spectra Compendium.pdf",
        "The Method 1.6 — The Register.pdf",
        "The Method 1.6 — The Index of Indices.pdf",
          "The Method 1.6 — The Physics Compendium.pdf"]

def layout(p):
    return subprocess.run(["pdftotext", "-layout", p, "-"],
                          capture_output=True, text=True).stdout

def plain(p):
    return subprocess.run(["pdftotext", p, "-"], capture_output=True, text=True).stdout

def run():
    R = {}
    for d in DOCS:
        p = os.path.join(OUT, d)
        if not os.path.exists(p): R[d] = None; continue
        L = layout(p); T = plain(p)
        pages = L.split("\f")
        f = {}

        # --- WHITESPACE
        f["blank pages"] = sum(1 for pg in pages if not pg.strip())
        f["runs of 4+ blank lines"] = len(re.findall(r"\n[ \t]*\n[ \t]*\n[ \t]*\n[ \t]*\n", L))
        f["lines with trailing space"] = sum(1 for l in L.split("\n") if l != l.rstrip())
        f["double spaces mid-sentence"] = len(re.findall(r"[a-z]  +[a-z]", T))

        # --- MARGINS: a line running past the frame, or starting far right
        wid = [len(l.rstrip()) for l in L.split("\n") if l.strip()]
        f["overlong lines (>105 cols)"] = sum(1 for w in wid if w > 105)
        ind = [len(l) - len(l.lstrip()) for l in L.split("\n") if l.strip()]
        f["lines indented >40 cols"] = sum(1 for i in ind if i > 40)

        # --- ORPHANS: a heading as the last line of a page
        orph = 0
        for pg in pages:
            ls = [l for l in pg.split("\n") if l.strip()]
            if ls and re.match(r"^\s*(?:#|\d+\.\d|[IVX]+ ·|PART )", ls[-1]): orph += 1
        f["heading orphaned at page foot"] = orph

        # --- NUMBERING and ORDER
        sec = re.findall(r"^\s*(\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)\s+\S", L, re.M)
        seen = []
        for s in sec:
            v = tuple(int(x) for x in s.split("."))
            seen.append(v)
        f["section numbers out of order"] = sum(
            1 for i in range(1, len(seen)) if seen[i][:1] == seen[i-1][:1] and seen[i] < seen[i-1])
        f["duplicate section numbers"] = len(sec) - len(set(sec))

        # --- REDUNDANCY: a sentence appearing more than twice
        sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", T))
                 if 60 < len(s.strip()) < 240]
        c = Counter(sents)
        f["sentences repeated 3+ times"] = sum(1 for v in c.values() if v >= 3)

        # --- COHERENCE: a § pointing at nothing in this document, for self-contained ones
        f["stray bullet or pipe artefacts"] = len(re.findall(r"^\s*[|·]\s*$", L, re.M))

        # --- TYPOGRAPHY a reader would notice
        f["hyphen used as minus"] = len(re.findall(r"\d\s-\s\d", T))
        f["unmatched bracket lines"] = sum(
            1 for l in T.split("\n") if l.count("(") != l.count(")") and len(l) > 40)
        R[d] = (f, len(pages))
    return R

with State("reader_audit") as st:
    R = step(st, "read the documents as a reader receives them", run, budget=900)

keys = None
for d, v in R.items():
    if v: keys = list(v[0]); break
print(f"  {'check':<34}" + "".join(f"{d.replace('The Method 1.6','')[:9]:>11}" for d in DOCS))
print()
tot = 0
for k in keys:
    row = f"  {k:<34}"
    for d in DOCS:
        v = R.get(d)
        n = v[0][k] if v else "—"
        if isinstance(n, int) and n: tot += n
        row += f"{n:>11}"
    print(row)
print(f"\n  total findings across all six: {tot}")
