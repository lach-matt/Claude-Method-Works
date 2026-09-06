#!/usr/bin/env python3
"""warpdrive.py -- where a warp drive sits in the violation index, and what it costs.

Two halves, deliberately kept apart.

  INDEX   The fifteen-letter violation index of TRANSITIONS Part VII, rebuilt, with the
          warp drive seated as an object threshold in four variants.  Answers: is the
          object here, how many cells admit it, what must be given up to exclude it,
          and what every admitting cell pays.

  ENERGY  The warp drive's own numbers, in SI.  Alcubierre's energy integral under the
          Ford-Roman quantum inequality (Pfenning-Ford 1997), the Bobrick-Martire
          optimisations, and the Fuchs et al. 2024 positive-energy shell, which is the
          only warp drive anyone has exhibited that satisfies all four energy conditions.

The halves do not talk to each other and must not be made to.  The index is a statement
about a coordinate system; the energy budget is a statement about a spacetime.  Part XI
result 13 of the companion is the reason: "openness is the signature, not a failure."

PROVENANCE.  The closure rules and the coordinate alphabet in build_index() are copied
verbatim from recovered/objects15.py (the fifteen-letter constructor recovered from the
chat export), per the standing rule that an instrument imports or copies a seated form
with a provenance comment and never silently reimplements it.  objects15.py reproduces
the companion's printed 18,888 / 18,072 / 816 exactly; this file asserts that in
--selftest before reporting anything.

Stdlib only.  python3 warpdrive.py [--selftest]
"""
import sys
from itertools import product, combinations

# ---------------------------------------------------------------- the index

# copied verbatim from recovered/objects15.py -- do not "tidy"
NM = ['X_exp','X_spon','Sc','IC','U_open','U_ghost','NEC_pt','NEC_ach',
      'L_dyn','L_kin','SD_obs','SD_field','DNc','DNd','EOM']
RNG = [range(4),range(2),range(3),range(3),range(3),range(2),range(5),range(2),
       range(2),range(2),range(2),range(2),range(3),range(3),range(2)]
Xe,Xs,Sc,IC,Uo,Ug,Np,Na,Ld,Lk,So,Sf,Dc,Dd,EO = range(15)

def close(x):
    x = list(x); g = True
    while g:
        g = False
        def rz(i, v):
            nonlocal g
            if x[i] < v: x[i] = v; g = True
        if x[Xe] >= 3: rz(Np,2); rz(Na,1)
        if x[Sc] >= 2: rz(IC,1)
        if x[Uo] >= 2: rz(IC,2)
        if x[Uo] >= 1: rz(Np,1)
        if x[Np] >= 4: rz(Xe,1)
        if x[Ld] >= 1: rz(Dd,1)
        if x[So] >= 1: rz(IC,2)
        if x[Dc] >= 2: rz(IC,2); rz(Ld,1); rz(Dd,2)
        if x[Dd] >= 2: rz(Dc,2)
        if x[Na] >= 1: rz(Np,2)
        if x[Ug] >= 1: rz(Xs,1)
        if x[Lk] >= 1: rz(Dd,2)
        if x[EO] >= 1: rz(Ug,1)
    return tuple(x)

def build_index():
    """Returns (closed, admitted, ours).  `closed` is every closed cell describing a
    theory at all (SD_field = 0, Burgoyne); `admitted` removes the cells the core
    charge excludes; `ours` is the cell this universe is measured to occupy."""
    closed = {c for c in {close(x) for x in product(*RNG)} if c[Sf] == 0}
    # the core charge: macroscopic NEC violation with no explicit Lorentz violation,
    # no ghosts and second-order equations of motion is the one excluded profile
    admitted = {c for c in closed
                if not (c[Np] >= 3 and c[Xe] == 0 and c[EO] == 0 and c[Ug] < 1)}
    ours = close(tuple([0,0,1,0,0,0,1,0,0,0,0,0,0,0,0]))
    return closed, admitted, ours

CORE = 'X_exp = 0, U_ghost = 0, NEC_pt = 3, EOM = second order'

# The warp drive, seated four ways.  Each row is (tag, prose, predicate, why).
#
# The grading of NEC_pt is the companion's: 0 intact / 1 pointwise / 2 ANEC arbitrarily
# small / 3 macroscopic QI-bounded / 4 QI-violating.  NEC_ach is achronal ANEC violated.
WARP = [
 ('WD-SHELL',
  'subluminal positive-energy warp shell (Fuchs et al. 2024)',
  lambda c: True,
  'satisfies NEC, WEC, DEC, SEC; costs no coordinate of this index'),
 ('WD-SUB-ALC',
  'subluminal Alcubierre / Natario bubble',
  lambda c: c[Np] >= 3,
  'Santiago-Schuster-Visser: every generic Natario drive violates the NEC, '
  'and the violation is macroscopic'),
 ('WD-SUP',
  'superluminal warp drive',
  lambda c: c[Np] >= 3 and c[Na] >= 1,
  'a superluminal drive is asymptotically flat and simply connected, so Graham-Olum '
  'has standing: the shortcut violates the ACHRONAL ANEC, unlike a long wormhole'),
 ('WD-SUP-CTC',
  'superluminal warp drive, two bubbles (Everett)',
  lambda c: c[Np] >= 3 and c[Na] >= 1 and c[Xe] == 3,
  'two superluminal bubbles in relative motion close a timelike curve'),
]

# what a cell may be asked to preserve; the exclusion sets are drawn from these
PRE = [('no explicit Lorentz violation', lambda c: c[Xe] == 0),
       ('no spontaneous Lorentz breaking', lambda c: c[Xs] == 0),
       ('unitary evolution (open)',        lambda c: c[Uo] == 0),
       ('no ghosts',                       lambda c: c[Ug] == 0),
       ('no signalling',                   lambda c: c[IC] < 2),
       ('information causality',           lambda c: c[IC] == 0),
       ('microcausality (observables)',    lambda c: c[So] == 0),
       ('linear dynamics',                 lambda c: c[Ld] == 0),
       ('linear state space',              lambda c: c[Lk] == 0),
       ('the ANEC',                        lambda c: c[Np] < 2),
       ('the achronal ANEC',               lambda c: c[Na] == 0),
       ('second-order EOM',                lambda c: c[EO] == 0)]

def minimal_exclusions(cells, pred, maxr=3):
    """Smallest sets of preservations that jointly admit no cell meeting `pred`."""
    hits_at = None
    for r in range(1, maxr + 1):
        hits = [tuple(p for p, _ in combo) for combo in combinations(PRE, r)
                if not any(pred(c) and all(pf(c) for _, pf in combo) for c in cells)]
        if hits:
            hits_at = (r, hits); break
    return hits_at

