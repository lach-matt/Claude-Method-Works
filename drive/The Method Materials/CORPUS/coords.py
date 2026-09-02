# coords.py — read Part 0's figures from COORDINATES-2.13, the data companion.
#
# WHY THIS EXISTS. The Spectra Compendium states twice that its counts are read from
# COORDINATES-2.13 at build time and none is transcribed. Until this instrument, no .py in the
# set opened that file (audit A2, finding SPEC-02): every Part 0 figure was transcribed and
# happened to be faithful. A claim that is true of the result but false of the mechanism is the
# dangerous kind, because nothing catches the drift. This closes it.
#
# DEFAULT is VERIFY and it is a GATE: a mismatch exits non-zero and names the site. --write
# drives the figures to the file. Sites are found by CONTENT, never by line number, because the
# press may already have moved them.
#
# usage:  python3 coords.py <spectra.md> [coords.csv] [--write]

import csv, collections, re, sys, os

md = sys.argv[1] if len(sys.argv) > 1 else 'The_Method_1_6___Spectra_Compendium-2.md'
csvp = None
for a in sys.argv[2:]:
    if not a.startswith('--'):
        csvp = a
if csvp is None:
    for c in ('COORDINATES-2.13.csv', 'COORDINATES-2_13.csv',
              '/mnt/project/COORDINATES-2_13.csv'):
        if os.path.exists(c):
            csvp = c
            break
if csvp is None or not os.path.exists(csvp):
    sys.exit('coords.py: COORDINATES-2.13 not found. It is the object; the pages are the reading.')

rows = list(csv.DictReader(open(csvp, encoding='utf-8-sig', newline='')))

# ---- the measurement -------------------------------------------------------
admits = len(rows)
wit = sum(1 for r in rows if r['witness'] == 'witnessed')
unwit = admits - wit
grade = collections.Counter(r['grade'] for r in rows)
bound = collections.Counter(r['bound'] for r in rows)
DASH = '-'
bounded = admits - bound[DASH]              # cells carrying a bound string
# the 25: witnessed AND bounded. Measured, not assumed — A3/SPEC-01's diagnosis.
both = sum(1 for r in rows if r['witness'] == 'witnessed' and r['bound'] != DASH)
pct = 100.0 * wit / admits

def com(n):
    return f'{n:,}'

print(f'{csvp}: {com(admits)} cells')
print(f'  witnessed {com(wit)} · unwitnessed {com(unwit)} · {pct:.3f}%')
print(f'  grade ' + ' · '.join(f'{k} {com(v)}' for k, v in sorted(grade.items())))
print(f'  bound: {len(bound)} distinct, {len(bound)-1} printed rows summing to {com(bounded)}')
print(f'  witnessed cells that ALSO carry a bound: {both}'
      f'   ({com(bounded)} - {com(unwit)} = {bounded-unwit})')

# ---- the sites, found by content ------------------------------------------
t = open(md, encoding='utf-8').read()
checks = []          # (label, regex with one capture group, expected string)

def site(label, pat, expect):
    checks.append((label, pat, expect))

site('admits (Part 0 table)',   r'\|\s*the index admits\s*\|\s*\*\*([\d,]+)\*\*',      com(admits))
site('witnessed (Part 0 table)', r'\|\s*\*\*witnessed\*\*\s*\|\s*\*\*([\d,]+)\*\*',    com(wit))
site('unwitnessed (Part 0 table)', r'\|\s*\*\*unwitnessed\*\*\s*\|\s*\*\*([\d,]+)\*\*', com(unwit))
site('checked-against-reality %', r'\*\*([\d.]+)% of the index has been checked',      f'{pct:.3f}')
site('admits (schema recap)',    r'\|\s*the index admits\s*\|\s*([\d,]+)\s*\|',        com(admits))
site('witness schema line',      r'\|\s*`witness`\s*\|[^|]*\|\s*([\d,]+ · [\d,]+)',    f'{com(wit)} · {com(unwit)}')
site('bound distinct count',     r'\|\s*`bound`\s*\|\s*(\d+) distinct',                str(len(bound)))
site('CSV row count',            r'\(CSV,\s*([\d,]+)\s*rows',                          com(admits))

fails, wrote = [], 0
for label, pat, expect in checks:
    m = re.search(pat, t)
    if not m:
        fails.append(f'{label}: SITE NOT FOUND (content match failed — did the wording change?)')
        continue
    got = m.group(1)
    if got == expect:
        print(f'  ok    {label}: {got}')
    elif '--write' in sys.argv:
        t = t[:m.start(1)] + expect + t[m.end(1):]
        wrote += 1
        print(f'  WROTE {label}: {got} -> {expect}')
    else:
        fails.append(f'{label}: file says {got}, COORDINATES says {expect}')

