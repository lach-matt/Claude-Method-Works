# FINDING R4-08 — Chapter 34's missing "why" exists. It is in the chat corpus, as registers 1401–1410, and it was never carried into the volumes. NOT REPAIRED.

M, 6 September 2026, on finding R4-06: *"I would imagine this resolution exists somewhere. likely
in the lowdin chats if not in the lowdin papers. if it doesn't resolve from existing data, we will
have to use the sound solution and derive the 'why' ourselves."*

**It resolves from existing data.** The repository was searched exhaustively first, per the standing
rule and `RULINGS-R4d.md` §3: a concordance was built over all 352 conversations of the chat export
(875 windowed passages), and swept alongside the recovered Löwdin estate, the restore-point
instruments, the delivery and the volumes.

**The answer is in the conversation titled "The Method 1.7", staged there as registers 1401 to 1410,
and it is in none of the six volumes.** `method/proofs/resetrule.py` tests it; the selftest asserts
nine of the corpus's own recorded numbers.

---

## What the corpus says, quoted

**Register 1401, as staged:**

> *"a can be held exactly while the **running intersection of corridors** is non-empty, and must move
> exactly when it **empties**. That is arithmetic on the intervals alone, **independent of where a
> sits**. Fourteen forced moves, at Z equals 37, 42, 43, 45, 55, 58, 64, 65, 80, 91, 96, 97, 103 and
> 104. All fourteen are recorded resets, with **zero false positives** — the intersection never
> empties anywhere the record does not already reset. Four recorded resets are not forced this way:
> lithium 3, potassium 19, thallium 81 and francium 87, every one the first element of a new period."*

**Register 1402:**

> *"the eighteen are a property of one trajectory, not of the corridor. … Placing a at the nearest
> endpoint gives ten resets; always-lower gives twelve; always-upper seventeen; the midpoint
> twenty-one; the farther endpoint twenty-two … **Only emptiness is trajectory-free**, which is why
> the fourteen stand and nothing beyond them does by that route."*

**Register 1403:**

> *"a is placed at an endpoint, never in the interior. … The rule is therefore: **a takes the
> tightest finite non-zero bound**, L where it exists as a real surd, U where it does not."*

**Register 1404:**

> *"four pairs of resets are single events, because the corridors meet at a point. … The intersection
> is a single point, empty as an open interval, so the second reset is forced and **the two are one
> event**."*

## Tested, and it holds

| what | result |
|---|---|
| **1401's rule run over the corpus's own corridors** | forces exactly **37 42 43 45 55 58 64 65 80 91 96 97 103 104** |
| false positives | **none** |
| recorded resets it does not force | **Li 3, K 19, Tl 81, Fr 87** — exactly the four 1401 names |
| **1403's placement rule** | every one of the eighteen lands exactly on a corridor endpoint. **11 at L, 7 at U, none in the interior.** |
| **1404's four pairs** | Mo/Tc meet at 1.000000, Gd/Tb at 0.707107, Cm/Bk at 1.366025, Lr/Rf at 1.984059. **All four are a single point.** |
| **1402's claim** | the count runs from **9 to 75** over the same 106 steps and the same corridors, across five placement policies. Confirmed. |

## What this settles about Chapter 34

**§34.6 gives no reason for its reset claims, and a reason exists.** The reset condition is a
statement about **intervals**, not about subshells: `a` is held while the corridors seen since the
last reset still share a point, and must move when they do not. **Nothing in it mentions a
subshell**, which is why *"it never resets mid-subshell"* was never a consequence of the rule and is
an observation about where the rule happens to fire.

**And 1402 is the deeper point.** The count of eighteen belongs to one placement policy. §34.6's own
next paragraph already says as much — *"eighteen is the cost of walking Z in order, not the cost of
the table"* — but it does not say that fourteen of the eighteen are **forced by the corridor alone**
and the other four are not. That is the division the chapter needs and does not have.

