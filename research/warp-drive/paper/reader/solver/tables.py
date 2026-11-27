"""The printed tables of a case (P-APPC sec:appc-format) from the solver's Chebyshev coefficients.
usage: tables.py case run.coef out_prefix p_R p_m p_n p_W p_s   (quanta 10^-p per field; or 'auto:GAP:F' to put
       p = ceil(-log10 F) + GAP for every field)
Writes out_prefix_tables.txt (the blocks, in the order of P-APPC: elements by i then j, fields R, m, n, W, s, each
read back with every line check and block sum verified), out_prefix.json (rows, entries, lines, pages at 79 lines,
degrees per block), out_prefix_approx.txt (for evalres) and out_prefix_z.pkl (the integers, for the certification)."""
import sys, os, json, math, pickle, numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import approx
NAPP1 = os.environ.get('NAPP1', '/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/napp1')
sys.path.insert(0, NAPP1)
import rep

def quantize_parts(parts, p):
    """z = round(C 10^p), C = sum of the NW double parts exactly; staircase |C| >= 10^-p/2 (else 0)"""
    approxv = parts[..., 0] * float(10.0 ** p)
    z = np.zeros(parts.shape[:-1], dtype=object)
    sc = 10 ** p
    for t in zip(*np.nonzero(np.abs(approxv) >= 0.45)):
        v = sum(Fr(float(q)) for q in parts[t]) * sc
        zi = round(v)
        if abs(v) >= Fr(1, 2): z[t] = zi
    return z

def trim(z):
    """smallest box containing the nonzero entries"""
    nz = np.argwhere(z != 0)
    if len(nz) == 0: return z[:1, :1, :1]
    hi = nz.max(0) + 1
    return z[:hi[0], :hi[1], :hi[2]]

def main():
    case, coef, out = sys.argv[1], sys.argv[2], sys.argv[3]
    C = approx.read_coef(coef)
    L = rep.layout(case)
    if sys.argv[4].startswith('auto'):
        _, gap, F = sys.argv[4].split(':'); P = [math.ceil(-math.log10(float(F)) + float(gap))] * 5
    else:
        P = [int(a) for a in sys.argv[4:9]]
    text = []; meta = []; blocks = {}; zs = {}
    e = 0
    for i, (mx, hx) in enumerate(L['xi']):
        for j, (mv, hv) in enumerate(L['v']):
            for f, F in enumerate(approx.FN):
                z = trim(quantize_parts(C[e][f], P[f]))
                head = ('element (%d,%d): ξ in [%s, %s], v in [%s, %s]; field %s; p = %d' %
                        (i + 1, j + 1, mx - hx, mx + hx, mv - hv, mv + hv, F, P[f])).replace('-', '−')
                lines, nr, ne = rep.print_block(z, head)
                z2, ok, bad = rep.read_block([l[4:] for l in lines], z.shape)
                assert ok and (np.array(z2, dtype=object) == z).all(), (i, j, F)
                assert max(len(l) for l in lines) <= 121
                text += lines + ['']
                nz = np.argwhere(z != 0)
                deg = [int(q) for q in nz.max(0)] if len(nz) else [0, 0, 0]
                digits = sum(len(str(abs(int(q)))) for q in z.flat if q != 0)
                meta.append(dict(el=[i + 1, j + 1], field=F, p=P[f], rows=nr, entries=ne, nonzero=int(len(nz)), digits=digits,
                                 degrees=deg, lines=len(lines)))
                blocks[(i, j, f)] = (P[f], z); zs['%d_%d_%s' % (i, j, F)] = (P[f], z)
            e += 1
    open(out + '_tables.txt', 'w').write('\n'.join(text))
    nl = sum(1 for l in text if l.strip())
    tot = sum(m['entries'] for m in meta)
    json.dump(dict(case=case, quanta=P, entries=tot, lines=nl, pages79=nl / 79, blocks=meta), open(out + '.json', 'w'), indent=1)
    pickle.dump(zs, open(out + '_z.pkl', 'wb'))
    approx.write_approx(case, blocks, out + '_approx.txt')
    print('%s: quanta %s; %d entries, %d lines, %.0f pages (79 lines); all blocks read back with checks' % (case, P, tot, nl, nl / 79))

if __name__ == '__main__':
    main()
