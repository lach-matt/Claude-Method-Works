#!/usr/bin/env python3
"""render_paper.py -- the paper's prose cannot state a number; it can only cite one.

WHY THIS EXISTS
---------------
`verify_paper.py` pass 3 asks whether every number in the prose is carried by
SOME ledger row. That is a VALUE test, not a BINDING test, and it has now let
two wrong figures through: three sec.9 quantities wrong by 1-5 percent, and a
0.855 that should have been 0.854, each passing because an unrelated row in an
800-row ledger happened to carry that value. The weakness is recorded at [3]
sec.9.9 and was left unrepaired because repairing it changes the standard.

This is the repair, and it is structural rather than procedural. The paper's
SOURCE carries no numerals in its prose at all. It carries citations --
`[[C044]]` -- and this program resolves each against `papers/CLAIMS.tsv` at
render time. A sentence therefore CANNOT acquire a figure the mathematics does
not produce, because a sentence cannot hold a figure at all. Pass 3 becomes
true by construction, and `audit_paper.py` audit 24 checks the one thing that
can still go wrong: a numeral typed into the source by hand.

CITATION FORMS
--------------
    [[C044]]     value and unit          "26.06 MeV"
    [[C044#]]    value alone             "26.06"
    [[C044~]]    unit alone              "MeV"
    [[C044!]]    value, unit, and the row's STATUS in brackets -- required
                 wherever a WITHDRAWN or RECONSTRUCTED row is cited, so a
                 status is never flattened by being quoted plainly
    [[?C044]]    the row's CLAIM TEXT, not its value

Scientific notation in the ledger ("2.80e14") renders as 2.80 x 10^14 in every
output. A unit the reader does not need to see -- ratio, count, dimensionless,
fraction -- is dropped from [[Cnnn]] and still available through [[Cnnn~]].

OUTPUTS, ALL FROM THE ONE SOURCE
--------------------------------
    --md     resolved Markdown       (what verify_paper.py reads)
    --html   a self-contained page
    --docx   Word, via python-docx
    --pdf    via reportlab
Audit 16 FIDELITY -- artefact against other places -- holds by construction
here: the four outputs are one document rendered four ways, not four documents.

    python3 tools/render_paper.py papers/Cold_Fusion_v1.0.src.md --all
    python3 tools/render_paper.py --selftest
"""
import argparse
import csv
import html as _html
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "papers", "CLAIMS.tsv")

# units the reader does not need printed; still reachable through [[Cnnn~]]
SILENT_UNITS = {"ratio", "count", "dimensionless", "fraction", "x", "-", ""}
# a status that must never be quoted plainly: [[Cnnn!]] is required for these
LOUD_STATUSES = {"WITHDRAWN", "RECONSTRUCTED", "PROJECTED", "ASSUMED", "DESIGN"}

# The ledger writes units in ASCII because it is a data file. This is DISPLAY
# only -- the value is never touched, and no substitution here can change a
# quantity, only how its unit is set.
UNIT_DISPLAY = (
    ("pi-/interacting p", "\u03c0\u207b per interacting proton"),
    ("pi-/p", "\u03c0\u207b per proton"),
    ("mu-/p", "\u03bc\u207b per proton"),
    ("g/cm2", "g/cm^2"), ("W/cm2", "W/cm^2"), ("cm3/mol", "cm^3/mol"),
    ("cm2", "cm^2"), ("cm3", "cm^3"),
    ("m_e", "electron masses"),
    ("pi-", "\u03c0\u207b"), ("mu-", "\u03bc\u207b"),
    ("pi+", "\u03c0\u207a"), ("mu+", "\u03bc\u207a"),
)


def display_unit(u):
    for a, b in UNIT_DISPLAY:
        if u == a:
            return b
    return u

CITE = re.compile(r"\[\[(\?)?(C\d+)([#~!])?\]\]")


