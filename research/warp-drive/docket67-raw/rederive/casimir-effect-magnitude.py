#!/usr/bin/env python3
"""DOCKET 67 -- rederivation for key casimir-effect-magnitude.

The tree's claim (phase1.py:403-404, figure from gjw.py:80-90, 115-128):
  "Casimir corridor ... reusable but the magnitude is 4.39e71 short at metre scale (gjw.py)"
gjw.py: |rho| = pi^2 hbar c / (90 (2D)^4) on a cycle of length 2D, against
seatindex.tkk_required(D) = pi c^4/(4 G D^2); gain = 4.387e71 D^2.

Checks (read-only; nothing under research/ is written):
 A  zeta/dim-reg mode sum: periodic massless scalar, rho = -pi^2/(90 L^4)   (sympy, exact)
 B  independent image sum: full <T_mu nu> = (pi^2/90L^4) diag(-1,1,1,-3)    (sympy, exact)
    -> matches Fewster-Olum-Pfenning gr-qc/0609007 eq.(24), Kuo-Ford gr-qc/9304008 eq.(3.33)
    -> T_kk along the winding direction = -4 pi^2/(90 L^4); transverse null = 0
 C  consistency: periodic(2a) = Dirichlet(a) + Neumann(a);  plates EM pi^2/720 = 2 x scalar Dirichlet
 D  the tree's numbers re-computed; closed form gain = 360 D^2/(pi l_P^2)
 E  data: CODATA 2022 (scipy 1.17.1 table) vs tree constants; G moves nothing
 F  model-hypothesis sensitivities: T_kk vs rho (x4), EM (x2), plate conflation, MMP cycle length
 G  MMP 1807.04726 eqs (5.24)-(5.31) re-derived: 2D Casimir, anomaly cancellation, l and E_min
 H  Butcher 1405.1283 eq.(68): two-length scaling a^2 = l_p^2 (L/a) ln(a/a0)/(360 pi) -- escape
    from the single-length Planck landing, evaluated
Exit 0 iff every check passes.
"""
import math, sys, json
import sympy as sp

ok = True
out = {}
def chk(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("   " + detail if detail else ""))

# ------------------------------------------------------------------ A
s, L, m, a = sp.symbols('s L m a', positive=True)
n = sp.symbols('n', integer=True, positive=True)
# dimensional-regularisation transverse integral: INT d^2k/(2pi)^2 (k^2+m^2)^(1/2)
#  = (1/(4pi)) Gamma(-1/2 - 1 + ... )  general: INT d^dk/(2pi)^d (k^2+m^2)^(-s) = Gamma(s-d/2)/((4pi)^(d/2) Gamma(s)) m^(d-2s)
d = 2
I_trans = sp.gamma(sp.Rational(-1, 2) - sp.Rational(d, 2)) / ((4*sp.pi)**sp.Rational(d, 2) * sp.gamma(sp.Rational(-1, 2))) * m**(d + 1)
I_trans = sp.simplify(I_trans)
chk("A1 transverse integral = -m^3/(6 pi)", sp.simplify(I_trans + m**3/(6*sp.pi)) == 0, str(I_trans))
# E/A = (1/2) sum_{n in Z} I_trans(m = 2 pi |n| / L), n=0 term zero; sum n^3 -> zeta(-3) = 1/120
E_per_A = sp.Rational(1, 2) * 2 * (I_trans.subs(m, 2*sp.pi/L)) * sp.zeta(-3)
rho_A = sp.simplify(E_per_A / L)
chk("A2 periodic scalar rho = -pi^2/(90 L^4)", sp.simplify(rho_A + sp.pi**2/(90*L**4)) == 0, str(rho_A))

# ------------------------------------------------------------------ B  image sum
t, x, y, z, tp, xp, yp, zp = sp.symbols("t x y z tp xp yp zp", real=True)
def G_image(k):
    # Minkowski Wightman fn (spacelike separation) 1/(4 pi^2 sigma2), image displaced k L in z
    s2 = -(t - tp)**2 + (x - xp)**2 + (y - yp)**2 + (z - zp + k*L)**2
    return 1/(4*sp.pi**2*s2)
k = sp.symbols('k', integer=True, nonzero=True)
Gk = G_image(k)
coinc = {tp: t, xp: x, yp: y, zp: z}
def dd(u, v):
    return sp.simplify(sp.diff(Gk, u, v).subs(coinc))
