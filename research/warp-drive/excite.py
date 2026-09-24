#!/usr/bin/env python3
r"""
excite.py -- DOCKET 63.  EXCITING THE HIGGS AT THE ENDPOINT: WHAT IT TAKES, AND
WHAT IT BUYS.

    python3 excite.py             the reading
    python3 excite.py --selftest  every fixture and every control; STDLIB ONLY
    python3 excite.py --verify    the sympy derivations, every residual exactly 0

Run under python3 (3.11) from research/warp-drive.  --selftest needs no sympy,
by design (axial.py's pattern): every identity it checks is a POLYNOMIAL
identity over fractions.Fraction, or an exact rational computation, and every
witness is stdlib Newton / RK4.  --verify re-derives the same statements
symbolically in sympy, including the three that are genuinely calculus rather
than polynomial algebra (the u = x f reduction in d dimensions, INT G d^3r, and
the Schrodinger and Dirac-Coulomb dilations).  RUN SYMPY FROM
research/warp-drive, never from a directory that can see recovered/struct.py.

M: "what would it take to excite the Higgs at the endpoint, and what would that
buy for addressing, binding and energy?"  This file is DOCKET 63's ruling,
section C, as an instrument.  It imports four seated modules (higgs, xigate,
endpoint, address) plus pdgcapture and warpfolder, and PINS NO NEW PHYSICAL
CONSTANT: m_h, Gamma_h, m_W, m_Z and the heavy quark masses are READ from
captures/PDG-2026.tsv through pdgcapture.read().

===============================================================================
0.  THE ANSWER
===============================================================================

WHAT IT TAKES IS A SOURCE THAT FILLS THE WHOLE ENDPOINT REGION, AT EVERY POINT,
FOR AS LONG AS THE DISPLACEMENT IS WANTED.

  1. Wherever the source is absent, the displacement relaxes to the vev at an
     asymptotic rate of EXACTLY m_h -- for every source sign, size and shape,
     and nonlinearly.  THEOREM D15, section 1.
  2. That length is attometres: hbar/(m_h c), computed below at the pinned
     125.20 and at the READ 125.13.
  3. So the displacement is ULTRALOCAL: delta phi = -J/m_h^2 [1 + O((lambda_h/
     L)^2)], and INT G d^3r = 1/m^2 means no arrangement of sources beats the
     local density.  THEOREM D16, section 2.
  4. THE EXACT COST (section 3).  A source whose mass is proportional to phi
     must carry rest energy 4 rho_EW eps(2-eps)(1-eps)^2; the field it holds
     carries rho_EW eps^2(2-eps)^2.  Total 8 rho_EW eps - 16 rho_EW eps^2 + ...
  5. At eps = 1e-18 (address.py section 7's clock fixture, an ORDER) the
     Higgs-derived density needed is address.source_density(1e-18, 1)[1], and
     built of stable neutral matter it is that divided by f = d ln m_p/d ln v,
     under H1 AND under H2 -- never one of them.

WHAT IT BUYS IS NOTHING ANY OF THE THREE ROLES CAN USE.

  ROLE 1, ADDRESSING: DEAD.  The source is a better address than the
  displacement it makes -- its gravity reads it farther (address.py section 9's
  domination theorem) and its own interior redshift beats the eps signal on a
  courier clock beyond a few centimetres.  Flat directions are inert (D19).
  ROLE 2, BINDING: NARROWED to O(eps), and only inside its own source.  The
  m_e mechanism is EXACTLY NULL -- an exact dilation (D18).
  ROLE 3, ENERGY: DEAD, by higgs.py's theorem that T_kk is a square for any
  minimally coupled scalar, which never mentions the mass.

  If "excite" means making Higgs QUANTA: at least m_h per quantum, gone in
  hbar/Gamma_h ~ 2e-22 s, and a number state has <delta phi> = 0 -- quanta
  displace nothing.

===============================================================================
1.  THEOREM D15.  TAIL_RATE_IS_MASS
===============================================================================

A static displacement of any vacuum with V''(v) = m^2 > 0 returns to v at
asymptotic rate exactly m.

    HYPOTHESES, NAMED.
      (H-a) static;
      (H-b) V smooth, V'(v) = 0, V''(v) = m^2 > 0;
      (H-c) outside the support of the source (J = 0 for r > r_s);
      (H-d) the displacement decays, f -> 0 as r -> infinity.  THIS IS THE
            ONLY PROPERTY OF THE SOLUTION THE PROOF USES;
      (H-e) the NONLINEAR proof is for a radial profile, in any dimension d.
            A non-spherical source is covered in its tail, where f is small,
            by the multipole witnesses k_l (l = 0..5), which are LINEAR.
    The Higgs mass enters only through (H-b).  No energy condition is used.

THE REDUCED EQUATION.  Put phi = v(1 + f), x = m r.  For the Mexican hat
V = (lambda/4)(phi^2 - v^2)^2, V'(v(1+f))/(lambda v^3) = f(f+1)(f+2) and
m^2 = V''(v) = 2 lambda v^2 (polynomial identities, exact), so

        f'' + 2 f'/x  =  (1/2) f (f+1)(f+2).

THE PROOF (ruling F1; elementary -- it replaces an unread Levinson/Hartman
citation).
  (i)   u = x f turns it into u'' = q u with q = 1 + (3/2) f + (1/2) f^2.  Since
        f -> 0, q -> 1, so q > 0 beyond some X1.
  (ii)  Beyond X1, u has at most one zero: a function with u'' = q u, q > 0, is
        convex where positive and concave where negative, so it cannot vanish
        at both ends of an interval without vanishing between.
  (iii) If u'/u > 0 at some point beyond that, u grows exponentially, which
        contradicts f -> 0.  So w = -u'/u > 0 eventually.
  (iv)  w satisfies the Riccati equation w' = w^2 - q.
  (v)   If w ever exceeds sqrt(1 + delta) + eta, it blows up at finite x --
        which would be a zero of u.  If it ever falls below sqrt(1 - delta) -
        eta, it reaches 0 at finite x -- contradicting (iii).  So w -> 1.
  In d dimensions u = x^{(d-1)/2} f adds (d-1)(d-3)/(4x^2) to q, which also
  tends to 0; the argument is unchanged.  For a general V, q = [V'(v(1+f))/
  (v m^2)]/f -> V''(v)/m^2 = 1.  --verify checks each identity in sympy.

WITNESSES (stdlib).  A two-point boundary-value solve (Numerov + Newton +
Thomas tridiagonal) whose ONLY condition at the far end is f(X) = 0 -- no tail
shape assumed, no rate imposed -- for f(5) in {-1e-6, -0.127814, -0.877854,
-1.585710, -2.448516, +50}, the rate measured at x = 15, 20, 25, and the box
moved from X = 40 to X = 70.  CONTROLS THAT MUST FIRE: the massless solve
returns 1/(X - x), NOT 1; mass-2 and mass-3 solves return 2 and 3; a Riccati
start 1e-3 above 1 blows up and 1e-3 below reaches zero, both at finite x.

    THE AMPLITUDES ARE RE-DERIVED, NOT SEATED.  They are f(5) of the tail
    u = A e^{-x} at A = -1e2, -1e3, -3e3, -1e4, shot inward by RK4; this file
    reproduces them.  Integrated further inward, every nonlinear profile BLOWS
    UP at a finite radius, reached two independent ways (from the boundary-value
    solution and from the tail).  THAT RADIUS IS REPORTED; THE WORD "CORE" IS
    REFUSED -- such a profile is the exterior of a singularity, realisable by
    J = grad^2 phi - V'(phi) inside it, not a physical core.

THE EXACT KINK, f = tanh(x/2) - 1, and its rate (1 + t)/2 -> 1, are polynomial
identities in t = tanh(x/2).  THEY HOLD IN THE REAL Z2 TOY ONLY: in the doublet
-v is gauge-equivalent to +v (the selftest exhibits the gauge element), so
"phi = -v, a degenerate TRUE vacuum", the kink and the sn-lattice are not
statements about the Higgs.

===============================================================================
2.  THEOREM D16.  DISPLACEMENT_IS_ULTRALOCAL
===============================================================================

    HYPOTHESES.  Linear regime (|delta phi| << v); static; a source J varying
    on a scale L >> lambda_h.

(-grad^2 + m^2) delta phi = -J has delta phi = -J/m^2 [1 + O((lambda_h/L)^2)],
and the Green's function integrates to INT G d^3r = INT r e^{-m r} dr = 1/m^2.
So no arrangement of sources does better than the local density: a displaced
vev exists only where its source is, give or take lambda_h.  For J = cos(x/L)
the exact response is the algebraic one times 1/(1 + (lambda_h/L)^2), whose
error is address.ultralocality_error(L) to leading order.

===============================================================================
3.  THE HOLDING COST (D20), DERIVED OVER Fraction
===============================================================================

    HYPOTHESES.  A static source of fixed number density whose rest mass is
    proportional to phi (m -> m phi/v) -- which is what the Higgs gives the
    fermions and W, Z; region large compared with lambda_h (D16), so gradient
    energy is negligible; energies measured from our vacuum.

Equilibrium V'(phi) + n m_0/v = 0 at phi = v(1 - eps) gives, in units of
rho_EW = |V_min| = lambda v^4/4,

        source rest energy  = -V'(phi) phi / rho_EW = 4 eps (2-eps)(1-eps)^2
        field energy        = [V(phi) - V(v)]/rho_EW =   eps^2 (2-eps)^2

both DERIVED by polynomial composition, not typed.  The total is
8 eps - 16 eps^2 + 12 eps^3 - ...  The ratio source/field is exactly
4(1-eps)^2/(eps(2-eps)) -> 2/eps: every joule of field costs 2/eps joules of
source.  V''(phi) = 0 at eps = 1 - 1/sqrt(3) -- past that the medium is
UNSTABLE -- and source = field at eps = 1 - 1/sqrt(5), which lies in the
unstable range.  So the source dominates the field everywhere the configuration
exists.

Built of stable neutral matter, rho = rho_H / f with f = d ln m_p/d ln v:
2/9 + 7S/9 under H1, S under H2 (address.dln_mp_dln_v), at S = 0.06.

===============================================================================
4.  ROLE 1, ADDRESSING: DEAD
===============================================================================

  - Ultralocality plus the screening theorem: the displacement says what the
    local mass density already says.
  - The same source is read farther by GRAVITY: address.py section 9, r/d grows
    without bound (sqrt(rho) against ln(rho)).  Asked of address.domination_ratio.
  - THE COURIER CLOCK.  A clock carried inside the region picks up the source's
    own interior redshift 2 pi G rho R^2/c^2 against a twin at infinity (uniform
    sphere: Phi(0) = -(3/2) G M/R).  It exceeds the eps signal once
    R > R* = sqrt(eps c^2/(2 pi G rho)).  With the twin at the SURFACE the
    potential difference is GM/(2R), one third as large, so each crossover is
    larger by EXACTLY sqrt(3).
  - THEOREM D19, FLAT_DIRECTIONS_ARE_INERT.  Moving along T1, T2, T3 or Y
    leaves H^dagger H invariant, so no mass and no derivative-free
    gauge-invariant local observable changes.  Exhibited exactly at the
    Pythagorean point cos = 3/5, sin = 4/5; a radial displacement is the
    control that must change it.
  - Role 1 is the only role the Higgs MASS kills by itself: the massless
    boundary-value solve decays as a power, 1/(X - x), not exponentially.
  - Consistent with DOCKET 60's D14: the priced object has no parameter a
    destination can be written in, and the Higgs does not supply one.

===============================================================================
5.  ROLE 2, BINDING: NARROWED TO O(eps), AND ONLY INSIDE ITS OWN SOURCE
===============================================================================

THEOREM D18, ELECTRON_MASS_IS_A_RULER.  m_e -> m_e(1 + eps) with alpha fixed
(H2) and point nuclei clamped is an EXACT DILATION of both the Schrodinger and
the Dirac-Coulomb problems: r -> r/(1+eps), E -> E(1+eps).  Every
dimensionless observable of that model is unchanged to all orders.  --verify
shows the m-dependence factors out of both radial systems exactly; the selftest
checks E_n propto m and <r> propto 1/m in exact rationals.

What remains: m_p/m_e through K_mu = 7(S-1)/9 (H1) or S-1 (H2), asked of
address.K_mu; under H1 alpha also moves (address.py W11).  Every residual shift
needs the same filling source: a chemically visible eps = 1e-2 needs the
source density this file prints.  A DOCKET 63 verifier's free-neutron
stability edge was not reproduced here and is therefore NOT STATED.

===============================================================================
6.  ROLE 3, ENERGY: DEAD
===============================================================================

T_kk = (k.grad phi)^2 >= 0 for any minimally coupled scalar, any potential, any
mass (higgs.MINIMAL_SCALAR_SATISFIES_NEC, sampled here over exact rationals
including V = 0, i.e. m_h = 0).  A vev saturates it at exactly zero.  The
phantom (ghost=True) is the control that goes negative.  The xi escape is S4
and O1, refused elsewhere: it needs phi at the GUT scale, where
xigate.xi_required = 1.48e4, and that field is 10^(4..6) times Degrassi's
instability scale 10^(11 +- 1) GeV -- a region where lambda < 0, so not an
excitation of our vacuum.

    DIVERGENCE FROM THE RULING, RECORDED.  DOCKET 63 rulings B and D (S8)
    print "2e4 to 2e5 times".  Computed across Degrassi's full band the ratio
    is 2e4 (upper edge 10^12) to 2e6 (lower edge 10^10), with 2e5 at the
    CENTRE 10^11.  The ruling's range is the upper edge to the centre: it
    covers half of Degrassi's band (in log10), and its "2e5" is the centre,
    not an edge.  XI_FIELD_OVER_INSTABILITY_UPPER_EDGE, _CENTRE and
    _LOWER_EDGE expose the three values; RULING_S8_COVERS_FRACTION_OF_BAND
    is computed.  Nothing turns on it -- every value is far above the scale.

===============================================================================
7.  WHAT THE THREE SHARE, AND W9
===============================================================================

The headline mechanisms of roles 2 and 3 die of theorems that never use the
Higgs mass (the dilation; T_kk a square).  What is left of roles 1 and 2 dies
of ONE mechanism, ultralocality: every effect of delta phi arrives with a source
whose own effects are larger -- its gravity for role 1, its medium for role 2.
A bigger budget makes role 1 worse, by the domination theorem.

W9, WITHDRAWN.  The orchestrator's dichotomy ("uniform and useless, or
localised and screened, nothing in between") fell because (a) a third case,
the filling medium, is banked; (b) role 3 dies at m_h = 0 too; (c) phi = 0 is a
spinodal maximum with an e-fold of ~7.44e-27 s, not 3.34 ns; (d) its figures
were computed at m_h = 125.25.  The six counts of its hypothesis are
endpoint.ORCHESTRATOR_HYPOTHESIS_FAILURES, imported, not copied.

===============================================================================
8.  WHAT THIS FILE REFUSES, AND WHY
===============================================================================

   1. ONE PRICE FOR AN ADDRESS.  Cost is printed only as a function of eps,
      source species and hypothesis.  A single headline would be the most
      quotable false line in the tree.
   2. CALLING ANY SOURCE COST A LOWER BOUND.  Higgs quanta decay in ~1e-22 s
      and portal scalars are BSM; the computation covers stable sources with
      m propto phi only.
   3. CHOOSING BETWEEN H1 AND H2 (address.H1_VS_H2_IS_REFUSED).
   4. THE WORD "RANGE" WITHOUT A QUALIFIER.  TAIL_RATE (source-independent) is
      printed separately from STANDOFF = lambda_h ln(eps_0/eps_det), which
      grows as ln(rho).
   5. A THEOREM LABEL ON ANY METRE FIGURE.  Those inherit their input's status.
   6. MORE THAN ONE SIGNIFICANT FIGURE FROM Gamma_h, and calling the driven
      ceiling a standing displacement: it needs a coherent 125 GeV source that
      nothing in the tree specifies.
   7. ANY COLLAPSE TIME OTHER THAN THE SPINODAL E-FOLD.  There is no false
      vacuum at phi = 0 and no 3+1 release has been computed.
   8. eps = 1e-18 AS A CAPABILITY.  It is an ORDER, not a measurement.
   9. TOTALS OR RANKINGS ACROSS ROLES.
  10. SEATING ANY /tmp FIGURE.  Everything is re-derived or left out.
  11. THE WORD "CORE" FOR A SOURCELESS DEEP PROFILE.  The blow-up radius is
      reported instead.
  12. TREATING THE DRIVE PDFs AS CORROBORATION:
      warpfolder.CONVERGENCE_IS_CORROBORATION, imported, is False.

===============================================================================
9.  WHAT IS NOT SETTLED
===============================================================================

DOCKET 63 ruling section E carries thirteen open questions and what would close
each: the cheapest stable static source with Pauli degeneracy; a self-consistent
fermion bag; whether a finite-density source reaches f = -2.45; the in-medium
massless point eps = 1 - 1/sqrt(3); evanescent reach with Gamma(omega); the
sign convention of xi R phi^2 (the break-even xi = f (M_red/v)^2 is printed,
its sign is NOT settled); a 3+1 release of a phi = 0 region; a hot symmetric
region; endpoint.py's E1, E3a, E3; the Yukawa-running correction to 2/9;
macroscopic gauged configurations; H1 against H2; a BSM light scalar.  None is
answered here and none is quoted as answered.

STATUSES.  D15, D16, D18, D19 are THEOREMs on their named hypotheses.  Every
metre, second and kg/m^3 figure is COMPUTED from READ or NAMED-NOT-READ inputs
and carries its input's status: every figure through v inherits G_F's
NAMED-NOT-READ.  m_h is READ: on M's ruling (DOCKET 63 F2) higgs.M_HIGGS IS the
capture's 125.13, and the withdrawn pin 125.20 is kept only as a record, printed
beside it and never used for a live figure.

NOTHING IS REPAIRED.
"""

