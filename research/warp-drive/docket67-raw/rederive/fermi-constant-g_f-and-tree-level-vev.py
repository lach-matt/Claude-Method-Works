#!/usr/bin/env python3
"""DOCKET 67 re-derivation: fermi-constant-g_f-and-tree-level-vev.

Checks, each printed PASS/FAIL (exit 1 on any FAIL):
  A. sympy: the tree relations G_F/sqrt2 = g^2/(8 M_W^2), M_W = g v/2
     give v = (sqrt2 G_F)^(-1/2) identically, and
     V_min = -lambda v^4/4 with lambda = m_h^2/(2 v^2) is -m_h^2 v^2/8.
  B. MuLan's own extraction (arXiv:1211.0960 eq. 23-24) re-run from its READ
     inputs: tau, m_mu, hbar, Delta q(0,1,2) -> G_F = 1.1663787(6).
  C. Eberhart et al. 2026 (arXiv:2607.02657 eq. 17, 20, 21) re-run from its
     READ inputs -> 1.16637859(59).
  D. Buttazzo et al. (arXiv:1307.3536 eq. 27) convention: without the
     3 m_mu^2/(5 M_W^2) term G_mu comes out ~0.6e-11 lower (they print
     1.1663781).
  E. v, rho_EW, xi_required under every READ value of G_F; the fractional
     move of each against the tree's pinned 1.1663788 and against the
     tolerance of the tree's own fixture.
  F. tree lambda vs MS-bar NNLO lambda(M_t) (Buttazzo Table 3): size of the
     tree-level truncation the owner does not name.
Every number is either READ at source (cited) or COMPUTED here.
"""
import math
import sys
import sympy as sp

FAILS = []


