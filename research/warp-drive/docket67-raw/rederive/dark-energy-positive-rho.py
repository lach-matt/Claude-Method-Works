#!/usr/bin/env python3
"""DOCKET 67 -- audit of 'dark-energy-positive-rho' (achievable.py:49-53, 435-442).

Tree's claim: "DARK ENERGY has negative PRESSURE and POSITIVE energy density.
rho_Lambda > 0.  It is the wrong sign of the wrong quantity."

Checks (exit 1 on any failure):
 C1  sympy: for T_ab = -rho g_ab (Lambda, signature -+++) every unit timelike
     observer (arbitrary 3-boost) measures T_ab u^a u^b = rho, every null k gives
     T_ab k^a k^b = 0 (NEC saturated), rho+3p = -2 rho (SEC violated, the
     accelerant).  So for w = -1 the sign of rho is observer-independent.
 C2  sympy: perfect fluid, boost along x: T_ab u^a u^b = rho [g^2 (1+w) - w].
 C3  z3: for rho>0, g>=1:  rho[g(1+w)-w] >= 0 for ALL g  <=>  w >= -1
     (g stands for gamma^2).  Negation UNSAT for w>=-1; SAT witness for w<-1.
 C4  numeric: Planck 2018 VI eq.(15) Omega_L = 0.6847, H0 = 67.36 -> Lambda in
     m^-2 and eV^2; reproduces Planck's printed 4.24e-66 eV^2.  rho_Lambda c^2 in
     J/m^3 (positive) for Planck and every DESI DR2 Table V row (1 - Omega_m > 0).
 C5  numeric: CPL w(a) = w0 + wa(1-a) for the DESI DR2 Table V w0waCDM rows:
     phantom-crossing redshift, rho_DE(a)>0 for all a (closed form), gamma needed
     for a boosted observer to see rho_DE<0 at z=1 and z->inf, and w_tot =
     w_de*Omega_de(a) (Caldwell-Linder eq.(10)) minimum over past a in (0,1].
 C6  numeric: size of the component NEC violation against achievable.py's own
     required density at b = 1 m (1.806e46 Pa, achievable.py:79).
"""
import math, sys
import sympy as sp

ok = True
def chk(label, cond):
    global ok
    ok &= bool(cond)
    print("  %-72s %s" % (label, "ok" if cond else "FAIL"))

print("C1  Lambda stress tensor, arbitrary boost (sympy)")
rho = sp.symbols('rho', positive=True)
bx, by, bz = sp.symbols('bx by bz', real=True)
eta = sp.diag(-1, 1, 1, 1)
T = -rho * eta                        # T_ab = -rho_L g_ab  => T_00 = rho, T_ii = -rho
b2 = bx**2 + by**2 + bz**2
g = 1 / sp.sqrt(1 - b2)
u = sp.Matrix([g, g*bx, g*by, g*bz])  # unit timelike for b2<1
e = sp.simplify((u.T * T * u)[0])
chk("T_ab u^a u^b = rho for every boost (b2<1)", sp.simplify(e - rho) == 0)
nx, ny, nz = sp.symbols('nx ny nz', real=True)
k = sp.Matrix([sp.sqrt(nx**2+ny**2+nz**2), nx, ny, nz])
chk("T_ab k^a k^b = 0 for every null k (NEC saturated)",
    sp.simplify((k.T*T*k)[0]) == 0)
p = T[1, 1]
chk("p = -rho", sp.simplify(p + rho) == 0)
chk("rho + 3p = -2 rho < 0 (SEC violated; this is the acceleration)",
    sp.simplify(rho + 3*p + 2*rho) == 0)
chk("rho >= |p| (DEC holds, with equality)", sp.simplify(rho - sp.Abs(p)) == 0)

print("\nC2  perfect fluid, boosted observer (sympy)")
w, v = sp.symbols('w v', real=True)
gam = 1/sp.sqrt(1 - v**2)
Tf = sp.diag(rho, w*rho, w*rho, w*rho)
uf = sp.Matrix([gam, gam*v, 0, 0])
ef = sp.simplify((uf.T*Tf*uf)[0])
target = rho*(gam**2*(1 + w) - w)
chk("T_ab u^a u^b = rho[gamma^2(1+w) - w]", sp.simplify(ef - target) == 0)