import inspect
import math
import re
import sys
from decimal import Decimal
from fractions import Fraction

import higgs
import xigate
import endpoint
import address
import pdgcapture
import warpfolder

# ---------------------------------------------------------------------------
# IMPORTED, NEVER COPIED.  Every name the ruling's section C lists, asked of
# its owner by module attribute.  The selftest checks with `inspect` that each
# callable is defined in the module it is imported from, i.e. that nothing
# here is a local re-implementation carrying an owner's name.
# ---------------------------------------------------------------------------
IMPORTS = (
    ("higgs", ("vev", "lam", "v_min_gev4", "gev4_to_si", "reduced_planck_gev",
               "xi_required", "nec_scalar", "M_HIGGS", "HBAR", "c", "G",
               "GEV_IN_J", "MINIMAL_SCALAR_SATISFIES_NEC")),
    ("xigate", ("xi_required",)),
    ("endpoint", ("yukawa_range_m", "cost_fraction", "GEVINV_TO_M",
                  "R_PROTON", "DEGRASSI_LOG10_LI", "DEGRASSI_LOG10_LI_ERR")),
    ("address", ("source_density", "source_to_field_ratio", "dln_mp_dln_v",
                 "dln_lambda_dln_v", "K_mu", "S_SCAN", "domination_ratio",
                 "detection_standoff", "eps_from_matter", "RHO_NUCLEAR")),
    ("pdgcapture", ("read", "verify")),
    ("warpfolder", ("CONVERGENCE_IS_CORROBORATION",)),
)
_MODS = {"higgs": higgs, "xigate": xigate, "endpoint": endpoint,
         "address": address, "pdgcapture": pdgcapture,
         "warpfolder": warpfolder}

HBAR = higgs.HBAR
C = higgs.c
G = higgs.G
GEV_IN_J = higgs.GEV_IN_J

# ---------------------------------------------------------------- READ inputs
PDGID = {"H0": 25, "W+": 24, "Z0": 23, "c": 4, "b": 5, "t": 6}


def _capture_rows():
    """{pdgid: row} for the six rows this file reads, via pdgcapture.read()."""
    want = set(PDGID.values())
    rows = {int(r["pdgid"]): r for r in pdgcapture.read()
            if int(r["pdgid"]) in want}
    if set(rows) != want:
        raise LookupError("capture is missing %s" % sorted(want - set(rows)))
    return rows


def _capture_lines():
    """{pdgid: 1-based line number} of those rows in captures/PDG-2026.tsv.

    Measured from the file, so a citation 'PDG-2026.tsv:307' is checked, not
    trusted."""
    want = set(PDGID.values())
    out = {}
    with open(pdgcapture.OUT, encoding="utf-8") as fh:
        for n, ln in enumerate(fh, 1):
            if ln.startswith("#"):
                continue
            head = ln.split("\t", 1)[0]
            if head.lstrip("-").isdigit() and int(head) in want:
                out[int(head)] = n
    return out


_ROWS = _capture_rows()
M_H_READ_GEV = float(_ROWS[25]["mass_MeV"]) / 1000.0          # READ
GAMMA_H_READ_GEV = float(_ROWS[25]["width_MeV"]) / 1000.0     # READ
M_W_READ_GEV = float(_ROWS[24]["mass_MeV"]) / 1000.0          # READ
M_Z_READ_GEV = float(_ROWS[23]["mass_MeV"]) / 1000.0          # READ
M_C_READ_GEV = float(_ROWS[4]["mass_MeV"]) / 1000.0           # READ
M_B_READ_GEV = float(_ROWS[5]["mass_MeV"]) / 1000.0           # READ
M_T_READ_GEV = float(_ROWS[6]["mass_MeV"]) / 1000.0           # READ
CAPTURE_LINES = _capture_lines()

#: The withdrawn pin 125.20 (NAMED-NOT-READ) is kept as a record beside the
#: READ value.  higgs.M_HIGGS IS the READ 125.13 since M's ruling, and the
#: selftest's drift guard (inverted) fires if it is ever re-pinned.
M_HIGGS_PIN_GEV = higgs.M_HIGGS_PIN_WITHDRAWN                 # the withdrawn pin, kept as a record

STATUS = {
    "m_h READ, Gamma_h, m_W, m_Z, m_c, m_b, m_t": "READ captures/PDG-2026.tsv",
    "higgs.M_HIGGS = 125.13 (READ); the withdrawn pin 125.20": "READ; the pin NAMED-NOT-READ, a record",
    "v = higgs.vev() from G_F": "COMPUTED from G_F, which is NAMED-NOT-READ",
    "c, hbar, G": "carried from ladder through higgs",
    "eps = 1e-18": "ORDER -- a fixture, never a capability",
    "every metre / second / kg m^-3 figure": "COMPUTED; inherits its inputs",
}

# ---------------------------------------------------------------- the fixture
#: address.py section 7's clock comparison.  ORDER, not a measurement and not a
#: capability (refusal 8).  eps follows from it through address's courier
#: coefficient, which is exactly 1.
CLOCK_ACCURACY_FIXTURE = 1e-18                                  # ORDER
EPS_AT_FIXTURE = address.eps_detectable_transported(CLOCK_ACCURACY_FIXTURE)
#: S = 0.06, address.S_SCAN's sigma_piN row -- a scanned input (ORDER) there.
S_MID = address.S_SCAN[1][1]
HYPOTHESES = ("H1", "H2")

#: rho_EW = |V_min|, J/m^3, asked of higgs.py.
RHO_EW = abs(higgs.gev4_to_si(higgs.v_min_gev4()))


# ===================================================================== algebra
# Polynomials as coefficient lists, lowest order first, over Fraction.  This is
# what makes the selftest's identities PROOFS on the polynomial ring rather than
# samples.
def _trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def padd(a, b):
    n = max(len(a), len(b))
    return _trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                  for i in range(n)])


def pscale(a, s):
    return _trim([s * x for x in a])


def pmul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return _trim(out)


def pderiv(a):
    return _trim([i * a[i] for i in range(1, len(a))] or [Fraction(0)])


def pcompose(a, b):
    """a(b(t))."""
    out = [Fraction(0)]
    for coef in reversed(a):
        out = padd(pmul(out, b), [coef])
    return out


def peval(a, t):
    s = 0
    for coef in reversed(a):
        s = s * t + coef
    return s


def P(*coefs):
    return _trim([Fraction(x) for x in coefs])


def mexican_hat(lam_, v_):
    """V(phi) = (lam/4)(phi^2 - v^2)^2 as a polynomial in phi."""
    return pscale(pmul(P(-v_ * v_, 0, 1), P(-v_ * v_, 0, 1)),
                  Fraction(lam_) / 4)


# ===================================================== 1. the reduced equation
def reduced_identity(lam_=Fraction(1), v_=Fraction(1), c_red=None):
    """(residual polynomial in f, c, m^2 / (lam v^2)).

    V'(v(1+f))/(lam v^3) must equal f(f+1)(f+2) and m^2 = V''(v) = 2 lam v^2,
    so in x = m r the reduced right-hand side is c f(f+1)(f+2) with
    c = lam v^2/m^2 = 1/2.  Pass c_red to test a different quartic
    coefficient (the CONTROL: 1/3 must leave a nonzero residual).
    """
    V = mexican_hat(lam_, v_)
    dV = pderiv(V)
    m2 = peval(pderiv(dV), v_)                           # V''(v)
    phi_of_f = P(v_, v_)                                 # v(1 + f)
    lhs = pscale(pcompose(dV, phi_of_f), 1 / (lam_ * v_ ** 3))
    target = pmul(pmul(P(0, 1), P(1, 1)), P(2, 1))       # f(f+1)(f+2)
    c = (lam_ * v_ * v_) / m2 if c_red is None else Fraction(c_red)
    # reduced: grad_x^2 f = (V'/v)/m^2 = (lam v^2/m^2) * lhs
    rhs_true = pscale(lhs, lam_ * v_ * v_ / m2)
    resid = padd(pscale(target, c), pscale(rhs_true, -1))
    return resid, c, m2 / (lam_ * v_ * v_), padd(lhs, pscale(target, -1))


def q_polynomial():
    """q(f) = c (f+1)(f+2): the u'' = q u coefficient, with c = 1/2."""
    _, c, _, _ = reduced_identity()
    return pscale(pmul(P(1, 1), P(2, 1)), c)


def u_substitution_holds(fpoly):
    """x(f'' + 2f'/x) == (x f)'' as polynomials in x, for a polynomial f."""
    x = P(0, 1)
    lhs = padd(pmul(x, pderiv(pderiv(fpoly))), pscale(pderiv(fpoly), 2))
    rhs = pderiv(pderiv(pmul(x, fpoly)))
    return padd(lhs, pscale(rhs, -1)) == [0]


def riccati_identity_holds(upoly, xs):
    """w' == w^2 - u''/u for w = -u'/u, exactly at rational points."""
    du, ddu = pderiv(upoly), pderiv(pderiv(upoly))
    for x in xs:
        u, u1, u2 = peval(upoly, x), peval(du, x), peval(ddu, x)
        if u == 0:
            continue
        w = -u1 / u
        wprime = -(u2 * u - u1 * u1) / (u * u)
        if wprime != w * w - u2 / u:
            return False
    return True


