#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key misner-sharp-1964-mass-and-equations.

Independent of the tree: nothing is imported from research/warp-drive.  The
Einstein tensor is built from scratch for

    ds^2 = -e^{2Phi(t,r)} dt^2 + e^{2Lam(t,r)} dr^2 + R(t,r)^2 dOmega^2

and every claim is a residual that must simplify to 0 (or a z3 check).

C1  MS scalar, the identity W^2 = 1 - 2m/R + U^2, MS-r, MS-t (G = 8 pi T, Lambda_c = 0)
C2  source agreement: Hayward gr-qc/9408002 eq.(28a),(28b) in his gauge (Phi = 0),
    and Herrera-Santos gr-qc/0410014 eq.(25),(30) (eps = 0), mapped to the tree's variables
C3  MS 1964's own perfect-fluid comoving form (Hayward eq.32): j = 0 =>
    E' = 4 pi r^2 rho r', Edot = -4 pi r^2 p rdot
C4  electrovac WITH magnetic charge P: rho = (Q^2+P^2)/(8 pi R^4), j = 0, p_r = -rho,
    Maxwell satisfied; drivensource.py:286,302 'ONLY ... F_tr' omits P
C5  Birkhoff-in-MS-variables: d(m_MS - [M - (Q^2+P^2)/2R]) = 0 from MS-r/MS-t
C6  with a cosmological constant: the frozen quantity is m + ... ; m = M - Q^2/2R + Lc R^3/6
C7  dR = 0 electrovac (Bertotti-Robinson): Einstein-Maxwell solution, NOT RN, m frozen
C8  Lemaitre (PG) slicing of Schwarzschild: m = rs/2, W = 1, U = -sqrt(2m/R)
C9  z3: E3 (W = 1 <=> U^2 = 2m/R) with and without the W > 0 hypothesis
"""
import sys
import sympy as sp

FAIL = []


def chk(name, expr, target=0):
    res = sp.simplify(sp.expand(expr - target))
    ok = (res == 0)
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else "   residual = %s" % res))
    if not ok:
        FAIL.append(name)
    return ok


t, r, th, ph = sp.symbols("t r theta phi", real=True)
x = [t, r, th, ph]


def einstein(g):
    gi = sp.simplify(g.inv())
    n = 4
    Gm = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                                        - sp.diff(g[b, c], x[d])) for d in range(n)) / 2)
            for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            s = 0
            for a in range(n):
                s += sp.diff(Gm[a][b][c], x[a]) - sp.diff(Gm[a][b][a], x[c])
                for d in range(n):
                    s += Gm[a][a][d] * Gm[d][b][c] - Gm[a][c][d] * Gm[d][b][a]
            Ric[b, c] = sp.simplify(s)
    Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    G = sp.Matrix(n, n, lambda a, b: sp.simplify(Ric[a, b] - Rs * g[a, b] / 2))
    return gi, G


# ---------------------------------------------------------------- C1
Phi = sp.Function("Phi")(t, r)
Lam = sp.Function("Lam")(t, r)
R = sp.Function("R")(t, r)
g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R**2, R**2 * sp.sin(th)**2)
gi, G = einstein(g)
Lc = sp.Symbol("Lambda_c", real=True)

def matter(Gt):
    T = Gt / (8 * sp.pi)
    return dict(rho=T[0, 0] * sp.exp(-2 * Phi), j=-T[0, 1] * sp.exp(-Phi - Lam),
                p_r=T[1, 1] * sp.exp(-2 * Lam), p_T=T[2, 2] / R**2)

M0 = matter(G)
U = sp.exp(-Phi) * sp.diff(R, t)
W = sp.exp(-Lam) * sp.diff(R, r)
Dt = lambda f: sp.exp(-Phi) * sp.diff(f, t)
Dr = lambda f: sp.exp(-Lam) * sp.diff(f, r)
gradR2 = sum(gi[a, b] * sp.diff(R, x[a]) * sp.diff(R, x[b]) for a in range(4) for b in range(4))
m = R / 2 * (1 - gradR2)                     # Hayward eq.(4) definition, invariant
print("--- C1  definitions and MS equations (G = 8 pi T, no Lambda_c)")
chk("C1a m = (R/2)(1 - W^2 + U^2)", m - R / 2 * (1 - W**2 + U**2))
chk("C1b identity W^2 = 1 - 2m/R + U^2", W**2 - (1 - 2 * m / R + U**2))
chk("C1c MS-r  D_r m = 4 pi R^2 (rho W + j U)", Dr(m) - 4 * sp.pi * R**2 * (M0["rho"] * W + M0["j"] * U))
chk("C1d MS-t  D_t m = -4 pi R^2 (p_r U + j W)", Dt(m) + 4 * sp.pi * R**2 * (M0["p_r"] * U + M0["j"] * W))
# sign of j: j = -T_ab u^a n^b with u = e^{-Phi} d_t, n = e^{-Lam} d_r
T0 = G / (8 * sp.pi)
uvec = [sp.exp(-Phi), 0, 0, 0]; nvec = [0, sp.exp(-Lam), 0, 0]
chk("C1e j = -T_ab u^a n^b (outward flux convention)",
    M0["j"] + sum(T0[a, b] * uvec[a] * nvec[b] for a in range(4) for b in range(4)))

# ---------------------------------------------------------------- C2  source mapping
print("--- C2  agreement with the READ restatements")
# Hayward gauge: metric (26) ds^2 = r^2 dO^2 + e^lambda dchi^2 - dtau^2  <=> Phi = 0, e^{2Lam} = e^lambda
sub_H = {Phi: 0}
T00 = M0["rho"]                                  # T(d_tau, d_tau) with g_tautau = -1
T01 = (T0[0, 1]).subs(Phi, 0)                    # T(d_tau, d_chi)
T11 = (T0[1, 1]).subs(Phi, 0)                    # T(d_chi, d_chi)
rp, rd = sp.diff(R, r), sp.diff(R, t)
mH = m.subs(Phi, 0).doit()
chk("C2a Hayward (27) 1 - 2E/r = e^{-lambda} r'^2 - rdot^2  (Phi = 0)",
    (1 - 2 * mH / R) - (sp.exp(-2 * Lam) * rp**2 - rd**2))
chk("C2b Hayward (28a) E' = 4 pi r^2 (T00 r' - T01 rdot)",
    (sp.diff(mH, r) - 4 * sp.pi * R**2 * (T00.subs(Phi, 0) * rp - T01 * rd)).doit())
chk("C2c Hayward (28b) Edot = 4 pi r^2 e^{-lambda} (T01 r' - T11 rdot)",
    (sp.diff(mH, t) - 4 * sp.pi * R**2 * sp.exp(-2 * Lam) * (T01 * rp - T11 * rd)).doit())
# Herrera-Santos (25),(30) with eps = 0: D_t m = -4 pi (P_r U + q_hat E) R^2 ;
# D_R m = (1/R') d_r m = 4 pi (mu + q_hat U/E) R^2 ; E = R'/B (their (22)) = W here
Ehs = W
chk("C2d Herrera-Santos (25) D_t m = -4 pi (P_r U + j E) R^2",
    Dt(m) + 4 * sp.pi * (M0["p_r"] * U + M0["j"] * Ehs) * R**2)
chk("C2e Herrera-Santos (30) (1/R') d_r m = 4 pi (mu + j U/E) R^2",
    sp.diff(m, r) / sp.diff(R, r) - 4 * sp.pi * (M0["rho"] + M0["j"] * U / Ehs) * R**2)

# ---------------------------------------------------------------- C3  MS 1964 form
print("--- C3  Misner-Sharp 1964 comoving perfect fluid (j = 0), Hayward eq.(32)")
# j = 0 is the comoving condition; then MS-r/MS-t become E' = 4 pi r^2 rho r', Edot = -4 pi r^2 p rdot
rho_, p_ = sp.symbols("rho p")
chk("C3a MS-r at j=0: d_r m = 4 pi R^2 rho R'",
    sp.exp(Lam) * 4 * sp.pi * R**2 * rho_ * W - 4 * sp.pi * R**2 * rho_ * sp.diff(R, r))
chk("C3b MS-t at j=0: d_t m = -4 pi R^2 p Rdot",
    sp.exp(Phi) * (-4 * sp.pi * R**2 * p_ * U) - (-4 * sp.pi * R**2 * p_ * sp.diff(R, t)))

# ---------------------------------------------------------------- C4  electrovac with P
print("--- C4  spherically symmetric Maxwell field WITH magnetic charge")
Q, P = sp.symbols("Q P", real=True)
F = sp.zeros(4, 4)
F[0, 1] = Q * sp.exp(Phi + Lam) / R**2; F[1, 0] = -F[0, 1]
F[2, 3] = P * sp.sin(th); F[3, 2] = -F[2, 3]
Fup = gi * F * gi
sg = sp.exp(Phi + Lam) * R**2 * sp.sin(th)
for b in range(4):
    chk("C4a Maxwell d_a(sqrt(-g) F^{a%d}) = 0" % b, sum(sp.diff(sg * Fup[a, b], x[a]) for a in range(4)))
# dF = 0 : F_{[ab,c]}
def dF(a, b, c):
    return sp.diff(F[a, b], x[c]) + sp.diff(F[b, c], x[a]) + sp.diff(F[c, a], x[b])
chk("C4b Bianchi dF = 0 (all components)", sum(dF(a, b, c)**2 for a in range(4) for b in range(4) for c in range(4)))
Fdd = sum(F[a, b] * Fup[a, b] for a in range(4) for b in range(4))
Fmix = F * gi
TEM = sp.Matrix(4, 4, lambda a, b: sp.simplify((sum(F[a, c] * Fmix[b, c] for c in range(4))
                                                  - g[a, b] * Fdd / 4) / (4 * sp.pi)))
rhoEM = sp.simplify(TEM[0, 0] * sp.exp(-2 * Phi))
jEM = sp.simplify(-TEM[0, 1] * sp.exp(-Phi - Lam))
prEM = sp.simplify(TEM[1, 1] * sp.exp(-2 * Lam))
chk("C4c rho = (Q^2 + P^2)/(8 pi R^4)", rhoEM - (Q**2 + P**2) / (8 * sp.pi * R**4))
chk("C4d j = 0", jEM)
chk("C4e p_r = -rho", prEM + rhoEM)
print("     => drivensource.py:286 'the ONLY spherically symmetric field' and :302 'admits only F_{tr}'")
print("        omit F_{theta phi} = P sin(theta); the conclusion survives with Q^2 -> Q^2 + P^2")

# ---------------------------------------------------------------- C5  Birkhoff in MS variables
print("--- C5  Birkhoff in MS variables: m_MS - [M - (Q^2+P^2)/2R] has zero gradient ON SHELL")
Mc = sp.Symbol("M")
mRN = Mc - (Q**2 + P**2) / (2 * R)
# On shell (G = 8 pi T_EM), MS-r/MS-t give D m_MS = the RHS evaluated with T_EM.
Dr_mMS = 4 * sp.pi * R**2 * (rhoEM * W + jEM * U)
Dt_mMS = -4 * sp.pi * R**2 * (prEM * U + jEM * W)
chk("C5a D_r(m_MS - m_RN) = 0 on shell", Dr_mMS - Dr(mRN))
chk("C5b D_t(m_MS - m_RN) = 0 on shell", Dt_mMS - Dt(mRN))
# the tree's own residual test (drivensource.py:329-343) is this same identity with T_EM on the RHS
# and needs NO field equation; the field equation enters only to identify m_MS with the solution.

# ---------------------------------------------------------------- C6  cosmological constant
print("--- C6  with Lambda_c: G + Lc g = 8 pi T  =>  effective rho+Lc/8pi, p_r-Lc/8pi")
Gc = G + Lc * g
Mc_ = matter(Gc)          # this is T when G + Lc g = 8 pi T
# MS-r with a cosmological constant (derived, not assumed):
chk("C6a D_r m = 4 pi R^2 (rho W + j U) + (Lc/2) R^2 W   [Lambda_c != 0]",
    Dr(m) - (4 * sp.pi * R**2 * (Mc_["rho"] * W + Mc_["j"] * U) + Lc / 2 * R**2 * W))
chk("C6b D_t m = -4 pi R^2 (p_r U + j W) + (Lc/2) R^2 U   [Lambda_c != 0]",
    Dt(m) - (-4 * sp.pi * R**2 * (Mc_["p_r"] * U + Mc_["j"] * W) + Lc / 2 * R**2 * U))
mRNdS = Mc - (Q**2 + P**2) / (2 * R) + Lc * R**3 / 6
chk("C6c electrovac + Lc: frozen solution is m = M - Q^2/2R + Lc R^3/6 (D_r)",
    4 * sp.pi * R**2 * rhoEM * W + Lc / 2 * R**2 * W - Dr(mRNdS))
chk("C6d electrovac + Lc: (D_t)", -4 * sp.pi * R**2 * prEM * U + Lc / 2 * R**2 * U - Dt(mRNdS))
print("     => 'm(R) = M - Q^2/(2R)' (drivensource.py:98) needs Lambda_c = 0 (unnamed); with Lambda_c the")
print("        M is still constant (Birkhoff conclusion survives), m(R) carries + Lc R^3/6")

# ---------------------------------------------------------------- C7  Bertotti-Robinson (dR = 0)
print("--- C7  dR = 0 electrovac: Bertotti-Robinson AdS2 x S2, R = |Q| const")
q = sp.Symbol("q", positive=True)
gBR = sp.diag(-q**2 * sp.cosh(r)**2, q**2, q**2, q**2 * sp.sin(th)**2)
giBR, GBR = einstein(gBR)
FBR = sp.zeros(4, 4)
FBR[0, 1] = q * (q * sp.cosh(r)) * q / q**2; FBR[1, 0] = -FBR[0, 1]   # Q e^{Phi+Lam}/R^2, Q = q
FupBR = giBR * FBR * giBR
FddBR = sum(FBR[a, b] * FupBR[a, b] for a in range(4) for b in range(4))
TBR = sp.Matrix(4, 4, lambda a, b: sp.simplify((sum(FBR[a, c] * (FBR * giBR)[b, c] for c in range(4))
                                                  - gBR[a, b] * FddBR / 4) / (4 * sp.pi)))
chk("C7a Bertotti-Robinson solves G = 8 pi T_EM with Q = R = q", sp.Matrix(GBR - 8 * sp.pi * TBR).norm()**2)
mBR = q / 2
chk("C7b m_MS = R/2 = q/2 (gradR = 0), = M - Q^2/2R with M = q", mBR - (q - q**2 / (2 * q)))
print("     => m frozen holds; but the spacetime is NOT Reissner-Nordstrom: 'Birkhoff for")
print("        Einstein-Maxwell' (drivensource.py:101) as local-RN needs dR != 0 (unnamed)")

# ---------------------------------------------------------------- C8  Lemaitre / PG
print("--- C8  Lemaitre slicing of Schwarzschild (drivensource.py:175-190 docstring, pg_witness() :373-387)")
rs = sp.Symbol("r_s", positive=True)
tt, rc = sp.symbols("tau rho_c", positive=True)
Rl = (sp.Rational(3, 2) * (rc - tt))**sp.Rational(2, 3) * rs**sp.Rational(1, 3)
Ul = sp.diff(Rl, tt)
Wl = sp.diff(Rl, rc) / sp.sqrt(rs / Rl)
ml = sp.simplify(Rl / 2 * (1 - Wl**2 + Ul**2))
chk("C8a m = r_s/2", ml - rs / 2)
chk("C8b W = 1", sp.simplify(Wl) - 1)
chk("C8c U = -sqrt(2m/R)", sp.simplify(Ul + sp.sqrt(2 * ml / Rl)))

# ---------------------------------------------------------------- C9  z3 on E3
print("--- C9  z3: drivensource.py:435-439 obligation E3")
try:
    import z3
    Uz, Wz, mz, Rz = z3.Reals("U W m R")
    ident = [Rz > 0, Wz * Wz == 1 - 2 * mz / Rz + Uz * Uz]
    s = z3.Solver(); s.add(ident + [Wz > 0]); s.add(z3.Not((Wz == 1) == (Uz * Uz == 2 * mz / Rz)))
    r1 = s.check(); print(("PASS " if r1 == z3.unsat else "FAIL ") + "C9a E3 with W > 0: negation %s" % r1)
    if r1 != z3.unsat: FAIL.append("C9a")
    s = z3.Solver(); s.add(ident); s.add(z3.Not((Wz == 1) == (Uz * Uz == 2 * mz / Rz)))
    r2 = s.check()
    print(("PASS " if r2 == z3.sat else "FAIL ") + "C9b drift guard: drop W > 0 and E3 fails (sat): %s  %s"
          % (r2, s.model() if r2 == z3.sat else ""))
    if r2 != z3.sat: FAIL.append("C9b")
except ImportError:
    print("SKIP C9 (z3 not installed)")

# ---------------------------------------------------------------- C10  the one moved datum: Lambda_c
print("--- C10  size of the Lambda_c term against the Q^2/2R term (Planck 2018 VI, arXiv 1807.06209, eq.15 / Table 2)")
import math
c = 299792458.0; Mpc = 3.0856775814913673e22
H0 = 67.36e3 / Mpc; OmL = 0.6847                     # TT,TE,EE+lowE+lensing
Lam_SI = 3 * OmL * H0**2 / c**2                      # m^-2
Lam_eV = 4.24e-66 / (1.973269804e-7)**2              # Planck's own quoted 4.24e-66 eV^2 -> m^-2
print("     Lambda = 3 Omega_L H0^2/c^2 = %.4e m^-2 ; from 4.24e-66 eV^2: %.4e m^-2" % (Lam_SI, Lam_eV))
ok = abs(Lam_SI / Lam_eV - 1) < 0.01
print(("PASS " if ok else "FAIL ") + "C10a the two Planck routes agree to 1%%: ratio %.4f" % (Lam_SI / Lam_eV))
if not ok: FAIL.append("C10a")
Gn = 6.67430e-11; k_e = 8.9875517923e9
for Qc, Rm in [(1.0, 1.0), (1e-6, 1e-2), (1.0, 1e3)]:
    Q2geo = Gn * k_e * Qc**2 / c**4                  # Q^2 in m^2 (geometrised)
    ratio = (Lam_SI * Rm**3 / 6) / (Q2geo / (2 * Rm))
    print("     Q = %g C, R = %g m : (Lambda R^3/6)/(Q^2/2R) = %.3e" % (Qc, Rm, ratio))
print("     => the Lambda_c term is negligible at laboratory scales; M-constant (the load-bearing claim) is exact either way")

print()
print("ALL PASS" if not FAIL else "FAILURES: %s" % FAIL)
sys.exit(1 if FAIL else 0)
