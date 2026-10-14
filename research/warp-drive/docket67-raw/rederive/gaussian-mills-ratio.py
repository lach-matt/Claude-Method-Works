"""DOCKET 67 -- re-derivation of the Gaussian Mills-ratio bounds as noise.py uses them.
Checks (read-only on research/warp-drive; no bytecode written):
 A. sympy: Q(z)=erfc(z/sqrt2)/2; (phi/z - Q)' = -phi/z^2 < 0 and (phi(1/z-1/z^3) - Q)' = 3 phi/z^4 > 0,
    both differences -> 0 as z -> oo  =>  phi(1/z-1/z^3) < Q < phi/z for every z > 0 (strict).
 B. sympy + z3: Gordon's (1941) lower bound z/(1+z^2) phi is STRONGER than the tree's (1/z-1/z^3) phi.
 C. The -ln P bracket and its O(1/z^2) remainder, checked against mpmath erfc at 60 digits.
 D. The tree's value: z from achievable/noise, stdlib Mills form vs mpmath erfc at 30 and 60 digits.
"""
import sys, math
sys.dont_write_bytecode = True
import sympy as sp, mpmath as mp
ok = True
def rep(name, cond, detail=""):
    global ok; ok &= bool(cond); print(("PASS " if cond else "FAIL ") + name + ("  " + detail if detail else ""))

z = sp.symbols('z', positive=True)
phi = sp.exp(-z**2/2)/sp.sqrt(2*sp.pi)
Q = sp.erfc(z/sp.sqrt(2))/2
rep("A1 Q' = -phi", sp.simplify(sp.diff(Q, z) + phi) == 0)
dU = sp.simplify(sp.diff(phi/z - Q, z))
rep("A2 (phi/z - Q)' = -phi/z^2", sp.simplify(dU + phi/z**2) == 0, str(dU))
dL = sp.simplify(sp.diff(phi*(1/z - 1/z**3) - Q, z))
rep("A3 (phi(1/z-1/z^3) - Q)' = 3 phi/z^4", sp.simplify(dL - 3*phi/z**4) == 0, str(dL))
rep("A4 limits at oo are 0", sp.limit(phi/z - Q, z, sp.oo) == 0 and sp.limit(phi*(1/z-1/z**3) - Q, z, sp.oo) == 0)
gap = sp.simplify(z/(1+z**2) - (1/z - 1/z**3))
rep("B1 Gordon lower - tree lower = 1/(z^3(1+z^2)) > 0", sp.simplify(gap - 1/(z**3*(1+z**2))) == 0, str(gap))
try:
    import z3
    x = z3.Real('x'); s = z3.Solver()
    # negation of: x>0 -> x^4 >= (x^2-1)(x^2+1)  (i.e. x/(1+x^2) >= 1/x - 1/x^3 after clearing x^3(1+x^2)>0)
    s.add(x > 0, x**4 < (x**2 - 1)*(x**2 + 1))
    rep("B2 z3: no x>0 violates Gordon-lower >= tree-lower (cleared denominators)", s.check() == z3.unsat, str(s.check()))
except ImportError:
    print("SKIP B2 z3 not installed")

# working precision must resolve the relative gap 1/z^2 of the bounds and the z^2/2 cancellation in C2:
# the exponent -z^2/2 carries absolute error 10^(2L-dps) (L = log10 z) against a remainder 10^(-2L), so dps = 4L + 30.
# (fixed 60 digits, then 2L+40, both FAILED at z >= 1e20 / 1e71 by PRECISION, not by the bound -- shown on the first runs)
def Qm(t): return mp.erfc(mp.mpf(t)/mp.sqrt(2))/2
def phim(t): return mp.exp(-mp.mpf(t)**2/2)/mp.sqrt(2*mp.pi)
worst = 0
for t in ['0.1','0.5','1','2','3','5','10','30','100','1e5','1e20','1e71','1.2823e71']:
    mp.mp.dps = int(4*max(0, math.log10(float(t))) + 30); t = mp.mpf(t); P = Qm(t); up = phim(t)/t; lo = phim(t)*(1/t - 1/t**3)
    rep("C1 bounds hold at z=%s" % mp.nstr(t, 6), lo < P < up)
    if t > 2:
        rem = -mp.log(P) - (t**2/2 + mp.log(t*mp.sqrt(2*mp.pi)))
        ratio = rem*t**2
        rep("C2 [dps=%d] remainder" % mp.mp.dps + " of -lnP in (0, -ln(1-1/z^2)] and ~1/z^2 at z=%s" % mp.nstr(t, 6),
            0 < rem <= -mp.log(1 - 1/t**2), "rem*z^2 = %s" % mp.nstr(ratio, 8))

# D. the tree's number
sys.path.insert(0, '/home/user/Claude-Method-Works/research/warp-drive')
import noise, achievable
K = noise.K_F_FIXTURE
unit = achievable.HBAR / (achievable.C_SI**3 * achievable.hold_time(1.0)**4)
zt = achievable.required_density(1.0) / (math.sqrt(K) * unit)
print("   z = %.6e, log10 z = %.6f" % (zt, math.log10(zt)))
stdlib = noise.el_vacuum_log10_neg_ln_p()
for dps in (30, 60):
    mp.mp.dps = dps
    Z = mp.mpf(achievable.required_density(1.0)) / (mp.sqrt(mp.mpf(K)) * mp.mpf(unit))
    val = mp.log10(-mp.log(mp.erfc(Z/mp.sqrt(2))/2))
    rep("D1 stdlib Mills form = mpmath erfc at %d digits (|diff| < 1e-12)" % dps, abs(float(val) - stdlib) < 1e-12,
        "mp=%s stdlib=%.12f" % (mp.nstr(val, 15), stdlib))
lead = 2*math.log10(zt) - math.log10(2)
rep("D2 value equals 2 log10 z - log10 2 to double precision (ln term contributes ~1e-140)", abs(stdlib - lead) < 1e-12,
    "lead=%.12f" % lead)
rep("D3 141 < log10(-ln P) < 142", 141 < stdlib < 142, "%.6f" % stdlib)
print("   log10 z needed for the 142 threshold: %.6f (have %.6f; margin %.4f dex in z)" %
      ((142 + math.log10(2))/2, math.log10(zt), (142 + math.log10(2))/2 - math.log10(zt)))
print("ALL PASS" if ok else "SOME FAIL"); sys.exit(0 if ok else 1)
