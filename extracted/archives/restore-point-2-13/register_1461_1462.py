#!/usr/bin/env python3
"""register_1461_1462.py"""
import pathlib, re, sys, textwrap

ENTRIES = [
(1461, "THE CORRIDOR IS ADDITIVE REPRESENTABILITY OF A RANKED ORDER, AND THE NUCLEAR RESULT IS A CANCELLATION CONDITION.",
 "*The person named it: an old-school question about ranked order pairs. It is, and it has a literature "
 "going back to 1959.* **Given a finite set with an observed order and a candidate additive form, each "
 "adjacent pair yields one strict linear inequality in the parameters; the order is REPRESENTABLE "
 "exactly when that system is feasible; and an infeasible system has a FARKAS CERTIFICATE, which in this "
 "literature is a CANCELLATION CONDITION.** *Kraft, Pratt & Seidenberg, Intuitive probability on finite "
 "sets, Ann. Math. Statist. 30 (1959) 408–419 — de Finetti's conjecture disproved by a five-element "
 "order satisfying every obvious condition and admitting no representing measure. Scott, Measurement "
 "structures and linear inequalities, J. Math. Psych. 1 (1964) 233–247 — the general criterion, proved "
 "by linear programming. Krantz, Luce, Suppes & Tversky, Foundations of Measurement I (1971) — Farkas' "
 "lemma ALONE gives the cancellation law as the characterisation. Behind them Motzkin (1936) and Kuhn "
 "(1956) on solvability of linear inequalities.* **So the corridor is the FEASIBLE REGION OF A LINEAR "
 "PROGRAM: non-emptiness is representability, emptiness is a violated cancellation condition. The "
 "observed ATOMIC order IS additively representable in ν's family, 106 of 106 feasible. The observed "
 "NUCLEAR order is NOT representable in Nilsson's.** *This is not a new instrument. It is a classical "
 "one, and knowing its name imports its theorems — including Fishburn's (1996–97) on how high the "
 "cancellation order must climb before infeasibility appears, which is the standing warning that "
 "feasibility found by spot-checking low-order conditions is NOT representability. Any corridor must be "
 "SOLVED, not sampled.*"),

(1462, "AND THE RATIO-4 IDENTITY IS NOT A STEP TOWARD THE PROOF — IT IS THE PROOF, BECAUSE IT MAKES THE CONSTRAINT MATRIX RANK ONE.",
 "*Computed in exact rationals: the six constraint vectors in (β, α) are (6, 3/2), (10, 5/2), (10, 5/2), "
 "(−6, −3/2), (−14, −7/2) and (−18, −9/2).* **Every one is a positive multiple of (4, 1). The constraint "
 "matrix has RANK ONE, so all six half-planes are bounded by parallel lines through the origin, and "
 "three point each way.** *That is why the certificate is the shortest an infeasible order system can "
 "have: two constraints on the same functional with opposite signs, summing to 0 > 0 — a SECOND-ORDER "
 "cancellation, where Kraft–Pratt–Seidenberg's celebrated counterexample needs a higher one.* **The "
 "identity Δ[ℓ(ℓ+1)] = 4ℓ+6 and Δ⟨L·S⟩ = −(ℓ+3/2) for every Δℓ = 2 pair within a shell is exactly the "
 "statement that every constraint carries the same normal. Parallel-with-both-signs is infeasible by "
 "inspection, so the identity does not lead to the proof; it IS the proof.** *And the field reached the "
 "same answer from the other side: arXiv 1110.6134's table gives κ = 0.0250 for ℓ = 1 within N = 5 where "
 "ℓ = 3 and ℓ = 5 get 0.0570, a factor of 2.3 INSIDE ONE SHELL — ℓ-independence abandoned by fitting, "
 "which is what the rank-one certificate says is forced. Two routes, one a proof and one thirty years of "
 "level-scheme fitting, to the same answer. Register 1393's narrowing was right in direction and did not "
 "go far enough: the field fits per (N, ℓ), not merely per mass region.*"),
]

P = pathlib.Path("/home/claude/work/REGISTER-DATA.md")
s = P.read_text(encoding="utf-8")
if max(int(m) for m in re.findall(r"^ {0,3}(\d{3,4})\. \*\*", s, re.M)) != 1460:
    print("REFUSING"); sys.exit(1)
blocks = []
for n, h, b in ENTRIES:
    t = f"{n}. **{h}** {re.sub(r'\s+', ' ', b).strip()}"
    blk = "\n".join(textwrap.wrap(t, 97, initial_indent=" ", subsequent_indent=" ",
                                 break_long_words=False, break_on_hyphens=False))
    if blk.count("**") % 2:
        print(f"ODD ** in {n}"); sys.exit(1)
    blocks.append(blk)
P.write_text(s.rstrip("\n") + "\n\n" + "\n\n".join(blocks) + "\n", encoding="utf-8")
print(f"appended 1461–1462")
