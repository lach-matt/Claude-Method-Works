#!/usr/bin/env python3
import json
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Image, Table, TableStyle, PageBreak,
                                KeepTogether, HRFlowable)

D = json.load(open('/home/claude/transitions/data.json'))
FIG = '/home/claude/transitions/figs/'
OUTPDF = '/mnt/user-data/outputs/Transitions.pdf'

INK   = colors.HexColor('#1a1a1a')
GREY  = colors.HexColor('#6d6d6d')
RED   = colors.HexColor('#a4302a')
BLUE  = colors.HexColor('#2d4a6b')
RULE  = colors.HexColor('#c9c3b8')

S = {}
S['title'] = ParagraphStyle('title', fontName='Times-Bold', fontSize=30, leading=34,
                            textColor=INK, spaceAfter=4, alignment=TA_LEFT)
S['sub'] = ParagraphStyle('sub', fontName='Times-Italic', fontSize=12.5, leading=16,
                          textColor=GREY, spaceAfter=18)
S['h1'] = ParagraphStyle('h1', fontName='Times-Bold', fontSize=14, leading=17,
                         textColor=INK, spaceBefore=16, spaceAfter=7)
S['h2'] = ParagraphStyle('h2', fontName='Times-Bold', fontSize=10.6, leading=13,
                         textColor=INK, spaceBefore=11, spaceAfter=4)
S['body'] = ParagraphStyle('body', fontName='Times-Roman', fontSize=9.6, leading=13.4,
                           textColor=INK, alignment=TA_JUSTIFY, spaceAfter=6)
S['small'] = ParagraphStyle('small', fontName='Times-Roman', fontSize=8.4, leading=11.4,
                            textColor=GREY, alignment=TA_JUSTIFY, spaceAfter=5)
S['cap'] = ParagraphStyle('cap', fontName='Times-Italic', fontSize=8.2, leading=10.8,
                          textColor=GREY, alignment=TA_LEFT, spaceBefore=3, spaceAfter=11)
S['math'] = ParagraphStyle('math', fontName='Times-Italic', fontSize=10.2, leading=15,
                           textColor=INK, alignment=TA_CENTER, spaceBefore=6, spaceAfter=8)
S['prop'] = ParagraphStyle('prop', fontName='Times-Roman', fontSize=9.6, leading=13.4,
                           textColor=INK, alignment=TA_JUSTIFY, spaceAfter=6,
                           leftIndent=10, borderPadding=0)
S['tab'] = ParagraphStyle('tab', fontName='Times-Roman', fontSize=8.3, leading=10.4, textColor=INK)
S['tabh'] = ParagraphStyle('tabh', fontName='Times-Bold', fontSize=8.3, leading=10.4, textColor=INK)

def P(t, st='body'): return Paragraph(t, S[st])
def rule(): return HRFlowable(width='100%', thickness=0.6, color=RULE,
                              spaceBefore=5, spaceAfter=8)
def fig(name, w=165*mm, cap=''):
    from PIL import Image as PILImage
    im = PILImage.open(FIG + name)
    h = w * im.size[1] / im.size[0]
    els = [Image(FIG + name, width=w, height=h)]
    if cap: els.append(P(cap, 'cap'))
    return KeepTogether(els)

def table(rows, widths, header=True, align=None):
    data = []
    for i, r in enumerate(rows):
        data.append([Paragraph(str(c), S['tabh'] if (header and i == 0) else S['tab']) for c in r])
    t = Table(data, colWidths=widths, hAlign='LEFT')
    st = [('VALIGN', (0,0), (-1,-1), 'TOP'),
          ('TOPPADDING', (0,0), (-1,-1), 3),
          ('BOTTOMPADDING', (0,0), (-1,-1), 3),
          ('LEFTPADDING', (0,0), (-1,-1), 4),
          ('LINEBELOW', (0,0), (-1,0), 0.7, INK if header else RULE),
          ('LINEBELOW', (0,1), (-1,-2), 0.25, RULE),
          ('LINEBELOW', (0,-1), (-1,-1), 0.7, INK)]
    t.setStyle(TableStyle(st))
    return t

story = []
A = story.append

# ============ TITLE ============
A(P('TRANSITIONS', 'title'))
A(P('The closure defect of an index, computed for a universe and for a transition between universes', 'sub'))
A(rule())
A(P('<b>Abstract.</b>  We compute the external definition cost E(X) = |R(X)| &minus; |X| of three '
    'objects: the Lach Cylinder lattice &Lambda;, an index of atomic configurations; a violation index '
    'over nine graded law-coordinates; and the condition under which a molecule survives transit. '
    'R is identified as the closure of a binary constraint network under its monotone binary projections, '
    'and E = 0 is identified as <i>global consistency</i> in the sense of the constraint-satisfaction literature. '
    '&Lambda; is globally consistent at every tower level, verified by ambient-box sweep to 47,775,744 cells, '
    'and its closure is certified by two named theorems &mdash; Freuder 1982 for the tree level, Montanari 1974 '
    'for the monotone levels above it. The violation index is not globally consistent: it carries a defect of '
    '<b>60</b>, characterised, factored 2 &times; 5 &times; 3 &times; 2, and shown projection-covariant across four '
    'resolutions. The molecular transit condition has Helly number greater than 2, with an explicit witness, and '
    'therefore admits no bounded-arity surrogate. The claim is not that other universes exist, nor that transit '
    'between them is possible. It is that an index has a computable defect, that the defect has a location and a '
    'cause, and that the answer differs in kind for a universe and for a transition between universes.', 'body'))
A(rule())

