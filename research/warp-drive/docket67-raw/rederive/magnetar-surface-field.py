#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for 'magnetar-surface-field' (tolman.py:1592-1593, 806-808, 59-61, 3076-3081).
Reads tolman.py READ-ONLY (import) for the bill; edits nothing.  Every external input is labelled with
where it was READ.  Exit 0 iff every assertion holds."""
import math, sys
import sympy as sp

sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import tolman  # read-only import

ok = True
def chk(label, got, want, rel=1e-3):
    global ok
    good = abs(got - want) <= rel * abs(want)
    ok &= good
    print("  %-4s %-66s got %.5e want %.5e" % ("OK" if good else "FAIL", label, got, want))
    return good

MU0 = 1.25663706212e-6            # CODATA 2018 (the tree's value, tolman.py:1125)
MU0_2022 = 1.25663706127e-6       # CODATA 2022
EPS0 = 1.0 / (MU0 * 299792458.0**2)
C = 299792458.0; QE = 1.602176634e-19; HBAR = 1.054571817e-34
REQ = abs(tolman.tension_for_contraction(0.01, 1.0))   # the bill, DERIVED in tolman.py
def Pmag(B): return B * B / (2 * MU0)
def shortfall(B): return REQ / Pmag(B)

print("[1] the tree's own arithmetic")
chk("magnetic_tension(1e11 T) = B^2/(2 mu0)  [tolman.py:3076 pins 3.9789e27]", Pmag(1e11), 3.9789e27, 1e-4)
chk("tolman.magnetic_tension agrees", tolman.magnetic_tension(1e11), Pmag(1e11), 1e-12)
chk("bill 9.7773e40 Pa [tolman.py:59, 783]", REQ, 9.7773e40, 1e-4)
chk("shortfall = bill / magnetar rung [tolman.py:3080 pins 2.4573e13]", shortfall(1e11), 2.4573e13, 1e-3)
chk("CODATA 2022 mu0 moves the rung by < 1e-9 (relative)", abs(1e22/(2*MU0_2022) - Pmag(1e11))/Pmag(1e11) + 1, 1.0, 1e-8)

print("[2] Maxwell stress along B is a TENSION of B^2/(2 mu0) (sympy, symbolic)")
B, mu = sp.symbols("B mu0", positive=True)
T = sp.Matrix(3, 3, lambda i, j: ((B if i == 2 else 0) * (B if j == 2 else 0) - (sp.Rational(1, 2) * B**2 if i == j else 0)) / mu)
ev = T.eigenvals()
print("     Maxwell stress eigenvalues (sigma_ij = (B_iB_j - d_ij B^2/2)/mu0):", ev)
along = sp.simplify(T[2, 2]); perp = sp.simplify(T[0, 0])
good = sp.simplify(along - B**2 / (2 * mu)) == 0 and sp.simplify(perp + B**2 / (2 * mu)) == 0
ok &= bool(good); print("  %-4s along B: +B^2/(2mu0) (tension), across B: -B^2/(2mu0) (pressure)" % ("OK" if good else "FAIL"))
Ttr = sp.simplify(sum(T[i, i] for i in range(3)) + B**2/(2*mu))   # 4D trace: -rho + sum sigma_ii with rho=B^2/2mu0 ... T^mu_mu = -rho + sum p_i
tr4 = sp.simplify(-B**2/(2*mu) - sum(-T[i, i] for i in range(3)))  # p_i = -sigma_ii
good = sp.simplify(-B**2/(2*mu) + sum(-T[i, i] for i in range(3))) == 0  # T^mu_mu = -rho + sum p_i with p_i=-sigma_ii
ok &= bool(good); print("  %-4s EM field is traceless: -rho + sum p_i = 0 (so the rung is inside tolman's traceless hypothesis)" % ("OK" if good else "FAIL"))

print("[3] the spin-down coefficient 3.2e19 G (Olausen & Kaspi 2014, arXiv:1309.4167 p.2) -- sympy")
I_, R_, c_, P_, Pd_, a_ = sp.symbols("I R c P Pdot alpha", positive=True)
# vacuum orthogonal rotator: L = (2/3) mu^2 Omega^4 sin^2a / c^3 = I Omega |Omegadot|; Omega = 2pi/P, |Omegadot| = 2pi Pdot/P^2; B_eq = mu/R^3
mu2_vac = sp.solve(sp.Eq(sp.Rational(2, 3) * sp.Symbol("m2") * (2*sp.pi/P_)**4 * sp.sin(a_)**2 / c_**3,
                         I_ * (2*sp.pi/P_) * 2*sp.pi*Pd_/P_**2), sp.Symbol("m2"))[0]
Beq_vac = sp.sqrt(mu2_vac.subs(a_, sp.pi/2)) / R_**3
coef = sp.simplify(Beq_vac / sp.sqrt(P_ * Pd_))
coef_num = float(coef.subs({I_: 1e45, R_: 1e6, c_: 2.99792458e10}))
print("     B_eq = sqrt(3 c^3 I P Pdot / (8 pi^2 R^6)); coefficient =", sp.simplify(coef))
chk("coefficient with I=1e45 g cm^2, R=10 km (cgs) -> 3.2e19 G", coef_num, 3.2e19, 1e-2)
# force-free (Spitkovsky 2006, named in 2405.15484 ref [48]; NAMED-NOT-READ): L = mu^2 Omega^4 (1+sin^2a)/c^3
mu2_ff = sp.solve(sp.Eq(sp.Symbol("m2") * (2*sp.pi/P_)**4 * (1 + sp.sin(a_)**2) / c_**3,
                        I_ * (2*sp.pi/P_) * 2*sp.pi*Pd_/P_**2), sp.Symbol("m2"))[0]
r_orth = float(sp.sqrt(mu2_ff.subs(a_, sp.pi/2) / mu2_vac.subs(a_, sp.pi/2)))
r_align = float(sp.sqrt(mu2_ff.subs(a_, 0) / mu2_vac.subs(a_, sp.pi/2)))
chk("force-free / vacuum-orthogonal B, orthogonal rotator = 1/sqrt(3)", r_orth, 1/math.sqrt(3), 1e-9)
chk("force-free (aligned) / vacuum-orthogonal B = sqrt(2/3)", r_align, math.sqrt(2/3), 1e-9)

print("[4] the catalogue values, recomputed from READ P, Pdot (Olausen & Kaspi 2014 Table 2, p.18)")
cat = {"SGR 1806-20": (7.547728, 49.5e-11, 20e14), "1E 1841-045": (11.782898, 3.93e-11, 6.9e14),
       "SGR 1900+14": (5.19987, 9.2e-11, 7.0e14), "SGR 0418+5729": (9.07838822, 0.0004e-11, 0.061e14)}
Bcat = {}
for k, (P, Pd, Btab) in cat.items():
    Bg = 3.2e19 * math.sqrt(P * Pd); Bcat[k] = Bg
    chk("%s  B = 3.2e19 sqrt(P Pdot) G vs table" % k, Bg, Btab, 0.03)
Bmax_T = Bcat["SGR 1806-20"] * 1e-4
print("     catalogue maximum: SGR 1806-20, %.3e G = %.3e T  (tree uses 1.0e11 T)" % (Bcat["SGR 1806-20"], Bmax_T))


print("[4b] radius / moment-of-inertia hypothesis: B ∝ I^(1/2) R^(-3) (from the sympy coefficient above)")
fR = (12.0/10.0)**-3
print("     R = 12 km (Tiengo+13's value, READ) instead of 10 km, I fixed: B x %.3f, rung x %.3f, shortfall x %.2f" % (fR, fR**2, fR**-2))
chk("R=12 km scale factor on B", fR, 0.5787, 1e-3)

print("[5] the shortfall across what the magnetar inference itself allows (each a NAMED hypothesis)")
rows = [
 ("tree: 1e11 T (round)", 1e11),
 ("Kouveliotou+98 wind-corrected SGR1806-20, 2e14 G", 2e10),
 ("Kouveliotou+98 vacuum SGR1806-20, 8e14 G", 8e10),
 ("catalogue max SGR1806-20 equatorial vacuum", Bmax_T),
 ("same, force-free orthogonal (x1/sqrt3)", Bmax_T / math.sqrt(3)),
 ("same, polar (x2) vacuum", 2 * Bmax_T),
 ("Tiengo+13 SGR0418 proton-cyclotron local, >1e15 G", 1e11),
 ("Tiengo+13 model loop base B_max 7.41e15 G", 7.41e11),
]
for lab, Bt in rows:
    print("     %-52s B=%.3e T  P=%.3e Pa  shortfall=%.3e" % (lab, Bt, Pmag(Bt), shortfall(Bt)))
lo = min(shortfall(b) for _, b in rows); hi = max(shortfall(b) for _, b in rows)
print("     magnetar-class shortfall spans %.2e .. %.2e (factor %.0f); every value >> 1" % (lo, hi, hi/lo))
ok &= lo > 1e11

print("[6] EM (traceless) fields stronger than the magnetar rung -- the tree's 'best in-hypothesis tension known'")
MPI = 139.57039e6 * QE   # J
B_mpi2 = MPI**2 / (QE * HBAR * C**2)    # eB = m_pi^2 in SI
chk("eB = m_pi^2  ->  B = 3.29e14 T (SI, computed)", B_mpi2, 3.29e14, 3e-3)
print("     Skokov+09 (0907.1396 p.5) write m_pi^2 = 140^2 x 0.512e14 G ~ 1e18 G; computed SI/Gaussian value is %.3e G"
      % (B_mpi2 * 1e4))
print("     -> a conversion DISCREPANCY of factor %.2f in the paper's footnote (recorded, not a refutation)" % (B_mpi2*1e4/(140**2*0.512e14)))
for lab, nmpi in (("RHIC Au+Au 200 GeV, eB ~ m_pi^2 (Skokov+09 UrQMD)", 1.0),
                  ("RHIC, eB ~ 3 m_pi^2 (Kharzeev-McLerran-Warringa, as restated by Skokov+09)", 3.0),
                  ("LHC Pb+Pb, eB ~ 15 m_pi^2 (Skokov+09 lower bound of maximum)", 15.0)):
    for conv, Bt in (("SI", nmpi * B_mpi2), ("paper's 1e18 G/m_pi^2", nmpi * 1e14)):
        print("     %-74s [%s] B=%.2e T  P=%.2e Pa  shortfall=%.2e  (x%.1e over magnetar rung)"
              % (lab, conv, Bt, Pmag(Bt), shortfall(Bt), Pmag(Bt)/Pmag(1e11)))
# static nuclear Coulomb field, Pb-208: uniform-sphere radius from rms charge radius 5.5012 fm (Angeli & Marinova 2013, NAMED-NOT-READ)
Rrms = 5.5012e-15; Ru = math.sqrt(5/3) * Rrms; Z = 82
E = Z * QE / (4 * math.pi * EPS0 * Ru**2)
Pcoul = EPS0 * E**2 / 2
print("     Pb-208 surface Coulomb field (static, radial, regular centre): R_u=%.3f fm E=%.3e V/m  eps0 E^2/2 = %.3e Pa"
      % (Ru*1e15, E, Pcoul))
print("       = %.1e x magnetar rung; shortfall would be %.2e" % (Pcoul/Pmag(1e11), REQ/Pcoul))
chk("Pb-208 surface Coulomb stress ~ 2.4e31 Pa", Pcoul, 2.4e31, 0.05)
print("     every one of these still leaves a shortfall >> 1 against the 1 m bill; none is macroscopic.")
ok &= REQ / Pmag(15*B_mpi2) > 1e3

print("RESULT:", "ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
