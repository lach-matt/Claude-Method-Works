#!/usr/bin/env python3
"""
DOCKET 67 -- audit: positive-mass-theorem-rigidity
(M_ADM = 0 under the DEC implies Minkowski), as used at
research/warp-drive/concentric.py:51-53, 126-138, 274-275, 353-355
(argument itself in pair.py:115-149, 304-329).

Reads nothing from research/; the seated device parameters are copied from
concentric.py:155-157 (A_CORE = 0.02, R_SHELL = 200) and the m window
5e-3 .. 4e-2 (concentric.py:357) and the design point m = 5e-3.

The device's spatial slice (static, so k = 0, time-symmetric):
    g = psi(r) delta,  psi = 1 - 2 Phi,
    Phi = m/sqrt(r^2+a^2) - m/max(r, R_s)
Write g = u^4 delta, u = psi^(1/4).

R1  sympy: scalar curvature of psi(r)(dr^2 + r^2 dOmega^2) from Christoffels
    equals -8 u^-5 (u'' + 2u'/r)  (the conformal formula used below).
R2  sympy: ADM energy E = -2 lim r^2 u' = lim r^2 Phi' = 0 EXACTLY outside R_s
    (EHLS/Huang-Lee Def. of E, flux form); fall-off g - delta = O(r^-3).
R3  the hypotheses the published theorem needs, checked on the device:
    one end, no boundary, complete (psi bounded between positive constants),
    AF fall-off, R in L^1; REGULARITY: g is only Lipschitz at R_s (Phi' jumps),
    below the C^2 of EHLS Def.3 / Huang-Lee Def.2.5 -- the mean-curvature jump
    is computed (H_- > H_+, a positive-energy corner).
R4  exact R at the core, every m in the window: R(0) < 0.  So mu = R/2 < 0 at the
    core: the time-symmetric DEC (R >= 0) fails, by direct computation, with
    no appeal to the theorem.
R5  the identity for conformally flat data on R^3:
        E = -(1/2pi) Int d(Lap u)  (a measure; shell = atom on r = R_s)
    evaluated numerically: core part < 0, shell part > 0, sum = 0 = E.
R6  ELEMENTARY RIGIDITY for the device's class (conformally flat, Lipschitz
    u > 0 on R^3, Lap u a finite signed measure, u -> 1):  R >= 0  <=>
    Lap u <= 0 (u > 0);  E = 0  <=>  Int d(Lap u) = 0;  so Lap u = 0, u harmonic
    (Weyl), bounded, -> 1, hence u == 1 (Liouville): FLAT.  The finite step
    (nonpositive terms summing to zero are all zero) is discharged by z3 for a
    50-cell discretisation; Weyl's lemma and Liouville are NAMED, not checked.
R7  z3: the tree's contrapositive (E = 0 & not-flat & hypotheses |= not-DEC)
    is valid; dropping the DEC, completeness or AF from the premises blocks it.
R8  sympy: COMPLETENESS IS LOAD-BEARING.  u = 1 - c/r^3 on r > r0 > c^(1/3):
    R > 0 everywhere, E = 0 exactly, not flat -- an incomplete (bounded-away,
    with inner boundary) counterexample to rigidity-without-completeness.
R9  the tree's non-Minkowski witness: the static K = 0 slice of Minkowski
    orthogonal to a timelike Killing field is flat, so a curved K = 0 slice
    (R(0) != 0, computed) is sufficient; the linearised conjugate point is not
    needed.
Exit 0 iff every check passes.
"""
import sys
import sympy as sp
import mpmath as mp
import z3

OK = True


def chk(label, cond):
    global OK
    OK = OK and bool(cond)
    print("  [%s] %s" % ("ok" if cond else "FAIL", label))


A_CORE, R_SHELL, M_DESIGN = 0.02, 200.0, 5e-3
M_WINDOW = (5e-3, 1e-2, 2e-2, 4e-2)

r, th, ph = sp.symbols("r theta phi", positive=True)
m, a, Rs, c, r0 = sp.symbols("m a R_s c r0", positive=True)

# ---------------------------------------------------------------- R1
print("R1  scalar curvature of psi(r)(dr^2 + r^2 dOmega^2), from Christoffels")
psi = sp.Function("psi")(r)
x = [r, th, ph]
g = sp.diag(psi, psi * r**2, psi * r**2 * sp.sin(th)**2)
gi = g.inv()
n = 3
Gam = [[[sp.simplify(sum(gi[i, l] * (sp.diff(g[l, j], x[k]) + sp.diff(g[l, k], x[j])
                                     - sp.diff(g[j, k], x[l])) for l in range(n)) / 2)
         for k in range(n)] for j in range(n)] for i in range(n)]