def load_claims(path=LEDGER):
    with open(path, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    return {r["id"]: r for r in rows}


def fmt_value(v):
    """2.80e14 -> 2.80 x 10^14, everything else verbatim from the ledger."""
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?)e([+-]?\d+)", v.strip())
    if not m:
        return v.strip()
    return f"{m.group(1)} × 10^{int(m.group(2))}"


SUP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def supers(s):
    """x^-1 -> x(superscript -1), anywhere in a value or a unit."""
    return re.sub(r"\^\{?(-?\d+)\}?", lambda m: m.group(1).translate(SUP), s)


def fmt_value_unicode(v):
    return supers(fmt_value(v))


def render_citation(row, mode, unicode_sup=True):
    val = fmt_value_unicode(row["value"]) if unicode_sup else fmt_value(row["value"])
    unit = display_unit(row["unit"].strip())
    if unicode_sup:
        unit = supers(unit)
    if mode == "#":
        return val
    if mode == "~":
        return unit
    shown = val if unit.lower() in SILENT_UNITS else f"{val} {unit}"
    if mode == "!":
        return f"{shown} [{row['status']}]"
    return shown


def resolve(text, claims, unicode_sup=False, seen=None):
    """Replace every citation. An unknown id is an error, never a silent pass."""
    missing = []

    def sub(m):
        question, cid, mode = m.group(1), m.group(2), m.group(3)
        row = claims.get(cid)
        if row is None:
            missing.append(cid)
            return f"[[MISSING {cid}]]"
        if seen is not None:
            seen.setdefault(cid, 0)
            seen[cid] += 1
        if question:
            return row["claim"]
        if row["status"] in LOUD_STATUSES and mode != "!":
            missing.append(f"{cid}(status {row['status']} needs [[{cid}!]])")
            return f"[[UNMARKED {cid}]]"
        return render_citation(row, mode, unicode_sup)

    out = CITE.sub(sub, text)
    # A citation this pattern does not recognise -- [[C692b]], [[c44]], [[C 44]] --
    # would otherwise survive into the document as literal text, which is the one
    # way a malformed citation could reach a reader. It is an error, not a pass.
    for m in re.finditer(r"\[\[[^\]]{0,40}\]\]", out):
        missing.append(f"malformed citation {m.group(0)}")
    return out, missing


# ---- the document model ----------------------------------------------------
# A deliberately small Markdown subset. Anything richer would be a second thing
# to keep true across four outputs, and audit 16 FIDELITY is easier to hold than
# to repair.
FRONT_KEYS = ("TITLE", "SUBTITLE", "AUTHOR", "DATE", "RUNNING", "ABSTRACTHEAD")


def parse(src):
    """(front matter dict, [block]). A block is (kind, payload)."""
    front, lines = {}, src.split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r"^([A-Z]+):\s*(.*)$", lines[i])
        if not m or m.group(1) not in FRONT_KEYS:
            break
        front[m.group(1)] = m.group(2).strip()
        i += 1
    blocks, para, table = [], [], []
    last_list = None                      # a wrapped list item continues its own

    def flush_para():
        if para:
            blocks.append(("p", " ".join(para)))
            para.clear()

    def flush_table():
        if table:
            blocks.append(("table", list(table)))
            table.clear()

    for ln in lines[i:]:
        s = ln.rstrip()
        if s.startswith("|") and s.endswith("|"):
            flush_para()
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                table.append("SEP")
            else:
                table.append(cells)
            continue
        flush_table()
        if not s.strip():
            flush_para()
            last_list = None
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            flush_para()
            blocks.append((f"h{len(m.group(1))}", m.group(2).strip()))
            continue
        if s.strip() == "---":
            flush_para()
            blocks.append(("rule", ""))
            continue
        if s.startswith("> "):
            flush_para()
            if blocks and blocks[-1][0] == "quote":
                blocks[-1] = ("quote", blocks[-1][1] + " " + s[2:].strip())
            else:
                blocks.append(("quote", s[2:].strip()))
            continue
        m = re.match(r"^[-*]\s+(.*)$", s)
        if m:
            flush_para()
            blocks.append(("li", m.group(1).strip()))
            last_list = len(blocks) - 1
            continue
        m = re.match(r"^(\d+)\.\s+(.*)$", s)
        if m:
            flush_para()
            blocks.append(("oli", m.group(2).strip()))
            last_list = len(blocks) - 1
            continue
        # an indented line straight after a list item is that item wrapping, not
        # a new paragraph. Without this a wrapped item silently becomes prose,
        # which breaks every count of the list and every check of its markup.
        if (not para and last_list is not None and last_list == len(blocks) - 1
                and ln[:1] in (" ", "\t")):
            k, v = blocks[last_list]
            blocks[last_list] = (k, v + " " + s.strip())
            continue
        para.append(s.strip())
    flush_para()
    flush_table()
    return front, blocks


INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)")
SUP_RE = re.compile(r"\^\{?(-?\d+)\}?")


def _split_sup(text, b, i, c):
    """A run carrying x^-1 becomes three runs, the middle one superscript."""
    out, last = [], 0
    for m in SUP_RE.finditer(text):
        if m.start() > last:
            out.append((text[last:m.start()], b, i, c, False))
        out.append((m.group(1), b, i, c, True))
        last = m.end()
    if last < len(text):
        out.append((text[last:], b, i, c, False))
    return out or [(text, b, i, c, False)]


def inline_runs(text):
    """[(text, bold, italic, code, sup)] -- the one inline model all outputs share.

    Superscripts are carried as a FLAG, not as Unicode characters, because the
    four outputs mark them up four different ways and only one of them can rely
    on a font having the glyph."""
    out = []
    for piece in INLINE.split(text):
        if not piece:
            continue
        if piece.startswith("**") and piece.endswith("**"):
            out += _split_sup(piece[2:-2], True, False, False)
        elif piece.startswith("*") and piece.endswith("*") and len(piece) > 2:
            out += _split_sup(piece[1:-1], False, True, False)
        elif piece.startswith("`") and piece.endswith("`"):
            out.append((piece[1:-1], False, False, True, False))
        else:
            out += _split_sup(piece, False, False, False)
    return out


# ---- emitters --------------------------------------------------------------
def emit_md(front, blocks):
    out = []
    if front.get("TITLE"):
        out += [f"# {front['TITLE']}", ""]
    if front.get("SUBTITLE"):
        out += [f"*{front['SUBTITLE']}*", ""]
    if front.get("AUTHOR"):
        out += [front["AUTHOR"], ""]
    if front.get("DATE"):
        out += [front["DATE"], ""]
    for kind, payload in blocks:
        if kind.startswith("h"):
            out += ["", "#" * int(kind[1]) + " " + payload, ""]
        elif kind == "p":
            out += [payload, ""]
        elif kind == "quote":
            out += ["> " + payload, ""]
        elif kind == "li":
            out.append("- " + payload)
        elif kind == "oli":
            out.append("1. " + payload)
        elif kind == "rule":
            out += ["", "---", ""]
        elif kind == "table":
            for row in payload:
                out.append("|---|" if row == "SEP" else "| " + " | ".join(row) + " |")
            out.append("")
    return "\n".join(out) + "\n"