A(fig('f6_1.png', 160*mm,
      'Figure 6.1 (shown first as orientation).  One object is decidable by local consistency; '
      'the two that cross between universes are not, and for the same reason.'))

A(PageBreak())

# ============ PART 0 ============
A(P('Part 0 &mdash; Procedure', 'h1'))
A(P('0.1  Protocols in force', 'h2'))
A(P('Every result below was produced under a fixed working discipline, stated here because several of the '
    'findings are findings <i>about</i> that discipline. Positions are committed in writing before retrieval '
    '(B.2.13); results are computed before the sentence reporting them is written (B.2.14); ambiguity is refused '
    'rather than silently defaulted (B.2.9); targets are enumerated before searching and re-enumerated when the '
    'set grows (B.2.10); and every failure is recorded together with what it excludes (B.2.15). Work is '
    'partitioned into bounded segments with atomic checkpoints.', 'body'))

A(P('0.2  The Admission Law', 'h2'))
A(P('An open index admits any content, and admits it only together with its verification grade. An entry&rsquo;s '
    'grade bounds the operations it may enter. <b>A derived entry carries the minimum grade of its inputs, and no '
    'derivation raises a grade.</b> Collisions route rather than gate: content contradicting the index is admitted '
    'at source grade and flagged, and a collision is discharged only by re-deriving the internal result, never by '
    'refusing the content. The law does not close the index; it prevents an entry from bearing weight it has not '
    'earned.', 'body'))

A(P('0.3  The merge rule, stated as it was learned', 'h2'))
A(P('Five coordinate merges were attempted. Four failed outright and the survivor failed under grading. The '
    'discriminator is unambiguous and is recorded as a rule: <b>a biconditional licenses a merge only if it holds '
    'at every rung of the graded axis.</b> Merging on a one-way implication, or on an intuitive ordering, does not '
    'survive.', 'body'))
A(table([['merge attempted', 'basis', 'outcome'],
         ['no-cloning &equiv; no-discrimination', 'stated biconditional', 'holds at the perfect rung only'],
         ['nonlinearity &rarr; signalling', 'one-way implication', 'failed &mdash; Polchinski nonlinearities'],
         ['microcausality &rarr; signalling', 'one-way implication', 'failed &mdash; Sorkin denies converse'],
         ['signalling on the CHSH scale', 'intuitive ordering', 'failed &mdash; PR boxes reach 4 without signalling'],
         ['discrimination into correlation strength', 'intuitive ordering', 'failed &mdash; different quantities']],
        [58*mm, 45*mm, 62*mm]))
A(Spacer(1, 6))

A(P('0.4  Operator reliability, measured rather than assumed', 'h2'))
A(P('Committed predictions were scored by domain. Predictions aimed at <i>logical structure</i> &mdash; which '
    'hypotheses a theorem uses, which way an entailment runs, what a conclusion licenses &mdash; scored 4/4 on '
    'three consecutive tests. Predictions aimed at <i>how a field regards a claim</i> scored 1/4. Predictions of '
    '<i>new implications not yet in the table</i> scored approximately 1 in 5. Grades were assigned accordingly, '
    'and no clause was entered into the index on the operator&rsquo;s assessment: every edge below comes from '
    'retrieval.', 'body'))

# ============ PART I ============
A(P('Part I &mdash; The operator', 'h1'))
A(P('1.1  Definitions', 'h2'))
A(P('Let X be a finite set of integer tuples, X &sube; A<sub>1</sub> &times; &hellip; &times; A<sub>d</sub>. '
    'Define the observed value sets, the pairwise monotone envelopes, and the reconstruction:', 'body'))
A(P('A<sub>i</sub>(X) = { x<sub>i</sub> : x &isin; X }', 'math'))
A(P('&phi;<sub>ij</sub>(v) = max { x<sub>i</sub> : x &isin; X, x<sub>j</sub> &le; v }', 'math'))
A(P('R(X) = { x &isin; &prod; A<sub>i</sub>(X) : x<sub>i</sub> &le; &phi;<sub>ij</sub>(x<sub>j</sub>) for all i &ne; j }', 'math'))
A(P('<b>E(X) = |R(X)| &minus; |X|</b>', 'math'))
A(P('No outside knowledge enters. R(X) is what a reader could reconstruct from the cells alone, and E(X) is the '
    'gap: cells the structure implies and the index denies. E is therefore an <i>external definition cost</i>.', 'body'))

A(P('1.2  Proposition (extensivity)', 'h2'))
A(P('<b>X &sube; R(X), hence E &ge; 0.</b>  <i>Proof.</i> Let x &isin; X. Each x<sub>i</sub> &isin; A<sub>i</sub>(X) '
    'by definition. For any i &ne; j, the set { y<sub>i</sub> : y &isin; X, y<sub>j</sub> &le; x<sub>j</sub> } '
    'contains x<sub>i</sub>, since x itself satisfies x<sub>j</sub> &le; x<sub>j</sub>. Hence '
    '&phi;<sub>ij</sub>(x<sub>j</sub>) &ge; x<sub>i</sub>, and x &isin; R(X). &#9633;', 'prop'))

A(P('1.3  Proposition (R is a closure operator)', 'h2'))
A(P('R is extensive (1.2), monotone, and idempotent. Idempotence was verified computationally on both principal '
    'objects: R(R(&Lambda;<sub>8</sub>)) = R(&Lambda;<sub>8</sub>) = 976, and R(R(V)) = R(V) = 2,400 for the '
    'violation index V. Monotonicity was tested on thirty nested random pairs without failure. The closed sets '
    'therefore form a Moore family.', 'prop'))

