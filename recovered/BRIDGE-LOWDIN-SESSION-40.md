# BRIDGE — THE LÖWDIN SESSION 40 (2026-08-18)
Successor to BRIDGE-LOWDIN-SESSION-39.md. Bank restore-point-2_13 (R 1700) UNCHANGED. HANDOFF-39 verified 858/858.
Runtime layered 5 -> 18 -> 19..39 with .json (F38.1). Gates 1-71 at open: **71/71 BYTE-IDENTICAL to GATES-39-OPEN.log,
diff = 0 lines**, including gate 6's sec field. PT8 pass (dsum 2.78e-17 / 0 / 0); 72, 73 SKIP as filed; GATE 74 REPRODUCES
(fkscale.py FEASIBLE, interval (0.2145, 0.5298), 315 grid points) and is RECOMMENDED ADOPTED. Census open ok=269 bad=0
nopack=3; post-gate ok=272 bad=3 (derive_P{,2,3}.json, gate-1-regenerated, as s37/s38/s39). No fault at open.

## 1 · Rulings (M, s40)
(1) "What is the recalled literature?" — THE CORRECTION THAT OPENED THE SESSION. I had offered a "recalled literature
    configuration" for Z>108 with NO SOURCE ATTACHED. That is R 1351's fault exactly. Debt paid at proposal, before any
    Z>108 was run: Desclaux 1973 (ADNDT 12, 311, Z=1-120) · Fricke/Greiner/Waber 1971 (Theor. Chim. Acta 21, 235) ·
    Pyykko 2011 (PCCP 13, 161, Z<=172) · ADNDT 2016 (Z=121-138).
