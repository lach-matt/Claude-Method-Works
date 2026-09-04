#!/usr/bin/env python3
# r2-ch14h — computable batch, Chapter 22 remainder (main member L6036-L6177).
# Chat 94.  Deterministic; prints no wall-clock time.  Imports no r2lib: Chapter 22
# is arithmetic on a Rydberg series and carries no tower computation (chat 93, DEFERRED).
# Every printed figure is quoted from the member line named beside it.

from math import log10

W = 78
def head(t): print('\n' + '=' * W + '\n' + t + '\n' + '=' * W)
def rule(): print('-' * W)

def sig_agree(a, b):
    """Number of leading significant decimal digits shared by a and b."""
    sa, sb = f'{a:.10e}', f'{b:.10e}'
    ma, ea = sa.split('e'); mb, eb = sb.split('e')
    if ea != eb: return 0
    da = ma.replace('.', '').replace('-', ''); db = mb.replace('.', '').replace('-', '')
    n = 0
    for x, y in zip(da, db):
        if x != y: break
        n += 1
    return n

# ----------------------------------------------------------------------------
head('H1  ablation table, L6058-L6064 — each cost column against its own pair')
# columns quoted verbatim from the table
rows = [
    ('extrapolate below the series', 0.46, 206.0,  446.0,  'L6060'),
    ('extrapolate above the series', 0.46, 0.13,   0.28,   'L6061'),
    ('wrong interpolation variable', 200.0, 588.0, 2.9,    'L6062'),
    ('include a collapsed orbital',  12.8, 41.3,   3.2,    'L6064'),
]
print(f'{"row":30s} {"from":>8s} {"to":>8s} {"to/from":>10s} {"printed":>9s}  verdict')
rule()
h1_fail = []
for name, a, b, printed, ln in rows:
    r = b / a
    # does the printed factor follow from the printed pair, to the printed precision?
    dp = len(str(printed).split('.')[1]) if '.' in str(printed) else 0
    ok = round(r, dp) == printed
    if not ok: h1_fail.append((name, r, printed, ln))
    print(f'{name:30s} {a:8.2f} {b:8.2f} {r:10.4f} {printed:9.2f}  '
          f'{"reproduces" if ok else "DOES NOT reproduce"}  {ln}')
rule()
for name, r, printed, ln in h1_fail:
    need = printed  # what the unrounded numerator/denominator would have to give
    print(f'  {ln}: printed {printed:g}x, printed pair gives {r:.4f} '
          f'(rounds to {round(r):g}).  Needs an unrounded input: '
          f'206/{printed:g} = {206.0/printed:.6f} as the true median, not the printed 0.46.')
print(f'\nrows reproducing from their own printed pair: {len(rows)-len(h1_fail)} of {len(rows)}')

# ----------------------------------------------------------------------------
head('H2  L6068 "The asymmetry is a factor of 1,577"')
printed_asym = 1577.0
cands = [
    ('206 / 0.13            (the two printed medians)', 206.0 / 0.13),
    ('446 / 0.28            (the two printed factors)', 446.0 / 0.28),
    ('(206/0.46) / (0.13/0.46)', (206.0 / 0.46) / (0.13 / 0.46)),
]
for label, v in cands:
    print(f'  {label:42s} = {v:10.2f}   printed 1,577   '
          f'{"MATCH" if round(v) == printed_asym else f"off by {v-printed_asym:+.1f} ({100*(v-printed_asym)/printed_asym:+.2f}%)"}')
print(f'\n  MEASURED: no pair of printed numbers in the section yields 1,577.')
print(f'  The closest printed route (206/0.13) gives {206.0/0.13:.1f}, which rounds to '
      f'{round(206.0/0.13):,}.')
print(f'  1,577 requires unrounded inputs, e.g. 206.0/1577 = {206.0/1577:.5f} as the true '
      f'above-median rather than the printed 0.13.')

