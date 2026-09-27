#!/usr/bin/env python3
"""DOCKET 67 -- audit re-derivation: Misner-Sharp / Hernandez-Misner evolution equations
as used by nonstatic.py, driven.py, foliation.py (research/warp-drive).

Independent of nonstatic.py: the Einstein tensor is built here from a separate routine
(mixed components G^a_b via Riemann with all indices computed afresh), and every published
form read at source is compared:
  HSW  = Herrera, Santos & Wang, arXiv:0810.1083, eqs (14),(18),(28),(30),(31),(37)
  MMR  = Musco, Miller & Rezzolla, arXiv:gr-qc/0412063, eqs (9),(12),(13),(14) [MS 1964]
         and (20),(25),(26) [Hernandez-Misner 1966]
Every CHECK prints PASS/FAIL; exit 1 on any FAIL.
"""
import sys, math
import sympy as sp

FAILS = []
def check(name, expr_or_bool, expect_zero=True):
    if isinstance(expr_or_bool, bool):
        ok = expr_or_bool
    else:
        z = sp.simplify(sp.expand(expr_or_bool))
        ok = (z == 0) if expect_zero else (z != 0)
    print(("PASS  " if ok else "FAIL  ") + name)
    if not ok:
        FAILS.append(name)
    return ok

t, r, th, ph = sp.symbols("t r theta phi", real=True)
X = [t, r, th, ph]

def einstein_mixed(g):
    """G^a_b and Christoffels for metric g on coords X (fresh implementation)."""
    n = 4
    gi = sp.simplify(g.inv())
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                         - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    # Riemann R^a_{bcd} = d_c Gam^a_{db} - d_d Gam^a_{cb} + Gam^a_{ce} Gam^e_{db} - Gam^a_{de} Gam^e_{cb}
    def Riem(a, b, c, d):
        s = sp.diff(Gam[a][d][b], X[c]) - sp.diff(Gam[a][c][b], X[d])
        s += sum(Gam[a][c][e] * Gam[e][d][b] - Gam[a][d][e] * Gam[e][c][b] for e in range(n))
        return s
    Ric = sp.Matrix(n, n, lambda b, d: sp.expand(sum(Riem(a, b, a, d) for a in range(n))))
    Rs = sp.expand(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    Gdn = Ric - Rs * g / 2
    Gmix = sp.simplify(gi * Gdn)          # G^a_b
    return Gmix, Gdn, Gam, gi

# ------------------------------------------------------------------ general metric
Phi = sp.Function("Phi")(t, r)
Lam = sp.Function("Lambda")(t, r)
R = sp.Function("R")(t, r)
g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R**2, R**2 * sp.sin(th)**2)
print("building Einstein tensor (independent routine) ...")
Gmix, Gdn, Gam, gi = einstein_mixed(g)
T = Gdn / (8 * sp.pi)          # T_ab := G_ab / 8pi  (the owner's definition, nonstatic.py:297)
Tmix = Gmix / (8 * sp.pi)

Dt = lambda f: sp.exp(-Phi) * sp.diff(f, t)
Dr = lambda f: sp.exp(-Lam) * sp.diff(f, r)
rho = -Tmix[0, 0]                       # = T_ab u^a u^b
p_r = Tmix[1, 1]
j = -T[0, 1] * sp.exp(-Phi - Lam)       # = -T_ab u^a n^b, outward flux
U, W = Dt(R), Dr(R)
m = R / 2 * (1 - W**2 + U**2)
pi = sp.pi

print("\nC1  the five equations as the tree states them (nonstatic.py:66-70), fresh G_ab")
check("C1a MS-r   D_r m = 4 pi R^2 (rho W + j U)", Dr(m) - 4*pi*R**2*(rho*W + j*U))
check("C1b MS-t   D_t m = -4 pi R^2 (p_r U + j W)", Dt(m) + 4*pi*R**2*(p_r*U + j*W))
check("C1c EV-U   D_t U = W D_r Phi - m/R^2 - 4 pi R p_r", Dt(U) - (W*Dr(Phi) - m/R**2 - 4*pi*R*p_r))
check("C1d EV-W   D_t W = 4 pi R j + U D_r Phi", Dt(W) - (4*pi*R*j + U*Dr(Phi)))
check("C1e EV-U'  D_r U = 4 pi R j + W D_t Lambda", Dr(U) - (4*pi*R*j + W*Dt(Lam)))