HTML_CSS = """
:root{--ink:#15140f;--mut:#5d5850;--rule:#d8d2c6;--bg:#fbfaf7;--acc:#7a2e12}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
 font:16px/1.62 "Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif}
.wrap{max-width:44rem;margin:0 auto;padding:4rem 1.5rem 6rem}
h1{font-size:2.05rem;line-height:1.18;margin:0 0 .4rem;letter-spacing:-.01em}
.sub{color:var(--mut);font-style:italic;font-size:1.08rem;margin:0 0 1.6rem}
.by{color:var(--mut);font-size:.92rem;margin:0 0 .2rem}
h2{font-size:1.34rem;margin:2.6rem 0 .7rem;padding-top:.9rem;border-top:1px solid var(--rule)}
h3{font-size:1.08rem;margin:1.9rem 0 .5rem}
h4{font-size:.97rem;margin:1.4rem 0 .4rem;color:var(--mut);
 text-transform:uppercase;letter-spacing:.06em}
p{margin:0 0 .95rem}
blockquote{margin:1.2rem 0;padding:.85rem 1.1rem;border-left:3px solid var(--acc);
 background:#f3efe6}
blockquote p{margin:0}
ul,ol{margin:0 0 1rem 1.2rem;padding:0}
li{margin:.3rem 0}
code{font:.88em/1.4 ui-monospace,"SF Mono",Menlo,Consolas,monospace;
 background:#efeade;padding:.08em .32em;border-radius:3px}
.tw{overflow-x:auto;margin:1.2rem 0}
table{border-collapse:collapse;width:100%;font-size:.92rem}
th,td{border:1px solid var(--rule);padding:.42rem .6rem;text-align:left;vertical-align:top}
th{background:#efeade;font-weight:600}
hr{border:0;border-top:1px solid var(--rule);margin:2.2rem 0}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
 --ink:#eae5da;--mut:#a29a8c;--rule:#3a352d;--bg:#141310;--acc:#c9743f}
 :root:not([data-theme="light"]) blockquote{background:#1e1b16}
 :root:not([data-theme="light"]) th{background:#1e1b16}
 :root:not([data-theme="light"]) code{background:#211e18}}
:root[data-theme="dark"]{--ink:#eae5da;--mut:#a29a8c;--rule:#3a352d;--bg:#141310;--acc:#c9743f}
:root[data-theme="dark"] blockquote,:root[data-theme="dark"] th{background:#1e1b16}
:root[data-theme="dark"] code{background:#211e18}
"""


def _h_inline(text):
    out = []
    for t, b, i, c, sup in inline_runs(text):
        e = _html.escape(t)
        if sup:
            e = f"<sup>{e}</sup>"
        if c:
            e = f"<code>{e}</code>"
        if b:
            e = f"<strong>{e}</strong>"
        if i:
            e = f"<em>{e}</em>"
        out.append(e)
    return "".join(out)


def emit_html(front, blocks):
    o = [f"<title>{_html.escape(front.get('TITLE','Paper'))}</title>",
         f"<style>{HTML_CSS}</style>", '<div class="wrap">']
    if front.get("TITLE"):
        o.append(f"<h1>{_h_inline(front['TITLE'])}</h1>")
    if front.get("SUBTITLE"):
        o.append(f'<p class="sub">{_h_inline(front["SUBTITLE"])}</p>')
    for k in ("AUTHOR", "DATE"):
        if front.get(k):
            o.append(f'<p class="by">{_h_inline(front[k])}</p>')
    mode = None

    def close():
        nonlocal mode
        if mode:
            o.append(f"</{mode}>")
            mode = None

    for kind, payload in blocks:
        if kind not in ("li", "oli"):
            close()
        if kind.startswith("h"):
            o.append(f"<h{kind[1]}>{_h_inline(payload)}</h{kind[1]}>")
        elif kind == "p":
            o.append(f"<p>{_h_inline(payload)}</p>")
        elif kind == "quote":
            o.append(f"<blockquote><p>{_h_inline(payload)}</p></blockquote>")
        elif kind in ("li", "oli"):
            want = "ul" if kind == "li" else "ol"
            if mode != want:
                close()
                o.append(f"<{want}>")
                mode = want
            o.append(f"<li>{_h_inline(payload)}</li>")
        elif kind == "rule":
            o.append("<hr>")
        elif kind == "table":
            rows = payload
            head = rows[0] if len(rows) > 1 and rows[1] == "SEP" else None
            body = rows[2:] if head else [r for r in rows if r != "SEP"]
            o.append('<div class="tw"><table>')
            if head:
                o.append("<tr>" + "".join(f"<th>{_h_inline(c)}</th>" for c in head) + "</tr>")
            for r in body:
                o.append("<tr>" + "".join(f"<td>{_h_inline(c)}</td>" for c in r) + "</tr>")
            o.append("</table></div>")
    close()
    o.append("</div>")
    return "\n".join(o) + "\n"


