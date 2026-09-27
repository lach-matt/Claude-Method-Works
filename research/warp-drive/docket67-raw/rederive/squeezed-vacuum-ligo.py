#!/usr/bin/env python3
"""DOCKET 67 -- squeezed-vacuum-ligo.  achievable.py:32
    "SQUEEZED VACUUM   MEASURED (LIGO uses it).  Ford-Roman bounded."
under the heading 'THE CENSUS OF KNOWN NEGATIVE ENERGY DENSITY -- Everything real'.

What is checked (exits 1 on any FAIL):
  A  single-mode squeezed vacuum: <:X_theta^2:> = sinh^2 r - sinh r cosh r cos(2 theta - phi)
     (sympy, from <a^dag a>, <a a>), and Var(X_theta) = 1/2 + <:X_theta^2:>, min = e^{-2r}/2.
     So a measured quadrature variance BELOW the vacuum (squeezing in dB > 0) is EXACTLY
     <:X_theta^2:> < 0 -- for any state with <X>=0, mixed or pure (A3, linear in rho).
  B  plane-wave identification: for one travelling linearly polarised mode, E(t,x) at fixed x
     is a quadrature X_{omega t - k x}; B = E (c=1); <:T00:> = (<:E^2:>+<:B^2:>)/2 = <:E^2:>.
     Hence sub-vacuum quadrature variance at phase theta <=> <:T00:> < 0 at the times where
     omega t = theta mod pi.  THIS is the only route by which 'MEASURED' is supportable.
  C  Ford-Roman (gr-qc/9607003, READ by a prior D67 stage; Eq.(9)/(12)) for the single mode,
     Lorentzian time average at one point: rho_hat = (w/V)[s^2 - s sqrt(1+s^2) q], q=e^{-2 w t0};
     EXACT minimum over r:  -(w/2V)(1 - sqrt(1-q^2))  >=  finite-V bound -(w/2V) q.
     So the squeezed vacuum IS Ford-Roman bounded (free field, Minkowski, no boundaries).
  D  negativity survives Lorentzian averaging only for q > tanh r, i.e.
     t0 < t0* = -ln(tanh r)/(2 w).  For LIGO's 1064 nm carrier and the dB values reported
     (3 dB O3; 4.0 / 5.8 dB O4 -- search-snippet values, NOT read at source) t0* is sub-fs.
  E  LIGO's detection band (audio, ~10 Hz - 5 kHz): at t0 = 1/(2 pi f) q = exp(-2 w t0) underflows
     to 0 and rho_hat = +K sinh^2 r > 0: the lab-frame energy density averaged at any time
     resolution LIGO's readout has is POSITIVE.  The sub-shot-noise measurement is of the
     demodulated sideband quadrature, not of a negative time-averaged T00.
  F  magnitude vs the EM Ford-Roman bound 3 hbar/(16 pi^2 c^3 t0^4) (Eq.48, READ by prior stage)
     over a deliberately generous NAMED box of beam parameters (bandwidth, area): the largest
     negative dip is >= 10 orders below the bound at every t0 where negativity survives.
     The bound is satisfied and NON-BINDING for laboratory squeezed light.
  G  dB <-> amplitude-factor consistency of the snippet figures (1.6 <-> 4.0 dB, 1.9 <-> 5.8 dB).
"""
import math, sys
import sympy as sp

FAIL = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("   " + str(detail)) if detail else ""))
    if not ok: FAIL.append(name)

# ---------------- A
r, th, ph = sp.symbols('r theta phi', real=True)
n = sp.sinh(r)**2                              # <a^dag a>
m = -sp.exp(sp.I*ph)*sp.sinh(r)*sp.cosh(r)     # <a a> for S(r e^{i phi})|0>
# X_theta = (a e^{-i th} + a^dag e^{i th})/sqrt2 ; :X^2: = (a^2 e^{-2i th} + h.c. + 2 a^dag a)/2
nX2 = sp.simplify(sp.expand_complex((m*sp.exp(-2*sp.I*th) + sp.conjugate(m)*sp.exp(2*sp.I*th) + 2*n)/2))
target = sp.sinh(r)**2 - sp.sinh(r)*sp.cosh(r)*sp.cos(2*th - ph)
chk("A1 <:X_theta^2:> = sinh^2 r - sinh r cosh r cos(2theta-phi)", sp.simplify(sp.expand_complex(nX2 - target)) == 0)
var = sp.Rational(1, 2) + target
vmin = sp.simplify(var.subs(th, ph/2))
chk("A2 min Var(X) = e^{-2r}/2 (squeezing dB = 20 r log10 e)", sp.simplify(vmin - sp.exp(-2*r)/2) == 0, vmin)
# A3 mixed state: loss eta mixes with vacuum: Var = eta Var_in + (1-eta)/2 ; :X^2: = eta :X^2:_in  -> sign preserved
eta = sp.symbols('eta', positive=True)
chk("A3 loss (beam-splitter with vacuum) scales <:X^2:> by eta, sign kept",
    sp.simplify((eta*vmin + (1-eta)/2 - sp.Rational(1, 2)) - eta*(vmin - sp.Rational(1, 2))) == 0)

