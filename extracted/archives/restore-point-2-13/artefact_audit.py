#!/usr/bin/env python3
"""artefact_audit.py -- PART 3: the five PDFs as artefacts.

Register 652: parts 1 and 2 checked the sources. This checks what a reader
actually receives — that each PDF exists, is searchable, renders its glyphs,
leaks no markup, carries its figures, and contains the text its source does.

The last is the one that matters: a source can be correct and the press can
silently drop a paragraph, which it did once this session while every audit
passed.
"""
import os, re, subprocess, sys
from zeno import State, step

OUT = "/mnt/user-data/outputs"
PAIRS = [
 ("The Method 1.6.pdf",                          "The Method 1.6.md",  33),
 ("The Method 1.6 — Mathematical Compendium.pdf", "COMPENDIUM.md",      0),
 ("The Method 1.6 — Spectra Compendium.pdf",      "SPECTRA.md",         0),
 ("The Method 1.6 — The Register.pdf",            "REGISTER.md",        0),
 ("The Method 1.6 — The Index of Indices.pdf",    "INDICES.md",         4),
]

def txt(p):
    return subprocess.run(["pdftotext", p, "-"], capture_output=True, text=True).stdout

def imgs(p):
    o = subprocess.run(["pdfimages", "-list", p], capture_output=True, text=True).stdout
    return sum(1 for l in o.splitlines()[2:] if l.split() and l.split()[2] == "image")

def pages(p):
    o = subprocess.run(["pdfinfo", p], capture_output=True, text=True).stdout
    m = re.search(r"Pages:\s+(\d+)", o)
    return int(m.group(1)) if m else 0

def run():
    rows = []
    for pdf, src, want_img in PAIRS:
        pp = os.path.join(OUT, pdf)
        if not os.path.exists(pp):
            rows.append((pdf, None)); continue
        t = txt(pp)
        s = open(src, encoding="utf-8").read() if os.path.exists(src) else ""
        # a sample of the source's own sentences must appear in the rendered text
        # the sample must be compared in RENDERED form: backticks become a font
        # span and vanish, and *italics* likewise (register 651)
        def _plain(x):
            x = re.sub(r"`([^`]+)`", r"\1", x)
            x = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"\1", x)
            return re.sub(r"\s+", " ", x).strip()
        sents = [_plain(x) for x in re.findall(r"\*\*([A-Z][^*\n]{28,90})\*\*", s)][:400]
        # a sentence spanning a page break has the page NUMBER between its halves,
        # so bare numeric lines are stripped before flattening (register 651)
        # page furniture between the halves of a wrapped sentence: a bare page
        # number, or the book's running header (register 660)
        # only the BOOK's running header, which is a fixed string — a broader
        # pattern ate the compendium titles out of the sample itself
        _HDR = re.compile(r"\s*(?:\d{1,4}|The Method — The Lach Cylinder)\s*$")
        _t = "\n".join(l for l in t.split("\n") if not _HDR.fullmatch(l))
        flat = re.sub(r"\s+", " ", _t)
        miss = [x for x in sents if re.sub(r"\s+", " ", x) not in flat]
        rows.append((pdf, dict(
            pages=pages(pp), size=os.path.getsize(pp), chars=len(t),
            glyphs=t.count("\ufffd"), markup=len(re.findall(r"\*\*", t)),
            images=imgs(pp), want_img=want_img,
            sampled=len(sents), missing=len(miss),
            sample_miss=miss[:2])))
    return rows

with State("artefact_audit") as st:
    rows = step(st, "check the five artefacts", run, budget=900)

print("  PART 3 · THE ARTEFACTS\n")
print(f"  {'document':<40}{'pp':>4}{'chars':>9}{'glyph':>7}{'markup':>8}{'figs':>6}{'lost':>6}")
bad = []
for pdf, r in rows:
    if r is None:
        print(f"  {pdf[:38]:<40}{'MISSING':>40}"); bad.append((pdf, "absent")); continue
    fig = f"{r['images']}/{r['want_img']}" if r["want_img"] else str(r["images"])
    print(f"  {pdf[:38]:<40}{r['pages']:>4}{r['chars']:>9,}{r['glyphs']:>7}"
          f"{r['markup']:>8}{fig:>6}{r['missing']:>6}")
    if r["glyphs"]: bad.append((pdf, f"{r['glyphs']} replacement glyphs"))
    if r["markup"]: bad.append((pdf, f"{r['markup']} leaked markup"))
    if r["want_img"] and r["images"] < r["want_img"]:
        bad.append((pdf, f"{r['images']} figures, expected {r['want_img']}"))
    if r["missing"]: bad.append((pdf, f"{r['missing']} of {r['sampled']} bold statements not rendered"))
print()
for pdf, r in rows:
    if r and r["missing"]:
        print(f"  {pdf}: {r['missing']} of {r['sampled']} sampled statements absent from the PDF")
        for x in r["sample_miss"]: print(f"      {x[:88]}")
print("\n" + ("PART 3 PASSES" if not bad else f"FAILURES: {len(bad)}"))
for p, w in bad: print(f"    {p[:44]:<46}{w}")
sys.exit(1 if bad else 0)
