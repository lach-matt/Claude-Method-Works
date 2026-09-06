"""gate90.py -- s55.  Scores PREDICTION-F543.md (9e78654cbc42a09a, filed 14:34:29Z).
usage: python3 gate90.py [RESULT.json]   default pack55/f543.json
       python3 gate90.py --canfail       three independent failure demonstrations
"""
import sys, os, json
D = os.path.dirname(os.path.abspath(__file__))
SEALED = dict(D_7s=-0.14359, D_6d=-0.13478, margin=0.00881, ref_it=34)

def score(r):
    c = {}
    f5, f7, f6 = r['chan']['5f'], r['chan']['7s'], r['chan']['6d']
    c['F3-1 5f does not converge at rung 0'] = (f5['conv'] is False and f5['it'] == 100
                                                and f5['rung'] == 0 and f5['E'] is None)
    c['F3-2 7s,6d converge at rung 0 and reproduce sealed D'] = (
        f7['conv'] and f6['conv'] and f7['it'] < 100 and f6['it'] < 100
        and f7['rung'] == 0 and f6['rung'] == 0
        and abs(f7['D'] - SEALED['D_7s']) <= 1e-5 and abs(f6['D'] - SEALED['D_6d']) <= 1e-5)
    m = None if not (f7['conv'] and f6['conv']) else round(abs(f7['D'] - f6['D']), 5)
    c['F3-3 margin 0.00881+/-2e-5, ent=7s, no rung-1 solve in the comparison'] = (
        m is not None and abs(m - SEALED['margin']) <= 2e-5 and f7['D'] < f6['D']
        and max(f7['rung'], f6['rung'], r['ref']['rung']) == 0)
    c['F3-4 5f rung-0 last iterate shallower than -0.06 Ha'] = (
        f5['D_last'] is not None and f5['D_last'] > -0.06)
    c['F3-5 reference converges at rung 0, it=34'] = (
        r['ref']['conv'] and r['ref']['rung'] == 0 and r['ref']['it'] == SEALED['ref_it'])
    c['LADDER truncated to rung 0 only'] = [tuple(x) for x in r['ladder']] == [(0.4, 100)]
    c['c = 1e6 (the live lever)'] = r['clight'] == 1e6
    return c

def report(c, name=''):
    bad = [k for k, v in c.items() if not v]
    for k, v in c.items(): print('  %-62s %s' % (k, 'PASS' if v else 'FAIL'))
    print('GATE90%s: %s -- %d/%d clauses' % (name, 'PASS' if not bad else 'FAIL',
                                             len(c) - len(bad), len(c)))
    return 0 if not bad else 1

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--canfail':
        base = json.load(open(os.path.join(D, 'f543.json')))
        import copy
        for tag, mut in [
            ('5f silently converged', lambda r: r['chan']['5f'].update(conv=True, it=57, E=-1.0)),
            ('7s D drifted 1e-4',     lambda r: r['chan']['7s'].update(D=-0.14369)),
            ('a rung-1 solve present',lambda r: r['chan']['6d'].update(rung=1))]:
            r = copy.deepcopy(base); mut(r)
            print('--- CANFAIL: %s' % tag)
            rc = report(score(r))
            print('    -> rc=%d %s' % (rc, 'CORRECTLY FAILED' if rc else '!!! GATE IS BLIND'))
        sys.exit(0)
    p = sys.argv[1] if len(sys.argv) > 1 else os.path.join(D, 'f543.json')
    sys.exit(report(score(json.load(open(p)))))