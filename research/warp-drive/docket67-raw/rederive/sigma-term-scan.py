#!/usr/bin/env python3
"""DOCKET 67 -- audit of the external input 'sigma-term-scan' (address.S_SCAN).

READ-ONLY with respect to research/warp-drive: imports address.py with
bytecode writing disabled and never writes under the tree.

Checks, in order:
 1. sympy: one-loop threshold matching gives d ln Lambda_3/d ln v = 2/9 exactly
    (3 heavy quarks x 2/27), and the H1 form d ln m_p/d ln v = 2/9 + 7S/9 follows
    from m_p = Lambda_3 f(m_u, m_d, m_s / Lambda_3) with S = sum over the THREE
    light flavours -- i.e. S must include sigma_s.  Cross-check against
    Hoferichter et al. 2015 eq.(24): 2/9 + 7/9 (f_u+f_d+f_s) = 0.305.
 2. The scan rows as MeV: 0.06 <-> sigma, 0.09 <-> sigma_piN + sigma_s.
 3. Current data (READ at source): Hoferichter 2015 sigma_piN = 59.1(3.5) MeV;
    FLAG 2024 sigma_piN = 42.2(2.4) [Nf=2+1], 60.9(6.5) [Nf=2+1+1];
    sigma_s = 44.9(6.4) [Nf=2+1], 41.0(8.8) [Nf=2+1+1].
 4. Every S-dependent output of address.py recomputed at the current S values,
    by calling address's own functions (never retyped).
"""
import sys
sys.dont_write_bytecode = True
from fractions import Fraction
import sympy as sp

sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import address as A  # noqa: E402

out = {}
ok = True


def check(name, cond):
    global ok
    ok = ok and bool(cond)
    print("  [%s] %s" % ("PASS" if cond else "FAIL", name))


print("1. sympy re-derivation of the H1 form")
nf = sp.symbols("n_f")
b0 = 11 - sp.Rational(2, 3) * nf
# Lambda_{n-1}^{b(n-1)} = Lambda_n^{b(n)} m^{b(n-1)-b(n)}; track exponents
a = sp.Integer(1)
e = {}
for n, q in ((6, "t"), (5, "b"), (4, "c")):
    bh, bl = b0.subs(nf, n), b0.subs(nf, n - 1)
    a = a * bh / bl
    for k in e:
        e[k] = e[k] * bh / bl
    e[q] = (bl - bh) / bl
dlam = sp.nsimplify(sum(e.values()))
print("   exponents:", e, " sum =", dlam, " Lambda_6 power =", a)
check("d ln Lambda_3/d ln v = 2/9 exactly", dlam == sp.Rational(2, 9))
check("each heavy quark carries 2/27", all(v == sp.Rational(2, 27) for v in e.values()))
check("address.dln_lambda_dln_v() agrees", A.dln_lambda_dln_v() == Fraction(2, 9))

# m_p = L * f(x_u, x_d, x_s), x_q = m_q/L ; homogeneity => sum_q m_q dm_p/dm_q + L dm_p/dL = m_p
L, mu, md, ms, lv = sp.symbols("Lambda m_u m_d m_s lnv", positive=True)
f = sp.Function("f")
mp = L * f(mu / L, md / L, ms / L)
euler = sp.simplify(L * sp.diff(mp, L) + sum(m * sp.diff(mp, m) for m in (mu, md, ms)) - mp)
check("Euler homogeneity: L dm/dL + sum_{u,d,s} m_q dm/dm_q = m_p (residual 0)", euler == 0)
S = sp.symbols("S")
# light masses ~ v (Yukawa), Lambda_3 ~ v^(2/9) (H1): dln m_p/dln v = (1-S)*2/9 + S*1
H1 = sp.expand((1 - S) * sp.Rational(2, 9) + S)
check("H1: dln m_p/dln v = 2/9 + 7S/9", sp.simplify(H1 - (sp.Rational(2, 9) + sp.Rational(7, 9) * S)) == 0)
print("   => S in this formula is the sum over ALL THREE flavours that are light relative")
print("      to Lambda_3 (u, d, s): S = (sigma_piN + sigma_s)/m_N.  Strange is not optional.")
# Hoferichter 2015 eq. (24): 2/9 + 7/9 (f_u+f_d+f_s) = 0.305 +- 0.009 (READ)
S_hof = (Fraction(305, 1000) - Fraction(2, 9)) * Fraction(9, 7)
f_ud_hof = (0.0208 + 0.0411 + 0.0189 + 0.0451) / 2   # eq. (23), p/n averaged
print("   Hoferichter eq.(24) inverted: S_uds = %.4f; eq.(23) f_u+f_d = %.4f -> implied f_s = %.4f"
      % (float(S_hof), f_ud_hof, float(S_hof) - f_ud_hof))
