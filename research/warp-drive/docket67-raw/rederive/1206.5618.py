#!/usr/bin/env python3
"""
DOCKET 67 re-derivation for C. Wang, arXiv:1206.5618v12 = Can. J. Phys. 93, 1470 (2015), eq. (20).

Published eq. (20) (READ at source; operator glyphs recovered from the text layer by the paper's
own consistent glyph use in footnotes 8/9, where the same two glyphs render '=' and '+'):

    oint_S dS_l (Omega^{l mu} X^i) = int_V (d_l Omega^{l mu}) X^i d^3x + int_V Omega^{i mu} d^3x ,
    i, l = 1, 2, 3 (left-divergence, row-four-vector), with d/dt = 0 so that d_l Omega^{l mu}
    is the full 4-divergence.

The tree (tolman.py:131-138) uses the divergence-free special case
    oint_S dS_l (Theta^{l mu} X^i) = int_V Theta^{i mu} d^3x
and traces it on a sphere: LHS = 4 pi R^3 <T^r_r>(R), RHS = int_V Theta^{ii}.

Checks (all exact, sympy):
  C1  GENERAL eq. (20), divergence term KEPT, on a BALL, for a generic non-symmetric,
      non-divergence-free polynomial tensor.                       -> residual 0
  C2  The same on a CUBE (region not a ball): eq. (20) does not need a ball.   -> residual 0
  C3  A NON-CONSTANT, NON-SPHERICAL, divergence-free symmetric stress (Maxwell/Beltrami stress
      function Theta_ij = delta_ij Lap(phi) - d_i d_j phi): identity holds on the ball and the
      traced LHS equals 4 pi R^3 <n.Theta.n>.                      -> residual 0
  C4  Constant plate stress diag(p_t,p_t,p_z): <T^r_r> = (2p_t+p_z)/3 (tolman F3); W5
      (p_t=-5, p_z=1): <T^r_r> = -3, e = -9, m = e V = 4 pi R^3 <T^r_r>; and the raw-cell
      factor of 9 (tolman.py:555-557).
  C5  REGULARITY is a hypothesis: Coulomb stress is divergence-free on r>0; on a SHELL a<r<R the
      identity holds exactly; on the BALL the LHS is finite (-q^2/(8 pi R)) and the RHS diverges.
  C6  TIME-INDEPENDENCE is a hypothesis: for a conserved but time-dependent tensor the 3-divergence
      is -d_t Theta^{0 mu} != 0 and the divergence-free form fails by exactly that term.
  C7  INDEX ORDER: for a NON-symmetric tensor, left-divergence-free does not give the
      right-contracted identity (eq. 21 vs 20); for a symmetric tensor they coincide.
  C8  SIGNATURE: Wang uses diag(-1,-1,-1,+1); T^r_r (mixed) = -T^{rr} there, = +T^{rr} in the
      tree's mostly-plus convention.  The upper-index spatial block is the pressure tensor in
      both (Wang Sect. 4: T^{ii} = 0.5 eps0 E^2 = W_em for electrostatics).
"""
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
r, th, ph = sp.symbols('r theta phi', positive=True)
R, a, q = sp.symbols('R a q', positive=True)
X = [x, y, z]
sph = {x: r*sp.sin(th)*sp.cos(ph), y: r*sp.sin(th)*sp.sin(ph), z: r*sp.cos(th)}
n = [sp.sin(th)*sp.cos(ph), sp.sin(th)*sp.sin(ph), sp.cos(th)]
results = []


def rec(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))


def ball_int(f):
    g = sp.expand(f.subs(sph)) * r**2 * sp.sin(th)
    return sp.simplify(sp.integrate(g, (r, 0, R), (th, 0, sp.pi), (ph, 0, 2*sp.pi)))


