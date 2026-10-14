#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key sakharov-1967 (Sakharov conditions, as used by
warpfolder.py:81-85,229,338-339,400-404,553-559 and massform.py:1250-1256).

Checks, each with its own status:
 A. data: m_p as used (CODATA 2018) vs CODATA 2022, READ from the banked scipy-1.17.1
    _codata.py table; 100 kg / m_p.
 B. the label "baryons": mass per baryon for real ordinary matter (isotope masses READ
    from the banked periodictable-2.1.0 package) vs m_p -- how far 100 kg/m_p is from
    the true baryon count.
 C. condition (iii) as a theorem, finite toy: with a CPT-type antiunitary Theta,
    Theta H Theta^-1 = H, Theta B Theta^-1 = -B  =>  Tr(exp(-beta H) B) = 0 even when
    [H,B] != 0 (B violated). Adding a CPT-odd term -mu*B breaks it: <B> != 0. Shows the
    CPT / zero-chemical-potential hypothesis is load-bearing for the necessity of (iii).
 D. SM equilibrium with sphalerons active (B+L violated, B-L conserved): chemical-
    potential equilibrium gives B = (8N_f+4m)/(22N_f+13m) (B-L) -> 28/79 for N_f=3,m=1
    (Harvey-Turner 1990 / Khlebnikov-Shaposhnikov 1988 relation: NAMED-NOT-READ, computed
    here). A flash starting from B-L = 0 ends at B = 0 in equilibrium.
 E. eta: 6.1e-10 against Omega_b h^2 = 0.02237 (Planck 2018 -- RECALLED, NOT READ in this
    stage) and T_CMB = 2.7255 K (RECALLED, NOT READ); and the scale the tree's sentence
    implies if eta were read as a yield per photon (named hypothesis, illustration only).
