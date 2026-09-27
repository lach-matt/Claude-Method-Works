#!/usr/bin/env python3
"""DOCKET 67 item 23 -- re-derivation of "Birkhoff's theorem for Einstein-Maxwell
in Misner-Sharp variables" as research/warp-drive/drivensource.py uses it.

Everything here is computed from the metric; nothing is imported from the tree, so
agreement with drivensource.py is an independent check, not a re-run of it.

Sections
  1  Misner-Sharp equations MS-r, MS-t derived as IDENTITIES of the Einstein tensor
     (the tree quotes them from nonstatic.py; here they are rebuilt from scratch).
  2  Source-free Maxwell in spherical symmetry FORCES Q constant (the tree assumes
     Q a Symbol and checks residuals; here Q(t,r) is left free and Maxwell fixes it).
  3  Electrovac T_ab: rho = Q^2/8piR^4, j = 0, p_r = -rho, p_T = +rho  (owner's claim).
  4  The owner's check: m = M - Q^2/2R, M const, satisfies MS-r, MS-t for arbitrary
     Phi, Lambda, R.
  5  UNIQUENESS (asserted in prose at drivensource.py:96, not machine-checked there):
     any m(t,r) satisfying MS-r, MS-t with the electrovac source has
     d(m + Q^2/2R) = 0 identically, so m + Q^2/2R is a constant.
  6  Magnetic charge: drivensource.py:302 says spherical symmetry admits ONLY F_tr.
     It also admits F_thph = P sin(theta); the conclusion survives with Q^2 -> Q^2+P^2.
  7  Witness A: Bertotti-Robinson (R = const = Q) -- the classical EXCEPTION to full
     Birkhoff (not locally RN); the frozen-mass statement still holds there.
  8  Witness B: Reissner-Nordstrom in a MOVING geodesic slicing (Phi = 0, R = R(r - t),
     infall energy E > 1): G = 8 pi T exactly, m = M - Q^2/2R with M constant, and the
     contraction variable is W = E > 1 -- the frozen mass is compatible with the tree's
     contraction inequality holding in a moving slicing, exactly as Milne does for vacuum
     in nonstatic.py.  This bears on the OWNER'S inference (lines 104-107), not on the
     theorem.
Exit status 1 on any failed check.
"""
import sys
import sympy as sp

t, r, th, ph = sp.symbols("t r theta phi")
x = [t, r, th, ph]
Q, P, M, E = sp.symbols("Q P M E", positive=True)
Rs = sp.Symbol("R_s", positive=True)          # stand-in for R(t,r) after substitution
FAIL = []


def chk(label, expr, want=0):
    got = sp.simplify(expr)
    ok = (got == want) if not isinstance(want, (list, tuple)) else all(sp.simplify(g - w) == 0 for g, w in zip(got, want))
    print("  %-70s %s" % (label, "ok" if ok else "FAIL  -> %s" % got))
    if not ok:
        FAIL.append(label)
    return ok


def einstein(Phi, Lam, R):
    """G_ab (lower) of ds^2 = -e^{2Phi}dt^2 + e^{2Lam}dr^2 + R^2 dOmega^2."""
    g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R**2, (R * sp.sin(th))**2)
    gi = g.inv()
    n = 4
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d])) for d in range(n)) / 2
             for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            Ric[b, c] = sp.simplify(sum(
                sp.diff(Gam[a][b][c], x[a]) - sp.diff(Gam[a][b][a], x[c])
                + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(n))
                for a in range(n)))
    Rsc = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    G = sp.simplify(Ric - Rsc * g / 2)
    return g, gi, G


def fluid_vars(G, Phi, Lam, R):
    """rho, j, p_r, p_T read off G = 8 pi T with u = e^{-Phi} d_t, n = e^{-Lam} d_r."""
    rho = G[0, 0] * sp.exp(-2 * Phi) / (8 * sp.pi)
    j = -G[0, 1] * sp.exp(-Phi - Lam) / (8 * sp.pi)
    p_r = G[1, 1] * sp.exp(-2 * Lam) / (8 * sp.pi)
    p_T = G[2, 2] / R**2 / (8 * sp.pi)
    return rho, j, p_r, p_T