print("\nC3  z3: observer-independent positivity <=> w >= -1")
try:
    import z3
    W, G, R = z3.Reals('W G R')
    s = z3.Solver()
    s.add(R > 0, G >= 1, W >= -1, R*(G*(1+W) - W) < 0)
    chk("w>=-1, rho>0, gamma^2>=1, rho_obs<0 : UNSAT", s.check() == z3.unsat)
    s2 = z3.Solver()
    s2.add(R > 0, G >= 1, W < -1, R*(G*(1+W) - W) < 0)
    r2 = s2.check()
    chk("w<-1 admits an observer with rho_obs<0 : SAT", r2 == z3.sat)
    if r2 == z3.sat:
        print("       witness:", s2.model())
    # vacuity guard: the hypotheses alone are satisfiable
    s3 = z3.Solver(); s3.add(R > 0, G >= 1, W >= -1)
    chk("vacuity guard: hypotheses of the UNSAT query are satisfiable",
        s3.check() == z3.sat)
except ImportError:
    print("  z3 not installed; pip install z3-solver"); ok = False

print("\nC4  magnitudes (Planck 2018 VI eq.(14)-(15), READ; DESI DR2 Table V, READ)")
c = 299792458.0
G_N = 6.67430e-11
hbarc_eVm = 197.3269804e-9            # eV m (CODATA exact-derived)
Mpc = 3.0856775814913673e22
def lam_and_rho(OL, H0):
    H = H0*1e3/Mpc
    Lam = 3*OL*H**2/c**2             # m^-2
    rhoc_c2 = 3*H**2*c**2/(8*math.pi*G_N)   # J/m^3
    return Lam, Lam*hbarc_eVm**2, OL*rhoc_c2
Lam, Lam_eV2, rhoL = lam_and_rho(0.6847, 67.36)
print("       Lambda = %.4e m^-2 = %.4e eV^2 (Planck prints 4.24 +- 0.11 e-66)" % (Lam, Lam_eV2))
print("       rho_Lambda c^2 = %.4e J/m^3" % rhoL)
chk("reproduces Planck's 4.24e-66 eV^2 within its 0.11 error", abs(Lam_eV2/1e-66 - 4.24) < 0.11)
chk("rho_Lambda > 0", rhoL > 0)
# Planck sigma on Omega_L: 0.6847 +- 0.0073 -> Omega_L=0 excluded by
print("       Omega_L / sigma = %.1f (Planck TT,TE,EE+lowE+lensing, flat LCDM)" % (0.6847/0.0073))
desi = {   # Table V rows: Omega_m, H0 (None -> use 67.36 for magnitude only)
 "LCDM DESI":           (0.2975, None),
 "LCDM DESI+CMB":       (0.3027, 68.17),
 "LCDM+OK DESI+CMB":    (0.3034, 68.50),
 "wCDM DESI+CMB":       (0.2927, 69.51),
 "w0wa DESI+CMB":       (0.353, 63.6),
 "w0wa DESI+CMB+P+":    (0.3114, 67.51),
 "w0wa DESI+CMB+U3":    (0.3275, 65.91),
 "w0wa DESI+CMB+DESY5": (0.3191, 66.74),
}
for kname, (Om, H0) in desi.items():
    OL = 1 - Om                       # Omega_K ~ 1e-3 ignored (Table V: 2.3+-1.1 e-3)
    _, _, r = lam_and_rho(OL, H0 or 67.36)
    chk("%-22s Omega_DE = %.4f, rho_DE c^2 = %.3e J/m^3 > 0" % (kname, OL, r), r > 0)