out["S_uds_from_Hoferichter_eq24"] = float(S_hof)

print("\n2. the scan rows, in MeV (m_p = %.5f MeV, address.M_P_MEV)" % A.M_P_MEV)
mp_mev = A.M_P_MEV
for lab, s in A.S_SCAN:
    print("   %-26s S = %.5f  <->  %.2f MeV" % (lab, s, s * mp_mev))
check("56 MeV / m_p rounds to 0.06 (%.5f)" % (56 / mp_mev), round(56 / mp_mev, 2) == 0.06)
implied_sigma_s = 0.09 * mp_mev - 0.06 * mp_mev
print("   0.09 row minus 0.06 row = %.1f MeV implied sigma_s" % implied_sigma_s)
out["row_0.09_MeV"] = 0.09 * mp_mev
out["implied_sigma_s_MeV"] = implied_sigma_s

print("\n3. current data (READ at source) as S")
data = {
    "Hoferichter15 sigma_piN (Roy-Steiner)": (59.1, 3.5),
    "FLAG24 Nf=2+1 sigma_piN": (42.2, 2.4),
    "FLAG24 Nf=2+1+1 sigma_piN": (60.9, 6.5),
    "FLAG24 Nf=2+1 sigma_s": (44.9, 6.4),
    "FLAG24 Nf=2+1+1 sigma_s": (41.0, 8.8),
}
for k, (v, u) in data.items():
    print("   %-40s %6.1f(%4.1f) MeV  S-part = %.4f(%.4f)" % (k, v, u, v / mp_mev, u / mp_mev))
combos = {
    "S_ud  FLAG Nf=2+1": (42.2, 2.4),
    "S_ud  pheno RS 2015": (59.1, 3.5),
    "S_ud  FLAG Nf=2+1+1": (60.9, 6.5),
    "S_uds FLAG Nf=2+1 (42.2+44.9)": (42.2 + 44.9, (2.4 ** 2 + 6.4 ** 2) ** 0.5),
    "S_uds FLAG Nf=2+1+1 (60.9+41.0)": (60.9 + 41.0, (6.5 ** 2 + 8.8 ** 2) ** 0.5),
    "S_uds pheno+FLAG2+1 sigma_s (59.1+44.9)": (59.1 + 44.9, (3.5 ** 2 + 6.4 ** 2) ** 0.5),
}
Svals = {}
for k, (v, u) in combos.items():
    Svals[k] = v / mp_mev
    print("   %-42s S = %.4f +- %.4f" % (k, v / mp_mev, u / mp_mev))
out["S_current"] = Svals
tension = (59.1 - 42.2) / (3.5 ** 2 + 2.4 ** 2) ** 0.5
print("   pheno vs FLAG Nf=2+1 sigma_piN: %.1f sigma apart (uncorrelated quadrature;"
      " FLAG applies a pi0 isospin convention shift not reproduced here)" % tension)
out["pheno_vs_lattice21_tension_sigma"] = tension
lo, hi = min(Svals.values()), max(Svals.values())
scan_hi = max(s for _, s in A.S_SCAN)
check("the scan's top row (0.09) covers the Nf=2+1 S_uds central (%.4f)"
      % Svals["S_uds FLAG Nf=2+1 (42.2+44.9)"], scan_hi >= Svals["S_uds FLAG Nf=2+1 (42.2+44.9)"] - 0.0075)
covers_all = scan_hi >= hi
print("   scan top %.2f vs largest current S_uds central %.4f -> covered: %s" % (scan_hi, hi, covers_all))
out["scan_covers_largest_current_S_uds"] = covers_all

