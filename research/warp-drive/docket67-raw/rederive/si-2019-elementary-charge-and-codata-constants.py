#!/usr/bin/env python3
"""DOCKET 67, pass S, audit 15/36: si-2019-elementary-charge-and-codata-constants.

Owner: research/warp-drive/linstab.py:321-323 (E_CHARGE_EXACT) and :624-633
(reduced_planck_ev, gmmps_mass_ev), with achievable.py:299-302 (HBAR, C_SI, G_SI).

Checks, all READ-ONLY on the tree (bytecode writing off; nothing written under
research/):
 1. The four typed constants against the NIST CODATA 2018 and 2022 tables as
    embedded in scipy 1.17.1 scipy/constants/_codata.py (md5 asserted), parsed
    here from the text, not from scipy's API.
 2. e, h, c marked '(exact)' in both tables; G = 6.674 30(15)e-11 in both.
 3. hbar typed vs h/2pi exact.
 4. Sympy: Mbar c^2/e = sqrt(hbar c/8 pi G) c^2 / e; log-derivatives.
 5. Mbar against the table's own Planck mass energy equivalent / sqrt(8 pi).
 6. The tree's own functions (imported read-only) against an independent
    re-typing; GMMPS 5.3 inversion with both alphas; convention control
    (reduced vs non-reduced); G and e counterfactuals (CODATA +-1 sigma,
    +-1e-3 envelope, pre-2019 CODATA 2014 e).
 7. The claim 'the only constant this file adds to achievable.py's'.
Exit 0 iff every check passes.
"""
import hashlib, math, os, re, sys
from fractions import Fraction as F

sys.dont_write_bytecode = True
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
CODATA = os.path.join(HERE, '..', 'src', 'codata', 'x', 'scipy', 'constants', '_codata.py')
TREE = '/home/user/Claude-Method-Works/research/warp-drive'
FAILS = []


def chk(label, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + label + (('  [' + detail + ']') if detail else ''))
    if not ok:
        FAILS.append(label)


# ---------------------------------------------------------------- 1. tables
src = open(CODATA, 'rb').read()
md5 = hashlib.md5(src).hexdigest()
chk('NIST table file is the scipy 1.17.1 copy', md5 == 'f65f9f0ee37f0d491374f1c629019d55', md5)
txt = src.decode()


def block(name):
    i = txt.index(name + ' = """\\')
    j = txt.index('"""', i + len(name) + 7)
    return txt[i:j]


def row(blk, qty):
    for line in blk.splitlines():
        if line.startswith(qty + '  '):
            parts = re.split(r'\s{2,}', line.strip())
            return parts[1], parts[2]
    raise KeyError(qty)


def num(s):
    s = s.replace(' ', '').replace('...', '')
    return F(s) if 'e' not in s else F(s.split('e')[0]) * F(10) ** int(s.split('e')[1])


T = {y: block('txt' + y) for y in ('2014', '2018', '2022')}
typed = {'e': F('1.602176634e-19'), 'hbar': F('1.054571817e-34'),
         'c': F(299792458), 'G': F('6.67430e-11')}
for y in ('2018', '2022'):
    v, u = row(T[y], 'elementary charge')
    chk('CODATA %s e = typed E_CHARGE_EXACT, (exact)' % y, num(v) == typed['e'] and u == '(exact)', v + ' ' + u)
    v, u = row(T[y], 'speed of light in vacuum')
    chk('CODATA %s c = typed C_SI, (exact)' % y, num(v) == typed['c'] and u == '(exact)', v + ' ' + u)
    v, u = row(T[y], 'Planck constant')
    chk('CODATA %s h = 6.626 070 15e-34, (exact)' % y, num(v) == F('6.62607015e-34') and u == '(exact)', v + ' ' + u)
    v, u = row(T[y], 'reduced Planck constant')
    chk('CODATA %s hbar printed 1.054 571 817... (exact, display truncated)' % y,
        num(v) == typed['hbar'] and u == '(exact)' and '...' in v, v + ' ' + u)
    v, u = row(T[y], 'Newtonian constant of gravitation')
    chk('CODATA %s G = typed G_SI = 6.674 30(15)e-11' % y,
        num(v) == typed['G'] and num(u) == F('0.00015e-11'), v + ' +- ' + u)
v14, u14 = row(T['2014'], 'elementary charge')
e14 = num(v14)
chk('CODATA 2014 (pre-SI-2019) e was MEASURED, not exact', u14 != '(exact)', v14 + ' +- ' + u14)

