#!/usr/bin/env python3
"""DOCKET 67 / pass S / 15 of 35 -- effective-mass-band-curvature.

Re-derives, from nothing but the definition, what the tree uses:
  candidates.py:47-53   m* = hbar^2/(d^2E/dk^2) is band curvature, not T_00;
                        m* < 0 still carries POSITIVE energy; the group
                        velocity's response to momentum is what inverts.
  candidates.py:486-491 effective_mass_violates_an_energy_condition() -> False
  achievable.py:55-59   ... "not T_00, it does not gravitate" ... negative-index
                        metamaterials "are about the refractive index".
  ledger.py:1542-1544   S1 STRUCK on KIND.

Checks (each prints PASS/FAIL; exit 1 on any FAIL):
  C1 sympy: m* = hbar^2/E'' reproduces the parabolic-band mass; semiclassical
     dv/dt = F/m* (so m*<0 inverts the ACCELERATION response, and v opposes k
     on an inverted parabola).
  C2 sympy+z3: tight-binding band E = E0 - 2t cos(ka): m*(k) < 0 exactly on
     pi/2 < |ka| <= pi, yet the excitation energy above the band minimum,
     2t(1 - cos ka), is >= 0 everywhere -- z3 proves no (t>0, c=cos ka in
     [-1,1], c<0) makes it negative.  The sign of m* and the sign of the
     excitation energy are independent.
  C3 negative control: the sign of E itself is NOT fixed by the curvature --
     an inverted parabola with E0 < 0 has E < 0 and m* < 0; a normal parabola
     with E0 < 0 has E < 0 and m* > 0.  "Positive energy" therefore needs a
     reference (a stable ground state, or the absolute rest-energy-inclusive
     T_00), which is a hypothesis the tree does not name.
  C4 numeric, RECONSTRUCTED model (NOT the fit of arXiv:2204.04041, which could
     not be read here): a 2x2 non-Hermitian exciton-photon model with a
     dissipative (imaginary) coupling produces a lower branch whose Re E has
     NEGATIVE curvature at k=0 while Re E ~ 2 eV > 0 throughout.  Inputs:
     E_x = 2.0 eV (order of the monolayer-WS2 A exciton; RECONSTRUCTED),
     photon mass 1e-5 m_e (typical planar microcavity; RECONSTRUCTED).
  C5 sympy: Brillouin energy density of a dispersive negative-index medium
     (Drude eps, Lorentz mu), u ~ d(w eps)/dw |E|^2 + d(w mu)/dw |H|^2, is
     POSITIVE throughout the band where eps<0 and mu<0 (lossless limit,
     quasi-monochromatic).  Negative index is a statement about n, not a
     negative energy density.  Plus the general passive-medium bound: if
     d eps/dw > 2(1-eps)/w (Landau-Lifshitz ECM Sec. 84, NAMED-NOT-READ) then
     d(w eps)/dw > 2 - eps >= 1 for eps <= 1 -- checked symbolically / z3.
  C6 what "does not gravitate" can and cannot mean: a quasiparticle of energy
     E adds E/c^2 of gravitating mass-energy whatever the sign of m*; the
     number printed is E/c^2 for a 2 eV polariton (m* is not in it).
"""
import sys
import sympy as sp

fails = []


def check(tag, ok, msg):
    print(("PASS " if ok else "FAIL ") + tag + " -- " + msg)
    if not ok:
        fails.append(tag)


hbar, k, m, E0, F, t, a = sp.symbols('hbar k m E0 F t a', positive=True)
kk = sp.symbols('kk', real=True)
E0r = sp.symbols('E0r', real=True)

# ---------------------------------------------------------------- C1
Epar = E0 + hbar**2 * kk**2 / (2 * m)
mstar = sp.simplify(hbar**2 / sp.diff(Epar, kk, 2))
check("C1a", sp.simplify(mstar - m) == 0, "hbar^2/E'' of E0+hbar^2k^2/2m is m")
Einv = E0 - hbar**2 * kk**2 / (2 * m)
mstar_inv = sp.simplify(hbar**2 / sp.diff(Einv, kk, 2))
check("C1b", sp.simplify(mstar_inv + m) == 0, "inverted parabola: m* = -m")
v_inv = sp.diff(Einv, kk) / hbar
check("C1c", sp.simplify(v_inv + hbar * kk / m) == 0,
      "inverted parabola: v = -hbar k/m, group velocity OPPOSITE to k")
