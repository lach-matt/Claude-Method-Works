#!/usr/bin/env python3
"""grflyby.py -- relativistic flyby: Schwarzschild deflection and the slingshot.

THE-BORROWED-WELL.md derived dv_max/c = sqrt(r_s/b) with an optimal 90-degree
turn, Newtonianly, and marked its strong-field rows "indicative only, scale
trustworthy, digits not".  This discharges that caveat.

Units G = c = 1, lengths in Schwarzschild radii (r_s = 2M = 1).  Stdlib only.
    python3 grflyby.py --selftest
"""
import math, sys

# ------------------------------------------------------------------ geodesic

def _cubic_roots(a2, a1, a0):
    """Real roots of u^3 + a2 u^2 + a1 u + a0, by trigonometric/Cardano form."""
    Q = (3.0*a1 - a2*a2) / 9.0
    R = (9.0*a2*a1 - 27.0*a0 - 2.0*a2**3) / 54.0
    D = Q**3 + R*R
    if D < 0.0:
        th = math.acos(max(-1.0, min(1.0, R / math.sqrt(-Q**3))))
        s = 2.0*math.sqrt(-Q)
        return [s*math.cos(th/3.0) - a2/3.0,
                s*math.cos((th + 2*math.pi)/3.0) - a2/3.0,
                s*math.cos((th + 4*math.pi)/3.0) - a2/3.0]
    sd = math.sqrt(D)
    cb = lambda x: math.copysign(abs(x)**(1.0/3.0), x)
    return [cb(R + sd) + cb(R - sd) - a2/3.0]

def turning_point(b, v):
    """Closest approach as u = r_s/r.  None means the orbit is captured.

    (du/dphi)^2 = u^3 - u^2 + u/(gamma^2 v^2 b^2) + 1/b^2   with r_s = 1."""
    g2 = 1.0/(1.0 - v*v)
    A, B = 1.0/(g2*v*v*b*b), 1.0/(b*b)
    pos = sorted(x for x in _cubic_roots(-1.0, A, B) if x > 0.0)
    return pos[0] if pos else None

def deflection(b, v, n=8000):
    """Total deflection angle in radians, or None if captured.

    u = u1 sin^2(psi) removes the inverse-square-root singularity at the
    turning point; f/(u1-u) = -q(u) with q the deflated quadratic, so nothing
    is ever evaluated as 0/0."""
    u1 = turning_point(b, v)
    if u1 is None: return None
    A = 1.0/((1.0/(1.0 - v*v))*v*v*b*b)
    q = lambda u: u*u + (u1 - 1.0)*u + (u1*u1 - u1 + A)
    tot = 0.0
    for i in range(n):
        psi = (i + 0.5)*(math.pi/2)/n
        val = -q(u1*math.sin(psi)**2)
        if val > 0.0:
            tot += 2.0*math.sqrt(u1)*math.sin(psi)/math.sqrt(val)
    return 2.0*tot*(math.pi/2)/n - math.pi

def capture_b(v, lo=1.0, hi=1e4):
    """Largest impact parameter that is still captured.  -> 3sqrt(3)/2 as v->1."""
    for _ in range(90):
        m = 0.5*(lo + hi)
        if turning_point(m, v) is None: lo = m
        else: hi = m
    return hi

def b_for_angle(v, target=math.pi):
    """Impact parameter giving a chosen net deflection.  Strong-field lensing
    makes the deflection diverge at the capture boundary, so a FULL REVERSAL is
    reachable at every v -- which is what the Newtonian treatment could not do."""
    lo, hi = capture_b(v)*(1 + 1e-6), capture_b(v)*40.0
    for _ in range(70):
        m = 0.5*(lo + hi)
        th = deflection(m, v, n=4000)
        if th is None or th > target: lo = m
        else: hi = m
    return 0.5*(lo + hi)

# ----------------------------------------------------------------- slingshot

def slingshot(U, theta):
    """Ship at rest in the lab, deflector moving at U.  In the deflector frame
    the ship arrives at speed U and is turned by theta; transform back."""
    gU = 1.0/math.sqrt(1.0 - U*U)
    wx, wy = -U*math.cos(theta), U*math.sin(theta)
    den = 1.0 + wx*U
    return math.hypot((wx + U)/den, wy/(gU*den))

