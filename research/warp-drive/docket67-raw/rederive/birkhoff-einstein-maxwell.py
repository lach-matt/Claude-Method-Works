#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for 'birkhoff-einstein-maxwell'.

Independent of drivensource.py: nothing is imported from the board.  The
Einstein tensor is built from the metric here (Christoffels -> Riemann ->
Ricci -> G), not taken from nonstatic.py's MS equations.

  E1  the tree's MS-r / MS-t ARE Einstein's G_uu, G_un, G_nn components
      (identity for arbitrary Phi(t,r), Lambda(t,r), R(t,r))
  E2  DYONIC Maxwell field F_tr = Q e^{Phi+Lam}/R^2, F_thph = P sin(th):
      Maxwell holds for arbitrary Phi, Lam, R; rho = (Q^2+P^2)/(8 pi R^4),
      j = 0, p_r = -rho, p_T = +rho  (the tree drops P; line ~295)
  E3  mass freezing: m = M - (Q^2+P^2)/(2R) solves MS-r and MS-t for
      arbitrary Phi, Lam, R, and any solution differs from it by a constant
  E4  the full Birkhoff step (Frolov-Zelnikov Thm, restated 2605.01811):
      trace-free 2D Einstein = -(2/R) trace-free Hessian of R (identity);
      electrovac T_AB = -rho gamma_AB is pure trace, so Hess R ~ gamma, and the
      Kodama vector K^A = eps^{AB} d_B R is then Killing (checked explicitly)
  E5  the EXCEPTION: Bertotti-Robinson AdS2 x S2, R0^2 = Q^2+P^2, solves
      Einstein-Maxwell with grad R = 0; it is NOT locally RN (Weyl = 0 vs RN
      Weyl != 0) -- yet its MS mass is R0/2, a constant: m = M - Q^2/2R
      with M = R0 (the extremal value), so the 'frozen mass' claim survives
      the exception although 'spherical electrovac is RN' does not
  E6  Lambda (unstated at the owner): m = M - Q^2/2R + Lambda R^3/6 is the
      frozen form; the tree's formula is the Lambda = 0 case
  E7  slicing note (use, not source): in RN, W^2 - U^2 = 1 - 2m/R is
      slice-invariant, and the driven condition 2m/R < U^2 (W > 1) holds for a
      boosted slice-normal at fixed R -- z3: satisfiable with M>0, Q>0, R>r+
  E8  sanity: RN is recovered in static gauge (G = 8 pi T component-wise)
