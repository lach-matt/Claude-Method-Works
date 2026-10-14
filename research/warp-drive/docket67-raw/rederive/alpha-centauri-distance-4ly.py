"""DOCKET 67 re-derivation: alpha-centauri-distance-4ly.

What phase1.py does with L = 4.0 ly, and how each dependent figure moves with L.
Reads phase1.py by import (read-only; bytecode writing disabled so nothing lands in the tree).
Distances other than 4.0 ly enter ONLY as candidate inputs, each labelled with its provenance
status; none was READ at source in this stage (see audit JSON).
"""
import sys, math
sys.dont_write_bytecode = True
sys.path.insert(0, '/home/user/Claude-Method-Works/research/warp-drive')
import phase1 as P
import sympy as sp

ok = True
def chk(name, cond):
    global ok
    ok &= bool(cond)
    print(('PASS ' if cond else 'FAIL ') + name)

# ---- R1: symbolic.  Theorem 4 ratio is independent of L; price is linear in L.
L, c, G, Lam, f, N = sp.symbols('L c G Lambda f N', positive=True)
t_est = L / (2 * c)
ratio = sp.simplify((t_est + L / c) / (L / c))
chk('R1a Theorem-4 ratio (L/2c + L/c)/(L/c) = 3/2, free of L', ratio == sp.Rational(3, 2) and L not in ratio.free_symbols)
chk('R1b beats-light test is L-independent: sign(1.5 L/c - L/c) = + for all L>0', sp.simplify((t_est + L/c) - L/c) == L/(2*c))
M = f * L * c**2 / (G * Lam)
chk('R1c price M(f L) = f L c^2/(G Lambda) is linear in L (d2M/dL2 = 0)', sp.diff(M, L, 2) == 0)
chk('R1d amortised establishment L/(2Nc) -> 0 as N -> oo for any L', sp.limit(t_est / N, N, sp.oo) == 0)

# ---- R2: reproduce phase1's own numbers at L = 4.0 ly.
ly = P.LIGHT_YEAR
L4 = 4.0 * ly
m1 = P.mass_for_contraction(0.01 * L4) / P.SOLAR_MASS
m50 = P.mass_for_contraction(0.50 * L4) / P.SOLAR_MASS
print('Lambda = %.6f   exchange = %.5e kg/m' % (P.lam(), P.exchange_rate()))
print('4.0 ly: 1%% -> %.5e Msun, 50%% -> %.5e Msun, establishment %.5e s = %.4f yr'
      % (m1, m50, P.establishment_time(L4), P.establishment_time(L4) / 3.15576e7))
chk('R2a 1% of 4.0 ly = 2.5667e10 Msun (phase1.py:508) to 1e-3', abs(m1 / 2.5667e10 - 1) < 1e-3)
chk('R2b 50% of 4.0 ly = 1.2833e12 Msun (phase1.py:510) to 1e-3', abs(m50 / 1.2833e12 - 1) < 1e-3)
chk('R2c report "2.6e10" (phase1.py:552) is 2.5667e10 rounded to 2 s.f.', round(m1, -9) == 2.6e10)
chk('R2d penalty ratio 1.5 at 4.0 ly', abs(P.single_transition_penalty() - 1.5) < 1e-12)
for Lt in (1.0, 4.2465 * ly, 4.37 * ly, 1e25):
    chk('R2e beats_light False and penalty 1.5 at L = %.4g m' % Lt,
        P.single_transition_beats_light(Lt) is False and abs(P.single_transition_penalty(Lt) - 1.5) < 1e-12)

# ---- R3: the light-year constant.  IAU: 1 ly = c * 365.25 d * 86400 s (Julian year), exact given c.
ly_exact = 299792458 * 365.25 * 86400
print('ly used %.6e m ; Julian-year ly %.10e m ; rel diff %.3e' % (ly, ly_exact, ly / ly_exact - 1))
chk('R3 phase1 LIGHT_YEAR = 9.4607e15 agrees with c*Julian year to < 4e-6 (truncation, not an error)',
    abs(ly / ly_exact - 1) < 4e-6)

