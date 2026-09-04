#!/usr/bin/env python3
"""r2-ch14o — prose batch for the §23.10-§23.11.2 section read (main member L6434-L6548).

Chat 97.  Imports heading_line / section_span / has_token / enclosing from r2lib by path.

Reads the six volume MEMBERS, never a BUILDnnn bundle path.  Chat 96's r2-ch14l and r2-ch14m
opened '/home/claude/The_Method_1_6_BUILD124_compendia_papers_audits.md' by name and both died at
this chat's gate; a member is a stable object and a bundle is not, and a bundle also comes to
contain the instrument's own banked output, so a whole-bundle census cannot reproduce.
"""
import importlib.util, re

_s = importlib.util.spec_from_file_location('r2lib', '/home/claude/members/r2lib.py')
r2lib = importlib.util.module_from_spec(_s); _s.loader.exec_module(r2lib)
heading_line, section_span, has_token, enclosing = (
    r2lib.heading_line, r2lib.section_span, r2lib.has_token, r2lib.enclosing)

D = '/home/claude/members/'
VOL = {'main': 'The_Method_1_6-2.md',
       'Register': 'The_Method_1_6___The_Register-2.md',
       'Math': 'The_Method_1_6___Mathematical_Compendium-2.md',
       'Phys': 'The_Method_1_6___The_Physics_Compendium-2.md',
       'IoI': 'The_Method_1_6___The_Index_of_Indices-2.md',
       'Spectra': 'The_Method_1_6___Spectra_Compendium-2.md'}
L = {k: open(D + v, encoding='utf-8').read().split('\n') for k, v in VOL.items()}
TXT = {k: '\n'.join(v) for k, v in L.items()}
M = L['main']


def body(vol, sec):
    sp = section_span(L[vol], sec)
    return (sp, '\n'.join(L[vol][sp[0]:sp[1] - 1])) if sp else (None, '')


def sites(vol, pat, flags=0):
    return [i + 1 for i, t in enumerate(L[vol]) if re.search(pat, t, flags)]


print('== the section pointers (L6501, L6517, L6531, L6477) ==')

sp13, b13 = body('main', '23.13')
toks13 = {t: has_token(b13, t) for t in ('nu_V', 'curvature', 'spacing', 'admissible', 'admissibility')}
print('  14o-01  L6501 "23.13 gives r >= 5 for the spacing and nu_V for the curvature" — 23.13 is',
      '"%s", L%d-L%d.' % (M[sp13[0] - 1].strip('# ').strip(), sp13[0], sp13[1] - 1))
print('          in 23.13\'s body: "nu_V" %d, "curvature" %d, "spacing" %d, "admissible" %d, "5" as a'
      % (b13.count('ν_V'), toks13['curvature'], toks13['spacing'], toks13['admissible']),
      'bare token %d ; the literal "r >= 5" (any spacing/glyph) %d'
      % (has_token(b13, '5'), len(re.findall(r'r\s*[>≥]=?\s*5', b13))))
r5 = [(k, [i for i in sites(k, r'r\s*[>≥]=?\s*5')]) for k in VOL]
print('          the claim\'s real home, all six volumes, "r >= 5":',
      '; '.join('%s %s' % (k, v if v else 'none') for k, v in r5))
nuv = [(k, len(sites(k, 'ν_V'))) for k in VOL]
print('          "nu_V" site counts by volume:', ', '.join('%s %d' % (k, n) for k, n in nuv))

sp11, b11 = body('main', '23.11')
sp104, b104 = body('main', '23.10.4')
voc = ('ceiling', 'granularity', 'quotation', 'curvature', 'resolve', 'unresolved')
print('  14o-02  chat 95\'s 14k-01 re-tested: 23.11 (L%d-L%d) against 23.10.4 (L%d-L%d), word-bounded'
      % (sp11[0], sp11[1] - 1, sp104[0], sp104[1] - 1))
print('          23.11   : nu_V %d, %s' % (b11.count('ν_V'), ', '.join('%s %d' % (t, has_token(b11, t)) for t in voc)))
print('          23.10.4 : nu_V %d, %s' % (b104.count('ν_V'), ', '.join('%s %d' % (t, has_token(b104, t)) for t in voc)))

for ln in (6270, 6923):
    print('  14o-03  citing site L%d (%s): %s' % (ln, enclosing(M, ln), M[ln - 1].strip()[:150]))

sp255, b255 = body('main', '25.5')
print('  14o-04  L6517 "supersedes 25.5\'s 1,061 order-1 bounds" — 25.5 is L%d-L%d; "1,061" appears'
      % (sp255[0], sp255[1] - 1), 'in it %d time(s); "1,061" across the main volume at %s'
      % (b255.count('1,061'), sites('main', r'1,061') or 'no line'))
print('          "499" in 25.5: %d ; "order-1"/"order 1" in 25.5: %d'
      % (has_token(b255, '499'), len(re.findall(r'order[- ]1\b', b255))))