# minimal coupling, flat, <phi^2> constant => T_mn = <d_m phi d_n phi> - 1/2 eta_mn <d phi.d phi>
# <d_m phi d_n phi> = lim d_m d_n' G  (symmetrised)
coords = [(t, tp), (x, xp), (y, yp), (z, zp)]
eta = sp.diag(-1, 1, 1, 1)
DD = sp.zeros(4, 4)
for i, (u, up) in enumerate(coords):
    for j, (v, vp) in enumerate(coords):
        DD[i, j] = dd(u, vp)
trace = sum(eta[i, i]*DD[i, i] for i in range(4))
T = sp.zeros(4, 4)
for i in range(4):
    for j in range(4):
        T[i, j] = sp.simplify(DD[i, j] - sp.Rational(1, 2)*eta[i, j]*trace)
# sum over k != 0: each entry ~ c/(k^4 L^4); sum_{k!=0} 1/k^4 = 2 zeta(4)
Tsum = T.applyfunc(lambda e: sp.simplify(sp.simplify(e * k**4 * L**4) * 2*sp.zeta(4) / L**4))
target = sp.pi**2/(90*L**4) * sp.diag(-1, 1, 1, -3)
chk("B1 <T_mn> = (pi^2/90L^4) diag(-1,1,1,-3)  [FOP gr-qc/0609007 eq.24]",
    sp.simplify(Tsum - target) == sp.zeros(4, 4), str([sp.simplify(Tsum[i, i]*L**4) for i in range(4)]))
T00 = Tsum[0, 0]
chk("B2 T_00 = -pi^2/(90 L^4)  [Kuo-Ford gr-qc/9304008 eq.3.33]", sp.simplify(T00 + sp.pi**2/(90*L**4)) == 0)
Tkk_wind = sp.simplify(Tsum[0, 0] + Tsum[3, 3] + 2*Tsum[0, 3])
Tkk_perp = sp.simplify(Tsum[0, 0] + Tsum[1, 1] + 2*Tsum[0, 1])
chk("B3 T_kk along winding null k=(1,0,0,1): -4 pi^2/(90 L^4) = 4 x rho", sp.simplify(Tkk_wind - 4*T00) == 0, str(Tkk_wind))
chk("B4 T_kk along transverse null k=(1,1,0,0): 0 (ANEC holds, FOP p.10)", Tkk_perp == 0)
chk("B5 traceless", sp.simplify(sum(eta[i, i]*Tsum[i, i] for i in range(4))) == 0)

# ------------------------------------------------------------------ C
rho_D_scalar = -sp.pi**2/(1440*a**4)   # Dirichlet scalar between plates (energy density, conformal)
rho_EM_plates = -sp.pi**2/(720*a**4)
per_area_periodic_2a = rho_A.subs(L, 2*a) * 2*a
chk("C1 periodic(2a) per area = Dirichlet(a)+Neumann(a) = 2 x (-pi^2/(1440 a^3))",
    sp.simplify(per_area_periodic_2a - 2*rho_D_scalar*a) == 0)
chk("C2 EM plates pi^2/720 = 2 x scalar-Dirichlet pi^2/1440", sp.simplify(rho_EM_plates - 2*rho_D_scalar) == 0)
chk("C3 gjw.py's cycle(2D) density = scalar-Dirichlet plates at D = (1/2) x EM plates at D",
    sp.simplify(rho_A.subs(L, 2*a) - rho_D_scalar) == 0)

# ------------------------------------------------------------------ D  tree numbers
HBAR_TREE = 1.054571817e-34; C = 299792458.0; G_TREE = 6.67430e-11; LP_TREE = 1.616255e-35
HBAR_C = HBAR_TREE*C
cas = lambda D: math.pi**2*HBAR_C/(90.0*(2.0*D)**4)
T_COEFF = math.pi*C**4/(4.0*G_TREE)
need = lambda D: T_COEFF/D**2
gain = lambda D: need(D)/cas(D)
chk("D1 casimir_cycle(1 m) = 2.167e-28 Pa (gjw.py:84)", abs(cas(1.0)/2.167e-28 - 1) < 5e-4, "%.4e" % cas(1.0))
chk("D2 tkk_required(1 m) = 9.505e43 Pa (gjw.py:84)", abs(need(1.0)/9.505e43 - 1) < 5e-4, "%.4e" % need(1.0))
chk("D3 gain(1 m) = 4.3866e71 (gjw.py:195; phase1.py:404 '4.39e71')", abs(gain(1.0)/4.3866e71 - 1) < 1e-4, "%.5e" % gain(1.0))
Dm, hb, cc, GG = sp.symbols('D hbar c G', positive=True)
gain_sym = sp.simplify((sp.pi*cc**4/(4*GG*Dm**2)) / (sp.pi**2*hb*cc/(90*(2*Dm)**4)))
chk("D4 closed form gain = 360 c^3 D^2/(pi G hbar) = 360 D^2/(pi l_P^2)",
    sp.simplify(gain_sym - 360*cc**3*Dm**2/(sp.pi*GG*hb)) == 0, str(gain_sym))