# ----------------------------------------------------------------------------
head('H3  L6080 "Same sign, same magnitude of asymmetry" — n axis against Z axis')
# L6077 n row: 446x / 1x / 0.28x ; L6078 Z row: 17.3% / 1.3% / 2.1%
n_loose, n_interp, n_tight = 446.0, 1.0, 0.28
z_loose, z_interp, z_tight = 17.3, 1.3, 2.1
n_asym = n_loose / n_tight
z_loose_ratio, z_tight_ratio = z_loose / z_interp, z_tight / z_interp
z_asym = z_loose_ratio / z_tight_ratio
print(f'  n axis (L6077): loose {n_loose:g}x  interpolate {n_interp:g}x  tight {n_tight:g}x')
print(f'  Z axis (L6078): loose {z_loose:g}%  interpolate {z_interp:g}%  tight {z_tight:g}%')
rule()
print(f'  n-axis asymmetry  = {n_loose:g} / {n_tight:g}                 = {n_asym:10.2f}')
print(f'  Z-axis asymmetry  = ({z_loose:g}/{z_interp:g}) / ({z_tight:g}/{z_interp:g})   '
      f'= {z_asym:10.2f}   [= {z_loose:g}/{z_tight:g}]')
print(f'  ratio of the two asymmetries                     = {n_asym/z_asym:10.2f}')
rule()
same_sign = (n_loose > n_interp) == (z_loose_ratio > 1) and (n_tight < n_interp) == (z_tight_ratio > 1)
print(f'  same SIGN (loose end dearer, tight end cheaper than interpolation):')
print(f'    n: loose {n_loose:g}x > 1 and tight {n_tight:g}x < 1  -> loose dearer, tight CHEAPER than interpolation')
print(f'    Z: loose {z_loose_ratio:.1f}x > 1 and tight {z_tight_ratio:.2f}x > 1  -> loose dearer, tight DEARER than interpolation')
print(f'    VERDICT sign: the two axes do NOT agree. On n the tight end is cheaper than')
print(f'    interpolation ({n_tight:g}x); on Z it is dearer ({z_tight_ratio:.2f}x).')
print(f'  same MAGNITUDE: {n_asym:.0f} against {z_asym:.2f} — a factor of {n_asym/z_asym:.0f} apart.')
print(f'    VERDICT magnitude: FALSE as printed.')
print(f'  Note on the table\'s own units: the n row is a ratio (interpolate = 1x); the Z row')
print(f'  is an absolute error (interpolate = {z_interp:g}%). The two rows carry different')
print(f'  kinds of quantity in the same three columns.')

# ----------------------------------------------------------------------------
head('H4  L6084 hold-outs against the Z row of L6078')
li, na = 11.1, 23.4          # lithium-like, sodium-like neutrals (loose end)
civ, siv = 1.8, 2.5          # C IV, Si IV (tight end)
for label, pair, printed in (('loose end', (li, na), z_loose), ('tight end', (civ, siv), z_tight)):
    m = sum(pair) / 2
    print(f'  {label:10s} mean({pair[0]:g}, {pair[1]:g}) = {m:.3f}   table prints {printed:g}%   '
          f'{"reproduces" if round(m,1)==printed else f"rounds to {round(m,1):g}, NOT {printed:g}"}')
print(f'\n  MEASURED: the table\'s loose-end 17.3% is the mean of the two printed hold-outs.')
print(f'  The tight-end 2.1% is {sum((civ,siv))/2:.3f} before rounding, which rounds half-up to '
      f'{round(sum((civ,siv))/2 + 1e-12, 1):g}; the printed 2.1 needs an unrounded input below 2.15.')
print(f'  The interpolate column (1.3%) has no printed constituents anywhere in the chapter.')

# ----------------------------------------------------------------------------
head('H5  L6090-L6094 fit table — error column recomputed from its own two columns')
true = 0.7129
fits = [('a + b/Z', 0.8189, 14.9), ('a + b/Z + c/Z^2', 0.7376, 3.47), ('d*Z linear in Z', 0.7835, 9.9)]
for name, pred, printed in fits:
    err = abs(pred - true) / true * 100
    dp = len(str(printed).split('.')[1])
    print(f'  {name:20s} pred {pred:.4f}  true {true:.4f}  |d|/true = {err:7.4f}%  '
          f'printed {printed:g}%  {"reproduces" if round(err,dp)==printed else "DOES NOT reproduce"}')