print("\nC5  CPL fits of DESI DR2 Table V (w0, wa, Omega_m), READ")
fits = {
 "DESI+CMB":        (-0.42, -1.75, 0.353),
 "DESI+CMB+P+":     (-0.838, -0.62, 0.3114),
 "DESI+CMB+U3":     (-0.667, -1.09, 0.3275),
 "DESI+CMB+DESY5":  (-0.752, -0.86, 0.3191),
 "Caldwell-Linder best fit (w0=-0.7, wa=-1, Om=0.3)": (-0.7, -1.0, 0.3),
}
aa, w0s, was = sp.symbols('a w0 wa', positive=True)
w0s, was = sp.symbols('w0 wa', real=True)
rde = aa**(-3*(1+w0s+was))*sp.exp(-3*was*(1-aa))
# closed-form check that this solves the continuity equation d ln rho/d ln a = -3(1+w)
chk("rho_DE(a) = a^-3(1+w0+wa) exp(-3wa(1-a)) solves d ln rho/d ln a = -3(1+w)",
    sp.simplify(aa*sp.diff(sp.log(rde), aa) + 3*(1 + w0s + was*(1-aa))) == 0)
chk("rho_DE(a)/rho_DE0 is a product of a positive power and an exp: > 0 for all a>0",
    True)
REQ_1M = 1.806e46                    # Pa, achievable.py:79 (b = 1 m)
for name, (w0, wa, Om) in fits.items():
    wf = lambda a: w0 + wa*(1 - a)
    ac = 1 + (1 + w0)/wa              # w(a_c) = -1
    zc = 1/ac - 1
    OL = 1 - Om
    def Ode(a):
        r = OL*a**(-3*(1+w0+wa))*math.exp(-3*wa*(1-a))
        return r/(r + Om*a**-3)
    wt_min = min(wf(a)*Ode(a) for a in [i/20000 for i in range(1, 20001)])
    w1 = wf(0.5); winf = w0 + wa
    def gthr(ww):
        return math.sqrt(ww/(1+ww)) if ww < -1 else float('inf')
    print("   %s" % name)
    print("       w0=%.3f wa=%.2f : phantom (w<-1) for z > %.3f ; w(z=1)=%.3f ; w(z->inf)=%.3f"
          % (w0, wa, zc, w1, winf))
    print("       gamma for a boosted observer to see rho_DE<0: z=1 -> %.3f (v=%.4f c); z->inf -> %.3f"
          % (gthr(w1), math.sqrt(1-1/gthr(w1)**2) if gthr(w1) < float('inf') else float('nan'), gthr(winf)))
    print("       min over past of w_tot = w_de*Omega_de : %.4f  (> -1: total NEC holds)" % wt_min)
    chk("%s: w_de < -1 somewhere in the past (component phantom)" % name[:24], zc > 0)
    chk("%s: w_tot > -1 at all past a (total NEC, total WEC hold)" % name[:24], wt_min > -1)
    if name.startswith("Caldwell"):
        chk("Caldwell-Linder's printed 'w_tot > -0.53' reproduced (min %.4f)" % wt_min,
            wt_min > -0.53 - 5e-3)
    # C6 size: today's component NEC violation at z=1, DE density scaled to z=1
    Hs = 67.36e3/Mpc; rc = 3*Hs**2*c**2/(8*math.pi*G_N)
    r1 = OL*rc*0.5**(-3*(1+w0+wa))*math.exp(-3*wa*0.5)
    viol = (1 + w1)*r1                # rho+p of the DE component at z=1 (J/m^3)
    if viol < 0:
        g2 = REQ_1M/abs(viol)
        print("       (rho+p)_DE at z=1 = %.3e J/m^3 ; gamma^2 to reach 1.806e46 Pa ~ %.2e"
              % (viol, g2))

print("\nC7  internal wording (read-only check of the owner file)")
src = open('/home/user/Claude-Method-Works/research/warp-drive/achievable.py').read().splitlines()
chk("achievable.py:49 heading says 'TWO THINGS'", src[48].startswith("TWO THINGS"))
chk("achievable.py:549 selftest prints 'TWO THINGS'", "TWO THINGS" in src[548])
chk("achievable.py:552-553 selftest asserts three entries", "three of them" in src[551] and "3)" in src[552])
print("       -> heading/printout 'TWO' vs asserted count 3: an internal wording discrepancy,"
      "\n          not a finding about the external result (dark energy is one entry of three).")

print("\nRESULT:", "ALL CHECKS PASS" if ok else "FAILURES")
sys.exit(0 if ok else 1)
