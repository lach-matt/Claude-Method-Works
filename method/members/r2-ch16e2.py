
# r2-ch16e2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch16e.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (3 anchors); nothing else changes. r2-ch16e.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 90+184 — reproduces r2-ch16e.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
"""r2-ch16e --- COMPUTABLE batch, chat 118, main L8575-L8699 (§30.4 - §31.2.5).

Every figure measured here; nothing carried from a handoff.  r2lib imported by path.
"""
import importlib.util, math, re
from fractions import Fraction as F
from decimal import Decimal, ROUND_HALF_UP

spec = importlib.util.spec_from_file_location('r2lib', '/home/claude/members/r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import load_tower, analyse, Rset, L8_at, is_tree

LO, HI = _L('### 30.4 The lists this work enumerated once'), _L("    exponential degeneracy and a limiting temperature. Λ's finiteness is what capping buys.", 1)
M = open('/home/claude/members/The_Method_1_6-2.md', encoding='utf-8').read().split('\n')


def q2(x, n=2):
    """Decimal.quantize, HALF_UP --- never round()."""
    return Decimal(repr(x)).quantize(Decimal('1.' + '0' * n), rounding=ROUND_HALF_UP)


def Vstat(f, x, h):
    """The book's pole statistic, §23.7 L6203: w = d0+d1, e = |d0-d1|/2, V = w/e."""
    a, b, c = f(x - h), f(x), f(x + h)
    d0, d1 = b - a, c - b
    w = d0 + d1
    e = abs(d0 - d1) / 2.0
    return (float('inf') if e == 0 else abs(w) / e), w, e


print('=' * 100)
print('r2-ch16e  COMPUTABLE  chat 118  main L%d-L%d  (§30.4 - §31.2.5)' % (LO, HI))
print('=' * 100)

# ------------------------------------------------------------------ 1. §30.4 closure algebra
print('\n## 1  §30.4 L8576-L8578  the closure of the four printed relations')
print('   printed set: V = 4v/3h,  lam^2 = (2/3)T,  w*V = 8 lam^2,  T = Z^2 R / v^2')
ok = []
for (Z, R, v, h) in [(1, 1, 5, 1), (3, 2, 7, 2), (2, 5, 11, 3), (7, 1, 13, 5)]:
    T = F(Z * Z * R, v * v)
    V = F(4 * v, 3 * h)
    lam2 = F(2, 3) * T
    w = 8 * lam2 / V
    ok.append((w / T == F(4 * h, v), (w / V) / T == 3 * F(h, v) ** 2))
    print('   Z=%d R=%d v=%d h=%d :  w/T = %-12s 4h/v = %-12s   e:=w/V, e/T = %-14s 3(h/v)^2 = %s'
          % (Z, R, v, h, w / T, F(4 * h, v), (w / V) / T, 3 * F(h, v) ** 2))
print('   w/T = 4(h/v)  holds on all %d instances: %s' % (len(ok), all(a for a, _ in ok)))
print('   e/T = 3(h/v)^2 holds on all %d instances: %s   [ONLY once e is READ AS w/V]' % (len(ok), all(b for _, b in ok)))
print('   MEASURED: the symbol e does NOT occur in the four printed relations.')
print('   sites of "e" as a defined symbol near the unit:',
      [i for i in range(LO, HI + 1) if re.search(r'V\s*[.\u00b7]\s*e\s*=|e\s*=\s*', M[i - 1])])
print('   L4349 prints (a) V = 4v/3 (b) w = V . e  ->  e = w/V is the book\'s own definition:')
print('        L4349: %s' % M[_L(' must pass. For Λ with p = (T, n, Z, σ) and q = (ν, δ, V, r, w, e), rank is 4 and ⅅ = 2, spanned by', 1)].strip()[:100])

# the three relations §30.4.1 says now reduce to zero
print('\n   §30.4.1 L8586 --- the three named further relations, tested under e = w/V:')
for (Z, R, v, h) in [(1, 1, 5, 1), (3, 2, 7, 2), (2, 5, 11, 3)]:
    T = F(Z * Z * R, v * v); V = F(4 * v, 3 * h); w = 8 * (F(2, 3) * T) / V; e = w / V
    print('      Z=%d v=%d h=%d :  V*e == w : %-5s   w^2 == (16/3)Te : %-5s   T*h^2 == e*v^2/3 : %s'
          % (Z, v, h, V * e == w, w * w == F(16, 3) * T * e, T * h * h == e * v * v / 3))

# ------------------------------------------------------------------ 2. Groebner
print('\n## 2  §30.4.1 L8584-L8586  "a Groebner basis of 18 where the original four gave 6"')
try:
    import sympy as sp
    V, lam, w, T, Z, R, v, h, e = sp.symbols('V lam w T Z R v h e')
    four = [3 * h * V - 4 * v, 3 * lam**2 - 2 * T, w * V - 8 * lam**2, T * v**2 - Z**2 * R]
    G = sp.groebner(four, V, lam, w, T, Z, R, v, h, order='lex')
    print('   original four, lex, 8 vars      : basis size %d' % len(G.exprs))
    G2 = sp.groebner(four, V, lam, w, T, Z, R, v, h, order='grevlex')
    print('   original four, grevlex, 8 vars  : basis size %d' % len(G2.exprs))
    G3 = sp.groebner(four + [V * e - w], V, lam, w, T, Z, R, v, h, e, order='lex')
    print('   four + (V*e = w), lex, 9 vars   : basis size %d' % len(G3.exprs))
    G9 = sp.groebner(four, V, lam, w, T, Z, R, v, h, e, order='lex')
    print('   IDEAL MEMBERSHIP, the decisive test for §30.4 L8577:')
    print('      is  V*e - w  in the ideal of the four?          %s' % (G9.reduce(V * e - w)[1] == 0))
    print('      is  e*v**2 - 3*T*h**2  in that ideal?           %s' % (G9.reduce(e * v**2 - 3 * T * h**2)[1] == 0))
    print('      is  w*v - 4*T*h  (i.e. w/T = 4h/v) in it?       %s' % (G9.reduce(w * v - 4 * T * h)[1] == 0))
    print('      -> e/T = 3(h/v)^2 is NOT a consequence of the four printed relations;')
    print('         it needs V*e = w, which §30.4.1 L8586 itself lists as one of the relations')
    print('         that reduce to zero only NOW and "did not before".')
    print('   PRINTED: 6 for the original four.  MEASURED above; convention (order, variable list)')
    print('   is NOT printed anywhere in the unit --- basis size is order-dependent.')
except Exception as ex:
    print('   sympy failure:', ex)
print('   sites of "eight polynomial relations" / the eight themselves, six volumes:')
VOL = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
       'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
       'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
       'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
       'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
VL = {k: open('/home/claude/members/' + f, encoding='utf-8').read().split('\n') for k, f in VOL.items()}
for k, L in VL.items():
    s = [i for i, t in enumerate(L, 1) if re.search(r'eight polynomial|eight relations', t, re.I)]
    if s: print('      %-4s %s' % (k, s))
print('      -> the eight are nowhere enumerated: UNPRINTED INPUT (docket 10).')

# ------------------------------------------------------------------ 3. Routh threshold
print('\n## 3  §31.1.1 L8642-L8643  L4/L5 linearly stable for mu < 0.0385209')
mu_c = (9 - math.sqrt(69)) / 18
print('   Routh critical mass ratio (9 - sqrt 69)/18 = %.10f   printed 0.0385209   match to 7 dp: %s'
      % (mu_c, q2(mu_c, 7) == Decimal('0.0385209')))
EM = 7.342e22 / (5.9722e24 + 7.342e22)
SJ = 1.89813e27 / (1.98847e30 + 1.89813e27)
print('   Earth-Moon  mu = %.7f  < mu_c : %s' % (EM, EM < mu_c))
print('   Sun-Jupiter mu = %.7f  < mu_c : %s' % (SJ, SJ < mu_c))
print('   (both mass values are UNPRINTED inputs; the qualification claim is robust to any')
print('    standard values --- EM ~ 0.0121, SJ ~ 0.00095, both far below 0.03852.)')

# ------------------------------------------------------------------ 4. collinear Lagrange points
print('\n## 4  §31.1.1 L8635-L8637  V at the collinear points, mu = 0.030, h = 0.010')


def collinear(mu, which):
    """x of L1/L2/L3 in the rotating frame, primaries at -mu and 1-mu."""
    def g(x):
        return (x - (1 - mu) * (x + mu) / abs(x + mu) ** 3
                - mu * (x - 1 + mu) / abs(x - 1 + mu) ** 3)
    if which == 1:   a, b = -mu + 1e-9, 1 - mu - 1e-9
    elif which == 2: a, b = 1 - mu + 1e-9, 2.0
    else:            a, b = -2.0, -mu - 1e-9
    fa = g(a)
    for _ in range(300):
        m = (a + b) / 2.0
        fm = g(m)
        if (fa > 0) == (fm > 0): a, fa = m, fm
        else: b = m
    return (a + b) / 2.0


for w_ in (1, 2, 3):
    Vv, wid, err = Vstat(lambda m: collinear(m, w_), 0.030, 0.010)
    print('   L%d  x(0.02)=%+.9f  x(0.03)=%+.9f  x(0.04)=%+.9f   w=%.3e  e=%.3e   V = %.1f'
          % (w_, collinear(0.02, w_), collinear(0.03, w_), collinear(0.04, w_), wid, err, Vv))
print('   PRINTED: 24.6 (L1), 12.4 (L2), 16,423 (L3).')

print('\n   monotone / convex / 3-monotone in mu, on the grid mu = 0.01 .. 0.08 step 0.01:')
grid = [0.01 * k for k in range(1, 9)]
for w_ in (1, 2, 3):
    ys = [collinear(m, w_) for m in grid]
    d1 = [b - a for a, b in zip(ys, ys[1:])]
    d2 = [b - a for a, b in zip(d1, d1[1:])]
    d3 = [b - a for a, b in zip(d2, d2[1:])]
    d4 = [b - a for a, b in zip(d3, d3[1:])]
    sg = lambda v: ''.join('+' if t > 0 else '-' if t < 0 else '0' for t in v)
    one = lambda v: ('+' if v[0] > 0 else '-') if v else '?'
    print('      L%d  d1 %-8s d2 %-8s d3 %-8s d4 %-8s  ->  order pattern %s'
          % (w_, sg(d1), sg(d2), sg(d3), sg(d4), ', '.join(one(x) for x in (d1, d2, d3, d4))))
print('   PRINTED L8646: "L1 and L3 alternate -, +, -, +;  L2 alternates +, -, +, -"')

print('\n   order-3 bracket widths (three-point Lagrange interpolation residual span, mu grid above):')
for w_ in (1, 3):
    ys = [collinear(m, w_) for m in grid]
    d3 = [ys[i + 3] - 3 * ys[i + 2] + 3 * ys[i + 1] - ys[i] for i in range(len(ys) - 3)]
    print('      L%d  |third differences| max %.3e  min %.3e' % (w_, max(map(abs, d3)), min(map(abs, d3))))
print('   PRINTED: widths 6.9e-4 (L1), 3.6e-9 (L3).  The mu-grid and the width convention are')
print('   NOT printed in the unit --- reported as UNPRINTED INPUT, with the measured span above.')

# ------------------------------------------------------------------ 5. Hill radius, Roche limit
print('\n## 5  §31.1.1 table  Hill radius (mu/3)^(1/3) V = 47.9;  Roche limit rho^(-1/3) V = 17.9')
for nm, p in (('Hill  (mu/3)^(1/3)', 1.0 / 3.0), ('Roche  rho^(-1/3)', -1.0 / 3.0)):
    Vv, _, _ = Vstat(lambda x: (x / 3.0) ** p if p > 0 else x ** p, 0.030, 0.010)
    print('   %-20s at the section\'s own grid x=0.030 h=0.010 :  V = %.2f' % (nm, Vv))
    need = 4.0 / abs(p - 1)               # §23.9.2 L6388: V ~ 4x/(h|p-1|)
    print('   %-20s power-law law V ~ 4x/(h|p-1|) = %.3f * (x/h);  V=47.9 needs x/h = %.2f;  V=17.9 needs x/h = %.2f'
          % ('', need, 47.9 / need, 17.9 / need))
print('   MEASURED: at the grid the section itself prints, the HILL row scores 17.7 --- which is')
print('   the value printed on the ROCHE row.  Neither printed V is reproducible from any grid')
print('   stated in the unit.')

# ------------------------------------------------------------------ 6. planetary semi-major axes
print('\n## 6  §31.1.1 table  planetary semi-major axes: monotone, not convex, third difference')
print('      changing sign between Jupiter and Saturn')
AU = [('Mercury', 0.387), ('Venus', 0.723), ('Earth', 1.000), ('Mars', 1.524),
      ('Jupiter', 5.203), ('Saturn', 9.537), ('Uranus', 19.191), ('Neptune', 30.069)]
ys = [a for _, a in AU]
d1 = [b - a for a, b in zip(ys, ys[1:])]
d2 = [b - a for a, b in zip(d1, d1[1:])]
d3 = [b - a for a, b in zip(d2, d2[1:])]
print('   monotone increasing: %s     convex (all d2 > 0): %s' % (all(t > 0 for t in d1), all(t > 0 for t in d2)))
print('   d2 %s' % ['%+.3f' % t for t in d2])
print('   d3 %s' % ['%+.3f' % t for t in d3])
lab = ['%s..%s' % (AU[i][0][:3], AU[i + 3][0][:3]) for i in range(len(d3))]
print('   d3 windows: %s' % [(lab[i], '+' if d3[i] > 0 else '-') for i in range(len(d3))])
ch = [i for i in range(len(d3) - 1) if (d3[i] > 0) != (d3[i + 1] > 0)]
print('   sign changes: %d, at the windows entering %s'
      % (len(ch), [AU[i + 4][0] for i in ch]))
print('   (semi-major axes are an UNPRINTED input; standard IAU values used.)')
print('\n   the row\'s own clause: "where Titius-Bode fails worst"')
tb = [0.4 + 0.3 * (0 if k == 0 else 2 ** (k - 1)) for k in range(9)]
slots = [('Mercury', tb[0], 0.387), ('Venus', tb[1], 0.723), ('Earth', tb[2], 1.000),
         ('Mars', tb[3], 1.524), ('Ceres', tb[4], 2.766), ('Jupiter', tb[5], 5.203),
         ('Saturn', tb[6], 9.537), ('Uranus', tb[7], 19.191), ('Neptune', tb[8], 30.069)]
errs = [(nm, p, a, abs(p - a) / a * 100) for nm, p, a in slots]
for nm, p, a, er in errs:
    print('      %-8s predicted %7.2f  actual %7.3f  error %6.2f %%' % (nm, p, a, er))
worst = max(errs, key=lambda t: t[3])
print('      MEASURED worst Titius-Bode error: %s at %.2f %% --- not Jupiter/Saturn (%.2f %%, %.2f %%)'
      % (worst[0], worst[3], errs[5][3], errs[6][3]))

# ------------------------------------------------------------------ 7. the nucleon index
print('\n## 7  §31.1.2 L8652-L8654  (N, L, 2j, occ) with occ <= 2j+1: join/meet closure, E(X)=0,')
print('      shell-order filling 2, 8, 20, 28, 50, 82')
cells = [(n, l, j, o) for n in range(4) for l in range(4) for j in range(1, 8, 2)
         for o in range(0, j + 2) if o <= j + 1]
S = set(cells)
jf = mf = 0
cl = list(cells)
for i in range(len(cl)):
    for k in range(i + 1, len(cl)):
        a, b = cl[i], cl[k]
        if tuple(max(x, y) for x, y in zip(a, b)) not in S: jf += 1
        if tuple(min(x, y) for x, y in zip(a, b)) not in S: mf += 1
print('   cells %d   ordered pairs tested %d   join leaks %d   meet leaks %d'
      % (len(cells), len(cl) * (len(cl) - 1) // 2, jf, mf))
Rn = Rset(S)                    # r2lib's R: the ambient box under the empirical pairwise envelope
print('   E(X) = |R(X)| - |X| = %d - %d = %d   [Rset, not the defining filter re-applied]'
      % (len(Rn), len(S), len(Rn) - len(S)))
shells = [('1s1/2', 2), ('1p3/2', 4), ('1p1/2', 2), ('1d5/2', 6), ('2s1/2', 2), ('1d3/2', 4),
          ('1f7/2', 8), ('2p3/2', 4), ('1f5/2', 6), ('2p1/2', 2), ('1g9/2', 10), ('1g7/2', 8),
          ('2d5/2', 6), ('2d3/2', 4), ('3s1/2', 2), ('1h11/2', 12)]
cum, t = [], 0
for nm, c in shells:
    t += c; cum.append((nm, t))
print('   cumulative occupancies: %s' % [t for _, t in cum])
for magic in (2, 8, 20, 28, 50, 82):
    print('      %3d present in shell-order cumulative set: %s' % (magic, magic in [t for _, t in cum]))

# ------------------------------------------------------------------ 8. three objects on the pole
print('\n## 8  §31.2.1 L8663-L8671  three objects with second difference zero, V infinite')
for nm, f in (("string m^2 = (N-1)/a'", lambda N: F(N) - 1),
              ('Regge J = a\'m^2 + a0', lambda N: F(9, 10) * N + F(1, 2)),
              ('central charge c = D', lambda N: F(26))):
    seq = [f(N) for N in range(1, 8)]
    d2 = [seq[i + 2] - 2 * seq[i + 1] + seq[i] for i in range(len(seq) - 2)]
    Vv, _, _ = Vstat(f, F(4), F(1))          # exact rationals: no floating-point noise
    print('   %-24s second differences %s   V = %s' % (nm, set(d2), Vv))
print('   L8670 "two levels determine every other, exactly": true for an affine sequence;')
print('   the third object is a CONSTANT, for which the claim is vacuous rather than false.')

# ------------------------------------------------------------------ 9. the string degeneracy
print('\n## 9  §31.2.2 L8674-L8678  log d(N) for prod (1-q^n)^(-24)')
NMAX = 40
d = [0] * (NMAX + 1); d[0] = 1
for n in range(1, NMAX + 1):
    for _ in range(24):
        for k in range(n, NMAX + 1):
            d[k] += d[k - n]
ld = [math.log(x) for x in d[1:NMAX + 1]]          # N = 1 .. NMAX
d1 = [b - a for a, b in zip(ld, ld[1:])]
d2 = [b - a for a, b in zip(d1, d1[1:])]
d3 = [b - a for a, b in zip(d2, d2[1:])]
print('   d(1..8) = %s' % d[1:9])
print('   first differences all positive (N=1..%d): %s' % (NMAX, all(t > 0 for t in d1)))
print('   second differences all negative: %s   third differences all positive: %s'
      % (all(t < 0 for t in d2), all(t > 0 for t in d3)))
print('   second difference at N = 2 : %+.4f   (printed -0.31)' % d2[0])
print('   second difference at N = 15: %+.4f   (printed -0.03)' % d2[13])
for N in (13, 14, 15):
    Vv, _, _ = Vstat(lambda x: math.log(d[int(x)]), float(N), 1.0)
    print('   V at N = %2d : %.1f   (printed ~147 at N ~ 14)' % (N, Vv))
print('   d(N) ~ exp(4 pi sqrt N):  log d(N) / (4 pi sqrt N) at N = 10, 20, 40 = %s'
      % ['%.3f' % (math.log(d[N]) / (4 * math.pi * math.sqrt(N))) for N in (10, 20, 40)])

# ------------------------------------------------------------------ 10. Lambda at every dimension
print('\n## 10  §31.2.4 L8686-L8691  Lambda closes at every dimension 2-8 with E = 0;')
print('       each Lambda_d the exact projection of Lambda_{d+1}, fibres of 1 to 4')
T8 = load_tower()
L8 = L8_at((3, 3, 1, 3, 1))
print('   |Lambda_8| = %d   coordinates = %d' % (len(L8), len(next(iter(L8)))))
prev = None
for dd in range(2, 9):
    proj = sorted({c[:dd] for c in L8})
    S = set(proj)
    R = Rset(S)
    jf = mf = 0
    pl = list(S)
    for i in range(len(pl)):
        for k in range(i + 1, len(pl)):
            a, b = pl[i], pl[k]
            if tuple(max(x, y) for x, y in zip(a, b)) not in S: jf += 1
            if tuple(min(x, y) for x, y in zip(a, b)) not in S: mf += 1
    fib = {}
    if dd < 8:
        nxt = {c[:dd + 1] for c in L8}
        for c in nxt:
            fib[c[:dd]] = fib.get(c[:dd], 0) + 1
        onto = set(fib) == S
    fv = sorted(set(fib.values())) if fib else []
    print('   d=%d  |L_d| = %-5d  |R(L_d)| = %-5d  E = %-3d  join leaks %-4d meet leaks %-4d  fibres L_%d -> L_d: %s  onto: %s'
          % (dd, len(S), len(R), len(R) - len(S), jf, mf, dd + 1, fv if fv else '--',
             onto if dd < 8 else '--'))
    prev = proj

# ------------------------------------------------------------------ 11. rank sequence and Sperner
print('\n## 11  §31.2.5 L8694-L8698  rank sequence finite and log-concave, peak 122 at rank 11;')
print('       "capped coordinates give a finite index and a Sperner bound"')
rk = {}
for c in L8:
    rk[sum(c)] = rk.get(sum(c), 0) + 1
ranks = sorted(rk)
seq = [rk[r] for r in ranks]
print('   ranks %d..%d   sizes %s   total %d' % (ranks[0], ranks[-1], seq, sum(seq)))
peak = max(seq); pr = ranks[seq.index(peak)]
print('   peak %d at rank %d   (printed: peak 122 at rank 11)' % (peak, pr))
lc = [i for i in range(1, len(seq) - 1) if seq[i] * seq[i] < seq[i - 1] * seq[i + 1]]
print('   log-concave (a_i^2 >= a_{i-1}a_{i+1}) at every interior rank: %s   failures at %s'
      % (not lc, lc))
cells = sorted(L8)
idx = {c: i for i, c in enumerate(cells)}
adj = [[] for _ in cells]
for i, a in enumerate(cells):
    for j, b in enumerate(cells):
        if i != j and all(x <= y for x, y in zip(a, b)) and a != b:
            adj[i].append(j)
mt = [-1] * len(cells)


def aug(u, seen):
    for v in adj[u]:
        if v in seen: continue
        seen.add(v)
        if mt[v] == -1 or aug(mt[v], seen):
            mt[v] = u; return True
    return False


import sys
sys.setrecursionlimit(10000)
mm = 0
for u in range(len(cells)):
    if aug(u, set()): mm += 1
print('   comparability pairs %d   maximum matching %d   min chain cover = %d - %d = %d'
      % (sum(len(a) for a in adj), mm, len(cells), mm, len(cells) - mm))
print('   Dilworth: maximum antichain = min chain cover = %d;  largest rank = %d;  Sperner holds: %s'
      % (len(cells) - mm, peak, (len(cells) - mm) == peak))
print('\n' + '=' * 100)
print('end r2-ch16e')
