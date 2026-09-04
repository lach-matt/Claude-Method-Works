"""gate93.py -- s55.  Scores PREDICTION-TRANSIT.md (655b5936c86c00b3, filed 14:52:17Z).
Computes transit widths from the chains themselves; asserts nothing by hand.
usage: python3 gate93.py [--canfail]
"""
import sys, os, json, copy
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(D, '..')
def rd(p): return {d['Z']: d for d in map(json.loads, open(p))}
S = rd(os.path.join(R, 'rt', 'nlchain.jsonl'))

def width(ents, target, lo, hi):
    """protons of non-target entrant at the same n+l, before target first enters"""
    L = 'spdfg'; nl = lambda e: int(e[0]) + L.index(e[1])
    t = nl(target); w = 0
    for z in range(lo, hi + 1):
        e = ents.get(z)
        if e is None: return None
        if e == target: return w
        if nl(e) == t: w += 1
    return None

def score(N58, N):
    ent_nr = dict((z, N[z]['ent']) for z in N); ent_nr.update({58: N58[58]['ent']})
    ent_sr = dict((z, S[z]['ent']) for z in S)
    for z in (57, 89, 90, 91):
        ent_nr.setdefault(z, None)
    c = {}
    c['TR-1 Z=58 at c=1e6 gives ent=4f'] = N58[58]['ent'] == '4f' == S[58]['ent']
    c['TR-2 Z=58 margin widens beyond 0.12115'] = N58[58]['margin'] > S[58]['margin']
    so = dict(S[58]['order']); no = dict(N58[58]['order'])
    c['TR-2b 4f deepens more than 5d'] = (no['4f'] - so['4f']) < (no['5d'] - so['5d'])
    w4_sr = width(ent_sr, '4f', 57, 62); w5_sr = width(ent_sr, '5f', 89, 95)
    w4_nr = width(ent_nr, '4f', 57, 58); w5_nr = width(ent_nr, '5f', 89, 91)
    c['TR-3a relativistic widths (4f,5f) = (1,2)'] = (w4_sr, w5_sr) == (1, 2)
    c['TR-3b non-relativistic widths (4f,5f) = (1,1)'] = (w4_nr, w5_nr) == (1, 1)
    c['TR-3c the 4f/5f asymmetry is entirely relativistic'] = (
        w4_sr == w4_nr and w5_sr == w5_nr + 1)
    c['TR-4 Z=58 rung 0 for ref, 4f, 5d'] = (N58[58]['rungs'] == [0] and N58[58]['rung_ref'] == 0
        and N58[58]['chan']['4f']['rung'] == 0 and N58[58]['chan']['5d']['rung'] == 0)
    return c

def report(c):
    bad = [k for k, v in c.items() if not v]
    for k, v in c.items(): print('  %-52s %s' % (k, 'PASS' if v else 'FAIL'))
    print('GATE93: %s -- %d/%d clauses' % ('PASS' if not bad else 'FAIL', len(c) - len(bad), len(c)))
    return 0 if not bad else 1

if __name__ == '__main__':
    b58 = rd(os.path.join(D, 'c3z58.jsonl')); bN = rd(os.path.join(D, 'c3confirm.jsonl'))
    if len(sys.argv) > 1 and sys.argv[1] == '--canfail':
        for tag, m58, mN in [
            ('Z=58 gives 5d', lambda n: n[58].update(ent='5d'), lambda n: None),
            ('Z=58 margin narrows', lambda n: n[58].update(margin=0.01), lambda n: None),
            ('Z=90 NR keeps 6d (no width change)', lambda n: None, lambda n: n[90].update(ent='6d'))]:
            a, b = copy.deepcopy(b58), copy.deepcopy(bN); m58(a); mN(b)
            print('--- CANFAIL: %s' % tag); rc = report(score(a, b))
            print('    -> rc=%d %s' % (rc, 'CORRECTLY FAILED' if rc else '!!! GATE IS BLIND'))
        sys.exit(0)
    sys.exit(report(score(b58, bN)))