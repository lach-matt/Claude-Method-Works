# FAULT F31.4 — the s31 OPEN foreign-file check (F18.1/F30.1) was read from a `| head` -truncated listing and reported "clean". The listing was truncated at
10 lines; the loop's ls test was also wrong (returned nonzero on the second glob's miss), so 220 names printed as "foreign" when rerun untruncated. Repaired by
census-to-file (R 1670 form): find pack*/ basenames vs ls rt, comm -23 -> ONE name, `out`, which is pack5's own out/ directory (119 Z*.tsv, copied at open).
Result: rt/ IS clean; the open-time claim was true by luck, not by check. Registered as a check fault (R 1664/1671 class: an instrument that narrows its own
input reports on what it admitted).