def emit_docx(front, blocks, path):
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.shared import Pt, Inches, RGBColor

    doc = Document()
    for s in doc.sections:
        s.top_margin = s.bottom_margin = Inches(1.0)
        s.left_margin = s.right_margin = Inches(1.15)
    normal = doc.styles["Normal"]
    normal.font.name = "Georgia"
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(7)
    normal.paragraph_format.line_spacing = 1.22

    def runs(par, text, bold_all=False):
        for t, b, i, c, sup in inline_runs(text):
            r = par.add_run(t)
            r.bold = b or bold_all
            r.italic = i
            r.font.superscript = sup or None
            if c:
                r.font.name = "Consolas"
                r.font.size = Pt(9.5)
        return par

    if front.get("TITLE"):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(front["TITLE"])
        r.bold = True
        r.font.size = Pt(21)
        p.paragraph_format.space_after = Pt(4)
    if front.get("SUBTITLE"):
        p = doc.add_paragraph()
        r = p.add_run(front["SUBTITLE"])
        r.italic = True
        r.font.size = Pt(12)
        r.font.color.rgb = RGBColor(0x5D, 0x58, 0x50)
        p.paragraph_format.space_after = Pt(12)
    for k in ("AUTHOR", "DATE"):
        if front.get(k):
            p = doc.add_paragraph()
            runs(p, front[k])
            for r in p.runs:
                r.font.size = Pt(9.5)
                r.font.color.rgb = RGBColor(0x5D, 0x58, 0x50)
            p.paragraph_format.space_after = Pt(2)

    for kind, payload in blocks:
        if kind.startswith("h"):
            lvl = int(kind[1])
            p = doc.add_paragraph()
            r = p.add_run(payload.replace("**", ""))
            r.bold = True
            r.font.size = Pt({1: 16, 2: 13.5, 3: 11.5, 4: 10.5}[lvl])
            p.paragraph_format.space_before = Pt({1: 18, 2: 16, 3: 12, 4: 10}[lvl])
            p.paragraph_format.space_after = Pt(4)
        elif kind == "p":
            runs(doc.add_paragraph(), payload)
        elif kind == "quote":
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.32)
            p.paragraph_format.right_indent = Inches(0.18)
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(10)
            runs(p, payload)
        elif kind in ("li", "oli"):
            style = "List Bullet" if kind == "li" else "List Number"
            runs(doc.add_paragraph(style=style), payload)
        elif kind == "rule":
            p = doc.add_paragraph()
            runs(p, "———")
        elif kind == "table":
            rows = payload
            head = rows[0] if len(rows) > 1 and rows[1] == "SEP" else None
            body = rows[2:] if head else [r for r in rows if r != "SEP"]
            ncol = max(len(r) for r in ([head] if head else []) + body)
            t = doc.add_table(rows=0, cols=ncol)
            t.style = "Table Grid"
            if head:
                cells = t.add_row().cells
                for j in range(ncol):
                    cells[j].paragraphs[0].text = ""
                    runs(cells[j].paragraphs[0],
                         head[j] if j < len(head) else "", bold_all=True)
            for r in body:
                cells = t.add_row().cells
                for j in range(ncol):
                    cells[j].paragraphs[0].text = ""
                    runs(cells[j].paragraphs[0], r[j] if j < len(r) else "")
            doc.add_paragraph()
    doc.save(path)
    return path


FONT_DIRS = ("/usr/share/fonts/truetype/liberation",
             "/usr/share/fonts/truetype/dejavu")
