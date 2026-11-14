#!/usr/bin/env python3
"""mtrunc5.py -- CERTIFY-10L5-RESULT.md rounds 8-10 (the verifiers of rounds 7 and 8, M7-B and M8-A): is the late
region's constraint violation consistent with angular truncation?  Labels: computed (arithmetic on the printed outputs
of cpaxis5.py --nullstep at 800 rows for M = 32, 40, 48 and 56; the regularised scheme, cut 0.9).

The rule (CERTIFY-10L5-RESULT.md 12.1; when it was written relative to reading the M = 48 and 56 outputs is not
documented: its first trace is this file's first commit, after those outputs were written).  For each band and
areal-radius class, m(M) is the interior Ric_xx monitor at 800 rows, on the 400-row nodes all compared runs keep.
  - 'consistent with angular truncation' if every step lowers it to at most theta of its value: m(M + 8)/m(M) <= theta
    for M = 32, 40, 48;
  - 'not truncation' if m(56)/m(48) >= theta while m(56) exceeds F times the class's 800-row null-step level L;
  - 'undecided' otherwise.
The verdicts are printed at theta = 0.8, F = 10, and then their sensitivity (M2): for every band the thresholds at
which its verdict changes, and the range of theta over which every decided verdict stands (round 9, M8-A), printed
to two decimals rounded inward and re-checked by classifying every decided band at both of its ends (round 10).
L is the largest m(M), over the four M, on the class's bands that converge at second order in the null step (v < 1.8
at 0.9-1.0 and 1.0-1.2; v < 2.0 at >= 1.2): there the monitor is the null step's, not the angle's.
  Controls: (k1) a sequence halving at each step must read 'consistent with angular truncation' on every band; (k2)
  the M = 32 values given for every M (no change with M) must never read so, and must read 'not truncation' exactly
  where m(32) > 10 L; (k3, round 9, m8-1) L's band set must be exactly the bands whose own 400 -> 800 ratio at M = 32 is
  second order, [3, 5.5], and none of the others; (k4, round 9, m8-1) run identity: each file's header must name the
  M = 32 runs at 400 and 800 rows and, third, the run at the M it is read for (40, 48, 56), so that files given in the
  wrong order or for the wrong M fail.

  python3 checks/mtrunc5.py     (reads checks/cpaxis5_a5.out, cpaxis5_a5_m48.out, cpaxis5_a5_m56.out)
"""
import math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CLAIMED = {'0.9-1.0': 1.8, '1.0-1.2': 1.8, '>= 1.2': 2.0}
FILES = (('cpaxis5_a5.out', 40), ('cpaxis5_a5_m48.out', 48), ('cpaxis5_a5_m56.out', 56))
TRUNC = 'consistent with angular truncation'


def print(*a, **k):
    """print, every line wrapped at 121 characters (the record's line limit)"""
    import builtins, textwrap
    s = (k.pop('sep', ' ')).join(str(q) for q in a)
    lines = []
    for ln in s.split('\n'):
        if len(ln) <= 121:
            lines.append(ln)
        else:
            ind = len(ln) - len(ln.lstrip()) + 4
            lines.extend(textwrap.wrap(ln, 121, subsequent_indent=' ' * ind, break_on_hyphens=False))
    builtins.print('\n'.join(lines), **k)


def header_runs(name):
    """the M of each run named on the file's command line (its first line)"""
    first = open(os.path.join(HERE, name)).readline()
    return [(int(m.group(1)), int(m.group(2))) for m in re.finditer(r'cp_M(\d+)_(\d+)_reg\.npz', first)]


def parse(name):
    """{(class, band start): (m32 at 800 rows, mM at 800 rows, M = 32's ratio 400/800)} from a --nullstep output"""
    t = re.sub(r'\n\s+', ' ', open(os.path.join(HERE, name)).read())
    out, cls = {}, None
    for m in re.finditer(r'(areal radius (0\.9-1\.0|1\.0-1\.2|>= 1\.2):)|v in \[(\S+), (\S+)\): monitor 400: \S+, '
                         r'800: (\S+) \(ratio (\S+)\); 800 at M = \d+: (\S+) \(', t):
        if m.group(1):
            cls = m.group(2)
        else:
            out[(cls, float(m.group(3)))] = (float(m.group(5)), float(m.group(7)), float(m.group(6)))
    return out


def classify(seq, level, theta=0.8, fac=10.0):
    st = [seq[i + 1] / seq[i] for i in range(3)]
    if all(s <= theta for s in st):
        return TRUNC, st
    if st[2] >= theta and seq[3] > fac * level:
        return 'not truncation', st
    return 'undecided', st


def levels(table, bands=None):
    bands = bands or (lambda c, b: b < CLAIMED[c])
    return {c: max(max(v) for (c_, b), v in table.items() if c_ == c and bands(c, b)) for c in CLAIMED}