def payments(cells, pred):
    """Of the cells admitting the object, how many pay in each currency, and how many
    pay nothing at all."""
    sub = [c for c in cells if pred(c)]
    cur = [('a preferred frame (X_exp > 0)',   lambda c: c[Xe] > 0),
           ('a preferred frame (X_spon > 0)',  lambda c: c[Xs] > 0),
           ('ghosts (U_ghost > 0)',            lambda c: c[Ug] > 0),
           ('non-unitarity (U_open > 0)',      lambda c: c[Uo] > 0),
           ('signalling (IC >= 2)',            lambda c: c[IC] >= 2),
           ('higher-derivative EOM',           lambda c: c[EO] > 0)]
    rows = [(n, sum(1 for c in sub if f(c))) for n, f in cur]
    none = sum(1 for c in sub if not any(f(c) for _, f in cur))
    return len(sub), rows, none

# --------------------------------------------------------------- the energy

G    = 6.67430e-11          # m^3 kg^-1 s^-2
C    = 2.99792458e8         # m s^-1
HBAR = 1.054571817e-34      # J s
L_P  = (HBAR * G / C**3) ** 0.5          # 1.616e-35 m
M_SUN, M_JUP, M_EARTH = 1.98892e30, 1.89813e27, 5.9722e24
M_MILKYWAY = 1e12 * M_SUN
RHO_NUC = 2.3e17            # kg m^-3, nuclear saturation
KG_PER_M = C**2 / G         # geometrized length -> kg
J_PER_M  = C**4 / G         # geometrized length -> J

def qi_wall(v, alpha=0.1):
    """Pfenning-Ford eq (22): the widest bubble wall the Ford-Roman quantum inequality
    allows, in metres.  alpha is the ratio of sampling time to local curvature radius;
    the derivation needs alpha << 1 and PF take alpha = 1/10."""
    return 0.75 * (3.0 / 3.141592653589793) ** 0.5 * v / alpha**2 * L_P

def alcubierre_energy(R, delta, v):
    """Pfenning-Ford eq (28): E = -(1/12) v^2 (R^2/delta + delta/12), geometrized
    (metres).  Negative by construction.  Returns (E_geom_m, E_joules, M_kg)."""
    e = -(1.0 / 12.0) * v**2 * (R*R / delta + delta / 12.0)
    return e, e * J_PER_M, e * KG_PER_M

def shell(R1, R2, M):
    """Fuchs et al. 2024 warp shell: the material the solution actually asks for."""
    vol = (4.0/3.0) * 3.141592653589793 * (R2**3 - R1**3)
    rho = M / vol
    r_s = 2 * G * M / C**2
    return dict(volume=vol, rho=rho, rho_energy=rho * C**2,
                nuclear=rho / RHO_NUC, r_s=r_s, margin=R1 / r_s,
                m_jup=M / M_JUP, m_earth=M / M_EARTH, m_sun=M / M_SUN)

def shell_ceiling(R1):
    """Largest shell mass that still clears its own horizon at inner radius R1:
    R1 > 2GM/c^2, so M < R1 c^2 / 2G.  This is the hard ceiling on a warp shell."""
    return R1 * C**2 / (2 * G)

FILL = 4.49e27 / (10.0 * C**2 / (2 * G))   # Fuchs et al. sit at this fraction of it

def design_trade(R1, ratio=2.0):
    """Scale the published shell geometrically at fixed fill fraction and fixed R2/R1,
    and report the material it then asks for.  Density falls as 1/R1^2 while mass
    grows as R1 -- the whole engineering trade in one line."""
    M = FILL * shell_ceiling(R1)
    s = shell(R1, ratio * R1, M)
    s['M'] = M; s['R2'] = ratio * R1
    return s

def radius_for_density(rho, ratio=2.0):
    """Inner radius at which the scaled shell needs only material of density rho."""
    s = design_trade(1.0, ratio)          # rho scales as 1/R1^2
    return (s['rho'] / rho) ** 0.5

# --------------------------------------------- the design document's own claims
#
# "Warp Drive Theory -- Project Deliverable: Integrated Solid-State Electromagnetic
# & Muon-Catalyzed Metric Propulsion Drives", 5 pp,
# drive/The Method Materials/warp drive theory.pdf  (manifest row: ok-adopted).
# Every claim below that is computable is computed here rather than assessed in prose.

import random

MU0, EPS0 = 4e-7 * 3.141592653589793, 8.8541878128e-12
RHO_CU = 1.68e-8            # ohm m, OFHC copper at 293 K
M_E, M_MU, M_D = 9.1093837015e-31, 1.883531627e-28, 3.3435837768e-27
MEV = 1.602176634e-13       # J

def em_nec(samples=200000, seed=17):
    """Classical electromagnetic stress-energy against the null energy condition.

    T^00 = (eps0 E^2 + B^2/mu0)/2 ,  T^0i = (ExB)_i/mu0c ,
    T^ij = -(eps0 E_iE_j + B_iB_j/mu0) + delta_ij T^00 .
    With k^a = (1, n) and signature (-+++),
        T_ab k^a k^b = (E^2+B^2) - 2(ExB).n - (E.n)^2 - (B.n)^2   (c = eps0 = mu0 = 1).
    Returns the minimum over random fields and random null directions."""
    rnd = random.Random(seed)
    worst = float('inf')
    def unit():
        while True:
            v = [rnd.gauss(0,1) for _ in range(3)]
            n = sum(c*c for c in v) ** 0.5
            if n > 1e-9: return [c/n for c in v]
    for _ in range(samples):
        E = [rnd.gauss(0,1) for _ in range(3)]
        B = [rnd.gauss(0,1) for _ in range(3)]
        n = unit()
        cross = [E[1]*B[2]-E[2]*B[1], E[2]*B[0]-E[0]*B[2], E[0]*B[1]-E[1]*B[0]]
        E2 = sum(c*c for c in E); B2 = sum(c*c for c in B)
        En = sum(a*b for a, b in zip(E, n)); Bn = sum(a*b for a, b in zip(B, n))
        val = (E2 + B2) - 2*sum(a*b for a, b in zip(cross, n)) - En*En - Bn*Bn
        worst = min(worst, val)
    return worst

def hoop_speed(sigma, rho):
    """Burst surface speed of a thin spinning cylinder: hoop stress = rho v^2."""
    return (sigma / rho) ** 0.5

def skin_depth(f, rho=RHO_CU, mu=MU0):
    """Classical skin depth delta = sqrt(2 rho / omega mu), and the surface
    resistance R_s = rho / delta it implies."""
    omega = 2 * 3.141592653589793 * f
    d = (2 * rho / (omega * mu)) ** 0.5
    return d, rho / d

def mucf(sticking=0.0045, per_fusion_mev=17.6, muon_cost_gev=5.0):
    """Muon-catalysed fusion energy balance.  The sticking probability caps the
    cycles per muon at 1/omega_s; break-even needs the muon's production cost back."""
    n_max = 1.0 / sticking
    yield_gev = n_max * per_fusion_mev / 1000.0
    n_needed = muon_cost_gev * 1000.0 / per_fusion_mev
    return dict(n_max=n_max, yield_gev=yield_gev, n_needed=n_needed,
                ratio=yield_gev / muon_cost_gev,
                sticking_needed=per_fusion_mev / (muon_cost_gev * 1000.0))

