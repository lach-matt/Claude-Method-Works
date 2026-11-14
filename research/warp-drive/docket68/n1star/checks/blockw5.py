#!/usr/bin/env python3
"""blockw5.py -- CERTIFY-10L5-RESULT.md round 6 (the verifier of round 5, m5-3): the block condition of 9.4 at
Theorem 8.W's weights.  Labels: computed (arithmetic on the printed outputs of blocks5.py and wgron5.py, every printed
figure rounded DOWN by half a unit of its last printed digit before use).

9.4 showed the block (Schur) condition fails on |x| <= 1/2 in the unweighted norms of Theorem 7.L.  Theorem 8.W's
constant 10^66.9 is in the weighted norms f_lam = sum_g lam_g f_g, S_lam = sum_rows lam_row S_row (W3's weights).  In
those norms the inverse blocks still have norm >= 1 (the data norm is weighted as the solution's), and the coupling
restricted to one (row bounding Y, unknown Z) pair scales by sqrt(lam_Y/lam_Z), so the product of the two couplings
of a pair (low -> high and high -> low through the same coefficient) scales by lam_Y/lam_Z.

  B1 (computed) for each of blocks5.out's six largest band pairs: the unweighted space-time coupling c (N >= 31), the
     groups of Y and Z (wgron5's GROUP: da_i, dc_i, dd_i -> phi_i), W3's log-weights, and c^2 lam_Y/lam_Z; and for the
     pair whose minimum over N = 0..30 blocks5 printed, that minimum weighted the same way.
  B2 the largest weighted product over the pairs (a lower bound for ||L_Ninf|| ||L_infN|| at W3's weights, every N
     for the pair with the all-N minimum): the block condition fails at W3's weights if it exceeds 1.
  Controls: (k1) equal weights reproduce blocks5's unweighted 484 (within the rounding margin); (k2) the minimum over
     pairs in place of the maximum must NOT exclude the condition (one pair alone can be weighted below 1: the
     conclusion rests on taking the largest coupling, and the program must see the difference).

  python3 checks/blockw5.py          (reads checks/blocks5.out and checks/wgron5.out)
"""
import os, re, sys, math

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


def down(txt, sig=None):
    """a printed number rounded down by half a unit of its last digit: of its last decimal (sig None, '%.2f'), or of
    its sig-th significant digit ('%.3g', whose trailing zeros are not printed)"""
    v = float(txt)
    if sig is not None:
        return v - 0.5 * 10 ** (math.floor(math.log10(abs(v))) - sig + 1)
    mant = txt.lower().split('e')[0]
    dec = len(mant.split('.')[1]) if '.' in mant else 0
    exp = int(txt.lower().split('e')[1]) if 'e' in txt.lower() else 0
    return v - 0.5 * 10 ** (exp - dec)


def parse_blocks(path):
    txt = open(path).read()
    band = txt[txt.index('H2 (computed) on |x| <= 0.5'):]
    flat = re.sub(r'\n\s+', ' ', band)
    pairs = []
    pat = r'(\S+) row \(bounds (\S+)\) <- (\S+) \[(\w+)\]: .*?space-time coupling >= ([0-9.e+-]+);'
    for m_ in re.finditer(pat, flat):
        pairs.append(dict(row=m_.group(1), bnd=m_.group(2), unk=m_.group(3), typ=m_.group(4), c=m_.group(5)))
    top = re.search(r'largest space-time coupling \((\S+) row <- (\S+)\): >= ([0-9.e+-]+) for every N >= \d+ '
                    r'\(N-independent, H1\), and for N = 0\.\.\d+ at least ([0-9.e+-]+)', flat)
    return pairs, (top.group(1), top.group(2), top.group(3), top.group(4))


def parse_weights(path):
    txt = re.sub(r'\n\s+', ' ', open(path).read())
    seg = re.search(r'W3 \|x\| <= 0\.5: optimal weights \(log lam, relative to the smallest\): (.*?) log\(max/min',
                    txt).group(1)
    return {k: v for k, v in re.findall(r'(\w+) ([0-9.]+)', seg)}


def group(n):
    m_ = re.match(r'd[acd](\d)$', n)
    return 'phi%s' % m_.group(1) if m_ else n


def weighted(pairs, top, w, use_weights=True, pick=max):
    """c^2 lam_Y/lam_Z per pair (N >= 31), the picked pair, and the all-N figure of blocks5's top pair"""
    out = []
    for p in pairs:
        gy, gz = group(p['bnd']), group(p['unk'])
        dt = (down(w[gy]) - (float(w[gz]) + 0.005)) if use_weights else 0.0      # rounded against the claim
        prod = down(p['c'], 3) ** 2 * math.exp(dt)
        out.append((prod, p, gy, gz, dt))
    best = pick(out, key=lambda e: e[0])
    tp = [e for e in out if (e[1]['row'], e[1]['unk']) == (top[0], top[1])][0]
    allN = min(down(top[2], 3), down(top[3], 3)) ** 2 * math.exp(tp[4])
    return out, best, (allN, tp)


def main():
    pairs, top = parse_blocks(os.path.join(HERE, 'blocks5.out'))
    w = parse_weights(os.path.join(HERE, 'wgron5.out'))
    ok = len(pairs) == 6
    out, best, (allN, tp) = weighted(pairs, top, w)
    print('B1 (computed) the six largest band pairs of blocks5.out at W3\'s weights (wgron5.out, |x| <= 0.5):')
    for prod, p, gy, gz, dt in out:
        print('   %s row (bounds %s, group %s) <- %s (group %s): c >= %s, log(lam_Y/lam_Z) >= %.2f, c^2 lam_Y/lam_Z >= '
              '%.3g' % (p['row'], p['bnd'], gy, p['unk'], gz, p['c'], dt, prod))
    print('B2 the largest at N >= 31: %s row <- %s, >= %.3g; blocks5\'s top pair (%s row <- %s), whose minimum over '
          'N = 0..30 it printed (%s), weighted: >= %.3g for EVERY N -> the block condition %s at W3\'s weights' % (
              best[1]['row'], best[1]['unk'], best[0], top[0], top[1], top[3], allN,
              'FAILS' if allN > 1 else 'is not excluded'))
    ok &= allN > 1 and best[0] > 1
    _, _, (a0, _) = weighted(pairs, top, w, use_weights=False)
    k1 = abs(a0 - 484.0) / 484.0 < 0.01
    print('   control (k1) equal weights: %.4g (blocks5: 484) -> %s' % (a0, 'reproduced' if k1 else 'NOT reproduced'))
    _, bmin, _ = weighted(pairs, top, w, pick=min)
    k2 = bmin[0] < 1
    print('   control (k2) the smallest pair in place of the largest: %s row <- %s, %.3g -> %s' % (
        bmin[1]['row'], bmin[1]['unk'], bmin[0], 'below 1, so the conclusion rests on the largest (good)' if k2 else
        'above 1 (the control does not separate)'))
    ok &= k1 and k2
    print('blockw5: %s' % ('all checks pass' if ok else 'FAILURES'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
