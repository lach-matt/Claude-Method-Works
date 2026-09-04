# THE QUEUE — THE METHOD 1.7

*Rebuilt 2026-08-11. The 1.6.1 `QUEUE.md` went with that container's rollback;
its items below are reconstructed from the transcript. The previous 582-line file
is preserved as `QUEUE-LOG.md` — it had become append-only, holding fifty-nine
section headings across every prior session, and was a log rather than a queue.*

**STATE.** Registers 165–1460, 1,253 entries. **ν IS DEACTIVATED AS A LAW
(R 1460) and retained as a FORM; the corridor is the instrument and survives
intact. See NU-DEACTIVATED.md for what demotes and what does not.**

Registers 165–1460, 1,253 entries. ALL TWENTY-FIVE PASS. 5 of 5
round-trip. Every entry corrected by 1443, 1445, 1454 or 1457 now carries a
forward marker in register 1395's format — thirteen in all. See `PROVENANCE.md` for which files are original, recovered, rebuilt
or absent — several artefacts here are reconstructions and must not be read as
originals.

---

# 0-c · ONE TASK FROM THE REGISTER REVIEW (R 1567, CORRECTED R 1568)

The review's fourteen "promises" sorted to **six false positives, one
discharged, and six real** — and M's reading corrected the last step: **they
are working NOTES, not tasks.** The register records what was true when
written; the queue holds what someone undertook to do.

    ★★★ 1296  **THE ONLY TASK.** "MARKED FOR THE NEXT PASS." Names an action,
              a target artefact and a criterion for done.
              **THE BOOK AND ALL FIVE COMPENDIA NEED THE LÖWDIN WORK** —
              registers 1249–1295 recorded, none of it in any artefact.
              · Mathematical Compendium: the law index and the constant index
                as objects, with closures and attributions
              · Spectra Compendium: the Kr-core, Hg-core, La/Ce and Cd/In
                captures in the channel table
              **The largest owed item in the register.**

**NOT tasks — returned to the register as what they are:**

    730   a **standing RULE**: a precedent search is owed BEFORE any claim of
          novelty. Fires when a claim is made. Never done, never overdue.
    433   STATUS — a citation that entry lacked (Cowan & Andrew 1965)
    534   STATUS — why a capture stopped: "no levels URL surfaced"
    630   STATUS — the entry's point is the gap is DISCLOSED, not reconciled
    1475  STATUS — the space index is not yet built

*If 534 or 630 are ever wanted, R 1538's `spectrum` SINGULAR fix may reach
that endpoint now. But nobody undertook them, and they are not owed.*

⚠ **THE INSTRUMENT'S FAULT, WORTH KEEPING:** the pattern searched for the word
"owed", and in this register that word marks a **LIMIT** far more often than a
plan. It produced four false tasks AND three falsely-outstanding searches —
reading vocabulary instead of grammar.

---

# 0-b · THE CAPTURE RUN, 2026-08-11 — WHAT IT SETTLED (R 1524–1552)

**Fourteen files held, 4,682 rows.** The escalation that worked, in order of
success: **PDF by full title, uploaded as a file** > URL supplied by M >
URL I construct (cache-blocked) > container network (403).

    CLOSED
    B1   five L-shell lines, 400 rows. 5 forced orderings, 0 violations.
         2p spin-orbit measured two ways, median agreement 0.00 eV.
    B1b  ANSWERED — the σ-offset is NOT a count. Slope −0.1129, r = −0.858.
    D2   495 rows, Z 19–36, every stage. **Only 19.4% is measured.**
    D4   3,558 rows. **E.nuclide = 2, NOT 9** — but stable, nameable, and the
         defect cell IS the diproton. Three of four claims reproduce.

    PARTIALLY
    D3   the PRA companion held (42 rows). Its K I experimental column matches
         my Rydberg–Ritz extrapolation in all three channels to ±0.0013 —
         including the d channel the authors call their largest ever
         theory–experiment discrepancy.

    NEW, from the overlap (R 1552)
         ground-state minus asymptotic defect falls toward zero as z rises,
         slope −0.0037, r = −0.846 on five ℓ = 0 species.

## STILL NEEDED

    D3 tables    ADNDT 35, 473 — "Quantum Defect Values for Positive Atomic
                 Ions". **Try the PDF by full title.** ~5,100 values.
    Kr I 1s3     the J = 0 metastable near 85191 cm⁻¹, absent from both listings
    B1 analysis  NOT a fetch — the Moseley fit failed with 4 of 7 screenings
                 pinned at the grid edge. Needs Z-DEPENDENT screening.

---

# 0-a · WHAT IS UNREACHABLE FROM HERE (R 1533)

Four external sources attempted 2026-08-11; **none returned data**, by four
distinct mechanisms. Recorded so nobody retries them blind.

    AME2020 (both files)   402 at www-nds.iaea.org — PROXY BLOCK, not a paywall.
                           Both files fail identically → the HOST is refused.
                           **✔ D4's ROUTE IS OPEN (R 1548).** Argonne serves the file:
                           www.anl.gov/sites/www/files/2021-05/mass_1.mas20.txt
                           (search first, fetch the reference page, then its
                           download link). IAEA is proxy-blocked and IMP CAS is
                           robots-disallowed; **Argonne works.**
                           ⚠ The '#' marking an ESTIMATE sits IN PLACE OF THE
                           DECIMAL POINT. Stripping it corrupts every
                           extrapolated value. Use the header's own format line,
                           not any supplied spec — both were wrong.
                           **CAPTURE IS BLOCKED BY TRANSPORT (R 1549), not by
                           permission.** Container network is 403; web_fetch reads
                           into context only. 3,500 rows retyped would carry ~170
                           faults at this session's observed transcription rate.
                           **NEEDED: the file in /mnt/user-data/uploads, or
                           container network.** Exact addresses, both verified:
                             mass_1    /sites/www/files/2021-05/mass_1.mas20.txt
                             massround /sites/www/files/2021-03/massround.mas20.txt
                           ⚠ DIFFERENT date directories — take each from its own
                           page at /phy/reference/ame-2020-<name>.
                           **D4 stays open.** *Wording corrected (R 1542): E.nuclide = 9 is a
                           RESULT — the (Z,N) chart's closure defect, nine cells
                           named as the mass formula's pairing and clustering
                           terms. It is not an error. What cannot be done is
                           RE-RUNNING the measurement, because the input file is
                           not held.*
                           **UNTRIED ROUTES:** amdc.impcas.ac.cn mirror; Argonne
                           mirror; and Chin. Phys. C 45 030001/030002/030003
                           (2021), open access, tables in full.
                           ⚠ *Any supplied column spec or header count is a
                           HYPOTHESIS to test against the file, never a spec to
                           build a parser from.*
    ASD energy1.pl         **SCHEMA FAULT NAMED (R 1538): it wants `spectrum`
                           SINGULAR — one species per query, e.g. spectrum=K+I —
                           where ie.pl takes `spectra` with a RANGE.** I sent the
                           plural to the singular endpoint. It reported no name
                           because the parameter's NAME was wrong, not its value.
                           **D3-by-levels IS reachable, one spectrum at a time.**
                           URL form:
                           physics.nist.gov/cgi-bin/ASD/energy1.pl?spectrum=K+I&units=1&format=2&submit=Retrieve+Data
    Theodosiou 1986        **IDENTIFIED (R 1543).** "Quantum Defect Values for
                           Positive Atomic Ions", Theodosiou, Inokuti & Manson,
                           ADNDT 35(3) 473–486, **PII 0092-640X(86)90018-5**,
                           DOI 10.1016/0092-640X(86)90018-5.
                           *My earlier PII ...900158 was a TRANSPOSITION of
                           ...900185 and hit Ivanova at pp. 419–428 — a typo that
                           returns a plausible wrong paper rather than a 404.*
                           R 1217's description confirmed element by element.
                           Three of its physical claims verify against held data,
                           incl. the 3d collapse at Z = 19–21 corroborating
                           R 1392's Z = 21 threshold from an independent route.
                           **Still paywalled — the TABLES are not held.**


    Ivanova et al. 1986    NEW SOURCE, recorded rather than lost. Mg-like ions
                           along an ISOELECTRONIC sequence Z = 25–84 — one of the
                           compendium's own three axes. Paywalled. Second lever.
    arXiv 1110.6134        Abstract only. Confirms a κ/μ table EXISTS; cannot
                           confirm R 1462's per-(N,ℓ) figures. **UNVERIFIED.**

