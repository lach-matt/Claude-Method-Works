# THE HANDOFF PROTOCOL — §H
**A session is a container that will die. The protocol is what survives it.**

Adopted session 1.8, 2026-08-15, at M's instruction: *this need is becoming more common as the
work expands.* Referenced hereafter as **§H**, with clauses **§H.1** to **§H.9**.

This is a protocol in the sense of Part I §2 — procedural, not a theorem. It is written to be
**run and checked**, not read and agreed with. Its test is §H.8: a handoff that has not produced
a passing certificate has not happened, whatever was written.

---

## §H.0 What a handoff is for

A new session begins with no memory of the last one. What it has is: whatever files it is given,
whatever the register says, and whatever a bridge document tells it. **Everything else is lost**,
including every intention that was held in the head of the outgoing session and never written.

The failure mode is not losing files. It is losing **why** — which thread was open, which decision
was M's and still unmade, which number is provisional, which claim was checked and which was
merely written. A file survives; a context does not, unless it is made into a file.

> **The handoff is complete when the incoming session can do the next piece of work without
> asking a question the outgoing session could have answered.**

---

## §H.1 The four things that must transfer

| | what | where it lives |
|---|---|---|
| **1** | **The work** — every data file, script, artefact, capture | the bank archive |
| **2** | **The record** — the register, complete and rebuilt | `REGISTER.md`, `REGISTER-DATA.md` |
| **3** | **The orientation** — what a session must hold before it works | `DIGEST.md` |
| **4** | **The state** — open threads, pending decisions, what is provisional | the bridge document |

**All four or none.** Three of four is the dangerous case, because it looks like a handoff.

---

## §H.2 The bridge document

One file, named `BRIDGE-<from>-to-<to>.md`, carrying **eight sections and in this order**:

1. **Identification** — session names, date, project folder, and the transcript filenames.
2. **What this session did** — in register-entry ranges, not prose summary. `R 1642–1658`.
3. **The state of the object** — the live counts, from instruments, with the command that produced
   them. Never recited.
4. **Open threads** — each with: what it is, what has been tried, what would settle it, and
   **whose decision it is**. A thread with no named owner is not an open thread; it is a wish.
5. **Provisional figures** — every number in the record that is a choice rather than a
   measurement, named as such. (§H.6.)
6. **What is read and what is not** — for every document the project holds. Named, not glossed.
7. **The resumption order** — what to do first, second, third, and why that order.
8. **The standing carry-overs** — items older than this session that remain open.

---

## §H.3 The transcripts travel

Transcripts are the only record of *how* a conclusion was reached. The register carries the
conclusion; the transcript carries the reasoning, the failed attempt, and the thing M said in
passing that turned out to matter.

**Copy them into the work tree** — `work/transcripts/` — with the journal that indexes them.
A transcript left in a mount that the next container may not have is not transferred.

---

## §H.4 Nothing is summarised that can be carried

A summary is a lossy compression chosen by the outgoing session, which does not know what the
incoming session will need. **Prefer the artefact to the account of the artefact.** Summarise only
what cannot travel: a decision's reasoning, a discarded route, the shape of a conversation.

Corollary: **do not rewrite history to match the present.** Where a document states a figure that
was true when written and is now superseded, leave it and say so in the bridge. R 1656 left three
occurrences of a stale cell count standing because they sat inside historical statements.

---

## §H.5 The bank is the unit of transfer

One archive, everything in it, verified after building rather than before:

```
rm -rf .zeno __pycache__
tar czf /mnt/user-data/outputs/<name>.tar.gz --exclude='.zeno' --exclude='__pycache__' .
tar tzf /mnt/user-data/outputs/<name>.tar.gz | wc -l     # count what actually went in
```

**A bank that has not been listed after building has not been verified.** The count is compared
against the working tree's own count; a mismatch is a finding, not a rounding error.

---

## §H.6 Provisional figures are named

Every number in the record is one of three things, and the bridge says which:
- **measured** — from an instrument, on data, reproducible by rerunning it;
- **chosen** — a statistic, a cap, a bound, a convention. Defensible, and not the only answer;
- **inherited** — carried from earlier work and not re-derived in this session.

The second kind is the one that causes damage, because it reads as the first. Ga I's δ = 1.31599
is a **median** where the same members give a mean of 1.2949 — one dataset, two statistics, and
nothing in the cell says so. Z = 120 is a **chosen** bound; E = 0 holds at any.

---

## §H.7 The incoming session's first four acts

Written for the reader of the bridge, in order:

1. **Read `DIGEST.md`.** It holds the one claim, the objects, the generating rules, §18.4.1's
   admitted operations, the gates, and what is read and unread.
2. **Read the bridge.** Open threads and pending decisions.
3. **Run both gates before touching anything** — `The_Method_1_6_audits.py` (25) and
   `roundtrip.py` (5/5). A session that begins by changing something has no baseline to compare to.
4. **Rebuild the register** and confirm the entry count matches what the bridge states.

---

## §H.8 The handoff certificate

A handoff is complete when **all seven** return true. This is checkable, and §4.6 requires that a
check be capable of failing before its passing is evidence — each clause below can fail.