# semiclassical: hbar dk/dt = F  =>  dv/dt = (1/hbar) E'' dk/dt = F E''/hbar^2
for name, Ek in (("normal", Epar), ("inverted", Einv)):
    Epp = sp.diff(Ek, kk, 2)
    dvdt = sp.simplify(Epp * F / hbar**2)
    ms = sp.simplify(hbar**2 / Epp)
    check("C1d-" + name, sp.simplify(dvdt - F / ms) == 0,
          "dv/dt = F/m* (%s band, m* = %s)" % (name, ms))

# ---------------------------------------------------------------- C2
Etb = E0r - 2 * t * sp.cos(kk * a)
mstar_tb = sp.simplify(hbar**2 / sp.diff(Etb, kk, 2))
check("C2a", sp.simplify(mstar_tb - hbar**2 / (2 * t * a**2 * sp.cos(a * kk))) == 0,
      "tight binding: m*(k) = hbar^2/(2 t a^2 cos ka)")
import math
neg = [x for x in (0.6, 1.0, 1.5, 2.0, 2.5, 3.0, 3.14159)
       if 2 * math.cos(x) < 0]
check("C2b", neg == [2.0, 2.5, 3.0, 3.14159],
      "m* < 0 exactly where cos ka < 0 (sampled ka = 0.6..pi): %s" % neg)
excit = sp.simplify(Etb - (E0r - 2 * t))
check("C2c", sp.simplify(excit - 2 * t * (1 - sp.cos(a * kk))) == 0,
      "excitation energy above band minimum = 2t(1 - cos ka)")
try:
    import z3
    T, C = z3.Reals('T C')
    s = z3.Solver()
    s.add(T > 0, C >= -1, C <= 1, C < 0,          # m* < 0 region
          2 * T * (1 - C) <= 0)                    # excitation energy <= 0 ?
    r = s.check()
    check("C2d", r == z3.unsat,
          "z3: no (t>0, cos ka in [-1,0)) gives excitation energy <= 0 -> %s" % r)
    s2 = z3.Solver()                               # vacuity guard: region inhabited
    s2.add(T > 0, C >= -1, C <= 1, C < 0)
    check("C2e", s2.check() == z3.sat, "vacuity guard: the m*<0 region is non-empty")
except ImportError:
    check("C2d", False, "z3 not installed (pip install z3-solver)")

# ---------------------------------------------------------------- C3
vals = []
for E0v, sgn in ((-1.0, -1), (-1.0, +1), (+1.0, -1)):
    Ek = E0v + sgn * 0.5 * 0.01            # hbar=m=1, k=0.1
    ms = 1.0 / sgn
    vals.append((E0v, sgn, Ek, ms))
indep = (vals[0][2] < 0 and vals[0][3] < 0) and (vals[1][2] < 0 and vals[1][3] > 0)
check("C3", indep,
      "negative control: E<0 occurs with m*<0 AND with m*>0 once the zero of E "
      "is moved -- the sign of E is a reference choice, not a curvature fact: %s" % vals)

# ---------------------------------------------------------------- C4
# RECONSTRUCTED 2x2 model (not the published fit): H = [[Ec(k)-i g, -i q],
# [-i q, Ex - i g]], equal linewidths, purely dissipative coupling q, photon
# detuned ABOVE the exciton by d0 > 2q (beyond the exceptional point).
# Closed form: E_pm = Ex + delta/2 - i g +/- sqrt(delta^2/4 - q^2),
# delta(k) = d0 + hbar^2 k^2 / (2 m_c).
import cmath
dl, qq, mcs, d0s = sp.symbols('delta q m_c d_0', positive=True)
Elow = dl / 2 - sp.sqrt(dl**2 / 4 - qq**2)          # Re E_lower - Ex
dEdd = sp.diff(Elow, dl)
check("C4a", sp.simplify(dEdd.subs(dl, 3 * qq)) < 0,
      "d(Re E_lower)/d(delta) < 0 beyond the EP (at delta = 3q: %s): the "
      "exciton-like lower branch FALLS as the photon moves away -- inverted" %
      sp.nsimplify(sp.simplify(dEdd.subs(dl, 3 * qq))))
Ek = Elow.subs(dl, d0s + hbar**2 * kk**2 / (2 * mcs))
curv0 = sp.simplify(sp.diff(Ek, kk, 2).subs(kk, 0))
mlow = sp.simplify(hbar**2 / curv0)
print("     m*_lower(k=0) =", mlow)
mlow_big = sp.simplify(sp.limit(mlow / (mcs * d0s**2 / qq**2), d0s, sp.oo))
check("C4b", sp.simplify(mlow.subs({d0s: 3 * qq})) .could_extract_minus_sign()
      and mlow_big == -1,
      "m*_lower < 0 for d0 > 2q; -> -m_c d0^2/q^2 for d0 >> q (limit ratio %s)" % mlow_big)
