# STRING-PF CONVEXITY DEFECT — RESOLVED (chat 63 by title / "chat 62" per HANDOFF-11) — CHANGE CERTIFICATE BUILD56 → BUILD76 main

## Verdict (M ruled): the reconstruction was right; the book was wrong on one word.
- §31.2.2 said log d(N) is "monotone, convex and 3-monotone, with V ≈ 147 at N ≈ 14". Measured: monotone ✔, CONCAVE ✘(was "convex"), 3-monotone ✔, V ≈ 147 ✔.
- Book vocabulary read (BUILD56 §23.10.1): monotone/convex/3-monotone = signs of 1st/2nd/3rd finite differences — ordinary sense. V = w/e (§23.1–23.2).
- V(log d(N)) at N=14 = 146.6 → the sentence's subject is log d(N) as written. V(d(N)) = 3.57.
- d(N) verified by two independent routes (series expansion; Euler σ-recurrence), identical to N=16.
- log d(N): 2nd differences −0.313 … −0.032 (N=2..15) all negative; 3rd differences +0.104 … +0.003 all positive.
- Consistent with §31.2.5's own d(N) ~ exp(4π√N) (concave logarithm).

## Sweep for casualties (M-directed, exhaustive) — ONE site
- Main (BUILD56, 18,446 lines): sentence occurs once (line 8675). No Register entry behind §31.2 at all. Pointers to §31.2 (lines 632, 2510, 7638, 8604, index 11442/11445) state nothing about convexity. §31.2.5 agrees with the correction.
- Compendia (BUILD75, 32,782 lines): NO casualty. IoI string-PF entry (18643–18652) carries coordinates, d(N) values (re-verified), E=0, pointer §31.2.3 only. "3-monotone"/"bracketable"/"steeper than"/"V≈147": zero hits. All 32 "convex" lines are other objects.
- Drive-wide phrase search "convex and 3-monotone": only main-volume files (BUILD9/10/53R/54/55/56, the two press copies "The Method 1.6.md") + the discrepancy note. No compendium/Register/paper press copy carries it. Pressed main PDF carries it by construction until re-pressed (inferred).
- IoI entry: NOT revised (M asked; answer measured: nothing in it is touched).

## Edits in BUILD76 main (all M-approved by slip; measured diff guard below)
1. §31.2.2 restated (§23.5.1/§23.10.2 pattern): concave + the three difference signs + "An earlier version of this line said convex … recorded at register 1787." (2 lines → 5 lines at 8675.)
2. Register 1787 appended after 1786 (append-only; settled form; "(a correction.)"; cites no register — none exists behind §31.2).
3. Register extent restated to include the entry (register 1784's rule): 15 word sites "one thousand six hundred and thirty"; line 7374 "1,630 entries, 1 to 1787, at this build (2026-08-29)"; line 7659 "1,630 at this build"; front matter "1630 entries, 1 to 1787", "165 to 1787, 1,466 entries", "mature record 165–1787".
4. Kinds table recomputed by the banked kinds.py (extracted verbatim from BUILD75): correction 143→144; measurement printed 498 → instrument writes 499 (pre-existing stale-by-one, see findings); "over the 1,560 entry headings".
NOT done (by slip): no Chapter 28 extension (Ch. 28 no longer prints items; rule at its head: cite the entry, don't reproduce the record). Load-bearing/citation-count lines (571/387/701/970) NOT restated — declared press-time recomputed; see findings.

## Measured-diff guard (difflib, BUILD56 → BUILD76)
- 23 hunks; 24 lines deleted, 30 added; 0 unauthorised deletions (every deleted line discriminated against the authorised site list).
- Reverse-applied diff recovers BUILD56 md5 5292fce89637c6b495363f76f99a4885 EXACTLY.
- BUILD76 main: 1,977,372 B · md5 a4fbbc49d58ec6c6d6dd71a13f116765 · 18,452 lines.
- BUILD75 compendia UNTOUCHED (2,471,737 B · md5 de89d94c0c371d4ac325c37c55f32915 · 32,782 lines).

## Findings for the WORKING register (editorial; never reader-facing)
- W: kinds.py on BUILD56 gave measurement 499 vs printed 498 BEFORE this session's entry — the printed column lagged one append (1786). Instrument unchanged.
- W: register_cites.py (banked in BUILD75, run on the split per-volume files) measures 584 / 391 / 856 / 1050 vs printed 571 / 387 / 701 / 970 (2026-08-26 press) — the load-bearing table + three citation-count sentences are stale and must be recomputed at Phase 4 press; ranking moved (1649 now 10×, 1526 8×). Not restated by hand.
- W: 31 register numbers are cited somewhere without an entry heading (incl. 1710); the three-body block 1713–1724 is NOT in the Register yet → Register pass.
- W: B10-CERTIFICATE's "FLAG carried out" (string-PF convexity) is CLOSED by this certificate.
- W: HANDOFF-11 self-identifies as chat 61→62; project chat titles run 61, 62 (which produced BUILD75/HANDOFF-11); this session is 63 by title.

## Instruments used this session (re-derivable; not banked as new files)
- tower.py (Drive tower-2.py, 1,213 B, md5 c0bce27abe23ad939d297ac1022a01d7): 976/1,654/2,535/13,585/70,905/199,130 ✔ gate.
- d(N): 24-fold nested series expansion of ∏(1−qⁿ)⁻²⁴; Euler recurrence d(N)=(24/N)Σσ(k)d(N−k) (Fraction-exact). V=w/e per §23.1.
- kinds.py, register_cites.py: extracted verbatim from BUILD75 FILE blocks.
