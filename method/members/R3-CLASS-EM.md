# R3-CLASS-EM.md — the split-emphasis class: sites, both texts, the repair, and what it may not touch

Written under M's direction to prepare the class found at reg7-01 / reg7-02. **Nothing here is
applied.** This is the `R3-CLASS-WL.md` model: the withdrawn-law class was specified, dry-run and
banked at chat 128 and held for R3, and it waits behind the same gate. The chat-67 hold stands and
RUL-128 item 1 puts the mathematics first and the prose after it — **this class is prose**.

Instrument `r3-em.py`, dry-run golden `r3-em.out` (2,387 B · `63f7206c` · 40 lines). It writes no
file and changes no member.

## The defect

**275 entries carry `X* *Y`** at **429 sites** — a bold `**` split so one asterisk attached to the
preceding word and one to the following. Inside an italic body a single-asterisk pair cannot nest:
it **closes** the body and opens a new italic. The sub-phrase the author marked therefore renders as
more continuous italic, and the distinction is not on the page. In **11** entries the split also
makes the line's asterisk total odd, so a literal asterisk survives into print — 313, 604, 747,
1642, 1643, 1648, 1649, 1652, 1653, 1657, 1681.

## The repair rule, stated before it is applied

For an entry whose body is a single italic run: split the body's interior on the split sites; the
segments alternate **body / emphasis**, beginning with body; re-emit each emphasis segment as
`**bold**`, which is the only nesting Markdown allows inside an italic run; rejoin with single
spaces. **The headline is never touched.**

Worked, from entry 289:

```
old   ** … ENTRY NUMBERS.** *What* *fifteen* *counted cannot be settled from the section …
new   ** … ENTRY NUMBERS.** *What **fifteen** counted cannot be settled from the section …
```

## What the rule does, measured

| | |
|---|---:|
| entries the rule repairs | **246** |
| entries it declines, for hand repair | **29** |
| repaired lines still carrying a split site | 0 |
| repaired lines that do not close their own emphasis | 0 |
| member delta | **+360 B**, 0 lines |
| lines differing | exactly 246 |
| **reverse guard** | reversing every substitution recovers `79aaf239a42c1649e914b7cba9d5ce2a` |

## The 29 the rule declines, and why it must

Their bodies are not one clean italic run, so the segments do not alternate and the rule would
corrupt correct markup. **238, 290, 313, 327, 338, 397, 463, 543, 595, 604, 608, 640, 641, 646, 648,
702, 707, 724, 747, 1394, 1642, 1643, 1648, 1649, 1652, 1653, 1657, 1681, 1722.** Both texts for every one are
regenerated deterministically by `r3-em.py` (the table is 420 kB and is derived, not seated —
instruments travel, outputs are goldens). Three examples of why they need a reading, not a rule:

- **290** — `** … REPAIRED.** **Every other block of the register ascends* **, so the descending
  block …` — the body opens on a bold run, not an italic one; where the italic body begins is a
  reading, not a parse.
- **313** — the headline itself is broken (`TIME MUST NOT ENTER Λ*`), so the repair must restore the
  quotation before any body rule applies. This is reg3-01.
- **1722** — `** … INSTRUMENT.** **Uniform failure is a fault in the instrument.*` — the headline is
  restated as the body's opening and the emphasis closes on a single asterisk.

## What R3 must do beyond this instrument

1. Repair the 29 by hand, with both texts, never by the rule.
2. The change is a volume change, so under **no silent change** it needs a Register entry in the
   same build recording it — and the entry that records the *form* (**1725**) does not exist
   (reg1-05), so the form has no seated statement to cite. That gap is repaired first or the
   correcting entry has nothing to point at.
3. RUL-128 item 1 puts the mathematics first. This class waits.
4. It runs through `close.py` with the member and bundle reverse guards, **never in place**.

## The fault this instrument caught in itself

An earlier draft **read** each body at `RL[pos+1]` and **wrote** the repair to `NL[pos]` — one line
up, the blank line. The repaired member duplicated every body onto the blank above it (**+195,358
B**) and left the originals untouched, and the reverse guard did not recover the seated md5. Nothing
was written, because this instrument writes nothing, and the fault surfaced in the dry run instead
of in a build. **That is what the reverse guard is for**, and it is why this class is specified and
dry-run before it is ever applied.
