#!/usr/bin/env python3
"""DOCKET 67 -- audit rederivation: 'VACUUM POLARISATION  MEASURED via the Lamb shift.'
(research/warp-drive/achievable.py:35, in 'THE CENSUS OF KNOWN NEGATIVE ENERGY DENSITY').

What is computed here (no source value is assumed; each literature comparison is labelled):
 R1  the leading (Uehling, alpha (Z alpha)^4) vacuum-polarisation shift of hydrogen nS levels,
     closed form -4 alpha (Z alpha)^4 m_r^3 c^2/(15 pi n^3 m_e^2), in MHz, for 1S and 2S; and the
     same quantity as the full expectation value of the Uehling potential (numerical, sympy+mpmath),
     so the closed form is checked, not copied.
 R2  its SIZE and SIGN against the measured classic 2S1/2-2P1/2 Lamb shift (~1057.8 MHz): VP is a
     few-percent piece of OPPOSITE sign to the total; the measured quantity is a frequency interval.
 R3  muonic hydrogen: the Uehling contribution to E(2P)-E(2S), point proton, numerically -- where VP
     is the DOMINANT term (~205 meV).  The literature figure it is compared with is labelled.
 R4  what the Uehling correction IS, as a field: Q_eff(r) >= Z e at every r (the kernel is positive),
     so the Coulomb field is STRENGTHENED, never reversed, and the classical field energy density
     E^2/(8 pi) built from it is positive at every r.  CONTROL: a deliberately sign-flipped kernel
     is caught by the same check.  (This is a statement about the effective potential the Lamb shift
     tests.  It is NOT a claim about the renormalised <T_00> of the QED vacuum, which no Lamb-shift
     measurement reads.)
Exit 0 iff every check passes.
"""
import sys
import mpmath as mp
import sympy as sp
from scipy import constants as C