def main():
    ok = True
    ids = {name: header_runs(name) for name, _ in FILES}
    k4 = all(ids[name] == [(32, 400), (32, 800), (M, 800)] for name, M in FILES)
    print('M0 run identity (k4): %s -> %s' % ('; '.join('%s: %s' % (n, ', '.join('M = %d at %d rows' % r for r in
                                                                                   ids[n])) for n, _ in FILES),
                                             'each file is the run it is read for (good)' if k4 else 'MISMATCH'))
    ok &= k4
    a = [parse(name) for name, _ in FILES]
    ok &= set(a[0]) == set(a[1]) == set(a[2]) and len(a[0]) == 21
    ok &= all(abs(a[0][k][0] - a[i][k][0]) <= 1e-12 + 1e-3 * a[0][k][0] for k in a[0] for i in (1, 2))
    table = {k: (a[0][k][0], a[0][k][1], a[1][k][1], a[2][k][1]) for k in a[0]}
    ratio32 = {k: a[0][k][2] for k in a[0]}
    L = levels(table)
    print('M1 (computed) the interior Ric_xx monitor at 800 rows for M = 32, 40, 48, 56, its steps m(M + 8)/m(M), and '
          'the verdict at theta = 0.8, F = 10; the null-step level L per class: %s' % ', '.join(
              '%s %.2e' % kv for kv in L.items()))
    beyond = {}
    for c in CLAIMED:
        print('  areal radius %s:' % c)
        for b in sorted(x for (c_, x) in table if c_ == c):
            seq = table[(c, b)]
            vd, st = classify(seq, L[c])
            if b < CLAIMED[c]:
                vd = 'claimed band (null-step level)'
            else:
                beyond[(c, b)] = (seq, st, vd)
            print('   v from %.2f: %s; steps %s -> %s' % (b, ', '.join('%.3g' % q for q in seq),
                                                       ', '.join('%.2f' % s for s in st), vd))
    # M2: sensitivity.  A band reads TRUNC for theta >= max(steps); 'not truncation' for theta <= last step when
    # m(56) > F L, i.e. for F < m(56)/L; otherwise undecided.
    print('M2 (computed) sensitivity: per band beyond, the theta at and above which it reads %s (max step), the theta '
          'at and below which it reads not truncation (last step, when m(56) > F L), and m(56)/L, the largest F for '
          'that:' % TRUNC)
    decided = {k: v[2] for k, v in beyond.items() if v[2] != 'undecided'}
    lo = max((max(v[1]) for k, v in beyond.items() if decided.get(k) == TRUNC), default=float('nan'))
    hi = min((v[1][2] for k, v in beyond.items() if decided.get(k) == 'not truncation'), default=float('nan'))
    for (c, b), (seq, st, vd) in sorted(beyond.items()):
        print('   %s from %.2f: truncation for theta >= %.3f; not truncation for theta <= %.3f with F < %.3g -> at '
              '0.8: %s' % (c, b, max(st), st[2], seq[3] / L[c], vd))
    flips = sorted((max(st), (c, b)) for (c, b), (seq, st, vd) in beyond.items() if vd == 'undecided')
    lo2, hi2 = math.ceil(lo * 100 - 1e-9) / 100, math.floor(hi * 100 + 1e-9) / 100
    ends = all(classify(beyond[k][0], L[k[0]], theta=th)[0] == vd for k, vd in decided.items() for th in (lo2, hi2))
    print('   every decided verdict (%d) stands for theta in [%.2f, %.2f] (F = 10; the exact ends %.4f and %.4f, '
          'rounded inward; re-checked at both ends: %s); the undecided bands read %s from theta = %s' % (
              len(decided), lo2, hi2, lo, hi, 'yes' if ends else 'NO', TRUNC,
              ', '.join('%.3f (%s from %.2f)' % (t, c, b) for t, (c, b) in flips)))
    for (c, b), (seq, st, vd) in sorted(beyond.items()):
        if vd == 'undecided' and seq[3] > 10 * L[c]:
            print('   %s from %.2f reads not truncation for theta <= %.3f' % (c, b, st[2]))
    ok &= lo < 0.8 < hi and ends
    # controls
    k1 = all(classify([1.0, 0.5, 0.25, 0.125], L[c])[0] == TRUNC for c in CLAIMED)
    k2 = True
    for (c, b), seq in table.items():
        v2 = classify([seq[0]] * 4, L[c])[0]
        k2 &= v2 != TRUNC and (v2 == 'not truncation') == (seq[0] > 10 * L[c])
    sec = {k for k, r in ratio32.items() if 3 <= r <= 5.5}
    used = {k for k in table if k[1] < CLAIMED[k[0]]}
    k3 = sec == used and levels(table, lambda c, b: (c, b) in sec) == L
    print('   control (k1) a halving sequence reads %s on every class: %s' % (TRUNC, 'yes (good)' if k1 else 'NO'))
    print('   control (k2) M = 32 given for every M: never %s, not truncation exactly where m(32) > 10 L: %s' % (
        TRUNC, 'yes (good)' if k2 else 'NO'))
    print('   control (k3) L\'s bands are exactly those whose M = 32 ratio 400/800 lies in [3, 5.5] (%d of %d): %s' % (
        len(used), len(table), 'yes (good)' if k3 else 'NO'))
    ok &= k1 and k2 and k3
    print('mtrunc5: %s' % ('all checks pass' if ok else 'FAILURES'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