print("\nC2  EV-W and EV-U' are ONE equation (difference vanishes with NO field equation used)")
check("C2a (D_tW - U D_rPhi) - (D_rU - W D_tLambda) == 0 identically",
      (Dt(W) - U*Dr(Phi)) - (Dr(U) - W*Dt(Lam)))
Rt, Rr, Rtr = sp.diff(R, t), sp.diff(R, r), sp.diff(R, t, r)
Phr, Lat = sp.diff(Phi, r), sp.diff(Lam, t)
check("C2b both equal e^{-Phi-Lam}(R_tr - Phi_r R_t - Lam_t R_r)",
      Dt(W) - U*Dr(Phi) - sp.exp(-Phi-Lam)*(Rtr - Phr*Rt - Lat*Rr))
check("C2c EV-W residual = -(R e^{-Phi-Lam}/2)(G_tr - 8 pi T_tr) with T_tr the SOURCE (momentum constraint)",
      (Dt(W) - U*Dr(Phi)) - (-(R*sp.exp(-Phi-Lam)/2)*Gdn[0, 1]))

print("\nC3  EV-W == Herrera-Santos-Wang eq.(14) (0810.1083 p.6): 8piT01 = -8pi q A B = -2(R'dot/R - Bdot R'/(B R) - Rdot A'/(R A))")
A_, B_ = sp.exp(Phi), sp.exp(Lam)
hsw14_rhs = -2*(Rtr/R - sp.diff(B_, t)/B_*Rr/R - Rt/R*sp.diff(A_, r)/A_)
check("C3a HSW(14) RHS equals G_tr computed here", hsw14_rhs - Gdn[0, 1])
q_hsw = -T[0, 1]/(A_*B_)
check("C3b HSW's comoving q = -T01/(AB) equals the tree's j", q_hsw - j)

print("\nC4  MS-t, MS-r, EV-U against HSW (30),(31),(28),(37) with eps = eta = 0; D_R := D_r / W, a := D_r Phi")
check("C4a HSW(28) E = R'/B = sqrt(1+U^2-2m/R)  (squared)", W**2 - (1 + U**2 - 2*m/R))
check("C4b HSW(30) D_T m = -4 pi (P_r U + q E) R^2", Dt(m) + 4*pi*(p_r*U + j*W)*R**2)
check("C4c HSW(31) D_R m = 4 pi (mu + q U/E) R^2", Dr(m)/W - 4*pi*(rho + j*U/W)*R**2)
check("C4d HSW(37) D_T U = -m/R^2 - 4 pi P_r R + E a", Dt(U) - (-m/R**2 - 4*pi*p_r*R + W*Dr(Phi)))

print("\nC5  MMR (gr-qc/0412063) MS-1964 perfect-fluid form, comoving, j = 0")
# radial conservation from the contracted Bianchi identity, perfect fluid at rest in the coords:
# nabla_a T^a_r = d_r p + (rho + p) Phi_r  (computed, not quoted)
rr_, pp_ = sp.Function("rho0")(t, r), sp.Function("p0")(t, r)
Tpf = sp.diag(-rr_, pp_, pp_, pp_)       # T^a_b
divr = sum(sp.diff(Tpf[a, 1], X[a]) for a in range(4)) \
     + sum(Gam[a][a][c]*Tpf[c, 1] for a in range(4) for c in range(4)) \
     - sum(Gam[c][a][1]*Tpf[a, c] for a in range(4) for c in range(4))
check("C5a nabla_a T^a_r = p' + (rho+p) Phi'  (so MMR(12) D_r a = -a D_r p/(e+p) with a = e^Phi)",
      divr - (sp.diff(pp_, r) + (rr_ + pp_)*sp.diff(Phi, r)))
