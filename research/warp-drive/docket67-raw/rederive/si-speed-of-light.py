#!/usr/bin/env python3
"""DOCKET 67 -- rederive si-speed-of-light.
Checks what is finite/closed-form about the tree's use of c = 299 792 458 m/s (exact, SI).
Reads the owner files read-only (never writes under research/)."""
import math, struct, sys, importlib.util, os
from fractions import Fraction
import sympy as sp

WD = "/home/user/Claude-Method-Works/research/warp-drive"
fails = []
def chk(name, got, want):
    ok = (got == want)
    print(("PASS " if ok else "FAIL ") + name + f"  got={got!r} want={want!r}")
    if not ok: fails.append(name)

# 1. The source value (CODATA 2022, arXiv:2409.03787, Table XXXII p.50: 'c 299 792 458 m s^-1 exact')
C_SOURCE = 299792458
# owner literals, read from the files as text (no import side effects)
src_ns = open(os.path.join(WD, "nonstatic.py")).read().splitlines()
src_tr = open(os.path.join(WD, "transit.py")).read().splitlines()
lit_ns = src_ns[252].split("=")[1].split("#")[0].strip()   # nonstatic.py:253
lit_tr = src_tr[141].split("=")[1].strip()                 # transit.py:142
chk("nonstatic.py:253 literal", lit_ns, "2.99792458e8")
chk("transit.py:142 literal", lit_tr, "2.99792458e8")
chk("literal == SI integer (exact rational)", Fraction(lit_ns), Fraction(C_SOURCE))
# 2. 'exact' survives IEEE-754 binary64: integer < 2^53
chk("c < 2^53", C_SOURCE < 2**53, True)
chk("float(literal) is exactly the integer", Fraction(float(lit_ns)) == C_SOURCE, True)
# 3. LY = Julian year x c  (nonstatic.py:256 claims 'exact')
LY_exact = Fraction(36525, 100) * 86400 * C_SOURCE
lit_ly = src_ns[255].split("=")[1].split("#")[0].strip()
chk("Julian-year light-year integer", LY_exact, Fraction(9460730472580800))
chk("nonstatic.py:256 literal equals it exactly", Fraction(lit_ly), LY_exact)
chk("LY exactly representable in binary64 (even, <2^54)", Fraction(float(lit_ly)) == LY_exact, True)
# 4. transit.advantage_over_light: symbolic identity and bit-exact float zero
D, c = sp.symbols("D c", positive=True)
chk("symbolic D/c - D/c == 0 (holds for ANY c>0)", sp.simplify(D/c - D/c), 0)
C_SI = float(lit_tr)
for name, Dm in [("Earth-Moon",3.844e8),("Earth-Mars (min)",5.46e10),("Earth-Proxima",4.0175e16),("Milky Way cross",9.46e20)]:
    chk(f"float advantage_over_light({name}) bit-exact 0", (Dm/C_SI) - Dm/C_SI, 0.0)
# 5. nonstatic.band_ratio: c cancels (tau_band/tau_cross = 2 eps W / sqrt(W^2-1))
R, W, eps = sp.symbols("R W eps", positive=True)
tb = 2*eps*R/(c*sp.sqrt(W**2-1)); tc = R/(W*c)
chk("band_time/crossing_time independent of c", sp.simplify(sp.diff(tb/tc, c)), 0)
chk("band_ratio closed form", sp.simplify(tb/tc - 2*eps*W/sp.sqrt(W**2-1)), 0)
# 6. build_energy: E = R dW c^4 / G.  c contributes zero relative uncertainty (exact);
#    the whole relative uncertainty is G's: CODATA 2022 u_r(G)=2.2e-5 (Table XXXII), value unchanged from 2018.
G = sp.Symbol("G", positive=True); dW = sp.Symbol("dW", positive=True)
E = R*dW*c**4/G
chk("d ln E / d ln c = 4 (c enters as c^4)", sp.simplify(c*sp.diff(E, c)/E), 4)
chk("CODATA 2022 G literal == tree G literal 6.67430e-11", Fraction("6.67430e-11"), Fraction(src_ns[253].split("=")[1].split("#")[0].strip()))
# 7. span consistency: transit Earth-Proxima 4.0175e16 m vs nonstatic PROXIMA_LY*LY
span = 4.2465 * float(lit_ly)
print(f"INFO nonstatic proxima span = {span:.6e} m; transit Earth-Proxima = 4.0175e16 m; rel diff = {(span-4.0175e16)/4.0175e16:.2e}")
chk("spans agree to the 5 figures transit prints", round(span/1e12)*1e12 == 4.0175e16 or abs(span-4.0175e16)/4.0175e16 < 5e-5, True)
# 8. Physical content NOT supplied by the definition: is 'the classical channel, at c' (transit.py:145) an
#    idealisation, and which way does it err?  (a) vacuum dispersion bound READ at source (LHAASO,
#    arXiv:2402.06009, E_QG,1 > 1.0e20 GeV subluminal, 95% CL): |dv/c| <= E/E_QG for n=1 ((n+1)/2 = 1).
h_eVs = 4.135667696e-15    # CODATA 2022, exact (Table XXXIII)
nu = 1e9                   # a 1 GHz radio carrier (illustrative channel choice, NOT a datum of the tree)
E_GeV = h_eVs*nu/1e9
dv_liv = E_GeV/1.0e20
t_prox = 4.0175e16/C_SOURCE
print(f"INFO 1 GHz photon: E={E_GeV:.3e} GeV; linear-LIV |dv/c| <= {dv_liv:.2e}; delay over Earth-Proxima <= {dv_liv*t_prox:.2e} s")
#    (b) cold-plasma group delay dt = e^2/(8 pi^2 eps0 m_e c) * N_col / nu^2, N_col = column density (m^-2).
#        Constants CODATA 2022 (read). n_e of the local ISM is NOT read here -> parametrised.
e=1.602176634e-19; eps0=8.8541878188e-12; me=9.1093837139e-31
K = e**2/(8*math.pi**2*eps0*me*C_SOURCE)
pc = 3.0856775814913673e16
print(f"INFO dispersion constant e^2/(8 pi^2 eps0 m_e c) = {K:.6e} s m^2 Hz^2 -> {K*pc*1e6/1e9**2*1e3:.4f} ms per (pc cm^-3) at 1 GHz")
for ne_cm3 in (0.01, 0.1, 1.0):
    Ncol = ne_cm3*1e6*4.0175e16
    print(f"INFO   n_e={ne_cm3} cm^-3 (assumed, not read): 1 GHz delay over Earth-Proxima = {K*Ncol/nu**2*1e3:.3f} ms  (signal SLOWER than c)")
chk("dispersion constant reproduces the radio-astronomy 4.149 ms/(pc cm^-3) at 1 GHz", round(K*pc*1e6/1e18*1e3,3), 4.149)
chk("any dispersion delay is >= 0 (channel never beats D/c): advantage_over_light can only go negative", K > 0, True)
print("\nRESULT:", "ALL PASS" if not fails else f"{len(fails)} FAIL: {fails}")
sys.exit(1 if fails else 0)
