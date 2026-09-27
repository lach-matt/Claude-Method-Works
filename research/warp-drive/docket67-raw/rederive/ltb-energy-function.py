#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of 'ltb-energy-function' (driven.py:78-80,215-217,398-406,596-601;
drivensource.py:183-186).  Reads research/warp-drive (import only, never writes).

C1  LTB dust metric: G_tr == 0, Gamma^2 = 1+2E (V9), MS identity, and Einstein eqs give
    R_t^2 = 2E + 2M/R + Lambda R^2/3 with m_MS = M + Lambda R^3/6.
C2  FRW with ARBITRARY a(t) (any pressure history): Gamma^2 = 1 - k r^2, E = -k r^2/2.
C3  General comoving diagonal metric: D_t Gamma = U D_r Phi - (R/2) e^{-Phi-Lam} G_tr, so
    E = (Gamma^2-1)/2 is conserved along the flow ONLY if D_r Phi = 0 and G_tr = 0 (no flux).
C4  z3/sympy: Lambda = 0 orbit classification -- E>0 <=> unbound (for every sign of M).
C5  Lambda != 0: E>0 neither necessary (Lambda>0) nor sufficient (Lambda<0) for unbound;
    threshold 2E_lim = -(3M)^{2/3} Lambda^{1/3} (Le Delliou-Mena-Mimoso 0911.0241 eq.15 conv.).
C6  Data: Planck 2018 Lambda; size of the misclassification window for local masses.
C7  Non-geodesic counterexample: Minkowski (m = 0), shells R = r0 + A sin T: E = U^2/2 > 0
    at almost every instant, every shell bounded.  'E > 0 => unbound' needs geodesic flow.
C8  The selftest fixture driven.contraction_is_unbound is an identity by construction (z3),
    and its float implementation disagrees at tiny U (cancellation in 1+U^2-2m/R-1).
