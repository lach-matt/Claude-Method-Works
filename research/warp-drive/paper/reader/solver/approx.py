"""Build the printed form of an approximant from solver coefficients, and its text description for evalres.
  quantize(C, p): z = round(C 10^p) exactly from the double-double pairs (staircase: |C| >= 10^-p / 2 kept).
  write_approx(case, blocks, fn): the approx.txt of evalres.cpp from {(i, j, f): (p, z or C)}.
  points(case, ...): sample points (xi, v, x) over the use region of each element or of the case."""
import sys, os, numpy as np, struct
from fractions import Fraction as Fr
sys.path.insert(0, os.environ.get('NAPP1', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'napp1')))
import rep
FN = ('R', 'm', 'n', 'W', 's')

def read_coef(fn):
    """list over elements of (hi, lo) arrays shaped (5, Nt+1, Ns+1, M+1)"""
    out = []
    with open(fn, 'rb') as f:
        assert f.read(6) == b'BSOLC2'
        ne, NX, NW = struct.unpack('<iii', f.read(12))
        for e in range(ne):
            nt, ns = struct.unpack('<ii', f.read(8))
            a = np.frombuffer(f.read(5 * (nt + 1) * (ns + 1) * NX * 8 * NW), dtype='<f8').reshape(5, nt + 1, ns + 1, NX, NW)
            out.append(a.copy())
    return out

def quantize(hi, lo, p):
    """exact z = round((hi + lo) 10^p) as a Python-int object array; zero where |C| < 10^-p / 2"""
    sc = 10 ** p
    z = np.zeros(hi.shape, dtype=object)
    approx = (hi + lo) * float(10.0 ** p)
    idx = np.nonzero(np.abs(approx) >= 0.49)
    for t in zip(*idx):
        v = (Fr(float(hi[t])) + Fr(float(lo[t]))) * sc
        z[t] = round(v)
    return z

def dec_string(parts, nd=70):
    """a decimal string with nd significant digits of the exact sum of the double parts"""
    v = sum(Fr(float(q)) for q in parts)
    if v == 0: return '0'
    s = '-' if v < 0 else ''; v = abs(v)
    e = len(str(v.numerator // v.denominator)) if v >= 1 else -len(str(v.denominator // max(v.numerator, 1))) + 1
    m = round(v * Fr(10) ** (nd - e))
    return '%s%de%d' % (s, m, e - nd)

def write_approx(case, blocks, fn, kappa=4):
    L = rep.layout(case)
    def d(fr): return str(Fr(fr).numerator) + '/' + str(Fr(fr).denominator)
    with open(fn, 'w') as f:
        f.write('kappa %d\n' % kappa)
        f.write('pou_xi %d %s %s\n' % (len(L['cxi']) + 1, ' '.join(dec(c) for c in L['cxi']), dec(L['dxi'])))
        f.write('pou_v %d %s %s\n' % (len(L['cv']) + 1, ' '.join(dec(c) for c in L['cv']), dec(L['dv'])))
        for i, (mx, hx) in enumerate(L['xi']):
            for j, (mv, hv) in enumerate(L['v']):
                f.write('elem %d %d %s %s %s %s\n' % (i + 1, j + 1, dec(mx - hx), dec(mx + hx), dec(mv - hv), dec(mv + hv)))
                for fi in range(5):
                    p, arr = blocks[(i, j, fi)]
                    if p >= 0:
                        nz = list(zip(*np.nonzero(arr != 0)))
                        sh = arr.shape
                        f.write('field %d %d %d %d %d %d\n' % (fi, p, sh[0] - 1, sh[1] - 1, sh[2] - 1, len(nz)))
                        for (a, b, k) in nz:
                            f.write('%d %d %d %d\n' % (a, b, k, arr[a, b, k]))
                    else:
                        parts = arr                     # (nt+1, ns+1, nx+1, NW)
                        nz = list(zip(*np.nonzero(parts[..., 0] != 0)))
                        sh = parts.shape
                        f.write('field %d -1 %d %d %d %d\n' % (fi, sh[0] - 1, sh[1] - 1, sh[2] - 1, len(nz)))
                        for (a, b, k) in nz:
                            f.write('%d %d %d %s\n' % (a, b, k, dec_string(parts[a, b, k])))

def dec(fr):
    fr = Fr(fr); s = '-' if fr < 0 else ''; fr = abs(fr)
    ip = fr.numerator // fr.denominator; rem = fr - ip; dg = ''
    for _ in range(14):
        if rem == 0: break
        rem *= 10; q = rem.numerator // rem.denominator; dg += str(q); rem -= q
    assert rem == 0, fr
    return s + str(ip) + ('.' + dg if dg else '')

def use_box(case, i, j):
    """the element's use interval U_ij in (xi, v) (def:appc-layout), as floats"""
    L = rep.layout(case)
    nx, nv = len(L['xi']), len(L['v'])
    a = L['xlo'] if i == 0 else float(L['cxi'][i - 1]) - float(L['dxi'])
    b = L['xhi'] if i == nx - 1 else float(L['cxi'][i]) + float(L['dxi'])
    c = 0.5 if j == 0 else float(L['cv'][j - 1]) - float(L['dv'])
    d = 3.5 if j == nv - 1 else float(L['cv'][j]) + float(L['dv'])
    return a, b, c, d

def points(case, n=(9, 9, 9), own=False, seed=1, extra_x=(-1.0, -0.999, 0.999, 1.0)):
    rng = np.random.default_rng(seed)
    L = rep.layout(case); out = []
    for i in range(len(L['xi'])):
        for j in range(len(L['v'])):
            a, b, c, d = use_box(case, i, j)
            for xi in np.linspace(a, b, n[0]):
                for v in np.linspace(c, d, n[1]):
                    xs = list(np.cos(np.pi * (np.arange(n[2]) + rng.random()) / n[2])) + list(extra_x)
                    for x in xs:
                        out.append('%.17g %.17g %.17g' % (xi, v, x) + (' %d %d' % (i + 1, j + 1) if own else ''))
    return out
