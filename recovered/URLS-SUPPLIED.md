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

## The block, stated precisely

**THREE fetches this session, three IDENTICAL bodies.** Requested in turn:
`spectra=H-Ar`, `spectra=Sr`, and `spectra=H-Ar` with `sremoval=on`.
Every `destination_url` read back as **`spectra=H-DS+i`** — a prior response.

So the cache is pinned per host+path for the session, and varying the query
string does not move it. **This is register 1526's rule, now confirmed for a
second endpoint and sharper than it was recorded: it is not one query per
session, it is ONE RESPONSE per session, whatever is asked.**

## What breaks it

A URL M pastes into the conversation. Those have broken the cache every time —
the whole X-ray capture set and the K-Kr ladder were fetched that way. **The
address is not the scarce thing; the cache-miss is.**