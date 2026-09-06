#!/usr/bin/env python3
"""r2-ch15t - computable batch for chat 113's unit: main L8029-L8097 (SS29.6-SS29.8).

Count words against their own tables; the four-owners arithmetic; the mathematics/
philosophy universal against the table that follows it; the filtration partition;
closure defect 36/0; w.V = 8L^2; page-range conventions; a digit-bounded numeral
sweep with cross-volume site counts.  Reads members, never a bundle.
"""
import re, importlib.util
from decimal import Decimal, ROUND_HALF_UP

MEM = '/home/claude/members/'
spec = importlib.util.spec_from_file_location('r2lib', MEM + 'r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
heading_line, section_span, has_token, enclosing = (
    r2lib.heading_line, r2lib.section_span, r2lib.has_token, r2lib.enclosing)

VOL = {
    'main': 'The_Method_1_6-2.md',
    'reg':  'The_Method_1_6___The_Register-2.md',
    'mc':   'The_Method_1_6___Mathematical_Compendium-2.md',
    'pc':   'The_Method_1_6___The_Physics_Compendium-2.md',
    'ioi':  'The_Method_1_6___The_Index_of_Indices-2.md',
    'sc':   'The_Method_1_6___Spectra_Compendium-2.md',
}
V = {k: open(MEM + f, encoding='utf-8').read().split('\n') for k, f in VOL.items()}
M = V['main']
LO, HI = 8029, 8097
UNIT = M[LO - 1:HI]


# --- owed to r2lib: body_range (heading -> next heading of ANY rank) ---------
def body_range(Mx, sec):
    s = heading_line(Mx, sec)
    if s is None:
        return None
    for i in range(s + 1, len(Mx) + 1):
        if re.match(r'^#{1,6} ', Mx[i - 1].strip()):
            return (s, i)
    return (s, len(Mx) + 1)


# --- owed to r2lib: left-bounded stem matcher --------------------------------
def has_stem(text, stem):
    return len(re.findall(r'(?<![A-Za-z])' + re.escape(stem), text, re.I))


# --- owed to r2lib: digit-bounded numeral sweep ------------------------------
def num_sites(lines, num):
    pat = r'(?<![0-9])' + re.escape(num) + r'(?![0-9])'
    return [i for i, t in enumerate(lines, 1) if re.search(pat, t)]


# --- owed to r2lib: two-line-join phrase sweep -------------------------------
def phrase_sites(lines, phrase):
    p = re.escape(phrase).replace(r'\ ', r'\s+')
    out = []
    for i in range(1, len(lines) + 1):
        if re.search(p, lines[i - 1], re.I):
            out.append(i)
        elif i < len(lines) and re.search(p, lines[i - 1] + ' ' + lines[i], re.I):
            out.append(i)
    return out


def q2(x):
    return Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def head(t):
    print('\n' + '=' * 78 + '\n' + t + '\n' + '=' * 78)


# --- space-aligned table parser: column offsets taken from the header line ---
def cols_from_header(hdr, names):
    """Character offsets of each column title in a space-aligned table header."""
    off = []
    for n in names:
        j = hdr.find(n)
        assert j >= 0, (n, hdr)
        off.append(j)
    return off


def parse_aligned(lines, first, last, names):
    """Rows of a space-aligned table; a line whose first column is blank is a
    continuation of the row above.  Returns [(startline, [c1, c2, ...]), ...]."""
    hdr = lines[first - 1]
    off = cols_from_header(hdr, names)
    bounds = list(zip(off, off[1:] + [10 ** 6]))
    rows = []
    for i in range(first + 1, last + 1):
        t = lines[i - 1]
        if not t.strip():
            continue
        cells = [t[a:b].strip() for a, b in bounds]
        if cells[0]:
            rows.append([i, cells])
        elif rows:
            for j, c in enumerate(cells):
                if c:
                    rows[-1][1][j] = (rows[-1][1][j] + ' ' + c).strip()
    return rows


# =============================================================================
head('T1  the unit extent, measured by heading scan, body occurrences only')
for sec in ('29.5.5', '29.6', '29.7', '29.7.1', '29.8', '29.9'):
    hl = heading_line(M, sec)
    print(f'  SS{sec:<8} heading_line {hl}   body_range {body_range(M, sec)}   '
          f'section_span {section_span(M, sec)}')
    print(f'            {M[hl-1].strip()[:88]}')
print(f'  unit L{LO}-L{HI} = {HI-LO+1} lines; non-blank {sum(1 for t in UNIT if t.strip())}')
print('  contents-list occurrences of "29." (must NOT be the resolved lines):',
      [i for i in range(145, 160) if re.search(r'^#{1,3}\s*29\.', M[i - 1].strip())])

# =============================================================================
head('T2  SS29.7 - "Nine literatures" against the two tables it introduces')
print('  claim L8042:', M[8041].strip())
names1 = ['literature', 'what it owns', 'for this book']
t1 = parse_aligned(M, 8046, 8054, names1)
t2 = parse_aligned(M, 8056, 8062, names1)
for lab, tb in (('table 1 (L8046 header)', t1), ('table 2 (L8056 header)', t2)):
    print(f'  --- {lab}: {len(tb)} rows ---')
    for ln, c in tb:
        print(f'   L{ln}  {c[0]!r:<34} | {c[1]!r:<46} | {c[2]!r}')
rows = t1 + t2
print(f'  ROWS TOTAL {len(rows)}   count word "Nine" at L8042 -> 9   '
      f'{"EXACT by row" if len(rows) == 9 else "MISMATCH"}')
named = []
for ln, c in rows:
    named += [p.strip() for p in c[0].split(';') if p.strip()]
print(f'  LITERATURES NAMED (splitting the row label on ";"): {len(named)}  {named}')
print(f'  -> {len(rows)} rows carry {len(named)} named literatures; the discrepant row is '
      f'{[c[0] for _, c in rows if ";" in c[0]]}')
print('  restatement L8076-8078 and L8085 use the same word:')
for i in (8076, 8077, 8078, 8085):
    print(f'   L{i}  {M[i-1].strip()[:120]}')

# =============================================================================
head('T3  "Four owners of the cost-of-rigour framing" - three statements, no common reading')
print('  L8064 :', M[8063].strip())
print('  L8066 :', M[8065].strip())
print('  L8067 :', M[8066].strip())
print('  L8085 :', M[8084].strip())
seg = M[8063]
after = seg.split('§23.8.4:', 1)[1] if '§23.8.4:' in seg else seg
after = after.split('—')[0]
listed = [p.strip(' *') for p in re.split(r',| and ', after) if p.strip(' *')]
print(f'  colon-list after the pointer -> {len(listed)} names: {listed}')
fr = [(ln, c[0], c[1], c[2]) for ln, c in rows if has_stem(c[2], 'framing')]
print(f'  table rows whose RETURN column names the framing: {len(fr)}')
for ln, a, b, c in fr:
    print(f'   L{ln}  {a!r:<24} owns {b!r:<34} -> {c!r}')
owners_named = set()
for _, a, b, c in fr:
    owners_named |= set(re.findall(r'\b(Moore|IEEE|Manski|Shannon|Korner|Orlitsky)\b', a + ' ' + b))
owners_named |= set(re.findall(r'\b(Moore|IEEE|Manski|Shannon)\b', seg))
print(f'  union of framing-owner names in the section: {sorted(owners_named)} '
      f'= {len(owners_named)}')
print('  READINGS:')
print(f'   R1  four = 3 named + this book      -> L8066 "the book is the fourth" HOLDS; '
      f'L8085 "four owners ... FOUND" FAILS (a search did not find this book)')
print(f'   R2  four = Moore, IEEE, Manski, Shannon (all prior, all found) -> L8085 HOLDS; '
      f'the colon-list at L8064 names {len(listed)} of 4 (IEEE 1788 omitted); '
      f'and L8066 FAILS - the book would be the fifth')
print(f'   R3  four = 4 prior, one unnamed     -> colon-list short AND L8066 FAILS')
print('   NO READING SATISFIES ALL THREE SENTENCES.')

# =============================================================================
head('T4  L8042-8044 - a universal over a partition the section never prints')
for i in (8042, 8043, 8044):
    print(f'  L{i}  {M[i-1].strip()}')
print('  test: which rows own MATHEMATICS (a formula or a formal technique), and what')
print('  each returned.  The section labels no row as mathematics or as philosophy.')
FORMULA = re.compile(r'[=/²·′″‖ΔδλμΩ]|\(Δx\)')
for ln, c in rows:
    math = bool(FORMULA.search(c[1]))
    ret = c[2]
    disclaim = bool(re.search(r'attribution only|different quantities', ret, re.I))
    newd = bool(has_stem(ret, 'deriv') or has_stem(ret, 'new'))
    print(f'   L{ln}  {c[0]!r:<34} owns-formula {str(math):<5} '
          f'return {ret!r:<28} new-derivation {str(newd):<5} explicit-non-contribution {disclaim}')
ctr = [(ln, c[0], c[2]) for ln, c in rows
       if FORMULA.search(c[1]) and re.search(r'attribution only|different quantities', c[2], re.I)]
print(f'  COUNTEREXAMPLES on the formula test: {len(ctr)}')
for ln, a, c in ctr:
    print(f'   L{ln}  {a!r} owns a formula and returned {c!r} - not a new derivation')
print('  Richardson extrapolation owns "step-ratio elimination" - a formal technique with')
print('  no typeset formula, so it fails the mechanical test but is mathematics by name;')
print('  it returned "attribution only".  Counting it, the counterexamples are 2.')

# =============================================================================
head('T5  SS29.7.1 L8074 - the filtration groups against the nine literatures')
print('  L8074:', M[8073].strip())
print('  L8072:', M[8071].strip())
grp = {'spectroscopy (nine approaches)': 1, 'received one search each': 4,
       'entered only after the audit': 2}
tot = sum(grp.values())
print(f'  groups named: {grp}  ->  {" + ".join(str(v) for v in grp.values())} = {tot}')
print(f'  literatures entered = 9 (L8042, L8076).  UNACCOUNTED = {9 - tot}')
print('  and no row of either table is labelled with which group it falls in:')
print('   members of "four literatures received one search each" : UNPRINTED')
print('   members of "two were entered only after the audit"     : UNPRINTED')
print('  L8076-8078 restates it as "one deeply, most by one or two searches";')
print(f'  "most" of 9 requires >= 5; 1 deeply + 4 one-search = 5 accounted, '
      f'{9 - 5} literatures have no stated depth.')

# =============================================================================
head('T6  SS29.6 - the heading count word against its own table (site is in this unit)')
print('  heading L8029:', M[8028].strip())
pipe = [i for i in range(8030, 8040) if M[i - 1].lstrip().startswith('|')]
body = [i for i in pipe if not re.match(r'^\|[\s\-:|]+\|$', M[i - 1].strip())
        and not M[i - 1].strip().startswith('| document')]
print(f'  pipe-table lines {pipe}; header 1, rule 1, BODY ROWS {len(body)} at {body}')
for i in body:
    print(f'   L{i}  {M[i-1].strip()[:110]}')
print(f'  heading count word "three" -> 3;  table body rows -> {len(body)}')
print('  carried MEASURED (chats 111-112, 15k-06), not re-derived here: main L5433 and')
print('  L4550 independently state four.  This unit holds the heading site itself.')
print('  L8039 applies "for each" across the table:', M[8038].strip()[:120])

# =============================================================================
head('T7  E(X) closure defect - 36 for the periodic table, 0 for Lambda')
print('  claim L8094:', M[8093].strip())
for k in V:
    for i in phrase_sites(V[k], 'closure defect'):
        print(f'   {k} L{i} [{enclosing(V[k], i) if k == "main" else "-"}]  '
              f'{V[k][i-1].strip()[:130]}')
print('  --- every digit-bounded "36" beside a closure/defect word, six volumes ---')
for k in V:
    for i in num_sites(V[k], '36'):
        t = V[k][i - 1]
        if has_stem(t, 'defect') or has_stem(t, 'closure') or has_stem(t, 'periodic'):
            print(f'   {k} L{i}  {t.strip()[:130]}')

# =============================================================================
head('T8  w.V = 8 lambda^2 and lambda^2 = f\'^2/f\'\' - every site, six volumes')
for ph in ('8λ²', 'w·V', 'f′²/f″', 'self-concordance', 'Nesterov'):
    print(f'  --- {ph} ---')
    n = 0
    for k in V:
        for i in phrase_sites(V[k], ph):
            n += 1
            print(f'   {k} L{i} [{enclosing(V[k], i) if k == "main" else "-"}]  '
                  f'{V[k][i-1].strip()[:120]}')
    if n == 0:
        print('   (no site)')

# =============================================================================
head('T9  page ranges in the unit, and the convention each is computed under')
print('  L8035:', M[8034].strip())
print('  L8096:', M[8095].strip()[:200])
for a, b, what in ((142, 150, 'Ritz, Oeuvres (1911), ~pp. 142-150'),
                   (401, 431, 'Habib et al., TCS 312 (2004), 401-431')):
    print(f'   {what}: inclusive {b-a+1}, exclusive {b-a}')
print('  "Two pages longer than the ApJ version" - the ApJ page range must be printed')
print('  somewhere for the difference to be checkable:')
for k in V:
    for ph in ('Astrophysical Journal', 'ApJ', 'Ritz'):
        for i in phrase_sites(V[k], ph):
            print(f'   {k} L{i} [{enclosing(V[k], i) if k == "main" else "-"}]  '
                  f'{V[k][i-1].strip()[:140]}')

# =============================================================================
head('T10  digit-bounded numeral sweep of the unit, with cross-volume site counts')
nums = []
for t in UNIT:
    nums += re.findall(r'(?<![0-9.])\d{3,4}(?![0-9])', t)
seen = []
for n in nums:
    if n not in seen:
        seen.append(n)
print(f'  distinct 3-4 digit numerals in the unit: {len(seen)}  {seen}')
for n in seen:
    tot = {k: len(num_sites(V[k], n)) for k in V}
    print(f'   {n}:  ' + '  '.join(f'{k} {v}' for k, v in tot.items()) +
          ('   SINGLE WITNESS' if sum(tot.values()) == 1 else ''))

# =============================================================================
head('T11  census row 1174 (main L8072) - the data for its disposition')
print('  flagged line L8072:', M[8071].strip())
print('  the section it sits in:', M[heading_line(M, '29.7.1') - 1].strip())
print('  is the "never" a claim about the mathematics or about the book\'s own process?')
print('  neighbouring sentences:')
for i in (8070, 8072, 8074):
    print(f'   L{i}  {M[i-1].strip()[:150]}')
print('  counterexample test: any site recording a control as looked-for-and-not-found?')
for k in V:
    for ph in ('looked for and not found', 'control'):
        s = phrase_sites(V[k], ph)
        if s:
            print(f'   {k} {ph!r}: {s[:12]}{" ..." if len(s) > 12 else ""}')

print('\nr2-ch15t complete.')
