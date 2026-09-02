# THE METHOD 1.6 — RETIRED GATES AND STANDING LESSONS
**NOT READ AT SESSION START. This file exists so the handoff can stop accreting.**
A lesson moves here once it has held for three consecutive sessions without firing. It stays in force;
it simply no longer costs reading time every session. Consult it when a fault resembles one below.

## Retired from §0 (still in force)
**L-A  A SHORTER STRING MATCHES INSIDE A LONGER ONE, AND `grep -c` COUNTS LINES, NOT OCCURRENCES.**
Was G0c. `W-015` matches inside `W-015a`. `grep -c 'SPEC-12'` returns 1 where SPEC-12 occurs once;
HANDOFF-32 predicted 2 by carrying SPEC-10's figure across.

**L-B  A HEADING LEVEL IS A SERIALIZATION.** Was G0d. After any ruling that changes heading levels,
heading names or part numbering, re-run every gate before declaring the build current. `coords.py`
located its sections by the literal `### ` and went dead for a whole build when Ruling 49 promoted
Spectra's headings. Repaired chat 30.

**L-C  EXTRACTED TEXT IS NOT THE PAGE — AND ITS ORDER IS NOT THE PAGE'S ORDER EITHER.** Was G0e.
SPEC-12: 51 rows correct in the `.docx`, zero in the PDF text layer. Remedy: render with
`pdftoppm -f N -l N -r 90 -png` and read as an image. **Extended at chat 32:** the three-body original's
caption list extracted out of order, dropping a caption inside a bibliography entry. Absence in a text
layer is not absence on the page, and sequence in a text layer is not sequence on the page.

**L-D  A REIMPLEMENTATION THAT DISAGREES WITH AN INSTRUMENT IS THE THING THAT IS WRONG.** Was G7.
Import the instrument's own functions; never rewrite its parser. Chat 32: four of eighteen load-bearing
checks first read as disagreements and all four were the checker's normaliser — superscript `U⁸`
against a regex wanting `U^8`.

**L-E  A QUESTION YOU CAN ANSWER BY READING IS NOT A STANDING QUESTION.** Was G8. B13's scope question
was settled by two Drive timestamps in one listing after being carried as possibly needing the author.

## Standing lessons
**L-F  AN EXTERNAL CHECK MUST BE SCOPED BEFORE IT IS TRUSTED.** Ruling 56 arrived as an authority and
HANDOFF-32 immediately listed four findings it would settle. It settles none: the paper does not contain
the numbers those findings are about, because this work derived them after the paper. **Before an
external source adjudicates anything, measure what it contains and write down what it cannot reach.** A
source's silence is not agreement and not disagreement — it is absence of jurisdiction.

**L-G  A FETCH CAN BE TOO SMALL TO BE SAFE, AND BELOW THE SPILL THRESHOLD IT IS NOT MERELY EXPENSIVE
BUT USELESS.** The connector spills to disk only above ~1 MB; below that it returns base64 inline, and
**inline base64 cannot be written to disk** — re-emitting it as assistant output is not possible. So a
340 KB PDF costs ~114,000 tokens and yields bytes that cannot be decoded, rendered or grepped. The
Löwdin PDF worked only because 879,791 bytes → ~1.17 MB cleared the threshold.
**REMEDY: `read_file_content` returns the text layer, not base64** — ~15 KB against ~454 KB.
Over 10 MB the connector refuses outright; direct upload only.

**L-H  ASSERTION-GUARDED REPLACEMENT IS THE SAFE EDIT PATTERN.** `assert t.count(a)==1` before each
substitution catches a missing anchor immediately instead of producing silently wrong output.

**L-I  WHEN A RULING IS OVERTURNED, SWEEP FOR EVERYTHING PARKED ON IT.** Ruling 55 overturned Ruling 52
and orphaned IOI-03, which had been parked inside the merge by an earlier disposition.

**L-J  MEASURE PER FILE, NOT PER PROJECT.** "Every file ends without a newline" is false. The Register's
terminal byte is `0x29`; `WORKING-REGISTER.md` ends `0x0a`, so its `wc -l` and its split-count differ by
one. Say which measure you mean: Spectra is 84,467 characters and 87,638 bytes.

**L-K  `xxd` IS NOT INSTALLED.** Use `od -An -tx1`. `pdftoppm`, `pdftotext`, `soffice` and `pandoc` are
present. Check a tool exists before trusting its silence.