A(P('1.4  Identification', 'h2'))
A(P('R is the closure of a binary constraint network under its monotone binary projections, and <b>E(X) = 0 if and '
    'only if X is globally consistent</b> &mdash; every tuple consistent with all binary projections is a solution. '
    'This is standard terminology in the constraint-satisfaction literature, and it supplies two theorems that '
    'certify closure rather than merely observe it.', 'body'))

A(P('1.5  Relation to the full minimal network', 'h2'))
A(P('R does not use the full binary projections; it retains only the monotone upper envelope. Writing BPC(X) for '
    'the closure under full binary projections, we have <b>X &sube; BPC(X) &sube; R(X)</b>: the first inclusion is '
    '1.2, the second because (x<sub>i</sub>, x<sub>j</sub>) &isin; proj<sub>ij</sub>(X) implies '
    '&phi;<sub>ij</sub>(x<sub>j</sub>) &ge; x<sub>i</sub>. Consequently E = 0 implies global consistency, while '
    'E &gt; 0 is in principle ambiguous &mdash; it may signal either failure of global consistency or mere '
    'coarseness of the envelope. <b>Both were computed.</b> For the violation index, R = BPC exactly '
    '(2,400 = 2,400), so R is the minimal network there and the entire defect is genuine global-consistency '
    'failure. For &Lambda;<sub>8</sub>, BPC = 976 = |&Lambda;<sub>8</sub>|.', 'body'))
A(fig('f1_1.png', 155*mm,
      'Figure 1.1.  The three nested sets, computed for both principal objects. For &Lambda; all three coincide. '
      'For the violation index BPC and R coincide and X sits strictly inside, so the defect of 60 is global-'
      'consistency failure and not envelope coarseness.'))

A(P('1.6  What the operator cannot see', 'h2'))
A(P('Six blindnesses were identified, each demonstrated by computation rather than argument.', 'body'))
A(table([['blind to', 'demonstration', 'E'],
         ['decreasing bounds (exclusion)', 'Rd forbids T', '0 &rarr; 6'],
         ['non-monotone relations (congruence)', 'axis-10 parity', '0 &rarr; 678'],
         ['ternary constraints', 'conjugation ceiling / triangle / Buniy', '186 / 35,570 / 60'],
         ['unoccupied dimensions', 'a fifth axis with one occupied value', 'unchanged'],
         ['the measure', 'the Lorentz-violating neighbour', 'unchanged'],
         ['derived coordinates', 'an added &ldquo;payment&rdquo; axis', '60 &rarr; 120']],
        [52*mm, 68*mm, 45*mm]))
A(Spacer(1, 4))
A(P('The last is a structural result about the method and not about this construction. A coordinate defined as a '
    'function of others cannot repair closure: R reconstructs from cells alone, and the definition is precisely the '
    'outside knowledge E measures the absence of. Adding such an axis enlarges the ambient box while leaving |X| '
    'fixed, so the defect strictly increases. <b>The entire class of derived-coordinate repairs is excluded.</b>', 'body'))
A(fig('f1_2.png', 165*mm,
      'Figure 1.2.  Four two-dimensional cases on a common grid. Solid dots are members of X; hollow red dots are '
      'cells the envelope admits and the constraint denies. A monotone bound is cut exactly; a decreasing bound, a '
      'congruence, and a ternary constraint are not. The fourth panel is the parity relation a &oplus; b &oplus; c = 0, '
      'whose three pairwise projections are all complete.'))

A(P('1.7  The closure rule', 'h2'))
A(P('<b>A tightening preserves E = 0 if and only if it binds one coordinate by a monotone function of one other.</b> '
    'Four cases were computed, two on each side of the rule, and the magnitude of the defect tracks the arity of the '
    'violation.', 'body'))
A(fig('f1_3.png', 160*mm,
      'Figure 1.3.  Pairwise-monotone tightenings preserve closure; multi-parent and non-monotone tightenings do not. '
      'Non-monotonicity costs more than extra arity on the same axis (678 against 186).'))

A(P('1.8  Named theorems', 'h2'))
A(table([['result', 'attribution'],
         ['Tree constraint graph &rArr; arc consistency gives global consistency',
          'Freuder 1982, <i>A sufficient condition for backtrack-free search</i>, JACM 29(1) 24&ndash;32'],
         ['Monotone constraints &rArr; path consistency gives global consistency', 'Montanari 1974'],
         ['Generalisation to row-convex constraints', 'Van Beek and Dechter 1995'],
         ['Constraint tightness', 'Van Beek and Dechter 1997'],
         ['Closure properties of constraints', 'Jeavons, Cohen and Cooper 1998']],
        [80*mm, 85*mm]))
A(Spacer(1, 4))
A(P('These two theorems between them certify every closure result in Part II, and neither applies to the violation '
    'index of Part IV.', 'body'))

A(PageBreak())

# ============ PART II ============
A(P('Part II &mdash; &Lambda; verified', 'h1'))
A(P('2.1  Caps and the tower', 'h2'))
A(P('The cap tuple (n, e, &#8467;, k, f) = (3, 3, 1, 3, 1) is unique in the search range for '
    '|&Lambda;<sub>8</sub>| = 976. The tower and its closure certificates reproduce exactly.', 'body'))
tw = [['level', 'cells', 'ambient box', 'E']]
for k in ['8','9','10','11','12','13']:
    t = D['tower'][k]
    tw.append([k, f"{t['cells']:,}", f"{t['box']:,}", '0'])
tw.insert(3, ["9'", f"{D['tower']['9prime']['cells']:,}" if '9prime' in D['tower'] else '1,561', '&mdash;', '0'])
A(table(tw, [22*mm, 34*mm, 40*mm, 20*mm]))
A(Spacer(1, 5))
A(P('E = 0 at every level, verified by sweeping the entire ambient box &mdash; 47,775,744 cells at '
    '&Lambda;<sub>13</sub> &mdash; rather than by pair testing. |BPC(&Lambda;<sub>8</sub>)| = 976, so &Lambda; is '
    'globally consistent in the literature&rsquo;s exact sense and not merely envelope-closed.', 'body'))