"""
import sys
import sympy as sp

PASS = FAIL = 0


def chk(label, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("  PASS", label)
    else:
        FAIL += 1
        print("  FAIL", label)


def z(e):
    return sp.simplify(e) == 0


t, r, th, ph = sp.symbols("t r theta phi", real=True)
X = [t, r, th, ph]
Phi = sp.Function("Phi")(t, r)
Lam = sp.Function("Lambda")(t, r)
R = sp.Function("R")(t, r)
Q, P, M, Lc = sp.symbols("Q P M Lambda_c", real=True)


def einstein(g, x):
    n = len(x)
    gi = sp.simplify(g.inv())
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                                          - sp.diff(g[b, c], x[d])) for d in range(n)) / 2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            Ric[b, c] = sp.simplify(sum(sp.diff(Gam[a][b][c], x[a]) - sp.diff(Gam[a][b][a], x[c])
                                        + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
                                              for d in range(n)) for a in range(n)))
    Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    G = sp.simplify(Ric - Rs * g / 2)
    return G, gi, Gam


print("E1  MS-r / MS-t are Einstein components (arbitrary Phi, Lambda, R)")
g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R**2, R**2 * sp.sin(th)**2)
G, gi, Gam = einstein(g, X)
Guu = sp.simplify(G[0, 0] * sp.exp(-2 * Phi))
Gun = sp.simplify(G[0, 1] * sp.exp(-Phi - Lam))
Gnn = sp.simplify(G[1, 1] * sp.exp(-2 * Lam))
GTT = sp.simplify(G[2, 2] / R**2)
Dt = lambda f: sp.exp(-Phi) * sp.diff(f, t)
Dr = lambda f: sp.exp(-Lam) * sp.diff(f, r)
U, W = Dt(R), Dr(R)
m_ms = R / 2 * (1 - W**2 + U**2)
# 8 pi rho = Guu, 8 pi j = -Gun, 8 pi p_r = Gnn
chk("D_r m == (R^2/2)(G_uu W - G_un U)  [MS-r with rho, j from G]",
    z(Dr(m_ms) - R**2 / 2 * (Guu * W - Gun * U)))
chk("D_t m == -(R^2/2)(G_nn U - G_un W)  [MS-t with p_r, j from G]",
    z(Dt(m_ms) + R**2 / 2 * (Gnn * U - Gun * W)))

print("E2  dyonic Maxwell field in the full dynamical metric")
F = sp.zeros(4, 4)
F[0, 1] = Q * sp.exp(Phi + Lam) / R**2
F[1, 0] = -F[0, 1]
F[2, 3] = P * sp.sin(th)
F[3, 2] = -F[2, 3]
Fup = gi * F * gi
sg = sp.exp(Phi + Lam) * R**2 * sp.sin(th)
chk("d*F = 0 (all four components)",
    all(z(sum(sp.diff(sg * Fup[a, b], X[a]) for a in range(4))) for b in range(4)))
chk("dF = 0 (all cyclic triples)",
    all(z(sp.diff(F[a, b], X[c]) + sp.diff(F[b, c], X[a]) + sp.diff(F[c, a], X[b]))
        for a in range(4) for b in range(4) for c in range(4)))
Fsq = sum(F[a, b] * Fup[a, b] for a in range(4) for b in range(4))
Fmix = F * gi
T = sp.Matrix(4, 4, lambda a, b: sp.simplify(
    (sum(F[a, c] * Fmix[b, c] for c in range(4)) - g[a, b] * Fsq / 4) / (4 * sp.pi)))
rho = sp.simplify(T[0, 0] * sp.exp(-2 * Phi))
j = sp.simplify(-T[0, 1] * sp.exp(-Phi - Lam))
p_r = sp.simplify(T[1, 1] * sp.exp(-2 * Lam))
p_T = sp.simplify(T[2, 2] / R**2)
chk("rho = (Q^2+P^2)/(8 pi R^4)", z(rho - (Q**2 + P**2) / (8 * sp.pi * R**4)))
chk("j = 0", z(j))
chk("p_r = -rho", z(p_r + rho))
chk("p_T = +rho", z(p_T - rho))
chk("off-diagonal T_{t th}, T_{r ph} etc vanish",
    all(z(T[a, b]) for a in range(4) for b in range(4) if a != b and not (a, b) in [(0, 1), (1, 0)]))

print("E3  mass freezing (the tree's birkhoff_residuals, dyonic, independent code)")
m_fr = M - (Q**2 + P**2) / (2 * R)
chk("MS-r residual 0 for arbitrary Phi, Lam, R",
    z(Dr(m_fr) - 4 * sp.pi * R**2 * (rho * W + j * U)))
chk("MS-t residual 0 for arbitrary Phi, Lam, R",
    z(Dt(m_fr) + 4 * sp.pi * R**2 * (p_r * U + j * W)))
# uniqueness: any m solving both has D_r(m - m_fr) = D_t(m - m_fr) = 0
mm = sp.Function("m")(t, r)
eq_r = sp.simplify(Dr(mm) - 4 * sp.pi * R**2 * (rho * W + j * U))
eq_t = sp.simplify(Dt(mm) + 4 * sp.pi * R**2 * (p_r * U + j * W))
chk("MS-r - MS-r[m_fr] = D_r(m - m_fr): gradient of (m - m_fr) is forced to 0",
    z(eq_r - Dr(mm - m_fr)) and z(eq_t - Dt(mm - m_fr)))

print("E4  full Birkhoff: trace-free Hessian identity and Kodama Killing vector")
xs = [t, r]
g2 = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam))
g2i = g2.inv()
Gam2 = [[[sum(g2i[a, d] * (sp.diff(g2[d, b], xs[c]) + sp.diff(g2[d, c], xs[b])
                           - sp.diff(g2[b, c], xs[d])) for d in range(2)) / 2
          for c in range(2)] for b in range(2)] for a in range(2)]
H = sp.Matrix(2, 2, lambda a, b: sp.diff(R, xs[a], xs[b]) - sum(Gam2[c][a][b] * sp.diff(R, xs[c]) for c in range(2)))
trH = sp.simplify(sum(g2i[a, b] * H[a, b] for a in range(2) for b in range(2)))
G2 = G[:2, :2]
trG2 = sp.simplify(sum(g2i[a, b] * G2[a, b] for a in range(2) for b in range(2)))
ok = all(z(G2[a, b] - g2[a, b] * trG2 / 2 + 2 / R * (H[a, b] - g2[a, b] * trH / 2))
         for a in range(2) for b in range(2))
chk("G_AB - (1/2) gamma_AB G  ==  -(2/R)(H_AB - (1/2) gamma_AB tr H)  (identity)", ok)
T2 = T[:2, :2]
chk("electrovac T_AB = -rho gamma_AB (pure trace in the orbit space)",
    all(z(T2[a, b] + rho * g2[a, b]) for a in range(2) for b in range(2)))
# Kodama vector K_A = eps_AB g^{BC} d_C R ; eps_tr = sqrt(-det g2)
e = sp.exp(Phi + Lam)
eps = sp.Matrix([[0, e], [-e, 0]])
dR = sp.Matrix([sp.diff(R, t), sp.diff(R, r)])
Kl = eps * (g2i * dR)
nabK = sp.Matrix(2, 2, lambda a, b: sp.diff(Kl[b], xs[a]) - sum(Gam2[c][a][b] * Kl[c] for c in range(2)))
Kill = sp.simplify(nabK + nabK.T)
# express Killing operator via trace-free Hessian Hf: 2 nabla_(A K_B) = eps_B^C Hf_AC + eps_A^C Hf_BC
Hf = sp.simplify(H - g2 * trH / 2)
epsmix = eps * g2i   # eps_A^C = eps_AD g^DC
rhs = sp.Matrix(2, 2, lambda a, b: sum(epsmix[b, c] * Hf[a, c] + epsmix[a, c] * Hf[b, c] for c in range(2)))
chk("2 nabla_(A K_B) == eps_B^C Hf_AC + eps_A^C Hf_BC (so Hf = 0 => K Killing)",
    all(z(Kill[a, b] - rhs[a, b]) for a in range(2) for b in range(2)))
chk("K.K = -grad R.grad R: K timelike iff grad R spacelike (static only there)",
    z((Kl.T * g2i * Kl)[0] + (dR.T * g2i * dR)[0]))

print("E5  the exception grad R = 0: Bertotti-Robinson is electrovac and NOT RN")
y = sp.symbols("y", positive=True)
R0 = sp.symbols("R0", positive=True)
gBR = sp.diag(-R0**2 / y**2, R0**2 / y**2, R0**2, R0**2 * sp.sin(th)**2)
XB = [t, y, th, ph]
GB, giB, _ = einstein(gBR, XB)
FB = sp.zeros(4, 4)
qe, qm = sp.symbols("q_e q_m", real=True)
FB[0, 1] = qe * R0**2 / y**2 / R0**2      # F_ty = q_e * sqrt(-g_tt g_yy) / R0^2
FB[1, 0] = -FB[0, 1]
FB[2, 3] = qm * sp.sin(th)
FB[3, 2] = -FB[2, 3]
FupB = giB * FB * giB
sgB = R0**4 / y**2 * sp.sin(th)
maxB = all(z(sum(sp.diff(sgB * FupB[a, b], XB[a]) for a in range(4))) for b in range(4))
FsqB = sum(FB[a, b] * FupB[a, b] for a in range(4) for b in range(4))
TB = sp.Matrix(4, 4, lambda a, b: sp.simplify(
    (sum(FB[a, c] * (FB * giB)[b, c] for c in range(4)) - gBR[a, b] * FsqB / 4) / (4 * sp.pi)))
resB = sp.simplify((GB - 8 * sp.pi * TB).subs(R0, sp.sqrt(qe**2 + qm**2)))
chk("BR: Maxwell holds and G = 8 pi T iff R0^2 = q_e^2 + q_m^2", maxB and resB == sp.zeros(4, 4))
chk("BR: R0 != sqrt(q_e^2+q_m^2) fails (the constraint is real)",
    sp.simplify((GB - 8 * sp.pi * TB).subs({R0: 2, qe: 1, qm: 0})) != sp.zeros(4, 4))
# Weyl scalar comparison via Kretschmann-minus-Ricci-part proxy: C_abcd C^abcd
def weyl_sq(gm, xx):
    n = 4
    gim = gm.inv()
    Gm = [[[sp.simplify(sum(gim[a, d] * (sp.diff(gm[d, b], xx[c]) + sp.diff(gm[d, c], xx[b])
                                          - sp.diff(gm[b, c], xx[d])) for d in range(n)) / 2)
            for c in range(n)] for b in range(n)] for a in range(n)]
    Riem = [[[[sp.simplify(sp.diff(Gm[a][b][d], xx[c]) - sp.diff(Gm[a][b][c], xx[d])
                           + sum(Gm[a][c][e] * Gm[e][b][d] - Gm[a][d][e] * Gm[e][b][c] for e in range(n)))
               for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    Rl = [[[[sp.simplify(sum(gm[a, e] * Riem[e][b][c][d] for e in range(n))) for d in range(n)]
            for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(Riem[a][b][a][d] for a in range(n))))
    Rs = sp.simplify(sum(gim[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    def C(a, b, c, d):
        return (Rl[a][b][c][d]
                - (gm[a, c] * Ric[b, d] - gm[a, d] * Ric[b, c] - gm[b, c] * Ric[a, d] + gm[b, d] * Ric[a, c]) / 2
                + Rs * (gm[a, c] * gm[b, d] - gm[a, d] * gm[b, c]) / 6)
    # diagonal metric: raise with gim diagonal entries
    tot = 0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    cc = C(a, b, c, d)
                    if cc != 0:
                        tot += cc**2 * gim[a, a] * gim[b, b] * gim[c, c] * gim[d, d]
    return sp.simplify(tot)
chk("BR: Weyl^2 = 0 (conformally flat)", z(weyl_sq(gBR, XB)))
rr = sp.symbols("r", positive=True)
Mp, Qp = sp.symbols("M Q", positive=True)
fRN = 1 - 2 * Mp / rr + Qp**2 / rr**2
gRN = sp.diag(-fRN, 1 / fRN, rr**2, rr**2 * sp.sin(th)**2)
w2 = weyl_sq(gRN, [t, rr, th, ph])
chk("RN: Weyl^2 = 48 (M r - Q^2)^2 / r^8 != 0, so BR is not locally RN",
    z(w2 - 48 * (Mp * rr - Qp**2)**2 / rr**8))
mBR = R0 / 2   # (R/2)(1 - W^2 + U^2) with W = U = 0
chk("BR: MS mass R0/2 = M - (q_e^2+q_m^2)/(2 R0) with constant M = R0 (extremal value)",
    z((mBR - (R0 - R0**2 / (2 * R0)))))

print("E6  cosmological constant: the frozen form carries Lambda R^3/6")
rhoL = rho + Lc / (8 * sp.pi)
prL = p_r - Lc / (8 * sp.pi)
mL = M - (Q**2 + P**2) / (2 * R) + Lc * R**3 / 6
chk("m = M - Q^2/2R + Lambda R^3/6 solves MS-r, MS-t (arbitrary Phi, Lam, R)",
    z(Dr(mL) - 4 * sp.pi * R**2 * (rhoL * W)) and z(Dt(mL) + 4 * sp.pi * R**2 * (prL * U)))
chk("the tree's Lambda-free m does NOT solve them when Lambda != 0",
    not z(Dr(m_fr) - 4 * sp.pi * R**2 * (rhoL * W)))

print("E7  slicing: the driven condition inside a fixed RN geometry")
import z3
Mz, Qz, Rz, g_, v_ = z3.Reals("M Q R gamma v")
f_ = 1 - 2 * Mz / Rz + Qz * Qz / (Rz * Rz)
mz = Mz - Qz * Qz / (2 * Rz)
s = z3.Solver()
# boosted slice-normal: U^2 = gamma^2 v^2 f, W^2 = gamma^2 f, gamma^2 (1 - v^2) = 1
s.add(Mz > 0, Qz > 0, Qz < Mz, Rz > 0, f_ > 0, Rz > 2 * Mz, v_ > 0, v_ < 1, g_ > 1,
      g_ * g_ * (1 - v_ * v_) == 1, 2 * mz / Rz < g_ * g_ * v_ * v_ * f_)
res = s.check()
chk("z3: driven condition 2m/R < U^2 SAT in RN exterior (a boosted slicing)", res == z3.sat)
if res == z3.sat:
    print("       witness:", s.model())
s2 = z3.Solver()
s2.add(Mz > 0, Qz > 0, Rz > 0, f_ > 0, g_ == 1, v_ == 0, g_ * g_ * (1 - v_ * v_) == 1,
       2 * mz / Rz < g_ * g_ * v_ * v_ * f_, 2 * mz / Rz > 0)
chk("z3: contrast -- static slice-normal (U = 0) with m > 0 is UNSAT, so the SAT above is the boost", s2.check() == z3.unsat)
Wsq, Usq = sp.symbols("W2 U2")
chk("W^2 - U^2 = 1 - 2m/R is slice-invariant (g^{ab} d_a R d_b R)",
    z(sp.simplify((W**2 - U**2) - (dR.T * g2i * dR)[0])))

print("E8  sanity: RN in static gauge satisfies G = 8 pi T (independent build)")
GRN, _, _ = einstein(gRN, [t, rr, th, ph])
TRN = sp.diag(fRN, -1 / fRN, rr**2, rr**2 * sp.sin(th)**2) * Qp**2 / (8 * sp.pi * rr**4)
chk("RN: G_ab = 8 pi T_ab with rho = Q^2/(8 pi r^4), p_r = -rho, p_T = rho",
    sp.simplify(GRN - 8 * sp.pi * TRN) == sp.zeros(4, 4))

print("E9  size of the Lambda term (Planck 2018 VI, arXiv:1807.06209 Table 2 / eq 14-15, READ)")
c = 299792458.0
Mpc = 3.0856775814913673e22
H0 = 67.36e3 / Mpc            # s^-1, TT,TE,EE+lowE+lensing
OL = 0.6847
Lam_SI = 3 * OL * H0**2 / c**2   # m^-2
print("       Lambda = 3 Omega_L H0^2 / c^2 = %.4e m^-2" % Lam_SI)
GN = 6.67430e-11
Msun_geo = GN * 1.98840987e30 / c**2    # m  (G M_sun / c^2, IAU nominal GM_sun ~ 1.3271244e20)
AU = 1.495978707e11
ratio = Lam_SI * AU**3 / 6 / Msun_geo
Req = (6 * Msun_geo / Lam_SI) ** (1 / 3)
print("       Lambda AU^3/6 / (G M_sun/c^2) = %.3e ; equality radius = %.3e m = %.1f pc" % (ratio, Req, Req / 3.0856775814913673e16))
chk("Lambda term negligible at 1 AU (ratio < 1e-20) -- a formula change, not a numerical one at lab/solar scales", ratio < 1e-20)

print("\n%d PASS, %d FAIL" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
