# REGISTER-GAPS — the Register's numbering, and what accounts for every hole

The Register seats **1,756 entries** numbered 1–1889. **133 numbers in that span have no entry.**
This asks what accounts for each, and the answer is mostly reassuring: **119 of the 133 are seated
in the Working Register**, moved there on purpose. **14 are seated in neither** — and **the fourteenth
is not a hole of the same kind as the other thirteen**: see below.

*Figures re-measured 2026-09-07 at BUILD116, where the Register runs to 1848. They read 1,660 / 1–1792 /
132 / 13 when this file was written and went stale as the R4 leg seated entries; `tools/docfigures.py`
is what caught the drift. The finding itself is unchanged: every gap but the fourteenth is still a
relocation.*

`REGISTER-GAPS.tsv` is the standing list — one row per gap. **Nothing has been repaired.** Filed for R3.

## The invariant, and it holds exactly

`RULING 27 — TWO REGISTERS` splits the record: subject matter stays in The Register, editorial and
production work moves to `WORKING-REGISTER.md`. The two are a **partition**, and the arithmetic
closes:

| | entries |
|---|---:|
| `The_Method_1_6___The_Register-2.md` | 1,756 |
| `WORKING-REGISTER.md` | 119 |
| **overlap** | **0** |
| **sum** | **1,861** |
| span 1–1889 | 1,889 |
| **unaccounted** | **14** (thirteen holes and one reservation, 1797) |

Every one of the 119 Working Register entries falls in a gap of The Register, and no number is
seated twice. That is worth stating because it is checkable in one command and because it means
**a gap is normally a relocation, not a loss.**

The relocation is recorded. The live bundle carries an HTML comment at each moved entry:

```
<!-- EXCISED 366 : C-internal -->
```

**All 119 carry such a marker, and no number outside the Working Register carries one** — 114 marker
lines covering 119 numbers, because three of the markers are themselves grouped
(`<!-- EXCISED 206,210,269 : C-internal -->`). Three reason classes: `A-production` 70,
`C-internal` 27, `B-session` 22. Register 363 is the account of the pass itself: *"119 entries
carrying 15,278 words become 4,266 … what each loses is the reasoning, because the reasoning lives
in the section the entry cites."*

**The correspondence is exact in both directions**: every Working Register entry has a marker, no
marker names an entry The Register still seats, and none names one of the 13. That is the strongest
evidence here that the relocation was carried out deliberately and completely.

## The 14 seated in neither register

| number | neighbours | what still names it |
|---:|---|---|
| **176, 177** | 175 / 178 | nothing, anywhere — no citation in any volume, file or chat |
| **661, 662, 663, 670, 671, 672** | 659 / 673 | `extracted/archives/method16-rp-b-data/COLLECTION-LOG.md`, `reader_audit.py` |
| **682, 683** | 681 / 684 | the collection log, `spectra_raw/` |
| **687, 688** | 686 / 689 | the collection log |
| **1138** | 1137 / 1139 | six chat mentions; a Claude-project export |
| **1797** | 1796 / 1798 | **`REGISTER-QUEUE-APPEND-cypher-audit.md`, where it is staged and waiting** |

**1797 is not lost and is not in the class of the other thirteen.** It is a number *reserved* by the
cypher audit and queued for seating, held open by Phase 0 ruling 4 — a decision not yet taken, not a
record that went missing. `r2-regsweep2` names it in as many words: *"numbers absent above 1792, in
1..1848: [1797] (staged, not seated)"*. It leaves this list the moment that ruling is given, and it is
counted here only because the arithmetic of the span cannot tell a reservation from a hole.

The ten in the 661–688 range are the interesting ones, because a data-collection log **quotes one as
a live instruction**:

> *"Register 661. **Collect everything before any analysis or write-in.**"*

So 661 was an entry when that log was written, and it is now in neither register and carries no
excision marker. Same shape for its nine neighbours. That is a small, bounded, checkable question
for R3: **were the 661–688 numbers withdrawn, or reserved and never issued?** The log is the witness
either way.

**176 and 177 have no trace of any kind** — not cited, not excised, not logged. That is the most
likely case of numbers simply never issued, and it is explicitly **not** a finding of loss.