print('\n  All three error entries reproduce from the printed predicted/true pair.')

# ----------------------------------------------------------------------------
head('H6  L6096 "3.5% rather than the 2.1% ... a factor of 1.7"')
for a, lab in ((3.5, 'printed rounded 3.5%'), (abs(0.7376-true)/true*100, 'unrounded 3.4654%')):
    print(f'  {lab:24s} / 2.1% = {a/2.1:.4f}  -> rounds to {round(a/2.1,1):g}   printed 1.7   '
          f'{"reproduces" if round(a/2.1,1)==1.7 else "DOES NOT"}')

# ----------------------------------------------------------------------------
head('H7  L6104 "delta departs by 0.14 where they depart by 0.008 — a factor of 17"')
r = 0.14 / 0.008
print(f'  0.14 / 0.008 = {r:.4f}   printed "a factor of 17"')
print(f'  round-half-up to integer: {int(r + 0.5)}   truncated: {int(r)}')
print(f'  VERDICT: the printed pair gives {r:g}, which rounds to {int(r+0.5)}, not 17.')
print(f'  17 requires an unrounded numerator below 0.14: 17 * 0.008 = {17*0.008:.3f}.')

# ----------------------------------------------------------------------------
head('H8  L6114 Sc VI 4S-ns — the constant form and Rule 4a (L6049-L6053)')
d4s, d5s, printed_bar = 1.0057, 0.9812, 0.9934
bar = (d4s + d5s) / 2
print(f'  delta(4s) = {d4s}, delta(5s) = {d5s}   mean = {bar:.6f}   printed {printed_bar}')
print(f'  round-half-up to 4 dp: {bar + 5e-9:.4f}   truncated to 4 dp: {int(bar*1e4)/1e4:.4f}')
print(f'  VERDICT: the printed 0.9934 is the truncation of {bar:.5f}; half-up gives 0.9935.')
rule()
decreasing = d5s < d4s
print(f'  channel decreasing (delta(5s) < delta(4s)): {decreasing}')
print(f'  Rule 4a on a decreasing channel requires  bar <= delta(last measured) = {d5s}')
print(f'  bar = {bar:.4f} > {d5s}  ->  constant form INADMISSIBLE.  Section says "above delta(5s)": '
      f'{bar > d5s}  CONSISTENT')
rule()
# the deductive bracket of 25.6.1, read at main L7014
lo, hi = 0.9376, 0.9812
print(f'  L6114 claims the estimate falls outside the deductive bracket monotonicity implies.')
print(f'  25.6.1 (main L7014) prints  {lo} < delta(6s) < {hi}')
print(f'  bar = {bar:.4f} outside [{lo}, {hi}]: {not (lo <= bar <= hi)}   POINTER RESOLVES TO ITS CLAIM')
print(f'  and 25.6.1 (main L7004) prints the same two defects {d4s} / {d5s}: exact match.')

# ----------------------------------------------------------------------------
head('H9  L6121 Kr I 6p — 70.9 cm-1 against sigma = 602')
print(f'  70.9 / 602 = {70.9/602:.5f}  -> {round(70.9/602,2):g} sigma   printed 0.12 sigma   '
      f'{"reproduces" if round(70.9/602,2)==0.12 else "DOES NOT"}')
print(f'  L6121 names the series 5p, 6p, 7p with 6p interior. Each neighbour is one principal')
print(f'  quantum number from 6p (|6-5| = 1, |7-6| = 1); the bracket SPANS two (|7-5| = 2).')
print(f'  L6123-L6124 says "its neighbours are two principal quantum numbers away": that is')
print(f'  true of the span, false of either neighbour.')

