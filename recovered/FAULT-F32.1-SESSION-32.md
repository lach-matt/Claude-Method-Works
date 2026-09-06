# FAULT-F32.1 (s32) — F18.1/F30.1/F31.4 shape recurred: abandoned-branch artefacts appeared DURING the session
Found at the moment create_file refused pack32/sox_table.py as existing (19:38 timestamp; the open-time census at 18:xx was clean, F31.4 protocol).
Foreign: pack32/sox_table.py (a "step 1" S(q) design in Fetter-Walecka convention, NOT this thread's), rt/sox_table.py, rt/sox_table.jsonl.
Action: registered here BEFORE reading their content beyond the docstring; moved to pack32/foreign/*.branch (kept as record, §H.4); rt/ re-censused
to file (comm) after removal. NOT adopted; nothing from them enters the build. This thread's own objects are sox_qres.py/.jsonl (checked: written by
this thread's batches, timestamps match) and the sox_table.py written next. Standing rule (README-31 "Known"): census rt/ to a file before writing AND
before adopting — extended: re-census whenever a write is refused as pre-existing.