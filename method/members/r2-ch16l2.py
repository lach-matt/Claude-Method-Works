
# r2-ch16l2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch16l.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (14 anchors); nothing else changes. r2-ch16l.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 90+184 — reproduces r2-ch16l.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
"""r2-ch16l --- PROSE batch, chat 120, main L8790-L8888 (ch.32 head, 32.1, 32.1.1).

Every pointer under BOTH resolvers and resolved to the CLAIM; the count words of the chapter head
against their own targets; Appendix E's item count against the head's *eight items*; the
attributions against the BODY occurrence of ## References and against R.7, and the reverse; the
out-of-unit sites a numeral sweep places; Rulings 45 and 46 case-sensitively in one pass; the
duplicated-section sweep; census rows in range; first-person prose; and Prints & Proofs anchored
witness by witness on its own text.
"""
import importlib.util, re

spec = importlib.util.spec_from_file_location('r2lib', '/home/claude/members/r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing

LO, HI = _L(' Everything the collection was built to settle is settled. The census is complete at 23 core types; the', -1), _L(' index does not carry. It is Q item D, and the largest unchecked number in the book.', 1)
VOL = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
       'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
       'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
       'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
       'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
V = {k: open('/home/claude/members/' + f, encoding='utf-8').read().split('\n') for k, f in VOL.items()}
M = V['main']
PP = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')
SEG = M[LO - 1:HI]


def body_range(Mx, sec):
    """[start, end) of a section's OWN body.  Owed to r2lib; provenance chat 108."""
    s = heading_line(Mx, sec)
    if s is None:
        return None
    for i in range(s + 1, len(Mx) + 1):
        if re.match(r'^#{1,4} ', Mx[i - 1].strip()):
            return (s, i)
    return (s, len(Mx) + 1)


def last_md_heading(Mx, title):
    """LAST line whose heading text is exactly `title` --- the BODY occurrence.  Owed to r2lib."""
    hits = [i for i, t in enumerate(Mx, 1)
            if re.match(r'^#{1,4}\s+' + re.escape(title) + r'\s*$', t.strip())]
    return hits[-1] if hits else None


def lettered_heading(Mx, label):
    hits = [i for i, t in enumerate(Mx, 1)
            if re.match(r'^#{1,4}\s+' + re.escape(label) + r'[ .]', t.strip())]
    return hits[-1] if hits else None


def phrase(Lx, pat, lo=1, hi=None):
    hi = hi or len(Lx) + 1
    return [i for i in range(lo, min(hi, len(Lx) + 1)) if re.search(pat, Lx[i - 1], re.I)]


print('=== A. every pointer in the unit, both resolvers, resolved to the CLAIM ===')
ptr = sorted({m.group(1) for t in SEG for m in re.finditer(r'§(\d+(?:\.\d+)*)(?!\d)(?!\.\d)', t)})
lettered = sorted({m.group(1) for t in SEG for m in re.finditer(r'§([A-Z]\.\d+(?:\.\d+)*)', t)})
print('  numeric pointers:', ptr)
print('  lettered pointers:', lettered)
for s in ptr:
    br, sp = body_range(M, s), section_span(M, s)
    print('  §%-8s body_range %-16s section_span %-16s %s'
          % (s, br, sp, 'coincide' if br == sp else 'DIFFER'))
for s in lettered:
    h = lettered_heading(M, s)
    print('  §%-8s lettered heading L%s' % (s, h))

print('=== B. the claims those pointers are cited FOR ===')
checks = [('16.4', r'at or before|support.*before|precede'),
          ('18.4.1', r'certificate'),
          ('7.4', r'presentation choice|caps'),
          ('12.11.5', r'four-cap|cap sweep|enlarge'),
          ('12.11.6', r'calibrat|veto'),
          ('2.18', r'decision|decide'),
          ('2.21', r'build readout|readout'),
          ('29.11', r'Bergman|double-projection'),
          ('29.12', r'2-decomposab|decomposab'),
          ('25.6.3', r'withdr|prediction'),
          ('32.2', r'reconstruct|S3'),
          ('31.3.4', r'Kreuzer|Skarke|540'),
          ('32.6', r'condition 1|reference integrity|three conditions')]
for sec, pat in checks:
    br = body_range(M, sec)
    if br is None:
        print('  §%-8s HEADING ABSENT  ---  claim /%s/ cannot resolve' % (sec, pat[:26]))
        continue
    hits = phrase(M, pat, br[0] + 1, br[1])
    sp = section_span(M, sec)
    wide = phrase(M, pat, sp[0] + 1, sp[1]) if sp else []
    print('  §%-8s body %s  own-body hits %s  chapter-span hits %d'
          % (sec, br, hits[:4], len(wide)))

print('=== C. Chapter-level pointers of the head ===')
for lbl, pat in (('Chapter 14', r'^## 14\.'), ('Chapter 15', r'^## 15\.'), ('Chapter 17', r'^## 17\.'),
                 ('Chapter 6', r'^## 6\.'), ('Chapter 25', r'^## 25\.'), ('Chapter 30', r'^## 30\.'),
                 ('Chapter 32', r'^## 32\.')):
    occ = [i for i, t in enumerate(M, 1) if re.match(pat, t)]
    print('  %-11s occurrences %s  (BODY = last)' % (lbl, occ))
print('  L8838 calls Chapter 30 "the missing Chapter 30" --- it is present at the BODY line above')

print('=== D. the head\'s three count words against their targets ===')
print('  -- "23 core types" --')
for k in ('main', 'reg', 'ioi'):
    h = [i for i in phrase(V[k], r'(?<![\d.,])23(?!\d)[^.]{0,24}core type|core type', 1) if True]
    print('    %-4s %s' % (k, h[:8]))
print('  -- "the four decline modes each have a worked case" --')
dm = phrase(M, r'decline mode')
print('    decline-mode sites: %s' % dm[:12])
print('  -- the three parked questions, resolved in Chapters 15 and 17 --')
for term in (r'C\u2086 density|C6 density', r'antiprotonic', r'isoelectronic law'):
    s = phrase(M, term)
    ch = []
    for i in s:
        prev = [j for j in range(i, 0, -1) if re.match(r'^## \d+\.', M[j - 1])]
        ch.append(re.match(r'^## (\d+)\.', M[prev[0] - 1]).group(1) if prev else '?')
    print('    %-22s %d sites, chapters %s' % (term[:22], len(s), sorted(set(ch))))
print('  -- "eight items" in Appendix E (L8794) against Appendix E itself --')
for i in (_L(" Serving PART VI — THE RECORD AND THE REACH. The book's own ignorance as a closed index — fourteen items,"), _L(' ten of them open, four ordered coordinates, one categorical fibre, E(Q) = 0 fibred by domain at the'), _L(' nine items; eight closed at E(Q) = 0 with four entered by §12.11.7; thirteen — are kept there as history.'), _L(' replacing it, so this appendix carried **three live item counts** — eight at E.4, fifteen here, and'), _L('### E.1.2 The open set as this session leaves it — ten open of 14, listed'), _L('### E.4.1 Q, enumerated and closed at eight')):
    print('    L%d %s' % (i, M[i - 1].strip()[:100]))

print('=== E. attributions against ## References BODY occurrence and R.7 ===')
ref = last_md_heading(M, 'References')
r7 = lettered_heading(M, 'R.7')
print('  ## References BODY L%s ; R.7 L%s' % (ref, r7))
names = ['Bergman', 'Baker', 'Pixley', 'Kreuzer', 'Skarke']
for n in names:
    inbib = [i for i in phrase(M, r'(?<![A-Za-z])' + n, ref, len(M) + 1)] if ref else []
    inunit = [i for i in range(LO, HI + 1) if re.search(r'(?<![A-Za-z])' + n, M[i - 1])]
    print('  %-8s unit %s   bibliography %s' % (n, inunit, inbib[:6] or 'ABSENT'))
print('  reverse: bibliography entries naming §32.1.1 or chapter 32')
if ref:
    print('   ', [i for i in range(ref, len(M) + 1) if re.search(r'§32\.1\.1|§32\b', M[i - 1])][:8])

print('=== F. Rulings 45 and 46 in one pass, case-sensitive ===')
r45 = [(LO + i, t.strip()[:82]) for i, t in enumerate(SEG)
       if re.search(r'at this build|this build|first reading|the reading this section was written on'
                    r'|a single late session|recomputed at|earlier drafts|this session', t, re.I)]
r46 = [(LO + i, t.strip()[:82]) for i, t in enumerate(SEG)
       if re.search(r'\b\w+\.py\b|BUILD\d+|\.md\b|\.tsv\b', t)]
print('  Ruling 45 candidate sites: %d' % len(r45))
for l, t in r45:
    print('    L%d %s' % (l, t))
print('  Ruling 46 sites: %d' % len(r46))
for l, t in r46:
    print('    L%d %s' % (l, t))

print('=== G. out-of-unit sites the numeral sweep placed ===')
for k, lines in (('main', [_L(" 153–162. — the unbounded forbidden submatrices; §30.3's obstruction route closes on them."), _L(' · Saari, D. G. (1971). *Trans. AMS* **162**, 267; (1973) **181**, 351; (1984) *J. Diff. Eq.* **55**, 300. — collisions improbable; the strata disjoint up to measure zero.'), _L(" **The companions' own bibliographies.** The Mathematical Compendium names a work for every one of its", 1)]), ):
    for i in lines:
        print('  main L%d %s' % (i, V[k][i - 1].strip()[:104]))
for i in (_L(' the two tables an hour earlier. Run against the book as it stood this morning it would have failed'), _L(' twice. Register 379.', 1), _L('| level | base | fibre |', 1)):
    print('  reg  L%d %s' % (i, V['reg'][i - 1].strip()[:104]))

print('=== H. duplicated-section sweep, first-person prose, census rows ===')
longs = [t.strip() for t in SEG if len(t.strip()) > 70]
dup = 0
for t in longs:
    hits = sum(1 for k in V for u in V[k] if t in u)
    if hits > 1:
        dup += 1
        print('  RECURS: %s' % t[:70])
print('  long lines %d, recurring elsewhere %d' % (len(longs), dup))
fp = [(LO + i, t.strip()[:70]) for i, t in enumerate(SEG)
      if re.search(r'(?<![A-Za-z])(I|we|my|our)(?![A-Za-z])', t)]
print('  first-person candidates: %s' % ([l for l, _ in fp] or 'none'))
rows = [l for l in open('/home/claude/members/DEFECT-CENSUS.tsv', encoding='utf-8').read().split('\n')[1:] if l.strip()]
hdr = open('/home/claude/members/DEFECT-CENSUS.tsv', encoding='utf-8').read().split('\n')[0].split('\t')
mi, li = hdr.index('member'), hdr.index('line')
inr = [r for r in rows if r.split('\t')[mi] in ('main', 'all')
       and r.split('\t')[li].isdigit() and LO <= int(r.split('\t')[li]) <= HI]
print('  census rows in range (classes main AND all): %d' % len(inr))
for r in inr[:6]:
    print('   ', r[:110])

print('=== I. Prints & Proofs, anchored witness by witness ===')
for probe in ('What a referee would flag', 'The book is an index', 'The law applied to this book',
              'The object does not contain the demonstration', 'The 540 remain unverified',
              'bookindex.py', 'thirty-five chapters and six appendices', 'Three hundred and sixty-eight'):
    p = [i for i, t in enumerate(PP, 1) if probe in t]
    m = [i for i, t in enumerate(M, 1) if probe in t]
    off = [a - b for a, b in zip(p, m)] if p and m else []
    print('  %-46s main %s  PP %s  offset %s' % (probe[:46], m[:3], p[:3] or 'ABSENT', off[:3]))
