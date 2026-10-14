#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for 'qcd-trace-anomaly-nucleon-mass'.
Tree use: tolman.py:803-806 "QCD matter is NOT traceless; the trace anomaly is
essentially the whole of the nucleon mass, so it sits OUTSIDE this identity's
hypothesis".  Checks (exit 1 on any failure):
 A  Ji 1995 (hep-ph/9410274) eqs (4),(7)-(11): <P|T^{mu nu}|P> = P^mu P^nu / M gives
    traceless 3/4 M and trace 1/4 M of the rest energy, and the Lorentz-invariant
    trace g_{mu nu}<T^{mu nu}> = M != 0 for every M > 0  (the load-bearing fact).
 B  Ji Table I reproduced from a = 0.55 and bM = 160 / 107 MeV (rounded to 10 MeV).
 C  Anomaly fraction of the TRACE sum rule, 1 - b (Nf = 3, gamma_m neglected, as in
    Ji eq (36)), with Ji's inputs and current inputs; and the same thing in Ji's
    HAMILTONIAN reading, (1-b)/4; and the Nf = 6 F^2-only reading (Hoferichter &
    Ruiz de Elvira 2506.23902 eq (35)).
 D  Heavy-quark theorem check, 2/27 (m_N - sigma_piN - sigma_s) (2506.23902 eq 33).
 E  Classical Maxwell flux tube is traceless; a Nambu-Goto string is not.
 F  The tree's rung ratios (9.7773e40 / QCD rung, / magnetar rung).
