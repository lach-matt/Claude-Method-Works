#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Herrera arXiv:1801.08358v2 eqs (20)-(22), the Darmois
matching of a static spherically symmetric anisotropic fluid to Schwarzschild,
and the tree's use of eq (22) in research/warp-drive/tolman.py:2396-2408 (L1).

Signature (+,-,-,-) and conventions exactly as the source, eq (1)-(8).
Checks, each printed PASS/FAIL:
  A  eq (7) for P_r from the computed Einstein tensor; eq (10) from (7)+(12)
  B  extrinsic curvature of r = const; Darmois [h]=[K]=0 <=> (20),(21),(22)
     (necessity AND sufficiency, given no surface layer)
  C  Israel: if (20),(21) hold and P_r(r_S) = p0 != 0, the surface layer has
     sigma = 0 and a tangential stress proportional to p0 -- so 'necessary'
     needs 'no thin shell' (Herrera's word 'smooth')
  D  conservation div T = 0 for T^mu_nu = diag(u,-p_r,-p_t,-p_t) on a FIXED
     background reproduces Herrera eq (9) -- the test-field route
  E  distributional conservation on a fixed background: delta-coefficient
     -P(R) + nu'(R) sigma/2 - 2 s/R = 0, so p_r(R^-) = 0 iff no surface layer
     (the tree's test-field class reaches eq (22)'s conclusion by THIS route,
     not by Herrera's sourced-geometry route)
  F  worked counterexample to 'bounded => p_r = 0 at the cut' when a surface
     layer is present: traceless flat source + traceless shell; and the check
     that L1's TOTAL-mass conclusion survives when the cut is outside the shell
  G  in-class positive control: a smooth traceless conserved flat source with
     p_r(R) = 0 has m(R) = 0 (L1 as used)
"""
import sympy as sp

ok_all = True


def check(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print(("PASS " if cond else "FAIL ") + label)


t, r, th, ph = sp.symbols("t r theta phi", real=True)
X = [t, r, th, ph]
nu = sp.Function("nu")(r)
lam = sp.Function("lam")(r)


def christoffel(g):
    gi = g.inv()
    G = [[[0] * 4 for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                G[a][b][c] = sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                                         - sp.diff(g[b, c], X[d])) for d in range(4)) / 2)
    return G


def ricci(G):
    R = sp.zeros(4)
    for b in range(4):
        for c in range(4):
            R[b, c] = sp.simplify(sum(sp.diff(G[a][b][c], X[a]) - sp.diff(G[a][b][a], X[c])
                                      + sum(G[a][a][d] * G[d][b][c] - G[a][c][d] * G[d][b][a] for d in range(4))
                                      for a in range(4)))
    return R


g = sp.diag(sp.exp(nu), -sp.exp(lam), -r ** 2, -r ** 2 * sp.sin(th) ** 2)
gi = g.inv()
Gam = christoffel(g)
Ric = ricci(Gam)
Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(4) for b in range(4)))
Gmix = sp.simplify(gi * Ric - sp.eye(4) * Rs / 2)   # G^mu_nu

# ---------------- A: eq (7) and eq (10)
nup = sp.diff(nu, r)
lamp = sp.diff(lam, r)
Pr_herrera = -(1 / (8 * sp.pi)) * (1 / r ** 2 - sp.exp(-lam) * (1 / r ** 2 + nup / r))
Pr_computed = -Gmix[1, 1] / (8 * sp.pi)             # T^1_1 = -P_r, eq (4)
check("A1 eq (7): P_r = -G^1_1/8pi equals Herrera's expression",
      sp.simplify(Pr_computed - Pr_herrera) == 0)
mu_herrera = -(1 / (8 * sp.pi)) * (-1 / r ** 2 + sp.exp(-lam) * (1 / r ** 2 - lamp / r))
check("A2 eq (6): mu = G^0_0/8pi equals Herrera's expression",
      sp.simplify(Gmix[0, 0] / (8 * sp.pi) - mu_herrera) == 0)
m, P, NUP = sp.symbols("m P_r nuprime", real=True)
eq7 = sp.Eq(P, (-(1 / (8 * sp.pi)) * (1 / r ** 2 - (1 - 2 * m / r) * (1 / r ** 2 + NUP / r))))
nup_sol = sp.solve(eq7, NUP)[0]
check("A3 eq (10): nu' = 2(m + 4 pi P_r r^3)/(r(r-2m)) from (7) and e^-lam = 1-2m/r",
      sp.simplify(nup_sol - 2 * (m + 4 * sp.pi * P * r ** 3) / (r * (r - 2 * m))) == 0)

# ---------------- B: extrinsic curvature of r = const, n_mu = (0, e^{lam/2}, 0, 0)
n_low = [0, sp.exp(lam / 2), 0, 0]
Klow = sp.zeros(4)
for a in (0, 2, 3):
    for b in (0, 2, 3):
        Klow[a, b] = sp.simplify(sp.diff(n_low[b], X[a]) - sum(Gam[c][a][b] * n_low[c] for c in range(4)))
Ktt = sp.simplify(gi[0, 0] * Klow[0, 0])   # mixed K^t_t
Kthth = sp.simplify(gi[2, 2] * Klow[2, 2])  # mixed K^theta_theta
print("   K^t_t =", Ktt, "   K^th_th =", Kthth)
sgn = sp.simplify(Kthth / (sp.exp(-lam / 2) / r))   # common overall sign (normal-orientation convention)
check("B0 K^t_t = e^{-lam/2} nu'/2 and K^th_th = e^{-lam/2}/r, up to ONE common overall sign",
      sgn in (1, -1) and sp.simplify(Ktt - sgn * sp.exp(-lam / 2) * nup / 2) == 0)

rS, M, L0, N1, p0 = sp.symbols("r_Sigma M L0 N1 p0", positive=True)
# interior values at r_S: e^{-lam} = L0, nu' = N1 ; exterior Schwarzschild
f = 1 - 2 * M / rS
Ktt_in = sp.sqrt(L0) * N1 / 2
Kth_in = sp.sqrt(L0) / rS
Ktt_out = sp.sqrt(f) * (2 * M / (rS * (rS - 2 * M))) / 2
Kth_out = sp.sqrt(f) / rS
solL = sp.solve(sp.Eq(Kth_in, Kth_out), L0)
print("   solve [K^th_th]=0 for e^{-lam_S}:", solL)
check("B1 [K^th_th] = 0  <=>  e^{-lam_S} = 1 - 2M/r_S  (eq 21)", len(solL) == 1 and sp.simplify(solL[0] - f) == 0)
Ktt_in21 = Ktt_in.subs(L0, f)
solN = sp.solve(sp.Eq(Ktt_in21, Ktt_out), N1)
check("B2 given (21), [K^t_t] = 0  <=>  nu'_S = 2M/(r_S(r_S-2M))", len(solN) == 1 and
      sp.simplify(solN[0] - 2 * M / (rS * (rS - 2 * M))) == 0)
# (21) with eq (12) gives m(r_S) = M; then eq (10) at r_S
mS = sp.solve(sp.Eq(1 - 2 * m / rS, f), m)[0]
check("B3 (21) + eq (12)  =>  m(r_S) = M", sp.simplify(mS - M) == 0)
nup_int_S = nup_sol.subs({m: M, r: rS})
solP = sp.solve(sp.Eq(nup_int_S, solN[0]), P)
check("B4 given (21), [K^t_t] = 0  <=>  P_r(r_S) = 0  (eq 22, necessity)", solP == [0])
# sufficiency: with (21) and P_r = 0 every mixed K component matches
check("B5 sufficiency: (21) & P_r(r_S)=0  =>  [K^t_t] = [K^th_th] = 0",
      sp.simplify(Ktt_in.subs({L0: f, N1: nup_int_S.subs(P, 0)}) - Ktt_out) == 0 and
      sp.simplify(Kth_in.subs(L0, f) - Kth_out) == 0)
print("   (eq 20 is [h]=0 with the exterior time normalised so the constant factor is 1:"
      " a coordinate choice, not a physical condition)")

# ---------------- C: Israel surface layer when P_r(r_S) = p0 != 0
jKtt = sp.simplify(Ktt_out - Ktt_in.subs({L0: f, N1: nup_int_S.subs(P, p0)}))
jKth = sp.simplify(Kth_out - Kth_in.subs(L0, f))
trJ = jKtt + 2 * jKth
S_tt = sp.simplify(-(jKtt - trJ) / (8 * sp.pi))   # S^a_b = -([K^a_b] - delta [K])/8pi
S_thth = sp.simplify(-(jKth - trJ) / (8 * sp.pi))
print("   [K^t_t] =", jKtt, "  S^t_t (surface energy) =", S_tt, "  S^th_th =", S_thth)
check("C1 with p0 != 0 the shell has ZERO surface energy (S^t_t = 0)", S_tt == 0)
check("C2 ... and a tangential surface stress proportional to p0 (nonzero iff p0 != 0)",
      sp.simplify(S_thth.subs(p0, 0)) == 0 and sp.simplify(S_thth) != 0 and
      sp.simplify(sp.diff(S_thth, p0, 2)) == 0)

# ---------------- D: conservation on a FIXED background (test-field route)
u = sp.Function("u")(r)
pr = sp.Function("p_r")(r)
pt = sp.Function("p_t")(r)
T = sp.diag(u, -pr, -pt, -pt)                     # T^mu_nu
sqrtg = sp.exp((nu + lam) / 2) * r ** 2 * sp.sin(th)
nu_idx = 1
divT = sp.simplify(sum(sp.diff(sqrtg * T[a, nu_idx], X[a]) for a in range(4)) / sqrtg
                   - sum(Gam[b][a][nu_idx] * T[a, b] for a in range(4) for b in range(4)))
herrera9 = sp.diff(pr, r) + nup / 2 * (u + pr) - 2 * (pt - pr) / r
check("D1 nabla_mu T^mu_r = 0 on a fixed background IS Herrera eq (9) (up to sign)",
      sp.simplify(divT + herrera9) == 0)

# ---------------- E: distributional conservation, bounded source + possible surface layer
Rb, sig, s = sp.symbols("R sigma s", real=True)
Pf, Qf, Uf, NUf = [sp.Function(n)(r) for n in ("P", "Q", "U", "NUP")]
H = sp.Heaviside(Rb - r)
D = sp.DiracDelta(r - Rb)
pr_d = Pf * H
pt_d = Qf * H + s * D
u_d = Uf * H + sig * D
cons = sp.diff(pr_d, r) + NUf / 2 * (u_d + pr_d) - 2 * (pt_d - pr_d) / r
cons = sp.expand(cons.replace(sp.DiracDelta(Rb - r), sp.DiracDelta(r - Rb)))
dcoef = sp.expand(cons).coeff(sp.DiracDelta(r - Rb)).subs(r, Rb)
print("   delta(r-R) coefficient of div T:", sp.simplify(dcoef))
check("E1 delta-coefficient = -P(R) + nu'(R) sigma/2 - 2 s/R",
      sp.simplify(dcoef - (-Pf.subs(r, Rb) + NUf.subs(r, Rb) * sig / 2 - 2 * s / Rb)) == 0)
check("E2 no surface layer (sigma = s = 0)  =>  p_r(R^-) = 0  on ANY fixed background",
      sp.solve(dcoef.subs({sig: 0, s: 0}), Pf.subs(r, Rb)) == [0])

# ---------------- F: counterexample with a surface layer, flat, traceless everywhere
p0f = sp.symbols("p_0", positive=True)
# interior: p_r = p_t = p0, u = 3 p0  (traceless, conserved in flat space)
check("F0 interior p_r=p_t=p0, u=3p0 is traceless and flat-conserved",
      (3 * p0f - p0f - 2 * p0f) == 0 and sp.diff(p0f, r) + 2 * (p0f - p0f) / r == 0)
s_sol = sp.solve(sp.Eq(-p0f - 2 * s / Rb, 0), s)[0]   # E1 with nu' = 0
sig_sol = 2 * s_sol                                   # shell trace sigma - 2 s = 0
print("   shell: s =", s_sol, "  sigma =", sig_sol)
m_in = sp.integrate(4 * sp.pi * r ** 2 * 3 * p0f, (r, 0, Rb))
m_out = m_in + 4 * sp.pi * Rb ** 2 * sig_sol
check("F1 bounded traceless source WITH a traceless shell has p_r(R^-) = p0 != 0",
      p0f != 0 and sp.simplify(m_in - 4 * sp.pi * Rb ** 3 * p0f) == 0)
check("F2 identity m = 4 pi R^3 p_r holds at R^- (m = 4 pi R^3 p0)",
      sp.simplify(m_in - 4 * sp.pi * Rb ** 3 * p0f) == 0)
check("F3 at R^+ (cut outside the shell) m = 0 = 4 pi R^3 p_r(R^+): L1's TOTAL-mass "
      "conclusion survives without eq (22)", sp.simplify(m_out) == 0)
check("F4 the traceless shell has NEGATIVE surface energy (sigma = -p0 R)",
      sp.simplify(sig_sol + p0f * Rb) == 0)

# ---------------- G: in-class positive control
A_ = sp.symbols("A", positive=True)
prG = A_ * (Rb ** 2 - r ** 2) ** 2
ptG = sp.expand(prG + r * sp.diff(prG, r) / 2)       # flat conservation solved for p_t
uG = prG + 2 * ptG                                   # traceless
mG = sp.integrate(4 * sp.pi * r ** 2 * uG, (r, 0, Rb))
check("G1 flat conservation holds for the control", sp.simplify(sp.diff(prG, r) + 2 * (prG - ptG) / r) == 0)
check("G2 identity m(r) = 4 pi r^3 p_r(r) for the control at every r",
      sp.simplify(sp.integrate(4 * sp.pi * r ** 2 * uG, (r, 0, r)) - 4 * sp.pi * r ** 3 * prG) == 0)
check("G3 p_r(R) = 0 (eq 22's conclusion) gives m(R) = 0 (L1 as used)", sp.simplify(mG) == 0)

print("\nALL PASS" if ok_all else "\nSOME FAILED")
raise SystemExit(0 if ok_all else 1)
