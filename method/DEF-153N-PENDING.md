# DEF-153N — the positional class, and the blind spot in `proveanchor`. RECORDED, NOT REPAIRED.

## The estate after two re-banks

At BUILD98 every instrument was re-run and cached: 9 UNCHANGED, 0 EXPLAINED, 73 UNEXPLAINED,
13 UNRUNNABLE. Twenty-two of the 73 were re-banked by running (W-208, W-209) after each changed
number was classified as a line reference re-found semantically or a count the appended entries
move. What remains is not many jobs but one class.

## The class: a literal line read whose content moved

An instrument reads a fixed line number, or a fixed window from a heading, and prints what is
there. The volume grew above it and what is there changed.

    r2-ch16p2   A, B = 9030, 9156           prints  L9030 ### 32.2 Self-reference   ->  L9030 Register 373.
    r2-ch17f    "main L9892–L9936 (Ch 36)"   Chapter 36 now begins L9922; the window straddles §35's tail
                                            and the check "read on the join" flips True -> False
    r2-ch17e2   'E(Λ₃) = 0' in M[6999]       the text is at L7002; the check flips True -> False
    r2-ch16q    DATA rows 6 -> 5             the table at L9174–L9182 still has six rows
    r2-ch16u2   "Six" vs DATA rows 4         §35.5's ledger still has seven; the window moved
    r2-ch16c    Schmid [8572, 8573] -> [8574] L8575 fell off the window's far edge
    r2-ch19b    A.19's rank table 7 -> 0     the same eleven code lines, moved +30, attributed to no
                                            sub-window; the banked sentence would be false
    r2-ch20a    main-paragraph numerals      a different paragraph is now at the literal range
    r2-ch28b    Hill 1878 above L11818 at [11790] -> []   References moved +42; the literal did not
    r2-ch18a    eight adjunction sites, all +2, then `L4806: Theorem 17.1` by literal — L4806 now
                holds "**And a theorem in the other direction"; the semantic and positional reads
                sit on ONE line, and a check truncated at 100 characters saw only the semantic half

About 45 instruments carry this shape, the 13 UNRUNNABLE among them. Each needs a SUCCESSOR that
resolves its site semantically and is cross-checked against an independent resolution of the same
site — W-207's disposition — and then `proveanchor`. None may be re-banked: a re-bank would bank
whatever text now sits at the old line, with the old label on it.

**Not a content defect.** Every "table lost rows", "check flipped", "site vanished" above was
traced to the window and not the volume. `r2-ch16q`'s six-row table has six rows.

## A near-miss in this pass, and what it says about the triage

`r2-ch18a` was placed in the second re-bank on a residual check that printed the first hundred
characters of each differing line. Its one differing line is 487 characters: a semantic list of
eight sites, every one moved +2, and then a literal read of L4806 labelled Theorem 17.1. The false
label sits past the hundredth character. The build was made with it and caught only because the
golden came out 47 bytes shorter — a pure line shift cannot shrink a golden — and was discarded
before install. **A single golden can carry both anchoring styles on one line**, so "the numbers
moved consistently" on the visible part of a line is not evidence about the rest of it. The check
now prints the divergence point in full.

## The blind spot: `proveanchor` proves the past, not the anchor

`r2-ch17e2` was seated this session as `r2-ch17e`'s successor after `proveanchor` reproduced the
predecessor's golden byte-exact on the pre-shift bundles. It still reads `M[6999]`. At proof time
L7000 held `E(Λ₃) = 0`, so the literal was correct and the proof passed. Two builds later it is
wrong, and nothing in the guard could have said so.

`proveanchor` establishes that a successor REPRODUCES a reading the predecessor made. It cannot
establish that the successor's anchor is semantic rather than positional — a literal that happens
to be right reproduces perfectly. The property a successor needs is invariance under a shift, and
the only test of that is to run it on TWO bundles that differ by a shift and require the same
reading of the same text. That test does not exist yet.

## A literal in prose over a live divisor

`r2-reg7a` prints `'%.1f%% of the 1,635 entries'` where the percentage is
`100 * len(split_e) / len(pos)` and `pos` is the live Register: 275 / 1648 = 16.7%, printed
beside a literal 1,635 that no longer divides it. The banked line says 16.8%, which was right when
1,635 was the count. The instrument is now false on its own line, and re-banking would seat the
false line. Held for a successor that prints `len(pos)`.

`r2-ch16k` was checked for the same fault and is clean: its `1635 -> 1641` is `len(ent)`.

## What waits, and on what

    kinds, r2-regsweep         the Register's census instruments  ->  with reg1-04, after the readings
    ~45 positional             successors, W-207's discipline     ->  a reading each
    r2-reg7a                   a successor printing len(pos)       ->  small
    r2-ch19b                   a successor with A.19's sub-window re-anchored  ->  small
