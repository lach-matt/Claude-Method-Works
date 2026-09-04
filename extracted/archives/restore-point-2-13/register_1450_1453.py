#!/usr/bin/env python3
"""register_1450_1453.py — the literature bridge and the join."""
import pathlib, re, sys, textwrap

ENTRIES = [
(1450, "THE OUTSIDE LITERATURE, SEARCHED AT LAST, AND OUR COORDINATES ARE FIFTY YEARS OLD.",
 "*A precedent search on the Löwdin challenge itself, owed since the work began.* **The challenge is open "
 "by consensus — Scerri, Phil. Trans. R. Soc. A 378, 20190300 (2020): numerous authors claim to have met "
 "it and the generally held opinion is that none has succeeded as Löwdin intended.** *The principal "
 "attempt is Demkov & Ostrovsky, Sov. Phys. JETP 35, 66 (1972): the focusing potential U(r) ∝ "
 "−r⁻¹(r+R)⁻², closely resembling Thomas–Fermi, gives additional degeneracy for levels of identical "
 "N = n+ℓ at E = 0. Thyssen & Ceulemans (Shattered Symmetry, OUP 2017) object that it cannot count as a "
 "solution BECAUSE THE POTENTIAL WAS GUESSED — an objection that transfers directly to ν, which this "
 "work posited.* **And the coordinates are not ours. Demkov & Ostrovsky write the degeneracy as "
 "N − 1 = n_r + 2ℓ with n_r = n − ℓ − 1; Belokolos (SIGMA 13, 038, 2017) states it as an identity, "
 "M = n + ℓ = n_r + 2ℓ + 1.** *The node count and ℓ are the standard coordinate system of this "
 "literature. That this work arrived at them independently is a validation of the coordinates and not a "
 "contribution.* **Belokolos also gives the period lengths in closed form, L_M = 2(⌊M/2⌋+1)², so the "
 "period-two structure this session found from node-count invariance under (n,ℓ)→(n+1,ℓ+1) is a "
 "restatement of a published formula. Correct, and not new. LOWDIN-LITERATURE.md holds the full record "
 "with attributions.**"),

(1451, "AND BELOKOLOS ANSWERS THE OBJECTION THAT SANK DEMKOV–OSTROVSKY: THE 2 IS DERIVED, NOT CHOSEN.",
 "*His chain: any central potential carries a dynamical O(4) symmetry, not merely the Coulomb one; "
 "frequency degeneracy qω_r = pω_θ forces the energy to depend only on p·n_r + q·ℓ; solving the "
 "resulting Abel integral equation gives a family of potentials indexed by α = q/p.* **Requiring the "
 "potential to be Coulombic as r → 0 FORCES α = 2. That yields the Tietz potential V(r) = −Z/(r(1+r/R)²) "
 "and E = E(n_r + 2ℓ), which is the Madelung rule.** *Demkov & Ostrovsky picked μ = ½ out of the same "
 "family and were criticised for it; Belokolos derives the ratio from the nuclear singularity.* **So the "
 "frequency ratio ω_r = 2ω_θ — the radial oscillation running twice per revolution — is the origin of "
 "the 2 in M = 2n − p − 1, which is Madelung's number written in OUR coordinates.** *His E = 0 condition "
 "√(2ZR) = M with R = (9/2Z)^(1/3) gives Z = M³/6 for the onset of each group. His nineteen exceptions — "
 "Cr, Cu, Nb, Mo, Ru, Rh, Pd, Ag, La, Ce, Gd, Pt, Au, Ac, Th, Pa, U, Np, Cm — are a strict SUPERSET of "
 "register 1395's eleven. And his stated intention is to compare his spectrum against the NIST Atomic "
 "Spectra Database, in future tense: he has the derivation this work lacks, and this work has the "
 "measurement he has not made.*"),

(1452, "THE INTRA-GROUP CROSSING IS THE ARITHMETIC MEAN OF TWO SQUARE ROOTS, AND THAT IS WHERE THE GOLDEN RATIO COMES FROM.",
 "*The person pointed at φ = 1.6180 appearing among the crossings and said that when the golden ratio "
 "turns up unexpectedly it is always worth explaining. It is, and the explanation simplifies a registered "
 "result.* **Within a Madelung group, p = 2n − M − 1, so Δp = 2Δn along the group and register 1400's "
 "a_cross = Δn(√p_g + √p_r)/(p_g − p_r) COLLAPSES to (√p_g + √p_r)/2.** *Every intra-group crossing is "
 "the arithmetic mean of the square roots of the two node counts — verified on all twenty pairs. The "
 "whole surd list reads off as means: 1/√2 = (√0+√2)/2, 1 = (√0+√4)/2, (1+√3)/2, (√2+2)/2, √6/2, "
 "(√3+√5)/2, (1+√7)/2, (√5+√7)/2.* **And φ is the p = 1, 5 member: (√1 + √5)/2 = (1+√5)/2, which is the "
 "DEFINITION of the golden ratio rather than a resemblance to it. It occurs at 4d/6s in M = 6 and at "
 "5f/7p in M = 8 — one pair seen twice under the shift that preserves p. Mercury's recorded a = 0.8090 "
 "is φ/2, the same surd halved, from the 5d/6s contest.** *Two things fell out of chasing it. The "
 "general a_cross formula is never needed on the pairs that matter, since Madelung's groups are same-M "
 "groups. And since p ≡ M+1 (mod 2), odd M gives even node counts and even M gives odd ones — so the two "
 "disjoint crossing families are means of √even and means of √odd, and φ is STRUCTURALLY EXCLUDED from "
 "half the table.*"),

(1453, "THE JOIN: BELOKOLOS SUPPLIES THE GROUP, PAULI PRUNES IT, AND a SITS ON THE CROSSING PAULI LEAVES BINDING.",
 "*Three layers, each doing one job.* **Belokolos's degeneracy at E = 0 makes every member of a Madelung "
 "group indistinguishable — the group exists and its internal order does not. Pauli removes members as "
 "they fill, which is register 1397's rule doing structural work. And a orders what survives: within a "
 "group, Madelung's second rule holds IF AND ONLY IF a < (√p_A + √p_B)/2 for every open pair, so the "
 "crossings are CEILINGS and the smallest is binding.** *Measured against the eight recorded values: "
 "five sit in groups Pauli has reduced to a single open member, where the group imposes no constraint at "
 "all. In the three where more than one member remains open — lanthanum at M = 7, protactinium and "
 "lawrencium at M = 8 — a sits EXACTLY on the binding ceiling: 0.7071, 1.3660, 1.9841, three for three.* "
 "**So the degeneracy Belokolos collapses at E = 0 is the degeneracy a resolves, and the value a takes "
 "is not interior but the crossing itself — which is what register 1403 found as an endpoint and Λ_t "
 "read as time being a value only at the point of observability. This says what that endpoint IS: the "
 "last crossing Pauli has left standing.** *Cautions: three cases is three cases, the other five are "
 "unconstrained rather than confirming, and the two agreements at 1.3660 are one surd seen twice since "
 "the binding ceiling alternates by the parity of M. It does however hand over a placement rule not yet "
 "tried — a = the minimum intra-group crossing among Pauli-admissible members — which reads only node "
 "counts, capacities and the current configuration, and which comes from a derivation rather than from "
 "guessing. It carries the same circularity risk as every rule tried this session and must be tested out "
 "of sample against Madelung's 96.*"),
]

P = pathlib.Path("/home/claude/work/REGISTER-DATA.md")
s = P.read_text(encoding="utf-8")
nums = [int(m) for m in re.findall(r"^ {0,3}(\d{3,4})\. \*\*", s, re.M)]
if max(nums) != 1449:
    print(f"REFUSING: highest is {max(nums)}, expected 1449"); sys.exit(1)
blocks = []
for n, head, body in ENTRIES:
    t = f"{n}. **{head}** {re.sub(r'\s+', ' ', body).strip()}"
    b = "\n".join(textwrap.wrap(t, 97, initial_indent=" ", subsequent_indent=" ",
                                break_long_words=False, break_on_hyphens=False))
    if b.count("**") % 2:
        print(f"ODD ** in {n}"); sys.exit(1)
    blocks.append(b)
P.write_text(s.rstrip("\n") + "\n\n" + "\n\n".join(blocks) + "\n", encoding="utf-8")
print(f"appended {len(blocks)} entries, 1450–{ENTRIES[-1][0]}")