# ---- R4: parsec from parallax.  1 pc = 648000/pi au, au = 149597870700 m (IAU 2012 B2, exact).
au = 149597870700.0
pc = 648000 / math.pi * au
def ly_from_mas(p_mas):
    return (1000.0 / p_mas) * pc / ly_exact
# Candidate inputs. Status: NONE READ AT SOURCE in this stage -- search-engine snippet only.
cands = [
    ('phase1 as written', 4.0, 'phase1.py:329'),
    ('tree own Proxima constant', 4.2465, 'nonstatic.py:257 "Gaia DR3 parallax distance"; oneway.py:63; closeout.py:71'),
    ('Proxima, Gaia DR3 parallax 768.0665 mas (SNIPPET, not read)', ly_from_mas(768.0665), 'web-search snippet only'),
    ('alpha Cen AB, 747.17 mas Kervella+2016 (SNIPPET, not read)', ly_from_mas(747.17), 'web-search snippet only'),
    ('canonical entry "about 4.37 ly" (AB)', 4.37, 'canonical.json hypothesis text'),
]
print('\n%-62s %9s %12s %12s %9s' % ('input', 'L (ly)', '1% (Msun)', '50% (Msun)', 'vs 4.0'))
base = m1
for name, Lly, src in cands:
    mm = P.mass_for_contraction(0.01 * Lly * ly) / P.SOLAR_MASS
    mm50 = P.mass_for_contraction(0.50 * Lly * ly) / P.SOLAR_MASS
    print('%-62s %9.4f %12.4e %12.4e %+8.2f%%' % (name, Lly, mm, mm50, 100 * (mm / base - 1)))
chk('R4a 768.0665 mas -> 4.2465 ly (the tree\'s own constant is the parallax distance to 4 d.p.)',
    abs(ly_from_mas(768.0665) - 4.2465) < 5e-5)
chk('R4b 747.17 mas -> 4.365 ly (consistent with "about 4.37")', abs(ly_from_mas(747.17) - 4.365) < 1e-3)

# ---- R5: does any candidate move a conclusion?
#  phase1's conclusions: (i) "a galaxy of negative mass" (order 1e10 Msun) for 1 %;
#  (ii) Theorem 4 ratio 1.5.  (i) moves by the factor L/4.0 ly; (ii) not at all.
lo, hi = 4.0, 4.37
chk('R5a order of magnitude of the 1% price is 1e10 Msun for every L in [4.0, 4.37] ly',
    all(int(math.floor(math.log10(P.mass_for_contraction(0.01 * x * ly) / P.SOLAR_MASS))) == 10 for x in (lo, 4.2465, hi)))
print('R5b max shift of printed price over candidates: %.2f%% (factor 4.37/4.0 = %.4f)' % (100 * (hi / lo - 1), hi / lo))
m_prox = P.mass_for_contraction(0.01 * 4.2465 * ly) / P.SOLAR_MASS
print('R5c Proxima (tree constant) 1%% price %.4e Msun -> printed 2 s.f. would read %.1e, not 2.6e10' % (m_prox, round(m_prox, -9)))
chk('R5d two-s.f. printed figure changes (2.6e10 -> 2.7e10 Proxima, 2.8e10 AB): a DISCREPANCY in the digits, not in the conclusion',
    round(m_prox, -9) == 2.7e10 and round(P.mass_for_contraction(0.01 * 4.365 * ly) / P.SOLAR_MASS, -9) == 2.8e10)
# Establishment time printed "2.0 years" at 4 ly; at Proxima L/2c = 2.12 yr.
print('R5e establishment L/2c: 4.0 ly -> %.4f yr ; 4.2465 ly -> %.4f yr ; 4.365 ly -> %.4f yr'
      % tuple(P.establishment_time(x * ly) / 3.15576e7 for x in (4.0, 4.2465, 4.365)))
print('\nALL PASS' if ok else '\nSOME FAIL')
sys.exit(0 if ok else 1)
