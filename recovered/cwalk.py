"""cwalk.py -- s54.  THE CLAUSE-3 WALK, ON THE LEVER THAT ACTUALLY MOVES c.

Supersedes pack52/cinf.py and pack53/induct.py, both of which drove a dead lever (F54.2).

THE ONE DIFFERENCE THAT MATTERS:
    s53:  patched t7c_kernel.{eigen_sr,numerov_wf_sr,scf_occ_sr}.__defaults__
          -- none on the walk's path; t7c_hfsr.py:39 passes self.c POSITIONALLY.
    s54:  nlguard.C0 = c
          -- nlguard.py:64 is H.HFC(Z, cfg, c=C0); this is the walk's only solver entry.

Verified live by cprobe.py: |dE(Z=80)| = 1206.45 Ha on this lever, 0.0 on s53's.

Reference is CHAINED -- cfg_from_chain(Z-1) -- so F53.2's confound cannot arise: the
c=1e6 walk and the sealed walk see the same reference configuration by construction.

SELF-CHECK BEFORE ANY ROW.  The walker refuses to compute if the lever is not moving:
it re-runs the Z=80 sensitivity check and exits rc=4 unless |dE| > 1 mHa.  An instrument
that varies a parameter must demonstrate the parameter moves the number -- every time it
runs, not once.

NO SEALED FILE IS MODIFIED.  C0 is rebound in memory (F44.1 precedent).

usage: python3 cwalk.py OUT.jsonl Z [Z...]
"""
import sys, os, json, time

D = os.path.dirname(os.path.abspath(__file__))
RT = os.path.join(D, '..', 'rt')
sys.path.insert(0, RT)
os.chdir(RT)

CINF = 1e6
CREL = 137.035999

import nlchain as NC
import nlguard as NG


def lever_live():
    """refuse to walk unless c demonstrably moves the object. rc=4 if dead."""
    cfg = NC.cfg_from_chain(79, NC.load())
    NG.C0 = CREL
    a = NG.run_guarded(80, cfg, 'selfcheck')['E']
    NG.C0 = CINF
    b = NG.run_guarded(80, cfg, 'selfcheck')['E']
    d = abs(b - a)
    print('SELFCHECK Z=80  E(c=137.035999)=%.6f  E(c=1e6)=%.6f  |dE|=%.6f Ha'
          % (a, b, d), flush=True)
    return d


if __name__ == '__main__':
    out = sys.argv[1]
    ZS = [int(z) for z in sys.argv[2:]]

    d = lever_live()
    if not d > 1e-3:
        print('HALT: lever is DEAD (|dE| = %.9f). No row computed. F54.2 not remedied.' % d)
        sys.exit(4)
    print('LEVER LIVE. walking %d rows at c=%g on the CHAINED reference.'
          % (len(ZS), CINF), flush=True)

    NG.C0 = CINF
    rows = NC.load()
    fh = open(out, 'a')
    for Z in ZS:
        t = time.time()
        r = NC.step(Z, NC.cfg_from_chain(Z - 1, rows), rows, 'c3-chainref')
        r['sec'] = round(time.time() - t, 1)
        r['clight'] = CINF
        r['lever'] = 'nlguard.C0'
        fh.write(json.dumps(r) + '\n')
        fh.flush()
        print('DONE Z=%d ent=%s sealed=%s margin=%s sealed_margin=%s sec=%s'
              % (Z, r['ent'], rows[Z]['ent'], r['margin'], rows[Z]['margin'], r['sec']),
              flush=True)
    fh.close()
    NG.C0 = CREL
