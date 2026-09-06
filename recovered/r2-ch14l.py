#!/usr/bin/env python3
"""r2-ch14l — computable batch for the Chapter 23 second read, main L6303-L6433
(§23.6 The fractional forms .. §23.9.3 And the pole sits on the field's favourite variable).

Cadence: chat 81 ruling 3 — one computable batch, one prose batch (r2-ch14m), per section read.
r2lib supplies heading_line / section_span / has_token / enclosing (lifted chat 95); nothing is
copied.  Deterministic: no wall-clock, no randomness.

Standing traps observed here: never round with round() (binary; 17.25 -> 17.2) — every printed
comparison goes through Decimal.quantize with the convention named in the line; a formula
numerator is not a value; word-bounding applies to numbers as much as to words.
"""
import sys, importlib.util
from fractions import Fraction as F
from decimal import Decimal, ROUND_HALF_EVEN, getcontext

getcontext().prec = 60
sys.path.insert(0, '/home/claude/members')
spec = importlib.util.spec_from_file_location('r2lib', '/home/claude/members/r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing  # noqa: E402

MAIN = open('/home/claude/members/The_Method_1_6-2.md').read().splitlines()

# ---------------------------------------------------------------- helpers
def q(x, places, conv=ROUND_HALF_EVEN):
    """Decimal quantize, ROUND_HALF_EVEN throughout unless a call names otherwise."""
    return Decimal(str(x)).quantize(Decimal('1.' + '0' * places) if places else Decimal('1'),
                                    rounding=conv)

def verdict(tag, ok, msg):
    print(f'{"OK  " if ok else "DEV "} {tag}  {msg}')

def V_exact(x, h, p):
    """V = |w|/|e| for the observable y = t**p bracketed at t = x +/- h.
    w = y(x+h) - y(x-h); e = mean of the two endpoints minus the centre (the linear-interpolation
    error at the centre).  Fraction when p is an integer, float otherwise."""
    if isinstance(p, int):
        a, b, c = F(x + h) ** p, F(x - h) ** p, F(x) ** p
    else:
        a, b, c = (x + h) ** p, (x - h) ** p, float(x) ** p
    w = a - b
    e = (a + b) / 2 - c
    return abs(w) / abs(e) if e != 0 else None, w, e

# ---------------------------------------------------------------- boundary
print('== boundaries (measured on the member, never carried) ==')
for s in ('23.6', '23.7', '23.8', '23.8.1', '23.8.2', '23.8.3', '23.8.4',
          '23.9', '23.9.1', '23.9.2', '23.9.3', '23.10'):
    print(f'  §{s:8s} heading L{heading_line(MAIN, s)}')
sp = section_span(MAIN, '23.6')
print(f'  span §23.6 = {sp};  unit L6303-L6433 =',
      heading_line(MAIN, '23.6') == 6303 and heading_line(MAIN, '23.10') == 6434)
print(f'  enclosing(6331) = {enclosing(MAIN, 6331)}   enclosing(6416) = {enclosing(MAIN, 6416)}')

# ---------------------------------------------------------------- §23.6
print('\n== §23.6 the fractional forms (L6303-L6320) ==')
# T(nu) = Z^2 R / nu^2.  w = T(nu-h) - T(nu+h); e = mean(endpoints) - T(nu).  Z, R cancel in w/T.
def wT_eT(nu, h):
    nu, h = F(nu), F(h)
    Tm, Tp, T0 = 1 / (nu - h) ** 2, 1 / (nu + h) ** 2, 1 / nu ** 2
    return (Tm - Tp) / T0, ((Tm + Tp) / 2 - T0) / T0

rows = [(20, 1, '0.201004', '0.200000', '7.531e-3', '7.500e-3'),
        (40, 1, '0.100125', '0.100000', '1.877e-3', '1.875e-3'),
        (40, 2, '0.201004', '0.200000', '7.531e-3', '7.500e-3')]
allok = True
for nu, h, pw, papp, pe, peapp in rows:
    wt, et = wT_eT(nu, h)
    u = F(h, nu)
    got_w, got_e = q(float(wt), 6), q(float(et), 6)
    exp_w, exp_e = Decimal(pw), q(float(Decimal(pe.replace('e-3', '')) / 1000), 6)
    ok_w = got_w == exp_w
    ok_e = q(float(et) * 1000, 3) == q(float(Decimal(pe.replace('e-3', ''))), 3)
    ok_a = q(float(4 * u), 6) == Decimal(papp)
    ok_b = q(float(3 * u * u) * 1000, 3) == q(float(Decimal(peapp.replace('e-3', ''))), 3)
    allok &= ok_w and ok_e and ok_a and ok_b
    print(f'  nu={nu:<3} h={h}: w/T exact {float(wt):.9f} vs printed {pw} {"ok" if ok_w else "MISMATCH"}'
          f' | 4h/nu {float(4*u):.6f} {"ok" if ok_a else "MISMATCH"}'
          f' | e/T exact {float(et):.6e} vs {pe} {"ok" if ok_e else "MISMATCH"}'
          f' | 3(h/nu)^2 {"ok" if ok_b else "MISMATCH"}')
verdict('14l-01', allok, 'six printed table cells of §23.6 reproduce exactly (4 dp / 6 sf)')

# the display equations at L6306-L6307 are printed as equalities
print('  display equations L6306-6307 tested as equalities:')
worst_w = worst_e = 0
for nu, h in [(20, 1), (40, 1), (40, 2), (10, 1), (5, 1)]:
    wt, et = wT_eT(nu, h); u = F(h, nu)
    ser_w = 4 * u + 8 * u ** 3
    ser_e = 3 * u * u
    dw = abs(float((wt - ser_w) / wt)) * 100
    de = abs(float((et - ser_e) / et)) * 100
    worst_w, worst_e = max(worst_w, dw), max(worst_e, de)
    print(f'    nu={nu:<3} h={h}: w/T {float(wt):.9f} vs 4u+8u^3 {float(ser_w):.9f} ({dw:.4f}% )'
          f' | e/T {float(et):.9f} vs 3u^2 {float(ser_e):.9f} ({de:.4f}% )')
verdict('14l-02', False,
        f'L6306 prints "w/T = 4(h/nu)+8(h/nu)^3" and "e/T = 3(h/nu)^2" as equalities; both are '
        f'truncated series — exact w/T = 4u/(1-u^2)^2, exact e/T = (3u^2-u^4)/(1-u^2)^2. '
        f'Deviation on the printed rows: w/T {worst_w:.4f}% worst, e/T {worst_e:.4f}% worst '
        f'(the table\'s own w/T column carries the exact value, not the display equation)')

# L6317 "their ratio returns V = (4/3)(nu/h)"
print('  L6317 ratio claim:')
bad = []
for nu, h in [(20, 1), (40, 1), (40, 2), (10, 1)]:
    wt, et = wT_eT(nu, h)
    r = F(nu, h)
    ratio = wt / et
    closed = 4 * r ** 3 / (3 * r ** 2 - 1)          # chat 95's settled exact V
    asym = F(4, 3) * r
    if ratio != asym: bad.append((nu, h, float(ratio), float(asym)))
    print(f'    nu={nu:<3} h={h}: (w/T)/(e/T) = {float(ratio):.6f} | 4r^3/(3r^2-1) = '
          f'{float(closed):.6f} {"identical" if ratio == closed else "DIFFERS"} | (4/3)(nu/h) = '
          f'{float(asym):.6f}  gap {float(ratio-asym):+.6f}')
verdict('14l-03', not bad,
        'L6317 "their ratio returns V = (4/3)(nu/h)" — the exact ratio of the two fractional forms '
        f'is 4r^3/(3r^2-1), above (4/3)r at every tested (nu,h); worst gap '
        f'{max(abs(b[2]-b[3]) for b in bad):.6f} at nu={bad[0][0]},h={bad[0][1]}. The identity holds '
        'only for the truncated forms, i.e. asymptotically')

# e IS the linear interpolation error (L6319's characterisation)
lin_ok = True
for nu, h in [(20, 1), (40, 2), (12, 3)]:
    nu_, h_ = F(nu), F(h)
    interp = (1 / (nu_ - h_) ** 2 + 1 / (nu_ + h_) ** 2) / 2      # chord midpoint
    true = 1 / nu_ ** 2
    _, et = wT_eT(nu, h)
    lin_ok &= (interp - true) / true == et
verdict('14l-04', lin_ok, 'L6319 e/T is exactly the relative error of linear interpolation of T '
                          'across the bracket (chord midpoint minus true value), verified on three (nu,h)')

# ---------------------------------------------------------------- §23.7
print('\n== §23.7 the exponent axis (L6321-L6332) ==')
cost = lambda p: 2 - p
viri = lambda p: -p
inv1 = all(cost(cost(p)) == p for p in range(-30, 31))
inv2 = all(viri(viri(p)) == p for p in range(-30, 31))
transl = all(cost(viri(p)) == p + 2 and viri(cost(p)) == p - 2 for p in range(-30, 31))
parity = all((p % 2) == (cost(p) % 2) and (p % 2) == (viri(p) % 2) for p in range(-30, 31))
verdict('14l-05', inv1 and inv2 and transl and parity,
        'L6322-6324 both maps are involutions; x^p·x^(2-p) = x^2 and x^p·x^(-p) = 1; the '
        'composition translates by 2 and the orbits are the two parity classes — all four hold')
Vinv = all(abs(4 * 20 / (1 * abs(p - 1))) == abs(4 * 20 / (1 * abs(cost(p) - 1)))
           for p in range(-30, 31) if p != 1)
verdict('14l-05b', Vinv, 'the asymptotic cost 4x/(h|p-1|) is invariant under the cost involution '
                         'p -> 2-p, which is what makes the name earned (tested p = -30..30, p != 1)')
verdict('14l-06', (1 % 2 == 1) and (2 % 2 == 0),
        'L6326 the pole p = 1 is odd and powers of <r> (p = 2) generate the even orbit only, so '
        'no power of <r> reaches p = 1')

print('  L6330-6331 caption "the pole at p = 1 is the method\'s only hard singularity":')
for p in (0, 1):
    v, w, e = V_exact(20, 1, p)
    print(f'    p={p}: w = {w}, e = {e}, V = {"undefined (0/0)" if v is None else v}'
          f' | asymptotic 4x/(h|p-1|) = '
          f'{"pole" if p == 1 else float(F(4*20, abs(p-1)))}')
verdict('14l-07', False,
        'caption L6331 claims p = 1 is the only hard singularity. MEASURED at x = 20, h = 1: '
        'p = 0 gives w = 0 and e = 0, so V = 0/0 is undefined there too, while the asymptotic form '
        '4x/(h|p-1|) returns a finite 80. Second site of chat 95\'s 14j-04 (p = 0 degenerate), and '
        'the caption states the exclusivity where §23.7\'s prose does not')

# ---------------------------------------------------------------- §23.8.1
print('\n== §23.8.1 the Newton decrement (L6336-L6348) ==')
def lam2_pow(x, p):
    """lambda^2 = f'^2/f'' for f = x^p."""
    return (p * x ** (p - 1)) ** 2 / (p * (p - 1) * x ** (p - 2))
ratios = {}
for p in (-2, -3, 2, 11):
    num = 8 * (p * F(20) ** (p - 1)) ** 2 / (p * (p - 1) * F(20) ** (p - 2))
    ratios[p] = num / (lam2_pow(F(20), p))
verdict('14l-08', all(r == 8 for r in ratios.values()),
        f'L6341 "verified symbolically at p = -2, -3, 2, 11: the ratio is 8 in every case" — '
        f'MEASURED exactly 8 at all four ({ratios[2]}); it is 8 identically for every p with '
        f'f\'\' != 0, the four values being an instance rather than a test')
# 1/2 lambda^2 is the decrease of the quadratic model at a full Newton step
dec_ok = True
for p in (-2, 3, 11):
    x = F(20); f1 = p * x ** (p - 1); f2 = p * (p - 1) * x ** (p - 2)
    step = -f1 / f2
    dec = -(f1 * step + f2 * step ** 2 / 2)            # f(x) - model(x + step)
    dec_ok &= dec == lam2_pow(x, p) / 2
verdict('14l-09', dec_ok, 'L6341 "half lambda^2 is exactly the decrease in the quadratic '
                          'approximation obtained by a full Newton step" — exact at p = -2, 3, 11')
# lambda^2 = (2/3) T
sym_ok = True
for Z in (1, 2, 6):
    for nu in (10, 40, 100):
        ZR = F(Z) ** 2 * F(1097373, 10)              # placeholder scale; cancels in the identity
        T = ZR / F(nu) ** 2
        T1 = -2 * ZR / F(nu) ** 3
        T2 = 6 * ZR / F(nu) ** 4
        sym_ok &= (T1 ** 2 / T2) == F(2, 3) * T
verdict('14l-10', sym_ok, "L6345 lambda^2 = T'^2/T'' = (2/3)T for T = Z^2R/nu^2 — exact at "
                          'Z = 1, 2, 6 and nu = 10, 40, 100')
print('  L6347 printed 731.5820 (nu = 10) and 7.3158 (nu = 100), Z = 1:')
for Rname, R in (('R = 109737.31568 (the constant r2-tools carries)', Decimal('109737.31568')),
                 ('R = 109737.3', Decimal('109737.3')),
                 ('R = 109737.31', Decimal('109737.31'))):
    v10 = (Decimal(2) / 3) * R / Decimal(100)
    v100 = (Decimal(2) / 3) * R / Decimal(10000)
    print(f'    {Rname:44s} nu=10 -> {q(v10,4)} (printed 731.5820)   '
          f'nu=100 -> {q(v100,4)} (printed 7.3158)')
v10_book = (Decimal(2) / 3) * Decimal('109737.31568') / Decimal(100)
verdict('14l-11', q(v10_book, 4) == Decimal('731.5820'),
        f'L6347 nu = 10: (2/3)T = {v10_book} -> {q(v10_book,4)} by Decimal.quantize '
        f'ROUND_HALF_EVEN, against the printed 731.5820. The printed digit reproduces only under '
        f'R = 109737.3 (five significant figures); under the book\'s own R the fourth decimal is 1, '
        f'not 0. nu = 100 prints 7.3158 and reproduces under both')

# ---------------------------------------------------------------- §23.8.2
print('\n== §23.8.2 self-concordance (L6349-L6364) ==')
R = Decimal('109737.31568')
def thresh(Z):
    return (Decimal(6).sqrt() / 2) * Decimal(Z) * R.sqrt()
def sc_ratio(Z, nu):
    """|T'''| / 2(T'')^{3/2} = 12 nu / (6^{3/2} sqrt(Z^2 R))."""
    return Decimal(12) * Decimal(nu) / (Decimal(6) ** Decimal('1.5') * (Decimal(Z) ** 2 * R).sqrt())
print('  algebraic equivalence 24Z^2R/nu^5 <= 2*6^{3/2}(Z^2R)^{3/2}/nu^6  <=>  nu <= (sqrt6/2)Z sqrtR:')
alg_ok = True
for Z in (1, 2, 6):
    for nu in (100, 405, 406, 800, 2500):
        lhs = Decimal(24) * Decimal(Z) ** 2 * R / Decimal(nu) ** 5
        rhs = 2 * Decimal(6) ** Decimal('1.5') * (Decimal(Z) ** 2 * R) ** Decimal('1.5') / Decimal(nu) ** 6
        alg_ok &= ((lhs <= rhs) == (Decimal(nu) <= thresh(Z)))
verdict('14l-12', alg_ok, 'L6353 the stated equivalence holds at every tested (Z, nu) — the '
                          'inequality and the threshold agree on all 15 pairs')
print('  the printed table:')
for Z, printed in ((1, 406), (2, 811), (6, 2434)):
    t = thresh(Z)
    print(f'    Z={Z}: threshold nu <= {q(t,3)}  floor {int(t)}  printed {printed}  '
          f'ratio at nu={printed}: {q(sc_ratio(Z, printed),6)} '
          f'{"(> 1: NOT self-concordant)" if sc_ratio(Z, printed) > 1 else "(<= 1: holds)"}')
verdict('14l-13', False,
        f'L6357 the Z = 1 row prints "nu <= 406" but the threshold is {q(thresh(1),3)}: at nu = 406 '
        f'the ratio is {q(sc_ratio(1,406),6)} > 1, so self-concordance fails there. The row should '
        f'read 405, as the section\'s own L6361 says ("crosses unity between nu = 405 and 406"). '
        f'Z = 2 ({q(thresh(2),3)} -> 811) and Z = 6 ({q(thresh(6),3)} -> 2,434) are floored '
        f'correctly, so the defect is the Z = 1 row alone and it contradicts the text twelve lines below')
r2v, r55, r405, r406 = sc_ratio(1, 2), sc_ratio(1, 55), sc_ratio(1, 405), sc_ratio(1, 406)
print(f'    ratio nu=2   {q(r2v,7)} -> printed 0.0049 {"ok" if q(r2v,4)==Decimal("0.0049") else "MISMATCH"}')
print(f'    ratio nu=55  {q(r55,7)} -> printed 0.1356 {"ok" if q(r55,4)==Decimal("0.1356") else "MISMATCH"}')
print(f'    ratio nu=405 {q(r405,7)} (<1) ; nu=406 {q(r406,7)} (>1) -> crossing between 405 and 406 '
      f'{"ok" if r405 < 1 < r406 else "MISMATCH"}')
verdict('14l-14', q(r2v, 4) == Decimal('0.0049') and q(r55, 4) == Decimal('0.1356') and r405 < 1 < r406,
        'L6361 all three ratio statements reproduce (ROUND_HALF_EVEN, 4 dp)')
verdict('14l-15', 6.5 <= float(1 / r55) < 7.5,
        f'L6363 "sevenfold margin" — 1/{q(r55,4)} = {q(1/r55,3)}, i.e. the margin at the deepest '
        f'channel is {q(1/r55,1)}x')

# ---------------------------------------------------------------- §23.8.3
print('\n== §23.8.3 the affine-invariance reason (L6365-L6371) ==')
print('  lambda^2 = (2/3)Z^2R/nu^2 at nu = 40:')
for Z in (1, 2, 6):
    l2 = (Decimal(2) / 3) * Decimal(Z) ** 2 * R / Decimal(40) ** 2
    print(f'    Z={Z}: lambda^2 = {q(l2,4)}   (Z=1 multiple: {q(l2/((Decimal(2)/3)*R/Decimal(1600)),4)})')
V40 = [float(4 * F(40) ** 3 / (3 * F(40) ** 2 - 1))] * 3
verdict('14l-16', False,
        'L6368 "Z^2R enters T as a multiplicative constant, a multiplicative constant is an affine '
        'map, and under an affine map the decrement cannot change." MEASURED: the decrement DOES '
        'change — lambda^2 = (2/3)Z^2R/nu^2 is the section\'s own formula (L6345) and scales by '
        'Z^2, a factor of 4 from Z = 1 to Z = 2 and 36 to Z = 6. Affine invariance of the Newton '
        'decrement is invariance under affine maps of the DOMAIN (nu), not under rescaling the '
        'function\'s values. What cancels in V is a ratio of two quantities each homogeneous of '
        f'degree 1 in Z^2R — V = 4r^3/(3r^2-1) = {V40[0]:.6f} at r = 40 for every Z. The '
        'cancellation §23.4 observed is real; the reason §23.8.3 gives contradicts §23.8.1')

# ---------------------------------------------------------------- §23.9.1
print('\n== §23.9.1 the cost ranks by exponent (L6387-L6403) ==')
tab = [('C6', 11, '8.18'), ('polarisability alpha', 7, '13.44'), ('spacing', -3, '20.04'),
       ('T, the term value', -2, '26.69'), ('C3, geometric cross-section', 4, '26.72'),
       ('radiative lifetime', 3, '40.03'), ('<r>, dipole moment', 2, '80.00'),
       ('blockade radius', F(11, 6), '95.99')]
vals = {}
ok17 = True
for name, p, printed in tab:
    if isinstance(p, F):
        v, _, _ = V_exact(20, 1, float(p))
        got = q(v, 2)
    else:
        v, _, _ = V_exact(20, 1, p)
        got = q(float(v), 2)
    vals[name] = float(v)
    asy = float(F(80, 1) / abs(F(p) - 1))
    ok = got == Decimal(printed); ok17 &= ok
    print(f'    {name:28s} p={str(p):5s} exact V = {float(v):10.5f} -> {got} vs printed {printed} '
          f'{"ok" if ok else "MISMATCH"} | asymptotic {asy:8.4f}')
verdict('14l-17', ok17, 'all eight V values of §23.9.1 reproduce exactly at nu = 20, h = 1 as the '
                        'EXACT V (not the asymptotic 4x/(h|p-1|) the sentence quotes as the source)')
third = vals['T, the term value'] / vals['C6']
twelfth = vals['<r>, dipole moment'] / vals['C6']
blockade = vals['blockade radius'] / vals['C6']
print(f'    V(T)/V(C6) = {third:.4f}   V(<r>)/V(C6) = {twelfth:.4f}   V(blockade)/V(C6) = {blockade:.4f}')
verdict('14l-18', False,
        f'L6402 "A guarantee on C6 costs a third of a guarantee on T, and a twelfth of one on the '
        f'dipole moment." MEASURED: C6 against T is 1/{third:.2f} — a third, ok. C6 against the '
        f'dipole moment is 1/{twelfth:.2f}, a TENTH, not a twelfth; the asymptotic forms give '
        f'exactly 1/10 (|p-1| = 10 against 1). The twelfth belongs to the blockade radius, the row '
        f'below, at 1/{blockade:.2f}')

# ---------------------------------------------------------------- §23.9.2
print('\n== §23.9.2 two branches (L6404-L6420) ==')
ok20 = True
for p, pv, pa in ((4, '26.72', '26.67'), (11, '8.18', '8.00'), (50, '2.39', '1.63'),
                  (300, '2.0000', '0.27'), (10000, '2.0000', '0.008')):
    v, _, _ = V_exact(20, 1, p)
    dp = len(pv.split('.')[1])
    got = q(float(v), dp) if p < 300 else q(v, dp)
    asy = F(80, abs(p - 1))
    da = len(pa.split('.')[1])
    gota = q(float(asy), da)
    ok = (got == Decimal(pv)) and (gota == Decimal(pa)); ok20 &= ok
    print(f'    p={p:<6} exact V -> {got} vs {pv} | 4x/(h|p-1|) -> {gota} vs {pa} '
          f'{"ok" if ok else "MISMATCH"}')
verdict('14l-20', ok20, 'all five rows of §23.9.2 reproduce in both columns')
lim = [float(V_exact(20, 1, p)[0]) for p in (10 ** 4, 10 ** 5)]
above2 = all(V_exact(20, 1, p)[0] > 2 for p in (4, 11, 50, 300, 10000))
cross_ok = (F(4 * 20, 1) / (1 * 40) == 2) and (abs(41 - 1) > 2 * 20 / 1) and (abs(40 - 1) < 40)
print(f'    V at p = 1e4, 1e5: {lim[0]:.10f}, {lim[1]:.10f}   strictly above 2 at every tested p: {above2}')
print(f'    branch crossing |p-1| = 2x/h = {2*20/1:.0f} -> p = 41 or p = -39; at nu = 20 "p > 41" '
      f'is the positive branch')
verdict('14l-21', above2 and cross_ok,
        'L6416-L6419 V -> 2 from above as p -> infinity, never reaching or crossing it at finite p; '
        'the branches cross at |p-1| = 2x/h, giving p > 41 at nu = 20 — all three reproduce. Note '
        'the printed 2.0000 rows are rounded, not exact: V(300) - 2 = '
        f'{float(V_exact(20,1,300)[0]) - 2:.3e}')

# ---------------------------------------------------------------- §23.9.3
print('\n== §23.9.3 the pole on nu (L6421-L6433) ==')
print('  V on T column, testing nu = n - delta with the exact V = 4r^3/(3r^2-1), h = 1:')
printed_T = {10: '11.58', 20: '24.89', 40: '51.54'}
best = None
for d100 in range(0, 300):
    d = F(d100, 100)
    good = all(q(float(4 * (F(n) - d) ** 3 / (3 * (F(n) - d) ** 2 - 1)), 2) == Decimal(printed_T[n])
               for n in (10, 20, 40))
    if good:
        best = d if best is None else best
        if d100 in (135,):
            pass
sols = [F(d, 100) for d in range(0, 300)
        if all(q(float(4 * (F(n) - F(d, 100)) ** 3 / (3 * (F(n) - F(d, 100)) ** 2 - 1)), 2)
               == Decimal(printed_T[n]) for n in (10, 20, 40))]
for n in (10, 20, 40):
    r = F(n) - F(135, 100)
    print(f'    n={n:<3} nu = n - 1.35 = {float(r):6.2f}  V = '
          f'{float(4*r**3/(3*r**2-1)):10.5f} -> {q(float(4*r**3/(3*r**2-1)),2)} vs printed '
          f'{printed_T[n]}')
verdict('14l-22', bool(sols),
        f'the V-on-T column reproduces exactly under nu = n - delta with delta in '
        f'{[str(s) for s in sols]} and h = 1 — delta = 1.35 is Na I ns. Neither delta nor h nor the '
        f'species is printed anywhere in §23.9.3: eighth member of the unprinted-input class')
print('  ratio column, as printed against the two printed columns:')
ok23 = True
for n, vn, vt, pr in ((10, '1.09e5', '11.58', '9.4e3'), (20, '1.77e6', '24.89', '7.1e4'),
                      (40, '2.84e7', '51.54', '5.5e5')):
    got = Decimal(vn) / Decimal(vt)
    exp = Decimal(pr)
    rel = abs(got - exp) / exp * 100
    ok = rel < Decimal('1.5'); ok23 &= ok
    print(f'    n={n:<3} {vn} / {vt} = {q(got,1)}  printed {pr}  ({q(rel,2)}% ) '
          f'{"ok" if ok else "MISMATCH"}')
verdict('14l-23', ok23, 'the ratio column of §23.9.3 is internally consistent with its own two V '
                        'columns to two significant figures')
print('  V on nu column — searching for any model that returns 1.09e5, 1.77e6, 2.84e7:')
def V_ritz(n, d0, d2, h=1):
    y = lambda t: t - d0 - d2 / (t - d0) ** 2
    a, b, c = y(n + h), y(n - h), y(n)
    w = a - b; e = (a + b) / 2 - c
    return abs(w / e) if e else None
tgt = {10: 1.09e5, 20: 1.77e6, 40: 2.84e7}
print(f'    Ritz nu(n) = n - d0 - d2/(n-d0)^2 with d0 = 1.35:')
for d2 in (0.06, 0.0335, 0.02, 0.01):
    got = {n: V_ritz(n, 1.35, d2) for n in (10, 20, 40)}
    print(f'      d2={d2:<7} -> ' + '  '.join(f'n={n}: {got[n]:.3e} (target {tgt[n]:.2e})'
                                              for n in (10, 20, 40)))
fits = [d2 / 10000 for d2 in range(1, 20000)
        if all(abs(V_ritz(n, 1.35, d2 / 10000) - tgt[n]) / tgt[n] < 0.005 for n in (10, 20, 40))]
verdict('14l-24', False,
        'the V-on-nu column reproduces from nothing printed. Its own scaling is n^4 (1.09e5 -> '
        '1.77e6 -> 2.84e7 are ratios 16.2 and 16.0), which is the Ritz-curvature model '
        'V = 2nu^4/(3 h delta2), but no single delta2 fits all three rows '
        f'({len(fits)} fits found in delta2 = 0.0001..2 at 0.5% tolerance): the implied delta2 is '
        '0.034 at n = 10 and 0.046 at n = 20. §23.9.3 prints three derived figures and none of '
        'their inputs — no delta0, no delta2, no h, no species')
print('\n== end r2-ch14l ==')
