#!/usr/bin/env python3
"""makepdf.py -- typeset DRAFT-3-THE-LOWDIN-SOLUTION.md as a formatted PDF."""
import re, os, glob
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib.colors import HexColor
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, PageBreak, Image, Preformatted, HRFlowable,
                                KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import matplotlib

FD = os.path.join(os.path.dirname(matplotlib.__file__), 'mpl-data', 'fonts', 'ttf')
pdfmetrics.registerFont(TTFont('Serif', os.path.join(FD, 'DejaVuSerif.ttf')))
pdfmetrics.registerFont(TTFont('SerifB', os.path.join(FD, 'DejaVuSerif-Bold.ttf')))
pdfmetrics.registerFont(TTFont('SerifI', os.path.join(FD, 'DejaVuSerif-Italic.ttf')))
pdfmetrics.registerFont(TTFont('SerifBI', os.path.join(FD, 'DejaVuSerif-BoldItalic.ttf')))
pdfmetrics.registerFont(TTFont('Sans', os.path.join(FD, 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('SansB', os.path.join(FD, 'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFont(TTFont('Mono', os.path.join(FD, 'DejaVuSansMono.ttf')))
pdfmetrics.registerFontFamily('Serif', normal='Serif', bold='SerifB',
                              italic='SerifI', boldItalic='SerifBI')

INK = HexColor('#1a1a1a'); ACC = HexColor('#8a1f11'); GREY = HexColor('#555555')
body = ParagraphStyle('body', fontName='Serif', fontSize=10.3, leading=15.2,
                      alignment=TA_JUSTIFY, textColor=INK, spaceAfter=7)
law = ParagraphStyle('law', parent=body, leftIndent=16, rightIndent=16,
                     fontName='SerifI', spaceBefore=3, spaceAfter=7)
h1 = ParagraphStyle('h1', fontName='SansB', fontSize=13.5, leading=17,
                    textColor=ACC, spaceBefore=20, spaceAfter=8)
h2 = ParagraphStyle('h2', fontName='SansB', fontSize=11, leading=14,
                    textColor=INK, spaceBefore=12, spaceAfter=5)
cap = ParagraphStyle('cap', fontName='Sans', fontSize=8.5, leading=11.5,
                     alignment=TA_CENTER, textColor=GREY, spaceBefore=4, spaceAfter=14)
refp = ParagraphStyle('ref', parent=body, fontSize=9.2, leading=13,
                      leftIndent=14, firstLineIndent=-14, spaceAfter=3,
                      alignment=TA_LEFT)
code = ParagraphStyle('code', fontName='Mono', fontSize=8.6, leading=12,
                      leftIndent=18, textColor=INK, backColor=HexColor('#f4f2ee'),
                      borderPadding=8, spaceBefore=6, spaceAfter=10)

def esc(t):
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', t)
    t = re.sub(r'`(.+?)`', r'<font face="Mono" size="9">\1</font>', t)
    t = t.replace('V^{N−1}', 'V<super rise="3" size="7">N−1</super>')
    t = t.replace('Σ⁽²⁾', 'Σ<super rise="3" size="7">(2)</super>')
    return t

FIGS = {  # insert AFTER the heading whose text contains the key
    'THE RESULTS I': [('FIG1-filling-index-2-120.png',
        'Figure 1 — The Filling Index, Z = 2–120. The derived Aufbau staircase; exceptions ringed; predictions as open markers.'),
        ('FIG2-spectra-index-2-120.png',
        'Figure 2 — The Spectra Index, Z = 2–120. Candidate-channel depths; the entrant sawtooth and its margin band; the pinned g channels.')],
    'CORRELATION CLOSES': [('FIG4-dm2-widening.png',
        'Figure 4 — The Correlation Clause. Second-order correlation over mean-field margin at the five contested elements: all positive.')],
    'RELATIVISTIC TABLE': [('FIG3-j120-window.png',
        'Figure 3 — The Predictions, Z = 109–120. Twelve unfitted rows, margins, and the spin-orbit worst-case band.'),
        ('FIG6-relativistic-vs-nonrelativistic.png',
        'Figure 6 — The Table Without Relativity. The derived filling index at c = 137.035999 and at c → ∞: the eleven misplaced elements, boxed.')],
    'THE FIGURES': [('FIG5-spectra-index-3D.png',
        'Figure 5 — The Spectra Index in three dimensions: the candidate sheet with the entrant path threading it.')],
}
OUT = '/mnt/user-data/outputs'

def fig_flow(fname, caption, maxw=6.7 * inch):
    from PIL import Image as PImage
    p = os.path.join(OUT, fname)
    w, h = PImage.open(p).size
    iw = maxw; ih = h * maxw / w
    return KeepTogether([Spacer(1, 6), Image(p, iw, ih), Paragraph(caption, cap)])

src = open(os.path.join(OUT, 'DRAFT-3-THE-LOWDIN-SOLUTION.md')).read()
lines = src.split('\n')
story = []
# ---- title page ----
story.append(Spacer(1, 1.5 * inch))
story.append(Paragraph('THE LÖWDIN SOLUTION', ParagraphStyle('T', fontName='SansB',
             fontSize=26, leading=31, alignment=TA_CENTER, textColor=INK)))
story.append(Spacer(1, 14))
story.append(Paragraph('Deriving the Structure of the Periodic Table from the '
             'Many-Electron Schrödinger Equation', ParagraphStyle('ST',
             fontName='Serif', fontSize=13.5, leading=19, alignment=TA_CENTER,
             textColor=INK)))
story.append(Spacer(1, 8))
story.append(Paragraph('A Formal Response to the 1969 Löwdin Challenge',
             ParagraphStyle('ST2', fontName='SerifI', fontSize=11.5, leading=16,
             alignment=TA_CENTER, textColor=GREY)))
story.append(Spacer(1, 40))
story.append(HRFlowable(width='40%', thickness=0.7, color=ACC, hAlign='CENTER'))
story.append(Spacer(1, 18))
story.append(Paragraph('Matthew Lach', ParagraphStyle('A', fontName='SansB',
             fontSize=13, alignment=TA_CENTER, textColor=INK)))
story.append(Paragraph('Independent Researcher', ParagraphStyle('A2', fontName='Sans',
             fontSize=10, alignment=TA_CENTER, textColor=GREY, spaceBefore=4)))
story.append(Spacer(1, 60))
story.append(Paragraph('c = 137.035999 — the only entered number',
             ParagraphStyle('E', fontName='SerifI', fontSize=10, alignment=TA_CENTER,
             textColor=GREY)))
story.append(Spacer(1, 24))
story.append(Paragraph('DRAFT 3 — for review', ParagraphStyle('D', fontName='Sans',
             fontSize=8.5, alignment=TA_CENTER, textColor=GREY)))
story.append(PageBreak())

i = 0; in_code = False; codebuf = []; started = False; in_refs = False
while i < len(lines):
    ln = lines[i]; i += 1
    if not started:
        if ln.startswith('## ABSTRACT'):
            started = True
            story.append(Paragraph('ABSTRACT', h1))
        continue
    if ln.strip().startswith('```'):
        if in_code:
            story.append(Preformatted('\n'.join(codebuf), code))
            codebuf = []; in_code = False
        else:
            in_code = True
        continue
    if in_code:
        codebuf.append(ln); continue
    s = ln.strip()
    if s == '---':
        continue
    if s.startswith('### '):
        story.append(Paragraph(esc(s[4:]), h2)); continue
    if s.startswith('## '):
        txt = s[3:]
        story.append(Paragraph(esc(txt), h1))
        if 'REFERENCES' in txt: in_refs = True
        for key, figs in FIGS.items():
            if key in txt:
                for f, c in figs:
                    story.append(fig_flow(f, c))
        continue
    if not s:
        continue
    if s.startswith('*DRAFT'):
        story.append(Spacer(1, 16))
        story.append(HRFlowable(width='30%', thickness=0.6, color=GREY, hAlign='CENTER'))
        story.append(Spacer(1, 8))
        story.append(Paragraph(esc(s.strip('*')), ParagraphStyle('end',
                     fontName='SerifI', fontSize=9, alignment=TA_CENTER,
                     textColor=GREY)))
        continue
    if s.startswith('- '):
        story.append(Paragraph('•&nbsp;&nbsp;' + esc(s[2:]),
                     ParagraphStyle('li', parent=body, leftIndent=16,
                                    firstLineIndent=-10, spaceAfter=4)))
        continue
    if re.match(r'^\d+\. ', s) and in_refs:
        story.append(Paragraph(esc(s), refp)); continue
    st = law if (s.startswith('*(') or s.startswith('*Let ') or
                 s.startswith('**THE ORDERING LAW')) else body
    story.append(Paragraph(esc(s), st))

def deco(canv, doc):
    canv.saveState()
    if doc.page > 1:
        canv.setFont('Sans', 7.5); canv.setFillColor(GREY)
        canv.drawString(0.9 * inch, 10.55 * inch, 'THE LÖWDIN SOLUTION — M. LACH')
        canv.drawRightString(7.6 * inch, 10.55 * inch, 'DRAFT 3')
        canv.setStrokeColor(HexColor('#cccccc')); canv.setLineWidth(0.4)
        canv.line(0.9 * inch, 10.47 * inch, 7.6 * inch, 10.47 * inch)
        canv.setFont('Sans', 8)
        canv.drawCentredString(4.25 * inch, 0.55 * inch, str(doc.page))
    canv.restoreState()

doc = BaseDocTemplate(os.path.join(OUT, 'THE-LOWDIN-SOLUTION-DRAFT3.pdf'),
                      pagesize=letter,
                      leftMargin=0.9 * inch, rightMargin=0.9 * inch,
                      topMargin=0.85 * inch, bottomMargin=0.85 * inch,
                      title='The Löwdin Solution', author='Matthew Lach')
fr = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='f')
doc.addPageTemplates([PageTemplate(id='p', frames=[fr], onPage=deco)])
doc.build(story)
print('PDF written')
