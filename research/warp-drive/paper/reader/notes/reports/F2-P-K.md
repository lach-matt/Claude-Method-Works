# F2-P-K: second fixes to proofs/P-K.md after R2-P-K

**Result.** The new md5 is **5258f67d066990c6de53d35be8fcfbd6** (466 lines); the old one was
e38d85b60ed9a392d9f143d944a8ed06. No chapter or crosswalk file was edited. Nothing was committed. No number changed.

## Resolutions

- **m1, minor.** Text 3 now carries the condition for the bound on d and cites the result that proves it. The reader's
  tested replacement is used: "and at one admissible choice of the weights, orders and inner products, d is at most an
  integer below 1.57157 × 10⁵⁰ ([[thm:uc-integer]])". The item header now says "seven lines".
- **n1.** The locations in crosswalk rows 2–6 now match the file: P-K.md:40, :176, :184, :192 and :307. They were
  recomputed from where each label is defined, after all the edits. Row 1 stays at :1.
- **n2.** Line 11 now reads "use the bounds for d at the computational point", not "the upper bound".
- **n3.** The parenthesis at the end of *Collecting* now reads "only at orders k ≥ 3, by [[eq:s27-theta]] and
  [[lem:iii-k-2-2]] (d), where m := k + 2 would serve …". This uses the reader's words.
- **n4.** Text 3 and the remark now cite [[thm:ec-lb-proved]], which is defined in chapter 71 at line 1707. The remark
  was refilled. I also moved one line break so that "β0(k_P) = max(2, 4C(k_P) + 1)" is no longer split across lines.
- **n5.** The item headers now give chapter 71 lines 29–30 (text 2) and chapter 90 lines 76–77 (text 8) and 134–135
  (text 9). Texts 3–7 keep their line numbers.
- **n6.** Item 10 now says that the lower-bound section ([[thm:ec-lb-proved]]) is already merged and that this placement
  applies after it. That section's texts overlap none of texts 2, 3, 8 and 9. My wording departs from the reader's in
  one respect: it names the label and states the order of application, as the coordinator asked.

## Checks on the current HEAD (2a4c9cd3)

- Each of the eight old texts was re-copied against the current chapters, and each occurs exactly once at its header's
  lines: ch71:29–30, ch03:311, ch46:248, ch46:1603, ch63:67, ch63:291–293, ch90:76–77 and ch90:134–135. The insertion
  anchor also occurs exactly once.
- Scratch merge (the insertion plus all eight replacements, in scratchpad/reader/pk/merge2):
  - lint --chapters gives 0 hits, with 4615 labels (the baseline 4609 plus the 6 new ones);
  - assemble --check gives 0 problems;
  - lint --paper on the scratch PAPER.md gives 0 hits;
  - the longest line in the paper is 121 characters, and in the new section (§49.14) 120;
  - the longest resolved line of text 3 is 111 characters.
- P-K.md itself:
  - every line is at most 121 characters, before and after label resolution;
  - no wrapped line starts with a forbidden marker;
  - there are no backslashes, and every key is lowercase;
  - the only lint hits are the six source paths in the crosswalk rows.
- Merge note (the reader's): row 3's note contains "; ". Keep it inside the note column when merging.
