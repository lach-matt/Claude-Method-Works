"""gate88b.py -- s54.  F54.1 REMEDY.  SCORES IN-4 AND NOTHING ELSE.

WHY THIS EXISTS.  PREDICTION-INDUCTION.md (filed 2026-08-20T03:39:21Z, sha256
8a9aef3f95..., BEFORE the first induction row) states five clauses IN-1..IN-5.
pack53/gate88.py scores IN-1, IN-2, IN-3 and IN-5.  It does NOT score IN-4.
A clause filed in a pre-run prediction that no instrument scores is a SILENT PASS,
which is the F44.1 fault exactly.  This gate closes that hole.

NO SEALED FILE IS TOUCHED (F44.1 precedent).  gate88.py is read only for its
provenance hash, never modified.

IN-4 AS FILED, VERBATIM:
    "Margins shift but never invert. |margin(c=1e6) - margin(sealed)| stays below
     the sealed margin at every one of the 34 steps, which is what 'no inversion'
     means quantitatively. Largest shifts at Z >= 92."

Two testable propositions, scored separately, NEITHER REWORDED:
    IN-4a  for every one of the 34 induction steps: |dmargin| < margin_sealed
    IN-4b  the largest |dmargin| over the 34 steps occurs at some Z >= 92

CAN-FAIL: pass --expect-fail to invert IN-4a's expectation; the gate must then
report FAIL.  Feeding a doctored margin must also produce FAIL.

usage: python3 gate88b.py INDUCT.jsonl [--expect-fail]
"""
import json, os, sys, hashlib

D = os.path.dirname(os.path.abspath(__file__))
RT = os.path.join(D, '..', 'rt')
P53 = os.path.join(D, '..', 'pack53')
sys.path.insert(0, RT)

IN = sys.argv[1] if len(sys.argv) > 1 else '/tmp/induct.jsonl'
FLIP = '--expect-fail' in sys.argv

os.chdir(RT)
sealed = {d['Z']: d for d in map(json.loads, open('nlchain.jsonl'))}
ind = {d['Z']: d for d in map(json.loads, open(IN))}

# provenance: the sealed gate this one supplements, and the prediction it scores
for f in ('gate88.py', 'PREDICTION-INDUCTION.md'):
    p = os.path.join(P53, f)
    print('  provenance %-26s sha256 %s' % (f, hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]))

CONF = sorted(ind)
fails = []


def chk(name, got, want):
    ok = (got == want)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:<34} got {got}  want {want}")
    if not ok:
        fails.append(name)


chk('rows to score', len(CONF), 34)

# ---- IN-4a  no inversion: |dmargin| < margin_sealed at every step -------------
shift = {}
for Z in CONF:
    ms, mi = sealed[Z]['margin'], ind[Z]['margin']
    shift[Z] = abs(mi - ms)

viol = sorted(Z for Z in CONF if not (shift[Z] < sealed[Z]['margin']))
chk('IN-4a |dmargin| < margin_sealed', viol, [] if not FLIP else [0])

# ---- IN-4b  largest shift at Z >= 92 ------------------------------------------
zmax = max(CONF, key=lambda Z: shift[Z])
chk('IN-4b argmax|dmargin| >= 92', zmax >= 92, True)

print()
print('  --- the five largest shifts, for the record ---')
for Z in sorted(CONF, key=lambda z: -shift[z])[:5]:
    print('    Z=%-4d sealed_margin=%.5f  ind_margin=%.5f  |d|=%.5f  ratio=%.3f'
          % (Z, sealed[Z]['margin'], ind[Z]['margin'], shift[Z],
             shift[Z] / sealed[Z]['margin']))
print('    max ratio over all 34 = %.3f at Z=%d'
      % (max(shift[Z] / sealed[Z]['margin'] for Z in CONF),
         max(CONF, key=lambda Z: shift[Z] / sealed[Z]['margin'])))

print()
print('GATE88B: ' + ('PASS -- IN-4 holds as filed' if not fails
                     else 'FAIL -- ' + ', '.join(fails)))
sys.exit(1 if fails else 0)