def ricci(j, k):
    s = 0
    for i in range(n):
        s += sp.diff(Gam[i][j][k], x[i]) - sp.diff(Gam[i][j][i], x[k])
        for l in range(n):
            s += Gam[i][i][l] * Gam[l][j][k] - Gam[i][k][l] * Gam[l][j][i]
    return s


Rscal = sp.simplify(sum(gi[j, k] * ricci(j, k) for j in range(n) for k in range(n)))
u = psi ** sp.Rational(1, 4)
Rconf = -8 * u**-5 * (sp.diff(u, r, 2) + 2 * sp.diff(u, r) / r)
chk("R[psi delta] == -8 u^-5 (u'' + 2u'/r), u = psi^(1/4)",
    sp.simplify(Rscal - Rconf) == 0)

# ---------------------------------------------------------------- R2
print("R2  ADM energy of the device slice, exact")
Phi_out = m / sp.sqrt(r**2 + a**2) - m / r
Phi_in = m / sp.sqrt(r**2 + a**2) - m / Rs
psi_out = 1 - 2 * Phi_out
u_out = psi_out ** sp.Rational(1, 4)
E_u = sp.limit(-2 * r**2 * sp.diff(u_out, r), r, sp.oo)
E_phi = sp.limit(r**2 * sp.diff(Phi_out, r), r, sp.oo)
chk("E = -2 lim r^2 u' = 0 exactly (got %s)" % E_u, sp.simplify(E_u) == 0)
chk("E = lim r^2 Phi' = 0 exactly (got %s)" % E_phi, sp.simplify(E_phi) == 0)
lead = sp.limit(Phi_out * r**3, r, sp.oo)
chk("Phi = -m a^2/(2 r^3) + ...: g - delta = O(r^-3), inside q in (1/2,1) (lead %s)" % lead,
    sp.simplify(lead + m * a**2 / 2) == 0)
# the first (wrong) potential in concentric.py:276 has E = -m
bad = m / sp.sqrt(r**2 + a**2) - m / Rs
chk("control: the Plummer core alone (concentric.py:276's 'bad' potential less its constant) has E = lim r^2 Phi' = -m",
    sp.simplify(sp.limit(r**2 * sp.diff(m / sp.sqrt(r**2 + a**2), r), r, sp.oo) + m) == 0)
# Schwarzschild isotropic control: u = 1 + M/(2r) gives E = M
M = sp.symbols("M", real=True)
chk("control: isotropic Schwarzschild u = 1 + M/2r gives E = M",
    sp.simplify(sp.limit(-2 * r**2 * sp.diff(1 + M / (2 * r), r), r, sp.oo) - M) == 0)

# ---------------------------------------------------------------- R3
print("R3  the published hypotheses, on the device (m in window, a = 0.02, R_s = 200)")
psi0 = sp.simplify((1 - 2 * Phi_in).subs(r, 0))
m_star = sp.solve(sp.Eq(psi0, 0), m)[0]
m_star_v = float(m_star.subs({a: A_CORE, Rs: R_SHELL}))
chk("psi(0) = 1 - 2m/a + 2m/R_s; psi(0) = 0 at m* = a R_s/(2(R_s - a)) = %.7f (got %s)"
    % (m_star_v, m_star), sp.simplify(m_star - a * Rs / (2 * (Rs - a))) == 0)
RIEMANNIAN = {}
for mv in M_WINDOW + (8e-3, 9.9e-3):
    sub = {m: mv, a: A_CORE, Rs: R_SHELL}
    # psi range: Phi is max at r=0 (Phi_in decreasing), Phi_out < 0 so psi > 1 outside
    f_in = sp.lambdify(r, (1 - 2 * Phi_in).subs(sub), "mpmath")
    f_out = sp.lambdify(r, (1 - 2 * Phi_out).subs(sub), "mpmath")
    grid_in = [mp.mpf(R_SHELL) * k / 4000 for k in range(0, 4001)]
    grid_out = [mp.mpf(R_SHELL) * (1 + k / 50.0) for k in range(0, 2000)]
    lo = min(min(f_in(t) for t in grid_in), min(f_out(t) for t in grid_out))
    hi = max(max(f_in(t) for t in grid_in), max(f_out(t) for t in grid_out))
    RIEMANNIAN[mv] = bool(lo > 0)
    print("       m=%.1e: psi in [%+.5f, %.8f] -> %s" % (mv, lo, hi,
          "Riemannian, bounded between positive constants: complete, no boundary, one end"
          if lo > 0 else "NOT A RIEMANNIAN METRIC at the core (psi <= 0): no initial data set, the theorem is silent"))
    chk("m=%.1e: Riemannian iff m < m* (%s)" % (mv, RIEMANNIAN[mv]), RIEMANNIAN[mv] == (mv < m_star_v))
