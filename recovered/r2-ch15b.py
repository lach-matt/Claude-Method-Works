#!/usr/bin/env python3
"""r2-ch15b — computable claims of Chapter 26 (main L7117-L7202, 'Collective sections').

Chat 104.  Reads members only.  Resolvers imported from r2lib by path; the LINE LIST is passed,
never the member text.  round() is never used: every printed figure is matched with
Decimal.quantize under BOTH ROUND_HALF_EVEN and ROUND_HALF_UP, and the convention is named.

Rewritten twice before banking.  The faults, all self-caught:
  1. sigma_2 was estimated by Frobenius deflation, which returned 7.6e-06 - my own arithmetic
     error, not a property of the matrix.  Now measured with numpy's SVD in double precision.
  2. the sigma_1 base sweep only tested bases; it now inverts to the norm the missing input
     must have, which is what names the absent quantity.
  3. one rounding convention only.  Both are swept and named.
  4. the Aitken column was computed in float and differed from print in the last place at n=10;
     it is now computed in 50-digit Decimal, which decides that last place.
  5. B3 swept exponent sets and nu grids but held the LOG BASE fixed at e.  A log-base choice
     rescales sigma_1 by ln(10) and is exactly the kind of unstated convention this chapter's
     other claims turn on, so it is swept too.
"""
import importlib.util
from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP, getcontext
import numpy as np
from math import log, log10

getcontext().prec = 50
H = '/home/claude/members/'
spec = importlib.util.spec_from_file_location('r2lib', H + 'r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)

MAIN = r2lib.read_member('The_Method_1_6-2.md').split('\n')
A, B = 7117, 7202                       # MEASURED heading scan, chat 104
R_BOOK = Decimal('109737.31568')        # the constant gate.py's r2-tools-constants holds
R_TRUNC = Decimal('109737.30')

def qe(x, places): return Decimal(x).quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_EVEN)
def qu(x, places): return Decimal(x).quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP)
def head(s): print('\n== ' + s)
def row(k, got, want, ok): print(f'   {k:<44} got {got:<20} want {want:<13} {"OK" if ok else "DEVIATION"}')

print('r2-ch15b  Chapter 26, main L%d-L%d' % (A, B))
print('span check:', r2lib.section_span(MAIN, '26'), '| heading:', MAIN[A-1].strip())

# ---------------------------------------------------------------- B1 assembly rule p = 2a+3b
head('B1  the assembly rule table (L7126-L7132): p = 2a + 3b')
for name, a, b, p in [('<r>', 1, 0, 2), ('cross-section/C3/quadrupole/diamagnetic', 2, 0, 4),
                      ('polarisability alpha', 2, 1, 7), ('C6', 4, 1, 11), ('C8', 6, 1, 15)]:
    row(name, 2*a + 3*b, p, 2*a + 3*b == p)
print('   observables named in the table:', 1+4+1+1+1,
      '| the section claims fifteen quantities at L7138 and L7142')

# ---------------------------------------------------------------- B2 C6 = (nu^2)^4 / nu^-3
head('B2  L7150: C6 = nu^11 is (nu^2)^4 / nu^-3')
row('exponent of (nu^2)^4 / nu^-3', 2*4 - (-3), 11, 2*4 - (-3) == 11)

# ---------------------------------------------------------------- B3 the centred log-matrix
head('B3  L7138-L7147: sigma_1 = 9.49e1, sigma_2 = 1.8e-14, rank(log q) = 1')
print('   ALGEBRA: log q_i = p_i log nu + const.  Row-centring kills the const, leaving the outer')
print('   product p (x) v exactly, so rank is 1 and sigma_2 = 0 for ANY exponent set and ANY grid.')
print('   The printed 1.8e-14 is a double-precision zero: reproducible in kind, carrying no')
print('   information about the inputs.  sigma_1 is the only figure here that constrains them.')

def svd2(exps, nus, centre, lg):
    M = np.array([[e*lg(n) for n in nus] for e in exps], dtype=float)
    M = M - (M.mean(axis=1, keepdims=True) if centre == 'rows' else M.mean(axis=0, keepdims=True))
    s = np.linalg.svd(M, compute_uv=False)
    return s[0], s[1]