*Three of the four cannot be fixed by changing the query.*

---

# 0 · THE JOINED OBJECT — ONE THING, THREE FACES (R 1523)

**Löwdin, the three-body problem and M.C2 are one queue item.** They are the
same measure returning three values, and the measure is the CONFLICT GRAPH
(R 1521): vertices are constraints, an edge means two cannot hold together, and
**the verdict is the max clique.**

    object      vertices  edges  MAX CLIQUE   verdict
    Λ                  8      0           1   CLOSED — the tree property (R 507, 1519)
    M.C2               4      0           1   CONDITIONAL — nothing conflicts
    nuclear            6      9           2   REFUTED — K(3,3), certificate is an edge
    Löwdin           106    735           3   needs THREE parameters, not one

**One instrument, three languages** (R 1518): geometry — Helly, Radon,
Carathéodory, Gallai duality; logic — Freuder's k-consistency; statistics — the
centerpoint theorem and fractional Helly. Provably the same theorem. **The
language you need is the one whose face is NOT degenerate for your object** —
Löwdin's geometry is non-degenerate, the nuclear case's is rank-one so its
content moves to statistics.

**The boundary of the method, stated (R 1519):** ℛ is complete on trees and
incomplete on anything carrying a cycle. Λ sits one edge from that boundary in
exactly seven places.

**What remains on each face:**

    M.C2      CONDITIONAL — proved in 9 Killing-free steps on one hypothesis:
              does an NEH admit an ANE-vacuum cyclic and separating for the
              exterior algebra? DMP supply 3 of 4 conditions; the last join is
              the classical-to-quantum passage (direct integral → continuous
              tensor product), R 1511.
    Löwdin    REFUTED at one parameter; minimum THREE, forced by B 5, La 57,
              Lr 103. The challenge as posed is NOT answered — Belokolos is
              87/106 and Scerri's consensus stands (R 1450). Approach is
              REVERSE ENGINEERING: solve the surroundings, identify, then trace
              back to the derivation.
    3-body    the nuclear instance is refuted; the general problem untouched.
              Two-state structure (R 1520): known vs unknown masses differ by
              exactly N − 1 Helly orders; certificates transfer UPWARD only;
              the envelope IS the feasible set, dimension N − 1.

---

# I · CLOSED IN 1.6.1, CARRIED HERE

    ✔ A2   Λ_spectra closes at the limit — E = 11, all named (three children below)
    ✔ A4   the update rule, derived
    ✔ A5   Λ_traj resolved as a PROJECTION of Λ, not a new index
    ✔ B0   Janet's E = 0 relabelled FORCED, not earned
    ✔ B0a  the index is 120, the table 118 — written into section III
    ✔ B0b  the limit recount: 38 / 20, not 47 / 11
    ✔ B2   Λ_ladder closes — fourteen ladders, nine cells, E = 0
    ✔ B2a  the five shared cells: four findings and one separation
    ✔ C2   the six-pair screen, all three candidates eliminated
    ✔ C3   the falsifier survived, by one shell
    ✔ C4   the swaps — feasible set empty under all four orderings
    ✔ F2b  all five generators diff-tested
    ✔ F2c  the timing line fixed at source, normalisation retired
    ✔ C    topic C complete

---

# II · THE REBUILD — twelve scripts lost, four rebuilt

    ✔ contingency.py    R 1383 — both worked examples report FORCED
    ✔ roundtrip.py      R 1389, 1433 — the second gate, 5 of 5
    ✔ sixpair_screen.py R 1371, 1372, 1394 — supersedes corridor_identity.py
    ✔ traj_index.py     R 1417–1420 — REBUILT, see the discrepancy at IV·6

    ✔ scorer.py        R 1413, 1438 — BUILT. Reproduces 99 of 106 and the
       lower-n tie-break's 91 exactly; six of the seven misses match, with a
       swap at the ends (this rebuild misses B 5 and gets Rf 104). Two figures
       do NOT reproduce: fifteen moves against the register's ten, and per-block
       ascent at 94 under 1409's literal reading. **And the 99 was FITTED — held
       out the score is 90, below Madelung's 96 (R 1445).**

    ★★ xray_index.py    R 1378, 1379 — BLOCKED on the candidate list.
       Known: the raw six are source n, source ℓ, target n, target ℓ, hole
       j-type, transferred count, giving E = 22. Eleven candidates were formed
       by differences and endpoints; 72 of C(11,3) = 165 close, all at nine
       cells. The intermediate list is NOT recoverable. Rebuild from Λ's own
       alphabet and see whether 165 falls out — if it does not, the candidate
       set differed and the 72 does not transfer.

    ✔ a5c.py           R 1420 — BUILT, and it closes queue item A5c. The
       twelve/ninety-four split reproduced; six of thirty-five three-axis systems
       close, one target-only (ℓ·p·q at 24 cells in 56, R 1418's system a third
       time) and five carrying a source coordinate. **The permutation explosion
       that killed 1.6.1 twice is solved by searching DIRECTION FLIPS only —
       every axis is a monotone chain, so its order is given and only its
       direction is free: 2³ orderings, not a product of factorials.**

    ★ merged_triples.py R 1420 — still worth building separately: source ℓ coded
       0 for the notional outside and ℓ+1 otherwise; source occupancy BEFORE the
       step; source block distance = source(n+ℓ) − target(n+ℓ) + 2.

    ✔ rival_pull.py     R 1406 — BUILT. Reproduces the 4d row exactly: the
       ceiling contracts 0.505 at Mo and 0.748 at Rh and RISES 0.059 at Pd,
       all three to three decimals. The pull is 1/cap and 1/gap².
    ✔ block_ascent.py   R 1409 — BUILT. Fifteen moves = seven placements +
       eight rises, six of them RE-placements (R 1411), and ALL EIGHT recorded
       a values reproduced. Highest floor 1.9841 over tightest ceiling 0.7071
       = 2.806, so no single a serves the walk.
       **AND IT SETTLES THE 'ZERO VIOLATIONS' QUESTION: a floors-only ascent
       stands at or above the ceiling on 44 of 106 steps, so the phrase means
       MONOTONICITY — a never descends within a block — and NOT corridor
       membership. The four descents are all block openings.**
    ✔ merged_triples.py R 1420 — BUILT with the recovered source coordinates.
       Landing systems containing q put their defect at q ∈ {1, 2} rather than
       at q = 2 alone, and THREE of forty-six systems with a source coordinate
       close, against 1420's twelve of twenty. **The twenty is NOT
       reconstructible** — five landing axes and three source coordinates give
       46 such systems and no grouping yields twenty — so the counts differ by
       candidate set, not by result. Flagged, not reconciled.
    ✔ hydrogenic_test.py R 1382 — BUILT, PARTIAL. The structural zero is
       verified with no data. The two reduced-mass points reproduce exactly:
       H −0.000267 against −0.000272, He −0.000046 against −0.000069. Lithium
       already departs, which is relativity entering.
       **BLOCKED beyond that: the climb to +0.103 at Z = 110, the (Zα)² + (Zα)⁴
       fit and the 7.04% Dirac deficit all need H-like ionisation energies to
       Z = 110, and this tree holds THREE.**
    ✔ merged_index.py   R 1418, 1419 — done inside `figures_walk.py`

*List given from memory at the far end and NOT verified against a directory
listing. Probably complete, not certainly.*