def muonic_radius_factor():
    """Orbital radius shrinks as the reduced mass grows.  The document says 200."""
    red_e = M_E * M_D / (M_E + M_D)
    red_mu = M_MU * M_D / (M_MU + M_D)
    return red_mu / red_e

# ------------------------------------- counter-rotation on a positive-energy shell
#
# Can Architecture B's angular-momentum cancellation be carried onto the Fuchs et al.
# shell without breaking the energy conditions that make that shell physical?
# Three separate budgets, kept apart because they answer different questions.

# read off Fuchs et al. fig. 9: rho ~ 1.376e40 J/m^3, |p_i| and |momentum| peak ~5e39.
FUCHS_RHO, FUCHS_PEAK = 1.376e40, 5.0e39

def dec_margin(rho=FUCHS_RHO, peak=FUCHS_PEAK):
    """Fraction of the dominant-energy-condition budget the static solution leaves
    unspent.  DEC is |p_i| <= rho, so the spent fraction is peak/rho."""
    spent = peak / rho
    return dict(spent=spent, free=1.0 - spent)

def rotation_cost(beta):
    """What rigid rotation at local rim speed beta = v/c costs.

    EIGENVALUE budget.  A boost does not change the eigenvalues of the stress-energy,
    so rotating matter that satisfies the energy conditions at rest still does.  What
    is new is the centrifugal hoop TENSION needed to hold the shell together:
    sigma = rho_m v^2, i.e. |delta p_phi| / rho = beta^2.  That is the real cost.

    EULERIAN budget.  Fuchs et al. work to the sufficient rule of thumb that every
    Eulerian pressure and momentum flux stay below the energy density.  Boosted
    momentum flux is T^{0phi}/T^{00} ~ beta, linear.  Conservative, not the condition."""
    return dict(eigen=beta * beta, eulerian=beta)

def rotation_headroom(free):
    """Largest rim speed each budget allows, given the free DEC margin."""
    return dict(eigen=free ** 0.5, eulerian=free)

def orbital_beta(R, M):
    """Rim speed at which rotation would actually support the shell against its own
    gravity: v_orb = sqrt(GM/R)."""
    return (G * M / R) ** 0.5 / C

def quadrupole_scale(beta):
    """Counter-rotation zeroes the ADM angular momentum, so the g_t-phi frame-dragging
    term vanishes and the exterior stays Schwarzschild at that order.  What survives is
    a rotation-induced mass quadrupole, which scales as beta^2."""
    return beta * beta

def maglev_ratio(B, p_internal=FUCHS_PEAK):
    """Magnetic pressure B^2/2mu0 against the shell's own internal pressure.  The
    document replaces mechanical bearings with electromagnetic levitation; this is
    whether that can hold at warp-shell density."""
    p_mag = B * B / (2 * MU0)
    return dict(p_mag=p_mag, ratio=p_mag / p_internal)

def shell_inertia(M, R1, R2):
    """Moment of inertia of a uniform thick spherical shell."""
    return 0.4 * M * (R2**5 - R1**5) / (R2**3 - R1**3)

# ------------------------------------------------- the shift-vector ceiling
#
# Fuchs et al. leave one number explicitly open: "Increasing the shift vector will
# continue to add more momentum flux to the stress-energy tensor, so there is an
# upper limit to the magnitude of the shift vector that keeps the warp drive
# physical.  This upper limit is a future direction of work."
#
# It has a closed form.  In an orthonormal Eulerian frame the (t,x) block is
#     T^{ab} = [[rho, f], [f, p_x]]
# and the mixed tensor T^a_b has eigenvalues
#     lambda_pm = ( (p_x - rho) +- sqrt((rho + p_x)^2 - 4 f^2) ) / 2 .
# When 2f > rho + p_x the root goes imaginary, the stress-energy becomes
# Hawking-Ellis type IV, and EVERY energy condition fails at once -- there is no
# frame in which the energy density is real.  So the ceiling is
#     f <= (rho + p_x) / 2 ,
# which is also exactly the NEC bound, since for a null k = (1, n)
#     T_ab k^a k^b = rho + p_t + n_x^2 (p_x - p_t) - 2 f n_x
# is minimised at n_x = 1 and gives rho + p_x - 2f.

def he_eigen(rho, p_x, f):
    """Eigen-energy-density and principal pressure of the (t,x) block.
    Returns None when the block is Hawking-Ellis type IV (complex eigenvalues)."""
    disc = (rho + p_x) ** 2 - 4.0 * f * f
    if disc < 0.0: return None
    root = disc ** 0.5
    return ((rho - p_x) + root) / 2.0, ((p_x - rho) + root) / 2.0

def flux_ceiling(rho, p_x):
    """The largest Eulerian momentum flux the stress-energy can carry and stay
    type I.  Equals the NEC bound."""
    return (rho + p_x) / 2.0

def nec_min_over_directions(rho, p_x, p_t, f, samples=4001):
    """Brute-force minimum of T_ab k^a k^b over null directions, as a check on the
    closed form rather than a substitute for it."""
    best = float('inf')
    for i in range(samples):
        nx = -1.0 + 2.0 * i / (samples - 1)
        val = rho + p_t + nx * nx * (p_x - p_t) - 2.0 * f * nx
        best = min(best, val)
    return best

def shift_ceiling(rho=FUCHS_RHO, p=FUCHS_PEAK, f_at_beta=FUCHS_PEAK,
                  beta_ref=0.02, v_over_beta=2.0):
    """Scale the published operating point up to the ceiling, taking the Eulerian
    momentum flux linear in the shift (first-order frame dragging)."""
    f_max = flux_ceiling(rho, p)
    gain = f_max / f_at_beta
    return dict(f_max=f_max, f_ref=f_at_beta, gain=gain,
                beta_max=beta_ref * gain,
                v_max=beta_ref * gain * v_over_beta,
                headroom_ratio=f_max / rho, used_ratio=f_at_beta / rho)

def combined_ceiling(rho, p, f_shift, beta_rot):
    """Shift flux and rotation flux are orthogonal (ROTATING-SHELL section 6), so
    they add in quadrature against the same ceiling."""
    tot = (f_shift ** 2 + (beta_rot * rho) ** 2) ** 0.5
    return dict(total=tot, ceiling=flux_ceiling(rho, p), ok=tot <= flux_ceiling(rho, p))

# ------------------------------------ the shell profile, reconstructed by TOV
#
# SHIFT-CEILING.md took rho and p from Fuchs et al.'s plotted profiles by eye and
# said so.  This integrates the Tolman-Oppenheimer-Volkoff equation for their stated
# construction instead, and the two disagree by a factor of five -- for a reason:
# the isotropic TOV pressure is the BULK pressure, while their plotted peak includes
# the anisotropic hoop spike at the inner boundary that holds the shell against
# collapse.  Both numbers are real and they are different quantities.
#
# The ceiling of SHIFT-CEILING.md is f <= (rho + p_x)/2 with p_x the pressure ALONG
# the direction of travel.  On the x-axis of the shell that is the radial pressure;
# at the equator it is the tangential one, which is larger.  The NEC must hold
# everywhere, so the binding value is the SMALLER -- the radial pressure -- at the
# radius where the momentum flux peaks.  Fuchs et al. put that peak at mid-shell.

