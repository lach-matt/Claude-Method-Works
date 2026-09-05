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

## Added at W-234 (Q5 pass 6's re-bank): the front matter grew and the class bit

- **Seven more members of this class, exposed by the first Register front-matter growth since the volumes were frozen** (two
  rows added to the load-bearing table at L50–L51, every line from 50 moving by +2): `r2-ch16l2` (prints L1366, L1368 and
  L2418 as fixed lines), `r2-ch16t2` (L1929), `r2-ch16v3` (L5017's neighbourhood), `r2-ch16u3` and `r2-ch16z2` (`REG[5016]`,
  register 1336 read at a fixed line — both now exit 1), `r2-ch24b2` (L1798, L1936), `r2-reg8a` (`RL[:74]` as the front
  matter, now 79 lines, so its reg8-B list drops the *411 entries are cited* line at L75). Each printed the same words while
  the front matter stood still and prints another line's words now; none is re-banked. Content-keyed successors owed —
  the anchor is the entry heading or the sentence, never the line (the `_L(text)` locator `r2-ch24b2` itself uses for its
  main-volume sites is the pattern; its Register sites are the exception).

## Repaired at W-235, and the class measured to its root

- **The blind spot `reanchor.py` documents was realised in nine instruments**, and each golden had banked another line's
  words since the day it was seated (9b718be): the main volume had gained +3 at L1105 and +2 at L1447 between BUILD90 and
  the re-anchoring, so every re-anchored number above L1452 that was not a main line — a Register or Index index, a
  register number — resolved five off while `proveanchor` passed on the old bytes. Found by resolving every `_L(text)`
  in the 49 re-anchored instruments in BUILD90's main and reading the predecessor's use of the number it replaced.
  `r2-ch16t2`, `r2-ch16l2`, `r2-ch16v3`, `r2-ch24b2`, `r2-ch19a2` (banked *False* for *True*), `r2-ch28b2` (counts),
  `r2-ch20a2` (five wrong registers), `r2-ch16u3`, `r2-ch16z2` (both red since pass 1, unlisted at W-232); `r2-reg8a`
  the plain literal. **Ten content-keyed successors seated** (W-235), each proved byte-identical to its predecessor's
  golden on the pre-shift members except at the mis-targeted sites, where it prints the first-generation instrument's
  words, and shift-only on the live members. **The rule that survives:** a successor is proved against the FIRST
  generation's words at every cross-volume site, not against its immediate predecessor's golden, because a predecessor
  banked green can be wrong. `tools/gate_live.py` finds a superseded golden by name; the seven held here at W-234 need no
  entry in its table now.
- **A label class beside the read class, named by the l3 verifier:** the re-anchored family also prints hard-coded main-volume
  L-numbers inside prose strings (`r2-ch16l3`'s *L8838* and *L8794*, stale by the same +5; `r2-ch16t3`'s *L9356* now computed).
  Labels, not reads — the words printed are the right words — so the successors carry them unchanged (G0c) and they are
  recorded here for the day a label successor is worth its own pass.
