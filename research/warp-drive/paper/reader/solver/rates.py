"""Geometric decay rates of the solver's element coefficients per element, field and direction (t, sigma, x), against
S-APP's measured rates (scratchpad/sapp/rates_*.json, from the record's double-precision runs).
Rate: geometric fit of the running-maximum envelope of max|C| over the other two indices, between A/10^2 and
10^3 x the floor (the floor: the coefficient level where the envelope stops decaying).
usage: rates.py case run.coef [sapp_rates.json] [out.json]"""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import approx
sys.path.insert(0, approx.os.environ.get('NAPP1', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'napp1')))
import rep

def rate(env, lo, hi):
    k = np.arange(len(env)); e = np.maximum.accumulate(env[::-1])[::-1]
    sel = (e < hi) & (e > lo)
    if sel.sum() < 4: return float('nan'), 0
    return float(np.exp(-np.polyfit(k[sel], np.log(e[sel]), 1)[0])), int(sel.sum())

def main():
    case, cf = sys.argv[1], sys.argv[2]
    C = approx.read_coef(cf); L = rep.layout(case)
    sapp = json.load(open(sys.argv[3])) if len(sys.argv) > 3 and sys.argv[3] != '-' else None
    out = []; e = 0
    for i, (mx, hx) in enumerate(L['xi']):
        for j, (mv, hv) in enumerate(L['v']):
            row = {}
            for f, F in enumerate(approx.FN):
                c = np.abs(C[e][f][..., 0] + C[e][f][..., 1])
                A = c.max()
                envs = [c.max(axis=(1, 2)), c.max(axis=(0, 2)), c.max(axis=(0, 1))]
                floor = min(np.median(en[-8:]) for en in envs)
                rr = [rate(en, max(1e3 * floor, 1e-34), A / 100) for en in envs]
                row[F] = dict(A=float(A), floor=float(floor), rho=[r[0] for r in rr], npts=[r[1] for r in rr],
                              deg_at_floor=[int(np.nonzero(np.maximum.accumulate(en[::-1])[::-1] > 10 * floor)[0].max()) if (en > 10 * floor).any() else 0 for en in envs])
            u0, u1 = rep.u_of_xi(float(mx - hx)), rep.u_of_xi(float(mx + hx))
            out.append(dict(el=[i + 1, j + 1], u=[u0, u1], v=[float(mv - hv), float(mv + hv)], fields=row))
            print('%s element (%d,%d) u [%.2f, %.2f] v [%.2f, %.2f]' % (case, i + 1, j + 1, u0, u1, float(mv - hv), float(mv + hv)))
            for F in approx.FN:
                r = row[F]
                print('    %s: A %.1e floor %.0e  rho (t, s, x) = %.2f %.2f %.2f  (fit points %s; last degree above 10 x floor %s)' %
                      (F, r['A'], r['floor'], *r['rho'], r['npts'], r['deg_at_floor']))
            if sapp:
                # S-APP's element of the same index on its equal-split layout
                k = i * len(L['v']) + j
                if k < len(sapp):
                    s = sapp[k]
                    print('    S-APP (%s, u %s, v %s): ' % (s.get('xi'), ['%.2f' % q for q in s['u']], s['v']) +
                          ' | '.join('%s %.2f %.2f %.2f' % (F, *s['fields'][F]['rho']) for F in approx.FN if F in s['fields']))
            e += 1
    if len(sys.argv) > 4: json.dump(out, open(sys.argv[4], 'w'), indent=1)

main()