A(fig('f2_1.png', 160*mm,
      'Figure 2.1.  Cells against ambient box, log scale. Closure holds at every level while density falls from '
      '14.1% to 0.42%. The two properties are independent: &Lambda; is self-defining and increasingly sparse.'))

A(P('2.2  The constraint graph and where Freuder applies', 'h2'))
A(P('&Lambda;<sub>9</sub> has nine nodes and eight edges and is acyclic &mdash; a spanning tree &mdash; so '
    'Freuder&rsquo;s theorem applies and closure is certified structurally. &Lambda;<sub>9</sub>&prime; adds the '
    'bound 2S&prime; &le; 2f+1 and creates the cycle f&ndash;g&ndash;2S&prime;. &Lambda;<sub>10</sub> adds v with '
    '<i>two</i> bounds, 2S&prime; &le; v and v &le; g, giving ten nodes and ten edges: also not a tree. '
    '<b>&Lambda;<sub>9</sub> is therefore the last tree level</b>, and closure above it rests on monotonicity '
    '(Montanari) rather than on structure (Freuder).', 'body'))
A(fig('f2_2.png', 150*mm,
      'Figure 2.2.  The constraint graph at &Lambda;<sub>9</sub> and &Lambda;<sub>9</sub>&prime;. The first cycle '
      'is f&ndash;g&ndash;2S&prime;, shown in red. This is the documented trade &mdash; the tree or the tightness &mdash; '
      'and the cost of taking the tightness is the propagation guarantee.'))

A(P('2.3  Density and the three non-obvious exact sets', 'h2'))
A(P('The density column &mdash; the fraction of each admissible fibre that exact vector coupling realises &mdash; '
    'reproduces at every axis once the correct exact sets are used. Three of the six are not the obvious ones, and '
    'the column cannot be rebuilt without them:', 'body'))
A(table([['axis', 'exact set', 'density'],
         ['9', 'the spin set of f<super>g</super> by microstate enumeration', '63.7%'],
         ["9'", 'the same, one Pauli cut tighter', '67.5%'],
         ['10', 'terms <i>new</i> at v, conjoined with parity and the conjugation ceiling', '44.7%'],
         ['11', 'J of terms of &#8467;<super>k</super> carrying <i>the cell&rsquo;s own</i> multiplicity 2S', '17.0%'],
         ['12', 'the triangle with the cell&rsquo;s own f, step 2', '31.4%'],
         ['13', 'the doublet K &plusmn; 1', '64.4%']],
        [16*mm, 110*mm, 24*mm]))
A(Spacer(1, 4))
A(P('The statistic is per-axis local: the exact fibre summed over every parent at the level below, divided by the '
    'admissible fibre summed the same way, unconditioned on whether the parent is itself exact.', 'small'))
A(fig('f2_3.png', 160*mm,
      'Figure 2.3.  Axis 9&prime; is a free tightening &mdash; it removes 93 cells that are provably unrealised, '
      'the (f = 0, g = 2, 2S&prime; = 2) triplet-spin s<super>2</super> targets &mdash; and the canonical tower '
      'declines it, because it costs the tree.'))

A(P('2.4  Closure against exactness', 'h2'))
A(P('The two are incompatible, and one axis demonstrates it. Tightening axis 12 from the envelope bound '
    '2K &le; 2J<sub>c</sub> + 2f<sub>max</sub> to the exact triangle with the cell&rsquo;s own f cuts the lattice '
    'by a factor of 3.18 and takes E from 0 to 35,570 &mdash; more than half the reconstructed cells denied by the '
    'tight index. <b>&Lambda; is loose by design.</b> The looseness is the price of being self-defining, and the '
    'exact coupling rules are precisely the external information E would then have to charge for.', 'body'))
A(fig('f2_4.png', 160*mm,
      'Figure 2.4.  Axis 12, loose and tight. An index cannot be both closed and exact when the exact bound is '
      'multi-parent.'))

A(PageBreak())

# ============ PART III ============
A(P('Part III &mdash; Transit structures on &Lambda;', 'h1'))
A(P('3.1  Composability and the one-level window', 'h2'))
A(P("A cell's target is a legal source exactly when 2S&prime; &le; g &mdash; which <i>is</i> axis 9. Below that "
    "level the target's spin is unspecified and composability has no truth value. "
    f"At &Lambda;<sub>9</sub>, {D['quiver']['arcs']:,} of {D['quiver']['composable_of']:,} cells are composable, "
    "reproducing the canonical figure. Combined with 2.2 this gives a single-level window: "
    "<b>&Lambda;<sub>9</sub> is the first composable level and the last tree level.</b> "
    "&Lambda;<sub>8</sub> has the tree and no endpoint; &Lambda;<sub>9</sub>&prime; has the endpoint and no tree.", 'body'))
A(fig('f3_1.png', 155*mm,
      'Figure 3.1.  The two properties a transit map requires &mdash; a defined endpoint and a propagation '
      'guarantee &mdash; overlap in exactly one column.'))