GRIDS = {'nu = 1..40': [float(i) for i in range(1, 41)],
         'nu = 10..49': [float(i) for i in range(10, 50)],
         'nu = 30..69': [float(i) for i in range(30, 70)],
         'nu = 35..100, 40 steps': [35 + i*(65/39) for i in range(40)],
         'nu = 10..100, 40 steps': [10 + i*(90/39) for i in range(40)],
         'nu = 61..100': [float(i) for i in range(61, 101)]}
EXPS = {'p = 1..15': list(range(1, 16)),
        'p = 2..16': list(range(2, 17)),
        'p = 3..17': list(range(3, 18)),
        'p = the five printed, padded to 15': [2,4,4,4,4,7,11,15,2,4,7,11,15,2,4],
        'p = 2,4,7,11,15 repeated x3': [2,4,7,11,15]*3}
LOGS = {'ln': log, 'log10': log10}
best = []
for el, exps in EXPS.items():
    for gl, nus in GRIDS.items():
        for c in ('rows', 'cols'):
            for ll, lg in LOGS.items():
                s1, s2 = svd2(exps, nus, c, lg)
                best.append((el, gl, c, ll, s1, s2))
hit = [b for b in best if f'{b[4]:.3g}' == '94.9']
print(f'   bases swept: {len(best)} (5 exponent sets x 6 grids x 2 centrings x 2 log bases)')
print(f'   reproducing sigma_1 = 9.49e1 at 3 s.f.: {len(hit)}')
for b in hit: print('     ', ' | '.join(map(str, b[:4])), 'sigma_1 =', f'{b[4]:.6g}')
nearest = min(best, key=lambda b: abs(b[4] - 94.9))
print('   nearest base: %s | %s | %s | %s -> sigma_1 = %.4f' % (nearest[0], nearest[1], nearest[2],
                                                               nearest[3], nearest[4]))
print('   sigma_1 over the sweep: %.4g .. %.4g' % (min(b[4] for b in best), max(b[4] for b in best)))
print('   sigma_2 over the sweep (true SVD): %.3g .. %.3g   printed 1.8e-14'
      % (min(b[5] for b in best), max(b[5] for b in best)))
print('\n   INVERTED - row-centred, sigma_1 = ||p|| * ||v||, so fifteen exponents on the named grid')
print('   must carry the norm below.  ||p|| for 1..15 is %.4f, for 2..16 %.4f, for 3..17 %.4f:'
      % tuple(float(np.linalg.norm(np.arange(a_, a_+15))) for a_ in (1, 2, 3)))
for gl, nus in GRIDS.items():
    for ll, lg in LOGS.items():
        v = np.array([lg(n) for n in nus]); v = v - v.mean()
        print(f'     {gl:<24} {ll:<6} ||v|| = {float(np.linalg.norm(v)):8.4f}'
              f'   required ||p|| = {94.9/float(np.linalg.norm(v)):9.4f}')

# ---------------------------------------------------------------- B4 error amplification
head('B4  L7154: fractional error eps in nu gives k*eps at exponent k')
for k in (2, 11, 15):
    e = 0.01; exact = (1+e)**k - 1
    row(f'k = {k}: exact vs first-order k*eps', f'{exact:.6f}', f'{k*e:.6f}',
        abs(exact - k*e) < k*k*e*e)

# ---------------------------------------------------------------- B6 Singer p_eff
head('B6  L7163-L7168: Singer et al. (2005) Rb ns-ns, p_eff at n = 35 and n = 100')
def p_eff(n, c0, c1, c2): return 11 + n*(c1 + 2*c2*n)/(c0 + c1*n + c2*n*n)
c0, c1, c2 = 11.97, -0.8486, 3.385e-3          # Singer et al. 2005, Rb ns-ns
print('   c0, c1, c2 are NOT printed in the section; tested at the published values')
print('   c0 = 11.97, c1 = -0.8486, c2 = 3.385e-3:')
for n, want in ((35, '12.58'), (100, '11.44')):
    v = p_eff(n, c0, c1, c2); ge, gu = str(qe(v, 2)), str(qu(v, 2))
    row(f'p_eff({n})  [HALF_EVEN | HALF_UP]', f'{ge} | {gu}', want, want in (ge, gu))