def ms_vars(Phi, Lam, R):
    U = sp.exp(-Phi) * sp.diff(R, t)
    W = sp.exp(-Lam) * sp.diff(R, r)
    m = R / 2 * (1 - W**2 + U**2)
    Dt = lambda f: sp.exp(-Phi) * sp.diff(f, t)
    Dr = lambda f: sp.exp(-Lam) * sp.diff(f, r)
    return U, W, m, Dt, Dr


def maxwell_T(g, gi, Phi, Lam, R, Qf, Pf=0):
    """F_tr = Qf e^{Phi+Lam}/R^2 (Gauss), F_thph = Pf sin(theta); returns Maxwell residuals and T_ab."""
    F = sp.zeros(4, 4)
    F[0, 1] = Qf * sp.exp(Phi + Lam) / R**2
    F[1, 0] = -F[0, 1]
    F[2, 3] = Pf * sp.sin(th)
    F[3, 2] = -F[2, 3]
    Fup = gi * F * gi
    sg = sp.exp(Phi + Lam) * R**2 * sp.sin(th)          # sqrt(-g)
    maxwell = [sp.simplify(sum(sp.diff(sg * Fup[a, b], x[a]) for a in range(4))) for b in range(4)]
    # Bianchi dF = 0 for the magnetic part is automatic (F_thph = P sin th, P const).
    Fdd = sum(F[a, b] * Fup[a, b] for a in range(4) for b in range(4))
    Fmix = F * gi
    T = sp.Matrix(4, 4, lambda a, b: sp.simplify(
        (sum(F[a, c] * Fmix[b, c] for c in range(4)) - sp.Rational(1, 4) * g[a, b] * Fdd) / (4 * sp.pi)))
    return maxwell, T


# ------------------------------------------------------------------ 1. MS identities
print("1. MISNER-SHARP EQUATIONS AS IDENTITIES OF THE EINSTEIN TENSOR (rebuilt, not quoted)")
Phi = sp.Function("Phi")(t, r)
Lam = sp.Function("Lambda")(t, r)
R = sp.Function("R")(t, r)
g, gi, G = einstein(Phi, Lam, R)
rho, j, p_r, p_T = fluid_vars(G, Phi, Lam, R)
U, W, m, Dt, Dr = ms_vars(Phi, Lam, R)
chk("MS-r  D_r m - 4 pi R^2 (rho W + j U)  == 0 identically", Dr(m) - 4 * sp.pi * R**2 * (rho * W + j * U))
chk("MS-t  D_t m + 4 pi R^2 (p_r U + j W)  == 0 identically", Dt(m) + 4 * sp.pi * R**2 * (p_r * U + j * W))
print("     Hypotheses used: the diagonal spherically symmetric ansatz and G_ab = 8 pi T_ab. Nothing else.")

# ------------------------------------------------------------------ 2. Q constant
print("\n2. SOURCE-FREE MAXWELL FORCES Q CONSTANT (owner assumes Q a Symbol; here Q = Q(t,r))")
Qf = sp.Function("Q")(t, r)
mx, _ = maxwell_T(g, gi, Phi, Lam, R, Qf)
# residual b = t is proportional to d_r Q, residual b = r to d_t Q
chk("Maxwell (b=t) residual  = +sin(th) dQ/dr", mx[0] - sp.sin(th) * sp.diff(Qf, r))
chk("Maxwell (b=r) residual  = -sin(th) dQ/dt", mx[1] + sp.sin(th) * sp.diff(Qf, t))
chk("Maxwell (b=th, b=ph) residuals vanish", sp.Matrix([mx[2], mx[3]]), [0, 0])
print("     So nabla_a F^{ab} = 0 <=> d_r Q = d_t Q = 0: Q is a constant, DERIVED not assumed.")