A(P('3.2  The quiver and its line digraph', 'h2'))
A(P(f"Composable cells are arcs of a quiver Q on {D['quiver']['states']} atomic states. The composition graph &mdash; "
    "A &rarr; B when A&rsquo;s target is B&rsquo;s source &mdash; is precisely the <b>line digraph L(Q)</b>. "
    f"Its edge count {D['quiver']['linedigraph_edges']:,} equals &Sigma;(in &times; out) over states exactly. "
    f"The {D['quiver']['loops']} degenerate cells, whose target equals their own source, are Q&rsquo;s loops; "
    "and because Q has a loop at every vertex, return is available in one step from every state. "
    "The shortest non-degenerate cycle has length 2 and is a spin flip in hydrogen&rsquo;s ground state.", 'body'))
A(fig('f3_2.png', 160*mm,
      'Figure 3.2.  Left: the quiver, with a loop at every vertex &mdash; which is why return is trivial. '
      'Right: the line-digraph identity, exact.'))

A(P('3.3  The Hasse diagram', 'h2'))
A(P('Unit-step adjacency coincides <i>exactly</i> with the covering relation of (&Lambda;<sub>9</sub>, &le;) &mdash; '
    f"{D['hasse']['edges']:,} edges by both definitions, with zero non-unit covers. &Lambda;<sub>9</sub> is gap-free. "
    f"Degrees run {D['hasse']['deg_min']} to {D['hasse']['deg_max']}, mean {D['hasse']['deg_mean']}; the graph is "
    "connected with no isolated cells.", 'body'))
A(P('<b>Proposition. The girth is exactly 4.</b>  <i>Proof.</i> Suppose a, b, c are mutually adjacent. If a&ndash;b '
    'differ in coordinate i and b&ndash;c in coordinate j &ne; i, then a&ndash;c differ in two coordinates and are '
    'not adjacent. If i = j, then a&ndash;c differ by 0 or 2 in that coordinate and are again not adjacent. So no '
    'triangle exists and the girth is at least 4. A square is exhibited. &#9633;', 'prop'))
A(fig('f3_3.png', 150*mm,
      'Figure 3.3.  A proof rather than a sample: the square establishes girth &le; 4 and the impossible triangle '
      'establishes girth &ge; 4.'))

A(P('3.4  The molecular condition', 'h2'))
A(P('Transit moves a fibre, not a cell: the atoms of a molecule must displace together, so a circuit requires a '
    '<i>common</i> square direction across every constituent. Individually this is never the obstacle &mdash; every '
    f"cell has between {D['squares']['min']} and {D['squares']['max']} square directions, mean "
    f"{D['squares']['mean']}, and none has zero. <b>The obstruction is entirely collective.</b>", 'body'))
fr = [['atoms', 'trials', 'feasible', '95% interval']]
for f in D['feasibility']:
    fr.append([str(f['m']), f"{f['N']:,}", f"{f['rate']:.4g}%", f"[{f['lo']:.4g}, {f['hi']:.4g}]"])
A(table(fr, [18*mm, 30*mm, 28*mm, 40*mm]))
A(Spacer(1, 4))
A(P('The decay is geometric, a factor of approximately 1.9 per added atom. Homonuclear molecules are unconstrained: '
    'atoms sharing a cell intersect trivially, so the constraint lives entirely in heteronuclear structure &mdash; '
    'which is a physically sensible place for it to be.', 'body'))
A(fig('f3_4.png', 160*mm,
      'Figure 3.4.  Wilson intervals are drawn and are invisible at this scale, which is the point: the earlier '
      'four-thousand-draw estimate of 0.03% at ten atoms was wrong by a factor of nearly three.'))

A(P('3.5  Helly number', 'h2'))
A(P('Each cell carries a set of available square directions, and molecular transit asks whether m such sets '
    'intersect. The natural invariant is the Helly number. <b>It exceeds 2</b>, with an explicit witness: three '
    'cells carrying 25, 26 and 40 directions, pairwise intersecting, with empty triple intersection. And the '
    'failure deepens with m without saturating.', 'body'))
hr = [['atoms', 'pairwise-intersecting samples', 'of those, jointly intersecting']]
for h in D['helly']:
    hr.append([str(h['m']), f"{h['pairwise']:,}", f"{h['joint']:,}   ({h['pct']:.1f}%)"])
A(table(hr, [18*mm, 55*mm, 55*mm]))
A(Spacer(1, 4))
A(P('<b>Molecular transit therefore has no bounded-arity surrogate.</b> It cannot be decomposed into pairwise '
    'compatibility between atoms at any fixed order, and by the same theorem that governs everything else here '
    '&mdash; local consistency is insufficient for non-binary networks &mdash; a molecule&rsquo;s transit '
    'feasibility is not a globally consistent constraint network.', 'body'))
A(fig('f3_5.png', 160*mm,
      'Figure 3.5.  The witness triple, and the absence of saturation. A Helly number of 2 would place every point '
      'on the dashed line.'))

A(PageBreak())

# ============ PART IV ============
A(P('Part IV &mdash; The violation index', 'h1'))
A(P('4.1  Coordinates and rungs', 'h2'))
A(P('Nine graded coordinates, arrived at after five merge withdrawals (0.3). Every rung is sourced individually; '
    'the causal ladder distinguishes a preferred <i>threading</i> &mdash; a preferred time direction, twist '
    'permitted, finite speeds, no universal horizon &mdash; from a preferred <i>foliation</i>, which is '
    'hypersurface-orthogonal, carries an instantaneous mode, and admits a universal horizon.', 'body'))
