# The adversarial review of the complete proposal and the pitch (2026-09-12)

**What this is.** The author asked for `California_Sovereign_Infrastructure_v0.2.md` and `Pitch_v0.2.md`
to be reviewed exhaustively and adversarially, the flags corrected, and both re-rendered. This file is
the record of that review: every flag, where it was found, what it is, and its disposition. A flag
that is a fault in an instrument is corrected in the instrument and every document that reads it is
re-rendered; a flag that is a fault in the rendering is corrected in `tools/proposal.py`; a flag that
is a limit rather than a fault is stated in the document rather than removed.

## Flags that were faults in the instruments (corrected, every renderer re-run)

1. **The closing plant carried no O&M.** `hourly3.price_delta` priced the capital that closes the load
   (the larger block and field, the second day of store, the pump-turbines and reservoir) as a financed
   annuity with **zero** O&M, so every whole-load price (mirrors route and adopted route), and the
   post-bond price, understated. Corrected: `hourly3.closure_om_m` takes the closing plant's O&M as
   proportional to direct capital at the design's own O&M-to-capital ratio (ASSUMED, stated); the
   water side carries `joinder.HYDRO_OM_SHARE` at 1.5 / 2.5 % of capital a year (ASSUMED band);
   `both.point` carries `extra_om_m` and prices with it; `pilot.consequence` and the mirrors route
   price with it. The whole-load and post-bond figures moved and the documents say so.
2. **Four environmental rows were computed at a route the author did not adopt.** `majors.ra`,
   `majors.washing`, `majors.land` and `minors.jobs` took the mirrors route (block ×1.25, field ×1.5)
   where the adopted route is block ×1.5, field ×1.25. Corrected: they take the adopted route from
   `both.py` (lazily), with `mirrors` and `water` kept as named alternatives.
3. **Title II's permanent jobs counted the full water route's modules.** `minors.jobs` used
   `modules_to_close(share=1.0)`, about thirty modules, where the adopted route builds fifteen to
   seventeen. Corrected to the adopted modules.
4. **Two heads in one route.** `both.py` sizes the water at 500 m for both cases while
   `joinder.hydraulic_per_m3(case)` and `aquacost.water_route` priced the lift on the water's bill at
   the case's own band, 300 m at critical. Corrected: `hydraulic_per_m3(case, head=None)` takes a head,
   and the adopted route passes its one head everywhere; the site term in `sites.py` now asks for the
   head the route is priced at, 500 m, rather than the band's 300 m bottom.
5. **The gen-tie's price disagreed with the design's own line.** `titleone.gentie` reported the
   switchyard band uncalibrated ($600 / 900 M) while the design's line carries the calibration
   ($771 / 1,157 M). Corrected: the gen-tie reports the design's line.
6. **The study register's field row was stale.** `studies.py` typed "~27 M m² critical / 14–21 towers"
   where the design is 30.9 M m² and 24 towers. Corrected: computed from `cspchain.design` at import.
   The architecture row's run record also carried the pre-correction price deltas and now names the
   function instead.

## Flags that were faults in the rendering (corrected in `proposal.py`)

7. §C: a line break split "$" from "190–350/MWh"; the peak-revenue row said "every peak hour" where
   the instrument overrides the four peak hours of every day; the carrying-cost row said "as stated"
   for a computed figure (Title I stated $1,933 M; the instrument gives $1,954 M). All three relabelled.
8. §C: the fidelity table printed Cerro Dominador at 0.12 with no note; the record's note ("2023;
   hot-tank damage, plant largely stopped") is now printed beside every ratio.
9. §D: the salt-tower CSP row's "band top" column repeated the mid figure because `firmpower.size_csp`
   has only a mid case; the cell now says so.
10. §E: the "Helios as proposed" column is the plant scaled to 18.1 TWh (42.9 M m², 34 towers), not the
    plant as specified in §C (45.6 M m², 36 towers); the header now says "scaled to 18.1 TWh".
11. §F: the sizing table showed only the design; the adopted route's aperture, towers, block and land
    are now printed beside it, and the pitch says the adopted route grows the field by a quarter and
    the block by half.
