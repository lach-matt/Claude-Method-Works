# URLs M has supplied, recovered from the transcripts (R 1595)

*I told M at register 1594 that the ladder "needs a URL supplied by M". That was
wrong: **M had already supplied them**, and they are recoverable from
`/mnt/transcripts/`. The block is the FETCH CACHE, not a missing address.*

## NIST ASD — ionisation energies (`ie.pl`)

    https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on&format=2&ion_charge_out=on&order=0&spectra=K-Kr&sremoval=on&submit=Retrieve+Data&units=1
    https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on&format=2&ion_charge_out=on&order=0&spectra=K-Kr&submit=Retrieve+Data&units=1
    https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on&format=2&ion_charge_out=on&order=0&slevel=on&spectra=K-Kr&sremoval=on&submit=Retrieve+Data&units=1
    https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on&e_out=0&format=1&ion_charge_out=on&level_out=on&seq_out=on&shells_out=on&sp_name_out=on&spectra=H-Ar+I-III&unc_out=on&units=0
    https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on&e_out=0&format=1&ion_charge_out=on&level_out=on&seq_out=on&shells_out=on&sp_name_out=on&spectra=Rf-Og+I&unc_out=on&units=0

**`sremoval=on` is the parameter that produces the MULTI-CHARGE ladder** — it is
what gave `LADDER-K-Kr.tsv` its 495 rows across every ionisation stage. Without
it the query returns one row per element.

## NIST ASD — energy LEVELS (`energy1.pl`)

    https://physics.nist.gov/cgi-bin/ASD/energy1.pl?spectra=K-Kr&units=1&format=2&order=0&level_out=on&j_out=on&submit=Retrieve+Data

**This is the form all 61 paths in `FETCH-PATHS.tsv` use**, with only the
`spectra` value changed.

## The block, stated precisely

**THREE fetches this session, three IDENTICAL bodies.** Requested in turn:
`spectra=H-Ar`, `spectra=Sr`, and `spectra=H-Ar` with `sremoval=on`.
Every `destination_url` read back as **`spectra=H-DS+i`** — a prior response.

So the cache is pinned per host+path for the session, and varying the query
string does not move it. **This is register 1526's rule, now confirmed for a
second endpoint and sharper than it was recorded: it is not one query per
session, it is ONE RESPONSE per session, whatever is asked.**

## THE PARAMETER SETS DIFFER BY ENDPOINT (R 1635)

| endpoint | its own parameters |
|---|---|
| `ie.pl` | spectra units format **order** sremoval slevel at_num_out ion_charge_out submit |
| `energy1.pl` | spectra units format **output page_size multiplet_ordered** level_out j_out temp submit |

**`order=0` is `ie.pl`'s. `energy1.pl` rejects it with 'Unknown parameter'
and does not say which one.** Four fetches were spent on that name.

⚠ **A URL THAT WAS SUPPLIED IS NOT A URL THAT RETURNED DATA.** The
`energy1.pl` form was my own untested reconstruction and I later called it the
only one that had ever worked. Read the transcripts for that distinction.

## THE SYNTAX DIFFERS BY ENDPOINT (R 1633)

| endpoint | what it takes | evidence |
|---|---|---|
| `ie.pl` — ionisation energies | ranges **AND stage suffixes** | `Rf-Og+I`, `H-Ar+I-III`, `Db+I` |
| `energy1.pl` — **LEVELS** | ranges, **NO STAGE** | `K-Kr` — the only one that has worked |

**`spectra=Cs-Ce+I` returns 'Unknown parameter' on `energy1.pl`.** Isolated by
differencing against the working URL: every other parameter identical, one
differs. The stage suffix is `ie.pl` syntax and does not transfer.

## THE `spectra` SYNTAX — ranges only (R 1632)

    spectra=Db+I           one element, one stage
    spectra=H-Ar           an element RANGE, all stages
    spectra=K-Kr           an element RANGE
    spectra=H-Ar+I-III     element range + stage range
    spectra=Rf-Og+I        element range + one stage

**A SEMICOLON LIST RETURNS 'Unknown parameter'.** I invented that form from the
help page's phrase "multiple spectra" without checking it against what had
worked. Ranges over-fetch; that costs nothing.

## THREE FAILURE MODES (R 1631)

| what | symptom |
|---|---|
| URL never in a result | **REFUSED** — permission |
| constructed near a permitted one | **SERVED THE PERMITTED BODY**, not the one asked for |
| URL longer than ~230 chars | **REFUSED FOR SIZE** — a 329-char batch failed |

**Keep every constructed URL under 230 characters.** The exact limit lies
between 225 and 329 and was not probed — finding it would cost fetches better
spent on data.

## ~~TWO BLOCKS~~ — ONE MECHANISM (corrected at R 1629)

| endpoint | mechanism | symptom |
|---|---|---|
| `ie.pl` | a URL **WAS** permitted (a search returned one) | SERVED — but **the permitted URL, not the one asked for** |
| `energy1.pl` | **no** URL permitted | REFUSED outright |

**THERE IS NO CACHE.** One permission layer, two exits. The three identical
`ie.pl` bodies were not a stale cache — only ONE such URL had ever appeared in
a result, so only one body was ever available to serve.

**The refusal is the safer exit** — it cannot be mistaken for a result, whereas
being served a different URL's body can, and at R 1595 it nearly was.

⚠ **VARYING THE QUERY STRING IS FUTILE.** It changes nothing on either
endpoint. Searching first does not help for `energy1.pl` — it returns
`levels_form.html`, the human form, not the query endpoint.

## What breaks it

A URL M pastes into the conversation. Those have broken the cache every time —
the whole X-ray capture set and the K-Kr ladder were fetched that way. **The
address is not the scarce thing; the cache-miss is.**
