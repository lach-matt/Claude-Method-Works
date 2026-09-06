#!/usr/bin/env python3
"""lawtest.py -- the promotion test for the proposed law.

CANDIDATE, as stated:
    A closed index has a shape that is definable, so it must have a mathematical
    expression, and that expression must be given in the book.

TWO CLAUSES, and they are different kinds of statement.

  (a) EXISTENCE   a closed index has a definable shape, hence an expression
  (b) OBLIGATION  the expression must be stated

(a) is a theorem or it is false. (b) is a protocol — it cannot be false, only
unmet, so it belongs in Part I with §2.14 and §2.19 rather than in Part III.

THE TEST FOR (a). What would "the expression" be? For a closed index the
envelopes φ̂ ARE the shape: X is closed iff X = {x : x_i ≤ φ̂_ij(x_j)}, so the
envelope set determines the index completely. And §15.2's S3 proves the
envelopes are RECOVERABLE FROM THE CELLS. So (a) is already a theorem of this
book, stated as bound recovery.

  If that is right the candidate is DECLINED as a law and (a) becomes a
  COROLLARY of S3, while (b) becomes a protocol. The test is whether (a) says
  anything S3 does not.

THE TEST FOR (b). Which closed indices in this corpus have their expression
stated? That count is what gives the obligation teeth or shows it vacuous.
"""
import sys
from zeno import State, step

# every closed index the corpus carries, with what stands as its expression
INDICES = [
 ("Λ₈, the lattice",              "F(z₁…z₈) = Σ_n z₁ⁿ Σ_{ℓ≤n−1} … , §11.3",              "STATED"),
 ("Λ₉–Λ₁₃, the tower",            "the five bounds, §12.11.1, one per axis",              "STATED"),
 ("the cylinder A_q × B_q",       "A_q(z), B_q(z), §12.7",                                "STATED"),
 ("the box ordering",             "l ≥ w ≥ h, two monotone bounds",                       "STATED"),
 ("the chessboard",               "the full product; ℛ is the identity",                  "STATED"),
 ("Janet's left-step table",       "period = n+ℓ, block order f,d,p,s",                   "STATED"),
 ("the calendar, relabelled",     "days(m) monotone in m",                                "STATED"),
 ("the drawn nuclide band",       "the two drip lines as envelopes",                      "STATED"),
 ("Appendix D, fibred",           "16 fibres by kind × language",                         "PARTIAL — the fibration is named, no expression"),
 ("the audits at 3 coordinates",  "—",                                                    "NOT STATED"),
 ("the back-matter Index",        "s ⊑ t ⇒ loc(s) ⊆ loc(t), a down-set condition",        "STATED"),
 ("Q, fibred by domain",          "—",                                                    "NOT STATED"),
 ("the register index (§26.9)",   "repair ≤ φ(corroboration), recovered by ℛ",            "STATED"),
 ("the reference index (§16.6.1)","access—referent—checked—verdict, a cycle",             "STATED"),
 ("V3 geometry (Transitions)",    "—",                                                    "NOT STATED"),
 ("V6 solution (Transitions)",    "—",                                                    "NOT STATED"),
 ("the local null surface",       "Θ = 0, θ carries no transverse derivative",            "STATED"),
 ("the ANEC covered cases",       "—",                                                    "NOT STATED"),
 ("the bibliography (§18.6.1)",   "era—ρ—access—entered, four bounds",                    "STATED"),
 ("the EM index in Λ",            "δ⁻¹(T) closed iff T ∩ range(δ) convex",                "STATED THIS SESSION"),
]

def run():
    from collections import Counter
    c = Counter(x[2].split(" —")[0] for x in INDICES)
    return c

with State("lawtest") as st:
    c = step(st, "audit the closed indices for a stated expression", run, budget=30)

print(f"  {'closed index':<32}{'its expression':<52}status")
for n, e, s in INDICES:
    print(f"  {n:<32}{e:<52}{s}")
tot = len(INDICES)
print(f"\n  {dict(c)}   of {tot}")
stated = c["STATED"] + c["STATED THIS SESSION"]
print(f"""
  CLAUSE (a) — EXISTENCE. For a closed index X, X = {{x : x_i ≤ φ̂_ij(x_j) ∀ i≠j}}
  by definition of ℛ and X = ℛ(X). The envelope set therefore DETERMINES the
  index, and §15.2's S3 proves the envelopes are recoverable from the cells.
  So every closed index has an expression AND it can always be read off.
  **(a) is a corollary of S3, not a new law.**

  CLAUSE (b) — OBLIGATION. {stated} of {tot} closed indices in this corpus carry a
  stated expression; {c['NOT STATED']} carry none and {c['PARTIAL']} is partial. The obligation is
  therefore NOT vacuous — it is unmet in a quarter of cases — but an obligation
  is a protocol, not a law: it cannot be false, only unfulfilled.
""")
sys.exit(0)