chk("FINDING (recorded): of the tree's window 5e-3..4e-2 (concentric.py:77-78, 360), the literal "
    "slice (1-2Phi) delta is Riemannian only for m < %.7f; at m = 2e-2 (the 'best relative lead') "
    "and 4e-2 it is not" % m_star_v,
    RIEMANNIAN[5e-3] and not RIEMANNIAN[2e-2] and not RIEMANNIAN[4e-2])
# mean curvature jump at R_s: H = psi^(-1/2)(2/r + psi'/psi)
dpsi_in = sp.diff(1 - 2 * Phi_in, r)
dpsi_out = sp.diff(1 - 2 * Phi_out, r)
jump = sp.simplify((dpsi_out - dpsi_in).subs(r, Rs))
chk("psi' jumps at R_s by %s (Lipschitz metric: below C^2 of EHLS Def.3 / HL Def.2.5)" % jump,
    sp.simplify(jump + 2 * m / Rs**2) == 0)
psiRs = (1 - 2 * Phi_in).subs(r, Rs)
Hjump = sp.simplify(jump / psiRs**sp.Rational(3, 2))
chk("H_+ - H_- = -2m/(R_s^2 psi^(3/2)) < 0: H_- > H_+, a positive-energy corner "
    "(Shi-Tam Thm 3.1 needs H_- = H_+, so it does not cover this device; Miao 2002 NAMED-NOT-READ)",
    float(Hjump.subs({m: M_DESIGN, a: A_CORE, Rs: R_SHELL})) < 0)
# R in L^1 outside: Lap(m/sqrt(r^2+a^2)) = -3 m a^2 (r^2+a^2)^(-5/2)
lapP = sp.simplify(sp.diff(r**2 * sp.diff(m / sp.sqrt(r**2 + a**2), r), r) / r**2)
chk("Lap Phi (smooth part) = -3 m a^2/(r^2+a^2)^(5/2): R = O(r^-5) in L^1",
    sp.simplify(lapP + 3 * m * a**2 / (r**2 + a**2)**sp.Rational(5, 2)) == 0)

# ---------------------------------------------------------------- R4
print("R4  exact R at the core, every m in the window")
u_in = (1 - 2 * Phi_in) ** sp.Rational(1, 4)
R_in = -8 * u_in**-5 * (sp.diff(u_in, r, 2) + 2 * sp.diff(u_in, r) / r)
R0 = sp.simplify(sp.limit(R_in, r, 0))
closed = -12 * m / a**3 / (1 - 2 * m / a + 2 * m / Rs) ** 2
chk("R(0) = -12 m / a^3 / (1 - 2m/a + 2m/R_s)^2 exactly", sp.simplify(R0 - closed) == 0)
for mv in M_WINDOW + (8e-3, 9.9e-3):
    v = float(R0.subs({m: mv, a: A_CORE, Rs: R_SHELL}))
    if RIEMANNIAN[mv]:
        chk("m=%.1e: R(0) = %+.5e < 0  ->  mu = R/2 < 0: time-symmetric DEC fails at the core" % (mv, v), v < 0)
    else:
        print("       m=%.1e: closed form gives %+.5e but psi(0) <= 0 -- not a scalar curvature of any "
              "Riemannian slice; NOT counted" % (mv, v))
R0_design = float(R0.subs({m: M_DESIGN, a: A_CORE, Rs: R_SHELL}))
chk("design point R(0) = %.4e reproduces the sibling audit's -2.9994e4" % R0_design,
    abs(R0_design + 2.9994e4) < 1.0)

