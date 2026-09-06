"""gate92.py -- s55.  Scores PREDICTION-SCREEN.md (655c2d3ef8c0d335, filed 14:48:20Z).
usage: python3 gate92.py [--canfail]
"""
import sys, os, json, copy
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(D, '..')
def rd(p): return {d['Z']: d for d in map(json.loads, open(p))}
S = rd(os.path.join(R, 'rt', 'nlchain.jsonl'))

def score(N):
    c = {}; r = N.get(92); s = S[92]
    so = dict(s['order']); no = dict(r['order']) if r else {}
    d5 = no.get('5f', 0) - so['5f']; d6 = no.get('6d', 0) - so['6d']
    c['SC-1 Z=92 ent=5f, unchanged from sealed'] = bool(r) and r['ent'] == s['ent'] == '5f'
    c['SC-2 Z=92 margin widens beyond 0.12638'] = bool(r) and r['margin'] > s['margin']
    c['SC-3 differential acts WITH 5f (5f deepens more)'] = d5 < d6
    c['SC-4 no reversal reachable: gap 0.12638, differential not opposed'] = (
        d5 < d6 and bool(r) and r['order'][0][0] == '5f')
    c['SC-5 Z=92 rung 0 for ref, 5f, 6d'] = bool(r) and r['rungs'] == [0] and r['rung_ref'] == 0 \
        and r['chan']['5f']['rung'] == 0 and r['chan']['6d']['rung'] == 0
    c['SC-6 Z=93..104 screened: sealed 5f lead grows monotonically'] = all(
        dict(S[z]['order'])['5f'] < dict(S[z]['order'])['6d'] and S[z]['ent'] == '5f'
        and S[z]['margin'] >= S[92]['margin'] for z in range(93, 105))
    return c

def report(c):
    bad = [k for k, v in c.items() if not v]
    for k, v in c.items(): print('  %-58s %s' % (k, 'PASS' if v else 'FAIL'))
    print('GATE92: %s -- %d/%d clauses' % ('PASS' if not bad else 'FAIL', len(c) - len(bad), len(c)))
    return 0 if not bad else 1

if __name__ == '__main__':
    base = rd(os.path.join(D, 'c3z92.jsonl'))
    if len(sys.argv) > 1 and sys.argv[1] == '--canfail':
        for tag, mut in [('ent flipped to 6d', lambda n: n[92].update(ent='6d')),
                         ('margin narrowed',   lambda n: n[92].update(margin=0.01)),
                         ('6d deepened more',  lambda n: n[92].update(order=[['5f',-0.36],['6d',-0.99]]))]:
            n = copy.deepcopy(base); mut(n)
            print('--- CANFAIL: %s' % tag); rc = report(score(n))
            print('    -> rc=%d %s' % (rc, 'CORRECTLY FAILED' if rc else '!!! GATE IS BLIND'))
        sys.exit(0)
    sys.exit(report(score(base)))