def sphere_int(f):  # f evaluated on r = R, times R^2 dOmega
    g = sp.expand(f.subs(sph).subs(r, R)) * R**2 * sp.sin(th)
    return sp.simplify(sp.integrate(g, (th, 0, sp.pi), (ph, 0, 2*sp.pi)))


def cube_int(f):
    return sp.integrate(f, (x, -1, 1), (y, -1, 1), (z, -1, 1))


def cube_surface(F):  # oint dS_l F_l over [-1,1]^3, F a 3-vector
    s = 0
    for l, v in enumerate(X):
        others = [w for w in X if w != v]
        s += sp.integrate(F[l].subs(v, 1) - F[l].subs(v, -1), (others[0], -1, 1), (others[1], -1, 1))
    return sp.expand(s)


# ---------------- C1 / C2  general eq. (20), generic tensor, divergence term kept
coef = sp.symbols('c0:40')
mono = [1, x, y, z, x*y, y*z, z*x, x**2, y**2, z**2]
k = iter(range(40))
Om = sp.zeros(3, 4)   # Omega^{l mu}, l = spatial row index, mu = 0..3 (mu=3 plays the role of '4')
import random
random.seed(20260926)
for l in range(3):
    for mu in range(4):
        Om[l, mu] = sum(sp.Integer(random.randint(-5, 5)) * m_ for m_ in mono)

ok_ball = ok_cube = True
for i in range(3):
    for mu in range(4):
        div = sum(sp.diff(Om[l, mu], X[l]) for l in range(3))
        # the Omega^{i mu} of eq (20) is the spatial row i of the SAME tensor
        rhs_integrand = div * X[i] + Om[i, mu]
        lhs = sphere_int(sum(n[l] * Om[l, mu] * X[i] for l in range(3)))
        rhs = ball_int(rhs_integrand)
        if sp.simplify(lhs - rhs) != 0:
            ok_ball = False
        lhs_c = cube_surface([Om[l, mu] * X[i] for l in range(3)])
        rhs_c = cube_int(rhs_integrand)
        if sp.simplify(lhs_c - rhs_c) != 0:
            ok_cube = False
rec("C1 eq.(20) GENERAL form (divergence term kept), ball, 12 (i,mu) pairs, generic non-symmetric tensor", ok_ball)
rec("C2 eq.(20) GENERAL form on a CUBE -- the region need not be a ball", ok_cube)

# dropping the divergence term is wrong unless divergence-free:
i, mu = 0, 0
div = sum(sp.diff(Om[l, mu], X[l]) for l in range(3))
lhs = sphere_int(sum(n[l]*Om[l, mu]*X[i] for l in range(3)))
rec("C1b without divergence-free, the tree's short form FAILS (guard against vacuity)",
    sp.simplify(lhs - ball_int(Om[i, mu])) != 0,
    "residual = int (d_l Om^{l mu}) X^i = %s" % sp.simplify(ball_int(div*X[i])))

# ---------------- C3  non-constant, non-spherical, divergence-free symmetric stress
phi = x**3*y + 2*y**2*z**2 - x*z**3 + x**2*y*z + 3*z**4
Th = sp.Matrix(3, 3, lambda I, J: (sp.KroneckerDelta(I, J) * sum(sp.diff(phi, v, 2) for v in X)
                                   - sp.diff(phi, X[I], X[J])))
divs = [sp.simplify(sum(sp.diff(Th[l, j], X[l]) for l in range(3))) for j in range(3)]
rec("C3a Maxwell stress-function tensor is divergence-free and symmetric",
    all(d == 0 for d in divs) and Th == Th.T)
nonsph = sp.simplify(Th[0, 0] - Th[1, 1]) != 0 and any(sp.diff(Th[I, J], v) != 0 for I in range(3) for J in range(3) for v in X)
rec("C3b ... and it is NON-constant and NON-spherical (Theta_xx != Theta_yy, spatially varying)", nonsph)
ok = True
for i in range(3):
    for j in range(3):
        lhs = sphere_int(sum(n[l]*Th[l, j]*X[i] for l in range(3)))
        if sp.simplify(lhs - ball_int(Th[i, j])) != 0:
            ok = False
