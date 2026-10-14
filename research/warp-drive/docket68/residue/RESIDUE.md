# The residue: every open row against your rulings (M-RULINGS item 135, step 1; computed; verified once; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## What you asked

- **Item 135:** *"Older waves first, then read/search outside art for sources and measurements, computable loose ends
  next, then reassess the questions only for me and present them. After all that, reassess the walls, and present each
  of them to me in question form."*
- *"We cannot move forward with designing that actually device until there is nothing to solve or account for in the
  chain."*

This note is step 1: every open row on the board, read against your later rulings.

## What passes

- **Of 106 open rows, 19 stay live on the chain, plus 5 new rows the audit opened.**
  - 37 rows are closed by your rulings: 5 answered and 32 whose premise you removed.
  - 31 were the same question as a live row and now stand under it.
  - 11 belong to the clock and support threads, which no link of the chain uses.
  - 1 is an input the user gives per trip.
  - 7 rest on a premise of physics you carry, and go to the walls.
- **Most older-wave closures are about a trip your rulings replaced.** 30 of the 79 older rows are off the path. They
  priced a link, a quantum payload, a collector, a moving bubble, the seat ranking or Chung–Freese's shape. Your rulings
  replaced each:
  - item 87: *"A faithful copy"*;
  - item 90: *"not by light"*;
  - item 94: *"their is no movement in warp travel"*;
  - item 119: *"precision is never a question"*;
  - item 126: *"it is realized in the same place the position 1 occupies"*.
- **Every disposition cites a ruling, and the selftest finds the cited fragment in that ruling's record.**
  - `residue.py` imports the open rows from ledger.py.
  - The search runs over the whole record: your words and the board's text around them. That each fragment is your
    word was checked by the verifier by hand. Two fragments that came only from the board's text were replaced.
  - Selftest: 13/13, with 10 controls.
  - The controls are a misquote, a dropped row, a duplicated row, a row pointed at a closed row, a tag the chain uses, a
    misspelt tag, a ruling not yet given, an unknown kind, a closure with no ruling cited, and a live row with no route.
    Each is caught on its own.

## The dispositions

| kind | rows |
|---|---|
| RULED (5) | S1B-O1, CMB-O1, BULK3-O1, COPY-O5, COPY-O8 |
| CARRIED (7), to the walls | S1B-O2, S1B-O4, S1C-O2, BULK-O3, COPY-O2, COPY-O9, C8O-O6 |
| OFF-PATH (32) | S1B-O5, O6; W3-O2, O4, O5; S1C-O3, O5..O8; W4-O1..O6; CMB-O3, O4; BULK2-O1, O4, O6; BULK3-O2, O5, O7; BULK4-O1, O7; BULK5-O2..O5; COPY-O6, O7 |
| OFF-CHAIN (11) | CMB2-O1..O6, CMB3-O1..O5 |
| INPUT (1) | COPY-O1 |
| LIVE (19) | BULK-O4, COPY-O3, COPY-O4, C8O-O1..O4, C8O-O7..O9, C8P-O1..O9 |

**Answered by a ruling:**
- **S1B-O1, which count is the object's information.** It is your input N, read from the object, in *"its most
  simplistically exact binary code form"* (items 130, 131).
  - Item 33's four counts and 89(c)'s fifth reading are set aside only on the board's reading of 131.
  - What "most simplistically exact" means is RES-N5.
- **BULK3-O1, classical or quantum.** Classical (items 87, 131).
- **COPY-O8, the device's mass at position 2.** There is no device there (item 90).
- **COPY-O5, the site's share of the README.** The README defines the object; the site is not in it (item 131).
- **CMB-O1, the frame.** It is the background's rest frame (item 96). Whether that frame is exact FRW's cosmic frame
  goes with RES-N3.

**Carried, to the walls:**
- **The build by position 2 itself, through a field reaction:** COPY-O2, S1B-O4, S1C-O2 (items 91, 101).
- **The build's energy as the closing energy:** S1B-O2, COPY-O9 (item 111).
- **One entangled state's accounting:** C8O-O6 (item 111).
- **A second plane:** BULK-O3 (item 123).

**Subsumed:**
- into **C8P-O1**, the global bulk: BULK4-O5, O6, O8; BULK5-O1, O6, O8; C8O-O5.
- into **C8P-O3**, k: BULK2-O3, O5, O7; BULK4-O10; BULK5-O7.
- into **C8P-O2**, the coinciding junction: BULK-O1, BULK3-O4, O6; BULK4-O2.
- into **C8P-O6**, censorship: BULK-O5, BULK2-O2, BULK4-O9. This reads a time-delay theorem as a censorship theorem,
  H-DELAY-AS-CENSORSHIP, the board's.