A(table([['axis', 'content', 'rungs'],
         ['X', 'causal ladder', 'Lorentz invariant / threading / foliation / chronology violated'],
         ['S<sub>corr</sub>', 'correlation strength', 'Bell-local (2) / quantum (2&radic;2) / post-quantum (4)'],
         ['IC', 'information causality', 'respected / violated at m &gt; 0 / violated at m = 0, i.e. signalling'],
         ['U', 'unitarity', 'unitary / Lindblad, local and EM-conserving / requiring locality broken'],
         ['E', 'null energy condition', 'intact / pointwise / ANEC small / QI-bounded / QI-violating'],
         ['L', 'linearity', 'linear / nonlinear'],
         ['SD', 'microcausality', 'holds / broken'],
         ['DN<sub>c</sub>', 'cloning', 'quantum-optimal / exceeding / perfect deterministic'],
         ['DN<sub>d</sub>', 'state discrimination', 'quantum-optimal / exceeding / perfect']],
        [16*mm, 34*mm, 115*mm]))
A(Spacer(1, 5))

A(P('4.2  The origin, two components empirically fixed', 'h2'))
A(P('Our universe sits at (0, 1, 0, 0, 1, 0, 0, 0, 0). Two components are fixed by measurement rather than by '
    'argument, and they are the first coordinates in the construction whose values are not matters of inference. '
    '<b>S<sub>corr</sub> = 1</b>: quantum mechanics violates Bell locality while respecting microcausality. '
    '<b>E = 1</b>: the Casimir effect is measured, gives negative energy density, and violates the null energy '
    'condition pointwise while satisfying its averaged forms. The remaining seven are argued.', 'body'))
A(fig('f4_1.png', 168*mm,
      'Figure 4.1.  The nine ladders and our position. Ringed nodes are the two empirically fixed components. '
      'Note that E = 0 &mdash; the null energy condition intact everywhere &mdash; is <i>not</i> where we sit.'))

A(P('4.3  The defect', 'h2'))
A(P(f"The index has {D['index']['cells']:,} cells and a defect of <b>{D['index']['gc_defect']}</b>, of which "
    f"{D['index']['coarseness']} is envelope coarseness. All sixty are genuine global-consistency failure. "
    "Every excess cell has X = 0, U = 0, SD = 0, IC &lt; 2 and E &ge; 2. In words: "
    "<b>sixty ways to violate the averaged null energy condition with nothing broken that could pay for it.</b>", 'body'))
A(fig('f4_3.png', 160*mm,
      'Figure 4.3.  The sixty enumerated and factored, in the manner in which the periodic table&rsquo;s thirty-six '
      'are the gaps in the short periods. The E rungs split exactly evenly, 30 and 30, because the constraint says '
      '<i>something must pay</i> and not <i>how much</i>.'))
A(P('The cause is identified. The constraint is a three-way branch &mdash; violating the averaged null energy '
    'condition forces instability or superluminal excitations, and instability itself branches to non-unitarity or '
    'a preferred frame. No pair of coordinates can carry it, and R sees only pairs.', 'body'))

A(P('4.4  Projection-covariance', 'h2'))
A(P('The defect is not an artefact of the coordinate count. Projecting the <i>same</i> index onto nested subsets, '
    'with one edge set throughout, gives a single finding counted four ways: the signature is identical at every '
    'resolution and each added axis multiplies the count by its free multiplicity.', 'body'))
pr = [['coordinates retained', 'cells', 'defect']]
for p in D['projections']:
    pr.append([f"{p['label']} ({p['coords']})", f"{p['cells']:,}", str(p['defect'])])
A(table(pr, [50*mm, 30*mm, 25*mm]))
A(Spacer(1, 4))
A(fig('f4_4.png', 158*mm,
      'Figure 4.4.  One index, four projections. An earlier uncontrolled sequence built from three separately '
      'constructed indices landed on the same points; the arithmetic was right and the warrant was not, and the '
      'controlled projection was required to establish it.'))

A(P('4.5  Destination and the formalism scoping', 'h2'))
A(P('Chronology violation sits at X = 3. What it <i>costs</i> depends on the quantum theory of closed timelike '
    'curves adopted, and the dependence is load-bearing on the destination and not merely on the path.', 'body'))
rr = [['CTC model', 'cells', 'destination floor', 'steps']]
for lab in ['D-CTC', 'P-CTC', 'model-independent']:
    r = D['routes'][lab]
    rr.append([lab, f"{r['cells']:,}", str(tuple(r['destination'])), str(r['steps'])])
A(table(rr, [40*mm, 25*mm, 62*mm, 18*mm]))
A(Spacer(1, 4))
A(P('<b>Model-independently, chronology violation requires exactly three things:</b> the causal ladder at X = 3, '
    'unitarity broken at the Lindblad rung, and the averaged null energy condition violated by an arbitrarily small '
    'amount. It does not require exceeding Tsirelson&rsquo;s bound, violating information causality, cloning, perfect '
    'discrimination, abandoning linearity, or breaking microcausality &mdash; each of which appeared in the '
    'destination at some earlier reconstruction and dropped out when a merge was undone or an axis graded.', 'body'))
A(P('The step count is withdrawn as a reportable quantity: it is grading-dependent, changing from six to seven '
    'purely by giving one axis three values instead of two. The destination floor is the invariant.', 'small'))
A(fig('f4_2.png', 168*mm,
      'Figure 4.2.  Three routes from the same origin. Choosing Deutsch&rsquo;s prescription rather than the '
      'model-independent core adds signalling, nonlinearity, cloning and perfect discrimination to the destination.'))

A(PageBreak())

# ============ PART V ============
A(P('Part V &mdash; The multilattice', 'h1'))
A(P('5.1  Profile to lattice', 'h2'))
A(P('If a profile fixes the laws, the laws fix the lattice. The map was demonstrated on two of the nine '
    'coordinates. <b>S<sub>corr</sub> = 3</b> breaks the spin-statistics theorem, hence Pauli exclusion, hence '
    '&Lambda;&rsquo;s third bound. <b>X &ge; 1</b> reaches the radial bound through Lorentz violation.', 'body'))