FONT_FILES = (("Serif", ("LiberationSerif-Regular.ttf", "DejaVuSerif.ttf")),
              ("Serif-Bold", ("LiberationSerif-Bold.ttf", "DejaVuSerif-Bold.ttf")),
              ("Serif-Italic", ("LiberationSerif-Italic.ttf", "DejaVuSerif-Italic.ttf")),
              ("Serif-BoldItalic", ("LiberationSerif-BoldItalic.ttf",
                                    "DejaVuSerif-BoldItalic.ttf")),
              ("Mono", ("LiberationMono-Regular.ttf", "DejaVuSansMono.ttf")))
_FONTS_DONE = []


def _find_font(names):
    for d in FONT_DIRS:
        for n in names:
            p = os.path.join(d, n)
            if os.path.exists(p):
                return p
    return None


def _register_fonts(pdfmetrics, TTFont):
    """A full-Unicode serif. The built-in Times is Type1/WinAnsi and cannot set
    a superscript digit or a multiplication sign, both of which this paper uses
    in nearly every table."""
    if _FONTS_DONE:
        return
    from reportlab.pdfbase.pdfmetrics import registerFontFamily
    for name, cands in FONT_FILES:
        p = _find_font(cands)
        if p is None:
            raise SystemExit(f"render_paper: no font file for {name} in {FONT_DIRS}")
        pdfmetrics.registerFont(TTFont(name, p))
    registerFontFamily("Serif", normal="Serif", bold="Serif-Bold",
                       italic="Serif-Italic", boldItalic="Serif-BoldItalic")
    _FONTS_DONE.append(True)


