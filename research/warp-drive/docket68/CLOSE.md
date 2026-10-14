# DOCKET 68 — close-out: information without transit

M's order (M-RULINGS item 40, "2 then 1 please"): D68 wave 4 first, then this close and the Q-1s prior-art gate.

DOCKET 68 asked M's question as one sentence (CHARTER.md): *is there a channel, beyond linear quantum mechanics or
beneath geometry, in which Bob's statistics depend on Alice's choice?* It tested M's thesis that warp travel "costs
little because we are only relying on the communication of information between two entangled locations in
spacetime". Every value below is its owner's. `ledger.py` asks each one at run time and reads this record's section
headings; nothing here is typed as a result.

## 1. The answer, as the board holds it

**Not found, and not excluded.** O9 stays OPEN. Each branch is graded by its owner:

- **Linear, local quantum mechanics.** No channel: Alice's choice carries 0 bits to Bob (`nosig.py`). Teleportation
  needs the two classical bits, at c (`transit.py`).
- **Beyond linear (H-SETTLE).** A Weinberg-type drift signals (`nlcontrol.py`, `settle.py`).
  - Under H-SETTLE × H-FRAME, O-BITS is REMOVED-IF {W2, F1}. Its support 1 (N_EPS) is ADMISSIBLE at the READ limits at
    most cells, meaning not excluded and not found.
  - At 1 AU, N = 7 and N = 1e3, the READ limits EXCLUDE support 1, given the window premises W_W2R. There, support 2
    (N_W2ANC, UNEVALUATED) still carries the removal (`combine.py`, `settle.window_read`; ledger O9).
  - The KR family permits zero superluminal signal (`settle.py`).
- **Beneath geometry (H-IT).** It is read three ways (ITB, ITE, ITJ). None removes an obstruction outright (`combine.py`,
  M-D68-C9).
- **The corridor as a coupling (wave 3, Step 1c).** Under H-LOCALITY the coupling is the channel itself: it is
  retarded, and it completes at L/c or later (`step1c/coupling.py`).
  - Without locality, H-NONLOCAL-COUPLING (M's branch) needs H-FRAME.
  - Present no-signalling tests do not exclude it at the device's strength, under named conditions
    (`step1c/nonlocal.py`).
- **What arrives.** On M's ruling, what arrives is the defining information, H-INFO-SHAPE (M-D68-1). The substance comes
  from the seat (M-D68-5), so O-MATTER is relocated to O-SEAT, which stays OPEN at the D25 gate: binder P, unmeasured at
  Proxima.

## 2. What each wave established (seated)

- **Wave 1** (`ledger.py` section 7): the seven hypotheses in combination (`combine.py`, 8,191 variants), H-FRAME, Q-1
  and Q-1s.
- **Wave 2** (section 7b): the Weinberg-family limits READ, vacuum entanglement as pair supply, and the S5 seat route.
- **M's DOCKET 66 rulings** (section 8b): the Gott bound corrected in the paper, H-TURN-CROSSING, and D68 re-graded.
- **Wave 3 and Step 1b** (section 8c):
  - the A–B coupling, the twelve criteria, H-12Q and H-SEATRANK;
  - the balanced equation I(A, before) = I(B, after), with compensation, the open terms, B's supply and placement;
  - the corridor's size.
- **Step 1c** (section 8d): the device's demand, its present supply READ at source, the coupling route, the non-local
  branch, and H-COHERENCE.
- **Wave 4** (section 8e, with this close):
  - the transmitted power at the floor quantum (`docket68/wave4/linkbudget.py`);
  - a fault-tolerant memory on measured surface-code figures (`docket68/wave4/ftmemory.py`).

## 3. M's hypotheses, carried and never dismissed

H-INFO-SHAPE (ruled), H-SETTLE, H-FRAME, H-IT, H-ZERO, H-NULL, H-INFO / Q-1, Q-1s (both weightings), H-12Q,
H-SEATRANK, H-RETIRE-A, H-COMPENSATION and H-NONLOCAL-COUPLING. None is shown and none is refuted. Each carries what
would test it, in its owner.

## 4. Claims withdrawn or corrected on verification (kept as history in their owners)

- **Wave 3:**
  - "Never in between" holds only for two sites.
  - Reznik's L/T < 1.1 belongs to its window.
  - The negatives' triangulation was not credited to projections.
- **Step 1b:**
  - "B holds I/2" became 𝟙/2.
  - "The read dissolves the retire term" became "subsumes".
  - "Under a week" fails at Faria's low L*.
- **Step 1c:**
  - "J ≤ πc/2L" as a locality ceiling: locality bounds time, not J.
  - "A century is not excluded" is withdrawn for an instantaneous coupling.
  - The formal 1/R³ carry understated the far field by (kL)².
  - "H-MIDPOINT-SOURCE minimises the hold": the hold is 2x/c.
  - "Two frames close a loop" became "loop iff no common simultaneity frame".
- **Wave 4:**
  - The floor quantum minimises received, not transmitted, power.
  - "More than the Sun" is fragile: a 0.14″ beam would suffice.
  - One atom per qubit is not a floor.

## 5. What stays open

These are listed in `ledger.py` as W3S1B_OPEN (13 items), S1C_OPEN (8) and W4_OPEN. Among them:

- a non-destructive atom-resolving bulk read;
- placement into a bonded solid;
- phosphorus at Proxima;
- a coherent source and focusing optic at the floor quantum;
- the minimum transmitted power over quanta;
- the origin of the 1e-10 burst floor;
- whether Λ holds to distance 245;
- the streamed hold;
- whether a non-local J is distance-free.

## 6. M's rulings

M-RULINGS-2026-10-03.md holds items 1–40. On RULED_BY_M they are M's answers to questions put, ids following the item
numbers. Carried without a ruling, by the charter (D68_CARRIED) or by the rulings file (D68_FILE_CARRIED): M's
statements, instructions, hypotheses and questions. `ledger.py` counts and checks every one of them against the file.

## 7. The paper and the Q-1s gate

- `paper/CLAIMS.md` was not edited by this docket, except where M ruled: items 12, 13 and 26, under their marker heads.
- M's condition for a Q-1s paper session: "when docket 68 workflow is finished" (C8b), and only "if the math concept is
  novel" (item 11).
- **The prior-art search is the gate.** It runs next, and no paper is written before M sees its result.

## 8. Checks

- `python3 ledger.py --selftest` and `--check`.
- The owners' selftests:
  - `docket68/wave3/*.py`, `step1b/*.py`, `step1c/*.py`, `docket68/wave4/*.py`;
  - `index3.py`, `specthm.py`;
  - `docket66/combine66.py`;
  - `tools/docfigures.py`.