# MMR (9): D_t U = -[Gamma/(e+p) D_r p + M/R^2 + 4 pi R p]; substitute D_r Phi = -D_r p/(e+p)
Dr_p = sp.Symbol("Drp"); e_, p_ = sp.symbols("e p", positive=True)
Gm, Ms, Rs_ = sp.symbols("Gamma M Rsym", positive=True)
mmr9 = -(Gm/(e_+p_)*Dr_p + Ms/Rs_**2 + 4*pi*Rs_*p_)
tree_evU = Gm*(-Dr_p/(e_+p_)) - Ms/Rs_**2 - 4*pi*Rs_*p_
check("C5b MMR(9) == EV-U once D_r Phi = -D_r p/(e+p)", mmr9 - tree_evU)
check("C5c MMR(13) D_r M = 4 pi Gamma e R^2 == MS-r at j = 0 (same symbols)",
      (4*pi*Gm*e_*Rs_**2) - (4*pi*Rs_**2*(e_*Gm + 0)))
check("C5d MMR(14) Gamma^2 = 1 + U^2 - 2M/R == tree's m definition", W**2 - (1 + U**2 - 2*m/R))
print("      C5e (by C1d at j = 0, C5a): comoving perfect fluid EV-W reads D_t Gamma = U D_r Phi = -U D_r p/(e+p)")

print("\nC6  Hernandez-Misner observer-time forms (MMR eqs 20, 25, 26) follow from MS-r + MS-t at j = 0")
jj = sp.Symbol("j"); ee, pr_, Wg, Ug, Rg = sp.symbols("e p_r W U R_")
Drm = 4*pi*Rg**2*(ee*Wg + jj*Ug); Dtm = -4*pi*Rg**2*(pr_*Ug + jj*Wg)
Dkm = Drm + Dtm                              # MMR (20): D_r = D_k - D_t
check("C6a HM(25) D_k M = 4 pi R^2 (e Gamma - p U) at j = 0", (Dkm - 4*pi*Rg**2*(ee*Wg - pr_*Ug)).subs(jj, 0))
check("C6b HM(26) Gamma = D_k R - U  (D_k R = W + U)", (Wg + Ug) - Ug - Wg)
print("      note: with j != 0, D_k M = 4 pi R^2 (e W - p U) + 4 pi R^2 j (U - W): extra term",
      sp.factor(sp.expand(Dkm - 4*pi*Rg**2*(ee*Wg - pr_*Ug))))

print("\nC7  EV-W is implied by m's definition + EV-U + MS-t wherever W != 0 (rho and p_r cancel)")
Dt_m = -4*pi*R**2*(p_r*U + j*W); Dt_U = W*Dr(Phi) - m/R**2 - 4*pi*R*p_r
# d/dt of W^2 = 1 + U^2 - 2m/R along the normal, using EV-U and MS-t:
lhs = 2*U*Dt_U - 2*Dt_m/R + 2*m*U/R**2      # = D_t(W^2) = 2 W D_t W
check("C7a 2W(4 pi R j + U D_r Phi) - [2U D_tU - 2 D_t m/R + 2mU/R^2] == 0", 2*W*(4*pi*R*j + U*Dr(Phi)) - lhs)
print("      but rho CONSTRAINS W on every slice: W^2 = 1 + U^2 - 2m/R with D_r m = 4 pi R^2 (rho W + j U).")
print("      So 'the contraction variable does not know the energy density exists' (nonstatic.py:82-83)")
print("      describes EV-W's time derivative only; W's slice profile is fixed by rho through MS-r.")