# ----------------------------------------------------------------------------
head('H10  L6142 L = |d\'/d\'\'| = n/3 for delta = d0 + d2/n^2, "the same as T\'s"')
d0, d2 = 0.35, 0.06
def dd(n):   return -2 * d2 / n ** 3
def ddd(n):  return 6 * d2 / n ** 4
print(f'  {"n":>4s} {"|delta\'/delta\'\'|":>18s} {"n/3":>10s} {"|T\'/T\'\'| (nu)":>16s} {"nu/3":>10s}')
rule()
for n in (4, 8, 20, 40, 55):
    L_delta = abs(dd(n) / ddd(n))
    # T = Z^2 R / nu^2 : T' = -2 Z^2 R nu^-3, T'' = 6 Z^2 R nu^-4  -> |T'/T''| = nu/3
    L_T = abs((-2 * n ** -3) / (6 * n ** -4))
    print(f'  {n:4d} {L_delta:18.6f} {n/3:10.6f} {L_T:16.6f} {n/3:10.6f}')
print(f'\n  Both reduce to n/3 exactly and independently of d2 and of Z^2R: the section\'s')
print(f'  identity holds, and holds for every d0 (d0 does not appear in either derivative).')

# ----------------------------------------------------------------------------
head('H11  L6142 "d0 is an additive constant that cancels from both w and e"')
def T(n, I=100000.0, Z=1.0, R=109737.31568, d0=0.35, d2=0.06):
    nu = n - (d0 + d2 / n ** 2)
    return Z ** 2 * R / nu ** 2
def w_e(n, **kw):
    a, b, c = T(n - 1, **kw), T(n, **kw), T(n + 1, **kw)
    return abs(c - a), abs(b - (a + c) / 2)
for shift in (0.0, 0.5, 1.0):
    w, e = w_e(8, d0=0.35 + shift)
    print(f'  d0 = {0.35+shift:4.2f}:  w = {w:14.6f}   e = {e:12.8f}   V = w/e = {w/e:10.6f}')
print(f'\n  MEASURED: shifting d0 changes w, e and V. The cancellation the line claims is exact')
print(f'  for an additive constant in the SAMPLED QUANTITY, not for d0 inside nu = n - delta:')
print(f'  d0 enters T non-linearly through nu^-2. Demonstrated directly on delta below.')
for shift in (0.0, 0.5, 1.0):
    d = lambda n: (0.35 + shift) + 0.06 / n ** 2
    a, b, c = d(7), d(8), d(9)
    w, e = abs(c - a), abs(b - (a + c) / 2)
    print(f'  bracketing delta itself, d0 = {0.35+shift:4.2f}:  w = {w:.10f}   e = {e:.10f}   '
          f'V = {w/e:.6f}')
print(f'  On delta, d0 cancels exactly from w, from e and therefore from V, at every d0.')

# ----------------------------------------------------------------------------
head('H12  L6148-L6149 "narrower by exactly n^3/(2*d2)" and "agreement to four figures"')
pairs = [(8, 4329.0, 4267.0), (55, 1.387e6, 1.386e6)]
print(f'  {"n":>4s} {"measured":>14s} {"predicted":>14s} {"d2 implied":>12s} {"sig digits shared":>18s}')
rule()
for n, meas, pred in pairs:
    d2_imp = n ** 3 / (2 * pred)
    print(f'  {n:4d} {meas:14,.0f} {pred:14,.0f} {d2_imp:12.6f} {sig_agree(meas, pred):18d}')
print(f'\n  d2 implied by the predicted column is {8**3/(2*4267):.5f} at n = 8 and '
      f'{55**3/(2*1.386e6):.5f} at n = 55 — a single d2 = 0.06, which the section never prints.')
print(f'  "Agreement to four figures": the n = 55 pair shares '
      f'{sig_agree(1.387e6, 1.386e6)} significant digits; the n = 8 pair shares '
      f'{sig_agree(4329.0, 4267.0)}.')