me = 9.1093837015e-31
hb = 1.054571817e-34
eV = 1.602176634e-19
mc = 1e-5 * me               # RECONSTRUCTED photon mass
Ex = 2.0                     # eV, RECONSTRUCTED (order of monolayer-WS2 A exciton)
d0v, qv, gv = 0.03, 0.01, 0.005   # eV, RECONSTRUCTED


def lower(kinv_um):
    kk_ = kinv_um * 1e6
    Ec = Ex + d0v + (hb * kk_) ** 2 / (2 * mc) / eV
    a11, a22, a12 = Ec - 1j * gv, Ex - 1j * gv, -1j * qv
    tr, det = a11 + a22, a11 * a22 - a12 * a12
    d = cmath.sqrt(tr * tr / 4 - det)
    return min(tr / 2 + d, tr / 2 - d, key=lambda z: z.real).real


ks = [i * 0.05 for i in range(0, 9)]
low = [lower(x) for x in ks]
check("C4c", all(low[i + 1] < low[i] for i in range(len(low) - 1)) and min(low) > 1.9,
      "numeric: Re E_lower falls monotonically over k = 0..0.4 /um (m* < 0) "
      "while staying at %.5f-%.5f eV > 0" % (min(low), max(low)))


def lower_coherent(kinv_um, g=0.01):
    kk_ = kinv_um * 1e6
    Ec = Ex + d0v + (hb * kk_) ** 2 / (2 * mc) / eV
    return (Ec + Ex) / 2 - math.sqrt(((Ec - Ex) / 2) ** 2 + g * g)


lc = [lower_coherent(x) for x in ks]
check("C4d", all(lc[i + 1] > lc[i] for i in range(len(lc) - 1)),
      "control: a Hermitian coupling g of the same size gives a NORMAL (m*>0) lower branch")

# ---------------------------------------------------------------- C5
w, wp, w0, Ff = sp.symbols('omega omega_p omega_0 F', positive=True)
eps = 1 - wp**2 / w**2
mu = 1 - Ff * w**2 / (w**2 - w0**2)
deps = sp.simplify(sp.diff(w * eps, w))
dmu = sp.simplify(sp.diff(w * mu, w))
check("C5a", sp.simplify(deps - (1 + wp**2 / w**2)) == 0,
      "Drude: d(w eps)/dw = 1 + wp^2/w^2 > 0 for all w")
print("     Lorentz: d(w mu)/dw =", sp.factor(dmu))
# numeric band: wp=10, w0=4, F=0.56 -> mu<0 on w0 < w < w0/sqrt(1-F)
wpv, w0v, Fv = 10.0, 4.0, 0.56
band_hi = w0v / math.sqrt(1 - Fv)
okband, npts, umin = True, 0, None
for i in range(1, 400):
    wv = w0v + (band_hi - w0v) * i / 400.0
    e = 1 - wpv**2 / wv**2
    mm = 1 - Fv * wv**2 / (wv**2 - w0v**2)
    if e < 0 and mm < 0:
        npts += 1
        de = float(deps.subs({w: wv, wp: wpv}))
        dm = float(dmu.subs({w: wv, w0: w0v, Ff: Fv}))
        u = de + dm                      # |E|^2 = |H|^2 = 1 in natural units
        umin = u if umin is None else min(umin, u)
        okband &= (de > 0 and dm > 0)
check("C5b", npts > 0 and okband,
      "negative-index band (eps<0, mu<0), %d points: both d(w eps)/dw, d(w mu)/dw > 0; "
      "min u = %.3f > 0" % (npts, umin if umin else float('nan')))
try:
    import z3
    E_, D_, W_ = z3.Reals('E D W')
    s = z3.Solver()
    s.add(W_ > 0, E_ <= 1, D_ > 2 * (1 - E_) / W_, E_ + W_ * D_ < 1)
    r = s.check()
    check("C5c", r == z3.unsat,
          "z3: eps <= 1 and d eps/dw > 2(1-eps)/w imply d(w eps)/dw >= 1 -> %s" % r)
except ImportError:
    pass

# ---------------------------------------------------------------- C6
c = 299792458.0
E_pol = 2.0 * eV
check("C6", E_pol / c**2 > 0,
      "a 2 eV polariton adds E/c^2 = %.4e kg of gravitating mass-energy; m* "
      "does not enter this number (so 'm* does not gravitate' is true of the "
      "curvature; 'the quasiparticle does not gravitate' would be false)" % (E_pol / c**2))

print()
print("FAILS:", fails if fails else "none")
sys.exit(1 if fails else 0)
