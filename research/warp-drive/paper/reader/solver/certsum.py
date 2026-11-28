"""Collect the certificate of each element: its own residual (cert3.py, prop:appc-element-bound) and the overlap
correction (overlapK.py, prop:appc-overlap), per derivative order |alpha| <= K in the element's (t, sigma, x).

    python3 certsum.py CERTDIR [mu ...]          (CERTPREFIX=c37_ OVPREFIX=ov37_ for other names)

reads CERTDIR/c30_ij.json and CERTDIR/ovK_ij.json (by default) and prints, per element and order, the own bound, the largest
overlap Lambda over the element's strips, and B = own + Lambda (the certificate eq:appc-certificate on U_ij); with mu
given, also max_|alpha|<=K mu^(|alpha|/2) B_alpha -- an indicative weighting only: the level-K norm weights the Lie
derivatives along the commutation fields, which are combinations of these (pending:lem-tl5-f3-residual).
"""
import json, os, sys
from fractions import Fraction

CP = os.environ.get('CERTPREFIX', 'c30_'); OP = os.environ.get('OVPREFIX', 'ovK_')

def load(d, ij):
    c = json.load(open(os.path.join(d, CP + '%d%d.json' % ij)))
    op = os.path.join(d, OP + '%d%d.json' % ij)
    o = json.load(open(op)) if os.path.exists(op) else []
    K = c['K']
    own = [0.0] * (K + 1); main = [0.0] * (K + 1)
    for ab, per in c['bounds'].items():
        for a, v in per.items():
            k = sum(int(ch) for ch in a)
            own[k] = max(own[k], v['main'] + v['tail']); main[k] = max(main[k], v['main'])
    lam = [0.0] * (K + 1)
    for s in o:
        # slivers (width < 1/1000, outside U_ij; overlapK.py drops them since, older JSON files still carry them)
        if any(Fraction(r[1]) - Fraction(r[0]) < Fraction(1, 1000) for r in s['strip']):
            continue
        for k, v in s['Lambda_by_order'].items():
            if int(k) <= K:
                lam[int(k)] = max(lam[int(k)], v)
    return c, own, main, lam

def main():
    d = sys.argv[1]; mus = [float(m) for m in sys.argv[2:]]
    for ij in [(1, 1), (1, 2), (2, 1), (2, 2)]:
        if not os.path.exists(os.path.join(d, CP + '%d%d.json' % ij)):
            print('element', ij, ': no certificate yet'); continue
        c, own, mn, lam = load(d, ij)
        print('element (%d,%d): N = %s, rho = %s, M = %.3g, nodes %d, %d s' % (ij + (c['N'], c['rho'], c['M'],
              c['nodes'], round(sum(c['times'].values())))))
        B = [own[k] + lam[k] for k in range(len(own))]
        for k in range(len(own)):
            print('  |alpha| = %d: own %.3g (sum|c| %.3g, tail %.3g)  overlap %.3g  B %.3g' % (k, own[k], mn[k],
                  own[k] - mn[k], lam[k], B[k]))
        for mu in mus:
            w = [mu ** (k / 2) * B[k] for k in range(len(B))]
            kk = max(range(len(w)), key=lambda k: w[k])
            print('  mu = %g: max_k mu^(k/2) B_k = %.3g (at |alpha| = %d); level 0..3 only: %.3g' % (mu, w[kk], kk,
                  max(w[:4])))

if __name__ == '__main__':
    main()
