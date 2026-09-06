import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Image, Table, TableStyle, PageBreak,
                                KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FD = "/usr/local/lib/python3.12/dist-packages/matplotlib/mpl-data/fonts/ttf"
pdfmetrics.registerFont(TTFont("DJ", f"{FD}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DJ-B", f"{FD}/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DJ-I", f"{FD}/DejaVuSans-Oblique.ttf"))
pdfmetrics.registerFont(TTFont("DJM", f"{FD}/DejaVuSansMono.ttf"))
pdfmetrics.registerFont(TTFont("DJS", f"{FD}/DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("DJS-B", f"{FD}/DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFontFamily("DJ", normal="DJ", bold="DJ-B", italic="DJ-I")

INK = colors.HexColor("#1a1a1a")
ACC = colors.HexColor("#8c2d19")
ACC2 = colors.HexColor("#2f5d7c")
MUT = colors.HexColor("#6b6b6b")
RULE = colors.HexColor("#c9c9c9")

S = {}
S['title'] = ParagraphStyle('title', fontName="DJS-B", fontSize=19, leading=23,
                            textColor=INK, spaceAfter=4)
S['sub'] = ParagraphStyle('sub', fontName="DJS", fontSize=12.5, leading=16,
                          textColor=ACC2, spaceAfter=14)
S['h1'] = ParagraphStyle('h1', fontName="DJS-B", fontSize=13.5, leading=17,
                         textColor=INK, spaceBefore=16, spaceAfter=7)
S['part'] = ParagraphStyle('part', fontName="DJS-B", fontSize=15, leading=19,
                           textColor=ACC, spaceBefore=20, spaceAfter=10)
S['h2'] = ParagraphStyle('h2', fontName="DJ-B", fontSize=10.5, leading=14,
                         textColor=INK, spaceBefore=11, spaceAfter=4)
S['h3'] = ParagraphStyle('h3', fontName="DJ-B", fontSize=9.5, leading=13,
                         textColor=ACC2, spaceBefore=8, spaceAfter=3)
S['body'] = ParagraphStyle('body', fontName="DJ", fontSize=9.1, leading=13.4,
                           textColor=INK, alignment=TA_JUSTIFY, spaceAfter=6)
S['abs'] = ParagraphStyle('abs', fontName="DJ", fontSize=8.9, leading=13,
                          textColor=INK, alignment=TA_JUSTIFY, spaceAfter=6,
                          leftIndent=10, rightIndent=10)
S['thm'] = ParagraphStyle('thm', fontName="DJ", fontSize=9.1, leading=13.4,
                          textColor=INK, alignment=TA_JUSTIFY, spaceAfter=6,
                          leftIndent=12, rightIndent=12, borderColor=ACC2,
                          borderWidth=0, backColor=colors.HexColor("#f2f6f9"),
                          borderPadding=7, spaceBefore=6)
S['note'] = ParagraphStyle('note', fontName="DJ-I", fontSize=8.5, leading=12.2,
                           textColor=MUT, alignment=TA_JUSTIFY, spaceAfter=6,
                           leftIndent=12, rightIndent=12)
S['cap'] = ParagraphStyle('cap', fontName="DJ", fontSize=8, leading=11,
                          textColor=MUT, alignment=TA_LEFT, spaceBefore=3,
                          spaceAfter=10)
S['mono'] = ParagraphStyle('mono', fontName="DJM", fontSize=7.8, leading=11,
                           textColor=INK, leftIndent=12, spaceAfter=6)
S['bul'] = ParagraphStyle('bul', fontName="DJ", fontSize=9.1, leading=13.2,
                          textColor=INK, alignment=TA_JUSTIFY, spaceAfter=3,
                          leftIndent=16, bulletIndent=5)


class Doc(BaseDocTemplate):
    def __init__(self, fn, **kw):
        BaseDocTemplate.__init__(self, fn, **kw)
        f = Frame(20 * mm, 18 * mm, self.width, self.height - 6 * mm, id='n')
        self.addPageTemplates([PageTemplate(id='p', frames=f, onPage=self.deco)])

    def deco(self, c, d):
        c.saveState()
        c.setFont("DJ", 7.2)
        c.setFillColor(MUT)
        if d.page > 1:
            c.drawString(20 * mm, A4[1] - 12 * mm,
                         "Indexing Without Prediction \u2014 Lach Elemental Lattice")
            c.setStrokeColor(RULE)
            c.setLineWidth(0.4)
            c.line(20 * mm, A4[1] - 14 * mm, A4[0] - 20 * mm, A4[1] - 14 * mm)
        c.drawCentredString(A4[0] / 2, 11 * mm, str(d.page))
        c.restoreState()


def P(t, s='body'):
    return Paragraph(t, S[s])


def tbl(data, widths, hdr=True, fs=8.0):
    t = Table(data, colWidths=widths, hAlign='LEFT')
    cmd = [('FONT', (0, 0), (-1, -1), "DJ", fs),
           ('TEXTCOLOR', (0, 0), (-1, -1), INK),
           ('VALIGN', (0, 0), (-1, -1), 'TOP'),
           ('TOPPADDING', (0, 0), (-1, -1), 3),
           ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
           ('LEFTPADDING', (0, 0), (-1, -1), 5),
           ('LINEBELOW', (0, 0), (-1, 0), 0.7, INK),
           ('LINEBELOW', (0, -1), (-1, -1), 0.5, RULE)]
    if hdr:
        cmd += [('FONT', (0, 0), (-1, 0), "DJ-B", fs),
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f4f4f4"))]
    t.setStyle(TableStyle(cmd))
    return t


def fig(n, cap, w=165 * mm):
    p = f"figs/fig{n:02d}.png"
    from PIL import Image as PIL
    iw, ih = PIL.open(p).size
    h = w * ih / iw
    mx = 118 * mm
    if h > mx:
        h = mx
        w = h * iw / ih
    return KeepTogether([Image(p, width=w, height=h), P(cap, 'cap')])


st = []
A = st.append

# ============================ FRONT MATTER ============================
A(P("Indexing Without Prediction", 'title'))
A(P("Maximality and Empirical Boundary of the Lach Elemental Lattice", 'sub'))
A(P("<b>Status.</b> Prepared for independent review. Every numerical claim is "
    "reproducible from the sources in Appendix C. Section 15.3 lists claims from "
    "earlier versions of this framework that are withdrawn. Readers checking this "
    "work are asked to attack Section 6.4 first; that is where the argument is "
    "thinnest and the authors know it.", 'note'))

A(P("Abstract", 'h1'))
A(P("We construct a lattice \u039b<sub>8</sub> over atomic electron configurations, "
    "prove that no quantity derived from its coordinates can raise its order "
    "dimension, and establish empirically that its order structure supplies no "
    "predictive information beyond the coordinates from which it is built.", 'abs'))
A(P("\u039b<sub>8</sub> is a closed distributive lattice of order dimension exactly "
    "eight, generated by an admissibility condition requiring every constraint to "
    "take the form <i>x</i> \u2264 \u03c6(<i>y</i>) with \u03c6 non-decreasing in a "
    "single coordinate and a constant floor. We prove that adjoining any function of "
    "the cell leaves the dimension unchanged, because the graph of a monotone "
    "function is order-isomorphic to its domain. The lattice is nonetheless "
    "extensible by <i>independent</i> physical quantities \u2014 the parent ion's "
    "angular momentum, the total angular momentum, the jK label, nuclear spin \u2014 "
    "each contributing exactly one dimension. \u039b<sub>11</sub> so constructed is "
    "injective on every test case assembled here.", 'abs'))
A(P("Against this we set a result of the opposite sign. A bracketing method for "
    "Rydberg binding energies, derived entirely from <i>T</i> = "
    "<i>Z</i><super>2</super><i>R</i>/\u03bd<super>2</super> and using none of the "
    "lattice's order structure, produces containment intervals holding in 295 of 295 "
    "interior cells across hydrogen, four alkaline earths, three alkali-like ions and "
    "a noble gas \u2014 spanning <i>Z</i><sub>eff</sub> = 1\u20133, \u2113 = 0\u20135, "
    "single-, two- and multi-limit systems, bound and autoionising. Its uncertainty "
    "estimate is derived rather than calibrated and returns \u00b11\u03c3 coverage of "
    "68.1%, 68.2% and 76.7% in the three limit regimes.", 'abs'))
A(P("Six independent attempts to extract predictive uplift from the lattice's order "
    "all failed, each by a distinct mechanism. We show these reduce to one theorem: "
    "on a product order, join, meet and comparability are definable from the "
    "coordinates, so lattice quantities restate the coordinates but cannot exceed "
    "them. The theorem is indifferent to dimension and to how faithfully the lattice "
    "represents the physics. Over the course of this work the index was improved to "
    "exactness; the predictive boundary did not move.", 'abs'))
A(P("The one construction that escapes the theorem is deductive containment, because "
    "a bracket is not a function of the coordinates but an entailment of the order "
    "relation given monotonicity. That is the sense in which an ordinal structure "
    "over configuration space is useful, and the only sense we have verified.", 'abs'))

# ============================ PART 0 ============================
A(P("Part 0 \u2014 Origin and Orientation", 'part'))
A(P("1. Introduction", 'h1'))
A(P("1.1 Where this began", 'h2'))
A(P("This framework began as a three-dimensional recoding of the periodic table. Each "
    "element was assigned a triple (<i>n</i>, \u2113, <i>k</i>): the principal quantum "
    "number of the subshell being filled, its orbital angular momentum, and the "
    "occupancy of that subshell. Under the componentwise partial order these triples "
    "form a lattice, and the periodic table becomes a path through it.", 'body'))
A(P("The recoding is exact and it is not new physics \u2014 it is a bijective "
    "relabelling of information already present in the Madelung filling order. Its "
    "interest was structural: periodicity appears as a projection of a "
    "three-dimensional object, and chemically analogous elements are close in the "
    "lattice for a structural reason rather than by convention.", 'body'))
A(P("Three additions produced the object studied here. Excited configurations require "
    "distinguishing the subshell an electron leaves from the one it enters, giving a "
    "second triple (<i>e</i>, <i>f</i>, <i>g</i>). Ionisation requires a count "
    "<i>q</i> of electrons removed. Spin multiplicity requires a coordinate <i>S</i>. "
    "The result is \u039b<sub>8</sub>, whose cells index electron configurations "
    "relative to a reference state.", 'body'))
A(P("The framework's earlier claims concerned prediction: that the lattice's order, "
    "closure and dimension would constrain atomic properties in ways the coordinates "
    "alone did not. This paper reports that those claims are false, establishes why in "
    "a form we believe is a theorem rather than a limitation of effort, and reports "
    "what survives.", 'body'))

A(P("1.2 What this paper claims", 'h2'))
A(P("<b>Structural (Part I).</b> \u039b<sub>8</sub> is closed under join and meet and "
    "has order dimension exactly eight. No derived quantity raises that dimension. It "
    "extends by one dimension per independent physical degree of freedom. As an index "
    "it achieves 86% coverage and, at eleven dimensions, injectivity on every test "
    "case. The physical subset is <i>not</i> a sublattice, and no choice of "
    "coordinates makes it one.", 'body'))
A(P("<b>Empirical (Part II).</b> A four-rule bracketing method, each rule derived from "
    "<i>T</i> = <i>Z</i><super>2</super><i>R</i>/\u03bd<super>2</super>, produces "
    "deductive containment verified on 295 interior cells with no exceptions, and an "
    "uncertainty estimate requiring no calibration. Its domain is bounded by four "
    "exclusions, each with an identified mechanism.", 'body'))
A(P("<b>Thesis (Part III).</b> The lattice's order contributes nothing to the method. "
    "Six tests establish this and a theorem about product orders explains why. The "
    "theorem does not depend on dimension or on faithfulness, so improving the index "
    "\u2014 which Part I does \u2014 leaves the predictive boundary where it was.",
    'body'))

A(P("1.3 What this paper does not claim", 'h2'))
A(P("We do not claim novel physics. Every quantitative result in Part II follows from "
    "the Rydberg formula and the quantum defect; the lattice's role is to make "
    "\u2018interior on some axis\u2019 and \u2018same channel\u2019 well defined. We "
    "do not claim the method extends beyond energies; Section 10 reports two attempts "
    "and both failed, for reasons we characterise.", 'body'))
A(P("An earlier line of this work concerned applications to condensed-matter nuclear "
    "phenomena. That material is removed entirely. It rested on extensions whose "
    "structural status we now know to be defective (Appendix A), and revisiting it "
    "requires first solving the multi-target representation problem.", 'body'))

# ============================ PART I ============================
A(PageBreak())
A(P("Part I \u2014 Structure", 'part'))
A(P("2. Construction", 'h1'))
A(P("2.1 The admissibility condition", 'h2'))
A(P("Let \u039b \u2286 \u2115<super>d</super> be defined by a family of constraints. "
    "The family is <b>admissible</b> \u2014 the condition previously designated "
    "\u00a79.4 \u2014 if every constraint has the form <i>x<sub>i</sub></i> \u2264 "
    "\u03c6(<i>x<sub>j</sub></i>) with \u03c6 non-decreasing, together with a constant "
    "floor <i>x<sub>i</sub></i> \u2265 <i>c</i>.", 'body'))
A(P("<b>Proposition 2.1.</b> <i>An admissible constraint family defines a set closed "
    "under componentwise join and meet.</i>", 'thm'))
A(P("<i>Proof.</i> Let <i>a</i>, <i>b</i> \u2208 \u039b. For the join, "
    "max(<i>a<sub>i</sub></i>, <i>b<sub>i</sub></i>) equals one of them, say "
    "<i>a<sub>i</sub></i>; then <i>a<sub>i</sub></i> \u2264 "
    "\u03c6(<i>a<sub>j</sub></i>) \u2264 \u03c6(max(<i>a<sub>j</sub></i>, "
    "<i>b<sub>j</sub></i>)) since \u03c6 is non-decreasing. For the meet, choose the "
    "index <i>m</i> minimising <i>x<sub>j</sub></i>; then min(<i>a<sub>i</sub></i>, "
    "<i>b<sub>i</sub></i>) \u2264 <i>m<sub>i</sub></i> \u2264 "
    "\u03c6(<i>m<sub>j</sub></i>) = \u03c6(min(<i>a<sub>j</sub></i>, "
    "<i>b<sub>j</sub></i>)). A constant floor is preserved trivially. \u220e", 'body'))
A(P("Two consequences shape everything following. A bound on a <b>sum</b> of two "
    "coordinates is not admissible and generally breaks closure \u2014 this defeats "
    "the multi-target extension of Appendix A. A <b>varying floor</b> is likewise "
    "inadmissible, which places the physical selection rules outside the language "
    "(Section 6.3).", 'body'))

A(P("2.2 The eight axes", 'h2'))
A(tbl([["axis", "meaning", "bound", "form"],
       ["n", "source shell", "1 \u2264 n \u2264 N", "free root"],
       ["\u2113", "source subshell", "\u2113 \u2264 n \u2212 1", "non-decr. in n"],
       ["k", "source occupancy", "1 \u2264 k \u2264 2(2\u2113+1)", "non-decr. in \u2113"],
       ["q", "electrons removed", "0 \u2264 q \u2264 k", "non-decr. in k"],
       ["e", "target shell", "1 \u2264 e \u2264 E", "free root"],
       ["f", "target subshell", "f \u2264 e \u2212 1", "non-decr. in e"],
       ["g", "electrons transferred", "g \u2264 min(q, 2(2f+1))", "min of two admissible"],
       ["2S", "spin multiplicity", "0 \u2264 2S \u2264 k", "non-decr. in k"]],
      [16 * mm, 40 * mm, 48 * mm, 44 * mm]))
A(Spacer(1, 7))
A(P("Derived quantities include net charge <i>c</i> = <i>q</i> \u2212 <i>g</i>, "
    "electron count <i>N</i>, and target occupancy <i>G</i>. <b>These are derived "
    "precisely because they cannot be coordinates</b>: each is a difference or sum of "
    "two axes, hence inadmissible. Section 4.3 makes this exact.", 'body'))

A(P("2.3 Closure and dimension", 'h2'))
A(P("Closure follows from Proposition 2.1 and was verified additionally on 8 \u00d7 "
    "10<super>6</super> sampled pairs at caps covering the observed data, with zero "
    "failures.", 'body'))
A(P("<b>Order dimension is exactly eight.</b> The upper bound is immediate. The lower "
    "bound follows from an explicit 8-box at (<i>n</i>, \u2113, <i>k</i>, <i>q</i>, "
    "<i>e</i>, <i>f</i>, <i>g</i>, 2<i>S</i>) = (3, 1, 2, 1, 2, 0, 0, 0), all "
    "2<super>8</super> = 256 corners of which are admissible. The box is "
    "<b>cap-independent</b>, remaining valid at cap settings (4,2,4,2), (6,3,8,3) and "
    "(8,4,12,4).", 'body'))
A(fig(1, "<b>Figure 1.</b> The admissibility constraint graph. Circles are axes; an "
         "arrow y \u2192 x indicates x is bounded by \u03c6(y). Two roots (n and e) "
         "make the graph a forest with a single cross-link at g."))
A(fig(2, "<b>Figure 2.</b> The 8-box projected onto four coordinate pairs. Every one "
         "of the 256 corners is admissible; labels give the number of corners mapping "
         "to each projected point."))

A(P("2.4 A note on cell counts", 'h2'))
A(P("Earlier versions reported |\u039b<sub>8</sub>| = 61,453 as a structural "
    "invariant. It is not. That is the cell count at one choice of caps, and it "
    "changes with them. Every quantity derived from it \u2014 the fraction of cells "
    "representing inward transitions, the fraction \u2018realisable\u2019 \u2014 is a "
    "truncation artefact and is withdrawn. The invariants of \u039b<sub>8</sub> are "
    "its closure, its order dimension and its behaviour under extension; its "
    "cardinality is not among them.", 'body'))

A(P("3. Algebra and geometry, axis by axis", 'h1'))
A(P("Each axis has an <i>algebra</i> \u2014 the bound defining it and its admissible "
    "form \u2014 and a <i>geometry</i> \u2014 the shape of the region it occupies. "
    "This section also reports where each is exercised, which varies enormously.",
    'body'))
for h, t in [
    ("3.1 n, the source shell",
     "Algebra: a free root; every electronic bound descends from it. Geometry: a "
     "chain. Exercised: distinguishes species but is <b>constant within any one "
     "atom</b>. Removing it from a single species' index costs zero collisions."),
    ("3.2 \u2113, the source subshell",
     "Algebra: \u2113 \u2264 n \u2212 1, non-decreasing in n. Geometry: a right "
     "triangle in the (n, \u2113) plane. Exercised: distinguishes species and blocks; "
     "constant within an atom."),
    ("3.3 k, the source occupancy",
     "Algebra: 1 \u2264 k \u2264 2(2\u2113+1). Geometry: a staircase widening with "
     "\u2113 \u2014 2, 6, 10, 14. Exercised: constant within an atom. k bounds q, 2S "
     "and the angular-momentum axes, so it is structurally central while empirically "
     "inert within a species."),
    ("3.4 q, electrons removed",
     "Algebra: 0 \u2264 q \u2264 k, a triangle nested inside k. Exercised: separates "
     "neutral from ionised species; constant (q = 1) across all singly-excited states "
     "of one atom."),
    ("3.5 e, the target shell",
     "Algebra: a second free root. <b>This is the workhorse.</b> Removing e from the "
     "Ca I index costs 13 collisions in 27 levels; from Kr I, 22 in 46. It is the axis "
     "the method of Part II interpolates along, and the only axis load-bearing both "
     "across and within species."),
    ("3.6 f, the target subshell",
     "Algebra: f \u2264 e \u2212 1, a second right triangle independent of the "
     "(n, \u2113) one. Geometry: \u039b<sub>8</sub> is therefore a product of two "
     "triangles, not a simplex \u2014 the clearest sense in which it is not a "
     "relabelled periodic table. Exercised: 7 collisions for Ca I, 22 for Kr I."),
    ("3.7 g, electrons transferred",
     "Algebra: g \u2264 min(q, 2(2f+1)) \u2014 the intersection of two triangles, a "
     "wedge, and the only axis bounded by two others. Exercised: <b>zero collisions on "
     "removal.</b> For singly-excited states g = q = 1 universally, so the axis is "
     "exercised only by doubly-excited configurations, of which the record holds few."),
    ("3.8 2S, spin",
     "Algebra: 0 \u2264 2S \u2264 k, a chain over k. Exercised: 5 collisions for Ca I. "
     "Load-bearing where LS coupling holds; <b>undefined</b> for jK-coupled systems "
     "such as Kr I, where the parent's J must substitute."),
]:
    A(P(h, 'h3'))
    A(P(t, 'body'))
A(P("3.9 The collective whole", 'h3'))
A(P("\u039b<sub>8</sub> is a product of two triangular regions \u2014 (n, \u2113) and "
    "(e, f) \u2014 with occupancy chains hung from each and a wedge (g) linking them. "
    "It is not a simplex, not a hypercube and not a chain product; two roots make the "
    "constraint graph a forest with a single cross-link.", 'body'))
A(fig(3, "<b>Figure 3.</b> The collective whole. Two triangular blocks, two chains "
         "descending from k, and one cross-link where g is bounded by both q and f."))
A(P("3.10 Axis ablation", 'h3'))
A(P("Removing each axis in turn from the index and counting collisions measures "
    "directly what each contributes.", 'body'))
A(tbl([["axis", "Ca I (27 levels)", "Kr I (46 levels)"],
       ["n, \u2113, k, q, g", "0", "0"],
       ["e", "13", "22"],
       ["f", "7", "22"],
       ["2S", "5", "undefined (jK)"],
       ["2J\u2091 (core)", "0 (fixed)", "20"],
       ["2J (total)", "12", "35"]],
      [42 * mm, 45 * mm, 45 * mm]))
A(Spacer(1, 7))
A(P("Six of ten coordinates are constant within a species and discriminate only "
    "<i>across</i> species. Only e and f appear in both roles \u2014 which is exactly "
    "why the method of Part II interpolates in e at fixed f and uses no other axis.",
    'body'))
A(fig(4, "<b>Figure 4.</b> Axis ablation for an LS-coupled species (Ca I) and a "
         "jK-coupled one (Kr I). Six of ten coordinates are inert within a species."))

A(P("4. What cannot be added, and what can", 'h1'))
A(P("4.1 The theorem", 'h2'))
A(P("<b>Theorem 4.1.</b> <i>Let L be a finite lattice and h : L \u2192 \u2124 a "
    "function whose graph G = {(x, h(x))} is closed under componentwise join and "
    "meet. Then h is monotone, G is order-isomorphic to L, and adjoining h leaves the "
    "order dimension unchanged.</i>", 'thm'))
A(P("<i>Proof.</i> Closure gives <i>h</i>(<i>x</i> \u2228 <i>y</i>) = "
    "max(<i>h</i>(<i>x</i>), <i>h</i>(<i>y</i>)). If <i>x</i> \u2264 <i>y</i> then "
    "<i>x</i> \u2228 <i>y</i> = <i>y</i>, so <i>h</i>(<i>y</i>) = "
    "max(<i>h</i>(<i>x</i>), <i>h</i>(<i>y</i>)) \u2265 <i>h</i>(<i>x</i>): "
    "<i>h</i> is monotone. The map <i>x</i> \u21a6 (<i>x</i>, <i>h</i>(<i>x</i>)) is a "
    "bijection onto <i>G</i>; monotonicity makes it order-preserving, and projection "
    "onto the first coordinate makes it order-reflecting. It is therefore an order "
    "isomorphism, and dim(<i>G</i>) = dim(<i>L</i>). \u220e", 'body'))
A(P("The theorem requires no admissibility hypothesis and no assumption that <i>L</i> "
    "is a product of chains. <b>Corollary:</b> no quantity computed from the eight "
    "electronic coordinates can raise \u039b<sub>8</sub>'s dimension. Verified: of 92 "
    "closure-preserving functions enumerated on a 28-cell test lattice, zero produce a "
    "4-box where the base has a 3-box.", 'body'))
A(P("<b>A stronger claim that is false.</b> An earlier version of this work asserted "
    "that any closure-preserving h must be a monotone function of a <i>single</i> "
    "coordinate. That holds for products of chains but not for \u039b, which is a "
    "sublattice of one: the constraint \u2113 \u2264 n \u2212 1 means \u039b is not "
    "interval-closed, since (1, 2) lies componentwise between (1, 0) and (3, 2) yet is "
    "not a cell. On the test lattice, 148 of 335 closure-preserving functions depend "
    "on more than one coordinate \u2014 for instance the one generated by the chain "
    "(1,0,2) \u2264 (3,0,2), which varies with both n and \u2113. Those functions are "
    "nonetheless redundant, not because they depend on one axis but because they add "
    "no dimension. Theorem 4.1 is the correct statement and it is what the argument "
    "requires.", 'body'))

A(P("4.2 Rejected candidates", 'h2'))
A(P("Each of the following was proposed as a ninth axis in earlier work; each fails, "
    "and the failure is now attributable to Theorem 4.1 rather than to case-by-case "
    "testing.", 'body'))
A(tbl([["candidate", "form", "join fail", "meet fail", "verdict"],
       ["h = n", "projection", "0", "0", "closed, no 9-box"],
       ["h = 2n", "monotone in n", "0", "0", "closed, redundant"],
       ["h = n + \u2113", "two coordinates", "42,492", "42,492", "breaks closure"],
       ["h = q \u2212 g  (net charge)", "difference", "284,858", "284,858", "breaks closure"],
       ["h = k \u2212 q", "difference", "406,400", "406,400", "breaks closure"],
       ["h = e \u2212 f", "difference", "266,440", "266,440", "breaks closure"],
       ["h = \u230aC/e\u00b2\u230b  (energy)", "anti-monotone", "503,404", "503,404", "breaks closure"]],
      [46 * mm, 30 * mm, 22 * mm, 22 * mm, 36 * mm], fs=7.6))
A(Spacer(1, 7))
A(P("The energy proxy deserves separate comment, being the original motivation for a "
    "ninth \u2018output\u2019 axis. It fails for a sharper reason than inadmissibility: "
    "energy <i>decreases</i> with e while the order increases, so an energy-valued "
    "coordinate is anti-monotone and pairs of cells acquire no upper bound at all. "
    "<b>A metric quantity increasing with the coordinates might well be admissible.</b> "
    "The obstruction is the sign, not the metricity \u2014 a correction to the earlier "
    "\u00a722.2 analysis.", 'body'))

A(P("5. Extension by independent quantities", 'h1'))
A(P("5.1 Three classes", 'h2'))
A(P("Theorem 4.1 constrains only functions of the existing coordinates. Physically "
    "independent quantities escape it, and fall into three classes.", 'body'))
A(P("<b>(a) Functions of the cell.</b> Graph order-isomorphic to \u039b; dimension "
    "unchanged. Always.", 'bul', ))
A(P("<b>(b) Independent, bounded by an existing coordinate.</b> Admissible iff the "
    "bound has \u00a79.4 form. Contributes exactly one dimension.", 'bul'))
A(P("<b>(c) Independent, bounded by a constant.</b> The set is a direct product; "
    "closure automatic; one dimension.", 'bul'))
A(P("5.2 \u039b\u2089, \u039b\u2081\u2080, \u039b\u2081\u2081", 'h2'))
A(P("<b>Parent-ion angular momentum (class b).</b> The same electronic cell can leave "
    "the residual ion in different J states, so J<sub>c</sub> is not a function of the "
    "eight. With 2J<sub>c</sub> \u2264 k \u2014 non-decreasing in a single coordinate "
    "\u2014 the enlarged set is <b>closed exactly</b>: 6,989 cells, all 24,419,566 "
    "pairs tested, zero failures, with a 9-box at (3,1,5,4,3,1,3,2,1). Order dimension "
    "9.", 'body'))
A(P("<b>Total angular momentum (class b).</b> With 2J \u2264 2k, closure holds on "
    "2,041,470 cells with zero failures and a 10-box at (3,1,2,1,2,0,0,0,0,0). Order "
    "dimension 10.", 'body'))
A(P("<b>jK label (class b)</b>, required for jK-coupled systems, and <b>nuclear spin "
    "(class c)</b>, bounded by a constant, follow the same pattern.", 'body'))
A(P("5.3 What extension buys and costs", 'h2'))
A(tbl([["lattice", "Kr I cells", "collisions", "Ca I fine structure"],
       ["\u039b\u2088", "7", "39", "1 collision"],
       ["\u039b\u2089", "11", "35", "1 collision"],
       ["\u039b\u2081\u2080", "34", "12", "resolved"],
       ["\u039b\u2081\u2081", "46", "0", "resolved"]],
      [28 * mm, 30 * mm, 30 * mm, 45 * mm]))
A(Spacer(1, 7))
A(P("The cost is looseness. Each class-(b) bound admits more than the physics permits: "
    "the true range for total J is the triangle rule |J<sub>c</sub> \u2212 j| \u2264 J "
    "\u2264 J<sub>c</sub> + j, whose <b>lower bound varies with the cell</b>, and "
    "\u00a79.4 permits only constant floors. On a bounded enumeration the physically "
    "realisable fraction is 23.3% at eight dimensions, 9.0% at nine, 1.7% at ten.",
    'body'))
A(fig(5, "<b>Figure 5.</b> Extension clears collisions (left axis) while admitting "
         "unphysical cells (right axis). The two curves crossing is the trade."))

A(P("6. The lattice as an index", 'h1'))
A(P("6.1 Coverage", 'h2'))
A(tbl([["species", "mapped", "coverage"],
       ["Kr I", "9 / 9", "100%"], ["Sc III", "8 / 8", "100%"],
       ["Ba II", "10 / 10", "100%"], ["Sr I", "9 / 10", "90%"],
       ["Ca I", "12 / 15", "80%"], ["Ti I", "6 / 11", "55%"],
       ["total", "54 / 63", "86%"]],
      [40 * mm, 32 * mm, 30 * mm]))
A(Spacer(1, 7))
A(P("Every failure is a <b>multi-subshell configuration</b> \u2014 two occupied "
    "non-source subshells, which a single (e, f, g) triple cannot name. Coverage is a "
    "representational limit and <b>no additional coordinate repairs it</b>; the "
    "natural repair, a second target triple, breaks the lattice (Appendix A).", 'body'))
A(P("6.2 Injectivity", 'h2'))
A(tbl([["collision type", "example", "resolved by", "at"],
       ["core J", "Kr I (\u00b2P\u00b0 3/2)5s vs (\u00b2P\u00b0 1/2)5s", "2J\u2091", "\u039b\u2089"],
       ["fine structure", "Ca I 4s4d \u00b3D with J = 1, 2, 3", "2J", "\u039b\u2081\u2080"],
       ["jK label", "Kr I 5p \u00b2[1/2] vs \u00b2[3/2], same J", "K", "\u039b\u2081\u2081"]],
      [30 * mm, 68 * mm, 26 * mm, 20 * mm], fs=7.8))
A(Spacer(1, 7))
A(P("The first is consequential beyond bookkeeping. The two Kr I channels converge on "
    "limits <b>5,370 cm<super>\u22121</super> apart</b>, and the method of Part II "
    "requires knowing which. <b>\u039b<sub>8</sub> cannot supply that assignment</b>; "
    "in the work reported here it was read from the ASD configuration string. "
    "\u039b<sub>9</sub> supplies it.", 'body'))
A(P("6.3 The physical set is not a sublattice", 'h2'))
A(P("The physically realisable cells satisfy the spin selection rules: 2S \u2261 k "
    "(mod 2) and 2S \u2264 min(k, 2(2\u2113+1) \u2212 k). <b>This set is not "
    "closed.</b> In the (k, 2S) plane, (1,1) and (2,0) are both physical; their join "
    "(2,1) is not, since 2S must be even when k is even. Failures: 1 at \u2113 = 0, 15 "
    "at \u2113 = 1, 70 at \u2113 = 2.", 'body'))
A(P("The obstruction is structural. A <b>congruence is not an inequality</b>, and "
    "\u00a79.4 admits only inequalities with constant floors. The selection rules of "
    "atomic physics \u2014 spin parity, hole symmetry, the triangle rule \u2014 are "
    "none of them of that form.", 'body'))
A(P("6.4 Offset coordinates: faithful but not closed", 'h2'))
A(P("<i>This section reports a negative result obtained late in the work and corrects "
    "an intermediate claim. It is the place a reviewer should attack first.</i>",
    'note'))
A(P("One may attempt to bring the selection rules inside the language by "
    "reparameterisation. Replace 2S by the paired-unit count m = (k \u2212 2S)/2, so "
    "2S = k \u2212 2m carries the parity of k automatically; replace 2J by the triangle "
    "offset t = (2J \u2212 |2J<sub>c</sub> \u2212 2j|)/2, so the triangle rule holds by "
    "construction. Each transformation is bijective, so the dimension is unchanged and "
    "Theorem 4.1 is untouched.", 'body'))
A(P("Tested <b>in isolation</b>, each works: the (k, m) plane is closed at every "
    "\u2113, and the (J<sub>c</sub>, j, t) block is closed with 140 cells and zero "
    "failures.", 'body'))
A(P("<b>Assembled into one lattice, they do not.</b> Exhaustive test on 1,431 cells "
    "and all 1,023,165 pairs: <b>222,075 join failures and 11,696 meet failures.</b> "
    "The cause is visible in the bounds \u2014 m has a floor varying with k, and "
    "2J<sub>c</sub> \u2264 k \u2212 q is decreasing in q. Isolated closure does not "
    "imply joint closure.", 'body'))
A(P("What the offset coordinates do achieve is worth recording: all 1,431 cells decode "
    "to genuine physical states, zero violations, and the encoding is injective \u2014 "
    "1,903 distinct states, no duplicates. <b>Offset coordinates are a faithful and "
    "injective parameterisation of the physical set that is not a lattice.</b>", 'body'))
A(P("The section's result is therefore: <b>one may have closure or faithfulness, not "
    "both.</b> The lattice properly contains the physics; the physics is not a "
    "sublattice; and no relabelling repairs this, because the obstruction is the "
    "varying floor and not the choice of origin.", 'body'))

# ============================ PART II ============================
A(PageBreak())
A(P("Part II \u2014 A Bracketing Method for Rydberg Energies", 'part'))
A(P("7. Derivation", 'h1'))
A(P("Every rule below follows from one expression: <i>T</i> = "
    "<i>Z</i><sub>eff</sub><super>2</super><i>R</i>/\u03bd<super>2</super>, with "
    "\u03bd = <i>n</i> \u2212 \u03b4(<i>n</i>, \u2113, core), where <i>T</i> is the "
    "binding energy relative to the series limit and \u03b4 the quantum defect. The "
    "method uses the lattice only to make two notions well defined: which cells belong "
    "to the same <b>channel</b>, and which cells are <b>interior</b> on an axis.",
    'body'))
A(P("8. The four rules", 'h1'))
A(P("<b>Rule 1 \u2014 Interiority.</b> Predict only cells with measured neighbours on "
    "both sides along some axis, and only cells belonging to the same Rydberg sequence "
    "as those neighbours.<br/><br/>"
    "<b>Rule 2 \u2014 Variable.</b> Read the interpolation variable off <i>T</i> = "
    "<i>Z</i><super>2</super><i>R</i>/\u03bd<super>2</super> for the axis in question: "
    "E along n within a series; interval ratios along J; geometric in T along the core "
    "shell.<br/><br/>"
    "<b>Rule 3 \u2014 Separation.</b> Report the deductive bracket separately from the "
    "inferential point estimate. Given monotonicity the true value cannot lie outside "
    "[max below, min above].<br/><br/>"
    "<b>Rule 4 \u2014 Uncertainty.</b> Fit \u03b4 locally by a Ritz expansion \u03b4 = "
    "\u03b4\u2080 + \u03b4\u2082/n<super>2</super> and take \u03c3 = 2R "
    "<i>Z</i><super>2</super> \u00b7 SE<sub>pred</sub>/\u03bd<super>3</super>.", 'thm'))
A(P("<b>Rule 1's second clause is not redundant.</b> Sc III 3d is interior in n within "
    "\u2113 = 2, yet including it inflates the median error by 3.2\u00d7 because it is "
    "the collapsed ground state rather than a sequence member. The operational test is "
    "that its defect departs from its neighbours' by 0.14 where they depart from each "
    "other by 0.008 \u2014 a factor of 17.", 'body'))
A(P("Each rule is justified by the cost of violating it:", 'body'))
A(tbl([["rule violated", "cost"],
       ["extrapolate rather than interpolate", "rms 248 \u2192 928 cm\u207b\u00b9 (3.7\u00d7), n = 91"],
       ["wrong interpolation variable", "rms 248 \u2192 589 cm\u207b\u00b9 (2.4\u00d7)"],
       ["pooled \u03c3 instead of per-cell", "\u00b11\u03c3 coverage 96.2% instead of 68%"],
       ["include collapsed orbital", "median error 12.8 \u2192 41.3 cm\u207b\u00b9 (3.2\u00d7)"]],
      [62 * mm, 80 * mm]))
A(Spacer(1, 7))

A(P("9. Verification", 'h1'))
A(P("<b>295 interior cells, bracket exact in every one.</b>", 'body'))
A(tbl([["regime", "cells", "bracket", "\u00b11\u03c3", "median error"],
       ["H I (Z\u2091 = 1)", "5", "5 / 5", "\u2014", "0.006 cm\u207b\u00b9"],
       ["Mg/Ca/Sr/Ba I, Ca/Sr/Ba II", "226", "226 / 226", "68.1%", "1.05"],
       ["Ca I 3d channel (autoionising)", "22", "22 / 22", "68.2%", "9.37"],
       ["Kr I (multi-limit p-block)", "30", "30 / 30", "76.7%", "3.54"],
       ["Sc III (Z\u2091 = 3)", "11", "11 / 11", "54.5%", "12.8"]],
      [58 * mm, 18 * mm, 24 * mm, 20 * mm, 30 * mm], fs=7.8))
A(Spacer(1, 7))
A(P("<b>On independence.</b> These 295 cells are drawn from approximately <b>22 "
    "channels</b>. Cells within a channel share neighbours, so successive brackets are "
    "correlated and 295 should not be read as 295 independent tests.", 'body'))
A(P("<b>On the bracket's robustness.</b> Perturbing the series limit by \u00b15 "
    "cm<super>\u22121</super> leaves coverage unchanged at 15/15, because the bracket "
    "uses only measured neighbours. The point estimate and \u03c3 require the limit; "
    "<b>the bracket does not</b>. Similarly, \u2018interior\u2019 requires that "
    "neighbours exist, not that they be adjacent: with n = 8\u201316 removed from a Ba "
    "I series, cell 17 still brackets correctly, at width 2,012 cm<super>\u22121</super> "
    "instead of 400.", 'body'))
A(P("<b>On the neighbour count.</b> The Ritz fit uses the k nearest members. "
    "Sensitivity: rms 14.0 / 17.1 / 15.8 / 15.5 / 15.5 cm<super>\u22121</super> for "
    "k = 3, 4, 6, 8, 10. No strong preference; k = 6 was chosen arbitrarily and the "
    "sensitivity is reported rather than the choice being presented as derived.",
    'body'))
A(fig(6, "<b>Figure 6.</b> Quantum-defect sequences across four species, two charge "
         "states and \u2113 = 2, 3. The smooth Ritz behaviour is what Rule 4 fits and "
         "what the bracket exploits."))
A(fig(7, "<b>Figure 7.</b> Derived \u03c3 against realised error on a representative "
         "subset. The calibration is not fitted \u2014 \u03c3 comes from the "
         "prediction standard error of the local Ritz fit.", w=118 * mm))
A(fig(8, "<b>Figure 8.</b> The bracket construction. One cell is withheld; the "
         "interval formed by its measured neighbours must contain it, given "
         "monotonicity in n."))

A(P("10. Domain and exclusions", 'h1'))
A(P("<b>Verified domain.</b> Binding energies of Rydberg series: one electron outside "
    "a core in a definite state, channel by channel, with the channel's limit supplied "
    "by the configuration label. Interior cells only, excluding collapsed orbitals.",
    'body'))
A(P("<b>(i) Sign-changing quantities.</b> Any property built from a matrix element "
    "passing through zero cannot be monotone. Sr I 5s\u00b2 \u00b9S\u2080 \u2192 "
    "5s<i>n</i>p \u00b9P\u2081 reduced transition probabilities collapse by a "
    "<b>factor of 60</b> at n = 6 and recover \u2014 a Cooper-type node. Bracket "
    "coverage across the node: 79%. Away from it: 100% on 11 cells.", 'body'))
A(P("<b>(ii) Asymptotically constant quantities.</b> Fine-structure splittings reduced "
    "by \u03bd<super>3</super> are constant to ~0.5% across a series, and the adjacent "
    "steps fall below measurement noise (1.6%). Bracket coverage: <b>35.3%</b>; zero "
    "of 17 adjacent steps are resolvable. A constant is not monotone.", 'body'))
A(P("<b>(iii) Systems without interior cells.</b> Ti I: 23 channels, 26 members, "
    "<b>zero interior cells</b>. No channel reaches three members, because the "
    "ionisation limit near 55,000 cm<super>\u22121</super> lies below the onset of "
    "severe level density, and above ~42,000 cm<super>\u22121</super> the levels are "
    "40\u201350% configuration-mixed with no assignable parent. The method declines "
    "rather than errs.", 'body'))
A(P("<b>(iv) Collapsed orbitals</b>, excluded by the defect-departure test of Rule 1.",
    'body'))
A(fig(9, "<b>Figure 9.</b> The three exclusion mechanisms, each measured: a sign "
         "change in the matrix element; a quantity too flat to bracket; a system whose "
         "series are too short to contain an interior cell."))
A(fig(10, "<b>Figure 10.</b> The verified domain. Cell counts by effective charge and "
          "orbital angular momentum; the excluded region is marked with its mechanism."))

A(P("11. Predictions", 'h1'))
A(P("11.1 Verified", 'h2'))
A(P("<b>Kr II \u00b2P\u00b0<sub>1/2</sub> fine-structure splitting.</b> Derived from "
    "three \u2113 channels of the Kr I (\u00b2P\u00b0<sub>1/2</sub>) series and "
    "committed <i>before</i> the measurement entered the analysis: <b>5,591 \u00b1 500 "
    "cm<super>\u22121</super></b>. Measured: <b>5,370.10 cm<super>\u22121</super></b>. "
    "Error +221 cm<super>\u22121</super>, 4.1%, within the stated interval.", 'body'))
A(P("<i>Full disclosure on the interval.</i> The three channel estimates were 6,061, "
    "5,679 and 5,031, giving sd = 521. The quoted \u00b1500 is therefore approximately "
    "1\u03c3, not the conventional 2\u03c3 (which would be \u00b11,030). The measured "
    "value lies 0.4\u03c3 from the mean. The prediction is correct; the interval was "
    "tighter than convention and this should have been stated at the time.", 'note'))
A(P("11.2 Open", 'h2'))
A(P("<b>Ba I 5d\u00b2 \u00b9G\u2084.</b> Deductive bracket from the term ordering "
    "\u00b3F &lt; \u00b9D &lt; \u00b3P &lt; \u00b9G &lt; \u00b9S: <b>[23,694, 26,757] "
    "cm<super>\u22121</super></b>. No point estimate is offered; see \u00a715.3.",
    'body'))
A(tbl([["Ba I level", "bracket (cm\u207b\u00b9)", "Ritz estimate"],
       ["6s8f", "[39,678, 40,614]", "40,238"],
       ["6s13f", "[41,251, 41,648]", "41,367"],
       ["6s14f", "[41,251, 41,648]", "41,461"],
       ["6s15f", "[41,251, 41,648]", "41,536"],
       ["6s16f", "[41,251, 41,648]", "41,597"]],
      [34 * mm, 46 * mm, 34 * mm]))
A(Spacer(1, 6))
A(P("Leave-one-out validation on the same series: 15/15 bracket coverage, rms 20.5 "
    "cm<super>\u22121</super>, with sub-wavenumber accuracy for n \u2265 17.", 'body'))
A(P("<b>Ti II a\u2074F intervals</b>, derived from the Ti I 4f and 5g manifolds "
    "resolved by core J, which agree to 0.7 cm<super>\u22121</super>: <b>94.3, 131.9, "
    "167.3 cm<super>\u22121</super></b> for J = 3/2 \u2192 5/2 \u2192 7/2 \u2192 9/2. "
    "Corresponding limits: 55,044.3 / 55,138.5 / 55,270.0 / 55,437.4 "
    "cm<super>\u22121</super>. Internal check: taking \u03b4(5g) = 0 gives \u03b4(4f) = "
    "0.0508, 0.0508, 0.0506, 0.0506 across four independent channels.", 'body'))

# ============================ PART III ============================
A(PageBreak())
A(P("Part III \u2014 Indexing Without Prediction", 'part'))
A(P("12. The theorem", 'h1'))
A(P("<b>Theorem 12.1.</b> <i>On a product order, join, meet and comparability are "
    "definable from the coordinates.</i> Explicitly (a \u2228 b)<sub>i</sub> = "
    "max(a<sub>i</sub>, b<sub>i</sub>), (a \u2227 b)<sub>i</sub> = min(a<sub>i</sub>, "
    "b<sub>i</sub>), and a \u2264 b iff a<sub>i</sub> \u2264 b<sub>i</sub> for all i.",
    'thm'))
A(P("Every lattice-theoretic quantity is therefore a function of the coordinates, and "
    "can restate them but cannot exceed them. Two properties of this theorem drive "
    "Part III. It is <b>indifferent to dimension</b>: \u039b<sub>11</sub> is as "
    "constrained as \u039b<sub>8</sub>. And it is <b>indifferent to faithfulness</b>: "
    "perfecting the index moves nothing.", 'body'))

A(P("13. Six mechanisms", 'h1'))
for h, t in [
    ("13.1 Rank aggregation",
     "Using rank(a \u2227 b) and rank(a \u2228 b) as predictors of configuration "
     "mixing: leave-one-out rmse 1.643 against 0.812 for a linear model in \u0394q, "
     "\u0394f \u2014 worse than predicting the mean (data sd 0.940). <i>Mechanism:</i> "
     "rank is a <b>sum over axes</b>, and summing discards which axis moved. Mixing "
     "depends on which subshell is involved; rank cannot see it. This holds at any "
     "faithfulness."),
    ("13.2 Comparability",
     "Comparable cells order energies correctly in 65 of 65 Ca I pairs, and select a "
     "52.1% subset with 100% accuracy using no training data. <i>Mechanism:</i> energy "
     "is separately monotone in every coordinate \u2014 49 single-coordinate pairs, "
     "zero violations \u2014 so a \u2264 b implies E(a) \u2264 E(b) is a <b>theorem "
     "given monotonicity</b>, not an empirical finding. Monotonicity is a coordinate "
     "property that a positive-weight linear model encodes directly, which is why the "
     "control reached 99.9%."),
    ("13.3 Zero-shot subset selection",
     "The lattice selects a reliable subset with no labels; a fitted linear model needs "
     "40 labels to approach it. <i>Mechanism:</i> a <b>naive positive-weight sum</b>, "
     "all weights +1 and no fitting, matches it exactly \u2014 100% at identical "
     "coverage, zero labels. The prior is identical in both cases."),
    ("13.4 Closure as existence",
     "Observed configurations are closed under meet more than chance allows \u2014 Mg I "
     "p = 0.006, Ca I 0.031, Sr I and Ba I &lt; 0.0001 against a marginal-matched null. "
     "<i>Mechanism:</i> spectroscopists measure <b>downward-closed regions</b>. Every "
     "Rydberg series is followed from its lowest member upward, so the observed set is "
     "a lower set by construction. The join/meet asymmetry that motivated the test "
     "appears only in sparse data and vanishes in dense."),
    ("13.5 Join-based configuration mixing",
     "For divalent atoms roughly 62% of pairs have <b>no upper bound at all</b>, at "
     "every valence count tested (k = 2, 3, 4). <i>Mechanism:</i> joining two "
     "doubly-excited configurations requires transferring the union of their target "
     "electrons, but q \u2264 k. The join is not ambiguous; it does not exist. Raising "
     "k does not help, adding admissible states as fast as it adds joins."),
    ("13.6 A derived ordinal coordinate",
     "Collapsing four verified monotonicities into \u03ba = (q, n<sub>core</sub>, "
     "\u2212n, \u2212\u2113) gives 2163/2163 monotone, 31.2% of pairs comparable, and "
     "containment across species and charge simultaneously. <i>Mechanism:</i> every "
     "component is a coordinate; the construction restates Theorem 12.1 rather than "
     "escaping it. Its one apparent violation traced to a transcription error in the "
     "input data (Appendix D)."),
]:
    A(P(h, 'h3'))
    A(P(t, 'body'))

A(P("14. What escapes", 'h1'))
A(P("Deductive containment escapes Theorem 12.1, and it is the only thing we have "
    "found that does.", 'body'))
A(P("A bracket is not a function of the coordinates. It is an <b>entailment</b>: given "
    "that the property is monotone in the order, the true value at an unmeasured cell "
    "<i>cannot</i> lie outside the interval formed by its measured neighbours. A "
    "regression returns a point and a confidence interval that fails some fraction of "
    "the time; the order returns containment that holds by construction. The "
    "distinction is between inference and deduction, and it is why the bracket never "
    "failed in 295 cells while every point-estimate claim in this work required "
    "qualification.", 'body'))
A(P("This also explains an asymmetry in compositional prediction. Propagating "
    "<b>point values</b> through the chain n \u2192 I \u2192 \u03b4 \u2192 E amplifies "
    "a 334 cm<super>\u22121</super> input error by a factor of 1.3 \u00d7 "
    "10<super>6</super>, because dI/d\u03b4 \u2248 75,000 cm<super>\u22121</super>. "
    "Propagating <b>intervals</b> through the same chain does not amplify at all: each "
    "level's width is set by the spacing of its own measured neighbours, not inherited "
    "from below. Monotone maps compose exactly on intervals and catastrophically on "
    "points.", 'body'))

A(P("15. Discussion", 'h1'))
A(P("15.1 The thesis against the strongest premise", 'h2'))
A(P("We began expecting the lattice's order to constrain physics. It does not, and the "
    "reason is not that the index was too coarse. Over the course of this work the "
    "index was <b>improved to exactness</b> \u2014 injective at eleven dimensions, "
    "resolving core J, fine structure and the jK label \u2014 and the predictive "
    "boundary did not move by one cell. Theorem 12.1 is indifferent to dimension and "
    "to faithfulness.", 'body'))
A(P("The useful formulation is therefore: <b>an ordinal structure over configuration "
    "space supplies indexing, and indexing is not prediction.</b> What the lattice "
    "contributes to Part II is the well-definedness of \u2018same channel\u2019 and "
    "\u2018interior on some axis\u2019 \u2014 real contributions, since without them "
    "the method could not be stated \u2014 and nothing further.", 'body'))
A(P("15.2 Why energies and nothing else", 'h2'))
A(P("<i>T</i> = <i>Z</i><super>2</super><i>R</i>/\u03bd<super>2</super> is strictly "
    "monotone in every coordinate, has no zeros or stationary points, varies by orders "
    "of magnitude across a series, and is measured to 10<super>\u22123</super> "
    "cm<super>\u22121</super>. The bracket requires all four properties. We tested the "
    "two nearest alternatives and each fails on a different one: dipole matrix elements "
    "have zeros; fine-structure splittings are asymptotically constant. We know of no "
    "other atomic observable with all four.", 'body'))
A(P("15.3 Claims withdrawn", 'h2'))
A(P("Stated explicitly so readers of earlier versions are not misled.", 'body'))
for i, t in enumerate([
    "<b>|\u039b\u2088| = 61,453 as an invariant.</b> A truncation artefact; all derived "
    "region fractions likewise.",
    "<b>\u2018Zero invention\u2019 as a substantive property.</b> The set measured at "
    "0% completion cost was defined by \u00a79.4 chain constraints, and such a set is "
    "closed by construction. The measurement was tautological. The genuinely physical "
    "set has nonzero completion cost at every dimension.",
    "<b>The physical set as a sublattice.</b> False; spin parity breaks join.",
    "<b>Offset coordinates as a repair.</b> Faithful and injective but not a lattice.",
    "<b>Any closure-preserving h depends on one coordinate.</b> True for products of "
    "chains, false for \u039b: 148 of 335 counterexamples on a test lattice. Theorem "
    "4.1 replaces it and is what the argument needs.",
    "<b>Ca I 3d\u00b2 \u00b9D\u2082 at 48,800\u201349,000 cm\u207b\u00b9.</b> Wrong by "
    "\u2248 1,000 cm\u207b\u00b9; it places \u00b9D above \u00b3P, which for "
    "d\u00b2 requires C/B &gt; 5. Revised unperturbed position 47,539\u201348,213 "
    "cm\u207b\u00b9. Caught by the term-ordering constraint, not by the three fitted "
    "analyses that produced it.",
    "<b>A point estimate for Ba I 5d\u00b2 \u00b9G\u2084.</b> Three methods gave 24,163, "
    "23,852 and 22,094 cm\u207b\u00b9, the last outside its own bracket. Withheld-term "
    "validation fails by 1,330 cm\u207b\u00b9. Only the bracket survives.",
    "<b>Maximality without qualification.</b> No derived quantity raises the dimension; "
    "independent quantities do.",
    "<b>The h-axis impossibility as a general result.</b> It is an instance of Theorem "
    "4.1 \u2014 h was defined as a function of outputs. Independent quantities are not "
    "so constrained, which is why J<sub>c</sub> succeeds where h fails.",
]):
    A(Paragraph(t, S['bul'], bulletText=f"{i+1}."))
A(P("15.4 Open questions", 'h2'))
A(P("Whether any atomic observable other than energy satisfies the four conditions of "
    "\u00a715.2. Whether the multi-subshell coverage gap admits a representation "
    "preserving closure \u2014 Appendix A shows the obvious route does not. And whether "
    "the bracketing method transfers to non-atomic ordered systems, which we have not "
    "attempted.", 'body'))

# ============================ APPENDICES ============================
A(PageBreak())
A(P("Appendix A \u2014 The multi-target extension and why it fails", 'h1'))
A(P("The 86% coverage ceiling is caused by configurations with two occupied non-source "
    "subshells. The natural repair is a second target triple (e\u2082, f\u2082, "
    "g\u2082). It fails, instructively.", 'body'))
A(P("<b>Ordering the targets is free.</b> The canonicalisation e\u2081 \u2264 e\u2082 "
    "is admissible \u2014 \u03c6 is the identity \u2014 with zero failures.", 'body'))
A(P("<b>Conservation is not.</b> The requirement g\u2081 + g\u2082 \u2264 q is a bound "
    "on a <b>sum</b>, hence outside \u00a79.4, and it breaks closure: 89,864 join "
    "failures in 979,300 sampled pairs, meets unaffected. The counterexample is two "
    "lines \u2014 a = (g\u2081=1, g\u2082=0, q=1) and b = (g\u2081=0, g\u2082=1, q=1) "
    "each conserve, and their join transfers two electrons having removed one.", 'body'))
A(P("<b>Dropping conservation restores closure</b> (45,690 cells, zero failures) and "
    "produces a lattice describing configurations that cannot exist.", 'body'))
A(P("<b>The conserving set is not a sublattice but is almost a lattice.</b> With "
    "sufficient headroom, 133,542 of 133,542 interior pairs have a unique least upper "
    "bound \u2014 the join exists but is not componentwise max: q rises to admit both "
    "transfers. Physically, the join of two transfer states requires removing another "
    "electron.", 'body'))
A(P("<b>With two sources uniqueness fails too.</b> Conservation becomes g\u2081 + "
    "g\u2082 \u2264 q\u2081 + q\u2082, a sum on both sides; 2.1% of pairs acquire "
    "multiple minimal upper bounds, because the extra ionisation can come from either "
    "source. The result is a graded bounded poset, self-dual in its failures, neither a "
    "join- nor a meet-semilattice.", 'body'))
A(P("<b>And the slot representation is not faithful.</b> Sorted pairs and multisets are "
    "in bijection but the bijection is <b>not a lattice homomorphism</b>: for 3d\u00b9 "
    "and 4p\u00b2, multiset union gives three transferred electrons and the sorted-pair "
    "join gives two. A single-target configuration must be padded to fill two slots, "
    "and two different single-target configurations then collide in the same slot.",
    'body'))

A(P("Appendix B \u2014 Computational methods", 'h1'))
A(P("All computations in Python 3 with NumPy and SciPy. Closure tests either exhaustive "
    "over all pairs (stated where so) or on uniform random samples of "
    "900\u20138,000,000 pairs with the sample size reported. Box searches enumerate all "
    "2<super>d</super> corners of candidate base cells. Null models for the "
    "closure-as-existence tests are of two kinds: uniform random subsets of the "
    "physical envelope matched in size, and marginal-matched subsets drawn with "
    "probability proportional to the observed frequency of each coordinate value, the "
    "latter constructed specifically to absorb observational-completeness effects. "
    "Ritz fits use ordinary least squares of \u03b4 against 1/n<super>2</super>, with "
    "\u03c3 from the standard prediction error including the leverage term.", 'body'))

A(P("Appendix C \u2014 Data provenance", 'h1'))
A(tbl([["source", "used for"],
       ["NIST ASD (Kramida et al., ver. 5.12)", "Ca I/II, Sr II, Kr I/II, Sc III, Ti I levels"],
       ["Sansonetti & Nave, JPCRD 39, 033103 (2010)", "Sr I levels and transition probabilities"],
       ["Curry, JPCRD 33, 725 (2004)", "Ba I/II levels, Land\u00e9 factors"],
       ["Martin et al., NIST SRD 111", "ground configurations, ionisation energies"],
       ["NIST Handbook of Basic Atomic Spectroscopic Data", "H I, Mg I levels"],
       ["Rafiq, Kalyar & Baig, J. Phys. B 40, 3181 (2007)", "Mg I 3snd \u00b9D\u2082 series"],
       ["Cowley (Michigan) compilation", "successive ionisation energies"]],
      [80 * mm, 78 * mm], fs=7.6))
A(Spacer(1, 6))
A(P("Levels are quoted as published; centres of gravity are (2J+1)-weighted.", 'body'))

A(P("Appendix D \u2014 Errors found and corrected during this work", 'h1'))
A(P("Recorded because the method by which they were caught is part of the result.",
    'body'))
for t in [
    "<b>Ba I 6s11f mis-keyed as 6s8f.</b> Detected by the derived ordinal coordinate "
    "producing four order violations, all involving one cell. The datum implies "
    "\u03b4 = \u22122.84 as n = 8, impossible, and \u03b4 = +0.16 as n = 11, correct "
    "for an f orbital. Corrected, the coordinate is 2163/2163 monotone.",
    "<b>Ca I 3d\u00b2 \u00b9D\u2082 position.</b> Detected by the d\u00b2 term-ordering "
    "constraint (\u00b9D &lt; \u00b3P iff C/B &lt; 5), which three fitted analyses had "
    "not applied.",
    "<b>Regex parsing failure.</b> An early configuration parser read 3d4s as "
    "3d\u2074, silently dropping the second subshell and reporting 0% of "
    "configurations as multi-target.",
    "<b>Bracket direction for decreasing sequences.</b> For a decreasing property the "
    "tightest bracket takes the maximum over cells above in n and the minimum over "
    "cells below; the reverse returns the global extremes. The error inflated a "
    "reported width from 11% to 114%.",
    "<b>Pooled \u03c3.</b> Quoting a single \u03c3 across series with genuinely "
    "different defect scatter (a 370\u00d7 range) produced 96.2% coverage at nominal "
    "\u00b11\u03c3 and was misread as heavy tails. Per-cell \u03c3 gives 68.1%.",
    "<b>Anchoring on a published estimate.</b> A point prediction for Ba I 5d\u00b2 "
    "\u00b9G\u2084 was developed with a literature value visible from the first "
    "computation. Three methods were tried and the selection among them was not "
    "independent of that value; the reported range was 38% narrower than the inputs "
    "supported. This is why \u00a711.2 reports a bracket and no estimate, and why the "
    "Kr II prediction was committed in writing before the measurement was requested.",
    "<b>Isolated closure mistaken for joint closure.</b> The offset coordinates of "
    "\u00a76.4 were each verified closed in their own plane and asserted to be jointly "
    "closed. Exhaustive testing showed 222,075 join failures.",
]:
    A(Paragraph(t, S['bul'], bulletText="\u2022"))

A(P("Acknowledgement of computational assistance", 'h1'))
A(P("Substantial parts of the analysis \u2014 the closure and dimension tests, the "
    "ablation studies, the 295-cell verification, the failure diagnostics of Part III, "
    "and several of the corrections in Appendix D \u2014 were carried out in dialogue "
    "with an AI system (Claude, Anthropic), which executed the computations and served "
    "as an adversarial check on intermediate conclusions. The system does not hold "
    "authorship: authorship entails accountability it cannot bear, since it will not "
    "persist to answer for the work. Its errors, several recorded in Appendix D, were "
    "caught by the same process that caught the human ones. What can be said precisely "
    "is that no numerical claim in this paper rests on unexamined output: each was "
    "recomputed, attacked, and in a number of cases withdrawn.", 'body'))

doc = Doc("/mnt/user-data/outputs/indexing-without-prediction.pdf",
          pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
          topMargin=20 * mm, bottomMargin=18 * mm,
          title="Indexing Without Prediction: Maximality and Empirical Boundary "
                "of the Lach Elemental Lattice",
          author="M. Lach", subject="Order theory; atomic spectroscopy",
          creator="prepared for independent review")
doc.build(st)
print("PDF built")
