#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for 2411.04268 (FLAG Review 2024, nucleon sigma terms)
as massform.py uses it (massform.py:320-338, 1314-1350, 1456-1462, 1789-1803, 1905-1912).

Read-only against the tree: the capture TSV is read as text; massform is imported with
bytecode writing OFF (sys.dont_write_bytecode) and nothing is written under research/.

Checks
  A. f_l = (sigma_piN + sigma_s)/m_N for both FLAG averages, m_N = (m_p+m_n)/2 from
     captures/PDG-2026.tsv -- exact over Fraction; compare the tree's 10.85 % / 9.28 %.
  B. The 2.7 sigma tension between Eqs (447) and (448), recomputed (uncorrelated).
  C. Uncertainty of f_l (uncorrelated quadrature) -- FLAG prints no f_l; the sum is the tree's.
  D. Robustness of C2 (HIGGS_SUPPLIES_MOST_ATOMIC_MASS = False): the sigma_piN + sigma_s
     needed for the share to reach 1/2, against every value in play (both FLAG averages,
     their 3-sigma and 5-sigma upper edges, phenomenology 59.1(3.5) charged-pion convention,
     ~56 MeV neutral-pion convention, 55.9(2.5) two-loop BChPT).
  E. The isospin-convention shift Delta sigma_piN = 3.1(5) MeV (restated) on f_l.
  F. H-LINEAR is load-bearing: for M(m) = M0 + c1 m + c32 m^(3/2) (the leading
     non-analytic chiral term, M_pi^2 ~ m), sigma = m dM/dm differs from the finite shift
     M(m) - M0 by (1/2) c32 m^(3/2) -- sympy, exact.  So FLAG's 'shift in M_N' reading of
     sigma is itself first order, which the tree names (H-LINEAR) and does not flatten.
  G. The 'three standard deviations' with Hoferichter 23: arithmetic for the candidate
     values, recorded (which number FLAG used is NOT read here).