A(P('5.2  Parastatistics: other universes are also globally consistent', 'h2'))
A(P('Generalising the term enumeration to m particles per spin-orbital, with capacity m(4&#8467;+2), and verifying '
    'that m = 1 reproduces the canon exactly:', 'body'))
ps = [['m', '&Lambda;<sub>8</sub>', '&Lambda;<sub>9</sub>', '&Lambda;<sub>10</sub>', '&Lambda;<sub>11</sub>', 'E']]
for m in ['1', '2', '3']:
    v = D['parastat'][m]
    ps.append([m + (' (fermionic)' if m == '1' else ''), f'{v[0]:,}', f'{v[1]:,}', f'{v[2]:,}', f'{v[3]:,}', '0'])
A(table(ps, [30*mm, 24*mm, 24*mm, 26*mm, 26*mm, 14*mm]))
A(Spacer(1, 4))
A(P('E = 0 throughout. <b>A universe with different statistics is also a closed index</b> &mdash; relaxing Pauli '
    'changes a coefficient inside a monotone pairwise bound, which is exactly the closure-preserving class.', 'body'))

A(P('5.3  Lorentz violation does not change the lattice', 'h2'))
A(P('The Standard-Model Extension computes level shifts in the existing (n, &#8467;, m) basis. The bound '
    '&#8467; &le; n &minus; 1 follows from node counting, n = n<sub>r</sub> + &#8467; + 1 with n<sub>r</sub> &ge; 0, '
    'which no level shift touches. <b>The accidental degeneracy lifts; the quantum numbers do not move.</b> So the '
    'Lorentz-violating neighbour has the <i>same</i> 976 cells and a different energy ordering.', 'body'))
A(P('<b>Corollary. The lattice does not individuate universes.</b> Two universes can share a cell set and differ '
    'only in measure &mdash; and the measure is invisible to R. This is the sharpest limitation of the method: '
    'E = 0 certifies that nothing about the <i>cell set</i> requires external definition. It says nothing whatever '
    'about the measure, and charges nothing for it.', 'body'))

A(P('5.4  Monotone and non-monotone radial bounds', 'h2'))
lb = [['bound', 'monotone', 'cells', 'E']]
for r in D['lbound']:
    lb.append([r['label'].replace('<=', ' &le; ').replace('//', '/'),
               'yes' if r['monotone'] else '<b>no</b>', f"{r['cells']:,}",
               f"<b>{r['E']:,}</b>" if r['E'] else '0'])
A(table(lb, [34*mm, 22*mm, 26*mm, 24*mm]))
A(Spacer(1, 4))
A(P('Two of these have <i>identical cardinality</i> &mdash; 32,535 cells each &mdash; and opposite closure. '
    '<b>Closure is not about how many cells an index has; it is about whether its bounds rise.</b> A peaked bound is '
    'the conjugation signature: a symmetric non-constant function is not monotone, which is the same shape that '
    'places the exact coupling bounds outside the closure-preserving class inside &Lambda; itself.', 'body'))
A(fig('f5_2.png', 168*mm,
      'Figure 5.2.  Six radial bounds. Four rise and close; two peak and open.'))

A(P('5.5  Transit admissibility is a containment condition', 'h2'))
A(P('The constraint a molecule must satisfy is that each of its atoms is a cell of the receiving universe &mdash; '
    'testable on the one-dimensional projection. At the book&rsquo;s caps every projection coincides across '
    'universes, but this is an artefact: the occupancy bound never binds, because k &le; min(cap(&#8467;,m), 3) '
    'reaches the cap at &#8467; = 1 for every m. At caps (4, 4, 2, 12, 2) the projections diverge in k, q, g and 2S.', 'body'))
A(P('<b>Containment survives at both cap settings, and it is directional.</b> Relaxing a bound only ever admits '
    f"cells, so &Lambda;(m=1) &sube; &Lambda;(m=2): outward loss {D['containment']['outward_lost']} of "
    f"{D['containment']['m1']:,}; inward loss {D['containment']['inward_lost']:,} of {D['containment']['m2']:,}. "
    "A molecule can always be carried outward and not always inward, and the failure is detectable at one dimension "
    "without ever examining the joint structure &mdash; which is what makes it the only relation &Lambda; needs to carry.", 'body'))
A(fig('f5_1.png', 158*mm,
      'Figure 5.1.  Transit outward is unobstructed; transit inward loses three quarters of the cells.'))

A(P('5.6  What the measure cannot see', 'h2'))
M = D['measure']
A(P(f"The componentwise order on &Lambda;<sub>8</sub> fixes the relative position of {M['comparable']:,} of "
    f"{M['pairs']:,} pairs &mdash; {M['pct_comparable']:.1f}% &mdash; with exactly one minimal and one maximal cell. "
    f"Of those ordered pairs, {M['ordered_same_n']:,} share the principal quantum number and are therefore "
    f"indistinguishable to a measure depending on n alone. <b>Our own universe fails to measure "
    f"{M['pct_blind_of_ordered']:.1f}% of what its own lattice orders.</b> That is the Coulomb accidental degeneracy, "
    "stated as a defect in the measure rather than as a symmetry of the potential &mdash; and it is precisely what "
    "the Lorentz-violating neighbour lifts.", 'body'))
A(fig('f5_3.png', 160*mm,
      'Figure 5.3.  The lattice says what exists; the order says what is near; the measure says what it costs. '
      'E certifies only the first.'))

A(PageBreak())