# ---------------------------------------------------------------- 3. hbar
hbar_exact = sp.Rational(662607015, 10 ** 42) / (2 * sp.pi)
d_hbar = float((sp.Rational(1054571817, 10 ** 43) - hbar_exact) / hbar_exact)
chk('typed hbar = h/2pi truncated at 10 s.f.', abs(d_hbar) < 1e-9, 'rel %.3e' % d_hbar)

# ---------------------------------------------------------------- 4. sympy
hb, c, G, e = sp.symbols('hbar c G e', positive=True)
Mbar = sp.sqrt(hb * c / (8 * sp.pi * G)) * c ** 2 / e
dl = {s: sp.simplify(sp.diff(sp.log(Mbar), s) * s) for s in (hb, c, G, e)}
chk('d ln Mbar/d ln (hbar, c, G, e) = (1/2, 5/2, -1/2, -1)',
    [dl[hb], dl[c], dl[G], dl[e]] == [sp.Rational(1, 2), sp.Rational(5, 2), -sp.Rational(1, 2), -1], str(dl))
Mnr = sp.sqrt(hb * c / G) * c ** 2 / e
chk('non-reduced / reduced = sqrt(8 pi) exactly', sp.simplify(Mnr / Mbar - sp.sqrt(8 * sp.pi)) == 0)


def mbar_ev(hbar=float(typed['hbar']), cc=299792458.0, GG=6.67430e-11, ee=1.602176634e-19):
    return math.sqrt(hbar * cc / (8 * math.pi * GG)) * cc ** 2 / ee


M0 = mbar_ev()
M_exact_hbar = mbar_ev(hbar=float(hbar_exact))
print('   Mbar (typed constants)     = %.9e eV' % M0)
print('   Mbar (exact hbar = h/2pi)  = %.9e eV  rel %.2e' % (M_exact_hbar, M_exact_hbar / M0 - 1))
chk('Mbar = 2.435323e27 eV (the tree elsewhere pins 2.435323e18 GeV, higgs.py:610)',
    abs(M0 / 2.435323e27 - 1) < 5e-7, '%.9e' % M0)

# ---------------------------------------------------------------- 5. table's Planck mass
for y in ('2018', '2022'):
    v, u = row(T[y], 'Planck mass energy equivalent in GeV')
    mpl = float(num(v)) * 1e9
    ump = float(num(u)) * 1e9
    ratio = (mpl / math.sqrt(8 * math.pi)) / M0 - 1
    chk('CODATA %s m_P c^2 / sqrt(8 pi) agrees with Mbar within its own u' % y,
        abs(ratio) < ump / mpl, 'rel %.2e vs u_r %.2e' % (ratio, ump / mpl))

# ---------------------------------------------------------------- 6. tree functions, read-only
sys.path.insert(0, TREE)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
try:
    import achievable, linstab
    tree_ok = True
except Exception as exc:  # recorded, not hidden
    tree_ok = False
    print('   tree import failed: %r' % exc)
chk('tree modules import read-only', tree_ok)
if tree_ok:
    chk('achievable HBAR, C_SI, G_SI and linstab E_CHARGE_EXACT equal the typed values',
        (F(repr(achievable.HBAR)), F(repr(achievable.C_SI)), F(repr(achievable.G_SI)),
         F(repr(linstab.E_CHARGE_EXACT))) == (typed['hbar'], typed['c'], typed['G'], typed['e']))
    chk('linstab.reduced_planck_ev() = independent re-typing (bit-level)',
        linstab.reduced_planck_ev() == M0, '%r' % linstab.reduced_planck_ev())

LAM, OM, PRINTED = 7.15e-121, 0.685, 7.8e-3


def m_gmmps(alpha, M=M0):
    return (LAM / (6 * OM * alpha)) ** 0.25 * M


a_thm, a_typo = 1 / (64 * math.pi ** 2), 1 / (64 * math.pi)
m1, m2 = m_gmmps(a_thm), m_gmmps(a_typo)
print('   m(1/64pi^2) = %.5e eV  (%+.2f %% vs printed)' % (m1, 100 * (m1 / PRINTED - 1)))
print('   m((64pi)^-1)= %.5e eV  (%+.2f %% vs printed)' % (m2, 100 * (m2 / PRINTED - 1)))
if tree_ok:
    tm1, _ = linstab.gmmps_mass_ev(a_thm)
    tm2, _ = linstab.gmmps_mass_ev(a_typo)
    chk('tree gmmps_mass_ev reproduces the independent inversion', abs(tm1 / m1 - 1) < 1e-14 and abs(tm2 / m2 - 1) < 1e-14)
