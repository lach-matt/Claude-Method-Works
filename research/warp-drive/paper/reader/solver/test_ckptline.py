"""Regression test for ckptline.py: the line coordinates of a checkpoint follow the quadrant being marched and the
configured breakpoints (solver.cpp main: breaks(), the quadrant's sides, make_geom).

    python3 test_ckptline.py            # tests ckptline.py next to this file; CKPTLINE=path tests another copy

Builds two small synthetic double-double checkpoints (BSOLV1) against one configuration with explicit, unequal
'xibreaks' on side 0 and explicit 'vbreaks' on side 1:
  A. quadrant Q1 after column 2: xi must be the third explicit breakpoint (-8.6), not 2/3 of the way to xi_hi;
  B. quadrant Q4 after column 1: xi must be xi_lo (side 1 of xi), and the one row's v-nodes must run from 1/2 down to
     0.4 (side 1 of v), Radau, excluding 1/2 and including 0.4.
Exit status 0 when both hold."""
import os, sys, struct, subprocess, tempfile, numpy as np, mpmath as mp
mp.mp.dps = 50
HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.environ.get('CKPTLINE', os.path.join(HERE, 'ckptline.py'))
PV, M = 3, 4
NB, NX = PV + 1, M + 1
XI0 = mp.asinh(mp.mpf(-4500))

def write_ckpt(fn, qi, col, nl):
    with open(fn, 'wb') as f:
        f.write(b'BSOLV1'); f.write(struct.pack('<ii', qi, col)); f.write(struct.pack('<ddd', 0.0, 0.0, 0.0))
        f.write(struct.pack('<i', nl))
        for j in range(nl):
            a = np.full((4, NB, NX, 2), float(j + 1)); a[..., 1] = 0
            f.write(struct.pack('<q', 4 * NB * NX)); f.write(a.astype('<f8').tobytes())
            f.write(struct.pack('<q', 0))
        f.write(struct.pack('<i', 0))                       # no elements
        for s in range(2): f.write(struct.pack('<q', 0)); f.write(struct.pack('<i', 0))

def run(d, qi, col, nl):
    ck = os.path.join(d, 'c%d.ckpt' % qi); out = os.path.join(d, 'o%d.npz' % qi)
    write_ckpt(ck, qi, col, nl)
    r = subprocess.run([sys.executable, SCRIPT, os.path.join(d, 't.cfg'), ck, out], capture_output=True, text=True)
    if r.returncode: return None, r.stdout + r.stderr
    z = np.load(out); return z, r.stdout

def main():
    fails = []
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, 't.cfg'), 'w').write('\n'.join([
            'lam 1', 'pxi 2', 'pv %d' % PV, 'M %d' % M, 'domain -9.2 -8.0 0.4 1.0', 'cells 3 1 2 1',
            'xibreaks 0 4 %s -9.0 -8.6 -8.0' % mp.nstr(XI0, 45), 'vbreaks 1 2 0.5 0.4', 'quadrants 1234', '']))
        # A: Q1 (index 0), after column 2, two rows (side 0 of v, equal: 0.5, 0.75, 1.0)
        z, msg = run(d, 0, 2, 2)
        if z is None: fails.append('A: script failed: ' + msg)
        else:
            if abs(mp.mpf(str(z['xi'])) - mp.mpf('-8.6')) > mp.mpf('1e-35'): fails.append('A: xi %s, expected -8.6' % z['xi'])
            v = [[mp.mpf(q) for q in row] for row in z['v']]
            if abs(v[0][-1] - mp.mpf('0.75')) > mp.mpf('1e-35') or abs(v[1][-1] - 1) > mp.mpf('1e-35'):
                fails.append('A: row ends %s %s, expected 0.75, 1.0' % (v[0][-1], v[1][-1]))
        # B: Q4 (index 3), after column 1, one row (side 1 of v: 0.5 down to 0.4)
        z, msg = run(d, 3, 1, 1)
        if z is None: fails.append('B: script failed: ' + msg)
        else:
            if abs(mp.mpf(str(z['xi'])) - mp.mpf('-9.2')) > mp.mpf('1e-35'): fails.append('B: xi %s, expected -9.2' % z['xi'])
            v = [mp.mpf(q) for q in z['v'][0]]
            rad = sorted(mp.cos(2 * mp.pi * b / (2 * PV + 1)) for b in range(PV + 1))
            want = [mp.mpf('0.5') - mp.mpf('0.05') * (t + 1) for t in rad]
            if max(abs(a - b) for a, b in zip(v, want)) > mp.mpf('1e-35'):
                fails.append('B: v-nodes %s, expected %s' % ([mp.nstr(q, 8) for q in v], [mp.nstr(q, 8) for q in want]))
            if not (all(q < mp.mpf('0.5') for q in v) and abs(v[-1] - mp.mpf('0.4')) < mp.mpf('1e-35')):
                fails.append('B: v-nodes must lie below 1/2 and end at 0.4')
    for m in fails: print('FAIL', m)
    print('ckptline test (%s): %s' % (SCRIPT, 'FAIL' if fails else 'ok'))
    sys.exit(1 if fails else 0)

if __name__ == '__main__':
    main()