**AND THE LIST IS NO LONGER THE RIGHT FRAME.** Four of the twelve are rebuilt,
but SEVENTEEN other scripts were written in 1.7 — `scorer.py`, `balance.py`,
`a5c.py`, `per_run.py`, `per_atom.py`, `transition.py`, `group_rule.py`,
`proximity.py`, `a_inward.py`, `belokolos_spectrum.py`, `null_madelung.py`,
`delta_grouping.py`, `figures_xray.py`, `figures_walk.py` and the three `bridge_*`
tools. Two of the eight outstanding are now redundant: `corridor_identity.py` is
superseded by `sixpair_screen.py`, and `merged_index.py` is done inside
`figures_walk.py`. What is genuinely still missing is `xray_index.py`, blocked on the eleven
candidate coordinates, and `isotopic_null.py`, blocked on atomic masses — the
mass shift R_M = R∞/(1 + mₑ/M) needs M per element and AME2020 is cited in five
places and held nowhere (D4). See PROVENANCE.md for what each script is and is not.

---

# III · OPEN FROM 1.6.1

**✔ A1 · WHAT IT IS FOR, SETTLED (R 1563).** Four anchors held (R 1557),
two unmeasurable (R 1556), and the magnitude test is CIRCULAR (R 1562).

    ✔ **THE SIGN** — lighter lies higher. Holds on 5 of 6 elements.
      Needs NO radius; an assumption cannot flip a sign. R 1381 stands.
    ✔ **THE FACTOR F = 4.13 ± 0.51 eV/fm²** for KL3 across Z = 92–96,
      from the four anchors whose δ⟨r²⟩ are independent of the X-ray column.
      A measured quantity, from material already held.
    ★ **NEW USE — A1 AS A DETECTOR.** Cf-249 and Cf-250 carry the IDENTICAL
      theory value 115031.1 eV, where one neutron should give ~0.5 eV against
      0.1 eV precision. **Where the theory column stops varying with A, it is
      announcing it has no radius to vary.** Run this across the whole X-ray
      capture, not just the actinides — it finds cells with missing inputs.
    ✗ **NOT a magnitude test.** Theory column circular; experimental column
      has 0.2–15 eV errors against 0.6–2.2 eV shifts.
`captures/RADII-actinide.tsv`, 23 rows from Angeli & Marinova Table 1.

    U  233→238  δ⟨r²⟩ = +0.4350 fm²   Kα X-ray IS
    Pu 239→244            +0.4260     OIS 420.64 nm, Pu I
    Am 241→243            +0.1420     λ [Ba98], HM-corrected
    Cm 245→248            +0.2490     λ [Au87], HM-corrected

    ✔ **R 1555's prediction held ROW BY ROW** — 4 present, 2 absent, from
      the abstract alone before the table was in hand.
    ✔ The paper CORRECTS uranium's mass interval to **233–238 instead of
      235–238**, in the Kα X-ray section — A1's own anchor and observable.
    ⚠ **Curium has NO experimental R.** Its δ⟨r²⟩ is measured; its absolute
      radius is calculated from a 3-parameter fit. Usable for field shift,
      not for anything resting on the absolute radius.
    ⚠ Four different measurement routes. Agreement across them would MEAN
      something; pooling their uncertainties would not. The δ⟨r²⟩ errors
      are STATISTICAL ONLY.

*Superseded framing below, kept for the trail:*

**★★ A1 · the field shift. LITERATURE NAMED (R 1555), AND IT COVERS ONLY 4 OF 6.**

    (a) **Angeli & Marinova, ADNDT 99 (2013) 69–95**, "Table of experimental
        nuclear ground state charge radii: An update". 909 isotopes, 92
        elements, **¹H to ⁹⁶Cm**. Covers U, Pu, Am, Cm.
    (b) **Bk (97) and Cf (98) are OUTSIDE it** — and Cf is the anchor with
        THREE mass numbers (R 1381). Candidates: Fricke, Heilig et al.,
        1995 and 2004.

    ✔ **SETTLED (R 1556). A1 IS BOUNDED BY MEASUREMENT, NOT ACCESS.**
    Fricke & Heilig, *Nuclear Charge Radii*, Landolt-Börnstein I/20 (2004),
    on Fricke et al. ADNDT 60, 177–285 (1995) — **"all INVESTIGATED isotopes
    of the elements (Z = 0 up to Z = 96)".** The SAME ceiling as Angeli &
    Marinova, from a different group with a different method. And a 2026 Bk
    charge-radius paper is purely THEORETICAL, stating the investigation is
    "still lacking".

    **Two independent evaluations stopping at identical Z is the limit of
    what has been measured. Bk and Cf charge radii do not exist.**

    → **A1 is a DOMAIN STATEMENT, like E2 — not an unfinished item.**
      The field shift is testable on U, Pu, Am, Cm at two masses each.
      The cost is asymmetric: **Cf carried THREE masses** (R 1381), the
      richest anchor, and it is one of the two that cannot be had.

    ✔ **Ohayon CHECKED (R 1558).** Z = 3–32 only — prediction held. But he
      states Angeli & Marinova give **no V₂(Z) uncertainty**, that σ_CD is
      **up to 4× the quoted totals**, and that **larger missing uncertainties
      are expected for heavier nuclei** — i.e. these actinides. Treat the
      unc_R column as a LOWER BOUND.

    ★ **WHY Z ≥ 97 IS BLOCKED (R 1559) — and it is a CALIBRATION failure.**
      3 of the 4 methods need TENS OF MILLIGRAMS; only OIS works on traces,
      and OIS gives DIFFERENCES ONLY. Eq (1) needs an absolute anchor R(A′),
      and Bk/Cf have no isotope with a measured absolute radius.

          Z ≤ 95   both measured        (Am is the last)
          Z = 96   δ⟨r²⟩ only; R CALCULATED
          Z ≥ 97   neither

      20 mg of ²⁴⁹Cf = 3.0 GBq; of ²⁴⁹Bk = 1,176 GBq; the ²³⁸U anchor = 250 Bq.

    ★★ **THE ROUTE THAT COULD MOVE THE WALL:** Heines et al., "Muonic x-ray
      spectroscopy on implanted targets", NIM B **541** (2023) 173 —
      **microgram-scale targets**, a 20,000× reduction. If it works, A1's two
      missing anchors become obtainable. **Worth watching.**

Blocked on δ⟨r²⟩, held nowhere and not in the X-ray
data. Six isotope anchors sit in `XRAY-KL3.tsv` — U, Pu, Cm, Am, Bk, Cf, each at
two mass numbers, **and Cf at three** (R 1381 corrected).

**✔ A5b · CLOSED (R 1457, 1458).** δ = a√p is not merely refuted but IMPOSSIBLE
— δ is bounded as n → ∞ and a√p diverges; the held series are flat to five
percent where √p demands a factor of six; and the Tietz potential has no Coulomb
tail, so no defect can be derived from it even in principle. **There is no route
from the walk to δ**, and ν is an ordering functional rather than an effective
quantum number. The completion criterion and the law are different objects —
see NU-AND-DELTA.md for the three ways out, and R 1341's own claim (they share an
index, not a value) for why this closes rather than blocks.

**✔ A5c · CLOSED.** `a5c.py` runs. Twelve of 106 steps have a real source — Cr,
Cu, Nb, Ru, Pd, Pr, Tb, Pt, Pa, Pu, Bk, Rf — and 94 come from the notional
outside. Six of thirty-five three-axis systems close. The permutation explosion
is solved by direction-flip search rather than by a smaller cap.

*The diagnosis, which any new session needs before touching it.* The boxes are
tiny — at most 336 — so the memory is NOT going into the closure computation.
It goes into the permutation loop: an axis with fourteen rungs makes the product
of permutations astronomically large, and `itertools.product` builds its
arguments eagerly. **Cap the permutation count before constructing the product,
never inside the loop.** `traj_index.py` already does this, capping the iterator
at 200,000 orderings and declaring when the cap bites; reuse that.

**✔ A4b · CLOSED (R 1470).** The four are not one class. **Li 3 is the origin**
(corridor (0, ∞), the law determines nothing). **K 19 is where the floor stops
being degenerate** — the first non-zero floor in the walk — so R 1403's rule
switches from ceiling to floor and a moves DOWN. **Tl 81 and Fr 87 are the floor
rising above the held a**, which the intersection-emptying test cannot see.
So the reset condition is THREE tests, not one, and all eighteen are accounted
for bar one false positive at In 49 — where the record holds no measured a and
the disagreement may be the record's.