| | clause | how it fails |
|---|---|---|
| **C1** | both gates pass in the outgoing session | an audit or a round-trip is red |
| **C2** | the register rebuilds and its count is stated | `register_gen.py` errors, or the count is recited rather than read |
| **C3** | every generated artefact regenerates identically | a compendium is stale — the R 1655 failure |
| **C4** | the bank lists at the expected file count | files excluded by a stray pattern |
| **C5** | transcripts and journal are inside the bank | left in a mount |
| **C6** | the bridge names every open thread with an owner | a thread with no owner |
| **C7** | the bridge names what is unread | a gap that closes over quietly |

**Certificate form.** Print the seven with their evidence. §18.4.1's practice applies: the
certificate is *exhibited, never found*, and what is falsifiable is the exhibition.

---

## §H.9 What this protocol does not do

It does not preserve judgement. The incoming session will not hold what the outgoing one
understood; it will hold what was written. **Write the disagreement, not only the conclusion** —
where M corrected a direction, the correction is the content and the conclusion is the residue.

And it does not make a handoff free. It makes it **bounded**: the cost is one bridge, one archive
listing, and one certificate, paid once at the end of a session rather than continuously in
recovered ground at the start of the next.

> A session that ends without a certificate has not ended. It has merely stopped.

---

## §H.10 The handoff is begun at 90%, not at exhaustion

**Adopted at M's instruction, session 1.7.2, as the Prime Handoff Directive.** §H tells a session
*how* to hand off and *what* must transfer. It did not say *when* to begin. This clause is that
trigger.

> **A session states its estimated context usage when it judges 90% reached, and recommends
> handoff at that point. The estimate is declared as an estimate.**

**Why 90% and not 100%.** Every clause of §H.8 costs context to satisfy. The bridge is written,
the bank is built *and listed*, the register is rebuilt and its count read, both gates are run,
and the certificate is printed with its evidence. A session that reaches exhaustion before
beginning has no budget left to produce any of them — so it hands off without a certificate,
and §H.8 says that is not a handoff. **The reserve is part of the protocol, not slack in it.**

**The estimate is honest about being one.** A session has no exact counter. It estimates from what
it has ingested — documents read, tool output returned, the length of the exchange — and it errs
**early**, because a handoff called late is a handoff that may not get written, whereas a handoff
called early costs one bridge that would have been written anyway.

**What the trigger changes, immediately.** On reaching the threshold the session stops opening
work it cannot close. §2.20's Zeno directive already forbids unbounded runs; this extends the same
reasoning from a single execution to the session itself. Concretely: a task whose completion is
larger than the remaining budget is **not started**, it is written into the bridge as an open
thread with an owner (§H.2.4). Half a reading pass is the lossy half-state §H.0 warns about —
the incoming session inherits neither the text nor the understanding, only the claim that it was
begun.

**Failure mode this clause has.** It can fire too early and cost a session productive room, and it
relies on a judgement no instrument checks. Both are accepted: the asymmetry runs one way, since
an early handoff loses capacity and a late one loses the record.

> A session that notices it is full has already left it too late to say so cheaply.

---

## §H.11 The session's context is spent on findings, not on raw output

**Adopted at M's instruction, session 1.7.2, from that session's own accounting.** §H.10 says
*when* to hand off. This clause is about how much room there is to hand off *with*. The finding
that produced it: the largest single cost of session 1.7.2 was not analysis and not reading —
it was **raw tool output**. Two calls alone, a full URL dump and a language census that printed
one row per member, cost more context than the entire Λ_spectra rename. In both, rows were
printed where counts were wanted.

> **No tool call returns more than about twenty-five lines. Where the detail matters, the script
> writes it to a file and the call prints the summary and the filename.**

**Aggregate in the script, never in the response.** A census is computed, written to a TSV, and
reported by its *shape* — how many rows, how many distinct values, where the mass sits. The
detail is not lost; it is on disk, and the next session can read it if a question arrives that
needs it. This is the same discipline §H.4 applies to the bridge — *nothing is summarised that
can be carried* — turned around: **nothing is carried in the response that can be summarised
there and read from a file later.**

**Three practices follow, and each was a measured waste in 1.7.2.**
- **Consult §H by clause.** This protocol is now eleven clauses. The bridge cites the clauses it
  invokes, so the whole file need not be read to act on one of them.
- **Batch the gates.** They are cheap individually, which is how a session comes to run them six
  times. Run them **once at start for a baseline and once at close**, and in between **only when
  something generated has changed** — which is the condition C3 tests anyway.
- **Batch the rulings.** Decisions brought to M one at a time cost a full round trip each. Rulings
  that share a subject are put in one question.

**Failure mode this clause has.** A cap on output is a cap on evidence, and a session can satisfy
it by reporting a summary that the underlying file would not support — the failure §2.14 names,
arriving by a new route. The defence is that the file is written **before** the summary is
composed and stays in the bank, so the summary remains checkable after the session that wrote it
has ended. A summary with no file behind it is in breach of this clause, not in compliance with it.

> Printing a hundred rows to prove a count is the most expensive way to be believed.