rec("C3c tree's short form (divergence-free) holds for all 9 (i,j) on the ball", ok)
traced_lhs = sphere_int(sum(n[l]*Th[l, i]*X[i] for l in range(3) for i in range(3)))
TrrR = sum(n[I]*n[J]*Th[I, J] for I in range(3) for J in range(3))
avg = sp.simplify(sp.integrate(sp.expand(TrrR.subs(sph).subs(r, R))*sp.sin(th), (th, 0, sp.pi), (ph, 0, 2*sp.pi)) / (4*sp.pi))
rec("C3d traced LHS == 4 pi R^3 <n.Theta.n>(R) == int_V Theta^{ii}",
    sp.simplify(traced_lhs - 4*sp.pi*R**3*avg) == 0 and sp.simplify(traced_lhs - ball_int(Th.trace())) == 0,
    "4 pi R^3 <T^r_r> = %s" % sp.factor(4*sp.pi*R**3*avg))
# single-direction read differs from the average for this source (tree F6's point, non-constant case)
Tzz_pole = sp.simplify(Th[2, 2].subs({x: 0, y: 0, z: R}))
rec("C3e single-direction read (z-pole T_zz) != angular average for this non-spherical source",
    sp.simplify(Tzz_pole - avg) != 0, "T_zz(pole)=%s vs <T^r_r>=%s" % (Tzz_pole, avg))

# ---------------- C4  constant plate stress, W5, factor 9
pt, pz, u0 = sp.symbols('p_t p_z u_0', real=True)
P = sp.diag(pt, pt, pz)
avgP = sp.simplify(sp.integrate(sum(n[I]*n[J]*P[I, J] for I in range(3) for J in range(3))*sp.sin(th),
                                (th, 0, sp.pi), (ph, 0, 2*sp.pi)) / (4*sp.pi))
rec("C4a <T^r_r> = (2 p_t + p_z)/3 for diag(p_t,p_t,p_z)", sp.simplify(avgP - (2*pt+pz)/3) == 0)
V = sp.Rational(4, 3)*sp.pi*R**3
w5 = {pt: -5, pz: 1}
e = 2*pt + pz  # traceless: -e + 2p_t + p_z = 0
rec("C4b W5: <T^r_r> = -3, e = -9, m = eV = 4 pi R^3 <T^r_r> < 0 while p_z = +1 > 0",
    avgP.subs(w5) == -3 and e.subs(w5) == -9 and sp.simplify(e.subs(w5)*V - 4*sp.pi*R**3*avgP.subs(w5)) == 0)
ratio = sp.simplify((4*sp.pi*R**3*(-3*u0)) / (V*(-u0)))
rec("C4c raw-cell misread 4 pi R^3 (-3u_0) vs (4/3) pi R^3 (-u_0): factor", ratio == 9, "ratio = %s" % ratio)

# ---------------- C5  Coulomb: regularity (Gauss theorem) is load-bearing
# mostly-plus, Gaussian-like units with u = E^2/2 (constants irrelevant): E = q/(4 pi r^2) n
E2 = (q/(4*sp.pi*r**2))**2
Trr = -E2/2            # radial tension
Tii = E2/2             # spatial trace (= u, traceless)
lhs_R = 4*sp.pi*R**3*Trr.subs(r, R)
lhs_a = 4*sp.pi*a**3*Trr.subs(r, a)
rhs_shell = sp.integrate(4*sp.pi*r**2*Tii, (r, a, R))
rec("C5a SHELL a<r<R (multiply connected, as Wang allows): outer - inner surface = volume trace",
    sp.simplify(lhs_R - lhs_a - rhs_shell) == 0, "both = %s" % sp.simplify(rhs_shell))
