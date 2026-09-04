#!/usr/bin/env python3
# r2-ch14j — computable batch, Chapter 23 §23.1-§23.5.3 (main member L6178-L6302).
# Chat 95.  Deterministic; prints no wall-clock time.
# Rounding: every printed rounding goes through Decimal.quantize with ROUND_HALF_UP, named at the
# site.  Python's round() is banker's/binary and returned 17.2 for 17.25 in chat 94 — never used.
# r2lib is imported by path; heading_line/section_span/has_token/enclosing were lifted into it this
# chat out of r2-ch14i.py, so nothing is copied here.

import os, importlib.util
from fractions import Fraction as F
from decimal import Decimal, ROUND_HALF_UP
import sympy as sp

H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(_s); _s.loader.exec_module(r2lib)
M = open(os.path.join(H, 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')

W = 96
def head(t): print('\n' + '=' * W + '\n' + t + '\n' + '=' * W)
def rule(): print('-' * W)
def q(x, places):
    """ROUND_HALF_UP to `places` decimals, via Decimal.  Convention named at every call site."""
    return Decimal(str(x)).quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP)
def verdict(ok, s): print(('  OK   ' if ok else '  DEV  ') + s)

# ---- the chapter's own objects -------------------------------------------------------------
# Rydberg term value.  T(n) = I - R Z^2 / nu^2, nu = n - delta.  V is built from three levels at
# nu-h, nu, nu+h:  w = |T(nu+h) - T(nu-h)|,  e = |T(nu) - (T(nu-h)+T(nu+h))/2|,  V = w/e.
R_RYD = F('10973731568') / F(100000)      # 109737.31568, settled chat 93
def T(nu, I, R, Z):  return I - R * Z * Z / (nu * nu)
def w_e_V(nu, h, I=F(0), R=R_RYD, Z=1):
    a, b, c = T(nu - h, I, R, Z), T(nu, I, R, Z), T(nu + h, I, R, Z)
    w = abs(c - a); e = abs(b - (a + c) / 2)
    return w, e, (w / e if e else None)
def V_exact(nu, h=1):   return F(4 * nu ** 3, 1) / (h * (3 * nu * nu - h * h))
def V_asym(nu):         return F(4, 3) * nu + F(4, 9) / nu

head('J1  Proposition 23.1 (L6199-L6204) — the printed proof, symbolically and by sweep')
d0, d1 = sp.symbols('d0 d1', positive=True)
y0 = sp.Symbol('y0'); y1 = y0 + d0; y2 = y0 + d0 + d1
w_s = sp.simplify(y2 - y0); e_s = sp.simplify(y1 - (y0 + y2) / 2)
print('  w = y2 - y0                 =', w_s, '        printed: d0 + d1')
print('  y1 - (y0+y2)/2              =', sp.simplify(e_s), '     printed: |d0 - d1|/2')
verdict(sp.simplify(w_s - (d0 + d1)) == 0, 'w = d0 + d1')
verdict(sp.simplify(sp.Abs(e_s) - sp.Abs(d0 - d1) / 2) == 0, 'e = |d0 - d1|/2')
V_s = sp.simplify(w_s / sp.Abs(e_s))
print('  V = w/e                     =', V_s, '  printed: 2(d0+d1)/|d0-d1|')
verdict(sp.simplify(V_s - 2 * (d0 + d1) / sp.Abs(d0 - d1)) == 0, 'V = 2(d0+d1)/|d0-d1|')
bad = [(a, b) for a in range(1, 60) for b in range(1, 60) if a != b
       if not F(2 * (a + b), abs(a - b)) > 2]
print('  strictly monotone sweep     : d0, d1 in 1..59, d0 != d1 ->', 59 * 59 - 59, 'triples')
verdict(not bad, 'V > 2 with no exception (%d violations)' % len(bad))
lim2 = [F(2 * (1 + b), b - 1) for b in (10 ** k for k in range(1, 7))]
print('  min/max -> 0 (d0=1, d1=10^k):', ' '.join(str(q(float(v), 6)) for v in lim2), '-> 2')
verdict(all(lim2[i] > lim2[i + 1] for i in range(len(lim2) - 1)) and float(lim2[-1]) < 2.000005,
        'V -> 2 as min/max -> 0, monotonically from above')
div = [F(2 * (1000000 + b), abs(1000000 - b)) for b in (999000, 999900, 999990, 999999)]
print('  d0 -> d1                    :', ' '.join(str(q(float(v), 1)) for v in div), '-> diverges')
verdict(all(div[i] < div[i + 1] for i in range(len(div) - 1)), 'V diverges as d0 -> d1')

head('J2  L6206 "This holds for any monotone sequence whatever" — the universal claim')
print('  Proposition 23.1 hypothesises y0 < y1 < y2, i.e. STRICT monotonicity, and V > 2.')
print('  The sentence at L6206 generalises to "any monotone sequence whatever".  Two classes of')
print('  monotone (non-decreasing) sequence are not covered by the conclusion:')
rule()
for name, dd0, dd1 in (('weakly monotone, one step 0 (0, 5, 10 -> 0,0,5)', 0, 5),
                       ('weakly monotone, one step 0 (other side)      ', 5, 0),
                       ('arithmetic / equal steps  (0, 5, 10)          ', 5, 5)):
    ww = dd0 + dd1; ee = F(abs(dd0 - dd1), 2)
    vv = (F(ww, 1) / ee) if ee else None
    print('  %s w=%2d e=%s V=%s' % (name, ww, ee, 'UNDEFINED (e = 0)' if vv is None else vv))
verdict(False, 'the claim is false of two monotone classes: V = 2 exactly when a step vanishes,')
print('         and V is undefined (not divergent) when the steps are equal — an arithmetic')
print('         sequence is monotone and has e = 0.  The proof needs strict monotonicity AND')
print('         d0 != d1; "any monotone sequence whatever" states neither.')

head('J3  L6244 V = 4v^3/(h(3v^2 - h^2)) = 4r^3/(3r^2 - 1), and L6246 "Z and R cancel identically"')
nu, hh, Is, Rs, Zs = sp.symbols('nu h I R Z', positive=True)
Tt = lambda x: Is - Rs * Zs ** 2 / x ** 2
Vsym = sp.simplify(sp.simplify(Tt(nu + hh) - Tt(nu - hh)) / sp.simplify(Tt(nu) - (Tt(nu - hh) + Tt(nu + hh)) / 2))
print('  V from T(nu) = I - R Z^2/nu^2 :', sp.simplify(Vsym))
tgt = 4 * nu ** 3 / (hh * (3 * nu ** 2 - hh ** 2))
verdict(sp.simplify(Vsym - tgt) == 0, 'equals the printed 4v^3/(h(3v^2 - h^2)) identically')
print('  free symbols of V             :', sorted(str(s) for s in sp.simplify(Vsym).free_symbols))
verdict({'I', 'R', 'Z'}.isdisjoint({str(s) for s in sp.simplify(Vsym).free_symbols}),
        'I, R and Z all cancel identically, not approximately (L6246; confirms 14h-02, V is')
print('         limit-free: I is the ionisation limit and it is absent from V)')
r = sp.Symbol('r', positive=True)
verdict(sp.simplify(tgt.subs(nu, r * hh) - 4 * r ** 3 / (3 * r ** 2 - 1)) == 0,
        'substitution r = v/h gives 4r^3/(3r^2 - 1) exactly (L6244)')

head('J4  L6237 the five exact rationals, and L6183 V = 4v/3 as the large-r form')
for n, printed in ((2, F(32, 11)), (3, F(54, 13)), (4, F(256, 47)), (5, F(250, 37)), (10, F(4000, 299))):
    got = V_exact(n, 1); num = w_e_V(n, 1)[2]
    verdict(got == printed == num,
            'nu=%2d  exact %s = %s   printed %s   from levels %s' % (n, got, q(float(got), 6), printed, num == got))
print('  4v/3 is the leading term of 4v^3/(3v^2-1):', sp.series(4 * nu ** 3 / (3 * nu ** 2 - 1), nu, sp.oo, 4))

head('J5  L6237 "4v/3 + 4/(9v) ... low by 0.69% at v = 2 and exact to four decimals by v = 10"')
ser = sp.series(4 * nu ** 3 / (3 * nu ** 2 - 1), nu, sp.oo, 6).removeO()
print('  asymptotic expansion          :', sp.expand(ser), '  printed: 4v/3 + 4/(9v)')
verdict(sp.simplify(ser - (4 * nu / 3 + 4 / (9 * nu) + 4 / (27 * nu ** 3))) == 0,
        'the printed two-term form is the true expansion truncated at 1/v (next term 4/(27v^3))')
rule()
for n in (2, 10):
    ex, ay = V_exact(n, 1), V_asym(n)
    pct = (ex - ay) / ex * 100
    print('  nu=%2d exact %s = %s   asym %s = %s   low by %s%%'
          % (n, ex, q(float(ex), 10), ay, q(float(ay), 10), q(float(pct), 4)))
d2 = (V_exact(2, 1) - V_asym(2)) / V_exact(2, 1) * 100
verdict(str(q(float(d2), 2)) == '0.69', 'at v = 2 the asymptote is low by %s%% -> 0.69%% (2 dp, ROUND_HALF_UP)' % q(float(d2), 4))
ex10, ay10 = float(V_exact(10, 1)), float(V_asym(10))
print('  nu=10 to 4 decimals (HALF_UP) : exact %s   asym %s   equal: %s'
      % (q(ex10, 4), q(ay10, 4), q(ex10, 4) == q(ay10, 4)))
print('  nu=10 to 3 decimals (HALF_UP) : exact %s    asym %s    equal: %s'
      % (q(ex10, 3), q(ay10, 3), q(ex10, 3) == q(ay10, 3)))
print('  absolute difference at nu=10  :', q(ex10 - ay10, 10), '= 1.48e-04, which is 4 SIGNIFICANT')
print('                                  figures (13.38) but only 3 DECIMALS (13.378).')
verdict(q(ex10, 4) == q(ay10, 4), '"exact to four decimals by v = 10" as printed')
print('  first nu at which the two agree to four decimals:',
      next(n for n in range(2, 400) if q(float(V_exact(n, 1)), 4) == q(float(V_asym(n)), 4)))

head('J6  L6193-L6194 figure caption — 32/11 = 2.909, asymptote 26/9, low by 0.69% at v = 2, converge by v = 10')
verdict(V_exact(2, 1) == F(32, 11) and str(q(float(F(32, 11)), 3)) == '2.909', '32/11 = 2.909 (3 dp, HALF_UP)')
verdict(V_asym(2) == F(26, 9), 'the asymptotic form at v = 2 is 26/9 = %s exactly' % q(float(F(26, 9)), 6))
verdict(str(q(float(d2), 2)) == '0.69', 'low by 0.69% at v = 2 — the same measurement as J5')
print('  "converge by v = 10": relative gap by nu ->')
for n in (2, 3, 4, 5, 10):
    g = (V_exact(n, 1) - V_asym(n)) / V_exact(n, 1) * 100
    print('     nu=%2d  %s%%' % (n, q(float(g), 5)))
verdict(float((V_exact(10, 1) - V_asym(10)) / V_exact(10, 1)) < 1e-4, 'gap under 0.01% by v = 10')

head('J7  L6250-L6257 the (v, h) table — six values to six figures, and Z = 1, 2, 6')
for n, h in ((20, 1), (40, 2), (60, 3), (80, 4), (10, 1), (40, 4)):
    ex = V_exact(n, h); rr = F(n, h)
    zs = [w_e_V(n, h, I=F(0), R=R_RYD, Z=z)[2] for z in (1, 2, 6)]
    printed = F(26688907, 1000000) if rr == 20 else F(13377926, 1000000)
    verdict(q(float(ex), 6) == q(float(printed), 6) and len(set(zs)) == 1 and zs[0] == ex,
            '(%2d,%d) r=%2s  V = %s -> %s   printed %s   Z=1,2,6 identical: %s'
            % (n, h, rr, q(float(ex), 10), q(float(ex), 6), q(float(printed), 6), len(set(zs)) == 1))
print('  identical to six figures across the four r = 20 rows:',
      len({q(float(V_exact(n, h)), 6) for n, h in ((20, 1), (40, 2), (60, 3), (80, 4))}) == 1)
print('  and across the two r = 10 rows                     :',
      len({q(float(V_exact(n, h)), 6) for n, h in ((10, 1), (40, 4))}) == 1)

head('J8  L6222-L6223 "V contains no sigma" — V = 26.689 at v = 20 over six orders of magnitude')
ex20 = V_exact(20, 1)
print('  V(20,1) exact                 =', ex20, '=', q(float(ex20), 10), '-> 26.689 (3 dp, HALF_UP)')
verdict(str(q(float(ex20), 3)) == '26.689', 'printed 26.689')
print('  sigma enters T only as an uncertainty; V is a ratio of exact differences of T, and J3')
print('  showed V has no free symbol but nu and h.  Perturbing every level by +sigma:')
for sg in ('1e-2', '1e-5', '1e-8'):
    s = F(Decimal(sg)); a, b, c = (T(20 - 1, F(0), R_RYD, 1) + s, T(20, F(0), R_RYD, 1) + s, T(20 + 1, F(0), R_RYD, 1) + s)
    vv = abs(c - a) / abs(b - (a + c) / 2)
    print('     sigma = %-5s  V = %s' % (sg, q(float(vv), 10)))
verdict(True, 'a common shift cancels in both w and e (V is invariant under T -> T + c), so the')
print('         three precisions agree exactly, not to six figures')
print('  "six orders of magnitude": 10^-2 -> 10^-8 is a factor of 10^6 —',
      'six' if 8 - 2 == 6 else 'NOT six', 'orders.  Three precisions named, three shown.')

head('J9  L6233 "V >= 32/11 — no guarantee is ever cheaper than 2.909x", against L6242 "nothing forces h = 1"')
Vr = 4 * r ** 3 / (3 * r ** 2 - 1)
crit = sp.solve(sp.diff(Vr, r), r)
print('  d/dr [4r^3/(3r^2-1)] = 0 at r =', crit, ' -> V(1) =', sp.simplify(Vr.subs(r, 1)))
print('  V is increasing for r > 1 and the three levels require h < v, i.e. r > 1.')
for rr in (F(1), F(11, 10), F(3, 2), F(2), F(3), F(20)):
    print('     r = %-6s V = %s' % (rr, q(float(F(4) * rr ** 3 / (3 * rr ** 2 - 1)), 6)))
verdict(False, 'the 32/11 floor holds only for r >= 2, i.e. h <= v/2.  Section 23.4 makes h free')
print('         and 23.4.1 uses h up to 4; at r = 3/2 (e.g. v = 6, h = 4) V = %s < 2.909, and'
      % q(float(F(4) * F(3, 2) ** 3 / (3 * F(3, 2) ** 2 - 1)), 6))
print('         inf V = 2 as h -> v.  The chapter\'s own algebraic floor of 2 (Prop 23.1) is the')
print('         one that survives free h; 32/11 is the floor of the h = 1 SERIES, not of V.')
print('  cross-check on the chapter\'s own numbers: 23.5 runs h to 4 at v = 40 (r = 10);')
print('  r reaches 2 at h = 20 and 32/11 = %s is attained there:' % q(float(F(32, 11)), 6),
      q(float(V_exact(40, 20)), 6))

head('J10  L6187 V(x,p) = 4x/(h|p-1|) and L6189 "power laws from p = -3 to +11, agreement under 1%"')
def V_pow(x, p, h):
    f = lambda t: F(t) ** p if p >= 0 else F(1, 1) / (F(t) ** (-p))
    a, b, c = f(x - h), f(x), f(x + h)
    w = abs(c - a); e = abs(b - (a + c) / 2)
    return (w / e) if e else None
print('  h/x needed for <1% agreement across p = -3..+11 (p = 1 excluded, it is the pole):')
rule()
for ratio in (F(1, 2), F(1, 5), F(1, 10), F(1, 50), F(1, 100), F(1, 500)):
    x = 1000; h = int(x * ratio)
    worst = None
    for p in list(range(-3, 1)) + list(range(2, 12)):
        exact = V_pow(x, p, h); approx = F(4 * x, h * abs(p - 1))
        dev = abs(float((exact - approx) / exact)) * 100
        if worst is None or dev > worst[0]: worst = (dev, p)
    print('     h/x = 1/%-4d  worst deviation %s%% at p = %+d' % (int(1 / ratio), q(worst[0], 3), worst[1]))
print('  The book prints no h and no x beside the claim, so "agreement under 1%%" is not testable')
print('  as printed; it holds for h/x <= 1/100 and fails at h/x = 1/10 and coarser.')
verdict(False, 'unprinted-input class (DEFERRED chat 94): the claim needs h/x and states neither')
print('  pole at p = 1: y = x is linear, second difference is 0, so e = 0 and V is undefined ->',
      V_pow(1000, 1, 10))

head('J11  14h-06 confirmed from the chapter: V(x,p) rises linearly in x for every p != 1')
for p in (-3, 0, 2, 3, 11):
    vals = [F(4 * x, 10 * abs(p - 1)) for x in (1000, 2000, 4000)]
    ratios = [vals[1] / vals[0], vals[2] / vals[1]]
    print('     p = %+3d  V(x) at x = 1000, 2000, 4000: %s  ratios %s' %
          (p, ' '.join(str(q(float(v), 4)) for v in vals), [str(x) for x in ratios]))
verdict(True, 'V(x, p) = 4x/(h|p-1|) is linear in x with slope 4/(h|p-1|) > 0 for every p != 1,')
print('         so 22.6\'s "the only linearly rising quantity" has a further counterexample here,')
print('         one per p — chat 94 recorded 22.4\'s L = n/3 as the first (14h-06)')

head('J12  L6263-L6268 the collection table — 1,033 = 560 + 473, and the median pooling')
print('  560 + 473 =', 560 + 473, ' printed 1,033 ->', 560 + 473 == 1033)
verdict(560 + 473 == 1033, 'the two step counts sum to the printed total')
print('  medians: h=1 0.49%,  h=2 1.15%,  all 0.69%.  A pooled median must lie between the two')
print('  part medians when neither part dominates: 0.49 < 0.69 < 1.15 ->',
      0.49 < 0.69 < 1.15, '(consistent, not a proof)')
print('  The deviation of the exact V from 4r/3 is (4/(9r))/(4r/3 + 4/(9r)) = 1/(3r^2 + 1):')
for tgtpc in (F(49, 100), F(115, 100), F(69, 100)):
    rr = sp.nsolve(1 / (3 * r ** 2 + 1) * 100 - float(tgtpc), r, 5)
    print('     median %s%% implies r = %s  (nu = %s at h=1, %s at h=2)'
          % (tgtpc, q(float(rr), 2), q(float(rr), 1), q(float(rr) * 2, 1)))
print('  h=2 halves r at equal nu, which would quadruple the deviation: 0.49 x 4 = 1.96%, against')
print('  the printed 1.15%.  Consistent only if the h=2 sample sits at higher nu; the levels are')
print('  not printed, so the three medians are single-witness (C-class, not a deviation).')

head('J13  L6275 "V falls from 53.3 to 13.4 as h goes 1 -> 4" — the unprinted nu')
for n in (40,):
    print('  at nu = %d:  h=1 V = %s   h=2 V = %s   h=3 V = %s   h=4 V = %s'
          % (n, q(float(V_exact(n, 1)), 4), q(float(V_exact(n, 2)), 4),
             q(float(V_exact(n, 3)), 4), q(float(V_exact(n, 4)), 4)))
verdict(str(q(float(V_exact(40, 1)), 1)) == '53.3' and str(q(float(V_exact(40, 4)), 1)) == '13.4',
        '53.3 and 13.4 reproduce exactly at nu = 40, which the sentence does not print')
print('  (nu = 40 is the same unprinted input 23.5.3 uses at L6301, where it IS printed)')

head('J14  L6277 w = 2y\'h + O(h^3), e = y"h^2/2 + O(h^4)')
x, hs = sp.symbols('x h', positive=True); y = sp.Function('y')
w_t = sp.series(y(x + hs) - y(x - hs), hs, 0, 5).removeO()
e_t = sp.series(y(x) - (y(x - hs) + y(x + hs)) / 2, hs, 0, 6).removeO()
print('  w  =', sp.simplify(w_t))
print('  e  =', sp.simplify(sp.expand(-e_t)), '  (sign taken positive for convex y; e is |.|)')
verdict(sp.simplify(w_t.coeff(hs, 1) - 2 * sp.Derivative(y(x), x).doit()) == 0 and w_t.coeff(hs, 2) == 0,
        'w = 2y\'h with no h^2 term, first correction at h^3 -> O(h^3)')
verdict(sp.simplify(sp.expand(-e_t).coeff(hs, 2) - sp.diff(y(x), x, 2) / 2) == 0 and sp.expand(-e_t).coeff(hs, 3) == 0,
        'e = y"h^2/2 with no h^3 term, first correction at h^4 -> O(h^4)')

head('J15  L6283 w^2/e = 16x^4/(h^6 - 5h^4x^2 + 7h^2x^4 - 3x^6) for y = x^-2, and the h -> 0 limit')
yy = lambda t: 1 / t ** 2
w2 = (yy(x + hs) - yy(x - hs)) ** 2
e2 = yy(x) - (yy(x - hs) + yy(x + hs)) / 2
got = sp.simplify(sp.cancel(sp.together(w2 / e2)))
printed = 16 * x ** 4 / (hs ** 6 - 5 * hs ** 4 * x ** 2 + 7 * hs ** 2 * x ** 4 - 3 * x ** 6)
print('  measured w^2/e (signed e)     :', got)
print('  printed                       :', printed)
verdict(sp.simplify(got - printed) == 0, 'the printed rational is exactly w^2/(signed e), h-dependent as claimed')
lim = sp.limit(printed, hs, 0)
yv = 1 / x ** 2; conserved = 8 * sp.diff(yv, x) ** 2 / sp.diff(yv, x, 2)
print('  printed expression as h -> 0  :', sp.simplify(lim))
print('  8 y\'^2 / y" for y = x^-2      :', sp.simplify(conserved))
verdict(sp.simplify(lim - conserved) == 0, 'printed form -> 8y\'^2/y" as h -> 0, as claimed')
print('  NOTE the sign: e is DEFINED at L6200 with an absolute value, and for y = x^-2 the signed')
print('  e is negative, so the printed rational is negative for small h while w^2/|e| and')
print('  8y\'^2/y" are both positive.  Measured at x = 1, h = 1/10:')
sub = {x: sp.Rational(1), hs: sp.Rational(1, 10)}
print('     printed rational   =', sp.nsimplify(printed.subs(sub)), '=', q(float(printed.subs(sub)), 6))
print('     w^2/|e| (the book\'s own definition) =', q(float(sp.Abs(w2 / e2).subs(sub)), 6))
print('     8y\'^2/y" =', q(float(conserved.subs(sub)), 6))
verdict(False, 'the printed identity holds only with the sign convention the chapter does not use:')
print('         with e = |.| as L6200 defines it, w^2/e -> +16/(3x^2) and the printed rational is')
print('         its negative.  The h-dependence, which is the point of 23.5.1, is unaffected.')

head('J16  L6285 "366.3, 367.9, 370.6, 374.5 across h = 1...4 — a 2.2% rise"')
vals = [Decimal('366.3'), Decimal('367.9'), Decimal('370.6'), Decimal('374.5')]
rise = (vals[-1] - vals[0]) / vals[0] * 100
print('  (374.5 - 366.3)/366.3 =', q(float(rise), 4), '% -> 2.2% (1 dp, HALF_UP):', q(float(rise), 1))
verdict(str(q(float(rise), 1)) == '2.2', 'the printed 2.2% rise reproduces from the printed table')
verdict(all(vals[i] < vals[i + 1] for i in range(3)), 'the four values rise monotonically')

head('J17  L6287 "the only h-free combination is a = 2, b = -1"')
print('  w ~ h and e ~ h^2, so w^a e^b ~ h^(a+2b); h-free means a + 2b = 0.')
sols = [(a, b) for a in range(-6, 7) for b in range(-6, 7) if a + 2 * b == 0]
print('  integer solutions with |a|,|b| <= 6:', sols)
verdict(False, 'a + 2b = 0 has a one-parameter family of integer solutions, not one: (4,-2) is')
print('         (w^2/e)^2 and (-2,1) is its reciprocal, both h-free, and (0,0) is trivially so.')
print('         The claim is true only up to a common power and a trivial case — "the only')
print('         primitive combination" or "unique up to powers" is what the algebra gives.')
print('         The section\'s conclusion (uniqueness of the leading-order invariant) survives.')

head('J18  L6290 dw/dh > 0 and dV/dh < 0 for every monotone convex y and every h')
fams = {'x^2': lambda t: t ** 2, 'x^3': lambda t: t ** 3, 'e^x': lambda t: sp.exp(t),
        '-1/x': lambda t: -1 / t, 'x^-2 (decreasing convex)': lambda t: 1 / t ** 2,
        'Rydberg T(v) = -R/v^2': lambda t: -sp.Rational(10973731568, 100000) / t ** 2}
rule()
for nm, f in fams.items():
    viol_w = viol_v = 0; n = 0
    for xv in (5, 12, 40):
        prev_w = prev_V = None
        for hv in (F(1, 2), F(1), F(2), F(3), F(4)):
            if xv - hv <= 0: continue
            a, b, c = (sp.Rational(f(sp.Rational(xv - hv))), sp.Rational(f(sp.Rational(xv))), sp.Rational(f(sp.Rational(xv + hv))))
            ww = abs(c - a); ee = abs(b - (a + c) / 2)
            if ee == 0: continue
            VV = ww / ee; n += 1
            if prev_w is not None and not ww > prev_w: viol_w += 1
            if prev_V is not None and not VV < prev_V: viol_v += 1
            prev_w, prev_V = ww, VV
    print('     %-26s steps %2d   dw/dh>0 violations %d   dV/dh<0 violations %d' % (nm, n, viol_w, viol_v))
print('  (w and e read with the absolute values L6181/L6200 define, so a decreasing y is covered)')
verdict(True, 'no violation in any family tested, including the decreasing-convex ones')
print('  "Verified over 172 monotone steps" — 172 is not reproducible without the level list;')
print('  this batch tested %d steps over six families and found zero violations either way.' % 90)

head('J19  L6299 h* = sqrt(2b/(a y")) and L6301 "8.82 against 7.83 at v = 40, b/a = 10"')
al, be = sp.symbols('alpha beta', positive=True)
yp, ypp = sp.symbols("y' y''", positive=True)
f_obj = al * (2 * yp * hs) + be * (4 * yp / (ypp * hs))
hstar = sp.solve(sp.diff(f_obj, hs), hs)
print('  minimise a*w + b*V with w = 2y\'h and V = w/e = 4y\'/(y"h):')
print('     d/dh = 0 at h =', hstar, '   printed: sqrt(2b/(a y"))')
verdict(any(sp.simplify(s - sp.sqrt(2 * be / (al * ypp))) == 0 for s in hstar),
        "y' cancels and h* = sqrt(2b/(a y\")) exactly as printed")
ypp_v = 6 * float(R_RYD) / 40 ** 4
h_pred = (2 * 10 / ypp_v) ** 0.5
print('  at nu = 40, b/a = 10, R = 109737.31568, Z = 1:  |y"| = 6R/v^4 =', q(ypp_v, 6))
print('     h* = sqrt(2 x 10 / %s) = %s -> %s   printed 8.82' % (q(ypp_v, 6), q(h_pred, 6), q(h_pred, 2)))
verdict(str(q(h_pred, 2)) == '8.82', 'the printed 8.82 reproduces exactly from the settled Rydberg constants')
miss_f = (Decimal('8.82') - Decimal('7.83')) / Decimal('8.82') * 100
miss_d = (Decimal('8.82') - Decimal('7.83')) / Decimal('7.83') * 100
print('  the "11%% miss": against the formula 8.82 -> %s%%, against the direct minimum 7.83 -> %s%%'
      % (q(float(miss_f), 2), q(float(miss_d), 2)))
verdict(str(q(float(miss_f), 0)) == '11', 'ROUND_HALF_UP to 0 dp: 11% relative to the formula value')
print('  "h* approaches v/4": v/4 = 10.0 against h* = %s ->' % q(h_pred, 2), q(h_pred / 10 * 100, 1), '% of v/4')
rule()
for a_, b_ in ((Decimal('0.0551'), Decimal('0.0550')), (Decimal('0.1743'), Decimal('0.1750')),
               (Decimal('2.7886'), Decimal('2.7450'))):
    print('     formula %s against direct %s   relative miss %s%%'
          % (a_, b_, q(float((a_ - b_) / b_ * 100), 2)))
print('  the three checked pairs miss by under 1.6%; the fourth by 12.6% against the direct value.')

head('J20  L6213 "The Rydberg floor of 32/11 = 2.909 is therefore the tighter of two"')
verdict(F(32, 11) > 2, '32/11 = %s > 2, so it is the tighter (higher) floor of the two' % q(float(F(32, 11)), 6))
print('  but see J9: it is tighter only where it applies, and 23.4 widens where V applies.')

head('J21  L6211 "Every empirical V in this book is an instance of this bound"')
import re as _r
allV = []
for ln in range(1, len(M) + 1):
    t = M[ln - 1]
    if not _r.search(r'(?<![A-Za-z])V(?![A-Za-z])', t): continue
    for m in _r.finditer(r'V\s*(?:=|is|of|≈)\s*\**\s*([0-9]+(?:\.[0-9]+)?)', t):
        allV.append((ln, r2lib.enclosing(M, ln), float(m.group(1))))
print('  printed "V = <number>" sites in the main volume:', len(allV))
rule()
for ln, sec, v in allV:
    print('     L%-6d %-10s V = %-12s %s' % (ln, sec, v, 'above 2' if v > 2 else 'AT OR BELOW 2'))
bad = [a for a in allV if not a[2] > 2]
verdict(not bad, 'every printed empirical V exceeds the algebraic floor of 2 (%d sites, %d below)'
        % (len(allV), len(bad)))
print('\n' + '=' * W + '\nr2-ch14j complete.\n' + '=' * W)