def chk(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    if not ok:
        FAILS.append(label)


def rel(a, b):
    return abs(a / b - 1.0)


# ---------------------------------------------------------------- A. sympy
GF, g, MW, v, mh = sp.symbols("G_F g M_W v m_h", positive=True)
sol_v = sp.solve(sp.Eq(GF / sp.sqrt(2), g ** 2 / (8 * (g * v / 2) ** 2)), v)
chk("A1 tree: G_F/sqrt2 = g^2/(8 M_W^2), M_W = g v/2  =>  v = (sqrt2 G_F)^(-1/2)",
    len(sol_v) == 1 and sp.simplify(sol_v[0] - (sp.sqrt(2) * GF) ** sp.Rational(-1, 2)) == 0,
    str(sol_v))
lam = mh ** 2 / (2 * v ** 2)
Vmin = -lam * v ** 4 / 4
chk("A2 V_min = -lambda v^4/4, lambda = m_h^2/(2v^2)  =>  -m_h^2 v^2/8",
    sp.simplify(Vmin + mh ** 2 * v ** 2 / 8) == 0)
# minimum of V = -(mu2/2) phi^2 + (lam/4) phi^4 with V(0)=0
phi, mu2, l4 = sp.symbols("phi mu2 lam", positive=True)
V = -mu2 / 2 * phi ** 2 + l4 / 4 * phi ** 4
phimin = [s for s in sp.solve(sp.diff(V, phi), phi) if s != 0][0]
chk("A3 V(0)=0 Mexican hat: phi_min^2 = mu2/lam, V_min = -mu2^2/(4 lam) = -lam v^4/4",
    sp.simplify(V.subs(phi, phimin) + l4 * phimin ** 4 / 4) == 0)

# ---------------------------------------------------------------- B. MuLan 2013
# READ: arXiv:1211.0960 p.28-29
tau_mulan = 2196980.3e-12            # s
hbar_2010 = 6.58211928e-25           # GeV s  (CODATA 2010, as MuLan used)
mmu_2010 = 105.6583715e-3            # GeV    (CODATA 2010)
dq = (-187.1 + -4233.7 + 36.3 - 0.4) * 1e-6   # Delta q(0)+(1)+(2) + Pak-Czarnecki
Gamma = hbar_2010 / tau_mulan        # GeV
GF_mulan_re = math.sqrt(192 * math.pi ** 3 * Gamma / mmu_2010 ** 5 / (1 + dq))
print("   B: G_F from MuLan inputs = %.9e GeV^-2 (published 1.1663787(6)e-5)" % GF_mulan_re)
chk("B1 MuLan eq.23 re-run agrees with printed 1.1663787(6)e-5 within its own 0.5 ppm uncertainty",
    abs(GF_mulan_re - 1.1663787e-5) < 0.6e-11, "rel %.2e" % rel(GF_mulan_re, 1.1663787e-5))
print("   B: DISCREPANCY RECORDED, not repaired: the re-run from the printed inputs sits %.2f ppm "
      "(%.2f sigma) above the printed value" % (rel(GF_mulan_re, 1.1663787e-5) * 1e6,
      (GF_mulan_re - 1.1663787e-5) / 0.6e-11))
# variants that could account for it (each printed Delta q term is rounded to 0.1 ppm)
for lab, d in (("without the separate -0.4 ppm Pak-Czarnecki term", (-187.1 - 4233.7 + 36.3) * 1e-6),
               ("with the 2026 Delta q (-4384.678 ppm)", -4384678e-9)):
    Gv = math.sqrt(192 * math.pi ** 3 * Gamma / mmu_2010 ** 5 / (1 + d))
    print("   B variant %-52s G_F = %.9e" % (lab, Gv))

# ---------------------------------------------------------------- C. 2026 update
# READ: arXiv:2607.02657 eq. (4), (17), (20), (21); hbar exact (SI 2019)
tau_avg = 2.1969811e-6               # s  (MuLan + PDG average, their eq. 20)
mmu_pdg = 105.6583755e-3             # GeV
hbar_si = 6.582119569e-25            # GeV s (exact to digits shown)
dq26 = -4384678e-9
GF26 = math.sqrt(192 * math.pi ** 3 * (hbar_si / tau_avg) / mmu_pdg ** 5 / (1 + dq26))
print("   C: G_F from 2026 inputs = %.10e GeV^-2 (published 1.16637859(59)e-5)" % GF26)
chk("C1 Eberhart et al. eq.21 re-run reproduces 1.16637859e-5 to < 0.05 ppm",
    rel(GF26, 1.16637859e-5) < 5e-8, "rel %.2e" % rel(GF26, 1.16637859e-5))

# ---------------------------------------------------------------- D. convention
MW_ = 80.384
wprop = 3 * mmu_2010 ** 2 / (5 * MW_ ** 2)
GF_nowprop = GF_mulan_re * math.sqrt(1 + wprop)   # G^2(1+w) fixed => G_nw = G*sqrt(1+w)
# In Buttazzo's convention the W-propagator factor is kept OUTSIDE G_mu, so
# G_mu^2 (1+w) = G_F^2  =>  G_mu = G_F / sqrt(1+w)
G_mu_buttazzo = 1.1663787e-5 / math.sqrt(1 + wprop)   # from MuLan's PRINTED value
print("   D: 3 m_mu^2/(5 M_W^2) = %.3e; G_mu (Buttazzo convention) = %.8e (printed 1.1663781e-5)"
      % (wprop, G_mu_buttazzo))
chk("D1 Buttazzo's 1.1663781e-5 is the MuLan value with the dim-8 W-propagator term removed",
    abs(G_mu_buttazzo - 1.1663781e-5) < 0.6e-12, "diff %.2e" % (G_mu_buttazzo - 1.1663781e-5))

# ---------------------------------------------------------------- E. sensitivity
TREE_GF = 1.1663788e-5
HBAR = 1.054571817e-34
C = 299792458.0
GN = 6.67430e-11
GEV_J = 1.602176634e-10
HBARC = HBAR * C


def vev(G):
    return 1.0 / math.sqrt(math.sqrt(2.0) * G)


def rho_ew(G, m_h):
    return (m_h ** 2 * vev(G) ** 2 / 8.0) * GEV_J ** 4 / HBARC ** 3


def mpl_red():
    return math.sqrt(HBAR * C ** 5 / GN) / GEV_J / math.sqrt(8 * math.pi)


def xi_req(G):
    return (mpl_red() / vev(G)) ** 2


chk("E0 tree fixture: v(1.1663788e-5) = 246.2196 to 1e-5 (excite.py:1172)",
    rel(vev(TREE_GF), 246.2196) < 1e-5, "v = %.6f" % vev(TREE_GF))
chk("E0b tree fixture: rho_EW(m_h=125.20) = 2.476937e45 J/m^3 to 1e-6 (excite.py:1381)",
    rel(rho_ew(TREE_GF, 125.20), 2.476937e45) < 1e-6, "%.7e" % rho_ew(TREE_GF, 125.20))
chk("E0c tree fixture: xi_required(v) = 9.7829068836e31 to 1e-9 (excite.py:1396)",
    rel(xi_req(TREE_GF), 9.7829068836e31) < 1e-9, "%.10e" % xi_req(TREE_GF))
chk("E0d Buttazzo Table 2 V = 246.21971 from G_mu=1.1663787e-5",
    abs(vev(1.1663787e-5) - 246.21971) < 6e-5, "v = %.6f" % vev(1.1663787e-5))

READS = [
    ("PDG 2024 Table 1.1 (tree's pin)", 1.1663788e-5),
    ("MuLan 2011 PRL 1010.0991", 1.1663788e-5),
    ("MuLan 2013 PRD 1211.0960 / CODATA 2022", 1.1663787e-5),
    ("Eberhart et al. 2026 2607.02657", 1.16637859e-5),
    ("Buttazzo 1307.3536 (no dim-8 W term)", 1.1663781e-5),
    ("hypothetical +17 ppm (1999 total unc., 1211.0960)", 1.1663788e-5 * (1 + 17e-6)),
    ("G_F^EW global fit (2102.02825)", 1.16716e-5),
    ("G_F^CKM unitarity (2102.02825)", 1.16550e-5),
]
print("\n   E: moves against the tree's pinned G_F = 1.1663788e-5")
print("   %-42s %14s %12s %12s %12s" % ("source", "G_F", "dv/v", "drho/rho", "dxi/xi"))
for name, G in READS:
    dv = vev(G) / vev(TREE_GF) - 1
    dr = rho_ew(G, 125.13) / rho_ew(TREE_GF, 125.13) - 1
    dx = xi_req(G) / xi_req(TREE_GF) - 1
    print("   %-42s %14.9e %12.3e %12.3e %12.3e" % (name, G, dv, dr, dx))
dv_max_muon = max(abs(vev(G) / vev(TREE_GF) - 1) for _, G in READS[:5])
chk("E1 every muon-decay READ moves v by < 1e-6 (tree fixture tol 1e-5)", dv_max_muon < 1e-6,
    "max |dv/v| = %.2e" % dv_max_muon)
dx26 = abs(xi_req(1.16637859e-5) / xi_req(TREE_GF) - 1)
print("   note: xi_required fixture tol 1e-9 is tighter than G_F's own 0.5 ppm; the 2026 value "
      "moves it by %.2e (a fixture-precision remark, not a physics move)" % dx26)
# rho_EW is an order-of-magnitude figure in the tree; largest non-muon move
dr_max = max(abs(rho_ew(G, 125.13) / rho_ew(TREE_GF, 125.13) - 1) for _, G in READS)
chk("E2 even the most discrepant independent G_F (EW fit / CKM) moves rho_EW by < 0.1 %",
    dr_max < 1e-3, "max |drho/rho| = %.2e" % dr_max)

# ---------------------------------------------------------------- F. tree vs MS-bar
# READ: Buttazzo et al. Table 2 (M_h=125.15, V=246.21971) and Table 3 (mu = M_t)
Mh_b = 125.15
lam_tree = 1.1663787e-5 / math.sqrt(2) * Mh_b ** 2
chk("F1 tree lambda = G_mu M_h^2/sqrt2 reproduces Buttazzo LO 0.12917",
    abs(lam_tree - 0.12917) < 1e-5, "%.6f" % lam_tree)
lam_nnlo, m_nnlo = 0.12604, 131.55
print("   F: lambda(M_t) NNLO / tree = %.4f ; m(M_t)^2 NNLO / M_h^2 = %.4f"
      % (lam_nnlo / lam_tree, (m_nnlo / Mh_b) ** 2))
# the tree-form depth -m^4/(16 lam) evaluated with MS-bar parameters at mu=M_t,
# against -M_h^2 V^2/8 -- ILLUSTRATIVE ONLY: V_min is not an observable, and the
# loop-corrected effective potential adds Coleman-Weinberg terms not included here.
depth_tree = Mh_b ** 2 * 246.21971 ** 2 / 8
depth_msbar_treeform = m_nnlo ** 4 / (16 * lam_nnlo)
print("   F: tree-form depth with MS-bar(M_t) parameters / on-shell tree depth = %.3f (illustrative)"
      % (depth_msbar_treeform / depth_tree))
chk("F2 the tree-level truncation is a percent-to-tens-of-percent effect, not an order of magnitude",
    0.5 < depth_msbar_treeform / depth_tree < 2.0)

print("\n%d FAIL" % len(FAILS))
sys.exit(1 if FAILS else 0)
