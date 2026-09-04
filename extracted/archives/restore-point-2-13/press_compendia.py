#!/usr/bin/env python3
"""press_compendia.py -- searchable PDFs for the five compendia.

Reuses the book press's font registration and glyph handling so the same
characters render — Greek, subscripts, arrows, the lattice operators — and the
text layer stays searchable.

Markdown handled: # ## ### headings, | tables |, **bold**, *italic*, `code`,
> blockquotes, --- rules, and plain paragraphs.
"""
import os, re, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, Image)
from PIL import Image as PILImage
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth

FD = "/usr/share/fonts/truetype/freefont"
for nm, fn in (("Serif", "FreeSerif.ttf"), ("Serif-B", "FreeSerifBold.ttf"),
               ("Serif-I", "FreeSerifItalic.ttf"), ("Mono", "FreeMono.ttf"),
               ("Sans", "FreeSans.ttf")):
    p = os.path.join(FD, fn)
    if os.path.exists(p): pdfmetrics.registerFont(TTFont(nm, p))

INK = HexColor("#1a1a1a"); GREY = HexColor("#5a5a5a"); RED = HexColor("#b03030")

# FreeSerifBold has NO blackboard-bold glyphs — ℝ ℂ ℤ ℕ ℚ are absent from the
# bold face and present in the regular, so each was silently DROPPED inside a
# bold span, taking ℝ out of Λ = { … ∈ ℤ⁸ … } wherever it was emphasised.
# Every face is now checked and any character it lacks is wrapped in a face that
# has it (register 653).
from fontTools.ttLib import TTFont as _FT
_CMAP = {}
for _nm, _fn in (("Serif", "FreeSerif.ttf"), ("Serif-B", "FreeSerifBold.ttf"),
                 ("Serif-I", "FreeSerifItalic.ttf"), ("Mono", "FreeMono.ttf")):
    _p = os.path.join(FD, _fn)
    if os.path.exists(_p): _CMAP[_nm] = set(_FT(_p).getBestCmap())

def fallback(t, face):
    """wrap any character the face lacks in one that has it"""
    have = _CMAP.get(face)
    if not have: return t
    out = []; buf = []
    for ch in t:
        if ord(ch) < 128 or ord(ch) in have: buf.append(ch)
        else:
            alt = next((f for f in ("Serif", "Serif-I", "Mono")
                        if ord(ch) in _CMAP.get(f, ())), None)
            if alt:
                if buf: out.append("".join(buf)); buf = []
                out.append(f'<font name="{alt}">{ch}</font>')
            else: buf.append(ch)
    if buf: out.append("".join(buf))
    return "".join(out)

S = {
 "h1": ParagraphStyle("h1", fontName="Serif-B", fontSize=17, leading=21,
                      textColor=INK, spaceBefore=20, spaceAfter=9),
 "h2": ParagraphStyle("h2", fontName="Serif-B", fontSize=13, leading=17,
                      textColor=INK, spaceBefore=15, spaceAfter=6),
 "h3": ParagraphStyle("h3", fontName="Serif-B", fontSize=10.5, leading=14,
                      textColor=INK, spaceBefore=10, spaceAfter=4),
 "body": ParagraphStyle("body", fontName="Serif", fontSize=9.2, leading=12.6,
                        textColor=INK, alignment=TA_LEFT, spaceAfter=5),
 "quote": ParagraphStyle("quote", fontName="Serif-I", fontSize=9.4, leading=13,
                         textColor=GREY, leftIndent=16, spaceBefore=4, spaceAfter=6),
 "cell": ParagraphStyle("cell", fontName="Serif", fontSize=7.6, leading=9.6,
                        textColor=INK),
 "cellb": ParagraphStyle("cellb", fontName="Serif-B", fontSize=7.6, leading=9.6,
                         textColor=INK),
}

def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def inline(t):
    t = esc(t)
    t = re.sub(r"\*\*(.+?)\*\*",
               lambda m: f'<font name="Serif-B">{fallback(m.group(1), "Serif-B")}</font>', t)
    # w*, h*, ν* are notation, not emphasis: an asterisk directly after a letter
    # or digit is protected before the italic pass (register 632)
    t = re.sub(r"(?<=[A-Za-z0-9\u0370-\u03ff])\*", "\u2217", t)
    t = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r'<font name="Serif-I">\1</font>', t)
    t = t.replace("\u2217", "*")
    t = re.sub(r"`([^`]+?)`", r'<font name="Mono" size="8.2">\1</font>', t)
    t = t.replace("\\|", "|").replace("\\_", "_").replace("\\*", "*")
    return t

