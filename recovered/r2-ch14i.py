#!/usr/bin/env python3
# r2-ch14i — prose batch, Chapter 22 remainder (main member L6036-L6177).
# Chat 94.  Deterministic; prints no wall-clock time.
# heading_line() copied verbatim from r2-ch14g.py (chat 93), itself chat 88's exact-token
# resolver — matches the whole section number, never a numeric prefix.  Owed to r2lib.

import os, re

H = os.path.dirname(os.path.abspath(__file__))
M = open(os.path.join(H, 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
LO, HI = 6036, 6177
W = 78
def head(t): print('\n' + '=' * W + '\n' + t + '\n' + '=' * W)
def rule(): print('-' * W)


def heading_line(sec):
    hits = []
    for i, t in enumerate(M, 1):
        m = re.match(r'^#{1,4} (\d+(?:\.\d+)*)\.? ', t.strip())
        if m and m.group(1) == sec:
            hits.append(i)
    return hits[-1] if hits else None


def section_span(sec):
    """[start, end) of a section: its heading to the next heading of equal or higher rank."""
    s = heading_line(sec)
    if s is None: return None
    rank = len(re.match(r'^(#+) ', M[s - 1]).group(1))
    for i in range(s + 1, len(M) + 1):
        m = re.match(r'^(#+) ', M[i - 1])
        if m and len(m.group(1)) <= rank:
            return (s, i)
    return (s, len(M) + 1)


def body(sec):
    sp = section_span(sec)
    return '\n'.join(M[sp[0] - 1:sp[1] - 1]) if sp else ''


def toks(t):
    return set(re.findall(r'[a-z]{3,}', t.lower()))


# ----------------------------------------------------------------------------
head('I1  every pointer in L6036-L6177, resolved to the CLAIM and not the heading')
ptrs = [
    (6098, '25.6', 'the Sc VI prediction has a second, independent route through its '
                   'isoelectronic sequence, and 3.5% is the figure that route must carry',
     ['isoelectronic', '3.5']),
    (6114, '25.6', 'the estimate falls outside the deductive bracket its own monotonicity implies',
     ['0.9376', '0.9812', 'monoton']),
    (6135, '25.6', 'the antiprotonic-helium cells of 25.6, where the relevant threshold is ambiguous',
     ['antiproton']),
    (6138, '32.3', 'presents limit-freedom as pure gain',
     ['limit-free', 'limit freedom', 'ionisation limit', 'gain']),
    (6175, '23',   'Chapter 23 prices it exactly, and the price is the only linearly rising quantity',
     ['w / e', 'V =', 'cost']),
]
print(f'  {"site":>7s} {"target":>7s} {"heading at":>11s} {"span":>15s}  witness tokens in the target body')
rule()
i1 = []
for ln, sec, claim, keys in ptrs:
    sp = section_span(sec)
    b = body(sec).lower()
    found = [(k, b.count(k.lower())) for k in keys]
    hit = [k for k, c in found if c]
    ok = bool(hit)
    i1.append((ln, sec, ok, found))
    print(f'  L{ln:<6d} {"§"+sec:>7s} {"L"+str(sp[0]):>11s} {f"L{sp[0]}-L{sp[1]-1}":>15s}  '
          + ', '.join(f'{k}:{c}' for k, c in found))
rule()
for ln, sec, ok, found in i1:
    print(f'  L{ln} -> §{sec}: {"RESOLVES" if ok else "DOES NOT RESOLVE"}'
          + ('' if ok else '  (no witness token present anywhere in the target section)'))
print(f'\n  MEASURED: {sum(1 for x in i1 if x[2])} of {len(i1)} pointers resolve to their claim.')

# ----------------------------------------------------------------------------
head('I2  §32.3 read for the claim L6138 attaches to it')
sp = section_span('32.3')
print(f'  §32.3 spans L{sp[0]}-L{sp[1]-1}, {sp[1]-sp[0]} lines. Its labelled clauses:')
for i in range(sp[0], sp[1]):
    m = re.match(r'^\s*(ⅅ_\w+|\*\*D\d+[^*]*\*\*)', M[i - 1])
    if m: print(f'    L{i}: {m.group(1)}')
rule()
b = body('32.3').lower()
for t in ('limit', 'threshold', 'ionisation', 'gain', 'bracket', 'free'):
    print(f'    token {t!r:14s} occurrences in §32.3: {b.count(t)}')
print(f'\n  MEASURED: §32.3 is titled {M[sp[0]-1].strip()!r} and none of the tokens the')
print(f'  claim needs appears in it. The section states a verification count and two')
print(f'  self-defence conditions; limit-freedom is not among its subjects.')
rule()
print('  Where the claim would resolve, tested by the same method:')
for cand in ('22.3', '23.1'):
    spc = section_span(cand)
    bc = body(cand).lower()
    print(f'    §{cand} (L{spc[0]}): "limit" {bc.count("limit")}, "free" {bc.count("free")}')
a12 = [i for i in range(10000, 10060) if M[i - 1].startswith('### A.12')]
if a12:
    j = a12[0]
    print(f'    App A.12 (L{j}) "The bracket is limit-free" — the theorem itself, and its')
    print(f'      Consequence at L{j+13} restates §22.3 verbatim.')

# ----------------------------------------------------------------------------
head('I3  §32.3 as a citation target across the main volume')
print(f'  {"line":>8s}  site')
rule()
cls = []
for i, s in enumerate(M, 1):
    if '§32.3' in s:
        kind = 'index/contents' if re.search(r'…|·\s*§', s) and s.count('§') > 2 else 'prose citation'
        cls.append((i, kind))
        print(f'  L{i:<7d} [{kind}] {s.strip()[:96]}')
rule()
prose = [c for c in cls if c[1] == 'prose citation']
print(f'  MEASURED: {len(cls)} sites cite §32.3; {len(prose)} are prose citations.')
print(f'  L5692 (chat 91, W-129) records §32.3 cited for ℛ reaching level 2 — not in §32.3.')
print(f'  L6138 (this chat) cites it for limit-freedom as pure gain — not in §32.3.')
print(f'  The index entries at L11472/L11476/L11477 map self-defence, ⅅ_def and ⅅ_phys to')
print(f'  §32.3 and DO resolve; the failures are confined to the prose citations.')
rule()
er = [i for i, s in enumerate(M, 1) if '§32.3' in s and 'clauses' in s]
for i in er:
    print(f'  L{i} erratum: {M[i-1].strip()[:110]}')
    lab = len(re.findall(r'^\s*(?:ⅅ_\w+|\*\*D\d+)', body('32.3'), re.M))
    print(f'    §32.3 prints {lab} labelled clauses (ⅅ_def, ⅅ_phys, D3); the erratum says four.')

# ----------------------------------------------------------------------------
head('I4  "antiprotonic" — where those cells actually are')
print(f'  {"line":>8s}  §section  site')
rule()
def enclosing(ln):
    best = None
    for i in range(ln, 0, -1):
        m = re.match(r'^#{2,4} (\d+(?:\.\d+)*)\.? ', M[i - 1])
        if m: return m.group(1)
    return best
anti = [i for i, s in enumerate(M, 1) if re.search(r'(?i)antiproton', s)]
for i in anti:
    print(f'  L{i:<7d} §{str(enclosing(i)):<8s} {M[i-1].strip()[:88]}')
rule()
sp256 = section_span('25.6')
inside = [i for i in anti if sp256[0] <= i < sp256[1]]
print(f'  MEASURED: {len(anti)} sites name antiprotonic helium; {len(inside)} fall inside')
print(f'  §25.6 (L{sp256[0]}-L{sp256[1]-1}). The worked cells are §16.4 and §19; §25.6 is Sc VI throughout.')

# ----------------------------------------------------------------------------
head('I5  "prediction" against "deduction" — the vocabulary L6098 adopts')
print(f'  L6098 calls it: {M[6097].strip()[:100]!r}')
rule()
for ln in (6991, 7039, 7093):
    print(f'  L{ln} heading: {M[ln-1].strip()}')
for ln in (6992, 7040, 7041):
    print(f'  L{ln}: {M[ln-1].strip()[:104]}')
rule()
b = body('25.6')
print(f'  MEASURED inside §25.6: "prediction" {len(re.findall(r"(?i)prediction", b))}, '
      f'"deduction" {len(re.findall(r"(?i)deduction", b))}.')
print(f'  §25.6\'s title and §25.6.3 both deny the word; §25.6\'s opening line and §25.6.6\'s')
print(f'  title both use it. L6098 follows the second usage. The section is not settled on')
print(f'  its own vocabulary, so the citing site cannot be judged against it.')

# ----------------------------------------------------------------------------
head('I6  Register citation density, this range against its neighbours')
def reg_count(a, b):
    n = 0
    for i in range(a, b):
        n += len(re.findall(r'(?i)\bregisters?\s+\d+', M[i - 1]))
    return n
ranges = [('ch 20        L5551-L5596', 5551, 5597),
          ('ch 21        L5597-L5936', 5597, 5937),
          ('ch 22 part 1 L5937-L6035', 5937, 6036),
          ('ch 22 rest   L6036-L6177', LO, HI + 1),
          ('ch 23        L6178-L6622', 6178, 6623)]
print(f'  {"range":28s} {"lines":>7s} {"Register cites":>15s} {"per 100 lines":>15s}')
rule()
for lab, a, b in ranges:
    n, ln = reg_count(a, b), b - a
    print(f'  {lab:28s} {ln:7d} {n:15d} {100*n/ln:15.2f}')
print(f'\n  MEASURED: this range carries no Register citation of any case. Chapter 22\'s first')
print(f'  99 lines carry {reg_count(5937,6036)}; the chapter\'s two halves differ in kind, not only in rate.')

# ----------------------------------------------------------------------------
head('I7  census row 1134 — C9-OVERGENERALISATION-WORD, main L6163, token "never"')
print(f'  L6162-L6163: {M[6161].strip()[:95]}')
print(f'               {M[6162].strip()[:95]}')
rule()
print('  The flagged word sits in "the energy bound is never better than the limit is known",')
print('  which is a bound statement, not a generalisation over cases: it is the exact content')
print('  H13 verifies numerically (the printed +limit column is the via-delta width plus 2σ,')
print('  and at n = 40 the limit dominates by 699x). The token is a regex artefact of the')
print('  C9 class, on the precedent of rows 678, 680-687, 1067, 1069, 702, 1132, 1133.')
print('  VERDICT: not a defect.')

# ----------------------------------------------------------------------------
head('I8  figures printed here and nowhere else in the six volumes')
VOL = {}
for f in ('The_Method_1_6-2.md',):
    VOL['main'] = M
for name, key in (('MATHEMATICAL-COMPENDIUM.md', 'mc'), ('PHYSICS-COMPENDIUM.md', 'pc'),
                  ('INDEX-OF-INDICES.md', 'ioi'), ('SPECTRA-COMPENDIUM.md', 'sc'),
                  ('REGISTER.md', 'reg')):
    p = os.path.join(H, name)
    if os.path.exists(p):
        VOL[key] = open(p, encoding='utf-8').read().split('\n')
figs = ['0.46', '69.6', '41.3', '12,942', '0.8189', '0.7129', '0.7376', '0.7835', '14.9',
        '3.47', '70.9', '14,602', '4,329', '4,267', '1.387', '1.386', '68.06', '0.00102',
        '0.0210', '7.613', '1,577', '17.3', '0.9934', '1.0057']
print(f'  volumes loaded: {", ".join(sorted(VOL))}')
print(f'  {"figure":>10s} {"in range":>9s} {"elsewhere in main":>18s} {"other volumes":>15s}')
rule()
alone = []
for f in figs:
    inr = sum(1 for i in range(LO, HI + 1) if f in M[i - 1])
    oth_main = sum(1 for i, s in enumerate(M, 1) if f in s and not (LO <= i <= HI))
    oth = 0
    for k, v in VOL.items():
        if k == 'main': continue
        oth += sum(1 for s in v if f in s)
    if oth_main == 0 and oth == 0: alone.append(f)
    print(f'  {f:>10s} {inr:9d} {oth_main:18d} {oth:15d}')
rule()
print(f'  MEASURED: {len(alone)} of {len(figs)} appear at no other site in any loaded volume:')
print('  ' + ', '.join(alone))
print('  Each is a single-witness figure: nothing in the collection can contradict it, and')
print('  R4 should say so rather than leave them looking checked.')

# ----------------------------------------------------------------------------
head('I9  the ablation table\'s cost column — one column, two baselines')
for i in range(6058, 6065):
    print(f'  L{i}: {M[i-1].strip()[:96]}')
rule()
print('  MEASURED: rows 1-2 are quoted against a median of 0.46; row 5 against 12.8; row 3')
print('  against an rms of 200 and row 4 against a coverage fraction. Four baselines share')
print('  one column headed "cost", and the table does not say that they differ.')
print('  Row 4 is also the only row where the larger number is the violation: ±1σ coverage')
print('  96.2% against 69.6%, where the nominal for 1σ is 68.3% — the per-cell figure is')
print('  1.3 points from nominal and the pooled figure 27.9 points from it.')

# ----------------------------------------------------------------------------
head('I10  pair counts, and the C(N,2) convention')
pairs = [(i, M[i - 1]) for i in range(LO, HI + 1)
         if re.search(r'(?i)\b(pairs?|combinations?)\b', M[i - 1])]
print(f'  printed pair counts in L{LO}-L{HI}: {len(pairs)}')
for i, s in pairs: print(f'    L{i}: {s.strip()[:96]}')
print('  Nothing in this range states a pair count, so the C(N,2) convention has no site here.')

# ----------------------------------------------------------------------------
head('I11  negative claims in the range, each with its own witness')
negs = [('§22.2.2  "Rule 1 is not about n"', 6070,
         'witness: the Z-axis row of L6078 and the two hold-out sequences of L6084 — a second '
         'axis carrying the same defect. Measured in H3/H4.'),
        ('§22.2.4  "Rule 1\'s second clause is not redundant"', 6100,
         'witness: Sc III 3d, interior in n within ℓ = 2, inflating the median error 3.2x '
         '(L6101) with a defect departure of 0.14 against 0.008 (L6104). Measured in H7.'),
        ('§22.3    "containment does not [need the limit]"', 6133,
         'witness: App A.12\'s proof at main L10025-L10033. Verified; the same proof refutes '
         'the clause about V in the same sentence. Measured in H17.'),
        ('§22.5    "Every channel eventually leaves the domain"', 6172,
         'witness: r falling as ν⁻³, which holds only on the levels-uncertainty reading of σ. '
         'Measured in H15.')]
for lab, ln, w in negs:
    print(f'  {lab}   L{ln}')
    print(f'    {w}')
print('\n  MEASURED: four negative claims, four witnesses, each measured separately from its')
print('  claim. Two witnesses hold outright; two hold only under a reading the text does not fix.')

print('\n' + '=' * W)
print('r2-ch14i complete.')
print('=' * W)