# ---------------------------------------------------------------- R5
print("R5  E = -(1/2pi) Int d(Lap u): core part, shell atom, sum")
mp.mp.dps = 30
for mv in (M_DESIGN, 9.9e-3):
    sub = {m: mv, a: A_CORE, Rs: R_SHELL}
    uin = sp.lambdify(r, u_in.subs(sub), "mpmath")
    uout = sp.lambdify(r, u_out.subs(sub), "mpmath")
    duin = sp.lambdify(r, sp.diff(u_in, r).subs(sub), "mpmath")
    duout = sp.lambdify(r, sp.diff(u_out, r).subs(sub), "mpmath")
    # Int_{ball} Lap u = 4 pi r^2 u' |boundary  (divergence theorem, smooth parts)
    core = 4 * mp.pi * (R_SHELL**2 * duin(mp.mpf(R_SHELL)) - 0)
    outer = 4 * mp.pi * (mp.mpf(10)**12 * duout(mp.mpf(10)**6) - R_SHELL**2 * duout(mp.mpf(R_SHELL)))
    shell = 4 * mp.pi * R_SHELL**2 * (duout(mp.mpf(R_SHELL)) - duin(mp.mpf(R_SHELL)))
    E_core, E_out, E_shell = [-x / (2 * mp.pi) for x in (core, outer, shell)]
    tot = E_core + E_out + E_shell
    chk("m=%.1e: E_core = %+.6e (<0 contribution to Int Lap u means core Lap u > 0, R < 0), "
        "E_shell = %+.6e, E_outside = %+.3e, sum = %+.3e"
        % (mv, E_core, E_shell, E_out, tot),
        E_core < 0 and E_shell > 0 and abs(tot) < 1e-15)
    # direct quadrature cross-check of the core integral (smooth Lap u over r < R_s)
    lap_in = sp.lambdify(r, (sp.diff(r**2 * sp.diff(u_in, r), r) / r**2).subs(sub), "mpmath")
    q = mp.re(mp.quad(lambda t: 4 * mp.pi * t**2 * lap_in(t), [0, A_CORE / 4, A_CORE, 10 * A_CORE, 1, R_SHELL]))
    chk("m=%.1e: quadrature Int_{r<R_s} Lap u = %.10e matches boundary flux %.10e" % (mv, q, core),
        abs(q - core) < 1e-12 * max(1, abs(core)))

# ---------------------------------------------------------------- R6
print("R6  elementary rigidity for conformally flat data: finite step by z3")
N = 50
d = [z3.Real("d%d" % i) for i in range(N)]
s = z3.Solver()
s.add([di <= 0 for di in d])          # R >= 0  <=>  Lap u <= 0  (u > 0)
s.add(z3.Sum(d) == 0)                  # E = 0
s.add(z3.Or([di != 0 for di in d]))    # some cell with Lap u != 0
chk("z3: nonpositive Lap u cells with zero total (E = 0) force every cell zero (UNSAT)",
    s.check() == z3.unsat)
s2 = z3.Solver()
s2.add(z3.Sum(d) == 0)
s2.add(z3.Or([di != 0 for di in d]))
chk("z3 vacuity guard: without R >= 0, E = 0 with Lap u != 0 is SAT (the device's case)",
    s2.check() == z3.sat)
# u > 0 so sign(R) = -sign(Lap u): check with sympy on the formula
L, U = sp.symbols("L U", real=True)
chk("sign: R = -8 U^-5 L with U > 0 gives R >= 0 <=> L <= 0",
    all((-8 * Uv**-5 * Lv >= 0) == (Lv <= 0) for Uv in (0.5, 1.0, 1.3) for Lv in (-2, -1e-9, 0, 1e-9, 3)))

# ---------------------------------------------------------------- R7
print("R7  the tree's contrapositive, and which premises carry it")
AF, CPL, REG, DEC, E0, FLAT = z3.Bools("AF complete regular DEC E0 flat")
THM = z3.Implies(z3.And(AF, CPL, REG, DEC, E0), FLAT)     # rigidity, time-symmetric
dev = z3.And(AF, CPL, REG, E0, z3.Not(FLAT))              # device facts (R2, R3, R4)


def valid(f):
    t = z3.Solver()
    t.add(z3.Not(f))
    return t.check() == z3.unsat


chk("THM & device |= not DEC  (concentric.py:51-53, pair.py:124-129)",
    valid(z3.Implies(z3.And(THM, dev), z3.Not(DEC))))
for drop, name in ((AF, "asymptotic flatness"), (CPL, "completeness"), (REG, "regularity")):
    dev_d = z3.And([p for p in (AF, CPL, REG, E0) if not p.eq(drop)] + [z3.Not(FLAT)])
    chk("without the device satisfying %s, not-DEC is NOT entailed" % name,
        not valid(z3.Implies(z3.And(THM, dev_d), z3.Not(DEC))))
chk("the inequality alone (E >= 0) with E = 0 entails nothing about the DEC",
    not valid(z3.Implies(z3.And(z3.Implies(DEC, z3.BoolVal(True)), E0, z3.Not(FLAT)), z3.Not(DEC))))

