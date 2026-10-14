#!/usr/bin/env python3
"""summary.py -- one row per paper, read from the files: title, pages, obligations, audit outcome.

    python3 papers/method/summary.py          prints a Markdown table
The check totals are read from the papers' own logs in the scratchpad checks/ directory when
present, else marked '-' ; nothing here recomputes a check.
"""
import os, re, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
S = "/tmp/claude-0/-home-user-Claude-Method-Works/550096c1-e482-5fca-a954-6b4d26a5afe4/scratchpad/checks"

def pages(pdf):
    try:
        import pypdf
        return len(pypdf.PdfReader(pdf).pages)
    except Exception:
        return "-"

def markup(pdf):
    try:
        import pypdf
        t = "".join(p.extract_text() or "" for p in pypdf.PdfReader(pdf).pages)
        return t.count("_") + t.count("^") + t.count("\\")
    except Exception:
        return "-"

def audit(d):
    p = os.path.join(d, "AUDIT.md")
    if not os.path.isfile(p):
        return "-", "-", "-"
    t = open(p, encoding="utf-8").read()
    i = t.find("## Part C")
    t = t[i:] if i >= 0 else t
    rows = [ln for ln in t.split("\n") if re.match(r"^\| *(A|R)-", ln)]
    fixed = sum(1 for ln in rows if "FIXED" in ln)
    decl = sum(1 for ln in rows if "DECLINED" in ln and "FIXED" not in ln)
    blank = sum(1 for ln in rows if "FIXED" not in ln and "DECLINED" not in ln)
    return len(rows), fixed, blank

print("| paper | title | pages | markup | audit rows | fixed | blank |")
print("|---|---|---|---|---|---|---|")
for d in sorted(glob.glob(os.path.join(HERE, "[0-9][0-9]-*"))):
    name = os.path.basename(d)
    title = open(os.path.join(d, "PAPER.md"), encoding="utf-8").readline().lstrip("# ").strip()
    pdf = os.path.join(OUT, name + ".pdf")
    n, f, b = audit(d)
    print("| %s | %s | %s | %s | %s | %s | %s |" % (name, title, pages(pdf), markup(pdf), n, f, b))