print("\n4. address.py's S-dependent outputs, recomputed by its own functions")
grid = [("tree S_mid", 0.06), ("tree 0.09", 0.09)] + [(k, v) for k, v in Svals.items() if k.startswith("S_uds")]
rows = []
base = {}
for lab, s in grid:
    r = {}
    for h in ("H1", "H2"):
        r["K_mu_" + h] = float(A.K_mu(s, h))
        r["f_" + h] = A.higgs_fraction(s, h)
        r["eps_det_" + h] = A.eps_det_stationary(h, s)
        r["eps_nuc_" + h] = A.eps_from_matter(A.RHO_NUCLEAR, A.higgs_fraction(s, h))
        r["nuc_over_det_" + h] = abs(r["eps_nuc_" + h]) / r["eps_det_" + h]
        r["courier_kg_m3_" + h] = A.source_density(A.eps_detectable_transported(1e-18),
                                                   A.higgs_fraction(s, h))[0]
    r["naive_correction_factor"] = A.naive_correction_factor(s)
    r["f_H1_over_0.0096"] = A.higgs_fraction(s, "H1") / (A.QUARK_SUM_MEV / A.M_P_MEV)
    rows.append((lab, s, r))
    if lab == "tree S_mid":
        base = r
keys = list(base)
print("   %-34s %7s " % ("row", "S") + " ".join("%12s" % k[:12] for k in keys))
for lab, s, r in rows:
    print("   %-34s %7.4f " % (lab[:34], s) + " ".join("%12.4e" % r[k] for k in keys))
print("\n   ratio to the tree's S_mid = 0.06 row:")
for lab, s, r in rows[1:]:
    print("   %-34s " % lab[:34] + " ".join("%12.3f" % (r[k] / base[k]) for k in keys))
out["outputs"] = {lab: dict(S=s, **r) for lab, s, r in rows}

print("\n   conclusions tested across S in [0.0096, 0.12]:")
Sgrid = [0.0096 + i * (0.12 - 0.0096) / 200 for i in range(201)]
check("K_mu < 0 under H1 and H2 at every S", all(A.K_mu(s, h) < 0 for s in Sgrid for h in ("H1", "H2")))
check("|K_mu| is O(1): in [0.6, 1.0]", all(0.6 <= abs(float(A.K_mu(s, h))) <= 1.0 for s in Sgrid for h in ("H1", "H2")))
check("|K_mu(H2)/K_mu(H1)| < 1.3 (address selftest's own pin) at every S",
      all(abs(A.K_mu(s, "H2") / A.K_mu(s, "H1")) < 1.3 for s in Sgrid))
check("nuclear matter displaces vev downward, both H, every S",
      all(A.eps_from_matter(A.RHO_NUCLEAR, A.higgs_fraction(s, h)) < 0 for s in Sgrid for h in ("H1", "H2")))
check("nuclear eps exceeds eps_det (>1) both H, every S",
      all(abs(A.eps_from_matter(A.RHO_NUCLEAR, A.higgs_fraction(s, h))) / A.eps_det_stationary(h, s) > 1
          for s in Sgrid for h in ("H1", "H2")))
nuc_min = min(abs(A.eps_from_matter(A.RHO_NUCLEAR, A.higgs_fraction(s, h))) / A.eps_det_stationary(h, s)
              for s in Sgrid for h in ("H1", "H2"))
print("   min nuclear-over-threshold across the band: %.3g" % nuc_min)
ncf = {lab: r["naive_correction_factor"] for lab, s, r in rows}
in_3_45 = {lab: 3.0 <= v <= 4.5 for lab, v in ncf.items()}
print("   address.py:86 prose 'at the scanned sigma-term values it is 3 to 4.5':")
for lab, v in ncf.items():
    print("     %-36s naive_correction_factor = %.3f  in [3,4.5]: %s" % (lab, v, in_3_45[lab]))
out["naive_correction_factor"] = ncf
out["all_checks_pass"] = ok

import json
with open("/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67/rederive/sigma-term-scan.out.json", "w") as fh:
    json.dump(out, fh, indent=1, default=str)
print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
sys.exit(0 if ok else 1)
