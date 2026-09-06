import numpy as np, sympy as sp
from itertools import product
print("="*88)
print("  APPLYING §23.5's LESSON TO §23.6, §23.7, §23.8")
print("="*88)
print("""
  §23.5: a list enumerated once, against a structure that kept growing.
  §23.3 had the same defect. **These three sections are lists too — of
  objects tested against the index. Ask what each list omits.**
""")
print("="*88)
print("  §23.6 — CELESTIAL: FOUR OBJECTS TESTED. WHAT DOES THE STRUCTURE ADMIT?")
print("="*88)
TESTED=[("Lagrange L1,L2,L3 in μ","bracket, 18/18"),
        ("Hill stability in mass ratio","bracket, V≈100"),
        ("planetary semi-major axes","monotone, sign change"),
        ("L4,L5","on the pole exactly")]
ADMITTED=[("orbital resonances p:q","§11.7.1 — E(X), order cut at 7/8","TESTED elsewhere, not listed here"),
          ("the nuclear shell model","§23.6.2","listed"),
          ("satellite counts vs Hill radius","+0.86 log-log","MEASURED, NOT IN THE SECTION"),
          ("Roche limit vs density","monotone in ρ^(1/3)","NOT TESTED"),
          ("Kozai-Lidov critical inclination","a threshold in one parameter","NOT TESTED"),
          ("Lagrange point STABILITY (μ < 0.0385)","a threshold, not a family","NOT TESTED"),
          ("periodic-orbit families","braid catalogues","NOT TESTED — §23.9"),
          ("secular resonance locations","monotone in semi-major axis","NOT TESTED")]
print("\n  %-40s%s"%("object the method admits","status"))
print("  "+"-"*76)
for a,b,c in ADMITTED: print("  %-40s%s"%(a,c))
n_new=sum(1 for _,_,c in ADMITTED if 'NOT' in c or 'NOT IN' in c)
print("\n     **E(§23.6's list) ≥ %d** — objects the method plainly applies to,"%n_new)
print("     absent from the section.")
print("""
  **And one is not merely absent — it is MEASURED IN THIS WORK and not
  reported there.** The Hill-radius / satellite-count correlation of +0.86
  appears in §16.14.1 as a capacity bound and never in §23.6's table.
""")
print("="*88)
print("  §23.7 — STRING: TWO OBJECTS. WHAT ELSE HAS THE SHAPE?")
print("="*88)
S7=[("mass spectrum α′m² = N−1","on the pole","LISTED"),
    ("partition function ∏(1−qⁿ)^−24","F with counts","LISTED"),
    ("no critical dimension","Λ closes at every d","LISTED"),
    ("no Hagedorn point","capped coordinates","LISTED"),
    ("level degeneracy d(N)","monotone, convex, 3-monotone — V measured","MEASURED, NOT LISTED"),
    ("the dimension ladder Λ_d ⊂ Λ_{d+1}","exact projection, closure both ways","MEASURED, NOT LISTED"),
    ("regge trajectories J vs m²","linear — the pole again","NOT TESTED"),
    ("central charge c vs dimension","linear in D","NOT TESTED"),
    ("BPS state counting","a generating function with counts","NOT TESTED")]
print("\n  %-44s%s"%("object","status"))
print("  "+"-"*74)
for a,b,c in S7: print("  %-44s%s"%(a,c))
print("\n     **E(§23.7's list) ≥ %d**"%sum(1 for _,_,c in S7 if 'NOT' in c))
print("""
  **Two of them were computed in this session and never written down**:
  d(N)'s bracket behaviour, and the dimension ladder in which each Λ_d is
  the exact projection of Λ_{d+1} with closure preserved both ways.
""")
print("="*88)
print("  §23.8 — CALABI–YAU: TWO TESTS RUN, AND ONE ARITHMETIC CHECK MISSED")
print("="*88)
print("""
  §23.8 verifies mirror symmetry from 248,305 / 248,305 / 495,515. **The
  same three numbers carry a second check the section does not make.**
""")
a=248305; u=495515; both=a+a-u
N=473800776
print("     both Hodge numbers ≥ 140 : %d"%both)
print("     as a fraction of the KS list : %.6f%%"%(100*both/N))
print("     and of the 495,515 with one large : %.3f%%"%(100*both/u))
print("""
     **0.221%% of the polytopes with one large Hodge number have both.**
  That is the Pareto strength, and §23.8.3 states it against the full
  473.8 million rather than against the relevant subpopulation —
  **0.0002%% instead of 0.221%%, a factor of a thousand.**

  Both are true; the second is the one that means something.
""")
print("="*88)
print("  THE COMMON DEFECT")
print("="*88)
print("""
  **All three sections are lists of objects tested, and all three omit
  objects the method plainly admits** — including several measured in this
  work and never written into them.

  > **E(§23.6) ≥ 6 · E(§23.7) ≥ 5 · E(§23.8): one statistic stated against
  > the wrong denominator.**

  **That is §23.5's finding for the third, fourth and fifth time in one
  chapter.** The protocol says enumerate before searching; **the chapter
  enumerates once per section and never revisits any of them.**
""")