# ------------------------------------------------------------------ 3. electrovac T
print("\n3. THE ELECTROVAC SOURCE IN THE FULL DYNAMICAL METRIC")
mx, T = maxwell_T(g, gi, Phi, Lam, R, Q)
chk("Maxwell residuals all vanish with Q constant", sp.Matrix(mx), [0, 0, 0, 0])
rhoM = sp.simplify(T[0, 0] * sp.exp(-2 * Phi))
jM = sp.simplify(-T[0, 1] * sp.exp(-Phi - Lam))
prM = sp.simplify(T[1, 1] * sp.exp(-2 * Lam))
pTM = sp.simplify(T[2, 2] / R**2)
chk("rho = Q^2/(8 pi R^4)", rhoM - Q**2 / (8 * sp.pi * R**4))
chk("j = 0", jM)
chk("p_r = -rho", prM + rhoM)
chk("p_T = +rho", pTM - rhoM)

# ------------------------------------------------------------------ 4. owner's check
print("\n4. THE OWNER'S CHECK: m = M - Q^2/2R with M constant satisfies MS-r, MS-t for ARBITRARY Phi, Lam, R")
mRN = M - Q**2 / (2 * R)
chk("MS-r residual with m = M - Q^2/2R", Dr(mRN) - 4 * sp.pi * R**2 * (rhoM * W + jM * U))
chk("MS-t residual with m = M - Q^2/2R", Dt(mRN) + 4 * sp.pi * R**2 * (prM * U + jM * W))

# ------------------------------------------------------------------ 5. uniqueness
print("\n5. UNIQUENESS (drivensource.py:96 'the solution is exact' -- asserted there, checked here)")
mf = sp.Function("m")(t, r)
resr = Dr(mf) - 4 * sp.pi * R**2 * (rhoM * W + jM * U)
rest = Dt(mf) + 4 * sp.pi * R**2 * (prM * U + jM * W)
Fc = mf + Q**2 / (2 * R)
chk("e^{Lam} * (MS-r residual)  ==  d_r (m + Q^2/2R)", sp.exp(Lam) * resr - sp.diff(Fc, r))
chk("e^{Phi} * (MS-t residual)  ==  d_t (m + Q^2/2R)", sp.exp(Phi) * rest - sp.diff(Fc, t))
print("     So MS-r = MS-t = 0  <=>  d(m + Q^2/2R) = 0  <=>  m = M - Q^2/2R with M constant on any")
print("     connected domain.  Uniqueness is one line and it holds for arbitrary Phi, Lam, R.")

# ------------------------------------------------------------------ 6. magnetic charge
print("\n6. MAGNETIC CHARGE: spherical symmetry admits F_thph = P sin(th) too (drivensource.py:302 says 'only F_tr')")
mxP, TP = maxwell_T(g, gi, Phi, Lam, R, Q, P)
chk("Maxwell residuals vanish with dyonic (Q, P)", sp.Matrix(mxP), [0, 0, 0, 0])
rhoP = sp.simplify(TP[0, 0] * sp.exp(-2 * Phi))
jP = sp.simplify(-TP[0, 1] * sp.exp(-Phi - Lam))
prP = sp.simplify(TP[1, 1] * sp.exp(-2 * Lam))
chk("rho = (Q^2+P^2)/(8 pi R^4)", rhoP - (Q**2 + P**2) / (8 * sp.pi * R**4))
chk("j = 0, p_r = -rho (dyonic)", sp.Matrix([jP, prP + rhoP]), [0, 0])
mD = M - (Q**2 + P**2) / (2 * R)
chk("MS-r residual with m = M - (Q^2+P^2)/2R", Dr(mD) - 4 * sp.pi * R**2 * (rhoP * W + jP * U))
chk("MS-t residual with m = M - (Q^2+P^2)/2R", Dt(mD) + 4 * sp.pi * R**2 * (prP * U + jP * W))
print("     The comment at line 302 is a discrepancy; the conclusion is unchanged (Q^2 -> Q^2 + P^2).")