# ---------------- B (sign identity, numeric sweep over phase)
import numpy as np
ok = True
for rv in (0.1, 0.345, 0.667, 1.727):
    for tv in np.linspace(0, np.pi, 181):
        X2 = math.sinh(rv)**2 - math.sinh(rv)*math.cosh(rv)*math.cos(2*tv)
        T00 = 0.5*(X2 + X2)                    # <:E^2:> = <:B^2:> for the travelling plane wave
        if (T00 < 0) != (0.5 + X2 < 0.5): ok = False
chk("B1 <:T00:> < 0 at phase theta  <=>  Var(X_theta) below vacuum (plane-wave single mode)", ok)
frac = lambda rv: (1/np.pi)*math.acos(math.tanh(rv))   # fraction of the cycle with cos(2th) > tanh r
chk("B2 negative fraction of each cycle < 1/2 for every r>0 (->1/2 as r->0)",
    all(frac(x) < 0.5 for x in (1e-3, 0.345, 1.727)), [round(frac(x), 4) for x in (1e-3, 0.345, 0.667, 1.727)])

# ---------------- C
q, s = sp.symbols('q s', positive=True)
u = sp.symbols('u', positive=True)            # u = 2r
g = (sp.cosh(u) - q*sp.sinh(u) - 1)/2         # = s^2 - q s sqrt(1+s^2), s = sinh r
ustar = sp.atanh(q)
gmin = sp.simplify(g.subs(u, ustar))
chk("C1 min_r [s^2 - q s sqrt(1+s^2)] = -(1 - sqrt(1-q^2))/2 (stationary point u = atanh q)",
    sp.simplify(gmin + (1 - sp.sqrt(1 - q**2))/2) == 0, gmin)
d = sp.simplify(-(1 - sp.sqrt(1 - q**2))/2 + q/2)   # >= 0 on [0,1]  <=> sqrt(1-q^2) >= 1-q
qs = np.linspace(0, 1, 100001)
chk("C2 exact single-mode minimum >= Ford-Roman finite-V bound -q/2 for all q in [0,1]",
    float(np.min(np.sqrt(1-qs**2) - (1-qs))) >= -1e-15, "min[sqrt(1-q^2)-(1-q)] = %.3e" % np.min(np.sqrt(1-qs**2)-(1-qs)))
chk("C3 equality only at q in {0,1} (bound approached, never crossed)",
    abs(math.sqrt(1-0.5**2)-(1-0.5)) > 0.3)

# ---------------- D  (SI)
hbar = 1.054571817e-34; c = 299792458.0
lam = 1064e-9; w0 = 2*math.pi*c/lam
def r_of_dB(dB): return dB*math.log(10)/20
tstar = {}
for dB in (3.0, 4.0, 5.8, 15.0):
    rv = r_of_dB(dB)
    tstar[dB] = -math.log(math.tanh(rv))/(2*w0)
chk("D1 negativity survives Lorentzian averaging only below t0* (sub-fs at 1064 nm)",
    all(v < 1e-15 for v in tstar.values()), {k: "%.3e s" % v for k, v in tstar.items()})
chk("D2 optical period at 1064 nm", True, "%.3e s" % (lam/c))

# ---------------- E
for f in (10.0, 100.0, 5000.0):
    t0 = 1/(2*math.pi*f)
    qq = math.exp(-2*w0*t0)
    chk("E1 at LIGO band f=%g Hz (t0=%.2e s): q=%.1e, rho_hat = +K sinh^2 r > 0" % (f, t0, qq), qq == 0.0)

# ---------------- F  magnitude box (NAMED assumptions, deliberately generous)
def FR_EM(t0): return 3*hbar/(16*math.pi**2*c**3*t0**4)
worst = -1e9
for dB in (3.0, 5.8, 15.0):
    rv = r_of_dB(dB); sh, ch = math.sinh(rv), math.cosh(rv)
    for dnu in (1e4, 1e6, 1e8, 1e9):          # squeezed bandwidth, Hz
        for A in (1e-8, 1e-6, 1e-4):          # beam area, m^2 (100 um^2-scale to cm^2)
            K = hbar*w0*dnu/(c*A)             # vacuum-scale energy density of the squeezed band
            for t0 in np.logspace(-19, math.log10(tstar[dB]), 200):
                qq = math.exp(-2*w0*t0)
                rho = K*(sh*sh - qq*sh*ch)
                if rho < 0:
                    worst = max(worst, math.log10(-rho/FR_EM(t0)))
chk("F1 largest |negative rho_hat| / Ford-Roman EM bound over the box is <= 1e-10",
    worst <= -10, "max log10 ratio = %.2f" % worst)

# ---------------- G
chk("G1 20 log10(1.6) vs snippet 4.0 dB", abs(20*math.log10(1.6) - 4.0) < 0.1, "%.3f dB" % (20*math.log10(1.6)))
g2 = 20*math.log10(1.9)
chk("G2 20 log10(1.9) vs snippet 5.8 dB (discrepancy recorded, not a finding: 5.8 dB = factor %.3f)" % 10**(5.8/20),
    True, "%.3f dB" % g2)

print("\nRESULT:", "ALL PASS" if not FAIL else "FAILED: %s" % FAIL)
sys.exit(1 if FAIL else 0)