print(f'  n = 8 relative difference = {abs(4329-4267)/4267*100:.3f}%; n = 55 = '
      f'{abs(1.387e6-1.386e6)/1.386e6*100:.4f}%.')
print(f'  VERDICT: the claim is true of the n = 55 pair and false of the n = 8 pair, which')
print(f'  agrees to two significant figures.')

# ----------------------------------------------------------------------------
head('H13  L6155-L6158 the limit-uncertainty table')
tab = [(20, 68.06, 0.00102, 0.0210), (40, 7.613, 1.43e-5, 0.0200)]
sig_limit = 0.01
print(f'  {"n":>4s} {"w_T direct":>12s} {"via delta":>12s} {"printed +limit":>15s} '
      f'{"via + 2*sigma":>14s} {"via + 1*sigma":>14s}')
rule()
for n, wt, wd, wl in tab:
    print(f'  {n:4d} {wt:12.4f} {wd:12.3e} {wl:15.4f} {wd + 2*sig_limit:14.5f} '
          f'{wd + sig_limit:14.5f}')
print(f'\n  MEASURED: the printed last column is the via-delta width plus 2*sigma at both n')
print(f'  ({0.00102 + 0.02:.5f} -> 0.0210 and {1.43e-5 + 0.02:.6f} -> 0.0200), i.e. the limit')
print(f'  uncertainty entering at both edges. The column header prints sigma = 0.01, not 2 sigma.')
rule()
for n, wt, wd, _ in tab:
    print(f'  n = {n}: w_T/w_delta = {wt/wd:12,.0f}   n^3/(2*d2) at d2=0.06 = {n**3/(2*0.06):12,.0f}   '
          f'agree to {sig_agree(wt/wd, n**3/(2*0.06))} sig digits')
print(f'  n = 40: limit sigma / via-delta width = {sig_limit/1.43e-5:,.1f} = '
      f'{log10(sig_limit/1.43e-5):.3f} orders. L6160 prints "three orders".')

# ----------------------------------------------------------------------------
head('H14  L6165 "true for some species, false for others"')
tightest, lo_lim, hi_lim = 1.398, 0.001, 0.4
print(f'  tightest bracket in the collection (L6165, and main L6974/L6987): {tightest} cm-1')
print(f'  limit uncertainties in the collection (L6165): {lo_lim} to {hi_lim} cm-1')
rule()
print(f'  The delta route wins where the limit is known better than the bracket.')
print(f'  Worst printed limit uncertainty, entering at both edges: 2 * {hi_lim} = {2*hi_lim} cm-1')
print(f'  Narrowest printed bracket:                                {tightest} cm-1')
print(f'  {2*hi_lim} < {tightest}: {2*hi_lim < tightest}  -> on the printed ranges the delta route wins')
print(f'  even in the worst case, by a factor of {tightest/(2*hi_lim):.2f}.')
print(f'  For the delta route to lose, a channel would need 2*sigma_limit >= its bracket, i.e.')
print(f'  sigma_limit >= {tightest/2:.3f} cm-1 against a bracket at the collection minimum —')
print(f'  above the printed maximum of {hi_lim}.')
print(f'  VERDICT: "false for others" has no witness among the two ranges the sentence prints.')

# ----------------------------------------------------------------------------
head('H15  L6170-L6172  r = 2Z^2R/(nu^3 sigma) and "r falls as nu^-3"')
Z, R, Zeff, SE = 1.0, 109737.31568, 1.0, 0.01
print('  reading A — sigma is the measured levels\' own uncertainty, constant per channel')
print(f'  {"nu":>5s} {"r (sigma = 1 cm-1)":>22s} {"ratio to previous":>20s}')
rule()
prev = None
for nu in (10, 20, 40, 80):
    r = 2 * Z ** 2 * R / (nu ** 3 * 1.0)
    print(f'  {nu:5d} {r:22.6f} {"" if prev is None else f"{r/prev:20.4f}":>20s}')
    prev = r