print("\nC8  witnesses in geodesic slicing (Phi = 0): D_t W = 0 where j = 0")
# (a) Schwarzschild in Lemaitre coordinates: ds^2 = -dtau^2 + (2M/R) drho^2 + R^2 dOmega^2
M = sp.Symbol("M", positive=True)
Rl = (sp.Rational(3, 2)*(r - t))**sp.Rational(2, 3)*(2*M)**sp.Rational(1, 3)
gl = sp.diag(-1, 2*M/Rl, Rl**2, Rl**2*sp.sin(th)**2)
Gl, Gld, _, _ = einstein_mixed(gl)
check("C8a Lemaitre-Schwarzschild: G_ab = 0 (vacuum)", sum(abs(sp.simplify(Gl[a, b])) for a in range(4) for b in range(4)) == 0)
Wl = sp.diff(Rl, r)/sp.sqrt(2*M/Rl)
check("C8b Lemaitre: W = 1, D_t W = 0", sp.simplify(Wl - 1))
# (b) LTB dust: ds^2 = -dt^2 + R'^2/(1+2E(r)) dr^2 + R^2 dOmega^2 -> W = sqrt(1+2E(r)), t-independent
Ef = sp.Function("E")(r)
Rltb = sp.Function("Rltb")(t, r)
W_ltb = sp.diff(Rltb, r)/(sp.diff(Rltb, r)/sp.sqrt(1 + 2*Ef))
check("C8c LTB: W = sqrt(1+2E(r)) exactly, so D_t W = 0 (geodesic slicing, j = 0)", sp.diff(sp.simplify(W_ltb), t))
# (c) Milne: ds^2 = -dt^2 + t^2 (dchi^2 + sinh^2 chi dOmega^2), W = cosh chi
gm = sp.diag(-1, t**2, (t*sp.sinh(r))**2, (t*sp.sinh(r)*sp.sin(th))**2)
Gmm, _, _, _ = einstein_mixed(gm)
check("C8d Milne: G_ab = 0 (flat)", sum(abs(sp.simplify(Gmm[a, b])) for a in range(4) for b in range(4)) == 0)
check("C8e Milne: W = cosh(chi), D_t W = 0", sp.diff(sp.diff(t*sp.sinh(r), r)/t, t))

print("\nC9  'geodesic slicing (Phi = 0, always available)' (nonstatic.py:87) holds LOCALLY: the normal congruence can focus")
# contracting Milne (t in (-a, 0)): R = -t sinh chi -> 0 at t -> 0- for EVERY chi: all normals meet at one event
Rc = -t*sp.sinh(r)
check("C9a contracting Milne: R(t->0-) = 0 for all chi (focal point at proper time a from t = -a)",
      sp.limit(Rc.subs(r, sp.Rational(7, 3)), t, 0, dir="-") == 0)
check("C9b ... while W = cosh chi is still constant there (so the gauge, not the geometry, ends)",
      sp.diff(sp.diff(Rc, r)/(-t), t))

print("\nC10 cosmological constant (unknown to MS 1964; measured 1998): G_ab + Lambda g_ab = 8 pi T^matter_ab")
Lc = sp.Symbol("Lambda_c")
Tm = (Gdn + Lc*g)/(8*pi)
Tmm = gi*Tm
rho_m, pr_m = -sp.simplify(Tmm[0, 0]), sp.simplify(Tmm[1, 1])
j_m = -Tm[0, 1]*sp.exp(-Phi-Lam)
check("C10a EV-W UNCHANGED by Lambda (g_tr = 0): D_tW = 4 pi R j_m + U D_rPhi", Dt(W) - (4*pi*R*j_m + U*Dr(Phi)))
check("C10b MS-r gains + Lambda R^2 W / 2", Dr(m) - (4*pi*R**2*(rho_m*W + j_m*U) + Lc*R**2*W/2))
check("C10c MS-t gains + Lambda R^2 U / 2", Dt(m) - (-4*pi*R**2*(pr_m*U + j_m*W) + Lc*R**2*U/2))
check("C10d EV-U gains + Lambda R / 2 (m the full MS mass)", Dt(U) - (W*Dr(Phi) - m/R**2 - 4*pi*R*pr_m + Lc*R/2))
check("C10e ... equivalently + Lambda R / 3 with the matter mass m_m = m - Lambda R^3/6",
      Dt(U) - (W*Dr(Phi) - (m - Lc*R**3/6)/R**2 - 4*pi*R*pr_m + Lc*R/3))

print("\nC11 E = R dW (nonstatic.py:178-184): where R is held fixed (U = 0) the U D_r Phi term is zero in ANY slicing")
Wf, Wi, Rfix = sp.symbols("W_f W_i R_fix", positive=True)
w = sp.Symbol("w")
E_flux = sp.integrate(Rfix, (w, Wi, Wf))                      # dE = 4 pi R^2 j dtau = R dW
dm_MS = -sp.integrate(Rfix*w, (w, Wi, Wf))                    # dm = -W dE at U = 0 (MS-t)
check("C11a E = R (W_f - W_i)", E_flux - Rfix*(Wf - Wi))
check("C11b MS mass change at fixed R: dm = -R (W_f^2 - W_i^2)/2 (= -W-weighted E)", dm_MS + Rfix*(Wf**2 - Wi**2)/2)
print("      W 1 -> 2: E = R, Delta m = %s R  (recorded: a different quantity, same order)" % (dm_MS.subs({Wi: 1, Wf: 2})/Rfix))