"""
import sys, math
import sympy as sp

fails = []
def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    if not ok:
        fails.append(label)

# ---------------------------------------------------------------- A
M = sp.symbols("M", positive=True)
g = sp.diag(1, -1, -1, -1)
P = sp.Matrix([M, 0, 0, 0])
T = P * P.T / M                                  # <P|T^{mu nu}|P>, Ji eq (4)
trace = sum(g[m, n] * T[m, n] for m in range(4) for n in range(4))
check("A1 Lorentz trace g_{mu nu}<T^{mu nu}> = M", sp.simplify(trace - M) == 0, str(trace))
That = g.inv() * trace / 4                        # hat T^{mu nu} = g^{mu nu} T/4
Tbar = T - That
tr_bar = sp.simplify(sum(g[m, n] * Tbar[m, n] for m in range(4) for n in range(4)))
check("A2 Tbar is traceless", tr_bar == 0)
check("A3 <Tbar^00> = 3M/4 (Ji eq 10)", sp.simplify(Tbar[0, 0] - 3 * M / 4) == 0)
check("A4 <That^00> = M/4 (Ji eq 11)", sp.simplify(That[0, 0] - M / 4) == 0)
check("A5 trace nonzero for every M>0 (hadron is never traceless)",
      sp.solve(sp.Eq(trace, 0), M) == [])

# ---------------------------------------------------------------- B
MN_ji = 939.0
a = 0.55
for bM, want in ((160.0, (270, 160, 320, 190)), (107.0, (300, 110, 320, 210))):
    b = bM / MN_ji
    got = (3 * (a - b) / 4 * MN_ji, b * MN_ji, 3 * (1 - a) / 4 * MN_ji, (1 - b) / 4 * MN_ji)
    rounded = tuple(int(10 * round(x / 10)) for x in got)
    # Ji rounds 'to nearest 10 MeV' and states 5-10 MeV errors; allow 10 MeV.
    ok = all(abs(r - w) <= 10 for r, w in zip(rounded, want))
    check("B  Ji Table I at bM=%g" % bM, ok,
          "computed %s -> rounded %s vs published %s" % (
              tuple(round(x, 1) for x in got), rounded, want))

# ---------------------------------------------------------------- C
MN = 938.27208816          # PDG proton mass, MeV
cases = [
    ("Ji 1995, ms->0 (bM=160)", MN_ji, 160.0),
    ("Ji 1995, ms->inf (bM=107)", MN_ji, 107.0),
    ("Roy-Steiner 59.0 + lattice sigma_s 43 (2506.23902)", MN, 59.0 + 43.0),
    ("lattice Nf=2+1 42.2 + 44.9 (FLAG via 2506.23902 Tab 1)", MN, 42.2 + 44.9),
    ("lattice Nf=2+1+1 60.9 + 41.0 (2506.23902 Tab 1)", MN, 60.9 + 41.0),
    ("chiQCD 2018 H_m = 9% (1808.08677)", 1.0, 0.09),
    ("HRdE 2025 incl. higher order m_ud=69 + 43", MN, 69.0 + 43.0),
]
fr = []
for lab, m, bm in cases:
    f = 1 - bm / m
    fr.append(f)
    print("     trace-sum-rule anomaly fraction 1-b = %.3f ; Ji-Hamiltonian (1-b)/4 = %.3f  [%s]"
          % (f, f / 4, lab))
check("C1 trace-sum-rule anomaly fraction in [0.80, 0.92] for every input set",
      all(0.80 <= f <= 0.92 for f in fr), "min %.3f max %.3f" % (min(fr), max(fr)))
check("C2 current-data spread (lattice vs Roy-Steiner) moves it < 0.03",
      abs((1 - (42.2 + 44.9) / MN) - (1 - (59.0 + 43.0) / MN)) < 0.03)
check("C3 Ji-Hamiltonian anomaly share is ~1/4, NOT 'essentially the whole'",
      all(f / 4 < 0.25 for f in fr))
nf6 = 1 - (69 + 43 + 68 + 65 + 63) / MN
check("C4 Nf=6 F^2-only share ~2/3 (2506.23902 eq 35: 630 MeV)",
      abs(nf6 * MN - 630) < 1.0, "%.3f (%.1f MeV)" % (nf6, nf6 * MN))

# ---------------------------------------------------------------- D
hq = 2.0 / 27.0 * (MN - 59.0 - 43.0)
check("D  heavy-quark theorem 2/27(m_N - sigma_piN - sigma_s) ~ 62 MeV", abs(hq - 62) < 1,
      "%.2f MeV" % hq)

# ---------------------------------------------------------------- E
E = sp.symbols("E", positive=True)
u = E ** 2 / 2
pz, px, py = -E ** 2 / 2, E ** 2 / 2, E ** 2 / 2     # longitudinal E-field tube
check("E1 Maxwell tube trace -u + p_x + p_y + p_z = 0", sp.simplify(-u + px + py + pz) == 0)
s, A = sp.symbols("sigma A", positive=True)
ng = -(s / A) + (-(s / A)) + 0 + 0                   # Nambu-Goto: u = s/A, p_z = -s/A, p_perp = 0
check("E2 Nambu-Goto string trace = -2 sigma/A != 0", sp.simplify(ng + 2 * s / A) == 0 and ng != 0)

# ---------------------------------------------------------------- F
QE = 1.602176634e-19
sig = 0.9e9 * QE / 1e-15
qcd = sig / (math.pi * (0.5e-15) ** 2)
mu0 = 1.25663706212e-6
mag = (1e11) ** 2 / (2 * mu0)
bill = 9.7773e40
check("F1 QCD rung 1.836e35 Pa", abs(qcd / 1.8359591832535274e35 - 1) < 1e-9, "%.4e" % qcd)
check("F2 bill / QCD rung ~ 1e6 (order of magnitude)", 1e5 < bill / qcd < 1e7, "%.3e" % (bill / qcd))
check("F3 bill / magnetar rung = 2.46e13", abs(bill / mag / 2.46e13 - 1) < 0.005, "%.4e" % (bill / mag))
GeVfm3 = 1e9 * QE / 1e-45
print("     Yanagihara 1803.05656 Fig 2: -T_zz(0) ~ 10-13 GeV/fm^3 at R = 0.46 fm = %.2e - %.2e Pa"
      % (10 * GeVfm3, 13 * GeVfm3))

print("\n%d failures" % len(fails))
sys.exit(1 if fails else 0)
