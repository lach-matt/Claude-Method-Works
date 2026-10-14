# PRE-DOCKET 68 COMPUTATION (2026-10-02), not seated.  M: "the corridor connects two positions as one".
# Modelled as an identification of positions under latticectc.py's hypotheses H1-H3 (flat bulk, translation
# lattice acting freely, test branes) -- a MODEL CHOICE, named.  latticectc's THEOREM: a closed causal curve exists
# iff the lattice contains a nonzero causal vector.  Imported, never copied.
import os, sys, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from fractions import Fraction as Fr
import latticectc as L
E1, E2 = L.WITNESS_E1, L.WITNESS_E2
print("one corridor whose ends share a moment in some frame (spacelike xi): nrm =", L.nrm(E1),
      "| closed causal curve:", L.rank1_has_causal(E1))
print("two such corridors, each simultaneous in a DIFFERENT frame (E1, E2): span", L.span_kind(E1, E2),
      "| closed causal curve:", L.box_has_causal(E1, E2))
# H-FRAME: every corridor keyed to the same moment of ONE frame -> every lattice vector has t = 0 -> none is
# causal (a theorem by inspection: nrm = sum of spatial squares > 0 for a nonzero vector).  Checked, not proved here:
random.seed(1); bad = n = 0
for _ in range(2000):
    g1 = (Fr(0),) + tuple(Fr(random.randint(-9, 9), random.randint(1, 9)) for _ in range(3))
    g2 = (Fr(0),) + tuple(Fr(random.randint(-9, 9), random.randint(1, 9)) for _ in range(3))
    if L.nrm(g1) == 0 or L.nrm(g2) == 0 or L.span_kind(g1, g2) != "spacelike": continue
    n += 1; bad += L.box_has_causal(g1, g2, nmax=6)
print(f"{n} random corridor pairs keyed to one frame: pairs with a closed causal curve = {bad}")