# ---------------------------------------------------------------- R8
print("R8  completeness is load-bearing: u = 1 - c/r^3 on r > r0")
ub = 1 - c / r**3
Rb = sp.simplify(-8 * ub**-5 * (sp.diff(ub, r, 2) + 2 * sp.diff(ub, r) / r))
Eb = sp.limit(-2 * r**2 * sp.diff(ub, r), r, sp.oo)
chk("Lap u = -6c/r^5 < 0 so R = 48 c r^-5 u^-5 > 0 wherever u > 0 (got R = %s)" % Rb,
    sp.simplify(Rb - 48 * c / r**5 / ub**5) == 0)
chk("E = 0 exactly (got %s), not flat (R != 0), incomplete: inner boundary r0 > c^(1/3)" % Eb,
    Eb == 0)
chk("numerically at c = 1, r = 2: R = %.6f > 0" % float(Rb.subs({c: 1, r: 2})),
    float(Rb.subs({c: 1, r: 2})) > 0)

# ---------------------------------------------------------------- R9
print("R9  non-Minkowski witness")
chk("device K = 0 slice is curved: R(0) = %.4e != 0, so it is not a static slice of Minkowski"
    % R0_design, R0_design != 0)

# ---------------------------------------------------------------- R10
print("R10 robustness to the O(Phi^2) ambiguity of the weak-field slice (RECONSTRUCTED completions)")
F = sp.Function("f")
P0 = sp.symbols("P0", real=True)
# any conformally flat completion u = f(Phi): E = -2 f'(0) lim r^2 Phi' = 0; at r = 0 grad Phi = 0 so
# Lap u(0) = f'(Phi(0)) Lap Phi(0), Lap Phi(0) = -3 m / a^3 < 0: f' < 0 gives Lap u(0) > 0, R(0) < 0
lapPhi0 = sp.limit(sp.diff(r**2 * sp.diff(Phi_in, r), r) / r**2, r, 0)
chk("Lap Phi(0) = -3 m/a^3 (got %s)" % lapPhi0, sp.simplify(lapPhi0 + 3 * m / a**3) == 0)
chk("grad Phi(0) = 0", sp.limit(sp.diff(Phi_in, r), r, 0) == 0)
for name, fu in (("u = exp(-Phi/2)", sp.exp(-Phi_in / 2)), ("u = 1 - Phi/2", 1 - Phi_in / 2),
                 ("u = (1-2Phi)^(1/4) [the tree's]", (1 - 2 * Phi_in) ** sp.Rational(1, 4))):
    Rf0 = sp.limit(-8 * fu**-5 * (sp.diff(fu, r, 2) + 2 * sp.diff(fu, r) / r), r, 0)
    fo = fu.subs(Phi_in, Phi_out) if False else None
    vals = []
    for mv in M_WINDOW:
        sub = {m: mv, a: A_CORE, Rs: R_SHELL}
        u0 = complex(fu.subs(r, 0).subs(sub))
        ok_pos = abs(u0.imag) < 1e-15 and u0.real > 0
        vals.append((mv, ok_pos, complex(Rf0.subs(sub)) if ok_pos else None))
    txt = ", ".join("m=%.0e:%s" % (mv, ("R(0)=%+.3e" % v.real) if ok else "u(0)<=0") for mv, ok, v in vals)
    good = all((v.real < 0) for mv, ok, v in vals if ok)
    print("       %s: %s" % (name, txt))
    chk("%s: R(0) < 0 wherever u(0) > 0" % name, good)
chk("u = exp(-Phi/2) is positive at every m and gives R(0) < 0 across the whole window: the DEC-failure "
    "conclusion does not depend on the O(Phi^2) completion (this completion is RECONSTRUCTED, not the tree's)",
    all(float(sp.limit(-8 * sp.exp(-Phi_in / 2)**-5 * (sp.diff(sp.exp(-Phi_in / 2), r, 2)
        + 2 * sp.diff(sp.exp(-Phi_in / 2), r) / r), r, 0).subs({m: mv, a: A_CORE, Rs: R_SHELL})) < 0
        for mv in M_WINDOW))
Eexp = sp.limit(-2 * r**2 * sp.diff(sp.exp(-Phi_out / 2), r), r, sp.oo)
chk("u = exp(-Phi/2): E = 0 exactly (got %s)" % Eexp, sp.simplify(Eexp) == 0)

print("\nOVERALL %s" % ("OK" if OK else "FAIL"))
sys.exit(0 if OK else 1)
