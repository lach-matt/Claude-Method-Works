# ruled_bracket.py — the sealed bracket (bracket.py, R 796) run under M's ruling
# (RULING-TOLERANCE-489.md, 2026-08-24): STRICT interval membership; the only ε is
# the QUOTATION FLOOR (half a unit in the last quoted decimal of the measured level),
# applied at the interval edges; a cell whose measurement cannot distinguish pass
# from fail is REFUSED, not passed: r = 2*Z^2*R/(nu^3 * sigma) >= 5 (Method §22.5),
# sigma = the quotation floor. Refusals counted separately from pass/fail.
import re, math, sys
from collections import defaultdict
R = 109737.31568

def qfloor(s):
    """Half a unit in the last quoted decimal place of the value as printed."""
    s = s.strip()
    return 0.5 * 10 ** -(len(s.split('.')[1]) if '.' in s else 0)

def run_series(members, lim, Z):
    """members: sorted [(n, E, E_as_printed)]. Returns (passed, failed, refused, detail)."""
    d = {n: n - Z * math.sqrt(R / (lim - E)) for n, E, _ in members}
    byn = {n: (E, s) for n, E, s in members}
    p = f = r = 0; detail = []
    for i in range(1, len(members) - 1):
        n = members[i][0]; a, b = members[i-1][0], members[i+1][0]
        if a != n - 1 or b != n + 1: continue          # only true neighbours (sealed)
        dl, dh = sorted((d[a], d[b]))
        lo = lim - Z*Z*R / (n - dl)**2
        hi = lim - Z*Z*R / (n - dh)**2
        lo, hi = min(lo, hi), max(lo, hi)
        E, s = byn[n]; qf = qfloor(s)
        nu = n - d[n]
        adm = 2 * Z*Z * R / (nu**3 * qf)               # §22.5 admissibility
        if adm < 5:
            r += 1; detail.append((n, 'REFUSED', adm)); continue
        if lo - qf <= E <= hi + qf:                     # strict, edge-guarded by the floor
            p += 1; detail.append((n, 'pass', (lo, hi, E, qf)))
        else:
            f += 1; detail.append((n, 'FAIL', (lo, hi, E, qf)))
    return p, f, r, detail

if __name__ == '__main__':
    # instrument verification on captures/LEVELS-K-I.tsv (the one untested species in the cut)
    lim, Z = 35009.814, 1
    ser = defaultdict(list)
    for line in open(sys.argv[1], encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        pp = line.rstrip('\n').split('\t')
        if len(pp) < 4: continue
        mm = re.match(r'^(\d+)([spdfghik])$', pp[0].strip())
        if not mm: continue
        try: E = float(pp[3])
        except ValueError: continue
        if E >= lim: continue
        ser[(mm.group(2), pp[1], pp[2])].append((int(mm.group(1)), E, pp[3]))
    for key, v in sorted(ser.items()):
        v = sorted(v)
        if len(v) < 3: continue
        p, f, r, det = run_series(v, lim, Z)
        print(key, f'pass {p} fail {f} refused {r}')
        for row in det: print('  ', row)
