# THE REGISTER CHAT — read this file and nothing else to begin

*One page. It replaces `DIGEST.md`, `BOARD.md`, `HANDOFF-PROTOCOL.md` and every transcript
for the purpose of keeping the register current. Read those only if a slip needs adjudicating.*

## Opening the session — two inputs, total

1. Upload the latest `restore-point-2_NN.tar.gz`.
2. Run:

       mkdir -p /home/claude/work && cd /home/claude/work \
         && tar xzf /mnt/user-data/uploads/restore-point-*_tar.gz && python3 regchat.py open

`open` verifies C4, runs both gates, counts the register by the declared instrument, prints the
**next free id**, and lists the slips waiting in `slips/`. **State nothing about the work before it
prints** (R 1685, R 1697).

## The rule this chat exists to enforce

**The register is a single-writer object (R 1726).** A chat that computes does not number its
finding. It writes a SLIP. Ids are allocated here, where the file lives, in one sequence.

## The slip — what other chats send instead of a transcript

One file per finding in `slips/`, named `NN-shortname.md`. No R number anywhere in it.

    SOURCE: <chat name, date>
    ARTEFACT: <files behind the claim, comma separated — or TRANSCRIPT-ONLY>
    TITLE: <the headline, in caps, ending in a full stop>
    BODY:
    <the entry text; italics for what was measured, bold for what it means>

`ARTEFACT: TRANSCRIPT-ONLY` is admitted but flagged in the certificate: an entry drafted from a
summary while the file behind it is unread is §2.14's named fault (R 1727).

## Working the session — three commands

| | |
|---|---|
| `python3 regchat.py open` | verify · gates · count · next free id · slip inbox |
| `python3 regchat.py ingest` | validate every slip, allocate ids in order, append, rebuild, re-gate |
| `python3 regchat.py close` | seal the next bank, write the certificate, list what is owed |

`ingest` refuses rather than coerces (§2.9). It fails on: unbalanced bold markers; any line that
would read as a false heading (R 1617, R 1730); a missing SOURCE, ARTEFACT or TITLE; an R number
claimed inside a slip; or a duplicate id after the append.

## Five standing facts, so they are not re-derived

- **Canonical register count is `entries`** — distinct ids, suffixes included. `register_count.py`
  prints all three readings and gates on duplicates (R 1730).
- **C4 has two right answers**: archive dir *entries* include `./`, so entries = dirs + 1 (R 1726).
- **Rebuild with the redirect**: `python3 register_gen.py > REGISTER.md`, always (R 1700).
- **Clear `.zeno/` before any gate rerun**, or the pass is the old instrument's (R 1709).
- **Never run python inside the tree without checking for new `.pyc` afterwards** (R 1713, R 1728).

## What this chat does NOT do

No press, no PDF, no index write. `COORDINATES.tsv` and `MEASUREMENTS.tsv` are not touched here.
Rulings belong to M and are listed as owed in the closing certificate, never decided.