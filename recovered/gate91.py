"""gate91.py -- s55.  Scores PREDICTION-Z90CONFIRM.md (a283c55eae21ba26, filed 14:37:52Z).
Light: reads jsonl only, imports no solver.
usage: python3 gate91.py [CONFIRM.jsonl]   default pack55/c3confirm.jsonl
       python3 gate91.py --canfail
"""
import sys, os, json, copy
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(D, '..')
def rd(p): return {d['Z']: d for d in map(json.loads, open(p))}
SEALED = rd(os.path.join(R, 'rt', 'nlchain.jsonl'))
C3 = rd(os.path.join(R, 'pack54', 'c3.jsonl'))
KEYS = ('ent', 'D_ent', 'margin', 'nfail', 'it_ref', 'rung_ref', 'rungs', 'ref_cfg')

def score(N):
    c = {}
    def same(Z):
        a, b = C3[Z], N[Z]
        return (all(a[k] == b[k] for k in KEYS) and a['order'] == b['order']
                and sorted(a['fail']) == sorted(b['fail']))
    c['Z90-1 Z=90 reproduces c3.jsonl bit-for-bit'] = 90 in N and same(90)
    c['Z90-2 fields disagree at Z=90 (sealed 6d, c=1e6 5f) -- C3-1 falsified'] = (
        90 in N and SEALED[90]['ent'] == '6d' and N[90]['ent'] == '5f')
    c['Z90-3 Z=89 reproduces c3.jsonl bit-for-bit; fields agree'] = (
        89 in N and same(89) and SEALED[89]['ent'] == N[89]['ent'] == '6d')
    c['Z90-4 Z=91 NEW: both fields choose 5f'] = (
        91 in N and SEALED[91]['ent'] == N[91]['ent'] == '5f')
    c['Z90-5 Z=91 margin widens without relativity'] = (
        91 in N and N[91]['margin'] > SEALED[91]['margin'])
    if 91 in N:
        o = dict((k, v) for k, v in N[91]['order']); s = dict((k, v) for k, v in SEALED[91]['order'])
        d5, d6 = abs(o.get('5f', 0) - s['5f']), abs(o.get('6d', 0) - s['6d'])
    else:
        d5 = d6 = None
    c['Z90-6 Z=91 5f shifts more than 6d'] = (d5 is not None and d5 > d6)
    c['Z90-7 disagreement at Z=90 ONLY -- crossover moves by one element'] = (
        all(z in N for z in (89, 90, 91))
        and [SEALED[z]['ent'] != N[z]['ent'] for z in (89, 90, 91)] == [False, True, False])
    c['Z90-8 every row rung 0, reference and 5f/6d channels'] = all(
        N[z]['rungs'] == [0] and N[z]['rung_ref'] == 0
        and N[z]['chan']['5f']['rung'] == 0 and N[z]['chan']['6d']['rung'] == 0
        for z in (89, 90, 91) if z in N) and len([z for z in (89, 90, 91) if z in N]) == 3
    c['Z90-9 all three rows carry the live lever c=1e6'] = all(
        N[z].get('clight') == 1e6 and N[z].get('lever') == 'nlguard.C0'
        for z in (89, 90, 91) if z in N)
    return c

def report(c):
    bad = [k for k, v in c.items() if not v]
    for k, v in c.items(): print('  %-64s %s' % (k, 'PASS' if v else 'FAIL'))
    print('GATE91: %s -- %d/%d clauses' % ('PASS' if not bad else 'FAIL', len(c) - len(bad), len(c)))
    return 0 if not bad else 1

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--canfail':
        base = rd(os.path.join(D, 'c3confirm.jsonl'))
        for tag, mut in [
            ('Z=90 drifts by 1e-5',      lambda n: n[90].update(D_ent=n[90]['D_ent'] - 1e-5)),
            ('Z=90 agrees with sealed',  lambda n: n[90].update(ent='6d')),
            ('Z=91 needed rung 1',       lambda n: n[91].update(rungs=[0, 1]))]:
            n = copy.deepcopy(base); mut(n)
            print('--- CANFAIL: %s' % tag); rc = report(score(n))
            print('    -> rc=%d %s' % (rc, 'CORRECTLY FAILED' if rc else '!!! GATE IS BLIND'))
        sys.exit(0)
    p = sys.argv[1] if len(sys.argv) > 1 else os.path.join(D, 'c3confirm.jsonl')
    sys.exit(report(score(rd(p))))