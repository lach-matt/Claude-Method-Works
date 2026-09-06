"""f543.py -- s55.  CLOSES F54.3.  Re-runs Z=88 with the ladder TRUNCATED TO RUNG 0.

Scores PREDICTION-F543.md (9e78654cbc42a09a, filed 14:34:29Z).
No sealed file is modified: NG.C0 and NG.LADDER are rebound in memory (F44.1 precedent).
Carries the s54 ruling's mandatory self-check: refuses to compute unless c demonstrably
moves the number, rc=4 if dead.
usage: python3 f543.py OUT.json
"""
import sys, os, json, time
D = os.path.dirname(os.path.abspath(__file__)); RT = os.path.join(D, '..', 'rt')
sys.path.insert(0, RT); os.chdir(RT)
CINF = 1e6; CREL = 137.035999
import nlchain as NC, nlguard as NG

def lever_live():
    cfg = NC.cfg_from_chain(79, NC.load())
    NG.C0 = CREL; a = NG.run_guarded(80, cfg, 'selfcheck')['E']
    NG.C0 = CINF; b = NG.run_guarded(80, cfg, 'selfcheck')['E']
    print('SELFCHECK Z=80 E(137.035999)=%.6f E(1e6)=%.6f |dE|=%.6f' % (a, b, abs(b-a)), flush=True)
    return abs(b - a)

if __name__ == '__main__':
    out = sys.argv[1]
    d = lever_live()
    if not d > 1e-3:
        print('HALT: lever DEAD (%.9f). No row computed.' % d); sys.exit(4)
    print('LEVER LIVE.', flush=True)
    NG.C0 = CINF
    NG.LADDER = [(0.4, 100)]                      # RUNG 0 ONLY -- the ruling field
    print('LADDER TRUNCATED: %r' % (NG.LADDER,), flush=True)
    rows = NC.load(); cfg = NC.cfg_from_chain(87, rows)
    res = {'Z': 88, 'clight': CINF, 'ladder': list(NG.LADDER), 'ref_cfg': cfg}
    t = time.time(); gr = NG.run_guarded(88, cfg, 'ref')
    res['ref'] = {k: gr[k] for k in ('E', 'it', 'rung', 'conv', 'err')}
    print('REF conv=%s it=%s E=%s' % (gr['conv'], gr['it'], gr['E']), flush=True)
    res['chan'] = {}
    for c, tag in [((7, 0), '7s'), ((6, 2), '6d'), ((5, 3), '5f')]:
        g = NG.run_guarded(88, NC.add(cfg, c), tag)
        e = {k: g[k] for k in ('E', 'it', 'rung', 'conv', 'err')}
        e['last_iterate'] = g.get('last_iterate')
        e['D'] = None if not g['conv'] else round(g['E'] - gr['E'], 5)
        e['D_last'] = None if g.get('last_iterate') is None else round(g['last_iterate'] - gr['E'], 5)
        res['chan'][tag] = e
        print('CHAN %s conv=%s it=%s D=%s D_last=%s' % (tag, g['conv'], g['it'], e['D'], e['D_last']), flush=True)
    res['sec'] = round(time.time() - t, 1)
    json.dump(res, open(out, 'w'), indent=1)
    print('WROTE', out, 'sec=%s' % res['sec'], flush=True)
    NG.C0 = CREL