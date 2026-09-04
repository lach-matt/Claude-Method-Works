#!/usr/bin/env python3
"""register_1454_1456.py"""
import pathlib, re, sys, textwrap

ENTRIES = [
(1454, "HIS SPECTRUM RANKED AGAINST OURS, AND A DOMAIN VIOLATION CAUGHT BEFORE IT BECAME A FALSE REFUTATION.",
 "*Gap 1's test: rank the admissible subshells by Belokolos's first-order semiclassical energy "
 "E = −8(√(2ZR) − M)(ℓ+½)/((3η² − 8η)R²), η = 2ZR/(ℓ+½)², R = (9/2Z)^⅓, and compare with the observed "
 "entrant and with ν.* **The first run gave him 34 of 106, picking 5g at almost every step. That was not "
 "a disagreement — it was his formula applied outside its domain. His derivation requires η > 4 for the "
 "turning points to be real, and 5g at low Z is nowhere near it, so the level does not exist and the "
 "expansion is meaningless. Reporting the 34 would have been a false refutation of a published result.** "
 "*The condition is his, stated in his own §4, and is now enforced in `belokolos_spectrum.py` with a "
 "comment saying why.* **With it applied: his ranking matches the observed entrant 87 of 106 — eighty-two "
 "percent, from a derivation, with NO carried parameter. Ours matches 99 in sample and 90 held out; the "
 "two rankings agree with each other 88 of 106.** *So ν is NOT a reparametrisation of his spectrum, and "
 "the prediction of register 1453 — agreement at q = 0, parting at q > 0 — is REFUTED: the eighteen "
 "disagreements split ten at q = 0 and eight at q > 0, no pattern. Gap 2 is not where the chains part.*"),

(1455, "AND HIS ERRORS ARE ONE-SIDED: HE NEVER BRINGS A GROUP IN LATE, ONLY EARLY.",
 "*Of the nineteen wrong picks, THIRTEEN choose a subshell of HIGHER M than the observed one and NONE "
 "chooses a lower one.* **That is the signature of a systematically low onset formula rather than of "
 "scattered inaccuracy — and the subshell he wrongly picks has even M in 74% of cases against a 36% "
 "even-M share of all candidates offered.** *The person's reading was that he sought a global solution "
 "where none can exist. Tested against the alternative — that the misses cluster where a single a cannot "
 "work — the reset-point explanation is real but weaker: seven of nineteen at our reset points against a "
 "17% base rate, P = 0.018.* **The parity signal is the stronger one and the reset enrichment is "
 "probably downstream of it, since the resets are where groups turn over.**"),

(1456, "GAP 5 CLOSED: THE PARITY TERM IS IN HIS OWN §2, AND HIS DERIVATION DROPS IT.",
 "*His E = 0 condition √(2ZR) = M gives Z = M³/6 for the onset of each group, which runs 3.7% low on odd "
 "M and 9.9% low on even M against the observed block starts 1, 3, 5, 13, 21, 39, 57, 89.* **But in his "
 "own §2 he quotes Klechkovski–Hakala: Z = K(n+ℓ) + 1 with K(x) = (1/6)x(x² + 2 − 3µ(x)) and "
 "µ(x) = x mod 2 — and that reproduces EVERY onset EXACTLY, all eight, no error.** *Z = M³/6 is the "
 "leading asymptotic of the same expression with the µ term discarded. Split by parity: odd M loses "
 "−M/6, even M loses +M/3 — twice the magnitude and the opposite sign, which is exactly the 3.7% against "
 "9.9%, and exactly why three quarters of his wrong picks are even-M groups brought in early.* **So the "
 "parity structure is exact combinatorics that he CITES and does not DERIVE, while the smooth cubic is "
 "what his symmetry argument produces. A single smooth closed form cannot represent an onset sequence "
 "whose increments are 2, 2, 8, 8, 18, 18, 32 — which is the person's reading made exact.** *And it "
 "bounds the comparison honestly: 87 of 106 is what his ASYMPTOTIC achieves, not what his approach can. "
 "Restoring µ would repair most of the thirteen early picks. Where this work advances is narrower and "
 "real: the corridor is built from node counts with no asymptotic step anywhere, so there is nothing to "
 "drop, and the parity is carried automatically because p ≡ M + 1 (mod 2) is built into the coordinates "
 "rather than approximated.*"),
]

P = pathlib.Path("/home/claude/work/REGISTER-DATA.md")
s = P.read_text(encoding="utf-8")
nums = [int(m) for m in re.findall(r"^ {0,3}(\d{3,4})\. \*\*", s, re.M)]
if max(nums) != 1453:
    print(f"REFUSING: highest is {max(nums)}, expected 1453"); sys.exit(1)
blocks = []
for n, head, body in ENTRIES:
    t = f"{n}. **{head}** {re.sub(r'\s+', ' ', body).strip()}"
    b = "\n".join(textwrap.wrap(t, 97, initial_indent=" ", subsequent_indent=" ",
                                break_long_words=False, break_on_hyphens=False))
    if b.count("**") % 2:
        print(f"ODD ** in {n}"); sys.exit(1)
    blocks.append(b)
P.write_text(s.rstrip("\n") + "\n\n" + "\n\n".join(blocks) + "\n", encoding="utf-8")
print(f"appended {len(blocks)} entries, 1454–{ENTRIES[-1][0]}")
