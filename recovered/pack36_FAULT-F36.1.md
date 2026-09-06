# FAULT F36.1 — SESSION 36 (open). Build-order fault, Claude's, at runtime rebuild.
Runtime layer copy split into two loops (19,20,21,22,24,25,26,27,28,29,31,34,35 then 23,30,32,33) instead of strict 19->35.
Effect: rt/frachf_S.jsonl = pack33 (1 row) instead of pack34 (6 rows). t7c_corrz.py ended at pack32 (latest) by luck of order.
Detected: gate 61 recomputed (DEc_R -0.03188, matched) instead of SKIP -> appended a row to the wrong file. Byte census did NOT catch it:
census admits a match to ANY pack, so an out-of-date pack copy passes as OK (R 1671 shape: the instrument narrows its own input).
Repair: cp pack34/frachf_S.jsonl rt/; gate 61 rerun -> SKIP 21. Recipe note for README-36: copy packs in strict numeric order.
Census repair owed: check each rt file against its LATEST pack copy, not any pack.