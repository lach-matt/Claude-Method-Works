#!/usr/bin/env python3
"""forward_markers.py — append a forward marker to every entry that register
1443, 1445, 1454 or 1457 corrects.

EDITORIAL ONLY. Nothing here recomputes anything, and no original claim is
altered: each marker is appended to the end of its entry, in the format register
1395 already uses ("WARNING: *…superseded by…*"), so the superseded figure stays
as history — which audit 13 exempts — while a reader is told where to go next.

The practice existed and had been applied exactly once. This applies it
consistently.
"""
import pathlib, re, sys

MARKERS = {
1385: "WARNING: *The row set behind the eighty-five is UNVERIFIED — see register 1443. No natural "
      "exclusion rule yields it and the nearest gives eighty-six, so the exponent 4.55, the σ scan and "
      "the +16% above Z ≥ 70 all rest on an unstated selection.*",
1390: "WARNING: *Corrected at register 1443: the ratio is monotone EXCEPT at palladium alone, where it "
      "falls 0.1756 → 0.1753. The endpoints and the never-exceeding-the-limit half both reproduce "
      "exactly; only the unqualified monotonicity is wrong.*",
1391: "WARNING: *Corrected at register 1443: n = 47, not 45. The three region offsets reproduce exactly "
      "at 3.798, 4.595 and 5.298, and the quoted spread of 0.108 IS the forty-seven-element figure — "
      "dropping any two tightens it to 0.097, so the fit ran over all forty-seven.*",
1396: "WARNING: *Corrected at register 1443: the entry splits the ELEVEN absent cells six-and-five and "
      "then scores against the TWELVE donor steps, which are different objects, and its list of nine "
      "names only seven — Pr and Tb are omitted. The base rate itself reproduces exactly at 3 of 12 "
      "against 36 of 94, so the refutation stands.*",
1401: "WARNING: *Corrected at register 1443: the four unforced resets are NOT period openings — thallium "
      "81 is not the first element of a period. All four open a SUBSHELL (Li 2s, K 4s, Tl 6p, Fr 7s), but "
      "so do eight of the fourteen forced, so the property is necessary and not sufficient and the four "
      "remain unexplained.*",
1403: "WARNING: *Qualified at register 1443: the eight a values are RECONSTRUCTIONS held in HANDOFF.md "
      "from earlier sessions' walk work, not measurements. This entry therefore claims agreement with a "
      "previously computed trajectory, which is weaker than it reads.*",
1407: "WARNING: *Qualified at register 1443 and superseded at 1435. This entry's `margin` is never "
      "defined; its ninety-nine is the CEILING-BEARING set, not the seventy-three with both bounds "
      "finite, and none of its figures reproduce from corridor widths. Measured instead on the RUNNING "
      "INTERSECTION, proximity IS the trigger, at a threshold of exactly zero, catching fourteen of "
      "eighteen resets with no false positives.*",
1409: "WARNING: *Clarified at register 1443: the seven block openings count the initial placement at "
      "lithium; register 1411's six count RE-placements, which excludes it. Both are self-consistent — "
      "nine matched plus six extra is fifteen moves. And per-block ascent cannot be corridor-respecting "
      "in blocks 5 to 8, whose corridor intersections are EMPTY (register 1447), so `zero violations` "
      "needs defining.*",
1413: "WARNING: *Clarified at register 1443 and measured at 1438. The seven misses are "
      "placement-INDEPENDENT; per-block ascent adds B 5 and Sc 21, which are placement-CAUSED — 106 − 9 "
      "= 97 and 106 − 7 = 99, so both figures are right and the clause was missing. And the 99 was "
      "FITTED: held out properly the score is 90, below plain Madelung's 96 (register 1445).*",
1415: "WARNING: *Corrected at register 1443: the percentages are exact — ceiling in the entrant's own "
      "block 84/99 = 85%, floor in the next block 71/80 = 89% — but the exception counts are "
      "undercounts. There are FIFTEEN ceiling exceptions, not eleven: the eleven s-against-s as stated "
      "PLUS four d-against-s at Mo, Rh, Pd and Au, so that set is not homogeneous. And NINE floor "
      "exceptions, not six, all of which are f or d intruders as stated.*",
1417: "WARNING: *Corrected at register 1443: SEVEN of twenty three-axis systems close, not three. The "
      "monotone-chain filter was applied as a stated principle rather than a computed test, so "
      "combinations may have been excluded on an unrecorded judgement. The landing-axis definitions are "
      "independently validated — they are the same quantity that reproduces 1415's 85% and 89%.*",
1341: "WARNING: *Superseded at registers 1416, 1457 and 1458. δ = a√p is not merely refuted but "
      "IMPOSSIBLE: δ is bounded as n → ∞ while a√(n−ℓ−1) diverges, the held series are flat to five "
      "percent where √p would demand a factor of six, and the Tietz potential has no Coulomb tail and so "
      "supports no defect at all. This entry's surviving claim is the one it actually makes — that a and "
      "δ SHARE AN INDEX, not that one number equals the other.*",
}

P = pathlib.Path("/home/claude/work/REGISTER-DATA.md")
s = P.read_text(encoding="utf-8")
done = skipped = 0
for n in sorted(MARKERS):
    pat = re.compile(rf"(^ {{0,3}}{n}\. .*?)(?=\n\n {{0,3}}\d{{3,4}}\. |\Z)", re.M | re.S)
    m = pat.search(s)
    if not m:
        print(f"  {n}: NOT FOUND — refusing to guess"); sys.exit(1)
    body = m.group(1)
    if "WARNING:" in body:
        print(f"  {n}: already carries a marker, left alone"); skipped += 1; continue
    s = s[:m.end(1)] + " " + MARKERS[n] + s[m.end(1):]
    done += 1

P.write_text(s, encoding="utf-8")
print(f"\n  markers appended: {done}   already marked: {skipped}")
print("  no original claim altered; every marker is an append in 1395's format")
