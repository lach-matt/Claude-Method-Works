#!/usr/bin/env python3
"""mtrunc5.py -- CERTIFY-10L5-RESULT.md round 8 (the verifier of round 7, M7-B): is the late region's constraint
violation the angular truncation's?  Labels: computed (arithmetic on the printed outputs of cpaxis5.py --nullstep at
800 rows for M = 32, 40, 48 and 56; the regularised scheme, cut 0.9).

The rule, fixed before the M = 48 and 56 runs were read (CERTIFY-10L5-RESULT.md 12.1).  For each band and areal-radius
class, m(M) is the interior Ric_xx monitor at 800 rows, on the 400-row nodes all compared runs keep.
  - 'angular truncation' if every step lowers it by at least a fifth: m(M + 8)/m(M) <= 0.8 for M = 32, 40, 48;
  - 'not truncation' if m(56)/m(48) >= 0.8 while m(56) exceeds ten times the class's 800-row null-step level L;
  - 'undecided' otherwise.
L is the largest m(M), over the four M, on the class's bands that converge at second order in the null step (v < 1.8
at 0.9-1.0 and 1.0-1.2; v < 2.0 at >= 1.2): there the monitor is the null step's, not the angle's.
  Controls: (k1) a sequence halving at each step must read 'angular truncation' on every band; (k2) the M = 32 values
  given for every M (no change with M) must read 'angular truncation' on no band, and 'not truncation' wherever
  m(32) > 10 L.

  python3 checks/mtrunc5.py     (reads checks/cpaxis5_a5.out, cpaxis5_a5_m48.out, cpaxis5_a5_m56.out)
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))


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
CLAIMED = {'0.9-1.0': 1.8, '1.0-1.2': 1.8, '>= 1.2': 2.0}


def parse(name):
    """{(class, band start): (m32 at 800 rows, mM at 800 rows)} from a cpaxis5.py --nullstep output"""
    t = re.sub(r'\n\s+', ' ', open(os.path.join(HERE, name)).read())
    out, cls = {}, None
    for m in re.finditer(r'(areal radius (0\.9-1\.0|1\.0-1\.2|>= 1\.2):)|v in \[(\S+), (\S+)\): monitor 400: \S+, '
                         r'800: (\S+) \(ratio \S+\); 800 at M = \d+: (\S+) \(', t):
        if m.group(1):
            cls = m.group(2)
        else:
            out[(cls, float(m.group(3)))] = (float(m.group(5)), float(m.group(6)))
    return out


def classify(seq, level):
    st = [seq[i + 1] / seq[i] for i in range(3)]
    if all(s <= 0.8 for s in st):
        return 'angular truncation', st
    if st[2] >= 0.8 and seq[3] > 10 * level:
        return 'not truncation', st
    return 'undecided', st


def levels(table):
    return {c: max(max(v) for (c_, b), v in table.items() if c_ == c and b < CLAIMED[c]) for c in CLAIMED}


def main():
    a40, a48, a56 = parse('cpaxis5_a5.out'), parse('cpaxis5_a5_m48.out'), parse('cpaxis5_a5_m56.out')
    ok = set(a40) == set(a48) == set(a56) and len(a40) == 21
    ok &= all(abs(a40[k][0] - a48[k][0]) <= 1e-12 + 1e-3 * a40[k][0] and abs(a40[k][0] - a56[k][0]) <= 1e-12 +
              1e-3 * a40[k][0] for k in a40)      # the same M = 32 file in all three
    table = {k: (a40[k][0], a40[k][1], a48[k][1], a56[k][1]) for k in a40}
    L = levels(table)
    print('M1 (computed) the interior Ric_xx monitor at 800 rows for M = 32, 40, 48, 56, its steps m(M + 8)/m(M), and '
          'the verdict by the fixed rule; the null-step level L per class: %s' % ', '.join('%s %.2e' % kv for kv in
                                                                                       L.items()))
    verdicts = {}
    for c in CLAIMED:
        print('  areal radius %s:' % c)
        for b in sorted(x for (c_, x) in table if c_ == c):
            seq = table[(c, b)]
            vd, st = classify(seq, L[c])
            if b < CLAIMED[c]:
                vd = 'claimed band (null-step level)'
            verdicts[(c, b)] = vd
            print('   v from %.2f: %s; steps %s -> %s' % (b, ', '.join('%.3g' % q for q in seq),
                                                       ', '.join('%.2f' % s for s in st), vd))
    k1 = all(classify([1.0, 0.5, 0.25, 0.125], L[c])[0] == 'angular truncation' for c in CLAIMED)
    k2 = True
    for (c, b), seq in table.items():
        v2 = classify([seq[0]] * 4, L[c])[0]
        k2 &= v2 != 'angular truncation' and (v2 == 'not truncation') == (seq[0] > 10 * L[c])
    print('   control (k1) a halving sequence reads angular truncation on every class: %s' % ('yes (good)' if k1 else
                                                                                         'NO'))
    print('   control (k2) M = 32 given for every M: never angular truncation, not truncation exactly where '
          'm(32) > 10 L: %s' % ('yes (good)' if k2 else 'NO'))
    ok &= k1 and k2
    print('mtrunc5: %s' % ('all checks pass' if ok else 'FAILURES'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
