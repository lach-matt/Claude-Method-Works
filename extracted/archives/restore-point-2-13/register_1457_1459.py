#!/usr/bin/env python3
"""register_1457_1459.py"""
import pathlib, re, sys, textwrap

ENTRIES = [
(1457, "δ = a√p IS NOT MERELY WRONG, IT IS IMPOSSIBLE — AND THE WKB ROUTE TO THE SQUARE ROOT IS CLOSED.",
 "*The last live candidate for giving ν a physical derivation was the WKB integral, where the momentum "
 "is itself a square root and where Belokolos's α came from. It fails three independent ways.* "
 "**STRUCTURALLY: in quantum defect theory δ is BOUNDED as n → ∞, and that boundedness is what makes a "
 "Rydberg series converge to the ionisation limit and why ONE δ per channel suffices rather than one per "
 "level. a√(n−ℓ−1) DIVERGES. A bounded quantity cannot equal a divergent one, and no refitting of a "
 "repairs it.** *EMPIRICALLY: across the 83 held channels spanning nine or more values of n, the median "
 "|δ| is 0.1392 and the median SPREAD over the whole series is 0.0129. He I 1sns ³S runs n = 3 to 36 "
 "with |δ| = 0.2965 and spread 0.0164 — flat to five percent — where √p would demand a factor of 5.8.* "
 "**AT THE SOURCE: Belokolos states in his own §3.2 that the neutral-atom potential goes as −1/r at "
 "large r, giving the Rydberg condensation, WHEREAS THE TIETZ POTENTIAL DECREASES MORE RAPIDLY. A "
 "potential with no Coulomb tail supports no Rydberg series, so the WKB integral cannot produce a defect "
 "even in principle.** *Register 1416 had only the numerical refutation and concluded the failure was "
 "MINE rather than 1341's. It is the relation's.* **So ν is NOT an effective quantum number. It is an "
 "ordering functional, its square root has only the closure axiom behind it — the demand that the "
 "crossing be linear in the f-values — and no physical candidate remains.**"),

(1458, "AND THE LÖWDIN COMPLETION CRITERION IS INCOMPATIBLE WITH THE LAW: THE TWO ARE DIFFERENT OBJECTS.",
 "*The handoff states that the challenge completes when the work populates Λ_spectra with δ per channel. "
 "There is no route from ν to δ — not through 1341, not through the WKB, not through the Tietz "
 "potential.* **The domains are almost disjoint, measured: of 114 neutral channels comparable with a "
 "walk step, the walk's entrant (n, ℓ) falls INSIDE the channel's own range in FIVE cases — Li 2s, "
 "Na 3s, K 4s, Al 3p, Ga 4p, all block openings where the ground configuration happens to be the first "
 "member of a series — and OUTSIDE it in 109.** *ν asks which subshell the last bound electron enters at "
 "the ground configuration; δ measures an outer electron in a series running to the ionisation limit. "
 "Register 1416 said this in words; it is now counted.* **Three ways out and none yet chosen: narrow the "
 "criterion, since Löwdin's question was about ORDERING and δ per channel was this work's addition; keep "
 "the criterion and change the law, which needs a Coulomb tail and a core phase shift and would not "
 "inherit the corridor; or keep both and drop the join.** *The third is what register 1341 actually "
 "claims — that they SHARE AN INDEX, not that one number equals the other — and on that reading queue "
 "item A5b is not open but CLOSED. NU-AND-DELTA.md holds the comparison in full.*"),

(1459, "δ IS PER CHANNEL ON A MONOTONE (ℓ, BLOCK) GRID — WHICH IS A RE-COORDINATISATION, NOT A JOIN.",
 "*The person asked whether δ might be per Madelung group or per Janet block rather than per channel. "
 "Tested by variance decomposition within fixed ℓ, against a permutation null that preserves group "
 "sizes.* **The Janet block explains 87% of the within-ℓ variance against a 5.5% null, and δ rises "
 "MONOTONICALLY with block at every ℓ — s: 0.257, 0.805, 1.525, 2.178, 3.368, 4.363; p, d and f "
 "likewise, without exception.** *But δ is NOT constant within a cell: the scatter inside each "
 "(ℓ, block) cell is a median FOURTEEN TIMES the channels' own fitted spread, and only two of "
 "twenty-six cells approach constancy. So δ remains per channel.* **The finding is therefore about "
 "COORDINATES rather than about atoms: ℓ and the Janet block are both monotone chains for δ, which by "
 "the work's own rule makes each a determined axis, and (block, ℓ) is a better coordinate system for "
 "Λ_spectra's VALUES than Z is — coarser, monotone in both directions, and explaining most of the "
 "variance.** *The mechanism is textbook and not ours: δ rises with block because more core shells mean "
 "more penetration. And it does NOT rescue the join — a also rises with block, but at r = +0.625 over "
 "four points, with a's rise manufactured by per-block ascent and δ's caused by penetration. Register "
 "1398 is the standing warning: a shared trend indicates a shared mechanism only when the coordinates "
 "generating it are the same, and here they are not.* **New queue item: test Λ_spectra's closure on "
 "(block, ℓ, charge) against the current (Z, c, ℓ). By A.erel a relabelling is free to try.**"),
]

P = pathlib.Path("/home/claude/work/REGISTER-DATA.md")
s = P.read_text(encoding="utf-8")
nums = [int(m) for m in re.findall(r"^ {0,3}(\d{3,4})\. \*\*", s, re.M)]
if max(nums) != 1456:
    print(f"REFUSING: highest is {max(nums)}, expected 1456"); sys.exit(1)
blocks = []
for n, head, body in ENTRIES:
    t = f"{n}. **{head}** {re.sub(r'\s+', ' ', body).strip()}"
    b = "\n".join(textwrap.wrap(t, 97, initial_indent=" ", subsequent_indent=" ",
                                break_long_words=False, break_on_hyphens=False))
    if b.count("**") % 2:
        print(f"ODD ** in {n}"); sys.exit(1)
    blocks.append(b)
P.write_text(s.rstrip("\n") + "\n\n" + "\n\n".join(blocks) + "\n", encoding="utf-8")
print(f"appended {len(blocks)} entries, 1457–{ENTRIES[-1][0]}")