chk('selftest 2%% window holds at the typed constants', abs(m1 / PRINTED - 1) < 0.02)
chk('selftest >20%% typo verdict holds at the typed constants', abs(m2 / PRINTED - 1) > 0.2)
m_nr = m_gmmps(a_thm, M0 * math.sqrt(8 * math.pi))
print('   convention control: non-reduced Planck mass gives m = %.4e eV (%+.0f %%)' % (m_nr, 100 * (m_nr / PRINTED - 1)))
chk('reduced convention is load-bearing (non-reduced misses by > 100%)', m_nr / PRINTED - 1 > 1.0)
m_nr_typo = m_gmmps(a_typo, M0 * math.sqrt(8 * math.pi))
chk('no (convention, alpha) cross-combination rescues (64 pi)^-1 into the 2% window',
    abs(m_nr_typo / PRINTED - 1) > 0.02, 'nonreduced+typo %.4e' % m_nr_typo)

# counterfactuals on the data
uG = 0.00015e-11
worst = 0.0
for GG, lab in ((6.67430e-11 + uG, '+1 sigma'), (6.67430e-11 - uG, '-1 sigma'),
                (6.67430e-11 * 1.001, '+1e-3'), (6.67430e-11 * 0.999, '-1e-3')):
    M = mbar_ev(GG=GG)
    a, b = m_gmmps(a_thm, M), m_gmmps(a_typo, M)
    worst = max(worst, abs(a / m1 - 1))
    chk('G at %s: both verdicts unchanged (m moves %.2e rel)' % (lab, a / m1 - 1),
        abs(a / PRINTED - 1) < 0.02 and abs(b / PRINTED - 1) > 0.2)
Me14 = mbar_ev(ee=float(e14))
# threshold first set at 2e-9 by estimate and FAILED at 8.24e-9 -- the estimate
# was wrong, not the data; re-set to 1e-8 and the 2014 u_r printed beside it.
u14r = float(num(u14) / e14)
chk('pre-2019 e (CODATA 2014, measured) moves Mbar by < 1e-8 (~1.35 x its own 2014 u_r)',
    abs(Me14 / M0 - 1) < 1e-8, 'rel %.2e, 2014 u_r %.2e' % (Me14 / M0 - 1, u14r))
# G enters m in eV through Mbar only (Lambda is a fixed printed number in M_P^2 units)
x = sp.symbols('x', positive=True)
chk('tree path: d ln m/d ln G = -1/2 (printed Lambda held in M_P^2 units)',
    sp.simplify(sp.diff(sp.log((sp.Symbol('L') / (6 * sp.Symbol('O') * sp.Symbol('a'))) ** sp.Rational(1, 4) * Mbar), G) * G)
    == -sp.Rational(1, 2))
chk('physical path: d ln m/d ln G = -1/4 (Lambda held in eV^2, Lambda/Mbar^2 re-formed)',
    sp.simplify(sp.diff(sp.log((x / Mbar ** 2) ** sp.Rational(1, 4) * Mbar), G) * G) == -sp.Rational(1, 4))
# margins: how far would G have to move to flip either verdict along the tree path?
# m ~ G^(-1/2): lower edge 0.98*7.8e-3 and upper edge 1.02*7.8e-3
g_hi = (m1 / (0.98 * PRINTED)) ** 2 - 1
g_lo = (m1 / (1.02 * PRINTED)) ** 2 - 1
print('   G would have to move by %+.3f or %+.3f (relative) to leave the 2%% window' % (g_hi, g_lo))
chk('window flip needs |dG/G| > 1e-2, i.e. > 450 CODATA sigma', min(abs(g_hi), abs(g_lo)) > 1e-2)

# ---------------------------------------------------------------- 7. 'only constant this file adds'
lines = open(os.path.join(TREE, 'linstab.py')).read().splitlines()
phys = [i + 1 for i, L in enumerate(lines)
        if re.match(r'^[A-Z_][A-Z0-9_]*\s*=\s*[0-9.]+e[-+]?\d+', L) and not L.startswith('GMMPS')]
print('   top-level float-with-exponent assignments outside GMMPS_* READ figures: %s' % phys)
chk("'the only constant this file adds' -- only line 323 carries an SI constant", phys == [323])

print('\n%d FAIL' % len(FAILS))
sys.exit(1 if FAILS else 0)