def riccati_escape(w0, q=1.0, h=1e-3, xmax=60.0):
    """Integrate w' = w^2 - q from w(0) = w0 by RK4.  ('blowup'|'zero'|'stays',
    x).  A start above sqrt(q) blows up and one below reaches zero, both at
    finite x -- step (v) of the proof, as a control that must fire both ways.
    """
    x, w = 0.0, w0

    def F(w):
        return w * w - q
    while x < xmax:
        if w > 1e6:
            return "blowup", x
        if w <= 0.0:
            return "zero", x
        k1 = F(w)
        k2 = F(w + h / 2 * k1)
        k3 = F(w + h / 2 * k2)
        k4 = F(w + h * k3)
        w += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
    return "stays", x


# ------------------------------------------------ the boundary-value witness
def bvp_solve(f0, X, mu2=1.0, linear=False, x0=5.0, h=0.01, tol=1e-13,
              maxit=200):
    """Solve u'' = g(x, u), u = x f, on [x0, X] with u(x0) = x0 f0, u(X) = 0.

    g = mu2 * u * q(u/x) for the reduced equation at mass sqrt(mu2) (mu2 = 1 is
    the Higgs, 0 is massless, 4 and 9 are the mass-2 and mass-3 controls);
    g = mu2 * u when linear.  Numerov (O(h^4)) discretisation, Newton with a
    damped step, Thomas tridiagonal solve.  STDLIB.  THE ONLY CONDITION AT THE
    FAR END IS f(X) = 0: no tail shape is assumed and no rate imposed.
    Returns (xs, us, iterations, h).
    """
    qp = q_polynomial()
    q1, q2 = float(qp[1]), float(qp[2])
    N = int(round((X - x0) / h))
    h = (X - x0) / N
    xs = [x0 + i * h for i in range(N + 1)]

    def g(x, u):
        if linear:
            return mu2 * u
        f = u / x
        return mu2 * u * (1.0 + q1 * f + q2 * f * f)

    def dg(x, u):
        if linear:
            return mu2
        f = u / x
        return mu2 * (1.0 + 2.0 * q1 * f + 3.0 * q2 * f * f)

    k = math.sqrt(mu2)
    u0 = x0 * f0
    us = [u0 * math.exp(-k * (x - x0)) * (X - x) / (X - x0) for x in xs]
    us[0], us[-1] = u0, 0.0
    cN = h * h / 12.0

    def resid(vs):
        gs = [g(x, u) for x, u in zip(xs, vs)]
        return [vs[i - 1] - 2.0 * vs[i] + vs[i + 1]
                - cN * (gs[i - 1] + 10.0 * gs[i] + gs[i + 1])
                for i in range(1, N)]

    R = resid(us)
    rn = max(abs(r) for r in R)
    n = N - 1
    for it in range(maxit):
        dgs = [dg(x, u) for x, u in zip(xs, us)]
        a = [1.0 - cN * dgs[i - 1] for i in range(1, N)]
        b = [-2.0 - 10.0 * cN * dgs[i] for i in range(1, N)]
        cc = [1.0 - cN * dgs[i + 1] for i in range(1, N)]
        cp, dp = [0.0] * n, [0.0] * n
        cp[0], dp[0] = cc[0] / b[0], -R[0] / b[0]
        for i in range(1, n):
            m = b[i] - a[i] * cp[i - 1]
            cp[i] = cc[i] / m
            dp[i] = (-R[i] - a[i] * dp[i - 1]) / m
        dx = [0.0] * n
        dx[-1] = dp[-1]
        for i in range(n - 2, -1, -1):
            dx[i] = dp[i] - cp[i] * dx[i + 1]
        damp = 1.0
        while True:
            trial = us[:]
            for i in range(n):
                trial[i + 1] = us[i + 1] + damp * dx[i]
            R2 = resid(trial)
            rn2 = max(abs(r) for r in R2)
            if rn2 < rn or damp < 1e-6:
                break
            damp *= 0.5
        us, R, rn = trial, R2, rn2
        if (max(abs(v) for v in dx) * damp
                <= tol * max(1.0, max(abs(v) for v in us))):
            return xs, us, it + 1, h
    raise RuntimeError("bvp_solve: no convergence at f0=%g (residual %g)"
                       % (f0, rn))


def measured_rate(xs, us, h, xq):
    """w = -u'/u at xq, fourth-order central difference."""
    i = int(round((xq - xs[0]) / h))
    up = (us[i - 2] - 8.0 * us[i - 1] + 8.0 * us[i + 1] - us[i + 2]) / (12.0 * h)
    return -up / us[i]


#: The six f(5) the ruling names, and the tail amplitudes they come from
#: (u = A e^{-x}); tail_to_f5() re-derives the four that have an A.
F5_AMPLITUDES = (-1e-6, -0.127814, -0.877854, -1.585710, -2.448516, 50.0)
TAIL_A_FOR_F5 = ((-1e2, -0.127814), (-1e3, -0.877854), (-3e3, -1.585710),
                 (-1e4, -2.448516))
RATE_POINTS = (15.0, 20.0, 25.0)
BOXES = (40.0, 50.0, 60.0, 70.0)


def _rk4_inward(x, u, p, xend, linear=False, fmax=1e8):
    """Integrate u'' = q u inward from (x, u, u') towards xend.

    Returns ('blowup', x) when |f| passes fmax, else ('reached', (x, u, u')).
    The step shrinks as 1/sqrt|q| so the approach to a blow-up is resolved."""
    qp = q_polynomial()
    q1, q2 = float(qp[1]), float(qp[2])

    def F(x, y):
        f = y[0] / x
        q = 1.0 if linear else 1.0 + q1 * f + q2 * f * f
        return (y[1], y[0] * q)
    y = (u, p)
    while x > xend:
        f = y[0] / x
        if abs(f) > fmax:
            return "blowup", x
        q = abs(1.0 if linear else 1.0 + q1 * f + q2 * f * f)
        hs = -min(1e-3, 0.02 / math.sqrt(max(q, 1e-30)), 0.01 * x)
        hs = max(hs, xend - x)
        k1 = F(x, y)
        k2 = F(x + hs / 2, (y[0] + hs / 2 * k1[0], y[1] + hs / 2 * k1[1]))
        k3 = F(x + hs / 2, (y[0] + hs / 2 * k2[0], y[1] + hs / 2 * k2[1]))
        k4 = F(x + hs, (y[0] + hs * k3[0], y[1] + hs * k3[1]))
        y = (y[0] + hs / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
             y[1] + hs / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]))
        x += hs
    return "reached", (x, y[0], y[1])


def tail_to_f5(A, x_tail=30.0):
    """f(5) of the tail u = A e^{-x}, shot inward from x_tail by RK4."""
    st, val = _rk4_inward(x_tail, A * math.exp(-x_tail),
                          -A * math.exp(-x_tail), 5.0)
    return val[1] / 5.0 if st == "reached" else None


def blowup_radius_from_bvp(f0, X=40.0, linear=False):
    """Integrate the boundary-value solution inward from x = 5.02.  Returns the
    blow-up radius, or None when the profile reaches x = 1e-3 finite.  THIS IS
    WHAT IS REPORTED IN PLACE OF A 'CORE' (refusal 11)."""
    xs, us, _it, h = bvp_solve(f0, X, linear=linear)
    i = 2
    up = (us[i - 2] - 8.0 * us[i - 1] + 8.0 * us[i + 1] - us[i + 2]) / (12.0 * h)
    st, val = _rk4_inward(xs[i], us[i], up, 1e-3, linear=linear)
    return val if st == "blowup" else None


def blowup_radius_from_tail(A):
    st, val = _rk4_inward(30.0, A * math.exp(-30.0), -A * math.exp(-30.0), 1e-3)
    return val if st == "blowup" else None


# ------------------------------------------------------------- the exact kink
def kink_identity():
    """f = t - 1 with t = tanh(x/2), dt/dx = (1 - t^2)/2.  Returns (residual of
    f'' - (1/2) f(f+1)(f+2), residual of -f' - rate*f with rate = (1+t)/2,
    rate at t = 1).  All polynomials in t over Fraction.  REAL Z2 TOY ONLY."""
    dtdx = P(Fraction(1, 2), 0, Fraction(-1, 2))

    def ddx(p):
        return pmul(pderiv(p), dtdx)
    f = P(-1, 1)
    f1 = ddx(f)
    f2 = ddx(f1)
    _, c, _, _ = reduced_identity()
    rhs = pscale(pmul(pmul(f, padd(f, P(1))), padd(f, P(2))), c)
    rate = P(Fraction(1, 2), Fraction(1, 2))
    r1 = padd(f2, pscale(rhs, -1))
    r2 = padd(pscale(f1, -1), pscale(pmul(rate, f), -1))
    return r1, r2, peval(rate, 1)


# ---------------------------------------------------------- the multipoles
def k_l_poly(l):
    """k_l(x) = e^{-x} p_l(y), y = 1/x, p_l(y) = sum_j (l+j)!/(j!(l-j)!)
    (y/2)^j * y.  The modified spherical Bessel function of the second kind,
    up to normalisation."""
    coefs = [Fraction(0)] * (l + 2)
    for j in range(l + 1):
        coefs[j + 1] = Fraction(math.factorial(l + j),
                                math.factorial(j) * math.factorial(l - j)
                                * 2 ** j)
    return _trim(coefs)


def _Dx(p):
    """d/dx of e^{-x} p(y), y = 1/x, written as e^{-x} D[p](y):
    D[p] = -p - y^2 p'(y)."""
    return padd(pscale(p, -1), pscale(pmul(P(0, 0, 1), pderiv(p)), -1))


def multipole_residual(l, ll=None):
    """R'' + 2R'/x - l(l+1) R/x^2 - R, as e^{-x} times a polynomial in y.
    [0] means exact.  ll overrides l(l+1) for the CONTROL."""
    ll = l * (l + 1) if ll is None else ll
    p = k_l_poly(l)
    d1 = _Dx(p)
    d2 = _Dx(d1)
    out = padd(d2, pmul(P(0, 2), d1))
    out = padd(out, pscale(pmul(P(0, 0, 1), p), -ll))
    return padd(out, pscale(p, -1))


def multipole_rate(l, y):
    """-R'/R = -D[p]/p at y = 1/x, exact."""
    p = k_l_poly(l)
    return -peval(_Dx(p), y) / peval(p, y)


# ================================================ 2. ultralocality (D16)
def green_integral(m, rmax_in_ranges=60.0, n=200001):
    """INT_0^inf r e^{-m r} dr by Simpson -- the numeric side of 1/m^2."""
    rmax = rmax_in_ranges / m
    h = rmax / (n - 1)
    s = 0.0 + rmax * math.exp(-m * rmax)
    for i in range(1, n - 1):
        r = i * h
        s += (4.0 if i % 2 else 2.0) * r * math.exp(-m * r)
    return s * h / 3.0


def cosine_response_ratio(lam_over_L):
    """Exact response / algebraic response for J = cos(x/L): 1/(1 + s^2)."""
    s = lam_over_L * lam_over_L
    return 1 / (1 + s)


def cosine_response_error(lam_over_L):
    """Fractional error of delta phi = -J/m^2 for J = cos(x/L), EXACT, written
    s^2/(1 + s^2) rather than 1 - 1/(1 + s^2): the second form cancels
    catastrophically in double precision once s^2 < 1e-16 (higgs.py's
    channel, a third time).  The selftest checks the two agree over Fraction."""
    s = lam_over_L * lam_over_L
    return s / (1 + s)


# ================================================ 3. the holding cost (D20)
def _holding_polys():
    """(source, field) as polynomials in eps, in units of rho_EW, DERIVED.

    lam = v = 1 without loss (both terms are homogeneous in lam v^4, which is
    rho_EW up to the 1/4 divided out).  phi = 1 - eps.
    """
    V = mexican_hat(1, 1)
    dV = pderiv(V)
    rho = peval(V, 0) - peval(V, 1)                      # |V_min| = 1/4
    phi = P(1, -1)
    source = pscale(pmul(pscale(pcompose(dV, phi), -1), phi), 1 / rho)
    field = pscale(padd(pcompose(V, phi), [-peval(V, 1)]), 1 / rho)
    return source, field


SOURCE_POLY, FIELD_POLY = _holding_polys()
TOTAL_POLY = padd(SOURCE_POLY, FIELD_POLY)
#: the ruling's closed forms, as FIXTURES the derivation must reproduce
SOURCE_CLOSED = pscale(pmul(pmul(P(0, 1), P(2, -1)), pmul(P(1, -1), P(1, -1))),
                       4)
FIELD_CLOSED = pmul(pmul(P(0, 1), P(0, 1)), pmul(P(2, -1), P(2, -1)))


def holding_terms(eps):
    """(source, field) at eps in units of rho_EW.  Exact over Fraction."""
    return peval(SOURCE_POLY, eps), peval(FIELD_POLY, eps)


def holding_ratio(eps):
    s, f = holding_terms(eps)
    return s / f


def _quadratic_roots(p):
    a, b, c = p[2], p[1], p[0]
    disc = b * b - 4 * a * c
    r = math.sqrt(disc)
    return sorted(((-b - r) / (2 * a), (-b + r) / (2 * a)))


def stability_edge():
    """eps where V''(v(1-eps)) = 0 in (0, 1): 1 - 1/sqrt(3).  From the
    polynomial, not typed."""
    V = mexican_hat(1, 1)
    d2 = pcompose(pderiv(pderiv(V)), P(1, -1))
    return [float(r) for r in _quadratic_roots(d2) if 0 < r < 1][0]


