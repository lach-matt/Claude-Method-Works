# Resuming a paper

A previous drafting run was cut off mid-flight by a service limit. Your paper's directory already
holds part of the work. **Read what is there before writing anything, and build on it — do not start
over, and do not rewrite a working `check.py` because you would have written it differently.**

Order of work:

1. Read `PAPER-SPEC.md` and `BRIEF-COMMON.md` beside this file. They bind exactly as before.
2. `ls` your directory and read every file in it. Read `check.py` in full.
3. `export PATH=/home/user/Claude-Method-Works/method/bin:$PATH` and run `python3 check.py`. It may
   take several minutes. The log of the last run is at
   `/tmp/claude-0/-home-user-Claude-Method-Works/550096c1-e482-5fca-a954-6b4d26a5afe4/scratchpad/checks/<your-dir>.log`.
4. **If an obligation fails, decide which of two things it is, and say which in `SOURCES.md`:**
   a bug in the check (fix the check), or a claim of the source that does not reproduce (record it —
   the paper then prints the reproduced result, or omits the claim, and never the unreproduced one).
   You may not change a check to make a discrepancy disappear.
5. Finish the paper: `PAPER.md`, `SOURCES.md`, `FIGURES.tsv`, figures, per the contract.
6. `python3 /home/user/Claude-Method-Works/papers/method/lint.py .` until clean.
7. `python3 /home/user/Claude-Method-Works/papers/method/render.py .` and confirm the PDF's page count.

Two papers are already drafted to full text and are the register to match: `04-seaton/PAPER.md` and
`03-bracket/PAPER.md`. Read `04-seaton/PAPER.md` before writing your own §0 — it shows the level of
precision about scope, sample and what is *not* established that every paper here carries.
