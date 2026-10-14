#!/usr/bin/env python3
"""DOCKET 67 re-derivation for arXiv:1808.08677 (Yang et al., chiQCD, PRL 121 212001).

The source could NOT be read this pass (alphaXiv quota exhausted; arxiv.org,
export.arxiv.org, inspirehep.net, osti.gov, pubmed, semanticscholar all refused
by the egress policy).  What is checked here is therefore only what is
checkable WITHOUT the source:
  (A) the tree's held quote parses to the values the tree uses;
  (B) internal consistency of the quoted numbers under a NAMED hypothesis
      H-TRACE-SR (trace sum rule  M = <H_m> + <H_a>, so that a quarter of the
      anomaly is (M - <H_m>)/4).  H-TRACE-SR is NOT READ from the source here;
      it is the textbook form (Ji 1995) and the source's own phrase "based on
      the sum rule, given 9(2)(1)% ..." is consistent with it;
  (C) additivity of the four components in the abstract (search-index
      restatement: 33(4)(4)%, 37(5)(4)%) vs the tree's p.5 note (32/36 %);
  (D) sensitivity of the condensate share to the sigma-term inputs the tree
      itself holds as READ (FLAG averages), and whether the chiQCD row can move
      massform's C2 (largest central reading over READ rows).
Stdlib + fractions only.  Imports massform read-only (no writes).
"""
import re, sys, math
from fractions import Fraction as F
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import massform as m

ok = True
def check(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + label + ("  -- " + detail if detail else ""))

# (A) held quote -> values used
held = m.SOURCES["chiQCD"][2] if hasattr(m, "SOURCES") else None
if held is None:
    # locate the dict holding the "chiQCD" entry
    for name in dir(m):
        v = getattr(m, name)
        if isinstance(v, dict) and "chiQCD" in v and isinstance(v["chiQCD"], tuple):
            held = v["chiQCD"][2]; break
print("held quote:", held)
check("A1 '9(2)(1)%' in held quote", "9(2)(1)%" in held)
check("A2 '23(1)(1)%' in held quote", "23(1)(1)%" in held)
check("A3 CHIQCD_QUARK_CONDENSATE == 9.0", m.CHIQCD_QUARK_CONDENSATE == 9.0)
check("A4 CHIQCD_QUARTER_ANOMALY == 23.0", m.CHIQCD_QUARTER_ANOMALY == 23.0)
check("A5 held quote names 'proton' (not nucleon)", "proton" in held and "nucleon" not in held)

# (B) H-TRACE-SR: quarter anomaly = (100 - f_m)/4
fm, e1, e2 = F(9), F(2), F(1)
qa = (100 - fm) / 4
qa_e1, qa_e2 = e1 / 4, e2 / 4
print("B  (100-9)/4 = %s = %.3f %%, propagated errors (%.2f)(%.2f)" % (qa, float(qa), float(qa_e1), float(qa_e2)))
check("B1 H-TRACE-SR reproduces 23 to printed precision", round(float(qa)) == 23,
      "22.75 rounds to 23; propagated (0.50)(0.25) vs printed (1)(1): printed errors are not smaller than propagation")
check("B2 printed errors >= propagated", 1 >= float(qa_e1) and 1 >= float(qa_e2))

# (C) additivity: condensate + quark energy + glue energy + quarter anomaly
abstract = (9, 33, 37, 23)   # abstract, via search-index restatement (NOT READ here)
p5 = (9, 32, 36, 23)         # tree's note, massform.py:1379-1380 (NOT READ here)
sa, sp = sum(abstract), sum(p5)
print("C  abstract sum = %d %%, p.5 (tree note) sum = %d %%" % (sa, sp))
check("C1 p.5 components (tree's reading) close to 100", sp == 100)
ea = math.sqrt(4**2 + 4**2 + 5**2 + 4**2 + 2**2 + 1 + 1 + 1)
check("C2 abstract excess of 2 points is inside combined uncertainty", abs(sa - 100) < ea,
      "excess 2 vs quadrature sum of printed errors %.1f -- a rounding discrepancy, not a contradiction" % ea)

# (D) sensitivity to sigma terms held as READ in the tree
mN = m.M_N_MEV
for k, (a, b, _s) in m.SIGMA_MEASURES.items():
    f = 100 * (a + b) / mN
    print("D  %-11s (sigma_piN %.1f + sigma_s %.1f)/m_N = %.2f %% ; H-TRACE-SR quarter anomaly %.2f %%"
          % (k, a, b, f, (100 - f) / 4))
f_rs = 100 * (m.SIGMA_PIN_ROY_STEINER + m.SIGMA_S_2P1P1) / mN
print("D  Roy-Steiner sigma_piN 59.1 + FLAG 2+1+1 sigma_s 41.0 -> %.2f %% ; quarter anomaly %.2f %%" % (f_rs, (100 - f_rs) / 4))
f211 = 100 * m.F_LIGHT["FLAG 2+1+1"]
check("D1 chiQCD 9%% within its combined error (2.24) of FLAG 2+1 (%.2f)" % (100 * m.F_LIGHT["FLAG 2+1"]),
      abs(9 - 100 * m.F_LIGHT["FLAG 2+1"]) < math.hypot(2, 1))
print("D  chiQCD vs FLAG 2+1+1: %.2f points = %.2f of chiQCD's combined error" % (f211 - 9, (f211 - 9) / math.hypot(2, 1)))
qa_span = (100 - 9) / 4 - (100 - f_rs) / 4
check("D2 moving the condensate to the largest sigma reading moves the quarter anomaly by < its printed (1)(1)",
      qa_span < math.hypot(1, 1), "shift %.2f points" % qa_span)

# (E) can the chiQCD row move C2 (largest central reading over READ rows)?
read_fracs = {"FLAG 2+1+1": m.F_LIGHT["FLAG 2+1+1"], "FLAG 2+1": m.F_LIGHT["FLAG 2+1"],
              "chiQCD": m.CHIQCD_QUARK_CONDENSATE / 100}
read_fracs.update({"Ji " + k: v for k, v in m.JI_FRACTION.items()})
top = max(read_fracs, key=read_fracs.get)
print("E  READ-row nucleon fractions:", {k: round(v, 4) for k, v in read_fracs.items()}, "largest:", top)
check("E1 chiQCD is not the largest READ row", top != "chiQCD")
thr = max(v for k, v in read_fracs.items() if k != "chiQCD")
print("E  chiQCD would need > %.2f %% to move C2: %.2f of its combined error above 9 %%"
      % (100 * thr, (100 * thr - 9) / math.hypot(2, 1)))
print("OVERALL", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
