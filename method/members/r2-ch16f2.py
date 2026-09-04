
# r2-ch16f2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch16f.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (24 anchors); nothing else changes. r2-ch16f.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 90+184 — reproduces r2-ch16f.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
"""r2-ch16f --- PROSE batch, chat 118, main L8575-L8699 (§30.4 - §31.2.5).

Pointers under both resolvers, count words against their own bodies, attributions against the
BODY occurrence of ## References and R.7, register citations grouped-aware, a digit-bounded
numeral SITE sweep, Rulings 45/46, the duplicated-section sweep, and Prints & Proofs anchored
on its own text.  r2lib by path; members read, never a bundle.
"""
import importlib.util, re

spec = importlib.util.spec_from_file_location('r2lib', '/home/claude/members/r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing

LO, HI = _L('### 30.4 The lists this work enumerated once'), _L("    exponential degeneracy and a limiting temperature. Λ's finiteness is what capping buys.", 1)
VOL = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
       'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
       'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
       'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
       'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
V = {k: open('/home/claude/members/' + f, encoding='utf-8').read().split('\n') for k, f in VOL.items()}
M = V['main']
R = V['reg']
PP = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')
NUMB = r'(?<![\d.,])%s(?!\d)(?!,\d)(?!\.\d)'          # both boundaries corrected, chats 116-117


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


def stemlines(L, s):
    """Left-bounded only: has_token is letter-bounded on BOTH sides.  Provenance chat 113."""
    return [i for i, t in enumerate(L, 1) if re.search(r'(?<![A-Za-z])' + re.escape(s), t, re.I)]


def numsites(pat):
    """Every SITE of a numeral, six volumes.  A count alone cannot be witnessed."""
    out = {}
    for k, L in V.items():
        s = [i for i, t in enumerate(L, 1) if re.search(NUMB % re.escape(pat), t)]
        if s: out[k] = s
    return out


def reg_entry(num):
    """Grouped-aware Register lookup.  heading_line fails on the Register's bare '### 96'."""
    exact = [i for i, t in enumerate(R, 1) if re.match(r'^#{1,4}\s*%s\s*$' % num, t.strip())]
    if exact:
        return exact[-1], 'exact'
    for i, t in enumerate(R, 1):
        m = re.match(r'^#{1,4}\s*(\d+)\s*[-\u2013]\s*(\d+)\s*$', t.strip())
        if m and int(m.group(1)) <= int(num) <= int(m.group(2)):
            return i, 'grouped %s-%s' % (m.group(1), m.group(2))
    return None, 'ABSENT'


print('=' * 100)
print('r2-ch16f  PROSE  chat 118  main L%d-L%d  (§30.4 - §31.2.5)' % (LO, HI))
print('=' * 100)

# ------------------------------------------------------------------ 1. pointers
print('\n## 1  EVERY §-POINTER IN THE UNIT, under body_range AND section_span, resolved to the CLAIM')
ptr = []
for i in range(LO, HI + 1):
    for m in re.finditer(r'§(\d+(?:\.\d+)*)(?!\d)(?!\.\d)', M[i - 1]):
        ptr.append((i, m.group(1)))
    for m in re.finditer(r'§([A-Z]\.\d+(?:\.\d+)*)', M[i - 1]):
        ptr.append((i, m.group(1)))
print('   pointer sites: %d  %s' % (len(ptr), ptr))
CLAIM = {
    '30.2': ('the structural invariants the row says omitted six', ['invariant', 'structur']),
    '31.1': ('the celestial objects list', ['celestial', 'Lagrange', 'Hill']),
    '31.2': ('the string objects list', ['string', 'Regge', 'degenerac']),
    '31.3': ('the Calabi-Yau statistic and its denominator', ['Pareto', 'denominator', 'Calabi']),
    '2.10': ('the rule the section quotes: "enumerate targets before searching"',
             ['enumerate', 'target', 'search']),
    '16.7.1': ('E(X) recovering an order cut at 7/8 from occupancy alone',
               ['occupancy', 'E(X)', '7/8', 'resonance']),
    '23.14.1': ('a capacity bound the +0.86 log-log slope is said to instance',
                ['capacity', 'bound', 'log']),
    '18.5': ('what the pole is --- the claim §31.1.1 says it CORRECTS',
             ['pole', 'worthless', 'unnecessary', 'bracket']),
    '23.10.1': ('a bracket at any order needs a KNOWN sign, not a positive one',
                ['sign', 'known', 'positive', 'bracket']),
    '11.7': ('three conditions with independence as their degenerate case',
             ['condition', 'independen', 'degenerate']),
    '30.4': ('the search targets the row says omitted 7 + 9', ['target', 'search', 'relation']),
}
for sec, (claim, toks) in CLAIM.items():
    br, sp = body_range(M, sec), section_span(M, sec)
    print('\n   §%-8s body_range %-16s section_span %-16s  %s'
          % (sec, br, sp, 'COINCIDE' if br == sp else 'DIFFER'))
    print('      claim sought: %s' % claim)
    for nm, rng in (('body', br), ('span', sp)):
        if rng is None:
            print('      %s: heading NOT FOUND' % nm); continue
        txt = '\n'.join(M[rng[0]:rng[1] - 1])          # excludes the heading line
        hits = {t: len(re.findall(re.escape(t), txt, re.I)) for t in toks}
        print('      %s L%d-L%d  token hits %s' % (nm, rng[0], rng[1] - 1, hits))
    if br:
        print('      first body lines: %s' % ' | '.join(t.strip()[:74] for t in M[br[0]:br[0] + 3] if t.strip())[:190])

# ------------------------------------------------------------------ 1b. full reads
print('\n## 1b  THE PROBE-NEGATIVE TARGETS, READ IN FULL (a token probe is not a reading)')
for sec, why in (('18.5', 'L8639 says §31.1.1 CORRECTS it: "the pole is where a bracket becomes '
                          'unnecessary, not worthless"'),
                 ('16.7.1', 'L8632 cites it for "E(X) recovers the order cut at 7/8 from occupancy alone"'),
                 ('11.7', 'L8683 cites "§11.7\'s three conditions"')):
    br = body_range(M, sec)
    print('\n   ----- §%s  L%d-L%d  ----- %s' % (sec, br[0], br[1] - 1, why))
    for i in range(br[0], br[1]):
        if M[i - 1].strip():
            print('      L%d %s' % (i, M[i - 1].rstrip()[:112]))

# ------------------------------------------------------------------ 2. the Chapter 36 promise
print('\n## 2  L8648 promises Chapter 36 COMPLETES the celestial reading --- read the target')
c36 = None
for i, t in enumerate(M, 1):
    if re.match(r'^##\s+36\.', t.strip()):
        c36 = i
print('   ## 36. body occurrence: L%s' % c36)
if c36:
    end = next((i for i in range(c36 + 1, len(M) + 1) if re.match(r'^##\s', M[i - 1].strip())), len(M) + 1)
    txt = '\n'.join(M[c36:end - 1])
    print('   chapter 36 spans L%d-L%d (%d lines); heading: %s' % (c36, end - 1, end - c36, M[c36 - 1].strip()))
    for t in ('famil', 'index', 'closure', 'closes', 'Poincar', 'Lagrange', 'chaos', 'chaotic'):
        print('      %-10s %d hits' % (t, len(re.findall(t, txt, re.I))))
    subs = [(i, M[i - 1].strip()) for i in range(c36, end) if re.match(r'^###\s', M[i - 1].strip())]
    print('   subsections: %s' % [s for _, s in subs][:8])
    print('   the promise is "the families are indexed, the index closes, and the closure is the')
    print('   reason nothing here touches Poincare" --- the target lines that carry it:')
    for i in range(c36, end):
        if re.search(r'famil|closes|closure|Poincar|chaotic', M[i - 1], re.I) and M[i - 1].strip():
            print('      L%d %s' % (i, M[i - 1].strip()[:110]))

print('\n   L8639 announces "Which corrects §18.5" --- is that correction RECORDED anywhere?')
for i, t in enumerate(R, 1):
    if re.search(r'18\.5(?!\d)', t) and re.search(r'pole|worthless|unnecessary', t, re.I):
        print('      reg L%d %s' % (i, t.strip()[:110]))
print('      Register lines naming §18.5 at all: %s'
      % [i for i, t in enumerate(R, 1) if re.search(r'§18\.5(?!\d)', t)])
print('      §18.5 body L5294-L5302 carries no forward notice: "corrects" sites in it = %d'
      % len([i for i in range(_L('### 18.5 The pole'), _L('### 18.6 E(X) is the prediction budget')) if re.search(r'correct', M[i - 1], re.I)]))

# ------------------------------------------------------------------ 3. count words
print('\n## 3  EVERY COUNT WORD, against its own body, its row labels and its numeral span')

print('\n   (a) L8588 "at least nine that are NOT [polynomial]" --- count the enumeration itself')
seg = [t for t in M[_L(' did not before — including V·e = w, w² = (16/3)·T·e and T·h² = eν²/3.', 1):_L(' was ever audited against any list.')] if t.strip()]
for i, t in enumerate(seg, _L(' Worse, the closure is over polynomial relations only. The book now states at least nine that are not:')):
    print('      L%d %s' % (i, t.strip()[:104]))
items = ['A^m(x^p)', 'V = 2/tanh(kh/2)', 'self-concordance', 'the modular rank law',
         'Sigma_q||A_q||.||B_q|| = |Lambda|', 'F(-1) = 2', 'E(X) as non-pairwise content',
         'the reorderability theorem']
print('      MEASURED items in the list: %d --- %s' % (len(items), items))
print('      printed count word: "at least nine"')

print('\n   (b) L8597 "This chapter contains five enumerations" --- against the rows\' own sections')
rows = [t for t in M[_L(' This chapter contains five enumerations, and every one was made once:', 1):_L("  §31.3's statistic                           stated against the wrong denominator", 1)] if t.strip()]
for i, t in enumerate(M[_L(' This chapter contains five enumerations, and every one was made once:', 1):_L("  §31.3's statistic                           stated against the wrong denominator", 1)], _L('  the list                                    what it omitted')):
    if t.strip(): print('      L%d %s' % (i, t.strip()[:100]))
print('      row sections: %s' % re.findall(r'§(\d+(?:\.\d+)*)', '\n'.join(rows)))
print('      chapter of the sentence: enclosing(L8597) = %s' % (enclosing(M, _L(' This chapter contains five enumerations, and every one was made once:')),))
print('      chapter 30 span = %s ; chapter 31 span = %s' % (section_span(M, '30'), section_span(M, '31')))
print('      rows whose section lies OUTSIDE chapter 30: ', end='')
c30 = section_span(M, '30')
out = []
for s in re.findall(r'§(\d+(?:\.\d+)*)', '\n'.join(rows)):
    hl = heading_line(M, s)
    if hl and not (c30[0] <= hl < c30[1]): out.append((s, hl))
print(out)
print('      column header is "what it omitted"; row 5 reads: %s'
      % [t.strip()[:80] for t in rows if '31.3' in t])

print('\n   (c) L8611 "four subjects it was not built for" --- against chapter 31\'s own sections')
c31 = section_span(M, '31')
subs = [(i, M[i - 1].strip()) for i in range(c31[0], c31[1]) if re.match(r'^###\s+31\.\d+\s', M[i - 1].strip())]
print('      chapter 31 top-level sections: %s' % [s[4:44] for _, s in subs])

print('\n   (d) other count words in the unit')
for ln, word in ((_L(' The relation set has grown since. Closing the eight polynomial relations the book now states gives a'), 'eight'), (_L(' Gröbner basis of 18 where the original four gave 6, and seven further relations reduce to zero that'), '18'), (_L(' Gröbner basis of 18 where the original four gave 6, and seven further relations reduce to zero that'), 'seven'), (_L("  Lagrange L1, L2, L3 in μ (Euler's        monotone, convex, 3-monotone; 18 of 18 containments at orders 1–3"), '18 of 18'),
                 (_L("  satellite counts vs Hill radius          log–log +0.86 across six planets — §23.14.1's capacity bound"), 'six planets'), (_L('### 31.2.1 Three objects on the pole'), 'Three objects'), (_L(" only along a tree. §11.7's three conditions have independence as their degenerate case."), 'three conditions')):
    print('      L%d  %-12s : %s' % (ln, word, M[ln - 1].strip()[:96]))
sp117 = body_range(M, '11.7')
if sp117:
    txt = '\n'.join(M[sp117[0]:sp117[1] - 1])
    print('      §11.7 body L%d-L%d, %d non-blank lines; enumerated items:'
          % (sp117[0], sp117[1] - 1, len([t for t in M[sp117[0]:sp117[1] - 1] if t.strip()])))
    for i in range(sp117[0], sp117[1] - 1):
        if re.match(r'^\s*(\(?[a-c1-3][\).]|[-*])\s', M[i]):
            print('         L%d %s' % (i + 1, M[i].strip()[:88]))

# ------------------------------------------------------------------ 4. register citation
print('\n## 4  REGISTER CITATIONS in the unit, grouped-aware, existence first')
cites = []
for i in range(LO, HI + 1):
    for m in re.finditer(r'[Rr]egister[s]?\s+(\d+)', M[i - 1]):
        cites.append((i, m.group(1)))
print('   sites: %s' % cites)
for ln, num in cites:
    where, how = reg_entry(num)
    print('   register %s cited at L%d -> %s (%s)' % (num, ln, where, how))
    if where:
        for j in range(where, min(where + 6, len(R))):
            if R[j].strip():
                print('        R L%d  %s' % (j + 1, R[j].strip()[:104]))

# ------------------------------------------------------------------ 5. attributions
print('\n## 5  EVERY ATTRIBUTION IN THE UNIT against ## References BODY and R.7')
refs = last_md_heading(M, 'References')
r7 = lettered_heading(M, 'R.7')
print('   ## References BODY occurrence L%s (all occurrences %s);  R.7 at L%s'
      % (refs, [i for i, t in enumerate(M, 1) if re.match(r'^#{1,4}\s+References\s*$', t.strip())], r7))
reftxt = '\n'.join(M[refs:]) if refs else ''
r7txt = '\n'.join(M[r7:]) if r7 else ''
NAMES = ['Poincar', 'Lagrange', 'Euler', 'Mardling', 'Aarseth', 'Hill', 'Roche', 'Titius', 'Bode',
         'Rydberg', 'Regge', 'Hagedorn', 'Sperner', 'Dilworth', 'Groebner', 'Gröbner', 'Nesterov']
for nm in NAMES:
    u = [i for i in range(LO, HI + 1) if re.search(nm, M[i - 1], re.I)]
    if not u: continue
    six = {k: len([i for i, t in enumerate(L, 1) if re.search(nm, t, re.I)]) for k, L in V.items()}
    print('   %-10s unit %s   References %d   R.7 %d   six-volume sites %s'
          % (nm, u, len(re.findall(nm, reftxt, re.I)), len(re.findall(nm, r7txt, re.I)),
             {k: v for k, v in six.items() if v}))

# ------------------------------------------------------------------ 6. Rulings 45 and 46
print('\n## 6  RULING 45 (build/editorial-process prose) and RULING 46 (script names, build numbers)')
R45 = ['an earlier version', 'an earlier draft', 'a previous draft', 'this book', 'was tried',
       'is now', 'recorded at register', 'now states', 'from recollection', 'the audit itself',
       'was run once', 'has grown since', 'the book now states']
for p in R45:
    s = [i for i in range(LO, HI + 1) if re.search(re.escape(p), M[i - 1], re.I)]
    if s: print('   R45  %-24s %s' % (p, s))
R46 = ['BUILD', 'gate.py', 'close.py', 'r2lib', 'r2-tools', '.py', 'chat ', 'HANDOFF']
for p in R46:
    s = [i for i in range(LO, HI + 1) if p in M[i - 1]]           # case-SENSITIVE
    if s: print('   R46  %-24s %s' % (p, s))
first = [i for i in range(LO, HI + 1) if re.search(r'(?<![A-Za-z])(I|we|my|our)(?![A-Za-z])', M[i - 1])]
print('   first-person sites (raw, before symbol filtering): %s' % first)
for i in first:
    print('      L%d %s' % (i, M[i - 1].strip()[:96]))

# ------------------------------------------------------------------ 7. numeral SITE sweep
print('\n## 7  DIGIT-BOUNDED NUMERAL SITE SWEEP, six volumes  (?<![\\d.,])N(?!\\d)(?!,\\d)(?!\\.\\d)')
nums = []
for i in range(LO, HI + 1):
    for m in re.finditer(r'(?<![\w.,])(\d[\d,]*(?:\.\d+)?)(?![\d,]*[\w])', M[i - 1]):
        nums.append(m.group(1))
seen = []
for n in nums:
    if n not in seen: seen.append(n)
print('   distinct numerals printed in the unit: %d' % len(seen))
for n in seen:
    if len(n) < 2 and n in '0123456789': continue
    st = numsites(n)
    tot = sum(len(v) for v in st.values())
    other = {k: v for k, v in st.items() if k != 'main'}
    mn = [i for i in st.get('main', []) if not (LO <= i <= HI)]
    print('   %-10s six-volume sites %-4d   main outside unit %s   other volumes %s'
          % (n, tot, mn[:8], {k: v[:5] for k, v in other.items()}))

# ------------------------------------------------------------------ 8. duplicated-section sweep
print('\n## 8  DUPLICATED-SECTION SWEEP (DEF-105 item 1): long lines of the unit, six volumes')
long = [(i, M[i - 1].strip()) for i in range(LO, HI + 1) if len(M[i - 1].strip()) >= 60]
dup = 0
for i, t in long:
    hits = []
    for k, L in V.items():
        for j, u in enumerate(L, 1):
            if u.strip() == t and not (k == 'main' and j == i):
                hits.append((k, j))
    if hits:
        dup += 1
        print('   L%d recurs at %s' % (i, hits))
print('   %d long lines swept, %d recur' % (len(long), dup))

# ------------------------------------------------------------------ 9. Prints & Proofs
print('\n## 9  PRINTS & PROOFS, anchored on its own text (never a single global offset)')
for probe in ('The target list for the novelty search', 'This chapter contains five enumerations',
              'The method was built on one index', 'Sensitive dependence destroys monotonicity',
              'mass sits in its nucleus', 'has second difference zero',
              'An earlier version of this line said convex', 'diverges above a limiting temperature',
              'the audit itself was run once', 'five lists in one chapter'):
    pp = [i for i, t in enumerate(PP, 1) if probe.lower() in t.lower()]
    mm = [i for i, t in enumerate(M, 1) if probe.lower() in t.lower()]
    print('   %-46s main %s   PP %s   offset %s'
          % (probe[:46], mm, pp, [p - m for m, p in zip(mm, pp)] if pp and mm else '--')) 

print('\n   docket 21 / 15h-12: the same "five lists" material is also printed at main L7634-L7635')
for i in range(_L(" published claim — and it was exhaustive search wearing the heuristic's name. It could not have"), _L(' written before the number above it was read.')):
    if M[i - 1].strip():
        print('      main L%d %s' % (i, M[i - 1].strip()[:110]))
for i in range(_L(' **69. *V*(δ) = *V*(*T*) taken too far.** True for the *ratio* under interpolation; **false for the width under extrapolation** — bracketing *T* for Sc VI is 129× worse than bracketing δ.'), _L('    the person operating it, which is what it was built to do.')):
    if i <= len(PP) and PP[i - 1].strip():
        print('      PP   P%d %s' % (i, PP[i - 1].strip()[:110]))

# ------------------------------------------------------------------ 10. census rows
print('\n## 10  CENSUS ROWS IN RANGE, measured from DEFECT-CENSUS.tsv on the `member` column')
import csv
rows = list(csv.DictReader(open('/home/claude/members/DEFECT-CENSUS.tsv', encoding='utf-8'), delimiter='\t'))
sel = [r for r in rows if r['member'] == 'main' and r['line'].isdigit() and LO <= int(r['line']) <= HI]
print('   %d rows in L%d-L%d' % (len(sel), LO, HI))
for r in sel:
    print('   %s  %s  L%s  item %r' % (r['id'], r['class'], r['line'], r['item']))
    print('        detail: %s' % r['detail'][:96])
    print('        line  : %s' % M[int(r['line']) - 1].strip()[:96])
print('\n' + '=' * 100)
print('end r2-ch16f')
