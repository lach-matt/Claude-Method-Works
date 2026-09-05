# FINDING R4-01 — §34.6 and register 1333 break the eighteen resets into 8 / 6 / 4; the instrument that produced them gives 12 / 7 / 4. An object defect. NOT REPAIRED.

Found 5 September 2026, under M's ruling that a false claim is an object that is false when the prose is stripped
away. This one is: no rewording reaches it, because the numbers themselves are wrong and the accounting they belong
to does not close.

## What the volumes print

Main volume §34.6 (member line 9638), *The walk*:

> **`a` is carried between elements and resets eighteen times.** Every reset is a **subshell opening** (8), an
> **aufbau exception** (6), or the **return from one** (4) — Tc after Mo, Tb after Gd, Bk after Cm, Hg after Au.

Register entry **1333** (member line 5010) states the same partition:

> **EVERY RESET IS AN OPENING, AN EXCEPTION, OR A RETURN — ALL EIGHTEEN ACCOUNTED.** *Eight at a subshell opening,
> six at an aufbau exception (four of them also openings), and four at the RETURN from an exception … And the
> converse fails: eleven openings leave a unchanged.*

## What the instruments give

`walk.py` and `resets.py`, the pair that produced this section, were recorded as **not held** (Working Register
L7914: *"The record's walk instruments (walk.py / brack.py / scorer.py) are not held"*). **They are held.** The
consolidation pass recovered them into `extracted/archives/restore-point-2-13/`, with 345 others. Their one
dependency, `ground.py`, is in the mirror at `drive/The Method Materials/LOWDIN-DELIVERY-1/ground.py` and is
**byte-identical** (md5 `236975ac23aa29960d4f7c2a4d200cd6`) to the seated member `LW1-ground.py`, so there is no
question which ground configurations are meant.

Run on that ground:

- `walk.py` — **106 steps · 106 satisfied · 18 recalibrations**, at Z = 3, 19, 37, 42, 43, 45, 55, 58, 64, 65, 80,
  81, 87, 91, 96, 97, 103, 104. The eighteen, and the 106, are confirmed exactly as printed.
- `resets.py` — classifies those eighteen: **opens a subshell 12 · aufbau exception 7 · neither 4**, and
  **"subshell openings that do NOT reset : 11"**.

**That last line is the corroboration that this is the right instrument.** Entry 1333's *"eleven openings leave a
unchanged"* is `resets.py`'s output verbatim. The same run that supplied the entry's eleven supplies twelve and seven
where the entry prints eight and six.

The full classification, enumerated:

| class | count | elements |
|---|---|---|
| opening only | 7 | Li, K, Rb, Cs, Tl, Fr, Rf |
| exception only | 2 | Mo, Rh |
| both opening and exception | 5 | Ce, Gd, Pa, Cm, Lr |
| neither — the four returns | 4 | Tc, Tb, Hg, Bk |
| **total** | **18** | |

So: openings 7 + 5 = **12**; exceptions 2 + 5 = **7**; returns **4**.

## Why it is a defect and not a reading

**The printed partition does not close on its own arithmetic.** Entry 1333 says eight openings, six exceptions, four
of the six also openings, four returns. Distinct that gives 8 + 6 − 4 + 4 = **14**, not the eighteen the headline
claims are all accounted for. Under the instrument's figures it does close: 12 + 7 − 5 + 4 = **18**.

**And no reading of the text reaches 8 and 6.** Openings total 12; openings that are not also exceptions, 7;
exceptions total 7; exceptions that are not also openings, 2; the overlap is 5, not the four the entry states. There
is no partition of these eighteen elements that yields eight and six.

**The likely origin, offered as a lead and not as a finding:** the seventh aufbau exception is **Lr**, whose ground
state is 7p¹ where Madelung gives 6d¹ — a relativistic exception a classic six-item list omits. That accounts for six
against seven. It does not account for eight against twelve.

## What would repair it

The numbers, in both places: **twelve at a subshell opening, seven at an aufbau exception (five of them also
openings), and four at the return** — which is eighteen accounted, and closes. Nothing else in §34.6 moves: the
eighteen, the 106, the four named returns and the eleven non-resetting openings are all confirmed as printed.

**Not repaired here.** It is a change to a reader-facing volume and to a seated Register entry's figures, so it needs
M's ruling and a guarded build with an entry that cites 1333 and preserves both states.

## Recorded beside it

**`walk.py`, `brack.py` and `scorer.py` are not missing.** The Working Register records them as not held, and every
figure they produced as record-carried. That record is stale: the restore point holds 348 instruments, and this pass
reproduced §34.6's central figures from them in minutes. **Before any further claim in Chapters 34 to 36 is called
unprovable, the restore point is searched.** That is a finding about the record, not about the book.
