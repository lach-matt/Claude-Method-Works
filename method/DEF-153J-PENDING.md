# DEF-153J — the readings estate, triaged. STAGED, NOT ACTED ON.

## Why shiftcheck cannot explain this estate

`shiftcheck --all` returns **0 EXPLAINED** even with both of this session's bands declared
(`9645:20` for §34.6 at BUILD96, `10752:2` for §D.2 at BUILD95). The reason is diagnostic:
`r2-reg9a` moves `§6.2 L1594 -> L1596` — a **+2 shift at line 1594**, far above both pivots.
Neither edit made in this session caused it. The estate carries drift from builds that predate
this session, and explaining it would need a per-vintage band map reaching back through every
build since each golden was banked.

That is the wrong route. `close_rebank.py` re-banks a golden **by running its instrument**, and
running does not need the shift explained at all — it needs the instrument's anchors to still
resolve to the right text. So the question is not "can the move be explained" but "does the
instrument still measure the thing it names".

## The triage

Each moved golden's banked and current output compared line for line, with every run of digits
masked. A diff that survives the mask is a TEXT change; one that vanishes is numbers only.

| class | count | what it means |
|---|---:|---|
| **numbers only** | **17** | same shape, same words, different figures — the volume moved under it |
| **text changed** | **41** | the instrument now prints different words; a reading, not a re-bank |
| **line count differs** | **15** | rows appeared or vanished; needs inspection before either route |

    numbers only    extent kinds r2-ch16k r2-ch19b r2-ch20b r2-ch21a r2-ch24a r2-ch26a
                    r2-reg10a r2-reg11a r2-reg12 r2-reg4a r2-reg5a r2-reg6a r2-reg7a
                    r2-reg8a r2-reg9a

    line count      r2-21a r2-ch16a r2-ch16f r2-ch16i r2-ch16o r2-ch16u r2-ch16x r2-ch17b
                    r2-ch18b r2-ch22a r2-ch22a2 r2-ch22b r2-reg1a r2-scf r2-warn

    text changed    the remaining 41 (r2-24a, r2-25b, r2-26c2, r2-27a2, r2-28a3, the r2-ch16*
                    and r2-ch1x-2x families, r2-regsweep, r3-em)

## THE CAVEAT, WHICH IS THE POINT

**"Numbers only" is necessary and not sufficient.** A figure can change because the volume moved
under a correct anchor, and it can change because the instrument now reads the WRONG LINE and
reports a wrong figure with a perfectly ordinary shape. Both produce a numbers-only diff, and the
second is invisible to this triage.

This session already met the second case: `r2-ch17e` asserted `L11832 is R.7` when R.7 stood at
L11840, and the assertion was a falsehood that ran clean. A numbers-only diff on that instrument
would have looked exactly like a safe re-bank.

So the seventeen are CANDIDATES, not a work list. Each needs its anchors proved — `proveanchor.py`
is the instrument for it: a successor is trusted only when it reproduces its predecessor's golden
byte-exact on the PRE-shift bundles. Nothing here may be re-banked on the strength of the mask
alone.

## Order of work, per M's earlier ruling

Readings first, then `reg1-04`'s front-matter count repair — which HANDOFF-152-RESUME records as
R3's to make ("R3 repairs it with its class"), and which entry 1804 has now widened again. Ruling A
still holds until the readings are done: `register_counts.py --write` is NOT run, and the drift is
scored.