rhs_ball = sp.limit(rhs_shell, a, 0, '+')
rec("C5b BALL with the singular centre: LHS finite, RHS divergent -> identity FAILS without regularity",
    rhs_ball == sp.oo and sp.simplify(lhs_R) == -q**2/(8*sp.pi*R), "LHS = %s, RHS = %s" % (sp.simplify(lhs_R), rhs_ball))

# ---------------- C6  time-independence
t = sp.Symbol('t', real=True); w = sp.Symbol('omega', positive=True)  # positive: a real omega made integrate() return a Piecewise (omega=0 branch)
# conserved but time-dependent: Theta^{00}=f, Theta^{0i}=Theta^{i0}= g_i, with d_t f + d_i g_i = 0;
# the mu=0 column: 3-divergence d_l Theta^{l0} = d_l g_l = -d_t Theta^{00}
g = [x**2*sp.cos(w*t), 0, 0]   # (first draft used x*cos: the gap vanished by parity -- a vacuous test, replaced)
f00 = -sp.integrate(sum(sp.diff(g[l], X[l]) for l in range(3)), t)   # f = -sin(wt)/w
cons = sp.simplify(sp.diff(f00, t) + sum(sp.diff(g[l], X[l]) for l in range(3)))
i = 0
lhs = sphere_int(sum(n[l]*g[l]*X[i] for l in range(3)))
short = ball_int(g[i])
gap = sp.simplify(lhs - short)
rec("C6 conserved (4-div 0) but time-dependent: short form fails by int (-d_t Theta^{00}) X^i",
    cons == 0 and gap != 0 and sp.simplify(gap - ball_int(-sp.diff(f00, t)*X[i])) == 0,
    "gap = %s" % gap)

# ---------------- C7  index order for a non-symmetric tensor
A = sp.Matrix([[0, 0, 0], [x**2/2, 0, 0], [0, 0, 0]])  # A^{10} = x^2/2: left-div (d_y A^{10}) = 0, right-div of row 1 (d_x A^{10}) = x
# (first draft put x at A^{01}, which is left-div-NONfree -- a wrong fixture, replaced)
leftdiv = [sp.simplify(sum(sp.diff(A[l, j], X[l]) for l in range(3))) for j in range(3)]
rightdiv = [sp.simplify(sum(sp.diff(A[j, l], X[l]) for l in range(3))) for j in range(3)]
# eq (21)-type contraction on the SECOND index with the left-divergence-free premise:
i, j = 0, 1
lhs21 = sphere_int(sum(n[l]*A[j, l]*X[i] for l in range(3)))
rhs_short21 = ball_int(A[j, i])
rec("C7 non-symmetric A: left-div-free=%s, right-div-free=%s; the second-index (eq.21) short form fails"
    % (all(d == 0 for d in leftdiv), all(d == 0 for d in rightdiv)),
    all(d == 0 for d in leftdiv) and not all(d == 0 for d in rightdiv) and sp.simplify(lhs21 - rhs_short21) != 0)

# ---------------- C8  signature bookkeeping
g_mm = sp.diag(-1, -1, -1, 1)   # Wang, index 4 = time
g_mp = sp.diag(1, 1, 1, -1)     # mostly plus, same index order
Tup = sp.diag(*sp.symbols('p1 p2 p3', real=True), sp.Symbol('W'))
mixed_mm = (Tup * g_mm)[0, 0]
mixed_mp = (Tup * g_mp)[0, 0]
rec("C8 T^1_1 = -T^{11} in Wang's diag(-1,-1,-1,+1); = +T^{11} in mostly-plus (tree's p_r = T^r_r)",
    mixed_mm == -Tup[0, 0] and mixed_mp == Tup[0, 0])

nf = sum(1 for _, ok, _ in results if not ok)
print("\n%d checks, %d failed" % (len(results), nf))
raise SystemExit(1 if nf else 0)
