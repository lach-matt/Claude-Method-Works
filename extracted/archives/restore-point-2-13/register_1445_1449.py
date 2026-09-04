#!/usr/bin/env python3
"""register_1445_1449.py — the evening's negatives, registered before anything builds on them."""
import pathlib, re, sys, textwrap

ENTRIES = [
(1445, "THE 99 WAS FITTED, NOT GENERATED: HELD OUT THE WALK SCORES 90 AND PLAIN MADELUNG BEATS IT.",
 "*`scorer.py` placed a using each step's OWN corridor — and a corridor is built by `brack.py` FROM the "
 "observed entrant at that step, so the answer was setting the parameter that produced the answer.* "
 "**Held out properly — a placed only from corridors already revealed, the step predicted, then the step "
 "revealed — the score falls from 99 of 106 to 90 of 106.** *The nine steps the leak was carrying are "
 "the recalibrations: Li 3, Rb 37, In 49, Cs 55, Hg 80, Tl 81, Fr 87, Lr 103, Rf 104, which is exactly "
 "where a is re-placed and where the corridor's endpoint is read off the answer.* **And plain Madelung, "
 "which takes no free parameter at all and was always honest, scores 96. So out of sample the corridor "
 "law LOSES to the rule it was meant to explain, by six steps.** *What survives untouched: the corridor "
 "is non-empty at 106 of 106, which is a result about the FORM and is what the nuclear corridor's "
 "emptiness contrasts against. Every lost step is a placement, not a law failure.* **The Löwdin "
 "challenge asks for the index to be populated WITHOUT spectral observation. On that question the "
 "standing of this work is 90 against a null of 96, and it should be quoted that way until it is not.**"),

(1446, "AND THE OBSERVATIONAL EDGE IS 102, NOT 108 — THERE ARE FOUR EDGES, NOT TWO.",
 "*NIST ASD returns five rows for Rf–Og: it holds no neutral ground configurations past Z = 108, and "
 "`ground.py` matches all five exactly, so our table is faithful to the source.* **But optical "
 "spectroscopy ends at nobelium, Z = 102. What NIST lists for 103 to 108 is calculation and chemical "
 "homology — every ionisation energy in those five rows carried a theoretical or interpolated flag, "
 "which is the row telling us what kind of row it is.** *So: the subject is 118 synthesised, 120 on "
 "Janet's count; NIST's listing stops at 108; observation stops at 102; and the collection is faithful "
 "to the listing.* **Register 1426's fault reads 'check whether the limit is the subject's or the "
 "collection's' — the answer here is neither, and conflating the RECORD's edge with the collection's is "
 "a third error.** *Graded by observational status the walk is 93 of 100 against measurement and 6 of 6 "
 "against calculation. All seven misses lie in the observed region and the calculated region is perfect, "
 "which is the part to be careful about rather than pleased by: agreement with Dirac–Fock and homology "
 "is agreement with a METHOD, and those methods already encode orbital-ordering regularities.*"),

(1447, "THE UNIT IS THE SUBSHELL-FILLING RUN, NOT THE JANET BLOCK, AND ONE a SERVES IT IN 31 OF 31.",
 "*The person's proposal — run the solution per Janet block, with a Pauli stepping in the algebra.* "
 "**The stepping is exact and visible: while q walks 0 to cap the entrant's radicand p + q/cap advances "
 "by 1/cap per step while its rivals sit still, and across the 3d row the ceiling stays at 1/√2 "
 "throughout.** *But the block is too coarse — blocks 5 to 8 have EMPTY corridor intersections, block 5 "
 "demanding a > 1.0000 from rubidium and a < 0.7071 from the 3d steps at once, so one a per block is "
 "impossible there.* **Grouped instead into runs of consecutive steps entering the same subshell: "
 "thirty-one runs, and the corridors intersect within EVERY ONE. One a serves a whole filling run, 31 of "
 "31.** *And four subshells are interrupted mid-fill — 3d by 4s at 25, 4d by 5s at 43, 4f by 5d at 64, "
 "5f by 6d at 96 — which are precisely the four misses the half-capacity screen selects. The run is "
 "interrupted exactly where the filling subshell reaches half capacity, so the structural statement and "
 "the algebraic one are one event seen twice.* **This also flags 1409: per-block ascent cannot be "
 "corridor-respecting in blocks 5 to 8, so its 'zero violations' needs defining.**"),

(1448, "BUT THE RUN DOES NOT GENERATE, AND THE PER-ATOM FIXED POINT IS VACUOUS — A CHECK I BUILT WITHOUT ASKING WHETHER IT COULD FAIL.",
 "*Two placements tried, both held out.* **Per-run placement scores 35, 36 and 20 at the run window's "
 "floor, midpoint and ceiling, and 90 only when it degenerates into the per-step rule. The loop places a "
 "on the corridor of the law's OWN guess — and a corridor is by construction the set of a making that "
 "entrant minimal, so the placement confirms whatever it was given and cannot correct it.** *Then the "
 "person's calibration correction: every constant must come from the same atom, so carrying a across "
 "species is a pooled parameter and 'the trajectory of a' is a category error.* **Calibrating per atom — "
 "a from that atom's own corridor and its own ℓ via the entry point √(ℓ(ℓ+1)/2) — determines 3 of 106 "
 "steps, all three WRONG, with 101 ambiguous.** *The self-consistency test cannot fail: asking whether "
 "a inside a candidate's corridor selects that candidate is asking whether a set contains its own "
 "defining property. `contingency.py` exists in this tree to catch exactly that and I did not run it on "
 "my own construction.* **What the failure names is a BOOTSTRAP: a is fixed by the entrant's corridor "
 "and the entrant is what a determines. Carrying a across species hid the loop by importing the value "
 "from elsewhere; per-atom calibration is right and makes it visible.**"),

(1449, "THE SEVEN MISSES CLASSIFY COMPLETELY, AND THE ONE WITHOUT A MECHANISM IS THE ONE WITH A REAL SOURCE.",
 "**Four are the half-capacity crossing — Mn 25, Tc 43, Gd 64, Cm 96 — where both contenders sit at "
 "exactly half capacity so every radicand is a half-integer and the contest collapses to "
 "Δn/(√(p_g+½) − √(p_r+½)), and the crossing lies INSIDE the corridor while a sits at the floor below "
 "it.** *Eight steps in the walk have a rival at exactly half capacity; the four whose crossing is "
 "admitted by the corridor are the four misses, and the four whose crossing is outside — Mo, Rh, Pd, Au "
 "— the walk gets right. P = 0.00001, and the witness exists.* **Two are node-free entrants with no "
 "floor at all — B 5 and Ce 58 — which is register 1414 rather than a failure.** *That leaves Pa 91, and "
 "it is the ONLY miss among the twelve donor steps: source 6d, target 5f, q = 2. The one step no "
 "mechanism accounts for is the one step where the cell is a transition with a real source and the "
 "walk's machinery records only the target, which is register 1420's defect arriving as a prediction "
 "rather than a description.* **One element is a signal and not a result — but the mechanism was named "
 "before the coincidence was found, so it is not a pattern read out of my own output.**"),
]

P = pathlib.Path("/home/claude/work/REGISTER-DATA.md")
s = P.read_text(encoding="utf-8")
nums = [int(m) for m in re.findall(r"^ {0,3}(\d{3,4})\. \*\*", s, re.M)]
if max(nums) != 1444:
    print(f"REFUSING: highest register is {max(nums)}, expected 1444"); sys.exit(1)
blocks = []
for n, head, body in ENTRIES:
    text = f"{n}. **{head}** {re.sub(r'\s+', ' ', body).strip()}"
    b = "\n".join(textwrap.wrap(text, 97, initial_indent=" ", subsequent_indent=" ",
                                break_long_words=False, break_on_hyphens=False))
    if b.count("**") % 2:
        print(f"ODD ** COUNT in {n}"); sys.exit(1)
    blocks.append(b)
P.write_text(s.rstrip("\n") + "\n\n" + "\n\n".join(blocks) + "\n", encoding="utf-8")
print(f"appended {len(blocks)} entries, 1445–{ENTRIES[-1][0]}")