def build(md, out, title):
    doc = BaseDocTemplate(out, pagesize=A4,
                          leftMargin=0.85*inch, rightMargin=0.85*inch,
                          topMargin=0.8*inch, bottomMargin=0.8*inch, title=title)
    fr = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    def deco(cv, d):
        cv.saveState(); cv.setFont("Serif", 7.6); cv.setFillColor(GREY)
        cv.drawCentredString(A4[0]/2, 0.5*inch, str(cv.getPageNumber()))
        cv.restoreState()
    doc.addPageTemplates([PageTemplate(id="p", frames=[fr], onPage=deco)])

    story = []
    lines = open(md, encoding="utf-8").read().split("\n")
    i = 0
    while i < len(lines):
        l = lines[i]
        # a genuine table's separator row has the SAME column count as its header
        # and every cell is dashes; a register entry carrying pipes in a formula
        # is prose and must not be parsed as a table (register 637)
        _isTable = (l.startswith("|") and i + 1 < len(lines)
                    and lines[i+1].strip().startswith("|")
                    and set(lines[i+1].replace("|", "").strip()) <= set("-: ")
                    and lines[i+1].strip()
                    and len(lines[i+1].strip("|").split("|")) == len(l.strip("|").split("|"))
                    and all(set(c.strip()) <= set("-:") and c.strip()
                            for c in lines[i+1].strip("|").split("|")))
        if _isTable:
            rows = []
            hdr = [c.strip() for c in l.strip("|").split("|")]
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip("|").split("|")]); i += 1
            data = [[Paragraph(inline(c), S["cellb"]) for c in hdr]] + \
                   [[Paragraph(inline(c), S["cell"]) for c in r] for r in rows]
            n = len(hdr); w = doc.width / n
            # a row taller than the frame cannot be placed; splitByRow lets long
            # tables break across pages (register 637)
            # Character counts under-measure: a floor of 4.2% left 'n' too narrow
            # for "3-5" once cell padding was added, and 'fits' broke its own
            # header. Widths are measured in POINTS with stringWidth, and each
            # column is given at least its widest unbreakable token plus padding
            # (register 668).
            PAD = 15.0   # 4 left + 6 right default + a glyph of safety
            MONO = 1.34  # a code span renders in Mono at 8.2 where the measurement
                         # assumes Serif at 7.6, so `A.alph` broke mid-identifier
            need = []
            for j in range(n):
                col = [hdr[j]] + [r[j] if j < len(r) else "" for r in rows]
                mn = 0.0; mx = 0.0
                for c in col:
                    c = re.sub(r"\*\*|\*|`", "", c).strip()
                    if not c: continue
                    _mono = "`" in (col[0] if False else c) or c.startswith("`")
                    _f, _sz = ("Mono", 8.2) if "`" in c else ("Serif", 7.6)
                    c = re.sub(r"`", "", c)
                    _k = MONO if "`" in col[min(1,len(col)-1)] else 1.0
                    mx = max(mx, stringWidth(c, _f, _sz)*_k)
                    for tok in re.split(r"[ ]", c.replace("\u00a0"," ")):
                        mn = max(mn, stringWidth(tok, "Serif-B" if c in hdr else _f, _sz)*_k)
                need.append((mn + PAD, mx + PAD))
            floor = [a for a, b in need]
            want = [b for a, b in need]
            tot = sum(want) or 1.0
            if sum(floor) >= doc.width:
                wid = [doc.width * a / sum(floor) for a in floor]
            else:
                slack = doc.width - sum(floor)
                extra = sum(max(0.0, b - a) for a, b in need) or 1.0
                wid = [a + slack * max(0.0, b - a) / extra for a, b in need]
            # A table wider than the frame is CENTRED by reportlab, so it overflows
            # BOTH edges and the first column is cut off the page — which is what
            # happened to the operators table. Clamp, then pin left (register 669).
            _sw = sum(wid)
            if _sw > doc.width: wid = [x*doc.width/_sw for x in wid]
            t = Table(data, colWidths=wid, repeatRows=1, splitByRow=1)
            t.hAlign = 'LEFT'
            t.setStyle(TableStyle([
                ("VALIGN", (0,0), (-1,-1), "TOP"),
                ("LINEBELOW", (0,0), (-1,0), 0.6, INK),
                ("LINEBELOW", (0,1), (-1,-2), 0.2, HexColor("#dddddd")),
                ("TOPPADDING", (0,0), (-1,-1), 2.4),
                ("BOTTOMPADDING", (0,0), (-1,-1), 2.4),
                ("LEFTPADDING", (0,0), (-1,-1), 4),
            ]))
            # and a single cell taller than a page still cannot fit, so oversized
            # tables are emitted row-group by row-group
            if len(data) > 40:
                for k in range(1, len(data), 30):
                    chunk = [data[0]] + data[k:k+30]
                    tt = Table(chunk, colWidths=wid, repeatRows=1, splitByRow=1)
                    tt.hAlign = 'LEFT'
                    tt.setStyle(t.getStyle() if hasattr(t, "getStyle") else TableStyle([
                        ("VALIGN", (0,0), (-1,-1), "TOP"),
                        ("LINEBELOW", (0,0), (-1,0), 0.6, INK),
                        ("TOPPADDING", (0,0), (-1,-1), 2.4),
                        ("BOTTOMPADDING", (0,0), (-1,-1), 2.4)]))
                    story += [Spacer(1, 4), tt, Spacer(1, 7)]
            else:
                story += [Spacer(1, 4), t, Spacer(1, 7)]
            continue
        # ![caption](file.png) — a figure, scaled to the frame and kept with its caption
        _im = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", l.strip())
        if _im and os.path.exists(_im.group(2)):
            iw, ih = PILImage.open(_im.group(2)).size
            w = min(doc.width, iw * 0.62); h = w * ih / iw
            if h > doc.height * 0.62: h = doc.height * 0.62; w = h * iw / ih
            blk = [Image(_im.group(2), width=w, height=h)]
            if _im.group(1):
                blk.append(Spacer(1, 3))
                blk.append(Paragraph(inline(_im.group(1)),
                    ParagraphStyle("cap", parent=S["body"], fontSize=8.2, leading=11,
                                   textColor=GREY, alignment=1)))
            story += [Spacer(1, 8), KeepTogether(blk), Spacer(1, 10)]
            i += 1; continue
        if l.startswith("### "): story.append(Paragraph(inline(l[4:]), S["h3"]))
        elif l.startswith("## "): story.append(Paragraph(inline(l[3:]), S["h2"]))
        elif l.startswith("# "):  story.append(Paragraph(inline(l[2:]), S["h1"]))
        elif l.startswith("> "):  story.append(Paragraph(inline(l[2:]), S["quote"]))
        elif l.strip() == "---":  story.append(Spacer(1, 10))
        elif l.startswith("```"):
            i += 1; buf = []
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i]); i += 1
            for b in buf:
                story.append(Paragraph(f'<font name="Mono" size="7.4">{esc(b) or "&nbsp;"}</font>',
                                       S["body"]))
        elif l.strip():
            # markdown wraps: join consecutive body lines so **bold** spanning a
            # line break closes properly instead of leaking asterisks
            buf = [l]
            while (i + 1 < len(lines) and lines[i+1].strip()
                   and not lines[i+1].startswith(("|", "#", ">", "```", "---"))):
                i += 1; buf.append(lines[i])
            story.append(Paragraph(inline(" ".join(x.strip() for x in buf)), S["body"]))
        i += 1
    doc.build(story)
    return out

for md, out, title in (("COMPENDIUM.md", "/mnt/user-data/outputs/The Method 1.6 — Mathematical Compendium.pdf",
                        "The Method 1.6 — Mathematical Compendium"),
                       ("SPECTRA.md", "/mnt/user-data/outputs/The Method 1.6 — Spectra Compendium.pdf",
                        "The Method 1.6 — Spectra Compendium"),
                       ("REGISTER.md", "/mnt/user-data/outputs/The Method 1.6 — The Register.pdf",
                        "The Method 1.6 — The Register"),
                       ("INDICES.md", "/mnt/user-data/outputs/The Method 1.6 — The Index of Indices.pdf",
                        "The Method 1.6 — The Index of Indices"),
                       ("PHYSICS.md", "/mnt/user-data/outputs/The Method 1.6 — The Physics Compendium.pdf",
                        "The Method 1.6 — The Physics Compendium")):
    if os.path.exists(md):
        p = build(md, out, title)
        print(f"  BUILT {p}  {os.path.getsize(p):,} bytes")