"""
import sys, zipfile, re, math, os
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D67 = os.path.dirname(HERE)
ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)

# ---------------------------------------------------------------- A. CODATA
whl = os.path.join(D67, "src/codata/scipy-1.17.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl")
t = zipfile.ZipFile(whl).read("scipy/constants/_codata.py").decode()
def codata(name, which):  # which = -1 -> last table (2022), -2 -> 2018
    rows = [l for l in t.splitlines() if l.startswith(name + "  ")]
    v = rows[which][60:85].replace(" ", "").replace("...", "")
    return float(v)
mp18, mp22 = codata("proton mass", -2), codata("proton mass", -1)
u22 = codata("atomic mass constant", -1); mn22 = codata("neutron mass", -1)
me22 = codata("electron mass", -1); G22 = codata("Newtonian constant of gravitation", -1)
kB = 1.380649e-23; hbar = 1.054571817e-34; c = 299792458.0
print("A. m_p CODATA 2018 = %.11e ; CODATA 2022 = %.11e ; rel move %.2e" % (mp18, mp22, (mp22-mp18)/mp18))
chk("tree's M_PROTON (warpfolder.py:190) equals CODATA 2018 m_p", mp18 == 1.67262192369e-27)
N18, N22 = 100.0/mp18, 100.0/mp22
print("   100 kg/m_p: 2018 %.6e  2022 %.6e" % (N18, N22))
chk("100 kg/m_p = 5.979e28 within 1e-3 under either CODATA", abs(N18/5.979e28-1) < 1e-3 and abs(N22/5.979e28-1) < 1e-3)

# ------------------------------------------------- B. mass per baryon, real matter
sys.path.insert(0, os.path.join(D67, "src/pkgs/pt"))
import periodictable as pt
H1, C12, N14, O16, Fe56 = pt.H[1].mass, pt.C[12].mass, pt.N[14].mass, pt.O[16].mass, pt.Fe[56].mass
mats = {
    "water H2O (1H,16O atoms)": ((2*H1 + O16), 18),
    "carbon-12 (atoms)":         (C12, 12),
    "nitrogen-14 (atoms)":       (N14, 14),
    "iron-56 (atoms)":           (Fe56, 56),
    "free protons":              (mp22/u22, 1),
}
print("B. isotope masses (periodictable 2.1.0, u): 1H %.8f 12C %.8f 16O %.8f 56Fe %.7f" % (H1, C12, O16, Fe56))
dev = []
for k, (m_u, A) in mats.items():
    per = m_u*u22/A
    Nb = 100.0/per
    dev.append((k, Nb/N22 - 1))
    print("   %-28s mass/baryon %.6e kg -> baryons in 100 kg %.5e  (vs 100kg/m_p: %+.3f%%)" % (k, per, Nb, 100*(Nb/N22-1)))
real = [d for k, d in dev if k != "free protons"]
chk("for atomic matter 100 kg/m_p UNDER-counts baryons by 0.3-0.9%", all(0.003 < d < 0.009 for d in real))
chk("the undercount does not change the order of magnitude (5.98e28 vs ~6.0e28)", all(abs(d) < 0.01 for d in real))

# ---------------------------------------------------- C. condition (iii), CPT toy
rng = np.random.default_rng(1967)
n = 4
b = np.array([1., 1., 2., 3.])               # baryon numbers of the n particle states
B = np.diag(np.concatenate([b, -b]))         # antiparticles carry -b
S = np.block([[np.zeros((n, n)), np.eye(n)], [np.eye(n), np.zeros((n, n))]])  # Theta psi = S conj(psi)
def herm(k):
    X = rng.normal(size=(k, k)) + 1j*rng.normal(size=(k, k)); return (X + X.conj().T)/2
A = herm(n)                                   # complex A: C and CP violated generically
Cm = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); Cm = (Cm + Cm.T)/2   # symmetric: B-violating
H = np.block([[A, Cm], [Cm.conj(), A.conj()]])
chk("toy H Hermitian", np.allclose(H, H.conj().T))
chk("toy H is Theta-invariant (S H* S = H)", np.allclose(S @ H.conj() @ S, H))
chk("B is Theta-odd (S B* S = -B)", np.allclose(S @ B.conj() @ S, -B))
chk("B is NOT conserved ([H,B] != 0): condition (i) present", not np.allclose(H @ B - B @ H, 0))
Ccon = S                                       # linear charge conjugation candidate: C = swap
chk("C violated in toy (S H S != H)", not np.allclose(S @ H @ S, H))
def thermal_B(Hm, beta=0.7):
    w, V = np.linalg.eigh(Hm); rho = V @ np.diag(np.exp(-beta*(w - w.min()))) @ V.conj().T
    return float(np.real(np.trace(rho @ B)/np.trace(rho)))
bB = thermal_B(H)
print("C. <B>_eq with Theta-invariant H: %.3e" % bB)
chk("equilibrium <B> = 0 for Theta-invariant H despite B and C violation", abs(bB) < 1e-12)
for mu in (0.05, 0.3):
    bm = thermal_B(H - mu*B)
    print("   <B>_eq with CPT-odd term -mu*B, mu=%.2f: %.4f" % (mu, bm))
    chk("CPT-odd term (mu=%.2f) gives <B>_eq != 0: the CPT hypothesis is load-bearing" % mu, abs(bm) > 1e-3)
# out of equilibrium: charge-symmetric start, Theta-invariant H, C and CP violating -> <B(t)> can move
w, V = np.linalg.eigh(H)
psi0 = np.zeros(2*n, complex); psi0[0] = 1/math.sqrt(2); psi0[n] = 1/math.sqrt(2)   # <B>=0, C-symmetric
Bt = [float(np.real((V @ np.diag(np.exp(-1j*w*tt)) @ V.conj().T @ psi0).conj() @ B @ (V @ np.diag(np.exp(-1j*w*tt)) @ V.conj().T @ psi0))) for tt in np.linspace(0, 5, 51)]
print("   pure-state evolution from <B>=0: max|<B(t)>| = %.3f" % max(abs(x) for x in Bt))
chk("out of equilibrium (unitary evolution) <B(t)> departs from 0: (iii) is necessary, not sufficient-blocking", max(abs(x) for x in Bt) > 1e-3)

# ---------------------------------------- D. SM chemical equilibrium, sphalerons on
muQ, muu, mud, muL, mue, muphi, Nf, m = sp.symbols("mu_Q mu_u mu_d mu_L mu_e mu_phi N_f m")
eqs = [sp.Eq(muu, muphi + muQ), sp.Eq(mud, -muphi + muQ), sp.Eq(mue, -muphi + muL),   # Yukawa
       sp.Eq(3*muQ + muL, 0),                                                           # EW sphaleron
       sp.Eq(Nf*(muQ + 2*muu - mud - muL - mue) + 2*m*muphi, 0)]                        # Y = 0
sol = sp.solve(eqs, [muu, mud, mue, muL, muphi], dict=True)[0]
Bexpr = Nf*(2*muQ + muu + mud); Lexpr = Nf*(2*muL + mue)
ratio = sp.simplify((Bexpr/(Bexpr - Lexpr)).subs(sol))
print("D. B/(B-L) =", ratio, " ; N_f=3,m=1:", ratio.subs({Nf: 3, m: 1}))
chk("B = 28/79 (B-L) for N_f = 3, one Higgs doublet", ratio.subs({Nf: 3, m: 1}) == sp.Rational(28, 79))
num, den = sp.fraction(sp.together(ratio))
chk("ratio finite (denominator 22N_f+13m > 0 for N_f,m >= 1), so B-L = 0 initial => B = 0 in equilibrium with sphalerons active",
    all(den.subs({Nf: a, m: bb}) > 0 for a in range(1, 7) for bb in range(1, 4)))

# ------------------------------------------------------------------ E. eta
Obh2, Tcmb = 0.02237, 2.7255                        # RECALLED, not read this stage
Mpc = 3.0856775814913673e22
H100 = 100e3/Mpc
rho_c_h2 = 3*H100**2/(8*math.pi*G22)
n_gamma = 2*1.2020569031595942/math.pi**2*(kB*Tcmb/(hbar*c))**3
for lab, mb in (("m_p", mp22), ("u", u22)):
    eta = Obh2*rho_c_h2/mb/n_gamma
    print("E. n_gamma = %.2f cm^-3; eta(Omega_b h^2=%.5f, m_b=%s) = %.4e" % (n_gamma*1e-6, Obh2, lab, eta))
eta_u = Obh2*rho_c_h2/u22/n_gamma
chk("6.1e-10 agrees with eta from Omega_b h^2=0.02237 to 2 significant figures", round(eta_u*1e10, 1) in (6.1, 6.2))
# the tree's sentence read as a yield: photons, and energy, per 100 kg of net baryons
Ngam = N18/6.1e-10
T_GeV = 160.0; Egam_J = 2.701*T_GeV*1.602176634e-10
E = Ngam*Egam_J
print("   IF eta were a yield per photon (named hypothesis): %.2e photons of mean energy 2.701 kT at T=%g GeV = %.2e J = %.2e kg c^2" % (Ngam, T_GeV, E, E/c**2))
chk("the yield reading implies a flash > 1e11 times the mass-energy of the payload", E/c**2/100.0 > 1e11)

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