# ------------------------------------------------------------------ 7. Bertotti-Robinson
print("\n7. WITNESS A -- BERTOTTI-ROBINSON, R = Q constant: the exception to FULL Birkhoff (not RN)")
PhiB, LamB, RB = sp.log(Q * sp.cosh(r)), sp.log(Q), Q
gB, giB, GB = einstein(PhiB, LamB, RB)
mxB, TB = maxwell_T(gB, giB, PhiB, LamB, RB, Q)
chk("Maxwell residuals vanish on BR", sp.Matrix(mxB), [0, 0, 0, 0])
chk("G_ab - 8 pi T_ab == 0 on BR (an exact electrovac solution)", GB - 8 * sp.pi * TB, sp.zeros(4, 4))
UB, WB, mB, _, _ = ms_vars(PhiB, LamB, RB)
chk("dR = 0 on BR (W = U = 0): outside Birkhoff's hypothesis", sp.Matrix([UB, WB]), [0, 0])
chk("m = R/2 = Q/2 = M - Q^2/(2Q) with M = Q: frozen-mass form still holds", mB - (Q - Q**2 / (2 * Q)))
print("     BR is not locally RN (no areal coordinate), so it is the classical exception to the theorem")
print("     as Bronnikov-Melnikov 4.3 state it; the tree's frozen-mass statement does not need dR != 0.")

# ------------------------------------------------------------------ 8. moving RN slicing
print("\n8. WITNESS B -- RN IN A MOVING GEODESIC SLICING, infall energy E (Phi = 0, R = R(r - t))")
Rf = sp.Function("R")(t, r)
f_of = lambda RR: 1 - 2 * M / RR + Q**2 / RR**2
s_of = lambda RR: sp.sqrt(E**2 - f_of(RR))         # radial velocity |dR/dtau| at areal radius RR
PhiL, LamL = sp.Integer(0), sp.log(s_of(Rf) / E)
gL, giL, GL = einstein(PhiL, LamL, Rf)
mxL, TL = maxwell_T(gL, giL, PhiL, LamL, Rf, Q)
UL, WL, mL, _, _ = ms_vars(PhiL, LamL, Rf)
s = s_of(Rs)
sprime = sp.diff(s, Rs)
# impose dR/dr = s(R), dR/dt = -s(R), and the chain-rule second derivatives
sec = {sp.Derivative(Rf, (t, 2)): sprime * s, sp.Derivative(Rf, (r, 2)): sprime * s,
       sp.Derivative(Rf, t, r): -sprime * s, sp.Derivative(Rf, r, t): -sprime * s}
first = {sp.Derivative(Rf, t): -s, sp.Derivative(Rf, r): s}


def impose(expr):
    e = expr.xreplace(sec).xreplace(first).xreplace({Rf: Rs})
    return sp.simplify(e)


chk("Maxwell residuals vanish in the moving slicing", sp.Matrix([impose(v) for v in mxL]), [0, 0, 0, 0])
chk("G_ab - 8 pi T_ab == 0 in the moving slicing (RN, exactly)", (GL - 8 * sp.pi * TL).applyfunc(impose), sp.zeros(4, 4))
chk("m = M - Q^2/2R in the moving slicing (M constant, frozen)", impose(mL) - (M - Q**2 / (2 * Rs)))
chk("contraction variable W = E (> 1 for E > 1): nonstatic.py's inequality HOLDS here", impose(WL) - E)
chk("areal velocity U = -s(R) != 0: the areal radius is moving", impose(UL) + s)
print("     The frozen mass does not by itself forbid 2m/R < e^{-2Phi} Rdot^2; a slicing of RN satisfies it")
print("     with rho > 0, exactly as Milne does for vacuum.  What closes the driven branch is the owner's")
print("     own inference that a driven contraction would need m(R) to evolve (drivensource.py:104-107),")
print("     plus nonstatic.py's 'a moving areal radius is not a destination'.  That is outside the theorem.")

print("\nRESULT:", "ALL CHECKS PASS" if not FAIL else "FAILED: %s" % FAIL)
sys.exit(1 if FAIL else 0)