- into **C8O-O4**, wall 9: W3-O1, S1C-O4, BULK3-O3.
- into **C8O-O1**, the joins: BULK-O2, BULK4-O4.
- into **C8O-O2**, the dynamics: BULK4-O3.
- into **C8O-O7**, the trajectories: W3-O6.
- into **COPY-O3**, the read: S1B-O7, S1C-O1.
- into **COPY-O4**, wall 7: W3-O3.
- into the new rows: S1B-O3 into RES-N1, CMB-O2 into RES-N3.

## Five rows the audit opened

- **RES-N1 (compute).** Items 111 and 133 make the build's energy *equal* to E(N). Does the assembly's free energy
  equal E(N), and if not, where does the difference go? Computed in `loose.py` L1.
- **RES-N2 (yours).** Does the original at position 1 stay or go?
  - Asked twice already: item 32, *"I suspect so"*; item 89, *"Leave it open"*. chain.py W11 names it.
  - It is re-presented because step 2 found no read that leaves a body whole.
- **RES-N3 (yours).** What does synchronizing two universes' cosmic beats mean? Items 97 and 114(d) bear on it.
- **RES-N4 (yours).** Where do the closing hold's bits go when position 2's horizon ends, and how long does the build
  take?
  - Item 109 left the bits OPEN.
  - Item 110 answered only the energy.
- **RES-N5 (yours).** Does "most simplistically exact binary code form" mean the shortest possible encoding, or one
  fixed exact encoding?
  - The shortest possible cannot be computed in general (the board's reading).
  - It decides how the device fixes N.

## What this does and does not show

- **It shows** that each closed row has a ruling of yours that answers it or removes its premise. It also shows that
  each subsumed row points at a live row.
- **It does not show** that a removed premise was wrong. An OFF-PATH row is the boundary of your path (item 82): kept,
  never leading, never dropped.
- **OFF-CHAIN rests on tags, not a ruling.**
  - Each tag is absent from every instrument under docket68/copy and docket68/bulk, and from what chain.py loads beside
    them. Each tag must also occur in ledger.py, so a misspelt tag fails.
  - If you take up the clock, support or contraction threads again, those eleven rows come back.
- **"Subsumed" moves a question; it answers nothing.** The code checks that the target is live, not that the questions
  are the same. That was the verifier's reading.

## Named hypotheses

- **The board's:**
  - H-FRONT-OWNERS, that the instruments named in `residue.py` are the current chain's owners;
  - H-DELAY-AS-CENSORSHIP.

## History (verifier, 2026-10-07)

Twenty-six findings were applied. The main ones:

- **COPY-O4 and W3-O3 are not inputs.** Item 86 answer 7 says *"what to construct with what it has"*, so a
  destination's composition is a fact about the place. COPY-O4 is live as wall 7.
  - *First written* as INPUT.
- **BULK3-O3** is subsumed into wall 9: the stabilisation scalar is still named in chain.py W9.
  - *First written* as OFF-PATH.
- **RES-N1 was one-sided.** It asked whether the energy *covers* the build. Items 111 and 133 make it an equality, and
  Landauer's term is negligible at about 8×10⁻⁶ J.
- **The "41" count was wrong.** It mixed in two front rows.
- **Two cites quoted only the board's text** (S1C-O6, W4-O5). *"This is entanglement"* was used on the board's own
  mapping of item 101.
- **S1B-O4 and S1C-O2 were "removed" on the same ruling that COPY-O2 carries.** Now all three are carried.
- **S1B-O2 and COPY-O9 are carried, not ruled.** Item 111 is a premise.
- **Clocks.** CMB2-O2, O3, O5 and O6 are OFF-CHAIN: item 97 keeps local clocks and only takes them off the joining.
- **Item 122(4) is now cited on wall 9.** C8O-O1 is restated as the apparent violation (items 117, 120).
- **RES-N2 and RES-N3 were restated.** RES-N4 and RES-N5 were opened.
- **The front-owner list was widened.** A vacuity guard and five controls were added.

## OPEN (after step 1)

- **COMPUTE:** C8O-O1, C8O-O2, C8O-O7, C8P-O2, C8P-O5, C8P-O7, RES-N1.
- **READ:** BULK-O4, COPY-O3, COPY-O4, C8O-O3, C8O-O4, C8O-O8, C8O-O9, C8P-O1, C8P-O3, C8P-O6.
- **Yours:** C8P-O4, C8P-O8, C8P-O9, RES-N2, RES-N3, RES-N4, RES-N5.
- **To the walls:** the seven carried rows.