**1404 is the derived form of something this pass measured independently.** `walkresets.py` found
eight of the eighteen recalibrations to be **boundary touches** where `a` does not move at all,
because `walk.py` tests the corridor strictly and the carried value sits exactly on an endpoint.
Register 1404 derives the same thing from the other end: consecutive corridors that meet at a single
point make the second reset an artefact of the first. **Two routes, no shared code, same object.**

## Two places where the staged registers do not survive as printed, and both are small

**1401's characterisation of the four covers three of them.** Li 3, K 19 and Fr 87 are each the first
element of a period. **Tl 81 is not** — period 6 begins at caesium, Z 55. Thallium opens the 6p
block. The clause *"every one the first element of a new period"* should read *a block opening*, or
name the exception.

**1402's five counts are not reproducible from what it prints.** It gives ten, twelve, seventeen,
twenty-one and twenty-two for five placement policies and does not define the policies precisely
enough to reproduce them; the sixth figure needs a random seed it does not carry. Five policies
implemented here give nine to seventy-five depending on whether corridor membership is tested open
or closed. **That is recorded as POLICY-NOT-DEFINED and is a refusal, not a finding.** 1402's claim
is confirmed; its five numbers are not checkable as printed.

---

## The same search answered §34.9 as well, and the answer is older than the chapter

The sweep was run for two questions. The second — *is the true reason for L = −∞ at an f opening
stated anywhere?* — is answered twice, and both answers predate the chapter's false premise.

**Computed in session, in "The Method 1.6" at message 1957**, in the run that produced the f-domain
paragraph:

> *"4f has p = 0. 0 is the FLOOR of the node count — no subshell can have fewer nodes than none. so
> no rival is below it, and L = −∞ necessarily. … **and 5f: p = 5−3−1 = 1. one rival could be below
> it — 4f, p = 0. but 4f is FULL by the time 5f opens (Pa, Z=91), so it is not admissible. the
> corridor is one-sided there too.**"*

**Twelve messages later, at message 1969, the chapter summary carries only *"at any f opening
p = 0"* and the 5f clause is gone.** That is the whole history of the defect: it was right when
computed and lost in the summary.

**And banked afterwards as deviation 16z-05**, in the conversation numbered 127:

> *"At Pa (Z = 91, entrant 5f) the corridor is one-sided because every admissible rival has larger n
> (all smaller-n subshells full) — **admissibility, not the node floor**. … The conclusion (no
> two-sided f corridor) stands; the stated reason holds at one of the two f openings."*

**So neither half of Chapter 34's problem needed deriving.** Both reasons were in the corpus before
the chapter was written, one of them in the very session that wrote it. What §34.6 and §34.9 lack is
not knowledge; it is the carriage of knowledge already had. **That is the shape of this whole
finding, and it is the argument for `RULINGS-R4c.md` §2** — subject matter in the sources that
belongs in the main volumes is brought in.

**Finding R4-06 is corrected accordingly**: its claim that the record does not carry the f-domain
reason was wrong and is withdrawn in that file.

## What is owed, and it is M's

**The derivation belongs in the volumes.** `RULINGS-R4c.md` §2 says subject matter in the sources
that belongs in the main volumes is brought in, and this is the clearest case yet: a derived,
trajectory-free reset condition with zero false positives, sitting in a chat and not in the book,
while the chapter states an undefended claim in its place.

M rules on three things:

1. **Whether registers 1401–1404 are seated as Register entries** and cited from §34.6. They are
   staged, not seated, and the Register is append-only.
2. **§34.6's sentence.** The measured replacement is available and is stronger than what stands:
   *fourteen of the eighteen recalibrations are forced by the corridors alone, independent of where
   `a` sits; the other four are the placement rule's, at lithium, potassium, thallium and francium.*
3. **1401's "first element of a new period"**, which is true of three of the four.

**Nothing is repaired here.**
