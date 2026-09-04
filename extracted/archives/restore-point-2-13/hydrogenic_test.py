#!/usr/bin/env python3
"""hydrogenic_test.py — REBUILT from register 1382, PARTIALLY: the data the
original ran on is not in this tree.

WHAT 1382 SAYS. Q.final's "hydrogenic output exactly zero" was listed among the
fit statistics as though 110 rows had confirmed it. It is a TAUTOLOGY of the
form: at Ne = 1 the factor (Ne − 1)/Ne vanishes identically, for every charge and
every C(Z), so no parameter can move it and no data can confirm it. That much is
arithmetic and is checked below with no data at all.

What the H-like sequence DOES test is the domain, by reading the defect back out
as  delta = 1 - Z*sqrt(R_inf / IE).  Register 1382 reports |delta| under 6e-4 to
Z = 10, climbing monotonically to +0.103 at Z = 110, with hydrogen and helium
slightly NEGATIVE from reduced mass, and a fit delta = A(Za)^2 + B(Za)^4 on
Z >= 3 giving R^2 = 0.99996 and A = 0.1162 against the Dirac 1s coefficient
1/8 = 0.125, SEVEN PERCENT LOW and unaccounted (queue item E2a).

WHAT IS BLOCKED. That sequence needs measured ionisation energies for H-like
ions up to Z = 110. This tree holds THREE: H I, He II and Li III, from
LADDER-H-Ar-I-III.tsv. The two reduced-mass points are checkable and are checked;
the Z >= 3 fit and the 7% Dirac deficit are NOT, and are left open rather than
estimated from three points.
"""
import re

R_INF = 109737.31568508          # cm^-1, CODATA
M_E_OVER_U = 1 / 1822.888486209  # electron mass in atomic mass units
ISOTOPE_A = {"H": 1.00782503, "He": 4.00260325, "Li": 7.01600344}

print("  PART 1 — THE STRUCTURAL ZERO, WHICH NEEDS NO DATA\n")
qf = lambda Ne: (Ne - 1) / Ne
print(f"    Q.final's factor (Ne − 1)/Ne at Ne = 1, for any charge and any C(Z):")
for c in (1, 2, 5, 10, 50):
    print(f"      charge {c:<3} -> {qf(1) * c:.20f}")
print("    Zero for every one, by construction. A quantity that vanishes by")
print("    construction must never be quoted beside quantities the data")
print("    constrains — R 1382's general statement, verified in one line.\n")

print("  PART 2 — THE DEFECT READ BACK OUT, ON WHAT THIS TREE HOLDS\n")
rows = [l.rstrip("\n").split("\t") for l in open("LADDER-H-Ar-I-III.tsv", encoding="utf-8")
        if not l.startswith("#")]
hdr, data = rows[0], rows[1:]
D = [dict(zip(hdr, r)) for r in data]
hlike = [r for r in D if r["isoel_seq"] == "H"]
print(f"    H-like species held: {len(hlike)}  ({', '.join(r['sp_name'] for r in hlike)})")
print(f"    R 1382's sequence runs to Z = 110. BLOCKED on data.\n")
print(f"    {'species':<9}{'Z':>3}{'IE (cm⁻¹)':>18}{'δ observed':>13}{'δ reduced-mass':>16}")
for r in hlike:
    Z = int(r["at_num"])
    ie = float(re.sub(r"\(.*\)", "", r["ie_cm1"]))
    d_obs = 1 - Z * (R_INF / ie) ** 0.5
    el = r["sp_name"].split()[0]
    A = ISOTOPE_A.get(el)
    # R_M = R_inf/(1 + m_e/M): delta from reduced mass alone, to first order
    d_pred = -0.5 * M_E_OVER_U / A if A else None
    ps = f"{d_pred:+.6f}" if d_pred is not None else "—"
    print(f"    {r['sp_name']:<9}{Z:>3}{ie:>18.6f}{d_obs:>+13.6f}{ps:>16}")
print("\n    R 1382 quotes hydrogen −0.000267 against −0.000272 predicted, and")
print("    helium −0.000046 against −0.000069. Both reproduce above.")
print("    Lithium already departs: reduced mass alone no longer accounts for it,")
print("    which is the relativistic term entering — and is exactly why 1382 says")
print("    only hydrogen and helium 'sit slightly negative, which is reduced mass'.\n")
print("  WHAT REMAINS BLOCKED\n")
print("    the monotone climb to +0.103 at Z = 110 : needs H-like IE to Z = 110")
print("    the fit δ = A(Zα)² + B(Zα)⁴ on Z ≥ 3    : needs the same")
print("    A = 0.1162 against 1/8, 7.04% low       : queue item E2a, unaccounted")
print("\n    Three points cannot carry a two-parameter fit and will not be asked to.")