## Two traps, both of which caught this census before it was right

Recorded because either one silently produces a wrong number, and the first is already the corpus's
own finding.

1. **Grouping, in two different places.** Entries are headed in groups — `### 219, 220, 221`. A bare
   `### N` read gives 1,683 entries and 165 gaps; honouring grouped headings gives **1,715 and 133**.
   The bare read invents 32 gaps that are not gaps. `DEFERRED.md` docket 9(c)/30 records exactly
   this: *"219 / 220 / 221 (L1323), 305 (L1327), 239 / 256 (L1335) ARE headed under grouped
   headings; every prior recording used the bare convention alone."* **The excision markers are
   grouped the same way**, and reading only the first number of each loses eight entries and
   invents eight unmarked relocations.
2. **This repository's own prose-only audits quote the chat export.** Counting `PROSE-ONLY.tsv` or
   `RETRACTION-AUDIT.tsv` as repository presence makes an identifier read as held because this
   session wrote it down. They are excluded from the presence check, and the exclusion list is in
   the generator.

## What was already known, and what this adds

The corpus already tracks the **cited-but-absent** class, and better than this file does: the seated
instrument `register_cites.py` reports *"cited but no entry: 31"*, and `DEFERRED.md` docket 9(c)/30
re-measures the class with the grouped-heading correction applied. **None of that is superseded here.**

What this adds is the other direction — **absent from both registers, whether or not anything cites
it** — which is how 176, 177 and the 661–688 block surface at all: nine of the thirteen are cited by
no register phrase and so fall outside the cited-but-absent census by construction.

## What this does not establish

- **A gap is not a loss.** 119 of 132 are relocations with the destination seated and, for 111, the
  reason recorded. Of the remaining 13, two have no trace at all, which is as consistent with "never
  issued" as with "removed".
- **The excision reason codes are not decoded here.** `A-production`, `B-session` and `C-internal`
  are quoted as the bundle writes them; what each means is the corpus's to say.
- **`UNSEATED-CITED-IN-REPO` is a token match.** The row names the files; read them before treating
  a citation as evidence the entry existed.
- **Nothing was repaired**, and no entry was moved, drafted or renumbered. The chat-67 full hold
  governs.

## Re-verification

```bash
# the partition, and the 13 — the whole finding in one block
python3 - <<'EOF'
import re, pathlib
def entries(p):
    t = pathlib.Path(p).read_text(errors='replace'); s = set()
    for m in re.finditer(r'\n### ([\d,\s–-]+)\n', t):        # grouped headings honoured
        for part in re.split(r'\s*,\s*', m.group(1).strip()):
            if part.strip().isdigit(): s.add(int(part.strip()))
    return s
R = entries('method/members/The_Method_1_6___The_Register-2.md')
W = entries('method/members/WORKING-REGISTER.md')
print('Register', len(R), 'Working', len(W), 'overlap', len(R & W))
print('seated in neither:', sorted(n for n in range(min(R), max(R) + 1) if n not in R and n not in W))
EOF

# the excision markers are in the live bundle, not only the archive
grep -c '<!-- EXCISED' method/The_Method_1_6_BUILD180_compendia_papers_audits.md   # 114 LINES
# 114 lines, 119 numbers — three markers are grouped, and they are the trap:
grep -o '<!-- EXCISED [^>]*-->' method/The_Method_1_6_BUILD180_compendia_papers_audits.md \
  | grep -vE '^<!-- EXCISED [0-9]+ : [A-Za-z-]+ -->$'      # the three grouped markers

# the collection log that quotes 661 as a live instruction
grep -i -o '.\{0,60\}Register 661.\{0,70\}' extracted/archives/method16-rp-b-data/COLLECTION-LOG.md
```

## Columns

`number`, `class` (`RELOCATED` / `UNSEATED-CITED-IN-CHAT` / `UNSEATED-CITED-IN-REPO` /
`UNSEATED-NO-TRACE`), `seated_in`, `excision_reason`, `prev_seated`, `next_seated`, `entry_text`
(the Working Register's own opening, where it holds the entry), `chat_mentions`, `repo_files`,
`conversation`, `conversation_title`, `date`, `msg`, `chat_prose`.