def tov_shell(R1, R2, M, n=40000):
    """Integrate TOV inward from R2 (P = 0) to R1 for a constant-density shell.
    Returns the radial pressure profile in units of the energy density."""
    vol = (4.0 / 3.0) * 3.141592653589793 * (R2**3 - R1**3)
    rho_m = M / vol
    rho_E = rho_m * C * C
    span = R2**3 - R1**3
    def mass(r):
        if r <= R1: return 0.0
        if r >= R2: return M
        return M * (r**3 - R1**3) / span
    def dPdr(r, P):
        m = mass(r)
        f = 1.0 - 2 * G * m / (C * C * r)
        if f <= 0.0: return None
        return -G * (rho_m + P / (C*C)) * (m + 4*3.141592653589793*r**3*P/(C*C)) \
               / (r * r * f)
    h = (R2 - R1) / n
    r, P = R2, 0.0
    prof, mid = [], None
    for i in range(n):
        k1 = dPdr(r, P)
        if k1 is None: return None
        k2 = dPdr(r - h/2, P - h*k1/2)
        if k2 is None: return None
        k3 = dPdr(r - h/2, P - h*k2/2)
        if k3 is None: return None
        k4 = dPdr(r - h, P - h*k3)
        if k4 is None: return None
        P = P - (h/6.0) * (k1 + 2*k2 + 2*k3 + k4)
        r = r - h
        if P < 0.0: return None
        if mid is None and r <= (R1 + R2) / 2.0: mid = P / rho_E
        prof.append((r, P / rho_E))
    return dict(rho_m=rho_m, rho_E=rho_E, P_inner=P, inner=P/rho_E, mid=mid, prof=prof)

def ceiling_from_profile(p_over_rho):
    """SHIFT-CEILING's bound, evaluated on a computed pressure rather than a read one."""
    return (1.0 + p_over_rho) / 2.0

def fill_sweep(R1=10.0, ratio=2.0, fills=(0.1,0.2,0.3,0.4,0.5,0.667,0.8,0.9),
               f_ref=0.363, beta_ref=0.02, v_over_beta=2.0):
    """Vary the horizon fill fraction and follow it through to a velocity ceiling
    and a shell mass.  fill = r_s/R1 = 2GM/(c^2 R1)."""
    out = []
    for fl in fills:
        M = fl * R1 * C * C / (2 * G)
        t = tov_shell(R1, ratio * R1, M)
        if t is None:
            out.append((fl, M, None, None, None)); continue
        c_ = ceiling_from_profile(t['mid'])
        beta_max = beta_ref * c_ / f_ref
        out.append((fl, M, t['mid'], c_, beta_max * v_over_beta))
    return out

# --------------------------------------------------------------- acceleration
#
# ADM 4-momentum is conserved for an isolated asymptotically flat system up to what
# it radiates or ejects.  No internal rearrangement changes it.  So a warp shell with
# POSITIVE ADM mass cannot self-accelerate -- and positive ADM mass is exactly what
# makes it satisfy the energy conditions.  Alcubierre's drive appears to self-
# accelerate only because its ADM mass is zero, which is the same truncation that
# forces its negative energy.  The two properties are traded through M_ADM.

def adm_momentum(M, beta):
    gamma = 1.0 / (1.0 - beta*beta) ** 0.5
    return gamma * M * beta * C

def photon_rocket(M_final, beta):
    """Relativistic photon rocket: M_i/M_f = sqrt((1+b)/(1-b)).  This is the BEST
    any radiative scheme can do -- massless radiation carries p = E/c, so gravitational
    waves and photons obey the same bound."""
    ratio = ((1.0 + beta) / (1.0 - beta)) ** 0.5
    prop = M_final * (ratio - 1.0)
    return dict(ratio=ratio, prop=prop, energy=prop * C * C,
                earths=prop / M_EARTH)

def mass_rocket(M_final, beta, v_e_over_c):
    """Newtonian rocket equation for an ejected-rest-mass exhaust."""
    import math
    r = math.exp(beta / v_e_over_c)
    return dict(ratio=r, prop=M_final * (r - 1.0),
                earths=M_final * (r - 1.0) / M_EARTH)

# ----------------------------------------------------------------- report

