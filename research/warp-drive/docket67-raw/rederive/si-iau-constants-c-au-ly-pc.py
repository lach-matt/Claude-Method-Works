#!/usr/bin/env python3
"""DOCKET 67 -- si-iau-constants-c-au-ly-pc.  Re-derivation of arrival.py:21-24.

Checks, in exact (sympy rational / symbolic pi) arithmetic:
 R1  c literal == SI defined value 299 792 458 m/s (CODATA 2022 Table XXXII, p.50)
 R2  AU literal == IAU 2012 B2 value 149 597 870 700 m (restated 1605.09788 p.8, p.13; 1510.07674 endnote 4)
 R3  LY literal vs c x Julian year (365.25 x 86400 s)  [Julian-year def NAMED-NOT-READ]
 R4  PC literal vs 648000/pi au (IAU 2015 B2 note, restated 1605.09788 p.8, p.13), and the
     identity au/radians(1 arcsec) == 648000/pi au (astropy iau2015.py form)
 R5  PC is referenced nowhere after its definition in arrival.py (hypothesis 'unused')
 R6  propagation: effect of the literal offsets on every printed AU/ly output
 R7  alternative-year sensitivity (Gregorian / tropical year ly) on the printed outputs
 R8  the prose figures '810 AU' and '2.6 ly' (arrival.py:151-152,159) vs the code's own output,
     and the AU / LY values that WOULD reconcile them (to show the constants cannot)
"""
import sys, re, math
import sympy as sp

OWNER = "/home/user/Claude-Method-Works/research/warp-drive/arrival.py"
src = open(OWNER).read().splitlines()
lit = {}
for i, L in enumerate(src[:40], 1):
    m = re.match(r"^(c|AU|LY|PC)\s*=\s*([0-9.eE+-]+)", L)
    if m: lit[m.group(1)] = (i, m.group(2))
print("literals read from owner:", lit)
fails = 0
def chk(name, cond, detail=""):
    global fails
    print(("  PASS " if cond else "  FAIL ") + name + ("   " + detail if detail else ""))
    if not cond: fails += 1

R = lambda s: sp.Rational(sp.nsimplify(s, rational=True))  # decimal literal -> exact rational
c_t, au_t, ly_t, pc_t = (sp.Rational(lit[k][1]) if 'e' not in lit[k][1] else sp.Rational(sp.Float(lit[k][1], 30)) for k in ("c","AU","LY","PC"))
# decimal literal parse exactly (avoid binary float): mantissa * 10^exp
def exact(s):
    m, e = (s.lower().split('e') + ['0'])[:2]
    return sp.Rational(m) * sp.Integer(10)**int(e)
c_t, au_t, ly_t, pc_t = (exact(lit[k][1]) for k in ("c","AU","LY","PC"))

c_SI  = sp.Integer(299792458)
au_IAU = sp.Integer(149597870700)
yr_J  = sp.Rational(36525, 100) * 86400
ly_J  = c_SI * yr_J
pc_IAU = 648000 / sp.pi * au_IAU

print("\nR1 c")
chk("c literal == 299792458 exactly", c_t == c_SI, str(c_t))
chk("float(c literal) represents it exactly", sp.Rational(float(lit['c'][1])) == c_SI)
print("\nR2 au")
chk("AU literal == 149597870700 exactly", au_t == au_IAU, str(au_t))
chk("float(AU literal) represents it exactly", sp.Rational(float(lit['AU'][1])) == au_IAU)
print("\nR3 ly")
print("  c x Julian year =", ly_J, "m")
d_ly = ly_t - ly_J
chk("ly_J == 9460730472580800 exactly", ly_J == 9460730472580800)
rel_ly = d_ly / ly_J
chk("LY literal = ly_J rounded to 11 s.f. (|diff| <= half-unit 5e4 m)", abs(d_ly) <= sp.Rational(5*10**4), "diff = %s m, rel = %.3e" % (d_ly, float(rel_ly)))
chk("LY literal == round(ly_J, 11 s.f.)", exact("%.10e" % float(ly_J)) == ly_t, "%.10e" % float(ly_J))
print("\nR4 pc")
pc_N = sp.N(pc_IAU, 30)
print("  648000/pi au =", pc_N, "m")
d_pc = pc_t - pc_IAU
rel_pc = sp.N(d_pc / pc_IAU, 15)
chk("PC literal = 648000/pi au rounded to 11 s.f. (last s.f. is 1e6 m; |diff| <= 5e5 m)", abs(sp.N(d_pc, 20)) <= 5*10**5, "diff = %s m, rel = %s" % (sp.N(d_pc, 8), rel_pc))
chk("1605.09788 p.8 printed digits 3.085 677 581 491... agree", str(pc_N).replace('.', '').startswith('3085677581491'))
arcsec = sp.pi / 180 / 3600
chk("identity au / (1 arcsec in rad) == 648000/pi au (symbolic)", sp.simplify(au_IAU/arcsec - pc_IAU) == 0)
chk("pc/au is irrational (pi): not rational", not (pc_IAU/au_IAU).is_rational)
chk("PC literal == round(648000/pi au, 11 s.f.)", exact("%.10e" % float(sp.N(pc_IAU, 30))) == pc_t, "%.10e" % float(sp.N(pc_IAU, 30)))
print("\nR5 PC usage")
uses = [i for i, L in enumerate(src, 1) if re.search(r"\bPC\b", L) and i != lit['PC'][0]]
chk("PC appears on no line other than its definition", uses == [], "other lines: %s" % uses)

