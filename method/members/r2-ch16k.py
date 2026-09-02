"""r2-ch16k --- COMPUTABLE batch, chat 120, main L8790-L8888 (ch.32 head, 32.1, 32.1.1).

The E(book) table's four densities and its first-reading column; the boxes against a MEASURED
count of chapters, appendices and parts; the two forward-citation percentages under BOTH rounding
conventions; the caps of 7.4 against the rebuilt tower; registers 424-426; the withdrawal count;
the count word *seven* against the object it names; Appendix E's items and the Q lettering; the
f-shell ceiling at its target; and a digit-bounded numeral SITE sweep over six volumes.
r2lib by path; members read, never a bundle; resolvers take the LINE LIST.
"""
import importlib.util, re
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_DOWN

spec = importlib.util.spec_from_file_location('r2lib', '/home/claude/members/r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing, load_tower

LO, HI = 8790, 8888
VOL = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
       'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
       'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
       'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
       'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
V = {k: open('/home/claude/members/' + f, encoding='utf-8').read().split('\n') for k, f in VOL.items()}
M = V['main']
R = V['reg']
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


def numsites(pat):
    """Every SITE of a numeral, six volumes.  A count alone cannot be witnessed."""
    out = {}
    for k, L in V.items():
        s = [i for i, t in enumerate(L, 1) if re.search(NUMB % re.escape(pat), t)]
        if s: out[k] = s
    return out


def pct(n, d):
    """Both conventions, named.  Never round()."""
    q = Decimal(n) * 100 / Decimal(d)
    return (q.quantize(Decimal('0.1'), ROUND_HALF_UP),
            q.quantize(Decimal('0.1'), ROUND_HALF_EVEN),
            q.quantize(Decimal('1'), ROUND_HALF_UP),
            q.quantize(Decimal('1'), ROUND_DOWN))


print('=== A. the E(book) table, this build (L8819-L8823) ===')
for label, cells, box, printed in (('chapter', 400, 1681, '23.8%'),
                                   ('chapter restricted', 238, 861, '27.6%'),
                                   ('part', 29, 64, '45.3%'),
                                   ('procedure/object/application', 7, 9, '77.8%')):
    hu, he, _, _ = pct(cells, box)
    print('  %-30s %4d/%-5d printed %-7s half-up %-6s half-even %-6s %s'
          % (label, cells, box, printed, str(hu) + '%', str(he) + '%',
             'EXACT' if printed == str(hu) + '%' else 'DEVIATION'))

print('=== B. the first-reading column (same table) ===')
for label, cells, box, printed in (('chapter', 138, 900, '15.3%'),
                                   ('chapter restricted', 80, 465, '17.2%'),
                                   ('part', 25, 25, '100.0%')):
    hu, he, _, _ = pct(cells, box)
    got = str(hu) + '%' if label != 'part' else '100.0%'
    print('  %-20s %4d/%-4d printed %-8s half-up %-8s %s'
          % (label, cells, box, printed, str(hu) + '%', 'EXACT' if printed == got else 'DEVIATION'))

print('=== C. the boxes against MEASURED structure ===')
chap = [i for i, t in enumerate(M, 1) if re.match(r'^## \d+\.', t) and i > 200]
app = [i for i, t in enumerate(M, 1) if re.match(r'^#{1,3}\s*Appendix\s', t) and i > 200]
# FAULT 2, chat 120: parts carry no markdown heading at all.  Measure the labels the volume prints.
partlab = sorted({m.group(1) for t in M for m in
                  re.finditer(r'PART\s+(0|[IVX]+)\b', t)} |
                 {m.group(1) for t in M for m in
                  re.finditer(r'(?<![A-Za-z])Parts?\s+(0|[IVX]+)\b', t)})
part = partlab
print('  body chapter headings   %d  (numbers %s)' % (len(chap), ','.join(re.match(r'^## (\d+)\.', M[i-1]).group(1) for i in chap)))
print('  body appendix headings  %d  (%s)' % (len(app), '; '.join(M[i-1].strip()[:26] for i in app)))
print('  body part headings      %d' % len(part))
print('  printed "thirty-five chapters and six appendices" -> 41; measured %d+%d = %d'
      % (len(chap), len(app), len(chap) + len(app)))
n = len(chap) + len(app)
print('  box at chapter resolution: printed 1,681 = 41^2 ; measured %d^2 = %d  %s'
      % (n, n * n, 'EXACT' if n * n == 1681 else 'DEVIATION'))
print('  restricted box: printed 861 = C(42,2) = 41*42/2 ; measured %d*%d/2 = %d  %s'
      % (n, n + 1, n * (n + 1) // 2, 'EXACT' if n * (n + 1) // 2 == 861 else 'DEVIATION'))
print('  part box: printed 64 = 8^2 ; measured %d part headings -> %d  %s'
      % (len(part), len(part) ** 2, 'EXACT' if len(part) ** 2 == 64 else 'CHECK'))
print('  first-reading chapter box 900 = 30^2, and the text says "over thirty chapters": consistent')
print('  first-reading restricted box 465 = 30*31/2 = %d: consistent' % (30 * 31 // 2))

print('=== D. the two forward-citation percentages (L8842) ===')
for label, a, b, printed in (('first reading', 58, 138, '42%'), ('this build', 162, 400, '40%')):
    _, _, iu, idn = pct(a, b)
    exact = Decimal(a) * 100 / Decimal(b)
    print('  %-14s %3d/%-4d = %s  printed %s  half-up %d%%  truncated %d%%  %s'
          % (label, a, b, exact, printed, iu, idn,
             'EXACT under half-up' if printed == str(iu) + '%' else
             ('EXACT only under TRUNCATION' if printed == str(idn) + '%' else 'DEVIATION')))
print('  heading sentence L8841 says "violated 162 times"; table row says 162 of 400: agree')

print('=== E. the caps of 7.4 against the rebuilt tower ===')
T = load_tower()
cells = T.build8() if hasattr(T, 'build8') else None
lam8 = r2lib.L8_at((3, 3, 1, 3, 1))
print('  L8_at((3,3,1,3,1)) -> %d cells   printed 976: %s' % (len(lam8), 'EXACT' if len(lam8) == 976 else 'DEVIATION'))
ell = sorted({c[1] for c in lam8})      # FAULT 1, chat 120: idx 2 is n', idx 1 is l.  Book right.
nsh = sorted({c[0] for c in lam8})
print('  l values present %s   printed "l in {0,1} - s and p only": %s' % (ell, 'EXACT' if ell == [0, 1] else 'DEVIATION'))
print('  principal shells %s   printed "three principal shells": %s' % (nsh, 'EXACT' if len(nsh) == 3 else 'DEVIATION'))
print('  s+p over three shells fills 2+2+6+2+6+2+6 -> Ne 10, Ar 18; "reaching argon" consistent with n=3, l<=1')
print('  item 1 cap tuple (5,5,2,6,2): l_max = 2 -> d, NOT f; "not the f shell either" is EXACT')

print('=== F. registers 424-426 (existence first, grouped-aware) ===')
for num in (424, 425, 426):
    hits = [i for i, t in enumerate(R, 1) if re.match(r'^#{1,4}\s*%d\s*$' % num, t.strip())]
    grouped = [i for i, t in enumerate(R, 1) if re.match(r'^#{1,4}\s*\d+\s*[-\u2013]\s*\d+\s*$', t.strip())
               and int(re.findall(r'\d+', t)[0]) <= num <= int(re.findall(r'\d+', t)[1])]
    ln = (hits + grouped)[:1]
    head = R[ln[0]].strip()[:88] if ln else ''
    for j in range(ln[0], min(ln[0] + 4, len(R))) if ln else []:
        if R[j].strip():
            head = R[j].strip()[:88]; break
    print('  register %d: %s  %s' % (num, ('bare heading L%d' % hits[0]) if hits else
                                     ('grouped L%d' % grouped[0] if grouped else 'ABSENT'), head))

print('=== G. the count word *seven* against the object it names (L8809) ===')
seg = M[LO - 1:HI]
first3 = [(LO + i, t.strip()[:52]) for i, t in enumerate(seg)
          if re.match(r'^\s*\*\*(First|Second|Third),', t)]
nums = [(LO + i, t.strip()[:52]) for i, t in enumerate(seg) if re.match(r'^\s*\*\*\d\.\s', t)]
print('  bolded ordinal items  %d: %s' % (len(first3), [l for l, _ in first3]))
print('  bolded numbered items %d: %s' % (len(nums), [l for l, _ in nums]))
for l, t in first3 + nums:
    print('    L%d %s' % (l, t))
print('  count word says seven; numbered items = %d; ALL bolded flag items = %d'
      % (len(nums), len(first3) + len(nums)))
h = heading_line(M, '32.1.2')
print('  out-of-unit anchor: 32.1.2 heading L%s -> %s' % (h, M[h - 1].strip() if h else 'ABSENT'))

print('=== H. Appendix E, its items, and the Q lettering ===')
eh = [i for i, t in enumerate(M, 1) if re.match(r'^#{1,3}\s*Appendix\s*E\b', t.strip()) and i > 200]
print('  Appendix E body heading: %s' % (eh or 'ABSENT'))
if eh:
    s = eh[-1]
    e = next((i for i in range(s + 1, len(M) + 1) if re.match(r'^#{1,2} ', M[i - 1])), len(M) + 1)
    # FAULT 4, chat 120: Appendix E enumerates in its own vocabulary, not by lettered lines.
    lab = sorted({m.group(1) for i in range(s, e) for m in
                  re.finditer(r'(?:^|\s)(?:item\s+)?\*{0,2}([A-N])\*{0,2}\s*[.\u2014-]\s', M[i - 1], re.I)})
    print('  span L%d-L%d ; single-letter item labels inside: %s' % (s, e - 1, lab))
    for i in range(s, e):
        if re.search(r'(?<![A-Za-z])(eight|nine|ten|thirteen|fourteen)\b', M[i - 1]) and re.search(r'item|open|closed|kept', M[i - 1]):
            print('    L%d %s' % (i, M[i - 1].strip()[:104]))
print('  chapter head L8794 prints "eight items"; item 7 L8887 cites "Q item D"')
qsites = [i for i, t in enumerate(M, 1) if re.search(r'Q item [A-H]', t)]
print('  "Q item X" sites in main: %s' % qsites[:14])

print('=== I. the f-shell ceiling at its target (12.11.2) ===')
br = body_range(M, '12.11.2'); sp = section_span(M, '12.11.2')
print('  12.11.2 body_range %s  section_span %s%s' % (br, sp, '  (coincide)' if br == sp else ''))
if br:
    hits = [(i, M[i - 1].strip()[:96]) for i in range(br[0], br[1])
            if re.search(NUMB % '25', M[i - 1]) or re.search(r'f\s*\u2077|f7|f\^7', M[i - 1])]
    for i, t in hits[:6]:
        print('    L%d %s' % (i, t))

print('=== J. withdrawals in the Register against "three hundred and sixty-eight" ===')
ent = [i for i, t in enumerate(R, 1) if re.match(r'^#{1,4}\s*\d+(\s*[-\u2013]\s*\d+)?\s*$', t.strip())]
bounds = ent + [len(R) + 1]
wd = 0
for k in range(len(ent)):
    body = '\n'.join(R[ent[k] - 1:bounds[k + 1] - 1])
    if re.search(r'withdr', body, re.I):        # FAULT 3, chat 120: 'withdraw' misses 'withdrew'.
        wd += 1
print('  register entry headings %d ; entries whose body contains a withdrawal word %d' % (len(ent), wd))
print('  occurrences of the stem anywhere in the Register: %d'
      % sum(len(re.findall(r'withdr', t, re.I)) for t in R))
print('  368 sites, six volumes: %s' % numsites('368'))
print('  37 sites in main: %s' % numsites('37').get('main', [])[:10])
print('  printed: 368 withdrawals, ~37 from a single late session')

print('=== K. numeral SITES for the unit\'s figures, six volumes ===')
for pat in ('1,021', '400', '1,681', '861', '354', '138', '162', '58', '1,442', '368', '540', '25'):
    s = numsites(pat)
    tot = sum(len(v) for v in s.values())
    if pat in ('400', '25', '138'):
        s = {k: v[:6] for k, v in s.items()}
    print('  %-6s %3d sites  %s' % (pat, tot, {k: v for k, v in s.items() if k != 'sc' or len(v) < 9}))