def emit_pdf(front, blocks, path):
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate,
                                    Paragraph, Spacer, Table, TableStyle,
                                    HRFlowable)

    _register_fonts(pdfmetrics, TTFont)

    INK = colors.HexColor("#15140f")
    MUT = colors.HexColor("#5d5850")
    RULE = colors.HexColor("#d8d2c6")
    ACC = colors.HexColor("#7a2e12")
    HEAD = colors.HexColor("#efeade")

    def st(name, size, lead, **kw):
        return ParagraphStyle(name, fontName=kw.pop("font", "Serif"),
                              fontSize=size, leading=lead, textColor=kw.pop("colour", INK),
                              alignment=TA_LEFT, **kw)

    S = {
        "title": st("title", 20, 23.5, font="Serif-Bold", spaceAfter=3),
        "sub": st("sub", 11.5, 15, font="Serif-Italic", colour=MUT, spaceAfter=10),
        "by": st("by", 9, 12, colour=MUT, spaceAfter=1),
        "h1": st("h1", 15, 19, font="Serif-Bold", spaceBefore=17, spaceAfter=5),
        "h2": st("h2", 12.5, 16, font="Serif-Bold", spaceBefore=14, spaceAfter=4),
        "h3": st("h3", 10.8, 14, font="Serif-Bold", spaceBefore=11, spaceAfter=3),
        "h4": st("h4", 9.6, 13, font="Serif-Bold", colour=MUT, spaceBefore=9, spaceAfter=3),
        "p": st("p", 9.9, 14.2, spaceAfter=6),
        "quote": st("quote", 9.9, 14.2, leftIndent=10, rightIndent=6,
                    borderPadding=6, spaceBefore=5, spaceAfter=8,
                    backColor=colors.HexColor("#f3efe6")),
        "li": st("li", 9.9, 14.2, leftIndent=13, bulletIndent=3, spaceAfter=2),
        "cell": st("cell", 8.7, 11.6, spaceAfter=0),
        "cellh": st("cellh", 8.7, 11.6, font="Serif-Bold", spaceAfter=0),
    }

    def rl(text):
        """Inline runs to reportlab markup, escaped."""
        out = []
        for t, b, i, c, sup in inline_runs(text):
            e = (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
            if sup:
                e = f"<super>{e}</super>"
            if c:
                e = f'<font face="Mono" size="8.6">{e}</font>'
            if b:
                e = f"<b>{e}</b>"
            if i:
                e = f"<i>{e}</i>"
            out.append(e)
        return "".join(out)

    running = front.get("RUNNING", front.get("TITLE", ""))

    def page(canv, doc_):
        canv.saveState()
        canv.setFont("Serif", 7.6)
        canv.setFillColor(MUT)
        if doc_.page > 1:
            canv.drawString(24 * mm, A4[1] - 13 * mm, running)
        canv.drawRightString(A4[0] - 24 * mm, 12 * mm, str(doc_.page))
        canv.restoreState()

    doc = BaseDocTemplate(path, pagesize=A4,
                          leftMargin=24 * mm, rightMargin=24 * mm,
                          topMargin=20 * mm, bottomMargin=18 * mm,
                          title=front.get("TITLE", ""), author=front.get("AUTHOR", ""))
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=page)])

    flow = []
    if front.get("TITLE"):
        flow.append(Paragraph(rl(front["TITLE"]), S["title"]))
    if front.get("SUBTITLE"):
        flow.append(Paragraph(rl(front["SUBTITLE"]), S["sub"]))
    for k in ("AUTHOR", "DATE"):
        if front.get(k):
            flow.append(Paragraph(rl(front[k]), S["by"]))
    flow.append(Spacer(1, 8))

    avail = doc.width
    for kind, payload in blocks:
        if kind.startswith("h"):
            flow.append(Paragraph(rl(payload), S[kind]))
        elif kind == "p":
            flow.append(Paragraph(rl(payload), S["p"]))
        elif kind == "quote":
            flow.append(Paragraph(rl(payload), S["quote"]))
        elif kind == "li":
            flow.append(Paragraph(rl(payload), S["li"], bulletText="•"))
        elif kind == "oli":
            flow.append(Paragraph(rl(payload), S["li"], bulletText="–"))
        elif kind == "rule":
            flow.append(Spacer(1, 5))
            flow.append(HRFlowable(width="100%", color=RULE, thickness=0.6))
            flow.append(Spacer(1, 7))
        elif kind == "table":
            rows = payload
            head = rows[0] if len(rows) > 1 and rows[1] == "SEP" else None
            body = rows[2:] if head else [r for r in rows if r != "SEP"]
            ncol = max(len(r) for r in ([head] if head else []) + body)
            data = []
            if head:
                data.append([Paragraph(rl(head[j] if j < len(head) else ""), S["cellh"])
                             for j in range(ncol)])
            for r in body:
                data.append([Paragraph(rl(r[j] if j < len(r) else ""), S["cell"])
                             for j in range(ncol)])
            # first column carries the label and gets the room
            if ncol == 1:
                widths = [avail]
            else:
                rest = min(24 * mm, (avail * 0.62) / (ncol - 1))
                widths = [avail - rest * (ncol - 1)] + [rest] * (ncol - 1)
            t = Table(data, colWidths=widths, repeatRows=1 if head else 0, hAlign="LEFT")
            style = [("GRID", (0, 0), (-1, -1), 0.4, RULE),
                     ("VALIGN", (0, 0), (-1, -1), "TOP"),
                     ("TOPPADDING", (0, 0), (-1, -1), 3),
                     ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                     ("LEFTPADDING", (0, 0), (-1, -1), 5),
                     ("RIGHTPADDING", (0, 0), (-1, -1), 5)]
            if head:
                style.append(("BACKGROUND", (0, 0), (-1, 0), HEAD))
            t.setStyle(TableStyle(style))
            flow += [Spacer(1, 5), t, Spacer(1, 8)]
    doc.build(flow)
    return path