sp167, b167 = body('main', '16.7.1')
print('  14o-05  L6531 "16.7.1 makes the same move for a different pair" — 16.7.1 is "%s", L%d-L%d;'
      % (M[sp167[0] - 1].strip('# ').strip(), sp167[0], sp167[1] - 1),
      '"whole" %d, "structure" %d, "cell" %d, "pair" %d'
      % tuple(has_token(b167, t) for t in ('whole', 'structure', 'cell', 'pair')))

prop = sites('main', r'Proposition 23\.1\b')
print('  14o-06  L6477 "Proposition 23.1\'s floor applies to the classical bracket only" —',
      'Proposition 23.1 stated/cited at main L%s' % prop)
for ln in prop[:3]:
    print('          L%-6d %s' % (ln, M[ln - 1].strip()[:130]))

print()
print('== the Register citations of L6455 and L6484 ==')
for n in (96, 97, 98):
    h = heading_line(L['Register'], str(n))
    seg = '\n'.join(L['Register'][h:h + 3]) if h else ''
    print('  14o-07  Register %d at L%s: %s' % (n, h, ' / '.join(x.strip() for x in seg.split('\n') if x.strip())[:170]))

print()
print('== named objects and vocabulary ==')

q9 = sites('main', r'\bQ9\b')
print('  14o-08  L6453 "Q9\'s conclusion — bounds becoming relatively worthless as data accumulates" —',
      '"Q9" at main L%s' % (q9[:8] if q9 else 'no line'))
if q9:
    print('          first site: %s' % M[q9[0] - 1].strip()[:150])

verdicts = ('exact', 'a smooth channel', 'a bifurcation', 'an oscillation', 'chaotic')
print('  14o-09  L6539 gives Li I np the verdict "repeated structure"; the classifier at L6523-L6529',
      'offers %d verdicts: %s' % (len(verdicts), ', '.join(verdicts)))
print('          "repeated structure" elsewhere in the main volume: %s ; in all six volumes: %s'
      % (sites('main', r'repeated structure') or 'this site only',
         {k: len(sites(k, r'repeated structure')) for k in VOL}))

ga = sites('main', r'Ga I\b')
print('  14o-10  Ga I in the main volume at L%s' % ga[:12])
for ln in ga[:6]:
    print('          L%-6d %s  %s' % (ln, enclosing(M, ln), M[ln - 1].strip()[:110]))

print()
print('== production and convention in the read window (L6434-L6548) ==')

win = M[6433:6548]
brk = [(6434 + i, t.strip()) for i, t in enumerate(win)
       if re.match(r'^\s*(d|rs|s)\s*$', t) and t.strip()]
print('  14o-11  single-fragment lines inside tables (a word broken across the line):',
      '; '.join('L%d "%s"' % x for x in brk) or 'none')
pipe = sum(1 for t in win if t.strip().startswith('|'))
print('          table conventions in the window: %d pipe-table lines against space-aligned blocks at'
      % pipe, 'L6459-L6465, L6523-L6529 and L6535-L6539 — both conventions inside 115 lines')
print('  14o-12  L6443 display line, verbatim: %s' % M[6442].strip())
print('          two sentences are run together at "above n k+1+m even"; the break is missing, and',
      '"Odd" on the next line has no subject')

edit = [(6434 + i, t.strip()[:100]) for i, t in enumerate(win)
        if re.search(r'earlier (draft|version)|is withdrawn|correction \d', t)]
print('  14o-13  Ruling 45 class (build/editorial remarks in a reader-facing volume):')
for ln, t in edit:
    print('          L%-6d %s' % (ln, t))

print()
print('== figures restated from elsewhere ==')
for fig in ('0.6779', '1,585', '619', '0.362', '25.96', '0.0164'):
    hits = {k: sites(k, re.escape(fig)) for k in VOL}
    hits = {k: v for k, v in hits.items() if v}
    print('  14o-14  "%s": %s' % (fig, '; '.join('%s L%s' % (k, v[:6]) for k, v in hits.items()) or 'nowhere'))

print()
print('== the three-part cost claim of L6495 ==')
print('  14o-15  L6495 "pays in robustness, domain and resolution" — three costs named; the table',
      'above it (L6489-L6493) carries three rows: bracket width, displacement tolerated, cells from')
print('          a 10-member channel.  "domain" as a word in 23.10.3: %d ; the row that would carry'
      % has_token('\n'.join(M[6485:6499]), 'domain'),
      'it is the cells row, which L6495 also reads as resolution')

figs = sorted(set(re.findall(r'Figure 23\.\d+', TXT['main'])))
print('  14o-16  figures named in the main volume for chapter 23: %s ; Figure 23.3 asset line at L%s'
      % (', '.join(figs), sites('main', r'figures/figure-23\.3\.png')))
