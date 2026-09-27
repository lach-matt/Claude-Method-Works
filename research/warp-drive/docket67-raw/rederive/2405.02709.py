"""DOCKET 67 -- rederive the Fuchs et al. (arXiv:2405.02709) shell mass as the tree uses it.
Read-only against research/warp-drive (imports stock.py / stockgate.py with bytecode writing off).
"""
import sys, math, importlib.util
sys.dont_write_bytecode = True
from fractions import Fraction
import sympy as sp

WD = "/home/user/Claude-Method-Works/research/warp-drive"
bad = []
def chk(label, got, want, tol=None):
    ok = (got == want) if tol is None else abs(got / want - 1) <= tol
    print("%-4s %-70s got=%r want=%r" % ("PASS" if ok else "FAIL", label, got, want))
    if not ok: bad.append(label)

# 1. The mass as Warp Factory's W1 example parameterises it: m = R2 c^2/(2G) * 1/3 (octave/run_*.m:9)
R2, c, G = sp.Rational(20), sp.Integer(299792458), sp.Rational(667430, 10**16)   # CODATA 2018 = CODATA 2022 G
m = R2 * c**2 / (2 * G) / 3
mf = float(m)
print("m = R2 c^2/(2G)/3 =", sp.N(m, 8), "kg")
chk("5-figure value 4.4886e27 reproduced", float("%.5g" % mf), 4.4886e27)
chk("paper's printed 4.49e27 (3 s.f., p.13 and Table 1) consistent", float("%.3g" % mf), 4.49e27)
# G's relative standard uncertainty 2.2e-5 (CODATA 2018/2022): does it move the 5th figure?
for sgn in (-1, 1):
    mg = mf / (1 + sgn * 2.2e-5)
    print("  G at %+d sigma -> m = %.6e (5 s.f. %.5g)" % (sgn, mg, mg))
# FINDING: +/-1 sigma in G moves the 5th figure by +/-1 (4.4885e27 .. 4.4887e27).  The 5th figure of
# 4.4886e27 is therefore at the edge of G's uncertainty; the value is exact only as 'R2 c^2/(6G)' with
# CODATA G.  It does not touch any orders-of-magnitude comparison (shift 2.2e-5 relative = 1e-5 dex).
chk("G's 1-sigma moves the 5th figure by at most 1 unit",
    max(abs(float("%.5g" % (mf / (1 + s * 2.2e-5))) - 4.4886e27) for s in (-1, 1)) <= 1.0001e23, True)
chk("G's 1-sigma moves log10(m) by < 1e-4 dex", abs(math.log10(1 + 2.2e-5)) < 1e-4, True)

# 2. Jupiter-mass statement (p.13: '2.365 Jupiter masses'); IAU 2015 nominal GM_J = 1.2668653e17 m^3 s^-2
MJ = 1.2668653e17 / 6.67430e-11
print("M/M_J (5-fig m) = %.5f ; (4.49e27) = %.5f" % (mf / MJ, 4.49e27 / MJ))
chk("2.365 M_J agrees with 4.4886e27 to 3 parts in 10^4", mf / MJ, 2.365, 3e-4)

# 3. Horizon hypothesis the paper states (p.27: R_shell > 2GM/c^2); exact rationals
rs = sp.nsimplify(2 * G * m / c**2)
chk("2GM/c^2 = R2/3 exactly (sympy)", sp.simplify(rs - R2 / 3) == 0, True)
chk("2GM/c^2 < R1 = 10 m (no horizon in shell)", float(rs) < 10.0, True)
chk("fill fraction M/(R1 c^2/2G) = 2/3 exactly", sp.simplify(m / (10 * c**2 / (2 * G)) - sp.Rational(2, 3)) == 0, True)
chk("Le 2602.18023 p.34: 2M = 6.668692 m for M = 4.49e27", 2 * 6.67430e-11 * 4.49e27 / 299792458.0**2, 6.668692, 1e-6)

# 4. The tree's comparisons, recomputed from the owner files themselves
def load(name):
    spec = importlib.util.spec_from_file_location(name + "_d67", "%s/%s.py" % (WD, name))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
st = load("stock"); sg = load("stockgate")
chk("stock.FUCHS_SHELL_KG equals the rederived 5-figure value", st.FUCHS_SHELL_KG, float("%.5g" % mf))
chk("stockgate.FUCHS_SHELL_KG equals the rederived 5-figure value", sg.FUCHS_SHELL_KG, float("%.5g" % mf))
r70 = st.against_the_shell(); fk = st.FUCHS_SHELL_KG / r70
print("stock.against_the_shell(70 kg) = %.4e  (feedstock %.4e kg, %.2f orders)" % (r70, fk, math.log10(r70)))
r1000 = sg.against_the_shell(); fk2 = sg.FUCHS_SHELL_KG / r1000
print("stockgate.against_the_shell(1000 kg) = %.4e (feedstock %.4e kg, %.2f orders)" % (r1000, fk2, math.log10(r1000)))
chk("stockgate:797 ratio 4.98e19 reproduced", float("%.3g" % r1000), 4.98e19)
# stock.py:175-178 prose: '120 tonnes, or 0.7 tonnes at a chondrite, sits about 25 orders below'
for t in (120e3, 0.7e3, fk):
    print("  %.4g kg -> %.2f orders below the shell" % (t, math.log10(st.FUCHS_SHELL_KG / t)))
print("  DISCREPANCY (tree-internal, recorded not repaired): 120 t sits %.1f orders below, not ~25;"
      " the 0.7 t figure gives %.1f; stock.py:525 label says '25+ orders' but asserts only > 1e22;"
      " against_the_shell(70) is %.2f orders." % (math.log10(st.FUCHS_SHELL_KG/120e3),
      math.log10(st.FUCHS_SHELL_KG/700.0), math.log10(r70)))

# 5. Robustness of the 'not a barrier' conclusion to the shell-mass hypothesis the tree drops:
# the paper (sec. 6) says optimisation may reduce required mass 'by orders of magnitude'.
# How many orders of reduction would it take for the feedstock to reach the shell mass?
print("orders of shell-mass reduction before the 70 kg feedstock equals the shell: %.1f" % math.log10(r70))
print("orders before the 1000 kg craft feedstock equals the shell: %.1f" % math.log10(r1000))
# Any static flat-cavity shell obeys 2M/R < 24/25 (surface DEC, Le 2606.22531 eq 2.13) -- an UPPER
# bound only; no LOWER bound on shell mass at fixed beta is stated in the source or found here.
print("upper bound check: M/(R1 c^2/2G) = 2/3 < 24/25 :", 2/3 < 24/25)

print("\n%d failure(s)" % len(bad))
sys.exit(1 if bad else 0)