mp.mp.dps = 30
ok = True
def chk(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  -- " + detail if detail else ""))

# ---------- constants (CODATA 2022 as shipped in scipy 1.17.1) ----------
alpha = mp.mpf(C.fine_structure)
me = mp.mpf(C.physical_constants['electron mass energy equivalent in MeV'][0]) * 1e6   # eV
mmu = mp.mpf(C.physical_constants['muon mass energy equivalent in MeV'][0]) * 1e6
mp_ = mp.mpf(C.physical_constants['proton mass energy equivalent in MeV'][0]) * 1e6
h_eVs = mp.mpf(C.physical_constants['Planck constant in eV/Hz'][0])
print(f"1/alpha = {1/alpha}, m_e = {me} eV, m_mu = {mmu} eV, m_p = {mp_} eV")

def eV_to_MHz(E): return E / h_eVs / 1e6

# ---------- Uehling expectation value, exact in the Schrodinger wavefunctions ----------
r, k, a = sp.symbols('r k a', positive=True)
R = {
    (1, 0): 2 * a**sp.Rational(-3, 2) * sp.exp(-r / a),
    (2, 0): a**sp.Rational(-3, 2) / sp.sqrt(2) * (1 - r / (2 * a)) * sp.exp(-r / (2 * a)),
    (2, 1): a**sp.Rational(-3, 2) / sp.sqrt(24) * (r / a) * sp.exp(-r / (2 * a)),
}
# normalisation check (symbolic)
for key, Rf in R.items():
    chk(f"R_{key} normalised", sp.simplify(sp.integrate(Rf**2 * r**2, (r, 0, sp.oo)) - 1) == 0)
# inner integral  I(k) = INT_0^oo r R^2 e^{-k r} dr   (closed form in k, a)
I = {key: sp.lambdify((k, a), sp.simplify(sp.integrate(r * Rf**2 * sp.exp(-k * r), (r, 0, sp.oo))), 'mpmath')
     for key, Rf in R.items()}

def w(t, sign=+1):
    """Uehling spectral weight (positive for t>1 when sign=+1)."""
    return sign * (1 + 1 / (2 * t**2)) * mp.sqrt(t**2 - 1) / t**2

def uehling_shift(key, mlep, Z=1, mlight=me, sign=+1):
    """<V_U> in eV for a lepton of mass mlep bound to a proton; loop particle mass mlight.
    V_U(r) = -(Z alpha / r) (2 alpha/3 pi) INT_1^oo dt w(t) exp(-2 mlight t r)   (hbar = c = 1)."""
    mr = mlep * mp_ / (mlep + mp_)
    a_ = 1 / (Z * alpha * mr)                     # Bohr radius in eV^-1
    f = lambda t: w(t, sign) * I[key](2 * mlight * t, a_)
    return -(Z * alpha) * (2 * alpha / (3 * mp.pi)) * mp.quad(f, [1, 2, 10, mp.inf])

# ---------- R1: hydrogen nS, closed form vs full expectation value ----------
mr_e = me * mp_ / (me + mp_)
def closed(n, mr=mr_e): return -4 * alpha * alpha**4 * mr**3 / (15 * mp.pi * n**3 * me**2)
for n, key in ((1, (1, 0)), (2, (2, 0))):
    cf = eV_to_MHz(closed(n)); full = eV_to_MHz(uehling_shift(key, me))
    rel = abs(full - cf) / abs(cf)
    print(f"R1 H {n}S  closed form {float(cf):.4f} MHz   full <V_U> {float(full):.4f} MHz   rel diff {float(rel):.2e}")
    chk(f"R1 H {n}S: full Uehling expectation agrees with closed form to O(Z alpha)", rel < 3 * alpha)
cf1, cf2 = eV_to_MHz(closed(1)), eV_to_MHz(closed(2))
chk("R1 H 1S Uehling = -217 MHz (tree's limitaxis.py:337 anchor VP_H1S_MHZ = -217.0) to 0.5 %", abs(cf1 + 217) / 217 < 5e-3,
    f"{float(cf1):.3f} MHz")
chk("R1 H 2S Uehling ~ -27.1 MHz (textbook figure, labelled; not READ this run)", abs(cf2 + 27.1) < 0.1, f"{float(cf2):.3f} MHz")
p2 = eV_to_MHz(uehling_shift((2, 1), me))
print(f"R1 H 2P1/2 Uehling (nonrel. <V_U>) {float(p2):.6f} MHz  (alpha(Z alpha)^6-suppressed; ~0 at leading order)")

# ---------- R2: size and sign against the measured Lamb shift ----------
LAMB_MEAS = mp.mpf('1057.8')   # MHz, 2S1/2-2P1/2; order-of-magnitude comparison only (see audit JSON for sources)
vp_2s2p = cf2 - p2
frac = vp_2s2p / LAMB_MEAS
print(f"R2 VP contribution to E(2S)-E(2P) = {float(vp_2s2p):.3f} MHz = {float(100*frac):.2f} % of the measured +{LAMB_MEAS} MHz")
chk("R2 VP is OPPOSITE in sign to the measured Lamb shift (S raised overall; VP lowers S)", vp_2s2p < 0 < LAMB_MEAS)
chk("R2 VP is a minority piece (|VP|/Lamb < 5 %): the dominant term is the self-energy", abs(frac) < 0.05)

# ---------- R3: muonic hydrogen, where VP dominates ----------
s2 = uehling_shift((2, 0), mmu); p2m = uehling_shift((2, 1), mmu)
d_meV = (p2m - s2) * 1e3
print(f"R3 mu-p: Uehling  E(2P)-E(2S) = {float(d_meV):.4f} meV   (2S {float(s2*1e3):.4f}, 2P {float(p2m*1e3):.4f})")
chk("R3 mu-p Uehling 2P-2S within 0.1 % of the literature 205.0 meV (labelled, not READ this run)",
    abs(d_meV - 205.0) / 205.0 < 1e-3, f"{float(d_meV):.4f}")
chk("R3 mu-p: the delta-function (short-range) approximation FAILS by >10 % -- the muon orbit is inside the "
    "electron loop's range, which is why mu-p tests the Uehling potential's SHAPE, not just its contact term",
    abs(eV_to_MHz(closed(2, mmu * mp_ / (mmu + mp_))) / eV_to_MHz(p2m - s2) + 1) > 0.1)

# ---------- R4: what the correction is, as a field ----------
def Qeff_ratio(rr, sign=+1):
    """Q_eff(r)/(Z e) implied by V_U: 1 + (2 alpha/3 pi) INT w(t) e^{-2 m_e t r} dt (r in units of 1/m_e)."""
    return 1 + (2 * alpha / (3 * mp.pi)) * mp.quad(lambda t: w(t, sign) * mp.exp(-2 * t * rr), [1, 2, 10, mp.inf])
grid = [mp.mpf(10)**e for e in range(-6, 2)]
Q = [Qeff_ratio(x) for x in grid]
chk("R4 potential-level effective charge Q_eff(r) >= Z e on r in [1e-6, 10] /m_e (strengthened, never reversed)",
    all(q >= 1 for q in Q), ", ".join(f"{float(q):.6f}" for q in Q))
# energy density of the effective field is (Q_eff/r^2)^2/(8 pi) -- a square: check it is > 0 and exceeds bare
chk("R4 classical energy density of the effective field >= that of the bare Coulomb field (>0) at every grid r",
    all(q**2 >= 1 for q in Q))
Qc = [Qeff_ratio(x, sign=-1) for x in grid]
chk("R4 CONTROL: a sign-flipped kernel is detected (Q_eff < Z e somewhere)", any(q < 1 for q in Qc))

print("\nRESULT:", "ALL PASS" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
