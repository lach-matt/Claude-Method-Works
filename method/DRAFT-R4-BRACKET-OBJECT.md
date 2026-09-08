# DRAFT — register 1880's owed expansion is not owed: the object was already printed

**NOTHING IN THIS FILE IS IN THE STORE.** No volume byte has moved, no Register entry written.

## What register 1880 says

Its closing clause: *"Its prose placement belongs to the time chapter, and **the Mathematical
Compendium prints no object for the bracket system — an expansion owed there and not written
here.**"*

## What the Mathematical Compendium prints

**`### The tower's two ends joined`**, at L2135–2148, family **K**. Its headline carries every figure
register 1880 says the compendium has no object for:

> *"at every consecutive stage Λ_{D+1} → Λ_D the correspondence from a rank above to the ranks below
> is a **GAP-FREE INTERVAL with both endpoints monotone** — no exception across all **199,130 cells**
> — so the tower's chains form **ONE directed system of monotone brackets χ(Λ₁₃) → … → χ(Λ₈)**,
> composition of the five stage-brackets containing the direct bracket with **slack ≤ 2 rank units**;
> the projection from Λ₁₃ covers ALL of χ(Λ₈), **ranks 3 through 20** without gap … the 1D chain is
> the system's **TERMINAL OBJECT** … the 14D direction is the same system's **LIMIT**; the strict MAP
> form is **REFUTED, branching 4, 4, 6, 8, 9** growing with height"*

And its grade line names the subject outright: *"Proved — M §12.11.0.11, **on the rebuilt tower and
its bracket system**."*

**That is the object. The expansion is not owed, and was not owed when 1880 was written.**

## When it entered

`tools/buildtrace.py --first "The tower's two ends joined" --stream compendia` reports **first
appearance BUILD77**, with BUILD75 absent. It is present at BUILD77, BUILD150 and BUILD179 — the
last archived compendia build — and in the live bundle now. **Register 1880 was seated at main
BUILD125, when the compendia bundle stood at BUILD268**: roughly a hundred and ninety compendia
builds after the object was there.

## Why nothing caught it, and it is the same fault twice

`compendia2.py`'s `bracket_system()` tested 1880's claim and confirmed it. It searched **object
headings in families B and T** for the words `stage-bracket|bracket system|rank value|fibre`.

**The object is in family K**, so it was outside the search; and it is **named for its result rather
than its mechanism** — *"The tower's two ends joined"* — so it matches none of those four words. The
test looked for the object by the name it would have had if it did not exist.

**That is M's correction again, in an instrument: a pattern narrower than the material.** It is the
third instance this leg, after `compendia3`'s dotted parent regex (which read 14 where the figure was
73) and register 1736's author-and-year match (which could not see a wrong year on a real author).

## What is owed instead

**Nothing in the volumes.** But **register 1880 is wrong in its closing clause, and a Register entry
is never edited** — so the repair, if M wants one, is a new appended entry citing 1880 and naming the
object it says is absent. The rest of 1880 is unaffected: its measurements are the object's own.

RECORDED, NOT REPAIRED.