# ============ PART VI ============
A(P('Part VI &mdash; Results', 'h1'))
A(P('<b>6.1</b>  A universe is a globally consistent constraint network: monotone, binary, tree-structured at '
    '&Lambda;<sub>9</sub> and monotone above it. Both certifying theorems are named and neither is ours. Closure '
    'survives under other statistics (m = 1, 2, 3) and under any monotone radial bound.', 'body'))
A(P('<b>6.2</b>  Transit between universes is not expressible as one. Its cost carries a defect of 60, located on '
    'a single ternary constraint, characterised, factored, and projection-covariant. What is transported carries an '
    'unbounded Helly number. Neither is decidable by local consistency, and for the same reason.', 'body'))
A(P('<b>6.3</b>  For chronology violation specifically, model-independently: destination floor X = 3, U = 1, E = 2; '
    'transit domain &Lambda;<sub>9</sub>; circuit floor girth 4; molecular feasibility decaying geometrically to '
    '0.0122% at twelve atoms.', 'body'))
A(P('<b>6.4</b>  Openness is not a defect awaiting repair. Derived-coordinate repair is excluded as a class, and '
    'the only repair available to the periodic table &mdash; a genuine re-indexing &mdash; has no analogue here that '
    'we have found. The defect is a property of the object.', 'body'))
A(P('<b>6.5</b>  What is <i>not</i> claimed. Nothing here bears on whether other universes exist, nor on whether '
    'transit between them is physically achievable. The periodic table&rsquo;s external definition cost of 36 is a '
    'claim about a drawing and not about chemistry; the 60 computed here is a claim about a coordinate set and not '
    'about the multiverse.', 'body'))

# ============ PART VII ============
A(P('Part VII &mdash; Register of withdrawals', 'h1'))
A(P('The following were held during the work and are withdrawn, with causes recorded. They are included because a '
    'register of what a method excluded is evidence about the method.', 'body'))
A(table([['withdrawn', 'cause'],
         ['16 destinations; 57 profiles; E = 0 for the violation index',
          'the 57-profile table was silently D-CTC; the assumption was unmarked'],
         ['surviving addresses {Rd} and {E, Rd}',
          'computed over entries since withdrawn; E is never minimal once its outgoing edge is queried'],
         ['the path-versus-jump distinction',
          'path-reachability equals jump-reachability: closure supplies satisfying disjuncts on arrival'],
         ['E = 0 at six consecutive reconstructions',
          'all six inherited a forcing edge that should have been a disjunction'],
         ['the six-step route as a robust figure',
          'grading-dependent; became seven on regrading one axis'],
         ['&ldquo;global parabolicity&rdquo;',
          'the author&rsquo;s own term, unsourced; the literature gives the universal horizon'],
         ['Penrose as evidence for weak cosmic censorship',
          'circular &mdash; censorship is an input required to read a black hole out of the theorem'],
         ['the 6 / 20 / 60 trend as first reported',
          'read across three separately constructed indices; required a controlled projection']],
        [66*mm, 99*mm]))
A(Spacer(1, 5))
A(P('Attribution corrections: Flanagan&ndash;Marolf&ndash;Wald for Flanagan&ndash;Wald; Bakker&ndash;Grimm&ndash;'
    'Schnell&ndash;Tsimerman for Douglas&ndash;Grimm&ndash;Schlechter; the strong-cosmic-censorship perturbation '
    'field is a massless neutral scalar and not gravitational or electromagnetic. Status corrections: '
    'Graham&ndash;Olum and Simon&ndash;Bu&#382;ek&ndash;Gisin both moved out of the theorem column.', 'small'))

# ============ PART VIII ============
A(P('Part VIII &mdash; Open', 'h1'))
A(table([['item', 'state'],
         ['The Lindblad rung mechanism (U = 1)',
          'blocked &mdash; two fetch attempts, full text unreachable; the rung stands at published-abstract grade '
          'with its mechanism untested'],
         ['Profile-to-lattice map', 'demonstrated on two of nine coordinates; not established that the map is '
          'injective, and one case shows it is not'],
         ['&Lambda;<sub>12</sub> and &Lambda;<sub>13</sub> under parastatistics',
          'ambient box exceeds the sweep limit'],
         ['The composition graph and the violation index',
          'unjoined &mdash; &Lambda; carries no coordinate for which universe a cell is in, only whether a cell '
          'exists there'],
         ['The joint-square condition', 'the literature supplies a name &mdash; an intersection problem on a set '
          'system &mdash; but no theorem; Helly numbers are computed per system, and this one is not finite in any '
          'tested range'],
         ['Retrieval matrix', '24 of 72 ordered coordinate pairs resolved']],
        [56*mm, 109*mm]))
A(Spacer(1, 6))
A(rule())
A(P('All numerical results in this paper were recomputed in a single audit pass immediately before writing: '
    'twenty-six checks against independently reproduced values, zero failures, together with two propositions '
    'replacing previously sampled claims. One methodological defect was found in that audit and is recorded in '
    'Part VII. Figure data and the audit script accompany this document.', 'small'))

doc = BaseDocTemplate(OUTPDF, pagesize=A4,
                      leftMargin=22*mm, rightMargin=22*mm,
                      topMargin=20*mm, bottomMargin=18*mm,
                      title='Transitions', author='The Method',
                      subject='The closure defect of an index')
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='f')

def deco(canv, d):
    canv.saveState()
    canv.setFont('Times-Roman', 7.5)
    canv.setFillColor(GREY)
    canv.drawString(22*mm, 11*mm, 'TRANSITIONS')
    canv.drawRightString(A4[0] - 22*mm, 11*mm, str(canv.getPageNumber()))
    canv.restoreState()

doc.addPageTemplates([PageTemplate(id='main', frames=[frame], onPage=deco)])
doc.build(story)
print('PDF written:', OUTPDF)