"""
import math, os, sys
import sympy as sp

FAIL = []
def rep(tag, ok, detail=""):
    print("%-4s %-6s %s" % (tag, "PASS" if ok else "FAIL", detail))
    if not ok: FAIL.append(tag)

t, r, th, ph = sp.symbols("t r theta phi", real=True)
X = [t, r, th, ph]

def einstein(g):
    gi = g.inv()
    n = 4
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
             - sp.diff(g[b, c], X[d])) for d in range(n)) / 2) for c in range(n)]
             for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            Ric[b, c] = sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) for a in range(n))
                - sum(sp.diff(Gam[a][b][a], X[c]) for a in range(n))
                + sum(Gam[a][a][d] * Gam[d][b][c] for a in range(n) for d in range(n))
                - sum(Gam[a][c][d] * Gam[d][b][a] for a in range(n) for d in range(n)))
    Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    return sp.simplify(Ric - Rs * g / 2), gi

# ---------------- C1: LTB
R = sp.Function("R", positive=True)(t, r)
E = sp.Function("E", real=True)(r)
M = sp.Function("M", real=True)(r)
L = sp.Symbol("Lambda", real=True)
Rp, Rt = sp.diff(R, r), sp.diff(R, t)
g = sp.diag(-1, Rp**2 / (1 + 2 * E), R**2, R**2 * sp.sin(th)**2)
G, gi = einstein(g)
rep("C1a", sp.simplify(G[0, 1]) == 0, "LTB form: G_tr == 0 identically (no radial flux)")
Gam2 = sp.simplify(Rp**2 / g[1, 1])        # (e^{-Lam} R')^2
rep("C1b", sp.simplify(Gam2 - (1 + 2 * E)) == 0, "Gamma^2 = 1 + 2E (driven.py V9)")
mMS = sp.simplify(R / 2 * (1 - (gi[0, 0] * Rt**2 + gi[1, 1] * Rp**2)))
U = Rt
rep("C1c", sp.simplify(Gam2 - 1 - U**2 + 2 * mMS / R) == 0,
    "Misner-Sharp identity Gamma^2 = 1 + U^2 - 2m/R holds on LTB")
# impose the LTB evolution eq with Lambda and check the Einstein tensor is dust + Lambda
evo = {sp.diff(R, t): sp.sqrt(2 * E + 2 * M / R + L * R**2 / 3)}
Rtt = sp.diff(sp.sqrt(2 * E + 2 * M / R + L * R**2 / 3), t)
# vacuum-plus-Lambda check of the spatial trace: G^r_r = -Lambda for dust
Grr_mixed = sp.simplify((gi * G)[1, 1])
Grr_sub = Grr_mixed.subs(sp.diff(R, t, 2), sp.diff(R, t) * sp.diff(2 * E + 2 * M / R + L * R**2 / 3, R) / (2 * sp.diff(R, t)))
Grr_sub = sp.simplify(Grr_sub.subs(sp.diff(R, t), sp.sqrt(2 * E + 2 * M / R + L * R**2 / 3)))
rep("C1d", sp.simplify(Grr_sub + L) == 0,
    "with R_t^2 = 2E+2M/R+Lambda R^2/3: G^r_r = -Lambda, i.e. p = 0 (dust) plus Lambda")
mMS_on = sp.simplify(mMS.subs(sp.diff(R, t), sp.sqrt(2 * E + 2 * M / R + L * R**2 / 3)))
rep("C1e", sp.simplify(mMS_on - (M + L * R**3 / 6)) == 0,
    "on that solution m_MS = M + Lambda R^3/6 (Lambda sits inside the tree's m)")

# ---------------- C2: FRW, arbitrary a(t)
a = sp.Function("a", positive=True)(t)
k = sp.Symbol("k", real=True)
gF = sp.diag(-1, a**2 / (1 - k * r**2), a**2 * r**2, a**2 * r**2 * sp.sin(th)**2)
RF = a * r
Gam2F = sp.simplify(sp.diff(RF, r)**2 / gF[1, 1])
rep("C2", sp.simplify(Gam2F - (1 - k * r**2)) == 0,
    "FRW any a(t): Gamma^2 = 1 - k r^2 -> E = -k r^2/2, sign E = -sign k, time-independent")

# ---------------- C3: general comoving diagonal metric
Phi = sp.Function("Phi", real=True)(t, r)
Lam = sp.Function("Lam", real=True)(t, r)
Rg = sp.Function("R", positive=True)(t, r)
gg = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), Rg**2, Rg**2 * sp.sin(th)**2)
Gg, _ = einstein(gg)
Gtr = sp.simplify(Gg[0, 1])
target = -(2 / Rg) * (sp.diff(Rg, t, r) - sp.diff(Phi, r) * sp.diff(Rg, t) - sp.diff(Lam, t) * sp.diff(Rg, r))
rep("C3a", sp.simplify(Gtr - target) == 0, "G_tr = -(2/R)(R'_t - Phi' R_t - Lam_t R')")
Gam_g = sp.exp(-Lam) * sp.diff(Rg, r)
U_g = sp.exp(-Phi) * sp.diff(Rg, t)
DtGam = sp.exp(-Phi) * sp.diff(Gam_g, t)
rhs = U_g * sp.exp(-Lam) * sp.diff(Phi, r) - (Rg / 2) * sp.exp(-Phi - Lam) * Gtr
rep("C3b", sp.simplify(DtGam - rhs) == 0,
    "D_t Gamma = U D_r Phi - (R/2) e^{-Phi-Lam} G_tr  (matches driven.py:240 form 4 pi R j + U D_r Phi)")
print("     => D_t E = Gamma D_t Gamma: E is a constant of the flow only when D_r Phi = 0 "
      "(perfect fluid: p' = 0, Euler Phi' = -p'/(rho+p)) and G_tr = 0 (no flux).  LTB/FRW satisfy both.")

# ---------------- C4: Lambda = 0 classification, z3
import z3
Ez, Mz, Rz = z3.Reals("E M R")
f0 = 2 * Ez + 2 * Mz / Rz
s = z3.Solver(); s.add(Ez > 0, Mz >= 0, Rz > 0, f0 <= 0)
rep("C4a", s.check() == z3.unsat, "Lambda=0, E>0, M>=0: R_t^2 > 0 at every R>0 (never turns, unbound)")
s = z3.Solver(); s.add(Ez > 0, Mz < 0, Rz > 0, Rz > -Mz / Ez, f0 <= 0)
rep("C4b", s.check() == z3.unsat, "Lambda=0, E>0, M<0: R_t^2 > 0 for all R > |M|/E (bounce, then unbound)")
s = z3.Solver(); s.add(Ez < 0, Mz > 0, Rz > 0, Rz > Mz / (-Ez), f0 >= 0)
rep("C4c", s.check() == z3.unsat, "Lambda=0, E<0, M>0: R_t^2 < 0 beyond R = M/|E| (bound, recollapses)")
s = z3.Solver(); s.add(Ez <= 0, Mz <= 0, z3.Or(Ez < 0, Mz < 0), Rz > 0, f0 >= 0)
rep("C4d", s.check() == z3.unsat, "Lambda=0, E<=0, M<=0 (not both 0): no real motion at all")
print("     => Lambda = 0 dust: wherever motion exists, E>0 <=> unbound (hyperbolic), E=0 marginal, E<0 bound.")

# ---------------- C5: Lambda != 0
Lz = z3.Real("L")
fL = 2 * Ez + 2 * Mz / Rz + Lz * Rz * Rz / 3
s = z3.Solver(); s.add(Ez > 0, Mz > 0, Lz < 0, Rz > 0, fL == 0)
ok = s.check() == z3.sat
rep("C5a", ok, "Lambda<0, E>0: a turning point exists (bound with E>0) -- z3 witness %s" % (s.model() if ok else ""))
# Lambda>0, E<0 unbound: min of f over R>0
Ms, Es, Ls, Rs = sp.symbols("M E Lambda R", positive=True)
fmin_R = sp.solve(sp.diff(2 * (-Es) * 0 + 2 * Ms / Rs + Ls * Rs**2 / 3, Rs), Rs)[0]
fmin = sp.simplify(2 * Ms / fmin_R + Ls * fmin_R**2 / 3)
rep("C5b", sp.simplify(fmin - (3 * Ms)**sp.Rational(2, 3) * Ls**sp.Rational(1, 3)) == 0,
    "min_R (2M/R + Lambda R^2/3) = (3M)^{2/3} Lambda^{1/3}: E<0 is unbound iff 2|E| < (3M)^{2/3}Lambda^{1/3}")
Mv, Ev, Lv = 1.0, -0.1, 1.0
Rstar = (3 * Mv / Lv) ** (1 / 3)
fm = 2 * Ev + 2 * Mv / Rstar + Lv * Rstar**2 / 3
rep("C5c", fm > 0, "witness M=1,E=-0.1,Lambda=1: min R_t^2 = %.4f > 0 -> unbound with E<0" % fm)
print("     => with Lambda != 0 the contraction criterion Gamma^2>1 <=> E>0 is untouched (definition),"
      " but 'E>0 <=> unbound' is false both ways; Le Delliou-Mena-Mimoso E_lim = -(3M)^{2/3}Lambda^{1/3}"
      " in their E (=2E here) convention agrees with C5b.")

# ---------------- C6: data -- Planck 2018 Lambda and the window
c = 299792458.0; Mpc = 3.0856775814913673e22; G_N = 6.67430e-11; Msun = 1.98840987e30
def Lam_of(H0, OL):
    H = H0 * 1e3 / Mpc
    return 3 * OL * H**2 / c**2
L_pl = Lam_of(67.36, 0.6847)
L_sh = Lam_of(74.03, 0.6847)   # SH0ES R19 as quoted by Planck VI p.26, same Omega_L (illustrative)
print("C6   Lambda(Planck 2018, H0=67.36, OmL=0.6847) = %.4e m^-2 ; with H0=74.03: %.4e m^-2" % (L_pl, L_sh))
for name, Mkg in (("1 kg", 1.0), ("Earth", 5.9722e24), ("Sun", Msun), ("1e12 Msun galaxy", 1e12 * Msun)):
    Mg = G_N * Mkg / c**2
    for tag, Lx in (("Planck", L_pl), ("SH0ES", L_sh)):
        win = (3 * Mg) ** (2 / 3) * Lx ** (1 / 3)
        print("     %-18s %-7s 2|E| window below which the Lambda=0 label flips: %.3e" % (name, tag, win))
rep("C6", (3 * G_N * Msun / c**2) ** (2 / 3) * L_pl ** (1 / 3) < 1e-14,
    "solar-mass shell: Lambda>0 reclassifies only |2E| < 1e-14 -- no moved datum moves a local reading")

# ---------------- C7: non-geodesic counterexample in Minkowski
Ts, A, r0 = sp.symbols("T A r0", positive=True)
v = sp.diff(r0 + A * sp.sin(Ts), Ts)
gam = 1 / sp.sqrt(1 - v**2)
Uc, Gc = gam * v, gam                     # u = gam(1,v), n = gam(v,1) in (T,R); U = u.dR, Gamma = n.dR
mc = sp.simplify((r0 + A * sp.sin(Ts)) / 2 * (1 - (Gc**2 - Uc**2)))
Ec = sp.simplify((Gc**2 - 1) / 2)
rep("C7a", mc == 0, "Minkowski: m_MS = 0 on the oscillating family (flat vacuum)")
rep("C7b", sp.simplify(Ec - Uc**2 / 2) == 0, "E = U^2/2 = A^2 cos^2T / (2(1 - A^2 cos^2 T)) >= 0")
Ev = [float(Ec.subs({A: 0.5, Ts: x})) for x in (0.0, 0.7, 2.0, 4.0)]
rep("C7c", all(e > 0 for e in Ev), "A=0.5: E > 0 at T = 0,0.7,2,4 (%s) while R in [r0-A, r0+A] forever" %
    ", ".join("%.4f" % e for e in Ev))
print("     => off geodesic flow E>0 is an instantaneous label, not the fate.  drivensource.py:186's"
      " '<=> THE CONFIGURATION IS UNBOUND' is exact only for geodesic (p'=0, no-flux) flow with Lambda=0.")

# ---------------- C8: the owner's fixture
mz, Rz2, Uz = z3.Reals("m R2 U")
s = z3.Solver(); s.add(Rz2 > 0)
s.add(z3.Not((2 * mz / Rz2 < Uz * Uz) == ((1 + Uz * Uz - 2 * mz / Rz2 - 1) / 2 > 0)))
rep("C8a", s.check() == z3.unsat, "contracts <=> ltb_energy>0 is valid over the reals: the fixture is a tautology")
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
try:
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        import driven
    got = driven.contraction_is_unbound(0.0, 10.0, 1e-9)
    print("C8b  driven.contraction_is_unbound(0, 10, 1e-9) = %r  (contracts=%r, ltb_energy=%r)" %
          (got, driven.contracts(0.0, 10.0, 1e-9), driven.ltb_energy(0.0, 10.0, 1e-9)))
    print("     float cancellation in 0.5*((1+U^2-2m/R)-1): a DISCREPANCY in the owner's code, not in the"
          " external result; the selftest samples U in {0,0.3,1} and never meets it.")
    rep("C8b", got is False, "discrepancy reproduced (recorded, not repaired)")
    v9 = [x for x in driven.residuals() if x[0].startswith("V9")]
    if v9:
        rep("C8c", v9[0][1] == 0, "owner's V9 residual re-run: %s" % v9[0][1])
except Exception as ex:  # import is optional
    print("C8b  driven import unavailable: %r" % ex)

print("\nRESULT: %s" % ("ALL PASS" if not FAIL else "FAILED: " + ", ".join(FAIL)))
sys.exit(1 if FAIL else 0)
