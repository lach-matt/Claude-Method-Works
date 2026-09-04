#!/usr/bin/env python3
"""register_1434_1444.py — append this session's entries to REGISTER-DATA.md.

Checks markup parity before writing, and refuses if the next number is not 1434,
so a rerun cannot double-append.
"""
import pathlib, re, sys, textwrap

ENTRIES = [
(1434, "THE CORRIDOR AND THE OBJECT IN IT ARE ONE EQUATION, AND THE PLACEMENT RULE FALLS OUT OF BALANCING THEM.",
 "*The person's reframing, tested: the corridor L(Z) < a < U(Z) and the value carried through it are not "
 "a constraint plus a heuristic for choosing inside it, but two halves of one equation.* **Intersecting "
 "the corridors and asking only where the running intersection empties gives FOURTEEN forced moves at "
 "Z = 37, 42, 43, 45, 55, 58, 64, 65, 80, 91, 96, 97, 103, 104 — identical to register 1401 element for "
 "element, with zero false positives — and nothing was supplied: no rule, no threshold, no parameter.** "
 "*The eight recorded a values then all sit on an endpoint of their own corridor, seven at L and "
 "protactinium at U, so register 1403 falls out of the same arithmetic rather than being imposed on top.* "
 "**The four not forced are Li 3, K 19, Tl 81 and Fr 87.** `balance.py`."),

(1435, "PROXIMITY IS THE TRIGGER, AND THE THRESHOLD IS NOT FITTED — IT IS ZERO.",
 "*Register 1407 measured the margin PER ELEMENT and demoted proximity to a signal: a best threshold "
 "reaching 91% against an 87% do-nothing baseline, with nine resets missed.* **Measured instead on the "
 "RUNNING INTERSECTION — the window a actually has to sit inside — the trigger fires at fourteen of the "
 "eighteen resets with zero false positives, 96% against an 83% baseline, and the threshold is not a "
 "scanned number but zero.** *So the law's strict inequality needs no proximity TERM: proximity IS the "
 "inequality reaching equality, which is what a corridor emptying is.* **This is not a tenth condition "
 "scanned after nine failed — nothing was searched over; it was derived from 1434's balance.** *And "
 "1407's own quantity cannot be reproduced from the intervals: its ninety-nine is the CEILING-BEARING "
 "set, not the seventy-three with both bounds finite, and none of its figures follow from corridor "
 "widths. The margin it scans is undefined in the register and is most likely trajectory-dependent — the "
 "distance from the HELD a to the nearer bound. Define it or withdraw the r = +0.64.*"),

(1436, "THERE ARE EIGHT ADJACENT HANDSHAKES, NOT FOUR, AND THEY SPLIT ON A CRITERION NO REGISTER STATES.",
 "*Computed from the exact intervals: eight places where one element's ceiling is exactly the next's "
 "floor, or the reverse — Mo/Tc at 1, La/Ce at 1/√2, Eu/Gd at 1/√2, Gd/Tb at 1/√2, Th/Pa at 1/(√3−1), "
 "Am/Cm at the same, Cm/Bk at the same, Lr/Rf at 1.9841.* **In four, BOTH members are forced resets — "
 "Mo/Tc, Gd/Tb, Cm/Bk, Lr/Rf, which is exactly register 1404's list. In four, only the second is — "
 "La/Ce, Eu/Gd, Th/Pa, Am/Cm.** *That is what 1404's phrase about the second reset being forced is "
 "describing, and why its enumeration found four rather than eight.* **And actinium's floor, thorium's "
 "floor and protactinium's ceiling are ONE surd, so 1403's reading that protactinium takes U and 1409's "
 "that its value is assigned at the actinium opening name the same value from two sides — they were "
 "never in conflict.**"),

(1437, "THE NULL OF 28 IS RETIRED: PLAIN MADELUNG SCORES 96, AND THE TWO RULES FAIL ON ALMOST DISJOINT SETS.",
 "*The handoff carried the Löwdin result as 99 of 106 against a null of 28. The 28 came from a broken "
 "step extractor, was known to be broken at the time, and was carried anyway — the recurring fault of "
 "quoting a check before its null is known, landing on the largest claim in the work.* **Recomputed on "
 "the SAME 106 clean steps: Madelung scores 96 of 106 conditionally, given the observed configuration at "
 "Z−1, and 94 free-running. So the comparison is 99 against 96 — three steps in a hundred and six, not "
 "seventy-one.** *But the two are NOT nested. Madelung misses Mo, Rh, Pd, La, Gd, Au, Ac, Th, Cm, Lr; "
 "the corridor misses Mn, Tc, Ce, Gd, Pa, Cm, Rf; they overlap in TWO.* **The corridor is right at eight "
 "elements where Madelung is wrong and Madelung at five where the corridor is wrong. Two rules of "
 "near-identical accuracy failing on disjoint sets are different objects, which is a better statement "
 "than a score.** `null_madelung.py`."),

(1438, "THE SCORER IS REBUILT AND THE 99 IS NOW MEASURED RATHER THAN REPORTED.",
 "*Rebuilt from register 1413's specification with nothing but the law, the candidate generator, the "
 "higher-n tie-break and the exact corridors.* **The handshake placement gives 99 of 106 and the lower-n "
 "tie-break gives 91, both matching the register exactly, and the score is invariant for every "
 "initialisation from 0.05 to 5 at lithium — the one place the corridor determines nothing also "
 "determines nothing about the result.** *Six of the seven misses match: Mn 25, Tc 43, Ce 58, Gd 64, "
 "Pa 91, Cm 96 in both, with a swap at the ends — this rebuild misses B 5 and gets Rf 104, the register "
 "the reverse.* **Two things do not reproduce: the handshake makes fifteen moves against the register's "
 "ten, and per-block ascent gives 94 under 1409's literal description or 95 if ceilings are also "
 "intersected, against a stated 97.** *That the score matches while the move count does not is the "
 "expected shape under 1402: the values are invariant and the count is rule-dependent.* `scorer.py`, a "
 "REBUILD — see PROVENANCE.md."),

(1439, "MANGANESE AND TECHNETIUM ARE ONE ALGEBRAIC OBJECT, AND THE CORRIDOR ADMITS THE ANSWER IT DOES NOT TAKE.",
 "*The two residual misses put through the cypher — the geometry of two crossing intervals read as its "
 "algebra.* **At manganese the entrant is 4s at q = 1 against 3d at q = 5; at technetium 5s at q = 1 "
 "against 4d at q = 5. In both, BOTH contenders sit at exactly half capacity, so every radicand is a "
 "half-integer and the contest collapses to a_cross = Δn/(√(p_g + ½) − √(p_r + ½)) — giving "
 "1/(√3.5 − √0.5) = 0.859312 and 1/(√4.5 − √1.5) = 1.115355, the same form at consecutive p with "
 "Δn = 1.** *What looked like two scattered failures is one surd family evaluated at two points, which "
 "is Λ_cross's own statement that a_cross is fixed by the pair.* **And both crossings lie STRICTLY "
 "INSIDE their own corridors while a sits at the floor, below them: the value that gets the step right "
 "is admitted by the law and not taken by the placement.**"),

(1440, "THE LAW'S CEILING OVER PLACEMENTS IS AT LEAST 100, AND THE 99 IS A PROPERTY OF THE TRAJECTORY.",
 "*Same law, same corridors, only where a sits inside them.* **At the floor 99 of 106; at the midpoint "
 "100, which fixes technetium; at the ceiling 93. Seven steps of spread over identical constraints.** "
 "*So the residue is not the law's, and the record's own handshake placement is not the best one "
 "available inside its own corridors.* **Register 1412's split now carries a number: the law admits at "
 "least 100 and the trajectory delivers 99.** *Nobody has asked what the best admissible placement "
 "scores — only what two particular rules score — and given 1402's finding that the reset COUNT is "
 "rule-dependent, the SCORE being rule-dependent too is the thing to say out loud rather than leave "
 "implicit.*"),

(1441, "THE EIGHTH JANET BLOCK IS TRUNCATED, AND THAT IS THE SUBJECT'S EDGE RATHER THAN THE COLLECTION'S.",
 "*Register 1415 finds the binding floor in the NEXT block 89% of the time — a subshell is bounded above "
 "within its block and aimed by the block that has not yet opened. I proposed supplying block nine so "
 "the rule would be total across the last twenty steps.* **The person refused it, and correctly: a block "
 "with no elements in it is an INVENTED CELL, and the proposal was that fault dressed as a test.** *Four "
 "of the nine floor exceptions sit in block eight — Ac 89, Th 90, Cm 96, Lr 103 — four of twenty steps "
 "against five of the other eighty-six, because for those steps there is nowhere else for the floor to "
 "come from.* **So the answer to the Löwdin challenge is not global and cannot be: it runs per block, "
 "takes its ceiling from within and its floor from the block ahead, and TERMINATES, because the eighth "
 "block has nothing ahead of it and is itself short. 1409's failure of global ascent was the first sign "
 "of it.** *And 1422's E = k reads as the index stating its own terminus rather than as a condition to "
 "be met at 120.*"),

(1442, "AND WHAT THE ROLLBACK DEMONSTRATED, WHICH IS REGISTER 1373 AT THE SCALE OF THE PROJECT.",
 "*The 1.6.1 container reverted to register 1370. Its compendium tail, its queue, `xray_index.py`, "
 "`traj_index.py`, the captures, twelve scripts and a staged archive were all lost.* **What survived is "
 "exactly what had been written into a transcript as prose — the sixty-three registers — and they "
 "survived because the register is where the reasoning was put rather than where the output was "
 "stored.** *The compendia are recoverable from the register and the register is not recoverable from "
 "them; that is a durability property earned the hard way rather than a preference.* **But the "
 "refinement matters for practice: the register survived because it was COPIED OUT, and the durability "
 "belongs to being outside the container. A compendium pasted into a transcript would have survived "
 "equally.** *So: copy out continuously, and prefer the artefact carrying the reasoning when only one "
 "can be copied. Anything rebuilt from a register is labelled REWRITTEN and never restored — "
 "PROVENANCE.md holds the classification for every file in this tree.*"),

(1443, "THE CORRECTIONS THIS SESSION'S COMPUTATION OWES THE REGISTER, INCLUDING ONE OF MY OWN FLAGS WITHDRAWN.",
 "**1391: n = 47, not 45 — the three region offsets reproduce exactly at 3.798, 4.595 and 5.298, and the "
 "quoted spread of 0.108 IS the forty-seven-element figure, since dropping any two tightens it to "
 "0.097.** *Scandium and titanium are the two largest deviations once the L1M2,3-blended elements are "
 "excluded as the regions imply.* **1390: monotone except at palladium alone, 0.1756 → 0.1753; the "
 "endpoints and the never-exceeding-the-limit half both hold.** **1401: the four unforced resets are not "
 "period openings — thallium is not one — they all open a SUBSHELL, but so do eight of the fourteen "
 "forced, so the property is necessary and not sufficient and the four remain unexplained.** **1415: "
 "fifteen ceiling exceptions, not eleven — eleven s-against-s plus four d-against-s at Mo, Rh, Pd and Au "
 "— so that set is not homogeneous; and nine floor exceptions, not six, all of which ARE f or d "
 "intruders.** **1417: seven of twenty systems close, not three; the monotone-chain filter was asserted "
 "rather than computed.** **1396: the entry splits the ELEVEN absent cells and scores against the TWELVE "
 "donor steps, and its list of nine names seven — Pr and Tb are omitted — though the base rate itself "
 "reproduces exactly at 3 of 12 against 36 of 94.** *1419 needs NO correction and my flag against it is "
 "WITHDRAWN: it reports two different base indexes and all four figures are right — replace on (n, ℓ, q) "
 "at 24 cells and box 48 → 56, adjoin on (n, ℓ) at 18 cells and box 24 → 168.* *1409 and 1411 likewise "
 "need only a clause: seven openings counts the initial placement at lithium, six counts re-placements.* "
 "**1385's eighty-five is UNVERIFIED — no rule yields it and the nearest gives eighty-six — and 1403's "
 "and 1409's eight a values are RECONSTRUCTIONS held in HANDOFF.md, not measurements, so both entries "
 "claim agreement with a previously computed trajectory.**"),

(1444, "TWO SMALLER OBJECTS RECOVERED IN PASSING, ONE ALGEBRAIC AND ONE ABOUT A DATABASE COLUMN.",
 "**The corridor combination collapses to a single condition on Nilsson's μ: with β = −κℏω₀μ and "
 "α = 2κℏω₀, 4β + α = 2κℏω₀(1 − 2μ), vanishing exactly at μ = ½.** *The published values straddle it — "
 "μ = 0.60 in the 50–82 proton shell gives it negative, which is the sense both of that shell's pairs "
 "demand, and μ = 0.42 in the 82–126 neutron shell gives it positive, in the one shell demanding both.* "
 "**So C3's falsifier is derivable from the field's own parameters rather than merely consistent with "
 "them.** *And NIST's Blend column is a MEMBERSHIP condition, not a data-quality annotation: where it "
 "flags KL2,3 or L1M2,3 the two files carry the SAME experimental value, so their difference is "
 "identically zero — twelve manufactured zeros in the doublet, and a silently widened comparison set "
 "that made 1391's scandium-titanium finding vanish until the flag was applied.* **That is the "
 "separation hypothesis in a place it had not been applied: a result conditioned on a coordinate holds "
 "exactly when that coordinate separates, and a database's own flag can BE the coordinate.**"),
]

P = pathlib.Path("/home/claude/work/REGISTER-DATA.md")
s = P.read_text(encoding="utf-8")
nums = [int(m) for m in re.findall(r"^ {0,3}(\d{3,4})\. \*\*", s, re.M)]
if max(nums) != 1433:
    print(f"REFUSING: highest register is {max(nums)}, expected 1433"); sys.exit(1)

blocks = []
for n, head, body in ENTRIES:
    text = f"{n}. **{head}** {re.sub(r'\s+', ' ', body).strip()}"
    b = "\n".join(textwrap.wrap(text, 97, initial_indent=" ", subsequent_indent=" ",
                                break_long_words=False, break_on_hyphens=False))
    if b.count("**") % 2:
        print(f"ODD ** COUNT in {n} — audit 12 would fail"); sys.exit(1)
    blocks.append(b)

P.write_text(s.rstrip("\n") + "\n\n" + "\n\n".join(blocks) + "\n", encoding="utf-8")
print(f"appended {len(blocks)} entries, 1434–{ENTRIES[-1][0]}; markup parity even on all")
