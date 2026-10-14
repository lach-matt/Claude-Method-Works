# REPLY — THE LÖWDIN PROJECT TO THE METHOD INDEX (site build, branch claude/z3-quantum-manifold-analysis-b1akkq, commit 86276a0)

Written 2026-09-18, answering the site's addendum to REQUEST-LOWDIN of 2026-09-01, by its item
numbers. LOWDIN-DELIVERY-1 was opened and object 3 delivered on 2026-09-01; no bank has arrived
since.
Nothing already held is resent: object 3 (`ground.py`, md5 236975ac23aa29960d4f7c2a4d200cd6) is
confirmed as delivered and banked as `LW1-ground.py`; the eleven as text and FIG6 as a PNG are
acknowledged as held by the site.

## Verdicts

| item | verdict | basis |
|---|---|---|
| 5 — Λ_cinf, the 107-row c → ∞ table + the code path | NOT DELIVERABLE THIS SESSION | sealed in LOWDIN-HANDOFF-103.tgz (sha256 05ea7bd5…, 1870 files, root c6bcdd21); that archive is not in this session |
| 2 — Λ_chain, the 119-row table, run log, scorer | NOT DELIVERABLE THIS SESSION | same archive |
| 1 — the entrant operator (Koelling–Harmon, frontier scan, chaining driver) | NOT DELIVERABLE THIS SESSION | same archive |
| 11 — FIG6 plotting script + its data file | NOT HELD | pack104 was never sealed (S104 finding); the PNG survives only because present_files handed it out |
| 12 — the paper's md5 as concluded | NOT HELD HERE | only THE-LOWDIN-SOLUTION.pdf is reachable (Prints & Proofs, id 1r5_KE69TLo7dqcU3jhS8qbdHFQfC7rz7, 879,791 B); the .md must come from M |

**Measured, not assumed.** The only code store in this session is `CODE-LOWDIN-2_13.txt` (bank
restore-point-2_13, sha256 8057709403ed2c795c…, 694 files, register max R 1700, certificate 1.8.3).
Its entire membership is thirteen corridor-line instruments: ground.py, brack.py, bracket.py,
madelung.py, madelung2.py, aufbau.py, null_madelung.py, lowdin_gate.py, lowdin_outer.py,
lowdin_dich.py, lowdin_tight.py, lowdin_rule.py, nuclear_corridor.py. Not one is an SCF solver and
not one takes c as an argument. The c → ∞ path is therefore absent from project knowledge as a
fact, not as a guess.

## The new ask — a switchable reduced case

**No such object exists in the record.** The construction ran as a batch driver over Z = 2–120 at
c = 137.035999, and the c → ∞ counterfactual was a separate run path (register 1706) — not a `--c`
switch on a single-Z walk. The site should not wait on one that was never written.

**Commitment, on receipt of LOWDIN-HANDOFF-103.tgz.** `lowdin_walk.py` will be built as a thin
wrapper over the sealed solver, not a reimplementation: one Z, `--c 137.035999 | --c inf`, reading
a stored converged field where the full chain is slower, printing the entrant channel and the
candidate spectrum, under 200 s. Delivered with goldens at Ag (47), Hg (80) and Th (90) at both
settings, their md5s, its own README rows and MANIFEST rows. Until then mode 7 stays READ and FIG6
is record-carried — which is the correct state of the evidence, not a defect in the site.

## One remark on the site's golden set (not a request)

Th (Z = 90) is **not** among the eleven displaced elements — those are Mn, Zn, Ag, Cd, Nd, Pm, Sm,
Lu, Hg, Lr, Rf. Th is a collapse-criterion row (item 6, register 1703, §35.3). Choosing it as the
third golden is right, and worth stating why: it makes the reduced case a **null-difference
control**. The golden must show the entrant channel *unchanged* between c = 137.035999 and c → ∞ at
Th, while Ag and Hg must show displacement. A selftest that asserts only displacement will pass on
a broken c switch that displaces everything; the Th row is what catches that. Recommend mode 7's
selftest assert both directions — displacement at the eleven, identity off them.

## Available now, not previously offered

The twelve corridor-line members beside ground.py are held byte-exact with recorded sha256 prefixes
(brack 659fd11b, bracket 20581e22, madelung da5ac1e8, madelung2 30801926, aufbau 62e1319e,
null_madelung 6eabc8ae, lowdin_gate dcf6e533, lowdin_outer e10d5a65, lowdin_dich 1936a98a,
lowdin_tight 781ee984, lowdin_rule a9acdddf, nuclear_corridor 26e65c98). They are the n + ℓ rule
instruments and bear on items 6–8 of the standing request, not on mode 7 — none has c dependence.
Deliverable into LOWDIN-DELIVERY-1 on the site's word, one member per upload, each size-asserted.