def source_equals_field():
    """eps in (0, 1) where source = field: 1 - 1/sqrt(5).  The difference is
    eps(2 - eps) times a quadratic; the quadratic is divided out exactly."""
    diff = padd(SOURCE_POLY, pscale(FIELD_POLY, -1))
    # divide by eps(2 - eps) = 2 eps - eps^2
    div = P(0, 2, -1)
    quo = [Fraction(0)] * (len(diff) - len(div) + 1)
    rem = list(diff)
    for k in range(len(quo) - 1, -1, -1):
        quo[k] = rem[k + len(div) - 1] / div[-1]
        for j, d in enumerate(div):
            rem[k + j] -= quo[k] * d
    assert _trim(rem) == [0], "eps(2-eps) does not divide source - field"
    return [float(r) for r in _quadratic_roots(_trim(quo)) if 0 < r < 1][0]


def higgs_derived_density(eps):
    """kg/m^3 of Higgs-derived mass holding eps, asked of address (linear)."""
    return address.source_density(eps, 1.0)[1]


def stable_matter_density(eps, hypothesis, S=None):
    """rho_H / f, f = address.dln_mp_dln_v(S, hypothesis)."""
    S = S_MID if S is None else S
    return address.source_density(eps, float(address.dln_mp_dln_v(S, hypothesis)))[0]


def exact_source_density(eps):
    """kg/m^3 from this file's exact source term 4 eps(2-eps)(1-eps)^2."""
    return float(peval(SOURCE_POLY, Fraction(eps))) * RHO_EW / C ** 2


#: THE LEDGER'S D20 OWNER.  address.source_density(1e-18, 1.0)[1].  MEASURED
#: in the ledger's vocabulary; COMPUTED here from G_F (NAMED-NOT-READ) and the
#: pinned m_h (NAMED-NOT-READ).
HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18 = address.source_density(EPS_AT_FIXTURE,
                                                              1.0)[1]
HOLD_STABLE_KG_M3_AT_EPS_1E18 = {h: stable_matter_density(EPS_AT_FIXTURE, h)
                                 for h in HYPOTHESES}


# ================================================ 4. role 1: the courier clock
def _redshift_coefficients():
    """(centre-vs-infinity, centre-vs-surface) coefficients of G rho R^2 in the
    interior potential of a uniform sphere, EXACT: Phi(0) = -(3/2) GM/R and
    Phi(R) - Phi(0) = GM/(2R), with M = (4/3) pi rho R^3.  In units of pi."""
    mass = Fraction(4, 3)
    return Fraction(3, 2) * mass, Fraction(1, 2) * mass


REDSHIFT_CENTRE, REDSHIFT_SURFACE = _redshift_coefficients()
SURFACE_TWIN_FACTOR = math.sqrt(REDSHIFT_CENTRE / REDSHIFT_SURFACE)


def courier_crossover_m(eps, rho, surface_twin=False):
    """R* where the source's own interior redshift equals eps."""
    k = REDSHIFT_SURFACE if surface_twin else REDSHIFT_CENTRE
    return math.sqrt(eps * C ** 2 / (float(k) * math.pi * G * rho))


COURIER_CROSSOVER_M = {
    "m propto phi": courier_crossover_m(EPS_AT_FIXTURE,
                                        HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18),
    "H1": courier_crossover_m(EPS_AT_FIXTURE,
                              HOLD_STABLE_KG_M3_AT_EPS_1E18["H1"]),
    "H2": courier_crossover_m(EPS_AT_FIXTURE,
                              HOLD_STABLE_KG_M3_AT_EPS_1E18["H2"]),
}


# ------------------------------------------------ D19: the flat directions
def _c(re, im=0):
    return (Fraction(re), Fraction(im))


def _cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def _cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def _cconj(a):
    return (a[0], -a[1])


SIGMA = {
    "T1": ((_c(0), _c(1)), (_c(1), _c(0))),
    "T2": ((_c(0), _c(0, -1)), (_c(0, 1), _c(0))),
    "T3": ((_c(1), _c(0)), (_c(0), _c(-1))),
    "Y": ((_c(1), _c(0)), (_c(0), _c(1))),
}
PYTHAGOREAN = (Fraction(3, 5), Fraction(4, 5))       # cos, sin: exactly unit


def gauge_element(gen, cs=PYTHAGOREAN):
    """U = cos I + i sin sigma (sigma^2 = I), i.e. exp(i theta sigma) with
    theta = 2 x (the half-angle in exp(i theta T)).  EXACT."""
    co, si = cs
    s = SIGMA[gen]
    I2 = ((_c(1), _c(0)), (_c(0), _c(1)))
    return tuple(tuple(_cadd(_cmul(_c(co), I2[a][b]),
                             _cmul(_c(0, si), s[a][b])) for b in range(2))
                 for a in range(2))


def _apply(U, H):
    return tuple(_cadd(_cmul(U[a][0], H[0]), _cmul(U[a][1], H[1]))
                 for a in range(2))


def hdagh(H):
    return sum(_cmul(_cconj(h), h)[0] for h in H)


def is_unitary(U):
    for a in range(2):
        for b in range(2):
            s = _cadd(_cmul(_cconj(U[0][a]), U[0][b]),
                      _cmul(_cconj(U[1][a]), U[1][b]))
            if s != _c(1 if a == b else 0):
                return False
    return True


H_SAMPLES = (((Fraction(0), Fraction(0)), (Fraction(1), Fraction(0))),
             ((Fraction(3, 7), Fraction(-2, 5)), (Fraction(11, 13), Fraction(1, 9))),
             ((Fraction(-5), Fraction(4)), (Fraction(0), Fraction(-7, 3))))


# ================================================ 5. role 2: the ruler
def hydrogen_levels(m, alpha, nmax=6):
    """E_n = -m alpha^2/(2 n^2) and <r>_{n,l} = (3n^2 - l(l+1))/(2 m alpha),
    hbar = c = 1, point nucleus of infinite mass.  EXACT over Fraction."""
    E = {n: -m * alpha * alpha / (2 * n * n) for n in range(1, nmax + 1)}
    r = {(n, l): Fraction(3 * n * n - l * (l + 1)) / (2 * m * alpha)
         for n in range(1, nmax + 1) for l in range(n)}
    return E, r


def dirac_level(m, alpha, n, kappa, Z=1):
    """Dirac-Coulomb E_{n kappa} = m [1 + (Z alpha/(n - |k| + sqrt(k^2 -
    Z^2 alpha^2)))^2]^{-1/2}.  The m-independence of E/m is the spectrum side
    of D18; the ODE side is in --verify."""
    k = abs(kappa)
    g = math.sqrt(k * k - (Z * alpha) ** 2)
    return m / math.sqrt(1.0 + (Z * alpha / (n - k + g)) ** 2)


def K_mu_rows():
    """[(label, S, K_mu H1, K_mu H2)] asked of address.K_mu."""
    return [(lab, S, address.K_mu(S, "H1"), address.K_mu(S, "H2"))
            for lab, S in address.S_SCAN]


EPS_CHEMICAL = Fraction(1, 100)     # a chemically visible displacement: a probe
HOLD_HIGGS_DERIVED_AT_CHEMICAL = address.source_density(float(EPS_CHEMICAL),
                                                        1.0)[1]


# ================================================ 6. role 3
def xi_field_over_instability():
    """xigate's GUT-scale field over Degrassi's 10^(11 +- 1) GeV: (at the upper
    edge, at the centre, at the lower edge).  COMPUTED."""
    phi = xigate.GUT_SCALE_GEV
    L, dL = endpoint.DEGRASSI_LOG10_LI, endpoint.DEGRASSI_LOG10_LI_ERR
    return (phi / 10 ** (L + dL), phi / 10 ** L, phi / 10 ** (L - dL))


XI_REQUIRED_AT_GUT = xigate.xi_required(xigate.GUT_SCALE_GEV)
XI_FIELD_OVER_INSTABILITY = xi_field_over_instability()
(XI_FIELD_OVER_INSTABILITY_UPPER_EDGE,          # at 10^(11+1) GeV: ~2e4
 XI_FIELD_OVER_INSTABILITY_CENTRE,              # at 10^11 GeV:     ~2e5
 XI_FIELD_OVER_INSTABILITY_LOWER_EDGE) = XI_FIELD_OVER_INSTABILITY   # ~2e6
#: DOCKET 63 rulings B and D (S8): "2e4 to 2e5 times", READ VERBATIM.  NOT the
#: seated range; the computed band is (upper edge, lower edge) above.
RULING_S8_PRINTED_RANGE = ("2e4", "2e5")


def _rounds_to_printed(x, txt):
    """Would x, rounded to txt's last printed digit, print as txt?"""
    d = Decimal(txt)
    return abs(x - float(d)) <= 0.5 * float(Decimal(1).scaleb(d.as_tuple().exponent))


def ruling_s8_matches():
    """Which computed band point each of the ruling's two figures is."""
    names = ("upper edge", "centre", "lower edge")
    return tuple(tuple(nm for nm, v in zip(names, XI_FIELD_OVER_INSTABILITY)
                       if _rounds_to_printed(v, t))
                 for t in RULING_S8_PRINTED_RANGE)


def ruling_s8_band_fraction():
    """The fraction of Degrassi's band, in log10, the ruling's range spans."""
    lo, hi = (float(Decimal(t)) for t in RULING_S8_PRINTED_RANGE)
    return (math.log10(hi / lo)
            / math.log10(XI_FIELD_OVER_INSTABILITY_LOWER_EDGE
                         / XI_FIELD_OVER_INSTABILITY_UPPER_EDGE))


RULING_S8_MATCHES = ruling_s8_matches()
RULING_S8_COVERS_FRACTION_OF_BAND = ruling_s8_band_fraction()


# ================================================ 7. times and lengths
def spinodal_ratio():
    """V''(0)/V''(v) for the Mexican hat, EXACT: -1/2."""
    V = mexican_hat(1, 1)
    d2 = pderiv(pderiv(V))
    return peval(d2, 0) / peval(d2, 1)


def spinodal_efold_s(m_gev):
    """hbar/(sqrt(|V''(0)|/m^2) m c^2) = sqrt(2) hbar/(m c^2).  The only
    collapse time this file will state (refusal 7)."""
    return HBAR / (math.sqrt(float(-spinodal_ratio())) * m_gev * GEV_IN_J)


def driven_ceiling_m(m_gev, gamma_gev):
    """Penetration of a drive at omega = m through k^2 = m^2 - omega^2 - i m
    Gamma: 1/Im k = sqrt(2/(m Gamma)).  NOT a standing displacement."""
    return math.sqrt(2.0 / (m_gev * gamma_gev)) * endpoint.GEVINV_TO_M


def quantum_lifetime_s(gamma_gev):
    return HBAR / (gamma_gev * GEV_IN_J)


def one_sig(x):
    """Refusal 6: one significant figure from anything carrying Gamma_h."""
    return "%.0e" % float(Decimal(repr(x)))


def curvature_break_even(hypothesis, S=None):
    """xi = f (M_red/v)^2 = f * higgs.xi_required(v).  SIGN NOT SETTLED (E6)."""
    S = S_MID if S is None else S
    return (float(address.dln_mp_dln_v(S, hypothesis))
            * higgs.xi_required(higgs.vev()))


LAMBDA_H_PIN_M = endpoint.yukawa_range_m(M_HIGGS_PIN_GEV)      # NAMED-NOT-READ in
LAMBDA_H_READ_M = endpoint.yukawa_range_m(M_H_READ_GEV)        # READ in
TAIL_RATE_M = {"pinned 125.20": LAMBDA_H_PIN_M, "READ": LAMBDA_H_READ_M}
LAMBDA_W_READ_M = endpoint.yukawa_range_m(M_W_READ_GEV)
LAMBDA_Z_READ_M = endpoint.yukawa_range_m(M_Z_READ_GEV)
SPINODAL_EFOLD_S = {"pinned 125.20": spinodal_efold_s(M_HIGGS_PIN_GEV),
                    "READ": spinodal_efold_s(M_H_READ_GEV)}
DRIVEN_CEILING_M = driven_ceiling_m(M_H_READ_GEV, GAMMA_H_READ_GEV)
QUANTUM_LIFETIME_S = quantum_lifetime_s(GAMMA_H_READ_GEV)


# ======================================================== the exported record
#: D15.  THEOREM on hypotheses (H-a)-(H-e), section 1.
TAIL_RATE_IS_MASS = True
TAIL_RATE_HYPOTHESES = (
    "static",
    "V smooth, V'(v) = 0, V''(v) = m^2 > 0",
    "outside the support of the source",
    "f -> 0 at infinity -- the only property of the solution used",
    "nonlinear proof radial in any d; non-spherical tails by linear multipoles")
#: D16.  THEOREM on: linear regime, static, source scale L >> lambda_h.
DISPLACEMENT_IS_ULTRALOCAL = True
#: D18.
ELECTRON_MASS_IS_A_RULER = "THEOREM given alpha fixed (H2) and clamped point nuclei"
#: D19.
FLAT_DIRECTIONS_ARE_INERT = True
#: S6, S7.
ROLE1_DOMINATED_BY_OWN_SOURCE = True
ROLE2_REBINDS = False
#: The real-Z2 statements of the first screening verdict (ruling F1).
KINK_IS_Z2_TOY_ONLY = True
NOTHING_IS_REPAIRED = True