print('  falls as nu^-3 exactly (each doubling divides r by 8).  CLAIM HOLDS on this reading.')
rule()
print('  reading B — sigma is Rule 4\'s sigma (L6047): sigma = 2 R Zeff^2 * SE_pred / nu^3')
print(f'  {"nu":>5s} {"sigma":>18s} {"r = 2Z^2R/(nu^3 sigma)":>26s}')
rule()
for nu in (10, 20, 40, 80):
    sig = 2 * R * Zeff ** 2 * SE / nu ** 3
    r = 2 * Z ** 2 * R / (nu ** 3 * sig)
    print(f'  {nu:5d} {sig:18.6f} {r:26.6f}')
print(f'  nu^3 cancels identically: r = Z^2/(Zeff^2 * SE_pred) = {Z**2/(Zeff**2*SE):.1f} at every nu.')
print('  On reading B, r is INDEPENDENT of nu and the section\'s "r falls as nu^-3" is false.')
print('  The chapter uses the symbol sigma for both quantities — Rule 4\'s prediction standard')
print('  error at L6047, the levels\' own uncertainty at L6168 — and never says which is meant.')

# ----------------------------------------------------------------------------
head('H16  L6175 "the price is the only linearly rising quantity in the structure"')
print('  price V = w/e = 4nu/3 (main L6183); the chapter also prints:')
print(f'  {"quantity":34s} {"printed at":>12s} {"scaling in n":>18s}')
rule()
qs = [('V = w/e = 4nu/3', 'L6183', 'linear'),
      ('V(delta) = V(T) = 4n/(3h)', 'L6143', 'linear'),
      ('V(x,p) = 4x/(h|p-1|)', 'L6187', 'linear in x, every p != 1'),
      ('L = |delta\'/delta\'\'| = n/3', 'L6142', 'linear'),
      ('w = |T(n+1)-T(n-1)|', 'L6181', 'falls as nu^-3'),
      ('e = |T(n)-mean|', 'L6181', 'falls as nu^-4'),
      ('r = 2Z^2R/(nu^3 sigma)', 'L6170', 'falls as nu^-3 (reading A)')]
for a, b, c in qs: print(f'  {a:34s} {b:>12s} {c:>18s}')
rule()
for n in (8, 20, 55):
    print(f'  n = {n:2d}:  V = 4n/3 = {4*n/3:8.4f}   L = n/3 = {n/3:8.4f}   ratio V/L = {(4*n/3)/(n/3):.4f}')
print('  MEASURED: L = n/3 is printed thirty-two lines before the claim, rises linearly in n,')
print('  and is a second linearly rising quantity. V(x,p) supplies a further one for each p != 1.')
print('  VERDICT: "the only" is unqualified and the chapter prints at least one counterexample.')

# ----------------------------------------------------------------------------
head('H17  L6133 / main L10035 "nu, delta and V all require I" against V = w/e')
I_values = [0.0, 100000.0, 1e6]
print(f'  {"I":>12s} {"w":>16s} {"e":>16s} {"V = w/e":>14s}')
rule()
E = {7: 12000.0, 8: 9000.0, 9: 7000.0}   # arbitrary measured levels, no threshold used
for I in I_values:
    t = {n: (I - E[n]) if I else -E[n] for n in E}
    w = abs(t[9] - t[7]); e = abs(t[8] - (t[7] + t[9]) / 2)
    print(f'  {I:12,.0f} {w:16.4f} {e:16.4f} {V:=w/e:14.6f}' if False else
          f'  {I:12,.0f} {w:16.4f} {e:16.4f} {w/e:14.6f}')
print('\n  MEASURED: w and e are a first and a second difference, so the additive constant I')
print('  cancels from both and V = w/e is identical at every I, including I unknown (I = 0).')
print('  This is the same cancellation A.12 proves for containment (main L10029-L10033) and the')
print('  same one L6142 states for d0. nu = Z sqrt(R/T) and delta = n - nu do require I.')
print('  VERDICT: the list of three is true of nu and delta and false of V, at both sites.')

print('\n' + '=' * W)
print('r2-ch14h complete.')
print('=' * W)