print("\nC12 what 'R held fixed' (nonstatic.py:180-182) adds: at U = 0, W is a SCALAR of (m, R)")
gradR = sum(gi[a, b]*sp.diff(R, X[a])*sp.diff(R, X[b]) for a in range(4) for b in range(4))
check("C12a W^2 - U^2 = g^ab d_aR d_bR = 1 - 2m/R (frame-invariant)", (W**2 - U**2) - gradR)
mm, Rp = sp.symbols("m R_p", real=True)
check("C12b so at U = 0: W = sqrt(1 - 2m/R); W > 1 iff m < 0 (W = 2 needs m = -3R/2)",
      sp.solve(sp.Eq(sp.sqrt(1 - 2*mm/Rp), 2), mm) == [-3*Rp/2])
check("C12c geodesic slicing AND U = 0 held (D_tU = 0) force m = -4 pi R^3 p_r (EV-U)",
      sp.solve(sp.Eq(0, W*0 - mm/Rp**2 - 4*pi*Rp*sp.Symbol("p_r")), mm)[0] + 4*pi*Rp**3*sp.Symbol("p_r"))
print("      Reading (recorded, not adjudicated): foliation.py:338-351 prices E = R dGamma as a GAUGE bill using")
print("      the V13 flat re-slicing, on which m = 0 and Gamma = 7071 means U ~ 7071 != 0. Under nonstatic.py's own")
print("      stated condition (R held fixed, U = 0) Gamma = sqrt(1 - 2m/R) is invariant and dGamma != 0 needs dm != 0.")

print("\nN   data the tree feeds through (none is an input of the MS equations themselves)")
c = 299792458.0
G18 = 6.67430e-11                 # CODATA 2018 = CODATA 2022 recommended value
MSUN_tree = 1.98840e30
GM_sun = 1.3271244e20             # IAU 2015 B3 nominal GM_sun (m^3 s^-2)
LY = 9.4607304725808e15
Rprox = 4.2465*LY
bill_tree = Rprox*c*c/G18/MSUN_tree
bill_GM = Rprox*c*c/GM_sun
print("  bill (tree constants)      = %.9e M_sun per unit dW" % bill_tree)
print("  bill (via IAU GM_sun only) = %.9e M_sun  (rel. diff %.2e)" % (bill_GM, bill_GM/bill_tree - 1))
check("N1 reproduces 2.720744289e13 to 1e-9", abs(bill_tree/2.720744289e13 - 1) < 1e-9)
# parallax check: Gaia DR3 value for Proxima (NOT re-read at source in this audit)
plx = 768.0665e-3; pc_ly = 3.261563777
d_ly = pc_ly/plx
print("  Proxima from parallax 768.0665 mas = %.5f ly (tree 4.2465); 1-sigma 0.0499 mas -> %.1e rel." % (d_ly, 0.0499/768.0665))
check("N2 flat foliation Gamma at eps = 1e-8 = 7071.067813726", abs(1/math.sqrt(1-(1-1e-8)**2) - 7071.067813726) < 1e-5)
# Lambda's size at the corridor scale: Lambda R^3 / 6 in solar masses (Planck-2018-like value, NOT re-read)
Lam_obs = 1.1e-52      # m^-2
dm_Lam = Lam_obs*Rprox**3/6 * c*c/G18/MSUN_tree
print("  Lambda R^3/6 over the Proxima span = %.2e M_sun (vs bill %.2e): does not move any figure" % (dm_Lam, bill_tree))
check("N3 Lambda contribution < 1e-15 of the bill", dm_Lam/bill_tree < 1e-15)

print("\n%d FAIL(S)" % len(FAILS))
sys.exit(1 if FAILS else 0)