# ---------------------------------------------------------------- refusals
PRICES_AN_ADDRESS_WITH_ONE_NUMBER = False           # 1
SOURCE_COST_IS_A_LOWER_BOUND = False                # 2
CHOOSES_BETWEEN_H1_AND_H2 = False                   # 3
SAYS_RANGE_WITHOUT_QUALIFIER = False                # 4
METRE_FIGURE_IS_A_THEOREM = False                   # 5
GAMMA_H_SIGNIFICANT_FIGURES = 1                     # 6
DRIVEN_CEILING_IS_A_STANDING_DISPLACEMENT = False   # 6
STATES_A_COLLAPSE_TIME_OTHER_THAN_SPINODAL = False  # 7
EPS_1E18_IS_A_CAPABILITY = False                    # 8
TOTALS_ACROSS_ROLES = None                          # 9
SEATS_A_TMP_FIGURE = False                          # 10
CALLS_A_SOURCELESS_PROFILE_A_CORE = False           # 11
CONVERGENCE_IS_CORROBORATION = warpfolder.CONVERGENCE_IS_CORROBORATION   # 12
#: Each refusal of section 8, by its number, and the flag(s) that carry it.
REFUSAL_FLAGS = (
    (1, "PRICES_AN_ADDRESS_WITH_ONE_NUMBER"),
    (2, "SOURCE_COST_IS_A_LOWER_BOUND"),
    (3, "CHOOSES_BETWEEN_H1_AND_H2"),
    (4, "SAYS_RANGE_WITHOUT_QUALIFIER"),
    (5, "METRE_FIGURE_IS_A_THEOREM"),
    (6, "GAMMA_H_SIGNIFICANT_FIGURES"),
    (6, "DRIVEN_CEILING_IS_A_STANDING_DISPLACEMENT"),
    (7, "STATES_A_COLLAPSE_TIME_OTHER_THAN_SPINODAL"),
    (8, "EPS_1E18_IS_A_CAPABILITY"),
    (9, "TOTALS_ACROSS_ROLES"),
    (10, "SEATS_A_TMP_FIGURE"),
    (11, "CALLS_A_SOURCELESS_PROFILE_A_CORE"),
    (12, "CONVERGENCE_IS_CORROBORATION"))
#: COUNTED from the flags, not typed.
REFUSALS = len({n for n, _ in REFUSAL_FLAGS})


def _doc_section(n):
    """The text of this module docstring's numbered section n."""
    m = re.search(r"\n%d\.  [^\n]*\n=+\n(.*?)\n=+\n" % n, __doc__ or "", re.S)
    return m.group(1) if m else ""


def doc_refusal_numbers():
    """The refusal numbers section 8 of the docstring enumerates."""
    return [int(k) for k in re.findall(r"(?m)^ {2,3}(\d+)\. ", _doc_section(8))]


def doc_tail_rate_hypotheses():
    """The distinct (H-x) labels section 1 of the docstring enumerates."""
    return sorted(set(re.findall(r"\(H-([a-z])\)", _doc_section(1))))

# ---------------------------------------------------------------- W9
#: The orchestrator's hypothesis, six counts, IMPORTED from its owner.
ORCHESTRATOR_HYPOTHESIS_FAILURES = endpoint.ORCHESTRATOR_HYPOTHESIS_FAILURES
W9 = ("the orchestrator's dichotomy: a vev displacement is either uniform and "
      "useless or localised and screened, nothing in between",
      ("a third case, the filling medium, is banked (section 3)",
       "role 3 dies at m_h = 0 too (T_kk is a square for any V)",
       "phi = 0 is a spinodal maximum, e-fold %.3g s (READ m_h), not %.3g ns"
       % (SPINODAL_EFOLD_S["READ"], 1e9 / C),
       "its figures were computed at m_h = 125.25"))


# ====================================================================== report
def report():
    print(__doc__.split("=====", 1)[0].strip())
    print()
    print("=" * 79)
    print("COMPUTED")
    print("=" * 79)
    print("\n  inputs (READ from captures/PDG-2026.tsv via pdgcapture.read())")
    for lab, val, pid in (("m_h", M_H_READ_GEV, 25), ("Gamma_h", GAMMA_H_READ_GEV, 25),
                          ("m_W", M_W_READ_GEV, 24), ("m_Z", M_Z_READ_GEV, 23),
                          ("m_c", M_C_READ_GEV, 4), ("m_b", M_B_READ_GEV, 5),
                          ("m_t", M_T_READ_GEV, 6)):
        print("      %-10s %14.6f GeV   READ  PDG-2026.tsv:%d"
              % (lab, val, CAPTURE_LINES[pid]))
    print("      %-10s %14.6f GeV   NAMED-NOT-READ, WITHDRAWN -- a record, never a "
          "live figure" % ("old pin", M_HIGGS_PIN_GEV))
    print("      %-10s %14.6f GeV   COMPUTED from G_F (NAMED-NOT-READ)"
          % ("v", higgs.vev()))
    print("      %-10s %14.6e J/m^3 COMPUTED (higgs)" % ("rho_EW", RHO_EW))

    print("\n  1. D15  TAIL_RATE -- source-independent (NOT a 'range')")
    for k, val in TAIL_RATE_M.items():
        print("      hbar/(m_h c) at %-15s %14.6e m" % (k, val))
    print("      reduced equation f'' + 2f'/x = c f(f+1)(f+2), c = %s"
          % reduced_identity()[1])
    print("      q(f) = %s  (coefficients of 1, f, f^2)"
          % " , ".join(str(x) for x in q_polynomial()))
    print("      boundary-value witness, only far condition f(X) = 0, X = 70:")
    print("      %12s %14s %14s %14s   %s" % ("f(5)", "rate x=15", "x=20",
                                             "x=25", "blow-up radius"))
    for f0 in F5_AMPLITUDES:
        xs, us, _it, h = bvp_solve(f0, 70.0)
        rb = blowup_radius_from_bvp(f0)
        print("      %12.6g %14.10f %14.10f %14.10f   %s"
              % ((f0,) + tuple(measured_rate(xs, us, h, q) for q in RATE_POINTS)
                 + ("none above x=1e-3" if rb is None else "x = %.6f" % rb,)))
    xs, us, _it, h = bvp_solve(-0.5, 40.0, mu2=0.0)
    print("      CONTROL massless, X = 40: %s  = 1/(X-x)"
          % ", ".join("%.10f" % measured_rate(xs, us, h, q) for q in RATE_POINTS))
    for mu2 in (4.0, 9.0):
        xs, us, _it, h = bvp_solve(-0.5, 40.0, mu2=mu2)
        print("      CONTROL mass %g: %s" % (math.sqrt(mu2), ", ".join(
            "%.8f" % measured_rate(xs, us, h, q) for q in RATE_POINTS)))
    print("      exact kink tanh(x/2) - 1 (Z2 toy only): rate at t=1 = %s"
          % kink_identity()[2])
    print("      multipoles k_l, rate at x = 1000: %s" % ", ".join(
        "l=%d %.6f" % (l, float(multipole_rate(l, Fraction(1, 1000))))
        for l in range(6)))
    print("      (-R'/R = 1 + 1/x + ..., the 1/x being the prefactor of k_l)")

    print("\n  2. D16  ULTRALOCALITY")
    print("      INT G d^3r * m^2 at m = 1, 2, 3: %s"
          % ", ".join("%.9f" % (green_integral(m) * m * m) for m in (1.0, 2.0, 3.0)))
    for L in (1e-17, 1e-15, 1e-10, 1.0):
        print("      L = %-8.0e  exact error %.6e   address.ultralocality_error %.6e"
              % (L, cosine_response_error(LAMBDA_H_PIN_M / L),
                 address.ultralocality_error(L)))

    print("\n  3. D20  THE HOLDING COST, units of rho_EW (derived over Fraction)")
    print("      source polynomial %s" % [str(x) for x in SOURCE_POLY])
    print("      field polynomial  %s" % [str(x) for x in FIELD_POLY])
    print("      total series      %s" % [str(x) for x in TOTAL_POLY[:4]])
    print("      source/field * eps at eps = 1e-3, 1e-6: %s"
          % ", ".join("%.9f" % float(holding_ratio(Fraction(1, 10 ** k))
                                      / 10 ** k) for k in (3, 6)))
    print("      stability edge V''=0      eps = %.9f  (1 - 1/sqrt 3)"
          % stability_edge())
    print("      source = field crossover  eps = %.9f  (1 - 1/sqrt 5), unstable"
          % source_equals_field())
    print("      AT eps = %.0e (ORDER, a fixture -- never a capability):"
          % EPS_AT_FIXTURE)
    print("      %-44s %14.6e kg/m^3" % ("Higgs-derived density (address, m propto phi)",
                                        HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18))
    for hyp in HYPOTHESES:
        print("      %-44s %14.6e kg/m^3   f = %.6f"
              % ("stable matter, %s, S = %.2f" % (hyp, S_MID),
                 HOLD_STABLE_KG_M3_AT_EPS_1E18[hyp],
                 float(address.dln_mp_dln_v(S_MID, hyp))))
    print("      (priced per eps, per species, per hypothesis -- refusal 1)")

    print("\n  4. ROLE 1, ADDRESSING: DEAD")
    print("      courier-clock crossover R* = sqrt(eps c^2 / (%s pi G rho))"
          % REDSHIFT_CENTRE)
    for k, val in COURIER_CROSSOVER_M.items():
        print("      %-16s %10.4f cm   surface twin %10.4f cm"
              % (k, val * 100, val * 100 * SURFACE_TWIN_FACTOR))
    print("      surface-twin factor = sqrt(%s) = %.9f"
          % (REDSHIFT_CENTRE / REDSHIFT_SURFACE, SURFACE_TWIN_FACTOR))
    fH1 = float(address.dln_mp_dln_v(S_MID, "H1"))
    print("      STANDOFF lambda_h ln(eps_0/eps_det) outside a 1 m source, H1:")
    for rho in (1e12, 1e14, 1e16, address.RHO_NUCLEAR, 1e20):
        e0 = abs(address.eps_from_matter(rho, fH1))
        d = address.detection_standoff(e0, 1.0, EPS_AT_FIXTURE)
        print("      rho %10.3e  eps_0 %10.3e  standoff %s  gravity/Higgs %s"
              % (rho, e0, "none" if d is None else "%.4e m" % d,
                 "%.4e" % address.domination_ratio(rho, 1.0, fH1, EPS_AT_FIXTURE)))
    print("      D19: H^dagger H invariant under T1, T2, T3, Y at cos=3/5, sin=4/5")

    print("\n  5. ROLE 2, BINDING: NARROWED")
    print("      %-28s %8s %14s %14s" % ("S (address.S_SCAN)", "S", "K_mu H1",
                                        "K_mu H2"))
    for lab, S, k1, k2 in K_mu_rows():
        print("      %-28s %8.4f %14.6f %14.6f" % (lab, S, k1, k2))
    print("      a chemically visible eps = %s needs %.6e kg/m^3 Higgs-derived"
          % (EPS_CHEMICAL, HOLD_HIGGS_DERIVED_AT_CHEMICAL))
    print("      (address, linear); exact source term gives %.6e"
          % exact_source_density(EPS_CHEMICAL))

    print("\n  6. ROLE 3, ENERGY: DEAD")
    print("      minimal scalar satisfies the NEC: %s (higgs)"
          % higgs.MINIMAL_SCALAR_SATISFIES_NEC)
    print("      xi_required at the GUT scale %.3e GeV: %.6e (xigate)"
          % (xigate.GUT_SCALE_GEV, XI_REQUIRED_AT_GUT))
    print("      that field over 10^(11 +- 1) GeV: %.0e (upper edge), %.0e "
          "(centre), %.0e (lower edge)" % XI_FIELD_OVER_INSTABILITY)

    print("\n  7. TIMES AND LENGTHS")
    for k, val in SPINODAL_EFOLD_S.items():
        print("      spinodal e-fold sqrt(2) hbar/(m_h c^2) at %-14s %.6e s"
              % (k, val))
    print("      V''(0)/V''(v) = %s (exact)" % spinodal_ratio())
    print("      driven ceiling sqrt(2/(m_h Gamma_h)), READ:   %s m  (1 s.f.)"
          % one_sig(DRIVEN_CEILING_M))
    print("      quantum lifetime hbar/Gamma_h, READ:          %s s  (1 s.f.)"
          % one_sig(QUANTUM_LIFETIME_S))
    print("      W Compton length at READ m_W  %.6e m = %.6f lambda_h(READ)"
          % (LAMBDA_W_READ_M, LAMBDA_W_READ_M / LAMBDA_H_READ_M))
    print("      Z Compton length at READ m_Z  %.6e m = %.6f lambda_h(READ)"
          % (LAMBDA_Z_READ_M, LAMBDA_Z_READ_M / LAMBDA_H_READ_M))
    for hyp in HYPOTHESES:
        print("      curvature break-even xi = f (M_red/v)^2, %s: %.4e  "
              "(SIGN NOT SETTLED, E6)" % (hyp, curvature_break_even(hyp)))

    print("\n  8. W9, WITHDRAWN -- and the orchestrator's six counts (endpoint)")
    for r in W9[1]:
        print("      - %s" % r)
    for claim, why in ORCHESTRATOR_HYPOTHESIS_FAILURES:
        print("      x %s -- %s" % (claim, why))
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print("""
  Exciting the Higgs at the endpoint takes a source that fills the region, at
  every point, for as long as the displacement is wanted: the displacement
  relaxes at exactly m_h wherever the source is absent.  What it buys is
  nothing a role can use.  Addressing is dead -- the source is the better
  address.  Binding is narrowed to O(eps) inside its own source, and the m_e
  mechanism is an exact dilation.  Energy is dead by a theorem that never
  mentions the mass.
""")
    return 0


