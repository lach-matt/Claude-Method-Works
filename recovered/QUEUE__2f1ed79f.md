# SPECTRA QUEUE — what is on disk and what it is for

**Uploads land at `/mnt/user-data/uploads/` and PERSIST across sessions.** Nothing needs
to be done to receive them. A new session lists them by TIME, never by name — register
690 — and works through this queue.

    ls -lat --time-style=full-iso /mnt/user-data/uploads/

## Done · in the compendium

  Ne I     4 channels   high Rydberg ns/nd, n = 11–20, delta 1.2921 vs published 1.300
  Ne II    levels only  no series of 3 in what was read
  Li II   10 channels   the cleanest QDT demonstration here — delta collapses with l
  Li III  13 channels   hydrogenic, returns zero with an l-ordered residual
  Bi II    7 channels   full table from ONE full-page capture
  Bi III   7 channels   Sc III 9 · Si II 9 · Mg I 10 · Ar II 4 · Ba III 10
  Zn I     2 channels   BUILT AND VERIFIED, NOT YET MERGED — np n=13–40, 28 members

## Withdrawn

  Ca I     FABRICATED — twenty-one values generated, not read. Register 695.
           Must be re-read from source, never from memory of the format.

## Wanted · in priority order

  1  Si I      542 levels, largest untouched · limit 65747.76
  2  Ar II     tail beyond level 125 of 419 · limit 222848.30
  3  Ca I      re-read properly · first limit 49305.95
  4  Zn II     3d10.nl series · limit 144892.6
  5  Ca II     3p6.nl series · limit 95751.88
  6  Sc IV     129 levels · limit 592732 +/- 3
  7  Be II     limits 107121.38 / 107127.96
  8  Ne II     the 2s2.2p4 core series · limits 330388.6 / 331031.5 / 331309.2

## For each species, the four things needed

  the CONFIGURATION column   enough to identify core, n and orbital letter
  the TERM and J             a channel is per (core, l, term, J)
  the LEVEL in cm-1          the measurement
  the LIMIT line             at the foot of the ASD output, after a double rule

**Nothing else is needed.** Leading percentages, Lande factors and references can be
skipped — no column of the compendium uses them.

## And the three free checks

  QD-CHECK.tsv     37 elements, independent compilation
  l-ordering       the defect must FALL as l rises
  J-consistency    same series, different J, same defect

*Fabricated data fails all three; it cannot fake structure it does not know about.*