pts = [35 + i*(65/8) for i in range(9)]
vals = [p_eff(n, c0, c1, c2) for n in pts]
print('   nine evenly spaced points 35..100:', ', '.join(f'{v:.3f}' for v in vals))
print('   monotone falling:', all(vals[i] > vals[i+1] for i in range(8)),
      f'| range {max(vals):.3f} to {min(vals):.3f}')

head('B5  L7156: "measuring C6 to 1% fixes nu to about 0.0<TRUNCATED>" - recovering the figure')
v = 1.0/p_eff(100, c0, c1, c2)
print(f'   1/p_eff(100) = {v:.6f}; 1% in C6 fixes nu to {v:.4f}%')
print(f'   printed prefix is "0.0", so the lost figure is {qe(v,2)}% (2 dp) or {qe(v,3)}% (3 dp).')
print('   The clause "roughly nine times sharper than the three-level bracket achieves" then')
print(f'   prices the three-level bracket at about {9*v:.3f}% - a figure the section never prints.')

# ---------------------------------------------------------------- B8 the Aitken table
head('B8  L7176-L7181: the Aitken table, in 50-digit Decimal')
PRINTED = {10: ('1097.3730', '365.1793', '365.7910'),
           20: ('274.3433', '91.4096', '91.4477'),
           40: ('68.5858', '22.8596', '22.8619'),
           80: ('17.1465', '5.7153', '5.7155')}
for lab, Rv in (("R = 109737.31568 (the book's)", R_BOOK), ('R = 109737.30', R_TRUNC)):
    print('  ', lab)
    for n, (t, a, t3) in PRINTED.items():
        pl = len(t.split('.')[1]); x = Rv/Decimal(n*n)
        ge, gu = str(qe(x, pl)), str(qu(x, pl))
        row(f'T({n})  [HALF_EVEN | HALF_UP]', f'{ge} | {gu}', t, t in (ge, gu))

print('\n   T/3 column, computed from the PRINTED T, and from exact R/(3n^2):')
for n, (t, a, t3) in PRINTED.items():
    pl = len(t3.split('.')[1])
    x = Decimal(t)/3; ge, gu = str(qe(x, pl)), str(qu(x, pl))
    y = R_TRUNC/Decimal(3*n*n); he, hu = str(qe(y, pl)), str(qu(y, pl))
    trunc = str(x.quantize(Decimal(1).scaleb(-pl), rounding='ROUND_DOWN'))
    row(f'printed T({n})/3 [EVEN|UP|TRUNC]', f'{ge} | {gu} | {trunc}', t3,
        t3 in (ge, gu)) 
    if t3 not in (ge, gu):
        print(f'      exact R/(3n^2) at R=109737.30 gives {he} | {hu}; truncation gives {trunc}')

def aitken(x0, x1, x2):
    d1 = x1 - x0; d2 = x2 - 2*x1 + x0
    return x0 - d1*d1/d2

print('\n   Aitken column, every window, on T(m) = R/m^2 in Decimal, at both constants:')
WIN = {'(n, n+1, n+2)': lambda n: (n, n+1, n+2),
       '(n-1, n, n+1)': lambda n: (n-1, n, n+1),
       '(n-2, n-1, n)': lambda n: (n-2, n-1, n),
       '(n, n+2, n+4)': lambda n: (n, n+2, n+4)}
for lab, Rv in (('R = 109737.31568', R_BOOK), ('R = 109737.30', R_TRUNC)):
    print('  ', lab)
    for wl, f in WIN.items():
        outs, ok = [], 0
        for n, (t, a, t3) in PRINTED.items():
            m0, m1, m2 = f(n)
            x = aitken(Rv/Decimal(m0*m0), Rv/Decimal(m1*m1), Rv/Decimal(m2*m2))
            pl = len(a.split('.')[1]); ge, gu = str(qe(x, pl)), str(qu(x, pl))
            good = a in (ge, gu); ok += good
            outs.append(f'n={n}: {ge} vs {a}{"" if good else " <-"}')
        print(f'     {wl}  {ok}/4  ' + ' | '.join(outs))