def newtonian_dv(b, U):
    """The comparison: dv = 2U sin(theta/2), tan(theta/2) = GM/(b U^2), r_s = 1."""
    return 2.0*U*math.sin(math.atan(1.0/(2.0*b*U*U)))

def tidal_mass_floor(b_over_rs, a_tide=9.8, d=20.0):
    """Smallest deflector for which a pass at b/r_s stays inside a tidal limit.
    Tides at fixed b/r_s go as 1/M^2, so this is a FLOOR on the deflector mass."""
    C, G, MS = 2.99792458e8, 6.6743e-11, 1.989e30
    return math.sqrt(d*C**6/(4.0*b_over_rs**3*G*G*a_tide))/MS

# ------------------------------------------------------------------ selftest

def selftest():
    ok = True
    def chk(name, got, want, tol=0.0):
        nonlocal ok
        good = (got == want) if not tol else (want != 0 and abs(got-want)/abs(want) <= tol)
        ok = ok and good
        print('    %-52s %-16s %s' % (name, ('%s' % (got,))[:16],
                                      'OK' if good else 'FAIL (want %s)' % (want,)))
    print('\n  SELFTEST -- against closed-form limits of general relativity\n')
    chk('photon bending -> 2 r_s / b', deflection(1e5, 0.999999), 2.0/1e5, tol=1e-3)
    chk('newtonian limit, b=1e4 v=0.01',
        deflection(1e4, 0.01), 2*math.atan(1.0/(2*1e4*1e-4)), tol=1e-3)
    chk('photon capture b -> 3 sqrt(3) / 2', capture_b(0.999999), 3*math.sqrt(3)/2, tol=1e-3)
    chk('slow-particle capture b -> 2/v', capture_b(0.01)*0.01, 2.0, tol=1e-2)
    chk('full reversal composes to 2U/(1+U^2)',
        slingshot(0.3, math.pi), 2*0.3/(1+0.09), tol=1e-9)
    chk('deflection diverges at the capture boundary',
        deflection(capture_b(0.35)*1.0001, 0.35) > 2*math.pi, True)
    chk('a full reversal is reachable at U = 0.35',
        abs(deflection(b_for_angle(0.35), 0.35) - math.pi) < 1e-3, True)
    chk('GR = Newtonian in weak field (b = 2205 r_s)',
        slingshot(0.0151, deflection(2205.0, 0.0151))/newtonian_dv(2205.0, 0.0151),
        1.0, tol=0.01)
    chk('GR beats Newtonian in strong field (b = 6.6 r_s)',
        slingshot(0.35, deflection(6.59, 0.35))/newtonian_dv(6.59, 0.35) > 1.5, True)
    chk('1 g full-reversal pass needs an IMBH', tidal_mass_floor(6.59) > 5e3, True)
    print('\n  SELFTEST %s\n' % ('OK' if ok else 'FAIL'))
    return 0 if ok else 1

def report():
    print('\n  RELATIVISTIC FLYBY\n  ' + '-'*68)
    print('    %-8s %11s %11s %13s %11s %9s'
          % ('U/c', 'b_crit', 'b(theta=pi)', 'dv = 2U/(1+U^2)', 'Newtonian', 'GR/Newt'))
    for U in (0.05, 0.10, 0.20, 0.35, 0.50, 0.70):
        bc, bp = capture_b(U), b_for_angle(U)
        dv, nw = slingshot(U, math.pi), newtonian_dv(bp, U)
        print('    %-8.2f %11.4f %11.4f %13.4f %11.4f %9.3f'
              % (U, bc, bp, dv, nw, dv/nw))
    print('\n    TIDAL FLOOR on the deflector for a full-reversal pass')
    print('    %-8s %12s %14s %14s' % ('U/c', 'b(pi)/r_s', 'M, 1 g [Msun]', 'M, 10 g'))
    for U in (0.10, 0.20, 0.35, 0.50):
        bp = b_for_angle(U)
        print('    %-8.2f %12.3f %14.3e %14.3e'
              % (U, bp, tidal_mass_floor(bp), tidal_mass_floor(bp, 98.0)))
    print()

if __name__ == '__main__':
    sys.exit(selftest() if '--selftest' in sys.argv else (report() or 0))