lp_tree = math.sqrt(HBAR_TREE*G_TREE/C**3)
chk("D5 360/(pi l_P^2) numerically = 4.3866e71", abs(360/(math.pi*lp_tree**2)/gain(1.0) - 1) < 1e-12)
u = math.sqrt(1.0/(360/(math.pi*lp_tree**2)))
chk("D6 unity separation = sqrt(pi/360) l_P = 0.0934 l_P (gjw.py:93)", abs(u/lp_tree - math.sqrt(math.pi/360)) < 1e-12,
    "%.4e m = %.4f l_P" % (u, u/lp_tree))
chk("D7 D^2 scaling exact", abs(gain(1e6)/gain(1.0) - 1e12) < 1e-3)
out["gain_1m_tree"] = gain(1.0)

# ------------------------------------------------------------------ E  data
try:
    import scipy.constants as spc, scipy
    G22 = spc.physical_constants['Newtonian constant of gravitation']
    hb22 = spc.physical_constants['reduced Planck constant'][0]
    lp22 = spc.physical_constants['Planck length'][0]
    g22 = 360/(math.pi*(hb22*G22[0]/C**3))
    print("     CODATA 2022 via scipy %s: G = %.5e +- %.1e ; hbar = %.16e ; l_P = %.6e"
          % (scipy.__version__, G22[0], G22[2], hb22, lp22))
    chk("E1 gain(1 m) with CODATA 2022 equals tree's to < 1e-8", abs(g22/gain(1.0) - 1) < 1e-8, "%.6e" % g22)
    chk("E2 G 1-sigma (22 ppm) moves gain by 22 ppm -- no conclusion moves", G22[2]/G22[0] < 3e-5,
        "rel %.2e" % (G22[2]/G22[0]))
    G14 = 6.67408e-11  # CODATA 2014 value, for the 'moved datum' row
    chk("E3 CODATA 2014 -> 2022 G shift moves gain by 3.3e-5 relative", abs((G22[0]/G14) - 1) < 4e-5,
        "%.2e" % (G22[0]/G14 - 1))
    out["gain_1m_codata2022"] = g22
except Exception as e:
    chk("E scipy CODATA table available", False, repr(e))

# ------------------------------------------------------------------ F  sensitivities
g_tkk = gain(1.0)/4.0
g_em = gain(1.0)/2.0
g_em_tkk = gain(1.0)/8.0
plate_1m = math.pi**2*HBAR_C/(720.0*1.0**4)
g_plate = need(1.0)/plate_1m
g_mmp_len = gain(1.0)*((1 + 2.35)/2.0)**4
print("     T_kk (winding) instead of rho:             gain(1 m) = %.4e" % g_tkk)
print("     EM field (2 dof) instead of one scalar:     gain(1 m) = %.4e" % g_em)
print("     EM + T_kk:                                  gain(1 m) = %.4e" % g_em_tkk)
print("     phase1 'Casimir corridor' = plates pi^2/720 at d = 1 m: gain = %.4e" % g_plate)
print("     cycle = d + pi*l with pi*l = 2.35 d (MMP Fig.7 large-d slope): gain = %.4e" % g_mmp_len)
chk("F1 every variant stays within [1e70, 1e73] -- 'about 1e71 short' survives each named variant",
    all(1e70 < g < 1e73 for g in (g_tkk, g_em, g_em_tkk, g_plate, g_mmp_len)))
chk("F2 T_kk correction is a factor-4 discrepancy, not a refutation", abs(gain(1.0)/g_tkk - 4) < 1e-12)
out.update(g_tkk=g_tkk, g_em=g_em, g_em_tkk=g_em_tkk, g_plate=g_plate, g_mmp_len=g_mmp_len)

# ------------------------------------------------------------------ G  MMP eqs 5.24-5.31
q, ell, re, GN = sp.symbols('q ell r_e G_N', positive=True)
Lc = sp.pi*ell
E_cyl = -q/12 * 2*sp.pi/Lc             # (5.24)
chk("G1 MMP (5.24): -q/12 * 2pi/L at L = pi l equals -q/(6 l)", sp.simplify(E_cyl + q/(6*ell)) == 0)
# 2D Dirac fermion, antiperiodic: E0 = -(2pi/L) * sum_{n in Z}|n+1/2|  (zeta-regularised) = -(2pi/L)*2*zeta(-1,1/2)
hz = sp.zeta(-1, sp.Rational(1, 2))
chk("G2 per-field 2D antiperiodic Dirac Casimir = -(1/12)(2pi/L)  [2 zeta_H(-1,1/2) = 1/12]",
    sp.simplify(2*hz - sp.Rational(1, 12)) == 0, "zeta_H(-1,1/2) = %s" % hz)
