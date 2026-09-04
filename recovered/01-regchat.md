SOURCE: the register session 1.8.5, 2026-08-15
ARTEFACT: regchat.py, REGISTER-CHAT.md, slips/SLIP-TEMPLATE.md, register_count.py
TITLE: THE REGISTER CHAT IS NOW ONE PAGE AND THREE COMMANDS, BECAUSE THE HANDOFF WILL RECUR.
BODY:
*M's direction: the register will hand off many times as it grows, so the opening cost must fall.
Measured problem — a fresh chat previously read `DIGEST.md` (20 KB), `BOARD.md`,
`HANDOFF-PROTOCOL.md` (12 KB), a bridge and several sibling transcripts before it could write one
line, and the transcript pass alone consumed roughly half a context window in this session.
Built: `REGISTER-CHAT.md`, sixty lines, the only file a register chat reads to begin; and
`regchat.py` with three verbs — `open` verifies C4, runs both gates with the Zeno cache cleared,
counts by the declared instrument and prints the NEXT FREE ID and the slip inbox; `ingest`
validates, allocates, appends, rebuilds with the redirect and re-gates; `close` seals the next
bank, writes the certificate and prints what is owed.*
**THE OPENING COST IS NOW TWO INPUTS — the bank and one command — AND THE CLOSING COST IS ONE.**
**Every refusal in `ingest` was demonstrated before adoption (§4.6): a deliberately bad slip was
refused for unbalanced markers and for a line that would read as a false heading, both named with
the register entry that earned the rule, and a good slip then ingested end to end and rolled back.
The five facts a session would otherwise re-derive — canonical count, C4's two right answers, the
rebuild redirect, the cache clause, the bytecode guard — are stated on the card with their
citations, so they are inherited rather than rediscovered.**