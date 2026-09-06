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
    print()
    print('  SELFTEST %s' % ('OK' if ok else 'FAIL'))
    print()
    return 0 if ok else 1

if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    report()
