#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for 'penrose-weyl-curvature-hypothesis'.

The tree (research/warp-drive/permute.py:87-91, 441-443, 543-547) uses:
  (i)  the early universe had near-zero Weyl curvature / extremely low
       gravitational entropy (Penrose's hypothesis);
  (ii) gravitational clumping raises it, so structure formation 'is a
       relaxation'.

What is finite / closed-form and checkable here:
  C1  FLRW (k = 0, +1, -1) is conformally flat: C_abcd == 0 identically.
      (So 'Weyl near zero' for the early universe == 'close to FLRW'.)
  C2  Schwarzschild: R_ab == 0, C_abcd C^abcd = K = 48 M^2 / r^6 (G=c=1).
      A pure-Weyl vacuum -- so any Weyl-scalar measure is maximal where
      Ricci vanishes; Penrose's C^2 is a curvature, not an entropy.
  C3  Linear scalar perturbations of Einstein-de Sitter dust, both modes:
      Phi growing = const, decaying ~ a^(-5/2); delta_growing ~ a,
      delta_decaying ~ a^(-3/2).  Sub-horizon, the Weyl electric part
      E_ij = D_i D_j Phi (trace-free, physical), and the Poisson equation
      ties |E| / rho to delta.  The dimensionless ratio |E|/rho (the
      Wainwright-Anderson / Goode-Wainwright-type ratio, restricted to the
      electric part) scales exactly as |delta| in BOTH modes: it rises with
      clumping and falls with de-clumping.  It is monotone in the density
      contrast, which is (ii) in the one regime where it is computable --
      a statement about a chosen measure, not a theorem about entropy.
  C4  Self-gravitating virialised system: E = -K, so C = dE/dT < 0
      (negative heat capacity) -- the standard reason clumped states are
      entropically favoured for gravity.  Symbolic.
  C5  Penrose's number: S_BH for the baryonic mass of the observable
      universe with the 1979-style input N_b = 1e80, and with Planck 2018
      inputs; and the present CMB (photon+neutrino) entropy.  The
      conclusion 'early-universe entropy << gravitational maximum' does
      not move with the modern data.
"""
import math
import sympy as sp

ok_all = True


def chk(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print("  [%s] %s" % ("OK" if cond else "FAIL", label))


# ------------------------------------------------------------------ tensors
def christoffel(g, x):
    n = len(x)
    gi = g.inv()
    return [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                                          - sp.diff(g[b, c], x[d])) for d in range(n)) / 2)
              for c in range(n)] for b in range(n)] for a in range(n)]


def riemann(g, x):
    n = len(x)
    G = christoffel(g, x)
    R = sp.MutableDenseNDimArray.zeros(n, n, n, n)  # R^a_{bcd}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    e = sp.diff(G[a][b][d], x[c]) - sp.diff(G[a][b][c], x[d])
                    e += sum(G[a][c][f] * G[f][b][d] - G[a][d][f] * G[f][b][c] for f in range(n))
                    R[a, b, c, d] = sp.simplify(e)
    return R


def lower(g, R):
    n = g.shape[0]
    L = sp.MutableDenseNDimArray.zeros(n, n, n, n)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    L[a, b, c, d] = sp.simplify(sum(g[a, e] * R[e, b, c, d] for e in range(n)))
    return L


def weyl(g, x):
    n = len(x)
    R = riemann(g, x)
    Rl = lower(g, R)
    Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(R[a, b, a, d] for a in range(n))))
    gi = g.inv()
    Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    C = sp.MutableDenseNDimArray.zeros(n, n, n, n)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    e = Rl[a, b, c, d]
                    e -= (g[a, c] * Ric[b, d] - g[a, d] * Ric[b, c] - g[b, c] * Ric[a, d]
                          + g[b, d] * Ric[a, c]) / (n - 2)
                    e += Rs * (g[a, c] * g[b, d] - g[a, d] * g[b, c]) / ((n - 1) * (n - 2))
                    C[a, b, c, d] = sp.simplify(e)
    return C, Rl, Ric, Rs


def full_contract(g, T):
    n = g.shape[0]
    gi = g.inv()
    # T_{abcd} T^{abcd}; metrics here are diagonal
    s = 0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    s += T[a, b, c, d] ** 2 * gi[a, a] * gi[b, b] * gi[c, c] * gi[d, d]
    return sp.simplify(s)


print("C1  FLRW is conformally flat (k = 0, +1, -1)")
t, r, th, ph = sp.symbols('t r theta phi', positive=True)
a = sp.Function('a')(t)
for k in (0, 1, -1):
    g = sp.diag(-1, a ** 2 / (1 - k * r ** 2), a ** 2 * r ** 2, a ** 2 * r ** 2 * sp.sin(th) ** 2)
    C, _, _, _ = weyl(g, [t, r, th, ph])
    nz = [C[i, j, kk, l] for i in range(4) for j in range(4) for kk in range(4) for l in range(4)
          if sp.simplify(sp.expand_trig(sp.simplify(C[i, j, kk, l]))) != 0]
    chk("k=%+d: all 256 Weyl components vanish identically" % k, len(nz) == 0)

print("\nC2  Schwarzschild: Ricci-flat, all curvature is Weyl")
M = sp.symbols('M', positive=True)
f = 1 - 2 * M / r
g = sp.diag(-f, 1 / f, r ** 2, r ** 2 * sp.sin(th) ** 2)
C, Rl, Ric, Rs = weyl(g, [t, r, th, ph])
chk("R_ab == 0", all(sp.simplify(Ric[i, j]) == 0 for i in range(4) for j in range(4)))
CC = full_contract(g, C)
KK = full_contract(g, Rl)
chk("C_abcd C^abcd = 48 M^2 / r^6  (got %s)" % CC, sp.simplify(CC - 48 * M ** 2 / r ** 6) == 0)
chk("C^2 == Kretschmann (vacuum)", sp.simplify(CC - KK) == 0)
print("       -> a Weyl-scalar measure is unbounded at r->0 of a black hole AND of a")
print("          white hole (time-reverse, same C^2): the scalar alone carries no arrow.")
print("          Penrose's hypothesis supplies the arrow by FIAT (Weyl->0 at INITIAL")
print("          singularities only); it is a boundary condition, not a derivation.")

print("\nC3  Linear EdS dust: the Weyl/Ricci ratio tracks the density contrast")
A, k_, Phi0 = sp.symbols('a k Phi0', positive=True)
# EdS: H^2 = H0^2 a^-3, rho = 3H^2/(8 pi G); units 8 pi G = 1 -> rho = 3 H^2
H0 = sp.symbols('H0', positive=True)
H2 = H0 ** 2 * A ** -3
rho = 3 * H2
for mode, Phi in (("growing", Phi0), ("decaying", Phi0 * A ** sp.Rational(-5, 2))):
    # physical sub-horizon Poisson: (k/a)^2 Phi = -(1/2) rho delta   (8 pi G = 1 -> 4 pi G = 1/2)
    delta = sp.simplify(-2 * (k_ / A) ** 2 * Phi / rho)
    # physical Weyl electric part magnitude for a plane wave: |E| ~ (k/a)^2 |Phi| (trace-free
    # projection of k_i k_j Phi gives sqrt(2/3)(k/a)^2 Phi; constant factors do not affect scaling)
    Emag = sp.sqrt(sp.Rational(2, 3)) * (k_ / A) ** 2 * Phi
    ratio = sp.simplify(Emag / rho)
    p_delta = sp.simplify(A * sp.diff(sp.log(sp.Abs(delta)), A))
    p_ratio = sp.simplify(A * sp.diff(sp.log(sp.Abs(ratio)), A))
    print("   %-8s: delta ~ a^%s,  |E|/rho ~ a^%s,  |E|/rho / |delta| = %s"
          % (mode, p_delta, p_ratio, sp.simplify(sp.Abs(ratio / delta))))
    chk("%s: |E|/rho proportional to |delta| (same power of a)" % mode, sp.simplify(p_delta - p_ratio) == 0)
    # Hubble-normalised |E|/H^2 (the CET-style 'Hubble weighted anisotropy'):
    p_hub = sp.simplify(A * sp.diff(sp.log(sp.Abs(Emag / H2)), A))
    print("             |E|/H^2 ~ a^%s" % p_hub)
    chk("%s: |E|/H^2 rises iff delta rises" % mode, sp.sign(p_hub) == sp.sign(p_delta))
print("       -> in the one computable regime, 'clumping raises the Weyl measure' holds")
print("          for these measures in both modes; it is Poisson's equation, and it")
print("          says nothing about whether C-based measures ARE an entropy.")

print("\nC4  Negative heat capacity of a virialised self-gravitating system")
N, kB, T = sp.symbols('N k_B T', positive=True)
Kin = sp.Rational(3, 2) * N * kB * T
E = -Kin  # virial: 2K + U = 0 -> E = K + U = -K
Ccap = sp.diff(E, T)
chk("C = dE/dT = %s < 0" % Ccap, sp.simplify(Ccap + sp.Rational(3, 2) * N * kB) == 0)

print("\nC5  Penrose's entropy numbers, 1979-style inputs vs Planck 2018")
G_ = 6.67430e-11; hbar = 1.054571817e-34; c = 2.99792458e8; mp = 1.67262192e-27
kB_ = 1.380649e-23; Mpc = 3.0856775814913673e22


def s_bh(Mkg):
    return 4 * math.pi * G_ * Mkg ** 2 / (hbar * c)


S79 = s_bh(1e80 * mp)
print("   N_b = 1e80 (Penrose's order):  S_BH/k = %.2e  (log10 %.1f)" % (S79, math.log10(S79)))
# Planck 2018 TT,TE,EE+lowE+lensing (1807.06209 Table 2): H0 = 67.36, Omega_b h^2 = 0.02237
h = 0.6736; ombh2 = 0.02237
H0si = 100 * h * 1e3 / Mpc
rho_c = 3 * H0si ** 2 / (8 * math.pi * G_)
rho_b = ombh2 / h ** 2 * rho_c
R_obs = 14.26e3 * Mpc  # comoving particle horizon ~ 46.5 Gly (14.26 Gpc)
V = 4 / 3 * math.pi * R_obs ** 3
Mb = rho_b * V
Nb = Mb / mp
S18 = s_bh(Mb)
print("   Planck 2018: N_b = %.2e,  S_BH/k = %.2e (log10 %.1f)" % (Nb, S18, math.log10(S18)))
Tcmb = 2.7255
s_gamma = (2 * math.pi ** 2 / 45) * 2 * (kB_ * Tcmb / (hbar * c)) ** 3  # per m^3, in units of k
s_rad = s_gamma * 3.909 / 2  # photons + neutrinos, g_s = 3.909
print("   present CMB photon entropy: s/k = %.0f cm^-3; S/k = %.2e;  with nu: %.2e"
      % (s_gamma * 1e-6, s_gamma * V, s_rad * V))
gap79 = math.log10(S79) - math.log10(s_rad * V)
gap18 = math.log10(S18) - math.log10(s_rad * V)
print("   gap log10(S_BH / S_rad): 1979 input %.1f dex, Planck 2018 %.1f dex" % (gap79, gap18))
chk("gap exceeds 30 dex under both inputs (conclusion unmoved)", gap79 > 30 and gap18 > 30)
print("   Penrose's '1 in 10^(10^123)' is exp(-S_max) with S_max ~ 10^123: the")
print("   exponent moves by %.2f dex with Planck 2018 inputs." % (math.log10(S18) - math.log10(S79)))

print("\nOVERALL:", "ALL CHECKS PASS" if ok_all else "SOME CHECKS FAILED")
raise SystemExit(0 if ok_all else 1)
