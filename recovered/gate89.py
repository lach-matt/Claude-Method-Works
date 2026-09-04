"""gate89.py -- s54. SCORES PREDICTION-C3RESUME.md (ef7bc9c19f8528753ba6776c5401d96d...,
filed 2026-08-20T14:01:10Z, BEFORE the first row of the fail-fast walk).

Scores C3-1..C3-5 on the genuine c=1e6 chained-reference walk produced by pack54/cwalk.py
on the nlguard.C0 lever. NOTHING here is scored against s53's null chains.

CAN-FAIL: --expect-fail inverts C3-1; a doctored entrant must also FAIL.
usage: python3 gate89.py C3.jsonl [--expect-fail]
"""
import json, os, sys, hashlib

D = os.path.dirname(os.path.abspath(__file__))
RT = os.path.join(D, '..', 'rt')
sys.path.insert(0, RT)
os.chdir(RT)
import nlchain as NC

IN = sys.argv[1] if len(sys.argv) > 1 else '/tmp/c3.jsonl'
FLIP = '--expect-fail' in sys.argv

SET = [55, 56, 57, 72, 88, 89, 90, 105]
SCHAN = {55: 's', 56: 's', 88: 's'}      # C3-3: s-channel entrants
DCHAN = {57: 'd', 72: 'd', 89: 'd', 90: 'd', 105: 'd'}

p = os.path.join(D, 'PREDICTION-C3RESUME.md')
print('  scoring PREDICTION-C3RESUME.md  sha256 %s'
      % hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16])

sealed = {d['Z']: d for d in map(json.loads, open('nlchain.jsonl'))}
c3 = {d['Z']: d for d in map(json.loads, open(IN))}

fails = []


def chk(name, got, want):
    ok = (got == want)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:<38} got {got}  want {want}")
    if not ok:
        fails.append(name)


chk('rows present', sorted(c3), SET)
chk('lever is nlguard.C0', sorted({r.get('lever') for r in c3.values()}), ['nlguard.C0'])
chk('clight is 1e6', sorted({r.get('clight') for r in c3.values()}), [1e6])

# C3-1 DECISIVE
bad = [Z for Z in SET if c3[Z]['ent'] != sealed[Z]['ent']]
chk('C3-1 c=1e6 entrant == sealed', bad, [] if not FLIP else [0])

# C3-2 margins genuinely move -- the clause that would have caught F54.2
shift = {Z: abs(c3[Z]['margin'] - sealed[Z]['margin']) for Z in SET}
chk('C3-2 some |dmargin| > 1 mHa', max(shift.values()) > 1e-3, True)
chk('C3-2 no shift is identically zero', [Z for Z in SET if shift[Z] == 0.0], [])

# C3-5 candidate sets identical (chained reference by construction)
cs = [Z for Z in SET if sorted(dict(c3[Z]['order'])) != sorted(dict(sealed[Z]['order']))]
chk('C3-5 candidate sets identical', cs, [])

# C3-4 convergence
chk('C3-4 all at rung 0', sorted({r for x in c3.values() for r in x['rungs']}), [0])

print()
print('  --- C3-3, the sign structure, per step (measured, not asserted) ---')
print('  Z    ent  sealed  margin_sealed  margin_c1e6   dmargin   D_ent sealed -> c=1e6')
for Z in SET:
    r, s = c3[Z], sealed[Z]
    print('  %-4d %-4s %-6s %-14.5f %-13.5f %+8.5f  %+.5f -> %+.5f'
          % (Z, r['ent'], s['ent'], s['margin'], r['margin'],
             r['margin'] - s['margin'], s['D_ent'], r['D_ent']))
sw = [Z for Z in SCHAN if c3[Z]['margin'] < sealed[Z]['margin']]
dw = [Z for Z in DCHAN if c3[Z]['margin'] > sealed[Z]['margin']]
print()
print('  s-entrant steps whose margin NARROWS without relativity : %s of %s'
      % (sorted(sw), sorted(SCHAN)))
print('  d-entrant steps whose margin WIDENS  without relativity : %s of %s'
      % (sorted(dw), sorted(DCHAN)))

print()
print('  VERDICT: ' + ('the ordering clause SURVIVES c -> infinity at the 8 steps most '
                       'able to break it.\n           This LICENSES the remaining 99 rows. '
                       'It does NOT close clause 3.'
                       if not bad else
                       'COUNTEREXAMPLE at Z=%s -- Deliverable 1 6.1 STANDS.' % bad))
print()
print('GATE89: ' + ('PASS -- all clauses' if not fails else 'FAIL -- ' + ', '.join(fails)))
sys.exit(1 if fails else 0)
