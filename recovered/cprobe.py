"""cprobe.py -- s54.  THE c-SENSITIVITY PROBE.  F54.2 REMEDY AND PRECONDITION.

Scores PREDICTION-CPROBE.md (sha256 db654c3d23fba6eb..., filed 2026-08-20T13:58:03Z,
BEFORE this file was written).  R 1449.

WHAT IT DOES.  One SCF reference solve through nlguard.run_guarded -- the SAME entry the
walk uses -- on the SAME chained reference configuration, at two values of c, for two
atoms.  Then it reproduces the s53 lever as a null.

THE LEVER.  nlguard.py:64 calls H.HFC(Z, cfg, c=C0) where C0 is nlguard's own
module-level binding.  Rebinding nlguard.C0 is therefore necessary AND sufficient for the
walk path.  t7c_hfsr.py:39 passes self.c POSITIONALLY into eigen_sr, so eigen_sr's
default is unreachable -- which is why s53's patch was doubly dead (F54.2).

NO SEALED FILE IS MODIFIED.  C0 is rebound in memory (F44.1 precedent).

CAN-FAIL:
  --null      set both legs to c=137.035999.  CP-1 must then FAIL.
  --s53lever  drive the c=1e6 leg with s53's dead patch instead of the real lever.
              CP-1 must then FAIL, and that failure IS the F54.2 demonstration.

usage: python3 cprobe.py [--null] [--s53lever]
"""
import json, os, sys, time, hashlib

D = os.path.dirname(os.path.abspath(__file__))
RT = os.path.join(D, '..', 'rt')
sys.path.insert(0, RT)
os.chdir(RT)

NULL = '--null' in sys.argv
S53LEVER = '--s53lever' in sys.argv

CREL = 137.035999
CINF = 1e6
ZS = [10, 80]

p = os.path.join(D, 'PREDICTION-CPROBE.md')
print('  scoring %s  sha256 %s' % ('PREDICTION-CPROBE.md',
      hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]))
print('  mode: %s' % ('NULL CAN-FAIL' if NULL else
                      ('s53 DEAD-LEVER CAN-FAIL' if S53LEVER else 'LIVE')))

import nlchain as NC
import nlguard as NG
import t7c_kernel as K

sealed = NC.load()


def s53_patch(c):
    """s53's lever, verbatim from pack52/cinf.py / pack53/induct.py. Reproduced to be
    shown dead, not to be used."""
    n = 0
    for name in ('eigen_sr', 'numerov_wf_sr', 'scf_occ_sr'):
        f = getattr(K, name)
        d = list(f.__defaults__)
        co = f.__code__
        names = co.co_varnames[:co.co_argcount]
        off = co.co_argcount - len(d)
        for i, nm in enumerate(names[off:]):
            if nm == 'c':
                d[i] = c
                n += 1
        f.__defaults__ = tuple(d)
    return n


def solve(Z, c, use_s53_lever=False):
    """one reference solve at speed of light c, through the walk's own entry"""
    cfg = NC.cfg_from_chain(Z - 1, sealed)
    if use_s53_lever:
        s53_patch(c)                 # the dead lever
        NG.C0 = CREL                 # the live one left alone -- this is the point
    else:
        NG.C0 = c                    # the live lever
    t = time.time()
    g = NG.run_guarded(Z, cfg, 'cprobe')
    return dict(Z=Z, c=c, E=g['E'], conv=g['conv'], rung=g['rung'],
                it=g['it'], sec=round(time.time() - t, 1))


res = {}
for Z in ZS:
    a = solve(Z, CREL)
    b = solve(Z, CREL if NULL else CINF, use_s53_lever=S53LEVER)
    NG.C0 = CREL                     # always restore
    s53_patch(CREL)
    res[Z] = (a, b)
    print('    Z=%-4d E(c=137.035999)=%-14r E(c=%g)=%-14r  dE=%+.6f  %ss'
          % (Z, a['E'], b['c'], b['E'], b['E'] - a['E'], a['sec'] + b['sec']))

fails = []


def chk(name, got, want):
    ok = (got == want)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:<38} got {got}  want {want}")
    if not ok:
        fails.append(name)


d10 = abs(res[10][1]['E'] - res[10][0]['E'])
d80 = abs(res[80][1]['E'] - res[80][0]['E'])

print()
chk('CP-1 |dE| at Z=80 exceeds 1 mHa', d80 > 1e-3, True)
chk('CP-2 |dE(Z=10)| < |dE(Z=80)|', d10 < d80, True)
chk('CP-4 all solves converged', all(x['conv'] for p in res.values() for x in p), True)
chk('CP-4 all at rung 0', sorted({x['rung'] for p in res.values() for x in p}), [0])
chk('CP-5 c=1e6 energy HIGHER at Z=80', res[80][1]['E'] > res[80][0]['E'], True)

print()
print('  |dE| Z=10 = %.6f Ha     |dE| Z=80 = %.6f Ha     ratio = %s'
      % (d10, d80, ('%.1f' % (d80 / d10)) if d10 > 0 else 'inf'))

print()
print('CPROBE: ' + ('PASS -- c is connected; clause-3 work may resume'
                    if not fails else 'FAIL -- ' + ', '.join(fails)))
sys.exit(1 if fails else 0)
