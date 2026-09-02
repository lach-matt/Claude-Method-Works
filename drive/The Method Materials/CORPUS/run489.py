# run489.py — the ruled bracket over the Spectra Compendium's untested rows.
# Sealed test (bracket.py, R 796) under M's ruling (RULING-TOLERANCE-489.md):
# strict interval membership; quotation floor (half a unit in the last quoted
# decimal of the measured level) as the only edge guard; admissibility
# r = 2*Z^2*R/(nu^3*sigma) >= 5 (Method Section 22.5) with sigma = the quotation
# floor — a cell that cannot distinguish pass from fail is REFUSED. The raw
# tables' unc column is present and NOT used, per the ruling's grounds (R 822, 807).
# Limits and Z: channels.py's LIM (the sealed pipeline's own), cross-checked
# against each row's printed limit; mismatches reported, never silently chosen.
import re, math, glob, os, json, sys
from collections import defaultdict
R = 109737.31568
SP = 'The_Method_1_6___Spectra_Compendium-2.md'

# LIM from the restore point's channels.py (identical to the store's)
src = open('rp/channels.py', encoding='utf-8').read()
i = src.index('LIM = {'); depth, j = 0, i + 6
while True:
    if src[j] == '{': depth += 1
    elif src[j] == '}':
        depth -= 1
        if depth == 0: break
    j += 1
LIM = eval(src[i+6:j+1])

def qfloor(s):
    s = s.strip()
    return 0.5 * 10 ** -(len(s.split('.')[1]) if '.' in s else 0)

def load_raw(name):
    ser = defaultdict(list)
    for line in open(f'rp/spectra_raw/{name}.tsv', encoding='utf-8'):
        if line.startswith('#') or line.startswith('config') or not line.strip(): continue
        p = line.rstrip('\n').split('\t')
        if len(p) < 4: continue
        mm = re.match(r'^(.*?)(\d+)([spdfghik])$', p[0].strip())
        if not mm: continue
        try: E = float(p[3])
        except ValueError: continue
        ser[(mm.group(1), mm.group(3), p[1].strip(), p[2].strip())].append((int(mm.group(2)), E, p[3].strip()))
    return ser

results = {}; anomalies = []
rows = [l for l in open(SP, encoding='utf-8') if l.startswith('| ') and re.search(r'\| [+-]\d\.\d+(?:e-\d+)? \|', l)]
for l in rows:
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if c[5] != 'untested': continue
    species = c[0].replace(' *', ''); name = species.replace(' ', '')
    key = (species, c[1])
    if not os.path.exists(f'rp/spectra_raw/{name}.tsv'):
        results[key] = ('no-data', 0, 0, 0, 0); continue
    m = re.match(r'^(.*?)n([spdfghik])\s+(\S+)\s+J=(\S+)$', c[1])
    if not m:
        anomalies.append((key, 'series-unparsed')); results[key] = ('unparsed', 0, 0, 0, 0); continue
    pre, lch, term, J = m.group(1), m.group(2), m.group(3), m.group(4)
    nr = re.match(r'(\d+)[–-](\d+)', c[2]); nlo, nhi = int(nr.group(1)), int(nr.group(2))
    lim, Z = LIM.get(name, (None, None))
    rowlim = float(c[10].replace(',', ''))
    if lim is None: lim, Z = rowlim, {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'IX':9,'XI':11,'XV':15,'XVI':16}[species.split()[1]]
    elif abs(lim - rowlim) > 0.5: anomalies.append((key, f'limit LIM {lim} vs row {rowlim}'))
    ser = load_raw(name)
    v = sorted({(n, E, s) for (p2, l2, t2, j2), vals in ser.items() if (p2, l2, t2, j2) == (pre, lch, term, J) for (n, E, s) in vals if nlo <= n <= nhi and E < lim})
    if len(v) != int(c[3]): anomalies.append((key, f'levels raw {len(v)} vs row {c[3]}'))
    d = {n: n - Z * math.sqrt(R / (lim - E)) for n, E, s in v}
    byn = {n: (E, s) for n, E, s in v}
    p = f = rf = t = 0; fails = []
    for k in range(1, len(v) - 1):
        n = v[k][0]
        if v[k-1][0] != n - 1 or v[k+1][0] != n + 1: continue
        dl, dh = sorted((d[n-1], d[n+1]))
        lo = lim - Z*Z*R / (n - dl)**2; hi = lim - Z*Z*R / (n - dh)**2
        lo, hi = min(lo, hi), max(lo, hi)
        E, s = byn[n]; qf = qfloor(s); nu = n - d[n]
        if 2 * Z*Z * R / (nu**3 * qf) < 5: rf += 1; continue
        t += 1
        if lo - qf <= E <= hi + qf: p += 1
        else: f += 1; fails.append(n)
    results[key] = ('run', p, f, rf, t)
    if fails: anomalies.append((key, f'FAIL at n={fails}'))

ran = [v for v in results.values() if v[0] == 'run']
print(f'rows: {len(results)} total — {len(ran)} run, {sum(1 for v in results.values() if v[0]=="no-data")} no-data, {sum(1 for v in results.values() if v[0]=="unparsed")} unparsed')
print(f'cells: {sum(v[4] for v in ran)} tested — {sum(v[1] for v in ran)} pass, {sum(v[2] for v in ran)} FAIL; {sum(v[3] for v in ran)} refused')
print(f'rows with zero testable cells: {sum(1 for v in ran if v[4]+v[3]==0)}')
print(f'anomalies: {len(anomalies)}')
for a in anomalies[:40]: print('  ', a)
json.dump({f'{k[0]}|{k[1]}': v for k, v in results.items()}, open('run489_results.json', 'w'), indent=0)