E_strip = -q/24 * sp.pi/Lc             # (5.25), cancelled by the anomaly
E_tot = sp.simplify(E_cyl - E_strip)
chk("G3 total = cylinder - strip = -q/(8 l)  (the -q/8l of MMP 5.30)", sp.simplify(E_tot + q/(8*ell)) == 0)
Evar = re**3/(GN*ell**2) + E_tot
lsol = sp.solve(sp.diff(Evar, ell), ell)
chk("G4 MMP (5.31): l = 16 r_e^3/(G_N q)", len(lsol) == 1 and sp.simplify(lsol[0] - 16*re**3/(GN*q)) == 0, str(lsol))
Emin = sp.simplify(Evar.subs(ell, lsol[0]))
chk("G5 MMP (5.31): E_min = -G_N q^2/(256 r_e^3)", sp.simplify(Emin + GN*q**2/(256*re**3)) == 0, str(Emin))
# the scaling contrast: MMP's source is q two-dimensional fields, energy ~ q/L (1D length), not ~ A L^-3
q_1m = (1.0/LP_TREE)**(1.0/3.0)
d_ew = HBAR_C/(1.0e12*1.602176634e-19)   # hbar c / 1 TeV, MMP p.5 'smaller than the electroweak scale'
print("     MMP p.24: N_f=1 analysis covers d < q^3 l_p; d = 1 m needs q > %.3e (parametric, NOT computed by MMP)" % q_1m)
print("     MMP p.5 SM embedding: d < electroweak length ~ hbar c/TeV = %.3e m; 1 m exceeds it by %.2e" % (d_ew, 1.0/d_ew))
e_compton = 2.42631023538e-12/(2*math.pi)
print("     lightest charged SM fermion (electron) reduced Compton length %.3e m << 1 m: no massless charged SM fermion at metre scale" % e_compton)
chk("G6 MMP's SM-embedded construction does not reach metre separation (d_ew < 1e-18 m)", d_ew < 1e-18)
out.update(mmp_q_for_1m=q_1m, mmp_d_ew=d_ew)
print("     MMP stress (5.27): T_tt = -q/(8 pi l^2) * 1/(4 pi r_e^2): ~ q/(l^2 r_e^2), two lengths, x q")

# ------------------------------------------------------------------ H  Butcher 2014 eq.(68)
# a^2 = l_p^2 (L/a) ln(a/a0) / (360 pi)  -> for given a, required throat length L = 360 pi a^3/(l_p^2 ln(a/a0))
lp = lp_tree
def L_needed(a_m, ln_fac=1.0):
    return 360*math.pi*a_m**3/(lp**2*ln_fac)
for a_m in (1e-15, 1e-10, 1e-6):
    print("     Butcher eq.68 (ln factor 1): throat radius a = %.0e m needs length L = %.3e m" % (a_m, L_needed(a_m)))
a_1m = (lp**2*1.0/(360*math.pi))**(1.0/3.0)   # throat radius for L = 1 m, ln factor 1
print("     Butcher eq.68 inverted (ln factor 1): throat length L = 1 m allows radius a = %.3e m = %.3e l_P" % (a_1m, a_1m/lp))
out.update(butcher_L_for_a_1fm=L_needed(1e-15), butcher_a_for_L_1m=a_1m)
chk("H1 two-length escape from the single-length Planck landing is real but small: L = 1 m gives a >> l_P (1e10 l_P) yet a < 1e-18 m",
    a_1m/lp > 1e9 and a_1m < 1e-18)
chk("H2 a nuclear-size throat (1 fm) needs L = 4.3e27 m, beyond the Hubble radius (~1.4e26 m): 'macroscopic in principle' is not metre-scale",
    L_needed(1e-15) > 1.4e26)
# NOTE (recorded, not repaired): the first version of H1 expected L(1 fm) ~ 4e24 m; that was this
# script's author's guess, and the computation returned 4.329e27 m. The check was re-stated to the computed value.
print("     (Butcher: magnitude sufficient 'in principle', but T_kk = 0 for null rays parallel to the throat,")
print("      so the static wormhole is NOT stabilised -- sec. IV A. Recorded, not extrapolated.)")

print("\nRESULT:", "ALL PASS" if ok else "SOME FAIL")
print(json.dumps(out, indent=1))
sys.exit(0 if ok else 1)