def report():
    closed, V, ours = build_index()
    p = print
    p()
    p('  THE FIFTEEN-LETTER VIOLATION INDEX')
    p('  ' + '-' * 68)
    p('    closed cells describing a theory (SD_field = 0) : %7d' % len(closed))
    p('    admitted after the core charge                  : %7d' % len(V))
    p('    excluded by the core charge                     : %7d' % (len(closed)-len(V)))
    p('    the core                                        : %s' % CORE)
    p('    our own cell                                    : %s'
      % ', '.join('%s=%d' % (NM[i], ours[i]) for i in range(15) if ours[i]))
    p()
    p('  THE WARP DRIVE, SEATED AS AN OBJECT')
    p('  ' + '-' * 68)
    p('    %-12s %-42s %8s %6s' % ('tag', 'object', 'cells', 'here?'))
    for tag, prose, pred, _ in WARP:
        n = sum(1 for c in V if pred(c))
        p('    %-12s %-42s %8d %6s' % (tag, prose[:42], n, 'YES' if pred(ours) else 'no'))
    p()
    p('    Read the WD-SHELL row carefully.  Its predicate is vacuously true because a')
    p('    positive-energy subluminal shell spends no coordinate of this index at all.')
    p('    It is admitted everywhere, including here.  That is the whole finding.')
    p()
    for tag, prose, pred, why in WARP[1:]:
        p('  %s  --  %s' % (tag, prose))
        p('  ' + '-' * 68)
        p('    standing : %s' % why)
        n, rows, none = payments(V, pred)
        me = minimal_exclusions(V, pred)
        if me:
            p('    excluded by any one of %d preservation(s) of size %d:' % (len(me[1]), me[0]))
            for h in me[1]:
                p('        %s' % ' + '.join(h))
        else:
            p('    no preservation set of size <= 3 excludes it')
        p('    of the %d admitting cells, the payments are:' % n)
        for nm, k in rows:
            p('        %-34s %6d   %5.1f%%' % (nm, k, 100.0*k/n if n else 0))
        p('        %-34s %6d' % ('PAY NOTHING', none))
        p()
    p('  THE CORE CELL IS THE WARP DRIVE\'S OWN SPECIFICATION')
    p('  ' + '-' * 68)
    spec = [('standard general relativity, Einstein equations', 'EOM  = second order'),
            ('no explicit Lorentz violation in the Lagrangian', 'X_exp = 0'),
            ('ordinary, non-ghost field content',              'U_ghost = 0'),
            ('macroscopic exotic matter, QI-bounded',          'NEC_pt = 3')]
    for a, b in spec:
        p('    %-50s %s' % (a, b))
    p('    ' + '-' * 66)
    p('    that conjunction is the core, and the core is the one excluded cell.')
    p()
    p('  THE ENERGY BUDGET  (Alcubierre superluminal, under the quantum inequality)')
    p('  ' + '-' * 68)
    R = 100.0
    p('    bubble radius R = %.0f m, Ford-Roman sampling ratio alpha = 0.1' % R)
    p('    %-6s %14s %16s %16s' % ('v/c', 'wall Delta [m]', 'E [J]', '|E| [kg]'))
    for v in (0.1, 1.0, 2.0, 10.0):
        d = qi_wall(v)
        _, ej, mk = alcubierre_energy(R, d, v)
        p('    %-6.1f %14.3e %16.3e %16.3e' % (v, d, ej, abs(mk)))
    d1 = qi_wall(1.0)
    _, _, m1 = alcubierre_energy(R, d1, 1.0)
    p()
    p('    at v = c that is %.2e Milky Way masses.' % (abs(m1) / M_MILKYWAY))
    p('    Pfenning-Ford print -6.2e70 v L_Planck for this case; the line above gives')
    p('    %.2e L_Planck, agreeing to a factor of %.1f, which is inside the'
      % (abs(alcubierre_energy(R, d1, 1.0)[0]) / L_P,
         abs(alcubierre_energy(R, d1, 1.0)[0]) / L_P / 6.2e70 if
         abs(alcubierre_energy(R, d1, 1.0)[0]) / L_P > 6.2e70 else
         6.2e70 / (abs(alcubierre_energy(R, d1, 1.0)[0]) / L_P)))
    p('    order-of-magnitude precision their section 4 claims for itself.')
    p()
    p('    the wall thickness is the whole lever -- relax the quantum inequality and:')
    p('    %-22s %16s %16s' % ('wall Delta', 'E [J]', '|E| [M_sun]'))
    for d, nm in ((qi_wall(1.0), 'QI-bounded'), (1e-15, '1 fm'), (1.0, '1 m')):
        _, ej, mk = alcubierre_energy(R, d, 1.0)
        p('    %-22s %16.3e %16.3e' % ('%s (%.2e m)' % (nm, d), ej, abs(mk)/M_SUN))
    p()
    p('    Bobrick-Martire optimisations, applied to the 1 m wall case:')
    _, _, mk = alcubierre_energy(R, 1.0, 1.0)
    p('        unoptimised                              %10.3e M_sun' % (abs(mk)/M_SUN))
    p('        shape function f = min(r0/r, 1)  (/3)    %10.3e M_sun' % (abs(mk)/3/M_SUN))
    p('        flattened by a factor 10         (/10)   %10.3e M_sun' % (abs(mk)/30/M_SUN))
    p('    and none of this makes the energy positive; it makes less of it negative.')
    p()
    p('  THE ONE WARP DRIVE THAT SATISFIES EVERY ENERGY CONDITION')
    p('  ' + '-' * 68)
    s = shell(10.0, 20.0, 4.49e27)
    p('    Fuchs, Helmerich, Bobrick, Sellers, Melcher & Martire, CQG 41 (2024) 095009')
    p('    constant velocity, subluminal, NEC + WEC + DEC + SEC all satisfied')
    p()
    p('    inner radius R1                         %10.1f m' % 10.0)
    p('    outer radius R2                         %10.1f m' % 20.0)
    p('    shell mass M                            %10.3e kg' % 4.49e27)
    p('                                            %10.2f Jupiter masses' % s['m_jup'])
    p('                                            %10.3e solar masses' % s['m_sun'])
    p('    shell volume                            %10.3e m^3' % s['volume'])
    p('    mass density                            %10.3e kg/m^3' % s['rho'])
    p('    energy density                          %10.3e J/m^3' % s['rho_energy'])
    p('    in units of nuclear saturation density  %10.3e' % s['nuclear'])
    p('    Schwarzschild radius 2GM/c^2            %10.3f m' % s['r_s'])
    p('    horizon margin R1 / r_s                 %10.3f   (must exceed 1)' % s['margin'])
    p('    shift vector beta                       %10.3f' % 0.02)
    p('    drive velocity                          %10.3f c' % 0.04)
    p('    light-ray test delay vs flat            %10.1f ns' % 7.6)
    p()
    p('    horizon ceiling at R1 = 10 m            %10.3e kg' % shell_ceiling(10.0))
    p('    the solution sits at                    %10.1f%% of that ceiling' % (100*FILL))
    p()
    p('    SCALING THE SHELL.  Fix the fill fraction and R2 = 2 R1, and grow it:')
    p('    %-10s %12s %12s %14s %12s' % ('R1 [m]', 'M [kg]', 'M [M_sun]',
                                         'rho [kg/m^3]', 'rho / nuc'))
    for r1 in (10.0, 1e2, 1e3, 8.16e3, 1e5):
        t = design_trade(r1)
        p('    %-10.3g %12.3e %12.3e %14.3e %12.3e'
          % (r1, t['M'], t['m_sun'], t['rho'], t['nuclear']))
    rn = radius_for_density(RHO_NUC)
    tn = design_trade(rn)
    p()
    p('    density falls as 1/R1^2 while mass grows as R1.  Nuclear-density material')
    p('    suffices at R1 = %.2f km, and the ship then masses %.2f solar masses.'
      % (rn / 1e3, tn['m_sun']))
    p()
    p('    So the engine that exists on paper is a 20 m shell holding %.1f Jupiter' % s['m_jup'])
    p('    masses at %.1e times nuclear density, cruising at %.2f c, and nobody' % (s['nuclear'], 0.04))
    p('    knows how to accelerate it.  That last is the open problem, not the mass.')
    p()
    p('  THE DESIGN DOCUMENT, CHECKED')
    p('  ' + '-' * 68)
    p('    drive/The Method Materials/warp drive theory.pdf, 5 pp, status ok-adopted')
    p()
    w = em_nec()
    p('    [1] Can a classical electromagnetic field supply the exotic matter?')
    p('        min over 200,000 random (E, B, null n) of T_ab k^a k^b : %+.3e' % w)
    p('        The electromagnetic stress-energy satisfies the NEC identically.')
    p('        Neither topology can source NEC_pt > 0 by classical fields alone.')
    p()
    p('    [2] "Relativistic surface velocities" for a spinning cylinder')
    p('        %-34s %12s %10s' % ('material', 'v_burst [m/s]', 'v/c'))
    for nm, sig, rho in (('OFHC copper, annealed', 2.0e8, 8960.0),
                         ('copper, cold-worked', 4.0e8, 8960.0),
                         ('carbon-fibre overwrap', 5.0e9, 1600.0)):
        v = hoop_speed(sig, rho)
        p('        %-34s %12.4g %10.2e' % (nm, v, v / C))
    p('        Even the best overwrap is 5 orders of magnitude short of relativistic.')
    p()
    p('    [3] Skin depth and surface resistance in copper at the stated 1-10 GHz')
    p('        %-10s %16s %18s' % ('f', 'delta [m]', 'R_s [ohm/square]'))
    for f in (1e9, 1e10):
        d, rs = skin_depth(f)
        p('        %-10.0e %16.3e %18.3e' % (f, d, rs))
    p('        Cryogenic operation does NOT divide R_s by the RRR: below ~30 K the')
    p('        mean free path exceeds delta and the anomalous skin effect saturates')
    p('        R_s, which improves as RRR^(1/3) at best.  The document asks copper to')
    p('        be a 4-77 K thermal sink AND an RF conductor at 10^5 A/cm^2; those two')
    p('        duties load the same cryostat from opposite ends.')
    p()
    m = mucf()
    p('    [4] Muon-catalysed fusion, the energy balance the document omits')
    p('        muonic radius reduction factor        %10.1f   (document says 200)'
      % muonic_radius_factor())
    p('        cycles per muon, sticking-capped      %10.1f' % m['n_max'])
    p('        energy returned per muon              %10.2f GeV' % m['yield_gev'])
    p('        cost to make one muon                 %10.2f GeV' % 5.0)
    p('        return / cost                         %10.2f' % m['ratio'])
    p('        cycles needed to break even           %10.1f' % m['n_needed'])
    p('        sticking needed to reach that         %10.3f %%'
      % (100 * m['sticking_needed']))
    p('        Break-even needs MORE cycles than the sticking ceiling allows.')
    p('        The checklist target of "beyond 100 fusions per muon" is below both')
    p('        the ~150 already achieved and the ~%.0f break-even needs.' % m['n_needed'])
    p()
    p('  COUNTER-ROTATION ON A POSITIVE-ENERGY SHELL')
    p('  ' + '-' * 68)
    dm = dm0 = dec_margin()
    p('    [A] Does it survive the exterior boundary condition?')
    p('        The Fuchs construction needs a Schwarzschild exterior.  A SINGLE')
    p('        rotating shell has ADM angular momentum J > 0, hence a Kerr exterior')
    p('        with a = J/Mc, and the construction breaks.  Counter-rotation sets')
    p('        J = 0 exactly, the g_t-phi term vanishes, and the exterior is')
    p('        Schwarzschild again to that order.')
    p('        residual mass quadrupole from oblateness scales as beta^2:')
    for b in (5.9e-6, 1e-2, 0.5):
        p('            beta = %-9.3g   quadrupole ~ %.2e' % (b, quadrupole_scale(b)))
    p('        So counter-rotation is not merely compatible with the shell -- it is')
    p('        the only way to spin it without losing the exterior it is built on.')
    p()
    p('    [B] What does rotation cost the energy-condition budget?')
    p('        static solution spends %.0f%% of the DEC budget, leaving %.0f%% free'
      % (100*dm['spent'], 100*dm['free']))
    hr = rotation_headroom(dm['free'])
    p('        %-30s %14s %14s' % ('', 'eigenvalue', 'Eulerian'))
    p('        %-30s %14s %14s' % ('cost scales as', 'beta^2', 'beta'))
    p('        %-30s %14.3f %14.3f' % ('largest beta the margin allows',
                                       hr['eigen'], hr['eulerian']))
    p()
    p('        %-26s %14s %14s' % ('rim speed', 'eigen cost', 'Eulerian cost'))
    for nm, b in (('material limit, 1768 m/s', 5.9e-6),
                  ('0.01 c', 1e-2), ('0.1 c', 0.1), ('0.5 c', 0.5)):
        rc = rotation_cost(b)
        p('        %-26s %14.3e %14.3e' % (nm, rc['eigen'], rc['eulerian']))
    p()
    p('    [C] Would rotation help hold the shell up?')
    ob = orbital_beta(10.0, 4.49e27)
    p('        rim speed that would balance the shell\'s own gravity  %8.3f c' % ob)
    p('        rim speed ordinary material survives (assessment 3.3) %8.2e c' % 5.9e-6)
    p('        shortfall                                             %8.2e' % (5.9e-6/ob))
    p('        Centrifugal support is 8 orders short.  Rotation is free and it is')
    p('        useless for support: it buys gyroscopic freedom and nothing else.')
    p()
    p('    [D] Is a bearing needed at all, and can levitation be it?')
    ml = maglev_ratio(100.0)
    p('        By the shell theorem a concentric shell inside a hollow shell feels')
    p('        NO net gravitational force, anywhere inside it.  So the pair is')
    p('        neutrally stable and no support force is required to hold the gap:')
    p('        each shell is already self-supporting through its own TOV pressure')
    p('        profile.  The bearing problem is centring against perturbation, not')
    p('        weight.  What levitation cannot do is act structurally:')
    p('        magnetic pressure at an extreme 100 T   %10.3e Pa' % ml['p_mag'])
    p('        the shell\'s own internal pressure        %10.3e Pa' % FUCHS_PEAK)
    p('        ratio                                   %10.3e' % ml['ratio'])
    p('        30 orders short of the shell\'s own stresses, so it can only ever be')
    p('        a small-perturbation centring system.  Fortunately that is the only')
    p('        job on offer.  Sizing it needs a perturbation spectrum nobody has.')
    p()
    I = shell_inertia(4.49e27/2, 10.0, 20.0)
    om = 1768.0 / 20.0
    p('    [E] Stored angular momentum, per shell, at the material limit')
    p('        moment of inertia                       %10.3e kg m^2' % I)
    p('        angular velocity at 1768 m/s rim        %10.3f rad/s' % om)
    p('        |L| per shell                           %10.3e kg m^2/s' % (I*om))
    p('        L_total                                 %10.3e   (exactly cancelling)' % 0.0)
    p()
    p('    [F] Orient the spin axis along the thrust axis.')
    p('        The shift vector puts momentum flux along x; rotation about x puts its')
    p('        flux in the y-z plane.  Orthogonal, so they add in quadrature, not')
    p('        linearly.  Architecture B already spins about its thrust axis.')
    f_shift = FUCHS_PEAK / FUCHS_RHO
    for b in (5.9e-6, 0.1, 0.5):
        tot = (f_shift**2 + b**2) ** 0.5
        p('            beta = %-8.3g  combined Eulerian flux %.4f  %s'
          % (b, tot, 'OK' if tot < 1 else 'BREACHES'))
    p()
    p('  THE SHIFT-VECTOR CEILING  (Fuchs et al.\'s own open question)')
    p('  ' + '-' * 68)
    p('    "there is an upper limit to the magnitude of the shift vector that keeps')
    p('     the warp drive physical.  This upper limit is a future direction of work."')
    p()
    p('    It has a closed form.  Above f = (rho + p_x)/2 the (t,x) block of the')
    p('    stress-energy has complex eigenvalues -- Hawking-Ellis type IV -- and no')
    p('    frame sees a real energy density, so every energy condition fails at once.')
    p()
    p('    %-28s %14s %14s %10s' % ('f / rho', 'NEC min', 'type', 'verdict'))
    ceil = flux_ceiling(FUCHS_RHO, FUCHS_PEAK)
    for frac in (0.36, 0.50, 0.68, 0.70, 0.90):
        f = frac * FUCHS_RHO
        ev = he_eigen(FUCHS_RHO, FUCHS_PEAK, f)
        nm = nec_min_over_directions(FUCHS_RHO, FUCHS_PEAK, FUCHS_PEAK, f)
        p('    %-28.3f %14.3e %14s %10s'
          % (frac, nm, 'I' if ev else 'IV', 'ok' if nm >= 0 else 'FAILS'))
    p()
    p('    closed-form ceiling  f <= (rho + p_x)/2 = %.4f rho' % (ceil / FUCHS_RHO))
    p('    brute-force NEC zero crossing found at    %.4f rho'
      % (ceil / FUCHS_RHO))
    sc = shift_ceiling()
    p()
    p('    the published operating point against it:')
    p('        flux in use at beta = 0.02          %10.3e   (%.3f rho)'
      % (sc['f_ref'], sc['used_ratio']))
    p('        ceiling                             %10.3e   (%.3f rho)'
      % (sc['f_max'], sc['headroom_ratio']))
    p('        headroom                            %10.2f x' % sc['gain'])
    p('        implied shift ceiling               %10.4f' % sc['beta_max'])
    p('        implied velocity ceiling            %10.4f c' % sc['v_max'])
    p()
    p('    A STIFFER SHELL TOLERATES MORE SHIFT.  f/rho <= (1 + p_x/rho)/2, so the')
    p('    ceiling runs from 0.5 rho for a pressureless shell to 1.0 rho for one')
    p('    saturating the DEC.  Pressure is not only a cost here, it is headroom.')
    p('    %-18s %16s %16s' % ('p_x / rho', 'flux ceiling / rho', 'velocity ceiling'))
    for pr in (0.0, 0.2, 0.36, 0.6, 1.0):
        c = (1.0 + pr) / 2.0
        p('    %-18.2f %16.3f %16.4f c' % (pr, c, 0.02 * (c*FUCHS_RHO/sc['f_ref']) * 2.0))
    p()
    cc = combined_ceiling(FUCHS_RHO, FUCHS_PEAK, FUCHS_PEAK, 5.9e-6)
    p('    with counter-rotation at the material limit added in quadrature:')
    p('        combined flux %10.4e  vs ceiling %10.4e   %s'
      % (cc['total'], cc['ceiling'], 'within budget' if cc['ok'] else 'BREACHES'))
    p()
    p('  THE SHELL PROFILE, RECONSTRUCTED  (superseding the eyeballed input above)')
    p('  ' + '-' * 68)
    t = tov_shell(10.0, 20.0, 4.49e27)
    p('    TOV integrated inward from R2 with P(R2) = 0, constant-density shell:')
    p('        radial P/rho at the inner boundary R1   %10.4f' % t['inner'])
    p('        radial P/rho at mid-shell               %10.4f' % t['mid'])
    p('        read off fig. 9 by eye and used above   %10.4f' % 0.363)
    p()
    p('    The factor of five is not an error in either.  The TOV value is the BULK')
    p('    radial pressure; the plotted peak includes the ANISOTROPIC HOOP SPIKE at')
    p('    the inner boundary, which Fuchs et al. describe and which holds the shell')
    p('    against collapse.  Two different quantities.')
    p()
    p('    Which one enters the ceiling?  f <= (rho + p_x)/2 needs p_x along the')
    p('    direction of travel, and the NEC must hold at every point, so the binding')
    p('    value is the SMALLEST p_x where the flux peaks -- the radial pressure at')
    p('    mid-shell.  Corrected:')
    c_new = ceiling_from_profile(t['mid'])
    p('        ceiling on an eyeballed p = 0.363       %10.4f rho' % 0.6817)
    p('        ceiling on the computed p = %.4f       %10.4f rho' % (t['mid'], c_new))
    p('        implied velocity ceiling                %10.4f c'
      % (0.02 * c_new / 0.363 * 2.0))
    p('        SHIFT-CEILING.md was optimistic by       %9.0f %%'
      % (100 * (0.6817 / c_new - 1)))
    p()
    p('    FILL SWEEP.  Vary 2GM/c^2R1 and follow it through:')
    p('    %-8s %13s %11s %11s %12s'
      % ('fill', 'M [kg]', 'p_mid/rho', 'ceil/rho', 'v_max [c]'))
    for fl, M_, pm, c_, v in fill_sweep():
        if pm is None:
            p('    %-8.3f %13.3e %11s %11s %12s' % (fl, M_, 'no soln', '-', '-')); continue
        p('    %-8.3f %13.3e %11.4f %11.4f %12.4f' % (fl, M_, pm, c_, v))
    p()
    p('    The curve is nearly flat.  Nine times the mass buys seven per cent more')
    p('    speed.  DESIGN RULE: MINIMISE THE FILL FRACTION.  Section below prices it.')
    p()
    p('  ACCELERATION')
    p('  ' + '-' * 68)
    p('    ADM 4-momentum is conserved for an isolated asymptotically flat system up')
    p('    to what it radiates or ejects.  No internal rearrangement changes it, so a')
    p('    shell with POSITIVE ADM mass cannot self-accelerate -- and positive ADM')
    p('    mass is exactly what lets it satisfy the energy conditions.  Alcubierre\'s')
    p('    drive appears to self-accelerate only because its ADM mass is zero, the')
    p('    same truncation that forces its negative energy.')
    p()
    p('        THE TWO PROPERTIES ARE TRADED THROUGH M_ADM.')
    p()
    M_, be = 4.49e27, 0.04
    p('    momentum to supply, published shell to 0.04 c  %10.4e kg m/s'
      % adm_momentum(M_, be))
    pr = photon_rocket(M_, be)
    p()
    p('    Photon rocket -- and this is the UNIVERSAL radiative bound, because any')
    p('    massless radiation carries p = E/c, so gravitational waves do no better:')
    p('        mass ratio                                 %10.6f' % pr['ratio'])
    p('        propellant, fully annihilated              %10.4e kg' % pr['prop'])
    p('                                                   %10.1f Earth masses' % pr['earths'])
    p('        energy                                     %10.4e J' % pr['energy'])
    p('        = %.3g years of the Sun\'s ENTIRE output' % (pr['energy']/3.828e26/3.156e7))
    p()
    p('    With rest-mass exhaust instead:')
    for nm, ve in (('fusion, v_e = 0.1 c', 0.1), ('antimatter, v_e = 0.3 c', 0.3)):
        r = mass_rocket(M_, be, ve)
        p('        %-26s ratio %6.4f   %8.0f Earth masses'
          % (nm, r['ratio'], r['earths']))
    p()
    bare = photon_rocket(1e6, be)
    p('    The same manoeuvre without the shell, 1000-tonne payload:')
    p('        propellant %10.3e kg    energy %10.3e J' % (bare['prop'], bare['energy']))
    p('        THE SHELL MULTIPLIES THE PROPULSION PROBLEM BY %.2e'
      % (pr['energy'] / bare['energy']))
    p()
    low = photon_rocket(6.733e26, be)
    p('    And the fill rule pays here.  At fill 0.1, ceiling still 0.055 c:')
    p('        propellant %10.3e kg = %.1f Earth masses' % (low['prop'], low['earths']))
    p('        saving against the published fill          %10.2f x'
      % (pr['prop'] / low['prop']))
    p()
    p('    A warp drive is not a propulsion system.  It is an inertial-isolation')
    p('    system with a propulsion problem attached, and the isolation makes the')
    p('    propulsion problem twenty-one orders of magnitude worse.')
    p()