# ---- the bounds table: every row, against the file -------------------------
rowpat = re.compile(r'^\|\s*\*\*([\d,]+)\*\*\s*\|\s*(.+?)\s*\|\s*$', re.M)
# LOCATE BY PREFIX, NOT BY THE FULL TITLE. Register 1772 renamed this section from
# "The bounds on the unwitnessed" to "The bounds, witnessed and unwitnessed" and this
# check went silently dead for a build: the gate exited 1 on "section not found", which
# reads like a missing section rather than a stale locator. Found at chat 28.
# AND IT DIED A SECOND TIME, THE SAME WAY, FOR THE SAME REASON. Ruling 49 (chat 28)
# promoted Spectra's 24 level-3 headings to level 2, so every '### ' locator in this
# file stopped matching and BOTH section checks reported 'not found'. No press ran at
# chat 29, so it surfaced only at chat 30. LOCATE BY NAME AT ANY LEVEL — never by one
# literal serialization of a heading, exactly as W-013 says of an XML element.
sec = re.split(r'^#{2,4} The bounds[^\n]*\n', t, maxsplit=1, flags=re.M)
if len(sec) > 1:
    seen = {}
    for m in rowpat.finditer(re.split(r'\n#{1,4} ', sec[1])[0]):
        seen[m.group(2)] = int(m.group(1).replace(',', ''))
    want = {k: v for k, v in bound.items() if k != DASH}
    for k in sorted(set(want) | set(seen), key=lambda x: -want.get(x, 0)):
        if seen.get(k) != want.get(k):
            fails.append(f'bounds row {k[:60]!r}: table {seen.get(k)}, COORDINATES {want.get(k)}')
    if sum(seen.values()) != bounded:
        fails.append(f'bounds table sums to {sum(seen.values())}, COORDINATES gives {bounded}')
    else:
        print(f'  ok    bounds table: {len(seen)} rows summing to {com(bounded)}')
else:
    fails.append('bounds table section not found by heading')

# ---- "The table": the supply across l, every figure against the file -------
# Built at chat 28 on the author's chat-26 ruling. The section claims its figures are
# read from COORDINATES-2.13; this is what makes that true of the mechanism and not
# only of the result (SPEC-02's distinction).
lt = re.split(r'^#{2,4} The table\s*\n', t, maxsplit=1, flags=re.M)
if len(lt) > 1:
    block = re.split(r'\n#{1,4} ', lt[1])[0]
    lrow = re.compile(r'^\|\s*\*\*(\d)\*\*\s*\S*\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)'
                      r'\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|', re.M)
    seen = {int(m.group(1)): [m.group(i) for i in (2, 3, 4, 5)]
            for m in lrow.finditer(block)}
    per = collections.defaultdict(collections.Counter)
    for r in rows:
        per[int(r['l'])][r['grade']] += 1
        per[int(r['l'])]['cells'] += 1
    if set(seen) != set(per):
        fails.append(f'The table: rows for l {sorted(seen)}, file has {sorted(per)}')
    for l in sorted(set(seen) & set(per)):
        want = [com(per[l]['cells']), com(per[l]['exact']),
                com(per[l]['measured']), com(per[l]['computed'])]
        if seen[l] != want:
            fails.append(f'The table, l={l}: row says {seen[l]}, COORDINATES gives {want}')
    tot = re.search(r'^\|\s*\|\s*\*\*([\d,]+)\*\*\s*\|\s*\*\*([\d,]+)\*\*\s*\|'
                    r'\s*\*\*([\d,]+)\*\*\s*\|\s*\*\*([\d,]+)\*\*', block, re.M)
    twant = [com(admits), com(grade['exact']), com(grade['measured']),
             com(grade['computed'])]
    if not tot:
        fails.append('The table: total row not found')
    elif list(tot.groups()) != twant:
        fails.append(f'The table, total row: {list(tot.groups())}, COORDINATES gives {twant}')
    if not fails:
        print(f'  ok    The table: {len(seen)} l-rows and the total, against the file')
else:
    fails.append('The table section not found')

if '--write' in sys.argv and wrote:
    open(md, 'w', encoding='utf-8').write(t)
    print(f'coords.py: wrote {wrote} figure(s) to {md}')

if fails:
    print('\ncoords.py: FAIL')
    for f in fails:
        print('  ' + f)
    sys.exit(1)
print('\ncoords.py: PASS — every Part 0 figure is read from COORDINATES-2.13, not transcribed.')