print("\nR6 propagation of literal offsets to printed outputs")
# owner's magsail floor: L = (gamma-1) m c^2 / (rho (b c)^2 A), rho = 1e6 * M_P
M_P = sp.Rational("1.67262192e-27")
def L(m, b, A, c=c_SI):
    b = sp.Rational(b); g = 1/sp.sqrt(1-b*b)
    return (g-1)*m*c**2 / (sp.Integer(10)**6*M_P*(b*c)**2*A)
rows = []
for A, lbl in ((10**10, "100 km"), (10**12, "1000 km"), (10**14, "10,000 km")):
    d1_t = sp.N(L(10**6, "0.0476", A)/au_t, 20); d1_x = sp.N(L(10**6, "0.0476", A)/au_IAU, 20)
    d2_t = sp.N(L(10**6, "0.866", A)/ly_t, 20);  d2_x = sp.N(L(10**6, "0.866", A)/ly_J, 20)
    rows.append((lbl, d1_t, d2_t))
    print("  %-10s AU tree %.6f exact %.6f | ly tree %.12f exact %.12f" % (lbl, d1_t, d1_x, d2_t, d2_x))
    chk("  %s printed AU (%%11.0f) unchanged" % lbl, "%11.0f" % d1_t == "%11.0f" % d1_x)
    chk("  %s printed ly (%%15.2f) unchanged" % lbl, "%15.2f" % d2_t == "%15.2f" % d2_x)
    chk("  %s ly relative shift = -rel_ly" % lbl, abs(float((d2_t-d2_x)/d2_x) + float(rel_ly)) < 1e-15)
chk("selftest pin 2001.64 AU reproduced within its tol 1e-4 (exact constants)",
    abs(float(L(10**6, "0.0476", 10**12)/au_IAU) - 2001.64) <= 1e-4*2001.64, "%.6f" % float(L(10**6, "0.0476", 10**12)/au_IAU))
# c cancels in L? L = (g-1) m / (rho b^2 A): yes -- symbolic check
cs = sp.symbols('c', positive=True)
chk("c cancels identically in the magsail floor L", sp.simplify(sp.diff(L(10**6, "0.0476", 10**12, c=cs), cs)) == 0)

print("\nR7 alternative year definitions (hypothesis: ly = Julian year x c) -- SENSITIVITY, not a pass/fail on the tree")
edge = sp.N(L(10**6, "0.866", 10**10)/ly_J, 20)
print("  100 km row exact value %.9f ly; distance below the %%.2f rounding boundary 8.425: %.3e ly (rel %.3e)"
      % (edge, 8.425-edge, (8.425-edge)/edge))
for nm, days in (("Gregorian 365.2425", sp.Rational("365.2425")), ("tropical 365.24219", sp.Rational("365.24219")),
                 ("sidereal 365.25636", sp.Rational("365.25636"))):
    ly_alt = c_SI*days*86400
    r = float(ly_alt/ly_J - 1)
    alt = ["%.2f" % sp.N(L(10**6, "0.866", A)/ly_alt, 20) for A in (10**10, 10**12, 10**14)]
    jul = ["%.2f" % sp.N(L(10**6, "0.866", A)/ly_J, 20) for A in (10**10, 10**12, 10**14)]
    print("  %-20s rel %+.3e  printed ly column %s (Julian: %s)%s" % (nm, r, alt, jul, "  <-- 100 km row flips" if alt != jul else ""))
# M_P (another key) CODATA 2022 1.67262192595e-27 vs tree 1.67262192e-27: does the edge row flip?
M22 = sp.Rational("1.67262192595e-27")
e22 = edge * M_P / M22
chk("the 8.42 edge row does NOT flip under CODATA 2022 m_p (context, other key)", "%.2f" % e22 == "%.2f" % edge, "%.9f" % e22)
# trip_time_ly(d, b) = d/b years: consistent only if 'year' is the same year that defines the ly -- identity
d_, b_ = sp.symbols('d b', positive=True)
chk("trip_time in years = d_ly/b is independent of which year defines the ly (units cancel)",
    sp.simplify((d_*ly_J/(b_*c_SI))/yr_J - d_/b_) == 0)

print("\nR8 prose vs code (arrival.py:151-152, 159) -- a discrepancy in the owner, not in the constants")
d1000_AU = float(L(10**6, "0.0476", 10**12)/au_IAU)
d1000_ly = float(L(10**6, "0.866", 10**12)/ly_J)
print("  code: 1000 km sail from 0.048 c = %.2f AU (prose: 810 AU); from 0.87 c = %.4f ly (prose: 2.6 ly)" % (d1000_AU, d1000_ly))
au_needed = float(L(10**6, "0.0476", 10**12))/810.0
ly_needed = float(L(10**6, "0.866", 10**12))/2.6
print("  AU that would give 810 AU: %.4e m (x%.3f of IAU au); LY that would give 2.6 ly: %.4e m (x%.4f of ly_J)"
      % (au_needed, au_needed/float(au_IAU), ly_needed, ly_needed/float(ly_J)))
chk("prose '810 AU' NOT reproduced by the code (differs by > 1%)", abs(d1000_AU/810 - 1) > 0.01)
chk("prose '2.6 ly' NOT reproduced by the code (differs by > 1%)", abs(d1000_ly/2.6 - 1) > 0.01)
chk("no admissible au/ly value reconciles them (required change > 1e-6 relative)",
    abs(au_needed/float(au_IAU)-1) > 1e-6 and abs(ly_needed/float(ly_J)-1) > 1e-6)
ratio1 = d1000_AU/810; ratio2 = 2.6/d1000_ly
print("  code/prose ratios: AU column %.4f, ly column prose/code %.4f -- not a single common factor" % (ratio1, ratio2))

print("\nRESULT: %s (%d fail)" % ("ALL PASS" if fails == 0 else "FAILURES", fails))
sys.exit(1 if fails else 0)