**✔✔ B1 · the L-shell lines — CAPTURE COMPLETE (R 1527).** All five held:
`XRAY-L3M1` (Ll, 88), `XRAY-L3M4` (Lα2, 78), `XRAY-L3M5` (Lα1, 78),
`XRAY-L2M1` (Lη, 88), `XRAY-L2M4` (Lβ1, 78) — in `captures/`.

    · five forced orderings, 0 violations across 74–88 elements each
    · the 2p spin-orbit splitting measured TWO independent ways (via M1 and
      via M4) agrees to a MEDIAN 0.00 eV, max 0.100 eV, on a quantity
      reaching 5,773.60 eV — 39 of 77 exact
    · every URL supplied by M; every destination_url read back before writing

**ANALYSIS NOW UNBLOCKED:** do the nine transition types hold at a second depth?


**✔ B1b · IS THE σ-OFFSET A COUNT? — ANSWERED, NO (R 1528).** Prediction
declared with three outcomes BEFORE the fetch; the test could fail and did,
against the branch I favoured. `XRAY-L1N2` (Lγ2, 67) and `XRAY-L1N3` (Lγ3, 65)
held. On the 45 UNBLENDED elements above Z = 55 the 4p offset **falls
monotonically**: slope −0.1129 per Z, r = −0.858, mean 14.420, sd 1.620.
**A count cannot drift; this drifts 5.1 units.** It is a screening that weakens
as the nucleus dominates — R 1390's reading, reached independently at 4p.

    ⚠ **USE THE BLEND FLAG.** Rb–Xe are marked L1N2,3: the lines are NOT
      resolved and their difference is not a splitting. Ignoring it produced
      sd 5.259 and a split verdict.

**✔✔ D2 · THE IONISATION LADDERS — K–Kr CAPTURED (R 1530).**
`captures/LADDER-K-Kr.tsv`, 495 rows, Z = 19–36, every stage of the 3d block.
Structural verification: 18 elements, exactly Z stages each, charges 0..Z−1,
strictly increasing, **zero failures**; seven first-IEs spot-checked against
known values.

    ⚠ **THE QUALITY FLAG IS KEPT AND MATTERS:** 96 measured, 287 estimated,
      112 theoretical — **only 19.4% is measurement.** Any fit that pools
      these without the flag is fitting mostly to interpolation.

    Held alongside: `LADDER-H-Ar-I-III.tsv` (51 rows). Ladder coverage is now
    H–Kr rather than 15 of 108.

**★★ D3 · Theodosiou, Inokuti & Manson 1986** — ~5,100 Hartree–Slater defects,
all ionisation stages to Z = 50. **The largest single lever in the queue.**

**★ D4 · AME2020** cited in `mathreg.py`, `indices.py`, LITERATURE, COMPENDIUM
and INDICES; held nowhere. **E.nuclide = 9 cannot be reproduced.** REPRODUCTION
checks that a build runs, not that its inputs are present — a check passing over
an absence, the same shape as the lost tails.

**★ E2a · the Dirac coefficient.** A = 0.1162 against 1/8, **7.04% low**
(recomputed), unexplained.

    **RESHAPED, NOT CLOSED (R 1553).** The L-shell captures give a SECOND
    Dirac coefficient on 77 elements — the 2p spin-orbit splitting,
    hydrogenically (Zα)⁴mc²/32. Fixing it at Dirac and fitting σ alone:
    **σ = 0.98 ± 2.43, drifting at slope −0.178, r = −0.978 above Z = 55.**

        3p offset (R 1391)   one value per Janet region, not universal
        4p offset (R 1528)   falls monotonically, r = −0.858
        2p splitting (NEW)   falls monotonically, r = −0.978

    **THREE SHELLS, ONE BEHAVIOUR** — screening weakening as the nucleus
    dominates, on three independent line pairs. E2a's 7% is NOT explained by
    this (different observable, wrong size and sign), but it is no longer a
    LONE unmatched coefficient.
    ⚠ Fitting C and σ jointly is DEGENERATE — it returns a ridge. Fix C.

**★ E2 · the relativistic wall** on three independent objects — a domain
statement, not a failure.

**★ G2 · Q.exch withdrawn**, fitted sign opposite the measured one, needs an
ℓ-dependent exchange term. Six of Λ_spectra's eleven remaining cells.

**★★ G1 · M.C2 — ONE EXISTENCE QUESTION (R 1506).**

> **Does a non-expanding horizon admit a state annihilated by all smeared ANE
> operators and cyclic and separating for the exterior algebra?**

Of the four Borchers conditions, **the Killing field is load-bearing in exactly
one place — the existence of this state.** Positivity comes from the ANEC on
ACHRONAL generators (R 1471); the inclusion is CAUSAL structure, not isometry;
and the geometric flow is DERIVED from the conditions by Borchers–Wiesbrock, not
required as input (R 1497). Standardness for the subalgebra follows from the
large algebra (R 1501).

