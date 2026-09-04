# CHANGE CERTIFICATE — BUILD75 → BUILD77 compendia (compendium review pass, step 1: format conversion)
Session: chat 63 by project title (HANDOFF-11's "chat 62"). Main volume this session: BUILD76 (see STRINGPF-CONVEXITY-RESOLVED.md).

## Rulings executed (M, this chat, verbatim in W-092)
all 266 convert now · captions reduced to stated facts (owed, not yet done) · title collisions: L.c1/L.c4 node counting ℓ≤n−1 / f≤e−1; L.c2/L.c5 Pauli k≤4ℓ+2 / g≤4f+2; Q.delta/Q.final the channel equation, first/final form · GRADED OPEN suffixes dropped · chains CONVERTED · PRIOR ART → Prior art · scheme applied in one guarded step.

## Instrument: convert.py (run once on BUILD75; sites located by content; bibliography VII excluded — task 3)
- 266 headers `### \`X.y\` — title` → `### Title`; 266 metadata lines → `Grade — citations.`; 309 handle mentions resolved (titles; pointer on first mention per entry from the target's own source: §-section or "register N"); L.birk mapped by hand (§8.3); `> **PRIOR ART:` → `> **Prior art:`.
- Residual backticked tokens in the four reader compendia: 0 handles; 13 instrument/data file names (Ruling 60 press-time substitution). Bibliography citing-objects column: 410 tokens untouched (task 3).
- W-092 appended to the in-bundle WORKING REGISTER (editorial record; never reader-facing).

## Measured-diff guard (difflib, BUILD75 → BUILD77)
- 845 hunks; 861 lines deleted, 873 added (861 replacements + the 12-line W-092 block); 0 unauthorised deletions — every deleted line is a handle header, a metadata line, a line carrying a handle token, or a PRIOR ART line; 0 hunks outside the four reader blocks + working register.
- Reverse-applied diff recovers BUILD75 md5 de89d94c0c371d4ac325c37c55f32915 EXACTLY.
- BUILD77 compendia: 2,461,542 B · md5 3abbb87055fc700b1f724d08a425c994 · 32,794 lines.
- Live pair now: BUILD76 main (1,977,372 B · a4fbbc49d58ec6c6d6dd71a13f116765 · 18,452 lines) + BUILD77 compendia.

## Owed in the review pass (authoring, entry by entry with slips): accuracy read; rhetoric reduction; 17 captions → stated facts (IoI 8 first).