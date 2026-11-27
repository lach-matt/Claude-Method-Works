"""Write a solver configuration for a case of P-APPC (def:appc-layouts), from rep.py's layout.
usage: mkcfg.py case M pxi pv ncol1 ncol2 nrow1 nrow2 Nt Ns out_prefix [threads] [quadrants] [extra key=value ...]"""
import sys, os, math
sys.path.insert(0, os.environ.get('NAPP1', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'napp1')))
import rep
from fractions import Fraction as Fr

def dec(fr):
    fr = Fr(fr); s = '-' if fr < 0 else ''; fr = abs(fr)
    ip = fr.numerator // fr.denominator; rem = fr - ip; d = ''
    for _ in range(12):
        if rem == 0: break
        rem *= 10; dg = rem.numerator // rem.denominator; d += str(dg); rem -= dg
    assert rem == 0, fr
    return s + str(ip) + ('.' + d if d else '')

def main():
    a = sys.argv[1:]
    case = a[0]; M, pxi, pv, c1, c2, r1, r2, Nt, Ns = (int(t) for t in a[1:10]); out = a[10]
    thr = a[11] if len(a) > 11 else '4'; quads = a[12] if len(a) > 12 else '1234'
    C = rep.CASES[case]; L = rep.layout(case)
    xlo = min(m - h for m, h in L['xi']); xhi = max(m + h for m, h in L['xi'])
    vlo = min(m - h for m, h in L['v']); vhi = max(m + h for m, h in L['v'])
    lam = '1' if C['seed'] == 1 else '0.3162277660168379331998893544432718533719555139325216826857504852792594438639238221344'
    lines = ['lam %s' % lam, 'amp 1', 'pxi %d' % pxi, 'pv %d' % pv, 'M %d' % M,
             'consts %s' % os.path.abspath('c_%d_%d_%d.bin' % (pxi, pv, M)),
             'domain %s %s %s %s' % (dec(xlo), dec(xhi), dec(vlo), dec(vhi)), 'cells %d %d %d %d' % (c1, c2, r1, r2)]
    for (mx, hx) in L['xi']:
        for (mv, hv) in L['v']:
            lines.append('elem %s %s %s %s %d %d' % (dec(mx - hx), dec(mx + hx), dec(mv - hv), dec(mv + hv), Nt, Ns))
    lines += ['out %s' % os.path.abspath(out), 'threads %s' % thr, 'quadrants %s' % quads]
    for kv in a[13:]:
        k, v = kv.split('='); lines.append('%s %s' % (k, v))
    open(out + '.cfg', 'w').write('\n'.join(lines) + '\n')
    if not os.path.exists('c_%d_%d_%d.bin' % (pxi, pv, M)):
        os.system('python3 %s/consts.py %d %d %d c_%d_%d_%d.bin' % (os.path.dirname(os.path.abspath(__file__)), pxi, pv, M, pxi, pv, M))
    print(open(out + '.cfg').read())

main()