"""
import os
import sys
from fractions import Fraction as F
from math import sqrt

import sympy as sp

sys.dont_write_bytecode = True
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
fails = []


def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    if not ok:
        fails.append(name)


# ---------------------------------------------------------------- inputs (READ by the tree)
SPIN_211, SPIN_21 = F("60.9"), F("42.2")      # FLAG Eqs (447), (448)
ESPIN_211, ESPIN_21 = F("6.5"), F("2.4")
SS_211, SS_21 = F("41.0"), F("44.9")          # FLAG Eqs (449), (450)
ESS_211, ESS_21 = F("8.8"), F("6.4")

mass = {}
with open(os.path.join(TREE, "captures/PDG-2026.tsv")) as fh:
    for line in fh:
        if line.startswith("#"):
            continue
        c = line.rstrip("\n").split("\t")
        if c[0] in ("2212", "2112"):
            mass[c[0]] = F(c[11])
m_p, m_n = mass["2212"], mass["2112"]
m_N = (m_p + m_n) / 2
chk("A0 m_N from capture = 938.9187555 MeV (canonical data_used)", m_N == F("938.9187555"),
    "m_p=%s m_n=%s m_N=%s" % (float(m_p), float(m_n), float(m_N)))

# ---------------------------------------------------------------- A
f211 = (SPIN_211 + SS_211) / m_N
f21 = (SPIN_21 + SS_21) / m_N
chk("A1 f_l(2+1+1) rounds to 10.85 %", round(float(f211) * 100, 2) == 10.85, "%.6f %%" % (float(f211) * 100))
chk("A2 f_l(2+1) rounds to 9.28 %", round(float(f21) * 100, 2) == 9.28, "%.6f %%" % (float(f21) * 100))

# ---------------------------------------------------------------- B
t = float(SPIN_211 - SPIN_21) / sqrt(float(ESPIN_211 ** 2 + ESPIN_21 ** 2))
chk("B  sigma_piN 2+1+1 vs 2+1 tension = 2.7 sigma (uncorrelated)", round(t, 1) == 2.7, "%.4f sigma" % t)
ts = float(SS_21 - SS_211) / sqrt(float(ESS_211 ** 2 + ESS_21 ** 2))
print("INFO sigma_s 2+1 vs 2+1+1: %.3f sigma (no tension)" % ts)

# ---------------------------------------------------------------- C
e211 = sqrt(float(ESPIN_211 ** 2 + ESS_211 ** 2)) / float(m_N)
e21 = sqrt(float(ESPIN_21 ** 2 + ESS_21 ** 2)) / float(m_N)
print("INFO f_l(2+1+1) = %.2f(%.2f) %%, f_l(2+1) = %.2f(%.2f) %% (quadrature, uncorrelated; "
      "tree prints centrals only)" % (float(f211) * 100, e211 * 100, float(f21) * 100, e21 * 100))
fd = abs(float(f211 - f21)) / sqrt(e211 ** 2 + e21 ** 2)
print("INFO f_l(2+1+1) - f_l(2+1) = %.3f sigma (sigma_s partly offsets the sigma_piN tension)" % fd)

# ---------------------------------------------------------------- D  (through massform, read-only)
sys.path.insert(0, TREE)
try:
    import massform as mf  # noqa: E402
    ok_import = True
except Exception as exc:  # pragma: no cover
    ok_import = False
    print("WARN massform import failed: %r" % exc)

if ok_import:
    chk("D0 massform F_LIGHT agrees with A", abs(mf.F_LIGHT["FLAG 2+1+1"] - float(f211)) < 1e-12
        and abs(mf.F_LIGHT["FLAG 2+1"] - float(f21)) < 1e-12)
    rows = mf.share_rows()
    ele = rows[0][2]
    pm = mf.payload_masses()
    k = pm["nucleon rest"] / mf.PAYLOAD_KG          # nucleon rest mass / payload mass
    print("INFO electron share %.6f, nucleon-rest/payload %.6f" % (ele, k))
    print("INFO tree HIGGS_SHARE_LARGEST_READ=%.4f ALL=%.4f MARGIN=%.4f; C2=%s, C2_CONTESTED_ONLY=%s"
          % (mf.HIGGS_SHARE_LARGEST_READ, mf.HIGGS_SHARE_LARGEST_ALL, mf.HIGGS_SHARE_READ_MARGIN,
             mf.HIGGS_SUPPLIES_MOST_ATOMIC_MASS, mf.C2_CONTESTED_ONLY))
    # FLAG rows' contribution to the payload share
    for key in ("FLAG 2+1+1", "FLAG 2+1"):
        print("INFO share row %s: %.4f" % (key, ele + mf.F_LIGHT[key] * k))
    # which row sets the READ maximum?
    read_rows = [r for r in rows[1:] if not r[1].startswith("CONTESTED")]
    top = max(read_rows, key=lambda r: r[2])
    print("INFO READ-row maximum is set by: %r (%.4f); FLAG does not set it" % (top[0], ele + top[2]))
    chk("D1 FLAG rows do not set the READ maximum (Ji row does)", not top[0].startswith("nucleons: sigma"))
    need = (0.5 - ele) / k * float(m_N)               # sigma_piN + sigma_s needed for share 1/2
    print("INFO sigma_piN + sigma_s needed for the payload share to reach 1/2: %.1f MeV" % need)
    cands = {
        "FLAG 2+1+1 central": float(SPIN_211 + SS_211),
        "FLAG 2+1 central": float(SPIN_21 + SS_21),
        "FLAG 2+1+1 +3 sigma (linear)": float(SPIN_211 + SS_211 + 3 * (ESPIN_211 + ESS_211)),
        "FLAG 2+1+1 +5 sigma (linear)": float(SPIN_211 + SS_211 + 5 * (ESPIN_211 + ESS_211)),
        "pheno 59.1(3.5) + FLAG 2+1 sigma_s 44.9": 59.1 + 44.9,
        "pheno +5 sigma + sigma_s +5 sigma": 59.1 + 5 * 3.5 + 44.9 + 5 * 6.4,
        "two-loop BChPT 55.9 + 44.9": 55.9 + 44.9,
        "with sigma_c ETM19 107 (CONTESTED as mass)": float(SPIN_211 + SS_211) + 107.0,
    }
    for name, s in cands.items():
        sh = ele + s / float(m_N) * k
        print("INFO %-45s sigma sum %6.1f MeV -> share %.4f (< 0.5: %s)" % (name, s, sh, sh < 0.5))
    chk("D2 no candidate value, to 5 sigma, moves C2 (share < 1/2 on every one)",
        all(ele + s / float(m_N) * k < 0.5 for s in cands.values()))
    # perturbation through the tree's own function: substitute the moved datum
    old = dict(mf.SIGMA_MEASURES)
    try:
        mf.SIGMA_MEASURES.clear()
        mf.SIGMA_MEASURES.update({"alt": (59.1 + 5 * 3.5, 44.9 + 5 * 6.4, "READ")})
        mf.F_LIGHT.clear()
        mf.F_LIGHT.update({kk: mf.sigma_fraction(a, b) for kk, (a, b, _s) in mf.SIGMA_MEASURES.items()})
        lr = mf.largest_central_reading(read_only=True)
        print("INFO largest_central_reading(read_only) with sigma set to pheno+5sigma: %.4f" % lr)
        chk("D3 tree's own verdict function stays < 1/2 under the moved datum", lr < 0.5)
    finally:
        mf.SIGMA_MEASURES.clear(); mf.SIGMA_MEASURES.update(old)
        mf.F_LIGHT.clear()
        mf.F_LIGHT.update({kk: mf.sigma_fraction(a, b) for kk, (a, b, _s) in old.items()})

# ---------------------------------------------------------------- E
d_iso = F("3.1")
print("INFO isospin-convention shift 3.1 MeV moves f_l by %.3f percentage points" % (float(d_iso / m_N) * 100))

# ---------------------------------------------------------------- F  (H-LINEAR is load-bearing)
m, M0, c1, c32 = sp.symbols("m M0 c1 c32", positive=True)
M = M0 + c1 * m + c32 * m ** sp.Rational(3, 2)
sigma = sp.simplify(m * sp.diff(M, m))
shift = sp.simplify(M - M0)
diff = sp.simplify(sigma - shift)
chk("F1 sigma - (M - M0) = c32 m^(3/2)/2 exactly", sp.simplify(diff - c32 * m ** sp.Rational(3, 2) / 2) == 0,
    "sigma - shift = %s" % diff)
chk("F2 sigma == finite shift iff M is linear in m (c32 = 0)", sp.simplify(diff.subs(c32, 0)) == 0)
# generic power: M0 + c m^p -> sigma/shift = p
p = sp.symbols("p", positive=True)
Mp = M0 + c1 * m ** p
chk("F3 sigma/shift = p for a pure power m^p", sp.simplify(m * sp.diff(Mp, m) / (Mp - M0) - p) == 0)

# ---------------------------------------------------------------- G
for lab, v, e in (("59.1(3.5) [1506.04142 eq.21, charged-pion conv.]", 59.1, 3.5),
                  ("59.0(3.5) [as restated in 2506.23902]", 59.0, 3.5),
                  ("56.0(3.5) [~56, neutral-pion conv.; error assumed 3.5]", 56.0, 3.5)):
    print("INFO %s vs FLAG 2+1 42.2(2.4): %.2f sigma; vs FLAG 2+1+1 60.9(6.5): %.2f sigma"
          % (lab, (v - 42.2) / sqrt(e ** 2 + 2.4 ** 2), (60.9 - v) / sqrt(e ** 2 + 6.5 ** 2)))

print("\nRESULT:", "ALL CHECKS PASS" if not fails else "FAILURES: %s" % fails)
sys.exit(1 if fails else 0)