**★★★ THE WITNESS PROGRAMME IS FOUND (R 1508).** Dappiaggi, Moretti & Pinamonti,
*Hadamard States from Light-like Hypersurfaces*, SpringerBriefs Math. Phys. 25
(2017), with CMP 2009, JMP 2009, ATMP 2011. Their **bulk-to-boundary
correspondence identifies a DISTINGUISHED STATE on the conformal null boundary**
whose bulk counterpart is automatically Hadamard — for spacetimes explicitly
"not necessarily homogeneous or isotropous". And the **asymptotic (conformal)
Killing horizon** generalisation covers null hypersurfaces tangent to a vector
field satisfying the Killing equation only IN A LIMITING SENSE, theory-agnostic,
no Einstein equations used.

    ✔ **CHECK 1 ANSWERED (R 1509) — AND BY A UNIQUENESS THEOREM.**
       Moretti, CMP 268 (2006) 727: the DMP state has a POSITIVE self-adjoint
       generator of u-translations **in every Bondi frame**, and there is a
       **UNIQUE** pure quasifree state invariant under u-displacements with
       positive generator. DMP, JMP 50 (2009) 062304 covers spacetimes "not
       necessarily homogeneous or isotropous", with invariance under isometries
       **"(if any)"** — their parenthesis, covering the case of none.

           condition (i)  P ≥ 0            SUPPLIED, every frame
           condition (ii) the inclusion    already held, causal (R 1506)
           condition (iii) PΩ = 0          SUPPLIED, and UNIQUE
           condition (iv) standardness     ** THE REMAINING GAP **

    ✔ **CHECK 2 HAS A ROUTE (R 1510).** Guido–Longo–Wiesbrock give a
       **BIJECTION** between standard half-sided modular inclusions and strongly
       additive conformal nets on the circle; for such a net the vacuum is
       **cyclic and separating by Reeh–Schlieder**. And a null hypersurface is
       ULTRALOCAL — one CFT per null ray — so the cut algebra is the product of
       chiral half-line algebras over the cut.

    ★★★ **THE ONE REMAINING JOIN, LOCATED PRECISELY (R 1511).**

       **THE CUT** = a cross-section of H ≅ S × ℝ; one copy of S at fixed affine
       parameter; S ≅ S² in d = 4, compact and 2-dimensional. The product is
       indexed by y ∈ S, one per generator, measure √q d²y. *(Distinct from "the
       cut u", meaning WHICH cross-section — M.C2's u₁ < u₂.)*

       **CLASSICALLY IT IS A DIRECT INTEGRAL AND THAT IS EXACT.** M.C1, verified:
       the presymplectic potential carries no transverse derivative, so the
       symplectic form is BLOCK DIAGONAL in y with δ^(d−2)(y − y′). Cyclicity
       passes through a direct integral given a measurable field of cyclic
       vectors.

       **QUANTUM MECHANICALLY IT IS NOT.** The Fock space over a direct integral
       of symplectic spaces is a CONTINUOUS TENSOR PRODUCT of Fock spaces — an
       Araki–Woods/ITPFI object, type III — where cyclicity does not pass
       automatically.

       **✔ AND THE PASSAGE IS NOT AN OBSTRUCTION (R 1512).** Sampled across six
       groups. The RINDLER WEDGE has a non-compact transverse cut ℝ^(d−2), its
       horizon algebra IS the continuous product of chiral half-line algebras,
       and Reeh–Schlieder is a THEOREM there (Bisognano–Wichmann). **Cyclicity
       survives the continuous product.** Kay–Wald (bifurcate Killing horizon),
       Moretti (null infinity) and Bunch–Davies (de Sitter) agree.

    ★★★ **THE CONFOUND, AND THE ONE ROW LEFT.** In four of five known groups a
       Killing or asymptotic Killing field is present and supplies the state, so
       the sample does not separate the product step from the Killing step.
       **The row that breaks it is DMP's expanding-universe case** — "not
       necessarily homogeneous or isotropous", isometries "if any".

           TWO THINGS TO VERIFY ON THAT ROW, AND THEN THE CHAIN IS COMPLETE:
           1. does their construction genuinely run with NO isometry at all?
           2. is their past cosmological horizon NON-EXPANDING in Ashtekar's
              sense — Θ = 0, σ = 0, H ≅ S × ℝ?

    *Two inferences NOT established, flagged so they are not leaned on: that
    "generator of u-translations" IS the smeared ANE operator (likely for a free
    field, but the general smearing is a SUPERTRANSLATION); and that their
    boundary setting transfers to a finite-distance non-expanding horizon.*

*Note for the record: M.C2's check has cited Dappiaggi–Moretti–Pinamonti since it
was written — filed as evidence that positivity is "assumed by everyone who needs
it". The reframing did not find a new source; it re-read one already held.*

    TWO ROUTES, BOTH NAMED:
    · annihilation — a simultaneous ground state problem, since ANE operators
      on different generators commute
    · standardness — SVW's analytic microlocal spectrum condition on
      real-analytic spacetimes, or Sanders's deformation argument

**And the corner freedom is NOT an obstruction (R 1505):** b(y) drops out of P_λ
by translation invariance, and a(y) acts transitively on positive smearings, so
choosing the boost IS choosing the observable. One parameter, and it is a label.

*Prior framing, kept for the trail:*

**★★ G1 · M.C2 — TWO QUESTIONS (R 1496).**

    (A) **IS THE ANE-VACUUM CYCLIC FOR THE HORIZON-CUT ALGEBRA?** The fourth
        Borchers condition, bundled into the sources' third and then ASSUMED.
        **The ANE vacuum is the state with ZERO NET ENERGY FLUX ACROSS EVERY
        GENERATOR** — P_λ|Ω⟩ = 0 for all λ ≥ 0 — and NOT the theory's vacuum.
        Δ and J come from (algebra, Ω), so M.C2 is a property of the horizon
        TOGETHER WITH THIS STATE, not of the horizon alone.

        **✔ LARGELY DISSOLVED (R 1500, 1501).** The degeneracy is real and
        harmless — every vacuum gives the SAME horizon modular Hamiltonian, by a
        Connes cocycle argument. And the fourth condition is DERIVABLE from the
        source's own three facts: P_λ|Ω⟩ = 0 gives U|Ω⟩ = |Ω⟩; Ω is cyclic for
        the LARGE algebra B by their condition (iii); and C_λ = U_λ(1) B U_λ(1)†
        by their own equation. Then **C_λ Ω = U B Ω is dense because U is
        unitary** — so Ω is cyclic for C_λ, and separating follows from C_λ ⊆ B.

        **✔ AND THE SOURCE'S ABSTRACT CONFIRMS IT (R 1502):** "in both free and
        interacting quantum field theories, such states are GUARANTEED TO EXIST
        by the properties of half-sided translations on the horizon." Guaranteed,
        not assumed. The register's reading of "assuming Ω is cyclic" as an open
        hypothesis was wrong.

        **★★★ WHAT ACTUALLY REMAINS — THE SOURCE'S DOMAIN, NOT A MISSING
        HYPOTHESIS.** The abstract's first line: "for arbitrary cuts of KILLING
        HORIZONS." Arbitrary CUTS, not arbitrary horizons. Everything derived is
        established ON A KILLING HORIZON, and **M.C2's hypothesis drops exactly
        that.** So (A) is answered where a Killing field exists and open
        precisely where M.C2 needs it.

        Routes, if the non-Killing case is to be attacked directly: SVW's
        analytic microlocal spectrum condition, or Sanders's deformation
        argument from a spacetime carrying a Reeh–Schlieder state.

        *Superseded reading, kept for the trail:*
        "when the algebra B∞ is nontrivial, the vacuum |Ω⟩ is NO LONGER UNIQUE;
        any other state b|Ω⟩ with b ∈ B∞ is also a vacuum, since [P_λ, b] = 0."
        **So wherever an algebra at infinity exists, the ANE vacuum is
        DEGENERATE** — and a degenerate ground state is exactly where cyclicity
        for a subalgebra can fail, the Hilbert space splitting into sectors the
        cut algebra cannot move between. **Test this before anything else.**

    ✔ (B) **SETTLED (R 1498), AND THE EXPECTED ANSWER REVERSES.** The NEH
        conditions confine the corner map's image to a 2-dimensional coadjoint
        orbit — but a map between two 2-manifolds is Whitney generic, with fold
        lines, cusp points and a TRIVIAL stabiliser in Diff(S). **So Mackey's
        second step is empty and the d = 4 block dissolves for a generic
        horizon.** Kerr's rotational Killing field forces U(1)-invariance and a
        continuous stabiliser, so the answer is NO for Kerr and YES for an NEH
        without a continuous spatial symmetry. *Target-space restriction is not
        map non-genericity — that was the error in the first answer.*

    Independent of each other, and neither is about modular theory or horizons.

*Prior state, kept for the trail:*

**★★ G1 · M.C2 — SHARPENED (R 1471).** The positivity obstruction
has a route the check never examined: **the ANEC**, via Faulkner & Speranza
(arXiv 2405.00847), plus **quasi-Killing vectors** (Killing only on H, defined
globally there rather than to first order at a cut). But the achronal ANEC is a
CONJECTURE, proved only for a free scalar at small curvature (Kontou & Olum
2015) or FROM the GSL for null lines (Wall 2010). Three things to check, in
order:

**THE NULL IS NOW COMPUTED (R 1472–1473).** The ANEC's QEI bound B — the null —
is **−∞** for null-geodesic smearing in 4D (Fewster & Roman 2003, explicit
construction on Hadamard states). Finite in 2D. So positivity of P_λ cannot be
bought locally, and every proof's price is visible: **Wall spends COMPLETENESS,
Kontou–Olum spend TIMELIKE SMEARING, SNEC spends a UV CUTOFF, the 2026 QNEIs
spend the QNEC.** And Buchholz's reason for the failure — no nontrivial
observables localized on a null surface for n > 2 — is the SAME fact that makes
the horizon algebra trivial.

**★★ THE QUESTION IS NOW ONE OF DIFFERENTIAL GEOMETRY (R 1474):**

> **IS A GENERATOR OF A NON-EXPANDING HORIZON AFFINELY COMPLETE?**

Ashtekar's three conditions fix the expansion, the topology (H ≅ S × ℝ) and the
state. They say nothing about affine completeness — and topological completeness
is not affine completeness. If the generators are affinely complete, Wall's route
supplies positivity and M.C2 may close. If they are not, only a regulated route
(SNEC, ℓ_UV) remains, and M.C2 closes with a cutoff or not at all.

    ✔ **the circularity — CLEARED (R 1479).** Wall's GSL proof (1105.3445)
      hypothesises an ALGEBRA OF OBSERVABLES ON THE HORIZON with four axioms —
      Determinism, Ultralocality, Local Lorentz Invariance, Stability. The ANEC
      is not among them and neither is HSMI, so no loop closes. **But he verifies
      those axioms only for FREE FIELDS and 1+1 CFTs**, and Buchholz's fact
      (R 1472) is that no nontrivial observables are localized on a null surface
      for n > 2. **The route is unavailable in exactly M.C2's regime — 4D,
      interacting — and available where the register's own 1018 already
      succeeded.** Same fact as the missing null QEI and the trivial horizon
      algebra: one obstruction, three costumes, 1+1 the exception in all three.

    ✔ **THE SUM IS COMPLETED (R 1484) AND THE SUDOKU READING REFUTED (R 1485).**
      The ledger counts a MANIFOLD and M.C2 needs an ALGEBRA; the corner content
      is two FUNCTIONS on the cut, a(y) and b(y), not commensurable with
      dimensions, so no arithmetic sum holds them. And the four constraints the
      register holds do not relate a(y) to a(y′) at all — the system decouples
      into a product of open half-lines, so it is not a sudoku and needs no
      search.

    ★★★ **THE ITEM THAT REPLACES THEM: WHAT COUPLES a(y) TO a(y′)?**
      Non-expansion fails to relate the boost at one point of the cut to the
      boost at another. That is R 1020 read across the whole cut, and it is the
      real shape of M.C2's openness.

      **ALL THREE CANDIDATES TESTED AND ALL THREE FAIL (R 1486):**
        ✗ the corner doubling — relates corner to corner at the SAME y, so it
          doubles the unknowns rather than coupling points
        ✗ the crossed product — the group is SUPERTRANSLATIONS and ARBITRARY
          DIFFEOMORPHISMS, infinite-dimensional and function-valued, forcing
          nothing pointwise
        ✗ the global condition — completeness is INVARIANT under u → u/a(y)+b(y),
          the same shape as R 1020's Θ = 0 result

      **What survives is ONE weak coupling, reached twice: the group is
      DIFFEOMORPHISMS, so a(y) is SMOOTH across the cut.** Plus a matching
      condition nobody predicted — the diffeomorphisms of the two null
      boundaries must COINCIDE AT THE CORNER.

      So the underdetermination is by a SMOOTH function's worth rather than a
      function's worth.

**★★★ AND THE FOURTH CANDIDATE IS FOUND (R 1487): diff(S).** The extended corner
symmetry algebra is (diff(S) ⊕ sl(2,ℝ)^S) ⊕ (ℝ²)^S, and exactly ONE of its three
factors is non-ultralocal — the surface diffeomorphisms. **Chandrasekaran and
Flanagan's corner modes are the other two**, both ultralocal, so the coupling
mechanism is universal, named, and ABSENT from the construction M.C2 rests on.
Diff(S) ⋉ SL(2,ℝ)^S carries a(y) to a(φ(y)) — the relation between distinct
points that nothing else supplied.

**TESTED, AND THE QUOTIENT IS NOT AVAILABLE (R 1488).** diff(S) carries
NON-VANISHING NOETHER CHARGE — physical, not gauge — so one must not quotient by
it and R 1485's underdetermination stands. Had it been gauge, a(y) is a SCALAR
and the complete invariants would have been its Reeb graph, cutting the freedom
to a finite tree with real labels. Not on offer.

**WHAT IT DOES INSTEAD:** a physical symmetry with charges ORGANISES rather than
shrinks, so the corner data lies on COADJOINT ORBITS of Diff(S) ⋉ SL(2,ℝ)^S. The
freedom is relabelled — from an arbitrary positive function to a coadjoint orbit
plus a point on it, the orbit labelled by physical charges.

**★★★ THE OPEN PIECE, SCOPED (R 1489).** Do the orbit calculation WITH diff(S)
retained. Feasibility depends on d, because the corner is (d−2)-dimensional:

    d = 3   corner = S¹   ORBITS CLASSIFIED — Kirillov, Lazutkin–Pankratova,
            Goldman, Segal, Witten CMP 114 (1988) 1–53, by monodromy conjugacy
            class; completed later. **TRACTABLE — this is the item to take.**

    d = 4   corner = S²   ORBITS NOT CLASSIFIED. No Virasoro analogue for
            Diff(S²); the matrix-quantisation work uses sdiff(S²) precisely
            because of it. **BLOCKED by an open problem in the theory of
            diffeomorphism groups, not by anything physical.**

So M.C2 is closeable in three dimensions and its physical case waits on named
mathematics. That is a better statement of its openness than the project has had.

**FLAGGED, NOT CLAIMED:** Witten's orbit stabilisers are SL(2,ℝ) embeddings, and
SL(2,ℝ)^S is the ultralocal factor of the corner algebra. Same group, two roles.
R 1398 applies before anything is made of it.

**AND THE d = 4 BLOCK MAY NOT BIND (R 1490).** Mackey: coadjoint orbits of a
semidirect product need (i) an orbit of Diff(S²) on maps from S² into the 3-dimensional dual of sl(2,ℝ) —
singularity theory, not the open problem — and (ii) a coadjoint orbit of the
STABILISER, which for a GENERIC map is trivial or finite. **So generic corner
data may need no Diff(S²) coadjoint orbit at all.**

    THREE THINGS TO CHECK, IN ORDER, BEFORE RELYING ON IT:
    1. is the dual really those maps, or something else?
    2. are generic stabilisers in Diff(S²) really finite?
    3. **IS THE PHYSICAL CORNER DATA GENERIC?** Black hole horizons are famously
       NOT generic — Kerr is axisymmetric — and this is the objection most
       likely to sink the whole line. Check it FIRST if time is short.

    ~~★★ FIRST — COMPLETE THE SUM ON THE DRESSED ALGEBRA (R 1483).~~ DONE. M.ledger's
      d − 1 = 1 + (d − 2) is the FREE count; the dressed algebra carries DOUBLED
      CORNER MODES besides, and those are relative boosts AND null translations,
      so they sit in both families at once — an OVERLAP, not a summand. **Nothing
      built on the ledger can be trusted until the dressed count is written.**
      Then, and only then, the sudoku reading is testable: overlapping families
      mean SEARCH rather than propagation, which would explain eight sessions of
      resistance and say the closure operator is the wrong instrument here.

    then:
    · **the geometric action.** Does P_ρ act on the horizon algebra without a
      Killing field? Witten's sesquilinear-form argument uses only that H⁺_λ is a
      Cauchy surface for R_λ.

**★★ H3 · POPULATE Λ_spectra BY MATH EXTRACTION — M's instruction, for the
Löwdin resume.** Apply the method used at R 1560 for Bk/Cf to Λ_spectra's
unfilled cells. It worked once on an object that CANNOT be measured, and the
same five steps apply to any cell the data does not reach.

    THE METHOD, as executed and as it must be repeated:

    1. **FIND THE SOURCE'S OWN FORMULA FOR ITS OWN GAPS.** Angeli & Marinova
       supply R0 = (0.9071 + 1.105/A^(2/3) − 0.548/A^(4/3))·A^(1/3) *because
       six of their own elements lack experimental R.* Look for the analogous
       thing: what does the field use when IT cannot measure?
    2. **VALIDATE BEFORE USING.** The formula reproduced their own Cm-244 to
       0.0000 fm. Without that step the implementation is unverified and any
       prediction is a guess with decimals.
    3. **MEASURE THE SYSTEMATIC ERROR WHERE MEASUREMENT EXISTS.** It ran LOW
       by +0.0544 ± 0.0131 fm on four measured actinides. That offset IS the
       correction and the scatter IS the uncertainty. Do not adopt the
       formula's own quoted error.
    4. **FIND THE MISSING DEPENDENCE.** R0 is a function of A ALONE and gave
       Bk-249 and Cf-249 the identical value — useless for an element-specific
       cell. Regressing the residual on Z recovered 0.0060 fm per proton.
       **Ask what coordinate the borrowed formula cannot see.**
    5. **SEPARATE CONFIDENCE BY QUANTITY.** Absolutes rested on 4 points and
       2 parameters — INDICATIVE. Differences rested on 18 pairs across 5
       elements — USABLE. They were labelled differently in the same file.

    ⚠ **AND THE LABEL IS PART OF THE METHOD.** `RADII-Bk-Cf-PREDICTED.tsv`
    says *PREDICTED, NOT MEASURED. NOT A CAPTURE.* in its first line. Any
    Λ_spectra cell filled this way carries the same marking, or a later
    session will read a prediction as a measurement — which is register
    1526's fabrication fault with better arithmetic.

    **WHERE TO POINT IT:** Λ_spectra's eleven remaining cells (A2), six of
    which are G2's withdrawn Q.exch. Take H1's re-coordinatisation on
    (block, ℓ, charge) first — a cell that is empty in one coordinate system
    may be filled in another, and relabelling is free to try under A.erel.
    **Extraction is for cells that survive the relabelling.**

**★★ H1 · RE-COORDINATISE Λ_spectra ON (block, ℓ, charge)** — NEW, R 1459. The
Janet block explains 87% of δ's within-ℓ variance against a 5.5% null and δ is
monotone in block at every ℓ, so both are determined axes by the work's own rule.
Test closure on (block, ℓ, charge) against the current (Z, c, ℓ). By A.erel a
relabelling is free to try.

**✔ H2 · CLOSED (R 1460).** ν is a FORM, not a law. It orders, does not measure,
and every physical reading failed. Its gap was localised the day it was built —
R 1311, one target cell (the amplitude a) fed by two source cells the law does
not draw on, electron–electron repulsion and exchange.

---

# VI-b · PRESENTATIONAL — DEFERRED TO THE BUILD (R 1478)

*Found by the full audit of 2026-08-11. None of it touches a computation; stage 4
recomputed every figure registered today and all twenty checks passed. These are
held until the topics at hand are finished and the artefacts are being built into
the books, then done in one pass.*

**⏸ PR1 · the self-count — HELD FOR BOOK TIME (M, R 1564).** Purely
reader-facing: the front matter is GENERATED and counts HEADINGS (1,357)
where there are NUMBERS (1,386), gap 29. **No computation, audit or
round-trip consumes it.** Decide heading-vs-number when the book is written.

**✔ PR2 · KEEP THE FIVE (M, R 1564).** 663, 670, 682, 683, 1138 stay
allocated and empty. *M's reasoning: they tell the reader there is a step
there that cannot be seen from our record.* Re-verified — none has an entry,
each appears once, in the note about them.

**✔ PR3 · SOLVED BY A GLYPH (M, R 1564).** All notation asterisks are now
**U+2217 ∗ ASTERISK OPERATOR** — Unicode's mathematical asterisk, which is
what n∗ actually means. 37 replaced (14 escaped, 23 raw); **0 remain**.
Unbalanced italics fell 25 → 14. Verified against a backup: files identical
once normalised, 14 characters shorter, heading count unchanged, both gates pass.

    ⚠ **THE ESCAPE NEVER WORKED.** 4 of the 6 "correctly escaped" entries
    still read as unbalanced — the parity counter sees the asterisk whether
    or not a backslash precedes it. **PR5's audit 26 would have fired on
    them forever.** The glyph leaves nothing to count.
    → **Any script searching for the notation must search for ∗, not `n*`.**

**★ PR4 · EIGHT slips, not fourteen (R 1565).** Five of the fourteen are
NOTATION, not markup, and must never be "fixed":

    313   Λ*                        an object name
    604   (3, 0, 1, 1, *, 0, 1, 1)  THE FREE COORDINATE the entry is about
    668   `colWidths=[w]*n`         Python multiplication, in backticks
    747   ns (1/2,1/2)* J=1         spectroscopic ODD PARITY
    1003  `vi_*` set                a glob pattern, in backticks

A sixth, 1263's `3n∗²`, was an n∗ the first sweep missed (`` fails between
a digit and a letter) — now swept.