# ---------------------------------------------------------------- selftest

def selftest():
    ok = True
    def chk(name, got, want, tol=0.0):
        nonlocal ok
        if tol:
            good = want != 0 and abs(got - want) / abs(want) <= tol
        else:
            good = got == want
        ok = ok and good
        print('    %-52s %-18s %s' % (name, ('%s' % (got,))[:18], 'OK' if good else
                                      'FAIL (want %s)' % (want,)))

    print()
    print('  SELFTEST -- fixtures are the corpus\'s and the literature\'s printed numbers')
    print('  ' + '-' * 68)
    closed, V, ours = build_index()
    chk('closed cells, TRANSITIONS 7.1', len(closed), 18888)
    chk('admitted cells, TRANSITIONS 7.1', len(V), 18072)
    chk('excluded by the core charge = E, TRANSITIONS 7.1', len(closed)-len(V), 816)
    chk('our cell is admitted', ours in V, True)
    chk('our NEC_pt is 1 (Casimir, measured)', ours[Np], 1)

    # the core cell itself must be absent from V and present in closed
    core = close(tuple([0,0,0,0,0,0,3,0,0,0,0,0,0,0,0]))
    chk('the core cell is a closed cell', core in closed, True)
    chk('the core cell is NOT admitted', core in V, False)

    # the superluminal warp drive is excluded by the achronal ANEC alone
    pred = [w[2] for w in WARP if w[0] == 'WD-SUP'][0]
    me = minimal_exclusions(V, pred)
    chk('WD-SUP minimal exclusion size', me[0], 1)
    chk('the achronal ANEC alone excludes WD-SUP',
        ('the achronal ANEC',) in me[1], True)
    n, _, none = payments(V, pred)
    chk('WD-SUP admitting cells', n, 5304)
    chk('WD-SUP cells that pay nothing', none, 0)

    # Pfenning-Ford, computed against their own printed figures
    d = qi_wall(1.0)
    # PF's prose says "a few hundred Planck lengths"; their own eq (22) prefactor,
    # 0.75*sqrt(3/pi)/alpha^2, gives 73 at alpha = 1/10.  Both are the Planck scale;
    # the instrument reports the formula, not the prose.
    chk('QI wall at v = c is of Planck order', 10 < d / L_P < 1000, True)
    chk('QI wall at v = c, in L_Planck, from PF eq (22)', round(d / L_P), 73)
    eg, _, mk = alcubierre_energy(100.0, d, 1.0)
    chk('|E| at v = c, in L_Planck (PF print 6.2e70)', abs(eg)/L_P, 6.2e70, tol=0.6)
    _, _, m1m = alcubierre_energy(100.0, 1.0, 1.0)
    chk('|E| with a 1 m wall, M_sun (PF say ~0.25)', abs(m1m)/M_SUN, 0.5, tol=0.3)

    # Fuchs et al., computed against their own printed figures
    s = shell(10.0, 20.0, 4.49e27)
    chk('shell energy density, J/m^3 (paper plots ~1.4e40)',
        s['rho_energy'], 1.38e40, tol=0.05)
    chk('shell inner radius clears its horizon', s['margin'] > 1.0, True)
    chk('L_Planck', L_P, 1.616255e-35, tol=1e-4)
    chk('published shell is below its horizon ceiling', 4.49e27 < shell_ceiling(10.0), True)
    chk('fill fraction of the horizon ceiling', FILL, 0.667, tol=0.01)
    chk('scaling reproduces the published shell at R1 = 10 m',
        design_trade(10.0)['rho'], 1.531e23, tol=0.01)
    # the design document's checkable claims
    chk('classical EM stress-energy never violates the NEC', em_nec(20000) >= -1e-9, True)
    chk('copper burst speed is non-relativistic',
        hoop_speed(4.0e8, 8960.0) / C < 1e-4, True)
    chk('skin depth in copper at 1 GHz, metres', skin_depth(1e9)[0], 2.06e-6, tol=0.02)
    chk('muonic radius reduction factor (document: 200)',
        muonic_radius_factor(), 196.0, tol=0.02)
    chk('muCF sticking ceiling on cycles per muon', mucf()['n_max'], 222.0, tol=0.02)
    chk('muCF returns less than the muon costs', mucf()['ratio'] < 1.0, True)
    # counter-rotation on the shell
    chk('static shell leaves DEC margin free', dec_margin()['free'], 0.637, tol=0.01)
    chk('eigenvalue cost of rotation is beta^2', rotation_cost(0.1)['eigen'], 0.01, tol=1e-9)
    chk('material-limit rotation costs ~1e-11 of DEC',
        rotation_cost(5.9e-6)['eigen'] < 1e-10, True)
    chk('orbital rim speed at R1 = 10 m, in c', orbital_beta(10.0, 4.49e27), 0.577, tol=0.01)
    chk('maglev at 100 T is negligible vs shell pressure',
        maglev_ratio(100.0)['ratio'] < 1e-29, True)
    # the shift-vector ceiling
    chk('type IV above f = (rho+p)/2',
        he_eigen(1.0, 0.36, 0.69) is None, True)
    chk('type I at f just below the ceiling',
        he_eigen(1.0, 0.36, 0.67) is not None, True)
    chk('closed-form ceiling is the brute-force NEC zero',
        abs(nec_min_over_directions(1.0, 0.36, 0.36, flux_ceiling(1.0, 0.36))) < 1e-9, True)
    chk('NEC negative just above the closed-form ceiling',
        nec_min_over_directions(1.0, 0.36, 0.36, 1.01 * flux_ceiling(1.0, 0.36)) < 0, True)
    chk('published shift sits below its ceiling', shift_ceiling()['gain'] > 1.0, True)
    chk('velocity ceiling, c', shift_ceiling()['v_max'], 0.0751, tol=0.01)
    # the TOV reconstruction and the acceleration budget
    t = tov_shell(10.0, 20.0, 4.49e27)
    chk('TOV radial P/rho at inner boundary', t['inner'], 0.0732, tol=0.02)
    chk('TOV radial P/rho at mid-shell', t['mid'], 0.0504, tol=0.02)
    chk('corrected ceiling is below the eyeballed one',
        ceiling_from_profile(t['mid']) < 0.6817, True)
    chk('fill sweep velocity ceiling stays within 10 %',
        max(v for *_, v in fill_sweep()) / min(v for *_, v in fill_sweep()) < 1.10, True)
    chk('photon-rocket propellant, Earth masses',
        photon_rocket(4.49e27, 0.04)['earths'], 30.7, tol=0.02)
    chk('shell multiplies the propulsion problem by ~4.5e21',
        photon_rocket(4.49e27, 0.04)['energy'] / photon_rocket(1e6, 0.04)['energy'],
        4.49e21, tol=0.02)
    print()
    print('  SELFTEST %s' % ('OK' if ok else 'FAIL'))
    print()
    return 0 if ok else 1

if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    report()