(2) "I agree. Continue" — THE LITERATURE IS REFUSED AS INPUT ON A CIRCULARITY GROUND, NOT A PROVENANCE-LABEL GROUND.
    All four supply energies for an ASSUMED configuration; where the assumption is stated it is Madelung ("following
    Hund rules and the Madelung prescription", ADNDT 2016). Importing any of them hands the walk the ordering the walk
    exists to produce. RECALLED-NOT-ENTERED, comparison column only, exactly as the record is treated for Z<=108.
GENERAL carried: SUBCELL=1; predictions before runs; R 1449 flags; comparison decides; no scans; no constant beyond c;
residue is not closure; T4 LAST; the n+l walk is the solution format.

## 2 · Findings (pack40)
(1) THE SELF-DRIVING CHAIN EXISTS AND RUNS. nlchain.py: config(Z+1) = config(Z) + one electron in the deepest-binding
    open channel. Reference = cation of Z carrying config(Z-1). Seed config(1)=1s (CHOSEN, declared). Record-free from
    Z=2. Runs above 108 by construction. F40.1 registered — reference built at nuclear charge Z-1 on the first build,
    caught by PC-0 on its FIRST number (Li 2s -4.5717 vs banked -0.19629), three rows purged, affects no result.
(2) PC-0 GATE 6/6 EXACT TO 5 dp. PC-1 HELD: **19/19, FIRST DIVERGENCE NONE.** The chain reproduces every OBSERVED
    ground configuration Z=2..20 with no record input. Aufbau performed, not assumed.
(3) PC-3 PARTLY FAILED and the failure found the law. |m| >= 0.05 held (min 0.05411 at Z=19); the three-smallest clause
    failed (predicted Z=19/5/13, measured Z=19/20/3). UNPREDICTED, REGISTERED — THE MARGIN LAW: m grows monotonically as
    a subshell fills and resets to minimum at each new ns opening. 2p 6/6 increasing, 3p 6/6 increasing. Sole exception
    is the 3s run, which is the row F39.2 corrupts.
(4) **THE RESULT — D(n,l) = -1/(2n^2) + Delta(n,l).** TIMING FLAG (R 1449): FINDING PRECEDES ITS PREDICTION. The
    hydrogenic reference is NOT FITTED. Delta at K: 4s -0.11649 · 4p -0.06238 · 3d -0.00251 · 4d -0.00157 · 4f 0.00000.
    At Ca: 5g 0.00000, 4f -0.00007. HIGH-l CHANNELS SIT EXACTLY ON THE HYDROGENIC VALUE — zero penetration, fully
    screened core of charge 1. The hydrogenic term is identical for all l at the same n, SO THE WHOLE l-DEPENDENCE OF
    THE ORDERING LIVES IN Delta, AND Delta IS PENETRATION. PW-6 measured rather than inferred. And the f collapse is a
    jump in Delta, not D: 4f Delta = -0.00002 at Cs, -0.33575 at Ce — zero through Z=55, then 0.336 Ha in three protons.
(5) F39.2 LOCATED. Three instances (Z=10 3p, Z=11 3p, Z=20 5d), not one. MECHANISM: in BOTH t7c_hfsr.solve_one and
    t7b_hf.solve_one, `tgt = n-l-1` is computed and NEVER USED — the eigenvalue search is a bare log-norm bracket with
    no node constraint; the check that catches it is one level up at hfc2.py:55, after the fact. STATUS CORRECTED from
    s39: it DOES affect one reported number (the Z=11 margin, overstated, computed against 3d). No entrant choice moves.

## 3 · Next chat, in order
(1) PREDICTION FILE FOR THE Delta DECOMPOSITION — owed before any further row is run on it (R 1449 timing flag, §2(4)).
    Predict Delta's l-monotonicity, its Z-dependence, and where Delta crosses so the n+l ordering flips.
(2) F39.2 REPAIR in a NEW module reimplementing the bracket with the node target ENFORCED. t7c_hfsr/t7b_hf must not be
    edited (gates 1-71 byte-identical). Comparison decides. Falsifiable target already in hand: the margin law predicts
    Na's repaired margin falls BELOW 0.09346, restoring monotone growth in the 3s run.
(3) EXTEND THE CHAIN Z=21..108. Cost measured: ~10 s/step at Z<10, ~30 s at Z~15, ~55 s at Z=20; segment cheapest-first
    and expect the heavy end near 300 s/step. First divergence is the score, not a tally (SPEC §5).
(4) THEN Z=109..120 under the s40 ruling, labels SYNTHESISED-UNMEASURED (109-118) and PREDICTED-UNSYNTHESISED (119-120),
    all rows PREDICTED-BY-FIELD. Compare against Pyykko/Desclaux/Fricke in the finding text ONLY, never into a file.
    Live target already visible: Pyykko's DF order 8s < 5g <= 8p1/2 < 6f < 7d puts 8p1/2 AHEAD of 6f and 7d, violating
    the lower-n tie-break at n+l=9 — the same direction as s39's K, Cs, Fr violations, on an independent field.
(5) The f-collapse trace Cs->Ba->La->Ce, run on Delta. (6) PV-3 frozen-vs-relaxed, still untested.
(7) Reverse derivation to Schrodinger — the light end is now anchored 19/19 except the F39.2 hole. (8) T4 LAST: R 1701-1966.

## 4 · Figures (§H.6) MEASURED: none entered. RECALLED-NOT-ENTERED: record ground configurations Z=2..20 (comparison
column); Desclaux/Fricke/Pyykko/ADNDT-2016 (comparison in finding text only, no value in any file). CHOSEN: seed
config(1)=1s; candidate rule (n<=N+1, l<=min(n-1,4)); grid/tolerance 4000 pts 2e-5; qtail 1/2; HF maxit 100; frozen
avg-of-config (bound NOT measured). DERIVED: rest, including the hydrogenic reference -1/(2n^2), which is arithmetic.

## 5 · Files (pack40): SPEC-CHAIN · PREDICTION-CHAIN-LIGHT · FINDING-CHAIN · TABLE-CHAIN · nlchain.py · nlchain.jsonl ·
this bridge · CENSUS-SESSION-40-{OPEN,POSTGATE} · GATES-40-OPEN.log. GATE 75 proposed: `python3 nlchain.py show` ->
chained score 19/19, FIRST DIVERGENCE none, ~0 s (reads nlchain.jsonl).

## 6 · Unread / owed: unchanged (R 1668; Dabo 2010, Borghi 2014; 2603.23283; Gruneis-Kresse 2009 / Ren 2013). Owed: T4;
PR3; PN-3; La 4f+corr; PN4 s' channels; PV-3; and NEW — the Delta prediction file, the F39.2 repair module.
Known: bash egress DENIES network; web_search/web_fetch DO work (that is how the s40 source debt was paid).
Known: ground.py caps at Z=108 — that is the COLLECTION's limit, not the subject's (R 1426); 109-118 exist and are
unmeasured. Known: nlchain.py's reference is the previous NEUTRAL's configuration on the CURRENT nucleus (F40.1).