print('\n   ratio (printed Aitken)/(printed T) against 1/3:')
for n, (t, a, t3) in PRINTED.items():
    r_ = Decimal(a)/Decimal(t)
    print(f'     n={n:>3}: {qe(r_,6)}   deficit from 1/3 = {qe(Decimal(1)/3 - r_, 8)}')
print('   the deficit falls as ~1/n^2: the column converges to T/3 from below, so L7183 is exact')
print('   as a limit and approximate at every tabulated n - which is what L7185 states.')

# ---------------------------------------------------------------- B9 T'^2/T'' = (2/3)T
head("B9  L7185: (dT)^2/d2T -> T'^2/T'' = (2/3)T on T = R/nu^2")
Rf = float(R_BOOK)
for nu in (10.0, 20.0, 40.0, 80.0):
    T = Rf/nu**2; T1 = -2*Rf/nu**3; T2 = 6*Rf/nu**4; v2 = T1*T1/T2
    row(f"T'^2/T'' at nu={nu:.0f}", f'{v2:.6f}', f'{2*T/3:.6f}', abs(v2 - 2*T/3) < 1e-9*T)
print('   residue T - (2/3)T = T/3 exactly.')

# ---------------------------------------------------------------- B10 the cm-1 errors
head('B10  L7187: "a 91 cm-1 error at n = 20 and 23 cm-1 at n = 40"')
for n, want in ((20, '91'), (40, '23')):
    t, a, t3 = PRINTED[n]
    row(f'T({n})/3 to the unit', str(qe(Decimal(t3), 0)), want, str(qe(Decimal(t3), 0)) == want)
    row(f'Aitken({n}) to the unit', str(qe(Decimal(a), 0)), want, str(qe(Decimal(a), 0)) == want)

# ---------------------------------------------------------------- B12 "Bracket 66 of 66"
head('B12  L7170: "Bracket 66 of 66" - what population has 66 members?')
c = [f'C({k},2)' for k in range(2, 40) if k*(k-1)//2 == 66]
c += [f'triangular({k})' for k in range(2, 60) if k*(k+1)//2 == 66]
print('   66 =', ', '.join(c), '| factor pairs:',
      ', '.join(f'{a_}x{66//a_}' for a_ in range(2, 67) if 66 % a_ == 0))
print('   nine points are stated twice (L7168, L7170); C(9,2) = 36 and 9x9 = 81, neither is 66.')
print('   no population of 66 is printed anywhere in L7117-L7202.')

# ---------------------------------------------------------------- B13 the cost law's errors
head('B13  L7170: "median error 1.05%, maximum 1.83%" across nine points')
print('   The cost law is not printed in the section.  Read as a power law A*n^p fitted to')
print('   Singer C6 = n^11(c0+c1n+c2n^2), the residual sits in the quadratic factor alone.')
n_ = np.array(pts); Q = c0 + c1*n_ + c2*n_**2
logC = 11*np.log(n_) + np.log(np.abs(Q))
for lab, deg in (('p free (2-parameter log fit)', 1), ('p fixed at 11 (prefactor only)', 0)):
    if deg == 1:
        cf = np.polyfit(np.log(n_), logC, 1); pred = np.polyval(cf, np.log(n_)); ps = cf[0]
    else:
        k = (logC - 11*np.log(n_)).mean(); pred = 11*np.log(n_) + k; ps = 11.0
    err = np.abs(np.exp(pred) - np.exp(logC))/np.exp(logC)*100
    print(f'     {lab:<32} exponent {ps:7.4f}  median {np.median(err):6.3f}%  max {err.max():6.3f}%')
print('   printed: median 1.05%, maximum 1.83%.  Neither fit reproduces the pair, so the claim')
print('   consumes a law and an input set the section does not print.')

print('\nr2-ch15b complete')