# ---- driver ----------------------------------------------------------------
def build(src_path, outdir=None, want=("md", "html", "docx", "pdf"), quiet=False):
    claims = load_claims()
    with open(src_path, encoding="utf-8") as fh:
        src = fh.read()
    seen = {}
    text, missing = resolve(src, claims, seen=seen)
    if missing:
        print("render_paper: UNRESOLVED CITATIONS -- nothing written", file=sys.stderr)
        for m in sorted(set(missing)):
            print("   " + m, file=sys.stderr)
        return None, 1
    front, blocks = parse(text)
    base = os.path.splitext(os.path.basename(src_path))[0].replace(".src", "")
    outdir = outdir or os.path.join(ROOT, "papers", "out")
    os.makedirs(outdir, exist_ok=True)
    made = []
    if "md" in want:
        p = os.path.join(outdir, base + ".md")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(emit_md(front, blocks))
        made.append(p)
    if "html" in want:
        p = os.path.join(outdir, base + ".html")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(emit_html(front, blocks))
        made.append(p)
    if "docx" in want:
        made.append(emit_docx(front, blocks, os.path.join(outdir, base + ".docx")))
    if "pdf" in want:
        made.append(emit_pdf(front, blocks, os.path.join(outdir, base + ".pdf")))
    if not quiet:
        n_words = sum(len(p.split()) for k, p in blocks if k in ("p", "quote", "li", "oli"))
        print(f"  source     {os.path.relpath(src_path, ROOT)}")
        print(f"  citations  {sum(seen.values())} sites over {len(seen)} distinct claims")
        print(f"  blocks     {len(blocks)}   words {n_words}")
        for p in made:
            print(f"  wrote      {os.path.relpath(p, ROOT)}  "
                  f"{os.path.getsize(p):,} B")
    return {"front": front, "blocks": blocks, "seen": seen, "made": made,
            "text": text}, 0


def selftest():
    """Fixtures are the ledger's own rows and the failure modes that matter."""
    fail = 0

    def check(label, got, want):
        nonlocal fail
        ok = got == want
        fail += 0 if ok else 1
        print(f"  {label:<58} {'PASS' if ok else 'FAIL'}")
        if not ok:
            print(f"      got {got!r} want {want!r}")

    claims = load_claims()
    check("the ledger loads and is not empty", len(claims) > 700, True)
    check("a plain citation resolves to value and unit",
          resolve("[[C01]]", claims)[0], "17.59 MeV")
    check("scientific notation renders as a power of ten",
          resolve("[[C02]]", claims)[0], "4.665 × 10^5 s^-1")
    check("a silent unit is dropped from the plain form",
          resolve("[[C784]]", claims)[0], "0.854")
    check("and is still reachable through the unit form",
          resolve("[[C784~]]", claims)[0], "ratio")
    check("the claim text is reachable without the value",
          resolve("[[?C01]]", claims)[0], "d+t fusion energy release")

    print()
    print("  the failures this exists to make impossible")
    _, miss = resolve("[[C99999]]", claims)
    check("an unknown claim id is an error, not a silent pass", bool(miss), True)
    wd = [k for k, r in claims.items() if r["status"] == "WITHDRAWN"]
    if wd:
        _, miss = resolve(f"[[{wd[0]}]]", claims)
        check("a WITHDRAWN row cited plainly is refused", bool(miss), True)
        out, miss = resolve(f"[[{wd[0]}!]]", claims)
        check("and is admitted only with its status shown",
              (not miss) and out.endswith("[WITHDRAWN]"), True)

    print()
    print("  the inline model is shared by all four outputs")
    runs = inline_runs("a **10^14** b")
    check("a superscript is a run flag, never a Unicode glyph",
          [r for r in runs if r[4]] and [r for r in runs if r[4]][0][0], "14")
    check("no output can disagree with another about a value: one resolve()",
          resolve("[[C01]]", claims)[0] == render_citation(claims["C01"], None, False),
          True)

    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("source", nargs="?", help="the .src.md paper source")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--outdir")
    for f in ("md", "html", "docx", "pdf", "all"):
        ap.add_argument("--" + f, action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.source:
        ap.error("a source file is required")
    want = [f for f in ("md", "html", "docx", "pdf") if getattr(a, f)]
    if a.all or not want:
        want = ("md", "html", "docx", "pdf")
    _, rc = build(a.source, a.outdir, want)
    return rc


if __name__ == "__main__":
    sys.exit(main())