# ==================================================================== selftest
def selftest():
    import time
    t0 = time.time()
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-64s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    def chkrel(label, got, want, rtol):
        ok = got is not None and abs(got - want) <= rtol * abs(want)
        print("  [%s] %-64s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("excite.py --selftest  (stdlib only; sympy is --verify)")

    # ------------------------------------------------ 0. imports, never copies
    print("\n0. IMPORTED, NEVER COPIED")
    missing, local = [], []
    for mod, names in IMPORTS:
        m = _MODS[mod]
        for nm in names:
            if not hasattr(m, nm):
                missing.append("%s.%s" % (mod, nm))
                continue
            obj = getattr(m, nm)
            if callable(obj) and inspect.getmodule(obj) is not m:
                local.append("%s.%s" % (mod, nm))
    chk("every name ruling C lists exists in its owner", missing, [])
    chk("every imported callable is DEFINED in its owner", local, [])
    chk("xigate.xi_required is higgs.xi_required's value (one gate)",
        xigate.xi_required(1e10) == higgs.xi_required(1e10), True)
    chk("this file defines no constant named M_HIGGS, HBAR_C or G_FERMI",
        [n for n in ("M_HIGGS", "HBAR_C", "G_FERMI") if n in globals()], [])

    # ------------------------------------------------ the capture
    print("\n1. THE CAPTURE (READ)")
    chk("m_h READ, captures/PDG-2026.tsv H0", M_H_READ_GEV, 125.13)
    chk("Gamma_h READ", GAMMA_H_READ_GEV, 0.003)
    chk("m_W, m_Z READ", (M_W_READ_GEV, M_Z_READ_GEV), (80.362, 91.1879))
    chk("m_c, m_b, m_t READ", (M_C_READ_GEV, M_B_READ_GEV, M_T_READ_GEV),
        (1.273, 4.186, 172.6))
    chk("the rows sit at the lines the ruling cites (305,306,307,579-581)",
        tuple(CAPTURE_LINES[p] for p in (23, 24, 25, 4, 5, 6)),
        (305, 306, 307, 579, 580, 581))
    chk("the capture header carries the source md5 the ruling cites",
        any("e96a23be061430adc72d5b2ea5a93764" in h for h in pdgcapture.header()),
        True)
    chk("higgs.py reads the same m_h", higgs.M_HIGGS_READ_GEV, M_H_READ_GEV)
    try:
        good, msg = pdgcapture.verify()
        chk("pdgcapture.verify(): the capture agrees with a fresh derivation",
            good, True)
    except ImportError as e:     # the `particle` package is the one non-stdlib
        print("  [--] pdgcapture.verify() NOT RUN: %s" % e)
    # DRIFT GUARD, INVERTED on M's ruling (DOCKET 63 F2): higgs.M_HIGGS IS the
    # capture value now, and this fires if it is ever re-pinned to anything else.
    chk("DRIFT GUARD higgs.M_HIGGS*1000 == capture m_h (MeV)",
        higgs.M_HIGGS * 1000 == float(_ROWS[25]["mass_MeV"]), True)

    # ------------------------------------------------ 2. corpus fixtures
    print("\n2. THE CORPUS'S OWN RECORDED NUMBERS")
    # M's ruling switched m_h to the READ 125.13 (DOCKET 63 F2).  Every m_h fixture
    # below KEEPS its original literal, pinned at the withdrawn 125.20, and expects
    # it times MH**k, k the power of m_h the figure carries -- so the check still
    # fails if anything but m_h moved, or if the power is wrong.
    MH = (higgs.M_HIGGS / higgs.M_HIGGS_PIN_WITHDRAWN)
    chkrel("|V_min| = rho_EW (endpoint.py selftest)", RHO_EW, 2.476937e45 * MH ** 2, 1e-6)
    chkrel("lambda_h at the withdrawn pin 125.20 (record)",
           LAMBDA_H_PIN_M, 1.576094e-18, 1e-6)
    chkrel("lambda_h at the READ m_h (ruling A.2)", LAMBDA_H_READ_M,
           1.576976e-18, 1e-6)
    for e in (Fraction(1, 10), Fraction(1, 1000), Fraction(3, 7)):
        chk("endpoint.cost_fraction exact at %s" % e, endpoint.cost_fraction(e),
            e * e * (2 + e) ** 2)
    chk("cost_fraction is 1 at eps = -1 and 9 at eps = +1 (address.py)",
        (endpoint.cost_fraction(-1), endpoint.cost_fraction(1)), (1, 9))
    for e in (1e-6, 1e-9, 1e-12):
        chkrel("address.source_to_field_ratio * eps -> 2 at %g" % e,
               address.source_to_field_ratio(e) * e, 2.0, 1e-5)
    chkrel("3.6746e12 kg/m^3 (address.py, H2)",
           HOLD_STABLE_KG_M3_AT_EPS_1E18["H2"], 3.6746e12 * MH ** 2, 1e-4)
    chkrel("xi_required(v) (higgs.py)", higgs.xi_required(higgs.vev()),
           9.7829068836e31, 1e-9)
    chkrel("xi_required(2e16) ~ 1.48e4 (xigate.py)", XI_REQUIRED_AT_GUT,
           1.48e4, 5e-3)
    chk("d ln Lambda / d ln v = 2/9 (address.py)", address.dln_lambda_dln_v(),
        Fraction(2, 9))

    # ------------------------------------------------ 3. D15, the algebra
    print("\n3. D15 TAIL_RATE_IS_MASS -- the reduced equation, exact")
    resid, c, m2, vid = reduced_identity()
    chk("V'(v(1+f))/(lam v^3) == f(f+1)(f+2) as polynomials", vid, [0])
    chk("m^2 = V''(v) = 2 lam v^2", m2, 2)
    chk("so the reduced coefficient is c = lam v^2/m^2 = 1/2", c, Fraction(1, 2))
    chk("residual of f'' + 2f'/x = (1/2) f(f+1)(f+2) is 0", resid, [0])
    for lv in ((Fraction(3, 7), Fraction(5, 2)), (Fraction(13), Fraction(1, 9))):
        r2, c2, m22, vid2 = reduced_identity(*lv)
        chk("  and at (lam, v) = (%s, %s): identity, m^2/(lam v^2), c" % lv,
            (vid2, m22, c2), ([0], 2, Fraction(1, 2)))
    chk("CONTROL a quartic coefficient 1/3 leaves a NONZERO residual",
        reduced_identity(c_red=Fraction(1, 3))[0] != [0], True)
    qp = q_polynomial()
    chk("q = 1 + (3/2) f + (1/2) f^2 exactly", qp,
        [Fraction(1), Fraction(3, 2), Fraction(1, 2)])
    chk("q(0) = V''(v)/m^2 = 1, so the tail rate is sqrt(1) = 1 in units of m",
        peval(qp, 0), 1)
    for fp in (P(1), P(0, 1), P(3, -2, 5), P(Fraction(1, 7), 0, 0, 4, -1)):
        chk("u = x f turns f'' + 2f'/x into u''/x, f = %s" % [str(x) for x in fp],
            u_substitution_holds(fp), True)
    pts = [Fraction(k, 7) for k in range(1, 40)]
    chk("w = -u'/u obeys w' = w^2 - u''/u exactly (3 test u, 39 points)",
        all(riccati_identity_holds(up, pts)
            for up in (P(1, 2, 3), P(-4, 0, 1, 1), P(5, -1, 0, 0, 2))), True)
    chk("step (v): w' = w^2 - 1 from 1 + 1e-3 BLOWS UP at finite x",
        riccati_escape(1.0 + 1e-3)[0], "blowup")
    chk("step (v): from 1 - 1e-3 it REACHES ZERO at finite x",
        riccati_escape(1.0 - 1e-3)[0], "zero")
    chk("  and from exactly 1 it stays", riccati_escape(1.0)[0], "stays")

    print("\n4. D15 -- the boundary-value witness (only far condition f(X) = 0)")
    rates70 = {}
    for f0 in F5_AMPLITUDES:
        xs, us, it, h = bvp_solve(f0, 70.0)
        r = [measured_rate(xs, us, h, q) for q in RATE_POINTS]
        rates70[f0] = r
        chk("f(5) = %-10g rate at x=25 within 1e-8 of 1 (%d Newton its)"
            % (f0, it), abs(r[2] - 1.0) < 1e-8, True)
        chk("  and at x=15 within 2e-4 -- the deficit is the O(e^-x) tail",
            abs(r[0] - 1.0) < 2e-4, True)
    worst = 0.0
    for f0 in (-2.448516, 50.0):
        for X in BOXES[:-1]:
            xs, us, _it, h = bvp_solve(f0, X)
            worst = max(worst, max(abs(measured_rate(xs, us, h, q)
                                       - rates70[f0][k])
                                   for k, q in enumerate(RATE_POINTS)))
    chk("BOX INDEPENDENCE X = 40..70: max rate shift < 1e-10", worst < 1e-10,
        True)
    xs, us, _it, h = bvp_solve(-1.0, 70.0, linear=True)
    floor = max(abs(measured_rate(xs, us, h, q) - 1.0) for q in RATE_POINTS)
    chk("grid floor from the LINEAR equation < 1e-9", floor < 1e-9, True)
    for X in (40.0, 70.0):
        xs, us, _it, h = bvp_solve(-0.5, X, mu2=0.0)
        got = [measured_rate(xs, us, h, q) for q in RATE_POINTS]
        chk("CONTROL massless, X=%g: rate is 1/(X-x), NOT 1" % X,
            all(abs(g - 1.0 / (X - q)) < 1e-9 for g, q in zip(got, RATE_POINTS)),
            True)
    for mu in (2.0, 3.0):
        xs, us, _it, h = bvp_solve(-0.5, 40.0, mu2=mu * mu)
        got = [measured_rate(xs, us, h, q) for q in RATE_POINTS]
        chk("CONTROL mass %g solve returns %g" % (mu, mu),
            all(abs(g - mu) < 1e-6 for g in got), True)
    for A, want in TAIL_A_FOR_F5:
        chkrel("the amplitude f(5) = %g is re-derived from tail A = %g"
               % (want, A), tail_to_f5(A), want, 1e-6)
    rb_bvp = blowup_radius_from_bvp(-0.127814)
    rb_tail = blowup_radius_from_tail(-1e2)
    chk("a sourceless deep profile BLOWS UP at finite radius (not a 'core')",
        rb_bvp is not None and 0.5 < rb_bvp < 1.5, True)
    chkrel("  and two independent routes agree on the radius", rb_bvp, rb_tail,
           1e-5)
    chk("CONTROL the linear equation from the same data does not blow up",
        blowup_radius_from_bvp(-0.127814, linear=True), None)

    print("\n5. D15 -- the exact kink (Z2 toy) and the multipoles")
    r1, r2, rate1 = kink_identity()
    chk("tanh(x/2) - 1 solves f'' = (1/2) f(f+1)(f+2): residual", r1, [0])
    chk("its rate is (1 + t)/2 exactly", r2, [0])
    chk("  and tends to m = 1 as t -> 1", rate1, 1)
    minus_I = gauge_element("Y", (Fraction(-1), Fraction(0)))
    H0 = H_SAMPLES[0]
    chk("in the DOUBLET -v is gauge-equivalent to +v (U = -1 in U(1)_Y)",
        (is_unitary(minus_I), _apply(minus_I, H0)
         == tuple((-a, -b) for a, b in H0)), (True, True))
    chk("so the kink is a real-Z2-toy statement", KINK_IS_Z2_TOY_ONLY, True)
    for l in range(6):
        chk("k_%d solves the radial equation exactly" % l,
            multipole_residual(l), [0])
    chk("CONTROL l^2 in place of l(l+1) leaves a residual (l = 1..5)",
        all(multipole_residual(l, ll=l * l) != [0] for l in range(1, 6)), True)
    chk("rate -R'/R -> 1: at x = 1e6 every l is within 1e-5",
        all(abs(multipole_rate(l, Fraction(1, 10 ** 6)) - 1) < Fraction(1, 10 ** 5)
            for l in range(6)), True)

    # ------------------------------------------------ D16
    print("\n6. D16 DISPLACEMENT_IS_ULTRALOCAL")
    for m in (1.0, 2.0, 3.0):
        chkrel("INT G d^3r = 1/m^2 at m = %g (Simpson)" % m,
               green_integral(m) * m * m, 1.0, 1e-9)
    # (a row "math.gamma(2) == 1" stood here: a constant, not a check; the
    #  Simpson rows above and --verify's V7 carry INT G d^3r = 1/m^2)
    for k in (10, 1000):
        s = Fraction(1, k)
        chk("cos(x/L) response error at lambda/L = 1/%d is 1 - exact ratio" % k,
            cosine_response_error(s), 1 - cosine_response_ratio(s))
    chkrel("  and its leading term is address.ultralocality_error(L)",
           float(cosine_response_error(LAMBDA_H_READ_M / 1e-15)),
           address.ultralocality_error(1e-15), 1e-4)

    # ------------------------------------------------ D20
    print("\n7. D20 THE HOLDING COST, DERIVED")
    chk("source = 4 eps(2-eps)(1-eps)^2 (derived == ruling's closed form)",
        SOURCE_POLY, SOURCE_CLOSED)
    chk("field  = eps^2 (2-eps)^2       (derived == ruling's closed form)",
        FIELD_POLY, FIELD_CLOSED)
    chk("field is endpoint.cost_fraction(-eps), exactly (3 rationals)",
        all(peval(FIELD_POLY, e) == endpoint.cost_fraction(-e)
            for e in (Fraction(1, 10), Fraction(1, 1000), Fraction(3, 7))), True)
    chk("total series coefficients 8, -16, 12", TOTAL_POLY[1:4],
        [Fraction(8), Fraction(-16), Fraction(12)])
    chk("  and the source's leading 8 is address.source_density's 8",
        SOURCE_POLY[1], 8)
    for k in (6, 9, 12):
        e = Fraction(1, 10 ** k)
        chk("source/field * eps -> 2 at eps = 1e-%d (exact, within %g)"
            % (k, 3 * float(e)), abs(holding_ratio(e) * e - 2) < 3 * e, True)
    se, cr = stability_edge(), source_equals_field()
    chkrel("stability edge V'' = 0 at 1 - 1/sqrt(3)", se,
           1 - 1 / math.sqrt(3), 1e-12)
    chkrel("source = field at 1 - 1/sqrt(5)", cr, 1 - 1 / math.sqrt(5), 1e-12)
    chk("  and that crossover lies in the UNSTABLE range", cr > se, True)
    chk("CONTROL below the crossover the source dominates (eps = 1/2)",
        holding_ratio(Fraction(1, 2)) > 1, True)
    chkrel("Higgs-derived density at eps = 1e-18 (ruling A.5)",
           HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18, 2.204772e11 * MH ** 2, 1e-6)
    chkrel("  stable matter H1 (f = 2/9 + 7S/9)",
           HOLD_STABLE_KG_M3_AT_EPS_1E18["H1"], 8.19956e11 * MH ** 2, 1e-5)
    chkrel("  stable matter H2 (f = S)", HOLD_STABLE_KG_M3_AT_EPS_1E18["H2"],
           3.67462e12 * MH ** 2, 1e-5)
    chk("  both agree with address.COURIER_SOURCE_KG_M3",
        all(abs(HOLD_STABLE_KG_M3_AT_EPS_1E18[h] / address.COURIER_SOURCE_KG_M3[h]
                - 1) < 1e-12 for h in HYPOTHESES), True)
    chk("eps comes from address's courier coefficient, exactly 1",
        EPS_AT_FIXTURE, CLOCK_ACCURACY_FIXTURE)

    # ------------------------------------------------ role 1
    print("\n8. ROLE 1 -- addressing is dead")
    chk("interior redshift coefficients 2 pi and (2/3) pi",
        (REDSHIFT_CENTRE, REDSHIFT_SURFACE), (Fraction(2), Fraction(2, 3)))
    chkrel("surface-twin factor is exactly sqrt(3)", SURFACE_TWIN_FACTOR,
           math.sqrt(3), 1e-15)
    for k, want in (("m propto phi", 3.118e-2), ("H1", 1.617e-2),
                    ("H2", 0.764e-2)):
        chkrel("courier crossover, %s (ruling B)" % k,
               COURIER_CROSSOVER_M[k], want, 2e-3)
    fH1 = float(address.dln_mp_dln_v(S_MID, "H1"))
    rhos = (1e12, 1e14, 1e16, 1e18, 1e20, 1e22)
    dom = [address.domination_ratio(r, 1.0, fH1, EPS_AT_FIXTURE) for r in rhos]
    # Two regimes, both recorded: just above threshold (1e12 is barely over
    # the 8.2e11 H1 hold) d -> 0 and the ratio is large for that reason; from
    # there on sqrt(rho) beats ln(rho) and it grows without bound.
    chk("address.domination_ratio grows monotonically with rho from 1e14",
        all(b > a for a, b in zip(dom[1:], dom[2:])), True)
    chk("  and just above threshold it is large too (d -> 0 there)",
        dom[0] > dom[1], True)
    chk("  gravity out-reads the Higgs by more than 1e20 everywhere scanned",
        min(dom) > 1e20, True)
    ds = [address.higgs_range(r, fH1, EPS_AT_FIXTURE) for r in rhos]
    chk("CONTROL the Higgs standoff itself does grow (so r/d is not d = 0)",
        all(b > a > 0 for a, b in zip(ds, ds[1:])), True)
    chk("STANDOFF grows as ln rho: equal steps per decade (to 1e-3)",
        max(abs((ds[i + 1] - ds[i]) - (ds[1] - ds[0])) for i in range(len(ds) - 1))
        < 1e-3 * (ds[1] - ds[0]), True)
    for gen in ("T1", "T2", "T3", "Y"):
        U = gauge_element(gen)
        chk("D19 %s at (3/5, 4/5): unitary, H^dagger H invariant (3 H)" % gen,
            (is_unitary(U), all(hdagh(_apply(U, H)) == hdagh(H) for H in H_SAMPLES)),
            (True, True))
    e = Fraction(1, 1000)
    chk("CONTROL a radial displacement (1+eps)H DOES change H^dagger H",
        all(hdagh(tuple(((1 + e) * a, (1 + e) * b) for a, b in H)) == (1 + e) ** 2 * hdagh(H)
            and hdagh(H) != 0 for H in H_SAMPLES), True)

    # ------------------------------------------------ role 2
    print("\n9. ROLE 2 -- the ruler (D18) and what remains")
    alpha = Fraction(address.ALPHA_EM)
    m0 = Fraction(1)
    E0, r0 = hydrogen_levels(m0, alpha)
    for eps in (Fraction(1, 10), Fraction(-3, 7), Fraction(1, 10 ** 18)):
        E1, r1 = hydrogen_levels(m0 * (1 + eps), alpha)
        chk("Schrodinger m -> m(1+%s): E_n scale by (1+eps), <r> by 1/(1+eps)"
            % eps, (all(E1[n] == E0[n] * (1 + eps) for n in E0),
                    all(r1[k] == r0[k] / (1 + eps) for k in r0)), (True, True))
        chk("  so every E_n/E_1 and <r>*E_1 is unchanged, exactly",
            (all(E1[n] / E1[1] == E0[n] / E0[1] for n in E0),
             all(r1[k] * E1[1] == r0[k] * E0[1] for k in r0)), (True, True))
    a = address.ALPHA_EM
    ratios = [dirac_level(2.0, a, n, k) / dirac_level(1.0, a, n, k)
              for n, k in ((1, -1), (2, -1), (2, 1), (2, -2), (3, 2))]
    chk("Dirac-Coulomb E_{n kappa}(2m) / E(m) = 2 to rounding",
        all(abs(r - 2.0) < 1e-15 for r in ratios), True)
    chk("CONTROL m_p/m_e DOES move: K_mu(S) != 0 in both hypotheses",
        all(k1 != 0 and k2 != 0 for _l, _S, k1, k2 in K_mu_rows()), True)
    for S in (Fraction(0), Fraction(6, 100), Fraction(9, 100), Fraction(1)):
        chk("K_mu(S) = 7(S-1)/9 (H1), S-1 (H2) exactly at S = %s" % S,
            (address.K_mu(S, "H1"), address.K_mu(S, "H2")),
            (Fraction(7, 9) * (S - 1), S - 1))
    chkrel("K_mu H1 at S = 0.06 (ruling B)", float(address.K_mu(S_MID, "H1")),
           -0.731111, 1e-6)
    chkrel("K_mu H2 at S = 0.06", float(address.K_mu(S_MID, "H2")), -0.94, 1e-12)
    chkrel("eps = 1e-2 needs 2.204772e27 kg/m^3 Higgs-derived (address)",
           HOLD_HIGGS_DERIVED_AT_CHEMICAL, 2.204772e27 * MH ** 2, 1e-6)
    chk("  and the exact source term asks slightly less (1-eps)^2(1-eps/2)",
        abs(exact_source_density(EPS_CHEMICAL)
            / HOLD_HIGGS_DERIVED_AT_CHEMICAL
            - float((1 - EPS_CHEMICAL) ** 2 * (1 - EPS_CHEMICAL / 2))) < 1e-12,
        True)
    chk("ROLE2_REBINDS", ROLE2_REBINDS, False)

    # ------------------------------------------------ role 3
    print("\n10. ROLE 3 -- energy is dead")
    import random
    rnd = random.Random(630063)
    neg = 0
    for _ in range(300):
        d = tuple(Fraction(rnd.randrange(-400, 401), 50) for _ in range(4))
        V = rnd.choice((Fraction(0), Fraction(rnd.randrange(-10 ** 12, 10 ** 12), 3)))
        q = higgs.QUADS[rnd.randrange(len(higgs.QUADS))]
        if higgs.nec_scalar(d, V, q) < 0:
            neg += 1
    chk("higgs.nec_scalar >= 0 on 300 exact configs, V = 0 (m_h = 0) among them",
        neg, 0)
    chk("CONTROL nec_scalar(ghost=True) goes negative",
        higgs.nec_scalar((Fraction(3), Fraction(0), Fraction(0), Fraction(0)),
                         Fraction(0), higgs.QUADS[0], ghost=True) < 0, True)
    chk("owner of S8/D17", higgs.MINIMAL_SCALAR_SATISFIES_NEC, True)
    lo, mid, hi = XI_FIELD_OVER_INSTABILITY
    chkrel("GUT field / instability scale, centre 10^11", mid, 2e5, 1e-12)
    chkrel("  at the upper edge 10^12", lo, 2e4, 1e-12)
    chkrel("  at the lower edge 10^10", hi, 2e6, 1e-12)
    chk("DIVERGENCE: the ruling's '2e4 to 2e5' is (upper edge, CENTRE)",
        RULING_S8_MATCHES, (("upper edge",), ("centre",)))
    chkrel("  so it spans half of Degrassi's band (log10)",
           RULING_S8_COVERS_FRACTION_OF_BAND, 0.5, 1e-12)

    # ------------------------------------------------ times and lengths
    print("\n11. TIMES AND LENGTHS")
    chk("V''(0)/V''(v) = -1/2 exactly: phi = 0 is a spinodal MAXIMUM",
        spinodal_ratio(), Fraction(-1, 2))
    chkrel("spinodal e-fold at READ 125.13 (ruling C.11)",
           SPINODAL_EFOLD_S["READ"], 7.439082e-27, 1e-6)
    chkrel("spinodal e-fold at the pin 125.20", SPINODAL_EFOLD_S["pinned 125.20"],
           7.434922e-27, 1e-6)
    chk("CONTROL 3.34 ns is not it: 1/c exceeds it by more than 1e17",
        (1.0 / C) / SPINODAL_EFOLD_S["pinned 125.20"] > 1e17, True)
    chkrel("driven ceiling sqrt(2/(m_h Gamma_h)) (ruling C.12, RUN)",
           DRIVEN_CEILING_M, 4.55e-16, 2e-3)
    chk("  printed to ONE significant figure (refusal 6)",
        one_sig(DRIVEN_CEILING_M), "5e-16")
    chk("quantum lifetime hbar/Gamma_h, one s.f.", one_sig(QUANTUM_LIFETIME_S),
        "2e-22")
    chkrel("W Compton length at READ m_W (ruling C.14)", LAMBDA_W_READ_M,
           2.455476e-18, 1e-6)
    chkrel("Z Compton length at READ m_Z", LAMBDA_Z_READ_M, 2.163960e-18, 1e-6)
    chkrel("  W / lambda_h(READ)", LAMBDA_W_READ_M / LAMBDA_H_READ_M,
           1.557079, 1e-6)
    chkrel("  Z / lambda_h(READ)", LAMBDA_Z_READ_M / LAMBDA_H_READ_M,
           1.372222, 1e-6)
    chkrel("curvature break-even H2 = S (M_red/v)^2", curvature_break_even("H2"),
           S_MID * 9.7829068836e31, 1e-9)

    # ------------------------------------------------ record and refusals
    print("\n12. THE RECORD, W9 AND THE REFUSALS")
    for nm in ("TAIL_RATE_IS_MASS", "DISPLACEMENT_IS_ULTRALOCAL",
               "ELECTRON_MASS_IS_A_RULER", "FLAT_DIRECTIONS_ARE_INERT",
               "HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18",
               "ROLE1_DOMINATED_BY_OWN_SOURCE", "ROLE2_REBINDS",
               "NOTHING_IS_REPAIRED"):
        chk("ledger owner excite.%s exists" % nm, nm in globals(), True)
    chk("D18 carries its hypotheses in its value", ELECTRON_MASS_IS_A_RULER,
        "THEOREM given alpha fixed (H2) and clamped point nuclei")
    chk("D15 carries one hypothesis per (H-x) label section 1 enumerates",
        len(TAIL_RATE_HYPOTHESES), len(doc_tail_rate_hypotheses()))
    chk("W9 fell on four reasons", len(W9[1]), 4)
    chk("the orchestrator's hypothesis: six counts, imported from endpoint",
        (len(ORCHESTRATOR_HYPOTHESIS_FAILURES),
         ORCHESTRATOR_HYPOTHESIS_FAILURES is endpoint.ORCHESTRATOR_HYPOTHESIS_FAILURES),
        (6, True))
    chkrel("W9(d): its 1.5755e-18 m is lambda at 125.25, not at the pin",
           endpoint.yukawa_range_m(125.25), 1.5755e-18, 1e-4)
    chk("refusal 3 matches address.H1_VS_H2_IS_REFUSED",
        (CHOOSES_BETWEEN_H1_AND_H2, address.H1_VS_H2_IS_REFUSED), (False, True))
    chk("refusal 12 is warpfolder's flag, imported",
        CONVERGENCE_IS_CORROBORATION, False)
    chk("every refusal section 8 enumerates carries a flag, and no other",
        sorted({n for n, _ in REFUSAL_FLAGS}), doc_refusal_numbers())
    chk("  REFUSALS, counted from the flags, is section 8's count",
        REFUSALS, len(doc_refusal_numbers()))
    chk("  every flag named exists in this module",
        all(nm in globals() for _, nm in REFUSAL_FLAGS), True)
    chk("recorded: none of the refusals is a total",
        (TOTALS_ACROSS_ROLES, PRICES_AN_ADDRESS_WITH_ONE_NUMBER,
         SEATS_A_TMP_FIGURE), (None, False, False))
    chk("nothing is repaired", NOTHING_IS_REPAIRED, True)

    dt = time.time() - t0
    print()
    if fails:
        for lab, g, w in fails:
            print("  FAIL %s: got %r want %r" % (lab, g, w))
        print("\nSELFTEST FAIL (%d) (%.1f s)" % (len(fails), dt))
        return 1
    print("SELFTEST PASS (%.1f s)" % dt)
    return 0


# ====================================================================== verify
def verify():
    """Every symbolic derivation, in sympy.  Each row must be exactly 0."""
    import sympy as sp
    rows = []
    x, r = sp.symbols("x r", positive=True)
    lam_, v_, m_ = sp.symbols("lambda v m", positive=True)
    ph, fs, t, e = sp.symbols("phi f t epsilon", real=True)

    # V1 reduced equation
    V = lam_ / 4 * (ph ** 2 - v_ ** 2) ** 2
    dV = sp.diff(V, ph)
    rows.append(("V1  V'(v(1+f))/(lam v^3) - f(f+1)(f+2)",
                 sp.expand(dV.subs(ph, v_ * (1 + fs)) / (lam_ * v_ ** 3)
                           - fs * (fs + 1) * (fs + 2))))
    rows.append(("V1b V''(v) - 2 lam v^2", sp.simplify(sp.diff(V, ph, 2).subs(ph, v_)
                                                       - 2 * lam_ * v_ ** 2)))
    # V2 u = x f, u'' = q u
    f = sp.Function("f")(x)
    u = x * f
    rows.append(("V2  (x f)'' - x (f'' + 2f'/x)",
                 sp.simplify(sp.diff(u, x, 2) - x * (sp.diff(f, x, 2)
                                                     + 2 * sp.diff(f, x) / x))))
    q = 1 + sp.Rational(3, 2) * fs + sp.Rational(1, 2) * fs ** 2
    rows.append(("V2b (1/2) f(f+1)(f+2) - q f",
                 sp.expand(sp.Rational(1, 2) * fs * (fs + 1) * (fs + 2) - q * fs)))
    # V3 Riccati
    U = sp.Function("u")(x)
    w = -sp.diff(U, x) / U
    rows.append(("V3  w' - (w^2 - u''/u), w = -u'/u",
                 sp.simplify(sp.diff(w, x) - (w ** 2 - sp.diff(U, x, 2) / U))))
    # V4 d dimensions
    d = sp.symbols("d", positive=True)
    ud = x ** ((d - 1) / 2) * f
    lhs = sp.diff(ud, x, 2) / x ** ((d - 1) / 2)
    rhs = (sp.diff(f, x, 2) + (d - 1) * sp.diff(f, x) / x
           + (d - 1) * (d - 3) / (4 * x ** 2) * f)
    rows.append(("V4  d-dim: u = x^((d-1)/2) f adds (d-1)(d-3)/(4x^2)",
                 sp.simplify(sp.expand(lhs - rhs))))
    # V5 kink
    fk = sp.tanh(x / 2) - 1
    rows.append(("V5  kink tanh(x/2)-1 residual",
                 sp.simplify((sp.diff(fk, x, 2) - sp.Rational(1, 2) * fk * (fk + 1)
                              * (fk + 2)).rewrite(sp.exp))))
    rows.append(("V5b kink rate -f'/f -> 1 (limit - 1)",
                 sp.limit(-sp.diff(fk, x) / fk, x, sp.oo) - 1))
    # V6 multipoles
    for l in range(6):
        R = sp.exp(-x) / x * sum(sp.factorial(l + j) / (sp.factorial(j)
                                                        * sp.factorial(l - j))
                                 * (2 * x) ** (-j) for j in range(l + 1))
        rows.append(("V6  k_%d radial residual" % l,
                     sp.simplify(sp.diff(R, x, 2) + 2 * sp.diff(R, x) / x
                                 - l * (l + 1) * R / x ** 2 - R)))
        rows.append(("V6b k_%d rate -> 1 (limit - 1)" % l,
                     sp.limit(-sp.diff(R, x) / R, x, sp.oo) - 1))
    # V7 Green's function
    Gr = sp.exp(-m_ * r) / (4 * sp.pi * r)
    rows.append(("V7  INT G d^3r - 1/m^2",
                 sp.simplify(sp.integrate(4 * sp.pi * r ** 2 * Gr, (r, 0, sp.oo))
                             - 1 / m_ ** 2)))
    rows.append(("V7b (-lap + m^2) G = 0 for r > 0",
                 sp.simplify(-sp.diff(r * Gr, r, 2) / r + m_ ** 2 * Gr)))
    s = sp.symbols("s", positive=True)
    rows.append(("V7c cos response error - s^2 + O(s^4)",
                 sp.series(1 - 1 / (1 + s ** 2), s, 0, 4).removeO() - s ** 2))
    # V8 Schrodinger dilation
    Za, ee, ll = sp.symbols("Zalpha e ell", positive=True)
    Uf = sp.Function("U")
    ur = Uf(m_ * r)
    schr = (-sp.diff(ur, r, 2) / (2 * m_) - Za / r * ur
            + ll * (ll + 1) / (2 * m_ * r ** 2) * ur - m_ * ee * ur)
    sch_x = sp.simplify((schr.subs(r, x / m_)).doit() / m_)
    rows.append(("V8  Schrodinger: m-dependence factors out (d/dm of residual/m)",
                 sp.simplify(sp.diff(sch_x, m_))))
    # CONTROL THAT MUST FIRE: a potential carrying its own fixed length (a
    # screened Coulomb e^{-r/a}/r, a fixed) does NOT dilate -- so V8's zero is
    # not something the substitution returns for any equation.
    aa = sp.symbols("a", positive=True)
    schr_c = (-sp.diff(ur, r, 2) / (2 * m_) - Za * sp.exp(-r / aa) / r * ur
              - m_ * ee * ur)
    sch_c = sp.simplify((schr_c.subs(r, x / m_)).doit() / m_)
    controls = [("C8  CONTROL screened Coulomb (fixed length a) does NOT dilate",
                 sp.simplify(sp.diff(sch_c, m_)))]
    # V9 Dirac-Coulomb radial pair
    kap = sp.symbols("kappa", real=True)
    gf, hf = sp.Function("g"), sp.Function("h")
    Gm, Fm = gf(m_ * r), hf(m_ * r)
    eq1 = sp.diff(Gm, r) + kap / r * Gm - (m_ * ee + m_ + Za / r) * Fm
    eq2 = sp.diff(Fm, r) - kap / r * Fm + (m_ * ee - m_ + Za / r) * Gm
    for lab, eq in (("V9a", eq1), ("V9b", eq2)):
        ex = sp.simplify((eq.subs(r, x / m_)).doit() / m_)
        rows.append(("%s Dirac-Coulomb: m factors out (d/dm of residual/m)" % lab,
                     sp.simplify(sp.diff(ex, m_))))
    m0 = sp.symbols("m0", positive=True)
    eq1c = sp.diff(Gm, r) + kap / r * Gm - (m_ * ee + m0 + Za / r) * Fm
    exc = sp.simplify((eq1c.subs(r, x / m_)).doit() / m_)
    controls.append(("C9  CONTROL a mass term that does not scale does NOT dilate",
                     sp.simplify(sp.diff(exc, m_))))
    nn, kk = sp.symbols("n k", positive=True)
    Ed = m_ / sp.sqrt(1 + (Za / (nn - kk + sp.sqrt(kk ** 2 - Za ** 2))) ** 2)
    rows.append(("V9c Dirac spectrum: d ln E/d ln m - 1",
                 sp.simplify(sp.diff(Ed, m_) * m_ / Ed - 1)))
    # V10 holding cost
    phi_e = v_ * (1 - e)
    rho = lam_ * v_ ** 4 / 4
    src = sp.expand(-dV.subs(ph, phi_e) * phi_e / rho)
    fld = sp.expand((V.subs(ph, phi_e) - V.subs(ph, v_)) / rho)
    rows.append(("V10 source - 4 eps(2-eps)(1-eps)^2",
                 sp.expand(src - 4 * e * (2 - e) * (1 - e) ** 2)))
    rows.append(("V10b field - eps^2(2-eps)^2",
                 sp.expand(fld - e ** 2 * (2 - e) ** 2)))
    ser = sp.Poly(sp.expand(src + fld), e).all_coeffs()[::-1]
    rows.append(("V10c series coefficients - (0, 8, -16, 12)",
                 sp.Matrix(ser[:4]) - sp.Matrix([0, 8, -16, 12])))
    rows.append(("V10d source/field * eps -> 2 (limit - 2)",
                 sp.limit(src / fld * e, e, 0) - 2))
    edge = [z for z in sp.solve(sp.diff(V, ph, 2).subs(ph, phi_e), e)
            if 0 < z < 1]
    rows.append(("V10e V''=0 root - (1 - 1/sqrt 3)",
                 sp.simplify(edge[0] - (1 - 1 / sp.sqrt(3)))))
    cross = [z for z in sp.solve(sp.expand(src - fld), e) if 0 < z < 1]
    rows.append(("V10f source=field root - (1 - 1/sqrt 5)",
                 sp.simplify(cross[0] - (1 - 1 / sp.sqrt(5)))))
    # V11 spinodal, against endpoint's own sympy
    ratio = sp.diff(V, ph, 2).subs(ph, 0) / sp.diff(V, ph, 2).subs(ph, v_)
    rows.append(("V11 V''(0)/V''(v) + 1/2", sp.simplify(ratio + sp.Rational(1, 2))))
    rows.append(("V11b == endpoint.spinodal_curvature_ratio()",
                 sp.simplify(ratio - endpoint.spinodal_curvature_ratio())))
    rel = abs(spinodal_efold_s(M_H_READ_GEV)
              / endpoint.spinodal_efold_s(M_H_READ_GEV) - 1)
    rows.append(("V11c spinodal e-fold vs endpoint's, rel > 1e-15 ?",
                 sp.Integer(0) if rel <= 1e-15 else sp.Float(rel)))
    # V12 uniform sphere potential
    Gs, rh, Rr = sp.symbols("G rho R", positive=True)
    M = sp.Rational(4, 3) * sp.pi * rh * Rr ** 3
    Phi = -Gs * M * (3 * Rr ** 2 - r ** 2) / (2 * Rr ** 3)
    rows.append(("V12 interior Phi solves lap Phi = 4 pi G rho",
                 sp.simplify(sp.diff(r ** 2 * sp.diff(Phi, r), r) / r ** 2
                             - 4 * sp.pi * Gs * rh)))
    rows.append(("V12b Phi(0) + 2 pi G rho R^2",
                 sp.simplify(Phi.subs(r, 0) + 2 * sp.pi * Gs * rh * Rr ** 2)))
    rows.append(("V12c [Phi(R)-Phi(0)] / [-Phi(0)] - 1/3",
                 sp.simplify((Phi.subs(r, Rr) - Phi.subs(r, 0))
                             / (-Phi.subs(r, 0)) - sp.Rational(1, 3))))
    # V13 driven ceiling
    Gam = sp.symbols("Gamma", positive=True)
    k = sp.sqrt(-sp.I * m_ * Gam)
    rows.append(("V13 |Im k| at omega = m - sqrt(m Gamma/2)",
                 sp.simplify(sp.Abs(sp.im(sp.expand_complex(k)))
                             - sp.sqrt(m_ * Gam / 2))))
    # V14 flat directions, general angle
    th = sp.symbols("theta", real=True)
    h1, h2 = sp.symbols("h1 h2")
    Hv = sp.Matrix([h1, h2])
    sig = {"T1": sp.Matrix([[0, 1], [1, 0]]), "T2": sp.Matrix([[0, -sp.I], [sp.I, 0]]),
           "T3": sp.Matrix([[1, 0], [0, -1]]), "Y": sp.eye(2)}
    for gname, sm in sig.items():
        Um = sp.cos(th) * sp.eye(2) + sp.I * sp.sin(th) * sm
        HU = Um * Hv
        diff = sp.simplify(sp.expand((HU.H * HU)[0] - (Hv.H * Hv)[0]))
        rows.append(("V14 %s: (U H)^dag (U H) - H^dag H, any theta" % gname, diff))

    bad = 0
    for lab, res in rows:
        good = (res == sp.zeros(*res.shape)) if isinstance(res, sp.MatrixBase) \
            else sp.simplify(res) == 0
        bad += 0 if good else 1
        print("  %-64s %s" % (lab, "0" if good else "NOT 0: %s" % res))
    for lab, res in controls:
        fired = sp.simplify(res) != 0
        bad += 0 if fired else 1
        print("  %-64s %s" % (lab, "NONZERO, fires" if fired
                              else "ZERO -- CONTROL FAILED"))
    print("\n  %d residual(s) not zero of %d; %d control(s), each must fire"
          % (bad, len(rows), len(controls)))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if "--verify" in sys.argv:
        sys.exit(verify())
    sys.exit(report())