12. §H: the row "energy the water returns / lift it needs / surplus" mixed the sized budget with the
    dispatched energy. Relabelled as sized / dispatched / lift / surplus, and a paragraph now states
    the finding it exposed: the water is sized to return half the shortfall as sized and the run
    dispatches about half of that, because the larger block serves first — the modules are sized on
    the shortfall, the water plant runs at about half its evening sizing, and all the water is
    delivered regardless.
13. §H: the mirrors-alone figure Title III prints ($5.7 / $9.5 B, `hourly3`'s one fixed route) differs
    from the ladder's own mirrors-only point at critical ($9.0 B, the scan's grid). Both are now
    printed and the difference explained rather than left for a reader to find.
14. §H: Figure 7's caption said share 1.0 "has no feasible point"; share 1.0 on the ladder carries the
    larger field and is feasible — what has no feasible point is water alone with the field and store
    at design. Caption corrected.
15. §H: the hydraulics paragraph quoted the mid head and the critical round trip from different heads;
    it now states the one head the route is priced at, both cases' figures at it, and the O&M band.
16. §I: the priced table did not close arithmetically (adders, premium, studies and credit with no
    base or overheads). It now runs direct lines → adders → contingency, EPC and tax → studies →
    premium → overnight → escalation and interest → gross → credit → net.
17. §L: `str.capitalize()` had lower-cased "MW_th" in the pilot note.
18. §M: the transmission peak is identical at both cases (the block is the same size at both) and the
    text now says why; the switchyard figure is the design's line (flag 5).
19. §M: the post-bond price is now the adopted route's (register plant plus closing plant O&M), and
    the per-year table shows the closing plant's O&M as its own row.
20. §N: the LT-MED comparison ("6.4×") was the renderer's own arithmetic; it now reads
    `joinder.topping_per_m3`. "80–50 acre" is now "80 / 50 acre". The fractional module count is
    printed with the whole modules built beside it.
21. §P: per-node land, washing and towers were at the mirrors sizing; now at the adopted route.
22. §Q: the jobs paragraph named "the closed block" without saying which route; now the adopted one,
    with the water modules the Title II figure counts.
23. §S: the flaw resolutions quote figures as recorded on the day each was closed, several of which
    later passes moved; a note now says so, and that a status is never flattened.
24. §T: the source list split a parenthetical citation on its semicolon ("Albrecht & Ho, Sandia
    (AIP Conf. Proc. 2020" / "Sandia 2022 performance evaluation)"); the splitter now respects
    parentheses. A note states what a "reviewed" mark means and that an encyclopaedia entry is a
    pointer to a record, not the source of a figure.
25. §U said every instrument is stdlib-only; the renderer needs matplotlib and python-docx and says so.

## Flags that are limits, stated rather than removed

- The load and DNI shapes are RECONSTRUCTED; `profiles.py` ingests measured series when reachable.
- The candidate comparison (§D) prices the alternatives at `firmpower.py`'s high band where the rest of
  the document says critical; the section says so.
- The study-cost and duration bands, the reservoir head, the days of holding, the hydro O&M share and
  the closing plant's O&M ratio are ASSUMED and marked.
- The head is one number (500 m) at both cases; the sensitivity runs 300–800 m and the modules go as
  one over head.
- "Plant records" appears in the source list because the study register cites it; the register marks
  what was reviewed and the sources note says what such entries carry. The Crescent Dunes row cited a
  Wikipedia project page until 2026-09-12, when the author asked for the plant's own record: it now
  cites the operator's Chapter 11 filing (In re Tonopah Solar Energy, LLC, No. 26-10060, Bankr. D. Del.,
  filed 2026-01-21), EIA Form 923 for plant 57275, the DOE Loan Programs Office and SolarPACES. The court
  record corrected the row: the four leaks are October 2016, March 2019, February 2022 and February 2023
  (the row had 2016, 2022, 2023); the offtake since late 2020 is short-term and month-to-month, not a
  night-only contract with NV Energy, whose 2009 PPA was terminated in October 2019; and the operator
  stayed ACS (Cobra Industrial Services, renamed ACS Industrial Activities), not Vinci.

## What did not change

The program's capital ($67 / $114 B), the register price ($126 / $205 per MWh), the studies line,
the schedule, the site rankings, the pilot pass mark and the flaws register. What moved is the
whole-load price and the household during and after the bonds (flag 1), and the environmental and
employment rows (flags 2–3); `CLAUDE.md`, `proposals/README.md` and the docs carrying the superseded
figures are updated in the same pass.