**THE EIGHT REAL SLIPS, in two kinds — M's editorial call:**

    one asterisk short of bold   277, 435
    italic section never closed  770, 789, 791, 808, 822, 846

    ⚠ **DO NOT widen the notation pattern.** Dropping `` gave 21 matches
    of which ONE was notation; the other 20 were words ending in n or h
    before a CLOSING marker ('variation*', 'prediction*'). It took the
    count 14 → 31. Reverted from backup. The rule is: **n or h NOT preceded
    by a letter.**

**★★ PR5 · AUDIT 26 · ITALIC PARITY.** Audit 12 checks bold parity only. The
check is already written, in `audit_full.py`. **Two conditions before switching
it on:**

    1. PR4's EIGHT slips swept (PR3 is done — the glyph cleared 12 of 25).
    2. **A SKIP LIST (R 1565).** Five entries are CORRECT and will fail any
       naive check — 313, 604, 668, 747, 1003 carry an asterisk as CONTENT.
       Audit 26 must skip asterisks inside backticks, inside coordinate
       tuples, and after a J-value, or it fires on good entries forever.

*Tooling in place: `audit_full.py` (structure, cross-refs, claimed corrections),
`audit_figures.py` (figures against generators, cross-artefact conflicts),
`audit_session.py` (this session's claims, recomputed from scratch). Re-run all
three before any build.*

---

# VII · THE PATH FROM HERE (R 1460, NU-DEACTIVATED.md)

**★★ P1 · THE INSTRUMENT, NOT THE FORM.** The question is no longer *what is a*
but *what other forms can the corridor eliminate*. That is the one thing this
work has done which the Löwdin literature has not: an empty feasible set refutes
a form, and no one else appears to have run the test.

**★★ P2 · FEED IT THE LITERATURE'S CANDIDATES.** Demkov–Ostrovsky's family
indexed by α; the group-theoretic orderings (Kibler, Thyssen–Ceulemans, the
SO(4,4) tower); Tangour's K(ZX) descriptor. Each posits an order; each can be
given a parameter and cornered. **Any that returns EMPTY is refuted, and that is
a publishable statement about someone else's form.**

**★★ P3 · WHY ARE THE ONSETS EXACT?** K(x) = (1/6)x(x² + 2 − 3µ(x)) reproduces
all eight Janet block openings with NO error. That is the strongest ordering
statement in this project and it is not ν's, not Belokolos's derivation, and not
ours. Ask what it is a consequence of.

**✗ P4 · DO NOT ATTEMPT A SEVENTH PLACEMENT RULE FOR a.** Six have failed —
endpoint, per-run, per-atom, transition, single fixed, group ceiling — and
register 1311 says why. A seventh needs a source in electron–electron repulsion
or exchange, or it is a seventh guess.

**✔ F2a · RUN (R 1469).** `contingency_sweep.py`, over 1.7's own findings with
each space declared before its computation. Two EARNED — the half-capacity screen
at P = 0.0038 with four witnesses, and the Madelung-exception recovery. One
correctly FORCED — the rank-one certificate is an identity, so the contingency
lies in the observed ORDER supplying both signs, not in the algebra. Two weaker
than they read: the 97-of-106 trajectory agreement sits at the 82nd percentile of
arbitrary constant pairs, and "both signs demanded" is the common case under its
null. **The sweep also found two faults in itself** — an automated verdict that
marked an identity EARNED by string-matching the witness field, and a SPACE that
dropped R 1371's spin condition. *Still owed: the same sweep over the OLDER
standing entries, which is what F2a originally meant.*

**✔ F2 · BOTH CHAPTERS WRITTEN AS DRAFTS (R 1569).** See the entry in §II.
*The standing rule — nothing written until both a target and a solution exist —
was RELAXED by M: an unfinished chapter that records where the work stands is
worth more than a finished one later.*

**★★★ F2b · THE BOOK STILL TRAILS THE REGISTER.** Highest citation 1225 against
a register at 1569 — **a gap of 344 entries.** The two drafts close the largest
topic; the gap itself remains the project's biggest debt.

---

# IV · CORRECTIONS OWED TO THE REGISTER

*Computed this session. Each states what to write.*

1. **R 1391 — n = 47, not 45.** The three region offsets reproduce exactly
   (3.798, 4.595, 5.298) and the quoted spread of **0.108 is the 47-element
   figure**; dropping any two tightens it to 0.097. The fit ran over all 47.
   Sc and Ti ARE the two largest deviations, once the L1M2,3-blended elements
   are excluded as the regions imply — 52 elements against the stated 53.

2. **R 1390 — monotone except at one step.** Endpoints exact (Ca 0.1082,
   Pb 0.2258) and the ratio never exceeds (2/3)³ = 0.2963. It falls **only at
   palladium**, 0.1756 → 0.1753. Add the exception; do not withdraw the claim.

3. **R 1401 — the four are not period openings.** Thallium 81 is not the first
   element of a period. All four DO open a subshell — Li 2s, K 4s, Tl 6p,
   Fr 7s — **but so do eight of the fourteen forced** (Rb, Cs, Ce, Gd, Pa, Cm,
   Lr, Rf), so the property is necessary and not sufficient. **The four remain
   unexplained.**

4. **R 1413 — the two extra misses are placement-caused.** The seven are
   placement-independent; per-block ascent adds B 5 and Sc 21. 106 − 9 = 97,
   106 − 7 = 99. Both figures right; the clause was missing.

5. **R 1415 — the exception counts are undercounts.** The percentages are exact
   (ceiling in own block 84/99 = 85%, floor in next block 71/80 = 89%). But
   there are **fifteen** ceiling exceptions, not eleven: eleven s-against-s as
   stated, **plus four d-against-s** — 4d→5s at Mo, Rh, Pd and 5d→6s at Au. So
   that set is NOT homogeneous. Floor exceptions are **nine**, not six, and all
   nine ARE f or d intruders, so that characterisation survives.

6. **R 1417 — seven of twenty close, not three.** The monotone-chain filter was
   applied as a stated principle rather than a computed test, so combinations
   may have been excluded on an unrecorded judgement. My landing-axis definition
   is independently validated — it is the same quantity that reproduces 1415's
   85% and 89%. Correct to seven; record that the filter is untested.

7. **R 1396 — two sets, one denominator.** The base rate reproduces exactly
   (3 of 12 = 25%, 36 of 94 = 38%) and the refutation stands. But the entry
   splits the ELEVEN absent cells six-and-five and scores against the TWELVE
   donor steps, and its "other nine" lists only seven — **Pr and Tb are
   omitted**.

8. **R 1419 — no correction; my flag is WITHDRAWN.** It reports two different
   base indexes and all four figures are right: replace runs on (n, ℓ, q),
   24 cells, box 48 → 56; adjoin runs on (n, ℓ), 18 cells, box 24 → 168. Add a
   clause naming which index each test uses.

9. **R 1409 / R 1411 — no correction; add a clause.** Seven openings counts the
   initial placement at lithium; six counts re-placements, which excludes it.
   9 matched + 6 extra = 15 moves. Both self-consistent.

10. **R 1385 — treat the eighty-five as UNVERIFIED.** No natural rule yields it;
    the nearest is eighty-six. It was a filter in code, not a recorded decision.
    The exponent 4.55, the σ scan and the +16% above Z ≥ 70 all hang on it.

11. **R 1407 — the margin is undefined.** Its ninety-nine is the **ceiling-
    bearing** set (99 of 106 steps carry a finite ceiling), not the 73 with both
    bounds finite. None of its figures reproduce from corridor widths, so the
    quantity is some other measure — most likely the distance from the HELD a to
    the nearer bound, which is trajectory-dependent. Define it or withdraw the
    r = +0.64.

12. **R 1403 / R 1409 — the eight a values are RECONSTRUCTIONS.** They were held
    in `HANDOFF.md` from earlier sessions' walk work, not measured. So both
    entries claim agreement with a previously computed trajectory, which is
    weaker than it reads. Annotate wherever cited.

13. **THE NULL OF 28 IS RETIRED.** See V·4.

---

# V · NEW, THIS SESSION — warrants registering

1. **The corridor and the object in it are ONE equation, and the placement rule
   falls out.** Intersecting corridors and asking only where the running
   intersection empties gives **fourteen forced moves, identical to R 1401,
   zero false positives**, with nothing supplied — no rule, no threshold, no
   parameter. The eight recorded values all sit on an endpoint of their own
   corridor, seven at L and Pa at U, which is R 1403 falling out of the same
   arithmetic. `balance.py`.

2. **Proximity IS the trigger — at threshold zero, on the running intersection.**
   R 1407 measured the margin per element and demoted proximity to a signal.
   Measured on the intersection a actually has to sit inside, the trigger fires
   at 14 of 18 with zero false positives, 96% against an 83% baseline. **The
   threshold is not fitted; it is zero.** So the law needs no proximity TERM:
   proximity is the strict inequality reaching equality. *This is not a tenth
   scan after nine failures — nothing was searched over.*

3. **There are eight adjacent handshakes, not four**, and they split on a
   criterion no register states. In four, BOTH members are forced resets —
   Mo/Tc, Gd/Tb, Cm/Bk, Lr/Rf, exactly R 1404's list. In four, only the second
   is — La/Ce, Eu/Gd, Th/Pa, Am/Cm. That is what "the second reset is forced and
   the two are one event" is describing. **Ac's floor, Th's floor and Pa's
   ceiling are one surd**, 1/(√3−1), which is why R 1403's "Pa takes U" and
   R 1409's "assigned at the actinium opening" name one value from two sides.

4. **The null is 96, not 28.** Plain Madelung on the same 106 clean steps:
   **96 of 106 conditional** (given the observed state at Z−1), **94
   free-running**. The 28 was a broken step extractor. So the headline is
   **99 against 96**, three steps in 106, not 99 against 28.
   **But the two are NOT nested** — Madelung misses Mo, Rh, Pd, La, Gd, Au, Ac,
   Th, Cm, Lr; the corridor misses Mn, Tc, Ce, Gd, Pa, Cm, Rf; **they overlap in
   two**. The corridor is right at eight where Madelung is wrong; Madelung at
   five where the corridor is wrong. *Two rules of near-identical accuracy
   failing on disjoint sets are different objects, which is a better statement
   than a score.* `null_madelung.py`.
   **CAVEAT: the 96 is measured here; the 99 is reported from R 1413 and is not
   verified in this tree.** Build the scorer.

5. **4β + α = 2κℏω₀(1 − 2μ), vanishing exactly at μ = ½** — the corridor
   combination collapses to one condition on Nilsson's μ. The published values
   straddle it: μ = 0.60 in the 50–82 protons gives negative, exactly the sense
   both its pairs demand; μ = 0.42 in the 82–126 neutrons gives positive, in the
   one shell demanding both. **C3's falsifier is derivable from the field's own
   parameters**, not merely consistent with them.

6. **NIST's Blend column is a MEMBERSHIP condition, not a quality annotation.**
   Where it flags L1M2,3 or KL2,3, the two files carry the *same* experimental
   value, so the experimental difference is identically zero — twelve
   manufactured zeros in the doublet, and a silently widened comparison set that
   made R 1391's Sc/Ti finding disappear until the flag was applied. *The
   separation hypothesis, in a place it had not been applied.*

7. **The 3d/4f asymmetry has a mechanism** (supplied, not derived here): the
   offset breaks at 3d and ignores 4f because 3d is inside a 3p electron's
   screening region and 4f is outside it. Converts the discriminating check from
   one that could have failed into one that had a reason not to.

8. **R 1406's sensitivity contains an inverse-square** — the gap between the two
   radicands, squared, in the denominator, with the cap beside it. **The shape
   is a fact about the algebra; identifying it with the Coulomb law is NOT
   tested** and the radicands are node counts, not distances.

---

# VI · THE RULES, AND WHAT WAS ADDED TO THEM

Read orderings from a source · don't invent a cell or column · three axes never
two · an axis is determined when its values form a monotone chain · E = 0 is
informative only where refusal was possible · never fill your own values when the
source is meant to be accurate · before calling a coordinate system new, ask
whether its axes are the parent's letters relabelled · read E as predictions, not
defects.

**Added 1.6.1:** every generator must be diff-tested against its held copy, and
any generator that writes IN PLACE must refuse partial output rather than write
it. Recorded under I, the method, as a standing rule.

**Added 1.7:** an artefact whose content exists only in a file is not durable.
Everything held only in a generated file was lost in the rollback; everything
written into a transcript as prose survived. **Anything rebuilt from a register
is labelled REWRITTEN, never restored** — see `PROVENANCE.md`.

**Recurring faults.** Reading a pattern in my own output · asserting a relation
without computing it · quoting a check before its null is known · summary
statistics over a series that turns · taking the collection's edge for the
subject's · rebuilding what the restore point already contains.

*Three of those fired this session and are recorded above: I asserted 1419 was
contradictory without computing its two base indexes; I derived Janet's block
boundaries arithmetically instead of reading them from a source; and the null of
28 was carried into a headline result after being known bad.*
