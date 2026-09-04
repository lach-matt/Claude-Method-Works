# HOW TO HAND A FINDING TO THE REGISTER — for every chat that is not the register chat

*Add this to project knowledge. It is the only thing a computing chat needs in order to have its
work registered. Adopted §H.12, R 1734.*

## The rule

**The register is a single-writer object (R 1726).** Four parallel chats once allocated ids from the
same bank and three ranges collided. **Do not number your finding.** Write a slip; the register chat
allocates the id, in one sequence, where the file lives.

## The slip

At the end of your session, output one file per finding — a fenced block the person can copy, or a
real file if you have `/mnt/user-data/outputs`. Name them `NN-shortname.md`. **No R number anywhere
inside.**

    SOURCE: <chat name, date>
    ARTEFACT: <the files behind the claim, comma separated — or TRANSCRIPT-ONLY>
    TITLE: <THE HEADLINE IN CAPS, ENDING IN A FULL STOP.>
    BODY:
    <Italics for what was measured, with the numbers. Bold for what it means. Name the script
    behind each claim. Register self-corrections here too — they are entries, not embarrassments.>

## What will get your slip refused

`regchat.py ingest` refuses rather than coerces (§2.9), and prints the entry that earned each rule:

- **unbalanced `**` markers** — parity cannot be repaired downstream (R 1565)
- **any line that would read as an entry heading** — a wrapped line beginning `1234. ` is read as a
  false heading (R 1617, R 1730)
- **a missing SOURCE, ARTEFACT or TITLE**
- **a slip that claims its own R number** (R 1726)

`ARTEFACT: TRANSCRIPT-ONLY` is admitted and flagged in the certificate. Prefer naming real files:
an entry drafted from a summary while the file behind it is unread is §2.14's fault, and R 1727 is
this project's own instance of it.

## And bank what you built

**R 1712 and R 1726: work produced outside the sealed tree does not survive its container.** The
Löwdin scripts and an entire press session reached no bank and had to be recovered from transcripts.
If your session wrote a script or a finding file, hand the files over too, not just the slip.
